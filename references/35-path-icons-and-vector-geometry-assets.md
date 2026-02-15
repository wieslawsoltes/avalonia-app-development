# Path Icons and Vector Geometry Assets

## Table of Contents
1. Scope and APIs
2. PathIcon Rendering Model
3. Authoring Geometry Assets
4. Reusable Icon Patterns
5. Runtime Icon Construction
6. Best Practices
7. Troubleshooting

## Scope and APIs

Primary APIs:
- `PathIcon`
- `IconElement`
- `PathIcon.DataProperty`
- `Geometry.Parse(...)`
- `StreamGeometry.Parse(...)`
- `PathGeometry.Parse(...)`
- `Geometry.Transform`

Reference source files:
- `src/Avalonia.Controls/PathIcon.cs`
- `src/Avalonia.Controls/IconElement.cs`
- `src/Avalonia.Themes.Fluent/Controls/PathIcon.xaml`
- `src/Avalonia.Themes.Simple/Controls/PathIcon.xaml`
- `src/Avalonia.Base/Media/Geometry.cs`
- `src/Avalonia.Base/Media/StreamGeometry.cs`
- `src/Avalonia.Base/Media/PathGeometry.cs`

## PathIcon Rendering Model

`PathIcon` is a lightweight templated icon control:
- `PathIcon.Data` contains the vector geometry.
- Theme templates render a `Path` inside a `Viewbox`.
- `Foreground` drives fill color.
- `Width`/`Height` define icon size.

Practical implication:
- Keep icon geometry normalized and let layout scale it.
- Prefer `PathIcon` over raw `Path` when representing semantic UI icons.

## Authoring Geometry Assets

Store icon geometry in shared resources:

```xml
<Application.Resources>
  <StreamGeometry x:Key="Icon.Settings">M14 9.5C11.5 9.5 9.5 11.5 9.5 14C9.5 16.5 11.5 18.5 14 18.5C16.5 18.5 18.5 16.5 18.5 14C18.5 11.5 16.5 9.5 14 9.5Z</StreamGeometry>
  <StreamGeometry x:Key="Icon.Search">M11 2A9 9 0 1 1 4.6 17.3L1 20.9L2.1 22L5.7 18.4A9 9 0 0 1 11 2Z</StreamGeometry>
</Application.Resources>
```

Use them with `PathIcon`:

```xml
<Button xmlns="https://github.com/avaloniaui">
  <StackPanel Orientation="Horizontal" Spacing="8">
    <PathIcon Width="16" Height="16" Data="{StaticResource Icon.Settings}" />
    <TextBlock VerticalAlignment="Center" Text="Settings" />
  </StackPanel>
</Button>
```

## Reusable Icon Patterns

Centralize size and color with style:

```xml
<Style Selector="PathIcon.app-icon">
  <Setter Property="Width" Value="16" />
  <Setter Property="Height" Value="16" />
  <Setter Property="Foreground" Value="{DynamicResource TextControlForeground}" />
</Style>
```

Usage:

```xml
<PathIcon Classes="app-icon" Data="{StaticResource Icon.Search}" />
```

When you need direct path drawing behavior instead of semantic icon behavior, use `Shapes.Path`.

## Runtime Icon Construction

```csharp
using Avalonia.Controls;
using Avalonia.Media;

public static class AppIcons
{
    public static readonly Geometry Search = Geometry.Parse("M11 2A9 9 0 1 1 4.6 17.3L1 20.9L2.1 22L5.7 18.4A9 9 0 0 1 11 2Z");
}

var icon = new PathIcon
{
    Data = AppIcons.Search,
    Width = 16,
    Height = 16
};
```

Use code construction for generated icons or plugin-delivered path data.

## Best Practices

- Keep geometry assets in app/theme resources, not inline in every control.
- Use `PathIcon` for icon semantics; use `Shapes.Path` for arbitrary vector layout.
- Bind `Foreground` from theme resources so icons follow theme variants.
- Keep icon bounds consistent (for example 16x16 or 24x24 design grid).
- Avoid frequent runtime reparsing of path strings in hot paths.

## Troubleshooting

1. Icon not visible:
- `Data` is `null` or invalid path data.
- `Foreground` is transparent or same as background.

2. Icon appears stretched unexpectedly:
- Host layout forces non-square area.
- Explicit `Width`/`Height` mismatch expected aspect ratio.

3. Icon clips at edges:
- Geometry coordinates exceed expected design box.
- Margin/padding or container clipping is too aggressive.

4. Theme color does not apply:
- Local value overrides `Foreground`.
- Resource key mismatch between app and selected theme.
