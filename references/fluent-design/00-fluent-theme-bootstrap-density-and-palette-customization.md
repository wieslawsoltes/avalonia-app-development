# `FluentTheme` Bootstrap, Density, and Palette Customization

## Table of Contents
1. Scope and Primary APIs
2. Basic Setup
3. Density
4. Palette Customization
5. AOT and Runtime Notes
6. Do and Don't Guidance
7. Troubleshooting
8. Official Resources

## Scope and Primary APIs

Use this reference to configure the Fluent baseline correctly.

Primary APIs:
- `Avalonia.Themes.Fluent.FluentTheme`
- `DensityStyle`
- `FluentTheme.Palettes`
- `ColorPaletteResources`
- `ThemeVariant`, `ThemeVariantScope`

High-value members:
- `FluentTheme.DensityStyleProperty`
- `FluentTheme.DensityStyle`
- `FluentTheme.Palettes`
- `ColorPaletteResources.AccentProperty`
- `ColorPaletteResources.Accent`
- `ColorPaletteResources.AltHigh`, `AltLow`, `AltMedium`, `AltMediumHigh`, `AltMediumLow`
- `ColorPaletteResources.BaseHigh`, `BaseLow`, `BaseMedium`, `BaseMediumHigh`, `BaseMediumLow`
- `ColorPaletteResources.ChromeAltLow`, `ChromeHigh`, `ChromeLow`, `ChromeMedium`, `ChromeMediumLow`
- `ColorPaletteResources.ChromeBlackHigh`, `ChromeBlackLow`, `ChromeBlackMedium`, `ChromeBlackMediumLow`
- `ColorPaletteResources.ChromeDisabledHigh`, `ChromeDisabledLow`, `ChromeGray`, `ChromeWhite`
- `ColorPaletteResources.ErrorText`, `ListLow`, `ListMedium`, `RegionColor`

## Basic Setup

```xml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             RequestedThemeVariant="Default">
  <Application.Styles>
    <FluentTheme DensityStyle="Normal" />
  </Application.Styles>
</Application>
```

## Density

Avalonia `11.3.12` exposes:
- `DensityStyle.Normal`
- `DensityStyle.Compact`

```csharp
using System.Linq;
using Avalonia;
using Avalonia.Themes.Fluent;

var fluent = Application.Current!.Styles.OfType<FluentTheme>().First();
fluent.DensityStyle = DensityStyle.Compact;
```

Use `Compact` when:
- data density matters,
- the app is tool-heavy,
- users expect desktop productivity layout.

## Palette Customization

```xml
<FluentTheme xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <FluentTheme.Palettes>
    <ColorPaletteResources x:Key="Light"
                           Accent="#0F6CBD"
                           BaseHigh="#FF201F1E"
                           ChromeLow="#FFF8F8F8"
                           RegionColor="#FFFFFFFF" />
    <ColorPaletteResources x:Key="Dark"
                           Accent="#4CC2FF"
                           BaseHigh="#FFFFFFFF"
                           ChromeLow="#FF1F1F21"
                           RegionColor="#FF111111" />
  </FluentTheme.Palettes>
</FluentTheme>
```

Guidance:
- override only the palette values your product needs,
- keep most palette behavior inherited from Fluent defaults,
- use semantic app tokens on top of the palette instead of exposing raw `System*` keys everywhere.

## AOT and Runtime Notes

- Keep Fluent bootstrap in compiled XAML.
- Treat `Accent` as the safest live palette-change path.
- Validate dark and light variants after every palette override.

## Do and Don't Guidance

Do:
- begin with stock `FluentTheme`,
- use density intentionally,
- keep palette changes minimal and meaningful.

Do not:
- rewrite the whole Fluent palette without a strong reason,
- use compact density as a substitute for layout cleanup,
- treat palette overrides as the whole design system.

## Troubleshooting

1. Palette values appear ignored.
- Confirm they are inside `FluentTheme.Palettes` and keyed by `Light` or `Dark`.

2. Compact mode looks broken.
- The problem is usually custom padding or local styles fighting the base theme.

3. Light and dark variants feel unrelated.
- Re-evaluate brand accent intensity and `RegionColor` / `ChromeLow` choices together.

## Official Resources

- Avalonia Fluent theme docs: [docs.avaloniaui.net/docs/basics/user-interface/styling/themes/fluent](https://docs.avaloniaui.net/docs/basics/user-interface/styling/themes/fluent)
- Avalonia `FluentTheme` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Themes_Fluent_FluentTheme](https://api-docs.avaloniaui.net/docs/T_Avalonia_Themes_Fluent_FluentTheme)
- Avalonia `ColorPaletteResources` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Themes_Fluent_ColorPaletteResources](https://api-docs.avaloniaui.net/docs/T_Avalonia_Themes_Fluent_ColorPaletteResources)
