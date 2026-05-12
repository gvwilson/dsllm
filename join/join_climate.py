import polars as pl

temps = pl.read_csv("ahccd_temp.csv", null_values=[""])
stations = pl.read_csv("ahccd_stations.csv", null_values=[""])

combined = temps.join(
    stations.select(["station_id", "province", "elevation_m"]),
    on="station_id",
    how="left",
)
print(combined.head())
