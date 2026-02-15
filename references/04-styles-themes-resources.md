# Styles, Themes, and Resources

## Styling Surface

Primary APIs:

- `Style`
- `Styles`
- `ControlTheme`
- `Selectors`
- `ThemeVariant`
- `ThemeVariantScope`
- `ResourceDictionary`
- `StyleBase`, `SetterBase`
- `StyleQuery`, `StyleQueries`, `StyleQueryComparisonOperator`
- `IStyleHost`, `IStyleable`, `IThemeVariantHost`, `IGlobalStyles`
- `ISetterInstance`, `ISetterValue`
- `ContainerSizing`

## Recommended Layering

1. `Application.Styles`
- global themes and broad app-level style policy.

2. `ControlTheme`
- control-family skinning and templated look.

3. Local `Style`
- narrow view-local adjustments.

4. Resources and theme dictionaries
- stable keys for colors/spacing/metrics.

## Runtime `Styles` Collection Operations

`Styles` is a mutable style collection and a resource provider.

High-value members for runtime composition:

- `Count`, `Owner`, `Resources`
- indexer `this[int index]`
- `CollectionChanged`, `OwnerChanged`
- `TryGetResource(...)`

Batch and reordering APIs:

- `AddRange(...)`, `InsertRange(...)`
- `Move(...)`, `MoveRange(...)`
- `RemoveAll(...)`, `RemoveRange(...)`
- `IndexOf(...)`, `Insert(...)`, `RemoveAt(...)`
- `Contains(...)`, `CopyTo(...)`, `GetEnumerator()`

Use `AddRange`/`InsertRange` and `MoveRange` when applying feature packs to reduce churn vs per-item edits.

```csharp
var styles = Application.Current!.Styles;

styles.AddRange(new IStyle[]
{
    new Style(x => x.OfType<Button>().Class("accent"))
    {
        Setters =
        {
            new Setter(Button.FontWeightProperty, FontWeight.Bold)
        }
    }
});

if (styles.Contains(styles[0]))
    styles.Move(0, styles.Count - 1);
```

Framework-level style contracts used by control/theme infrastructure:

- `StyleBase.Parent`, `StyleBase.Setters`
- `IGlobalStyles.GlobalStylesAdded`, `IGlobalStyles.GlobalStylesRemoved`
- `IStyleHost`, `IStyleable`, `IThemeVariantHost`
- `ISetterInstance`, `ISetterValue`, `SetterBase`

## Selector API Strategy (`Selectors`)

Typed selector APIs are easier to refactor than long selector strings.

Commonly useful APIs:

- `Selectors.Is(...)`, `Selectors.Is<T>()`
- `Selectors.OfType(...)`, `Selectors.OfType<T>()`
- `Selectors.Class(...)`, `Selectors.Name(...)`
- `Selectors.Child()`, `Selectors.Descendant()`, `Selectors.Template()`, `Selectors.Nesting()`
- `Selectors.Not(...)`
- `Selectors.NthChild(...)`, `Selectors.NthLastChild(...)`
- `Selectors.Or(...)`
- `Selectors.PropertyEquals(...)`

Container-query helper contracts:

- `StyleQuery`
- `StyleQueryComparisonOperator`
- `StyleQueries.And(params StyleQuery[] queries)`
- `StyleQueries.And(IReadOnlyList<StyleQuery> query)`

```csharp
var selector = default(Selector?)
    .Is<Button>()
    .Class("accent")
    .Not(x => x.Class("danger"))
    .NthChild(step: 2, offset: 1);

var style = new Style(_ => selector!);
```

## Theme Variant Model

Core values and fields:

- `ThemeVariant.Default`, `ThemeVariant.Light`, `ThemeVariant.Dark`
- `ThemeVariant.InheritVariant`
- explicit conversion operators between `ThemeVariant` and `PlatformThemeVariant`

App and subtree controls:

- `Application.RequestedThemeVariant`
- `ThemeVariantScope.RequestedThemeVariant`
- `ActualThemeVariant`
- `ThemeVariantTypeConverter` (`CanConvertFrom(...)`, `ConvertFrom(...)`)

Use `ThemeVariantScope` for local overrides and avoid branching style logic in code.

## Resource Dictionaries in Style Pipelines

`ResourceDictionary` features commonly used with styles:

- `MergedDictionaries`, `ThemeDictionaries`
- `TryGetResource(...)`
- `AddDeferred(...)` / `AddNotSharedDeferred(...)`
- `SetItems(...)`, `ContainsKey(...)`, `EnsureCapacity(...)`

Deferred resource entries are useful when expensive value construction should happen only if a key is requested.

Container sizing attached-property APIs (media-query-like behavior):

- `Container.SizingProperty`
- `Container.GetSizing(...)`
- `Container.SetSizing(...)`
- `ContainerSizing` (`Normal`, `Width`, `Height`, `WidthAndHeight`)

## Includes, Dynamic Resources, and AOT Notes

XAML include and dynamic-resource APIs:

- `StyleInclude`, `ResourceInclude`
- `DynamicResourceExtension` (`ResourceKey`)

Guidance:

- keep default style/theme definitions in compiled XAML,
- use runtime include/dynamic-resource patterns for explicit plugin or user-driven theme swaps.

## Common Styling Mistakes

1. Massive global style files with unclear ownership.
- Fix: split by feature/control category and use `AddRange` for bundle registration.

2. Runtime mutation without ordering discipline.
- Fix: use `Move`/`MoveRange` when precedence must be explicit.

3. Overly complex selector chains.
- Fix: prefer clear classes and typed `Selectors` composition.

4. Theme logic in code-behind.
- Fix: use `ThemeDictionaries` + `DynamicResource`.

## XAML-First and Code-Only Usage

Default mode:

- author styles/themes/resources in XAML first,
- use code-only style composition when runtime style packs are required.

XAML-first usage example:

```xml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             x:Class="MyApp.App">
  <Application.Resources>
    <Color x:Key="AccentColor">#2F6FED</Color>
    <SolidColorBrush x:Key="AccentBrush" Color="{DynamicResource AccentColor}" />
  </Application.Resources>

  <Application.Styles>
    <Style Selector="Button.accent">
      <Setter Property="Background" Value="{DynamicResource AccentBrush}" />
      <Setter Property="Foreground" Value="White" />
    </Style>
  </Application.Styles>
</Application>
```

Code-only alternative (on request):

```csharp
var style = new Style(x => x.OfType<Button>().Class("accent"));
style.Setters.Add(new Setter(Button.BackgroundProperty, Brushes.SteelBlue));
style.Setters.Add(new Setter(Button.ForegroundProperty, Brushes.White));
Application.Current!.Styles.Add(style);
```
