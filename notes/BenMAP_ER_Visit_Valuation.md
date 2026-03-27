# How BenMAP Puts a Dollar Value on Emergency Room Visits

**Source:** BenMAP-CE User's Manual Appendices, Appendix H (August 2025), plus external research

---

## What Is BenMAP?

BenMAP-CE (Benefits Mapping and Analysis Program) is a tool built by the EPA. Its job is to answer one question: **if we clean up the air, how much money does that save in avoided health problems?**

When the EPA proposes a new air quality regulation (say, tightening the limit on fine particulate matter), they need to show that the health benefits justify the cost of compliance. BenMAP is how they calculate those benefits.

This document focuses on one piece of that calculation: **how BenMAP assigns a dollar value to an avoided emergency room visit** for three types of health events — cardiovascular disease, asthma, and respiratory disease.

---

## The Big Picture: Three Steps from Air Quality to Dollar Benefits

BenMAP connects cleaner air to dollar savings through a three-step pipeline:

### Step 1 — Measure the Air Quality Improvement

BenMAP takes two air quality scenarios — one "before" (baseline) and one "after" (post-regulation) — and computes the difference in pollutant concentrations at every point on a map grid. This difference is the improvement in air quality.

### Step 2 — Estimate How Many Fewer People Get Sick

The air quality improvement feeds into equations from published medical studies. These equations say things like: "for every 10 µg/m³ decrease in PM2.5, ER visits for respiratory disease drop by X%." BenMAP uses these equations to estimate the **number of ER visits avoided** across the population.

### Step 3 — Multiply by a Dollar Value

Each avoided ER visit gets multiplied by a unit value — a single dollar figure representing the cost of one ER visit for that health condition. This is the step we care about. The rest of this document explains where those unit values come from.

---

## How They Measure the Cost: The Cost-of-Illness Approach

There are two ways to put a dollar value on a health event:

**Cost-of-Illness (COI)** adds up the tangible costs: medical bills, and sometimes lost wages if you miss work. This is what BenMAP uses for ER visits.

**Willingness-to-Pay (WTP)** asks: how much would someone pay to avoid the entire experience — not just the bills, but the pain, anxiety, disrupted life, and everything else? WTP is always higher than COI, sometimes by 2x to 10x, because it captures suffering that doesn't show up on a bill.

### Why BenMAP Uses the Cheaper Number

EPA's Science Advisory Board specifically recommended using COI rather than trying to estimate WTP. Their reasoning:

1. **No reliable way to adjust.** The gap between COI and WTP varies wildly depending on the condition. A blanket multiplier would be a guess.
2. **Avoids inflating the numbers.** If EPA overstates benefits, regulations look better than they are. That's a problem when billions of dollars are at stake.
3. **It's a safe lower bound.** If a regulation passes a cost-benefit test using the conservative COI numbers, it would definitely pass using the higher WTP numbers too.

### What COI Leaves Out

Most economists agree that WTP is the theoretically correct measure of cost — it captures everything a health event actually does to someone's life. COI only counts the medical bill and (sometimes) lost wages. It has no way to account for things like:

- The pain and anxiety of the ER visit itself
- Missing a few hours of work that day (for a short ER visit, lost wages are treated as negligible)
- Missing something irreplaceable — a family event, a graduation, a trip
- Costs of avoidance behavior (buying an air purifier, staying indoors on bad air days)
- The general disruption to your life and the people around you

These are real costs to real people, and they can easily exceed the medical bill. The problem isn't that EPA thinks they don't matter — it's that **nobody has been able to reliably measure them for ER visits**. The few WTP studies that exist for specific ER endpoints produce inconsistent results, with estimates ranging from 1.5x to 10x the COI value. With no empirical basis for picking a multiplier, EPA chose to report a number they know is too low rather than a number that might be too high or too low by an unknown amount.

This means every dollar-valued benefit in BenMAP's ER visit calculations is a **deliberate undercount** of the true social cost. It's a conservative choice made for regulatory credibility, not a statement about what the actual cost is.

For standard ER visits, COI includes **only medical costs** — no lost wages — because the visit is short enough that missed work isn't a significant factor. The exception is when a patient enters through the ER and gets admitted to the hospital (more on this later), where the stay is long enough that lost wages matter.

All dollar values in BenMAP are expressed in **2015 dollars** so that different endpoints can be compared apples-to-apples.

---

## Where the Data Comes From

BenMAP needs to know: what does a typical ER visit actually cost? To answer that, it relies on two massive hospital databases, both from a federal project called HCUP (Healthcare Cost and Utilization Project), run by AHRQ (Agency for Healthcare Research and Quality).

### Database 1: NEDS (Nationwide Emergency Department Sample)

This is the largest ER database in the country.

- **~30 million ER visit records** from ~950 hospitals across ~37 states (2016 data)
- Captures every visit at each sampled hospital — not a subsample
- Records diagnoses (what was wrong), procedures (what they did), total charges (what the hospital billed), patient demographics, and whether the patient was sent home or admitted
- **Key limitation:** NEDS records what the hospital *billed*, not what care actually *cost*. Hospital bills are inflated way above the real cost of delivering care — often 2-3x higher

### Database 2: NIS (Nationwide Inpatient Sample)

This covers patients who were admitted to the hospital (stayed overnight or longer), not ER-only visits.

- **~8 million inpatient discharge records** per year from ~4,400 hospitals
- Critically, NIS includes something NEDS doesn't: **cost-to-charge ratios** — the conversion factor needed to turn inflated bills into actual costs

### Why These Two Databases?

EPA considered alternatives and found them insufficient:

| Alternative | Problem |
|---|---|
| Medicare Claims | Only covers ages 65+ — can't be used for all-age conditions like asthma |
| MEPS (household survey) | Too small (~15,000 households) to get reliable diagnosis-specific cost estimates |
| Commercial insurance databases | Only covers people with employer insurance — misses uninsured, Medicaid, Medicare |
| CDC's NHAMCS | Much smaller than NEDS with limited cost data |

HCUP's combination of huge sample size, all-payer coverage, and clinical detail makes it the best available option.

---

## Cleaning Up the Data

Before computing average costs, BenMAP has to deal with three data problems.

### Problem 1: Hospital Bills Aren't Real Costs

Hospitals bill far more than care actually costs. A hospital might bill $10,000 for a visit that cost $3,500 to deliver. To get real costs, BenMAP applies **cost-to-charge ratios (CCRs)**.

A CCR is simply: **actual cost ÷ billed charge**. A typical CCR is around 0.30 to 0.45, meaning real costs are 30-45% of what's on the bill. These ratios come from cost reports that hospitals file annually with Medicare.

Since NEDS (the ER database) doesn't include its own CCRs, BenMAP borrows them from NIS (the inpatient database) by matching hospitals across the two datasets. This is an imperfect workaround — ER-specific ratios might differ from inpatient ratios — but it's the best available method.

**The conversion:** Estimated Real Cost = Billed Charge × CCR

### Problem 2: Diagnosis Codes Changed

The medical studies that link air pollution to ER visits use an older diagnosis coding system called ICD-9 (~13,000 codes). But the 2016 hospital data uses the newer ICD-10 system (~68,000 codes), which the U.S. switched to in October 2015.

BenMAP bridges this gap using an official crosswalk (translation table) published by CMS. Since ICD-10 is much more detailed, one old ICD-9 code often maps to several ICD-10 codes. BenMAP only looks at the **principal diagnosis** — the first-listed reason for the visit — to keep things clean.

### Problem 3: The Data Is a Sample, Not a Census

NEDS doesn't contain every ER visit in America — it's a carefully designed sample of hospitals. To get nationally representative averages, BenMAP uses statistical techniques that account for three features of the sampling design:

1. **Stratification:** Hospitals are grouped by region, urban/rural, teaching status, etc. before sampling, which reduces variability.
2. **Clustering:** Entire hospitals are sampled (not individual visits), so visits within the same hospital are correlated.
3. **Discharge weights:** Each visit record carries a weight indicating how many national visits it represents. The weight depends on how many hospitals like that one are in the country versus how many made it into the sample. If there are 500 rural hospitals in America but only a handful are in NEDS, each sampled rural visit gets a high weight because it has to stand in for many similar visits that aren't in the database. If most large urban hospitals are already in the sample, their visits get lower weights because they only stand in for a few.

Standard averaging would give wrong answers — it would overcount hospital types that are overrepresented in the sample and undercount those that are underrepresented. Instead, BenMAP uses survey estimation software that accounts for all three features to produce weighted national averages with proper confidence intervals.

---

## The Unit Values: Three Health Endpoints

Now for the actual dollar figures. BenMAP assigns a per-visit cost for three types of ER visits related to air pollution.

---

### 1. Cardiovascular Disease ER Visits — $1,161

| Detail | Value |
|---|---|
| What it covers | All cardiac outcomes (heart attacks, heart failure, arrhythmias, stroke, hypertension, etc.) |
| Diagnosis codes | ICD-9 390-459 → ICD-10 I00-I99 |
| Age range | 0-99 (all ages) |
| Dollar value | **$1,161** per visit (2015$) |
| Data source | 2016 HCUP NEDS |
| What's included | Medical costs only |

**How the $1,161 was calculated:**

Think of the 2016 NEDS database as a giant spreadsheet with ~30 million rows — one row per ER visit at the sampled hospitals. Each row records the patient's diagnosis, what the hospital billed, and a weight representing how many national visits that one record stands for.

Here's what BenMAP does with it:

1. **Filter to heart-related visits.** The medical studies define "cardiovascular" using ICD-9 codes 390-459, but the 2016 data uses the newer ICD-10 system. So BenMAP first translates 390-459 into the equivalent ICD-10 codes (mostly I00-I99) using a published crosswalk table, then keeps only visits where the primary reason for the visit matches one of those codes. This narrows 30 million rows down to just the cardiovascular ER visits.

2. **Convert billed charges to real costs.** Each remaining row has a "total charges" field — what the hospital billed. But hospital bills are inflated well above the actual cost of care. To get real costs, BenMAP multiplies each visit's charge by that hospital's cost-to-charge ratio (borrowed from the NIS database). For example, if a hospital billed $3,200 for a visit and its CCR is 0.38, the estimated real cost is $3,200 × 0.38 = **$1,216**.

3. **Compute the weighted national average.** BenMAP can't just add up all the costs and divide — the database is a sample, not a census. Each visit has a discharge weight that reflects how many similar visits exist nationally but aren't in the sample. A visit at a rural hospital that's one of only a few rural hospitals sampled might get a weight of 8 ("this visit stands in for 8 nationally"), while a visit at a large urban hospital — a type well-represented in the sample — might get a weight of 3. The weighted average multiplies each visit's cost by its weight, so underrepresented hospital types aren't drowned out by overrepresented ones. On top of this, the survey estimation software adjusts the confidence interval to account for stratification (which tightens it) and clustering (which widens it, because visits at the same hospital tend to have similar costs and thus provide less independent information).

4. **Adjust to 2015 dollars.** Since the data is from 2016, BenMAP applies the medical care price index to express the result in 2015 dollars for consistency with other endpoints.

The result of all this: the average real cost of one cardiovascular ER visit in the United States is **$1,161** (2015$).

---

### 2. Asthma ER Visits — $534 or $447

Unlike cardiovascular and respiratory visits, asthma ER visits are **not** valued using the HCUP database approach. Instead, BenMAP offers two values from older published studies:

| | Smith et al. (1997) | Stanford et al. (1999) |
|---|---|---|
| **Unit value (2015$)** | **$534** | **$447** |
| **Original value** | ~$155 (1987$) | ~$235 (1997$) |
| **Data source** | 1987 national household survey | Multi-hospital cost accounting records, 1996-97 |
| **What "cost" means** | Total expenditures (what was billed/paid) | Actual cost to the hospital to deliver care |
| **Age range** | 0-99 | 0-99 |

**Smith et al.** looked at a 1987 national survey, found ~1.2 million asthma ER visits costing a total of ~$186.5 million, and divided to get ~$155 per visit. Adjusted for medical inflation to 2015 dollars: **$534**.

**Stanford et al.** had something unusual: access to a hospital system's internal cost accounting, so they could see what it *actually cost* the hospital to treat each asthma patient (not what they billed or were paid). This gave ~$235 per visit in 1997 dollars, inflated to **$447** in 2015 dollars.

**Why the two differ:** Smith's number is based on charges/payments (higher). Stanford's is based on actual resource consumption (lower but arguably more accurate). Having both lets analysts check whether the choice of value changes the final answer significantly.

**Why BenMAP uses old studies instead of HCUP data for asthma:**
- These values have been used in major EPA rulemakings for years; switching would complicate comparisons across regulations
- Both studies have been through extensive peer review
- Stanford's actual-cost approach is methodologically distinct from the charge-and-adjust method
- BenMAP updates its valuation functions gradually, not all at once

**Handling uncertainty:**
- Smith: uses a **triangular distribution** (minimum $395, most likely $534, maximum $738) — a wide range because the per-visit cost comes from dividing two uncertain totals
- Stanford: uses a **normal distribution** (mean $447, standard deviation $8.95) — a very tight range because the large hospital sample pins down the average precisely

---

### 3. Respiratory Disease ER Visits — $875 or $11,990

BenMAP has two respiratory endpoints because there are two very different clinical pathways:

#### 3a. Standard ER Visit (Treat-and-Release) — $875

This is for patients who come to the ER with a respiratory problem, get treated, and go home the same day.

| Detail | Value |
|---|---|
| What it covers | Bronchitis, emphysema, asthma, COPD, pneumonia, upper respiratory infections, allergic rhinitis, wheezing |
| Diagnosis codes | ICD-9: 491-493, 460-466, 477, 480-486, 496, 786.07, 786.09 |
| Age range | 0-99 |
| Dollar value | **$875** per visit (2015$) |
| Data source | 2016 HCUP NEDS |
| What's included | Medical costs only |

Calculated the same way as the cardiovascular value: filter NEDS by diagnosis, apply CCRs, compute the weighted average.

#### 3b. Emergency Hospital Admission (EHA) — $11,990

This is for patients who come through the ER but are sick enough to be **admitted to the hospital as inpatients**. It's a fundamentally more severe (and expensive) event.

| Detail | Value |
|---|---|
| What it covers | All respiratory diseases |
| Diagnosis codes | ICD-9 460-519 (broader than the standard endpoint) |
| Age range | **65-99 only** |
| Dollar value | **$11,990** per admission (2015$) |
| Mean hospital stay | 5.09 days |

**Why only ages 65+?** The medical studies that established the link between air pollution and emergency hospital admissions used Medicare data, which only covers people 65 and older. BenMAP matches its dollar values to the same age range as the studies.

**Why it costs so much more:** The $11,990 is built from three cost components, not just one:

**Component 1 — ER costs:** The initial emergency department visit. Calculated from NEDS the same way as the $875 figure, but filtered to patients who were subsequently admitted (not sent home).

**Component 2 — Inpatient hospital costs:** The multi-day hospital stay after admission. Calculated from NIS (the inpatient database). The average billed charge is $11,111, converted to real cost via CCRs.

**Component 3 — Lost wages:** With an average 5-day hospital stay, lost work time is no longer negligible. BenMAP estimates this as:

> Lost Wages = (County Median Annual Income ÷ 260 workdays) × Days in Hospital

This is adjusted based on whether the patient is employed:
- **Employed patients:** Daily wage is increased by ~25-30% to account for fringe benefits (health insurance, retirement contributions, etc.)
- **Non-employed patients** (including retirees — the majority in this 65+ group): Valued at the after-tax wage rate, representing the value of their lost time (caregiving, household work, leisure)

The employed and non-employed values are blended using the county's employment rate. This means an avoided admission in a high-income county is valued higher than one in a low-income county.

**Why two databases are needed:** No single HCUP database captures the full cost of an ER-to-inpatient episode. NEDS has the ER portion but doesn't track what happens after admission. NIS has the inpatient portion but may not separately report the ER component. You need both.

**Important:** The $875 (treat-and-release) and $11,990 (admitted) endpoints should never be applied to the same population simultaneously — that would double-count admitted patients.

---

## How BenMAP Handles Uncertainty

Every number feeding into BenMAP's calculation is an estimate with a margin of error — the unit dollar values, the pollution-to-health equations, all of it. BenMAP doesn't ignore that uncertainty. Instead, it uses a technique called **Monte Carlo simulation** to show decision-makers the full range of plausible answers.

### The Problem: Stacking Uncertain Inputs

BenMAP's final answer — "this regulation will save $X in avoided ER visits" — depends on two key inputs:

1. **The health effect estimate:** How many fewer ER visits result from a given air quality improvement? This comes from a medical study, and that study's result has a margin of error.
2. **The unit dollar value:** How much does one ER visit cost? As we've seen, this also has a margin of error (the confidence interval from the NEDS data, or the range of estimates from the asthma studies).

If you just multiply the single best guess for each input, you get a single final answer — but that answer hides the fact that both inputs could reasonably be higher or lower. The true benefit could be quite different.

### The Solution: Run the Calculation Thousands of Times

Here's what Monte Carlo simulation does, step by step:

**Round 1:** Instead of using the best-guess values, BenMAP randomly picks a health effect estimate from within its margin of error (maybe a little higher than the best guess this time) and randomly picks a dollar value from within its margin of error (maybe a little lower). It multiplies them together and records the result.

**Round 2:** New random picks for both inputs. Maybe the health effect comes in low and the dollar value comes in high. Multiply, record.

**Round 3 through 5,000:** Same thing. Each time, both inputs are randomly drawn from their respective ranges, and the result is recorded.

After 5,000 rounds, BenMAP has 5,000 different answers. Most cluster in the middle, but some are higher and some are lower. This collection of answers *is* the result — it shows the full spread of plausible benefit estimates.

### A Concrete Example

Suppose BenMAP is estimating the benefit of avoided cardiovascular ER visits in one county:

- The medical study says the regulation will prevent somewhere between **80 and 120 visits** (best guess: 100)
- Each visit costs somewhere between **$926 and $1,396** (best guess: $1,161)

Using best guesses only: 100 × $1,161 = **$116,100**

But Monte Carlo might produce rounds like:

| Round | Health effect draw | Dollar value draw | Result |
|---|---|---|---|
| 1 | 108 visits | $1,050 | $113,400 |
| 2 | 87 visits | $1,280 | $111,360 |
| 3 | 115 visits | $980 | $112,700 |
| 4 | 94 visits | $1,190 | $111,860 |
| ... | ... | ... | ... |
| 5,000 | 103 visits | $1,145 | $117,935 |

After all 5,000 rounds, BenMAP can report: "The benefit is most likely around $116,000, but could plausibly be as low as $85,000 or as high as $155,000." That range is far more useful to a policymaker than a single number.

### Latin Hypercube Sampling: Smarter Random Draws

If you just pick random numbers, you might, by chance, cluster your draws in one part of the range and miss another part — like rolling a die 10 times and never getting a 6. With only 5,000 rounds, that could skew the results.

BenMAP avoids this with a technique called **Latin Hypercube Sampling**. Instead of picking purely at random, it divides each input's range into equal slices and makes sure it draws from every slice. Think of it like dealing cards from a deck instead of drawing from a shuffled pile — you're guaranteed to cover the full range evenly. This gives more reliable results without needing to run millions of rounds.

### What Shapes the Uncertainty for Each Endpoint

Each unit value has a different amount of uncertainty, depending on where the data came from:

| Endpoint | Shape of uncertainty | Why |
|---|---|---|
| Cardiovascular ($1,161) | Bell curve, moderate spread | Large NEDS sample gives a solid estimate, but not perfect |
| Asthma — Smith ($534) | Triangle, wide spread ($395–$738) | Derived from dividing two uncertain national totals — lots of room for the answer to shift |
| Asthma — Stanford ($447) | Bell curve, very narrow ($429–$465) | Huge hospital sample pinned the average down tightly |
| Respiratory ($875) | Bell curve, moderate spread | Same NEDS approach as cardiovascular |
| Respiratory EHA ($11,990) | Bell curve, moderate spread + geographic variation | Medical cost uncertainty plus county-to-county differences in wages |

The practical effect: when BenMAP runs Monte Carlo for asthma using the Smith value, the dollar value bounces around a lot from round to round (wide triangle). When it uses the Stanford value, the dollar value barely moves (tight bell curve). Most of the uncertainty in the final answer then comes from the health effect estimate rather than the dollar value.

---

## Inflation Adjustment

All values are standardized to 2015 dollars using the **Consumer Price Index for Medical Care** — a version of the CPI that tracks medical prices specifically.

Why not use the regular CPI? Medical prices rise much faster than prices in general. From 1987 to 2015, general prices roughly doubled, but medical prices roughly **tripled**. Using the regular CPI would significantly understate what old medical costs are worth in today's dollars.

For non-medical components (like lost wages in the EHA calculation), BenMAP uses general wage indices instead.

---

## Quick Reference: All Unit Values

| Endpoint | Value (2015$) | Ages | Includes | Source |
|---|---|---|---|---|
| Cardiovascular ER visit | $1,161 | 0-99 | Medical costs only | 2016 HCUP NEDS |
| Asthma ER visit (Smith) | $534 | 0-99 | Medical costs only | 1987 national survey, inflated |
| Asthma ER visit (Stanford) | $447 | 0-99 | Medical costs only | 1996-97 hospital cost data, inflated |
| Respiratory ER visit | $875 | 0-99 | Medical costs only | 2016 HCUP NEDS |
| Respiratory emergency hospital admission | $11,990 | 65-99 | Medical + inpatient + lost wages | 2016 HCUP NEDS + NIS + ACS |

---

## Key References

**EPA & BenMAP**
- BenMAP-CE User's Manual and Appendices (August 2025): https://www.epa.gov/benmap
- EPA Science Advisory Board Advisories: EPA-SAB-COUNCIL-ADV-04-002 (2004), EPA-SAB-09-012 (2009)

**Hospital Data (HCUP)**
- NEDS Overview: https://hcup-us.ahrq.gov/nedsoverview.jsp
- NIS Overview: https://hcup-us.ahrq.gov/nisoverview.jsp
- Cost-to-Charge Ratio Files: https://hcup-us.ahrq.gov/db/ccr/costtocharge.htm

**Asthma Studies**
- Smith DH et al. "A national estimate of the economic costs of asthma." *Am J Respir Crit Care Med.* 1997;156(3):787-793.
- Stanford R et al. "The cost of asthma in the emergency department and hospital." *Am J Respir Crit Care Med.* 1999;160(3):211-216.

**Other**
- CPI for Medical Care (BLS Series CUUR0000SAM): https://data.bls.gov/timeseries/CUUR0000SAM
- American Community Survey: https://data.census.gov/
- CMS ICD-10 General Equivalence Mappings: https://www.cms.gov/medicare/coding-billing/icd-10-codes/general-equivalence-mappings-gems
