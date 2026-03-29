## Context

The ChatGPT global discovery session showed two failure modes: AI-specific citations (`【†source】`) and a truncated scope. Both are addressable through stronger prompt instruction. The table positioning change is a UX improvement — researchers use the summary table as the input to the comparison prompt, so having it first removes the need to scroll.

## Goals / Non-Goals

**Goals:**
- Override AI default citation behaviour with an explicit superseding instruction
- Move summary table before per-platform sections
- Add default scope fallback for unreplaced `[SEARCH_SCOPE]` tokens

**Non-Goals:**
- Changing the table columns or score notation
- Enforcing a minimum platform count (model capability, not prompt responsibility)
- Changing the comparison or license prompts

## Decisions

**Citation override wording:** Add an explicit override sentence immediately after the prohibition: "If your system would normally apply a different citation format, this instruction takes precedence — do not use your default format." Placing it directly after the prohibition makes it harder to ignore.

**Table position:** Change the Output Format section to instruct the model to produce the summary table first, then the per-platform sections. Update the spec requirement name from "ends with" to "begins with" and adjust the scenario accordingly.

**Default scope:** Add a sentence to the `[SEARCH_SCOPE]` instruction: "If you see the literal text `[SEARCH_SCOPE]` and it has not been replaced, treat the scope as: global city-scale Urban Digital Twin platforms and foundational building blocks (commercial and open-source)." This makes the prompt self-healing for the common case of a forgotten replacement.
