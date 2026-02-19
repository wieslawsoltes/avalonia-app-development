# WinUI Composition Visual Layer, Implicit Animations, and Effects to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- Compositor, SpriteVisual, ImplicitAnimationCollection, ExpressionAnimation

Primary Avalonia APIs:

- Compositor, ElementComposition, CompositionAnimation, Transitions

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| WinUI control and state pipeline | Avalonia control themes, selectors, and transitions |
| WinUI command/input surfaces | Avalonia commands + `KeyBinding`/routed input |
| WinUI resource/theme flow | Avalonia resource dictionaries + `ThemeVariant` |

## Conversion Example

WinUI XAML:

```xaml
var compositor = ElementCompositionPreview.GetElementVisual(this).Compositor;
```

WinUI C#:

```csharp
var sprite = compositor.CreateSpriteVisual();
```

Avalonia XAML:

```xaml
var visual = ElementComposition.GetElementVisual(this);
```

Avalonia C#:

```csharp
var transition = new DoubleTransition { Property = Visual.OpacityProperty, Duration = TimeSpan.FromMilliseconds(200) };
```

## Migration Notes

1. Preserve behavior and interaction contracts before visual refinements.
2. Port hot paths with explicit UI-thread and invalidation discipline.
3. Prefer typed compiled bindings and deterministic state flow in migrated views.
