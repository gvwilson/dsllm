import polars as pl

LEAD_THRESHOLD = 10.0  # tonnes
LEAD_SUBSTANCE = "Lead (and its compounds)"

df = pl.read_csv("npri_data.csv", null_values=[""])

most_recent_year = df["Reporting_Year"].max()
df_year = df.filter(pl.col("Reporting_Year") == most_recent_year)
df_lead = df_year.filter(pl.col("Substance_Name_English") == LEAD_SUBSTANCE)
df_lead = df_lead.drop_nulls(subset=["Total_Released_Tonnes"])

total = len(df_lead)
exceeds = df_lead.filter(pl.col("Total_Released_Tonnes") > LEAD_THRESHOLD).height
proportion = exceeds / total

print(f"Year: {most_recent_year}")
print(f"Facilities reporting lead: {total}")
print(f"Facilities exceeding threshold: {exceeds}")
print(f"Proportion: {proportion:.3f}")
