import polars as pl

temps = pl.read_csv("ahccd_temp.csv", null_values=[""])
stations = pl.read_csv("ahccd_stations.csv", null_values=[""])

print(f"Temperature rows before join: {temps.height}")

combined = temps.join(
    stations.select(["station_id", "province", "elevation_m"]),
    on="station_id",
    how="left",
)
print(f"Rows after join: {combined.height}")

if combined.height > temps.height:
    print("WARNING: join multiplied rows. Check for duplicate station IDs.")
    dupes = (
        stations.group_by("station_id")
        .count()
        .filter(pl.col("count") > 1)
    )
    print(f"Stations with duplicate entries: {dupes.height}")
