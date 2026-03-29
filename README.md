# Capstone: The Economic Impact of Wildfire Smoke on Emergency Department Visits

This project estimates the economic cost of wildfire smoke-attributable emergency department visits (EDVs) in California by applying two competing valuation frameworks — Cost-of-Illness (COI) and Willingness-to-Pay (WTP) — to the health burden estimates from Chen et al. (2023). The analysis centers on two endpoints:

- **All respiratory diseases** — 4,597 attributable EDVs on smoke event days (2016-2019)
- **All cardiovascular diseases** — 889 attributable EDVs on smoke event days (2016-2019)

## Background

The EPA's BenMAP-CE tool estimates the health benefits of air quality improvements through a three-step pipeline: (1) measure the air quality change, (2) estimate how many fewer people get sick, and (3) assign a dollar value to each avoided health event. This capstone connects Steps 2 and 3 by taking real-world health burden estimates from a California wildfire smoke study and applying the valuation methods used in EPA regulatory analysis.

BenMAP values ER visits using **Cost-of-Illness** — essentially the medical bill. The economics literature shows that **Willingness-to-Pay** — what people would actually pay to avoid the full experience — is 2 to 6 times higher. By applying both approaches to the same set of attributable EDVs, this project demonstrates how the choice of valuation method changes the estimated economic impact of wildfire smoke on California emergency departments.

## Directory Structure

```
capstone/
├── README.md              # This file
├── CLAUDE.md              # Issues log & project notes
├── session_log.md         # Running log of work sessions
├── sources/               # Original source PDFs (read-only)
│   ├── BenMAP_guide.pdf
│   ├── BenMAP_guide_Appendix_H.pdf
│   ├── Alberini and Krupnick (2000).pdf
│   ├── Johnson, Banzhaf, Desrousges (2000).pdf
│   ├── Stieb et al. (2002).pdf
│   ├── Van Houtven, Powers, Jessup, and Yang (2006).pdf
│   └── Chen_ER_2023.pdf
├── notes/                 # Research summaries and outputs
│   ├── BenMAP_ER_Visit_Valuation.md
│   ├── WTP_ER_Visit_Literature.md
│   ├── review_essay.md
│   ├── Chen_Ebisu_Benmarhnia_Basu_2023.md
│   ├── Alberini_Krupnick_2000.md
│   ├── Johnson_Banzhaf_Desvousges_2000.md
│   └── Stieb_et_al_2002.md
├── figures/                # Generated figures
│   ├── margin_of_error.py
│   └── margin_of_error.png
└── articles/              # PDF processing working directory (read_pdf splits)
```

## Key Sources

| Document | Role in Project |
|---|---|
| **Chen et al. (2023)** | **Core epidemiological study** — provides attributable EDV counts for respiratory (4,597) and cardiovascular (889) outcomes from wildfire smoke in California, 2016-2019 |
| BenMAP-CE Appendix H (Aug 2025) | COI unit values: $1,161/cardiovascular EDV, $875/respiratory EDV, $534 or $447/asthma EDV |
| Alberini & Krupnick (2000) | WTP/COI ratio of 1.48-2.26x for acute respiratory illness (Taiwan) |
| Stieb et al. (2002) | Comprehensive WTP valuations: CAN$5,200/cardiac admission, CAN$2,000/respiratory ED visit |
| Johnson, Banzhaf & Desvousges (2000) | Stated-preference WTP methodology underlying Stieb et al. |
| Van Houtven et al. (2006) | Meta-regression of 230+ WTP estimates from 17 studies; benefit-transfer functions |
| BenMAP-CE User's Manual (Aug 2025) | Full guide to the BenMAP-CE tool and methodology |
