import polars as pl

df = pl.read_csv("flow_data.csv")
df = df.filter(pl.col("FLOW").is_not_null() & (pl.col("FLOW") < 50_000))

station_stats = (
    df.group_by("STATION_NUMBER")
    .agg([
        pl.col("FLOW").mean().alias("mean_flow"),
        pl.col("FLOW").std().alias("std_flow"),
    ])
    .sort("std_flow", descending=True)
)
print(station_stats.head(10))
# TODO: add a column "cv" (coefficient of variation) equal to std_flow / mean_flow,
# then re-sort by cv descending and print the top 10
