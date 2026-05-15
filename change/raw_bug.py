import polars as pl

df = pl.read_csv("fluwatch.csv", null_values=[""])
df = df.with_columns(
    pl.col("ili_pct").cast(pl.Float64, strict=False),
    pl.col("year").cast(pl.Int64, strict=False),
)
df = df.drop_nulls(subset=["ili_pct", "year"])

x = df["year"].cast(pl.Float64)
y = df["ili_pct"]
slope = ((x - x.mean()) * (y - y.mean())).sum() / ((x - x.mean()) ** 2).sum()

print(f"Data points used: {len(df)}")
print(f"Trend line slope: {slope:.4f} percentage points per year")
if slope > 0:
    print("Direction: upward (flu becoming more severe on average)")
else:
    print("Direction: downward (flu becoming less severe on average)")
