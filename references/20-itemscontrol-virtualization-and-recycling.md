# ItemsControl Virtualization and Recycling

## Table of Contents
1. Scope and APIs
2. Virtualization Architecture
3. Authoring Patterns
4. Performance Practices
5. Troubleshooting

## Scope and APIs

Primary APIs:
- `ItemsControl`
- `ItemsPresenter`
- `ItemContainerGenerator`
- `VirtualizingPanel`
- `VirtualizingStackPanel`
- `IRecyclingDataTemplate`
- `FuncDataTemplate`

Important members:
- `ItemsControl.ItemsSource`, `Items`, `ItemsView`
- `ItemsControl.ItemTemplate`, `ItemsPanel`, `ItemContainerTheme`
- `ItemsControl.ItemContainerGenerator`
- `ItemsPresenter.Panel`, `ScrollIntoView(...)`, `ContainerFromIndex(...)`
- `ItemContainerGenerator.NeedsContainer(...)`
- `ItemContainerGenerator.CreateContainer(...)`
- `ItemContainerGenerator.PrepareItemContainer(...)`
- `ItemContainerGenerator.ItemContainerPrepared(...)`
- `ItemContainerGenerator.ClearItemContainer(...)`
- `VirtualizingPanel.ScrollIntoView(...)`, `ContainerFromIndex(...)`, `GetRealizedContainers()`
- `VirtualizingStackPanel.CacheLength`, `FirstRealizedIndex`, `LastRealizedIndex`
- `IRecyclingDataTemplate.Build(data, existing)`
- `FuncDataTemplate(..., supportsRecycling: true)`

Reference source files:
- `src/Avalonia.Controls/ItemsControl.cs`
- `src/Avalonia.Controls/Presenters/ItemsPresenter.cs`
- `src/Avalonia.Controls/Generators/ItemContainerGenerator.cs`
- `src/Avalonia.Controls/VirtualizingPanel.cs`
- `src/Avalonia.Controls/VirtualizingStackPanel.cs`
- `src/Avalonia.Controls/Templates/IRecyclingDataTemplate.cs`
- `src/Avalonia.Controls/Templates/FuncDataTemplate.cs`

## Virtualization Architecture

Default high-level pipeline:
1. `ItemsControl` owns item source and template.
2. `ItemsPresenter` creates panel from `ItemsPanel`.
3. If panel is `VirtualizingPanel`, it realizes only visible range.
4. `ItemContainerGenerator` prepares/clears containers.
5. Recyclable templates reduce container churn.

## Authoring Patterns

### Enable virtualizing panel and prefetch buffer

```xml
<ListBox ItemsSource="{Binding Rows}">
  <ListBox.ItemsPanel>
    <ItemsPanelTemplate>
      <VirtualizingStackPanel Orientation="Vertical" CacheLength="1.0" />
    </ItemsPanelTemplate>
  </ListBox.ItemsPanel>
</ListBox>
```

### Recycling-friendly data template in C#

```csharp
using Avalonia.Controls;
using Avalonia.Controls.Templates;

itemsControl.ItemTemplate = new FuncDataTemplate(
    match: item => item is RowViewModel,
    build: (_, _) => new RowView(),
    supportsRecycling: true);
```

### Programmatic scroll to item

```csharp
itemsControl.Presenter?.ScrollIntoView(index);
```

### Custom virtualizing panel workflow

When deriving `VirtualizingPanel`, use `ItemContainerGenerator` in this order:
1. `NeedsContainer(...)`
2. `CreateContainer(...)` when needed
3. `PrepareItemContainer(...)`
4. Add via `AddInternalChild(...)` or `InsertInternalChild(...)`
5. `ItemContainerPrepared(...)`
6. On unrealize: `ClearItemContainer(...)`

## Performance Practices

- Prefer `VirtualizingStackPanel` for large linear lists.
- Use simple item visuals; defer expensive bindings/converters.
- Enable recycling for stable container types.
- Tune `CacheLength` for your scroll profile.
- Keep container theme and style selectors shallow.
- Avoid forcing full refreshes on high-frequency collection updates.

## Troubleshooting

1. List realizes too many items:
- Non-virtualizing panel selected in `ItemsPanel`.
- Nested layout constraints make viewport effectively infinite.

2. Reuse artifacts (wrong visual state on scrolled items):
- Recycled view state not reset in control/viewmodel.
- Template assumes one-time initialization.

3. `ContainerFromIndex` returns null unexpectedly:
- Item is not currently realized.
- Use `ScrollIntoView(...)` first.

4. Jank on fast scroll:
- Item templates allocate heavily.
- `CacheLength` too small for workload, causing churn.

## XAML-First and Code-Only Usage

Default mode:
- Define virtualized item controls and templates in XAML first.
- Use code-only items/template wiring only when requested.

XAML-first complete example:

```xml
<ListBox xmlns="https://github.com/avaloniaui"
         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
         xmlns:vm="using:MyApp.ViewModels"
         x:DataType="vm:ListPageViewModel"
         ItemsSource="{CompiledBinding Rows}">
  <ListBox.ItemsPanel>
    <ItemsPanelTemplate>
      <VirtualizingStackPanel CacheLength="1.0" />
    </ItemsPanelTemplate>
  </ListBox.ItemsPanel>

  <ListBox.ItemTemplate>
    <DataTemplate x:DataType="vm:RowViewModel">
      <TextBlock Text="{CompiledBinding Title}" />
    </DataTemplate>
  </ListBox.ItemTemplate>
</ListBox>
```

Code-only alternative (on request):

```csharp
using Avalonia.Controls.Templates;

listBox.ItemsSource = viewModel.Rows;
listBox.ItemTemplate = new FuncDataTemplate<RowViewModel>((row, _) =>
    new TextBlock { Text = row.Title },
    supportsRecycling: true);

listBox.Presenter?.ScrollIntoView(0);
```
