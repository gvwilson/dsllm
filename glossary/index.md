# Glossary

## C

<span id="causation">causation</span>
:   A relationship in which one variable directly produces a change in another.
    Causation is stronger than correlation: two variables can be correlated without one causing the other.
    Establishing causation usually requires a controlled experiment in which everything except the variable of interest is held constant.

<span id="csv">comma-separated values</span> (CSV)
:   A plain-text file format for tabular data in which each line is one row and values
    within a row are separated by commas.
    The first line is usually a header row listing column names.
    Empty values are represented by two consecutive commas or by a sentinel like `?` or `-99`.

<span id="confidence-interval">confidence interval</span>
:   A range of values computed from data such that, if the study were repeated many times,
    a specified percentage (commonly 95%) of the intervals computed would contain the true population value.
    A wider interval reflects greater uncertainty; a narrower interval reflects a more precise estimate.

<span id="correlation">correlation</span>
:   A measure of how consistently two variables move together.
    A positive correlation means both tend to increase together; a negative correlation means one tends to increase as the other decreases.
    Correlation is commonly measured on a scale from -1 (perfect inverse relationship) to +1 (perfect direct relationship), with 0 indicating no linear relationship.

## D

<span id="data-science">data science</span>
:   The practice of using computational and statistical tools to turn messy observations into defensible claims.
    Data science combines elements of statistics, programming, and domain knowledge to clean, summarize, visualize, and model data.

<span id="dataframe">dataframe</span>
:   An in-memory table with named columns and typed data, used to represent a dataset in code.
    Each column holds one kind of value (numbers, text, dates) and each row represents one observation.
    Polars and pandas are Python libraries that provide dataframes.

<span id="deskilling">deskilling</span>
:   The gradual loss of a skill that results from no longer practicing it,
    often because a tool or technology has taken over the task.
    Using an LLM to avoid thinking about data rather than to automate well-understood steps is a deskilling risk.

## J

<span id="join">join</span>
:   An operation that combines two tables by matching rows that share a common value in a specified column.
    A left join keeps every row from the first (left) table and adds matching columns from the second (right) table,
    filling in null where no match is found.

## L

<span id="llm">large language model</span> (LLM)
:   A machine-learning system trained on large amounts of text that generates new text
    by predicting the most plausible next word given everything before it.
    LLMs can write code, summarize documents, and answer questions,
    but they do not reason about problems.
    They produce plausible-sounding text based on patterns in their training data.

## M

<span id="mean">mean</span>
:   The arithmetic average of a set of values: the sum of all values divided by the count.
    The mean is sensitive to extreme values (outliers), which can pull it away from the center of the distribution.

<span id="median">median</span>
:   The middle value of a sorted list of numbers.
    When the list has an even number of values, the median is the average of the two middle values.
    The median is not sensitive to extreme values, making it a more stable measure of the center than the mean when outliers are present.

<span id="missing-value">missing value</span>
:   A data point that was not recorded or was lost.
    Missing values are represented differently in different datasets: as blank cells, as special codes like `?`, `-99`, or `NA`, or as the special null marker that database systems use.
    How missing values are dropped, filled in, or kept affects every analysis that uses the column.

## N

<span id="notebook">notebook</span>
:   An interactive document that combines code, output, and text in a single file.
    Jupyter notebooks (`.ipynb`) and Marimo notebooks (`.py`) are common formats in data science.
    A notebook is reproducible if running all cells from top to bottom always produces the same result.

<span id="null-hypothesis">null hypothesis</span>
:   The default assumption in a hypothesis test that there is no effect, no difference, or no relationship.
    A statistical test asks: how surprising would the observed data be if the null hypothesis were true?
    A small p-value means the data are surprising under the null hypothesis, which is evidence against it.

## O

<span id="outlier">outlier</span>
:   A value that is far from the bulk of the data.
    Outliers can be genuine extreme observations (a record-breaking temperature, a very large company) or data errors (a mistyped value, a missing-value code that was not filtered out).
    Identifying outliers and deciding how to handle them is a critical step in data cleaning.

## P

<span id="p-value">p-value</span>
:   The probability of observing data at least as extreme as what was observed, assuming the null hypothesis is true.
    A p-value below a chosen threshold (commonly 0.05) is taken as evidence against the null hypothesis.
    A p-value is not the probability that the null hypothesis is true, and a significant p-value does not mean the effect is large or that the measurement was correct.

<span id="probability">probability</span>
:   A number between 0 and 1 that describes how often an event occurs in a large number of identical trials.
    A probability of 0 means the event never occurs; 1 means it always occurs; 0.5 means it occurs about half the time.
    When estimated from data, probability is a proportion: if 23 of 200 samples exceed a threshold, the estimated probability is 0.115.

## R

<span id="stat-range">range</span>
:   The difference between the maximum and minimum values in a dataset.
    Range is easy to compute but sensitive to a single extreme value; a dataset can have a large range because of one outlier even if almost all values are clustered tightly.

<span id="regression">regression</span>
:   A statistical method that fits a line (or curve) to a set of data points to summarize the overall relationship between two variables.
    A linear regression line minimizes the total squared distance from each point to the line.
    The slope of the line describes the direction and rate of change; the scatter of points around the line describes how consistently the relationship holds.

<span id="replication-crisis">replication crisis</span>
:   The finding, starting around 2011, that many published scientific results could not be reproduced by other researchers.
    Common causes include underpowered studies, selective reporting of results, and analyses that were not saved in a runnable form.

<span id="reproducibility">reproducibility</span>
:   The property of an analysis such that running the same code on the same data produces the same result.
    Reproducibility requires that the data file, the code, and the software environment are all available and unchanged.

<span id="right-skewed">right-skewed</span>
:   A distribution in which most values are clustered near the low end,
    but a long tail extends toward higher values,
    pulling the mean above the median.
    Income distributions are a classic example.

## S

<span id="sampling-bias">sampling bias</span>
:   A systematic error that occurs when the data collected is not a representative sample of the population being studied.
    If records for one group are missing more often than for others, any conclusion drawn from the data may not apply to the full population.

<span id="scatter-plot">scatter plot</span>
:   A chart that represents each observation as a point with one variable on the x axis and another on the y axis.
    Scatter plots reveal the shape of the relationship between two variables, including clusters, outliers, and non-linear patterns that summary statistics alone cannot show.

<span id="standard-deviation">standard deviation</span>
:   A measure of how far a typical value in a dataset is from the mean.
    A small standard deviation means most values are clustered near the mean; a large one means they are spread out.
    Standard deviation is in the same units as the original data, making it easier to interpret than variance.

## T

<span id="trend-line">trend line</span>
:   A line added to a chart to summarize the overall direction of the data.
    In Altair, a trend line is commonly added using a regression transform.
    The slope of the trend line shows the rate and direction of change; points scattered widely around the line indicate high year-to-year variation.
