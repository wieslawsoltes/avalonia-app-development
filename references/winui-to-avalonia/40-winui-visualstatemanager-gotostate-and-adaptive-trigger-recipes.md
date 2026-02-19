# WinUI VisualStateManager GoToState and AdaptiveTrigger Recipes to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- VisualStateManager, VisualStateGroup, VisualState, AdaptiveTrigger, GoToState

Primary Avalonia APIs:

- Style selectors, classes, pseudo-classes, transitions, bindings

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| WinUI control and state pipeline | Avalonia control themes, selectors, and transitions |
| WinUI command/input surfaces | Avalonia commands + `KeyBinding`/routed input |
| WinUI resource/theme flow | Avalonia resource dictionaries + `ThemeVariant` |

## Conversion Example

WinUI XAML:

```xaml
<VisualStateManager.VisualStateGroups><VisualStateGroup><VisualState x:Name="Narrow" /><VisualState x:Name="Wide" /></VisualStateGroup></VisualStateManager.VisualStateGroups>
```

WinUI C#:

```csharp
VisualStateManager.GoToState(this, "Wide", true);
```

Avalonia XAML:

```xaml
<Style Selector="Grid.narrow"><Setter Property="ColumnDefinitions" Value="*" /></Style><Style Selector="Grid.wide"><Setter Property="ColumnDefinitions" Value="240,*" /></Style>
```

Avalonia C#:

```csharp
root.Classes.Set("wide", viewModel.IsWide);
```

## Migration Notes

1. Preserve behavior and interaction contracts before visual refinements.
2. Port hot paths with explicit UI-thread and invalidation discipline.
3. Prefer typed compiled bindings and deterministic state flow in migrated views.
