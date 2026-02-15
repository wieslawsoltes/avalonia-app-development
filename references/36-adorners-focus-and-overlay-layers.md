# Adorners, Focus Visuals, and Overlay Layers

## Table of Contents
1. Scope and APIs
2. Adorner Layer Architecture
3. Focus Adorner Pipeline
4. Attaching Custom Adorners
5. Clipping and Transform Behavior
6. Theming Default Focus Adorners
7. Best Practices
8. Troubleshooting

## Scope and APIs

Primary APIs:
- `AdornerLayer`
- `AdornerLayer.GetAdornerLayer(...)`
- `AdornerLayer.AdornerProperty`
- `AdornerLayer.AdornedElementProperty`
- `AdornerLayer.IsClipEnabledProperty`
- `AdornerLayer.DefaultFocusAdorner`
- `Control.FocusAdorner`
- `FocusAdornerTemplate`
- `VisualLayerManager.AdornerLayer`

Reference source files:
- `src/Avalonia.Controls/Primitives/AdornerLayer.cs`
- `src/Avalonia.Controls/Control.cs`
- `src/Avalonia.Controls/Primitives/VisualLayerManager.cs`
- `src/Markup/Avalonia.Markup.Xaml/Templates/FocusAdornerTemplate.cs`
- `src/Avalonia.Themes.Fluent/Controls/AdornerLayer.xaml`
- `src/Avalonia.Themes.Simple/Controls/AdornerLayer.xaml`
- `samples/ControlCatalog/Pages/AdornerLayerPage.xaml`

## Adorner Layer Architecture

`AdornerLayer` is an overlay `Canvas` managed by `VisualLayerManager`.

Use cases:
- Focus visuals.
- Temporary interaction overlays.
- Selection/highlight overlays that must stay above normal content.

Attachment model:
- Set `AdornerLayer.Adorner` on the adorned visual.
- Link adorner to target via `AdornerLayer.AdornedElement`.

## Focus Adorner Pipeline

Control focus visuals are adorner-backed:
- `Control.FocusAdorner` provides per-control template override.
- If not set, `AdornerLayer.DefaultFocusAdorner` is used.
- Focus adorner is shown when focus comes from keyboard directional or tab navigation.

This is why mouse focus may not show the same focus adorner behavior by default.

## Attaching Custom Adorners

XAML pattern:

```xml
<Button xmlns="https://github.com/avaloniaui"
        Content="Adorned Button">
  <AdornerLayer.Adorner>
    <Canvas IsHitTestVisible="False"
            Background="#3300D4FF"
            AdornerLayer.IsClipEnabled="False">
      <Line StartPoint="-10000,0" EndPoint="10000,0" Stroke="#00D4FF" StrokeThickness="1" />
      <Line StartPoint="0,-10000" EndPoint="0,10000" Stroke="#00D4FF" StrokeThickness="1" />
    </Canvas>
  </AdornerLayer.Adorner>
</Button>
```

Code pattern:

```csharp
using Avalonia.Controls;
using Avalonia.Controls.Primitives;
using Avalonia.Media;

var adorner = new Border
{
    BorderBrush = Brushes.DeepSkyBlue,
    BorderThickness = new Thickness(2),
    IsHitTestVisible = false
};

AdornerLayer.SetIsClipEnabled(adorner, false);
AdornerLayer.SetAdorner(targetControl, adorner);
```

Remove adorner when done:

```csharp
AdornerLayer.SetAdorner(targetControl, null);
```

## Clipping and Transform Behavior

`AdornerLayer` tracks adorned bounds and arranges overlays accordingly.

Important controls:
- `AdornerLayer.IsClipEnabled`: clip to adorned bounds when `true`.
- Render transform propagation: adorner follows adorned visual transforms.

Use `IsClipEnabled="False"` for crosshair/ruler overlays that intentionally extend outside bounds.

## Theming Default Focus Adorners

Override the default focus adorner template through `AdornerLayer` theme:

```xml
<ControlTheme xmlns="https://github.com/avaloniaui"
              xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
              x:Key="{x:Type AdornerLayer}"
              TargetType="AdornerLayer">
  <Setter Property="DefaultFocusAdorner">
    <FocusAdornerTemplate>
      <Border BorderThickness="2" BorderBrush="DodgerBlue" />
    </FocusAdornerTemplate>
  </Setter>
</ControlTheme>
```

Per-control opt-out:

```xml
<TextBox FocusAdorner="{x:Null}" />
```

## Best Practices

- Keep adorners non-interactive (`IsHitTestVisible="False"`) unless interaction is required.
- Prefer declarative focus adorners in themes for consistency.
- Remove temporary adorners explicitly when workflow completes.
- Use clipping intentionally; disable it only for overlays that must exceed bounds.
- Keep adorner visuals lightweight to avoid layout/render overhead.

## Troubleshooting

1. Adorner does not appear:
- No adorner layer in visual ancestry.
- `AdornerLayer.Adorner` not set or set to `null`.

2. Focus ring does not show:
- Focus came from pointer, not tab/directional navigation.
- `FocusAdorner` and `DefaultFocusAdorner` are both unset/null.

3. Adorner is misaligned:
- Adorned control bounds not what you expect after layout.
- Additional transforms applied to parent chain.

4. Adorner is clipped unexpectedly:
- `AdornerLayer.IsClipEnabled` is still `true`.
