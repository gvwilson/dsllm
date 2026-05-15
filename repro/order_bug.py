import polars as pl

COLUMN_NAMES = [
    "year", "month", "decimal_date", "average",
    "deseasonalized", "ndays", "std_dev", "uncertainty",
]

# This line uses df_clean before it is defined below.
print(f"CO\u2082 range: {df_clean['average'].min():.1f}\u2013{df_clean['average'].max():.1f} ppm")

df = pl.read_csv(
    "alert_co2_monthly.csv",
    comment_prefix="#",
    has_header=False,
    new_columns=COLUMN_NAMES,
    null_values=["-999.99", "-1"],
)
df_clean = df.drop_nulls(subset=["average"])
print(f"Rows after removing missing values: {len(df_clean)}")
