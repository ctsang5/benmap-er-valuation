# Chen et al. (2023) — Reading Notes

**Full citation:** Chen, A.I., Ebisu, K., Benmarhnia, T. & Basu, R. (2023). Emergency department visits associated with wildfire smoke events in California, 2016-2019. *Environmental Research*, 238, 117154.

**DOI:** https://doi.org/10.1016/j.envres.2023.117154

**Open access:** CC BY-NC-ND 4.0

---

## 1. Research Question

Are short-term wildfire smoke events associated with increased emergency department visits (EDVs) for respiratory, cardiovascular, metabolic, and mental health outcomes in California? And do the health effects differ by race/ethnicity, age, and sex?

**Why it matters:** While wildfire smoke is known to cause respiratory problems, its effects on cardiovascular disease, diabetes, and mental health are much less clear. There is also growing evidence that wildfire-specific PM2.5 may be more harmful than ambient PM2.5 from other sources (up to 10x more for respiratory hospital visits), and that marginalized communities are disproportionately exposed. Few studies have assessed differential health effects by race/ethnicity.

---

## 2. Audience

Environmental epidemiologists and public health officials working on wildfire preparedness and health impact assessment. The paper is from California's Office of Environmental Health Hazard Assessment (OEHHA), part of Cal/EPA — the state agency that produces health risk assessments and informs policy.

---

## 3. Method

### Study Design

**Two-stage time-series analysis:**

1. **Stage 1:** Quasi-Poisson regression for each air basin separately (to handle overdispersion in count data)
2. **Stage 2:** Random effects meta-analysis combining air basin-specific estimates into an overall relative risk (RR) and 95% CI, using the `mixmeta` package in R

Results reported as percent change in risk: (RR - 1) * 100%.

### Exposure Definition

- Daily, ZCTA-level **wildfire-specific PM2.5** concentrations from an ensemble machine learning model (Aguilera et al. 2023) that combines 3 ML algorithms with ~50 predictor variables (satellite, land use, meteorological data). Model validated against EPA AQS monitors (R² = 0.83).
- Wildfire-specific PM2.5 isolated by: (1) identifying smoke-exposed days via NOAA Hazard Mapping System smoke plume data, (2) removing those days and imputing counterfactual (non-wildfire) PM2.5 via chained random forest, (3) subtracting counterfactual from observed total PM2.5.
- ZCTA-level concentrations aggregated to **air basins** (15 geographic units defined by California for air quality management) using population-weighted averaging.
- **Smoke event** = air basin-day with wildfire-specific PM2.5 >= 98th percentile across all June-December 2016-2019 air basin-days. **Threshold = 13.5 ug/m3.**
- Restricted to June-December (wildfire season); January-May max was only 1.8 ug/m3.
- Continuous PM2.5 variable showed minimal associations; binary smoke event indicator performed better.

### Main Model Specification

```
log(mu_ij) = alpha + beta1(smoke_event_ij) + beta2(mean_apparent_temp_ij)
             + beta3(day_of_week_j) + beta4(holiday_j)
             + ns(date_j, df = years * df/yr) + log(population_i)
```

Where i = air basin, j = date. The log(population) offset models rates rather than counts.

**Confounding adjustment:**
- Natural cubic spline of time for seasonal/long-term trends (4 df/yr for respiratory; 2 df/yr for all others — chosen by minimizing sum of qAIC across first-stage models)
- Day of week (6 indicator variables, Sunday = reference)
- Holidays (binary: NYE, NYD, Memorial Day, July 4th, Labor Day, Thanksgiving, Christmas)
- Same-day mean apparent temperature (heat index)

### Lag Structure

- **Respiratory outcomes:** lag 0, 1, 2, cumulative 0_1, cumulative 0_2 (no lags past 2 based on prior literature)
- **All other outcomes:** also lag 7, 10, 14
- For cumulative lags, EVERY day in the lag period must be a smoke event
- Best lag selected by lowest total qAIC

### Co-pollutant Sensitivity

Assessed confounding by non-wildfire PM2.5, O3, CO, NO2 in separate models. Not included in main model because: (1) these pollutants are not thought to be associated with wildfire-specific PM2.5 concentration, (2) wanted consistent covariates across all outcomes, (3) some air basins excluded from co-pollutant analyses due to insufficient monitor coverage.

### Effect Modification

Stratified analyses by race/ethnicity (Hispanic, White, Black, API), age (0-17, 18-64, 65+), and sex (male, female). Z-test of interaction for subgroup differences.

### Health Impact Function

Attributable EDVs calculated per air basin and summed:

```
delta_y_SE_j = SUM_i [y0_ij * (exp(beta_SE_j) - 1) * Population_i * SmokeEventDays_i]
```

Where y0 = baseline daily incidence rate, beta_SE = overall effect estimate from meta-analysis.

---

## 4. Data

### Exposure Data
- **Wildfire-specific PM2.5:** Daily, ZCTA-level, from Aguilera et al. (2023) ensemble ML model
  - GitHub: https://github.com/benmarhnia-lab/Wildfire_PM25_California_ZIP
- **Co-pollutants:** O3 (8-hr max, ppb), CO (1-hr max, ppm), NO2 (1-hr max, ppb) from EPA AQS Data Mart. Monitors within 5 km (CO, NO2) or 10 km (O3) of ZCTA centroids, >=90% daily coverage. Inverse distance weighting to ZCTA, then population-weighted to air basin.
- **Temperature:** Hourly temp + relative humidity from EPA, CIMIS, NOAA NCEI. Apparent temperature (heat index) calculated per Basu et al. (2008). >=18 hourly measurements/day, >=90% daily coverage.

### Health Outcome Data
- **Source:** California Department of Health Care Access and Information (HCAI) — Emergency Department Data + Patient Discharge Data, 2016-2019
- **Inclusion:** Unscheduled EDVs. Patient Discharge Data used for unscheduled acute or psychiatric inpatient hospitalizations originating from the ED.
- **Variables extracted:** Service/admission date, ICD-10-CM principal diagnosis, race/ethnicity, age, sex, residential zip code
- **Diagnosis grouping:** AHRQ Clinical Classifications Software Refined (CCSR) v2022-1 SAS mapping program. Compatible with ICD-10-CM Oct 2015 - Sep 2022.
- **19 outcome categories** (Table 1): all respiratory, asthma, AURI, CLRD, pneumonia, all cardiovascular, AMI, cerebrovascular, dysrhythmia, IHD, PVD, TIA, diabetes, all mental health, anxiety, mood disorders, schizophrenia, substance use disorders, suicide

### Population Data
- 2015-2019 5-year ACS via `tidycensus` R package
- 2010 ZCTA population-weighted centroids for spatial assignment to air basins

### Study Population
- **11 air basins** with at least 1 smoke event (excluded: South Coast, San Diego, Salton Sea, Mojave Desert — zero smoke events)
- **N = 17,847,917** people (45.4% of California's 39.3M population)
- Demographics similar to statewide, except slightly more White (42.6% vs 37.2%) and less Hispanic (32.1% vs 39.0%)

### Exposure Summary
- **257 smoke events** out of 12,840 air basin-days (June-Dec 2016-2019)
- Wildfire PM2.5 range: 0-164.6 ug/m3; median = 0; mean = 1.1 ug/m3; 95% below 5 ug/m3
- On smoke event days: median wildfire PM2.5 = 23.1 ug/m3 (IQR: 14.9)
- Mean smoke events per basin: 23.4 (range: 7 in North Central Coast to 61 in Northeast Plateau)

### Outcome Counts (total EDVs, 11 air basins, 2016-2019)
| Outcome | N | Mean daily rate per 100K (all days) | Rate on smoke days | Rate on non-smoke days |
|---|---|---|---|---|
| All respiratory | 1,363,054 | 8.92 | 10.03 | 8.90 |
| Asthma | 163,994 | 1.07 | 1.77 | 1.06 |
| AURI | 622,512 | 4.07 | 4.40 | 4.07 |
| CLRD | 102,189 | 0.67 | 0.74 | 0.67 |
| Pneumonia | 143,820 | 0.94 | 0.92 | 0.94 |
| All cardiovascular | 1,166,893 | 7.64 | 7.55 | 7.64 |
| AMI | 59,686 | 0.39 | 0.41 | 0.39 |
| Dysrhythmia | 124,935 | 0.82 | 0.82 | 0.82 |
| Diabetes | 146,888 | 0.96 | 0.99 | 0.96 |
| All mental health | 630,113 | 4.12 | 4.03 | 4.13 |
| Schizophrenia | 66,577 | 0.44 | 0.46 | 0.44 |
| Substance use | 227,765 | 1.49 | 1.44 | 1.49 |

---

## 5. Statistical Methods

- **Stage 1:** Quasi-Poisson regression (accounts for overdispersion in count data) with log(population) offset
- **Stage 2:** Random effects meta-analysis via `mixmeta` R package (Sera et al. 2019)
- **Model selection:** Minimize sum of qAIC across first-stage models for both spline df/yr and lag selection
- **Spline:** Natural cubic spline of time; 4 df/yr for respiratory, 2 df/yr for all other outcomes
- **Software:** SAS 9.4 for data preparation; R 4.2.1 + RStudio for analysis
- **IRB:** California Committee for the Protection of Human Subjects, project #12-04-0075

---

## 6. Findings

### Main Results — Statistically Significant Associations

| Outcome | Best lag | % Change in Risk | 95% CI |
|---|---|---|---|
| **All respiratory diseases** | lag 1 | **+14.3%** | (6.8, 22.5) |
| **Asthma** | lag 0 | **+57.1%** | (44.5, 70.8) |
| **CLRD** | lag 0 | **+12.7%** | (6.2, 19.6) |
| **All cardiovascular diseases** | lag 10 | **+3.2%** | (1.7, 4.7) |
| **Schizophrenia** | lag 0 | **+13.1%** | (5.1, 21.8) |
| Substance use disorders | lag 10 | **-6.3%** | (significant, negative) |
| Suicide | lag 0_1 | **negative** | (significant, negative) |

### Key Patterns

1. **Respiratory effects are immediate and large.** Asthma is the strongest signal (+57% same-day). All respiratory subcategories show positive associations. AURI and pneumonia positive but not significant.

2. **Cardiovascular effects are delayed.** Association is null or slightly negative at short lags, gradually becomes positive, and is significant at lag 10 (+3.2%). No individual CV subgroups reached significance.

3. **Mental health effects are mixed.** Schizophrenia is the only positive finding (+13.1% same-day). Substance use and suicide are *negatively* associated — likely because people avoid the ED for non-urgent conditions during smoke events, or because social activities (and therefore substance-related incidents) decline during active wildfires.

4. **Biological mechanism for delayed CV effects:** Toxicological studies show lung inflammation appears first, followed by systemic inflammation and tissue injury in the heart. Wildfire smoke activates extracellular vesicles carrying miRNAs from lungs to heart (Carberry et al. 2022). Ultrafine particles may also translocate directly into the bloodstream.

5. **Schizophrenia mechanism:** Wildfire smoke-derived PM may trigger neuroinflammation and immune alterations consistent with the neuroinflammatory phenotype of schizophrenia. Other factors: psychosocial stress, medication nonadherence, inability to relocate during smoke events.

### Health Burden (Attributable EDVs on Smoke Event Days, 11 Air Basins)

| Outcome | Attributable EDVs | 95% CI |
|---|---|---|
| All respiratory diseases | 4,597 | (2,164 - 7,203) |
| Asthma | 2,204 | (1,718 - 2,733) |
| CLRD | 323 | (158 - 498) |
| All cardiovascular diseases | 889 | (476 - 1,307) |
| Schizophrenia | 208 | (81 - 345) |

### Effect Modification by Race/Ethnicity

- **Diabetes:** Hispanic +13.7% (2.2, 26.4%) significantly higher than White -2.6% (-9.8, 5.2%)
- **Anxiety:** API significantly lower risk than White (neither individually significant)
- **Asthma:** Trending lower for Black and API (not significant)
- **Pneumonia:** Trending higher for API and Hispanic (all subgroups positive)
- **AMI, dysrhythmia:** Trending positive for Black populations (not significant)

### Effect Modification by Age

- **TIA:** 65+ significantly higher risk than 18-64 at lag 2 (8.3%, 95% CI: -7.9, 27.4%)
- **All mental health:** Children 0-17 significantly *lower* risk than 18-64 at lag 7 (-12.7%, -18.6 to -6.4%)
- No significant child vs. adult differences for respiratory outcomes (contrary to some prior studies)

### Effect Modification by Sex

- No significant differences
- Asthma and CLRD trending higher among females (consistent with prior literature)

### Robustness

- **Co-pollutant adjustment:** Results generally robust. CO and non-wildfire PM2.5 reduced respiratory associations slightly but they remained positive. Fewer air basins for O3 (8), NO2 (5), CO (6) analyses.
- **Alternative smoke event definitions:** Basin-specific 98th percentile thresholds gave similar results. Pneumonia, mood disorders, schizophrenia slightly higher with basin-specific thresholds. Asthma effect lower when all 15 basins included (driven by 4 excluded basins having near-null estimates).

---

## 7. Contributions

1. **Demonstrated that cardiovascular effects of wildfire smoke are delayed (~10 days) relative to respiratory effects (~0-1 days).** This is consistent with the toxicological mechanism of lung inflammation propagating systemically to the heart via extracellular vesicles, and means studies that only look at short lags will miss cardiovascular impacts.

2. **Found a significant positive association between wildfire smoke and schizophrenia EDVs** — a rarely examined outcome in wildfire epidemiology. The neuroinflammatory mechanism is biologically plausible.

3. **Provided race/ethnicity-stratified estimates**, which are rare in wildfire health studies. Found significantly higher diabetes risk for Hispanic populations and trending cardiovascular risk elevations for Black populations.

4. **Quantified the attributable health burden:** ~4,600 additional respiratory EDVs and ~900 additional cardiovascular EDVs attributable to smoke events across 11 California air basins, 2016-2019.

5. **Used wildfire-specific PM2.5** (isolated from total PM2.5 via ML + counterfactual estimation) rather than total PM2.5, which allows more precise attribution of health effects specifically to wildfire smoke.

---

## 8. Replication Feasibility

- **Health data:** Confidential. Must be requested from California HCAI.
- **Wildfire PM2.5 data:** Publicly available at https://github.com/benmarhnia-lab/Wildfire_PM25_California_ZIP
- **Co-pollutant data:** EPA AQS Data Mart (publicly available)
- **Temperature data:** EPA, CIMIS, NOAA NCEI (all publicly available)
- **Population data:** ACS via `tidycensus` R package (publicly available)
- **Fire perimeters:** CAL FIRE FRAP GIS Data (publicly available)
- **Diagnosis grouping:** AHRQ CCSR v2022-1 SAS program (publicly available)
- **Software:** SAS 9.4 + R 4.2.1 (`mixmeta` package)
- **No replication archive or code repository mentioned**
- **Funding:** No specific grant funding
- **Total references:** 53

---

## 9. Connection to the Capstone

This paper sits in a **different part of the BenMAP pipeline** than the other capstone papers. The valuation papers (BenMAP Appendix H, Alberini & Krupnick, Stieb et al., Johnson et al.) focus on **Step 3** of BenMAP — assigning a dollar value to each avoided ED visit. Chen et al. focuses on **Step 2** — estimating how changes in air quality translate into changes in the number of ED visits. Specifically:

- It quantifies the **health concentration-response relationship** between wildfire smoke and ED visits — exactly the type of epidemiological input that BenMAP needs to convert pollution changes into health outcome counts
- The health impact function (Section 2.4.4) is structurally identical to BenMAP's approach: effect estimate x baseline incidence x population x exposure change
- The 19 outcome categories use the same ICD-10-CM diagnostic coding and AHRQ classification tools that BenMAP's HCUP-based valuation pipeline uses
- The finding that **asthma EDVs increase 57% on smoke event days** is directly relevant to the valuation side: each of those additional ED visits would be valued at $534 (Smith) or $447 (Stanford) under BenMAP's COI framework — and at 2-4x those amounts under a WTP framework

This paper also highlights the **wildfire-specific PM2.5 challenge** for BenMAP: standard BenMAP runs use concentration-response functions derived from studies of general ambient PM2.5, but emerging evidence (including this paper) suggests wildfire-specific PM2.5 may be substantially more toxic. If so, BenMAP may underestimate the health benefits of wildfire smoke mitigation not just because of the COI-vs-WTP valuation gap, but also because of an underestimated concentration-response relationship.
