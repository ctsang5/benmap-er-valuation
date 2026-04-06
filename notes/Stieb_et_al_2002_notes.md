# Stieb et al. (2002) — Reading Notes
*Environmental Health: A Global Access Science Source 1:7 (2002)*
**WTP PAPER: provides economic unit values for ED visits combining COT + lost productivity + pain/suffering (WTP component)**

## 1. Research Question
What is the total economic value of a cardiorespiratory disease episode for patients presenting to the emergency department, combining traditional cost-of-treatment (COT) and lost productivity (LP) components with willingness-to-pay (WTP) estimates for pain and suffering? Compares total value (COT + LP + WTP) to the COT+LP portion alone (i.e., the ratio of comprehensive value to COI).

## 2. Audience
Health economists, environmental health researchers, Canadian regulatory agencies (Health Canada involvement). Canadian setting — values are in 1997 Canadian dollars. Published in a new open-access journal at the time; part of a broader program of research on air pollution and ED use in Ottawa-Hull.

## 3. Method

### Study Setting
Emergency Department patients in **Ottawa-Hull, Canada** presenting with cardiorespiratory disease (acute), drawn from a larger parent study. Study period: **1996–1997**.

### Economic Components
Total value per episode = Cost of Treatment (COT) + Lost Productivity (LP) + WTP for pain/suffering/averting (from literature transfer)

**COT** — micro-costing of actual ED episode:
- Physician costs (ED visit, follow-up, specialist)
- Drug costs (prescription + OTC, provincial formulary)
- Hospital overhead allocation
- Lab and diagnostic costs
- Patient time costs (opportunity cost at wage rate)
- Estimated separately for respiratory vs. cardiac presentations

**Lost Productivity (LP)**:
- Restricted activity days (RAD) and bed days
- Valued at average weekly earnings from Statistics Canada
- Work loss and home productivity loss both included

**WTP component** — transferred from:
- Johnson et al. (1998, 2000) stated preference study on respiratory and cardiovascular health states
- Uses health state classifications to attach WTP per day of illness
- Derived from U.S. population, PPP-adjusted to Canadian dollars
- Captures pain, suffering, and disutility of illness — the component excluded from COI

### Uncertainty
Monte Carlo analysis using Analytica software; 95% CIs from 5,000 simulations across uncertain parameters. Key uncertain parameters: WTP unit values, physician fee schedules, RAD duration.

## 4. Data
- **Patient sample**: Ottawa-Hull ED patients with cardiorespiratory disease, 1996–1997
- **Resource use**: actual billing records and patient self-report (Stieb et al. 2000 linked dataset)
- **WTP values**: Johnson et al. (1998, 2000) — transferred, not locally estimated
- **Wages**: Statistics Canada CANSIM Matrix 4468 (average weekly earnings, all employees)
- **Drug costs**: provincial formulary + OTC self-report
- **Currency**: 1997 Canadian dollars throughout

## 5. Key Results (Table 5 — Total Value per Episode, 1997 CAD)

| Endpoint | Total Value | 95% CI | Total/COI Ratio |
|---|---|---|---|
| Respiratory Hospital Admission | $4,200 | ($3,400–$5,000) | 1.3 |
| Cardiac Hospital Admission | $5,200 | ($4,000–$6,400) | 1.3 |
| **Respiratory ED Visit** | **$2,000** | **($1,700–$2,500)** | **1.9** |
| Cardiac ED Visit | $4,400 | ($3,300–$5,600) | 1.3 |
| Restricted Activity Day | $48 | ($13–$82) | 1.9 |
| Asthma Symptom Day | $28 | ($11–$71) | 2.3 |
| Acute Respiratory Symptom Day | $13 | ($0–$28) | 1.1 |

**Total/COI ratio** = (COT + LP + WTP) / (COT + LP). Values >1 indicate the WTP component adds meaningfully. The ratio of 1.9 for respiratory ED visits means WTP-based pain/suffering adds ~90% to the COI value for this endpoint.

**Respiratory ED Visit decomposition (approximate):**
- COT + LP ≈ $1,050 (the "COI" portion)
- WTP component (pain/suffering) ≈ $950
- Total: **$2,000 CAD 1997**

## 6. Currency and Inflation Adjustments

To apply Stieb values in a U.S. context (for comparison to BenMAP's $36,000):

**1997 CAD → USD:**
- OECD PPP for 1997: approximately 0.83 CAD/USD (i.e., $1 USD ≈ $1.20 CAD)
- $2,000 CAD 1997 ÷ 1.20 ≈ **$1,667 USD 1997**

**1997 USD → 2022 USD (CPI adjustment):**
- CPI 1997 ≈ 160.5; CPI 2022 ≈ 296.8
- Multiplier ≈ 1.85
- **$1,667 × 1.85 ≈ $3,085 USD 2022**

**Comparison to BenMAP:**
- BenMAP's $36,000 COI is per **hospital admission** (Fann et al. 2017, from NAAQS RIA)
- Stieb's $2,000 CAD is per **ED visit** — a less resource-intensive endpoint
- Direct comparison requires acknowledging the different health outcome (ED visit vs. inpatient admission)
- BenMAP uses hospital admission as the morbidity endpoint; the capstone is asking about ED visits specifically — Stieb is closer to the right comparator

## 7. Contributions
- One of very few studies providing total economic value (COI + WTP) specifically for **ED visits** as distinct from hospital admissions
- Shows WTP component for pain/suffering is substantial for ED visits (nearly doubles the COI estimate; ratio 1.9)
- Provides uncertainty estimates (Monte Carlo CIs) — useful for sensitivity analysis
- Establishes that the COT+LP component alone (the COI) substantially understates total economic burden, consistent with Harrington & Portney (1987)

## 8. Limitations
- Canadian setting — population preferences may differ from U.S.; requires PPP adjustment
- WTP component is **transferred** from Johnson et al., not locally estimated — introduces benefit transfer uncertainty
- 1997 values — require inflation adjustment for current-dollar comparisons
- Study population is ED patients (ill at time of interview) — may not reflect general population preferences
- Does not separately report what fraction of $2,000 is WTP vs. COI; requires back-calculation

## 9. Replication
- Patient data from parent study (Anis et al. 2000; Stieb et al. 2000) — not publicly available
- WTP values from Johnson et al. (1998, 2000) — available from Triangle Economic Research
- Methods well-documented; Analytica software used for Monte Carlo

## Project Relevance
- **Provides a WTP-inclusive unit value for respiratory ED visits**: $2,000 CAD 1997 ≈ $3,085 USD 2022 (inflation + PPP adjusted)
- This is substantially lower than BenMAP's $36,000/admission, but reflects a different endpoint (ED visit vs. hospital admission); direct comparison should acknowledge this difference
- The Total/COI ratio of **1.9** for respiratory ED visits is directly usable in the capstone: if BenMAP's COI for ED visits were known, multiplying by 1.9 would give a WTP-inclusive estimate
- The pain/suffering component being ~50% of total value for ED visits (vs. ~23% for hospital admissions, ratio 1.3) suggests that patient disutility is proportionally larger for ED visits — possibly because ED presentations involve acute distress
- Supports the capstone argument that BenMAP's COI-based values are lower bounds, particularly for ED visits where the WTP ratio exceeds that for hospital admissions
- **Key comparison**: Stieb vs. Richardson — Stieb gives WTP per ED visit episode ($2,000 CAD); Richardson gives WTP per symptom day ($87–$95). At ~7 symptom days per episode (Richardson's sample mean), Richardson implies ~$600–$665 per episode, lower than Stieb's $2,000 but in the same order of magnitude after currency/method differences.
