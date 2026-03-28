# Stieb et al. (2002) — Reading Notes

**Full citation:** Stieb, D.M., De Civita, P., Johnson, F.R., Manary, M.P., Anis, A.H., Beveridge, R.C. & Judek, S. (2002). Economic evaluation of the benefits of reducing acute cardiorespiratory morbidity associated with air pollution. *Environmental Health: A Global Access Science Source*, 1, 7.

**Open Access:** http://www.ehjournal.net/content/1/1/7

**Note on authorship:** F. Reed Johnson is a co-author here AND on Johnson, Banzhaf & Desvousges (2000). Dave Stieb and Paul De Civita are the "Scientific Authorities" acknowledged in Johnson et al. (2000) — they oversaw the WTP survey contract that feeds into this paper. This is the same team applying the Johnson et al. methodology to produce policy-ready dollar estimates.

---

## 1. Research Question

What is the full societal value of avoiding acute cardiorespiratory morbidity outcomes linked to air pollution — including not just medical costs and lost wages, but also pain, suffering, and disrupted life? And can we estimate this comprehensively by combining COI data with WTP data?

**Why it matters:** Previous benefits assessments either (a) used only COI, which understates true damages, or (b) applied crude WTP/COI multipliers uniformly across all conditions. This paper develops a comprehensive, condition-specific framework that adds the components together rather than multiplying.

---

## 2. Audience

Government analysts conducting regulatory benefit-cost analyses of air pollution policies, particularly in Canada. The approach is designed to produce estimates directly usable in policy assessments like the Canadian Sulphur in Gasoline study.

---

## 3. Method

### The Key Innovation: Adding Components, Not Multiplying

The total value of avoiding an acute morbidity episode (Eq. 1):

**V_T = V_AE + V_PS + V_COT + V_LP**

Where:
- **V_AE** = value of reduced averting expenditures (e.g., buying an air conditioner)
- **V_PS** = value of reduced pain and suffering, inconvenience, anxiety
- **V_COT** = cost of treatment (hospital, doctor, medication, out-of-pocket)
- **V_LP** = value of lost productivity (missed work days)

### How They Estimate Each Component

The authors combine data from **two separate studies** to cover all four components:

**Study 1 — Stated Preference Survey (captures V_PS + V_AE):**
- This IS the Johnson, Banzhaf & Desvousges (2000) survey
- 399 randomly selected subjects in Toronto, 1997
- Graded-pairs + discrete-choice formats (joint model)
- QWB-based health state descriptions with symptoms, activity restrictions, duration
- Payment vehicle: "illness-related costs not covered by the government health system or a company insurance plan"
- Respondents instructed to assume they have paid sick leave
- **Crucially:** Because Canada has universal health care and respondents assumed paid sick leave, this WTP captures ONLY the pain/suffering + averting components — NOT medical costs or lost wages. Those have to be added separately.

**Study 2 — Emergency Department COI Study (captures V_COT + V_LP):**
- Prospective data on 1,772 individuals visiting EDs in Saint John, Canada, 1992-1996
- Telephone follow-up 2 weeks after visit: duration, disposition, restricted activity days, missed work, health care utilization, expenses
- 393 randomly selected inpatient records for cost analysis
- Fully allocated costs: hospital, ED, physician visits, medications, equipment, out-of-pocket
- Stepwise OLS regression for cost model (Akaike's Information Criterion)

**Lost productivity:**
- V_LP = days of lost productivity × CAN$119.60 (1997 average daily wage)
- Work loss days = 21% of restricted activity days (from U.S. National Health Interview Survey)
- For asthma/respiratory symptom days: assumed 10% are work loss days

### Mapping Health Outcomes

Seven health outcomes mapped to symptoms and activity levels (Table 2):

| Outcome | Key Symptoms | % In Hospital |
|---|---|---|
| Acute Respiratory Symptom Day (ARS) | 70% upper respiratory, 30% eye irritation | 0% |
| Restricted Activity Day (RAD) | 40% upper resp, 15% each: eye, asthma/COPD, resp infection | 0% |
| Asthma Symptom Day (ASD) | 100% asthma/COPD | 0% |
| Respiratory ED Visit (REDV) | 44% asthma/COPD, 56% resp infection | 7% |
| Respiratory Hospital Admission (RHA) | 60% asthma/COPD, 40% resp infection | 37% |
| Cardiac ED Visit (CEDV) | 50% MI/angina, 27% CHF, 23% dysrhythmia | 48% |
| Cardiac Hospital Admission (CHA) | 59% MI/angina, 28% CHF, 13% dysrhythmia | 57% |

### Monte Carlo Estimation

1,000 iterations sampling from observed distributions of model parameters and input values, accounting for correlation among parameters. Reports central estimate and 95% CI (2.5th–97.5th percentiles).

---

## 4. Data

### From Study 1 (WTP — Johnson et al.)
- 399 subjects, Toronto, 1997
- Computerized survey with information treatment, quiz, health history
- Graded-pairs (8 per subject) + discrete-choice (8 per subject)
- ~5,500 total observations in joint model

### From Study 2 (COI — Saint John ED study)
- 1,772 individuals with ED follow-up interviews
- 393 inpatient records for cost analysis
- Saint John, Canada, 1992-1996
- Conditions: asthma, COPD, respiratory infections, CHF, dysrhythmias, MI/angina

### Duration and Disposition Inputs (Table 3)

Selected examples for hospital-admitted patients:

| Condition | % Critical Care | Mean Days In Hospital | Mean Days Out of Hospital | Mean Lost Work Days |
|---|---|---|---|---|
| Asthma | 23.1% | 4.4 | 9.3 | 2.8 |
| Respiratory Infection | 11.3% | 5.1 | 8.7 | 3.3 |
| CHF | 12.9% | 7.2 | 8.9 | 1.2 |
| MI/Angina | 65.0% | 6.0 | 3.2 | 2.4 |

---

## 5. Statistical Methods

### Cost of Treatment Model (Table 4)

V_COT = α + β_AS·AS + β_CHF·CHF + β_D·D + β_CC·CC + β_NCC·NCC + interaction terms

| Variable | Parameter Estimate ($) | Standard Error ($) |
|---|---|---|
| Intercept | 348.58 | 90.71 |
| Asthma (dummy) | 440.33 | 125.97 |
| CHF (dummy) | 1,680.09 | 406.92 |
| Duration (days) | 31.70 | 7.85 |
| Critical care (dummy) | 4,530.36 | 176.20 |
| Non-critical care (dummy) | 1,977.94 | 163.67 |
| AS×Duration | -27.71 | 9.17 |
| RI×Duration | -29.02 | 8.07 |
| MIA×Duration | -30.54 | 14.50 |
| RI×CC | -1,544.58 | 538.12 |
| DYS×CC | -2,402.73 | 906.97 |
| AS×NCC | -431.01 | 272.89 |
| MIA×NCC | +1,180.79 | 301.74 |
| CHF×NCC | -2,158.82 | 539.88 |

Key: Critical care adds ~$4,500; non-critical care adds ~$2,000. CHF adds $1,680 to base. MI/angina in non-critical care is $1,181 MORE than baseline non-critical care.

---

## 6. Findings

### Table 5 — The Core Results (all in 1997 CAN$)

| Endpoint | Cost of Treatment | Lost Productivity | WTP (in hospital) | WTP (out of hospital) | **Total** | **95% CI** | V_T/(CoT+LP) |
|---|---|---|---|---|---|---|---|
| Respiratory Hospital Admission | $2,800 | $300 | $670 | $410 | **$4,200** | ($3,400–$5,000) | 1.3 |
| **Cardiac Hospital Admission** | **$3,800** | **$270** | **$760** | **$340** | **$5,200** | **($4,000–$6,400)** | **1.3** |
| Respiratory ED Visit | $930 | $160 | $430 | $520 | **$2,000** | ($1,700–$2,500) | 1.9 |
| Cardiac ED Visit | $3,200 | $210 | $680 | $330 | **$4,400** | ($3,300–$5,600) | 1.3 |
| Restricted Activity Day | — | $25 | — | $23 | **$48** | ($13–$82) | 1.9 |
| Asthma Symptom Day | — | $12 | — | $16 | **$28** | ($11–$71) | 2.3 |
| **Acute Respiratory Symptom Day** | — | **$12** | — | **$1** | **$13** | **($0–$28)** | **1.1** |

### Key Patterns

1. **Cardiac > respiratory** for both admissions and ED visits. Driven by higher proportion of cardiac patients needing critical care and invasive procedures.

2. **Cost of treatment dominates** for hospital admissions and cardiac ED visits. For cardiac hospital admission: CoT = $3,800 out of $5,200 total (73%).

3. **Lost productivity is small.** For cardiac hospital admission: LP = $270 out of $5,200 (5%).

4. **Pain/suffering (WTP component) matters most for mild endpoints.** For acute respiratory symptom days: WTP = $1 out of $13 (8%), but LP = $12 (92%). For restricted activity days: WTP = $23 out of $48 (48%).

5. **V_T/(CoT+LP) ratios range from 1.1 to 2.3.** These are NOT the same as the Alberini & Krupnick WTP/COI ratios. Stieb's ratios are lower because the denominator (CoT+LP) is larger — it includes the full cost of treatment, not just out-of-pocket costs.

### The "6x" Claim in Context

The review essay compares Stieb's CAN$5,200 cardiac hospital admission with BenMAP's $1,161 cardiovascular ER visit. Converting:
- CAN$5,200 (1997) × 0.72 (CAD→USD) × 1.90 (CPI-Medical 1997→2015) ≈ **US$7,114** (2015)
- BenMAP cardiovascular ER visit: **US$1,161** (2015)
- Ratio: ~6.1x

**But this comparison has two important caveats:**
1. **Different endpoints:** Stieb's $5,200 is for a full cardiac HOSPITAL ADMISSION (57% in-hospital, 65% of MI patients in critical care). BenMAP's $1,161 is for an average cardiovascular ER VISIT (mixed severity, many treat-and-release). Hospital admissions are much more severe.
2. **Different scope:** Stieb's $5,200 is a COMPREHENSIVE value (COT + LP + WTP for pain/suffering). BenMAP's $1,161 is COI ONLY (medical costs). They are measuring different things.

The fair comparison is: Stieb's V_T/(CoT+LP) ratio of 1.3 for cardiac admissions — meaning the full value is 30% more than tangible costs alone. The "6x" comes from comparing a comprehensive value for a severe endpoint against a COI-only value for a milder endpoint — which conflates two separate issues (comprehensiveness and severity).

### Sensitivity Analysis

- Results NOT sensitive to demographic/health status inputs (survey sample vs. nationally representative values)
- Hospital admissions and ED visits: total value varied <10% when activity restriction weights changed
- Restricted activity days and asthma symptom days: highly sensitive to severity assumptions (54-57% lower to 65-104% higher)
- Acute respiratory symptom days: $12-$28 range depending on severity

### Illustrative Application: Toronto Sulfate Reduction

- Particulate sulfate declined from 5.0 to 3.8 μg/m³ (1984-86 to 1997-99)
- Population: 4.771 million (2000)
- Estimated benefits: CAN$1.4 million/year (95% CI $0.91–$1.8 million) for reduced cardiorespiratory ED visits and hospital admissions
- Does NOT include mortality or chronic morbidity benefits

### Comparison with U.S. Estimates

- Stieb's hospital admission estimates are LOWER than most U.S.-based studies
- Reasons: (1) lower treatment costs in Canada vs. U.S. (single-payer vs. multi-payer), (2) lower intensity of care for some conditions, (3) lower administrative/overhead costs
- The WTP component is also lower — possibly because universal health care reduces perceived risk of catastrophic financial consequences

---

## 7. Contributions

1. **First comprehensive, component-by-component valuation of acute air pollution morbidity.** Previous studies either used COI alone (understating), WTP alone (potentially double-counting some costs), or crude WTP/COI multipliers applied uniformly. Stieb et al. explicitly decompose the total value into its four components and estimate each from appropriate data sources.

2. **Demonstrated how to combine COI and WTP data without double-counting.** The stated preference survey was designed so respondents' WTP captures only the pain/suffering and averting components (because Canada's universal health care covers treatment costs and respondents assumed paid sick leave). Medical costs and lost productivity are then added separately from the ED study. This is ADDING components, not blending or averaging methods.

3. **Produced Canadian-specific estimates.** Previous benefits assessments relied on U.S. data. These estimates reflect Canadian treatment costs (lower than U.S.) and Canadian preferences (potentially different WTP under universal health care).

4. **Provided condition-specific rather than uniform valuation.** The mapping in Table 2 allows different valuations for cardiac vs. respiratory conditions, hospital admissions vs. ED visits, and different severity levels — rather than applying one number to all morbidity.

5. **Propagated uncertainty via Monte Carlo simulation.** All estimates come with 95% confidence intervals, which previous studies often lacked.

---

## 8. Replication Feasibility

- **WTP data:** From Johnson, Banzhaf & Desvousges (2000) — proprietary survey under Health Canada contract H4078-5-C174/01-SS
- **COI data:** From Stieb et al. (2000, *Can J Public Health* 91:107-112) and Anis et al. (2000, *Can J Public Health* 91:103-106) — Saint John ED study data
- **Software:** Analytica (Lumina Decision Systems) for Monte Carlo simulation [Ref 53]
- **Funding:** Health Canada
- **Open access paper:** Yes, freely available from BioMed Central
- **Additional file:** Table 6 with comparison to earlier studies available as supplementary PDF
- **Key supporting references:** Woolhandler & Himmelstein (1991, 1997) in *NEJM* for U.S. vs. Canadian administrative cost comparisons; Johnson, Fries & Banzhaf (1997, *J Health Econ* 16:641-665) for the earlier WTP/health-status-index integration framework
- **Total references:** 53

---

## 9. Connection to the Capstone

This is the paper that produces the **CAN$13/respiratory-symptom-day** and **CAN$5,200/cardiac-hospital-admission** figures cited in the review essay. It sits at the intersection of the two methodological streams the essay traces:

1. **Johnson et al. (2000)** developed the WTP survey tool → feeds into the V_PS + V_AE component
2. **The Saint John ED study** provides the V_COT + V_LP component
3. **Stieb et al. (2002)** adds them together to get comprehensive valuations

The paper demonstrates that "combining WTP with COI" means literally adding the components that each method captures, after carefully ensuring they don't overlap. This is what the essay means when it says Stieb et al. "combined the resulting WTP data with cost-of-illness data."
