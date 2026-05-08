# Proposal: ban product-native source handles in Markdown output

## Summary

Strengthen `repo-prompt-markdown-format` so governed Markdown outputs cannot contain product-native citation or source handles such as `cite...`, `url...`, `turn8search14`, or similar opaque model UI references.

The fix belongs in the shared Markdown contract so every manifest that inlines `repo-prompt-markdown-format` inherits the rule.

## Motivation

A recent platform discovery output used product-native source markers and URL handles instead of portable Markdown links. The current formatting contract already bans AI-specific markers, but it only names one example form. Some web models use other marker families, so the contract should ban the class of artifact explicitly.

The desired output is portable Markdown:

```md
[Official page](https://example.com)
```

not product-specific handles:

```text
urlOfficial pageturn8search14
citeturn11view6
```

## Scope

In scope:

- update `repo-prompt-markdown-format`
- explicitly ban product-native source handles, citation handles, search-result handles, and opaque `turn...` references
- require inline Markdown links with real URL targets for link output

Out of scope:

- changing observe output contracts
- cleaning generated model outputs
- changing prompt manifests
