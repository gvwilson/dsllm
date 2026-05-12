# Tracking Change

## Goals

-   Prompt an LLM to plot a variable over time and describe what it shows.
-   Interpret a [%g trend-line "trend line" %]: direction, slope, and scatter around the line.
-   Distinguish a real [%g regression "trend" %] from seasonal or random fluctuation.

## Why Change Matters

*Why do researchers usually study change over time rather than a single snapshot?*

-   A single measurement tells you where something is; a time series tells you where it is going
    -   One year of flu data tells you how bad that season was; decades of data reveal whether flu is becoming more or less severe
    -   One temperature reading tells you today's weather; a century of readings reveals the climate trend
-   The dataset for this session is the Public Health Agency of Canada FluWatch weekly influenza surveillance program [%b fluwatch2025 %]
    -   Download the weekly data from [FluWatch][fluwatch]
    -   It has one row per week per region with columns for the week number, year, region, and the percentage of physician visits for influenza-like illness (ILI)
    -   Canada has used the same surveillance methodology since the early 1990s, making it suitable for long-term trend analysis
-   The question: has the peak severity of flu season in Canada been changing over the decades?

## Plotting Over Time

*Plot weekly influenza-like illness percentage over time as a line chart.*

-   Paste this prompt: "Using Polars and Altair, read fluwatch.csv, plot the weekly ILI percentage over time as a line chart coloured by year, and save it as flu_line.png."
-   The LLM will produce something like:

[%inc flu_line.py %]

-   Run the cell and open the PNG
    -   The chart should show a repeating winter spike pattern
    -   Different years appear as different coloured lines
    -   The seasonal pattern is immediately visible---this is why you plot before computing anything

## Fitting a Trend Line

*Fit a trend line to the annual peak ILI values and show the slope.*

-   Paste this prompt: "Using Polars and Altair, compute the maximum weekly ILI percentage for each year, then plot those annual peaks with a regression trend line. Save the chart as flu_trend.png."
-   The LLM will produce something like:

[%inc flu_trend.py %]

-   Run the cell; the chart shows annual peaks as dots and a line through them
    -   Look at whether the line tilts up or down
    -   A rising line means flu peaks have been getting more severe on average
    -   A falling line means they have been getting milder

## What a Regression Line Tells You

*What does the trend line actually represent?*

-   A [%g regression "regression" %] line is the line that minimizes the total squared distance from each point to the line
    -   It is the best straight-line summary of the overall direction of the data
    -   It does not describe any individual year---most years will be above or below the line
-   The slope of the line tells you the direction and rate of change
    -   A slope of +0.1 means flu peak severity increases by about 0.1 percentage points per year on average
    -   A slope near 0 means no consistent trend over the period
-   The scatter of points around the line measures how reliable the trend is
    -   If all points are close to the line, the trend is consistent
    -   If points are scattered widely, year-to-year variation dominates and the trend is weak

## Seasonal Pattern vs. Long-Term Trend

*How do I tell the difference between the winter flu spike and a real long-term change?*

-   The winter spike is a seasonal pattern: it repeats every year and tells you nothing about whether flu is getting worse over time
    -   Seasonal patterns are short-cycle fluctuations driven by predictable factors (cold weather, school schedules, indoor crowding)
    -   Confusing the spike with a trend is one of the most common mistakes in time-series analysis
-   A long-term trend is the underlying direction visible across many seasons
    -   To see the trend, you need to compare the same part of each cycle---the annual peak, or the annual mean---across years
    -   Fitting a trend line to raw weekly data (including all the seasonal variation) will produce a line, but it will not be a meaningful trend
-   Ask yourself: "Am I comparing like to like?"
    -   Annual peak to annual peak: yes
    -   One winter week in 2000 to one spring week in 2010: no

## Checking the Trend Direction

*How do I confirm the trend line is pointing in the right direction?*

-   The most basic check: does the trend line agree with what you see by eye?
    -   If the dots appear to be drifting upward but the line slopes down, something is wrong
    -   The most common cause is the LLM using a variable that does not represent the trend you wanted
-   Ask the LLM to print the slope: "What is the slope of the regression line in the previous chart?"
    -   A positive number should correspond to an upward-sloping line
    -   If the sign does not match the visual direction, the regression used the wrong axis

[%inc check_slope.py %]

## Check Understanding

<details markdown="1">
<summary markdown="1">You plot annual FluWatch peaks from 1993 to 2023 and fit a trend line. The line has a slope of +0.12 percentage points per year. A classmate says "this proves Canadian flu seasons are getting worse." What is the correct interpretation, and what is missing?</summary>

A slope of +0.12 means Canadian flu peaks have increased by an average of about 0.12 percentage points per year over this period in this dataset.
It does not prove flu is getting worse---the trend could reverse, surveillance methodology may have changed, and 0.12 pp per year may or may not be practically meaningful.
What is missing: a confidence interval on the slope (which would show whether the trend is distinguishable from zero) and a check on whether any pandemic years (2009, 2020) are distorting the estimate.

</details>

<details markdown="1">
<summary markdown="1">The FluWatch line chart shows an enormous spike in 2009 that is much higher than any other year. You fit a trend line to the full dataset. How does this spike affect the slope, and what should you do about it?</summary>

The 2009 H1N1 pandemic caused an unusually severe flu season.
That extreme point pulls the trend line upward if it falls late in the dataset.
The right approach is to note the outlier explicitly, fit the trend line with and without 2009, and report both results.
A single year driven by a pandemic is qualitatively different from a severe seasonal flu and should not silently drive a long-term trend estimate.

</details>

<details markdown="1">
<summary markdown="1">A classmate fits a trend line to raw weekly ILI percentages over all years and concludes "there is a slight upward trend in flu rates." What is wrong with this analysis?</summary>

Fitting a trend line to raw weekly data mixes the seasonal pattern with any long-term trend.
If surveillance weeks shifted slightly over time (for example, more winter-week data in recent years due to expanded reporting), the raw weekly series will slope upward for reasons unrelated to actual flu severity.
The correct approach is to compare annual peaks or annual means---comparable points across years---rather than raw weekly values.

</details>

<details markdown="1">
<summary markdown="1">You ask the LLM to compute the slope of the trend line and it returns -0.09. But when you look at the chart, the line clearly slopes upward to the right. What should you do?</summary>

A negative slope with an upward-sloping chart means the LLM computed the regression with the axes reversed---fitting year as a function of ILI rather than ILI as a function of year---or reported the slope of a different variable.
Ask the LLM: "In the regression, which variable is x (the predictor) and which is y (the response)?"
Do not report the slope until the sign matches what you see in the chart.

</details>

## Exercises

### Pandemic Year

Remove the 2009 pandemic year from the annual peak data and refit the trend line.
Does the slope change meaningfully?
Report both slopes and explain what the comparison shows.

### Regional Trends

FluWatch data includes provincial and regional breakdowns.
Pick two provinces and plot their annual peaks on the same chart.
Are their trends parallel, or does one province show a stronger change than the other?

### Early vs. Late Period

Split the data at 2010 and compute a trend line for the period before 2010 and a separate one for the period after.
Are the slopes similar or different?
What might explain a difference?

### Seasonality Index

For each week number (1 through 52), compute the mean ILI percentage across all years.
Plot the result as a line chart.
In which week does flu typically peak in Canada?
