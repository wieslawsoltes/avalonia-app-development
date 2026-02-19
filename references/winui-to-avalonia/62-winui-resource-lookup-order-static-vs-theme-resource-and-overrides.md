# WinUI Resource Lookup Order and ThemeResource to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- ResourceDictionary, StaticResource, ThemeResource
- ResourceDictionary.MergedDictionaries, ThemeDictionaries

Primary Avalonia APIs:

- ResourceDictionary, StaticResource, DynamicResource
- ResourceDictionary.MergedDictionaries, ThemeDictionaries
- ResourceInclude, StyleInclude
- Application.TryGetResource(...)

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| `StaticResource` for stable values | `StaticResource` |
| `ThemeResource` for theme-variant values | `DynamicResource` + `ThemeDictionaries` |
| merged dictionary layering | merged dictionary layering |
| resource probe at runtime | `TryGetResource(key, theme, out value)` |

## Conversion Example

WinUI XAML:

```xaml
<Page.Resources>
  <ResourceDictionary>
    <ResourceDictionary.ThemeDictionaries>
      <ResourceDictionary x:Key="Light">
        <SolidColorBrush x:Key="AccentBrush" Color="#0063B1" />
      </ResourceDictionary>
      <ResourceDictionary x:Key="Dark">
        <SolidColorBrush x:Key="AccentBrush" Color="#4CC2FF" />
      </ResourceDictionary>
    </ResourceDictionary.ThemeDictionaries>
  </ResourceDictionary>
</Page.Resources>

<Border Background="{ThemeResource AccentBrush}" />
```

WinUI C#:

```csharp
if (Application.Current.Resources.TryGetValue("AccentBrush", out var value) && value is SolidColorBrush brush)
{
    HeaderBorder.Background = brush;
}
```

Avalonia XAML:

```xaml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <Application.Resources>
    <ResourceDictionary>
      <ResourceDictionary.ThemeDictionaries>
        <ResourceDictionary x:Key="Light">
          <SolidColorBrush x:Key="AccentBrush" Color="#0063B1" />
        </ResourceDictionary>
        <ResourceDictionary x:Key="Dark">
          <SolidColorBrush x:Key="AccentBrush" Color="#4CC2FF" />
        </ResourceDictionary>
      </ResourceDictionary.ThemeDictionaries>
    </ResourceDictionary>
  </Application.Resources>
</Application>

<Border Background="{DynamicResource AccentBrush}" />
```

Avalonia C#:

```csharp
if (Application.Current!.TryGetResource("AccentBrush", ThemeVariant.Dark, out var value) && value is IBrush brush)
{
    HeaderBorder.Background = brush;
}
```

## Migration Notes

1. Translate `ThemeResource` usage to `DynamicResource` with explicit `ThemeDictionaries` keys.
2. Keep shared keys stable across light/dark dictionaries to prevent missing-resource fallbacks.
3. Validate lookup behavior at control scope and app scope after dictionary merge order changes.
