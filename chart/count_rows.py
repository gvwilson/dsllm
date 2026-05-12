import polars as pl

df = pl.read_csv("earthquakes.csv", null_values=[""])
print(f"Total rows in file: {len(df)}")

df_plot = df.drop_nulls(subset=["depth", "magnitude"])
print(f"Rows with both columns present: {len(df_plot)}")
print(f"Rows dropped: {len(df) - len(df_plot)}")
