# Joining Data

## Goals

-   Explain what a join does and when it is needed.
-   Prompt an LLM to join two dataframes and interpret the result.
-   Compare summary statistics across groups created by the join.

## Why Data Arrives in Pieces

> Why would data about the same topic be stored in two separate files?

-   Different teams collect different parts of the picture
    -   Temperature readings are collected continuously at each station;
        station locations and elevations are recorded once when the station is established
    -   Storing location data in every temperature row wastes space and creates inconsistency:
        if a station is relocated, you update one row in the station file instead of decades of readings
-   The dataset for this session is the Environment and Climate Change Canada
    Adjusted and Homogenized Canadian Climate Data (AHCCD) [%b ahccd2025 %]
    -   Download both files from [AHCCD][ahccd]:
        the annual temperature series (`ahccd_temp.csv`) and the station inventory (`ahccd_stations.csv`)
    -   The temperature file has one row per station per year with the mean annual temperature
    -   The station file has one row per station with name, province, latitude, longitude, and elevation

> What is a join?

-   A [%g join "join" %] combines two tables by matching rows that share a common value
    -   If both tables have a `station_id` column,
        a join finds every temperature row and attaches the matching station row to it
    -   The result is one wide row per temperature record,
        with both the temperature and the station's province in the same row
-   Without the join, you cannot answer "what is the mean annual temperature by province?"
    -   Province is only in the station file; temperature is only in the readings file
    -   The join is what makes the question answerable

## Joining the Tables

> Combine the temperature dataframe and the stations dataframe so each temperature row also shows the station's province and elevation.

or

> Using Polars, read ahccd_temp.csv and ahccd_stations.csv. Join them so each temperature row gains the matching station's province and elevation columns. Use a left join on the station_id column. Print the first five rows of the result.

-   Read both files first and print their column names so you know which column to join on:

[%inc load_both.py %]

-   The LLM will produce something like:

[%inc join_climate.py %]

-   Run the cell and check the output
    -   Do the column names match what `load_both.py` showed?
    -   Does each row have both a temperature value and a province?

## Checking the Join Result

> How do I know the join worked correctly?

-   A left join keeps every row from the left table (temperatures) and adds matching columns from the right (stations)
    -   If a station ID appears in temperatures but not in stations, its province and elevation will be null
    -   Many nulls after the join mean the station IDs do not match between files
    -   This is a common problem when data is compiled from different sources
-   Check how many rows have null province after the join:

[%inc check_join.py %]

-   If the null count is zero, every temperature record matched a station: the join is complete
    -   If the null count is large, inspect a few unmatched IDs and compare them to the station file format

## Comparing Groups

> Show me the mean annual temperature by province.

or

> Using the joined dataframe, compute the mean annual temperature for each province. Sort from warmest to coolest. Drop rows where temperature or province is null.

-   The LLM will produce something like:

[%inc mean_by_province.py %]

-   Run the cell
    -   Does the ordering match your expectations? (BC coast warmest, Prairie provinces cold winters, North coldest)
    -   This question was only answerable after the join; the temperature file alone has no province column

> What does it mean when two provinces have different mean temperatures?

-   A difference in group means tells you the groups are different in this dataset, not that province determines temperature
    -   Provincial boundaries do not align with climate zones: northern Ontario has a colder climate than southern Ontario
    -   Provinces with more stations in the north will appear colder than their geography suggests
    -   The join adds information; it does not settle which factor drives the difference

## Counting Rows Before and After

> How do I detect if the join accidentally multiplied my rows?

-   A left join multiplies rows when one station ID appears multiple times in the station file
    -   If station XYZ has two entries (perhaps renamed or relocated), every temperature reading for XYZ will appear twice in the result

[%inc row_counts.py %]

-   If `after` is larger than `before`, the join multiplied rows
    -   Find the duplicated station IDs and decide which record is correct before re-running the join

## Check Understanding

<details markdown="1">
<summary markdown="1">After a left join, the province column has 3 500 null values where it had zero before. The temperature file has 200 000 rows. What is the most likely cause, and how would you find out?</summary>

The most likely cause is that some station IDs in the temperature file do not appear in the station inventory.
They may use a different format (with or without leading zeros, with or without a country prefix).
To diagnose: find the distinct station_id values in temperature rows where province is null, and check whether any of those IDs appear in the station file in a slightly different format.
If they match after stripping a prefix, ask the LLM to normalize the IDs before joining.

</details>

<details markdown="1">
<summary markdown="1">The joined dataframe has 210 000 rows but the temperature file has only 200 000. A classmate says "the join added information so more rows is expected." Are they right?</summary>

No.
A left join cannot add rows: every row in the result corresponds to exactly one row in the left table.
Having more rows after the join means the station inventory has duplicate entries for some station IDs.
Each temperature reading for a duplicated station matched multiple station rows and was replicated.
Find duplicated station IDs with `stations.group_by("station_id").count().filter(pl.col("count") > 1)`.

</details>

<details markdown="1">
<summary markdown="1">You find that Alberta has a mean annual temperature of 2.1 °C and Prince Edward Island has 6.8 °C. A classmate says "this proves maritime provinces are warmer than prairie ones." What is a more careful interpretation?</summary>

The AHCCD stations in Alberta include many in the far north and at high elevations, while PEI stations are all at low elevation near the ocean.
The difference reflects station geography as much as provincial climate.
A fairer comparison would control for latitude and elevation, or compare only stations in similar geographic settings.
"Maritime provinces appear warmer than prairie provinces in this dataset" is accurate; "maritime provinces are warmer" is an overclaim.

</details>

<details markdown="1">
<summary markdown="1">You want to compute the mean temperature for the Arctic vs. non-Arctic parts of Canada. The temperature file has station IDs and the station file has latitude. Describe the two steps needed before grouping by Arctic status.</summary>

First, join the temperature file to the station file on station_id so each temperature row gains the latitude column.
Second, add a column that classifies each station as Arctic (latitude above 60° N) or non-Arctic, then group by that classification and compute the mean temperature.
Without the join, the temperature file has no latitude information.

</details>

## Exercises

### Elevation Effect

Bin stations into three elevation groups: below 300 m, 300-1 000 m, and above 1 000 m.
Ask the LLM to compute the mean annual temperature for each group.
Is there a consistent relationship between elevation and temperature?

### Longest Records

Find the ten stations with the longest continuous temperature records (most years of data).
What provinces are they in?
Is there a geographic pattern?

### Missing Data by Province

Compute the proportion of null temperature values for each province.
Is missing data evenly distributed, or do some provinces have much less data?
What might cause that pattern?

### Station Count per Province

After the join, count how many distinct stations each province has in the temperature file.
Compare the station count to the province's area.
Are larger provinces better-covered?

### Inner Join Loses Rows

The following code joins the temperature and station files,
but the combined row count is smaller than the number of temperature records.
Work with an LLM to explain why rows disappeared and fix the join type.

[%inc inner_bug.py %]

<details markdown="1">
<summary markdown="1">How do you know the fix worked?</summary>

After fixing, the row count of the joined result should equal `len(temps)`.
If it is smaller, some temperature records had no matching station and were dropped.

</details>

### Join Key Capitalisation

The following code attempts to join the two files but crashes with an error about a missing column.
Work with an LLM to find the column name mismatch and fix it.

[%inc case_bug.py %]

<details markdown="1">
<summary markdown="1">How do you know the fix worked?</summary>

Print `temps.columns` and `stations.columns` side by side and confirm the key column
appears with exactly the same name and capitalisation in both.
After fixing, the null province count should be zero or very small.

</details>

### Detecting Duplicate Station IDs

The following code joins the temperature and station files and prints the row counts.
Work with an LLM to extend it so it also checks whether any `station_id`
appears more than once in the station file, and prints those duplicated IDs if found.

[%inc dup_extend.py %]

<details markdown="1">
<summary markdown="1">How do you know the addition is correct?</summary>

If `combined` has more rows than `temps`, duplicated station IDs in the station file are the cause.
The list of duplicated IDs printed by the new code should account for the extra rows exactly.

</details>

### Reporting Unmatched Stations

The following code joins the files and computes mean temperature by province,
but does not report how many temperature records had no matching station.
Work with an LLM to extend it so it prints the null province count
and a sample of the unmatched station IDs before computing the group means.

[%inc unmatched_extend.py %]

<details markdown="1">
<summary markdown="1">How do you know the addition is correct?</summary>

The null count plus the non-null count should equal `len(combined)`.
Look at the unmatched station IDs and compare them to the station file
to understand why they did not match.

</details>
