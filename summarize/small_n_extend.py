import polars as pl

T_CRIT = 1.96

df = pl.read_csv("contracts.csv")
df = df.with_columns(
    pl.col("contract_date").str.slice(0, 4).cast(pl.Int64).alias("year")
)

summary = (
    df.group_by(["department_en", "year"])
    .agg([
        pl.col("contract_value").mean().alias("mean"),
        pl.col("contract_value").count().alias("n"),
        pl.col("contract_value").std().alias("std"),
    ])
    .sort(["department_en", "year"])
    .with_columns([
        (pl.col("mean") - T_CRIT * pl.col("std") / pl.col("n").sqrt()).alias("ci_low"),
        (pl.col("mean") + T_CRIT * pl.col("std") / pl.col("n").sqrt()).alias("ci_high"),
    ])
)
print(summary.head(20))
# TODO: add a column "ci_reliable" that is True when n >= 5 and False otherwise,
# then print only the rows where ci_reliable is False
