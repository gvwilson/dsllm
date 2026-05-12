# First Charts

## Goals

-   Prompt an LLM to create a scatter plot and save it to a file.
-   Interpret whether a chart answers the question you asked.
-   Explain what correlation means and how to read it from a scatter plot.

## Why Charts Come First

*What is Anscombe's quartet, and why does it matter before we compute any statistics?*

-   A set of four small datasets with identical means, variances, and [%g correlation "correlation" %] [%b anscombe1973 %]
    -   Their [%g scatter-plot "scatter plots" %] look completely different:
	    one is linear, one is curved, one has a single extreme outlier
    -   Any statistical summary alone would tell you they are the same;
	    the charts immediately show they are not
-   The lesson: look at your data before computing anything
    -   A suspicious cluster, a curved pattern, or a handful of extreme points
	    can invalidate a statistical summary
-   Charts are not decoration; they are part of the analysis

*What dataset will we use, and what question will we ask?*

-   The dataset for this session is the Natural Resources Canada Earthquake Catalog [%b nrcan-quakes2025 %]
    -   Download the catalog from [NRCan Earthquakes][nrcan-quakes] as `earthquakes.csv`
    -   It has one row per recorded earthquake
	    with columns for date, location, depth in kilometres, magnitude, and region
    -   Canada experiences thousands of earthquakes per year;
	    most are too small to feel, but British Columbia and Quebec have significant seismic activity
-   Do deeper earthquakes tend to have larger magnitudes?
    -   Subduction-zone earthquakes (such as those off the BC coast) can be both deep and very large
    -   But the relationship is not guaranteed: the chart will show the actual pattern

## Drawing the Scatter Plot

*Make a scatter plot of earthquake depth on the x axis and magnitude on the y axis, coloured by region, and save it as a PNG.*

-   The LLM will produce something like:

[%inc scatter.py %]

-   Run the cell; the file `scatter.png` appears in the same folder as the notebook
-   Open the file to see the chart
    -   Most points should cluster at shallow depths and low magnitudes
    -   The largest earthquakes may appear at a range of depths, so look for any pattern
    -   Different regions (BC, Quebec, Yukon) should appear as distinct colours

## Validating the Chart

*How do I check that the chart shows all the data I expected?*

-   Count the rows in the dataframe and compare to the number of points in the chart
    -   If the dataframe has 15,000 rows but the chart shows 12,000 points, some data was silently dropped
    -   The most common cause is rows with missing values in the columns being plotted
-   The code already prints the point count; compare that to the total row count:

[%inc count_rows.py %]

-   A large mismatch is worth investigating before drawing conclusions
    -   If earthquakes in one region are more likely to have missing depth data,
	    the chart misrepresents that region

## Measuring Correlation

*Compute the correlation between earthquake depth and magnitude. Drop rows where depth or magnitude is missing.*

-   The LLM will produce something like:

[%inc correlation.py %]

-   The output should be a number between -1 and +1
    -   A value near 0 means no consistent linear relationship---deeper quakes are not systematically larger
    -   A positive value means deeper quakes tend to be larger; a negative value means the opposite
    -   The scatter plot will tell you whether the relationship is linear or curved

*What kind of correlation did you calculate?*

-   Should be Pearson

*What does the correlation coefficient actually tell you?*

-   Correlation measures the strength of a linear relationship between two variables
    -   0.9 is a strong positive relationship; 0.3 is a weak one
    -   The number tells you direction and strength, not the slope
-   Correlation does not tell you whether one variable causes the other
    -   Both earthquake depth and magnitude are determined by tectonic structure, not by each other
    -   This distinction matters more in sessions with human data
-   A correlation near zero does not mean there is no relationship
    -   There may be a non-linear pattern that a linear correlation cannot capture
	-   for example, very deep earthquakes in subduction zones tend to be large,
	    while very shallow ones can be large or small

## Iterating on Prompts

*The chart is hard to read because the points overlap. Adjust the prompt to improve it.*

-   Prompts rarely produce a perfect chart on the first try
-   Common improvements to ask for:
    -   "Add transparency (opacity 0.4) so overlapping points are visible."
    -   "Remove earthquakes with magnitude below 1.5---they clutter the chart without adding information."
    -   "Change the x axis label to 'Depth (km)' and the y axis label to 'Magnitude'."
-   After each change, re-run the cell and look at the new PNG
    -   If the chart looks worse, describe what changed and ask the LLM to revert that part

## Check Understanding

<details markdown="1">
<summary markdown="1">Your scatter plot shows 12,000 points but the dataframe has 18,000 rows. The LLM says some rows were dropped because they had missing values. Is this a problem? How would you decide?</summary>

It depends on whether the missing values are random or systematic.
If earthquakes in one region or detected by only a subset of seismograph networks
are more likely to have missing depth data,
the chart underrepresents those earthquakes
and any correlation you compute is biased toward the ones with complete data.
Ask the LLM to show how many rows are dropped per region and per year,
then decide whether the pattern is random or whether it affects your conclusions.

</details>

<details markdown="1">
<summary markdown="1">You compute a correlation of 0.12 between depth and magnitude. A classmate says this proves deeper earthquakes are slightly more powerful. What is the correct interpretation?</summary>

A correlation of 0.12 is a weak positive relationship.
It means deeper earthquakes in this dataset tend very slightly toward larger magnitudes on average,
but the association is so weak that depth explains almost none of the variation in magnitude.
"Proves" is too strong a word:
the correlation is small and may reflect chance variation rather than a physical mechanism.

</details>

<details markdown="1">
<summary markdown="1">You ask the LLM to plot depth vs. magnitude, and all the points are compressed into the bottom-left corner. What should you add to the next prompt, and why?</summary>

Ask for log scales on both axes.
Earthquake depth ranges from near-surface to over 600 km,
and magnitude spans several orders of magnitude of energy release.
A linear scale compresses most events into a small region.
A log scale stretches the smaller values apart
so the distribution of common earthquakes is visible alongside the rare large ones.

</details>

<details markdown="1">
<summary markdown="1">You ask the LLM to compute the correlation between two variables and it returns -0.03. You expected a strong relationship from the scatter plot. What is a likely explanation?</summary>

A correlation near zero with a visible pattern in the scatter plot usually means the relationship is not linear.
The scatter plot may show a curved or clustered pattern
(for example, two distinct populations of earthquakes at very different depths)
that a linear correlation coefficient cannot capture.
Ask the LLM to colour the points by a third variable such as region or fault type,
or consider fitting a non-linear model.

</details>

## Exercises

### Magnitude Distribution

Plot a histogram of earthquake magnitudes.
Describe the shape.
Are large earthquakes (magnitude 5 or above) common or rare in the catalog?

### BC vs. Quebec

Filter the dataset to BC earthquakes and Quebec earthquakes separately.
Compute the mean magnitude and mean depth for each.
Do the two regions have different seismic characteristics?

### Remove Micro-Earthquakes

The catalog includes many micro-earthquakes (magnitude below 2.0) detected only by sensitive instruments.
Filter them out and remake the scatter plot.
Does the correlation change meaningfully?

### Recent Decade

Filter to earthquakes recorded in the last ten years.
Is the density of points different from the full catalog?
What might explain the difference (hint: think about improvements to monitoring networks)?
