# WinUI SwipeControl List Gestures and Item Actions to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- SwipeControl, SwipeItems, SwipeItem, Invoked

Primary Avalonia APIs:

- ContextFlyout/MenuFlyout, MenuItem commands, GestureRecognizers, PullGestureRecognizer

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| SwipeControl reveal actions | ContextFlyout/ContextMenu action surface |
| SwipeItem invoked callbacks | MenuItem commands |
| Directional swipe semantics | PullGestureRecognizer + custom threshold logic |
| inline action affordances | templated item with command buttons |

## Conversion Example

WinUI XAML:

```xaml
<SwipeControl>
  <SwipeControl.RightItems>
    <SwipeItems>
      <SwipeItem Text="Delete" Invoked="OnDeleteInvoked" />
    </SwipeItems>
  </SwipeControl.RightItems>
  <Grid>
    <TextBlock Text="{x:Bind ViewModel.Subject}" />
  </Grid>
</SwipeControl>
```

WinUI C#:

```csharp
var swipe = new SwipeControl();
var rightItems = new SwipeItems();
rightItems.Add(new SwipeItem { Text = "Archive", Command = ViewModel.ArchiveCommand });
swipe.RightItems = rightItems;
```

Avalonia XAML:

```xaml
<Border xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <Border.GestureRecognizers>
    <PullGestureRecognizer PullDirection="RightToLeft" />
  </Border.GestureRecognizers>

  <Border.ContextFlyout>
    <MenuFlyout>
      <MenuItem Header="Archive" Command="{Binding ArchiveCommand}" />
      <MenuItem Header="Delete" Command="{Binding DeleteCommand}" />
    </MenuFlyout>
  </Border.ContextFlyout>

  <TextBlock Text="{Binding Subject}" />
</Border>
```

Avalonia C#:

```csharp
var item = new Border();
item.GestureRecognizers.Add(new PullGestureRecognizer(PullDirection.RightToLeft));

var flyout = new MenuFlyout();
flyout.Items.Add(new MenuItem { Header = "Archive", Command = viewModel.ArchiveCommand });
flyout.Items.Add(new MenuItem { Header = "Delete", Command = viewModel.DeleteCommand });
item.ContextFlyout = flyout;
```

## Migration Notes

1. Avalonia has no direct `SwipeControl`; compose gesture + flyout patterns.
2. Keep destructive actions command-based with confirm/undo workflows.
3. Use consistent action surfaces for touch and pointer parity.
