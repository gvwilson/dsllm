import polars as pl
import altair as alt

COLUMN_NAMES = [
    "year", "month", "decimal_date", "average",
    "deseasonalized", "ndays", "std_dev", "uncertainty",
]

df = pl.read_csv(
    "alert_co2_monthly.csv",
    comment_prefix="#",
    has_header=False,
    new_columns=COLUMN_NAMES,
    null_values=[""],
)

print(f"Rows: {len(df)}")
print(f"CO\u2082 min: {df['average'].min():.2f}, max: {df['average'].max():.2f}")

chart = (
    alt.Chart(df.drop_nulls(subset=["average"]))
    .mark_line(color="steelblue", strokeWidth=1)
    .encode(
        x=alt.X("decimal_date:Q", title="Year"),
        y=alt.Y("average:Q", title="CO\u2082 Concentration (ppm)"),
    )
    .properties(title="Atmospheric CO\u2082 at Alert Station", width=700, height=350)
)
chart.save("alert_co2.png")
print("Saved alert_co2.png")
