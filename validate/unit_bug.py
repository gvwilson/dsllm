import polars as pl

production = pl.read_csv("gas_production_tcm.csv")   # units: 10³ m³ (thousands)
consumption = pl.read_csv("gas_consumption_mcm.csv")  # units: 10⁶ m³ (millions)

ab_prod = production.filter(pl.col("province") == "AB")["production"].mean()
ab_cons = consumption.filter(pl.col("province") == "AB")["consumption"].mean()

ratio = ab_prod / ab_cons
print(f"Alberta mean annual production: {ab_prod:.1f}")
print(f"Alberta mean annual consumption: {ab_cons:.1f}")
print(f"Production-to-consumption ratio: {ratio:.4f}")
