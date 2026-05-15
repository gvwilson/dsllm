import polars as pl

df = pl.read_csv("flow_data.csv")

spread = df.select([
    pl.col("FLOW").mean().alias("mean"),
    pl.col("FLOW").std().alias("std_dev"),
    pl.col("FLOW").min().alias("minimum"),
    pl.col("FLOW").max().alias("maximum"),
])
print(spread)
