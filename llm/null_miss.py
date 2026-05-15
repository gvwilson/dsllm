import polars as pl

df = pl.read_csv("climate.csv", skip_rows=1)
print(f"Temperature column type: {df['Mean Temp (°C)'].dtype}")
temps = df["Mean Temp (°C)"].drop_nulls()
print(f"Non-null rows: {len(temps)}")
print(f"Mean:   {temps.mean()}")
print(f"Median: {temps.median()}")
