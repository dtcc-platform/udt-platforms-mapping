# UDT Ecosystem Discovery — Layer Classification

This file defines the Layer classification system used in the **discovery phase** of the UDT ecosystem mapping study.
Paste the full content of this file into the `[PASTE_SCOPE_HERE]` slot in the discovery prompt before running a session.

---

## Layer Criteria

Assign each discovered platform exactly one Layer value using the observable criteria below. All four values are valid outputs from a discovery session.

| Layer           | Definition                                    | Criteria                                                                                          |
| --------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `core-platform` | Full UDT platform                             | Official docs claim city-scale digital twin; owns data + simulation + visualisation as one system |
| `backbone`      | Enabling infrastructure layer                 | Designed to be composed into other systems; API/SDK is primary interface, not end-user UI         |
| `domain-module` | Domain-specific urban analytics or simulation | Covers one urban domain (mobility, energy, climate…); outputs consumed by a larger UDT stack      |
| `excluded`      | Outside the study boundary                    | None of the above apply; note reason in one sentence                                              |
