import polars as pl

df = pl.read_csv("contracts.csv")
df = df.with_columns(
    pl.col("contract_date").str.slice(0, 4).cast(pl.Int64).alias("year")
)

summary = (
    df.select(pl.col("contract_value").sum())
    .group_by("department_en")
    .agg(pl.col("contract_value").mean().alias("mean"))
    .sort("department_en")
)
print(summary)
