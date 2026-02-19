# WinUI ScrollPresenter/ScrollView and Snap Behaviors to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- ScrollPresenter, ScrollView, ChangeView/ScrollTo, snap points, chaining

Primary Avalonia APIs:

- ScrollViewer, Offset, ScrollChanged, snap point attached properties, scroll chaining/inertia properties

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| ScrollView.ScrollTo / presenter view changes | ScrollViewer.Offset and scroll methods |
| Snap points configuration | ScrollViewer snap point attached properties |
| Scroll chaining toggles | ScrollViewer.IsScrollChainingEnabled |
| Inertia behavior toggles | ScrollViewer.IsScrollInertiaEnabled |

## Conversion Example

WinUI XAML:

```xaml
<muxc:ScrollView x:Name="Host">
  <ListView x:Name="ItemsList" />
</muxc:ScrollView>
```

WinUI C#:

```csharp
Host.ScrollTo(0, 240);
ItemsList.ScrollIntoView(ViewModel.Items[20]);
```

Avalonia XAML:

```xaml
<ScrollViewer xmlns="https://github.com/avaloniaui"
              xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
              x:Name="Host"
              ScrollViewer.VerticalSnapPointsType="MandatorySingle"
              ScrollViewer.VerticalSnapPointsAlignment="Near"
              ScrollViewer.IsScrollChainingEnabled="True"
              ScrollViewer.IsScrollInertiaEnabled="True">
  <ListBox x:Name="ItemsList" ItemsSource="{Binding Items}" />
</ScrollViewer>
```

Avalonia C#:

```csharp
Host.Offset = new Vector(0, 240);
ItemsList.BringIntoView();
```

## Migration Notes

1. Map programmatic scroll operations to `Offset`/scroll methods and item `BringIntoView`.
2. Configure snapping/chaining in XAML for predictable cross-platform behavior.
3. Avoid per-frame imperative scrolling unless implementing custom interaction models.
