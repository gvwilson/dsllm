import polars as pl

df = pl.read_csv("collision_data.csv", null_values=["U", "Q", "N", "UU", "QQ", "NN"])

province_counts = (
    df["C_PROV"]
    .value_counts()
    .sort("count", descending=True)
)
print(f"Distinct province values: {province_counts.height}")
print(province_counts)
