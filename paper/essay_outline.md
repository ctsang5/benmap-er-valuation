## Outline: The Economic Impact of Wildfire Smoke ED Visits in California

### I. Introduction
**Theme:** The question and why it matters

- Wildfire smoke is a growing health threat in California. Chen et al. (2023) estimated thousands of ED visits attributable to wildfire smoke, but the economic cost of those visits depends on how you measure it.
- State the question: what is the economic impact of wildfire smoke-attributable ED visits in California?
- Preview: this paper estimates the economic impact using two approaches and finds that the COI approach underestimates the total cost by roughly a factor of three.

**Sources:** Chen et al.

**Why this goes first:** The reader needs to know what question we're answering before anything else.

**Revision note (feedback #10):** The introduction now previews the magnitude of the finding ("by roughly a factor of three"), giving the reader a concrete reason to keep reading rather than just "substantially underestimates."

---

### II. The Health Burden
**Theme:** Wildfire smoke causes a measurable number of ED visits in California

- Chen et al.'s two-stage method: basin-level regressions -> random-effects meta-analysis -> health impact function
- Results: 4,597 respiratory ED visits and 889 cardiovascular ED visits attributable to wildfire smoke in California, 2016-2019

**Sources:** Chen et al. (2023)

**Why this goes second:** Before we can talk about dollars, we need the ED visit counts. Everything that follows is about putting a price on these 5,486 visits.

**Revision note (feedback #8):** Removed the note that cardiovascular is "a newer finding." It's a health science point, not an economics one. If worth mentioning at all, relegate to a footnote.

---

### III. The Default Valuation
**Theme:** EPA's default approach values an ED visit using only medical costs---but this approach has genuine strengths

#### III.A. How BenMAP calculates the COI

- BenMAP uses HCUP data (NEDS for billed charges, NIS for cost-to-charge ratios) to calculate a single unit value per ED visit
- The values: $875 per respiratory ED visit, $1,161 per cardiovascular ED visit (2015 USD)
- What these numbers include: medical costs only (hospital bills adjusted by CCR)
- What these numbers exclude: lost wages, pain and suffering, averting expenditures, costs borne by family members

#### III.B. What COI gets right

- COI is based on observed HCUP expenditure data---real hospital bills from real patients, not hypothetical survey responses
- It is transparent and replicable: another researcher can pull the same NEDS/NIS data and arrive at the same numbers
- It avoids the well-known biases of stated-preference methods (hypothetical bias, scope insensitivity, framing effects)
- These are real advantages. The question is not whether COI is bad, but whether it is complete.

**Sources:** BenMAP Appendix H

**Why this goes third:** The reader needs to see the baseline valuation before they can understand why the literature suggests it might be insufficient. This section sets up the comparison. Acknowledging COI's strengths makes the later argument for WTP more credible, because it shows the paper understands the tradeoff rather than just advocating for bigger numbers.

**Revision note (feedback #6):** Added III.B to acknowledge COI's genuine advantages. The original outline framed COI as purely insufficient; now the reader sees that COI is rigorous but incomplete.

---

### IV. The Alternative Valuation
**Theme:** A comprehensive valuation that includes pain, suffering, and lost productivity gives substantially larger values

#### IV.A. Stieb et al.'s framework and results

- Stieb et al.'s framework: V\_T = V\_COT + V\_LP + V\_SP (cost of treatment + lost productivity + pain/suffering and averting expenditures)
- How each component was estimated: WTP survey (Johnson et al. 2000) for V\_SP, Saint John ED data for V\_COT and V\_LP, Table 2 composition weights to assemble endpoint-level values
- Results: CAN$2,000 per respiratory ED visit, CAN$4,400 per cardiovascular ED visit (1997 CAN$) -> $2,752 and $6,054 in 2015 USD after currency conversion and CPI-Medical inflation
- Why the gap: for respiratory ED visits, pain/suffering ($950) actually exceeds cost of treatment ($930)---COI misses more than half the total value

#### IV.B. Two different gaps, two different reasons

- **The internal gap (1.9x for respiratory, 1.3x for cardiovascular):** Within Stieb's own data, V\_T exceeds (V\_COT + V\_LP) by these ratios. This is the gap between a comprehensive valuation and a standard COI (which includes medical costs + lost productivity). It measures how much pain, suffering, and averting expenditures add on top of the costs that COI typically captures.
- **The cross-study gap (3.1x for respiratory, 5.2x for cardiovascular):** Stieb's V\_T ($2,752 respiratory, $6,054 cardiovascular) divided by BenMAP's unit values ($875 respiratory, $1,161 cardiovascular). This gap is larger than 1.9x because BenMAP's COI is *even more incomplete* than a standard COI---it includes only medical costs and drops lost wages entirely.
- Decomposition: how much of the 3.1x respiratory gap comes from adding lost productivity (moving from BenMAP's medical-only COI to a standard COI), and how much comes from adding pain/suffering (moving from standard COI to Stieb's comprehensive V\_T)?
  - BenMAP respiratory COI: $875 (medical costs only)
  - Stieb's V\_COT + V\_LP for respiratory: ~$1,630 (medical costs + lost productivity)---ratio to BenMAP: ~1.9x
  - Stieb's full V\_T for respiratory: $2,752 (adding pain/suffering)---ratio to BenMAP: 3.1x
  - So roughly half the 3.1x gap comes from lost productivity that BenMAP drops, and the other half comes from pain/suffering that no COI measure captures.

#### IV.C. A composition mismatch to flag

- Stieb assumes 44% asthma in the respiratory ED population (from Saint John, New Brunswick ED data in the 1990s); Chen's California wildfire data shows ~26% asthma in the wildfire-attributable respiratory population.
- This means Stieb's respiratory unit value is calibrated to a different patient mix than the one being valued.
- The implications of this mismatch are discussed in Section VII---but the reader should know the caveat now, before the Stieb values are taken at face value for the next two sections.

**Sources:** Stieb et al. (2002), Johnson et al. (2000) as underlying methodology, BenMAP Appendix H for comparison

**Why this goes fourth:** Now the reader can see both approaches side by side. They know what BenMAP counts (Section III) and what it leaves out (this section fills the gap). The decomposition in IV.B prevents the reader from confusing the two different ratios that will appear in the paper.

**Revision notes:**
- **(Feedback #1):** Added IV.B to explicitly decompose the 1.9x internal gap vs. the 3.1x cross-study gap, explaining that BenMAP's denominator is smaller because it drops lost wages.
- **(Feedback #3):** Added IV.C to flag the composition mismatch early, rather than waiting until the Discussion.

---

### V. Why the Gap Is Especially Large for ED Visits
**Theme:** The COI-WTP gap is expected to be especially large for ED visits because they are short, severe events

- Van Houtven et al.'s meta-regression of 236 WTP estimates: severity elasticity (~2.0) is 4x larger than duration elasticity (~0.5)
- The constant WTP/QALY assumption (that severity and duration contribute equally) is rejected (p < 0.001)
- **The connecting logic:** COI captures costs of treatment, which scale primarily with duration---longer hospital stays mean higher medical bills. WTP, by contrast, is dominated by severity perception, because people are disproportionately willing to pay to avoid more severe illness (severity elasticity ~2.0). For short, severe events like ED visits, the COI denominator is small (short duration keeps treatment costs low) while the WTP numerator is large (high severity drives willingness to pay far above treatment costs). The asymmetric elasticities quantify this intuition.
- This means the COI-vs-WTP gap should be especially large for ED visits, which is consistent with Stieb's 1.9x respiratory EDV ratio (where pain/suffering actually exceeds treatment costs)

**Sources:** Van Houtven et al. (2006)

**Why this goes fifth:** This section explains *why* the gap from Section IV exists, not just *that* it exists. It moves the argument from "here are two different numbers" to "there's a theoretical reason to expect the comprehensive number to be substantially larger for this specific type of health event."

**Structural note (feedback #7):** This material could alternatively be folded into Section IV as "IV.C: Why the gap is expected to be large for ED visits," which would tighten the path from valuations to calculation. Keeping it as a standalone section is justified if the Van Houtven discussion is substantial enough to warrant its own space---but watch for whether it interrupts the reader's momentum before the Section VI payoff.

**Revision note (feedback #4):** Added the explicit connecting logic: COI scales with duration, WTP scales with severity, so for short/severe events the gap is asymmetrically large. The original outline stated the conclusion but not the reasoning that links the elasticities to the COI-WTP gap.

---

### VI. The Calculation and Its Stakes
**Theme:** Applying both approaches to the same ED visit counts produces very different economic impact estimates---and the difference has real consequences

#### VI.A. The multiplication

- COI approach (BenMAP): (4,597 x $875) + (889 x $1,161) = ~$5.1M
- WTP approach (Stieb): (4,597 x $2,752) + (889 x $6,054) = ~$18.0M
- The difference: ~$12.9M in economic impact that the COI approach misses (overall ratio ~3.5x)

#### VI.B. Why the difference matters

- Who uses BenMAP? EPA, CARB, and state regulators use it to produce the benefit estimates in benefit-cost analyses for air quality regulations.
- What decisions does BenMAP inform? Whether a proposed regulation's health benefits justify its compliance costs. If BenMAP understates the cost of wildfire smoke ED visits by ~3.5x, the health benefits side of the ledger is systematically too low.
- The consequence: regulations that would reduce wildfire smoke exposure look less justified than they actually are. Investments in smoke mitigation (prescribed burns, air filtration programs, public warning systems) appear to have lower returns than they actually do.
- This is not just an academic exercise---it is a measurement choice that shapes whether protective policies pass benefit-cost tests.

**Sources:** Chen et al. (counts), BenMAP (COI values), Stieb et al. (WTP values)

**Why this goes sixth:** This is the payoff. Every previous section was building toward this multiplication. The reader now has the counts (Section II), both sets of unit values (Sections III-IV), and the theoretical justification for why they differ (Section V).

**Revision note (feedback #2):** Added VI.B to connect the dollar gap to real-world decision-making. The original outline went straight from the calculation to limitations, leaving the reader without any sense of why the gap matters.

---

### VII. Discussion and Limitations
**Theme:** Both estimates involve assumptions; acknowledging them strengthens the comparison

#### VII.A. Composition mismatch (detailed)

- Stieb's respiratory values assume 44% asthma/COPD in the ED population; Chen's wildfire-attributable respiratory EDVs are ~26% asthma. This means Stieb's unit value may be miscalibrated for the wildfire population.
- Direction of bias: asthma ED visits tend to involve higher treatment costs and longer restricted-activity days than respiratory infections. If the wildfire population has proportionally less asthma, Stieb's composite may overstate the per-visit value slightly. However, the WTP component (pain/suffering) may not follow the same pattern---wildfire smoke ED visits involve a distinctive etiology (smoke inhalation, evacuation stress) that could shift WTP in either direction.

#### VII.B. Benefit transfer as a shared assumption

- Both estimates involve benefit transfer, not just the WTP approach. The COI values transfer national HCUP data to California. The WTP values transfer Canadian 1990s ED data to California 2016-2019. Neither set of values was estimated on the California wildfire population.
- This is a shared methodological limitation, not something unique to Stieb's approach. The relevant question is not "does benefit transfer introduce error?" (it does, for both) but "which transfer is more likely to be directionally misleading?"

#### VII.C. Currency and inflation conversion

- The CAD-to-USD conversion uses the 1997 annual average exchange rate (1 CAD = 0.7226 USD), not purchasing power parity (PPP). Using PPP would give a slightly different result. The choice of exchange rate method introduces a known approximation.
- The CPI-Medical deflator (1997 -> 2015, ratio = 446.752 / 234.583 = 1.90) compounds over an 18-year window. Medical inflation has been uneven across this period; the single ratio smooths over year-to-year variation. Applying a different deflator (e.g., CPI-All Items, or a hospital-specific index) would change the converted values.
- Direction: because medical costs have inflated faster than general prices, using CPI-Medical rather than CPI-All Items produces a larger 2015 USD figure. This means the Stieb values are at the upper end of reasonable conversions.

#### VII.D. The wildfire-specific WTP gap

- No source provides WTP specifically for wildfire smoke ED visits.
- Richardson, Champ & Loomis (2013) provides wildfire-specific WTP evidence---WTP/COI ratios of 5-31x for wildfire smoke symptom days, far larger than Stieb's general-morbidity ratios. However, Richardson's values are per symptom day, not per ED visit, so they cannot plug directly into the calculation.
- Richardson's finding that 89% of respondents took defensive actions but only 5% sought medical care explains why the wildfire-specific gap is so large: COI captures almost nothing when most of the welfare cost is defensive spending and disutility, not medical treatment.
- The implication: the 3.5x gap estimated here, based on Stieb's general-morbidity WTP values, may actually be a conservative lower bound for wildfire smoke specifically.

#### VII.E. The COI estimate as a lower bound

- The COI estimate is a lower bound by construction: it captures only medical costs, which are a subset of the total welfare loss.
- The WTP estimate is more comprehensive but depends on benefit transfer from a different context (Canadian, 1990s, non-wildfire). Its advantage is completeness; its limitation is external validity.
- Neither estimate captures the full picture. But the direction of the gap---WTP substantially exceeding COI---is robust across multiple literatures, multiple methods, and the theoretical prediction from Van Houtven's elasticity asymmetry.

**Sources:** All sources as relevant

**Revision notes:**
- **(Feedback #5):** Added VII.D on Richardson et al., explaining why it can't be used directly (per-symptom-day, not per-visit) but noting that its large ratios suggest the 3.5x estimate is conservative.
- **(Feedback #9):** Expanded VII.C from "currency conversion introduces approximation" to specific discussion of exchange rate method, deflator choice, 18-year compounding window, and directional bias.
- **(Feedback #11):** Reframed benefit transfer in VII.B as a shared assumption underlying both estimates, not a limitation unique to WTP.

---

### VIII. Conclusion

- Restate the core finding: using BenMAP's COI-only approach, the economic impact of wildfire smoke ED visits in California (2016-2019) is ~$5.1M. Using Stieb et al.'s comprehensive valuation, it is ~$18.0M---roughly 3.5x larger.
- The gap is not an artifact of one paper's assumptions. It is consistent with the theoretical prediction from Van Houtven's elasticity asymmetry, with Stieb's internal WTP/COI ratios, and with the broader WTP literature.
- The practical implication: benefit-cost analyses that rely on COI-only valuations systematically understate the health benefits of reducing wildfire smoke exposure, potentially tipping regulatory decisions against protective policies that would pass a more complete benefit-cost test.

---

## Summary of Revisions from Feedback

| # | Issue | Fix | Location |
|---|-------|-----|----------|
| 1 | Two WTP/COI ratios (1.9x vs 3.1x) unexplained | Decomposed into internal vs. cross-study gap with arithmetic | IV.B |
| 2 | No "so what" after calculation | Added policy implications (who uses BenMAP, what decisions it shapes) | VI.B |
| 3 | Composition mismatch buried too late | Flagged in IV.C, detailed in VII.A | IV.C, VII.A |
| 4 | Van Houtven logic chain missing a step | Added explicit COI-scales-with-duration / WTP-scales-with-severity link | V |
| 5 | Richardson et al. unaddressed | Explained why it can't be used directly + conservative lower bound argument | VII.D |
| 6 | COI strengths unacknowledged | Added III.B on observed data, replicability, no hypothetical bias | III.B |
| 7 | Van Houtven standalone vs. subsection | Kept standalone with structural note about the alternative | V (note) |
| 8 | "Newer finding" in Section II | Cut; footnote if needed | II |
| 9 | Currency conversion vague | Specific: exchange rate method, deflator choice, 18-year window, direction | VII.C |
| 10 | Introduction lacks magnitude | Added "by roughly a factor of three" | I |
| 11 | Benefit transfer not framed as shared | Reframed as shared assumption for both COI and WTP | VII.B |
