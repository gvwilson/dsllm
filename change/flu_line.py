import polars as pl
import altair as alt

df = pl.read_csv("fluwatch.csv", null_values=[""])
df = df.with_columns(
    pl.col("ili_pct").cast(pl.Float64, strict=False)
)
df = df.drop_nulls(subset=["ili_pct"])

chart = (
    alt.Chart(df)
    .mark_line(opacity=0.6, strokeWidth=1)
    .encode(
        x=alt.X("week:O", title="Week of Year"),
        y=alt.Y("ili_pct:Q", title="ILI (% of physician visits)"),
        color=alt.Color("year:N", title="Year", legend=None),
        tooltip=["year", "week", "ili_pct"],
    )
    .properties(title="Weekly Influenza-Like Illness Percentage — Canada (FluWatch)",
                width=700, height=300)
)
chart.save("flu_line.png")
print("Saved flu_line.png")
