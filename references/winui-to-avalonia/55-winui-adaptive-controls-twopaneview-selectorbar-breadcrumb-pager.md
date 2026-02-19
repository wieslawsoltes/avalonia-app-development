# WinUI Adaptive Controls (TwoPaneView/SelectorBar/Breadcrumb/Pager) to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- TwoPaneView, SelectorBar, BreadcrumbBar, PagerControl, PipsPager

Primary Avalonia APIs:

- Grid/SplitView, TabStrip, ItemsControl, ToggleButton/RadioButton selectors, custom breadcrumb templates

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| TwoPaneView auto-adaptive layout | responsive Grid/SplitView with breakpoints |
| SelectorBar segmented navigation | TabStrip or styled SelectingItemsControl |
| BreadcrumbBar | ItemsControl + separator template + command navigation |
| PagerControl/PipsPager | command-driven page index + indicator items |

## Conversion Example

WinUI XAML:

```xaml
<TwoPaneView WideModeConfiguration="LeftRight"
             TallModeConfiguration="TopBottom"
             MinWideModeWidth="900">
  <TwoPaneView.Pane1>
    <BreadcrumbBar ItemsSource="{x:Bind ViewModel.Path}" />
  </TwoPaneView.Pane1>
  <TwoPaneView.Pane2>
    <PipsPager NumberOfPages="{x:Bind ViewModel.PageCount}" SelectedPageIndex="{x:Bind ViewModel.PageIndex, Mode=TwoWay}" />
  </TwoPaneView.Pane2>
</TwoPaneView>
```

WinUI C#:

```csharp
var pager = new PipsPager
{
    NumberOfPages = viewModel.PageCount,
    SelectedPageIndex = viewModel.PageIndex
};
```

Avalonia XAML:

```xaml
<Grid xmlns="https://github.com/avaloniaui"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      ColumnDefinitions="Auto,*"
      RowDefinitions="Auto,*">
  <ItemsControl Grid.Row="0" Grid.ColumnSpan="2" ItemsSource="{Binding PathSegments}" />

  <TabStrip Grid.Row="1" Grid.Column="0" ItemsSource="{Binding Sections}" />

  <StackPanel Grid.Row="1" Grid.Column="1" Orientation="Horizontal" HorizontalAlignment="Center" Spacing="6">
    <Button Content="Prev" Command="{Binding PrevPageCommand}" />
    <TextBlock Text="{Binding PageDisplayText}" VerticalAlignment="Center" />
    <Button Content="Next" Command="{Binding NextPageCommand}" />
  </StackPanel>
</Grid>
```

Avalonia C#:

```csharp
var root = new Grid
{
    ColumnDefinitions = new ColumnDefinitions("Auto,*"),
    RowDefinitions = new RowDefinitions("Auto,*")
};

var tabs = new TabStrip { ItemsSource = viewModel.Sections };
var breadcrumb = new ItemsControl { ItemsSource = viewModel.PathSegments };
```

## Migration Notes

1. Replace one-to-one adaptive controls with composable layout primitives.
2. Keep adaptation rules centralized (window width, orientation, feature flags).
3. Build pager and breadcrumb semantics as reusable components for consistency.
