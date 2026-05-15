import polars as pl
from scipy import stats

TCM_TO_MCM = 1 / 1_000.0

production = pl.read_csv("gas_production_tcm.csv")
production = production.with_columns(
    (pl.col("production") * TCM_TO_MCM).alias("production_mcm")
)

alberta = production.filter(pl.col("province") == "AB")["production_mcm"].to_numpy()
bc = production.filter(pl.col("province") == "BC")["production_mcm"].to_numpy()

result = stats.ttest_ind(alberta, bc, equal_var=False, alternative="greater")
print(f"t-statistic: {result.statistic:.3f}")
print(f"p-value:     {result.pvalue:.4f}")

if result.pvalue < 0.05:
    print("Result: statistically significant at the 0.05 level.")
else:
    print("Result: not statistically significant at the 0.05 level.")
