import polars as pl

df = pl.read_csv("collision_data.csv", null_values=["U", "Q", "N", "UU", "QQ", "NN"])

province_counts = (
    df.group_by("C_PROV")
    .agg(pl.len().alias("collisions"))
    .sort("collisions", descending=True)
)
print(province_counts)
# TODO: add a column showing collisions per 100,000 people using 2021 census population
# figures for each province, then re-sort by rate instead of raw count
