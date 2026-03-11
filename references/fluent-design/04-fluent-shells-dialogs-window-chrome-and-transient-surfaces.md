# Fluent Shells, Dialogs, Window Chrome, and Transient Surfaces

## Scope and Primary APIs

Use this reference to shape Fluent shell behavior and transient surfaces.

Primary APIs:
- `Window`, `TopLevel`
- custom decoration properties from the Avalonia windowing stack
- `FlyoutPresenter`, `MenuFlyout`, `ContextMenu`
- `WindowNotificationManager`
- `ExperimentalAcrylicBorder`

## Shell Guidance

- Use clear header, rail, and content regions.
- Keep shell chrome quieter than content surfaces.
- Use translucent or acrylic accents sparingly for rails, title areas, or special panes.

## Overlay Surface Example

```xml
<ControlTheme xmlns="https://github.com/avaloniaui"
              xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
              x:Key="FluentFlyoutPresenterTheme"
              TargetType="FlyoutPresenter"
              BasedOn="{StaticResource {x:Type FlyoutPresenter}}">
  <Setter Property="Background" Value="{DynamicResource Brush.Surface.Card}" />
  <Setter Property="BorderBrush" Value="{DynamicResource Brush.Border.Subtle}" />
  <Setter Property="BorderThickness" Value="1" />
  <Setter Property="CornerRadius" Value="12" />
  <Setter Property="Padding" Value="6" />
</ControlTheme>
```

## Window Chrome Guidance

- Prefer system-respecting chrome unless the app has a strong shell reason not to.
- If customizing window chrome, preserve hit targets, drag regions, and contrast.
- Treat title bars and side rails as part of the same shell token system.

## AOT and Runtime Notes

- Keep shell and overlay themes in shared dictionaries.
- Avoid runtime XAML-loading for window chrome experiments unless the scenario explicitly needs it.

## Do and Don't Guidance

Do:
- theme dialogs, flyouts, menus, and notifications with the same token family,
- keep overlay spacing tighter than page spacing,
- use acrylic where it adds context, not everywhere.

Do not:
- style flyouts and dialogs as unrelated micro-products,
- trade usability for decorative custom chrome,
- depend on transparency for critical text contrast.

## Troubleshooting

1. Overlays feel disconnected from the shell.
- Align radius, surface, border, and shadow rules across all transient surfaces.

2. Custom title area feels fragile.
- Re-check drag regions, focus states, and text contrast under both variants.

3. In-app notifications look bolted on.
- Theme notification surfaces with the same shell tokens and spacing rules.

## Official Resources

- Fluent 2 layout: [fluent2.microsoft.design/layout](https://fluent2.microsoft.design/layout)
- Fluent 2 onboarding: [fluent2.microsoft.design/onboarding](https://fluent2.microsoft.design/onboarding/)
