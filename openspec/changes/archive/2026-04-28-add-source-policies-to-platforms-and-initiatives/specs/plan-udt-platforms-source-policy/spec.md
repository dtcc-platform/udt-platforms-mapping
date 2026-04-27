## ADDED Requirements

### Requirement: UDT platforms source policy file exists

The repository SHALL contain a file at `plan/udt-platforms/source-policy.md` that governs acceptable evidence and source-priority rules for the `udt-platforms` cycle.

#### Scenario: Researcher opens the platforms planning inputs
- **WHEN** a researcher inspects `plan/udt-platforms/`
- **THEN** they find a `source-policy.md` file alongside the cycle’s other canonical inputs

### Requirement: UDT platforms source policy defines ranked evidence for technical-artifact mapping

`plan/udt-platforms/source-policy.md` SHALL define a ranked evidence model for technical-artifact mapping that prioritizes official technical documentation, official repositories, standards or specifications, peer-reviewed literature, official organizational communications, technical reports, and reputable secondary sources.

It SHALL explicitly distinguish preferred primary evidence from corroborating secondary evidence.

#### Scenario: Researcher checks whether a vendor blog can stand alone
- **WHEN** the researcher reads `plan/udt-platforms/source-policy.md`
- **THEN** the policy makes clear whether vendor communications are primary evidence or only supporting evidence relative to higher-ranked sources

### Requirement: UDT platforms source policy rejects unreliable evidence classes

`plan/udt-platforms/source-policy.md` SHALL identify unacceptable evidence classes for canonical mapping outputs, including anonymous forum posts, AI-generated summaries, and undated or unattributed pages with unclear provenance.

#### Scenario: Researcher considers an unattributed summary page
- **WHEN** a candidate source lacks authorship or provenance
- **THEN** the policy tells the researcher that the source is not acceptable as canonical evidence

### Requirement: UDT platforms source policy defines contradiction handling

`plan/udt-platforms/source-policy.md` SHALL define how contradictions between sources are handled, including preferring higher-ranked sources and recording material discrepancies when classification or inclusion depends on conflicting evidence.

#### Scenario: Documentation and a secondary article disagree
- **WHEN** an official repository or documentation page contradicts a lower-ranked article
- **THEN** the policy requires the higher-ranked source to control the canonical mapping judgment and the discrepancy to be noted if it matters
