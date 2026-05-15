import polars as pl

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

x = annual_peak["peak_ili"]
y = annual_peak["year"].cast(pl.Float64)
slope = ((x - x.mean()) * (y - y.mean())).sum() / ((x - x.mean()) ** 2).sum()
print(f"Trend line slope: {slope:.4f}")
if slope > 0:
    print("Direction: upward (flu peaks becoming more severe on average)")
else:
    print("Direction: downward (flu peaks becoming less severe on average)")
