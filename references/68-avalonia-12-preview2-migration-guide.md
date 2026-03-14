# Avalonia 12.0.0-preview2 Migration Guide

## Table of Contents
1. Scope and Status
2. Coverage Contract
3. Package and Toolchain Changes
4. Breaking Changes to Fix First
5. Behavior Changes to Re-verify
6. Major New APIs in Preview2
7. Migration Workflow
8. Code Migration Examples
9. AOT and Trimming Notes
10. Troubleshooting
11. Full Reference Pointers

## Scope and Status

This lane extends the skill with migration guidance for the current Avalonia 12 preview while keeping the rest of the repository pinned to Avalonia `11.3.12`.

Latest preview status for this guide:

- verified against Avalonia upstream tags and releases on **March 14, 2026**,
- latest published preview tag at that point: **`12.0.0-preview2`**,
- release date of that preview: **March 5, 2026**.

Use this guide when you are actively porting an application, library, or samples from `11.3.12` to `12.0.0-preview2`. Keep using the stable references for day-to-day app-building decisions unless the task explicitly targets the preview lane.

## Coverage Contract

This guide is the curated migration chapter. Exhaustive coverage for the preview lane comes from the generated companion references:

- official breaking changes: [`69-avalonia-12-preview2-breaking-changes-and-new-api-catalog.md`](69-avalonia-12-preview2-breaking-changes-and-new-api-catalog),
- preview public API index: [`api-index-12.0.0-preview2-generated.md`](api-index-12.0.0-preview2-generated).

Official upstream breaking-change docs cross-checked for this guide:

- [Avalonia wiki: v12 Breaking Changes](https://github.com/AvaloniaUI/Avalonia/wiki/v12-Breaking-Changes),
- [Avalonia wiki: Breaking Changes](https://github.com/AvaloniaUI/Avalonia/wiki/Breaking-Changes).

Coverage intent:

- public API additions are exhaustively indexed through the generated preview API index,
- approved breaking changes are exhaustively listed from Avalonia's checked-in package-validation suppressions,
- this guide folds in the user-facing upstream wiki notes that are easy to miss in raw API diff output,
- this guide focuses on app-development migrations, sequencing, examples, and the highest-risk behavior changes.

## Package and Toolchain Changes

Start here before touching view code.

- `Avalonia` no longer targets `netstandard2.0`; the package project in `12.0.0-preview2` targets the current line plus `net8.0`.
- the previewer tool path moved to `tools/net8.0/designer/Avalonia.Designer.HostApp.dll`; the `.NET Framework` previewer executable path is gone.
- `AvaloniaUseCompiledBindingsByDefault` now defaults to `true` in `packages/Avalonia/Avalonia.props`.
- Android minimum supported version moved from `21.0` to `24.0`, and the current build line uses `net10.0-android36.0`.
- the upstream repo no longer contains the old `Avalonia.Browser.Blazor`, `Avalonia.Tizen`, or in-repo `Avalonia.ReactiveUI` projects from the `11.3.12` tree.

Practical do/don't:

- do upgrade your app target frameworks and CI images before you start fixing API errors.
- do audit any project that depended on implicit reflection bindings; preview2 compiles more aggressively by default.
- don't treat this as a pure namespace rename upgrade; several platform, input, dialog, and hosting APIs changed shape.

## Breaking Changes to Fix First

These changes usually block the first successful build or require immediate code edits.

### 1. Binding and metadata types moved

Several binding-facing APIs now live in `Avalonia.Base` / `Avalonia.Data` / `Avalonia.Metadata` instead of their old markup-specific locations.

Common moves:

- `BindingBase`
- `CompiledBinding`
- `CompiledBindingPath`
- `ReflectionBinding`
- `RelativeSource`
- `ConstructorArgumentAttribute`

Migration rule:

- fix `using` directives first,
- then fix code-only binding construction,
- then rebuild to catch any remaining path or converter issues.

### 2. `Binding` and `ReflectionBinding` constructor overloads were removed

`Binding(string, BindingMode)` and `ReflectionBinding(string, BindingMode)` are gone.

Migration rule:

- construct the binding with the path,
- then set `Mode`, `UpdateSourceTrigger`, `Delay`, and other options explicitly.

### 3. Compiled bindings are now the default

If a view relied on implicit reflection binding behavior, preview2 can start surfacing XAML compile errors or different binding resolution.

Migration rule:

- add `x:DataType`,
- use `{CompiledBinding ...}` for typed bindings,
- opt out per binding with `{ReflectionBinding ...}` when you really need dynamic lookup,
- only set `<AvaloniaUseCompiledBindingsByDefault>false</AvaloniaUseCompiledBindingsByDefault>` as a temporary migration escape hatch.

### 4. Data annotations validation is no longer implicit

Avalonia hid the validation plugins and stopped enabling data annotations validation by default.

Migration rule:

- if your forms depended on `System.ComponentModel.DataAnnotations`, opt back in with `AppBuilder.WithDataAnnotationsValidation()`,
- otherwise validation attributes may stop producing UI errors even though the project still compiles.

### 5. Legacy dialog types are gone from the public surface

The suppression-backed break list includes:

- `OpenFileDialog`
- `OpenFolderDialog`
- `SaveFileDialog`
- related system-dialog types

Migration rule:

- move dialog flows to `TopLevel.StorageProvider` and the picker option types from the storage-provider stack,
- use the stable storage guidance in [`29-storage-provider-and-file-pickers.md`](29-storage-provider-and-file-pickers).

### 6. Data transfer APIs moved away from `IDataObject`

Preview2 exposes `IDataTransfer`, `IAsyncDataTransfer`, `DataTransfer`, and `DataTransferItem` as the public drag/drop and clipboard model.

Migration rule:

- replace `IDataObject`-shaped code with `IDataTransfer`/`IAsyncDataTransfer`,
- use the new typed helpers such as `TryGetText`, `TryGetFiles`, `TryGetTextAsync`, and `TryGetBitmapAsync`.

### 7. Window chrome was renamed and reworked

`SystemDecorations` became `WindowDecorations`, and custom drawn decorations gained a new role model for hit testing and themed client chrome.

Migration rule:

- rename `SystemDecorations` property usage to `WindowDecorations`,
- rename platform-impl calls from `SetSystemDecorations(...)` to `SetWindowDecorations(...)`,
- when building custom title bars or resize grips, use `Avalonia.Controls.Chrome.WindowDecorationProperties.ElementRole`.

### 8. `PseudolassesExtensions` was renamed to `PseudoClassesExtensions`

The official upstream `v12 Breaking Changes` wiki calls out the typo fix from `PseudolassesExtensions` to `PseudoClassesExtensions`.

Migration rule:

- update any direct type references, `using static` imports, analyzers, source generators, or reflection-based lookups that still reference `PseudolassesExtensions`,
- if your code only calls the extension method through instance-style syntax on `PseudoClasses`, this rename may not require source edits.

### 9. `TopLevel` is no longer the public catch-all root interface

`TopLevel` no longer publicly carries all of the `IInputRoot` / `ILayoutRoot` / `IRenderRoot` responsibilities directly. Preview2 introduces `IPresentationSource` and a deeper root split.

Migration rule:

- if your app code assumed `TopLevel` was every root service, re-check those assumptions,
- prefer `TopLevel.GetTopLevel(control)` plus public APIs like `StorageProvider`, `Clipboard`, `Screens`, and `Launcher`,
- for visual-root inspection, use the preview `IPresentationSource` and `GetPresentationSource()` extension when appropriate.

### 10. Android bootstrap changed

The old generic `AvaloniaMainActivity<TApp>` path is gone.

Migration rule:

- create an Android `Application` subclass that inherits `AvaloniaAndroidApplication<TApp>`,
- use a plain `AvaloniaMainActivity`,
- prefer `IActivityApplicationLifetime.MainViewFactory` on Android over assigning `ISingleViewApplicationLifetime.MainView`.

## Behavior Changes to Re-verify

These are not just compile fixes. They need runtime checks.

- compiled bindings defaulting to `true` can change which bindings fail at build time versus runtime.
- custom title bars and non-client hit testing need explicit verification after the `WindowDecorations` rename and role-based chrome changes.
- drag/drop, clipboard, and picker flows need end-to-end tests after the data-transfer and storage-provider shifts.
- form validation needs smoke tests if your app depended on data annotations.
- Android activity recreation needs device testing after the new application-driven bootstrap and `MainViewFactory` pattern.

Recommended verification passes:

- build debug and release,
- run XAML compile with source info enabled,
- exercise window chrome, dialogs, drag/drop, clipboard, validation, and navigation flows,
- rerun headless/UI tests if your suite covers bindings or overlay behavior.

## Major New APIs in Preview2

Preview2 is not just cleanup. It adds substantial new surface area.

### Navigation and page stack

New page/navigation APIs include:

- `Page`
- `ContentPage`
- `DrawerPage`
- `NavigationPage`
- `TabbedPage`
- navigation event args and page transitions

Use this lane when you need app-shell navigation that is more structured than ad-hoc `ContentControl` swapping.

### Command bar family

Preview2 adds:

- `CommandBar`
- `AppBarButton`
- `AppBarToggleButton`
- `AppBarSeparator`
- `ICommandBarElement`

These are useful when migrating WinUI-style top command surfaces or mobile/tablet page command bars.

### Code-first compiled bindings

New API:

- `CompiledBinding.Create<TIn, TOut>(...)`

Use it when you need a typed, code-only binding path without falling back to reflection.

### Dispatcher ownership helpers

New helpers include:

- `Dispatcher.CurrentDispatcher`
- `Dispatcher.FromThread(Thread)`
- `AvaloniaObject.Dispatcher`

These are especially useful in long-lived services, custom visuals, and cross-thread coordination code.

### Text rendering split

Preview2 adds:

- `TextOptions`
- `BaselinePixelAlignment`

The old `RenderOptions.TextRenderingMode` path is obsolete; prefer the new `TextOptions` attached properties and drawing-context push methods.

### Modern chrome and popup infrastructure

New or expanded APIs include:

- `WindowDrawnDecorations`
- `WindowDrawnDecorationsContent`
- `WindowDecorationProperties`
- `WindowDecorationsElementRole`
- `PopupOverlayLayer`
- `IPresentationSource`

Use these when you need more precise client-area chrome, overlay placement, or visual-root hosting behavior.

### Input and gesture additions

New input additions include:

- `SwipeGestureRecognizer`
- `SwipeGestureEventArgs`
- `FindNextElementOptions`

These help when migrating touch-first shells and directional navigation behaviors.

## Migration Workflow

1. Move the project baseline first.
- update target frameworks, Android minimums, and any designer/CI expectations.

2. Fix namespace and constructor breaks.
- binding types, metadata attributes, dialog types, and data-transfer APIs should be corrected before UI polish work.

3. Make bindings explicit.
- add `x:DataType`, fix compiled-binding errors, and isolate true reflection cases.

4. Migrate platform services.
- convert dialogs to `StorageProvider`, drag/drop and clipboard to `IDataTransfer`, and Android bootstrap to `AvaloniaAndroidApplication<TApp>`.

5. Re-test window chrome and overlays.
- especially if you extend client area, host popups manually, or rely on custom title bars.

6. Adopt new APIs only after parity.
- page navigation, command bars, `CompiledBinding.Create`, and `TextOptions` are good phase-two upgrades once the app is stable on preview2.

## Code Migration Examples

### Binding constructor migration

Before:

```csharp
using Avalonia.Data;

var nameBinding = new Binding("Customer.Name", BindingMode.TwoWay);
var titleBinding = new ReflectionBinding("WindowTitle", BindingMode.OneWay);
```

After:

```csharp
using Avalonia.Data;

var nameBinding = new Binding("Customer.Name")
{
    Mode = BindingMode.TwoWay
};

var titleBinding = new ReflectionBinding("WindowTitle")
{
    Mode = BindingMode.OneWay
};

var dirtyBinding = CompiledBinding.Create<EditorViewModel, bool>(vm => vm.IsDirty);
```

### XAML binding migration with compiled bindings enabled by default

Before:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <TextBlock Text="{Binding DisplayName}" />
</UserControl>
```

After:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:CustomerViewModel">
  <StackPanel Spacing="8">
    <TextBlock Text="{CompiledBinding DisplayName}" />
    <TextBlock Text="{ReflectionBinding LegacyDynamicValue}" />
  </StackPanel>
</UserControl>
```

### `SystemDecorations` to `WindowDecorations`

Before:

```xaml
<Window xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        SystemDecorations="None"
        ExtendClientAreaToDecorationsHint="True">
  <Grid />
</Window>
```

After:

```xaml
<Window xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:chrome="clr-namespace:Avalonia.Controls.Chrome;assembly=Avalonia.Controls"
        WindowDecorations="None"
        ExtendClientAreaToDecorationsHint="True">
  <Grid>
    <Button chrome:WindowDecorationProperties.ElementRole="CloseButton"
            HorizontalAlignment="Right"
            Content="Close" />
  </Grid>
</Window>
```

### `PseudolassesExtensions` to `PseudoClassesExtensions`

Before:

```csharp
using static Avalonia.Controls.PseudolassesExtensions;

Set(control.PseudoClasses, ":busy", viewModel.IsBusy);
```

After:

```csharp
using static Avalonia.Controls.PseudoClassesExtensions;

Set(control.PseudoClasses, ":busy", viewModel.IsBusy);
```

If you never referenced the static class name directly and only called `control.PseudoClasses.Set(...)`, this rename may already be covered by extension-method resolution.

### `OpenFileDialog` to `StorageProvider`

Before:

```csharp
var dialog = new OpenFileDialog
{
    AllowMultiple = false
};

var result = await dialog.ShowAsync(this);
```

After:

```csharp
var topLevel = TopLevel.GetTopLevel(this)
    ?? throw new InvalidOperationException("No TopLevel available.");

var files = await topLevel.StorageProvider.OpenFilePickerAsync(
    new FilePickerOpenOptions
    {
        AllowMultiple = false,
        FileTypeFilter = new[]
        {
            new FilePickerFileType("Images")
            {
                Patterns = new[] { "*.png", "*.jpg" }
            }
        }
    });
```

### Android bootstrap migration

Before (`11.3.12`):

```csharp
[Activity(MainLauncher = true)]
public class MainActivity : AvaloniaMainActivity<App>
{
}
```

After (`12.0.0-preview2`):

```csharp
[Application]
public class Application : AvaloniaAndroidApplication<App>
{
    protected Application(nint javaReference, JniHandleOwnership transfer)
        : base(javaReference, transfer)
    {
    }
}

[Activity(MainLauncher = true)]
public class MainActivity : AvaloniaMainActivity
{
}
```

If you need dynamic content creation on Android, prefer:

```csharp
if (ApplicationLifetime is IActivityApplicationLifetime activityLifetime)
{
    activityLifetime.MainViewFactory = () => new MainView();
}
```

## AOT and Trimming Notes

- preview2's default compiled-binding mode is generally better for trimming than reflection-heavy `Binding` usage.
- `ReflectionBinding` still carries trimming and dynamic-code caveats; keep it explicit and local.
- `AppBuilder.WithDataAnnotationsValidation()` is annotated for trim risk because it relies on runtime property access.
- `CompiledBinding.Create(...)` is the preferred code-only path when you need a typed binding in AOT-conscious code.

## Troubleshooting

1. Build suddenly fails on views that worked in `11.3.12`.
- Add `x:DataType`, switch to `{CompiledBinding ...}`, or explicitly opt a binding into `{ReflectionBinding ...}`.

2. Validation attributes stopped showing UI errors.
- Re-enable data annotations validation in `BuildAvaloniaApp()` with `WithDataAnnotationsValidation()`.

3. File picker code no longer compiles.
- Move to `TopLevel.StorageProvider` and the `FilePicker*Options` types.

4. Android app starts but the Avalonia view is missing.
- Check that the project now has an `[Application]` type inheriting `AvaloniaAndroidApplication<TApp>` and that `MainActivity` inherits plain `AvaloniaMainActivity`.

5. Custom title bar hit testing broke after the rename.
- Rename `SystemDecorations` to `WindowDecorations` and assign `WindowDecorationProperties.ElementRole` to chrome visuals that must behave like non-client controls.

## Full Reference Pointers

- curated migration lane: this file
- exhaustive break and new API catalog: [`69-avalonia-12-preview2-breaking-changes-and-new-api-catalog.md`](69-avalonia-12-preview2-breaking-changes-and-new-api-catalog)
- exhaustive preview API index: [`api-index-12.0.0-preview2-generated.md`](api-index-12.0.0-preview2-generated)
- official upstream wiki references:
  - [Avalonia wiki: v12 Breaking Changes](https://github.com/AvaloniaUI/Avalonia/wiki/v12-Breaking-Changes)
  - [Avalonia wiki: Breaking Changes](https://github.com/AvaloniaUI/Avalonia/wiki/Breaking-Changes)
- stable binding/build references:
  - [`02-bindings-xaml-aot.md`](02-bindings-xaml-aot)
  - [`41-xaml-compiler-and-build-pipeline.md`](41-xaml-compiler-and-build-pipeline)
- stable platform-service references:
  - [`29-storage-provider-and-file-pickers.md`](29-storage-provider-and-file-pickers)
  - [`31-clipboard-and-data-transfer.md`](31-clipboard-and-data-transfer)
- stable windowing and chrome references:
  - [`13-windowing-and-custom-decorations.md`](13-windowing-and-custom-decorations)
  - [`48-toplevel-window-and-runtime-services.md`](48-toplevel-window-and-runtime-services)
