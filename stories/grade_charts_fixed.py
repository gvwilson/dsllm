import polars as pl
import altair as alt

df = pl.read_csv("eqao_school_results.csv", null_values=[""])

chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("board_type:N", title="Board Type"),
        y=alt.Y("mean(grade3_reading_pct):Q",
                title="Mean % at Level 3 or 4 (Grade 3 Reading)",
                scale=alt.Scale(domainMin=0)),
        column=alt.Column("school_language:N", title="School Language"),
        color=alt.Color("board_type:N", legend=None),
        tooltip=["board_type", "school_language", "mean(grade3_reading_pct)"],
    )
    .properties(title="Mean Grade 3 Reading Score by Board Type and Language (y-axis from 0)",
                width=200, height=250)
)
chart.save("reading_chart_fixed.png")
print("Saved reading_chart_fixed.png")
