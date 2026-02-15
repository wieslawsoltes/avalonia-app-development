# Avalonia App Development Skill

Comprehensive Codex skill for building, reviewing, migrating, and optimizing Avalonia applications with modern XAML/C# patterns, compiled bindings, and AOT-friendly architecture.

## Skill Identity

- Skill name: `avalonia-app-development`
- Primary definition: `SKILL.md`
- Main reference index: `references/compendium.md`
- Avalonia upstream repository: [AvaloniaUI/Avalonia](https://github.com/AvaloniaUI/Avalonia)

## Avalonia Version Coverage

This skill is currently pinned to Avalonia **11.3.12**.

- API references and guidance are aligned to `11.3.12` behavior.
- Generated API indexing is expected to use `--git-ref 11.3.12`.
- Guidance should avoid relying on `master`-only APIs unless a document explicitly states that exception.

As of **February 15, 2026**, this repository is maintained against the 11.3.12 release line.

## Scope

This skill covers app-development-facing Avalonia topics, including:

- App startup and lifetime wiring (desktop, single-view, activity hooks)
- XAML compilation and runtime loading patterns
- Compiled bindings, typed templates, and data/template composition
- Styling, theming, resources, and asset packaging
- Controls, templates, input/focus, layout, rendering, and animation
- Platform services (storage provider, clipboard, launcher, drag/drop, screens)
- Diagnostics, performance, testing, accessibility, and troubleshooting

It includes both curated guidance and a generated API index for signature lookup.

## Out of Scope

This skill is not intended to be:

- A full Avalonia internals/source-contributor guide
- A replacement for upstream API docs or source browsing
- A mandate to use unstable/private APIs in production code

When internals are mentioned, it is usually for diagnostics, constraints, or behavioral explanation.

## Repository Structure

- `SKILL.md`
  - Skill entrypoint and execution rules
- `references/`
  - Numbered, topic-focused reference documents
- `references/compendium.md`
  - Top-level table of contents and task-oriented navigation
- `references/api-index-generated.md`
  - Broad generated API signature index
- `scripts/generate_api_index.py`
  - API index generator script
- `assets/`
  - Supporting skill assets/templates
- `agents/`
  - Agent-specific instructions/context files

## How to Use the Skill

1. Start from `SKILL.md`.
2. Follow the workflow sections to load only the references needed for the current task.
3. Use `references/compendium.md` for fast navigation.
4. Use `references/api-index-generated.md` when exact public signatures are required.

## XAML and API Coverage Notes

Recent additions include focused references for:

- XAML compiler/build pipeline
- Runtime XAML loader and dynamic loading
- XAML in libraries and resource packaging
- Runtime XAML manipulation and service-provider patterns
- Visual tree and logical tree inspection/traversal
- Data templates and `IDataTemplate` selector patterns
- Path icons, adorners, and shapes

These are designed to reduce accidental drift to unreleased APIs.

## Regenerating API Index (Pinned)

```bash
python3 scripts/generate_api_index.py \
  --repo <path-to-avalonia-repo> \
  --git-ref 11.3.12 \
  --output references/api-index-generated.md
```

Recommended checks after regeneration:

- Verify key startup/binding/platform signatures still match references.
- Audit docs for master-only APIs introduced by mistake.
- Update this README and `SKILL.md` if version coverage changes.

## Maintenance Checklist for New Avalonia Release

1. Switch target release tag (for example `11.3.x` -> `11.4.x`).
2. Regenerate `api-index-generated.md` from the new tag.
3. Diff critical APIs referenced by docs.
4. Update affected reference files.
5. Update:
   - `README.md`
   - `SKILL.md`
   - `references/compendium.md`

## Quality Bar

Skill guidance should remain:

- Version-accurate to the declared release
- Explicit about tradeoffs (trim/AOT/runtime dynamic paths)
- Focused on production-safe defaults (compiled XAML + compiled bindings)
- Structured for rapid task execution and review
