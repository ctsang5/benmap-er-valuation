# Alberini & Krupnick (2000) — Reading Notes

**Full citation:** Alberini, A. & Krupnick, A. (2000). Cost-of-illness and willingness-to-pay estimates of the benefits of improved air quality: Evidence from Taiwan. *Land Economics*, 76(1), 37-53.

**JSTOR:** https://www.jstor.org/stable/3147256

---

## 1. Research Question

How does WTP to avoid minor respiratory illness compare with COI estimates, using data from the same individuals in the same study? And are the WTP/COI ratios found in the U.S. applicable to a newly industrialized country like Taiwan?

**Why it matters:** COI (medical bills + lost wages) is cheap and easy to calculate but understates true damages because it ignores the discomfort, pain, and disruption of being sick. WTP captures the full welfare cost but requires expensive surveys. If you knew the WTP/COI ratio was stable across countries and contexts, you could skip the WTP survey and just multiply COI by that ratio. This paper tests whether the ratio holds outside the U.S.

---

## 2. Audience

Environmental economists and regulatory analysts who need to value the health benefits of air pollution reductions, especially in developing countries where original WTP studies are rare and analysts rely on benefits transfer from U.S. estimates.

---

## 3. Method

### Two-Part Study Design

The paper exploits a **combined epidemiological/economic study** with two data-collection components conducted on the **same people**:

1. **Prospective cohort study (health diaries):** 602 adults in 3 Taiwan cities filled out daily diaries for 92 days (Nov 1991–Jan 1992), recording presence/absence of 19 respiratory symptoms, doctor visits, medication use, work days lost, and outdoor time. Diaries were matched with daily PM10 readings from 5 monitors within 750m of respondents' homes.

2. **Contingent valuation survey:** ~9 months later (Sep 1992), the same respondents were re-contacted for a face-to-face CV survey about their most recent episode of acute respiratory illness. Respondent-defined illness (the respondent describes their own illness, not a hypothetical one). Double-bounded dichotomous choice WTP format with two follow-up questions.

### Why This Design Is Powerful

Because both COI and WTP are estimated from **the same individuals**, the comparison is internally valid. You're not comparing a COI estimate from one population with a WTP estimate from a different one.

### COI Estimation Approach

Three probit regression equations estimated from the 92-day panel data:
- **Doctor visits** (Eq [8]): Pr(see doctor on day t) = Φ(x·γ)
- **Prescription medication** (Eq [9]): Pr(take Rx meds on day t) = Φ(x·α)
- **Work-loss days** (Eq [10]): Pr(miss work on day t) = Φ(x·δ)

Independent variables: daily PM10, max temperature, relative humidity, day-of-week dummies, day-of-study trend, lagged illness indicator (was the respondent sick yesterday?), age, gender, education, insurance status, marital status, occupational exposure to smoke/fumes/dust.

COI = N · Σ(c_j · Φ(x̄β_j)), where c_j are unit costs and Φ(x̄β_j) are predicted probabilities at various PM10 levels.

### WTP Estimation Approach

Uses the dose-response function from Alberini & Krupnick (1998, *Journal of Urban Economics*), which breaks PM10's health effects into two parts:
1. **Onset:** PM10 increases the probability of starting a new episode of illness
2. **Duration:** PM10 does NOT significantly affect how long an episode lasts once it starts

WTP damages formula (Eq [12]):

WTP = N · Pr(Illness|PM10 = Y) · Σ(π_k · WTP_k)

Where Pr(Illness|PM10=Y) is the onset probability at a given PM10 level, π_k is the probability an episode lasts k days, and WTP_k is the WTP to avoid a k-day episode.

WTP estimates (from the companion CV survey, analyzed in Alberini et al. 1997 and Alberini & Krupnick 1998):
- WTP for 1-day illness: ~US$25
- WTP for 5-day illness: ~US$43 → implies ~US$8.18 per symptom-day (diminishing returns)
- WTP increases with duration, number of symptoms, income, education
- WTP is lower for common colds vs. more severe ailments
- WTP is higher for people with prior serious respiratory illness (increasing marginal disutility)

### Averting Behavior

The authors attempted to estimate averting expenditures (a third component of WTP beyond COI) but found:
- Outdoor time was *positively* correlated with PM10 (opposite of expected — Taiwanese didn't reduce outdoor time on polluted days, unlike L.A. residents)
- 99% used gas ranges regardless of pollution levels
- Air conditioning data unavailable on a daily basis
- Concluded: averting behavior is "probably not very important" in Taiwan and excluded it from the analysis

### Theoretical Framework

Follows Harrington & Portney (1987). Key decomposition (Eq [6]):

WTP = w·(dW/dP) + p_M·(dM/dP) + p_A·(∂A*/∂P) − (U_D/λ)·(dD/dP)

In words: WTP = lost earnings + medical expenditures + averting costs + dollar value of discomfort

COI captures only the first two terms. The discomfort term (U_D/λ) is what COI misses. Economic theory predicts WTP > COI under general assumptions.

---

## 4. Data

- **Sample:** 602 adults who completed both the diary study and the CV survey
- **Cities:** Taipei (capital), Kaohsiung (industrial, polluted), Hualien (unpolluted resort city)
- **Time period:** Health diaries: Nov 1991–Jan 1992 (92 days). CV survey: Sep 1992.
- **Recruitment:** Random sampling after stratification by age, from residents within 750m of 5 air monitors
- **Panel dataset:** 87,676 person-day observations (602 × ~92 days, adjusted for in-town days)
- **PM10 levels:** High at Sun-San (downtown Taipei) and both Kaohsiung monitors (Sun-Min, Fu-Hsing). Taiwan standard: 125 μg/m³. Large day-to-day fluctuations (up to 200+ μg/m³). Hualien averaged only 32 μg/m³.
- **1992 Taiwan per capita income:** ~$10,000 (about half of U.S.)

### Illness Rates from Diaries

- Nearly half of respondents had zero symptoms over the entire 92-day study
- On average day, only 4.6% reported any symptoms
- Most common: cold/flu, cough with phlegm, runny nose, sore throat
- Doctor visits: 1.5% of respondents on any given day
- Prescription medication: similar percentage
- Work days lost: <1% on any given day

---

## 5. Statistical Methods

### COI Component: Probit Regressions (Tables 1-3)

**Doctor visits (Table 1):**

| Variable | General Spec. | Parsimonious Spec. |
|---|---|---|
| Intercept | -1.9437 (7.636) | -2.4205 (-85.51) |
| Symptoms on previous day | 1.2199 (33.52) | 1.2036 (34.29) |
| PM10 | 0.00061 (2.508) | 0.00078 (3.512) |
| Max temperature | -0.0025 (-0.586) | — |
| Relative humidity | -0.0030 (-1.520) | — |
| Insurance dummy | -0.0782 (-1.256) | — |
| Age | 0.0044 (3.159) | — |
| Male (dummy) | -0.1351 (-3.997) | — |
| Education (years) | -0.0329 (-6.551) | — |
| Exposed to smoke/fumes at work | 0.0165 (0.463) | — |
| Married (dummy) | 0.0156 (0.386) | — |
| Sample size | 55,626 | 57,078 |
| Log likelihood | -3,758.11 | -3,952.31 |

Key findings:
- PM10 significantly increases doctor visits (p < 0.01)
- Effect is small: Pr(doctor visit) goes from ~1% at PM10=150 to ~1.5% at PM10=350
- More educated → less likely to see doctor (self-care)
- Insurance dummy negative but not significant (paradoxical — may capture occupation-based effects)
- Income and sick-leave excluded because LR tests showed no loss of fit

**Prescription medication (Table 2):**
- PM10: 0.00036 (t=1.343) general / 0.00059 (t=2.425) parsimonious — weaker than for doctor visits
- Same pattern: lagged symptoms strongly predict medication use; more educated → less medication
- Insurance dummy essentially zero (-0.0043, t=-0.006)

**Work-loss days (Table 3):**
- PM10: 0.0011 (t=2.712) general / 0.00096 (t=2.626) parsimonious — significant
- Insurance dummy: -0.2591 (t=-2.549) — significant here (insured workers less likely to miss work)
- Temperature: -0.0198 (t=-2.665) — colder days → more work loss
- Gender not significant; occupational exposure not significant

### Unit Costs for COI Calculation

- N = 3,031,532 adult residents of the three cities
- Doctor visit: NT$216 = **US$8.64** (1992 dollars)
- Prescription medication: NT$298.52 = **US$11.94** (1992 dollars)
- Lost earnings per work-loss day: NT$464.66 = **US$18.58** (1992 dollars)
- Exchange rate: NT$25 = US$1 (1992)

Note: COI figures are conservative — they do not include travel time to or waiting time at the doctor's office.

### WTP Component

WTP damages computed using formula in Section V (Eq [12]), blending the dose-response onset probabilities with the WTP-per-episode estimates from the companion CV survey.

---

## 6. Findings

### The Core Comparison: Table 4

All figures are aggregate annual damages for ~3 million adult residents of the three cities, in 1992 U.S. dollars:

| PM10 (μg/m³) | Doctor Cost | Lost Earnings | Rx Meds | **Total COI** | **WTP** | **WTP/COI** |
|---|---|---|---|---|---|---|
| 25 | 214,097 | 93,416 | 229,175 | 536,689 | 794,733 | **1.48** |
| 50 | 225,779 | 100,913 | 238,985 | 565,678 | 869,629 | 1.54 |
| 100 | 250,845 | 117,575 | 259,655 | 628,074 | 1,038,187 | **1.65** |
| 150 | 278,295 | 136,692 | 281,881 | 696,867 | 1,234,551 | **1.77** |
| 200 | 308,337 | 158,580 | 305,772 | 772,690 | 1,462,317 | 1.89 |
| 250 | 341,130 | 183,577 | 318,370 | 843,077 | 1,725,357 | **2.05** |
| 300 | 376,909 | 212,078 | 344,940 | 933,927 | 2,027,815 | 2.17 |
| 350 | 415,884 | 244,477 | 388,414 | 1,048,775 | 2,374,087 | **2.26** |

### Key Patterns in the WTP/COI Ratio

1. **WTP > COI at every pollution level** — consistent with economic theory. The gap represents the dollar value of pain, discomfort, and disruption that COI ignores.

2. **The ratio increases with pollution.** At low PM10 (25 μg/m³), WTP/COI = 1.48. At high PM10 (350 μg/m³), WTP/COI = 2.26. Why? As pollution worsens, people experience more symptoms, but their doctor visits, medication expenses, and lost earnings don't increase proportionally. The discomfort component grows faster than the tangible-cost component.

3. **Taiwan ratios match U.S. ratios.** Despite economic, cultural, and institutional differences (Taiwan per capita income = half of U.S.; different health care system; different sick-leave norms), the WTP/COI ratios are "in line with" U.S. findings:
   - Rowe & Chestnut (1985): WTP/COI = **1.61** for asthma symptoms (L.A. asthmatics)
   - Alternative calculation for the same L.A. group: WTP/COI = **3.7**

4. **WTP per episode:** ~US$25 for a 1-day illness; ~US$43 for a 5-day illness (diminishing returns: ~$8.18/day)

### Why the Ratio Increases with Severity

This is the mechanism behind the "severity gradient" discussed in the review essay. For mild illness at low pollution, the tangible costs (doctor, meds, lost work) are a decent fraction of what people would pay to avoid the illness — the discomfort isn't that bad. But for worse illness at high pollution, the discomfort grows much faster than the bills. This is the same logic that explains why Stieb et al. (2002) found a ~6x ratio for cardiac hospital admissions: cardiac events involve much more pain, fear, and life disruption than a runny nose, so the gap between COI and WTP is much larger.

**Prior U.S. evidence for comparison:** WTP/COI ratio is 1.6 to ~4x for various respiratory endpoints (Rowe & Chestnut 1985; Chestnut et al. 1988; Dickie & Gerking 1991b).

---

## 7. Contributions

1. **First head-to-head WTP vs. COI comparison outside the U.S.** Previous WTP/COI comparisons (Rowe & Chestnut 1985; Chestnut et al. 1988; Dickie & Gerking 1991b) were all based on U.S. data. This paper is the first to test whether the ratio holds in a non-U.S. context with different income levels, health care systems, and cultural norms around illness.

2. **Validated WTP responses using COI as a benchmark.** Because COI and WTP data come from the same people, finding WTP > COI is a validity check: it confirms that CV survey respondents are reporting economically meaningful WTP amounts, not random numbers.

3. **Established that the WTP/COI ratio is relatively stable across countries.** Taiwan's 1.48–2.26 range is similar to U.S. findings (1.6–3.7), despite Taiwan having half the per capita income. This means analysts in developing countries can use the ratio as a rough multiplier: estimate COI from official health statistics, multiply by ~2, and get an approximation of WTP without conducting an expensive CV survey.

4. **Demonstrated that the ratio increases with pollution severity.** This finding — that discomfort grows faster than tangible costs as pollution worsens — provides empirical support for the theoretical prediction that COI understates WTP more severely for more serious health endpoints. This is the mechanism behind the severity gradient in the capstone's literature review.

---

## 8. Replication Feasibility

- **Data availability:** Proprietary dataset from a combined epidemiological/CV study conducted under Academia Sinica and U.S. EPA Office of Research and Development funding. Not publicly available.
- **Companion studies:** Epidemiological study reported in Shaw et al. (1996) and Alberini & Krupnick (1997). CV survey methodology described in Alberini et al. (1997, JEEM 34, 107-126) — the 1997 paper also in the capstone sources directory.
- **Software:** LIMDEP Version 7.0 (Greene 1995).
- **References:** 22 total.

---

## 9. Connection to the Capstone

This is the paper cited in the review essay for the **WTP/COI ratio of ~2x for mild respiratory illness**. The essay uses this ratio to argue that BenMAP's COI-based ER visit valuations (e.g., $1,161 for cardiovascular) understate the true welfare cost by at least a factor of 2. Combined with Stieb et al. (2002)'s ~6x ratio for cardiac admissions, the paper establishes a severity gradient: the more severe the health event, the larger the gap between what it costs (COI) and what people would pay to avoid it (WTP).
