# Accessibility and Automation

## Table of Contents
1. Scope and APIs
2. Automation Model
3. Authoring Patterns
4. Accessibility Practices
5. Troubleshooting

## Scope and APIs

Primary APIs:
- `AutomationProperties`
- `AutomationPeer`
- `ControlAutomationPeer`
- `AutomationControlType`
- `AutomationLiveSetting`
- `Control.OnCreateAutomationPeer()`

Important members:
- `AutomationProperties.SetName/GetName`
- `AutomationProperties.SetAutomationId/GetAutomationId`
- `AutomationProperties.SetHelpText/GetHelpText`
- `AutomationProperties.SetLabeledBy/GetLabeledBy`
- `AutomationProperties.SetControlTypeOverride/GetControlTypeOverride`
- `AutomationProperties.SetLiveSetting/GetLiveSetting`
- `AutomationProperties.SetAccessKey/GetAccessKey`
- `AutomationPeer.GetName()`, `GetAutomationId()`, `GetAutomationControlType()`
- `AutomationPeer.GetHelpText()`, `GetLabeledBy()`, `GetLiveSetting()`
- `ControlAutomationPeer.CreatePeerForElement(...)`

Reference source files:
- `src/Avalonia.Controls/Automation/AutomationProperties.cs`
- `src/Avalonia.Controls/Automation/Peers/AutomationPeer.cs`
- `src/Avalonia.Controls/Automation/Peers/ControlAutomationPeer.cs`
- `src/Avalonia.Controls/Automation/AutomationLiveSetting.cs`
- `src/Avalonia.Controls/Control.cs`

## Automation Model

Model summary:
1. Control creates an automation peer (`OnCreateAutomationPeer`).
2. Peer exposes automation metadata and tree relationships.
3. `AutomationProperties` attached properties provide defaults and overrides.
4. Platform accessibility backends consume peer data.

## Authoring Patterns

### Set core automation metadata in XAML

```xml
<TextBox
    AutomationProperties.Name="Email"
    AutomationProperties.AutomationId="EmailInput"
    AutomationProperties.HelpText="Enter your work email" />
```

### Associate label and control for assistive tech

```xml
<Label x:Name="EmailLabel" Content="_Email" Target="{Binding #EmailBox}" />
<TextBox x:Name="EmailBox"
         AutomationProperties.LabeledBy="{Binding #EmailLabel}" />
```

### Custom automation peer for custom control

```csharp
using Avalonia.Automation.Peers;
using Avalonia.Controls;

public class StatusBadge : Control
{
    protected override AutomationPeer OnCreateAutomationPeer()
        => new StatusBadgeAutomationPeer(this);
}

public sealed class StatusBadgeAutomationPeer : ControlAutomationPeer
{
    public StatusBadgeAutomationPeer(StatusBadge owner) : base(owner) { }

    protected override AutomationControlType GetAutomationControlTypeCore()
        => AutomationControlType.Group;

    protected override string? GetNameCore()
        => AutomationProperties.GetName(Owner) ?? "Status";
}
```

## Accessibility Practices

- Always provide a meaningful `AutomationProperties.Name` for actionable controls.
- Keep `AutomationId` stable for test automation and assistive tooling.
- Use `LabeledBy` for form controls when label text is not part of control content.
- Use `LiveSetting` only for true live regions to avoid noisy announcements.
- Keep focus order and automation tree order predictable.

## Troubleshooting

1. Screen reader reads generic or empty names:
- `AutomationProperties.Name` missing and peer fallback is weak.

2. Control not discoverable:
- Accessibility view/control type overrides hide it unexpectedly.

3. Wrong control role announced:
- Missing or incorrect `ControlTypeOverride` for custom interaction model.

4. Live updates not announced:
- `LiveSetting` not set or content changes not represented in peer-visible properties.

## XAML-First and Code-Only Usage

Default mode:
- Declare automation semantics in XAML first.
- Use code-only automation metadata/peer wiring only when requested.

XAML-first complete example:

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            Spacing="8">
  <Label x:Name="EmailLabel" Content="_Email" Target="{Binding #EmailBox}" />
  <TextBox x:Name="EmailBox"
           AutomationProperties.Name="Email"
           AutomationProperties.AutomationId="EmailInput"
           AutomationProperties.LabeledBy="{Binding #EmailLabel}" />
</StackPanel>
```

Code-only alternative (on request):

```csharp
using Avalonia.Automation;

AutomationProperties.SetName(emailBox, "Email");
AutomationProperties.SetAutomationId(emailBox, "EmailInput");
AutomationProperties.SetHelpText(emailBox, "Enter your work email address");
AutomationProperties.SetLabeledBy(emailBox, emailLabel);
```
