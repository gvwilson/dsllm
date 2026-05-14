# Checking Your Work

## Goals

-   Verify LLM output by checking it against known values and common sense.
-   Interpret a hypothesis test result without misreading it as certainty.
-   Recognize that a confident-sounding LLM answer is not a correct answer.

## The Unit Error

> What happens when the LLM silently uses the wrong units?

-   The dataset for this session comes from
    the Canada Energy Regulator and Natural Resources Canada [%b cer2025 %]
    -   Download two tables from [Canada Energy Regulator][cer]:
        -   Provincial natural gas production reported in thousands of cubic metres (10³ m³)
        -   Provincial natural gas consumption reported in millions of cubic metres (10⁶ m³)
    -   Both tables cover the same years and provinces but use different prefixes
-   When you ask the LLM to compare production to consumption, it reads both columns and divides them
    -   The code runs without error and returns a number
    -   That number is off by a factor of 1 000, because 1 million m³ = 1 000 thousand m³
    -   Nothing in the code signals that anything is wrong

[%inc unit_error.py %]

-   Run the cell and look at the ratio
    -   Alberta produces far more gas than it consumes:
        a ratio well above 1 for a major exporting province is plausible
    -   If the ratio is in the hundreds or in the thousandths, there is a unit error

## Checking Without Reading Code

> What strategies let me catch this error without reading the code?

-   Check a single known value by hand
    -   The Canada Energy Regulator publishes summary statistics; find Alberta's production for one recent year
    -   If the CER says Alberta produced approximately 163 billion m³ in 2022, and your file shows 163 000 for that row, the column is in millions of m³ (163 000 × 10⁶ = 163 × 10⁹ m³)
    -   Confirm the units before computing any ratio
-   Ask the LLM what units it assumed
    -   Paste the code into a new prompt: "What units did you assume for each column in this code?"
    -   A well-functioning LLM will identify the unit columns; a poorly-prompted one will guess
-   Compare to a published figure
    -   If your computed ratio is 1 000 or 0.001, the units do not match

## The Correct Comparison

> Fix the code so both columns use the same unit before comparing.

or

> The production column is in 10³ m³ (thousands of cubic metres)
> and the consumption column is in 10⁶ m³ (millions of cubic metres).
> Convert the production column to 10⁶ m³ by dividing by 1000 before computing the ratio.

-   The LLM will produce something like:

[%inc unit_fix.py %]

-   Run the cell and check: does the result match the by-hand estimate from the previous section?

## Running a Hypothesis Test

> Run a t-test to check whether natural gas production differs significantly
> between Alberta and British Columbia.

or

> Using Polars and scipy.stats, read gas_production.csv,
> extract the production values for Alberta and BC, and run a Welch's t-test.
> Print the t-statistic and the p-value.

-   The LLM will produce something like:

[%inc ttest.py %]

-   Run the cell and look at the p-value

## What a P-Value Means

> What does it actually mean when the p-value is 0.003?

-   A [%g p-value "p-value" %] is the probability of seeing a difference at least this large if there were truly no difference between the two groups
    -   p = 0.003 means that if Alberta and BC truly had identical production levels,
         only 0.3% of random samples would show a difference this large or larger
    -   It does not mean "there is a 99.7% chance the difference is real"
-   Rejecting the [%g null-hypothesis "null hypothesis" %] (the assumption of no difference) at p < 0.05
     means "this result is surprising enough that we should take it seriously"
    -   It does not mean the difference is large enough to matter practically
    -   It does not mean the measurement was correct
-   A unit error that inflates one column by 1 000× will produce a very significant p-value
    -   The difference is real, but you measured the wrong thing

## When Significance Misleads

> Why can a statistically significant result be meaningless?

-   Statistical significance tells you the signal is large relative to the noise in your sample
    -   It says nothing about whether you measured the right quantity
    -   A perfectly measured wrong quantity can be highly significant
-   The unit error in this session is an example
    -   After the error, production appears 1 000 times larger relative to consumption than it should
    -   That difference is highly statistically significant, and entirely artifactual
-   Before interpreting a significant p-value, confirm the inputs are correct
    -   Do the units match? Do the columns contain what you think they contain?
    -   Has someone checked a known row by hand?

## Check Understanding

<details markdown="1">
<summary markdown="1">The LLM produces a production-to-consumption ratio of 0.001 for Alberta. You expected a value around 5 (Alberta exports far more than it consumes). What unit conversion did the LLM get backwards, and what is the correct ratio?</summary>

The LLM divided thousands of m³ of production by millions of m³ of consumption without converting.
1 million m³ = 1000 thousand m³, so consumption in millions
is 1000 times larger than the same value in thousands.
To get the correct ratio,
first convert production from 10³ m³ to 10⁶ m³ by dividing by 1000,
then divide production by consumption.
If Alberta produced roughly 163 000 in 10³ m³ units (163 million m³) and consumed 20 million m³,
the correct ratio is approximately 8.

</details>

<details markdown="1">
<summary markdown="1">A t-test returns p = 0.0004. A classmate says "this proves Alberta and BC have different production levels." Correct their interpretation in one or two sentences.</summary>

p = 0.0004 means that if Alberta and BC truly had identical production levels,
only 0.04% of random samples would show a difference this large.
It does not prove they are different.
It says the observed difference is very unlikely under the null hypothesis,
and it says nothing about whether the units were correct
or whether the difference is large enough to be practically meaningful.

</details>

<details markdown="1">
<summary markdown="1">You check a single row by hand and find the LLM's computed ratio for 2020 is 0.0081, but your manual calculation gives 8.1. List the steps you would take before re-running the analysis.</summary>

First, confirm your manual calculation by re-deriving the 2020 values from the published CER tables
and recomputing the ratio.
Second, ask the LLM which columns it used and what units it assumed for each.
Third, check whether the code reads the correct rows for 2020,
as there may be summary rows or header rows the LLM included.
Fourth, re-run the corrected code on only the 2020 row
to confirm the output matches your manual result before running on the full dataset.

</details>

<details markdown="1">
<summary markdown="1">After fixing the unit error, you re-run the t-test comparing Alberta and BC production and get p = 0.21. The original (incorrect) analysis gave p < 0.001. What does this change tell you?</summary>

The original highly significant result was driven entirely by the unit error,
which made BC and Alberta production appear 1000 times more different than they actually are.
After correcting the units,
the actual year-to-year variation in production within each province is large enough that
the difference between provinces is not statistically distinguishable from chance.
This shows why significance alone is not enough:
the first analysis produced a convincingly significant result that was measuring the wrong thing.

</details>

## Exercises

### Three-Province Comparison

Add Saskatchewan to the comparison.
Ask the LLM to compute mean natural gas production for Alberta, BC, and Saskatchewan in the same unit.
Verify your result against a published CER summary table.

### Ask About Assumptions

Take any code from an earlier session and paste it into a new prompt:
"What assumptions did you make about the data types and units of each column?"
Compare the LLM's answer to the actual column types in the data.

### Sensitivity Analysis

For the Alberta vs. BC comparison, vary the significance threshold from 0.01 to 0.10 in steps of 0.01.
At which threshold does the corrected analysis first become significant?
What does this tell you about using a single fixed threshold?

### Find the Published Figure

The CER publishes annual energy market reports.
Find their stated value for Alberta natural gas production in the most recent year
and compare it to your computed total.
Do they match?
