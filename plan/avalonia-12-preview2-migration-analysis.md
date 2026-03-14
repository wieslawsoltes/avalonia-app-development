# Avalonia 12.0.0-preview2 Migration Analysis

## Verification

- verification date: `2026-03-14`
- stable repository pin preserved: `11.3.12`
- latest upstream preview tag verified: `12.0.0-preview2`
- preview release date: `2026-03-05`

## Methodology

This migration lane uses two complementary sources from the Avalonia source tree:

1. official package-validation suppressions under `/api`
- treated as the authoritative list of approved package-surface breaking changes.

2. source-level public API scan under `src/**/*.cs`
- used to enumerate newly added public signatures and generate the preview API index.

Generated artifacts for this update:

- [`../references/69-avalonia-12-preview2-breaking-changes-and-new-api-catalog.md`](../references/69-avalonia-12-preview2-breaking-changes-and-new-api-catalog.md)
- [`../references/api-index-12.0.0-preview2-generated.md`](../references/api-index-12.0.0-preview2-generated.md)

## Quantitative Summary

- official compatibility suppressions: `536`
- added public signatures in preview2: `1041`
- removed public signatures in parser view: `812`
- preview public signatures indexed: `11173`

Breaking-change suppressions by package:

- `Avalonia`: `499`
- `Avalonia.Android`: `6`
- `Avalonia.Headless`: `3`
- `Avalonia.Headless.XUnit`: `6`
- `Avalonia.LinuxFramebuffer`: `3`
- `Avalonia.Skia`: `15`
- `Avalonia.Win32.Interoperability`: `2`
- `Avalonia.X11`: `2`

New public signatures by major area:

- `Application Model and Controls`: `496`
- `Property, Data, Styling, Threading`: `388`
- `XAML and Markup`: `15`
- `Rendering and Text`: `10`
- `Headless Platform`: `8`
- `Linux Framebuffer`: `7`
- the remainder is spread across Android, iOS, X11, Windows, macOS native, source-generator, and other support areas.

## Main Migration Themes

### Binding and metadata relocation

Preview2 moves binding-facing types deeper into `Avalonia.Base` / `Avalonia.Data` / `Avalonia.Metadata` and removes older convenience constructors. This is one of the highest compile-break clusters for application code and helper libraries.

### Build defaults changed, not just APIs

`AvaloniaUseCompiledBindingsByDefault` is now `true`. That changes the migration profile because many `11.3.12` views that silently used reflection can now fail in the XAML compiler until `x:DataType` and typed binding paths are added.

### Platform service modernization

The public surface moved away from the old dialog and `IDataObject` stack toward storage-provider and data-transfer APIs. App code that still used `OpenFileDialog`, `SaveFileDialog`, or `IDataObject` needs deliberate migration, not mechanical renames.

### Window/root architecture split

`TopLevel` no longer carries the same public root responsibilities, and preview2 introduces `IPresentationSource` plus additional window-decoration infrastructure. Apps with custom chrome, hosted visuals, or low-level root assumptions need focused runtime verification.

### Android bootstrap rewrite

The generic `AvaloniaMainActivity<TApp>` path is gone. Android startup is now application-first with `AvaloniaAndroidApplication<TApp>` plus a plain `AvaloniaMainActivity`. This is a hard migration requirement for Android targets.

### Large new feature surfaces

Preview2 adds substantial new API families rather than only replacement APIs:

- page-based navigation (`Page`, `ContentPage`, `DrawerPage`, `NavigationPage`, `TabbedPage`),
- command bar controls (`CommandBar`, `AppBarButton`, `AppBarToggleButton`),
- code-first compiled bindings (`CompiledBinding.Create`),
- dispatcher ownership helpers,
- text rendering split via `TextOptions`,
- swipe gestures and modern chrome roles.

## Hard Limits

This lane is exhaustive for:

- approved breaking changes represented in Avalonia's package-validation suppressions,
- public signature additions captured by the source parser and preview index generator.

This lane is not a guarantee for:

- undocumented behavioral changes that do not appear in suppressions or public signatures,
- platform-specific regressions that only appear under runtime device conditions,
- private or internal framework changes that affect applications indirectly.

For that reason, the migration guide pairs the generated inventories with explicit runtime verification steps.
