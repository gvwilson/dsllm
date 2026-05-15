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
    null_values=["-999.99", "-1"],
)
df = df.drop_nulls(subset=["average"])

print(f"Rows: {len(df)}, Date range: {df['year'].min()}\u2013{df['year'].max()}")
print(f"CO\u2082 range: {df['average'].min():.1f}\u2013{df['average'].max():.1f} ppm")
# TODO: print the versions of Python, Polars, and Altair being used,
# so that anyone re-running this analysis can confirm they have the same environment
