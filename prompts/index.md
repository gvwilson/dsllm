# Better Prompts

## Goals

-   Identify what information an LLM needs to write useful data-science code.
-   Write prompts that include data shape, goal, and constraints.
-   Interpret a probability as a proportion and connect it to observed counts.

## Why Vague Prompts Fail

*What goes wrong when I give an LLM a vague prompt?*

-   The dataset for this session is the Environment and Climate Change Canada National Pollutant Release Inventory (NPRI) [%b npri2025 %]
    -   Download the most recent annual CSV from [NPRI][npri]
    -   It has one row per facility per substance reported, with columns for facility name, province, substance name (in English and French), the quantity released, and the units
    -   Under Canadian law, facilities that release more than threshold quantities of listed substances must report them here
-   Consider the vague prompt: "How many facilities released dangerous amounts of lead?"
    -   The LLM does not know the column name for substance, so it invents one
    -   It does not know the threshold or the substance name as it appears in the file, so it guesses
    -   The code may run without error and be entirely wrong

[%inc vague_prompt.py %]

-   This code may crash (`KeyError: 'substance'`) or silently return the wrong answer (if the LLM guessed a column name that happens to exist but refers to something else)

## Anatomy of a Good Prompt

*What information does a prompt need to include to get useful code?*

-   A useful prompt has three parts: a description of the data, the goal, and any constraints
    -   Data description: column names, data types, and a sample row
    -   Goal: exactly what you want to compute or display
    -   Constraints: the exact substance name as it appears in the file, the threshold, the units
-   To give the LLM column names and a sample row, print them first:

[%inc show_sample.py %]

-   Then include that output in your prompt: "The data has columns NPRI_ID, Facility_Name, Province_Territory, Substance_Name_English, Total_Released_Tonnes. One row looks like: {row}. Using Polars, find the proportion of facilities that released more than 1 tonne of 'Lead (and its compounds)' in the most recent year."
    -   Now the LLM knows the exact column names, the exact substance string, and the threshold
    -   This is the difference between a guess and a grounded answer

## Computing a Proportion

*What proportion of facilities released more than one tonne of lead compounds in the most recent year?*

-   Paste the well-structured prompt from above
-   The LLM will produce something like:

[%inc lead_prop.py %]

-   Read through the code before running it
    -   `LEAD_THRESHOLD = 1.0` is a named constant (good)
    -   `LEAD_SUBSTANCE` names the exact string from the file: this will only work if it matches the CSV exactly
    -   The final print statement shows the proportion and its 1-in-N equivalent:
	    check that both numbers are consistent

## Probability as a Proportion

*What does it mean to say the probability of exceeding the threshold is 0.059?*

-   A [%g probability "probability" %] between 0 and 1 is a proportion
    -   0.059 means about 59 out of 1 000 facilities (or roughly 1 in 17)
    -   0 means it never happened in this sample; 1 means it always occurred
    -   It is a description of this dataset, not a guarantee about any individual facility
-   Probability is estimated from counts: if 47 of 800 facilities exceed the threshold, the estimated probability is 0.059
    -   A larger sample gives a more reliable estimate
    -   Facilities from one province may not represent the national picture

## Verifying by Hand

*How do I check that the code produced the right answer?*

-   For a proportion, the verification is simple: count a small subset by hand
    -   Sort the lead rows by quantity descending; check how many of the first 20 exceed 1 tonne
    -   Multiply that fraction by the total facility count and compare to the code's output

[%inc verify.py %]

-   Look at the output and count the rows above 1 tonne yourself
    -   If the code says 4 out of 20 and you count 4, the proportion calculation is probably correct
    -   If you count 3 and the code says 4, find which row the code counted that you did not

## Check Understanding

<details markdown="1">
<summary markdown="1">You paste the prompt: "Compute the average lead released." The LLM produces code that reads `df["lead_tonnes"].mean()` but your column is named `Total_Released_Tonnes`. The code crashes. Rewrite the prompt so this error cannot happen.</summary>

Include the exact column names and a sample row: "The dataset has columns NPRI_ID, Facility_Name, Province_Territory, Substance_Name_English, Total_Released_Tonnes. Using Polars, filter to rows where Substance_Name_English is 'Lead (and its compounds)' and compute the mean of Total_Released_Tonnes, excluding nulls."
With the exact column name in the prompt, the LLM cannot invent an alternative.

</details>

<details markdown="1">
<summary markdown="1">The code filters to `Substance_Name_English == "Lead (and its compounds)"` and returns 0 rows. You can see lead entries in the first few rows of the file. What are two likely causes?</summary>

First, the substance name in the file might use different capitalisation or punctuation
(for example, "Lead and its compounds" without parentheses, or "lead (and its compounds)" in lowercase).
Print `df["Substance_Name_English"].unique()` and search for rows containing "Lead" to find the exact string.
Second, the filter may be applied before the year filter, so the correct rows exist in the full data but are excluded by an earlier step.
Print the dataframe at each step to find where the rows disappear.

</details>

<details markdown="1">
<summary markdown="1">The code returns a proportion of 0.031. You check the first 20 lead-reporting rows and find 2 above 1 tonne. Is the code consistent with your check? Show your reasoning.</summary>

2 out of 20 is 0.10, which is much higher than 0.031.
This discrepancy is suspicious.
Possible causes: the first 20 rows may be sorted by quantity descending, so they overrepresent high-release facilities; the LLM may have filtered to a different set of rows for the proportion than for the sample; or the denominator may be different (perhaps it counted all facilities, not just lead-reporting ones).
Expand the hand-check to a random sample of rows rather than the first 20.

</details>

<details markdown="1">
<summary markdown="1">A report says "6% of facilities reporting to NPRI released more than 1 tonne of lead compounds." Someone reads this and says "my city's factory has a 6% chance of being a lead emitter." What is wrong with this interpretation?</summary>

The 6% is a proportion across all NPRI-reporting facilities, which are a specific, non-random group
(facilities large enough to meet reporting thresholds).
A factory that does not meet any NPRI reporting threshold is not in the denominator at all.
The proportion from a non-random, self-selected reporting group cannot be applied as a probability to a specific facility that may or may not be in the group.

</details>

## Exercises

### Provincial Breakdown

Ask the LLM to compute the proportion of facilities exceeding 1 tonne separately for each province.
Which provinces have the highest proportions?
Is there a pattern you would expect given Canada's industrial geography?

### Multiple Substances

The NPRI tracks many pollutants.
Ask the LLM to compute the proportion of facilities exceeding reporting thresholds for mercury (Hg, threshold 5 kg) and arsenic (As, threshold 1 tonne) in addition to lead.
Compare the three proportions.

### Trend Over Time

Ask the LLM to compute the proportion of facilities reporting lead releases above 1 tonne for each year in the dataset.
Has the proportion changed over time?

### Re-prompt After Failure

Give the LLM the vague prompt "How many facilities released dangerous amounts of lead?" and record what it produces.
Then give it the well-structured prompt from this session and compare the two results.
Write one sentence describing what changed between the two outputs.
