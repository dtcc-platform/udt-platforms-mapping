## MODIFIED Requirements

### Requirement: Excluded Type means outside platform discovery boundary

An artifact SHALL be classified as `excluded` when it is not a technical UDT artifact, is only an initiative or project without identifiable technical substrate, or falls outside the study boundary.

Map storytelling tools, communication tools, presentation tools, and lightweight web-map narrative tools SHALL be classified as `excluded` unless they expose a distinct technical artifact that satisfies `platform`, `framework`, or `module` criteria.

Initiatives, programmes, deployments, and projects SHALL be tracked in initiative discovery unless they expose a distinct technical artifact that can be classified by platform discovery.

#### Scenario: Artifact is excluded

- **WHEN** an item has no identifiable technical artifact
- **THEN** platform discovery classifies it as `excluded`

#### Scenario: StoryMapJS-style tool is considered

- **WHEN** a tool is mainly presented as map-based storytelling, communication, or narrative publishing
- **THEN** platform discovery classifies it as `excluded`
- **THEN** the exclusion reason explains that it is not a technical UDT artifact
