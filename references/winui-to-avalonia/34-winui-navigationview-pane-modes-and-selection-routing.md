# WinUI NavigationView Pane Modes and Selection Routing to Avalonia Shell Patterns

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- NavigationView, NavigationViewItem, PaneDisplayMode, SelectionChanged, ItemInvoked

Primary Avalonia APIs:

- SplitView, ListBox, TreeView, SelectionModel, commands

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| WinUI control and state pipeline | Avalonia control themes, selectors, and transitions |
| WinUI command/input surfaces | Avalonia commands + `KeyBinding`/routed input |
| WinUI resource/theme flow | Avalonia resource dictionaries + `ThemeVariant` |

## Conversion Example

WinUI XAML:

```xaml
<NavigationView PaneDisplayMode="LeftCompact"><NavigationView.MenuItems><NavigationViewItem Content="Home" Tag="home" /></NavigationView.MenuItems><Frame x:Name="RootFrame" /></NavigationView>
```

WinUI C#:

```csharp
var nav = new NavigationView(); nav.SelectionChanged += OnSelectionChanged;
```

Avalonia XAML:

```xaml
<SplitView DisplayMode="CompactInline" IsPaneOpen="{Binding IsPaneOpen}"><SplitView.Pane><ListBox ItemsSource="{Binding NavItems}" SelectedItem="{Binding SelectedNavItem, Mode=TwoWay}" /></SplitView.Pane><ContentControl Content="{Binding CurrentView}" /></SplitView>
```

Avalonia C#:

```csharp
var shell = new SplitView { IsPaneOpen = viewModel.IsPaneOpen };
```

## Migration Notes

1. Preserve behavior and interaction contracts before visual refinements.
2. Port hot paths with explicit UI-thread and invalidation discipline.
3. Prefer typed compiled bindings and deterministic state flow in migrated views.
