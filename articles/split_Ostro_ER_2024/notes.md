# Reading Notes: Ostro et al. (2024)

**Full citation:** Ostro B, Fang Y, Carreras Sospedra M, Kuiper H, Ebisu K, Spada N. "Health impact assessment of PM2.5 from uncovered coal trains in the San Francisco Bay Area: Implications for global exposures." *Environmental Research* 252 (2024) 118787. https://doi.org/10.1016/j.envres.2024.118787

---

## 1. Research Question

What are the health impacts of PM2.5 emitted by uncovered coal rail cars on communities living near the rail corridor in the East Bay (Oakland-to-Martinez corridor), San Francisco Bay Area? How do these impacts differ by race/ethnicity?

**Why it matters:** Coal rail transport is widespread globally (70% of U.S. coal moves by rail; 80+ countries use coal). Exposed communities are disproportionately low-income and non-White. This is the first study to formally quantify health impacts from this specific exposure source.

---

## 2. Audience

Air quality regulators, environmental justice researchers, BenMAP practitioners, policymakers evaluating coal export proposals. The paper is methodologically a BenMAP application study — it demonstrates how BenMAP is used for a real-world health impact assessment.

**Note:** Keita Ebisu is an OEHHA co-author, connecting this to the same research group as Chen et al. (2023) and Nguyen et al. (2024).

---

## 3. Method

**Design:** Health impact assessment (HIA) using BenMAP software.

**General HIA formula:**
ΔHE = Baseline × Population Exposed × (1 − exp(−β × ΔPM))

Where: ΔHE = estimated increase in health endpoint, Baseline = background incidence/prevalence, β = health risk per µg/m³ from epidemiologic evidence, ΔPM = change in PM2.5.

**Exposure scenarios:** Three based on wind conditions at the Richmond, CA rail monitor site:
- Scenario 1: 0.7 µg/m³ annual average (baseline comparison)
- Scenario 2: 1.0 µg/m³ (moderate wind, ~50% of days)
- Scenario 3: 2.1 µg/m³ (calm west wind, dominant direction ~70% of days)

These annual average increments derive from 5-min peak readings of 8.32–25.0 µg/m³ during coal train passages, averaged with background concentrations of 10.4 µg/m³.

---

## 4. Data

| Item | Detail |
|---|---|
| **PM2.5 exposure** | From Ostro et al. (2023a,b): AI-trained cameras identified coal vs. freight trains at a monitor 32m from the rail line in Richmond, CA. 15 full coal trains measured. Coal dust increment: 8.32 µg/m³ vs. freight baseline. |
| **Dispersion model** | Liu et al. (2022): co-kriging model from 46 monitors in LA area (only study to measure dispersion from passing trains). Applied to Contra Costa and Alameda counties. |
| **Study population** | 262,031 people in the East Bay near the rail corridor (Oakland to Martinez). 74% non-White: Hispanic 35%, Black 22%, Asian 17%, White 26%. |
| **Population source** | 2010 U.S. Census, projected to 2023 via BenMAP. |
| **Baseline incidence** | BenMAP default (2012–2014 data projected to 2025). Supplemented with county-specific data for comparison. |
| **Age distribution** | 14% ≥65, 26% <18 (most vulnerable groups for PM2.5) |

**Key limitation on baselines:** County-level baseline rates in BenMAP underestimate true local rates. West Oakland (proposed terminal site) has asthma ER visits, heart disease mortality, and cancer rates approximately **twice** the county average. Richmond census tracts near the rail line have mortality rates 10–50% above county average.

---

## 5. Statistical Methods / Concentration-Response Functions

The paper uses BenMAP default CRFs for most endpoints, with some replacements:

| Endpoint | Study used | Key beta estimate |
|---|---|---|
| All-cause mortality (WHO Basic) | Chen & Hoek (2020) | 0.8%/µg/m³ |
| All-cause mortality (WHO <12 µg/m³) | Chen & Hoek (2020) | 1.2%/µg/m³ |
| All-cause mortality (Race-Adjusted) | Di et al. (2017) for Black persons | 2.1%/µg/m³ |
| HA Stroke, COPD, pneumonia, CHF, all CVD | Yazdi et al. (2019/2021) | Stroke 5.2%, COPD 7.3%, AMI 3.4%, pneumonia 10.1%, CHF 7.6% per µg/m³ |
| Acute MI | Peters et al. (2004) | — |
| Asthma symptom days | Rabinovitch et al. (2006) | 0.002/µg/m³ |
| New asthma (age 0–4, 5–17) | Tetreault et al. (2016) | — |
| Hay fever/rhinitis | Parker et al. (2009) | — |
| Minor Restricted Activity Days | Ostro & Rothschild (1989) | — |
| Work Loss Days | Ostro (1987) | — |

---

## 6. Findings

### Health impacts at 1.0 µg/m³ scenario (middle scenario, 262,000 people)

| Endpoint | Estimated cases/year |
|---|---|
| Deaths (WHO Basic) | 2.8 (2.4, 3.2) |
| Deaths (WHO <12 µg/m³) | 3.9 (3.2, 4.6) |
| Deaths (Race-Adjusted) | 7.3 (6.0, 8.5) |
| HA Chronic Lung Disease | 5.0 (4.8, 5.2) |
| HA Congestive HF | 9.1 (8.7, 9.4) |
| HA Pneumonia | 8.3 (8.0, 8.6) |
| HA Stroke | 5.9 (5.1, 6.6) |
| HA All Cardiovascular | 13.4 (11.8, 15.0) |
| Acute MI (nonfatal) | 1.5 (0.3, 2.6) |
| Asthma Symptom Days (000s) | 27.0 (19.5, 43.3) |
| New Asthma (0–4) | 6.3 (6.1, 6.6) |
| New Asthma (5–17) | 4.4 (4.2, 4.5) |
| Hay Fever/Rhinitis | 64 (15, 111) |
| Minor Restricted Activity Days | 3.2 (2.7, 3.9) |
| Work Loss Days | 564 (476, 650) |

**Overall magnitude:** 1–6% increase over baseline rates depending on endpoint and scenario.

### Environmental justice finding

| Race/ethnicity | PM2.5 increment | Relative exposure |
|---|---|---|
| Hispanic | 0.82 µg/m³ | 1.15× |
| Black | 0.75 µg/m³ | 1.07× |
| Asian | 0.62 µg/m³ | 0.88× |
| White | 0.58 µg/m³ | 0.81× |
| Total | 0.71 µg/m³ | 1.00 |

Hispanic residents face 41% higher exposure than White residents; Black residents face 29% higher exposure.

---

## 7. Contributions

1. **First HIA of uncovered coal rail transport** — fills gap in the coal lifecycle HIA literature (combustion and mining were studied; transport was not).
2. **Demonstrates BenMAP in practice** — shows how the full HIA pipeline works: exposure increment → dispersion → population exposure → CRFs → health endpoints + economic values.
3. **Race/income disaggregation** — quantifies the disproportionate exposure burden on Black and Hispanic residents, relevant for environmental justice framing.
4. **Global implications** — the method is explicitly designed to generalize to coal transport globally (India, China, U.S. are the three largest coal users).

---

## 8. Replication Feasibility

- PM2.5 exposure data: available via California Air Resources Board Public Records Request
- Health outcome data: not specified (likely county-level public data via HCAI/CDPH)
- BenMAP software: publicly available from EPA
- No replication archive mentioned

---

## 9. Relevance to Capstone

**Direct relevance: BenMAP methodology demonstration.** This paper uses BenMAP for a California-specific HIA, the same software and approach the capstone is evaluating. It shows exactly how BenMAP's ΔHE formula works, what baseline and CRF inputs BenMAP provides, and where the default values come from (2012–2014 incidence, Yazdi et al. for hospitalizations).

**Note on endpoints:** Ostro et al. focus on hospital admissions and mortality — not ER visits. This is the "more severe" side of the severity gradient that the capstone discussion uses to contextualize BenMAP's ER visit values.

**Note on BenMAP CRFs:** This paper uses BenMAP defaults for hospitalizations (Yazdi et al.) but replaces the mortality function for low-PM2.5 environments (Chen & Hoek 2020 instead of the older default). This illustrates that BenMAP defaults can be and are replaced when better-fitting literature exists — relevant context for the capstone's argument about WTP alternatives to the COI defaults.

**Key limitation for capstone:** Ostro et al. do not address ER visits as an outcome category (Table 1 lists no ER endpoint). This is consistent with BenMAP's design — ER visits appear in BenMAP's COI module, but Ostro et al. focus on the more severe hospitalization and mortality endpoints.
