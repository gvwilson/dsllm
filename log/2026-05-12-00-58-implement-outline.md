# 2026-05-12 00:58 — Implement Outline

## Prompts

1.  Start a new log file.
2.  Read `outline.txt`.
3.  Read Markdown files in `~/webllm/*/*.md` and log files in `~/webllm/log/*` to understand prior work.
4.  Implement the outline, following the style of `~/webllm` material.

## Actions

-   Read `outline.txt` (12 sessions + intro + finale + appendices).
-   Read `~/webllm/htmlcss/index.md` and `~/webllm/forms/index.md` for style reference.
-   Read `~/webllm/log/2026-05-10-12-28-create-htmlcss-lesson.md` for log format.
-   Read existing `README.md`, `glossary/index.md`, `bibliography/index.md` (all stubs).
-   Updated `README.md` to list all 13 lessons (intro through finale) plus 5 appendices.
-   Created `_extras/links.md` with external link definitions for all datasets.
-   Updated `glossary/index.md` with 20 terms covering all new concepts in the course.
-   Updated `bibliography/index.md` with 18 references (datasets, tools, methodology papers).
-   Updated `intro/index.md`: Goals, What Is Data Science, What LLMs Do, The Costs of LLMs,
    What This Course Does Not Do, Check Understanding (4 questions), Exercises (3).
-   Updated `finale/index.md`: Goals, The Workflow You Built, When LLMs Fail,
    The Environmental and Labor Costs, Where to Go Next, Check Understanding (4 questions), Exercises (3).
-   Created `llm/index.md` (Session 2: First Steps, GISTEMP data, mean and median).
-   Created `llm/read_temps.py`, `llm/mean_median.py`.
-   Created `chart/index.md` (Session 3: First Charts, Exoplanet Archive, correlation).
-   Created `chart/scatter.py`, `chart/count_rows.py`, `chart/correlation.py`.
-   Created `clean/index.md` (Session 4: Cleaning, Diabetes 130-US Hospitals, sampling bias).
-   Created `clean/find_missing.py`, `clean/check_gender.py`, `clean/normalize.py`.
-   Created `summarize/index.md` (Session 5: Summarizing, Chicago budget, confidence intervals).
-   Created `summarize/group_spend.py`, `summarize/add_ci.py`.
-   Created `tables/index.md` (Session 6: Tables, Breeding Bird Survey, standard deviation).
-   Created `tables/describe_birds.py`, `tables/spread_birds.py`.
-   Created `prompts/index.md` (Session 7: Better Prompts, USGS geochemistry, probability).
-   Created `prompts/vague_prompt.py`, `prompts/show_sample.py`, `prompts/lead_prop.py`, `prompts/verify.py`.
-   Created `change/index.md` (Session 8: Tracking Change, CDC FluView, regression).
-   Created `change/flu_line.py`, `change/flu_trend.py`, `change/check_slope.py`.
-   Created `join/index.md` (Session 9: Joining Data, NOAA GHCN-D, comparing groups).
-   Created `join/load_both.py`, `join/join_climate.py`, `join/check_join.py`,
    `join/mean_by_zone.py`, `join/row_counts.py`.
-   Created `stories/index.md` (Session 10: Telling Stories, Student Performance, correlation vs. causation).
-   Created `stories/grade_charts.py`, `stories/grade_charts_fixed.py`, `stories/validate_panels.py`.
-   Created `validate/index.md` (Session 11: Checking Your Work, EIA energy data, hypothesis testing).
-   Created `validate/unit_error.py`, `validate/unit_fix.py`, `validate/ttest.py`.
-   Created `repro/index.md` (Session 12: Reproducibility, NOAA Mauna Loa CO2, replication crisis).
-   Created `repro/versions.py`, `repro/keeling.py`, `repro/rerun_check.py`.
