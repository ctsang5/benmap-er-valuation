# What Would People Actually Pay to Avoid an ER Visit?

**A review of Willingness-to-Pay studies for emergency room visits and acute health events related to air pollution**

**Key sources:** Alberini & Krupnick (2000); Stieb et al. (2002); Johnson, Banzhaf & Desvousges (2000); Van Houtven et al. (2006); U.S. EPA (2010)

---

## Why This Document Exists

The companion document ([BenMAP_ER_Visit_Valuation.md](BenMAP_ER_Visit_Valuation.md)) explains how the EPA puts a dollar value on emergency room visits using **Cost-of-Illness (COI)** — essentially adding up the medical bill. That approach deliberately ignores pain, anxiety, missed life events, and every other cost that doesn't show up on a hospital invoice. As that document notes, the result is a **deliberate undercount** of what an ER visit actually costs someone.

This raises an obvious question: **how much of an undercount?** A family of economics studies has tried to answer that using a different approach called **Willingness-to-Pay (WTP)**, which attempts to capture the full cost — bill plus suffering. This document reviews what those studies found and compares their numbers to BenMAP's COI values.

---

## How Do You Measure What Someone Would Pay?

COI is straightforward: look at the hospital bill. WTP is harder, because you're trying to measure something that doesn't have a receipt — the value someone places on *not being sick*.

### The Survey Approach: Contingent Valuation

The most common method is called **contingent valuation (CV)**. A researcher gives you a scenario and asks a question like:

> *"Suppose there were a treatment that guaranteed you would not have this respiratory episode. What is the most you would pay for it?"*

The answer is your **stated WTP** — what you say you'd pay in a hypothetical scenario. Researchers collect these answers from hundreds or thousands of people and compute averages.

The word "contingent" means the value is *contingent on* (depends on) a hypothetical scenario that the researcher describes. The scenario isn't real — it's a carefully designed thought experiment.

### Why This Is Harder Than It Sounds

Stated-preference surveys face several well-known problems:

- **Hypothetical bias:** People tend to overstate what they'd pay when it's not real money. If nobody is actually going to charge you, it's easy to say "$500" when you'd really only pay $200.
- **Anchoring:** If the survey mentions a specific dollar amount (even as an example), people's answers cluster around that number instead of reflecting their true value.
- **Protest zeros:** Some respondents answer "$0" not because they don't value the health improvement, but because they object to the idea of paying for something they think should be free (like clean air).

Researchers use various techniques to mitigate these problems — randomizing the dollar amounts shown, using multiple question formats, screening out protest responses — but they can never fully eliminate them.

### An Alternative: Health-Utility Indices

Instead of asking people directly about dollars, some studies describe health states using a standardized scoring system and ask people to rank or compare them. One common system is the **Quality of Well-Being (QWB) Index**, which rates health states on four dimensions: symptom type, episode duration, activity restrictions, and cost. The Johnson, Banzhaf & Desvousges (2000) study used this approach, as described below.

---

## Respiratory Illness: WTP Is 2–4 Times the Medical Bill

BenMAP values a standard respiratory ER visit at **$875** (2015$) and asthma ER visits at **$534 or $447** (2015$), using COI. How do WTP estimates compare?

### Alberini & Krupnick (2000) — The Key Comparison Study

The most direct comparison of WTP versus COI for acute respiratory illness comes from a study conducted in three cities in Taiwan.

**What they did:** Over 900 residents kept daily health diaries recording their symptoms. When someone got sick, a contingent valuation survey asked how much they would pay to avoid a recurrence of that specific episode. The researchers then compared three measures side by side: (1) the CV-based WTP bids, (2) the cost-of-illness (medical bills plus lost wages), and (3) money spent on averting behavior (like buying medicine to reduce symptoms) (Alberini & Krupnick, 2000).

**What they found:** WTP to avoid an episode of acute respiratory illness was approximately **2 to 4 times larger** than the cost-of-illness alone (Alberini & Krupnick, 2000). The gap represents everything COI misses — the pain, the disruption, the anxiety, the lost leisure time.

**What this implies for BenMAP's numbers:** If the 2–4× ratio holds for U.S. ER visits, then:

- BenMAP's **$875** respiratory ER visit might really cost people **$1,750 to $3,500** in total welfare terms ($875 × 2 = $1,750; $875 × 4 = $3,500)
- BenMAP's **$534** asthma ER visit (Smith value) might really cost **$1,068 to $2,136**

**Important caveats:** This study was conducted in Taiwan, not the United States. Income levels, healthcare systems, and cultural attitudes toward health spending all differ. The WTP/COI ratio may not transfer directly to U.S. ER visits. Still, the finding that WTP substantially exceeds COI is consistent across many studies in different countries.

The underlying data for this comparison came from a larger research project that also produced a separate paper focused on the contingent valuation methodology and aggregate benefit estimates (Alberini, Cropper, Fu, Krupnick, Liu, Shaw & Harrington, 1997).

### Stieb et al. (2002) — Putting a Dollar on Respiratory Symptom Days

A Canadian study combined cost-of-illness data, lost productivity estimates, and WTP data (drawing on stated-preference methods related to Johnson et al., 2000) to produce comprehensive valuations for air-pollution-related health events.

**Their respiratory estimate:** The WTP to avoid one **acute respiratory symptom day** was **CAN$13** (1997 Canadian dollars), with a 95% confidence interval of CAN$0 to CAN$28 (Stieb et al., 2002).

**Converting to 2015 U.S. dollars:** In 1997, one Canadian dollar was worth approximately US$0.72. The CPI for Medical Care (BLS Series CUUR0000SAM) was approximately 234.6 in 1997 and 446.8 in 2015 — a ratio of about 1.90.

> CAN$13 × 0.72 (exchange rate) = **US$9.36** (1997$)
> US$9.36 × 1.90 (medical inflation) = **~US$18** (2015$)

That's the WTP for a single *symptom day* — not an ER visit. An ER-level respiratory episode is far more severe and typically involves multiple days of illness, so the per-visit WTP would be considerably higher. This is consistent with the 2–4× ratio found by Alberini & Krupnick.

*Note: The CPI-Medical index values and exchange rate used here are approximate. For precise figures, consult the BLS time series (CUUR0000SAM) and Bank of Canada historical rates directly.*

---

## Cardiovascular Events: The Gap Widens

BenMAP values a cardiovascular ER visit at **$1,161** (2015$) using COI. For cardiac events, the WTP literature suggests the gap between COI and WTP is even larger than for respiratory illness.

### Stieb et al. (2002) — Cardiac Hospital Admission

The same Canadian study that valued respiratory symptom days also estimated WTP for a more severe endpoint: a cardiac hospital admission.

**Their cardiac estimate:** The WTP to avoid one **cardiac hospital admission** was **CAN$5,200** (1997 Canadian dollars), with a 95% confidence interval of CAN$4,000 to CAN$6,400 (Stieb et al., 2002).

**Converting to 2015 U.S. dollars:**

> CAN$5,200 × 0.72 (exchange rate) = **US$3,744** (1997$)
> US$3,744 × 1.90 (medical inflation) = **~US$7,114** (2015$)

The 95% confidence interval converts similarly:

> Lower bound: CAN$4,000 → US$2,880 → **~US$5,472** (2015$)
> Upper bound: CAN$6,400 → US$4,608 → **~US$8,755** (2015$)

**Comparing to BenMAP:** BenMAP's COI for a cardiovascular ER visit is $1,161. The Stieb et al. WTP estimate is roughly **$7,100 in 2015 dollars** — about **6 times higher**. Even the lower bound of the confidence interval (~$5,500) is nearly 5 times the COI value.

**Why is the gap so much larger for cardiac events?** A cardiac event — a heart attack, a stroke, a dangerous arrhythmia — is terrifying. It carries a real risk of death or permanent disability. The pain and anxiety are intense. Recovery can take weeks. People are willing to pay far more to avoid that experience than the hospital bill alone would suggest. The "missing piece" that COI ignores (fear, suffering, life disruption) is enormous for cardiac events.

**An important distinction:** The Stieb et al. figure is for a full cardiac *hospital admission*, which is a more severe event than the average cardiovascular ER visit in BenMAP (which includes many treat-and-release visits). This means the 6× ratio is likely an upper bound for the comparison. The true WTP/COI ratio for the average cardiovascular ER visit is probably somewhere between the respiratory ratio (2–4×) and the cardiac admission ratio (~6×).

### The Underlying Methodology: Johnson, Banzhaf & Desvousges (2000)

The WTP estimates in Stieb et al. drew on a stated-preference framework developed in a methodological paper by Johnson, Banzhaf, and Desvousges. Their study used a **multiple-format stated-preference approach** — participants evaluated health states described using a modified version of the **Quality of Well-Being (QWB) Index**, with four attributes: symptom type, episode duration, activity restrictions, and cost (Johnson et al., 2000).

The study used two different question formats (graded-pair comparisons and discrete-choice experiments) and found that combining formats produced more robust estimates than either alone. The survey was conducted with a Canadian general population sample, and the marginal WTP estimates for health state improvements ranged from approximately CAN$100 to CAN$225, depending on the attribute changed (Johnson et al., 2000).

This methodological paper is significant because it showed that stated-preference techniques *can* produce valid WTP estimates for acute health events — even from people who have never personally experienced the condition being valued.

---

## The Pattern: Severity Drives the WTP/COI Gap

Across the studies reviewed above, a clear pattern emerges: **the more severe and frightening the health event, the larger the gap between what the medical bill says and what people would pay to avoid it.**

### For Mild Acute Illness: WTP Is a Modest Multiple of COI

Alberini and Krupnick (2000) found WTP was 2–4× COI for episodes of acute respiratory illness — conditions like a bad cold or a bout of bronchitis triggered by air pollution. These are unpleasant but not life-threatening. The "missing piece" (discomfort, lost leisure, disrupted plans) is real but bounded.

### For Severe Events: The Gap Grows Dramatically

Stieb et al. (2002) found WTP for cardiac hospital admissions was roughly 6× what a COI-only approach would suggest. Life-threatening events carry an enormous subjective cost that simply does not appear on any bill.

### Why the Ratio Isn't Constant

Several factors push the WTP/COI ratio up or down depending on the condition:

| Factor | Effect on WTP/COI ratio |
|---|---|
| Fear and mortality risk | Higher ratio — cardiac events involve fear that a cold does not |
| Duration of illness | Higher ratio — longer episodes mean more lost life, not just more bills |
| Pain intensity | Higher ratio — severe pain is highly valued to avoid |
| Insurance coverage | Can compress COI toward zero (insurer pays the bill), pushing the ratio higher |
| Third-party payment | For severe inpatient stays, COI may already be high, narrowing the gap |

### Van Houtven et al. (2006) — A Meta-Regression Across Many Studies

Rather than looking at one condition at a time, Van Houtven and colleagues analyzed approximately 210 WTP estimates drawn from roughly 40 published studies of acute health symptoms (Van Houtven, Powers, Jessup & Yang, 2006).

**What they did:** They ran a **meta-regression** — a statistical analysis of results *across* many studies — to find out what predicts how much people are willing to pay to avoid a health event.

**What they found:** The strongest predictors of WTP were:

1. **Illness severity** (measured by the QWB index score) — more severe health states commanded higher WTP
2. **Illness duration** — longer episodes were valued more to avoid
3. **Income** — higher-income respondents stated higher WTP
4. **Study methodology** — the type of survey format affected results

**The practical payoff — benefit transfer functions:** The regression coefficients from this analysis can be used as **benefit transfer functions**. In plain language, a benefit transfer function is a formula that lets you *estimate* WTP for a health condition that nobody has directly studied, by plugging in that condition's severity score and duration and seeing what the formula predicts. This is the closest thing researchers have to a general-purpose WTP calculator for acute health events (Van Houtven et al., 2006).

This approach is important because it partially addresses EPA's main objection to using WTP: the lack of condition-specific estimates for BenMAP's exact endpoints. Benefit transfer functions offer a way to derive WTP estimates for specific ER visit types, even if no study has directly surveyed people about that exact condition.

---

## Why EPA Still Uses COI

Given that WTP is widely considered the theoretically correct measure — and that the studies above suggest COI undercounts the true cost by 2–6× — why does BenMAP still use COI for ER visits?

EPA's own *Guidelines for Preparing Economic Analyses* states clearly that **WTP is the preferred welfare measure** for valuing changes in health risk (U.S. EPA, 2010, Chapter 7). The Guidelines acknowledge that COI provides only a **lower-bound estimate** because it omits pain, suffering, lost leisure, and averting behavior. They recommend using WTP when reliable estimates are available.

The problem is the word "reliable." For ER visits specifically, EPA has concluded that:

1. **No WTP estimates exist for BenMAP's exact endpoints.** Nobody has run a contingent valuation study asking U.S. residents their WTP to avoid a cardiovascular ER visit coded to ICD-9 390–459, or a respiratory ER visit coded to ICD-9 460–519. The available WTP studies cover related but different endpoints (symptom days, hospital admissions, acute illness episodes).

2. **Existing WTP estimates vary too much.** The WTP/COI ratio ranges from roughly 2× for mild respiratory illness to 6× or more for cardiac admissions. Picking a single multiplier to apply across all ER endpoints would require judgment calls that EPA prefers to avoid in a regulatory tool.

3. **COI is a defensible lower bound.** If a regulation passes a cost-benefit test using the conservative COI numbers, it would definitely pass using the higher WTP numbers too. This makes COI a strategically safe choice for EPA — it understates benefits but never overstates them.

4. **The Science Advisory Board endorsed this approach.** EPA's SAB specifically recommended using COI for ER visit endpoints rather than attempting to estimate WTP with insufficient data (as discussed in the companion document).

This doesn't mean EPA ignores WTP entirely. For some other health endpoints (like mortality, valued using the "Value of a Statistical Life"), EPA does use WTP-based estimates. And the benefit transfer approach developed by Van Houtven et al. (2006) offers a potential path forward for future updates to BenMAP's morbidity valuations.

---

## Putting It All Together: COI vs. WTP Side by Side

The following table compares BenMAP's COI-based unit values with the best available WTP evidence:

| Endpoint | BenMAP COI (2015$) | Best Available WTP Evidence (2015$) | Approximate WTP/COI Ratio | Source |
|---|---|---|---|---|
| Cardiovascular ER visit | $1,161 | ~$5,500–$8,800 (from cardiac admission WTP) | ~5–8× | Stieb et al. (2002) |
| Respiratory ER visit (treat-and-release) | $875 | ~$1,750–$3,500 (applying 2–4× ratio) | 2–4× | Alberini & Krupnick (2000) |
| Asthma ER visit | $534 / $447 | No direct single-visit WTP available | Unknown | — |
| Respiratory EHA (65+, admitted) | $11,990 | No direct WTP estimate available | Unknown | — |

**How to read this table:** The cardiovascular and respiratory rows have WTP evidence suggesting BenMAP's COI values undercount the true social cost substantially. The asthma and EHA rows lack direct WTP comparisons — a gap in the literature, not evidence that COI is accurate for those endpoints.

**The bottom line:** For a standard cardiovascular or respiratory ER visit, the true cost to the person — including everything the medical bill misses — is likely **2 to 6 times higher** than what BenMAP reports. This means the total health benefits of air quality regulations are probably substantially larger than BenMAP's official estimates suggest.

This is not a flaw in BenMAP — it's a deliberate choice. EPA would rather report a number it can defend as a floor than a number that might be challenged as too high. But anyone interpreting BenMAP's output should understand that the reported dollar benefits are almost certainly conservative.

---

## Key Takeaways

- **WTP captures what COI misses.** Cost-of-Illness counts the medical bill. Willingness-to-Pay tries to measure the *full* cost, including pain, anxiety, lost time, and life disruption.
- **WTP exceeds COI by 2–6× for acute health events.** For minor respiratory illness, the ratio is roughly 2–4× (Alberini & Krupnick, 2000). For cardiac admissions, it's roughly 5–8× (Stieb et al., 2002).
- **The gap grows with severity.** The more frightening and life-threatening the event, the more people are willing to pay beyond the medical bill.
- **EPA knows COI is a lower bound but uses it anyway** — because no WTP estimates are specific enough to BenMAP's exact ER endpoints, and COI is strategically safe for regulatory cost-benefit analysis.
- **BenMAP's reported benefits are conservative by design.** The true social value of avoided ER visits from cleaner air is likely several times higher than the official numbers.

---

## Bibliography

Alberini, A., Cropper, M., Fu, T.-T., Krupnick, A., Liu, J.-T., Shaw, D., & Harrington, W. (1997). Valuing health effects of air pollution in developing countries: The case of Taiwan. *Journal of Environmental Economics and Management*, 34(2), 107–126.

Alberini, A., & Krupnick, A. (1997). Air pollution and acute respiratory illness: Evidence from Taiwan and Los Angeles. *American Journal of Agricultural Economics*, 79(5), 1620–1624.

Alberini, A., & Krupnick, A. (2000). Cost-of-illness and willingness-to-pay estimates of the benefits of improved air quality: Evidence from Taiwan. *Land Economics*, 76(1), 37–53.

Johnson, F. R., Banzhaf, M. R., & Desvousges, W. H. (2000). Willingness to pay for improved respiratory and cardiovascular health: A multiple-format, stated-preference approach. *Health Economics*, 9(4), 295–317.

Stieb, D. M., De Civita, P., Johnson, F. R., Manary, M. P., Anis, A. H., Beveridge, R. C., & Judek, S. (2002). Economic evaluation of the benefits of reducing acute cardiorespiratory morbidity associated with air pollution. *Environmental Health*, 1, Article 7.

U.S. Environmental Protection Agency. (2010). *Guidelines for preparing economic analyses* (updated 2014). National Center for Environmental Economics, Office of Policy.

Van Houtven, G., Powers, J., Jessup, A., & Yang, J. C. (2006). Valuing avoided morbidity using meta-regression analysis: What can health status measures and QALYs tell us about WTP? *Health Economics*, 15(8), 775–795.
