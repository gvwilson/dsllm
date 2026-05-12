# 2026-05-12 01:30 — Replace US Datasets with Canadian Datasets

## Prompts

1.  These data sets are largely from the US. Replace them with Canadian datasets.

## Actions

Updated all 11 session lesson files and their Python code files to use Canadian open data sources:

-   **llm**: ECCC Historical Climate Data (`climate.weather.gc.ca`) replacing GISTEMP; file `climate.csv`; column `Mean Temp (°C)`; deleted `read_temps.py`, rewrote `read_climate.py` and `mean_median.py`
-   **chart**: NRCan Earthquake Catalog (`earthquakescanada.nrcan.gc.ca`) replacing NASA Exoplanet Archive; file `earthquakes.csv`; columns `date`, `depth`, `magnitude`, `region`; rewrote `scatter.py`
-   **clean**: Transport Canada NCDB (`open.canada.ca`) replacing UCI Diabetes; file `collision_data.csv`; coded unknowns (`U`, `Q`, `N`, etc.); deleted `check_gender.py`, rewrote `normalize.py` and `check_sex.py`
-   **summarize**: Government of Canada Contracts (`open.canada.ca`) replacing Chicago Budget; file `contracts.csv`; columns `department_en`, `contract_date`, `contract_value`, `vendor_name`; rewrote `group_spend.py`
-   **tables**: ECCC HYDAT Streamflow (`canada.ca`) replacing USGS BBS; file `flow_data.csv`; columns `STATION_NUMBER`, `STATION_NAME`, `YEAR`, `MONTH`, `FLOW`; deleted `describe_birds.py` and `spread_birds.py`; rewrote `describe_flow.py` and `spread_flow.py`
-   **prompts**: ECCC NPRI (`canada.ca`) replacing USGS Geochemical Survey; file `npri_data.csv`; substance `Lead (and its compounds)`; rewrote `lead_prop.py`
-   **change**: PHAC FluWatch (`canada.ca`) replacing CDC FluView; file `fluwatch.csv`; columns `week`, `year`, `region`, `ili_pct`; rewrote `trend_flu.py` and `seasonal_flu.py`
-   **join**: ECCC AHCCD (`canada.ca`) replacing NOAA GHCN-D; files `ahccd_temp.csv` + `ahccd_stations.csv`; join key `station_id`; deleted `mean_by_zone.py`; rewrote `join_climate.py` and `mean_by_province.py`
-   **stories**: EQAO Ontario School Results replacing UCI Student Performance; file `eqao_school_results.csv`; columns include `board_type`, `school_language`, `grade3_reading_pct`, `grade3_math_pct`; rewrote `grade_charts.py`
-   **validate**: Canada Energy Regulator data replacing EIA Monthly Energy Review; files `gas_production_tcm.csv` (10³ m³) + `gas_consumption_mcm.csv` (10⁶ m³); unit error factor of 1,000; rewrote `unit_fix.py` and `ttest.py`
-   **repro**: ECCC Alert Station CO2 (`canada.ca`) replacing NOAA Mauna Loa; file `alert_co2_monthly.csv`; Alert, Nunavut 82.5°N, continuous since 1975; deleted `keeling.py`; rewrote `alert_co2.py` and `rerun_check.py`

Updated reference files to remove all US dataset entries:

-   **bibliography/index.md**: removed `bbs2025`, `cdc-fluview2025`, `chicago-budget2025`, `eia-mer2025`, `exoplanet2025`, `gistemp2025`, `noaa-co22025`, `noaa-ghcnd2025`, `uci-diabetes2014`, `uci-student2014`, `usgs-geochem2025`; added `ahccd2025`, `alert-co22025`, `cer2025`, `eccc-climate2025`, `eqao2025`, `fluwatch2025`, `gc-contracts2025`, `hydat2025`, `ncdb2025`, `npri2025`, `nrcan-quakes2025`
-   **_extras/links.md**: replaced all US dataset link keys with Canadian equivalents: `eccc-climate`, `nrcan-quakes`, `ncdb`, `gc-contracts`, `hydat`, `npri`, `fluwatch`, `ahccd`, `eqao`, `cer`, `eccc-alert`
-   **outline.txt**: updated all Dataset lines to reference Canadian sources
