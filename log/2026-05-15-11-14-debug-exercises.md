# Debug and Extend Exercises

**Date:** 2026-05-15 11:14 UTC

## Prompt

Add four exercises to each chapter except intro and finale in which learners are
presented with a short piece of code relevant to the chapter that contains a bug or
that needs to be extended in some way, and are asked to find and fix the bug or add
the new feature or capability starting from the existing code with an LLM's assistance.
The emphasis of each exercise is, "how do you know the answer is (now) right?"
Look at `../unbreak/datasci` for inspiration.

## Decisions

- Exercises are added after the existing four exercises in each chapter's `## Exercises` section.
- Extension exercises use a `# TODO` comment to mark where new code goes.
- Each exercise ends with a verification question ("How do you know the fix worked?") that names one or two specific things to check.
- Bugs are chosen to be plausible: they produce wrong output rather than loud errors where possible.

## Files Created (44 Python files)

| Chapter | File | Type | Issue |
|---------|------|------|-------|
| llm | `skip_bug.py` | bug | `skip_rows=0` so title row becomes data header |
| llm | `wrong_col.py` | bug | reads `Total Precip (mm)` instead of `Mean Temp (°C)` |
| llm | `null_miss.py` | bug | missing `null_values=[""]` so temperature column reads as String |
| llm | `mm_extend.py` | extend | add min, max, count to mean/median output |
| chart | `axis_bug.py` | bug | depth and magnitude column bindings swapped |
| chart | `col_bug.py` | bug | `"Magnitude:Q"` (capital M) doesn't match column `"magnitude"` |
| chart | `type_bug.py` | bug | magnitude encoded without `:Q` so Altair treats it as nominal |
| chart | `opacity_extend.py` | extend | add `opacity=0.4` to mark_point |
| clean | `null_partial.py` | bug | `null_values=["U"]` only — misses `Q` and `N` |
| clean | `strip_bug.py` | bug | province groups not stripped so padded duplicates appear |
| clean | `drop_bug.py` | bug | `drop_nulls()` with no subset drops any row with any null |
| clean | `rate_extend.py` | extend | add collisions per 100,000 people column |
| summarize | `order_bug.py` | bug | `.sum()` before `.group_by()` produces one-row output |
| summarize | `year_bug.py` | bug | `.dt.month()` instead of `.dt.year()` |
| summarize | `small_n_extend.py` | extend | flag CI rows where n < 5 |
| summarize | `vendor_bug.py` | bug | groups by department instead of vendor |
| tables | `type_bug.py` | bug | FLOW forced to String type so statistics return None |
| tables | `sentinel_bug.py` | bug | sentinel value not filtered before computing max |
| tables | `std_extend.py` | extend | add coefficient of variation per station |
| tables | `filter_bug.py` | bug | `"Station_Number"` wrong case — should be `"STATION_NUMBER"` |
| prompts | `threshold_bug.py` | bug | `LEAD_THRESHOLD = 10.0` instead of `1.0` |
| prompts | `substance_bug.py` | bug | substance name in lowercase — doesn't match CSV |
| prompts | `denom_bug.py` | bug | denominator is all NPRI facilities, not just lead reporters |
| prompts | `count_extend.py` | extend | print numerator and denominator alongside proportion |
| change | `axes_bug.py` | bug | regression x and y swapped — slope has wrong units and sign |
| change | `mean_bug.py` | bug | `.mean()` instead of `.max()` for annual peak ILI |
| change | `raw_bug.py` | bug | trend fitted to all weekly rows instead of annual peaks |
| change | `pandemic_extend.py` | extend | refit slope after removing 2009 pandemic year |
| join | `inner_bug.py` | bug | `how="inner"` silently drops unmatched temperature rows |
| join | `case_bug.py` | bug | `left_on="Station_ID"` doesn't match column `"station_id"` |
| join | `dup_extend.py` | extend | detect duplicate station IDs in station file |
| join | `unmatched_extend.py` | extend | print null province count and sample unmatched IDs |
| stories | `axis_bug.py` | bug | y axis domain `[55, 75]` exaggerates differences |
| stories | `facet_bug.py` | bug | facets on `board_type` instead of `school_language` |
| stories | `color_bug.py` | bug | reading score encoded as `:N` instead of `:Q` |
| stories | `count_extend.py` | extend | add school count as text mark on bars |
| validate | `unit_bug.py` | bug | production not converted before ratio computed |
| validate | `onetail_bug.py` | bug | `alternative="greater"` instead of `"two-sided"` |
| validate | `col_bug.py` | bug | filters on "Alberta" / "British Columbia" but data uses "AB" / "BC" |
| validate | `effect_extend.py` | extend | add Cohen's d alongside t-test |
| repro | `path_bug.py` | bug | hardcoded absolute path `/Users/alice/Desktop/...` |
| repro | `sentinel_bug.py` | bug | `null_values=[""]` doesn't catch `-999.99` sentinel |
| repro | `order_bug.py` | bug | `df_clean` used before it is defined |
| repro | `version_extend.py` | extend | print Python, Polars, Altair versions |

## Files Modified (11 chapter index files)

`llm/index.md`, `chart/index.md`, `clean/index.md`, `summarize/index.md`,
`tables/index.md`, `prompts/index.md`, `change/index.md`, `join/index.md`,
`stories/index.md`, `validate/index.md`, `repro/index.md`
