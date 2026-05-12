# Conclusion

## Goals

-   Review the workflow built across twelve sessions.
-   Know where to find help when an LLM fails.
-   Make an informed choice about when to use LLM tools and when not to.
-   Identify the next skills worth learning.

## The Workflow You Built

*Look back at the code and charts you produced over twelve sessions. What steps appear in every session?*

-   Every session followed the same loop, even when the dataset and question changed:
    -   Write a prompt that describes the data, the goal, and any constraints
    -   Paste the LLM's code into a notebook cell and run it
    -   Check whether the output is plausible before trusting it
    -   Iterate: ask the LLM to fix what is wrong, or adjust the prompt and try again
    -   Produce a chart or table and verify it against the raw data
-   The loop looks simple, but the judgment inside each step takes practice
    -   Knowing what counts as "plausible" requires knowing the domain
    -   Knowing how to check output requires knowing what could go wrong
    -   Knowing when to stop iterating requires knowing what "good enough" looks like for your question
-   Sessions 1 through 6 asked you to focus on prompting and interpreting
-   Sessions 7 through 12 asked you to read the code well enough to catch errors
    -   You do not need to write code from scratch to be a competent data scientist
    -   You do need to understand what the code is doing well enough to know when it is wrong

## When LLMs Fail

*What do I do when the LLM produces code that crashes, or code that runs but gives the wrong answer?*

-   When the code crashes, the error message is your first clue
    -   Copy the error message into a new prompt: "I got this error: [paste]. What is wrong?"
    -   Most errors have a standard fix; the LLM has seen them many times
    -   If the LLM's fix crashes too, read the error message yourself before prompting again
-   When the code runs but produces a suspicious result, the LLM is the wrong tool to ask
    -   Checking output is your job, not the LLM's
    -   The strategies from [session 11](@/validate/): check a known row by hand, compare to a published figure, ask "what units did you assume?"
-   When the LLM cannot help, other resources can:
    -   The official documentation for Polars, Altair, and Python is free, current, and accurate [%b polars2025 %] [%b altair2025 %]
    -   Stack Overflow has answered most beginner questions many times; look for answers with many upvotes and recent dates
    -   A colleague who codes is often the fastest path to a correct answer

## The Environmental and Labor Costs

*Given everything this course has covered, how should I decide when to use an LLM?*

-   The energy cost of a single query is small; the aggregate cost of millions of queries is not [%b strubell2019 %]
    -   Using an LLM to automate a repetitive, well-understood step is a reasonable use of that energy
    -   Using an LLM to avoid thinking about your data is not
-   The people whose writing trained these models were not compensated for that use
    -   This is an ongoing legal and ethical debate, not a resolved one
    -   Being aware of it is the beginning of making informed choices
-   The deskilling risk is real but not inevitable
    -   Every session in this course asked you to interpret the output yourself
    -   If you have been doing that, you have been building skills, not losing them
    -   If you have been copying results without reading them, review the sessions where you did not check the output

## Where to Go Next

*What should I learn after finishing this course?*

-   More statistics: this course introduced mean, median, correlation, regression, confidence intervals, and hypothesis testing
    -   A next step is understanding when each is appropriate and what the assumptions behind them are
    -   A good free resource is the OpenIntro Statistics textbook [%b openintro2019 %]
-   Reproducible research workflows: notebooks are a start, but projects with many collaborators need more
    -   Version control with [Git][git] tracks who changed what and when
    -   Environments managed with uv or conda ensure that someone else can re-run your analysis on their machine
-   More Python: this course asked you to read code, not write it
    -   If you want to modify code or write your own analyses, a Python fundamentals course is a natural next step
    -   Software Carpentry offers free, research-focused Python lessons [%b swc-python2024 %]
-   Machine learning: once you can produce honest descriptive statistics, you can ask whether a model generalizes
    -   Machine learning without the foundations in this course produces models whose errors you cannot diagnose

## Check Understanding

<details markdown="1">
<summary markdown="1">A colleague says "I don't need to check the LLM's output because it's always right for standard tasks." What is the flaw in this reasoning, and how would you explain it?</summary>

The LLM produces plausible text, not correct answers.
For standard tasks it is right most of the time,
which is what makes unchecked errors dangerous:
they look like correct output.
A unit error, a wrong column name, or a dropped null
can all produce results that appear reasonable without a sanity check.
The right approach is to check every result against something the LLM did *not* generate,
such as a known row or a manual calculation.

</details>

<details markdown="1">
<summary markdown="1">You want to share your analysis with a collaborator so they can re-run it. List three things they will need, and one thing that can silently break even when all three are present.</summary>

They need: the data file, the notebook (with all cells run in order), and the same software versions (Polars, Altair, Python).
Something that can silently break: if the data file is updated by its source (many government datasets are refreshed regularly),
re-running the notebook will produce different results even with identical code.
Record the date you downloaded the data and, if possible, save a copy alongside the notebook.

</details>

<details markdown="1">
<summary markdown="1">Explain the difference between statistical significance and practical significance, using an example from any session in this course.</summary>

Statistical significance means the result is unlikely to have arisen by chance given the sample size.
Practical significance means the effect is large enough to matter in the real world.
From session 11: a unit error can inflate numbers by a factor of nearly 300, making a trivial difference appear highly significant.
A result can be statistically significant (p-value well below 0.05) and practically meaningless,
or practically large and statistically insignificant if the sample is small.
Both kinds of significance matter; neither alone is enough.

</details>

<details markdown="1">
<summary markdown="1">What is one question from your own field that you could now answer with the tools from this course, and one that you could not? Explain the difference.</summary>

Answers will vary.
A question this course equips you to answer: "Do two groups in my dataset have different mean values, and is that difference larger than what chance would produce?"
A question it does not equip you to answer: "Will this model correctly classify new cases it has never seen?" (That requires machine learning, not just descriptive statistics.)
The difference is between describing what is in the data and predicting what is not yet in it.

</details>

## Exercises

### Write Your Own Methods Section

Take any analysis you produced in this course and write a methods section for it, as if you were submitting it to a journal.
Include the data source, the cleaning steps, the software used, and the statistical methods applied.

### Find a Retraction

Search for a published paper in your field that was retracted because of a data or statistical error.
Identify which step in the workflow introduced the error.
Describe what check from this course would have caught it.

### Teach It Back

Pick one statistical concept from this course (mean vs. median, confidence intervals, correlation vs. causation) and write a one-page explanation aimed at a first-year undergraduate with no statistics background.
Use an example that is not from this course.
