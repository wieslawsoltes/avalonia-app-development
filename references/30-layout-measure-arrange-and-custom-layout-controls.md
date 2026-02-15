# Layout Measure/Arrange Pass and Custom Controls/Panels

## Table of Contents
1. Scope and APIs
2. How Measure Pass Works
3. How Arrange Pass Works
4. Building a Custom Layout Control
5. Building a Custom Panel
6. Invalidation and Performance Strategy
7. XAML-First and Code-Only Usage
8. Troubleshooting

## Scope and APIs

Primary APIs:
- `Layoutable.Measure(Size)`
- `Layoutable.Arrange(Rect)`
- `Layoutable.MeasureOverride(Size)`
- `Layoutable.ArrangeOverride(Size)`
- `Layoutable.DesiredSize`
- `Layoutable.IsMeasureValid`
- `Layoutable.IsArrangeValid`
- `Layoutable.InvalidateMeasure()`
- `Layoutable.InvalidateArrange()`
- `Layoutable.AffectsMeasure<T>(...)`
- `Layoutable.AffectsArrange<T>(...)`
- `Panel.Children`
- `Panel.AffectsParentMeasure<TPanel>(...)`
- `Panel.AffectsParentArrange<TPanel>(...)`

Reference source files:
- `src/Avalonia.Base/Layout/Layoutable.cs`
- `src/Avalonia.Controls/Panel.cs`
- `src/Avalonia.Base/Layout/LayoutManager.cs`

## How Measure Pass Works

Measure computes requested size (`DesiredSize`) under parent constraints.

Pass model:
1. Parent calls `child.Measure(availableSize)`.
2. Child runs `MeasureOverride(availableSize)` if invalid or size changed.
3. Child sets `DesiredSize`.
4. Parent uses `DesiredSize` to compute its own size.

Rules for authoring `MeasureOverride`:
- Treat `availableSize` as an upper bound, not a target size.
- Measure each child with the constraints it should live under.
- Return the minimum size required to represent content correctly.
- Avoid side effects and property writes that trigger more layout.

Important behavior:
- If child desired size changes, parent is invalidated via layout pipeline.
- `Width`/`Height`/`Min*`/`Max*`/`Margin`/alignment properties affect measure by default on `Layoutable`.

## How Arrange Pass Works

Arrange finalizes geometry and sets bounds.

Pass model:
1. Parent decides final rectangle for each child.
2. Parent calls `child.Arrange(rect)`.
3. Child runs `ArrangeOverride(finalSize)` if invalid or rect changed.
4. Child `Bounds` are updated.

Rules for authoring `ArrangeOverride`:
- Place and size children deterministically.
- Use the passed `finalSize` as actual available arrangement space.
- Return final arranged size for the control.
- Do not perform expensive work that belongs in render or data preprocessing.

## Building a Custom Layout Control

For a single-child layout behavior, derive from `Decorator` and control child sizing/placement.

```csharp
using Avalonia;
using Avalonia.Controls;

public class AspectRatioDecorator : Decorator
{
    public static readonly StyledProperty<double> AspectRatioProperty =
        AvaloniaProperty.Register<AspectRatioDecorator, double>(
            nameof(AspectRatio), 16d / 9d);

    static AspectRatioDecorator()
    {
        AffectsMeasure<AspectRatioDecorator>(AspectRatioProperty);
        AffectsArrange<AspectRatioDecorator>(AspectRatioProperty);
    }

    public double AspectRatio
    {
        get => GetValue(AspectRatioProperty);
        set => SetValue(AspectRatioProperty, value);
    }

    protected override Size MeasureOverride(Size availableSize)
    {
        if (Child is null)
            return default;

        var ratio = AspectRatio <= 0 ? 1 : AspectRatio;
        var width = availableSize.Width;
        var height = double.IsInfinity(width) ? availableSize.Height : width / ratio;

        if (double.IsInfinity(height))
            height = 0;

        var constrained = new Size(
            double.IsInfinity(width) ? 0 : width,
            height);

        Child.Measure(constrained);
        return Child.DesiredSize;
    }

    protected override Size ArrangeOverride(Size finalSize)
    {
        if (Child is null)
            return finalSize;

        var ratio = AspectRatio <= 0 ? 1 : AspectRatio;
        var width = finalSize.Width;
        var height = width / ratio;

        if (height > finalSize.Height && finalSize.Height > 0)
        {
            height = finalSize.Height;
            width = height * ratio;
        }

        var x = (finalSize.Width - width) * 0.5;
        var y = (finalSize.Height - height) * 0.5;

        Child.Arrange(new Rect(x, y, width, height));
        return finalSize;
    }
}
```

## Building a Custom Panel

For multi-child placement, derive from `Panel`.

```csharp
using Avalonia;
using Avalonia.Controls;

public class UniformRowPanel : Panel
{
    protected override Size MeasureOverride(Size availableSize)
    {
        if (Children.Count == 0)
            return default;

        var childWidth = availableSize.Width / Children.Count;
        var maxHeight = 0d;

        foreach (var child in Children)
        {
            child.Measure(new Size(childWidth, availableSize.Height));
            maxHeight = Math.Max(maxHeight, child.DesiredSize.Height);
        }

        return new Size(availableSize.Width, maxHeight);
    }

    protected override Size ArrangeOverride(Size finalSize)
    {
        if (Children.Count == 0)
            return finalSize;

        var childWidth = finalSize.Width / Children.Count;

        for (var i = 0; i < Children.Count; i++)
        {
            Children[i].Arrange(new Rect(i * childWidth, 0, childWidth, finalSize.Height));
        }

        return finalSize;
    }
}
```

If child attached properties affect panel geometry, use:
- `Panel.AffectsParentMeasure<TPanel>(...)`
- `Panel.AffectsParentArrange<TPanel>(...)`

## Invalidation and Performance Strategy

- Call `InvalidateMeasure()` only when desired size can change.
- Call `InvalidateArrange()` when only position or final placement changes.
- Avoid `UpdateLayout()` in normal UI flow.
- Keep measure/arrange allocation-light in hot paths.
- Do not mutate layout-affecting properties from inside `MeasureOverride`/`ArrangeOverride`.

## XAML-First and Code-Only Usage

Default mode:
- Consume custom controls/panels from XAML first.
- Use code-only tree construction when explicitly requested.

XAML-first usage example:

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            xmlns:local="using:MyApp.Controls"
            Spacing="12">
  <local:AspectRatioDecorator AspectRatio="1.7778" Height="180">
    <Border Background="CornflowerBlue" />
  </local:AspectRatioDecorator>

  <local:UniformRowPanel>
    <Button Content="One" />
    <Button Content="Two" />
    <Button Content="Three" />
  </local:UniformRowPanel>
</StackPanel>
```

Code-only alternative (on request):

```csharp
var row = new UniformRowPanel();
row.Children.Add(new Button { Content = "One" });
row.Children.Add(new Button { Content = "Two" });
row.Children.Add(new Button { Content = "Three" });

var aspect = new AspectRatioDecorator
{
    AspectRatio = 16d / 9d,
    Height = 180,
    Child = new Border { Background = Brushes.CornflowerBlue }
};
```

## Troubleshooting

1. Infinite layout loop:
- `InvalidateMeasure()`/`InvalidateArrange()` called every pass.
- Layout-affecting properties changed during measure/arrange.

2. Zero size control:
- `MeasureOverride` returns `default` even when content exists.
- Child measured with zero or invalid constraints.

3. Child clipped or misplaced:
- Wrong `Arrange` rectangle math.
- Using desired size directly without clamping to `finalSize`.

4. Scroll performance issues:
- Heavy work in layout methods.
- Missing virtualization or overly complex child tree.
