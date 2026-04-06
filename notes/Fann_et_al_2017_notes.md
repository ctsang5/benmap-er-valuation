# Fann et al. (2017) — Reading Notes
*Science of the Total Environment 610–611 (2018) 802–809*

## 1. Research Question
What is the number and economic value of premature deaths and illnesses attributable to wildland fire PM2.5 in the continental U.S. over a multi-year period (2008–2012)? First study to do this nationally across multiple years.

## 2. Audience
EPA analysts, environmental health economists, air quality policy researchers. Directly connected to BenMAP-CE methodology; Neal Fann is at EPA Office of Air Quality Planning and Standards.

## 3. Method
Health impact assessment (HIA) using:
- Photochemical air quality modeling (CMAQ v5.1) with and without fire emissions to isolate fire-attributable PM2.5
- Concentration-response functions from epidemiological literature applied via BenMAP-CE v1.1
- Economic valuation using VSL and COI

Health impact function:
> y_ija = m0_ija × (e^(β × C_ij) − 1) × P_ija

where β = risk coefficient, m0_ija = baseline death/admission rate (county j, year i, age strata a), C_ij = annual mean wildfire PM2.5 (county j, year i), P_ija = population.

## 4. Data
- **Air quality**: CMAQ v5.1, 12×12 km grid, 2008–2012, continental U.S.; wildfire emissions from Hazard Mapping System + Sonoma Technology SMARTFIRE v2
- **Mortality baseline**: CDC WONDER county-level age-stratified all-cause death rates, 2010
- **Hospital rates**: Healthcare Cost and Utilization Program (HCUP) — mixture of county, state, regional rates
- **Population**: 2010 U.S. Census (stratified by age, sex, race, ethnicity) via BenMAP-CE; 2011–2012 projected via Woods & Poole
- **Unit of observation**: County-year
- **Time period**: 2008–2012

## 5. Statistical Methods
- Random effects meta-analysis of 4 studies for respiratory hospital admissions (PM10, wildfire-specific); concluded not usable for HIA (non-U.S. studies, PM10 not PM2.5)
- Final effect coefficients used:
  - Respiratory hospital admissions: **Delfino et al. (2009)** (2003 SoCal wildfires) and **Zanobetti et al. (2009)**
  - Cardiovascular admissions: **Delfino et al. (2009)**
  - Short-term mortality: **Zanobetti & Schwartz (2009)**
  - Long-term mortality: **Krewski et al. (2009)** (ACS cohort) and **Lepeule et al. (2012)** (Harvard Six Cities)

## 6. Findings

**Health counts (annual, 2008–2012 range):**
| Endpoint | Annual range |
|---|---|
| Respiratory hospital admissions (Delfino) | 5,200–8,500 |
| Cardiovascular hospital admissions (Delfino) | 1,500–2,800 |
| Premature deaths, short-term (Zanobetti & Schwartz) | 1,500–2,500 |
| Premature deaths, long-term (Krewski) | 8,700–14,000 |
| Premature deaths, long-term (Lepeule) | 19,000–32,000 |

**Economic values (2010$):**
| Scenario | Annual | Net present value (5-yr, 3% discount) |
|---|---|---|
| Short-term mortality + resp. admissions | $11–20B | $63B (95% CI: $6–$170B) |
| Long-term mortality + resp. admissions | $76–130B | $450B (95% CI: $42–$1,200B) |

**Unit values used:**
- VSL: **$10.1M** (2010 inflation, 2016 income, per EPA Guidelines for Preparing Economic Analyses)
- Respiratory hospital admission: **$36,000** (COI — direct medical costs + lost earnings, from PM2.5 NAAQS RIA)

**Note:** The $36,000 hospital COI value is the same BenMAP unit value relevant to our capstone project. (This is hospital admission, not strictly emergency department visits)

## 7. Contributions
- First national, multi-year characterization of wildland fire PM2.5 health and economic burden in the U.S.
- First quantitative meta-analysis of wildland fire epidemiological studies
- Characterizes distributional burden by race: Black populations disproportionately exposed in highly affected areas

## 8. Replication Feasibility
- BenMAP-CE v1.1 is publicly available (EPA)
- CMAQ model is open-source
- CDC WONDER mortality data: publicly available
- HCUP hospital rates: available (some purchase required)
- Fire emissions: SMARTFIRE v2 / HMS fire detections
- No replication archive mentioned, but methods well-documented

## Project Relevance
- Directly validates BenMAP-CE approach for wildfire health valuation
- The $36,000 COI for respiratory hospital admissions is the same unit value used in our capstone baseline
- The VSL of $10.1M (2016 income, 2010$) is the relevant comparator for WTP-vs-COI discussion
- Fann et al. use the same hospital COI approach we're critiquing — this paper is the methodological precedent
- Supports argument that BenMAP COI values are consistent with peer-reviewed EPA methodology
