# Property System, Attached Properties, Behaviors, and Style Properties

## Table of Contents
1. Scope and APIs
2. Avalonia Property System
3. Attached Property Authoring
4. Behavior Patterns
5. Style Property Authoring
6. Container Queries (Media Query Equivalent)
7. Best Practices
8. Troubleshooting

## Scope and APIs

Primary APIs:
- `AvaloniaProperty.Register<TOwner, TValue>(...)`
- `AvaloniaProperty.RegisterAttached<...>(...)`
- `AvaloniaProperty.RegisterDirect<...>(...)`
- `StyledProperty<T>`
- `AttachedProperty<T>`
- `DirectProperty<TOwner, TValue>`
- `AvaloniaObject.GetValue/SetValue/ClearValue/SetCurrentValue`
- `AvaloniaObject.Bind(...)`
- `Setter`, `Style`, `Styles`, `Selectors`
- `ContainerQuery`, `Container.Name`, `Container.Sizing`
- `Interactive`, routed events, `InteractiveExtensions`

Reference source files:
- `src/Avalonia.Base/AvaloniaProperty.cs`
- `src/Avalonia.Base/AvaloniaObject.cs`
- `src/Avalonia.Base/AttachedProperty.cs`
- `src/Avalonia.Base/DirectProperty.cs`
- `src/Avalonia.Base/Styling/Setter.cs`
- `src/Avalonia.Base/Styling/Style.cs`
- `src/Avalonia.Base/Styling/ContainerQuery.cs`
- `src/Avalonia.Base/Styling/Container.cs`

## Avalonia Property System

Property flavors:
- `StyledProperty<T>`: styleable, bindable, inheritable if configured.
- `AttachedProperty<T>`: property attached to other types.
- `DirectProperty<TOwner, TValue>`: field-backed, optionally read-only.

Read/write APIs:
- `GetValue(...)`
- `SetValue(...)`
- `SetCurrentValue(...)`
- `ClearValue(...)`
- `Bind(...)`

Choose registration based on need:
- Use `Register` for normal styleable control properties.
- Use `RegisterAttached` for layout/behavior metadata shared by arbitrary hosts.
- Use `RegisterDirect` for high-performance field-backed values.

## Attached Property Authoring

Canonical pattern:

```csharp
public static class FocusAssist
{
    public static readonly AttachedProperty<bool> HighlightWhenFocusedProperty =
        AvaloniaProperty.RegisterAttached<FocusAssist, Control, bool>("HighlightWhenFocused");

    static FocusAssist()
    {
        HighlightWhenFocusedProperty.Changed.AddClassHandler<Control>((control, e) =>
        {
            if (e.GetNewValue<bool>())
                control.Classes.Add("focus-highlight");
            else
                control.Classes.Remove("focus-highlight");
        });
    }

    public static bool GetHighlightWhenFocused(Control control) =>
        control.GetValue(HighlightWhenFocusedProperty);

    public static void SetHighlightWhenFocused(Control control, bool value) =>
        control.SetValue(HighlightWhenFocusedProperty, value);
}
```

XAML usage:

```xml
<TextBox local:FocusAssist.HighlightWhenFocused="True" />
```

## Behavior Patterns

Avalonia core does not provide a built-in `Behavior<T>` base in this repository.

Preferred behavior patterns in core apps:
- Attached property + changed handler + routed event subscriptions.
- Reusable helper classes over ad-hoc code-behind.
- Routed event APIs via `Interactive.AddHandler` or `InteractiveExtensions.GetObservable`.

Use cases:
- Declarative interaction toggles.
- Cross-control policies (validation visuals, keyboard behavior, drag policies).

## Style Property Authoring

In styles/themes:
- Set only valid property values through `Setter(Property, Value)`.
- Use selectors with clear scope.
- Avoid huge descendant chains when a class selector would do.

Typed C# selector example:

```csharp
var style = new Style(x => x.OfType<Button>().Class("primary"));
style.Setters.Add(new Setter(Button.FontWeightProperty, FontWeight.SemiBold));
```

## Container Queries (Media Query Equivalent)

Avalonia equivalent of media-query-like behavior uses `ContainerQuery`.

Key APIs:
- `ContainerQuery.Query`
- `ContainerQuery.Name`
- `Container.Name` attached property
- `Container.Sizing` attached property

Example from sample style pattern:

```xml
<ContainerQuery Name="Host" Query="min-width:800">
  <Style Selector="UniformGrid#ContentGrid">
    <Setter Property="Columns" Value="3" />
  </Style>
</ContainerQuery>

<Border Container.Name="Host" Container.Sizing="Width" />
```

## Best Practices

- Favor styled properties for themeability.
- Keep attached properties small and single-purpose.
- Use `SetCurrentValue` when preserving existing binding/priority semantics.
- Keep behavior code deterministic and easy to detach.
- Treat runtime selector parser paths as advanced (trimming-sensitive) scenarios.

## Troubleshooting

1. Setter value invalid for property:
- Type mismatch or unsupported value conversion.

2. Direct property cannot be set from style:
- Direct properties with style activators can be restricted; use styled property when style-driven changes are required.

3. Attached property appears ignored:
- Getter/setter type mismatch or wrong host type in registration.

4. Container query not triggering:
- Missing `Container.Name` or `Container.Sizing` on expected container.
- Query condition does not match current container dimensions.

## XAML-First and Code-Only Usage

Default mode:
- Apply attached properties and style selectors from XAML first.
- Build style/property wiring in code only when requested.

XAML-first complete example:

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            xmlns:local="using:MyApp.Behaviors"
            Spacing="8">
  <TextBox local:FocusAssist.HighlightWhenFocused="True" />
  <Button Classes="primary" Content="Submit" />
</StackPanel>
```

Code-only alternative (on request):

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;
using Avalonia.Styling;

var text = new TextBox();
FocusAssist.SetHighlightWhenFocused(text, true);

var style = new Style(x => x.OfType<Button>().Class("primary"));
style.Setters.Add(new Setter(Button.FontWeightProperty, FontWeight.SemiBold));
Application.Current!.Styles.Add(style);
```
