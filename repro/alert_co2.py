import polars as pl
import altair as alt

# Column order from ECCC Alert Station readme:
# year, month, decimal_date, average, deseasonalized,
# ndays, std_dev, uncertainty. Missing values are -999.99.
COLUMN_NAMES = [
    "year", "month", "decimal_date", "average",
    "deseasonalized", "ndays", "std_dev", "uncertainty",
]

df = pl.read_csv(
    "alert_co2_monthly.csv",
    comment_prefix="#",
    has_header=False,
    new_columns=COLUMN_NAMES,
    null_values=["-999.99", "-1"],
)
df = df.drop_nulls(subset=["average"])

chart = (
    alt.Chart(df)
    .mark_line(color="steelblue", strokeWidth=1)
    .encode(
        x=alt.X("decimal_date:Q", title="Year"),
        y=alt.Y("average:Q", title="CO\u2082 Concentration (ppm)"),
        tooltip=["year", "month", "average"],
    )
    .properties(
        title="Atmospheric CO\u2082 at Alert Station, Nunavut",
        width=700,
        height=350,
    )
)
chart.save("alert_co2.png")
print(f"Saved alert_co2.png")
print(f"Rows: {len(df)}, Date range: {df['year'].min()}\u2013{df['year'].max()}")
print(f"CO\u2082 range: {df['average'].min():.1f}\u2013{df['average'].max():.1f} ppm")
