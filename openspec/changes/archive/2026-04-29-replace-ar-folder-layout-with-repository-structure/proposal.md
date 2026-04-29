# Proposal: replace-ar-folder-layout-with-repository-structure

## Why

`ar-folder-layout` no longer names its role accurately.

The current spec governs more than folder placement. It defines:

- the top-level phase structure
- canonical research-thread locations
- canonical prompt and output locations
- README explanation requirements for the active workflow

Keeping that contract under the name `ar-folder-layout` makes the baseline harder to read and weakens the clarity of the spec set.

The repository still needs a first-class structural spec. This change does not remove that concern. It replaces the misleading capability name with one that matches the current scope of the contract.

## What Changes

- retire `ar-folder-layout`
- add `repository-structure` as the replacement structural capability
- carry over the current baseline structural requirements under the new name
- update any baseline references that still rely on the old capability name

## Impact

- improves the readability of the baseline spec set
- makes the structure-vs-naming separation clearer
- prepares the repo for a separate naming-conventions capability without overloading the structural spec
