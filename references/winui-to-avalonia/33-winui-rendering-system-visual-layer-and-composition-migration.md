# WinUI Rendering System (Visual Layer, Composition) to Avalonia Rendering

## Table of Contents
1. Scope and APIs
2. WinUI Rendering Model
3. Avalonia Rendering Model
4. Conversion Example
5. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- `CompositionTarget.Rendering`
- `Compositor`, `SpriteVisual`, visual layer effects
- control templating and visual states for most UI updates

Primary Avalonia APIs:

- `Control.Render(DrawingContext)`
- `Visual.InvalidateVisual()`, `AffectsRender<T>(...)`
- compositor APIs and transitions/animations

## WinUI Rendering Model

WinUI supports retained rendering and composition effects through the Windows composition layer. In most apps, rendering changes should remain declarative (templates, states, theme resources).

## Avalonia Rendering Model

Avalonia renders visual-tree updates and supports custom rendering via `Render(DrawingContext)` plus compositor paths for advanced scenarios.

## Conversion Example

WinUI XAML:

```xaml
<Canvas x:Name="RenderHost" Width="220" Height="24" />
```

WinUI C#:

```csharp
CompositionTarget.Rendering += (_, __) =>
{
    MeterLevel = Math.Clamp(MeterLevel + 0.01, 0.0, 1.0);
};
```

Avalonia XAML:

```xaml
<local:RenderHostControl xmlns="https://github.com/avaloniaui"
                         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                         xmlns:local="using:MyApp.Controls"
                         Width="220"
                         Height="24" />
```

Avalonia C#:

```csharp
var timer = new DispatcherTimer(TimeSpan.FromMilliseconds(16), DispatcherPriority.Render, (_, _) =>
{
    MeterLevel = Math.Clamp(MeterLevel + 0.01, 0.0, 1.0);
    meterControl.InvalidateVisual();
});
timer.Start();
```

Avalonia custom control draw:

```csharp
public override void Render(DrawingContext context)
{
    base.Render(context);
    context.FillRectangle(Brushes.Black, Bounds);
}
```

## Migration Notes

1. Replace frame-loop logic with transitions/animations when possible.
2. Reserve custom drawing for hotspots; keep most visuals in templates/styles.
3. Separate layout invalidation from render invalidation.
