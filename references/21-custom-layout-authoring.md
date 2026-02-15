# Custom Layout Authoring

## Table of Contents
1. Scope and APIs
2. Layout Lifecycle
3. Authoring Patterns
4. Invalidation Strategy
5. Troubleshooting

## Scope and APIs

Primary APIs:
- `Layoutable`
- `Panel`
- `ILayoutManager`
- `LayoutManager`
- `EffectiveViewportChangedEventArgs`

Important members:
- `Layoutable.Measure(...)`, `Arrange(...)`
- `Layoutable.MeasureOverride(...)`, `ArrangeOverride(...)`
- `Layoutable.InvalidateMeasure()`, `InvalidateArrange()`, `UpdateLayout()`
- `Layoutable.EffectiveViewportChanged`, `LayoutUpdated`
- `Layoutable.AffectsMeasure<T>(...)`, `AffectsArrange<T>(...)`
- `Panel.Children`
- `Panel.AffectsParentMeasure<TPanel>(...)`, `AffectsParentArrange<TPanel>(...)`
- `ILayoutManager.InvalidateMeasure(...)`, `InvalidateArrange(...)`, `ExecuteLayoutPass()`

Reference source files:
- `src/Avalonia.Base/Layout/Layoutable.cs`
- `src/Avalonia.Controls/Panel.cs`
- `src/Avalonia.Base/Layout/ILayoutManager.cs`
- `src/Avalonia.Base/Layout/LayoutManager.cs`
- `src/Avalonia.Base/Layout/EffectiveViewportChangedEventArgs.cs`

## Layout Lifecycle

`Layoutable` lifecycle for custom controls/panels:
1. Measure pass computes `DesiredSize` (`MeasureOverride`).
2. Arrange pass finalizes geometry (`ArrangeOverride`).
3. Invalidation queues next pass (`InvalidateMeasure`/`InvalidateArrange`).
4. Viewport-driven controls can react to `EffectiveViewportChanged`.

## Authoring Patterns

### Minimal custom panel

```csharp
using Avalonia;
using Avalonia.Controls;

public class EqualColumnsPanel : Panel
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

### Mark properties that affect layout

```csharp
public class StripePanel : Panel
{
    public static readonly StyledProperty<double> StripeWidthProperty =
        AvaloniaProperty.Register<StripePanel, double>(nameof(StripeWidth), 24);

    static StripePanel()
    {
        AffectsMeasure<StripePanel>(StripeWidthProperty);
        AffectsArrange<StripePanel>(StripeWidthProperty);
    }

    public double StripeWidth
    {
        get => GetValue(StripeWidthProperty);
        set => SetValue(StripeWidthProperty, value);
    }
}
```

### Child-attached properties affecting parent layout

Use `Panel.AffectsParentMeasure<TPanel>(...)` and `AffectsParentArrange<TPanel>(...)` when child properties influence parent arrangement logic.

## Invalidation Strategy

- Invalidate measure only when desired size can change.
- Invalidate arrange when only placement/offset changes.
- Avoid direct `UpdateLayout()` in normal control flow.
- For viewport-driven realization, subscribe to `EffectiveViewportChanged`.
- Keep measure/arrange allocation-free in hot paths.

## Troubleshooting

1. Infinite or repeated layout passes:
- Changing layout-affecting properties inside `MeasureOverride`/`ArrangeOverride`.
- Calling `InvalidateMeasure()` every frame without guard conditions.

2. Child controls not visible:
- Measured with zero/invalid size.
- Not arranged within final bounds.

3. Wrong desired size:
- Returning unconstrained or NaN sizes.
- Ignoring child desired sizes where required.

4. Jank under scroll:
- Heavy work in measure/arrange.
- Missing viewport-aware behavior for large child sets.

## XAML-First and Code-Only Usage

Default mode:
- Consume custom panels from XAML first.
- Write full code-only layout trees only when requested.

XAML-first references:
- Custom panel declaration and child layout in `.axaml`

XAML-first usage example:

```xml
<local:EqualColumnsPanel xmlns="https://github.com/avaloniaui"
                         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                         xmlns:local="using:MyApp.Controls">
  <Button Content="A" />
  <Button Content="B" />
  <Button Content="C" />
</local:EqualColumnsPanel>
```

Code-only alternative (on request):

```csharp
var panel = new EqualColumnsPanel();
panel.Children.Add(new Button { Content = "A" });
panel.Children.Add(new Button { Content = "B" });
panel.Children.Add(new Button { Content = "C" });
```
