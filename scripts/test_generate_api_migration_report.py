import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.generate_api_migration_report import (
    ApiItem,
    build_added_api_section,
    extract_api_items,
    main,
    normalize_target_name,
    parse_suppressions,
)
from scripts.generate_api_index import extract_signatures


class GenerateApiMigrationReportTests(unittest.TestCase):
    def test_normalize_target_name_drops_target_prefix(self) -> None:
        self.assertEqual(
            normalize_target_name("M:Avalonia.Controls.Window.Show"),
            "Avalonia.Controls.Window.Show",
        )

    def test_parse_suppressions_dedupes_across_framework_entries(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            api_dir = Path(temp_dir)
            path = api_dir / "Avalonia.nupkg.xml"
            path.write_text(
                textwrap.dedent(
                    """\
                    <?xml version="1.0" encoding="utf-8"?>
                    <Suppressions>
                      <Suppression>
                        <DiagnosticId>CP0002</DiagnosticId>
                        <Target>M:Avalonia.Controls.Window.Show</Target>
                        <Left>baseline/Avalonia/lib/net8.0/Avalonia.Controls.dll</Left>
                        <Right>current/Avalonia/lib/net8.0/Avalonia.Controls.dll</Right>
                      </Suppression>
                      <Suppression>
                        <DiagnosticId>CP0002</DiagnosticId>
                        <Target>M:Avalonia.Controls.Window.Show</Target>
                        <Left>baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll</Left>
                        <Right>current/Avalonia/lib/net10.0/Avalonia.Controls.dll</Right>
                      </Suppression>
                    </Suppressions>
                    """
                ),
                encoding="utf-8",
            )

            entries = parse_suppressions(api_dir)

        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].package, "Avalonia")
        self.assertEqual(entries[0].diagnostic_id, "CP0002")
        self.assertEqual(entries[0].target, "M:Avalonia.Controls.Window.Show")

    def test_build_added_api_section_formats_container_separately(self) -> None:
        lines = build_added_api_section(
            "Added Public APIs",
            [
                ApiItem(
                    area="Application Model and Controls",
                    source_file="src/Avalonia.Controls/AppBuilder.cs",
                    namespace="Avalonia.Controls",
                    container="AppBuilder",
                    kind="member",
                    symbol="TextShapingSubsystemName",
                    signature="public string? TextShapingSubsystemName { get; private set; }",
                )
            ],
        )

        self.assertIn(
            "- `AppBuilder` -> `public string? TextShapingSubsystemName { get; private set; }`",
            lines,
        )

    def test_extract_api_items_includes_implicit_interface_members(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo = Path(temp_dir)
            path = repo / "src" / "Sample.cs"
            path.parent.mkdir(parents=True)
            path.write_text(
                textwrap.dedent(
                    """\
                    namespace Sample;

                    public interface IFoo
                    {
                        void Execute();
                        string Name { get; }
                        event EventHandler? Changed;
                        private void Hidden() { }
                    }
                    """
                ),
                encoding="utf-8",
            )

            items = extract_api_items(repo, path)

        signatures = {item.signature for item in items}
        self.assertIn("void Execute();", signatures)
        self.assertIn("string Name { get; }", signatures)
        self.assertIn("event EventHandler? Changed;", signatures)
        self.assertNotIn("private void Hidden() { }", signatures)

    def test_extract_signatures_includes_implicit_interface_members(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "Sample.cs"
            path.write_text(
                textwrap.dedent(
                    """\
                    namespace Sample;

                    public interface IFoo
                    {
                        void Execute();
                        string Name { get; }
                    }
                    """
                ),
                encoding="utf-8",
            )

            _, signatures = extract_signatures(path)

        self.assertIn("void Execute();", signatures)
        self.assertIn("string Name { get; }", signatures)

    def test_extract_signatures_skips_interface_closing_brace_as_member_start(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "Sample.cs"
            path.write_text(
                textwrap.dedent(
                    """\
                    namespace Sample;

                    public interface IFoo
                    {
                        void Execute();
                    }

                    public class Bar
                    {
                        public void Run() { }
                    }
                    """
                ),
                encoding="utf-8",
            )

            _, signatures = extract_signatures(path)

        self.assertNotIn("} public class Bar {", signatures)
        self.assertIn("public class Bar", signatures)
        self.assertIn("public void Run() { }", signatures)

    def test_extract_api_items_skips_interface_closing_brace_as_member_start(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo = Path(temp_dir)
            path = repo / "src" / "Sample.cs"
            path.parent.mkdir(parents=True)
            path.write_text(
                textwrap.dedent(
                    """\
                    namespace Sample;

                    public interface IFoo
                    {
                        void Execute();
                    }

                    public static class FeatureExtensions
                    {
                        public static void Run() { }
                    }
                    """
                ),
                encoding="utf-8",
            )

            items = extract_api_items(repo, path)

        signatures = {item.signature for item in items}
        self.assertFalse(any(signature.startswith("} ") for signature in signatures))
        self.assertIn("public static class FeatureExtensions {", signatures)
        self.assertIn("public static void Run() { }", signatures)

    def test_main_cleans_up_first_worktree_if_second_ref_setup_fails(self) -> None:
        cleanup_calls: list[str] = []

        def cleanup_first() -> None:
            cleanup_calls.append("from")

        with tempfile.TemporaryDirectory() as temp_dir:
            repo = Path(temp_dir)
            output = repo / "report.md"

            argv = [
                "generate_api_migration_report.py",
                "--repo",
                str(repo),
                "--from-ref",
                "good-ref",
                "--to-ref",
                "bad-ref",
                "--output",
                str(output),
            ]

            with (
                patch.object(sys, "argv", argv),
                patch(
                    "scripts.generate_api_migration_report.prepare_scan_repo",
                    side_effect=[
                        (repo, "good-ref", cleanup_first),
                        RuntimeError("unknown ref: bad-ref"),
                    ],
                ),
            ):
                exit_code = main()

        self.assertEqual(exit_code, 4)
        self.assertEqual(cleanup_calls, ["from"])


if __name__ == "__main__":
    unittest.main()
