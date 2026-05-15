import polars as pl
import altair as alt

df = pl.read_csv("eqao_school_results.csv", null_values=[""])
df = df.drop_nulls(subset=["grade3_reading_pct", "grade3_math_pct"])

chart = (
    alt.Chart(df)
    .mark_point(size=30, opacity=0.5)
    .encode(
        x=alt.X("grade3_reading_pct:Q", title="Grade 3 Reading (%)"),
        y=alt.Y("grade3_math_pct:Q", title="Grade 3 Math (%)"),
        color=alt.Color("grade3_reading_pct:N", title="Reading Score"),
    )
    .properties(title="Reading vs. Math by School",
                width=400, height=400)
)
chart.save("reading_math.png")
print("Saved reading_math.png")
