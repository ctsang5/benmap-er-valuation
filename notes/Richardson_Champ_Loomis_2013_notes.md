# Richardson, Champ & Loomis (2013) — Reading Notes
*Land Economics 89(1): 76–100 (February 2013)*
**WTP PAPER: first to estimate WTP:COI ratio specifically for wildfire smoke morbidity**

## 1. Research Question
What is the individual willingness to pay (WTP) for a reduction in wildfire smoke–induced symptom days, and how does this compare to cost-of-illness (COI) estimates? Estimates WTP using both the Defensive Behavior Method (DBM) and Contingent Valuation Method (CVM), and compares both to traditional and comprehensive COI.

## 2. Audience
Environmental and natural resource economists, EPA regulatory analysts, wildfire cost researchers. Funded by Agricultural Experiment Station, Colorado State University. First study to apply the WTP:COI comparison specifically to wildfire smoke (all prior comparisons were for other pollutants).

## 3. Method

### Survey Design
Mail survey of residents in 5 Southern California cities (Duarte, Monrovia, Sierra Madre, Burbank, Glendora) near the **2009 Station Fire** — largest fire in Los Angeles County history at the time. Survey administered ~3 months after fire.
- Total usable responses: **413** (response rate: ~50%)
- Respondents reporting health symptoms: **156**
- Respondents taking defensive actions: **366 (89%)**
- Eligible CVM respondents (had symptoms): **157**

### Defensive Behavior Method (DBM)
Based on Bockstael & McConnell (2007) health production function framework. WTP = price of defensive input ÷ marginal product of that input on health.

Of 15 defensive actions tracked, only **"Used a home air cleaner"** had a statistically significant negative effect on symptom days (also found to be endogenous — instrumented via Hausman test).

Health production function estimated as maximum simulated likelihood (Deb & Trivedi 2006) joint model:
- **Symptom days**: negative binomial regression (Eq. 16)
- **Air cleaner use**: probit regression (Eq. 17)
- N = 377; latent factor λ = 0.858*** (significant — air cleaner users are predisposed to experience more symptoms)

Air cleaner marginal effect on symptom days: **−0.31** (discrete change from binary variable)
Average reported cost of air cleaner: **$26.93**

WTP_DBM = $26.93 / 0.31 = **$86.87 per symptom day**

### Contingent Valuation Method (CVM)
Dichotomous choice WTP question: would you pay $[bid] to reduce all household symptom days by 50%?
- Bid amounts: $10, $25, $50, $75, $100, $150, $200, $300, $500, $750
- Log-normal WTP distribution assumed; log of bid included (restricts WTP ≥ 0)
- Estimated via probit regression (Table 7, N=157)

CVM model (Table 7) significant predictors of WTP:
- ln(Bid): −0.455*** (correct sign — higher bid → less likely to say yes)
- ln(Half of household symptom days): +0.338** (WTP increases in illness, at decreasing rate)
- Current heart condition: +0.695* (heart patients WTP more)
- College/technical graduate: +0.666** (more educated → higher WTP)
- Health insurance: −1.093*** (insurance reduces WTP — moral hazard / substitution effect)
- Lives in Duarte or Burbank: positive and significant (location effects)

WTP calculated at sample mean: **$95.03 per symptom day** (mean); **$8.51** (median)
- WTP for average 7-day illness episode: $400 total = $57/day

### Cost of Illness (COI)
From survey respondents who had symptoms:
- **COI_trad**: medical visits, Rx, OTC medications, lost wages, opportunity cost of care time — private out-of-pocket only (excludes insurance-paid costs)
  - Mean: **$3.02/symptom day**; median: **$0** (most sought no medical care)
- **COI_comp**: adds value of lost recreation days ($20.27/day consumer surplus for Pacific coast sightseeing, from Loomis 2005)
  - Mean: **$16.87/symptom day**; median: $13.51

## 4. Data
- **Health symptoms**: self-reported days of symptoms from Station Fire smoke exposure
- **Defensive actions**: 15 categories, binary indicators; cost self-reported
- **CVM bids**: random assignment from 10 levels
- **Demographics**: age (mean 59), 60% male, 79% White, 92% insured, mean income $83,500
- **Beliefs**: 86% heard about health effects; 90% believe smoke affects health
- **Setting**: summer/fall 2009, Station Fire near Los Angeles

## 5. Key Results (Table 8, 2009 USD)

| Method | Point Estimate | 90% CI |
|---|---|---|
| COI_trad | $3.02 | [$1.63–$4.41] |
| COI_comp | $16.87 | [$14.11–$19.62] |
| DBM WTP | $86.87 | [$76.56–$443.26] |
| CVM WTP | $95.03 | [$22.78–$610.42] |

**WTP:COI ratios:**
- WTP / COI_trad ≈ **30x**
- WTP / COI_comp ≈ **5x**

**Statistical tests:**
- WTP ≠ COI_trad at 90% level (non-overlapping CIs)
- WTP ≠ COI_comp at 90% level (non-overlapping CIs)
- DBM WTP = CVM WTP (null of equality cannot be rejected; two-sided p = 0.62, complete combinatorial test)

Note: wide CIs on WTP reflect high individual heterogeneity AND small sample (n=157).

## 6. Contributions
- **First study** to estimate WTP and WTP:COI ratio specifically for wildfire smoke–induced morbidity
- **Convergent validity**: DBM and CVM produce statistically indistinguishable estimates ($86.87 vs $95.03)
- Confirms Harrington & Portney (1987) theoretical prediction: COI substantially underestimates WTP
- Identifies **calibration factor of 5** (WTP/COI_comp) as conservative adjustment for wildfire smoke
- Authors note WTP values are within range of literature for other air pollutants (Johnson et al. 1997: $36–$194/day depending on symptom)

## 7. Limitations
- Excludes insurance-paid medical costs from COI_trad (so COI_trad is itself a lower bound on true COI)
- DBM cannot be applied to children (revealed preference requires autonomous choice)
- Small CVM sample (n=157) → wide CIs
- Results specific to Station Fire context (Southern California, 2009, suburban population)
- Only one defensive action (air cleaner) identified as effective — may not fully capture total averting expenditure

## 8. Replication
- Survey data not publicly posted; available from authors
- No formal replication archive
- Methods well-documented; Stata's `treatreg2` (Deb & Trivedi) used for DBM
- All values in 2009 USD

## Project Relevance
- **Core WTP alternative for the capstone**: $87–$95 per symptom day is the WTP-based comparator to BenMAP COI values
- The WTP values are per **symptom day**, not per ED visit — to apply to Chen et al.'s ED visit counts, we need to bridge the outcome metric (symptom day → ED visit episode)
- The calibration factor of **5x** (WTP/COI_comp) or **30x** (WTP/COI_trad) could be applied to BenMAP's $36,000 hospital COI to derive an upper-bound WTP estimate
- DBM = CVM validates that both approaches give similar answers — supports using either as a benchmark
- The 30x ratio for wildfire specifically exceeds ratios for other pollutants — consistent with Aguilera et al.'s finding that wildfire PM2.5 is more toxic (and presumably more aversive)
- COI_trad = $3.02 comes entirely from private out-of-pocket costs. The $36,000 BenMAP figure includes hospital direct costs + lost earnings — conceptually closer to COI_comp territory, but still a COI measure. The WTP:COI ratio in the capstone context depends on which COI benchmark we use.
- **Key quote**: "if policy makers use COI estimates to quantify the cost of health damages from wildfire smoke, applying a conservative calibration factor of five found in this study may more accurately reflect the true value of these damages" (p. 96)
