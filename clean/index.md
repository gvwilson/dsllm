# Cleaning

## Goals

-   Prompt an LLM to find missing values and inconsistent categories.
-   Prompt an LLM to find missing values and inconsistent categories.
-   Interpret before-and-after output to confirm cleaning worked.
-   Explain how missing data can make a sample unrepresentative.

## Why Real Data Is Dirty

> What kinds of problems appear in real datasets, and why?

-   Real datasets almost always have problems that need fixing before analysis:
    -   [%g missing-value "Missing values" %] recorded as `U` (unknown),
        `Q` (not applicable), blank cells, or special codes like `-99`
    -   The same category recorded with different codes in different years as forms change
    -   Duplicate records from merging data from multiple sources or systems
    -   Columns where the meaning of a code changed between reporting periods
-   These problems arise because data is collected by different agencies at different times using different tools
    -   A traffic collision form may have been redesigned several times over decades
    -   Merging records from ten provincial systems produces ten different conventions in one table
-   The dataset for this session is the Transport Canada National Collision Database (NCDB) [%b ncdb2025 %]
    -   Download `collision_data.csv` from [Transport Canada NCDB][ncdb]
    -   It contains individual motor vehicle collision records going back decades,
        with columns for year, province, road conditions, and person characteristics

## Finding Missing Values

> Show me how many missing or unknown values each column has.

or

> Using Polars, read collision_data.csv, treat U, Q, and N as missing values,
> then print a table showing each column name and how many missing values it has,
> sorted from most to fewest.

-   The NCDB uses coded values: `U` means unknown, `Q` means not applicable, `N` means not stated
    -   None of these are the same as a number: they mean "we do not know this value"
    -   Polars reads them as strings, not as nulls, unless you tell it otherwise
-   The LLM will produce something like:

[%inc find_missing.py %]

-   Run the cell and look at the output
    -   Some columns may have missing values in the majority of rows
    -   Columns like `C_WTHR` (weather condition) are often missing when conditions were not recorded at the scene

## Checking Category Values

> Show me every distinct value in the sex column.

or:

> Using Polars, read collision_data.csv with U, Q, and N as missing,
> then print every distinct value in the P_SEX column and how many times each appears.

-   The LLM will produce something like:

[%inc check_sex.py %]

-   The output should show `M`, `F`, and possibly `U` or blank
    if some rows were not caught by the null-value argument
    -   `M` = male, `F` = female, `U` = unknown sex
    -   Unknown sex is not the same as a missing value:
        the record exists, but the person's sex was not recorded at the scene

## Normalizing Values

> Treat U and N as missing so only M and F remain in the sex column.

or:

> Using Polars, read collision_data.csv with U, Q, and N as missing.
> Print the distinct values and counts in P_SEX after cleaning.
> Print the total number of rows before and after dropping rows where P_SEX is null.

-   The LLM will produce something like:

[%inc normalize.py %]

-   Run the cell and check:
    -   Only `M` and `F` appear in the cleaned column
    -   The row count after dropping null sex is smaller than before
    -   Spot-check: find one row that had `U` and confirm it is now null or gone

## Understanding Sampling Bias

> If collision records in remote areas are under-reported, what does that mean for our analysis?

-   [%g sampling-bias "Sampling bias" %] occurs when the data we have
    is not a fair sample of the population we are studying
    -   In Canada, minor collisions on remote roads may not be reported to police or to Transport Canada
    -   If remote collisions are missing from the database,
        any analysis of "where roads are most dangerous" underestimates rural risk
    -   The LLM has no way to warn you about this: it only knows the data you give it
-   One way to check for bias is to compare what was recorded against what you know about the population

> Show me the distribution of P_PROV (province) in the data. Is it proportional to provincial population?

-   If a province is severely under-represented, its collision records may be less complete

> Why can an LLM not fix sampling bias for you?

-   The LLM can clean the coded values as instructed, but it cannot know what collisions were never recorded
    -   Knowing whether the bias matters requires understanding your research question and data collection process
    -   Every cleaning decision is also a research decision: dropping rows,
        treating codes as missing,
        or pooling categories all change the population you are studying

## Check Understanding

<details markdown="1">
<summary markdown="1">After treating U as missing in the P_SEX column, a classmate removes all rows where sex is null to get a "clean" dataset. What assumption are they making, and when is that assumption wrong?</summary>

They are assuming that rows with unknown sex are missing at random,
i.e., that collisions where sex was not recorded are otherwise the same as collisions where it was.
If sex is less likely to be recorded for pedestrians, cyclists,
or collisions involving multiple vehicles, dropping those rows changes the composition of the dataset.
The cleaned sample no longer represents the same population as the full collision database.

</details>

<details markdown="1">
<summary markdown="1">You run the missing-value check and find that the C_WTHR (weather condition) column is 40% missing. The LLM suggests filling in the missing values with "Clear" since that is the most common value. What is wrong with this approach?</summary>

Filling in 40% of a column with the most common value assumes that weather condition was missing randomly
and that most missing records happened on clear days.
Neither assumption is justified.
Collisions in bad weather may be more likely to have incomplete police reports
if responding officers were busy managing the scene.
Filling missing weather values with "Clear" would make conditions appear better than they were
for a large fraction of the data,
biasing any analysis of weather effects on collision rates.

</details>

<details markdown="1">
<summary markdown="1">The LLM produces code that reads null_values=["U", "Q", "N"]. You run it and then print the distinct values of P_SEX. You still see "U" in the output. What likely went wrong?</summary>

Polars requires null_values to match the exact string in the file,
including any surrounding whitespace.
If the file stores " U" (with a leading space) rather than "U",
the match fails and the value is left as a string.
Print `df["P_SEX"].unique()` and look carefully at the values:
use `df["P_SEX"].str.strip().unique()` to reveal hidden spaces.
Then either add the padded version to null_values or strip the column before checking.

</details>

<details markdown="1">
<summary markdown="1">You want to compare collision rates per 100 000 people between provinces. After cleaning, Alberta has 80 000 records and Prince Edward Island has 2 000. Should you compare raw counts or rates? Why?</summary>

Compare rates (collisions per 100 000 people), not raw counts.
Alberta has roughly 25 times the population of PEI,
so more collisions are expected regardless of road safety differences.
Dividing by population puts the provinces on a comparable scale.
The raw counts differ because the populations differ,
not necessarily because one province has more dangerous roads.

</details>

## Exercises

### Weather Conditions

Print the distinct values and counts for the `C_WTHR` (weather condition) column
before and after treating unknown codes as missing.
What proportion of collision records have known weather conditions?

### Road Surface

The `C_RSUR` column codes the road surface condition (dry, wet, snow/ice, etc.).
Ask the LLM to show the proportion of collisions for each road condition.
Does icy or snowy road surface correspond to a higher proportion of fatal collisions (P_INJ = 1)?

### Before and After

Ask the LLM to compute the percentage of collisions
that resulted in at least one fatality (P_INJ = 1)
before and after dropping rows where P_SEX is unknown.
Does the fatality rate change? What does that tell you?

### Provincial Distribution

Ask the LLM to count how many records come from each province (C_PROV).
Compare the provincial shares to the 2021 census population shares.
Which provinces appear over- or under-represented in the collision database?

### Incomplete Null List

The following code reads the collision data and reports missing-value counts,
but the number of null values is much lower than expected:
the NCDB uses `U`, `Q`, and `N` as missing codes, but not all are declared.
Work with an LLM to find what is missing and fix the `null_values` argument.

[%inc null_partial.py %]

<details markdown="1">
<summary markdown="1">How do you know the fix worked?</summary>

After fixing, the distinct values printed for `C_WTHR` should contain only numeric codes,
not the letters `Q` or `N`.
Re-run the missing-value count and confirm it is higher than before.

</details>

### Hidden Whitespace in Categories

The following code counts province values, but prints more distinct provinces than Canada has.
Work with an LLM to identify what is causing the extra groups and fix the code.

[%inc strip_bug.py %]

<details markdown="1">
<summary markdown="1">How do you know the fix worked?</summary>

Canada has 13 provinces and territories.
After fixing, the number of distinct `C_PROV` values should be 13 or fewer.
Print the unique values and confirm none look like duplicates with extra spaces.

</details>

### Dropping Too Many Rows

The following code removes rows with unknown sex, but the row count after cleaning is far smaller than expected.
Work with an LLM to explain why so many rows were dropped and rewrite the cleaning step.

[%inc drop_bug.py %]

<details markdown="1">
<summary markdown="1">How do you know the fix worked?</summary>

The correctly cleaned dataset should only lose the rows where `P_SEX` is null,
not rows where any other column is null.
Compare the before and after row counts to the count from `normalize.py` to verify.

</details>

### Raw Counts vs. Rates

The following code prints the number of collision records per province,
but raw counts are misleading because provinces have very different populations.
Work with an LLM to add a column showing collisions per 100,000 people
using 2021 census population figures.

[%inc rate_extend.py %]

<details markdown="1">
<summary markdown="1">How do you know the addition is correct?</summary>

Compute one rate by hand for a province whose population you know,
and confirm it matches the new column.
Re-sort by rate: if the ordering changes significantly compared to raw counts,
the rates are doing their job.

</details>
