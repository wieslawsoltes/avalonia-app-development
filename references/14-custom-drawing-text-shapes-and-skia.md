# Custom Drawing, Text, Shapes, and SkiaSharp

## Table of Contents
1. Scope and APIs
2. Custom Drawing in Controls
3. Custom Draw Operations
4. Text Rendering APIs
5. Shape Rendering APIs
6. Working with SkiaSharp
7. Best Practices
8. Troubleshooting

## Scope and APIs

Primary APIs:
- `Control.Render(DrawingContext)`
- `DrawingContext` drawing methods (`DrawLine`, `DrawGeometry`, `DrawRectangle`, `DrawEllipse`, `DrawText`, `DrawGlyphRun`)
- `DrawingContext.Custom(ICustomDrawOperation)`
- `ICustomDrawOperation`
- `FormattedText`
- `TextLayout`
- `GlyphRun`
- `Shape` and derived controls (`Rectangle`, `Ellipse`, `Path`, `Line`, etc.)
- `ISkiaSharpApiLeaseFeature`
- `Avalonia.Skia.Helpers.DrawingContextHelper`

Reference source files:
- `src/Avalonia.Base/Media/DrawingContext.cs`
- `src/Avalonia.Base/Rendering/SceneGraph/CustomDrawOperation.cs`
- `src/Avalonia.Base/Media/FormattedText.cs`
- `src/Avalonia.Base/Media/TextFormatting/TextLayout.cs`
- `src/Avalonia.Base/Media/GlyphRun.cs`
- `src/Avalonia.Controls/Shapes/Shape.cs`
- `src/Skia/Avalonia.Skia/ISkiaSharpApiLeaseFeature.cs`
- `src/Skia/Avalonia.Skia/Helpers/DrawingContextHelper.cs`
- `samples/RenderDemo/Pages/CustomSkiaPage.cs`

## Custom Drawing in Controls

Use `Render(DrawingContext context)` for direct immediate-mode drawing:

```csharp
public sealed class ChartSurface : Control
{
    public override void Render(DrawingContext context)
    {
        base.Render(context);

        context.DrawRectangle(Brushes.Black, null, new Rect(Bounds.Size));
        context.DrawLine(new Pen(Brushes.Lime, 2), new Point(0, Bounds.Height), new Point(Bounds.Width, 0));
    }
}
```

## Custom Draw Operations

Use `ICustomDrawOperation` when you need backend-specific access (for example Skia lease features).

Pattern:
1. Implement `Bounds`, `HitTest`, `Render`, and `Dispose`.
2. In control render, call `context.Custom(op)`.

```csharp
public override void Render(DrawingContext context)
{
    context.Custom(new MyCustomDrawOp(new Rect(Bounds.Size)));
}
```

From the sample, inside custom op:
- Probe `context.TryGetFeature<ISkiaSharpApiLeaseFeature>()`
- If available, use leased `SKCanvas`
- If unavailable, fallback to Avalonia drawing primitives

## Text Rendering APIs

Use:
- `FormattedText` for simpler formatted text scenarios
- `TextLayout` for multiline measurement/hit-testing and advanced flow
- `GlyphRun` for low-level text rendering and custom glyph operations

Typical flow for advanced text:
1. Build `TextLayout` with typeface, size, wrapping, trimming.
2. Read metrics (`Width`, `Height`, `Baseline`, etc.).
3. Call `TextLayout.Draw(context, origin)`.
4. Use hit test methods when needed (`HitTestTextPosition`, ranges).

## Shape Rendering APIs

Use built-in shape controls when possible:
- `Shape.Fill`
- `Shape.Stroke`
- `Shape.StrokeThickness`
- `Shape.StrokeDashArray`
- `Shape.Stretch`

`Shape.Render` ultimately draws geometry with `DrawingContext.DrawGeometry`.

Guidance:
- Prefer shape controls for declarative XAML and styling.
- Prefer custom `Render` only for highly specialized visuals.

## Working with SkiaSharp

### In-process Skia access during rendering

```csharp
if (context.TryGetFeature<ISkiaSharpApiLeaseFeature>(out var leaseFeature))
{
    using var lease = leaseFeature.Lease();
    var canvas = lease.SkCanvas;
    // Skia drawing here
}
```

### Render Avalonia visual to external SKCanvas

Use helper:
- `Avalonia.Skia.Helpers.DrawingContextHelper.RenderAsync(SKCanvas, Visual, Rect, dpi)`

This is useful when rendering into non-Avalonia canvas hosts.

## Best Practices

- Keep `Render` allocation-light.
- Reuse pens/brushes/geometries where possible.
- Fallback gracefully when backend features are unavailable.
- Use Avalonia primitives first; drop to Skia only when needed.
- Invalidate only necessary regions/frames.

## Troubleshooting

1. Nothing is drawn:
- `Bounds` may be zero.
- Brush/pen is null for expected draw path.
- Clipping or transform hides content.

2. Custom draw op runs but no Skia feature:
- Current backend/context is not exposing `ISkiaSharpApiLeaseFeature`.
- Implement fallback path with `ImmediateDrawingContext`.

3. Text appears blurry or mismeasured:
- Mismatch in DPI assumptions or font setup.
- Use `TextLayout` metrics and avoid ad-hoc baseline math.

4. Frequent redraw causes jank:
- Avoid unconditional per-frame `InvalidateVisual` without throttling.
- Use request-frame scheduling APIs intentionally.

## XAML-First and Code-Only Usage

Default mode:
- Declare drawing surfaces and shapes in XAML first.
- Use code-only drawing setup only when requested.

XAML-first references:
- `Shape` controls (`Path`, `Rectangle`, `Ellipse`)
- Control declarations hosting custom render controls

XAML-first usage example:

```xml
<Grid xmlns="https://github.com/avaloniaui"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      xmlns:local="using:MyApp.Controls">
  <Path Stroke="DodgerBlue"
        StrokeThickness="2"
        Data="M 10,10 L 110,10 110,60 Z" />

  <local:ChartSurface Width="320" Height="180" />
</Grid>
```

Code-only alternative (on request):

```csharp
var surface = new ChartSurface
{
    Width = 320,
    Height = 180
};
```
