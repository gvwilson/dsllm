import polars as pl

df = pl.read_csv("flow_data.csv")

print(f"Rows: {df.height}, Columns: {df.width}")
print()
print(df.schema)
print()
print(df.head(2))
