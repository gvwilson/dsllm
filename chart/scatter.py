import polars as pl
import altair as alt

df = pl.read_csv("earthquakes.csv", null_values=[""])
df = df.drop_nulls(subset=["depth", "magnitude", "region"])

chart = (
    alt.Chart(df)
    .mark_point(opacity=0.4, size=20)
    .encode(
        x=alt.X("depth:Q", title="Depth (km)"),
        y=alt.Y("magnitude:Q", title="Magnitude"),
        color=alt.Color("region:N", title="Region"),
        tooltip=["date", "depth", "magnitude", "region"],
    )
    .properties(title="Canadian Earthquakes: Depth vs. Magnitude",
                width=600, height=400)
)
chart.save("scatter.png")
print(f"Points in chart: {len(df)}")
