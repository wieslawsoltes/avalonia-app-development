# WinUI Property Types, Metadata, and Value Precedence to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- DependencyProperty.Register, DependencyProperty.RegisterAttached, PropertyMetadata
- DependencyObject.GetValue, SetValue, ClearValue, ReadLocalValue

Primary Avalonia APIs:

- AvaloniaProperty.Register, RegisterAttached, RegisterDirect
- StyledProperty, AttachedProperty, DirectProperty
- AvaloniaObject.GetValue, SetValue, SetCurrentValue, ClearValue, GetBaseValue
- BindingPriority

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| dependency property (styled storage) | `StyledProperty<T>` |
| attached dependency property | `AttachedProperty<T>` |
| CLR-backed dependency property with custom storage | `DirectProperty<T>` |
| property metadata default + callback | register default + `OnPropertyChanged`/class handlers |
| value precedence (local/style/template/default) | `BindingPriority`-based precedence |

## Conversion Example

WinUI XAML:

```xaml
<local:StatusChip State="Warning"
                  local:StatusChip.IsEmphasis="True" />
```

WinUI C#:

```csharp
public sealed class StatusChip : Control
{
    public static readonly DependencyProperty StateProperty =
        DependencyProperty.Register(
            nameof(State),
            typeof(string),
            typeof(StatusChip),
            new PropertyMetadata("Normal", OnStateChanged));

    public static readonly DependencyProperty IsEmphasisProperty =
        DependencyProperty.RegisterAttached(
            "IsEmphasis",
            typeof(bool),
            typeof(StatusChip),
            new PropertyMetadata(false));

    public string State
    {
        get => (string)GetValue(StateProperty);
        set => SetValue(StateProperty, value);
    }

    public static bool GetIsEmphasis(DependencyObject obj) => (bool)obj.GetValue(IsEmphasisProperty);
    public static void SetIsEmphasis(DependencyObject obj, bool value) => obj.SetValue(IsEmphasisProperty, value);

    private static void OnStateChanged(DependencyObject d, DependencyPropertyChangedEventArgs e)
    {
    }
}
```

Avalonia XAML:

```xaml
<local:StatusChip State="Warning"
                  local:StatusChip.IsEmphasis="True" />
```

Avalonia C#:

```csharp
public class StatusChip : Control
{
    public static readonly StyledProperty<string> StateProperty =
        AvaloniaProperty.Register<StatusChip, string>(nameof(State), "Normal");

    public static readonly AttachedProperty<bool> IsEmphasisProperty =
        AvaloniaProperty.RegisterAttached<StatusChip, Control, bool>("IsEmphasis", false);

    public string State
    {
        get => GetValue(StateProperty);
        set => SetValue(StateProperty, value);
    }

    public static bool GetIsEmphasis(Control obj) => obj.GetValue(IsEmphasisProperty);
    public static void SetIsEmphasis(Control obj, bool value) => obj.SetValue(IsEmphasisProperty, value);

    static StatusChip()
    {
        AffectsRender<StatusChip>(StateProperty);
    }

    public void SetStateWithoutBreakingBindings(string next)
    {
        SetCurrentValue(StateProperty, next);
    }
}
```

## Migration Notes

1. Use `StyledProperty` for styleable values and `DirectProperty` only when custom backing storage is required.
2. Prefer `SetCurrentValue` when updating control state from code to avoid overriding bindings/styles.
3. Port precedence-sensitive code by validating effective value behavior under local, style, and template inputs.
