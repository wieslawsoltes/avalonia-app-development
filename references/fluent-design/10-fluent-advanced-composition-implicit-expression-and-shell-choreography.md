# Fluent Advanced Composition, Implicit Animations, and Shell Choreography

## Table of Contents
1. Scope and Primary APIs
2. Fluent Shell-Choreography Rules
3. Implicit Animation Recipe
4. Expression and Animation-Group Recipe
5. AOT and Runtime Notes
6. Do and Don't Guidance
7. Troubleshooting
8. Official Resources

## Scope and Primary APIs

Use this reference when Fluent shell polish needs deeper composition control than simple transitions.

Primary APIs:
- `ElementComposition`, `Compositor`
- `ImplicitAnimationCollection`
- `CompositionAnimationGroup`
- `CompositionPropertySet`
- `ExpressionAnimation`
- `CompositionObject.StartAnimationGroup(...)`
- `Compositor.CreateColorKeyFrameAnimation()`, `CreateVector3KeyFrameAnimation()`, `CreateScalarKeyFrameAnimation()`
- `ExpressionAnimation.SetScalarParameter(...)`

## Fluent Shell-Choreography Rules

Advanced Fluent motion should:
- reinforce shell hierarchy,
- stay calm under repetition,
- help orientation during navigation,
- coordinate depth, motion, and content priority together.

Use deeper composition choreography for:
- workspace reveal or collapse,
- elevated command surfaces,
- onboarding and teaching moments,
- shell-level transitions that should stay smooth under heavier load.

## Implicit Animation Recipe

```csharp
using System;
using Avalonia.Rendering.Composition;

var visual = ElementComposition.GetElementVisual(ShellPane)!;
var compositor = visual.Compositor;

var offsetAnimation = compositor.CreateVector3KeyFrameAnimation();
offsetAnimation.Target = "Offset";
offsetAnimation.InsertExpressionKeyFrame(1f, "this.FinalValue");
offsetAnimation.Duration = TimeSpan.FromMilliseconds(180);

var implicitAnimations = compositor.CreateImplicitAnimationCollection();
implicitAnimations["Offset"] = offsetAnimation;

visual.ImplicitAnimations = implicitAnimations;
```

Use this for:
- shell rails that expand or collapse,
- command panes that slide,
- surfaces that reflow in response to layout changes.

## Expression and Animation-Group Recipe

```csharp
using System;
using System.Numerics;
using Avalonia.Rendering.Composition;

var visual = ElementComposition.GetElementVisual(CommandSurface)!;
var compositor = visual.Compositor;

var scale = compositor.CreateVector3KeyFrameAnimation();
scale.Target = "Scale";
scale.InsertKeyFrame(0f, new Vector3(0.985f, 0.985f, 1f));
scale.InsertKeyFrame(1f, new Vector3(1f, 1f, 1f));
scale.Duration = TimeSpan.FromMilliseconds(160);

var slide = compositor.CreateVector3KeyFrameAnimation();
slide.Target = "Offset";
slide.InsertKeyFrame(0f, new Vector3(0f, 6f, 0f));
slide.InsertKeyFrame(1f, new Vector3(0f, 0f, 0f));
slide.Duration = TimeSpan.FromMilliseconds(160);

var group = compositor.CreateAnimationGroup();
group.Add(scale);
group.Add(slide);

visual.StartAnimationGroup(group);

var emphasis = compositor.CreateExpressionAnimation("baseOpacity * emphasis");
emphasis.Target = "Opacity";
emphasis.SetScalarParameter("baseOpacity", 1f);
emphasis.SetScalarParameter("emphasis", 0.98f);
visual.StartAnimation("Opacity", emphasis);
```

`CompositionPropertySet` exists in Avalonia `11.3.12`, but app code typically drives shared composition input through animation parameters because there is no public compositor factory for constructing property sets directly.

## AOT and Runtime Notes

- Keep most Fluent motion in compiled XAML and reserve advanced composition for shell hotspots.
- Reuse one motion grammar across transitions and composition animations so the shell stays coherent.
- Prefer animation parameter APIs over direct `CompositionPropertySet` construction in app code on Avalonia `11.3.12`.
- Clean up attached visuals and long-running animations during view detach or navigation.

## Do and Don't Guidance

Do:
- use composition to support orientation and hierarchy,
- coordinate scale, opacity, and color only when they reinforce the same meaning,
- keep advanced motion rare enough to stay special.

Do not:
- apply shell choreography to every small interaction,
- use advanced composition to compensate for unclear layout or weak IA,
- let motion, shadow, acrylic, and accent all compete on the same surface.

## Troubleshooting

1. Shell polish feels too busy.
- Reduce the number of simultaneously animated properties and simplify the hierarchy story.

2. Advanced composition looks disconnected from normal transitions.
- Reuse the same timing and easing grammar between XAML and composition paths.

3. Elevated surfaces still feel muddy.
- Reduce transparency and color emphasis before increasing motion.

## Official Resources

- Avalonia `Compositor` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Compositor](https://api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Compositor)
- Avalonia `CompositionPropertySet` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_CompositionPropertySet](https://api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_CompositionPropertySet)
- Avalonia `CompositionAnimationGroup` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Animations_CompositionAnimationGroup](https://api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Animations_CompositionAnimationGroup)
- Avalonia `StartAnimationGroup` API: [api-docs.avaloniaui.net/docs/M_Avalonia_Rendering_Composition_CompositionObject_StartAnimationGroup](https://api-docs.avaloniaui.net/docs/M_Avalonia_Rendering_Composition_CompositionObject_StartAnimationGroup)
- Avalonia `CreateColorKeyFrameAnimation` API: [api-docs.avaloniaui.net/docs/M_Avalonia_Rendering_Composition_Compositor_CreateColorKeyFrameAnimation](https://api-docs.avaloniaui.net/docs/M_Avalonia_Rendering_Composition_Compositor_CreateColorKeyFrameAnimation)
- Avalonia `SetScalarParameter` API: [api-docs.avaloniaui.net/docs/M_Avalonia_Rendering_Composition_Animations_ExpressionAnimation_SetScalarParameter](https://api-docs.avaloniaui.net/docs/M_Avalonia_Rendering_Composition_Animations_ExpressionAnimation_SetScalarParameter)
- Fluent 2 motion: [fluent2.microsoft.design/motion](https://fluent2.microsoft.design/motion)
- Fluent 2 dialog guidance: [fluent2.microsoft.design/components/web/react/core/dialog/usage](https://fluent2.microsoft.design/components/web/react/core/dialog/usage)
