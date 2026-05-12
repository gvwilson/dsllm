import polars as pl

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

print(f"Rows after dropping missing: {len(df)}")
print(f"First year: {df['year'].min()}, Last year: {df['year'].max()}")
print(f"Most recent monthly average: {df['average'].tail(1).item():.2f} ppm")
