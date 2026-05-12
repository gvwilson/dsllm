import polars as pl

df = pl.read_csv("collision_data.csv", null_values=["U", "Q", "N", "UU", "QQ", "NN"])
print(f"Rows before cleaning: {len(df)}")

print("\nDistinct P_SEX values after null coding:")
print(df["P_SEX"].value_counts().sort("count", descending=True))

df_clean = df.drop_nulls(subset=["P_SEX"])
print(f"\nRows after dropping null P_SEX: {len(df_clean)}")
