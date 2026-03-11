# Fluent Language System for Status, Confirmations, and Notifications

## Table of Contents
1. Scope and Primary APIs
2. Status and Recovery Language
3. Confirmation and Risk Patterns
4. Notification and Message Patterns
5. AOT and Runtime Notes
6. Do and Don't Guidance
7. Troubleshooting
8. Official Resources

## Scope and Primary APIs

Use this reference to extend Fluent language-system guidance into operational status, risk, and notification moments.

Primary APIs:
- `TextBlock`, `SelectableTextBlock`
- `Button`, `MenuFlyout`, `ToolTip`
- `WindowNotificationManager`
- `TransitioningContentControl`
- `AutomationProperties`

This file covers:
- status copy,
- error and recovery language,
- confirmations and destructive actions,
- in-app notifications and message surfaces.

## Status and Recovery Language

Status copy should answer:
- what happened,
- what it means,
- what the user can do next.

```xml
<Border xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Classes="status-surface"
        Padding="12">
  <StackPanel Spacing="6">
    <TextBlock FontWeight="SemiBold" Text="Deployment paused" />
    <TextBlock Foreground="{DynamicResource Brush.Text.Secondary}"
               Text="Verification found one blocking check. Fix the issue and retry the rollout." />
    <Button Content="Retry checks" />
  </StackPanel>
</Border>
```

Guidance:
- make status language explicit and specific,
- avoid blame-focused language,
- prefer one recovery action over several weak ones,
- keep warning and error tone calm.

## Confirmation and Risk Patterns

Use confirmations only when risk or irreversibility justifies them.

Rules:
- destructive labels should name the consequence,
- confirmations should restate the object or scope affected,
- quiet actions should not get heavy confirmation treatment,
- if undo is available, prefer that over constant blocking confirmations.

Good labels:
- `Delete environment`
- `Remove access`
- `Retry sync`

Weak labels:
- `Yes`
- `OK`
- `Confirm`

## Notification and Message Patterns

Avalonia does not ship the WinUI `InfoBar` control in the core framework, so Fluent-style message surfaces usually map to a themed `Border`, `Flyout`, or `WindowNotificationManager`.

Use:
- inline status surfaces for contextual issues,
- managed notifications for transient completion or warning messages,
- flyouts or dialogs when the user must make a choice.

Guidance:
- toast-like notifications should be short and low-risk,
- inline messages should stay near the affected workflow,
- do not make notifications carry essential missing context.

## AOT and Runtime Notes

- Keep status and notification surfaces theme-driven and shared.
- Prefer one or two reusable status surface variants instead of view-local ad hoc designs.
- Keep notification copy generation separate from styling rules so both can evolve safely.

## Do and Don't Guidance

Do:
- use explicit nouns and verbs in status copy,
- make destructive actions unmistakable,
- align notification tone with the rest of the product.

Do not:
- rely on vague confirmations,
- use transient notifications for critical unrecoverable failures,
- mix calm Fluent visuals with sharp or inconsistent language.

## Troubleshooting

1. The product looks Fluent but sounds generic.
- The language system likely stops at headings and buttons instead of covering status moments.

2. Confirmations feel heavy and repetitive.
- Reserve them for real risk and prefer undo where appropriate.

3. Notifications feel disconnected.
- Reuse the same voice, spacing, and hierarchy rules as the main shell.

## Official Resources

- Fluent 2 content design: [fluent2.microsoft.design/content-design](https://fluent2.microsoft.design/content-design)
- Fluent 2 message bar guidance: [fluent2.microsoft.design/components/web/react/core/messagebar/usage](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)
- Fluent 2 toast guidance: [fluent2.microsoft.design/components/web/react/core/toast/usage](https://fluent2.microsoft.design/components/web/react/core/toast/usage)
- Microsoft Style Guide welcome: [learn.microsoft.com/en-us/style-guide/welcome](https://learn.microsoft.com/en-us/style-guide/welcome/)
