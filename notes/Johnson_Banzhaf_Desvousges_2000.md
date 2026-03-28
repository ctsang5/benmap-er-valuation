# Johnson, Banzhaf & Desvousges (2000) — Reading Notes

**Full citation:** Johnson, F.R., Banzhaf, M.R. & Desvousges, W.H. (2000). Willingness to pay for improved respiratory and cardiovascular health: A multiple-format, stated-preference approach. *Health Economics*, 9(4), 295-317.

---

## 1. Research Question

Can stated-preference (SP) survey methods produce valid, meaningful WTP estimates for acute respiratory and cardiovascular health events? And does combining two different SP elicitation formats (graded-pair and discrete-choice) yield more robust estimates than using either format alone?

**Why it matters:** Revealed-preference data (observing actual market behavior) generally fails for health valuation because insurance, universal health care, and unrepresentative market participants obscure true supply and demand. Contingent valuation (CV) — asking a single "how much would you pay?" question — is poorly suited to valuing health states with multiple attributes. SP methods offer a way to decompose health states into attributes and estimate WTP for each component.

---

## 2. Audience

Health economists, environmental economists, and regulatory analysts doing benefit-cost analysis of health interventions and air quality regulations. The paper explicitly frames its contribution in terms of producing WTP estimates that can be transferred to different policy contexts (benefit transfer).

---

## 3. Method

### The Survey Tool

Health states are described using a **modified Quality of Well-Being (QWB) Index** with four attributes:

| Attribute | Levels |
|---|---|
| **Symptom** | 7 levels: Nose (stuffy/runny nose, sore throat), Eye (irritation), Flutter (fluttering in chest, light-headed), Breath (coughing, wheezing, shortness of breath), Ache (coughing/wheezing + fever/chills/aching), Swell (shortness of breath + ankle/feet swelling), Pain (chest or arm pain) |
| **Duration** | 3 levels: 1 day, 5 days, 10 days |
| **Daily activity** | 6 levels: NOLIM (no limitations), SOMELIM (some physical limitations), NOSOC (physical limitations + no social/recreational activities), ATHOME (housebound, can self-care), NEEDHELP (housebound, needs help with self-care), INHOSP (hospitalized, needs help with self-care) |
| **Annual cost** | 6 levels each; graded-pair: CAN$10-500; discrete-choice: CAN$50-750 (higher to induce trade-offs) |

### Two Elicitation Formats

**Graded-pair:** Subject sees two health state profiles side by side. Rates preference intensity on a 1-7 scale (1 = strong preference for A, 4 = indifference, 7 = strong preference for B). No baseline reference point — designed to capture *marginal* trade-offs among attributes.

**Discrete-choice:** Subject sees three options: an Initial Condition (severe health state, $0 cost), Alternative A (intermediate severity, intermediate cost), and Alternative B (subject's current health, high cost). Subject picks the most preferred. This format captures *total* values for moving from a diminished health state back to current health.

### Experimental Design

- 40 graded pairs and 40 choice sets (nearly orthogonal main-effects arrays)
- Constraints imposed to eliminate implausible combinations (e.g., mild symptoms like NOSE/EYE never paired with severe activity restrictions beyond NOSOC or costs above CAN$100; severe symptoms never paired with NOLIM)
- Each subject saw 8 graded pairs and 8 choice sets, randomly drawn from a 5-block design
- Computerized administration with information treatment (2-page article on heart/lung illness), 4 quiz questions, and detailed health history questions

### Why Two Formats?

Citing Huber et al. (1993): each format relies on a different cognitive process. Choice format better predicts short-term, familiar purchase behavior; graded-pairs better predicts longer-term adaptation to unfamiliar products. Acute health events have attributes of both. Using both formats captures a fuller picture of preferences than either alone.

---

## 4. Data

- **Sample:** 399 randomly recruited subjects in the Toronto area
- **Time period:** March-July 1997
- **Administration:** Computer-based survey
- **Observations:** 2,752 for graded-pair model (399 subjects x 8 questions, minus exclusions); similar for discrete-choice
- **Demographic/health data collected:** Personal health history, family health history, socio-demographics, current health condition (used to construct Alternative B in choice sets)

---

## 5. Statistical Methods

### Graded-Pair Analysis: Ordered Probit Panel Model

- Responses are ordinal ratings of utility differences between health state pairs
- Ordered probit accounts for discrete, ordinal nature of responses
- Random effects panel model accounts for correlation among each subject's 8 responses (RHO = 0.1260, significant)
- Individual scale parameters (inverse of error variance) estimated as function of personal characteristics — captures "noise" in ratings
- Marginal utility of money varies with personal characteristics (SCORE, AGE, EDUCATION, SYMPTOMATIC, VIMPORTANT) via square root of cost specification

### Discrete-Choice Analysis: Random Parameter Logit (RPL)

- Preferred over standard conditional logit because: (1) IIA assumption violated in the data; (2) conditional logit doesn't account for taste heterogeneity beyond marginal utility of money; (3) doesn't handle panel correlations
- Each beta coefficient estimated as a distribution (mean + standard deviation) — significant standard deviation indicates taste heterogeneity
- Current health state estimated from health history covariates (ASTHMA, BRONCHITIS, LUNGINFECTION, HEARTDISEASE)

### WTP Calculation

WTP = (sum of health attribute coefficient differences) / (marginal utility of money)

Marginal utility of money varies with personal characteristics, so WTP estimates can be transferred to populations with different demographics.

---

## 6. Findings

### From pages 1-12 (graded-pair and discrete-choice models separately):

**Graded-pair results (Table 3):**
- Symptoms: NOSE and EYE have highest utility (mildest); SWELL and ACHE have lowest (most severe). Five of seven symptoms significantly different from mean.
- Activity restrictions: Monotonically decreasing as expected (NOLIM best → INHOSP worst). SOMELIM and NOSOC reversed but statistically equivalent.
- Utility of money: Higher quiz scores → lower WTP; older and symptomatic subjects → higher WTP.
- Scale function: High quiz scorers and those without paid sick leave had less noisy responses; elderly and those who failed consistency checks had noisier responses.

**Discrete-choice RPL results (Table 4):**
- Symptom ranking differs from graded-pair: PAIN now worst (was middle in graded-pair); ACHE now milder (was severe in graded-pair). More variation in normalized coefficients (0.54-0.97 vs 0.35-0.61).
- Activity restrictions: All significant except ATHOME. Very little difference between NOLIM and SOMELIM (unlike graded-pair which showed a large gap).
- Standard deviations: No significant taste heterogeneity for symptoms, but substantial heterogeneity for activity restrictions.
- Current health covariates: All four conditions (ASTHMA, BRONCHITIS, LUNGINFECTION, HEARTDISEASE) significant — indicate worse health than sample average.

**Key observation:** The two formats produced different symptom rankings, supporting the paper's argument that combining formats captures a more complete picture of preferences.

### Joint Model (Table 5) — The Core Results

The authors pool data from both formats (5,504 total observations) into a single model to capture all available preference information. Key features:

- Health attribute coefficients (betas) constrained to be the **same** across both formats
- Utility of money functions estimated **separately** for each format (to account for systematic differences in how subjects processed cost in each task)
- SOMELIM and NOSOC combined into a single "MILD" category (subjects couldn't distinguish them)
- A relative scale function controls for different variance levels between the two datasets (graded-pair data had significantly more noise than discrete-choice)

**Joint model results:**
- **Symptom coefficients** show more variability and more statistical significance than either format alone. NOSE and EYE significantly milder than other symptoms; SWELL significantly worse.
- **Activity restriction coefficients** track the discrete-choice model more closely (where activity was more salient). Monotonically decreasing: NOLIM ≈ SOMELIM/NOSOC > ATHOME > NEEDHELP > INHOSP.
- **Key property:** Joint estimates fall between the two individual-format estimates in nearly every case, giving more weight to whichever format had the smaller variance (more precise estimate) for each parameter. This is exactly the desired behavior — it's not a simple average.

### WTP Estimates (Table 6)

WTP estimates for all plausible symptom × activity level × duration combinations, in **1997 CAN$**, with bootstrapped 90% confidence intervals (1,000 draws from the multivariate normal distribution of coefficients):

**Selected WTP values (1997 CAN$):**

| Condition | 1-day episode | 5-day episode | 10-day episode |
|---|---|---|---|
| BREATH + ATHOME | $158 (100-225) | $435 (299-589) | $589 (411-789) |
| BREATH + INHOSP | $448 (371-536) | $712 (566-872) | $857 (668-1058) |
| SWELL + ATHOME | $229 (164-306) | $621 (469-799) | $837 (634-1073) |
| SWELL + INHOSP | $535 (443-644) | $908 (737-1111) | $1,114 (896-1375) |
| PAIN + ATHOME | $190 (125-263) | $522 (370-693) | $705 (503-934) |
| PAIN + INHOSP | $510 (426-611) | $827 (665-1015) | $1,002 (791-1240) |
| NOSE + MILD | $0 (neg.) | $0 (neg.) | $44 (neg./199) |
| EYE + MILD | $0 (neg.) | $29 (neg./138) | $85 (neg./232) |

**Key patterns in WTP estimates:**
- **Activity restrictions matter more than symptom type.** Moving from MILD to INHOSP increases WTP dramatically for any given symptom. Differences between symptoms at the same activity level are smaller.
- **Duration increases WTP but with diminishing returns.** Going from 1 to 5 days roughly doubles WTP; going from 5 to 10 days adds another ~40%. This reflects the ln(duration+1) specification.
- **Mild symptoms produce zero or negative WTP.** For NOSE and EYE at MILD activity levels, estimated WTP is negative — meaning the average subject's current health was actually *worse* than these mild health states. 36% of subjects had experienced cardiovascular or respiratory conditions in the past year.
- **The most severe combinations reach ~CAN$1,000-1,100** (10-day SWELL or PAIN episodes requiring hospitalization).

---

## 7. Contributions

1. **Demonstrated feasibility of SP for acute health events.** Showed that stated-preference surveys can produce internally valid, severity-sensitive WTP estimates for short-duration respiratory and cardiovascular episodes — even from subjects who have never personally experienced the conditions. This answered a standing objection to WTP for ER-type endpoints.

2. **Proved the value of combining elicitation formats.** The two formats produced different symptom rankings because they activate different cognitive processes. The joint model captures the strengths of each: graded-pair is more informative about symptom trade-offs; discrete-choice is more informative about activity restriction trade-offs. The joint estimates give more weight to whichever format is more precise for each parameter.

3. **Produced transferable WTP estimates.** Because WTP is decomposed into individual health attributes (symptom, duration, activity level) and the marginal utility of money varies with demographics, the estimates can be recombined and recalibrated for different health conditions and different populations. This is the "benefit transfer" capability that makes the paper useful for policy applications like Stieb et al. (2002).

4. **Provided a modular health valuation framework.** Any combination of the 7 symptom types × 6 activity levels × 3 durations can be valued, subject to plausibility constraints. This modularity allows matching WTP estimates to specific policy-relevant health endpoints rather than using one-size-fits-all values.

---

## 8. Replication Feasibility

- **Data availability:** The survey data are proprietary (collected under a Canadian government contract: Public Works and Government Services Canada contract #H4078-5-C174/01-SS). Not publicly available.
- **Funding sources:** Health Canada, Environment Canada, Ontario Hydro, Ontario Ministry of Environment and Energy, Environnement et de la Faune Quebec.
- **Software:** All analysis performed in Aptech System's GAUSS software.
- **Replication materials:** No public replication archive. The experimental design, survey instrument development, and estimation procedures are described in detail in Johnson et al. (1998, *Medical Decision Making*) and Desvousges et al. (1996, Triangle Economic Research Report).
- **Scientific authorities on the project:** Dave Stieb and Paul De Civita (both later co-authors on Stieb et al. 2002).
- **Advisory panel:** Mike Fortin, Magnus Johannesson, Kerry Smith, David Streiner.

---

## 9. Connection to Stieb et al. (2002)

The acknowledgments section confirms the direct link: **Dave Stieb and Paul De Civita** are listed as the project's "Scientific Authorities" — the government officials overseeing the research contract. Both became co-authors on Stieb et al. (2002), which applied the Johnson et al. framework to produce the policy-relevant dollar estimates (CAN$13/respiratory symptom day, CAN$5,200/cardiac admission) used in your capstone's WTP literature review.
