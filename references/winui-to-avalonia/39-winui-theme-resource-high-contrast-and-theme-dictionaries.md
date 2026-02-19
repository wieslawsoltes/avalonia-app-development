# WinUI ThemeResource, High Contrast, and Theme Dictionaries to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- ThemeResource, RequestedTheme, ResourceDictionary.ThemeDictionaries, HighContrastAdjustment

Primary Avalonia APIs:

- DynamicResource, ThemeVariant, resource dictionaries, style selectors

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| WinUI control and state pipeline | Avalonia control themes, selectors, and transitions |
| WinUI command/input surfaces | Avalonia commands + `KeyBinding`/routed input |
| WinUI resource/theme flow | Avalonia resource dictionaries + `ThemeVariant` |

## Conversion Example

WinUI XAML:

```xaml
<Grid Background="{ThemeResource SystemControlAcrylicWindowBrush}" RequestedTheme="Dark" />
```

WinUI C#:

```csharp
Application.Current.RequestedTheme = ApplicationTheme.Dark;
```

Avalonia XAML:

```xaml
<Grid Background="{DynamicResource ThemeBackgroundBrush}" ThemeVariant="Dark" />
```

Avalonia C#:

```csharp
Application.Current!.RequestedThemeVariant = ThemeVariant.Dark;
```

## Migration Notes

1. Preserve behavior and interaction contracts before visual refinements.
2. Port hot paths with explicit UI-thread and invalidation discipline.
3. Prefer typed compiled bindings and deterministic state flow in migrated views.
