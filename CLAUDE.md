# Claude

This project is an introduction to data science for researchers who
have no previous programming experience, and have never used command
line tools.

## Audience

Learners have completed the first two years of an undergraduate
degree. They wrote a little bit of Python in high school, but haven't
used it since.  They do *not* want to become software engineers: they
regard programming as a means to an end.  They want to create charts
and have confidence in their results.

Learners frequently use LLM tools like Claude to summarize documents
or write first drafts of emails, to solve homework problems, or in
place of search engines. They do not understand how such tools work;
they are nervous that these tools are going to deskill or eliminate
research jobs, and are very concerned about the social and
environmental impact of these tools in general.

## Content

-   Each lesson should take one hour to complete, including exercises.
    When in doubt, go slowly.
-   Each lesson is built around a separate small example, each drawn
    from a different problem domain. Examples can rely on high school
	level science, but nothing more.
-   Define new terms using the `%g` shortcode and add definitions to
    `./glossary/index.md`.
-   Each lesson is in its own subdirectory, whose name is a one-word
    descriptive slug. Lessons are included in the `Lessons` section
    of `README.md` in order (see `intro` and `finale` for format).
-   Each lesson has an `index.md` file with an H1 title followed by
    sections with H2 titles.
-   Lesson content in each section is written as point-form lists
    using four-space indentation. *NEVER* put tab characters in files.
    Point-form lists may include sub-lists, but only one level deep.
-   The first H2 in each lesson is `Goals`, which is followed by a
    point-form list of the goals of that lesson. Do not wrap new terms
    in this section in glossary references, but make sure that all new
    terms mentioned here are defined in the lesson.
-   Each H2 title is a short description of the next thing to be added
    to the running example. This is followed by at least two italicized
    prompts for an LLM. Each prompt either asks a question or tells the
    LLM to do the next step in the running example. Prompts are given
    directly, without any prefix such as "Ask an LLM", and are not in
    quotes. The point-form content is split between the prompts, with
    each prompt followed by the bullets that describe what the LLM does
    in response to that prompt, along with excerpts of generated code.
-   Do not introduce a concept, tag, or feature until the running
    example actually needs it. If you cannot point to a specific place
    in the example where the new material is required, leave it for a
    later lesson.
-   Start examples with the simplest structure that illustrates the
    concept and build complexity progressively. For example, introduce
    a paragraph and a list before introducing a table.
-   Code is put in files in the lesson directory. These files are
    transcluded in the lesson using mccole's `%inc` tag. The shell
    command to run the code (if needed) is put in a `.sh` file in the
    lesson directory, which is also transcluded in the lesson.
-   The penultimate section of each lesson is an H2 titled `Check
    Understanding`. The content underneath this is a series of 3-5
    questions for learners to answer *without* using an LLM. At least
    one question must ask the learner to diagnose and fix a bug rather
    than simply recall or distinguish concepts. Each question is written
    as `<details markdown="1">`, followed by
    `<summary markdown="1">text of question</summary>` on a line of
    its own, followed by a blank line, followed by a paragraph answer
    and/or snippets of code, followed by a blank line, followed by
    `</details>`.
-   The final section of each lesson is an H2 titled `Exercises`. It
    is followed by 3-5 exercises, each of which has a brief H3 title
    followed by a paragraph describing the goal of the exercise.
-   Citations must be to free, actively maintained resources such as
    official documentation or MDN. Only cite a book if it covers
    something the online references do not, and verify that it is no
    more than a few years old before recommending it.

## Style Rules

-   *NEVER* use `---` as dashes in prose.
-   Callouts are written as `<div class="callout" markdown="1">`
    followed by an H3 header, prose content, and `</div>`. Use
    callouts sparingly for warnings or important asides.
-   Each lesson directory must be self-contained and not depend on
    files in other lesson directories, unless the lessons are
    explicitly ordered and one lesson builds directly on the previous
    one.
-   Always use lowercase for SQL keywords (e.g., `select`, `from`,
    `where`, `insert into`, `create table`). Never use uppercase SQL
    keywords.

## Stack

-   [bash](https://www.gnu.org/software/bash/): Unix shell
-   [git](https://git-scm.com/): version control
-   [uv](https://docs.astral.sh/uv/): package and environment management
-   [polars](https://pola.rs/): dataframes
-   [Vega-Altair](https://altair-viz.github.io/): charts
-   [SQLite](https://sqlite.org/): database
-   [ruff](https://astral.sh/ruff): linting
-   [taskipy](https://github.com/taskipy/taskipy): task runner

@~/.claude/mccole.md
