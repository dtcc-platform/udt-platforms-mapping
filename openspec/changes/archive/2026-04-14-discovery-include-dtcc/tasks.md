## 1. Update Discovery Prompt

- [x] 1.1 Add explicit instruction to include DTCC as a required research entry in every discovery session
- [x] 1.2 Specify primary sources for DTCC research (dtcc.chalmers.se, official GitHub repository)
- [x] 1.3 Clarify that DTCC appears in the summary table with a full per-platform section (Relevance 3–5 tier, identification block + 12 dimensions)

## 2. Update Comparison Prompt

- [x] 2.1 Remove the hardcoded DTCC description block from the comparison prompt
- [x] 2.2 Remove the instruction to add DTCC independently; replace with instruction to treat the DTCC row from the pasted table as the reference platform for Part 3
- [x] 2.3 Add a note in the usage header (or near `[PASTE_SELECTED_PLATFORMS_HERE]`) that the DTCC row must be included when selecting platforms to compare
