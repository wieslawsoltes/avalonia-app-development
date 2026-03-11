# Fluent Localization, BiDi, and Inclusive Content Patterns

## Table of Contents
1. Scope and Primary APIs
2. Fluent Localization Rules
3. BiDi and Mirrored Fluent Shells
4. Inclusive Content and Command Language
5. AOT and Runtime Notes
6. Do and Don't Guidance
7. Troubleshooting
8. Official Resources

## Scope and Primary APIs

Use this reference to keep Fluent UI calm, clear, and correct across languages, directions, and user contexts.

Primary APIs:
- `FlowDirection`
- `TextBlock`, `SelectableTextBlock`
- `Button`, `MenuFlyout`, `ToolTip`
- `Grid`, `SplitView`, `TabControl`
- `AutomationProperties`

This file covers:
- translation-safe Fluent copy,
- mirrored layouts and RTL shell expectations,
- inclusive command and status language,
- keeping Fluent language-system rules intact across locales.

## Fluent Localization Rules

Fluent language should survive localization without losing clarity.

Rules:
- keep labels concise but specific,
- avoid layout that assumes short English verbs,
- prefer semantically stable wording over clever phrasing,
- keep paired actions parallel so translation remains predictable,
- let supporting text wrap rather than clip when possible.

```xml
<Grid xmlns="https://github.com/avaloniaui"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      ColumnDefinitions="*,Auto"
      ColumnSpacing="12">
  <TextBlock TextWrapping="Wrap"
             Text="Review the release summary and choose the next step." />
  <Button Grid.Column="1"
          MinWidth="144"
          Content="Deploy now" />
</Grid>
```

## BiDi and Mirrored Fluent Shells

Fluent shells should respect language direction, not just text direction.

```xml
<SplitView xmlns="https://github.com/avaloniaui"
           xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
           FlowDirection="RightToLeft"
           DisplayMode="Inline"
           IsPaneOpen="True">
  <SplitView.Pane>
    <ListBox ItemContainerTheme="{StaticResource FluentNavItemTheme}" />
  </SplitView.Pane>
</SplitView>
```

Rules:
- test global navigation, tabs, and dialogs in RTL,
- review icons and directional metaphors,
- avoid saying `left` or `right` when `start` or `end` is the real concept,
- keep mirrored layouts feeling intentional rather than mechanically flipped.

## Inclusive Content and Command Language

Inclusive Fluent copy should:
- reduce uncertainty,
- avoid blame,
- stay specific in error and risk states,
- support both novice and expert users.

Good examples:
- `Retry checks`
- `Delete environment`
- `View history`

Weak examples:
- `Proceed`
- `OK`
- `Something went wrong`

## AOT and Runtime Notes

- `FlowDirection` is normal compiled-XAML surface area in Avalonia and should be part of shell testing.
- Keep Fluent content rules in shared guidance and review checklists rather than page-level exceptions.
- Audit custom drawing or text-layout code paths for culture and flow-direction assumptions.

## Do and Don't Guidance

Do:
- test Fluent shells under long strings and RTL,
- write command text for clarity before brevity,
- include localization and inclusion in design reviews.

Do not:
- assume Fluent color and spacing are enough without Fluent language quality,
- rely on directional icons without RTL review,
- let translated screens quietly degrade command hierarchy.

## Troubleshooting

1. The app still feels English-first.
- Fixed-width action bars and short-label assumptions are usually the cause.

2. RTL shells feel mirrored but awkward.
- Revisit navigation hierarchy and directional iconography, not only text.

3. Inclusive review still finds friction.
- The visual system may be fine while the language system remains too vague or too expert-only.

## Official Resources

- Design for bidirectional text: [learn.microsoft.com/en-us/windows/apps/design/globalizing/design-for-bidi-text](https://learn.microsoft.com/en-us/windows/apps/design/globalizing/design-for-bidi-text)
- Adjust layout and fonts and support RTL: [learn.microsoft.com/en-us/windows/apps/design/globalizing/adjust-layout-and-fonts--and-support-rtl](https://learn.microsoft.com/en-us/windows/apps/design/globalizing/adjust-layout-and-fonts--and-support-rtl)
- Prepare your app for localization: [learn.microsoft.com/en-us/windows/apps/design/globalizing/prepare-your-app-for-localization](https://learn.microsoft.com/en-us/windows/apps/design/globalizing/prepare-your-app-for-localization)
- Designing inclusive software: [learn.microsoft.com/en-us/windows/apps/design/accessibility/designing-inclusive-software](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/designing-inclusive-software)
- Fluent 2 accessibility: [fluent2.microsoft.design/accessibility](https://fluent2.microsoft.design/accessibility)
- Fluent 2 content design: [fluent2.microsoft.design/content-design](https://fluent2.microsoft.design/content-design)
