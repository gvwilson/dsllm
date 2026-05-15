import polars as pl

temps = pl.read_csv("ahccd_temp.csv", null_values=[""])
stations = pl.read_csv("ahccd_stations.csv", null_values=[""])

print(f"Temperature rows: {len(temps)}")

combined = temps.join(
    stations.select(["station_id", "province", "elevation_m"]),
    on="station_id",
    how="left",
)
print(f"Combined rows: {len(combined)}")
# TODO: check whether any station_id appears more than once in the stations file;
# if combined has more rows than temps, duplicates in stations are the cause
