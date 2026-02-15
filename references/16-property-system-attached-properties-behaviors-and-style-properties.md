# Property System, Attached Properties, Behaviors, and Style Properties

## Table of Contents
1. Scope and APIs
2. Avalonia Property System
3. Property Identity, Flags, and Metadata Lookup
4. Metadata and Binding Defaults
5. Effective Values, Base Values, and Priority-Safe Updates
6. Change Events and Registry Diagnostics
7. Attached Property Authoring
8. Behavior Patterns
9. Style Property Authoring
10. Container Queries (Media Query Equivalent)
11. Best Practices
12. Troubleshooting
13. XAML-First and Code-Only Usage

## Scope and APIs

Primary APIs:
- `AvaloniaProperty.Register<TOwner, TValue>(...)`
- `AvaloniaProperty.RegisterAttached<...>(...)`
- `AvaloniaProperty.RegisterDirect<...>(...)`
- `AvaloniaProperty.Name`, `PropertyType`, `OwnerType`
- `AvaloniaProperty.GetMetadata<T>()` / `GetMetadata(Type)` / `GetMetadata(AvaloniaObject)`
- `AvaloniaProperty.IsValidValue(object?)`
- `AvaloniaProperty.UnsetValue` and `UnsetValueType`
- `StyledProperty<T>`
- `AttachedProperty<T>`
- `DirectProperty<TOwner, TValue>`
- `AvaloniaObject.GetValue/SetValue/ClearValue/SetCurrentValue`
- `AvaloniaObject.Bind(...)`
- `AvaloniaPropertyChangedEventArgs` / `AvaloniaPropertyChangedEventArgs<T>`
- `AvaloniaPropertyChangedExtensions`
- `AvaloniaPropertyRegistry`
- `Setter`, `Style`, `Styles`, `Selectors`
- `ContainerQuery`, `Container.Name`, `Container.Sizing`
- `Interactive`, routed events, `InteractiveExtensions`

Reference source files:
- `src/Avalonia.Base/AvaloniaProperty.cs`
- `src/Avalonia.Base/AvaloniaObject.cs`
- `src/Avalonia.Base/AttachedProperty.cs`
- `src/Avalonia.Base/DirectProperty.cs`
- `src/Avalonia.Base/StyledProperty.cs`
- `src/Avalonia.Base/AvaloniaPropertyMetadata.cs`
- `src/Avalonia.Base/AvaloniaPropertyRegistry.cs`
- `src/Avalonia.Base/AvaloniaPropertyChangedEventArgs.cs`
- `src/Avalonia.Base/AvaloniaPropertyChangedExtensions.cs`
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

## Property Identity, Flags, and Metadata Lookup

Every `AvaloniaProperty` exposes identity and capability flags:
- `Name`
- `PropertyType`
- `OwnerType`
- `Inherits`
- `IsAttached`
- `IsDirect`
- `IsReadOnly`

Metadata and validation query APIs:
- `GetMetadata<T>()`
- `GetMetadata(Type)`
- `GetMetadata(AvaloniaObject)`
- `IsValidValue(object?)`

Indexer helper operators:
- `operator !(AvaloniaProperty)` for property-indexer binding descriptors.
- `operator ~(AvaloniaProperty)` for descriptor inversion workflows.

Unset marker semantics:
- `AvaloniaProperty.UnsetValue` is a singleton `UnsetValueType`.
- `UnsetValueType` means “no value provided by this source”, which is different from `null`.

Administrative cleanup API:
- `Unregister(Type)` exists for specialized cleanup/testing paths, not normal app runtime flows.

Example:

```csharp
AvaloniaProperty property = TextBox.TextProperty;
string name = property.Name;
Type propertyType = property.PropertyType;
Type ownerType = property.OwnerType;

AvaloniaPropertyMetadata metadataByType = property.GetMetadata(typeof(TextBox));
AvaloniaPropertyMetadata metadataByInstance = property.GetMetadata(textBox);

object? candidate = "hello";
if (!property.IsValidValue(candidate))
    candidate = AvaloniaProperty.UnsetValue; // UnsetValueType marker

var descriptor = ~property;
```

## Metadata and Binding Defaults

`AvaloniaPropertyMetadata` controls binding and validation behavior at registration/owner level.

Key points:
- `DefaultBindingMode` resolves `BindingMode.Default` to a concrete mode (commonly `OneWay`).
- `EnableDataValidation` opt-in controls whether a property participates in data-validation messages.
- metadata is merged per owner; call `AddOwner(...)` + optional metadata overrides for owner-specific behavior.

`StyledProperty<T>` advanced APIs:
- `AddOwner<TOwner>(...)`
- `OverrideMetadata<T>(...)`
- `OverrideDefaultValue<T>(...)`
- `GetDefaultValue(Type)` / `GetDefaultValue(AvaloniaObject)`
- `CoerceValue(AvaloniaObject, TValue)`
- `ValidateValue`

`DirectProperty<TOwner, TValue>` advanced owner extension:
- `AddOwner<TNewOwner>(getter, setter, unsetValue, defaultBindingMode, enableDataValidation)`
- `Getter`

Metadata lifecycle APIs (mainly for control/framework authors):
- `AvaloniaPropertyMetadata.Merge(...)`
- `AvaloniaPropertyMetadata.Freeze()`
- `AvaloniaPropertyMetadata.IsReadOnly`
- `AvaloniaPropertyMetadata.GenerateTypeSafeMetadata()`

Use these APIs to tune property behavior per control family, not per instance.

Notes:
- `StyledProperty<T>.ValidateValue` is the runtime predicate used to validate typed values before they become effective.
- `DirectProperty<TOwner, TValue>.Getter` exposes the field-backed read delegate used by direct property access paths.

## Effective Values, Base Values, and Priority-Safe Updates

Important distinction:
- effective value: what the control currently sees (after bindings/styles/animation),
- base value: styled property value excluding animation and excluding inherited/default fallback.

Useful APIs:
- `GetBaseValue<T>(StyledProperty<T>)`
- `IsAnimating(AvaloniaProperty)`
- `IsSet(AvaloniaProperty)`
- `SetCurrentValue(...)` (preserve existing binding/style source)
- `CoerceValue(AvaloniaProperty)`
- `AvaloniaProperty.UnsetValue`

`UnsetValue` versus `null`:
- `null` can be a valid effective value for many reference-type properties.
- `AvaloniaProperty.UnsetValue` (`UnsetValueType`) means the current source did not produce a value, so priority fallback continues.

Example:

```csharp
if (control.IsSet(MyControl.ValueProperty))
{
    var baseValue = control.GetBaseValue(MyControl.ValueProperty).GetValueOrDefault();
    // Use baseValue for diagnostics or non-animated logic paths.
}

control.SetCurrentValue(MyControl.ValueProperty, 42);
control.CoerceValue(MyControl.ValueProperty);
```

When updating control-owned properties at runtime, prefer `SetCurrentValue` over `SetValue` to avoid accidentally breaking app-declared bindings and style precedence.

## Change Events and Registry Diagnostics

Change event APIs:
- `AvaloniaObject.PropertyChanged`
- `AvaloniaProperty.Changed`
- `AvaloniaPropertyChangedEventArgs(AvaloniaObject sender, BindingPriority priority)`
- `AvaloniaPropertyChangedEventArgs.Property`
- `AvaloniaPropertyChangedEventArgs.Sender`
- `AvaloniaPropertyChangedEventArgs.Priority`
- `AvaloniaPropertyChangedEventArgs.OldValue` / `AvaloniaPropertyChangedEventArgs.NewValue`
- typed argument paths via `AvaloniaPropertyChangedEventArgs<T>`
- typed values on generic args:
  - `AvaloniaPropertyChangedEventArgs<T>.OldValue`
  - `AvaloniaPropertyChangedEventArgs<T>.NewValue`
- strongly-typed helper extensions:
  - `AvaloniaPropertyChangedExtensions.GetOldValue<T>()`
  - `AvaloniaPropertyChangedExtensions.GetNewValue<T>()`

Typed constructor path for manual advanced scenarios:
- `AvaloniaPropertyChangedEventArgs<T>(AvaloniaObject sender, AvaloniaProperty<T> property, Optional<T> oldValue, BindingValue<T> newValue, BindingPriority priority)`

Registry APIs (diagnostics/tooling oriented):
- `AvaloniaPropertyRegistry.Instance`
- `GetRegistered(Type)` / `GetRegisteredAttached(Type)` / `GetRegisteredDirect(Type)` / `GetRegisteredInherited(Type)`
- `FindRegistered(Type, string)` / `FindRegistered(AvaloniaObject, string)`
- `FindRegisteredDirect<T>(AvaloniaObject, DirectPropertyBase<T>)`
- `IsRegistered(Type, AvaloniaProperty)` / `IsRegistered(object, AvaloniaProperty)`
- `UnregisterByModule(IEnumerable<Type>)`

Practical uses:
- verify attached/direct registration during control migrations,
- detect incorrect owner registration when a property appears to be ignored,
- build lightweight diagnostics tooling for property discovery.

Example:

```csharp
control.PropertyChanged += (_, e) =>
{
    if (e.Property == TextBox.TextProperty)
    {
        string? oldText = e.GetOldValue<string?>();
        string? newText = e.GetNewValue<string?>();
    }
};

var registry = AvaloniaPropertyRegistry.Instance;
bool isRegistered = registry.IsRegistered(typeof(TextBox), TextBox.TextProperty);
```

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
