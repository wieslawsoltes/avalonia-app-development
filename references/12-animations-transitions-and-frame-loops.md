# Animations, Transitions, and Frame Loops

## Table of Contents
1. Scope and APIs
2. Property Transitions
3. Keyframe Animations
4. Page Transitions
5. Frame-Scheduled Updates
6. Best Practices
7. Troubleshooting

## Scope and APIs

Primary APIs:
- `Animatable.Transitions`
- `Transitions`
- `ITransition` and built-in transition types
- `Animation`, `KeyFrame`, `Cue`, `RunAsync`
- `IPageTransition`, `CrossFade`, `PageSlide`
- `TopLevel.RequestAnimationFrame(Action<TimeSpan>)`
- `MediaContext.BeginInvokeOnRender(Action)`

Reference source files:
- `src/Avalonia.Base/Animation/Animatable.cs`
- `src/Avalonia.Base/Animation/Animation.cs`
- `src/Avalonia.Base/Animation/CrossFade.cs`
- `src/Avalonia.Base/Animation/PageSlide.cs`
- `src/Avalonia.Controls/TopLevel.cs`
- `src/Avalonia.Base/Media/MediaContext.cs`

## Property Transitions

Use transitions for implicit animation when a property value changes.

Common transition types:
- `DoubleTransition`
- `ColorTransition`
- `ThicknessTransition`
- `TransformOperationsTransition`

Example:

```xml
<Button>
  <Button.Transitions>
    <Transitions>
      <TransformOperationsTransition Property="RenderTransform" Duration="0:0:0.1" />
    </Transitions>
  </Button.Transitions>
</Button>
```

## Keyframe Animations

Use `Animation` when you need explicit timeline control.

```csharp
var animation = new Animation
{
    Duration = TimeSpan.FromMilliseconds(220),
    Easing = new Avalonia.Animation.Easings.CubicEaseOut(),
    Children =
    {
        new KeyFrame
        {
            Cue = new Cue(0d),
            Setters = { new Setter(Visual.OpacityProperty, 0d) }
        },
        new KeyFrame
        {
            Cue = new Cue(1d),
            Setters = { new Setter(Visual.OpacityProperty, 1d) }
        }
    }
};

await animation.RunAsync(myControl);
```

Useful knobs:
- `Duration`
- `IterationCount`
- `PlaybackDirection`
- `FillMode`
- `Delay`
- `DelayBetweenIterations`
- `SpeedRatio`

## Page Transitions

Use `IPageTransition` for view switching.

Built-ins:
- `CrossFade`
- `PageSlide`
- `CompositePageTransition`

`PageSlide` expects source and destination visuals to share parent (see implementation constraints).

## Frame-Scheduled Updates

For request-frame animation loops in app code:
- Use `TopLevel.RequestAnimationFrame` to schedule per-frame callbacks.
- Use `MediaContext.BeginInvokeOnRender` for render-loop callback injection (infrastructure-level API).

Pattern:

```csharp
void Start(TopLevel top)
{
    void Tick(TimeSpan now)
    {
        UpdateSimulation(now);
        InvalidateVisual();
        top.RequestAnimationFrame(Tick);
    }

    top.RequestAnimationFrame(Tick);
}
```

Keep loops stoppable (window detach, view disposed, cancellation token).

## Best Practices

- Use transitions for simple property changes; use keyframes for choreographed sequences.
- Keep animation work lightweight; avoid heavy allocations inside per-frame callbacks.
- Keep render-thread and UI-thread responsibilities clear.
- Prefer composition APIs (`ElementComposition`) for advanced/high-frequency effects.

## Troubleshooting

1. Transition does not run:
- Property may be direct/read-only or not animatable by registered animator.
- Control may not be attached (transitions are managed by visual-tree attachment state).

2. Animation throws about missing animator:
- The setter property type has no animator; use supported property or custom animator.

3. Page transition glitches:
- For `PageSlide`, ensure both visuals share the same parent.

4. Frame loop causes CPU spikes:
- You are scheduling continuously without throttling or without visibility checks.
- Stop loop when control is detached or hidden.

## XAML-First and Code-Only Usage

Default mode:
- Declare transitions in XAML first.
- Use code-only animation setup when requested.

XAML-first complete example:

```xml
<Button xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        x:Name="PulseButton"
        Content="Animate"
        Opacity="0.7">
  <Button.Transitions>
    <Transitions>
      <DoubleTransition Property="Opacity" Duration="0:0:0.2" />
    </Transitions>
  </Button.Transitions>
</Button>
```

Code-only alternative (on request):

```csharp
using Avalonia;
using Avalonia.Animation;
using Avalonia.Animation.Easings;
using Avalonia.Styling;

var fade = new Animation
{
    Duration = TimeSpan.FromMilliseconds(200),
    Easing = new CubicEaseOut(),
    Children =
    {
        new KeyFrame { Cue = new Cue(0d), Setters = { new Setter(Visual.OpacityProperty, 0.7d) } },
        new KeyFrame { Cue = new Cue(1d), Setters = { new Setter(Visual.OpacityProperty, 1.0d) } }
    }
};

await fade.RunAsync(pulseButton);
```
