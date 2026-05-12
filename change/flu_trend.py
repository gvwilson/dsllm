import polars as pl
import altair as alt

df = pl.read_csv("fluwatch.csv", null_values=[""])
df = df.with_columns(
    pl.col("ili_pct").cast(pl.Float64, strict=False),
    pl.col("year").cast(pl.Int64, strict=False),
)
df = df.drop_nulls(subset=["ili_pct", "year"])

annual_peak = (
    df.group_by("year")
    .agg(pl.col("ili_pct").max().alias("peak_ili"))
    .sort("year")
)

base = alt.Chart(annual_peak)
points = base.mark_point(filled=True, size=60).encode(
    x=alt.X("year:Q", title="Year"),
    y=alt.Y("peak_ili:Q", title="Peak ILI (%)"),
    tooltip=["year", "peak_ili"],
)
trend = base.transform_regression("year", "peak_ili").mark_line(color="red")

chart = (points + trend).properties(
    title="Annual Peak Flu Season Severity with Trend Line — Canada",
    width=550, height=300,
)
chart.save("flu_trend.png")
print("Saved flu_trend.png")
