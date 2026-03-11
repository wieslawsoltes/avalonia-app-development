# Fluent Alias Tokens, Brand Mapping, Materials, and Elevation

## Table of Contents
1. Scope and Primary APIs
2. Semantic Mapping
3. Elevation and Materials
4. AOT and Runtime Notes
5. Do and Don't Guidance
6. Troubleshooting
7. Official Resources

## Scope and Primary APIs

Use this reference to map Fluent palette resources into product-level semantics.

Primary APIs:
- `ColorPaletteResources`
- `ResourceDictionary`, `ThemeDictionaries`
- `DynamicResourceExtension`
- `BoxShadows`
- `ExperimentalAcrylicBorder`, `ExperimentalAcrylicMaterial`

High-value material members:
- `ExperimentalAcrylicBorder.CornerRadiusProperty`
- `ExperimentalAcrylicBorder.MaterialProperty`
- `ExperimentalAcrylicMaterial.TintColorProperty`
- `ExperimentalAcrylicMaterial.BackgroundSourceProperty`
- `ExperimentalAcrylicMaterial.TintOpacityProperty`
- `ExperimentalAcrylicMaterial.MaterialOpacityProperty`
- `ExperimentalAcrylicMaterial.PlatformTransparencyCompensationLevelProperty`
- `ExperimentalAcrylicMaterial.FallbackColorProperty`
- `ExperimentalAcrylicMaterial.BackgroundSource`
- `ExperimentalAcrylicMaterial.PlatformTransparencyCompensationLevel`

## Semantic Mapping

```xml
<ResourceDictionary xmlns="https://github.com/avaloniaui"
                    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <SolidColorBrush x:Key="Brush.Brand.Primary" Color="{DynamicResource SystemAccentColor}" />
  <SolidColorBrush x:Key="Brush.Brand.Secondary" Color="{DynamicResource SystemAccentColorDark1}" />
  <SolidColorBrush x:Key="Brush.Text.Primary" Color="{DynamicResource SystemBaseHighColor}" />
  <SolidColorBrush x:Key="Brush.Text.Secondary" Color="{DynamicResource SystemBaseMediumColor}" />
  <SolidColorBrush x:Key="Brush.Surface.Window" Color="{DynamicResource SystemRegionColor}" />
  <SolidColorBrush x:Key="Brush.Surface.Card" Color="{DynamicResource SystemChromeLowColor}" />
  <SolidColorBrush x:Key="Brush.Border.Subtle" Color="{DynamicResource SystemChromeMediumLowColor}" />
</ResourceDictionary>
```

Guidance:
- map brand intent with semantic names,
- let Fluent own raw palette generation,
- keep app code and themes referencing semantic aliases.

## Elevation and Materials

```xml
<Border xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Background="{DynamicResource Brush.Surface.Card}"
        BorderBrush="{DynamicResource Brush.Border.Subtle}"
        BorderThickness="1"
        CornerRadius="12"
        BoxShadow="0 8 24 0 #18000000" />
```

```xml
<ExperimentalAcrylicBorder xmlns="https://github.com/avaloniaui"
                           xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                           CornerRadius="12">
  <ExperimentalAcrylicBorder.Material>
    <ExperimentalAcrylicMaterial TintColor="{DynamicResource SystemChromeLowColor}"
                                 TintOpacity="0.8"
                                 MaterialOpacity="0.45"
                                 FallbackColor="#CC1F1F21" />
  </ExperimentalAcrylicBorder.Material>
</ExperimentalAcrylicBorder>
```

Guidance:
- Avalonia exposes acrylic directly; true Mica is not a general cross-platform Fluent abstraction in Avalonia,
- use translucent materials mainly for shell accents or special overlays,
- keep most productivity surfaces opaque and legible.

## AOT and Runtime Notes

- Prefer static semantic brush resources.
- Keep acrylic use limited on large or rapidly changing surfaces.

## Do and Don't Guidance

Do:
- wrap `System*` resources in semantic aliases,
- keep elevation subtle,
- use materials deliberately.

Do not:
- expose raw Fluent palette names as your app’s design language,
- put acrylic on every surface,
- rely on accent color as the only hierarchy tool.

## Troubleshooting

1. Brand mapping feels too loud.
- Reduce the number of accent-derived surfaces and let neutrals carry more of the UI.

2. Acrylic surfaces hurt readability.
- Increase fallback strength and isolate text from the translucent background.

3. Dark theme elevation feels muddy.
- Reduce shadow and increase border contrast instead.

## Official Resources

- Fluent 2 color: [fluent2.microsoft.design/styles/color](https://fluent2.microsoft.design/styles/color/)
- Fluent 2 material: [fluent2.microsoft.design/material](https://fluent2.microsoft.design/material)
- Fluent 2 elevation: [fluent2.microsoft.design/elevation](https://fluent2.microsoft.design/elevation)
