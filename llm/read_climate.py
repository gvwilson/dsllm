import polars as pl

df = pl.read_csv("climate.csv", skip_rows=1, null_values=[""])
print(df.head())
