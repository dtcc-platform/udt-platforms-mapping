# Platform Definition

This file defines the technical-artifact classification used in platform discovery.
Platform discovery is a broad global discovery action.
Its job is to maximize recall across software or technical artifacts from literature and current ecosystem evidence, while keeping the classification contract stable.

Initiatives and projects are tracked separately in initiative discovery. They are not primary rows in the platform discovery summary table.

---

## Type Criteria

Assign each discovered artifact exactly one `Type` value using the observable criteria below.

| Type        | Definition                                 | Observable Criteria                                                                                                                |
| ----------- | ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| `platform`  | Usable UDT platform for urban environments | Presented as a deployable or usable system for city-scale integration, visualization, simulation, or management of urban systems   |
| `framework` | Reusable development or enabling structure | Presented as an SDK, API-centered backbone, reusable architecture, or enabling framework rather than the primary end-user platform |
| `module`    | Narrower capability component              | Covers a specific urban capability, workflow, or domain and is meant to be used inside or alongside a larger UDT stack             |
| `excluded`  | Outside the study boundary                 | None of the above apply; record a brief reason                                                                                     |

## Interpretation Rules

Classify by the artifact's observable presentation and role in the urban digital twin ecosystem, not by name alone.
Use public descriptions, documentation, papers, product pages, repositories, or project pages to decide what role the artifact is presented as playing.

Assign exactly one `Type` value per artifact.
When an artifact appears to fit more than one type, use this tie-break guidance:

1. Use `platform` when the artifact is presented as a usable or deployable city-scale UDT system, even if it exposes APIs, SDKs, modules, or framework-like extension points.
2. Use `framework` when the artifact is mainly presented as a reusable architecture, toolkit, API backbone, SDK, reference model, or enabling layer for building UDT systems rather than as the primary end-user platform.
3. Use `module` when the artifact mainly provides one bounded capability, domain workflow, analytical function, data pipeline, visualization component, simulator, or integration component for use inside or alongside a broader UDT stack.
4. Use `excluded` when the artifact is not a technical UDT artifact, is only an initiative or project without identifiable technical substrate, or falls outside the study boundary.

Preserve uncertainty when evidence is weak or ambiguous.
Do not upgrade an artifact to `platform` only because it has an ambitious name, is part of a smart-city initiative, or is mentioned near UDT language.
If the technical role is unclear, classify using the strongest observable evidence and make the uncertainty visible in the reason or artifact details.

Initiatives, programmes, deployments, and projects are tracked in initiative discovery unless they expose a distinct technical artifact that can be classified here.
