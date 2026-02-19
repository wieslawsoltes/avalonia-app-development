# WinUI ListView/GridView Selection and ItemContainer Patterns to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- ListView, GridView, SelectionMode, IsItemClickEnabled, ContainerStyle

Primary Avalonia APIs:

- ListBox, SelectingItemsControl, SelectionMode, ItemTemplate, styles

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| WinUI control and state pipeline | Avalonia control themes, selectors, and transitions |
| WinUI command/input surfaces | Avalonia commands + `KeyBinding`/routed input |
| WinUI resource/theme flow | Avalonia resource dictionaries + `ThemeVariant` |

## Conversion Example

WinUI XAML:

```xaml
<ListView ItemsSource="{x:Bind ViewModel.Items}" SelectionMode="Multiple" IsItemClickEnabled="True" />
```

WinUI C#:

```csharp
listView.SelectionChanged += OnSelectionChanged;
```

Avalonia XAML:

```xaml
<ListBox ItemsSource="{Binding Items}" SelectionMode="Multiple" />
```

Avalonia C#:

```csharp
listBox.SelectionChanged += OnSelectionChanged;
```

## Migration Notes

1. Preserve behavior and interaction contracts before visual refinements.
2. Port hot paths with explicit UI-thread and invalidation discipline.
3. Prefer typed compiled bindings and deterministic state flow in migrated views.
