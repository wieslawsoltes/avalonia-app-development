# WinUI ScrollViewer/Scroller Anchoring and BringIntoView to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- ScrollViewer, Scroller, ChangeView, ScrollIntoView, BringIntoView

Primary Avalonia APIs:

- ScrollViewer.Offset, ScrollViewer.ScrollChanged, BringIntoView(), snap points

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| WinUI control and state pipeline | Avalonia control themes, selectors, and transitions |
| WinUI command/input surfaces | Avalonia commands + `KeyBinding`/routed input |
| WinUI resource/theme flow | Avalonia resource dictionaries + `ThemeVariant` |

## Conversion Example

WinUI XAML:

```xaml
<ScrollViewer x:Name="Host"><ListView x:Name="ItemsList" /></ScrollViewer>
```

WinUI C#:

```csharp
Host.ChangeView(null, 240, null);
```

Avalonia XAML:

```xaml
<ScrollViewer x:Name="Host"><ListBox x:Name="ItemsList" /></ScrollViewer>
```

Avalonia C#:

```csharp
ItemsList.BringIntoView();
```

## Migration Notes

1. Preserve behavior and interaction contracts before visual refinements.
2. Port hot paths with explicit UI-thread and invalidation discipline.
3. Prefer typed compiled bindings and deterministic state flow in migrated views.
