import polars as pl

df = pl.read_csv("collision_data.csv", null_values=["U", "Q", "N", "UU", "QQ", "NN"])
print(df["P_SEX"].value_counts().sort("count", descending=True))
