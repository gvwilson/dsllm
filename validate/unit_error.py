import polars as pl

production = pl.read_csv("gas_production_tcm.csv")   # units: 10³ m³ (thousands)
consumption = pl.read_csv("gas_consumption_mcm.csv")  # units: 10⁶ m³ (millions)

# BUG: treats 10³ m³ and 10⁶ m³ as the same unit.
# The ratio will be off by a factor of 1 000.
ratio = production["production"].mean() / consumption["consumption"].mean()
print(f"Production-to-consumption ratio: {ratio:.4f}")
print("(This number is wrong if the units have not been converted.)")
