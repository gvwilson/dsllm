import polars as pl

df = pl.read_csv("climate.csv", skip_rows=1, null_values=[""])
temps = df["Mean Temp (°C)"].drop_nulls()
print(f"Mean:   {temps.mean():.2f} °C")
print(f"Median: {temps.median():.2f} °C")
