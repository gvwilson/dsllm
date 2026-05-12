import polars as pl

# 1 × 10⁶ m³ = 1 000 × 10³ m³
# Divide production (10³ m³) by 1 000 to convert to 10⁶ m³ before comparing.
TCM_TO_MCM = 1 / 1_000.0

production = pl.read_csv("gas_production_tcm.csv")
consumption = pl.read_csv("gas_consumption_mcm.csv")

production_mcm = production.with_columns(
    (pl.col("production") * TCM_TO_MCM).alias("production_mcm")
)

ratio = production_mcm["production_mcm"].mean() / consumption["consumption"].mean()
print(f"Production (mean, 10⁶ m³): {production_mcm['production_mcm'].mean():.1f}")
print(f"Consumption (mean, 10⁶ m³): {consumption['consumption'].mean():.1f}")
print(f"Ratio (production / consumption, same units): {ratio:.2f}")
