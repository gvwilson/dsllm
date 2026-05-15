import polars as pl

df = pl.read_csv("flow_data.csv")

station = df.filter(pl.col("Station_Number") == "02GA010")
print(f"Rows for station 02GA010: {len(station)}")
if len(station) > 0:
    print(f"Years covered: {station['YEAR'].min()} to {station['YEAR'].max()}")
else:
    print("No rows found.")
