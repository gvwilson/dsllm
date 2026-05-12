import polars as pl

df = pl.read_csv("earthquakes.csv", null_values=[""])
df = df.drop_nulls(subset=["depth", "magnitude"])

r = df.select(pl.corr("depth", "magnitude")).item()
print(f"Correlation between depth and magnitude: {r:.3f}")
print(f"(computed from {len(df)} earthquakes with both values present)")
