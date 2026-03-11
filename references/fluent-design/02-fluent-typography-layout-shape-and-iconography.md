# Fluent Typography, Layout, Shape, and Iconography in Avalonia

## Scope and Primary APIs

Use this reference to shape Fluent visual tone beyond just colors.

Primary APIs:
- `TextBlock`, `TextElement.FontFamily`, `FontWeight`
- `PathIcon`
- `Grid`, `StackPanel`, `SplitView`
- `CornerRadius`, `Thickness`

## Typography Guidance

- Keep a restrained type ramp.
- Prefer sentence case.
- Use stronger weight before larger size when hierarchy is shallow.
- If cross-platform consistency matters, prefer one explicit UI family instead of depending on platform drift.

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            Spacing="4">
  <TextBlock FontSize="30" FontWeight="SemiBold" Text="Release center" />
  <TextBlock Foreground="{DynamicResource Brush.Text.Secondary}"
             Text="Ship Fluent UI with calm spacing and direct copy." />
</StackPanel>
```

## Layout and Shape

- Use clear rails, header bands, and grouped content regions.
- Keep shape tokens limited: small, medium, and large corners are enough for most apps.
- Increase spacing between groups before adding decorative separators.

## Iconography

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            Orientation="Horizontal"
            Spacing="8">
  <PathIcon Data="{StaticResource Icon.Deploy}" />
  <TextBlock Text="Deploy" FontWeight="SemiBold" />
</StackPanel>
```

Guidance:
- keep most command icons single-color,
- pair icons with labels for destructive or high-risk actions,
- align icon size and padding with the surrounding text rhythm.

For public icon-set selection, library sourcing, and all Avalonia icon-delivery options, see [`13-fluent-icons-public-icon-sets-selection-and-avalonia-usage.md`](13-fluent-icons-public-icon-sets-selection-and-avalonia-usage).

## AOT and Runtime Notes

- Keep icon geometry resources shared and compiled.
- Avoid per-view duplicated typography styles when a global role system exists.

## Do and Don't Guidance

Do:
- reuse a small shape scale,
- define type roles for headers, body, and metadata,
- let layout spacing carry hierarchy.

Do not:
- mix many corner-radius systems,
- use oversized display text for routine productivity surfaces,
- treat icons as decoration with no semantic role.

## Troubleshooting

1. Fluent UI still feels generic.
- Tighten content hierarchy and shell spacing; palette alone will not create Fluent tone.

2. Command bars feel crowded.
- Reduce concurrent actions, align icon sizes, and simplify the label hierarchy.

3. Typography drifts between views.
- Centralize text roles into shared styles rather than view-local ad hoc values.

## Official Resources

- Fluent 2 typography: [fluent2.microsoft.design/typography](https://fluent2.microsoft.design/typography)
- Fluent 2 layout: [fluent2.microsoft.design/layout](https://fluent2.microsoft.design/layout)
- Fluent 2 iconography: [fluent2.microsoft.design/iconography](https://fluent2.microsoft.design/iconography)
- Fluent 2 corner radius: [fluent2.microsoft.design/styles/corner-radius](https://fluent2.microsoft.design/styles/corner-radius/)
