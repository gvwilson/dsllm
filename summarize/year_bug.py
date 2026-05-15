import polars as pl

df = pl.read_csv("contracts.csv")
df = df.with_columns(
    pl.col("contract_date").str.to_date("%Y-%m-%d").dt.month().alias("year")
)

summary = (
    df.group_by(["department_en", "year"])
    .agg([
        pl.col("contract_value").sum().alias("total"),
        pl.col("contract_value").mean().alias("mean"),
    ])
    .sort(["department_en", "year"])
)
print(summary.head(20))
