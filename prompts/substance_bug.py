import polars as pl

LEAD_THRESHOLD = 1.0  # tonnes
LEAD_SUBSTANCE = "lead (and its compounds)"

df = pl.read_csv("npri_data.csv", null_values=[""])

most_recent_year = df["Reporting_Year"].max()
df_year = df.filter(pl.col("Reporting_Year") == most_recent_year)
df_lead = df_year.filter(pl.col("Substance_Name_English") == LEAD_SUBSTANCE)

print(f"Rows matching substance filter: {len(df_lead)}")
print(f"Distinct substances in full dataset (sample):")
print(df["Substance_Name_English"].unique().sort().head(10))
