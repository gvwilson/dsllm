import polars as pl

LEAD_THRESHOLD = 1.0  # tonnes
LEAD_SUBSTANCE = "Lead (and its compounds)"

df = pl.read_csv("npri_data.csv", null_values=[""])

most_recent_year = df["Reporting_Year"].max()
df_year = df.filter(pl.col("Reporting_Year") == most_recent_year)
df_lead = df_year.filter(pl.col("Substance_Name_English") == LEAD_SUBSTANCE)
df_lead = df_lead.drop_nulls(subset=["Total_Released_Tonnes"])

all_facilities = df_year["NPRI_ID"].n_unique()
exceeds = df_lead.filter(pl.col("Total_Released_Tonnes") > LEAD_THRESHOLD).height
proportion = exceeds / all_facilities

print(f"Year: {most_recent_year}")
print(f"All facilities this year: {all_facilities}")
print(f"Lead-reporting facilities: {len(df_lead)}")
print(f"Facilities exceeding {LEAD_THRESHOLD} t: {exceeds}")
print(f"Proportion (of all facilities): {proportion:.4f}")
