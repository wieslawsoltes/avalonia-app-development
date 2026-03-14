#!/usr/bin/env python3
"""Generate a version-to-version Avalonia migration report.

The report combines two complementary sources:
- official API-compat suppressions from Avalonia's `api/*.xml` files for breaking changes,
- a source-level public API signature diff for newly added public APIs.

This keeps the migration lane readable while still being backed by reproducible source data.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import datetime as dt
from dataclasses import dataclass
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.find_uncovered_apis import parse_signature
from scripts.generate_api_index import (
    NAMESPACE_RE,
    PUBLIC_RE,
    area_for,
    declaration_terminated,
    normalize_signature,
    prepare_scan_repo,
    resolve_files,
    sanitize_for_braces,
    strip_comments,
)

DEFAULT_PATTERNS = ["src/**/*.cs"]
TYPE_START_RE = re.compile(
    r"^\s*(public|internal|private|protected)\s+"
    r"(?:new\s+|unsafe\s+|abstract\s+|sealed\s+|static\s+|partial\s+|readonly\s+|ref\s+)*"
    r"(class|interface|struct|enum|record(?:\s+class|\s+struct)?)\b"
)
DELEGATE_START_RE = re.compile(
    r"^\s*(public|internal|private|protected)\s+"
    r"(?:new\s+|unsafe\s+|static\s+|partial\s+|readonly\s+|ref\s+)*delegate\b"
)
ACCESS_MODIFIER_RE = re.compile(r"^\s*(public|internal|private|protected)\b")
DECLARATION_START_RE = re.compile(
    r"^\s*(?:"
    r"event\b|"
    r"static\b|"
    r"abstract\b|"
    r"sealed\b|"
    r"partial\b|"
    r"delegate\b|"
    r"new\b|"
    r"unsafe\b|"
    r"readonly\b|"
    r"ref\b|"
    r"[A-Za-z_@]"
    r")"
)
TARGET_KIND_LABELS = {
    "T": "type",
    "M": "method/member",
    "P": "property",
    "F": "field",
    "E": "event",
}
DIAGNOSTIC_LABELS = {
    "CP0001": "missing public type",
    "CP0002": "missing public member",
    "CP0006": "new interface member without default implementation",
    "CP0007": "removed base type",
    "CP0008": "removed base interface",
    "CP0009": "type became sealed",
    "CP0012": "member lost virtual/abstract",
}


@dataclass(frozen=True)
class TypeScope:
    name: str
    is_public: bool
    is_interface: bool
    brace_depth: int


@dataclass(frozen=True)
class ApiItem:
    area: str
    source_file: str
    namespace: str | None
    container: str | None
    kind: str
    symbol: str
    signature: str

    @property
    def identity(self) -> tuple[str | None, str | None, str, str]:
        return (self.namespace, self.container, self.kind, self.symbol)

    @property
    def unique_key(self) -> tuple[str | None, str | None, str]:
        return (self.namespace, self.container, self.signature)


@dataclass(frozen=True)
class SuppressionEntry:
    package: str
    diagnostic_id: str
    target: str
    left: str
    right: str

    @property
    def target_kind(self) -> str:
        prefix = self.target.split(":", 1)[0]
        return TARGET_KIND_LABELS.get(prefix, "symbol")


def normalize_package_name(path: pathlib.Path) -> str:
    return path.name.replace(".nupkg.xml", "")


def normalize_target_name(target: str) -> str:
    if ":" not in target:
        return target
    _, name = target.split(":", 1)
    return name


def parse_suppressions(api_dir: pathlib.Path) -> list[SuppressionEntry]:
    entries: list[SuppressionEntry] = []

    for path in sorted(api_dir.glob("*.xml")):
        package = normalize_package_name(path)
        root = ET.fromstring(path.read_text(encoding="utf-8"))

        for node in root.findall("Suppression"):
            diagnostic_id = (node.findtext("DiagnosticId") or "").strip()
            target = (node.findtext("Target") or "").strip()
            left = (node.findtext("Left") or "").strip()
            right = (node.findtext("Right") or "").strip()

            if not diagnostic_id or not target:
                continue

            entries.append(
                SuppressionEntry(
                    package=package,
                    diagnostic_id=diagnostic_id,
                    target=target,
                    left=left,
                    right=right,
                )
            )

    deduped: list[SuppressionEntry] = []
    seen: set[tuple[str, str, str]] = set()

    for entry in entries:
        key = (entry.package, entry.diagnostic_id, entry.target)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(entry)

    return deduped


def append_api_item(
    items: list[ApiItem],
    repo: pathlib.Path,
    path: pathlib.Path,
    namespace: str | None,
    container: str | None,
    signature: str,
) -> None:
    kind, symbol = parse_signature(signature)
    if not symbol:
        return

    rel = path.relative_to(repo).as_posix()
    items.append(
        ApiItem(
            area=area_for(rel),
            source_file=rel,
            namespace=namespace,
            container=container,
            kind=kind,
            symbol=symbol,
            signature=signature,
        )
    )


def is_implicit_interface_member_start(line: str, stripped: str, scope: TypeScope | None) -> bool:
    if scope is None or not (scope.is_public and scope.is_interface):
        return False
    if stripped.startswith(("[", "}", "#")) or stripped.startswith("public:"):
        return False
    return ACCESS_MODIFIER_RE.match(line) is None and DECLARATION_START_RE.match(line) is not None


def extract_api_items(repo: pathlib.Path, path: pathlib.Path) -> list[ApiItem]:
    items: list[ApiItem] = []
    namespace: str | None = None
    in_block = False
    depth = 0
    type_stack: list[TypeScope] = []
    pending_type: dict[str, object] | None = None
    pending_sig: dict[str, object] | None = None

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return items

    for raw in lines:
        line, in_block = strip_comments(raw, in_block)
        if not line.strip():
            continue

        ns_match = NAMESPACE_RE.match(line)
        if ns_match:
            namespace = ns_match.group(1)

        clean = sanitize_for_braces(line)
        stripped = line.lstrip()

        if pending_type is not None:
            pending_type["parts"].append(line)
            pending_type["clean_parts"].append(clean)

            if "{" in clean or ";" in clean:
                combined = normalize_signature(" ".join(pending_type["parts"]))
                access = str(pending_type["access"])
                parent_public = type_stack[-1].is_public if type_stack else True
                is_public = access == "public" and parent_public
                namespace_at_start = pending_type["namespace"]
                container_names = pending_type["container"]
                container = ".".join(container_names) if container_names else None

                if is_public:
                    append_api_item(
                        items,
                        repo,
                        path,
                        namespace_at_start,
                        container,
                        combined,
                    )

                kind, symbol = parse_signature(combined)
                if kind == "type" and "{" in clean:
                    type_stack.append(
                        TypeScope(
                            name=symbol,
                            is_public=is_public,
                            is_interface=bool(type_start and type_start.group(2) == "interface"),
                            brace_depth=depth + 1,
                        )
                    )
                pending_type = None
        else:
            type_start = TYPE_START_RE.match(line)
            delegate_start = DELEGATE_START_RE.match(line)

            if type_start or delegate_start:
                access = (type_start or delegate_start).group(1)
                is_interface = bool(type_start and type_start.group(2) == "interface")
                pending_type = {
                    "access": access,
                    "is_interface": is_interface,
                    "parts": [line],
                    "clean_parts": [clean],
                    "namespace": namespace,
                    "container": tuple(scope.name for scope in type_stack if scope.is_public),
                }

                if "{" in clean or ";" in clean:
                    combined = normalize_signature(" ".join(pending_type["parts"]))
                    access = str(pending_type["access"])
                    parent_public = type_stack[-1].is_public if type_stack else True
                    is_public = access == "public" and parent_public
                    namespace_at_start = pending_type["namespace"]
                    container_names = pending_type["container"]
                    container = ".".join(container_names) if container_names else None

                    if is_public:
                        append_api_item(
                            items,
                            repo,
                            path,
                            namespace_at_start,
                            container,
                            combined,
                        )

                    kind, symbol = parse_signature(combined)
                    if kind == "type" and "{" in clean:
                        type_stack.append(
                            TypeScope(
                                name=symbol,
                                is_public=is_public,
                                is_interface=bool(pending_type["is_interface"]),
                                brace_depth=depth + 1,
                            )
                        )
                    pending_type = None
            else:
                current_scope = type_stack[-1] if type_stack else None
                innermost_public = current_scope.is_public if current_scope else False
                member_depth = current_scope.brace_depth if current_scope else -1

                if pending_sig is None:
                    if (
                        innermost_public
                        and depth == member_depth
                        and (PUBLIC_RE.match(line) or is_implicit_interface_member_start(line, stripped, current_scope))
                        and not stripped.startswith("public:")
                    ):
                        container_names = tuple(scope.name for scope in type_stack if scope.is_public)
                        pending_sig = {
                            "parts": [line],
                            "namespace": namespace,
                            "container": container_names,
                        }
                        combined = normalize_signature(line)
                        if declaration_terminated(combined):
                            append_api_item(
                                items,
                                repo,
                                path,
                                pending_sig["namespace"],
                                ".".join(pending_sig["container"]) if pending_sig["container"] else None,
                                combined,
                            )
                            pending_sig = None
                else:
                    pending_sig["parts"].append(line)
                    combined = normalize_signature(" ".join(pending_sig["parts"]))
                    if declaration_terminated(combined):
                        append_api_item(
                            items,
                            repo,
                            path,
                            pending_sig["namespace"],
                            ".".join(pending_sig["container"]) if pending_sig["container"] else None,
                            combined,
                        )
                        pending_sig = None

        depth += clean.count("{")
        depth -= clean.count("}")

        while type_stack and depth < type_stack[-1].brace_depth:
            type_stack.pop()

    if pending_sig is not None:
        append_api_item(
            items,
            repo,
            path,
            pending_sig["namespace"],
            ".".join(pending_sig["container"]) if pending_sig["container"] else None,
            normalize_signature(" ".join(pending_sig["parts"])),
        )

    return items


def scan_api_items(repo: pathlib.Path) -> list[ApiItem]:
    items: list[ApiItem] = []
    for path in resolve_files(repo, DEFAULT_PATTERNS):
        items.extend(extract_api_items(repo, path))

    deduped: list[ApiItem] = []
    seen: set[tuple[str | None, str | None, str]] = set()
    for item in items:
        key = item.unique_key
        if key in seen:
            continue
        seen.add(key)
        deduped.append(item)
    return deduped


def diff_added_items(old_items: list[ApiItem], new_items: list[ApiItem]) -> list[ApiItem]:
    old_keys = {item.unique_key for item in old_items}
    return [item for item in new_items if item.unique_key not in old_keys]


def diff_removed_items(old_items: list[ApiItem], new_items: list[ApiItem]) -> list[ApiItem]:
    new_keys = {item.unique_key for item in new_items}
    return [item for item in old_items if item.unique_key not in new_keys]


def build_breaking_summary(entries: list[SuppressionEntry]) -> list[str]:
    lines: list[str] = []
    package_counts = Counter(entry.package for entry in entries)
    diagnostic_counts = Counter(entry.diagnostic_id for entry in entries)

    lines.append("## Breaking Change Summary")
    lines.append("")
    lines.append("Official breaking-change source: Avalonia `api/*.xml` package-validation suppressions.")
    lines.append("")
    lines.append(f"- Unique approved compatibility suppressions: `{len(entries)}`")
    lines.append("")
    lines.append("### By Package")
    lines.append("")
    for package, count in sorted(package_counts.items()):
        lines.append(f"- `{package}`: `{count}`")
    lines.append("")
    lines.append("### By Diagnostic")
    lines.append("")
    for diagnostic_id, count in sorted(diagnostic_counts.items()):
        label = DIAGNOSTIC_LABELS.get(diagnostic_id, "other compatibility change")
        lines.append(f"- `{diagnostic_id}` ({label}): `{count}`")
    lines.append("")

    grouped: dict[str, dict[str, list[SuppressionEntry]]] = defaultdict(lambda: defaultdict(list))
    for entry in entries:
        grouped[entry.package][entry.diagnostic_id].append(entry)

    for package in sorted(grouped.keys()):
        lines.append(f"## Breaking Changes: `{package}`")
        lines.append("")
        for diagnostic_id in sorted(grouped[package].keys()):
            label = DIAGNOSTIC_LABELS.get(diagnostic_id, "other compatibility change")
            lines.append(f"### `{diagnostic_id}`: {label}")
            lines.append("")
            for entry in sorted(grouped[package][diagnostic_id], key=lambda item: item.target):
                lines.append(
                    f"- `{normalize_target_name(entry.target)}` "
                    f"({entry.target_kind}; baseline `{entry.left}` -> current `{entry.right}`)"
                )
            lines.append("")

    return lines


def build_added_api_section(title: str, items: list[ApiItem]) -> list[str]:
    lines: list[str] = []
    area_counts = Counter(item.area for item in items)
    kind_counts = Counter(item.kind for item in items)
    items_by_area: dict[str, dict[str, list[ApiItem]]] = defaultdict(lambda: defaultdict(list))

    for item in items:
        items_by_area[item.area][item.source_file].append(item)

    lines.append(f"## {title}")
    lines.append("")
    lines.append(f"- Public signatures: `{len(items)}`")
    lines.append("")
    lines.append("### By Area")
    lines.append("")
    for area, count in sorted(area_counts.items()):
        lines.append(f"- `{area}`: `{count}`")
    lines.append("")
    lines.append("### By Kind")
    lines.append("")
    for kind, count in sorted(kind_counts.items()):
        lines.append(f"- `{kind}`: `{count}`")
    lines.append("")

    for area in sorted(items_by_area.keys()):
        lines.append(f"### {area}")
        lines.append("")
        for source_file in sorted(items_by_area[area].keys()):
            lines.append(f"#### `{source_file}`")
            lines.append("")
            namespaces = sorted({item.namespace for item in items_by_area[area][source_file] if item.namespace})
            if namespaces:
                lines.append(f"- Namespace(s): `{', '.join(namespaces)}`")
            for item in sorted(items_by_area[area][source_file], key=lambda current: current.signature):
                if item.container:
                    lines.append(f"- `{item.container}` -> `{item.signature}`")
                else:
                    lines.append(f"- `{item.signature}`")
            lines.append("")

    return lines


def write_report(
    output: pathlib.Path,
    repo: pathlib.Path,
    from_ref: str,
    to_ref: str,
    suppressions: list[SuppressionEntry],
    added_items: list[ApiItem],
    removed_items: list[ApiItem],
) -> None:
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    lines: list[str] = []
    lines.append("# Avalonia Migration Report (Generated)")
    lines.append("")
    lines.append(f"- Generated at (UTC): `{now}`")
    lines.append(f"- Repository: `{repo}`")
    lines.append(f"- From ref: `{from_ref}`")
    lines.append(f"- To ref: `{to_ref}`")
    lines.append("")
    lines.append("## Coverage Contract")
    lines.append("")
    lines.append("- Breaking changes come from Avalonia's checked-in package-validation suppression files under `api/*.xml`.")
    lines.append("- Added public APIs come from a source-level scan of public signatures under `src/**/*.cs`.")
    lines.append("- Removed public signatures are included as an auxiliary parser-based view; treat the suppression-backed section as the official breaking-change list for shipped packages.")
    lines.append("")

    lines.extend(build_breaking_summary(suppressions))
    lines.extend(build_added_api_section("Added Public APIs", added_items))
    lines.extend(build_added_api_section("Removed Public Signatures (Parser View)", removed_items))

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate an Avalonia migration report.")
    parser.add_argument("--repo", required=True, help="Path to Avalonia repository root.")
    parser.add_argument("--from-ref", required=True, help="Baseline ref, tag, or commit.")
    parser.add_argument("--to-ref", required=True, help="Target ref, tag, or commit.")
    parser.add_argument("--output", required=True, help="Output markdown path.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    repo = pathlib.Path(args.repo).expanduser().resolve()
    output = pathlib.Path(args.output).expanduser().resolve()

    if not repo.exists() or not repo.is_dir():
        print(f"error: invalid repo path: {repo}", file=sys.stderr)
        return 2

    from_cleanup = lambda: None
    to_cleanup = lambda: None

    try:
        from_repo, _, from_cleanup = prepare_scan_repo(repo, args.from_ref)
        to_repo, _, to_cleanup = prepare_scan_repo(repo, args.to_ref)
    except RuntimeError as ex:
        from_cleanup()
        to_cleanup()
        print(f"error: {ex}", file=sys.stderr)
        return 4

    try:
        api_dir = to_repo / "api"
        if not api_dir.is_dir():
            print(f"error: expected suppression directory at {api_dir}", file=sys.stderr)
            return 3

        suppressions = parse_suppressions(api_dir)
        old_items = scan_api_items(from_repo)
        new_items = scan_api_items(to_repo)
        added_items = diff_added_items(old_items, new_items)
        removed_items = diff_removed_items(old_items, new_items)
        write_report(
            output,
            repo,
            args.from_ref,
            args.to_ref,
            suppressions,
            added_items,
            removed_items,
        )
        print(
            f"Wrote {output} "
            f"({len(suppressions)} suppressions, {len(added_items)} added signatures, {len(removed_items)} removed signatures)"
        )
        return 0
    finally:
        from_cleanup()
        to_cleanup()


if __name__ == "__main__":
    raise SystemExit(main())
