# Introduction

## Goals

-   Understand what this course will teach and why it matters.
-   See how researchers actually use data science tools today.
-   Articulate what LLMs can and cannot do as coding assistants.

## What Is Data Science?

> What is data science, and how is it different from statistics or spreadsheet work?

-   [%g data-science "Data science" %] is the practice of turning messy observations into defensible claims
    -   Data from a hospital or a climate station always has missing values, typos, and inconsistent formatting
    -   Data science is the discipline of cleaning up those problems and then drawing statistical conclusions
-   Spreadsheets work well up to a few hundred rows; Python scripts handle millions without slowing down
-   A spreadsheet analysis is hard to share or re-run exactly; a script runs the same way every time
    -   When a collaborator asks "how did you get that number?", you send the script and the data
    -   When you come back to a project six months later, you can re-run the script from scratch
-   But writing a script is harder than clicking on a spreadsheet
    -   So we use LLMs to get started and help us learn

> What kind of work will this course prepare you to do?

-   By the end of this course you will be able to:
    -   Read a dataset from a file and understand its shape and contents
    -   Find and fix missing values and inconsistent categories
    -   Compute summary statistics and understand what they mean
    -   Make charts that honestly represent what the data show
    -   Join data from two separate files to answer a question neither answers alone
    -   Re-run an analysis from scratch and get the same result every time
-   Each session uses data from a different problem domain
    -   The skills are the same even though the domain changes
    -   This is intentional: data science is not a subject, it is a set of tools

## What LLMs Do

> What does an LLM do when I ask it to write Python code?

-   A [%g llm "large language model" %] (LLM) predicts the most plausible next word given everything before it
    -   It has no model of the world and does not reason about problems
    -   It produces text that resembles the answer to your question
        because it has seen thousands of similar questions and answers
-   This makes LLMs fast and useful for code that follows common patterns
    -   "Read a [%g csv "CSV" %] file and print the first five rows"
        appears thousands of times in public code repositories
    -   The LLM will produce something that works most of the time
-   LLMs also fail in specific and predictable ways:
    -   They invent column names that do not exist in your data
    -   They use library functions from older versions that have since changed
    -   They choose the wrong statistical approach without warning you
    -   They produce confident-sounding code that silently computes the wrong answer

> Why does it matter that LLMs do not actually understand data?

-   An LLM cannot look at your data file
    -   It can only see what you write in your prompt
    -   If you do not tell it the column names, it will invent them
-   An LLM does not know your research question
    -   If you ask for "the average" without specifying which average, it picks one
    -   If your data has outliers that distort the mean, the LLM will compute the mean anyway
-   The skills in this course exist because you cannot hand off research judgment to a language model
    -   You still need to know whether the answer is plausible
    -   You still need to know when the chart is misleading
    -   You still need to know which statistical test is appropriate

## The Costs of LLMs

> What are the environmental and labor costs of using LLM tools?

-   Training a large language model uses roughly as much electricity
    as flying a hundred passengers across the Atlantic [%b strubell2019 %]
    -   Running queries costs additional energy every time you use the tool
    -   Most of this energy comes from fossil fuels in most countries today
-   LLMs are built on text written by human researchers, journalists, and authors
    -   Legal and ethical questions about consent and compensation remain unresolved
    -   The people whose writing trained these models were not paid for that use
-   There is a real risk of [%g deskilling "deskilling" %]: if you never practice a skill, you lose it
    -   Using an LLM to avoid reading your own data is different from
        using one to automate a tedious step you understand
    -   This course asks you to use LLMs for the tedious steps and to do the thinking yourself

## What This Course Does Not Do

> What should I not use an LLM for in a research context?

-   LLMs should not interpret results for you
    -   "The correlation is 0.73, what does that mean for my study?" is a question only you can answer
    -   The LLM will produce plausible-sounding text that may have nothing to do with your data
-   LLMs should not choose your statistical methods
    -   The right test depends on the shape of your data, your sample size, and your research question
    -   This course teaches you enough to make those choices yourself
-   LLMs should not validate their own output
    -   Asking an LLM "did you do this correctly?" is like asking a student to grade their own exam
    -   Every result this course produces will be checked by a method the LLM did not generate

## Check Understanding

<details markdown="1">
<summary markdown="1">A classmate says LLMs "understand" data because they can write correct code. What is wrong with this claim, and what evidence would help you explain the difference?</summary>

LLMs predict plausible text based on patterns in their training data.
They produce code that looks correct because they have seen many similar examples,
not because they understand what the code does.
To prove this, ask an LLM a question about a dataset and include a false column name in the prompt.
The LLM will use that column name without questioning it, because it cannot see the data.

</details>

<details markdown="1">
<summary markdown="1">You ask an LLM to compute the average temperature in a dataset and it returns 2847.3. You expected a number between -30 and 45. List two things you would check before running the code again.</summary>

First, check whether the LLM used the correct column:
it may have computed the average of a year or station identifier instead of a temperature.
Second, check the units:
some temperature datasets store values in hundredths of a degree Celsius (so 2847 means 28.47)
or use Kelvin instead of Celsius.
Ask the LLM "what units did you assume for the temperature column?" before trusting any number.

</details>

<details markdown="1">
<summary markdown="1">Why is saving an analysis as a Python script more reproducible than saving it as a spreadsheet?</summary>

A Python script records every step:
which file was read, which rows were filtered, which formula was applied, in which order.
Anyone can re-run the script and get the same result.
A spreadsheet mixes data, formulas, and results in the same cells
, making it easy to overwrite a value without any record of the change,
and hard to verify that the visible numbers follow from the raw data.

</details>

<details markdown="1">
<summary markdown="1">Name one situation where using an LLM to write code is worth its environmental cost, and one where it probably is not.</summary>

Worth the cost:
automating a well-understood, repetitive task such as reading fifty CSV files in the same format
and combining them into one table.
Probably not worth it: asking an LLM to interpret what your results mean
or to decide which statistical test suits your research design,
because those are exactly the judgments you need to practice to become a competent researcher.

</details>

## Exercises

### Map the Workflow

Draw a flowchart of the prompt-check-run-interpret loop that this course uses in every session.
Label each step with one question you should ask yourself before moving to the next step.

### Find the Deskilling Risk

Think of one task you already use an LLM for regularly,
such as searching for references, summarizing papers, or writing emails.
Write a paragraph describing how you would do that task without the LLM for one week,
and what you expect you would notice.

### Read a Methods Section

Find a published paper in your field that includes a "data analysis" or "methods" section.
Write down every software tool, cleaning step, or statistical procedure the authors mention.
Identify one step where an LLM could have helped,
and one where relying on it uncritically could have introduced an error.
