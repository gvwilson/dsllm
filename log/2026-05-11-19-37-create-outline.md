# 2026-05-11 19:37 UTC - Create Outline

## Prompts

1. Write an outline in outline.txt for this tutorial. Assume twelve sessions
   of one hour each.
2. They don't want to write code. Assume the LLM is writing the code for the
   first six lessons. Rewrite the outline.
3. Do not include SQL. Assume people are loading dataframes from sqlite, but
   not writing them. This will be incidental to the main work.
4. There should be some statistical analysis in each lesson — introduce all
   basic statistical ideas (probability, inference, hypothesis testing,
   confidence intervals, regression) at most one per lesson. Agreed mapping:
   S1 what stats is for, S2 mean/median, S3 spread, S4 sampling bias,
   S5 central tendency, S6 correlation, S7 probability, S8 probability applied
   to seasonal patterns, S9 regression, S10 correlation vs causation,
   S11 inference/hypothesis testing, S12 confidence intervals.

## Actions

- Read README.md, intro/index.md, finale/index.md, CLAUDE.md
- Ran `brief .` to understand project structure
- Wrote outline.txt with 12 sessions plus appendices section
- Rewrote outline.txt: sessions 1-6 are pure prompt-run-interpret (no code
  reading or writing); sessions 7-12 add enough code literacy to verify
  outputs and catch errors, but learners still do not write code from scratch

## Decisions

- Sessions 1-6: LLM writes all code; learner writes prompts, runs scripts,
  reads output tables and charts, iterates via re-prompting
- Sessions 7-12: learner reads code the LLM wrote (SQL in session 8 because
  it is more readable than Python), asks LLM to explain code, verifies by
  checking outputs against known values rather than auditing code directly
- Removed "read code line by line" and "edit the code" from sessions 1-6;
  re-prompting replaces manual editing throughout
- Checking session (11) uses unit-error scenario so verification strategy
  is concrete and does not require reading code
- Session 6 uses Anscombe's quartet to motivate visualization without
  requiring learners to understand the underlying statistics
