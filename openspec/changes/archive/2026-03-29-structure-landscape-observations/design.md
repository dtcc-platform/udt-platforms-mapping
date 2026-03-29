## Context

Part 3 of the comparison output currently instructs the model with four open-ended questions. The model is free to answer in any format — prose, lists, mixed — leading to inconsistent output across agents and sessions. The change enforces four named `####` subheadings, each containing a bullet list, so the structure is predictable and comparable.

## Goals / Non-Goals

**Goals:**

- Replace the four loose questions in the Part 3 prompt instruction with four `####` subheadings and explicit list format
- Specify `####` heading level to avoid visual conflict with `###` platform profile headings in Part 2

**Non-Goals:**

- Changing the content scope of Part 3 (the four topics remain the same)
- Adding new landscape topics beyond the current four

## Decisions

**`####` heading level, not `###`**

Platform profiles in Part 2 use `###`. Using `###` for Part 3 subheadings would make them visually indistinguishable from platform profiles in a rendered document. `####` nests cleanly under the Part 3 section heading and preserves the hierarchy: document → part → subheading.

**Four subheadings, not merged**

"DTCC's Position" and "Comparable Platforms" are related but distinct: position is a narrative claim about DTCC's place in the landscape; comparable platforms is an enumeration of specific platforms. Merging them would force the model to conflate a qualitative statement with a list, reducing scannability. Keeping them separate preserves both.

**Exact subheading names specified in the prompt**

Leaving naming to the model risks variation ("Comparable" vs "Most Comparable" vs "Direct Competitors"). The prompt specifies exact heading text so responses are consistent across agents.

## Risks / Trade-offs

**Model may add additional subheadings** → The prompt says "include the following subheadings" — some models interpret this permissively and add extras. Mitigation: phrase the instruction as "use exactly the following four subheadings."

**Heading text is now a formatting contract** → If a subheading name ever changes, saved response files will be inconsistent with the new format. Low risk given the stability of these four topics.
