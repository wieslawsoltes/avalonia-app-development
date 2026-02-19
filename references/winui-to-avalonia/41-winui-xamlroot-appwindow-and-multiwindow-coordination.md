# WinUI XamlRoot, AppWindow, and Multi-Window Coordination to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- XamlRoot, AppWindow, WindowId, DisplayArea, multi-window APIs

Primary Avalonia APIs:

- TopLevel, Window, Screens, IClassicDesktopStyleApplicationLifetime

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| WinUI control and state pipeline | Avalonia control themes, selectors, and transitions |
| WinUI command/input surfaces | Avalonia commands + `KeyBinding`/routed input |
| WinUI resource/theme flow | Avalonia resource dictionaries + `ThemeVariant` |

## Conversion Example

WinUI XAML:

```xaml
var root = this.XamlRoot;
```

WinUI C#:

```csharp
var appWindow = AppWindow.GetFromWindowId(id);
```

Avalonia XAML:

```xaml
var top = TopLevel.GetTopLevel(this);
```

Avalonia C#:

```csharp
var desktop = (IClassicDesktopStyleApplicationLifetime)Application.Current!.ApplicationLifetime!;
```

## Migration Notes

1. Preserve behavior and interaction contracts before visual refinements.
2. Port hot paths with explicit UI-thread and invalidation discipline.
3. Prefer typed compiled bindings and deterministic state flow in migrated views.
