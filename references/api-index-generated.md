# Avalonia Public API Index (Generated)

- Generated at (UTC): `2026-02-15 20:44:52Z`
- Repository: `Avalonia@11.3.12`
- Git ref: `11.3.12`
- Files scanned: `2667`
- Captured public signatures: `9995`

## Scope

This index targets public APIs across Avalonia product source files and build configuration surfaces.

## Regenerate

```bash
python3 scripts/generate_api_index.py --repo <path-to-avalonia-repo> --git-ref 11.3.12 --output references/api-index-generated.md
```

## Android Platform

### `src/Android/Avalonia.Android/AndroidPlatform.cs`
- `public static class AndroidApplicationExtensions`
- `public static AppBuilder UseAndroid(this AppBuilder builder) {`
- `public enum AndroidRenderingMode`
- `public sealed class AndroidPlatformOptions`
- `public IReadOnlyList<AndroidRenderingMode> RenderingMode { get; set; } = new[]`

### `src/Android/Avalonia.Android/AndroidViewControlHandle.cs`
- `public class AndroidViewControlHandle : PlatformHandle, INativeControlHostDestroyableControlHandle`
- `public AndroidViewControlHandle(View view) : base(view.Handle, AndroidViewDescriptor) {`
- `public View View { get; private set; }`
- `public void Destroy() {`

### `src/Android/Avalonia.Android/Automation/INodeInfoProvider.cs`
- `public interface INodeInfoProvider`

### `src/Android/Avalonia.Android/AvaloniaActivity.cs`
- Namespace: `Avalonia.Android`
- `public class AvaloniaActivity : AppCompatActivity, IAvaloniaActivity`
- `public Action<int, Result, Intent?>? ActivityResult { get; set; }`
- `public Action<int, string[], Permission[]>? RequestPermissionsResult { get; set; }`
- `public event EventHandler<AndroidBackRequestedEventArgs>? BackRequested;`
- `public object? Content {`
- `public override void OnBackPressed() {`
- `public override void OnRequestPermissionsResult(int requestCode, string[] permissions, Permission[] grantResults) {`
- `public void OnBackInvoked() {`

### `src/Android/Avalonia.Android/AvaloniaMainActivity.App.cs`
- `public class AvaloniaMainActivity<TApp> : AvaloniaMainActivity`

### `src/Android/Avalonia.Android/AvaloniaMainActivity.cs`
- Namespace: `Avalonia.Android`
- `public class AvaloniaMainActivity : AvaloniaActivity`

### `src/Android/Avalonia.Android/AvaloniaView.Input.cs`
- `public partial class AvaloniaView : IInitEditorInfo`
- `public override IInputConnection OnCreateInputConnection(EditorInfo? outAttrs) {`
- `public override bool DispatchTouchEvent(MotionEvent? e) {`
- `public override bool DispatchKeyEvent(KeyEvent? e) {`

### `src/Android/Avalonia.Android/AvaloniaView.cs`
- `public partial class AvaloniaView : FrameLayout`
- `public AvaloniaView(Context context) : base(context) {`
- `public object? Content {`
- `public override void OnVisibilityAggregated(bool isVisible) {`

### `src/Android/Avalonia.Android/IActivityResultHandler.cs`
- Namespace: `Avalonia.Android`
- `public interface IActivityResultHandler`
- `public Action<int, Result, Intent?>? ActivityResult { get; set; }`
- `public Action<int, string[], Permission[]>? RequestPermissionsResult { get; set; }`

### `src/Android/Avalonia.Android/IAndroidNavigationService.cs`
- `public interface IActivityNavigationService`
- `public class AndroidBackRequestedEventArgs : EventArgs`
- `public bool Handled { get; set; }`

### `src/Android/Avalonia.Android/IAvaloniaActivity.cs`
- Namespace: `Avalonia.Android`
- `public interface IAvaloniaActivity : IActivityResultHandler, IActivityNavigationService`

### `src/Android/Avalonia.Android/Platform/SkiaPlatform/AndroidFramebuffer.cs`
- `public enum AndroidPixelFormat`

### `src/Android/Avalonia.Android/Platform/Specific/IAndroidView.cs`
- `public interface IAndroidView`

## Application Model and Controls

### `src/Avalonia.Controls/AcrylicPlatformCompensationLevels.cs`
- `public record struct AcrylicPlatformCompensationLevels`
- `public AcrylicPlatformCompensationLevels(double transparent, double blurred, double acrylic) {`
- `public double TransparentLevel { get; }`
- `public double BlurLevel { get; }`
- `public double AcrylicBlurLevel { get; }`

### `src/Avalonia.Controls/AppBuilder.cs`
- `public sealed class AppBuilder`
- `public Action? RuntimePlatformServicesInitializer { get; private set; }`
- `public string? RuntimePlatformServicesName { get; private set; }`
- `public Application? Instance { get; private set; }`
- `public Type? ApplicationType { get; private set; }`
- `public Action? WindowingSubsystemInitializer { get; private set; }`
- `public string? WindowingSubsystemName { get; private set; }`
- `public Action? RenderingSubsystemInitializer { get; private set; }`
- `public Func<Type, IApplicationLifetime?>? LifetimeOverride { get; private set; }`
- `public string? RenderingSubsystemName { get; private set; }`
- `public Action<AppBuilder> AfterSetupCallback { get; private set; } = builder => { };`
- `public Action<AppBuilder> AfterPlatformServicesSetupCallback { get; private set; } = builder => { };`
- `public static AppBuilder Configure<TApp>() where TApp : Application, new() {`
- `public static AppBuilder Configure<TApp>(Func<TApp> appFactory) where TApp : Application {`
- `public AppBuilder AfterSetup(Action<AppBuilder> callback) {`
- `public AppBuilder AfterApplicationSetup(Action<AppBuilder> callback) {`
- `public AppBuilder AfterPlatformServicesSetup(Action<AppBuilder> callback) {`
- `public delegate void AppMainDelegate(Application app, string[] args);`
- `public void Start(AppMainDelegate main, string[] args) {`
- `public AppBuilder SetupWithoutStarting() {`
- `public AppBuilder SetupWithLifetime(IApplicationLifetime lifetime) {`
- `public AppBuilder UseWindowingSubsystem(Action initializer, string name = "") {`
- `public AppBuilder UseRenderingSubsystem(Action initializer, string name = "") {`
- `public AppBuilder UseRuntimePlatformSubsystem(Action initializer, string name = "") {`
- `public AppBuilder UseStandardRuntimePlatformSubsystem() {`
- `public AppBuilder With<T>(T options) {`
- `public AppBuilder With<T>(Func<T> options) {`
- `public AppBuilder ConfigureFonts(Action<FontManager> action) {`

### `src/Avalonia.Controls/Application.cs`
- `public class Application : AvaloniaObject, IDataContextProvider, IGlobalDataTemplates, IGlobalStyles, IThemeVariantHost, IResourceHost2, IApplicationPlatformEvents, IOptionalFeatureProvider`
- `public static readonly StyledProperty<object?> DataContextProperty = StyledElement.DataContextProperty.AddOwner<Application>();`
- `public static readonly StyledProperty<ThemeVariant> ActualThemeVariantProperty = ThemeVariantScope.ActualThemeVariantProperty.AddOwner<Application>();`
- `public static readonly StyledProperty<ThemeVariant?> RequestedThemeVariantProperty = ThemeVariantScope.RequestedThemeVariantProperty.AddOwner<Application>();`
- `public event EventHandler<ResourcesChangedEventArgs>? ResourcesChanged;`
- `public event EventHandler<UrlOpenedEventArgs>? UrlsOpened;`
- `public event EventHandler? ActualThemeVariantChanged;`
- `public Application() {`
- `public object? DataContext {`
- `public ThemeVariant? RequestedThemeVariant {`
- `public ThemeVariant ActualThemeVariant => GetValue(ActualThemeVariantProperty);`
- `public static Application? Current {`
- `public DataTemplates DataTemplates => _dataTemplates ?? (_dataTemplates = new DataTemplates());`
- `public IResourceDictionary Resources {`
- `public Styles Styles => _styles ??= new Styles(this);`
- `public IApplicationLifetime? ApplicationLifetime {`
- `public IPlatformSettings? PlatformSettings => this.TryGetFeature<IPlatformSettings>();`
- `public virtual void Initialize() { }`
- `public bool TryGetResource(object key, ThemeVariant? theme, out object? value) {`
- `public virtual void RegisterServices() {`
- `public virtual void OnFrameworkInitializationCompleted() {`
- `public static readonly DirectProperty<Application, string?> NameProperty = AvaloniaProperty.RegisterDirect<Application, string?>("Name", o => o.Name, (o, v) => o.Name = v);`
- `public string? Name {`
- `public object? TryGetFeature(Type featureType) {`

### `src/Avalonia.Controls/ApplicationLifetimes/ActivatableLifetimeBase.cs`
- Namespace: `Avalonia.Controls.ApplicationLifetimes`
- `public abstract class ActivatableLifetimeBase : IActivatableLifetime`
- `public event EventHandler<ActivatedEventArgs>? Activated;`
- `public event EventHandler<ActivatedEventArgs>? Deactivated;`
- `public virtual bool TryLeaveBackground() => false;`
- `public virtual bool TryEnterBackground() => false;`

### `src/Avalonia.Controls/ApplicationLifetimes/ActivatedEventArgs.cs`
- Namespace: `Avalonia.Controls.ApplicationLifetimes`
- `public class ActivatedEventArgs : EventArgs`
- `public ActivatedEventArgs(ActivationKind kind) {`
- `public ActivationKind Kind { get; }`

### `src/Avalonia.Controls/ApplicationLifetimes/ActivationKind.cs`
- Namespace: `Avalonia.Controls.ApplicationLifetimes`
- `public enum ActivationKind`

### `src/Avalonia.Controls/ApplicationLifetimes/ClassicDesktopStyleApplicationLifetime.cs`
- `public class ClassicDesktopStyleApplicationLifetime : IClassicDesktopStyleApplicationLifetime, IDisposable`
- `public event EventHandler<ControlledApplicationLifetimeStartupEventArgs>? Startup;`
- `public event EventHandler<ShutdownRequestedEventArgs>? ShutdownRequested;`
- `public event EventHandler<ControlledApplicationLifetimeExitEventArgs>? Exit;`
- `public string[]? Args { get; set; }`
- `public ShutdownMode ShutdownMode { get; set; }`
- `public Window? MainWindow { get; set; }`
- `public IReadOnlyList<Window> Windows => _windows;`
- `public void Shutdown(int exitCode = 0) {`
- `public bool TryShutdown(int exitCode = 0) {`
- `public int Start(string[] args) {`
- `public int Start() {`
- `public void Dispose() {`
- `public class ClassicDesktopStyleApplicationLifetimeOptions`
- `public bool ProcessUrlActivationCommandLine { get; set; }`
- `public static class ClassicDesktopStyleApplicationLifetimeExtensions`
- `public static AppBuilder SetupWithClassicDesktopLifetime(this AppBuilder builder, string[] args, Action<IClassicDesktopStyleApplicationLifetime>? lifetimeBuilder = null) {`
- `public static int StartWithClassicDesktopLifetime( this AppBuilder builder, string[] args, Action<IClassicDesktopStyleApplicationLifetime>? lifetimeBuilder = null) {`
- `public static int StartWithClassicDesktopLifetime( this AppBuilder builder, string[] args, ShutdownMode shutdownMode) {`

### `src/Avalonia.Controls/ApplicationLifetimes/ControlledApplicationLifetimeExitEventArgs.cs`
- `public class ControlledApplicationLifetimeExitEventArgs : EventArgs`
- `public ControlledApplicationLifetimeExitEventArgs(int applicationExitCode) {`
- `public int ApplicationExitCode { get; set; }`

### `src/Avalonia.Controls/ApplicationLifetimes/FileActivatedEventArgs.cs`
- Namespace: `Avalonia.Controls.ApplicationLifetimes`
- `public sealed class FileActivatedEventArgs : ActivatedEventArgs`
- `public FileActivatedEventArgs(IReadOnlyList<IStorageItem> files) : base(ActivationKind.File) {`
- `public IReadOnlyList<IStorageItem> Files { get; }`

### `src/Avalonia.Controls/ApplicationLifetimes/IActivatableApplicationLifetime.cs`
- Namespace: `Avalonia.Controls.ApplicationLifetimes`
- `public interface IActivatableApplicationLifetime : IActivatableLifetime {`
- `public interface IActivatableLifetime`
- `public bool TryLeaveBackground();`
- `public bool TryEnterBackground();`

### `src/Avalonia.Controls/ApplicationLifetimes/IApplicationLifetime.cs`
- `public interface IApplicationLifetime`

### `src/Avalonia.Controls/ApplicationLifetimes/IClassicDesktopStyleApplicationLifetime.cs`
- `public interface IClassicDesktopStyleApplicationLifetime : IControlledApplicationLifetime`

### `src/Avalonia.Controls/ApplicationLifetimes/IControlledApplicationLifetime.cs`
- `public interface IControlledApplicationLifetime : IApplicationLifetime`

### `src/Avalonia.Controls/ApplicationLifetimes/ISingleTopLevelApplicationLifetime.cs`
- Namespace: `Avalonia.Controls.ApplicationLifetimes`
- `public interface ISingleTopLevelApplicationLifetime : IApplicationLifetime`

### `src/Avalonia.Controls/ApplicationLifetimes/ISingleViewApplicationLifetime.cs`
- `public interface ISingleViewApplicationLifetime : IApplicationLifetime`

### `src/Avalonia.Controls/ApplicationLifetimes/ProtocolActivatedEventArgs.cs`
- Namespace: `Avalonia.Controls.ApplicationLifetimes`
- `public sealed class ProtocolActivatedEventArgs : ActivatedEventArgs`
- `public ProtocolActivatedEventArgs(Uri uri) : base(ActivationKind.OpenUri) {`
- `public Uri Uri { get; }`

### `src/Avalonia.Controls/ApplicationLifetimes/ShutdownRequestedEventArgs.cs`
- `public class ShutdownRequestedEventArgs : CancelEventArgs`

### `src/Avalonia.Controls/ApplicationLifetimes/StartupEventArgs.cs`
- `public class ControlledApplicationLifetimeStartupEventArgs : EventArgs`
- `public ControlledApplicationLifetimeStartupEventArgs(IEnumerable<string> args) {`
- `public string[] Args { get; }`

### `src/Avalonia.Controls/AutoCompleteBox/AutoCompleteBox.Properties.cs`
- `public partial class AutoCompleteBox`
- `public static readonly StyledProperty<int> CaretIndexProperty = TextBox.CaretIndexProperty.AddOwner<AutoCompleteBox>(new( defaultValue: 0, defaultBindingMode: BindingMode.TwoWay));`
- `public static readonly StyledProperty<string?> WatermarkProperty = TextBox.WatermarkProperty.AddOwner<AutoCompleteBox>();`
- `public static readonly StyledProperty<int> MinimumPrefixLengthProperty = AvaloniaProperty.Register<AutoCompleteBox, int>( nameof(MinimumPrefixLength), 1, validate: IsValidMinimumPrefixLength);`
- `public static readonly StyledProperty<TimeSpan> MinimumPopulateDelayProperty = AvaloniaProperty.Register<AutoCompleteBox, TimeSpan>( nameof(MinimumPopulateDelay), TimeSpan.Zero, validate: IsValidMinimumPopulateDelay);`
- `public static readonly StyledProperty<double> MaxDropDownHeightProperty = AvaloniaProperty.Register<AutoCompleteBox, double>( nameof(MaxDropDownHeight), double.PositiveInfinity, validate: IsValidMaxDropDownHeight);`
- `public static readonly StyledProperty<bool> IsTextCompletionEnabledProperty = AvaloniaProperty.Register<AutoCompleteBox, bool>( nameof(IsTextCompletionEnabled));`
- `public static readonly StyledProperty<IDataTemplate> ItemTemplateProperty = AvaloniaProperty.Register<AutoCompleteBox, IDataTemplate>( nameof(ItemTemplate));`
- `public static readonly StyledProperty<bool> ClearSelectionOnLostFocusProperty = TextBox.ClearSelectionOnLostFocusProperty.AddOwner<AutoCompleteBox>();`
- `public static readonly StyledProperty<bool> IsDropDownOpenProperty = AvaloniaProperty.Register<AutoCompleteBox, bool>( nameof(IsDropDownOpen));`
- `public static readonly StyledProperty<object?> SelectedItemProperty = AvaloniaProperty.Register<AutoCompleteBox, object?>( nameof(SelectedItem), defaultBindingMode: BindingMode.TwoWay, enableDataValidation: true);`
- `public static readonly StyledProperty<string?> TextProperty = TextBlock.TextProperty.AddOwner<AutoCompleteBox>(new(string.Empty, defaultBindingMode: BindingMode.TwoWay, enableDataValidation: true));`
- `public static readonly DirectProperty<AutoCompleteBox, string?> SearchTextProperty = AvaloniaProperty.RegisterDirect<AutoCompleteBox, string?>( nameof(SearchText), o => o.SearchText,`
- `public static readonly StyledProperty<AutoCompleteFilterMode> FilterModeProperty = AvaloniaProperty.Register<AutoCompleteBox, AutoCompleteFilterMode>( nameof(FilterMode), defaultValue: AutoCompleteFilterMode.StartsWith, validate: IsValidFilterMode);`
- `public static readonly StyledProperty<AutoCompleteFilterPredicate<object?>?> ItemFilterProperty = AvaloniaProperty.Register<AutoCompleteBox, AutoCompleteFilterPredicate<object?>?>( nameof(ItemFilter));`
- `public static readonly StyledProperty<AutoCompleteFilterPredicate<string?>?> TextFilterProperty = AvaloniaProperty.Register<AutoCompleteBox, AutoCompleteFilterPredicate<string?>?>( nameof(TextFilter), defaultValue: AutoCompleteSearch.GetFilter(AutoCompleteFilterMode.StartsWith));`
- `public static readonly StyledProperty<AutoCompleteSelector<object>?> ItemSelectorProperty = AvaloniaProperty.Register<AutoCompleteBox, AutoCompleteSelector<object>?>( nameof(ItemSelector));`
- `public static readonly StyledProperty<AutoCompleteSelector<string?>?> TextSelectorProperty = AvaloniaProperty.Register<AutoCompleteBox, AutoCompleteSelector<string?>?>( nameof(TextSelector));`
- `public static readonly StyledProperty<IEnumerable?> ItemsSourceProperty = AvaloniaProperty.Register<AutoCompleteBox, IEnumerable?>( nameof(ItemsSource));`
- `public static readonly StyledProperty<Func<string?, CancellationToken, Task<IEnumerable<object>>>?> AsyncPopulatorProperty = AvaloniaProperty.Register<AutoCompleteBox, Func<string?, CancellationToken, Task<IEnumerable<object>>>?>( nameof(AsyncPopulator));`
- `public static readonly StyledProperty<int> MaxLengthProperty = TextBox.MaxLengthProperty.AddOwner<AutoCompleteBox>();`
- `public static readonly StyledProperty<object?> InnerLeftContentProperty = TextBox.InnerLeftContentProperty.AddOwner<AutoCompleteBox>();`
- `public static readonly StyledProperty<object?> InnerRightContentProperty = TextBox.InnerRightContentProperty.AddOwner<AutoCompleteBox>();`
- `public int CaretIndex {`
- `public int MinimumPrefixLength {`
- `public bool IsTextCompletionEnabled {`
- `public IDataTemplate ItemTemplate {`
- `public TimeSpan MinimumPopulateDelay {`
- `public double MaxDropDownHeight {`
- `public bool IsDropDownOpen {`
- `public bool ClearSelectionOnLostFocus {`
- `public IBinding? ValueMemberBinding {`
- `public object? SelectedItem {`
- `public string? Text {`
- `public string? SearchText {`
- `public AutoCompleteFilterMode FilterMode {`
- `public string? Watermark {`
- `public AutoCompleteFilterPredicate<object?>? ItemFilter {`
- `public AutoCompleteFilterPredicate<string?>? TextFilter {`
- `public AutoCompleteSelector<object>? ItemSelector {`
- `public AutoCompleteSelector<string?>? TextSelector {`
- `public Func<string?, CancellationToken, Task<IEnumerable<object>>>? AsyncPopulator {`
- `public IEnumerable? ItemsSource {`
- `public int MaxLength {`
- `public object? InnerLeftContent {`
- `public object? InnerRightContent {`

### `src/Avalonia.Controls/AutoCompleteBox/AutoCompleteBox.cs`
- `public partial class AutoCompleteBox : TemplatedControl`
- `public static readonly RoutedEvent<SelectionChangedEventArgs> SelectionChangedEvent = RoutedEvent.Register<SelectionChangedEventArgs>( nameof(SelectionChanged), RoutingStrategies.Bubble, typeof(AutoCompleteBox));`
- `public static readonly RoutedEvent<TextChangedEventArgs> TextChangedEvent = RoutedEvent.Register<AutoCompleteBox, TextChangedEventArgs>( nameof(TextChanged), RoutingStrategies.Bubble);`
- `public AutoCompleteBox() {`
- `public event EventHandler<TextChangedEventArgs>? TextChanged {`
- `public event EventHandler<PopulatingEventArgs>? Populating;`
- `public event EventHandler<PopulatedEventArgs>? Populated;`
- `public event EventHandler<CancelEventArgs>? DropDownOpening;`
- `public event EventHandler? DropDownOpened;`
- `public event EventHandler<CancelEventArgs>? DropDownClosing;`
- `public event EventHandler? DropDownClosed;`
- `public event EventHandler<SelectionChangedEventArgs> SelectionChanged {`
- `public void PopulateComplete() {`
- `public class BindingEvaluator<T> : Control`
- `public static readonly StyledProperty<T> ValueProperty = AvaloniaProperty.Register<BindingEvaluator<T>, T>(nameof(Value));`
- `public T Value {`
- `public IBinding? ValueBinding {`
- `public BindingEvaluator() { }`
- `public BindingEvaluator(IBinding? binding) : this() {`
- `public void ClearDataContext() {`
- `public T GetDynamicValue(object o, bool clearDataContext) {`
- `public T GetDynamicValue(object? o) {`

### `src/Avalonia.Controls/AutoCompleteBox/AutoCompleteFilterMode.cs`
- `public enum AutoCompleteFilterMode`

### `src/Avalonia.Controls/AutoCompleteBox/PopulatedEventArgs.cs`
- `public class PopulatedEventArgs : EventArgs`
- `public IEnumerable Data { get; private set; }`
- `public PopulatedEventArgs(IEnumerable data) {`

### `src/Avalonia.Controls/AutoCompleteBox/PopulatingEventArgs.cs`
- `public class PopulatingEventArgs : CancelEventArgs`
- `public string? Parameter { get; private set; }`
- `public PopulatingEventArgs(string? parameter) {`

### `src/Avalonia.Controls/Automation/AutomationElementIdentifiers.cs`
- `public static class AutomationElementIdentifiers`
- `public static AutomationProperty BoundingRectangleProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty ClassNameProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty NameProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty HelpTextProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty ItemStatusProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty LandmarkTypeProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty HeadingLevelProperty { get; } = new AutomationProperty();`

### `src/Avalonia.Controls/Automation/AutomationLiveSetting.cs`
- `public enum AutomationLiveSetting`

### `src/Avalonia.Controls/Automation/AutomationProperties.cs`
- `public enum AccessibilityView`
- `public static class AutomationProperties`
- `public static readonly AttachedProperty<string?> AcceleratorKeyProperty = AvaloniaProperty.RegisterAttached<StyledElement, string?>( "AcceleratorKey", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<AccessibilityView> AccessibilityViewProperty = AvaloniaProperty.RegisterAttached<StyledElement, AccessibilityView>( "AccessibilityView", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<string?> AccessKeyProperty = AvaloniaProperty.RegisterAttached<StyledElement, string?>( "AccessKey", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<string?> AutomationIdProperty = AvaloniaProperty.RegisterAttached<StyledElement, string?>( "AutomationId", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<AutomationControlType?> ControlTypeOverrideProperty = AvaloniaProperty.RegisterAttached<StyledElement, AutomationControlType?>( "ControlTypeOverride", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<string?> HelpTextProperty = AvaloniaProperty.RegisterAttached<StyledElement, string?>( "HelpText", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<AutomationLandmarkType?> LandmarkTypeProperty = AvaloniaProperty.RegisterAttached<StyledElement, AutomationLandmarkType?>( "LandmarkType", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<int> HeadingLevelProperty = AvaloniaProperty.RegisterAttached<StyledElement, int>( "HeadingLevel", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<bool> IsColumnHeaderProperty = AvaloniaProperty.RegisterAttached<StyledElement, bool>( "IsColumnHeader", typeof(AutomationProperties), false);`
- `public static readonly AttachedProperty<bool> IsRequiredForFormProperty = AvaloniaProperty.RegisterAttached<StyledElement, bool>( "IsRequiredForForm", typeof(AutomationProperties), false);`
- `public static readonly AttachedProperty<bool> IsRowHeaderProperty = AvaloniaProperty.RegisterAttached<StyledElement, bool>( "IsRowHeader", typeof(AutomationProperties), false);`
- `public static readonly AttachedProperty<IsOffscreenBehavior> IsOffscreenBehaviorProperty = AvaloniaProperty.RegisterAttached<StyledElement, IsOffscreenBehavior>( "IsOffscreenBehavior", typeof(AutomationProperties), IsOffscreenBehavior.Default);`
- `public static readonly AttachedProperty<string?> ItemStatusProperty = AvaloniaProperty.RegisterAttached<StyledElement, string?>( "ItemStatus", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<string?> ItemTypeProperty = AvaloniaProperty.RegisterAttached<StyledElement, string?>( "ItemType", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<Control> LabeledByProperty = AvaloniaProperty.RegisterAttached<StyledElement, Control>( "LabeledBy", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<AutomationLiveSetting> LiveSettingProperty = AvaloniaProperty.RegisterAttached<StyledElement, AutomationLiveSetting>( "LiveSetting", typeof(AutomationProperties), AutomationLiveSetting.Off);`
- `public static readonly AttachedProperty<string?> NameProperty = AvaloniaProperty.RegisterAttached<StyledElement, string?>( "Name", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<int> PositionInSetProperty = AvaloniaProperty.RegisterAttached<StyledElement, int>( "PositionInSet", typeof(AutomationProperties), AutomationPositionInSetDefault);`
- `public static readonly AttachedProperty<int> SizeOfSetProperty = AvaloniaProperty.RegisterAttached<StyledElement, int>( "SizeOfSet", typeof(AutomationProperties), AutomationSizeOfSetDefault);`
- `public static void SetAcceleratorKey(StyledElement element, string value) {`
- `public static string? GetAcceleratorKey(StyledElement element) {`
- `public static void SetAccessibilityView(StyledElement element, AccessibilityView value) {`
- `public static AccessibilityView GetAccessibilityView(StyledElement element) {`
- `public static void SetAccessKey(StyledElement element, string value) {`
- `public static string? GetAccessKey(StyledElement element) {`
- `public static void SetAutomationId(StyledElement element, string? value) {`
- `public static string? GetAutomationId(StyledElement element) {`
- `public static void SetControlTypeOverride(StyledElement element, AutomationControlType? value) {`
- `public static AutomationControlType? GetControlTypeOverride(StyledElement element) {`
- `public static void SetHelpText(StyledElement element, string? value) {`
- `public static string? GetHelpText(StyledElement element) {`
- `public static void SetLandmarkType(StyledElement element, AutomationLandmarkType? value) {`
- `public static AutomationLandmarkType? GetLandmarkType(StyledElement element) {`
- `public static void SetHeadingLevel(StyledElement element, int value) {`
- `public static int GetHeadingLevel(StyledElement element) {`
- `public static void SetIsColumnHeader(StyledElement element, bool value) {`
- `public static bool GetIsColumnHeader(StyledElement element) {`
- `public static void SetIsRequiredForForm(StyledElement element, bool value) {`
- `public static bool GetIsRequiredForForm(StyledElement element) {`
- `public static bool GetIsRowHeader(StyledElement element) {`
- `public static void SetIsRowHeader(StyledElement element, bool value) {`
- `public static void SetIsOffscreenBehavior(StyledElement element, IsOffscreenBehavior value) {`
- `public static IsOffscreenBehavior GetIsOffscreenBehavior(StyledElement element) {`
- `public static void SetItemStatus(StyledElement element, string? value) {`
- `public static string? GetItemStatus(StyledElement element) {`
- `public static void SetItemType(StyledElement element, string? value) {`
- `public static string? GetItemType(StyledElement element) {`
- `public static void SetLabeledBy(StyledElement element, Control value) {`
- `public static Control GetLabeledBy(StyledElement element) {`
- `public static void SetLiveSetting(StyledElement element, AutomationLiveSetting value) {`
- `public static AutomationLiveSetting GetLiveSetting(StyledElement element) {`
- `public static void SetName(StyledElement element, string? value) {`
- `public static string? GetName(StyledElement element) {`
- `public static void SetPositionInSet(StyledElement element, int value) {`
- `public static int GetPositionInSet(StyledElement element) {`
- `public static void SetSizeOfSet(StyledElement element, int value) {`
- `public static int GetSizeOfSet(StyledElement element) {`

### `src/Avalonia.Controls/Automation/AutomationProperty.cs`
- `public sealed class AutomationProperty`

### `src/Avalonia.Controls/Automation/AutomationPropertyChangedEventArgs.cs`
- `public class AutomationPropertyChangedEventArgs : EventArgs`
- `public AutomationPropertyChangedEventArgs( AutomationProperty property, object? oldValue, object? newValue) {`
- `public AutomationProperty Property { get; }`
- `public object? OldValue { get; }`
- `public object? NewValue { get; }`

### `src/Avalonia.Controls/Automation/ElementNotEnabledException.cs`
- `public class ElementNotEnabledException : Exception`
- `public ElementNotEnabledException() : base("Element not enabled.") { }`
- `public ElementNotEnabledException(string message) : base(message) { }`

### `src/Avalonia.Controls/Automation/ExpandCollapsePatternIdentifiers.cs`
- `public static class ExpandCollapsePatternIdentifiers`
- `public static AutomationProperty ExpandCollapseStateProperty { get; } = new AutomationProperty();`

### `src/Avalonia.Controls/Automation/ExpandCollapseState.cs`
- `public enum ExpandCollapseState`

### `src/Avalonia.Controls/Automation/IsOffscreenBehavior.cs`
- `public enum IsOffscreenBehavior`

### `src/Avalonia.Controls/Automation/Peers/AutomationPeer.cs`
- `public enum AutomationControlType`
- `public enum AutomationLandmarkType`
- `public abstract class AutomationPeer`
- `public void BringIntoView() => BringIntoViewCore();`
- `public string? GetAcceleratorKey() => GetAcceleratorKeyCore();`
- `public string? GetAccessKey() => GetAccessKeyCore();`
- `public AutomationControlType GetAutomationControlType() => GetControlTypeOverrideCore();`
- `public string? GetAutomationId() => GetAutomationIdCore();`
- `public Rect GetBoundingRectangle() => GetBoundingRectangleCore();`
- `public IReadOnlyList<AutomationPeer> GetChildren() => GetOrCreateChildrenCore();`
- `public string GetClassName() => GetClassNameCore() ?? string.Empty;`
- `public AutomationPeer? GetLabeledBy() => GetLabeledByCore();`
- `public string GetLocalizedControlType() => GetLocalizedControlTypeCore();`
- `public string GetName() => GetNameCore() ?? string.Empty;`
- `public string GetHelpText() => GetHelpTextCore() ?? string.Empty;`
- `public AutomationLandmarkType? GetLandmarkType() => GetLandmarkTypeCore();`
- `public int GetHeadingLevel() => GetHeadingLevelCore();`
- `public string? GetItemType() => GetItemTypeCore();`
- `public string? GetItemStatus() => GetItemStatusCore();`
- `public AutomationPeer? GetParent() => GetParentCore();`
- `public AutomationPeer? GetVisualRoot() => GetVisualRootCore();`
- `public bool HasKeyboardFocus() => HasKeyboardFocusCore();`
- `public bool IsContentElement() => IsContentElementOverrideCore();`
- `public bool IsControlElement() => IsControlElementOverrideCore();`
- `public bool IsEnabled() => IsEnabledCore();`
- `public bool IsKeyboardFocusable() => IsKeyboardFocusableCore();`
- `public bool IsOffscreen() => IsOffscreenCore();`
- `public void SetFocus() => SetFocusCore();`
- `public bool ShowContextMenu() => ShowContextMenuCore();`
- `public AutomationLiveSetting GetLiveSetting() => GetLiveSettingCore();`
- `public T? GetProvider<T>() => (T?)GetProviderCore(typeof(T));`
- `public event EventHandler? ChildrenChanged;`
- `public event EventHandler<AutomationPropertyChangedEventArgs>? PropertyChanged;`
- `public void RaisePropertyChangedEvent( AutomationProperty property, object? oldValue, object? newValue) {`

### `src/Avalonia.Controls/Automation/Peers/ButtonAutomationPeer.cs`
- `public class ButtonAutomationPeer : ContentControlAutomationPeer,`
- `public ButtonAutomationPeer(Button owner) : base(owner) {`
- `public new Button Owner => (Button)base.Owner;`
- `public void Invoke() {`

### `src/Avalonia.Controls/Automation/Peers/ComboBoxAutomationPeer.cs`
- `public class ComboBoxAutomationPeer : SelectingItemsControlAutomationPeer,`
- `public ComboBoxAutomationPeer(ComboBox owner) : base(owner) {`
- `public new ComboBox Owner => (ComboBox)base.Owner;`
- `public ExpandCollapseState ExpandCollapseState => ToState(Owner.IsDropDownOpen);`
- `public bool ShowsMenu => true;`
- `public void Collapse() => Owner.IsDropDownOpen = false;`
- `public void Expand() => Owner.IsDropDownOpen = true;`

### `src/Avalonia.Controls/Automation/Peers/ContentControlAutomationPeer.cs`
- `public class ContentControlAutomationPeer : ControlAutomationPeer`
- `public new ContentControl Owner => (ContentControl)base.Owner;`

### `src/Avalonia.Controls/Automation/Peers/ControlAutomationPeer.cs`
- `public class ControlAutomationPeer : AutomationPeer`
- `public ControlAutomationPeer(Control owner) {`
- `public Control Owner { get; }`
- `public AutomationPeer GetOrCreate(Control element) {`
- `public static AutomationPeer CreatePeerForElement(Control element) {`
- `public static AutomationPeer? FromElement(Control element) => element.GetAutomationPeer();`

### `src/Avalonia.Controls/Automation/Peers/DatePickerAutomationPeer.cs`
- Namespace: `Avalonia.Automation.Peers`
- `public class DatePickerAutomationPeer : ControlAutomationPeer, IValueProvider`
- `public DatePickerAutomationPeer(DatePicker owner) : base(owner) {`
- `public bool IsReadOnly => false;`
- `public new DatePicker Owner => (DatePicker)base.Owner;`
- `public string? Value => Owner.SelectedDate?.ToString();`
- `public void SetValue(string? value) {`

### `src/Avalonia.Controls/Automation/Peers/EmbeddableControlRootAutomationPeer.cs`
- `public class EmbeddableControlRootAutomationPeer : ContentControlAutomationPeer, IEmbeddedRootProvider`
- `public EmbeddableControlRootAutomationPeer(EmbeddableControlRoot owner) : base(owner) {`
- `public new EmbeddableControlRoot Owner => (EmbeddableControlRoot)base.Owner;`
- `public event EventHandler? FocusChanged;`
- `public AutomationPeer? GetFocus() => _focus is object ? GetOrCreate(_focus) : null;`
- `public AutomationPeer? GetPeerFromPoint(Point p) {`

### `src/Avalonia.Controls/Automation/Peers/ExpanderAutomationPeer.cs`
- `public class ExpanderAutomationPeer : ControlAutomationPeer,`
- `public ExpanderAutomationPeer(Control owner) : base(owner) {`
- `public new Expander Owner => (Expander)base.Owner;`
- `public ExpandCollapseState ExpandCollapseState => ToState(Owner.IsExpanded);`
- `public bool ShowsMenu => false;`
- `public void Collapse() => Owner.IsExpanded = false;`
- `public void Expand() => Owner.IsExpanded = true;`

### `src/Avalonia.Controls/Automation/Peers/ImageAutomationPeer.cs`
- `public class ImageAutomationPeer : ControlAutomationPeer`
- `public ImageAutomationPeer(Control owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/ItemsControlAutomationPeer.cs`
- `public class ItemsControlAutomationPeer : ControlAutomationPeer, IScrollProvider`
- `public ItemsControlAutomationPeer(ItemsControl owner) : base(owner) {`
- `public new ItemsControl Owner => (ItemsControl)base.Owner;`
- `public bool HorizontallyScrollable => _scroller?.HorizontallyScrollable ?? false;`
- `public double HorizontalScrollPercent => _scroller?.HorizontalScrollPercent ?? -1;`
- `public double HorizontalViewSize => _scroller?.HorizontalViewSize ?? 0;`
- `public bool VerticallyScrollable => _scroller?.VerticallyScrollable ?? false;`
- `public double VerticalScrollPercent => _scroller?.VerticalScrollPercent ?? -1;`
- `public double VerticalViewSize => _scroller?.VerticalViewSize ?? 0;`
- `public void Scroll(ScrollAmount horizontalAmount, ScrollAmount verticalAmount) {`
- `public void SetScrollPercent(double horizontalPercent, double verticalPercent) {`

### `src/Avalonia.Controls/Automation/Peers/LabelAutomationPeer.cs`
- `public class LabelAutomationPeer : ControlAutomationPeer`
- `public LabelAutomationPeer(Label owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/ListItemAutomationPeer.cs`
- `public class ListItemAutomationPeer : ContentControlAutomationPeer,`
- `public ListItemAutomationPeer(ContentControl owner) : base(owner) {`
- `public bool IsSelected => Owner.GetValue(ListBoxItem.IsSelectedProperty);`
- `public ISelectionProvider? SelectionContainer {`
- `public void Select() {`

### `src/Avalonia.Controls/Automation/Peers/MenuItemAutomationPeer.cs`
- `public class MenuItemAutomationPeer : ControlAutomationPeer`
- `public MenuItemAutomationPeer(MenuItem owner) : base(owner) {`
- `public new MenuItem Owner => (MenuItem)base.Owner;`

### `src/Avalonia.Controls/Automation/Peers/NoneAutomationPeer.cs`
- `public class NoneAutomationPeer : ControlAutomationPeer`
- `public NoneAutomationPeer(Control owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/PopupAutomationPeer.cs`
- `public class PopupAutomationPeer : ControlAutomationPeer`
- `public PopupAutomationPeer(Popup owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/PopupRootAutomationPeer.cs`
- `public class PopupRootAutomationPeer : WindowBaseAutomationPeer`
- `public PopupRootAutomationPeer(PopupRoot owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/ProgressBarAutomationPeer.cs`
- `public class ProgressBarAutomationPeer : RangeBaseAutomationPeer, IRangeValueProvider`
- `public ProgressBarAutomationPeer(RangeBase owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/RadioButtonAutomationPeer.cs`
- `public class RadioButtonAutomationPeer : ToggleButtonAutomationPeer, ISelectionItemProvider`
- `public RadioButtonAutomationPeer(RadioButton owner) : base(owner) {`
- `public bool IsSelected => ((RadioButton)Owner).IsChecked == true;`
- `public ISelectionProvider? SelectionContainer => null;`
- `public void AddToSelection() {`
- `public void RemoveFromSelection() {`
- `public void Select() {`

### `src/Avalonia.Controls/Automation/Peers/RangeBaseAutomationPeer.cs`
- `public abstract class RangeBaseAutomationPeer : ControlAutomationPeer, IRangeValueProvider`
- `public RangeBaseAutomationPeer(RangeBase owner) : base(owner) {`
- `public new RangeBase Owner => (RangeBase)base.Owner;`
- `public virtual bool IsReadOnly => false;`
- `public double Maximum => Owner.Maximum;`
- `public double Minimum => Owner.Minimum;`
- `public double Value => Owner.Value;`
- `public double SmallChange => Owner.SmallChange;`
- `public double LargeChange => Owner.LargeChange;`
- `public void SetValue(double value) => Owner.Value = value;`

### `src/Avalonia.Controls/Automation/Peers/ScrollBarAutomationPeer.cs`
- `public class ScrollBarAutomationPeer : RangeBaseAutomationPeer`
- `public ScrollBarAutomationPeer(ScrollBar owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/ScrollViewerAutomationPeer.cs`
- `public class ScrollViewerAutomationPeer : ControlAutomationPeer, IScrollProvider`
- `public ScrollViewerAutomationPeer(ScrollViewer owner) : base(owner) {`
- `public new ScrollViewer Owner => (ScrollViewer)base.Owner;`
- `public bool HorizontallyScrollable {`
- `public double HorizontalScrollPercent {`
- `public double HorizontalViewSize {`
- `public bool VerticallyScrollable {`
- `public double VerticalScrollPercent {`
- `public double VerticalViewSize {`
- `public void Scroll(ScrollAmount horizontalAmount, ScrollAmount verticalAmount) {`
- `public void SetScrollPercent(double horizontalPercent, double verticalPercent) {`

### `src/Avalonia.Controls/Automation/Peers/SelectingItemsControlAutomationPeer.cs`
- `public abstract class SelectingItemsControlAutomationPeer : ItemsControlAutomationPeer,`
- `public bool CanSelectMultiple => GetSelectionModeCore().HasAllFlags(SelectionMode.Multiple);`
- `public bool IsSelectionRequired => GetSelectionModeCore().HasAllFlags(SelectionMode.AlwaysSelected);`
- `public IReadOnlyList<AutomationPeer> GetSelection() => GetSelectionCore() ?? Array.Empty<AutomationPeer>();`

### `src/Avalonia.Controls/Automation/Peers/SliderAutomationPeer.cs`
- `public class SliderAutomationPeer : RangeBaseAutomationPeer`
- `public SliderAutomationPeer(Slider owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/TextBlockAutomationPeer.cs`
- `public class TextBlockAutomationPeer : ControlAutomationPeer`
- `public TextBlockAutomationPeer(TextBlock owner) : base(owner) {`
- `public new TextBlock Owner => (TextBlock)base.Owner;`

### `src/Avalonia.Controls/Automation/Peers/TextBoxAutomationPeer.cs`
- `public class TextBoxAutomationPeer : ControlAutomationPeer, IValueProvider`
- `public TextBoxAutomationPeer(TextBox owner) : base(owner) {`
- `public new TextBox Owner => (TextBox)base.Owner;`
- `public bool IsReadOnly => Owner.IsReadOnly;`
- `public string? Value => Owner.Text;`
- `public void SetValue(string? value) => Owner.Text = value;`

### `src/Avalonia.Controls/Automation/Peers/ThumbAutomationPeer.cs`
- `public class ThumbAutomationPeer : ControlAutomationPeer`
- `public ThumbAutomationPeer(Thumb owner) : base(owner) { }`

### `src/Avalonia.Controls/Automation/Peers/TimePickerAutomationPeer.cs`
- Namespace: `Avalonia.Automation.Peers`
- `public class TimePickerAutomationPeer : ControlAutomationPeer, IValueProvider`
- `public TimePickerAutomationPeer(TimePicker owner) : base(owner) {`
- `public bool IsReadOnly => false;`
- `public new TimePicker Owner => (TimePicker)base.Owner;`
- `public string? Value => Owner.SelectedTime?.ToString();`
- `public void SetValue(string? value) {`

### `src/Avalonia.Controls/Automation/Peers/ToggleButtonAutomationPeer.cs`
- `public class ToggleButtonAutomationPeer : ContentControlAutomationPeer, IToggleProvider`
- `public ToggleButtonAutomationPeer(ToggleButton owner) : base(owner) {`
- `public new ToggleButton Owner => (ToggleButton)base.Owner;`

### `src/Avalonia.Controls/Automation/Peers/TreeViewAutomationPeer.cs`
- Namespace: `Avalonia.Automation.Peers`
- `public class TreeViewAutomationPeer : ItemsControlAutomationPeer`
- `public TreeViewAutomationPeer(TreeView owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/TreeViewItemAutomationPeer.cs`
- Namespace: `Avalonia.Automation.Peers`
- `public class TreeViewItemAutomationPeer : ItemsControlAutomationPeer`
- `public TreeViewItemAutomationPeer(TreeViewItem owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/UnrealizedElementAutomationPeer.cs`
- `public abstract class UnrealizedElementAutomationPeer : AutomationPeer`
- `public void SetParent(AutomationPeer? parent) => TrySetParent(parent);`

### `src/Avalonia.Controls/Automation/Peers/UserControlAutomationPeer.cs`
- Namespace: `Avalonia.Controls.Automation.Peers`
- `public class UserControlAutomationPeer : ControlAutomationPeer`
- `public UserControlAutomationPeer(UserControl owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/WindowAutomationPeer.cs`
- `public class WindowAutomationPeer : WindowBaseAutomationPeer`
- `public WindowAutomationPeer(Window owner) : base(owner) {`
- `public new Window Owner => (Window)base.Owner;`

### `src/Avalonia.Controls/Automation/Peers/WindowBaseAutomationPeer.cs`
- `public class WindowBaseAutomationPeer : ControlAutomationPeer, IRootProvider`
- `public WindowBaseAutomationPeer(WindowBase owner) : base(owner) {`
- `public new WindowBase Owner => (WindowBase)base.Owner;`
- `public ITopLevelImpl? PlatformImpl => Owner.PlatformImpl;`
- `public event EventHandler? FocusChanged;`
- `public AutomationPeer? GetFocus() => _focus is object ? GetOrCreate(_focus) : null;`
- `public AutomationPeer? GetPeerFromPoint(Point p) {`

### `src/Avalonia.Controls/Automation/Provider/IEmbeddedRootProvider.cs`
- `public interface IEmbeddedRootProvider`

### `src/Avalonia.Controls/Automation/Provider/IExpandCollapseProvider.cs`
- `public interface IExpandCollapseProvider`

### `src/Avalonia.Controls/Automation/Provider/IInvokeProvider.cs`
- `public interface IInvokeProvider`

### `src/Avalonia.Controls/Automation/Provider/IRangeValueProvider.cs`
- `public interface IRangeValueProvider`
- `public void SetValue(double value);`

### `src/Avalonia.Controls/Automation/Provider/IRootProvider.cs`
- `public interface IRootProvider`

### `src/Avalonia.Controls/Automation/Provider/IScrollProvider.cs`
- `public enum ScrollAmount`
- `public interface IScrollProvider`

### `src/Avalonia.Controls/Automation/Provider/ISelectionItemProvider .cs`
- `public interface ISelectionItemProvider`

### `src/Avalonia.Controls/Automation/Provider/ISelectionProvider.cs`
- `public interface ISelectionProvider`

### `src/Avalonia.Controls/Automation/Provider/IToggleProvider.cs`
- `public enum ToggleState`
- `public interface IToggleProvider`

### `src/Avalonia.Controls/Automation/Provider/IValueProvider.cs`
- `public interface IValueProvider`
- `public string? Value { get; }`
- `public void SetValue(string? value);`

### `src/Avalonia.Controls/Automation/RangeValuePatternIdentifiers.cs`
- `public static class RangeValuePatternIdentifiers`
- `public static AutomationProperty IsReadOnlyProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty MinimumProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty MaximumProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty ValueProperty { get; } = new AutomationProperty();`

### `src/Avalonia.Controls/Automation/ScrollPatternIdentifiers.cs`
- `public static class ScrollPatternIdentifiers`
- `public const double NoScroll = -1;`
- `public static AutomationProperty HorizontallyScrollableProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty HorizontalScrollPercentProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty HorizontalViewSizeProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty VerticallyScrollableProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty VerticalScrollPercentProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty VerticalViewSizeProperty { get; } = new AutomationProperty();`

### `src/Avalonia.Controls/Automation/SelectionItemPatternIdentifiers.cs`
- `public static class SelectionItemPatternIdentifiers`
- `public static AutomationProperty IsSelectedProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty SelectionContainerProperty { get; } = new AutomationProperty();`

### `src/Avalonia.Controls/Automation/SelectionPatternIdentifiers.cs`
- `public static class SelectionPatternIdentifiers`
- `public static AutomationProperty CanSelectMultipleProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty IsSelectionRequiredProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty SelectionProperty { get; } = new AutomationProperty();`

### `src/Avalonia.Controls/Automation/TogglePatternIdentifiers.cs`
- `public static class TogglePatternIdentifiers`
- `public static AutomationProperty ToggleStateProperty { get; } = new AutomationProperty();`

### `src/Avalonia.Controls/Automation/ValuePatternIdentifiers.cs`
- `public static class ValuePatternIdentifiers`
- `public static AutomationProperty IsReadOnlyProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty ValueProperty { get; } = new AutomationProperty();`

### `src/Avalonia.Controls/Border.cs`
- `public partial class Border : Decorator, IVisualWithRoundRectClip`
- `public static readonly StyledProperty<IBrush?> BackgroundProperty = AvaloniaProperty.Register<Border, IBrush?>(nameof(Background));`
- `public static readonly StyledProperty<BackgroundSizing> BackgroundSizingProperty = AvaloniaProperty.Register<Border, BackgroundSizing>( nameof(BackgroundSizing), BackgroundSizing.CenterBorder);`
- `public static readonly StyledProperty<IBrush?> BorderBrushProperty = AvaloniaProperty.Register<Border, IBrush?>(nameof(BorderBrush));`
- `public static readonly StyledProperty<Thickness> BorderThicknessProperty = AvaloniaProperty.Register<Border, Thickness>(nameof(BorderThickness));`
- `public static readonly StyledProperty<CornerRadius> CornerRadiusProperty = AvaloniaProperty.Register<Border, CornerRadius>(nameof(CornerRadius));`
- `public static readonly StyledProperty<BoxShadows> BoxShadowProperty = AvaloniaProperty.Register<Border, BoxShadows>(nameof(BoxShadow));`
- `public IBrush? Background {`
- `public BackgroundSizing BackgroundSizing {`
- `public IBrush? BorderBrush {`
- `public Thickness BorderThickness {`
- `public CornerRadius CornerRadius {`
- `public BoxShadows BoxShadow {`
- `public sealed override void Render(DrawingContext context) {`
- `public CornerRadius ClipToBoundsRadius => CornerRadius;`

### `src/Avalonia.Controls/Button.cs`
- `public enum ClickMode`
- `public class Button : ContentControl, ICommandSource, IClickableControl`
- `public static readonly StyledProperty<ClickMode> ClickModeProperty = AvaloniaProperty.Register<Button, ClickMode>(nameof(ClickMode));`
- `public static readonly StyledProperty<ICommand?> CommandProperty = AvaloniaProperty.Register<Button, ICommand?>(nameof(Command), enableDataValidation: true);`
- `public static readonly StyledProperty<KeyGesture?> HotKeyProperty = HotKeyManager.HotKeyProperty.AddOwner<Button>();`
- `public static readonly StyledProperty<object?> CommandParameterProperty = AvaloniaProperty.Register<Button, object?>(nameof(CommandParameter));`
- `public static readonly StyledProperty<bool> IsDefaultProperty = AvaloniaProperty.Register<Button, bool>(nameof(IsDefault));`
- `public static readonly StyledProperty<bool> IsCancelProperty = AvaloniaProperty.Register<Button, bool>(nameof(IsCancel));`
- `public static readonly RoutedEvent<RoutedEventArgs> ClickEvent = RoutedEvent.Register<Button, RoutedEventArgs>(nameof(Click), RoutingStrategies.Bubble);`
- `public static readonly DirectProperty<Button, bool> IsPressedProperty = AvaloniaProperty.RegisterDirect<Button, bool>(nameof(IsPressed), b => b.IsPressed);`
- `public static readonly StyledProperty<FlyoutBase?> FlyoutProperty = AvaloniaProperty.Register<Button, FlyoutBase?>(nameof(Flyout));`
- `public Button() {`
- `public event EventHandler<RoutedEventArgs>? Click {`
- `public ClickMode ClickMode {`
- `public ICommand? Command {`
- `public KeyGesture? HotKey {`
- `public object? CommandParameter {`
- `public bool IsDefault {`
- `public bool IsCancel {`
- `public bool IsPressed {`
- `public FlyoutBase? Flyout {`

### `src/Avalonia.Controls/ButtonSpinner.cs`
- `public enum Location`
- `public class ButtonSpinner : Spinner`
- `public static readonly StyledProperty<bool> AllowSpinProperty = AvaloniaProperty.Register<ButtonSpinner, bool>(nameof(AllowSpin), true);`
- `public static readonly StyledProperty<bool> ShowButtonSpinnerProperty = AvaloniaProperty.Register<ButtonSpinner, bool>(nameof(ShowButtonSpinner), true);`
- `public static readonly StyledProperty<Location> ButtonSpinnerLocationProperty = AvaloniaProperty.Register<ButtonSpinner, Location>(nameof(ButtonSpinnerLocation), Location.Right);`
- `public ButtonSpinner() {`
- `public bool AllowSpin {`
- `public bool ShowButtonSpinner {`
- `public Location ButtonSpinnerLocation {`

### `src/Avalonia.Controls/Calendar/Calendar.cs`
- `public enum CalendarMode`
- `public enum CalendarSelectionMode`
- `public class CalendarDateChangedEventArgs : RoutedEventArgs`
- `public DateTime? RemovedDate { get; private set; }`
- `public DateTime? AddedDate { get; private set; }`
- `public class CalendarModeChangedEventArgs : RoutedEventArgs`
- `public CalendarMode OldMode { get; private set; }`
- `public CalendarMode NewMode { get; private set; }`
- `public CalendarModeChangedEventArgs(CalendarMode oldMode, CalendarMode newMode) {`
- `public class Calendar : TemplatedControl`
- `public static readonly StyledProperty<DayOfWeek> FirstDayOfWeekProperty = AvaloniaProperty.Register<Calendar, DayOfWeek>( nameof(FirstDayOfWeek), defaultValue: DateTimeHelper.GetCurrentDateFormat().FirstDayOfWeek);`
- `public DayOfWeek FirstDayOfWeek {`
- `public static readonly StyledProperty<bool> IsTodayHighlightedProperty = AvaloniaProperty.Register<Calendar, bool>( nameof(IsTodayHighlighted), defaultValue: true);`
- `public bool IsTodayHighlighted {`
- `public static readonly StyledProperty<IBrush?> HeaderBackgroundProperty = AvaloniaProperty.Register<Calendar, IBrush?>(nameof(HeaderBackground));`
- `public IBrush? HeaderBackground {`
- `public static readonly StyledProperty<CalendarMode> DisplayModeProperty = AvaloniaProperty.Register<Calendar, CalendarMode>( nameof(DisplayMode), validate: IsValidDisplayMode);`
- `public CalendarMode DisplayMode {`
- `public static readonly StyledProperty<CalendarSelectionMode> SelectionModeProperty = AvaloniaProperty.Register<Calendar, CalendarSelectionMode>( nameof(SelectionMode), defaultValue: CalendarSelectionMode.SingleDate);`
- `public static readonly StyledProperty<bool> AllowTapRangeSelectionProperty = AvaloniaProperty.Register<Calendar, bool>( nameof(AllowTapRangeSelection), defaultValue: true);`
- `public CalendarSelectionMode SelectionMode {`
- `public bool AllowTapRangeSelection {`
- `public static readonly StyledProperty<DateTime?> SelectedDateProperty = AvaloniaProperty.Register<Calendar, DateTime?>(nameof(SelectedDate), defaultBindingMode: BindingMode.TwoWay);`
- `public DateTime? SelectedDate {`
- `public SelectedDatesCollection SelectedDates { get; private set; }`
- `public static readonly StyledProperty<DateTime> DisplayDateProperty = AvaloniaProperty.Register<Calendar, DateTime>(nameof(DisplayDate), defaultBindingMode: BindingMode.TwoWay);`
- `public DateTime DisplayDate {`
- `public static readonly StyledProperty<DateTime?> DisplayDateStartProperty = AvaloniaProperty.Register<Calendar, DateTime?>(nameof(DisplayDateStart), defaultBindingMode: BindingMode.TwoWay);`
- `public DateTime? DisplayDateStart {`
- `public CalendarBlackoutDatesCollection BlackoutDates { get; private set; }`
- `public static readonly StyledProperty<DateTime?> DisplayDateEndProperty = AvaloniaProperty.Register<Calendar, DateTime?>(nameof(DisplayDateEnd), defaultBindingMode: BindingMode.TwoWay);`
- `public DateTime? DisplayDateEnd {`
- `public override string ToString() {`
- `public event EventHandler<SelectionChangedEventArgs>? SelectedDatesChanged;`
- `public event EventHandler<CalendarDateChangedEventArgs>? DisplayDateChanged;`
- `public event EventHandler<CalendarModeChangedEventArgs>? DisplayModeChanged;`
- `public Calendar() {`

### `src/Avalonia.Controls/Calendar/CalendarBlackoutDatesCollection.cs`
- `public sealed class CalendarBlackoutDatesCollection : ObservableCollection<CalendarDateRange>`
- `public CalendarBlackoutDatesCollection(Calendar owner) {`
- `public void AddDatesInPast() {`
- `public bool Contains(DateTime date) {`
- `public bool Contains(DateTime start, DateTime end) {`
- `public bool ContainsAny(CalendarDateRange range) {`

### `src/Avalonia.Controls/Calendar/CalendarButton.cs`
- `public sealed class CalendarButton : Button`
- `public CalendarButton() : base() {`
- `public event EventHandler<PointerPressedEventArgs>? CalendarLeftMouseButtonDown;`
- `public event EventHandler<PointerReleasedEventArgs>? CalendarLeftMouseButtonUp;`

### `src/Avalonia.Controls/Calendar/CalendarDateRange.cs`
- `public sealed class CalendarDateRange`
- `public DateTime Start { get; private set; }`
- `public DateTime End { get; private set; }`
- `public CalendarDateRange(DateTime day) {`
- `public CalendarDateRange(DateTime start, DateTime end) {`

### `src/Avalonia.Controls/Calendar/CalendarDayButton.cs`
- `public sealed class CalendarDayButton : Button`
- `public CalendarDayButton() : base() {`
- `public event EventHandler<PointerPressedEventArgs>? CalendarDayButtonMouseDown;`
- `public event EventHandler<PointerReleasedEventArgs>? CalendarDayButtonMouseUp;`

### `src/Avalonia.Controls/Calendar/CalendarItem.cs`
- `public sealed class CalendarItem : TemplatedControl`
- `public static readonly StyledProperty<IBrush?> HeaderBackgroundProperty = Calendar.HeaderBackgroundProperty.AddOwner<CalendarItem>();`
- `public IBrush? HeaderBackground {`
- `public static readonly StyledProperty<ITemplate<Control>?> DayTitleTemplateProperty = AvaloniaProperty.Register<CalendarItem, ITemplate<Control>?>( nameof(DayTitleTemplate), defaultBindingMode: BindingMode.OneTime);`
- `public ITemplate<Control>? DayTitleTemplate {`

### `src/Avalonia.Controls/Calendar/SelectedDatesCollection.cs`
- `public sealed class SelectedDatesCollection : ObservableCollection<DateTime>`
- `public SelectedDatesCollection(Calendar owner) {`
- `public void AddRange(DateTime start, DateTime end) {`

### `src/Avalonia.Controls/CalendarDatePicker/CalendarDatePicker.Properties.cs`
- `public partial class CalendarDatePicker`
- `public static readonly StyledProperty<DateTime> DisplayDateProperty = AvaloniaProperty.Register<CalendarDatePicker, DateTime>(nameof(DisplayDate));`
- `public static readonly StyledProperty<DateTime?> DisplayDateStartProperty = AvaloniaProperty.Register<CalendarDatePicker, DateTime?>( nameof(DisplayDateStart));`
- `public static readonly StyledProperty<DateTime?> DisplayDateEndProperty = AvaloniaProperty.Register<CalendarDatePicker, DateTime?>( nameof(DisplayDateEnd));`
- `public static readonly StyledProperty<DayOfWeek> FirstDayOfWeekProperty = AvaloniaProperty.Register<CalendarDatePicker, DayOfWeek>(nameof(FirstDayOfWeek));`
- `public static readonly StyledProperty<bool> IsDropDownOpenProperty = AvaloniaProperty.Register<CalendarDatePicker, bool>( nameof(IsDropDownOpen));`
- `public static readonly StyledProperty<bool> IsTodayHighlightedProperty = AvaloniaProperty.Register<CalendarDatePicker, bool>(nameof(IsTodayHighlighted));`
- `public static readonly StyledProperty<DateTime?> SelectedDateProperty = AvaloniaProperty.Register<CalendarDatePicker, DateTime?>( nameof(SelectedDate), enableDataValidation: true, defaultBindingMode:BindingMode.TwoWay);`
- `public static readonly StyledProperty<CalendarDatePickerFormat> SelectedDateFormatProperty = AvaloniaProperty.Register<CalendarDatePicker, CalendarDatePickerFormat>( nameof(SelectedDateFormat), defaultValue: CalendarDatePickerFormat.Short, validate: IsValidSelectedDateFormat);`
- `public static readonly StyledProperty<string> CustomDateFormatStringProperty = AvaloniaProperty.Register<CalendarDatePicker, string>( nameof(CustomDateFormatString), defaultValue: "d", validate: IsValidDateFormatString);`
- `public static readonly StyledProperty<string?> TextProperty = AvaloniaProperty.Register<CalendarDatePicker, string?>(nameof(Text));`
- `public static readonly StyledProperty<string?> WatermarkProperty = TextBox.WatermarkProperty.AddOwner<CalendarDatePicker>();`
- `public static readonly StyledProperty<bool> UseFloatingWatermarkProperty = TextBox.UseFloatingWatermarkProperty.AddOwner<CalendarDatePicker>();`
- `public static readonly StyledProperty<HorizontalAlignment> HorizontalContentAlignmentProperty = ContentControl.HorizontalContentAlignmentProperty.AddOwner<CalendarDatePicker>();`
- `public static readonly StyledProperty<VerticalAlignment> VerticalContentAlignmentProperty = ContentControl.VerticalContentAlignmentProperty.AddOwner<CalendarDatePicker>();`
- `public CalendarBlackoutDatesCollection? BlackoutDates { get; private set; }`
- `public DateTime DisplayDate {`
- `public DateTime? DisplayDateStart {`
- `public DateTime? DisplayDateEnd {`
- `public DayOfWeek FirstDayOfWeek {`
- `public bool IsDropDownOpen {`
- `public bool IsTodayHighlighted {`
- `public DateTime? SelectedDate {`
- `public CalendarDatePickerFormat SelectedDateFormat {`
- `public string CustomDateFormatString {`
- `public string? Text {`
- `public string? Watermark {`
- `public bool UseFloatingWatermark {`
- `public HorizontalAlignment HorizontalContentAlignment {`
- `public VerticalAlignment VerticalContentAlignment {`

### `src/Avalonia.Controls/CalendarDatePicker/CalendarDatePicker.cs`
- `public partial class CalendarDatePicker : TemplatedControl`
- `public event EventHandler? CalendarClosed;`
- `public event EventHandler? CalendarOpened;`
- `public event EventHandler<CalendarDatePickerDateValidationErrorEventArgs>? DateValidationError;`
- `public event EventHandler<SelectionChangedEventArgs>? SelectedDateChanged;`
- `public CalendarDatePicker() {`
- `public void Clear() {`

### `src/Avalonia.Controls/CalendarDatePicker/CalendarDatePickerDateValidationErrorEventArgs.cs`
- `public class CalendarDatePickerDateValidationErrorEventArgs : EventArgs`
- `public CalendarDatePickerDateValidationErrorEventArgs(Exception exception, string text) {`
- `public Exception Exception { get; private set; }`
- `public string Text { get; private set; }`
- `public bool ThrowException {`

### `src/Avalonia.Controls/CalendarDatePicker/CalendarDatePickerFormat.cs`
- `public enum CalendarDatePickerFormat`

### `src/Avalonia.Controls/Canvas.cs`
- `public class Canvas : Panel, INavigableContainer`
- `public static readonly AttachedProperty<double> LeftProperty = AvaloniaProperty.RegisterAttached<Canvas, Control, double>("Left", double.NaN);`
- `public static readonly AttachedProperty<double> TopProperty = AvaloniaProperty.RegisterAttached<Canvas, Control, double>("Top", double.NaN);`
- `public static readonly AttachedProperty<double> RightProperty = AvaloniaProperty.RegisterAttached<Canvas, Control, double>("Right", double.NaN);`
- `public static readonly AttachedProperty<double> BottomProperty = AvaloniaProperty.RegisterAttached<Canvas, Control, double>("Bottom", double.NaN);`
- `public static double GetLeft(AvaloniaObject element) {`
- `public static void SetLeft(AvaloniaObject element, double value) {`
- `public static double GetTop(AvaloniaObject element) {`
- `public static void SetTop(AvaloniaObject element, double value) {`
- `public static double GetRight(AvaloniaObject element) {`
- `public static void SetRight(AvaloniaObject element, double value) {`
- `public static double GetBottom(AvaloniaObject element) {`
- `public static void SetBottom(AvaloniaObject element, double value) {`

### `src/Avalonia.Controls/Carousel.cs`
- `public class Carousel : SelectingItemsControl`
- `public static readonly StyledProperty<IPageTransition?> PageTransitionProperty = AvaloniaProperty.Register<Carousel, IPageTransition?>(nameof(PageTransition));`
- `public IPageTransition? PageTransition {`
- `public void Next() {`
- `public void Previous() {`

### `src/Avalonia.Controls/CheckBox.cs`
- `public class CheckBox : ToggleButton`

### `src/Avalonia.Controls/Chrome/CaptionButtons.cs`
- `public class CaptionButtons : TemplatedControl`
- `public virtual void Attach(Window hostWindow) {`
- `public virtual void Detach() {`

### `src/Avalonia.Controls/Chrome/TitleBar.cs`
- `public class TitleBar : TemplatedControl`

### `src/Avalonia.Controls/ColumnDefinition.cs`
- `public class ColumnDefinition : DefinitionBase`
- `public static readonly StyledProperty<double> MaxWidthProperty = AvaloniaProperty.Register<ColumnDefinition, double>(nameof(MaxWidth), double.PositiveInfinity);`
- `public static readonly StyledProperty<double> MinWidthProperty = AvaloniaProperty.Register<ColumnDefinition, double>(nameof(MinWidth));`
- `public static readonly StyledProperty<GridLength> WidthProperty = AvaloniaProperty.Register<ColumnDefinition, GridLength>(nameof(Width), new GridLength(1, GridUnitType.Star));`
- `public ColumnDefinition() {`
- `public ColumnDefinition(double value, GridUnitType type) : this(new GridLength(value, type)) {`
- `public ColumnDefinition(GridLength width) {`
- `public double ActualWidth => Parent?.GetFinalColumnDefinitionWidth(Index) ?? 0d;`
- `public double MaxWidth {`
- `public double MinWidth {`
- `public GridLength Width {`

### `src/Avalonia.Controls/ColumnDefinitions.cs`
- `public class ColumnDefinitions : DefinitionList<ColumnDefinition>`
- `public ColumnDefinitions() {`
- `public ColumnDefinitions(string s) : this() {`
- `public override string ToString() {`
- `public static ColumnDefinitions Parse(string s) => new ColumnDefinitions(s);`

### `src/Avalonia.Controls/ComboBox.cs`
- `public class ComboBox : SelectingItemsControl`
- `public static readonly StyledProperty<bool> IsDropDownOpenProperty = AvaloniaProperty.Register<ComboBox, bool>(nameof(IsDropDownOpen));`
- `public static readonly StyledProperty<bool> IsEditableProperty = AvaloniaProperty.Register<ComboBox, bool>(nameof(IsEditable));`
- `public static readonly StyledProperty<double> MaxDropDownHeightProperty = AvaloniaProperty.Register<ComboBox, double>(nameof(MaxDropDownHeight), 200);`
- `public static readonly DirectProperty<ComboBox, object?> SelectionBoxItemProperty = AvaloniaProperty.RegisterDirect<ComboBox, object?>(nameof(SelectionBoxItem), o => o.SelectionBoxItem);`
- `public static readonly StyledProperty<string?> PlaceholderTextProperty = AvaloniaProperty.Register<ComboBox, string?>(nameof(PlaceholderText));`
- `public static readonly StyledProperty<IBrush?> PlaceholderForegroundProperty = AvaloniaProperty.Register<ComboBox, IBrush?>(nameof(PlaceholderForeground));`
- `public static readonly StyledProperty<HorizontalAlignment> HorizontalContentAlignmentProperty = ContentControl.HorizontalContentAlignmentProperty.AddOwner<ComboBox>();`
- `public static readonly StyledProperty<VerticalAlignment> VerticalContentAlignmentProperty = ContentControl.VerticalContentAlignmentProperty.AddOwner<ComboBox>();`
- `public static readonly StyledProperty<string?> TextProperty = TextBlock.TextProperty.AddOwner<ComboBox>(new(string.Empty, BindingMode.TwoWay));`
- `public static readonly StyledProperty<IDataTemplate?> SelectionBoxItemTemplateProperty = AvaloniaProperty.Register<ComboBox, IDataTemplate?>( nameof(SelectionBoxItemTemplate), defaultBindingMode: BindingMode.TwoWay, coerce: CoerceSelectionBoxItemTemplate);`
- `public event EventHandler? DropDownClosed;`
- `public event EventHandler? DropDownOpened;`
- `public bool IsDropDownOpen {`
- `public bool IsEditable {`
- `public double MaxDropDownHeight {`
- `public object? SelectionBoxItem {`
- `public string? PlaceholderText {`
- `public IBrush? PlaceholderForeground {`
- `public HorizontalAlignment HorizontalContentAlignment {`
- `public VerticalAlignment VerticalContentAlignment {`
- `public IDataTemplate? SelectionBoxItemTemplate {`
- `public string? Text {`
- `public void Clear() {`

### `src/Avalonia.Controls/ComboBoxItem.cs`
- `public class ComboBoxItem : ListBoxItem`
- `public ComboBoxItem() {`

### `src/Avalonia.Controls/ContainerClearingEventArgs.cs`
- `public class ContainerClearingEventArgs : EventArgs`
- `public ContainerClearingEventArgs(Control container) {`
- `public Control Container { get; }`

### `src/Avalonia.Controls/ContainerIndexChangedEventArgs.cs`
- `public class ContainerIndexChangedEventArgs : EventArgs`
- `public ContainerIndexChangedEventArgs(Control container, int oldIndex, int newIndex) {`
- `public Control Container { get; }`
- `public int NewIndex { get; }`
- `public int OldIndex { get; }`

### `src/Avalonia.Controls/ContainerPreparedEventArgs.cs`
- `public class ContainerPreparedEventArgs : EventArgs`
- `public ContainerPreparedEventArgs(Control container, int index) {`
- `public Control Container { get; }`
- `public int Index { get; }`

### `src/Avalonia.Controls/ContentControl.cs`
- `public class ContentControl : TemplatedControl, IContentControl, IContentPresenterHost`
- `public static readonly StyledProperty<object?> ContentProperty = AvaloniaProperty.Register<ContentControl, object?>(nameof(Content));`
- `public static readonly StyledProperty<IDataTemplate?> ContentTemplateProperty = AvaloniaProperty.Register<ContentControl, IDataTemplate?>(nameof(ContentTemplate));`
- `public static readonly StyledProperty<HorizontalAlignment> HorizontalContentAlignmentProperty = AvaloniaProperty.Register<ContentControl, HorizontalAlignment>(nameof(HorizontalContentAlignment));`
- `public static readonly StyledProperty<VerticalAlignment> VerticalContentAlignmentProperty = AvaloniaProperty.Register<ContentControl, VerticalAlignment>(nameof(VerticalContentAlignment));`
- `public object? Content {`
- `public IDataTemplate? ContentTemplate {`
- `public ContentPresenter? Presenter {`
- `public HorizontalAlignment HorizontalContentAlignment {`
- `public VerticalAlignment VerticalContentAlignment {`

### `src/Avalonia.Controls/ContextMenu.cs`
- `public class ContextMenu : MenuBase, ISetterValue, IPopupHostProvider`
- `public static readonly StyledProperty<double> HorizontalOffsetProperty = Popup.HorizontalOffsetProperty.AddOwner<ContextMenu>();`
- `public static readonly StyledProperty<double> VerticalOffsetProperty = Popup.VerticalOffsetProperty.AddOwner<ContextMenu>();`
- `public static readonly StyledProperty<PopupAnchor> PlacementAnchorProperty = Popup.PlacementAnchorProperty.AddOwner<ContextMenu>();`
- `public static readonly StyledProperty<PopupPositionerConstraintAdjustment> PlacementConstraintAdjustmentProperty = Popup.PlacementConstraintAdjustmentProperty.AddOwner<ContextMenu>();`
- `public static readonly StyledProperty<PopupGravity> PlacementGravityProperty = Popup.PlacementGravityProperty.AddOwner<ContextMenu>();`
- `public static readonly StyledProperty<PlacementMode> PlacementProperty = Popup.PlacementProperty.AddOwner<ContextMenu>();`
- `public static readonly StyledProperty<PlacementMode> PlacementModeProperty = PlacementProperty;`
- `public static readonly StyledProperty<Rect?> PlacementRectProperty = Popup.PlacementRectProperty.AddOwner<ContextMenu>();`
- `public static readonly StyledProperty<bool> WindowManagerAddShadowHintProperty = Popup.WindowManagerAddShadowHintProperty.AddOwner<ContextMenu>();`
- `public static readonly StyledProperty<Control?> PlacementTargetProperty = Popup.PlacementTargetProperty.AddOwner<ContextMenu>();`
- `public static readonly StyledProperty<CustomPopupPlacementCallback?> CustomPopupPlacementCallbackProperty = Popup.CustomPopupPlacementCallbackProperty.AddOwner<ContextMenu>();`
- `public ContextMenu() : this(new DefaultMenuInteractionHandler(true)) {`
- `public ContextMenu(IMenuInteractionHandler interactionHandler) : base(interactionHandler) {`
- `public double HorizontalOffset {`
- `public double VerticalOffset {`
- `public PopupAnchor PlacementAnchor {`
- `public PopupPositionerConstraintAdjustment PlacementConstraintAdjustment {`
- `public PopupGravity PlacementGravity {`
- `public PlacementMode PlacementMode {`
- `public PlacementMode Placement {`
- `public bool WindowManagerAddShadowHint {`
- `public Rect? PlacementRect {`
- `public Control? PlacementTarget {`
- `public CustomPopupPlacementCallback? CustomPopupPlacementCallback {`
- `public event CancelEventHandler? Opening;`
- `public event CancelEventHandler? Closing;`
- `public override void Open() => Open(null);`
- `public void Open(Control? control) {`
- `public override void Close() {`

### `src/Avalonia.Controls/ContextRequestedEventArgs.cs`
- `public class ContextRequestedEventArgs : RoutedEventArgs`
- `public ContextRequestedEventArgs() : base(Control.ContextRequestedEvent) {`
- `public ContextRequestedEventArgs(PointerEventArgs pointerEventArgs) : this() {`
- `public ContextRequestedEventArgs(ContextRequestedEventArgs contextRequestedEventArgs) : this() {`
- `public bool TryGetPosition(Control? relativeTo, out Point point) {`

### `src/Avalonia.Controls/Control.cs`
- `public class Control : InputElement, IDataTemplateHost, IVisualBrushInitialize, ISetterValue`
- `public static readonly StyledProperty<ITemplate<Control>?> FocusAdornerProperty = AvaloniaProperty.Register<Control, ITemplate<Control>?>(nameof(FocusAdorner));`
- `public static readonly StyledProperty<object?> TagProperty = AvaloniaProperty.Register<Control, object?>(nameof(Tag));`
- `public static readonly StyledProperty<ContextMenu?> ContextMenuProperty = AvaloniaProperty.Register<Control, ContextMenu?>(nameof(ContextMenu));`
- `public static readonly StyledProperty<FlyoutBase?> ContextFlyoutProperty = AvaloniaProperty.Register<Control, FlyoutBase?>(nameof(ContextFlyout));`
- `public static readonly RoutedEvent<RequestBringIntoViewEventArgs> RequestBringIntoViewEvent = RoutedEvent.Register<Control, RequestBringIntoViewEventArgs>( "RequestBringIntoView", RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<ContextRequestedEventArgs> ContextRequestedEvent = RoutedEvent.Register<Control, ContextRequestedEventArgs>( nameof(ContextRequested), RoutingStrategies.Tunnel | RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<RoutedEventArgs> LoadedEvent = RoutedEvent.Register<Control, RoutedEventArgs>( nameof(Loaded), RoutingStrategies.Direct);`
- `public static readonly RoutedEvent<RoutedEventArgs> UnloadedEvent = RoutedEvent.Register<Control, RoutedEventArgs>( nameof(Unloaded), RoutingStrategies.Direct);`
- `public static readonly RoutedEvent<SizeChangedEventArgs> SizeChangedEvent = RoutedEvent.Register<Control, SizeChangedEventArgs>( nameof(SizeChanged), RoutingStrategies.Direct);`
- `public ITemplate<Control>? FocusAdorner {`
- `public DataTemplates DataTemplates => _dataTemplates ??= new DataTemplates();`
- `public ContextMenu? ContextMenu {`
- `public FlyoutBase? ContextFlyout {`
- `public bool IsLoaded => _loadState == LoadState.Loaded;`
- `public object? Tag {`
- `public event EventHandler<ContextRequestedEventArgs>? ContextRequested {`
- `public event EventHandler<RoutedEventArgs>? Loaded {`
- `public event EventHandler<RoutedEventArgs>? Unloaded {`
- `public event EventHandler<SizeChangedEventArgs>? SizeChanged {`

### `src/Avalonia.Controls/ControlExtensions.cs`
- `public static class ControlExtensions`
- `public static void BringIntoView(this Control control) {`
- `public static void BringIntoView(this Control control, Rect rect) {`
- `public static T? FindControl<T>(this Control control, string name) where T : Control {`
- `public static T GetControl<T>(this Control control, string name) where T : Control {`
- `public static IDisposable Set(this IPseudoClasses classes, string name, IObservable<bool> trigger) {`

### `src/Avalonia.Controls/Controls.cs`
- `public class Controls : AvaloniaList<Control>, IAvaloniaListItemValidator<Control>`
- `public Controls() {`
- `public Controls(IEnumerable<Control> items) {`

### `src/Avalonia.Controls/Converters/CornerRadiusFilterConverter.cs`
- `public class CornerRadiusFilterConverter : IValueConverter`
- `public Corners Filter { get; set; }`
- `public double Scale { get; set; } = 1;`
- `public object? Convert( object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public object? ConvertBack( object? value, Type targetType, object? parameter, CultureInfo culture) {`

### `src/Avalonia.Controls/Converters/CornerRadiusToDoubleConverter.cs`
- `public class CornerRadiusToDoubleConverter : IValueConverter`
- `public Corners Corner { get; set; }`
- `public object? Convert(object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public object? ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture) {`

### `src/Avalonia.Controls/Converters/Corners.cs`
- `public enum Corners`

### `src/Avalonia.Controls/Converters/EnumToBoolConverter.cs`
- `public class EnumToBoolConverter : IValueConverter`
- `public object? Convert( object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public object? ConvertBack( object? value, Type targetType, object? parameter, CultureInfo culture) {`

### `src/Avalonia.Controls/Converters/MarginMultiplierConverter.cs`
- `public class MarginMultiplierConverter : IValueConverter`
- `public double Indent { get; set; }`
- `public bool Left { get; set; } = false;`
- `public bool Top { get; set; } = false;`
- `public bool Right { get; set; } = false;`
- `public bool Bottom { get; set; } = false;`
- `public object? Convert(object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public object? ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture) {`

### `src/Avalonia.Controls/Converters/MenuScrollingVisibilityConverter.cs`
- `public class MenuScrollingVisibilityConverter : IMultiValueConverter`
- `public static readonly MenuScrollingVisibilityConverter Instance = new MenuScrollingVisibilityConverter();`
- `public object? Convert(IList<object?> values, Type targetType, object? parameter, CultureInfo culture) {`

### `src/Avalonia.Controls/Converters/PlatformKeyGestureConverter.cs`
- `public class PlatformKeyGestureConverter : IValueConverter`
- `public object? Convert(object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public object? ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public static string ToPlatformString(KeyGesture gesture) => gesture.ToString("p", null);`

### `src/Avalonia.Controls/Converters/StringFormatConverter.cs`
- Namespace: `Avalonia.Controls.Converters`
- `public class StringFormatConverter : IMultiValueConverter`
- `public object? Convert(IList<object?> values, Type targetType, object? parameter, CultureInfo culture) {`

### `src/Avalonia.Controls/DataValidationErrors.cs`
- `public class DataValidationErrors : ContentControl`
- `public static readonly AttachedProperty<IEnumerable<object>?> ErrorsProperty = AvaloniaProperty.RegisterAttached<DataValidationErrors, Control, IEnumerable<object>?>("Errors");`
- `public static readonly AttachedProperty<bool> HasErrorsProperty = AvaloniaProperty.RegisterAttached<DataValidationErrors, Control, bool>("HasErrors");`
- `public static readonly AttachedProperty<Func<object, object>?> ErrorConverterProperty = AvaloniaProperty.RegisterAttached<DataValidationErrors, Control, Func<object, object>?>("ErrorConverter");`
- `public static readonly StyledProperty<IDataTemplate> ErrorTemplateProperty = AvaloniaProperty.Register<DataValidationErrors, IDataTemplate>(nameof(ErrorTemplate));`
- `public static readonly DirectProperty<DataValidationErrors, Control?> OwnerProperty = AvaloniaProperty.RegisterDirect<DataValidationErrors, Control?>( nameof(Owner), o => o.Owner,`
- `public Control? Owner {`
- `public IDataTemplate ErrorTemplate {`
- `public static IEnumerable<object>? GetErrors(Control control) {`
- `public static void SetErrors(Control control, IEnumerable<object>? errors) {`
- `public static void SetError(Control control, Exception? error) {`
- `public static void ClearErrors(Control control) {`
- `public static bool GetHasErrors(Control control) {`
- `public static Func<object, object?>? GetErrorConverter(Control control) {`
- `public static void SetErrorConverter(Control control, Func<object, object>? converter) {`

### `src/Avalonia.Controls/DateTimePickers/DatePicker.cs`
- `public class DatePicker : TemplatedControl`
- `public static readonly StyledProperty<string> DayFormatProperty = AvaloniaProperty.Register<DatePicker, string>(nameof(DayFormat), "%d");`
- `public static readonly StyledProperty<bool> DayVisibleProperty = AvaloniaProperty.Register<DatePicker, bool>(nameof(DayVisible), true);`
- `public static readonly StyledProperty<DateTimeOffset> MaxYearProperty = AvaloniaProperty.Register<DatePicker, DateTimeOffset>(nameof(MaxYear), DateTimeOffset.MaxValue, coerce: CoerceMaxYear);`
- `public static readonly StyledProperty<DateTimeOffset> MinYearProperty = AvaloniaProperty.Register<DatePicker, DateTimeOffset>(nameof(MinYear), DateTimeOffset.MinValue, coerce: CoerceMinYear);`
- `public static readonly StyledProperty<string> MonthFormatProperty = AvaloniaProperty.Register<DatePicker, string>(nameof(MonthFormat), "MMMM");`
- `public static readonly StyledProperty<bool> MonthVisibleProperty = AvaloniaProperty.Register<DatePicker, bool>(nameof(MonthVisible), true);`
- `public static readonly StyledProperty<string> YearFormatProperty = AvaloniaProperty.Register<DatePicker, string>(nameof(YearFormat), "yyyy");`
- `public static readonly StyledProperty<bool> YearVisibleProperty = AvaloniaProperty.Register<DatePicker, bool>(nameof(YearVisible), true);`
- `public static readonly StyledProperty<DateTimeOffset?> SelectedDateProperty = AvaloniaProperty.Register<DatePicker, DateTimeOffset?>(nameof(SelectedDate), defaultBindingMode: BindingMode.TwoWay, enableDataValidation: true);`
- `public DatePicker() {`
- `public string DayFormat {`
- `public bool DayVisible {`
- `public DateTimeOffset MaxYear {`
- `public DateTimeOffset MinYear {`
- `public string MonthFormat {`
- `public bool MonthVisible {`
- `public string YearFormat {`
- `public bool YearVisible {`
- `public DateTimeOffset? SelectedDate {`
- `public event EventHandler<DatePickerSelectedValueChangedEventArgs>? SelectedDateChanged;`
- `public void Clear() {`

### `src/Avalonia.Controls/DateTimePickers/DatePickerPresenter.cs`
- `public class DatePickerPresenter : PickerPresenterBase`
- `public static readonly StyledProperty<DateTimeOffset> DateProperty = AvaloniaProperty.Register<DatePickerPresenter, DateTimeOffset>(nameof(Date), coerce: CoerceDate);`
- `public static readonly StyledProperty<string> DayFormatProperty = DatePicker.DayFormatProperty.AddOwner<DatePickerPresenter>();`
- `public static readonly StyledProperty<bool> DayVisibleProperty = DatePicker.DayVisibleProperty.AddOwner<DatePickerPresenter>();`
- `public static readonly StyledProperty<DateTimeOffset> MaxYearProperty = DatePicker.MaxYearProperty.AddOwner<DatePickerPresenter>();`
- `public static readonly StyledProperty<DateTimeOffset> MinYearProperty = DatePicker.MinYearProperty.AddOwner<DatePickerPresenter>();`
- `public static readonly StyledProperty<string> MonthFormatProperty = DatePicker.MonthFormatProperty.AddOwner<DatePickerPresenter>();`
- `public static readonly StyledProperty<bool> MonthVisibleProperty = DatePicker.MonthVisibleProperty.AddOwner<DatePickerPresenter>();`
- `public static readonly StyledProperty<string> YearFormatProperty = DatePicker.YearFormatProperty.AddOwner<DatePickerPresenter>();`
- `public static readonly StyledProperty<bool> YearVisibleProperty = DatePicker.YearVisibleProperty.AddOwner<DatePickerPresenter>();`
- `public DatePickerPresenter() {`
- `public DateTimeOffset Date {`
- `public string DayFormat {`
- `public bool DayVisible {`
- `public DateTimeOffset MaxYear {`
- `public DateTimeOffset MinYear {`
- `public string MonthFormat {`
- `public bool MonthVisible {`
- `public string YearFormat {`
- `public bool YearVisible {`

### `src/Avalonia.Controls/DateTimePickers/DatePickerSelectedValueChangedEventArgs.cs`
- `public class DatePickerSelectedValueChangedEventArgs`
- `public DateTimeOffset? NewDate { get; }`
- `public DateTimeOffset? OldDate { get; }`
- `public DatePickerSelectedValueChangedEventArgs(DateTimeOffset? oldDate, DateTimeOffset? newDate) {`

### `src/Avalonia.Controls/DateTimePickers/DateTimePickerPanel.cs`
- `public enum DateTimePickerPanelType`
- `public class DateTimePickerPanel : Panel, ILogicalScrollable`
- `public static readonly StyledProperty<double> ItemHeightProperty = AvaloniaProperty.Register<DateTimePickerPanel, double>(nameof(ItemHeight), 40.0);`
- `public static readonly StyledProperty<DateTimePickerPanelType> PanelTypeProperty = AvaloniaProperty.Register<DateTimePickerPanel, DateTimePickerPanelType>(nameof(PanelType));`
- `public static readonly StyledProperty<string> ItemFormatProperty = AvaloniaProperty.Register<DateTimePickerPanel, string>(nameof(ItemFormat), "yyyy");`
- `public static readonly StyledProperty<bool> ShouldLoopProperty = AvaloniaProperty.Register<DateTimePickerPanel, bool>(nameof(ShouldLoop));`
- `public DateTimePickerPanel() {`
- `public DateTimePickerPanelType PanelType {`
- `public double ItemHeight {`
- `public string ItemFormat {`
- `public bool ShouldLoop {`
- `public int MinimumValue {`
- `public int MaximumValue {`
- `public int SelectedValue {`
- `public int Increment {`
- `public Vector Offset {`
- `public bool CanHorizontallyScroll { get => false; set { } }`
- `public bool CanVerticallyScroll { get => true; set { } }`
- `public bool IsLogicalScrollEnabled => true;`
- `public Size ScrollSize => new Size(0, ItemHeight);`
- `public Size PageScrollSize => new Size(0, ItemHeight * 4);`
- `public Size Extent => _extent;`
- `public Size Viewport => Bounds.Size;`
- `public event EventHandler? ScrollInvalidated;`
- `public event EventHandler? SelectionChanged;`
- `public void RefreshItems() {`
- `public void ScrollUp(int numItems = 1) {`
- `public void ScrollDown(int numItems = 1) {`
- `public bool BringIntoView(Control target, Rect targetRect) { return false; }`
- `public Control? GetControlInDirection(NavigationDirection direction, Control? from) { return null; }`
- `public void RaiseScrollInvalidated(EventArgs e) {`

### `src/Avalonia.Controls/DateTimePickers/PickerPresenterBase.cs`
- `public abstract class PickerPresenterBase : TemplatedControl`
- `public event EventHandler? Confirmed;`
- `public event EventHandler? Dismissed;`

### `src/Avalonia.Controls/DateTimePickers/TimePicker.cs`
- `public class TimePicker : TemplatedControl`
- `public static readonly StyledProperty<int> MinuteIncrementProperty = AvaloniaProperty.Register<TimePicker, int>(nameof(MinuteIncrement), 1, coerce: CoerceMinuteIncrement);`
- `public static readonly StyledProperty<int> SecondIncrementProperty = AvaloniaProperty.Register<TimePicker, int>(nameof(SecondIncrement), 1, coerce: CoerceSecondIncrement);`
- `public static readonly StyledProperty<string> ClockIdentifierProperty = AvaloniaProperty.Register<TimePicker, string>(nameof(ClockIdentifier), "12HourClock", coerce: CoerceClockIdentifier);`
- `public static readonly StyledProperty<bool> UseSecondsProperty = AvaloniaProperty.Register<TimePicker, bool>(nameof(UseSeconds), false, coerce: CoerceUseSeconds);`
- `public static readonly StyledProperty<TimeSpan?> SelectedTimeProperty = AvaloniaProperty.Register<TimePicker, TimeSpan?>(nameof(SelectedTime), defaultBindingMode: BindingMode.TwoWay, enableDataValidation: true);`
- `public TimePicker() {`
- `public int MinuteIncrement {`
- `public int SecondIncrement {`
- `public string ClockIdentifier {`
- `public bool UseSeconds {`
- `public TimeSpan? SelectedTime {`
- `public event EventHandler<TimePickerSelectedValueChangedEventArgs>? SelectedTimeChanged;`
- `public void Clear() {`

### `src/Avalonia.Controls/DateTimePickers/TimePickerPresenter.cs`
- `public class TimePickerPresenter : PickerPresenterBase`
- `public static readonly StyledProperty<int> MinuteIncrementProperty = TimePicker.MinuteIncrementProperty.AddOwner<TimePickerPresenter>();`
- `public static readonly StyledProperty<int> SecondIncrementProperty = TimePicker.SecondIncrementProperty.AddOwner<TimePickerPresenter>();`
- `public static readonly StyledProperty<string> ClockIdentifierProperty = TimePicker.ClockIdentifierProperty.AddOwner<TimePickerPresenter>();`
- `public static readonly StyledProperty<bool> UseSecondsProperty = TimePicker.UseSecondsProperty.AddOwner<TimePickerPresenter>();`
- `public static readonly StyledProperty<TimeSpan> TimeProperty = AvaloniaProperty.Register<TimePickerPresenter, TimeSpan>(nameof(Time));`
- `public TimePickerPresenter() {`
- `public int MinuteIncrement {`
- `public int SecondIncrement {`
- `public string ClockIdentifier {`
- `public bool UseSeconds {`
- `public TimeSpan Time {`

### `src/Avalonia.Controls/DateTimePickers/TimePickerSelectedValueChangedEventArgs.cs`
- `public class TimePickerSelectedValueChangedEventArgs`
- `public TimeSpan? OldTime { get; }`
- `public TimeSpan? NewTime { get; }`
- `public TimePickerSelectedValueChangedEventArgs(TimeSpan? old, TimeSpan? newT) {`

### `src/Avalonia.Controls/Decorator.cs`
- `public class Decorator : Control`
- `public static readonly StyledProperty<Control?> ChildProperty = AvaloniaProperty.Register<Decorator, Control?>(nameof(Child));`
- `public static readonly StyledProperty<Thickness> PaddingProperty = AvaloniaProperty.Register<Decorator, Thickness>(nameof(Padding));`
- `public Control? Child {`
- `public Thickness Padding {`

### `src/Avalonia.Controls/DefinitionBase.cs`
- `public abstract class DefinitionBase : AvaloniaObject`
- `public string? SharedSizeGroup {`
- `public static readonly AttachedProperty<string?> SharedSizeGroupProperty = AvaloniaProperty.RegisterAttached<DefinitionBase, Control, string?>( "SharedSizeGroup", validate: SharedSizeGroupPropertyValueValid);`

### `src/Avalonia.Controls/DefinitionList.cs`
- `public abstract class DefinitionList<T> : AvaloniaList<T> where T : DefinitionBase`
- `public DefinitionList() {`

### `src/Avalonia.Controls/Design.cs`
- `public static class Design`
- `public static bool IsDesignMode { get; internal set; }`
- `public static readonly AttachedProperty<double> HeightProperty = AvaloniaProperty .RegisterAttached<Control, double>("Height", typeof (Design));`
- `public static void SetHeight(Control control, double value) {`
- `public static double GetHeight(Control control) {`
- `public static readonly AttachedProperty<double> WidthProperty = AvaloniaProperty .RegisterAttached<Control, double>("Width", typeof(Design));`
- `public static void SetWidth(Control control, double value) {`
- `public static double GetWidth(Control control) {`
- `public static readonly AttachedProperty<object> DataContextProperty = AvaloniaProperty .RegisterAttached<Control, object>("DataContext", typeof (Design));`
- `public static void SetDataContext(Control control, object value) {`
- `public static object GetDataContext(Control control) {`
- `public static readonly AttachedProperty<Control?> PreviewWithProperty = AvaloniaProperty .RegisterAttached<AvaloniaObject, Control?>("PreviewWith", typeof (Design));`
- `public static void SetPreviewWith(AvaloniaObject target, Control? control) {`
- `public static void SetPreviewWith(ResourceDictionary target, Control? control) {`
- `public static Control? GetPreviewWith(AvaloniaObject target) {`
- `public static Control? GetPreviewWith(ResourceDictionary target) {`
- `public static readonly AttachedProperty<IStyle> DesignStyleProperty = AvaloniaProperty .RegisterAttached<Control, IStyle>("DesignStyle", typeof(Design));`
- `public static void SetDesignStyle(Control control, IStyle value) {`
- `public static IStyle GetDesignStyle(Control control) {`
- `public static void ApplyDesignModeProperties(Control target, Control source) {`

### `src/Avalonia.Controls/DesktopApplicationExtensions.cs`
- `public static class DesktopApplicationExtensions`
- `public static void Run(this Application app, ICloseable closable) {`
- `public static void Run(this Application app, Window mainWindow) {`
- `public static void Run(this Application app, CancellationToken token) {`
- `public static void RunWithMainWindow<TWindow>(this Application app) where TWindow : Avalonia.Controls.Window, new() {`

### `src/Avalonia.Controls/Diagnostics/IPopupHostProvider.cs`
- `public interface IPopupHostProvider`

### `src/Avalonia.Controls/Diagnostics/ToolTipDiagnostics.cs`
- `public static class ToolTipDiagnostics`
- `public static readonly AvaloniaProperty<ToolTip?> ToolTipProperty = ToolTip.ToolTipProperty;`

### `src/Avalonia.Controls/DockPanel.cs`
- `public enum Dock`
- `public class DockPanel : Panel`
- `public static readonly AttachedProperty<Dock> DockProperty = AvaloniaProperty.RegisterAttached<DockPanel, Control, Dock>("Dock");`
- `public static readonly StyledProperty<bool> LastChildFillProperty = AvaloniaProperty.Register<DockPanel, bool>( nameof(LastChildFill), defaultValue: true);`
- `public static readonly StyledProperty<double> HorizontalSpacingProperty = AvaloniaProperty.Register<DockPanel, double>( nameof(HorizontalSpacing));`
- `public static readonly StyledProperty<double> VerticalSpacingProperty = AvaloniaProperty.Register<DockPanel, double>( nameof(VerticalSpacing));`
- `public static Dock GetDock(Control control) {`
- `public static void SetDock(Control control, Dock value) {`
- `public bool LastChildFill {`
- `public double HorizontalSpacing {`
- `public double VerticalSpacing {`

### `src/Avalonia.Controls/Documents/Bold.cs`
- `public sealed class Bold : Span`
- `public Bold() {`

### `src/Avalonia.Controls/Documents/Inline.cs`
- `public abstract class Inline : TextElement`
- `public static readonly StyledProperty<TextDecorationCollection?> TextDecorationsProperty = AvaloniaProperty.RegisterAttached<Inline, Inline, TextDecorationCollection?>( nameof(TextDecorations), inherits: true);`
- `public static readonly StyledProperty<BaselineAlignment> BaselineAlignmentProperty = AvaloniaProperty.Register<Inline, BaselineAlignment>( nameof(BaselineAlignment), BaselineAlignment.Baseline);`
- `public TextDecorationCollection? TextDecorations {`
- `public BaselineAlignment BaselineAlignment {`
- `public static TextDecorationCollection? GetTextDecorations(Control control) {`
- `public static void SetTextDecorations(Control control, TextDecorationCollection? value) {`

### `src/Avalonia.Controls/Documents/InlineCollection.cs`
- `public class InlineCollection : AvaloniaList<Inline>`
- `public InlineCollection() {`
- `public string? Text {`
- `public override void Add(Inline inline) {`
- `public void Add(string text) {`
- `public void Add(Control control) {`
- `public event EventHandler? Invalidated;`

### `src/Avalonia.Controls/Documents/InlineUIContainer.cs`
- `public class InlineUIContainer : Inline`
- `public static readonly StyledProperty<Control> ChildProperty = AvaloniaProperty.Register<InlineUIContainer, Control>(nameof(Child));`
- `public InlineUIContainer() {`
- `public InlineUIContainer(Control child) {`
- `public Control Child {`

### `src/Avalonia.Controls/Documents/Italic.cs`
- `public sealed class Italic : Span`
- `public Italic() {`

### `src/Avalonia.Controls/Documents/LineBreak.cs`
- `public class LineBreak : Inline`
- `public LineBreak() {`

### `src/Avalonia.Controls/Documents/Run.cs`
- `public class Run : Inline`
- `public Run() {`
- `public Run(string? text) {`
- `public static readonly StyledProperty<string?> TextProperty = AvaloniaProperty.Register<Run, string?> ( nameof (Text), defaultBindingMode: BindingMode.TwoWay);`
- `public string? Text {`

### `src/Avalonia.Controls/Documents/Span.cs`
- `public class Span : Inline, IAddChild<Inline>, IAddChild<Control>, IAddChild<string>`
- `public static readonly StyledProperty<InlineCollection> InlinesProperty = AvaloniaProperty.Register<Span, InlineCollection>( nameof(Inlines));`
- `public Span() {`
- `public InlineCollection Inlines {`

### `src/Avalonia.Controls/Documents/TextElement.cs`
- `public abstract class TextElement : StyledElement`
- `public static readonly StyledProperty<IBrush?> BackgroundProperty = Border.BackgroundProperty.AddOwner<TextElement>();`
- `public static readonly AttachedProperty<FontFamily> FontFamilyProperty = AvaloniaProperty.RegisterAttached<TextElement, TextElement, FontFamily>( nameof(FontFamily), defaultValue: FontFamily.Default, inherits: true);`
- `public static readonly AttachedProperty<FontFeatureCollection?> FontFeaturesProperty = AvaloniaProperty.RegisterAttached<TextElement, TextElement, FontFeatureCollection?>( nameof(FontFeatures), inherits: true);`
- `public static readonly AttachedProperty<double> FontSizeProperty = AvaloniaProperty.RegisterAttached<TextElement, TextElement, double>( nameof(FontSize), defaultValue: 12, inherits: true, validate: fontSize => fontSize > 0 && !double.IsNaN(fontSize) && !double.IsInfinity(fontSize));`
- `public static readonly AttachedProperty<FontStyle> FontStyleProperty = AvaloniaProperty.RegisterAttached<TextElement, TextElement, FontStyle>( nameof(FontStyle), inherits: true);`
- `public static readonly AttachedProperty<FontWeight> FontWeightProperty = AvaloniaProperty.RegisterAttached<TextElement, TextElement, FontWeight>( nameof(FontWeight), inherits: true, defaultValue: FontWeight.Normal);`
- `public static readonly AttachedProperty<FontStretch> FontStretchProperty = AvaloniaProperty.RegisterAttached<TextElement, TextElement, FontStretch>( nameof(FontStretch), inherits: true, defaultValue: FontStretch.Normal);`
- `public static readonly AttachedProperty<IBrush?> ForegroundProperty = AvaloniaProperty.RegisterAttached<TextElement, TextElement, IBrush?>( nameof(Foreground), Brushes.Black, inherits: true);`
- `public IBrush? Background {`
- `public FontFamily FontFamily {`
- `public FontFeatureCollection? FontFeatures {`
- `public double FontSize {`
- `public FontStyle FontStyle {`
- `public FontWeight FontWeight {`
- `public FontStretch FontStretch {`
- `public IBrush? Foreground {`
- `public static FontFamily GetFontFamily(Control control) {`
- `public static void SetFontFamily(Control control, FontFamily value) {`
- `public static FontFeatureCollection? GetFontFeatures(Control control) {`
- `public static void SetFontFeatures(Control control, FontFeatureCollection? value) {`
- `public static double GetFontSize(Control control) {`
- `public static void SetFontSize(Control control, double value) {`
- `public static FontStyle GetFontStyle(Control control) {`
- `public static void SetFontStyle(Control control, FontStyle value) {`
- `public static FontWeight GetFontWeight(Control control) {`
- `public static void SetFontWeight(Control control, FontWeight value) {`
- `public static FontStretch GetFontStretch(Control control) {`
- `public static void SetFontStretch(Control control, FontStretch value) {`
- `public static IBrush? GetForeground(Control control) {`
- `public static void SetForeground(Control control, IBrush? value) {`

### `src/Avalonia.Controls/Documents/Underline.cs`
- `public sealed class Underline : Span`
- `public Underline() {`

### `src/Avalonia.Controls/DropDownButton.cs`
- `public class DropDownButton : Button`
- `public DropDownButton() {`

### `src/Avalonia.Controls/Embedding/EmbeddableControlRoot.cs`
- `public class EmbeddableControlRoot : TopLevel, IFocusScope, IDisposable`
- `public EmbeddableControlRoot(ITopLevelImpl impl) : base(impl) {`
- `public EmbeddableControlRoot() : base(PlatformManager.CreateEmbeddableTopLevel()) {`
- `public void Prepare() {`
- `public new void StartRendering() => base.StartRendering();`
- `public new void StopRendering() => base.StopRendering();`
- `public void Dispose() {`

### `src/Avalonia.Controls/Embedding/Offscreen/OffscreenTopLevelImpl.cs`
- `public abstract class OffscreenTopLevelImplBase : ITopLevelImpl`
- `public IInputRoot? InputRoot { get; private set; }`
- `public bool IsDisposed { get; private set; }`
- `public virtual void Dispose() {`
- `public Compositor Compositor { get; }`
- `public OffscreenTopLevelImplBase() => Compositor = new Compositor(null);`
- `public abstract IEnumerable<object> Surfaces { get; }`
- `public virtual double DesktopScaling => _scaling;`
- `public IPlatformHandle? Handle { get; }`
- `public Size ClientSize {`
- `public Size? FrameSize => null;`
- `public double RenderScaling {`
- `public Action<RawInputEventArgs>? Input { get; set; }`
- `public Action<Rect>? Paint { get; set; }`
- `public Action<Size, WindowResizeReason>? Resized { get; set; }`
- `public Action<double>? ScalingChanged { get; set; }`
- `public Action<WindowTransparencyLevel>? TransparencyLevelChanged { get; set; }`
- `public void SetFrameThemeVariant(PlatformThemeVariant themeVariant) { }`
- `public AcrylicPlatformCompensationLevels AcrylicCompensationLevels { get; } = new AcrylicPlatformCompensationLevels(1, 1, 1);`
- `public void SetInputRoot(IInputRoot inputRoot) => InputRoot = inputRoot;`
- `public virtual Point PointToClient(PixelPoint point) => point.ToPoint(1);`
- `public virtual PixelPoint PointToScreen(Point point) => PixelPoint.FromPoint(point, 1);`
- `public virtual void SetCursor(ICursorImpl? cursor) {`
- `public Action? Closed { get; set; }`
- `public Action? LostFocus { get; set; }`
- `public abstract IMouseDevice MouseDevice { get; }`
- `public void SetTransparencyLevelHint(IReadOnlyList<WindowTransparencyLevel> transparencyLevel) { }`
- `public WindowTransparencyLevel TransparencyLevel => WindowTransparencyLevel.None;`
- `public IPopupImpl? CreatePopup() => null;`
- `public virtual object? TryGetFeature(Type featureType) => null;`

### `src/Avalonia.Controls/Expander.cs`
- `public enum ExpandDirection`
- `public class Expander : HeaderedContentControl`
- `public static readonly StyledProperty<IPageTransition?> ContentTransitionProperty = AvaloniaProperty.Register<Expander, IPageTransition?>( nameof(ContentTransition));`
- `public static readonly StyledProperty<ExpandDirection> ExpandDirectionProperty = AvaloniaProperty.Register<Expander, ExpandDirection>( nameof(ExpandDirection), ExpandDirection.Down);`
- `public static readonly StyledProperty<bool> IsExpandedProperty = AvaloniaProperty.Register<Expander, bool>( nameof(IsExpanded), defaultBindingMode: BindingMode.TwoWay, coerce: CoerceIsExpanded);`
- `public static readonly RoutedEvent<RoutedEventArgs> CollapsedEvent = RoutedEvent.Register<Expander, RoutedEventArgs>( nameof(Collapsed), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<CancelRoutedEventArgs> CollapsingEvent = RoutedEvent.Register<Expander, CancelRoutedEventArgs>( nameof(Collapsing), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<RoutedEventArgs> ExpandedEvent = RoutedEvent.Register<Expander, RoutedEventArgs>( nameof(Expanded), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<CancelRoutedEventArgs> ExpandingEvent = RoutedEvent.Register<Expander, CancelRoutedEventArgs>( nameof(Expanding), RoutingStrategies.Bubble);`
- `public Expander() {`
- `public IPageTransition? ContentTransition {`
- `public ExpandDirection ExpandDirection {`
- `public bool IsExpanded {`
- `public event EventHandler<RoutedEventArgs>? Collapsed {`
- `public event EventHandler<CancelRoutedEventArgs>? Collapsing {`
- `public event EventHandler<RoutedEventArgs>? Expanded {`
- `public event EventHandler<CancelRoutedEventArgs>? Expanding {`

### `src/Avalonia.Controls/ExperimentalAcrylicBorder.cs`
- `public class ExperimentalAcrylicBorder : Decorator`
- `public static readonly StyledProperty<CornerRadius> CornerRadiusProperty = Border.CornerRadiusProperty.AddOwner<ExperimentalAcrylicBorder>();`
- `public static readonly StyledProperty<ExperimentalAcrylicMaterial> MaterialProperty = AvaloniaProperty.Register<ExperimentalAcrylicBorder, ExperimentalAcrylicMaterial>(nameof(Material));`
- `public CornerRadius CornerRadius {`
- `public ExperimentalAcrylicMaterial Material {`

### `src/Avalonia.Controls/Flyouts/Flyout.cs`
- `public class Flyout : PopupFlyoutBase`
- `public static readonly StyledProperty<object?> ContentProperty = AvaloniaProperty.Register<Flyout, object?>(nameof(Content));`
- `public static readonly StyledProperty<IDataTemplate?> ContentTemplateProperty = AvaloniaProperty.Register<Flyout, IDataTemplate?>(nameof(ContentTemplate));`
- `public Classes FlyoutPresenterClasses => _classes ??= new Classes();`
- `public static readonly StyledProperty<ControlTheme?> FlyoutPresenterThemeProperty = AvaloniaProperty.Register<Flyout, ControlTheme?>(nameof(FlyoutPresenterTheme));`
- `public ControlTheme? FlyoutPresenterTheme {`
- `public object? Content {`
- `public IDataTemplate? ContentTemplate {`

### `src/Avalonia.Controls/Flyouts/FlyoutBase.cs`
- `public abstract class FlyoutBase : AvaloniaObject`
- `public static readonly DirectProperty<FlyoutBase, bool> IsOpenProperty = AvaloniaProperty.RegisterDirect<FlyoutBase, bool>(nameof(IsOpen), x => x.IsOpen);`
- `public static readonly DirectProperty<FlyoutBase, Control?> TargetProperty = AvaloniaProperty.RegisterDirect<FlyoutBase, Control?>(nameof(Target), x => x.Target);`
- `public static readonly AttachedProperty<FlyoutBase?> AttachedFlyoutProperty = AvaloniaProperty.RegisterAttached<FlyoutBase, Control, FlyoutBase?>("AttachedFlyout", null);`
- `public event EventHandler? Opened;`
- `public event EventHandler? Closed;`
- `public bool IsOpen {`
- `public Control? Target {`
- `public static FlyoutBase? GetAttachedFlyout(Control element) {`
- `public static void SetAttachedFlyout(Control element, FlyoutBase? value) {`
- `public static void ShowAttachedFlyout(Control flyoutOwner) {`
- `public abstract void ShowAt(Control placementTarget);`
- `public abstract void Hide();`

### `src/Avalonia.Controls/Flyouts/FlyoutPresenter.cs`
- `public class FlyoutPresenter : ContentControl`

### `src/Avalonia.Controls/Flyouts/FlyoutShowMode.cs`
- `public enum FlyoutShowMode`

### `src/Avalonia.Controls/Flyouts/MenuFlyout.cs`
- `public class MenuFlyout : PopupFlyoutBase`
- `public MenuFlyout() {`
- `public static readonly StyledProperty<IEnumerable?> ItemsSourceProperty = AvaloniaProperty.Register<MenuFlyout, IEnumerable?>( nameof(ItemsSource));`
- `public static readonly StyledProperty<IDataTemplate?> ItemTemplateProperty = AvaloniaProperty.Register<MenuFlyout, IDataTemplate?>(nameof(ItemTemplate));`
- `public static readonly StyledProperty<ControlTheme?> ItemContainerThemeProperty = ItemsControl.ItemContainerThemeProperty.AddOwner<MenuFlyout>();`
- `public static readonly StyledProperty<ControlTheme?> FlyoutPresenterThemeProperty = Flyout.FlyoutPresenterThemeProperty.AddOwner<MenuFlyout>();`
- `public Classes FlyoutPresenterClasses => _classes ??= new Classes();`
- `public ItemCollection Items { get; }`
- `public IEnumerable? ItemsSource {`
- `public IDataTemplate? ItemTemplate {`
- `public ControlTheme? ItemContainerTheme {`
- `public ControlTheme? FlyoutPresenterTheme {`

### `src/Avalonia.Controls/Flyouts/MenuFlyoutPresenter.cs`
- `public class MenuFlyoutPresenter : MenuBase`
- `public MenuFlyoutPresenter() :base(new DefaultMenuInteractionHandler(true)) {`
- `public MenuFlyoutPresenter(IMenuInteractionHandler menuInteractionHandler) : base(menuInteractionHandler) {`
- `public override void Close() {`
- `public override void Open() {`

### `src/Avalonia.Controls/Flyouts/PopupFlyoutBase.cs`
- `public abstract class PopupFlyoutBase : FlyoutBase, IPopupHostProvider`
- `public static readonly StyledProperty<PlacementMode> PlacementProperty = Popup.PlacementProperty.AddOwner<PopupFlyoutBase>();`
- `public static readonly StyledProperty<double> HorizontalOffsetProperty = Popup.HorizontalOffsetProperty.AddOwner<PopupFlyoutBase>();`
- `public static readonly StyledProperty<double> VerticalOffsetProperty = Popup.VerticalOffsetProperty.AddOwner<PopupFlyoutBase>();`
- `public static readonly StyledProperty<PopupAnchor> PlacementAnchorProperty = Popup.PlacementAnchorProperty.AddOwner<PopupFlyoutBase>();`
- `public static readonly StyledProperty<PopupGravity> PlacementGravityProperty = Popup.PlacementGravityProperty.AddOwner<PopupFlyoutBase>();`
- `public static readonly StyledProperty<CustomPopupPlacementCallback?> CustomPopupPlacementCallbackProperty = Popup.CustomPopupPlacementCallbackProperty.AddOwner<PopupFlyoutBase>();`
- `public static readonly StyledProperty<FlyoutShowMode> ShowModeProperty = AvaloniaProperty.Register<PopupFlyoutBase, FlyoutShowMode>(nameof(ShowMode));`
- `public static readonly StyledProperty<bool> OverlayDismissEventPassThroughProperty = Popup.OverlayDismissEventPassThroughProperty.AddOwner<PopupFlyoutBase>();`
- `public static readonly StyledProperty<IInputElement?> OverlayInputPassThroughElementProperty = Popup.OverlayInputPassThroughElementProperty.AddOwner<PopupFlyoutBase>();`
- `public static readonly StyledProperty<PopupPositionerConstraintAdjustment> PlacementConstraintAdjustmentProperty = Popup.PlacementConstraintAdjustmentProperty.AddOwner<PopupFlyoutBase>();`
- `public PopupFlyoutBase() {`
- `public PlacementMode Placement {`
- `public PopupGravity PlacementGravity {`
- `public PopupAnchor PlacementAnchor {`
- `public double HorizontalOffset {`
- `public double VerticalOffset {`
- `public CustomPopupPlacementCallback? CustomPopupPlacementCallback {`
- `public FlyoutShowMode ShowMode {`
- `public bool OverlayDismissEventPassThrough {`
- `public IInputElement? OverlayInputPassThroughElement {`
- `public PopupPositionerConstraintAdjustment PlacementConstraintAdjustment {`
- `public event EventHandler<CancelEventArgs>? Closing;`
- `public event EventHandler? Opening;`
- `public sealed override void ShowAt(Control placementTarget) {`
- `public void ShowAt(Control placementTarget, bool showAtPointer) {`
- `public sealed override void Hide() {`

### `src/Avalonia.Controls/Generators/ItemContainerGenerator.cs`
- `public class ItemContainerGenerator`
- `public bool NeedsContainer(object? item, int index, out object? recycleKey) =>`
- `public Control CreateContainer(object? item, int index, object? recycleKey) => _owner.CreateContainerForItemOverride(item, index, recycleKey);`
- `public void PrepareItemContainer(Control container, object? item, int index) =>`
- `public void ItemContainerPrepared(Control container, object? item, int index) =>`
- `public void ItemContainerIndexChanged(Control container, int oldIndex, int newIndex) =>`
- `public void ClearItemContainer(Control container) => _owner.ClearItemContainer(container);`
- `public Control? ContainerFromIndex(int index) => _owner.ContainerFromIndex(index);`
- `public int IndexFromContainer(Control container) => _owner.IndexFromContainer(container);`

### `src/Avalonia.Controls/Generators/TreeItemContainerGenerator.cs`
- `public class TreeItemContainerGenerator : ItemContainerGenerator`
- `public TreeContainerIndex Index { get; }`
- `public class TreeContainerIndex`
- `public IEnumerable<Control> Containers => _owner.GetRealizedTreeContainers();`
- `public Control? ContainerFromItem(object item) => _owner.TreeContainerFromItem(item);`
- `public object? ItemFromContainer(Control container) => _owner.TreeItemFromContainer(container);`

### `src/Avalonia.Controls/Grid.cs`
- `public class Grid : Panel`
- `public Grid() {`
- `public static void SetColumn(Control element, int value) {`
- `public static int GetColumn(Control element) {`
- `public static void SetRow(Control element, int value) {`
- `public static int GetRow(Control element) {`
- `public static void SetColumnSpan(Control element, int value) {`
- `public static int GetColumnSpan(Control element) {`
- `public static void SetRowSpan(Control element, int value) {`
- `public static int GetRowSpan(Control element) {`
- `public static void SetIsSharedSizeScope(Control element, bool value) {`
- `public static bool GetIsSharedSizeScope(Control element) {`
- `public bool ShowGridLines {`
- `public double RowSpacing {`
- `public double ColumnSpacing {`
- `public ColumnDefinitions ColumnDefinitions {`
- `public RowDefinitions RowDefinitions {`
- `public static readonly StyledProperty<bool> ShowGridLinesProperty = AvaloniaProperty.Register<Grid, bool>(nameof(ShowGridLines));`
- `public static readonly StyledProperty<double> RowSpacingProperty = AvaloniaProperty.Register<Grid, double>(nameof(RowSpacing));`
- `public static readonly StyledProperty<double> ColumnSpacingProperty = AvaloniaProperty.Register<Grid, double>(nameof(ColumnSpacing));`
- `public static readonly AttachedProperty<int> ColumnProperty = AvaloniaProperty.RegisterAttached<Grid, Control, int>( "Column", defaultValue: 0, validate: v => v >= 0);`
- `public static readonly AttachedProperty<int> RowProperty = AvaloniaProperty.RegisterAttached<Grid, Control, int>( "Row", defaultValue: 0, validate: v => v >= 0);`
- `public static readonly AttachedProperty<int> ColumnSpanProperty = AvaloniaProperty.RegisterAttached<Grid, Control, int>( "ColumnSpan", defaultValue: 1, validate: v => v > 0);`
- `public static readonly AttachedProperty<int> RowSpanProperty = AvaloniaProperty.RegisterAttached<Grid, Control, int>( "RowSpan", defaultValue: 1, validate: v => v > 0);`
- `public static readonly AttachedProperty<bool> IsSharedSizeScopeProperty = AvaloniaProperty.RegisterAttached<Grid, Control, bool>( "IsSharedSizeScope");`

### `src/Avalonia.Controls/GridSplitter.cs`
- `public class GridSplitter : Thumb`
- `public static readonly StyledProperty<GridResizeDirection> ResizeDirectionProperty = AvaloniaProperty.Register<GridSplitter, GridResizeDirection>(nameof(ResizeDirection));`
- `public static readonly StyledProperty<GridResizeBehavior> ResizeBehaviorProperty = AvaloniaProperty.Register<GridSplitter, GridResizeBehavior>(nameof(ResizeBehavior));`
- `public static readonly StyledProperty<bool> ShowsPreviewProperty = AvaloniaProperty.Register<GridSplitter, bool>(nameof(ShowsPreview));`
- `public static readonly StyledProperty<double> KeyboardIncrementProperty = AvaloniaProperty.Register<GridSplitter, double>(nameof(KeyboardIncrement), 10d);`
- `public static readonly StyledProperty<double> DragIncrementProperty = AvaloniaProperty.Register<GridSplitter, double>(nameof(DragIncrement), 1d);`
- `public static readonly StyledProperty<ITemplate<Control>> PreviewContentProperty = AvaloniaProperty.Register<GridSplitter, ITemplate<Control>>(nameof(PreviewContent));`
- `public GridResizeDirection ResizeDirection {`
- `public GridResizeBehavior ResizeBehavior {`
- `public bool ShowsPreview {`
- `public double KeyboardIncrement {`
- `public double DragIncrement {`
- `public ITemplate<Control> PreviewContent {`
- `public enum GridResizeDirection`
- `public enum GridResizeBehavior`

### `src/Avalonia.Controls/HotkeyManager.cs`
- `public class HotKeyManager`
- `public static readonly AttachedProperty<KeyGesture?> HotKeyProperty = AvaloniaProperty.RegisterAttached<Control, KeyGesture?>("HotKey", typeof(HotKeyManager));`
- `public static void SetHotKey(AvaloniaObject target, KeyGesture value) => target.SetValue(HotKeyProperty, value);`
- `public static KeyGesture? GetHotKey(AvaloniaObject target) => target.GetValue(HotKeyProperty);`

### `src/Avalonia.Controls/HyperlinkButton.cs`
- `public class HyperlinkButton : Button`
- `public static readonly StyledProperty<bool> IsVisitedProperty = AvaloniaProperty.Register<HyperlinkButton, bool>( nameof(IsVisited), defaultValue: false);`
- `public static readonly StyledProperty<Uri?> NavigateUriProperty = AvaloniaProperty.Register<HyperlinkButton, Uri?>( nameof(NavigateUri), defaultValue: null);`
- `public HyperlinkButton() {`
- `public bool IsVisited {`
- `public Uri? NavigateUri {`

### `src/Avalonia.Controls/IGlobalDataTemplates.cs`
- `public interface IGlobalDataTemplates : IDataTemplateHost`

### `src/Avalonia.Controls/INativeMenuExporterEventsImplBridge.cs`
- `public interface INativeMenuExporterEventsImplBridge`

### `src/Avalonia.Controls/INativeMenuItemExporterEventsImplBridge.cs`
- `public interface INativeMenuItemExporterEventsImplBridge`

### `src/Avalonia.Controls/IScrollAnchorProvider.cs`
- `public interface IScrollAnchorProvider`

### `src/Avalonia.Controls/IScrollable.cs`
- `public interface IScrollable`

### `src/Avalonia.Controls/ISelectable.cs`
- `public interface ISelectable`

### `src/Avalonia.Controls/IconElement.cs`
- `public abstract class IconElement : TemplatedControl`

### `src/Avalonia.Controls/Image.cs`
- `public class Image : Control`
- `public static readonly StyledProperty<IImage?> SourceProperty = AvaloniaProperty.Register<Image, IImage?>(nameof(Source));`
- `public static readonly StyledProperty<BitmapBlendingMode> BlendModeProperty = AvaloniaProperty.Register<Image, BitmapBlendingMode>(nameof(BlendMode));`
- `public static readonly StyledProperty<Stretch> StretchProperty = AvaloniaProperty.Register<Image, Stretch>(nameof(Stretch), Stretch.Uniform);`
- `public static readonly StyledProperty<StretchDirection> StretchDirectionProperty = AvaloniaProperty.Register<Image, StretchDirection>( nameof(StretchDirection), StretchDirection.Both);`
- `public IImage? Source {`
- `public BitmapBlendingMode BlendMode {`
- `public Stretch Stretch {`
- `public StretchDirection StretchDirection {`
- `public sealed override void Render(DrawingContext context) {`

### `src/Avalonia.Controls/ItemCollection.cs`
- `public class ItemCollection : ItemsSourceView, IList`
- `public new object? this[int index] {`
- `public bool IsReadOnly => _mode == Mode.ItemsSource;`
- `public int Add(object? value) => WritableSource.Add(value);`
- `public void Clear() => WritableSource.Clear();`
- `public void Insert(int index, object? value) => WritableSource.Insert(index, value);`
- `public void RemoveAt(int index) => WritableSource.RemoveAt(index);`
- `public bool Remove(object? value) {`

### `src/Avalonia.Controls/ItemsControl.cs`
- `public class ItemsControl : TemplatedControl, IChildIndexProvider`
- `public static readonly StyledProperty<ControlTheme?> ItemContainerThemeProperty = AvaloniaProperty.Register<ItemsControl, ControlTheme?>(nameof(ItemContainerTheme));`
- `public static readonly DirectProperty<ItemsControl, int> ItemCountProperty = AvaloniaProperty.RegisterDirect<ItemsControl, int>(nameof(ItemCount), o => o.ItemCount);`
- `public static readonly StyledProperty<ITemplate<Panel?>> ItemsPanelProperty = AvaloniaProperty.Register<ItemsControl, ITemplate<Panel?>>(nameof(ItemsPanel), DefaultPanel);`
- `public static readonly StyledProperty<IEnumerable?> ItemsSourceProperty = AvaloniaProperty.Register<ItemsControl, IEnumerable?>(nameof(ItemsSource));`
- `public static readonly StyledProperty<IDataTemplate?> ItemTemplateProperty = AvaloniaProperty.Register<ItemsControl, IDataTemplate?>(nameof(ItemTemplate));`
- `public static readonly StyledProperty<IBinding?> DisplayMemberBindingProperty = AvaloniaProperty.Register<ItemsControl, IBinding?>(nameof(DisplayMemberBinding));`
- `public IBinding? DisplayMemberBinding {`
- `public ItemsControl() {`
- `public ItemContainerGenerator ItemContainerGenerator {`
- `public ItemCollection Items => _items;`
- `public ControlTheme? ItemContainerTheme {`
- `public int ItemCount {`
- `public ITemplate<Panel?> ItemsPanel {`
- `public IEnumerable? ItemsSource {`
- `public IDataTemplate? ItemTemplate {`
- `public ItemsPresenter? Presenter { get; private set; }`
- `public Panel? ItemsPanelRoot => Presenter?.Panel;`
- `public ItemsSourceView ItemsView => _items;`
- `public event EventHandler<ContainerPreparedEventArgs>? PreparingContainer;`
- `public event EventHandler<ContainerPreparedEventArgs>? ContainerPrepared;`
- `public event EventHandler<ContainerIndexChangedEventArgs>? ContainerIndexChanged;`
- `public event EventHandler<ContainerClearingEventArgs>? ContainerClearing;`
- `public Control? ContainerFromIndex(int index) => Presenter?.ContainerFromIndex(index);`
- `public Control? ContainerFromItem(object item) {`
- `public int IndexFromContainer(Control container) => Presenter?.IndexFromContainer(container) ?? -1;`
- `public object? ItemFromContainer(Control container) {`
- `public IEnumerable<Control> GetRealizedContainers() => Presenter?.GetRealizedContainers() ?? Array.Empty<Control>();`
- `public void ScrollIntoView(int index) => Presenter?.ScrollIntoView(index);`
- `public void ScrollIntoView(object item) => ScrollIntoView(ItemsView.IndexOf(item));`
- `public static ItemsControl? ItemsControlFromItemContaner(Control container) =>`
- `public static ItemsControl? ItemsControlFromItemContainer(Control container) {`

### `src/Avalonia.Controls/ItemsSourceView.cs`
- `public class ItemsSourceView : IReadOnlyList<object?>,`
- `public static ItemsSourceView Empty { get; } = new ItemsSourceView(Array.Empty<object?>());`
- `public int Count => Source.Count;`
- `public IList Source => _source;`
- `public object? this[int index] => GetAt(index);`
- `public event NotifyCollectionChangedEventHandler? CollectionChanged {`
- `public object? GetAt(int index) => Source[index];`
- `public bool Contains(object? item) => Source.Contains(item);`
- `public int IndexOf(object? item) => Source.IndexOf(item);`
- `public static ItemsSourceView GetOrCreate(IEnumerable? items) {`
- `public static ItemsSourceView<T> GetOrCreate<T>(IEnumerable? items) {`
- `public static ItemsSourceView<T> GetOrCreate<T>(IEnumerable<T>? items) {`
- `public IEnumerator<object?> GetEnumerator() {`
- `public sealed class ItemsSourceView<T> : ItemsSourceView, IReadOnlyList<T>`
- `public new static ItemsSourceView<T> Empty { get; } = new ItemsSourceView<T>(Array.Empty<T>());`
- `public new T this[int index] => GetAt(index);`
- `public new T GetAt(int index) => (T)Source[index]!;`
- `public new IEnumerator<T> GetEnumerator() {`

### `src/Avalonia.Controls/Label.cs`
- `public class Label : ContentControl`
- `public static readonly StyledProperty<IInputElement?> TargetProperty = AvaloniaProperty.Register<Label, IInputElement?>(nameof(Target));`
- `public IInputElement? Target {`
- `public Label() {`

### `src/Avalonia.Controls/LayoutTransformControl.cs`
- `public class LayoutTransformControl : Decorator`
- `public static readonly StyledProperty<ITransform?> LayoutTransformProperty = AvaloniaProperty.Register<LayoutTransformControl, ITransform?>(nameof(LayoutTransform));`
- `public static readonly StyledProperty<bool> UseRenderTransformProperty = AvaloniaProperty.Register<LayoutTransformControl, bool>(nameof(UseRenderTransform));`
- `public ITransform? LayoutTransform {`
- `public bool UseRenderTransform {`
- `public Control? TransformRoot => Child;`

### `src/Avalonia.Controls/ListBox.cs`
- `public class ListBox : SelectingItemsControl`
- `public static readonly DirectProperty<ListBox, IScrollable?> ScrollProperty = AvaloniaProperty.RegisterDirect<ListBox, IScrollable?>(nameof(Scroll), o => o.Scroll);`
- `public static readonly new DirectProperty<SelectingItemsControl, IList?> SelectedItemsProperty = SelectingItemsControl.SelectedItemsProperty;`
- `public static readonly new DirectProperty<SelectingItemsControl, ISelectionModel> SelectionProperty = SelectingItemsControl.SelectionProperty;`
- `public static readonly new StyledProperty<SelectionMode> SelectionModeProperty = SelectingItemsControl.SelectionModeProperty;`
- `public IScrollable? Scroll {`
- `public new IList? SelectedItems {`
- `public new ISelectionModel Selection {`
- `public new SelectionMode SelectionMode {`
- `public void SelectAll() => Selection.SelectAll();`
- `public void UnselectAll() => Selection.Clear();`

### `src/Avalonia.Controls/ListBoxItem.cs`
- `public class ListBoxItem : ContentControl, ISelectable`
- `public static readonly StyledProperty<bool> IsSelectedProperty = SelectingItemsControl.IsSelectedProperty.AddOwner<ListBoxItem>();`
- `public bool IsSelected {`

### `src/Avalonia.Controls/LoggingExtensions.cs`
- `public static class LoggingExtensions`
- `public static AppBuilder LogToTrace(this AppBuilder builder, LogEventLevel level = LogEventLevel.Warning, params string[] areas) =>`
- `public static AppBuilder LogToTextWriter(this AppBuilder builder, TextWriter writer, LogEventLevel level = LogEventLevel.Warning, params string[] areas) =>`
- `public static AppBuilder LogToDelegate( this AppBuilder builder, Action<string> logCallback, LogEventLevel level = LogEventLevel.Warning, params string[] areas) {`

### `src/Avalonia.Controls/MaskedTextBox.cs`
- `public class MaskedTextBox : TextBox`
- `public static readonly StyledProperty<bool> AsciiOnlyProperty = AvaloniaProperty.Register<MaskedTextBox, bool>(nameof(AsciiOnly));`
- `public static readonly StyledProperty<CultureInfo?> CultureProperty = AvaloniaProperty.Register<MaskedTextBox, CultureInfo?>(nameof(Culture), CultureInfo.CurrentCulture);`
- `public static readonly StyledProperty<bool> HidePromptOnLeaveProperty = AvaloniaProperty.Register<MaskedTextBox, bool>(nameof(HidePromptOnLeave));`
- `public static readonly DirectProperty<MaskedTextBox, bool?> MaskCompletedProperty = AvaloniaProperty.RegisterDirect<MaskedTextBox, bool?>(nameof(MaskCompleted), o => o.MaskCompleted);`
- `public static readonly DirectProperty<MaskedTextBox, bool?> MaskFullProperty = AvaloniaProperty.RegisterDirect<MaskedTextBox, bool?>(nameof(MaskFull), o => o.MaskFull);`
- `public static readonly StyledProperty<string?> MaskProperty = AvaloniaProperty.Register<MaskedTextBox, string?>(nameof(Mask), string.Empty);`
- `public static readonly StyledProperty<char> PromptCharProperty = AvaloniaProperty.Register<MaskedTextBox, char>(nameof(PromptChar), '_', coerce: CoercePromptChar);`
- `public static readonly StyledProperty<bool> ResetOnPromptProperty = AvaloniaProperty.Register<MaskedTextBox, bool>(nameof(ResetOnPrompt), true);`
- `public static readonly StyledProperty<bool> ResetOnSpaceProperty = AvaloniaProperty.Register<MaskedTextBox, bool>(nameof(ResetOnSpace), true);`
- `public MaskedTextBox() { }`
- `public MaskedTextBox(MaskedTextProvider maskedTextProvider) {`
- `public bool AsciiOnly {`
- `public CultureInfo? Culture {`
- `public bool HidePromptOnLeave {`
- `public string? Mask {`
- `public bool? MaskCompleted {`
- `public bool? MaskFull {`
- `public MaskedTextProvider? MaskProvider { get; private set; }`
- `public char PromptChar {`
- `public bool ResetOnPrompt {`
- `public bool ResetOnSpace {`

### `src/Avalonia.Controls/Menu.cs`
- `public class Menu : MenuBase, IMainMenu`
- `public Menu() {`
- `public Menu(IMenuInteractionHandler interactionHandler) : base(interactionHandler) {`
- `public override void Close() {`
- `public override void Open() {`

### `src/Avalonia.Controls/MenuBase.cs`
- `public abstract class MenuBase : SelectingItemsControl, IFocusScope, IMenu`
- `public static readonly DirectProperty<MenuBase, bool> IsOpenProperty = AvaloniaProperty.RegisterDirect<MenuBase, bool>( nameof(IsOpen), o => o.IsOpen);`
- `public static readonly RoutedEvent<RoutedEventArgs> OpenedEvent = RoutedEvent.Register<MenuBase, RoutedEventArgs>(nameof(Opened), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<RoutedEventArgs> ClosedEvent = RoutedEvent.Register<MenuBase, RoutedEventArgs>(nameof(Closed), RoutingStrategies.Bubble);`
- `public bool IsOpen {`
- `public event EventHandler<RoutedEventArgs>? Opened {`
- `public event EventHandler<RoutedEventArgs>? Closed {`
- `public abstract void Close();`
- `public abstract void Open();`

### `src/Avalonia.Controls/MenuItem.cs`
- `public class MenuItem : HeaderedSelectingItemsControl, IMenuItem, ISelectable, ICommandSource, IClickableControl, IRadioButton`
- `public static readonly StyledProperty<ICommand?> CommandProperty = Button.CommandProperty.AddOwner<MenuItem>(new(enableDataValidation: true));`
- `public static readonly StyledProperty<KeyGesture?> HotKeyProperty = HotKeyManager.HotKeyProperty.AddOwner<MenuItem>();`
- `public static readonly StyledProperty<object?> CommandParameterProperty = Button.CommandParameterProperty.AddOwner<MenuItem>();`
- `public static readonly StyledProperty<object?> IconProperty = AvaloniaProperty.Register<MenuItem, object?>(nameof(Icon));`
- `public static readonly StyledProperty<KeyGesture?> InputGestureProperty = AvaloniaProperty.Register<MenuItem, KeyGesture?>(nameof(InputGesture));`
- `public static readonly StyledProperty<bool> IsSubMenuOpenProperty = AvaloniaProperty.Register<MenuItem, bool>(nameof(IsSubMenuOpen));`
- `public static readonly StyledProperty<bool> StaysOpenOnClickProperty = AvaloniaProperty.Register<MenuItem, bool>(nameof(StaysOpenOnClick));`
- `public static readonly StyledProperty<MenuItemToggleType> ToggleTypeProperty = AvaloniaProperty.Register<MenuItem, MenuItemToggleType>(nameof(ToggleType));`
- `public static readonly StyledProperty<bool> IsCheckedProperty = AvaloniaProperty.Register<MenuItem, bool>(nameof(IsChecked));`
- `public static readonly StyledProperty<string?> GroupNameProperty = RadioButton.GroupNameProperty.AddOwner<MenuItem>();`
- `public static readonly RoutedEvent<RoutedEventArgs> ClickEvent = RoutedEvent.Register<MenuItem, RoutedEventArgs>( nameof(Click), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<RoutedEventArgs> PointerEnteredItemEvent = RoutedEvent.Register<MenuItem, RoutedEventArgs>( nameof(PointerEnteredItem), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<RoutedEventArgs> PointerExitedItemEvent = RoutedEvent.Register<MenuItem, RoutedEventArgs>( nameof(PointerExitedItem), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<RoutedEventArgs> SubmenuOpenedEvent = RoutedEvent.Register<MenuItem, RoutedEventArgs>( nameof(SubmenuOpened), RoutingStrategies.Bubble);`
- `public MenuItem() {`
- `public event EventHandler<RoutedEventArgs>? Click {`
- `public event EventHandler<RoutedEventArgs>? PointerEnteredItem {`
- `public event EventHandler<RoutedEventArgs>? PointerExitedItem {`
- `public event EventHandler<RoutedEventArgs>? SubmenuOpened {`
- `public ICommand? Command {`
- `public KeyGesture? HotKey {`
- `public object? CommandParameter {`
- `public object? Icon {`
- `public KeyGesture? InputGesture {`
- `public bool IsSelected {`
- `public bool IsSubMenuOpen {`
- `public bool StaysOpenOnClick {`
- `public MenuItemToggleType ToggleType {`
- `public bool IsChecked {`
- `public string? GroupName {`
- `public bool HasSubMenu => !Classes.Contains(":empty");`
- `public bool IsTopLevel => Parent is Menu;`
- `public void Open() => SetCurrentValue(IsSubMenuOpenProperty, true);`
- `public void Close() => SetCurrentValue(IsSubMenuOpenProperty, false);`

### `src/Avalonia.Controls/MenuItemToggleType.cs`
- `public enum MenuItemToggleType`

### `src/Avalonia.Controls/Mixins/PressedMixin.cs`
- `public static class PressedMixin`
- `public static void Attach<TControl>() where TControl : Control {`

### `src/Avalonia.Controls/Mixins/SelectableMixin.cs`
- `public static class SelectableMixin`
- `public static void Attach<TControl>(AvaloniaProperty<bool> isSelected) where TControl : Control {`

### `src/Avalonia.Controls/NativeControlHost.cs`
- `public class NativeControlHost : Control`
- `public bool TryUpdateNativeControlPosition() {`

### `src/Avalonia.Controls/NativeMenu.Export.cs`
- `public partial class NativeMenu`
- `public static readonly AttachedProperty<bool> IsNativeMenuExportedProperty = AvaloniaProperty.RegisterAttached<NativeMenu, TopLevel, bool>("IsNativeMenuExported");`
- `public static bool GetIsNativeMenuExported(TopLevel tl) => tl.GetValue(IsNativeMenuExportedProperty);`
- `public static readonly AttachedProperty<NativeMenu?> MenuProperty = AvaloniaProperty.RegisterAttached<NativeMenu, AvaloniaObject, NativeMenu?>("Menu");`
- `public static void SetMenu(AvaloniaObject o, NativeMenu? menu) => o.SetValue(MenuProperty, menu);`
- `public static NativeMenu? GetMenu(AvaloniaObject o) => o.GetValue(MenuProperty);`

### `src/Avalonia.Controls/NativeMenu.cs`
- `public partial class NativeMenu : AvaloniaObject,`
- `public IList<NativeMenuItemBase> Items => _items;`
- `public event EventHandler<EventArgs>? NeedsUpdate;`
- `public event EventHandler<EventArgs>? Opening;`
- `public event EventHandler<EventArgs>? Closed;`
- `public NativeMenu() {`
- `public static readonly DirectProperty<NativeMenu, NativeMenuItem?> ParentProperty = AvaloniaProperty.RegisterDirect<NativeMenu, NativeMenuItem?>(nameof(Parent), o => o.Parent);`
- `public NativeMenuItem? Parent {`
- `public void Add(NativeMenuItemBase item) => _items.Add(item);`
- `public IEnumerator<NativeMenuItemBase> GetEnumerator() => _items.GetEnumerator();`

### `src/Avalonia.Controls/NativeMenuBar.cs`
- `public class NativeMenuBar : TemplatedControl`
- `public static readonly AttachedProperty<bool> EnableMenuItemClickForwardingProperty = AvaloniaProperty.RegisterAttached<NativeMenuBar, MenuItem, bool>( "EnableMenuItemClickForwarding");`
- `public static void SetEnableMenuItemClickForwarding(MenuItem menuItem, bool enable) {`

### `src/Avalonia.Controls/NativeMenuItem.cs`
- `public class NativeMenuItem : NativeMenuItemBase, INativeMenuItemExporterEventsImplBridge`
- `public NativeMenuItem() {`
- `public NativeMenuItem(string header) : this() {`
- `public static readonly StyledProperty<NativeMenu?> MenuProperty = AvaloniaProperty.Register<NativeMenuItem, NativeMenu?>(nameof(Menu), coerce: CoerceMenu);`
- `public NativeMenu? Menu {`
- `public static readonly StyledProperty<Bitmap?> IconProperty = AvaloniaProperty.Register<NativeMenuItem, Bitmap?>(nameof(Icon));`
- `public Bitmap? Icon {`
- `public static readonly StyledProperty<string?> HeaderProperty = AvaloniaProperty.Register<NativeMenuItem, string?>(nameof(Header));`
- `public string? Header {`
- `public static readonly StyledProperty<string?> ToolTipProperty = AvaloniaProperty.Register<NativeMenuItem, string?>(nameof(ToolTip));`
- `public string? ToolTip {`
- `public static readonly StyledProperty<KeyGesture?> GestureProperty = AvaloniaProperty.Register<NativeMenuItem, KeyGesture?>(nameof(Gesture));`
- `public KeyGesture? Gesture {`
- `public static readonly StyledProperty<bool> IsCheckedProperty = MenuItem.IsCheckedProperty.AddOwner<NativeMenuItem>();`
- `public bool IsChecked {`
- `public static readonly StyledProperty<NativeMenuItemToggleType> ToggleTypeProperty = AvaloniaProperty.Register<NativeMenuItem, NativeMenuItemToggleType>(nameof(ToggleType));`
- `public NativeMenuItemToggleType ToggleType {`
- `public static readonly StyledProperty<ICommand?> CommandProperty = MenuItem.CommandProperty.AddOwner<NativeMenuItem>(new(enableDataValidation: true));`
- `public static readonly StyledProperty<object?> CommandParameterProperty = MenuItem.CommandParameterProperty.AddOwner<NativeMenuItem>();`
- `public static readonly StyledProperty<bool> IsEnabledProperty = AvaloniaProperty.Register<NativeMenuItem, bool>(nameof(IsEnabled), true);`
- `public bool IsEnabled {`
- `public static readonly StyledProperty<bool> IsVisibleProperty = Visual.IsVisibleProperty.AddOwner<NativeMenuItem>();`
- `public bool IsVisible {`
- `public bool HasClickHandlers => Click != null;`
- `public ICommand? Command {`
- `public object? CommandParameter {`
- `public event EventHandler? Click;`
- `public enum NativeMenuItemToggleType`

### `src/Avalonia.Controls/NativeMenuItemBase.cs`
- `public class NativeMenuItemBase : AvaloniaObject`
- `public static readonly DirectProperty<NativeMenuItemBase, NativeMenu?> ParentProperty = AvaloniaProperty.RegisterDirect<NativeMenuItemBase, NativeMenu?>(nameof(Parent), o => o.Parent);`
- `public NativeMenu? Parent {`

### `src/Avalonia.Controls/NativeMenuItemSeparator.cs`
- `public class NativeMenuItemSeparator : NativeMenuItem`
- `public NativeMenuItemSeparator() {`

### `src/Avalonia.Controls/Notifications/IManagedNotificationManager.cs`
- `public interface IManagedNotificationManager : INotificationManager`

### `src/Avalonia.Controls/Notifications/INotification.cs`
- `public interface INotification`

### `src/Avalonia.Controls/Notifications/INotificationManager.cs`
- `public interface INotificationManager`

### `src/Avalonia.Controls/Notifications/Notification.cs`
- `public class Notification : INotification, INotifyPropertyChanged`
- `public Notification(string? title, string? message, NotificationType type = NotificationType.Information, TimeSpan? expiration = null, Action? onClick = null, Action? onClose = null) {`
- `public Notification() : this(null, null) {`
- `public string? Title {`
- `public string? Message {`
- `public NotificationType Type { get; set; }`
- `public TimeSpan Expiration { get; set; }`
- `public Action? OnClick { get; set; }`
- `public Action? OnClose { get; set; }`
- `public event PropertyChangedEventHandler? PropertyChanged;`

### `src/Avalonia.Controls/Notifications/NotificationCard.cs`
- `public class NotificationCard : ContentControl`
- `public NotificationCard() {`
- `public bool IsClosing {`
- `public static readonly DirectProperty<NotificationCard, bool> IsClosingProperty = AvaloniaProperty.RegisterDirect<NotificationCard, bool>(nameof(IsClosing), o => o.IsClosing);`
- `public bool IsClosed {`
- `public static readonly StyledProperty<bool> IsClosedProperty = AvaloniaProperty.Register<NotificationCard, bool>(nameof(IsClosed));`
- `public NotificationType NotificationType {`
- `public static readonly StyledProperty<NotificationType> NotificationTypeProperty = AvaloniaProperty.Register<NotificationCard, NotificationType>(nameof(NotificationType));`
- `public static readonly RoutedEvent<RoutedEventArgs> NotificationClosedEvent = RoutedEvent.Register<NotificationCard, RoutedEventArgs>(nameof(NotificationClosed), RoutingStrategies.Bubble);`
- `public event EventHandler<RoutedEventArgs>? NotificationClosed {`
- `public static bool GetCloseOnClick(Button obj) {`
- `public static void SetCloseOnClick(Button obj, bool value) {`
- `public static readonly AttachedProperty<bool> CloseOnClickProperty = AvaloniaProperty.RegisterAttached<NotificationCard, Button, bool>("CloseOnClick", defaultValue: false);`
- `public void Close() {`

### `src/Avalonia.Controls/Notifications/NotificationPosition.cs`
- `public enum NotificationPosition`

### `src/Avalonia.Controls/Notifications/NotificationType.cs`
- `public enum NotificationType`

### `src/Avalonia.Controls/Notifications/ReversibleStackPanel.cs`
- `public class ReversibleStackPanel : StackPanel`
- `public static readonly StyledProperty<bool> ReverseOrderProperty = AvaloniaProperty.Register<ReversibleStackPanel, bool>(nameof(ReverseOrder));`
- `public bool ReverseOrder {`

### `src/Avalonia.Controls/Notifications/WindowNotificationManager.cs`
- `public class WindowNotificationManager : TemplatedControl, IManagedNotificationManager`
- `public static readonly StyledProperty<NotificationPosition> PositionProperty = AvaloniaProperty.Register<WindowNotificationManager, NotificationPosition>(nameof(Position), NotificationPosition.TopRight);`
- `public NotificationPosition Position {`
- `public static readonly StyledProperty<int> MaxItemsProperty = AvaloniaProperty.Register<WindowNotificationManager, int>(nameof(MaxItems), 5);`
- `public int MaxItems {`
- `public WindowNotificationManager(TopLevel? host) : this() {`
- `public WindowNotificationManager() {`
- `public void Show(INotification content) {`
- `public void Show(object content) {`
- `public void Show(object content, NotificationType type, TimeSpan? expiration = null, Action? onClick = null, Action? onClose = null, string[]? classes = null) {`
- `public void Close(INotification notification) => Close(notification as object);`
- `public void Close(object content) {`
- `public void CloseAll() {`

### `src/Avalonia.Controls/NumericUpDown/NumericUpDown.cs`
- `public class NumericUpDown : TemplatedControl`
- `public static readonly StyledProperty<bool> AllowSpinProperty = ButtonSpinner.AllowSpinProperty.AddOwner<NumericUpDown>();`
- `public static readonly StyledProperty<Location> ButtonSpinnerLocationProperty = ButtonSpinner.ButtonSpinnerLocationProperty.AddOwner<NumericUpDown>();`
- `public static readonly StyledProperty<bool> ShowButtonSpinnerProperty = ButtonSpinner.ShowButtonSpinnerProperty.AddOwner<NumericUpDown>();`
- `public static readonly StyledProperty<bool> ClipValueToMinMaxProperty = AvaloniaProperty.Register<NumericUpDown, bool>(nameof(ClipValueToMinMax));`
- `public static readonly StyledProperty<NumberFormatInfo?> NumberFormatProperty = AvaloniaProperty.Register<NumericUpDown, NumberFormatInfo?>(nameof(NumberFormat), NumberFormatInfo.CurrentInfo);`
- `public static readonly StyledProperty<string> FormatStringProperty = AvaloniaProperty.Register<NumericUpDown, string>(nameof(FormatString), string.Empty);`
- `public static readonly StyledProperty<decimal> IncrementProperty = AvaloniaProperty.Register<NumericUpDown, decimal>(nameof(Increment), 1.0m, coerce: OnCoerceIncrement);`
- `public static readonly StyledProperty<bool> IsReadOnlyProperty = AvaloniaProperty.Register<NumericUpDown, bool>(nameof(IsReadOnly));`
- `public static readonly StyledProperty<decimal> MaximumProperty = AvaloniaProperty.Register<NumericUpDown, decimal>(nameof(Maximum), decimal.MaxValue, coerce: OnCoerceMaximum);`
- `public static readonly StyledProperty<decimal> MinimumProperty = AvaloniaProperty.Register<NumericUpDown, decimal>(nameof(Minimum), decimal.MinValue, coerce: OnCoerceMinimum);`
- `public static readonly StyledProperty<NumberStyles> ParsingNumberStyleProperty = AvaloniaProperty.Register<NumericUpDown, NumberStyles>(nameof(ParsingNumberStyle), NumberStyles.Any);`
- `public static readonly StyledProperty<string?> TextProperty = AvaloniaProperty.Register<NumericUpDown, string?>(nameof(Text), defaultBindingMode: BindingMode.TwoWay, enableDataValidation: true);`
- `public static readonly StyledProperty<IValueConverter?> TextConverterProperty = AvaloniaProperty.Register<NumericUpDown, IValueConverter?>(nameof(TextConverter), defaultBindingMode: BindingMode.OneWay);`
- `public static readonly StyledProperty<decimal?> ValueProperty = AvaloniaProperty.Register<NumericUpDown, decimal?>(nameof(Value), coerce: (s,v) => ((NumericUpDown)s).OnCoerceValue(v),`
- `public static readonly StyledProperty<string?> WatermarkProperty = AvaloniaProperty.Register<NumericUpDown, string?>(nameof(Watermark));`
- `public static readonly StyledProperty<HorizontalAlignment> HorizontalContentAlignmentProperty = ContentControl.HorizontalContentAlignmentProperty.AddOwner<NumericUpDown>();`
- `public static readonly StyledProperty<VerticalAlignment> VerticalContentAlignmentProperty = ContentControl.VerticalContentAlignmentProperty.AddOwner<NumericUpDown>();`
- `public static readonly StyledProperty<Media.TextAlignment> TextAlignmentProperty = TextBox.TextAlignmentProperty.AddOwner<NumericUpDown>();`
- `public static readonly StyledProperty<object?> InnerLeftContentProperty = TextBox.InnerLeftContentProperty.AddOwner<NumericUpDown>();`
- `public static readonly StyledProperty<object?> InnerRightContentProperty = TextBox.InnerRightContentProperty.AddOwner<NumericUpDown>();`
- `public bool AllowSpin {`
- `public Location ButtonSpinnerLocation {`
- `public bool ShowButtonSpinner {`
- `public bool ClipValueToMinMax {`
- `public NumberFormatInfo? NumberFormat {`
- `public string FormatString {`
- `public decimal Increment {`
- `public bool IsReadOnly {`
- `public decimal Maximum {`
- `public decimal Minimum {`
- `public NumberStyles ParsingNumberStyle {`
- `public string? Text {`
- `public IValueConverter? TextConverter {`
- `public decimal? Value {`
- `public string? Watermark {`
- `public HorizontalAlignment HorizontalContentAlignment {`
- `public VerticalAlignment VerticalContentAlignment {`
- `public Media.TextAlignment TextAlignment {`
- `public NumericUpDown() {`
- `public object? InnerLeftContent {`
- `public object? InnerRightContent {`
- `public event EventHandler<SpinEventArgs>? Spinned;`
- `public static readonly RoutedEvent<NumericUpDownValueChangedEventArgs> ValueChangedEvent = RoutedEvent.Register<NumericUpDown, NumericUpDownValueChangedEventArgs>(nameof(ValueChanged), RoutingStrategies.Bubble);`
- `public event EventHandler<NumericUpDownValueChangedEventArgs>? ValueChanged {`

### `src/Avalonia.Controls/NumericUpDown/NumericUpDownValueChangedEventArgs.cs`
- `public class NumericUpDownValueChangedEventArgs : RoutedEventArgs`
- `public NumericUpDownValueChangedEventArgs(RoutedEvent routedEvent, decimal? oldValue, decimal? newValue) : base(routedEvent) {`
- `public decimal? OldValue { get; }`
- `public decimal? NewValue { get; }`

### `src/Avalonia.Controls/Panel.cs`
- `public class Panel : Control, IChildIndexProvider`
- `public static readonly StyledProperty<IBrush?> BackgroundProperty = Border.BackgroundProperty.AddOwner<Panel>();`
- `public Panel() {`
- `public Controls Children { get; } = new Controls();`
- `public IBrush? Background {`
- `public bool IsItemsHost { get; internal set; }`
- `public sealed override void Render(DrawingContext context) {`

### `src/Avalonia.Controls/PathIcon.cs`
- `public class PathIcon : IconElement`
- `public static readonly StyledProperty<Geometry?> DataProperty = AvaloniaProperty.Register<PathIcon, Geometry?>(nameof(Data));`
- `public Geometry? Data {`

### `src/Avalonia.Controls/PixelPointEventArgs.cs`
- `public class PixelPointEventArgs : EventArgs`
- `public PixelPointEventArgs(PixelPoint point) {`
- `public PixelPoint Point { get; }`

### `src/Avalonia.Controls/PlacementMode.cs`
- `public enum PlacementMode`

### `src/Avalonia.Controls/Platform/DefaultMenuInteractionHandler.cs`
- `public class DefaultMenuInteractionHandler : IMenuInteractionHandler`
- `public DefaultMenuInteractionHandler(bool isContextMenu) : this(isContextMenu, Input.InputManager.Instance, DefaultDelayRun) {`
- `public DefaultMenuInteractionHandler( bool isContextMenu, IInputManager? inputManager, Action<Action, TimeSpan> delayRun) {`
- `public void Attach(MenuBase menu) => AttachCore(menu);`
- `public void Detach(MenuBase menu) => DetachCore(menu);`
- `public static TimeSpan MenuShowDelay { get; set;} = TimeSpan.FromMilliseconds(400);`

### `src/Avalonia.Controls/Platform/Dialogs/IMountedVolumeInfoProvider.cs`
- `public interface IMountedVolumeInfoProvider`

### `src/Avalonia.Controls/Platform/Dialogs/IStorageProviderFactory.cs`
- Namespace: `Avalonia.Controls.Platform`
- `public interface IStorageProviderFactory`

### `src/Avalonia.Controls/Platform/Dialogs/ISystemDialogImpl.cs`
- `public interface ISystemDialogImpl`

### `src/Avalonia.Controls/Platform/Dialogs/MountedDriveInfo.cs`
- `public class MountedVolumeInfo : IEquatable<MountedVolumeInfo>`
- `public string? VolumeLabel { get; set; }`
- `public string? VolumePath { get; set; }`
- `public ulong VolumeSizeBytes { get; set; }`
- `public bool Equals(MountedVolumeInfo? other) {`

### `src/Avalonia.Controls/Platform/ExtendClientAreaChromeHints.cs`
- `public enum ExtendClientAreaChromeHints`

### `src/Avalonia.Controls/Platform/IApplicationPlatformEvents.cs`
- `public interface IApplicationPlatformEvents`

### `src/Avalonia.Controls/Platform/IInputPane.cs`
- `public interface IInputPane`
- `public abstract class InputPaneBase : IInputPane`
- `public virtual InputPaneState State { get; protected set; }`
- `public virtual Rect OccludedRect { get; protected set; }`
- `public event EventHandler<InputPaneStateEventArgs>? StateChanged;`
- `public enum InputPaneState`
- `public sealed class InputPaneStateEventArgs : EventArgs`
- `public InputPaneState NewState { get; }`
- `public Rect? StartRect { get; }`
- `public Rect EndRect { get; }`
- `public TimeSpan AnimationDuration { get; }`
- `public IEasing? Easing { get; }`
- `public InputPaneStateEventArgs(InputPaneState newState, Rect? startRect, Rect endRect, TimeSpan animationDuration, IEasing? easing) {`
- `public InputPaneStateEventArgs(InputPaneState newState, Rect? startRect, Rect endRect) : this(newState, startRect, endRect, default, null) {`

### `src/Avalonia.Controls/Platform/IInsetsManager.cs`
- `public interface IInsetsManager`
- `public abstract class InsetsManagerBase : IInsetsManager`
- `public virtual bool? IsSystemBarVisible { get; set; }`
- `public virtual bool DisplayEdgeToEdgePreference { get; set; }`
- `public virtual bool DisplayEdgeToEdge { get => DisplaysEdgeToEdge; set => DisplayEdgeToEdgePreference = value; }`
- `public virtual Thickness SafeAreaPadding { get; protected set; }`
- `public virtual Color? SystemBarColor { get; set; }`
- `public virtual bool DisplaysEdgeToEdge => DisplayEdgeToEdgePreference;`
- `public event EventHandler<SafeAreaChangedArgs>? SafeAreaChanged;`
- `public class SafeAreaChangedArgs : EventArgs`
- `public SafeAreaChangedArgs(Thickness safeArePadding) {`
- `public Thickness SafeAreaPadding { get; }`
- `public enum SystemBarTheme`

### `src/Avalonia.Controls/Platform/IMenuInteractionHandler.cs`
- `public interface IMenuInteractionHandler`

### `src/Avalonia.Controls/Platform/INativeControlHostImpl.cs`
- `public interface INativeControlHostImpl`
- `public interface INativeControlHostDestroyableControlHandle : IPlatformHandle`
- `public interface INativeControlHostControlTopLevelAttachment : IDisposable`

### `src/Avalonia.Controls/Platform/IPlatformIconLoader.cs`
- `public interface IPlatformIconLoader`

### `src/Avalonia.Controls/Platform/IPlatformLifetimeEventsImpl.cs`
- `public interface IPlatformLifetimeEventsImpl`

### `src/Avalonia.Controls/Platform/IPlatformNativeSurfaceHandle.cs`
- `public interface INativePlatformHandleSurface : IPlatformHandle`

### `src/Avalonia.Controls/Platform/IPopupImpl.cs`
- `public interface IPopupImpl : IWindowBaseImpl`

### `src/Avalonia.Controls/Platform/IScreenImpl.cs`
- `public interface IScreenImpl`
- `public class PlatformScreen(IPlatformHandle platformHandle) : Screen`
- `public override IPlatformHandle? TryGetPlatformHandle() => platformHandle;`
- `public override int GetHashCode() => platformHandle.GetHashCode();`
- `public override bool Equals(Screen? obj) {`
- `public abstract class ScreensBase<TKey, TScreen>(IEqualityComparer<TKey>? screenKeyComparer) : IScreenImpl`
- `public int ScreenCount => _screenCount ??= GetScreenCount();`
- `public IReadOnlyList<Screen> AllScreens {`
- `public Action? Changed { get; set; }`
- `public Screen? ScreenFromWindow(IWindowBaseImpl window) => ScreenFromTopLevel(window);`
- `public Screen? ScreenFromTopLevel(ITopLevelImpl topLevel) => ScreenFromTopLevelCore(topLevel);`
- `public Screen? ScreenFromPoint(PixelPoint point) => ScreenFromPointCore(point);`
- `public Screen? ScreenFromRect(PixelRect rect) => ScreenFromRectCore(rect);`
- `public void OnChanged() {`
- `public async Task<bool> RequestScreenDetails() {`

### `src/Avalonia.Controls/Platform/ITopLevelImpl.cs`
- `public interface ITopLevelImpl : IOptionalFeatureProvider, IDisposable`

### `src/Avalonia.Controls/Platform/ITopLevelNativeMenuExporter.cs`
- `public interface INativeMenuExporter`
- `public interface ITopLevelNativeMenuExporter : INativeMenuExporter`
- `public interface INativeMenuExporterProvider`

### `src/Avalonia.Controls/Platform/ITrayIconImpl.cs`
- `public interface ITrayIconImpl : IDisposable`
- `public interface ITrayIconWithIsTemplateImpl : ITrayIconImpl`

### `src/Avalonia.Controls/Platform/IWin32OptionsTopLevelImpl.cs`
- `public interface IWin32OptionsTopLevelImpl : ITopLevelImpl`
- `public CustomWindowStylesCallback? WindowStylesCallback { get; set; }`
- `public CustomWndProcHookCallback? WndProcHookCallback { get; set; }`

### `src/Avalonia.Controls/Platform/IWindowBaseImpl.cs`
- `public interface IWindowBaseImpl : ITopLevelImpl`

### `src/Avalonia.Controls/Platform/IWindowIconImpl.cs`
- `public interface IWindowIconImpl`

### `src/Avalonia.Controls/Platform/IWindowImpl.cs`
- `public interface IWindowImpl : IWindowBaseImpl`

### `src/Avalonia.Controls/Platform/IWindowingPlatform.cs`
- `public interface IWindowingPlatform`

### `src/Avalonia.Controls/Platform/IX11OptionsToplevelImplFeature.cs`
- Namespace: `Avalonia.Controls.Platform`
- `public enum X11NetWmWindowType`
- `public interface IX11OptionsToplevelImplFeature`

### `src/Avalonia.Controls/Platform/MacOSProperties.cs`
- Namespace: `Avalonia.Controls`
- `public class MacOSProperties`
- `public static readonly AttachedProperty<bool> IsTemplateIconProperty = AvaloniaProperty.RegisterAttached<MacOSProperties, TrayIcon, bool>("IsTemplateIcon");`
- `public static void SetIsTemplateIcon(TrayIcon obj, bool value) => obj.SetValue(IsTemplateIconProperty, value);`
- `public static bool GetIsTemplateIcon(TrayIcon obj) => obj.GetValue(IsTemplateIconProperty);`

### `src/Avalonia.Controls/Platform/ManagedDispatcherImpl.cs`
- Namespace: `Avalonia.Controls.Platform`
- `public class ManagedDispatcherImpl : IControlledDispatcherImpl`
- `public interface IManagedDispatcherInputProvider`
- `public ManagedDispatcherImpl(IManagedDispatcherInputProvider? inputProvider) {`
- `public bool CurrentThreadIsLoopThread => _loopThread == Thread.CurrentThread;`
- `public void Signal() {`
- `public event Action? Signaled;`
- `public event Action? Timer;`
- `public long Now => _clock.ElapsedMilliseconds;`
- `public void UpdateTimer(long? dueTimeInMs) {`
- `public bool CanQueryPendingInput => _inputProvider != null;`
- `public bool HasPendingInput => _inputProvider?.HasInput ?? false;`
- `public void RunLoop(CancellationToken token) {`

### `src/Avalonia.Controls/Platform/PlatformManager.cs`
- `public static partial class PlatformManager`
- `public static IDisposable DesignerMode() {`
- `public static void SetDesignerScalingFactor(double factor) {`
- `public static ITrayIconImpl? CreateTrayIcon() =>`
- `public static IWindowImpl CreateWindow() {`
- `public static IWindowImpl CreateEmbeddableWindow() {`
- `public static ITopLevelImpl CreateEmbeddableTopLevel() {`

### `src/Avalonia.Controls/Platform/Screen.cs`
- `public enum ScreenOrientation`
- `public class Screen : IEquatable<Screen>`
- `public string? DisplayName { get; protected set; }`
- `public ScreenOrientation CurrentOrientation { get; protected set; }`
- `public double Scaling { get; protected set; } = 1;`
- `public double PixelDensity => Scaling;`
- `public PixelRect Bounds { get; protected set; }`
- `public PixelRect WorkingArea { get; protected set; }`
- `public bool IsPrimary { get; protected set; }`
- `public bool Primary => IsPrimary;`
- `public Screen(double scaling, PixelRect bounds, PixelRect workingArea, bool isPrimary) {`
- `public virtual IPlatformHandle? TryGetPlatformHandle() => null;`
- `public override int GetHashCode() => RuntimeHelpers.GetHashCode(this);`
- `public override bool Equals(object? obj) => obj is Screen other && Equals(other);`
- `public virtual bool Equals(Screen? other) => ReferenceEquals(this, other);`
- `public static bool operator ==(Screen? left, Screen? right) {`
- `public static bool operator !=(Screen? left, Screen? right) {`
- `public override string ToString() {`

### `src/Avalonia.Controls/Platform/Surfaces/IFramebufferPlatformSurface.cs`
- `public interface IFramebufferPlatformSurface`
- `public interface IFramebufferRenderTarget : IDisposable`
- `public interface IFramebufferRenderTargetWithProperties : IFramebufferRenderTarget`
- `public record struct FramebufferLockProperties(bool PreviousFrameIsRetained);`
- `public class FuncFramebufferRenderTarget : IFramebufferRenderTarget`
- `public FuncFramebufferRenderTarget(Func<ILockedFramebuffer> lockFramebuffer) {`
- `public void Dispose() {`
- `public ILockedFramebuffer Lock() => _lockFramebuffer();`

### `src/Avalonia.Controls/Platform/Win32Properties.cs`
- `public static class Win32Properties`
- `public delegate (uint style, uint exStyle) CustomWindowStylesCallback(uint style, uint exStyle);`
- `public delegate IntPtr CustomWndProcHookCallback(IntPtr hWnd, uint msg, IntPtr wParam, IntPtr lParam, ref bool handled);`
- `public static void AddWindowStylesCallback(TopLevel topLevel, CustomWindowStylesCallback? callback) {`
- `public static void RemoveWindowStylesCallback(TopLevel topLevel, CustomWindowStylesCallback? callback) {`
- `public static void AddWndProcHookCallback(TopLevel topLevel, CustomWndProcHookCallback? callback) {`
- `public static void RemoveWndProcHookCallback(TopLevel topLevel, CustomWndProcHookCallback? callback) {`
- `public static readonly AttachedProperty<Win32HitTestValue> NonClientHitTestResultProperty = AvaloniaProperty.RegisterAttached<Visual, Win32HitTestValue>( "NonClientHitTestResult", typeof(Win32Properties), inherits: true, defaultValue: Win32HitTestValue.Client);`
- `public static void SetNonClientHitTestResult(Visual obj, Win32HitTestValue value) => obj.SetValue(NonClientHitTestResultProperty, value);`
- `public static Win32HitTestValue GetNonClientHitTestResult(Visual obj) => obj.GetValue(NonClientHitTestResultProperty);`
- `public enum Win32HitTestValue`

### `src/Avalonia.Controls/Platform/X11Properties.cs`
- Namespace: `Avalonia.Controls`
- `public class X11Properties`
- `public static readonly AttachedProperty<X11NetWmWindowType> NetWmWindowTypeProperty = AvaloniaProperty.RegisterAttached<X11Properties, Window, X11NetWmWindowType>("NetWmWindowType");`
- `public static void SetNetWmWindowType(Window obj, X11NetWmWindowType value) => obj.SetValue(NetWmWindowTypeProperty, value);`
- `public static X11NetWmWindowType GetNetWmWindowType(Window obj) => obj.GetValue(NetWmWindowTypeProperty);`
- `public static readonly AttachedProperty<string?> WmClassProperty = AvaloniaProperty.RegisterAttached<X11Properties, Window, string?>("WmClass");`
- `public static void SetWmClass(Window obj, string? value) => obj.SetValue(WmClassProperty, value);`
- `public static string? GetWmClass(Window obj) => obj.GetValue(WmClassProperty);`

### `src/Avalonia.Controls/PlatformInhibitionType.cs`
- `public enum PlatformInhibitionType`

### `src/Avalonia.Controls/Presenters/ContentPresenter.cs`
- `public class ContentPresenter : Control`
- `public static readonly StyledProperty<IBrush?> BackgroundProperty = Border.BackgroundProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<BackgroundSizing> BackgroundSizingProperty = Border.BackgroundSizingProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<IBrush?> BorderBrushProperty = Border.BorderBrushProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<Thickness> BorderThicknessProperty = Border.BorderThicknessProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<CornerRadius> CornerRadiusProperty = Border.CornerRadiusProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<BoxShadows> BoxShadowProperty = Border.BoxShadowProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<IBrush?> ForegroundProperty = TextElement.ForegroundProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<FontFamily> FontFamilyProperty = TextElement.FontFamilyProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<double> FontSizeProperty = TextElement.FontSizeProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<FontStyle> FontStyleProperty = TextElement.FontStyleProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<FontWeight> FontWeightProperty = TextElement.FontWeightProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<FontStretch> FontStretchProperty = TextElement.FontStretchProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<TextAlignment> TextAlignmentProperty = TextBlock.TextAlignmentProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<TextWrapping> TextWrappingProperty = TextBlock.TextWrappingProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<TextTrimming> TextTrimmingProperty = TextBlock.TextTrimmingProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<double> LineHeightProperty = TextBlock.LineHeightProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<int> MaxLinesProperty = TextBlock.MaxLinesProperty.AddOwner<ContentPresenter>();`
- `public static readonly DirectProperty<ContentPresenter, Control?> ChildProperty = AvaloniaProperty.RegisterDirect<ContentPresenter, Control?>( nameof(Child), o => o.Child);`
- `public static readonly StyledProperty<object?> ContentProperty = ContentControl.ContentProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<IDataTemplate?> ContentTemplateProperty = ContentControl.ContentTemplateProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<HorizontalAlignment> HorizontalContentAlignmentProperty = ContentControl.HorizontalContentAlignmentProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<VerticalAlignment> VerticalContentAlignmentProperty = ContentControl.VerticalContentAlignmentProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<Thickness> PaddingProperty = Decorator.PaddingProperty.AddOwner<ContentPresenter>();`
- `public static readonly StyledProperty<bool> RecognizesAccessKeyProperty = AvaloniaProperty.Register<ContentPresenter, bool>(nameof(RecognizesAccessKey));`
- `public ContentPresenter() {`
- `public IBrush? Background {`
- `public BackgroundSizing BackgroundSizing {`
- `public IBrush? BorderBrush {`
- `public Thickness BorderThickness {`
- `public CornerRadius CornerRadius {`
- `public BoxShadows BoxShadow {`
- `public IBrush? Foreground {`
- `public FontFamily FontFamily {`
- `public double FontSize {`
- `public FontStyle FontStyle {`
- `public FontWeight FontWeight {`
- `public FontStretch FontStretch {`
- `public TextAlignment TextAlignment {`
- `public TextWrapping TextWrapping {`
- `public TextTrimming TextTrimming {`
- `public double LineHeight {`
- `public int MaxLines {`
- `public Control? Child {`
- `public object? Content {`
- `public IDataTemplate? ContentTemplate {`
- `public HorizontalAlignment HorizontalContentAlignment {`
- `public VerticalAlignment VerticalContentAlignment {`
- `public Thickness Padding {`
- `public bool RecognizesAccessKey {`
- `public sealed override void ApplyTemplate() {`
- `public void UpdateChild() {`
- `public sealed override void Render(DrawingContext context) {`

### `src/Avalonia.Controls/Presenters/ItemsPresenter.cs`
- `public class ItemsPresenter : Control, ILogicalScrollable`
- `public static readonly StyledProperty<ITemplate<Panel?>> ItemsPanelProperty = ItemsControl.ItemsPanelProperty.AddOwner<ItemsPresenter>();`
- `public ITemplate<Panel?> ItemsPanel {`
- `public Panel? Panel { get; private set; }`
- `public override sealed void ApplyTemplate() {`

### `src/Avalonia.Controls/Presenters/ScrollContentPresenter.cs`
- `public class ScrollContentPresenter : ContentPresenter, IScrollable, IScrollAnchorProvider`
- `public static readonly StyledProperty<bool> CanHorizontallyScrollProperty = AvaloniaProperty.Register<ScrollContentPresenter, bool>(nameof(CanHorizontallyScroll));`
- `public static readonly StyledProperty<bool> CanVerticallyScrollProperty = AvaloniaProperty.Register<ScrollContentPresenter, bool>(nameof(CanVerticallyScroll));`
- `public static readonly DirectProperty<ScrollContentPresenter, Size> ExtentProperty = ScrollViewer.ExtentProperty.AddOwner<ScrollContentPresenter>( o => o.Extent);`
- `public static readonly StyledProperty<Vector> OffsetProperty = ScrollViewer.OffsetProperty.AddOwner<ScrollContentPresenter>(new(coerce: ScrollViewer.CoerceOffset));`
- `public static readonly DirectProperty<ScrollContentPresenter, Size> ViewportProperty = ScrollViewer.ViewportProperty.AddOwner<ScrollContentPresenter>( o => o.Viewport);`
- `public static readonly StyledProperty<SnapPointsType> HorizontalSnapPointsTypeProperty = ScrollViewer.HorizontalSnapPointsTypeProperty.AddOwner<ScrollContentPresenter>();`
- `public static readonly StyledProperty<SnapPointsType> VerticalSnapPointsTypeProperty = ScrollViewer.VerticalSnapPointsTypeProperty.AddOwner<ScrollContentPresenter>();`
- `public static readonly StyledProperty<SnapPointsAlignment> HorizontalSnapPointsAlignmentProperty = ScrollViewer.HorizontalSnapPointsAlignmentProperty.AddOwner<ScrollContentPresenter>();`
- `public static readonly StyledProperty<SnapPointsAlignment> VerticalSnapPointsAlignmentProperty = ScrollViewer.VerticalSnapPointsAlignmentProperty.AddOwner<ScrollContentPresenter>();`
- `public static readonly StyledProperty<bool> IsScrollChainingEnabledProperty = ScrollViewer.IsScrollChainingEnabledProperty.AddOwner<ScrollContentPresenter>();`
- `public ScrollContentPresenter() {`
- `public bool CanHorizontallyScroll {`
- `public bool CanVerticallyScroll {`
- `public Size Extent {`
- `public Vector Offset {`
- `public Size Viewport {`
- `public SnapPointsType HorizontalSnapPointsType {`
- `public SnapPointsType VerticalSnapPointsType {`
- `public SnapPointsAlignment HorizontalSnapPointsAlignment {`
- `public SnapPointsAlignment VerticalSnapPointsAlignment {`
- `public bool IsScrollChainingEnabled {`
- `public bool BringDescendantIntoView(Visual target, Rect targetRect) {`

### `src/Avalonia.Controls/Presenters/TextPresenter.cs`
- `public class TextPresenter : Control`
- `public static readonly StyledProperty<bool> ShowSelectionHighlightProperty = AvaloniaProperty.Register<TextPresenter, bool>(nameof(ShowSelectionHighlight), defaultValue: true);`
- `public static readonly StyledProperty<int> CaretIndexProperty = TextBox.CaretIndexProperty.AddOwner<TextPresenter>(new(coerce: TextBox.CoerceCaretIndex));`
- `public static readonly StyledProperty<bool> RevealPasswordProperty = AvaloniaProperty.Register<TextPresenter, bool>(nameof(RevealPassword));`
- `public static readonly StyledProperty<char> PasswordCharProperty = AvaloniaProperty.Register<TextPresenter, char>(nameof(PasswordChar));`
- `public static readonly StyledProperty<IBrush?> SelectionBrushProperty = AvaloniaProperty.Register<TextPresenter, IBrush?>(nameof(SelectionBrush));`
- `public static readonly StyledProperty<IBrush?> SelectionForegroundBrushProperty = AvaloniaProperty.Register<TextPresenter, IBrush?>(nameof(SelectionForegroundBrush));`
- `public static readonly StyledProperty<IBrush?> CaretBrushProperty = AvaloniaProperty.Register<TextPresenter, IBrush?>(nameof(CaretBrush));`
- `public static readonly StyledProperty<TimeSpan> CaretBlinkIntervalProperty = TextBox.CaretBlinkIntervalProperty.AddOwner<TextPresenter>();`
- `public static readonly StyledProperty<int> SelectionStartProperty = TextBox.SelectionStartProperty.AddOwner<TextPresenter>(new(coerce: TextBox.CoerceCaretIndex));`
- `public static readonly StyledProperty<int> SelectionEndProperty = TextBox.SelectionEndProperty.AddOwner<TextPresenter>(new(coerce: TextBox.CoerceCaretIndex));`
- `public static readonly StyledProperty<string?> TextProperty = TextBlock.TextProperty.AddOwner<TextPresenter>(new(string.Empty));`
- `public static readonly StyledProperty<string?> PreeditTextProperty = AvaloniaProperty.Register<TextPresenter, string?>(nameof(PreeditText));`
- `public static readonly StyledProperty<int?> PreeditTextCursorPositionProperty = AvaloniaProperty.Register<TextPresenter, int?>(nameof(PreeditTextCursorPosition));`
- `public static readonly StyledProperty<TextAlignment> TextAlignmentProperty = TextBlock.TextAlignmentProperty.AddOwner<TextPresenter>();`
- `public static readonly StyledProperty<TextWrapping> TextWrappingProperty = TextBlock.TextWrappingProperty.AddOwner<TextPresenter>();`
- `public static readonly StyledProperty<double> LineHeightProperty = TextBlock.LineHeightProperty.AddOwner<TextPresenter>();`
- `public static readonly StyledProperty<double> LetterSpacingProperty = TextBlock.LetterSpacingProperty.AddOwner<TextPresenter>();`
- `public static readonly StyledProperty<IBrush?> BackgroundProperty = Border.BackgroundProperty.AddOwner<TextPresenter>();`
- `public TextPresenter() { }`
- `public event EventHandler? CaretBoundsChanged;`
- `public IBrush? Background {`
- `public bool ShowSelectionHighlight {`
- `public string? Text {`
- `public string? PreeditText {`
- `public int? PreeditTextCursorPosition {`
- `public FontFamily FontFamily {`
- `public FontFeatureCollection? FontFeatures {`
- `public double FontSize {`
- `public FontStyle FontStyle {`
- `public FontWeight FontWeight {`
- `public FontStretch FontStretch {`
- `public IBrush? Foreground {`
- `public TextWrapping TextWrapping {`
- `public double LineHeight {`
- `public double LetterSpacing {`
- `public TextAlignment TextAlignment {`
- `public TextLayout TextLayout {`
- `public int CaretIndex {`
- `public char PasswordChar {`
- `public bool RevealPassword {`
- `public IBrush? SelectionBrush {`
- `public IBrush? SelectionForegroundBrush {`
- `public IBrush? CaretBrush {`
- `public TimeSpan CaretBlinkInterval {`
- `public int SelectionStart {`
- `public int SelectionEnd {`
- `public sealed override void Render(DrawingContext context) {`
- `public void ShowCaret() {`
- `public void HideCaret() {`
- `public void MoveCaretToTextPosition(int textPosition, bool trailingEdge = false) {`
- `public void MoveCaretToPoint(Point point) {`
- `public void MoveCaretVertical(LogicalDirection direction = LogicalDirection.Forward) {`
- `public CharacterHit GetNextCharacterHit(LogicalDirection direction = LogicalDirection.Forward) {`
- `public void MoveCaretHorizontal(LogicalDirection direction = LogicalDirection.Forward) {`

### `src/Avalonia.Controls/Primitives/AccessText.cs`
- `public class AccessText : TextBlock`
- `public static readonly AttachedProperty<bool> ShowAccessKeyProperty = AvaloniaProperty.RegisterAttached<AccessText, Control, bool>("ShowAccessKey", inherits: true);`
- `public AccessText() {`
- `public char AccessKey {`
- `public bool ShowAccessKey {`

### `src/Avalonia.Controls/Primitives/AdornerLayer.cs`
- `public class AdornerLayer : Canvas`
- `public static readonly AttachedProperty<Visual?> AdornedElementProperty = AvaloniaProperty.RegisterAttached<AdornerLayer, Visual, Visual?>("AdornedElement");`
- `public static readonly AttachedProperty<bool> IsClipEnabledProperty = AvaloniaProperty.RegisterAttached<AdornerLayer, Visual, bool>("IsClipEnabled", true);`
- `public static readonly AttachedProperty<Control?> AdornerProperty = AvaloniaProperty.RegisterAttached<AdornerLayer, Visual, Control?>("Adorner");`
- `public static readonly StyledProperty<ITemplate<Control>?> DefaultFocusAdornerProperty = AvaloniaProperty.Register<AdornerLayer, ITemplate<Control>?>(nameof(DefaultFocusAdorner));`
- `public AdornerLayer() {`
- `public static Visual? GetAdornedElement(Visual adorner) {`
- `public static void SetAdornedElement(Visual adorner, Visual? adorned) {`
- `public static AdornerLayer? GetAdornerLayer(Visual visual) {`
- `public static bool GetIsClipEnabled(Visual adorner) {`
- `public static void SetIsClipEnabled(Visual adorner, bool isClipEnabled) {`
- `public static Control? GetAdorner(Visual visual) {`
- `public static void SetAdorner(Visual visual, Control? adorner) {`
- `public ITemplate<Control>? DefaultFocusAdorner {`

### `src/Avalonia.Controls/Primitives/ChromeOverlayLayer.cs`
- `public class ChromeOverlayLayer : Panel`
- `public static Panel? GetOverlayLayer(Visual visual) {`
- `public void Add(Control c) {`

### `src/Avalonia.Controls/Primitives/HeaderedContentControl.cs`
- `public class HeaderedContentControl : ContentControl, IHeadered`
- `public static readonly StyledProperty<object?> HeaderProperty = AvaloniaProperty.Register<HeaderedContentControl, object?>(nameof(Header));`
- `public static readonly StyledProperty<IDataTemplate?> HeaderTemplateProperty = AvaloniaProperty.Register<HeaderedContentControl, IDataTemplate?>(nameof(HeaderTemplate));`
- `public object? Header {`
- `public ContentPresenter? HeaderPresenter {`
- `public IDataTemplate? HeaderTemplate {`

### `src/Avalonia.Controls/Primitives/HeaderedItemsControl.cs`
- `public class HeaderedItemsControl : ItemsControl, IContentPresenterHost`
- `public static readonly StyledProperty<object?> HeaderProperty = HeaderedContentControl.HeaderProperty.AddOwner<HeaderedItemsControl>();`
- `public static readonly StyledProperty<IDataTemplate?> HeaderTemplateProperty = AvaloniaProperty.Register<HeaderedItemsControl, IDataTemplate?>(nameof(HeaderTemplate));`
- `public object? Header {`
- `public IDataTemplate? HeaderTemplate {`
- `public ContentPresenter? HeaderPresenter {`

### `src/Avalonia.Controls/Primitives/HeaderedSelectingItemsControl.cs`
- `public class HeaderedSelectingItemsControl : SelectingItemsControl, IContentPresenterHost`
- `public static readonly StyledProperty<object?> HeaderProperty = HeaderedContentControl.HeaderProperty.AddOwner<HeaderedSelectingItemsControl>();`
- `public static readonly StyledProperty<IDataTemplate?> HeaderTemplateProperty = HeaderedItemsControl.HeaderTemplateProperty.AddOwner<HeaderedSelectingItemsControl>();`
- `public object? Header {`
- `public IDataTemplate? HeaderTemplate {`
- `public ContentPresenter? HeaderPresenter {`

### `src/Avalonia.Controls/Primitives/ILogicalScrollable.cs`
- `public interface ILogicalScrollable : IScrollable`

### `src/Avalonia.Controls/Primitives/IPopupHost.cs`
- `public interface IPopupHost : IDisposable, IFocusScope`

### `src/Avalonia.Controls/Primitives/IScrollSnapPointsInfo.cs`
- `public interface IScrollSnapPointsInfo`

### `src/Avalonia.Controls/Primitives/LightDismissOverlayLayer.cs`
- `public class LightDismissOverlayLayer : Border, ICustomHitTest`
- `public IInputElement? InputPassThroughElement { get; set; }`
- `public static LightDismissOverlayLayer? GetLightDismissOverlayLayer(Visual visual) {`
- `public bool HitTest(Point point) {`

### `src/Avalonia.Controls/Primitives/OverlayLayer.cs`
- `public class OverlayLayer : Canvas`
- `public Size AvailableSize { get; private set; }`
- `public static OverlayLayer? GetOverlayLayer(Visual visual) {`

### `src/Avalonia.Controls/Primitives/OverlayPopupHost.cs`
- `public class OverlayPopupHost : ContentControl, IPopupHost, IManagedPopupPositionerPopup, IInputRoot`
- `public static readonly StyledProperty<Transform?> TransformProperty = PopupRoot.TransformProperty.AddOwner<OverlayPopupHost>();`
- `public OverlayPopupHost(OverlayLayer overlayLayer) {`
- `public void SetChild(Control? control) {`
- `public Visual? HostedVisualTreeRoot => null;`
- `public Transform? Transform {`
- `public void Dispose() => Hide();`
- `public void Show() {`
- `public void Hide() {`
- `public void TakeFocus() {`
- `public void ConfigurePosition(Visual target, PlacementMode placement, Point offset, PopupAnchor anchor = PopupAnchor.None, PopupGravity gravity = PopupGravity.None, PopupPositionerConstraintAdjustment constraintAdjustment = PopupPositionerConstraintAdjustment.All, Rect? rect = null) {`
- `public static IPopupHost CreatePopupHost(Visual target, IAvaloniaDependencyResolver? dependencyResolver) => CreatePopupHost(target, dependencyResolver, false);`

### `src/Avalonia.Controls/Primitives/Popup.cs`
- `public class Popup : Control, IPopupHostProvider`
- `public static readonly StyledProperty<bool> WindowManagerAddShadowHintProperty = AvaloniaProperty.Register<Popup, bool>(nameof(WindowManagerAddShadowHint), false);`
- `public static readonly StyledProperty<Control?> ChildProperty = AvaloniaProperty.Register<Popup, Control?>(nameof(Child));`
- `public static readonly StyledProperty<bool> InheritsTransformProperty = AvaloniaProperty.Register<Popup, bool>(nameof(InheritsTransform));`
- `public static readonly StyledProperty<bool> IsOpenProperty = AvaloniaProperty.Register<Popup, bool>(nameof(IsOpen));`
- `public static readonly StyledProperty<PopupAnchor> PlacementAnchorProperty = AvaloniaProperty.Register<Popup, PopupAnchor>(nameof(PlacementAnchor));`
- `public static readonly StyledProperty<PopupPositionerConstraintAdjustment> PlacementConstraintAdjustmentProperty = AvaloniaProperty.Register<Popup, PopupPositionerConstraintAdjustment>( nameof(PlacementConstraintAdjustment), PopupPositionerConstraintAdjustment.FlipX | PopupPositionerConstraintAdjustment.FlipY | PopupPositionerConstraintAdjustment.SlideX | PopupPositionerConstraintAdjustment.SlideY | PopupPositionerConstraintAdjustment.ResizeX | PopupPositionerConstraintAdjustment.ResizeY);`
- `public static readonly StyledProperty<PopupGravity> PlacementGravityProperty = AvaloniaProperty.Register<Popup, PopupGravity>(nameof(PlacementGravity));`
- `public static readonly StyledProperty<PlacementMode> PlacementProperty = AvaloniaProperty.Register<Popup, PlacementMode>(nameof(Placement), defaultValue: PlacementMode.Bottom);`
- `public static readonly StyledProperty<PlacementMode> PlacementModeProperty = PlacementProperty;`
- `public static readonly StyledProperty<Rect?> PlacementRectProperty = AvaloniaProperty.Register<Popup, Rect?>(nameof(PlacementRect));`
- `public static readonly StyledProperty<Control?> PlacementTargetProperty = AvaloniaProperty.Register<Popup, Control?>(nameof(PlacementTarget));`
- `public static readonly StyledProperty<CustomPopupPlacementCallback?> CustomPopupPlacementCallbackProperty = AvaloniaProperty.Register<Popup, CustomPopupPlacementCallback?>(nameof(CustomPopupPlacementCallback));`
- `public static readonly StyledProperty<bool> OverlayDismissEventPassThroughProperty = AvaloniaProperty.Register<Popup, bool>(nameof(OverlayDismissEventPassThrough));`
- `public static readonly StyledProperty<IInputElement?> OverlayInputPassThroughElementProperty = AvaloniaProperty.Register<Popup, IInputElement?>(nameof(OverlayInputPassThroughElement));`
- `public static readonly StyledProperty<double> HorizontalOffsetProperty = AvaloniaProperty.Register<Popup, double>(nameof(HorizontalOffset));`
- `public static readonly StyledProperty<bool> IsLightDismissEnabledProperty = AvaloniaProperty.Register<Popup, bool>(nameof(IsLightDismissEnabled));`
- `public static readonly StyledProperty<double> VerticalOffsetProperty = AvaloniaProperty.Register<Popup, double>(nameof(VerticalOffset));`
- `public static readonly StyledProperty<bool> TopmostProperty = AvaloniaProperty.Register<Popup, bool>(nameof(Topmost));`
- `public static readonly AttachedProperty<bool> TakesFocusFromNativeControlProperty = AvaloniaProperty.RegisterAttached<Popup, Control, bool>(nameof(TakesFocusFromNativeControl), true);`
- `public static readonly StyledProperty<bool> ShouldUseOverlayLayerProperty = AvaloniaProperty.Register<Popup, bool>(nameof(ShouldUseOverlayLayer));`
- `public static readonly DirectProperty<Popup, bool> IsUsingOverlayLayerProperty = AvaloniaProperty.RegisterDirect<Popup, bool>( nameof(IsUsingOverlayLayer), o => o.IsUsingOverlayLayer);`
- `public event EventHandler<EventArgs>? Closed;`
- `public event EventHandler? Opened;`
- `public IPopupHost? Host => _openState?.PopupHost;`
- `public bool WindowManagerAddShadowHint {`
- `public Control? Child {`
- `public IAvaloniaDependencyResolver? DependencyResolver {`
- `public bool InheritsTransform {`
- `public bool IsLightDismissEnabled {`
- `public bool IsOpen {`
- `public PopupAnchor PlacementAnchor {`
- `public PopupPositionerConstraintAdjustment PlacementConstraintAdjustment {`
- `public PopupGravity PlacementGravity {`
- `public PlacementMode PlacementMode {`
- `public PlacementMode Placement {`
- `public Rect? PlacementRect {`
- `public Control? PlacementTarget {`
- `public CustomPopupPlacementCallback? CustomPopupPlacementCallback {`
- `public bool OverlayDismissEventPassThrough {`
- `public IInputElement? OverlayInputPassThroughElement {`
- `public double HorizontalOffset {`
- `public double VerticalOffset {`
- `public bool Topmost {`
- `public bool TakesFocusFromNativeControl {`
- `public bool ShouldUseOverlayLayer {`
- `public bool IsUsingOverlayLayer {`
- `public void Open() {`
- `public void Close() => CloseCore();`
- `public static bool GetTakesFocusFromNativeControl(Control control) {`
- `public static void SetTakesFocusFromNativeControl(Control control, bool value) {`
- `public bool IsInsidePopup(Visual visual) {`
- `public bool IsPointerOverPopup => ((IInputElement?)_openState?.PopupHost)?.IsPointerOver ?? false;`

### `src/Avalonia.Controls/Primitives/PopupPositioning/CustomPopupPlacement.cs`
- `public record CustomPopupPlacement`
- `public Size PopupSize { get; }`
- `public Visual Target { get; }`
- `public Rect AnchorRectangle { get; set; }`
- `public PopupAnchor Anchor {`
- `public PopupGravity Gravity {`
- `public PopupPositionerConstraintAdjustment ConstraintAdjustment { get; set; }`
- `public Point Offset { get; set; }`

### `src/Avalonia.Controls/Primitives/PopupPositioning/IPopupPositioner.cs`
- `public record struct PopupPositionerParameters`
- `public Size Size { get; set; }`
- `public Rect AnchorRectangle { get; set; }`
- `public PopupAnchor Anchor {`
- `public PopupGravity Gravity {`
- `public PopupPositionerConstraintAdjustment ConstraintAdjustment { get; set; }`
- `public Point Offset { get; set; }`
- `public enum PopupPositionerConstraintAdjustment`
- `public enum PopupAnchor`
- `public enum PopupGravity`
- `public interface IPopupPositioner`

### `src/Avalonia.Controls/Primitives/PopupPositioning/ManagedPopupPositioner.cs`
- `public interface IManagedPopupPositionerPopup`
- `public class ManagedPopupPositionerScreenInfo`
- `public Rect Bounds { get; }`
- `public Rect WorkingArea { get; }`
- `public ManagedPopupPositionerScreenInfo(Rect bounds, Rect workingArea) {`
- `public class ManagedPopupPositioner : IPopupPositioner`
- `public ManagedPopupPositioner(IManagedPopupPositionerPopup popup) {`
- `public void Update(PopupPositionerParameters parameters) {`

### `src/Avalonia.Controls/Primitives/PopupPositioning/ManagedPopupPositionerPopupImplHelper.cs`
- `public class ManagedPopupPositionerPopupImplHelper : IManagedPopupPositionerPopup`
- `public delegate void MoveResizeDelegate(PixelPoint position, Size size, double scaling);`
- `public ManagedPopupPositionerPopupImplHelper(ITopLevelImpl parent, MoveResizeDelegate moveResize) {`
- `public IReadOnlyList<ManagedPopupPositionerScreenInfo> Screens {`
- `public Rect ParentClientAreaScreenGeometry {`
- `public void MoveAndResize(Point devicePoint, Size virtualSize) {`
- `public virtual double Scaling => _parent.DesktopScaling;`

### `src/Avalonia.Controls/Primitives/PopupPositioning/PopupPositionRequest.cs`
- Namespace: `Avalonia.Controls.Primitives.PopupPositioning`
- `public class PopupPositionRequest`
- `public Visual Target { get; }`
- `public PlacementMode Placement {get;}`
- `public Point Offset {get;}`
- `public PopupAnchor Anchor {get;}`
- `public PopupGravity Gravity {get;}`
- `public PopupPositionerConstraintAdjustment ConstraintAdjustment {get;}`
- `public Rect? AnchorRect {get;}`
- `public CustomPopupPlacementCallback? PlacementCallback {get;}`

### `src/Avalonia.Controls/Primitives/PopupRoot.cs`
- `public sealed class PopupRoot : WindowBase, IHostedVisualTreeRoot, IDisposable, IStyleHost, IPopupHost`
- `public static readonly StyledProperty<Transform?> TransformProperty = AvaloniaProperty.Register<PopupRoot, Transform?>(nameof(Transform));`
- `public static readonly StyledProperty<bool> WindowManagerAddShadowHintProperty = Popup.WindowManagerAddShadowHintProperty.AddOwner<PopupRoot>();`
- `public PopupRoot(TopLevel parent, IPopupImpl impl) : this(parent, impl,null) {`
- `public PopupRoot(TopLevel parent, IPopupImpl impl, IAvaloniaDependencyResolver? dependencyResolver) : base(impl, dependencyResolver) {`
- `public new IPopupImpl? PlatformImpl => (IPopupImpl?)base.PlatformImpl;`
- `public Transform? Transform {`
- `public bool WindowManagerAddShadowHint {`
- `public TopLevel ParentTopLevel { get; }`
- `public void Dispose() {`
- `public void ConfigurePosition(Visual target, PlacementMode placement, Point offset, PopupAnchor anchor = PopupAnchor.None, PopupGravity gravity = PopupGravity.None, PopupPositionerConstraintAdjustment constraintAdjustment = PopupPositionerConstraintAdjustment.All, Rect? rect = null) {`
- `public void SetChild(Control? control) => Content = control;`
- `public void TakeFocus() => PlatformImpl?.TakeFocus();`

### `src/Avalonia.Controls/Primitives/RangeBase.cs`
- `public abstract class RangeBase : TemplatedControl`
- `public static readonly StyledProperty<double> MinimumProperty = AvaloniaProperty.Register<RangeBase, double>(nameof(Minimum), coerce: CoerceMinimum);`
- `public static readonly StyledProperty<double> MaximumProperty = AvaloniaProperty.Register<RangeBase, double>(nameof(Maximum), 100, coerce: CoerceMaximum);`
- `public static readonly StyledProperty<double> ValueProperty = AvaloniaProperty.Register<RangeBase, double>(nameof(Value), defaultBindingMode: BindingMode.TwoWay, coerce: CoerceValue);`
- `public static readonly StyledProperty<double> SmallChangeProperty = AvaloniaProperty.Register<RangeBase, double>(nameof(SmallChange), 1);`
- `public static readonly StyledProperty<double> LargeChangeProperty = AvaloniaProperty.Register<RangeBase, double>(nameof(LargeChange), 10);`
- `public static readonly RoutedEvent<RangeBaseValueChangedEventArgs> ValueChangedEvent = RoutedEvent.Register<RangeBase, RangeBaseValueChangedEventArgs>( nameof(ValueChanged), RoutingStrategies.Bubble);`
- `public event EventHandler<RangeBaseValueChangedEventArgs>? ValueChanged {`
- `public double Minimum {`
- `public double Maximum {`
- `public double Value {`
- `public double SmallChange {`
- `public double LargeChange {`

### `src/Avalonia.Controls/Primitives/RangeBaseValueChangedEventArgs.cs`
- `public class RangeBaseValueChangedEventArgs : RoutedEventArgs`
- `public RangeBaseValueChangedEventArgs(double oldValue, double newValue, RoutedEvent? routedEvent) : base(routedEvent) {`
- `public RangeBaseValueChangedEventArgs(double oldValue, double newValue, RoutedEvent? routedEvent, object? source) : base(routedEvent, source) {`
- `public double OldValue { get; init; }`
- `public double NewValue { get; init; }`

### `src/Avalonia.Controls/Primitives/ScrollBar.cs`
- `public class ScrollEventArgs : EventArgs`
- `public ScrollEventArgs(ScrollEventType eventType, double newValue) {`
- `public double NewValue { get; private set; }`
- `public ScrollEventType ScrollEventType { get; private set; }`
- `public class ScrollBar : RangeBase`
- `public static readonly StyledProperty<double> ViewportSizeProperty = AvaloniaProperty.Register<ScrollBar, double>(nameof(ViewportSize), defaultValue: double.NaN);`
- `public static readonly StyledProperty<ScrollBarVisibility> VisibilityProperty = AvaloniaProperty.Register<ScrollBar, ScrollBarVisibility>(nameof(Visibility), ScrollBarVisibility.Visible);`
- `public static readonly StyledProperty<Orientation> OrientationProperty = AvaloniaProperty.Register<ScrollBar, Orientation>(nameof(Orientation), Orientation.Vertical);`
- `public static readonly DirectProperty<ScrollBar, bool> IsExpandedProperty = AvaloniaProperty.RegisterDirect<ScrollBar, bool>( nameof(IsExpanded), o => o.IsExpanded);`
- `public static readonly StyledProperty<bool> AllowAutoHideProperty = AvaloniaProperty.Register<ScrollBar, bool>(nameof(AllowAutoHide), true);`
- `public static readonly StyledProperty<TimeSpan> HideDelayProperty = AvaloniaProperty.Register<ScrollBar, TimeSpan>(nameof(HideDelay), TimeSpan.FromSeconds(2));`
- `public static readonly StyledProperty<TimeSpan> ShowDelayProperty = AvaloniaProperty.Register<ScrollBar, TimeSpan>(nameof(ShowDelay), TimeSpan.FromSeconds(0.5));`
- `public ScrollBar() {`
- `public double ViewportSize {`
- `public ScrollBarVisibility Visibility {`
- `public Orientation Orientation {`
- `public bool IsExpanded {`
- `public bool AllowAutoHide {`
- `public TimeSpan HideDelay {`
- `public TimeSpan ShowDelay {`
- `public event EventHandler<ScrollEventArgs>? Scroll;`

### `src/Avalonia.Controls/Primitives/ScrollBarVisibility.cs`
- `public enum ScrollBarVisibility`

### `src/Avalonia.Controls/Primitives/ScrollEventType.cs`
- `public enum ScrollEventType`

### `src/Avalonia.Controls/Primitives/SelectingItemsControl.cs`
- `public class SelectingItemsControl : ItemsControl`
- `public static readonly StyledProperty<bool> AutoScrollToSelectedItemProperty = AvaloniaProperty.Register<SelectingItemsControl, bool>( nameof(AutoScrollToSelectedItem), defaultValue: true);`
- `public static readonly DirectProperty<SelectingItemsControl, int> SelectedIndexProperty = AvaloniaProperty.RegisterDirect<SelectingItemsControl, int>( nameof(SelectedIndex), o => o.SelectedIndex,`
- `public static readonly DirectProperty<SelectingItemsControl, object?> SelectedItemProperty = AvaloniaProperty.RegisterDirect<SelectingItemsControl, object?>( nameof(SelectedItem), o => o.SelectedItem,`
- `public static readonly StyledProperty<object?> SelectedValueProperty = AvaloniaProperty.Register<SelectingItemsControl, object?>(nameof(SelectedValue), defaultBindingMode: BindingMode.TwoWay);`
- `public static readonly StyledProperty<IBinding?> SelectedValueBindingProperty = AvaloniaProperty.Register<SelectingItemsControl, IBinding?>(nameof(SelectedValueBinding));`
- `public static readonly StyledProperty<bool> IsSelectedProperty = AvaloniaProperty.RegisterAttached<SelectingItemsControl, Control, bool>( "IsSelected", defaultBindingMode: BindingMode.TwoWay);`
- `public static readonly StyledProperty<bool> IsTextSearchEnabledProperty = AvaloniaProperty.Register<SelectingItemsControl, bool>(nameof(IsTextSearchEnabled), false);`
- `public static readonly RoutedEvent<RoutedEventArgs> IsSelectedChangedEvent = RoutedEvent.Register<SelectingItemsControl, RoutedEventArgs>( "IsSelectedChanged", RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<SelectionChangedEventArgs> SelectionChangedEvent = RoutedEvent.Register<SelectingItemsControl, SelectionChangedEventArgs>( nameof(SelectionChanged), RoutingStrategies.Bubble);`
- `public static readonly StyledProperty<bool> WrapSelectionProperty = AvaloniaProperty.Register<SelectingItemsControl, bool>(nameof(WrapSelection), defaultValue: false);`
- `public SelectingItemsControl() {`
- `public event EventHandler<SelectionChangedEventArgs>? SelectionChanged {`
- `public bool AutoScrollToSelectedItem {`
- `public int SelectedIndex {`
- `public object? SelectedItem {`
- `public IBinding? SelectedValueBinding {`
- `public object? SelectedValue {`
- `public bool IsTextSearchEnabled {`
- `public bool WrapSelection {`
- `public override void BeginInit() {`
- `public override void EndInit() {`
- `public static bool GetIsSelected(Control control) => control.GetValue(IsSelectedProperty);`
- `public static void SetIsSelected(Control control, bool value) => control.SetValue(IsSelectedProperty, value);`

### `src/Avalonia.Controls/Primitives/SelectionHandleType.cs`
- `public enum SelectionHandleType`

### `src/Avalonia.Controls/Primitives/SnapPointsAlignment.cs`
- `public enum SnapPointsAlignment`

### `src/Avalonia.Controls/Primitives/SnapPointsType.cs`
- `public enum SnapPointsType`

### `src/Avalonia.Controls/Primitives/TabStrip.cs`
- `public class TabStrip : SelectingItemsControl`

### `src/Avalonia.Controls/Primitives/TabStripItem.cs`
- `public class TabStripItem : ListBoxItem`

### `src/Avalonia.Controls/Primitives/TemplateAppliedEventArgs.cs`
- `public class TemplateAppliedEventArgs : RoutedEventArgs`
- `public TemplateAppliedEventArgs(INameScope nameScope) : base(TemplatedControl.TemplateAppliedEvent) {`
- `public INameScope NameScope { get; }`

### `src/Avalonia.Controls/Primitives/TemplatedControl.cs`
- `public class TemplatedControl : Control`
- `public static readonly StyledProperty<IBrush?> BackgroundProperty = Border.BackgroundProperty.AddOwner<TemplatedControl>();`
- `public static readonly StyledProperty<BackgroundSizing> BackgroundSizingProperty = Border.BackgroundSizingProperty.AddOwner<TemplatedControl>();`
- `public static readonly StyledProperty<IBrush?> BorderBrushProperty = Border.BorderBrushProperty.AddOwner<TemplatedControl>();`
- `public static readonly StyledProperty<Thickness> BorderThicknessProperty = Border.BorderThicknessProperty.AddOwner<TemplatedControl>();`
- `public static readonly StyledProperty<CornerRadius> CornerRadiusProperty = Border.CornerRadiusProperty.AddOwner<TemplatedControl>();`
- `public static readonly StyledProperty<FontFamily> FontFamilyProperty = TextElement.FontFamilyProperty.AddOwner<TemplatedControl>();`
- `public static readonly StyledProperty<FontFeatureCollection?> FontFeaturesProperty = TextElement.FontFeaturesProperty.AddOwner<TemplatedControl>();`
- `public static readonly StyledProperty<double> FontSizeProperty = TextElement.FontSizeProperty.AddOwner<TemplatedControl>();`
- `public static readonly StyledProperty<FontStyle> FontStyleProperty = TextElement.FontStyleProperty.AddOwner<TemplatedControl>();`
- `public static readonly StyledProperty<FontWeight> FontWeightProperty = TextElement.FontWeightProperty.AddOwner<TemplatedControl>();`
- `public static readonly StyledProperty<FontStretch> FontStretchProperty = TextElement.FontStretchProperty.AddOwner<TemplatedControl>();`
- `public static readonly StyledProperty<IBrush?> ForegroundProperty = TextElement.ForegroundProperty.AddOwner<TemplatedControl>();`
- `public static readonly StyledProperty<Thickness> PaddingProperty = Decorator.PaddingProperty.AddOwner<TemplatedControl>();`
- `public static readonly StyledProperty<IControlTemplate?> TemplateProperty = AvaloniaProperty.Register<TemplatedControl, IControlTemplate?>(nameof(Template));`
- `public static readonly AttachedProperty<bool> IsTemplateFocusTargetProperty = AvaloniaProperty.RegisterAttached<TemplatedControl, Control, bool>("IsTemplateFocusTarget");`
- `public static readonly RoutedEvent<TemplateAppliedEventArgs> TemplateAppliedEvent = RoutedEvent.Register<TemplatedControl, TemplateAppliedEventArgs>( nameof(TemplateApplied), RoutingStrategies.Direct);`
- `public event EventHandler<TemplateAppliedEventArgs>? TemplateApplied {`
- `public IBrush? Background {`
- `public BackgroundSizing BackgroundSizing {`
- `public IBrush? BorderBrush {`
- `public Thickness BorderThickness {`
- `public CornerRadius CornerRadius {`
- `public FontFamily FontFamily {`
- `public FontFeatureCollection? FontFeatures {`
- `public double FontSize {`
- `public FontStyle FontStyle {`
- `public FontWeight FontWeight {`
- `public FontStretch FontStretch {`
- `public IBrush? Foreground {`
- `public Thickness Padding {`
- `public IControlTemplate? Template {`
- `public static bool GetIsTemplateFocusTarget(Control control) {`
- `public static void SetIsTemplateFocusTarget(Control control, bool value) {`
- `public sealed override void ApplyTemplate() {`

### `src/Avalonia.Controls/Primitives/TextSearch.cs`
- `public static class TextSearch`
- `public static readonly AttachedProperty<string?> TextProperty = AvaloniaProperty.RegisterAttached<Interactive, string?>("Text", typeof(TextSearch));`
- `public static readonly AttachedProperty<IBinding?> TextBindingProperty = AvaloniaProperty.RegisterAttached<Interactive, IBinding?>("TextBinding", typeof(TextSearch));`
- `public static void SetText(Control control, string? text) => control.SetValue(TextProperty, text);`
- `public static string? GetText(Control control) => control.GetValue(TextProperty);`
- `public static void SetTextBinding(Interactive interactive, IBinding? value) => interactive.SetValue(TextBindingProperty, value);`
- `public static IBinding? GetTextBinding(Interactive interactive) => interactive.GetValue(TextBindingProperty);`

### `src/Avalonia.Controls/Primitives/TextSelectionHandle.cs`
- `public class TextSelectionHandle : Thumb`

### `src/Avalonia.Controls/Primitives/TextSelectorLayer.cs`
- `public class TextSelectorLayer : Canvas`
- `public Size AvailableSize { get; private set; }`
- `public static TextSelectorLayer? GetTextSelectorLayer(Visual visual) {`
- `public void Add(Control control) {`
- `public void Remove(Control control) {`

### `src/Avalonia.Controls/Primitives/Thumb.cs`
- `public class Thumb : TemplatedControl`
- `public static readonly RoutedEvent<VectorEventArgs> DragStartedEvent = RoutedEvent.Register<Thumb, VectorEventArgs>(nameof(DragStarted), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<VectorEventArgs> DragDeltaEvent = RoutedEvent.Register<Thumb, VectorEventArgs>(nameof(DragDelta), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<VectorEventArgs> DragCompletedEvent = RoutedEvent.Register<Thumb, VectorEventArgs>(nameof(DragCompleted), RoutingStrategies.Bubble);`
- `public event EventHandler<VectorEventArgs>? DragStarted {`
- `public event EventHandler<VectorEventArgs>? DragDelta {`
- `public event EventHandler<VectorEventArgs>? DragCompleted {`

### `src/Avalonia.Controls/Primitives/ToggleButton.cs`
- `public class ToggleButton : Button`
- `public static readonly StyledProperty<bool?> IsCheckedProperty = AvaloniaProperty.Register<ToggleButton, bool?>(nameof(IsChecked), false, defaultBindingMode: BindingMode.TwoWay);`
- `public static readonly StyledProperty<bool> IsThreeStateProperty = AvaloniaProperty.Register<ToggleButton, bool>(nameof(IsThreeState));`
- `public static readonly RoutedEvent<RoutedEventArgs> CheckedEvent = RoutedEvent.Register<ToggleButton, RoutedEventArgs>( nameof(Checked), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<RoutedEventArgs> UncheckedEvent = RoutedEvent.Register<ToggleButton, RoutedEventArgs>( nameof(Unchecked), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<RoutedEventArgs> IndeterminateEvent = RoutedEvent.Register<ToggleButton, RoutedEventArgs>( nameof(Indeterminate), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<RoutedEventArgs> IsCheckedChangedEvent = RoutedEvent.Register<ToggleButton, RoutedEventArgs>( nameof(IsCheckedChanged), RoutingStrategies.Bubble);`
- `public ToggleButton() {`
- `public event EventHandler<RoutedEventArgs>? Checked {`
- `public event EventHandler<RoutedEventArgs>? Unchecked {`
- `public event EventHandler<RoutedEventArgs>? Indeterminate {`
- `public event EventHandler<RoutedEventArgs>? IsCheckedChanged {`
- `public bool? IsChecked {`
- `public bool IsThreeState {`

### `src/Avalonia.Controls/Primitives/Track.cs`
- `public class Track : Control`
- `public static readonly StyledProperty<double> MinimumProperty = RangeBase.MinimumProperty.AddOwner<Track>();`
- `public static readonly StyledProperty<double> MaximumProperty = RangeBase.MaximumProperty.AddOwner<Track>();`
- `public static readonly StyledProperty<double> ValueProperty = RangeBase.ValueProperty.AddOwner<Track>();`
- `public static readonly StyledProperty<double> ViewportSizeProperty = ScrollBar.ViewportSizeProperty.AddOwner<Track>();`
- `public static readonly StyledProperty<Orientation> OrientationProperty = ScrollBar.OrientationProperty.AddOwner<Track>();`
- `public static readonly StyledProperty<Thumb?> ThumbProperty = AvaloniaProperty.Register<Track, Thumb?>(nameof(Thumb));`
- `public static readonly StyledProperty<Button?> IncreaseButtonProperty = AvaloniaProperty.Register<Track, Button?>(nameof(IncreaseButton));`
- `public static readonly StyledProperty<Button?> DecreaseButtonProperty = AvaloniaProperty.Register<Track, Button?>(nameof(DecreaseButton));`
- `public static readonly StyledProperty<bool> IsDirectionReversedProperty = AvaloniaProperty.Register<Track, bool>(nameof(IsDirectionReversed));`
- `public static readonly StyledProperty<bool> IgnoreThumbDragProperty = AvaloniaProperty.Register<Track, bool>(nameof(IgnoreThumbDrag));`
- `public static readonly StyledProperty<bool> DeferThumbDragProperty = AvaloniaProperty.Register<Track, bool>(nameof(DeferThumbDrag));`
- `public Track() {`
- `public double Minimum {`
- `public double Maximum {`
- `public double Value {`
- `public double ViewportSize {`
- `public Orientation Orientation {`
- `public Thumb? Thumb {`
- `public Button? IncreaseButton {`
- `public Button? DecreaseButton {`
- `public bool IsDirectionReversed {`
- `public bool IgnoreThumbDrag {`
- `public bool DeferThumbDrag {`
- `public virtual double ValueFromPoint(Point point) {`
- `public virtual double ValueFromDistance(double horizontal, double vertical) {`

### `src/Avalonia.Controls/Primitives/UniformGrid.cs`
- `public class UniformGrid : Panel`
- `public static readonly StyledProperty<int> RowsProperty = AvaloniaProperty.Register<UniformGrid, int>(nameof(Rows));`
- `public static readonly StyledProperty<int> ColumnsProperty = AvaloniaProperty.Register<UniformGrid, int>(nameof(Columns));`
- `public static readonly StyledProperty<int> FirstColumnProperty = AvaloniaProperty.Register<UniformGrid, int>(nameof(FirstColumn));`
- `public static readonly StyledProperty<double> RowSpacingProperty = AvaloniaProperty.Register<UniformGrid, double>(nameof(RowSpacing), 0);`
- `public static readonly StyledProperty<double> ColumnSpacingProperty = AvaloniaProperty.Register<UniformGrid, double>(nameof(ColumnSpacing), 0);`
- `public int Rows {`
- `public int Columns {`
- `public int FirstColumn {`
- `public double RowSpacing {`
- `public double ColumnSpacing {`

### `src/Avalonia.Controls/Primitives/VisualLayerManager.cs`
- `public class VisualLayerManager : Decorator`
- `public static readonly StyledProperty<ChromeOverlayLayer?> ChromeOverlayLayerProperty = AvaloniaProperty.Register<VisualLayerManager, ChromeOverlayLayer?>(nameof(ChromeOverlayLayer));`
- `public bool IsPopup { get; set; }`
- `public AdornerLayer AdornerLayer {`
- `public ChromeOverlayLayer ChromeOverlayLayer {`
- `public OverlayLayer? OverlayLayer {`
- `public TextSelectorLayer? TextSelectorLayer {`
- `public LightDismissOverlayLayer LightDismissOverlayLayer {`

### `src/Avalonia.Controls/ProgressBar.cs`
- `public class ProgressBar : RangeBase`
- `public class ProgressBarTemplateSettings : AvaloniaObject`
- `public static readonly DirectProperty<ProgressBarTemplateSettings, double> ContainerAnimationStartPositionProperty = AvaloniaProperty.RegisterDirect<ProgressBarTemplateSettings, double>( nameof(ContainerAnimationStartPosition), p => p.ContainerAnimationStartPosition,`
- `public static readonly DirectProperty<ProgressBarTemplateSettings, double> ContainerAnimationEndPositionProperty = AvaloniaProperty.RegisterDirect<ProgressBarTemplateSettings, double>( nameof(ContainerAnimationEndPosition), p => p.ContainerAnimationEndPosition,`
- `public static readonly DirectProperty<ProgressBarTemplateSettings, double> Container2AnimationStartPositionProperty = AvaloniaProperty.RegisterDirect<ProgressBarTemplateSettings, double>( nameof(Container2AnimationStartPosition), p => p.Container2AnimationStartPosition,`
- `public static readonly DirectProperty<ProgressBarTemplateSettings, double> Container2AnimationEndPositionProperty = AvaloniaProperty.RegisterDirect<ProgressBarTemplateSettings, double>( nameof(Container2AnimationEndPosition), p => p.Container2AnimationEndPosition,`
- `public static readonly DirectProperty<ProgressBarTemplateSettings, double> Container2WidthProperty = AvaloniaProperty.RegisterDirect<ProgressBarTemplateSettings, double>( nameof(Container2Width), p => p.Container2Width,`
- `public static readonly DirectProperty<ProgressBarTemplateSettings, double> ContainerWidthProperty = AvaloniaProperty.RegisterDirect<ProgressBarTemplateSettings, double>( nameof(ContainerWidth), p => p.ContainerWidth,`
- `public static readonly DirectProperty<ProgressBarTemplateSettings, double> IndeterminateStartingOffsetProperty = AvaloniaProperty.RegisterDirect<ProgressBarTemplateSettings, double>( nameof(IndeterminateStartingOffset), p => p.IndeterminateStartingOffset,`
- `public static readonly DirectProperty<ProgressBarTemplateSettings, double> IndeterminateEndingOffsetProperty = AvaloniaProperty.RegisterDirect<ProgressBarTemplateSettings, double>( nameof(IndeterminateEndingOffset), p => p.IndeterminateEndingOffset,`
- `public double ContainerWidth {`
- `public double Container2Width {`
- `public double ContainerAnimationStartPosition {`
- `public double ContainerAnimationEndPosition {`
- `public double Container2AnimationStartPosition {`
- `public double Container2AnimationEndPosition {`
- `public double IndeterminateStartingOffset {`
- `public double IndeterminateEndingOffset {`
- `public static readonly StyledProperty<bool> IsIndeterminateProperty = AvaloniaProperty.Register<ProgressBar, bool>(nameof(IsIndeterminate));`
- `public static readonly StyledProperty<bool> ShowProgressTextProperty = AvaloniaProperty.Register<ProgressBar, bool>(nameof(ShowProgressText));`
- `public static readonly StyledProperty<string> ProgressTextFormatProperty = AvaloniaProperty.Register<ProgressBar, string>(nameof(ProgressTextFormat), "{1:0}%");`
- `public static readonly StyledProperty<Orientation> OrientationProperty = AvaloniaProperty.Register<ProgressBar, Orientation>(nameof(Orientation));`
- `public static readonly DirectProperty<ProgressBar, double> PercentageProperty = AvaloniaProperty.RegisterDirect<ProgressBar, double>( nameof(Percentage), o => o.Percentage);`
- `public double Percentage {`
- `public ProgressBar() {`
- `public ProgressBarTemplateSettings TemplateSettings { get; } = new ProgressBarTemplateSettings();`
- `public bool IsIndeterminate {`
- `public bool ShowProgressText {`
- `public string ProgressTextFormat {`
- `public Orientation Orientation {`

### `src/Avalonia.Controls/PullToRefresh/RefreshCompletionDeferral.cs`
- `public class RefreshCompletionDeferral`
- `public RefreshCompletionDeferral(Action deferredAction) {`
- `public void Complete() {`
- `public RefreshCompletionDeferral Get() {`

### `src/Avalonia.Controls/PullToRefresh/RefreshContainer.cs`
- `public class RefreshContainer : ContentControl`
- `public static readonly RoutedEvent<RefreshRequestedEventArgs> RefreshRequestedEvent = RoutedEvent.Register<RefreshContainer, RefreshRequestedEventArgs>(nameof(RefreshRequested), RoutingStrategies.Bubble);`
- `public static readonly DirectProperty<RefreshContainer, RefreshVisualizer?> VisualizerProperty = AvaloniaProperty.RegisterDirect<RefreshContainer, RefreshVisualizer?>(nameof(Visualizer), s => s.Visualizer, (s, o) => s.Visualizer = o);`
- `public static readonly StyledProperty<PullDirection> PullDirectionProperty = AvaloniaProperty.Register<RefreshContainer, PullDirection>(nameof(PullDirection), PullDirection.TopToBottom);`
- `public RefreshVisualizer? Visualizer {`
- `public PullDirection PullDirection {`
- `public event EventHandler<RefreshRequestedEventArgs>? RefreshRequested {`
- `public RefreshContainer() {`
- `public void RequestRefresh() {`

### `src/Avalonia.Controls/PullToRefresh/RefreshRequestedEventArgs.cs`
- `public class RefreshRequestedEventArgs : RoutedEventArgs`
- `public RefreshCompletionDeferral GetDeferral() {`
- `public RefreshRequestedEventArgs(Action deferredAction, RoutedEvent? routedEvent) : base(routedEvent) {`
- `public RefreshRequestedEventArgs(RefreshCompletionDeferral completionDeferral, RoutedEvent? routedEvent) : base(routedEvent) {`

### `src/Avalonia.Controls/PullToRefresh/RefreshVisualizer.cs`
- `public class RefreshVisualizer : ContentControl`
- `public static readonly RoutedEvent<RefreshRequestedEventArgs> RefreshRequestedEvent = RoutedEvent.Register<RefreshVisualizer, RefreshRequestedEventArgs>(nameof(RefreshRequested), RoutingStrategies.Bubble);`
- `public static readonly DirectProperty<RefreshVisualizer, RefreshVisualizerState> RefreshVisualizerStateProperty = AvaloniaProperty.RegisterDirect<RefreshVisualizer, RefreshVisualizerState>(nameof(RefreshVisualizerState), s => s.RefreshVisualizerState);`
- `public static readonly DirectProperty<RefreshVisualizer, RefreshVisualizerOrientation> OrientationProperty = AvaloniaProperty.RegisterDirect<RefreshVisualizer, RefreshVisualizerOrientation>(nameof(Orientation), s => s.Orientation, (s, o) => s.Orientation = o);`
- `public RefreshVisualizerOrientation Orientation {`
- `public event EventHandler<RefreshRequestedEventArgs>? RefreshRequested {`
- `public void RequestRefresh() {`

### `src/Avalonia.Controls/PullToRefresh/RefreshVisualizerOrientation.cs`
- `public enum RefreshVisualizerOrientation`

### `src/Avalonia.Controls/PullToRefresh/RefreshVisualizerState.cs`
- `public enum RefreshVisualizerState`

### `src/Avalonia.Controls/RadioButton.cs`
- `public class RadioButton : ToggleButton, IRadioButton`
- `public static readonly StyledProperty<string?> GroupNameProperty = AvaloniaProperty.Register<RadioButton, string?>(nameof(GroupName));`
- `public string? GroupName {`

### `src/Avalonia.Controls/RelativePanel.AttachedProperties.cs`
- `public partial class RelativePanel`
- `public static object GetAbove(AvaloniaObject obj) {`
- `public static void SetAbove(AvaloniaObject obj, object value) {`
- `public static readonly AttachedProperty<object> AboveProperty = AvaloniaProperty.RegisterAttached<Layoutable, object>("Above", typeof(RelativePanel));`
- `public static bool GetAlignBottomWithPanel(AvaloniaObject obj) {`
- `public static void SetAlignBottomWithPanel(AvaloniaObject obj, bool value) {`
- `public static readonly AttachedProperty<bool> AlignBottomWithPanelProperty = AvaloniaProperty.RegisterAttached<Layoutable, bool>("AlignBottomWithPanel", typeof(RelativePanel));`
- `public static object GetAlignBottomWith(AvaloniaObject obj) {`
- `public static void SetAlignBottomWith(AvaloniaObject obj, object value) {`
- `public static readonly AttachedProperty<object> AlignBottomWithProperty = AvaloniaProperty.RegisterAttached<Layoutable, object>("AlignBottomWith", typeof(RelativePanel));`
- `public static bool GetAlignHorizontalCenterWithPanel(AvaloniaObject obj) {`
- `public static void SetAlignHorizontalCenterWithPanel(AvaloniaObject obj, bool value) {`
- `public static readonly AttachedProperty<bool> AlignHorizontalCenterWithPanelProperty = AvaloniaProperty.RegisterAttached<Layoutable, bool>("AlignHorizontalCenterWithPanel", typeof(RelativePanel), false);`
- `public static object GetAlignHorizontalCenterWith(AvaloniaObject obj) {`
- `public static void SetAlignHorizontalCenterWith(AvaloniaObject obj, object value) {`
- `public static readonly AttachedProperty<object> AlignHorizontalCenterWithProperty = AvaloniaProperty.RegisterAttached<Layoutable, object>("AlignHorizontalCenterWith", typeof(object), typeof(RelativePanel));`
- `public static bool GetAlignLeftWithPanel(AvaloniaObject obj) {`
- `public static void SetAlignLeftWithPanel(AvaloniaObject obj, bool value) {`
- `public static readonly AttachedProperty<bool> AlignLeftWithPanelProperty = AvaloniaProperty.RegisterAttached<Layoutable, bool>("AlignLeftWithPanel", typeof(RelativePanel), false);`
- `public static object GetAlignLeftWith(AvaloniaObject obj) {`
- `public static void SetAlignLeftWith(AvaloniaObject obj, object value) {`
- `public static readonly AttachedProperty<object> AlignLeftWithProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, object>("AlignLeftWith");`
- `public static bool GetAlignRightWithPanel(AvaloniaObject obj) {`
- `public static void SetAlignRightWithPanel(AvaloniaObject obj, bool value) {`
- `public static readonly AttachedProperty<bool> AlignRightWithPanelProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, bool>("AlignRightWithPanel", false);`
- `public static object GetAlignRightWith(AvaloniaObject obj) {`
- `public static void SetAlignRightWith(AvaloniaObject obj, object value) {`
- `public static readonly AttachedProperty<object> AlignRightWithProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, object>("AlignRightWith");`
- `public static bool GetAlignTopWithPanel(AvaloniaObject obj) {`
- `public static void SetAlignTopWithPanel(AvaloniaObject obj, bool value) {`
- `public static readonly AttachedProperty<bool> AlignTopWithPanelProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, bool>("AlignTopWithPanel", false);`
- `public static object GetAlignTopWith(AvaloniaObject obj) {`
- `public static void SetAlignTopWith(AvaloniaObject obj, object value) {`
- `public static readonly AttachedProperty<object> AlignTopWithProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, object>("AlignTopWith");`
- `public static bool GetAlignVerticalCenterWithPanel(AvaloniaObject obj) {`
- `public static void SetAlignVerticalCenterWithPanel(AvaloniaObject obj, bool value) {`
- `public static readonly AttachedProperty<bool> AlignVerticalCenterWithPanelProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, bool>("AlignVerticalCenterWithPanel", false);`
- `public static object GetAlignVerticalCenterWith(AvaloniaObject obj) {`
- `public static void SetAlignVerticalCenterWith(AvaloniaObject obj, object value) {`
- `public static readonly AttachedProperty<object> AlignVerticalCenterWithProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, object>("AlignVerticalCenterWith");`
- `public static object GetBelow(AvaloniaObject obj) {`
- `public static void SetBelow(AvaloniaObject obj, object value) {`
- `public static readonly AttachedProperty<object> BelowProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, object>("Below");`
- `public static object GetLeftOf(AvaloniaObject obj) {`
- `public static void SetLeftOf(AvaloniaObject obj, object value) {`
- `public static readonly AttachedProperty<object> LeftOfProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, object>("LeftOf");`
- `public static object GetRightOf(AvaloniaObject obj) {`
- `public static void SetRightOf(AvaloniaObject obj, object value) {`
- `public static readonly AttachedProperty<object> RightOfProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, object>("RightOf");`

### `src/Avalonia.Controls/RelativePanel.cs`
- `public partial class RelativePanel : Panel`
- `public RelativePanel() => _childGraph = new Graph();`

### `src/Avalonia.Controls/Remote/RemoteServer.cs`
- `public class RemoteServer : IDisposable`
- `public RemoteServer(IAvaloniaRemoteTransportConnection transport) {`
- `public object? Content {`
- `public void Dispose() {`

### `src/Avalonia.Controls/Remote/RemoteWidget.cs`
- `public class RemoteWidget : Control`
- `public enum SizingMode`
- `public RemoteWidget(IAvaloniaRemoteTransportConnection connection) {`
- `public SizingMode Mode { get; set; }`
- `public sealed override void Render(DrawingContext context) {`

### `src/Avalonia.Controls/RepeatButton.cs`
- `public class RepeatButton : Button`
- `public static readonly StyledProperty<int> IntervalProperty = AvaloniaProperty.Register<RepeatButton, int>(nameof(Interval), 100);`
- `public static readonly StyledProperty<int> DelayProperty = AvaloniaProperty.Register<RepeatButton, int>(nameof(Delay), 300);`
- `public int Interval {`
- `public int Delay {`

### `src/Avalonia.Controls/RequestBringIntoViewEventArgs.cs`
- `public class RequestBringIntoViewEventArgs : RoutedEventArgs`
- `public Visual? TargetObject { get; set; }`
- `public Rect TargetRect { get; set; }`

### `src/Avalonia.Controls/ResolveByNameAttribute.cs`
- `public sealed class ResolveByNameAttribute : Attribute`

### `src/Avalonia.Controls/RowDefinition.cs`
- `public class RowDefinition : DefinitionBase`
- `public static readonly StyledProperty<double> MaxHeightProperty = AvaloniaProperty.Register<RowDefinition, double>(nameof(MaxHeight), double.PositiveInfinity);`
- `public static readonly StyledProperty<double> MinHeightProperty = AvaloniaProperty.Register<RowDefinition, double>(nameof(MinHeight));`
- `public static readonly StyledProperty<GridLength> HeightProperty = AvaloniaProperty.Register<RowDefinition, GridLength>(nameof(Height), new GridLength(1, GridUnitType.Star));`
- `public RowDefinition() {`
- `public RowDefinition(double value, GridUnitType type) : this(new GridLength(value, type)) {`
- `public RowDefinition(GridLength height) {`
- `public double ActualHeight => Parent?.GetFinalRowDefinitionHeight(Index) ?? 0d;`
- `public double MaxHeight {`
- `public double MinHeight {`
- `public GridLength Height {`

### `src/Avalonia.Controls/RowDefinitions.cs`
- `public class RowDefinitions : DefinitionList<RowDefinition>`
- `public RowDefinitions() : base() {`
- `public RowDefinitions(string s) : this() {`
- `public override string ToString() {`
- `public static RowDefinitions Parse(string s) => new RowDefinitions(s);`

### `src/Avalonia.Controls/Screens.cs`
- `public class Screens`
- `public int ScreenCount => _iScreenImpl.ScreenCount;`
- `public IReadOnlyList<Screen> All => _iScreenImpl.AllScreens;`
- `public Screen? Primary => All.FirstOrDefault(x => x.IsPrimary);`
- `public event EventHandler? Changed {`
- `public Screens(IScreenImpl iScreenImpl) {`
- `public Screen? ScreenFromBounds(PixelRect bounds) {`
- `public Screen? ScreenFromWindow(WindowBase window) {`
- `public Screen? ScreenFromTopLevel(TopLevel topLevel) {`
- `public Screen? ScreenFromWindow(IWindowBaseImpl window) {`
- `public Screen? ScreenFromPoint(PixelPoint point) {`
- `public Screen? ScreenFromVisual(Visual visual) {`
- `public Task<bool> RequestScreenDetails() => _iScreenImpl.RequestScreenDetails();`

### `src/Avalonia.Controls/ScrollChangedEventArgs.cs`
- `public class ScrollChangedEventArgs : RoutedEventArgs`
- `public ScrollChangedEventArgs( Vector extentDelta, Vector offsetDelta, Vector viewportDelta) : this(ScrollViewer.ScrollChangedEvent, extentDelta, offsetDelta, viewportDelta) {`
- `public ScrollChangedEventArgs( RoutedEvent routedEvent, Vector extentDelta, Vector offsetDelta, Vector viewportDelta) : base(routedEvent) {`
- `public Vector ExtentDelta { get; }`
- `public Vector OffsetDelta { get; }`
- `public Vector ViewportDelta { get; }`

### `src/Avalonia.Controls/ScrollViewer.cs`
- `public class ScrollViewer : ContentControl, IScrollable, IScrollAnchorProvider, IInternalScroller`
- `public static readonly AttachedProperty<bool> BringIntoViewOnFocusChangeProperty = AvaloniaProperty.RegisterAttached<ScrollViewer, Control, bool>(nameof(BringIntoViewOnFocusChange), true);`
- `public static readonly DirectProperty<ScrollViewer, Size> ExtentProperty = AvaloniaProperty.RegisterDirect<ScrollViewer, Size>(nameof(Extent), o => o.Extent);`
- `public static readonly StyledProperty<Vector> OffsetProperty = AvaloniaProperty.Register<ScrollViewer, Vector>(nameof(Offset), coerce: CoerceOffset);`
- `public static readonly DirectProperty<ScrollViewer, Size> ViewportProperty = AvaloniaProperty.RegisterDirect<ScrollViewer, Size>(nameof(Viewport), o => o.Viewport);`
- `public static readonly DirectProperty<ScrollViewer, Size> LargeChangeProperty = AvaloniaProperty.RegisterDirect<ScrollViewer, Size>( nameof(LargeChange), o => o.LargeChange);`
- `public static readonly DirectProperty<ScrollViewer, Size> SmallChangeProperty = AvaloniaProperty.RegisterDirect<ScrollViewer, Size>( nameof(SmallChange), o => o.SmallChange);`
- `public static readonly DirectProperty<ScrollViewer, Vector> ScrollBarMaximumProperty = AvaloniaProperty.RegisterDirect<ScrollViewer, Vector>( nameof(ScrollBarMaximum), o => o.ScrollBarMaximum);`
- `public static readonly AttachedProperty<ScrollBarVisibility> HorizontalScrollBarVisibilityProperty = AvaloniaProperty.RegisterAttached<ScrollViewer, Control, ScrollBarVisibility>( nameof(HorizontalScrollBarVisibility), ScrollBarVisibility.Disabled);`
- `public static readonly AttachedProperty<SnapPointsType> HorizontalSnapPointsTypeProperty = AvaloniaProperty.RegisterAttached<ScrollViewer, Control, SnapPointsType>( nameof(HorizontalSnapPointsType));`
- `public static readonly AttachedProperty<SnapPointsType> VerticalSnapPointsTypeProperty = AvaloniaProperty.RegisterAttached<ScrollViewer, Control, SnapPointsType>( nameof(VerticalSnapPointsType));`
- `public static readonly AttachedProperty<SnapPointsAlignment> HorizontalSnapPointsAlignmentProperty = AvaloniaProperty.RegisterAttached<ScrollViewer, Control, SnapPointsAlignment>( nameof(HorizontalSnapPointsAlignment));`
- `public static readonly AttachedProperty<SnapPointsAlignment> VerticalSnapPointsAlignmentProperty = AvaloniaProperty.RegisterAttached<ScrollViewer, Control, SnapPointsAlignment>( nameof(VerticalSnapPointsAlignment));`
- `public static readonly AttachedProperty<ScrollBarVisibility> VerticalScrollBarVisibilityProperty = AvaloniaProperty.RegisterAttached<ScrollViewer, Control, ScrollBarVisibility>( nameof(VerticalScrollBarVisibility), ScrollBarVisibility.Auto);`
- `public static readonly DirectProperty<ScrollViewer, bool> IsExpandedProperty = ScrollBar.IsExpandedProperty.AddOwner<ScrollViewer>(o => o.IsExpanded);`
- `public static readonly AttachedProperty<bool> AllowAutoHideProperty = AvaloniaProperty.RegisterAttached<ScrollViewer, Control, bool>( nameof(AllowAutoHide), true);`
- `public static readonly AttachedProperty<bool> IsScrollChainingEnabledProperty = AvaloniaProperty.RegisterAttached<ScrollViewer, Control, bool>( nameof(IsScrollChainingEnabled), defaultValue: true);`
- `public static readonly AttachedProperty<bool> IsScrollInertiaEnabledProperty = AvaloniaProperty.RegisterAttached<ScrollViewer, Control, bool>( nameof(IsScrollInertiaEnabled), defaultValue: true);`
- `public static readonly AttachedProperty<bool> IsDeferredScrollingEnabledProperty = AvaloniaProperty.RegisterAttached<ScrollViewer, Control, bool>( nameof(IsDeferredScrollingEnabled));`
- `public static readonly RoutedEvent<ScrollChangedEventArgs> ScrollChangedEvent = RoutedEvent.Register<ScrollViewer, ScrollChangedEventArgs>( nameof(ScrollChanged), RoutingStrategies.Bubble);`
- `public ScrollViewer() {`
- `public event EventHandler<ScrollChangedEventArgs>? ScrollChanged {`
- `public bool BringIntoViewOnFocusChange {`
- `public Size Extent {`
- `public Vector Offset {`
- `public Size Viewport {`
- `public Size LargeChange => _largeChange;`
- `public Size SmallChange => _smallChange;`
- `public ScrollBarVisibility HorizontalScrollBarVisibility {`
- `public ScrollBarVisibility VerticalScrollBarVisibility {`
- `public Control? CurrentAnchor => (Presenter as IScrollAnchorProvider)?.CurrentAnchor;`
- `public Vector ScrollBarMaximum => new(Max(_extent.Width - _viewport.Width, 0), Max(_extent.Height - _viewport.Height, 0));`
- `public bool IsExpanded {`
- `public SnapPointsType HorizontalSnapPointsType {`
- `public SnapPointsType VerticalSnapPointsType {`
- `public SnapPointsAlignment HorizontalSnapPointsAlignment {`
- `public SnapPointsAlignment VerticalSnapPointsAlignment {`
- `public bool AllowAutoHide {`
- `public bool IsScrollChainingEnabled {`
- `public bool IsScrollInertiaEnabled {`
- `public bool IsDeferredScrollingEnabled {`
- `public void LineUp() => SetCurrentValue(OffsetProperty, Offset - new Vector(0, _smallChange.Height));`
- `public void LineDown() => SetCurrentValue(OffsetProperty, Offset + new Vector(0, _smallChange.Height));`
- `public void LineLeft() => SetCurrentValue(OffsetProperty, Offset - new Vector(_smallChange.Width, 0));`
- `public void LineRight() => SetCurrentValue(OffsetProperty, Offset + new Vector(_smallChange.Width, 0));`
- `public void PageUp() => SetCurrentValue(OffsetProperty, Offset.WithY(Math.Max(Offset.Y - _viewport.Height, 0)));`
- `public void PageDown() => SetCurrentValue(OffsetProperty, Offset.WithY(Math.Min(Offset.Y + _viewport.Height, ScrollBarMaximum.Y)));`
- `public void PageLeft() => SetCurrentValue(OffsetProperty, Offset.WithX(Math.Max(Offset.X - _viewport.Width, 0)));`
- `public void PageRight() => SetCurrentValue(OffsetProperty, Offset.WithX(Math.Min(Offset.X + _viewport.Width, ScrollBarMaximum.X)));`
- `public void ScrollToHome() => SetCurrentValue(OffsetProperty, new Vector(double.NegativeInfinity, double.NegativeInfinity));`
- `public void ScrollToEnd() => SetCurrentValue(OffsetProperty, new Vector(double.NegativeInfinity, double.PositiveInfinity));`
- `public static bool GetBringIntoViewOnFocusChange(Control control) {`
- `public static void SetBringIntoViewOnFocusChange(Control control, bool value) {`
- `public static ScrollBarVisibility GetHorizontalScrollBarVisibility(Control control) {`
- `public static void SetHorizontalScrollBarVisibility(Control control, ScrollBarVisibility value) {`
- `public static SnapPointsType GetHorizontalSnapPointsType(Control control) {`
- `public static void SetHorizontalSnapPointsType(Control control, SnapPointsType value) {`
- `public static SnapPointsType GetVerticalSnapPointsType(Control control) {`
- `public static void SetVerticalSnapPointsType(Control control, SnapPointsType value) {`
- `public static SnapPointsAlignment GetHorizontalSnapPointsAlignment(Control control) {`
- `public static void SetHorizontalSnapPointsAlignment(Control control, SnapPointsAlignment value) {`
- `public static SnapPointsAlignment GetVerticalSnapPointsAlignment(Control control) {`
- `public static void SetVerticalSnapPointsAlignment(Control control, SnapPointsAlignment value) {`
- `public static ScrollBarVisibility GetVerticalScrollBarVisibility(Control control) {`
- `public static void SetAllowAutoHide(Control control, bool value) {`
- `public static bool GetAllowAutoHide(Control control) {`
- `public static void SetIsScrollChainingEnabled(Control control, bool value) {`
- `public static bool GetIsScrollChainingEnabled(Control control) {`
- `public static void SetVerticalScrollBarVisibility(Control control, ScrollBarVisibility value) {`
- `public static bool GetIsScrollInertiaEnabled(Control control) {`
- `public static void SetIsScrollInertiaEnabled(Control control, bool value) {`
- `public static bool GetIsDeferredScrollingEnabled(Control control) => control.GetValue(IsDeferredScrollingEnabledProperty);`
- `public static void SetIsDeferredScrollingEnabled(Control control, bool value) => control.SetValue(IsDeferredScrollingEnabledProperty, value);`
- `public void RegisterAnchorCandidate(Control element) {`
- `public void UnregisterAnchorCandidate(Control element) {`

### `src/Avalonia.Controls/SelectableTextBlock.cs`
- `public class SelectableTextBlock : TextBlock, IInlineHost`
- `public static readonly StyledProperty<int> SelectionStartProperty = TextBox.SelectionStartProperty.AddOwner<SelectableTextBlock>();`
- `public static readonly StyledProperty<int> SelectionEndProperty = TextBox.SelectionEndProperty.AddOwner<SelectableTextBlock>();`
- `public static readonly DirectProperty<SelectableTextBlock, string> SelectedTextProperty = AvaloniaProperty.RegisterDirect<SelectableTextBlock, string>( nameof(SelectedText), o => o.SelectedText);`
- `public static readonly StyledProperty<IBrush?> SelectionBrushProperty = TextBox.SelectionBrushProperty.AddOwner<SelectableTextBlock>();`
- `public static readonly StyledProperty<IBrush?> SelectionForegroundBrushProperty = TextBox.SelectionForegroundBrushProperty.AddOwner<SelectableTextBlock>();`
- `public static readonly DirectProperty<SelectableTextBlock, bool> CanCopyProperty = TextBox.CanCopyProperty.AddOwner<SelectableTextBlock>(o => o.CanCopy);`
- `public static readonly RoutedEvent<RoutedEventArgs> CopyingToClipboardEvent = RoutedEvent.Register<SelectableTextBlock, RoutedEventArgs>( nameof(CopyingToClipboard), RoutingStrategies.Bubble);`
- `public event EventHandler<RoutedEventArgs>? CopyingToClipboard {`
- `public IBrush? SelectionBrush {`
- `public IBrush? SelectionForegroundBrush {`
- `public int SelectionStart {`
- `public int SelectionEnd {`
- `public string SelectedText {`
- `public bool CanCopy {`
- `public async void Copy() {`
- `public void SelectAll() {`
- `public void ClearSelection() {`

### `src/Avalonia.Controls/Selection/ISelectionModel.cs`
- `public interface ISelectionModel : INotifyPropertyChanged`
- `public event EventHandler<SelectionModelIndexesChangedEventArgs>? IndexesChanged;`
- `public event EventHandler<SelectionModelSelectionChangedEventArgs>? SelectionChanged;`
- `public event EventHandler? LostSelection;`
- `public event EventHandler? SourceReset;`
- `public void BeginBatchUpdate();`
- `public void EndBatchUpdate();`
- `public static class SelectionModelExtensions`
- `public static IDisposable BatchUpdate(this ISelectionModel model) {`
- `public record struct BatchUpdateOperation : IDisposable`
- `public BatchUpdateOperation(ISelectionModel owner) {`
- `public void Dispose() {`

### `src/Avalonia.Controls/Selection/SelectionModel.cs`
- `public class SelectionModel<T> : SelectionNodeBase<T>, ISelectionModel`
- `public SelectionModel() {`
- `public SelectionModel(IEnumerable<T>? source) {`
- `public new IEnumerable? Source {`
- `public bool SingleSelect {`
- `public int SelectedIndex {`
- `public IReadOnlyList<int> SelectedIndexes => _selectedIndexes ??= new SelectedIndexes<T>(this);`
- `public T? SelectedItem {`
- `public IReadOnlyList<T?> SelectedItems {`
- `public int AnchorIndex {`
- `public int Count {`
- `public event EventHandler<SelectionModelIndexesChangedEventArgs>? IndexesChanged;`
- `public event EventHandler<SelectionModelSelectionChangedEventArgs<T>>? SelectionChanged;`
- `public event EventHandler? LostSelection;`
- `public event EventHandler? SourceReset;`
- `public event PropertyChangedEventHandler? PropertyChanged;`
- `public BatchUpdateOperation BatchUpdate() => new BatchUpdateOperation(this);`
- `public void BeginBatchUpdate() {`
- `public void EndBatchUpdate() {`
- `public bool IsSelected(int index) {`
- `public void Select(int index) => SelectRange(index, index, false, true);`
- `public void Deselect(int index) => DeselectRange(index, index);`
- `public void SelectRange(int start, int end) => SelectRange(start, end, false, false);`
- `public void DeselectRange(int start, int end) {`
- `public void SelectAll() => SelectRange(0, int.MaxValue);`
- `public void Clear() => DeselectRange(0, int.MaxValue);`
- `public record struct BatchUpdateOperation : IDisposable`
- `public BatchUpdateOperation(SelectionModel<T> owner) {`
- `public void Dispose() {`

### `src/Avalonia.Controls/Selection/SelectionModelIndexesChangedEventArgs.cs`
- `public class SelectionModelIndexesChangedEventArgs : EventArgs`
- `public SelectionModelIndexesChangedEventArgs(int startIndex, int delta) {`
- `public int StartIndex { get; }`
- `public int Delta { get; }`

### `src/Avalonia.Controls/Selection/SelectionModelSelectionChangedEventArgs.cs`
- `public abstract class SelectionModelSelectionChangedEventArgs : EventArgs`
- `public abstract IReadOnlyList<int> DeselectedIndexes { get; }`
- `public abstract IReadOnlyList<int> SelectedIndexes { get; }`
- `public IReadOnlyList<object?> DeselectedItems => GetUntypedDeselectedItems();`
- `public IReadOnlyList<object?> SelectedItems => GetUntypedSelectedItems();`
- `public class SelectionModelSelectionChangedEventArgs<T> : SelectionModelSelectionChangedEventArgs`
- `public SelectionModelSelectionChangedEventArgs( IReadOnlyList<int>? deselectedIndices = null, IReadOnlyList<int>? selectedIndices = null, IReadOnlyList<T?>? deselectedItems = null, IReadOnlyList<T?>? selectedItems = null) {`
- `public override IReadOnlyList<int> DeselectedIndexes { get; }`
- `public override IReadOnlyList<int> SelectedIndexes { get; }`
- `public new IReadOnlyList<T?> DeselectedItems { get; }`
- `public new IReadOnlyList<T?> SelectedItems { get; }`

### `src/Avalonia.Controls/Selection/SelectionNodeBase.cs`
- `public abstract class SelectionNodeBase<T>`

### `src/Avalonia.Controls/SelectionChangedEventArgs.cs`
- `public class SelectionChangedEventArgs : RoutedEventArgs`
- `public SelectionChangedEventArgs(RoutedEvent routedEvent, IList removedItems, IList addedItems) : base(routedEvent) {`
- `public IList AddedItems { get; }`
- `public IList RemovedItems { get; }`

### `src/Avalonia.Controls/SelectionMode.cs`
- `public enum SelectionMode`

### `src/Avalonia.Controls/Separator.cs`
- `public class Separator : TemplatedControl`

### `src/Avalonia.Controls/Shapes/Arc.cs`
- `public class Arc : Shape`
- `public static readonly StyledProperty<double> StartAngleProperty = AvaloniaProperty.Register<Arc, double>(nameof(StartAngle), 0.0);`
- `public static readonly StyledProperty<double> SweepAngleProperty = AvaloniaProperty.Register<Arc, double>(nameof(SweepAngle), 0.0);`
- `public double StartAngle {`
- `public double SweepAngle {`

### `src/Avalonia.Controls/Shapes/Ellipse.cs`
- `public class Ellipse : Shape`

### `src/Avalonia.Controls/Shapes/Line.cs`
- `public class Line : Shape`
- `public static readonly StyledProperty<Point> StartPointProperty = AvaloniaProperty.Register<Line, Point>(nameof(StartPoint));`
- `public static readonly StyledProperty<Point> EndPointProperty = AvaloniaProperty.Register<Line, Point>(nameof(EndPoint));`
- `public Point StartPoint {`
- `public Point EndPoint {`

### `src/Avalonia.Controls/Shapes/Path.cs`
- `public class Path : Shape`
- `public static readonly StyledProperty<Geometry?> DataProperty = AvaloniaProperty.Register<Path, Geometry?>(nameof(Data));`
- `public Geometry? Data {`

### `src/Avalonia.Controls/Shapes/Polygon.cs`
- `public class Polygon : Shape`
- `public static readonly StyledProperty<IList<Point>> PointsProperty = AvaloniaProperty.Register<Polygon, IList<Point>>("Points");`
- `public static readonly StyledProperty<FillRule> FillRuleProperty = AvaloniaProperty.Register<Polygon, FillRule>(nameof(FillRule));`
- `public Polygon() {`
- `public IList<Point> Points {`
- `public FillRule FillRule {`

### `src/Avalonia.Controls/Shapes/Polyline.cs`
- `public class Polyline : Shape`
- `public static readonly StyledProperty<IList<Point>> PointsProperty = AvaloniaProperty.Register<Polyline, IList<Point>>("Points");`
- `public static readonly StyledProperty<FillRule> FillRuleProperty = AvaloniaProperty.Register<Polyline, FillRule>(nameof(FillRule));`
- `public Polyline() {`
- `public IList<Point> Points {`
- `public FillRule FillRule {`

### `src/Avalonia.Controls/Shapes/Rectangle.cs`
- `public class Rectangle : Shape`
- `public static readonly StyledProperty<double> RadiusXProperty = AvaloniaProperty.Register<Rectangle, double>(nameof(RadiusX));`
- `public static readonly StyledProperty<double> RadiusYProperty = AvaloniaProperty.Register<Rectangle, double>(nameof(RadiusY));`
- `public double RadiusX {`
- `public double RadiusY {`

### `src/Avalonia.Controls/Shapes/Sector.cs`
- `public class Sector : Shape`
- `public static readonly StyledProperty<double> StartAngleProperty = AvaloniaProperty.Register<Sector, double>(nameof(StartAngle), 0.0d);`
- `public static readonly StyledProperty<double> SweepAngleProperty = AvaloniaProperty.Register<Sector, double>(nameof(SweepAngle), 0.0d);`
- `public double StartAngle {`
- `public double SweepAngle {`

### `src/Avalonia.Controls/Shapes/Shape.cs`
- `public abstract class Shape : Control`
- `public static readonly StyledProperty<IBrush?> FillProperty = AvaloniaProperty.Register<Shape, IBrush?>(nameof(Fill));`
- `public static readonly StyledProperty<Stretch> StretchProperty = AvaloniaProperty.Register<Shape, Stretch>(nameof(Stretch));`
- `public static readonly StyledProperty<IBrush?> StrokeProperty = AvaloniaProperty.Register<Shape, IBrush?>(nameof(Stroke));`
- `public static readonly StyledProperty<AvaloniaList<double>?> StrokeDashArrayProperty = AvaloniaProperty.Register<Shape, AvaloniaList<double>?>(nameof(StrokeDashArray));`
- `public static readonly StyledProperty<double> StrokeDashOffsetProperty = AvaloniaProperty.Register<Shape, double>(nameof(StrokeDashOffset));`
- `public static readonly StyledProperty<double> StrokeThicknessProperty = AvaloniaProperty.Register<Shape, double>(nameof(StrokeThickness));`
- `public static readonly StyledProperty<PenLineCap> StrokeLineCapProperty = AvaloniaProperty.Register<Shape, PenLineCap>(nameof(StrokeLineCap), PenLineCap.Flat);`
- `public static readonly StyledProperty<PenLineJoin> StrokeJoinProperty = AvaloniaProperty.Register<Shape, PenLineJoin>(nameof(StrokeJoin), PenLineJoin.Miter);`
- `public static readonly StyledProperty<double> StrokeMiterLimitProperty = AvaloniaProperty.Register<Shape, double>(nameof(StrokeMiterLimit), 10.0);`
- `public Geometry? DefiningGeometry {`
- `public Geometry? RenderedGeometry {`
- `public IBrush? Fill {`
- `public Stretch Stretch {`
- `public IBrush? Stroke {`
- `public AvaloniaList<double>? StrokeDashArray {`
- `public double StrokeDashOffset {`
- `public double StrokeThickness {`
- `public PenLineCap StrokeLineCap {`
- `public PenLineJoin StrokeJoin {`
- `public double StrokeMiterLimit {`
- `public sealed override void Render(DrawingContext context) {`

### `src/Avalonia.Controls/ShutdownMode.cs`
- `public enum ShutdownMode`

### `src/Avalonia.Controls/SizeChangedEventArgs.cs`
- `public class SizeChangedEventArgs : RoutedEventArgs`
- `public SizeChangedEventArgs(RoutedEvent? routedEvent) : base (routedEvent) {`
- `public SizeChangedEventArgs(RoutedEvent? routedEvent, object? source) : base(routedEvent, source) {`
- `public SizeChangedEventArgs( RoutedEvent? routedEvent, object? source, Size previousSize, Size newSize) : base(routedEvent, source) {`
- `public bool HeightChanged => !MathUtilities.AreClose(NewSize.Height, PreviousSize.Height, LayoutHelper.LayoutEpsilon);`
- `public Size NewSize { get; init; }`
- `public Size PreviousSize { get; init; }`
- `public bool WidthChanged => !MathUtilities.AreClose(NewSize.Width, PreviousSize.Width, LayoutHelper.LayoutEpsilon);`

### `src/Avalonia.Controls/Slider.cs`
- `public enum TickPlacement`
- `public class Slider : RangeBase`
- `public static readonly StyledProperty<Orientation> OrientationProperty = ScrollBar.OrientationProperty.AddOwner<Slider>();`
- `public static readonly StyledProperty<bool> IsDirectionReversedProperty = Track.IsDirectionReversedProperty.AddOwner<Slider>();`
- `public static readonly StyledProperty<bool> IsSnapToTickEnabledProperty = AvaloniaProperty.Register<Slider, bool>(nameof(IsSnapToTickEnabled), false);`
- `public static readonly StyledProperty<double> TickFrequencyProperty = AvaloniaProperty.Register<Slider, double>(nameof(TickFrequency), 0.0);`
- `public static readonly StyledProperty<TickPlacement> TickPlacementProperty = AvaloniaProperty.Register<Slider, TickPlacement>(nameof(TickPlacement), 0d);`
- `public static readonly StyledProperty<AvaloniaList<double>?> TicksProperty = TickBar.TicksProperty.AddOwner<Slider>();`
- `public Slider() {`
- `public AvaloniaList<double>? Ticks {`
- `public Orientation Orientation {`
- `public bool IsDirectionReversed {`
- `public bool IsSnapToTickEnabled {`
- `public double TickFrequency {`
- `public TickPlacement TickPlacement {`

### `src/Avalonia.Controls/Spinner.cs`
- `public enum ValidSpinDirections`
- `public enum SpinDirection`
- `public class SpinEventArgs : RoutedEventArgs`
- `public SpinDirection Direction { get; }`
- `public bool UsingMouseWheel{ get; }`
- `public SpinEventArgs(SpinDirection direction) {`
- `public SpinEventArgs(RoutedEvent routedEvent, SpinDirection direction) : base(routedEvent) {`
- `public SpinEventArgs(SpinDirection direction, bool usingMouseWheel) {`
- `public SpinEventArgs(RoutedEvent routedEvent, SpinDirection direction, bool usingMouseWheel) : base(routedEvent) {`
- `public abstract class Spinner : ContentControl`
- `public static readonly StyledProperty<ValidSpinDirections> ValidSpinDirectionProperty = AvaloniaProperty.Register<Spinner, ValidSpinDirections>(nameof(ValidSpinDirection), ValidSpinDirections.Increase | ValidSpinDirections.Decrease);`
- `public static readonly RoutedEvent<SpinEventArgs> SpinEvent = RoutedEvent.Register<Spinner, SpinEventArgs>(nameof(Spin), RoutingStrategies.Bubble);`
- `public event EventHandler<SpinEventArgs>? Spin {`
- `public ValidSpinDirections ValidSpinDirection {`

### `src/Avalonia.Controls/SplitButton/SplitButton.cs`
- `public class SplitButton : ContentControl, ICommandSource, IClickableControl`
- `public event EventHandler<RoutedEventArgs>? Click {`
- `public static readonly RoutedEvent<RoutedEventArgs> ClickEvent = RoutedEvent.Register<SplitButton, RoutedEventArgs>( nameof(Click), RoutingStrategies.Bubble);`
- `public static readonly StyledProperty<ICommand?> CommandProperty = Button.CommandProperty.AddOwner<SplitButton>();`
- `public static readonly StyledProperty<object?> CommandParameterProperty = Button.CommandParameterProperty.AddOwner<SplitButton>();`
- `public static readonly StyledProperty<FlyoutBase?> FlyoutProperty = Button.FlyoutProperty.AddOwner<SplitButton>();`
- `public static readonly StyledProperty<KeyGesture?> HotKeyProperty = Button.HotKeyProperty.AddOwner<SplitButton>();`
- `public SplitButton() {`
- `public ICommand? Command {`
- `public object? CommandParameter {`
- `public FlyoutBase? Flyout {`
- `public KeyGesture? HotKey {`

### `src/Avalonia.Controls/SplitButton/ToggleSplitButton.cs`
- `public class ToggleSplitButton : SplitButton`
- `public event EventHandler<RoutedEventArgs>? IsCheckedChanged {`
- `public static readonly RoutedEvent<RoutedEventArgs> IsCheckedChangedEvent = RoutedEvent.Register<ToggleSplitButton, RoutedEventArgs>( nameof(IsCheckedChanged), RoutingStrategies.Bubble);`
- `public static readonly StyledProperty<bool> IsCheckedProperty = AvaloniaProperty.Register<ToggleSplitButton, bool>(nameof(IsChecked), false, defaultBindingMode: BindingMode.TwoWay);`
- `public ToggleSplitButton() {`
- `public bool IsChecked {`

### `src/Avalonia.Controls/SplitView/SplitView.cs`
- `public class SplitView : ContentControl`
- `public static readonly StyledProperty<double> CompactPaneLengthProperty = AvaloniaProperty.Register<SplitView, double>( nameof(CompactPaneLength), defaultValue: 48);`
- `public static readonly StyledProperty<SplitViewDisplayMode> DisplayModeProperty = AvaloniaProperty.Register<SplitView, SplitViewDisplayMode>( nameof(DisplayMode), defaultValue: SplitViewDisplayMode.Overlay);`
- `public static readonly StyledProperty<bool> IsPaneOpenProperty = AvaloniaProperty.Register<SplitView, bool>( nameof(IsPaneOpen), defaultValue: false, coerce: CoerceIsPaneOpen);`
- `public static readonly StyledProperty<double> OpenPaneLengthProperty = AvaloniaProperty.Register<SplitView, double>( nameof(OpenPaneLength), defaultValue: 320);`
- `public static readonly StyledProperty<IBrush?> PaneBackgroundProperty = AvaloniaProperty.Register<SplitView, IBrush?>(nameof(PaneBackground));`
- `public static readonly StyledProperty<SplitViewPanePlacement> PanePlacementProperty = AvaloniaProperty.Register<SplitView, SplitViewPanePlacement>(nameof(PanePlacement));`
- `public static readonly StyledProperty<object?> PaneProperty = AvaloniaProperty.Register<SplitView, object?>(nameof(Pane));`
- `public static readonly StyledProperty<IDataTemplate> PaneTemplateProperty = AvaloniaProperty.Register<SplitView, IDataTemplate>(nameof(PaneTemplate));`
- `public static readonly StyledProperty<bool> UseLightDismissOverlayModeProperty = AvaloniaProperty.Register<SplitView, bool>(nameof(UseLightDismissOverlayMode));`
- `public static readonly DirectProperty<SplitView, SplitViewTemplateSettings> TemplateSettingsProperty = AvaloniaProperty.RegisterDirect<SplitView, SplitViewTemplateSettings>(nameof(TemplateSettings), x => x.TemplateSettings);`
- `public static readonly RoutedEvent<RoutedEventArgs> PaneClosedEvent = RoutedEvent.Register<SplitView, RoutedEventArgs>( nameof(PaneClosed), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<CancelRoutedEventArgs> PaneClosingEvent = RoutedEvent.Register<SplitView, CancelRoutedEventArgs>( nameof(PaneClosing), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<RoutedEventArgs> PaneOpenedEvent = RoutedEvent.Register<SplitView, RoutedEventArgs>( nameof(PaneOpened), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<CancelRoutedEventArgs> PaneOpeningEvent = RoutedEvent.Register<SplitView, CancelRoutedEventArgs>( nameof(PaneOpening), RoutingStrategies.Bubble);`
- `public double CompactPaneLength {`
- `public SplitViewDisplayMode DisplayMode {`
- `public bool IsPaneOpen {`
- `public double OpenPaneLength {`
- `public IBrush? PaneBackground {`
- `public SplitViewPanePlacement PanePlacement {`
- `public object? Pane {`
- `public IDataTemplate PaneTemplate {`
- `public bool UseLightDismissOverlayMode {`
- `public SplitViewTemplateSettings TemplateSettings {`
- `public event EventHandler<RoutedEventArgs>? PaneClosed {`
- `public event EventHandler<CancelRoutedEventArgs>? PaneClosing {`
- `public event EventHandler<RoutedEventArgs>? PaneOpened {`
- `public event EventHandler<CancelRoutedEventArgs>? PaneOpening {`

### `src/Avalonia.Controls/SplitView/SplitViewDisplayMode.cs`
- `public enum SplitViewDisplayMode`

### `src/Avalonia.Controls/SplitView/SplitViewPanePlacement.cs`
- `public enum SplitViewPanePlacement`

### `src/Avalonia.Controls/SplitView/SplitViewTemplateSettings.cs`
- `public class SplitViewTemplateSettings : AvaloniaObject`
- `public static readonly StyledProperty<double> ClosedPaneWidthProperty = AvaloniaProperty.Register<SplitViewTemplateSettings, double>(nameof(ClosedPaneWidth), 0d);`
- `public static readonly StyledProperty<GridLength> PaneColumnGridLengthProperty = AvaloniaProperty.Register<SplitViewTemplateSettings, GridLength>( nameof(PaneColumnGridLength));`
- `public static readonly StyledProperty<double> ClosedPaneHeightProperty = AvaloniaProperty.Register<SplitViewTemplateSettings, double>(nameof(ClosedPaneHeight), 0d);`
- `public static readonly StyledProperty<GridLength> PaneRowGridLengthProperty = AvaloniaProperty.Register<SplitViewTemplateSettings, GridLength>( nameof(PaneRowGridLength));`
- `public double ClosedPaneWidth {`
- `public GridLength PaneColumnGridLength {`
- `public double ClosedPaneHeight {`
- `public GridLength PaneRowGridLength {`

### `src/Avalonia.Controls/StackPanel.cs`
- `public class StackPanel : Panel, INavigableContainer, IScrollSnapPointsInfo`
- `public static readonly StyledProperty<double> SpacingProperty = AvaloniaProperty.Register<StackPanel, double>(nameof(Spacing));`
- `public static readonly StyledProperty<Orientation> OrientationProperty = AvaloniaProperty.Register<StackPanel, Orientation>(nameof(Orientation), Orientation.Vertical);`
- `public static readonly StyledProperty<bool> AreHorizontalSnapPointsRegularProperty = AvaloniaProperty.Register<StackPanel, bool>(nameof(AreHorizontalSnapPointsRegular));`
- `public static readonly StyledProperty<bool> AreVerticalSnapPointsRegularProperty = AvaloniaProperty.Register<StackPanel, bool>(nameof(AreVerticalSnapPointsRegular));`
- `public static readonly RoutedEvent<RoutedEventArgs> HorizontalSnapPointsChangedEvent = RoutedEvent.Register<StackPanel, RoutedEventArgs>( nameof(HorizontalSnapPointsChanged), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<RoutedEventArgs> VerticalSnapPointsChangedEvent = RoutedEvent.Register<StackPanel, RoutedEventArgs>( nameof(VerticalSnapPointsChanged), RoutingStrategies.Bubble);`
- `public double Spacing {`
- `public Orientation Orientation {`
- `public event EventHandler<RoutedEventArgs>? HorizontalSnapPointsChanged {`
- `public event EventHandler<RoutedEventArgs>? VerticalSnapPointsChanged {`
- `public bool AreHorizontalSnapPointsRegular {`
- `public bool AreVerticalSnapPointsRegular {`
- `public IReadOnlyList<double> GetIrregularSnapPoints(Orientation orientation, SnapPointsAlignment snapPointsAlignment) {`
- `public double GetRegularSnapPoints(Orientation orientation, SnapPointsAlignment snapPointsAlignment, out double offset) {`

### `src/Avalonia.Controls/SystemDialog.cs`
- `public abstract class FileDialog : FileSystemDialog`
- `public List<FileDialogFilter> Filters { get; set; } = new List<FileDialogFilter>();`
- `public string? InitialFileName { get; set; }`
- `public abstract class FileSystemDialog : SystemDialog`
- `public string? Directory { get; set; }`
- `public class SaveFileDialog : FileDialog`
- `public string? DefaultExtension { get; set; }`
- `public bool? ShowOverwritePrompt { get; set; }`
- `public async Task<string?> ShowAsync(Window parent) {`
- `public FilePickerSaveOptions ToFilePickerSaveOptions() {`
- `public class OpenFileDialog : FileDialog`
- `public bool AllowMultiple { get; set; }`
- `public Task<string[]?> ShowAsync(Window parent) {`
- `public FilePickerOpenOptions ToFilePickerOpenOptions() {`
- `public class OpenFolderDialog : FileSystemDialog`
- `public Task<string?> ShowAsync(Window parent) {`
- `public FolderPickerOpenOptions ToFolderPickerOpenOptions() {`
- `public abstract class SystemDialog`
- `public string? Title { get; set; }`
- `public class FileDialogFilter`
- `public string? Name { get; set; }`
- `public List<string> Extensions { get; set; } = new List<string>();`

### `src/Avalonia.Controls/SystemFontAppBuilderExtension.cs`
- `public static class SystemFontAppBuilderExtension`
- `public static AppBuilder WithSystemFontSource(this AppBuilder appBuilder, Uri fontSource) {`

### `src/Avalonia.Controls/TabControl.cs`
- `public class TabControl : SelectingItemsControl, IContentPresenterHost`
- `public static readonly StyledProperty<Dock> TabStripPlacementProperty = AvaloniaProperty.Register<TabControl, Dock>(nameof(TabStripPlacement), defaultValue: Dock.Top);`
- `public static readonly StyledProperty<HorizontalAlignment> HorizontalContentAlignmentProperty = ContentControl.HorizontalContentAlignmentProperty.AddOwner<TabControl>();`
- `public static readonly StyledProperty<VerticalAlignment> VerticalContentAlignmentProperty = ContentControl.VerticalContentAlignmentProperty.AddOwner<TabControl>();`
- `public static readonly StyledProperty<IDataTemplate?> ContentTemplateProperty = ContentControl.ContentTemplateProperty.AddOwner<TabControl>();`
- `public static readonly DirectProperty<TabControl, object?> SelectedContentProperty = AvaloniaProperty.RegisterDirect<TabControl, object?>(nameof(SelectedContent), o => o.SelectedContent);`
- `public static readonly DirectProperty<TabControl, IDataTemplate?> SelectedContentTemplateProperty = AvaloniaProperty.RegisterDirect<TabControl, IDataTemplate?>(nameof(SelectedContentTemplate), o => o.SelectedContentTemplate);`
- `public HorizontalAlignment HorizontalContentAlignment {`
- `public VerticalAlignment VerticalContentAlignment {`
- `public Dock TabStripPlacement {`
- `public IDataTemplate? ContentTemplate {`
- `public object? SelectedContent {`
- `public IDataTemplate? SelectedContentTemplate {`

### `src/Avalonia.Controls/TabItem.cs`
- `public class TabItem : HeaderedContentControl, ISelectable`
- `public static readonly DirectProperty<TabItem, Dock?> TabStripPlacementProperty = AvaloniaProperty.RegisterDirect<TabItem, Dock?>(nameof(TabStripPlacement), o => o.TabStripPlacement);`
- `public static readonly StyledProperty<bool> IsSelectedProperty = SelectingItemsControl.IsSelectedProperty.AddOwner<TabItem>();`
- `public Dock? TabStripPlacement {`
- `public bool IsSelected {`

### `src/Avalonia.Controls/Templates/DataTemplateExtensions.cs`
- `public static class DataTemplateExtensions`
- `public static IDataTemplate? FindDataTemplate( this Control control, object? data, IDataTemplate? primary = null) {`

### `src/Avalonia.Controls/Templates/DataTemplates.cs`
- `public class DataTemplates : AvaloniaList<IDataTemplate>, IAvaloniaListItemValidator<IDataTemplate>`
- `public DataTemplates() {`

### `src/Avalonia.Controls/Templates/FuncControlTemplate.cs`
- `public class FuncControlTemplate : FuncTemplate<TemplatedControl, Control>, IControlTemplate`
- `public FuncControlTemplate(Func<TemplatedControl, INameScope, Control> build) : base(build) {`
- `public new TemplateResult<Control> Build(TemplatedControl param) {`

### `src/Avalonia.Controls/Templates/FuncControlTemplate`2.cs`
- `public class FuncControlTemplate<T> : FuncControlTemplate where T : TemplatedControl`
- `public FuncControlTemplate(Func<T, INameScope, Control> build) : base((x, s) => build((T)x, s))`

### `src/Avalonia.Controls/Templates/FuncDataTemplate.cs`
- `public class FuncDataTemplate : FuncTemplate<object?, Control?>, IRecyclingDataTemplate`
- `public static readonly FuncDataTemplate Default = new FuncDataTemplate<object?>( (data, s) =>`
- `public static readonly FuncDataTemplate Access = new FuncDataTemplate<object>( (data, s) =>`
- `public FuncDataTemplate( Type type, Func<object?, INameScope, Control?> build, bool supportsRecycling = false) : this(o => IsInstance(o, type), build, supportsRecycling)`
- `public FuncDataTemplate( Func<object?, bool> match, Func<object?, INameScope, Control?> build, bool supportsRecycling = false) : base(build) {`
- `public bool Match(object? data) {`
- `public Control? Build(object? data, Control? existing) {`

### `src/Avalonia.Controls/Templates/FuncDataTemplate`1.cs`
- `public class FuncDataTemplate<T> : FuncDataTemplate`
- `public FuncDataTemplate(Func<T, INameScope, Control?> build, bool supportsRecycling = false) : base(o => TypeUtilities.CanCast<T>(o), CastBuild(build), supportsRecycling)`
- `public FuncDataTemplate( Func<T, bool> match, Func<T, INameScope, Control> build, bool supportsRecycling = false) : base(CastMatch(match), CastBuild(build), supportsRecycling) {`
- `public FuncDataTemplate( Func<T, bool> match, Func<T, Control> build, bool supportsRecycling = false) : this(match, (a, _) => build(a), supportsRecycling)`

### `src/Avalonia.Controls/Templates/FuncTemplateNameScopeExtensions.cs`
- `public static class FuncTemplateNameScopeExtensions`
- `public static T RegisterInNameScope<T>(this T control, INameScope scope) where T : StyledElement {`

### `src/Avalonia.Controls/Templates/FuncTemplate`1.cs`
- `public class FuncTemplate<TControl> : ITemplate<TControl> where TControl : Control?`
- `public FuncTemplate(Func<TControl> func) {`
- `public TControl Build() {`

### `src/Avalonia.Controls/Templates/FuncTemplate`2.cs`
- `public class FuncTemplate<TParam, TControl> : ITemplate<TParam, TControl>`
- `public FuncTemplate(Func<TParam, INameScope, TControl> func) {`
- `public TControl Build(TParam param) {`

### `src/Avalonia.Controls/Templates/FuncTreeDataTemplate.cs`
- `public class FuncTreeDataTemplate : FuncDataTemplate, ITreeDataTemplate`
- `public FuncTreeDataTemplate( Type type, Func<object?, INameScope, Control> build, Func<object?, IEnumerable> itemsSelector) : this(o => IsInstance(o, type), build, itemsSelector)`
- `public FuncTreeDataTemplate( Func<object?, bool> match, Func<object?, INameScope, Control?> build, Func<object?, IEnumerable> itemsSelector) : base(match, build) {`
- `public InstancedBinding ItemsSelector(object item) {`

### `src/Avalonia.Controls/Templates/FuncTreeDataTemplate`1.cs`
- `public class FuncTreeDataTemplate<T> : FuncTreeDataTemplate`
- `public FuncTreeDataTemplate( Func<T, INameScope, Control> build, Func<T, IEnumerable> itemsSelector) : base( typeof(T), Cast(build), Cast(itemsSelector)) {`
- `public FuncTreeDataTemplate( Func<T, bool> match, Func<T, INameScope, Control> build, Func<T, IEnumerable> itemsSelector) : base( CastMatch(match), Cast(build), Cast(itemsSelector)) {`

### `src/Avalonia.Controls/Templates/IControlTemplate.cs`
- `public interface IControlTemplate : ITemplate<TemplatedControl, TemplateResult<Control>?>`

### `src/Avalonia.Controls/Templates/IDataTemplate.cs`
- `public interface IDataTemplate : ITemplate<object?, Control?>`

### `src/Avalonia.Controls/Templates/IDataTemplateHost.cs`
- `public interface IDataTemplateHost`

### `src/Avalonia.Controls/Templates/IRecyclingDataTemplate.cs`
- `public interface IRecyclingDataTemplate : IDataTemplate`

### `src/Avalonia.Controls/Templates/ITemplate`1.cs`
- `public interface ITemplate<TControl> : ITemplate where TControl : Control?`

### `src/Avalonia.Controls/Templates/ITemplate`2.cs`
- `public interface ITemplate<TParam, TControl>`

### `src/Avalonia.Controls/Templates/ITreeDataTemplate.cs`
- `public interface ITreeDataTemplate : IDataTemplate`

### `src/Avalonia.Controls/Templates/ITypedDataTemplate.cs`
- Namespace: `Avalonia.Controls.Templates`
- `public interface ITypedDataTemplate : IDataTemplate`

### `src/Avalonia.Controls/Templates/TemplateExtensions.cs`
- `public static class TemplateExtensions`
- `public static IEnumerable<Control> GetTemplateChildren(this TemplatedControl control) {`

### `src/Avalonia.Controls/TextBlock.cs`
- `public class TextBlock : Control, IInlineHost`
- `public static readonly StyledProperty<IBrush?> BackgroundProperty = Border.BackgroundProperty.AddOwner<TextBlock>();`
- `public static readonly StyledProperty<Thickness> PaddingProperty = Decorator.PaddingProperty.AddOwner<TextBlock>();`
- `public static readonly StyledProperty<FontFamily> FontFamilyProperty = TextElement.FontFamilyProperty.AddOwner<TextBlock>();`
- `public static readonly StyledProperty<double> FontSizeProperty = TextElement.FontSizeProperty.AddOwner<TextBlock>();`
- `public static readonly StyledProperty<FontStyle> FontStyleProperty = TextElement.FontStyleProperty.AddOwner<TextBlock>();`
- `public static readonly StyledProperty<FontWeight> FontWeightProperty = TextElement.FontWeightProperty.AddOwner<TextBlock>();`
- `public static readonly StyledProperty<FontStretch> FontStretchProperty = TextElement.FontStretchProperty.AddOwner<TextBlock>();`
- `public static readonly StyledProperty<IBrush?> ForegroundProperty = TextElement.ForegroundProperty.AddOwner<TextBlock>();`
- `public static readonly AttachedProperty<double> BaselineOffsetProperty = AvaloniaProperty.RegisterAttached<TextBlock, Control, double>( nameof(BaselineOffset), 0, true);`
- `public static readonly AttachedProperty<double> LineHeightProperty = AvaloniaProperty.RegisterAttached<TextBlock, Control, double>( nameof(LineHeight), double.NaN, validate: IsValidLineHeight, inherits: true);`
- `public static readonly AttachedProperty<double> LineSpacingProperty = AvaloniaProperty.RegisterAttached<TextBlock, Control, double>( nameof(LineSpacing), 0, validate: IsValidLineSpacing, inherits: true);`
- `public static readonly AttachedProperty<double> LetterSpacingProperty = AvaloniaProperty.RegisterAttached<TextBlock, Control, double>( nameof(LetterSpacing), 0, inherits: true);`
- `public static readonly AttachedProperty<int> MaxLinesProperty = AvaloniaProperty.RegisterAttached<TextBlock, Control, int>( nameof(MaxLines), validate: IsValidMaxLines, inherits: true);`
- `public static readonly StyledProperty<string?> TextProperty = AvaloniaProperty.Register<TextBlock, string?>(nameof(Text));`
- `public static readonly AttachedProperty<TextAlignment> TextAlignmentProperty = AvaloniaProperty.RegisterAttached<TextBlock, Control, TextAlignment>( nameof(TextAlignment), defaultValue: TextAlignment.Start, inherits: true);`
- `public static readonly AttachedProperty<TextWrapping> TextWrappingProperty = AvaloniaProperty.RegisterAttached<TextBlock, Control, TextWrapping>(nameof(TextWrapping), inherits: true);`
- `public static readonly AttachedProperty<TextTrimming> TextTrimmingProperty = AvaloniaProperty.RegisterAttached<TextBlock, Control, TextTrimming>(nameof(TextTrimming), defaultValue: TextTrimming.None, inherits: true);`
- `public static readonly StyledProperty<TextDecorationCollection?> TextDecorationsProperty = Inline.TextDecorationsProperty.AddOwner<TextBlock>();`
- `public static readonly StyledProperty<FontFeatureCollection?> FontFeaturesProperty = TextElement.FontFeaturesProperty.AddOwner<TextBlock>();`
- `public static readonly DirectProperty<TextBlock, InlineCollection?> InlinesProperty = AvaloniaProperty.RegisterDirect<TextBlock, InlineCollection?>( nameof(Inlines), t => t.Inlines, (t, v) => t.Inlines = v);`
- `public TextBlock() {`
- `public TextLayout TextLayout => _textLayout ??= CreateTextLayout(Text);`
- `public Thickness Padding {`
- `public IBrush? Background {`
- `public string? Text {`
- `public FontFamily FontFamily {`
- `public double FontSize {`
- `public FontStyle FontStyle {`
- `public FontWeight FontWeight {`
- `public FontStretch FontStretch {`
- `public IBrush? Foreground {`
- `public double LineHeight {`
- `public double LineSpacing {`
- `public double LetterSpacing {`
- `public int MaxLines {`
- `public TextWrapping TextWrapping {`
- `public TextTrimming TextTrimming {`
- `public TextAlignment TextAlignment {`
- `public TextDecorationCollection? TextDecorations {`
- `public FontFeatureCollection? FontFeatures {`
- `public InlineCollection? Inlines {`
- `public double BaselineOffset {`
- `public static double GetBaselineOffset(Control control) {`
- `public static void SetBaselineOffset(Control control, double value) {`
- `public static TextAlignment GetTextAlignment(Control control) {`
- `public static void SetTextAlignment(Control control, TextAlignment alignment) {`
- `public static TextWrapping GetTextWrapping(Control control) {`
- `public static void SetTextWrapping(Control control, TextWrapping wrapping) {`
- `public static TextTrimming GetTextTrimming(Control control) {`
- `public static void SetTextTrimming(Control control, TextTrimming trimming) {`
- `public static double GetLineHeight(Control control) {`
- `public static void SetLineHeight(Control control, double height) {`
- `public static double GetLetterSpacing(Control control) {`
- `public static void SetLetterSpacing(Control control, double letterSpacing) {`
- `public static int GetMaxLines(Control control) {`
- `public static void SetMaxLines(Control control, int maxLines) {`
- `public sealed override void Render(DrawingContext context) {`

### `src/Avalonia.Controls/TextBox.cs`
- `public class TextBox : TemplatedControl, UndoRedoHelper<TextBox.UndoRedoState>.IUndoRedoHost`
- `public static KeyGesture? CutGesture => Application.Current?.PlatformSettings?.HotkeyConfiguration.Cut.FirstOrDefault();`
- `public static KeyGesture? CopyGesture => Application.Current?.PlatformSettings?.HotkeyConfiguration.Copy.FirstOrDefault();`
- `public static KeyGesture? PasteGesture => Application.Current?.PlatformSettings?.HotkeyConfiguration.Paste.FirstOrDefault();`
- `public static readonly StyledProperty<bool> IsInactiveSelectionHighlightEnabledProperty = AvaloniaProperty.Register<TextBox, bool>(nameof(IsInactiveSelectionHighlightEnabled), defaultValue: true);`
- `public static readonly StyledProperty<bool> ClearSelectionOnLostFocusProperty = AvaloniaProperty.Register<TextBox, bool>(nameof(ClearSelectionOnLostFocus), defaultValue: true);`
- `public static readonly StyledProperty<bool> AcceptsReturnProperty = AvaloniaProperty.Register<TextBox, bool>(nameof(AcceptsReturn));`
- `public static readonly StyledProperty<bool> AcceptsTabProperty = AvaloniaProperty.Register<TextBox, bool>(nameof(AcceptsTab));`
- `public static readonly StyledProperty<int> CaretIndexProperty = AvaloniaProperty.Register<TextBox, int>(nameof(CaretIndex), coerce: CoerceCaretIndex);`
- `public static readonly StyledProperty<bool> IsReadOnlyProperty = AvaloniaProperty.Register<TextBox, bool>(nameof(IsReadOnly));`
- `public static readonly StyledProperty<char> PasswordCharProperty = AvaloniaProperty.Register<TextBox, char>(nameof(PasswordChar));`
- `public static readonly StyledProperty<IBrush?> SelectionBrushProperty = AvaloniaProperty.Register<TextBox, IBrush?>(nameof(SelectionBrush));`
- `public static readonly StyledProperty<IBrush?> SelectionForegroundBrushProperty = AvaloniaProperty.Register<TextBox, IBrush?>(nameof(SelectionForegroundBrush));`
- `public static readonly StyledProperty<IBrush?> CaretBrushProperty = AvaloniaProperty.Register<TextBox, IBrush?>(nameof(CaretBrush));`
- `public static readonly StyledProperty<TimeSpan> CaretBlinkIntervalProperty = AvaloniaProperty.Register<TextBox, TimeSpan>(nameof(CaretBlinkInterval), defaultValue: TimeSpan.FromMilliseconds(500));`
- `public static readonly StyledProperty<int> SelectionStartProperty = AvaloniaProperty.Register<TextBox, int>(nameof(SelectionStart), coerce: CoerceCaretIndex);`
- `public static readonly StyledProperty<int> SelectionEndProperty = AvaloniaProperty.Register<TextBox, int>(nameof(SelectionEnd), coerce: CoerceCaretIndex);`
- `public static readonly StyledProperty<int> MaxLengthProperty = AvaloniaProperty.Register<TextBox, int>(nameof(MaxLength));`
- `public static readonly StyledProperty<int> MaxLinesProperty = AvaloniaProperty.Register<TextBox, int>(nameof(MaxLines));`
- `public static readonly StyledProperty<int> MinLinesProperty = AvaloniaProperty.Register<TextBox, int>(nameof(MinLines));`
- `public static readonly StyledProperty<string?> TextProperty = TextBlock.TextProperty.AddOwner<TextBox>(new( coerce: CoerceText, defaultBindingMode: BindingMode.TwoWay, enableDataValidation: true));`
- `public static readonly StyledProperty<TextAlignment> TextAlignmentProperty = TextBlock.TextAlignmentProperty.AddOwner<TextBox>();`
- `public static readonly StyledProperty<HorizontalAlignment> HorizontalContentAlignmentProperty = ContentControl.HorizontalContentAlignmentProperty.AddOwner<TextBox>();`
- `public static readonly StyledProperty<VerticalAlignment> VerticalContentAlignmentProperty = ContentControl.VerticalContentAlignmentProperty.AddOwner<TextBox>();`
- `public static readonly StyledProperty<TextWrapping> TextWrappingProperty = TextBlock.TextWrappingProperty.AddOwner<TextBox>();`
- `public static readonly StyledProperty<double> LineHeightProperty = TextBlock.LineHeightProperty.AddOwner<TextBox>(new(defaultValue: double.NaN));`
- `public static readonly StyledProperty<double> LetterSpacingProperty = TextBlock.LetterSpacingProperty.AddOwner<TextBox>();`
- `public static readonly StyledProperty<string?> WatermarkProperty = AvaloniaProperty.Register<TextBox, string?>(nameof(Watermark));`
- `public static readonly StyledProperty<bool> UseFloatingWatermarkProperty = AvaloniaProperty.Register<TextBox, bool>(nameof(UseFloatingWatermark));`
- `public static readonly StyledProperty<string> NewLineProperty = AvaloniaProperty.Register<TextBox, string>(nameof(NewLine), Environment.NewLine);`
- `public static readonly StyledProperty<object?> InnerLeftContentProperty = AvaloniaProperty.Register<TextBox, object?>(nameof(InnerLeftContent));`
- `public static readonly StyledProperty<object?> InnerRightContentProperty = AvaloniaProperty.Register<TextBox, object?>(nameof(InnerRightContent));`
- `public static readonly StyledProperty<bool> RevealPasswordProperty = AvaloniaProperty.Register<TextBox, bool>(nameof(RevealPassword));`
- `public static readonly DirectProperty<TextBox, bool> CanCutProperty = AvaloniaProperty.RegisterDirect<TextBox, bool>( nameof(CanCut), o => o.CanCut);`
- `public static readonly DirectProperty<TextBox, bool> CanCopyProperty = AvaloniaProperty.RegisterDirect<TextBox, bool>( nameof(CanCopy), o => o.CanCopy);`
- `public static readonly DirectProperty<TextBox, bool> CanPasteProperty = AvaloniaProperty.RegisterDirect<TextBox, bool>( nameof(CanPaste), o => o.CanPaste);`
- `public static readonly StyledProperty<bool> IsUndoEnabledProperty = AvaloniaProperty.Register<TextBox, bool>( nameof(IsUndoEnabled), defaultValue: true);`
- `public static readonly StyledProperty<int> UndoLimitProperty = AvaloniaProperty.Register<TextBox, int>(nameof(UndoLimit), UndoRedoHelper<UndoRedoState>.DefaultUndoLimit);`
- `public static readonly DirectProperty<TextBox, bool> CanUndoProperty = AvaloniaProperty.RegisterDirect<TextBox, bool>(nameof(CanUndo), x => x.CanUndo);`
- `public static readonly DirectProperty<TextBox, bool> CanRedoProperty = AvaloniaProperty.RegisterDirect<TextBox, bool>(nameof(CanRedo), x => x.CanRedo);`
- `public static readonly RoutedEvent<RoutedEventArgs> CopyingToClipboardEvent = RoutedEvent.Register<TextBox, RoutedEventArgs>( nameof(CopyingToClipboard), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<RoutedEventArgs> CuttingToClipboardEvent = RoutedEvent.Register<TextBox, RoutedEventArgs>( nameof(CuttingToClipboard), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<RoutedEventArgs> PastingFromClipboardEvent = RoutedEvent.Register<TextBox, RoutedEventArgs>( nameof(PastingFromClipboard), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<TextChangedEventArgs> TextChangedEvent = RoutedEvent.Register<TextBox, TextChangedEventArgs>( nameof(TextChanged), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<TextChangingEventArgs> TextChangingEvent = RoutedEvent.Register<TextBox, TextChangingEventArgs>( nameof(TextChanging), RoutingStrategies.Bubble);`
- `public TextBox() {`
- `public bool IsInactiveSelectionHighlightEnabled {`
- `public bool ClearSelectionOnLostFocus {`
- `public bool AcceptsReturn {`
- `public bool AcceptsTab {`
- `public int CaretIndex {`
- `public bool IsReadOnly {`
- `public char PasswordChar {`
- `public IBrush? SelectionBrush {`
- `public IBrush? SelectionForegroundBrush {`
- `public IBrush? CaretBrush {`
- `public TimeSpan CaretBlinkInterval {`
- `public int SelectionStart {`
- `public int SelectionEnd {`
- `public int MaxLength {`
- `public int MaxLines {`
- `public int MinLines {`
- `public double LetterSpacing {`
- `public double LineHeight {`
- `public string? Text {`
- `public string SelectedText {`
- `public HorizontalAlignment HorizontalContentAlignment {`
- `public VerticalAlignment VerticalContentAlignment {`
- `public TextAlignment TextAlignment {`
- `public string? Watermark {`
- `public bool UseFloatingWatermark {`
- `public object? InnerLeftContent {`
- `public object? InnerRightContent {`
- `public bool RevealPassword {`
- `public TextWrapping TextWrapping {`
- `public string NewLine {`
- `public void ClearSelection() {`
- `public bool CanCut {`
- `public bool CanCopy {`
- `public bool CanPaste {`
- `public bool IsUndoEnabled {`
- `public int UndoLimit {`
- `public bool CanUndo {`
- `public bool CanRedo {`
- `public int GetLineCount() {`
- `public event EventHandler<RoutedEventArgs>? CopyingToClipboard {`
- `public event EventHandler<RoutedEventArgs>? CuttingToClipboard {`
- `public event EventHandler<RoutedEventArgs>? PastingFromClipboard {`
- `public event EventHandler<TextChangedEventArgs>? TextChanged {`
- `public event EventHandler<TextChangingEventArgs>? TextChanging {`
- `public async void Cut() {`
- `public async void Copy() {`
- `public async void Paste() {`
- `public void Clear() => SetCurrentValue(TextProperty, string.Empty);`
- `public void ScrollToLine(int lineIndex) {`
- `public void SelectAll() {`
- `public void Undo() {`
- `public void Redo() {`

### `src/Avalonia.Controls/TextChangedEventArgs.cs`
- `public class TextChangedEventArgs : RoutedEventArgs`
- `public TextChangedEventArgs(RoutedEvent? routedEvent) : base (routedEvent) {`
- `public TextChangedEventArgs(RoutedEvent? routedEvent, Interactive? source) : base(routedEvent, source) {`

### `src/Avalonia.Controls/TextChangingEventArgs.cs`
- `public class TextChangingEventArgs : RoutedEventArgs`
- `public TextChangingEventArgs(RoutedEvent? routedEvent) : base (routedEvent) {`
- `public TextChangingEventArgs(RoutedEvent? routedEvent, Interactive? source) : base(routedEvent, source) {`

### `src/Avalonia.Controls/ThemeVariantScope.cs`
- `public class ThemeVariantScope : Decorator`
- `public static readonly StyledProperty<ThemeVariant> ActualThemeVariantProperty = ThemeVariant.ActualThemeVariantProperty.AddOwner<ThemeVariantScope>();`
- `public static readonly StyledProperty<ThemeVariant?> RequestedThemeVariantProperty = ThemeVariant.RequestedThemeVariantProperty.AddOwner<ThemeVariantScope>();`
- `public ThemeVariant? RequestedThemeVariant {`

### `src/Avalonia.Controls/TickBar.cs`
- `public enum TickBarPlacement`
- `public class TickBar : Control`
- `public static readonly StyledProperty<IBrush?> FillProperty = AvaloniaProperty.Register<TickBar, IBrush?>(nameof(Fill));`
- `public IBrush? Fill {`
- `public static readonly StyledProperty<double> MinimumProperty = AvaloniaProperty.Register<TickBar, double>(nameof(Minimum), 0d);`
- `public double Minimum {`
- `public static readonly StyledProperty<double> MaximumProperty = AvaloniaProperty.Register<TickBar, double>(nameof(Maximum), 0d);`
- `public double Maximum {`
- `public static readonly StyledProperty<double> TickFrequencyProperty = AvaloniaProperty.Register<TickBar, double>(nameof(TickFrequency), 0d);`
- `public double TickFrequency {`
- `public static readonly StyledProperty<Orientation> OrientationProperty = AvaloniaProperty.Register<TickBar, Orientation>(nameof(Orientation));`
- `public Orientation Orientation {`
- `public static readonly StyledProperty<AvaloniaList<double>?> TicksProperty = AvaloniaProperty.Register<TickBar, AvaloniaList<double>?>(nameof(Ticks));`
- `public AvaloniaList<double>? Ticks {`
- `public static readonly StyledProperty<bool> IsDirectionReversedProperty = AvaloniaProperty.Register<TickBar, bool>(nameof(IsDirectionReversed), false);`
- `public bool IsDirectionReversed {`
- `public static readonly StyledProperty<TickBarPlacement> PlacementProperty = AvaloniaProperty.Register<TickBar, TickBarPlacement>(nameof(Placement), 0d);`
- `public TickBarPlacement Placement {`
- `public static readonly StyledProperty<Rect> ReservedSpaceProperty = AvaloniaProperty.Register<TickBar, Rect>(nameof(ReservedSpace));`
- `public Rect ReservedSpace {`
- `public sealed override void Render(DrawingContext dc) {`

### `src/Avalonia.Controls/ToggleSwitch.cs`
- `public class ToggleSwitch : ToggleButton`
- `public static readonly StyledProperty<object?> OffContentProperty = AvaloniaProperty.Register<ToggleSwitch, object?>(nameof(OffContent), defaultValue: "Off");`
- `public static readonly StyledProperty<IDataTemplate?> OffContentTemplateProperty = AvaloniaProperty.Register<ToggleSwitch, IDataTemplate?>(nameof(OffContentTemplate));`
- `public static readonly StyledProperty<object?> OnContentProperty = AvaloniaProperty.Register<ToggleSwitch, object?>(nameof(OnContent), defaultValue: "On");`
- `public static readonly StyledProperty<IDataTemplate?> OnContentTemplateProperty = AvaloniaProperty.Register<ToggleSwitch, IDataTemplate?>(nameof(OnContentTemplate));`
- `public static readonly StyledProperty<Transitions> KnobTransitionsProperty = AvaloniaProperty.Register<ToggleSwitch, Transitions>(nameof(KnobTransitions));`
- `public object? OnContent {`
- `public object? OffContent {`
- `public ContentPresenter? OffContentPresenter {`
- `public ContentPresenter? OnContentPresenter {`
- `public IDataTemplate? OffContentTemplate {`
- `public IDataTemplate? OnContentTemplate {`
- `public Transitions KnobTransitions {`

### `src/Avalonia.Controls/ToolTip.cs`
- `public class ToolTip : ContentControl, IPopupHostProvider`
- `public static readonly AttachedProperty<object?> TipProperty = AvaloniaProperty.RegisterAttached<ToolTip, Control, object?>("Tip");`
- `public static readonly AttachedProperty<bool> IsOpenProperty = AvaloniaProperty.RegisterAttached<ToolTip, Control, bool>("IsOpen");`
- `public static readonly AttachedProperty<PlacementMode> PlacementProperty = AvaloniaProperty.RegisterAttached<ToolTip, Control, PlacementMode>("Placement", defaultValue: PlacementMode.Pointer);`
- `public static readonly AttachedProperty<double> HorizontalOffsetProperty = AvaloniaProperty.RegisterAttached<ToolTip, Control, double>("HorizontalOffset");`
- `public static readonly AttachedProperty<double> VerticalOffsetProperty = AvaloniaProperty.RegisterAttached<ToolTip, Control, double>("VerticalOffset", 20);`
- `public static readonly AttachedProperty<CustomPopupPlacementCallback?> CustomPopupPlacementCallbackProperty = AvaloniaProperty.RegisterAttached<ToolTip, Control, CustomPopupPlacementCallback?>("CustomPopupPlacementCallback");`
- `public static readonly AttachedProperty<int> ShowDelayProperty = AvaloniaProperty.RegisterAttached<ToolTip, Control, int>("ShowDelay", 400);`
- `public static readonly AttachedProperty<int> BetweenShowDelayProperty = AvaloniaProperty.RegisterAttached<ToolTip, Control, int>("BetweenShowDelay", 100);`
- `public static readonly AttachedProperty<bool> ShowOnDisabledProperty = AvaloniaProperty.RegisterAttached<ToolTip, Control, bool>("ShowOnDisabled", defaultValue: false, inherits: true);`
- `public static readonly AttachedProperty<bool> ServiceEnabledProperty = AvaloniaProperty.RegisterAttached<ToolTip, Control, bool>("ServiceEnabled", defaultValue: true, inherits: true);`
- `public static readonly RoutedEvent<CancelRoutedEventArgs> ToolTipOpeningEvent = RoutedEvent.Register<ToolTip, CancelRoutedEventArgs>("ToolTipOpening", RoutingStrategies.Direct);`
- `public static readonly RoutedEvent ToolTipClosingEvent = RoutedEvent.Register<ToolTip, RoutedEventArgs>("ToolTipClosing", RoutingStrategies.Direct);`
- `public static object? GetTip(Control element) {`
- `public static void SetTip(Control element, object? value) {`
- `public static bool GetIsOpen(Control element) {`
- `public static void SetIsOpen(Control element, bool value) {`
- `public static PlacementMode GetPlacement(Control element) {`
- `public static void SetPlacement(Control element, PlacementMode value) {`
- `public static double GetHorizontalOffset(Control element) {`
- `public static void SetHorizontalOffset(Control element, double value) {`
- `public static double GetVerticalOffset(Control element) {`
- `public static void SetVerticalOffset(Control element, double value) {`
- `public static int GetShowDelay(Control element) {`
- `public static void SetShowDelay(Control element, int value) {`
- `public static int GetBetweenShowDelay(Control element) => element.GetValue(BetweenShowDelayProperty);`
- `public static void SetBetweenShowDelay(Control element, int value) => element.SetValue(BetweenShowDelayProperty, value);`
- `public static bool GetShowOnDisabled(Control element) =>`
- `public static void SetShowOnDisabled(Control element, bool value) =>`
- `public static bool GetServiceEnabled(Control element) =>`
- `public static void SetServiceEnabled(Control element, bool value) =>`
- `public static void AddToolTipOpeningHandler(Control element, EventHandler<CancelRoutedEventArgs> handler) =>`
- `public static void RemoveToolTipOpeningHandler(Control element, EventHandler<CancelRoutedEventArgs> handler) =>`
- `public static void AddToolTipClosingHandler(Control element, EventHandler<RoutedEventArgs> handler) =>`
- `public static void RemoveToolTipClosingHandler(Control element, EventHandler<RoutedEventArgs> handler) =>`
- `public static CustomPopupPlacementCallback? GetCustomPopupPlacementCallback(Control element) {`
- `public static void SetCustomPopupPlacementCallback(Control element, CustomPopupPlacementCallback? value) {`

### `src/Avalonia.Controls/TopLevel.cs`
- `public abstract class TopLevel : ContentControl,`
- `public static readonly DirectProperty<TopLevel, Size> ClientSizeProperty = AvaloniaProperty.RegisterDirect<TopLevel, Size>(nameof(ClientSize), o => o.ClientSize);`
- `public static readonly DirectProperty<TopLevel, Size?> FrameSizeProperty = AvaloniaProperty.RegisterDirect<TopLevel, Size?>(nameof(FrameSize), o => o.FrameSize);`
- `public static readonly StyledProperty<IInputElement?> PointerOverElementProperty = AvaloniaProperty.Register<TopLevel, IInputElement?>(nameof(IInputRoot.PointerOverElement));`
- `public static readonly StyledProperty<IReadOnlyList<WindowTransparencyLevel>> TransparencyLevelHintProperty = AvaloniaProperty.Register<TopLevel, IReadOnlyList<WindowTransparencyLevel>>(nameof(TransparencyLevelHint), Array.Empty<WindowTransparencyLevel>());`
- `public static readonly DirectProperty<TopLevel, WindowTransparencyLevel> ActualTransparencyLevelProperty = AvaloniaProperty.RegisterDirect<TopLevel, WindowTransparencyLevel>(nameof(ActualTransparencyLevel), o => o.ActualTransparencyLevel,`
- `public static readonly StyledProperty<IBrush> TransparencyBackgroundFallbackProperty = AvaloniaProperty.Register<TopLevel, IBrush>(nameof(TransparencyBackgroundFallback), Brushes.White);`
- `public static readonly StyledProperty<ThemeVariant> ActualThemeVariantProperty = ThemeVariantScope.ActualThemeVariantProperty.AddOwner<TopLevel>();`
- `public static readonly StyledProperty<ThemeVariant?> RequestedThemeVariantProperty = ThemeVariantScope.RequestedThemeVariantProperty.AddOwner<TopLevel>();`
- `public static readonly AttachedProperty<SolidColorBrush?> SystemBarColorProperty = AvaloniaProperty.RegisterAttached<TopLevel, Control, SolidColorBrush?>( "SystemBarColor", inherits: true);`
- `public static readonly AttachedProperty<bool> AutoSafeAreaPaddingProperty = AvaloniaProperty.RegisterAttached<TopLevel, Control, bool>( "AutoSafeAreaPadding", defaultValue: true);`
- `public static readonly RoutedEvent<RoutedEventArgs> BackRequestedEvent = RoutedEvent.Register<TopLevel, RoutedEventArgs>(nameof(BackRequested), RoutingStrategies.Bubble);`
- `public TopLevel(ITopLevelImpl impl) : this(impl, AvaloniaLocator.Current) {`
- `public TopLevel(ITopLevelImpl impl, IAvaloniaDependencyResolver? dependencyResolver) {`
- `public event EventHandler? Opened;`
- `public event EventHandler? Closed;`
- `public event EventHandler? ScalingChanged;`
- `public Size ClientSize {`
- `public Size? FrameSize {`
- `public IReadOnlyList<WindowTransparencyLevel> TransparencyLevelHint {`
- `public WindowTransparencyLevel ActualTransparencyLevel {`
- `public IBrush TransparencyBackgroundFallback {`
- `public ThemeVariant? RequestedThemeVariant {`
- `public event EventHandler<RoutedEventArgs> BackRequested {`
- `public ITopLevelImpl? PlatformImpl { get; private set; }`
- `public IPlatformHandle? TryGetPlatformHandle() => PlatformImpl?.Handle;`
- `public RendererDiagnostics RendererDiagnostics => Renderer.Diagnostics;`
- `public static void SetSystemBarColor(Control control, SolidColorBrush? color) {`
- `public static SolidColorBrush? GetSystemBarColor(Control control) {`
- `public static void SetAutoSafeAreaPadding(Control control, bool value) {`
- `public static bool GetAutoSafeAreaPadding(Control control) {`
- `public double RenderScaling => _scaling;`
- `public IStorageProvider StorageProvider => _storageProvider`
- `public IInsetsManager? InsetsManager => PlatformImpl?.TryGetFeature<IInsetsManager>();`
- `public IInputPane? InputPane => PlatformImpl?.TryGetFeature<IInputPane>();`
- `public ILauncher Launcher => PlatformImpl?.TryGetFeature<ILauncher>() ?? new NoopLauncher();`
- `public Screens? Screens => _screens ??=`
- `public IClipboard? Clipboard => PlatformImpl?.TryGetFeature<IClipboard>();`
- `public IFocusManager? FocusManager => AvaloniaLocator.Current.GetService<IFocusManager>();`
- `public IPlatformSettings? PlatformSettings => AvaloniaLocator.Current.GetService<IPlatformSettings>();`
- `public static TopLevel? GetTopLevel(Visual? visual) {`
- `public async Task<IDisposable> RequestPlatformInhibition(PlatformInhibitionType type, string reason) {`
- `public void RequestAnimationFrame(Action<TimeSpan> action) {`

### `src/Avalonia.Controls/TransitionCompletedEventArgs.cs`
- Namespace: `Avalonia.Controls`
- `public class TransitionCompletedEventArgs : RoutedEventArgs`
- `public TransitionCompletedEventArgs(object? from, object? to, bool hasRunToCompletion) : base(TransitioningContentControl.TransitionCompletedEvent) {`
- `public object? From { get; }`
- `public object? To { get; }`
- `public bool HasRunToCompletion { get; }`

### `src/Avalonia.Controls/TransitioningContentControl.cs`
- Namespace: `Avalonia.Controls`
- `public class TransitioningContentControl : ContentControl`
- `public static readonly StyledProperty<IPageTransition?> PageTransitionProperty = AvaloniaProperty.Register<TransitioningContentControl, IPageTransition?>( nameof(PageTransition), defaultValue: new ImmutableCrossFade(TimeSpan.FromMilliseconds(125)));`
- `public static readonly StyledProperty<bool> IsTransitionReversedProperty = AvaloniaProperty.Register<TransitioningContentControl, bool>( nameof(IsTransitionReversed), defaultValue: false);`
- `public static readonly RoutedEvent<TransitionCompletedEventArgs> TransitionCompletedEvent = RoutedEvent.Register<TransitioningContentControl, TransitionCompletedEventArgs>( nameof(TransitionCompleted), RoutingStrategies.Direct);`
- `public IPageTransition? PageTransition {`
- `public bool IsTransitionReversed {`
- `public event EventHandler<TransitionCompletedEventArgs> TransitionCompleted {`

### `src/Avalonia.Controls/TrayIcon.cs`
- `public sealed class TrayIcons : AvaloniaList<TrayIcon>`
- `public class TrayIcon : AvaloniaObject, INativeMenuExporterProvider, IDisposable`
- `public TrayIcon() : this(PlatformManager.CreateTrayIcon()) {`
- `public event EventHandler? Clicked;`
- `public static readonly StyledProperty<ICommand?> CommandProperty = Button.CommandProperty.AddOwner<TrayIcon>(new(enableDataValidation: true));`
- `public static readonly StyledProperty<object?> CommandParameterProperty = Button.CommandParameterProperty.AddOwner<TrayIcon>();`
- `public static readonly AttachedProperty<TrayIcons?> IconsProperty = AvaloniaProperty.RegisterAttached<TrayIcon, Application, TrayIcons?>("Icons");`
- `public static readonly StyledProperty<NativeMenu?> MenuProperty = AvaloniaProperty.Register<TrayIcon, NativeMenu?>(nameof(Menu));`
- `public static readonly StyledProperty<WindowIcon?> IconProperty = Window.IconProperty.AddOwner<TrayIcon>();`
- `public static readonly StyledProperty<string?> ToolTipTextProperty = AvaloniaProperty.Register<TrayIcon, string?>(nameof(ToolTipText));`
- `public static readonly StyledProperty<bool> IsVisibleProperty = Visual.IsVisibleProperty.AddOwner<TrayIcon>();`
- `public static void SetIcons(Application o, TrayIcons? trayIcons) => o.SetValue(IconsProperty, trayIcons);`
- `public static TrayIcons? GetIcons(Application o) => o.GetValue(IconsProperty);`
- `public ICommand? Command {`
- `public object? CommandParameter {`
- `public NativeMenu? Menu {`
- `public WindowIcon? Icon {`
- `public string? ToolTipText {`
- `public bool IsVisible {`
- `public INativeMenuExporter? NativeMenuExporter => _impl?.MenuExporter;`
- `public void Dispose() => _impl?.Dispose();`

### `src/Avalonia.Controls/TreeView.cs`
- `public class TreeView : ItemsControl, ICustomKeyboardNavigation`
- `public static readonly StyledProperty<bool> AutoScrollToSelectedItemProperty = SelectingItemsControl.AutoScrollToSelectedItemProperty.AddOwner<TreeView>();`
- `public static readonly DirectProperty<TreeView, object?> SelectedItemProperty = SelectingItemsControl.SelectedItemProperty.AddOwner<TreeView>( o => o.SelectedItem,`
- `public static readonly DirectProperty<TreeView, IList> SelectedItemsProperty = AvaloniaProperty.RegisterDirect<TreeView, IList>( nameof(SelectedItems), o => o.SelectedItems,`
- `public static readonly StyledProperty<SelectionMode> SelectionModeProperty = ListBox.SelectionModeProperty.AddOwner<TreeView>();`
- `public event EventHandler<SelectionChangedEventArgs>? SelectionChanged {`
- `public new TreeItemContainerGenerator ItemContainerGenerator =>`
- `public bool AutoScrollToSelectedItem {`
- `public SelectionMode SelectionMode {`
- `public object? SelectedItem {`
- `public IList SelectedItems {`
- `public void ExpandSubTree(TreeViewItem item) {`
- `public void CollapseSubTree(TreeViewItem item) {`
- `public void SelectAll() {`
- `public void UnselectAll() {`
- `public IEnumerable<Control> GetRealizedTreeContainers() {`
- `public Control? TreeContainerFromItem(object item) {`
- `public object? TreeItemFromContainer(Control container) {`

### `src/Avalonia.Controls/TreeViewItem.cs`
- `public class TreeViewItem : HeaderedItemsControl, ISelectable`
- `public static readonly StyledProperty<bool> IsExpandedProperty = AvaloniaProperty.Register<TreeViewItem, bool>( nameof(IsExpanded), defaultBindingMode: BindingMode.TwoWay);`
- `public static readonly StyledProperty<bool> IsSelectedProperty = SelectingItemsControl.IsSelectedProperty.AddOwner<TreeViewItem>();`
- `public static readonly DirectProperty<TreeViewItem, int> LevelProperty = AvaloniaProperty.RegisterDirect<TreeViewItem, int>( nameof(Level), o => o.Level);`
- `public static readonly RoutedEvent<RoutedEventArgs> ExpandedEvent = RoutedEvent.Register<TreeViewItem, RoutedEventArgs>(nameof(Expanded), RoutingStrategies.Bubble | RoutingStrategies.Tunnel);`
- `public static readonly RoutedEvent<RoutedEventArgs> CollapsedEvent = RoutedEvent.Register<TreeViewItem, RoutedEventArgs>(nameof(Collapsed), RoutingStrategies.Bubble | RoutingStrategies.Tunnel);`
- `public bool IsExpanded {`
- `public bool IsSelected {`
- `public int Level {`
- `public event EventHandler<RoutedEventArgs>? Expanded {`
- `public event EventHandler<RoutedEventArgs>? Collapsed {`

### `src/Avalonia.Controls/UrlOpenedEventArgs.cs`
- `public class UrlOpenedEventArgs : EventArgs`
- `public UrlOpenedEventArgs(string[] urls) {`
- `public string[] Urls { get; }`

### `src/Avalonia.Controls/UserControl.cs`
- `public class UserControl : ContentControl`

### `src/Avalonia.Controls/Utils/AncestorFinder.cs`
- `public static class AncestorFinder`
- `public static IObservable<T?> Create<T>(StyledElement control) where T : StyledElement {`
- `public static IObservable<StyledElement?> Create(StyledElement control, Type ancestorType) {`

### `src/Avalonia.Controls/Utils/ISelectionAdapter.cs`
- `public interface ISelectionAdapter`

### `src/Avalonia.Controls/Utils/SelectingItemsControlSelectionAdapter.cs`
- `public class SelectingItemsControlSelectionAdapter : ISelectionAdapter`
- `public SelectingItemsControl? SelectorControl {`
- `public event EventHandler<SelectionChangedEventArgs>? SelectionChanged;`
- `public event EventHandler<RoutedEventArgs>? Commit;`
- `public event EventHandler<RoutedEventArgs>? Cancel;`
- `public SelectingItemsControlSelectionAdapter() {`
- `public SelectingItemsControlSelectionAdapter(SelectingItemsControl selector) {`
- `public object? SelectedItem {`
- `public IEnumerable? ItemsSource {`
- `public void HandleKeyDown(KeyEventArgs e) {`

### `src/Avalonia.Controls/Utils/UndoRedoHelper.cs`
- `public interface IUndoRedoHost`

### `src/Avalonia.Controls/Viewbox.cs`
- `public class Viewbox : Control`
- `public static readonly StyledProperty<Stretch> StretchProperty = AvaloniaProperty.Register<Viewbox, Stretch>(nameof(Stretch), Stretch.Uniform);`
- `public static readonly StyledProperty<StretchDirection> StretchDirectionProperty = AvaloniaProperty.Register<Viewbox, StretchDirection>(nameof(StretchDirection), StretchDirection.Both);`
- `public static readonly StyledProperty<Control?> ChildProperty = Decorator.ChildProperty.AddOwner<Viewbox>();`
- `public Viewbox() {`
- `public Stretch Stretch {`
- `public StretchDirection StretchDirection {`
- `public Control? Child {`

### `src/Avalonia.Controls/VirtualizingCarouselPanel.cs`
- `public class VirtualizingCarouselPanel : VirtualizingPanel, ILogicalScrollable`

### `src/Avalonia.Controls/VirtualizingPanel.cs`
- `public abstract class VirtualizingPanel : Panel, INavigableContainer`
- `public ItemContainerGenerator? ItemContainerGenerator => _itemsControl?.ItemContainerGenerator;`

### `src/Avalonia.Controls/VirtualizingStackPanel.cs`
- `public class VirtualizingStackPanel : VirtualizingPanel, IScrollSnapPointsInfo`
- `public static readonly StyledProperty<Orientation> OrientationProperty = StackPanel.OrientationProperty.AddOwner<VirtualizingStackPanel>();`
- `public static readonly StyledProperty<bool> AreHorizontalSnapPointsRegularProperty = AvaloniaProperty.Register<VirtualizingStackPanel, bool>(nameof(AreHorizontalSnapPointsRegular));`
- `public static readonly StyledProperty<bool> AreVerticalSnapPointsRegularProperty = AvaloniaProperty.Register<VirtualizingStackPanel, bool>(nameof(AreVerticalSnapPointsRegular));`
- `public static readonly RoutedEvent<RoutedEventArgs> HorizontalSnapPointsChangedEvent = RoutedEvent.Register<VirtualizingStackPanel, RoutedEventArgs>( nameof(HorizontalSnapPointsChanged), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<RoutedEventArgs> VerticalSnapPointsChangedEvent = RoutedEvent.Register<VirtualizingStackPanel, RoutedEventArgs>( nameof(VerticalSnapPointsChanged), RoutingStrategies.Bubble);`
- `public static readonly StyledProperty<double> CacheLengthProperty = AvaloniaProperty.Register<VirtualizingStackPanel, double>(nameof(CacheLength), 0.0, validate: v => v is >= 0 and <= 2);`
- `public VirtualizingStackPanel() {`
- `public Orientation Orientation {`
- `public event EventHandler<RoutedEventArgs>? HorizontalSnapPointsChanged {`
- `public event EventHandler<RoutedEventArgs>? VerticalSnapPointsChanged {`
- `public bool AreHorizontalSnapPointsRegular {`
- `public bool AreVerticalSnapPointsRegular {`
- `public double CacheLength {`
- `public int FirstRealizedIndex => _realizedElements?.FirstIndex ?? -1;`
- `public int LastRealizedIndex => _realizedElements?.LastIndex ?? -1;`
- `public IReadOnlyList<double> GetIrregularSnapPoints(Orientation orientation, SnapPointsAlignment snapPointsAlignment) {`
- `public double GetRegularSnapPoints(Orientation orientation, SnapPointsAlignment snapPointsAlignment, out double offset) {`

### `src/Avalonia.Controls/Window.cs`
- `public enum SizeToContent`
- `public enum SystemDecorations`
- `public enum WindowClosingBehavior`
- `public class Window : WindowBase, IFocusScope, ILayoutRoot`
- `public static readonly StyledProperty<SizeToContent> SizeToContentProperty = AvaloniaProperty.Register<Window, SizeToContent>(nameof(SizeToContent));`
- `public static readonly StyledProperty<bool> ExtendClientAreaToDecorationsHintProperty = AvaloniaProperty.Register<Window, bool>(nameof(ExtendClientAreaToDecorationsHint), false);`
- `public static readonly StyledProperty<ExtendClientAreaChromeHints> ExtendClientAreaChromeHintsProperty = AvaloniaProperty.Register<Window, ExtendClientAreaChromeHints>(nameof(ExtendClientAreaChromeHints), ExtendClientAreaChromeHints.Default);`
- `public static readonly StyledProperty<double> ExtendClientAreaTitleBarHeightHintProperty = AvaloniaProperty.Register<Window, double>(nameof(ExtendClientAreaTitleBarHeightHint), -1);`
- `public static readonly DirectProperty<Window, bool> IsExtendedIntoWindowDecorationsProperty = AvaloniaProperty.RegisterDirect<Window, bool>(nameof(IsExtendedIntoWindowDecorations), o => o.IsExtendedIntoWindowDecorations,`
- `public static readonly DirectProperty<Window, Thickness> WindowDecorationMarginProperty = AvaloniaProperty.RegisterDirect<Window, Thickness>(nameof(WindowDecorationMargin), o => o.WindowDecorationMargin);`
- `public static readonly DirectProperty<Window, Thickness> OffScreenMarginProperty = AvaloniaProperty.RegisterDirect<Window, Thickness>(nameof(OffScreenMargin), o => o.OffScreenMargin);`
- `public static readonly StyledProperty<SystemDecorations> SystemDecorationsProperty = AvaloniaProperty.Register<Window, SystemDecorations>(nameof(SystemDecorations), SystemDecorations.Full);`
- `public static readonly StyledProperty<bool> ShowActivatedProperty = AvaloniaProperty.Register<Window, bool>(nameof(ShowActivated), true);`
- `public static readonly StyledProperty<bool> ShowInTaskbarProperty = AvaloniaProperty.Register<Window, bool>(nameof(ShowInTaskbar), true);`
- `public static readonly StyledProperty<WindowClosingBehavior> ClosingBehaviorProperty = AvaloniaProperty.Register<Window, WindowClosingBehavior>(nameof(ClosingBehavior));`
- `public static readonly StyledProperty<WindowState> WindowStateProperty = AvaloniaProperty.Register<Window, WindowState>(nameof(WindowState));`
- `public static readonly StyledProperty<string?> TitleProperty = AvaloniaProperty.Register<Window, string?>(nameof(Title), "Window");`
- `public static readonly StyledProperty<WindowIcon?> IconProperty = AvaloniaProperty.Register<Window, WindowIcon?>(nameof(Icon));`
- `public static readonly StyledProperty<WindowStartupLocation> WindowStartupLocationProperty = AvaloniaProperty.Register<Window, WindowStartupLocation>(nameof(WindowStartupLocation));`
- `public static readonly StyledProperty<bool> CanResizeProperty = AvaloniaProperty.Register<Window, bool>(nameof(CanResize), true);`
- `public static readonly StyledProperty<bool> CanMinimizeProperty = AvaloniaProperty.Register<Window, bool>(nameof(CanMinimize), true);`
- `public static readonly StyledProperty<bool> CanMaximizeProperty = AvaloniaProperty.Register<Window, bool>(nameof(CanMaximize), true, coerce: CoerceCanMaximize);`
- `public static readonly RoutedEvent<RoutedEventArgs> WindowClosedEvent = RoutedEvent.Register<Window, RoutedEventArgs>("WindowClosed", RoutingStrategies.Direct);`
- `public static readonly RoutedEvent<RoutedEventArgs> WindowOpenedEvent = RoutedEvent.Register<Window, RoutedEventArgs>("WindowOpened", RoutingStrategies.Direct);`
- `public Window() : this(PlatformManager.CreateWindow()) {`
- `public Window(IWindowImpl impl) : base(impl) {`
- `public new IWindowImpl? PlatformImpl => (IWindowImpl?)base.PlatformImpl;`
- `public IReadOnlyList<Window> OwnedWindows => _children.Select(x => x.child).ToArray();`
- `public SizeToContent SizeToContent {`
- `public string? Title {`
- `public bool ExtendClientAreaToDecorationsHint {`
- `public ExtendClientAreaChromeHints ExtendClientAreaChromeHints {`
- `public double ExtendClientAreaTitleBarHeightHint {`
- `public bool IsExtendedIntoWindowDecorations {`
- `public Thickness WindowDecorationMargin {`
- `public Thickness OffScreenMargin {`
- `public SystemDecorations SystemDecorations {`
- `public bool ShowActivated {`
- `public bool ShowInTaskbar {`
- `public WindowClosingBehavior ClosingBehavior {`
- `public WindowState WindowState {`
- `public bool CanResize {`
- `public bool CanMinimize {`
- `public bool CanMaximize {`
- `public WindowIcon? Icon {`
- `public WindowStartupLocation WindowStartupLocation {`
- `public PixelPoint Position {`
- `public bool IsDialog => _showingAsDialog;`
- `public void BeginMoveDrag(PointerPressedEventArgs e) => PlatformImpl?.BeginMoveDrag(e);`
- `public void BeginResizeDrag(WindowEdge edge, PointerPressedEventArgs e) => PlatformImpl?.BeginResizeDrag(edge, e);`
- `public event EventHandler<WindowClosingEventArgs>? Closing;`
- `public void Close() {`
- `public void Close(object? dialogResult) {`
- `public override void Hide() {`
- `public override void Show() {`
- `public void Show(Window owner) {`
- `public Task ShowDialog(Window owner) {`
- `public Task<TResult> ShowDialog<TResult>(Window owner) => ShowCore<TResult>(owner, true)!;`
- `public static void SortWindowsByZOrder(Window[] windows) {`

### `src/Avalonia.Controls/WindowBase.cs`
- `public class WindowBase : TopLevel`
- `public static readonly DirectProperty<WindowBase, bool> IsActiveProperty = AvaloniaProperty.RegisterDirect<WindowBase, bool>(nameof(IsActive), o => o.IsActive);`
- `public static readonly DirectProperty<WindowBase, WindowBase?> OwnerProperty = AvaloniaProperty.RegisterDirect<WindowBase, WindowBase?>(nameof(Owner), o => o.Owner);`
- `public static readonly StyledProperty<bool> TopmostProperty = AvaloniaProperty.Register<WindowBase, bool>(nameof(Topmost));`
- `public WindowBase(IWindowBaseImpl impl) : this(impl, AvaloniaLocator.Current) {`
- `public WindowBase(IWindowBaseImpl impl, IAvaloniaDependencyResolver? dependencyResolver) : base(impl, dependencyResolver) {`
- `public event EventHandler? Activated;`
- `public event EventHandler? Deactivated;`
- `public event EventHandler<PixelPointEventArgs>? PositionChanged;`
- `public event EventHandler<WindowResizedEventArgs>? Resized;`
- `public new IWindowBaseImpl? PlatformImpl => (IWindowBaseImpl?) base.PlatformImpl;`
- `public bool IsActive {`
- `public new Screens Screens => base.Screens`
- `public WindowBase? Owner {`
- `public bool Topmost {`
- `public double DesktopScaling => DesktopScalingOverride ?? PlatformImpl?.DesktopScaling ?? 1;`
- `public void Activate() {`
- `public virtual void Hide() {`
- `public virtual void Show() {`

### `src/Avalonia.Controls/WindowClosingEventArgs.cs`
- `public enum WindowCloseReason`
- `public class WindowClosingEventArgs : CancelEventArgs`
- `public WindowCloseReason CloseReason { get; }`
- `public bool IsProgrammatic { get; }`

### `src/Avalonia.Controls/WindowEdge.cs`
- `public enum WindowEdge`

### `src/Avalonia.Controls/WindowIcon.cs`
- `public class WindowIcon`
- `public WindowIcon(Bitmap bitmap) {`
- `public WindowIcon(string fileName) {`
- `public WindowIcon(Stream stream) {`
- `public void Save(Stream stream) => PlatformImpl.Save(stream);`

### `src/Avalonia.Controls/WindowResizedEventArgs.cs`
- `public enum WindowResizeReason`
- `public class WindowResizedEventArgs : EventArgs`
- `public Size ClientSize { get; }`
- `public WindowResizeReason Reason { get; }`

### `src/Avalonia.Controls/WindowStartupLocation.cs`
- `public enum WindowStartupLocation`

### `src/Avalonia.Controls/WindowState.cs`
- `public enum WindowState`

### `src/Avalonia.Controls/WindowTransparencyLevel.cs`
- Namespace: `Avalonia.Controls`
- `public readonly record struct WindowTransparencyLevel`
- `public static WindowTransparencyLevel None { get; } = new(nameof(None));`
- `public static WindowTransparencyLevel Transparent { get; } = new(nameof(Transparent));`
- `public static WindowTransparencyLevel Blur { get; } = new(nameof(Blur));`
- `public static WindowTransparencyLevel AcrylicBlur { get; } = new(nameof(AcrylicBlur));`
- `public static WindowTransparencyLevel Mica { get; } = new(nameof(Mica));`
- `public override string ToString() {`
- `public class WindowTransparencyLevelCollection : ReadOnlyCollection<WindowTransparencyLevel>`
- `public WindowTransparencyLevelCollection(IList<WindowTransparencyLevel> list) : base(list) {`

### `src/Avalonia.Controls/WrapPanel.cs`
- `public enum WrapPanelItemsAlignment`
- `public class WrapPanel : Panel, INavigableContainer`
- `public static readonly StyledProperty<double> ItemSpacingProperty = AvaloniaProperty.Register<WrapPanel, double>(nameof(ItemSpacing));`
- `public static readonly StyledProperty<double> LineSpacingProperty = AvaloniaProperty.Register<WrapPanel, double>(nameof(LineSpacing));`
- `public static readonly StyledProperty<Orientation> OrientationProperty = AvaloniaProperty.Register<WrapPanel, Orientation>(nameof(Orientation), defaultValue: Orientation.Horizontal);`
- `public static readonly StyledProperty<WrapPanelItemsAlignment> ItemsAlignmentProperty = AvaloniaProperty.Register<WrapPanel, WrapPanelItemsAlignment>(nameof(ItemsAlignment), defaultValue: WrapPanelItemsAlignment.Start);`
- `public static readonly StyledProperty<double> ItemWidthProperty = AvaloniaProperty.Register<WrapPanel, double>(nameof(ItemWidth), double.NaN);`
- `public static readonly StyledProperty<double> ItemHeightProperty = AvaloniaProperty.Register<WrapPanel, double>(nameof(ItemHeight), double.NaN);`
- `public double ItemSpacing {`
- `public double LineSpacing {`
- `public Orientation Orientation {`
- `public WrapPanelItemsAlignment ItemsAlignment {`
- `public double ItemWidth {`
- `public double ItemHeight {`

## Browser Platform

### `src/Browser/Avalonia.Browser.Blazor/AvaloniaView.cs`
- Namespace: `Avalonia.Browser.Blazor`
- `public class AvaloniaView : ComponentBase`
- `public AvaloniaView() {`

### `src/Browser/Avalonia.Browser.Blazor/BlazorSingleViewLifetime.cs`
- Namespace: `Avalonia.Browser.Blazor`
- `public static class BlazorAppBuilder`
- `public static async Task StartBlazorAppAsync(this AppBuilder builder, BrowserPlatformOptions? options = null) {`

### `src/Browser/Avalonia.Browser/AvaloniaView.cs`
- `public class AvaloniaView`
- `public AvaloniaView(string divId) : this(DomHelper.GetElementById(divId, BrowserWindowingPlatform.GlobalThis) ?? throw new Exception($"Element with id '{divId}' was not found in the html document."))`
- `public AvaloniaView(JSObject host) {`
- `public Control? Content {`

### `src/Browser/Avalonia.Browser/BrowserAppBuilder.cs`
- Namespace: `Avalonia.Browser`
- `public enum BrowserRenderingMode`
- `public record BrowserPlatformOptions`
- `public IReadOnlyList<BrowserRenderingMode> RenderingMode { get; set; } = new[]`
- `public Func<string, string>? FrameworkAssetPathResolver { get; set; }`
- `public bool RegisterAvaloniaServiceWorker { get; set; }`
- `public string? AvaloniaServiceWorkerScope { get; set; }`
- `public bool PreferFileDialogPolyfill { get; set; }`
- `public bool? PreferManagedThreadDispatcher { get; set; } = true;`
- `public static class BrowserAppBuilder`
- `public static async Task StartBrowserAppAsync( this AppBuilder builder, string mainDivId, BrowserPlatformOptions? options = null) {`
- `public static async Task SetupBrowserAppAsync(this AppBuilder builder, BrowserPlatformOptions? options = null) {`
- `public static AppBuilder UseBrowser( this AppBuilder builder) {`

### `src/Browser/Avalonia.Browser/JSObjectControlHandle.cs`
- Namespace: `Avalonia.Browser`
- `public class JSObjectPlatformHandle : PlatformHandle`
- `public JSObject Object { get; }`
- `public class JSObjectControlHandle : JSObjectPlatformHandle, INativeControlHostDestroyableControlHandle`
- `public JSObjectControlHandle(JSObject reference) : base(reference) {`
- `public void Destroy() {`

## Desktop Bootstrap

### `src/Avalonia.Desktop/AppBuilderDesktopExtensions.cs`
- `public static class AppBuilderDesktopExtensions`
- `public static AppBuilder UsePlatformDetect(this AppBuilder builder) {`

## Headless Platform

### `src/Headless/Avalonia.Headless.NUnit/AvaloniaTest.cs`
- Namespace: `Avalonia.Headless.NUnit`
- `public sealed class AvaloniaTestAttribute : TestAttribute, IWrapSetUpTearDown`
- `public TestCommand Wrap(TestCommand command) {`

### `src/Headless/Avalonia.Headless.NUnit/AvaloniaTheory.cs`
- Namespace: `Avalonia.Headless.NUnit`
- `public sealed class AvaloniaTheoryAttribute : TheoryAttribute, IWrapSetUpTearDown`
- `public TestCommand Wrap(TestCommand command) {`

### `src/Headless/Avalonia.Headless.Vnc/HeadlessVncFramebufferSource.cs`
- `public class HeadlessVncFramebufferSource : IVncFramebufferSource`
- `public Window Window { get; set; }`
- `public VncFramebuffer _framebuffer = new VncFramebuffer("Avalonia", 1, 1, VncPixelFormat.RGB32);`
- `public HeadlessVncFramebufferSource(VncServerSession session, Window window) {`
- `public unsafe VncFramebuffer Capture() {`
- `public ExtendedDesktopSizeStatus SetDesktopSize(int width, int height) {`
- `public bool SupportsResizing => true;`

### `src/Headless/Avalonia.Headless.Vnc/HeadlessVncPlatformExtensions.cs`
- `public static class HeadlessVncPlatformExtensions`
- `public static int StartWithHeadlessVncPlatform( this AppBuilder builder, string host, int port, string[] args, ShutdownMode shutdownMode = ShutdownMode.OnLastWindowClose) {`
- `public static int StartWithHeadlessVncPlatform( this AppBuilder builder, string host, int port, string? password, string[] args, ShutdownMode shutdownMode = ShutdownMode.OnLastWindowClose) {`

### `src/Headless/Avalonia.Headless.XUnit/AvaloniaFact.cs`
- Namespace: `Avalonia.Headless.XUnit`
- `public sealed class AvaloniaFactAttribute : FactAttribute`
- `public class AvaloniaUIFactDiscoverer : FactDiscoverer`
- `public AvaloniaUIFactDiscoverer(IMessageSink diagnosticMessageSink) : base(diagnosticMessageSink) {`

### `src/Headless/Avalonia.Headless.XUnit/AvaloniaTestFrameworkAttribute.cs`
- Namespace: `Avalonia.Headless.XUnit`
- `public sealed class AvaloniaTestFrameworkAttribute : Attribute, ITestFrameworkAttribute`
- `public class AvaloniaTestFrameworkTypeDiscoverer : ITestFrameworkTypeDiscoverer`
- `public AvaloniaTestFrameworkTypeDiscoverer(IMessageSink _) {`
- `public Type GetTestFrameworkType(IAttributeInfo attribute) {`

### `src/Headless/Avalonia.Headless.XUnit/AvaloniaTheoryAttribute.cs`
- Namespace: `Avalonia.Headless.XUnit`
- `public sealed class AvaloniaTheoryAttribute : TheoryAttribute`
- `public class AvaloniaTheoryDiscoverer : TheoryDiscoverer`
- `public AvaloniaTheoryDiscoverer(IMessageSink diagnosticMessageSink) : base(diagnosticMessageSink) {`

### `src/Headless/Avalonia.Headless/AvaloniaHeadlessPlatform.cs`
- `public static class AvaloniaHeadlessPlatform`
- `public static void ForceRenderTimerTick(int count = 1) {`
- `public class AvaloniaHeadlessPlatformOptions`
- `public bool UseHeadlessDrawing { get; set; } = true;`
- `public PixelFormat FrameBufferFormat { get; set; } = PixelFormat.Rgba8888;`
- `public static class AvaloniaHeadlessPlatformExtensions`
- `public static AppBuilder UseHeadless(this AppBuilder builder, AvaloniaHeadlessPlatformOptions opts) {`

### `src/Headless/Avalonia.Headless/AvaloniaTestApplicationAttribute.cs`
- Namespace: `Avalonia.Headless`
- `public sealed class AvaloniaTestApplicationAttribute : Attribute`
- `public Type AppBuilderEntryPointType { get; }`
- `public AvaloniaTestApplicationAttribute( [DynamicallyAccessedMembers(HeadlessUnitTestSession.DynamicallyAccessed)] Type appBuilderEntryPointType) {`

### `src/Headless/Avalonia.Headless/HeadlessUnitTestIsolationAttribute.cs`
- Namespace: `Avalonia.Headless`
- `public enum AvaloniaTestIsolationLevel`
- `public sealed class AvaloniaTestIsolationAttribute(AvaloniaTestIsolationLevel isolationLevel) : Attribute`
- `public AvaloniaTestIsolationLevel IsolationLevel { get; } = isolationLevel;`

### `src/Headless/Avalonia.Headless/HeadlessUnitTestSession.cs`
- Namespace: `Avalonia.Headless`
- `public sealed class HeadlessUnitTestSession : IDisposable`
- `public Task Dispatch(Action action, CancellationToken cancellationToken) {`
- `public Task<TResult> Dispatch<TResult>(Func<TResult> action, CancellationToken cancellationToken) {`
- `public Task<TResult> Dispatch<TResult>(Func<Task<TResult>> action, CancellationToken cancellationToken) {`
- `public void Dispose() {`
- `public static HeadlessUnitTestSession StartNew( [DynamicallyAccessedMembers(DynamicallyAccessed)] Type entryPointType) {`
- `public static HeadlessUnitTestSession StartNew( [DynamicallyAccessedMembers(DynamicallyAccessed)] Type entryPointType, AvaloniaTestIsolationLevel isolationLevel) {`
- `public static HeadlessUnitTestSession GetOrStartForAssembly(Assembly? assembly) {`

### `src/Headless/Avalonia.Headless/HeadlessWindowExtensions.cs`
- Namespace: `Avalonia.Headless`
- `public static class HeadlessWindowExtensions`
- `public static WriteableBitmap? CaptureRenderedFrame(this TopLevel topLevel) {`
- `public static WriteableBitmap? GetLastRenderedFrame(this TopLevel topLevel) {`
- `public static void KeyPress(this TopLevel topLevel, Key key, RawInputModifiers modifiers) =>`
- `public static void KeyPress(this TopLevel topLevel, Key key, RawInputModifiers modifiers, PhysicalKey physicalKey, string? keySymbol) =>`
- `public static void KeyPressQwerty(this TopLevel topLevel, PhysicalKey physicalKey, RawInputModifiers modifiers) =>`
- `public static void KeyRelease(this TopLevel topLevel, Key key, RawInputModifiers modifiers) =>`
- `public static void KeyRelease(this TopLevel topLevel, Key key, RawInputModifiers modifiers, PhysicalKey physicalKey, string? keySymbol) =>`
- `public static void KeyReleaseQwerty(this TopLevel topLevel, PhysicalKey physicalKey, RawInputModifiers modifiers) =>`
- `public static void KeyTextInput(this TopLevel topLevel, string text) =>`
- `public static void MouseDown(this TopLevel topLevel, Point point, MouseButton button, RawInputModifiers modifiers = RawInputModifiers.None) =>`
- `public static void MouseMove(this TopLevel topLevel, Point point, RawInputModifiers modifiers = RawInputModifiers.None) =>`
- `public static void MouseUp(this TopLevel topLevel, Point point, MouseButton button, RawInputModifiers modifiers = RawInputModifiers.None) =>`
- `public static void MouseWheel(this TopLevel topLevel, Point point, Vector delta, RawInputModifiers modifiers = RawInputModifiers.None) =>`
- `public static void DragDrop(this TopLevel topLevel, Point point, RawDragEventType type, IDataObject data, DragDropEffects effects, RawInputModifiers modifiers = RawInputModifiers.None) =>`
- `public static void DragDrop(this TopLevel topLevel, Point point, RawDragEventType type, IDataTransfer data, DragDropEffects effects, RawInputModifiers modifiers = RawInputModifiers.None) =>`

## Linux Framebuffer

### `src/Linux/Avalonia.LinuxFramebuffer/DrmConnectorType.cs`
- `public enum DrmConnectorType : uint`

### `src/Linux/Avalonia.LinuxFramebuffer/DrmOutputOptions.cs`
- `public class DrmOutputOptions`
- `public double Scaling { get; set; } = 1.0;`
- `public bool EnableInitialBufferSwapping { get; set; } = true;`
- `public Color InitialBufferSwappingColor { get; set; } = new Color(0, 0, 0, 0);`
- `public PixelSize? VideoMode { get; set; }`
- `public DrmConnectorType? ConnectorType { get; set; }`
- `public uint? ConnectorTypeId { get; set; }`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/EvDev/EvDevBackend.cs`
- `public class EvDevBackend : IInputBackend`
- `public EvDevBackend(EvDevDeviceDescription[] devices) {`
- `public void Initialize(IScreenInfoProvider info, Action<RawInputEventArgs> onInput) {`
- `public void SetInputRoot(IInputRoot root) {`
- `public static EvDevBackend CreateFromEnvironment() {`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/EvDev/EvDevDeviceDescription.cs`
- `public abstract class EvDevDeviceDescription`
- `public string? Path { get; set; }`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/EvDev/EvDevTouchScreenDeviceDescription.cs`
- `public sealed class EvDevTouchScreenDeviceDescription : EvDevDeviceDescription`
- `public Matrix CalibrationMatrix { get; set; } = Matrix.Identity;`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/IInputBackend.cs`
- `public interface IInputBackend`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/IScreenInfoProvider.cs`
- `public interface IScreenInfoProvider`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/LibInput/LibInputBackend.Pointer.cs`
- Namespace: `Avalonia.LinuxFramebuffer.Input.LibInput`
- `public partial class LibInputBackend`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/LibInput/LibInputBackend.Touch.cs`
- Namespace: `Avalonia.LinuxFramebuffer.Input.LibInput`
- `public partial class LibInputBackend`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/LibInput/LibInputBackend.cs`
- `public partial class LibInputBackend : IInputBackend`
- `public LibInputBackend() {`
- `public LibInputBackend(LibInputBackendOptions options) {`
- `public void Initialize(IScreenInfoProvider screen, Action<RawInputEventArgs> onInput) {`
- `public void SetInputRoot(IInputRoot root) {`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/LibInput/LibInputBackendOptions.cs`
- Namespace: `Avalonia.LinuxFramebuffer.Input.LibInput`
- `public sealed record class LibInputBackendOptions`
- `public IReadOnlyList<string>? Events { get; init; } = null;`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/LibInput/LibInputNativeUnsafeMethods.cs`
- `public enum LibInputEventType`
- `public enum LibInputPointerAxisSource`
- `public enum LibInputPointerAxis`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/NullInput/NullInputBackend.cs`
- Namespace: `Avalonia.LinuxFramebuffer.Input.NullInput`
- `public class NullInputBackend : IInputBackend`
- `public void Initialize(IScreenInfoProvider screen, Action<RawInputEventArgs> onInput) {`
- `public void SetInputRoot(IInputRoot root) {`

### `src/Linux/Avalonia.LinuxFramebuffer/LinuxFramebufferPlatform.cs`
- `public static class LinuxFramebufferPlatformExtensions`
- `public static int StartLinuxFbDev(this AppBuilder builder, string[] args, string? fbdev = null, double scaling = 1, IInputBackend? inputBackend = default) => StartLinuxDirect(builder, args, new FbdevOutput(fileName: fbdev, format: null) { Scaling = scaling }, inputBackend);`
- `public static int StartLinuxFbDev(this AppBuilder builder, string[] args, string fbdev, PixelFormat? format, double scaling, IInputBackend? inputBackend = default) => StartLinuxDirect(builder, args, new FbdevOutput(fileName: fbdev, format: format) { Scaling = scaling }, inputBackend);`
- `public static int StartLinuxFbDev(this AppBuilder builder, string[] args, FbDevOutputOptions options, IInputBackend? inputBackend = default) => StartLinuxDirect(builder, args, new FbdevOutput(options), inputBackend);`
- `public static int StartLinuxDrm(this AppBuilder builder, string[] args, string? card = null, double scaling = 1, IInputBackend? inputBackend = default) => StartLinuxDirect(builder, args, new DrmOutput(card) { Scaling = scaling }, inputBackend);`
- `public static int StartLinuxDrm(this AppBuilder builder, string[] args, string? card = null, bool connectorsForceProbe = false, DrmOutputOptions? options = null, IInputBackend? inputBackend = default) => StartLinuxDirect(builder, args, new DrmOutput(card, connectorsForceProbe, options), inputBackend);`
- `public static int StartLinuxDirect(this AppBuilder builder, string[] args, IOutputBackend outputBackend, IInputBackend? inputBackend = default) {`

### `src/Linux/Avalonia.LinuxFramebuffer/LinuxFramebufferPlatformOptions.cs`
- `public class LinuxFramebufferPlatformOptions`
- `public int Fps { get; set; } = 60;`
- `public bool ShouldRenderOnUIThread { get; set; }`

### `src/Linux/Avalonia.LinuxFramebuffer/Output/Drm.cs`
- `public enum DrmModeConnection`
- `public enum DrmModeSubPixel{`
- `public struct DrmEventContext`
- `public int version;`
- `public IntPtr vblank_handler;`
- `public IntPtr page_flip_handler;`
- `public IntPtr page_flip_handler2;`
- `public IntPtr sequence_handler;`
- `public struct drmModeRes {`
- `public int count_fbs;`
- `public uint *fbs;`
- `public int count_crtcs;`
- `public uint *crtcs;`
- `public int count_connectors;`
- `public uint *connectors;`
- `public int count_encoders;`
- `public uint *encoders;`
- `public enum DrmModeType`
- `public struct drmModeModeInfo`
- `public uint clock;`
- `public ushort hdisplay, hsync_start, hsync_end, htotal, hskew;`
- `public ushort vdisplay, vsync_start, vsync_end, vtotal, vscan;`
- `public uint vrefresh;`
- `public uint flags;`
- `public DrmModeType type;`
- `public fixed byte name[32];`
- `public PixelSize Resolution => new PixelSize(hdisplay, vdisplay);`
- `public struct drmModeConnector {`
- `public uint connector_id;`
- `public uint encoder_id;`
- `public uint connector_type;`
- `public uint connector_type_id;`
- `public DrmModeConnection connection;`
- `public uint mmWidth, mmHeight;`
- `public DrmModeSubPixel subpixel;`
- `public int count_modes;`
- `public drmModeModeInfo* modes;`
- `public int count_props;`
- `public uint *props;`
- `public ulong *prop_values;`
- `public int count_encoders;`
- `public uint *encoders;`
- `public struct drmModeEncoder {`
- `public uint encoder_id;`
- `public uint encoder_type;`
- `public uint crtc_id;`
- `public uint possible_crtcs;`
- `public uint possible_clones;`
- `public struct drmModeCrtc {`
- `public uint crtc_id;`
- `public uint buffer_id;`
- `public uint x, y;`
- `public uint width, height;`
- `public int mode_valid;`
- `public drmModeModeInfo mode;`
- `public int gamma_size;`
- `public enum DrmModePageFlip`
- `public enum GbmBoFlags {`
- `public struct GbmBoHandle`
- `public void *ptr;`
- `public int s32;`
- `public uint u32;`
- `public long s64;`
- `public ulong u64;`
- `public static class GbmColorFormats`
- `public static uint FourCC(char a, char b, char c, char d) =>`
- `public static uint GBM_FORMAT_XRGB8888 { get; } = FourCC('X', 'R', '2', '4');`

### `src/Linux/Avalonia.LinuxFramebuffer/Output/DrmBindings.cs`
- `public unsafe class DrmConnector`
- `public DrmModeConnection Connection { get; }`
- `public uint Id { get; }`
- `public string Name { get; }`
- `public Size SizeMm { get; }`
- `public DrmModeSubPixel SubPixel { get; }`
- `public List<DrmModeInfo> Modes { get; } = new List<DrmModeInfo>();`
- `public DrmConnectorType ConnectorType { get; }`
- `public uint ConnectorTypeId { get; }`
- `public unsafe class DrmModeInfo`
- `public PixelSize Resolution => new PixelSize(Mode.hdisplay, Mode.vdisplay);`
- `public bool IsPreferred => Mode.type.HasAllFlags(DrmModeType.DRM_MODE_TYPE_PREFERRED);`
- `public string? Name { get; }`
- `public unsafe class DrmResources`
- `public List<DrmConnector> Connectors { get; } = new List<DrmConnector>();`
- `public DrmResources(int fd, bool connectorsForceProbe = false) {`
- `public unsafe class DrmCard : IDisposable`
- `public int Fd { get; private set; }`
- `public DrmCard(string? path = null) {`
- `public DrmCard(int fd) {`
- `public DrmResources GetResources(bool connectorsForceProbe = false) => new DrmResources(Fd, connectorsForceProbe);`
- `public void Dispose() {`

### `src/Linux/Avalonia.LinuxFramebuffer/Output/DrmOutput.cs`
- `public unsafe class DrmOutput : IGlOutputBackend, IGlPlatformSurface`
- `public PixelSize PixelSize => _mode.Resolution;`
- `public double Scaling {`
- `public IPlatformGraphics PlatformGraphics { get; private set; }`
- `public DrmOutput(DrmCard card, DrmResources resources, DrmConnector connector, DrmModeInfo modeInfo, DrmOutputOptions? options = null) {`
- `public DrmOutput(string? path = null, bool connectorsForceProbe = false, DrmOutputOptions? options = null) :this(new DrmCard(path), connectorsForceProbe, options) {`
- `public DrmOutput(DrmCard card, bool connectorsForceProbe = false, DrmOutputOptions? options = null) {`
- `public DrmOutput(DrmCard card, DrmResources resources, DrmConnector connector, DrmModeInfo modeInfo) {`
- `public IGlPlatformSurfaceRenderTarget CreateGlRenderTarget() => new RenderTarget(this);`
- `public IGlPlatformSurfaceRenderTarget CreateGlRenderTarget(IGlContext context) {`
- `public IGlContext CreateContext() {`

### `src/Linux/Avalonia.LinuxFramebuffer/Output/FbDevOutputOptions.cs`
- Namespace: `Avalonia.LinuxFramebuffer.Output`
- `public class FbDevOutputOptions`
- `public string? FileName { get; set; }`
- `public PixelFormat? PixelFormat { get; set; }`
- `public bool RenderDirectlyToMappedMemory { get; set; }`
- `public double Scaling { get; set; } = 1;`
- `public bool? UseAsyncFrontBufferBlit { get; set; }`

### `src/Linux/Avalonia.LinuxFramebuffer/Output/FbdevOutput.cs`
- `public sealed unsafe class FbdevOutput : IFramebufferPlatformSurface, IDisposable, IOutputBackend`
- `public double Scaling { get; set; }`
- `public FbdevOutput(string? fileName = null) : this(fileName, null) {`
- `public FbdevOutput(string? fileName, PixelFormat? format) : this(new FbDevOutputOptions() {`
- `public FbdevOutput(FbDevOutputOptions options) {`
- `public string Id { get; private set; }`
- `public PixelSize PixelSize {`
- `public ILockedFramebuffer Lock() => Lock(out _);`
- `public IFramebufferRenderTarget CreateFramebufferRenderTarget() => new FuncRetainedFramebufferRenderTarget(Lock);`
- `public void Dispose() {`

### `src/Linux/Avalonia.LinuxFramebuffer/Output/IGlOutputBackend.cs`
- `public interface IGlOutputBackend : IOutputBackend`
- `public IPlatformGraphics PlatformGraphics { get; }`

### `src/Linux/Avalonia.LinuxFramebuffer/Output/IOutputBackend.cs`
- `public interface IOutputBackend`

## Linux/X11 Platform

### `src/Avalonia.X11/Clipboard/ClipboardReadSession.cs`
- Namespace: `Avalonia.X11.Clipboard`
- `public class GetDataResult(byte[]? data, MemoryStream? stream, IntPtr actualTypeAtom)`
- `public IntPtr TypeAtom => actualTypeAtom;`
- `public byte[] AsBytes() => data ?? stream!.ToArray();`
- `public MemoryStream AsStream() => stream ?? new MemoryStream(data!);`

### `src/Avalonia.X11/Interop/GtkInteropHelper.cs`
- Namespace: `Avalonia.X11.Interop`
- `public class GtkInteropHelper`
- `public static async Task<T> RunOnGlibThread<T>(Func<T> cb) {`

### `src/Avalonia.X11/X11Platform.cs`
- `public enum X11RenderingMode`
- `public class X11PlatformOptions`
- `public IReadOnlyList<X11RenderingMode> RenderingMode { get; set; } = new[]`
- `public bool OverlayPopups { get; set; }`
- `public bool UseDBusMenu { get; set; } = true;`
- `public bool UseDBusFilePicker { get; set; } = true;`
- `public bool? EnableIme { get; set; } = true;`
- `public bool EnableInputFocusProxy { get; set; }`
- `public bool EnableSessionManagement { get; set; } =`
- `public bool ShouldRenderOnUIThread { get; set; }`
- `public IList<GlVersion> GlProfiles { get; set; } = new List<GlVersion>`
- `public IList<string> GlxRendererBlacklist { get; set; } = new List<string>`
- `public string? WmClass { get; set; }`
- `public bool? EnableMultiTouch { get; set; } = true;`
- `public bool? UseRetainedFramebuffer { get; set; }`
- `public bool UseGLibMainLoop { get; set; }`
- `public Action<Exception>? ExterinalGLibMainLoopExceptionLogger { get; set; }`
- `public X11PlatformOptions() {`
- `public static class AvaloniaX11PlatformExtensions`
- `public static AppBuilder UseX11(this AppBuilder builder) {`
- `public static void InitializeX11Platform(X11PlatformOptions? options = null) =>`

### `src/Avalonia.X11/X11WindowModes/DefaultWindowMode.cs`
- Namespace: `Avalonia.X11`
- `public class DefaultTopLevelWindowMode : X11WindowMode`
- `public override void Activate() {`
- `public override void Show(bool activate, bool isDialog) {`
- `public override void Hide() {`
- `public override Point PointToClient(PixelPoint point) => new Point(`
- `public override PixelPoint PointToScreen(Point point) => new PixelPoint(`

### `src/Avalonia.X11/X11WindowModes/InputProxyWindowMode.cs`
- Namespace: `Avalonia.X11`
- `public class InputProxyWindowMode : DefaultTopLevelWindowMode`
- `public override void OnHandleCreated(IntPtr handle) {`
- `public override bool OnEvent(ref XEvent ev) {`
- `public override void OnDestroyNotify() {`
- `public override void AppendWmProtocols(List<IntPtr> data) {`

### `src/Avalonia.X11/X11WindowModes/WindowMode.cs`
- Namespace: `Avalonia.X11`
- `public abstract class X11WindowMode`
- `public X11Window Window { get; private set; } = null!;`
- `public virtual bool BlockInput => false;`
- `public void Init(X11Window window) {`
- `public virtual bool OnEvent(ref XEvent ev) {`
- `public virtual void Activate() {`
- `public virtual void OnHandleCreated(IntPtr handle) {`
- `public virtual void OnDestroyNotify() {`
- `public virtual void AppendWmProtocols(List<IntPtr> data) {`
- `public virtual void Show(bool activate, bool isDialog) {`
- `public abstract PixelPoint PointToScreen(Point pt);`
- `public abstract Point PointToClient(PixelPoint pt);`
- `public virtual void Hide() {`

### `src/Avalonia.X11/X11WindowModes/XEmbedClientWindowMode.cs`
- Namespace: `Avalonia.X11`
- `public class XEmbedClientWindowMode : X11WindowMode`
- `public override bool BlockInput => _disabled;`
- `public double Scaling {`
- `public override void OnHandleCreated(IntPtr handle) {`
- `public override bool OnEvent(ref XEvent ev) {`
- `public void ProcessInteractiveResize(PixelSize size) {`
- `public override Point PointToClient(PixelPoint point) {`
- `public override PixelPoint PointToScreen(Point point) =>`

### `src/Avalonia.X11/XEmbedPlug.cs`
- Namespace: `Avalonia.X11`
- `public class XEmbedPlug : IDisposable`
- `public IntPtr Handle =>`
- `public object? Content {`
- `public Color BackgroundColor {`
- `public double ScaleFactor {`
- `public void ProcessInteractiveResize(PixelSize size) {`
- `public void Dispose() {`
- `public static XEmbedPlug Create() => new(null);`
- `public static XEmbedPlug Create(IntPtr embedderXid) =>`

## Other

### `src/Avalonia.Build.Tasks/CompileAvaloniaXamlTask.cs`
- `public class CompileAvaloniaXamlTask: ITask`
- `public const string AvaloniaCompileOutputMetadataName = "AvaloniaCompileOutput";`
- `public bool Execute() {`
- `public string ProjectDirectory { get; set; }`
- `public ITaskItem AssemblyFile { get; set; }`
- `public ITaskItem? RefAssemblyFile { get; set; }`
- `public ITaskItem[]? References { get; set; }`
- `public bool VerifyIl { get; set; }`
- `public bool DefaultCompileBindings { get; set; }`
- `public bool SkipXamlCompilation { get; set; }`
- `public string AssemblyOriginatorKeyFile { get; set; }`
- `public bool SignAssembly { get; set; }`
- `public bool DelaySign { get; set; }`
- `public string ReportImportance { get; set; }`
- `public IBuildEngine BuildEngine { get; set; }`
- `public ITaskHost HostObject { get; set; }`
- `public bool DebuggerLaunch { get; set; }`
- `public bool CreateSourceInfo { get; set; }`
- `public bool VerboseExceptions { get; set; }`
- `public ITaskItem[] AnalyzerConfigFiles { get; set; }`

### `src/Avalonia.Build.Tasks/DeterministicIdGenerator.cs`
- `public class DeterministicIdGenerator : IXamlIdentifierGenerator`
- `public string GenerateIdentifierPart() => (_nextId++).ToString();`

### `src/Avalonia.Build.Tasks/GenerateAvaloniaResourcesTask.cs`
- `public class GenerateAvaloniaResourcesTask : ITask`
- `public ITaskItem[] Resources { get; set; }`
- `public string Root { get; set; }`
- `public string Output { get; set; }`
- `public string ReportImportance { get; set; }`
- `public bool Execute() {`
- `public IBuildEngine BuildEngine { get; set; }`
- `public ITaskHost HostObject { get; set; }`

### `src/Avalonia.Build.Tasks/XamlCompilerDiagnosticsFilter.cs`
- Namespace: `Avalonia.Build.Tasks`
- `public class XamlCompilerDiagnosticsFilter`
- `public XamlCompilerDiagnosticsFilter( ITaskItem[]? analyzerConfigFiles) {`

### `src/Avalonia.Build.Tasks/XamlCompilerTaskExecutor.Helpers.cs`
- `public static partial class XamlCompilerTaskExecutor`

### `src/Avalonia.Build.Tasks/XamlCompilerTaskExecutor.cs`
- `public static partial class XamlCompilerTaskExecutor`
- `public class CompileResult`
- `public bool Success { get; set; }`
- `public bool WrittenFile { get; }`
- `public CompileResult(bool success, bool writtenFile = false) {`

### `src/Avalonia.Build.Tasks/XamlFileInfo.cs`
- `public class XamlFileInfo`
- `public string XClass { get; set; }`
- `public static XamlFileInfo Parse(string data) {`

### `src/Avalonia.Controls.ColorPicker/AlphaComponentPosition.cs`
- `public enum AlphaComponentPosition`

### `src/Avalonia.Controls.ColorPicker/ColorChangedEventArgs.cs`
- `public class ColorChangedEventArgs : EventArgs`
- `public ColorChangedEventArgs(Color oldColor, Color newColor) {`
- `public Color OldColor { get; private set; }`
- `public Color NewColor { get; private set; }`

### `src/Avalonia.Controls.ColorPicker/ColorComponent.cs`
- `public enum ColorComponent`

### `src/Avalonia.Controls.ColorPicker/ColorModel.cs`
- `public enum ColorModel`

### `src/Avalonia.Controls.ColorPicker/ColorPalettes/FlatColorPalette.cs`
- `public class FlatColorPalette : IColorPalette`
- `public enum FlatColor : uint`
- `public int ColorCount {`
- `public int ShadeCount {`
- `public Color GetColor(int colorIndex, int shadeIndex) {`

### `src/Avalonia.Controls.ColorPicker/ColorPalettes/FlatHalfColorPalette.cs`
- `public class FlatHalfColorPalette : IColorPalette`
- `public int ColorCount {`
- `public int ShadeCount {`
- `public Color GetColor(int colorIndex, int shadeIndex) {`

### `src/Avalonia.Controls.ColorPicker/ColorPalettes/FluentColorPalette.cs`
- `public class FluentColorPalette : IColorPalette`
- `public int ColorCount {`
- `public int ShadeCount {`
- `public Color GetColor(int colorIndex, int shadeIndex) {`

### `src/Avalonia.Controls.ColorPicker/ColorPalettes/IColorPalette.cs`
- `public interface IColorPalette`

### `src/Avalonia.Controls.ColorPicker/ColorPalettes/MaterialColorPalette.cs`
- `public class MaterialColorPalette : IColorPalette`
- `public enum MaterialColor : uint`
- `public int ColorCount {`
- `public int ShadeCount {`
- `public Color GetColor(int colorIndex, int shadeIndex) {`

### `src/Avalonia.Controls.ColorPicker/ColorPalettes/MaterialHalfColorPalette.cs`
- `public class MaterialHalfColorPalette : IColorPalette`
- `public int ColorCount {`
- `public int ShadeCount {`
- `public Color GetColor(int colorIndex, int shadeIndex) {`

### `src/Avalonia.Controls.ColorPicker/ColorPalettes/SixteenColorPalette.cs`
- `public class SixteenColorPalette : IColorPalette`
- `public int ColorCount {`
- `public int ShadeCount {`
- `public Color GetColor(int colorIndex, int shadeIndex) {`

### `src/Avalonia.Controls.ColorPicker/ColorPicker/ColorPicker.cs`
- `public class ColorPicker : ColorView`
- `public ColorPicker() : base() {`
- `public static readonly StyledProperty<object?> ContentProperty = ContentControl.ContentProperty.AddOwner<ColorPicker>();`
- `public static readonly StyledProperty<IDataTemplate?> ContentTemplateProperty = ContentControl.ContentTemplateProperty.AddOwner<ColorPicker>();`
- `public static readonly StyledProperty<HorizontalAlignment> HorizontalContentAlignmentProperty = ContentControl.HorizontalContentAlignmentProperty.AddOwner<ColorPicker>();`
- `public static readonly StyledProperty<VerticalAlignment> VerticalContentAlignmentProperty = ContentControl.VerticalContentAlignmentProperty.AddOwner<ColorPicker>();`
- `public object? Content {`
- `public IDataTemplate? ContentTemplate {`
- `public HorizontalAlignment HorizontalContentAlignment {`
- `public VerticalAlignment VerticalContentAlignment {`

### `src/Avalonia.Controls.ColorPicker/ColorPreviewer/ColorPreviewer.Properties.cs`
- `public partial class ColorPreviewer`
- `public static readonly StyledProperty<HsvColor> HsvColorProperty = AvaloniaProperty.Register<ColorPreviewer, HsvColor>( nameof(HsvColor), Colors.Transparent.ToHsv(), defaultBindingMode: BindingMode.TwoWay);`
- `public static readonly StyledProperty<bool> IsAccentColorsVisibleProperty = AvaloniaProperty.Register<ColorPreviewer, bool>( nameof(IsAccentColorsVisible), true);`
- `public HsvColor HsvColor {`
- `public bool IsAccentColorsVisible {`

### `src/Avalonia.Controls.ColorPicker/ColorPreviewer/ColorPreviewer.cs`
- `public partial class ColorPreviewer : TemplatedControl`
- `public event EventHandler<ColorChangedEventArgs>? ColorChanged;`
- `public ColorPreviewer() : base() {`

### `src/Avalonia.Controls.ColorPicker/ColorSlider/ColorSlider.Properties.cs`
- `public partial class ColorSlider`
- `public static readonly StyledProperty<Color> ColorProperty = AvaloniaProperty.Register<ColorSlider, Color>( nameof(Color), Colors.White, defaultBindingMode: BindingMode.TwoWay);`
- `public static readonly StyledProperty<ColorComponent> ColorComponentProperty = AvaloniaProperty.Register<ColorSlider, ColorComponent>( nameof(ColorComponent), ColorComponent.Component1);`
- `public static readonly StyledProperty<ColorModel> ColorModelProperty = AvaloniaProperty.Register<ColorSlider, ColorModel>( nameof(ColorModel), ColorModel.Rgba);`
- `public static readonly StyledProperty<HsvColor> HsvColorProperty = AvaloniaProperty.Register<ColorSlider, HsvColor>( nameof(HsvColor), Colors.White.ToHsv(), defaultBindingMode: BindingMode.TwoWay);`
- `public static readonly StyledProperty<bool> IsAlphaVisibleProperty = AvaloniaProperty.Register<ColorSlider, bool>( nameof(IsAlphaVisible), false);`
- `public static readonly StyledProperty<bool> IsPerceptiveProperty = AvaloniaProperty.Register<ColorSlider, bool>( nameof(IsPerceptive), true);`
- `public static readonly StyledProperty<bool> IsRoundingEnabledProperty = AvaloniaProperty.Register<ColorSlider, bool>( nameof(IsRoundingEnabled), false);`
- `public Color Color {`
- `public ColorComponent ColorComponent {`
- `public ColorModel ColorModel {`
- `public HsvColor HsvColor {`
- `public bool IsAlphaVisible {`
- `public bool IsPerceptive {`
- `public bool IsRoundingEnabled {`

### `src/Avalonia.Controls.ColorPicker/ColorSlider/ColorSlider.cs`
- `public partial class ColorSlider : Slider`
- `public event EventHandler<ColorChangedEventArgs>? ColorChanged;`
- `public ColorSlider() : base() {`

### `src/Avalonia.Controls.ColorPicker/ColorSpectrum/ColorSpectrum.Properties.cs`
- `public partial class ColorSpectrum`
- `public static readonly StyledProperty<Color> ColorProperty = AvaloniaProperty.Register<ColorSpectrum, Color>( nameof(Color), Colors.White, defaultBindingMode: BindingMode.TwoWay);`
- `public static readonly StyledProperty<ColorSpectrumComponents> ComponentsProperty = AvaloniaProperty.Register<ColorSpectrum, ColorSpectrumComponents>( nameof(Components), ColorSpectrumComponents.HueSaturation);`
- `public static readonly StyledProperty<HsvColor> HsvColorProperty = AvaloniaProperty.Register<ColorSpectrum, HsvColor>( nameof(HsvColor), Colors.White.ToHsv(), defaultBindingMode: BindingMode.TwoWay);`
- `public static readonly StyledProperty<int> MaxHueProperty = AvaloniaProperty.Register<ColorSpectrum, int>( nameof(MaxHue), 359);`
- `public static readonly StyledProperty<int> MaxSaturationProperty = AvaloniaProperty.Register<ColorSpectrum, int>( nameof(MaxSaturation), 100);`
- `public static readonly StyledProperty<int> MaxValueProperty = AvaloniaProperty.Register<ColorSpectrum, int>( nameof(MaxValue), 100);`
- `public static readonly StyledProperty<int> MinHueProperty = AvaloniaProperty.Register<ColorSpectrum, int>( nameof(MinHue), 0);`
- `public static readonly StyledProperty<int> MinSaturationProperty = AvaloniaProperty.Register<ColorSpectrum, int>( nameof(MinSaturation), 0);`
- `public static readonly StyledProperty<int> MinValueProperty = AvaloniaProperty.Register<ColorSpectrum, int>( nameof(MinValue), 0);`
- `public static readonly StyledProperty<ColorSpectrumShape> ShapeProperty = AvaloniaProperty.Register<ColorSpectrum, ColorSpectrumShape>( nameof(Shape), ColorSpectrumShape.Box);`
- `public static readonly DirectProperty<ColorSpectrum, ColorComponent> ThirdComponentProperty = AvaloniaProperty.RegisterDirect<ColorSpectrum, ColorComponent>( nameof(ThirdComponent), o => o.ThirdComponent);`
- `public Color Color {`
- `public ColorSpectrumComponents Components {`
- `public HsvColor HsvColor {`
- `public int MaxHue {`
- `public int MaxSaturation {`
- `public int MaxValue {`
- `public int MinHue {`
- `public int MinSaturation {`
- `public int MinValue {`
- `public ColorSpectrumShape Shape {`
- `public ColorComponent ThirdComponent {`

### `src/Avalonia.Controls.ColorPicker/ColorSpectrum/ColorSpectrum.cs`
- `public partial class ColorSpectrum : TemplatedControl`
- `public event EventHandler<ColorChangedEventArgs>? ColorChanged;`
- `public ColorSpectrum() : base() {`
- `public void RaiseColorChanged() {`

### `src/Avalonia.Controls.ColorPicker/ColorSpectrum/ColorSpectrumComponents.cs`
- `public enum ColorSpectrumComponents`

### `src/Avalonia.Controls.ColorPicker/ColorSpectrum/ColorSpectrumShape.cs`
- `public enum ColorSpectrumShape`

### `src/Avalonia.Controls.ColorPicker/ColorView/ColorView.Properties.cs`
- `public partial class ColorView`
- `public static readonly StyledProperty<Color> ColorProperty = AvaloniaProperty.Register<ColorView, Color>( nameof(Color), Colors.White, defaultBindingMode: BindingMode.TwoWay, coerce: CoerceColor) ;`
- `public static readonly StyledProperty<ColorModel> ColorModelProperty = AvaloniaProperty.Register<ColorView, ColorModel>( nameof(ColorModel), ColorModel.Rgba);`
- `public static readonly StyledProperty<ColorSpectrumComponents> ColorSpectrumComponentsProperty = AvaloniaProperty.Register<ColorView, ColorSpectrumComponents>( nameof(ColorSpectrumComponents), ColorSpectrumComponents.HueSaturation);`
- `public static readonly StyledProperty<ColorSpectrumShape> ColorSpectrumShapeProperty = AvaloniaProperty.Register<ColorView, ColorSpectrumShape>( nameof(ColorSpectrumShape), ColorSpectrumShape.Box);`
- `public static readonly StyledProperty<AlphaComponentPosition> HexInputAlphaPositionProperty = AvaloniaProperty.Register<ColorView, AlphaComponentPosition>( nameof(HexInputAlphaPosition), AlphaComponentPosition.Leading);`
- `public static readonly StyledProperty<HsvColor> HsvColorProperty = AvaloniaProperty.Register<ColorView, HsvColor>( nameof(HsvColor), Colors.White.ToHsv(), defaultBindingMode: BindingMode.TwoWay, coerce: CoerceHsvColor);`
- `public static readonly StyledProperty<bool> IsAccentColorsVisibleProperty = AvaloniaProperty.Register<ColorView, bool>( nameof(IsAccentColorsVisible), true);`
- `public static readonly StyledProperty<bool> IsAlphaEnabledProperty = AvaloniaProperty.Register<ColorView, bool>( nameof(IsAlphaEnabled), true);`
- `public static readonly StyledProperty<bool> IsAlphaVisibleProperty = AvaloniaProperty.Register<ColorView, bool>( nameof(IsAlphaVisible), true);`
- `public static readonly StyledProperty<bool> IsColorComponentsVisibleProperty = AvaloniaProperty.Register<ColorView, bool>( nameof(IsColorComponentsVisible), true);`
- `public static readonly StyledProperty<bool> IsColorModelVisibleProperty = AvaloniaProperty.Register<ColorView, bool>( nameof(IsColorModelVisible), true);`
- `public static readonly StyledProperty<bool> IsColorPaletteVisibleProperty = AvaloniaProperty.Register<ColorView, bool>( nameof(IsColorPaletteVisible), true);`
- `public static readonly StyledProperty<bool> IsColorPreviewVisibleProperty = AvaloniaProperty.Register<ColorView, bool>( nameof(IsColorPreviewVisible), true);`
- `public static readonly StyledProperty<bool> IsColorSpectrumVisibleProperty = AvaloniaProperty.Register<ColorView, bool>( nameof(IsColorSpectrumVisible), true);`
- `public static readonly StyledProperty<bool> IsColorSpectrumSliderVisibleProperty = AvaloniaProperty.Register<ColorView, bool>( nameof(IsColorSpectrumSliderVisible), true);`
- `public static readonly StyledProperty<bool> IsComponentSliderVisibleProperty = AvaloniaProperty.Register<ColorView, bool>( nameof(IsComponentSliderVisible), true);`
- `public static readonly StyledProperty<bool> IsComponentTextInputVisibleProperty = AvaloniaProperty.Register<ColorView, bool>( nameof(IsComponentTextInputVisible), true);`
- `public static readonly StyledProperty<bool> IsHexInputVisibleProperty = AvaloniaProperty.Register<ColorView, bool>( nameof(IsHexInputVisible), true);`
- `public static readonly StyledProperty<int> MaxHueProperty = AvaloniaProperty.Register<ColorView, int>( nameof(MaxHue), 359);`
- `public static readonly StyledProperty<int> MaxSaturationProperty = AvaloniaProperty.Register<ColorView, int>( nameof(MaxSaturation), 100);`
- `public static readonly StyledProperty<int> MaxValueProperty = AvaloniaProperty.Register<ColorView, int>( nameof(MaxValue), 100);`
- `public static readonly StyledProperty<int> MinHueProperty = AvaloniaProperty.Register<ColorView, int>( nameof(MinHue), 0);`
- `public static readonly StyledProperty<int> MinSaturationProperty = AvaloniaProperty.Register<ColorView, int>( nameof(MinSaturation), 0);`
- `public static readonly StyledProperty<int> MinValueProperty = AvaloniaProperty.Register<ColorView, int>( nameof(MinValue), 0);`
- `public static readonly StyledProperty<IEnumerable<Color>?> PaletteColorsProperty = AvaloniaProperty.Register<ColorView, IEnumerable<Color>?>( nameof(PaletteColors), null);`
- `public static readonly StyledProperty<int> PaletteColumnCountProperty = AvaloniaProperty.Register<ColorView, int>( nameof(PaletteColumnCount), 4);`
- `public static readonly StyledProperty<IColorPalette?> PaletteProperty = AvaloniaProperty.Register<ColorView, IColorPalette?>( nameof(Palette), null);`
- `public static readonly StyledProperty<int> SelectedIndexProperty = AvaloniaProperty.Register<ColorView, int>( nameof(SelectedIndex), (int)ColorViewTab.Spectrum);`
- `public Color Color {`
- `public ColorModel ColorModel {`
- `public ColorSpectrumComponents ColorSpectrumComponents {`
- `public ColorSpectrumShape ColorSpectrumShape {`
- `public AlphaComponentPosition HexInputAlphaPosition {`
- `public HsvColor HsvColor {`
- `public bool IsAccentColorsVisible {`
- `public bool IsAlphaEnabled {`
- `public bool IsAlphaVisible {`
- `public bool IsColorComponentsVisible {`
- `public bool IsColorModelVisible {`
- `public bool IsColorPaletteVisible {`
- `public bool IsColorPreviewVisible {`
- `public bool IsColorSpectrumVisible {`
- `public bool IsColorSpectrumSliderVisible {`
- `public bool IsComponentSliderVisible {`
- `public bool IsComponentTextInputVisible {`
- `public bool IsHexInputVisible {`
- `public int MaxHue {`
- `public int MaxSaturation {`
- `public int MaxValue {`
- `public int MinHue {`
- `public int MinSaturation {`
- `public int MinValue {`
- `public IEnumerable<Color>? PaletteColors {`
- `public int PaletteColumnCount {`
- `public IColorPalette? Palette {`
- `public int SelectedIndex {`

### `src/Avalonia.Controls.ColorPicker/ColorView/ColorView.cs`
- `public partial class ColorView : TemplatedControl`
- `public event EventHandler<ColorChangedEventArgs>? ColorChanged;`
- `public ColorView() : base() {`

### `src/Avalonia.Controls.ColorPicker/ColorView/ColorViewTab.cs`
- `public enum ColorViewTab`

### `src/Avalonia.Controls.ColorPicker/Converters/AccentColorConverter.cs`
- `public class AccentColorConverter : IValueConverter`
- `public const double ValueDelta = 0.1;`
- `public object? Convert( object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public object? ConvertBack( object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public static HsvColor GetAccent(HsvColor hsvColor, int accentStep) {`

### `src/Avalonia.Controls.ColorPicker/Converters/ColorToDisplayNameConverter.cs`
- `public class ColorToDisplayNameConverter : IValueConverter`
- `public object? Convert( object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public object? ConvertBack( object? value, Type targetType, object? parameter, CultureInfo culture) {`

### `src/Avalonia.Controls.ColorPicker/Converters/ColorToHexConverter.cs`
- `public class ColorToHexConverter : IValueConverter`
- `public bool IsAlphaVisible { get; set; } = true;`
- `public AlphaComponentPosition AlphaPosition { get; set; } = AlphaComponentPosition.Leading;`
- `public object? Convert( object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public object? ConvertBack( object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public static string ToHexString( Color color, AlphaComponentPosition alphaPosition, bool includeAlpha = true, bool includeSymbol = false) {`
- `public static Color? ParseHexString( string hexColor, AlphaComponentPosition alphaPosition) {`

### `src/Avalonia.Controls.ColorPicker/Converters/ContrastBrushConverter.cs`
- `public class ContrastBrushConverter : IValueConverter`
- `public byte AlphaThreshold { get; set; } = 128;`
- `public object? Convert( object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public object? ConvertBack( object? value, Type targetType, object? parameter, CultureInfo culture) {`

### `src/Avalonia.Controls.ColorPicker/Converters/DoNothingForNullConverter.cs`
- `public class DoNothingForNullConverter : IValueConverter`
- `public object? Convert( object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public object? ConvertBack( object? value, Type targetType, object? parameter, CultureInfo culture) {`

### `src/Avalonia.Controls.ColorPicker/Converters/ToBrushConverter.cs`
- `public class ToBrushConverter : IValueConverter`
- `public object? Convert( object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public object? ConvertBack( object? value, Type targetType, object? parameter, CultureInfo culture) {`

### `src/Avalonia.Controls.ColorPicker/Converters/ToColorConverter.cs`
- `public class ToColorConverter : IValueConverter`
- `public object? Convert( object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public object? ConvertBack( object? value, Type targetType, object? parameter, CultureInfo culture) {`

### `src/Avalonia.Controls.ColorPicker/Helpers/ColorHelper.cs`
- `public static class ColorHelper`
- `public static double GetRelativeLuminance(Color color) {`
- `public static bool ToDisplayNameExists {`
- `public static string ToDisplayName(Color color) {`

### `src/Avalonia.Controls.ColorPicker/HsvComponent.cs`
- `public enum HsvComponent`

### `src/Avalonia.Controls.ColorPicker/RgbComponent.cs`
- `public enum RgbComponent`

### `src/Avalonia.DesignerSupport/DesignWindowLoader.cs`
- `public class DesignWindowLoader`
- `public static Window LoadDesignerWindow(string xaml, string assemblyPath, string xamlFileProjectPath) => LoadDesignerWindow(xaml, assemblyPath, xamlFileProjectPath, 1.0);`
- `public static Window LoadDesignerWindow(string xaml, string assemblyPath, string xamlFileProjectPath, double renderScaling) {`

### `src/Avalonia.DesignerSupport/Remote/HtmlTransport/HtmlTransport.cs`
- `public class HtmlWebSocketTransport : IAvaloniaRemoteTransportConnection`
- `public HtmlWebSocketTransport(IAvaloniaRemoteTransportConnection signalTransport, Uri listenUri) {`

### `src/Avalonia.DesignerSupport/Remote/HtmlTransport/SimpleWebSocketHttpServer.cs`
- `public class SimpleWebSocketHttpServer : IDisposable`
- `public async Task<SimpleWebSocketHttpRequest> AcceptAsync() {`
- `public void Listen() {`
- `public SimpleWebSocketHttpServer(IPAddress address, int port) {`
- `public void Dispose() {`
- `public class SimpleWebSocketHttpRequest : IDisposable`
- `public Dictionary<string, string> Headers { get; }`
- `public string Path { get; }`
- `public bool IsWebsocketRequest { get; }`
- `public IReadOnlyList<string> WebSocketProtocols { get; }`
- `public SimpleWebSocketHttpRequest(NetworkStream stream, string path, Dictionary<string, string> headers) {`
- `public async Task RespondAsync(int code, byte[] data, string contentType) {`
- `public async Task<SimpleWebSocket> AcceptWebSocket(string protocol = null) {`
- `public void Dispose() => _stream?.Dispose();`
- `public class SimpleWebSocket : IDisposable`
- `public void Dispose() {`
- `public Task SendMessage(string text) {`
- `public Task SendMessage(bool isText, byte[] data) => SendMessage(isText, data, 0, data.Length);`
- `public Task SendMessage(bool isText, byte[] data, int offset, int length) => SendFrame(isText ? FrameType.Text : FrameType.Binary, data, offset, length);`
- `public async Task<SimpleWebSocketMessage> ReceiveMessage() {`
- `public class SimpleWebSocketMessage`
- `public bool IsText { get; set; }`
- `public byte[] Data { get; set; }`
- `public string AsString() {`

### `src/Avalonia.DesignerSupport/Remote/RemoteDesignerEntryPoint.cs`
- `public class RemoteDesignerEntryPoint`
- `public static void Main(string[] cmdline) {`

### `src/Avalonia.Diagnostics/DevToolsExtensions.cs`
- `public static class DevToolsExtensions`
- `public static void AttachDevTools(this TopLevel root) {`
- `public static void AttachDevTools(this TopLevel root, KeyGesture gesture) {`
- `public static void AttachDevTools(this TopLevel root, DevToolsOptions options) {`
- `public static void AttachDevTools(this Application application) {`
- `public static void AttachDevTools(this Application application, DevToolsOptions options) {`

### `src/Avalonia.Diagnostics/Diagnostics/DevToolsDataFormats.cs`
- Namespace: `Avalonia.Diagnostics`
- `public static class DevToolsDataFormats`
- `public static DataFormat<string> Selector { get; } = DataFormat.CreateStringPlatformFormat("Avalonia_DevTools_Selector");`

### `src/Avalonia.Diagnostics/Diagnostics/DevToolsOptions.cs`
- `public class DevToolsOptions`
- `public KeyGesture Gesture { get; set; } = new KeyGesture(Key.F12);`
- `public bool ShowAsChildWindow { get; set; } = true;`
- `public Size Size { get; set; } = new Size(1280, 720);`
- `public int? StartupScreenIndex { get; set; }`
- `public bool ShowImplementedInterfaces { get; set; } = true;`
- `public IScreenshotHandler ScreenshotHandler { get; set; }`
- `public ThemeVariant? ThemeVariant { get; set; }`
- `public IBrush? FocusHighlighterBrush { get; set; }`
- `public DevToolsViewKind LaunchView { get; init; }`
- `public HotKeyConfiguration HotKeys { get; init; } = new();`

### `src/Avalonia.Diagnostics/Diagnostics/DevToolsViewKind.cs`
- `public enum DevToolsViewKind`

### `src/Avalonia.Diagnostics/Diagnostics/HotKeyConfiguration.cs`
- `public class HotKeyConfiguration`
- `public KeyGesture ValueFramesFreeze { get; init; } = new(Key.S, KeyModifiers.Alt);`
- `public KeyGesture ValueFramesUnfreeze { get; init; } = new(Key.D, KeyModifiers.Alt);`
- `public KeyGesture InspectHoveredControl { get; init; } = new(Key.None, KeyModifiers.Shift | KeyModifiers.Control);`
- `public KeyGesture TogglePopupFreeze { get; init; } = new(Key.F, KeyModifiers.Alt | KeyModifiers.Control);`
- `public KeyGesture ScreenshotSelectedControl { get; init; } = new(Key.F8);`

### `src/Avalonia.Diagnostics/Diagnostics/IScreenshotHandler.cs`
- `public interface IScreenshotHandler`

### `src/Avalonia.Diagnostics/Diagnostics/Screenshots/BaseRenderToStreamHandler.cs`
- `public abstract class BaseRenderToStreamHandler : IScreenshotHandler`
- `public async Task Take(Control control) {`

### `src/Avalonia.Diagnostics/Diagnostics/Screenshots/FilePickerHandler.cs`
- `public sealed class FilePickerHandler : BaseRenderToStreamHandler`
- `public FilePickerHandler() : this(null, null) {`
- `public FilePickerHandler( string? title, string? screenshotRoot = default) {`

### `src/Avalonia.Diagnostics/Diagnostics/VisualTreeDebug.cs`
- `public static class VisualTreeDebug`
- `public static string PrintVisualTree(Visual visual) {`

### `src/Avalonia.Dialogs/AboutAvaloniaDialog.xaml.cs`
- `public class AboutAvaloniaDialog : Window`
- `public static string Version { get; } = $@"v{s_version.ToString(2)}";`
- `public static bool IsDevelopmentBuild { get; } = s_version.Revision == 999;`
- `public static string Copyright { get; } = $"© {DateTime.Now.Year} The Avalonia Project";`
- `public AboutAvaloniaDialog() {`

### `src/Avalonia.Dialogs/Internal/AvaloniaDialogsInternalViewModelBase.cs`
- `public class AvaloniaDialogsInternalViewModelBase : INotifyPropertyChanged`
- `public event PropertyChangedEventHandler? PropertyChanged;`

### `src/Avalonia.Dialogs/Internal/ChildFitter.cs`
- `public class ChildFitter : Decorator`

### `src/Avalonia.Dialogs/Internal/FileSizeStringConverter.cs`
- `public class FileSizeStringConverter : IValueConverter`
- `public object Convert(object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public object ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture) {`

### `src/Avalonia.Dialogs/Internal/ManagedFileChooserFilterViewModel.cs`
- `public class ManagedFileChooserFilterViewModel : AvaloniaDialogsInternalViewModelBase`
- `public string Name { get; }`
- `public ManagedFileChooserFilterViewModel(FilePickerFileType filter) : this(filter, 0) {`
- `public ManagedFileChooserFilterViewModel(FilePickerFileType filter, int index) {`
- `public bool Match(string filename) {`
- `public override string ToString() => Name;`

### `src/Avalonia.Dialogs/Internal/ManagedFileChooserItemType.cs`
- `public enum ManagedFileChooserItemType`

### `src/Avalonia.Dialogs/Internal/ManagedFileChooserItemViewModel.cs`
- `public class ManagedFileChooserItemViewModel : AvaloniaDialogsInternalViewModelBase`
- `public string? DisplayName {`
- `public string? Path {`
- `public DateTime Modified {`
- `public string? Type {`
- `public long Size {`
- `public ManagedFileChooserItemType ItemType {`
- `public string IconKey {`
- `public ManagedFileChooserItemViewModel() {`
- `public ManagedFileChooserItemViewModel(ManagedFileChooserNavigationItem item) {`

### `src/Avalonia.Dialogs/Internal/ManagedFileChooserNavigationItem.cs`
- `public class ManagedFileChooserNavigationItem`
- `public string? DisplayName { get; set; }`
- `public string? Path { get; set; }`
- `public ManagedFileChooserItemType ItemType { get; set; }`

### `src/Avalonia.Dialogs/Internal/ManagedFileChooserViewModel.cs`
- `public class ManagedFileChooserViewModel : AvaloniaDialogsInternalViewModelBase`
- `public event Action? CancelRequested;`
- `public event Action<string[]>? CompleteRequested;`
- `public event Action<string>? OverwritePrompt;`
- `public AvaloniaList<ManagedFileChooserItemViewModel> QuickLinks { get; } =`
- `public AvaloniaList<ManagedFileChooserItemViewModel> Items { get; } =`
- `public AvaloniaList<ManagedFileChooserFilterViewModel> Filters { get; } =`
- `public AvaloniaList<ManagedFileChooserItemViewModel> SelectedItems { get; } =`
- `public string? Location {`
- `public string? FileName {`
- `public bool SelectingFolder => _selectingDirectory;`
- `public bool ShowFilters { get; }`
- `public SelectionMode SelectionMode { get; }`
- `public string? Title { get; }`
- `public int QuickLinksSelectedIndex {`
- `public ManagedFileChooserFilterViewModel? SelectedFilter {`
- `public bool ShowHiddenFiles {`
- `public ManagedFileChooserViewModel(ManagedFileDialogOptions options) {`
- `public ManagedFileChooserViewModel(FilePickerOpenOptions filePickerOpen, ManagedFileDialogOptions options) : this(options) {`
- `public ManagedFileChooserViewModel(FilePickerSaveOptions filePickerSave, ManagedFileDialogOptions options) : this(options) {`
- `public ManagedFileChooserViewModel(FolderPickerOpenOptions folderPickerOpen, ManagedFileDialogOptions options) : this(options) {`
- `public void EnterPressed() {`
- `public void Refresh() => Navigate(Location);`
- `public void Navigate(IStorageFolder? path, string? initialSelectionName = null) {`
- `public void Navigate(string? path, string? initialSelectionName = null) {`
- `public void GoUp() {`
- `public void Cancel() {`
- `public bool CanOk(object _) =>`
- `public void Ok() {`
- `public void SelectSingleFile(ManagedFileChooserItemViewModel item) {`

### `src/Avalonia.Dialogs/Internal/ResourceSelectorConverter.cs`
- `public class ResourceSelectorConverter : ResourceDictionary, IValueConverter`
- `public object? Convert(object? key, Type targetType, object? parameter, CultureInfo culture) {`
- `public object ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture) {`

### `src/Avalonia.Dialogs/ManagedFileChooser.cs`
- `public class ManagedFileChooser : TemplatedControl`
- `public ManagedFileChooser() {`

### `src/Avalonia.Dialogs/ManagedFileChooserOverwritePrompt.cs`
- Namespace: `Avalonia.Dialogs`
- `public class ManagedFileChooserOverwritePrompt : TemplatedControl`
- `public static readonly DirectProperty<ManagedFileChooserOverwritePrompt, string> FileNameProperty = AvaloniaProperty.RegisterDirect<ManagedFileChooserOverwritePrompt, string>( "FileName", o => o.FileName, (o, v) => o.FileName = v);`
- `public string FileName {`
- `public void Confirm() {`
- `public void Cancel() {`

### `src/Avalonia.Dialogs/ManagedFileDialogExtensions.cs`
- `public static class ManagedFileDialogExtensions`
- `public static AppBuilder UseManagedSystemDialogs(this AppBuilder builder) {`
- `public static AppBuilder UseManagedSystemDialogs<TWindow>(this AppBuilder builder) where TWindow : Window, new() {`
- `public static Task<string[]> ShowManagedAsync(this OpenFileDialog dialog, Window parent, ManagedFileDialogOptions? options = null) => ShowManagedAsync<Window>(dialog, parent, options);`
- `public static async Task<string[]> ShowManagedAsync<TWindow>(this OpenFileDialog dialog, Window parent, ManagedFileDialogOptions? options = null) where TWindow : Window, new() {`

### `src/Avalonia.Dialogs/ManagedFileDialogOptions.cs`
- `public record ManagedFileDialogOptions`
- `public bool AllowDirectorySelection { get; set; }`
- `public IMountedVolumeInfoProvider? CustomVolumeInfoProvider { get; set; }`
- `public Func<ContentControl>? ContentRootFactory { get; set; }`

### `src/Avalonia.Metal/IMetalDevice.cs`
- Namespace: `Avalonia.Metal`
- `public interface IMetalDevice : IPlatformGraphicsContext`
- `public interface IMetalPlatformSurface`
- `public interface IMetalPlatformSurfaceRenderTarget : IDisposable`
- `public interface IMetalPlatformSurfaceRenderingSession : IDisposable`

### `src/Avalonia.Metal/IMetalExternalObjectsFeature.cs`
- Namespace: `Avalonia.Metal`
- `public interface IMetalExternalObjectsFeature`
- `public interface IMetalExternalTexture : IDisposable`
- `public interface IMetalSharedEvent : IDisposable`

### `src/Avalonia.MicroCom/CallbackBase.cs`
- `public abstract class CallbackBase : IUnknown, IMicroComShadowContainer`
- `public bool IsDestroyed => _destroyed;`
- `public void Dispose() {`
- `public MicroComShadow? Shadow { get; set; }`
- `public void OnReferencedFromNative() {`
- `public void OnUnreferencedFromNative() {`

### `src/Avalonia.OpenGL/Controls/OpenGlControlBase.cs`
- `public abstract class OpenGlControlBase : Control`
- `public OpenGlControlBase() {`
- `public new void InvalidateVisual() => RequestNextFrameRendering();`
- `public void RequestNextFrameRendering() {`

### `src/Avalonia.OpenGL/Egl/EglConsts.cs`
- `public static class EglConsts`
- `public const int EGL_ALPHA_SIZE = 0x3021;`
- `public const int EGL_BAD_ACCESS = 0x3002;`
- `public const int EGL_BAD_ALLOC = 0x3003;`
- `public const int EGL_BAD_ATTRIBUTE = 0x3004;`
- `public const int EGL_BAD_CONFIG = 0x3005;`
- `public const int EGL_BAD_CONTEXT = 0x3006;`
- `public const int EGL_BAD_CURRENT_SURFACE = 0x3007;`
- `public const int EGL_BAD_DISPLAY = 0x3008;`
- `public const int EGL_BAD_MATCH = 0x3009;`
- `public const int EGL_BAD_NATIVE_PIXMAP = 0x300A;`
- `public const int EGL_BAD_NATIVE_WINDOW = 0x300B;`
- `public const int EGL_BAD_PARAMETER = 0x300C;`
- `public const int EGL_BAD_SURFACE = 0x300D;`
- `public const int EGL_BLUE_SIZE = 0x3022;`
- `public const int EGL_CORE_NATIVE_ENGINE = 0x305B;`
- `public const int EGL_DEPTH_SIZE = 0x3025;`
- `public const int EGL_DRAW = 0x3059;`
- `public const int EGL_EXTENSIONS = 0x3055;`
- `public const int EGL_FALSE = 0;`
- `public const int EGL_GREEN_SIZE = 0x3023;`
- `public const int EGL_HEIGHT = 0x3056;`
- `public const int EGL_NONE = 0x3038;`
- `public const int EGL_NOT_INITIALIZED = 0x3001;`
- `public const int EGL_NO_CONTEXT = 0;`
- `public const int EGL_NO_DISPLAY = 0;`
- `public const int EGL_NO_SURFACE = 0;`
- `public const int EGL_PBUFFER_BIT = 0x0001;`
- `public const int EGL_READ = 0x305A;`
- `public const int EGL_RED_SIZE = 0x3024;`
- `public const int EGL_SAMPLES = 0x3031;`
- `public const int EGL_STENCIL_SIZE = 0x3026;`
- `public const int EGL_SUCCESS = 0x3000;`
- `public const int EGL_SURFACE_TYPE = 0x3033;`
- `public const int EGL_TRUE = 1;`
- `public const int EGL_WIDTH = 0x3057;`
- `public const int EGL_WINDOW_BIT = 0x0004;`
- `public const int EGL_BACK_BUFFER = 0x3084;`
- `public const int EGL_CONTEXT_LOST = 0x300E;`
- `public const int EGL_TEXTURE_2D = 0x305F;`
- `public const int EGL_TEXTURE_FORMAT = 0x3080;`
- `public const int EGL_TEXTURE_RGBA = 0x305E;`
- `public const int EGL_TEXTURE_TARGET = 0x3081;`
- `public const int EGL_OPENGL_ES_BIT = 0x0001;`
- `public const int EGL_OPENGL_ES_API = 0x30A0;`
- `public const int EGL_RENDERABLE_TYPE = 0x3040;`
- `public const int EGL_OPENGL_ES2_BIT = 0x0004;`
- `public const int EGL_CONTEXT_MAJOR_VERSION = 0x3098;`
- `public const int EGL_CONTEXT_MINOR_VERSION = 0x30FB;`
- `public const int EGL_OPENGL_ES3_BIT = 0x00000040;`
- `public const int EGL_PLATFORM_ANGLE_TYPE_D3D9_ANGLE = 0x3207;`
- `public const int EGL_PLATFORM_ANGLE_TYPE_D3D11_ANGLE = 0x3208;`
- `public const int EGL_PLATFORM_ANGLE_ANGLE = 0x3202;`
- `public const int EGL_PLATFORM_ANGLE_TYPE_ANGLE = 0x3203;`
- `public const int EGL_PLATFORM_DEVICE_EXT = 0x313F;`
- `public const int EGL_DEVICE_EXT = 0x322C;`
- `public const int EGL_D3D9_DEVICE_ANGLE = 0x33A0;`
- `public const int EGL_D3D11_DEVICE_ANGLE = 0x33A1;`
- `public const int EGL_D3D_TEXTURE_2D_SHARE_HANDLE_ANGLE = 0x3200;`
- `public const int EGL_D3D_TEXTURE_ANGLE = 0x33A3;`
- `public const int EGL_TEXTURE_OFFSET_X_ANGLE = 0x3490;`
- `public const int EGL_TEXTURE_OFFSET_Y_ANGLE = 0x3491;`
- `public const int EGL_FLEXIBLE_SURFACE_COMPATIBILITY_SUPPORTED_ANGLE = 0x33A6;`
- `public const int EGL_TEXTURE_INTERNAL_FORMAT_ANGLE = 0x345D;`

### `src/Avalonia.OpenGL/Egl/EglContext.cs`
- `public class EglContext : IGlContext`
- `public IntPtr Context =>`
- `public EglSurface? OffscreenSurface { get; }`
- `public GlVersion Version { get; }`
- `public GlInterface GlInterface { get; }`
- `public int SampleCount { get; }`
- `public int StencilSize { get; }`
- `public EglDisplay Display => _disp;`
- `public EglInterface EglInterface => _egl;`
- `public IDisposable MakeCurrent() => MakeCurrent(OffscreenSurface);`
- `public IDisposable MakeCurrent(EglSurface? surface) {`
- `public void NotifyContextLost() {`
- `public bool IsLost => _isLost || _disp.IsLost || Context == IntPtr.Zero;`
- `public IDisposable EnsureCurrent() {`
- `public IDisposable EnsureLocked() {`
- `public bool IsSharedWith(IGlContext context) {`
- `public bool CanCreateSharedContext => _disp.SupportsSharing;`
- `public IGlContext CreateSharedContext(IEnumerable<GlVersion>? preferredVersions = null) =>`
- `public bool IsCurrent => _context != default && _egl.GetCurrentDisplay() == _disp.Handle && _egl.GetCurrentContext() == _context;`
- `public void Dispose() {`
- `public object? TryGetFeature(Type featureType) {`

### `src/Avalonia.OpenGL/Egl/EglDisplay.cs`
- `public class EglDisplay : IDisposable`
- `public bool SupportsSharing { get; }`
- `public IntPtr Handle => _display;`
- `public IntPtr Config => _config.Config;`
- `public EglDisplay() : this(new EglDisplayCreationOptions {`
- `public EglDisplay(EglDisplayCreationOptions options) : this(EglDisplayUtils.CreateDisplay(options), options) {`
- `public EglDisplay(IntPtr display, EglDisplayOptions options) {`
- `public EglInterface EglInterface => _egl;`
- `public EglContext CreateContext(EglContextOptions? options) {`
- `public EglSurface CreateWindowSurface(IntPtr window) {`
- `public unsafe EglSurface CreatePBufferFromClientBuffer(int bufferType, IntPtr handle, int[] attribs) {`
- `public unsafe EglSurface CreatePBufferFromClientBuffer (int bufferType, IntPtr handle, int* attribs) {`
- `public bool IsLost {`
- `public IDisposable Lock() {`
- `public void Dispose() {`

### `src/Avalonia.OpenGL/Egl/EglDisplayOptions.cs`
- Namespace: `Avalonia.OpenGL.Egl`
- `public class EglDisplayOptions`
- `public EglInterface? Egl { get; set; }`
- `public bool SupportsContextSharing { get; set; }`
- `public bool SupportsMultipleContexts { get; set; }`
- `public bool ContextLossIsDisplayLoss { get; set; }`
- `public Func<bool>? DeviceLostCheckCallback { get; set; }`
- `public Action? DisposeCallback { get; set; }`
- `public IEnumerable<GlVersion>? GlVersions { get; set; }`
- `public class EglContextOptions`
- `public EglContext? ShareWith { get; set; }`
- `public EglSurface? OffscreenSurface { get; set; }`
- `public Action? DisposeCallback { get; set; }`
- `public Dictionary<Type, Func<EglContext, object>>? ExtraFeatures { get; set; }`
- `public class EglDisplayCreationOptions : EglDisplayOptions`
- `public int? PlatformType { get; set; }`
- `public IntPtr PlatformDisplay { get; set; }`
- `public int[]? PlatformDisplayAttrs { get; set; }`

### `src/Avalonia.OpenGL/Egl/EglErrors.cs`
- `public enum EglErrors`

### `src/Avalonia.OpenGL/Egl/EglGlPlatformSurface.cs`
- `public class EglGlPlatformSurface : EglGlPlatformSurfaceBase`
- `public interface IEglWindowGlPlatformSurfaceInfo`
- `public EglGlPlatformSurface(IEglWindowGlPlatformSurfaceInfo info) {`
- `public override IGlPlatformSurfaceRenderTarget CreateGlRenderTarget(IGlContext context) {`

### `src/Avalonia.OpenGL/Egl/EglGlPlatformSurfaceBase.cs`
- `public abstract class EglGlPlatformSurfaceBase : IGlPlatformSurface`
- `public abstract IGlPlatformSurfaceRenderTarget CreateGlRenderTarget(IGlContext context);`
- `public abstract class EglPlatformSurfaceRenderTargetBase : IGlPlatformSurfaceRenderTargetWithCorruptionInfo`
- `public virtual void Dispose() {`
- `public IGlPlatformSurfaceRenderingSession BeginDraw() {`
- `public abstract IGlPlatformSurfaceRenderingSession BeginDrawCore();`
- `public virtual bool IsCorrupted => Context.IsLost;`

### `src/Avalonia.OpenGL/Egl/EglInterface.cs`
- `public unsafe partial class EglInterface`
- `public EglInterface(Func<string, IntPtr> getProcAddress) {`
- `public EglInterface(string library) : this(Load(library)) {`
- `public EglInterface() : this(Load()) {`
- `public partial int GetError();`
- `public partial IntPtr GetDisplay(IntPtr nativeDisplay);`
- `public partial IntPtr GetPlatformDisplayExt(int platform, IntPtr nativeDisplay, int[]? attrs);`
- `public partial bool Initialize(IntPtr display, out int major, out int minor);`
- `public partial void Terminate(IntPtr display);`
- `public partial IntPtr GetProcAddress(IntPtr proc);`
- `public partial bool BindApi(int api);`
- `public partial bool ChooseConfig(IntPtr display, int[] attribs, out IntPtr surfaceConfig, int numConfigs, out int choosenConfig);`
- `public partial IntPtr CreateContext(IntPtr display, IntPtr config, IntPtr share, int[] attrs);`
- `public partial bool DestroyContext(IntPtr display, IntPtr context);`
- `public partial IntPtr CreatePBufferSurface(IntPtr display, IntPtr config, int[]? attrs);`
- `public partial bool MakeCurrent(IntPtr display, IntPtr draw, IntPtr read, IntPtr context);`
- `public partial IntPtr GetCurrentContext();`
- `public partial IntPtr GetCurrentDisplay();`
- `public partial IntPtr GetCurrentSurface(int readDraw);`
- `public partial void DestroySurface(IntPtr display, IntPtr surface);`
- `public partial void SwapBuffers(IntPtr display, IntPtr surface);`
- `public partial IntPtr CreateWindowSurface(IntPtr display, IntPtr config, IntPtr window, int[]? attrs);`
- `public partial int BindTexImage(IntPtr display, IntPtr surface, int buffer);`
- `public partial bool GetConfigAttrib(IntPtr display, IntPtr config, int attr, out int rv);`
- `public partial bool WaitGL();`
- `public partial bool WaitClient();`
- `public partial bool WaitNative(int engine);`
- `public partial IntPtr QueryStringNative(IntPtr display, int i);`
- `public string? QueryString(IntPtr display, int i) {`
- `public partial IntPtr CreatePbufferFromClientBuffer(IntPtr display, int buftype, IntPtr buffer, IntPtr config, int[]? attrib_list);`
- `public partial IntPtr CreatePbufferFromClientBufferPtr(IntPtr display, int buftype, IntPtr buffer, IntPtr config, int* attrib_list);`
- `public partial bool QueryDisplayAttribExt(IntPtr display, int attr, out IntPtr res);`
- `public partial bool QueryDeviceAttribExt(IntPtr display, int attr, out IntPtr res);`

### `src/Avalonia.OpenGL/Egl/EglPlatformGraphics.cs`
- `public sealed class EglPlatformGraphics : IPlatformGraphics`
- `public bool UsesSharedContext => false;`
- `public IPlatformGraphicsContext CreateContext() => _display.CreateContext(null);`
- `public IPlatformGraphicsContext GetSharedContext() => throw new NotSupportedException();`
- `public EglPlatformGraphics(EglDisplay display) {`
- `public static EglPlatformGraphics? TryCreate() => TryCreate(() => new EglDisplay(new EglDisplayCreationOptions`
- `public static EglPlatformGraphics? TryCreate(Func<EglDisplay> displayFactory) {`

### `src/Avalonia.OpenGL/Egl/EglSurface.cs`
- `public class EglSurface : SafeHandle`
- `public EglSurface(EglDisplay display, IntPtr surface) : base(surface, true) {`
- `public override bool IsInvalid => handle == IntPtr.Zero;`
- `public void SwapBuffers() => _egl.SwapBuffers(_display.Handle, handle);`

### `src/Avalonia.OpenGL/Features/ExternalObjectsOpenGlExtensionFeature.cs`
- Namespace: `Avalonia.OpenGL.Features`
- `public class ExternalObjectsOpenGlExtensionFeature : IGlContextExternalObjectsFeature`
- `public static ExternalObjectsOpenGlExtensionFeature? TryCreate(IGlContext context) {`
- `public IReadOnlyList<string> SupportedImportableExternalImageTypes => _imageTypes;`
- `public IReadOnlyList<string> SupportedExportableExternalImageTypes { get; } = Array.Empty<string>();`
- `public IReadOnlyList<string> SupportedImportableExternalSemaphoreTypes => _semaphoreTypes;`
- `public IReadOnlyList<string> SupportedExportableExternalSemaphoreTypes { get; } = Array.Empty<string>();`
- `public IReadOnlyList<PlatformGraphicsExternalImageFormat> GetSupportedFormatsForExternalMemoryType(string type) {`
- `public IGlExportableExternalImageTexture CreateImage(string type, PixelSize size, PlatformGraphicsExternalImageFormat format) =>`
- `public IGlExportableExternalImageTexture CreateSemaphore(string type) => throw new NotSupportedException();`
- `public IGlExternalImageTexture ImportImage(IPlatformHandle handle, PlatformGraphicsExternalImageProperties properties) {`
- `public IGlExternalSemaphore ImportSemaphore(IPlatformHandle handle) {`
- `public CompositionGpuImportedImageSynchronizationCapabilities GetSynchronizationCapabilities(string imageHandleType) {`
- `public byte[]? DeviceLuid { get; }`
- `public byte[]? DeviceUuid { get; }`

### `src/Avalonia.OpenGL/GlBasicInfoInterface.cs`
- `public unsafe partial class GlBasicInfoInterface`
- `public GlBasicInfoInterface(Func<string, IntPtr> getProcAddress) {`
- `public partial void GetIntegerv(int name, out int rv);`
- `public partial void GetFloatv(int name, out float rv);`
- `public partial IntPtr GetStringNative(int v);`
- `public partial IntPtr GetStringiNative(int v, int v1);`
- `public partial int GetError();`
- `public string? GetString(int v) {`
- `public string? GetString(int v, int index) {`
- `public List<string> GetExtensions() {`

### `src/Avalonia.OpenGL/GlConsts.cs`
- `public static class GlConsts`
- `public const int GL_UNSIGNED_BYTE = 0x1401;`
- `public const int GL_UNSIGNED_SHORT = 0x1403;`
- `public const int GL_FLOAT = 0x1406;`
- `public const int GL_TRIANGLES = 0x0004;`
- `public const int GL_CULL_FACE = 0x0B44;`
- `public const int GL_LESS = 0x0201;`
- `public const int GL_GREATER = 0x0204;`
- `public const int GL_DEPTH_TEST = 0x0B71;`
- `public const int GL_DEPTH_COMPONENT = 0x1902;`
- `public const int GL_LINEAR = 0x2601;`
- `public const int GL_STENCIL_BITS = 0x0D57;`
- `public const int GL_RGBA = 0x1908;`
- `public const int GL_SCISSOR_TEST = 0x0C11;`
- `public const int GL_TEXTURE_2D = 0x0DE1;`
- `public const int GL_TEXTURE_MAG_FILTER = 0x2800;`
- `public const int GL_TEXTURE_MIN_FILTER = 0x2801;`
- `public const int GL_NEAREST = 0x2600;`
- `public const int GL_VENDOR = 0x1F00;`
- `public const int GL_RENDERER = 0x1F01;`
- `public const int GL_VERSION = 0x1F02;`
- `public const int GL_EXTENSIONS = 0x1F03;`
- `public const int GL_NO_ERROR = 0;`
- `public const int GL_INVALID_ENUM = 0x0500;`
- `public const int GL_INVALID_VALUE = 0x0501;`
- `public const int GL_INVALID_OPERATION = 0x0502;`
- `public const int GL_STACK_OVERFLOW = 0x0503;`
- `public const int GL_STACK_UNDERFLOW = 0x0504;`
- `public const int GL_OUT_OF_MEMORY = 0x0505;`
- `public const int GL_INVALID_FRAMEBUFFER_OPERATION = 0x0506;`
- `public const int GL_CONTEXT_LOST = 0x0507;`
- `public const int GL_DEPTH_BUFFER_BIT = 0x00000100;`
- `public const int GL_STENCIL_BUFFER_BIT = 0x00000400;`
- `public const int GL_COLOR_BUFFER_BIT = 0x00004000;`
- `public const int GL_TEXTURE_BINDING_2D = 0x8069;`
- `public const int GL_RGBA8 = 0x8058;`
- `public const int GL_BGRA = 0x80E1;`
- `public const int GL_UNSIGNED_INT_8_8_8_8_REV = 0x8367;`
- `public const int GL_TEXTURE0 = 0x84C0;`
- `public const int GL_ACTIVE_TEXTURE = 0x84E0;`
- `public const int GL_SAMPLES = 0x80A9;`
- `public const int GL_DEPTH_COMPONENT16 = 0x81A5;`
- `public const int GL_ARRAY_BUFFER = 0x8892;`
- `public const int GL_ELEMENT_ARRAY_BUFFER = 0x8893;`
- `public const int GL_STATIC_DRAW = 0x88E4;`
- `public const int GL_FRAGMENT_SHADER = 0x8B30;`
- `public const int GL_VERTEX_SHADER = 0x8B31;`
- `public const int GL_COMPILE_STATUS = 0x8B81;`
- `public const int GL_LINK_STATUS = 0x8B82;`
- `public const int GL_INFO_LOG_LENGTH = 0x8B84;`
- `public const int GL_MAJOR_VERSION = 0x821B;`
- `public const int GL_MINOR_VERSION = 0x821C;`
- `public const int GL_NUM_EXTENSIONS = 0x821D;`
- `public const int GL_DEPTH_STENCIL = 0x84F9;`
- `public const int GL_DEPTH24_STENCIL8 = 0x88F0;`
- `public const int GL_FRAMEBUFFER_BINDING = 0x8CA6;`
- `public const int GL_RENDERBUFFER_BINDING = 0x8CA7;`
- `public const int GL_READ_FRAMEBUFFER = 0x8CA8;`
- `public const int GL_DRAW_FRAMEBUFFER = 0x8CA9;`
- `public const int GL_READ_FRAMEBUFFER_BINDING = 0x8CAA;`
- `public const int GL_FRAMEBUFFER_COMPLETE = 0x8CD5;`
- `public const int GL_COLOR_ATTACHMENT0 = 0x8CE0;`
- `public const int GL_DEPTH_ATTACHMENT = 0x8D00;`
- `public const int GL_STENCIL_ATTACHMENT = 0x8D20;`
- `public const int GL_FRAMEBUFFER = 0x8D40;`
- `public const int GL_RENDERBUFFER = 0x8D41;`
- `public const int GL_RENDERBUFFER_WIDTH = 0x8D42;`
- `public const int GL_RENDERBUFFER_HEIGHT = 0x8D43;`
- `public const int GL_STENCIL_INDEX8 = 0x8D48;`
- `public const int GL_TEXTURE_RECTANGLE = 0x84F5;`
- `public const int GL_TEXTURE_BINDING_RECTANGLE = 0x84F6;`
- `public const int GL_CONTEXT_CORE_PROFILE_BIT = 0x00000001;`
- `public const int GL_CONTEXT_COMPATIBILITY_PROFILE_BIT = 0x00000002;`
- `public const int GL_CONTEXT_PROFILE_MASK = 0x9126;`
- `public const int GL_DEVICE_LUID_EXT = 0x9599;`

### `src/Avalonia.OpenGL/GlErrors.cs`
- `public enum GlErrors`

### `src/Avalonia.OpenGL/GlInterface.cs`
- `public unsafe partial class GlInterface : GlBasicInfoInterface`
- `public string? Version { get; }`
- `public string? Vendor { get; }`
- `public string? Renderer { get; }`
- `public GlContextInfo ContextInfo { get; }`
- `public class GlContextInfo`
- `public GlVersion Version { get; }`
- `public HashSet<string> Extensions { get; }`
- `public GlContextInfo(GlVersion version, HashSet<string> extensions) {`
- `public static GlContextInfo Create(GlVersion version, Func<string, IntPtr> getProcAddress) {`
- `public GlInterface(GlVersion version, Func<string, IntPtr> getProcAddress) : this( GlContextInfo.Create(version, getProcAddress), getProcAddress) {`
- `public IntPtr GetProcAddress(string proc) => _getProcAddress(proc);`
- `public partial void ClearStencil(int s);`
- `public partial void ClearColor(float r, float g, float b, float a);`
- `public void ClearDepth(float value) {`
- `public partial void DepthFunc(int value);`
- `public partial void DepthMask(int value);`
- `public partial void Clear(int bits);`
- `public partial void Viewport(int x, int y, int width, int height);`
- `public partial void Flush();`
- `public partial void Finish();`
- `public partial void GenFramebuffers(int count, int* res);`
- `public int GenFramebuffer() {`
- `public partial void DeleteFramebuffers(int count, int* framebuffers);`
- `public void DeleteFramebuffer(int fb) {`
- `public partial void BindFramebuffer(int target, int fb);`
- `public partial int CheckFramebufferStatus(int target);`
- `public partial void BlitFramebuffer(int srcX0, int srcY0, int srcX1, int srcY1, int dstX0, int dstY0, int dstX1, int dstY1, int mask, int filter);`
- `public partial void GenRenderbuffers(int count, int* res);`
- `public int GenRenderbuffer() {`
- `public partial void DeleteRenderbuffers(int count, int* renderbuffers);`
- `public void DeleteRenderbuffer(int renderbuffer) {`
- `public partial void BindRenderbuffer(int target, int fb);`
- `public partial void RenderbufferStorage(int target, int internalFormat, int width, int height);`
- `public partial void FramebufferRenderbuffer(int target, int attachment, int renderbufferTarget, int renderbuffer);`
- `public partial void GenTextures(int count, int* res);`
- `public int GenTexture() {`
- `public partial void BindTexture(int target, int fb);`
- `public partial void ActiveTexture(int texture);`
- `public partial void DeleteTextures(int count, int* textures);`
- `public void DeleteTexture(int texture) => DeleteTextures(1, &texture);`
- `public partial void TexImage2D(int target, int level, int internalFormat, int width, int height, int border, int format, int type, IntPtr data);`
- `public partial void CopyTexSubImage2D(int target, int level, int xoffset, int yoffset, int x, int y, int width, int height);`
- `public partial void TexParameteri(int target, int name, int value);`
- `public partial void FramebufferTexture2D(int target, int attachment, int texTarget, int texture, int level);`
- `public partial int CreateShader(int shaderType);`
- `public partial void ShaderSource(int shader, int count, IntPtr strings, IntPtr lengths);`
- `public void ShaderSourceString(int shader, string source) {`
- `public partial void CompileShader(int shader);`
- `public partial void GetShaderiv(int shader, int name, int* parameters);`
- `public partial void GetShaderInfoLog(int shader, int maxLength, out int length, void* infoLog);`
- `public unsafe string? CompileShaderAndGetError(int shader, string source) {`
- `public partial int CreateProgram();`
- `public partial void AttachShader(int program, int shader);`
- `public partial void LinkProgram(int program);`
- `public partial void GetProgramiv(int program, int name, int* parameters);`
- `public partial void GetProgramInfoLog(int program, int maxLength, out int len, void* infoLog);`
- `public unsafe string? LinkProgramAndGetError(int program) {`
- `public partial void BindAttribLocation(int program, int index, IntPtr name);`
- `public void BindAttribLocationString(int program, int index, string name) {`
- `public partial void GenBuffers(int len, int* rv);`
- `public int GenBuffer() {`
- `public partial void BindBuffer(int target, int buffer);`
- `public partial void BufferData(int target, IntPtr size, IntPtr data, int usage);`
- `public partial int GetAttribLocation(int program, IntPtr name);`
- `public int GetAttribLocationString(int program, string name) {`
- `public partial void VertexAttribPointer(int index, int size, int type, int normalized, int stride, IntPtr pointer);`
- `public partial void EnableVertexAttribArray(int index);`
- `public partial void UseProgram(int program);`
- `public partial void DrawArrays(int mode, int first, IntPtr count);`
- `public partial void DrawElements(int mode, int count, int type, IntPtr indices);`
- `public partial int GetUniformLocation(int program, IntPtr name);`
- `public int GetUniformLocationString(int program, string name) {`
- `public partial void Uniform1f(int location, float falue);`
- `public partial void UniformMatrix4fv(int location, int count, bool transpose, void* value);`
- `public partial void Enable(int what);`
- `public partial void Disable(int what);`
- `public partial void DeleteBuffers(int count, int* buffers);`
- `public void DeleteBuffer(int buffer) => DeleteBuffers(1, &buffer);`
- `public partial void DeleteProgram(int program);`
- `public partial void DeleteShader(int shader);`
- `public partial void GetRenderbufferParameteriv(int target, int name, out int value);`
- `public partial void DeleteVertexArrays(int count, int* arrays);`
- `public void DeleteVertexArray(int array) => DeleteVertexArrays(1, &array);`
- `public partial void BindVertexArray(int array);`
- `public partial void GenVertexArrays(int n, int* rv);`
- `public int GenVertexArray() {`
- `public static GlInterface FromNativeUtf8GetProcAddress(GlVersion version, Func<IntPtr, IntPtr> getProcAddress) {`

### `src/Avalonia.OpenGL/GlVersion.cs`
- `public enum GlProfileType`
- `public record struct GlVersion`
- `public GlProfileType Type { get; }`
- `public int Major { get; }`
- `public int Minor { get; }`
- `public bool IsCompatibilityProfile { get; }`
- `public GlVersion(GlProfileType type, int major, int minor) : this(type, major, minor, false) { }`
- `public GlVersion(GlProfileType type, int major, int minor, bool isCompatibilityProfile) {`

### `src/Avalonia.OpenGL/IGlContext.cs`
- `public interface IGlContext : IPlatformGraphicsContext`
- `public interface IGlPlatformSurfaceRenderTargetFactory`

### `src/Avalonia.OpenGL/IGlContextExternalObjectsFeature.cs`
- Namespace: `Avalonia.OpenGL`
- `public interface IGlContextExternalObjectsFeature`
- `public byte[]? DeviceLuid { get; }`
- `public byte[]? DeviceUuid { get; }`
- `public interface IGlExternalSemaphore : IDisposable`
- `public interface IGlExportableExternalSemaphore : IGlExternalSemaphore`
- `public interface IGlExternalImageTexture : IDisposable`
- `public int TextureType { get; }`
- `public interface IGlExportableExternalImageTexture : IGlExternalImageTexture`

### `src/Avalonia.OpenGL/IOpenGlTextureSharingRenderInterfaceContextFeature.cs`
- `public interface IOpenGlTextureSharingRenderInterfaceContextFeature`
- `public interface ICompositionImportableOpenGlSharedTexture : ICompositionImportableSharedGpuContextImage`

### `src/Avalonia.OpenGL/IPlatformGraphicsOpenGlContextFactory.cs`
- Namespace: `Avalonia.OpenGL`
- `public interface IPlatformGraphicsOpenGlContextFactory`

### `src/Avalonia.OpenGL/OpenGlException.cs`
- `public class OpenGlException : Exception`
- `public int? ErrorCode { get; }`
- `public OpenGlException(string? message) : base(message) {`
- `public static OpenGlException GetFormattedException(string funcName, EglInterface egl) {`
- `public static OpenGlException GetFormattedException(string funcName, GlInterface gl) {`
- `public static OpenGlException GetFormattedException(string funcName, int errorCode) =>`
- `public static OpenGlException GetFormattedEglException(string funcName, int errorCode) =>`

### `src/Avalonia.OpenGL/Surfaces/IGlPlatformSurface.cs`
- `public interface IGlPlatformSurface`

### `src/Avalonia.OpenGL/Surfaces/IGlPlatformSurfaceRenderTarget.cs`
- `public interface IGlPlatformSurfaceRenderTarget : IDisposable`
- `public interface IGlPlatformSurfaceRenderTargetWithCorruptionInfo : IGlPlatformSurfaceRenderTarget`
- `public interface IGlPlatformSurfaceRenderTarget2 : IGlPlatformSurfaceRenderTargetWithCorruptionInfo`

### `src/Avalonia.OpenGL/Surfaces/IGlPlatformSurfaceRenderingSession.cs`
- `public interface IGlPlatformSurfaceRenderingSession : IDisposable`

### `src/Avalonia.Remote.Protocol/AvaloniaRemoteMessageGuidAttribute.cs`
- `public sealed class AvaloniaRemoteMessageGuidAttribute : Attribute`
- `public Guid Guid { get; }`
- `public AvaloniaRemoteMessageGuidAttribute(string guid) {`

### `src/Avalonia.Remote.Protocol/BsonTcpTransport.cs`
- `public class BsonTcpTransport : TcpTransportBase`
- `public BsonTcpTransport(IMessageTypeResolver resolver) : base(resolver) {`
- `public BsonTcpTransport() : this(new DefaultMessageTypeResolver(typeof(BsonTcpTransport).GetTypeInfo().Assembly)) {`

### `src/Avalonia.Remote.Protocol/DefaultMessageTypeResolver.cs`
- `public class DefaultMessageTypeResolver : IMessageTypeResolver`
- `public DefaultMessageTypeResolver(params Assembly[] assemblies) {`
- `public Type GetByGuid(Guid id) => _guidsToTypes[id];`
- `public Guid GetGuid(Type type) => _typesToGuids[type];`

### `src/Avalonia.Remote.Protocol/DesignMessages.cs`
- `public class UpdateXamlMessage`
- `public string Xaml { get; set; }`
- `public string AssemblyPath { get; set; }`
- `public string XamlFileProjectPath { get; set; }`
- `public class UpdateXamlResultMessage`
- `public string Error { get; set; }`
- `public string Handle { get; set; }`
- `public ExceptionDetails Exception { get; set; }`
- `public class StartDesignerSessionMessage`
- `public string SessionId { get; set; }`
- `public class ExceptionDetails`
- `public ExceptionDetails() {`
- `public ExceptionDetails(Exception e) {`
- `public string ExceptionType { get; set; }`
- `public string Message { get; set; }`
- `public int? LineNumber { get; set; }`
- `public int? LinePosition { get; set; }`

### `src/Avalonia.Remote.Protocol/IMessageTypeResolver.cs`
- `public interface IMessageTypeResolver`

### `src/Avalonia.Remote.Protocol/ITransport.cs`
- `public interface IAvaloniaRemoteTransportConnection : IDisposable`

### `src/Avalonia.Remote.Protocol/InputMessages.cs`
- `public enum InputModifiers`
- `public enum MouseButton`
- `public abstract class InputEventMessageBase`
- `public InputModifiers[]? Modifiers { get; set; }`
- `public abstract class PointerEventMessageBase : InputEventMessageBase`
- `public double X { get; set; }`
- `public double Y { get; set; }`
- `public class PointerMovedEventMessage : PointerEventMessageBase`
- `public class PointerPressedEventMessage : PointerEventMessageBase`
- `public MouseButton Button { get; set; }`
- `public class PointerReleasedEventMessage : PointerEventMessageBase`
- `public MouseButton Button { get; set; }`
- `public class ScrollEventMessage : PointerEventMessageBase`
- `public double DeltaX { get; set; }`
- `public double DeltaY { get; set; }`
- `public class KeyEventMessage : InputEventMessageBase`
- `public bool IsDown { get; set; }`
- `public Key Key { get; set; }`
- `public PhysicalKey PhysicalKey { get; set; }`
- `public string? KeySymbol { get; set; }`
- `public class TextInputEventMessage : InputEventMessageBase`
- `public string Text { get; set; } = string.Empty;`

### `src/Avalonia.Remote.Protocol/MetsysBson.cs`
- `public interface IExpando`
- `public static class Helper`
- `public static readonly DateTime Epoch = new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc);`
- `public interface ITypeConfiguration<T>`
- `public static class ExpressionHelper`
- `public static string GetName(this MemberExpression expression) {`
- `public static MemberExpression GetMemberExpression<T, TValue>(this Expression<Func<T, TValue>> expression) {`

### `src/Avalonia.Remote.Protocol/TcpTransportBase.cs`
- `public abstract class TcpTransportBase`
- `public TcpTransportBase(IMessageTypeResolver resolver) {`
- `public IDisposable Listen(IPAddress address, int port, Action<IAvaloniaRemoteTransportConnection> cb) {`
- `public async Task<IAvaloniaRemoteTransportConnection> Connect(IPAddress address, int port) {`

### `src/Avalonia.Remote.Protocol/TransportConnectionWrapper.cs`
- `public class TransportConnectionWrapper : IAvaloniaRemoteTransportConnection`
- `public TransportConnectionWrapper(IAvaloniaRemoteTransportConnection conn) {`
- `public void Dispose() => _conn.Dispose();`
- `public Task Send(object data) {`
- `public event Action<IAvaloniaRemoteTransportConnection, object> OnMessage {`
- `public event Action<IAvaloniaRemoteTransportConnection, Exception> OnException {`
- `public void Start() => _conn.Start();`

### `src/Avalonia.Remote.Protocol/TransportMessages.cs`
- `public class HtmlTransportStartedMessage`
- `public string Uri { get; set; }`

### `src/Avalonia.Remote.Protocol/ViewportMessages.cs`
- `public enum PixelFormat`
- `public class MeasureViewportMessage`
- `public double Width { get; set; }`
- `public double Height { get; set; }`
- `public class ClientViewportAllocatedMessage`
- `public double Width { get; set; }`
- `public double Height { get; set; }`
- `public double DpiX { get; set; }`
- `public double DpiY { get; set; }`
- `public class RequestViewportResizeMessage`
- `public double Width { get; set; }`
- `public double Height { get; set; }`
- `public class ClientSupportedPixelFormatsMessage`
- `public PixelFormat[] Formats { get; set; }`
- `public class ClientRenderInfoMessage`
- `public double DpiX { get; set; }`
- `public double DpiY { get; set; }`
- `public class FrameReceivedMessage`
- `public long SequenceId { get; set; }`
- `public class FrameMessage`
- `public long SequenceId { get; set; }`
- `public PixelFormat Format { get; set; }`
- `public byte[] Data { get; set; }`
- `public int Width { get; set; }`
- `public int Height { get; set; }`
- `public int Stride { get; set; }`
- `public double DpiX { get; set; }`
- `public double DpiY { get; set; }`

### `src/Avalonia.Themes.Fluent/ColorPaletteResources.Properties.cs`
- Namespace: `Avalonia.Themes.Fluent`
- `public partial class ColorPaletteResources`
- `public static readonly DirectProperty<ColorPaletteResources, Color> AccentProperty = AvaloniaProperty.RegisterDirect<ColorPaletteResources, Color>(nameof(Accent), r => r.Accent, (r, v) => r.Accent = v);`
- `public Color Accent {`
- `public Color AltHigh { get => GetColor("SystemAltHighColor"); set => SetColor("SystemAltHighColor", value); }`
- `public Color AltLow { get => GetColor("SystemAltLowColor"); set => SetColor("SystemAltLowColor", value); }`
- `public Color AltMedium { get => GetColor("SystemAltMediumColor"); set => SetColor("SystemAltMediumColor", value); }`
- `public Color AltMediumHigh { get => GetColor("SystemAltMediumHighColor"); set => SetColor("SystemAltMediumHighColor", value); }`
- `public Color AltMediumLow { get => GetColor("SystemAltMediumLowColor"); set => SetColor("SystemAltMediumLowColor", value); }`
- `public Color BaseHigh { get => GetColor("SystemBaseHighColor"); set => SetColor("SystemBaseHighColor", value); }`
- `public Color BaseLow { get => GetColor("SystemBaseLowColor"); set => SetColor("SystemBaseLowColor", value); }`
- `public Color BaseMedium { get => GetColor("SystemBaseMediumColor"); set => SetColor("SystemBaseMediumColor", value); }`
- `public Color BaseMediumHigh { get => GetColor("SystemBaseMediumHighColor"); set => SetColor("SystemBaseMediumHighColor", value); }`
- `public Color BaseMediumLow { get => GetColor("SystemBaseMediumLowColor"); set => SetColor("SystemBaseMediumLowColor", value); }`
- `public Color ChromeAltLow { get => GetColor("SystemChromeAltLowColor"); set => SetColor("SystemChromeAltLowColor", value); }`
- `public Color ChromeBlackHigh { get => GetColor("SystemChromeBlackHighColor"); set => SetColor("SystemChromeBlackHighColor", value); }`
- `public Color ChromeBlackLow { get => GetColor("SystemChromeBlackLowColor"); set => SetColor("SystemChromeBlackLowColor", value); }`
- `public Color ChromeBlackMedium { get => GetColor("SystemChromeBlackMediumColor"); set => SetColor("SystemChromeBlackMediumColor", value); }`
- `public Color ChromeBlackMediumLow { get => GetColor("SystemChromeBlackMediumLowColor"); set => SetColor("SystemChromeBlackMediumLowColor", value); }`
- `public Color ChromeDisabledHigh { get => GetColor("SystemChromeDisabledHighColor"); set => SetColor("SystemChromeDisabledHighColor", value); }`
- `public Color ChromeDisabledLow { get => GetColor("SystemChromeDisabledLowColor"); set => SetColor("SystemChromeDisabledLowColor", value); }`
- `public Color ChromeGray { get => GetColor("SystemChromeGrayColor"); set => SetColor("SystemChromeGrayColor", value); }`
- `public Color ChromeHigh { get => GetColor("SystemChromeHighColor"); set => SetColor("SystemChromeHighColor", value); }`
- `public Color ChromeLow { get => GetColor("SystemChromeLowColor"); set => SetColor("SystemChromeLowColor", value); }`
- `public Color ChromeMedium { get => GetColor("SystemChromeMediumColor"); set => SetColor("SystemChromeMediumColor", value); }`
- `public Color ChromeMediumLow { get => GetColor("SystemChromeMediumLowColor"); set => SetColor("SystemChromeMediumLowColor", value); }`
- `public Color ChromeWhite { get => GetColor("SystemChromeWhiteColor"); set => SetColor("SystemChromeWhiteColor", value); }`
- `public Color ErrorText { get => GetColor("SystemErrorTextColor"); set => SetColor("SystemErrorTextColor", value); }`
- `public Color ListLow { get => GetColor("SystemListLowColor"); set => SetColor("SystemListLowColor", value); }`
- `public Color ListMedium { get => GetColor("SystemListMediumColor"); set => SetColor("SystemListMediumColor", value); }`
- `public Color RegionColor { get => GetColor("SystemRegionColor"); set => SetColor("SystemRegionColor", value); }`

### `src/Avalonia.Themes.Fluent/ColorPaletteResources.cs`
- Namespace: `Avalonia.Themes.Fluent`
- `public partial class ColorPaletteResources : ResourceProvider`
- `public override bool HasResources => _hasAccentColor || _colors.Count > 0;`
- `public override bool TryGetResource(object key, ThemeVariant? theme, out object? value) {`

### `src/Avalonia.Themes.Fluent/FluentTheme.xaml.cs`
- `public enum DensityStyle`
- `public class FluentTheme : Styles, IResourceNode`
- `public FluentTheme(IServiceProvider? sp = null) {`
- `public static readonly DirectProperty<FluentTheme, DensityStyle> DensityStyleProperty = AvaloniaProperty.RegisterDirect<FluentTheme, DensityStyle>( nameof(DensityStyle), o => o.DensityStyle, (o, v) => o.DensityStyle = v);`
- `public DensityStyle DensityStyle {`
- `public IDictionary<ThemeVariant, ColorPaletteResources> Palettes { get; }`

### `src/Avalonia.Themes.Simple/SimpleTheme.xaml.cs`
- Namespace: `Avalonia.Themes.Simple`
- `public class SimpleTheme : Styles`
- `public SimpleTheme(IServiceProvider? sp = null) {`

### `src/Avalonia.Vulkan/IVulkanContextExternalObjectsFeature.cs`
- Namespace: `Avalonia.Vulkan`
- `public interface IVulkanContextExternalObjectsFeature`
- `public interface IVulkanExternalSemaphore : IDisposable`
- `public interface IVulkanExternalImage : IDisposable`

### `src/Avalonia.Vulkan/IVulkanDevice.cs`
- Namespace: `Avalonia.Vulkan`
- `public interface IVulkanDevice : IDisposable, IOptionalFeatureProvider`
- `public IntPtr Handle { get; }`
- `public IntPtr PhysicalDeviceHandle { get; }`
- `public IntPtr MainQueueHandle { get; }`
- `public uint GraphicsQueueFamilyIndex { get; }`
- `public IVulkanInstance Instance { get; }`
- `public IDisposable Lock();`
- `public IEnumerable<string> EnabledExtensions { get; }`
- `public interface IVulkanInstance`
- `public IntPtr Handle { get; }`
- `public IntPtr GetInstanceProcAddress(IntPtr instance, string name);`
- `public IntPtr GetDeviceProcAddress(IntPtr device, string name);`
- `public IEnumerable<string> EnabledExtensions { get; }`
- `public interface IVulkanPlatformGraphicsContext : IPlatformGraphicsContext`

### `src/Avalonia.Vulkan/IVulkanPlatformSurface.cs`
- Namespace: `Avalonia.Vulkan`
- `public interface IVulkanKhrSurfacePlatformSurface : IDisposable`
- `public interface IVulkanKhrSurfacePlatformSurfaceFactory`

### `src/Avalonia.Vulkan/IVulkanRenderTarget.cs`
- Namespace: `Avalonia.Vulkan`
- `public interface IVulkanRenderTarget : IDisposable`
- `public interface IVulkanRenderSession : IDisposable`
- `public bool IsYFlipped { get; }`

### `src/Avalonia.Vulkan/UnmanagedInterop/VulkanStructs.cs`
- `public struct VkMemoryTypesBuffer`
- `public VkMemoryType Element0;`
- `public VkMemoryType Element1;`
- `public VkMemoryType Element2;`
- `public VkMemoryType Element3;`
- `public VkMemoryType Element4;`
- `public VkMemoryType Element5;`
- `public VkMemoryType Element6;`
- `public VkMemoryType Element7;`
- `public VkMemoryType Element8;`
- `public VkMemoryType Element9;`
- `public VkMemoryType Element10;`
- `public VkMemoryType Element11;`
- `public VkMemoryType Element12;`
- `public VkMemoryType Element13;`
- `public VkMemoryType Element14;`
- `public VkMemoryType Element15;`
- `public VkMemoryType Element16;`
- `public VkMemoryType Element17;`
- `public VkMemoryType Element18;`
- `public VkMemoryType Element19;`
- `public VkMemoryType Element20;`
- `public VkMemoryType Element21;`
- `public VkMemoryType Element22;`
- `public VkMemoryType Element23;`
- `public VkMemoryType Element24;`
- `public VkMemoryType Element25;`
- `public VkMemoryType Element26;`
- `public VkMemoryType Element27;`
- `public VkMemoryType Element28;`
- `public VkMemoryType Element29;`
- `public VkMemoryType Element30;`
- `public VkMemoryType Element31;`
- `public ref VkMemoryType this[int index] {`
- `public struct VkMemoryHeapsBuffer`
- `public VkMemoryHeap Element0;`
- `public VkMemoryHeap Element1;`
- `public VkMemoryHeap Element2;`
- `public VkMemoryHeap Element3;`
- `public VkMemoryHeap Element4;`
- `public VkMemoryHeap Element5;`
- `public VkMemoryHeap Element6;`
- `public VkMemoryHeap Element7;`
- `public VkMemoryHeap Element8;`
- `public VkMemoryHeap Element9;`
- `public VkMemoryHeap Element10;`
- `public VkMemoryHeap Element11;`
- `public VkMemoryHeap Element12;`
- `public VkMemoryHeap Element13;`
- `public VkMemoryHeap Element14;`
- `public VkMemoryHeap Element15;`
- `public ref VkMemoryHeap this[int index] {`

### `src/Avalonia.Vulkan/VulkanException.cs`
- Namespace: `Avalonia.Vulkan`
- `public class VulkanException : Exception`
- `public VulkanException(string message) : base(message) {`
- `public VulkanException(string funcName, int res) : this(funcName, (VkResult)res) {`
- `public static void ThrowOnError(string funcName, int res) => ((VkResult)res).ThrowOnError(funcName);`

### `src/Avalonia.Vulkan/VulkanImageInfo.cs`
- Namespace: `Avalonia.Vulkan`
- `public record struct VulkanImageInfo`
- `public uint Format { get; set; }`
- `public PixelSize PixelSize { get; set; }`
- `public ulong Handle { get; set; }`
- `public uint Layout { get; set; }`
- `public uint Tiling { get; set; }`
- `public uint UsageFlags { get; set; }`
- `public uint LevelCount { get; set; }`
- `public uint SampleCount { get; set; }`
- `public ulong MemoryHandle { get; set; }`
- `public ulong ViewHandle { get; set; }`
- `public ulong MemorySize { get; set; }`
- `public bool IsProtected { get; set; }`

### `src/Avalonia.Vulkan/VulkanOptions.cs`
- Namespace: `Avalonia.Vulkan`
- `public class VulkanOptions`
- `public VulkanInstanceCreationOptions VulkanInstanceCreationOptions { get; set; } = new();`
- `public VulkanDeviceCreationOptions VulkanDeviceCreationOptions { get; set; } = new();`
- `public IVulkanDevice? CustomSharedDevice { get; set; }`
- `public class VulkanInstanceCreationOptions`
- `public VkGetInstanceProcAddressDelegate? CustomGetProcAddressDelegate { get; set; }`
- `public string? ApplicationName { get; set; }`
- `public Version VulkanVersion{ get; set; } = new Version(1, 1, 0);`
- `public IList<string> InstanceExtensions { get; set; } = new List<string>();`
- `public IList<string> EnabledLayers { get; set; } = new List<string>();`
- `public bool UseDebug { get; set; }`
- `public class VulkanDeviceCreationOptions`
- `public IList<string> DeviceExtensions { get; set; } = new List<string>();`
- `public bool PreferDiscreteGpu { get; set; }`
- `public bool RequireComputeBit { get; set; }`
- `public class VulkanPlatformSpecificOptions`
- `public IList<string> RequiredInstanceExtensions { get; set; } = new List<string>();`
- `public VkGetInstanceProcAddressDelegate? GetProcAddressDelegate { get; set; }`
- `public Func<IVulkanInstance, ulong>? DeviceCheckSurfaceFactory { get; set; }`
- `public Dictionary<Type, object> PlatformFeatures { get; set; } = new();`

### `src/Avalonia.Vulkan/VulkanPlatformGraphics.cs`
- Namespace: `Avalonia.Vulkan`
- `public class VulkanPlatformGraphics : IPlatformGraphics`
- `public VulkanPlatformGraphics(IVulkanDeviceFactory factory, VulkanPlatformSpecificOptions platformOptions) {`
- `public IPlatformGraphicsContext CreateContext() =>`
- `public IPlatformGraphicsContext GetSharedContext() {`
- `public bool UsesSharedContext => _factory.UsesShadedDevice;`
- `public interface IVulkanDeviceFactory`
- `public static VulkanPlatformGraphics? TryCreate(VulkanOptions options, VulkanPlatformSpecificOptions platformOptions) {`

### `src/Tizen/Avalonia.Tizen/NuiAvaloniaView.cs`
- Namespace: `Avalonia.Tizen`
- `public class NuiAvaloniaView : GLView, ITizenView, ITextInputMethodImpl`
- `public INativeControlHostImpl NativeControlHost { get; }`
- `public double Scaling => 1;`
- `public Size ClientSize => new(Size.Width, Size.Height);`
- `public IInputRoot InputRoot {`
- `public Control? Content {`
- `public event Action? OnSurfaceInit;`
- `public NuiAvaloniaView() : base(ColorFormat.RGBA8888) {`
- `public void SetClient(TextInputMethodClient? client) {`
- `public void SetCursorRect(Rect rect) {`
- `public void SetOptions(TextInputOptions options) =>`

### `src/Tizen/Avalonia.Tizen/NuiAvaloniaViewTextEditable.cs`
- Namespace: `Avalonia.Tizen`
- `public class NuiMultiLineTextInput : TextEditor, INuiTextInput`
- `public class NuiSingleLineTextInput : TextField, INuiTextInput`

### `src/Tizen/Avalonia.Tizen/NuiTizenApplication.cs`
- Namespace: `Avalonia.Tizen`
- `public class NuiTizenApplication<TApp> : NUIApplication`

### `src/Tizen/Avalonia.Tizen/NuiViewControlHandle.cs`
- Namespace: `Avalonia.Tizen`
- `public class NuiViewControlHandle : INativeControlHostDestroyableControlHandle`
- `public NuiViewControlHandle(View view) {`
- `public View View { get; set; }`
- `public IntPtr Handle => throw new NotSupportedException();`
- `public string? HandleDescriptor => ViewDescriptor;`
- `public void Destroy() => View.Dispose();`

### `src/Tizen/Avalonia.Tizen/TizenApplicationExtensions.cs`
- Namespace: `Avalonia.Tizen`
- `public static class TizenApplicationExtensions`
- `public static AppBuilder UseTizen(this AppBuilder builder) {`

### `src/tools/Avalonia.Analyzers/AvaloniaPropertyAnalyzer.CompileAnalyzer.cs`
- Namespace: `Avalonia.Analyzers`
- `public partial class AvaloniaPropertyAnalyzer`
- `public class CompileAnalyzer`
- `public CompileAnalyzer(CompilationStartAnalysisContext context, INamedTypeSymbol avaloniaObjectType) {`

### `src/tools/Avalonia.Analyzers/AvaloniaPropertyAnalyzer.cs`
- Namespace: `Avalonia.Analyzers`
- `public partial class AvaloniaPropertyAnalyzer : DiagnosticAnalyzer`
- `public override ImmutableArray<DiagnosticDescriptor> SupportedDiagnostics { get; } = ImmutableArray.Create(`
- `public override void Initialize(AnalysisContext context) {`
- `public class AvaloniaAnalysisException : Exception`
- `public AvaloniaAnalysisException(string message, Exception? innerException = null) : base(message, innerException) {`

### `src/tools/Avalonia.Analyzers/BitmapAnalyzer.cs`
- Namespace: `Avalonia.Analyzers`
- `public class BitmapAnalyzer: DiagnosticAnalyzer`
- `public const string DiagnosticId = "AVA2002";`
- `public override void Initialize(AnalysisContext context) {`
- `public override ImmutableArray<DiagnosticDescriptor> SupportedDiagnostics { get { return ImmutableArray.Create(_rule); } }`

### `src/tools/Avalonia.Analyzers/BitmapAnalyzerCSCodeFixProvider.cs`
- Namespace: `Avalonia.Analyzers`
- `public class BitmapAnalyzerCSCodeFixProvider : CodeFixProvider`
- `public override ImmutableArray<string> FixableDiagnosticIds { get; } =`
- `public override FixAllProvider? GetFixAllProvider() {`
- `public sealed override async Task RegisterCodeFixesAsync(CodeFixContext context) {`

### `src/tools/Avalonia.Analyzers/OnPropertyChangedOverrideAnalyzer.cs`
- Namespace: `Avalonia.Analyzers`
- `public class OnPropertyChangedOverrideAnalyzer : DiagnosticAnalyzer`
- `public const string DiagnosticId = "AVA2001";`
- `public override ImmutableArray<DiagnosticDescriptor> SupportedDiagnostics => ImmutableArray.Create(Rule);`
- `public override void Initialize(AnalysisContext context) {`

### `src/tools/DevAnalyzers/GenericVirtualAnalyzer.cs`
- Namespace: `DevAnalyzers`
- `public class GenericVirtualAnalyzer : DiagnosticAnalyzer`
- `public const string DiagnosticId = "AVADEV1001";`
- `public override ImmutableArray<DiagnosticDescriptor> SupportedDiagnostics => ImmutableArray.Create(Rule);`
- `public override void Initialize(AnalysisContext context) {`

### `src/tools/DevAnalyzers/OnPropertyChangedOverrideAnalyzer.cs`
- `public class OnPropertyChangedOverrideAnalyzer : DiagnosticAnalyzer`
- `public const string DiagnosticId = "AVADEV2001";`
- `public override ImmutableArray<DiagnosticDescriptor> SupportedDiagnostics => ImmutableArray.Create(Rule);`
- `public override void Initialize(AnalysisContext context) {`

### `src/tools/DevGenerators/CompilerDynamicDependenciesGenerator.cs`
- Namespace: `DevGenerators`
- `public class CompilerDynamicDependenciesGenerator : IIncrementalGenerator`
- `public void Initialize(IncrementalGeneratorInitializationContext context) {`

### `src/tools/DevGenerators/CompositionGenerator/CompositionRoslynGenerator.cs`
- `public class CompositionRoslynGenerator : IIncrementalGenerator`
- `public void Initialize(IncrementalGeneratorInitializationContext context) {`

### `src/tools/DevGenerators/CompositionGenerator/Config.cs`
- `public class GConfig`
- `public List<GUsing> Usings { get; set; } = new List<GUsing>();`
- `public List<GManualClass> ManualClasses { get; set; } = new List<GManualClass>();`
- `public List<GClass> Classes { get; set; } = new List<GClass>();`
- `public List<GAnimationType> KeyFrameAnimations { get; set; } = new List<GAnimationType>();`
- `public class GUsing`
- `public string Name { get; set; }`
- `public class GManualClass`
- `public string Name { get; set; }`
- `public bool Passthrough { get; set; }`
- `public string ServerName { get; set; }`
- `public class GImplements`
- `public string Name { get; set; }`
- `public string ServerName { get; set; }`
- `public class GClass`
- `public string Name { get; set; }`
- `public string Inherits { get; set; }`
- `public string ChangesBase { get; set; }`
- `public string ServerBase { get; set; }`
- `public bool CustomCtor { get; set; }`
- `public bool CustomServerCtor { get; set; }`
- `public bool Internal { get; set; }`
- `public bool ServerOnly { get; set; }`
- `public List<GImplements> Implements { get; set; } = new List<GImplements>();`
- `public bool Abstract { get; set; }`
- `public List<GProperty> Properties { get; set; } = new List<GProperty>();`
- `public class GBrush : GClass`
- `public bool CustomUpdate { get; set; }`
- `public GBrush() {`
- `public class GList : GClass`
- `public string ItemType { get; set; }`
- `public class GProperty`
- `public string Name { get; set; }`
- `public string ClientName { get; set; }`
- `public string Type { get; set; }`
- `public string DefaultValue { get; set; }`
- `public bool Animated { get; set; }`
- `public bool InternalSet { get; set; }`
- `public bool Internal { get; set; }`
- `public bool Private { get; set; }`
- `public class GAnimationType`
- `public string Name { get; set; }`
- `public string Type { get; set; }`

### `src/tools/DevGenerators/CompositionGenerator/Extensions.cs`
- `public static class Extensions`
- `public static ClassDeclarationSyntax AddModifiers(this ClassDeclarationSyntax cl, params SyntaxKind[]? modifiers) {`
- `public static MethodDeclarationSyntax AddModifiers(this MethodDeclarationSyntax cl, params SyntaxKind[]? modifiers) {`
- `public static PropertyDeclarationSyntax AddModifiers(this PropertyDeclarationSyntax cl, params SyntaxKind[]? modifiers) {`
- `public static ConstructorDeclarationSyntax AddModifiers(this ConstructorDeclarationSyntax cl, params SyntaxKind[]? modifiers) {`
- `public static AccessorDeclarationSyntax AddModifiers(this AccessorDeclarationSyntax cl, params SyntaxKind[]? modifiers) {`
- `public static EnumDeclarationSyntax AddModifiers(this EnumDeclarationSyntax cl, params SyntaxKind[]? modifiers) {`
- `public static string WithLowerFirst(this string s) {`
- `public static ExpressionSyntax MemberAccess(params string[]? identifiers) {`
- `public static ExpressionSyntax MemberAccess(ExpressionSyntax expr, params string[] identifiers) {`
- `public static MemberAccessExpressionSyntax MemberAccess(ExpressionSyntax expr, string identifier) =>`
- `public static ExpressionSyntax ConditionalMemberAccess(ExpressionSyntax expr, string member, bool checkNull) {`
- `public static ClassDeclarationSyntax WithBaseType(this ClassDeclarationSyntax cl, string bt) {`
- `public static string StripPrefix(this string s, string prefix) => string.IsNullOrEmpty(s)`

### `src/tools/DevGenerators/CompositionGenerator/Generator.ConfigHelpers.cs`
- Namespace: `Avalonia.SourceGenerator.CompositionGenerator`
- `public partial class Generator`

### `src/tools/DevGenerators/CompositionGenerator/Generator.KeyFrameAnimation.cs`
- `public partial class Generator`
- `public partial class Compositor`

### `src/tools/DevGenerators/CompositionGenerator/Generator.ListProxy.cs`
- `public partial class Generator`

### `src/tools/DevGenerators/CompositionGenerator/Generator.Utils.cs`
- `public partial class Generator`

### `src/tools/DevGenerators/CompositionGenerator/Generator.cs`
- `public partial class Generator`
- `public Generator(ICompositionGeneratorSink output, GConfig config) {`
- `public void Generate() {`

### `src/tools/DevGenerators/CompositionGenerator/ICompositionGeneratorSink.cs`
- Namespace: `Avalonia.SourceGenerator.CompositionGenerator`
- `public interface ICompositionGeneratorSink`

### `src/tools/DevGenerators/EnumMemberDictionaryGenerator.cs`
- Namespace: `DevGenerators`
- `public class EnumMemberDictionaryGenerator : IIncrementalGenerator`
- `public void Initialize(IncrementalGeneratorInitializationContext context) {`

### `src/tools/DevGenerators/GetProcAddressInitialization.cs`
- Namespace: `Generator`
- `public class GetProcAddressInitializationGenerator : IIncrementalGenerator`
- `public void Initialize(IncrementalGeneratorInitializationContext context) {`

### `src/tools/DevGenerators/SubtypesFactoryGenerator.cs`
- `public class SubtypesFactoryGenerator : IIncrementalGenerator`
- `public void Initialize(IncrementalGeneratorInitializationContext context) {`

### `src/tools/DevGenerators/X11AtomsGenerator.cs`
- Namespace: `DevGenerators`
- `public class X11AtomsGenerator : IIncrementalGenerator`
- `public void Initialize(IncrementalGeneratorInitializationContext context) {`

## Property, Data, Styling, Threading

### `src/Avalonia.Base/Animation/Animatable.cs`
- `public class Animatable : AvaloniaObject`
- `public static readonly StyledProperty<Transitions?> TransitionsProperty = AvaloniaProperty.Register<Animatable, Transitions?>(nameof(Transitions));`
- `public Transitions? Transitions {`

### `src/Avalonia.Base/Animation/Animation.cs`
- `public sealed partial class Animation : AvaloniaObject, IAnimation`
- `public static readonly DirectProperty<Animation, TimeSpan> DurationProperty = AvaloniaProperty.RegisterDirect<Animation, TimeSpan>( nameof(Duration), o => o._duration,`
- `public static readonly DirectProperty<Animation, IterationCount> IterationCountProperty = AvaloniaProperty.RegisterDirect<Animation, IterationCount>( nameof(IterationCount), o => o._iterationCount,`
- `public static readonly DirectProperty<Animation, PlaybackDirection> PlaybackDirectionProperty = AvaloniaProperty.RegisterDirect<Animation, PlaybackDirection>( nameof(PlaybackDirection), o => o._playbackDirection,`
- `public static readonly DirectProperty<Animation, FillMode> FillModeProperty = AvaloniaProperty.RegisterDirect<Animation, FillMode>( nameof(FillMode), o => o._fillMode,`
- `public static readonly DirectProperty<Animation, Easing> EasingProperty = AvaloniaProperty.RegisterDirect<Animation, Easing>( nameof(Easing), o => o._easing,`
- `public static readonly DirectProperty<Animation, TimeSpan> DelayProperty = AvaloniaProperty.RegisterDirect<Animation, TimeSpan>( nameof(Delay), o => o._delay,`
- `public static readonly DirectProperty<Animation, TimeSpan> DelayBetweenIterationsProperty = AvaloniaProperty.RegisterDirect<Animation, TimeSpan>( nameof(DelayBetweenIterations), o => o._delayBetweenIterations,`
- `public static readonly DirectProperty<Animation, double> SpeedRatioProperty = AvaloniaProperty.RegisterDirect<Animation, double>( nameof(SpeedRatio), o => o._speedRatio,`
- `public TimeSpan Duration {`
- `public IterationCount IterationCount {`
- `public PlaybackDirection PlaybackDirection {`
- `public FillMode FillMode {`
- `public Easing Easing {`
- `public TimeSpan Delay {`
- `public TimeSpan DelayBetweenIterations {`
- `public double SpeedRatio {`
- `public KeyFrames Children { get; } = new KeyFrames();`
- `public Task RunAsync(Animatable control, CancellationToken cancellationToken = default) =>`

### `src/Avalonia.Base/Animation/CompositePageTransition.cs`
- `public class CompositePageTransition : IPageTransition`
- `public List<IPageTransition> PageTransitions { get; set; } = new List<IPageTransition>();`
- `public Task Start(Visual? from, Visual? to, bool forward, CancellationToken cancellationToken) {`

### `src/Avalonia.Base/Animation/CrossFade.cs`
- `public class CrossFade : IPageTransition`
- `public CrossFade() : this(TimeSpan.Zero) {`
- `public CrossFade(TimeSpan duration) {`
- `public TimeSpan Duration {`
- `public Easing FadeInEasing {`
- `public Easing FadeOutEasing {`
- `public async Task Start(Visual? from, Visual? to, CancellationToken cancellationToken) {`

### `src/Avalonia.Base/Animation/Cue.cs`
- `public readonly record struct Cue : IEquatable<Cue>, IEquatable<double>`
- `public double CueValue { get; }`
- `public Cue(double value) {`
- `public static Cue Parse(string value, CultureInfo? culture) {`
- `public bool Equals(double other) {`
- `public class CueTypeConverter : TypeConverter`
- `public override bool CanConvertFrom(ITypeDescriptorContext? context, Type sourceType) {`
- `public override object ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object value) {`

### `src/Avalonia.Base/Animation/Easings/BackEaseIn.cs`
- `public class BackEaseIn : Easing`
- `public override double Ease(double p) {`

### `src/Avalonia.Base/Animation/Easings/BackEaseInOut.cs`
- `public class BackEaseInOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/BackEaseOut.cs`
- `public class BackEaseOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/BounceEaseIn.cs`
- `public class BounceEaseIn : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/BounceEaseInOut.cs`
- `public class BounceEaseInOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/BounceEaseOut.cs`
- `public class BounceEaseOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/CircularEaseIn.cs`
- `public class CircularEaseIn : Easing`
- `public override double Ease(double p) {`

### `src/Avalonia.Base/Animation/Easings/CircularEaseInOut.cs`
- `public class CircularEaseInOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/CircularEaseOut.cs`
- `public class CircularEaseOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/CubicBezierEasing.cs`
- Namespace: `Avalonia.Animation.Easings`
- `public sealed class CubicBezierEasing : IEasing`
- `public Point ControlPoint2 { get; set; }`
- `public Point ControlPoint1 { get; set; }`

### `src/Avalonia.Base/Animation/Easings/CubicEaseIn.cs`
- `public class CubicEaseIn : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/CubicEaseInOut.cs`
- `public class CubicEaseInOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/CubicEaseOut.cs`
- `public class CubicEaseOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/Easing.cs`
- `public abstract partial class Easing : IEasing`
- `public abstract double Ease(double progress);`
- `public static Easing Parse(string e) {`

### `src/Avalonia.Base/Animation/Easings/EasingTypeConverter.cs`
- `public class EasingTypeConverter : TypeConverter`
- `public override bool CanConvertFrom(ITypeDescriptorContext? context, Type sourceType) {`
- `public override object ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object value) {`

### `src/Avalonia.Base/Animation/Easings/ElasticEaseIn.cs`
- `public class ElasticEaseIn : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/ElasticEaseInOut.cs`
- `public class ElasticEaseInOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/ElasticEaseOut.cs`
- `public class ElasticEaseOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/ExponentialEaseIn.cs`
- `public class ExponentialEaseIn : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/ExponentialEaseInOut.cs`
- `public class ExponentialEaseInOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/ExponentialEaseOut.cs`
- `public class ExponentialEaseOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/IEasing.cs`
- `public interface IEasing`

### `src/Avalonia.Base/Animation/Easings/LinearEasing.cs`
- `public class LinearEasing : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/QuadraticEaseIn.cs`
- `public class QuadraticEaseIn : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/QuadraticEaseInOut.cs`
- `public class QuadraticEaseInOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/QuadraticEaseOut.cs`
- `public class QuadraticEaseOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/QuarticEaseIn.cs`
- `public class QuarticEaseIn : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/QuarticEaseInOut.cs`
- `public class QuarticEaseInOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/QuarticEaseOut.cs`
- `public class QuarticEaseOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/QuinticEaseIn.cs`
- `public class QuinticEaseIn : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/QuinticEaseInOut.cs`
- `public class QuinticEaseInOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/QuinticEaseOut.cs`
- `public class QuinticEaseOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/SineEaseIn.cs`
- `public class SineEaseIn : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/SineEaseInOut.cs`
- `public class SineEaseInOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/SineEaseOut.cs`
- `public class SineEaseOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/SplineEasing.cs`
- `public class SplineEasing : Easing`
- `public double X1 {`
- `public double Y1 {`
- `public double X2 {`
- `public double Y2 {`
- `public SplineEasing(double x1 = 0d, double y1 = 0d, double x2 = 1d, double y2 = 1d) {`
- `public SplineEasing(KeySpline keySpline) {`
- `public SplineEasing() {`
- `public override double Ease(double progress) =>`

### `src/Avalonia.Base/Animation/Easings/SpringEasing.cs`
- `public class SpringEasing : Easing`
- `public double Mass {`
- `public double Stiffness {`
- `public double Damping {`
- `public double InitialVelocity {`
- `public SpringEasing(double mass = 0d, double stiffness = 0d, double damping = 0d, double initialVelocity = 0d) {`
- `public SpringEasing() {`
- `public override double Ease(double progress) => _internalSpring.GetSpringProgress(progress);`

### `src/Avalonia.Base/Animation/FillMode.cs`
- `public enum FillMode`

### `src/Avalonia.Base/Animation/IAnimation.cs`
- `public interface IAnimation`

### `src/Avalonia.Base/Animation/IAnimationSetter.cs`
- `public interface IAnimationSetter`

### `src/Avalonia.Base/Animation/ICustomAnimator.cs`
- Namespace: `Avalonia.Animation`
- `public abstract class CustomAnimatorBase`
- `public abstract class CustomAnimatorBase<T> : CustomAnimatorBase`
- `public abstract T Interpolate(double progress, T oldValue, T newValue);`
- `public interface ICustomAnimator`
- `public abstract class InterpolatingAnimator<T> : ICustomAnimator`
- `public abstract T Interpolate(double progress, T oldValue, T newValue);`

### `src/Avalonia.Base/Animation/IPageTransition.cs`
- `public interface IPageTransition`

### `src/Avalonia.Base/Animation/ITransition.cs`
- `public interface ITransition`

### `src/Avalonia.Base/Animation/InterpolatingTransitionBase.cs`
- Namespace: `Avalonia.Animation`
- `public abstract class InterpolatingTransitionBase<T> : Transition<T>`

### `src/Avalonia.Base/Animation/IterationCount.cs`
- `public enum IterationType`
- `public struct IterationCount : IEquatable<IterationCount>`
- `public IterationCount(ulong value) : this(value, IterationType.Many) {`
- `public IterationCount(ulong value, IterationType type) {`
- `public static IterationCount Infinite => new IterationCount(0, IterationType.Infinite);`
- `public IterationType RepeatType => _type;`
- `public bool IsInfinite => _type == IterationType.Infinite;`
- `public ulong Value => _value;`
- `public static bool operator ==(IterationCount a, IterationCount b) {`
- `public static bool operator !=(IterationCount rc1, IterationCount rc2) {`
- `public override bool Equals(object? o) {`
- `public bool Equals(IterationCount IterationCount) {`
- `public override int GetHashCode() {`
- `public override string ToString() {`
- `public static IterationCount Parse(string s) {`

### `src/Avalonia.Base/Animation/IterationCountTypeConverter.cs`
- `public class IterationCountTypeConverter : TypeConverter`
- `public override bool CanConvertFrom(ITypeDescriptorContext? context, Type sourceType) {`
- `public override object ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object value) {`

### `src/Avalonia.Base/Animation/KeyFrame.cs`
- `public sealed class KeyFrame : AvaloniaObject`
- `public KeyFrame() {`
- `public AvaloniaList<IAnimationSetter> Setters { get; } = new AvaloniaList<IAnimationSetter>();`
- `public TimeSpan KeyTime {`
- `public Cue Cue {`
- `public KeySpline? KeySpline {`

### `src/Avalonia.Base/Animation/KeyFrames.cs`
- `public sealed class KeyFrames : AvaloniaList<KeyFrame>`
- `public KeyFrames() {`
- `public KeyFrames(IEnumerable<KeyFrame> items) : base(items) {`

### `src/Avalonia.Base/Animation/KeySpline.cs`
- `public sealed class KeySpline : AvaloniaObject`
- `public KeySpline() {`
- `public KeySpline(double x1, double y1, double x2, double y2) {`
- `public static KeySpline Parse(string value, CultureInfo? culture) {`
- `public double ControlPointX1 {`
- `public double ControlPointY1 {`
- `public double ControlPointX2 {`
- `public double ControlPointY2 {`
- `public double GetSplineProgress(double linearProgress) {`
- `public bool IsValid() {`

### `src/Avalonia.Base/Animation/KeySplineTypeConverter.cs`
- `public class KeySplineTypeConverter : TypeConverter`
- `public override bool CanConvertFrom(ITypeDescriptorContext? context, Type sourceType) {`
- `public override object ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object value) {`

### `src/Avalonia.Base/Animation/PageSlide.cs`
- `public class PageSlide : IPageTransition`
- `public enum SlideAxis`
- `public PageSlide() {`
- `public PageSlide(TimeSpan duration, SlideAxis orientation = SlideAxis.Horizontal) {`
- `public TimeSpan Duration { get; set; }`
- `public SlideAxis Orientation { get; set; }`
- `public Easing SlideInEasing { get; set; } = new LinearEasing();`
- `public Easing SlideOutEasing { get; set; } = new LinearEasing();`
- `public virtual async Task Start(Visual? from, Visual? to, bool forward, CancellationToken cancellationToken) {`

### `src/Avalonia.Base/Animation/PlayState.cs`
- `public enum PlayState`

### `src/Avalonia.Base/Animation/PlaybackDirection.cs`
- `public enum PlaybackDirection`

### `src/Avalonia.Base/Animation/Transition.cs`
- `public abstract class Transition<T> : TransitionBase`

### `src/Avalonia.Base/Animation/TransitionBase.cs`
- `public abstract class TransitionBase : AvaloniaObject, ITransition`
- `public static readonly DirectProperty<TransitionBase, TimeSpan> DurationProperty = AvaloniaProperty.RegisterDirect<TransitionBase, TimeSpan>( nameof(Duration), o => o._duration,`
- `public static readonly DirectProperty<TransitionBase, TimeSpan> DelayProperty = AvaloniaProperty.RegisterDirect<TransitionBase, TimeSpan>( nameof(Delay), o => o._delay,`
- `public static readonly DirectProperty<TransitionBase, Easing> EasingProperty = AvaloniaProperty.RegisterDirect<TransitionBase, Easing>( nameof(Easing), o => o._easing,`
- `public static readonly DirectProperty<TransitionBase, AvaloniaProperty?> PropertyProperty = AvaloniaProperty.RegisterDirect<TransitionBase, AvaloniaProperty?>( nameof(Property), o => o._prop,`
- `public TimeSpan Duration {`
- `public TimeSpan Delay {`
- `public Easing Easing {`
- `public AvaloniaProperty? Property {`

### `src/Avalonia.Base/Animation/Transitions.cs`
- `public sealed class Transitions : AvaloniaList<ITransition>, IAvaloniaListItemValidator<ITransition>`
- `public Transitions() {`

### `src/Avalonia.Base/Animation/Transitions/BoolTransition.cs`
- `public class BoolTransition : Transition<bool>`

### `src/Avalonia.Base/Animation/Transitions/BoxShadowsTransition.cs`
- `public class BoxShadowsTransition : Transition<BoxShadows>`

### `src/Avalonia.Base/Animation/Transitions/BrushTransition.cs`
- `public class BrushTransition : Transition<IBrush?>`

### `src/Avalonia.Base/Animation/Transitions/ColorTransition.cs`
- `public class ColorTransition : Transition<Color>`

### `src/Avalonia.Base/Animation/Transitions/CornerRadiusTransition.cs`
- `public class CornerRadiusTransition : Transition<CornerRadius>`

### `src/Avalonia.Base/Animation/Transitions/DoubleTransition.cs`
- `public class DoubleTransition : Transition<double>`

### `src/Avalonia.Base/Animation/Transitions/FloatTransition.cs`
- `public class FloatTransition : Transition<float>`

### `src/Avalonia.Base/Animation/Transitions/IntegerTransition.cs`
- `public class IntegerTransition : Transition<int>`

### `src/Avalonia.Base/Animation/Transitions/PointTransition.cs`
- `public class PointTransition : Transition<Point>`

### `src/Avalonia.Base/Animation/Transitions/RelativePointTransition.cs`
- `public class RelativePointTransition : Transition<RelativePoint>`

### `src/Avalonia.Base/Animation/Transitions/Rotate3DTransition.cs`
- Namespace: `Avalonia.Animation`
- `public class Rotate3DTransition: PageSlide`
- `public Rotate3DTransition(TimeSpan duration, SlideAxis orientation = SlideAxis.Horizontal, double? depth = null) : base(duration, orientation) {`
- `public double? Depth { get; set; }`
- `public Rotate3DTransition() { }`
- `public override async Task Start(Visual? @from, Visual? to, bool forward, CancellationToken cancellationToken) {`

### `src/Avalonia.Base/Animation/Transitions/SizeTransition.cs`
- `public class SizeTransition : Transition<Size>`

### `src/Avalonia.Base/Animation/Transitions/ThicknessTransition.cs`
- `public class ThicknessTransition : Transition<Thickness>`

### `src/Avalonia.Base/Animation/Transitions/TransformOperationsTransition.cs`
- `public class TransformOperationsTransition : Transition<ITransform>`

### `src/Avalonia.Base/Animation/Transitions/VectorTransition.cs`
- `public class VectorTransition : Transition<Vector>`

### `src/Avalonia.Base/AttachedProperty.cs`
- `public sealed class AttachedProperty<TValue> : StyledProperty<TValue>`
- `public new AttachedProperty<TValue> AddOwner<TOwner>(StyledPropertyMetadata<TValue>? metadata = null) where TOwner : AvaloniaObject {`

### `src/Avalonia.Base/AvaloniaInternalException.cs`
- `public class AvaloniaInternalException : Exception`
- `public AvaloniaInternalException(string message) : base(message) {`

### `src/Avalonia.Base/AvaloniaLocator.cs`
- `public class AvaloniaLocator : IAvaloniaDependencyResolver`
- `public static IAvaloniaDependencyResolver Current { get; set; }`
- `public static AvaloniaLocator CurrentMutable { get; set; }`
- `public AvaloniaLocator() {`
- `public AvaloniaLocator(IAvaloniaDependencyResolver parentScope) {`
- `public object? GetService(Type t) {`
- `public class RegistrationHelper<TService>`
- `public RegistrationHelper(AvaloniaLocator locator) {`
- `public AvaloniaLocator ToConstant<TImpl>(TImpl constant) where TImpl : TService {`
- `public AvaloniaLocator ToFunc<TImlp>(Func<TImlp> func) where TImlp : TService {`
- `public AvaloniaLocator ToLazy<TImlp>(Func<TImlp> func) where TImlp : TService {`
- `public AvaloniaLocator ToSingleton<TImpl>() where TImpl : class, TService, new() {`
- `public AvaloniaLocator ToTransient<TImpl>() where TImpl : class, TService, new() => ToFunc(() => new TImpl());`
- `public RegistrationHelper<T> Bind<T>() => new RegistrationHelper<T>(this);`
- `public AvaloniaLocator BindToSelf<T>(T constant) => Bind<T>().ToConstant(constant);`
- `public AvaloniaLocator BindToSelfSingleton<T>() where T : class, new() => Bind<T>().ToSingleton<T>();`
- `public static IDisposable EnterScope() {`
- `public interface IAvaloniaDependencyResolver`
- `public static class LocatorExtensions`
- `public static T? GetService<T>(this IAvaloniaDependencyResolver resolver) {`
- `public static object GetRequiredService(this IAvaloniaDependencyResolver resolver, Type t) {`
- `public static T GetRequiredService<T>(this IAvaloniaDependencyResolver resolver) {`

### `src/Avalonia.Base/AvaloniaObject.cs`
- `public class AvaloniaObject : IAvaloniaObjectDebug, INotifyPropertyChanged`
- `public AvaloniaObject() {`
- `public event EventHandler<AvaloniaPropertyChangedEventArgs>? PropertyChanged {`
- `public object? this[AvaloniaProperty property] {`
- `public IBinding this[IndexerDescriptor binding] {`
- `public bool CheckAccess() => Dispatcher.UIThread.CheckAccess();`
- `public void VerifyAccess() => Dispatcher.UIThread.VerifyAccess();`
- `public void ClearValue(AvaloniaProperty property) {`
- `public void ClearValue<T>(AvaloniaProperty<T> property) {`
- `public void ClearValue<T>(StyledProperty<T> property) {`
- `public void ClearValue<T>(DirectPropertyBase<T> property) {`
- `public sealed override bool Equals(object? obj) => base.Equals(obj);`
- `public sealed override int GetHashCode() => base.GetHashCode();`
- `public object? GetValue(AvaloniaProperty property) {`
- `public T GetValue<T>(StyledProperty<T> property) {`
- `public T GetValue<T>(DirectPropertyBase<T> property) {`
- `public Optional<T> GetBaseValue<T>(StyledProperty<T> property) {`
- `public bool IsAnimating(AvaloniaProperty property) {`
- `public bool IsSet(AvaloniaProperty property) {`
- `public IDisposable? SetValue( AvaloniaProperty property, object? value, BindingPriority priority = BindingPriority.LocalValue) {`
- `public IDisposable? SetValue<T>( StyledProperty<T> property, T value, BindingPriority priority = BindingPriority.LocalValue) {`
- `public void SetValue<T>(DirectPropertyBase<T> property, T value) {`
- `public void SetCurrentValue(AvaloniaProperty property, object? value) =>`
- `public void SetCurrentValue<T>(StyledProperty<T> property, T value) {`
- `public BindingExpressionBase Bind(AvaloniaProperty property, IBinding binding) {`
- `public IDisposable Bind( AvaloniaProperty property, IObservable<object?> source, BindingPriority priority = BindingPriority.LocalValue) => property.RouteBind(this, source, priority);`
- `public IDisposable Bind<T>( StyledProperty<T> property, IObservable<object?> source, BindingPriority priority = BindingPriority.LocalValue) {`
- `public IDisposable Bind<T>( StyledProperty<T> property, IObservable<T> source, BindingPriority priority = BindingPriority.LocalValue) {`
- `public IDisposable Bind<T>( StyledProperty<T> property, IObservable<BindingValue<T>> source, BindingPriority priority = BindingPriority.LocalValue) {`
- `public IDisposable Bind<T>( DirectPropertyBase<T> property, IObservable<object?> source) {`
- `public IDisposable Bind<T>( DirectPropertyBase<T> property, IObservable<T> source) {`
- `public IDisposable Bind<T>( DirectPropertyBase<T> property, IObservable<BindingValue<T>> source) {`
- `public void CoerceValue(AvaloniaProperty property) => _values.CoerceValue(property);`

### `src/Avalonia.Base/AvaloniaObjectExtensions.cs`
- `public static class AvaloniaObjectExtensions`
- `public static IBinding ToBinding<T>(this IObservable<T> source) {`
- `public static IObservable<object?> GetObservable(this AvaloniaObject o, AvaloniaProperty property) {`
- `public static IObservable<T> GetObservable<T>(this AvaloniaObject o, AvaloniaProperty<T> property) {`
- `public static IObservable<TResult> GetObservable<TSource, TResult>(this AvaloniaObject o, AvaloniaProperty<TSource> property, Func<TSource, TResult> converter) {`
- `public static IObservable<TResult> GetObservable<TResult>(this AvaloniaObject o, AvaloniaProperty property, Func<object?, TResult> converter) {`
- `public static IObservable<BindingValue<object?>> GetBindingObservable( this AvaloniaObject o, AvaloniaProperty property) {`
- `public static IObservable<BindingValue<TResult>> GetBindingObservable<TResult>(this AvaloniaObject o, AvaloniaProperty property, Func<object?, TResult> converter) {`
- `public static IObservable<BindingValue<T>> GetBindingObservable<T>( this AvaloniaObject o, AvaloniaProperty<T> property) {`
- `public static IObservable<BindingValue<TResult>> GetBindingObservable<TSource, TResult>( this AvaloniaObject o, AvaloniaProperty<TSource> property, Func<TSource, TResult> converter) {`
- `public static IObservable<AvaloniaPropertyChangedEventArgs> GetPropertyChangedObservable( this AvaloniaObject o, AvaloniaProperty property) {`
- `public static IDisposable Bind<T>( this AvaloniaObject target, AvaloniaProperty<T> property, IObservable<BindingValue<T>> source, BindingPriority priority = BindingPriority.LocalValue) {`
- `public static IDisposable Bind<T>( this AvaloniaObject target, AvaloniaProperty<T> property, IObservable<T> source, BindingPriority priority = BindingPriority.LocalValue) {`
- `public static IDisposable Bind( this AvaloniaObject target, AvaloniaProperty property, IBinding binding, object? anchor = null) {`
- `public static T GetValue<T>(this AvaloniaObject target, AvaloniaProperty<T> property) {`
- `public static object? GetBaseValue( this AvaloniaObject target, AvaloniaProperty property) {`
- `public static Optional<T> GetBaseValue<T>( this AvaloniaObject target, AvaloniaProperty<T> property) {`
- `public static IDisposable AddClassHandler<TTarget>( this IObservable<AvaloniaPropertyChangedEventArgs> observable, Action<TTarget, AvaloniaPropertyChangedEventArgs> action) where TTarget : AvaloniaObject {`
- `public static IDisposable AddClassHandler<TTarget, TValue>( this IObservable<AvaloniaPropertyChangedEventArgs<TValue>> observable, Action<TTarget, AvaloniaPropertyChangedEventArgs<TValue>> action) where TTarget : AvaloniaObject {`

### `src/Avalonia.Base/AvaloniaProperty.cs`
- `public abstract class AvaloniaProperty : IEquatable<AvaloniaProperty>, IPropertyInfo`
- `public static readonly object UnsetValue = new UnsetValueType();`
- `public string Name { get; }`
- `public Type PropertyType { get; }`
- `public Type OwnerType { get; }`
- `public bool Inherits { get; private protected set; }`
- `public bool IsAttached { get; private protected set; }`
- `public bool IsDirect { get; private protected set; }`
- `public bool IsReadOnly { get; private protected set; }`
- `public IObservable<AvaloniaPropertyChangedEventArgs> Changed => GetChanged();`
- `public static IndexerDescriptor operator !(AvaloniaProperty property) {`
- `public static IndexerDescriptor operator ~(AvaloniaProperty property) {`
- `public static bool operator ==(AvaloniaProperty? a, AvaloniaProperty? b) {`
- `public static bool operator !=(AvaloniaProperty? a, AvaloniaProperty? b) {`
- `public void Unregister(Type type) {`
- `public static StyledProperty<TValue> Register<TOwner, TValue>( string name, TValue defaultValue = default!, bool inherits = false, BindingMode defaultBindingMode = BindingMode.OneWay, Func<TValue, bool>? validate = null, Func<AvaloniaObject, TValue, TValue>? coerce = null, bool enableDataValidation = false) where TOwner : AvaloniaObject {`
- `public static AttachedProperty<TValue> RegisterAttached<TOwner, THost, TValue>( string name, TValue defaultValue = default!, bool inherits = false, BindingMode defaultBindingMode = BindingMode.OneWay, Func<TValue, bool>? validate = null, Func<AvaloniaObject, TValue, TValue>? coerce = null) where THost : AvaloniaObject {`
- `public static AttachedProperty<TValue> RegisterAttached<THost, TValue>( string name, Type ownerType, TValue defaultValue = default!, bool inherits = false, BindingMode defaultBindingMode = BindingMode.OneWay, Func<TValue, bool>? validate = null, Func<AvaloniaObject, TValue, TValue>? coerce = null) where THost : AvaloniaObject {`
- `public static DirectProperty<TOwner, TValue> RegisterDirect<TOwner, TValue>( string name, Func<TOwner, TValue> getter, Action<TOwner, TValue>? setter = null, TValue unsetValue = default!, BindingMode defaultBindingMode = BindingMode.OneWay, bool enableDataValidation = false) where TOwner : AvaloniaObject {`
- `public IndexerDescriptor Bind() {`
- `public override bool Equals(object? obj) {`
- `public bool Equals(AvaloniaProperty? other) {`
- `public override int GetHashCode() {`
- `public AvaloniaPropertyMetadata GetMetadata<T>() where T : AvaloniaObject => GetMetadata(typeof(T));`
- `public AvaloniaPropertyMetadata GetMetadata(Type type) {`
- `public AvaloniaPropertyMetadata GetMetadata(AvaloniaObject owner) {`
- `public bool IsValidValue(object? value) {`
- `public override string ToString() {`
- `public sealed class UnsetValueType`
- `public override string ToString() => "(unset)";`

### `src/Avalonia.Base/AvaloniaPropertyChangedEventArgs.cs`
- `public abstract class AvaloniaPropertyChangedEventArgs : EventArgs`
- `public AvaloniaPropertyChangedEventArgs( AvaloniaObject sender, BindingPriority priority) {`
- `public AvaloniaObject Sender { get; private set; }`
- `public AvaloniaProperty Property => GetProperty();`
- `public object? OldValue => GetOldValue();`
- `public object? NewValue => GetNewValue();`
- `public BindingPriority Priority { get; private set; }`

### `src/Avalonia.Base/AvaloniaPropertyChangedEventArgs`1.cs`
- `public class AvaloniaPropertyChangedEventArgs<T> : AvaloniaPropertyChangedEventArgs`
- `public AvaloniaPropertyChangedEventArgs( AvaloniaObject sender, AvaloniaProperty<T> property, Optional<T> oldValue, BindingValue<T> newValue, BindingPriority priority) : this(sender, property, oldValue, newValue, priority, true) {`
- `public new AvaloniaProperty<T> Property { get; }`
- `public new Optional<T> OldValue { get; private set; }`
- `public new BindingValue<T> NewValue { get; private set; }`

### `src/Avalonia.Base/AvaloniaPropertyChangedExtensions.cs`
- `public static class AvaloniaPropertyChangedExtensions`
- `public static T GetOldValue<T>(this AvaloniaPropertyChangedEventArgs e) {`
- `public static T GetNewValue<T>(this AvaloniaPropertyChangedEventArgs e) {`
- `public static (T oldValue, T newValue) GetOldAndNewValue<T>(this AvaloniaPropertyChangedEventArgs e) {`

### `src/Avalonia.Base/AvaloniaPropertyMetadata.cs`
- `public abstract class AvaloniaPropertyMetadata`
- `public AvaloniaPropertyMetadata( BindingMode defaultBindingMode = BindingMode.Default, bool? enableDataValidation = null) {`
- `public BindingMode DefaultBindingMode {`
- `public bool? EnableDataValidation { get; private set; }`
- `public bool IsReadOnly { get; private set; }`
- `public virtual void Merge( AvaloniaPropertyMetadata baseMetadata, AvaloniaProperty property) {`
- `public void Freeze() => IsReadOnly = true;`
- `public abstract AvaloniaPropertyMetadata GenerateTypeSafeMetadata();`

### `src/Avalonia.Base/AvaloniaPropertyRegistry.cs`
- `public class AvaloniaPropertyRegistry`
- `public static AvaloniaPropertyRegistry Instance { get; }`
- `public bool UnregisterByModule(IEnumerable<Type> types) {`
- `public IReadOnlyList<AvaloniaProperty> GetRegistered(Type type) {`
- `public IReadOnlyList<AvaloniaProperty> GetRegisteredAttached(Type type) {`
- `public IReadOnlyList<AvaloniaProperty> GetRegisteredDirect(Type type) {`
- `public IReadOnlyList<AvaloniaProperty> GetRegisteredInherited(Type type) {`
- `public IReadOnlyList<AvaloniaProperty> GetRegistered(AvaloniaObject o) {`
- `public DirectPropertyBase<T> GetRegisteredDirect<T>( AvaloniaObject o, DirectPropertyBase<T> property) {`
- `public AvaloniaProperty? FindRegistered(Type type, string name) {`
- `public AvaloniaProperty? FindRegistered(AvaloniaObject o, string name) {`
- `public DirectPropertyBase<T>? FindRegisteredDirect<T>( AvaloniaObject o, DirectPropertyBase<T> property) {`
- `public bool IsRegistered(Type type, AvaloniaProperty property) {`
- `public bool IsRegistered(object o, AvaloniaProperty property) {`
- `public void Register(Type type, AvaloniaProperty property) {`
- `public void RegisterAttached(Type type, AvaloniaProperty property) {`

### `src/Avalonia.Base/AvaloniaProperty`1.cs`
- `public abstract class AvaloniaProperty<TValue> : AvaloniaProperty`
- `public new IObservable<AvaloniaPropertyChangedEventArgs<TValue>> Changed => _changed;`

### `src/Avalonia.Base/Collections/AvaloniaDictionary.cs`
- `public class AvaloniaDictionary<TKey, TValue> : IAvaloniaDictionary<TKey, TValue> where TKey : notnull`
- `public AvaloniaDictionary() {`
- `public AvaloniaDictionary(int capacity) {`
- `public AvaloniaDictionary(IDictionary<TKey, TValue> dictionary, IEqualityComparer<TKey>? comparer = null) {`
- `public event NotifyCollectionChangedEventHandler? CollectionChanged;`
- `public event PropertyChangedEventHandler? PropertyChanged;`
- `public int Count => _inner.Count;`
- `public bool IsReadOnly => false;`
- `public ICollection<TKey> Keys => _inner.Keys;`
- `public ICollection<TValue> Values => _inner.Values;`
- `public TValue this[TKey key] {`
- `public void Add(TKey key, TValue value) {`
- `public void Clear() {`
- `public bool ContainsKey(TKey key) => _inner.ContainsKey(key);`
- `public void CopyTo(KeyValuePair<TKey, TValue>[] array, int arrayIndex) {`
- `public IEnumerator<KeyValuePair<TKey, TValue>> GetEnumerator() => _inner.GetEnumerator();`
- `public bool Remove(TKey key) {`
- `public bool TryGetValue(TKey key, [MaybeNullWhen(false)] out TValue value) => _inner.TryGetValue(key, out value);`

### `src/Avalonia.Base/Collections/AvaloniaDictionaryExtensions.cs`
- `public static class AvaloniaDictionaryExtensions`
- `public static IDisposable ForEachItem<TKey, TValue>( this IAvaloniaReadOnlyDictionary<TKey, TValue> collection, Action<TKey, TValue> added, Action<TKey, TValue> removed, Action reset, bool weakSubscription = false) where TKey : notnull {`

### `src/Avalonia.Base/Collections/AvaloniaList.cs`
- `public enum ResetBehavior`
- `public class AvaloniaList<T> : IAvaloniaList<T>, IList, INotifyCollectionChangedDebug`
- `public AvaloniaList() {`
- `public AvaloniaList(int capacity) {`
- `public AvaloniaList(IEnumerable<T> items) {`
- `public AvaloniaList(params T[] items) {`
- `public event NotifyCollectionChangedEventHandler? CollectionChanged {`
- `public event PropertyChangedEventHandler? PropertyChanged;`
- `public int Count => _inner.Count;`
- `public ResetBehavior ResetBehavior { get; set; }`
- `public Action<T>? Validate {`
- `public T this[int index] {`
- `public int Capacity {`
- `public virtual void Add(T item) {`
- `public virtual void AddRange(IEnumerable<T> items) => InsertRange(_inner.Count, items);`
- `public virtual void Clear() {`
- `public bool Contains(T item) {`
- `public void CopyTo(T[] array, int arrayIndex) {`
- `public Enumerator GetEnumerator() {`
- `public IEnumerable<T> GetRange(int index, int count) {`
- `public int IndexOf(T item) {`
- `public virtual void Insert(int index, T item) {`
- `public virtual void InsertRange(int index, IEnumerable<T> items) {`
- `public void Move(int oldIndex, int newIndex) {`
- `public void MoveRange(int oldIndex, int count, int newIndex) {`
- `public void EnsureCapacity(int capacity) {`
- `public virtual bool Remove(T item) {`
- `public virtual void RemoveAll(IEnumerable<T> items) {`
- `public virtual void RemoveAt(int index) {`
- `public virtual void RemoveRange(int index, int count) {`
- `public struct Enumerator : IEnumerator<T>`
- `public Enumerator(List<T> inner) {`
- `public bool MoveNext() {`
- `public T Current => _innerEnumerator.Current;`
- `public void Dispose() {`

### `src/Avalonia.Base/Collections/AvaloniaListConverter.cs`
- `public class AvaloniaListConverter<[DynamicallyAccessedMembers(DynamicallyAccessedMemberTypes.All)] T> : TypeConverter`
- `public override bool CanConvertFrom(ITypeDescriptorContext? context, Type sourceType) {`
- `public override object? ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object? value) {`

### `src/Avalonia.Base/Collections/AvaloniaListExtensions.cs`
- `public static class AvaloniaListExtensions`
- `public static IDisposable ForEachItem<T>( this IAvaloniaReadOnlyList<T> collection, Action<T> added, Action<T> removed, Action reset, bool weakSubscription = false) {`
- `public static IDisposable ForEachItem<T>( this IAvaloniaReadOnlyList<T> collection, Action<int, T> added, Action<int, T> removed, Action reset, bool weakSubscription = false) {`
- `public static IDisposable TrackItemPropertyChanged<T>( this IAvaloniaReadOnlyList<T> collection, Action<Tuple<object?, PropertyChangedEventArgs>> callback) {`

### `src/Avalonia.Base/Collections/IAvaloniaDictionary.cs`
- `public interface IAvaloniaDictionary<TKey, TValue>`

### `src/Avalonia.Base/Collections/IAvaloniaList.cs`
- `public interface IAvaloniaList<T> : IList<T>, IAvaloniaReadOnlyList<T>`

### `src/Avalonia.Base/Collections/IAvaloniaReadOnlyDictionary.cs`
- `public interface IAvaloniaReadOnlyDictionary<TKey, TValue>`

### `src/Avalonia.Base/Collections/IAvaloniaReadOnlyList.cs`
- `public interface IAvaloniaReadOnlyList<out T> : IReadOnlyList<T>, INotifyCollectionChanged, INotifyPropertyChanged`

### `src/Avalonia.Base/Collections/NotifyCollectionChangedExtensions.cs`
- `public static class NotifyCollectionChangedExtensions`
- `public static IObservable<NotifyCollectionChangedEventArgs> GetWeakCollectionChangedObservable( this INotifyCollectionChanged collection) {`
- `public static IDisposable WeakSubscribe( this INotifyCollectionChanged collection, NotifyCollectionChangedEventHandler handler) {`
- `public static IDisposable WeakSubscribe( this INotifyCollectionChanged collection, Action<NotifyCollectionChangedEventArgs> handler) {`

### `src/Avalonia.Base/CombinedGeometry.cs`
- `public enum GeometryCombineMode`
- `public class CombinedGeometry : Geometry`
- `public static readonly StyledProperty<Geometry?> Geometry1Property = AvaloniaProperty.Register<CombinedGeometry, Geometry?>(nameof(Geometry1));`
- `public static readonly StyledProperty<Geometry?> Geometry2Property = AvaloniaProperty.Register<CombinedGeometry, Geometry?>(nameof(Geometry2));`
- `public static readonly StyledProperty<GeometryCombineMode> GeometryCombineModeProperty = AvaloniaProperty.Register<CombinedGeometry, GeometryCombineMode>(nameof(GeometryCombineMode));`
- `public CombinedGeometry() {`
- `public CombinedGeometry(Geometry geometry1, Geometry geometry2) {`
- `public CombinedGeometry(GeometryCombineMode combineMode, Geometry? geometry1, Geometry? geometry2) {`
- `public CombinedGeometry( GeometryCombineMode combineMode, Geometry? geometry1, Geometry? geometry2, Transform? transform) {`
- `public Geometry? Geometry1 {`
- `public Geometry? Geometry2 {`
- `public GeometryCombineMode GeometryCombineMode {`
- `public override Geometry Clone() {`

### `src/Avalonia.Base/Controls/Classes.cs`
- `public class Classes : AvaloniaList<string>, IPseudoClasses`
- `public Classes() {`
- `public Classes(IEnumerable<string> items) : base(items) {`
- `public Classes(params string[] items) : base(items) {`
- `public static Classes Parse(string s) => new Classes(s.Split(' '));`
- `public override void Add(string name) {`
- `public override void AddRange(IEnumerable<string> names) {`
- `public override void Clear() {`
- `public override void Insert(int index, string name) {`
- `public override void InsertRange(int index, IEnumerable<string> names) {`
- `public override bool Remove(string name) {`
- `public override void RemoveAll(IEnumerable<string> names) {`
- `public override void RemoveAt(int index) {`
- `public override void RemoveRange(int index, int count) {`
- `public void Replace(IList<string> source) {`
- `public void Set(string name, bool value) {`

### `src/Avalonia.Base/Controls/IDeferredContent.cs`
- Namespace: `Avalonia.Controls`
- `public interface IDeferredContent`

### `src/Avalonia.Base/Controls/INameScope.cs`
- `public interface INameScope`

### `src/Avalonia.Base/Controls/IPseudoClasses.cs`
- `public interface IPseudoClasses`

### `src/Avalonia.Base/Controls/IResourceDictionary.cs`
- `public interface IResourceDictionary : IResourceProvider, IDictionary<object, object?>`

### `src/Avalonia.Base/Controls/IResourceHost.cs`
- `public interface IResourceHost : IResourceNode`

### `src/Avalonia.Base/Controls/IResourceNode.cs`
- `public interface IResourceNode`

### `src/Avalonia.Base/Controls/IResourceProvider.cs`
- `public interface IResourceProvider : IResourceNode`

### `src/Avalonia.Base/Controls/ISetInheritanceParent.cs`
- `public interface ISetInheritanceParent`

### `src/Avalonia.Base/Controls/ISetLogicalParent.cs`
- `public interface ISetLogicalParent`

### `src/Avalonia.Base/Controls/IThemeVariantProvider.cs`
- Namespace: `Avalonia.Controls`
- `public interface IThemeVariantProvider : IResourceProvider`

### `src/Avalonia.Base/Controls/Metadata/PseudoClassesAttribute.cs`
- `public sealed class PseudoClassesAttribute : Attribute`
- `public PseudoClassesAttribute(params string[] pseudoClasses) {`
- `public IReadOnlyList<string> PseudoClasses { get; }`

### `src/Avalonia.Base/Controls/Metadata/TemplatePartAttribute.cs`
- `public sealed class TemplatePartAttribute : Attribute`
- `public TemplatePartAttribute() {`
- `public TemplatePartAttribute(string name, Type type) {`
- `public string Name { get; set; }`
- `public Type Type { get; set; }`
- `public bool IsRequired { get; set; }`

### `src/Avalonia.Base/Controls/NameScope.cs`
- `public class NameScope : INameScope`
- `public static readonly AttachedProperty<INameScope> NameScopeProperty = AvaloniaProperty.RegisterAttached<NameScope, StyledElement, INameScope>("NameScope");`
- `public bool IsCompleted { get; private set; }`
- `public static INameScope GetNameScope(StyledElement styled) {`
- `public static void SetNameScope(StyledElement styled, INameScope value) {`
- `public void Register(string name, object element) {`
- `public SynchronousCompletionAsyncResult<object?> FindAsync(string name) {`
- `public object? Find(string name) {`
- `public void Complete() {`

### `src/Avalonia.Base/Controls/NameScopeExtensions.cs`
- `public static class NameScopeExtensions`
- `public static T? Find<T>(this INameScope nameScope, string name) where T : class {`
- `public static T? Find<T>(this ILogical anchor, string name) where T : class {`
- `public static T Get<T>(this INameScope nameScope, string name) where T : class {`
- `public static T Get<T>(this ILogical anchor, string name) where T : class {`
- `public static INameScope? FindNameScope(this ILogical control) {`

### `src/Avalonia.Base/Controls/NameScopeLocator.cs`
- `public class NameScopeLocator`
- `public static IObservable<object?> Track(INameScope scope, string name) {`

### `src/Avalonia.Base/Controls/PseudoClassesExtensions.cs`
- `public static class PseudolassesExtensions`
- `public static void Set(this IPseudoClasses classes, string name, bool value) {`

### `src/Avalonia.Base/Controls/ResourceDictionary.cs`
- `public class ResourceDictionary : ResourceProvider, IResourceDictionary, IThemeVariantProvider`
- `public ResourceDictionary() { }`
- `public ResourceDictionary(IResourceHost owner) : base(owner) { }`
- `public int Count => _inner?.Count ?? 0;`
- `public object? this[object key] {`
- `public ICollection<object> Keys => (ICollection<object>?)_inner?.Keys ?? Array.Empty<object>();`
- `public ICollection<object?> Values => (ICollection<object?>?)_inner?.Values ?? Array.Empty<object?>();`
- `public IList<IResourceProvider> MergedDictionaries {`
- `public IDictionary<ThemeVariant, IThemeVariantProvider> ThemeDictionaries {`
- `public sealed override bool HasResources {`
- `public void Add(object key, object? value) {`
- `public void AddDeferred(object key, Func<IServiceProvider?, object?> factory) => Add(key, new DeferredItem(factory));`
- `public void AddDeferred(object key, IDeferredContent deferredContent) => Add(key, deferredContent);`
- `public void AddNotSharedDeferred(object key, IDeferredContent deferredContent) => Add(key, new NotSharedDeferredItem(deferredContent));`
- `public void SetItems(IEnumerable<KeyValuePair<object, object?>> values) {`
- `public void Clear() {`
- `public bool ContainsKey(object key) => _inner?.ContainsKey(key) ?? false;`
- `public bool Remove(object key) {`
- `public sealed override bool TryGetResource(object key, ThemeVariant? theme, out object? value) {`
- `public bool TryGetValue(object key, out object? value) {`
- `public void EnsureCapacity(int capacity) {`
- `public IEnumerator<KeyValuePair<object, object?>> GetEnumerator() {`

### `src/Avalonia.Base/Controls/ResourceNodeExtensions.cs`
- `public static class ResourceNodeExtensions`
- `public static object? FindResource(this IResourceHost control, object key) {`
- `public static bool TryFindResource(this IResourceHost control, object key, out object? value) {`
- `public static object? FindResource(this IResourceHost control, ThemeVariant? theme, object key) {`
- `public static bool TryFindResource(this IResourceHost control, object key, ThemeVariant? theme, out object? value) {`
- `public static bool TryGetResource(this IResourceHost control, object key, out object? value) {`
- `public static IObservable<object?> GetResourceObservable( this IResourceHost control, object key, Func<object?, object?>? converter = null) {`
- `public static IObservable<object?> GetResourceObservable( this IResourceProvider resourceProvider, object key, Func<object?, object?>? converter = null) {`
- `public static IObservable<object?> GetResourceObservable( this IResourceProvider resourceProvider, object key, ThemeVariant? defaultThemeVariant, Func<object?, object?>? converter = null) {`

### `src/Avalonia.Base/Controls/ResourceProvider.cs`
- Namespace: `Avalonia.Controls`
- `public abstract class ResourceProvider : AvaloniaObject, IResourceProvider`
- `public ResourceProvider() {`
- `public ResourceProvider(IResourceHost owner) {`
- `public abstract bool HasResources { get; }`
- `public abstract bool TryGetResource(object key, ThemeVariant? theme, out object? value);`
- `public IResourceHost? Owner {`
- `public event EventHandler? OwnerChanged;`

### `src/Avalonia.Base/Controls/ResourcesChangedEventArgs.cs`
- `public class ResourcesChangedEventArgs : EventArgs`
- `public static new readonly ResourcesChangedEventArgs Empty = new ResourcesChangedEventArgs();`

### `src/Avalonia.Base/Controls/Templates/ITemplateResult.cs`
- `public interface ITemplateResult`
- `public object? Result { get; }`
- `public INameScope NameScope { get; }`

### `src/Avalonia.Base/Controls/Templates/TemplateResult.cs`
- `public class TemplateResult<T> : ITemplateResult`
- `public T Result { get; }`
- `public INameScope NameScope { get; }`
- `public TemplateResult(T result, INameScope nameScope) {`
- `public void Deconstruct(out T result, out INameScope scope) {`

### `src/Avalonia.Base/Data/AssignBindingAttribute.cs`
- `public sealed class AssignBindingAttribute : Attribute`

### `src/Avalonia.Base/Data/BindingChainException.cs`
- `public class BindingChainException : Exception`
- `public BindingChainException() {`
- `public BindingChainException(string message) {`
- `public BindingChainException(string message, string expression, string errorPoint) {`
- `public string? Expression { get; protected set; }`
- `public string? ExpressionErrorPoint { get; protected set; }`
- `public override string Message {`

### `src/Avalonia.Base/Data/BindingExpressionBase.cs`
- Namespace: `Avalonia.Data`
- `public abstract class BindingExpressionBase : IDisposable, ISetterInstance`
- `public virtual void Dispose() {`
- `public virtual void UpdateSource() { }`
- `public virtual void UpdateTarget() { }`

### `src/Avalonia.Base/Data/BindingMode.cs`
- `public enum BindingMode`

### `src/Avalonia.Base/Data/BindingNotification.cs`
- `public enum BindingErrorType`
- `public class BindingNotification`
- `public static readonly BindingNotification Null = new BindingNotification(null);`
- `public static readonly BindingNotification UnsetValue = new BindingNotification(AvaloniaProperty.UnsetValue);`
- `public BindingNotification(object? value) {`
- `public BindingNotification(Exception error, BindingErrorType errorType) {`
- `public BindingNotification(Exception error, BindingErrorType errorType, object? fallbackValue) : this(error, errorType) {`
- `public object? Value => _value;`
- `public bool HasValue => _value != AvaloniaProperty.UnsetValue;`
- `public Exception? Error { get; set; }`
- `public BindingErrorType ErrorType { get; set; }`
- `public static bool operator ==(BindingNotification? a, BindingNotification? b) {`
- `public static bool operator !=(BindingNotification? a, BindingNotification? b) {`
- `public static object? ExtractValue(object? o) {`
- `public static object? UpdateValue(object? o, object value) {`
- `public static object? ExtractError(object? o) {`
- `public override bool Equals(object? obj) {`
- `public bool Equals(BindingNotification? other) {`
- `public override int GetHashCode() {`
- `public void AddError(Exception e, BindingErrorType type) {`
- `public void ClearValue() {`
- `public void SetValue(object? value) {`
- `public override string ToString() {`

### `src/Avalonia.Base/Data/BindingOperations.cs`
- `public static class BindingOperations`
- `public static readonly object DoNothing = new DoNothingType();`
- `public static IDisposable Apply( AvaloniaObject target, AvaloniaProperty property, InstancedBinding binding) {`
- `public static IDisposable Apply( AvaloniaObject target, AvaloniaProperty property, InstancedBinding binding, object? anchor) {`
- `public static BindingExpressionBase? GetBindingExpressionBase(AvaloniaObject target, AvaloniaProperty property) {`
- `public sealed class DoNothingType`
- `public override string ToString() => "(do nothing)";`

### `src/Avalonia.Base/Data/BindingPriority.cs`
- `public enum BindingPriority`

### `src/Avalonia.Base/Data/BindingValue.cs`
- `public enum BindingValueType`
- `public readonly record struct BindingValue<T>`
- `public BindingValue(T value) {`
- `public bool HasError => Type.HasAllFlags(BindingValueType.HasError);`
- `public bool HasValue => Type.HasAllFlags(BindingValueType.HasValue);`
- `public BindingValueType Type { get; }`
- `public T Value => HasValue ? _value! : throw new InvalidOperationException("BindingValue has no value.");`
- `public Exception? Error { get; }`
- `public Optional<T> ToOptional() => HasValue ? new Optional<T>(_value) : default;`
- `public override string ToString() => HasError ? $"Error: {Error!.Message}" : _value?.ToString() ?? "(null)";`
- `public object? ToUntyped() {`
- `public BindingValue<T> WithValue(T value) {`
- `public T? GetValueOrDefault() => HasValue ? _value : default;`
- `public T? GetValueOrDefault(T defaultValue) => HasValue ? _value : defaultValue;`
- `public TResult? GetValueOrDefault<TResult>() {`
- `public TResult? GetValueOrDefault<TResult>(TResult defaultValue) {`
- `public static BindingValue<T> FromUntyped(object? value) {`
- `public static BindingValue<T> FromUntyped(object? value, Type targetType) {`
- `public static implicit operator BindingValue<T>(T value) => new BindingValue<T>(value);`
- `public static implicit operator BindingValue<T>(Optional<T> optional) {`
- `public static BindingValue<T> Unset => new BindingValue<T>(BindingValueType.UnsetValue, default, null);`
- `public static BindingValue<T> DoNothing => new BindingValue<T>(BindingValueType.DoNothing, default, null);`
- `public static BindingValue<T> BindingError(Exception e) {`
- `public static BindingValue<T> BindingError(Exception e, T fallbackValue) {`
- `public static BindingValue<T> BindingError(Exception e, Optional<T> fallbackValue) {`
- `public static BindingValue<T> DataValidationError(Exception e) {`
- `public static BindingValue<T> DataValidationError(Exception e, T fallbackValue) {`
- `public static BindingValue<T> DataValidationError(Exception e, Optional<T> fallbackValue) {`

### `src/Avalonia.Base/Data/Converters/BoolConverters.cs`
- `public static class BoolConverters`
- `public static readonly IMultiValueConverter And = new FuncMultiValueConverter<bool, bool>(x => x.All(y => y));`
- `public static readonly IMultiValueConverter Or = new FuncMultiValueConverter<bool, bool>(x => x.Any(y => y));`
- `public static readonly IValueConverter Not = new NotConverter();`

### `src/Avalonia.Base/Data/Converters/DefaultValueConverter.cs`
- `public class DefaultValueConverter : IValueConverter`
- `public static readonly DefaultValueConverter Instance = new DefaultValueConverter();`
- `public object? Convert(object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public object? ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture) {`

### `src/Avalonia.Base/Data/Converters/FuncMultiValueConverter.cs`
- `public class FuncMultiValueConverter<TIn, TOut> : IMultiValueConverter`
- `public FuncMultiValueConverter(Func<IEnumerable<TIn?>, TOut> convert) {`
- `public object? Convert(IList<object?> values, Type targetType, object? parameter, CultureInfo culture) {`

### `src/Avalonia.Base/Data/Converters/FuncValueConverter.cs`
- `public class FuncValueConverter<TIn, TOut> : IValueConverter`
- `public FuncValueConverter(Func<TIn?, TOut> convert) {`
- `public FuncValueConverter(Func<TIn?, TOut> convert, Func<TOut?, TIn>? convertBack) {`
- `public object? Convert(object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public object? ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public class FuncValueConverter<TIn, TParam, TOut> : IValueConverter`
- `public FuncValueConverter(Func<TIn?, TParam?, TOut> convert) {`
- `public FuncValueConverter(Func<TIn?, TParam?, TOut> convert, Func<TOut?, TParam?, TIn>? convertBack = null) {`
- `public object? Convert(object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public object? ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture) {`

### `src/Avalonia.Base/Data/Converters/IMultiValueConverter.cs`
- `public interface IMultiValueConverter`

### `src/Avalonia.Base/Data/Converters/IValueConverter.cs`
- `public interface IValueConverter`

### `src/Avalonia.Base/Data/Converters/ObjectConverters.cs`
- `public static class ObjectConverters`
- `public static readonly IValueConverter IsNull = new FuncValueConverter<object?, bool>(x => x is null);`
- `public static readonly IValueConverter IsNotNull = new FuncValueConverter<object?, bool>(x => x is not null);`
- `public static readonly IValueConverter Equal = new FuncValueConverter<object?, object?, bool>((a, b) => a?.Equals(b) ?? b is null);`
- `public static readonly IValueConverter NotEqual = new FuncValueConverter<object?, object?, bool>((a, b) => !a?.Equals(b) ?? b is not null);`

### `src/Avalonia.Base/Data/Converters/StringConverters.cs`
- `public static class StringConverters`
- `public static readonly IValueConverter IsNullOrEmpty = new FuncValueConverter<string?, bool>(string.IsNullOrEmpty);`
- `public static readonly IValueConverter IsNotNullOrEmpty = new FuncValueConverter<string?, bool>(x => !string.IsNullOrEmpty(x));`

### `src/Avalonia.Base/Data/Converters/StringFormatMultiValueConverter.cs`
- `public class StringFormatMultiValueConverter : IMultiValueConverter`
- `public StringFormatMultiValueConverter(string format, IMultiValueConverter? inner) {`
- `public IMultiValueConverter? Inner { get; }`
- `public string Format { get; }`
- `public object? Convert(IList<object?> values, Type targetType, object? parameter, CultureInfo culture) {`

### `src/Avalonia.Base/Data/Converters/StringFormatValueConverter.cs`
- `public class StringFormatValueConverter : IValueConverter`
- `public StringFormatValueConverter(string format, IValueConverter? inner) {`
- `public IValueConverter? Inner { get; }`
- `public string Format { get; }`
- `public object? Convert(object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public object? ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture) {`

### `src/Avalonia.Base/Data/Core/ClrPropertyInfo.cs`
- `public class ClrPropertyInfo : IPropertyInfo`
- `public ClrPropertyInfo(string name, Func<object, object?>? getter, Action<object, object?>? setter, Type propertyType) {`
- `public string Name { get; }`
- `public Type PropertyType { get; }`
- `public object? Get(object target) {`
- `public void Set(object target, object? value) {`
- `public bool CanSet => _setter != null;`
- `public bool CanGet => _getter != null;`
- `public class ReflectionClrPropertyInfo : ClrPropertyInfo`
- `public ReflectionClrPropertyInfo(PropertyInfo info) : base(info.Name, CreateGetter(info), CreateSetter(info), info.PropertyType) {`

### `src/Avalonia.Base/Data/Core/IPropertyInfo.cs`
- `public interface IPropertyInfo`

### `src/Avalonia.Base/Data/Core/Plugins/BindingPlugins.cs`
- `public static class BindingPlugins`
- `public static IList<IPropertyAccessorPlugin> PropertyAccessors => s_propertyAccessors;`
- `public static IList<IDataValidationPlugin> DataValidators => s_dataValidators;`
- `public static IList<IStreamPlugin> StreamHandlers => s_streamHandlers;`

### `src/Avalonia.Base/Data/Core/Plugins/DataAnnotationsValidationPlugin.cs`
- `public class DataAnnotationsValidationPlugin : IDataValidationPlugin`
- `public bool Match(WeakReference<object?> reference, string memberName) {`
- `public IPropertyAccessor Start(WeakReference<object?> reference, string name, IPropertyAccessor inner) {`

### `src/Avalonia.Base/Data/Core/Plugins/DataValidationBase.cs`
- `public abstract class DataValidationBase : PropertyAccessorBase, IObserver<object?>`
- `public override Type? PropertyType => _inner.PropertyType;`
- `public override object? Value => _inner.Value;`
- `public override bool SetValue(object? value, BindingPriority priority) => _inner.SetValue(value, priority);`

### `src/Avalonia.Base/Data/Core/Plugins/ExceptionValidationPlugin.cs`
- `public class ExceptionValidationPlugin : IDataValidationPlugin`
- `public bool Match(WeakReference<object?> reference, string memberName) => true;`
- `public IPropertyAccessor Start(WeakReference<object?> reference, string name, IPropertyAccessor inner) {`

### `src/Avalonia.Base/Data/Core/Plugins/IDataValidationPlugin.cs`
- `public interface IDataValidationPlugin`

### `src/Avalonia.Base/Data/Core/Plugins/IPropertyAccessor.cs`
- `public interface IPropertyAccessor : IDisposable`

### `src/Avalonia.Base/Data/Core/Plugins/IPropertyAccessorPlugin.cs`
- `public interface IPropertyAccessorPlugin`

### `src/Avalonia.Base/Data/Core/Plugins/IStreamPlugin.cs`
- `public interface IStreamPlugin`

### `src/Avalonia.Base/Data/Core/Plugins/IndeiValidationPlugin.cs`
- `public class IndeiValidationPlugin : IDataValidationPlugin`
- `public bool Match(WeakReference<object?> reference, string memberName) {`
- `public IPropertyAccessor Start(WeakReference<object?> reference, string name, IPropertyAccessor accessor) {`

### `src/Avalonia.Base/Data/Core/Plugins/PropertyAccessorBase.cs`
- `public abstract class PropertyAccessorBase : IPropertyAccessor`
- `public abstract Type? PropertyType { get; }`
- `public abstract object? Value { get; }`
- `public void Dispose() {`
- `public abstract bool SetValue(object? value, BindingPriority priority);`
- `public void Subscribe(Action<object?> listener) {`
- `public void Unsubscribe() {`

### `src/Avalonia.Base/Data/Core/Plugins/PropertyError.cs`
- `public class PropertyError : IPropertyAccessor`
- `public PropertyError(BindingNotification error) {`
- `public Type? PropertyType => null;`
- `public object? Value => _error;`
- `public void Dispose() {`
- `public bool SetValue(object? value, BindingPriority priority) {`
- `public void Subscribe(Action<object> listener) {`
- `public void Unsubscribe() {`

### `src/Avalonia.Base/Data/Core/PropertyPath.cs`
- `public class PropertyPath`
- `public IReadOnlyList<IPropertyPathElement> Elements { get; }`
- `public PropertyPath(IEnumerable<IPropertyPathElement> elements) {`
- `public class PropertyPathBuilder`
- `public PropertyPathBuilder Property(IPropertyInfo property) {`
- `public PropertyPathBuilder ChildTraversal() {`
- `public PropertyPathBuilder EnsureType(Type type) {`
- `public PropertyPathBuilder Cast(Type type) {`
- `public PropertyPath Build() {`
- `public interface IPropertyPathElement`
- `public class PropertyPropertyPathElement : IPropertyPathElement`
- `public IPropertyInfo Property { get; }`
- `public PropertyPropertyPathElement(IPropertyInfo property) {`
- `public class ChildTraversalPropertyPathElement : IPropertyPathElement`
- `public class EnsureTypePropertyPathElement : IPropertyPathElement`
- `public Type Type { get; }`
- `public EnsureTypePropertyPathElement(Type type) {`
- `public class CastTypePropertyPathElement : IPropertyPathElement`
- `public CastTypePropertyPathElement(Type type) {`
- `public Type Type { get; }`

### `src/Avalonia.Base/Data/Core/StreamBindingExtensions.cs`
- `public static class StreamBindingExtensions`
- `public static T StreamBinding<T>(this Task<T> @this) {`
- `public static object StreamBinding(this Task @this) {`
- `public static T StreamBinding<T>(this IObservable<T> @this) {`

### `src/Avalonia.Base/Data/Core/UntypedBindingExpressionBase.cs`
- Namespace: `Avalonia.Data.Core`
- `public abstract class UntypedBindingExpressionBase : BindingExpressionBase,`
- `public UntypedBindingExpressionBase( BindingPriority defaultPriority, AvaloniaProperty? targetProperty = null, bool isDataValidationEnabled = false) {`
- `public abstract string Description { get; }`
- `public BindingErrorType ErrorType => _error?.ErrorType ?? BindingErrorType.None;`
- `public bool IsDataValidationEnabled => _isDataValidationEnabled;`
- `public bool IsRunning => _isRunning;`
- `public BindingPriority Priority { get; private set; }`
- `public AvaloniaProperty? TargetProperty { get; private set; }`
- `public Type TargetType { get; private set; }`
- `public override void Dispose() {`
- `public object? GetValue() {`
- `public object? GetValueOrDefault() {`
- `public void Start() => Start(produceValue: true);`

### `src/Avalonia.Base/Data/CultureInfoIetfLanguageTagConverter.cs`
- Namespace: `Avalonia.Data`
- `public class CultureInfoIetfLanguageTagConverter : TypeConverter`
- `public override bool CanConvertFrom(ITypeDescriptorContext? context, Type sourceType) => sourceType == typeof(string);`
- `public override object? ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object value) {`

### `src/Avalonia.Base/Data/DataValidationException.cs`
- `public class DataValidationException : Exception`
- `public DataValidationException(object? errorData) : base(errorData?.ToString()) {`
- `public object? ErrorData { get; }`

### `src/Avalonia.Base/Data/IBinding.cs`
- `public interface IBinding`

### `src/Avalonia.Base/Data/IndexerDescriptor.cs`
- `public class IndexerDescriptor : IObservable<object?>, IDescription`
- `public BindingMode Mode {`
- `public BindingPriority Priority {`
- `public AvaloniaProperty? Property {`
- `public AvaloniaObject? Source {`
- `public IObservable<object>? SourceObservable {`
- `public string Description => $"{Source?.GetType().Name}.{Property?.Name}";`
- `public static IndexerDescriptor operator !(IndexerDescriptor binding) {`
- `public static IndexerDescriptor operator ~(IndexerDescriptor binding) {`
- `public IndexerDescriptor WithMode(BindingMode mode) {`
- `public IndexerDescriptor WithPriority(BindingPriority priority) {`
- `public IDisposable Subscribe(IObserver<object?> observer) {`

### `src/Avalonia.Base/Data/InstancedBinding.cs`
- `public sealed class InstancedBinding`
- `public BindingMode Mode { get; }`
- `public BindingPriority Priority { get; }`
- `public IObservable<object?> Source => _observable ??= _expression!.ToObservable(_target);`
- `public IObservable<object?> Observable => Source;`
- `public static InstancedBinding OneTime( object value, BindingPriority priority = BindingPriority.LocalValue) {`
- `public static InstancedBinding OneTime( IObservable<object?> observable, BindingPriority priority = BindingPriority.LocalValue) {`
- `public static InstancedBinding OneWay( IObservable<object?> observable, BindingPriority priority = BindingPriority.LocalValue) {`
- `public static InstancedBinding OneWayToSource( IObserver<object?> observer, BindingPriority priority = BindingPriority.LocalValue) {`
- `public static InstancedBinding TwoWay( IObservable<object?> observable, IObserver<object?> observer, BindingPriority priority = BindingPriority.LocalValue) {`
- `public InstancedBinding WithPriority(BindingPriority priority) {`

### `src/Avalonia.Base/Data/Optional.cs`
- `public readonly struct Optional<T> : IEquatable<Optional<T>>`
- `public Optional(T value) {`
- `public bool HasValue { get; }`
- `public T Value => HasValue ? _value : throw new InvalidOperationException("Optional has no value.");`
- `public override bool Equals(object? obj) => obj is Optional<T> o && this == o;`
- `public bool Equals(Optional<T> other) => this == other;`
- `public override int GetHashCode() => HasValue ? _value?.GetHashCode() ?? 0 : 0;`
- `public Optional<object?> ToObject() => HasValue ? new Optional<object?>(_value) : default;`
- `public override string ToString() => HasValue ? _value?.ToString() ?? "(null)" : "(empty)";`
- `public T? GetValueOrDefault() => _value;`
- `public T? GetValueOrDefault(T defaultValue) => HasValue ? _value : defaultValue;`
- `public TResult? GetValueOrDefault<TResult>() {`
- `public TResult? GetValueOrDefault<TResult>(TResult defaultValue) {`
- `public static implicit operator Optional<T>(T value) => new Optional<T>(value);`
- `public static bool operator !=(Optional<T> x, Optional<T> y) => !(x == y);`
- `public static bool operator ==(Optional<T> x, Optional<T> y) {`
- `public static Optional<T> Empty => default;`
- `public static class OptionalExtensions`
- `public static Optional<T> Cast<T>(this Optional<object?> value) {`

### `src/Avalonia.Base/Data/TemplateBinding.Observable.cs`
- `public partial class TemplateBinding : IAvaloniaSubject<object?>`
- `public IDisposable Subscribe(IObserver<object?> observer) {`

### `src/Avalonia.Base/Data/TemplateBinding.cs`
- `public partial class TemplateBinding : UntypedBindingExpressionBase,`
- `public TemplateBinding() : base(BindingPriority.Template) {`
- `public TemplateBinding([InheritDataTypeFrom(InheritDataTypeFromScopeKind.ControlTemplate)] AvaloniaProperty property) : base(BindingPriority.Template) {`
- `public IValueConverter? Converter { get; set; }`
- `public CultureInfo? ConverterCulture { get; set; }`
- `public object? ConverterParameter { get; set; }`
- `public new BindingMode Mode {`
- `public AvaloniaProperty? Property { get; set; }`
- `public override string Description => "TemplateBinding: " + Property;`
- `public IBinding ProvideValue() => this;`
- `public InstancedBinding? Initiate( AvaloniaObject target, AvaloniaProperty? targetProperty, object? anchor = null, bool enableDataValidation = false) {`

### `src/Avalonia.Base/Data/UpdateSourceTrigger.cs`
- `public enum UpdateSourceTrigger`

### `src/Avalonia.Base/Diagnostics/AvaloniaObjectExtensions.cs`
- `public static class AvaloniaObjectExtensions`
- `public static AvaloniaPropertyValue GetDiagnostic(this AvaloniaObject o, AvaloniaProperty property) {`
- `public static ValueStoreDiagnostic GetValueStoreDiagnostic(this AvaloniaObject avaloniaObject) {`

### `src/Avalonia.Base/Diagnostics/AvaloniaPropertyValue.cs`
- `public sealed class AvaloniaPropertyValue`
- `public AvaloniaProperty Property { get; }`
- `public object? Value { get; }`
- `public BindingPriority Priority { get; }`
- `public string? Diagnostic { get; }`
- `public bool IsOverriddenCurrentValue { get; }`

### `src/Avalonia.Base/Diagnostics/IValueFrameDiagnostic.cs`
- Namespace: `Avalonia.Diagnostics`
- `public record ValueEntryDiagnostic(AvaloniaProperty Property, object? Value);`
- `public interface IValueFrameDiagnostic`
- `public enum FrameType`

### `src/Avalonia.Base/Diagnostics/StyleDiagnostics.cs`
- Namespace: `Avalonia.Diagnostics`
- `public class StyleDiagnostics`
- `public IReadOnlyList<AppliedStyle> AppliedStyles { get; }`
- `public StyleDiagnostics(IReadOnlyList<AppliedStyle> appliedStyles) {`
- `public sealed class AppliedStyle`
- `public bool HasActivator => _instance.HasActivator;`
- `public bool IsActive => _instance.IsActive();`
- `public StyleBase Style => (StyleBase)_instance.Source;`

### `src/Avalonia.Base/Diagnostics/StyledElementExtensions.cs`
- Namespace: `Avalonia.Diagnostics`
- `public static class StyledElementExtensions`
- `public static StyleDiagnostics GetStyleDiagnostics(this StyledElement styledElement) {`

### `src/Avalonia.Base/Diagnostics/ValueStoreDiagnostic.cs`
- Namespace: `Avalonia.Diagnostics`
- `public class ValueStoreDiagnostic`
- `public IReadOnlyList<IValueFrameDiagnostic> AppliedFrames { get; }`

### `src/Avalonia.Base/DirectProperty.cs`
- `public class DirectProperty<TOwner, TValue> : DirectPropertyBase<TValue>, IDirectPropertyAccessor`
- `public Func<TOwner, TValue> Getter { get; }`
- `public Action<TOwner, TValue>? Setter { get; }`
- `public DirectProperty<TNewOwner, TValue> AddOwner<TNewOwner>( Func<TNewOwner, TValue> getter, Action<TNewOwner, TValue>? setter = null, TValue unsetValue = default!, BindingMode defaultBindingMode = BindingMode.Default, bool enableDataValidation = false) where TNewOwner : AvaloniaObject {`

### `src/Avalonia.Base/DirectPropertyBase.cs`
- `public abstract class DirectPropertyBase<TValue> : AvaloniaProperty<TValue>`
- `public Type Owner { get; }`
- `public TValue GetUnsetValue(Type type) => GetMetadata(type).UnsetValue;`
- `public TValue GetUnsetValue(AvaloniaObject owner) => GetMetadata(owner).UnsetValue;`
- `public new DirectPropertyMetadata<TValue> GetMetadata(Type type) => CastMetadata(base.GetMetadata(type));`
- `public new DirectPropertyMetadata<TValue> GetMetadata(AvaloniaObject owner) => CastMetadata(base.GetMetadata(owner));`
- `public void OverrideMetadata<T>(DirectPropertyMetadata<TValue> metadata) where T : AvaloniaObject {`
- `public void OverrideMetadata(Type type, DirectPropertyMetadata<TValue> metadata) {`

### `src/Avalonia.Base/DirectPropertyMetadata`1.cs`
- `public class DirectPropertyMetadata<TValue> : AvaloniaPropertyMetadata, IDirectPropertyMetadata`
- `public DirectPropertyMetadata( TValue unsetValue = default!, BindingMode defaultBindingMode = BindingMode.Default, bool? enableDataValidation = null) : base(defaultBindingMode, enableDataValidation) {`
- `public TValue UnsetValue { get; private set; }`
- `public override void Merge(AvaloniaPropertyMetadata baseMetadata, AvaloniaProperty property) {`
- `public override AvaloniaPropertyMetadata GenerateTypeSafeMetadata() {`

### `src/Avalonia.Base/IDataContextProvider.cs`
- `public interface IDataContextProvider`

### `src/Avalonia.Base/IDescription.cs`
- `public interface IDescription`

### `src/Avalonia.Base/IDirectPropertyMetadata.cs`
- `public interface IDirectPropertyMetadata`

### `src/Avalonia.Base/INamed.cs`
- `public interface INamed`

### `src/Avalonia.Base/IStyledPropertyMetadata.cs`
- `public interface IStyledPropertyMetadata`

### `src/Avalonia.Base/Input/AsyncDataTransferExtensions.cs`
- Namespace: `Avalonia.Input`
- `public static class AsyncDataTransferExtensions`
- `public static bool Contains(this IAsyncDataTransfer dataTransfer, DataFormat format) {`
- `public static IEnumerable<IAsyncDataTransferItem> GetItems(this IAsyncDataTransfer dataTransfer, DataFormat format) {`
- `public static Task<T?> TryGetValueAsync<T>(this IAsyncDataTransfer dataTransfer, DataFormat<T> format) where T : class => dataTransfer.GetItems(format).FirstOrDefault() is { } item ?`
- `public static async Task<T[]?> TryGetValuesAsync<T>(this IAsyncDataTransfer dataTransfer, DataFormat<T> format) where T : class {`
- `public static Task<string?> TryGetTextAsync(this IAsyncDataTransfer dataTransfer) => dataTransfer.TryGetValueAsync(DataFormat.Text);`
- `public static Task<IStorageItem?> TryGetFileAsync(this IAsyncDataTransfer dataTransfer) => dataTransfer.TryGetValueAsync(DataFormat.File);`
- `public static Task<IStorageItem[]?> TryGetFilesAsync(this IAsyncDataTransfer dataTransfer) => dataTransfer.TryGetValuesAsync(DataFormat.File);`
- `public static Task<Bitmap?> TryGetBitmapAsync(this IAsyncDataTransfer dataTransfer) => dataTransfer.TryGetValueAsync(DataFormat.Bitmap);`

### `src/Avalonia.Base/Input/AsyncDataTransferItemExtensions.cs`
- Namespace: `Avalonia.Input`
- `public static class AsyncDataTransferItemExtensions`
- `public static bool Contains(this IAsyncDataTransferItem dataTransferItem, DataFormat format) {`
- `public static async Task<T?> TryGetValueAsync<T>(this IAsyncDataTransferItem dataTransferItem, DataFormat<T> format) where T : class => await dataTransferItem.TryGetRawAsync(format).ConfigureAwait(false) as T;`
- `public static Task<string?> TryGetTextAsync(this IAsyncDataTransferItem dataTransferItem) => dataTransferItem.TryGetValueAsync(DataFormat.Text);`
- `public static Task<IStorageItem?> TryGetFileAsync(this IAsyncDataTransferItem dataTransferItem) => dataTransferItem.TryGetValueAsync(DataFormat.File);`
- `public static Task<Bitmap?> TryGetBitmapAsync(this IAsyncDataTransferItem dataTransferItem) => dataTransferItem.TryGetValueAsync(DataFormat.Bitmap);`

### `src/Avalonia.Base/Input/Cursor.cs`
- `public enum StandardCursorType`
- `public class Cursor : IDisposable`
- `public static readonly Cursor Default = new Cursor(StandardCursorType.Arrow);`
- `public Cursor(StandardCursorType cursorType) : this(GetCursorFactory().GetCursor(cursorType), cursorType.ToString()) {`
- `public Cursor(Bitmap cursor, PixelPoint hotSpot) : this(GetCursorFactory().CreateCursor(cursor.PlatformImpl.Item, hotSpot), "BitmapCursor") {`
- `public void Dispose() => PlatformImpl.Dispose();`
- `public static Cursor Parse(string s) {`
- `public override string ToString() {`

### `src/Avalonia.Base/Input/DataFormat.cs`
- Namespace: `Avalonia.Input`
- `public abstract class DataFormat : IEquatable<DataFormat>`
- `public DataFormatKind Kind { get; }`
- `public string Identifier { get; }`
- `public static DataFormat<string> Text { get; } = CreateUniversalFormat<string>("Text");`
- `public static DataFormat<Bitmap> Bitmap { get; } = CreateUniversalFormat<Bitmap>("Bitmap");`
- `public static DataFormat<IStorageItem> File { get; } = CreateUniversalFormat<IStorageItem>("File");`
- `public string ToSystemName(string applicationPrefix) {`
- `public bool Equals(DataFormat? other) {`
- `public override bool Equals(object? obj) => Equals(obj as DataFormat);`
- `public override int GetHashCode() => ((int)Kind * 397) ^ Identifier.GetHashCode();`
- `public static bool operator ==(DataFormat? left, DataFormat? right) => Equals(left, right);`
- `public static bool operator !=(DataFormat? left, DataFormat? right) => !Equals(left, right);`
- `public static DataFormat<byte[]> CreateBytesApplicationFormat(string identifier) => CreateApplicationFormat<byte[]>(identifier);`
- `public static DataFormat<string> CreateStringApplicationFormat(string identifier) => CreateApplicationFormat<string>(identifier);`
- `public static DataFormat<byte[]> CreateBytesPlatformFormat(string identifier) => CreatePlatformFormat<byte[]>(identifier);`
- `public static DataFormat<string> CreateStringPlatformFormat(string identifier) => CreatePlatformFormat<string>(identifier);`
- `public static DataFormat<T> FromSystemName<T>(string systemName, string applicationPrefix) where T : class {`
- `public override string ToString() => $"{Kind}: {Identifier}";`

### `src/Avalonia.Base/Input/DataFormatKind.cs`
- `public enum DataFormatKind`

### `src/Avalonia.Base/Input/DataFormatOfT.cs`
- Namespace: `Avalonia.Input`
- `public sealed class DataFormat<T> : DataFormat`

### `src/Avalonia.Base/Input/DataFormats.cs`
- `public static class DataFormats`
- `public static readonly string Text = nameof(Text);`
- `public static readonly string Files = nameof(Files);`
- `public static readonly string FileNames = nameof(FileNames);`

### `src/Avalonia.Base/Input/DataObject.cs`
- `public class DataObject : IDataObject`
- `public bool Contains(string dataFormat) {`
- `public object? Get(string dataFormat) {`
- `public IEnumerable<string> GetDataFormats() {`
- `public void Set(string dataFormat, object value) {`

### `src/Avalonia.Base/Input/DataObjectExtensions.cs`
- `public static class DataObjectExtensions`
- `public static IEnumerable<IStorageItem>? GetFiles(this IDataObject dataObject) {`
- `public static IEnumerable<string>? GetFileNames(this IDataObject dataObject) {`
- `public static string? GetText(this IDataObject dataObject) {`

### `src/Avalonia.Base/Input/DataTransfer.cs`
- Namespace: `Avalonia.Input`
- `public sealed class DataTransfer : IDataTransfer, IAsyncDataTransfer`
- `public IReadOnlyList<DataFormat> Formats {`
- `public IReadOnlyList<DataTransferItem> Items => _items;`
- `public void Add(DataTransferItem item) {`

### `src/Avalonia.Base/Input/DataTransferExtensions.cs`
- Namespace: `Avalonia.Input`
- `public static class DataTransferExtensions`
- `public static bool Contains(this IDataTransfer dataTransfer, DataFormat format) {`
- `public static IEnumerable<IDataTransferItem> GetItems(this IDataTransfer dataTransfer, DataFormat format) {`
- `public static T? TryGetValue<T>(this IDataTransfer dataTransfer, DataFormat<T> format) where T : class => dataTransfer.GetItems(format).FirstOrDefault() is { } item ?`
- `public static T[]? TryGetValues<T>(this IDataTransfer dataTransfer, DataFormat<T> format) where T : class {`
- `public static string? TryGetText(this IDataTransfer dataTransfer) => dataTransfer.TryGetValue(DataFormat.Text);`
- `public static IStorageItem? TryGetFile(this IDataTransfer dataTransfer) => dataTransfer.TryGetValue(DataFormat.File);`
- `public static IStorageItem[]? TryGetFiles(this IDataTransfer dataTransfer) => dataTransfer.TryGetValues(DataFormat.File);`
- `public static Bitmap? TryGetBitmap(this IDataTransfer dataTransfer) => dataTransfer.TryGetValue(DataFormat.Bitmap);`

### `src/Avalonia.Base/Input/DataTransferItem.cs`
- Namespace: `Avalonia.Input`
- `public sealed class DataTransferItem : IDataTransferItem, IAsyncDataTransferItem`
- `public IReadOnlyList<DataFormat> Formats {`
- `public object? TryGetRaw(DataFormat format) => FindAccessor(format)?.GetValue();`
- `public void Set<T>(DataFormat<T> format, T? value) where T : class {`
- `public void Set<T>(DataFormat<T> format, Func<T?> getValue) where T : class {`
- `public void SetText(string? value) => Set(DataFormat.Text, value);`
- `public void SetFile(IStorageItem? value) => Set(DataFormat.File, value);`
- `public void SetBitmap(Bitmap? value) => Set(DataFormat.Bitmap, value);`
- `public static DataTransferItem Create<T>(DataFormat<T> format, T? value) where T : class {`
- `public static DataTransferItem Create<T>(DataFormat<T> format, Func<T?> getValue) where T : class {`
- `public static DataTransferItem CreateText(string? value) => Create(DataFormat.Text, value);`
- `public static DataTransferItem CreateFile(IStorageItem? value) => Create(DataFormat.File, value);`

### `src/Avalonia.Base/Input/DataTransferItemExtensions.cs`
- Namespace: `Avalonia.Input`
- `public static class DataTransferItemExtensions`
- `public static bool Contains(this IDataTransferItem dataTransferItem, DataFormat format) {`
- `public static T? TryGetValue<T>(this IDataTransferItem dataTransferItem, DataFormat<T> format) where T : class => dataTransferItem.TryGetRaw(format) as T;`
- `public static string? TryGetText(this IDataTransferItem dataTransferItem) => dataTransferItem.TryGetValue(DataFormat.Text);`
- `public static IStorageItem? TryGetFile(this IDataTransferItem dataTransferItem) => dataTransferItem.TryGetValue(DataFormat.File);`
- `public static Bitmap? TryGetBitmap(this IDataTransferItem dataTransferItem) => dataTransferItem.TryGetValue(DataFormat.Bitmap);`

### `src/Avalonia.Base/Input/DragDrop.cs`
- `public static class DragDrop`
- `public static readonly RoutedEvent<DragEventArgs> DragEnterEvent = RoutedEvent.Register<DragEventArgs>("DragEnter", RoutingStrategies.Bubble, typeof(DragDrop));`
- `public static readonly RoutedEvent<DragEventArgs> DragLeaveEvent = RoutedEvent.Register<DragEventArgs>("DragLeave", RoutingStrategies.Bubble, typeof(DragDrop));`
- `public static readonly RoutedEvent<DragEventArgs> DragOverEvent = RoutedEvent.Register<DragEventArgs>("DragOver", RoutingStrategies.Bubble, typeof(DragDrop));`
- `public static readonly RoutedEvent<DragEventArgs> DropEvent = RoutedEvent.Register<DragEventArgs>("Drop", RoutingStrategies.Bubble, typeof(DragDrop));`
- `public static readonly AttachedProperty<bool> AllowDropProperty = AvaloniaProperty.RegisterAttached<Interactive, bool>("AllowDrop", typeof(DragDrop), inherits: true);`
- `public static bool GetAllowDrop(Interactive interactive) {`
- `public static void SetAllowDrop(Interactive interactive, bool value) {`
- `public static void AddDragEnterHandler(Interactive element, EventHandler<DragEventArgs> handler) {`
- `public static void RemoveDragEnterHandler(Interactive element, EventHandler<DragEventArgs> handler) {`
- `public static void AddDragLeaveHandler(Interactive element, EventHandler<DragEventArgs> handler) {`
- `public static void RemoveDragLeaveHandler(Interactive element, EventHandler<DragEventArgs> handler) {`
- `public static void AddDragOverHandler(Interactive element, EventHandler<DragEventArgs> handler) {`
- `public static void RemoveDragOverHandler(Interactive element, EventHandler<DragEventArgs> handler) {`
- `public static void AddDropHandler(Interactive element, EventHandler<DragEventArgs> handler) {`
- `public static void RemoveDropHandler(Interactive element, EventHandler<DragEventArgs> handler) {`
- `public static Task<DragDropEffects> DoDragDrop(PointerEventArgs triggerEvent, IDataObject data, DragDropEffects allowedEffects) {`
- `public static Task<DragDropEffects> DoDragDropAsync( PointerEventArgs triggerEvent, IDataTransfer dataTransfer, DragDropEffects allowedEffects) {`

### `src/Avalonia.Base/Input/DragDropDevice.cs`
- `public class DragDropDevice : IDragDropDevice`
- `public static readonly DragDropDevice Instance = new DragDropDevice();`
- `public void ProcessRawEvent(RawInputEventArgs e) {`

### `src/Avalonia.Base/Input/DragDropEffects.cs`
- `public enum DragDropEffects`

### `src/Avalonia.Base/Input/DragEventArgs.cs`
- `public class DragEventArgs : RoutedEventArgs`
- `public DragDropEffects DragEffects { get; set; }`
- `public IDataTransfer DataTransfer { get; }`
- `public IDataObject Data => _legacyDataObject ??= DataTransfer.ToLegacyDataObject();`
- `public KeyModifiers KeyModifiers { get; }`
- `public Point GetPosition(Visual relativeTo) {`
- `public DragEventArgs( RoutedEvent<DragEventArgs> routedEvent, IDataObject data, Interactive target, Point targetLocation, KeyModifiers keyModifiers) : this(routedEvent, new DataObjectToDataTransferWrapper(data), target, targetLocation, keyModifiers) {`
- `public DragEventArgs( RoutedEvent<DragEventArgs> routedEvent, IDataTransfer dataTransfer, Interactive target, Point targetLocation, KeyModifiers keyModifiers) : base(routedEvent) {`

### `src/Avalonia.Base/Input/FocusManager.cs`
- `public class FocusManager : IFocusManager`
- `public IInputElement? GetFocusedElement() => Current;`
- `public bool Focus( IInputElement? control, NavigationMethod method = NavigationMethod.Unspecified, KeyModifiers keyModifiers = KeyModifiers.None) {`
- `public void ClearFocus() {`
- `public void ClearFocusOnElementRemoved(IInputElement removedElement, Visual oldParent) {`
- `public IInputElement? GetFocusedElement(IFocusScope scope) {`
- `public void SetFocusScope(IFocusScope scope) {`
- `public void RemoveFocusRoot(IFocusScope scope) {`
- `public static bool GetIsFocusScope(IInputElement e) => e is IFocusScope;`

### `src/Avalonia.Base/Input/GestureRecognizers/GestureRecognizer.cs`
- `public abstract class GestureRecognizer : StyledElement`

### `src/Avalonia.Base/Input/GestureRecognizers/GestureRecognizerCollection.cs`
- `public class GestureRecognizerCollection : IReadOnlyCollection<GestureRecognizer>`
- `public GestureRecognizerCollection(IInputElement inputElement) {`
- `public void Add(GestureRecognizer recognizer) {`
- `public IEnumerator<GestureRecognizer> GetEnumerator() => _recognizers?.GetEnumerator() ?? s_Empty.GetEnumerator();`
- `public int Count => _recognizers?.Count ?? 0;`

### `src/Avalonia.Base/Input/GestureRecognizers/PinchGestureRecognizer.cs`
- `public class PinchGestureRecognizer : GestureRecognizer`

### `src/Avalonia.Base/Input/GestureRecognizers/PullGestureRecognizer.cs`
- `public class PullGestureRecognizer : GestureRecognizer`
- `public static readonly StyledProperty<PullDirection> PullDirectionProperty = AvaloniaProperty.Register<PullGestureRecognizer, PullDirection>(nameof(PullDirection));`
- `public PullDirection PullDirection {`
- `public PullGestureRecognizer(PullDirection pullDirection) {`
- `public PullGestureRecognizer() { }`

### `src/Avalonia.Base/Input/GestureRecognizers/ScrollGestureRecognizer.cs`
- `public class ScrollGestureRecognizer : GestureRecognizer`
- `public const double InertialResistance = 0.15;`
- `public static readonly DirectProperty<ScrollGestureRecognizer, bool> CanHorizontallyScrollProperty = AvaloniaProperty.RegisterDirect<ScrollGestureRecognizer, bool>(nameof(CanHorizontallyScroll), o => o.CanHorizontallyScroll, (o, v) => o.CanHorizontallyScroll = v);`
- `public static readonly DirectProperty<ScrollGestureRecognizer, bool> CanVerticallyScrollProperty = AvaloniaProperty.RegisterDirect<ScrollGestureRecognizer, bool>(nameof(CanVerticallyScroll), o => o.CanVerticallyScroll, (o, v) => o.CanVerticallyScroll = v);`
- `public static readonly DirectProperty<ScrollGestureRecognizer, bool> IsScrollInertiaEnabledProperty = AvaloniaProperty.RegisterDirect<ScrollGestureRecognizer, bool>(nameof(IsScrollInertiaEnabled), o => o.IsScrollInertiaEnabled, (o,v) => o.IsScrollInertiaEnabled = v);`
- `public static readonly DirectProperty<ScrollGestureRecognizer, int> ScrollStartDistanceProperty = AvaloniaProperty.RegisterDirect<ScrollGestureRecognizer, int>(nameof(ScrollStartDistance), o => o.ScrollStartDistance, (o, v) => o.ScrollStartDistance = v,`
- `public bool CanHorizontallyScroll {`
- `public bool CanVerticallyScroll {`
- `public bool IsScrollInertiaEnabled {`
- `public int ScrollStartDistance {`

### `src/Avalonia.Base/Input/Gestures.cs`
- `public static class Gestures`
- `public static readonly AttachedProperty<bool> IsHoldingEnabledProperty = AvaloniaProperty.RegisterAttached<StyledElement, bool>("IsHoldingEnabled", typeof(Gestures), true);`
- `public static readonly AttachedProperty<bool> IsHoldWithMouseEnabledProperty = AvaloniaProperty.RegisterAttached<StyledElement, bool>("IsHoldWithMouseEnabled", typeof(Gestures), false);`
- `public static readonly RoutedEvent<TappedEventArgs> TappedEvent = RoutedEvent.Register<TappedEventArgs>( "Tapped", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<TappedEventArgs> DoubleTappedEvent = RoutedEvent.Register<TappedEventArgs>( "DoubleTapped", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<TappedEventArgs> RightTappedEvent = RoutedEvent.Register<TappedEventArgs>( "RightTapped", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<ScrollGestureEventArgs> ScrollGestureEvent = RoutedEvent.Register<ScrollGestureEventArgs>( "ScrollGesture", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<ScrollGestureInertiaStartingEventArgs> ScrollGestureInertiaStartingEvent = RoutedEvent.Register<ScrollGestureInertiaStartingEventArgs>( "ScrollGestureInertiaStarting", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<ScrollGestureEndedEventArgs> ScrollGestureEndedEvent = RoutedEvent.Register<ScrollGestureEndedEventArgs>( "ScrollGestureEnded", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<PointerDeltaEventArgs> PointerTouchPadGestureMagnifyEvent = RoutedEvent.Register<PointerDeltaEventArgs>( "PointerTouchPadGestureMagnify", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<PointerDeltaEventArgs> PointerTouchPadGestureRotateEvent = RoutedEvent.Register<PointerDeltaEventArgs>( "PointerTouchPadGestureRotate", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<PointerDeltaEventArgs> PointerTouchPadGestureSwipeEvent = RoutedEvent.Register<PointerDeltaEventArgs>( "PointerTouchPadGestureSwipe", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<PinchEventArgs> PinchEvent = RoutedEvent.Register<PinchEventArgs>( "Pinch", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<PinchEndedEventArgs> PinchEndedEvent = RoutedEvent.Register<PinchEndedEventArgs>( "PinchEnded", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<PullGestureEventArgs> PullGestureEvent = RoutedEvent.Register<PullGestureEventArgs>( "PullGesture", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<HoldingRoutedEventArgs> HoldingEvent = RoutedEvent.Register<HoldingRoutedEventArgs>( "Holding", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<PullGestureEndedEventArgs> PullGestureEndedEvent = RoutedEvent.Register<PullGestureEndedEventArgs>( "PullGestureEnded", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static bool GetIsHoldingEnabled(StyledElement element) {`
- `public static void SetIsHoldingEnabled(StyledElement element, bool value) {`
- `public static bool GetIsHoldWithMouseEnabled(StyledElement element) {`
- `public static void SetIsHoldWithMouseEnabled(StyledElement element, bool value) {`
- `public static void AddTappedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`
- `public static void AddDoubleTappedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`
- `public static void AddRightTappedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`
- `public static void AddHoldingHandler(Interactive element, EventHandler<HoldingRoutedEventArgs> handler) =>`
- `public static void AddPinchHandler(Interactive element, EventHandler<PinchEventArgs> handler) =>`
- `public static void AddPinchEndedHandler(Interactive element, EventHandler<PinchEndedEventArgs> handler) =>`
- `public static void AddPullGestureHandler(Interactive element, EventHandler<PullGestureEventArgs> handler) =>`
- `public static void AddPullGestureEndedHandler(Interactive element, EventHandler<PullGestureEndedEventArgs> handler) =>`
- `public static void AddPointerTouchPadGestureMagnifyHandler(Interactive element, EventHandler<PointerDeltaEventArgs> handler) =>`
- `public static void AddPointerTouchPadGestureRotateHandler(Interactive element, EventHandler<PointerDeltaEventArgs> handler) =>`
- `public static void AddPointerTouchPadGestureSwipeHandler(Interactive element, EventHandler<PointerDeltaEventArgs> handler) =>`
- `public static void AddScrollGestureHandler(Interactive element, EventHandler<RoutedEventArgs> handler) =>`
- `public static void AddScrollGestureEndedHandler(Interactive element, EventHandler<ScrollGestureEndedEventArgs> handler) =>`
- `public static void AddScrollGestureInertiaStartingHandler(Interactive element, EventHandler<ScrollGestureInertiaStartingEventArgs> handler) =>`
- `public static void RemoveTappedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`
- `public static void RemoveDoubleTappedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`
- `public static void RemoveRightTappedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`
- `public static void RemoveHoldingHandler(Interactive element, EventHandler<RoutedEventArgs> handler) =>`
- `public static void RemovePinchHandler(Interactive element, EventHandler<PinchEventArgs> handler) =>`
- `public static void RemovePinchEndedHandler(Interactive element, EventHandler<PinchEndedEventArgs> handler) =>`
- `public static void RemovePullGestureHandler(Interactive element, EventHandler<PullGestureEventArgs> handler) =>`
- `public static void RemovePullGestureEndedHandler(Interactive element, EventHandler<PullGestureEndedEventArgs> handler) =>`
- `public static void RemovePointerTouchPadGestureMagnifyHandler(Interactive element, EventHandler<PointerDeltaEventArgs> handler) =>`
- `public static void RemovePointerTouchPadGestureRotateHandler(Interactive element, EventHandler<PointerDeltaEventArgs> handler) =>`
- `public static void RemovePointerTouchPadGestureSwipeHandler(Interactive element, EventHandler<PointerDeltaEventArgs> handler) =>`
- `public static void RemoveScrollGestureHandler(Interactive element, EventHandler<ScrollGestureEventArgs> handler) =>`
- `public static void RemoveScrollGestureEndedHandler(Interactive element,EventHandler<ScrollGestureEndedEventArgs> handler) =>`
- `public static void RemoveScrollGestureInertiaStartingHandler(Interactive element, EventHandler<ScrollGestureInertiaStartingEventArgs> handler) =>`

### `src/Avalonia.Base/Input/GotFocusEventArgs.cs`
- `public class GotFocusEventArgs : RoutedEventArgs`
- `public GotFocusEventArgs() : base(InputElement.GotFocusEvent) {`
- `public NavigationMethod NavigationMethod { get; init; }`
- `public KeyModifiers KeyModifiers { get; init; }`

### `src/Avalonia.Base/Input/HoldingRoutedEventArgs.cs`
- `public class HoldingRoutedEventArgs : RoutedEventArgs`
- `public HoldingState HoldingState { get; }`
- `public Point Position { get; }`
- `public PointerType PointerType { get; }`
- `public HoldingRoutedEventArgs(HoldingState holdingState, Point position, PointerType pointerType) : base(Gestures.HoldingEvent) {`
- `public enum HoldingState`

### `src/Avalonia.Base/Input/IAsyncDataTransfer.cs`
- Namespace: `Avalonia.Input`
- `public interface IAsyncDataTransfer : IDisposable`

### `src/Avalonia.Base/Input/IAsyncDataTransferItem.cs`
- Namespace: `Avalonia.Input`
- `public interface IAsyncDataTransferItem`

### `src/Avalonia.Base/Input/ICloseable.cs`
- `public interface ICloseable`

### `src/Avalonia.Base/Input/ICommandSource.cs`
- `public interface ICommandSource`

### `src/Avalonia.Base/Input/ICustomKeyboardNavigation.cs`
- `public interface ICustomKeyboardNavigation`

### `src/Avalonia.Base/Input/IDataObject.cs`
- `public interface IDataObject`

### `src/Avalonia.Base/Input/IDataTransfer.cs`
- Namespace: `Avalonia.Input`
- `public interface IDataTransfer : IDisposable`

### `src/Avalonia.Base/Input/IDataTransferItem.cs`
- Namespace: `Avalonia.Input`
- `public interface IDataTransferItem`

### `src/Avalonia.Base/Input/IFocusManager.cs`
- `public interface IFocusManager`

### `src/Avalonia.Base/Input/IFocusScope.cs`
- `public interface IFocusScope`

### `src/Avalonia.Base/Input/IInputDevice.cs`
- `public interface IInputDevice`

### `src/Avalonia.Base/Input/IInputElement.cs`
- `public interface IInputElement`

### `src/Avalonia.Base/Input/IInputManager.cs`
- `public interface IInputManager`

### `src/Avalonia.Base/Input/IInputRoot.cs`
- `public interface IInputRoot : IInputElement`

### `src/Avalonia.Base/Input/IKeyboardDevice.cs`
- `public enum KeyModifiers`
- `public enum KeyStates`
- `public enum RawInputModifiers`
- `public interface IKeyboardDevice : IInputDevice`

### `src/Avalonia.Base/Input/IKeyboardNavigationHandler.cs`
- `public interface IKeyboardNavigationHandler`

### `src/Avalonia.Base/Input/IMouseDevice.cs`
- `public interface IMouseDevice : IPointerDevice`

### `src/Avalonia.Base/Input/INavigableContainer.cs`
- `public interface INavigableContainer`

### `src/Avalonia.Base/Input/IPenDevice.cs`
- `public interface IPenDevice : IPointerDevice`

### `src/Avalonia.Base/Input/IPointer.cs`
- `public interface IPointer`
- `public enum PointerType`

### `src/Avalonia.Base/Input/IPointerDevice.cs`
- `public interface IPointerDevice : IInputDevice`

### `src/Avalonia.Base/Input/InputElement.cs`
- `public class InputElement : Interactive, IInputElement`
- `public static readonly StyledProperty<bool> FocusableProperty = AvaloniaProperty.Register<InputElement, bool>(nameof(Focusable));`
- `public static readonly StyledProperty<bool> IsEnabledProperty = AvaloniaProperty.Register<InputElement, bool>(nameof(IsEnabled), true);`
- `public static readonly DirectProperty<InputElement, bool> IsEffectivelyEnabledProperty = AvaloniaProperty.RegisterDirect<InputElement, bool>( nameof(IsEffectivelyEnabled), o => o.IsEffectivelyEnabled);`
- `public static readonly StyledProperty<Cursor?> CursorProperty = AvaloniaProperty.Register<InputElement, Cursor?>(nameof(Cursor), null, true);`
- `public static readonly DirectProperty<InputElement, bool> IsKeyboardFocusWithinProperty = AvaloniaProperty.RegisterDirect<InputElement, bool>( nameof(IsKeyboardFocusWithin), o => o.IsKeyboardFocusWithin);`
- `public static readonly DirectProperty<InputElement, bool> IsFocusedProperty = AvaloniaProperty.RegisterDirect<InputElement, bool>(nameof(IsFocused), o => o.IsFocused);`
- `public static readonly StyledProperty<bool> IsHitTestVisibleProperty = AvaloniaProperty.Register<InputElement, bool>(nameof(IsHitTestVisible), true);`
- `public static readonly DirectProperty<InputElement, bool> IsPointerOverProperty = AvaloniaProperty.RegisterDirect<InputElement, bool>(nameof(IsPointerOver), o => o.IsPointerOver);`
- `public static readonly StyledProperty<bool> IsTabStopProperty = KeyboardNavigation.IsTabStopProperty.AddOwner<InputElement>();`
- `public static readonly RoutedEvent<GotFocusEventArgs> GotFocusEvent = RoutedEvent.Register<InputElement, GotFocusEventArgs>(nameof(GotFocus), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<RoutedEventArgs> LostFocusEvent = RoutedEvent.Register<InputElement, RoutedEventArgs>(nameof(LostFocus), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<KeyEventArgs> KeyDownEvent = RoutedEvent.Register<InputElement, KeyEventArgs>( nameof(KeyDown), RoutingStrategies.Tunnel | RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<KeyEventArgs> KeyUpEvent = RoutedEvent.Register<InputElement, KeyEventArgs>( nameof(KeyUp), RoutingStrategies.Tunnel | RoutingStrategies.Bubble);`
- `public static readonly StyledProperty<int> TabIndexProperty = KeyboardNavigation.TabIndexProperty.AddOwner<InputElement>();`
- `public static readonly RoutedEvent<TextInputEventArgs> TextInputEvent = RoutedEvent.Register<InputElement, TextInputEventArgs>( nameof(TextInput), RoutingStrategies.Tunnel | RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<TextInputMethodClientRequestedEventArgs> TextInputMethodClientRequestedEvent = RoutedEvent.Register<InputElement, TextInputMethodClientRequestedEventArgs>( nameof(TextInputMethodClientRequested), RoutingStrategies.Tunnel | RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<PointerEventArgs> PointerEnteredEvent = RoutedEvent.Register<InputElement, PointerEventArgs>( nameof(PointerEntered), RoutingStrategies.Direct);`
- `public static readonly RoutedEvent<PointerEventArgs> PointerExitedEvent = RoutedEvent.Register<InputElement, PointerEventArgs>( nameof(PointerExited), RoutingStrategies.Direct);`
- `public static readonly RoutedEvent<PointerEventArgs> PointerMovedEvent = RoutedEvent.Register<InputElement, PointerEventArgs>( nameof(PointerMoved), RoutingStrategies.Tunnel | RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<PointerPressedEventArgs> PointerPressedEvent = RoutedEvent.Register<InputElement, PointerPressedEventArgs>( nameof(PointerPressed), RoutingStrategies.Tunnel | RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<PointerReleasedEventArgs> PointerReleasedEvent = RoutedEvent.Register<InputElement, PointerReleasedEventArgs>( nameof(PointerReleased), RoutingStrategies.Tunnel | RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<PointerCaptureLostEventArgs> PointerCaptureLostEvent = RoutedEvent.Register<InputElement, PointerCaptureLostEventArgs>( nameof(PointerCaptureLost), RoutingStrategies.Direct);`
- `public static readonly RoutedEvent<PointerWheelEventArgs> PointerWheelChangedEvent = RoutedEvent.Register<InputElement, PointerWheelEventArgs>( nameof(PointerWheelChanged), RoutingStrategies.Tunnel | RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<TappedEventArgs> TappedEvent = Gestures.TappedEvent;`
- `public static readonly RoutedEvent<HoldingRoutedEventArgs> HoldingEvent = Gestures.HoldingEvent;`
- `public static readonly RoutedEvent<TappedEventArgs> DoubleTappedEvent = Gestures.DoubleTappedEvent;`
- `public InputElement() {`
- `public event EventHandler<GotFocusEventArgs>? GotFocus {`
- `public event EventHandler<RoutedEventArgs>? LostFocus {`
- `public event EventHandler<KeyEventArgs>? KeyDown {`
- `public event EventHandler<KeyEventArgs>? KeyUp {`
- `public event EventHandler<TextInputEventArgs>? TextInput {`
- `public event EventHandler<TextInputMethodClientRequestedEventArgs>? TextInputMethodClientRequested {`
- `public event EventHandler<PointerEventArgs>? PointerEntered {`
- `public event EventHandler<PointerEventArgs>? PointerExited {`
- `public event EventHandler<PointerEventArgs>? PointerMoved {`
- `public event EventHandler<PointerPressedEventArgs>? PointerPressed {`
- `public event EventHandler<PointerReleasedEventArgs>? PointerReleased {`
- `public event EventHandler<PointerCaptureLostEventArgs>? PointerCaptureLost {`
- `public event EventHandler<PointerWheelEventArgs>? PointerWheelChanged {`
- `public event EventHandler<TappedEventArgs>? Tapped {`
- `public event EventHandler<HoldingRoutedEventArgs>? Holding {`
- `public event EventHandler<TappedEventArgs>? DoubleTapped {`
- `public bool Focusable {`
- `public bool IsEnabled {`
- `public Cursor? Cursor {`
- `public bool IsKeyboardFocusWithin {`
- `public bool IsFocused {`
- `public bool IsHitTestVisible {`
- `public bool IsPointerOver {`
- `public bool IsTabStop {`
- `public bool IsEffectivelyEnabled {`
- `public int TabIndex {`
- `public List<KeyBinding> KeyBindings { get; } = new List<KeyBinding>();`
- `public GestureRecognizerCollection GestureRecognizers => _gestureRecognizers ?? (_gestureRecognizers = new GestureRecognizerCollection(this));`
- `public bool Focus(NavigationMethod method = NavigationMethod.Unspecified, KeyModifiers keyModifiers = KeyModifiers.None) {`

### `src/Avalonia.Base/Input/InputExtensions.cs`
- `public static class InputExtensions`
- `public static IEnumerable<IInputElement> GetInputElementsAt(this IInputElement element, Point p, bool enabledElementsOnly = true) {`
- `public static IEnumerable<IInputElement> GetInputElementsAt(this IInputElement element, Point p) => GetInputElementsAt(element, p, true);`
- `public static IInputElement? InputHitTest(this IInputElement element, Point p, bool enabledElementsOnly = true) {`
- `public static IInputElement? InputHitTest(this IInputElement element, Point p) => InputHitTest(element, p, true);`
- `public static IInputElement? InputHitTest( this IInputElement element, Point p, Func<Visual, bool> filter, bool enabledElementsOnly = true) {`
- `public static IInputElement? InputHitTest(this IInputElement element, Point p, Func<Visual, bool> filter) => InputHitTest(element, p, filter, true);`

### `src/Avalonia.Base/Input/InputMethod.cs`
- `public class InputMethod`
- `public static readonly AvaloniaProperty<bool> IsInputMethodEnabledProperty = AvaloniaProperty.RegisterAttached<InputMethod, InputElement, bool>("IsInputMethodEnabled", true);`
- `public static void SetIsInputMethodEnabled(InputElement target, bool value) {`
- `public static bool GetIsInputMethodEnabled(InputElement target) {`
- `public static readonly RoutedEvent<TextInputMethodClientRequeryRequestedEventArgs> TextInputMethodClientRequeryRequestedEvent = RoutedEvent.Register<InputElement, TextInputMethodClientRequeryRequestedEventArgs>( "TextInputMethodClientRequeryRequested", RoutingStrategies.Bubble);`
- `public static void AddTextInputMethodClientRequeryRequestedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`
- `public static void RemoveTextInputMethodClientRequeryRequestedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`

### `src/Avalonia.Base/Input/Key.cs`
- `public enum Key`

### `src/Avalonia.Base/Input/KeyBinding.cs`
- `public class KeyBinding : AvaloniaObject`
- `public static readonly StyledProperty<ICommand> CommandProperty = AvaloniaProperty.Register<KeyBinding, ICommand>(nameof(Command));`
- `public ICommand Command {`
- `public static readonly StyledProperty<object> CommandParameterProperty = AvaloniaProperty.Register<KeyBinding, object>(nameof(CommandParameter));`
- `public object CommandParameter {`
- `public static readonly StyledProperty<KeyGesture> GestureProperty = AvaloniaProperty.Register<KeyBinding, KeyGesture>(nameof(Gesture));`
- `public KeyGesture Gesture {`
- `public void TryHandle(KeyEventArgs args) {`

### `src/Avalonia.Base/Input/KeyDeviceType.cs`
- Namespace: `Avalonia.Input`
- `public enum KeyDeviceType`

### `src/Avalonia.Base/Input/KeyEventArgs.cs`
- Namespace: `Avalonia.Input`
- `public class KeyEventArgs : RoutedEventArgs`
- `public Key Key { get; init; }`
- `public KeyModifiers KeyModifiers { get; init; }`
- `public PhysicalKey PhysicalKey { get; init; }`
- `public string? KeySymbol { get; init; }`
- `public KeyDeviceType KeyDeviceType { get; init; }`

### `src/Avalonia.Base/Input/KeyGesture.cs`
- `public sealed class KeyGesture : IEquatable<KeyGesture>, IFormattable`
- `public KeyGesture(Key key, KeyModifiers modifiers = KeyModifiers.None) {`
- `public bool Equals(KeyGesture? other) {`
- `public override bool Equals(object? obj) {`
- `public override int GetHashCode() {`
- `public static bool operator ==(KeyGesture? left, KeyGesture? right) {`
- `public static bool operator !=(KeyGesture? left, KeyGesture? right) {`
- `public Key Key { get; }`
- `public KeyModifiers KeyModifiers { get; }`
- `public static KeyGesture Parse(string gesture) {`
- `public override string ToString() => ToString(null, null);`
- `public string ToString(string? format, IFormatProvider? formatProvider) {`
- `public bool Matches(KeyEventArgs? keyEvent) =>`

### `src/Avalonia.Base/Input/KeyboardDevice.cs`
- `public class KeyboardDevice : IKeyboardDevice, INotifyPropertyChanged`
- `public event PropertyChangedEventHandler? PropertyChanged;`
- `public IInputManager? InputManager => AvaloniaLocator.Current.GetService<IInputManager>();`
- `public IFocusManager? FocusManager => AvaloniaLocator.Current.GetService<IFocusManager>();`
- `public IInputElement? FocusedElement => _focusedElement;`
- `public void SetFocusedElement( IInputElement? element, NavigationMethod method, KeyModifiers keyModifiers) {`
- `public void ProcessRawEvent(RawInputEventArgs e) {`

### `src/Avalonia.Base/Input/KeyboardNavigation.cs`
- `public static class KeyboardNavigation`
- `public static readonly AttachedProperty<int> TabIndexProperty = AvaloniaProperty.RegisterAttached<StyledElement, int>( "TabIndex", typeof(KeyboardNavigation), int.MaxValue);`
- `public static readonly AttachedProperty<KeyboardNavigationMode> TabNavigationProperty = AvaloniaProperty.RegisterAttached<InputElement, KeyboardNavigationMode>( "TabNavigation", typeof(KeyboardNavigation));`
- `public static readonly AttachedProperty<IInputElement?> TabOnceActiveElementProperty = AvaloniaProperty.RegisterAttached<InputElement, IInputElement?>( "TabOnceActiveElement", typeof(KeyboardNavigation));`
- `public static readonly AttachedProperty<bool> IsTabStopProperty = AvaloniaProperty.RegisterAttached<InputElement, bool>( "IsTabStop", typeof(KeyboardNavigation), true);`
- `public static int GetTabIndex(IInputElement element) {`
- `public static void SetTabIndex(IInputElement element, int value) {`
- `public static KeyboardNavigationMode GetTabNavigation(InputElement element) {`
- `public static void SetTabNavigation(InputElement element, KeyboardNavigationMode value) {`
- `public static IInputElement? GetTabOnceActiveElement(InputElement element) {`
- `public static void SetTabOnceActiveElement(InputElement element, IInputElement? value) {`
- `public static void SetIsTabStop(InputElement element, bool value) {`
- `public static bool GetIsTabStop(InputElement element) {`

### `src/Avalonia.Base/Input/KeyboardNavigationHandler.cs`
- `public sealed class KeyboardNavigationHandler : IKeyboardNavigationHandler`
- `public void SetOwner(IInputRoot owner) {`
- `public static IInputElement? GetNext( IInputElement element, NavigationDirection direction) {`
- `public void Move( IInputElement? element, NavigationDirection direction, KeyModifiers keyModifiers = KeyModifiers.None) {`

### `src/Avalonia.Base/Input/KeyboardNavigationMode.cs`
- `public enum KeyboardNavigationMode`

### `src/Avalonia.Base/Input/MouseDevice.cs`
- `public class MouseDevice : IMouseDevice, IDisposable`
- `public MouseDevice(Pointer? pointer = null) {`
- `public void ProcessRawEvent(RawInputEventArgs e) {`
- `public void Dispose() {`
- `public IPointer? TryGetPointer(RawPointerEventArgs ev) {`

### `src/Avalonia.Base/Input/Navigation/XYFocus.Bubbling.cs`
- Namespace: `Avalonia.Input`
- `public partial class XYFocus`

### `src/Avalonia.Base/Input/Navigation/XYFocus.FindElements.cs`
- Namespace: `Avalonia.Input`
- `public partial class XYFocus`

### `src/Avalonia.Base/Input/Navigation/XYFocus.Impl.cs`
- Namespace: `Avalonia.Input`
- `public partial class XYFocus`

### `src/Avalonia.Base/Input/Navigation/XYFocus.Properties.cs`
- Namespace: `Avalonia.Input`
- `public partial class XYFocus`
- `public static readonly AttachedProperty<InputElement> DownProperty = AvaloniaProperty.RegisterAttached<XYFocus, InputElement, InputElement>("Down");`
- `public static void SetDown(InputElement obj, InputElement value) => obj.SetValue(DownProperty, value);`
- `public static InputElement GetDown(InputElement obj) => obj.GetValue(DownProperty);`
- `public static readonly AttachedProperty<InputElement> LeftProperty = AvaloniaProperty.RegisterAttached<XYFocus, InputElement, InputElement>("Left");`
- `public static void SetLeft(InputElement obj, InputElement value) => obj.SetValue(LeftProperty, value);`
- `public static InputElement GetLeft(InputElement obj) => obj.GetValue(LeftProperty);`
- `public static readonly AttachedProperty<InputElement> RightProperty = AvaloniaProperty.RegisterAttached<XYFocus, InputElement, InputElement>("Right");`
- `public static void SetRight(InputElement obj, InputElement value) =>`
- `public static InputElement GetRight(InputElement obj) => obj.GetValue(RightProperty);`
- `public static readonly AttachedProperty<InputElement> UpProperty = AvaloniaProperty.RegisterAttached<XYFocus, InputElement, InputElement>("Up");`
- `public static void SetUp(InputElement obj, InputElement value) => obj.SetValue(UpProperty, value);`
- `public static InputElement GetUp(InputElement obj) => obj.GetValue(UpProperty);`
- `public static readonly AttachedProperty<XYFocusNavigationStrategy> DownNavigationStrategyProperty = AvaloniaProperty.RegisterAttached<XYFocus, InputElement, XYFocusNavigationStrategy>( "DownNavigationStrategy", inherits: true);`
- `public static void SetDownNavigationStrategy(InputElement obj, XYFocusNavigationStrategy value) =>`
- `public static XYFocusNavigationStrategy GetDownNavigationStrategy(InputElement obj) =>`
- `public static readonly AttachedProperty<XYFocusNavigationStrategy> UpNavigationStrategyProperty = AvaloniaProperty.RegisterAttached<XYFocus, InputElement, XYFocusNavigationStrategy>( "UpNavigationStrategy", inherits: true);`
- `public static void SetUpNavigationStrategy(InputElement obj, XYFocusNavigationStrategy value) =>`
- `public static XYFocusNavigationStrategy GetUpNavigationStrategy(InputElement obj) =>`
- `public static readonly AttachedProperty<XYFocusNavigationStrategy> LeftNavigationStrategyProperty = AvaloniaProperty.RegisterAttached<XYFocus, InputElement, XYFocusNavigationStrategy>( "LeftNavigationStrategy", inherits: true);`
- `public static void SetLeftNavigationStrategy(InputElement obj, XYFocusNavigationStrategy value) =>`
- `public static XYFocusNavigationStrategy GetLeftNavigationStrategy(InputElement obj) =>`
- `public static readonly AttachedProperty<XYFocusNavigationStrategy> RightNavigationStrategyProperty = AvaloniaProperty.RegisterAttached<XYFocus, InputElement, XYFocusNavigationStrategy>( "RightNavigationStrategy", inherits: true);`
- `public static void SetRightNavigationStrategy(InputElement obj, XYFocusNavigationStrategy value) =>`
- `public static XYFocusNavigationStrategy GetRightNavigationStrategy(InputElement obj) =>`
- `public static readonly AttachedProperty<XYFocusNavigationModes> NavigationModesProperty = AvaloniaProperty.RegisterAttached<XYFocus, InputElement, XYFocusNavigationModes>( "NavigationModes", XYFocusNavigationModes.Gamepad | XYFocusNavigationModes.Remote, inherits: true);`
- `public static void SetNavigationModes(InputElement obj, XYFocusNavigationModes value) =>`
- `public static XYFocusNavigationModes GetNavigationModes(InputElement obj) =>`

### `src/Avalonia.Base/Input/Navigation/XYFocusNavigationModes.cs`
- Namespace: `Avalonia.Input`
- `public enum XYFocusNavigationModes`

### `src/Avalonia.Base/Input/Navigation/XYFocusNavigationStrategy.cs`
- `public enum XYFocusNavigationStrategy`

### `src/Avalonia.Base/Input/NavigationDirection.cs`
- `public enum NavigationDirection`
- `public static class NavigationDirectionExtensions`
- `public static bool IsTab(this NavigationDirection direction) {`
- `public static bool IsDirectional(this NavigationDirection direction) {`
- `public static NavigationDirection? ToNavigationDirection( this Key key, KeyModifiers modifiers = KeyModifiers.None) {`

### `src/Avalonia.Base/Input/NavigationMethod.cs`
- `public enum NavigationMethod`

### `src/Avalonia.Base/Input/PenDevice.cs`
- `public class PenDevice : IPenDevice, IDisposable`
- `public PenDevice(bool releasePointerOnPenUp = false) {`
- `public void ProcessRawEvent(RawInputEventArgs e) {`
- `public void Dispose() {`
- `public IPointer? TryGetPointer(RawPointerEventArgs ev) {`

### `src/Avalonia.Base/Input/PhysicalKey.cs`
- Namespace: `Avalonia.Input`
- `public enum PhysicalKey`

### `src/Avalonia.Base/Input/PhysicalKeyExtensions.cs`
- Namespace: `Avalonia.Input`
- `public static class PhysicalKeyExtensions`
- `public static Key ToQwertyKey(this PhysicalKey physicalKey) => physicalKey switch`
- `public static string? ToQwertyKeySymbol(this PhysicalKey physicalKey, bool useShiftModifier = false) => physicalKey switch`

### `src/Avalonia.Base/Input/PinchEventArgs.cs`
- `public class PinchEventArgs : RoutedEventArgs`
- `public PinchEventArgs(double scale, Point scaleOrigin) : base(Gestures.PinchEvent) {`
- `public PinchEventArgs(double scale, Point scaleOrigin, double angle, double angleDelta) : base(Gestures.PinchEvent) {`
- `public double Scale { get; } = 1;`
- `public Point ScaleOrigin { get; }`
- `public double Angle { get; }`
- `public double AngleDelta { get; }`
- `public class PinchEndedEventArgs : RoutedEventArgs`
- `public PinchEndedEventArgs() : base(Gestures.PinchEndedEvent) {`

### `src/Avalonia.Base/Input/Platform/ClipboardExtensions.cs`
- Namespace: `Avalonia.Input.Platform`
- `public static class ClipboardExtensions`
- `public static async Task<IReadOnlyList<DataFormat>> GetDataFormatsAsync(this IClipboard clipboard) {`
- `public static async Task<T?> TryGetValueAsync<T>(this IClipboard clipboard, DataFormat<T> format) where T : class {`
- `public static async Task<T[]?> TryGetValuesAsync<T>(this IClipboard clipboard, DataFormat<T> format) where T : class {`
- `public static Task SetValueAsync<T>(this IClipboard clipboard, DataFormat<T> format, T? value) where T : class {`
- `public static Task SetValuesAsync<T>(this IClipboard clipboard, DataFormat<T> format, IEnumerable<T>? values) where T : class {`
- `public static Task<string?> TryGetTextAsync(this IClipboard clipboard) => clipboard.TryGetValueAsync(DataFormat.Text);`
- `public static Task<IStorageItem?> TryGetFileAsync(this IClipboard clipboard) => clipboard.TryGetValueAsync(DataFormat.File);`
- `public static Task<IStorageItem[]?> TryGetFilesAsync(this IClipboard clipboard) => clipboard.TryGetValuesAsync(DataFormat.File);`
- `public static Task<Bitmap?> TryGetBitmapAsync(this IClipboard clipboard) => clipboard.TryGetValueAsync(DataFormat.Bitmap);`
- `public static Task SetTextAsync(this IClipboard clipboard, string? text) => clipboard.SetValueAsync(DataFormat.Text, text);`
- `public static Task SetFileAsync(this IClipboard clipboard, IStorageItem? file) => clipboard.SetValueAsync(DataFormat.File, file);`
- `public static Task SetFilesAsync(this IClipboard clipboard, IEnumerable<IStorageItem>? files) => clipboard.SetValuesAsync(DataFormat.File, files);`
- `public static Task SetBitmapAsync(this IClipboard clipboard, Bitmap? bitmap) => clipboard.SetValueAsync(DataFormat.Bitmap, bitmap);`

### `src/Avalonia.Base/Input/Platform/IClipboard.cs`
- `public interface IClipboard`

### `src/Avalonia.Base/Input/Platform/IClipboardImpl.cs`
- Namespace: `Avalonia.Input.Platform`
- `public interface IClipboardImpl`

### `src/Avalonia.Base/Input/Platform/IFlushableClipboardImpl.cs`
- Namespace: `Avalonia.Input.Platform`
- `public interface IFlushableClipboardImpl : IClipboardImpl`

### `src/Avalonia.Base/Input/Platform/IOwnedClipboardImpl.cs`
- Namespace: `Avalonia.Input.Platform`
- `public interface IOwnedClipboardImpl : IClipboardImpl`

### `src/Avalonia.Base/Input/Platform/IPlatformDragSource.cs`
- `public interface IPlatformDragSource`

### `src/Avalonia.Base/Input/Platform/KeyGestureFormatInfo.cs`
- `public sealed class KeyGestureFormatInfo(IReadOnlyDictionary<Key, string>? platformKeyOverrides = null,`
- `public static KeyGestureFormatInfo Invariant { get; } = new();`
- `public string Meta { get; } = meta;`
- `public string Ctrl { get; } = ctrl;`
- `public string Alt { get; } = alt;`
- `public string Shift { get; } = shift;`
- `public object? GetFormat(Type? formatType) => formatType == typeof(KeyGestureFormatInfo) ? this : null;`
- `public static KeyGestureFormatInfo GetInstance(IFormatProvider? formatProvider) => formatProvider?.GetFormat(typeof(KeyGestureFormatInfo)) as KeyGestureFormatInfo`
- `public string FormatKey(Key key) {`

### `src/Avalonia.Base/Input/Platform/PlatformHotkeyConfiguration.cs`
- `public sealed class PlatformHotkeyConfiguration`
- `public PlatformHotkeyConfiguration() : this(KeyModifiers.Control) {`
- `public PlatformHotkeyConfiguration(KeyModifiers commandModifiers, KeyModifiers selectionModifiers = KeyModifiers.Shift, KeyModifiers wholeWordTextActionModifiers = KeyModifiers.Control) {`
- `public KeyModifiers CommandModifiers { get; set; }`
- `public KeyModifiers WholeWordTextActionModifiers { get; set; }`
- `public KeyModifiers SelectionModifiers { get; set; }`
- `public List<KeyGesture> Copy { get; set; }`
- `public List<KeyGesture> Cut { get; set; }`
- `public List<KeyGesture> Paste { get; set; }`
- `public List<KeyGesture> Undo { get; set; }`
- `public List<KeyGesture> Redo { get; set; }`
- `public List<KeyGesture> SelectAll { get; set; }`
- `public List<KeyGesture> MoveCursorToTheStartOfLine { get; set; }`
- `public List<KeyGesture> MoveCursorToTheEndOfLine { get; set; }`
- `public List<KeyGesture> MoveCursorToTheStartOfDocument { get; set; }`
- `public List<KeyGesture> MoveCursorToTheEndOfDocument { get; set; }`
- `public List<KeyGesture> MoveCursorToTheStartOfLineWithSelection { get; set; }`
- `public List<KeyGesture> MoveCursorToTheEndOfLineWithSelection { get; set; }`
- `public List<KeyGesture> MoveCursorToTheStartOfDocumentWithSelection { get; set; }`
- `public List<KeyGesture> MoveCursorToTheEndOfDocumentWithSelection { get; set; }`
- `public List<KeyGesture> OpenContextMenu { get; set; }`
- `public List<KeyGesture> Back { get; set; }`
- `public List<KeyGesture> PageUp { get; set; }`
- `public List<KeyGesture> PageDown { get; set; }`
- `public List<KeyGesture> PageRight { get; set; }`
- `public List<KeyGesture> PageLeft { get; set; }`

### `src/Avalonia.Base/Input/Pointer.cs`
- `public class Pointer : IPointer, IDisposable`
- `public static int GetNextFreeId() => s_NextFreePointerId++;`
- `public Pointer(int id, PointerType type, bool isPrimary) {`
- `public int Id { get; }`
- `public void Capture(IInputElement? control) {`
- `public IInputElement? Captured { get; private set; }`
- `public PointerType Type { get; }`
- `public bool IsPrimary { get; }`
- `public bool IsGestureRecognitionSkipped { get; set; }`
- `public void Dispose() {`

### `src/Avalonia.Base/Input/PointerDeltaEventArgs.cs`
- `public class PointerDeltaEventArgs : PointerEventArgs`
- `public Vector Delta { get; }`
- `public PointerDeltaEventArgs(RoutedEvent routedEvent, object? source, IPointer pointer, Visual rootVisual, Point rootVisualPosition, ulong timestamp, PointerPointProperties properties, KeyModifiers modifiers, Vector delta) : base(routedEvent, source, pointer, rootVisual, rootVisualPosition, timestamp, properties, modifiers) {`

### `src/Avalonia.Base/Input/PointerEventArgs.cs`
- `public class PointerEventArgs : RoutedEventArgs`
- `public PointerEventArgs(RoutedEvent routedEvent, object? source, IPointer pointer, Visual? rootVisual, Point rootVisualPosition, ulong timestamp, PointerPointProperties properties, KeyModifiers modifiers) : base(routedEvent) {`
- `public IPointer Pointer { get; }`
- `public ulong Timestamp { get; }`
- `public KeyModifiers KeyModifiers { get; }`
- `public Point GetPosition(Visual? relativeTo) => GetPosition(_rootVisualPosition, relativeTo);`
- `public PointerPoint GetCurrentPoint(Visual? relativeTo) => new PointerPoint(Pointer, GetPosition(relativeTo), _properties);`
- `public IReadOnlyList<PointerPoint> GetIntermediatePoints(Visual? relativeTo) {`
- `public void PreventGestureRecognition() {`
- `public PointerPointProperties Properties => _properties;`
- `public enum MouseButton`
- `public class PointerPressedEventArgs : PointerEventArgs`
- `public PointerPressedEventArgs( object source, IPointer pointer, Visual rootVisual, Point rootVisualPosition, ulong timestamp, PointerPointProperties properties, KeyModifiers modifiers, int clickCount = 1) : base(InputElement.PointerPressedEvent, source, pointer, rootVisual, rootVisualPosition, timestamp, properties, modifiers) {`
- `public int ClickCount { get; }`
- `public class PointerReleasedEventArgs : PointerEventArgs`
- `public PointerReleasedEventArgs( object source, IPointer pointer, Visual rootVisual, Point rootVisualPosition, ulong timestamp, PointerPointProperties properties, KeyModifiers modifiers, MouseButton initialPressMouseButton) : base(InputElement.PointerReleasedEvent, source, pointer, rootVisual, rootVisualPosition, timestamp, properties, modifiers) {`
- `public MouseButton InitialPressMouseButton { get; }`
- `public class PointerCaptureLostEventArgs : RoutedEventArgs`
- `public IPointer Pointer { get; }`
- `public PointerCaptureLostEventArgs(object source, IPointer pointer) : base(InputElement.PointerCaptureLostEvent) {`

### `src/Avalonia.Base/Input/PointerPoint.cs`
- `public record struct PointerPoint`
- `public PointerPoint(IPointer pointer, Point position, PointerPointProperties properties) {`
- `public IPointer Pointer { get; }`
- `public PointerPointProperties Properties { get; }`
- `public Point Position { get; }`
- `public record struct PointerPointProperties`
- `public Rect ContactRect { get; }`
- `public bool IsLeftButtonPressed { get; } = false;`
- `public bool IsMiddleButtonPressed { get; } = false;`
- `public bool IsRightButtonPressed { get; } = false;`
- `public bool IsXButton1Pressed { get; } = false;`
- `public bool IsXButton2Pressed { get; } = false;`
- `public bool IsBarrelButtonPressed { get; } = false;`
- `public bool IsEraser { get; } = false;`
- `public bool IsInverted { get; } = false;`
- `public float Twist { get; } = 0.0F;`
- `public float Pressure { get; } = 0.5f;`
- `public float XTilt { get; } = 0.0F;`
- `public float YTilt { get; } = 0.0F;`
- `public PointerUpdateKind PointerUpdateKind { get; } = PointerUpdateKind.LeftButtonPressed;`
- `public PointerPointProperties() {`
- `public PointerPointProperties(RawInputModifiers modifiers, PointerUpdateKind kind) {`
- `public PointerPointProperties(RawInputModifiers modifiers, PointerUpdateKind kind, float twist, float pressure, float xTilt, float yTilt) : this(modifiers, kind, twist, pressure, xTilt, yTilt, default) {`
- `public PointerPointProperties(RawInputModifiers modifiers, PointerUpdateKind kind, float twist, float pressure, float xTilt, float yTilt, Rect contactRect) : this(modifiers, kind) {`
- `public static PointerPointProperties None { get; } = new PointerPointProperties();`
- `public enum PointerUpdateKind`
- `public static class PointerUpdateKindExtensions`
- `public static MouseButton GetMouseButton(this PointerUpdateKind kind) {`

### `src/Avalonia.Base/Input/PointerWheelEventArgs.cs`
- `public class PointerWheelEventArgs : PointerEventArgs`
- `public Vector Delta { get; }`
- `public PointerWheelEventArgs(object source, IPointer pointer, Visual rootVisual, Point rootVisualPosition, ulong timestamp, PointerPointProperties properties, KeyModifiers modifiers, Vector delta) : base(InputElement.PointerWheelChangedEvent, source, pointer, rootVisual, rootVisualPosition, timestamp, properties, modifiers) {`

### `src/Avalonia.Base/Input/PullGestureEventArgs.cs`
- `public class PullGestureEventArgs : RoutedEventArgs`
- `public int Id { get; }`
- `public Vector Delta { get; }`
- `public PullDirection PullDirection { get; }`
- `public PullGestureEventArgs(int id, Vector delta, PullDirection pullDirection) : base(Gestures.PullGestureEvent) {`
- `public class PullGestureEndedEventArgs : RoutedEventArgs`
- `public int Id { get; }`
- `public PullDirection PullDirection { get; }`
- `public PullGestureEndedEventArgs(int id, PullDirection pullDirection) : base(Gestures.PullGestureEndedEvent) {`
- `public enum PullDirection`

### `src/Avalonia.Base/Input/Raw/IDragDropDevice.cs`
- `public interface IDragDropDevice : IInputDevice`

### `src/Avalonia.Base/Input/Raw/RawDragEvent.cs`
- `public class RawDragEvent : RawInputEventArgs`
- `public Point Location { get; set; }`
- `public IDataTransfer DataTransfer { get; }`
- `public IDataObject Data => _legacyDataObject ??= DataTransfer.ToLegacyDataObject();`
- `public DragDropEffects Effects { get; set; }`
- `public RawDragEventType Type { get; }`
- `public KeyModifiers KeyModifiers { get; }`
- `public RawDragEvent(IDragDropDevice inputDevice, RawDragEventType type, IInputRoot root, Point location, IDataObject data, DragDropEffects effects, RawInputModifiers modifiers) : this(inputDevice, type, root, location, new DataObjectToDataTransferWrapper(data), effects, modifiers) {`
- `public RawDragEvent( IDragDropDevice inputDevice, RawDragEventType type, IInputRoot root, Point location, IDataTransfer dataTransfer, DragDropEffects effects, RawInputModifiers modifiers) : base(inputDevice, 0, root) {`

### `src/Avalonia.Base/Input/Raw/RawDragEventType.cs`
- `public enum RawDragEventType`

### `src/Avalonia.Base/Input/Raw/RawInputEventArgs.cs`
- `public class RawInputEventArgs : EventArgs`
- `public RawInputEventArgs(IInputDevice device, ulong timestamp, IInputRoot root) {`
- `public IInputDevice Device { get; }`
- `public IInputRoot Root { get; }`
- `public bool Handled { get; set; }`
- `public ulong Timestamp { get; set; }`

### `src/Avalonia.Base/Input/Raw/RawKeyEventArgs.cs`
- `public enum RawKeyEventType`
- `public class RawKeyEventArgs : RawInputEventArgs`
- `public RawKeyEventArgs( IKeyboardDevice device, ulong timestamp, IInputRoot root, RawKeyEventType type, Key key, RawInputModifiers modifiers) : this(device, timestamp, root, type, key, modifiers, PhysicalKey.None, KeyDeviceType.Keyboard, null) {`
- `public RawKeyEventArgs( IInputDevice device, ulong timestamp, IInputRoot root, RawKeyEventType type, Key key, RawInputModifiers modifiers, PhysicalKey physicalKey, string? keySymbol) : this(device, timestamp, root, type, key, modifiers, physicalKey, KeyDeviceType.Keyboard, keySymbol) { }`
- `public RawKeyEventArgs( IInputDevice device, ulong timestamp, IInputRoot root, RawKeyEventType type, Key key, RawInputModifiers modifiers, PhysicalKey physicalKey, KeyDeviceType keyDeviceType, string? keySymbol) : base(device, timestamp, root) {`
- `public Key Key { get; set; }`
- `public RawInputModifiers Modifiers { get; set; }`
- `public RawKeyEventType Type { get; set; }`
- `public PhysicalKey PhysicalKey { get; set; }`
- `public KeyDeviceType KeyDeviceType { get; set; }`
- `public string? KeySymbol { get; set; }`

### `src/Avalonia.Base/Input/Raw/RawMouseWheelEventArgs.cs`
- `public class RawMouseWheelEventArgs : RawPointerEventArgs`
- `public RawMouseWheelEventArgs( IInputDevice device, ulong timestamp, IInputRoot root, Point position, Vector delta, RawInputModifiers inputModifiers) : base(device, timestamp, root, RawPointerEventType.Wheel, position, inputModifiers) {`
- `public Vector Delta { get; private set; }`

### `src/Avalonia.Base/Input/Raw/RawPointerEventArgs.cs`
- `public enum RawPointerEventType`
- `public class RawPointerEventArgs : RawInputEventArgs`
- `public RawPointerEventArgs( IInputDevice device, ulong timestamp, IInputRoot root, RawPointerEventType type, Point position, RawInputModifiers inputModifiers) : base(device, timestamp, root) {`
- `public RawPointerEventArgs( IInputDevice device, ulong timestamp, IInputRoot root, RawPointerEventType type, RawPointerPoint point, RawInputModifiers inputModifiers) : base(device, timestamp, root) {`
- `public long RawPointerId { get; set; }`
- `public RawPointerPoint Point {`
- `public Point Position {`
- `public RawPointerEventType Type { get; set; }`
- `public RawInputModifiers InputModifiers { get; set; }`
- `public Lazy<IReadOnlyList<RawPointerPoint>?>? IntermediatePoints { get; set; }`
- `public record struct RawPointerPoint`
- `public Point Position { get; set; }`
- `public float Twist { get; set; }`
- `public float Pressure { get; set; }`
- `public float XTilt { get; set; }`
- `public float YTilt { get; set; }`
- `public Rect ContactRect {`
- `public RawPointerPoint() {`

### `src/Avalonia.Base/Input/Raw/RawPointerGestureEventArgs.cs`
- `public class RawPointerGestureEventArgs : RawPointerEventArgs`
- `public RawPointerGestureEventArgs( IInputDevice device, ulong timestamp, IInputRoot root, RawPointerEventType gestureType, Point position, Vector delta, RawInputModifiers inputModifiers) : base(device, timestamp, root, gestureType, position, inputModifiers) {`
- `public Vector Delta { get; private set; }`

### `src/Avalonia.Base/Input/Raw/RawSizeEventArgs.cs`
- `public class RawSizeEventArgs : EventArgs`
- `public RawSizeEventArgs(Size size) {`
- `public RawSizeEventArgs(double width, double height) {`
- `public Size Size { get; private set; }`

### `src/Avalonia.Base/Input/Raw/RawTextInputEventArgs.cs`
- `public class RawTextInputEventArgs : RawInputEventArgs`
- `public RawTextInputEventArgs( IKeyboardDevice device, ulong timestamp, IInputRoot root, string text) : base(device, timestamp, root) {`
- `public string Text { get; }`

### `src/Avalonia.Base/Input/Raw/RawTouchEventArgs.cs`
- `public class RawTouchEventArgs : RawPointerEventArgs`
- `public RawTouchEventArgs(IInputDevice device, ulong timestamp, IInputRoot root, RawPointerEventType type, Point position, RawInputModifiers inputModifiers, long rawPointerId) : base(device, timestamp, root, type, position, inputModifiers) {`
- `public RawTouchEventArgs(IInputDevice device, ulong timestamp, IInputRoot root, RawPointerEventType type, RawPointerPoint point, RawInputModifiers inputModifiers, long rawPointerId) : base(device, timestamp, root, type, point, inputModifiers) {`

### `src/Avalonia.Base/Input/ScrollGestureEventArgs.cs`
- `public class ScrollGestureEventArgs : RoutedEventArgs`
- `public int Id { get; }`
- `public Vector Delta { get; }`
- `public bool ShouldEndScrollGesture { get; set; }`
- `public static int GetNextFreeId() => _nextId++;`
- `public ScrollGestureEventArgs(int id, Vector delta) : base(Gestures.ScrollGestureEvent) {`
- `public class ScrollGestureEndedEventArgs : RoutedEventArgs`
- `public int Id { get; }`
- `public ScrollGestureEndedEventArgs(int id) : base(Gestures.ScrollGestureEndedEvent) {`
- `public sealed class ScrollGestureInertiaStartingEventArgs : RoutedEventArgs`
- `public int Id { get; }`
- `public Vector Inertia { get; }`

### `src/Avalonia.Base/Input/TappedEventArgs.cs`
- `public class TappedEventArgs : RoutedEventArgs`
- `public TappedEventArgs(RoutedEvent routedEvent, PointerEventArgs lastPointerEventArgs) : base(routedEvent) {`
- `public IPointer Pointer => lastPointerEventArgs.Pointer;`
- `public KeyModifiers KeyModifiers => lastPointerEventArgs.KeyModifiers;`
- `public ulong Timestamp => lastPointerEventArgs.Timestamp;`
- `public Point GetPosition(Visual? relativeTo) => lastPointerEventArgs.GetPosition(relativeTo);`

### `src/Avalonia.Base/Input/TextInput/ITextInputMethodImpl.cs`
- `public interface ITextInputMethodImpl`
- `public interface ITextInputMethodRoot : IInputRoot`

### `src/Avalonia.Base/Input/TextInput/TextInputContentType.cs`
- `public enum TextInputContentType`

### `src/Avalonia.Base/Input/TextInput/TextInputMethodClient.cs`
- `public abstract class TextInputMethodClient`
- `public event EventHandler? TextViewVisualChanged;`
- `public event EventHandler? CursorRectangleChanged;`
- `public event EventHandler? SurroundingTextChanged;`
- `public event EventHandler? SelectionChanged;`
- `public event EventHandler? ResetRequested;`
- `public event EventHandler? InputPaneActivationRequested;`
- `public abstract Visual TextViewVisual { get; }`
- `public abstract bool SupportsPreedit { get; }`
- `public abstract bool SupportsSurroundingText { get; }`
- `public abstract string SurroundingText { get; }`
- `public abstract Rect CursorRectangle { get; }`
- `public abstract TextSelection Selection { get; set; }`
- `public virtual void SetPreeditText(string? preeditText) { }`
- `public virtual void ExecuteContextMenuAction(ContextMenuAction action) { }`
- `public virtual void SetPreeditText(string? preeditText, int? cursorPos) {`
- `public virtual void ShowInputPanel() {`
- `public record struct TextSelection(int Start, int End);`
- `public enum ContextMenuAction`

### `src/Avalonia.Base/Input/TextInput/TextInputMethodClientRequeryRequestedEventArgs.cs`
- Namespace: `Avalonia.Input.TextInput`
- `public class TextInputMethodClientRequeryRequestedEventArgs : RoutedEventArgs`

### `src/Avalonia.Base/Input/TextInput/TextInputMethodClientRequestedEventArgs.cs`
- `public class TextInputMethodClientRequestedEventArgs : RoutedEventArgs`
- `public TextInputMethodClient? Client { get; set; }`

### `src/Avalonia.Base/Input/TextInput/TextInputOptions.cs`
- Namespace: `Avalonia.Input.TextInput`
- `public class TextInputOptions`
- `public static TextInputOptions FromStyledElement(StyledElement avaloniaObject) {`
- `public static readonly TextInputOptions Default = new();`
- `public static readonly AttachedProperty<TextInputContentType> ContentTypeProperty = AvaloniaProperty.RegisterAttached<TextInputOptions, StyledElement, TextInputContentType>( "ContentType", defaultValue: TextInputContentType.Normal, inherits: true);`
- `public static void SetContentType(StyledElement avaloniaObject, TextInputContentType value) {`
- `public static TextInputContentType GetContentType(StyledElement avaloniaObject) {`
- `public TextInputContentType ContentType { get; set; }`
- `public static readonly AttachedProperty<TextInputReturnKeyType> ReturnKeyTypeProperty = AvaloniaProperty.RegisterAttached<TextInputOptions, StyledElement, TextInputReturnKeyType>( "ReturnKeyType", defaultValue: TextInputReturnKeyType.Default, inherits: true);`
- `public static void SetReturnKeyType(StyledElement avaloniaObject, TextInputReturnKeyType value) {`
- `public static TextInputReturnKeyType GetReturnKeyType(StyledElement avaloniaObject) {`
- `public TextInputReturnKeyType ReturnKeyType { get; set; }`
- `public static readonly AttachedProperty<bool> MultilineProperty = AvaloniaProperty.RegisterAttached<TextInputOptions, StyledElement, bool>( "Multiline", inherits: true);`
- `public static void SetMultiline(StyledElement avaloniaObject, bool value) {`
- `public static bool GetMultiline(StyledElement avaloniaObject) {`
- `public bool Multiline { get; set; }`
- `public static readonly AttachedProperty<bool> LowercaseProperty = AvaloniaProperty.RegisterAttached<TextInputOptions, StyledElement, bool>( "Lowercase", inherits: true);`
- `public static void SetLowercase(StyledElement avaloniaObject, bool value) {`
- `public static bool GetLowercase(StyledElement avaloniaObject) {`
- `public bool Lowercase { get; set; }`
- `public static readonly AttachedProperty<bool> UppercaseProperty = AvaloniaProperty.RegisterAttached<TextInputOptions, StyledElement, bool>( "Uppercase", inherits: true);`
- `public static void SetUppercase(StyledElement avaloniaObject, bool value) {`
- `public static bool GetUppercase(StyledElement avaloniaObject) {`
- `public bool Uppercase { get; set; }`
- `public static readonly AttachedProperty<bool> AutoCapitalizationProperty = AvaloniaProperty.RegisterAttached<TextInputOptions, StyledElement, bool>( "AutoCapitalization", inherits: true);`
- `public static void SetAutoCapitalization(StyledElement avaloniaObject, bool value) {`
- `public static bool GetAutoCapitalization(StyledElement avaloniaObject) {`
- `public bool AutoCapitalization { get; set; }`
- `public static readonly AttachedProperty<bool> IsSensitiveProperty = AvaloniaProperty.RegisterAttached<TextInputOptions, StyledElement, bool>( "IsSensitive", inherits: true);`
- `public static void SetIsSensitive(StyledElement avaloniaObject, bool value) {`
- `public static bool GetIsSensitive(StyledElement avaloniaObject) {`
- `public bool IsSensitive { get; set; }`
- `public static readonly AttachedProperty<bool?> ShowSuggestionsProperty = AvaloniaProperty.RegisterAttached<TextInputOptions, StyledElement, bool?>( "ShowSuggestions", inherits: true);`
- `public static void SetShowSuggestions(StyledElement avaloniaObject, bool? value) {`
- `public static bool? GetShowSuggestions(StyledElement avaloniaObject) {`
- `public bool? ShowSuggestions { get; set; }`

### `src/Avalonia.Base/Input/TextInput/TextInputReturnKeyType.cs`
- Namespace: `Avalonia.Input.TextInput`
- `public enum TextInputReturnKeyType`

### `src/Avalonia.Base/Input/TextInputEventArgs.cs`
- `public class TextInputEventArgs : RoutedEventArgs`
- `public string? Text { get; set; }`

### `src/Avalonia.Base/Input/TouchDevice.cs`
- `public class TouchDevice : IPointerDevice, IDisposable`
- `public void ProcessRawEvent(RawInputEventArgs ev) {`
- `public void Dispose() {`
- `public IPointer? TryGetPointer(RawPointerEventArgs ev) {`

### `src/Avalonia.Base/Input/VectorEventArgs.cs`
- `public class VectorEventArgs : RoutedEventArgs`
- `public Vector Vector { get; init; }`

### `src/Avalonia.Base/Interactivity/CancelRoutedEventArgs.cs`
- `public class CancelRoutedEventArgs : RoutedEventArgs`
- `public CancelRoutedEventArgs() {`
- `public CancelRoutedEventArgs(RoutedEvent? routedEvent) : base(routedEvent) {`
- `public CancelRoutedEventArgs(RoutedEvent? routedEvent, object? source) : base(routedEvent, source) {`
- `public bool Cancel { get; set; } = false;`

### `src/Avalonia.Base/Interactivity/EventRoute.cs`
- `public class EventRoute : IDisposable`
- `public EventRoute(RoutedEvent e) {`
- `public bool HasHandlers => _route?.Count > 0;`
- `public void Add( Interactive target, Delegate handler, RoutingStrategies routes, bool handledEventsToo = false, Action<Delegate, object, RoutedEventArgs>? adapter = null) {`
- `public void AddClassHandler(Interactive target) {`
- `public void RaiseEvent(Interactive source, RoutedEventArgs e) {`
- `public void Dispose() {`

### `src/Avalonia.Base/Interactivity/Interactive.cs`
- `public class Interactive : Layoutable`
- `public void AddHandler( RoutedEvent routedEvent, Delegate handler, RoutingStrategies routes = RoutingStrategies.Direct | RoutingStrategies.Bubble, bool handledEventsToo = false) {`
- `public void AddHandler<TEventArgs>( RoutedEvent<TEventArgs> routedEvent, EventHandler<TEventArgs>? handler, RoutingStrategies routes = RoutingStrategies.Direct | RoutingStrategies.Bubble, bool handledEventsToo = false) where TEventArgs : RoutedEventArgs {`
- `public void RemoveHandler(RoutedEvent routedEvent, Delegate handler) {`
- `public void RemoveHandler<TEventArgs>(RoutedEvent<TEventArgs> routedEvent, EventHandler<TEventArgs>? handler) where TEventArgs : RoutedEventArgs {`
- `public void RaiseEvent(RoutedEventArgs e) {`

### `src/Avalonia.Base/Interactivity/InteractiveExtensions.cs`
- `public static class InteractiveExtensions`
- `public static IDisposable AddDisposableHandler<TEventArgs>(this Interactive o, RoutedEvent<TEventArgs> routedEvent, EventHandler<TEventArgs> handler, RoutingStrategies routes = RoutingStrategies.Direct | RoutingStrategies.Bubble, bool handledEventsToo = false) where TEventArgs : RoutedEventArgs {`
- `public static Interactive? GetInteractiveParent(this Interactive o) => o.InteractiveParent;`
- `public static IObservable<TEventArgs> GetObservable<TEventArgs>( this Interactive o, RoutedEvent<TEventArgs> routedEvent, RoutingStrategies routes = RoutingStrategies.Direct | RoutingStrategies.Bubble, bool handledEventsToo = false) where TEventArgs : RoutedEventArgs {`

### `src/Avalonia.Base/Interactivity/RoutedEvent.cs`
- `public enum RoutingStrategies`
- `public class RoutedEvent`
- `public RoutedEvent( string name, RoutingStrategies routingStrategies, Type eventArgsType, Type ownerType) {`
- `public Type EventArgsType { get; }`
- `public string Name { get; }`
- `public Type OwnerType { get; }`
- `public RoutingStrategies RoutingStrategies { get; }`
- `public bool HasRaisedSubscriptions => _raised.HasObservers;`
- `public IObservable<(object, RoutedEventArgs)> Raised => _raised;`
- `public IObservable<RoutedEventArgs> RouteFinished => _routeFinished;`
- `public static RoutedEvent<TEventArgs> Register<TOwner, TEventArgs>( string name, RoutingStrategies routingStrategy) where TEventArgs : RoutedEventArgs {`
- `public static RoutedEvent<TEventArgs> Register<TEventArgs>( string name, RoutingStrategies routingStrategy, Type ownerType) where TEventArgs : RoutedEventArgs {`
- `public IDisposable AddClassHandler( Type targetType, EventHandler<RoutedEventArgs> handler, RoutingStrategies routes = RoutingStrategies.Direct | RoutingStrategies.Bubble, bool handledEventsToo = false) {`
- `public override string ToString() {`
- `public class RoutedEvent<TEventArgs> : RoutedEvent`
- `public RoutedEvent(string name, RoutingStrategies routingStrategies, Type ownerType) : base(name, routingStrategies, typeof(TEventArgs), ownerType) {`
- `public IDisposable AddClassHandler<TTarget>( Action<TTarget, TEventArgs> handler, RoutingStrategies routes = RoutingStrategies.Direct | RoutingStrategies.Bubble, bool handledEventsToo = false) where TTarget : Interactive {`

### `src/Avalonia.Base/Interactivity/RoutedEventArgs.cs`
- `public class RoutedEventArgs : EventArgs`
- `public RoutedEventArgs() {`
- `public RoutedEventArgs(RoutedEvent? routedEvent) {`
- `public RoutedEventArgs(RoutedEvent? routedEvent, object? source) {`
- `public bool Handled { get; set; }`
- `public RoutedEvent? RoutedEvent { get; set; }`
- `public RoutingStrategies Route { get; set; }`
- `public object? Source { get; set; }`

### `src/Avalonia.Base/Interactivity/RoutedEventRegistry.cs`
- `public class RoutedEventRegistry`
- `public static RoutedEventRegistry Instance { get; }`
- `public void Register(Type type, RoutedEvent @event) {`
- `public IEnumerable<RoutedEvent> GetAllRegistered() {`
- `public IReadOnlyList<RoutedEvent> GetRegistered(Type type) {`
- `public IReadOnlyList<RoutedEvent> GetRegistered<TOwner>() {`

### `src/Avalonia.Base/Layout/EffectiveViewportChangedEventArgs.cs`
- `public class EffectiveViewportChangedEventArgs : EventArgs`
- `public EffectiveViewportChangedEventArgs(Rect effectiveViewport) {`
- `public Rect EffectiveViewport { get; }`

### `src/Avalonia.Base/Layout/IEmbeddedLayoutRoot.cs`
- `public interface IEmbeddedLayoutRoot : ILayoutRoot`

### `src/Avalonia.Base/Layout/ILayoutManager.cs`
- `public interface ILayoutManager : IDisposable`

### `src/Avalonia.Base/Layout/ILayoutRoot.cs`
- `public interface ILayoutRoot`

### `src/Avalonia.Base/Layout/LayoutExtensions.cs`
- `public static class LayoutExtensions`
- `public static Rect Align( this Rect rect, Rect constraint, HorizontalAlignment horizontalAlignment, VerticalAlignment verticalAlignment) {`

### `src/Avalonia.Base/Layout/LayoutHelper.cs`
- `public static class LayoutHelper`
- `public static double LayoutEpsilon { get; } = 0.00000153;`
- `public static Size ApplyLayoutConstraints(Layoutable control, Size constraints) => ApplyLayoutConstraints(new MinMax(control), constraints);`
- `public static Size MeasureChild(Layoutable? control, Size availableSize, Thickness padding, Thickness borderThickness) {`
- `public static Size MeasureChild(Layoutable? control, Size availableSize, Thickness padding) {`
- `public static Size ArrangeChild(Layoutable? child, Size availableSize, Thickness padding, Thickness borderThickness) {`
- `public static Size ArrangeChild(Layoutable? child, Size availableSize, Thickness padding) {`
- `public static void InvalidateSelfAndChildrenMeasure(Layoutable control) {`
- `public static double GetLayoutScale(Layoutable control) => control.VisualRoot is ILayoutRoot layoutRoot ? layoutRoot.LayoutScaling : 1.0;`
- `public static Size RoundLayoutSizeUp(Size size, double dpiScaleX, double dpiScaleY) {`
- `public static Thickness RoundLayoutThickness(Thickness thickness, double dpiScaleX, double dpiScaleY) {`
- `public static double RoundLayoutValue(double value, double dpiScale) {`
- `public static double RoundLayoutValueUp(double value, double dpiScale) {`

### `src/Avalonia.Base/Layout/LayoutInformation.cs`
- Namespace: `Avalonia.Layout`
- `public static class LayoutInformation`
- `public static Size? GetPreviousMeasureConstraint(Layoutable control) {`
- `public static Rect? GetPreviousArrangeBounds(Layoutable control) {`

### `src/Avalonia.Base/Layout/LayoutManager.cs`
- `public class LayoutManager : ILayoutManager, IDisposable`
- `public LayoutManager(ILayoutRoot owner) {`
- `public virtual event EventHandler? LayoutUpdated;`
- `public virtual void InvalidateMeasure(Layoutable control) {`
- `public virtual void InvalidateArrange(Layoutable control) {`
- `public virtual void ExecuteLayoutPass() {`
- `public virtual void ExecuteInitialLayoutPass() {`
- `public void Dispose() {`

### `src/Avalonia.Base/Layout/Layoutable.cs`
- `public enum HorizontalAlignment`
- `public enum VerticalAlignment`
- `public class Layoutable : Visual`
- `public static readonly DirectProperty<Layoutable, Size> DesiredSizeProperty = AvaloniaProperty.RegisterDirect<Layoutable, Size>(nameof(DesiredSize), o => o.DesiredSize);`
- `public static readonly StyledProperty<double> WidthProperty = AvaloniaProperty.Register<Layoutable, double>(nameof(Width), double.NaN, validate: ValidateDimension);`
- `public static readonly StyledProperty<double> HeightProperty = AvaloniaProperty.Register<Layoutable, double>(nameof(Height), double.NaN, validate: ValidateDimension);`
- `public static readonly StyledProperty<double> MinWidthProperty = AvaloniaProperty.Register<Layoutable, double>(nameof(MinWidth), validate: ValidateMinimumDimension);`
- `public static readonly StyledProperty<double> MaxWidthProperty = AvaloniaProperty.Register<Layoutable, double>(nameof(MaxWidth), double.PositiveInfinity, validate: ValidateMaximumDimension);`
- `public static readonly StyledProperty<double> MinHeightProperty = AvaloniaProperty.Register<Layoutable, double>(nameof(MinHeight), validate: ValidateMinimumDimension);`
- `public static readonly StyledProperty<double> MaxHeightProperty = AvaloniaProperty.Register<Layoutable, double>(nameof(MaxHeight), double.PositiveInfinity, validate: ValidateMaximumDimension);`
- `public static readonly StyledProperty<Thickness> MarginProperty = AvaloniaProperty.Register<Layoutable, Thickness>(nameof(Margin));`
- `public static readonly StyledProperty<HorizontalAlignment> HorizontalAlignmentProperty = AvaloniaProperty.Register<Layoutable, HorizontalAlignment>(nameof(HorizontalAlignment));`
- `public static readonly StyledProperty<VerticalAlignment> VerticalAlignmentProperty = AvaloniaProperty.Register<Layoutable, VerticalAlignment>(nameof(VerticalAlignment));`
- `public static readonly StyledProperty<bool> UseLayoutRoundingProperty = AvaloniaProperty.Register<Layoutable, bool>(nameof(UseLayoutRounding), defaultValue: true, inherits: true);`
- `public event EventHandler<EffectiveViewportChangedEventArgs>? EffectiveViewportChanged {`
- `public event EventHandler? LayoutUpdated {`
- `public void UpdateLayout() => (this.GetVisualRoot() as ILayoutRoot)?.LayoutManager?.ExecuteLayoutPass();`
- `public double Width {`
- `public double Height {`
- `public double MinWidth {`
- `public double MaxWidth {`
- `public double MinHeight {`
- `public double MaxHeight {`
- `public Thickness Margin {`
- `public HorizontalAlignment HorizontalAlignment {`
- `public VerticalAlignment VerticalAlignment {`
- `public Size DesiredSize {`
- `public bool IsMeasureValid {`
- `public bool IsArrangeValid {`
- `public bool UseLayoutRounding {`
- `public virtual void ApplyTemplate() {`
- `public void Measure(Size availableSize) {`
- `public void Arrange(Rect rect) {`
- `public void InvalidateMeasure() {`
- `public void InvalidateArrange() {`

### `src/Avalonia.Base/Layout/Orientation.cs`
- `public enum Orientation`

### `src/Avalonia.Base/Logging/ILogSink.cs`
- `public interface ILogSink`

### `src/Avalonia.Base/Logging/LogArea.cs`
- `public static class LogArea`
- `public const string Property = nameof(Property);`
- `public const string Binding = nameof(Binding);`
- `public const string Animations = nameof(Animations);`
- `public const string Visual = nameof(Visual);`
- `public const string Layout = nameof(Layout);`
- `public const string Control = nameof(Control);`
- `public const string Platform = nameof(Platform);`
- `public const string Win32Platform = nameof(Win32Platform);`
- `public const string X11Platform = nameof(X11Platform);`
- `public const string AndroidPlatform = nameof(AndroidPlatform);`
- `public const string IOSPlatform = nameof(IOSPlatform);`
- `public const string LinuxFramebufferPlatform = nameof(LinuxFramebufferPlatform);`
- `public const string FreeDesktopPlatform = nameof(FreeDesktopPlatform);`
- `public const string macOSPlatform = nameof(macOSPlatform);`
- `public const string BrowserPlatform = nameof(BrowserPlatform);`
- `public const string VncPlatform = nameof(VncPlatform);`

### `src/Avalonia.Base/Logging/LogEventLevel.cs`
- `public enum LogEventLevel`

### `src/Avalonia.Base/Logging/Logger.cs`
- `public static class Logger`
- `public static ILogSink? Sink { get; set; }`
- `public static bool IsEnabled(LogEventLevel level, string area) {`
- `public static ParametrizedLogger? TryGet(LogEventLevel level, string area) {`
- `public static bool TryGet(LogEventLevel level, string area, out ParametrizedLogger outLogger) {`

### `src/Avalonia.Base/Logging/ParametrizedLogger.cs`
- `public readonly record struct ParametrizedLogger`
- `public ParametrizedLogger(ILogSink sink, LogEventLevel level, string area) {`
- `public bool IsValid => _sink != null;`
- `public void Log( object? source, string messageTemplate) {`
- `public void Log<T0>( object? source, string messageTemplate, T0 propertyValue0) {`
- `public void Log<T0, T1>( object? source, string messageTemplate, T0 propertyValue0, T1 propertyValue1) {`
- `public void Log<T0, T1, T2>( object? source, string messageTemplate, T0 propertyValue0, T1 propertyValue1, T2 propertyValue2) {`
- `public void Log<T0, T1, T2, T3>( object? source, string messageTemplate, T0 propertyValue0, T1 propertyValue1, T2 propertyValue2, T3 propertyValue3) {`
- `public void Log<T0, T1, T2, T3, T4>( object? source, string messageTemplate, T0 propertyValue0, T1 propertyValue1, T2 propertyValue2, T3 propertyValue3, T4 propertyValue4) {`
- `public void Log<T0, T1, T2, T3, T4, T5>( object? source, string messageTemplate, T0 propertyValue0, T1 propertyValue1, T2 propertyValue2, T3 propertyValue3, T4 propertyValue4, T5 propertyValue5) {`

### `src/Avalonia.Base/LogicalTree/ChildIndexChangedEventArgs.cs`
- `public enum ChildIndexChangedAction`
- `public class ChildIndexChangedEventArgs : EventArgs`
- `public ChildIndexChangedEventArgs(ILogical child, int index) {`
- `public ChildIndexChangedAction Action { get; }`
- `public ILogical? Child { get; }`
- `public int Index { get; }`
- `public static ChildIndexChangedEventArgs ChildIndexesReset { get; } = new(ChildIndexChangedAction.ChildIndexesReset);`
- `public static ChildIndexChangedEventArgs TotalCountChanged { get; } = new(ChildIndexChangedAction.TotalCountChanged);`

### `src/Avalonia.Base/LogicalTree/ControlLocator.cs`
- `public static class ControlLocator`
- `public static IObservable<ILogical?> Track(ILogical relativeTo, int ancestorLevel, Type? ancestorType = null) {`

### `src/Avalonia.Base/LogicalTree/IChildIndexProvider.cs`
- `public interface IChildIndexProvider`

### `src/Avalonia.Base/LogicalTree/ILogical.cs`
- `public interface ILogical`

### `src/Avalonia.Base/LogicalTree/ILogicalRoot.cs`
- `public interface ILogicalRoot : ILogical`

### `src/Avalonia.Base/LogicalTree/LogicalExtensions.cs`
- `public static class LogicalExtensions`
- `public static IEnumerable<ILogical> GetLogicalAncestors(this ILogical logical) {`
- `public static IEnumerable<ILogical> GetSelfAndLogicalAncestors(this ILogical logical) {`
- `public static T? FindLogicalAncestorOfType<T>(this ILogical? logical, bool includeSelf = false) where T : class {`
- `public static IEnumerable<ILogical> GetLogicalChildren(this ILogical logical) {`
- `public static IEnumerable<ILogical> GetLogicalDescendants(this ILogical logical) {`
- `public static IEnumerable<ILogical> GetSelfAndLogicalDescendants(this ILogical logical) {`
- `public static T? FindLogicalDescendantOfType<T>(this ILogical? logical, bool includeSelf = false) where T : class {`
- `public static ILogical? GetLogicalParent(this ILogical logical) {`
- `public static T? GetLogicalParent<T>(this ILogical logical) where T : class {`
- `public static IEnumerable<ILogical> GetLogicalSiblings(this ILogical logical) {`
- `public static bool IsLogicalAncestorOf(this ILogical? logical, ILogical? target) {`

### `src/Avalonia.Base/LogicalTree/LogicalTreeAttachmentEventArgs.cs`
- `public class LogicalTreeAttachmentEventArgs : EventArgs`
- `public LogicalTreeAttachmentEventArgs( ILogicalRoot root, ILogical source, ILogical? parent) {`
- `public ILogicalRoot Root { get; }`
- `public ILogical Source { get; }`
- `public ILogical? Parent { get; }`

### `src/Avalonia.Base/Matrix.cs`
- `public record struct Decomposed`
- `public Vector Translate;`
- `public Vector Scale;`
- `public Vector Skew;`
- `public double Angle;`

### `src/Avalonia.Base/Media/AcrylicBackgroundSource.cs`
- `public enum AcrylicBackgroundSource`

### `src/Avalonia.Base/Media/AlignmentX.cs`
- `public enum AlignmentX`

### `src/Avalonia.Base/Media/AlignmentY.cs`
- `public enum AlignmentY`

### `src/Avalonia.Base/Media/ArcSegment.cs`
- `public sealed class ArcSegment : PathSegment`
- `public static readonly StyledProperty<bool> IsLargeArcProperty = AvaloniaProperty.Register<ArcSegment, bool>(nameof(IsLargeArc), false);`
- `public static readonly StyledProperty<Point> PointProperty = AvaloniaProperty.Register<ArcSegment, Point>(nameof(Point));`
- `public static readonly StyledProperty<double> RotationAngleProperty = AvaloniaProperty.Register<ArcSegment, double>(nameof(RotationAngle), 0);`
- `public static readonly StyledProperty<Size> SizeProperty = AvaloniaProperty.Register<ArcSegment, Size>(nameof(Size));`
- `public static readonly StyledProperty<SweepDirection> SweepDirectionProperty = AvaloniaProperty.Register<ArcSegment, SweepDirection>(nameof(SweepDirection), SweepDirection.Clockwise);`
- `public bool IsLargeArc {`
- `public Point Point {`
- `public double RotationAngle {`
- `public Size Size {`
- `public SweepDirection SweepDirection {`
- `public override string ToString() => FormattableString.Invariant($"A {Size} {RotationAngle} {(IsLargeArc ? 1 : 0)} {(int)SweepDirection} {Point}");`

### `src/Avalonia.Base/Media/BackgroundSizing.cs`
- `public enum BackgroundSizing`

### `src/Avalonia.Base/Media/BaselineAlignment.cs`
- `public enum BaselineAlignment`

### `src/Avalonia.Base/Media/BezierSegment .cs`
- `public sealed class BezierSegment : PathSegment`
- `public static readonly StyledProperty<Point> Point1Property = AvaloniaProperty.Register<BezierSegment, Point>(nameof(Point1));`
- `public static readonly StyledProperty<Point> Point2Property = AvaloniaProperty.Register<BezierSegment, Point>(nameof(Point2));`
- `public static readonly StyledProperty<Point> Point3Property = AvaloniaProperty.Register<BezierSegment, Point>(nameof(Point3));`
- `public Point Point1 {`
- `public Point Point2 {`
- `public Point Point3 {`
- `public override string ToString() => FormattableString.Invariant($"C {Point1} {Point2} {Point3}");`

### `src/Avalonia.Base/Media/BoxShadow.cs`
- `public struct BoxShadow`
- `public double OffsetX { get; set; }`
- `public double OffsetY { get; set; }`
- `public double Blur { get; set; }`
- `public double Spread { get; set; }`
- `public Color Color { get; set; }`
- `public bool IsInset { get; set; }`
- `public bool Equals(in BoxShadow other) {`
- `public override bool Equals(object? obj) {`
- `public override int GetHashCode() {`
- `public override string ToString() {`
- `public static unsafe BoxShadow Parse(string s) {`
- `public Rect TransformBounds(in Rect rect) => IsInset ? rect : rect.Translate(new Vector(OffsetX, OffsetY)).Inflate(Spread + Blur);`
- `public static bool operator ==(BoxShadow left, BoxShadow right) =>`
- `public static bool operator !=(BoxShadow left, BoxShadow right) =>`

### `src/Avalonia.Base/Media/BoxShadows.cs`
- `public struct BoxShadows`
- `public int Count { get; }`
- `public BoxShadows(BoxShadow shadow) {`
- `public BoxShadows(BoxShadow first, BoxShadow[] rest) {`
- `public BoxShadow this[int index] {`
- `public override string ToString() {`
- `public struct BoxShadowsEnumerator`
- `public BoxShadowsEnumerator(BoxShadows shadows) {`
- `public BoxShadow Current => _shadows[_index];`
- `public bool MoveNext() {`
- `public BoxShadowsEnumerator GetEnumerator() => new BoxShadowsEnumerator(this);`
- `public static BoxShadows Parse(string s) {`
- `public Rect TransformBounds(in Rect rect) {`
- `public bool HasInsetShadows {`
- `public bool Equals(BoxShadows other) {`
- `public override bool Equals(object? obj) {`
- `public override int GetHashCode() {`
- `public static bool operator ==(BoxShadows left, BoxShadows right) =>`
- `public static bool operator !=(BoxShadows left, BoxShadows right) =>`

### `src/Avalonia.Base/Media/Brush.cs`
- `public abstract class Brush : Animatable, IBrush, ICompositionRenderResource<IBrush>, ICompositorSerializable`
- `public static readonly StyledProperty<double> OpacityProperty = AvaloniaProperty.Register<Brush, double>(nameof(Opacity), 1.0);`
- `public static readonly StyledProperty<ITransform?> TransformProperty = AvaloniaProperty.Register<Brush, ITransform?>(nameof(Transform));`
- `public static readonly StyledProperty<RelativePoint> TransformOriginProperty = AvaloniaProperty.Register<Brush, RelativePoint>(nameof(TransformOrigin));`
- `public double Opacity {`
- `public ITransform? Transform {`
- `public RelativePoint TransformOrigin {`
- `public static IBrush Parse(string s) {`

### `src/Avalonia.Base/Media/BrushConverter.cs`
- `public class BrushConverter : TypeConverter`
- `public override bool CanConvertFrom(ITypeDescriptorContext? context, Type sourceType) {`
- `public override object? ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object? value) {`

### `src/Avalonia.Base/Media/BrushExtensions.cs`
- `public static class BrushExtensions`
- `public static IImmutableBrush ToImmutable(this IBrush brush) {`
- `public static ImmutableDashStyle ToImmutable(this IDashStyle style) {`
- `public static ImmutablePen ToImmutable(this IPen pen) {`

### `src/Avalonia.Base/Media/BrushMappingMode.cs`
- `public enum BrushMappingMode`

### `src/Avalonia.Base/Media/Brushes.cs`
- `public static class Brushes`
- `public static IImmutableSolidColorBrush AliceBlue => KnownColor.AliceBlue.ToBrush();`
- `public static IImmutableSolidColorBrush AntiqueWhite => KnownColor.AntiqueWhite.ToBrush();`
- `public static IImmutableSolidColorBrush Aqua => KnownColor.Aqua.ToBrush();`
- `public static IImmutableSolidColorBrush Aquamarine => KnownColor.Aquamarine.ToBrush();`
- `public static IImmutableSolidColorBrush Azure => KnownColor.Azure.ToBrush();`
- `public static IImmutableSolidColorBrush Beige => KnownColor.Beige.ToBrush();`
- `public static IImmutableSolidColorBrush Bisque => KnownColor.Bisque.ToBrush();`
- `public static IImmutableSolidColorBrush Black => KnownColor.Black.ToBrush();`
- `public static IImmutableSolidColorBrush BlanchedAlmond => KnownColor.BlanchedAlmond.ToBrush();`
- `public static IImmutableSolidColorBrush Blue => KnownColor.Blue.ToBrush();`
- `public static IImmutableSolidColorBrush BlueViolet => KnownColor.BlueViolet.ToBrush();`
- `public static IImmutableSolidColorBrush Brown => KnownColor.Brown.ToBrush();`
- `public static IImmutableSolidColorBrush BurlyWood => KnownColor.BurlyWood.ToBrush();`
- `public static IImmutableSolidColorBrush CadetBlue => KnownColor.CadetBlue.ToBrush();`
- `public static IImmutableSolidColorBrush Chartreuse => KnownColor.Chartreuse.ToBrush();`
- `public static IImmutableSolidColorBrush Chocolate => KnownColor.Chocolate.ToBrush();`
- `public static IImmutableSolidColorBrush Coral => KnownColor.Coral.ToBrush();`
- `public static IImmutableSolidColorBrush CornflowerBlue => KnownColor.CornflowerBlue.ToBrush();`
- `public static IImmutableSolidColorBrush Cornsilk => KnownColor.Cornsilk.ToBrush();`
- `public static IImmutableSolidColorBrush Crimson => KnownColor.Crimson.ToBrush();`
- `public static IImmutableSolidColorBrush Cyan => KnownColor.Cyan.ToBrush();`
- `public static IImmutableSolidColorBrush DarkBlue => KnownColor.DarkBlue.ToBrush();`
- `public static IImmutableSolidColorBrush DarkCyan => KnownColor.DarkCyan.ToBrush();`
- `public static IImmutableSolidColorBrush DarkGoldenrod => KnownColor.DarkGoldenrod.ToBrush();`
- `public static IImmutableSolidColorBrush DarkGray => KnownColor.DarkGray.ToBrush();`
- `public static IImmutableSolidColorBrush DarkGreen => KnownColor.DarkGreen.ToBrush();`
- `public static IImmutableSolidColorBrush DarkKhaki => KnownColor.DarkKhaki.ToBrush();`
- `public static IImmutableSolidColorBrush DarkMagenta => KnownColor.DarkMagenta.ToBrush();`
- `public static IImmutableSolidColorBrush DarkOliveGreen => KnownColor.DarkOliveGreen.ToBrush();`
- `public static IImmutableSolidColorBrush DarkOrange => KnownColor.DarkOrange.ToBrush();`
- `public static IImmutableSolidColorBrush DarkOrchid => KnownColor.DarkOrchid.ToBrush();`
- `public static IImmutableSolidColorBrush DarkRed => KnownColor.DarkRed.ToBrush();`
- `public static IImmutableSolidColorBrush DarkSalmon => KnownColor.DarkSalmon.ToBrush();`
- `public static IImmutableSolidColorBrush DarkSeaGreen => KnownColor.DarkSeaGreen.ToBrush();`
- `public static IImmutableSolidColorBrush DarkSlateBlue => KnownColor.DarkSlateBlue.ToBrush();`
- `public static IImmutableSolidColorBrush DarkSlateGray => KnownColor.DarkSlateGray.ToBrush();`
- `public static IImmutableSolidColorBrush DarkTurquoise => KnownColor.DarkTurquoise.ToBrush();`
- `public static IImmutableSolidColorBrush DarkViolet => KnownColor.DarkViolet.ToBrush();`
- `public static IImmutableSolidColorBrush DeepPink => KnownColor.DeepPink.ToBrush();`
- `public static IImmutableSolidColorBrush DeepSkyBlue => KnownColor.DeepSkyBlue.ToBrush();`
- `public static IImmutableSolidColorBrush DimGray => KnownColor.DimGray.ToBrush();`
- `public static IImmutableSolidColorBrush DodgerBlue => KnownColor.DodgerBlue.ToBrush();`
- `public static IImmutableSolidColorBrush Firebrick => KnownColor.Firebrick.ToBrush();`
- `public static IImmutableSolidColorBrush FloralWhite => KnownColor.FloralWhite.ToBrush();`
- `public static IImmutableSolidColorBrush ForestGreen => KnownColor.ForestGreen.ToBrush();`
- `public static IImmutableSolidColorBrush Fuchsia => KnownColor.Fuchsia.ToBrush();`
- `public static IImmutableSolidColorBrush Gainsboro => KnownColor.Gainsboro.ToBrush();`
- `public static IImmutableSolidColorBrush GhostWhite => KnownColor.GhostWhite.ToBrush();`
- `public static IImmutableSolidColorBrush Gold => KnownColor.Gold.ToBrush();`
- `public static IImmutableSolidColorBrush Goldenrod => KnownColor.Goldenrod.ToBrush();`
- `public static IImmutableSolidColorBrush Gray => KnownColor.Gray.ToBrush();`
- `public static IImmutableSolidColorBrush Green => KnownColor.Green.ToBrush();`
- `public static IImmutableSolidColorBrush GreenYellow => KnownColor.GreenYellow.ToBrush();`
- `public static IImmutableSolidColorBrush Honeydew => KnownColor.Honeydew.ToBrush();`
- `public static IImmutableSolidColorBrush HotPink => KnownColor.HotPink.ToBrush();`
- `public static IImmutableSolidColorBrush IndianRed => KnownColor.IndianRed.ToBrush();`
- `public static IImmutableSolidColorBrush Indigo => KnownColor.Indigo.ToBrush();`
- `public static IImmutableSolidColorBrush Ivory => KnownColor.Ivory.ToBrush();`
- `public static IImmutableSolidColorBrush Khaki => KnownColor.Khaki.ToBrush();`
- `public static IImmutableSolidColorBrush Lavender => KnownColor.Lavender.ToBrush();`
- `public static IImmutableSolidColorBrush LavenderBlush => KnownColor.LavenderBlush.ToBrush();`
- `public static IImmutableSolidColorBrush LawnGreen => KnownColor.LawnGreen.ToBrush();`
- `public static IImmutableSolidColorBrush LemonChiffon => KnownColor.LemonChiffon.ToBrush();`
- `public static IImmutableSolidColorBrush LightBlue => KnownColor.LightBlue.ToBrush();`
- `public static IImmutableSolidColorBrush LightCoral => KnownColor.LightCoral.ToBrush();`
- `public static IImmutableSolidColorBrush LightCyan => KnownColor.LightCyan.ToBrush();`
- `public static IImmutableSolidColorBrush LightGoldenrodYellow => KnownColor.LightGoldenrodYellow.ToBrush();`
- `public static IImmutableSolidColorBrush LightGray => KnownColor.LightGray.ToBrush();`
- `public static IImmutableSolidColorBrush LightGreen => KnownColor.LightGreen.ToBrush();`
- `public static IImmutableSolidColorBrush LightPink => KnownColor.LightPink.ToBrush();`
- `public static IImmutableSolidColorBrush LightSalmon => KnownColor.LightSalmon.ToBrush();`
- `public static IImmutableSolidColorBrush LightSeaGreen => KnownColor.LightSeaGreen.ToBrush();`
- `public static IImmutableSolidColorBrush LightSkyBlue => KnownColor.LightSkyBlue.ToBrush();`
- `public static IImmutableSolidColorBrush LightSlateGray => KnownColor.LightSlateGray.ToBrush();`
- `public static IImmutableSolidColorBrush LightSteelBlue => KnownColor.LightSteelBlue.ToBrush();`
- `public static IImmutableSolidColorBrush LightYellow => KnownColor.LightYellow.ToBrush();`
- `public static IImmutableSolidColorBrush Lime => KnownColor.Lime.ToBrush();`
- `public static IImmutableSolidColorBrush LimeGreen => KnownColor.LimeGreen.ToBrush();`
- `public static IImmutableSolidColorBrush Linen => KnownColor.Linen.ToBrush();`
- `public static IImmutableSolidColorBrush Magenta => KnownColor.Magenta.ToBrush();`
- `public static IImmutableSolidColorBrush Maroon => KnownColor.Maroon.ToBrush();`
- `public static IImmutableSolidColorBrush MediumAquamarine => KnownColor.MediumAquamarine.ToBrush();`
- `public static IImmutableSolidColorBrush MediumBlue => KnownColor.MediumBlue.ToBrush();`
- `public static IImmutableSolidColorBrush MediumOrchid => KnownColor.MediumOrchid.ToBrush();`
- `public static IImmutableSolidColorBrush MediumPurple => KnownColor.MediumPurple.ToBrush();`
- `public static IImmutableSolidColorBrush MediumSeaGreen => KnownColor.MediumSeaGreen.ToBrush();`
- `public static IImmutableSolidColorBrush MediumSlateBlue => KnownColor.MediumSlateBlue.ToBrush();`
- `public static IImmutableSolidColorBrush MediumSpringGreen => KnownColor.MediumSpringGreen.ToBrush();`
- `public static IImmutableSolidColorBrush MediumTurquoise => KnownColor.MediumTurquoise.ToBrush();`
- `public static IImmutableSolidColorBrush MediumVioletRed => KnownColor.MediumVioletRed.ToBrush();`
- `public static IImmutableSolidColorBrush MidnightBlue => KnownColor.MidnightBlue.ToBrush();`
- `public static IImmutableSolidColorBrush MintCream => KnownColor.MintCream.ToBrush();`
- `public static IImmutableSolidColorBrush MistyRose => KnownColor.MistyRose.ToBrush();`
- `public static IImmutableSolidColorBrush Moccasin => KnownColor.Moccasin.ToBrush();`
- `public static IImmutableSolidColorBrush NavajoWhite => KnownColor.NavajoWhite.ToBrush();`
- `public static IImmutableSolidColorBrush Navy => KnownColor.Navy.ToBrush();`
- `public static IImmutableSolidColorBrush OldLace => KnownColor.OldLace.ToBrush();`
- `public static IImmutableSolidColorBrush Olive => KnownColor.Olive.ToBrush();`
- `public static IImmutableSolidColorBrush OliveDrab => KnownColor.OliveDrab.ToBrush();`
- `public static IImmutableSolidColorBrush Orange => KnownColor.Orange.ToBrush();`
- `public static IImmutableSolidColorBrush OrangeRed => KnownColor.OrangeRed.ToBrush();`
- `public static IImmutableSolidColorBrush Orchid => KnownColor.Orchid.ToBrush();`
- `public static IImmutableSolidColorBrush PaleGoldenrod => KnownColor.PaleGoldenrod.ToBrush();`
- `public static IImmutableSolidColorBrush PaleGreen => KnownColor.PaleGreen.ToBrush();`
- `public static IImmutableSolidColorBrush PaleTurquoise => KnownColor.PaleTurquoise.ToBrush();`
- `public static IImmutableSolidColorBrush PaleVioletRed => KnownColor.PaleVioletRed.ToBrush();`
- `public static IImmutableSolidColorBrush PapayaWhip => KnownColor.PapayaWhip.ToBrush();`
- `public static IImmutableSolidColorBrush PeachPuff => KnownColor.PeachPuff.ToBrush();`
- `public static IImmutableSolidColorBrush Peru => KnownColor.Peru.ToBrush();`
- `public static IImmutableSolidColorBrush Pink => KnownColor.Pink.ToBrush();`
- `public static IImmutableSolidColorBrush Plum => KnownColor.Plum.ToBrush();`
- `public static IImmutableSolidColorBrush PowderBlue => KnownColor.PowderBlue.ToBrush();`
- `public static IImmutableSolidColorBrush Purple => KnownColor.Purple.ToBrush();`
- `public static IImmutableSolidColorBrush Red => KnownColor.Red.ToBrush();`
- `public static IImmutableSolidColorBrush RosyBrown => KnownColor.RosyBrown.ToBrush();`
- `public static IImmutableSolidColorBrush RoyalBlue => KnownColor.RoyalBlue.ToBrush();`
- `public static IImmutableSolidColorBrush SaddleBrown => KnownColor.SaddleBrown.ToBrush();`
- `public static IImmutableSolidColorBrush Salmon => KnownColor.Salmon.ToBrush();`
- `public static IImmutableSolidColorBrush SandyBrown => KnownColor.SandyBrown.ToBrush();`
- `... 22 more signatures omitted (increase --max-per-file to include them).`

### `src/Avalonia.Base/Media/CharacterHit.cs`
- `public readonly struct CharacterHit : IEquatable<CharacterHit>`
- `public CharacterHit(int firstCharacterIndex, int trailingLength = 0) {`
- `public int FirstCharacterIndex { get; }`
- `public int TrailingLength { get; }`
- `public bool Equals(CharacterHit other) {`
- `public override bool Equals(object? obj) {`
- `public override int GetHashCode() {`
- `public static bool operator ==(CharacterHit left, CharacterHit right) {`
- `public static bool operator !=(CharacterHit left, CharacterHit right) {`

### `src/Avalonia.Base/Media/Colors.cs`
- `public sealed class Colors`
- `public static Color AliceBlue => KnownColor.AliceBlue.ToColor();`
- `public static Color AntiqueWhite => KnownColor.AntiqueWhite.ToColor();`
- `public static Color Aqua => KnownColor.Aqua.ToColor();`
- `public static Color Aquamarine => KnownColor.Aquamarine.ToColor();`
- `public static Color Azure => KnownColor.Azure.ToColor();`
- `public static Color Beige => KnownColor.Beige.ToColor();`
- `public static Color Bisque => KnownColor.Bisque.ToColor();`
- `public static Color Black => KnownColor.Black.ToColor();`
- `public static Color BlanchedAlmond => KnownColor.BlanchedAlmond.ToColor();`
- `public static Color Blue => KnownColor.Blue.ToColor();`
- `public static Color BlueViolet => KnownColor.BlueViolet.ToColor();`
- `public static Color Brown => KnownColor.Brown.ToColor();`
- `public static Color BurlyWood => KnownColor.BurlyWood.ToColor();`
- `public static Color CadetBlue => KnownColor.CadetBlue.ToColor();`
- `public static Color Chartreuse => KnownColor.Chartreuse.ToColor();`
- `public static Color Chocolate => KnownColor.Chocolate.ToColor();`
- `public static Color Coral => KnownColor.Coral.ToColor();`
- `public static Color CornflowerBlue => KnownColor.CornflowerBlue.ToColor();`
- `public static Color Cornsilk => KnownColor.Cornsilk.ToColor();`
- `public static Color Crimson => KnownColor.Crimson.ToColor();`
- `public static Color Cyan => KnownColor.Cyan.ToColor();`
- `public static Color DarkBlue => KnownColor.DarkBlue.ToColor();`
- `public static Color DarkCyan => KnownColor.DarkCyan.ToColor();`
- `public static Color DarkGoldenrod => KnownColor.DarkGoldenrod.ToColor();`
- `public static Color DarkGray => KnownColor.DarkGray.ToColor();`
- `public static Color DarkGreen => KnownColor.DarkGreen.ToColor();`
- `public static Color DarkKhaki => KnownColor.DarkKhaki.ToColor();`
- `public static Color DarkMagenta => KnownColor.DarkMagenta.ToColor();`
- `public static Color DarkOliveGreen => KnownColor.DarkOliveGreen.ToColor();`
- `public static Color DarkOrange => KnownColor.DarkOrange.ToColor();`
- `public static Color DarkOrchid => KnownColor.DarkOrchid.ToColor();`
- `public static Color DarkRed => KnownColor.DarkRed.ToColor();`
- `public static Color DarkSalmon => KnownColor.DarkSalmon.ToColor();`
- `public static Color DarkSeaGreen => KnownColor.DarkSeaGreen.ToColor();`
- `public static Color DarkSlateBlue => KnownColor.DarkSlateBlue.ToColor();`
- `public static Color DarkSlateGray => KnownColor.DarkSlateGray.ToColor();`
- `public static Color DarkTurquoise => KnownColor.DarkTurquoise.ToColor();`
- `public static Color DarkViolet => KnownColor.DarkViolet.ToColor();`
- `public static Color DeepPink => KnownColor.DeepPink.ToColor();`
- `public static Color DeepSkyBlue => KnownColor.DeepSkyBlue.ToColor();`
- `public static Color DimGray => KnownColor.DimGray.ToColor();`
- `public static Color DodgerBlue => KnownColor.DodgerBlue.ToColor();`
- `public static Color Firebrick => KnownColor.Firebrick.ToColor();`
- `public static Color FloralWhite => KnownColor.FloralWhite.ToColor();`
- `public static Color ForestGreen => KnownColor.ForestGreen.ToColor();`
- `public static Color Fuchsia => KnownColor.Fuchsia.ToColor();`
- `public static Color Gainsboro => KnownColor.Gainsboro.ToColor();`
- `public static Color GhostWhite => KnownColor.GhostWhite.ToColor();`
- `public static Color Gold => KnownColor.Gold.ToColor();`
- `public static Color Goldenrod => KnownColor.Goldenrod.ToColor();`
- `public static Color Gray => KnownColor.Gray.ToColor();`
- `public static Color Green => KnownColor.Green.ToColor();`
- `public static Color GreenYellow => KnownColor.GreenYellow.ToColor();`
- `public static Color Honeydew => KnownColor.Honeydew.ToColor();`
- `public static Color HotPink => KnownColor.HotPink.ToColor();`
- `public static Color IndianRed => KnownColor.IndianRed.ToColor();`
- `public static Color Indigo => KnownColor.Indigo.ToColor();`
- `public static Color Ivory => KnownColor.Ivory.ToColor();`
- `public static Color Khaki => KnownColor.Khaki.ToColor();`
- `public static Color Lavender => KnownColor.Lavender.ToColor();`
- `public static Color LavenderBlush => KnownColor.LavenderBlush.ToColor();`
- `public static Color LawnGreen => KnownColor.LawnGreen.ToColor();`
- `public static Color LemonChiffon => KnownColor.LemonChiffon.ToColor();`
- `public static Color LightBlue => KnownColor.LightBlue.ToColor();`
- `public static Color LightCoral => KnownColor.LightCoral.ToColor();`
- `public static Color LightCyan => KnownColor.LightCyan.ToColor();`
- `public static Color LightGoldenrodYellow => KnownColor.LightGoldenrodYellow.ToColor();`
- `public static Color LightGray => KnownColor.LightGray.ToColor();`
- `public static Color LightGreen => KnownColor.LightGreen.ToColor();`
- `public static Color LightPink => KnownColor.LightPink.ToColor();`
- `public static Color LightSalmon => KnownColor.LightSalmon.ToColor();`
- `public static Color LightSeaGreen => KnownColor.LightSeaGreen.ToColor();`
- `public static Color LightSkyBlue => KnownColor.LightSkyBlue.ToColor();`
- `public static Color LightSlateGray => KnownColor.LightSlateGray.ToColor();`
- `public static Color LightSteelBlue => KnownColor.LightSteelBlue.ToColor();`
- `public static Color LightYellow => KnownColor.LightYellow.ToColor();`
- `public static Color Lime => KnownColor.Lime.ToColor();`
- `public static Color LimeGreen => KnownColor.LimeGreen.ToColor();`
- `public static Color Linen => KnownColor.Linen.ToColor();`
- `public static Color Magenta => KnownColor.Magenta.ToColor();`
- `public static Color Maroon => KnownColor.Maroon.ToColor();`
- `public static Color MediumAquamarine => KnownColor.MediumAquamarine.ToColor();`
- `public static Color MediumBlue => KnownColor.MediumBlue.ToColor();`
- `public static Color MediumOrchid => KnownColor.MediumOrchid.ToColor();`
- `public static Color MediumPurple => KnownColor.MediumPurple.ToColor();`
- `public static Color MediumSeaGreen => KnownColor.MediumSeaGreen.ToColor();`
- `public static Color MediumSlateBlue => KnownColor.MediumSlateBlue.ToColor();`
- `public static Color MediumSpringGreen => KnownColor.MediumSpringGreen.ToColor();`
- `public static Color MediumTurquoise => KnownColor.MediumTurquoise.ToColor();`
- `public static Color MediumVioletRed => KnownColor.MediumVioletRed.ToColor();`
- `public static Color MidnightBlue => KnownColor.MidnightBlue.ToColor();`
- `public static Color MintCream => KnownColor.MintCream.ToColor();`
- `public static Color MistyRose => KnownColor.MistyRose.ToColor();`
- `public static Color Moccasin => KnownColor.Moccasin.ToColor();`
- `public static Color NavajoWhite => KnownColor.NavajoWhite.ToColor();`
- `public static Color Navy => KnownColor.Navy.ToColor();`
- `public static Color OldLace => KnownColor.OldLace.ToColor();`
- `public static Color Olive => KnownColor.Olive.ToColor();`
- `public static Color OliveDrab => KnownColor.OliveDrab.ToColor();`
- `public static Color Orange => KnownColor.Orange.ToColor();`
- `public static Color OrangeRed => KnownColor.OrangeRed.ToColor();`
- `public static Color Orchid => KnownColor.Orchid.ToColor();`
- `public static Color PaleGoldenrod => KnownColor.PaleGoldenrod.ToColor();`
- `public static Color PaleGreen => KnownColor.PaleGreen.ToColor();`
- `public static Color PaleTurquoise => KnownColor.PaleTurquoise.ToColor();`
- `public static Color PaleVioletRed => KnownColor.PaleVioletRed.ToColor();`
- `public static Color PapayaWhip => KnownColor.PapayaWhip.ToColor();`
- `public static Color PeachPuff => KnownColor.PeachPuff.ToColor();`
- `public static Color Peru => KnownColor.Peru.ToColor();`
- `public static Color Pink => KnownColor.Pink.ToColor();`
- `public static Color Plum => KnownColor.Plum.ToColor();`
- `public static Color PowderBlue => KnownColor.PowderBlue.ToColor();`
- `public static Color Purple => KnownColor.Purple.ToColor();`
- `public static Color Red => KnownColor.Red.ToColor();`
- `public static Color RosyBrown => KnownColor.RosyBrown.ToColor();`
- `public static Color RoyalBlue => KnownColor.RoyalBlue.ToColor();`
- `public static Color SaddleBrown => KnownColor.SaddleBrown.ToColor();`
- `public static Color Salmon => KnownColor.Salmon.ToColor();`
- `public static Color SandyBrown => KnownColor.SandyBrown.ToColor();`
- `... 22 more signatures omitted (increase --max-per-file to include them).`

### `src/Avalonia.Base/Media/ConicGradientBrush.cs`
- `public sealed class ConicGradientBrush : GradientBrush, IConicGradientBrush`
- `public static readonly StyledProperty<RelativePoint> CenterProperty = AvaloniaProperty.Register<ConicGradientBrush, RelativePoint>( nameof(Center), RelativePoint.Center);`
- `public static readonly StyledProperty<double> AngleProperty = AvaloniaProperty.Register<ConicGradientBrush, double>( nameof(Angle), 0);`
- `public RelativePoint Center {`
- `public double Angle {`
- `public override IImmutableBrush ToImmutable() {`

### `src/Avalonia.Base/Media/DashStyle.cs`
- `public sealed class DashStyle : Animatable, IDashStyle`
- `public static readonly StyledProperty<AvaloniaList<double>?> DashesProperty = AvaloniaProperty.Register<DashStyle, AvaloniaList<double>?>(nameof(Dashes));`
- `public static readonly StyledProperty<double> OffsetProperty = AvaloniaProperty.Register<DashStyle, double>(nameof(Offset));`
- `public DashStyle() {`
- `public DashStyle(IEnumerable<double>? dashes, double offset) {`
- `public static IDashStyle Dash => s_dash ??= new ImmutableDashStyle(new double[] { 2, 2 }, 1);`
- `public static IDashStyle Dot => s_dot ??= new ImmutableDashStyle(new double[] { 0, 2 }, 0);`
- `public static IDashStyle DashDot => s_dashDot ??= new ImmutableDashStyle(new double[] { 2, 2, 0, 2 }, 1);`
- `public static IDashStyle DashDotDot => s_dashDotDot ??= new ImmutableDashStyle(new double[] { 2, 2, 0, 2, 0, 2 }, 1);`
- `public AvaloniaList<double>? Dashes {`
- `public double Offset {`
- `public ImmutableDashStyle ToImmutable() => new ImmutableDashStyle(Dashes, Offset);`

### `src/Avalonia.Base/Media/Drawing.cs`
- `public abstract class Drawing : AvaloniaObject`
- `public void Draw(DrawingContext context) => DrawCore(context);`
- `public abstract Rect GetBounds();`

### `src/Avalonia.Base/Media/DrawingBrush.cs`
- `public sealed class DrawingBrush : TileBrush, ISceneBrush`
- `public static readonly StyledProperty<Drawing?> DrawingProperty = AvaloniaProperty.Register<DrawingBrush, Drawing?>(nameof(Drawing));`
- `public DrawingBrush() {`
- `public DrawingBrush(Drawing visual) {`
- `public Drawing? Drawing {`

### `src/Avalonia.Base/Media/DrawingCollection.cs`
- `public sealed class DrawingCollection : AvaloniaList<Drawing>`
- `public DrawingCollection() {`
- `public DrawingCollection(IEnumerable<Drawing> items) : base(items) {`

### `src/Avalonia.Base/Media/DrawingContext.cs`
- `public abstract class DrawingContext : IDisposable`
- `public void Dispose() {`
- `public virtual void DrawImage(IImage source, Rect rect) {`
- `public virtual void DrawImage(IImage source, Rect sourceRect, Rect destRect) {`
- `public void DrawLine(IPen pen, Point p1, Point p2) {`
- `public void DrawGeometry(IBrush? brush, IPen? pen, Geometry geometry) {`
- `public void DrawGeometry(IBrush? brush, IPen? pen, IGeometryImpl geometry) {`
- `public void DrawRectangle(IBrush? brush, IPen? pen, Rect rect, double radiusX = 0, double radiusY = 0, BoxShadows boxShadows = default) {`
- `public void DrawRectangle(IBrush? brush, IPen? pen, RoundedRect rrect, BoxShadows boxShadows = default) {`
- `public void DrawRectangle(IPen pen, Rect rect, float cornerRadius = 0.0f) =>`
- `public void FillRectangle(IBrush brush, Rect rect, float cornerRadius = 0.0f) =>`
- `public void DrawEllipse(IBrush? brush, IPen? pen, Point center, double radiusX, double radiusY) {`
- `public void DrawEllipse(IBrush? brush, IPen? pen, Rect rect) {`
- `public abstract void Custom(ICustomDrawOperation custom);`
- `public virtual void DrawText(FormattedText text, Point origin) {`
- `public abstract void DrawGlyphRun(IBrush? foreground, GlyphRun glyphRun);`
- `public record struct PushedState : IDisposable`
- `public PushedState(DrawingContext context) {`
- `public void Dispose() {`
- `public PushedState PushClip(RoundedRect clip) {`
- `public PushedState PushClip(Rect clip) {`
- `public PushedState PushGeometryClip(Geometry clip) {`
- `public PushedState PushOpacity(double opacity) {`
- `public PushedState PushOpacityMask(IBrush mask, Rect bounds) {`
- `public PushedState PushTransform(Matrix matrix) {`
- `public PushedState PushRenderOptions(RenderOptions renderOptions) {`
- `public PushedState PushPreTransform(Matrix matrix) => PushTransform(matrix);`
- `public PushedState PushPostTransform(Matrix matrix) => PushTransform(matrix);`
- `public PushedState PushTransformContainer() => PushTransform(Matrix.Identity);`

### `src/Avalonia.Base/Media/DrawingGroup.cs`
- `public sealed class DrawingGroup : Drawing`
- `public static readonly StyledProperty<double> OpacityProperty = AvaloniaProperty.Register<DrawingGroup, double>(nameof(Opacity), 1);`
- `public static readonly StyledProperty<Transform?> TransformProperty = AvaloniaProperty.Register<DrawingGroup, Transform?>(nameof(Transform));`
- `public static readonly StyledProperty<Geometry?> ClipGeometryProperty = AvaloniaProperty.Register<DrawingGroup, Geometry?>(nameof(ClipGeometry));`
- `public static readonly StyledProperty<IBrush?> OpacityMaskProperty = AvaloniaProperty.Register<DrawingGroup, IBrush?>(nameof(OpacityMask));`
- `public static readonly DirectProperty<DrawingGroup, DrawingCollection> ChildrenProperty = AvaloniaProperty.RegisterDirect<DrawingGroup, DrawingCollection>( nameof(Children), o => o.Children,`
- `public double Opacity {`
- `public Transform? Transform {`
- `public Geometry? ClipGeometry {`
- `public IBrush? OpacityMask {`
- `public DrawingCollection Children {`
- `public DrawingContext Open() => new DrawingGroupDrawingContext(this);`
- `public override Rect GetBounds() {`

### `src/Avalonia.Base/Media/DrawingImage.cs`
- `public class DrawingImage : AvaloniaObject, IImage, IAffectsRender`
- `public DrawingImage() {`
- `public DrawingImage(Drawing drawing) {`
- `public static readonly StyledProperty<Drawing?> DrawingProperty = AvaloniaProperty.Register<DrawingImage, Drawing?>(nameof(Drawing));`
- `public event EventHandler? Invalidated;`
- `public Drawing? Drawing {`
- `public Size Size => Drawing?.GetBounds().Size ?? default;`

### `src/Avalonia.Base/Media/EdgeMode.cs`
- `public enum EdgeMode : byte`

### `src/Avalonia.Base/Media/Effects/BlurEffect.cs`
- Namespace: `Avalonia.Media`
- `public sealed class BlurEffect : Effect, IBlurEffect, IMutableEffect`
- `public static readonly StyledProperty<double> RadiusProperty = AvaloniaProperty.Register<BlurEffect, double>( nameof(Radius), 5);`
- `public double Radius {`
- `public IImmutableEffect ToImmutable() => new ImmutableBlurEffect(Radius);`

### `src/Avalonia.Base/Media/Effects/DropShadowEffect.cs`
- Namespace: `Avalonia.Media`
- `public abstract class DropShadowEffectBase : Effect`
- `public static readonly StyledProperty<double> BlurRadiusProperty = AvaloniaProperty.Register<DropShadowEffectBase, double>( nameof(BlurRadius), 5);`
- `public double BlurRadius {`
- `public static readonly StyledProperty<Color> ColorProperty = AvaloniaProperty.Register<DropShadowEffectBase, Color>( nameof(Color), Colors.Black);`
- `public Color Color {`
- `public static readonly StyledProperty<double> OpacityProperty = AvaloniaProperty.Register<DropShadowEffectBase, double>( nameof(Opacity), 1);`
- `public double Opacity {`
- `public sealed class DropShadowEffect : DropShadowEffectBase, IDropShadowEffect, IMutableEffect`
- `public static readonly StyledProperty<double> OffsetXProperty = AvaloniaProperty.Register<DropShadowEffect, double>( nameof(OffsetX), 3.5355);`
- `public double OffsetX {`
- `public static readonly StyledProperty<double> OffsetYProperty = AvaloniaProperty.Register<DropShadowEffect, double>( nameof(OffsetY), 3.5355);`
- `public double OffsetY {`
- `public IImmutableEffect ToImmutable() {`
- `public sealed class DropShadowDirectionEffect : DropShadowEffectBase, IDirectionDropShadowEffect, IMutableEffect`
- `public static readonly StyledProperty<double> ShadowDepthProperty = AvaloniaProperty.Register<DropShadowDirectionEffect, double>( nameof(ShadowDepth), 5);`
- `public double ShadowDepth {`
- `public static readonly StyledProperty<double> DirectionProperty = AvaloniaProperty.Register<DropShadowDirectionEffect, double>( nameof(Direction), 315);`
- `public double Direction {`
- `public double OffsetX => Math.Cos(Direction * Math.PI / 180) * ShadowDepth;`
- `public double OffsetY => Math.Sin(Direction * Math.PI / 180) * ShadowDepth;`
- `public IImmutableEffect ToImmutable() => new ImmutableDropShadowDirectionEffect(OffsetX, OffsetY, BlurRadius, Color, Opacity);`

### `src/Avalonia.Base/Media/Effects/Effect.cs`
- Namespace: `Avalonia.Media`
- `public class Effect : Animatable, IAffectsRender`
- `public event EventHandler? Invalidated;`
- `public static IEffect Parse(string s) {`

### `src/Avalonia.Base/Media/Effects/EffectConverter.cs`
- Namespace: `Avalonia.Media`
- `public class EffectConverter : TypeConverter`
- `public override bool CanConvertFrom(ITypeDescriptorContext? context, Type sourceType) {`
- `public override object? ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object? value) {`

### `src/Avalonia.Base/Media/Effects/EffectExtesions.cs`
- Namespace: `Avalonia.Media`
- `public static class EffectExtensions`
- `public static IImmutableEffect ToImmutable(this IEffect effect) {`

### `src/Avalonia.Base/Media/Effects/EffectTransition.cs`
- Namespace: `Avalonia.Animation`
- `public class EffectTransition : Transition<IEffect?>`

### `src/Avalonia.Base/Media/Effects/IBlurEffect.cs`
- Namespace: `Avalonia.Media`
- `public interface IBlurEffect : IEffect`
- `public class ImmutableBlurEffect : IBlurEffect, IImmutableEffect`
- `public ImmutableBlurEffect(double radius) {`
- `public double Radius { get; }`
- `public bool Equals(IEffect? other) =>`

### `src/Avalonia.Base/Media/Effects/IDropShadowEffect.cs`
- Namespace: `Avalonia.Media`
- `public interface IDropShadowEffect : IEffect`
- `public class ImmutableDropShadowEffect : IDropShadowEffect, IImmutableEffect`
- `public ImmutableDropShadowEffect(double offsetX, double offsetY, double blurRadius, Color color, double opacity) {`
- `public double OffsetX { get; }`
- `public double OffsetY { get; }`
- `public double BlurRadius { get; }`
- `public Color Color { get; }`
- `public double Opacity { get; }`
- `public bool Equals(IEffect? other) {`
- `public class ImmutableDropShadowDirectionEffect : IDirectionDropShadowEffect, IImmutableEffect`
- `public ImmutableDropShadowDirectionEffect(double direction, double shadowDepth, double blurRadius, Color color, double opacity) {`
- `public double OffsetX => Math.Cos(Direction * Math.PI / 180) * ShadowDepth;`
- `public double OffsetY => Math.Sin(Direction * Math.PI / 180) * ShadowDepth;`
- `public double Direction { get; }`
- `public double ShadowDepth { get; }`
- `public double BlurRadius { get; }`
- `public Color Color { get; }`
- `public double Opacity { get; }`
- `public bool Equals(IEffect? other) {`

### `src/Avalonia.Base/Media/Effects/IEffect.cs`
- Namespace: `Avalonia.Media`
- `public interface IEffect`
- `public interface IMutableEffect : IEffect`
- `public interface IImmutableEffect : IEffect, IEquatable<IEffect>`

### `src/Avalonia.Base/Media/EllipseGeometry.cs`
- `public class EllipseGeometry : Geometry`
- `public static readonly StyledProperty<Rect> RectProperty = AvaloniaProperty.Register<EllipseGeometry, Rect>(nameof(Rect));`
- `public static readonly StyledProperty<double> RadiusXProperty = AvaloniaProperty.Register<EllipseGeometry, double>(nameof(RadiusX));`
- `public static readonly StyledProperty<double> RadiusYProperty = AvaloniaProperty.Register<EllipseGeometry, double>(nameof(RadiusY));`
- `public static readonly StyledProperty<Point> CenterProperty = AvaloniaProperty.Register<EllipseGeometry, Point>(nameof(Center));`
- `public EllipseGeometry() {`
- `public EllipseGeometry(Rect rect) : this() {`
- `public Rect Rect {`
- `public double RadiusX {`
- `public double RadiusY {`
- `public Point Center {`
- `public override Geometry Clone() {`

### `src/Avalonia.Base/Media/ExperimentalAcrylicMaterial.cs`
- `public class ExperimentalAcrylicMaterial : AvaloniaObject, IMutableExperimentalAcrylicMaterial`
- `public static readonly StyledProperty<Color> TintColorProperty = AvaloniaProperty.Register<ExperimentalAcrylicMaterial, Color>(nameof(TintColor));`
- `public static readonly StyledProperty<AcrylicBackgroundSource> BackgroundSourceProperty = AvaloniaProperty.Register<ExperimentalAcrylicMaterial, AcrylicBackgroundSource>(nameof(BackgroundSource));`
- `public static readonly StyledProperty<double> TintOpacityProperty = AvaloniaProperty.Register<ExperimentalAcrylicMaterial, double>(nameof(TintOpacity), 0.8);`
- `public static readonly StyledProperty<double> MaterialOpacityProperty = AvaloniaProperty.Register<ExperimentalAcrylicMaterial, double>(nameof(MaterialOpacity), 0.5);`
- `public static readonly StyledProperty<double> PlatformTransparencyCompensationLevelProperty = AvaloniaProperty.Register<ExperimentalAcrylicMaterial, double>(nameof(PlatformTransparencyCompensationLevel), 0.0);`
- `public static readonly StyledProperty<Color> FallbackColorProperty = AvaloniaProperty.Register<ExperimentalAcrylicMaterial, Color>(nameof(FallbackColor));`
- `public event EventHandler? Invalidated;`
- `public AcrylicBackgroundSource BackgroundSource {`
- `public Color TintColor {`
- `public double TintOpacity {`
- `public Color FallbackColor {`
- `public double MaterialOpacity {`
- `public double PlatformTransparencyCompensationLevel {`
- `public IExperimentalAcrylicMaterial ToImmutable() {`

### `src/Avalonia.Base/Media/FillRule.cs`
- `public enum FillRule`

### `src/Avalonia.Base/Media/FlowDirection.cs`
- `public enum FlowDirection`

### `src/Avalonia.Base/Media/FontFallback.cs`
- `public class FontFallback`
- `public FontFamily FontFamily { get; set; } = FontFamily.Default;`
- `public UnicodeRange UnicodeRange { get; set; } = UnicodeRange.Default;`

### `src/Avalonia.Base/Media/FontFamily.cs`
- `public sealed class FontFamily`
- `public const string DefaultFontFamilyName = "$Default";`
- `public FontFamily(string name) : this(null, name) {`
- `public FontFamily(Uri? baseUri, string name) {`
- `public static FontFamily Default { get; }`
- `public string Name => FamilyNames.PrimaryFamilyName;`
- `public FamilyNameCollection FamilyNames { get; }`
- `public FontFamilyKey? Key { get; }`
- `public IReadOnlyList<Typeface> FamilyTypefaces => FontManager.Current.GetFamilyTypefaces(this);`
- `public static implicit operator FontFamily(string s) {`
- `public static FontFamily Parse(string s) => Parse(s, null);`
- `public static FontFamily Parse(string s, Uri? baseUri) {`
- `public override string ToString() {`
- `public override int GetHashCode() {`
- `public static bool operator !=(FontFamily? a, FontFamily? b) {`
- `public static bool operator ==(FontFamily? a, FontFamily? b) {`
- `public override bool Equals(object? obj) {`

### `src/Avalonia.Base/Media/FontFeature.cs`
- Namespace: `Avalonia.Media`
- `public record FontFeature`
- `public string Tag {`
- `public int Value {`
- `public int Start {`
- `public int End {`
- `public FontFeature() {`
- `public static FontFeature Parse(string s) {`
- `public override string ToString() {`

### `src/Avalonia.Base/Media/FontFeatureCollection.cs`
- Namespace: `Avalonia.Media`
- `public class FontFeatureCollection : AvaloniaList<FontFeature>`

### `src/Avalonia.Base/Media/FontManager.cs`
- `public sealed class FontManager : IDisposable`
- `public const string FontCollectionScheme = "fonts";`
- `public const string SystemFontScheme = "systemfont";`
- `public const string CompositeFontScheme = "compositefont";`
- `public FontManager(IFontManagerImpl platformImpl) {`
- `public static FontManager Current {`
- `public FontFamily DefaultFontFamily {`
- `public IFontCollection SystemFonts => _fontCollections[SystemFontsKey];`
- `public bool TryGetGlyphTypeface(Typeface typeface, [NotNullWhen(true)] out IGlyphTypeface? glyphTypeface) {`
- `public void AddFontCollection(IFontCollection fontCollection) {`
- `public void RemoveFontCollection(Uri key) {`
- `public bool TryMatchCharacter(int codepoint, FontStyle fontStyle, FontWeight fontWeight, FontStretch fontStretch, FontFamily? fontFamily, CultureInfo? culture, out Typeface typeface) {`

### `src/Avalonia.Base/Media/FontManagerOptions.cs`
- `public class FontManagerOptions`
- `public string? DefaultFamilyName { get; set; }`
- `public IReadOnlyList<FontFallback>? FontFallbacks { get; set; }`
- `public IReadOnlyDictionary<string, FontFamily>? FontFamilyMappings { get; set; }`

### `src/Avalonia.Base/Media/FontMetrics.cs`
- `public readonly record struct FontMetrics`
- `public short DesignEmHeight { get; init; }`
- `public bool IsFixedPitch { get; init; }`
- `public int Ascent { get; init; }`
- `public int Descent { get; init; }`
- `public int LineGap { get; init; }`
- `public int LineSpacing => Descent - Ascent + LineGap;`
- `public int UnderlinePosition { get; init; }`
- `public int UnderlineThickness { get; init; }`
- `public int StrikethroughPosition { get; init; }`
- `public int StrikethroughThickness { get; init; }`

### `src/Avalonia.Base/Media/FontSimulations.cs`
- `public enum FontSimulations : byte`

### `src/Avalonia.Base/Media/FontStretch.cs`
- `public enum FontStretch`

### `src/Avalonia.Base/Media/FontStyle.cs`
- `public enum FontStyle`

### `src/Avalonia.Base/Media/FontWeight.cs`
- `public enum FontWeight`

### `src/Avalonia.Base/Media/Fonts/EmbeddedFontCollection.cs`
- `public class EmbeddedFontCollection : FontCollectionBase, IFontCollection2`
- `public EmbeddedFontCollection(Uri key, Uri source) {`
- `public override Uri Key => _key;`
- `public override FontFamily this[int index] => _fontFamilies[index];`
- `public override int Count => _fontFamilies.Count;`
- `public override void Initialize(IFontManagerImpl fontManager) {`
- `public override bool TryGetGlyphTypeface(string familyName, FontStyle style, FontWeight weight, FontStretch stretch, [NotNullWhen(true)] out IGlyphTypeface? glyphTypeface) {`
- `public override IEnumerator<FontFamily> GetEnumerator() => _fontFamilies.GetEnumerator();`
- `public bool TryGetFamilyTypefaces(string familyName, [NotNullWhen(true)] out IReadOnlyList<Typeface>? familyTypefaces) {`

### `src/Avalonia.Base/Media/Fonts/FamilyNameCollection.cs`
- `public sealed class FamilyNameCollection : IReadOnlyList<string>`
- `public FamilyNameCollection(string familyNames) {`
- `public string PrimaryFamilyName { get; }`
- `public bool HasFallbacks { get; }`
- `public ImmutableReadOnlyListStructEnumerator<string> GetEnumerator() {`
- `public override string ToString() => String.Join(", ", _names);`
- `public override int GetHashCode() {`
- `public static bool operator !=(FamilyNameCollection? a, FamilyNameCollection? b) {`
- `public static bool operator ==(FamilyNameCollection? a, FamilyNameCollection? b) {`
- `public override bool Equals(object? obj) => obj is FamilyNameCollection other && _names.AsSpan().SequenceEqual(other._names);`
- `public int Count => _names.Length;`
- `public string this[int index] => _names[index];`

### `src/Avalonia.Base/Media/Fonts/FontCollectionBase.cs`
- `public abstract class FontCollectionBase : IFontCollection`
- `public abstract Uri Key { get; }`
- `public abstract int Count { get; }`
- `public abstract FontFamily this[int index] { get; }`
- `public abstract bool TryGetGlyphTypeface(string familyName, FontStyle style, FontWeight weight, FontStretch stretch, [NotNullWhen(true)] out IGlyphTypeface? glyphTypeface);`
- `public virtual bool TryMatchCharacter(int codepoint, FontStyle style, FontWeight weight, FontStretch stretch, string? familyName, CultureInfo? culture, out Typeface match) {`
- `public virtual bool TryCreateSyntheticGlyphTypeface( IGlyphTypeface glyphTypeface, FontStyle style, FontWeight weight, FontStretch stretch, [NotNullWhen(true)] out IGlyphTypeface? syntheticGlyphTypeface) {`
- `public abstract void Initialize(IFontManagerImpl fontManager);`
- `public abstract IEnumerator<FontFamily> GetEnumerator();`

### `src/Avalonia.Base/Media/Fonts/FontCollectionKey.cs`
- `public readonly record struct FontCollectionKey(FontStyle Style, FontWeight Weight, FontStretch Stretch);`

### `src/Avalonia.Base/Media/Fonts/FontFamilyKey.cs`
- `public class FontFamilyKey`
- `public FontFamilyKey(Uri source, Uri? baseUri = null) {`
- `public Uri Source { get; }`
- `public Uri? BaseUri { get; }`
- `public override int GetHashCode() {`
- `public static bool operator !=(FontFamilyKey? a, FontFamilyKey? b) {`
- `public static bool operator ==(FontFamilyKey? a, FontFamilyKey? b) {`
- `public override bool Equals(object? obj) {`
- `public override string ToString() {`

### `src/Avalonia.Base/Media/Fonts/FontFamilyLoader.cs`
- `public static class FontFamilyLoader`
- `public static IEnumerable<Uri> LoadFontAssets(Uri source) {`

### `src/Avalonia.Base/Media/Fonts/IFontCollection.cs`
- `public interface IFontCollection : IReadOnlyList<FontFamily>, IDisposable`

### `src/Avalonia.Base/Media/FormattedText.cs`
- `public class FormattedText`
- `public const double DefaultRealToIdeal = 28800.0 / 96;`
- `public const double DefaultIdealToReal = 1 / DefaultRealToIdeal;`
- `public const int IdealInfiniteWidth = 0x3FFFFFFE;`
- `public const double RealInfiniteWidth = IdealInfiniteWidth * DefaultIdealToReal;`
- `public const double GreatestMultiplierOfEm = 100;`
- `public FormattedText( string textToFormat, CultureInfo culture, FlowDirection flowDirection, Typeface typeface, double emSize, IBrush? foreground) {`
- `public void SetForegroundBrush(IBrush foregroundBrush) {`
- `public void SetForegroundBrush(IBrush? foregroundBrush, int startIndex, int count) {`
- `public void SetFontFeatures(FontFeatureCollection? fontFeatures) {`
- `public void SetFontFeatures(FontFeatureCollection? fontFeatures, int startIndex, int count) {`
- `public void SetFontFamily(string fontFamily) {`
- `public void SetFontFamily(string fontFamily, int startIndex, int count) {`
- `public void SetFontFamily(FontFamily fontFamily) {`
- `public void SetFontFamily(FontFamily fontFamily, int startIndex, int count) {`
- `public void SetFontSize(double emSize) {`
- `public void SetFontSize(double emSize, int startIndex, int count) {`
- `public void SetCulture(CultureInfo culture) {`
- `public void SetCulture(CultureInfo culture, int startIndex, int count) {`
- `public void SetFontWeight(FontWeight weight) {`
- `public void SetFontWeight(FontWeight weight, int startIndex, int count) {`
- `public void SetFontStyle(FontStyle style) {`
- `public void SetFontStyle(FontStyle style, int startIndex, int count) {`
- `public void SetFontTypeface(Typeface typeface) {`
- `public void SetFontTypeface(Typeface typeface, int startIndex, int count) {`
- `public void SetTextDecorations(TextDecorationCollection textDecorations) {`
- `public void SetTextDecorations(TextDecorationCollection textDecorations, int startIndex, int count) {`
- `public FlowDirection FlowDirection {`
- `public TextAlignment TextAlignment {`
- `public double LineHeight {`
- `public double MaxTextWidth {`
- `public void SetMaxTextWidths(double[] maxTextWidths) {`
- `public double[] GetMaxTextWidths() {`
- `public double MaxTextHeight {`
- `public int MaxLineCount {`
- `public TextTrimming Trimming {`
- `public double Height {`
- `public double Extent {`
- `public double Baseline {`
- `public double OverhangAfter {`
- `public double OverhangLeading {`
- `public double OverhangTrailing {`
- `public double Width {`
- `public double WidthIncludingTrailingWhitespace {`
- `public Geometry? BuildGeometry(Point origin) {`
- `public Geometry? BuildHighlightGeometry(Point origin) {`
- `public Geometry? BuildHighlightGeometry(Point origin, int startIndex, int count) {`

### `src/Avalonia.Base/Media/Geometry.cs`
- `public abstract class Geometry : AvaloniaObject`
- `public static readonly StyledProperty<Transform?> TransformProperty = AvaloniaProperty.Register<Geometry, Transform?>(nameof(Transform));`
- `public event EventHandler? Changed;`
- `public Rect Bounds => PlatformImpl?.Bounds ?? default;`
- `public Transform? Transform {`
- `public static Geometry Parse(string s) => StreamGeometry.Parse(s);`
- `public abstract Geometry Clone();`
- `public Rect GetRenderBounds(IPen pen) => PlatformImpl?.GetRenderBounds(pen) ?? default;`
- `public bool FillContains(Point point) {`
- `public bool StrokeContains(IPen pen, Point point) {`
- `public Geometry GetWidenedGeometry(IPen pen) {`
- `public double ContourLength => PlatformImpl?.ContourLength ?? 0;`
- `public static Geometry Combine(Geometry geometry1, RectangleGeometry geometry2, GeometryCombineMode combineMode, Transform? transform = null) {`
- `public bool TryGetPointAtDistance(double distance, out Point point) {`
- `public bool TryGetPointAndTangentAtDistance(double distance, out Point point, out Point tangent) {`
- `public bool TryGetSegment(double startDistance, double stopDistance, bool startOnBeginFigure, [NotNullWhen(true)] out Geometry? segmentGeometry) {`
- `public class GeometryTypeConverter : TypeConverter`
- `public override bool CanConvertFrom(ITypeDescriptorContext? context, Type sourceType) {`
- `public override object? ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object value) {`

### `src/Avalonia.Base/Media/GeometryCollection.cs`
- `public sealed class GeometryCollection : AvaloniaList<Geometry>`
- `public GeometryCollection() {`
- `public GeometryCollection(IEnumerable<Geometry> items) : base(items) {`
- `public GeometryGroup? Parent { get; set; }`

### `src/Avalonia.Base/Media/GeometryDrawing.cs`
- `public sealed class GeometryDrawing : Drawing`
- `public static readonly StyledProperty<Geometry?> GeometryProperty = AvaloniaProperty.Register<GeometryDrawing, Geometry?>(nameof(Geometry));`
- `public static readonly StyledProperty<IBrush?> BrushProperty = AvaloniaProperty.Register<GeometryDrawing, IBrush?>(nameof(Brush), Brushes.Transparent);`
- `public static readonly StyledProperty<IPen?> PenProperty = AvaloniaProperty.Register<GeometryDrawing, IPen?>(nameof(Pen));`
- `public Geometry? Geometry {`
- `public IBrush? Brush {`
- `public IPen? Pen {`
- `public override Rect GetBounds() {`

### `src/Avalonia.Base/Media/GeometryGroup.cs`
- `public class GeometryGroup : Geometry`
- `public static readonly DirectProperty<GeometryGroup, GeometryCollection> ChildrenProperty = AvaloniaProperty.RegisterDirect<GeometryGroup, GeometryCollection> ( nameof(Children), o => o.Children,`
- `public static readonly StyledProperty<FillRule> FillRuleProperty = AvaloniaProperty.Register<GeometryGroup, FillRule>(nameof(FillRule));`
- `public GeometryGroup() {`
- `public GeometryCollection Children {`
- `public FillRule FillRule {`
- `public override Geometry Clone() {`

### `src/Avalonia.Base/Media/GlyphMetrics.cs`
- `public readonly record struct GlyphMetrics`
- `public int XBearing { get; init; }`
- `public int YBearing{ get; init; }`
- `public int Width{ get; init; }`
- `public int Height{ get; init; }`

### `src/Avalonia.Base/Media/GlyphRun.cs`
- `public sealed class GlyphRun : IDisposable`
- `public GlyphRun( IGlyphTypeface glyphTypeface, double fontRenderingEmSize, ReadOnlyMemory<char> characters, IReadOnlyList<ushort> glyphIndices, Point? baselineOrigin = null, int biDiLevel = 0) : this(glyphTypeface, fontRenderingEmSize, characters, CreateGlyphInfos(glyphIndices, fontRenderingEmSize, glyphTypeface), baselineOrigin, biDiLevel) {`
- `public GlyphRun( IGlyphTypeface glyphTypeface, double fontRenderingEmSize, ReadOnlyMemory<char> characters, IReadOnlyList<GlyphInfo> glyphInfos, Point? baselineOrigin = null, int biDiLevel = 0) {`
- `public IGlyphTypeface GlyphTypeface { get; }`
- `public double FontRenderingEmSize {`
- `public Rect Bounds => new Rect(new Point(BaselineOrigin.X, 0),`
- `public Rect InkBounds => PlatformImpl.Item.Bounds;`
- `public GlyphRunMetrics Metrics => _glyphRunMetrics ??= CreateGlyphRunMetrics();`
- `public Point BaselineOrigin {`
- `public ReadOnlyMemory<char> Characters {`
- `public IReadOnlyList<GlyphInfo> GlyphInfos {`
- `public int BiDiLevel {`
- `public bool IsLeftToRight => ((BiDiLevel & 1) == 0);`
- `public Geometry BuildGeometry() {`
- `public double GetDistanceFromCharacterHit(CharacterHit characterHit) {`
- `public CharacterHit GetCharacterHitFromDistance(double distance, out bool isInside) {`
- `public CharacterHit GetNextCaretCharacterHit(CharacterHit characterHit) {`
- `public CharacterHit GetPreviousCaretCharacterHit(CharacterHit characterHit) {`
- `public int FindGlyphIndex(int characterIndex) {`
- `public CharacterHit FindNearestCharacterHit(int index, out double width) {`
- `public void Dispose() {`
- `public IReadOnlyList<float> GetIntersections(float lowerLimit, float upperLimit) {`
- `public IImmutableGlyphRunReference? TryCreateImmutableGlyphRunReference() => new ImmutableGlyphRunReference(PlatformImpl.Clone());`

### `src/Avalonia.Base/Media/GlyphRunDrawing.cs`
- `public sealed class GlyphRunDrawing : Drawing`
- `public static readonly StyledProperty<IBrush?> ForegroundProperty = AvaloniaProperty.Register<GlyphRunDrawing, IBrush?>(nameof(Foreground));`
- `public static readonly StyledProperty<GlyphRun?> GlyphRunProperty = AvaloniaProperty.Register<GlyphRunDrawing, GlyphRun?>(nameof(GlyphRun));`
- `public IBrush? Foreground {`
- `public GlyphRun? GlyphRun {`
- `public override Rect GetBounds() {`

### `src/Avalonia.Base/Media/GlyphRunMetrics.cs`
- `public readonly record struct GlyphRunMetrics`
- `public double Baseline { get; init; }`
- `public double Width { get; init; }`
- `public double WidthIncludingTrailingWhitespace { get; init; }`
- `public double Height { get; init; }`
- `public int TrailingWhitespaceLength { get; init; }`
- `public int NewLineLength { get; init; }`
- `public int FirstCluster { get; init; }`
- `public int LastCluster { get; init; }`

### `src/Avalonia.Base/Media/GradientBrush.cs`
- `public abstract class GradientBrush : Brush, IGradientBrush, IMutableBrush`
- `public static readonly StyledProperty<GradientSpreadMethod> SpreadMethodProperty = AvaloniaProperty.Register<GradientBrush, GradientSpreadMethod>(nameof(SpreadMethod));`
- `public static readonly StyledProperty<GradientStops> GradientStopsProperty = AvaloniaProperty.Register<GradientBrush, GradientStops>(nameof(GradientStops));`
- `public GradientSpreadMethod SpreadMethod {`
- `public GradientStops GradientStops {`
- `public abstract IImmutableBrush ToImmutable();`

### `src/Avalonia.Base/Media/GradientSpreadMethod.cs`
- `public enum GradientSpreadMethod`

### `src/Avalonia.Base/Media/GradientStop.cs`
- `public sealed class GradientStop : AvaloniaObject, IGradientStop`
- `public static readonly StyledProperty<double> OffsetProperty = AvaloniaProperty.Register<GradientStop, double>(nameof(Offset));`
- `public static readonly StyledProperty<Color> ColorProperty = AvaloniaProperty.Register<GradientStop, Color>(nameof(Color));`
- `public GradientStop() { }`
- `public GradientStop(Color color, double offset) {`
- `public double Offset {`
- `public Color Color {`

### `src/Avalonia.Base/Media/GradientStops.cs`
- `public class GradientStops : AvaloniaList<GradientStop>`
- `public GradientStops() {`
- `public IReadOnlyList<ImmutableGradientStop> ToImmutable() {`

### `src/Avalonia.Base/Media/IBrush.cs`
- `public interface IBrush`

### `src/Avalonia.Base/Media/IConicGradientBrush.cs`
- `public interface IConicGradientBrush : IGradientBrush`

### `src/Avalonia.Base/Media/IDashStyle.cs`
- `public interface IDashStyle`

### `src/Avalonia.Base/Media/IExperimentalAcrylicMaterial.cs`
- `public interface IExperimentalAcrylicMaterial`

### `src/Avalonia.Base/Media/IGlyphTypeface.cs`
- `public interface IGlyphTypeface : IDisposable`

### `src/Avalonia.Base/Media/IGradientBrush.cs`
- `public interface IGradientBrush : IBrush`

### `src/Avalonia.Base/Media/IGradientStop.cs`
- `public interface IGradientStop`

### `src/Avalonia.Base/Media/IImage.cs`
- `public interface IImage`

### `src/Avalonia.Base/Media/IImageBrush.cs`
- `public interface IImageBrush : ITileBrush`
- `public interface IImageBrushSource`

### `src/Avalonia.Base/Media/IImmutableBrush.cs`
- Namespace: `Avalonia.Media`
- `public interface IImmutableBrush : IBrush`

### `src/Avalonia.Base/Media/IImmutableGlyphRunReference.cs`
- Namespace: `Avalonia.Media`
- `public interface IImmutableGlyphRunReference : IDisposable`

### `src/Avalonia.Base/Media/ILinearGradientBrush.cs`
- `public interface ILinearGradientBrush : IGradientBrush`

### `src/Avalonia.Base/Media/IMutableExperimentalAcrylicMaterial.cs`
- `public interface IMutableExperimentalAcrylicMaterial : IExperimentalAcrylicMaterial`

### `src/Avalonia.Base/Media/IMutableTransform.cs`
- `public interface IMutableTransform : ITransform`

### `src/Avalonia.Base/Media/IPen.cs`
- `public interface IPen`

### `src/Avalonia.Base/Media/IRadialGradientBrush.cs`
- `public interface IRadialGradientBrush : IGradientBrush`

### `src/Avalonia.Base/Media/ISceneBrush.cs`
- `public interface ISceneBrush : ITileBrush`
- `public interface ISceneBrushContent : IImmutableBrush, IDisposable`

### `src/Avalonia.Base/Media/ISolidColorBrush.cs`
- `public interface ISolidColorBrush : IBrush`
- `public interface IImmutableSolidColorBrush : ISolidColorBrush, IImmutableBrush`

### `src/Avalonia.Base/Media/ITileBrush.cs`
- `public interface ITileBrush : IBrush`

### `src/Avalonia.Base/Media/ITransform.cs`
- `public interface ITransform`

### `src/Avalonia.Base/Media/ImageBrush.cs`
- `public sealed class ImageBrush : TileBrush, IImageBrush, IMutableBrush`
- `public static readonly StyledProperty<IImageBrushSource?> SourceProperty = AvaloniaProperty.Register<ImageBrush, IImageBrushSource?>(nameof(Source));`
- `public ImageBrush() {`
- `public ImageBrush(IImageBrushSource? source) {`
- `public IImageBrushSource? Source {`
- `public IImmutableBrush ToImmutable() {`

### `src/Avalonia.Base/Media/ImageDrawing.cs`
- `public sealed class ImageDrawing : Drawing`
- `public static readonly StyledProperty<IImage?> ImageSourceProperty = AvaloniaProperty.Register<ImageDrawing, IImage?>(nameof(ImageSource));`
- `public static readonly StyledProperty<Rect> RectProperty = AvaloniaProperty.Register<ImageDrawing, Rect>(nameof(Rect));`
- `public IImage? ImageSource {`
- `public Rect Rect {`
- `public override Rect GetBounds() => Rect;`

### `src/Avalonia.Base/Media/Imaging/Bitmap.cs`
- `public class Bitmap : IBitmap, IImageBrushSource`
- `public static Bitmap DecodeToWidth(Stream stream, int width, BitmapInterpolationMode interpolationMode = BitmapInterpolationMode.HighQuality) {`
- `public static Bitmap DecodeToHeight(Stream stream, int height, BitmapInterpolationMode interpolationMode = BitmapInterpolationMode.HighQuality) {`
- `public Bitmap CreateScaledBitmap(PixelSize destinationSize, BitmapInterpolationMode interpolationMode = BitmapInterpolationMode.HighQuality) {`
- `public Bitmap(string fileName) {`
- `public Bitmap(Stream stream) {`
- `public virtual void Dispose() {`
- `public Bitmap(PixelFormat format, AlphaFormat alphaFormat, IntPtr data, PixelSize size, Vector dpi, int stride) {`
- `public Vector Dpi => PlatformImpl.Item.Dpi;`
- `public Size Size => PlatformImpl.Item.PixelSize.ToSizeWithDpi(Dpi);`
- `public PixelSize PixelSize => PlatformImpl.Item.PixelSize;`
- `public void Save(string fileName, int? quality = null) {`
- `public void Save(Stream stream, int? quality = null) {`
- `public virtual PixelFormat? Format => (PlatformImpl.Item as IReadableBitmapImpl)?.Format;`
- `public virtual AlphaFormat? AlphaFormat => (PlatformImpl.Item as IReadableBitmapWithAlphaImpl)?.AlphaFormat;`
- `public virtual void CopyPixels(PixelRect sourceRect, IntPtr buffer, int bufferSize, int stride) {`
- `public void CopyPixels(ILockedFramebuffer buffer, AlphaFormat alphaFormat) {`

### `src/Avalonia.Base/Media/Imaging/BitmapBlendingMode.cs`
- `public enum BitmapBlendingMode : byte`

### `src/Avalonia.Base/Media/Imaging/BitmapInterpolationMode.cs`
- `public enum BitmapInterpolationMode : byte`

### `src/Avalonia.Base/Media/Imaging/CroppedBitmap.cs`
- `public class CroppedBitmap : AvaloniaObject, IImage, IAffectsRender, IDisposable`
- `public static readonly StyledProperty<IImage?> SourceProperty = AvaloniaProperty.Register<CroppedBitmap, IImage?>(nameof(Source));`
- `public static readonly StyledProperty<PixelRect> SourceRectProperty = AvaloniaProperty.Register<CroppedBitmap, PixelRect>(nameof(SourceRect));`
- `public event EventHandler? Invalidated;`
- `public IImage? Source {`
- `public PixelRect SourceRect {`
- `public CroppedBitmap() {`
- `public CroppedBitmap(IImage source, PixelRect sourceRect) {`
- `public virtual void Dispose() {`
- `public Size Size {`
- `public void Draw(DrawingContext context, Rect sourceRect, Rect destRect) {`

### `src/Avalonia.Base/Media/Imaging/RenderTargetBitmap.cs`
- `public class RenderTargetBitmap : Bitmap`
- `public RenderTargetBitmap(PixelSize pixelSize) : this(pixelSize, new Vector(96, 96)) {`
- `public RenderTargetBitmap(PixelSize pixelSize, Vector dpi) : this(RefCountable.Create(CreateImpl(pixelSize, dpi))) {`
- `public void Render(Visual visual) {`
- `public DrawingContext CreateDrawingContext() => CreateDrawingContext(true);`
- `public DrawingContext CreateDrawingContext(bool clear) {`
- `public override void Dispose() {`

### `src/Avalonia.Base/Media/Imaging/WriteableBitmap.cs`
- `public class WriteableBitmap : Bitmap`
- `public WriteableBitmap(PixelSize size, Vector dpi, PixelFormat? format = null, AlphaFormat? alphaFormat = null) : this(CreatePlatformImpl(size, dpi, format, alphaFormat)) {`
- `public unsafe WriteableBitmap(PixelFormat format, AlphaFormat alphaFormat, IntPtr data, PixelSize size, Vector dpi, int stride) : this(size, dpi, format, alphaFormat) {`
- `public override PixelFormat? Format => _pixelFormatMemory?.Format ?? base.Format;`
- `public ILockedFramebuffer Lock() {`
- `public override void CopyPixels(PixelRect sourceRect, IntPtr buffer, int bufferSize, int stride) {`
- `public static WriteableBitmap Decode(Stream stream) {`
- `public new static WriteableBitmap DecodeToWidth(Stream stream, int width, BitmapInterpolationMode interpolationMode = BitmapInterpolationMode.HighQuality) {`
- `public new static WriteableBitmap DecodeToHeight(Stream stream, int height, BitmapInterpolationMode interpolationMode = BitmapInterpolationMode.HighQuality) {`

### `src/Avalonia.Base/Media/ImmediateDrawingContext.cs`
- `public sealed class ImmediateDrawingContext : IDisposable, IOptionalFeatureProvider`
- `public IDrawingContextImpl PlatformImpl { get; }`
- `public Matrix CurrentTransform {`
- `public void DrawBitmap(Bitmap source, Rect rect) {`
- `public void DrawBitmap(Bitmap source, Rect sourceRect, Rect destRect) {`
- `public void DrawLine(ImmutablePen pen, Point p1, Point p2) {`
- `public void DrawRectangle(IImmutableBrush? brush, ImmutablePen? pen, Rect rect, double radiusX = 0, double radiusY = 0, BoxShadows boxShadows = default) {`
- `public void DrawRectangle(ImmutablePen pen, Rect rect, float cornerRadius = 0.0f) {`
- `public void DrawEllipse(IImmutableBrush? brush, ImmutablePen? pen, Point center, double radiusX, double radiusY) {`
- `public void DrawGlyphRun(IImmutableBrush foreground, IImmutableGlyphRunReference glyphRun) {`
- `public void FillRectangle(IImmutableBrush brush, Rect rect, float cornerRadius = 0.0f) {`
- `public readonly record struct PushedState : IDisposable`
- `public enum PushedStateType`
- `public void Dispose() {`
- `public PushedState PushClip(RoundedRect clip) {`
- `public PushedState PushClip(Rect clip) {`
- `public PushedState PushOpacity(double opacity, Rect bounds) {`
- `public PushedState PushOpacityMask(IImmutableBrush mask, Rect bounds) {`
- `public PushedState PushPostTransform(Matrix matrix) => PushSetTransform(CurrentTransform * matrix);`
- `public PushedState PushPreTransform(Matrix matrix) => PushSetTransform(matrix * CurrentTransform);`
- `public PushedState PushSetTransform(Matrix matrix) {`
- `public PushedState PushTransformContainer() {`
- `public void Dispose() {`
- `public object? TryGetFeature(Type type) => PlatformImpl.GetFeature(type);`

### `src/Avalonia.Base/Media/Immutable/ImmutableConicGradientBrush.cs`
- `public class ImmutableConicGradientBrush : ImmutableGradientBrush, IConicGradientBrush`
- `public ImmutableConicGradientBrush( IReadOnlyList<ImmutableGradientStop> gradientStops, double opacity = 1, ImmutableTransform? transform = null, RelativePoint? transformOrigin = null, GradientSpreadMethod spreadMethod = GradientSpreadMethod.Pad, RelativePoint? center = null, double angle = 0) : base(gradientStops, opacity, transform, transformOrigin, spreadMethod) {`
- `public ImmutableConicGradientBrush(ConicGradientBrush source) : base(source) {`
- `public RelativePoint Center { get; }`
- `public double Angle { get; }`

### `src/Avalonia.Base/Media/Immutable/ImmutableDashStyle.cs`
- `public class ImmutableDashStyle : IDashStyle, IEquatable<IDashStyle>`
- `public ImmutableDashStyle(IEnumerable<double>? dashes, double offset) {`
- `public IReadOnlyList<double> Dashes => _dashes;`
- `public double Offset { get; }`
- `public override bool Equals(object? obj) => Equals(obj as IDashStyle);`
- `public bool Equals(IDashStyle? other) {`
- `public override int GetHashCode() {`

### `src/Avalonia.Base/Media/Immutable/ImmutableGradientBrush.cs`
- `public abstract class ImmutableGradientBrush : IGradientBrush, IImmutableBrush`
- `public IReadOnlyList<IGradientStop> GradientStops { get; }`
- `public double Opacity { get; }`
- `public ITransform? Transform { get; }`
- `public RelativePoint TransformOrigin { get; }`
- `public GradientSpreadMethod SpreadMethod { get; }`

### `src/Avalonia.Base/Media/Immutable/ImmutableGradientStop.cs`
- `public class ImmutableGradientStop : IGradientStop`
- `public ImmutableGradientStop(double offset, Color color) {`
- `public double Offset { get; }`
- `public Color Color { get; }`

### `src/Avalonia.Base/Media/Immutable/ImmutableLinearGradientBrush.cs`
- `public class ImmutableLinearGradientBrush : ImmutableGradientBrush, ILinearGradientBrush`
- `public ImmutableLinearGradientBrush( IReadOnlyList<ImmutableGradientStop> gradientStops, double opacity = 1, ImmutableTransform? transform = null, RelativePoint? transformOrigin = null, GradientSpreadMethod spreadMethod = GradientSpreadMethod.Pad, RelativePoint? startPoint = null, RelativePoint? endPoint = null) : base(gradientStops, opacity, transform, transformOrigin, spreadMethod) {`
- `public ImmutableLinearGradientBrush(LinearGradientBrush source) : base(source) {`
- `public RelativePoint StartPoint { get; }`
- `public RelativePoint EndPoint { get; }`

### `src/Avalonia.Base/Media/Immutable/ImmutablePen.cs`
- `public class ImmutablePen : IPen, IEquatable<IPen>`
- `public ImmutablePen( uint color, double thickness = 1.0, ImmutableDashStyle? dashStyle = null, PenLineCap lineCap = PenLineCap.Flat, PenLineJoin lineJoin = PenLineJoin.Miter, double miterLimit = 10.0) : this(new ImmutableSolidColorBrush(color), thickness, dashStyle, lineCap, lineJoin, miterLimit) {`
- `public ImmutablePen( IImmutableBrush? brush, double thickness = 1.0, ImmutableDashStyle? dashStyle = null, PenLineCap lineCap = PenLineCap.Flat, PenLineJoin lineJoin = PenLineJoin.Miter, double miterLimit = 10.0) {`
- `public IBrush? Brush { get; }`
- `public double Thickness { get; }`
- `public IDashStyle? DashStyle { get; }`
- `public PenLineCap LineCap { get; }`
- `public PenLineJoin LineJoin { get; }`
- `public double MiterLimit { get; }`
- `public override bool Equals(object? obj) => Equals(obj as IPen);`
- `public bool Equals(IPen? other) {`
- `public override int GetHashCode() {`

### `src/Avalonia.Base/Media/Immutable/ImmutableRadialGradientBrush.cs`
- `public class ImmutableRadialGradientBrush : ImmutableGradientBrush, IRadialGradientBrush`
- `public ImmutableRadialGradientBrush( IReadOnlyList<ImmutableGradientStop> gradientStops, double opacity = 1, ImmutableTransform? transform = null, RelativePoint? transformOrigin = null, GradientSpreadMethod spreadMethod = GradientSpreadMethod.Pad, RelativePoint? center = null, RelativePoint? gradientOrigin = null, double radius = 0.5) : this(gradientStops, opacity, transform, transformOrigin, spreadMethod, center, gradientOrigin, new RelativeScalar(radius, RelativeUnit.Relative), new RelativeScalar(radius, RelativeUnit.Relative) ) {`
- `public ImmutableRadialGradientBrush( IReadOnlyList<ImmutableGradientStop> gradientStops, double opacity = 1, ImmutableTransform? transform = null, RelativePoint? transformOrigin = null, GradientSpreadMethod spreadMethod = GradientSpreadMethod.Pad, RelativePoint? center = null, RelativePoint? gradientOrigin = null, RelativeScalar? radiusX = null, RelativeScalar? radiusY = null ) : base(gradientStops, opacity, transform, transformOrigin, spreadMethod) {`
- `public ImmutableRadialGradientBrush(RadialGradientBrush source) : base(source) {`
- `public RelativePoint Center { get; }`
- `public RelativePoint GradientOrigin { get; }`
- `public RelativeScalar RadiusX { get; }`
- `public RelativeScalar RadiusY { get; }`

### `src/Avalonia.Base/Media/Immutable/ImmutableSolidColorBrush.cs`
- `public class ImmutableSolidColorBrush : IImmutableSolidColorBrush, IEquatable<ImmutableSolidColorBrush>`
- `public ImmutableSolidColorBrush(Color color, double opacity = 1, ImmutableTransform? transform = null) {`
- `public ImmutableSolidColorBrush(uint color) : this(Color.FromUInt32(color)) {`
- `public ImmutableSolidColorBrush(ISolidColorBrush source) : this(source.Color, source.Opacity, source.Transform?.ToImmutable()) {`
- `public Color Color { get; }`
- `public double Opacity { get; }`
- `public ITransform? Transform { get; }`
- `public RelativePoint TransformOrigin { get; }`
- `public bool Equals(ImmutableSolidColorBrush? other) {`
- `public override bool Equals(object? obj) {`
- `public override int GetHashCode() {`
- `public static bool operator ==(ImmutableSolidColorBrush left, ImmutableSolidColorBrush right) {`
- `public static bool operator !=(ImmutableSolidColorBrush left, ImmutableSolidColorBrush right) {`
- `public override string ToString() {`

### `src/Avalonia.Base/Media/Immutable/ImmutableTextDecoration.cs`
- `public class ImmutableTextDecoration`
- `public ImmutableTextDecoration(TextDecorationLocation location, ImmutablePen pen, TextDecorationUnit penThicknessUnit, double penOffset, TextDecorationUnit penOffsetUnit) {`
- `public TextDecorationLocation Location { get; }`
- `public ImmutablePen Pen { get; }`
- `public TextDecorationUnit PenThicknessUnit { get; }`
- `public double PenOffset { get; }`
- `public TextDecorationUnit PenOffsetUnit { get; }`

### `src/Avalonia.Base/Media/Immutable/ImmutableTileBrush.cs`
- `public abstract class ImmutableTileBrush : ITileBrush, IImmutableBrush`
- `public AlignmentX AlignmentX { get; }`
- `public AlignmentY AlignmentY { get; }`
- `public RelativeRect DestinationRect { get; }`
- `public double Opacity { get; }`
- `public ITransform? Transform { get; }`
- `public RelativePoint TransformOrigin { get; }`
- `public RelativeRect SourceRect { get; }`
- `public Stretch Stretch { get; }`
- `public TileMode TileMode { get; }`

### `src/Avalonia.Base/Media/Immutable/ImmutableTransform.cs`
- `public class ImmutableTransform : ITransform`
- `public Matrix Value { get; }`
- `public ImmutableTransform(Matrix matrix) {`

### `src/Avalonia.Base/Media/ImmutableExperimentalAcrylicMaterial.cs`
- `public readonly struct ImmutableExperimentalAcrylicMaterial : IExperimentalAcrylicMaterial, IEquatable<ImmutableExperimentalAcrylicMaterial>`
- `public ImmutableExperimentalAcrylicMaterial(IExperimentalAcrylicMaterial brush) {`
- `public AcrylicBackgroundSource BackgroundSource { get; }`
- `public Color TintColor { get; }`
- `public Color MaterialColor { get; }`
- `public double TintOpacity { get; }`
- `public Color FallbackColor { get; }`
- `public bool Equals(ImmutableExperimentalAcrylicMaterial other) {`
- `public override bool Equals(object? obj) {`
- `public Color GetEffectiveTintColor() {`
- `public override int GetHashCode() {`
- `public static bool operator ==(ImmutableExperimentalAcrylicMaterial left, ImmutableExperimentalAcrylicMaterial right) {`
- `public static bool operator !=(ImmutableExperimentalAcrylicMaterial left, ImmutableExperimentalAcrylicMaterial right) {`

### `src/Avalonia.Base/Media/LineGeometry.cs`
- `public class LineGeometry : Geometry`
- `public static readonly StyledProperty<Point> StartPointProperty = AvaloniaProperty.Register<LineGeometry, Point>(nameof(StartPoint));`
- `public static readonly StyledProperty<Point> EndPointProperty = AvaloniaProperty.Register<LineGeometry, Point>(nameof(EndPoint));`
- `public LineGeometry() {`
- `public LineGeometry(Point startPoint, Point endPoint) : this() {`
- `public Point StartPoint {`
- `public Point EndPoint {`
- `public override Geometry Clone() {`

### `src/Avalonia.Base/Media/LineSegment.cs`
- `public sealed class LineSegment : PathSegment`
- `public static readonly StyledProperty<Point> PointProperty = AvaloniaProperty.Register<LineSegment, Point>(nameof(Point));`
- `public Point Point {`
- `public override string ToString() => FormattableString.Invariant($"L {Point}");`

### `src/Avalonia.Base/Media/LinearGradientBrush.cs`
- `public sealed class LinearGradientBrush : GradientBrush, ILinearGradientBrush`
- `public static readonly StyledProperty<RelativePoint> StartPointProperty = AvaloniaProperty.Register<LinearGradientBrush, RelativePoint>( nameof(StartPoint), RelativePoint.TopLeft);`
- `public static readonly StyledProperty<RelativePoint> EndPointProperty = AvaloniaProperty.Register<LinearGradientBrush, RelativePoint>( nameof(EndPoint), RelativePoint.BottomRight);`
- `public RelativePoint StartPoint {`
- `public RelativePoint EndPoint {`
- `public override IImmutableBrush ToImmutable() {`

### `src/Avalonia.Base/Media/MaterialExtensions.cs`
- `public static class MaterialExtensions`
- `public static IExperimentalAcrylicMaterial ToImmutable(this IExperimentalAcrylicMaterial material) {`

### `src/Avalonia.Base/Media/MatrixTransform.cs`
- `public sealed class MatrixTransform : Transform`
- `public static readonly StyledProperty<Matrix> MatrixProperty = AvaloniaProperty.Register<MatrixTransform, Matrix>(nameof(Matrix), Matrix.Identity);`
- `public MatrixTransform() {`
- `public MatrixTransform(Matrix matrix) : this() {`
- `public Matrix Matrix {`
- `public override Matrix Value => Matrix;`

### `src/Avalonia.Base/Media/MediaExtensions.cs`
- `public static class MediaExtensions`
- `public static Vector CalculateScaling( this Stretch stretch, Size destinationSize, Size sourceSize, StretchDirection stretchDirection = StretchDirection.Both) {`
- `public static Size CalculateSize( this Stretch stretch, Size destinationSize, Size sourceSize, StretchDirection stretchDirection = StretchDirection.Both) {`

### `src/Avalonia.Base/Media/PathFigure.cs`
- `public sealed class PathFigure : AvaloniaObject`
- `public static readonly StyledProperty<bool> IsClosedProperty = AvaloniaProperty.Register<PathFigure, bool>(nameof(IsClosed), true);`
- `public static readonly StyledProperty<bool> IsFilledProperty = AvaloniaProperty.Register<PathFigure, bool>(nameof(IsFilled), true);`
- `public static readonly DirectProperty<PathFigure, PathSegments?> SegmentsProperty = AvaloniaProperty.RegisterDirect<PathFigure, PathSegments?>( nameof(Segments), f => f.Segments,`
- `public static readonly StyledProperty<Point> StartPointProperty = AvaloniaProperty.Register<PathFigure, Point>(nameof(StartPoint));`
- `public PathFigure() {`
- `public bool IsClosed {`
- `public bool IsFilled {`
- `public PathSegments? Segments {`
- `public Point StartPoint {`
- `public override string ToString() => FormattableString.Invariant($"M {StartPoint} {string.Join(" ", _segments ?? Enumerable.Empty<PathSegment>())}{(IsClosed ? "Z" : "")}");`

### `src/Avalonia.Base/Media/PathGeometry.cs`
- `public class PathGeometry : StreamGeometry`
- `public static readonly DirectProperty<PathGeometry, PathFigures?> FiguresProperty = AvaloniaProperty.RegisterDirect<PathGeometry, PathFigures?>(nameof(Figures), g => g.Figures, (g, f) => g.Figures = f);`
- `public static readonly StyledProperty<FillRule> FillRuleProperty = AvaloniaProperty.Register<PathGeometry, FillRule>(nameof(FillRule));`
- `public PathGeometry() {`
- `public new static PathGeometry Parse(string pathData) {`
- `public PathFigures? Figures {`
- `public FillRule FillRule {`
- `public override string ToString() {`

### `src/Avalonia.Base/Media/PathGeometryCollections.cs`
- `public sealed class PathFigures : AvaloniaList<PathFigure>`
- `public static PathFigures Parse(string pathData) {`
- `public sealed class PathSegments : AvaloniaList<PathSegment>`
- `public PathSegments() {`
- `public PathSegments(IEnumerable<PathSegment> collection) : base(collection) {`
- `public PathSegments(int capacity) : base(capacity) {`

### `src/Avalonia.Base/Media/PathMarkupParser.cs`
- `public class PathMarkupParser : IDisposable`
- `public PathMarkupParser(IGeometryContext geometryContext) {`
- `public void Parse(string pathData) {`

### `src/Avalonia.Base/Media/PathSegment.cs`
- `public abstract class PathSegment : AvaloniaObject`
- `public static readonly StyledProperty<bool> IsStrokedProperty = AvaloniaProperty.Register<PathSegment, bool>(nameof(IsStroked), true);`
- `public bool IsStroked {`

### `src/Avalonia.Base/Media/Pen.cs`
- `public sealed class Pen : AvaloniaObject, IPen, ICompositionRenderResource<IPen>, ICompositorSerializable`
- `public static readonly StyledProperty<IBrush?> BrushProperty = AvaloniaProperty.Register<Pen, IBrush?>(nameof(Brush));`
- `public static readonly StyledProperty<double> ThicknessProperty = AvaloniaProperty.Register<Pen, double>(nameof(Thickness), 1.0);`
- `public static readonly StyledProperty<IDashStyle?> DashStyleProperty = AvaloniaProperty.Register<Pen, IDashStyle?>(nameof(DashStyle));`
- `public static readonly StyledProperty<PenLineCap> LineCapProperty = AvaloniaProperty.Register<Pen, PenLineCap>(nameof(LineCap));`
- `public static readonly StyledProperty<PenLineJoin> LineJoinProperty = AvaloniaProperty.Register<Pen, PenLineJoin>(nameof(LineJoin));`
- `public static readonly StyledProperty<double> MiterLimitProperty = AvaloniaProperty.Register<Pen, double>(nameof(MiterLimit), 10.0);`
- `public Pen() { }`
- `public Pen( uint color, double thickness = 1.0, IDashStyle? dashStyle = null, PenLineCap lineCap = PenLineCap.Flat, PenLineJoin lineJoin = PenLineJoin.Miter, double miterLimit = 10.0) : this(new SolidColorBrush(color), thickness, dashStyle, lineCap, lineJoin, miterLimit) { }`
- `public Pen( IBrush? brush, double thickness = 1.0, IDashStyle? dashStyle = null, PenLineCap lineCap = PenLineCap.Flat, PenLineJoin lineJoin = PenLineJoin.Miter, double miterLimit = 10.0) {`
- `public IBrush? Brush {`
- `public double Thickness {`
- `public IDashStyle? DashStyle {`
- `public PenLineCap LineCap {`
- `public PenLineJoin LineJoin {`
- `public double MiterLimit {`
- `public ImmutablePen ToImmutable() {`

### `src/Avalonia.Base/Media/PenLineCap.cs`
- `public enum PenLineCap`

### `src/Avalonia.Base/Media/PenLineJoin.cs`
- `public enum PenLineJoin`

### `src/Avalonia.Base/Media/PolyBezierSegment.cs`
- Namespace: `Avalonia.Media`
- `public sealed class PolyBezierSegment : PathSegment`
- `public static readonly DirectProperty<PolyBezierSegment, Points?> PointsProperty = AvaloniaProperty.RegisterDirect<PolyBezierSegment, Points?>(nameof(Points), o => o.Points,`
- `public PolyBezierSegment() {`
- `public PolyBezierSegment(IEnumerable<Point> points, bool isStroked) {`
- `public Points? Points {`
- `public override string ToString() {`

### `src/Avalonia.Base/Media/PolyLineSegment.cs`
- `public sealed class PolyLineSegment : PathSegment`
- `public static readonly StyledProperty<IList<Point>> PointsProperty = AvaloniaProperty.Register<PolyLineSegment, IList<Point>>(nameof(Points));`
- `public IList<Point> Points {`
- `public PolyLineSegment() {`
- `public PolyLineSegment(IEnumerable<Point> points) {`
- `public override string ToString() => Points.Count >= 1 ? "L " + string.Join(" ", Points) : "";`

### `src/Avalonia.Base/Media/PolylineGeometry.cs`
- `public class PolylineGeometry : Geometry`
- `public static readonly DirectProperty<PolylineGeometry, IList<Point>> PointsProperty = AvaloniaProperty.RegisterDirect<PolylineGeometry, IList<Point>>(nameof(Points), g => g.Points, (g, f) => g.Points = f);`
- `public static readonly StyledProperty<bool> IsFilledProperty = AvaloniaProperty.Register<PolylineGeometry, bool>(nameof(IsFilled));`
- `public PolylineGeometry() {`
- `public PolylineGeometry(IEnumerable<Point> points, bool isFilled) {`
- `public PolylineGeometry(IEnumerable<Point> points, bool isFilled, FillRule fillRule) {`
- `public IList<Point> Points {`
- `public bool IsFilled {`
- `public FillRule FillRule => _fillRule;`
- `public override Geometry Clone() {`

### `src/Avalonia.Base/Media/PreciseEllipticArcHelper.cs`
- `public sealed class EllipticalArc`
- `public bool DrawInOppositeDirection { get; set; }`
- `public EllipticalArc() {`
- `public EllipticalArc(Point center, double a, double b, double theta, double lambda1, double lambda2, bool isPieSlice) : this(center.X, center.Y, a, b, theta, lambda1, lambda2, isPieSlice) {`
- `public EllipticalArc(double cx, double cy, double a, double b, double theta, double lambda1, double lambda2, bool isPieSlice) {`
- `public EllipticalArc(Point center, double a, double b, double theta) : this(center.X, center.Y, a, b, theta) {`
- `public EllipticalArc(double cx, double cy, double a, double b, double theta) {`
- `public void SetMaxDegree(int maxDegree) {`
- `public void SetDefaultFlatness(double defaultFlatness) {`
- `public double EstimateError(int degree, double etaA, double etaB) {`
- `public Point PointAt(double lambda) {`
- `public bool Contains(double x, double y) {`
- `public bool Contains(double x, double y, double w, double h) {`
- `public bool Contains(Point p) {`
- `public bool Contains(Rect r) {`
- `public Rect GetBounds() {`
- `public void BuildArc(StreamGeometryContext path) {`
- `public void BuildArc(StreamGeometryContext path, int degree, double threshold, bool openNewFigure) {`
- `public static void BuildArc(StreamGeometryContext path, Point p1, Point p2, Size size, double theta, bool isLargeArc, bool clockwise) {`
- `public bool Intersects(double x, double y, double w, double h) {`
- `public bool Intersects(Rect r) {`

### `src/Avalonia.Base/Media/QuadraticBezierSegment .cs`
- `public sealed class QuadraticBezierSegment : PathSegment`
- `public static readonly StyledProperty<Point> Point1Property = AvaloniaProperty.Register<QuadraticBezierSegment, Point>(nameof(Point1));`
- `public static readonly StyledProperty<Point> Point2Property = AvaloniaProperty.Register<QuadraticBezierSegment, Point>(nameof(Point2));`
- `public Point Point1 {`
- `public Point Point2 {`
- `public override string ToString() => FormattableString.Invariant($"Q {Point1} {Point2}");`

### `src/Avalonia.Base/Media/RadialGradientBrush.cs`
- `public sealed class RadialGradientBrush : GradientBrush, IRadialGradientBrush`
- `public static readonly StyledProperty<RelativePoint> CenterProperty = AvaloniaProperty.Register<RadialGradientBrush, RelativePoint>( nameof(Center), RelativePoint.Center);`
- `public static readonly StyledProperty<RelativePoint> GradientOriginProperty = AvaloniaProperty.Register<RadialGradientBrush, RelativePoint>( nameof(GradientOrigin), RelativePoint.Center);`
- `public static readonly StyledProperty<double> RadiusProperty = AvaloniaProperty.Register<RadialGradientBrush, double>( nameof(Radius), 0.5);`
- `public static readonly StyledProperty<RelativeScalar> RadiusXProperty = AvaloniaProperty.Register<RadialGradientBrush, RelativeScalar>( nameof(RadiusX), RelativeScalar.Middle);`
- `public static readonly StyledProperty<RelativeScalar> RadiusYProperty = AvaloniaProperty.Register<RadialGradientBrush, RelativeScalar>( nameof(RadiusY), RelativeScalar.Middle);`
- `public RelativePoint Center {`
- `public RelativePoint GradientOrigin {`
- `public RelativeScalar RadiusX {`
- `public RelativeScalar RadiusY {`
- `public double Radius {`
- `public override IImmutableBrush ToImmutable() {`

### `src/Avalonia.Base/Media/RectangleGeometry.cs`
- `public class RectangleGeometry : Geometry`
- `public static readonly StyledProperty<double> RadiusXProperty = AvaloniaProperty.Register<RectangleGeometry, double>(nameof(RadiusX));`
- `public static readonly StyledProperty<double> RadiusYProperty = AvaloniaProperty.Register<RectangleGeometry, double>(nameof(RadiusY));`
- `public static readonly StyledProperty<Rect> RectProperty = AvaloniaProperty.Register<RectangleGeometry, Rect>(nameof(Rect));`
- `public RectangleGeometry() {`
- `public RectangleGeometry(Rect rect) {`
- `public RectangleGeometry(Rect rect, double radiusX, double radiusY) {`
- `public double RadiusX {`
- `public double RadiusY {`
- `public Rect Rect {`
- `public override Geometry Clone() => new RectangleGeometry(Rect, RadiusX, RadiusY);`

### `src/Avalonia.Base/Media/RenderOptions.cs`
- `public readonly record struct RenderOptions`
- `public BitmapInterpolationMode BitmapInterpolationMode { get; init; }`
- `public EdgeMode EdgeMode { get; init; }`
- `public TextRenderingMode TextRenderingMode { get; init; }`
- `public BitmapBlendingMode BitmapBlendingMode { get; init; }`
- `public bool? RequiresFullOpacityHandling { get; init; }`
- `public static BitmapInterpolationMode GetBitmapInterpolationMode(Visual visual) {`
- `public static void SetBitmapInterpolationMode(Visual visual, BitmapInterpolationMode value) {`
- `public static BitmapBlendingMode GetBitmapBlendingMode(Visual visual) {`
- `public static void SetBitmapBlendingMode(Visual visual, BitmapBlendingMode value) {`
- `public static EdgeMode GetEdgeMode(Visual visual) {`
- `public static void SetEdgeMode(Visual visual, EdgeMode value) {`
- `public static TextRenderingMode GetTextRenderingMode(Visual visual) {`
- `public static void SetTextRenderingMode(Visual visual, TextRenderingMode value) {`
- `public static bool? GetRequiresFullOpacityHandling(Visual visual) {`
- `public static void SetRequiresFullOpacityHandling(Visual visual, bool? value) {`
- `public RenderOptions MergeWith(RenderOptions other) {`

### `src/Avalonia.Base/Media/RotateTransform.cs`
- `public sealed class RotateTransform : Transform`
- `public static readonly StyledProperty<double> AngleProperty = AvaloniaProperty.Register<RotateTransform, double>(nameof(Angle));`
- `public static readonly StyledProperty<double> CenterXProperty = AvaloniaProperty.Register<RotateTransform, double>(nameof(CenterX));`
- `public static readonly StyledProperty<double> CenterYProperty = AvaloniaProperty.Register<RotateTransform, double>(nameof(CenterY));`
- `public RotateTransform() {`
- `public RotateTransform(double angle) : this() {`
- `public RotateTransform(double angle, double centerX, double centerY) : this() {`
- `public double Angle {`
- `public double CenterX {`
- `public double CenterY {`
- `public override Matrix Value => Matrix.CreateTranslation(-CenterX, -CenterY) *`

### `src/Avalonia.Base/Media/ScaleTransform.cs`
- `public sealed class ScaleTransform : Transform`
- `public static readonly StyledProperty<double> ScaleXProperty = AvaloniaProperty.Register<ScaleTransform, double>(nameof(ScaleX), 1);`
- `public static readonly StyledProperty<double> ScaleYProperty = AvaloniaProperty.Register<ScaleTransform, double>(nameof(ScaleY), 1);`
- `public ScaleTransform() {`
- `public ScaleTransform(double scaleX, double scaleY) : this() {`
- `public double ScaleX {`
- `public double ScaleY {`
- `public override Matrix Value => Matrix.CreateScale(ScaleX, ScaleY);`

### `src/Avalonia.Base/Media/SkewTransform.cs`
- `public sealed class SkewTransform : Transform`
- `public static readonly StyledProperty<double> AngleXProperty = AvaloniaProperty.Register<SkewTransform, double>(nameof(AngleX));`
- `public static readonly StyledProperty<double> AngleYProperty = AvaloniaProperty.Register<SkewTransform, double>(nameof(AngleY));`
- `public SkewTransform() {`
- `public SkewTransform(double angleX, double angleY) : this() {`
- `public double AngleX {`
- `public double AngleY {`
- `public override Matrix Value => Matrix.CreateSkew(Matrix.ToRadians(AngleX), Matrix.ToRadians(AngleY));`

### `src/Avalonia.Base/Media/SolidColorBrush.cs`
- `public sealed class SolidColorBrush : Brush, ISolidColorBrush, IMutableBrush`
- `public static readonly StyledProperty<Color> ColorProperty = AvaloniaProperty.Register<SolidColorBrush, Color>(nameof(Color));`
- `public SolidColorBrush() {`
- `public SolidColorBrush(Color color, double opacity = 1) {`
- `public SolidColorBrush(uint color) : this(Color.FromUInt32(color)) {`
- `public Color Color {`
- `public static new SolidColorBrush Parse(string s) {`
- `public override string ToString() {`
- `public IImmutableBrush ToImmutable() {`

### `src/Avalonia.Base/Media/StreamGeometry.cs`
- `public class StreamGeometry : Geometry`
- `public StreamGeometry() {`
- `public new static StreamGeometry Parse(string s) {`
- `public override Geometry Clone() {`
- `public StreamGeometryContext Open() {`

### `src/Avalonia.Base/Media/StreamGeometryContext.cs`
- `public class StreamGeometryContext : IGeometryContext, IGeometryContext2`
- `public StreamGeometryContext(IStreamGeometryContextImpl impl) {`
- `public void SetFillRule(FillRule fillRule) {`
- `public void ArcTo(Point point, Size size, double rotationAngle, bool isLargeArc, SweepDirection sweepDirection) {`
- `public void PreciseArcTo(Point point, Size size, double rotationAngle, bool isLargeArc, SweepDirection sweepDirection) {`
- `public void BeginFigure(Point startPoint, bool isFilled) {`
- `public void CubicBezierTo(Point controlPoint1, Point controlPoint2, Point endPoint) {`
- `public void QuadraticBezierTo(Point controlPoint , Point endPoint) {`
- `public void LineTo(Point endPoint) {`
- `public void EndFigure(bool isClosed) {`
- `public void Dispose() {`
- `public void LineTo(Point point, bool isStroked) {`
- `public void ArcTo(Point point, Size size, double rotationAngle, bool isLargeArc, SweepDirection sweepDirection, bool isStroked) {`
- `public void CubicBezierTo(Point controlPoint1, Point controlPoint2, Point endPoint, bool isStroked) {`
- `public void QuadraticBezierTo(Point controlPoint, Point endPoint, bool isStroked) {`

### `src/Avalonia.Base/Media/Stretch.cs`
- `public enum Stretch`

### `src/Avalonia.Base/Media/StretchDirection.cs`
- `public enum StretchDirection`

### `src/Avalonia.Base/Media/SweepDirection.cs`
- `public enum SweepDirection`

### `src/Avalonia.Base/Media/TextAlignment.cs`
- `public enum TextAlignment`

### `src/Avalonia.Base/Media/TextCollapsingCreateInfo.cs`
- `public readonly record struct TextCollapsingCreateInfo`
- `public readonly double Width;`
- `public readonly TextRunProperties TextRunProperties;`
- `public readonly FlowDirection FlowDirection;`
- `public TextCollapsingCreateInfo(double width, TextRunProperties textRunProperties, FlowDirection flowDirection) {`

### `src/Avalonia.Base/Media/TextDecoration.cs`
- `public class TextDecoration : AvaloniaObject`
- `public static readonly StyledProperty<TextDecorationLocation> LocationProperty = AvaloniaProperty.Register<TextDecoration, TextDecorationLocation>(nameof(Location));`
- `public static readonly StyledProperty<IBrush?> StrokeProperty = AvaloniaProperty.Register<TextDecoration, IBrush?>(nameof(Stroke));`
- `public static readonly StyledProperty<TextDecorationUnit> StrokeThicknessUnitProperty = AvaloniaProperty.Register<TextDecoration, TextDecorationUnit>(nameof(StrokeThicknessUnit));`
- `public static readonly StyledProperty<AvaloniaList<double>?> StrokeDashArrayProperty = AvaloniaProperty.Register<TextDecoration, AvaloniaList<double>?>(nameof(StrokeDashArray));`
- `public static readonly StyledProperty<double> StrokeDashOffsetProperty = AvaloniaProperty.Register<TextDecoration, double>(nameof(StrokeDashOffset));`
- `public static readonly StyledProperty<double> StrokeThicknessProperty = AvaloniaProperty.Register<TextDecoration, double>(nameof(StrokeThickness), 1);`
- `public static readonly StyledProperty<PenLineCap> StrokeLineCapProperty = AvaloniaProperty.Register<TextDecoration, PenLineCap>(nameof(StrokeLineCap));`
- `public static readonly StyledProperty<double> StrokeOffsetProperty = AvaloniaProperty.Register<TextDecoration, double>(nameof(StrokeOffset));`
- `public static readonly StyledProperty<TextDecorationUnit> StrokeOffsetUnitProperty = AvaloniaProperty.Register<TextDecoration, TextDecorationUnit>(nameof(StrokeOffsetUnit));`
- `public TextDecorationLocation Location {`
- `public IBrush? Stroke {`
- `public TextDecorationUnit StrokeThicknessUnit {`
- `public AvaloniaList<double>? StrokeDashArray {`
- `public double StrokeDashOffset {`
- `public double StrokeThickness {`
- `public PenLineCap StrokeLineCap {`
- `public double StrokeOffset {`
- `public TextDecorationUnit StrokeOffsetUnit {`

### `src/Avalonia.Base/Media/TextDecorationCollection.cs`
- `public class TextDecorationCollection : AvaloniaList<TextDecoration>`
- `public TextDecorationCollection() {`
- `public TextDecorationCollection(IEnumerable<TextDecoration> textDecorations) : base(textDecorations) {`
- `public static TextDecorationCollection Parse(string s) {`

### `src/Avalonia.Base/Media/TextDecorationLocation.cs`
- `public enum TextDecorationLocation`

### `src/Avalonia.Base/Media/TextDecorationUnit.cs`
- `public enum TextDecorationUnit`

### `src/Avalonia.Base/Media/TextDecorations.cs`
- `public static class TextDecorations`
- `public static TextDecorationCollection Underline { get; }`
- `public static TextDecorationCollection Strikethrough { get; }`
- `public static TextDecorationCollection Overline { get; }`
- `public static TextDecorationCollection Baseline { get; }`

### `src/Avalonia.Base/Media/TextFormatting/DrawableTextRun.cs`
- `public abstract class DrawableTextRun : TextRun`
- `public abstract Size Size { get; }`
- `public abstract double Baseline { get; }`
- `public abstract void Draw(DrawingContext drawingContext, Point origin);`

### `src/Avalonia.Base/Media/TextFormatting/GenericTextParagraphProperties.cs`
- `public sealed class GenericTextParagraphProperties : TextParagraphProperties`
- `public GenericTextParagraphProperties(TextRunProperties defaultTextRunProperties, TextAlignment textAlignment = TextAlignment.Left, TextWrapping textWrap = TextWrapping.NoWrap, double lineHeight = 0, double letterSpacing = 0) {`
- `public GenericTextParagraphProperties( FlowDirection flowDirection, TextAlignment textAlignment, bool firstLineInParagraph, bool alwaysCollapsible, TextRunProperties defaultTextRunProperties, TextWrapping textWrap, double lineHeight, double indent, double letterSpacing) {`
- `public GenericTextParagraphProperties(TextParagraphProperties textParagraphProperties) : this(textParagraphProperties.FlowDirection, textParagraphProperties.TextAlignment, textParagraphProperties.FirstLineInParagraph, textParagraphProperties.AlwaysCollapsible, textParagraphProperties.DefaultTextRunProperties, textParagraphProperties.TextWrapping, textParagraphProperties.LineHeight, textParagraphProperties.Indent, textParagraphProperties.LetterSpacing) {`
- `public override FlowDirection FlowDirection {`
- `public override TextAlignment TextAlignment {`
- `public override double LineHeight {`
- `public override bool FirstLineInParagraph { get; }`
- `public override bool AlwaysCollapsible { get; }`
- `public override TextRunProperties DefaultTextRunProperties { get; }`
- `public override TextWrapping TextWrapping {`
- `public override double Indent { get; }`
- `public override double LetterSpacing { get; }`

### `src/Avalonia.Base/Media/TextFormatting/GenericTextRunProperties.cs`
- `public class GenericTextRunProperties : TextRunProperties`
- `public GenericTextRunProperties(Typeface typeface, double fontRenderingEmSize = DefaultFontRenderingEmSize, TextDecorationCollection? textDecorations = null, IBrush? foregroundBrush = null, IBrush? backgroundBrush = null, BaselineAlignment baselineAlignment = BaselineAlignment.Baseline, CultureInfo? cultureInfo = null) : this(typeface, null, fontRenderingEmSize, textDecorations, foregroundBrush, backgroundBrush, baselineAlignment, cultureInfo) {`
- `public GenericTextRunProperties( Typeface typeface, FontFeatureCollection? fontFeatures, double fontRenderingEmSize = DefaultFontRenderingEmSize, TextDecorationCollection? textDecorations = null, IBrush? foregroundBrush = null, IBrush? backgroundBrush = null, BaselineAlignment baselineAlignment = BaselineAlignment.Baseline, CultureInfo? cultureInfo = null) {`
- `public override Typeface Typeface { get; }`
- `public override double FontRenderingEmSize { get; }`
- `public override TextDecorationCollection? TextDecorations { get; }`
- `public override IBrush? ForegroundBrush { get; }`
- `public override IBrush? BackgroundBrush { get; }`
- `public override FontFeatureCollection? FontFeatures { get; }`
- `public override BaselineAlignment BaselineAlignment { get; }`
- `public override CultureInfo? CultureInfo { get; }`

### `src/Avalonia.Base/Media/TextFormatting/GlyphInfo.cs`
- `public readonly record struct GlyphInfo(ushort GlyphIndex, int GlyphCluster, double GlyphAdvance, Vector GlyphOffset = default)`
- `public ushort GlyphIndex { get; } = GlyphIndex;`
- `public int GlyphCluster { get; } = GlyphCluster;`
- `public double GlyphAdvance { get; } = GlyphAdvance;`
- `public Vector GlyphOffset { get; } = GlyphOffset;`

### `src/Avalonia.Base/Media/TextFormatting/ITextSource.cs`
- `public interface ITextSource`

### `src/Avalonia.Base/Media/TextFormatting/JustificationProperties.cs`
- `public abstract class JustificationProperties`
- `public abstract double Width { get; }`
- `public abstract void Justify(TextLine textLine);`

### `src/Avalonia.Base/Media/TextFormatting/LogicalDirection.cs`
- `public enum LogicalDirection`

### `src/Avalonia.Base/Media/TextFormatting/ShapedBuffer.cs`
- `public sealed class ShapedBuffer : IReadOnlyList<GlyphInfo>, IDisposable`
- `public ShapedBuffer(ReadOnlyMemory<char> text, int bufferLength, IGlyphTypeface glyphTypeface, double fontRenderingEmSize, sbyte bidiLevel) {`
- `public int Length => _glyphInfos.Length;`
- `public IGlyphTypeface GlyphTypeface { get; }`
- `public double FontRenderingEmSize { get; }`
- `public sbyte BidiLevel { get; private set; }`
- `public bool IsLeftToRight => (BidiLevel & 1) == 0;`
- `public ReadOnlyMemory<char> Text { get; }`
- `public void Reverse() {`
- `public void Dispose() {`
- `public GlyphInfo this[int index] {`
- `public IEnumerator<GlyphInfo> GetEnumerator() => _glyphInfos.GetEnumerator();`
- `public SplitResult<ShapedBuffer> Split(int textLength) {`

### `src/Avalonia.Base/Media/TextFormatting/ShapedTextRun.cs`
- `public sealed class ShapedTextRun : DrawableTextRun, IDisposable`
- `public ShapedTextRun(ShapedBuffer shapedBuffer, TextRunProperties properties) {`
- `public bool IsReversed { get; private set; }`
- `public sbyte BidiLevel => ShapedBuffer.BidiLevel;`
- `public ShapedBuffer ShapedBuffer { get; }`
- `public override ReadOnlyMemory<char> Text => ShapedBuffer.Text;`
- `public override TextRunProperties Properties { get; }`
- `public override int Length => ShapedBuffer.Text.Length;`
- `public TextMetrics TextMetrics { get; }`
- `public override double Baseline => -TextMetrics.Ascent + TextMetrics.LineGap * 0.5;`
- `public override Size Size => GlyphRun.Bounds.Size;`
- `public GlyphRun GlyphRun => _glyphRun ??= CreateGlyphRun();`
- `public override void Draw(DrawingContext drawingContext, Point origin) {`
- `public bool TryMeasureCharacters(double availableWidth, out int length) {`
- `public void Dispose() {`

### `src/Avalonia.Base/Media/TextFormatting/SplitResult.cs`
- `public readonly struct SplitResult<T>`
- `public SplitResult(T? first, T? second) {`
- `public T? First { get; }`
- `public T? Second { get; }`
- `public void Deconstruct(out T? first, out T? second) {`

### `src/Avalonia.Base/Media/TextFormatting/TextBounds.cs`
- `public sealed class TextBounds`
- `public Rect Rectangle { get; internal set; }`
- `public FlowDirection FlowDirection { get; }`
- `public IList<TextRunBounds> TextRunBounds { get; }`

### `src/Avalonia.Base/Media/TextFormatting/TextCharacters.cs`
- `public class TextCharacters : TextRun`
- `public TextCharacters(string text, TextRunProperties textRunProperties) : this(text.AsMemory(), textRunProperties) {`
- `public TextCharacters(ReadOnlyMemory<char> text, TextRunProperties textRunProperties) {`
- `public override int Length => Text.Length;`
- `public override ReadOnlyMemory<char> Text { get; }`
- `public override TextRunProperties Properties { get; }`

### `src/Avalonia.Base/Media/TextFormatting/TextCollapsingProperties.cs`
- `public abstract class TextCollapsingProperties`
- `public abstract double Width { get; }`
- `public abstract TextRun Symbol { get; }`
- `public abstract FlowDirection FlowDirection { get; }`
- `public abstract TextRun[]? Collapse(TextLine textLine);`
- `public static TextRun[] CreateCollapsedRuns(TextLine textLine, int collapsedLength, FlowDirection flowDirection, TextRun shapedSymbol) {`

### `src/Avalonia.Base/Media/TextFormatting/TextEndOfLine.cs`
- `public class TextEndOfLine : TextRun`
- `public TextEndOfLine(int textSourceLength = DefaultTextSourceLength) {`
- `public override int Length { get; }`

### `src/Avalonia.Base/Media/TextFormatting/TextEndOfParagraph.cs`
- `public class TextEndOfParagraph : TextEndOfLine`
- `public TextEndOfParagraph() {`
- `public TextEndOfParagraph(int textSourceLength) : base(textSourceLength) {`

### `src/Avalonia.Base/Media/TextFormatting/TextFormatter.cs`
- `public abstract class TextFormatter`
- `public static TextFormatter Current {`
- `public abstract TextLine? FormatLine(ITextSource textSource, int firstTextSourceIndex, double paragraphWidth, TextParagraphProperties paragraphProperties, TextLineBreak? previousLineBreak = null);`
- `public static ShapedTextRun CreateSymbol(TextRun textRun, FlowDirection flowDirection) {`

### `src/Avalonia.Base/Media/TextFormatting/TextLayout.cs`
- `public class TextLayout : IDisposable`
- `public TextLayout( string? text, Typeface typeface, double fontSize, IBrush? foreground, TextAlignment textAlignment = TextAlignment.Left, TextWrapping textWrapping = TextWrapping.NoWrap, TextTrimming? textTrimming = null, TextDecorationCollection? textDecorations = null, FlowDirection flowDirection = FlowDirection.LeftToRight, double maxWidth = double.PositiveInfinity, double maxHeight = double.PositiveInfinity, double lineHeight = double.NaN, double letterSpacing = 0, int maxLines = 0, IReadOnlyList<ValueSpan<TextRunProperties>>? textStyleOverrides = null) : this(text, typeface, null, fontSize, foreground, textAlignment, textWrapping, textTrimming, textDecorations, flowDirection, maxWidth, maxHeight, lineHeight, letterSpacing, maxLines, textStyleOverrides) {`
- `public TextLayout( string? text, Typeface typeface, FontFeatureCollection? fontFeatures, double fontSize, IBrush? foreground, TextAlignment textAlignment = TextAlignment.Left, TextWrapping textWrapping = TextWrapping.NoWrap, TextTrimming? textTrimming = null, TextDecorationCollection? textDecorations = null, FlowDirection flowDirection = FlowDirection.LeftToRight, double maxWidth = double.PositiveInfinity, double maxHeight = double.PositiveInfinity, double lineHeight = double.NaN, double letterSpacing = 0, int maxLines = 0, IReadOnlyList<ValueSpan<TextRunProperties>>? textStyleOverrides = null) {`
- `public TextLayout( ITextSource textSource, TextParagraphProperties paragraphProperties, TextTrimming? textTrimming = null, double maxWidth = double.PositiveInfinity, double maxHeight = double.PositiveInfinity, int maxLines = 0) {`
- `public double LineHeight => _paragraphProperties.LineHeight;`
- `public double MaxWidth { get; }`
- `public double MaxHeight { get; }`
- `public int MaxLines { get; }`
- `public double LetterSpacing => _paragraphProperties.LetterSpacing;`
- `public IReadOnlyList<TextLine> TextLines => _textLines;`
- `public double Height {`
- `public double Extent {`
- `public double Baseline {`
- `public double OverhangAfter {`
- `public double OverhangLeading {`
- `public double OverhangTrailing {`
- `public double Width {`
- `public double WidthIncludingTrailingWhitespace {`
- `public void Draw(DrawingContext context, Point origin) {`
- `public Rect HitTestTextPosition(int textPosition) {`
- `public IEnumerable<Rect> HitTestTextRange(int start, int length) {`
- `public TextHitTestResult HitTestPoint(in Point point) {`
- `public int GetLineIndexFromCharacterIndex(int charIndex, bool trailingEdge) {`
- `public void Dispose() {`

### `src/Avalonia.Base/Media/TextFormatting/TextLeadingPrefixCharacterEllipsis.cs`
- `public sealed class TextLeadingPrefixCharacterEllipsis : TextCollapsingProperties`
- `public TextLeadingPrefixCharacterEllipsis( string ellipsis, int prefixLength, double width, TextRunProperties textRunProperties, FlowDirection flowDirection) {`
- `public override double Width { get; }`
- `public override TextRun Symbol { get; }`
- `public override FlowDirection FlowDirection { get; }`
- `public override TextRun[]? Collapse(TextLine textLine) {`

### `src/Avalonia.Base/Media/TextFormatting/TextLine.cs`
- `public abstract class TextLine : IDisposable`
- `public abstract IReadOnlyList<TextRun> TextRuns { get; }`
- `public abstract int FirstTextSourceIndex { get; }`
- `public abstract int Length { get; }`
- `public abstract TextLineBreak? TextLineBreak { get; }`
- `public abstract double Baseline { get; }`
- `public abstract double Extent { get; }`
- `public abstract bool HasCollapsed { get; }`
- `public abstract bool HasOverflowed { get; }`
- `public abstract double Height { get; }`
- `public abstract int NewLineLength { get; }`
- `public abstract double OverhangAfter { get; }`
- `public abstract double OverhangLeading { get; }`
- `public abstract double OverhangTrailing { get; }`
- `public abstract double Start { get; }`
- `public abstract int TrailingWhitespaceLength { get; }`
- `public abstract double Width { get; }`
- `public abstract double WidthIncludingTrailingWhitespace { get; }`
- `public abstract void Draw(DrawingContext drawingContext, Point lineOrigin);`
- `public abstract TextLine Collapse(params TextCollapsingProperties?[] collapsingPropertiesList);`
- `public abstract void Justify(JustificationProperties justificationProperties);`
- `public abstract CharacterHit GetCharacterHitFromDistance(double distance);`
- `public abstract double GetDistanceFromCharacterHit(CharacterHit characterHit);`
- `public abstract CharacterHit GetNextCaretCharacterHit(CharacterHit characterHit);`
- `public abstract CharacterHit GetPreviousCaretCharacterHit(CharacterHit characterHit);`
- `public abstract CharacterHit GetBackspaceCaretCharacterHit(CharacterHit characterHit);`
- `public abstract IReadOnlyList<TextBounds> GetTextBounds(int firstTextSourceCharacterIndex, int textLength);`
- `public abstract void Dispose();`

### `src/Avalonia.Base/Media/TextFormatting/TextLineBreak.cs`
- `public class TextLineBreak`
- `public TextLineBreak(TextEndOfLine? textEndOfLine = null, FlowDirection flowDirection = FlowDirection.LeftToRight, bool isSplit = false) {`
- `public TextEndOfLine? TextEndOfLine { get; }`
- `public FlowDirection FlowDirection { get; }`
- `public bool IsSplit { get; }`

### `src/Avalonia.Base/Media/TextFormatting/TextLineMetrics.cs`
- `public readonly record struct TextLineMetrics`
- `public bool HasOverflowed { get; init; }`
- `public double Height { get; init; }`
- `public int NewlineLength { get; init; }`
- `public double Start { get; init; }`
- `public double TextBaseline { get; init; }`
- `public int TrailingWhitespaceLength { get; init; }`
- `public double Width { get; init; }`
- `public double WidthIncludingTrailingWhitespace { get; init; }`
- `public double Extent { get; init; }`
- `public double OverhangAfter { get; init; }`
- `public double OverhangLeading { get; init; }`
- `public double OverhangTrailing { get; init; }`

### `src/Avalonia.Base/Media/TextFormatting/TextMetrics.cs`
- `public readonly record struct TextMetrics`
- `public TextMetrics(IGlyphTypeface glyphTypeface, double fontRenderingEmSize) {`
- `public double FontRenderingEmSize { get; }`
- `public double Baseline { get; }`
- `public double Ascent { get; }`
- `public double Descent { get; }`
- `public double LineGap { get; }`
- `public double LineHeight { get; }`
- `public double UnderlineThickness { get; }`
- `public double UnderlinePosition { get; }`
- `public double StrikethroughThickness { get; }`
- `public double StrikethroughPosition { get; }`

### `src/Avalonia.Base/Media/TextFormatting/TextParagraphProperties.cs`
- `public abstract class TextParagraphProperties`
- `public abstract FlowDirection FlowDirection { get; }`
- `public abstract TextAlignment TextAlignment { get; }`
- `public abstract double LineHeight { get; }`
- `public abstract bool FirstLineInParagraph { get; }`
- `public virtual bool AlwaysCollapsible {`
- `public abstract TextRunProperties DefaultTextRunProperties { get; }`
- `public virtual TextDecorationCollection? TextDecorations => null;`
- `public abstract TextWrapping TextWrapping { get; }`
- `public abstract double Indent { get; }`
- `public virtual double ParagraphIndent {`
- `public virtual double DefaultIncrementalTab => 0;`
- `public virtual double LetterSpacing { get; }`

### `src/Avalonia.Base/Media/TextFormatting/TextRange.cs`
- `public readonly record struct TextRange`
- `public TextRange(int start, int length) {`
- `public int Start { get; }`
- `public int Length { get; }`
- `public int End => Start + Length - 1;`
- `public TextRange Take(int length) {`
- `public TextRange Skip(int length) {`

### `src/Avalonia.Base/Media/TextFormatting/TextRun.cs`
- `public abstract class TextRun`
- `public const int DefaultTextSourceLength = 1;`
- `public virtual int Length => DefaultTextSourceLength;`
- `public virtual ReadOnlyMemory<char> Text => default;`
- `public virtual TextRunProperties? Properties => null;`

### `src/Avalonia.Base/Media/TextFormatting/TextRunBounds.cs`
- `public readonly record struct TextRunBounds`
- `public int TextSourceCharacterIndex { get; }`
- `public int Length { get; }`
- `public Rect Rectangle { get; }`
- `public TextRun TextRun { get; }`

### `src/Avalonia.Base/Media/TextFormatting/TextRunProperties.cs`
- `public abstract class TextRunProperties : IEquatable<TextRunProperties>`
- `public abstract Typeface Typeface { get; }`
- `public abstract double FontRenderingEmSize { get; }`
- `public abstract TextDecorationCollection? TextDecorations { get; }`
- `public abstract IBrush? ForegroundBrush { get; }`
- `public abstract IBrush? BackgroundBrush { get; }`
- `public abstract CultureInfo? CultureInfo { get; }`
- `public virtual FontFeatureCollection? FontFeatures => null;`
- `public virtual BaselineAlignment BaselineAlignment => BaselineAlignment.Baseline;`
- `public bool Equals(TextRunProperties? other) {`
- `public override bool Equals(object? obj) {`
- `public override int GetHashCode() {`
- `public static bool operator ==(TextRunProperties left, TextRunProperties right) {`
- `public static bool operator !=(TextRunProperties left, TextRunProperties right) {`

### `src/Avalonia.Base/Media/TextFormatting/TextShaper.cs`
- `public class TextShaper`
- `public TextShaper(ITextShaperImpl platformImpl) {`
- `public static TextShaper Current {`
- `public ShapedBuffer ShapeText(ReadOnlyMemory<char> text, TextShaperOptions options = default) {`
- `public ShapedBuffer ShapeText(string text, TextShaperOptions options = default) {`

### `src/Avalonia.Base/Media/TextFormatting/TextShaperOptions.cs`
- `public readonly record struct TextShaperOptions`
- `public TextShaperOptions( IGlyphTypeface typeface, double fontRenderingEmSize = 12, sbyte bidiLevel = 0, CultureInfo? culture = null, double incrementalTabWidth = 0, double letterSpacing = 0) : this(typeface, null, fontRenderingEmSize, bidiLevel, culture, incrementalTabWidth, letterSpacing) {`
- `public TextShaperOptions( IGlyphTypeface typeface, IReadOnlyList<FontFeature>? fontFeatures, double fontRenderingEmSize = 12, sbyte bidiLevel = 0, CultureInfo? culture = null, double incrementalTabWidth = 0, double letterSpacing = 0) {`
- `public IGlyphTypeface Typeface { get; }`
- `public double FontRenderingEmSize { get; }`
- `public sbyte BidiLevel { get; }`
- `public CultureInfo? Culture { get; }`
- `public double IncrementalTabWidth { get; }`
- `public double LetterSpacing { get; }`
- `public IReadOnlyList<FontFeature>? FontFeatures { get; }`

### `src/Avalonia.Base/Media/TextFormatting/TextTrailingCharacterEllipsis.cs`
- `public sealed class TextTrailingCharacterEllipsis : TextCollapsingProperties`
- `public TextTrailingCharacterEllipsis(string ellipsis, double width, TextRunProperties textRunProperties, FlowDirection flowDirection) {`
- `public override double Width { get; }`
- `public override TextRun Symbol { get; }`
- `public override FlowDirection FlowDirection { get; }`
- `public override TextRun[]? Collapse(TextLine textLine) {`

### `src/Avalonia.Base/Media/TextFormatting/TextTrailingWordEllipsis.cs`
- `public sealed class TextTrailingWordEllipsis : TextCollapsingProperties`
- `public TextTrailingWordEllipsis( string ellipsis, double width, TextRunProperties textRunProperties, FlowDirection flowDirection ) {`
- `public override double Width { get; }`
- `public override TextRun Symbol { get; }`
- `public override FlowDirection FlowDirection { get; }`
- `public override TextRun[]? Collapse(TextLine textLine) {`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/BiDiClass.cs`
- `public enum BidiClass`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/BiDiPairedBracketType.cs`
- `public enum BidiPairedBracketType`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/Codepoint.cs`
- `public readonly record struct Codepoint`
- `public static Codepoint ReplacementCodepoint {`
- `public Codepoint(uint value) => _value = value;`
- `public uint Value => _value;`
- `public GeneralCategory GeneralCategory => UnicodeData.GetGeneralCategory(_value);`
- `public Script Script => UnicodeData.GetScript(_value);`
- `public BidiClass BiDiClass => UnicodeData.GetBiDiClass(_value);`
- `public BidiPairedBracketType PairedBracketType => UnicodeData.GetBiDiPairedBracketType(_value);`
- `public LineBreakClass LineBreakClass => UnicodeData.GetLineBreakClass(_value);`
- `public GraphemeBreakClass GraphemeBreakClass => UnicodeData.GetGraphemeClusterBreak(_value);`
- `public EastAsianWidthClass EastAsianWidthClass => UnicodeData.GetEastAsianWidthClass(_value);`
- `public bool IsEastAsian {`
- `public bool IsBreakChar {`
- `public bool IsWhiteSpace {`
- `public bool TryGetPairedBracket(out Codepoint codepoint) {`
- `public static implicit operator int(Codepoint codepoint) {`
- `public static implicit operator uint(Codepoint codepoint) {`
- `public static Codepoint ReadAt(ReadOnlySpan<char> text, int index, out int count) {`
- `public static bool IsInRangeInclusive(Codepoint cp, uint lowerBound, uint upperBound) => IsInRangeInclusive(cp._value, lowerBound, upperBound);`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/CodepointEnumerator.cs`
- `public ref struct CodepointEnumerator`
- `public CodepointEnumerator(ReadOnlySpan<char> text) => _text = text;`
- `public bool MoveNext(out Codepoint codepoint) {`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/EastAsianWidthClass.cs`
- `public enum EastAsianWidthClass`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/GeneralCategory.cs`
- `public enum GeneralCategory`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/Grapheme.cs`
- `public readonly ref struct Grapheme`
- `public Grapheme(Codepoint firstCodepoint, int offset, int length) {`
- `public Codepoint FirstCodepoint { get; }`
- `public int Offset { get; }`
- `public int Length { get; }`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/GraphemeBreakClass.cs`
- `public enum GraphemeBreakClass`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/GraphemeEnumerator.cs`
- `public ref struct GraphemeEnumerator`
- `public GraphemeEnumerator(ReadOnlySpan<char> text) {`
- `public bool MoveNext(out Grapheme grapheme) {`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/LineBreak.cs`
- `public readonly record struct LineBreak`
- `public LineBreak(int positionMeasure, int positionWrap, bool required = false) {`
- `public int PositionMeasure { get; }`
- `public int PositionWrap { get; }`
- `public bool Required { get; }`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/LineBreakClass.cs`
- `public enum LineBreakClass`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/LineBreakEnumerator.cs`
- `public ref struct LineBreakEnumerator`
- `public readonly ReadOnlySpan<char> _text;`
- `public LineBreakEnumerator(ReadOnlySpan<char> text) {`
- `public bool MoveNext([NotNullWhen(true)] out LineBreak lineBreak) {`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/Script.cs`
- `public enum Script`

### `src/Avalonia.Base/Media/TextFormatting/UnshapedTextRun.cs`
- `public sealed class UnshapedTextRun : TextRun`
- `public UnshapedTextRun(ReadOnlyMemory<char> text, TextRunProperties properties, sbyte biDiLevel) {`
- `public override int Length => Text.Length;`
- `public override ReadOnlyMemory<char> Text { get; }`
- `public override TextRunProperties Properties { get; }`
- `public sbyte BidiLevel { get; }`

### `src/Avalonia.Base/Media/TextHitTestResult.cs`
- `public readonly record struct TextHitTestResult`
- `public TextHitTestResult(CharacterHit characterHit, int textPosition, bool isInside, bool isTrailing) {`
- `public CharacterHit CharacterHit { get; }`
- `public bool IsInside { get; }`
- `public int TextPosition { get; }`
- `public bool IsTrailing { get; }`

### `src/Avalonia.Base/Media/TextLeadingPrefixTrimming.cs`
- `public sealed class TextLeadingPrefixTrimming : TextTrimming`
- `public TextLeadingPrefixTrimming(string ellipsis, int prefixLength) {`
- `public override TextCollapsingProperties CreateCollapsingProperties(TextCollapsingCreateInfo createInfo) {`
- `public override string ToString() {`

### `src/Avalonia.Base/Media/TextPathSegmentEllipsis.cs`
- `public sealed class TextPathSegmentEllipsis : TextCollapsingProperties`
- `public TextPathSegmentEllipsis(string ellipsis, double width, TextRunProperties textRunProperties, FlowDirection flowDirection) {`
- `public override double Width { get; }`
- `public override TextRun Symbol { get; }`
- `public override FlowDirection FlowDirection { get; }`
- `public override TextRun[]? Collapse(TextLine textLine) {`

### `src/Avalonia.Base/Media/TextPathSegmentTrimming.cs`
- `public sealed class TextPathSegmentTrimming : TextTrimming`
- `public TextPathSegmentTrimming(string ellipsis) {`
- `public override TextCollapsingProperties CreateCollapsingProperties(TextCollapsingCreateInfo createInfo) {`
- `public override string ToString() {`

### `src/Avalonia.Base/Media/TextRenderingMode.cs`
- `public enum TextRenderingMode : byte`

### `src/Avalonia.Base/Media/TextTrailingTrimming.cs`
- `public sealed class TextTrailingTrimming : TextTrimming`
- `public TextTrailingTrimming(string ellipsis, bool isWordBased) {`
- `public override TextCollapsingProperties CreateCollapsingProperties(TextCollapsingCreateInfo createInfo) {`
- `public override string ToString() {`

### `src/Avalonia.Base/Media/TextTrimming.cs`
- `public abstract class TextTrimming`
- `public static TextTrimming None { get; } = new TextNoneTrimming();`
- `public static TextTrimming CharacterEllipsis { get; } = new TextTrailingTrimming(DefaultEllipsisChar, false);`
- `public static TextTrimming WordEllipsis { get; } = new TextTrailingTrimming(DefaultEllipsisChar, true);`
- `public static TextTrimming PrefixCharacterEllipsis { get; } = new TextLeadingPrefixTrimming(DefaultEllipsisChar, 8);`
- `public static TextTrimming LeadingCharacterEllipsis { get; } = new TextLeadingPrefixTrimming(DefaultEllipsisChar, 0);`
- `public static TextTrimming PathSegmentEllipsis { get; } = new TextPathSegmentTrimming(DefaultEllipsisChar);`
- `public abstract TextCollapsingProperties CreateCollapsingProperties(TextCollapsingCreateInfo createInfo);`
- `public static TextTrimming Parse(string s) {`

### `src/Avalonia.Base/Media/TextWrapping.cs`
- `public enum TextWrapping`

### `src/Avalonia.Base/Media/TileBrush.cs`
- `public enum TileMode`
- `public abstract class TileBrush : Brush, ITileBrush`
- `public static readonly StyledProperty<AlignmentX> AlignmentXProperty = AvaloniaProperty.Register<TileBrush, AlignmentX>(nameof(AlignmentX), AlignmentX.Center);`
- `public static readonly StyledProperty<AlignmentY> AlignmentYProperty = AvaloniaProperty.Register<TileBrush, AlignmentY>(nameof(AlignmentY), AlignmentY.Center);`
- `public static readonly StyledProperty<RelativeRect> DestinationRectProperty = AvaloniaProperty.Register<TileBrush, RelativeRect>(nameof(DestinationRect), RelativeRect.Fill);`
- `public static readonly StyledProperty<RelativeRect> SourceRectProperty = AvaloniaProperty.Register<TileBrush, RelativeRect>(nameof(SourceRect), RelativeRect.Fill);`
- `public static readonly StyledProperty<Stretch> StretchProperty = AvaloniaProperty.Register<TileBrush, Stretch>(nameof(Stretch), Stretch.Uniform);`
- `public static readonly StyledProperty<TileMode> TileModeProperty = AvaloniaProperty.Register<TileBrush, TileMode>(nameof(TileMode));`
- `public AlignmentX AlignmentX {`
- `public AlignmentY AlignmentY {`
- `public RelativeRect DestinationRect {`
- `public RelativeRect SourceRect {`
- `public Stretch Stretch {`
- `public TileMode TileMode {`

### `src/Avalonia.Base/Media/Transform.cs`
- `public abstract class Transform : Animatable, IMutableTransform, ICompositionRenderResource<ITransform>, ICompositorSerializable`
- `public event EventHandler? Changed;`
- `public abstract Matrix Value { get; }`
- `public static Transform Parse(string s) {`
- `public ImmutableTransform ToImmutable() {`
- `public override string ToString() {`

### `src/Avalonia.Base/Media/TransformConverter.cs`
- `public class TransformConverter : TypeConverter`
- `public override bool CanConvertFrom(ITypeDescriptorContext? context, Type sourceType) {`
- `public override object? ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object? value) {`

### `src/Avalonia.Base/Media/TransformExtensions.cs`
- `public static class TransformExtensions`
- `public static ImmutableTransform ToImmutable(this ITransform transform) {`

### `src/Avalonia.Base/Media/TransformGroup.cs`
- `public sealed class TransformGroup : Transform`
- `public static readonly StyledProperty<Transforms> ChildrenProperty = AvaloniaProperty.Register<TransformGroup, Transforms>(nameof(Children));`
- `public TransformGroup() {`
- `public Transforms Children {`
- `public override Matrix Value {`
- `public sealed class Transforms : AvaloniaList<Transform>`

### `src/Avalonia.Base/Media/Transformation/TransformOperation.cs`
- `public record struct TransformOperation`
- `public OperationType Type;`
- `public Matrix Matrix;`
- `public DataLayout Data;`
- `public enum OperationType`
- `public bool IsIdentity => Matrix.IsIdentity;`
- `public void Bake() {`
- `public static TransformOperation Identity =>`
- `public static bool TryInterpolate(TransformOperation? from, TransformOperation? to, double progress, ref TransformOperation result) {`
- `public record struct DataLayout`
- `public record struct SkewLayout`
- `public double X;`
- `public double Y;`
- `public record struct ScaleLayout`
- `public double X;`
- `public double Y;`
- `public record struct TranslateLayout`
- `public double X;`
- `public double Y;`
- `public record struct RotateLayout`
- `public double Angle;`

### `src/Avalonia.Base/Media/Transformation/TransformOperations.cs`
- `public sealed class TransformOperations : ITransform`
- `public static TransformOperations Identity { get; } = new TransformOperations(new List<TransformOperation>());`
- `public bool IsIdentity { get; }`
- `public IReadOnlyList<TransformOperation> Operations => _operations;`
- `public Matrix Value { get; }`
- `public static TransformOperations Parse(string s) {`
- `public static Builder CreateBuilder(int capacity) {`
- `public static TransformOperations Interpolate(TransformOperations from, TransformOperations to, double progress) {`
- `public readonly record struct Builder`
- `public Builder(int capacity) {`
- `public void AppendTranslate(double x, double y) {`
- `public void AppendRotate(double angle) {`
- `public void AppendScale(double x, double y) {`
- `public void AppendSkew(double x, double y) {`
- `public void AppendMatrix(Matrix matrix) {`
- `public void AppendIdentity() {`
- `public void Append(TransformOperation toAdd) {`
- `public TransformOperations Build() {`

### `src/Avalonia.Base/Media/TranslateTransform.cs`
- `public sealed class TranslateTransform : Transform`
- `public static readonly StyledProperty<double> XProperty = AvaloniaProperty.Register<TranslateTransform, double>(nameof(X));`
- `public static readonly StyledProperty<double> YProperty = AvaloniaProperty.Register<TranslateTransform, double>(nameof(Y));`
- `public TranslateTransform() {`
- `public TranslateTransform(double x, double y) : this() {`
- `public double X {`
- `public double Y {`
- `public override Matrix Value => Matrix.CreateTranslation(X, Y);`

### `src/Avalonia.Base/Media/Typeface.cs`
- `public readonly struct Typeface : IEquatable<Typeface>`
- `public Typeface(FontFamily fontFamily, FontStyle style = FontStyle.Normal, FontWeight weight = FontWeight.Normal, FontStretch stretch = FontStretch.Normal) {`
- `public Typeface(string fontFamilyName, FontStyle style = FontStyle.Normal, FontWeight weight = FontWeight.Normal, FontStretch stretch = FontStretch.Normal) : this(string.IsNullOrEmpty(fontFamilyName) ? FontFamily.Default : new FontFamily(fontFamilyName), style, weight, stretch) {`
- `public static Typeface Default { get; } = new Typeface(FontFamily.Default);`
- `public FontFamily FontFamily { get; }`
- `public FontStyle Style { get; }`
- `public FontWeight Weight { get; }`
- `public FontStretch Stretch { get; }`
- `public IGlyphTypeface GlyphTypeface {`
- `public static bool operator !=(Typeface a, Typeface b) {`
- `public static bool operator ==(Typeface a, Typeface b) {`
- `public override bool Equals(object? obj) {`
- `public bool Equals(Typeface other) {`
- `public override int GetHashCode() {`

### `src/Avalonia.Base/Media/UnicodeRange.cs`
- `public readonly record struct UnicodeRange`
- `public readonly static UnicodeRange Default = Parse("0-10FFFD");`
- `public UnicodeRange(int start, int end) {`
- `public UnicodeRange(UnicodeRangeSegment single) {`
- `public UnicodeRange(IReadOnlyList<UnicodeRangeSegment> segments) {`
- `public bool IsInRange(int value) {`
- `public static UnicodeRange Parse(string s) {`
- `public readonly record struct UnicodeRangeSegment`
- `public UnicodeRangeSegment(int start, int end) {`
- `public int Start { get; }`
- `public int End { get; }`
- `public bool IsInRange(int value) {`
- `public static UnicodeRangeSegment Parse(string s) {`

### `src/Avalonia.Base/Media/VisualBrush.cs`
- `public sealed class VisualBrush : TileBrush, ISceneBrush`
- `public static readonly StyledProperty<Visual?> VisualProperty = AvaloniaProperty.Register<VisualBrush, Visual?>(nameof(Visual));`
- `public VisualBrush() {`
- `public VisualBrush(Visual visual) {`
- `public Visual? Visual {`

### `src/Avalonia.Base/Metadata/AmbientAttribute.cs`
- `public sealed class AmbientAttribute : Attribute`

### `src/Avalonia.Base/Metadata/AvaloniaListAttribute.cs`
- Namespace: `Avalonia.Metadata`
- `public sealed class AvaloniaListAttribute : Attribute`
- `public string[]? Separators { get; init; }`
- `public StringSplitOptions SplitOptions { get; init; } = StringSplitOptions.RemoveEmptyEntries | (StringSplitOptions)2;`

### `src/Avalonia.Base/Metadata/ContentAttribute.cs`
- `public sealed class ContentAttribute : Attribute`

### `src/Avalonia.Base/Metadata/ControlTemplateScopeAttribute.cs`
- Namespace: `Avalonia.Metadata`
- `public sealed class ControlTemplateScopeAttribute : Attribute;`

### `src/Avalonia.Base/Metadata/DataTypeAttribute.cs`
- Namespace: `Avalonia.Metadata`
- `public sealed class DataTypeAttribute : Attribute`

### `src/Avalonia.Base/Metadata/DependsOnAttribute.cs`
- `public sealed class DependsOnAttribute : Attribute`
- `public DependsOnAttribute(string propertyName) {`
- `public string Name { get; }`

### `src/Avalonia.Base/Metadata/IAddChild.cs`
- `public interface IAddChild`
- `public interface IAddChild<T>`

### `src/Avalonia.Base/Metadata/InheritDataTypeFromAttribute.cs`
- Namespace: `Avalonia.Metadata`
- `public enum InheritDataTypeFromScopeKind`
- `public sealed class InheritDataTypeFromAttribute : Attribute`
- `public InheritDataTypeFromAttribute(InheritDataTypeFromScopeKind scopeKind) {`
- `public InheritDataTypeFromScopeKind ScopeKind { get; }`

### `src/Avalonia.Base/Metadata/InheritDataTypeFromItemsAttribute.cs`
- Namespace: `Avalonia.Metadata`
- `public sealed class InheritDataTypeFromItemsAttribute : Attribute`
- `public InheritDataTypeFromItemsAttribute(string ancestorItemsProperty) {`
- `public string AncestorItemsProperty { get; }`
- `public Type? AncestorType { get; set; }`

### `src/Avalonia.Base/Metadata/MarkupExtensionOption.cs`
- Namespace: `Avalonia.Metadata`
- `public sealed class MarkupExtensionOptionAttribute : Attribute`
- `public MarkupExtensionOptionAttribute(object value) {`
- `public object Value { get; }`
- `public int Priority { get; set; } = 0;`
- `public sealed class MarkupExtensionDefaultOptionAttribute : Attribute`

### `src/Avalonia.Base/Metadata/NotClientImplementableAttribute.cs`
- `public sealed class NotClientImplementableAttribute : Attribute`

### `src/Avalonia.Base/Metadata/PrivateApiAttribute.cs`
- Namespace: `Avalonia.Metadata`
- `public sealed class PrivateApiAttribute : Attribute`

### `src/Avalonia.Base/Metadata/TemplateContent.cs`
- `public sealed class TemplateContentAttribute : Attribute`
- `public Type? TemplateResultType { get; set; }`

### `src/Avalonia.Base/Metadata/TrimSurroundingWhitespaceAttribute.cs`
- `public sealed class TrimSurroundingWhitespaceAttribute : Attribute`

### `src/Avalonia.Base/Metadata/UnstableAttribute.cs`
- `public sealed class UnstableAttribute : Attribute`
- `public UnstableAttribute() {`
- `public UnstableAttribute(string? message) {`
- `public string? Message { get; }`

### `src/Avalonia.Base/Metadata/UsableDuringInitializationAttribute.cs`
- `public sealed class UsableDuringInitializationAttribute : Attribute`

### `src/Avalonia.Base/Metadata/WhitespaceSignificantCollectionAttribute.cs`
- `public sealed class WhitespaceSignificantCollectionAttribute : Attribute`

### `src/Avalonia.Base/Metadata/XmlnsDefinitionAttribute.cs`
- `public sealed class XmlnsDefinitionAttribute : Attribute`
- `public XmlnsDefinitionAttribute(string xmlNamespace, string clrNamespace) {`
- `public string XmlNamespace { get; }`
- `public string ClrNamespace { get; }`

### `src/Avalonia.Base/Metadata/XmlnsPrefixAttribute.cs`
- `public sealed class XmlnsPrefixAttribute : Attribute`
- `public XmlnsPrefixAttribute(string xmlNamespace, string prefix) {`
- `public string XmlNamespace { get; }`
- `public string Prefix { get; }`

### `src/Avalonia.Base/PixelPoint.cs`
- `public readonly struct PixelPoint : IEquatable<PixelPoint>`
- `public static readonly PixelPoint Origin = new PixelPoint(0, 0);`
- `public PixelPoint(int x, int y) {`
- `public int X { get; }`
- `public int Y { get; }`
- `public static bool operator ==(PixelPoint left, PixelPoint right) {`
- `public static bool operator !=(PixelPoint left, PixelPoint right) {`
- `public static implicit operator PixelVector(PixelPoint p) {`
- `public static PixelPoint operator +(PixelPoint a, PixelPoint b) {`
- `public static PixelPoint operator +(PixelPoint a, PixelVector b) {`
- `public static PixelPoint operator -(PixelPoint a, PixelPoint b) {`
- `public static PixelPoint operator -(PixelPoint a, PixelVector b) {`
- `public static PixelPoint Parse(string s) {`
- `public bool Equals(PixelPoint other) {`
- `public override bool Equals(object? obj) => obj is PixelPoint other && Equals(other);`
- `public override int GetHashCode() {`
- `public PixelPoint WithX(int x) => new PixelPoint(x, Y);`
- `public PixelPoint WithY(int y) => new PixelPoint(X, y);`
- `public Point ToPoint(double scale) => new Point(X / scale, Y / scale);`
- `public Point ToPoint(Vector scale) => new Point(X / scale.X, Y / scale.Y);`
- `public Point ToPointWithDpi(double dpi) => ToPoint(dpi / 96);`
- `public Point ToPointWithDpi(Vector dpi) => ToPoint(new Vector(dpi.X / 96, dpi.Y / 96));`
- `public static PixelPoint FromPoint(Point point, double scale) => new PixelPoint(`
- `public static PixelPoint FromPoint(Point point, Vector scale) => new PixelPoint(`
- `public static PixelPoint FromPointWithDpi(Point point, double dpi) => FromPoint(point, dpi / 96);`
- `public static PixelPoint FromPointWithDpi(Point point, Vector dpi) => FromPoint(point, new Vector(dpi.X / 96, dpi.Y / 96));`
- `public override string ToString() {`

### `src/Avalonia.Base/PixelRect.cs`
- `public readonly struct PixelRect : IEquatable<PixelRect>`
- `public PixelRect(int x, int y, int width, int height) {`
- `public PixelRect(PixelSize size) {`
- `public PixelRect(PixelPoint position, PixelSize size) {`
- `public PixelRect(PixelPoint topLeft, PixelPoint bottomRight) {`
- `public int X { get; }`
- `public int Y { get; }`
- `public int Width { get; }`
- `public int Height { get; }`
- `public PixelPoint Position => new PixelPoint(X, Y);`
- `public PixelSize Size => new PixelSize(Width, Height);`
- `public int Right => X + Width;`
- `public int Bottom => Y + Height;`
- `public PixelPoint TopLeft => new PixelPoint(X, Y);`
- `public PixelPoint TopRight => new PixelPoint(Right, Y);`
- `public PixelPoint BottomLeft => new PixelPoint(X, Bottom);`
- `public PixelPoint BottomRight => new PixelPoint(Right, Bottom);`
- `public PixelPoint Center => new PixelPoint(X + (Width / 2), Y + (Height / 2));`
- `public static bool operator ==(PixelRect left, PixelRect right) {`
- `public static bool operator !=(PixelRect left, PixelRect right) {`
- `public bool Contains(PixelPoint p) {`
- `public bool ContainsExclusive(PixelPoint p) {`
- `public bool Contains(PixelRect r) {`
- `public PixelRect CenterRect(PixelRect rect) {`
- `public bool Equals(PixelRect other) {`
- `public override bool Equals(object? obj) => obj is PixelRect other && Equals(other);`
- `public override int GetHashCode() {`
- `public PixelRect Intersect(PixelRect rect) {`
- `public bool Intersects(PixelRect rect) {`
- `public PixelRect Translate(PixelVector offset) {`
- `public PixelRect Union(PixelRect rect) {`
- `public PixelRect WithX(int x) {`
- `public PixelRect WithY(int y) {`
- `public PixelRect WithWidth(int width) {`
- `public PixelRect WithHeight(int height) {`
- `public Rect ToRect(double scale) => new Rect(Position.ToPoint(scale), Size.ToSize(scale));`
- `public Rect ToRect(Vector scale) => new Rect(Position.ToPoint(scale), Size.ToSize(scale));`
- `public Rect ToRectWithDpi(double dpi) => new Rect(Position.ToPointWithDpi(dpi), Size.ToSizeWithDpi(dpi));`
- `public Rect ToRectWithDpi(Vector dpi) => new Rect(Position.ToPointWithDpi(dpi), Size.ToSizeWithDpi(dpi));`
- `public static PixelRect FromRect(Rect rect, double scale) => new PixelRect(`
- `public static PixelRect FromRect(Rect rect, Vector scale) => new PixelRect(`
- `public static PixelRect FromRectWithDpi(Rect rect, double dpi) => new PixelRect(`
- `public static PixelRect FromRectWithDpi(Rect rect, Vector dpi) => new PixelRect(`
- `public override string ToString() {`
- `public static PixelRect Parse(string s) {`

### `src/Avalonia.Base/PixelSize.cs`
- `public readonly struct PixelSize : IEquatable<PixelSize>`
- `public static readonly PixelSize Empty = new PixelSize(0, 0);`
- `public PixelSize(int width, int height) {`
- `public double AspectRatio => (double)Width / Height;`
- `public int Width { get; }`
- `public int Height { get; }`
- `public static bool operator ==(PixelSize left, PixelSize right) {`
- `public static bool operator !=(PixelSize left, PixelSize right) {`
- `public static PixelSize Parse(string s) {`
- `public static bool TryParse([NotNullWhen(true)] string? source, out PixelSize result) {`
- `public bool Equals(PixelSize other) {`
- `public override bool Equals(object? obj) => obj is PixelSize other && Equals(other);`
- `public override int GetHashCode() {`
- `public PixelSize WithWidth(int width) => new PixelSize(width, Height);`
- `public PixelSize WithHeight(int height) => new PixelSize(Width, height);`
- `public Size ToSize(double scale) => new Size(Width / scale, Height / scale);`
- `public Size ToSize(Vector scale) => new Size(Width / scale.X, Height / scale.Y);`
- `public Size ToSizeWithDpi(double dpi) => ToSize(dpi / 96);`
- `public Size ToSizeWithDpi(Vector dpi) => ToSize(new Vector(dpi.X / 96, dpi.Y / 96));`
- `public static PixelSize FromSize(Size size, double scale) => new PixelSize(`
- `public static PixelSize FromSize(Size size, Vector scale) => new PixelSize(`
- `public static PixelSize FromSizeWithDpi(Size size, double dpi) => FromSize(size, dpi / 96);`
- `public static PixelSize FromSizeWithDpi(Size size, Vector dpi) => FromSize(size, new Vector(dpi.X / 96, dpi.Y / 96));`
- `public override string ToString() {`

### `src/Avalonia.Base/PixelVector.cs`
- `public readonly struct PixelVector`
- `public PixelVector(int x, int y) {`
- `public int X => _x;`
- `public int Y => _y;`
- `public static explicit operator PixelPoint(PixelVector a) {`
- `public static int operator *(PixelVector a, PixelVector b) {`
- `public static PixelVector operator *(PixelVector vector, int scale) {`
- `public static PixelVector operator /(PixelVector vector, int scale) {`
- `public double Length => Math.Sqrt(X * X + Y * Y);`
- `public static PixelVector operator -(PixelVector a) {`
- `public static PixelVector operator +(PixelVector a, PixelVector b) {`
- `public static PixelVector operator -(PixelVector a, PixelVector b) {`
- `public bool Equals(PixelVector other) {`
- `public bool NearlyEquals(PixelVector other) {`
- `public override bool Equals(object? obj) {`
- `public override int GetHashCode() {`
- `public static bool operator ==(PixelVector left, PixelVector right) {`
- `public static bool operator !=(PixelVector left, PixelVector right) {`
- `public override string ToString() {`
- `public PixelVector WithX(int x) {`
- `public PixelVector WithY(int y) {`

### `src/Avalonia.Base/Platform/AlphaFormat.cs`
- `public enum AlphaFormat`

### `src/Avalonia.Base/Platform/AssetLoader.cs`
- Namespace: `Avalonia.Platform`
- `public static class AssetLoader`
- `public static void SetDefaultAssembly(Assembly assembly) => GetAssetLoader().SetDefaultAssembly(assembly);`
- `public static bool Exists(Uri uri, Uri? baseUri = null) => GetAssetLoader().Exists(uri, baseUri);`
- `public static Stream Open(Uri uri, Uri? baseUri = null) => GetAssetLoader().Open(uri, baseUri);`
- `public static (Stream stream, Assembly assembly) OpenAndGetAssembly(Uri uri, Uri? baseUri = null) => GetAssetLoader().OpenAndGetAssembly(uri, baseUri);`
- `public static Assembly? GetAssembly(Uri uri, Uri? baseUri = null) => GetAssetLoader().GetAssembly(uri, baseUri);`
- `public static IEnumerable<Uri> GetAssets(Uri uri, Uri? baseUri) => GetAssetLoader().GetAssets(uri, baseUri);`
- `public static void InvalidateAssemblyCache(string name) => GetAssetLoader().InvalidateAssemblyCache(name);`
- `public static void InvalidateAssemblyCache() => GetAssetLoader().InvalidateAssemblyCache();`

### `src/Avalonia.Base/Platform/DefaultPlatformSettings.cs`
- `public class DefaultPlatformSettings : IPlatformSettings`
- `public virtual Size GetTapSize(PointerType type) {`
- `public virtual Size GetDoubleTapSize(PointerType type) {`
- `public virtual TimeSpan GetDoubleTapTime(PointerType type) => TimeSpan.FromMilliseconds(500);`
- `public virtual TimeSpan HoldWaitDuration => TimeSpan.FromMilliseconds(300);`
- `public PlatformHotkeyConfiguration HotkeyConfiguration =>`
- `public virtual PlatformColorValues GetColorValues() {`
- `public virtual event EventHandler<PlatformColorValues>? ColorValuesChanged;`

### `src/Avalonia.Base/Platform/IAssetLoader.cs`
- `public interface IAssetLoader`

### `src/Avalonia.Base/Platform/IBitmapImpl.cs`
- `public interface IBitmapImpl : IDisposable`

### `src/Avalonia.Base/Platform/ICursorFactory.cs`
- `public interface ICursorFactory`

### `src/Avalonia.Base/Platform/ICursorImpl.cs`
- `public interface ICursorImpl : IDisposable`

### `src/Avalonia.Base/Platform/IDrawingContextImpl.cs`
- `public interface IDrawingContextImpl : IDisposable`
- `public interface IDrawingContextImplWithEffects : IDrawingContextImpl`
- `public static class DrawingContextImplExtensions`
- `public static T? GetFeature<T>(this IDrawingContextImpl context) where T : class =>`
- `public interface IDrawingContextLayerImpl : IRenderTargetBitmapImpl`
- `public interface IDrawingContextLayerWithRenderContextAffinityImpl : IDrawingContextLayerImpl`

### `src/Avalonia.Base/Platform/IDrawingContextWithAcrylicLikeSupport.cs`
- `public interface IDrawingContextWithAcrylicLikeSupport`

### `src/Avalonia.Base/Platform/IExternalObjectsRenderInterfaceContextFeature.cs`
- Namespace: `Avalonia.Platform`
- `public interface IExternalObjectsRenderInterfaceContextFeature`
- `public byte[]? DeviceUuid { get; }`
- `public byte[]? DeviceLuid { get; }`
- `public interface IExternalObjectsHandleWrapRenderInterfaceContextFeature`
- `public interface IExternalObjectsWrappedGpuHandle : IPlatformHandle, IDisposable`
- `public interface IPlatformRenderInterfaceImportedObject : IDisposable`
- `public interface IPlatformRenderInterfaceImportedImage : IPlatformRenderInterfaceImportedObject`
- `public interface IPlatformRenderInterfaceImportedSemaphore : IPlatformRenderInterfaceImportedObject`

### `src/Avalonia.Base/Platform/IFontManagerImpl.cs`
- `public interface IFontManagerImpl`

### `src/Avalonia.Base/Platform/IGeometryContext.cs`
- `public interface IGeometryContext : IDisposable`

### `src/Avalonia.Base/Platform/IGeometryContext2.cs`
- `public interface IGeometryContext2 : IGeometryContext`

### `src/Avalonia.Base/Platform/IGeometryImpl.cs`
- `public interface IGeometryImpl`

### `src/Avalonia.Base/Platform/IGlyphRunImpl.cs`
- `public interface IGlyphRunImpl : IDisposable`

### `src/Avalonia.Base/Platform/ILockedFramebuffer.cs`
- `public interface ILockedFramebuffer : IDisposable`

### `src/Avalonia.Base/Platform/IMacOSTopLevelPlatformHandle.cs`
- `public interface IMacOSTopLevelPlatformHandle`

### `src/Avalonia.Base/Platform/IOptionalFeatureProvider.cs`
- Namespace: `Avalonia.Platform`
- `public interface IOptionalFeatureProvider`
- `public object? TryGetFeature(Type featureType);`
- `public static class OptionalFeatureProviderExtensions`
- `public static T? TryGetFeature<T>(this IOptionalFeatureProvider provider) where T : class =>`
- `public static bool TryGetFeature<T>(this IOptionalFeatureProvider provider, [MaybeNullWhen(false)] out T rv) where T : class {`

### `src/Avalonia.Base/Platform/IPlatformBehaviorInhibition.cs`
- `public interface IPlatformBehaviorInhibition`

### `src/Avalonia.Base/Platform/IPlatformGpu.cs`
- Namespace: `Avalonia.Platform`
- `public interface IPlatformGraphics`
- `public interface IPlatformGraphicsWithFeatures : IPlatformGraphics, IOptionalFeatureProvider`
- `public interface IPlatformGraphicsReadyStateFeature`
- `public interface IPlatformGraphicsContext : IDisposable, IOptionalFeatureProvider`
- `public class PlatformGraphicsContextLostException : Exception`

### `src/Avalonia.Base/Platform/IPlatformHandle.cs`
- `public interface IPlatformHandle`

### `src/Avalonia.Base/Platform/IPlatformRenderInterface.cs`
- `public interface IPlatformRenderInterface`
- `public AlphaFormat DefaultAlphaFormat { get; }`
- `public PixelFormat DefaultPixelFormat { get; }`
- `public interface IPlatformRenderInterfaceContext : IOptionalFeatureProvider, IDisposable`

### `src/Avalonia.Base/Platform/IPlatformRenderInterfaceRegion.cs`
- Namespace: `Avalonia.Platform`
- `public interface IPlatformRenderInterfaceRegion : IDisposable`

### `src/Avalonia.Base/Platform/IPlatformSettings.cs`
- `public interface IPlatformSettings`

### `src/Avalonia.Base/Platform/IPlatformThreadingInterface.cs`
- `public interface IPlatformThreadingInterface`

### `src/Avalonia.Base/Platform/IReadableBitmapImpl.cs`
- Namespace: `Avalonia.Platform`
- `public interface IReadableBitmapImpl`
- `public interface IReadableBitmapWithAlphaImpl : IReadableBitmapImpl`

### `src/Avalonia.Base/Platform/IRenderTarget.cs`
- `public interface IRenderTarget : IDisposable`
- `public bool IsCorrupted { get; }`
- `public interface IRenderTargetWithProperties : IRenderTarget`
- `public interface IRenderTarget2 : IRenderTarget`

### `src/Avalonia.Base/Platform/IRenderTargetBitmapImpl.cs`
- `public interface IRenderTargetBitmapImpl : IBitmapImpl, IRenderTarget`

### `src/Avalonia.Base/Platform/IRuntimePlatform.cs`
- `public interface IRuntimePlatform`
- `public record struct RuntimePlatformInfo`
- `public FormFactorType FormFactor => IsDesktop ? FormFactorType.Desktop :`
- `public bool IsDesktop { get; set; }`
- `public bool IsMobile { get; set; }`
- `public bool IsTV { get; set; }`
- `public enum FormFactorType`

### `src/Avalonia.Base/Platform/IScopedResource.cs`
- Namespace: `Avalonia.Platform`
- `public interface IScopedResource<T> : IDisposable`
- `public T Value { get; }`
- `public class ScopedResource<T> : IScopedResource<T>`
- `public static IScopedResource<T> Create(T value, Action dispose) => new ScopedResource<T>(value, dispose);`
- `public void Dispose() {`
- `public T Value {`

### `src/Avalonia.Base/Platform/IStreamGeometryContextImpl.cs`
- `public interface IStreamGeometryContextImpl : IGeometryContext`

### `src/Avalonia.Base/Platform/IStreamGeometryImpl.cs`
- `public interface IStreamGeometryImpl : IGeometryImpl`

### `src/Avalonia.Base/Platform/ITextShaperImpl.cs`
- `public interface ITextShaperImpl`

### `src/Avalonia.Base/Platform/ITransformedGeometryImpl.cs`
- `public interface ITransformedGeometryImpl : IGeometryImpl`

### `src/Avalonia.Base/Platform/IWriteableBitmapImpl.cs`
- `public interface IWriteableBitmapImpl : IBitmapImpl, IReadableBitmapWithAlphaImpl`

### `src/Avalonia.Base/Platform/LockedFramebuffer.cs`
- `public class LockedFramebuffer : ILockedFramebuffer`
- `public LockedFramebuffer(IntPtr address, PixelSize size, int rowBytes, Vector dpi, PixelFormat format, Action? onDispose) {`
- `public IntPtr Address { get; }`
- `public PixelSize Size { get; }`
- `public int RowBytes { get; }`
- `public Vector Dpi { get; }`
- `public PixelFormat Format { get; }`
- `public void Dispose() {`

### `src/Avalonia.Base/Platform/LtrbRect.cs`
- Namespace: `Avalonia.Platform`
- `public struct LtrbRect`
- `public double Left, Top, Right, Bottom;`
- `public static bool operator ==(LtrbRect left, LtrbRect right)=>`
- `public static bool operator !=(LtrbRect left, LtrbRect right) =>`
- `public bool Equals(LtrbRect other) =>`
- `public bool Equals(ref LtrbRect other) =>`
- `public override bool Equals(object? obj) {`
- `public override int GetHashCode() {`
- `public struct LtrbPixelRect`
- `public int Left, Top, Right, Bottom;`
- `public static bool operator ==(LtrbPixelRect left, LtrbPixelRect right)=>`
- `public static bool operator !=(LtrbPixelRect left, LtrbPixelRect right) =>`
- `public bool Equals(LtrbPixelRect other) =>`
- `public override bool Equals(object? obj) {`
- `public override int GetHashCode() {`

### `src/Avalonia.Base/Platform/PathGeometryContext.cs`
- `public class PathGeometryContext : IGeometryContext`
- `public PathGeometryContext(PathGeometry pathGeometry) {`
- `public void Dispose() {`
- `public void ArcTo(Point point, Size size, double rotationAngle, bool isLargeArc, SweepDirection sweepDirection) {`
- `public void BeginFigure(Point startPoint, bool isFilled) {`
- `public void CubicBezierTo(Point controlPoint1, Point controlPoint2, Point endPoint) {`
- `public void QuadraticBezierTo(Point controlPoint , Point endPoint) {`
- `public void LineTo(Point endPoint) {`
- `public void EndFigure(bool isClosed) {`
- `public void SetFillRule(FillRule fillRule) {`

### `src/Avalonia.Base/Platform/PixelFormat.cs`
- `public record struct PixelFormat`
- `public int BitsPerPixel {`
- `public static PixelFormat Rgb565 => PixelFormats.Rgb565;`
- `public static PixelFormat Rgba8888 => PixelFormats.Rgba8888;`
- `public static PixelFormat Rgb32 => PixelFormats.Rgb32;`
- `public static PixelFormat Bgra8888 => PixelFormats.Bgra8888;`
- `public override string ToString() => FormatEnum.ToString();`
- `public static class PixelFormats`
- `public static PixelFormat Rgb565 { get; } = new PixelFormat(PixelFormatEnum.Rgb565);`
- `public static PixelFormat Rgba8888 { get; } = new PixelFormat(PixelFormatEnum.Rgba8888);`
- `public static PixelFormat Rgba64 { get; } = new PixelFormat(PixelFormatEnum.Rgba64);`
- `public static PixelFormat Bgra8888 { get; } = new PixelFormat(PixelFormatEnum.Bgra8888);`
- `public static PixelFormat BlackWhite { get; } = new PixelFormat(PixelFormatEnum.BlackWhite);`
- `public static PixelFormat Gray2 { get; } = new PixelFormat(PixelFormatEnum.Gray2);`
- `public static PixelFormat Gray4 { get; } = new PixelFormat(PixelFormatEnum.Gray4);`
- `public static PixelFormat Gray8 { get; } = new PixelFormat(PixelFormatEnum.Gray8);`
- `public static PixelFormat Gray16 { get; } = new PixelFormat(PixelFormatEnum.Gray16);`
- `public static PixelFormat Gray32Float { get; } = new PixelFormat(PixelFormatEnum.Gray32Float);`
- `public static PixelFormat Rgb24 { get; } = new PixelFormat(PixelFormatEnum.Rgb24);`
- `public static PixelFormat Rgb32 { get; } = new PixelFormat(PixelFormatEnum.Rgb32);`
- `public static PixelFormat Bgr24 { get; } = new PixelFormat(PixelFormatEnum.Bgr24);`
- `public static PixelFormat Bgr32 { get; } = new PixelFormat(PixelFormatEnum.Bgr32);`
- `public static PixelFormat Bgr555 { get; } = new PixelFormat(PixelFormatEnum.Bgr555);`
- `public static PixelFormat Bgr565 { get; } = new PixelFormat(PixelFormatEnum.Bgr565);`

### `src/Avalonia.Base/Platform/PlatformColorValues.cs`
- Namespace: `Avalonia.Platform`
- `public enum PlatformThemeVariant`
- `public enum ColorContrastPreference`
- `public record PlatformColorValues`
- `public PlatformThemeVariant ThemeVariant { get; init; }`
- `public ColorContrastPreference ContrastPreference { get; init; }`
- `public Color AccentColor1 { get; init; }`
- `public Color AccentColor2 {`
- `public Color AccentColor3 {`
- `public PlatformColorValues() {`

### `src/Avalonia.Base/Platform/PlatformGraphicsDeviceAdapterDescription.cs`
- Namespace: `Avalonia.Platform`
- `public class PlatformGraphicsDeviceAdapterDescription`
- `public string? Description { get; set; }`
- `public byte[]? DeviceLuid { get; set; }`
- `public byte[]? DeviceUuid { get; set; }`

### `src/Avalonia.Base/Platform/PlatformGraphicsExternalMemory.cs`
- Namespace: `Avalonia.Platform`
- `public record struct PlatformGraphicsExternalImageProperties`
- `public int Width { get; set; }`
- `public int Height { get; set; }`
- `public PlatformGraphicsExternalImageFormat Format { get; set; }`
- `public ulong MemorySize { get; set; }`
- `public ulong MemoryOffset { get; set; }`
- `public bool TopLeftOrigin { get; set; }`
- `public enum PlatformGraphicsExternalImageFormat`
- `public static class KnownPlatformGraphicsExternalImageHandleTypes`
- `public const string D3D11TextureGlobalSharedHandle = nameof(D3D11TextureGlobalSharedHandle);`
- `public const string D3D11TextureNtHandle = nameof(D3D11TextureNtHandle);`
- `public const string VulkanOpaquePosixFileDescriptor = nameof(VulkanOpaquePosixFileDescriptor);`
- `public const string VulkanOpaqueNtHandle = nameof(VulkanOpaqueNtHandle);`
- `public const string VulkanOpaqueKmtHandle = nameof(VulkanOpaqueKmtHandle);`
- `public const string IOSurfaceRef = nameof(IOSurfaceRef);`
- `public static class KnownPlatformGraphicsExternalSemaphoreHandleTypes`
- `public const string VulkanOpaquePosixFileDescriptor = nameof(VulkanOpaquePosixFileDescriptor);`
- `public const string VulkanOpaqueNtHandle = nameof(VulkanOpaqueNtHandle);`
- `public const string VulkanOpaqueKmtHandle = nameof(VulkanOpaqueKmtHandle);`
- `public const string Direct3D12FenceNtHandle = nameof(Direct3D12FenceNtHandle);`
- `public const string MetalSharedEvent = nameof(MetalSharedEvent);`

### `src/Avalonia.Base/Platform/PlatformHandle.cs`
- `public class PlatformHandle : IPlatformHandle, IEquatable<PlatformHandle>`
- `public PlatformHandle(IntPtr handle, string? descriptor) {`
- `public IntPtr Handle { get; }`
- `public string? HandleDescriptor { get; }`
- `public override string ToString() {`
- `public bool Equals(PlatformHandle? other) {`
- `public override bool Equals(object? obj) {`
- `public override int GetHashCode() {`
- `public static bool operator ==(PlatformHandle? left, PlatformHandle? right) {`
- `public static bool operator !=(PlatformHandle? left, PlatformHandle? right) {`

### `src/Avalonia.Base/Platform/RenderTargetProperties.cs`
- Namespace: `Avalonia.Platform`
- `public struct RenderTargetProperties`
- `public bool RetainsPreviousFrameContents { get; init; }`
- `public bool IsSuitableForDirectRendering { get; init; }`
- `public struct RenderTargetDrawingContextProperties`
- `public bool PreviousFrameIsRetained { get; init; }`

### `src/Avalonia.Base/Platform/StandardAssetLoader.cs`
- Namespace: `Avalonia.Platform`
- `public class StandardAssetLoader : IAssetLoader`
- `public StandardAssetLoader(Assembly? assembly = null) : this(new AssemblyDescriptorResolver(), assembly) {`
- `public void SetDefaultAssembly(Assembly assembly) {`
- `public bool Exists(Uri uri, Uri? baseUri = null) {`
- `public Stream Open(Uri uri, Uri? baseUri = null) => OpenAndGetAssembly(uri, baseUri).Item1;`
- `public (Stream stream, Assembly assembly) OpenAndGetAssembly(Uri uri, Uri? baseUri = null) {`
- `public Assembly? GetAssembly(Uri uri, Uri? baseUri) {`
- `public IEnumerable<Uri> GetAssets(Uri uri, Uri? baseUri) {`
- `public void InvalidateAssemblyCache(string name) {`
- `public void InvalidateAssemblyCache() {`
- `public static void RegisterResUriParsers() => AssetLoader.RegisterResUriParsers();`

### `src/Avalonia.Base/Platform/StandardRuntimePlatform.cs`
- `public class StandardRuntimePlatform : IRuntimePlatform`
- `public virtual RuntimePlatformInfo GetRuntimeInfo() => new()`

### `src/Avalonia.Base/Platform/Storage/FilePickerFileType.cs`
- Namespace: `Avalonia.Platform.Storage`
- `public sealed class FilePickerFileType(string? name)`
- `public string Name { get; } = name ?? string.Empty;`
- `public IReadOnlyList<string>? Patterns { get; set; }`
- `public IReadOnlyList<string>? MimeTypes { get; set; }`
- `public IReadOnlyList<string>? AppleUniformTypeIdentifiers { get; set; }`
- `public override string ToString() => Name;`

### `src/Avalonia.Base/Platform/Storage/FilePickerFileTypes.cs`
- `public static class FilePickerFileTypes`
- `public static FilePickerFileType All { get; } = new("All")`

### `src/Avalonia.Base/Platform/Storage/FilePickerOpenOptions.cs`
- Namespace: `Avalonia.Platform.Storage`
- `public class FilePickerOpenOptions : PickerOptions`
- `public FilePickerFileType? SuggestedFileType { get; set; }`
- `public bool AllowMultiple { get; set; }`
- `public IReadOnlyList<FilePickerFileType>? FileTypeFilter { get; set; }`

### `src/Avalonia.Base/Platform/Storage/FilePickerSaveOptions.cs`
- Namespace: `Avalonia.Platform.Storage`
- `public class FilePickerSaveOptions : PickerOptions`
- `public FilePickerFileType? SuggestedFileType { get; set; }`
- `public string? DefaultExtension { get; set; }`
- `public IReadOnlyList<FilePickerFileType>? FileTypeChoices { get; set; }`
- `public bool? ShowOverwritePrompt { get; set; }`

### `src/Avalonia.Base/Platform/Storage/FolderPickerOpenOptions.cs`
- `public class FolderPickerOpenOptions : PickerOptions`
- `public bool AllowMultiple { get; set; }`

### `src/Avalonia.Base/Platform/Storage/ILauncher.cs`
- Namespace: `Avalonia.Platform.Storage`
- `public interface ILauncher`
- `public static class LauncherExtensions`
- `public static Task<bool> LaunchFileInfoAsync(this ILauncher launcher, FileInfo fileInfo) {`
- `public static Task<bool> LaunchDirectoryInfoAsync(this ILauncher launcher, DirectoryInfo directoryInfo) {`

### `src/Avalonia.Base/Platform/Storage/IStorageBookmarkItem.cs`
- Namespace: `Avalonia.Platform.Storage`
- `public interface IStorageBookmarkItem : IStorageItem`
- `public interface IStorageBookmarkFile : IStorageFile, IStorageBookmarkItem`
- `public interface IStorageBookmarkFolder : IStorageFolder, IStorageBookmarkItem`

### `src/Avalonia.Base/Platform/Storage/IStorageFile.cs`
- Namespace: `Avalonia.Platform.Storage`
- `public interface IStorageFile : IStorageItem`

### `src/Avalonia.Base/Platform/Storage/IStorageFolder.cs`
- Namespace: `Avalonia.Platform.Storage`
- `public interface IStorageFolder : IStorageItem`

### `src/Avalonia.Base/Platform/Storage/IStorageItem.cs`
- Namespace: `Avalonia.Platform.Storage`
- `public interface IStorageItem : IDisposable`

### `src/Avalonia.Base/Platform/Storage/IStorageProvider.cs`
- Namespace: `Avalonia.Platform.Storage`
- `public interface IStorageProvider`

### `src/Avalonia.Base/Platform/Storage/PickerOptions.cs`
- Namespace: `Avalonia.Platform.Storage`
- `public class PickerOptions`
- `public string? Title { get; set; }`
- `public IStorageFolder? SuggestedStartLocation { get; set; }`
- `public string? SuggestedFileName { get; set; }`

### `src/Avalonia.Base/Platform/Storage/SaveFilePickerResult.cs`
- Namespace: `Avalonia.Platform.Storage`
- `public readonly struct SaveFilePickerResult`
- `public IStorageFile? File { get; init; }`
- `public FilePickerFileType? SelectedFileType { get; init; }`

### `src/Avalonia.Base/Platform/Storage/StorageItemProperties.cs`
- Namespace: `Avalonia.Platform.Storage`
- `public class StorageItemProperties`
- `public StorageItemProperties( ulong? size = null, DateTimeOffset? dateCreated = null, DateTimeOffset? dateModified = null) {`
- `public ulong? Size { get; }`
- `public DateTimeOffset? DateCreated { get; }`
- `public DateTimeOffset? DateModified { get; }`

### `src/Avalonia.Base/Platform/Storage/StorageProviderExtensions.cs`
- Namespace: `Avalonia.Platform.Storage`
- `public static class StorageProviderExtensions`
- `public static Task<IStorageFile?> TryGetFileFromPathAsync(this IStorageProvider provider, string filePath) {`
- `public static Task<IStorageFolder?> TryGetFolderFromPathAsync(this IStorageProvider provider, string folderPath) {`
- `public static string? TryGetLocalPath(this IStorageItem item) {`

### `src/Avalonia.Base/Platform/Storage/WellKnownFolder.cs`
- `public enum WellKnownFolder`

### `src/Avalonia.Base/Platform/SystemNavigationManagerImpl.cs`
- `public interface ISystemNavigationManagerImpl`
- `public event EventHandler<RoutedEventArgs>? BackRequested;`

### `src/Avalonia.Base/Points.cs`
- Namespace: `Avalonia`
- `public sealed class Points : AvaloniaList<Point>`
- `public Points() {`
- `public Points(IEnumerable<Point> points) : base(points) {`

### `src/Avalonia.Base/Reactive/AnonymousObserver.cs`
- Namespace: `Avalonia.Reactive`
- `public class AnonymousObserver<T> : IObserver<T>`
- `public AnonymousObserver(TaskCompletionSource<T> tcs) {`
- `public AnonymousObserver(Action<T> onNext, Action<Exception> onError, Action onCompleted) {`
- `public AnonymousObserver(Action<T> onNext) : this(onNext, ThrowsOnError, NoOpCompleted) {`
- `public AnonymousObserver(Action<T> onNext, Action<Exception> onError) : this(onNext, onError, NoOpCompleted) {`
- `public AnonymousObserver(Action<T> onNext, Action onCompleted) : this(onNext, ThrowsOnError, onCompleted) {`
- `public void OnCompleted() {`
- `public void OnError(Exception error) {`
- `public void OnNext(T value) {`

### `src/Avalonia.Base/Rect.cs`
- `public readonly struct Rect : IEquatable<Rect>`
- `public Rect(double x, double y, double width, double height) {`
- `public Rect(Size size) {`
- `public Rect(Point position, Size size) {`
- `public Rect(Point topLeft, Point bottomRight) {`
- `public double X => _x;`
- `public double Y => _y;`
- `public double Width => _width;`
- `public double Height => _height;`
- `public Point Position => new Point(_x, _y);`
- `public Size Size => new Size(_width, _height);`
- `public double Right => _x + _width;`
- `public double Bottom => _y + _height;`
- `public double Left => _x;`
- `public double Top => _y;`
- `public Point TopLeft => new Point(_x, _y);`
- `public Point TopRight => new Point(Right, _y);`
- `public Point BottomLeft => new Point(_x, Bottom);`
- `public Point BottomRight => new Point(Right, Bottom);`
- `public Point Center => new Point(_x + (_width / 2), _y + (_height / 2));`
- `public static bool operator ==(Rect left, Rect right) {`
- `public static bool operator !=(Rect left, Rect right) {`
- `public static Rect operator *(Rect rect, Vector scale) {`
- `public static Rect operator *(Rect rect, double scale) {`
- `public static Rect operator /(Rect rect, Vector scale) {`
- `public bool Contains(Point p) {`
- `public bool ContainsExclusive(Point p) {`
- `public bool Contains(Rect r) {`
- `public Rect CenterRect(Rect rect) {`
- `public Rect Inflate(double thickness) {`
- `public Rect Inflate(Thickness thickness) {`
- `public Rect Deflate(double thickness) {`
- `public Rect Deflate(Thickness thickness) {`
- `public bool Equals(Rect other) {`
- `public override bool Equals(object? obj) => obj is Rect other && Equals(other);`
- `public override int GetHashCode() {`
- `public Rect Intersect(Rect rect) {`
- `public bool Intersects(Rect rect) {`
- `public Rect TransformToAABB(Matrix matrix) {`
- `public Rect Translate(Vector offset) {`
- `public Rect Normalize() {`
- `public Rect Union(Rect rect) {`
- `public Rect WithX(double x) {`
- `public Rect WithY(double y) {`
- `public Rect WithWidth(double width) {`
- `public Rect WithHeight(double height) {`
- `public override string ToString() {`
- `public static Rect Parse(string s) {`

### `src/Avalonia.Base/RelativeRect.cs`
- `public readonly struct RelativeRect : IEquatable<RelativeRect>`
- `public static readonly RelativeRect Fill = new RelativeRect(0, 0, 1, 1, RelativeUnit.Relative);`
- `public RelativeRect(double x, double y, double width, double height, RelativeUnit unit) {`
- `public RelativeRect(Rect rect, RelativeUnit unit) {`
- `public RelativeRect(Size size, RelativeUnit unit) {`
- `public RelativeRect(Point position, Size size, RelativeUnit unit) {`
- `public RelativeRect(Point topLeft, Point bottomRight, RelativeUnit unit) {`
- `public RelativeUnit Unit { get; }`
- `public Rect Rect { get; }`
- `public static bool operator ==(RelativeRect left, RelativeRect right) {`
- `public static bool operator !=(RelativeRect left, RelativeRect right) {`
- `public override bool Equals(object? obj) => obj is RelativeRect other && Equals(other);`
- `public bool Equals(RelativeRect p) {`
- `public override int GetHashCode() {`
- `public Rect ToPixels(Size size) {`
- `public Rect ToPixels(Rect boundingBox) {`
- `public static RelativeRect Parse(string s) {`

### `src/Avalonia.Base/RelativeScalar.cs`
- Namespace: `Avalonia`
- `public struct RelativeScalar : IEquatable<RelativeScalar>`
- `public RelativeScalar(double scalar, RelativeUnit unit) {`
- `public double Scalar => _scalar;`
- `public RelativeUnit Unit => _unit;`
- `public static RelativeScalar Beginning { get; } = new RelativeScalar(0, RelativeUnit.Relative);`
- `public static RelativeScalar Middle { get; } = new RelativeScalar(0.5, RelativeUnit.Relative);`
- `public static RelativeScalar End { get; } = new RelativeScalar(1, RelativeUnit.Relative);`
- `public bool Equals(RelativeScalar other) {`
- `public override bool Equals(object? obj) {`
- `public override int GetHashCode() {`
- `public static bool operator ==(RelativeScalar left, RelativeScalar right) {`
- `public static bool operator !=(RelativeScalar left, RelativeScalar right) {`
- `public double ToValue(double size) {`
- `public static RelativeScalar Parse(string s) {`
- `public override string ToString() {`

### `src/Avalonia.Base/RenderTargetCorruptedException.cs`
- `public class RenderTargetCorruptedException : Exception`
- `public RenderTargetCorruptedException() {`
- `public RenderTargetCorruptedException(string message) : base(message) {`
- `public RenderTargetCorruptedException(Exception innerException) : base(null, innerException) {`
- `public RenderTargetCorruptedException(string message, Exception innerException) : base(message, innerException) {`

### `src/Avalonia.Base/RenderTargetNotReadyException.cs`
- Namespace: `Avalonia`
- `public class RenderTargetNotReadyException : Exception`
- `public RenderTargetNotReadyException() {`
- `public RenderTargetNotReadyException(string message) : base(message) {`
- `public RenderTargetNotReadyException(Exception innerException) : base(null, innerException) {`
- `public RenderTargetNotReadyException(string message, Exception innerException) : base(message, innerException) {`

### `src/Avalonia.Base/Rendering/Composition/Animations/CompositionAnimation.cs`
- `public abstract class CompositionAnimation : CompositionObject, ICompositionAnimationBase`
- `public void ClearAllParameters() => _propertySet.ClearAll();`
- `public void ClearParameter(string key) => _propertySet.Clear(key);`
- `public void SetColorParameter(string key, Media.Color value) => SetVariant(key, value);`
- `public void SetMatrix3x2Parameter(string key, Matrix3x2 value) => SetVariant(key, value);`
- `public void SetMatrix4x4Parameter(string key, Matrix4x4 value) => SetVariant(key, value);`
- `public void SetQuaternionParameter(string key, Quaternion value) => SetVariant(key, value);`
- `public void SetReferenceParameter(string key, CompositionObject compositionObject) =>`
- `public void SetScalarParameter(string key, float value) => SetVariant(key, value);`
- `public void SetVector2Parameter(string key, Vector2 value) => SetVariant(key, value);`
- `public void SetVector3Parameter(string key, Vector3 value) => SetVariant(key, value);`
- `public void SetVector4Parameter(string key, Vector4 value) => SetVariant(key, value);`
- `public string? Target { get; set; }`

### `src/Avalonia.Base/Rendering/Composition/Animations/CompositionAnimationGroup.cs`
- `public class CompositionAnimationGroup : CompositionObject, ICompositionAnimationBase`
- `public void Add(CompositionAnimation value) => Animations.Add(value);`
- `public void Remove(CompositionAnimation value) => Animations.Remove(value);`
- `public void RemoveAll() => Animations.Clear();`
- `public CompositionAnimationGroup(Compositor compositor) : base(compositor, null) {`

### `src/Avalonia.Base/Rendering/Composition/Animations/ExpressionAnimation.cs`
- `public sealed class ExpressionAnimation : CompositionAnimation`
- `public string? Expression {`

### `src/Avalonia.Base/Rendering/Composition/Animations/ICompositionAnimationBase.cs`
- `public interface ICompositionAnimationBase`

### `src/Avalonia.Base/Rendering/Composition/Animations/ImplicitAnimationCollection.cs`
- `public sealed class ImplicitAnimationCollection : CompositionObject, IDictionary<string, ICompositionAnimationBase>`
- `public IEnumerator<KeyValuePair<string, ICompositionAnimationBase>> GetEnumerator() => _inner.GetEnumerator();`
- `public void Clear() => _inner.Clear();`
- `public int Count => _inner.Count;`
- `public void Add(string key, ICompositionAnimationBase value) => _inner.Add(key, value);`
- `public bool ContainsKey(string key) => _inner.ContainsKey(key);`
- `public bool Remove(string key) => _inner.Remove(key);`
- `public bool TryGetValue(string key, [MaybeNullWhen(false)] out ICompositionAnimationBase value) =>`
- `public ICompositionAnimationBase this[string key] {`
- `public uint Size => (uint) Count;`
- `public IReadOnlyDictionary<string, ICompositionAnimationBase> GetView() =>`
- `public bool HasKey(string key) => ContainsKey(key);`
- `public void Insert(string key, ICompositionAnimationBase animation) => Add(key, animation);`
- `public ICompositionAnimationBase? Lookup(string key) {`

### `src/Avalonia.Base/Rendering/Composition/Animations/KeyFrameAnimation.cs`
- `public abstract class KeyFrameAnimation : CompositionAnimation`
- `public AnimationDelayBehavior DelayBehavior { get; set; }`
- `public System.TimeSpan DelayTime { get; set; }`
- `public PlaybackDirection Direction { get; set; }`
- `public TimeSpan Duration {`
- `public AnimationIterationBehavior IterationBehavior { get; set; }`
- `public int IterationCount { get; set; } = 1;`
- `public AnimationStopBehavior StopBehavior { get; set; }`
- `public void InsertExpressionKeyFrame(float normalizedProgressKey, string value, Easing? easingFunction = null) =>`
- `public enum AnimationDelayBehavior`
- `public enum AnimationIterationBehavior`
- `public enum AnimationStopBehavior`

### `src/Avalonia.Base/Rendering/Composition/CompositionCustomVisual.cs`
- Namespace: `Avalonia.Rendering.Composition`
- `public sealed class CompositionCustomVisual : CompositionContainerVisual`
- `public void SendHandlerMessage(object message) {`

### `src/Avalonia.Base/Rendering/Composition/CompositionCustomVisualHandler.cs`
- Namespace: `Avalonia.Rendering.Composition`
- `public abstract class CompositionCustomVisualHandler`
- `public virtual void OnMessage(object message) {`
- `public virtual void OnAnimationFrameUpdate() {`
- `public abstract void OnRender(ImmediateDrawingContext drawingContext);`
- `public virtual Rect GetRenderBounds() =>`

### `src/Avalonia.Base/Rendering/Composition/CompositionDrawingSurface.cs`
- Namespace: `Avalonia.Rendering.Composition`
- `public sealed class CompositionDrawingSurface : CompositionSurface, IDisposable`
- `public Task UpdateWithKeyedMutexAsync(ICompositionImportedGpuImage image, uint acquireIndex, uint releaseIndex) {`
- `public Task UpdateWithSemaphoresAsync(ICompositionImportedGpuImage image, ICompositionImportedGpuSemaphore waitForSemaphore, ICompositionImportedGpuSemaphore signalSemaphore) {`
- `public Task UpdateWithTimelineSemaphoresAsync(ICompositionImportedGpuImage image, ICompositionImportedGpuSemaphore waitForSemaphore, ulong waitForValue, ICompositionImportedGpuSemaphore signalSemaphore, ulong signalValue) {`
- `public Task UpdateAsync(ICompositionImportedGpuImage image) {`
- `public new void Dispose() => base.Dispose();`

### `src/Avalonia.Base/Rendering/Composition/CompositionExternalMemory.cs`
- Namespace: `Avalonia.Rendering.Composition`
- `public interface ICompositionGpuInterop`
- `public bool IsLost { get; }`
- `public byte[]? DeviceLuid { get; set; }`
- `public byte[]? DeviceUuid { get; set; }`
- `public enum CompositionGpuImportedImageSynchronizationCapabilities`
- `public interface ICompositionGpuImportedObject : IAsyncDisposable`
- `public interface ICompositionImportedGpuImage : ICompositionGpuImportedObject`
- `public interface ICompositionImportedGpuSemaphore : ICompositionGpuImportedObject`
- `public interface ICompositionImportableSharedGpuContextObject : IDisposable`
- `public interface ICompositionImportableSharedGpuContextImage : IDisposable`
- `public interface ICompositionImportableSharedGpuContextSemaphore : IDisposable`

### `src/Avalonia.Base/Rendering/Composition/CompositionObject.cs`
- `public abstract class CompositionObject : ICompositorSerializable`
- `public ImplicitAnimationCollection? ImplicitAnimations { get; set; }`
- `public Compositor Compositor { get; }`
- `public bool IsDisposed { get; private set; }`
- `public void StartAnimation(string propertyName, CompositionAnimation animation) => StartAnimation(propertyName, animation, null);`
- `public void StopAnimation(string propertyName) {`
- `public void StartAnimationGroup(ICompositionAnimationBase grp) {`
- `public void StopAnimationGroup(ICompositionAnimationBase grp) {`

### `src/Avalonia.Base/Rendering/Composition/CompositionOptions.cs`
- Namespace: `Avalonia.Rendering.Composition`
- `public class CompositionOptions`
- `public bool? UseRegionDirtyRectClipping { get; set; }`
- `public bool? UseSaveLayerRootClip { get; set; }`

### `src/Avalonia.Base/Rendering/Composition/CompositionPropertySet.cs`
- `public sealed class CompositionPropertySet : CompositionObject`
- `public void InsertColor(string propertyName, Avalonia.Media.Color value) => Set(propertyName, value);`
- `public void InsertMatrix3x2(string propertyName, Matrix3x2 value) => Set(propertyName, value);`
- `public void InsertMatrix4x4(string propertyName, Matrix4x4 value) => Set(propertyName, value);`
- `public void InsertQuaternion(string propertyName, Quaternion value) => Set(propertyName, value);`
- `public void InsertScalar(string propertyName, float value) => Set(propertyName, value);`
- `public void InsertVector2(string propertyName, Vector2 value) => Set(propertyName, value);`
- `public void InsertVector3(string propertyName, Vector3 value) => Set(propertyName, value);`
- `public void InsertVector4(string propertyName, Vector4 value) => Set(propertyName, value);`
- `public CompositionGetValueStatus TryGetColor(string propertyName, out Avalonia.Media.Color value) => TryGetVariant(propertyName, out value);`
- `public CompositionGetValueStatus TryGetMatrix3x2(string propertyName, out Matrix3x2 value) => TryGetVariant(propertyName, out value);`
- `public CompositionGetValueStatus TryGetMatrix4x4(string propertyName, out Matrix4x4 value) => TryGetVariant(propertyName, out value);`
- `public CompositionGetValueStatus TryGetQuaternion(string propertyName, out Quaternion value) => TryGetVariant(propertyName, out value);`
- `public CompositionGetValueStatus TryGetScalar(string propertyName, out float value) => TryGetVariant(propertyName, out value);`
- `public CompositionGetValueStatus TryGetVector2(string propertyName, out Vector2 value) => TryGetVariant(propertyName, out value);`
- `public CompositionGetValueStatus TryGetVector3(string propertyName, out Vector3 value) => TryGetVariant(propertyName, out value);`
- `public CompositionGetValueStatus TryGetVector4(string propertyName, out Vector4 value) => TryGetVariant(propertyName, out value);`
- `public void InsertBoolean(string propertyName, bool value) => Set(propertyName, value);`
- `public CompositionGetValueStatus TryGetBoolean(string propertyName, out bool value) => TryGetVariant(propertyName, out value);`
- `public enum CompositionGetValueStatus`

### `src/Avalonia.Base/Rendering/Composition/CompositionSurface.cs`
- Namespace: `Avalonia.Rendering.Composition`
- `public class CompositionSurface : CompositionObject`

### `src/Avalonia.Base/Rendering/Composition/Compositor.Factories.cs`
- Namespace: `Avalonia.Rendering.Composition`
- `public partial class Compositor`
- `public CompositionContainerVisual CreateContainerVisual() => new(this, new ServerCompositionContainerVisual(_server));`
- `public ExpressionAnimation CreateExpressionAnimation() => new ExpressionAnimation(this);`
- `public ExpressionAnimation CreateExpressionAnimation(string expression) => new ExpressionAnimation(this)`
- `public ImplicitAnimationCollection CreateImplicitAnimationCollection() => new ImplicitAnimationCollection(this);`
- `public CompositionAnimationGroup CreateAnimationGroup() => new CompositionAnimationGroup(this);`
- `public CompositionSolidColorVisual CreateSolidColorVisual() =>`
- `public CompositionCustomVisual CreateCustomVisual(CompositionCustomVisualHandler handler) => new(this, handler);`
- `public CompositionSurfaceVisual CreateSurfaceVisual() => new(this, new ServerCompositionSurfaceVisual(_server));`
- `public CompositionDrawingSurface CreateDrawingSurface() => new(this);`

### `src/Avalonia.Base/Rendering/Composition/Compositor.cs`
- `public partial class Compositor`
- `public Compositor(IPlatformGraphics? gpu, bool useUiThreadForSynchronousCommits = false) : this(RenderLoop.LocatorAutoInstance, gpu, useUiThreadForSynchronousCommits) {`
- `public Task RequestCommitAsync() => RequestCompositionBatchCommitAsync().Processed;`
- `public CompositionBatch RequestCompositionBatchCommitAsync() {`
- `public void RequestCompositionUpdate(Action action) {`
- `public async ValueTask<object?> TryGetRenderInterfaceFeature(Type featureType) {`
- `public async Task<Bitmap> CreateCompositionVisualSnapshot(CompositionVisual visual, double scaling) {`
- `public async ValueTask<ICompositionGpuInterop?> TryGetCompositionGpuInterop() {`
- `public static Compositor? TryGetDefaultCompositor() => AvaloniaLocator.Current.GetService<Compositor>();`

### `src/Avalonia.Base/Rendering/Composition/ContainerVisual.cs`
- `public partial class CompositionContainerVisual : CompositionVisual`
- `public CompositionVisualCollection Children { get; private set; } = null!;`

### `src/Avalonia.Base/Rendering/Composition/ElementCompositionPreview.cs`
- Namespace: `Avalonia.Rendering.Composition`
- `public static class ElementComposition`
- `public static CompositionVisual? GetElementVisual(Visual visual) => visual.CompositionVisual;`
- `public static void SetElementChildVisual(Visual visual, CompositionVisual? compositionVisual) {`
- `public static CompositionVisual? GetElementChildVisual(Visual visual) => visual.ChildCompositionVisual;`

### `src/Avalonia.Base/Rendering/Composition/Enums.cs`
- `public enum CompositionBlendMode`
- `public enum CompositionGradientExtendMode`
- `public enum CompositionTileMode`
- `public enum CompositionStretch`

### `src/Avalonia.Base/Rendering/Composition/Server/ServerCompositionVisual.cs`
- `public record struct UpdateResult(LtrbRect? Bounds, bool InvalidatedOld, bool InvalidatedNew)`
- `public UpdateResult() : this(null, false, false) {`
- `public struct ReadbackData`
- `public Matrix Matrix;`
- `public ulong Revision;`
- `public long TargetId;`
- `public bool Visible;`

### `src/Avalonia.Base/Rendering/Composition/Transport/Batch.cs`
- `public sealed class CompositionBatch`
- `public Task Processed => _acceptedTcs.Task;`
- `public Task Rendered => _renderedTcs.Task;`

### `src/Avalonia.Base/Rendering/Composition/Transport/BatchStream.cs`
- Namespace: `Avalonia.Rendering.Composition.Transport`
- `public record struct BatchStreamSegment<TData>`
- `public TData Data { get; set; }`
- `public int ElementCount { get; set; }`

### `src/Avalonia.Base/Rendering/Composition/Transport/ServerListProxyHelper.cs`
- `public interface IRegisterForSerialization`

### `src/Avalonia.Base/Rendering/Composition/Visual.cs`
- `public abstract partial class CompositionVisual`
- `public IBrush? OpacityMask {`

### `src/Avalonia.Base/Rendering/Composition/VisualCollection.cs`
- `public partial class CompositionVisualCollection : CompositionObject`
- `public void InsertAbove(CompositionVisual newChild, CompositionVisual sibling) {`
- `public void InsertBelow(CompositionVisual newChild, CompositionVisual sibling) {`
- `public void InsertAtTop(CompositionVisual newChild) => Insert(_list.Count, newChild);`
- `public void InsertAtBottom(CompositionVisual newChild) => Insert(0, newChild);`
- `public void RemoveAll() => Clear();`

### `src/Avalonia.Base/Rendering/DefaultRenderTimer.cs`
- `public class DefaultRenderTimer : IRenderTimer`
- `public DefaultRenderTimer(int framesPerSecond) {`
- `public int FramesPerSecond { get; }`
- `public event Action<TimeSpan> Tick {`
- `public virtual bool RunsInBackground => true;`

### `src/Avalonia.Base/Rendering/ICustomHitTest.cs`
- `public interface ICustomHitTest`

### `src/Avalonia.Base/Rendering/IRenderRoot.cs`
- `public interface IRenderRoot`
- `public IRenderer Renderer { get; }`
- `public IHitTester HitTester { get; }`

### `src/Avalonia.Base/Rendering/IRenderTimer.cs`
- `public interface IRenderTimer`

### `src/Avalonia.Base/Rendering/IRenderer.cs`
- `public interface IRenderer : IDisposable`
- `public ValueTask<object?> TryGetRenderInterfaceFeature(Type featureType);`
- `public interface IHitTester`

### `src/Avalonia.Base/Rendering/RendererDebugOverlays.cs`
- Namespace: `Avalonia.Rendering`
- `public enum RendererDebugOverlays`

### `src/Avalonia.Base/Rendering/RendererDiagnostics.cs`
- `public class RendererDiagnostics : INotifyPropertyChanged`
- `public RendererDebugOverlays DebugOverlays {`
- `public event PropertyChangedEventHandler? PropertyChanged;`

### `src/Avalonia.Base/Rendering/SceneGraph/CustomDrawOperation.cs`
- `public interface ICustomDrawOperation : IEquatable<ICustomDrawOperation>, IDisposable`

### `src/Avalonia.Base/Rendering/SceneInvalidatedEventArgs.cs`
- `public class SceneInvalidatedEventArgs : EventArgs`
- `public SceneInvalidatedEventArgs( IRenderRoot root, Rect dirtyRect) {`
- `public Rect DirtyRect { get; }`
- `public IRenderRoot RenderRoot { get; }`

### `src/Avalonia.Base/Rendering/SleepLoopRenderTimer.cs`
- `public class SleepLoopRenderTimer : IRenderTimer`
- `public SleepLoopRenderTimer(int fps) {`
- `public event Action<TimeSpan> Tick {`
- `public bool RunsInBackground => true;`

### `src/Avalonia.Base/Rendering/ThreadProxyRenderTimer.cs`
- Namespace: `Avalonia.Rendering`
- `public sealed class ThreadProxyRenderTimer : IRenderTimer`
- `public ThreadProxyRenderTimer(IRenderTimer inner, int maxStackSize = 1 * 1024 * 1024) {`
- `public event Action<TimeSpan> Tick {`
- `public bool RunsInBackground => true;`

### `src/Avalonia.Base/Rendering/UiThreadRenderTimer.cs`
- Namespace: `Avalonia.Rendering`
- `public class UiThreadRenderTimer : DefaultRenderTimer`
- `public UiThreadRenderTimer(int framesPerSecond) : base(framesPerSecond) {`
- `public override bool RunsInBackground => false;`

### `src/Avalonia.Base/Rotate3DTransform.cs`
- Namespace: `Avalonia.Media`
- `public sealed class Rotate3DTransform : Transform`
- `public static readonly StyledProperty<double> AngleXProperty = AvaloniaProperty.Register<Rotate3DTransform, double>(nameof(AngleX));`
- `public static readonly StyledProperty<double> AngleYProperty = AvaloniaProperty.Register<Rotate3DTransform, double>(nameof(AngleY));`
- `public static readonly StyledProperty<double> AngleZProperty = AvaloniaProperty.Register<Rotate3DTransform, double>(nameof(AngleZ));`
- `public static readonly StyledProperty<double> CenterXProperty = AvaloniaProperty.Register<Rotate3DTransform, double>(nameof(CenterX));`
- `public static readonly StyledProperty<double> CenterYProperty = AvaloniaProperty.Register<Rotate3DTransform, double>(nameof(CenterY));`
- `public static readonly StyledProperty<double> CenterZProperty = AvaloniaProperty.Register<Rotate3DTransform, double>(nameof(CenterZ));`
- `public static readonly StyledProperty<double> DepthProperty = AvaloniaProperty.Register<Rotate3DTransform, double>(nameof(Depth));`
- `public Rotate3DTransform() { }`
- `public Rotate3DTransform( double angleX, double angleY, double angleZ, double centerX, double centerY, double centerZ, double depth) : this() {`
- `public double AngleX {`
- `public double AngleY {`
- `public double AngleZ {`
- `public double CenterX {`
- `public double CenterY {`
- `public double CenterZ {`
- `public double Depth {`
- `public override Matrix Value {`

### `src/Avalonia.Base/RoundedRect.cs`
- `public struct RoundedRect`
- `public bool Equals(RoundedRect other) {`
- `public override bool Equals(object? obj) {`
- `public override int GetHashCode() {`
- `public static bool operator ==(RoundedRect left, RoundedRect right) => left.Equals(right);`
- `public static bool operator !=(RoundedRect left, RoundedRect right) => !left.Equals(right);`
- `public Rect Rect { get; }`
- `public Vector RadiiTopLeft { get; }`
- `public Vector RadiiTopRight { get; }`
- `public Vector RadiiBottomLeft { get; }`
- `public Vector RadiiBottomRight { get; }`
- `public RoundedRect( Rect rect, Vector radiiTopLeft, Vector radiiTopRight, Vector radiiBottomRight, Vector radiiBottomLeft) {`
- `public RoundedRect( Rect rect, double radiusTopLeft, double radiusTopRight, double radiusBottomRight, double radiusBottomLeft) : this(rect, new Vector(radiusTopLeft, radiusTopLeft), new Vector(radiusTopRight, radiusTopRight), new Vector(radiusBottomRight, radiusBottomRight), new Vector(radiusBottomLeft, radiusBottomLeft) ) {`
- `public RoundedRect(Rect rect, Vector radii) : this(rect, radii, radii, radii, radii) {`
- `public RoundedRect(Rect rect, double radiusX, double radiusY) : this(rect, new Vector(radiusX, radiusY)) {`
- `public RoundedRect(Rect rect, double radius) : this(rect, radius, radius) {`
- `public RoundedRect(Rect rect) : this(rect, 0) {`
- `public RoundedRect(in Rect bounds, in CornerRadius radius) : this(bounds, radius.TopLeft, radius.TopRight, radius.BottomRight, radius.BottomLeft) {`
- `public static implicit operator RoundedRect(Rect r) => new RoundedRect(r);`
- `public bool IsRounded => RadiiTopLeft != default || RadiiTopRight != default || RadiiBottomRight != default ||`
- `public bool IsUniform =>`
- `public RoundedRect Inflate(double dx, double dy) {`
- `public unsafe RoundedRect Deflate(double dx, double dy) {`
- `public bool ContainsExclusive(Point p) {`

### `src/Avalonia.Base/StyledElement.cs`
- `public class StyledElement : Animatable,`
- `public static readonly StyledProperty<object?> DataContextProperty = AvaloniaProperty.Register<StyledElement, object?>( nameof(DataContext), defaultValue: null, inherits: true, defaultBindingMode: BindingMode.OneWay, validate: null, coerce: null, enableDataValidation: false, notifying: DataContextNotifying);`
- `public static readonly DirectProperty<StyledElement, string?> NameProperty = AvaloniaProperty.RegisterDirect<StyledElement, string?>(nameof(Name), o => o.Name, (o, v) => o.Name = v);`
- `public static readonly DirectProperty<StyledElement, StyledElement?> ParentProperty = AvaloniaProperty.RegisterDirect<StyledElement, StyledElement?>(nameof(Parent), o => o.Parent);`
- `public static readonly DirectProperty<StyledElement, AvaloniaObject?> TemplatedParentProperty = AvaloniaProperty.RegisterDirect<StyledElement, AvaloniaObject?>( nameof(TemplatedParent), o => o.TemplatedParent);`
- `public static readonly StyledProperty<ControlTheme?> ThemeProperty = AvaloniaProperty.Register<StyledElement, ControlTheme?>(nameof(Theme));`
- `public StyledElement() {`
- `public event EventHandler<LogicalTreeAttachmentEventArgs>? AttachedToLogicalTree;`
- `public event EventHandler<LogicalTreeAttachmentEventArgs>? DetachedFromLogicalTree;`
- `public event EventHandler? DataContextChanged;`
- `public event EventHandler? Initialized;`
- `public event EventHandler<ResourcesChangedEventArgs>? ResourcesChanged;`
- `public event EventHandler? ActualThemeVariantChanged;`
- `public string? Name {`
- `public Classes Classes => _classes ??= new();`
- `public object? DataContext {`
- `public bool IsInitialized { get; private set; }`
- `public Styles Styles => _styles ??= new Styles(this);`
- `public Type StyleKey => StyleKeyOverride;`
- `public IResourceDictionary Resources {`
- `public AvaloniaObject? TemplatedParent {`
- `public ControlTheme? Theme {`
- `public StyledElement? Parent { get; private set; }`
- `public ThemeVariant ActualThemeVariant => GetValue(ThemeVariant.ActualThemeVariantProperty);`
- `public virtual void BeginInit() {`
- `public virtual void EndInit() {`
- `public bool ApplyStyling() {`
- `public bool TryGetResource(object key, ThemeVariant? theme, out object? value) {`

### `src/Avalonia.Base/StyledElementExtensions.cs`
- `public static class StyledElementExtensions`
- `public static IDisposable BindClass(this StyledElement target, string className, IBinding source, object anchor) =>`
- `public static AvaloniaProperty GetClassProperty(string className) =>`

### `src/Avalonia.Base/StyledProperty.cs`
- `public class StyledProperty<TValue> : AvaloniaProperty<TValue>, IStyledPropertyAccessor`
- `public Func<TValue, bool>? ValidateValue { get; }`
- `public StyledProperty<TValue> AddOwner<TOwner>(StyledPropertyMetadata<TValue>? metadata = null) where TOwner : AvaloniaObject {`
- `public TValue CoerceValue(AvaloniaObject instance, TValue baseValue) {`
- `public TValue GetDefaultValue(Type type) {`
- `public TValue GetDefaultValue(AvaloniaObject owner) {`
- `public new StyledPropertyMetadata<TValue> GetMetadata(Type type) => CastMetadata(base.GetMetadata(type));`
- `public new StyledPropertyMetadata<TValue> GetMetadata(AvaloniaObject owner) => CastMetadata(base.GetMetadata(owner));`
- `public void OverrideDefaultValue<T>(TValue defaultValue) where T : AvaloniaObject {`
- `public void OverrideDefaultValue(Type type, TValue defaultValue) {`
- `public void OverrideMetadata<T>(StyledPropertyMetadata<TValue> metadata) where T : AvaloniaObject => OverrideMetadata(typeof(T), metadata);`
- `public void OverrideMetadata(Type type, StyledPropertyMetadata<TValue> metadata) {`
- `public override string ToString() {`

### `src/Avalonia.Base/StyledPropertyMetadata`1.cs`
- `public class StyledPropertyMetadata<TValue> : AvaloniaPropertyMetadata, IStyledPropertyMetadata`
- `public StyledPropertyMetadata( Optional<TValue> defaultValue = default, BindingMode defaultBindingMode = BindingMode.Default, Func<AvaloniaObject, TValue, TValue>? coerce = null, bool enableDataValidation = false) : base(defaultBindingMode, enableDataValidation) {`
- `public TValue DefaultValue {`
- `public Func<AvaloniaObject, TValue, TValue>? CoerceValue { get; private set; }`
- `public override void Merge(AvaloniaPropertyMetadata baseMetadata, AvaloniaProperty property) {`
- `public override AvaloniaPropertyMetadata GenerateTypeSafeMetadata() {`

### `src/Avalonia.Base/Styling/Container.cs`
- `public static class Container`
- `public static readonly AttachedProperty<string?> NameProperty = AvaloniaProperty.RegisterAttached<Layoutable, string?>("Name", typeof(Container));`
- `public static readonly AttachedProperty<ContainerSizing> SizingProperty = AvaloniaProperty.RegisterAttached<Layoutable, ContainerSizing>("Sizing", typeof(Container), coerce:UpdateQueryProvider);`
- `public static string? GetName(Layoutable layoutable) {`
- `public static void SetName(Layoutable layoutable, string? name) {`
- `public static ContainerSizing GetSizing(Layoutable layoutable) {`
- `public static void SetSizing(Layoutable layoutable, ContainerSizing sizing) {`

### `src/Avalonia.Base/Styling/ContainerQuery.cs`
- `public class ContainerQuery`
- `public ContainerQuery() {`
- `public ContainerQuery(Func<StyleQuery?, StyleQuery> query, string? containerName = null) {`
- `public StyleQuery? Query {`
- `public string? Name {`
- `public override string ToString() => Query?.ToString(this) ?? "ContainerQuery";`

### `src/Avalonia.Base/Styling/ContainerSizing.cs`
- `public enum ContainerSizing`

### `src/Avalonia.Base/Styling/ControlTheme.cs`
- `public class ControlTheme : StyleBase`
- `public ControlTheme() { }`
- `public ControlTheme(Type targetType) => TargetType = targetType;`
- `public Type? TargetType { get; set; }`
- `public ControlTheme? BasedOn { get; set; }`
- `public override string ToString() => TargetType?.Name ?? "ControlTheme";`

### `src/Avalonia.Base/Styling/IGlobalStyles.cs`
- `public interface IGlobalStyles : IStyleHost`
- `public event Action<IReadOnlyList<IStyle>>? GlobalStylesAdded;`
- `public event Action<IReadOnlyList<IStyle>>? GlobalStylesRemoved;`

### `src/Avalonia.Base/Styling/ISetterInstance.cs`
- `public interface ISetterInstance`

### `src/Avalonia.Base/Styling/ISetterValue.cs`
- `public interface ISetterValue`

### `src/Avalonia.Base/Styling/IStyle.cs`
- `public interface IStyle : IResourceNode`

### `src/Avalonia.Base/Styling/IStyleHost.cs`
- `public interface IStyleHost`

### `src/Avalonia.Base/Styling/IStyleable.cs`
- `public interface IStyleable : INamed`

### `src/Avalonia.Base/Styling/ITemplate.cs`
- `public interface ITemplate`

### `src/Avalonia.Base/Styling/IThemeVariantHost.cs`
- Namespace: `Avalonia.Styling`
- `public interface IThemeVariantHost : IResourceHost`

### `src/Avalonia.Base/Styling/Selector.cs`
- `public abstract class Selector`
- `public override string ToString() => ToString(null);`
- `public abstract string ToString(Style? owner);`

### `src/Avalonia.Base/Styling/Selectors.cs`
- `public static class Selectors`
- `public static Selector Child(this Selector previous) {`
- `public static Selector Class(this Selector? previous, string name) {`
- `public static Selector Descendant(this Selector? previous) {`
- `public static Selector Is(this Selector? previous, Type type) {`
- `public static Selector Is<T>(this Selector? previous) where T : StyledElement {`
- `public static Selector Name(this Selector? previous, string name) {`
- `public static Selector Nesting(this Selector? previous) {`
- `public static Selector Not(this Selector? previous, Func<Selector?, Selector> argument) {`
- `public static Selector Not(this Selector? previous, Selector argument) {`
- `public static Selector NthChild(this Selector? previous, int step, int offset) {`
- `public static Selector NthLastChild(this Selector? previous, int step, int offset) {`
- `public static Selector OfType(this Selector? previous, Type type) {`
- `public static Selector OfType<T>(this Selector? previous) where T : StyledElement {`
- `public static Selector Or(params Selector[] selectors) {`
- `public static Selector Or(IReadOnlyList<Selector> selectors) {`
- `public static Selector PropertyEquals<T>(this Selector? previous, AvaloniaProperty<T> property, object? value) {`
- `public static Selector PropertyEquals(this Selector? previous, AvaloniaProperty property, object? value) {`
- `public static Selector Template(this Selector previous) {`

### `src/Avalonia.Base/Styling/Setter.cs`
- `public class Setter : SetterBase, IValueEntry, ISetterInstance, IAnimationSetter`
- `public Setter() {`
- `public Setter(AvaloniaProperty property, object? value) {`
- `public AvaloniaProperty? Property { get; set; }`
- `public object? Value {`
- `public override string ToString() => $"Setter: {Property} = {Value}";`

### `src/Avalonia.Base/Styling/SetterBase.cs`
- `public abstract class SetterBase`

### `src/Avalonia.Base/Styling/Style.cs`
- `public class Style : StyleBase`
- `public Style() {`
- `public Style(Func<Selector?, Selector> selector) {`
- `public Selector? Selector {`
- `public override string ToString() => Selector?.ToString(this) ?? "Style";`

### `src/Avalonia.Base/Styling/StyleBase.cs`
- `public abstract class StyleBase : AvaloniaObject, IStyle, IResourceProvider`
- `public IList<IStyle> Children => _children ??= new(this);`
- `public IResourceHost? Owner {`
- `public IStyle? Parent { get; private set; }`
- `public IResourceDictionary Resources {`
- `public IList<SetterBase> Setters => _setters ??= new();`
- `public IList<IAnimation> Animations => _animations ??= new List<IAnimation>();`
- `public void Add(SetterBase setter) => Setters.Add(setter);`
- `public void Add(IStyle style) => Children.Add(style);`
- `public event EventHandler? OwnerChanged;`
- `public bool TryGetResource(object key, ThemeVariant? themeVariant, out object? result) {`

### `src/Avalonia.Base/Styling/StyleQueries.cs`
- `public static class StyleQueries`
- `public static StyleQuery Width(this StyleQuery? previous, StyleQueryComparisonOperator @operator, double value) {`
- `public static StyleQuery Height(this StyleQuery? previous, StyleQueryComparisonOperator @operator, double value) {`
- `public static StyleQuery Or(params StyleQuery[] queries) {`
- `public static StyleQuery Or(IReadOnlyList<StyleQuery> query) {`
- `public static StyleQuery And(params StyleQuery[] queries) {`
- `public static StyleQuery And(IReadOnlyList<StyleQuery> query) {`

### `src/Avalonia.Base/Styling/StyleQuery.cs`
- `public abstract class StyleQuery`
- `public override string ToString() => ToString(null);`
- `public abstract string ToString(ContainerQuery? owner);`

### `src/Avalonia.Base/Styling/StyleQueryComparisonOperator.cs`
- `public enum StyleQueryComparisonOperator`

### `src/Avalonia.Base/Styling/Styles.cs`
- `public class Styles : AvaloniaObject,`
- `public Styles() {`
- `public Styles(IResourceHost owner) : this() {`
- `public event NotifyCollectionChangedEventHandler? CollectionChanged;`
- `public event EventHandler? OwnerChanged;`
- `public int Count => _styles.Count;`
- `public IResourceHost? Owner {`
- `public IResourceDictionary Resources {`
- `public IStyle this[int index] {`
- `public bool TryGetResource(object key, ThemeVariant? theme, out object? value) {`
- `public void AddRange(IEnumerable<IStyle> items) => _styles.AddRange(items);`
- `public void InsertRange(int index, IEnumerable<IStyle> items) => _styles.InsertRange(index, items);`
- `public void Move(int oldIndex, int newIndex) => _styles.Move(oldIndex, newIndex);`
- `public void MoveRange(int oldIndex, int count, int newIndex) => _styles.MoveRange(oldIndex, count, newIndex);`
- `public void RemoveAll(IEnumerable<IStyle> items) => _styles.RemoveAll(items);`
- `public void RemoveRange(int index, int count) => _styles.RemoveRange(index, count);`
- `public int IndexOf(IStyle item) => _styles.IndexOf(item);`
- `public void Insert(int index, IStyle item) => _styles.Insert(index, item);`
- `public void RemoveAt(int index) => _styles.RemoveAt(index);`
- `public void Add(IStyle item) => _styles.Add(item);`
- `public void Clear() => _styles.Clear();`
- `public bool Contains(IStyle item) => _styles.Contains(item);`
- `public void CopyTo(IStyle[] array, int arrayIndex) => _styles.CopyTo(array, arrayIndex);`
- `public bool Remove(IStyle item) => _styles.Remove(item);`
- `public AvaloniaList<IStyle>.Enumerator GetEnumerator() => _styles.GetEnumerator();`

### `src/Avalonia.Base/Styling/ThemeVariant.cs`
- Namespace: `Avalonia.Styling`
- `public sealed record ThemeVariant`
- `public ThemeVariant(object key, ThemeVariant? inheritVariant) {`
- `public object Key { get; }`
- `public ThemeVariant? InheritVariant { get; }`
- `public static ThemeVariant Default { get; } = new(nameof(Default));`
- `public static ThemeVariant Light { get; } = new(nameof(Light));`
- `public static ThemeVariant Dark { get; } = new(nameof(Dark));`
- `public override string ToString() {`
- `public override int GetHashCode() {`
- `public bool Equals(ThemeVariant? other) {`
- `public static explicit operator ThemeVariant(PlatformThemeVariant themeVariant) {`
- `public static explicit operator PlatformThemeVariant?(ThemeVariant themeVariant) {`

### `src/Avalonia.Base/Styling/ThemeVariantTypeConverter.cs`
- Namespace: `Avalonia.Styling`
- `public class ThemeVariantTypeConverter : TypeConverter`
- `public override bool CanConvertFrom(ITypeDescriptorContext? context, Type sourceType) {`
- `public override object ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object value) {`

### `src/Avalonia.Base/Threading/AvaloniaSynchronizationContext.cs`
- `public class AvaloniaSynchronizationContext : SynchronizationContext`
- `public AvaloniaSynchronizationContext() : this(Dispatcher.UIThread, DispatcherPriority.Default, Thread.CurrentThread.GetApartmentState() == ApartmentState.STA) {`
- `public AvaloniaSynchronizationContext(DispatcherPriority priority) : this(Dispatcher.UIThread, priority, false) {`
- `public AvaloniaSynchronizationContext(Dispatcher dispatcher, DispatcherPriority priority) : this(dispatcher, priority, false) {`
- `public static bool AutoInstall { get; set; } = true;`
- `public static void InstallIfNeeded() {`
- `public override void Post(SendOrPostCallback d, object? state) {`
- `public override void Send(SendOrPostCallback d, object? state) {`
- `public override int Wait(IntPtr[] waitHandles, bool waitAll, int millisecondsTimeout) {`
- `public record struct RestoreContext : IDisposable`
- `public void Dispose() {`
- `public static RestoreContext Ensure(DispatcherPriority priority) => Ensure(Dispatcher.UIThread, priority);`
- `public static RestoreContext Ensure(Dispatcher dispatcher, DispatcherPriority priority) {`

### `src/Avalonia.Base/Threading/Dispatcher.Exceptions.cs`
- Namespace: `Avalonia.Threading`
- `public partial class Dispatcher`
- `public event DispatcherUnhandledExceptionEventHandler? UnhandledException;`
- `public event DispatcherUnhandledExceptionFilterEventHandler? UnhandledExceptionFilter {`

### `src/Avalonia.Base/Threading/Dispatcher.Invoke.cs`
- Namespace: `Avalonia.Threading`
- `public partial class Dispatcher`
- `public void Invoke(Action callback) {`
- `public void Invoke(Action callback, DispatcherPriority priority) {`
- `public void Invoke(Action callback, DispatcherPriority priority, CancellationToken cancellationToken) {`
- `public void Invoke(Action callback, DispatcherPriority priority, CancellationToken cancellationToken, TimeSpan timeout) {`
- `public TResult Invoke<TResult>(Func<TResult> callback) {`
- `public TResult Invoke<TResult>(Func<TResult> callback, DispatcherPriority priority) {`
- `public TResult Invoke<TResult>(Func<TResult> callback, DispatcherPriority priority, CancellationToken cancellationToken) {`
- `public TResult Invoke<TResult>(Func<TResult> callback, DispatcherPriority priority, CancellationToken cancellationToken, TimeSpan timeout) {`
- `public DispatcherOperation InvokeAsync(Action callback) {`
- `public DispatcherOperation InvokeAsync(Action callback, DispatcherPriority priority) {`
- `public DispatcherOperation InvokeAsync(Action callback, DispatcherPriority priority, CancellationToken cancellationToken) {`
- `public DispatcherOperation<TResult> InvokeAsync<TResult>(Func<TResult> callback) {`
- `public DispatcherOperation<TResult> InvokeAsync<TResult>(Func<TResult> callback, DispatcherPriority priority) {`
- `public DispatcherOperation<TResult> InvokeAsync<TResult>(Func<TResult> callback, DispatcherPriority priority, CancellationToken cancellationToken) {`
- `public void Post(Action action, DispatcherPriority priority = default) {`
- `public Task InvokeAsync(Func<Task> callback) => InvokeAsync(callback, DispatcherPriority.Default);`
- `public Task InvokeAsync(Func<Task> callback, DispatcherPriority priority) {`
- `public Task<TResult> InvokeAsync<TResult>(Func<Task<TResult>> action) =>`
- `public Task<TResult> InvokeAsync<TResult>(Func<Task<TResult>> action, DispatcherPriority priority) {`
- `public void Post(SendOrPostCallback action, object? arg, DispatcherPriority priority = default) {`
- `public DispatcherPriorityAwaitable AwaitWithPriority(Task task, DispatcherPriority priority) =>`
- `public DispatcherPriorityAwaitable<T> AwaitWithPriority<T>(Task<T> task, DispatcherPriority priority) =>`

### `src/Avalonia.Base/Threading/Dispatcher.MainLoop.cs`
- Namespace: `Avalonia.Threading`
- `public partial class Dispatcher`
- `public event EventHandler? ShutdownStarted;`
- `public event EventHandler? ShutdownFinished;`
- `public void PushFrame(DispatcherFrame frame) {`
- `public void MainLoop(CancellationToken cancellationToken) {`
- `public void ExitAllFrames() {`
- `public void BeginInvokeShutdown(DispatcherPriority priority) => Post(StartShutdownImpl, priority);`
- `public void InvokeShutdown() => Invoke(StartShutdownImpl, DispatcherPriority.Send);`
- `public record struct DispatcherProcessingDisabled : IDisposable`
- `public void Dispose() {`
- `public DispatcherProcessingDisabled DisableProcessing() {`

### `src/Avalonia.Base/Threading/Dispatcher.Queue.cs`
- Namespace: `Avalonia.Threading`
- `public partial class Dispatcher`
- `public void RunJobs(DispatcherPriority? priority = null) {`
- `public bool HasJobsWithPriority(DispatcherPriority priority) {`

### `src/Avalonia.Base/Threading/Dispatcher.Timers.cs`
- Namespace: `Avalonia.Threading`
- `public partial class Dispatcher`

### `src/Avalonia.Base/Threading/Dispatcher.cs`
- Namespace: `Avalonia.Threading`
- `public partial class Dispatcher : IDispatcher`
- `public static Dispatcher UIThread {`
- `public bool SupportsRunLoops => _controlledImpl != null;`
- `public bool CheckAccess() => _impl.CurrentThreadIsLoopThread;`
- `public void VerifyAccess() {`

### `src/Avalonia.Base/Threading/DispatcherEventArgs.cs`
- Namespace: `Avalonia.Threading`
- `public abstract class DispatcherEventArgs : EventArgs`
- `public Dispatcher Dispatcher { get; }`

### `src/Avalonia.Base/Threading/DispatcherFrame.cs`
- Namespace: `Avalonia.Threading`
- `public class DispatcherFrame`
- `public DispatcherFrame() : this(true) {`
- `public Dispatcher Dispatcher { get; }`
- `public DispatcherFrame(bool exitWhenRequested) : this(Dispatcher.UIThread, exitWhenRequested) {`
- `public bool Continue {`

### `src/Avalonia.Base/Threading/DispatcherOperation.cs`
- Namespace: `Avalonia.Threading`
- `public class DispatcherOperation`
- `public DispatcherOperationStatus Status { get; internal set; }`
- `public Dispatcher Dispatcher { get; }`
- `public DispatcherPriority Priority {`
- `public event EventHandler Aborted {`
- `public event EventHandler Completed {`
- `public bool Abort() {`
- `public void Wait() => Wait(TimeSpan.FromMilliseconds(-1));`
- `public void Wait(TimeSpan timeout) {`
- `public Task GetTask() => GetTaskCore();`
- `public TaskAwaiter GetAwaiter() {`
- `public class DispatcherOperation<T> : DispatcherOperation`
- `public DispatcherOperation(Dispatcher dispatcher, DispatcherPriority priority, Func<T> callback) : base(dispatcher, priority, false) {`
- `public new TaskAwaiter<T> GetAwaiter() => GetTask().GetAwaiter();`
- `public new Task<T> GetTask() => TaskCompletionSource!.Task;`
- `public T Result {`
- `public enum DispatcherOperationStatus`

### `src/Avalonia.Base/Threading/DispatcherOptions.cs`
- Namespace: `Avalonia.Threading`
- `public class DispatcherOptions`
- `public TimeSpan InputStarvationTimeout { get; set; } = TimeSpan.FromSeconds(1);`

### `src/Avalonia.Base/Threading/DispatcherPriority.cs`
- `public readonly struct DispatcherPriority : IEquatable<DispatcherPriority>, IComparable<DispatcherPriority>`
- `public int Value { get; }`
- `public static readonly DispatcherPriority Default = new(0);`
- `public static readonly DispatcherPriority Input = new(Default - 1);`
- `public static readonly DispatcherPriority Background = new(Input - 1);`
- `public static readonly DispatcherPriority ContextIdle = new(Background - 1);`
- `public static readonly DispatcherPriority ApplicationIdle = new (ContextIdle - 1);`
- `public static readonly DispatcherPriority SystemIdle = new(ApplicationIdle - 1);`
- `public static readonly DispatcherPriority Inactive = new(MinimumActiveValue - 1);`
- `public static readonly DispatcherPriority Invalid = new(MinimumActiveValue - 2);`
- `public static readonly DispatcherPriority Loaded = new(Default + 1);`
- `public static readonly DispatcherPriority UiThreadRender = new(Loaded + 1);`
- `public static readonly DispatcherPriority Render = new(AfterRender + 1);`
- `public static readonly DispatcherPriority BeforeRender = new(Render + 1);`
- `public static readonly DispatcherPriority AsyncRenderTargetResize = new(BeforeRender + 1);`
- `public static readonly DispatcherPriority Normal = new(DataBind + 1);`
- `public static readonly DispatcherPriority Send = new(Normal + 1);`
- `public static readonly DispatcherPriority MaxValue = Send;`
- `public static DispatcherPriority FromValue(int value) {`
- `public static implicit operator int(DispatcherPriority priority) => priority.Value;`
- `public static implicit operator DispatcherPriority(int value) => FromValue(value);`
- `public bool Equals(DispatcherPriority other) => Value == other.Value;`
- `public override bool Equals(object? obj) => obj is DispatcherPriority other && Equals(other);`
- `public override int GetHashCode() => Value.GetHashCode();`
- `public static bool operator ==(DispatcherPriority left, DispatcherPriority right) => left.Value == right.Value;`
- `public static bool operator !=(DispatcherPriority left, DispatcherPriority right) => left.Value != right.Value;`
- `public static bool operator <(DispatcherPriority left, DispatcherPriority right) => left.Value < right.Value;`
- `public static bool operator >(DispatcherPriority left, DispatcherPriority right) => left.Value > right.Value;`
- `public static bool operator <=(DispatcherPriority left, DispatcherPriority right) => left.Value <= right.Value;`
- `public static bool operator >=(DispatcherPriority left, DispatcherPriority right) => left.Value >= right.Value;`
- `public int CompareTo(DispatcherPriority other) => Value.CompareTo(other.Value);`
- `public static void Validate(DispatcherPriority priority, string parameterName) {`
- `public override string ToString() {`

### `src/Avalonia.Base/Threading/DispatcherPriorityAwaitable.cs`
- Namespace: `Avalonia.Threading`
- `public class DispatcherPriorityAwaitable : INotifyCompletion`
- `public void OnCompleted(Action continuation) =>`
- `public bool IsCompleted => Task.IsCompleted;`
- `public void GetResult() => Task.GetAwaiter().GetResult();`
- `public DispatcherPriorityAwaitable GetAwaiter() => this;`
- `public sealed class DispatcherPriorityAwaitable<T> : DispatcherPriorityAwaitable`
- `public new T GetResult() => ((Task<T>)Task).GetAwaiter().GetResult();`
- `public new DispatcherPriorityAwaitable<T> GetAwaiter() => this;`

### `src/Avalonia.Base/Threading/DispatcherTimer.cs`
- Namespace: `Avalonia.Threading`
- `public partial class DispatcherTimer`
- `public DispatcherTimer() : this(DispatcherPriority.Background) {`
- `public DispatcherTimer(DispatcherPriority priority) : this(Threading.Dispatcher.UIThread, priority, TimeSpan.FromMilliseconds(0)) {`
- `public DispatcherTimer(TimeSpan interval, DispatcherPriority priority, EventHandler callback) : this(Threading.Dispatcher.UIThread, priority, interval) {`
- `public Dispatcher Dispatcher {`
- `public bool IsEnabled {`
- `public TimeSpan Interval {`
- `public void Start() {`
- `public void Stop() {`
- `public static IDisposable Run(Func<bool> action, TimeSpan interval, DispatcherPriority priority = default) {`
- `public static IDisposable RunOnce( Action action, TimeSpan interval, DispatcherPriority priority = default) {`
- `public event EventHandler? Tick;`
- `public object? Tag { get; set; }`

### `src/Avalonia.Base/Threading/DispatcherUnhandledExceptionEventArgs.cs`
- Namespace: `Avalonia.Threading`
- `public sealed class DispatcherUnhandledExceptionEventArgs : DispatcherEventArgs`
- `public Exception Exception => _exception;`
- `public bool Handled {`

### `src/Avalonia.Base/Threading/DispatcherUnhandledExceptionFilterEventArgs.cs`
- Namespace: `Avalonia.Threading`
- `public sealed class DispatcherUnhandledExceptionFilterEventArgs : DispatcherEventArgs`
- `public Exception Exception => _exception!;`
- `public bool RequestCatch {`

### `src/Avalonia.Base/Threading/IDispatcher.cs`
- `public interface IDispatcher`

### `src/Avalonia.Base/Threading/IDispatcherImpl.cs`
- Namespace: `Avalonia.Threading`
- `public interface IDispatcherImpl`
- `public interface IDispatcherImplWithPendingInput : IDispatcherImpl`
- `public interface IDispatcherImplWithExplicitBackgroundProcessing : IDispatcherImpl`
- `public interface IControlledDispatcherImpl : IDispatcherImplWithPendingInput`

### `src/Avalonia.Base/Utilities/IWeakEventSubscriber.cs`
- Namespace: `Avalonia.Utilities`
- `public interface IWeakEventSubscriber<in TEventArgs>`
- `public sealed class WeakEventSubscriber<TEventArgs> : IWeakEventSubscriber<TEventArgs>`
- `public event Action<object?, WeakEvent, TEventArgs>? Event;`
- `public sealed class TargetWeakEventSubscriber<TTarget, TEventArgs> : IWeakEventSubscriber<TEventArgs>`
- `public TargetWeakEventSubscriber(TTarget target, Action<TTarget, object?, WeakEvent, TEventArgs> dispatchFunc) {`

### `src/Avalonia.Base/Utilities/ImmutableReadOnlyListStructEnumerator.cs`
- `public struct ImmutableReadOnlyListStructEnumerator<T> : IEnumerator<T>`
- `public ImmutableReadOnlyListStructEnumerator(IReadOnlyList<T> readOnlyList) {`
- `public T Current => _current!;`
- `public void Dispose() { }`
- `public bool MoveNext() {`
- `public void Reset() {`

### `src/Avalonia.Base/Utilities/SynchronousCompletionAsyncResult.cs`
- `public record struct SynchronousCompletionAsyncResult<T> : INotifyCompletion`
- `public SynchronousCompletionAsyncResult(T result) {`
- `public bool IsCompleted {`
- `public T GetResult() {`
- `public void OnCompleted(Action continuation) {`
- `public SynchronousCompletionAsyncResult<T> GetAwaiter() => this;`
- `public class SynchronousCompletionAsyncResultSource<T>`
- `public SynchronousCompletionAsyncResult<T> AsyncResult => new SynchronousCompletionAsyncResult<T>(this);`
- `public void SetResult(T result) {`
- `public void TrySetResult(T result) {`

### `src/Avalonia.Base/Utilities/TypeUtilities.cs`
- `public static class TypeUtilities`
- `public static bool AcceptsNull(Type type) {`
- `public static bool AcceptsNull<T>() {`
- `public static bool CanCast<T>(object? value) {`
- `public static bool TryConvert(Type to, object? value, CultureInfo? culture, out object? result) {`
- `public static bool TryConvertImplicit(Type to, object? value, out object? result) {`
- `public static object? ConvertOrDefault(object? value, Type type, CultureInfo culture) {`
- `public static object? ConvertImplicitOrDefault(object? value, Type type) {`
- `public static T ConvertImplicit<T>(object? value) {`
- `public static object? Default(Type type) {`
- `public static bool IsNumeric(Type type) {`

### `src/Avalonia.Base/Utilities/ValueSpan.cs`
- `public readonly record struct ValueSpan<T>`
- `public ValueSpan(int start, int length, T value) {`
- `public int Start { get; }`
- `public int Length { get; }`
- `public T Value { get; }`

### `src/Avalonia.Base/Utilities/WeakEvent.cs`
- Namespace: `Avalonia.Utilities`
- `public sealed class WeakEvent<TSender, TEventArgs> : WeakEvent where TSender : class`
- `public void Subscribe(TSender target, IWeakEventSubscriber<TEventArgs> subscriber) {`
- `public void Unsubscribe(TSender target, IWeakEventSubscriber<TEventArgs> subscriber) {`
- `public class WeakEvent`
- `public static WeakEvent<TSender, TEventArgs> Register<TSender, TEventArgs>( Action<TSender, EventHandler<TEventArgs>> subscribe, Action<TSender, EventHandler<TEventArgs>> unsubscribe) where TSender : class {`
- `public static WeakEvent<TSender, TEventArgs> Register<TSender, TEventArgs>( Func<TSender, EventHandler<TEventArgs>, Action> subscribe) where TSender : class where TEventArgs : EventArgs {`
- `public static WeakEvent<TSender, EventArgs> Register<TSender>( Action<TSender, EventHandler> subscribe, Action<TSender, EventHandler> unsubscribe) where TSender : class {`

### `src/Avalonia.Base/Utilities/WeakEventHandlerManager.cs`
- `public static class WeakEventHandlerManager`
- `public static void Subscribe<[DynamicallyAccessedMembers(DynamicallyAccessedMemberTypes.PublicEvents | DynamicallyAccessedMemberTypes.NonPublicEvents)] TTarget, TEventArgs, TSubscriber>( TTarget target, string eventName, EventHandler<TEventArgs> subscriber) where TEventArgs : EventArgs where TSubscriber : class {`
- `public static void Unsubscribe<TEventArgs, TSubscriber>(object target, string eventName, EventHandler<TEventArgs> subscriber) where TEventArgs : EventArgs where TSubscriber : class {`

### `src/Avalonia.Base/Utilities/WeakEvents.cs`
- Namespace: `Avalonia.Utilities`
- `public class WeakEvents`
- `public static readonly WeakEvent<INotifyCollectionChanged, NotifyCollectionChangedEventArgs> CollectionChanged = WeakEvent.Register<INotifyCollectionChanged, NotifyCollectionChangedEventArgs>( (c, s) =>`
- `public static readonly WeakEvent<INotifyPropertyChanged, PropertyChangedEventArgs> ThreadSafePropertyChanged = WeakEvent.Register<INotifyPropertyChanged, PropertyChangedEventArgs>( (s, h) =>`
- `public static readonly WeakEvent<AvaloniaObject, AvaloniaPropertyChangedEventArgs> AvaloniaPropertyChanged = WeakEvent.Register<AvaloniaObject, AvaloniaPropertyChangedEventArgs>( (s, h) =>`
- `public static readonly WeakEvent<ICommand, EventArgs> CommandCanExecuteChanged = WeakEvent.Register<ICommand>((s, h) => s.CanExecuteChanged += h,`

### `src/Avalonia.Base/Vector3D.cs`
- Namespace: `Avalonia`
- `public readonly record struct Vector3D(double X, double Y, double Z)`
- `public static Vector3D Parse(string s) {`
- `public static implicit operator Vector3D(Vector3 vector) => new(vector);`
- `public static double Dot(Vector3D vector1, Vector3D vector2) =>`
- `public static Vector3D Add(Vector3D left, Vector3D right) =>`
- `public static Vector3D operator +(Vector3D left, Vector3D right) => Add(left, right);`
- `public static Vector3D Substract(Vector3D left, Vector3D right) =>`
- `public static Vector3D operator -(Vector3D left, Vector3D right) => Substract(left, right);`
- `public static Vector3D operator -(Vector3D v) => new(-v.X, -v.Y, -v.Z);`
- `public static Vector3D Multiply(Vector3D left, Vector3D right) =>`
- `public static Vector3D Multiply(Vector3D left, double right) =>`
- `public static Vector3D operator *(Vector3D left, double right) => Multiply(left, right);`
- `public static Vector3D Divide(Vector3D left, Vector3D right) =>`
- `public static Vector3D Divide(Vector3D left, double right) =>`
- `public Vector3D Abs() => new(Math.Abs(X), Math.Abs(Y), Math.Abs(Z));`
- `public static Vector3D Clamp(Vector3D value, Vector3D min, Vector3D max) =>`
- `public static Vector3D Max(Vector3D left, Vector3D right) =>`
- `public static Vector3D Min(Vector3D left, Vector3D right) =>`
- `public double Length => Math.Sqrt(Dot(this, this));`
- `public static Vector3D Normalize(Vector3D value) => Divide(value, value.Length);`
- `public static double DistanceSquared(Vector3D value1, Vector3D value2) {`
- `public static double Distance(Vector3D value1, Vector3D value2) => Math.Sqrt(DistanceSquared(value1, value2));`

### `src/Avalonia.Base/Visual.Composition.cs`
- Namespace: `Avalonia`
- `public partial class Visual`

### `src/Avalonia.Base/Visual.cs`
- `public partial class Visual : StyledElement, IAvaloniaListItemValidator<Visual>`
- `public static readonly DirectProperty<Visual, Rect> BoundsProperty = AvaloniaProperty.RegisterDirect<Visual, Rect>(nameof(Bounds), o => o.Bounds);`
- `public static readonly StyledProperty<bool> ClipToBoundsProperty = AvaloniaProperty.Register<Visual, bool>(nameof(ClipToBounds));`
- `public static readonly StyledProperty<Geometry?> ClipProperty = AvaloniaProperty.Register<Visual, Geometry?>(nameof(Clip));`
- `public static readonly StyledProperty<bool> IsVisibleProperty = AvaloniaProperty.Register<Visual, bool>(nameof(IsVisible), true);`
- `public static readonly StyledProperty<double> OpacityProperty = AvaloniaProperty.Register<Visual, double>(nameof(Opacity), 1);`
- `public static readonly StyledProperty<IBrush?> OpacityMaskProperty = AvaloniaProperty.Register<Visual, IBrush?>(nameof(OpacityMask));`
- `public static readonly StyledProperty<IEffect?> EffectProperty = AvaloniaProperty.Register<Visual, IEffect?>(nameof(Effect));`
- `public static readonly DirectProperty<Visual, bool> HasMirrorTransformProperty = AvaloniaProperty.RegisterDirect<Visual, bool>(nameof(HasMirrorTransform), o => o.HasMirrorTransform);`
- `public static readonly StyledProperty<ITransform?> RenderTransformProperty = AvaloniaProperty.Register<Visual, ITransform?>(nameof(RenderTransform));`
- `public static readonly StyledProperty<RelativePoint> RenderTransformOriginProperty = AvaloniaProperty.Register<Visual, RelativePoint>(nameof(RenderTransformOrigin), defaultValue: RelativePoint.Center);`
- `public static readonly AttachedProperty<FlowDirection> FlowDirectionProperty = AvaloniaProperty.RegisterAttached<Visual, Visual, FlowDirection>( nameof(FlowDirection), inherits: true);`
- `public static readonly DirectProperty<Visual, Visual?> VisualParentProperty = AvaloniaProperty.RegisterDirect<Visual, Visual?>(nameof(VisualParent), o => o._visualParent);`
- `public static readonly StyledProperty<int> ZIndexProperty = AvaloniaProperty.Register<Visual, int>(nameof(ZIndex));`
- `public Visual() {`
- `public event EventHandler<VisualTreeAttachmentEventArgs>? AttachedToVisualTree;`
- `public event EventHandler<VisualTreeAttachmentEventArgs>? DetachedFromVisualTree;`
- `public Rect Bounds {`
- `public bool ClipToBounds {`
- `public Geometry? Clip {`
- `public bool IsEffectivelyVisible { get; private set; } = true;`
- `public bool IsVisible {`
- `public double Opacity {`
- `public IBrush? OpacityMask {`
- `public IEffect? Effect {`
- `public bool HasMirrorTransform {`
- `public ITransform? RenderTransform {`
- `public RelativePoint RenderTransformOrigin {`
- `public FlowDirection FlowDirection {`
- `public int ZIndex {`
- `public static FlowDirection GetFlowDirection(Visual visual) {`
- `public static void SetFlowDirection(Visual visual, FlowDirection value) {`
- `public void InvalidateVisual() {`
- `public virtual void Render(DrawingContext context) {`

### `src/Avalonia.Base/VisualExtensions.cs`
- `public static class VisualExtensions`
- `public static Point PointToClient(this Visual visual, PixelPoint point) {`
- `public static PixelPoint PointToScreen(this Visual visual, Point point) {`
- `public static Matrix? TransformToVisual(this Visual from, Visual to) {`
- `public static Point? TranslatePoint(this Visual visual, Point point, Visual relativeTo) {`

### `src/Avalonia.Base/VisualTree/IHostedVisualTreeRoot.cs`
- `public interface IHostedVisualTreeRoot`

### `src/Avalonia.Base/VisualTree/TransformedBounds.cs`
- `public readonly struct TransformedBounds : IEquatable<TransformedBounds>`
- `public TransformedBounds(Rect bounds, Rect clip, Matrix transform) {`
- `public Rect Bounds { get; }`
- `public Rect Clip { get; }`
- `public Matrix Transform { get; }`
- `public bool Contains(Point point) {`
- `public bool Equals(TransformedBounds other) {`
- `public override bool Equals(object? obj) => obj is TransformedBounds other && Equals(other);`
- `public override int GetHashCode() {`
- `public static bool operator ==(TransformedBounds left, TransformedBounds right) {`
- `public static bool operator !=(TransformedBounds left, TransformedBounds right) {`
- `public override string ToString() => FormattableString.Invariant($"Bounds: {Bounds} Clip: {Clip} Transform {Transform}");`

### `src/Avalonia.Base/VisualTree/VisualExtensions.cs`
- `public static class VisualExtensions`
- `public static int CalculateDistanceFromAncestor(this Visual visual, Visual? ancestor) {`
- `public static int CalculateDistanceFromRoot(Visual visual) {`
- `public static Visual? FindCommonVisualAncestor(this Visual? visual, Visual? target) {`
- `public static IEnumerable<Visual> GetVisualAncestors(this Visual visual) {`
- `public static T? FindAncestorOfType<T>(this Visual? visual, bool includeSelf = false) where T : class {`
- `public static T? FindAncestorOfType<T>(this Visual? visual, bool includeSelf, Predicate<T>? predicate) where T : class {`
- `public static T? FindDescendantOfType<T>(this Visual? visual, bool includeSelf = false) where T : class {`
- `public static T? FindDescendantOfType<T>(this Visual? visual, bool includeSelf, Predicate<T>? predicate) where T : class {`
- `public static IEnumerable<Visual> GetSelfAndVisualAncestors(this Visual visual) {`
- `public static TransformedBounds? GetTransformedBounds(this Visual visual) {`
- `public static Visual? GetVisualAt(this Visual visual, Point p) {`
- `public static Visual? GetVisualAt(this Visual visual, Point p, Func<Visual, bool> filter) {`
- `public static IEnumerable<Visual> GetVisualsAt( this Visual visual, Point p) {`
- `public static IEnumerable<Visual> GetVisualsAt( this Visual visual, Point p, Func<Visual, bool> filter) {`
- `public static IEnumerable<Visual> GetVisualChildren(this Visual visual) {`
- `public static IEnumerable<Visual> GetVisualDescendants(this Visual visual) {`
- `public static IEnumerable<Visual> GetSelfAndVisualDescendants(this Visual visual) {`
- `public static Visual? GetVisualParent(this Visual visual) {`
- `public static T? GetVisualParent<T>(this Visual visual) where T : class {`
- `public static IRenderRoot? GetVisualRoot(this Visual visual) {`
- `public static bool IsAttachedToVisualTree(this Visual visual) => visual.IsAttachedToVisualTree;`
- `public static bool IsVisualAncestorOf(this Visual? visual, Visual? target) {`
- `public static IEnumerable<Visual> SortByZIndex(this IEnumerable<Visual> elements) {`

### `src/Avalonia.Base/VisualTree/VisualLocator.cs`
- `public class VisualLocator`
- `public static IObservable<Visual?> Track(Visual relativeTo, int ancestorLevel, Type? ancestorType = null) {`

### `src/Avalonia.Base/VisualTreeAttachmentEventArgs.cs`
- `public class VisualTreeAttachmentEventArgs : EventArgs`
- `public VisualTreeAttachmentEventArgs(Visual parent, IRenderRoot root) {`
- `public Visual Parent { get; }`
- `public IRenderRoot Root { get; }`

## Rendering and Text

### `src/Avalonia.Fonts.Inter/AppBuilderExtension.cs`
- `public static class AppBuilderExtension`
- `public static AppBuilder WithInterFont(this AppBuilder appBuilder) {`

### `src/Avalonia.Fonts.Inter/InterFontCollection.cs`
- `public sealed class InterFontCollection : EmbeddedFontCollection`
- `public InterFontCollection() : base( new Uri("fonts:Inter", UriKind.Absolute), new Uri("avares: {`

### `src/Skia/Avalonia.Skia/Gpu/ISkiaGpu.cs`
- `public interface ISkiaGpu : IPlatformGraphicsContext`
- `public interface ISkiaGpuWithPlatformGraphicsContext : ISkiaGpu`
- `public interface ISkiaSurface : IDisposable`

### `src/Skia/Avalonia.Skia/Gpu/ISkiaGpuRenderSession.cs`
- `public interface ISkiaGpuRenderSession : IDisposable`

### `src/Skia/Avalonia.Skia/Gpu/ISkiaGpuRenderTarget.cs`
- `public interface ISkiaGpuRenderTarget : IDisposable`
- `public interface ISkiaGpuRenderTarget2 : ISkiaGpuRenderTarget`

### `src/Skia/Avalonia.Skia/Gpu/OpenGl/IGlSkiaSpecificOptionsFeature.cs`
- Namespace: `Avalonia.Skia`
- `public interface IGlSkiaSpecificOptionsFeature`
- `public bool UseNativeSkiaGrGlInterface { get; }`

### `src/Skia/Avalonia.Skia/Helpers/DrawingContextHelper.cs`
- `public static class DrawingContextHelper`
- `public static Task RenderAsync(SKCanvas canvas, Visual visual) {`
- `public static Task RenderAsync(SKCanvas canvas, Visual visual, Rect clipRect, Vector dpi) {`
- `public static IDrawingContextImpl WrapSkiaCanvas(SKCanvas canvas, Vector dpi) {`
- `public static bool TryCreateDashEffect(IPen? pen, [NotNullWhen(true)] out SKPathEffect? effect) {`

### `src/Skia/Avalonia.Skia/Helpers/ImageSavingHelper.cs`
- `public static class ImageSavingHelper`
- `public static void SaveImage(SKImage image, string fileName, int? quality = null) {`
- `public static void SaveImage(SKImage image, Stream stream, int? quality = null) {`

### `src/Skia/Avalonia.Skia/Helpers/PixelFormatHelper.cs`
- `public static class PixelFormatHelper`
- `public static SKColorType ResolveColorType(PixelFormat? format) {`

### `src/Skia/Avalonia.Skia/ISkiaSharpApiLeaseFeature.cs`
- Namespace: `Avalonia.Skia`
- `public interface ISkiaSharpApiLeaseFeature`
- `public ISkiaSharpApiLease Lease();`
- `public interface ISkiaSharpApiLease : IDisposable`
- `public interface ISkiaSharpPlatformGraphicsApiLease : IDisposable`

### `src/Skia/Avalonia.Skia/SkiaApplicationExtensions.cs`
- `public static class SkiaApplicationExtensions`
- `public static AppBuilder UseSkia(this AppBuilder builder) {`

### `src/Skia/Avalonia.Skia/SkiaOptions.cs`
- `public class SkiaOptions`
- `public long? MaxGpuResourceSizeBytes { get; set; } = 1024 * 600 * 4 * 12;`
- `public bool UseOpacitySaveLayer { get; set; } = false;`

### `src/Skia/Avalonia.Skia/SkiaPlatform.cs`
- `public static class SkiaPlatform`
- `public static void Initialize() {`
- `public static void Initialize(SkiaOptions options) {`
- `public static Vector DefaultDpi => new Vector(96.0f, 96.0f);`

### `src/Skia/Avalonia.Skia/SkiaSharpExtensions.cs`
- `public static class SkiaSharpExtensions`
- `public static SKFilterQuality ToSKFilterQuality(this BitmapInterpolationMode interpolationMode) {`
- `public static SKBlendMode ToSKBlendMode(this BitmapBlendingMode blendingMode) {`
- `public static SKPoint ToSKPoint(this Point p) {`
- `public static SKPoint ToSKPoint(this Vector p) {`
- `public static SKRect ToSKRect(this Rect r) {`
- `public static SKRectI ToSKRectI(this PixelRect r) {`
- `public static SKRoundRect ToSKRoundRect(this RoundedRect r) {`
- `public static Rect ToAvaloniaRect(this SKRect r) {`
- `public static PixelRect ToAvaloniaPixelRect(this SKRectI r) {`
- `public static SKMatrix ToSKMatrix(this Matrix m) {`
- `public static SKColor ToSKColor(this Color c) {`
- `public static SKColorType ToSkColorType(this PixelFormat fmt) {`
- `public static PixelFormat? ToAvalonia(this SKColorType colorType) {`
- `public static PixelFormat ToPixelFormat(this SKColorType fmt) {`
- `public static SKAlphaType ToSkAlphaType(this AlphaFormat fmt) {`
- `public static AlphaFormat ToAlphaFormat(this SKAlphaType fmt) {`
- `public static SKShaderTileMode ToSKShaderTileMode(this GradientSpreadMethod m) {`
- `public static SKTextAlign ToSKTextAlign(this TextAlignment a) {`
- `public static SKStrokeCap ToSKStrokeCap(this PenLineCap cap) {`
- `public static SKStrokeJoin ToSKStrokeJoin(this PenLineJoin join) {`
- `public static TextAlignment ToAvalonia(this SKTextAlign a) {`
- `public static FontStyle ToAvalonia(this SKFontStyleSlant slant) {`
- `public static SKFontStyleSlant ToSkia(this FontStyle style) {`
- `public static SKPath? Clone(this SKPath? src) {`

## Source Generator Integration

### `src/tools/Avalonia.Generators/NameGenerator/AvaloniaNameSourceGenerator.cs`
- Namespace: `Avalonia.Generators.NameGenerator`
- `public class AvaloniaNameSourceGenerator : ISourceGenerator`
- `public void Initialize(GeneratorInitializationContext context) { }`
- `public void Execute(GeneratorExecutionContext context) {`

## Windows Platform

### `src/Windows/Avalonia.Direct2D1/Direct2D1Platform.cs`
- `public static class Direct2DApplicationExtensions`
- `public static AppBuilder UseDirect2D1(this AppBuilder builder) {`

### `src/Windows/Avalonia.Direct2D1/IExternalDirect2DRenderTargetSurface.cs`
- `public interface IExternalDirect2DRenderTargetSurface`

### `src/Windows/Avalonia.Win32.Interoperability/WinForms/WinFormsAvaloniaControlHost.cs`
- Namespace: `Avalonia.Win32.Interoperability`
- `public class WinFormsAvaloniaControlHost : WinFormsControl, IMessageFilter`
- `public WinFormsAvaloniaControlHost() {`
- `public AvControl? Content {`
- `public bool PreFilterMessage(ref Message m) {`

### `src/Windows/Avalonia.Win32/AngleOptions.cs`
- `public class AngleOptions`
- `public enum PlatformApi`
- `public IList<GlVersion> GlProfiles { get; set; } = new List<GlVersion>`
- `public IList<PlatformApi>? AllowedPlatformApis { get; set; } = null;`

### `src/Windows/Avalonia.Win32/DirectX/IDirect3D11TexturePlatformSurface.cs`
- Namespace: `Avalonia.Win32.DirectX`
- `public interface IDirect3D11TexturePlatformSurface`
- `public IDirect3D11TextureRenderTarget CreateRenderTarget(IPlatformGraphicsContext graphicsContext, IntPtr d3dDevice);`
- `public interface IDirect3D11TextureRenderTarget : IDisposable`
- `public interface IDirect3D11TextureRenderTargetRenderSession : IDisposable`
- `public IntPtr D3D11Texture2D { get; }`
- `public PixelSize Size { get; }`
- `public PixelPoint Offset { get; }`
- `public double Scaling { get; }`

### `src/Windows/Avalonia.Win32/Input/KeyInterop.cs`
- `public static class KeyInterop`
- `public static Key KeyFromVirtualKey(int virtualKey, int keyData) {`
- `public static int VirtualKeyFromKey(Key key) {`
- `public static PhysicalKey PhysicalKeyFromVirtualKey(int virtualKey, int keyData) {`
- `public static unsafe string? GetKeySymbol(int virtualKey, int keyData) {`

### `src/Windows/Avalonia.Win32/Win32Platform.cs`
- `public static class Win32ApplicationExtensions`
- `public static AppBuilder UseWin32(this AppBuilder builder) {`

### `src/Windows/Avalonia.Win32/Win32PlatformOptions.cs`
- Namespace: `Avalonia`
- `public enum Win32RenderingMode`
- `public enum Win32DpiAwareness`
- `public enum Win32CompositionMode`
- `public class Win32PlatformOptions`
- `public bool OverlayPopups { get; set; }`
- `public IReadOnlyList<Win32RenderingMode> RenderingMode { get; set; } = new[]`
- `public IReadOnlyList<Win32CompositionMode> CompositionMode { get; set; } = new[]`
- `public float? WinUICompositionBackdropCornerRadius { get; set; }`
- `public bool ShouldRenderOnUIThread { get; set; }`
- `public IList<GlVersion> WglProfiles { get; set; } = new List<GlVersion>`
- `public IPlatformGraphics? CustomPlatformGraphics { get; set; }`
- `public Win32DpiAwareness DpiAwareness { get; set; } = Win32DpiAwareness.PerMonitorDpiAware;`
- `public Func<IReadOnlyList<PlatformGraphicsDeviceAdapterDescription>, int>? GraphicsAdapterSelectionCallback { get; set; }`

## XAML and Markup

### `src/Markup/Avalonia.Markup.Xaml.Loader/AvaloniaRuntimeXamlLoader.cs`
- `public static class AvaloniaRuntimeXamlLoader`
- `public static object Load([StringSyntax(StringSyntaxAttribute.Xml)] string xaml, Assembly? localAssembly = null, object? rootInstance = null, Uri? uri = null, bool designMode = false) {`
- `public static object Load(Stream stream, Assembly? localAssembly = null, object? rootInstance = null, Uri? uri = null, bool designMode = false) => AvaloniaXamlIlRuntimeCompiler.Load(new RuntimeXamlLoaderDocument(uri, rootInstance, stream),`
- `public static object Load(RuntimeXamlLoaderDocument document, RuntimeXamlLoaderConfiguration? configuration = null) => AvaloniaXamlIlRuntimeCompiler.Load(document, configuration ?? new RuntimeXamlLoaderConfiguration());`
- `public static IReadOnlyList<object?> LoadGroup(IReadOnlyCollection<RuntimeXamlLoaderDocument> documents, RuntimeXamlLoaderConfiguration? configuration = null) => AvaloniaXamlIlRuntimeCompiler.LoadGroup(documents, configuration ?? new RuntimeXamlLoaderConfiguration());`
- `public static object Parse([StringSyntax(StringSyntaxAttribute.Xml)] string xaml, Assembly? localAssembly = null) => Load(xaml, localAssembly);`
- `public static T Parse<[DynamicallyAccessedMembers(DynamicallyAccessedMemberTypes.All)] T>([StringSyntax(StringSyntaxAttribute.Xml)] string xaml, Assembly? localAssembly = null) => (T)Parse(xaml, localAssembly);`

### `src/Markup/Avalonia.Markup.Xaml.Loader/CompilerExtensions/Transformers/AvaloniaXamlIlControlTemplateTargetTypeMetadataTransformer.cs`
- `public enum ScopeTypes`

### `src/Markup/Avalonia.Markup.Xaml.Loader/CompilerExtensions/Transformers/AvaloniaXamlIlQueryTransformer.cs`
- `public enum QueryType`
- `public enum CombinatorQueryType`

### `src/Markup/Avalonia.Markup.Xaml.Loader/CompilerExtensions/Transformers/AvaloniaXamlIlSelectorTransformer.cs`
- `public enum SelectorType`
- `public enum CombinatorSelectorType`
- `public enum SelectorType`

### `src/Markup/Avalonia.Markup.Xaml/AvaloniaXamlLoader.cs`
- `public static class AvaloniaXamlLoader`
- `public static void Load(object obj) {`
- `public static void Load(IServiceProvider? sp, object obj) {`
- `public static object Load(Uri uri, Uri? baseUri = null) {`
- `public static object Load(IServiceProvider? sp, Uri uri, Uri? baseUri = null) {`

### `src/Markup/Avalonia.Markup.Xaml/Converters/AvaloniaPropertyTypeConverter.cs`
- `public class AvaloniaPropertyTypeConverter : TypeConverter`
- `public override bool CanConvertFrom(ITypeDescriptorContext? context, Type sourceType) {`
- `public override object ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object value) {`

### `src/Markup/Avalonia.Markup.Xaml/Converters/AvaloniaUriTypeConverter.cs`
- `public class AvaloniaUriTypeConverter : TypeConverter`
- `public override bool CanConvertFrom(ITypeDescriptorContext? context, Type sourceType) {`
- `public override object? ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object value) {`

### `src/Markup/Avalonia.Markup.Xaml/Converters/BitmapTypeConverter.cs`
- `public class BitmapTypeConverter : TypeConverter`
- `public override bool CanConvertFrom(ITypeDescriptorContext? context, Type sourceType) {`
- `public override object ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object value) {`

### `src/Markup/Avalonia.Markup.Xaml/Converters/ColorToBrushConverter.cs`
- `public class ColorToBrushConverter : IValueConverter`
- `public object? Convert(object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public object? ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture) {`
- `public static object? Convert(object? value, Type? targetType) {`
- `public static object? ConvertBack(object? value, Type? targetType) {`

### `src/Markup/Avalonia.Markup.Xaml/Converters/FontFamilyTypeConverter.cs`
- `public class FontFamilyTypeConverter : TypeConverter`
- `public override bool CanConvertFrom(ITypeDescriptorContext? context, Type sourceType) {`
- `public override object ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object value) {`

### `src/Markup/Avalonia.Markup.Xaml/Converters/IconTypeConverter.cs`
- `public class IconTypeConverter : TypeConverter`
- `public override bool CanConvertFrom(ITypeDescriptorContext? context, Type sourceType) {`
- `public override object ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object value) {`

### `src/Markup/Avalonia.Markup.Xaml/Converters/PointsListTypeConverter.cs`
- `public class PointsListTypeConverter : TypeConverter`
- `public override bool CanConvertFrom(ITypeDescriptorContext? context, Type sourceType) {`
- `public override object ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object value) {`

### `src/Markup/Avalonia.Markup.Xaml/Converters/TimeSpanTypeConverter.cs`
- `public class TimeSpanTypeConverter : TimeSpanConverter`
- `public override object? ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object value) {`

### `src/Markup/Avalonia.Markup.Xaml/Diagnostics/XamlSourceInfo.cs`
- `public record XamlSourceInfo`
- `public Uri? SourceUri { get; }`
- `public int LineNumber { get; }`
- `public int LinePosition { get; }`
- `public XamlSourceInfo(int line, int column, string? filePath) {`
- `public static void SetXamlSourceInfo(object obj, XamlSourceInfo? info) {`
- `public static void SetXamlSourceInfo(IResourceDictionary dictionary, object key, XamlSourceInfo? info) {`
- `public static XamlSourceInfo? GetXamlSourceInfo(object obj) {`
- `public static XamlSourceInfo? GetXamlSourceInfo(IResourceDictionary dictionary, object key) {`
- `public override string ToString() {`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtension.cs`
- `public abstract class MarkupExtension`
- `public abstract object ProvideValue(IServiceProvider serviceProvider);`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/CompiledBindingExtension.cs`
- `public class CompiledBindingExtension : BindingBase`
- `public CompiledBindingExtension() {`
- `public CompiledBindingExtension(CompiledBindingPath path) {`
- `public CompiledBindingExtension ProvideValue(IServiceProvider provider) {`
- `public CompiledBindingPath Path { get; set; }`
- `public object? Source { get; set; } = AvaloniaProperty.UnsetValue;`
- `public Type? DataType { get; set; }`
- `public override InstancedBinding? Initiate( AvaloniaObject target, AvaloniaProperty? targetProperty, object? anchor = null, bool enableDataValidation = false) {`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/CompiledBindings/CompiledBindingPath.cs`
- `public class CompiledBindingPath`
- `public CompiledBindingPath() => _elements = Array.Empty<ICompiledBindingPathElement>();`
- `public override string ToString() => string.Concat((IEnumerable<ICompiledBindingPathElement>) _elements);`
- `public class CompiledBindingPathBuilder`
- `public CompiledBindingPathBuilder() {`
- `public CompiledBindingPathBuilder(int apiVersion) => _apiVersion = apiVersion;`
- `public CompiledBindingPathBuilder Not() {`
- `public CompiledBindingPathBuilder Property(IPropertyInfo info, Func<WeakReference<object?>, IPropertyInfo, IPropertyAccessor> accessorFactory) {`
- `public CompiledBindingPathBuilder Property( IPropertyInfo info, Func<WeakReference<object?>, IPropertyInfo, IPropertyAccessor> accessorFactory, bool acceptsNull) {`
- `public CompiledBindingPathBuilder Method(RuntimeMethodHandle handle, RuntimeTypeHandle delegateType) {`
- `public CompiledBindingPathBuilder Method( RuntimeMethodHandle handle, RuntimeTypeHandle delegateType, bool acceptsNull) {`
- `public CompiledBindingPathBuilder Command(string methodName, Action<object, object?> executeHelper, Func<object, object?, bool>? canExecuteHelper, string[]? dependsOnProperties) {`
- `public CompiledBindingPathBuilder StreamTask<T>() {`
- `public CompiledBindingPathBuilder StreamObservable<T>() {`
- `public CompiledBindingPathBuilder Self() {`
- `public CompiledBindingPathBuilder Ancestor(Type ancestorType, int level) {`
- `public CompiledBindingPathBuilder VisualAncestor(Type ancestorType, int level) {`
- `public CompiledBindingPathBuilder ElementName(INameScope nameScope, string name) {`
- `public CompiledBindingPathBuilder ArrayElement(int[] indices, Type elementType) {`
- `public CompiledBindingPathBuilder TypeCast<T>() {`
- `public CompiledBindingPathBuilder TemplatedParent() {`
- `public CompiledBindingPathBuilder SetRawSource(object? rawSource) {`
- `public CompiledBindingPath Build() => new CompiledBindingPath(_elements.ToArray());`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/CompiledBindings/PropertyInfoAccessorFactory.cs`
- `public static class PropertyInfoAccessorFactory`
- `public static IPropertyAccessor CreateInpcPropertyAccessor(WeakReference<object?> target, IPropertyInfo property) => new InpcPropertyAccessor(target, property);`
- `public static IPropertyAccessor CreateAvaloniaPropertyAccessor(WeakReference<object?> target, IPropertyInfo property) => new AvaloniaPropertyAccessor(new WeakReference<AvaloniaObject?>((AvaloniaObject?)(target.TryGetTarget(out var o) ? o : null)), (AvaloniaProperty)property);`
- `public static IPropertyAccessor CreateIndexerPropertyAccessor(WeakReference<object?> target, IPropertyInfo property, int argument) => new IndexerAccessor(target, property, argument);`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/DynamicResourceExtension.cs`
- `public class DynamicResourceExtension : IBinding2`
- `public DynamicResourceExtension() {`
- `public DynamicResourceExtension(object resourceKey) {`
- `public object? ResourceKey { get; set; }`
- `public IBinding ProvideValue(IServiceProvider serviceProvider) {`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/On.cs`
- Namespace: `Avalonia.Markup.Xaml.MarkupExtensions`
- `public class On<TReturn>`
- `public IReadOnlyList<string> Options { get; } = new List<string>();`
- `public TReturn? Content { get; set; }`
- `public class On : On<object> {}`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/OnFormFactorExtension.cs`
- Namespace: `Avalonia.Markup.Xaml.MarkupExtensions`
- `public sealed class OnFormFactorExtension : OnFormFactorExtensionBase<object, On>`
- `public OnFormFactorExtension() {`
- `public OnFormFactorExtension(object defaultValue) {`
- `public static bool ShouldProvideOption(IServiceProvider serviceProvider, FormFactorType option) {`
- `public sealed class OnFormFactorExtension<TReturn> : OnFormFactorExtensionBase<TReturn, On<TReturn>>`
- `public OnFormFactorExtension() {`
- `public OnFormFactorExtension(TReturn defaultValue) {`
- `public static bool ShouldProvideOption(IServiceProvider serviceProvider, FormFactorType option) {`
- `public abstract class OnFormFactorExtensionBase<TReturn, TOn> : IAddChild<TOn>`
- `public TReturn? Default { get; set; }`
- `public TReturn? Desktop { get; set; }`
- `public TReturn? Mobile { get; set; }`
- `public TReturn? TV { get; set; }`
- `public object ProvideValue() { return this; }`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/OnPlatformExtension.cs`
- Namespace: `Avalonia.Markup.Xaml.MarkupExtensions`
- `public sealed class OnPlatformExtension : OnPlatformExtensionBase<object, On>`
- `public OnPlatformExtension() {`
- `public OnPlatformExtension(object defaultValue) {`
- `public static bool ShouldProvideOption(string option) {`
- `public sealed class OnPlatformExtension<TReturn> : OnPlatformExtensionBase<TReturn, On<TReturn>>`
- `public OnPlatformExtension() {`
- `public OnPlatformExtension(TReturn defaultValue) {`
- `public static bool ShouldProvideOption(string option) {`
- `public abstract class OnPlatformExtensionBase<TReturn, TOn> : IAddChild<TOn>`
- `public TReturn? Default { get; set; }`
- `public TReturn? Windows { get; set; }`
- `public TReturn? macOS { get; set; }`
- `public TReturn? Linux { get; set; }`
- `public TReturn? Android { get; set; }`
- `public TReturn? iOS { get; set; }`
- `public TReturn? Browser { get; set; }`
- `public object ProvideValue() { return this; }`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/ReflectionBindingExtension.cs`
- `public class ReflectionBindingExtension`
- `public ReflectionBindingExtension() {`
- `public ReflectionBindingExtension(string path) {`
- `public Binding ProvideValue(IServiceProvider serviceProvider) {`
- `public int Delay { get; set; }`
- `public IValueConverter? Converter { get; set; }`
- `public CultureInfo? ConverterCulture { get; set; }`
- `public object? ConverterParameter { get; set; }`
- `public string? ElementName { get; set; }`
- `public object? FallbackValue { get; set; } = AvaloniaProperty.UnsetValue;`
- `public BindingMode Mode { get; set; }`
- `public string Path { get; set; } = "";`
- `public BindingPriority Priority { get; set; } = BindingPriority.LocalValue;`
- `public object? Source { get; set; } = AvaloniaProperty.UnsetValue;`
- `public string? StringFormat { get; set; }`
- `public RelativeSource? RelativeSource { get; set; }`
- `public object? TargetNullValue { get; set; } = AvaloniaProperty.UnsetValue;`
- `public UpdateSourceTrigger UpdateSourceTrigger { get; set; }`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/RelativeSourceExtension.cs`
- `public class RelativeSourceExtension`
- `public RelativeSourceExtension() {`
- `public RelativeSourceExtension(RelativeSourceMode mode) {`
- `public RelativeSource ProvideValue(IServiceProvider serviceProvider) {`
- `public RelativeSourceMode Mode { get; set; } = RelativeSourceMode.FindAncestor;`
- `public Type? AncestorType { get; set; }`
- `public TreeType Tree { get; set; }`
- `public int AncestorLevel { get; set; } = 1;`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/ResolveByNameExtension.cs`
- `public class ResolveByNameExtension`
- `public ResolveByNameExtension(string name) {`
- `public string Name { get; }`
- `public object? ProvideValue(IServiceProvider serviceProvider) => ProvideValue(serviceProvider, Name);`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/StaticResourceExtension.cs`
- `public class StaticResourceExtension`
- `public StaticResourceExtension() {`
- `public StaticResourceExtension(object resourceKey) {`
- `public object? ResourceKey { get; set; }`
- `public object? ProvideValue(IServiceProvider serviceProvider) => ProvideValue(serviceProvider, ResourceKey);`

### `src/Markup/Avalonia.Markup.Xaml/RuntimeXamlLoaderConfiguration.cs`
- Namespace: `Avalonia.Markup.Xaml`
- `public class RuntimeXamlLoaderConfiguration`
- `public Assembly? LocalAssembly { get; set; }`
- `public bool UseCompiledBindingsByDefault { get; set; } = false;`
- `public bool DesignMode { get; set; } = false;`
- `public bool CreateSourceInfo { get; set; } = false;`
- `public XamlDiagnosticFunc? DiagnosticHandler { get; set; }`
- `public delegate RuntimeXamlDiagnosticSeverity XamlDiagnosticFunc(RuntimeXamlDiagnostic diagnostic);`
- `public enum RuntimeXamlDiagnosticSeverity`
- `public record RuntimeXamlDiagnostic(`
- `public string? Document { get; set; }`

### `src/Markup/Avalonia.Markup.Xaml/RuntimeXamlLoaderDocument.cs`
- Namespace: `Avalonia.Markup.Xaml`
- `public class RuntimeXamlLoaderDocument`
- `public RuntimeXamlLoaderDocument([StringSyntax(StringSyntaxAttribute.Xml)] string xaml) {`
- `public RuntimeXamlLoaderDocument(Uri? baseUri, [StringSyntax(StringSyntaxAttribute.Xml)] string xaml) : this(xaml) {`
- `public RuntimeXamlLoaderDocument(object? rootInstance, [StringSyntax(StringSyntaxAttribute.Xml)] string xaml) : this(xaml) {`
- `public RuntimeXamlLoaderDocument(Uri? baseUri, object? rootInstance, [StringSyntax(StringSyntaxAttribute.Xml)] string xaml) : this(baseUri, xaml) {`
- `public RuntimeXamlLoaderDocument(Stream stream) {`
- `public RuntimeXamlLoaderDocument(Uri? baseUri, Stream stream) : this(stream) {`
- `public RuntimeXamlLoaderDocument(object? rootInstance, Stream stream) : this(stream) {`
- `public RuntimeXamlLoaderDocument(Uri? baseUri, object? rootInstance, Stream stream) : this(baseUri, stream) {`
- `public Uri? BaseUri { get; set; }`
- `public string? Document { get; set; }`
- `public object? RootInstance { get; set; }`
- `public Stream XamlStream { get; }`
- `public IServiceProvider? ServiceProvider { get; set; }`

### `src/Markup/Avalonia.Markup.Xaml/Styling/MergeResourceInclude.cs`
- Namespace: `Avalonia.Markup.Xaml.Styling`
- `public class MergeResourceInclude : ResourceInclude`
- `public MergeResourceInclude(Uri? baseUri) : base(baseUri) {`
- `public MergeResourceInclude(IServiceProvider serviceProvider) : base(serviceProvider) {`

### `src/Markup/Avalonia.Markup.Xaml/Styling/ResourceInclude.cs`
- `public class ResourceInclude : IResourceProvider, IThemeVariantProvider`
- `public ResourceInclude(Uri? baseUri) {`
- `public ResourceInclude(IServiceProvider serviceProvider) {`
- `public IResourceDictionary Loaded {`
- `public IResourceHost? Owner => Loaded.Owner;`
- `public Uri? Source { get; set; }`
- `public event EventHandler? OwnerChanged {`
- `public bool TryGetResource(object key, ThemeVariant? theme, out object? value) {`

### `src/Markup/Avalonia.Markup.Xaml/Styling/StyleInclude.cs`
- `public class StyleInclude : IStyle, IResourceProvider`
- `public StyleInclude(Uri? baseUri) {`
- `public StyleInclude(IServiceProvider serviceProvider) {`
- `public IResourceHost? Owner => (Loaded as IResourceProvider)?.Owner;`
- `public Uri? Source { get; set; }`
- `public IStyle Loaded {`
- `public event EventHandler? OwnerChanged {`
- `public bool TryGetResource(object key, ThemeVariant? theme, out object? value) {`

### `src/Markup/Avalonia.Markup.Xaml/Templates/ControlTemplate.cs`
- `public class ControlTemplate : IControlTemplate`
- `public object? Content { get; set; }`
- `public Type? TargetType { get; set; }`
- `public TemplateResult<Control>? Build(TemplatedControl control) => TemplateContent.Load(Content);`

### `src/Markup/Avalonia.Markup.Xaml/Templates/DataTemplate.cs`
- `public class DataTemplate : IRecyclingDataTemplate, ITypedDataTemplate`
- `public Type? DataType { get; set; }`
- `public object? Content { get; set; }`
- `public bool Match(object? data) {`
- `public Control? Build(object? data) => Build(data, null);`
- `public Control? Build(object? data, Control? existing) {`

### `src/Markup/Avalonia.Markup.Xaml/Templates/FocusAdornerTemplate.cs`
- `public class FocusAdornerTemplate : Template`

### `src/Markup/Avalonia.Markup.Xaml/Templates/ItemsPanelTemplate.cs`
- `public class ItemsPanelTemplate : ITemplate<Panel?>`
- `public object? Content { get; set; }`
- `public Panel? Build() => (Panel?)TemplateContent.Load(Content)?.Result;`

### `src/Markup/Avalonia.Markup.Xaml/Templates/Template.cs`
- `public class Template : ITemplate<Control?>`
- `public object? Content { get; set; }`
- `public Control? Build() => TemplateContent.Load(Content)?.Result;`

### `src/Markup/Avalonia.Markup.Xaml/Templates/TemplateContent.cs`
- `public static class TemplateContent`
- `public static TemplateResult<Control>? Load(object? templateContent) => Load<Control>(templateContent);`
- `public static TemplateResult<T>? Load<T>(object? templateContent) => templateContent switch`

### `src/Markup/Avalonia.Markup.Xaml/Templates/TreeDataTemplate.cs`
- `public class TreeDataTemplate : ITreeDataTemplate, ITypedDataTemplate`
- `public Type? DataType { get; set; }`
- `public object? Content { get; set; }`
- `public BindingBase? ItemsSource { get; set; }`
- `public bool Match(object? data) {`
- `public InstancedBinding? ItemsSelector(object item) {`
- `public Control? Build(object? data) {`

### `src/Markup/Avalonia.Markup.Xaml/XamlIl/Runtime/IAvaloniaXamlIlControlTemplateProvider.cs`
- `public interface IAvaloniaXamlIlControlTemplateProvider`

### `src/Markup/Avalonia.Markup.Xaml/XamlIl/Runtime/IAvaloniaXamlIlParentStackProvider.cs`
- `public interface IAvaloniaXamlIlParentStackProvider`
- `public interface IAvaloniaXamlIlEagerParentStackProvider : IAvaloniaXamlIlParentStackProvider`

### `src/Markup/Avalonia.Markup.Xaml/XamlIl/Runtime/IAvaloniaXamlIlXmlNamespaceInfoProviderV1.cs`
- `public interface IAvaloniaXamlIlXmlNamespaceInfoProvider`
- `public class AvaloniaXamlIlXmlNamespaceInfo`
- `public string ClrNamespace { get; set; } = string.Empty;`
- `public string ClrAssemblyName { get; set; } = string.Empty;`

### `src/Markup/Avalonia.Markup.Xaml/XamlIl/Runtime/XamlIlRuntimeHelpers.cs`
- `public static class XamlIlRuntimeHelpers`
- `public static Func<IServiceProvider, object> DeferredTransformationFactoryV1(Func<IServiceProvider, object> builder, IServiceProvider provider) {`
- `public static Func<IServiceProvider, object> DeferredTransformationFactoryV2<T>(Func<IServiceProvider, object> builder, IServiceProvider provider) {`
- `public static unsafe IDeferredContent DeferredTransformationFactoryV3<T>( IntPtr builder, IServiceProvider provider) {`
- `public static IAvaloniaXamlIlEagerParentStackProvider AsEagerParentStackProvider( this IAvaloniaXamlIlParentStackProvider provider) => provider as IAvaloniaXamlIlEagerParentStackProvider ?? new XamlIlParentStackProviderWrapper(provider);`
- `public static void ApplyNonMatchingMarkupExtensionV1(object target, object property, IServiceProvider prov, object value) {`
- `public static IServiceProvider CreateInnerServiceProviderV1(IServiceProvider compiled) => new InnerServiceProvider(compiled);`

### `src/Markup/Avalonia.Markup.Xaml/XamlLoadException.cs`
- `public class XamlLoadException: Exception`
- `public XamlLoadException() {`
- `public XamlLoadException(string message): base(message) {`
- `public XamlLoadException(string message, Exception innerException): base(message, innerException) {`

### `src/Markup/Avalonia.Markup.Xaml/XamlTypes.cs`
- `public interface IProvideValueTarget`
- `public interface IRootObjectProvider`
- `public interface IUriContext`
- `public interface IXamlTypeResolver`
- `public sealed class ConstructorArgumentAttribute : Attribute`
- `public ConstructorArgumentAttribute(string name) {`

### `src/Markup/Avalonia.Markup/Data/Binding.cs`
- `public class Binding : BindingBase`
- `public Binding() {`
- `public Binding(string path, BindingMode mode = BindingMode.Default) : base(mode) {`
- `public string? ElementName { get; set; }`
- `public RelativeSource? RelativeSource { get; set; }`
- `public object? Source { get; set; } = AvaloniaProperty.UnsetValue;`
- `public string Path { get; set; } = "";`
- `public Func<string?, string, Type>? TypeResolver { get; set; }`
- `public override InstancedBinding? Initiate( AvaloniaObject target, AvaloniaProperty? targetProperty, object? anchor = null, bool enableDataValidation = false) {`

### `src/Markup/Avalonia.Markup/Data/BindingBase.cs`
- `public abstract class BindingBase : IBinding, IBinding2`
- `public BindingBase() {`
- `public BindingBase(BindingMode mode = BindingMode.Default) :this() {`
- `public int Delay { get; set; }`
- `public IValueConverter? Converter { get; set; }`
- `public CultureInfo? ConverterCulture { get; set; }`
- `public object? ConverterParameter { get; set; }`
- `public object? FallbackValue { get; set; }`
- `public object? TargetNullValue { get; set; }`
- `public BindingMode Mode { get; set; }`
- `public BindingPriority Priority { get; set; }`
- `public string? StringFormat { get; set; }`
- `public UpdateSourceTrigger UpdateSourceTrigger { get; set; }`
- `public WeakReference? DefaultAnchor { get; set; }`
- `public WeakReference<INameScope?>? NameScope { get; set; }`
- `public abstract InstancedBinding? Initiate( AvaloniaObject target, AvaloniaProperty? targetProperty, object? anchor = null, bool enableDataValidation = false);`

### `src/Markup/Avalonia.Markup/Data/MultiBinding.cs`
- `public class MultiBinding : IBinding2`
- `public IList<IBinding> Bindings { get; set; } = new List<IBinding>();`
- `public IMultiValueConverter? Converter { get; set; }`
- `public CultureInfo? ConverterCulture { get; set; }`
- `public object? ConverterParameter { get; set; }`
- `public object FallbackValue { get; set; }`
- `public object TargetNullValue { get; set; }`
- `public BindingMode Mode { get; set; } = BindingMode.OneWay;`
- `public BindingPriority Priority { get; set; }`
- `public RelativeSource? RelativeSource { get; set; }`
- `public string? StringFormat { get; set; }`
- `public MultiBinding() {`
- `public InstancedBinding? Initiate( AvaloniaObject target, AvaloniaProperty? targetProperty, object? anchor = null, bool enableDataValidation = false) {`

### `src/Markup/Avalonia.Markup/Data/RelativeSource.cs`
- `public enum RelativeSourceMode`
- `public enum TreeType`
- `public class RelativeSource`
- `public RelativeSource() {`
- `public RelativeSource(RelativeSourceMode mode) {`
- `public int AncestorLevel {`
- `public Type? AncestorType { get; set; }`
- `public RelativeSourceMode Mode { get; set; }`
- `public TreeType Tree { get; set; } = TreeType.Visual;`

## iOS Platform

### `src/iOS/Avalonia.iOS/AvaloniaAppDelegate.cs`
- `public interface IAvaloniaAppDelegate`
- `public class AvaloniaAppDelegate<TApp> : UIResponder, IUIApplicationDelegate, IAvaloniaAppDelegate`
- `public AvaloniaAppDelegate() {`
- `public UIWindow? Window { get; set; }`
- `public bool FinishedLaunching(UIApplication application, NSDictionary launchOptions) {`
- `public bool OpenUrl(UIApplication app, NSUrl url, NSDictionary options) {`
- `public bool ContinueUserActivity(UIApplication application, NSUserActivity userActivity, UIApplicationRestorationHandler completionHandler) {`

### `src/iOS/Avalonia.iOS/AvaloniaView.Text.cs`
- Namespace: `Avalonia.iOS`
- `public partial class AvaloniaView`
- `public override bool BecomeFirstResponder() {`
- `public override bool ResignFirstResponder() {`

### `src/iOS/Avalonia.iOS/AvaloniaView.cs`
- `public partial class AvaloniaView : UIView, ITextInputMethodImpl`
- `public AvaloniaView() {`
- `public override bool CanBecomeFirstResponder => true;`
- `public override bool CanResignFirstResponder => true;`
- `public override void TraitCollectionDidChange(UITraitCollection? previousTraitCollection) {`
- `public override void TintColorDidChange() {`
- `public void InitWithController<TController>(TController controller) where TController : UIViewController, IAvaloniaViewController {`
- `public static Class LayerClass() {`
- `public override void TouchesBegan(NSSet touches, UIEvent? evt) => _input.Handle(touches, evt);`
- `public override void TouchesMoved(NSSet touches, UIEvent? evt) => _input.Handle(touches, evt);`
- `public override void TouchesEnded(NSSet touches, UIEvent? evt) => _input.Handle(touches, evt);`
- `public override void TouchesCancelled(NSSet touches, UIEvent? evt) => _input.Handle(touches, evt);`
- `public override void PressesBegan(NSSet<UIPress> presses, UIPressesEvent evt) {`
- `public override void PressesChanged(NSSet<UIPress> presses, UIPressesEvent evt) {`
- `public override void PressesEnded(NSSet<UIPress> presses, UIPressesEvent evt) {`
- `public override void PressesCancelled(NSSet<UIPress> presses, UIPressesEvent evt) {`
- `public override void LayoutSubviews() {`
- `public Control? Content {`

### `src/iOS/Avalonia.iOS/NativeControlHostImpl.cs`
- `public class UIViewControlHandle : PlatformHandle, INativeControlHostDestroyableControlHandle`
- `public UIViewControlHandle(UIView view) : base(view.Handle.Handle, UIViewDescriptor) {`
- `public UIView View { get; }`
- `public void Destroy() {`

### `src/iOS/Avalonia.iOS/Platform.cs`
- `public enum iOSRenderingMode`
- `public class iOSPlatformOptions`
- `public IReadOnlyList<iOSRenderingMode> RenderingMode { get; set; } = new[]`
- `public static class IOSApplicationExtensions`
- `public static AppBuilder UseiOS(this AppBuilder builder, IAvaloniaAppDelegate appDelegate) {`
- `public static AppBuilder UseiOS(this AppBuilder builder) => UseiOS(builder, null!);`

### `src/iOS/Avalonia.iOS/ViewController.cs`
- Namespace: `Avalonia.iOS`
- `public interface IAvaloniaViewController`
- `public class DefaultAvaloniaViewController : UIViewController, IAvaloniaViewController`
- `public override void ViewDidLayoutSubviews() {`
- `public override bool PrefersStatusBarHidden() {`
- `public override UIStatusBarStyle PreferredStatusBarStyle() {`
- `public Thickness SafeAreaPadding { get; private set; }`
- `public event EventHandler? SafeAreaPaddingChanged;`

## macOS Native Platform

### `src/Avalonia.Native/AvaloniaNativePlatformExtensions.cs`
- `public static class AvaloniaNativePlatformExtensions`
- `public static AppBuilder UseAvaloniaNative(this AppBuilder builder) {`
- `public enum AvaloniaNativeRenderingMode`
- `public class AvaloniaNativePlatformOptions`
- `public IReadOnlyList<AvaloniaNativeRenderingMode> RenderingMode { get; set; } = new[]`
- `public bool OverlayPopups { get; set; }`
- `public string AvaloniaNativeLibraryPath { get; set; }`
- `public bool AppSandboxEnabled { get; set; } = true;`
- `public class MacOSPlatformOptions`
- `public bool ShowInDock { get; set; } = true;`
- `public bool DisableDefaultApplicationMenuItems { get; set; }`
- `public bool DisableNativeMenus { get; set; }`
- `public bool DisableSetProcessName { get; set; }`
- `public bool DisableAvaloniaAppDelegate { get; set; }`
