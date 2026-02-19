# WinUI ContentDialog and Modal Workflow Migration to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- ContentDialog, ContentDialogResult, ShowAsync, Primary/Secondary buttons

Primary Avalonia APIs:

- Window, ShowDialog, Task-based dialog result patterns

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| WinUI control and state pipeline | Avalonia control themes, selectors, and transitions |
| WinUI command/input surfaces | Avalonia commands + `KeyBinding`/routed input |
| WinUI resource/theme flow | Avalonia resource dictionaries + `ThemeVariant` |

## Conversion Example

WinUI XAML:

```xaml
<ContentDialog x:Name="ConfirmDialog" Title="Delete item?" PrimaryButtonText="Delete" CloseButtonText="Cancel" />
```

WinUI C#:

```csharp
var result = await confirmDialog.ShowAsync();
```

Avalonia XAML:

```xaml
<Window x:Class="MyApp.Views.ConfirmDialog" Width="420" Height="180"><StackPanel Margin="16" Spacing="12"><TextBlock Text="Delete item?" /><StackPanel Orientation="Horizontal" HorizontalAlignment="Right" Spacing="8"><Button IsCancel="True" Content="Cancel" /><Button IsDefault="True" Content="Delete" /></StackPanel></StackPanel></Window>
```

Avalonia C#:

```csharp
var result = await confirmWindow.ShowDialog<bool>(owner);
```

## Migration Notes

1. Preserve behavior and interaction contracts before visual refinements.
2. Port hot paths with explicit UI-thread and invalidation discipline.
3. Prefer typed compiled bindings and deterministic state flow in migrated views.
