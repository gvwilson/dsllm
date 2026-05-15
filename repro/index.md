# Reproducibility

## Goals

-   Re-run a complete analysis from a saved notebook and verify it produces identical output.
-   Reproduce a published scientific figure from public data and code.
-   Explain what makes an analysis reproducible and why it matters.

## The Replication Crisis

> Why does replication matter for data science?

-   Many published scientific findings fail when other researchers try to reproduce them [%b ioannidis2005 %]
    -   In one large study, only about 36% of psychology findings replicated successfully [%b osc2015 %]
    -   Similar problems have been found in medicine, economics, and ecology
    -   A [%g replication-crisis "replication crisis" %]
-   A common cause is that the analysis was not saved in a runnable form
    -   The researcher clicked through a spreadsheet, applied some filters, computed a number, and wrote it down
    -   Six months later, neither they nor anyone else can retrace the exact steps
-   Reproducibility means that running the same code on the same data produces the same result
    -   A saved notebook is a start, but reproducibility also requires the data and the software environment to be available and unchanged
-   This session uses atmospheric CO2 data from the Environment and Climate Change Canada Alert Station [%b alert-co22025 %]
    -   Alert, Nunavut sits at 82.5° N on the tip of Ellesmere Island
        (the northernmost point of Canada and one of the most remote places on Earth)
    -   Continuous CO2 measurements have been taken there since 1975 as part of the Global Atmosphere Watch program
    -   Like the better-known Mauna Loa record from Hawaii, the Alert record shows the same unmistakable upward trend in atmospheric CO2

## What Reproducibility Requires

> What does an analysis need in order to be reproducible?

-   Three things must all be available and unchanged:
    -   The data file, exactly as it was when the analysis was run
    -   The code, in the order it was executed
    -   The software environment: the versions of Python, Polars, Altair, and every other package used
-   The notebook handles the code and the execution order, but not the other two
    -   Record the data download date and, where possible, save a copy of the raw file alongside the notebook
    -   Record the software versions in the notebook using a cell that prints them

[%inc versions.py %]

## Recreating the Alert CO2 Curve

> Prompt the LLM to write a complete analysis that recreates the Alert Station CO2 curve.

-   Download the monthly CO2 data from [ECCC Alert Station][eccc-alert]
    -   Save it as `alert_co2_monthly.csv`
    -   The file has no column headers; the columns in order are year, month, decimal date, monthly average CO2 in ppm, deseasonalized CO2, number of days, standard deviation, and uncertainty
    -   Missing values are coded as -999.99

or

> The file alert_co2_monthly.csv has no column headers. The columns in order are year, month, decimal date, monthly average CO2 in ppm, deseasonalized CO2, number of days, standard deviation, and uncertainty. Missing values are -999.99. Using Polars and Altair, read the file, drop missing values, plot monthly average CO2 over decimal date as a line chart, and save it as alert_co2.png.

-   The LLM will produce something like:

[%inc alert_co2.py %]

-   Run the cell and open the PNG
    -   The chart should show a rising curve with a seasonal oscillation overlaid on it
    -   The oscillation is larger at Alert than at lower latitudes because the Arctic seasonal cycle of plant growth and decay is more pronounced
    -   The overall rise is the long-term accumulation of atmospheric CO2

## Comparing to the Published Figure

> How close does our chart come to the ECCC published figure?

-   Visit [ECCC Alert Station][eccc-alert] and view the official atmospheric CO2 graphic
    -   The x axis should cover the same year range (1975 to present)
    -   The y axis scale (approximately 330 to 425 ppm) should match
    -   The shape (a rising curve with seasonal sawtooth) should be identical
-   If your chart and the official figure disagree:
    -   Check whether you dropped the right rows (missing values coded as -999.99, not as 0 or blank)
    -   Check whether you used the `average` column rather than the `deseasonalized` column
    -   Check whether the x axis is decimal date (continuous) rather than year (discrete)

## Running the Notebook Again

> How do I confirm the analysis is truly reproducible?

-   Restart the kernel (Kernel → Restart in Jupyter) and run all cells from top to bottom
    -   If any cell fails or produces different output, the notebook is not reproducible
    -   Common causes: cells run out of order, variables changed in a cell that was later deleted, or a file path that no longer exists
-   Compare the output chart to the one saved earlier
    -   If they are visually identical, the analysis is reproducible on this machine with this software version

[%inc rerun_check.py %]

## Sharing the Notebook

> What does a collaborator need to re-run this analysis?

-   The minimum they need:
    -   The `.ipynb` notebook file
    -   The `alert_co2_monthly.csv` data file
    -   The same versions of Python, Polars, and Altair that you used
-   What can silently break when they try:
    -   A newer version of Polars or Altair may change an API, causing a crash or a different result
    -   The ECCC data file is updated periodically; a file downloaded later has more rows and may produce a slightly different chart
    -   If the collaborator runs cells out of order, the results may differ even with identical software and data
-   The safest approach: include a `requirements.txt` or `pyproject.toml` that locks the package versions, and note the download date of the data file in the first cell of the notebook

## Check Understanding

<details markdown="1">
<summary markdown="1">You share a notebook with a colleague. They install the packages fresh and run all cells, but the Altair chart looks slightly different from yours: the axis labels are in a different font and the line is a slightly different shade of blue. Is the analysis reproducible?</summary>

Yes, if the underlying numbers are the same.
Visual rendering details like fonts and colour shades can vary between operating systems, browser versions, and Altair versions without affecting the data or computations.
The relevant test is whether the plotted CO2 values at each date are identical.
If the colleague's chart shows the same curve with the same x and y values, the analysis is reproducible even if the appearance differs slightly.

</details>

<details markdown="1">
<summary markdown="1">You download the Alert CO2 file in January 2025 and run the analysis. A colleague downloads the same file in March 2025 and gets a chart that extends two months further. Is either analysis wrong?</summary>

Neither is wrong.
ECCC updates the file periodically with new measurements.
The two analyses are each reproducible from their respective data files, but they are not identical because the input data changed.
To ensure your colleague gets the same chart, share your copy of the data file alongside the notebook, not just a link to the ECCC download page.

</details>

<details markdown="1">
<summary markdown="1">You restart the kernel and run all cells, but cell 5 crashes with "NameError: name 'df' is not defined." Cell 3 defines df. What is the most likely cause?</summary>

Cell 5 refers to a variable defined in cell 3, which should have run first.
But cell 3 may have been skipped, crashed silently, or a previous run left `df` defined in memory so the notebook appeared to work until the kernel was restarted.
The fix is to ensure cell 3 runs without error before cell 5.
The lesson is that notebooks that only work when run in a particular partial order are not truly reproducible.

</details>

<details markdown="1">
<summary markdown="1">A paper claims its results are reproducible because the code is available on GitHub. A reviewer finds that the code uses a hardcoded path like `/Users/alice/Desktop/data.csv`. Is the paper's claim correct?</summary>

No.
The hardcoded path works only on the original author's computer.
Anyone else who runs the code will get a FileNotFoundError unless they happen to have a file at exactly that path.
Reproducibility requires that the path either be relative to the notebook location (so the data file can be placed next to the notebook) or configurable by the user.
The reviewer is right to flag this as a reproducibility failure.

</details>

## Exercises

### Record the Environment

Add a cell at the top of your Alert CO2 notebook that prints the version of Python, Polars, and Altair being used.
Share the notebook with a classmate.
Ask them to run it and compare the version numbers to yours.

### Add a Trend Line

Ask the LLM to add a linear trend line to the Alert CO2 chart.
What is the slope in ppm per year?
Compare your slope to the rate of increase reported in the ECCC documentation.

### Seasonal Amplitude

The seasonal oscillation in the Alert CO2 record gets slightly larger over time.
Ask the LLM to compute the amplitude (maximum minus minimum CO2 within each year) for each year.
Plot the amplitude over time and describe the trend.

### Two-Run Comparison

Run the notebook twice, saving the output chart each time as `alert_co2_run1.png` and `alert_co2_run2.png`.
Ask the LLM to write code that checks whether the two files are identical pixel-for-pixel.
Are they?

### Hardcoded Path

The following code reads the Alert CO2 data from an absolute path that only works on one computer.
Work with an LLM to replace it with a relative path so the script runs on any machine
where the data file sits next to the script.

[%inc path_bug.py %]

<details markdown="1">
<summary markdown="1">How do you know the fix worked?</summary>

Move the data file and script to a different folder and run the script from there.
If it runs without a `FileNotFoundError`, the path is now relative and portable.
A classmate should be able to run the script on their own machine without editing it.

</details>

### Sentinel Values Not Removed

The following code reads the CO2 data but forgets to treat `-999.99` as missing,
so the chart shows a dramatic downward spike that is not in the published figure.
Work with an LLM to add the missing filter and fix the chart.

[%inc sentinel_bug.py %]

<details markdown="1">
<summary markdown="1">How do you know the fix worked?</summary>

After fixing, the printed CO2 minimum should be around 330 ppm (the 1975 value),
not -999.99.
The chart should show a smooth rising curve with a seasonal oscillation and no downward spikes.

</details>

### Using a Variable Before It Is Defined

The following script crashes with a `NameError` on its first print statement.
Work with an LLM to explain why the error happens and reorder the lines to fix it.

[%inc order_bug.py %]

<details markdown="1">
<summary markdown="1">How do you know the fix worked?</summary>

The script should run from top to bottom without any errors.
After fixing, the CO2 range printed at the top should match the range computed at the bottom.
This error is the script-level equivalent of running notebook cells out of order.

</details>

### Recording the Environment

The following code reads and summarises the CO2 data but does not record
which versions of Python, Polars, and Altair were used.
Work with an LLM to extend it to print those version numbers.

[%inc version_extend.py %]

<details markdown="1">
<summary markdown="1">How do you know the addition is correct?</summary>

Run `pip show polars altair` in the terminal and compare the versions it reports
to the ones your script prints.
They should match exactly.

</details>
