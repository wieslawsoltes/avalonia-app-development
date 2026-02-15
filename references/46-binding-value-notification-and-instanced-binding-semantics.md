# Binding Value, Notification, and Instanced Binding Semantics

## Table of Contents
1. Scope and APIs
2. Typed Binding Value States (`BindingValue<T>`)
3. Construction and Implicit Conversions (`BindingValue<T>`)
4. `Optional<T>` as a Missing-Value Primitive
5. Untyped Binding Error Channel (`BindingNotification`)
6. Typed/Untyped Bridging
7. Binding Chain Diagnostics (`BindingChainException`)
8. `BindingOperations.DoNothingType` and No-Update Semantics
9. `InstancedBinding` for Dynamic Pipelines
10. Binding Expression Control and Diagnostics
11. `IndexerDescriptor` and Property Indexer Binding
12. Practical Patterns
13. AOT and Trimming Notes
14. Troubleshooting

## Scope and APIs

Primary APIs:
- `BindingValue<T>`
- `BindingValueType`
- `BindingNotification`
- `BindingErrorType`
- `Optional<T>`
- `BindingChainException`
- `InstancedBinding`
- `IBinding`
- `BindingOperations`
- `BindingOperations.DoNothingType`
- `BindingExpressionBase`
- `IndexerDescriptor`

Compatibility-sensitive APIs in this space:
- `IBinding.Initiate(...)` (obsolete in 11.3.12)
- `BindingOperations.Apply(...)` (obsolete in 11.3.12)

Reference source files:
- `src/Avalonia.Base/Data/BindingValue.cs`
- `src/Avalonia.Base/Data/BindingNotification.cs`
- `src/Avalonia.Base/Data/Optional.cs`
- `src/Avalonia.Base/Data/BindingChainException.cs`
- `src/Avalonia.Base/Data/InstancedBinding.cs`
- `src/Avalonia.Base/Data/IBinding.cs`
- `src/Avalonia.Base/Data/BindingOperations.cs`
- `src/Avalonia.Base/Data/BindingExpressionBase.cs`
- `src/Avalonia.Base/Data/IndexerDescriptor.cs`
- `src/Avalonia.Base/AvaloniaObject.cs`
- `src/Avalonia.Base/AvaloniaObjectExtensions.cs`

## Typed Binding Value States (`BindingValue<T>`)

`BindingValue<T>` is the typed transport used in binding pipelines. It carries both value and state.

Core states (`BindingValueType`):
- `Value`
- `UnsetValue`
- `DoNothing`
- `BindingError` / `BindingErrorWithFallback`
- `DataValidationError` / `DataValidationErrorWithFallback`

Useful members:
- `Type`, `HasValue`, `HasError`, `Value`, `Error`
- `Unset`, `DoNothing`
- `BindingError(...)`, `DataValidationError(...)`
- `WithValue(...)`
- `GetValueOrDefault(...)`
- `ToOptional()`

Design implication:
- do not treat binding data as value-only in advanced flows,
- always branch on state when consuming `GetBindingObservable(...)`.

## Construction and Implicit Conversions (`BindingValue<T>`)

Construction and conversion APIs:
- `BindingValue(T value)`
- `implicit operator BindingValue<T>(T value)`
- `implicit operator BindingValue<T>(Optional<T> optional)`

Practical semantics:
- direct `T` conversion creates a `BindingValueType.Value` state,
- `Optional<T>` conversion preserves `HasValue` semantics (`default(Optional<T>)` maps to unset),
- these operators are convenient for adapters but can hide state transitions if overused.

Example:

```csharp
BindingValue<int> fromCtor = new BindingValue<int>(42);
BindingValue<int> fromImplicitValue = 42;

Optional<int> missing = default;
BindingValue<int> fromOptional = missing; // maps to unset semantics
```

## `Optional<T>` as a Missing-Value Primitive

`Optional<T>` is a small two-state value (`HasValue` / missing) used by property/binding internals.

Useful members:
- `HasValue`
- `Value`
- `GetValueOrDefault(...)`
- `Empty`
- `ToObject()`
- `operator Optional<T>`
- `OptionalExtensions.Cast<T>(...)`

Use:
- represent “value missing” distinctly from `null` for reference types,
- carry optional fallback values in typed binding error states.

Creation forms:
- `new Optional<T>(value)`
- implicit conversion via `operator Optional<T>` from plain `T`

Interop helper:
- `ToObject()` converts `Optional<T>` to `Optional<object?>` for untyped bridges.
- `OptionalExtensions.Cast<T>(...)` rehydrates typed optional values from untyped optional payloads.

## Untyped Binding Error Channel (`BindingNotification`)

`BindingNotification` is the untyped carrier for:
- error metadata (`Error`, `ErrorType`),
- optional fallback/passthrough value (`Value`, `HasValue`).

Useful APIs:
- constructors for value-only and error+fallback forms,
- `ExtractValue(...)`
- `UpdateValue(...)`
- `ExtractError(...)`
- `AddError(...)`
- `BindingNotification.Null`

Use it when integrating untyped binding edges, custom adapters, or diagnostics surfaces.

## Typed/Untyped Bridging

Bridge APIs:
- typed -> untyped: `BindingValue<T>.ToUntyped()`
- untyped -> typed: `BindingValue<T>.FromUntyped(...)`

Special-value mapping is stable:
- `AvaloniaProperty.UnsetValue` <-> `BindingValue<T>.Unset`
- `BindingOperations.DoNothing` <-> `BindingValue<T>.DoNothing`
- `BindingNotification` <-> `BindingError*` / `DataValidationError*` states

Example:

```csharp
BindingValue<string> typed = BindingValue<string>.BindingError(
    new InvalidOperationException("Missing source"),
    fallbackValue: "(fallback)");

object? untyped = typed.ToUntyped();
BindingValue<string> roundTrip = BindingValue<string>.FromUntyped(untyped);
```

## Binding Chain Diagnostics (`BindingChainException`)

`BindingChainException` is the dedicated exception type for binding chain parse/evaluation failures.

Constructor forms:
- `BindingChainException()`
- `BindingChainException(string message)`
- `BindingChainException(string message, string expression, string errorPoint)`

Diagnostic members:
- `ExpressionErrorPoint`
- overridden `Message`

Use:
- catch/log this exception type at dynamic-binding infrastructure boundaries,
- surface `ExpressionErrorPoint` in diagnostics UIs to show where the chain failed.

Example:

```csharp
catch (BindingChainException ex)
{
    logger.LogWarning("Binding chain failed: {Message} @ {ErrorPoint}", ex.Message, ex.ExpressionErrorPoint);
}
```

## `BindingOperations.DoNothingType` and No-Update Semantics

`BindingOperations.DoNothing` is a singleton marker whose runtime type is `BindingOperations.DoNothingType`.

Meaning:
- converter/adapter intentionally requests “do not update the target/source right now”.

Boundaries:
- valid as a binding pipeline marker,
- do not persist/store `BindingOperations.DoNothingType` in model state,
- do not confuse with `AvaloniaProperty.UnsetValue` (which means no value supplied by current source).

## `InstancedBinding` for Dynamic Pipelines

`InstancedBinding` represents a binding already initiated for a concrete target context.

Factory helpers:
- `InstancedBinding.OneTime(...)`
- `InstancedBinding.OneWay(...)`
- `InstancedBinding.OneWayToSource(...)`
- `InstancedBinding.TwoWay(...)`
- `WithPriority(...)`

Key fields:
- `Mode`
- `Priority`
- `Source`

Practical guidance:
- keep `InstancedBinding` usage for dynamic composition/infrastructure,
- for normal app UI, prefer normal XAML/C# binding APIs.
- avoid creating new app architecture around obsolete `IBinding.Initiate(...)` / `BindingOperations.Apply(...)` flows.

## Binding Expression Control and Diagnostics

For a bound property, `BindingOperations.GetBindingExpressionBase(...)` gives access to active expression control.

Useful controls:
- `UpdateSource()` for explicit-update scenarios,
- `UpdateTarget()` for source-to-target refresh.

Example:

```csharp
var expr = BindingOperations.GetBindingExpressionBase(textBox, TextBox.TextProperty);
expr?.UpdateSource();
```

If you use `UpdateSourceTrigger=Explicit`, this call is required to push value back.

## `IndexerDescriptor` and Property Indexer Binding

Advanced property-indexer binding path uses:
- `AvaloniaProperty` operators `!` and `~` to create `IndexerDescriptor`,
- `IndexerDescriptor.WithMode(...)` / `WithPriority(...)`.
- `IndexerDescriptor.SourceObservable` for direct observable source pipelines.
- `IndexerDescriptor.Description` for diagnostics-friendly binding summaries.

Example:

```csharp
var descriptor = !TextBox.TextProperty;
textBox[descriptor.WithMode(BindingMode.TwoWay)] = new ReflectionBinding(nameof(ViewModel.Query));
```

Use this only when dynamic property selection is required. For normal authoring, regular `Bind(...)` or XAML bindings are clearer.

## Practical Patterns

### 1) Consume typed binding stream with error channel

```csharp
using Avalonia;
using Avalonia.Data;

IDisposable sub = textBox
    .GetBindingObservable(TextBox.TextProperty)
    .Subscribe(v =>
    {
        if (v.HasError)
        {
            viewModel.ValidationMessage = v.Error?.Message;
            return;
        }

        if (v.Type == BindingValueType.Value)
            viewModel.LastText = v.GetValueOrDefault() ?? string.Empty;
    });
```

### 2) Preserve current value intentionally

When a custom converter/adapter returns `BindingOperations.DoNothing`, target value is retained.

Use this for partial-update workflows where “no change” is a valid output state.

### 3) Explicit source push in form commit

- bind input with explicit update trigger,
- call `UpdateSource()` on commit action.

This gives deterministic source updates and avoids per-keystroke writes.

## AOT and Trimming Notes

Advanced conversion paths can use runtime conversion logic (for example `BindingValue<T>.FromUntyped(...)`).

Guidance:
- keep such bridges localized,
- favor strongly typed compiled binding paths for core app flows,
- treat dynamic conversion-heavy paths as opt-in infrastructure.

## Troubleshooting

1. Value appears lost after adapter step
- Verify whether result was `UnsetValue` (fallback/default path) vs `DoNothing` (retain current target value).

2. Error exists but target shows fallback text
- This is expected when using `BindingError/DataValidationError` with fallback values.

3. `UpdateSource()` seems ineffective
- Check binding mode and trigger; explicit update only applies to `TwoWay` / `OneWayToSource` scenarios.

4. Dynamic binding behaves inconsistently across targets
- Confirm `InstancedBinding.Mode`, `Priority`, and target property metadata default binding mode.

5. Indexer-descriptor syntax is hard to follow
- Prefer explicit `Bind(...)` or XAML binding unless dynamic property selection is a hard requirement.
