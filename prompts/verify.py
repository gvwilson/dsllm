import polars as pl

LEAD_THRESHOLD = 1.0
LEAD_SUBSTANCE = "Lead (and its compounds)"

df = pl.read_csv("npri_data.csv", null_values=[""])
most_recent_year = df["Reporting_Year"].max()

sample = (
    df.filter(
        (pl.col("Reporting_Year") == most_recent_year)
        & (pl.col("Substance_Name_English") == LEAD_SUBSTANCE)
    )
    .drop_nulls(subset=["Total_Released_Tonnes"])
    .select(["Facility_Name", "Province_Territory", "Total_Released_Tonnes"])
    .sort("Total_Released_Tonnes", descending=True)
    .head(20)
)
print(sample)
print(f"\nRows in this sample above {LEAD_THRESHOLD} tonne: "
      f"{sample.filter(pl.col('Total_Released_Tonnes') > LEAD_THRESHOLD).height}")
