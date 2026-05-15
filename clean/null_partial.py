import polars as pl

df = pl.read_csv("collision_data.csv", null_values=["U"])

missing = (
    df.null_count()
    .transpose(include_header=True, header_name="column", column_names=["missing"])
    .filter(pl.col("missing") > 0)
    .sort("missing", descending=True)
)
print(missing)
print(f"\nDistinct C_WTHR values: {sorted(df['C_WTHR'].drop_nulls().unique().to_list())}")
