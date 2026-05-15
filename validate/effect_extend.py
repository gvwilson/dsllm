import polars as pl
import numpy as np
from scipy import stats

TCM_TO_MCM = 1 / 1_000.0

production = pl.read_csv("gas_production_tcm.csv")
production = production.with_columns(
    (pl.col("production") * TCM_TO_MCM).alias("production_mcm")
)

alberta = production.filter(pl.col("province") == "AB")["production_mcm"].to_numpy()
bc = production.filter(pl.col("province") == "BC")["production_mcm"].to_numpy()

result = stats.ttest_ind(alberta, bc, equal_var=False)
print(f"t-statistic: {result.statistic:.3f}")
print(f"p-value:     {result.pvalue:.4f}")
# TODO: compute Cohen's d = (mean_alberta - mean_bc) / pooled_std,
# where pooled_std = sqrt((std_alberta**2 + std_bc**2) / 2),
# and print it alongside an interpretation (small < 0.2, medium 0.2–0.8, large > 0.8)
