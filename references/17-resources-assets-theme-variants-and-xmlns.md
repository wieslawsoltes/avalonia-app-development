# Resources, Assets, Theme Variants, and XmlnsDefinition

## Table of Contents
1. Scope and APIs
2. Resource Authoring
3. Theme Variant Authoring
4. Asset Authoring and Access
5. XmlnsDefinition Usage
6. Best Practices
7. Troubleshooting

## Scope and APIs

Primary APIs:
- `ResourceDictionary`
- `IResourceDictionary`
- `ResourceDictionary.MergedDictionaries`
- `ResourceDictionary.ThemeDictionaries`
- `TryGetResource(key, theme, out value)`
- `ThemeVariant` (`Default`, `Light`, `Dark`)
- `ThemeVariantScope`
- `Application.RequestedThemeVariant`
- `AssetLoader` and `IAssetLoader`
- `XmlnsDefinitionAttribute`

Reference source files:
- `src/Avalonia.Base/Controls/ResourceDictionary.cs`
- `src/Avalonia.Base/Controls/IResourceDictionary.cs`
- `src/Avalonia.Base/Styling/ThemeVariant.cs`
- `src/Avalonia.Controls/ThemeVariantScope.cs`
- `src/Avalonia.Controls/Application.cs`
- `src/Avalonia.Base/Platform/AssetLoader.cs`
- `src/Avalonia.Base/Platform/IAssetLoader.cs`
- `src/Avalonia.Base/Metadata/XmlnsDefinitionAttribute.cs`
- `src/Avalonia.Base/Properties/AssemblyInfo.cs`

## Resource Authoring

Use a layered resource strategy:
1. Global resources (`Application.Resources`, `Application.Styles`).
2. Feature/module dictionaries via `MergedDictionaries`.
3. Control-local resources only for tightly scoped values.

`ResourceDictionary` behavior highlights:
- Lookup checks local entries, then theme dictionaries, then merged dictionaries.
- Theme lookup follows inherit chain from selected `ThemeVariant`.

Example:

```xml
<ResourceDictionary>
  <Color x:Key="BrandColor">#0A84FF</Color>

  <ResourceDictionary.MergedDictionaries>
    <ResourceInclude Source="avares://MyApp/Styles/Buttons.axaml" />
  </ResourceDictionary.MergedDictionaries>
</ResourceDictionary>
```

## Theme Variant Authoring

Theme variant APIs:
- `ThemeVariant.Default`
- `ThemeVariant.Light`
- `ThemeVariant.Dark`
- `RequestedThemeVariant`
- `ActualThemeVariant`

Use app-wide setting:

```xml
<Application RequestedThemeVariant="Default" />
```

Use local override scope:

```xml
<ThemeVariantScope RequestedThemeVariant="Dark">
  <ContentPresenter Content="{Binding}" />
</ThemeVariantScope>
```

Theme dictionaries:

```xml
<ResourceDictionary>
  <ResourceDictionary.ThemeDictionaries>
    <ResourceDictionary x:Key="Light">
      <SolidColorBrush x:Key="AppBackground" Color="White" />
    </ResourceDictionary>
    <ResourceDictionary x:Key="Dark">
      <SolidColorBrush x:Key="AppBackground" Color="#202020" />
    </ResourceDictionary>
    <ResourceDictionary x:Key="Default">
      <SolidColorBrush x:Key="AppBackground" Color="#F5F5F5" />
    </ResourceDictionary>
  </ResourceDictionary.ThemeDictionaries>
</ResourceDictionary>
```

## Asset Authoring and Access

Project item guidance:
- Mark XAML and static assets as `AvaloniaResource`.
- Access with `avares://AssemblyName/path` URIs.

C# asset access:

```csharp
using Avalonia.Platform;

using var stream = AssetLoader.Open(new Uri("avares://MyApp/Assets/logo.png"));
```

Other asset APIs:
- `AssetLoader.Exists(...)`
- `AssetLoader.OpenAndGetAssembly(...)`
- `AssetLoader.GetAssets(...)`

Includes from assets:
- `StyleInclude Source="avares://..."`
- `ResourceInclude Source="avares://..."`
- `MergeResourceInclude Source="avares://..."`

## XmlnsDefinition Usage

`XmlnsDefinitionAttribute` maps XML namespace to CLR namespace at assembly level.

Pattern:

```csharp
[assembly: XmlnsDefinition("https://github.com/avaloniaui", "MyApp.Controls")]
[assembly: XmlnsDefinition("https://github.com/avaloniaui", "MyApp.Theming")]
```

Effect:
- Your controls are available in XAML under the mapped XML namespace.
- Avoids repetitive `xmlns:local="clr-namespace:..."` in some scenarios.

## Best Practices

- Keep resource keys stable and semantic.
- Put variant-specific values in `ThemeDictionaries` instead of `if` logic.
- Prefer `DynamicResource` for values expected to change with theme.
- Keep asset URIs explicit and assembly-qualified in shared libraries.
- Keep XML namespace mappings intentional and non-ambiguous.

## Troubleshooting

1. Resource not found:
- Wrong key, dictionary not merged, or wrong scope owner.

2. Theme variant not switching values:
- Missing `ThemeDictionaries` entry for selected variant.
- No `RequestedThemeVariant`/`ThemeVariantScope` configuration where expected.

3. Asset load fails (`FileNotFoundException`):
- Wrong `avares://` URI.
- Asset not marked as `AvaloniaResource`.

4. XAML cannot resolve custom controls:
- Missing or incorrect `XmlnsDefinition` mapping.
- Namespace mapped, but type is not public/accessible to XAML loader.

## XAML-First and Code-Only Usage

Default mode:
- Define resources/assets/theme variants in XAML first.
- Use code-only dictionary construction when requested.

XAML-first complete example:

```xml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             x:Class="MyApp.App"
             RequestedThemeVariant="Default">
  <Application.Resources>
    <ResourceDictionary>
      <ResourceDictionary.ThemeDictionaries>
        <ResourceDictionary x:Key="Light">
          <SolidColorBrush x:Key="SurfaceBrush" Color="White" />
        </ResourceDictionary>
        <ResourceDictionary x:Key="Dark">
          <SolidColorBrush x:Key="SurfaceBrush" Color="#202020" />
        </ResourceDictionary>
      </ResourceDictionary.ThemeDictionaries>
    </ResourceDictionary>
  </Application.Resources>
</Application>
```

Code-only alternative (on request):

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;
using Avalonia.Platform;

var res = Application.Current!.Resources;
res.ThemeDictionaries[ThemeVariant.Light] = new ResourceDictionary
{
    ["SurfaceBrush"] = Brushes.White
};
res.ThemeDictionaries[ThemeVariant.Dark] = new ResourceDictionary
{
    ["SurfaceBrush"] = new SolidColorBrush(Color.Parse("#202020"))
};

using var logo = AssetLoader.Open(new Uri("avares://MyApp/Assets/logo.png"));
```
