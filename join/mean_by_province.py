import polars as pl

temps = pl.read_csv("ahccd_temp.csv", null_values=[""])
stations = pl.read_csv("ahccd_stations.csv", null_values=[""])

combined = temps.join(
    stations.select(["station_id", "province", "elevation_m"]),
    on="station_id",
    how="left",
)

mean_by_province = (
    combined.drop_nulls(subset=["temp_mean", "province"])
    .group_by("province")
    .agg([
        pl.col("temp_mean").mean().alias("mean_temp_c"),
        pl.col("temp_mean").count().alias("n_readings"),
    ])
    .sort("mean_temp_c", descending=True)
)
print(mean_by_province)
