# XAML and C# Cross-Platform Development (for Avalonia) Compendium

Use this as the entry page for the full skill reference set.

## Table of Contents

00. API map: `00-api-map.md`
01. Architecture and lifetimes: `01-architecture-and-lifetimes.md`
02. Bindings, XAML, AOT: `02-bindings-xaml-aot.md`
03. Reactive + threading: `03-reactive-threading.md`
04. Styles/themes/resources: `04-styles-themes-resources.md`
05. Platform bootstrap: `05-platforms-and-bootstrap.md`
06. MSBuild and AOT tooling: `06-msbuild-aot-and-tooling.md`
07. Troubleshooting: `07-troubleshooting.md`
08. Performance checklist: `08-performance-checklist.md`
09. End-to-end examples: `09-end-to-end-examples.md`
10. Templated controls + control themes: `10-templated-controls-and-control-themes.md`
11. View locator + tree patterns: `11-user-views-locator-and-tree-patterns.md`
12. Animations, transitions, frame loops: `12-animations-transitions-and-frame-loops.md`
13. Windowing + custom decorations: `13-windowing-and-custom-decorations.md`
14. Custom drawing, text, shapes, Skia: `14-custom-drawing-text-shapes-and-skia.md`
15. Compositor + compositor animations: `15-compositor-and-custom-visuals.md`
16. Property system + attached behaviors + style/media queries: `16-property-system-attached-properties-behaviors-and-style-properties.md`
17. Resources, assets, theme variants, xmlns: `17-resources-assets-theme-variants-and-xmlns.md`
18. Input system + routed events: `18-input-system-and-routed-events.md`
19. Focus + keyboard navigation: `19-focus-and-keyboard-navigation.md`
20. ItemsControl virtualization + recycling: `20-itemscontrol-virtualization-and-recycling.md`
21. Custom layout authoring: `21-custom-layout-authoring.md`
22. Validation pipeline + data errors: `22-validation-pipeline-and-data-errors.md`
23. Accessibility + automation: `23-accessibility-and-automation.md`
24. Commands + hotkeys + gestures: `24-commands-hotkeys-and-gestures.md`
25. Popups/flyouts/tooltips + overlays: `25-popups-flyouts-tooltips-and-overlays.md`
26. Testing stack (headless/render/UI): `26-testing-stack-headless-render-and-ui-tests.md`
27. Diagnostics/profiling + devtools: `27-diagnostics-profiling-and-devtools.md`
28. Custom themes (XAML + code-only): `28-custom-themes-xaml-and-code-only.md`
29. Storage provider + file pickers: `29-storage-provider-and-file-pickers.md`
30. Layout measure/arrange + custom controls/panels: `30-layout-measure-arrange-and-custom-layout-controls.md`
31. Clipboard + data transfer: `31-clipboard-and-data-transfer.md`
32. Launcher + external open: `32-launcher-and-external-open.md`
33. Screens + display awareness: `33-screens-and-display-awareness.md`
34. DragDrop workflows: `34-dragdrop-workflows.md`
35. Path icons + vector geometry assets: `35-path-icons-and-vector-geometry-assets.md`
36. Adorners, focus visuals, overlay layers: `36-adorners-focus-and-overlay-layers.md`
37. Shapes, geometry, hit testing: `37-shapes-geometry-and-hit-testing.md`
38. Data templates + IDataTemplate selector patterns: `38-data-templates-and-idatatemplate-selector-patterns.md`
39. Visual tree inspection + traversal: `39-visual-tree-inspection-and-traversal.md`
40. Logical tree inspection + traversal: `40-logical-tree-inspection-and-traversal.md`
41. XAML compiler and build pipeline: `41-xaml-compiler-and-build-pipeline.md`
42. Runtime XAML loader and dynamic loading: `42-runtime-xaml-loader-and-dynamic-loading.md`
43. XAML in libraries and resource packaging: `43-xaml-in-libraries-and-resource-packaging.md`
44. Runtime XAML manipulation and service-provider patterns: `44-runtime-xaml-manipulation-and-service-provider-patterns.md`
45. Value converters: `45-value-converters-single-multi-and-binding-wiring.md`
46. Binding value/notification and instanced binding semantics: `46-binding-value-notification-and-instanced-binding-semantics.md`
47. Dispatcher priority, operations, and timers: `47-dispatcher-priority-operations-and-timers.md`
48. TopLevel, window, and runtime services: `48-toplevel-window-and-runtime-services.md`
49. Adaptive markup and dynamic resource patterns: `49-adaptive-markup-and-dynamic-resource-patterns.md`
50. Relative/static resource and name resolution markup: `50-relative-static-resource-and-name-resolution-markup.md`
51. Template content and func template patterns: `51-template-content-and-func-template-patterns.md`
52. Controls reference catalog: `52-controls-reference-catalog.md`
API index: `api-index-generated.md`

## Fast Navigation by Task

- Startup/lifetime wiring:
  - `01-architecture-and-lifetimes.md`
  - `05-platforms-and-bootstrap.md`
  - `48-toplevel-window-and-runtime-services.md`
  - `29-storage-provider-and-file-pickers.md`

- Platform services and external integration:
  - `48-toplevel-window-and-runtime-services.md`
  - `29-storage-provider-and-file-pickers.md`
  - `31-clipboard-and-data-transfer.md`
  - `32-launcher-and-external-open.md`
  - `33-screens-and-display-awareness.md`
  - `34-dragdrop-workflows.md`

- XAML compiler, runtime loader, and manipulation:
  - `41-xaml-compiler-and-build-pipeline.md`
  - `42-runtime-xaml-loader-and-dynamic-loading.md`
  - `43-xaml-in-libraries-and-resource-packaging.md`
  - `44-runtime-xaml-manipulation-and-service-provider-patterns.md`
  - `49-adaptive-markup-and-dynamic-resource-patterns.md`
  - `50-relative-static-resource-and-name-resolution-markup.md`

- Binding correctness and AOT safety:
  - `02-bindings-xaml-aot.md`
  - `45-value-converters-single-multi-and-binding-wiring.md`
  - `46-binding-value-notification-and-instanced-binding-semantics.md`
  - `50-relative-static-resource-and-name-resolution-markup.md`
  - `06-msbuild-aot-and-tooling.md`
  - `41-xaml-compiler-and-build-pipeline.md`
  - `42-runtime-xaml-loader-and-dynamic-loading.md`
  - `44-runtime-xaml-manipulation-and-service-provider-patterns.md`
  - `38-data-templates-and-idatatemplate-selector-patterns.md`

- Reactive UI correctness:
  - `03-reactive-threading.md`
  - `47-dispatcher-priority-operations-and-timers.md`

- Theme/style consistency:
  - `04-styles-themes-resources.md`
  - `10-templated-controls-and-control-themes.md`
  - `16-property-system-attached-properties-behaviors-and-style-properties.md`
  - `17-resources-assets-theme-variants-and-xmlns.md`
  - `49-adaptive-markup-and-dynamic-resource-patterns.md`
  - `43-xaml-in-libraries-and-resource-packaging.md`
  - `28-custom-themes-xaml-and-code-only.md`

- View composition and lookup patterns:
  - `11-user-views-locator-and-tree-patterns.md`
  - `38-data-templates-and-idatatemplate-selector-patterns.md`
  - `51-template-content-and-func-template-patterns.md`
  - `39-visual-tree-inspection-and-traversal.md`
  - `40-logical-tree-inspection-and-traversal.md`

- Input, focus, and interaction routing:
  - `18-input-system-and-routed-events.md`
  - `19-focus-and-keyboard-navigation.md`
  - `24-commands-hotkeys-and-gestures.md`
  - `34-dragdrop-workflows.md`
  - `36-adorners-focus-and-overlay-layers.md`
  - `39-visual-tree-inspection-and-traversal.md`

- Large-data item controls:
  - `30-layout-measure-arrange-and-custom-layout-controls.md`
  - `20-itemscontrol-virtualization-and-recycling.md`
  - `21-custom-layout-authoring.md`
  - `38-data-templates-and-idatatemplate-selector-patterns.md`
  - `51-template-content-and-func-template-patterns.md`

- Validation and accessibility:
  - `22-validation-pipeline-and-data-errors.md`
  - `23-accessibility-and-automation.md`

- Animation and rendering loops:
  - `12-animations-transitions-and-frame-loops.md`
  - `15-compositor-and-custom-visuals.md`

- Windowing and custom chrome:
  - `13-windowing-and-custom-decorations.md`
  - `48-toplevel-window-and-runtime-services.md`
  - `25-popups-flyouts-tooltips-and-overlays.md`
  - `52-controls-reference-catalog.md`

- Drawing and graphics:
  - `14-custom-drawing-text-shapes-and-skia.md`
  - `35-path-icons-and-vector-geometry-assets.md`
  - `37-shapes-geometry-and-hit-testing.md`

- Testing and diagnostics:
  - `26-testing-stack-headless-render-and-ui-tests.md`
  - `27-diagnostics-profiling-and-devtools.md`

- Production hardening:
  - `07-troubleshooting.md`
  - `08-performance-checklist.md`

- API lookup by file/signature:
  - `api-index-generated.md`
