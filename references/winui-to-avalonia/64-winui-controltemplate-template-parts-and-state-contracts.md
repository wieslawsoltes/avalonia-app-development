# WinUI ControlTemplate, Template Parts, and State Contracts to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- ControlTemplate, TemplatePart attribute
- OnApplyTemplate, GetTemplateChild
- VisualStateManager.GoToState

Primary Avalonia APIs:

- ControlTheme + ControlTemplate
- TemplateAppliedEventArgs.NameScope
- PseudoClasses and selector-driven states
- TemplatedControl.OnApplyTemplate

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| template part contract (`PART_*`) | template part contract (`PART_*`) |
| `GetTemplateChild` lookup | `NameScope.Find<T>` lookup |
| `VisualStateManager.GoToState` | pseudo-class toggles + selectors/transitions |
| default template in generic styles | default `ControlTheme` |

## Conversion Example

WinUI XAML:

```xaml
<ControlTemplate TargetType="local:StatusBadge">
  <Border x:Name="PART_Indicator" />
</ControlTemplate>
```

WinUI C#:

```csharp
[TemplatePart(Name = "PART_Indicator", Type = typeof(Border))]
public sealed class StatusBadge : Control
{
    private Border? _indicator;

    protected override void OnApplyTemplate()
    {
        base.OnApplyTemplate();
        _indicator = GetTemplateChild("PART_Indicator") as Border;
        VisualStateManager.GoToState(this, IsWarning ? "Warning" : "Normal", false);
    }
}
```

Avalonia XAML:

```xaml
<ControlTheme xmlns="https://github.com/avaloniaui"
              xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
              xmlns:local="using:MyApp.Controls"
              TargetType="local:StatusBadge">
  <Setter Property="Template">
    <ControlTemplate>
      <Border x:Name="PART_Indicator" />
    </ControlTemplate>
  </Setter>
</ControlTheme>

<Style Selector="local|StatusBadge:warning /template/ Border#PART_Indicator">
  <Setter Property="Background" Value="OrangeRed" />
</Style>
```

Avalonia C#:

```csharp
public class StatusBadge : TemplatedControl
{
    public static readonly StyledProperty<bool> IsWarningProperty =
        AvaloniaProperty.Register<StatusBadge, bool>(nameof(IsWarning));

    private Border? _indicator;

    public bool IsWarning
    {
        get => GetValue(IsWarningProperty);
        set => SetValue(IsWarningProperty, value);
    }

    protected override void OnApplyTemplate(TemplateAppliedEventArgs e)
    {
        base.OnApplyTemplate(e);
        _indicator = e.NameScope.Find<Border>("PART_Indicator");
        PseudoClasses.Set(":warning", IsWarning);
    }

    protected override void OnPropertyChanged(AvaloniaPropertyChangedEventArgs change)
    {
        base.OnPropertyChanged(change);
        if (change.Property == IsWarningProperty)
            PseudoClasses.Set(":warning", IsWarning);
    }
}
```

## Migration Notes

1. Keep `PART_*` contracts stable and documented during migration.
2. Replace imperative state switching with pseudo-class state projection where possible.
3. Re-run part lookup logic on template reapply; do not assume one-time template lifetime.
