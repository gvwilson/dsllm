import polars as pl

df = pl.read_csv("contracts.csv")

top_vendors = (
    df.group_by("department_en")
    .agg(pl.col("contract_value").sum().alias("total_value"))
    .sort("total_value", descending=True)
    .head(10)
)
print("Top 10 vendors by total contract value:")
print(top_vendors)
