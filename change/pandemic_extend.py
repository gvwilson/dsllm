import polars as pl

PANDEMIC_YEAR = 2009

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

x = annual_peak["year"].cast(pl.Float64)
y = annual_peak["peak_ili"]
slope = ((x - x.mean()) * (y - y.mean())).sum() / ((x - x.mean()) ** 2).sum()
print(f"Slope (all years): {slope:.4f} percentage points per year")
# TODO: refit the slope after removing PANDEMIC_YEAR from annual_peak,
# then print both slopes so the reader can compare them
