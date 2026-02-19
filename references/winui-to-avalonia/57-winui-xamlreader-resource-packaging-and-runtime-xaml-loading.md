# WinUI XamlReader/Resource Packaging to Avalonia Runtime XAML Loading

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- XamlReader.Load, ResourceDictionary, merged dictionary `Source`, ms-appx packaging

Primary Avalonia APIs:

- AvaloniaXamlLoader, AvaloniaRuntimeXamlLoader, RuntimeXamlLoaderDocument, ResourceInclude, StyleInclude, avares packaging

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| XamlReader.Load runtime fragments | AvaloniaRuntimeXamlLoader.Parse/Load |
| ResourceDictionary Source (`ms-appx`) | ResourceInclude/StyleInclude (`avares`) |
| compiled XAML + runtime fallback | compiled XAML + explicit runtime loader |
| package-relative resource URI | `avares://Assembly/Path.axaml` |

## Conversion Example

WinUI XAML:

```xaml
<Page.Resources>
  <ResourceDictionary Source="ms-appx:///Themes/Shared.xaml" />
</Page.Resources>
```

WinUI C#:

```csharp
var dynamicButton = (UIElement)XamlReader.Load("<Button xmlns='http://schemas.microsoft.com/winfx/2006/xaml/presentation' Content='Dynamic' />");
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <UserControl.Resources>
    <ResourceInclude Source="avares://MyApp/Styles/Shared.axaml" />
  </UserControl.Resources>

  <ContentPresenter />
</UserControl>
```

Avalonia C#:

```csharp
var dynamicButton = AvaloniaRuntimeXamlLoader.Parse<Button>(
    "<Button xmlns='https://github.com/avaloniaui' Content='Dynamic' />");

var doc = new RuntimeXamlLoaderDocument(new Uri("avares://MyApp/Views/DynamicView.axaml"), xamlText);
var view = AvaloniaRuntimeXamlLoader.Load(doc);
```

## Migration Notes

1. Keep runtime XAML loading isolated to plugin/editor paths; prefer compiled XAML for core UI.
2. Convert resource URIs to `avares://` and verify assembly/resource packaging paths.
3. Treat runtime loader APIs as trim/AOT-sensitive and opt-in.
