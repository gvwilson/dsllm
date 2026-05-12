import polars as pl

df = pl.read_csv("npri_data.csv", null_values=[""])
print("Column names:")
print(df.columns)
print("\nFirst row:")
print(df.head(1))
print("\nDistinct substance names (first 20):")
print(df["Substance_Name_English"].unique().sort().head(20))
