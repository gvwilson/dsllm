# Convert LLM Prompts to Blockquotes

## Task

Convert all italicized LLM prompts (`*text*`) in lesson files to Markdown blockquotes (`> text`).

## Files Modified

- `intro/index.md`
- `clean/index.md`
- `validate/index.md`
- `tables/index.md`
- `summarize/index.md`
- `stories/index.md`
- `repro/index.md`
- `prompts/index.md`
- `llm/index.md`
- `join/index.md`
- `finale/index.md`
- `chart/index.md`
- `change/index.md`

## Approach

Used a Python script to scan each file line by line. Lines starting with `*` (but not `**`) were treated as prompt delimiters. Single-line prompts (`*text*`) had both asterisks stripped and the line prefixed with `> `. Multi-line prompts (opening `*` without closing `*` on the same line) had all continuation lines also prefixed with `> ` until the closing `*` was found.
