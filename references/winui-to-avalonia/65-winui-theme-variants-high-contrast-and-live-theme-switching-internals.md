# WinUI Theme Variants, High Contrast, and Live Theme Switching to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- Application.RequestedTheme, FrameworkElement.RequestedTheme
- AccessibilitySettings.HighContrast
- UISettings.ColorValuesChanged

Primary Avalonia APIs:

- Application.RequestedThemeVariant, TopLevel.RequestedThemeVariant, ThemeVariantScope
- Application.ActualThemeVariantChanged
- IPlatformSettings.GetColorValues, ColorValuesChanged
- PlatformColorValues.ContrastPreference

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| app-level requested theme | `Application.RequestedThemeVariant` |
| subtree theme override | `ThemeVariantScope RequestedThemeVariant` |
| high-contrast preference checks | `PlatformColorValues.ContrastPreference` |
| live system color/theme updates | `IPlatformSettings.ColorValuesChanged` |

## Conversion Example

WinUI XAML:

```xaml
<Grid RequestedTheme="Dark"
      Background="{ThemeResource ApplicationPageBackgroundThemeBrush}" />
```

WinUI C#:

```csharp
Application.Current.RequestedTheme = ApplicationTheme.Dark;

var accessibility = new AccessibilitySettings();
bool isHighContrast = accessibility.HighContrast;
```

Avalonia XAML:

```xaml
<ThemeVariantScope xmlns="https://github.com/avaloniaui"
                   xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                   RequestedThemeVariant="Dark">
  <Border Background="{DynamicResource ThemeBackgroundBrush}" />
</ThemeVariantScope>
```

Avalonia C#:

```csharp
Application.Current!.RequestedThemeVariant = ThemeVariant.Dark;

if (Application.Current.PlatformSettings is { } platform)
{
    ApplyContrast(platform.GetColorValues());
    platform.ColorValuesChanged += (_, values) => ApplyContrast(values);
}

void ApplyContrast(PlatformColorValues values)
{
    if (values.ContrastPreference == ColorContrastPreference.High)
        Application.Current!.RequestedThemeVariant = ThemeVariant.Dark;
}
```

## Migration Notes

1. Keep theme switching reactive and resource-driven (`DynamicResource`) rather than repainting manually.
2. Handle system contrast/theme notifications as runtime events, not startup-only state.
3. Validate contrast and accent behavior on each target OS backend.
