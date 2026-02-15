# Reactive Patterns and UI Threading

## Objective

Keep state propagation reactive while guaranteeing UI-thread correctness.

## UI Thread Contract

All visual tree and control property updates must run on `Dispatcher.UIThread`.

Primary APIs:
- `Dispatcher.UIThread`
- `Invoke(...)`
- `InvokeAsync(...)`
- `Post(...)`

Use:
- `Post` for non-blocking UI notifications.
- `InvokeAsync` when caller must await completion.
- `Invoke` only for short synchronous operations.

## Dispatcher Operation Lifecycle

`InvokeAsync(...)` returns `DispatcherOperation` / `DispatcherOperation<T>`.

High-value APIs:
- `Status` (`Pending`, `Executing`, `Completed`, `Aborted`)
- `Priority` (can be adjusted while queued)
- `Abort()`
- `GetTask()` / `GetAwaiter()`
- `Completed` / `Aborted` events
- `Wait()` (use with care; avoid blocking UI thread)

Pattern:

```csharp
var op = Dispatcher.UIThread.InvokeAsync(
    () => ApplyUiDelta(snapshot),
    DispatcherPriority.Background);

if (cancellationToken.IsCancellationRequested)
    op.Abort();

await op.GetTask();
```

Guideline:
- Prefer `await op.GetTask()` over `Wait()` in async code paths.
- Treat `Wait()` as a narrow escape hatch for synchronous boundaries.

## Priority Strategy

Useful priorities in app code:
- `Send`: immediate synchronous work (already on UI thread).
- `Normal` / `Default`: most UI updates.
- `Input`: input-adjacent work.
- `Render` / `Loaded`: render/layout-adjacent work.
- `Background` / `ContextIdle` / `ApplicationIdle`: non-urgent UI updates.

Keep priority choices stable and intentional. Escalating everything to high priority causes responsiveness regressions.

## Await With Priority

`Dispatcher.UIThread.AwaitWithPriority(...)` lets you continue on the dispatcher with explicit priority after a task completes.

```csharp
await Dispatcher.UIThread.AwaitWithPriority(loadTask, DispatcherPriority.Background);
// Continuation is now queued on UI dispatcher at Background priority.
UpdateUiFromLoadedData();
```

Use this when you need deterministic continuation priority instead of default scheduler behavior.

## DispatcherTimer Patterns

For scheduled UI work:
- periodic: `DispatcherTimer.Run(...)`
- one-shot: `DispatcherTimer.RunOnce(...)`
- imperative control: `Start()`, `Stop()`, `Interval`, `IsEnabled`, `Tick`

```csharp
IDisposable heartbeat = DispatcherTimer.Run(
    action: () =>
    {
        UpdateClockText();
        return !viewModel.IsDisposed;
    },
    interval: TimeSpan.FromSeconds(1),
    priority: DispatcherPriority.Background);
```

Dispose returned timer handles during teardown to avoid stale callbacks.

## Dispatcher Exception Pipeline

Dispatcher exposes exception hooks for invoked delegates:
- `UnhandledExceptionFilter`
- `UnhandledException`

Use them as a final safety net and telemetry path, not as normal control flow.
- keep handlers lightweight,
- avoid allocations/heavy work in the handler itself,
- mark handled only when recovery is explicit and safe.

## Reactive Property Pipelines

Useful entry points:
- `AvaloniaObjectExtensions.GetObservable(...)`
- `GetBindingObservable(...)`
- `GetPropertyChangedObservable(...)`
- `ToBinding()`

Example: bind observable stream to UI property

```csharp
IDisposable subscription = textBlock.Bind(
    TextBlock.TextProperty,
    viewModel.StatusObservable);
```

Example: observe property changes

```csharp
IDisposable subscription = textBox
    .GetObservable(TextBox.TextProperty)
    .Subscribe(value =>
    {
        // Transform/validate or dispatch commands.
    });
```

## Command and Input Flow

Command/input APIs:
- `ICommandSource`
- `KeyGesture`
- `KeyBinding`
- `HotkeyManager`

Routing APIs:
- `RoutedEvent`
- `RoutedEventArgs`
- `Interactive.AddHandler(...)`

Use:
- Keep command logic in viewmodel/services.
- Keep routed events for cross-cutting UI behavior, not business logic.

## Thread-Safe Async Pattern

```csharp
public async Task RefreshAsync()
{
    IsBusy = true;
    try
    {
        var dto = await _api.GetDataAsync();

        await Dispatcher.UIThread.InvokeAsync(() =>
        {
            Items.Clear();
            foreach (var item in dto.Items)
                Items.Add(item);
        });
    }
    finally
    {
        IsBusy = false;
    }
}
```

## Avoiding Reactive Pitfalls

1. Updating control properties from background threads.
- Fix: marshal to `Dispatcher.UIThread`.

2. Manual event subscriptions without deterministic disposal.
- Fix: keep and dispose subscriptions with view/lifetime ownership.

3. Coupling viewmodels directly to concrete control instances.
- Fix: expose state/commands only; let bindings wire controls.

4. Using heavy sync work inside `Dispatcher.Invoke`.
- Fix: compute off-thread, then apply minimal UI delta on UI thread.

## Practical Disposal Guidance

- Keep per-view subscriptions in a disposable container owned by that view.
- Dispose during view teardown/unload transitions.
- Avoid static/global subscriptions unless truly app-scoped.

## XAML-First and Code-Only Usage

Default mode:
- Express reactive UI updates through XAML bindings first.
- Use code-only binding/wiring only when requested.

XAML-first references:
- `x:DataType`, `{CompiledBinding ...}`, control property bindings

XAML-first usage example:

```xml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:Class="MyApp.Views.StatusView"
             x:DataType="vm:StatusViewModel">
  <StackPanel Spacing="8">
    <TextBlock Text="{CompiledBinding StatusText}" />
    <ProgressBar IsIndeterminate="{CompiledBinding IsBusy}" />
  </StackPanel>
</UserControl>
```

Code-only alternative (on request):

```csharp
textBlock.Bind(TextBlock.TextProperty, viewModel.StatusObservable);
progressBar.Bind(ProgressBar.IsIndeterminateProperty, viewModel.IsBusyObservable);
```
