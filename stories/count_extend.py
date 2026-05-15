import polars as pl
import altair as alt

df = pl.read_csv("eqao_school_results.csv", null_values=[""])

summary = (
    df.group_by(["board_type", "school_language"])
    .agg([
        pl.col("grade3_reading_pct").mean().alias("mean_reading"),
        pl.len().alias("n_schools"),
    ])
)

chart = (
    alt.Chart(summary)
    .mark_bar()
    .encode(
        x=alt.X("board_type:N", title="Board Type"),
        y=alt.Y("mean_reading:Q", title="Mean % at Level 3 or 4",
                scale=alt.Scale(domain=[0, 100])),
        column=alt.Column("school_language:N", title="School Language"),
        color=alt.Color("board_type:N", legend=None),
    )
    .properties(width=200, height=250)
)
chart.save("reading_chart.png")
print("Saved reading_chart.png")
# TODO: add a text mark showing n_schools on top of each bar
