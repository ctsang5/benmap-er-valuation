# Reading Notes: Chen et al. (2023)

**Full citation:** Chen AI, Ebisu K, Benmarhnia T, Basu R. "Emergency department visits associated with wildfire smoke events in California, 2016–2019." *Environmental Research* 238 (2023) 117154. https://doi.org/10.1016/j.envres.2023.117154

---

## 1. Research Question

Are short-term wildfire smoke events associated with increased emergency department visits (EDVs) for respiratory, cardiovascular, metabolic, and mental health outcomes in California? Which subpopulations are most vulnerable?

**Why it matters:** Wildfires are increasing in frequency and severity in California due to climate change. Wildfire-specific PM2.5 may be more toxic than ambient PM2.5 from other sources. Little is known about non-respiratory impacts (cardiovascular, metabolic, mental health) or differential risk by race/ethnicity. This is the primary epidemiological paper underlying the capstone's economic valuation exercise.

---

## 2. Audience

Epidemiologists studying wildfire health impacts, California public health officials (OEHHA, CDPH, air districts), and researchers designing health impact assessments for wildfire smoke. All four authors are from OEHHA (Chen, Ebisu, Basu) or UC San Diego (Benmarhnia) — the same research group that requested the capstone.

---

## 3. Method

**Design:** Two-stage time-series analysis.

- **Stage 1:** Quasi-Poisson regression for each air basin (11 basins), regressing daily EDV counts on a binary smoke event indicator, controlling for apparent temperature, day of week, holidays, and seasonal/long-term trends via natural cubic spline. Log(population) included as an offset to model rates.

- **Stage 2:** Random effects meta-analysis across air basins using the `mixmeta` package in R to produce an overall relative risk (RR) for each outcome.

**Smoke event definition:** Air basin-day with wildfire-specific PM2.5 ≥ 98th percentile across all air basin-days during June–December 2016–2019. **Threshold = 13.5 µg/m³.**

- This is a binary exposure (event vs. non-event), not a continuous PM2.5 metric.
- For cumulative lags, each day in the lag period must meet the threshold.

**Lag structure tested:** Lag 0, 1, 2, cumulative lag 0_1, 0_2 (for respiratory outcomes); additionally lag 7, 10, 14 (for other outcomes). Optimal lag chosen by minimizing total qAIC.

**Health impact function (for attributable EDV counts):**

ΔySE = Σᵢ [y₀ᵢⱼ × (exp(βSEⱼ) − 1) × Populationᵢ × SmokeEventDaysᵢ]

Where: i = air basin, j = outcome, βSE = overall effect estimate, y₀ = baseline incidence rate, SmokeEventDays = number of smoke event days.

---

## 4. Data

| Item | Detail |
|---|---|
| **Wildfire-specific PM2.5** | Ensemble machine learning model (Aguilera et al. 2023): 3 ML algorithms, ~50 predictor variables (satellite, land use, meteorology). Validated against EPA AQS monitors (R² = 0.83). Counterfactual PM2.5 estimated by removing smoke-exposed days and imputing via chained random forest. Wildfire PM2.5 = total PM2.5 − counterfactual PM2.5. |
| **Smoke plume identification** | NOAA Hazard Mapping System (HMS) smoke plume data. |
| **Health outcomes** | California HCAI: Emergency Department Data + Patient Discharge Data, 2016–2019. Unscheduled EDVs. ICD-10-CM principal diagnosis. Variables: date, ICD-10 code, race/ethnicity, age, sex, residential zip code. **Data are confidential.** |
| **ICD-10 mapping** | AHRQ Clinical Classifications Software Refined (CCSR), Version 2022-1 (DXCCSR_Mapping_Program_v2022-1.sas). |
| **Co-pollutants** | O3, CO, NO2 from EPA AQS Data Mart (monitors ≥90% daily coverage). |
| **Temperature** | Apparent temperature from USEPA, CIMIS, NOAA NCEI. Inverse distance weighting to ZCTA centroid, then population-weighted average to air basin. |
| **Geography** | 15 CA air basins. 4 excluded (0 smoke events): South Coast, San Diego, Salton Sea, Mojave Desert. 11 basins analyzed. |
| **Unit of observation** | Air basin-day (11 basins × ~856 days in June–December 2016–2019 = ~9,416 observations) |
| **Study population** | 17,847,917 people in 11 air basins (~45.4% of CA population). Similar age/sex to state; slightly more White and API, fewer Hispanic vs. whole state. |
| **Study period** | June–December 2016–2019 (wildfire season only) |
| **Software** | SAS 9.4 (data prep); R 4.2.1 / RStudio (analysis) |

### Smoke events summary
- 257 smoke events out of 12,840 air basin-days (all 15 basins)
- Median wildfire PM2.5 on smoke event days: 23.1 µg/m³ (IQR: 14.9)
- Median on non-smoke days: 0 µg/m³ (IQR: 0.2)
- Mean smoke events per basin: 23.4; range: 7 (North Central Coast) to 61 (Northeast Plateau)

---

## 5. Statistical Methods

- **Quasi-Poisson regression** (overdispersion adjustment)
- **Natural cubic spline** for seasonal/long-term trends: 4 df/yr (respiratory), 2 df/yr (all other)
- **Random effects meta-analysis** (`mixmeta`, Sera et al. 2019)
- **Stratified analyses** by race/ethnicity (Hispanic, White, Black, API), age (0–17, 18–64, 65+), sex (male/female)
- **Z-test of interaction** (Altman 2003) to test subgroup differences
- **Sensitivity analyses:** basin-specific 98th percentile thresholds; co-pollutant adjustment (non-wildfire PM2.5, O3, CO, NO2)

**Model specification:**
log(μᵢⱼ) = α + β₁(smoke event indicatorᵢⱼ) + β₂(apparent tempᵢⱼ) + β₃(day of weekⱼ) + β₄(holidayⱼ) + ns(dateⱼ, df = years × df/yr) + log(populationᵢ)

---

## 6. Findings

### Risk estimates (percent change in EDV risk, 95% CI)

| Outcome | Best lag | % Change | 95% CI |
|---|---|---|---|
| **All respiratory diseases** | lag 1 | **+14.3%** | **(6.8, 22.5)** |
| Asthma | lag 0 | **+57.1%** | **(44.5, 70.8)** |
| AURI | lag 2 | +~15%* | not significant |
| CLRD | lag 0 | **+12.7%** | **(6.2, 19.6)** |
| Pneumonia | lag 0_2 | positive | not significant |
| **All cardiovascular diseases** | lag 10 | **+3.2%** | **(1.7, 4.7)** |
| AMI, cerebrovascular, dysrhythmia, IHD, PVD, TIA | various | null/positive | not significant |
| **Diabetes** | lag 0_2 | positive | not significant |
| **Schizophrenia** | lag 0 | **+13.1%** | **(5.1, 21.8)** |
| Substance use disorders | lag 10 | **negative** | significant |
| Suicide | lag 0_1 | **negative** | significant |
| Anxiety, mood disorders | various | null | not significant |

*Note: cardiovascular association was null at early lags and became significantly positive only at lag 10, suggesting delayed physiological cascade (lung inflammation → systemic → cardiac).

### Health burden attributable to smoke events (total across 11 air basins, 2016–2019)

| Outcome | Attributable EDVs | 95% CI |
|---|---|---|
| **All respiratory diseases** | **4,597** | **(2,164, 7,203)** |
| Asthma | **2,204** | **(1,718, 2,733)** |
| CLRD | **323** | **(158, 498)** |
| **All cardiovascular diseases** | **889** | **(476, 1,307)** |
| Schizophrenia | **208** | **(81, 345)** |

### EDV counts by outcome category (raw totals, 2016–2019, 11 basins)

| Outcome | N |
|---|---|
| All respiratory diseases | 1,363,054 |
| Asthma | 163,994 |
| AURI | 622,512 |
| CLRD | 102,189 |
| Pneumonia | 143,820 |
| All cardiovascular diseases | 1,166,893 |
| AMI | 59,686 |
| Cerebrovascular | 83,924 |
| Dysrhythmia | 124,935 |
| IHD | 86,699 |
| PVD | 67,111 |
| TIA | 27,261 |
| Diabetes | 146,888 |
| All mental health | 630,113 |
| Schizophrenia | 66,577 |
| Substance use disorders | 227,765 |
| Suicide | 83,584 |

### Subgroup findings

- **Hispanic:** significantly higher diabetes EDV risk (13.7% vs. −2.6% for White)
- **API:** significantly lower anxiety EDV risk vs. White
- **Black:** trending positive AMI and dysrhythmia (not significant; consistent with EJ literature)
- **Age 65+:** higher TIA risk at lag 2 (not significant)
- **Children 0–17:** lower mental health EDVs at lag 7 (significant); no significant respiratory difference from adults
- **Female:** trending higher asthma and CLRD (consistent with prior literature)

### Sensitivity analyses
Results generally robust to co-pollutant adjustment. Adjustment for CO or non-wildfire PM2.5 reduced magnitude somewhat (especially respiratory), but results remained similar. Basin-specific vs. overall threshold definitions produced similar results.

---

## 7. Contributions

1. **Most comprehensive California wildfire EDV study to date** (2016–2019, all air basins, 20 outcome categories including mental health and metabolic).
2. **First to document cardiovascular lag structure** for wildfire smoke (delayed effect at lag 10, consistent with toxicological lung→cardiac cascade).
3. **First to quantify schizophrenia–wildfire smoke association** using EDV data.
4. **Provides the EDV counts** (4,597 respiratory, 889 cardiovascular) that the capstone uses as its baseline health burden for economic valuation.
5. **Environmental justice contribution:** elevated diabetes risk among Hispanic populations; trending cardiovascular disparities for Black populations.

---

## 8. Replication Feasibility

- **Wildfire-specific PM2.5:** Publicly available — GitHub: https://github.com/benmarhnia-lab/Wildfire_PM25_California_ZIP
- **Health outcome data (HCAI):** Confidential — available with approved application from HCAI
- **Air quality data:** Publicly available from EPA AQS Data Mart
- **ACS data:** Publicly available via `tidycensus` R package
- **Analysis code:** Not mentioned in text (no replication archive cited)
- **ICD-10 mapping:** AHRQ CCSR v2022-1 (public)

---

## 9. Relevance to Capstone

**This is the primary paper for the capstone.** The capstone's economic valuation exercise applies dollar values to Chen et al.'s EDV counts.

### Key numbers for the capstone calculation

| Endpoint | Attributable EDVs | Best-fit lag |
|---|---|---|
| All respiratory | 4,597 (2,164–7,203) | lag 1 |
| Asthma | 2,204 (1,718–2,733) | lag 0 |
| CLRD | 323 (158–498) | lag 0 |
| All cardiovascular | 889 (476–1,307) | lag 10 |
| Schizophrenia | 208 (81–345) | lag 0 |

### What Chen et al. provides vs. what the capstone needs

**Provided:**
- Attributable EDV counts by outcome category for California, June–December 2016–2019
- Relative risk estimates and confidence intervals for each outcome
- Methodology for the health impact function (same formula as BenMAP's HIA approach)

**Not provided (must come from other sources for the valuation):**
- Dollar values per EDV — that's BenMAP's COI module (Appendix H) and the WTP literature (Stieb et al., Richardson et al.)
- Mapping of CCSR/ICD-10 categories to BenMAP's endpoint categories — requires a bridging assumption
- WTP estimates for mental health, metabolic (diabetes), or schizophrenia EDVs — no source in the literature

### Mapping to BenMAP/valuation sources

| Chen et al. endpoint | Valuation source | Notes |
|---|---|---|
| All respiratory (4,597) | BenMAP COI $875; Stieb REDV CAN$2,000 | Closest match |
| All cardiovascular (889) | BenMAP COI $1,161; Stieb CEDV CAN$4,400 | Closest match |
| Mental health, diabetes | None | 8 of 19 endpoints unvalued |

### Important methodological note

Chen et al. define a "smoke event" as a binary indicator (≥ 98th percentile = 13.5 µg/m³), not a continuous PM2.5 concentration. This means the RR reflects the effect of a high-smoke day vs. a non-smoke day — it is **not** a per-µg/m³ estimate. The health impact function produces attributable EDVs over the study period, not per-year estimates. The capstone should be clear about the time frame (4 wildfire seasons: June–December 2016–2019).

### Limitation for capstone: 4 Southern CA air basins excluded

South Coast, San Diego, Salton Sea, and Mojave Desert were excluded because they had no smoke events by the study's definition. This means the 4,597 respiratory and 889 cardiovascular EDVs cover only 45.4% of California's population. Statewide totals would be higher, but the excluded basins had lower wildfire smoke exposure during this period.
