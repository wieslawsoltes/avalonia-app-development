# Performance and AOT Checklist

## Startup

- Keep `BuildAvaloniaApp()` minimal and deterministic.
- Avoid heavy sync I/O in startup path.
- Preload only resources needed at first screen.

## Binding and Data Flow

- Prefer compiled bindings with `x:DataType`.
- Avoid reflection binding in hot visual trees.
- Avoid unnecessary `TwoWay` bindings; use `OneWay` where possible.

## Rendering

- Keep platform rendering fallback arrays explicit and safe.
- For Skia, tune `SkiaOptions.MaxGpuResourceSizeBytes` only with profiling evidence.
- Do not enable expensive rendering options globally without measurement.

## Visual Tree and Layout

- Keep deeply nested layout trees under control.
- Reuse templates/styles instead of one-off visual definitions.
- Avoid excessive invalidation loops caused by frequent property churn.

## Reactive and Async

- Compute off-thread, apply small UI deltas on UI thread.
- Throttle/debounce high-frequency streams before UI binding.
- Dispose subscriptions predictably with view/lifetime boundaries.

## Resources and Themes

- Centralize repeated brushes/metrics in resources.
- Use theme dictionaries instead of runtime branching in controls.
- Avoid loading large resource dictionaries at startup if not needed.

## AOT/Trim Compatibility

- Keep runtime dynamic loading to explicit opt-in paths.
- Scan for `RequiresUnreferencedCode` / `RequiresDynamicCode` call sites.
- Replace dynamic APIs with static/compiled alternatives when feasible.

## Release Validation

- Test desktop/browser/mobile targets that are actually shipped.
- Validate publish artifacts with representative data volume.
- Verify startup time, first interaction latency, and steady-state responsiveness.

## XAML-First and Code-Only Usage

Default mode:
- Prefer XAML-first for templates/styles/bindings because it is easier to profile and reason about.
- Use code-only visual tree creation only when requested.

XAML-first references:
- `x:DataType` compiled bindings
- `DataTemplate` reuse and resource dictionaries

XAML-first usage example:

```xml
<ListBox ItemsSource="{CompiledBinding Rows}">
  <ListBox.ItemTemplate>
    <DataTemplate x:DataType="vm:RowViewModel">
      <TextBlock Text="{CompiledBinding Title}" />
    </DataTemplate>
  </ListBox.ItemTemplate>
</ListBox>
```

Code-only alternative (on request):

```csharp
listBox.ItemTemplate = new FuncDataTemplate<RowViewModel>((row, _) =>
    new TextBlock { Text = row.Title },
    supportsRecycling: true);
```
