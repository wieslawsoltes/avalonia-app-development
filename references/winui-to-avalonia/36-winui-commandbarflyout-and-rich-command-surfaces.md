# WinUI CommandBarFlyout and Rich Command Surfaces to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- CommandBar, CommandBarFlyout, AppBarButton, AppBarToggleButton, MenuFlyout

Primary Avalonia APIs:

- MenuFlyout, MenuItem, SplitButton, DropDownButton, KeyBinding

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| WinUI control and state pipeline | Avalonia control themes, selectors, and transitions |
| WinUI command/input surfaces | Avalonia commands + `KeyBinding`/routed input |
| WinUI resource/theme flow | Avalonia resource dictionaries + `ThemeVariant` |

## Conversion Example

WinUI XAML:

```xaml
<Button Content="Actions"><Button.Flyout><CommandBarFlyout><AppBarButton Label="Save" Icon="Save" /></CommandBarFlyout></Button.Flyout></Button>
```

WinUI C#:

```csharp
var flyout = new CommandBarFlyout();
```

Avalonia XAML:

```xaml
<SplitButton Content="Actions"><SplitButton.Flyout><MenuFlyout><MenuItem Header="Save" Command="{Binding SaveCommand}" /></MenuFlyout></SplitButton.Flyout></SplitButton>
```

Avalonia C#:

```csharp
var split = new SplitButton { Content = "Actions", Command = viewModel.PrimaryCommand };
```

## Migration Notes

1. Preserve behavior and interaction contracts before visual refinements.
2. Port hot paths with explicit UI-thread and invalidation discipline.
3. Prefer typed compiled bindings and deterministic state flow in migrated views.
