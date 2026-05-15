import polars as pl

temps = pl.read_csv("ahccd_temp.csv", null_values=[""])
stations = pl.read_csv("ahccd_stations.csv", null_values=[""])

combined = temps.join(
    stations.select(["station_id", "province", "elevation_m"]),
    on="station_id",
    how="left",
)

mean_by_province = (
    combined.drop_nulls(subset=["mean_temp", "province"])
    .group_by("province")
    .agg(pl.col("mean_temp").mean().alias("mean_annual_temp"))
    .sort("mean_annual_temp")
)
print(mean_by_province)
# TODO: before printing mean_by_province, print how many temperature rows
# had a null province after the join, and print a sample of the unmatched
# station_id values so you can see why they did not match
