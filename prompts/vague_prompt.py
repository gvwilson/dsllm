import polars as pl

df = pl.read_csv("npri_data.csv", null_values=[""])

# The LLM invented "substance" and "lead_threshold" -- neither exists.
# This code will crash with KeyError: 'substance'
dangerous = df.filter(
    (pl.col("substance") == "lead") & (pl.col("lead_threshold") > 10)
)
print(f"Facilities releasing dangerous amounts of lead: {len(dangerous)}")
