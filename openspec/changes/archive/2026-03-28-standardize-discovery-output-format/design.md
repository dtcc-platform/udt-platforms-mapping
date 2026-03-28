## Context

The current discovery prompt asks for a Markdown table followed by short paragraphs. In practice, AI agents interpret this differently: some write dense prose, some omit fields, some merge the table and notes. The result is responses that look different across ChatGPT, Claude, and Gemini, making it harder to scan, compare, and transfer data to the inventory.

The fix is to replace the table+paragraph pattern with a per-platform section structure — one `##` heading per platform, with a fixed bullet list of fields. This is more scannable, easier to diff, and unambiguous enough that any agent produces the same shape.

## Goals / Non-Goals

**Goals:**
- Define a concrete output template in the prompt that any agent can follow mechanically
- Make responses consistent across ChatGPT, Claude, Gemini, and future agents
- Keep each platform's data self-contained and scannable
- Tighten the spec requirement to reflect the new format

**Non-Goals:**
- Change the inclusion criteria or research instructions
- Change the metadata block, Markdown syntax rules, or save-as instruction
- Redesign the inventory schema

## Decisions

**Per-platform `##` heading + bullet fields instead of table + paragraphs**

The table pattern requires agents to fit multi-sentence values into table cells, which breaks rendering or forces truncation. A heading + bullet list per platform gives agents natural room for each field and produces a consistent, diffable structure.

Field set mirrors inventory columns directly:
```
## <Platform Name>

- **Organization:** <name>
- **Link:** [<label>](<url>)
- **License:** <license> — <open-source / proprietary>
- **Type:** <e.g., visualization engine, data platform, simulation framework>
- **Maturity:** <experimental / research / production-ready>
- **City-scale capability:** <what makes it relevant to UDT>
- **Integration posture:** <e.g., open APIs, SDK, standalone>
- **Inclusion criterion:** <which of the three criteria it satisfies>
- **Notes:** <limitations, gaps, or anything notable>
```

Agents are told to use exactly these field labels so responses are grep-able and the structure is predictable.

**Keep the summary table as optional**

Some researchers may want a quick overview. The prompt will instruct agents to produce the per-platform sections first, then optionally append a summary table. This keeps the structured data primary without removing the overview entirely.

## Risks / Trade-offs

- Longer responses — per-platform sections with 9 fields are more verbose than a table row → acceptable, the goal is readability over brevity
- Agents may still deviate — mitigated by showing a concrete example in the prompt rather than describing the format abstractly
- Existing saved responses use the old format — no migration needed, they remain valid historical records

## Open Questions

- Should the summary table be required or truly optional? Leaning optional — researchers who need it can ask the agent to add one.
