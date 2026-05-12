import polars as pl

df = pl.read_csv("collision_data.csv", null_values=["U", "Q", "N", "UU", "QQ", "NN"])

missing = (
    df.null_count()
    .transpose(include_header=True, header_name="column", column_names=["missing"])
    .filter(pl.col("missing") > 0)
    .sort("missing", descending=True)
)
print(missing)
