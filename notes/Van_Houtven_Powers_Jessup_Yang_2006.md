# Van Houtven, Powers, Jessup, and Yang (2006) — Reading Notes

**Full citation:** Van Houtven, G., Powers, J., Jessup, A., & Yang, J.-C. (2006). Valuing avoided morbidity using meta-regression analysis: What can health status measures and QALYs tell us about WTP? *Health Economics*, 15(8), 775--795.

**DOI:** 10.1002/hec.1105

**Affiliations:** RTI International (Van Houtven, Yang); US EPA (Powers); US DHHS (Jessup)

---

## 1. Research Question

Can QALY-based health status measures (HSMs) --- specifically the Quality of Well-Being (QWB) Scale --- be systematically combined with WTP studies to build **benefit transfer functions** that predict WTP for avoided acute morbidity?

Two sub-questions:
1. Is there a systematic, theory-consistent relationship between illness severity (measured by QWB scores) and WTP?
2. Is the common assumption of a **constant dollar value per QALY** valid? (They test and reject it.)

**Why it matters:** Policy analysts doing cost-benefit analysis for EPA regulations need WTP values for health endpoints, but they can't commission a new survey for every endpoint. If a regression equation can predict WTP from an illness's severity and duration, that equation becomes a **benefit transfer function** --- a formula for generating WTP estimates without new primary research.

---

## 2. Audience

Health economists and regulatory policy analysts working on cost-benefit analysis for environmental, food safety, and public health programs. The paper bridges two literatures that usually don't talk to each other: the WTP/CBA literature and the QALY/CEA literature.

---

## 3. Method

### Approach

**Meta-regression analysis** --- a specific form of meta-analysis that uses regression to identify what factors systematically explain variation in WTP estimates across studies. Three purposes: (1) research synthesis, (2) hypothesis testing, (3) prediction (benefit transfer).

Builds on and extends Johnson et al. [3] by adding 12 more studies (183 additional estimates) and controlling for more covariates.

### Conceptual Framework

Standard utility maximization: U = U(H, X), subject to budget constraint Y = PX.

WTP for health improvement derived as **compensating variation (CV)**:
- V(H0, Y, P) = V(H0 + DH, Y - CV, P)

WTP for avoiding health decline derived as **equivalent variation (EV)**:
- V(H0 - DH, Y, P) = V(H0, Y - EV, P)

Key point: Private WTP should capture (1) avoided direct medical costs, (2) avoided indirect costs (lost income/production), and (3) avoided pain and suffering. But if costs are externalized through insurance or sick leave, private WTP will **underestimate** societal welfare.

### QALY Framework and the Constant-Value Hypothesis

Under restrictive QALY assumptions: WTP = alpha * (DQALY)^beta, where beta = 1 implies a constant dollar value per QALY (~$100,000/QALY derived from annualized VSL). The paper tests whether beta = 1.

Decomposition: if DQALY = Dq * Dt (change in quality x change in duration), then constant QALY value implies elasticities of WTP w.r.t. both Dq and Dt equal 1.

Under less restrictive conditions (Hammitt, Klose), WTP per QALY gain is **declining** with health status and size of QALY gain --- i.e., beta < 1.

### Health Severity Measure: QWB Scale

QWB chosen over HUI-III and EuroQol because it can be most readily applied as a severity index for acute illness. It has 4 dimensions:
- **Symptoms** (27 categories, from eye irritation to loss of consciousness)
- **Mobility** (3 levels)
- **Physical activity** (3 levels)
- **Social activity** (3 levels)

Total of 1,170 possible health states. Composite score = 1 - sum of four component scores. Higher composite = better health; higher component scores = more severe.

### Model Specifications

Eight specifications tested across two tables:
- **Functional form:** Linear, semi-log (ln(WTP) as DV), log-linear (ln on both sides)
- **Health index:** Composite DQWB score vs. four separate QWB dimension scores
- **Weights:** Sample-size-weighted (not equal-weighted as in Johnson et al.)
- **Clustering:** Huber-White robust standard errors clustered by study

### Hypotheses Tested

| Hypothesis | Expected direction | Result (pp. 1-12) |
|---|---|---|
| WTP increases with illness duration (DDAYS) | Positive | Confirmed (significant) |
| WTP increases with illness severity (DQWB) | Positive | Confirmed (significant) |
| WTP increases with income | Positive (normal good) | Confirmed (elasticity ~0.7) |
| WTP increases with age | Positive (worse baseline health) | Confirmed (elasticity ~2.56) |
| Constant WTP/QALY (beta = 1) | Tested | **Strongly rejected** (p < 0.001) |
| Four QWB components contribute equally | Tested | Rejected (F-test, p < 0.05) |
| WTP higher for avoiding decline (EV) vs. improving (CV) | Positive (loss aversion) | Not significant |

---

## 4. Data

### Sample
- **236 WTP estimates** from **17 stated-preference studies**
- Started with 53 observations from Johnson et al. (5 CV studies, US, late 1970s-1980s, cardiorespiratory/air pollution health effects)
- Added 183 estimates from 12 additional studies, mostly post-1990, US and international
- Selection criteria: (1) well-defined acute health effects, (2) adults' private values for own health, (3) stated preference methods, (4) severity expressible as QWB score, (5) duration quantifiable in days/episodes
- Inclusive approach to study quality --- did not exclude based on quality judgments, controlled for methodological differences via covariates instead

### Key Variables (Table 3 summary statistics)

| Variable | N | Mean | SD | Min | Median | Max |
|---|---|---|---|---|---|---|
| WTPACUTE (2000 USD) | 236 | $270.22 | $322.06 | $2.70 | $145.62 | $2,927.69 |
| DDAYS | 236 | 11.9 | 20.5 | 1 | 5 | 90 |
| DQWB | 236 | 0.37 | 0.11 | 0.17 | 0.36 | 0.57 |
| INCOME (2000 USD) | 236 | $46,348 | $13,618 | $21,891 | $47,067 | $88,020 |
| AGE | 236 | 45.2 | 6.8 | 35.4 | 44.5 | 68 |
| US (dummy) | 236 | 0.39 | | 0 | 0 | 1 |
| WTPAVOID (dummy) | 236 | 0.88 | | 0 | 1 | 1 |
| JOURNAL (dummy) | 236 | 0.67 | | 0 | 1 | 1 |
| SAMPLE SIZE | 236 | 316 | 152 | 20 | 399 | 832 |

- All WTP converted to 2000 USD via CPI; foreign currencies first converted via PPP
- Health effects characterized on two dimensions: **duration** (DDAYS) and **severity** (QWB scores)
- 88% of WTP estimates are for **avoiding a decline** (EV framing); 12% for improving health (CV framing)
- 39% of estimates from US studies; 61% international

---

## 5. Statistical Methods

- **Weighted least squares** (weighted by sample size, not inverse variance --- few studies report SEs)
- **Clustered robust standard errors** (Huber-White) corrected for within-study correlation
- **Functional forms tested:** linear, semi-log, log-linear
- Log-linear preferred on conceptual grounds: (1) WTP -> 0 as health change -> 0, (2) marginal effects of severity/duration not independent of income, (3) allows direct test of constant QALY value
- **R-squared range:** 44-65% across specifications; log-linear with composite QWB achieves R^2 = 64.5%
- Robustness: results stable when top 2 WTP outliers (>$1,000) excluded

---

## 6. Findings

### Scope Test Results (Tables 4 and 5)

WTP passes the scope test across all specifications:

**Duration (DDAYS):**
- Linear: +$4.80 per additional day avoided (t = 3.59)
- Log-linear: elasticity = 0.50 (t = 12.59) --- a 10% increase in days avoided raises WTP by ~5%

**Severity (DQWB, composite):**
- Linear: +$16 per 0.01 QWB increment (t = 2.82)
- Log-linear: elasticity = 1.97 (t = 3.26) --- WTP is highly responsive to severity

**Income:**
- Log-linear elasticity = 0.70 (t = 2.13) --- health is a normal good, positive but inelastic
- US dummy not significant after controlling for income

**Age:**
- Log-linear elasticity = 2.56 (t = 1.78) --- large positive effect, consistent with declining marginal utility of health (older = sicker = higher WTP for an increment)

### Decomposed QWB Results (Table 5)

The four QWB dimensions do NOT contribute equally to WTP:
- **Mobility score:** largest, most consistently significant (coefficient = 2,897 in linear, t = 5.86; log-linear elasticity effect = 10.94, t = 9.93)
- **Physical activity score:** large, significant (coefficient = 2,381 in linear, t = 1.86; log-linear = 10.49, t = 3.65)
- **Social activity score:** moderate, generally insignificant
- **Symptom score:** smallest, insignificant

**F-test rejects** the restriction that all four scores have equal marginal effects (p < 0.05 across all specifications). This contradicts the additive assumption of the composite QWB score.

Interpretation: People's WTP is driven more by functional limitations (can't move, can't do physical activities) than by symptoms alone (coughing, wheezing). This makes sense --- symptoms are uncomfortable but functional restrictions disrupt life.

### Other Variables
- WTPAVOID: not significant (no strong evidence of loss aversion)
- Study design dummies (OPEN ENDED, PAYMENT CARD, IN PERSON): not significant
- JOURNAL: sometimes negative at 0.10 level (peer-reviewed values slightly lower)

---

### Testing the Constant WTP/QALY Assumption

The QALY valuation approach assumes WTP = alpha * (DQALY)^beta with beta = 1, which implies:
- The elasticity of WTP w.r.t. duration (DDAYS) = 1
- The elasticity of WTP w.r.t. severity (DQWB) = 1
- Both elasticities are equal to each other

**All three restrictions are rejected:**

| Test | Null hypothesis | Result |
|---|---|---|
| Both elasticities = 1 | beta_DDAYS = beta_DQWB = 1 | **Rejected** (F-test, p < 0.001) |
| Both elasticities equal | beta_DDAYS = beta_DQWB | **Rejected** (p = 0.026) |

**What the elasticities actually are:**
- **Duration elasticity = 0.50** --- WTP increases *less* than proportionately with duration. A 10x increase in sick days yields only ~3x more WTP. Consistent with declining marginal disutility of duration (the 10th sick day hurts less than the 1st).
- **Severity elasticity = 1.97** --- WTP increases *more* than proportionately with severity. Doubling the QWB score (twice as severe) yields ~4x more WTP. Consistent with decreasing marginal utility of health (the sicker you already are, the more you'll pay for an increment of improvement).

**Implication:** The common practice of valuing health changes at ~$100,000/QALY (derived from annualized VSL) is **not supported** for acute morbidity. The QALY approach overvalues long-duration, low-severity conditions and undervalues short-duration, high-severity conditions relative to what people actually report they'd pay.

### Benefit Transfer Functions (Table 6)

Two final specifications selected for policy application, after dropping insignificant variables:

**BT Function 1** (composite QWB, WLS, R^2 = 63.5%, N = 236):

| Variable | Coefficient | t-stat |
|---|---|---|
| ln(DDAYS) | 0.501 | 13.07 |
| ln(DQWB) | 2.339 | 6.23 |
| ln(INCOME) | 0.777 | 3.01 |
| ln(AGE) | 2.591 | 2.06 |
| US | -0.181 | -1.52 |
| WTPAVOID | 0.799 | 1.72 |
| JOURNAL | -0.357 | -2.05 |
| CONSTANT | -12.031 | -1.66 |

**BT Function 2** (4 separate QWB scores, MLE, N = 235):

| Variable | Coefficient | t-stat |
|---|---|---|
| ln(DDAYS) | 0.477 | 12.93 |
| beta | 1.239 | 2.22 |
| QWBSYSCORE (eta_1) | 0.357 | 1.31 |
| QWBMOBSCORE (eta_2) | 2.120 | 4.45 |
| QWBSACSCORE (eta_3) | 0.476 | 2.22 |
| QWBPACSCORE (eta_4) | 1.000 | (restricted) |
| ln(INCOME) | 0.833 | 3.96 |
| ln(AGE) | 2.987 | 2.49 |
| %MALE | -0.017 | -2.61 |
| US | -0.101 | -0.73 |
| WTPAVOID | 0.516 | 1.25 |
| JOURNAL | -0.382 | -1.96 |
| CONSTANT | -13.293 | -2.02 |

Both functions drop survey method dummies (OPEN ENDED, PAYMENT CARD, IN PERSON) as jointly insignificant.

### Out-of-Sample WTP Predictions (Table 7)

Four illustrative acute conditions, each at 1 and 10 days duration. All predictions assume: INCOME = $45,000, AGE = 45, US = 1, WTPAVOID = 1, JOURNAL = 1. Smearing factor applied for log retransformation.

| Condition | Symptoms | Functional restrictions | DQWB | Duration | BT Func 1 WTP | BT Func 2 WTP | QALY est. |
|---|---|---|---|---|---|---|---|
| 1 | Breathing smog/unpleasant air | Moderate | 0.284 | 1 day | **$45** ($39-$51) | **$124** ($68-$181) | $78 |
| 1 | Same | Moderate | 0.284 | 10 days | **$143** ($130-$155) | **$372** ($228-$516) | $778 |
| 2 | Cough, wheeze, shortness of breath | Moderate | 0.44 | 1 day | **$125** ($89-$162) | **$158** ($100-$216) | $121 |
| 2 | Same | Moderate | 0.44 | 10 days | **$397** ($264-$529) | **$474** ($258-$691) | $1,205 |
| 3 | Headache or dizziness | Severe | 0.517 | 1 day | **$182** ($109-$256) | **$219** ($111-$327) | $142 |
| 3 | Same | Severe | 0.517 | 10 days | **$578** ($318-$839) | **$656** ($264-$1,048) | $1,416 |
| 4 | Sick, vomiting | Severe | 0.563 | 1 day | **$223** ($120-$326) | **$230** ($102-$358) | $154 |
| 4 | Same | Severe | 0.563 | 10 days | **$706** ($345-$1,067) | **$689** ($227-$1,150) | $1,542 |

**Key patterns:**
- 10x duration → only ~3x WTP (BT functions) vs. 10x WTP (QALY approach)
- 2x severity → ~5x WTP (BT Function 1) --- severity matters much more than duration
- QALY approach **overestimates** for long-duration, mild conditions and **underestimates** for short-duration, severe conditions
- BT Function 2 gives higher values for mild conditions (less sensitive to symptom variation) but similar values for severe conditions

---

## 7. Contributions

1. **Demonstrated that QALY-based severity measures (QWB scores) systematically predict WTP.** This validates the use of HSMs as inputs to benefit transfer for CBA, bridging the CEA/CBA literatures.

2. **Tested and rejected the constant WTP/QALY assumption** (p < 0.001). WTP increases less than proportionately with duration (elasticity ~0.5) and more than proportionately with severity (elasticity ~2). The common ~$100,000/QALY valuation is not supported for acute morbidity.

3. **Found that the four QWB dimensions contribute unequally to WTP.** Mobility and physical activity restrictions drive WTP far more than symptoms or social activity restrictions. The equal-weighting assumption in composite QWB scores is rejected.

4. **Produced two benefit transfer functions** (Table 6) that can predict WTP for any acute health condition, given its QWB severity profile, duration, and the affected population's income and age. These are ready-made tools for regulatory benefit estimation.

5. **Extended the Johnson et al. (1997) meta-analysis** by more than quadrupling the sample (53 → 236 estimates) and adding controls for study population characteristics and design features, with results that confirm and strengthen the earlier findings.

### Limitations noted by the authors

1. **Only applies to acute conditions** --- chronic illness WTP literature was too sparse for comparable meta-analysis
2. **Age effect is unexpectedly large** (elasticity > 2.5) --- needs further investigation
3. **Only captures adults' private WTP** --- excludes externalized costs (insurance-covered medical costs, employer-paid sick leave) and altruistic values (parents' WTP for children's health). Private WTP may therefore **underestimate** total social benefits
4. **Depends on the quality of underlying WTP estimates and QWB scores** --- if either measure has systematic biases, results would be weakened

---

## 8. Replication Feasibility

- **Data:** 236 WTP estimates compiled from 17 published studies (listed in Appendix A / Table A1). No replication archive or dataset provided. Would need to reconstruct from original publications.
- **QWB scores:** Assigned by the authors using published QWB weights (Kaplan et al. 1989). Assignments could be reproduced from the health effect descriptions in each study, but involve subjective judgment.
- **Software:** Not specified (likely Stata, given Huber-White clustering references)
- **Funding:** US EPA Contract 68-C-01-142; US FDA Contract 223-01-2466
- **Total references:** 56

### Studies included in the meta-analysis (Table A1)

| # | Study | Method | Health effect | Country | N obs |
|---|---|---|---|---|---|
| 1 | Alberini & Krupnick (1998) | CVM | Acute respiratory symptoms | Taiwan | 3 |
| 1 | Alberini et al. (1997) | CVM | Acute respiratory symptoms | Taiwan | 2 |
| 2 | Bala et al. (1998) | CVM | Pain from shingles | US | 1 |
| 3 | Chestnut et al. (1996) | CVM | Angina attacks | US | 2 |
| 3 | Rowe & Chestnut (1985) | CVM | Asthma attacks | US | 1 |
| 4 | Dickie & Ulery (2002) | CVM | Acute symptoms | US | 15 |
| 5 | **Johnson et al. (2000)** | Conjoint | Acute symptoms/activity restrictions | Canada | **67** |
| 6 | Kartman et al. (1996) | CVM | Angina attacks | Sweden | 12 |
| 7 | Keith et al. (2000) | CVM | Allergic rhinitis | US | 1 |
| 8 | Liu et al. (2000) | CVM | Cold | Taiwan | 1 |
| 9 | Ready et al. (2001) | CVM | Acute symptoms | Norway | 10 |
| 9 | Ready et al. (1999) | CVM | Acute symptoms | Norway, Netherlands, Portugal, Spain, England | 27 |
| 10 | Navrud (2001) | CVM | Acute symptoms | Norway | 18 |
| 11 | Lee et al. (2002) | Conjoint | Influenza symptoms | US | 3 |
| 12 | Torrance et al. (1999) | CVM | Acute exacerbation of chronic bronchitis | Canada | 2 |
| 13 | Jacobs et al. (2002) | CVM | Hepatitis A | US | 1 |
| 14 | **Chestnut et al. (1988)** | CVM | **Angina attacks** | US | **12** |
| 15 | Dickie et al. (1988) | CVM | Acute symptoms | US | 2 |
| 16 | **Loehman et al. (1979)** | CVM | **Acute symptoms** | US | **36** |
| 17 | **Tolley & Babcock (1986)** | CVM | **Acute symptoms** | US | **20** |

Studies in bold were included in the original Johnson et al. (1997) meta-analysis (53 obs from 5 studies). Note: Johnson et al. (2000) contributes the most observations (67) and is a capstone source.

---

## 9. Connection to the Capstone

Van Houtven et al. (2006) connects to the capstone in two distinct ways --- one for the **review essay** and one for the **valuation calculation** --- and it's important to distinguish between them.

### Role in the review essay

In the essay's narrative about why EPA still uses COI despite available WTP evidence, Van Houtven serves as the **culmination of the WTP challenge period** (2000-2006). The key argument: EPA's stated reason for not adopting WTP is that no WTP study directly values BenMAP's specific ER visit endpoints. Van Houtven's benefit transfer functions offer a potential **off-ramp** from that objection --- if you can predict WTP from any illness's severity and duration, you don't need a bespoke survey for every ICD code. The essay then shows that EPA chose not to adopt this approach, partly because of heterogeneity in the underlying studies and partly because of infrastructure lock-in with COI.

### Role in the valuation calculation

For the capstone's core arithmetic --- multiplying Chen et al.'s attributable EDV counts by dollar values under COI vs. WTP --- Van Houtven is **less directly useful** than Stieb et al. or Alberini & Krupnick. Those papers give you actual dollar values for ER-type endpoints. Van Houtven gives you a *method* (the BT functions in Table 6) for *generating* values, which requires:
1. Assigning QWB scores to the specific health conditions (respiratory ER visit, cardiovascular ER visit)
2. Specifying duration, income, age, and other parameters
3. Plugging into the log-linear equation and exponentiating

This is feasible but introduces an additional layer of methodological judgment. The paper is more about **why a general WTP approach is viable** than about providing off-the-shelf numbers.

### Specific connections to other capstone sources

- **Johnson, Banzhaf & Desvousges (2000):** Contributes 67 of the 236 WTP estimates --- the single largest source in the meta-analysis. Van Houtven explicitly builds on and extends the earlier Johnson et al. (1997) meta-regression.
- **Alberini & Krupnick:** Two Alberini/Krupnick studies (1997 and 1998) contribute 5 estimates. The Taiwan data that produced the 2-4x WTP/COI ratio in Alberini & Krupnick (2000) feeds into this synthesis.
- **Stieb et al. (2002):** Not directly included in the meta-analysis (Stieb's estimates are comprehensive WTP+COI composites, not raw stated-preference WTP). But Stieb's ED-specific values (CAN$4,400 cardiac, CAN$2,000 respiratory) can be compared against predictions from Van Houtven's BT functions as a consistency check.

### Key insight for the capstone argument

The finding that **severity drives WTP more than duration** (elasticity 2.0 vs. 0.5) has a direct implication: a single ER visit (short duration, high severity) is worth *disproportionately more* per QALY than a multi-day mild illness. This means the COI-vs-WTP gap should be especially large for ER visits, because ER visits involve intense, short-duration, high-severity events where the severity elasticity dominates. This is consistent with the 3-5x ratios found in Stieb et al. for ED-specific endpoints.
