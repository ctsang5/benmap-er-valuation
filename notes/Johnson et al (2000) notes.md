# Johnson, Ruby Banzhaf & Desvousges (2000) — Reading Notes
*Health Economics 9: 295–317 (2000)*
**SOURCE PAPER: provides the WTP unit values transferred by Stieb et al. (2002) to value ED visits**

---

## 1. Research Question
What is the WTP to reduce acute episodes of respiratory and cardiovascular ill health, estimated using stated-preference (SP) methods? Can two different SP elicitation formats (graded-pair and discrete-choice) be combined to yield more valid and robust WTP estimates than either alone?

---

## 2. Audience
Health economists and environmental/regulatory economists. Directly motivated by need for morbidity WTP values for air pollution cost-benefit analysis (CBA). Paper is the published version of the 1998 Triangle Economic Research working report used by Stieb et al. (2002).

---

## 3. Method

### Survey Design
- **Setting**: Toronto area, Canada
- **Sample**: 399 randomly recruited subjects
- **Field period**: March–July 1997
- **Currency**: Canadian dollars (CAN$)
- **Format**: Computerized survey with information treatment (2-page article on heart/lung illness), 4 quiz questions, detailed health history, then SP questions

### Health State Description
Uses simplified Quality of Well Being (QWB) framework. Health states defined by 4 attributes (Table 1):

**Symptom (7 levels)**:
- NOSE: stuffy/runny nose and sore throat
- EYE: eye irritation
- FLUTTER: fluttering in chest, feeling light-headed
- BREATH: coughing, wheezing, shortness of breath
- ACHE: coughing/wheezing with fever, chills, aching
- SWELL: shortness of breath, swelling in ankles/feet
- PAIN: pain in chest or arm

**Duration**: 1, 5, or 10 days

**Daily activity (6 levels)**:
- NOLIM: no limitations (best)
- SOMELIM: physical limitations only
- NOSOC: physical limitations + no social/rec activities
- ATHOME: cannot leave house, can care for self
- NEEDHELP: cannot leave house, needs help caring for self
- INHOSP: in hospital, needs help caring for self (worst)

**Annual costs**: CAN$10–500 (graded-pair) / CAN$50–750 (discrete-choice)

### Two SP Elicitation Formats
**Graded-pair**: Rate preference intensity (1–7 scale) for pairs of health states. Elicits marginal trade-offs. 8 pairs per subject from 40-pair orthogonal design.

**Discrete-choice**: Choose among 3 alternatives (Initial Condition / Alternative A / Current Health). Directly elicits total WTP for improvement from a diminished state to current health. 8 choice sets per subject from 40-set design.

Both formats combined to produce joint WTP estimates using combined preference information.

### Econometric Models
**Graded-pair**: Ordered probit panel model with random effects (Eq. 5–7). Individual scale parameters μᵢ estimated (accounts for heterogeneous response variance). n=2,752 observations.

**Discrete-choice**: Random parameter logit (RPL) — used instead of conditional logit because conditional logit fails IIA test. RPL accommodates: (1) IIA violations, (2) within-subject correlation across 8 choice sets, (3) uncontrolled taste heterogeneity. Each β estimated as distribution (mean + SD).

**WTP calculation** (Eq. 13):
WTP = Σₕ (X*ₕⱼ − X⁰ₕⱼ) × βʰᵢ / [−(Zⁱ·γ) / (2√P)]

Marginal utility of money varies with personal characteristics Zⁱ (income, age, symptomatic status, etc.), allowing WTP transfer to different populations.

---

## 4. Data
- **Sample**: N=399 subjects, Toronto area
- **Health history**: personal diagnosis of respiratory/cardiac conditions, frequency of illness, pain ratings
- **Demographics**: age (mean not yet captured), income (1996 pre-tax household), education, employment
- **Quiz scores**: comprehension of health background material (0–4 questions correct)
- **Unit of observation**: subject-response pair (8 per subject = 3,192 graded-pair obs; 3,192 choice obs)
- **Software**: not stated in pp1–12

---

## 5. Statistical Methods (pp1–12)

### Graded-pair model (Table 3, N=2,752 observations):
Key coefficients (normalized scale: NOLIM=1.0, INHOSP=0.0):

**Activity levels:**
| Variable | Coefficient | Normalized | t |
|---|---|---|---|
| NOLIM | 0.9242*** | 1.0000 | 6.88 |
| SOMELIM | 0.0803*** | 0.4949 | 2.52 |
| NOSOC | 0.1243** | 0.5212 | 3.75 |
| ATHOME | −0.1026** | 0.3854 | −2.01 |
| NEEDHELP | −0.2796*** | 0.2795 | −7.22 |
| INHOSP | −0.7466*** | 0.0000 | −6.87 |

**Symptoms (interacted with lnDays):**
| Variable | Coefficient | Normalized | t |
|---|---|---|---|
| NOSE*LNDAYS | 0.2720*** | 0.6096 | 4.38 |
| EYE*LNDAYS | 0.1610*** | 0.5432 | 6.33 |
| FLUTTER*LNDAYS | −0.0862*** | 0.3953 | −3.38 |
| BREATH*LNDAYS | −0.0301 | 0.4288 | −1.34 |
| ACHE*LNDAYS | −0.1426*** | 0.3615 | −5.13 |
| SWELL*LNDAYS | −0.1559*** | 0.3535 | −7.39 |
| PAIN*LNDAYS | −0.0182 | 0.4360 | −0.63 |

RHO (within-subject correlation) = 0.1260*** — significant, confirming need for panel model.

**Utility of money covariates**: SCORE (−**), AGE (+**), SYMPTOMATIC (+**) — older and symptomatic subjects WTP more; subjects who scored better on quiz WTP less.

Model fit: LR χ²=536***, McFadden R²=0.076, n=2,752.

### Discrete-choice RPL (Table 4 — not yet captured):
RPL used because conditional logit fails IIA. Each β estimated as distribution (mean + SD). Activity SD parameters all significant → large preference heterogeneity for activity levels.

---

## 6. Findings

### Joint Model (Table 5, used for all WTP calculations, N=5,504)
Combined graded-pair + discrete-choice. Utility parameters constrained equal across formats; utility of money estimated separately per format. Joint model properties: gives more weight to format with smaller variance per parameter.

Activity coefficients (normalized, NOLIM=1.0, INHOSP=0.0):
| Activity | Coefficient | Normalized | t |
|---|---|---|---|
| NOLIM | 0.2683*** | 1.0000 | 4.47 |
| SOMELIM/NOSOC | 0.2299*** | 0.9410 | 9.39 |
| ATHOME | 0.0225 | 0.6220 | 0.84 |
| NEEDHELP | −0.1387*** | 0.3741 | −5.36 |
| INHOSP | −0.3820*** | 0.0000 | −9.48 |

### WTP Estimates (Table 6, 1997 CAN$, joint model, 90% CI from 1,000 bootstrapped draws)

WTP to avoid episode for selected symptoms and activity levels:

**BREATH (coughing, wheezing, shortness of breath) — most relevant for respiratory ED visits:**
| Duration | MILD | ATHOME | NEEDHELP | INHOSP |
|---|---|---|---|---|
| 1 day | $0ᵇ | $158 ($100–$225) | $286 ($224–$363) | $448 ($371–$536) |
| 5 days | $266 ($141–$405) | $435 ($299–$589) | $566 ($427–$732) | $712 ($566–$872) |
| 10 days | $415 ($249–$602) | $589 ($411–$789) | $721 ($537–$937) | $857 ($668–$1058) |

**PAIN (pain in chest or arm) — most relevant for cardiac ED visits:**
| Duration | MILD | ATHOME | NEEDHELP | INHOSP |
|---|---|---|---|---|
| 1 day | $14 | $190 ($125–$263) | $329 ($260–$411) | $510 ($426–$611) |
| 5 days | $338 ($193–$489) | $522 ($370–$693) | $663 ($508–$841) | $827 ($665–$1015) |
| 10 days | $516 ($322–$719) | $705 ($503–$934) | $848 ($645–$1084) | $1,002 ($791–$1240) |

**SWELL (shortness of breath + ankle swelling — heart failure):**
| Duration | MILD | ATHOME | NEEDHELP | INHOSP |
|---|---|---|---|---|
| 1 day | $56 | $229 | $365 | $535 ($443–$644) |
| 5 days | $439 | $621 | $761 | $908 ($737–$1111) |
| 10 days | $650 | $837 | $979 | $1,114 ($896–$1375) |

**Worked example (from paper):** WTP(BREATH, ATHOME, 1-day) = $158, 90% CI: $100–$225

**Key pattern**: Activity restriction dominates over symptom type. NOLIM vs INHOSP difference much larger than difference between any two symptoms at the same activity level. ~36% of sample symptomatic → WTP near zero for mild conditions (sample already worse than mild hypothetical states).

ᵇ Negative point estimate shown as zero. Interpretation: average current health in sample is *worse* than these mild conditions, so subjects not willing to pay to avoid them.

### Currency/Inflation Conversion for Capstone
To express in USD 2022:
- PPP 1997: 1 USD ≈ 1.20 CAD → divide by 1.20
- CPI adjustment 1997→2022: multiply by ~1.85
- Net multiplier: × (1.85/1.20) ≈ × 1.54

Representative conversions:
| Health state | 1997 CAN$ | USD 2022 (approx) |
|---|---|---|
| BREATH, ATHOME, 1 day | $158 | ~$243 |
| BREATH, ATHOME, 5 days | $435 | ~$670 |
| BREATH, INHOSP, 1 day | $448 | ~$690 |
| BREATH, INHOSP, 5 days | $712 | ~$1,096 |
| PAIN, INHOSP, 5 days | $827 | ~$1,273 |

Stieb et al.'s $2,000 CAD 1997 for a respiratory ED visit is consistent with the BREATH/ACHE range at moderate-to-severe activity restrictions over a multi-day episode.

---

## 7. Contributions
- Demonstrates feasibility of SP methods for morbidity valuation from complete multi-attribute health state descriptions
- First study to combine graded-pair and discrete-choice formats for health valuation, showing convergent validity
- Provides a comprehensive WTP lookup table for respiratory and cardiovascular episodes varying by symptom type, duration, and activity restriction
- Modular structure: WTP for individual components can be aggregated differently depending on policy application
- Funded by Health Canada, Environment Canada, Ontario Hydro — directly motivated by air pollution CBA needs
- Dave Stieb listed explicitly in acknowledgments as "Scientific Authority" — confirms this paper was the direct source for Stieb et al. (2002)'s WTP component

---

## 8. Replication Feasibility
- Triangle Economic Research, Durham, NC — private firm; survey data not publicly available
- 1998 working report (TER Technical Working Paper T-9807) is the unpublished precursor; same dataset
- All analysis done in GAUSS (Aptech Systems)
- No public replication archive; bootstrapped CIs from 1,000 draws of multivariate normal parameter distribution

---

## Project Relevance
- **Direct source of Stieb's WTP values**: The acknowledgments explicitly name "Dave Stieb" as Scientific Authority. This paper's WTP estimates were transferred into Stieb et al. (2002) to construct the total economic value of ED visits.
- **For the capstone**: To apply Johnson et al. values directly to Chen et al.'s California ED visits, need to: (1) select appropriate symptom (BREATH for respiratory, PAIN for cardiac), (2) select appropriate activity level (ATHOME or NEEDHELP for ED-severity episodes), (3) select duration (1-day acute to 5-day), (4) convert from 1997 CAN$ to current USD
- **Activity level mapping for ED visits**: An ED visit implies the patient cannot care for themselves at home (at minimum ATHOME or NEEDHELP) — so MILD category understates the relevant WTP. ATHOME or NEEDHELP are more appropriate for ED-presenting patients.
- **WTP per episode vs. per day**: These are total WTP to avoid the entire episode (1, 5, or 10 days), not per-day values. This matters for comparison with Richardson's per-symptom-day estimates.
- **Asymmetry in symptom vs. activity**: Activity restriction level matters much more than symptom type — a key insight for choosing which health state to match to wildfire smoke ED visits (characterized mainly by restriction severity, not specific symptom)
- Values consistent with Richardson ($87–$95/day × ~5 days ≈ $435–$475) vs. Johnson's BREATH/ATHOME/5-day = $435 CAD (~$670 USD 2022) — same order of magnitude after currency adjustment
