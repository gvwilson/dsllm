# Summarizing

## Goals

-   Prompt an LLM to group data and compute aggregations.
-   Interpret a confidence interval as a measure of how certain an estimate is.
-   Sanity-check a summary against a known published figure.

## What "Group By" Means

> What does it mean to group data, and what kinds of questions does it answer?

-   A "group by" operation splits a table into groups that share a common value, computes something for each group, and returns one row per group
    -   "Total contract value per department per year" requires grouping by department and year, then summing
    -   "Mean contract size by vendor" requires grouping by vendor, then averaging
    -   Without grouping, you get one number for the whole table; with it, you get one number per category
-   The dataset for this session is the Government of Canada Proactive Disclosure of Contracts from the Open Government portal [%b gc-contracts2025 %]
    -   Download `contracts.csv` from [Open Government][open-canada]
    -   It has one row per contract awarded with columns for department, vendor name, contract value, and award date
    -   Every federal department with contracts over $10 000 must disclose them here

> Why would you want both the total and the mean for the same group?

-   The total tells you how much a department spent overall; the mean tells you how large a typical contract was
    -   A department that awards one large infrastructure contract looks different from one that awards thousands of small consulting contracts, even if the totals are similar
    -   Both numbers together give a more complete picture

## Computing Totals and Means

> Show me total and mean contract value by department for each year, sorted by department name.

or

> Using Polars, read contracts.csv. Extract the year from the contract_date column. Compute the total and mean contract_value by department_en and year. Sort by department name, then year. Print the first twenty rows.

-   The LLM will produce something like:

[%inc group_spend.py %]

-   Run the cell and scan the output
    -   Check that the department names look like real Government of Canada departments
    -   Check that the totals are in a plausible range (millions of dollars for large departments)
    -   If the totals look like individual salaries rather than department budgets, the LLM may have misread the column

## Adding Confidence Intervals

> Add a 95% confidence interval to each group mean.

or

> Extend the previous code to also compute a 95% confidence interval for the mean contract value in each department-year group. Add columns ci_low and ci_high to the output.

-   The LLM will produce something like:

[%inc add_ci.py %]

-   The `ci_low` and `ci_high` columns bracket the mean
    -   For departments with only a few contracts, the interval is wide: there is not enough data to be precise
    -   For departments with hundreds of contracts, the interval is narrow: the mean is well-estimated

## Reading a Confidence Interval

> What does a 95% confidence interval actually mean?

-   A 95% [%g confidence-interval "confidence interval" %] does not mean "there is a 95% chance the true mean is in this range"
    -   It means: if we built many such intervals from different samples, 95% of them would contain the true mean
    -   The statement is about the method, not about this one interval
-   In plain language: a narrow interval means the estimate is precise; a wide interval means more data is needed
    -   "Department A awarded contracts with a mean value of $420K ± $15K" is a precise claim
    -   "Department B awarded contracts with a mean value of $1.2M ± $900K" is too uncertain to act on
-   When two departments' confidence intervals do not overlap, their typical contract sizes are probably genuinely different
    -   When they do overlap, the data cannot distinguish them

## Checking Against a Published Figure

> The government publishes the total value of contracts. Let us compare our sum to that published number.

or

> Compute the total contract_value across all departments for the most recent year in the dataset.

-   Find the government's published total in the Public Accounts of Canada at [Open Government][open-canada]
    -   The published total should be in the same order of magnitude as your computed sum
    -   If your number is off by a factor of ten or more, the LLM probably misread the units or missed some rows
-   Proactive disclosure covers contracts over $10 000; very small contracts are not included, so your total will be lower than the overall procurement total

## Check Understanding

<details markdown="1">
<summary markdown="1">You compute a 95% confidence interval of ($480K, $620K) for mean contract size in one department. A classmate says "there is a 95% chance the true mean is between $480K and $620K." What is wrong with this statement?</summary>

The true mean is a fixed value: it either is or is not in the interval, with probability 1 or 0.
The 95% refers to the procedure: if you built many intervals from different samples, 95% of them would contain the true mean.
This particular interval either contains the true mean or does not; we just do not know which.

</details>

<details markdown="1">
<summary markdown="1">Two departments have mean contract values of $350K and $510K, with 95% confidence intervals of ($280K, $420K) and ($450K, $570K). Do the intervals overlap? What can you conclude?</summary>

The intervals do not overlap: the first ends at $420K and the second starts at $450K.
This suggests the difference is real: large-sample departments with non-overlapping intervals are probably genuinely different in typical contract size.
A formal hypothesis test would confirm this more rigorously, but non-overlapping intervals are good evidence that the departments procure at different scales.

</details>

<details markdown="1">
<summary markdown="1">Your computed total for one department is $2.8 billion, but the Public Accounts show $1.4 billion. List two things you would check before concluding the data is wrong.</summary>

First, check whether the years match:
the dataset might include a different fiscal year than the Public Accounts reference,
or might include amendments and modifications not in the original totals.
Second, check whether the LLM summed all rows or only a subset:
it may have failed to filter by department correctly and included other departments.
Ask the LLM to print the number of rows it summed and the range of years included.

</details>

<details markdown="1">
<summary markdown="1">A department has only two contracts in one year, with values of $15K and $4.8M. The confidence interval for the mean is ($-3.2M, $8.0M). What does this tell you?</summary>

The interval is enormous and includes negative values, which is meaningless for a contract value.
Two observations are nowhere near enough to estimate a mean reliably.
This department-year combination should either be excluded from comparisons or clearly flagged as having too few observations to interpret.

</details>

## Exercises

### Largest Vendors

Find the five vendors with the highest total contract value across all departments and years.
Are any surprising?

### Year-Over-Year Change

For one department of your choice, compute the total contract value for each year in the dataset.
Ask the LLM to compute the percentage change from one year to the next.
Plot the result as a bar chart.

### Wide Intervals

Find all department-year combinations where the 95% confidence interval for the mean is wider than $500 000.
What do those groups have in common?

### Plot the Intervals

Ask the LLM to create a chart showing the mean contract value and 95% confidence interval for each department in the most recent year.
Sort the departments from highest to lowest mean.

### Sum Before Group

The following code is meant to compute the mean contract value per department per year,
but the output has only one row instead of one row per department.
Work with an LLM to explain what went wrong and fix the pipeline.

[%inc order_bug.py %]

<details markdown="1">
<summary markdown="1">How do you know the fix worked?</summary>

The corrected output should have one row per unique combination of department and year.
Count the distinct department names in the result and compare to the number of departments
in the original file.

</details>

### Month Instead of Year

The following code groups contracts by year, but the `year` column in the output
contains values between 1 and 12 instead of four-digit years.
Work with an LLM to find the error and fix it.

[%inc year_bug.py %]

<details markdown="1">
<summary markdown="1">How do you know the fix worked?</summary>

Print the distinct values in the `year` column of the summary.
They should be four-digit years matching the range of dates in `contracts.csv`.

</details>

### Flag Unreliable Intervals

The following code computes 95% confidence intervals for the mean contract value per department per year.
Work with an LLM to extend it so it also adds a column `ci_reliable`
that is `True` when the group has five or more contracts and `False` otherwise,
then prints only the unreliable rows.

[%inc small_n_extend.py %]

<details markdown="1">
<summary markdown="1">How do you know the addition is correct?</summary>

Find one department-year group with a very small `n` in the output of `add_ci.py`
and confirm it appears in the `ci_reliable == False` rows.
Also check that no group with `n >= 5` appears there.

</details>

### Wrong Grouping Column

The following code is meant to find the top 10 vendors by total contract value,
but the output shows department names instead of vendor names.
Work with an LLM to identify the wrong column and fix it.

[%inc vendor_bug.py %]

<details markdown="1">
<summary markdown="1">How do you know the fix worked?</summary>

The output should contain company and supplier names, not the names of government departments.
Spot-check one of the top vendors by searching for their name in the contracts CSV
and summing their rows by hand.

</details>
