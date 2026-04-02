# Literature Review Outline

## Introduction
- California wildfire seasons are worsening; smoke exposure drives ER visit spikes
- Capstone question: what do wildfire smoke ER visits cost, and does the measurement method matter?
- Preview the argument: EPA captures only the medical bill; the full cost is roughly 3-4x larger, and the gap determines whether smoke mitigation policies pass cost-benefit tests

## Section 1: How EPA Values an Emergency Department Visit

**Argues:** BenMAP's COI approach captures only the medical bill, producing values EPA itself calls "conservative lower bounds."

### 1A. The BenMAP COI pipeline
- BenMAP is EPA's standard tool for monetizing health benefits of air quality regulations. The dollar value it assigns to an avoided ER visit determines whether a regulation passes a cost-benefit test.
- Data pipeline: start with HCUP NEDS (national sample of ER discharges) -> filter by ICD diagnosis codes (crosswalked from ICD-9 to ICD-10 via CDC mapping) -> convert billed charges to actual costs using cost-to-charge ratios from the NIS -> compute discharge-weighted national mean -> deflate to 2015 dollars using medical CPI.
- Unit values: $1,161 per cardiovascular ER visit, $875 per respiratory ER visit (2015$).
- Source: BenMAP Appendix H, Section H.2.2, Table H-6.

### 1B. What COI means for ER visits specifically
- For ER visits, BenMAP defines COI as medical costs only. Unlike hospital admissions, which also include lost wages, ER visit COI excludes lost productivity entirely.
- EPA explicitly calls these "conservative (lower bound) estimates" and acknowledges downward bias from omitting WTP. The Science Advisory Board advised against applying a WTP adjustment, citing risk of "over-adjusting."
- The result: a known undercount that persists by institutional choice, not analytic necessity.
- Source: BenMAP Appendix H, Section H.2.1 (COI framing and SAB discussion).

**Transition:** If COI captures only the medical bill, what costs does a person actually bear when they visit the ER for a smoke-related illness?

## Section 2: What COI Leaves Out

**Argues:** COI misses three major categories of cost. For wildfire smoke, the missing categories dominate the total.

### 2A. Lost productivity
- ER patients miss work -- not just during the visit, but during recovery and follow-up. BenMAP excludes lost wages from ER visit COI entirely.
- Stieb et al. (2002) include lost productivity (V_LP) as a named component in their total valuation framework (V_T = V_AE + V_PS + V_COT + V_LP), making the omission explicit.
- Source: Stieb et al. (2002) component framework. BenMAP Appendix H for the wage exclusion.

### 2B. Pain and suffering
- The most fundamental omission. COI treats the ER visit as a financial transaction (bill paid), but the person experiencing chest tightness or an asthma attack bears a welfare cost with no line item on the hospital bill.
- Stieb et al. isolate this as V_PS (pain and suffering). In their Canadian universal healthcare context, medical costs are covered by the system, so the WTP they measure is primarily pain and suffering -- a relatively clean measure of exactly the gap COI misses.
- Source: Stieb et al. (2002) V_PS component.

### 2C. Defensive spending
- During wildfire smoke events, people buy air purifiers, masks, and cancel outdoor activities. These costs never appear in ER data because the point of defensive spending is to avoid the ER.
- Richardson et al. (2013) found that during the 2009 California Station Fire, 89% of respondents took defensive actions but only 5% sought medical care. COI captures costs for the 5% who showed up at a hospital and misses the 95% who suffered and spent money at home.
- Source: Richardson et al. (2013).

### 2D. Why the gap is largest for ER visits
- The COI-WTP gap is not constant across health endpoints. Van Houtven et al. (2006) found WTP elasticity with respect to severity (~2.0) is roughly 4x larger than elasticity with respect to duration (~0.5).
- ER visits are high-severity, short-duration events. WTP rises steeply with severity while COI scales with duration (more hospital days = higher bills). For events that are severe but brief, the gap widens.
- Van Houtven's F-test rejects the assumption of constant WTP per QALY (p < 0.001), meaning you cannot apply a single multiplier across all health endpoints.
- Source: Van Houtven et al. (2006).

**Transition:** If COI misses these costs, how do economists actually measure them? Two broad methods exist: ask people directly (stated preference) and observe their behavior (revealed preference).

## Section 3: Methods That Capture the Missing Costs

**Argues:** Both stated and revealed preference WTP methods produce valuations substantially higher than COI, and when both are applied to the same population, they converge.

### 3A. Stated preference: Stieb et al. (2002)
- **TODO: Re-read `sources/Stieb et al. (2002).pdf` before writing this subsection. Previous reading notes were deleted in Session 14 cleanup.**

### 3B. Revealed preference: Richardson, Champ & Loomis (2013)
- **TODO: Re-read `sources/Richardson, Champ & Loomis (2013).pdf` before writing this subsection. Previous reading notes were deleted in Session 14 cleanup.**

### 3C. What the two methods tell us together
- **TODO: Write after 3A and 3B are complete.**

**Transition:** With both frameworks established, the final step is to apply them to wildfire smoke ER visits in California.

## Section 4: The Gap Applied to California Wildfire Smoke

This section applies both valuation frameworks (COI and WTP) to Chen et al.'s wildfire smoke EDV counts to show the dollar difference between the two approaches.

### 4A. Chen et al.'s attributable EDV counts
- Two-stage model: quasi-Poisson regression per air basin, then random-effects meta-analysis. Wildfire smoke caused 4,597 respiratory ER visits and 889 cardiovascular ER visits in California, 2016-2019.
- Health impact function uses the same mathematical structure as BenMAP's standard formula (Appendix C, log-linear model).
- Note: respiratory association (+14.3%) is well-established. Cardiovascular association (+3.2%) is one of Chen's novel findings and rests on a less established evidence base.
- Source: Chen et al. (2023).

### 4B. COI valuation
- 4,597 respiratory x $875 + 889 cardiovascular x $1,161 = ~$5.05 million.
- This represents total medical bills. No lost wages, no pain and suffering, no defensive spending. This is what EPA would report as the "health benefit" of preventing these ER visits.
- Source: BenMAP Appendix H unit values x Chen et al. counts.

### 4C. WTP valuation
- **TODO: Write after reading Stieb et al. and completing Section 3.**

### 4D. What the gap means
- **TODO: Write after 4C is complete.**

## Conclusion
- Restate: the COI-WTP gap for wildfire smoke ER visits is ~$13 million for 2016-2019, and this is conservative
- Limitations: currency conversion assumptions, unvalued endpoints, unit-of-analysis mismatch (Richardson per symptom-day vs. capstone per ER visit), weaker cardiovascular evidence
- Implication: as wildfire smoke worsens with climate change, the undervaluation grows
