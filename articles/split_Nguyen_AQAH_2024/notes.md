# Reading Notes: Nguyen et al. (2024)

**Full citation:** Nguyen A, Ebisu K, Basu R, Schulte N, Epstein SA, Wu X. "Subdaily PM2.5 exposure and cardiorespiratory risks: data and findings from Southern California, 2018–2020." *Air Quality, Atmosphere & Health*. Published online May 13, 2024. https://doi.org/10.1007/s11869-024-01583-6

---

## 1. Research Question

Does measuring PM2.5 exposure at a subdaily (hourly) resolution capture additional cardiorespiratory health risk not detected by the standard daily average metric? Specifically: do "daily exceedance concentration hours" (DECH) — the sum of concentration-hours above a given threshold — predict emergency department visits (EDVs) differently than the 24-hour average? Are the risks heterogeneous across age, race/ethnicity, and neighborhood poverty?

**Why it matters:** Hourly monitoring is increasingly available. If subdaily peaks (wildfires, fireworks, industrial sources) drive health effects that daily averages miss, public health guidance and ambient air quality standards may need updating to incorporate subdaily metrics.

---

## 2. Audience

Air quality epidemiologists, OEHHA/EPA scientists, and policymakers evaluating whether hourly AQI guidance is sufficient protection. Particularly relevant to California air quality regulators.

**Note:** Three of the six authors (Wu, Ebisu, Basu) are OEHHA scientists — the same institution that requested the capstone. This paper and Chen et al. (2023) come from overlapping research groups using the same underlying EDV data source (HCAI).

---

## 3. Method

**Design:** Two-stage time-series analysis.

- **Stage 1:** Quasi-Poisson regression with distributed lag nonlinear models (DLNM, R package `dlnm`) run separately for each of 35 regional clusters. Outcome: daily EDV counts. Exposure: PM2.5 DECH metrics and daily average. Covariates: apparent temperature (3-day rolling average), weekend indicator, holiday indicator, log(cluster population), natural cubic spline for long-term trends.

- **Stage 2:** Cluster-specific estimates pooled using random-effects meta-analysis with maximum likelihood.

**DECH construction:** DECH-*k* = sum of (hourly concentration − *k*) for all hours where concentration > *k*, within a 24-hour day. Units: µg/m³·hour. Thresholds tested: 9 µg/m³ (current U.S. annual standard), 12 µg/m³ (former standard), 15 µg/m³ (WHO daily guideline).

**Lag structure:** 1, 3, 7, and 14 distributed lags tested. Optimal lag selected by minimizing qAIC: **7-day lag for cardiovascular, 3-day lag for respiratory**.

**Regionalization:** 465 ZCTAs → 455 after exclusions → 35 clusters using SKATER algorithm (R `spdep` package), minimizing total mean square error of sociodemographic similarity (race/ethnicity, poverty) while maximizing between-cluster PM2.5 variability. Minimum cluster population: 35,000.

---

## 4. Data

| Item | Detail |
|---|---|
| **Exposure** | Hourly PM2.5 from South Coast AQMD, May 2018–March 2020. Combines regulatory monitors + hundreds of PurpleAir sensors + CMAQ model output via kriging. ~5km × 5km grid. |
| **Geography** | South Coast AQMD jurisdiction: Orange County, most of LA County, most of Riverside County, SW San Bernardino County. |
| **Health outcomes** | Individual patient EDV records from California HCAI (Dept of Health Care Access and Information). ICD-10-CM primary diagnosis: respiratory (J00–J99) and cardiovascular (I00–I99). Daily counts aggregated to ZCTA, then cluster level. |
| **Unit of observation** | Cluster-day (35 clusters × 699 days) |
| **Time period** | May 2018–March 2020 |
| **Sample size** | 35 clusters; avg population 477,655/cluster; 699 exposure-outcome days/cluster |
| **Demographics** | ACS 2015–2019: proportion Black, Hispanic, household income < 2× FPL |
| **Mean EDV rates** | Cardiovascular: 4.9/100k/day; Respiratory: 10.7/100k/day |
| **Mean PM2.5** | Daily average: 11.2 µg/m³ (SD 5.6); DECH-9: 89.3 µg/m³·hr (SD 106.7) |

**Data availability:** Hourly PM2.5 available via Public Records Request from South Coast AQMD. EDV data via HCAI with an approved application. No public replication archive.

---

## 5. Statistical Methods

- **Quasi-Poisson regression** to handle over-dispersed count data
- **DLNM** (`dlnm` R package): crossbasis matrix for PM2.5 and lag simultaneously; linear exposure-response assumed (supported by prior evidence)
- Polynomial distributed lag functions: 1 d.f. for 1-day and 3-day lags, 2 d.f. for 7-day, 4 d.f. for 14-day
- **Natural cubic spline** for long-term trend: 5 d.f. (cardiovascular), 4 d.f. (respiratory), selected by qAIC
- **Random effects meta-analysis** (maximum likelihood) to pool cluster estimates
- **Stratified models** by age (0–17, 18–64, 65+), race/ethnicity (NHW vs. Hispanic), cluster poverty (low/moderate/high by Jenks breaks)
- **Sensitivity analyses:** co-pollutant adjustment with O3 (DECH-30) and NO2 (DECH-5, DECH-13)
- **Interaction test:** ratio of difference in risk ratios to their standard errors (Altman 2003)

---

## 6. Findings

### Primary results (excess risk per IQR increase, 95% CI)

**Cardiovascular EDVs (7-day lag):**

| Metric | IQR | Excess risk | 95% CI |
|---|---|---|---|
| DECH-9 | 110 µg/m³·hr | +1.77% | (1.20, 2.34) |
| DECH-12 | 65.8 µg/m³·hr | +1.04% | (0.61, 1.47) |
| Daily max | 10.4 µg/m³ | +1.89% | (1.21, 2.59) |
| **Daily average** | **6.8 µg/m³** | **+2.67%** | **(1.98, 3.37)** |

**Respiratory EDVs (3-day lag):**

| Metric | IQR | Excess risk | 95% CI |
|---|---|---|---|
| DECH-9 | 110 µg/m³·hr | +6.34% | (4.25, 8.48) |
| DECH-12 | 65.8 µg/m³·hr | +4.39% | (2.85, 5.95) |
| DECH-15 | 32.7 µg/m³·hr | +1.91% | (1.41, 2.41) |
| Daily max | 10.4 µg/m³ | +6.04% | (4.51, 7.60) |
| **Daily average** | **6.8 µg/m³** | **+6.61%** | **(4.78, 8.47)** |

**Bottom line:** DECH-9 and daily max track the daily average closely. DECH-12 and DECH-15 are attenuated (likely because 15–27% of observations were zero at those thresholds). **Subdaily metrics do not exceed daily average in effect size** for either outcome category.

### Subgroup findings

- **Older adults (65+):** Higher cardiovascular risk than adults 18–64 across all metrics. Differences statistically significant for DECH-9, DECH-12, and daily average.
- **Children (0–17):** Higher respiratory risk than adults across all metrics. Differences statistically significant for DECH metrics. Effect sizes smaller than daily average and daily max.
- **Race/ethnicity:** Slightly higher cardiovascular risk among NHW; slightly higher respiratory risk among Hispanic. Neither modification statistically significant. Age confounding likely explains the pattern (Hispanic patients averaged 23.4 years vs. 43.3 for NHW).
- **Poverty:** Low-poverty clusters showed higher cardiovascular risk for both adult groups (statistically significant). Authors attribute to better insurance coverage/healthcare access in high-SES areas, rather than lower exposure.
- **Sensitivity (co-pollutants):** PM2.5 cardiovascular associations robust to O3 and NO2 adjustment. NO2 **attenuated** PM2.5–respiratory associations across all metrics, suggesting traffic-related emissions partly explain respiratory EDVs.

### Novel finding on lag duration
Respiratory risks from subdaily metrics (DECH) persisted or slightly increased beyond 7 days, unlike daily average PM2.5 (which peaked at lag 7 and declined at lag 14). Suggests peak subdaily exposures may produce prolonged respiratory effects not fully captured by daily average.

---

## 7. Contributions

1. **First U.S. study** applying DECH metrics to cardiorespiratory EDVs. Prior DECH work was almost entirely in China.
2. **Validates the tightened EPA annual standard (9 µg/m³):** DECH-9 shows significant cardiorespiratory health effects, supporting health evidence below 12 µg/m³.
3. **Supports adequacy of daily average metric** for capturing cardiorespiratory EDV risk from ambient PM2.5 in Southern California — subdaily metrics do not reveal additional burden.
4. **Novel regionalization method (SKATER)** for handling sparse EDV counts at ZCTA level — potentially reusable for future studies.
5. **Children's respiratory vulnerability** under subdaily metrics is statistically confirmed for the first time in a U.S. context.

---

## 8. Replication Feasibility

- Hourly PM2.5: available via Public Records Request (South Coast AQMD)
- EDV data: available via HCAI application (same source as Chen et al. 2023)
- No replication archive or code repository mentioned
- Analysis uses R with `dlnm` and `spdep` packages (standard, publicly available)

---

## 9. Relevance to Capstone

**Connection to Chen et al. (2023):** Both papers use California HCAI EDV data and both focus on cardiorespiratory ED visits as the health endpoint. Chen covers the whole state over 2006–2019 (wildfire-specific); Nguyen covers Southern California 2018–2020 (all PM2.5, subdaily focus). They are methodologically related but ask different questions.

**Connection to OEHHA:** Wu, Ebisu, and Basu are OEHHA scientists — this comes from the same branch as the capstone requestors. This paper shows the research group's active interest in California EDV epidemiology.

**Relevance to valuation question:** Indirect. This paper confirms that cardiorespiratory EDVs attributable to PM2.5 are real and quantifiable, and that the daily average metric (which Chen uses) adequately captures the risk. It does **not** address economic valuation of those visits.

**Key limitation for capstone purposes:** Nguyen et al. do not disaggregate by wildfire smoke vs. other PM2.5 sources. Their study period (May 2018–March 2020) includes the 2018 California wildfire season (Camp Fire, Woolsey Fire) but also excludes 2020 onward when smoke events were severe. Chen et al.'s wildfire-specific design is more directly applicable to the capstone calculation.
