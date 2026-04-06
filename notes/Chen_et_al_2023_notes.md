# Chen et al. (2023) — Reading Notes
*Environmental Research 238 (2023) 117154*
**THE CORE PAPER: provides the ED visit counts that this capstone values**

## 1. Research Question
What are the short-term associations between wildfire smoke events and emergency department visits (EDVs) for respiratory, cardiovascular, diabetes, and mental health outcomes in California (2016–2019)? Are some subpopulations (by race/ethnicity, age, sex) disproportionately affected?

## 2. Audience
OEHHA researchers — two of four authors (Annie I. Chen, Rupa Basu) are in the Air and Climate Epidemiology Section at OEHHA, CalEPA. This paper was internally produced by the requesting agency for the capstone.

## 3. Method
Two-stage time-series analysis:
- **Stage 1**: Quasi-Poisson regression per air basin, modeling daily EDV counts as a function of a binary smoke event indicator, adjusted for seasonal/long-term trends (natural cubic spline), holidays, day of week, and mean apparent temperature at lag 0
- **Stage 2**: Random effects meta-analysis (mixmeta R package) combining air basin-specific estimates into an overall RR

**Smoke event definition**: air basin-day with wildfire-specific PM2.5 ≥ 98th percentile across all air basin-days (June–December 2016–2019); threshold = **13.5 μg/m³**. 257 smoke events out of 12,840 air basin-days.

**Health impact function** (applied to estimate attributable EDVs):
> ΔySE_j = Σᵢ y₀ᵢⱼ × [exp(βSEⱼ) − 1] × Populationᵢ × SmokeEventDaysᵢ

**Lags tested**: 0, 1, 2, 0_1 (cumulative 2-day), 0_2 (cumulative 3-day), 7, 10, 14 days. Best lag chosen by lowest total qAIC.

## 4. Data

**Exposure:**
- Wildfire-specific PM2.5: daily ZCTA-level estimates from ensemble ML model (Aguilera et al., 2023) — three ML algorithms combining satellite data, land use, and meteorological data (R² = 0.83 vs. EPA AQS monitors). HMS smoke plume data used to identify smoke-exposed zip code days. ZCTA values aggregated to air basin level using population-weighted averaging.
- 15 California air basins; 4 excluded (South Coast, San Diego, Salton Sea, Mojave Desert) — no smoke events. **11 air basins included.**
- Co-pollutants (sensitivity only): O₃, CO, NO₂ from EPA AQS

**Health outcomes:**
- California HCAI Emergency Department Data and Patient Discharge Data, 2016–2019
- ICD-10-CM codes mapped to CCSR categories; 18 outcome groups
- Outcomes: all respiratory, asthma, AURI, CLRD, pneumonia; all cardiovascular, AMI, cerebrovascular, dysrhythmia, IHD, PVD, TIA; diabetes; all mental health, anxiety, mood disorders, schizophrenia, substance use, suicide
- **Health data are confidential**

**Population:**
- Study population: **17,847,917** people (45.4% of CA) in 11 air basins
- 2015–2019 5-year ACS via tidycensus R package
- **Unit of observation**: air basin-day

**Software**: SAS 9.4 (data prep), R 4.2.1 (analysis)

**Study period**: June–December, 2016–2019 (wildfire season only)

## 5. Statistical Methods
Stage 1 model specification:
> log(μᵢⱼ) = α + β₁(smoke eventᵢⱼ) + β₂(apparent tempᵢⱼ) + β₃(day of weekⱼ) + β₄(holidayⱼ) + ns(dateⱼ, df = years × df/yr) + log(populationᵢ)

- 4 df/yr for respiratory; 2 df/yr for other outcomes
- Offset: log(population) to model rates
- Effect modification: stratified by race/ethnicity (White, Black, Hispanic, API), age (0–17, 18–64, 65+), sex
- Sensitivity: basin-specific 98th percentile thresholds; co-pollutant adjustment

## 6. Findings

### Main Results (percent change in risk of EDVs):
| Outcome | % Change | 95% CI | Lag |
|---|---|---|---|
| All respiratory | **+14.4%** | (6.8, 22.5) | 1 |
| Asthma | **+57.1%** | (44.5, 70.8) | 0 |
| CLRD | **+12.7%** | (6.2, 19.6) | 0 |
| AURI | positive, NS | — | 2 |
| Pneumonia | positive, NS | — | 0_2 |
| All cardiovascular | **+3.2%** | (1.7, 4.7) | 10 |
| Diabetes | positive, NS | — | 0_2 |
| Schizophrenia | **+13.1%** | (5.1, 21.8) | 0 |
| Substance use | negative, sig | — | 10 |
| Suicide | negative, sig | — | 0_1 |

Cardiovascular effects are **delayed** (lag 10) compared to respiratory effects, consistent with toxicological mechanisms (lung inflammation → systemic inflammation → cardiac effects).

### EDV Counts (Table 3):
| Outcome | Total EDVs | Daily rate/100,000 (all days) | Daily rate (smoke events) |
|---|---|---|---|
| All respiratory | 1,363,054 | 8.92 | 10.03 |
| Asthma | 163,994 | 1.07 | 1.77 |
| CLRD | 102,189 | 0.67 | 0.74 |
| All cardiovascular | 1,166,893 | 7.64 | 7.55 |
| All mental health | 630,113 | 4.12 | 4.03 |

### Attributable EDVs on Smoke Event Days (HIF estimates):
| Outcome | Attributable EDVs | 95% CI |
|---|---|---|
| **All respiratory** | **4,597** | (2,164, 7,203) |
| **Asthma** | **2,204** | (1,718, 2,733) |
| CLRD | 323 | (158, 498) |
| All cardiovascular | 889 | (476, 1,307) |
| Schizophrenia | 208 | (81, 345) |

### Equity/Subpopulation Results:
- **Hispanic**: significantly higher risk of diabetes EDVs at lag 0_2 (+13.7% vs. −2.6% for White, p<0.05)
- **API**: significantly lower risk of anxiety EDVs
- **Black**: trending positive for AMI and dysrhythmia (not significant)
- **Female**: trending higher asthma and CLRD risk vs. male
- **Age**: 65+ had higher TIA risk; children had lower mental health risk at lag 7

## 7. Contributions
- First study using ML-estimated wildfire PM2.5 to examine health impacts in California across multiple years (2016–2019), covering recent extreme fire years (2017, 2018 Camp Fire era)
- Broad set of outcomes including cardiovascular subgroups, mental health, diabetes — well beyond the respiratory focus of most prior studies
- Stratified analyses add to sparse literature on race/ethnicity effect modification
- Applies health impact function to estimate attributable ED burden — the number our capstone uses

## 8. Replication Feasibility
- **Health data**: **Confidential** (California HCAI) — not publicly available
- **Wildfire-specific PM2.5**: Available on GitHub: `benmarhnia-lab/Wildfire_PM25_California_ZIP`
- **Air quality/meteorological data**: Publicly available (EPA AQS, CIMIS, NCEI)
- **Population data**: Publicly available via `tidycensus` R package (2015–2019 5-year ACS)
- **Code**: Not explicitly stated as available; uses R and SAS

## Project Relevance
- **This is the foundational paper** for our capstone — it produces the attributable ED visit counts we apply unit values to
- The **4,597 attributable respiratory EDVs** and **2,204 asthma EDVs** are the quantities we multiply by BenMAP COI values ($36,000/admission from Fann et al., also used by EPA)
- The paper uses a **binary smoke event threshold** (≥ 98th percentile = 13.5 μg/m³), not a continuous exposure — this matters for how we characterize the marginal unit being valued
- Authors are at OEHHA — same agency that requested the capstone. The paper's framing (how do we value these?) is directly the capstone question.
- The delayed cardiovascular effect (lag 10) and schizophrenia finding extend the scope of economic harm beyond what BenMAP's COI for respiratory admissions captures
- **Key limitation for valuation**: attributable EDV estimates cover only smoke event days (98th+ percentile days); subthreshold exposures are not captured, so our valuation is likely a lower bound
