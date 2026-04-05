

* The goal of this paper is to test whether health status measures (like QALYs) can systematically predict WTP for avoided acute illness, using meta-regression analysis. This is a method paper--it produces benefit transfer functions, not off-the-shelf dollar values for specific endpoints like ED visits.

* The dataset: 236 WTP estimates from 17 stated-preference studies of acute morbidity. All values converted to 2000 USD. The largest single source of estimates is Johnson et al. (2000) with 67 observations--the same Johnson et al. that Stieb et al. used.

* Each WTP estimate is characterized by:
  * Duration (DDAYS): number of days with the acute condition
  * Severity (DQWB): measured using the Quality of Well-Being (QWB) Scale, which scores health states on four dimensions: symptoms, mobility, physical activity, social activity. Each dimension gets a score; higher score = more severe. DQWB = sum of all four scores.
  * Study population characteristics: income, age, % male, country (US or not)
  * Study design: valuation method (open-ended, payment card, dichotomous choice), survey mode (in-person or not), whether published in peer-reviewed journal

* The key regression (log-linear form, Table 4 last column):
  * ln(WTP) = 0.50 * ln(DDAYS) + 1.97 * ln(DQWB) + 0.70 * ln(INCOME) + 2.56 * ln(AGE) + other controls
  * R-squared = 64.5%

* What do the coefficients mean?
  * **Duration elasticity = 0.50**: if you double the number of sick days, WTP goes up by about 41% (not 100%). WTP increases with duration but at a decreasing rate--diminishing marginal disutility of additional sick days.
  * **Severity elasticity = 1.97**: if you double the severity (DQWB), WTP goes up by about 292%. WTP increases with severity more than proportionately--people are disproportionately more willing to pay to avoid more severe illness.
  * Income elasticity = 0.70: health is a normal good but WTP is inelastic with respect to income.
  * Age elasticity = 2.56: older people are willing to pay more. Surprisingly large.

* The severity-vs-duration asymmetry is the key finding for the capstone:
  * Duration elasticity (~0.5) is about 4x smaller than severity elasticity (~2.0)
  * The QALY approach assumes both elasticities = 1 (WTP is proportional to QALY gains). This paper rejects that assumption (F-test p < 0.001).
  * What this means: a short, severe illness is undervalued by QALYs (because QALYs weight duration equally with severity), and a long, mild illness is overvalued by QALYs.

* Why does this matter for the capstone?
  * ED visits are short-duration, high-severity events. The severity elasticity (~2.0) dominates for these events. This means the COI-vs-WTP gap should be especially large for ED visits--exactly what Stieb et al. found (1.9x for respiratory EDVs where pain/suffering exceeds treatment costs).
  * This provides theoretical backing for the claim that COI systematically undervalues ED visits specifically.

* The four QWB dimensions don't contribute equally to WTP:
  * Mobility and physical activity restrictions drive WTP far more than symptoms or social activity restrictions (F-test rejects equal weighting, p < 0.05).
  * This contradicts the simple additive QWB composite score assumption.

* Benefit transfer functions (Table 6): the paper produces two prediction equations that can estimate WTP for any acute condition given its severity, duration, and population characteristics.
  * Example predictions (Table 7): range from $45 (1 day, mild symptoms, moderate restrictions) to $706 (10 days, vomiting, severe restrictions). All in 2000 USD.

* Limitations for the capstone:
  * This paper only covers acute morbidity, not chronic conditions.
  * It estimates private WTP only--doesn't capture externalized costs (insurance-covered medical expenses, lost productivity covered by sick leave).
  * The paper doesn't produce dollar values for ED visits. It's a framework for generating WTP estimates from illness characteristics, not a source of numbers to plug into a calculation.

