# Tables

## Goals

-   Prompt an LLM to load tabular data and describe what it contains.
-   Interpret shape, column names, and data types.
-   Ask the LLM to compute standard deviation and range and explain what they mean for this data.

## What a Dataframe Contains

*What is a dataframe, and what does it look like?*

-   A [%g dataframe "dataframe" %] is a table with named columns where each column holds one type of data
    -   Text columns hold strings; numeric columns hold integers or decimal numbers; date columns hold dates
    -   Every row has a value for every column, or a special null marker if the value is missing
    -   A dataframe is the in-memory representation of data; a CSV file is one way to store it on disk
-   The dataset for this session is the Environment and Climate Change Canada HYDAT National Water Data Archive [%b hydat2025 %]
    -   HYDAT is a database of streamflow and water level measurements at Canadian rivers and streams going back to the 1800s
    -   Download a CSV export from [HYDAT][hydat] using the online data explorer, or use the tidyhydat R package to export a station subset as CSV
    -   The file has one row per station-month with columns for station number, station name, year, month, and mean monthly streamflow in cubic metres per second (m³/s)

*Why do different columns have different types, and why does it matter?*

-   A station number like `08MF065` looks like text but is stored as a string, so arithmetic on station IDs is meaningless
    -   Polars reads it correctly as a string by default
    -   Date columns stored as text cannot be sorted chronologically without conversion
	-   Confirm the type of any date column before using it in a time-series analysis

## Shape, Types, and Sample Rows

*Load the HYDAT flow data and tell me how many rows and columns it has, what each column contains, and what the data types are.*

or

*Using Polars, read flow_data.csv and print: the number of rows and columns, the name and type of each column, and the first two rows.*

-   The LLM will produce something like:

[%inc describe_flow.py %]

-   Run the cell and check each part of the output:
    -   Does the number of rows match the documentation for the stations and years you downloaded?
    -   Do the column types make sense? (`YEAR` and `MONTH` should be integers; `FLOW` should be a float; `STATION_NUMBER` should be a string)
    -   Does the sample row look like a real river observation?
-   If `FLOW` shows type `String`, the LLM did not parse it correctly
    -   Ask: "The FLOW column shows type String. How do I cast it to Float64 in Polars?"

## Standard Deviation and Range

*Compute the standard deviation and range of the streamflow column.*

or

*Compute the mean, standard deviation, minimum, maximum, and range of the FLOW column in flow_data.csv.*

-   The LLM will produce something like:

[%inc spread_flow.py %]

-   Run the cell and look at the numbers
    -   A standard deviation larger than the mean is common for streamflow data:
	    most months are near baseflow, but spring snowmelt can produce flows orders of magnitude higher
    -   A range of zero would mean every observation is identical: clearly wrong for river flow data
    -   A negative minimum would mean a data entry error: flow cannot be negative

## Interpreting High Spread

*What does a large standard deviation mean for river flow data?*

-   [%g standard-deviation "Standard deviation" %] measures how far a typical observation sits from the mean
    -   If the mean flow is 50 m³/s and the standard deviation is 200 m³/s, most months are far from the average
    -   This is not a data error: Canadian rivers experience dramatic seasonal variation
    -   A prairie river fed by snowmelt may run nearly dry in late summer and surge to hundreds of m³/s in May
-   [%g stat-range "Range" %] is the distance from the smallest to the largest value
    -   A high range reflects the difference between the lowest late-summer baseflow and the highest spring flood
    -   A single extreme flood event can set the maximum for decades of record

*Why is spread as important as the mean?*

-   Two stations with the same mean monthly flow can look completely different across the year
    -   Station A: flows of 40, 45, 50, 55, 60 m³/s all year (low spread, stable, likely groundwater-fed)
    -   Station B: flows of 2, 3, 250, 80, 10 m³/s (high spread, snowmelt-dominated)
    -   Both have approximately the same mean, but very different seasonal behaviour
-   A report that mentions only the mean without the spread hides information critical to flood risk and water management

## Checking a Single Station

*Filter to one known station and verify its row count against the dataset documentation.*

or

*Filter flow_data.csv to rows where STATION_NUMBER is '02GA010' and print the number of rows and the range of years covered.*

-   Station `02GA010` is the Grand River at Galt (Cambridge, Ontario), one of the longest continuous records in Canada
-   The HYDAT documentation describes how many years each station has been active
    -   If the station has been active since 1912 and the dataset covers monthly data, you expect roughly (current year - 1912) × 12 rows
    -   A very different number suggests the filter is wrong or the station ID format does not match

## Check Understanding

<details markdown="1">
<summary markdown="1">You load a CSV and see that the `YEAR` column has type `String`. When you ask the LLM to filter rows where YEAR is greater than 2000, the filter returns no results. What is wrong and how do you fix it?</summary>

Polars compares strings lexicographically, not numerically.
"2001" > "2000" works alphabetically, but "999" > "2000" does not, because "9" comes after "2" in character order.
More importantly, the filter `pl.col("YEAR") > 2000` compares a string to an integer, which Polars may reject with an error or handle incorrectly.
The fix is to cast the column first: `df.with_columns(pl.col("YEAR").cast(pl.Int64))`.

</details>

<details markdown="1">
<summary markdown="1">The mean monthly flow is 35 m³/s and the standard deviation is 120 m³/s. A classmate says "the data must be wrong because the standard deviation is larger than the mean." Are they right?</summary>

No.
A standard deviation larger than the mean is common for streamflow data;
it happens when the distribution is [%g right-skewed "right-skewed" %].
Most months have low flow near baseflow,
but a few months during spring snowmelt have extremely high flows that pull the mean upward
while the standard deviation reflects the wide spread.
The correct response is to plot the distribution and check whether the high values are physically plausible,
not to assume the data is wrong.

</details>

<details markdown="1">
<summary markdown="1">You filter to station `02GA010` and get 0 rows. The documentation says this station has records going back to 1912. List two things you would check.</summary>

First, check whether the station identifier column is named `STATION_NUMBER` in the actual CSV:
it might be `Station_Number`, `stn_id`, or something else entirely.
Print `df.columns` to see the exact names before filtering.
Second, check whether the value `"02GA010"` is stored with the same capitalisation and zero-padding in the data.
If the file uses `"2GA010"` without the leading zero, the filter will not match.
Print `df["STATION_NUMBER"].head()` to see the actual format.

</details>

<details markdown="1">
<summary markdown="1">You compute a maximum flow of 99 999 m³/s for one station. The mean is 18 m³/s and all other values are below 2 000 m³/s. Does this suggest a data error? What would you do next?</summary>

Yes, 99 999 is a suspicious round number that may be a sentinel value used to indicate an error or a missing data code in HYDAT's historic records.
Check the HYDAT data dictionary for what sentinel values are used.
Filter to rows where FLOW equals 99 999 and examine those rows for other patterns:
a specific year, a specific data quality symbol, or a note column.
Do not include that value in any statistical computation until you have confirmed what it represents.

</details>

## Exercises

### Most Variable Rivers

Ask the LLM to compute the coefficient of variation (standard deviation divided by mean) for each station.
Which stations have the highest coefficient of variation?
Are they in regions you would expect to have highly variable flow?

### Seasonal Pattern

Pick one station and ask the LLM to compute the mean flow for each month (January through December) averaged across all years.
Plot the result as a bar chart.
Does the seasonal pattern match what you would expect for the region?

### Stations with Suspicious Values

Ask the LLM to find all rows where FLOW is negative, zero, or greater than 50 000 m³/s.
How many rows have each kind of extreme value?

### Long-Term Change

For one station with records going back at least fifty years, ask the LLM to compute the mean annual flow for each year and plot it over time.
Is there a trend?
