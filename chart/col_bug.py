import polars as pl
import altair as alt

df = pl.read_csv("earthquakes.csv", null_values=[""])
df = df.drop_nulls(subset=["depth", "magnitude"])

chart = (
    alt.Chart(df)
    .mark_point(opacity=0.4, size=20)
    .encode(
        x=alt.X("depth:Q", title="Depth (km)"),
        y=alt.Y("Magnitude:Q", title="Magnitude"),
    )
    .properties(title="Canadian Earthquakes: Depth vs. Magnitude",
                width=600, height=400)
)
chart.save("scatter.png")
print(f"Points in chart: {len(df)}")
