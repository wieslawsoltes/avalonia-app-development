# WinUI ItemsView/LayoutPanel and Virtualization Strategies to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- ItemsView, LayoutPanel, item container state, virtualization-oriented layouts

Primary Avalonia APIs:

- ItemsControl/ListBox, ItemsPanelTemplate, VirtualizingStackPanel, data templates, custom panel composition

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| ItemsView generalized items surface | ItemsControl/ListBox based surface |
| LayoutPanel layout strategies | ItemsPanelTemplate + custom panels |
| virtualized items realization | VirtualizingStackPanel with recycling-friendly templates |
| item container states | item container styles/selectors |

## Conversion Example

WinUI XAML:

```xaml
<muxc:ItemsView ItemsSource="{x:Bind ViewModel.Items}">
  <muxc:ItemsView.Layout>
    <muxc:StackLayout Spacing="8" />
  </muxc:ItemsView.Layout>
</muxc:ItemsView>
```

WinUI C#:

```csharp
var itemsView = new ItemsView
{
    ItemsSource = ViewModel.Items,
    Layout = new StackLayout { Spacing = 8 }
};
```

Avalonia XAML:

```xaml
<ListBox xmlns="https://github.com/avaloniaui"
         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
         ItemsSource="{Binding Items}">
  <ListBox.ItemsPanel>
    <ItemsPanelTemplate>
      <VirtualizingStackPanel />
    </ItemsPanelTemplate>
  </ListBox.ItemsPanel>
</ListBox>
```

Avalonia C#:

```csharp
var list = new ListBox
{
    ItemsSource = viewModel.Items,
    ItemTemplate = itemTemplate
};
```

## Migration Notes

1. Start with `ListBox` + `VirtualizingStackPanel` for production-ready virtualization.
2. Keep item templates lightweight and stable to preserve recycling performance.
3. Move specialized layout behavior into custom panels only when profiling justifies it.
