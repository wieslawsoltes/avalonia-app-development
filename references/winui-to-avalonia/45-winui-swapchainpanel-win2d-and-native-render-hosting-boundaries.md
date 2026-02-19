# WinUI SwapChainPanel, Win2D, and Native Render Hosting Boundaries to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- SwapChainPanel, CanvasControl (Win2D), CompositionGraphicsDevice interop

Primary Avalonia APIs:

- NativeControlHost, custom rendering (`Render`), composition custom visuals

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| WinUI control and state pipeline | Avalonia control themes, selectors, and transitions |
| WinUI command/input surfaces | Avalonia commands + `KeyBinding`/routed input |
| WinUI resource/theme flow | Avalonia resource dictionaries + `ThemeVariant` |

## Conversion Example

WinUI XAML:

```xaml
<SwapChainPanel x:Name="SwapHost" />
```

WinUI C#:

```csharp
var swap = new SwapChainPanel();
```

Avalonia XAML:

```xaml
<local:NativeRenderHost />
```

Avalonia C#:

```csharp
var host = new NativeControlHost();
```

## Migration Notes

1. Preserve behavior and interaction contracts before visual refinements.
2. Port hot paths with explicit UI-thread and invalidation discipline.
3. Prefer typed compiled bindings and deterministic state flow in migrated views.
