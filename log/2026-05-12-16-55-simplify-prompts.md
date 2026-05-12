# Simplify Prompts in Subsequent Lessons

## Context

User edited `clean/index.md` to replace `- Paste this prompt: "..."` style with a
simple/or/technical pattern matching the audience's level.

## Changes Made

Updated 7 files to replace `Paste this prompt: "..."` (with quoted text) with:

```
*Simple colloquial prompt.*

or

*Detailed technical prompt with column names, tools, and constraints.*
```

### Files modified

- `summarize/index.md` - 3 occurrences
- `tables/index.md` - 3 occurrences
- `change/index.md` - 2 explicit + 1 inline (`Ask the LLM to print the slope: "..."` lifted to standalone italicized prompt)
- `join/index.md` - 2 occurrences; prerequisite `load_both.py` step moved to after both prompts
- `stories/index.md` - 3 occurrences
- `validate/index.md` - 2 occurrences
- `repro/index.md` - 1 occurrence; data description bullets placed between simple and technical prompts

### Files NOT modified

- `prompts/index.md` - intentionally contrasts vague vs. detailed prompting; the existing structure is the lesson's point
- `finale/index.md` - already uses simple italicized prompts throughout
