# AGENTS.md

## Purpose

This repository defines and maintains the `avalonia-app-development` skill.

Primary goals:
- keep guidance accurate to the pinned Avalonia release,
- provide practical app-development references (not framework-internals docs),
- maintain clear navigation across `SKILL.md`, `README.md`, and `references/`.

## Source of Truth

Use these files in this order:
1. `SKILL.md` (execution workflow and default behavior)
2. `references/compendium.md` (reference index and task navigation)
3. `references/00-api-map.md` (curated app-facing API map)
4. `references/api-index-generated.md` (broad signature lookup)

If they conflict, align all docs to the pinned version and update the conflicting files.

## Version Pinning

- Target Avalonia version: `11.3.12`
- Do not introduce guidance that depends on Avalonia `master` unless explicitly requested.
- Keep version statements in top-level docs (`README.md`, optionally `SKILL.md`), not repeated in every reference file.

Regenerate API index with pinned ref:

```bash
python3 scripts/generate_api_index.py \
  --repo <path-to-avalonia-repo> \
  --git-ref 11.3.12 \
  --output references/api-index-generated.md
```

## Reference Authoring Rules

- Reference docs live under the `references/` folder using `NN-topic-name` filename patterns.
- Keep numbering and filenames stable and sequential.
- When adding/renaming a reference, update all of:
  - `references/compendium.md`
  - `SKILL.md` workflow links
  - `README.md` coverage/scope sections when relevant
- Prefer relative paths in docs and examples inside this repo.
- Keep content app-development-focused; avoid low-value API tail coverage unless needed for practical usage.

## Reference Content Standard

Each new or expanded reference should include:
- clear scope and primary APIs,
- realistic XAML and/or C# examples,
- AOT/trimming notes where relevant,
- practical do/don't guidance,
- troubleshooting or edge-case notes for common mistakes.

Default guidance bias:
- compiled bindings + `x:DataType`,
- XAML-first patterns unless user requests code-only,
- explicit UI-thread and dispatcher behavior for async/reactive flows.

## API Coverage Workflow

Use coverage tooling after significant reference updates.

1. Recompute gaps:

```bash
python3 scripts/find_uncovered_apis.py --output plan/api-coverage-not-covered.md
```

2. Run parser tests:

```bash
python3 -m unittest scripts.test_find_uncovered_apis
```

3. Refresh planning/report docs as needed:
- `plan/api-coverage-detailed-report.md`
- `plan/api-coverage-reference-update-plan.md`

Coverage target is practical completeness for app development, not 100% signature parity.

## Change Review Checklist

Before finalizing changes:
1. Verify numbering consistency between reference filenames and `references/compendium.md`.
2. Verify new docs are linked from `SKILL.md` workflow sections.
3. Verify examples use APIs available in Avalonia `11.3.12`.
4. Re-run coverage script when API-focused docs changed.
5. Ensure no accidental drift to `master`-only APIs.

## Commits

- Keep commits granular and topic-based (one logical change set per commit).
- Avoid mixing script changes, coverage artifacts, and large doc rewrites in a single commit when separable.
