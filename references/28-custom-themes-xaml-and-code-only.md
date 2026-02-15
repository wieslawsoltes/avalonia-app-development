# Creating Custom Themes (XAML and Code-Only)

## Table of Contents
1. Scope and APIs
2. XAML-Based Theme Authoring (Preferred)
3. Code-Only Theme Authoring (On Request)
4. Runtime Theme Switching and Scope
5. AOT and Performance Guidance
6. Troubleshooting

## Scope and APIs

Primary APIs:
- `ControlTheme`
- `Style`
- `Styles`
- `ThemeVariant`
- `ThemeVariantScope`
- `ResourceDictionary`
- `Application.RequestedThemeVariant`
- `StyledElement.Theme`

Important members:
- `ControlTheme.TargetType`
- `ControlTheme.BasedOn`
- `Style.Setters`
- `ResourceDictionary.ThemeDictionaries`
- `ResourceDictionary.MergedDictionaries`
- `Application.Resources`
- `TopLevel.RequestedThemeVariant`

Reference source files:
- `src/Avalonia.Base/Styling/ControlTheme.cs`
- `src/Avalonia.Base/Styling/Style.cs`
- `src/Avalonia.Base/Styling/ThemeVariant.cs`
- `src/Avalonia.Controls/ThemeVariantScope.cs`
- `src/Avalonia.Base/Controls/ResourceDictionary.cs`
- `src/Avalonia.Controls/Application.cs`

## XAML-Based Theme Authoring (Preferred)

Default approach for this skill:
- Author theme palette, variants, and control themes in `.axaml`.
- Keep theme structure declarative and layered.

Recommended layering:
1. Palette keys in `Application.Resources`.
2. Variant overrides in `Application.Resources.ThemeDictionaries`.
3. Reusable `ControlTheme` entries keyed by explicit resource names.
4. Per-control application through `Theme="{StaticResource ...}"`.

### XAML theme dictionary and variants

```xml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             x:Class="MyApp.App">
  <Application.Resources>
    <SolidColorBrush x:Key="BrandPrimaryBrush">#2F6FED</SolidColorBrush>
    <SolidColorBrush x:Key="BrandForegroundBrush">White</SolidColorBrush>

    <ResourceDictionary.ThemeDictionaries>
      <ResourceDictionary x:Key="Light">
        <SolidColorBrush x:Key="BrandSurfaceBrush">#F7F9FC</SolidColorBrush>
      </ResourceDictionary>
      <ResourceDictionary x:Key="Dark">
        <SolidColorBrush x:Key="BrandSurfaceBrush">#1B1E24</SolidColorBrush>
      </ResourceDictionary>
    </ResourceDictionary.ThemeDictionaries>

    <ControlTheme x:Key="BrandButtonTheme" TargetType="Button">
      <Setter Property="Background" Value="{DynamicResource BrandPrimaryBrush}" />
      <Setter Property="Foreground" Value="{DynamicResource BrandForegroundBrush}" />
      <Setter Property="Padding" Value="12,8" />
      <Setter Property="CornerRadius" Value="8" />
    </ControlTheme>
  </Application.Resources>
</Application>
```

### XAML usage

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            Spacing="8">
  <Border Background="{DynamicResource BrandSurfaceBrush}" Padding="12">
    <TextBlock Text="Themed surface" />
  </Border>

  <Button Content="Primary Action"
          Theme="{StaticResource BrandButtonTheme}" />
</StackPanel>
```

## Code-Only Theme Authoring (On Request)

Use this mode only when the user explicitly asks for code-only UI/theme setup.

### Code-only equivalent theme setup

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;
using Avalonia.Styling;

public static class BrandTheme
{
    public static void Apply(Application app)
    {
        var resources = app.Resources;

        resources["BrandPrimaryBrush"] = new SolidColorBrush(Color.Parse("#2F6FED"));
        resources["BrandForegroundBrush"] = Brushes.White;

        var light = new ResourceDictionary();
        light["BrandSurfaceBrush"] = new SolidColorBrush(Color.Parse("#F7F9FC"));

        var dark = new ResourceDictionary();
        dark["BrandSurfaceBrush"] = new SolidColorBrush(Color.Parse("#1B1E24"));

        resources.ThemeDictionaries[ThemeVariant.Light] = light;
        resources.ThemeDictionaries[ThemeVariant.Dark] = dark;

        var brandButtonTheme = new ControlTheme(typeof(Button));
        brandButtonTheme.Setters.Add(new Setter(Button.BackgroundProperty, resources["BrandPrimaryBrush"]));
        brandButtonTheme.Setters.Add(new Setter(Button.ForegroundProperty, resources["BrandForegroundBrush"]));
        brandButtonTheme.Setters.Add(new Setter(Button.PaddingProperty, new Thickness(12, 8)));
        brandButtonTheme.Setters.Add(new Setter(Button.CornerRadiusProperty, new CornerRadius(8)));

        resources["BrandButtonTheme"] = brandButtonTheme;
    }
}
```

### Code-only usage

```csharp
var button = new Button { Content = "Primary Action" };
button.Theme = (ControlTheme)Application.Current!.Resources["BrandButtonTheme"]!;
```

## Runtime Theme Switching and Scope

Set app-wide variant:

```csharp
Application.Current!.RequestedThemeVariant = ThemeVariant.Dark;
```

Set subtree variant scope in XAML:

```xml
<ThemeVariantScope xmlns="https://github.com/avaloniaui"
                   RequestedThemeVariant="Light">
  <Border Background="{DynamicResource BrandSurfaceBrush}" />
</ThemeVariantScope>
```

Guidance:
- Use app-level variant for user preference.
- Use `ThemeVariantScope` for isolated previews/editors.
- Prefer `DynamicResource` for keys expected to change by variant.

## AOT and Performance Guidance

- XAML-defined themes with compiled XAML are the default path.
- Keep resource keys stable and avoid runtime parser-heavy dynamic style construction.
- Avoid rebuilding large dictionaries at runtime; update only changed keys.
- Keep control theme set operations bounded and explicit.

## Troubleshooting

1. Custom theme not applied:
- `Theme` key missing or wrong key/type.
- `ControlTheme.TargetType` does not match the control type.

2. Dark/light values do not change:
- Keys are not inside `ThemeDictionaries`.
- Resource is referenced via `StaticResource` where `DynamicResource` is needed.

3. Styles look inconsistent across windows:
- Theme resources added only to a local dictionary, not `Application.Resources`.
- Multiple merged dictionaries override the same keys in unexpected order.

4. Code-only theme throws cast/key errors:
- Resource key not present or incorrect type at lookup.
- Theme initialization executed after control creation instead of at startup.

## XAML-First and Code-Only Usage

Default mode:
- Start with theme resources and `ControlTheme` declarations in XAML.
- Provide code-only theme construction only when the user explicitly requests it.

XAML-first complete usage:

```xml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             x:Class="MyApp.App"
             RequestedThemeVariant="Default">
  <Application.Resources>
    <ResourceDictionary>
      <ResourceDictionary.ThemeDictionaries>
        <ResourceDictionary x:Key="Light">
          <SolidColorBrush x:Key="PageBackgroundBrush" Color="#F7F9FC" />
        </ResourceDictionary>
        <ResourceDictionary x:Key="Dark">
          <SolidColorBrush x:Key="PageBackgroundBrush" Color="#171A20" />
        </ResourceDictionary>
      </ResourceDictionary.ThemeDictionaries>

      <ControlTheme x:Key="PrimaryButtonTheme" TargetType="Button">
        <Setter Property="Background" Value="#2F6FED" />
        <Setter Property="Foreground" Value="White" />
      </ControlTheme>
    </ResourceDictionary>
  </Application.Resources>
</Application>
```

Code-only alternative (on request):

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;
using Avalonia.Styling;

var app = Application.Current!;
app.Resources.ThemeDictionaries[ThemeVariant.Light] = new ResourceDictionary
{
    ["PageBackgroundBrush"] = new SolidColorBrush(Color.Parse("#F7F9FC"))
};
app.Resources.ThemeDictionaries[ThemeVariant.Dark] = new ResourceDictionary
{
    ["PageBackgroundBrush"] = new SolidColorBrush(Color.Parse("#171A20"))
};

var primaryButton = new ControlTheme(typeof(Button));
primaryButton.Setters.Add(new Setter(Button.BackgroundProperty, new SolidColorBrush(Color.Parse("#2F6FED"))));
primaryButton.Setters.Add(new Setter(Button.ForegroundProperty, Brushes.White));
app.Resources["PrimaryButtonTheme"] = primaryButton;
```
