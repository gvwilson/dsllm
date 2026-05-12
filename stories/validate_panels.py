import polars as pl

df = pl.read_csv("eqao_school_results.csv", null_values=[""])

panel_counts = (
    df.group_by(["board_type", "school_language"])
    .agg([
        pl.len().alias("n_schools"),
        pl.col("grade3_reading_pct").mean().round(1).alias("mean_reading_pct"),
    ])
    .sort(["school_language", "board_type"])
)
print(panel_counts)
