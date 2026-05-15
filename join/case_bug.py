import polars as pl

temps = pl.read_csv("ahccd_temp.csv", null_values=[""])
stations = pl.read_csv("ahccd_stations.csv", null_values=[""])

combined = temps.join(
    stations.select(["station_id", "province", "elevation_m"]),
    left_on="Station_ID",
    right_on="station_id",
    how="left",
)
null_province = combined["province"].null_count()
print(f"Rows with null province: {null_province} of {combined.height}")
print(combined.head())
