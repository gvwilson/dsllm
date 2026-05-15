import polars as pl
import altair as alt

COLUMN_NAMES = [
    "year", "month", "decimal_date", "average",
    "deseasonalized", "ndays", "std_dev", "uncertainty",
]

df = pl.read_csv(
    "/Users/alice/Desktop/alert_co2_monthly.csv",
    comment_prefix="#",
    has_header=False,
    new_columns=COLUMN_NAMES,
    null_values=["-999.99", "-1"],
)
df = df.drop_nulls(subset=["average"])

print(f"Rows: {len(df)}, CO\u2082 range: {df['average'].min():.1f}\u2013{df['average'].max():.1f} ppm")
