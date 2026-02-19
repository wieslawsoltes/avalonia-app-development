# WinUI ItemsRepeater Layouts, Virtualization, and ScrollHost to Avalonia Items Controls

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- ItemsRepeater, StackLayout, UniformGridLayout, ItemsRepeaterScrollHost, ElementFactory

Primary Avalonia APIs:

- ItemsControl, ListBox, VirtualizingStackPanel, ItemsPresenter, ScrollViewer

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| WinUI control and state pipeline | Avalonia control themes, selectors, and transitions |
| WinUI command/input surfaces | Avalonia commands + `KeyBinding`/routed input |
| WinUI resource/theme flow | Avalonia resource dictionaries + `ThemeVariant` |

## Conversion Example

WinUI XAML:

```xaml
<muxc:ItemsRepeater ItemsSource="{x:Bind ViewModel.Items}"><muxc:ItemsRepeater.Layout><muxc:StackLayout Spacing="8" /></muxc:ItemsRepeater.Layout></muxc:ItemsRepeater>
```

WinUI C#:

```csharp
var repeater = new ItemsRepeater(); repeater.ItemsSource = ViewModel.Items;
```

Avalonia XAML:

```xaml
<ListBox ItemsSource="{Binding Items}">
  <ListBox.ItemsPanel>
    <ItemsPanelTemplate>
      <VirtualizingStackPanel />
    </ItemsPanelTemplate>
  </ListBox.ItemsPanel>
</ListBox>
```

Avalonia C#:

```csharp
var list = new ListBox { ItemsSource = viewModel.Items };
```

## Migration Notes

1. Preserve behavior and interaction contracts before visual refinements.
2. Port hot paths with explicit UI-thread and invalidation discipline.
3. Prefer typed compiled bindings and deterministic state flow in migrated views.
