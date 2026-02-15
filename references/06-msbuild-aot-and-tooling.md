# MSBuild, XAML Compilation, and AOT Tooling

## Key Build Pipeline Facts

From Avalonia package/build targets:
- XAML compilation is controlled by `EnableAvaloniaXamlCompilation`.
- Compiled bindings default is controlled by `AvaloniaUseCompiledBindingsByDefault`.
- XAML compiler diagnostics and debug info are controlled by:
  - `AvaloniaXamlVerboseExceptions`
  - `AvaloniaXamlCreateSourceInfo`
  - `AvaloniaXamlIlVerifyIl`
- Avalonia item groups:
  - `AvaloniaXaml`
  - `AvaloniaResource`

## Recommended Defaults for Modern Apps

- Keep `EnableAvaloniaXamlCompilation=true`.
- Keep `AvaloniaUseCompiledBindingsByDefault=true`.
- Keep source info enabled in Debug to improve stack traces.
- Keep verbose exceptions on during development and CI validation.

## NativeAOT/Trimming-Oriented Project Baseline

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>

    <!-- Avalonia + XAML -->
    <EnableAvaloniaXamlCompilation>true</EnableAvaloniaXamlCompilation>
    <AvaloniaUseCompiledBindingsByDefault>true</AvaloniaUseCompiledBindingsByDefault>

    <!-- NativeAOT -->
    <PublishAot>true</PublishAot>
    <TrimMode>full</TrimMode>
    <InvariantGlobalization>true</InvariantGlobalization>
  </PropertyGroup>
</Project>
```

Adjust runtime and trim settings per product requirements, but keep compiled bindings and compiled XAML as baseline.

## Source Generator Controls (`Avalonia.Generators.props`)

Available knobs:
- `AvaloniaNameGeneratorIsEnabled`
- `AvaloniaNameGeneratorBehavior`
- `AvaloniaNameGeneratorDefaultFieldModifier`
- `AvaloniaNameGeneratorFilterByPath`
- `AvaloniaNameGeneratorFilterByNamespace`
- `AvaloniaNameGeneratorViewFileNamingStrategy`
- `AvaloniaNameGeneratorAttachDevTools`

Use:
- Keep generator enabled for typed named-control access and robust component initialization.

## Packaging and Resource Item Rules

- Ensure views are included as `AvaloniaXaml` (or default item inclusion picks them up).
- Ensure static assets referenced by `avares://` are included as `AvaloniaResource`.

Symptoms of misconfiguration:
- "No precompiled XAML found..."
- Resource not found at runtime.

## AOT Risk APIs to Review Explicitly

Treat these as design decisions, not defaults:
- `ReflectionBinding` and reflection-driven markup bindings.
- Runtime XAML loading APIs.
- Dynamic selector parsing paths where typed alternatives exist.
- Reflection-heavy validation plugins unless explicitly needed.

## Build Verification Checklist

- Build Debug and Release.
- Publish (trim/AOT) target profile.
- Start app and exercise key navigation paths.
- Scan warnings for `RequiresUnreferencedCode`/`RequiresDynamicCode` call chains.
- Resolve warnings by moving to compiled/static alternatives where feasible.

## XAML-First and Code-Only Usage

Default mode:
- Keep UI in compiled XAML with compiled bindings.
- Use code-only UI construction only when the user requests it.

XAML-first references:
- `EnableAvaloniaXamlCompilation`
- `AvaloniaUseCompiledBindingsByDefault`

Code-only alternative (on request):

```csharp
var view = new StackPanel
{
    Children =
    {
        new TextBlock { Text = "AOT-safe baseline" },
        new Button { Content = "Run" }
    }
};

window.Content = view;
```
