# Fluent Motion, Composition, and Depth Recipes in Avalonia

## Table of Contents
1. Scope and Primary APIs
2. Fluent Motion Rules
3. Fluent Transition Recipes
4. Fluent Composition Recipe
5. Depth, Materials, and Motion
6. AOT and Runtime Notes
7. Do and Don't Guidance
8. Troubleshooting
9. Official Resources

## Scope and Primary APIs

Use this reference to turn Fluent motion guidance into concrete Avalonia motion and composition patterns.

Primary APIs:
- `Transitions`, `TransformOperationsTransition`, `DoubleTransition`, `BoxShadowsTransition`
- `TransitioningContentControl`
- `CrossFade`, `PageSlide`, `CompositePageTransition`
- `ElementComposition`, `Compositor`
- `ExpressionAnimation`, `ImplicitAnimationCollection`
- `Compositor.CreateVector3KeyFrameAnimation()`, `Compositor.CreateScalarKeyFrameAnimation()`
- `ExperimentalAcrylicBorder`

## Fluent Motion Rules

Fluent motion should be:
- calm rather than flashy,
- connected rather than abrupt,
- informative rather than decorative,
- depth-aware rather than flat or random.

Use motion to:
- connect navigation states,
- clarify hierarchy,
- confirm intent,
- support teaching and onboarding,
- improve perceived performance during loading.

Use less motion when:
- the screen is data-dense,
- repeated updates would become distracting,
- the motion does not teach anything new.

## Fluent Transition Recipes

```xml
<Border xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Classes="fluent-command-card"
        Opacity="0.96"
        RenderTransform="translateY(0px)">
  <Border.Transitions>
    <Transitions>
      <TransformOperationsTransition Property="RenderTransform" Duration="0:0:0.16" />
      <DoubleTransition Property="Opacity" Duration="0:0:0.16" />
      <BoxShadowsTransition Property="BoxShadow" Duration="0:0:0.16" />
    </Transitions>
  </Border.Transitions>
</Border>
```

```xml
<CompositePageTransition xmlns="https://github.com/avaloniaui"
                         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                         x:Key="FluentShellTransition">
  <CompositePageTransition.PageTransitions>
    <CrossFade Duration="0:0:0.18" />
    <PageSlide Duration="0:0:0.18" Orientation="Horizontal" />
  </CompositePageTransition.PageTransitions>
</CompositePageTransition>

<TransitioningContentControl PageTransition="{StaticResource FluentShellTransition}"
                             Content="{CompiledBinding CurrentView}" />
```

Guidance:
- use shorter durations for command confirmation,
- use page transitions to connect views, not to decorate every content refresh,
- make focus and hover feedback immediate and readable.

## Fluent Composition Recipe

```csharp
using System;
using System.Numerics;
using Avalonia.Rendering.Composition;

var visual = ElementComposition.GetElementVisual(CommandSurface)!;
var compositor = visual.Compositor;

var scale = compositor.CreateVector3KeyFrameAnimation();
scale.InsertKeyFrame(0f, new Vector3(0.98f, 0.98f, 1f));
scale.InsertKeyFrame(1f, new Vector3(1f, 1f, 1f));
scale.Duration = TimeSpan.FromMilliseconds(160);

var fade = compositor.CreateScalarKeyFrameAnimation();
fade.InsertKeyFrame(0f, 0.9f);
fade.InsertKeyFrame(1f, 1f);
fade.Duration = TimeSpan.FromMilliseconds(160);

visual.StartAnimation("Scale", scale);
visual.StartAnimation("Opacity", fade);

var center = compositor.CreateExpressionAnimation(
    "Vector3(this.Target.Size.X * 0.5, this.Target.Size.Y * 0.5, 1)");
visual.StartAnimation("CenterPoint", center);
```

Use composition for:
- shell reveal and hide choreography,
- elevated command surfaces,
- teaching cards,
- custom visual effects,
- motion that should stay smooth under heavier UI load.

## Depth, Materials, and Motion

Depth rules:
- if a surface feels elevated, its motion should support that hierarchy,
- acrylic or translucent surfaces should move less than content-heavy panes,
- shadow, border, and motion should agree on which layer is in front.

Practical guidance:
- keep most dense content surfaces opaque,
- reserve acrylic and stronger motion for shell accents and transient surfaces,
- avoid stacking motion, blur, and high-contrast accent color on the same element unless the state is rare and important.

## AOT and Runtime Notes

- Keep normal Fluent transitions in compiled XAML.
- Use composition from code only where the extra smoothness or flexibility matters.
- Remove attached child visuals or stop animations when a view is detached.

## Do and Don't Guidance

Do:
- keep Fluent motion short and purposeful,
- align motion with depth and content priority,
- use composition for shell-level polish, not for every control.

Do not:
- animate every card, row, or command surface,
- mix multiple motion languages in one shell,
- let acrylic, shadow, and motion all compete for attention.

## Troubleshooting

1. Fluent motion feels too loud.
- Reduce translation distance, accent emphasis, and shadow depth together.

2. Composition-driven shell polish looks disconnected.
- Reuse the same duration and easing grammar as your XAML transitions.

3. Elevated surfaces feel muddy in dark theme.
- Lower transparency and motion strength before increasing shadow.

## Official Resources

- Avalonia transitions: [docs.avaloniaui.net/docs/guides/graphics-and-animation/transitions](https://docs.avaloniaui.net/docs/guides/graphics-and-animation/transitions)
- Avalonia `TransitioningContentControl` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Controls_TransitioningContentControl](https://api-docs.avaloniaui.net/docs/T_Avalonia_Controls_TransitioningContentControl)
- Avalonia `CompositePageTransition` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Animation_CompositePageTransition](https://api-docs.avaloniaui.net/docs/T_Avalonia_Animation_CompositePageTransition)
- Avalonia `Compositor` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Compositor](https://api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Compositor)
- Avalonia `ElementComposition` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_ElementComposition](https://api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_ElementComposition)
- Avalonia `ExpressionAnimation` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Animations_ExpressionAnimation](https://api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Animations_ExpressionAnimation)
- Avalonia `CreateVector3KeyFrameAnimation` API: [api-docs.avaloniaui.net/docs/M_Avalonia_Rendering_Composition_Compositor_CreateVector3KeyFrameAnimation](https://api-docs.avaloniaui.net/docs/M_Avalonia_Rendering_Composition_Compositor_CreateVector3KeyFrameAnimation)
- Avalonia `CreateScalarKeyFrameAnimation` API: [api-docs.avaloniaui.net/docs/M_Avalonia_Rendering_Composition_Compositor_CreateScalarKeyFrameAnimation](https://api-docs.avaloniaui.net/docs/M_Avalonia_Rendering_Composition_Compositor_CreateScalarKeyFrameAnimation)
- Fluent 2 motion: [fluent2.microsoft.design/motion](https://fluent2.microsoft.design/motion)
- Fluent 2 wait UX: [fluent2.microsoft.design/wait-ux](https://fluent2.microsoft.design/wait-ux)
