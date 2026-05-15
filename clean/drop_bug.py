import polars as pl

df = pl.read_csv("collision_data.csv", null_values=["U", "Q", "N", "UU", "QQ", "NN"])
print(f"Rows before cleaning: {len(df)}")

df_clean = df.drop_nulls()
print(f"Rows after cleaning: {len(df_clean)}")

print("\nDistinct P_SEX values after cleaning:")
print(df_clean["P_SEX"].value_counts())
