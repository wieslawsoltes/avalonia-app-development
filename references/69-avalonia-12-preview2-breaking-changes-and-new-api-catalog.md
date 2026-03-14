# Avalonia Migration Report (Generated)

- Generated at (UTC): `2026-03-14 18:39:20Z`
- Repository: `/Users/wieslawsoltes/GitHub/Avalonia`
- From ref: `11.3.12`
- To ref: `12.0.0-preview2`

## Coverage Contract

- Breaking changes come from Avalonia's checked-in package-validation suppression files under `api/*.xml`.
- Added public APIs come from a source-level scan of public signatures under `src/**/*.cs`.
- Removed public signatures are included as an auxiliary parser-based view; treat the suppression-backed section as the official breaking-change list for shipped packages.

## Breaking Change Summary

Official breaking-change source: Avalonia `api/*.xml` package-validation suppressions.

- Unique approved compatibility suppressions: `536`

### By Package

- `Avalonia`: `499`
- `Avalonia.Android`: `6`
- `Avalonia.Headless`: `3`
- `Avalonia.Headless.XUnit`: `6`
- `Avalonia.LinuxFramebuffer`: `3`
- `Avalonia.Skia`: `15`
- `Avalonia.Win32.Interoperability`: `2`
- `Avalonia.X11`: `2`

### By Diagnostic

- `CP0001` (missing public type): `102`
- `CP0002` (missing public member): `303`
- `CP0003` (other compatibility change): `1`
- `CP0005` (other compatibility change): `4`
- `CP0006` (new interface member without default implementation): `59`
- `CP0007` (removed base type): `5`
- `CP0008` (removed base interface): `43`
- `CP0009` (type became sealed): `13`
- `CP0012` (member lost virtual/abstract): `6`

## Breaking Changes: `Avalonia`

### `CP0001`: missing public type

- `Avalonia.Animation.CustomAnimatorBase` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Animation.CustomAnimatorBase`1` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Animation.Easings.CubicBezierEasing` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Controls.ApplicationLifetimes.ClassicDesktopStyleApplicationLifetimeOptions` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.ApplicationLifetimes.IActivatableApplicationLifetime` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.AutoCompleteBox.BindingEvaluator`1` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Chrome.CaptionButtons` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Chrome.TitleBar` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.ContextRequestedEventArgs` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Diagnostics.IPopupHostProvider` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.FileDialog` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.FileDialogFilter` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.FileSystemDialog` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Generators.TreeContainerIndex` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Generators.TreeItemContainerGenerator` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.NativeMenuItemToggleType` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.OpenFileDialog` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.OpenFolderDialog` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Platform.ISystemDialogImpl` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Platform.ManagedDispatcherImpl` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Platform.Surfaces.FramebufferLockProperties` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Platform.Surfaces.FuncFramebufferRenderTarget` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Platform.Surfaces.IFramebufferPlatformSurface` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Platform.Surfaces.IFramebufferRenderTarget` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Platform.Surfaces.IFramebufferRenderTargetWithProperties` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.ChromeOverlayLayer` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.IPopupHost` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.IScrollable` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Controls.Primitives.LightDismissOverlayLayer` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.OverlayLayer` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.PseudolassesExtensions` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Controls.Remote.RemoteServer` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Remote.RemoteWidget` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.SaveFileDialog` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.SystemDecorations` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.SystemDialog` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Data.BindingBase` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Markup.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Markup.dll`)
- `Avalonia.Data.Core.CastTypePropertyPathElement` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Data.Core.ChildTraversalPropertyPathElement` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Data.Core.EnsureTypePropertyPathElement` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Data.Core.IPropertyPathElement` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Data.Core.Plugins.BindingPlugins` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Data.Core.Plugins.DataValidationBase` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Data.Core.Plugins.ExceptionValidationPlugin` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Data.Core.Plugins.IDataValidationPlugin` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Data.Core.Plugins.IPropertyAccessorPlugin` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Data.Core.Plugins.IStreamPlugin` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Data.Core.Plugins.IndeiValidationPlugin` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Data.Core.Plugins.PropertyAccessorBase` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Data.Core.Plugins.PropertyError` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Data.Core.PropertyPath` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Data.Core.PropertyPathBuilder` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Data.Core.PropertyPropertyPathElement` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Data.IBinding` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Data.InstancedBinding` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Data.RelativeSourceMode` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Markup.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Markup.dll`)
- `Avalonia.Data.TreeType` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Markup.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Markup.dll`)
- `Avalonia.Diagnostics.AppliedStyle` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Diagnostics.StyleDiagnostics` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Diagnostics.StyledElementExtensions` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.DataObjectExtensions` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.Gestures` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.IDataObject` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.IKeyboardNavigationHandler` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.KeyboardNavigationHandler` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.TextInput.ITextInputMethodRoot` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Layout.IEmbeddedLayoutRoot` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Layout.ILayoutRoot` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Layout.LayoutManager` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Markup.Xaml.ConstructorArgumentAttribute` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Markup.Xaml.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Markup.Xaml.dll`)
- `Avalonia.Markup.Xaml.MarkupExtensions.CompiledBindings.CompiledBindingPath` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll`)
- `Avalonia.Markup.Xaml.MarkupExtensions.CompiledBindings.CompiledBindingPathBuilder` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll`)
- `Avalonia.Media.Fonts.FontFamilyLoader` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.IGlyphTypeface` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.OpenGL.Surfaces.IGlPlatformSurfaceRenderTarget2` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.OpenGL.Surfaces.IGlPlatformSurfaceRenderTargetWithCorruptionInfo` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.Platform.ExtendClientAreaChromeHints` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.IApplicationPlatformEvents` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.IGeometryContext2` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IOptionalFeatureProvider` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IReadableBitmapWithAlphaImpl` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IRenderTarget2` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IRenderTargetWithProperties` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.OptionalFeatureProviderExtensions` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Rendering.IHitTester` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Rendering.IRenderRoot` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Rendering.IRenderer` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Styling.IStyleable` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Utilities.CharacterReader` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Utilities.IdentifierParser` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Utilities.KeywordParser` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Utilities.MathUtilities` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Utilities.StringTokenizer` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Utilities.StyleClassParser` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.VisualTree.IHostedVisualTreeRoot` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)

### `CP0002`: missing public member

- `Avalonia.Controls.ContextMenu.PlacementModeProperty` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Control.ContextRequestedEvent` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Documents.Inline.TextDecorationsProperty` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.ItemsControl.DisplayMemberBindingProperty` (field; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.NativeMenuBar.EnableMenuItemClickForwardingProperty` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.NativeMenuItem.ToggleTypeProperty` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.Popup.PlacementModeProperty` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.SelectingItemsControl.SelectedValueBindingProperty` (field; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.TextSearch.TextBindingProperty` (field; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.ToggleButton.CheckedEvent` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.ToggleButton.IndeterminateEvent` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.ToggleButton.UncheckedEvent` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.VisualLayerManager.ChromeOverlayLayerProperty` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.ResourcesChangedEventArgs.Empty` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Controls.TextBlock.LetterSpacingProperty` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.TextBox.LetterSpacingProperty` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.TopLevel.PointerOverElementProperty` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Window.ExtendClientAreaChromeHintsProperty` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Window.SystemDecorationsProperty` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Data.BindingPriority.TemplatedParent` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.DataFormats.FileNames` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.DataFormats.Files` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.DataFormats.Text` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.HoldingState.Cancelled` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.DrawingImage.ViewboxProperty` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.Fonts.FontCollectionBase._glyphTypefaceCache` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.RadialGradientBrush.RadiusProperty` (field; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Animation.Animation.SetAnimator(Avalonia.Animation.IAnimationSetter,Avalonia.Animation.CustomAnimatorBase)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.AppBuilder.get_LifetimeOverride` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Application.add_UrlsOpened(System.EventHandler{Avalonia.UrlOpenedEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Application.remove_UrlsOpened(System.EventHandler{Avalonia.UrlOpenedEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Automation.Peers.AutomationPeer.GetVisualRootCore` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.AvaloniaObject.Bind(Avalonia.AvaloniaProperty,Avalonia.Data.IBinding)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.AvaloniaObject.get_Item(Avalonia.Data.IndexerDescriptor)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.AvaloniaObjectExtensions.Bind(Avalonia.AvaloniaObject,Avalonia.AvaloniaProperty,Avalonia.Data.BindingBase,System.Object)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.AvaloniaObjectExtensions.Bind(Avalonia.AvaloniaObject,Avalonia.AvaloniaProperty,Avalonia.Data.IBinding,System.Object)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.AvaloniaObjectExtensions.ToBinding``1(System.IObservable{``0})` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Controls.AutoCompleteBox.get_ValueMemberBinding` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.ContextMenu.get_PlacementMode` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.ContextMenu.set_PlacementMode(Avalonia.Controls.PlacementMode)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Design.CreatePreviewWithControl(System.Object)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Design.GetDataContext(Avalonia.Controls.Templates.IDataTemplate)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Design.GetPreviewWith(Avalonia.Controls.Templates.IDataTemplate)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Design.GetPreviewWith(Avalonia.Styling.IStyle)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Design.SetDataContext(Avalonia.Controls.Templates.IDataTemplate,System.Object)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Design.SetPreviewWith(Avalonia.AvaloniaObject,Avalonia.Controls.Control)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Design.SetPreviewWith(Avalonia.AvaloniaObject,Avalonia.Controls.ITemplate{Avalonia.Controls.Control})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Design.SetPreviewWith(Avalonia.Controls.ResourceDictionary,Avalonia.Controls.ITemplate{Avalonia.Controls.Control})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Design.SetPreviewWith(Avalonia.Controls.Templates.IDataTemplate,Avalonia.Controls.Control)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Design.SetPreviewWith(Avalonia.Controls.Templates.IDataTemplate,Avalonia.Controls.ITemplate{Avalonia.Controls.Control})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Design.SetPreviewWith(Avalonia.Styling.IStyle,Avalonia.Controls.Control)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Design.SetPreviewWith(Avalonia.Styling.IStyle,Avalonia.Controls.ITemplate{Avalonia.Controls.Control})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Embedding.Offscreen.OffscreenTopLevelImplBase.get_Surfaces` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Generators.ItemContainerGenerator.ContainerFromIndex(System.Int32)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Generators.ItemContainerGenerator.IndexFromContainer(Avalonia.Controls.Control)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.ItemsControl.ItemsControlFromItemContaner(Avalonia.Controls.Control)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.ItemsControl.get_DisplayMemberBinding` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.NativeMenuBar.SetEnableMenuItemClickForwarding(Avalonia.Controls.MenuItem,System.Boolean)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.NativeMenuItem.get_ToggleType` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Platform.IInsetsManager.get_DisplayEdgeToEdge` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Platform.IInsetsManager.set_DisplayEdgeToEdge(System.Boolean)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Platform.InsetsManagerBase.get_DisplayEdgeToEdge` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Platform.InsetsManagerBase.set_DisplayEdgeToEdge(System.Boolean)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.AccessText.get_AccessKey` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.AdornerLayer.#ctor` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.OverlayLayer.#ctor` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.OverlayPopupHost.#ctor(Avalonia.Controls.Primitives.OverlayLayer)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.OverlayPopupHost.ConfigurePosition(Avalonia.Visual,Avalonia.Controls.PlacementMode,Avalonia.Point,Avalonia.Controls.Primitives.PopupPositioning.PopupAnchor,Avalonia.Controls.Primitives.PopupPositioning.PopupGravity,Avalonia.Controls.Primitives.PopupPositioning.PopupPositionerConstraintAdjustment,System.Nullable{Avalonia.Rect})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.OverlayPopupHost.CreatePopupHost(Avalonia.Visual,Avalonia.IAvaloniaDependencyResolver)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.OverlayPopupHost.CreatePopupHost(Avalonia.Visual,Avalonia.IAvaloniaDependencyResolver,System.Boolean)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.OverlayPopupHost.SetChild(Avalonia.Controls.Control)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.OverlayPopupHost.TakeFocus` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.Popup.get_Host` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.Popup.get_PlacementMode` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.Popup.set_PlacementMode(Avalonia.Controls.PlacementMode)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.PopupRoot.ConfigurePosition(Avalonia.Visual,Avalonia.Controls.PlacementMode,Avalonia.Point,Avalonia.Controls.Primitives.PopupPositioning.PopupAnchor,Avalonia.Controls.Primitives.PopupPositioning.PopupGravity,Avalonia.Controls.Primitives.PopupPositioning.PopupPositionerConstraintAdjustment,System.Nullable{Avalonia.Rect})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.SelectingItemsControl.get_SelectedValueBinding` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.TextSearch.GetText(Avalonia.Controls.Control)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.TextSearch.GetTextBinding(Avalonia.Interactivity.Interactive)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.TextSearch.SetText(Avalonia.Controls.Control,System.String)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.TextSearch.SetTextBinding(Avalonia.Interactivity.Interactive,Avalonia.Data.IBinding)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.ToggleButton.OnChecked(Avalonia.Interactivity.RoutedEventArgs)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.ToggleButton.OnIndeterminate(Avalonia.Interactivity.RoutedEventArgs)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.ToggleButton.OnUnchecked(Avalonia.Interactivity.RoutedEventArgs)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.ToggleButton.add_Checked(System.EventHandler{Avalonia.Interactivity.RoutedEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.ToggleButton.add_Indeterminate(System.EventHandler{Avalonia.Interactivity.RoutedEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.ToggleButton.add_Unchecked(System.EventHandler{Avalonia.Interactivity.RoutedEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.ToggleButton.remove_Checked(System.EventHandler{Avalonia.Interactivity.RoutedEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.ToggleButton.remove_Indeterminate(System.EventHandler{Avalonia.Interactivity.RoutedEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.ToggleButton.remove_Unchecked(System.EventHandler{Avalonia.Interactivity.RoutedEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.VisualLayerManager.get_AdornerLayer` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.VisualLayerManager.get_ChromeOverlayLayer` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.VisualLayerManager.get_LightDismissOverlayLayer` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.VisualLayerManager.get_OverlayLayer` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.VisualLayerManager.get_TextSelectorLayer` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.ResourcesChangedEventArgs.#ctor` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Controls.Screens.ScreenFromWindow(Avalonia.Platform.IWindowBaseImpl)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.TabItem.SubscribeToOwnerProperties(Avalonia.AvaloniaObject)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Templates.FuncTreeDataTemplate.ItemsSelector(System.Object)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Templates.ITreeDataTemplate.ItemsSelector(System.Object)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.TopLevel.#ctor(Avalonia.Platform.ITopLevelImpl,Avalonia.IAvaloniaDependencyResolver)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.TopLevel.StartRendering` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.TopLevel.StopRendering` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.TopLevel.get_PlatformSettings` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.TreeView.get_ItemContainerGenerator` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Window.SortWindowsByZOrder(Avalonia.Controls.Window[])` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Window.get_ExtendClientAreaChromeHints` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Window.get_SystemDecorations` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Window.set_ExtendClientAreaChromeHints(Avalonia.Platform.ExtendClientAreaChromeHints)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.WindowBase.ArrangeSetBounds(Avalonia.Size)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Data.Binding.#ctor(System.String,Avalonia.Data.BindingMode)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Markup.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Markup.dll`)
- `Avalonia.Data.BindingOperations.Apply(Avalonia.AvaloniaObject,Avalonia.AvaloniaProperty,Avalonia.Data.InstancedBinding)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Data.BindingOperations.Apply(Avalonia.AvaloniaObject,Avalonia.AvaloniaProperty,Avalonia.Data.InstancedBinding,System.Object)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Data.CompiledBindingPathBuilder.SetRawSource(System.Object)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Data.CompiledBindingPathBuilder.StreamObservable` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Data.CompiledBindingPathBuilder.StreamTask` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Data.CompiledBindingPathBuilder.TypeCast(System.Type)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Data.MultiBinding.Initiate(Avalonia.AvaloniaObject,Avalonia.AvaloniaProperty,System.Object,System.Boolean)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Markup.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Markup.dll`)
- `Avalonia.Data.MultiBinding.get_Bindings` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Markup.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Markup.dll`)
- `Avalonia.Data.ReflectionBinding.#ctor(System.String,Avalonia.Data.BindingMode)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Data.TemplateBinding.Initiate(Avalonia.AvaloniaObject,Avalonia.AvaloniaProperty,System.Object,System.Boolean)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Data.TemplateBinding.ProvideValue` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Data.TemplateBinding.Subscribe(System.IObserver{System.Object})` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Dialogs.Internal.ManagedFileChooserFilterViewModel.#ctor(Avalonia.Platform.Storage.FilePickerFileType)` (method/member; baseline `baseline/Avalonia/lib/net6.0/Avalonia.Dialogs.dll` -> current `current/Avalonia/lib/net6.0/Avalonia.Dialogs.dll`)
- `Avalonia.Dialogs.ManagedFileDialogExtensions.ShowManagedAsync(Avalonia.Controls.OpenFileDialog,Avalonia.Controls.Window,Avalonia.Dialogs.ManagedFileDialogOptions)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Dialogs.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Dialogs.dll`)
- `Avalonia.Dialogs.ManagedFileDialogExtensions.ShowManagedAsync``1(Avalonia.Controls.OpenFileDialog,Avalonia.Controls.Window,Avalonia.Dialogs.ManagedFileDialogOptions)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Dialogs.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Dialogs.dll`)
- `Avalonia.Input.DataObject.Contains(System.String)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.DataObject.Get(System.String)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.DataObject.GetDataFormats` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.DataObject.Set(System.String,System.Object)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.DragDrop.DoDragDrop(Avalonia.Input.PointerEventArgs,Avalonia.Input.IDataObject,Avalonia.Input.DragDropEffects)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.DragEventArgs.#ctor(Avalonia.Interactivity.RoutedEvent{Avalonia.Input.DragEventArgs},Avalonia.Input.IDataObject,Avalonia.Interactivity.Interactive,Avalonia.Point,Avalonia.Input.KeyModifiers)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.DragEventArgs.get_Data` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.HoldingRoutedEventArgs.#ctor(Avalonia.Input.HoldingState,Avalonia.Point,Avalonia.Input.PointerType)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.IInputRoot.get_KeyboardNavigationHandler` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.IInputRoot.get_PlatformSettings` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.IInputRoot.get_PointerOverElement` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.IInputRoot.get_ShowAccessKeys` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.IInputRoot.set_PointerOverElement(Avalonia.Input.IInputElement)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.IInputRoot.set_ShowAccessKeys(System.Boolean)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.IKeyboardNavigationHandler.Move(Avalonia.Input.IInputElement,Avalonia.Input.NavigationDirection,Avalonia.Input.KeyModifiers)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.AddPinchEndedHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.PinchEndedEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.AddPinchHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.PinchEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.AddPointerTouchPadGestureMagnifyHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.PointerDeltaEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.AddPointerTouchPadGestureRotateHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.PointerDeltaEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.AddPointerTouchPadGestureSwipeHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.PointerDeltaEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.AddPullGestureEndedHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.PullGestureEndedEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.AddPullGestureHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.PullGestureEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.AddScrollGestureEndedHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.ScrollGestureEndedEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.AddScrollGestureHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.ScrollGestureEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.AddScrollGestureInertiaStartingHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.ScrollGestureInertiaStartingEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.RemovePinchEndedHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.PinchEndedEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.RemovePinchHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.PinchEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.RemovePointerTouchPadGestureMagnifyHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.PointerDeltaEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.RemovePointerTouchPadGestureRotateHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.PointerDeltaEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.RemovePointerTouchPadGestureSwipeHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.PointerDeltaEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.RemovePullGestureEndedHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.PullGestureEndedEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.RemovePullGestureHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.PullGestureEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.RemoveScrollGestureEndedHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.ScrollGestureEndedEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.RemoveScrollGestureHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.ScrollGestureEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.InputElement.RemoveScrollGestureInertiaStartingHandler(Avalonia.Interactivity.Interactive,System.EventHandler{Avalonia.Input.ScrollGestureInertiaStartingEventArgs})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.KeyboardNavigationHandler.Move(Avalonia.Input.IInputElement,Avalonia.Input.NavigationDirection,Avalonia.Input.KeyModifiers)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.Platform.IClipboard.GetDataAsync(System.String)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.Platform.IClipboard.GetFormatsAsync` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.Platform.IClipboard.GetTextAsync` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.Platform.IClipboard.SetDataObjectAsync(Avalonia.Input.IDataObject)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.Platform.IClipboard.SetTextAsync(System.String)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.Platform.IClipboard.TryGetInProcessDataObjectAsync` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.Platform.IPlatformDragSource.DoDragDrop(Avalonia.Input.PointerEventArgs,Avalonia.Input.IDataObject,Avalonia.Input.DragDropEffects)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.Raw.RawDragEvent.#ctor(Avalonia.Input.Raw.IDragDropDevice,Avalonia.Input.Raw.RawDragEventType,Avalonia.Input.IInputRoot,Avalonia.Point,Avalonia.Input.IDataObject,Avalonia.Input.DragDropEffects,Avalonia.Input.RawInputModifiers)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.Raw.RawDragEvent.get_Data` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.Raw.RawKeyEventArgs.#ctor(Avalonia.Input.IInputDevice,System.UInt64,Avalonia.Input.IInputRoot,Avalonia.Input.Raw.RawKeyEventType,Avalonia.Input.Key,Avalonia.Input.RawInputModifiers,Avalonia.Input.PhysicalKey,Avalonia.Input.KeyDeviceType,System.String)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.Raw.RawKeyEventArgs.#ctor(Avalonia.Input.IInputDevice,System.UInt64,Avalonia.Input.IInputRoot,Avalonia.Input.Raw.RawKeyEventType,Avalonia.Input.Key,Avalonia.Input.RawInputModifiers,Avalonia.Input.PhysicalKey,System.String)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.Raw.RawKeyEventArgs.#ctor(Avalonia.Input.IKeyboardDevice,System.UInt64,Avalonia.Input.IInputRoot,Avalonia.Input.Raw.RawKeyEventType,Avalonia.Input.Key,Avalonia.Input.RawInputModifiers)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.TextInput.TextInputMethodClient.ShowInputPanel` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Layout.LayoutHelper.RoundLayoutSizeUp(Avalonia.Size,System.Double,System.Double)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Layout.LayoutHelper.RoundLayoutThickness(Avalonia.Thickness,System.Double,System.Double)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Markup.Xaml.MarkupExtensions.CompiledBindingExtension.#ctor(Avalonia.Markup.Xaml.MarkupExtensions.CompiledBindings.CompiledBindingPath)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll`)
- `Avalonia.Markup.Xaml.MarkupExtensions.CompiledBindingExtension.ProvideValue(System.IServiceProvider)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll`)
- `Avalonia.Markup.Xaml.MarkupExtensions.CompiledBindingExtension.get_Path` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll`)
- `Avalonia.Markup.Xaml.MarkupExtensions.DynamicResourceExtension.ProvideValue(System.IServiceProvider)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll`)
- `Avalonia.Markup.Xaml.MarkupExtensions.ReflectionBindingExtension.#ctor(System.String,Avalonia.Data.BindingMode)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Markup.Xaml.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Markup.Xaml.dll`)
- `Avalonia.Markup.Xaml.MarkupExtensions.ReflectionBindingExtension.ProvideValue(System.IServiceProvider)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll`)
- `Avalonia.Markup.Xaml.Templates.TreeDataTemplate.ItemsSelector(System.Object)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll`)
- `Avalonia.Markup.Xaml.XamlLoadException.#ctor(System.Runtime.Serialization.SerializationInfo,System.Runtime.Serialization.StreamingContext)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Markup.Xaml.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Markup.Xaml.dll`)
- `Avalonia.Media.Color.ToUint32` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.DrawingContext.PushPostTransform(Avalonia.Matrix)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.DrawingContext.PushPreTransform(Avalonia.Matrix)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.DrawingContext.PushTransformContainer` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.DrawingImage.get_Viewbox` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.DrawingImage.set_Viewbox(System.Nullable{Avalonia.Rect})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.FontManager.TryGetGlyphTypeface(Avalonia.Media.Typeface,Avalonia.Media.IGlyphTypeface@)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Media.FontMetrics.get_DesignEmHeight` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Media.Fonts.FontCollectionBase.Initialize(Avalonia.Platform.IFontManagerImpl)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.Fonts.FontCollectionBase.TryCreateSyntheticGlyphTypeface(Avalonia.Media.IGlyphTypeface,Avalonia.Media.FontStyle,Avalonia.Media.FontWeight,Avalonia.Media.FontStretch,Avalonia.Media.IGlyphTypeface@)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Media.Fonts.FontCollectionBase.TryGetGlyphTypeface(System.String,Avalonia.Media.FontStyle,Avalonia.Media.FontWeight,Avalonia.Media.FontStretch,Avalonia.Media.IGlyphTypeface@)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Media.Fonts.IFontCollection.Initialize(Avalonia.Platform.IFontManagerImpl)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.Fonts.IFontCollection.TryGetGlyphTypeface(System.String,Avalonia.Media.FontStyle,Avalonia.Media.FontWeight,Avalonia.Media.FontStretch,Avalonia.Media.IGlyphTypeface@)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Media.GlyphMetrics.get_Height` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Media.GlyphMetrics.get_Width` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Media.GlyphRun.#ctor(Avalonia.Media.IGlyphTypeface,System.Double,System.ReadOnlyMemory{System.Char},System.Collections.Generic.IReadOnlyList{Avalonia.Media.TextFormatting.GlyphInfo},System.Nullable{Avalonia.Point},System.Int32)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Media.GlyphRun.#ctor(Avalonia.Media.IGlyphTypeface,System.Double,System.ReadOnlyMemory{System.Char},System.Collections.Generic.IReadOnlyList{System.UInt16},System.Nullable{Avalonia.Point},System.Int32)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Media.GlyphRun.get_GlyphTypeface` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Media.IRadialGradientBrush.get_Radius` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.Imaging.Bitmap.CopyPixels(Avalonia.Platform.ILockedFramebuffer,Avalonia.Platform.AlphaFormat)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.Immutable.ImmutableRadialGradientBrush.get_Radius` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.RadialGradientBrush.get_Radius` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.RadialGradientBrush.set_Radius(System.Double)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.StreamGeometryContext.ArcTo(Avalonia.Point,Avalonia.Size,System.Double,System.Boolean,Avalonia.Media.SweepDirection)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.StreamGeometryContext.CubicBezierTo(Avalonia.Point,Avalonia.Point,Avalonia.Point)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.StreamGeometryContext.LineTo(Avalonia.Point)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.StreamGeometryContext.QuadraticBezierTo(Avalonia.Point,Avalonia.Point)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.TextFormatting.GenericTextRunProperties.#ctor(Avalonia.Media.Typeface,Avalonia.Media.FontFeatureCollection,System.Double,Avalonia.Media.TextDecorationCollection,Avalonia.Media.IBrush,Avalonia.Media.IBrush,Avalonia.Media.BaselineAlignment,System.Globalization.CultureInfo)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.TextFormatting.GenericTextRunProperties.#ctor(Avalonia.Media.Typeface,System.Double,Avalonia.Media.TextDecorationCollection,Avalonia.Media.IBrush,Avalonia.Media.IBrush,Avalonia.Media.BaselineAlignment,System.Globalization.CultureInfo)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.TextFormatting.ShapedBuffer.#ctor(System.ReadOnlyMemory{System.Char},System.Int32,Avalonia.Media.IGlyphTypeface,System.Double,System.SByte)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Media.TextFormatting.ShapedBuffer.get_GlyphTypeface` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Media.TextFormatting.TextCollapsingProperties.CreateCollapsedRuns(Avalonia.Media.TextFormatting.TextLine,System.Int32,Avalonia.Media.FlowDirection,Avalonia.Media.TextFormatting.TextRun)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.TextFormatting.TextLayout.#ctor(System.String,Avalonia.Media.Typeface,Avalonia.Media.FontFeatureCollection,System.Double,Avalonia.Media.IBrush,Avalonia.Media.TextAlignment,Avalonia.Media.TextWrapping,Avalonia.Media.TextTrimming,Avalonia.Media.TextDecorationCollection,Avalonia.Media.FlowDirection,System.Double,System.Double,System.Double,System.Double,System.Int32,System.Collections.Generic.IReadOnlyList{Avalonia.Utilities.ValueSpan{Avalonia.Media.TextFormatting.TextRunProperties}})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.TextFormatting.TextLayout.#ctor(System.String,Avalonia.Media.Typeface,System.Double,Avalonia.Media.IBrush,Avalonia.Media.TextAlignment,Avalonia.Media.TextWrapping,Avalonia.Media.TextTrimming,Avalonia.Media.TextDecorationCollection,Avalonia.Media.FlowDirection,System.Double,System.Double,System.Double,System.Double,System.Int32,System.Collections.Generic.IReadOnlyList{Avalonia.Utilities.ValueSpan{Avalonia.Media.TextFormatting.TextRunProperties}})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.TextFormatting.TextMetrics.#ctor(Avalonia.Media.IGlyphTypeface,System.Double)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Media.TextFormatting.TextShaperOptions.#ctor(Avalonia.Media.GlyphTypeface,System.Collections.Generic.IReadOnlyList{Avalonia.Media.FontFeature},System.Double,System.SByte,System.Globalization.CultureInfo,System.Double,System.Double)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.TextFormatting.TextShaperOptions.#ctor(Avalonia.Media.GlyphTypeface,System.Double,System.SByte,System.Globalization.CultureInfo,System.Double,System.Double)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.TextFormatting.TextShaperOptions.#ctor(Avalonia.Media.IGlyphTypeface,System.Collections.Generic.IReadOnlyList{Avalonia.Media.FontFeature},System.Double,System.SByte,System.Globalization.CultureInfo,System.Double,System.Double)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Media.TextFormatting.TextShaperOptions.#ctor(Avalonia.Media.IGlyphTypeface,System.Double,System.SByte,System.Globalization.CultureInfo,System.Double,System.Double)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Media.TextFormatting.TextShaperOptions.get_Typeface` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Media.Typeface.get_GlyphTypeface` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.OpenGL.Egl.EglPlatformSurfaceRenderTargetBase.BeginDraw` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.OpenGL.Egl.EglPlatformSurfaceRenderTargetBase.BeginDraw(System.Nullable{Avalonia.PixelSize})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.OpenGL.Egl.EglPlatformSurfaceRenderTargetBase.BeginDrawCore` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.OpenGL.Egl.EglPlatformSurfaceRenderTargetBase.BeginDrawCore(System.Nullable{Avalonia.PixelSize})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.OpenGL.IGlPlatformSurfaceRenderTargetFactory.CanRenderToSurface(Avalonia.OpenGL.IGlContext,System.Object)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.OpenGL.IGlPlatformSurfaceRenderTargetFactory.CreateRenderTarget(Avalonia.OpenGL.IGlContext,System.Object)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.OpenGL.Surfaces.IGlPlatformSurfaceRenderTarget.BeginDraw` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.OpenGL.Surfaces.IGlPlatformSurfaceRenderTarget.BeginDraw(System.Nullable{Avalonia.PixelSize})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.Platform.ICursorFactory.CreateCursor(Avalonia.Platform.IBitmapImpl,Avalonia.PixelPoint)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IDrawingContextImplWithEffects.PopEffect` (method/member; baseline `baseline/netstandard2.0/Avalonia.Base.dll` -> current `target/netstandard2.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IDrawingContextImplWithEffects.PushEffect(Avalonia.Media.IEffect)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IFontManagerImpl.TryCreateGlyphTypeface(System.IO.Stream,Avalonia.Media.FontSimulations,Avalonia.Media.IGlyphTypeface@)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IFontManagerImpl.TryCreateGlyphTypeface(System.String,Avalonia.Media.FontStyle,Avalonia.Media.FontWeight,Avalonia.Media.FontStretch,Avalonia.Media.IGlyphTypeface@)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IFontManagerImpl.TryMatchCharacter(System.Int32,Avalonia.Media.FontStyle,Avalonia.Media.FontWeight,Avalonia.Media.FontStretch,System.Globalization.CultureInfo,Avalonia.Media.Typeface@)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IGeometryContext.ArcTo(Avalonia.Point,Avalonia.Size,System.Double,System.Boolean,Avalonia.Media.SweepDirection)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IGeometryContext.CubicBezierTo(Avalonia.Point,Avalonia.Point,Avalonia.Point)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IGeometryContext.LineTo(Avalonia.Point)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IGeometryContext.QuadraticBezierTo(Avalonia.Point,Avalonia.Point)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IGlyphRunImpl.get_GlyphTypeface` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IPlatformRenderInterface.CreateGlyphRun(Avalonia.Media.IGlyphTypeface,System.Double,System.Collections.Generic.IReadOnlyList{Avalonia.Media.TextFormatting.GlyphInfo},Avalonia.Point)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IPlatformRenderInterfaceContext.CreateOffscreenRenderTarget(Avalonia.PixelSize,System.Double)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IPlatformRenderInterfaceContext.CreateRenderTarget(System.Collections.Generic.IEnumerable{System.Object})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IRenderTarget.CreateDrawingContext(Avalonia.PixelSize,Avalonia.Platform.RenderTargetDrawingContextProperties@)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IRenderTarget.CreateDrawingContext(System.Boolean)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.ITopLevelImpl.get_Surfaces` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.IWindowImpl.GetWindowsZOrder(System.Span{Avalonia.Controls.Window},System.Span{System.Int64})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.IWindowImpl.SetExtendClientAreaChromeHints(Avalonia.Platform.ExtendClientAreaChromeHints)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.IWindowImpl.SetSystemDecorations(Avalonia.Controls.SystemDecorations)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.LockedFramebuffer.#ctor(System.IntPtr,Avalonia.PixelSize,System.Int32,Avalonia.Vector,Avalonia.Platform.PixelFormat,System.Action)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.Screen.#ctor(System.Double,Avalonia.PixelRect,Avalonia.PixelRect,System.Boolean)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.Screen.get_PixelDensity` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.Screen.get_Primary` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.Screen.set_Bounds(Avalonia.PixelRect)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.Screen.set_CurrentOrientation(Avalonia.Platform.ScreenOrientation)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.Screen.set_DisplayName(System.String)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.Screen.set_IsPrimary(System.Boolean)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.Screen.set_Scaling(System.Double)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.Screen.set_WorkingArea(Avalonia.PixelRect)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Rendering.Composition.ICompositionGpuImportedObject.get_ImportCompeted` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Rendering.SceneInvalidatedEventArgs.#ctor(Avalonia.Rendering.IRenderRoot,Avalonia.Rect)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Rendering.SceneInvalidatedEventArgs.get_RenderRoot` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.StyledElementExtensions.BindClass(Avalonia.StyledElement,System.String,Avalonia.Data.IBinding,System.Object)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Threading.DispatcherPriorityAwaitable.GetAwaiter` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Threading.DispatcherPriorityAwaitable.GetResult` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Threading.DispatcherPriorityAwaitable.OnCompleted(System.Action)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Threading.DispatcherPriorityAwaitable.get_IsCompleted` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Threading.DispatcherPriorityAwaitable`1.GetAwaiter` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Threading.DispatcherPriorityAwaitable`1.GetResult` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Utilities.AvaloniaResourcesIndexReaderWriter.WriteResources(System.IO.Stream,System.Collections.Generic.List{System.ValueTuple{System.String,System.Int32,System.Func{System.IO.Stream}}})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Visual.get_VisualRoot` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.VisualTree.VisualExtensions.GetVisualRoot(Avalonia.Visual)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.VisualTreeAttachmentEventArgs.#ctor(Avalonia.Visual,Avalonia.Rendering.IRenderRoot)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.VisualTreeAttachmentEventArgs.get_Root` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Visuals.Platform.PathGeometryContext.ArcTo(Avalonia.Point,Avalonia.Size,System.Double,System.Boolean,Avalonia.Media.SweepDirection)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Visuals.Platform.PathGeometryContext.CubicBezierTo(Avalonia.Point,Avalonia.Point,Avalonia.Point)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Visuals.Platform.PathGeometryContext.LineTo(Avalonia.Point)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Visuals.Platform.PathGeometryContext.QuadraticBezierTo(Avalonia.Point,Avalonia.Point)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Vulkan.IVulkanKhrSurfacePlatformSurfaceFactory.CanRenderToSurface(Avalonia.Vulkan.IVulkanPlatformGraphicsContext,System.Object)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Vulkan.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Vulkan.dll`)
- `Avalonia.Vulkan.IVulkanKhrSurfacePlatformSurfaceFactory.CreateSurface(Avalonia.Vulkan.IVulkanPlatformGraphicsContext,System.Object)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Vulkan.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Vulkan.dll`)
- `Avalonia.Vulkan.IVulkanPlatformGraphicsContext.CreateRenderTarget(System.Collections.Generic.IEnumerable{System.Object})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Vulkan.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Vulkan.dll`)

### `CP0003`: other compatibility change

- `Avalonia.DesignerSupport, Version=0.7.0.0, Culture=neutral, PublicKeyToken=c8d484a7012f9a8b` (symbol; baseline `baseline/Avalonia/lib/net10.0/Avalonia.DesignerSupport.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.DesignerSupport.dll`)

### `CP0005`: other compatibility change

- `Avalonia.Controls.Embedding.Offscreen.OffscreenTopLevelImplBase.get_Surfaces` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.OpenGL.Egl.EglPlatformSurfaceRenderTargetBase.BeginDrawCore(Avalonia.Platform.IRenderTarget.RenderTargetSceneInfo)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.OpenGL.Egl.EglPlatformSurfaceRenderTargetBase.BeginDrawCore(System.Nullable{Avalonia.PixelSize})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.Controls.Embedding.Offscreen.OffscreenTopLevelImplBase.Surfaces` (property; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)

### `CP0006`: new interface member without default implementation

- `Avalonia.Controls.Templates.ITreeDataTemplate.BindChildren(Avalonia.AvaloniaObject,Avalonia.AvaloniaProperty,System.Object)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Controls.dll`)
- `Avalonia.Input.IKeyboardNavigationHandler.Move(Avalonia.Input.IInputElement,Avalonia.Input.NavigationDirection,Avalonia.Input.KeyModifiers,System.Nullable{Avalonia.Input.KeyDeviceType})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.Platform.IClipboard.SetDataAsync(Avalonia.Input.IAsyncDataTransfer)` (method/member; baseline `baseline/Avalonia/lib/net6.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net6.0/Avalonia.Base.dll`)
- `Avalonia.Input.Platform.IClipboard.TryGetDataAsync` (method/member; baseline `baseline/Avalonia/lib/net6.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net6.0/Avalonia.Base.dll`)
- `Avalonia.Input.Platform.IClipboard.TryGetInProcessDataAsync` (method/member; baseline `baseline/Avalonia/lib/net6.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net6.0/Avalonia.Base.dll`)
- `Avalonia.Input.Platform.IPlatformDragSource.DoDragDropAsync(Avalonia.Input.PointerEventArgs,Avalonia.Input.IDataTransfer,Avalonia.Input.DragDropEffects)` (method/member; baseline `baseline/Avalonia/lib/net6.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net6.0/Avalonia.Base.dll`)
- `Avalonia.Media.Fonts.IFontCollection.TryCreateSyntheticGlyphTypeface(Avalonia.Media.GlyphTypeface,Avalonia.Media.FontStyle,Avalonia.Media.FontWeight,Avalonia.Media.FontStretch,Avalonia.Media.GlyphTypeface@)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Media.Fonts.IFontCollection.TryGetFamilyTypefaces(System.String,System.Collections.Generic.IReadOnlyList{Avalonia.Media.Typeface}@)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Media.Fonts.IFontCollection.TryGetGlyphTypeface(System.String,Avalonia.Media.FontStyle,Avalonia.Media.FontWeight,Avalonia.Media.FontStretch,Avalonia.Media.GlyphTypeface@)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Media.Fonts.IFontCollection.TryGetNearestMatch(System.String,Avalonia.Media.FontStyle,Avalonia.Media.FontWeight,Avalonia.Media.FontStretch,Avalonia.Media.GlyphTypeface@)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.OpenGL.IGlExternalSemaphore.SignalTimelineSemaphore(Avalonia.OpenGL.IGlExternalImageTexture,System.UInt64)` (method/member; baseline `baseline/Avalonia/lib/net6.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net6.0/Avalonia.OpenGL.dll`)
- `Avalonia.OpenGL.IGlExternalSemaphore.WaitTimelineSemaphore(Avalonia.OpenGL.IGlExternalImageTexture,System.UInt64)` (method/member; baseline `baseline/Avalonia/lib/net6.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net6.0/Avalonia.OpenGL.dll`)
- `Avalonia.OpenGL.IGlPlatformSurfaceRenderTargetFactory.CanRenderToSurface(Avalonia.OpenGL.IGlContext,Avalonia.Platform.Surfaces.IPlatformRenderSurface)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.OpenGL.IGlPlatformSurfaceRenderTargetFactory.CreateRenderTarget(Avalonia.OpenGL.IGlContext,Avalonia.Platform.Surfaces.IPlatformRenderSurface)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.OpenGL.Surfaces.IGlPlatformSurfaceRenderTarget.BeginDraw(Avalonia.Platform.IRenderTarget.RenderTargetSceneInfo)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.OpenGL.Surfaces.IGlPlatformSurfaceRenderTarget.BeginDraw(System.Nullable{Avalonia.PixelSize})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.Platform.ICursorFactory.CreateCursor(Avalonia.Media.Imaging.Bitmap,Avalonia.PixelPoint)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IDrawingContextImpl.PopTextOptions` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IDrawingContextImpl.PushTextOptions(Avalonia.Media.TextOptions)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IDrawingContextImplWithEffects.PushEffect(System.Nullable{Avalonia.Rect},Avalonia.Media.IEffect)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IDrawingContextLayerImpl.CreateDrawingContext` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IFontManagerImpl.TryCreateGlyphTypeface(System.IO.Stream,Avalonia.Media.FontSimulations,Avalonia.Media.IPlatformTypeface@)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IFontManagerImpl.TryCreateGlyphTypeface(System.String,Avalonia.Media.FontStyle,Avalonia.Media.FontWeight,Avalonia.Media.FontStretch,Avalonia.Media.IPlatformTypeface@)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IFontManagerImpl.TryGetFamilyTypefaces(System.String,System.Collections.Generic.IReadOnlyList{Avalonia.Media.Typeface}@)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IFontManagerImpl.TryMatchCharacter(System.Int32,Avalonia.Media.FontStyle,Avalonia.Media.FontWeight,Avalonia.Media.FontStretch,System.String,System.Globalization.CultureInfo,Avalonia.Media.IPlatformTypeface@)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IFontManagerImpl.TryMatchCharacter(System.Int32,Avalonia.Media.FontStyle,Avalonia.Media.FontWeight,Avalonia.Media.FontStretch,System.String,System.Globalization.CultureInfo,Avalonia.Media.Typeface@)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IGeometryContext.ArcTo(Avalonia.Point,Avalonia.Size,System.Double,System.Boolean,Avalonia.Media.SweepDirection,System.Boolean)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IGeometryContext.CubicBezierTo(Avalonia.Point,Avalonia.Point,Avalonia.Point,System.Boolean)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IGeometryContext.LineTo(Avalonia.Point,System.Boolean)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IGeometryContext.QuadraticBezierTo(Avalonia.Point,Avalonia.Point,System.Boolean)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IPlatformRenderInterface.CreateGlyphRun(Avalonia.Media.GlyphTypeface,System.Double,System.Collections.Generic.IReadOnlyList{Avalonia.Media.TextFormatting.GlyphInfo},Avalonia.Point)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IPlatformRenderInterfaceContext.CreateOffscreenRenderTarget(Avalonia.PixelSize,Avalonia.Vector,System.Boolean)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IPlatformRenderInterfaceContext.CreateRenderTarget(System.Collections.Generic.IEnumerable{Avalonia.Platform.Surfaces.IPlatformRenderSurface})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IPlatformRenderInterfaceImportedImage.SnapshotWithTimelineSemaphores(Avalonia.Platform.IPlatformRenderInterfaceImportedSemaphore,System.UInt64,Avalonia.Platform.IPlatformRenderInterfaceImportedSemaphore,System.UInt64)` (method/member; baseline `baseline/Avalonia/lib/net6.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net6.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IRenderTarget.CreateDrawingContext(Avalonia.PixelSize,Avalonia.Platform.RenderTargetDrawingContextProperties@)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IRenderTarget.CreateDrawingContext(Avalonia.Platform.IRenderTarget.RenderTargetSceneInfo,Avalonia.Platform.RenderTargetDrawingContextProperties@)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IRenderTargetBitmapImpl.CreateDrawingContext` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.ITextShaperImpl.CreateTypeface(Avalonia.Media.GlyphTypeface)` (method/member; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IWindowImpl.SetWindowDecorations(Avalonia.Controls.WindowDecorations)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.IWindowingPlatform.GetWindowsZOrder(System.ReadOnlySpan{Avalonia.Platform.IWindowImpl},System.Span{System.Int64})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.Storage.IStorageProvider.SaveFilePickerWithResultAsync(Avalonia.Platform.Storage.FilePickerSaveOptions)` (method/member; baseline `baseline/Avalonia/lib/net6.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net6.0/Avalonia.Base.dll`)
- `Avalonia.Vulkan.IVulkanKhrSurfacePlatformSurfaceFactory.CanRenderToSurface(Avalonia.Vulkan.IVulkanPlatformGraphicsContext,Avalonia.Platform.Surfaces.IPlatformRenderSurface)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Vulkan.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Vulkan.dll`)
- `Avalonia.Vulkan.IVulkanKhrSurfacePlatformSurfaceFactory.CreateSurface(Avalonia.Vulkan.IVulkanPlatformGraphicsContext,Avalonia.Platform.Surfaces.IPlatformRenderSurface)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Vulkan.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Vulkan.dll`)
- `Avalonia.Vulkan.IVulkanPlatformGraphicsContext.CreateRenderTarget(System.Collections.Generic.IEnumerable{Avalonia.Platform.Surfaces.IPlatformRenderSurface})` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Vulkan.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Vulkan.dll`)
- `Avalonia.Input.IInputRoot.FocusRoot` (property; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.OpenGL.IGlExternalImageTexture.TextureType` (property; baseline `baseline/Avalonia/lib/net6.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net6.0/Avalonia.OpenGL.dll`)
- `Avalonia.OpenGL.Surfaces.IGlPlatformSurfaceRenderTarget.IsCorrupted` (property; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.Platform.IDrawingContextLayerImpl.IsCorrupted` (property; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.ILockedFramebuffer.AlphaFormat` (property; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IPlatformRenderInterfaceContext.MaxOffscreenRenderTargetPixelSize` (property; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IReadableBitmapImpl.AlphaFormat` (property; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IRenderTarget.Properties` (property; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.ITopLevelImpl.Surfaces` (property; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.IWindowImpl.RequestedDrawnDecorations` (property; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)

### `CP0007`: removed base type

- `Avalonia.Controls.ResourcesChangedEventArgs` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Data.TemplateBinding` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Threading.DispatcherPriorityAwaitable` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Threading.DispatcherPriorityAwaitable`1` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)

### `CP0008`: removed base interface

- `Avalonia.Application` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Embedding.EmbeddableControlRoot` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Embedding.Offscreen.OffscreenTopLevelImplBase` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Platform.IWin32OptionsTopLevelImpl` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.OverlayPopupHost` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.PopupRoot` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.TopLevel` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Window` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.WindowBase` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Data.Binding` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Markup.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Markup.dll`)
- `Avalonia.Data.TemplateBinding` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Dialogs.AboutAvaloniaDialog` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Dialogs.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Dialogs.dll`)
- `Avalonia.Input.DataObject` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.IInputRoot` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Markup.Xaml.MarkupExtensions.CompiledBindingExtension` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll`)
- `Avalonia.Media.ImmediateDrawingContext` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.StreamGeometryContext` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Metal.IMetalDevice` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Metal.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Metal.dll`)
- `Avalonia.OpenGL.Egl.EglContext` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.OpenGL.Egl.EglPlatformSurfaceRenderTargetBase` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.OpenGL.IGlContext` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.OpenGL.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.OpenGL.dll`)
- `Avalonia.Platform.IDrawingContextLayerImpl` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IDrawingContextLayerWithRenderContextAffinityImpl` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IPlatformGraphicsContext` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IPlatformGraphicsWithFeatures` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IPlatformRenderInterfaceContext` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.IPopupImpl` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.IRenderTargetBitmapImpl` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.ITopLevelImpl` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.IWindowBaseImpl` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.IWindowImpl` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Platform.IWriteableBitmapImpl` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Threading.DispatcherPriorityAwaitable` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Threading.DispatcherPriorityAwaitable`1` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Vulkan.IVulkanDevice` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Vulkan.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Vulkan.dll`)
- `Avalonia.Vulkan.IVulkanPlatformGraphicsContext` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Vulkan.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Vulkan.dll`)

### `CP0009`: type became sealed

- `Avalonia.Controls.Primitives.AdornerLayer` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.OverlayLayer` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.OverlayPopupHost` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.Primitives.VisualLayerManager` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Controls.ResourcesChangedEventArgs` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Data.MultiBinding` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Markup.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Markup.dll`)
- `Avalonia.Data.TemplateBinding` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Base.dll`)
- `Avalonia.Input.DataObject` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Input.HoldingRoutedEventArgs` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Markup.Xaml.MarkupExtensions.CompiledBindingExtension` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll`)
- `Avalonia.Markup.Xaml.MarkupExtensions.DynamicResourceExtension` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll`)
- `Avalonia.Markup.Xaml.MarkupExtensions.ReflectionBindingExtension` (type; baseline `baseline/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll` -> current `current/Avalonia/lib/net8.0/Avalonia.Markup.Xaml.dll`)
- `Avalonia.Platform.Screen` (type; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)

### `CP0012`: member lost virtual/abstract

- `Avalonia.Media.Fonts.FontCollectionBase.GetEnumerator` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.Fonts.FontCollectionBase.get_Count` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.Fonts.FontCollectionBase.get_Item(System.Int32)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Platform.Screen.Equals(Avalonia.Platform.Screen)` (method/member; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Controls.dll`)
- `Avalonia.Media.Fonts.FontCollectionBase.Count` (property; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)
- `Avalonia.Media.Fonts.FontCollectionBase.Item(System.Int32)` (property; baseline `baseline/Avalonia/lib/net10.0/Avalonia.Base.dll` -> current `current/Avalonia/lib/net10.0/Avalonia.Base.dll`)

## Breaking Changes: `Avalonia.Android`

### `CP0001`: missing public type

- `Avalonia.Android.Platform.Specific.IAndroidView` (type; baseline `baseline/Avalonia.Android/lib/net10.0-android36.0/Avalonia.Android.dll` -> current `current/Avalonia.Android/lib/net10.0-android36.0/Avalonia.Android.dll`)
- `Avalonia.Android.Resource` (type; baseline `baseline/Avalonia.Android/lib/net10.0-android36.0/Avalonia.Android.dll` -> current `current/Avalonia.Android/lib/net10.0-android36.0/Avalonia.Android.dll`)

### `CP0002`: missing public member

- `Avalonia.Android.AvaloniaMainActivity.CreateAppBuilder` (method/member; baseline `baseline/Avalonia.Android/lib/net10.0-android36.0/Avalonia.Android.dll` -> current `current/Avalonia.Android/lib/net10.0-android36.0/Avalonia.Android.dll`)
- `Avalonia.Android.AvaloniaMainActivity.CustomizeAppBuilder(Avalonia.AppBuilder)` (method/member; baseline `baseline/Avalonia.Android/lib/net10.0-android36.0/Avalonia.Android.dll` -> current `current/Avalonia.Android/lib/net10.0-android36.0/Avalonia.Android.dll`)

### `CP0008`: removed base interface

- `Avalonia.Android.AvaloniaActivity` (type; baseline `baseline/Avalonia.Android/lib/net10.0-android36.0/Avalonia.Android.dll` -> current `current/Avalonia.Android/lib/net10.0-android36.0/Avalonia.Android.dll`)
- `Avalonia.Android.AvaloniaMainActivity` (type; baseline `baseline/Avalonia.Android/lib/net10.0-android36.0/Avalonia.Android.dll` -> current `current/Avalonia.Android/lib/net10.0-android36.0/Avalonia.Android.dll`)

## Breaking Changes: `Avalonia.Headless`

### `CP0002`: missing public member

- `Avalonia.Headless.HeadlessWindowExtensions.DragDrop(Avalonia.Controls.TopLevel,Avalonia.Point,Avalonia.Input.Raw.RawDragEventType,Avalonia.Input.IDataObject,Avalonia.Input.DragDropEffects,Avalonia.Input.RawInputModifiers)` (method/member; baseline `baseline/Avalonia.Headless/lib/net10.0/Avalonia.Headless.dll` -> current `current/Avalonia.Headless/lib/net10.0/Avalonia.Headless.dll`)
- `Avalonia.Headless.HeadlessWindowExtensions.KeyPress(Avalonia.Controls.TopLevel,Avalonia.Input.Key,Avalonia.Input.RawInputModifiers)` (method/member; baseline `baseline/Avalonia.Headless/lib/net10.0/Avalonia.Headless.dll` -> current `current/Avalonia.Headless/lib/net10.0/Avalonia.Headless.dll`)
- `Avalonia.Headless.HeadlessWindowExtensions.KeyRelease(Avalonia.Controls.TopLevel,Avalonia.Input.Key,Avalonia.Input.RawInputModifiers)` (method/member; baseline `baseline/Avalonia.Headless/lib/net10.0/Avalonia.Headless.dll` -> current `current/Avalonia.Headless/lib/net10.0/Avalonia.Headless.dll`)

## Breaking Changes: `Avalonia.Headless.XUnit`

### `CP0001`: missing public type

- `Avalonia.Headless.XUnit.AvaloniaTestFrameworkTypeDiscoverer` (type; baseline `baseline/Avalonia.Headless.XUnit/lib/net10.0/Avalonia.Headless.XUnit.dll` -> current `current/Avalonia.Headless.XUnit/lib/net10.0/Avalonia.Headless.XUnit.dll`)
- `Avalonia.Headless.XUnit.AvaloniaUIFactDiscoverer` (type; baseline `baseline/Avalonia.Headless.XUnit/lib/net10.0/Avalonia.Headless.XUnit.dll` -> current `current/Avalonia.Headless.XUnit/lib/net10.0/Avalonia.Headless.XUnit.dll`)

### `CP0002`: missing public member

- `Avalonia.Headless.XUnit.AvaloniaFactAttribute.#ctor` (method/member; baseline `baseline/Avalonia.Headless.XUnit/lib/net10.0/Avalonia.Headless.XUnit.dll` -> current `current/Avalonia.Headless.XUnit/lib/net10.0/Avalonia.Headless.XUnit.dll`)
- `Avalonia.Headless.XUnit.AvaloniaTheoryDiscoverer.#ctor(Xunit.Abstractions.IMessageSink)` (method/member; baseline `baseline/Avalonia.Headless.XUnit/lib/net10.0/Avalonia.Headless.XUnit.dll` -> current `current/Avalonia.Headless.XUnit/lib/net10.0/Avalonia.Headless.XUnit.dll`)

### `CP0007`: removed base type

- `Avalonia.Headless.XUnit.AvaloniaTheoryDiscoverer` (type; baseline `baseline/Avalonia.Headless.XUnit/lib/net10.0/Avalonia.Headless.XUnit.dll` -> current `current/Avalonia.Headless.XUnit/lib/net10.0/Avalonia.Headless.XUnit.dll`)

### `CP0008`: removed base interface

- `Avalonia.Headless.XUnit.AvaloniaTestFrameworkAttribute` (type; baseline `baseline/Avalonia.Headless.XUnit/lib/net10.0/Avalonia.Headless.XUnit.dll` -> current `current/Avalonia.Headless.XUnit/lib/net10.0/Avalonia.Headless.XUnit.dll`)

## Breaking Changes: `Avalonia.LinuxFramebuffer`

### `CP0002`: missing public member

- `Avalonia.LinuxFramebuffer.FbdevOutput.CreateFramebufferRenderTarget` (method/member; baseline `baseline/Avalonia.LinuxFramebuffer/lib/net10.0/Avalonia.LinuxFramebuffer.dll` -> current `current/Avalonia.LinuxFramebuffer/lib/net10.0/Avalonia.LinuxFramebuffer.dll`)
- `Avalonia.LinuxFramebuffer.FbdevOutput.Lock` (method/member; baseline `baseline/Avalonia.LinuxFramebuffer/lib/net10.0/Avalonia.LinuxFramebuffer.dll` -> current `current/Avalonia.LinuxFramebuffer/lib/net10.0/Avalonia.LinuxFramebuffer.dll`)

### `CP0008`: removed base interface

- `Avalonia.LinuxFramebuffer.FbdevOutput` (type; baseline `baseline/Avalonia.LinuxFramebuffer/lib/net10.0/Avalonia.LinuxFramebuffer.dll` -> current `current/Avalonia.LinuxFramebuffer/lib/net10.0/Avalonia.LinuxFramebuffer.dll`)

## Breaking Changes: `Avalonia.Skia`

### `CP0001`: missing public type

- `Avalonia.Skia.ISkiaGpu` (type; baseline `baseline/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll` -> current `current/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll`)
- `Avalonia.Skia.ISkiaGpuRenderTarget2` (type; baseline `baseline/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll` -> current `current/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll`)
- `Avalonia.Skia.ISkiaGpuWithPlatformGraphicsContext` (type; baseline `baseline/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll` -> current `current/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll`)

### `CP0002`: missing public member

- `Avalonia.Skia.Helpers.DrawingContextHelper.WrapSkiaCanvas(SkiaSharp.SKCanvas,Avalonia.Vector)` (method/member; baseline `baseline/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll` -> current `current/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll`)
- `Avalonia.Skia.ISkiaGpu.TryCreateRenderTarget(System.Collections.Generic.IEnumerable{System.Object})` (method/member; baseline `baseline/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll` -> current `current/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll`)
- `Avalonia.Skia.ISkiaGpuRenderTarget.BeginRenderingSession` (method/member; baseline `baseline/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll` -> current `current/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll`)
- `Avalonia.Skia.ISkiaGpuRenderTarget.BeginRenderingSession(System.Nullable{Avalonia.PixelSize})` (method/member; baseline `baseline/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll` -> current `current/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll`)
- `Avalonia.Skia.SkiaSharpExtensions.ToSKFilterQuality(Avalonia.Media.Imaging.BitmapInterpolationMode)` (method/member; baseline `baseline/Avalonia.Skia/lib/net8.0/Avalonia.Skia.dll` -> current `current/Avalonia.Skia/lib/net8.0/Avalonia.Skia.dll`)

### `CP0006`: new interface member without default implementation

- `Avalonia.Skia.ISkiaGpu.TryCreateRenderTarget(System.Collections.Generic.IEnumerable{Avalonia.Platform.Surfaces.IPlatformRenderSurface})` (method/member; baseline `baseline/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll` -> current `current/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll`)
- `Avalonia.Skia.ISkiaGpu.TryGetGrContext` (method/member; baseline `baseline/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll` -> current `current/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll`)
- `Avalonia.Skia.ISkiaGpuRenderTarget.BeginRenderingSession(Avalonia.Platform.IRenderTarget.RenderTargetSceneInfo)` (method/member; baseline `baseline/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll` -> current `current/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll`)
- `Avalonia.Skia.ISkiaGpuRenderTarget.BeginRenderingSession(System.Nullable{Avalonia.PixelSize})` (method/member; baseline `baseline/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll` -> current `current/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll`)
- `Avalonia.Skia.ISkiaGpu.PlatformGraphicsContext` (property; baseline `baseline/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll` -> current `current/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll`)

### `CP0008`: removed base interface

- `Avalonia.Skia.ISkiaGpu` (type; baseline `baseline/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll` -> current `current/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll`)
- `Avalonia.Skia.ISkiaGpuWithPlatformGraphicsContext` (type; baseline `baseline/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll` -> current `current/Avalonia.Skia/lib/net10.0/Avalonia.Skia.dll`)

## Breaking Changes: `Avalonia.Win32.Interoperability`

### `CP0002`: missing public member

- `Avalonia.Win32.Interoperability.WinFormsAvaloniaControlHost.PreFilterMessage(System.Windows.Forms.Message@)` (method/member; baseline `baseline/Avalonia.Win32.Interoperability/lib/net461/Avalonia.Win32.Interoperability.dll` -> current `current/Avalonia.Win32.Interoperability/lib/net461/Avalonia.Win32.Interoperability.dll`)

### `CP0008`: removed base interface

- `Avalonia.Win32.Interoperability.WinFormsAvaloniaControlHost` (type; baseline `baseline/Avalonia.Win32.Interoperability/lib/net461/Avalonia.Win32.Interoperability.dll` -> current `current/Avalonia.Win32.Interoperability/lib/net461/Avalonia.Win32.Interoperability.dll`)

## Breaking Changes: `Avalonia.X11`

### `CP0002`: missing public member

- `Avalonia.X11PlatformOptions.get_ExterinalGLibMainLoopExceptionLogger` (method/member; baseline `baseline/Avalonia.X11/lib/net8.0/Avalonia.X11.dll` -> current `current/Avalonia.X11/lib/net8.0/Avalonia.X11.dll`)
- `Avalonia.X11PlatformOptions.set_ExterinalGLibMainLoopExceptionLogger(System.Action{System.Exception})` (method/member; baseline `baseline/Avalonia.X11/lib/net8.0/Avalonia.X11.dll` -> current `current/Avalonia.X11/lib/net8.0/Avalonia.X11.dll`)

## Added Public APIs

- Public signatures: `1041`

### By Area

- `Android Platform`: `2`
- `Application Model and Controls`: `529`
- `Headless Platform`: `8`
- `Linux Framebuffer`: `7`
- `Linux/X11 Platform`: `2`
- `Other`: `27`
- `Property, Data, Styling, Threading`: `431`
- `Rendering and Text`: `12`
- `Source Generator Integration`: `2`
- `Windows Platform`: `2`
- `XAML and Markup`: `15`
- `iOS Platform`: `3`
- `macOS Native Platform`: `1`

### By Kind

- `delegate`: `1`
- `event`: `37`
- `indexer`: `3`
- `member`: `508`
- `method`: `341`
- `operator`: `4`
- `type`: `147`

### Android Platform

#### `src/Android/Avalonia.Android/AvaloniaAndroidApplication.cs`

- `public class AvaloniaAndroidApplication<TApp> : global::Android.App.Application, IAndroidApplication where TApp : Application, new() {`
- `AvaloniaAndroidApplication` -> `public override void OnCreate() {`

### Application Model and Controls

#### `src/Avalonia.Controls/AppBuilder.cs`

- `AppBuilder` -> `public Action? TextShapingSubsystemInitializer { get; private set; }`
- `AppBuilder` -> `public AppBuilder UseTextShapingSubsystem(Action initializer, string name = "") {`
- `AppBuilder` -> `public AppBuilder WithDataAnnotationsValidation() {`
- `AppBuilder` -> `public string? TextShapingSubsystemName { get; private set; }`

#### `src/Avalonia.Controls/Application.cs`

- `public class Application : AvaloniaObject, IDataContextProvider, IGlobalDataTemplates, IGlobalStyles, IThemeVariantHost, IResourceHost, IOptionalFeatureProvider {`

#### `src/Avalonia.Controls/ApplicationLifetimes/IActivityApplicationLifetime.cs`

- `IActivityApplicationLifetime` -> `Func<Control>? MainViewFactory { get; set; }`
- `public interface IActivityApplicationLifetime : IApplicationLifetime {`

#### `src/Avalonia.Controls/AutoCompleteBox/AutoCompleteBox.Properties.cs`

- `AutoCompleteBox` -> `public BindingBase? ValueMemberBinding {`
- `AutoCompleteBox` -> `public Media.IBrush? PlaceholderForeground {`
- `AutoCompleteBox` -> `public Media.IBrush? WatermarkForeground {`
- `AutoCompleteBox` -> `public static readonly StyledProperty<BindingBase?> ValueMemberBindingProperty = AvaloniaProperty.Register<AutoCompleteBox, BindingBase?>(nameof(ValueMemberBinding));`
- `AutoCompleteBox` -> `public static readonly StyledProperty<Media.IBrush?> PlaceholderForegroundProperty = TextBox.PlaceholderForegroundProperty.AddOwner<AutoCompleteBox>();`
- `AutoCompleteBox` -> `public static readonly StyledProperty<Media.IBrush?> WatermarkForegroundProperty = PlaceholderForegroundProperty;`
- `AutoCompleteBox` -> `public static readonly StyledProperty<string?> PlaceholderTextProperty = TextBox.PlaceholderTextProperty.AddOwner<AutoCompleteBox>();`
- `AutoCompleteBox` -> `public static readonly StyledProperty<string?> WatermarkProperty = PlaceholderTextProperty;`
- `AutoCompleteBox` -> `public string? PlaceholderText {`

#### `src/Avalonia.Controls/Automation/AutomationProperties.cs`

- `AutomationProperties` -> `public static bool? GetIsControlElementOverride(StyledElement element) {`
- `AutomationProperties` -> `public static readonly AttachedProperty<bool?> IsControlElementOverrideProperty = AvaloniaProperty.RegisterAttached<StyledElement, bool?>( "IsControlElementOverride", typeof(AutomationProperties));`
- `AutomationProperties` -> `public static readonly AttachedProperty<string?> ClassNameOverrideProperty = AvaloniaProperty.RegisterAttached<StyledElement, string?>( "ClassNameOverride", typeof(AutomationProperties));`
- `AutomationProperties` -> `public static string? GetClassNameOverride(StyledElement element) {`
- `AutomationProperties` -> `public static void SetClassNameOverride(StyledElement element, string? value) {`
- `AutomationProperties` -> `public static void SetIsControlElementOverride(StyledElement element, bool? value) {`

#### `src/Avalonia.Controls/Automation/Peers/AutomationPeer.cs`

- `AutomationPeer` -> `public AutomationPeer? GetAutomationRoot() => GetAutomationRootCore();`
- `AutomationPeer` -> `public string GetClassName() => GetClassNameOverrideCore() ?? string.Empty;`
- `AutomationPeer` -> `public string GetPlaceholderText() => GetPlaceholderTextCore() ?? string.Empty;`

#### `src/Avalonia.Controls/Automation/Peers/ContentPageAutomationPeer.cs`

- Namespace(s): `Avalonia.Automation.Peers`
- `ContentPageAutomationPeer` -> `public ContentPageAutomationPeer(ContentPage owner) : base(owner) {`
- `public class ContentPageAutomationPeer : ControlAutomationPeer {`
- `ContentPageAutomationPeer` -> `public new ContentPage Owner => (ContentPage)base.Owner;`

#### `src/Avalonia.Controls/Automation/Peers/DrawerPageAutomationPeer.cs`

- Namespace(s): `Avalonia.Automation.Peers`
- `DrawerPageAutomationPeer` -> `public DrawerPageAutomationPeer(DrawerPage owner) : base(owner) {`
- `public class DrawerPageAutomationPeer : ControlAutomationPeer {`
- `DrawerPageAutomationPeer` -> `public new DrawerPage Owner => (DrawerPage)base.Owner;`

#### `src/Avalonia.Controls/Automation/Peers/NavigationPageAutomationPeer.cs`

- Namespace(s): `Avalonia.Automation.Peers`
- `NavigationPageAutomationPeer` -> `public NavigationPageAutomationPeer(NavigationPage owner) : base(owner) {`
- `public class NavigationPageAutomationPeer : ControlAutomationPeer {`
- `NavigationPageAutomationPeer` -> `public new NavigationPage Owner => (NavigationPage)base.Owner;`

#### `src/Avalonia.Controls/Automation/Peers/TabbedPageAutomationPeer.cs`

- Namespace(s): `Avalonia.Automation.Peers`
- `TabbedPageAutomationPeer` -> `public TabbedPageAutomationPeer(TabbedPage owner) : base(owner) {`
- `public class TabbedPageAutomationPeer : ControlAutomationPeer {`
- `TabbedPageAutomationPeer` -> `public new TabbedPage Owner => (TabbedPage)base.Owner;`

#### `src/Avalonia.Controls/CalendarDatePicker/CalendarDatePicker.Properties.cs`

- `CalendarDatePicker` -> `public Media.IBrush? PlaceholderForeground {`
- `CalendarDatePicker` -> `public Media.IBrush? WatermarkForeground {`
- `CalendarDatePicker` -> `public bool UseFloatingPlaceholder {`
- `CalendarDatePicker` -> `public static readonly StyledProperty<Media.IBrush?> PlaceholderForegroundProperty = TextBox.PlaceholderForegroundProperty.AddOwner<CalendarDatePicker>();`
- `CalendarDatePicker` -> `public static readonly StyledProperty<Media.IBrush?> WatermarkForegroundProperty = PlaceholderForegroundProperty;`
- `CalendarDatePicker` -> `public static readonly StyledProperty<bool> UseFloatingPlaceholderProperty = TextBox.UseFloatingPlaceholderProperty.AddOwner<CalendarDatePicker>();`
- `CalendarDatePicker` -> `public static readonly StyledProperty<bool> UseFloatingWatermarkProperty = UseFloatingPlaceholderProperty;`
- `CalendarDatePicker` -> `public static readonly StyledProperty<string?> PlaceholderTextProperty = TextBox.PlaceholderTextProperty.AddOwner<CalendarDatePicker>();`
- `CalendarDatePicker` -> `public static readonly StyledProperty<string?> WatermarkProperty = PlaceholderTextProperty;`
- `CalendarDatePicker` -> `public string? PlaceholderText {`

#### `src/Avalonia.Controls/Chrome/IWindowDrawnDecorationsTemplate.cs`

- Namespace(s): `Avalonia.Controls.Chrome`
- `IWindowDrawnDecorationsTemplate` -> `new TemplateResult<WindowDrawnDecorationsContent> Build();`
- `public interface IWindowDrawnDecorationsTemplate : ITemplate {`

#### `src/Avalonia.Controls/Chrome/WindowDecorationProperties.cs`

- Namespace(s): `Avalonia.Controls.Chrome`
- `WindowDecorationProperties` -> `public static WindowDecorationsElementRole GetElementRole(Visual element) => element.GetValue(ElementRoleProperty);`
- `public static class WindowDecorationProperties {`
- `WindowDecorationProperties` -> `public static readonly AttachedProperty<WindowDecorationsElementRole> ElementRoleProperty = AvaloniaProperty.RegisterAttached<Visual, WindowDecorationsElementRole>("ElementRole", typeof(WindowDecorationProperties));`
- `WindowDecorationProperties` -> `public static void SetElementRole(Visual element, WindowDecorationsElementRole value) => element.SetValue(ElementRoleProperty, value);`

#### `src/Avalonia.Controls/Chrome/WindowDrawnDecorations.cs`

- Namespace(s): `Avalonia.Controls.Chrome`
- `WindowDrawnDecorations` -> `public IWindowDrawnDecorationsTemplate? Template {`
- `WindowDrawnDecorations` -> `public Thickness DefaultFrameThickness {`
- `WindowDrawnDecorations` -> `public Thickness DefaultShadowThickness {`
- `WindowDrawnDecorations` -> `public Thickness FrameThickness {`
- `WindowDrawnDecorations` -> `public Thickness ShadowThickness {`
- `WindowDrawnDecorations` -> `public WindowDrawnDecorationsContent? Content { get; private set; }`
- `WindowDrawnDecorations` -> `public bool HasBorder {`
- `WindowDrawnDecorations` -> `public bool HasShadow {`
- `WindowDrawnDecorations` -> `public bool HasTitleBar {`
- `public class WindowDrawnDecorations : StyledElement {`
- `WindowDrawnDecorations` -> `public double DefaultTitleBarHeight {`
- `WindowDrawnDecorations` -> `public double TitleBarHeight {`
- `WindowDrawnDecorations` -> `public static readonly DirectProperty<WindowDrawnDecorations, Thickness> FrameThicknessProperty = AvaloniaProperty.RegisterDirect<WindowDrawnDecorations, Thickness>( nameof(FrameThickness), o => o.FrameThickness);`
- `WindowDrawnDecorations` -> `public static readonly DirectProperty<WindowDrawnDecorations, Thickness> ShadowThicknessProperty = AvaloniaProperty.RegisterDirect<WindowDrawnDecorations, Thickness>( nameof(ShadowThickness), o => o.ShadowThickness);`
- `WindowDrawnDecorations` -> `public static readonly DirectProperty<WindowDrawnDecorations, bool> HasBorderProperty = AvaloniaProperty.RegisterDirect<WindowDrawnDecorations, bool>( nameof(HasBorder), o => o.HasBorder);`
- `WindowDrawnDecorations` -> `public static readonly DirectProperty<WindowDrawnDecorations, bool> HasShadowProperty = AvaloniaProperty.RegisterDirect<WindowDrawnDecorations, bool>( nameof(HasShadow), o => o.HasShadow);`
- `WindowDrawnDecorations` -> `public static readonly DirectProperty<WindowDrawnDecorations, bool> HasTitleBarProperty = AvaloniaProperty.RegisterDirect<WindowDrawnDecorations, bool>( nameof(HasTitleBar), o => o.HasTitleBar);`
- `WindowDrawnDecorations` -> `public static readonly DirectProperty<WindowDrawnDecorations, double> TitleBarHeightProperty = AvaloniaProperty.RegisterDirect<WindowDrawnDecorations, double>( nameof(TitleBarHeight), o => o.TitleBarHeight);`
- `WindowDrawnDecorations` -> `public static readonly StyledProperty<IWindowDrawnDecorationsTemplate?> TemplateProperty = AvaloniaProperty.Register<WindowDrawnDecorations, IWindowDrawnDecorationsTemplate?>(nameof(Template));`
- `WindowDrawnDecorations` -> `public static readonly StyledProperty<Thickness> DefaultFrameThicknessProperty = AvaloniaProperty.Register<WindowDrawnDecorations, Thickness>(nameof(DefaultFrameThickness));`
- `WindowDrawnDecorations` -> `public static readonly StyledProperty<Thickness> DefaultShadowThicknessProperty = AvaloniaProperty.Register<WindowDrawnDecorations, Thickness>(nameof(DefaultShadowThickness));`
- `WindowDrawnDecorations` -> `public static readonly StyledProperty<double> DefaultTitleBarHeightProperty = AvaloniaProperty.Register<WindowDrawnDecorations, double>(nameof(DefaultTitleBarHeight));`
- `WindowDrawnDecorations` -> `public static readonly StyledProperty<string?> TitleProperty = AvaloniaProperty.Register<WindowDrawnDecorations, string?>(nameof(Title));`
- `WindowDrawnDecorations` -> `public string? Title {`

#### `src/Avalonia.Controls/Chrome/WindowDrawnDecorationsContent.cs`

- Namespace(s): `Avalonia.Controls.Chrome`
- `WindowDrawnDecorationsContent` -> `public Control? FullscreenPopover {`
- `WindowDrawnDecorationsContent` -> `public Control? Overlay {`
- `WindowDrawnDecorationsContent` -> `public Control? Underlay {`
- `public class WindowDrawnDecorationsContent : StyledElement {`

#### `src/Avalonia.Controls/ComboBox.cs`

- `ComboBox` -> `public override bool UpdateSelectionFromEvent(Control container, RoutedEventArgs eventArgs) {`

#### `src/Avalonia.Controls/CommandBar/AppBarButton.cs`

- `AppBarButton` -> `public CommandBarDefaultLabelPosition LabelPosition {`
- `AppBarButton` -> `public bool IsCompact {`
- `AppBarButton` -> `public bool IsInOverflow {`
- `public class AppBarButton : Button, ICommandBarElement {`
- `AppBarButton` -> `public int DynamicOverflowOrder {`
- `AppBarButton` -> `public object? Icon {`
- `AppBarButton` -> `public static readonly StyledProperty<CommandBarDefaultLabelPosition> LabelPositionProperty = AvaloniaProperty.Register<AppBarButton, CommandBarDefaultLabelPosition>(nameof(LabelPosition), CommandBarDefaultLabelPosition.Bottom);`
- `AppBarButton` -> `public static readonly StyledProperty<bool> IsCompactProperty = AvaloniaProperty.Register<AppBarButton, bool>(nameof(IsCompact));`
- `AppBarButton` -> `public static readonly StyledProperty<bool> IsInOverflowProperty = AvaloniaProperty.Register<AppBarButton, bool>(nameof(IsInOverflow));`
- `AppBarButton` -> `public static readonly StyledProperty<int> DynamicOverflowOrderProperty = AvaloniaProperty.Register<AppBarButton, int>(nameof(DynamicOverflowOrder));`
- `AppBarButton` -> `public static readonly StyledProperty<object?> IconProperty = AvaloniaProperty.Register<AppBarButton, object?>(nameof(Icon));`
- `AppBarButton` -> `public static readonly StyledProperty<string?> LabelProperty = AvaloniaProperty.Register<AppBarButton, string?>(nameof(Label));`
- `AppBarButton` -> `public string? Label {`

#### `src/Avalonia.Controls/CommandBar/AppBarSeparator.cs`

- `AppBarSeparator` -> `public bool IsCompact {`
- `AppBarSeparator` -> `public bool IsInOverflow {`
- `public class AppBarSeparator : TemplatedControl, ICommandBarElement {`
- `AppBarSeparator` -> `public static readonly StyledProperty<bool> IsCompactProperty = AvaloniaProperty.Register<AppBarSeparator, bool>(nameof(IsCompact));`
- `AppBarSeparator` -> `public static readonly StyledProperty<bool> IsInOverflowProperty = AvaloniaProperty.Register<AppBarSeparator, bool>(nameof(IsInOverflow));`

#### `src/Avalonia.Controls/CommandBar/AppBarToggleButton.cs`

- `AppBarToggleButton` -> `public CommandBarDefaultLabelPosition LabelPosition {`
- `AppBarToggleButton` -> `public bool IsCompact {`
- `AppBarToggleButton` -> `public bool IsInOverflow {`
- `public class AppBarToggleButton : ToggleButton, ICommandBarElement {`
- `AppBarToggleButton` -> `public int DynamicOverflowOrder {`
- `AppBarToggleButton` -> `public object? Icon {`
- `AppBarToggleButton` -> `public static readonly StyledProperty<CommandBarDefaultLabelPosition> LabelPositionProperty = AvaloniaProperty.Register<AppBarToggleButton, CommandBarDefaultLabelPosition>(nameof(LabelPosition), CommandBarDefaultLabelPosition.Bottom);`
- `AppBarToggleButton` -> `public static readonly StyledProperty<bool> IsCompactProperty = AvaloniaProperty.Register<AppBarToggleButton, bool>(nameof(IsCompact));`
- `AppBarToggleButton` -> `public static readonly StyledProperty<bool> IsInOverflowProperty = AvaloniaProperty.Register<AppBarToggleButton, bool>(nameof(IsInOverflow));`
- `AppBarToggleButton` -> `public static readonly StyledProperty<int> DynamicOverflowOrderProperty = AvaloniaProperty.Register<AppBarToggleButton, int>(nameof(DynamicOverflowOrder));`
- `AppBarToggleButton` -> `public static readonly StyledProperty<object?> IconProperty = AvaloniaProperty.Register<AppBarToggleButton, object?>(nameof(Icon));`
- `AppBarToggleButton` -> `public static readonly StyledProperty<string?> LabelProperty = AvaloniaProperty.Register<AppBarToggleButton, string?>(nameof(Label));`
- `AppBarToggleButton` -> `public string? Label {`

#### `src/Avalonia.Controls/CommandBar/CommandBar.cs`

- `CommandBar` -> `public CommandBar() {`
- `CommandBar` -> `public CommandBarDefaultLabelPosition DefaultLabelPosition {`
- `CommandBar` -> `public CommandBarOverflowButtonVisibility OverflowButtonVisibility {`
- `CommandBar` -> `public IList<ICommandBarElement> PrimaryCommands {`
- `CommandBar` -> `public IList<ICommandBarElement> SecondaryCommands {`
- `CommandBar` -> `public ReadOnlyObservableCollection<ICommandBarElement> OverflowItems { get; }`
- `CommandBar` -> `public ReadOnlyObservableCollection<ICommandBarElement> VisiblePrimaryCommands { get; }`
- `CommandBar` -> `public bool HasSecondaryCommands {`
- `CommandBar` -> `public bool IsDynamicOverflowEnabled {`
- `CommandBar` -> `public bool IsOpen {`
- `CommandBar` -> `public bool IsOverflowButtonVisible {`
- `CommandBar` -> `public bool IsSticky {`
- `public class CommandBar : TemplatedControl {`
- `CommandBar` -> `public double ItemWidthBottom {`
- `CommandBar` -> `public double ItemWidthCollapsed {`
- `CommandBar` -> `public double ItemWidthRight {`
- `CommandBar` -> `public event EventHandler<RoutedEventArgs>? Closed {`
- `CommandBar` -> `public event EventHandler<RoutedEventArgs>? Closing {`
- `CommandBar` -> `public event EventHandler<RoutedEventArgs>? Opened {`
- `CommandBar` -> `public event EventHandler<RoutedEventArgs>? Opening {`
- `CommandBar` -> `public object? Content {`
- `CommandBar` -> `public static readonly DirectProperty<CommandBar, bool> HasSecondaryCommandsProperty = AvaloniaProperty.RegisterDirect<CommandBar, bool>( nameof(HasSecondaryCommands), o => o._hasSecondaryCommands);`
- `CommandBar` -> `public static readonly DirectProperty<CommandBar, bool> IsOverflowButtonVisibleProperty = AvaloniaProperty.RegisterDirect<CommandBar, bool>( nameof(IsOverflowButtonVisible), o => o._isOverflowButtonVisible);`
- `CommandBar` -> `public static readonly RoutedEvent<RoutedEventArgs> ClosedEvent = RoutedEvent.Register<CommandBar, RoutedEventArgs>(nameof(Closed), RoutingStrategies.Bubble);`
- `CommandBar` -> `public static readonly RoutedEvent<RoutedEventArgs> ClosingEvent = RoutedEvent.Register<CommandBar, RoutedEventArgs>(nameof(Closing), RoutingStrategies.Bubble);`
- `CommandBar` -> `public static readonly RoutedEvent<RoutedEventArgs> OpenedEvent = RoutedEvent.Register<CommandBar, RoutedEventArgs>(nameof(Opened), RoutingStrategies.Bubble);`
- `CommandBar` -> `public static readonly RoutedEvent<RoutedEventArgs> OpeningEvent = RoutedEvent.Register<CommandBar, RoutedEventArgs>(nameof(Opening), RoutingStrategies.Bubble);`
- `CommandBar` -> `public static readonly StyledProperty<CommandBarDefaultLabelPosition> DefaultLabelPositionProperty = AvaloniaProperty.Register<CommandBar, CommandBarDefaultLabelPosition>(nameof(DefaultLabelPosition), CommandBarDefaultLabelPosition.Bottom);`
- `CommandBar` -> `public static readonly StyledProperty<CommandBarOverflowButtonVisibility> OverflowButtonVisibilityProperty = AvaloniaProperty.Register<CommandBar, CommandBarOverflowButtonVisibility>(nameof(OverflowButtonVisibility), CommandBarOverflowButtonVisibility.Auto);`
- `CommandBar` -> `public static readonly StyledProperty<IList<ICommandBarElement>?> PrimaryCommandsProperty = AvaloniaProperty.Register<CommandBar, IList<ICommandBarElement>?>(nameof(PrimaryCommands));`
- `CommandBar` -> `public static readonly StyledProperty<IList<ICommandBarElement>?> SecondaryCommandsProperty = AvaloniaProperty.Register<CommandBar, IList<ICommandBarElement>?>(nameof(SecondaryCommands));`
- `CommandBar` -> `public static readonly StyledProperty<bool> IsDynamicOverflowEnabledProperty = AvaloniaProperty.Register<CommandBar, bool>(nameof(IsDynamicOverflowEnabled));`
- `CommandBar` -> `public static readonly StyledProperty<bool> IsOpenProperty = AvaloniaProperty.Register<CommandBar, bool>(nameof(IsOpen));`
- `CommandBar` -> `public static readonly StyledProperty<bool> IsStickyProperty = AvaloniaProperty.Register<CommandBar, bool>(nameof(IsSticky));`
- `CommandBar` -> `public static readonly StyledProperty<double> ItemWidthBottomProperty = AvaloniaProperty.Register<CommandBar, double>(nameof(ItemWidthBottom), defaultValue: 70d);`
- `CommandBar` -> `public static readonly StyledProperty<double> ItemWidthCollapsedProperty = AvaloniaProperty.Register<CommandBar, double>(nameof(ItemWidthCollapsed), defaultValue: 42d);`
- `CommandBar` -> `public static readonly StyledProperty<double> ItemWidthRightProperty = AvaloniaProperty.Register<CommandBar, double>(nameof(ItemWidthRight), defaultValue: 102d);`
- `CommandBar` -> `public static readonly StyledProperty<object?> ContentProperty = ContentControl.ContentProperty.AddOwner<CommandBar>();`

#### `src/Avalonia.Controls/CommandBar/CommandBarDefaultLabelPosition.cs`

- `public enum CommandBarDefaultLabelPosition {`

#### `src/Avalonia.Controls/CommandBar/CommandBarOverflowButtonVisibility.cs`

- `public enum CommandBarOverflowButtonVisibility {`

#### `src/Avalonia.Controls/CommandBar/ICommandBarElement.cs`

- `ICommandBarElement` -> `bool IsCompact { get; set; }`
- `ICommandBarElement` -> `bool IsInOverflow { get; set; }`
- `public interface ICommandBarElement {`

#### `src/Avalonia.Controls/Converters/TreeViewItemIndentConverter.cs`

- Namespace(s): `Avalonia.Controls.Converters`
- `public class TreeViewItemIndentConverter : IMultiValueConverter {`
- `TreeViewItemIndentConverter` -> `public object? Convert(IList<object?> values, Type targetType, object? parameter, CultureInfo culture) {`
- `TreeViewItemIndentConverter` -> `public static readonly TreeViewItemIndentConverter Instance = new();`

#### `src/Avalonia.Controls/Design.cs`

- `Design` -> `public static Control CreatePreviewWithControl(object target) {`
- `Design` -> `public static Control? GetPreviewWith(IDataTemplate target) {`
- `Design` -> `public static Control? GetPreviewWith(IStyle target) {`
- `Design` -> `public static object? GetDataContext(Control control) {`
- `Design` -> `public static object? GetDataContext(IDataTemplate control) {`
- `Design` -> `public static readonly AttachedProperty<object?> DataContextProperty = AvaloniaProperty .RegisterAttached<Control, object?>("DataContext", typeof (Design));`
- `Design` -> `public static void SetDataContext(Control control, object? value) {`
- `Design` -> `public static void SetDataContext(IDataTemplate control, object? value) {`
- `Design` -> `public static void SetPreviewWith(AvaloniaObject target, ITemplate<Control>? template) {`
- `Design` -> `public static void SetPreviewWith(IDataTemplate target, Control? control) {`
- `Design` -> `public static void SetPreviewWith(IDataTemplate target, ITemplate<Control>? template) {`
- `Design` -> `public static void SetPreviewWith(IStyle target, Control? control) {`
- `Design` -> `public static void SetPreviewWith(IStyle target, ITemplate<Control>? template) {`
- `Design` -> `public static void SetPreviewWith(ResourceDictionary target, ITemplate<Control>? template) {`

#### `src/Avalonia.Controls/Documents/Inline.cs`

- `Inline` -> `public static readonly AttachedProperty<TextDecorationCollection?> TextDecorationsProperty = AvaloniaProperty.RegisterAttached<Inline, Inline, TextDecorationCollection?>( nameof(TextDecorations), inherits: true);`

#### `src/Avalonia.Controls/Documents/TextElement.cs`

- `TextElement` -> `public double LetterSpacing {`
- `TextElement` -> `public static double GetLetterSpacing(Control control) {`
- `TextElement` -> `public static readonly AttachedProperty<double> LetterSpacingProperty = AvaloniaProperty.RegisterAttached<TextElement, Control, double>( name: nameof(LetterSpacing), defaultValue: 0.0, inherits: true);`
- `TextElement` -> `public static void SetLetterSpacing(Control control, double value) {`

#### `src/Avalonia.Controls/Embedding/Offscreen/OffscreenTopLevelImpl.cs`

- `OffscreenTopLevelImplBase` -> `public abstract IPlatformRenderSurface[] Surfaces { get; }`

#### `src/Avalonia.Controls/ExperimentalAcrylicBorder.cs`

- `ExperimentalAcrylicBorder` -> `public ExperimentalAcrylicMaterial? Material {`
- `ExperimentalAcrylicBorder` -> `public static readonly StyledProperty<ExperimentalAcrylicMaterial?> MaterialProperty = AvaloniaProperty.Register<ExperimentalAcrylicBorder, ExperimentalAcrylicMaterial?>(nameof(Material));`

#### `src/Avalonia.Controls/Flyouts/PopupFlyoutBase.cs`

- `PopupFlyoutBase` -> `public Popup Popup => _popupLazy.Value;`

#### `src/Avalonia.Controls/GroupBox.cs`

- Namespace(s): `Avalonia.Controls`
- `public class GroupBox : HeaderedContentControl {`

#### `src/Avalonia.Controls/HotkeyManager.cs`

- `HotKeyManager` -> `public static void SetHotKey(AvaloniaObject target, KeyGesture? value) => target.SetValue(HotKeyProperty, value);`

#### `src/Avalonia.Controls/ItemsControl.cs`

- `ItemsControl` -> `public BindingBase? DisplayMemberBinding {`
- `ItemsControl` -> `public ItemContainerGenerator ItemContainerGenerator => _itemContainerGenerator ??= new ItemContainerGenerator(this);`
- `ItemsControl` -> `public static readonly StyledProperty<BindingBase?> DisplayMemberBindingProperty = AvaloniaProperty.Register<ItemsControl, BindingBase?>(nameof(DisplayMemberBinding));`

#### `src/Avalonia.Controls/NativeDock.cs`

- `NativeDock` -> `public static NativeMenu? GetMenu(AvaloniaObject o) => o.GetValue(MenuProperty);`
- `public static class NativeDock {`
- `NativeDock` -> `public static readonly AttachedProperty<NativeMenu?> MenuProperty = AvaloniaProperty.RegisterAttached<AvaloniaObject, NativeMenu?>("Menu", typeof(NativeDock));`
- `NativeDock` -> `public static void SetMenu(AvaloniaObject o, NativeMenu? menu) => o.SetValue(MenuProperty, menu);`

#### `src/Avalonia.Controls/NativeMenuItem.cs`

- `NativeMenuItem` -> `public MenuItemToggleType ToggleType {`
- `NativeMenuItem` -> `public static readonly StyledProperty<MenuItemToggleType> ToggleTypeProperty = AvaloniaProperty.Register<NativeMenuItem, MenuItemToggleType>(nameof(ToggleType));`

#### `src/Avalonia.Controls/NumericUpDown/NumericUpDown.cs`

- `NumericUpDown` -> `public Media.IBrush? PlaceholderForeground {`
- `NumericUpDown` -> `public Media.IBrush? WatermarkForeground {`
- `NumericUpDown` -> `public static readonly StyledProperty<Media.IBrush?> PlaceholderForegroundProperty = TextBox.PlaceholderForegroundProperty.AddOwner<NumericUpDown>();`
- `NumericUpDown` -> `public static readonly StyledProperty<Media.IBrush?> WatermarkForegroundProperty = PlaceholderForegroundProperty;`
- `NumericUpDown` -> `public static readonly StyledProperty<string?> PlaceholderTextProperty = AvaloniaProperty.Register<NumericUpDown, string?>(nameof(PlaceholderText));`
- `NumericUpDown` -> `public static readonly StyledProperty<string?> WatermarkProperty = PlaceholderTextProperty;`
- `NumericUpDown` -> `public string? PlaceholderText {`

#### `src/Avalonia.Controls/Page/BarLayoutBehavior.cs`

- `public enum BarLayoutBehavior {`

#### `src/Avalonia.Controls/Page/ContentPage.cs`

- `ContentPage` -> `public HorizontalAlignment HorizontalContentAlignment {`
- `ContentPage` -> `public IDataTemplate? ContentTemplate {`
- `ContentPage` -> `public VerticalAlignment VerticalContentAlignment {`
- `ContentPage` -> `public bool AutomaticallyApplySafeAreaPadding {`
- `public class ContentPage : Page {`
- `ContentPage` -> `public object? BottomCommandBar {`
- `ContentPage` -> `public object? Content {`
- `ContentPage` -> `public object? TopCommandBar {`
- `ContentPage` -> `public static readonly StyledProperty<HorizontalAlignment> HorizontalContentAlignmentProperty = ContentControl.HorizontalContentAlignmentProperty.AddOwner<ContentPage>();`
- `ContentPage` -> `public static readonly StyledProperty<IDataTemplate?> ContentTemplateProperty = ContentControl.ContentTemplateProperty.AddOwner<ContentPage>();`
- `ContentPage` -> `public static readonly StyledProperty<VerticalAlignment> VerticalContentAlignmentProperty = ContentControl.VerticalContentAlignmentProperty.AddOwner<ContentPage>();`
- `ContentPage` -> `public static readonly StyledProperty<bool> AutomaticallyApplySafeAreaPaddingProperty = AvaloniaProperty.Register<ContentPage, bool>(nameof(AutomaticallyApplySafeAreaPadding), defaultValue: true);`
- `ContentPage` -> `public static readonly StyledProperty<object?> BottomCommandBarProperty = AvaloniaProperty.Register<ContentPage, object?>(nameof(BottomCommandBar));`
- `ContentPage` -> `public static readonly StyledProperty<object?> ContentProperty = ContentControl.ContentProperty.AddOwner<ContentPage>();`
- `ContentPage` -> `public static readonly StyledProperty<object?> TopCommandBarProperty = AvaloniaProperty.Register<ContentPage, object?>(nameof(TopCommandBar));`

#### `src/Avalonia.Controls/Page/DrawerBehavior.cs`

- `public enum DrawerBehavior {`

#### `src/Avalonia.Controls/Page/DrawerClosingEventArgs.cs`

- `DrawerClosingEventArgs` -> `public bool Cancel { get; set; }`
- `public class DrawerClosingEventArgs : RoutedEventArgs {`

#### `src/Avalonia.Controls/Page/DrawerLayoutBehavior.cs`

- `public enum DrawerLayoutBehavior {`

#### `src/Avalonia.Controls/Page/DrawerPage.cs`

- `DrawerPage` -> `public DrawerBehavior DrawerBehavior {`
- `DrawerPage` -> `public DrawerLayoutBehavior DrawerLayoutBehavior {`
- `DrawerPage` -> `public DrawerPage() {`
- `DrawerPage` -> `public DrawerPlacement DrawerPlacement {`
- `DrawerPage` -> `public HorizontalAlignment HorizontalContentAlignment {`
- `DrawerPage` -> `public IBrush? BackdropBrush {`
- `DrawerPage` -> `public IBrush? DrawerBackground {`
- `DrawerPage` -> `public IBrush? DrawerFooterBackground {`
- `DrawerPage` -> `public IBrush? DrawerFooterForeground {`
- `DrawerPage` -> `public IBrush? DrawerHeaderBackground {`
- `DrawerPage` -> `public IBrush? DrawerHeaderForeground {`
- `DrawerPage` -> `public IDataTemplate? ContentTemplate {`
- `DrawerPage` -> `public IDataTemplate? DrawerTemplate {`
- `DrawerPage` -> `public SplitViewDisplayMode DisplayMode {`
- `DrawerPage` -> `public VerticalAlignment VerticalContentAlignment {`
- `DrawerPage` -> `public bool IsGestureEnabled {`
- `DrawerPage` -> `public bool IsOpen {`
- `public class DrawerPage : Page {`
- `DrawerPage` -> `public double CompactDrawerLength {`
- `DrawerPage` -> `public double DrawerBreakpointWidth {`
- `DrawerPage` -> `public double DrawerLength {`
- `DrawerPage` -> `public event EventHandler<DrawerClosingEventArgs>? Closing {`
- `DrawerPage` -> `public event EventHandler<RoutedEventArgs>? Closed {`
- `DrawerPage` -> `public event EventHandler<RoutedEventArgs>? Opened {`
- `DrawerPage` -> `public object? Content {`
- `DrawerPage` -> `public object? Drawer {`
- `DrawerPage` -> `public object? DrawerFooter {`
- `DrawerPage` -> `public object? DrawerHeader {`
- `DrawerPage` -> `public object? DrawerIcon {`
- `DrawerPage` -> `public static readonly RoutedEvent<DrawerClosingEventArgs> ClosingEvent = RoutedEvent.Register<DrawerPage, DrawerClosingEventArgs>(nameof(Closing), RoutingStrategies.Bubble);`
- `DrawerPage` -> `public static readonly RoutedEvent<RoutedEventArgs> ClosedEvent = RoutedEvent.Register<DrawerPage, RoutedEventArgs>(nameof(Closed), RoutingStrategies.Bubble);`
- `DrawerPage` -> `public static readonly RoutedEvent<RoutedEventArgs> OpenedEvent = RoutedEvent.Register<DrawerPage, RoutedEventArgs>(nameof(Opened), RoutingStrategies.Bubble);`
- `DrawerPage` -> `public static readonly StyledProperty<DrawerBehavior> DrawerBehaviorProperty = AvaloniaProperty.Register<DrawerPage, DrawerBehavior>(nameof(DrawerBehavior), DrawerBehavior.Auto);`
- `DrawerPage` -> `public static readonly StyledProperty<DrawerLayoutBehavior> DrawerLayoutBehaviorProperty = AvaloniaProperty.Register<DrawerPage, DrawerLayoutBehavior>(nameof(DrawerLayoutBehavior), DrawerLayoutBehavior.Overlay);`
- `DrawerPage` -> `public static readonly StyledProperty<DrawerPlacement> DrawerPlacementProperty = AvaloniaProperty.Register<DrawerPage, DrawerPlacement>(nameof(DrawerPlacement), DrawerPlacement.Left);`
- `DrawerPage` -> `public static readonly StyledProperty<HorizontalAlignment> HorizontalContentAlignmentProperty = ContentControl.HorizontalContentAlignmentProperty.AddOwner<DrawerPage>();`
- `DrawerPage` -> `public static readonly StyledProperty<IBrush?> BackdropBrushProperty = AvaloniaProperty.Register<DrawerPage, IBrush?>(nameof(BackdropBrush));`
- `DrawerPage` -> `public static readonly StyledProperty<IBrush?> DrawerBackgroundProperty = AvaloniaProperty.Register<DrawerPage, IBrush?>(nameof(DrawerBackground));`
- `DrawerPage` -> `public static readonly StyledProperty<IBrush?> DrawerFooterBackgroundProperty = AvaloniaProperty.Register<DrawerPage, IBrush?>(nameof(DrawerFooterBackground));`
- `DrawerPage` -> `public static readonly StyledProperty<IBrush?> DrawerFooterForegroundProperty = AvaloniaProperty.Register<DrawerPage, IBrush?>(nameof(DrawerFooterForeground));`
- `DrawerPage` -> `public static readonly StyledProperty<IBrush?> DrawerHeaderBackgroundProperty = AvaloniaProperty.Register<DrawerPage, IBrush?>(nameof(DrawerHeaderBackground));`
- `DrawerPage` -> `public static readonly StyledProperty<IBrush?> DrawerHeaderForegroundProperty = AvaloniaProperty.Register<DrawerPage, IBrush?>(nameof(DrawerHeaderForeground));`
- `DrawerPage` -> `public static readonly StyledProperty<IDataTemplate?> ContentTemplateProperty = AvaloniaProperty.Register<DrawerPage, IDataTemplate?>(nameof(ContentTemplate), s_defaultPageDataTemplate);`
- `DrawerPage` -> `public static readonly StyledProperty<IDataTemplate?> DrawerTemplateProperty = AvaloniaProperty.Register<DrawerPage, IDataTemplate?>(nameof(DrawerTemplate));`
- `DrawerPage` -> `public static readonly StyledProperty<SplitViewDisplayMode> DisplayModeProperty = SplitView.DisplayModeProperty.AddOwner<DrawerPage>();`
- `DrawerPage` -> `public static readonly StyledProperty<VerticalAlignment> VerticalContentAlignmentProperty = ContentControl.VerticalContentAlignmentProperty.AddOwner<DrawerPage>();`
- `DrawerPage` -> `public static readonly StyledProperty<bool> IsGestureEnabledProperty = AvaloniaProperty.Register<DrawerPage, bool>(nameof(IsGestureEnabled), true);`
- `DrawerPage` -> `public static readonly StyledProperty<bool> IsOpenProperty = AvaloniaProperty.Register<DrawerPage, bool>(nameof(IsOpen), coerce: CoerceIsOpen);`
- `DrawerPage` -> `public static readonly StyledProperty<double> CompactDrawerLengthProperty = AvaloniaProperty.Register<DrawerPage, double>(nameof(CompactDrawerLength), 48, validate: ValidateLength);`
- `DrawerPage` -> `public static readonly StyledProperty<double> DrawerBreakpointWidthProperty = AvaloniaProperty.Register<DrawerPage, double>(nameof(DrawerBreakpointWidth), 0d);`
- `DrawerPage` -> `public static readonly StyledProperty<double> DrawerLengthProperty = AvaloniaProperty.Register<DrawerPage, double>(nameof(DrawerLength), 320, validate: ValidateLength);`
- `DrawerPage` -> `public static readonly StyledProperty<object?> ContentProperty = AvaloniaProperty.Register<DrawerPage, object?>(nameof(Content));`
- `DrawerPage` -> `public static readonly StyledProperty<object?> DrawerFooterProperty = AvaloniaProperty.Register<DrawerPage, object?>(nameof(DrawerFooter));`
- `DrawerPage` -> `public static readonly StyledProperty<object?> DrawerHeaderProperty = AvaloniaProperty.Register<DrawerPage, object?>(nameof(DrawerHeader));`
- `DrawerPage` -> `public static readonly StyledProperty<object?> DrawerIconProperty = AvaloniaProperty.Register<DrawerPage, object?>(nameof(DrawerIcon));`
- `DrawerPage` -> `public static readonly StyledProperty<object?> DrawerProperty = AvaloniaProperty.Register<DrawerPage, object?>(nameof(Drawer));`

#### `src/Avalonia.Controls/Page/DrawerPlacement.cs`

- `public enum DrawerPlacement {`

#### `src/Avalonia.Controls/Page/INavigation.cs`

- `INavigation` -> `IReadOnlyList<Page> ModalStack { get; }`
- `INavigation` -> `IReadOnlyList<Page> NavigationStack { get; }`
- `INavigation` -> `Task PopAllModalsAsync();`
- `INavigation` -> `Task PopAllModalsAsync(IPageTransition? transition);`
- `INavigation` -> `Task PopToPageAsync(Page page);`
- `INavigation` -> `Task PopToPageAsync(Page page, IPageTransition? transition);`
- `INavigation` -> `Task PopToRootAsync();`
- `INavigation` -> `Task PopToRootAsync(IPageTransition? transition);`
- `INavigation` -> `Task PushAsync(Page page);`
- `INavigation` -> `Task PushAsync(Page page, IPageTransition? transition);`
- `INavigation` -> `Task PushModalAsync(Page page);`
- `INavigation` -> `Task PushModalAsync(Page page, IPageTransition? transition);`
- `INavigation` -> `Task ReplaceAsync(Page page);`
- `INavigation` -> `Task ReplaceAsync(Page page, IPageTransition? transition);`
- `INavigation` -> `Task<Page?> PopAsync();`
- `INavigation` -> `Task<Page?> PopAsync(IPageTransition? transition);`
- `INavigation` -> `Task<Page?> PopModalAsync();`
- `INavigation` -> `Task<Page?> PopModalAsync(IPageTransition? transition);`
- `INavigation` -> `bool CanGoBack { get; }`
- `INavigation` -> `int StackDepth { get; }`
- `public interface INavigation {`
- `INavigation` -> `void InsertPage(Page page, Page before);`
- `INavigation` -> `void RemovePage(Page page);`

#### `src/Avalonia.Controls/Page/ModalPoppedEventArgs.cs`

- `ModalPoppedEventArgs` -> `public ModalPoppedEventArgs(Page modal) {`
- `ModalPoppedEventArgs` -> `public Page Modal { get; }`
- `public class ModalPoppedEventArgs : EventArgs {`

#### `src/Avalonia.Controls/Page/ModalPushedEventArgs.cs`

- `ModalPushedEventArgs` -> `public ModalPushedEventArgs(Page modal) {`
- `ModalPushedEventArgs` -> `public Page Modal { get; }`
- `public class ModalPushedEventArgs : EventArgs {`

#### `src/Avalonia.Controls/Page/MultiPage.cs`

- `MultiPage` -> `public IDataTemplate? PageTemplate {`
- `MultiPage` -> `public IEnumerable<Page>? Pages {`
- `public abstract class MultiPage : Page {`
- `MultiPage` -> `public event EventHandler<NotifyCollectionChangedEventArgs>? PagesChanged;`
- `MultiPage` -> `public event EventHandler? CurrentPageChanged;`
- `MultiPage` -> `public static readonly StyledProperty<IDataTemplate?> PageTemplateProperty = AvaloniaProperty.Register<MultiPage, IDataTemplate?>(nameof(PageTemplate), new DefaultPageDataTemplate());`
- `MultiPage` -> `public static readonly StyledProperty<IEnumerable<Page>?> PagesProperty = AvaloniaProperty.Register<MultiPage, IEnumerable<Page>?>(nameof(Pages));`

#### `src/Avalonia.Controls/Page/NavigatedFromEventArgs.cs`

- `NavigatedFromEventArgs` -> `public NavigatedFromEventArgs(Page? destinationPage, NavigationType navigationType) {`
- `NavigatedFromEventArgs` -> `public NavigationType NavigationType { get; }`
- `NavigatedFromEventArgs` -> `public Page? DestinationPage { get; }`
- `public class NavigatedFromEventArgs : EventArgs {`

#### `src/Avalonia.Controls/Page/NavigatedToEventArgs.cs`

- `NavigatedToEventArgs` -> `public NavigatedToEventArgs(Page? previousPage, NavigationType navigationType) {`
- `NavigatedToEventArgs` -> `public NavigationType NavigationType { get; }`
- `NavigatedToEventArgs` -> `public Page? PreviousPage { get; }`
- `public class NavigatedToEventArgs : EventArgs {`

#### `src/Avalonia.Controls/Page/NavigatingFromEventArgs.cs`

- `NavigatingFromEventArgs` -> `public NavigatingFromEventArgs(Page? destinationPage, NavigationType navigationType) {`
- `NavigatingFromEventArgs` -> `public NavigationType NavigationType { get; }`
- `NavigatingFromEventArgs` -> `public Page? DestinationPage { get; }`
- `NavigatingFromEventArgs` -> `public bool Cancel { get; set; }`
- `public class NavigatingFromEventArgs : EventArgs {`

#### `src/Avalonia.Controls/Page/NavigationEventArgs.cs`

- `NavigationEventArgs` -> `public NavigationEventArgs(Page page, NavigationType navigationType) {`
- `NavigationEventArgs` -> `public NavigationType NavigationType { get; }`
- `NavigationEventArgs` -> `public Page Page { get; }`
- `public class NavigationEventArgs : EventArgs {`

#### `src/Avalonia.Controls/Page/NavigationPage.cs`

- `NavigationPage` -> `public IPageTransition? ModalTransition {`
- `NavigationPage` -> `public IPageTransition? PageTransition {`
- `NavigationPage` -> `public IReadOnlyList<Page> ModalStack {`
- `NavigationPage` -> `public IReadOnlyList<Page> NavigationStack {`
- `NavigationPage` -> `public NavigationPage() {`
- `NavigationPage` -> `public async Task PopAllModalsAsync() {`
- `NavigationPage` -> `public async Task PopAllModalsAsync(IPageTransition? transition) {`
- `NavigationPage` -> `public async Task PopToPageAsync(Page page) {`
- `NavigationPage` -> `public async Task PopToPageAsync(Page page, IPageTransition? transition) {`
- `NavigationPage` -> `public async Task PopToRootAsync() {`
- `NavigationPage` -> `public async Task PopToRootAsync(IPageTransition? transition) {`
- `NavigationPage` -> `public async Task PushAsync(Page page) {`
- `NavigationPage` -> `public async Task PushAsync(Page page, IPageTransition? transition) {`
- `NavigationPage` -> `public async Task PushModalAsync(Page page) {`
- `NavigationPage` -> `public async Task PushModalAsync(Page page, IPageTransition? transition) {`
- `NavigationPage` -> `public async Task ReplaceAsync(Page page) {`
- `NavigationPage` -> `public async Task ReplaceAsync(Page page, IPageTransition? transition) {`
- `NavigationPage` -> `public async Task<Page?> PopAsync() {`
- `NavigationPage` -> `public async Task<Page?> PopAsync(IPageTransition? transition) {`
- `NavigationPage` -> `public async Task<Page?> PopModalAsync() {`
- `NavigationPage` -> `public async Task<Page?> PopModalAsync(IPageTransition? transition) {`
- `NavigationPage` -> `public bool CanGoBack => _canGoBack;`
- `NavigationPage` -> `public bool HasShadow {`
- `NavigationPage` -> `public bool IsBackButtonVisible {`
- `NavigationPage` -> `public bool IsGestureEnabled {`
- `NavigationPage` -> `public bool? IsBackButtonEffectivelyVisible {`
- `public class NavigationPage : MultiPage, INavigation {`
- `NavigationPage` -> `public double BarHeight {`
- `NavigationPage` -> `public double EffectiveBarHeight {`
- `NavigationPage` -> `public event EventHandler<ModalPoppedEventArgs>? ModalPopped;`
- `NavigationPage` -> `public event EventHandler<ModalPushedEventArgs>? ModalPushed;`
- `NavigationPage` -> `public event EventHandler<NavigationEventArgs>? Popped;`
- `NavigationPage` -> `public event EventHandler<NavigationEventArgs>? PoppedToRoot;`
- `NavigationPage` -> `public event EventHandler<NavigationEventArgs>? Pushed;`
- `NavigationPage` -> `public event EventHandler<PageInsertedEventArgs>? PageInserted;`
- `NavigationPage` -> `public event EventHandler<PageRemovedEventArgs>? PageRemoved;`
- `NavigationPage` -> `public int StackDepth {`
- `NavigationPage` -> `public object? Content {`
- `NavigationPage` -> `public static BarLayoutBehavior? GetBarLayoutBehavior(Page page) =>`
- `NavigationPage` -> `public static Control? GetBottomCommandBar(Page page) =>`
- `NavigationPage` -> `public static Control? GetTopCommandBar(Page page) =>`
- `NavigationPage` -> `public static bool GetHasBackButton(Page page) =>`
- `NavigationPage` -> `public static bool GetHasNavigationBar(Page page) =>`
- `NavigationPage` -> `public static bool GetIsBackButtonEnabled(Page page) =>`
- `NavigationPage` -> `public static double? GetBarHeightOverride(Page page) =>`
- `NavigationPage` -> `public static object? GetBackButtonContent(Page page) =>`
- `NavigationPage` -> `public static object? GetHeader(Page page) =>`
- `NavigationPage` -> `public static readonly AttachedProperty<BarLayoutBehavior?> BarLayoutBehaviorProperty = AvaloniaProperty.RegisterAttached<NavigationPage, Page, BarLayoutBehavior?>("BarLayoutBehavior");`
- `NavigationPage` -> `public static readonly AttachedProperty<Control?> BottomCommandBarProperty = AvaloniaProperty.RegisterAttached<NavigationPage, Page, Control?>("BottomCommandBar");`
- `NavigationPage` -> `public static readonly AttachedProperty<Control?> TopCommandBarProperty = AvaloniaProperty.RegisterAttached<NavigationPage, Page, Control?>("TopCommandBar");`
- `NavigationPage` -> `public static readonly AttachedProperty<bool> HasBackButtonProperty = AvaloniaProperty.RegisterAttached<NavigationPage, Page, bool>("HasBackButton", true);`
- `NavigationPage` -> `public static readonly AttachedProperty<bool> HasNavigationBarProperty = AvaloniaProperty.RegisterAttached<NavigationPage, Page, bool>("HasNavigationBar", true);`
- `NavigationPage` -> `public static readonly AttachedProperty<bool> IsBackButtonEnabledProperty = AvaloniaProperty.RegisterAttached<NavigationPage, Page, bool>("IsBackButtonEnabled", true);`
- `NavigationPage` -> `public static readonly AttachedProperty<double?> BarHeightOverrideProperty = AvaloniaProperty.RegisterAttached<NavigationPage, Page, double?>("BarHeightOverride");`
- `NavigationPage` -> `public static readonly AttachedProperty<object?> BackButtonContentProperty = AvaloniaProperty.RegisterAttached<NavigationPage, Page, object?>("BackButtonContent");`
- `NavigationPage` -> `public static readonly DirectProperty<NavigationPage, bool> CanGoBackProperty = AvaloniaProperty.RegisterDirect<NavigationPage, bool>(nameof(CanGoBack), o => o.CanGoBack);`
- `NavigationPage` -> `public static readonly DirectProperty<NavigationPage, bool?> IsBackButtonEffectivelyVisibleProperty = AvaloniaProperty.RegisterDirect<NavigationPage, bool?>(nameof(IsBackButtonEffectivelyVisible), o => o.IsBackButtonEffectivelyVisible);`
- `NavigationPage` -> `public static readonly DirectProperty<NavigationPage, double> EffectiveBarHeightProperty = AvaloniaProperty.RegisterDirect<NavigationPage, double>(nameof(EffectiveBarHeight), o => o.EffectiveBarHeight);`
- `NavigationPage` -> `public static readonly StyledProperty<IPageTransition?> ModalTransitionProperty = AvaloniaProperty.Register<NavigationPage, IPageTransition?>(nameof(ModalTransition));`
- `NavigationPage` -> `public static readonly StyledProperty<IPageTransition?> PageTransitionProperty = AvaloniaProperty.Register<NavigationPage, IPageTransition?>(nameof(PageTransition));`
- `NavigationPage` -> `public static readonly StyledProperty<bool> HasShadowProperty = AvaloniaProperty.Register<NavigationPage, bool>(nameof(HasShadow), false);`
- `NavigationPage` -> `public static readonly StyledProperty<bool> IsBackButtonVisibleProperty = AvaloniaProperty.Register<NavigationPage, bool>(nameof(IsBackButtonVisible), true);`
- `NavigationPage` -> `public static readonly StyledProperty<bool> IsGestureEnabledProperty = AvaloniaProperty.Register<NavigationPage, bool>(nameof(IsGestureEnabled), true);`
- `NavigationPage` -> `public static readonly StyledProperty<double> BarHeightProperty = AvaloniaProperty.Register<NavigationPage, double>(nameof(BarHeight), 48.0);`
- `NavigationPage` -> `public static readonly StyledProperty<object?> ContentProperty = AvaloniaProperty.Register<NavigationPage, object?>(nameof(Content));`
- `NavigationPage` -> `public static void SetBackButtonContent(Page page, object? content) =>`
- `NavigationPage` -> `public static void SetBarHeightOverride(Page page, double? value) =>`
- `NavigationPage` -> `public static void SetBarLayoutBehavior(Page page, BarLayoutBehavior? value) =>`
- `NavigationPage` -> `public static void SetBottomCommandBar(Page page, Control? commandBar) =>`
- `NavigationPage` -> `public static void SetHasBackButton(Page page, bool value) =>`
- `NavigationPage` -> `public static void SetHasNavigationBar(Page page, bool value) =>`
- `NavigationPage` -> `public static void SetHeader(Page page, object? header) =>`
- `NavigationPage` -> `public static void SetIsBackButtonEnabled(Page page, bool value) =>`
- `NavigationPage` -> `public static void SetTopCommandBar(Page page, Control? commandBar) =>`
- `NavigationPage` -> `public void InsertPage(Page page, Page before) {`
- `NavigationPage` -> `public void RemovePage(Page page) {`

#### `src/Avalonia.Controls/Page/NavigationType.cs`

- `public enum NavigationType {`

#### `src/Avalonia.Controls/Page/Page.cs`

- `Page` -> `public INavigation? Navigation {`
- `Page` -> `public Page? CurrentPage {`
- `Page` -> `public Thickness SafeAreaPadding {`
- `public abstract class Page : TemplatedControl, IHeadered {`
- `Page` -> `public bool IsInNavigationPage {`
- `Page` -> `public event EventHandler<NavigatedFromEventArgs>? NavigatedFrom;`
- `Page` -> `public event EventHandler<NavigatedToEventArgs>? NavigatedTo;`
- `Page` -> `public event EventHandler<RoutedEventArgs>? PageNavigationSystemBackButtonPressed {`
- `Page` -> `public event Func<NavigatingFromEventArgs, Task>? Navigating;`
- `Page` -> `public object? Header {`
- `Page` -> `public object? Icon {`
- `Page` -> `public static readonly DirectProperty<Page, INavigation?> NavigationProperty = AvaloniaProperty.RegisterDirect<Page, INavigation?>( nameof(Navigation), o => o.Navigation,`
- `Page` -> `public static readonly RoutedEvent<RoutedEventArgs> PageNavigationSystemBackButtonPressedEvent = RoutedEvent.Register<Page, RoutedEventArgs>( nameof(PageNavigationSystemBackButtonPressed), RoutingStrategies.Bubble);`
- `Page` -> `public static readonly StyledProperty<Page?> CurrentPageProperty = AvaloniaProperty.Register<Page, Page?>(nameof(CurrentPage));`
- `Page` -> `public static readonly StyledProperty<Thickness> SafeAreaPaddingProperty = AvaloniaProperty.Register<Page, Thickness>(nameof(SafeAreaPadding));`
- `Page` -> `public static readonly StyledProperty<bool> IsInNavigationPageProperty = AvaloniaProperty.Register<Page, bool>(nameof(IsInNavigationPage));`
- `Page` -> `public static readonly StyledProperty<object?> HeaderProperty = AvaloniaProperty.Register<Page, object?>(nameof(Header));`
- `Page` -> `public static readonly StyledProperty<object?> IconProperty = AvaloniaProperty.Register<Page, object?>(nameof(Icon));`

#### `src/Avalonia.Controls/Page/PageInsertedEventArgs.cs`

- `PageInsertedEventArgs` -> `public Page Before { get; }`
- `PageInsertedEventArgs` -> `public Page Page { get; }`
- `PageInsertedEventArgs` -> `public PageInsertedEventArgs(Page page, Page before) {`
- `public class PageInsertedEventArgs : EventArgs {`

#### `src/Avalonia.Controls/Page/PageNavigationHost.cs`

- `PageNavigationHost` -> `public Page? Page {`
- `public class PageNavigationHost : ContentControl {`
- `PageNavigationHost` -> `public static readonly StyledProperty<Page?> PageProperty = AvaloniaProperty.Register<PageNavigationHost, Page?>(nameof(Page));`

#### `src/Avalonia.Controls/Page/PageRemovedEventArgs.cs`

- `PageRemovedEventArgs` -> `public Page Page { get; }`
- `PageRemovedEventArgs` -> `public PageRemovedEventArgs(Page page) {`
- `public class PageRemovedEventArgs : EventArgs {`

#### `src/Avalonia.Controls/Page/PageSelectionChangedEventArgs.cs`

- `PageSelectionChangedEventArgs` -> `public Page? CurrentPage { get; }`
- `PageSelectionChangedEventArgs` -> `public Page? PreviousPage { get; }`
- `PageSelectionChangedEventArgs` -> `public PageSelectionChangedEventArgs(Page? previousPage, Page? currentPage) {`
- `public class PageSelectionChangedEventArgs : EventArgs {`

#### `src/Avalonia.Controls/Page/SelectingMultiPage.cs`

- `SelectingMultiPage` -> `public Page? SelectedPage => _selectedPage;`
- `public abstract class SelectingMultiPage : MultiPage {`
- `SelectingMultiPage` -> `public event EventHandler<PageSelectionChangedEventArgs>? SelectionChanged;`
- `SelectingMultiPage` -> `public int SelectedIndex {`
- `SelectingMultiPage` -> `public static readonly DirectProperty<SelectingMultiPage, Page?> SelectedPageProperty = AvaloniaProperty.RegisterDirect<SelectingMultiPage, Page?>( nameof(SelectedPage), o => o._selectedPage);`
- `SelectingMultiPage` -> `public static readonly DirectProperty<SelectingMultiPage, int> SelectedIndexProperty = AvaloniaProperty.RegisterDirect<SelectingMultiPage, int>( nameof(SelectedIndex), o => o._selectedIndex,`

#### `src/Avalonia.Controls/Page/TabPlacement.cs`

- `public enum TabPlacement {`

#### `src/Avalonia.Controls/Page/TabbedPage.cs`

- `TabbedPage` -> `public IDataTemplate? IndicatorTemplate {`
- `TabbedPage` -> `public IPageTransition? PageTransition {`
- `TabbedPage` -> `public TabPlacement TabPlacement {`
- `TabbedPage` -> `public TabbedPage() {`
- `TabbedPage` -> `public bool IsGestureEnabled {`
- `TabbedPage` -> `public bool IsKeyboardNavigationEnabled {`
- `public class TabbedPage : SelectingMultiPage {`
- `TabbedPage` -> `public static bool GetIsTabEnabled(Page page) => page.GetValue(IsTabEnabledProperty);`
- `TabbedPage` -> `public static readonly AttachedProperty<bool> IsTabEnabledProperty = AvaloniaProperty.RegisterAttached<TabbedPage, Page, bool>("IsTabEnabled", defaultValue: true);`
- `TabbedPage` -> `public static readonly StyledProperty<IDataTemplate?> IndicatorTemplateProperty = AvaloniaProperty.Register<TabbedPage, IDataTemplate?>(nameof(IndicatorTemplate));`
- `TabbedPage` -> `public static readonly StyledProperty<IPageTransition?> PageTransitionProperty = AvaloniaProperty.Register<TabbedPage, IPageTransition?>(nameof(PageTransition));`
- `TabbedPage` -> `public static readonly StyledProperty<TabPlacement> TabPlacementProperty = AvaloniaProperty.Register<TabbedPage, TabPlacement>(nameof(TabPlacement), TabPlacement.Auto);`
- `TabbedPage` -> `public static readonly StyledProperty<bool> IsGestureEnabledProperty = AvaloniaProperty.Register<TabbedPage, bool>(nameof(IsGestureEnabled), defaultValue: false);`
- `TabbedPage` -> `public static readonly StyledProperty<bool> IsKeyboardNavigationEnabledProperty = AvaloniaProperty.Register<TabbedPage, bool>(nameof(IsKeyboardNavigationEnabled), true);`
- `TabbedPage` -> `public static void SetIsTabEnabled(Page page, bool value) =>`

#### `src/Avalonia.Controls/Platform/IPlatformNativeSurfaceHandle.cs`

- `public interface INativePlatformHandleSurface : IPlatformHandle, IPlatformRenderSurface {`

#### `src/Avalonia.Controls/Platform/ITopLevelImpl.cs`

- `ITopLevelImpl` -> `IPlatformRenderSurface[] Surfaces { get; }`

#### `src/Avalonia.Controls/Platform/IWindowImpl.cs`

- `IWindowImpl` -> `PlatformRequestedDrawnDecoration RequestedDrawnDecorations { get; }`
- `IWindowImpl` -> `void SetWindowDecorations(WindowDecorations enabled);`

#### `src/Avalonia.Controls/Platform/IWindowingPlatform.cs`

- `IWindowingPlatform` -> `void GetWindowsZOrder(ReadOnlySpan<IWindowImpl> windows, Span<long> zOrder);`

#### `src/Avalonia.Controls/Platform/PlatformRequestedDrawnDecoration.cs`

- Namespace(s): `Avalonia.Controls.Platform`
- `public enum PlatformRequestedDrawnDecoration {`

#### `src/Avalonia.Controls/Platform/Screen.cs`

- `Screen` -> `public abstract bool Equals(Screen? other);`
- `public abstract class Screen : IEquatable<Screen> {`
- `Screen` -> `public abstract override int GetHashCode();`

#### `src/Avalonia.Controls/Presenters/ContentPresenter.cs`

- `ContentPresenter` -> `public double LetterSpacing {`
- `ContentPresenter` -> `public static readonly StyledProperty<double> LetterSpacingProperty = TextElement.LetterSpacingProperty.AddOwner<ContentPresenter>();`

#### `src/Avalonia.Controls/Presenters/TextPresenter.cs`

- `TextPresenter` -> `public static readonly StyledProperty<double> LetterSpacingProperty = TextElement.LetterSpacingProperty.AddOwner<TextPresenter>();`

#### `src/Avalonia.Controls/Primitives/AccessText.cs`

- `AccessText` -> `public static readonly AttachedProperty<bool> ShowAccessKeyProperty = AccessKeyHandler.ShowAccessKeyProperty.AddOwner<AccessText>();`
- `AccessText` -> `public string? AccessKey {`

#### `src/Avalonia.Controls/Primitives/ILogicalScrollable.cs`

- `ILogicalScrollable` -> `new bool CanHorizontallyScroll { get; set; }`
- `ILogicalScrollable` -> `new bool CanVerticallyScroll { get; set; }`

#### `src/Avalonia.Controls/Primitives/ItemSelectionEventTriggers.cs`

- Namespace(s): `Avalonia.Controls.Primitives`
- `ItemSelectionEventTriggers` -> `public static bool HasRangeSelectionModifier(Visual selectable, RoutedEventArgs eventArgs) => HasModifiers(eventArgs, Hotkeys(selectable)?.SelectionModifiers);`
- `ItemSelectionEventTriggers` -> `public static bool HasToggleSelectionModifier(Visual selectable, RoutedEventArgs eventArgs) => HasModifiers(eventArgs, Hotkeys(selectable)?.CommandModifiers);`
- `ItemSelectionEventTriggers` -> `public static bool ShouldTriggerSelection(Visual selectable, KeyEventArgs eventArgs) {`
- `ItemSelectionEventTriggers` -> `public static bool ShouldTriggerSelection(Visual selectable, PointerEventArgs eventArgs) {`
- `public static class ItemSelectionEventTriggers {`

#### `src/Avalonia.Controls/Primitives/OverlayPopupHost.cs`

- `public class OverlayPopupHost : ContentControl, IPopupHost, IManagedPopupPositionerPopup {`

#### `src/Avalonia.Controls/Primitives/SelectingItemsControl.cs`

- `SelectingItemsControl` -> `public BindingBase? SelectedValueBinding {`
- `SelectingItemsControl` -> `public new static SelectingItemsControl? ItemsControlFromItemContainer(Control container) => ItemsControl.ItemsControlFromItemContainer(container) as SelectingItemsControl;`
- `SelectingItemsControl` -> `public static readonly StyledProperty<BindingBase?> SelectedValueBindingProperty = AvaloniaProperty.Register<SelectingItemsControl, BindingBase?>(nameof(SelectedValueBinding));`
- `SelectingItemsControl` -> `public virtual bool UpdateSelectionFromEvent(Control container, RoutedEventArgs eventArgs) {`

#### `src/Avalonia.Controls/Primitives/TabStrip.cs`

- `TabStrip` -> `public override bool UpdateSelectionFromEvent(Control container, RoutedEventArgs eventArgs) {`

#### `src/Avalonia.Controls/Primitives/TemplatedControl.cs`

- `TemplatedControl` -> `public double LetterSpacing {`
- `TemplatedControl` -> `public static readonly StyledProperty<double> LetterSpacingProperty = TextElement.LetterSpacingProperty.AddOwner<TemplatedControl>();`

#### `src/Avalonia.Controls/Primitives/TextSearch.cs`

- `TextSearch` -> `public static BindingBase? GetTextBinding(Interactive interactive) => interactive.GetValue(TextBindingProperty);`
- `TextSearch` -> `public static readonly AttachedProperty<BindingBase?> TextBindingProperty = AvaloniaProperty.RegisterAttached<Interactive, BindingBase?>("TextBinding", typeof(TextSearch));`
- `TextSearch` -> `public static string? GetText(Interactive control) => control.GetValue(TextProperty);`
- `TextSearch` -> `public static void SetText(Interactive control, string? text) => control.SetValue(TextProperty, text);`
- `TextSearch` -> `public static void SetTextBinding(Interactive interactive, BindingBase? value) => interactive.SetValue(TextBindingProperty, value);`

#### `src/Avalonia.Controls/Primitives/VisualLayerManager.cs`

- `public sealed class VisualLayerManager : Decorator {`

#### `src/Avalonia.Controls/Remote/RemoteWidget.cs`

- `public enum SizingMode {`

#### `src/Avalonia.Controls/ScrollViewer.cs`

- `public class ScrollViewer : ContentControl, IScrollable, IScrollAnchorProvider {`

#### `src/Avalonia.Controls/TabControl.cs`

- `TabControl` -> `public IDataTemplate? IndicatorTemplate {`
- `TabControl` -> `public IPageTransition? PageTransition {`
- `TabControl` -> `public override bool UpdateSelectionFromEvent(Control container, RoutedEventArgs eventArgs) {`
- `TabControl` -> `public static readonly StyledProperty<IDataTemplate?> IndicatorTemplateProperty = AvaloniaProperty.Register<TabControl, IDataTemplate?>(nameof(IndicatorTemplate));`
- `TabControl` -> `public static readonly StyledProperty<IPageTransition?> PageTransitionProperty = AvaloniaProperty.Register<TabControl, IPageTransition?>(nameof(PageTransition));`

#### `src/Avalonia.Controls/TabItem.cs`

- `TabItem` -> `public Control? Icon {`
- `TabItem` -> `public IDataTemplate? IndicatorTemplate {`
- `TabItem` -> `public static readonly StyledProperty<Control?> IconProperty = AvaloniaProperty.Register<TabItem, Control?>(nameof(Icon));`
- `TabItem` -> `public static readonly StyledProperty<IDataTemplate?> IndicatorTemplateProperty = AvaloniaProperty.Register<TabItem, IDataTemplate?>(nameof(IndicatorTemplate));`

#### `src/Avalonia.Controls/Templates/FuncTreeDataTemplate.cs`

- `FuncTreeDataTemplate` -> `public IDisposable BindChildren(AvaloniaObject target, AvaloniaProperty targetProperty, object item) {`

#### `src/Avalonia.Controls/Templates/ITreeDataTemplate.cs`

- `ITreeDataTemplate` -> `IDisposable BindChildren(AvaloniaObject target, AvaloniaProperty targetProperty, object item);`

#### `src/Avalonia.Controls/TextBlock.cs`

- `TextBlock` -> `public static readonly StyledProperty<double> LetterSpacingProperty = TextElement.LetterSpacingProperty.AddOwner<TextBlock>();`

#### `src/Avalonia.Controls/TextBox.cs`

- `TextBox` -> `public IBrush? PlaceholderForeground {`
- `TextBox` -> `public IBrush? WatermarkForeground {`
- `TextBox` -> `public bool UseFloatingPlaceholder {`
- `TextBox` -> `public static readonly StyledProperty<IBrush?> PlaceholderForegroundProperty = AvaloniaProperty.Register<TextBox, IBrush?>(nameof(PlaceholderForeground));`
- `TextBox` -> `public static readonly StyledProperty<IBrush?> WatermarkForegroundProperty = PlaceholderForegroundProperty;`
- `TextBox` -> `public static readonly StyledProperty<bool> UseFloatingPlaceholderProperty = AvaloniaProperty.Register<TextBox, bool>(nameof(UseFloatingPlaceholder));`
- `TextBox` -> `public static readonly StyledProperty<bool> UseFloatingWatermarkProperty = UseFloatingPlaceholderProperty;`
- `TextBox` -> `public static readonly StyledProperty<string?> PlaceholderTextProperty = AvaloniaProperty.Register<TextBox, string?>(nameof(PlaceholderText));`
- `TextBox` -> `public static readonly StyledProperty<string?> WatermarkProperty = PlaceholderTextProperty;`
- `TextBox` -> `public string? PlaceholderText {`

#### `src/Avalonia.Controls/TopLevel.cs`

- `TopLevel` -> `public IFocusManager FocusManager => _source.FocusManager;`
- `public abstract class TopLevel : ContentControl, ICloseable, IStyleHost, ILogicalRoot {`

#### `src/Avalonia.Controls/TreeView.cs`

- `TreeView` -> `public virtual bool UpdateSelectionFromEvent(Control container, RoutedEventArgs eventArgs) {`

#### `src/Avalonia.Controls/Window.cs`

- `Window` -> `public WindowDecorations SystemDecorations {`
- `Window` -> `public WindowDecorations WindowDecorations {`
- `public class Window : WindowBase, IFocusScope {`
- `public enum WindowDecorations {`
- `Window` -> `public static readonly StyledProperty<WindowDecorations> WindowDecorationsProperty = AvaloniaProperty.Register<Window, WindowDecorations>(nameof(WindowDecorations), WindowDecorations.Full);`
- `Window` -> `public static void SortWindowsByZOrder(Span<Window> windows) {`

### Headless Platform

#### `src/Headless/Avalonia.Headless.Vnc/HeadlessVncPlatformExtensions.cs`

- `HeadlessVncPlatformExtensions` -> `public static int StartWithHeadlessVncPlatform( this AppBuilder builder, string? host, int port, string? password, string[] args, ShutdownMode shutdownMode = ShutdownMode.OnLastWindowClose) {`
- `HeadlessVncPlatformExtensions` -> `public static int StartWithHeadlessVncPlatform( this AppBuilder builder, string? host, int port, string[] args, ShutdownMode shutdownMode = ShutdownMode.OnLastWindowClose) {`

#### `src/Headless/Avalonia.Headless.XUnit/AvaloniaFact.cs`

- Namespace(s): `Avalonia.Headless.XUnit`
- `public sealed class AvaloniaFactAttribute( [CallerFilePath] string? sourceFilePath = null, [CallerLineNumber] int sourceLineNumber = -1) : FactAttribute(sourceFilePath, sourceLineNumber);`

#### `src/Headless/Avalonia.Headless.XUnit/AvaloniaFactDiscoverer.cs`

- Namespace(s): `Avalonia.Headless.XUnit`
- `public class AvaloniaFactDiscoverer : FactDiscoverer {`

#### `src/Headless/Avalonia.Headless.XUnit/AvaloniaTestFrameworkAttribute.cs`

- Namespace(s): `Avalonia.Headless.XUnit`
- `AvaloniaTestFrameworkAttribute` -> `public Type FrameworkType => typeof(AvaloniaTestFramework);`

#### `src/Headless/Avalonia.Headless.XUnit/AvaloniaTheoryAttribute.cs`

- Namespace(s): `Avalonia.Headless.XUnit`
- `public sealed class AvaloniaTheoryAttribute : TheoryAttribute;`

#### `src/Headless/Avalonia.Headless/HeadlessUnitTestSession.cs`

- Namespace(s): `Avalonia.Headless`
- `HeadlessUnitTestSession` -> `public async ValueTask DisposeAsync() {`
- `public sealed class HeadlessUnitTestSession : IDisposable, IAsyncDisposable {`

### Linux Framebuffer

#### `src/Linux/Avalonia.LinuxFramebuffer/DrmOutputOptions.cs`

- `DrmOutputOptions` -> `public SurfaceOrientation Orientation { get; set; } = SurfaceOrientation.Rotation0;`

#### `src/Linux/Avalonia.LinuxFramebuffer/Output/DrmOutput.cs`

- `DrmOutput` -> `public PixelSize PixelSize => Orientation == SurfaceOrientation.Rotation0 || Orientation == SurfaceOrientation.Rotation180`
- `DrmOutput` -> `public SurfaceOrientation Orientation {`
- `public unsafe class DrmOutput : IGlOutputBackend, IGlPlatformSurface, ISurfaceOrientation {`

#### `src/Linux/Avalonia.LinuxFramebuffer/Output/FbdevOutput.cs`

- `FbdevOutput` -> `public IFramebufferRenderTarget CreateFramebufferRenderTarget() => new FuncFramebufferRenderTarget(Lock, true);`
- `FbdevOutput` -> `public ILockedFramebuffer Lock(IRenderTarget.RenderTargetSceneInfo _, out FramebufferLockProperties properties) {`

#### `src/Linux/Avalonia.LinuxFramebuffer/Output/IOutputBackend.cs`

- `public interface IOutputBackend : IPlatformRenderSurface {`

### Linux/X11 Platform

#### `src/Avalonia.X11/X11Platform.cs`

- `X11PlatformOptions` -> `public Action<Exception>? ExternalGLibMainLoopExceptionLogger { get; set; }`
- `X11PlatformOptions` -> `public bool? EnableDrawnDecorations {`

### Other

#### `src/Avalonia.Metal/IMetalDevice.cs`

- Namespace(s): `Avalonia.Metal`
- `public interface IMetalPlatformSurface : IPlatformRenderSurface {`
- `public interface IMetalPlatformSurfaceRenderTarget : IDisposable, IPlatformRenderSurfaceRenderTarget {`

#### `src/Avalonia.OpenGL/Egl/EglGlPlatformSurface.cs`

- `EglGlPlatformSurface.IEglWindowGlPlatformSurfaceInfoWithWaitPolicy` -> `public bool SkipWaits { get; }`
- `EglGlPlatformSurface` -> `public interface IEglWindowGlPlatformSurfaceInfoWithWaitPolicy : IEglWindowGlPlatformSurfaceInfo {`

#### `src/Avalonia.OpenGL/Egl/EglGlPlatformSurfaceBase.cs`

- `EglPlatformSurfaceRenderTargetBase` -> `public IGlPlatformSurfaceRenderingSession BeginDraw(IRenderTarget.RenderTargetSceneInfo sceneInfo) {`
- `EglPlatformSurfaceRenderTargetBase` -> `public abstract IGlPlatformSurfaceRenderingSession BeginDrawCore(IRenderTarget.RenderTargetSceneInfo sceneInfo);`
- `public abstract class EglPlatformSurfaceRenderTargetBase : IGlPlatformSurfaceRenderTarget {`

#### `src/Avalonia.OpenGL/GlConsts.cs`

- `GlConsts` -> `public const int GL_TRIANGLE_FAN = 0x0006;`

#### `src/Avalonia.OpenGL/GlInterface.cs`

- `GlInterface` -> `public partial void Uniform1i(int location, int value);`

#### `src/Avalonia.OpenGL/IGlContext.cs`

- `IGlPlatformSurfaceRenderTargetFactory` -> `IGlPlatformSurfaceRenderTarget CreateRenderTarget(IGlContext context, IPlatformRenderSurface surface);`
- `IGlPlatformSurfaceRenderTargetFactory` -> `bool CanRenderToSurface(IGlContext context, IPlatformRenderSurface surface);`

#### `src/Avalonia.OpenGL/Surfaces/IGlPlatformSurface.cs`

- `public interface IGlPlatformSurface : IPlatformRenderSurface {`

#### `src/Avalonia.OpenGL/Surfaces/IGlPlatformSurfaceRenderTarget.cs`

- `IGlPlatformSurfaceRenderTarget` -> `IGlPlatformSurfaceRenderingSession BeginDraw(IRenderTarget.RenderTargetSceneInfo sceneInfo);`
- `IGlPlatformSurfaceRenderTarget` -> `bool IsCorrupted { get; }`
- `public interface IGlPlatformSurfaceRenderTarget : IDisposable, IPlatformRenderSurfaceRenderTarget {`

#### `src/Avalonia.Vulkan/IVulkanDevice.cs`

- Namespace(s): `Avalonia.Vulkan`
- `IVulkanPlatformGraphicsContext` -> `IVulkanRenderTarget CreateRenderTarget(IEnumerable<IPlatformRenderSurface> surfaces);`

#### `src/Avalonia.Vulkan/IVulkanPlatformSurface.cs`

- Namespace(s): `Avalonia.Vulkan`
- `IVulkanKhrSurfacePlatformSurfaceFactory` -> `IVulkanKhrSurfacePlatformSurface CreateSurface(IVulkanPlatformGraphicsContext context, IPlatformRenderSurface surface);`
- `IVulkanKhrSurfacePlatformSurfaceFactory` -> `bool CanRenderToSurface(IVulkanPlatformGraphicsContext context, IPlatformRenderSurface surface);`
- `public interface IVulkanKhrSurfacePlatformSurface : IDisposable, IPlatformRenderSurface {`

#### `src/Avalonia.Vulkan/IVulkanRenderTarget.cs`

- Namespace(s): `Avalonia.Vulkan`
- `public interface IVulkanRenderTarget : IDisposable, IPlatformRenderSurfaceRenderTarget {`

#### `src/tools/Avalonia.Analyzers.CSharp/DiagnosticIds.cs`

- `DiagnosticIds` -> `public const string Bitmap = "AVA2002";`
- `DiagnosticIds` -> `public const string OnPropertyChangedOverride = "AVA2001";`
- `public static class DiagnosticIds {`

#### `src/tools/Avalonia.Analyzers.CodeFixes.CSharp/BitmapAnalyzerCodeFixProvider.cs`

- Namespace(s): `Avalonia.Analyzers.CodeFixes.CSharp`
- `public class BitmapAnalyzerCodeFixProvider : CodeFixProvider {`
- `BitmapAnalyzerCodeFixProvider` -> `public override FixAllProvider? GetFixAllProvider() {`
- `BitmapAnalyzerCodeFixProvider` -> `public override ImmutableArray<string> FixableDiagnosticIds { get; } =`
- `BitmapAnalyzerCodeFixProvider` -> `public sealed override async Task RegisterCodeFixesAsync(CodeFixContext context) {`

### Property, Data, Styling, Threading

#### `src/Avalonia.Base/Animation/CrossFade.cs`

- `CrossFade` -> `public FillMode FillMode {`

#### `src/Avalonia.Base/Animation/PageSlide.cs`

- `PageSlide` -> `public FillMode FillMode { get; set; } = FillMode.Forward;`

#### `src/Avalonia.Base/AvaloniaObject.cs`

- `AvaloniaObject` -> `public BindingBase this[IndexerDescriptor binding] {`
- `AvaloniaObject` -> `public BindingExpressionBase Bind(AvaloniaProperty property, BindingBase binding) {`
- `AvaloniaObject` -> `public Dispatcher Dispatcher { get; } = Dispatcher.CurrentDispatcher;`
- `AvaloniaObject` -> `public bool CheckAccess() => Dispatcher.CheckAccess();`
- `AvaloniaObject` -> `public void VerifyAccess() => Dispatcher.VerifyAccess();`

#### `src/Avalonia.Base/AvaloniaObjectExtensions.cs`

- `AvaloniaObjectExtensions` -> `public static BindingBase ToBinding<T>(this IObservable<T> source) {`

#### `src/Avalonia.Base/Controls/NameScope.cs`

- `NameScope` -> `public static INameScope? GetNameScope(StyledElement styled) {`
- `NameScope` -> `public static readonly AttachedProperty<INameScope?> NameScopeProperty = AvaloniaProperty.RegisterAttached<NameScope, StyledElement, INameScope?>("NameScope");`
- `NameScope` -> `public static void SetNameScope(StyledElement styled, INameScope? value) {`

#### `src/Avalonia.Base/Controls/Primitives/IScrollable.cs`

- `IScrollable` -> `bool CanHorizontallyScroll { get; }`
- `IScrollable` -> `bool CanVerticallyScroll { get; }`

#### `src/Avalonia.Base/Controls/PseudoClassesExtensions.cs`

- `public static class PseudoClassesExtensions {`
- `PseudoClassesExtensions` -> `public static void Set(this IPseudoClasses classes, string name, bool value) {`

#### `src/Avalonia.Base/Controls/ResourcesChangedEventArgs.cs`

- Namespace(s): `Avalonia.Controls`
- `public readonly record struct ResourcesChangedEventArgs(int SequenceNumber) {`
- `ResourcesChangedEventArgs` -> `public static ResourcesChangedEventArgs Create() => new(Interlocked.Increment(ref s_lastSequenceNumber));`

#### `src/Avalonia.Base/Data/BindingBase.cs`

- Namespace(s): `Avalonia.Data`
- `public abstract class BindingBase {`

#### `src/Avalonia.Base/Data/CompiledBinding.cs`

- Namespace(s): `Avalonia.Data`
- `CompiledBinding` -> `public BindingMode Mode { get; set; }`
- `CompiledBinding` -> `public BindingPriority Priority { get; set; }`
- `CompiledBinding` -> `public CompiledBinding() { }`
- `CompiledBinding` -> `public CompiledBinding(CompiledBindingPath path) => Path = path;`
- `CompiledBinding` -> `public CompiledBindingPath? Path { get; set; }`
- `CompiledBinding` -> `public CultureInfo? ConverterCulture { get; set; }`
- `CompiledBinding` -> `public IValueConverter? Converter { get; set; }`
- `CompiledBinding` -> `public UpdateSourceTrigger UpdateSourceTrigger { get; set; }`
- `public class CompiledBinding : BindingBase {`
- `CompiledBinding` -> `public int Delay { get; set; }`
- `CompiledBinding` -> `public object? ConverterParameter { get; set; }`
- `CompiledBinding` -> `public object? FallbackValue { get; set; } = AvaloniaProperty.UnsetValue;`
- `CompiledBinding` -> `public object? Source { get; set; } = AvaloniaProperty.UnsetValue;`
- `CompiledBinding` -> `public object? TargetNullValue { get; set; } = AvaloniaProperty.UnsetValue;`
- `CompiledBinding` -> `public static CompiledBinding Create<TIn, TOut>( Expression<Func<TIn, TOut>> expression, object? source = null, IValueConverter? converter = null, BindingMode mode = BindingMode.Default, BindingPriority priority = BindingPriority.LocalValue, CultureInfo? converterCulture = null, object? converterParameter = null, object? fallbackValue = null, string? stringFormat = null, object? targetNullValue = null, UpdateSourceTrigger updateSourceTrigger = UpdateSourceTrigger.Default, int delay = 0) {`
- `CompiledBinding` -> `public string? StringFormat { get; set; }`

#### `src/Avalonia.Base/Data/CompiledBindingPath.cs`

- `CompiledBindingPathBuilder` -> `public CompiledBindingPathBuilder StreamObservable() {`
- `CompiledBindingPathBuilder` -> `public CompiledBindingPathBuilder StreamTask() {`
- `CompiledBindingPathBuilder` -> `public CompiledBindingPathBuilder TypeCast(Type targetType) {`
- `CompiledBindingPath` -> `public override string ToString() => string.Concat((IEnumerable<ICompiledBindingPathElement>)_elements);`

#### `src/Avalonia.Base/Data/Converters/FuncMultiValueConverter.cs`

- `FuncMultiValueConverter` -> `public FuncMultiValueConverter(Func<IEnumerable<TIn?>, TOut> convert) : this(new Func<IReadOnlyList<TIn?>, TOut>(convert)) {`
- `FuncMultiValueConverter` -> `public FuncMultiValueConverter(Func<IReadOnlyList<TIn?>, TOut> convert) {`

#### `src/Avalonia.Base/Data/MultiBinding.cs`

- `MultiBinding` -> `public IList<BindingBase> Bindings { get; set; } = new List<BindingBase>();`
- `public sealed class MultiBinding : BindingBase {`

#### `src/Avalonia.Base/Data/ReflectionBinding.cs`

- `ReflectionBinding` -> `public BindingMode Mode { get; set; }`
- `ReflectionBinding` -> `public BindingPriority Priority { get; set; }`
- `ReflectionBinding` -> `public CultureInfo? ConverterCulture { get; set; }`
- `ReflectionBinding` -> `public Func<string?, string, Type>? TypeResolver { get; set; }`
- `ReflectionBinding` -> `public IValueConverter? Converter { get; set; }`
- `ReflectionBinding` -> `public ReflectionBinding() {`
- `ReflectionBinding` -> `public ReflectionBinding(string path) {`
- `ReflectionBinding` -> `public RelativeSource? RelativeSource { get; set; }`
- `ReflectionBinding` -> `public UpdateSourceTrigger UpdateSourceTrigger { get; set; }`
- `public class ReflectionBinding : BindingBase {`
- `ReflectionBinding` -> `public int Delay { get; set; }`
- `ReflectionBinding` -> `public object? ConverterParameter { get; set; }`
- `ReflectionBinding` -> `public object? FallbackValue { get; set; } = AvaloniaProperty.UnsetValue;`
- `ReflectionBinding` -> `public object? Source { get; set; } = AvaloniaProperty.UnsetValue;`
- `ReflectionBinding` -> `public object? TargetNullValue { get; set; } = AvaloniaProperty.UnsetValue;`
- `ReflectionBinding` -> `public string Path { get; set; } = "";`
- `ReflectionBinding` -> `public string? ElementName { get; set; }`
- `ReflectionBinding` -> `public string? StringFormat { get; set; }`

#### `src/Avalonia.Base/Data/TemplateBinding.cs`

- `TemplateBinding` -> `public BindingBase ProvideValue() => this;`
- `TemplateBinding` -> `public BindingMode Mode { get; set; }`
- `TemplateBinding` -> `public TemplateBinding() {`
- `TemplateBinding` -> `public TemplateBinding([InheritDataTypeFrom(InheritDataTypeFromScopeKind.ControlTemplate)] AvaloniaProperty property) {`
- `public sealed partial class TemplateBinding : BindingBase {`

#### `src/Avalonia.Base/IOptionalFeatureProvider.cs`

- Namespace(s): `Avalonia`
- `public interface IOptionalFeatureProvider {`
- `IOptionalFeatureProvider` -> `public object? TryGetFeature(Type featureType);`
- `OptionalFeatureProviderExtensions` -> `public static T? TryGetFeature<T>(this IOptionalFeatureProvider provider) where T : class =>`
- `OptionalFeatureProviderExtensions` -> `public static bool TryGetFeature<T>(this IOptionalFeatureProvider provider, [MaybeNullWhen(false)] out T rv) where T : class {`
- `public static class OptionalFeatureProviderExtensions {`

#### `src/Avalonia.Base/Input/ContextRequestedEventArgs.cs`

- `ContextRequestedEventArgs` -> `public ContextRequestedEventArgs() : base(InputElement.ContextRequestedEvent) {`
- `ContextRequestedEventArgs` -> `public bool TryGetPosition(InputElement? relativeTo, out Point point) {`

#### `src/Avalonia.Base/Input/Cursor.cs`

- `Cursor` -> `public Cursor(Bitmap cursor, PixelPoint hotSpot) : this(GetCursorFactory().CreateCursor(cursor, hotSpot), "BitmapCursor") {`

#### `src/Avalonia.Base/Input/DataFormats.cs`

- Namespace(s): `Avalonia.Input`
- `public static class DataFormats;`

#### `src/Avalonia.Base/Input/DataObject.cs`

- Namespace(s): `Avalonia.Input`
- `public sealed class DataObject;`

#### `src/Avalonia.Base/Input/DragEventArgs.cs`

- `public class DragEventArgs : RoutedEventArgs, IKeyModifiersEventArgs {`

#### `src/Avalonia.Base/Input/FindNextElementOptions.cs`

- `FindNextElementOptions` -> `public InputElement? SearchRoot { get; init; }`
- `FindNextElementOptions` -> `public Rect ExclusionRect { get; init; }`
- `FindNextElementOptions` -> `public Rect? FocusHintRectangle { get; init; }`
- `FindNextElementOptions` -> `public XYFocusNavigationStrategy? NavigationStrategyOverride { get; init; }`
- `FindNextElementOptions` -> `public bool IgnoreOcclusivity { get; init; }`
- `public sealed class FindNextElementOptions {`

#### `src/Avalonia.Base/Input/FocusChangingEventArgs.cs`

- `FocusChangingEventArgs` -> `public IInputElement? NewFocusedElement { get; internal set; }`
- `FocusChangingEventArgs` -> `public IInputElement? OldFocusedElement { get; init; }`
- `FocusChangingEventArgs` -> `public KeyModifiers KeyModifiers { get; init; }`
- `FocusChangingEventArgs` -> `public NavigationMethod NavigationMethod { get; init; }`
- `FocusChangingEventArgs` -> `public bool Canceled { get; private set; }`
- `FocusChangingEventArgs` -> `public bool TryCancel() {`
- `FocusChangingEventArgs` -> `public bool TrySetNewFocusedElement(IInputElement? inputElement) {`
- `public class FocusChangingEventArgs : RoutedEventArgs, IKeyModifiersEventArgs {`

#### `src/Avalonia.Base/Input/FocusManager.cs`

- `FocusManager` -> `public FocusManager() {`
- `FocusManager` -> `public FocusManager(IInputElement contentRoot) {`
- `FocusManager` -> `public IInputElement? FindFirstFocusableElement() {`
- `FocusManager` -> `public IInputElement? FindLastFocusableElement() {`
- `FocusManager` -> `public IInputElement? FindNextElement(NavigationDirection direction) {`
- `FocusManager` -> `public IInputElement? FindNextElement(NavigationDirection direction, FindNextElementOptions options) {`
- `FocusManager` -> `public bool TryMoveFocus(NavigationDirection direction) {`
- `FocusManager` -> `public bool TryMoveFocus(NavigationDirection direction, FindNextElementOptions options) {`
- `FocusManager` -> `public static IInputElement? FindFirstFocusableElement(IInputElement searchScope) {`
- `FocusManager` -> `public static IInputElement? FindLastFocusableElement(IInputElement searchScope) {`

#### `src/Avalonia.Base/Input/GestureRecognizers/ScrollGestureRecognizer.cs`

- `ScrollGestureRecognizer` -> `public static readonly DirectProperty<ScrollGestureRecognizer, bool> IsScrollInertiaEnabledProperty = AvaloniaProperty.RegisterDirect<ScrollGestureRecognizer, bool>(nameof(IsScrollInertiaEnabled), o => o.IsScrollInertiaEnabled, (o, v) => o.IsScrollInertiaEnabled = v);`

#### `src/Avalonia.Base/Input/GestureRecognizers/SwipeGestureRecognizer.cs`

- `SwipeGestureRecognizer` -> `public bool IsEnabled {`
- `public class SwipeGestureRecognizer : GestureRecognizer {`
- `SwipeGestureRecognizer` -> `public double CrossAxisCancelThreshold {`
- `SwipeGestureRecognizer` -> `public double EdgeSize {`
- `SwipeGestureRecognizer` -> `public double Threshold {`
- `SwipeGestureRecognizer` -> `public static readonly StyledProperty<bool> IsEnabledProperty = AvaloniaProperty.Register<SwipeGestureRecognizer, bool>(nameof(IsEnabled), true);`
- `SwipeGestureRecognizer` -> `public static readonly StyledProperty<double> CrossAxisCancelThresholdProperty = AvaloniaProperty.Register<SwipeGestureRecognizer, double>( nameof(CrossAxisCancelThreshold), 8d);`
- `SwipeGestureRecognizer` -> `public static readonly StyledProperty<double> EdgeSizeProperty = AvaloniaProperty.Register<SwipeGestureRecognizer, double>(nameof(EdgeSize), 0d);`
- `SwipeGestureRecognizer` -> `public static readonly StyledProperty<double> ThresholdProperty = AvaloniaProperty.Register<SwipeGestureRecognizer, double>(nameof(Threshold), 30d);`

#### `src/Avalonia.Base/Input/GotFocusEventArgs.cs`

- `public class GotFocusEventArgs : RoutedEventArgs, IKeyModifiersEventArgs {`

#### `src/Avalonia.Base/Input/IInputRoot.cs`

- `IInputRoot` -> `public IFocusManager? FocusManager { get; }`
- `IInputRoot` -> `public InputElement FocusRoot { get; }`
- `public interface IInputRoot {`

#### `src/Avalonia.Base/Input/IKeyModifiersEventArgs.cs`

- Namespace(s): `Avalonia.Input`
- `IKeyModifiersEventArgs` -> `KeyModifiers KeyModifiers { get; }`
- `public interface IKeyModifiersEventArgs {`

#### `src/Avalonia.Base/Input/InputElement.Gestures.cs`

- `InputElement` -> `public event EventHandler<PinchEndedEventArgs>? PinchEnded {`
- `InputElement` -> `public event EventHandler<PinchEventArgs>? Pinch {`
- `InputElement` -> `public event EventHandler<PointerDeltaEventArgs>? PointerTouchPadGestureMagnify {`
- `InputElement` -> `public event EventHandler<PointerDeltaEventArgs>? PointerTouchPadGestureRotate {`
- `InputElement` -> `public event EventHandler<PointerDeltaEventArgs>? PointerTouchPadGestureSwipe {`
- `InputElement` -> `public event EventHandler<PullGestureEndedEventArgs>? PullGestureEnded {`
- `InputElement` -> `public event EventHandler<PullGestureEventArgs>? PullGesture {`
- `InputElement` -> `public event EventHandler<ScrollGestureEndedEventArgs>? ScrollGestureEnded {`
- `InputElement` -> `public event EventHandler<ScrollGestureEventArgs>? ScrollGesture {`
- `InputElement` -> `public event EventHandler<ScrollGestureInertiaStartingEventArgs>? ScrollGestureInertiaStarting {`
- `InputElement` -> `public event EventHandler<SwipeGestureEventArgs>? SwipeGesture {`
- `InputElement` -> `public event EventHandler<TappedEventArgs>? RightTapped {`
- `public partial class InputElement {`
- `InputElement` -> `public static bool GetIsHoldWithMouseEnabled(StyledElement element) {`
- `InputElement` -> `public static bool GetIsHoldingEnabled(StyledElement element) {`
- `InputElement` -> `public static readonly AttachedProperty<bool> IsHoldWithMouseEnabledProperty = AvaloniaProperty.RegisterAttached<StyledElement, bool>("IsHoldWithMouseEnabled", typeof(InputElement), false);`
- `InputElement` -> `public static readonly AttachedProperty<bool> IsHoldingEnabledProperty = AvaloniaProperty.RegisterAttached<StyledElement, bool>("IsHoldingEnabled", typeof(InputElement), true);`
- `InputElement` -> `public static readonly RoutedEvent<HoldingRoutedEventArgs> HoldingEvent = RoutedEvent.Register<InputElement, HoldingRoutedEventArgs>( nameof(Holding), RoutingStrategies.Bubble);`
- `InputElement` -> `public static readonly RoutedEvent<PinchEndedEventArgs> PinchEndedEvent = RoutedEvent.Register<InputElement, PinchEndedEventArgs>( nameof(PinchEnded), RoutingStrategies.Bubble);`
- `InputElement` -> `public static readonly RoutedEvent<PinchEventArgs> PinchEvent = RoutedEvent.Register<InputElement, PinchEventArgs>( nameof(Pinch), RoutingStrategies.Bubble);`
- `InputElement` -> `public static readonly RoutedEvent<PointerDeltaEventArgs> PointerTouchPadGestureMagnifyEvent = RoutedEvent.Register<InputElement, PointerDeltaEventArgs>( nameof(PointerTouchPadGestureMagnify), RoutingStrategies.Bubble);`
- `InputElement` -> `public static readonly RoutedEvent<PointerDeltaEventArgs> PointerTouchPadGestureRotateEvent = RoutedEvent.Register<InputElement, PointerDeltaEventArgs>( nameof(PointerTouchPadGestureRotate), RoutingStrategies.Bubble);`
- `InputElement` -> `public static readonly RoutedEvent<PointerDeltaEventArgs> PointerTouchPadGestureSwipeEvent = RoutedEvent.Register<InputElement, PointerDeltaEventArgs>( nameof(PointerTouchPadGestureSwipe), RoutingStrategies.Bubble);`
- `InputElement` -> `public static readonly RoutedEvent<PullGestureEndedEventArgs> PullGestureEndedEvent = RoutedEvent.Register<InputElement, PullGestureEndedEventArgs>( nameof(PullGestureEnded), RoutingStrategies.Bubble);`
- `InputElement` -> `public static readonly RoutedEvent<PullGestureEventArgs> PullGestureEvent = RoutedEvent.Register<InputElement, PullGestureEventArgs>( nameof(PullGesture), RoutingStrategies.Bubble);`
- `InputElement` -> `public static readonly RoutedEvent<ScrollGestureEndedEventArgs> ScrollGestureEndedEvent = RoutedEvent.Register<InputElement, ScrollGestureEndedEventArgs>( nameof(ScrollGestureEnded), RoutingStrategies.Bubble);`
- `InputElement` -> `public static readonly RoutedEvent<ScrollGestureEventArgs> ScrollGestureEvent = RoutedEvent.Register<InputElement, ScrollGestureEventArgs>( nameof(ScrollGesture), RoutingStrategies.Bubble);`
- `InputElement` -> `public static readonly RoutedEvent<ScrollGestureInertiaStartingEventArgs> ScrollGestureInertiaStartingEvent = RoutedEvent.Register<InputElement, ScrollGestureInertiaStartingEventArgs>( nameof(ScrollGestureInertiaStarting), RoutingStrategies.Bubble);`
- `InputElement` -> `public static readonly RoutedEvent<SwipeGestureEventArgs> SwipeGestureEvent = RoutedEvent.Register<InputElement, SwipeGestureEventArgs>( nameof(SwipeGesture), RoutingStrategies.Bubble);`
- `InputElement` -> `public static readonly RoutedEvent<TappedEventArgs> DoubleTappedEvent = RoutedEvent.Register<InputElement, TappedEventArgs>( nameof(DoubleTapped), RoutingStrategies.Bubble);`
- `InputElement` -> `public static readonly RoutedEvent<TappedEventArgs> RightTappedEvent = RoutedEvent.Register<InputElement, TappedEventArgs>( nameof(RightTapped), RoutingStrategies.Bubble);`
- `InputElement` -> `public static readonly RoutedEvent<TappedEventArgs> TappedEvent = RoutedEvent.Register<InputElement, TappedEventArgs>( nameof(Tapped), RoutingStrategies.Bubble);`
- `InputElement` -> `public static void SetIsHoldWithMouseEnabled(StyledElement element, bool value) {`
- `InputElement` -> `public static void SetIsHoldingEnabled(StyledElement element, bool value) {`

#### `src/Avalonia.Base/Input/InputElement.cs`

- `InputElement` -> `public event EventHandler<ContextRequestedEventArgs>? ContextRequested {`
- `InputElement` -> `public event EventHandler<FocusChangingEventArgs>? GettingFocus {`
- `InputElement` -> `public event EventHandler<FocusChangingEventArgs>? LosingFocus {`
- `InputElement` -> `public event EventHandler<RoutedEventArgs>? ContextCanceled {`
- `public partial class InputElement : Interactive, IInputElement {`
- `InputElement` -> `public static readonly RoutedEvent<ContextRequestedEventArgs> ContextRequestedEvent = RoutedEvent.Register<InputElement, ContextRequestedEventArgs>( nameof(ContextRequested), RoutingStrategies.Tunnel | RoutingStrategies.Bubble);`
- `InputElement` -> `public static readonly RoutedEvent<FocusChangingEventArgs> GettingFocusEvent = RoutedEvent.Register<InputElement, FocusChangingEventArgs>(nameof(GettingFocus), RoutingStrategies.Bubble);`
- `InputElement` -> `public static readonly RoutedEvent<FocusChangingEventArgs> LosingFocusEvent = RoutedEvent.Register<InputElement, FocusChangingEventArgs>(nameof(LosingFocus), RoutingStrategies.Bubble);`
- `InputElement` -> `public static readonly RoutedEvent<RoutedEventArgs> ContextCanceledEvent = RoutedEvent.Register<InputElement, RoutedEventArgs>( nameof(ContextCanceled), RoutingStrategies.Tunnel | RoutingStrategies.Bubble);`

#### `src/Avalonia.Base/Input/KeyEventArgs.cs`

- Namespace(s): `Avalonia.Input`
- `public class KeyEventArgs : RoutedEventArgs, IKeyModifiersEventArgs {`

#### `src/Avalonia.Base/Input/KeyboardDevice.cs`

- `KeyboardDevice` -> `public void SetFocusedElement( IInputElement? element, NavigationMethod method, KeyModifiers keyModifiers, bool isFocusChangeCancellable) {`

#### `src/Avalonia.Base/Input/PinchEventArgs.cs`

- `PinchEndedEventArgs` -> `public PinchEndedEventArgs() : base(InputElement.PinchEndedEvent) {`
- `PinchEventArgs` -> `public PinchEventArgs(double scale, Point scaleOrigin) : base(InputElement.PinchEvent) {`
- `PinchEventArgs` -> `public PinchEventArgs(double scale, Point scaleOrigin, double angle, double angleDelta) : base(InputElement.PinchEvent) {`

#### `src/Avalonia.Base/Input/PointerEventArgs.cs`

- `public class PointerEventArgs : RoutedEventArgs, IKeyModifiersEventArgs {`

#### `src/Avalonia.Base/Input/PullGestureEventArgs.cs`

- `PullGestureEndedEventArgs` -> `public PullGestureEndedEventArgs(int id, PullDirection pullDirection) : base(InputElement.PullGestureEndedEvent) {`
- `PullGestureEventArgs` -> `public PullGestureEventArgs(int id, Vector delta, PullDirection pullDirection) : base(InputElement.PullGestureEvent) {`

#### `src/Avalonia.Base/Input/Raw/RawKeyEventArgs.cs`

- `RawKeyEventArgs` -> `public RawKeyEventArgs( IInputDevice device, ulong timestamp, IInputRoot root, RawKeyEventType type, Key key, RawInputModifiers modifiers, PhysicalKey physicalKey, string? keySymbol, KeyDeviceType keyDeviceType = KeyDeviceType.Keyboard) : base(device, timestamp, root) {`

#### `src/Avalonia.Base/Input/ScrollGestureEventArgs.cs`

- `ScrollGestureEndedEventArgs` -> `public ScrollGestureEndedEventArgs(int id) : base(InputElement.ScrollGestureEndedEvent) {`
- `ScrollGestureEventArgs` -> `public ScrollGestureEventArgs(int id, Vector delta) : base(InputElement.ScrollGestureEvent) {`

#### `src/Avalonia.Base/Input/SwipeGestureEventArgs.cs`

- `SwipeGestureEventArgs` -> `public Point StartPoint { get; }`
- `SwipeGestureEventArgs` -> `public SwipeDirection SwipeDirection { get; }`
- `SwipeGestureEventArgs` -> `public SwipeGestureEventArgs(int id, SwipeDirection direction, Vector delta, Point startPoint) : base(InputElement.SwipeGestureEvent) {`
- `SwipeGestureEventArgs` -> `public Vector Delta { get; }`
- `public class SwipeGestureEventArgs : RoutedEventArgs {`
- `public enum SwipeDirection { Left, Right, Up, Down }`
- `SwipeGestureEventArgs` -> `public int Id { get; }`

#### `src/Avalonia.Base/Input/TappedEventArgs.cs`

- `public class TappedEventArgs : RoutedEventArgs, IKeyModifiersEventArgs {`

#### `src/Avalonia.Base/Input/WindowDecorationsElementRole.cs`

- Namespace(s): `Avalonia.Input`
- `public enum WindowDecorationsElementRole {`

#### `src/Avalonia.Base/Layout/LayoutHelper.cs`

- `LayoutHelper` -> `public static Point RoundLayoutPoint(Point point, double dpiScale) {`
- `LayoutHelper` -> `public static Size RoundLayoutSizeUp(Size size, double dpiScale) {`
- `LayoutHelper` -> `public static Thickness RoundLayoutThickness(Thickness thickness, double dpiScale) {`
- `LayoutHelper` -> `public static double GetLayoutScale(Layoutable control) => control.GetLayoutRoot()?.LayoutScaling ?? 1.0;`

#### `src/Avalonia.Base/Layout/Layoutable.cs`

- `Layoutable` -> `public void UpdateLayout() => this.GetLayoutManager()?.ExecuteLayoutPass();`

#### `src/Avalonia.Base/Logging/LogArea.cs`

- `LogArea` -> `public const string Fonts = nameof(Fonts);`

#### `src/Avalonia.Base/Media/BaselinePixelAlignment.cs`

- `public enum BaselinePixelAlignment : byte {`

#### `src/Avalonia.Base/Media/BitmapCache.cs`

- Namespace(s): `Avalonia.Media`
- `BitmapCache` -> `public bool EnableClearType {`
- `BitmapCache` -> `public bool SnapsToDevicePixels {`
- `public class BitmapCache : CacheMode {`
- `BitmapCache` -> `public double RenderAtScale {`
- `BitmapCache` -> `public static readonly StyledProperty<bool> EnableClearTypeProperty = AvaloniaProperty.Register<BitmapCache, bool>( nameof(EnableClearType));`
- `BitmapCache` -> `public static readonly StyledProperty<bool> SnapsToDevicePixelsProperty = AvaloniaProperty.Register<BitmapCache, bool>( nameof(SnapsToDevicePixels));`
- `BitmapCache` -> `public static readonly StyledProperty<double> RenderAtScaleProperty = AvaloniaProperty.Register<BitmapCache, double>( nameof(RenderAtScale), 1);`

#### `src/Avalonia.Base/Media/CacheMode.cs`

- Namespace(s): `Avalonia.Media`
- `public abstract class CacheMode : StyledElement {`
- `CacheMode` -> `public static CacheMode Parse(string s) {`

#### `src/Avalonia.Base/Media/DrawingContext.cs`

- `DrawingContext` -> `public PushedState PushTextOptions(TextOptions textOptions) {`

#### `src/Avalonia.Base/Media/DrawingImage.cs`

- `DrawingImage` -> `public Rect? Viewbox {`
- `DrawingImage` -> `public Size Size => GetBounds().Size;`
- `DrawingImage` -> `public static readonly StyledProperty<Rect?> ViewboxProperty = AvaloniaProperty.Register<DrawingImage, Rect?>(nameof(Viewbox));`

#### `src/Avalonia.Base/Media/FontFeatureCollection.cs`

- Namespace(s): `Avalonia.Media`
- `FontFeatureCollection` -> `public FontFeatureCollection() {`
- `FontFeatureCollection` -> `public FontFeatureCollection(IEnumerable<FontFeature> fontFeatures) : base(fontFeatures) {`
- `FontFeatureCollection` -> `public FontFeatureCollection(int capacity) : base(capacity) {`
- `FontFeatureCollection` -> `public static FontFeatureCollection Parse(string s) {`

#### `src/Avalonia.Base/Media/FontManager.cs`

- `FontManager` -> `public IFontCollection SystemFonts {`
- `FontManager` -> `public bool TryGetGlyphTypeface(Typeface typeface, [NotNullWhen(true)] out GlyphTypeface? glyphTypeface) {`

#### `src/Avalonia.Base/Media/FontMetrics.cs`

- `FontMetrics` -> `public ushort DesignEmHeight { get; init; }`

#### `src/Avalonia.Base/Media/Fonts/EmbeddedFontCollection.cs`

- `public class EmbeddedFontCollection : FontCollectionBase {`

#### `src/Avalonia.Base/Media/Fonts/FontCollectionBase.cs`

- `FontCollectionBase` -> `public FontFamily this[int index] => _fontFamilies[index];`
- `FontCollectionBase` -> `public IEnumerator<FontFamily> GetEnumerator() => ((IEnumerable<FontFamily>)_fontFamilies).GetEnumerator();`
- `FontCollectionBase` -> `public bool TryAddFontSource(Uri source) {`
- `FontCollectionBase` -> `public bool TryAddGlyphTypeface(GlyphTypeface glyphTypeface) {`
- `FontCollectionBase` -> `public bool TryAddGlyphTypeface(GlyphTypeface glyphTypeface, FontCollectionKey key) {`
- `FontCollectionBase` -> `public bool TryAddGlyphTypeface(Stream stream, [NotNullWhen(true)] out GlyphTypeface? glyphTypeface) {`
- `FontCollectionBase` -> `public bool TryGetNearestMatch(string familyName, FontStyle style, FontWeight weight, FontStretch stretch, [NotNullWhen(true)] out GlyphTypeface? glyphTypeface) {`
- `FontCollectionBase` -> `public int Count => _fontFamilies.Length;`
- `FontCollectionBase` -> `public virtual bool TryCreateSyntheticGlyphTypeface( GlyphTypeface glyphTypeface, FontStyle style, FontWeight weight, FontStretch stretch, [NotNullWhen(true)] out GlyphTypeface? syntheticGlyphTypeface) {`
- `FontCollectionBase` -> `public virtual bool TryGetFamilyTypefaces(string familyName, [NotNullWhen(true)] out IReadOnlyList<Typeface>? familyTypefaces) {`
- `FontCollectionBase` -> `public virtual bool TryGetGlyphTypeface(string familyName, FontStyle style, FontWeight weight, FontStretch stretch, [NotNullWhen(true)] out GlyphTypeface? glyphTypeface) {`

#### `src/Avalonia.Base/Media/Fonts/IFontCollection.cs`

- `IFontCollection` -> `bool TryCreateSyntheticGlyphTypeface(GlyphTypeface glyphTypeface, FontStyle style, FontWeight weight, FontStretch stretch, [NotNullWhen(true)] out GlyphTypeface? syntheticGlyphTypeface);`
- `IFontCollection` -> `bool TryGetFamilyTypefaces(string familyName, [NotNullWhen(true)] out IReadOnlyList<Typeface>? familyTypefaces);`
- `IFontCollection` -> `bool TryGetGlyphTypeface(string familyName, FontStyle style, FontWeight weight, FontStretch stretch, [NotNullWhen(true)] out GlyphTypeface? glyphTypeface);`
- `IFontCollection` -> `bool TryGetNearestMatch(string familyName, FontStyle style, FontWeight weight, FontStretch stretch, [NotNullWhen(true)] out GlyphTypeface? glyphTypeface);`

#### `src/Avalonia.Base/Media/Fonts/OpenTypeTag.cs`

- `OpenTypeTag` -> `public OpenTypeTag(char c1, char c2, char c3, char c4) {`
- `OpenTypeTag` -> `public OpenTypeTag(uint value) {`
- `OpenTypeTag` -> `public override string ToString() {`
- `public readonly record struct OpenTypeTag {`
- `OpenTypeTag` -> `public static OpenTypeTag Parse(string tag) {`
- `OpenTypeTag` -> `public static implicit operator OpenTypeTag(uint tag) => new OpenTypeTag(tag);`
- `OpenTypeTag` -> `public static implicit operator uint(OpenTypeTag tag) => tag._value;`

#### `src/Avalonia.Base/Media/Fonts/Tables/Cmap/CharacterToGlyphMap.cs`

- `CharacterToGlyphMap` -> `public CodepointRangeEnumerator GetMappedRanges() {`
- `CharacterToGlyphMap` -> `public bool ContainsGlyph(int codePoint) {`
- `CharacterToGlyphMap` -> `public bool TryGetGlyph(int codePoint, out ushort glyphId) {`
- `public readonly struct CharacterToGlyphMap #pragma warning restore CA1815 {`
- `CharacterToGlyphMap` -> `public ushort GetGlyph(int codePoint) {`
- `CharacterToGlyphMap` -> `public ushort this[int codePoint] {`
- `CharacterToGlyphMap` -> `public void GetGlyphs(ReadOnlySpan<int> codePoints, Span<ushort> glyphIds) {`

#### `src/Avalonia.Base/Media/Fonts/Tables/Cmap/CodepointRange.cs`

- `CodepointRange` -> `public CodepointRange(int start, int end) {`
- `CodepointRange` -> `public override bool Equals(object? obj) {`
- `CodepointRange` -> `public override int GetHashCode() {`
- `CodepointRange` -> `public readonly int End;`
- `CodepointRange` -> `public readonly int Start;`
- `public readonly struct CodepointRange {`
- `CodepointRange` -> `public static bool operator !=(CodepointRange left, CodepointRange right) {`
- `CodepointRange` -> `public static bool operator ==(CodepointRange left, CodepointRange right) {`

#### `src/Avalonia.Base/Media/Fonts/Tables/Cmap/CodepointRangeEnumerator.cs`

- `CodepointRangeEnumerator` -> `public CodepointRange Current { get; private set; }`
- `CodepointRangeEnumerator` -> `public bool MoveNext() {`
- `public ref struct CodepointRangeEnumerator {`

#### `src/Avalonia.Base/Media/GlyphMetrics.cs`

- `GlyphMetrics` -> `public int YBearing { get; init; }`
- `GlyphMetrics` -> `public ushort Height { get; init; }`
- `GlyphMetrics` -> `public ushort Width { get; init; }`

#### `src/Avalonia.Base/Media/GlyphRun.cs`

- `GlyphRun` -> `public GlyphRun( GlyphTypeface glyphTypeface, double fontRenderingEmSize, ReadOnlyMemory<char> characters, IReadOnlyList<GlyphInfo> glyphInfos, Point? baselineOrigin = null, int biDiLevel = 0) {`
- `GlyphRun` -> `public GlyphRun( GlyphTypeface glyphTypeface, double fontRenderingEmSize, ReadOnlyMemory<char> characters, IReadOnlyList<ushort> glyphIndices, Point? baselineOrigin = null, int biDiLevel = 0) : this(glyphTypeface, fontRenderingEmSize, characters, CreateGlyphInfos(glyphIndices, fontRenderingEmSize, glyphTypeface), baselineOrigin, biDiLevel) {`
- `GlyphRun` -> `public GlyphTypeface GlyphTypeface { get; }`

#### `src/Avalonia.Base/Media/GlyphTypeface.cs`

- `GlyphTypeface` -> `public CharacterToGlyphMap CharacterToGlyphMap => _cmapTable;`
- `GlyphTypeface` -> `public FontMetrics Metrics { get; }`
- `GlyphTypeface` -> `public FontSimulations FontSimulations { get; }`
- `GlyphTypeface` -> `public FontStretch Stretch { get; }`
- `GlyphTypeface` -> `public FontStyle Style { get; }`
- `GlyphTypeface` -> `public FontWeight Weight { get; }`
- `GlyphTypeface` -> `public GlyphTypeface(IPlatformTypeface typeface, FontSimulations fontSimulations = FontSimulations.None) {`
- `GlyphTypeface` -> `public IPlatformTypeface PlatformTypeface { get; }`
- `GlyphTypeface` -> `public IReadOnlyDictionary<CultureInfo, string> FaceNames { get; }`
- `GlyphTypeface` -> `public IReadOnlyDictionary<CultureInfo, string> FamilyNames { get; }`
- `GlyphTypeface` -> `public IReadOnlyList<OpenTypeTag> SupportedFeatures {`
- `GlyphTypeface` -> `public ITextShaperTypeface TextShaperTypeface {`
- `GlyphTypeface` -> `public bool TryGetGlyphMetrics(ReadOnlySpan<ushort> glyphIds, Span<GlyphMetrics> metrics) {`
- `GlyphTypeface` -> `public bool TryGetGlyphMetrics(ushort glyph, out GlyphMetrics metrics) {`
- `GlyphTypeface` -> `public bool TryGetHorizontalGlyphAdvance(ushort glyphId, out ushort advance) {`
- `GlyphTypeface` -> `public bool TryGetHorizontalGlyphAdvances(ReadOnlySpan<ushort> glyphIds, Span<ushort> advances) {`
- `GlyphTypeface` -> `public int GlyphCount { get; }`
- `public sealed class GlyphTypeface {`
- `GlyphTypeface` -> `public string FamilyName { get; }`
- `GlyphTypeface` -> `public string TypographicFamilyName { get; }`
- `GlyphTypeface` -> `public void Dispose() {`

#### `src/Avalonia.Base/Media/IFontMemory.cs`

- `IFontMemory` -> `bool TryGetTable(OpenTypeTag tag, out ReadOnlyMemory<byte> table);`
- `public interface IFontMemory : IDisposable {`

#### `src/Avalonia.Base/Media/IPlatformTypeface.cs`

- `IPlatformTypeface` -> `FontSimulations FontSimulations { get; }`
- `IPlatformTypeface` -> `FontStretch Stretch { get; }`
- `IPlatformTypeface` -> `FontStyle Style { get; }`
- `IPlatformTypeface` -> `FontWeight Weight { get; }`
- `IPlatformTypeface` -> `bool TryGetStream([NotNullWhen(true)] out Stream? stream);`
- `public interface IPlatformTypeface : IFontMemory {`
- `IPlatformTypeface` -> `string FamilyName { get; }`

#### `src/Avalonia.Base/Media/ITextShaperTypeface.cs`

- `public interface ITextShaperTypeface : IDisposable {`

#### `src/Avalonia.Base/Media/Imaging/Bitmap.cs`

- `Bitmap` -> `public virtual AlphaFormat? AlphaFormat => (PlatformImpl.Item as IReadableBitmapImpl)?.AlphaFormat;`
- `Bitmap` -> `public void CopyPixels(ILockedFramebuffer buffer) {`

#### `src/Avalonia.Base/Media/StreamGeometryContext.cs`

- `public class StreamGeometryContext : IGeometryContext {`
- `StreamGeometryContext` -> `public void ArcTo(Point point, Size size, double rotationAngle, bool isLargeArc, SweepDirection sweepDirection, bool isStroked = true) {`
- `StreamGeometryContext` -> `public void BeginFigure(Point startPoint, bool isFilled = true) {`
- `StreamGeometryContext` -> `public void CubicBezierTo(Point controlPoint1, Point controlPoint2, Point endPoint, bool isStroked = true) {`
- `StreamGeometryContext` -> `public void LineTo(Point point, bool isStroked = true) {`
- `StreamGeometryContext` -> `public void QuadraticBezierTo(Point controlPoint, Point endPoint, bool isStroked = true) {`

#### `src/Avalonia.Base/Media/TextFormatting/GenericTextParagraphProperties.cs`

- `GenericTextParagraphProperties` -> `public GenericTextParagraphProperties( FlowDirection flowDirection, TextAlignment textAlignment, bool firstLineInParagraph, bool alwaysCollapsible, TextRunProperties defaultTextRunProperties, TextWrapping textWrapping, double lineHeight, double indent, double letterSpacing) {`
- `GenericTextParagraphProperties` -> `public GenericTextParagraphProperties(TextRunProperties defaultTextRunProperties, TextAlignment textAlignment = TextAlignment.Left, TextWrapping textWrapping = TextWrapping.NoWrap, double lineHeight = 0, double letterSpacing = 0) {`

#### `src/Avalonia.Base/Media/TextFormatting/GenericTextRunProperties.cs`

- `GenericTextRunProperties` -> `public GenericTextRunProperties( Typeface typeface, double fontRenderingEmSize = DefaultFontRenderingEmSize, TextDecorationCollection? textDecorations = null, IBrush? foregroundBrush = null, IBrush? backgroundBrush = null, BaselineAlignment baselineAlignment = BaselineAlignment.Baseline, CultureInfo? cultureInfo = null, FontFeatureCollection? fontFeatures = null) {`

#### `src/Avalonia.Base/Media/TextFormatting/ShapedBuffer.cs`

- `ShapedBuffer` -> `public GlyphTypeface GlyphTypeface { get; }`
- `ShapedBuffer` -> `public ShapedBuffer(ReadOnlyMemory<char> text, int bufferLength, GlyphTypeface glyphTypeface, double fontRenderingEmSize, sbyte bidiLevel) {`

#### `src/Avalonia.Base/Media/TextFormatting/TextCollapsingProperties.cs`

- `TextCollapsingProperties` -> `public static TextRun[] CreateCollapsedRuns(TextLine textLine, int collapsedLength, TextRun shapedSymbol) {`

#### `src/Avalonia.Base/Media/TextFormatting/TextLayout.cs`

- `TextLayout` -> `public TextLayout( string? text, Typeface typeface, double fontSize = GenericTextRunProperties.DefaultFontRenderingEmSize, IBrush? foreground = null, TextAlignment textAlignment = TextAlignment.Left, TextWrapping textWrapping = TextWrapping.NoWrap, TextTrimming? textTrimming = null, TextDecorationCollection? textDecorations = null, FlowDirection flowDirection = FlowDirection.LeftToRight, double maxWidth = double.PositiveInfinity, double maxHeight = double.PositiveInfinity, double lineHeight = double.NaN, double letterSpacing = 0, int maxLines = 0, FontFeatureCollection? fontFeatures = null, IReadOnlyList<ValueSpan<TextRunProperties>>? textStyleOverrides = null) {`

#### `src/Avalonia.Base/Media/TextFormatting/TextMetrics.cs`

- `TextMetrics` -> `public TextMetrics(GlyphTypeface glyphTypeface, double fontRenderingEmSize) {`

#### `src/Avalonia.Base/Media/TextFormatting/TextShaperOptions.cs`

- `TextShaperOptions` -> `public GlyphTypeface GlyphTypeface { get; }`
- `TextShaperOptions` -> `public TextShaperOptions( GlyphTypeface typeface, double fontRenderingEmSize = GenericTextRunProperties.DefaultFontRenderingEmSize, sbyte bidiLevel = 0, CultureInfo? culture = null, double incrementalTabWidth = 0, double letterSpacing = 0, IReadOnlyList<FontFeature>? fontFeatures = null) {`

#### `src/Avalonia.Base/Media/TextHintingMode.cs`

- `public enum TextHintingMode : byte {`

#### `src/Avalonia.Base/Media/TextOptions.cs`

- `TextOptions` -> `public BaselinePixelAlignment BaselinePixelAlignment { get; init; }`
- `TextOptions` -> `public TextHintingMode TextHintingMode { get; init; }`
- `TextOptions` -> `public TextOptions MergeWith(TextOptions other) {`
- `TextOptions` -> `public TextRenderingMode TextRenderingMode { get; init; }`
- `public readonly record struct TextOptions {`
- `TextOptions` -> `public static BaselinePixelAlignment GetBaselinePixelAlignment(Visual visual) {`
- `TextOptions` -> `public static TextHintingMode GetTextHintingMode(Visual visual) {`
- `TextOptions` -> `public static TextOptions GetTextOptions(Visual visual) {`
- `TextOptions` -> `public static TextRenderingMode GetTextRenderingMode(Visual visual) {`
- `TextOptions` -> `public static void SetBaselinePixelAlignment(Visual visual, BaselinePixelAlignment value) {`
- `TextOptions` -> `public static void SetTextHintingMode(Visual visual, TextHintingMode value) {`
- `TextOptions` -> `public static void SetTextOptions(Visual visual, TextOptions value) {`
- `TextOptions` -> `public static void SetTextRenderingMode(Visual visual, TextRenderingMode value) {`

#### `src/Avalonia.Base/Media/Typeface.cs`

- `Typeface` -> `public GlyphTypeface GlyphTypeface {`
- `Typeface` -> `public Typeface Normalize(out string normalizedFamilyName) {`

#### `src/Avalonia.Base/Metadata/ConstructorArgumentAttribute.cs`

- Namespace(s): `Avalonia.Metadata`
- `public sealed class ConstructorArgumentAttribute(string name) : Attribute {`
- `ConstructorArgumentAttribute` -> `public string Name { get; } = name;`

#### `src/Avalonia.Base/Platform/ICursorFactory.cs`

- `ICursorFactory` -> `ICursorImpl CreateCursor(Bitmap cursor, PixelPoint hotSpot);`

#### `src/Avalonia.Base/Platform/IDrawingContextImpl.cs`

- `IDrawingContextLayerImpl` -> `IDrawingContextImpl CreateDrawingContext();`
- `IDrawingContextLayerImpl` -> `bool IsCorrupted { get; }`
- `public interface IDrawingContextLayerImpl : IBitmapImpl {`
- `IDrawingContextImpl` -> `void PopTextOptions();`
- `IDrawingContextImpl` -> `void PushTextOptions(TextOptions textOptions);`

#### `src/Avalonia.Base/Platform/IFontManagerImpl.cs`

- `IFontManagerImpl` -> `bool TryCreateGlyphTypeface(Stream stream, FontSimulations fontSimulations, [NotNullWhen(returnValue: true)] out IPlatformTypeface? platformTypeface);`
- `IFontManagerImpl` -> `bool TryCreateGlyphTypeface(string familyName, FontStyle style, FontWeight weight, FontStretch stretch, [NotNullWhen(returnValue: true)] out IPlatformTypeface? platformTypeface);`
- `IFontManagerImpl` -> `bool TryGetFamilyTypefaces(string familyName, [NotNullWhen(true)] out IReadOnlyList<Typeface>? familyTypefaces);`
- `IFontManagerImpl` -> `bool TryMatchCharacter(int codepoint, FontStyle fontStyle, FontWeight fontWeight, FontStretch fontStretch, string? familyName, CultureInfo? culture, [NotNullWhen(returnValue: true)] out IPlatformTypeface? platformTypeface);`

#### `src/Avalonia.Base/Platform/IGeometryContext.cs`

- `IGeometryContext` -> `void ArcTo(Point point, Size size, double rotationAngle, bool isLargeArc, SweepDirection sweepDirection, bool isStroked = true);`
- `IGeometryContext` -> `void CubicBezierTo(Point controlPoint1, Point controlPoint2, Point endPoint, bool isStroked = true);`
- `IGeometryContext` -> `void LineTo(Point point, bool isStroked = true);`
- `IGeometryContext` -> `void QuadraticBezierTo(Point controlPoint, Point endPoint, bool isStroked = true);`

#### `src/Avalonia.Base/Platform/ILockedFramebuffer.cs`

- `ILockedFramebuffer` -> `AlphaFormat AlphaFormat { get; }`

#### `src/Avalonia.Base/Platform/IPlatformRenderInterface.cs`

- `IPlatformRenderInterfaceContext` -> `IDrawingContextLayerImpl CreateOffscreenRenderTarget(PixelSize pixelSize, Vector scaling, bool enableTextAntialiasing);`
- `IPlatformRenderInterface` -> `IGlyphRunImpl CreateGlyphRun(GlyphTypeface glyphTypeface, double fontRenderingEmSize, IReadOnlyList<GlyphInfo> glyphInfos, Point baselineOrigin);`
- `IPlatformRenderInterfaceContext` -> `IRenderTarget CreateRenderTarget(IEnumerable<IPlatformRenderSurface> surfaces);`
- `IPlatformRenderInterfaceContext` -> `bool IsReadyToCreateRenderTarget(IEnumerable<IPlatformRenderSurface> surfaces) => true;`
- `IPlatformRenderInterfaceContext` -> `public PixelSize? MaxOffscreenRenderTargetPixelSize { get; }`

#### `src/Avalonia.Base/Platform/IReadableBitmapImpl.cs`

- Namespace(s): `Avalonia.Platform`
- `IReadableBitmapImpl` -> `AlphaFormat? AlphaFormat { get; }`
- `public interface IReadableBitmapImpl : IBitmapImpl {`

#### `src/Avalonia.Base/Platform/IRenderTarget.cs`

- `IRenderTarget` -> `IDrawingContextImpl CreateDrawingContext(RenderTargetSceneInfo sceneInfo, out RenderTargetDrawingContextProperties properties);`
- `IRenderTarget` -> `RenderTargetProperties Properties { get; }`
- `IRenderTarget` -> `bool IsCorrupted { get; }`
- `IRenderTarget` -> `bool IsReady => true;`
- `IRenderTarget` -> `public record struct RenderTargetSceneInfo(PixelSize Size, double Scaling);`

#### `src/Avalonia.Base/Platform/IRenderTargetBitmapImpl.cs`

- `IRenderTargetBitmapImpl` -> `IDrawingContextImpl CreateDrawingContext();`
- `public interface IRenderTargetBitmapImpl : IReadableBitmapImpl {`

#### `src/Avalonia.Base/Platform/ITextShaperImpl.cs`

- `ITextShaperImpl` -> `ITextShaperTypeface CreateTypeface(GlyphTypeface glyphTypeface);`

#### `src/Avalonia.Base/Platform/IWriteableBitmapImpl.cs`

- `public interface IWriteableBitmapImpl : IBitmapImpl, IReadableBitmapImpl {`

#### `src/Avalonia.Base/Platform/LockedFramebuffer.cs`

- `LockedFramebuffer` -> `public AlphaFormat AlphaFormat { get; }`
- `LockedFramebuffer` -> `public LockedFramebuffer(IntPtr address, PixelSize size, int rowBytes, Vector dpi, PixelFormat format, AlphaFormat alphaFormat, Action? onDispose) {`

#### `src/Avalonia.Base/Platform/LtrbRect.cs`

- Namespace(s): `Avalonia.Platform`
- `LtrbRect` -> `public LtrbRect Union(LtrbRect rect) {`
- `LtrbRect` -> `public bool Contains(LtrbRect rect) {`
- `LtrbRect` -> `public bool Contains(Point point) {`
- `LtrbRect` -> `public double Height => Bottom - Top;`
- `LtrbRect` -> `public double Width => Right - Left;`
- `LtrbRect` -> `public override string ToString() => $"{Left}:{Top}-{Right}:{Bottom} ({Width}x{Height})";`

#### `src/Avalonia.Base/Platform/PathGeometryContext.cs`

- `PathGeometryContext` -> `public void ArcTo(Point point, Size size, double rotationAngle, bool isLargeArc, SweepDirection sweepDirection, bool isStroked = true) {`
- `PathGeometryContext` -> `public void CubicBezierTo(Point controlPoint1, Point controlPoint2, Point endPoint, bool isStroked = true) {`
- `PathGeometryContext` -> `public void LineTo(Point point, bool isStroked = true) {`
- `PathGeometryContext` -> `public void QuadraticBezierTo(Point controlPoint , Point endPoint, bool isStroked = true) {`

#### `src/Avalonia.Base/Platform/Storage/SaveFilePickerResult.cs`

- Namespace(s): `Avalonia.Platform.Storage`
- `public readonly record struct SaveFilePickerResult {`

#### `src/Avalonia.Base/Platform/SurfaceOrientation.cs`

- Namespace(s): `Avalonia.Platform`
- `public enum SurfaceOrientation {`

#### `src/Avalonia.Base/Platform/Surfaces/IFramebufferPlatformSurface.cs`

- `IFramebufferRenderTarget` -> `ILockedFramebuffer Lock(IRenderTarget.RenderTargetSceneInfo sceneInfo, out FramebufferLockProperties properties);`
- `IFramebufferRenderTarget` -> `bool RetainsFrameContents => false;`
- `FuncFramebufferRenderTarget` -> `public FuncFramebufferRenderTarget(Func<ILockedFramebuffer> lockFramebuffer) : this((_, out properties) =>`
- `FuncFramebufferRenderTarget` -> `public FuncFramebufferRenderTarget(LockFramebufferDelegate lockFramebuffer, bool retainsFrameContents = false) {`
- `FuncFramebufferRenderTarget` -> `public ILockedFramebuffer Lock(IRenderTarget.RenderTargetSceneInfo sceneInfo, out FramebufferLockProperties properties) => _lockFramebuffer(sceneInfo, out properties);`
- `FuncFramebufferRenderTarget` -> `public bool RetainsFrameContents { get; }`
- `FuncFramebufferRenderTarget` -> `public delegate ILockedFramebuffer LockFramebufferDelegate(IRenderTarget.RenderTargetSceneInfo sceneInfo, out FramebufferLockProperties properties);`
- `public interface IFramebufferPlatformSurface : IPlatformRenderSurface {`
- `public interface IFramebufferRenderTarget : IDisposable, IPlatformRenderSurfaceRenderTarget {`

#### `src/Avalonia.Base/Platform/Surfaces/IPlatformRenderSurface.cs`

- Namespace(s): `Avalonia.Platform.Surfaces`
- `IPlatformRenderSurface` -> `bool IsReady => true;`
- `IPlatformRenderSurfaceRenderTarget` -> `bool IsReady => true;`
- `public interface IPlatformRenderSurface {`
- `public interface IPlatformRenderSurfaceRenderTarget {`

#### `src/Avalonia.Base/Rendering/Composition/CompositionOptions.cs`

- Namespace(s): `Avalonia.Rendering.Composition`
- `CompositionOptions` -> `public double? DirtyRectMergeEagerness { get; set; }`
- `CompositionOptions` -> `public int? MaxDirtyRects { get; set; }`

#### `src/Avalonia.Base/Rendering/Composition/Server/CompositorPools.cs`

- Namespace(s): `Avalonia.Rendering.Composition.Server`
- `StackPool` -> `public Stack<T> Rent() {`
- `public class StackPool<T> : Stack<Stack<T>> {`
- `StackPool` -> `public void Return(Stack<T>? stack) {`
- `StackPool` -> `public void Return(ref Stack<T> stack) {`

#### `src/Avalonia.Base/Rendering/Composition/Server/ServerCompositionVisual/ServerCompositionVisual.Readback.cs`

- Namespace(s): `Avalonia.Rendering.Composition.Server`
- `ReadbackData` -> `public LtrbRect? TransformedSubtreeBounds;`
- `ReadbackData` -> `public Matrix Matrix;`
- `ReadbackData` -> `public bool Visible;`
- `public class ReadbackData {`
- `ReadbackData` -> `public long TargetId;`
- `ReadbackData` -> `public ulong Revision;`

#### `src/Avalonia.Base/Rendering/Composition/Server/ServerCompositionVisual/ServerCompositionVisual.Walker.cs`

- Namespace(s): `Avalonia.Rendering.Composition.Server`
- `public record struct TreeWalkerFrame(ServerCompositionVisual Visual, int CurrentIndex);`

#### `src/Avalonia.Base/Rendering/Composition/Visual.cs`

- `CompositionVisual` -> `public bool DisableSubTreeBoundsHitTestOptimization => CustomHitTestCountInSubTree != 0;`

#### `src/Avalonia.Base/Rendering/IPresentationSource.cs`

- Namespace(s): `Avalonia.Rendering`
- `IPresentationSource` -> `public Visual? RootVisual { get; }`
- `IPresentationSource` -> `public double RenderScaling { get; }`
- `public interface IPresentationSource {`

#### `src/Avalonia.Base/Rendering/SceneInvalidatedEventArgs.cs`

- `SceneInvalidatedEventArgs` -> `public SceneInvalidatedEventArgs(Rect dirtyRect) {`

#### `src/Avalonia.Base/StyledElement.cs`

- `public class StyledElement : Animatable, IDataContextProvider, ILogical, IThemeVariantHost, IResourceHost, IStyleHost, ISetLogicalParent, ISetInheritanceParent, ISupportInitialize, INamed, IAvaloniaListItemValidator<ILogical> {`

#### `src/Avalonia.Base/StyledElementExtensions.cs`

- `StyledElementExtensions` -> `public static IDisposable BindClass(this StyledElement target, string className, BindingBase source, object anchor) =>`

#### `src/Avalonia.Base/Styling/StyleBase.cs`

- `public abstract class StyleBase : AvaloniaObject, IStyle, IResourceProvider, IAddChild {`

#### `src/Avalonia.Base/Threading/Dispatcher.Invoke.cs`

- Namespace(s): `Avalonia.Threading`
- `Dispatcher` -> `public DispatcherPriorityAwaitable Resume() =>`
- `Dispatcher` -> `public DispatcherPriorityAwaitable Resume(DispatcherPriority priority) {`
- `Dispatcher` -> `public static DispatcherPriorityAwaitable Yield() =>`
- `Dispatcher` -> `public static DispatcherPriorityAwaitable Yield(DispatcherPriority priority) {`

#### `src/Avalonia.Base/Threading/Dispatcher.ThreadStorage.cs`

- Namespace(s): `Avalonia.Threading`
- `Dispatcher` -> `public static Dispatcher CurrentDispatcher {`
- `Dispatcher` -> `public static Dispatcher? FromThread(Thread thread) {`
- `Dispatcher` -> `public static void InitializeUIThreadDispatcher(IDispatcherImpl impl) {`
- `Dispatcher` -> `public static void InitializeUIThreadDispatcher(IPlatformThreadingInterface impl) =>`

#### `src/Avalonia.Base/Threading/Dispatcher.cs`

- Namespace(s): `Avalonia.Threading`
- `Dispatcher` -> `public IDispatcherImpl PlatformImpl => _impl;`
- `Dispatcher` -> `public Thread Thread => _thread;`
- `Dispatcher` -> `public bool CheckAccess() => Thread.CurrentThread == _thread;`

#### `src/Avalonia.Base/Threading/DispatcherPriorityAwaitable.cs`

- Namespace(s): `Avalonia.Threading`
- `DispatcherPriorityAwaitable` -> `public DispatcherPriorityAwaiter GetAwaiter() => new(_dispatcher, _task, _priority);`
- `DispatcherPriorityAwaitable` -> `public DispatcherPriorityAwaiter<T> GetAwaiter() => new(_dispatcher, _task, _priority);`
- `DispatcherPriorityAwaiter` -> `public bool IsCompleted => false;`
- `public struct DispatcherPriorityAwaitable {`
- `public struct DispatcherPriorityAwaitable<T> {`
- `public struct DispatcherPriorityAwaiter : INotifyCompletion {`
- `public struct DispatcherPriorityAwaiter<T> : INotifyCompletion {`
- `DispatcherPriorityAwaiter` -> `public void GetResult() => _task.GetAwaiter().GetResult();`
- `DispatcherPriorityAwaiter` -> `public void GetResult() {`
- `DispatcherPriorityAwaiter` -> `public void OnCompleted(Action continuation) {`

#### `src/Avalonia.Base/Visual.cs`

- `Visual` -> `public CacheMode? CacheMode {`
- `Visual` -> `public static readonly StyledProperty<CacheMode?> CacheModeProperty = AvaloniaProperty.Register<Visual, CacheMode?>( nameof(CacheMode));`

#### `src/Avalonia.Base/VisualTree/VisualExtensions.cs`

- `VisualExtensions` -> `public static ILayoutManager? GetLayoutManager(this Visual visual) =>`
- `VisualExtensions` -> `public static IPlatformSettings? GetPlatformSettings(this Visual visual) =>`
- `VisualExtensions` -> `public static IPresentationSource? GetPresentationSource(this Visual visual) => visual.PresentationSource;`

#### `src/Avalonia.Base/VisualTreeAttachmentEventArgs.cs`

- `VisualTreeAttachmentEventArgs` -> `public IPresentationSource PresentationSource { get; }`
- `VisualTreeAttachmentEventArgs` -> `public Visual Root => RootVisual;`
- `VisualTreeAttachmentEventArgs` -> `public Visual RootVisual { get; set; }`
- `VisualTreeAttachmentEventArgs` -> `public Visual? AttachmentPoint { get; }`
- `VisualTreeAttachmentEventArgs` -> `public Visual? Parent => AttachmentPoint;`
- `VisualTreeAttachmentEventArgs` -> `public VisualTreeAttachmentEventArgs(Visual? attachmentPoint, IPresentationSource presentationSource) {`

### Rendering and Text

#### `src/HarfBuzz/Avalonia.HarfBuzz/HarfBuzzApplicationExtensions.cs`

- `HarfBuzzApplicationExtensions` -> `public static AppBuilder UseHarfBuzz(this AppBuilder builder) {`
- `public static class HarfBuzzApplicationExtensions {`

#### `src/HarfBuzz/Avalonia.HarfBuzz/HarfBuzzTextShaper.cs`

- `HarfBuzzTextShaper` -> `public ITextShaperTypeface CreateTypeface(GlyphTypeface glyphTypeface) {`
- `HarfBuzzTextShaper` -> `public ShapedBuffer ShapeText(ReadOnlyMemory<char> text, TextShaperOptions options) {`
- `public class HarfBuzzTextShaper : ITextShaperImpl {`

#### `src/Skia/Avalonia.Skia/Gpu/ISkiaGpuRenderTarget.cs`

- `ISkiaGpuRenderTarget` -> `ISkiaGpuRenderSession BeginRenderingSession(IRenderTarget.RenderTargetSceneInfo sceneInfo);`
- `ISkiaGpuRenderTarget` -> `bool IsReady => true;`

#### `src/Skia/Avalonia.Skia/Gpu/Metal/SkiaMetalGpu.cs`

- Namespace(s): `Avalonia.Skia.Metal`
- `SkiaMetalRenderTarget` -> `public ISkiaGpuRenderSession BeginRenderingSession(IRenderTarget.RenderTargetSceneInfo sceneInfo) {`
- `SkiaMetalRenderTarget` -> `public bool IsReady => _target?.IsReady ?? false;`

#### `src/Skia/Avalonia.Skia/SkiaSharpExtensions.cs`

- `SkiaSharpExtensions` -> `public static SKMatrix44 ToSKMatrix44(this Matrix m) {`
- `SkiaSharpExtensions` -> `public static SKSamplingOptions ToSKSamplingOptions(this BitmapInterpolationMode interpolationMode) => ToSKSamplingOptions(interpolationMode, true);`

#### `src/Skia/Avalonia.Skia/SurfaceRenderTarget.cs`

- `CreateInfo` -> `public bool UseScaledDrawing;`

### Source Generator Integration

#### `src/tools/Avalonia.Generators/NameGenerator/AvaloniaNameIncrementalGenerator.cs`

- Namespace(s): `Avalonia.Generators.NameGenerator`
- `public class AvaloniaNameIncrementalGenerator : IIncrementalGenerator {`
- `AvaloniaNameIncrementalGenerator` -> `public void Initialize(IncrementalGeneratorInitializationContext context) {`

### Windows Platform

#### `src/Windows/Avalonia.Win32/DirectX/IDirect3D11TexturePlatformSurface.cs`

- Namespace(s): `Avalonia.Win32.DirectX`
- `public interface IDirect3D11TexturePlatformSurface : IPlatformRenderSurface {`

#### `src/Windows/Avalonia.Win32/Interop/UnmanagedMethods.cs`

- `public enum DwmNCRenderingPolicy : uint {`

### XAML and Markup

#### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/CompiledBindingExtension.cs`

- `CompiledBindingExtension` -> `public CompiledBinding ProvideValue(IServiceProvider? provider) {`
- `public sealed class CompiledBindingExtension : CompiledBinding {`

#### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/DynamicResourceExtension.cs`

- `DynamicResourceExtension` -> `public BindingBase ProvideValue(IServiceProvider serviceProvider) {`
- `public sealed class DynamicResourceExtension : BindingBase {`

#### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/ReflectionBindingExtension.cs`

- `ReflectionBindingExtension` -> `public ReflectionBinding ProvideValue(IServiceProvider serviceProvider) {`
- `ReflectionBindingExtension` -> `public ReflectionBindingExtension() { }`
- `ReflectionBindingExtension` -> `public ReflectionBindingExtension(string path) : base(path) { }`
- `public sealed class ReflectionBindingExtension : ReflectionBinding {`

#### `src/Markup/Avalonia.Markup.Xaml/Templates/TreeDataTemplate.cs`

- `TreeDataTemplate` -> `public IDisposable BindChildren(AvaloniaObject target, AvaloniaProperty targetProperty, object item) {`

#### `src/Markup/Avalonia.Markup.Xaml/Templates/WindowDrawnDecorationsTemplate.cs`

- Namespace(s): `Avalonia.Markup.Xaml.Templates`
- `WindowDrawnDecorationsTemplate` -> `public TemplateResult<WindowDrawnDecorationsContent> Build() =>`
- `public class WindowDrawnDecorationsTemplate : IWindowDrawnDecorationsTemplate, ITemplate {`
- `WindowDrawnDecorationsTemplate` -> `public object? Content { get; set; }`

#### `src/Markup/Avalonia.Markup/Data/Binding.cs`

- Namespace(s): `Avalonia.Data`
- `Binding` -> `public Binding() { }`
- `Binding` -> `public Binding(string path) : base(path) { }`
- `public class Binding : ReflectionBinding {`

### iOS Platform

#### `src/iOS/Avalonia.iOS/AvaloniaAppDelegate.cs`

- `AvaloniaAppDelegate` -> `public UISceneConfiguration GetConfiguration(UIApplication application, UISceneSession connectingSceneSession, UISceneConnectionOptions options) {`
- `AvaloniaAppDelegate` -> `public bool FinishedLaunching(UIApplication application, NSDictionary? launchOptions) {`
- `public class AvaloniaAppDelegate<TApp> : UIResponder, IUIApplicationDelegate, IAvaloniaAppDelegate, IAvaloniaAppInternalDelegate where TApp : Application, new() {`

### macOS Native Platform

#### `src/Avalonia.Native/AvaloniaNativePlatformExtensions.cs`

- `AvaloniaNativePlatformOptions` -> `public string? AvaloniaNativeLibraryPath { get; set; }`

## Removed Public Signatures (Parser View)

- Public signatures: `812`

### By Area

- `Android Platform`: `3`
- `Application Model and Controls`: `201`
- `Browser Platform`: `6`
- `Headless Platform`: `14`
- `Linux Framebuffer`: `5`
- `Linux/X11 Platform`: `1`
- `Other`: `85`
- `Property, Data, Styling, Threading`: `412`
- `Rendering and Text`: `12`
- `Source Generator Integration`: `3`
- `Windows Platform`: `8`
- `XAML and Markup`: `59`
- `iOS Platform`: `2`
- `macOS Native Platform`: `1`

### By Kind

- `delegate`: `1`
- `event`: `6`
- `indexer`: `3`
- `member`: `265`
- `method`: `374`
- `type`: `163`

### Android Platform

#### `src/Android/Avalonia.Android/AvaloniaMainActivity.App.cs`

- `public class AvaloniaMainActivity<TApp> : AvaloniaMainActivity where TApp : Application, new() {`

#### `src/Android/Avalonia.Android/Platform/Specific/IAndroidView.cs`

- `IAndroidView` -> `View View { get; }`
- `public interface IAndroidView {`

### Application Model and Controls

#### `src/Avalonia.Controls/AppBuilder.cs`

- `AppBuilder` -> `public Func<Type, IApplicationLifetime?>? LifetimeOverride { get; private set; }`

#### `src/Avalonia.Controls/Application.cs`

- `public class Application : AvaloniaObject, IDataContextProvider, IGlobalDataTemplates, IGlobalStyles, IThemeVariantHost, IResourceHost2, IApplicationPlatformEvents, IOptionalFeatureProvider {`
- `Application` -> `public event EventHandler<UrlOpenedEventArgs>? UrlsOpened;`

#### `src/Avalonia.Controls/ApplicationLifetimes/ClassicDesktopStyleApplicationLifetime.cs`

- `ClassicDesktopStyleApplicationLifetimeOptions` -> `public bool ProcessUrlActivationCommandLine { get; set; }`
- `public class ClassicDesktopStyleApplicationLifetimeOptions {`

#### `src/Avalonia.Controls/ApplicationLifetimes/IActivatableApplicationLifetime.cs`

- Namespace(s): `Avalonia.Controls.ApplicationLifetimes`
- `public interface IActivatableApplicationLifetime : IActivatableLifetime {`

#### `src/Avalonia.Controls/AutoCompleteBox/AutoCompleteBox.Properties.cs`

- `AutoCompleteBox` -> `public IBinding? ValueMemberBinding {`
- `AutoCompleteBox` -> `public static readonly StyledProperty<string?> WatermarkProperty = TextBox.WatermarkProperty.AddOwner<AutoCompleteBox>();`

#### `src/Avalonia.Controls/AutoCompleteBox/AutoCompleteBox.cs`

- `AutoCompleteBox.BindingEvaluator` -> `public BindingEvaluator() { }`
- `AutoCompleteBox.BindingEvaluator` -> `public BindingEvaluator(IBinding? binding) : this() {`
- `AutoCompleteBox.BindingEvaluator` -> `public IBinding? ValueBinding {`
- `AutoCompleteBox.BindingEvaluator` -> `public T GetDynamicValue(object o, bool clearDataContext) {`
- `AutoCompleteBox.BindingEvaluator` -> `public T GetDynamicValue(object? o) {`
- `AutoCompleteBox.BindingEvaluator` -> `public T Value {`
- `AutoCompleteBox` -> `public class BindingEvaluator<T> : Control {`
- `AutoCompleteBox.BindingEvaluator` -> `public static readonly StyledProperty<T> ValueProperty = AvaloniaProperty.Register<BindingEvaluator<T>, T>(nameof(Value));`
- `AutoCompleteBox.BindingEvaluator` -> `public void ClearDataContext() {`

#### `src/Avalonia.Controls/Automation/Peers/AutomationPeer.cs`

- `AutomationPeer` -> `public string GetClassName() => GetClassNameCore() ?? string.Empty;`

#### `src/Avalonia.Controls/CalendarDatePicker/CalendarDatePicker.Properties.cs`

- `CalendarDatePicker` -> `public static readonly StyledProperty<bool> UseFloatingWatermarkProperty = TextBox.UseFloatingWatermarkProperty.AddOwner<CalendarDatePicker>();`
- `CalendarDatePicker` -> `public static readonly StyledProperty<string?> WatermarkProperty = TextBox.WatermarkProperty.AddOwner<CalendarDatePicker>();`

#### `src/Avalonia.Controls/Chrome/CaptionButtons.cs`

- `public class CaptionButtons : TemplatedControl {`
- `CaptionButtons` -> `public virtual void Attach(Window hostWindow) {`
- `CaptionButtons` -> `public virtual void Detach() {`

#### `src/Avalonia.Controls/Chrome/TitleBar.cs`

- `public class TitleBar : TemplatedControl {`

#### `src/Avalonia.Controls/ContextMenu.cs`

- `ContextMenu` -> `public PlacementMode PlacementMode {`
- `ContextMenu` -> `public static readonly StyledProperty<PlacementMode> PlacementModeProperty = PlacementProperty;`

#### `src/Avalonia.Controls/ContextRequestedEventArgs.cs`

- `ContextRequestedEventArgs` -> `public ContextRequestedEventArgs() : base(Control.ContextRequestedEvent) {`
- `ContextRequestedEventArgs` -> `public bool TryGetPosition(Control? relativeTo, out Point point) {`

#### `src/Avalonia.Controls/Control.cs`

- `Control` -> `public event EventHandler<ContextRequestedEventArgs>? ContextRequested {`
- `Control` -> `public static readonly RoutedEvent<ContextRequestedEventArgs> ContextRequestedEvent = RoutedEvent.Register<Control, ContextRequestedEventArgs>( nameof(ContextRequested), RoutingStrategies.Tunnel | RoutingStrategies.Bubble);`

#### `src/Avalonia.Controls/Design.cs`

- `Design` -> `public static object GetDataContext(Control control) {`
- `Design` -> `public static readonly AttachedProperty<object> DataContextProperty = AvaloniaProperty .RegisterAttached<Control, object>("DataContext", typeof (Design));`
- `Design` -> `public static void SetDataContext(Control control, object value) {`
- `Design` -> `public static void SetPreviewWith(AvaloniaObject target, Control? control) {`

#### `src/Avalonia.Controls/Diagnostics/IPopupHostProvider.cs`

- `IPopupHostProvider` -> `IPopupHost? PopupHost { get; }`
- `IPopupHostProvider` -> `event Action<IPopupHost?>? PopupHostChanged;`
- `public interface IPopupHostProvider {`

#### `src/Avalonia.Controls/Documents/Inline.cs`

- `Inline` -> `public static readonly StyledProperty<TextDecorationCollection?> TextDecorationsProperty = AvaloniaProperty.RegisterAttached<Inline, Inline, TextDecorationCollection?>( nameof(TextDecorations), inherits: true);`

#### `src/Avalonia.Controls/Embedding/Offscreen/OffscreenTopLevelImpl.cs`

- `OffscreenTopLevelImplBase` -> `public abstract IEnumerable<object> Surfaces { get; }`

#### `src/Avalonia.Controls/ExperimentalAcrylicBorder.cs`

- `ExperimentalAcrylicBorder` -> `public ExperimentalAcrylicMaterial Material {`
- `ExperimentalAcrylicBorder` -> `public static readonly StyledProperty<ExperimentalAcrylicMaterial> MaterialProperty = AvaloniaProperty.Register<ExperimentalAcrylicBorder, ExperimentalAcrylicMaterial>(nameof(Material));`

#### `src/Avalonia.Controls/Generators/ItemContainerGenerator.cs`

- `ItemContainerGenerator` -> `public Control? ContainerFromIndex(int index) => _owner.ContainerFromIndex(index);`
- `ItemContainerGenerator` -> `public int IndexFromContainer(Control container) => _owner.IndexFromContainer(container);`

#### `src/Avalonia.Controls/Generators/TreeItemContainerGenerator.cs`

- `TreeContainerIndex` -> `public Control? ContainerFromItem(object item) => _owner.TreeContainerFromItem(item);`
- `TreeContainerIndex` -> `public IEnumerable<Control> Containers => _owner.GetRealizedTreeContainers();`
- `TreeItemContainerGenerator` -> `public TreeContainerIndex Index { get; }`
- `public class TreeContainerIndex {`
- `public class TreeItemContainerGenerator : ItemContainerGenerator {`
- `TreeContainerIndex` -> `public object? ItemFromContainer(Control container) => _owner.TreeItemFromContainer(container);`

#### `src/Avalonia.Controls/HotkeyManager.cs`

- `HotKeyManager` -> `public static void SetHotKey(AvaloniaObject target, KeyGesture value) => target.SetValue(HotKeyProperty, value);`

#### `src/Avalonia.Controls/ItemsControl.cs`

- `ItemsControl` -> `public IBinding? DisplayMemberBinding {`
- `ItemsControl` -> `public ItemContainerGenerator ItemContainerGenerator {`
- `ItemsControl` -> `public static ItemsControl? ItemsControlFromItemContaner(Control container) =>`
- `ItemsControl` -> `public static readonly StyledProperty<IBinding?> DisplayMemberBindingProperty = AvaloniaProperty.Register<ItemsControl, IBinding?>(nameof(DisplayMemberBinding));`

#### `src/Avalonia.Controls/NativeMenuBar.cs`

- `NativeMenuBar` -> `public static readonly AttachedProperty<bool> EnableMenuItemClickForwardingProperty = AvaloniaProperty.RegisterAttached<NativeMenuBar, MenuItem, bool>( "EnableMenuItemClickForwarding");`
- `NativeMenuBar` -> `public static void SetEnableMenuItemClickForwarding(MenuItem menuItem, bool enable) {`

#### `src/Avalonia.Controls/NativeMenuItem.cs`

- `NativeMenuItem` -> `public NativeMenuItemToggleType ToggleType {`
- `public enum NativeMenuItemToggleType {`
- `NativeMenuItem` -> `public static readonly StyledProperty<NativeMenuItemToggleType> ToggleTypeProperty = AvaloniaProperty.Register<NativeMenuItem, NativeMenuItemToggleType>(nameof(ToggleType));`

#### `src/Avalonia.Controls/NumericUpDown/NumericUpDown.cs`

- `NumericUpDown` -> `public static readonly StyledProperty<string?> WatermarkProperty = AvaloniaProperty.Register<NumericUpDown, string?>(nameof(Watermark));`

#### `src/Avalonia.Controls/Platform/Dialogs/ISystemDialogImpl.cs`

- `ISystemDialogImpl` -> `Task<string?> ShowFolderDialogAsync(OpenFolderDialog dialog, Window parent);`
- `ISystemDialogImpl` -> `Task<string[]?> ShowFileDialogAsync(FileDialog dialog, Window parent);`
- `public interface ISystemDialogImpl {`

#### `src/Avalonia.Controls/Platform/ExtendClientAreaChromeHints.cs`

- `public enum ExtendClientAreaChromeHints {`

#### `src/Avalonia.Controls/Platform/IApplicationPlatformEvents.cs`

- `public interface IApplicationPlatformEvents {`
- `IApplicationPlatformEvents` -> `void RaiseUrlsOpened(string[] urls);`

#### `src/Avalonia.Controls/Platform/IInsetsManager.cs`

- `IInsetsManager` -> `bool DisplayEdgeToEdge { get; set; }`
- `InsetsManagerBase` -> `public virtual bool DisplayEdgeToEdge { get => DisplaysEdgeToEdge; set => DisplayEdgeToEdgePreference = value; }`

#### `src/Avalonia.Controls/Platform/IPlatformNativeSurfaceHandle.cs`

- `public interface INativePlatformHandleSurface : IPlatformHandle {`

#### `src/Avalonia.Controls/Platform/ITopLevelImpl.cs`

- `ITopLevelImpl` -> `IEnumerable<object> Surfaces { get; }`

#### `src/Avalonia.Controls/Platform/IWindowImpl.cs`

- `IWindowImpl` -> `void GetWindowsZOrder(Span<Window> windows, Span<long> zOrder);`
- `IWindowImpl` -> `void SetExtendClientAreaChromeHints(ExtendClientAreaChromeHints hints);`
- `IWindowImpl` -> `void SetSystemDecorations(SystemDecorations enabled);`

#### `src/Avalonia.Controls/Platform/Screen.cs`

- `Screen` -> `public Screen(double scaling, PixelRect bounds, PixelRect workingArea, bool isPrimary) {`
- `Screen` -> `public bool Primary => IsPrimary;`
- `public class Screen : IEquatable<Screen> {`
- `Screen` -> `public double PixelDensity => Scaling;`
- `Screen` -> `public override int GetHashCode() => RuntimeHelpers.GetHashCode(this);`
- `Screen` -> `public virtual bool Equals(Screen? other) => ReferenceEquals(this, other);`

#### `src/Avalonia.Controls/Platform/Surfaces/IFramebufferPlatformSurface.cs`

- `IFramebufferRenderTarget` -> `ILockedFramebuffer Lock();`
- `IFramebufferRenderTargetWithProperties` -> `ILockedFramebuffer Lock(out FramebufferLockProperties properties);`
- `IFramebufferRenderTargetWithProperties` -> `bool RetainsFrameContents { get; }`
- `FuncFramebufferRenderTarget` -> `public FuncFramebufferRenderTarget(Func<ILockedFramebuffer> lockFramebuffer) {`
- `FuncFramebufferRenderTarget` -> `public ILockedFramebuffer Lock() => _lockFramebuffer();`
- `public delegate ILockedFramebuffer LockDelegate(out FramebufferLockProperties properties);`
- `public interface IFramebufferPlatformSurface {`
- `public interface IFramebufferRenderTarget : IDisposable {`
- `public interface IFramebufferRenderTargetWithProperties : IFramebufferRenderTarget {`

#### `src/Avalonia.Controls/Presenters/TextPresenter.cs`

- `TextPresenter` -> `public static readonly StyledProperty<double> LetterSpacingProperty = TextBlock.LetterSpacingProperty.AddOwner<TextPresenter>();`

#### `src/Avalonia.Controls/Primitives/AccessText.cs`

- `AccessText` -> `public char AccessKey {`
- `AccessText` -> `public static readonly AttachedProperty<bool> ShowAccessKeyProperty = AvaloniaProperty.RegisterAttached<AccessText, Control, bool>("ShowAccessKey", inherits: true);`

#### `src/Avalonia.Controls/Primitives/AdornerLayer.cs`

- `AdornerLayer` -> `public AdornerLayer() {`

#### `src/Avalonia.Controls/Primitives/ChromeOverlayLayer.cs`

- `public class ChromeOverlayLayer : Panel {`
- `ChromeOverlayLayer` -> `public static Panel? GetOverlayLayer(Visual visual) {`
- `ChromeOverlayLayer` -> `public void Add(Control c) {`

#### `src/Avalonia.Controls/Primitives/ILogicalScrollable.cs`

- `ILogicalScrollable` -> `bool CanHorizontallyScroll { get; set; }`
- `ILogicalScrollable` -> `bool CanVerticallyScroll { get; set; }`

#### `src/Avalonia.Controls/Primitives/IPopupHost.cs`

- `IPopupHost` -> `ContentPresenter? Presenter { get; }`
- `IPopupHost` -> `Transform? Transform { get; set; }`
- `IPopupHost` -> `Visual? HostedVisualTreeRoot { get; }`
- `IPopupHost` -> `bool Topmost { get; set; }`
- `IPopupHost` -> `double Height { get; set; }`
- `IPopupHost` -> `double MaxHeight { get; set; }`
- `IPopupHost` -> `double MaxWidth { get; set; }`
- `IPopupHost` -> `double MinHeight { get; set; }`
- `IPopupHost` -> `double MinWidth { get; set; }`
- `IPopupHost` -> `double Width { get; set; }`
- `IPopupHost` -> `event EventHandler<TemplateAppliedEventArgs>? TemplateApplied;`
- `public interface IPopupHost : IDisposable, IFocusScope {`
- `IPopupHost` -> `void ConfigurePosition(PopupPositionRequest positionRequest);`
- `IPopupHost` -> `void Hide();`
- `IPopupHost` -> `void SetChild(Control? control);`
- `IPopupHost` -> `void Show();`
- `IPopupHost` -> `void TakeFocus();`

#### `src/Avalonia.Controls/Primitives/LightDismissOverlayLayer.cs`

- `LightDismissOverlayLayer` -> `public IInputElement? InputPassThroughElement { get; set; }`
- `LightDismissOverlayLayer` -> `public bool HitTest(Point point) {`
- `public class LightDismissOverlayLayer : Border, ICustomHitTest {`
- `LightDismissOverlayLayer` -> `public static LightDismissOverlayLayer? GetLightDismissOverlayLayer(Visual visual) {`

#### `src/Avalonia.Controls/Primitives/OverlayPopupHost.cs`

- `OverlayPopupHost` -> `public OverlayPopupHost(OverlayLayer overlayLayer) {`
- `public class OverlayPopupHost : ContentControl, IPopupHost, IManagedPopupPositionerPopup, IInputRoot {`
- `OverlayPopupHost` -> `public static IPopupHost CreatePopupHost(Visual target, IAvaloniaDependencyResolver? dependencyResolver) => CreatePopupHost(target, dependencyResolver, false);`
- `OverlayPopupHost` -> `public void ConfigurePosition(Visual target, PlacementMode placement, Point offset, PopupAnchor anchor = PopupAnchor.None, PopupGravity gravity = PopupGravity.None, PopupPositionerConstraintAdjustment constraintAdjustment = PopupPositionerConstraintAdjustment.All, Rect? rect = null) {`
- `OverlayPopupHost` -> `public void SetChild(Control? control) {`
- `OverlayPopupHost` -> `public void TakeFocus() {`

#### `src/Avalonia.Controls/Primitives/Popup.cs`

- `Popup` -> `public IPopupHost? Host => _openState?.PopupHost;`
- `Popup` -> `public PlacementMode PlacementMode {`
- `Popup` -> `public static readonly StyledProperty<PlacementMode> PlacementModeProperty = PlacementProperty;`

#### `src/Avalonia.Controls/Primitives/PopupRoot.cs`

- `PopupRoot` -> `public void ConfigurePosition(Visual target, PlacementMode placement, Point offset, PopupAnchor anchor = PopupAnchor.None, PopupGravity gravity = PopupGravity.None, PopupPositionerConstraintAdjustment constraintAdjustment = PopupPositionerConstraintAdjustment.All, Rect? rect = null) {`

#### `src/Avalonia.Controls/Primitives/SelectingItemsControl.cs`

- `SelectingItemsControl` -> `public IBinding? SelectedValueBinding {`
- `SelectingItemsControl` -> `public static readonly StyledProperty<IBinding?> SelectedValueBindingProperty = AvaloniaProperty.Register<SelectingItemsControl, IBinding?>(nameof(SelectedValueBinding));`

#### `src/Avalonia.Controls/Primitives/TextSearch.cs`

- `TextSearch` -> `public static IBinding? GetTextBinding(Interactive interactive) => interactive.GetValue(TextBindingProperty);`
- `TextSearch` -> `public static readonly AttachedProperty<IBinding?> TextBindingProperty = AvaloniaProperty.RegisterAttached<Interactive, IBinding?>("TextBinding", typeof(TextSearch));`
- `TextSearch` -> `public static string? GetText(Control control) => control.GetValue(TextProperty);`
- `TextSearch` -> `public static void SetText(Control control, string? text) => control.SetValue(TextProperty, text);`
- `TextSearch` -> `public static void SetTextBinding(Interactive interactive, IBinding? value) => interactive.SetValue(TextBindingProperty, value);`

#### `src/Avalonia.Controls/Primitives/ToggleButton.cs`

- `ToggleButton` -> `public event EventHandler<RoutedEventArgs>? Checked {`
- `ToggleButton` -> `public event EventHandler<RoutedEventArgs>? Indeterminate {`
- `ToggleButton` -> `public event EventHandler<RoutedEventArgs>? Unchecked {`
- `ToggleButton` -> `public static readonly RoutedEvent<RoutedEventArgs> CheckedEvent = RoutedEvent.Register<ToggleButton, RoutedEventArgs>( nameof(Checked), RoutingStrategies.Bubble);`
- `ToggleButton` -> `public static readonly RoutedEvent<RoutedEventArgs> IndeterminateEvent = RoutedEvent.Register<ToggleButton, RoutedEventArgs>( nameof(Indeterminate), RoutingStrategies.Bubble);`
- `ToggleButton` -> `public static readonly RoutedEvent<RoutedEventArgs> UncheckedEvent = RoutedEvent.Register<ToggleButton, RoutedEventArgs>( nameof(Unchecked), RoutingStrategies.Bubble);`

#### `src/Avalonia.Controls/Primitives/VisualLayerManager.cs`

- `VisualLayerManager` -> `public AdornerLayer AdornerLayer {`
- `VisualLayerManager` -> `public ChromeOverlayLayer ChromeOverlayLayer {`
- `VisualLayerManager` -> `public LightDismissOverlayLayer LightDismissOverlayLayer {`
- `VisualLayerManager` -> `public OverlayLayer? OverlayLayer {`
- `VisualLayerManager` -> `public TextSelectorLayer? TextSelectorLayer {`
- `public class VisualLayerManager : Decorator {`
- `VisualLayerManager` -> `public static readonly StyledProperty<ChromeOverlayLayer?> ChromeOverlayLayerProperty = AvaloniaProperty.Register<VisualLayerManager, ChromeOverlayLayer?>(nameof(ChromeOverlayLayer));`

#### `src/Avalonia.Controls/Remote/RemoteServer.cs`

- `RemoteServer` -> `public RemoteServer(IAvaloniaRemoteTransportConnection transport) {`
- `public class RemoteServer : IDisposable {`
- `RemoteServer` -> `public object? Content {`
- `RemoteServer` -> `public void Dispose() {`

#### `src/Avalonia.Controls/Remote/RemoteWidget.cs`

- `RemoteWidget` -> `public RemoteWidget(IAvaloniaRemoteTransportConnection connection) {`
- `RemoteWidget` -> `public SizingMode Mode { get; set; }`
- `public class RemoteWidget : Control {`
- `RemoteWidget` -> `public enum SizingMode {`
- `RemoteWidget` -> `public sealed override void Render(DrawingContext context) {`

#### `src/Avalonia.Controls/Screens.cs`

- `Screens` -> `public Screen? ScreenFromWindow(IWindowBaseImpl window) {`

#### `src/Avalonia.Controls/ScrollViewer.cs`

- `public class ScrollViewer : ContentControl, IScrollable, IScrollAnchorProvider, IInternalScroller {`

#### `src/Avalonia.Controls/SystemDialog.cs`

- `OpenFileDialog` -> `public FilePickerOpenOptions ToFilePickerOpenOptions() {`
- `SaveFileDialog` -> `public FilePickerSaveOptions ToFilePickerSaveOptions() {`
- `OpenFolderDialog` -> `public FolderPickerOpenOptions ToFolderPickerOpenOptions() {`
- `FileDialog` -> `public List<FileDialogFilter> Filters { get; set; } = new List<FileDialogFilter>();`
- `FileDialogFilter` -> `public List<string> Extensions { get; set; } = new List<string>();`
- `OpenFolderDialog` -> `public Task<string?> ShowAsync(Window parent) {`
- `OpenFileDialog` -> `public Task<string[]?> ShowAsync(Window parent) {`
- `public abstract class FileDialog : FileSystemDialog {`
- `public abstract class FileSystemDialog : SystemDialog {`
- `public abstract class SystemDialog {`
- `SaveFileDialog` -> `public async Task<string?> ShowAsync(Window parent) {`
- `OpenFileDialog` -> `public bool AllowMultiple { get; set; }`
- `SaveFileDialog` -> `public bool? ShowOverwritePrompt { get; set; }`
- `public class FileDialogFilter {`
- `public class OpenFileDialog : FileDialog {`
- `public class OpenFolderDialog : FileSystemDialog {`
- `public class SaveFileDialog : FileDialog {`
- `SaveFileDialog` -> `public string? DefaultExtension { get; set; }`
- `FileSystemDialog` -> `public string? Directory { get; set; }`
- `FileDialog` -> `public string? InitialFileName { get; set; }`
- `FileDialogFilter` -> `public string? Name { get; set; }`
- `SystemDialog` -> `public string? Title { get; set; }`

#### `src/Avalonia.Controls/Templates/FuncTreeDataTemplate.cs`

- `FuncTreeDataTemplate` -> `public InstancedBinding ItemsSelector(object item) {`

#### `src/Avalonia.Controls/Templates/ITreeDataTemplate.cs`

- `ITreeDataTemplate` -> `InstancedBinding? ItemsSelector(object item);`

#### `src/Avalonia.Controls/TextBlock.cs`

- `TextBlock` -> `public static readonly AttachedProperty<double> LetterSpacingProperty = AvaloniaProperty.RegisterAttached<TextBlock, Control, double>( nameof(LetterSpacing), 0, inherits: true);`

#### `src/Avalonia.Controls/TextBox.cs`

- `TextBox` -> `public double LetterSpacing {`
- `TextBox` -> `public static readonly StyledProperty<bool> UseFloatingWatermarkProperty = AvaloniaProperty.Register<TextBox, bool>(nameof(UseFloatingWatermark));`
- `TextBox` -> `public static readonly StyledProperty<double> LetterSpacingProperty = TextBlock.LetterSpacingProperty.AddOwner<TextBox>();`
- `TextBox` -> `public static readonly StyledProperty<string?> WatermarkProperty = AvaloniaProperty.Register<TextBox, string?>(nameof(Watermark));`

#### `src/Avalonia.Controls/TopLevel.cs`

- `TopLevel` -> `public IFocusManager? FocusManager => AvaloniaLocator.Current.GetService<IFocusManager>();`
- `TopLevel` -> `public IPlatformSettings? PlatformSettings => AvaloniaLocator.Current.GetService<IPlatformSettings>();`
- `TopLevel` -> `public TopLevel(ITopLevelImpl impl, IAvaloniaDependencyResolver? dependencyResolver) {`
- `public abstract class TopLevel : ContentControl, IInputRoot, ILayoutRoot, IRenderRoot, ICloseable, IStyleHost, ILogicalRoot, ITextInputMethodRoot {`
- `TopLevel` -> `public static readonly StyledProperty<IInputElement?> PointerOverElementProperty = AvaloniaProperty.Register<TopLevel, IInputElement?>(nameof(IInputRoot.PointerOverElement));`

#### `src/Avalonia.Controls/TreeView.cs`

- `TreeView` -> `public new TreeItemContainerGenerator ItemContainerGenerator =>`

#### `src/Avalonia.Controls/Window.cs`

- `Window` -> `public ExtendClientAreaChromeHints ExtendClientAreaChromeHints {`
- `Window` -> `public SystemDecorations SystemDecorations {`
- `public class Window : WindowBase, IFocusScope, ILayoutRoot {`
- `public enum SystemDecorations {`
- `Window` -> `public static readonly StyledProperty<ExtendClientAreaChromeHints> ExtendClientAreaChromeHintsProperty = AvaloniaProperty.Register<Window, ExtendClientAreaChromeHints>(nameof(ExtendClientAreaChromeHints), ExtendClientAreaChromeHints.Default);`
- `Window` -> `public static readonly StyledProperty<SystemDecorations> SystemDecorationsProperty = AvaloniaProperty.Register<Window, SystemDecorations>(nameof(SystemDecorations), SystemDecorations.Full);`
- `Window` -> `public static void SortWindowsByZOrder(Window[] windows) {`

### Browser Platform

#### `src/Browser/Avalonia.Browser.Blazor/AvaloniaView.cs`

- Namespace(s): `Avalonia.Browser.Blazor`
- `AvaloniaView` -> `public AvaloniaView() {`
- `public class AvaloniaView : ComponentBase {`

#### `src/Browser/Avalonia.Browser.Blazor/BlazorSingleViewLifetime.cs`

- Namespace(s): `Avalonia.Browser.Blazor`
- `BlazorAppBuilder` -> `public static async Task StartBlazorAppAsync(this AppBuilder builder, BrowserPlatformOptions? options = null) {`
- `public static class BlazorAppBuilder {`

#### `src/Browser/Avalonia.Browser/Rendering/RenderWorker.cs`

- Namespace(s): `Avalonia.Browser.Rendering`
- `JSWebWorkerClone` -> `public static Task RunAsync(Func<Task> run) {`
- `public static class JSWebWorkerClone {`

### Headless Platform

#### `src/Headless/Avalonia.Headless.Vnc/HeadlessVncPlatformExtensions.cs`

- `HeadlessVncPlatformExtensions` -> `public static int StartWithHeadlessVncPlatform( this AppBuilder builder, string host, int port, string? password, string[] args, ShutdownMode shutdownMode = ShutdownMode.OnLastWindowClose) {`
- `HeadlessVncPlatformExtensions` -> `public static int StartWithHeadlessVncPlatform( this AppBuilder builder, string host, int port, string[] args, ShutdownMode shutdownMode = ShutdownMode.OnLastWindowClose) {`

#### `src/Headless/Avalonia.Headless.XUnit/AvaloniaFact.cs`

- Namespace(s): `Avalonia.Headless.XUnit`
- `AvaloniaUIFactDiscoverer` -> `public AvaloniaUIFactDiscoverer(IMessageSink diagnosticMessageSink) : base(diagnosticMessageSink) {`
- `public class AvaloniaUIFactDiscoverer : FactDiscoverer {`
- `public sealed class AvaloniaFactAttribute : FactAttribute {`

#### `src/Headless/Avalonia.Headless.XUnit/AvaloniaTestFrameworkAttribute.cs`

- Namespace(s): `Avalonia.Headless.XUnit`
- `AvaloniaTestFrameworkTypeDiscoverer` -> `public AvaloniaTestFrameworkTypeDiscoverer(IMessageSink _) {`
- `AvaloniaTestFrameworkTypeDiscoverer` -> `public Type GetTestFrameworkType(IAttributeInfo attribute) {`
- `public class AvaloniaTestFrameworkTypeDiscoverer : ITestFrameworkTypeDiscoverer {`

#### `src/Headless/Avalonia.Headless.XUnit/AvaloniaTheoryAttribute.cs`

- Namespace(s): `Avalonia.Headless.XUnit`
- `AvaloniaTheoryDiscoverer` -> `public AvaloniaTheoryDiscoverer(IMessageSink diagnosticMessageSink) : base(diagnosticMessageSink) {`
- `public sealed class AvaloniaTheoryAttribute : TheoryAttribute {`

#### `src/Headless/Avalonia.Headless/HeadlessUnitTestSession.cs`

- Namespace(s): `Avalonia.Headless`
- `public sealed class HeadlessUnitTestSession : IDisposable {`

#### `src/Headless/Avalonia.Headless/HeadlessWindowExtensions.cs`

- Namespace(s): `Avalonia.Headless`
- `HeadlessWindowExtensions` -> `public static void DragDrop(this TopLevel topLevel, Point point, RawDragEventType type, IDataObject data, DragDropEffects effects, RawInputModifiers modifiers = RawInputModifiers.None) =>`
- `HeadlessWindowExtensions` -> `public static void KeyPress(this TopLevel topLevel, Key key, RawInputModifiers modifiers) =>`
- `HeadlessWindowExtensions` -> `public static void KeyRelease(this TopLevel topLevel, Key key, RawInputModifiers modifiers) =>`

### Linux Framebuffer

#### `src/Linux/Avalonia.LinuxFramebuffer/Output/DrmOutput.cs`

- `DrmOutput` -> `public PixelSize PixelSize => _mode.Resolution;`
- `public unsafe class DrmOutput : IGlOutputBackend, IGlPlatformSurface {`

#### `src/Linux/Avalonia.LinuxFramebuffer/Output/FbdevOutput.cs`

- `FbdevOutput` -> `public IFramebufferRenderTarget CreateFramebufferRenderTarget() => new FuncRetainedFramebufferRenderTarget(Lock);`
- `FbdevOutput` -> `public ILockedFramebuffer Lock() => Lock(out _);`

#### `src/Linux/Avalonia.LinuxFramebuffer/Output/IOutputBackend.cs`

- `public interface IOutputBackend {`

### Linux/X11 Platform

#### `src/Avalonia.X11/X11Platform.cs`

- `X11PlatformOptions` -> `public Action<Exception>? ExterinalGLibMainLoopExceptionLogger { get; set; }`

### Other

#### `src/Avalonia.Diagnostics/DevToolsExtensions.cs`

- `public static class DevToolsExtensions {`
- `DevToolsExtensions` -> `public static void AttachDevTools(this Application application) {`
- `DevToolsExtensions` -> `public static void AttachDevTools(this Application application, DevToolsOptions options) {`
- `DevToolsExtensions` -> `public static void AttachDevTools(this TopLevel root) {`
- `DevToolsExtensions` -> `public static void AttachDevTools(this TopLevel root, DevToolsOptions options) {`
- `DevToolsExtensions` -> `public static void AttachDevTools(this TopLevel root, KeyGesture gesture) {`

#### `src/Avalonia.Diagnostics/Diagnostics/DevToolsDataFormats.cs`

- Namespace(s): `Avalonia.Diagnostics`
- `DevToolsDataFormats` -> `public static DataFormat<string> Selector { get; } = DataFormat.CreateStringPlatformFormat("Avalonia_DevTools_Selector");`
- `public static class DevToolsDataFormats {`

#### `src/Avalonia.Diagnostics/Diagnostics/DevToolsOptions.cs`

- `DevToolsOptions` -> `public DevToolsViewKind LaunchView { get; init; }`
- `DevToolsOptions` -> `public HotKeyConfiguration HotKeys { get; init; } = new();`
- `DevToolsOptions` -> `public IBrush? FocusHighlighterBrush { get; set; }`
- `DevToolsOptions` -> `public IScreenshotHandler ScreenshotHandler { get; set; }`
- `DevToolsOptions` -> `public KeyGesture Gesture { get; set; } = new KeyGesture(Key.F12);`
- `DevToolsOptions` -> `public Size Size { get; set; } = new Size(1280, 720);`
- `DevToolsOptions` -> `public ThemeVariant? ThemeVariant { get; set; }`
- `DevToolsOptions` -> `public bool ShowAsChildWindow { get; set; } = true;`
- `DevToolsOptions` -> `public bool ShowImplementedInterfaces { get; set; } = true;`
- `public class DevToolsOptions {`
- `DevToolsOptions` -> `public int? StartupScreenIndex { get; set; }`

#### `src/Avalonia.Diagnostics/Diagnostics/DevToolsViewKind.cs`

- `public enum DevToolsViewKind {`

#### `src/Avalonia.Diagnostics/Diagnostics/HotKeyConfiguration.cs`

- `HotKeyConfiguration` -> `public KeyGesture InspectHoveredControl { get; init; } = new(Key.None, KeyModifiers.Shift | KeyModifiers.Control);`
- `HotKeyConfiguration` -> `public KeyGesture ScreenshotSelectedControl { get; init; } = new(Key.F8);`
- `HotKeyConfiguration` -> `public KeyGesture TogglePopupFreeze { get; init; } = new(Key.F, KeyModifiers.Alt | KeyModifiers.Control);`
- `HotKeyConfiguration` -> `public KeyGesture ValueFramesFreeze { get; init; } = new(Key.S, KeyModifiers.Alt);`
- `HotKeyConfiguration` -> `public KeyGesture ValueFramesUnfreeze { get; init; } = new(Key.D, KeyModifiers.Alt);`
- `public class HotKeyConfiguration {`

#### `src/Avalonia.Diagnostics/Diagnostics/IScreenshotHandler.cs`

- `IScreenshotHandler` -> `Task Take(Control control);`
- `public interface IScreenshotHandler {`

#### `src/Avalonia.Diagnostics/Diagnostics/Screenshots/BaseRenderToStreamHandler.cs`

- `public abstract class BaseRenderToStreamHandler : IScreenshotHandler {`
- `BaseRenderToStreamHandler` -> `public async Task Take(Control control) {`

#### `src/Avalonia.Diagnostics/Diagnostics/Screenshots/FilePickerHandler.cs`

- `FilePickerHandler` -> `public FilePickerHandler( string? title, string? screenshotRoot = default) {`
- `FilePickerHandler` -> `public FilePickerHandler() : this(null, null) {`
- `public sealed class FilePickerHandler : BaseRenderToStreamHandler {`

#### `src/Avalonia.Diagnostics/Diagnostics/VisualTreeDebug.cs`

- `public static class VisualTreeDebug {`
- `VisualTreeDebug` -> `public static string PrintVisualTree(Visual visual) {`

#### `src/Avalonia.Dialogs/ManagedFileDialogExtensions.cs`

- `ManagedFileDialogExtensions` -> `public static Task<string[]> ShowManagedAsync(this OpenFileDialog dialog, Window parent, ManagedFileDialogOptions? options = null) => ShowManagedAsync<Window>(dialog, parent, options);`
- `ManagedFileDialogExtensions` -> `public static async Task<string[]> ShowManagedAsync<TWindow>(this OpenFileDialog dialog, Window parent, ManagedFileDialogOptions? options = null) where TWindow : Window, new() {`

#### `src/Avalonia.Metal/IMetalDevice.cs`

- Namespace(s): `Avalonia.Metal`
- `public interface IMetalPlatformSurface {`
- `public interface IMetalPlatformSurfaceRenderTarget : IDisposable {`

#### `src/Avalonia.OpenGL/Egl/EglGlPlatformSurfaceBase.cs`

- `EglPlatformSurfaceRenderTargetBase` -> `public IGlPlatformSurfaceRenderingSession BeginDraw() {`
- `EglPlatformSurfaceRenderTargetBase` -> `public abstract IGlPlatformSurfaceRenderingSession BeginDrawCore();`
- `public abstract class EglPlatformSurfaceRenderTargetBase : IGlPlatformSurfaceRenderTargetWithCorruptionInfo {`

#### `src/Avalonia.OpenGL/IGlContext.cs`

- `IGlPlatformSurfaceRenderTargetFactory` -> `IGlPlatformSurfaceRenderTarget CreateRenderTarget(IGlContext context, object surface);`
- `IGlPlatformSurfaceRenderTargetFactory` -> `bool CanRenderToSurface(IGlContext context, object surface);`

#### `src/Avalonia.OpenGL/Surfaces/IGlPlatformSurface.cs`

- `public interface IGlPlatformSurface {`

#### `src/Avalonia.OpenGL/Surfaces/IGlPlatformSurfaceRenderTarget.cs`

- `IGlPlatformSurfaceRenderTarget` -> `IGlPlatformSurfaceRenderingSession BeginDraw();`
- `IGlPlatformSurfaceRenderTarget2` -> `IGlPlatformSurfaceRenderingSession BeginDraw(PixelSize expectedPixelSize);`
- `IGlPlatformSurfaceRenderTargetWithCorruptionInfo` -> `bool IsCorrupted { get; }`
- `public interface IGlPlatformSurfaceRenderTarget : IDisposable {`
- `public interface IGlPlatformSurfaceRenderTarget2 : IGlPlatformSurfaceRenderTargetWithCorruptionInfo {`
- `public interface IGlPlatformSurfaceRenderTargetWithCorruptionInfo : IGlPlatformSurfaceRenderTarget {`

#### `src/Avalonia.Vulkan/IVulkanDevice.cs`

- Namespace(s): `Avalonia.Vulkan`
- `IVulkanPlatformGraphicsContext` -> `IVulkanRenderTarget CreateRenderTarget(IEnumerable<object> surfaces);`

#### `src/Avalonia.Vulkan/IVulkanPlatformSurface.cs`

- Namespace(s): `Avalonia.Vulkan`
- `IVulkanKhrSurfacePlatformSurfaceFactory` -> `IVulkanKhrSurfacePlatformSurface CreateSurface(IVulkanPlatformGraphicsContext context, object surface);`
- `IVulkanKhrSurfacePlatformSurfaceFactory` -> `bool CanRenderToSurface(IVulkanPlatformGraphicsContext context, object surface);`
- `public interface IVulkanKhrSurfacePlatformSurface : IDisposable {`

#### `src/Avalonia.Vulkan/IVulkanRenderTarget.cs`

- Namespace(s): `Avalonia.Vulkan`
- `public interface IVulkanRenderTarget : IDisposable {`

#### `src/Tizen/Avalonia.Tizen/NuiAvaloniaView.cs`

- Namespace(s): `Avalonia.Tizen`
- `NuiAvaloniaView` -> `public Control? Content {`
- `NuiAvaloniaView` -> `public IInputRoot InputRoot {`
- `NuiAvaloniaView` -> `public INativeControlHostImpl NativeControlHost { get; }`
- `NuiAvaloniaView` -> `public NuiAvaloniaView() : base(ColorFormat.RGBA8888) {`
- `NuiAvaloniaView` -> `public Size ClientSize => new(Size.Width, Size.Height);`
- `public class NuiAvaloniaView : GLView, ITizenView, ITextInputMethodImpl {`
- `NuiAvaloniaView` -> `public double Scaling => 1;`
- `NuiAvaloniaView` -> `public event Action? OnSurfaceInit;`
- `NuiAvaloniaView` -> `public void SetClient(TextInputMethodClient? client) {`
- `NuiAvaloniaView` -> `public void SetCursorRect(Rect rect) {`
- `NuiAvaloniaView` -> `public void SetOptions(TextInputOptions options) =>`

#### `src/Tizen/Avalonia.Tizen/NuiAvaloniaViewTextEditable.cs`

- Namespace(s): `Avalonia.Tizen`
- `public class NuiMultiLineTextInput : TextEditor, INuiTextInput {`
- `public class NuiSingleLineTextInput : TextField, INuiTextInput {`

#### `src/Tizen/Avalonia.Tizen/NuiTizenApplication.cs`

- Namespace(s): `Avalonia.Tizen`
- `public class NuiTizenApplication<TApp> : NUIApplication where TApp : Application, new() {`

#### `src/Tizen/Avalonia.Tizen/NuiViewControlHandle.cs`

- Namespace(s): `Avalonia.Tizen`
- `NuiViewControlHandle` -> `public IntPtr Handle => throw new NotSupportedException();`
- `NuiViewControlHandle` -> `public NuiViewControlHandle(View view) {`
- `NuiViewControlHandle` -> `public View View { get; set; }`
- `public class NuiViewControlHandle : INativeControlHostDestroyableControlHandle {`
- `NuiViewControlHandle` -> `public string? HandleDescriptor => ViewDescriptor;`
- `NuiViewControlHandle` -> `public void Destroy() => View.Dispose();`

#### `src/Tizen/Avalonia.Tizen/Platform/Permissions.cs`

- Namespace(s): `Avalonia.Tizen.Platform`
- `public record Privilege (string Path, bool IsRuntime);`

#### `src/Tizen/Avalonia.Tizen/TizenApplicationExtensions.cs`

- Namespace(s): `Avalonia.Tizen`
- `TizenApplicationExtensions` -> `public static AppBuilder UseTizen(this AppBuilder builder) {`
- `public static class TizenApplicationExtensions {`

#### `src/tools/Avalonia.Analyzers/BitmapAnalyzer.cs`

- Namespace(s): `Avalonia.Analyzers`
- `BitmapAnalyzer` -> `public const string DiagnosticId = "AVA2002";`

#### `src/tools/Avalonia.Analyzers/BitmapAnalyzerCSCodeFixProvider.cs`

- Namespace(s): `Avalonia.Analyzers`
- `public class BitmapAnalyzerCSCodeFixProvider : CodeFixProvider {`
- `BitmapAnalyzerCSCodeFixProvider` -> `public override FixAllProvider? GetFixAllProvider() {`
- `BitmapAnalyzerCSCodeFixProvider` -> `public override ImmutableArray<string> FixableDiagnosticIds { get; } =`
- `BitmapAnalyzerCSCodeFixProvider` -> `public sealed override async Task RegisterCodeFixesAsync(CodeFixContext context) {`

#### `src/tools/Avalonia.Analyzers/OnPropertyChangedOverrideAnalyzer.cs`

- Namespace(s): `Avalonia.Analyzers`
- `OnPropertyChangedOverrideAnalyzer` -> `public const string DiagnosticId = "AVA2001";`

### Property, Data, Styling, Threading

#### `src/Avalonia.Base/Animation/Easings/CubicBezierEasing.cs`

- Namespace(s): `Avalonia.Animation.Easings`
- `CubicBezierEasing` -> `public Point ControlPoint1 { get; set; }`
- `CubicBezierEasing` -> `public Point ControlPoint2 { get; set; }`
- `public sealed class CubicBezierEasing : IEasing {`

#### `src/Avalonia.Base/Animation/ICustomAnimator.cs`

- Namespace(s): `Avalonia.Animation`
- `CustomAnimatorBase` -> `public abstract T Interpolate(double progress, T oldValue, T newValue);`
- `public abstract class CustomAnimatorBase {`
- `public abstract class CustomAnimatorBase<T> : CustomAnimatorBase {`

#### `src/Avalonia.Base/AvaloniaObject.cs`

- `AvaloniaObject` -> `public BindingExpressionBase Bind(AvaloniaProperty property, IBinding binding) {`
- `AvaloniaObject` -> `public IBinding this[IndexerDescriptor binding] {`
- `AvaloniaObject` -> `public bool CheckAccess() => Dispatcher.UIThread.CheckAccess();`
- `AvaloniaObject` -> `public void VerifyAccess() => Dispatcher.UIThread.VerifyAccess();`

#### `src/Avalonia.Base/AvaloniaObjectExtensions.cs`

- `AvaloniaObjectExtensions` -> `public static IBinding ToBinding<T>(this IObservable<T> source) {`
- `AvaloniaObjectExtensions` -> `public static IDisposable Bind( this AvaloniaObject target, AvaloniaProperty property, IBinding binding, object? anchor = null) {`

#### `src/Avalonia.Base/Controls/NameScope.cs`

- `NameScope` -> `public static INameScope GetNameScope(StyledElement styled) {`
- `NameScope` -> `public static readonly AttachedProperty<INameScope> NameScopeProperty = AvaloniaProperty.RegisterAttached<NameScope, StyledElement, INameScope>("NameScope");`
- `NameScope` -> `public static void SetNameScope(StyledElement styled, INameScope value) {`

#### `src/Avalonia.Base/Controls/PseudoClassesExtensions.cs`

- `public static class PseudolassesExtensions {`
- `PseudolassesExtensions` -> `public static void Set(this IPseudoClasses classes, string name, bool value) {`

#### `src/Avalonia.Base/Controls/ResourcesChangedEventArgs.cs`

- `public class ResourcesChangedEventArgs : EventArgs {`
- `ResourcesChangedEventArgs` -> `public static new readonly ResourcesChangedEventArgs Empty = new ResourcesChangedEventArgs();`

#### `src/Avalonia.Base/Data/BindingOperations.cs`

- `BindingOperations` -> `public static IDisposable Apply( AvaloniaObject target, AvaloniaProperty property, InstancedBinding binding) {`
- `BindingOperations` -> `public static IDisposable Apply( AvaloniaObject target, AvaloniaProperty property, InstancedBinding binding, object? anchor) {`

#### `src/Avalonia.Base/Data/Converters/FuncMultiValueConverter.cs`

- `FuncMultiValueConverter` -> `public FuncMultiValueConverter(Func<IEnumerable<TIn?>, TOut> convert) {`

#### `src/Avalonia.Base/Data/Core/Plugins/BindingPlugins.cs`

- `BindingPlugins` -> `public static IList<IDataValidationPlugin> DataValidators => s_dataValidators;`
- `BindingPlugins` -> `public static IList<IPropertyAccessorPlugin> PropertyAccessors => s_propertyAccessors;`
- `BindingPlugins` -> `public static IList<IStreamPlugin> StreamHandlers => s_streamHandlers;`
- `public static class BindingPlugins {`

#### `src/Avalonia.Base/Data/Core/Plugins/DataValidationBase.cs`

- `public abstract class DataValidationBase : PropertyAccessorBase, IObserver<object?> {`
- `DataValidationBase` -> `public override Type? PropertyType => _inner.PropertyType;`
- `DataValidationBase` -> `public override bool SetValue(object? value, BindingPriority priority) => _inner.SetValue(value, priority);`
- `DataValidationBase` -> `public override object? Value => _inner.Value;`

#### `src/Avalonia.Base/Data/Core/Plugins/ExceptionValidationPlugin.cs`

- `ExceptionValidationPlugin` -> `public IPropertyAccessor Start(WeakReference<object?> reference, string name, IPropertyAccessor inner) {`
- `ExceptionValidationPlugin` -> `public bool Match(WeakReference<object?> reference, string memberName) => true;`
- `public class ExceptionValidationPlugin : IDataValidationPlugin {`

#### `src/Avalonia.Base/Data/Core/Plugins/IDataValidationPlugin.cs`

- `IDataValidationPlugin` -> `IPropertyAccessor Start(WeakReference<object?> reference, string propertyName, IPropertyAccessor inner);`
- `IDataValidationPlugin` -> `bool Match(WeakReference<object?> reference, string memberName);`
- `public interface IDataValidationPlugin {`

#### `src/Avalonia.Base/Data/Core/Plugins/IPropertyAccessorPlugin.cs`

- `IPropertyAccessorPlugin` -> `IPropertyAccessor? Start(WeakReference<object?> reference, string propertyName);`
- `IPropertyAccessorPlugin` -> `bool Match(object obj, string propertyName);`
- `public interface IPropertyAccessorPlugin {`

#### `src/Avalonia.Base/Data/Core/Plugins/IStreamPlugin.cs`

- `IStreamPlugin` -> `IObservable<object?> Start(WeakReference<object?> reference);`
- `IStreamPlugin` -> `bool Match(WeakReference<object?> reference);`
- `public interface IStreamPlugin {`

#### `src/Avalonia.Base/Data/Core/Plugins/IndeiValidationPlugin.cs`

- `IndeiValidationPlugin` -> `public IPropertyAccessor Start(WeakReference<object?> reference, string name, IPropertyAccessor accessor) {`
- `IndeiValidationPlugin` -> `public bool Match(WeakReference<object?> reference, string memberName) {`
- `public class IndeiValidationPlugin : IDataValidationPlugin {`

#### `src/Avalonia.Base/Data/Core/Plugins/PropertyAccessorBase.cs`

- `PropertyAccessorBase` -> `public abstract Type? PropertyType { get; }`
- `PropertyAccessorBase` -> `public abstract bool SetValue(object? value, BindingPriority priority);`
- `public abstract class PropertyAccessorBase : IPropertyAccessor {`
- `PropertyAccessorBase` -> `public abstract object? Value { get; }`
- `PropertyAccessorBase` -> `public void Dispose() {`
- `PropertyAccessorBase` -> `public void Subscribe(Action<object?> listener) {`
- `PropertyAccessorBase` -> `public void Unsubscribe() {`

#### `src/Avalonia.Base/Data/Core/Plugins/PropertyError.cs`

- `PropertyError` -> `public PropertyError(BindingNotification error) {`
- `PropertyError` -> `public Type? PropertyType => null;`
- `PropertyError` -> `public bool SetValue(object? value, BindingPriority priority) {`
- `public class PropertyError : IPropertyAccessor {`
- `PropertyError` -> `public object? Value => _error;`
- `PropertyError` -> `public void Dispose() {`
- `PropertyError` -> `public void Subscribe(Action<object> listener) {`
- `PropertyError` -> `public void Unsubscribe() {`

#### `src/Avalonia.Base/Data/Core/PropertyPath.cs`

- `CastTypePropertyPathElement` -> `public CastTypePropertyPathElement(Type type) {`
- `EnsureTypePropertyPathElement` -> `public EnsureTypePropertyPathElement(Type type) {`
- `PropertyPropertyPathElement` -> `public IPropertyInfo Property { get; }`
- `PropertyPath` -> `public IReadOnlyList<IPropertyPathElement> Elements { get; }`
- `PropertyPathBuilder` -> `public PropertyPath Build() {`
- `PropertyPath` -> `public PropertyPath(IEnumerable<IPropertyPathElement> elements) {`
- `PropertyPathBuilder` -> `public PropertyPathBuilder Cast(Type type) {`
- `PropertyPathBuilder` -> `public PropertyPathBuilder ChildTraversal() {`
- `PropertyPathBuilder` -> `public PropertyPathBuilder EnsureType(Type type) {`
- `PropertyPathBuilder` -> `public PropertyPathBuilder Property(IPropertyInfo property) {`
- `PropertyPropertyPathElement` -> `public PropertyPropertyPathElement(IPropertyInfo property) {`
- `EnsureTypePropertyPathElement` -> `public Type Type { get; }`
- `CastTypePropertyPathElement` -> `public Type Type { get; }`
- `public class CastTypePropertyPathElement : IPropertyPathElement {`
- `public class ChildTraversalPropertyPathElement : IPropertyPathElement {`
- `public class EnsureTypePropertyPathElement : IPropertyPathElement {`
- `public class PropertyPath {`
- `public class PropertyPathBuilder {`
- `public class PropertyPropertyPathElement : IPropertyPathElement {`
- `public interface IPropertyPathElement {`

#### `src/Avalonia.Base/Data/IBinding.cs`

- `IBinding` -> `InstancedBinding? Initiate( AvaloniaObject target, AvaloniaProperty? targetProperty, object? anchor = null, bool enableDataValidation = false);`
- `public interface IBinding {`

#### `src/Avalonia.Base/Data/InstancedBinding.cs`

- `InstancedBinding` -> `public BindingMode Mode { get; }`
- `InstancedBinding` -> `public BindingPriority Priority { get; }`
- `InstancedBinding` -> `public IObservable<object?> Observable => Source;`
- `InstancedBinding` -> `public IObservable<object?> Source => _observable ??= _expression!.ToObservable(_target);`
- `InstancedBinding` -> `public InstancedBinding WithPriority(BindingPriority priority) {`
- `public sealed class InstancedBinding {`
- `InstancedBinding` -> `public static InstancedBinding OneTime( IObservable<object?> observable, BindingPriority priority = BindingPriority.LocalValue) {`
- `InstancedBinding` -> `public static InstancedBinding OneTime( object value, BindingPriority priority = BindingPriority.LocalValue) {`
- `InstancedBinding` -> `public static InstancedBinding OneWay( IObservable<object?> observable, BindingPriority priority = BindingPriority.LocalValue) {`
- `InstancedBinding` -> `public static InstancedBinding OneWayToSource( IObserver<object?> observer, BindingPriority priority = BindingPriority.LocalValue) {`
- `InstancedBinding` -> `public static InstancedBinding TwoWay( IObservable<object?> observable, IObserver<object?> observer, BindingPriority priority = BindingPriority.LocalValue) {`

#### `src/Avalonia.Base/Data/TemplateBinding.Observable.cs`

- `TemplateBinding` -> `public IDisposable Subscribe(IObserver<object?> observer) {`
- `public partial class TemplateBinding : IAvaloniaSubject<object?> {`

#### `src/Avalonia.Base/Data/TemplateBinding.cs`

- `TemplateBinding` -> `public IBinding ProvideValue() => this;`
- `TemplateBinding` -> `public InstancedBinding? Initiate( AvaloniaObject target, AvaloniaProperty? targetProperty, object? anchor = null, bool enableDataValidation = false) {`
- `TemplateBinding` -> `public TemplateBinding() : base(BindingPriority.Template) {`
- `TemplateBinding` -> `public TemplateBinding([InheritDataTypeFrom(InheritDataTypeFromScopeKind.ControlTemplate)] AvaloniaProperty property) : base(BindingPriority.Template) {`
- `TemplateBinding` -> `public new BindingMode Mode {`
- `TemplateBinding` -> `public override string Description => "TemplateBinding: " + Property;`
- `public partial class TemplateBinding : UntypedBindingExpressionBase, IBinding, IBinding2, IDescription, ISetterValue, IDisposable {`

#### `src/Avalonia.Base/Diagnostics/StyleDiagnostics.cs`

- Namespace(s): `Avalonia.Diagnostics`
- `StyleDiagnostics` -> `public IReadOnlyList<AppliedStyle> AppliedStyles { get; }`
- `AppliedStyle` -> `public StyleBase Style => (StyleBase)_instance.Source;`
- `StyleDiagnostics` -> `public StyleDiagnostics(IReadOnlyList<AppliedStyle> appliedStyles) {`
- `AppliedStyle` -> `public bool HasActivator => _instance.HasActivator;`
- `AppliedStyle` -> `public bool IsActive => _instance.IsActive();`
- `public class StyleDiagnostics {`
- `public sealed class AppliedStyle {`

#### `src/Avalonia.Base/Diagnostics/StyledElementExtensions.cs`

- Namespace(s): `Avalonia.Diagnostics`
- `StyledElementExtensions` -> `public static StyleDiagnostics GetStyleDiagnostics(this StyledElement styledElement) {`
- `public static class StyledElementExtensions {`

#### `src/Avalonia.Base/Input/Cursor.cs`

- `Cursor` -> `public Cursor(Bitmap cursor, PixelPoint hotSpot) : this(GetCursorFactory().CreateCursor(cursor.PlatformImpl.Item, hotSpot), "BitmapCursor") {`

#### `src/Avalonia.Base/Input/DataFormats.cs`

- `public static class DataFormats {`
- `DataFormats` -> `public static readonly string FileNames = nameof(FileNames);`
- `DataFormats` -> `public static readonly string Files = nameof(Files);`
- `DataFormats` -> `public static readonly string Text = nameof(Text);`

#### `src/Avalonia.Base/Input/DataObject.cs`

- `DataObject` -> `public IEnumerable<string> GetDataFormats() {`
- `DataObject` -> `public bool Contains(string dataFormat) {`
- `public class DataObject : IDataObject {`
- `DataObject` -> `public object? Get(string dataFormat) {`
- `DataObject` -> `public void Set(string dataFormat, object value) {`

#### `src/Avalonia.Base/Input/DataObjectExtensions.cs`

- `DataObjectExtensions` -> `public static IEnumerable<IStorageItem>? GetFiles(this IDataObject dataObject) {`
- `DataObjectExtensions` -> `public static IEnumerable<string>? GetFileNames(this IDataObject dataObject) {`
- `public static class DataObjectExtensions {`
- `DataObjectExtensions` -> `public static string? GetText(this IDataObject dataObject) {`

#### `src/Avalonia.Base/Input/DragDrop.cs`

- `DragDrop` -> `public static Task<DragDropEffects> DoDragDrop(PointerEventArgs triggerEvent, IDataObject data, DragDropEffects allowedEffects) {`

#### `src/Avalonia.Base/Input/DragEventArgs.cs`

- `DragEventArgs` -> `public DragEventArgs( RoutedEvent<DragEventArgs> routedEvent, IDataObject data, Interactive target, Point targetLocation, KeyModifiers keyModifiers) : this(routedEvent, new DataObjectToDataTransferWrapper(data), target, targetLocation, keyModifiers) {`
- `DragEventArgs` -> `public IDataObject Data => _legacyDataObject ??= DataTransfer.ToLegacyDataObject();`
- `public class DragEventArgs : RoutedEventArgs {`

#### `src/Avalonia.Base/Input/GestureRecognizers/ScrollGestureRecognizer.cs`

- `ScrollGestureRecognizer` -> `public static readonly DirectProperty<ScrollGestureRecognizer, bool> IsScrollInertiaEnabledProperty = AvaloniaProperty.RegisterDirect<ScrollGestureRecognizer, bool>(nameof(IsScrollInertiaEnabled), o => o.IsScrollInertiaEnabled, (o,v) => o.IsScrollInertiaEnabled = v);`

#### `src/Avalonia.Base/Input/Gestures.cs`

- `Gestures` -> `public static bool GetIsHoldWithMouseEnabled(StyledElement element) {`
- `Gestures` -> `public static bool GetIsHoldingEnabled(StyledElement element) {`
- `public static class Gestures {`
- `Gestures` -> `public static readonly AttachedProperty<bool> IsHoldWithMouseEnabledProperty = AvaloniaProperty.RegisterAttached<StyledElement, bool>("IsHoldWithMouseEnabled", typeof(Gestures), false);`
- `Gestures` -> `public static readonly AttachedProperty<bool> IsHoldingEnabledProperty = AvaloniaProperty.RegisterAttached<StyledElement, bool>("IsHoldingEnabled", typeof(Gestures), true);`
- `Gestures` -> `public static readonly RoutedEvent<HoldingRoutedEventArgs> HoldingEvent = RoutedEvent.Register<HoldingRoutedEventArgs>( "Holding", RoutingStrategies.Bubble, typeof(Gestures));`
- `Gestures` -> `public static readonly RoutedEvent<PinchEndedEventArgs> PinchEndedEvent = RoutedEvent.Register<PinchEndedEventArgs>( "PinchEnded", RoutingStrategies.Bubble, typeof(Gestures));`
- `Gestures` -> `public static readonly RoutedEvent<PinchEventArgs> PinchEvent = RoutedEvent.Register<PinchEventArgs>( "Pinch", RoutingStrategies.Bubble, typeof(Gestures));`
- `Gestures` -> `public static readonly RoutedEvent<PointerDeltaEventArgs> PointerTouchPadGestureMagnifyEvent = RoutedEvent.Register<PointerDeltaEventArgs>( "PointerTouchPadGestureMagnify", RoutingStrategies.Bubble, typeof(Gestures));`
- `Gestures` -> `public static readonly RoutedEvent<PointerDeltaEventArgs> PointerTouchPadGestureRotateEvent = RoutedEvent.Register<PointerDeltaEventArgs>( "PointerTouchPadGestureRotate", RoutingStrategies.Bubble, typeof(Gestures));`
- `Gestures` -> `public static readonly RoutedEvent<PointerDeltaEventArgs> PointerTouchPadGestureSwipeEvent = RoutedEvent.Register<PointerDeltaEventArgs>( "PointerTouchPadGestureSwipe", RoutingStrategies.Bubble, typeof(Gestures));`
- `Gestures` -> `public static readonly RoutedEvent<PullGestureEndedEventArgs> PullGestureEndedEvent = RoutedEvent.Register<PullGestureEndedEventArgs>( "PullGestureEnded", RoutingStrategies.Bubble, typeof(Gestures));`
- `Gestures` -> `public static readonly RoutedEvent<PullGestureEventArgs> PullGestureEvent = RoutedEvent.Register<PullGestureEventArgs>( "PullGesture", RoutingStrategies.Bubble, typeof(Gestures));`
- `Gestures` -> `public static readonly RoutedEvent<ScrollGestureEndedEventArgs> ScrollGestureEndedEvent = RoutedEvent.Register<ScrollGestureEndedEventArgs>( "ScrollGestureEnded", RoutingStrategies.Bubble, typeof(Gestures));`
- `Gestures` -> `public static readonly RoutedEvent<ScrollGestureEventArgs> ScrollGestureEvent = RoutedEvent.Register<ScrollGestureEventArgs>( "ScrollGesture", RoutingStrategies.Bubble, typeof(Gestures));`
- `Gestures` -> `public static readonly RoutedEvent<ScrollGestureInertiaStartingEventArgs> ScrollGestureInertiaStartingEvent = RoutedEvent.Register<ScrollGestureInertiaStartingEventArgs>( "ScrollGestureInertiaStarting", RoutingStrategies.Bubble, typeof(Gestures));`
- `Gestures` -> `public static readonly RoutedEvent<TappedEventArgs> DoubleTappedEvent = RoutedEvent.Register<TappedEventArgs>( "DoubleTapped", RoutingStrategies.Bubble, typeof(Gestures));`
- `Gestures` -> `public static readonly RoutedEvent<TappedEventArgs> RightTappedEvent = RoutedEvent.Register<TappedEventArgs>( "RightTapped", RoutingStrategies.Bubble, typeof(Gestures));`
- `Gestures` -> `public static readonly RoutedEvent<TappedEventArgs> TappedEvent = RoutedEvent.Register<TappedEventArgs>( "Tapped", RoutingStrategies.Bubble, typeof(Gestures));`
- `Gestures` -> `public static void AddDoubleTappedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`
- `Gestures` -> `public static void AddHoldingHandler(Interactive element, EventHandler<HoldingRoutedEventArgs> handler) =>`
- `Gestures` -> `public static void AddPinchEndedHandler(Interactive element, EventHandler<PinchEndedEventArgs> handler) =>`
- `Gestures` -> `public static void AddPinchHandler(Interactive element, EventHandler<PinchEventArgs> handler) =>`
- `Gestures` -> `public static void AddPointerTouchPadGestureMagnifyHandler(Interactive element, EventHandler<PointerDeltaEventArgs> handler) =>`
- `Gestures` -> `public static void AddPointerTouchPadGestureRotateHandler(Interactive element, EventHandler<PointerDeltaEventArgs> handler) =>`
- `Gestures` -> `public static void AddPointerTouchPadGestureSwipeHandler(Interactive element, EventHandler<PointerDeltaEventArgs> handler) =>`
- `Gestures` -> `public static void AddPullGestureEndedHandler(Interactive element, EventHandler<PullGestureEndedEventArgs> handler) =>`
- `Gestures` -> `public static void AddPullGestureHandler(Interactive element, EventHandler<PullGestureEventArgs> handler) =>`
- `Gestures` -> `public static void AddRightTappedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`
- `Gestures` -> `public static void AddScrollGestureEndedHandler(Interactive element, EventHandler<ScrollGestureEndedEventArgs> handler) =>`
- `Gestures` -> `public static void AddScrollGestureHandler(Interactive element, EventHandler<RoutedEventArgs> handler) =>`
- `Gestures` -> `public static void AddScrollGestureInertiaStartingHandler(Interactive element, EventHandler<ScrollGestureInertiaStartingEventArgs> handler) =>`
- `Gestures` -> `public static void AddTappedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`
- `Gestures` -> `public static void RemoveDoubleTappedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`
- `Gestures` -> `public static void RemoveHoldingHandler(Interactive element, EventHandler<RoutedEventArgs> handler) =>`
- `Gestures` -> `public static void RemovePinchEndedHandler(Interactive element, EventHandler<PinchEndedEventArgs> handler) =>`
- `Gestures` -> `public static void RemovePinchHandler(Interactive element, EventHandler<PinchEventArgs> handler) =>`
- `Gestures` -> `public static void RemovePointerTouchPadGestureMagnifyHandler(Interactive element, EventHandler<PointerDeltaEventArgs> handler) =>`
- `Gestures` -> `public static void RemovePointerTouchPadGestureRotateHandler(Interactive element, EventHandler<PointerDeltaEventArgs> handler) =>`
- `Gestures` -> `public static void RemovePointerTouchPadGestureSwipeHandler(Interactive element, EventHandler<PointerDeltaEventArgs> handler) =>`
- `Gestures` -> `public static void RemovePullGestureEndedHandler(Interactive element, EventHandler<PullGestureEndedEventArgs> handler) =>`
- `Gestures` -> `public static void RemovePullGestureHandler(Interactive element, EventHandler<PullGestureEventArgs> handler) =>`
- `Gestures` -> `public static void RemoveRightTappedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`
- `Gestures` -> `public static void RemoveScrollGestureEndedHandler(Interactive element,EventHandler<ScrollGestureEndedEventArgs> handler) =>`
- `Gestures` -> `public static void RemoveScrollGestureHandler(Interactive element, EventHandler<ScrollGestureEventArgs> handler) =>`
- `Gestures` -> `public static void RemoveScrollGestureInertiaStartingHandler(Interactive element, EventHandler<ScrollGestureInertiaStartingEventArgs> handler) =>`
- `Gestures` -> `public static void RemoveTappedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`
- `Gestures` -> `public static void SetIsHoldWithMouseEnabled(StyledElement element, bool value) {`
- `Gestures` -> `public static void SetIsHoldingEnabled(StyledElement element, bool value) {`

#### `src/Avalonia.Base/Input/GotFocusEventArgs.cs`

- `public class GotFocusEventArgs : RoutedEventArgs {`

#### `src/Avalonia.Base/Input/HoldingRoutedEventArgs.cs`

- `HoldingRoutedEventArgs` -> `public HoldingRoutedEventArgs(HoldingState holdingState, Point position, PointerType pointerType) : base(Gestures.HoldingEvent) {`

#### `src/Avalonia.Base/Input/IDataObject.cs`

- `IDataObject` -> `IEnumerable<string> GetDataFormats();`
- `IDataObject` -> `bool Contains(string dataFormat);`
- `IDataObject` -> `object? Get(string dataFormat);`
- `public interface IDataObject {`

#### `src/Avalonia.Base/Input/IInputRoot.cs`

- `IInputRoot` -> `IFocusManager? FocusManager { get; }`
- `IInputRoot` -> `IInputElement? PointerOverElement { get; set; }`
- `IInputRoot` -> `IKeyboardNavigationHandler? KeyboardNavigationHandler { get; }`
- `IInputRoot` -> `IPlatformSettings? PlatformSettings { get; }`
- `IInputRoot` -> `bool ShowAccessKeys { get; set; }`
- `public interface IInputRoot : IInputElement {`

#### `src/Avalonia.Base/Input/IKeyboardNavigationHandler.cs`

- `public interface IKeyboardNavigationHandler {`
- `IKeyboardNavigationHandler` -> `void Move( IInputElement element, NavigationDirection direction, KeyModifiers keyModifiers = KeyModifiers.None);`
- `IKeyboardNavigationHandler` -> `void SetOwner(IInputRoot owner);`

#### `src/Avalonia.Base/Input/InputElement.cs`

- `public class InputElement : Interactive, IInputElement {`
- `InputElement` -> `public static readonly RoutedEvent<HoldingRoutedEventArgs> HoldingEvent = Gestures.HoldingEvent;`
- `InputElement` -> `public static readonly RoutedEvent<TappedEventArgs> DoubleTappedEvent = Gestures.DoubleTappedEvent;`
- `InputElement` -> `public static readonly RoutedEvent<TappedEventArgs> TappedEvent = Gestures.TappedEvent;`

#### `src/Avalonia.Base/Input/KeyEventArgs.cs`

- Namespace(s): `Avalonia.Input`
- `public class KeyEventArgs : RoutedEventArgs {`

#### `src/Avalonia.Base/Input/KeyboardNavigationHandler.cs`

- `public sealed class KeyboardNavigationHandler : IKeyboardNavigationHandler {`
- `KeyboardNavigationHandler` -> `public static IInputElement? GetNext( IInputElement element, NavigationDirection direction) {`
- `KeyboardNavigationHandler` -> `public void Move( IInputElement? element, NavigationDirection direction, KeyModifiers keyModifiers = KeyModifiers.None) {`
- `KeyboardNavigationHandler` -> `public void SetOwner(IInputRoot owner) {`

#### `src/Avalonia.Base/Input/PinchEventArgs.cs`

- `PinchEndedEventArgs` -> `public PinchEndedEventArgs() : base(Gestures.PinchEndedEvent) {`
- `PinchEventArgs` -> `public PinchEventArgs(double scale, Point scaleOrigin) : base(Gestures.PinchEvent) {`
- `PinchEventArgs` -> `public PinchEventArgs(double scale, Point scaleOrigin, double angle, double angleDelta) : base(Gestures.PinchEvent) {`

#### `src/Avalonia.Base/Input/Platform/IClipboard.cs`

- `IClipboard` -> `Task SetDataObjectAsync(IDataObject data);`
- `IClipboard` -> `Task SetTextAsync(string? text);`
- `IClipboard` -> `Task<IDataObject?> TryGetInProcessDataObjectAsync();`
- `IClipboard` -> `Task<object?> GetDataAsync(string format);`
- `IClipboard` -> `Task<string?> GetTextAsync();`
- `IClipboard` -> `Task<string[]> GetFormatsAsync();`

#### `src/Avalonia.Base/Input/Platform/IPlatformDragSource.cs`

- `IPlatformDragSource` -> `Task<DragDropEffects> DoDragDrop( PointerEventArgs triggerEvent, IDataObject data, DragDropEffects allowedEffects);`

#### `src/Avalonia.Base/Input/PointerEventArgs.cs`

- `public class PointerEventArgs : RoutedEventArgs {`

#### `src/Avalonia.Base/Input/PullGestureEventArgs.cs`

- `PullGestureEndedEventArgs` -> `public PullGestureEndedEventArgs(int id, PullDirection pullDirection) : base(Gestures.PullGestureEndedEvent) {`
- `PullGestureEventArgs` -> `public PullGestureEventArgs(int id, Vector delta, PullDirection pullDirection) : base(Gestures.PullGestureEvent) {`

#### `src/Avalonia.Base/Input/Raw/RawDragEvent.cs`

- `RawDragEvent` -> `public IDataObject Data => _legacyDataObject ??= DataTransfer.ToLegacyDataObject();`
- `RawDragEvent` -> `public RawDragEvent(IDragDropDevice inputDevice, RawDragEventType type, IInputRoot root, Point location, IDataObject data, DragDropEffects effects, RawInputModifiers modifiers) : this(inputDevice, type, root, location, new DataObjectToDataTransferWrapper(data), effects, modifiers) {`

#### `src/Avalonia.Base/Input/Raw/RawKeyEventArgs.cs`

- `RawKeyEventArgs` -> `public RawKeyEventArgs( IInputDevice device, ulong timestamp, IInputRoot root, RawKeyEventType type, Key key, RawInputModifiers modifiers, PhysicalKey physicalKey, KeyDeviceType keyDeviceType, string? keySymbol) : base(device, timestamp, root) {`
- `RawKeyEventArgs` -> `public RawKeyEventArgs( IInputDevice device, ulong timestamp, IInputRoot root, RawKeyEventType type, Key key, RawInputModifiers modifiers, PhysicalKey physicalKey, string? keySymbol) : this(device, timestamp, root, type, key, modifiers, physicalKey, KeyDeviceType.Keyboard, keySymbol) { }`
- `RawKeyEventArgs` -> `public RawKeyEventArgs( IKeyboardDevice device, ulong timestamp, IInputRoot root, RawKeyEventType type, Key key, RawInputModifiers modifiers) : this(device, timestamp, root, type, key, modifiers, PhysicalKey.None, KeyDeviceType.Keyboard, null) {`

#### `src/Avalonia.Base/Input/ScrollGestureEventArgs.cs`

- `ScrollGestureEndedEventArgs` -> `public ScrollGestureEndedEventArgs(int id) : base(Gestures.ScrollGestureEndedEvent) {`
- `ScrollGestureEventArgs` -> `public ScrollGestureEventArgs(int id, Vector delta) : base(Gestures.ScrollGestureEvent) {`

#### `src/Avalonia.Base/Input/TappedEventArgs.cs`

- `public class TappedEventArgs : RoutedEventArgs {`

#### `src/Avalonia.Base/Input/TextInput/ITextInputMethodImpl.cs`

- `ITextInputMethodRoot` -> `ITextInputMethodImpl? InputMethod { get; }`
- `public interface ITextInputMethodRoot : IInputRoot {`

#### `src/Avalonia.Base/Input/TextInput/TextInputMethodClient.cs`

- `TextInputMethodClient` -> `public virtual void ShowInputPanel() {`

#### `src/Avalonia.Base/Layout/IEmbeddedLayoutRoot.cs`

- `IEmbeddedLayoutRoot` -> `Size AllocatedSize { get; }`
- `public interface IEmbeddedLayoutRoot : ILayoutRoot {`

#### `src/Avalonia.Base/Layout/ILayoutRoot.cs`

- `ILayoutRoot` -> `Size ClientSize { get; }`
- `ILayoutRoot` -> `double LayoutScaling { get; }`
- `public interface ILayoutRoot {`

#### `src/Avalonia.Base/Layout/LayoutHelper.cs`

- `LayoutHelper` -> `public static Size RoundLayoutSizeUp(Size size, double dpiScaleX, double dpiScaleY) {`
- `LayoutHelper` -> `public static Thickness RoundLayoutThickness(Thickness thickness, double dpiScaleX, double dpiScaleY) {`
- `LayoutHelper` -> `public static double GetLayoutScale(Layoutable control) => control.VisualRoot is ILayoutRoot layoutRoot ? layoutRoot.LayoutScaling : 1.0;`

#### `src/Avalonia.Base/Layout/LayoutManager.cs`

- `LayoutManager` -> `public LayoutManager(ILayoutRoot owner) {`
- `public class LayoutManager : ILayoutManager, IDisposable {`
- `LayoutManager` -> `public virtual event EventHandler? LayoutUpdated;`
- `LayoutManager` -> `public virtual void ExecuteInitialLayoutPass() {`
- `LayoutManager` -> `public virtual void ExecuteLayoutPass() {`
- `LayoutManager` -> `public virtual void InvalidateArrange(Layoutable control) {`
- `LayoutManager` -> `public virtual void InvalidateMeasure(Layoutable control) {`
- `LayoutManager` -> `public void Dispose() {`

#### `src/Avalonia.Base/Layout/Layoutable.cs`

- `Layoutable` -> `public void UpdateLayout() => (this.GetVisualRoot() as ILayoutRoot)?.LayoutManager?.ExecuteLayoutPass();`

#### `src/Avalonia.Base/Media/DrawingContext.cs`

- `DrawingContext` -> `public PushedState PushPostTransform(Matrix matrix) => PushTransform(matrix);`
- `DrawingContext` -> `public PushedState PushPreTransform(Matrix matrix) => PushTransform(matrix);`
- `DrawingContext` -> `public PushedState PushTransformContainer() => PushTransform(Matrix.Identity);`

#### `src/Avalonia.Base/Media/DrawingImage.cs`

- `DrawingImage` -> `public Size Size => Drawing?.GetBounds().Size ?? default;`

#### `src/Avalonia.Base/Media/FontManager.cs`

- `FontManager` -> `public IFontCollection SystemFonts => _fontCollections[SystemFontsKey];`
- `FontManager` -> `public bool TryGetGlyphTypeface(Typeface typeface, [NotNullWhen(true)] out IGlyphTypeface? glyphTypeface) {`

#### `src/Avalonia.Base/Media/FontMetrics.cs`

- `FontMetrics` -> `public short DesignEmHeight { get; init; }`

#### `src/Avalonia.Base/Media/Fonts/EmbeddedFontCollection.cs`

- `EmbeddedFontCollection` -> `public bool TryGetFamilyTypefaces(string familyName, [NotNullWhen(true)] out IReadOnlyList<Typeface>? familyTypefaces) {`
- `public class EmbeddedFontCollection : FontCollectionBase, IFontCollection2 {`
- `EmbeddedFontCollection` -> `public override FontFamily this[int index] => _fontFamilies[index];`
- `EmbeddedFontCollection` -> `public override IEnumerator<FontFamily> GetEnumerator() => _fontFamilies.GetEnumerator();`
- `EmbeddedFontCollection` -> `public override bool TryGetGlyphTypeface(string familyName, FontStyle style, FontWeight weight, FontStretch stretch, [NotNullWhen(true)] out IGlyphTypeface? glyphTypeface) {`
- `EmbeddedFontCollection` -> `public override int Count => _fontFamilies.Count;`
- `EmbeddedFontCollection` -> `public override void Initialize(IFontManagerImpl fontManager) {`

#### `src/Avalonia.Base/Media/Fonts/FontCollectionBase.cs`

- `FontCollectionBase` -> `public abstract FontFamily this[int index] { get; }`
- `FontCollectionBase` -> `public abstract IEnumerator<FontFamily> GetEnumerator();`
- `FontCollectionBase` -> `public abstract bool TryGetGlyphTypeface(string familyName, FontStyle style, FontWeight weight, FontStretch stretch, [NotNullWhen(true)] out IGlyphTypeface? glyphTypeface);`
- `FontCollectionBase` -> `public abstract int Count { get; }`
- `FontCollectionBase` -> `public abstract void Initialize(IFontManagerImpl fontManager);`
- `FontCollectionBase` -> `public virtual bool TryCreateSyntheticGlyphTypeface( IGlyphTypeface glyphTypeface, FontStyle style, FontWeight weight, FontStretch stretch, [NotNullWhen(true)] out IGlyphTypeface? syntheticGlyphTypeface) {`

#### `src/Avalonia.Base/Media/Fonts/FontFamilyLoader.cs`

- `FontFamilyLoader` -> `public static IEnumerable<Uri> LoadFontAssets(Uri source) {`
- `public static class FontFamilyLoader {`

#### `src/Avalonia.Base/Media/Fonts/IFontCollection.cs`

- `IFontCollection` -> `bool TryGetGlyphTypeface(string familyName, FontStyle style, FontWeight weight, FontStretch stretch, [NotNullWhen(true)] out IGlyphTypeface? glyphTypeface);`
- `IFontCollection` -> `void Initialize(IFontManagerImpl fontManager);`

#### `src/Avalonia.Base/Media/GlyphMetrics.cs`

- `GlyphMetrics` -> `public int Height{ get; init; }`
- `GlyphMetrics` -> `public int Width{ get; init; }`
- `GlyphMetrics` -> `public int YBearing{ get; init; }`

#### `src/Avalonia.Base/Media/GlyphRun.cs`

- `GlyphRun` -> `public GlyphRun( IGlyphTypeface glyphTypeface, double fontRenderingEmSize, ReadOnlyMemory<char> characters, IReadOnlyList<GlyphInfo> glyphInfos, Point? baselineOrigin = null, int biDiLevel = 0) {`
- `GlyphRun` -> `public GlyphRun( IGlyphTypeface glyphTypeface, double fontRenderingEmSize, ReadOnlyMemory<char> characters, IReadOnlyList<ushort> glyphIndices, Point? baselineOrigin = null, int biDiLevel = 0) : this(glyphTypeface, fontRenderingEmSize, characters, CreateGlyphInfos(glyphIndices, fontRenderingEmSize, glyphTypeface), baselineOrigin, biDiLevel) {`
- `GlyphRun` -> `public IGlyphTypeface GlyphTypeface { get; }`

#### `src/Avalonia.Base/Media/IGlyphTypeface.cs`

- `IGlyphTypeface` -> `FontMetrics Metrics { get; }`
- `IGlyphTypeface` -> `FontSimulations FontSimulations { get; }`
- `IGlyphTypeface` -> `FontStretch Stretch { get; }`
- `IGlyphTypeface` -> `FontStyle Style { get; }`
- `IGlyphTypeface` -> `FontWeight Weight { get; }`
- `IGlyphTypeface` -> `bool TryGetGlyph(uint codepoint, out ushort glyph);`
- `IGlyphTypeface` -> `bool TryGetGlyphMetrics(ushort glyph, out GlyphMetrics metrics);`
- `IGlyphTypeface` -> `bool TryGetTable(uint tag, out byte[] table);`
- `IGlyphTypeface` -> `int GetGlyphAdvance(ushort glyph);`
- `IGlyphTypeface` -> `int GlyphCount { get; }`
- `IGlyphTypeface` -> `int[] GetGlyphAdvances(ReadOnlySpan<ushort> glyphs);`
- `public interface IGlyphTypeface : IDisposable {`
- `IGlyphTypeface` -> `string FamilyName { get; }`
- `IGlyphTypeface` -> `ushort GetGlyph(uint codepoint);`
- `IGlyphTypeface` -> `ushort[] GetGlyphs(ReadOnlySpan<uint> codepoints);`

#### `src/Avalonia.Base/Media/Imaging/Bitmap.cs`

- `Bitmap` -> `public virtual AlphaFormat? AlphaFormat => (PlatformImpl.Item as IReadableBitmapWithAlphaImpl)?.AlphaFormat;`
- `Bitmap` -> `public void CopyPixels(ILockedFramebuffer buffer, AlphaFormat alphaFormat) {`

#### `src/Avalonia.Base/Media/RadialGradientBrush.cs`

- `RadialGradientBrush` -> `public double Radius {`
- `RadialGradientBrush` -> `public static readonly StyledProperty<double> RadiusProperty = AvaloniaProperty.Register<RadialGradientBrush, double>( nameof(Radius), 0.5);`

#### `src/Avalonia.Base/Media/StreamGeometryContext.cs`

- `public class StreamGeometryContext : IGeometryContext, IGeometryContext2 {`
- `StreamGeometryContext` -> `public void ArcTo(Point point, Size size, double rotationAngle, bool isLargeArc, SweepDirection sweepDirection) {`
- `StreamGeometryContext` -> `public void ArcTo(Point point, Size size, double rotationAngle, bool isLargeArc, SweepDirection sweepDirection, bool isStroked) {`
- `StreamGeometryContext` -> `public void BeginFigure(Point startPoint, bool isFilled) {`
- `StreamGeometryContext` -> `public void CubicBezierTo(Point controlPoint1, Point controlPoint2, Point endPoint) {`
- `StreamGeometryContext` -> `public void CubicBezierTo(Point controlPoint1, Point controlPoint2, Point endPoint, bool isStroked) {`
- `StreamGeometryContext` -> `public void LineTo(Point endPoint) {`
- `StreamGeometryContext` -> `public void LineTo(Point point, bool isStroked) {`
- `StreamGeometryContext` -> `public void QuadraticBezierTo(Point controlPoint , Point endPoint) {`
- `StreamGeometryContext` -> `public void QuadraticBezierTo(Point controlPoint, Point endPoint, bool isStroked) {`

#### `src/Avalonia.Base/Media/TextFormatting/GenericTextParagraphProperties.cs`

- `GenericTextParagraphProperties` -> `public GenericTextParagraphProperties( FlowDirection flowDirection, TextAlignment textAlignment, bool firstLineInParagraph, bool alwaysCollapsible, TextRunProperties defaultTextRunProperties, TextWrapping textWrap, double lineHeight, double indent, double letterSpacing) {`
- `GenericTextParagraphProperties` -> `public GenericTextParagraphProperties(TextRunProperties defaultTextRunProperties, TextAlignment textAlignment = TextAlignment.Left, TextWrapping textWrap = TextWrapping.NoWrap, double lineHeight = 0, double letterSpacing = 0) {`

#### `src/Avalonia.Base/Media/TextFormatting/GenericTextRunProperties.cs`

- `GenericTextRunProperties` -> `public GenericTextRunProperties( Typeface typeface, FontFeatureCollection? fontFeatures, double fontRenderingEmSize = DefaultFontRenderingEmSize, TextDecorationCollection? textDecorations = null, IBrush? foregroundBrush = null, IBrush? backgroundBrush = null, BaselineAlignment baselineAlignment = BaselineAlignment.Baseline, CultureInfo? cultureInfo = null) {`
- `GenericTextRunProperties` -> `public GenericTextRunProperties(Typeface typeface, double fontRenderingEmSize = DefaultFontRenderingEmSize, TextDecorationCollection? textDecorations = null, IBrush? foregroundBrush = null, IBrush? backgroundBrush = null, BaselineAlignment baselineAlignment = BaselineAlignment.Baseline, CultureInfo? cultureInfo = null) : this(typeface, null, fontRenderingEmSize, textDecorations, foregroundBrush, backgroundBrush, baselineAlignment, cultureInfo) {`

#### `src/Avalonia.Base/Media/TextFormatting/ShapedBuffer.cs`

- `ShapedBuffer` -> `public IGlyphTypeface GlyphTypeface { get; }`
- `ShapedBuffer` -> `public ShapedBuffer(ReadOnlyMemory<char> text, int bufferLength, IGlyphTypeface glyphTypeface, double fontRenderingEmSize, sbyte bidiLevel) {`

#### `src/Avalonia.Base/Media/TextFormatting/TextCollapsingProperties.cs`

- `TextCollapsingProperties` -> `public static TextRun[] CreateCollapsedRuns(TextLine textLine, int collapsedLength, FlowDirection flowDirection, TextRun shapedSymbol) {`

#### `src/Avalonia.Base/Media/TextFormatting/TextLayout.cs`

- `TextLayout` -> `public TextLayout( string? text, Typeface typeface, FontFeatureCollection? fontFeatures, double fontSize, IBrush? foreground, TextAlignment textAlignment = TextAlignment.Left, TextWrapping textWrapping = TextWrapping.NoWrap, TextTrimming? textTrimming = null, TextDecorationCollection? textDecorations = null, FlowDirection flowDirection = FlowDirection.LeftToRight, double maxWidth = double.PositiveInfinity, double maxHeight = double.PositiveInfinity, double lineHeight = double.NaN, double letterSpacing = 0, int maxLines = 0, IReadOnlyList<ValueSpan<TextRunProperties>>? textStyleOverrides = null) {`
- `TextLayout` -> `public TextLayout( string? text, Typeface typeface, double fontSize, IBrush? foreground, TextAlignment textAlignment = TextAlignment.Left, TextWrapping textWrapping = TextWrapping.NoWrap, TextTrimming? textTrimming = null, TextDecorationCollection? textDecorations = null, FlowDirection flowDirection = FlowDirection.LeftToRight, double maxWidth = double.PositiveInfinity, double maxHeight = double.PositiveInfinity, double lineHeight = double.NaN, double letterSpacing = 0, int maxLines = 0, IReadOnlyList<ValueSpan<TextRunProperties>>? textStyleOverrides = null) : this(text, typeface, null, fontSize, foreground, textAlignment, textWrapping, textTrimming, textDecorations, flowDirection, maxWidth, maxHeight, lineHeight, letterSpacing, maxLines, textStyleOverrides) {`

#### `src/Avalonia.Base/Media/TextFormatting/TextMetrics.cs`

- `TextMetrics` -> `public TextMetrics(IGlyphTypeface glyphTypeface, double fontRenderingEmSize) {`

#### `src/Avalonia.Base/Media/TextFormatting/TextShaperOptions.cs`

- `TextShaperOptions` -> `public IGlyphTypeface Typeface { get; }`
- `TextShaperOptions` -> `public TextShaperOptions( IGlyphTypeface typeface, IReadOnlyList<FontFeature>? fontFeatures, double fontRenderingEmSize = 12, sbyte bidiLevel = 0, CultureInfo? culture = null, double incrementalTabWidth = 0, double letterSpacing = 0) {`
- `TextShaperOptions` -> `public TextShaperOptions( IGlyphTypeface typeface, double fontRenderingEmSize = 12, sbyte bidiLevel = 0, CultureInfo? culture = null, double incrementalTabWidth = 0, double letterSpacing = 0) : this(typeface, null, fontRenderingEmSize, bidiLevel, culture, incrementalTabWidth, letterSpacing) {`

#### `src/Avalonia.Base/Media/Typeface.cs`

- `Typeface` -> `public IGlyphTypeface GlyphTypeface {`

#### `src/Avalonia.Base/Platform/ICursorFactory.cs`

- `ICursorFactory` -> `ICursorImpl CreateCursor(IBitmapImpl cursor, PixelPoint hotSpot);`

#### `src/Avalonia.Base/Platform/IDrawingContextImpl.cs`

- `public interface IDrawingContextLayerImpl : IRenderTargetBitmapImpl {`

#### `src/Avalonia.Base/Platform/IFontManagerImpl.cs`

- `IFontManagerImpl` -> `bool TryCreateGlyphTypeface(Stream stream, FontSimulations fontSimulations, [NotNullWhen(returnValue: true)] out IGlyphTypeface? glyphTypeface);`
- `IFontManagerImpl` -> `bool TryCreateGlyphTypeface(string familyName, FontStyle style, FontWeight weight, FontStretch stretch, [NotNullWhen(returnValue: true)] out IGlyphTypeface? glyphTypeface);`
- `IFontManagerImpl` -> `bool TryMatchCharacter(int codepoint, FontStyle fontStyle, FontWeight fontWeight, FontStretch fontStretch, CultureInfo? culture, out Typeface typeface);`

#### `src/Avalonia.Base/Platform/IGeometryContext.cs`

- `IGeometryContext` -> `void ArcTo(Point point, Size size, double rotationAngle, bool isLargeArc, SweepDirection sweepDirection);`
- `IGeometryContext` -> `void CubicBezierTo(Point controlPoint1, Point controlPoint2, Point endPoint);`
- `IGeometryContext` -> `void LineTo(Point endPoint);`
- `IGeometryContext` -> `void QuadraticBezierTo(Point controlPoint , Point endPoint);`

#### `src/Avalonia.Base/Platform/IGeometryContext2.cs`

- `public interface IGeometryContext2 : IGeometryContext {`
- `IGeometryContext2` -> `void ArcTo(Point point, Size size, double rotationAngle, bool isLargeArc, SweepDirection sweepDirection, bool isStroked);`
- `IGeometryContext2` -> `void CubicBezierTo(Point controlPoint1, Point controlPoint2, Point endPoint, bool isStroked);`
- `IGeometryContext2` -> `void LineTo(Point point, bool isStroked);`
- `IGeometryContext2` -> `void QuadraticBezierTo(Point controlPoint, Point endPoint, bool isStroked);`

#### `src/Avalonia.Base/Platform/IGlyphRunImpl.cs`

- `IGlyphRunImpl` -> `IGlyphTypeface GlyphTypeface { get; }`

#### `src/Avalonia.Base/Platform/IOptionalFeatureProvider.cs`

- Namespace(s): `Avalonia.Platform`
- `public interface IOptionalFeatureProvider {`
- `IOptionalFeatureProvider` -> `public object? TryGetFeature(Type featureType);`
- `OptionalFeatureProviderExtensions` -> `public static T? TryGetFeature<T>(this IOptionalFeatureProvider provider) where T : class =>`
- `OptionalFeatureProviderExtensions` -> `public static bool TryGetFeature<T>(this IOptionalFeatureProvider provider, [MaybeNullWhen(false)] out T rv) where T : class {`
- `public static class OptionalFeatureProviderExtensions {`

#### `src/Avalonia.Base/Platform/IPlatformRenderInterface.cs`

- `IPlatformRenderInterfaceContext` -> `IDrawingContextLayerImpl CreateOffscreenRenderTarget(PixelSize pixelSize, double scaling);`
- `IPlatformRenderInterface` -> `IGlyphRunImpl CreateGlyphRun(IGlyphTypeface glyphTypeface, double fontRenderingEmSize, IReadOnlyList<GlyphInfo> glyphInfos, Point baselineOrigin);`
- `IPlatformRenderInterfaceContext` -> `IRenderTarget CreateRenderTarget(IEnumerable<object> surfaces);`

#### `src/Avalonia.Base/Platform/IReadableBitmapImpl.cs`

- Namespace(s): `Avalonia.Platform`
- `IReadableBitmapWithAlphaImpl` -> `AlphaFormat? AlphaFormat { get; }`
- `public interface IReadableBitmapImpl {`
- `public interface IReadableBitmapWithAlphaImpl : IReadableBitmapImpl {`

#### `src/Avalonia.Base/Platform/IRenderTarget.cs`

- `IRenderTarget2` -> `IDrawingContextImpl CreateDrawingContext(PixelSize expectedPixelSize, out RenderTargetDrawingContextProperties properties);`
- `IRenderTarget` -> `IDrawingContextImpl CreateDrawingContext(bool useScaledDrawing);`
- `IRenderTargetWithProperties` -> `RenderTargetProperties Properties { get; }`
- `IRenderTarget2` -> `RenderTargetProperties Properties { get; }`
- `IRenderTarget` -> `public bool IsCorrupted { get; }`
- `public interface IRenderTarget2 : IRenderTarget {`
- `public interface IRenderTargetWithProperties : IRenderTarget {`

#### `src/Avalonia.Base/Platform/IRenderTargetBitmapImpl.cs`

- `public interface IRenderTargetBitmapImpl : IBitmapImpl, IRenderTarget {`

#### `src/Avalonia.Base/Platform/IWriteableBitmapImpl.cs`

- `public interface IWriteableBitmapImpl : IBitmapImpl, IReadableBitmapWithAlphaImpl {`

#### `src/Avalonia.Base/Platform/LockedFramebuffer.cs`

- `LockedFramebuffer` -> `public LockedFramebuffer(IntPtr address, PixelSize size, int rowBytes, Vector dpi, PixelFormat format, Action? onDispose) {`

#### `src/Avalonia.Base/Platform/PathGeometryContext.cs`

- `PathGeometryContext` -> `public void ArcTo(Point point, Size size, double rotationAngle, bool isLargeArc, SweepDirection sweepDirection) {`
- `PathGeometryContext` -> `public void CubicBezierTo(Point controlPoint1, Point controlPoint2, Point endPoint) {`
- `PathGeometryContext` -> `public void LineTo(Point endPoint) {`
- `PathGeometryContext` -> `public void QuadraticBezierTo(Point controlPoint , Point endPoint) {`

#### `src/Avalonia.Base/Platform/Storage/SaveFilePickerResult.cs`

- Namespace(s): `Avalonia.Platform.Storage`
- `public readonly struct SaveFilePickerResult {`

#### `src/Avalonia.Base/Rendering/Composition/CompositionExternalMemory.cs`

- Namespace(s): `Avalonia.Rendering.Composition`
- `ICompositionGpuImportedObject` -> `Task ImportCompeted { get; }`

#### `src/Avalonia.Base/Rendering/Composition/Server/ServerCompositionVisual.cs`

- `ReadbackData` -> `public Matrix Matrix;`
- `UpdateResult` -> `public UpdateResult() : this(null, false, false) {`
- `ReadbackData` -> `public bool Visible;`
- `ReadbackData` -> `public long TargetId;`
- `public record struct UpdateResult(LtrbRect? Bounds, bool InvalidatedOld, bool InvalidatedNew) {`
- `public struct ReadbackData {`
- `ReadbackData` -> `public ulong Revision;`

#### `src/Avalonia.Base/Rendering/Composition/Server/ServerVisualRenderContext.cs`

- Namespace(s): `Avalonia.Rendering.Composition.Server`
- `public struct RestoreTransform(ServerVisualRenderContext? parent) : IDisposable {`
- `RestoreTransform` -> `public void Dispose() {`

#### `src/Avalonia.Base/Rendering/IRenderRoot.cs`

- `IRenderRoot` -> `PixelPoint PointToScreen(Point point);`
- `IRenderRoot` -> `Point PointToClient(PixelPoint point);`
- `IRenderRoot` -> `Size ClientSize { get; }`
- `IRenderRoot` -> `double RenderScaling { get; }`
- `IRenderRoot` -> `public IHitTester HitTester { get; }`
- `IRenderRoot` -> `public IRenderer Renderer { get; }`
- `public interface IRenderRoot {`

#### `src/Avalonia.Base/Rendering/IRenderer.cs`

- `IHitTester` -> `IEnumerable<Visual> HitTest(Point p, Visual root, Func<Visual, bool>? filter);`
- `IRenderer` -> `RendererDiagnostics Diagnostics { get; }`
- `IHitTester` -> `Visual? HitTestFirst(Point p, Visual root, Func<Visual, bool>? filter);`
- `IRenderer` -> `event EventHandler<SceneInvalidatedEventArgs>? SceneInvalidated;`
- `IRenderer` -> `public ValueTask<object?> TryGetRenderInterfaceFeature(Type featureType);`
- `public interface IHitTester {`
- `public interface IRenderer : IDisposable {`
- `IRenderer` -> `void AddDirty(Visual visual);`
- `IRenderer` -> `void Paint(Rect rect);`
- `IRenderer` -> `void RecalculateChildren(Visual visual);`
- `IRenderer` -> `void Resized(Size size);`
- `IRenderer` -> `void Start();`
- `IRenderer` -> `void Stop();`

#### `src/Avalonia.Base/Rendering/SceneInvalidatedEventArgs.cs`

- `SceneInvalidatedEventArgs` -> `public IRenderRoot RenderRoot { get; }`
- `SceneInvalidatedEventArgs` -> `public SceneInvalidatedEventArgs( IRenderRoot root, Rect dirtyRect) {`

#### `src/Avalonia.Base/StyledElement.cs`

- `public class StyledElement : Animatable, IDataContextProvider, ILogical, IThemeVariantHost, IResourceHost2, IStyleHost, ISetLogicalParent, ISetInheritanceParent, ISupportInitialize, INamed, IAvaloniaListItemValidator<ILogical>, #pragma warning disable CS0618 IStyleable #pragma warning restore CS0618 {`

#### `src/Avalonia.Base/StyledElementExtensions.cs`

- `StyledElementExtensions` -> `public static IDisposable BindClass(this StyledElement target, string className, IBinding source, object anchor) =>`

#### `src/Avalonia.Base/Styling/IStyleable.cs`

- `IStyleable` -> `AvaloniaObject? TemplatedParent { get; }`
- `IStyleable` -> `IAvaloniaReadOnlyList<string> Classes { get; }`
- `IStyleable` -> `Type StyleKey { get; }`
- `public interface IStyleable : INamed {`

#### `src/Avalonia.Base/Styling/StyleBase.cs`

- `public abstract class StyleBase : AvaloniaObject, IStyle, IResourceProvider {`

#### `src/Avalonia.Base/Threading/Dispatcher.cs`

- Namespace(s): `Avalonia.Threading`
- `Dispatcher` -> `public bool CheckAccess() => _impl.CurrentThreadIsLoopThread;`

#### `src/Avalonia.Base/Threading/DispatcherPriorityAwaitable.cs`

- Namespace(s): `Avalonia.Threading`
- `DispatcherPriorityAwaitable` -> `public DispatcherPriorityAwaitable GetAwaiter() => this;`
- `DispatcherPriorityAwaitable` -> `public bool IsCompleted => Task.IsCompleted;`
- `public class DispatcherPriorityAwaitable : INotifyCompletion {`
- `DispatcherPriorityAwaitable` -> `public new DispatcherPriorityAwaitable<T> GetAwaiter() => this;`
- `DispatcherPriorityAwaitable` -> `public new T GetResult() => ((Task<T>)Task).GetAwaiter().GetResult();`
- `public sealed class DispatcherPriorityAwaitable<T> : DispatcherPriorityAwaitable {`
- `DispatcherPriorityAwaitable` -> `public void GetResult() => Task.GetAwaiter().GetResult();`
- `DispatcherPriorityAwaitable` -> `public void OnCompleted(Action continuation) =>`

#### `src/Avalonia.Base/VisualTree/IHostedVisualTreeRoot.cs`

- `IHostedVisualTreeRoot` -> `Visual? Host { get; }`
- `public interface IHostedVisualTreeRoot {`

#### `src/Avalonia.Base/VisualTree/VisualExtensions.cs`

- `VisualExtensions` -> `public static IRenderRoot? GetVisualRoot(this Visual visual) {`

#### `src/Avalonia.Base/VisualTreeAttachmentEventArgs.cs`

- `VisualTreeAttachmentEventArgs` -> `public IRenderRoot Root { get; }`
- `VisualTreeAttachmentEventArgs` -> `public Visual Parent { get; }`
- `VisualTreeAttachmentEventArgs` -> `public VisualTreeAttachmentEventArgs(Visual parent, IRenderRoot root) {`

### Rendering and Text

#### `src/Skia/Avalonia.Skia/Gpu/ISkiaGpu.cs`

- `ISkiaGpuWithPlatformGraphicsContext` -> `IPlatformGraphicsContext? PlatformGraphicsContext { get; }`
- `ISkiaGpuWithPlatformGraphicsContext` -> `IScopedResource<GRContext>? TryGetGrContext();`
- `ISkiaGpu` -> `ISkiaGpuRenderTarget? TryCreateRenderTarget(IEnumerable<object> surfaces);`
- `ISkiaGpu` -> `ISkiaSurface? TryCreateSurface(PixelSize size, ISkiaGpuRenderSession? session);`
- `public interface ISkiaGpu : IPlatformGraphicsContext {`
- `public interface ISkiaGpuWithPlatformGraphicsContext : ISkiaGpu {`

#### `src/Skia/Avalonia.Skia/Gpu/ISkiaGpuRenderTarget.cs`

- `ISkiaGpuRenderTarget` -> `ISkiaGpuRenderSession BeginRenderingSession();`
- `ISkiaGpuRenderTarget2` -> `ISkiaGpuRenderSession BeginRenderingSession(PixelSize pixelSize);`
- `public interface ISkiaGpuRenderTarget2 : ISkiaGpuRenderTarget {`

#### `src/Skia/Avalonia.Skia/Gpu/Metal/SkiaMetalGpu.cs`

- Namespace(s): `Avalonia.Skia.Metal`
- `SkiaMetalRenderTarget` -> `public ISkiaGpuRenderSession BeginRenderingSession() {`

#### `src/Skia/Avalonia.Skia/Helpers/DrawingContextHelper.cs`

- `DrawingContextHelper` -> `public static IDrawingContextImpl WrapSkiaCanvas(SKCanvas canvas, Vector dpi) {`

#### `src/Skia/Avalonia.Skia/SkiaSharpExtensions.cs`

- `SkiaSharpExtensions` -> `public static SKFilterQuality ToSKFilterQuality(this BitmapInterpolationMode interpolationMode) {`

### Source Generator Integration

#### `src/tools/Avalonia.Generators/NameGenerator/AvaloniaNameSourceGenerator.cs`

- Namespace(s): `Avalonia.Generators.NameGenerator`
- `public class AvaloniaNameSourceGenerator : ISourceGenerator {`
- `AvaloniaNameSourceGenerator` -> `public void Execute(GeneratorExecutionContext context) {`
- `AvaloniaNameSourceGenerator` -> `public void Initialize(GeneratorInitializationContext context) { }`

### Windows Platform

#### `src/Windows/Avalonia.Direct2D1/Direct2D1Platform.cs`

- `Direct2DApplicationExtensions` -> `public static AppBuilder UseDirect2D1(this AppBuilder builder) {`
- `public static class Direct2DApplicationExtensions {`

#### `src/Windows/Avalonia.Direct2D1/IExternalDirect2DRenderTargetSurface.cs`

- `IExternalDirect2DRenderTargetSurface` -> `SharpDX.Direct2D1.RenderTarget GetOrCreateRenderTarget();`
- `public interface IExternalDirect2DRenderTargetSurface {`
- `IExternalDirect2DRenderTargetSurface` -> `void AfterDrawing();`
- `IExternalDirect2DRenderTargetSurface` -> `void BeforeDrawing();`
- `IExternalDirect2DRenderTargetSurface` -> `void DestroyRenderTarget();`

#### `src/Windows/Avalonia.Win32/DirectX/IDirect3D11TexturePlatformSurface.cs`

- Namespace(s): `Avalonia.Win32.DirectX`
- `public interface IDirect3D11TexturePlatformSurface {`

### XAML and Markup

#### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/CompiledBindingExtension.cs`

- `CompiledBindingExtension` -> `public CompiledBindingExtension ProvideValue(IServiceProvider provider) {`
- `CompiledBindingExtension` -> `public CompiledBindingPath Path { get; set; }`
- `public class CompiledBindingExtension : BindingBase {`
- `CompiledBindingExtension` -> `public object? Source { get; set; } = AvaloniaProperty.UnsetValue;`
- `CompiledBindingExtension` -> `public override InstancedBinding? Initiate( AvaloniaObject target, AvaloniaProperty? targetProperty, object? anchor = null, bool enableDataValidation = false) {`

#### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/CompiledBindings/CompiledBindingPath.cs`

- `CompiledBindingPathBuilder` -> `public CompiledBindingPathBuilder SetRawSource(object? rawSource) {`
- `CompiledBindingPathBuilder` -> `public CompiledBindingPathBuilder(int apiVersion) => _apiVersion = apiVersion;`
- `CompiledBindingPath` -> `public override string ToString() => string.Concat((IEnumerable<ICompiledBindingPathElement>) _elements);`

#### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/DynamicResourceExtension.cs`

- `DynamicResourceExtension` -> `public IBinding ProvideValue(IServiceProvider serviceProvider) {`
- `public class DynamicResourceExtension : IBinding2 {`

#### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/ReflectionBindingExtension.cs`

- `ReflectionBindingExtension` -> `public Binding ProvideValue(IServiceProvider serviceProvider) {`
- `ReflectionBindingExtension` -> `public BindingMode Mode { get; set; }`
- `ReflectionBindingExtension` -> `public BindingPriority Priority { get; set; } = BindingPriority.LocalValue;`
- `ReflectionBindingExtension` -> `public CultureInfo? ConverterCulture { get; set; }`
- `ReflectionBindingExtension` -> `public IValueConverter? Converter { get; set; }`
- `ReflectionBindingExtension` -> `public ReflectionBindingExtension() {`
- `ReflectionBindingExtension` -> `public ReflectionBindingExtension(string path) {`
- `ReflectionBindingExtension` -> `public RelativeSource? RelativeSource { get; set; }`
- `ReflectionBindingExtension` -> `public UpdateSourceTrigger UpdateSourceTrigger { get; set; }`
- `public class ReflectionBindingExtension {`
- `ReflectionBindingExtension` -> `public int Delay { get; set; }`
- `ReflectionBindingExtension` -> `public object? ConverterParameter { get; set; }`
- `ReflectionBindingExtension` -> `public object? FallbackValue { get; set; } = AvaloniaProperty.UnsetValue;`
- `ReflectionBindingExtension` -> `public object? Source { get; set; } = AvaloniaProperty.UnsetValue;`
- `ReflectionBindingExtension` -> `public object? TargetNullValue { get; set; } = AvaloniaProperty.UnsetValue;`
- `ReflectionBindingExtension` -> `public string Path { get; set; } = "";`
- `ReflectionBindingExtension` -> `public string? ElementName { get; set; }`
- `ReflectionBindingExtension` -> `public string? StringFormat { get; set; }`

#### `src/Markup/Avalonia.Markup.Xaml/Templates/TreeDataTemplate.cs`

- `TreeDataTemplate` -> `public InstancedBinding? ItemsSelector(object item) {`

#### `src/Markup/Avalonia.Markup.Xaml/XamlTypes.cs`

- `ConstructorArgumentAttribute` -> `public ConstructorArgumentAttribute(string name) {`
- `public sealed class ConstructorArgumentAttribute : Attribute {`

#### `src/Markup/Avalonia.Markup/Data/Binding.cs`

- `Binding` -> `public Binding() {`
- `Binding` -> `public Binding(string path, BindingMode mode = BindingMode.Default) : base(mode) {`
- `Binding` -> `public Func<string?, string, Type>? TypeResolver { get; set; }`
- `Binding` -> `public RelativeSource? RelativeSource { get; set; }`
- `public class Binding : BindingBase {`
- `Binding` -> `public object? Source { get; set; } = AvaloniaProperty.UnsetValue;`
- `Binding` -> `public override InstancedBinding? Initiate( AvaloniaObject target, AvaloniaProperty? targetProperty, object? anchor = null, bool enableDataValidation = false) {`
- `Binding` -> `public string Path { get; set; } = "";`
- `Binding` -> `public string? ElementName { get; set; }`

#### `src/Markup/Avalonia.Markup/Data/BindingBase.cs`

- `BindingBase` -> `public BindingBase() {`
- `BindingBase` -> `public BindingBase(BindingMode mode = BindingMode.Default) :this() {`
- `BindingBase` -> `public BindingMode Mode { get; set; }`
- `BindingBase` -> `public BindingPriority Priority { get; set; }`
- `BindingBase` -> `public CultureInfo? ConverterCulture { get; set; }`
- `BindingBase` -> `public IValueConverter? Converter { get; set; }`
- `BindingBase` -> `public UpdateSourceTrigger UpdateSourceTrigger { get; set; }`
- `BindingBase` -> `public WeakReference<INameScope?>? NameScope { get; set; }`
- `BindingBase` -> `public WeakReference? DefaultAnchor { get; set; }`
- `BindingBase` -> `public abstract InstancedBinding? Initiate( AvaloniaObject target, AvaloniaProperty? targetProperty, object? anchor = null, bool enableDataValidation = false);`
- `public abstract class BindingBase : IBinding, IBinding2 {`
- `BindingBase` -> `public int Delay { get; set; }`
- `BindingBase` -> `public object? ConverterParameter { get; set; }`
- `BindingBase` -> `public object? FallbackValue { get; set; }`
- `BindingBase` -> `public object? TargetNullValue { get; set; }`
- `BindingBase` -> `public string? StringFormat { get; set; }`

#### `src/Markup/Avalonia.Markup/Data/MultiBinding.cs`

- `MultiBinding` -> `public IList<IBinding> Bindings { get; set; } = new List<IBinding>();`
- `MultiBinding` -> `public InstancedBinding? Initiate( AvaloniaObject target, AvaloniaProperty? targetProperty, object? anchor = null, bool enableDataValidation = false) {`
- `public class MultiBinding : IBinding2 {`

### iOS Platform

#### `src/iOS/Avalonia.iOS/AvaloniaAppDelegate.cs`

- `AvaloniaAppDelegate` -> `public bool FinishedLaunching(UIApplication application, NSDictionary launchOptions) {`
- `public class AvaloniaAppDelegate<TApp> : UIResponder, IUIApplicationDelegate, IAvaloniaAppDelegate where TApp : Application, new() {`

### macOS Native Platform

#### `src/Avalonia.Native/AvaloniaNativePlatformExtensions.cs`

- `AvaloniaNativePlatformOptions` -> `public string AvaloniaNativeLibraryPath { get; set; }`
