# Microsoft Fluent Design and `FluentTheme` in Avalonia

## Table of Contents
1. Scope and Coverage Contract
2. Fluent Workflow
3. Granular Reference Set
4. Full API Coverage Pointers
5. First Example
6. AOT and Runtime Notes
7. Official Design Resources

## Scope and Coverage Contract

This reference lane covers how to build Fluent-inspired Avalonia apps with:

- `FluentTheme` bootstrap and density control,
- palette customization through `ColorPaletteResources`,
- semantic token mapping on top of Fluent palette resources,
- Fluent-shaped control themes, shells, overlays, and command surfaces,
- material, elevation, motion, accessibility, wait UX, and content-tone guidance,
- Fluent language-system rules for labels, commands, teaching, and recovery copy,
- Fluent page-transition and composition-animation recipes for shell polish,
- Fluent navigation, productivity-shell, notification, and risk-language patterns.
- Fluent public icon-set selection and Avalonia-specific icon delivery patterns.

Coverage intent for this lane:

- stay accurate to Avalonia `11.3.12`,
- use `FluentTheme` as the baseline instead of reinventing a parallel design system,
- split detail into smaller topic files so tasks can load only what they need.

## Fluent Workflow

1. Start with `FluentTheme`, theme variants, and density.
2. Configure `FluentTheme.Palettes` only for palette-level decisions.
3. Build semantic tokens on top of `SystemAccent*`, `SystemBase*`, and `SystemChrome*` resources.
4. Add Fluent-aligned component and shell themes.
5. Define Fluent command language, teaching patterns, and content review rules.
6. Finish with material, motion, composition, accessibility, content, and wait UX review.

## Granular Reference Set

All detailed Fluent references now live under [`fluent-design/README.md`](fluent-design/README):

- [`00-fluent-theme-bootstrap-density-and-palette-customization.md`](fluent-design/00-fluent-theme-bootstrap-density-and-palette-customization)
- [`01-fluent-alias-tokens-brand-mapping-materials-and-elevation.md`](fluent-design/01-fluent-alias-tokens-brand-mapping-materials-and-elevation)
- [`02-fluent-typography-layout-shape-and-iconography.md`](fluent-design/02-fluent-typography-layout-shape-and-iconography)
- [`03-fluent-controls-navigation-and-command-surfaces.md`](fluent-design/03-fluent-controls-navigation-and-command-surfaces)
- [`04-fluent-shells-dialogs-window-chrome-and-transient-surfaces.md`](fluent-design/04-fluent-shells-dialogs-window-chrome-and-transient-surfaces)
- [`05-fluent-motion-content-wait-ux-and-accessibility-recipes.md`](fluent-design/05-fluent-motion-content-wait-ux-and-accessibility-recipes)
- [`06-fluent-language-system-content-commanding-and-teaching-patterns.md`](fluent-design/06-fluent-language-system-content-commanding-and-teaching-patterns)
- [`07-fluent-motion-composition-and-depth-recipes.md`](fluent-design/07-fluent-motion-composition-and-depth-recipes)
- [`08-fluent-navigation-information-architecture-and-productivity-shells.md`](fluent-design/08-fluent-navigation-information-architecture-and-productivity-shells)
- [`09-fluent-language-system-status-confirmation-and-notification-patterns.md`](fluent-design/09-fluent-language-system-status-confirmation-and-notification-patterns)
- [`10-fluent-advanced-composition-implicit-expression-and-shell-choreography.md`](fluent-design/10-fluent-advanced-composition-implicit-expression-and-shell-choreography)
- [`11-fluent-localization-bidi-and-inclusive-content-patterns.md`](fluent-design/11-fluent-localization-bidi-and-inclusive-content-patterns)
- [`12-fluent-touch-gesture-posture-and-motion-feedback.md`](fluent-design/12-fluent-touch-gesture-posture-and-motion-feedback)
- [`13-fluent-icons-public-icon-sets-selection-and-avalonia-usage.md`](fluent-design/13-fluent-icons-public-icon-sets-selection-and-avalonia-usage)

## Full API Coverage Pointers

For exhaustive lookup beyond these Fluent-specific docs:

- styles/resources/themes: [`04-styles-themes-resources.md`](04-styles-themes-resources), [`17-resources-assets-theme-variants-and-xmlns.md`](17-resources-assets-theme-variants-and-xmlns)
- control themes and templates: [`10-templated-controls-and-control-themes.md`](10-templated-controls-and-control-themes)
- shell and windows: [`13-windowing-and-custom-decorations.md`](13-windowing-and-custom-decorations), [`48-toplevel-window-and-runtime-services.md`](48-toplevel-window-and-runtime-services)
- menus and overlays: [`25-popups-flyouts-tooltips-and-overlays.md`](25-popups-flyouts-tooltips-and-overlays), [`53-menu-controls-contextmenu-and-menuflyout-patterns.md`](53-menu-controls-contextmenu-and-menuflyout-patterns)
- color, text, and vector assets: [`35-path-icons-and-vector-geometry-assets.md`](35-path-icons-and-vector-geometry-assets), [`59-media-colors-brushes-and-formatted-text-practical-usage.md`](59-media-colors-brushes-and-formatted-text-practical-usage)
- icon delivery on app and OS surfaces: [`13-fluent-icons-public-icon-sets-selection-and-avalonia-usage.md`](fluent-design/13-fluent-icons-public-icon-sets-selection-and-avalonia-usage), [`48-toplevel-window-and-runtime-services.md`](48-toplevel-window-and-runtime-services), [`53-menu-controls-contextmenu-and-menuflyout-patterns.md`](53-menu-controls-contextmenu-and-menuflyout-patterns), [`55-tray-icons-and-system-tray-integration.md`](55-tray-icons-and-system-tray-integration)
- signatures: [`api-index-generated.md`](api-index-generated)

## First Example

```xml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             RequestedThemeVariant="Default">
  <Application.Styles>
    <FluentTheme DensityStyle="Compact">
      <FluentTheme.Palettes>
        <ColorPaletteResources x:Key="Light"
                               Accent="#0F6CBD"
                               RegionColor="#FFFFFFFF" />
        <ColorPaletteResources x:Key="Dark"
                               Accent="#4CC2FF"
                               RegionColor="#FF111111" />
      </FluentTheme.Palettes>
    </FluentTheme>
  </Application.Styles>
</Application>
```

## AOT and Runtime Notes

- Keep `FluentTheme` setup in compiled XAML by default.
- Treat `Accent` as the main live palette override path; broader palette changes should be validated carefully.
- Keep semantic app tokens separate from raw `System*` resource names.

## Official Design Resources

- Avalonia Fluent theme docs: [docs.avaloniaui.net/docs/basics/user-interface/styling/themes/fluent](https://docs.avaloniaui.net/docs/basics/user-interface/styling/themes/fluent)
- Avalonia `FluentTheme` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Themes_Fluent_FluentTheme](https://api-docs.avaloniaui.net/docs/T_Avalonia_Themes_Fluent_FluentTheme)
- Avalonia `ColorPaletteResources` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Themes_Fluent_ColorPaletteResources](https://api-docs.avaloniaui.net/docs/T_Avalonia_Themes_Fluent_ColorPaletteResources)
- Avalonia `Compositor` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Compositor](https://api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Compositor)
- Fluent 2 design principles: [fluent2.microsoft.design/design-principles](https://fluent2.microsoft.design/design-principles)
- Fluent 2 content design: [fluent2.microsoft.design/content-design](https://fluent2.microsoft.design/content-design)
- Fluent 2 color: [fluent2.microsoft.design/styles/color](https://fluent2.microsoft.design/styles/color/)
- Fluent 2 motion: [fluent2.microsoft.design/styles/motion](https://fluent2.microsoft.design/styles/motion/)
- Fluent 2 accessibility: [fluent2.microsoft.design/accessibility](https://fluent2.microsoft.design/accessibility)
