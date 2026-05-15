import polars as pl

df = pl.read_csv("climate.csv", skip_rows=1, null_values=[""])
col = "Mean Temp (°C)"
temps = df[col].drop_nulls()
print(f"Mean:   {temps.mean():.2f} °C")
print(f"Median: {temps.median():.2f} °C")
# TODO: also print the minimum value, maximum value, and count of non-null observations
