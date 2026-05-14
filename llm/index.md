# First Steps

## Goals

-   Launch the notebook environment and run a first code cell.
-   Prompt an LLM to read a data file and print its contents.
-   Prompt an LLM to compute and interpret the mean and median of a column.

## Starting the Notebook

> How do I start a notebook and create a first cell?

-   A [%g notebook "notebook" %] is a document that mixes text, code, and output in one file
    -   Jupyter notebooks have the extension `.ipynb`; each piece of code or text is called a "cell"
    -   Each cell can hold either code or explanatory text; you run code cells one at a time and the output appears directly below
-   Your instructor will give you a URL to open the notebook environment in your browser
    -   If you are running Jupyter on your own laptop, open the Terminal app (Mac) or Command Prompt (Windows), type `jupyter notebook`, and press Enter; a browser tab will open automatically
    -   Either way, you will see a file browser; click "New" and choose "Python 3" to create a fresh notebook
-   To add a code cell, click the `+` button in the toolbar or press `B` when a cell is selected
-   To run a cell, press `Shift+Enter`
    -   The output appears directly below the cell
    -   If the cell causes an error, the error message appears there too

> What should I type in the first cell to make sure everything is working?

-   Paste `print("hello")` into the first cell and press `Shift+Enter`
    -   If you see `hello` appear below the cell, the environment is working
    -   If you see an error like `ModuleNotFoundError`, a required package is not installed

## Reading the Data

> Read a CSV file of monthly climate observations and print its first five rows.

-   The dataset for this session is
    the Environment and Climate Change Canada Historical Climate Data [%b eccc-climate2025 %]
    -   Go to [ECCC Climate Data][eccc-climate] and search for a station near you
        (e.g., Toronto Pearson International Airport or Vancouver International Airport)
    -   Select "Monthly" data, choose all available years, and download as CSV
    -   The file is named something like `en_climate_monthly_ON_6158731_1840-2025_P1M.csv`
    -   It has one row per month with columns for mean temperature, precipitation, and other observations

-   [Polars][polars] is a Python library for working with tables of data
    -   It is already installed in the course environment; you do not need to do anything to set it up
    -   Including "Using Polars" in your prompt tells the LLM which tool to use;
        without it, the LLM might choose a different library and produce code that does not run in your environment

> Use Polars to read a CSV file called climate.csv, skip the first row which is a title line, treat empty cells as missing, and print the first five rows.

-   The LLM will produce something like:

[%inc read_climate.py %]

-   Paste the code into a new notebook cell and run it
    -   The output shows five rows with columns including `Year`, `Month`, and `Mean Temp (°C)`
    -   If the code crashes with `FileNotFoundError`, the CSV is not in the same folder as the notebook

## Mean and Median

-   The [%g mean "mean" %] is the sum of all values divided by the count (also called the average)
-   The [%g median "median" %] is the middle value when all observations are sorted from smallest to largest

> Compute the mean and median of the monthly mean temperature column.

- If that doesn't work, try a more specific prompt:

> Using Polars, read climate.csv the same way, then compute and print the mean and median of the 'Mean Temp (°C)' column, excluding missing values.

-   The LLM will produce something like:

[%inc mean_median.py %]

-   Run the cell
    -   For most Canadian cities the annual mean will be between -10° and +15° C
    -   If the number is in the hundreds, the LLM likely read the wrong column

> Why would the mean and median of a dataset ever be different numbers?

-   The mean is the sum of all values divided by the count
    -   It is pulled toward extreme values:
        a few very cold winters raise the magnitude of negative values and pull the mean down
-   The median is the middle value when the data is sorted
    -   Exactly half the values are above it and half are below
    -   A few extreme months do not move it much
-   For Canadian climate data,
    the mean and median are often close because temperatures follow a roughly symmetric seasonal cycle
    -   They can differ dramatically in a dataset with [%g outlier "outliers" %]
-   When outliers matter for your question, report the mean;
    when you want a typical value unaffected by extremes, report the median
    -   Temperature records: usually mean, because the total heat budget drives most climate effects
    -   Housing prices: usually median, because a handful of luxury properties distort the mean

## Saving the Notebook

> What does it mean to save a notebook, and why does it matter?

-   Saving a Jupyter notebook writes all cells and all outputs to a `.ipynb` file on disk
    -   In Jupyter, press `Ctrl+S` (or `Cmd+S` on Mac) or click the save icon
    -   The saved file is a record of the analysis that anyone with the same data file can re-run
-   [%g reproducibility "Reproducibility" %] means that
    running the same code on the same data produces the same result
    -   A notebook achieves this only if cells are run in order from top to bottom
    -   Running cells out of order can produce outputs that no longer match the code
    -   Use "Kernel → Restart and Run All" before sharing a notebook to confirm everything runs cleanly
-   The combination of the data file and the saved notebook is the smallest unit of reproducible analysis

## Saving Prompts

> I am tired of typing "use Polars" and "treat empty cells as missing" in every prompt. Is there a way to set these once?

-   Most LLM tools let you set custom instructions that are added to every conversation automatically
    -   In Claude, open Settings and look for "Custom instructions" or create a Project and add instructions there
    -   In ChatGPT, open Settings → Personalization → Custom instructions
    -   Whatever you write there is sent to the LLM along with every prompt you type, without you having to repeat it
-   Useful things to put in custom instructions for this course:
    -   "Always use Polars for data manipulation, not pandas."
    -   "Always use Altair for charts."
    -   "Treat blank cells and the values U, Q, and N as missing unless I say otherwise."
    -   "Print the first five rows after reading any CSV file."
-   Custom instructions do not replace careful prompting
    -   You still need to give the LLM the column names and goal for each specific task
    -   They only save you from repeating the same background preferences in every session

## Check Understanding

<details markdown="1">
<summary markdown="1">You run the cell with `read_climate.py` and see a column of values like `14567`, `15023`, `-9999`. None of these look like temperatures. What are two likely causes, and how would you diagnose each?</summary>

The first likely cause is reading the wrong column:
the code may be using a station ID or a precipitation total instead of mean temperature.
Check the column names printed in the output header to confirm which column was used.
The second likely cause is that `skip_rows=1` was wrong and the first data row was skipped or misaligned,
shifting all values.
Print `df.head(1)` and compare it to the raw CSV to see whether the rows line up correctly.

</details>

<details markdown="1">
<summary markdown="1">The mean monthly temperature for your station is -2.8 °C but the median is -1.1 °C. What does this tell you about the shape of the data?</summary>

The mean is lower than the median, which means the data is skewed toward colder values.
A few very cold winter months (perhaps during extreme cold snaps) pull the mean downward
while the median stays closer to the centre of the distribution.
This is a common pattern for Canadian climate data,
where extreme cold events are more severe than extreme warm events at most stations.

</details>

<details markdown="1">
<summary markdown="1">A classmate runs their notebook, gets a correct result, then closes it and reopens it the next day. They see the output from yesterday still displayed. They say "the analysis still works." What is wrong with this reasoning?</summary>

Jupyter displays the last-run output even after the kernel shuts down.
The visible result from yesterday does not mean the code will produce the same result today:
it is a snapshot, not a live computation.
To confirm the analysis still works, they need to restart the kernel and run all cells from top to bottom.

</details>

<details markdown="1">
<summary markdown="1">Your research partner works with data on Canadian home sale prices where a handful of luxury waterfront properties are in the sample. They want to report "the typical sale price." Should they use the mean or the median? Explain your reasoning.</summary>

The median.
A few multi-million-dollar properties would pull the mean far above what a typical buyer pays.
The median is the middle value and is not affected by those extremes,
so it better represents what a typical property in the sample sells for.

</details>

## Exercises

### Different Seasons

Compute the mean and median for January temperatures and July temperatures separately.
Are they closer together within a season than across the full year? Why might that be?

### Plot Over Time

Ask the LLM to make a line chart of mean annual temperature over time (one point per year).
Save it as a PNG.
Describe in one sentence what the chart shows about temperature change at your station.

### Count Missing Values

Ask the LLM to count how many missing values appear in each column.
Which columns tend to have more missing data, and why might that be for a weather station dataset?

### Compare Two Stations

Download data for a second station in a different region (e.g., one coastal and one inland).
Ask the LLM to compute the mean annual temperature for each station and display them side by side.
Which station is warmer on average?
