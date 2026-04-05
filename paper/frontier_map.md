# Frontier Map: Economic Valuation of Wildfire Smoke-Attributable ED Visits

## Overview

This document maps the current state of knowledge at the intersection of wildfire smoke epidemiology and economic valuation, identifying where active research clusters exist, where gaps remain, and how different literature strands connect.

---

## 1. What Has Been Done

### 1.1 Wildfire Smoke Epidemiology (Well-Established)

The causal link between wildfire smoke PM2.5 and emergency department visits is firmly established. Key findings:

- **Respiratory ED visits**: Consistently elevated during smoke events. Chen et al. (2023) report 14.4% increases in all-respiratory ED visits and 57.1% increases for asthma in California. Wettstein et al. (2018) confirm respiratory elevations across 8 California air basins.
- **Cardiovascular/cerebrovascular ED visits**: Growing evidence. Wettstein et al. (2018) document elevated risks for MI, ischemic heart disease, heart failure, and stroke on dense smoke days, especially among adults 65+.
- **Dose-response nonlinearity**: Heft-Neal et al. (2023) show that total ED visits decline at extreme smoke concentrations (behavioral avoidance), while respiratory-specific visits increase 30-110%. This concave shape challenges linear valuation models.
- **Differential toxicity**: Aguilera et al. (2021) find wildfire PM2.5 is 1.5-8x more harmful per ug/m3 than non-wildfire PM2.5. Darling et al. (2023) show that ignoring this differential underestimates California's respiratory burden by ~13%.
- **Systematic reviews**: Reid et al. (2016) and Liu et al. (2015) synthesize the evidence base; Cascio (2018) adds the EPA perspective.

**Assessment**: This strand is mature. The epidemiological relationships are well-characterized, though questions remain about mental health endpoints, chronic effects, and threshold effects at very high concentrations.

### 1.2 Economic Valuation of Wildfire Smoke Health Effects (Active but Fragmented)

Several approaches have been applied, but no unified framework exists:

- **COI-based valuation**: Kochi et al. (2016) estimate $3.4M in medical costs from the 2007 SoCal fires using hospital/ED cost data. This is straightforward but widely acknowledged to underestimate total welfare losses.
- **WTP via defensive behavior**: Richardson et al. (2012) estimate WTP of $84.42/person/day versus $9.50 COI. Richardson et al. (2013) confirm with a second method (contingent valuation: $95/day). The WTP-COI ratio of approximately 9:1 is a critical finding.
- **Benefits transfer using BenMAP-CE**: Jones (2016) applies BenMAP-CE to the Wallow mega-fire; Jones & Berrens (2017) scale to the Western US; Fann et al. (2018) provide national estimates. All rely on BenMAP-CE's default unit values.
- **Mortality valuation**: Connolly et al. (2024) estimate $432-456B from California wildfire mortality (2008-2018) using wildfire-specific dose-response functions. This mortality estimate dwarfs existing morbidity estimates, suggesting morbidity costs are relatively under-studied.

**Assessment**: Active research area but no study has combined California wildfire smoke ED visit epidemiology with a systematic critique of the valuation approach. Most studies either do epidemiology OR economics, not both critically.

### 1.3 BenMAP-CE Critique (Emerging)

A small but growing body of work identifies specific deficiencies in BenMAP-CE's valuation framework:

- **Ambulatory care gap**: Birnbaum et al. (2020) document a ~40% underestimate from missing ambulatory care costs.
- **Work-loss underestimate**: Meng et al. (2024) find BenMAP-CE underestimates wildfire work-loss by 5-10x in California.
- **Non-wildfire-specific dose-response**: Multiple studies (Aguilera 2021; Darling 2023) show that generic PM2.5 concentration-response functions are inappropriate for wildfire contexts.
- **Missing defensive expenditures**: Richardson et al. (2012, 2013) show that COI misses the majority of welfare cost. Han et al. (2024) document significant defensive spending on air purifiers and health products.

**Assessment**: This is where the frontier is most active and where the most impactful contributions can be made. The critique is scattered across individual papers; no single study synthesizes all the dimensions of BenMAP-CE underestimation.

### 1.4 Environmental Justice Dimensions (Growing)

- **Exposure disparities**: Liu et al. (2021) and Tessum et al. (2019, 2021) establish that PM2.5 exposure is systematically higher for racial/ethnic minorities.
- **Wildfire-specific disparities**: Masri et al. (2021) show elderly and low-income Californians are disproportionately affected. Darling et al. (2023) find differential toxicity underestimation is worse in high-SVI areas.
- **Community vulnerability**: Rappold et al. (2017) develop a vulnerability index incorporating health, demographic, and socioeconomic factors.
- **Adaptive capacity**: Han et al. (2024) show defensive spending varies with socioeconomic status, implying unequal ability to mitigate exposure.

**Assessment**: Well-established for general PM2.5, growing for wildfire-specific contexts. The economic justice dimension -- whether valuation methods themselves embed inequity -- is underexplored.

---

## 2. What Methods Have Been Used

| Method | Papers | Strengths | Weaknesses in This Context |
|--------|--------|-----------|---------------------------|
| **Cost of Illness (COI)** | Kochi et al. 2016; BenMAP-CE defaults | Transparent, data-driven, widely accepted | Misses disutility, defensive spending, ambulatory care; underestimates by ~9x per Richardson et al. |
| **Defensive Behavior (Revealed Preference WTP)** | Richardson et al. 2012; Han et al. 2024 | Observed market behavior, no hypothetical bias | Requires individual-level expenditure data; may underestimate if defensive options are limited |
| **Contingent Valuation (Stated Preference WTP)** | Richardson et al. 2013 | Can capture non-market values including disutility | Hypothetical bias, anchoring, protest responses |
| **Benefits Transfer** | Jones 2016; Jones & Berrens 2017 | Scalable, low cost, leverages existing estimates | Transfer error; sensitivity to source study selection; may not match local conditions |
| **BenMAP-CE (Integrated)** | Fann et al. 2018; Meng et al. 2024 | EPA standard tool, reproducible, includes multiple endpoints | Default COI values, non-wildfire-specific CRFs, missing cost categories |
| **Instrumental Variables** | Deryugina et al. 2019 | Causal identification of air pollution costs | General PM2.5, not wildfire-specific; Medicare population only |
| **Health Impact Assessment** | Darling et al. 2023; Connolly et al. 2024 | Combines exposure modeling with health/economic endpoints | Sensitive to CRF choice and unit value assumptions |

---

## 3. What Data Has Been Used

| Dataset | Coverage | Used By | Relevance to Capstone |
|---------|----------|---------|----------------------|
| **California OSHPD/HCAI** | CA ED visits and hospital discharges | Chen et al. 2023; Wettstein et al. 2018; Kochi et al. 2016 | Primary source for ED visit counts and costs |
| **CMAQ Fire PM2.5** | National; daily gridded estimates | Fann et al. 2018; Connolly et al. 2024; Meng et al. 2024 | Wildfire-specific PM2.5 attribution |
| **Stanford ECHO Lab Smoke PM2.5** | National; daily zip-code level | Heft-Neal et al. 2023 | High-resolution smoke exposure |
| **BenMAP-CE Appendix H** | Default unit values for health endpoints | EPA standard; Fann et al. 2018; Jones 2016 | The valuation framework being critiqued |
| **Medicare Claims** | US elderly (65+) | Deryugina et al. 2019; Liu et al. 2017 | Health costs for elderly subpopulation |
| **CHIS** | CA population health survey | Meng et al. 2024 | Work-loss and self-reported health data |
| **NielsenIQ Retail Scanner** | US retail purchases | Han et al. 2024 | Defensive spending on health products |
| **ACS/Census** | Sociodemographic data | Masri et al. 2021; Rappold et al. 2017 | Environmental justice analysis |
| **CDC WONDER** | National mortality/morbidity rates | Fann et al. 2012, 2018 | Baseline incidence rates |

---

## 4. Where the Gaps Are

### Gap 1: No Integrated Valuation Critique for Wildfire ED Visits (PRIMARY GAP)
No existing study systematically quantifies ALL dimensions of BenMAP-CE underestimation for wildfire smoke ED visits in a single analysis. The pieces exist separately: Birnbaum (ambulatory care), Meng (work loss), Richardson (WTP vs COI), Aguilera/Darling (differential toxicity). Nobody has assembled these into a comprehensive assessment of how much the default BenMAP-CE values underestimate the true economic cost of wildfire smoke ED visits.

### Gap 2: California-Specific Morbidity Valuation
Connolly et al. (2024) provide California-specific wildfire mortality valuation ($432-456B). No equivalent California-specific morbidity valuation exists for ED visits. Chen et al. (2023) provide the epidemiology; the economic valuation has not been done.

### Gap 3: Connecting Epidemiology to Economics with Appropriate Unit Values
Studies either estimate ED visit counts (Chen et al. 2023; Heft-Neal et al. 2023) or critique valuation methods (Richardson et al. 2012, 2013; Birnbaum et al. 2020) but do not combine state-of-the-art epidemiological estimates with WTP-adjusted unit values.

### Gap 4: Equity-Adjusted Valuation
While environmental justice literature documents unequal exposure and vulnerability, no study examines whether BenMAP-CE's uniform unit values per ED visit capture the differential economic burden across communities with different baseline health conditions, income levels, and adaptive capacities.

### Gap 5: Behavioral Avoidance Costs
Heft-Neal et al. (2023) document behavioral avoidance during extreme smoke events, and Han et al. (2024) measure defensive spending, but the welfare costs of avoidance behavior are not incorporated into any existing wildfire smoke valuation framework.

---

## 5. Where This Capstone Fits

This capstone directly addresses **Gap 1** and partially addresses **Gaps 2 and 3** by:

1. Taking Chen et al.'s (2023) California wildfire smoke ED visit estimates as the epidemiological foundation
2. Applying BenMAP-CE's default COI unit values to generate a baseline valuation
3. Systematically documenting how and by how much BenMAP-CE underestimates, drawing on:
   - Richardson et al.'s WTP-to-COI ratio (~9x)
   - Birnbaum et al.'s ambulatory care gap (~40%)
   - Meng et al.'s work-loss underestimate (5-10x)
   - Aguilera et al.'s differential toxicity evidence (1.5-8x)
4. Producing adjusted estimates that better approximate the true economic burden
5. Discussing implications for environmental policy and equity

The capstone's contribution is **synthetic and applied**: it is the first study to assemble the scattered critique of BenMAP-CE's unit values into a single, California-specific analysis of wildfire smoke ED visit costs.

---

## 6. Scooping Risk Assessment

### LOW-MODERATE overall risk

**No paper found that combines Chen et al. (2023) ED visit estimates with systematic economic valuation.**

| Potential Competitor | Risk Level | Differentiation |
|---------------------|------------|-----------------|
| Meng et al. (2024) | Moderate | Focuses on work-loss days, not ED visits; uses CHIS data not OSHPD |
| Connolly et al. (2024) | Low | Focuses on mortality, not morbidity |
| Darling et al. (2023) | Low | Health impact assessment, not economic valuation |
| Heft-Neal et al. (2023) | Low | Epidemiology focus; no valuation component |
| OEHHA internal work | Unknown | Chen et al. (2023) are OEHHA researchers; possible internal follow-up not detected in published literature |

**Primary risk**: An OEHHA or CalEPA team could be working on economic valuation as a follow-up to Chen et al. (2023), but no evidence of this was found in published or working paper literature as of April 2026.

**Mitigating factors**: (1) The capstone's contribution is primarily methodological critique of BenMAP-CE, not new epidemiology; (2) the synthesis across multiple dimensions of underestimation is novel; (3) as a master's capstone, the contribution bar is appropriate.

---

## Connection Map

```
                    EPIDEMIOLOGY                          ECONOMICS
                    ============                          =========

  Reid 2016 (review)                          EPA Guidelines (2024)
        |                                           |
  Cascio 2018 (review)                       BenMAP-CE Appendix H
        |                                           |
  Aguilera 2021 -----> Differential          Richardson 2012, 2013
  (differential         toxicity gap ------> (WTP ~9x COI)
   toxicity)                |                       |
        |                   |                Birnbaum 2020
  Chen 2023 ---------> [THIS CAPSTONE] <---- (ambulatory gap ~40%)
  (CA ED visits)        synthesizes all             |
        |               dimensions           Meng 2024
  Heft-Neal 2023                             (work-loss gap 5-10x)
  (nonlinear                                        |
   dose-response)                            Han 2024
        |                                    (defensive spending)
  Wettstein 2018                                    |
  (CV/cerebrovascular)                       Kochi 2016
                                             (COI-only estimate)
                              |
                    ENVIRONMENTAL JUSTICE
                    ====================
                    Masri 2021 (CA disparities)
                    Liu 2021 (racial/ethnic PM2.5)
                    Tessum 2019, 2021 (systemic inequality)
                    Darling 2023 (differential burden in high-SVI)
                    Rappold 2017 (community vulnerability index)
```

---

## Timeline of Key Publications

```
2012  Richardson et al. -- WTP vs COI for wildfire smoke (9:1 ratio)
2013  Richardson et al. -- Revealed vs stated preference comparison
2015  Liu et al. -- Systematic review of wildfire smoke health impacts
2016  Reid et al. -- Critical review (EHP)
2016  Jones -- BenMAP-CE mega-fire case study
2016  Kochi et al. -- COI of 2007 SoCal fire ED visits
2016  Robinson & Hammitt -- Fatal illness risk valuation
2017  Jones & Berrens -- Western US benefits transfer
2017  Rappold et al. -- Community vulnerability index
2017  Liu et al. -- Wildfire PM2.5 and hospital admissions
2018  Cascio -- Wildland fire smoke review
2018  Wettstein et al. -- CV/cerebrovascular ED visits in CA
2018  Fann et al. -- National BenMAP-CE wildfire valuation
2019  Deryugina et al. -- Air pollution mortality costs (AER)
2019  Tessum et al. -- Consumption-exposure inequity (PNAS)
2020  Birnbaum et al. -- BenMAP-CE ambulatory care gap (Health Affairs)
2020  Dittrich & McCallum -- Systematic review of wildfire cost methods
2021  Aguilera et al. -- Differential toxicity (Nature Comms)
2021  Masri et al. -- CA wildfire disparities
2021  Liu et al. -- Racial/ethnic PM2.5 disparities (EHP)
2021  Tessum et al. -- Systemic PM2.5 inequity (Sci Advances)
2023  Chen et al. -- CA wildfire smoke ED visits (Env Research) ***
2023  Heft-Neal et al. -- Nonlinear ED visit response (PNAS)
2023  Darling et al. -- Zip-code burden + differential toxicity
2024  Meng et al. -- Work-loss BenMAP-CE gap (BMJ Public Health) ***
2024  Connolly et al. -- CA wildfire mortality valuation (Sci Advances)
2024  Han et al. -- Defensive spending (Env & Resource Econ)
2024  EPA -- Guidelines for Economic Analyses, 3rd ed.
2026  THIS CAPSTONE -- Synthesizing valuation critique for CA ED visits

*** = Most directly relevant recent publications
```
