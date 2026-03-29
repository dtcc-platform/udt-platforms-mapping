## Context

The discovery and comparison prompts both include explicit "use primary sources only" and "distinguish facts from inference / state unknown" instructions in their body. The license prompt's Research Instructions section only lists the five checklist steps without these cross-cutting research conduct rules.

The Output Format section shows field labels but no filled-in example, so models must infer the expected shape. The other two prompts both provide a fictional example.

## Goals / Non-Goals

**Goals:**
- Add primary-sources and uncertainty instructions to the license prompt body (before or within Research Instructions)
- Add a concrete fictional license analysis example to the Output Format section

**Non-Goals:**
- Changing the spec (requirements already exist)
- Changing the taxonomy tables, rubric, or checklist steps

## Decisions

**Placement of research conduct instructions:** Add them as a short paragraph directly after the `[PASTE_SELECTED_PLATFORM_HERE]` block and before the taxonomy section — matching the pattern in the comparison prompt where conduct rules appear near the top of the body, before the dimension rubrics.

**Example placement:** Append the fictional example after the Output Format field template, separated by a horizontal rule — matching the comparison prompt's example placement. Use a clearly fictional platform name and realistic but invented data.

**Example scope:** Cover all five output sections (Software License, Data Licensing, Community vs. Enterprise Split, Score, Open Questions) so the model has a complete shape to follow.
