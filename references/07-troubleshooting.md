# Troubleshooting

## Fast Triage Order

1. Confirm lifetime branch (`Desktop`, `SingleView`, `Activity`) executes as expected.
2. Confirm precompiled XAML/resources are included correctly.
3. Confirm binding style (`CompiledBinding` vs reflection binding) and `x:DataType` contracts.
4. Confirm UI-thread access for control updates.
5. Confirm platform backend options and rendering fallbacks.

## Symptom Matrix

### 1) "No precompiled XAML found for ..."

Likely causes:
- XAML file not included as `AvaloniaXaml`/`AvaloniaResource`.
- Missing/incorrect `x:Class`.
- XAML compilation disabled.

Fixes:
- Ensure `EnableAvaloniaXamlCompilation=true`.
- Ensure XAML item inclusion is correct.
- Ensure class/file naming and `x:Class` match generated partial type.

### 2) Binding works in Debug but fails in trimmed/AOT publish

Likely causes:
- Reflection binding (`{Binding ...}` / `ReflectionBinding`) used in critical path.
- Runtime dynamic loader/parsing paths.

Fixes:
- Move to `x:DataType` + `{CompiledBinding ...}`.
- Remove or isolate reflection/dynamic binding paths.

### 3) UI updates throw cross-thread exceptions or behave inconsistently

Likely causes:
- Viewmodel/service updates control properties off UI thread.

Fixes:
- Marshal to `Dispatcher.UIThread` via `Post`/`InvokeAsync`.
- Keep data fetch/compute off-thread, apply UI deltas on UI thread.

### 4) Dialog/file-picker behavior differs by platform

Likely causes:
- Platform feature availability differs.
- Missing `UseManagedSystemDialogs()` where desired.

Fixes:
- Use `TopLevel.StorageProvider` APIs and platform-appropriate fallback.
- Configure managed dialog extension when native behavior mismatch is unacceptable.

### 5) Window close/shutdown behavior is incorrect

Likely causes:
- Wrong `ShutdownMode`.
- Root window not assigned as `MainWindow`.

Fixes:
- Set `ShutdownMode` explicitly.
- Assign `MainWindow` in lifetime setup path.

### 6) Theme changes do not propagate as expected

Likely causes:
- Mixing local resources with missing theme dictionaries.
- Overriding variant in wrong scope.

Fixes:
- Use `ThemeVariantScope` for subtree overrides.
- Put variant resources in `ThemeDictionaries` and verify key consistency.

### 7) Startup fails only on one backend (Win32/X11/Browser/etc.)

Likely causes:
- Backend initialization mismatch.
- Unsupported rendering mode with no fallback.

Fixes:
- Verify `UseWin32`/`UseX11`/`UseBrowser`/etc. path is actually selected.
- Add and order rendering fallbacks including software mode.

### 8) Data templates not applied or type mismatch exceptions

Likely causes:
- Missing `DataType` in shared/global template contexts.

Fixes:
- Add `x:DataType`/`DataType` consistently for template collections.

## Binding Diagnostics Tips

- Prefer explicit mode declarations (`Mode=TwoWay` etc.) in critical forms.
- Validate fallback/null handling (`FallbackValue`, `TargetNullValue`).
- If a path is ambiguous, create a minimal reproduction with a typed viewmodel and one control.

## Publish Validation Tips

- Validate both `dotnet build` and publish profile outputs.
- Run smoke tests on each target runtime.
- Track and resolve trimming warnings before release freeze.

## XAML-First and Code-Only Usage

Default mode:
- Reproduce and fix issues in XAML-first paths before considering code-only rewrites.
- Provide code-only equivalents only when requested.

XAML-first references:
- `x:DataType` and `{CompiledBinding ...}`
- `Application.Styles` and `DataTemplates`

XAML-first minimal repro:

```xml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:LoginViewModel">
  <TextBox Text="{CompiledBinding UserName}" />
</UserControl>
```

Code-only minimal repro (on request):

```csharp
var textBox = new TextBox();
textBox.Bind(TextBox.TextProperty, new Binding(nameof(LoginViewModel.UserName)));
```
