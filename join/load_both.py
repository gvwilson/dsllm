import polars as pl

temps = pl.read_csv("ahccd_temp.csv", null_values=[""])
print("Temperature file columns:", temps.columns)
print(f"Temperature rows: {temps.height}")

stations = pl.read_csv("ahccd_stations.csv", null_values=[""])
print("\nStation file columns:", stations.columns)
print(f"Station rows: {stations.height}")
