# Fluent Icons, Public Icon Sets, and Avalonia Usage

## Table of Contents
1. Scope and Primary APIs
2. Fluent Icon Rules Before You Pick a Library
3. Public Icon Sets Worth Considering
4. Avalonia Icon Delivery Options
5. Recommended Fluent Workflow
6. `PathIcon` with Shared `StreamGeometry`
7. `Path` and Geometry Composition for Advanced Cases
8. `DrawingImage` plus `Image`
9. Raster Assets with `Image` and `Bitmap`
10. Icon Fonts with `TextBlock`
11. Menu, Native Menu, Window, and Tray Icons
12. Choosing the Right Representation
13. AOT and Runtime Notes
14. Do and Don't Guidance
15. Troubleshooting
16. Official Resources

## Scope and Primary APIs

Use this reference when you need Fluent-aligned iconography in Avalonia and want a precise answer to three questions:

- which public icon families fit Fluent best,
- how to choose the right icon semantics and visual treatment,
- which Avalonia icon path to use for each surface in `11.3.12`.

Primary APIs and surfaces:

- `PathIcon`
- `IconElement`
- `Path`
- `Geometry`, `StreamGeometry`, `PathGeometry`, `GeometryGroup`, `CombinedGeometry`
- `DrawingImage`, `GeometryDrawing`
- `Image`, `Bitmap`, `CroppedBitmap`, `IImage`
- `AssetLoader`
- `MenuItem.Icon`
- `NativeMenuItem.Icon`
- `WindowIcon`
- `TrayIcon.Icon`
- `MacOSProperties.IsTemplateIcon`
- `TextBlock`, `Run`, `FontFamily`

This file complements, not replaces:

- [`02-fluent-typography-layout-shape-and-iconography.md`](02-fluent-typography-layout-shape-and-iconography)
- [`35-path-icons-and-vector-geometry-assets.md`](../35-path-icons-and-vector-geometry-assets)
- [`55-tray-icons-and-system-tray-integration.md`](../55-tray-icons-and-system-tray-integration)
- [`48-toplevel-window-and-runtime-services.md`](../48-toplevel-window-and-runtime-services)

## Fluent Icon Rules Before You Pick a Library

For Fluent-style UI, icon quality is mostly a systems problem, not an asset-download problem.

Follow these rules first:

- choose one primary icon family for the product shell and command surfaces,
- keep command icons mostly single-color and let `Foreground`/theme resources drive their tone,
- use regular or outline icons for default/rest states and stronger or filled variants for selected/current states,
- align icon boxes to a consistent grid such as `16`, `20`, or `24`,
- pair icons with labels for destructive, rare, or domain-specific actions,
- do not rely on direction-only metaphors without RTL review,
- do not mix several stroke languages on the same toolbar, nav rail, or settings surface.

Fluent-specific guidance:

- use icons to reinforce a clear verb or noun, not to decorate empty space,
- reserve filled variants for selected, active, pinned, or emphasized states,
- keep icon density lower in desktop productivity shells than in mobile-first command bars,
- keep visual weight calmer than the text hierarchy around it.

## Public Icon Sets Worth Considering

Best-fit public sets for Avalonia apps:

| Set | Best use | Why it fits or does not fit Fluent |
| --- | --- | --- |
| Fluent System Icons | primary choice for Fluent apps | closest visual and metaphor fit to Microsoft Fluent, with regular and filled variants |
| Material Symbols | large coverage, cross-platform app suites | broad set and flexible delivery, but visually reads more Google than Microsoft |
| Lucide | neutral productivity tools | clean outline system, easy to convert to paths, but no Fluent filled/regular pairing model |
| Tabler Icons | dashboards and admin tools | broad OSS catalog with friendly stroke language; visually softer than Fluent |
| Heroicons | simple product and marketing-adjacent surfaces | strong set for clean outline/solid pairs, but stylistically web-oriented |
| Iconoir | broader expressive set | useful when breadth matters, but visual voice is less Fluent-native |

Practical selection rule:

- if the app is explicitly Fluent, start with Fluent System Icons,
- if you need very broad coverage and are willing to accept a different visual language, consider Material Symbols or Lucide,
- if your shell already uses one non-Fluent language, stay consistent instead of mixing families per feature.

Before adoption, verify:

- license compatibility for your product,
- availability of SVG or path export,
- whether the set provides size-specific assets or only one master drawing,
- whether the set offers filled/outline state pairs,
- whether the set contains the specialist domain icons you actually need.

## Avalonia Icon Delivery Options

Avalonia core gives you several valid icon paths, and each solves a different problem.

1. `PathIcon`
- Best for most Fluent command icons.
- Takes `Geometry` and inherits `Foreground`.

2. `Path`
- Best when the icon needs stroke control, multicolor layering, clipping, transforms, or composition with badges.

3. `DrawingImage` used through `Image`
- Best when the host surface expects `IImage` instead of a control, or when you want a reusable vector-backed image source.

4. `Image` with `Bitmap`
- Best for multicolor, branded, illustrated, or raster-only icon assets.

5. `TextBlock` or `Run` with an icon font
- Best when the library ships as a font and you want compact glyph delivery.
- Avalonia `11.3.12` does not provide a dedicated `FontIcon` or `SymbolIcon`; text rendering is the built-in path.

6. Platform icon types
- `WindowIcon` for `Window.Icon` and `TrayIcon.Icon`.
- `NativeMenuItem.Icon` for native menu exports, where the property is `Bitmap`.

## Recommended Fluent Workflow

For most Fluent apps:

1. Choose one public set, normally Fluent System Icons.
2. Export the icons you actually use as SVG or path data.
3. Normalize them to a small set of design grids, typically `16`, `20`, and `24`.
4. Store single-color command icons as shared `StreamGeometry` resources.
5. Surface those icons with `PathIcon` and shared size/foreground styles.
6. Use `Image`/`Bitmap` only for multicolor or brand-sensitive assets.
7. Use `WindowIcon` or `NativeMenuItem.Icon` for OS-level surfaces that do not consume `PathIcon`.

## `PathIcon` with Shared `StreamGeometry`

This is the default Fluent path for command bars, nav rows, list actions, settings pages, and empty-state supplements.

```xml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <Application.Resources>
    <StreamGeometry x:Key="Icon.MailRegular">M3 5H21V19H3Z M3 6.5L12 13L21 6.5</StreamGeometry>
    <StreamGeometry x:Key="Icon.MailFilled">M3 5H21V19H3Z</StreamGeometry>
  </Application.Resources>

  <Application.Styles>
    <Style Selector="PathIcon.fluent-command">
      <Setter Property="Width" Value="16" />
      <Setter Property="Height" Value="16" />
      <Setter Property="Foreground" Value="{DynamicResource TextControlForeground}" />
    </Style>
  </Application.Styles>
</Application>
```

```xml
<Button xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <StackPanel Orientation="Horizontal" Spacing="8">
    <PathIcon Classes="fluent-command"
              Data="{StaticResource Icon.MailRegular}" />
    <TextBlock VerticalAlignment="Center"
               Text="Inbox" />
  </StackPanel>
</Button>
```

Selected-state swap pattern:

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            Orientation="Horizontal"
            Spacing="8">
  <PathIcon Classes="fluent-command"
            Data="{Binding CurrentMailIcon}" />
  <TextBlock Text="Inbox" />
</StackPanel>
```

Use `PathIcon` when:

- the icon should follow text color,
- the icon is single-color,
- you want predictable sizing and theming,
- the surface is standard app UI, not OS shell chrome.

## `Path` and Geometry Composition for Advanced Cases

Use `Path` instead of `PathIcon` when the icon itself needs more control than a semantic icon element.

Examples:

- stroked icons from libraries that are not meant to be filled,
- two-layer icons,
- badge overlays,
- geometry transforms or custom clipping.

```xml
<Viewbox xmlns="https://github.com/avaloniaui"
         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
         Width="20"
         Height="20">
  <Canvas Width="20" Height="20">
    <Path Data="{StaticResource Icon.BellRegular}"
          Fill="{DynamicResource TextControlForeground}" />
    <Path Data="M14 2A4 4 0 1 1 14 10A4 4 0 1 1 14 2Z"
          Fill="#D13438" />
  </Canvas>
</Viewbox>
```

Geometry composition in code:

```csharp
using Avalonia;
using Avalonia.Media;

Geometry MakeBadgeIcon()
{
    var bell = StreamGeometry.Parse("M10 2C6.7 2 4 4.7 4 8V12L2.5 14V15H17.5V14L16 12V8C16 4.7 13.3 2 10 2Z");
    var badge = new EllipseGeometry(new Rect(12, 1, 6, 6));

    return new GeometryGroup
    {
        Children =
        {
            bell,
            badge
        }
    };
}
```

Use this path only when you genuinely need icon-level drawing control. For ordinary command symbols, `PathIcon` is simpler and more Fluent-friendly.

## `DrawingImage` plus `Image`

`DrawingImage` is useful when the consuming surface wants an `IImage` or when you want a reusable vector-backed image source.

```xml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <Application.Resources>
    <StreamGeometry x:Key="Icon.Search">M11 2A9 9 0 1 1 4.6 17.3L1 20.9L2.1 22L5.7 18.4A9 9 0 0 1 11 2Z</StreamGeometry>

    <DrawingImage x:Key="ImageIcon.Search">
      <DrawingImage.Drawing>
        <GeometryDrawing Brush="{DynamicResource TextControlForeground}"
                         Geometry="{StaticResource Icon.Search}" />
      </DrawingImage.Drawing>
    </DrawingImage>
  </Application.Resources>
</Application>
```

```xml
<Image xmlns="https://github.com/avaloniaui"
       xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
       Width="16"
       Height="16"
       Source="{StaticResource ImageIcon.Search}" />
```

Use `DrawingImage` when:

- you need a reusable `IImage`,
- the consumer is already built around `Image.Source`,
- you want to keep a vector source without dropping to raster.

## Raster Assets with `Image` and `Bitmap`

Use raster icons for:

- multicolor brand marks,
- detailed pictograms,
- photo-like or illustration-heavy assets,
- public icon sets that you do not want to convert to geometry.

Simple XAML pattern:

```xml
<Image xmlns="https://github.com/avaloniaui"
       xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
       Width="20"
       Height="20"
       Stretch="Uniform"
       Source="avares://MyApp/Assets/Icons/brand-mark.png" />
```

Code-loading pattern:

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media.Imaging;
using Avalonia.Platform;

using var stream = AssetLoader.Open(new Uri("avares://MyApp/Assets/Icons/brand-mark.png"));

var iconBitmap = new Bitmap(stream);
var image = new Image
{
    Width = 20,
    Height = 20,
    Source = iconBitmap
};
```

Sprite-sheet crop pattern:

```csharp
using Avalonia.Controls;
using Avalonia.Media.Imaging;
using Avalonia.Platform;

using var spriteStream = AssetLoader.Open(new Uri("avares://MyApp/Assets/Icons/toolbar-strip.png"));
var spriteSheet = new Bitmap(spriteStream);
var shareBitmap = new CroppedBitmap(spriteSheet, new PixelRect(32, 0, 16, 16));

var shareImage = new Image
{
    Width = 16,
    Height = 16,
    Source = shareBitmap
};
```

Important note:

- core Avalonia `11.3.12` does not expose a built-in SVG `Image` type in this repo's app-facing API map,
- if you want direct SVG-as-image workflows, use an ecosystem package and validate trimming, packaging, and rendering behavior separately,
- for Fluent command icons, converting SVG paths to shared `Geometry` resources is usually the cleaner core-Avalonia path.

## Icon Fonts with `TextBlock`

Some public icon libraries ship fonts. Avalonia can use them through normal text rendering.

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            Orientation="Horizontal"
            Spacing="8">
  <TextBlock FontFamily="avares://MyApp/Assets/Fonts#App Icons"
             FontSize="16"
             Foreground="{DynamicResource TextControlForeground}"
             Text="&#xE001;" />
  <TextBlock VerticalAlignment="Center"
             Text="Search" />
</StackPanel>
```

Use the resource directory or an embedded font collection URI for `FontFamily`; do not point `FontFamily` at a single `.ttf` file path.

Use icon fonts when:

- the source library is already delivered as a font,
- you want very compact asset distribution,
- the icons behave like glyphs in text runs.

Do not assume icon fonts are always the best answer:

- they are weaker for multicolor icons,
- glyph code points are harder to review than named geometry keys,
- per-icon optical tuning is usually clearer with path resources.

For Fluent desktop UI, icon fonts are usually a secondary option behind `PathIcon`.

## Menu, Native Menu, Window, and Tray Icons

Regular Avalonia menu items can host a control as `Icon`, so `PathIcon` works well there:

```xml
<MenuItem xmlns="https://github.com/avaloniaui"
          xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
          Header="_Settings">
  <MenuItem.Icon>
    <PathIcon Width="16"
              Height="16"
              Foreground="{DynamicResource TextControlForeground}"
              Data="{StaticResource Icon.SettingsRegular}" />
  </MenuItem.Icon>
</MenuItem>
```

Native menus use `Bitmap`, not `PathIcon`:

```csharp
using Avalonia.Controls;
using Avalonia.Media.Imaging;
using Avalonia.Platform;

using var bitmapStream = AssetLoader.Open(new Uri("avares://MyApp/Assets/Icons/menu-open.png"));

var nativeItem = new NativeMenuItem("Open")
{
    Icon = new Bitmap(bitmapStream)
};
```

Window and tray icons use `WindowIcon`:

```csharp
using Avalonia.Controls;
using Avalonia.Platform;

using var iconStream = AssetLoader.Open(new Uri("avares://MyApp/Assets/App/app-icon.ico"));
var appIcon = new WindowIcon(iconStream);

window.Icon = appIcon;
trayIcon.Icon = appIcon;
```

macOS tray note:

- for monochrome menu-bar style icons, set `MacOSProperties.IsTemplateIcon="True"` on the `TrayIcon`.

## Choosing the Right Representation

| Need | Best Avalonia option |
| --- | --- |
| single-color Fluent command icon | `PathIcon` + shared `StreamGeometry` |
| stroked or layered vector icon | `Path` + `Geometry` resources |
| reusable vector `IImage` | `DrawingImage` + `Image` |
| multicolor or brand icon | `Image` + `Bitmap` |
| icon font package | `TextBlock` with custom `FontFamily` |
| native menu icon | `NativeMenuItem.Icon` with `Bitmap` |
| window or tray icon | `WindowIcon` |

Default recommendation:

- `PathIcon` for in-app Fluent commands,
- `Bitmap` or `WindowIcon` for OS-level surfaces,
- icon fonts only when the asset pipeline already depends on them.

## AOT and Runtime Notes

- keep geometry dictionaries in compiled XAML instead of reparsing icon path strings per item,
- keep icon resources shared at app or theme scope,
- prefer explicit asset URIs (`avares://`) for fonts and bitmaps,
- do not assume an ecosystem SVG package is trimming-safe until you verify it in your own build,
- if icons come from plugins or remote configuration, parse once and cache the resulting `Geometry` or `Bitmap`.

## Do and Don't Guidance

Do:

- standardize icon sizes per surface,
- keep icon names semantic (`Icon.SaveRegular`, `Icon.SaveFilled`) instead of numeric,
- use icon pairs to express selected/current state,
- test icons in light, dark, high-contrast, and compact-density surfaces,
- review directional icons under RTL.

Do not:

- mix Fluent, Material, and outline-only OSS icons on the same command surface,
- use raster icons for every small command just because export is easy,
- use icon-only destructive actions without labels or automation names,
- let window, tray, and native-menu icons reuse command-bar assets blindly,
- animate icons constantly just because composition APIs exist.

## Troubleshooting

1. Icon looks blurry.
- The asset is raster and is being scaled across several sizes.
- Prefer vector or ship size-specific raster exports.

2. Icon disappears in dark theme.
- `Foreground` or `GeometryDrawing.Brush` is bound to the wrong resource.
- Validate contrast in both theme variants.

3. Icon font shows the wrong glyph.
- The code point does not match the shipped font file.
- The `FontFamily` URI or family name after `#` is wrong.

4. `PathIcon` clips at the edges.
- The source geometry was not normalized to the intended design box.
- Remove extra transforms or fix the exported SVG view box before conversion.

5. Native menu icon does not appear.
- `NativeMenuItem.Icon` expects a `Bitmap`, not a `PathIcon`.
- Validate platform support and actual menu export path.

6. Tray icon looks wrong on macOS.
- Use a monochrome template-style asset where appropriate.
- Set `MacOSProperties.IsTemplateIcon="True"` for menu-bar template behavior.

7. RTL makes the icon meaning ambiguous.
- Mirror or replace directional metaphors after localization review.
- Do not assume arrow direction alone conveys meaning globally.

## Official Resources

- Avalonia `PathIcon`: [docs.avaloniaui.net/docs/reference/controls/path-icon](https://docs.avaloniaui.net/docs/reference/controls/path-icon)
- Avalonia `Image`: [docs.avaloniaui.net/docs/reference/controls/image](https://docs.avaloniaui.net/docs/reference/controls/image)
- Avalonia assets: [docs.avaloniaui.net/docs/basics/user-interface/assets](https://docs.avaloniaui.net/docs/basics/user-interface/assets)
- Avalonia fonts: [docs.avaloniaui.net/docs/guides/styles-and-resources/how-to-use-fonts](https://docs.avaloniaui.net/docs/guides/styles-and-resources/how-to-use-fonts)
- Avalonia `DrawingImage` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Media_DrawingImage](https://api-docs.avaloniaui.net/docs/T_Avalonia_Media_DrawingImage)
- Avalonia `WindowIcon` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Controls_WindowIcon](https://api-docs.avaloniaui.net/docs/T_Avalonia_Controls_WindowIcon)
- Avalonia `NativeMenuItem.Icon` API: [api-docs.avaloniaui.net/docs/P_Avalonia_Controls_NativeMenuItem_Icon](https://api-docs.avaloniaui.net/docs/P_Avalonia_Controls_NativeMenuItem_Icon)
- Fluent 2 iconography: [fluent2.microsoft.design/iconography](https://fluent2.microsoft.design/iconography)
- Fluent System Icons: [github.com/microsoft/fluentui-system-icons](https://github.com/microsoft/fluentui-system-icons)
- Material Symbols: [fonts.google.com/icons](https://fonts.google.com/icons)
- Lucide icons: [lucide.dev/icons](https://lucide.dev/icons)
- Tabler Icons: [tabler.io/icons](https://tabler.io/icons)
- Heroicons: [heroicons.com](https://heroicons.com)
- Iconoir: [iconoir.com](https://iconoir.com)
