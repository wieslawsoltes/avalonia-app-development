# WinUI Text Editing, IME, Undo/Redo, and InputScope to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- TextBox, SelectionStart, SelectionLength, CanUndo, Undo, Redo, InputScope

Primary Avalonia APIs:

- TextBox, SelectionStart, SelectionEnd, CanUndo, Undo, Redo, TextInputOptions

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| TextBox.InputScope | TextInputOptions.ContentType |
| Return key hints | TextInputOptions.ReturnKeyType |
| Undo/Redo APIs | Undo/Redo APIs on TextBox |
| SelectionStart + SelectionLength | SelectionStart + SelectionEnd/SelectAll |
| TextChanging/TextChanged | TextChanging/TextChanged |

## Conversion Example

WinUI XAML:

```xaml
<TextBox x:Name="Editor"
         Text="{x:Bind ViewModel.Query, Mode=TwoWay}"
         InputScope="Search"
         AcceptsReturn="True" />
```

WinUI C#:

```csharp
if (Editor.CanUndo)
    Editor.Undo();

Editor.SelectionStart = 0;
Editor.SelectionLength = Editor.Text?.Length ?? 0;
```

Avalonia XAML:

```xaml
<TextBox xmlns="https://github.com/avaloniaui"
         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
         x:Name="Editor"
         Text="{Binding Query}"
         AcceptsReturn="True"
         TextInputOptions.ContentType="Search"
         TextInputOptions.ReturnKeyType="Search" />
```

Avalonia C#:

```csharp
if (Editor.CanUndo)
    Editor.Undo();

Editor.SelectAll();

if (Editor.CanRedo)
    Editor.Redo();
```

## Migration Notes

1. Move `InputScope` intent to `TextInputOptions` attached properties.
2. Keep undo/redo command wiring bound to `CanUndo`/`CanRedo`.
3. Prefer explicit text-input options for mobile/IME parity.
