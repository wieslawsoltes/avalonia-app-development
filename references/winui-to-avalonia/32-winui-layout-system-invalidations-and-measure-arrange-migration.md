# WinUI Layout System Invalidations and Measure/Arrange Migration to Avalonia

## Table of Contents
1. Scope and APIs
2. WinUI Layout Model
3. Avalonia Layout Model
4. Conversion Example
5. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- `MeasureOverride(Size)`, `ArrangeOverride(Size)`
- `UIElement.InvalidateMeasure()`, `UIElement.InvalidateArrange()`
- `FrameworkElement.UpdateLayout()`
- layout panels (`Grid`, `StackPanel`, `RelativePanel`, `ScrollViewer`)

Primary Avalonia APIs:

- `MeasureOverride(Size)`, `ArrangeOverride(Size)`
- `Layoutable.InvalidateMeasure()`, `Layoutable.InvalidateArrange()`
- `Layoutable.UpdateLayout()`
- `Grid`, `StackPanel`, `RelativePanel`, `ScrollViewer`

## WinUI Layout Model

WinUI layout runs as queued measure/arrange passes. Property changes invalidate measure or arrange and the framework resolves layout in a pass before rendering.

## Avalonia Layout Model

Avalonia uses a similar invalidation-based pass model through `LayoutManager`. The key migration rule is to keep layout-affecting state separated from rendering-only state.

## Conversion Example

WinUI XAML:

```xaml
<local:TilePanel>
  <Button Content="One" />
  <Button Content="Two" />
  <Button Content="Three" />
</local:TilePanel>
```

WinUI C#:

```csharp
public sealed class TilePanel : Panel
{
    protected override Size MeasureOverride(Size availableSize)
    {
        foreach (var child in Children)
        {
            child.Measure(new Size(200, 120));
        }
        return availableSize;
    }

    protected override Size ArrangeOverride(Size finalSize)
    {
        var x = 0.0;
        foreach (var child in Children)
        {
            child.Arrange(new Rect(x, 0, 200, 120));
            x += 208;
        }
        return finalSize;
    }
}
```

Avalonia XAML:

```xaml
<local:TilePanel xmlns="https://github.com/avaloniaui"
                 xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                 xmlns:local="using:MyApp.Controls">
  <Button Content="One" />
  <Button Content="Two" />
  <Button Content="Three" />
</local:TilePanel>
```

Avalonia C#:

```csharp
public sealed class TilePanel : Panel
{
    protected override Size MeasureOverride(Size availableSize)
    {
        foreach (var child in Children)
        {
            child.Measure(new Size(200, 120));
        }
        return availableSize;
    }

    protected override Size ArrangeOverride(Size finalSize)
    {
        var x = 0.0;
        foreach (var child in Children)
        {
            child.Arrange(new Rect(x, 0, 200, 120));
            x += 208;
        }
        return finalSize;
    }
}
```

## Migration Notes

1. Avoid `UpdateLayout()` in normal command paths; prefer invalidation.
2. Keep `LayoutUpdated` handlers side-effect free.
3. Port custom panel math first, then optimize for virtualization/recycling.
