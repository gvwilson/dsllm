import polars as pl
import altair as alt

df = pl.read_csv("earthquakes.csv", null_values=[""])
df = df.drop_nulls(subset=["depth", "magnitude", "region"])

chart = (
    alt.Chart(df)
    .mark_point(size=20)  # TODO: add opacity=0.4 so overlapping points are visible
    .encode(
        x=alt.X("depth:Q", title="Depth (km)"),
        y=alt.Y("magnitude:Q", title="Magnitude"),
        color=alt.Color("region:N", title="Region"),
    )
    .properties(title="Canadian Earthquakes: Depth vs. Magnitude",
                width=600, height=400)
)
chart.save("scatter.png")
print(f"Points in chart: {len(df)}")
