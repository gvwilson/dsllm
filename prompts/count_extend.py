import polars as pl

LEAD_THRESHOLD = 1.0  # tonnes
LEAD_SUBSTANCE = "Lead (and its compounds)"

df = pl.read_csv("npri_data.csv", null_values=[""])

most_recent_year = df["Reporting_Year"].max()
df_lead = (
    df.filter(pl.col("Reporting_Year") == most_recent_year)
    .filter(pl.col("Substance_Name_English") == LEAD_SUBSTANCE)
    .drop_nulls(subset=["Total_Released_Tonnes"])
)

total = len(df_lead)
exceeds = df_lead.filter(pl.col("Total_Released_Tonnes") > LEAD_THRESHOLD).height
proportion = exceeds / total

print(f"Proportion exceeding {LEAD_THRESHOLD} t: {proportion:.3f}")
# TODO: also print exceeds and total so the reader can verify
# that proportion = exceeds / total
