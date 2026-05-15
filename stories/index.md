# Telling Stories

## Goals

-   Choose chart types that match the question being asked.
-   Prompt an LLM to create bar charts, line charts, and faceted charts.
-   Explain why a correlation between two variables does not prove one causes the other.

## Matching Chart Type to Question

> How do I decide which type of chart to make?

-   The chart type should follow from the question, not from the tool's default
    -   "How many?" → bar chart (counts or totals per category)
    -   "How does this change over time?" → line chart
    -   "What is the distribution of values?" → histogram
    -   "Do two variables move together?" → scatter plot
-   The dataset for this session is the Education Quality and Accountability Office Ontario School Results [%b eqao2025 %]
    -   Download school-level results from [EQAO][eqao]
    -   It has one row per school with columns for school name, board name, board type (Public or Catholic), school language (English or French), and the percentage of Grade 3 students achieving Level 3 or 4 in reading and mathematics

> What question will we ask?

-   The question: do Catholic board schools score differently from public board schools in Grade 3 reading, and does this pattern differ between English and French schools?
    -   Board type is a category with two values; score is a number; school language creates natural panels
    -   A bar chart of mean reading score by board type, with one panel per language, is the right starting point

## Building a Faceted Chart

> Make a bar chart of mean percentage at Level 3 or 4 in Grade 3 reading by board type, with one panel per school language.

or

> Using Polars and Altair, read eqao_school_results.csv. Make a bar chart of mean Grade 3 reading percentage (level 3 or 4) by board type, with a separate panel for English and French schools. Save it as reading_chart.png.

-   The LLM will produce something like:

[%inc grade_charts.py %]

-   Run the cell and open the PNG
    -   Are there two panels (one for English schools, one for French)?
    -   Is there a visible difference between Public and Catholic bars?

## Reading the Chart

> What does the chart show, and what does it not show?

-   A taller bar for Catholic schools than Public schools means students in Catholic schools had a higher mean percentage at Levels 3 and 4
    -   This is a difference in group averages, not a measure of what caused it
    -   The bars tell you where each group ended up, not why
-   Look at the size of the differences: a mean of 64% vs. 66% may look dramatic on a bar chart but is small in absolute terms
    -   Check the y axis range: if it starts at 60 instead of 0, a 2-point difference looks enormous
-   Count whether both board types appear in both panels
    -   If a bar is missing, there are no schools of that type in that language stream
    -   This is not an error, but worth noting

## Why Correlation Is Not Causation

> The chart shows Catholic schools score slightly higher. Does that prove board type causes better scores?

-   No. Correlation means two things tend to appear together; causation means one thing produces the other
    -   Catholic schools may enrol students from communities with higher household incomes, lower family stress, or stronger cultural emphasis on academic achievement
    -   Any of these factors could independently produce higher scores
    -   The chart cannot separate board type from everything else that might be different between schools
-   [%g causation "Causation" %] is established through controlled experiments where the only thing that differs between groups is the factor being tested
    -   In an observational dataset like this one, you can describe a pattern but cannot claim to have found its cause
    -   "Catholic board schools have a higher mean reading score in this dataset" is a fair summary; "attending a Catholic school causes higher reading scores" is not

## Fixing a Misleading Axis

> The y axis starts at 55 instead of 0. Fix the chart so the differences are not visually exaggerated.

or

> Remake the reading chart but set the y axis to start at 0 so the bar heights honestly show the magnitude of the differences.

-   The LLM will produce something like:

[%inc grade_charts_fixed.py %]

-   Compare the two charts side by side
    -   In the version starting at 55, a 3-point difference looks large
    -   In the version starting at 0, the same difference looks small relative to the full 0-100 scale, which is more honest
-   Starting a bar chart axis above zero is one of the most common ways charts mislead; always start bar charts at zero unless you have an explicit reason not to

## Validating Each Panel

> How do I confirm that each panel in the faceted chart contains the data I expect?

or

> For each combination of board type and school language, print the number of schools and the mean reading percentage.

[%inc validate_panels.py %]

-   Check the output:
    -   Are the counts roughly what you expect for Ontario's school system?
    -   Do any cells have very few schools (fewer than 5)? A bar built on 3 schools is not reliable
    -   Does the mean in the table match the bar height in the chart?

## Check Understanding

<details markdown="1">
<summary markdown="1">You want to show how Ontario's mean Grade 3 reading score has changed over the years the EQAO has been published. Which chart type should you use, and why?</summary>

A line chart with year on the x axis and mean score on the y axis.
A line chart is appropriate for showing change over time because the connected line signals continuity and directionality.
A bar chart could also work but would not convey the same sense of trajectory.
A scatter plot would work but lacks the visual connection between years.

</details>

<details markdown="1">
<summary markdown="1">A classmate makes a bar chart where the y axis runs from 60 to 68. The Catholic bar reaches 67 and the Public bar reaches 64. They say "Catholic schools perform 5% better." What is wrong?</summary>

Two errors.
First, 67 minus 64 is 3 percentage points, not 5%.
Second, on a scale from 0 to 100, a 3-point difference is 3% of the full scale,
but the y axis starting at 60 makes the Catholic bar look nearly twice as tall as the Public bar.
The correct description is "Catholic schools had a mean reading score 3 percentage points higher in this dataset," and the chart should start at 0 to make the difference look proportional.

</details>

<details markdown="1">
<summary markdown="1">The data shows that schools in boards with higher per-pupil funding have higher mean reading scores. A classmate says "more money causes better scores." What alternative explanations should you consider?</summary>

Higher-income municipalities generate more local property tax revenue, which funds higher per-pupil spending and also tends to mean students come from families with more resources, more stability, and more access to books and enrichment activities.
Both the funding and the scores may be driven by the same underlying factor (community wealth) rather than one causing the other.
Establishing that funding itself causes higher scores would require comparing schools that received different funding levels for reasons unrelated to community wealth.

</details>

<details markdown="1">
<summary markdown="1">You check the panel validation table and find that one cell contains only 2 schools with a mean reading percentage of 91%. Should this bar appear in the published chart? What should you do?</summary>

A mean based on 2 schools is unreliable:
one school with an unusual student population could set the mean at any value.
Either remove bars with fewer than a minimum threshold (say, 10 schools) and note the cutoff, or add a note to the chart indicating that cells with fewer than 10 schools are suppressed or flagged.
EQAO itself suppresses results for small schools for exactly this reason;
you should follow the same practice.

</details>

## Exercises

### Histogram of Reading Scores

Plot a histogram of the Grade 3 reading percentage across all schools.
Describe the shape of the distribution.
Are there any schools with unusually high or low scores?

### Math vs. Reading

Make a scatter plot of Grade 3 reading percentage on the x axis and Grade 3 math percentage on the y axis, coloured by board type.
Compute the correlation.
Do schools that perform well in reading tend to perform well in math?

### Urban vs. Rural

If the dataset includes a municipality or region column, compare mean reading scores between schools in large cities and schools in smaller communities.
Does the pattern match what you would expect?

### Chart Comparison

Make three versions of the mean reading score by board type chart: one starting the y axis at 0, one starting at 50, and one starting at the minimum mean value.
Write one sentence describing how the visual impression changes in each version.

### Exaggerated Differences

The following code draws the reading score chart with a y axis that starts at 55 instead of 0,
making small differences look much larger than they are.
Work with an LLM to fix the axis so the bars are drawn to an honest scale.

[%inc axis_bug.py %]

<details markdown="1">
<summary markdown="1">How do you know the fix worked?</summary>

Open both the original and fixed PNGs side by side.
In the fixed version, the Catholic and Public bars should look similar in height
if their mean scores differ by only a few percentage points on a 0-to-100 scale.

</details>

### Facets on the Wrong Variable

The following code is meant to show one panel per school language,
but the panels are labelled with board types instead.
Work with an LLM to find the wrong column and fix it.

[%inc facet_bug.py %]

<details markdown="1">
<summary markdown="1">How do you know the fix worked?</summary>

The fixed chart should have panels labelled "English" and "French,"
not "Public" and "Catholic."
Check that each panel contains bars for both board types.

</details>

### Colour Scale for a Continuous Variable

The following code draws a scatter plot of reading vs. math scores coloured by reading percentage,
but the legend shows dozens of discrete colour swatches instead of a smooth gradient.
Work with an LLM to find the encoding error and fix it.

[%inc color_bug.py %]

<details markdown="1">
<summary markdown="1">How do you know the fix worked?</summary>

After fixing, the legend should show a continuous colour gradient from low to high reading scores.
Print `df["grade3_reading_pct"].dtype` and confirm it is `Float64`, not `String`.

</details>

### Showing School Counts on the Bars

The following code draws a bar chart of mean reading scores per board type per language panel.
Work with an LLM to extend it so the number of schools in each group
appears as a text label on top of each bar.

[%inc count_extend.py %]

<details markdown="1">
<summary markdown="1">How do you know the addition is correct?</summary>

Compare the text labels to the `n_schools` values already in `summary`.
For one group, count the matching rows in the raw CSV yourself and confirm the label is right.

</details>
