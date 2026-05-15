import polars as pl

df = pl.read_csv("flow_data.csv", schema_overrides={"FLOW": pl.String})

print(f"FLOW column type: {df['FLOW'].dtype}")
print(f"Mean flow: {df['FLOW'].mean()}")
print(f"Max flow:  {df['FLOW'].max()}")
print(f"Min flow:  {df['FLOW'].min()}")
