import polars as pl
from scipy import stats

TCM_TO_MCM = 1 / 1_000.0

production = pl.read_csv("gas_production_tcm.csv")
production = production.with_columns(
    (pl.col("production") * TCM_TO_MCM).alias("production_mcm")
)

print(f"Distinct province values: {sorted(production['province'].unique().to_list())}")

alberta = production.filter(pl.col("province") == "Alberta")["production_mcm"].to_numpy()
bc = production.filter(pl.col("province") == "British Columbia")["production_mcm"].to_numpy()

print(f"Alberta rows: {len(alberta)}, BC rows: {len(bc)}")

result = stats.ttest_ind(alberta, bc, equal_var=False)
print(f"t-statistic: {result.statistic:.3f}")
print(f"p-value:     {result.pvalue:.4f}")
