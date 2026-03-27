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
│   ├── Chen_ER_2023.pdf
│   ├── Nguyen_AQAH_2024.pdf
│   └── Ostro_ER_2024.pdf
├── notes/                 # Research summaries and outputs
│   ├── BenMAP_ER_Visit_Valuation_Summary.md
│   └── BenMAP_ER_Visit_Methodology_Deep_Dive.md
└── articles/              # PDF processing working directory
```

## Key Sources

| Document | Description |
|---|---|
| BenMAP-CE User's Manual (Aug 2025) | Full guide to the BenMAP-CE tool |
| Appendix H | Core health valuation functions used in the U.S. setup |
| Chen et al. (2023) | Research on air pollution and ER visits |
| Nguyen et al. (2024) | Air quality and health outcomes |
| Ostro et al. (2024) | ER visit health impact analysis |

## Status

Work in progress. See `session_log.md` for detailed progress tracking.
