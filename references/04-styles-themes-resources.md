# Styles, Themes, and Resources

## Styling Surface

Primary APIs:
- `Style`
- `Styles`
- `ControlTheme`
- `Selectors`
- `ThemeVariant`
- `ThemeVariantScope`
- `ResourceDictionary`

## Recommended Layering

1. `Application.Styles`:
- Host global themes and broad app-level styles.

2. `ControlTheme` per control family:
- Keep lookless/themeable control appearance isolated.

3. Local control styles:
- Apply small local adjustments closest to usage sites.

4. Resources:
- Place shared constants/brushes/spacing in dictionaries.
- Use theme dictionaries for variant-specific values.

## Theme Variant Model

Theme APIs:
- `ThemeVariant.Default`
- `ThemeVariant.Light`
- `ThemeVariant.Dark`
- `RequestedThemeVariant`
- `ActualThemeVariant`

Use:
- Set `Application.RequestedThemeVariant` for app-wide preference.
- Use `ThemeVariantScope` for subtree overrides.

## Resource Dictionaries

`ResourceDictionary` highlights:
- `MergedDictionaries`
- `ThemeDictionaries`
- `TryGetResource(...)`

Use:
- Keep keys stable and explicit.
- Use `ThemeDictionaries` for dark/light values, not runtime `if` logic in controls.

## Selector Strategy

### XAML selector strings

Good for static styles in compiled XAML files.

### C# typed selectors

`Selectors` factory methods (`OfType<T>`, `Class`, `Name`, `Child`, `Descendant`, `Template`, etc.) give stronger refactorability and avoid some runtime parser tradeoffs.

Example:

```csharp
var style = new Style(x => x.OfType<Button>().Class("accent"));
style.Setters.Add(new Setter(Button.FontWeightProperty, FontWeight.Bold));
```

## Includes and AOT Notes

XAML include APIs:
- `StyleInclude`
- `ResourceInclude`
- `MergeResourceInclude`

Guidance:
- Includes declared in compiled XAML are generally the intended safe path.
- Dynamic loading/inclusion patterns should be treated as advanced scenarios and reviewed for trim impact.

## ControlTheme Guidance

`ControlTheme`:
- Requires `TargetType`.
- Supports `BasedOn` composition.

Use:
- Put control skinning behavior here instead of monolithic global selectors.
- Keep template-specific nested selectors constrained and readable.

## Common Styling Mistakes

1. Massive global style files with no ownership boundaries.
- Fix: split by feature/control category.

2. Duplicated color/spacing literals in many views.
- Fix: centralize in resources and theme dictionaries.

3. Heavy selector chains that are hard to maintain.
- Fix: prefer direct classes, clear scope, and control themes.

4. Runtime style construction for static concerns.
- Fix: move static style definitions back into compiled XAML.

## XAML-First and Code-Only Usage

Default mode:
- Author styles/themes/resources in XAML first.
- Use code-only style construction when requested.

XAML-first references:
- `Style`, `ControlTheme`, `ThemeVariantScope`, `ResourceDictionary`

XAML-first usage example:

```xml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             x:Class="MyApp.App">
  <Application.Resources>
    <Color x:Key="AccentColor">#2F6FED</Color>
    <SolidColorBrush x:Key="AccentBrush" Color="{DynamicResource AccentColor}" />
  </Application.Resources>

  <Application.Styles>
    <Style Selector="Button.accent">
      <Setter Property="Background" Value="{DynamicResource AccentBrush}" />
      <Setter Property="Foreground" Value="White" />
    </Style>
  </Application.Styles>
</Application>
```

Code-only alternative (on request):

```csharp
var style = new Style(x => x.OfType<Button>().Class("accent"));
style.Setters.Add(new Setter(Button.BackgroundProperty, Brushes.SteelBlue));
style.Setters.Add(new Setter(Button.ForegroundProperty, Brushes.White));
Application.Current!.Styles.Add(style);
```
