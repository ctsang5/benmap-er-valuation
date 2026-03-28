# Capstone: EPA BenMAP Emergency Room Visit Valuation Analysis

This project examines how the U.S. Environmental Protection Agency (EPA) uses the BenMAP-CE (Benefits Mapping and Analysis Program - Community Edition) tool to estimate the economic value of air-pollution-related emergency room visits. The focus is on three health endpoints:

- **Cardiovascular disease** (All Cardiac Outcomes, ICD 390-459)
- **Asthma** (ICD 493)
- **Respiratory disease** (ICD 460-519)

## Background

BenMAP-CE is EPA's primary tool for estimating the health benefits of changes in air quality. It links changes in pollutant concentrations to health outcomes using epidemiological concentration-response functions, then assigns dollar values to those outcomes using Cost-of-Illness (COI) and Willingness-to-Pay (WTP) approaches. This capstone focuses on the ER visit valuation side of that pipeline.

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
│   ├── Chen_ER_2023.pdf
│   ├── Nguyen_AQAH_2024.pdf
│   └── Ostro_ER_2024.pdf
├── notes/                 # Research summaries and outputs
│   ├── BenMAP_ER_Visit_Valuation.md
│   ├── WTP_ER_Visit_Literature.md
│   ├── review_essay.md
│   ├── Alberini_Krupnick_2000.md
│   ├── Johnson_Banzhaf_Desvousges_2000.md
│   └── Stieb_et_al_2002.md
├── figures/                # Generated figures
│   ├── margin_of_error.py
│   └── margin_of_error.png
└── articles/              # PDF processing working directory (read_pdf splits)
```

## Key Sources

| Document | Description |
|---|---|
| BenMAP-CE User's Manual (Aug 2025) | Full guide to the BenMAP-CE tool |
| Appendix H | Core health valuation functions used in the U.S. setup |
| Alberini & Krupnick (2000) | WTP vs. COI comparison for respiratory illness in Taiwan |
| Johnson, Banzhaf & Desvousges (2000) | Stated-preference WTP methodology for acute health events |
| Stieb et al. (2002) | Comprehensive valuation of acute cardiorespiratory morbidity (Canada) |
| Van Houtven et al. (2006) | Meta-regression of WTP estimates for acute health symptoms |
| Chen et al. (2023) | Research on air pollution and ER visits |
| Nguyen et al. (2024) | Air quality and health outcomes |
| Ostro et al. (2024) | ER visit health impact analysis |
