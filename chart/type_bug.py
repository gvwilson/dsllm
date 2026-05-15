import polars as pl
import altair as alt

df = pl.read_csv("earthquakes.csv", null_values=[""])
df = df.drop_nulls(subset=["magnitude"])

chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("magnitude", title="Magnitude"),
        y=alt.Y("count()", title="Number of Earthquakes"),
    )
    .properties(title="Earthquake Magnitude Distribution",
                width=400, height=300)
)
chart.save("magnitude_hist.png")
print(f"Rows in data: {len(df)}")
