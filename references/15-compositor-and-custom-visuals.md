# Compositor and Compositor Animations

## Table of Contents
1. Scope and APIs
2. Composition Tree Access
3. Compositor Object Creation
4. Compositor Animations
5. Custom Composition Visual Rendering
6. Frame-Driven Composition Updates
7. Best Practices
8. Troubleshooting

## Scope and APIs

Primary APIs:
- `ElementComposition.GetElementVisual(...)`
- `ElementComposition.SetElementChildVisual(...)`
- `Compositor`
- `CompositionObject.StartAnimation(...)`
- `CompositionObject.StopAnimation(...)`
- `CompositionAnimationGroup`
- `ImplicitAnimationCollection`
- `CompositionCustomVisual`
- `CompositionCustomVisualHandler`
- `Compositor.RequestCompositionUpdate(...)`
- `Compositor.RequestCommitAsync()`

Reference source files:
- `src/Avalonia.Base/Rendering/Composition/ElementCompositionPreview.cs`
- `src/Avalonia.Base/Rendering/Composition/Compositor.cs`
- `src/Avalonia.Base/Rendering/Composition/Compositor.Factories.cs`
- `src/Avalonia.Base/Rendering/Composition/CompositionObject.cs`
- `src/Avalonia.Base/Rendering/Composition/CompositionCustomVisualHandler.cs`
- `samples/ControlCatalog/Pages/CompositionPage.axaml.cs`
- `samples/ControlCatalog/Pages/OpenGl/OpenGlLeasePage.xaml.cs`

## Composition Tree Access

Get the composition visual backing a normal Avalonia visual:

```csharp
var compositionVisual = ElementComposition.GetElementVisual(myControl);
```

Attach a custom child composition visual:

```csharp
var compositor = ElementComposition.GetElementVisual(myControl)!.Compositor;
var child = compositor.CreateSolidColorVisual();
ElementComposition.SetElementChildVisual(myControl, child);
```

Important constraint:
- Child and host must belong to the same `Compositor` instance.

## Compositor Object Creation

Common factories on `Compositor`:
- `CreateContainerVisual()`
- `CreateSolidColorVisual()`
- `CreateSurfaceVisual()`
- `CreateCustomVisual(handler)`
- `CreateExpressionAnimation(...)`
- `CreateAnimationGroup()`
- `CreateImplicitAnimationCollection()`
- Keyframe animation factories (scalar, vector, color)

## Compositor Animations

Core pattern:
1. Create animation object.
2. Set `Target` to property name.
3. Insert keyframes.
4. Set duration/iteration settings.
5. Start animation with `StartAnimation`.

```csharp
var visual = compositor.CreateSolidColorVisual();
var color = compositor.CreateColorKeyFrameAnimation();
color.Target = "Color";
color.InsertKeyFrame(0f, Colors.Red);
color.InsertKeyFrame(1f, Colors.Blue);
color.Duration = TimeSpan.FromSeconds(1);
color.IterationBehavior = AnimationIterationBehavior.Forever;
visual.StartAnimation("Color", color);
```

Use implicit animations for automatic transitions on property change:

```csharp
var implicitAnimations = compositor.CreateImplicitAnimationCollection();
implicitAnimations["Offset"] = compositor.CreateAnimationGroup();
compositionVisual.ImplicitAnimations = implicitAnimations;
```

## Custom Composition Visual Rendering

Use `CompositionCustomVisualHandler` for custom render-thread visual logic.

Key overridable methods:
- `OnRender(ImmediateDrawingContext drawingContext)`
- `OnMessage(object message)`
- `OnAnimationFrameUpdate()`

Useful protected methods:
- `Invalidate()` / `Invalidate(Rect)`
- `RegisterForNextAnimationFrameUpdate()`
- `GetRenderBounds()`
- `RenderClipContains(...)`
- `RenderClipIntersectes(...)`

The sample in `CompositionPage` and `OpenGlLeasePage` demonstrates this pattern.

## Frame-Driven Composition Updates

Two major mechanisms:
- `RegisterForNextAnimationFrameUpdate()` inside custom visual handler
- `Compositor.RequestCompositionUpdate(Action)` for UI-thread pre-commit updates

Use `Compositor.RequestCommitAsync()` when you need explicit commit lifecycle control.

## Best Practices

- Prefer composition for high-frequency effects over heavy UI-thread property churn.
- Keep custom visual message payloads small and explicit.
- Dispose/detach composition visuals when host visual detaches.
- Avoid cross-compositor object sharing.

## Troubleshooting

1. Exception about different compositor instances:
- You attached a composition visual created by another root/compositor.

2. Animation does not run:
- Wrong `Target` string or property unsupported for that object type.

3. Custom handler `OnRender` not called:
- No invalidation and no animation-frame registration.
- Visual not attached via `SetElementChildVisual`.

4. Leaks after navigation:
- Custom visual remains attached; clear with `SetElementChildVisual(host, null)` on detach.

## XAML-First and Code-Only Usage

Default mode:
- Define host visuals in XAML first.
- Attach compositor visuals from code only for effects/animation paths or when requested.

XAML-first references:
- Host control declarations in `.axaml`
- Class/name hooks for composition attachment points

XAML-first usage example:

```xml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             x:Class="MyApp.Views.CompositionView">
  <Border x:Name="CompositionHost"
          Width="320"
          Height="180"
          Background="#1E1E1E" />
</UserControl>
```

Code-only alternative (on request):

```csharp
var host = this.FindControl<Border>("CompositionHost")!;
var visual = ElementComposition.GetElementVisual(host)!;
var compositor = visual.Compositor;
var child = compositor.CreateSolidColorVisual();
ElementComposition.SetElementChildVisual(host, child);
```
