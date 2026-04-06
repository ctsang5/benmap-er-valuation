# Aguilera et al. (2021) — Reading Notes
*Nature Communications 12:1493 (2021)*

## 1. Research Question
Is wildfire-specific PM2.5 more harmful to respiratory health than PM2.5 from other (non-wildfire) sources? Current air quality regulations treat all PM2.5 as equally toxic regardless of source — this paper tests that assumption.

## 2. Audience
Environmental epidemiologists, air quality policy researchers, OEHHA researchers (paper was partly funded by OEHHA #19-E0022). Directly relevant to the regulatory debate about whether BenMAP/EPA concentration-response functions designed for ambient PM2.5 are appropriate for wildfire smoke.

## 3. Method
Four analytical approaches to isolate wildfire-specific PM2.5 in Southern California (Santa Ana wind domain), 1999–2012 (excluding summer months Jun–Aug):

1. **Instrumental variable (IV) / two-stage regression**: Strong Santa Ana winds + wildfire upwind as joint instrument for wildfire PM2.5. Isolates local average treatment effect of smoke PM2.5 on admissions.
2. **Spatio-temporal multiple imputation**: Cubic spline interpolation imputes non-smoke background PM2.5 on smoke-exposed days; wildfire PM2.5 = total − imputed non-smoke.
3. **Interaction effect (Poisson)**: ZIP code fixed effects Poisson regression with PM2.5 × wildfire indicator interaction; β1 captures non-wildfire effect, β1+β3 captures wildfire PM2.5 effect.
4. **Seasonal interpolation** (Lipner et al. method): Non-smoke background = seasonal median of non-exposed days; wildfire PM2.5 = total − seasonal background.

Two exposure definitions used: (i) fire upwind + strong SAW, (ii) HMS smoke plumes within 160 km buffer.

## 4. Data
- **Study region**: 696 zip codes in the Santa Ana wind domain, Southern California
- **Study period**: September–May, 1999–2012 (summer excluded)
- **Health outcome**: Daily hospital admissions for respiratory diseases (ICD-9 codes 460–519: asthma, COPD, pneumonia, interstitial lung disease), n = **1,655,011** admissions; from California OSHPD patient discharge database
- **PM2.5**: Daily zip code-level estimates from EPA AQS monitoring stations within 20 km, inverse distance weighted; available for 578 zip codes (mean 33% missing)
- **Wildfire perimeters**: CalFire FRAP, 1999–2012
- **SAW**: Daily SAWRI (Santa Ana Wind Regional Index), threshold = 3.06 m/s (median conditional on positive)
- **Smoke plumes**: NOAA HMS, available from September 2005 onward
- **Weather**: NOAA NCEI ISD (wind speed, temperature, humidity)
- **Unit of observation**: Zip code-day
- **Software**: ArcGIS 10.5, R 3.5.1, Stata 16

## 5. Statistical Methods
All models control for: flu admissions, weather covariates (wind speed, temp, humidity), day-of-week, month-of-year, zip code fixed effects, linear time trend.

IV first stage: PM2.5 ~ wildfire upwind × strong SAW + controls + zip FE
IV second stage: Resp admissions ~ fitted PM2.5 + controls

Interaction model (Poisson):
> Resp ~ exp(log(Pop) + β1×PM2.5 + β2×Wildfire + β3×PM2.5×Wildfire + controls + zip FE + time)

Non-wildfire effect = β1; wildfire PM2.5 effect = β1 + β3 (delta method for SEs).

## 6. Findings

**Key result (Table 1, fire upwind + strong SAW exposure definition):**

| Approach | Non-smoke % change per 10 μg/m³ | Wildfire-specific % change per 10 μg/m³ |
|---|---|---|
| Aggregated (no separation) | 0.76% (0.42–1.1) | — |
| IV | 3.8% (−1.2 to 8.9) | — |
| Imputation | 0.72% (0.36–1.1) | **10.0% (3.5–16.5)** |
| Interaction | 0.67% (0.48–0.86) | 1.28% (0.37–2.19) |
| Seasonal interpolation | 1.3% (0.97–1.7) | 3.0% (−0.37 to 6.3) |

Wildfire-specific PM2.5 is **up to 10 times more harmful** than non-wildfire PM2.5, consistently across methods.

Toxicological support: Wildfire PM2.5 is mostly carbonaceous (50%+ organic carbon), has higher oxidative potential, generates more free radicals, induces inflammation and oxidative stress. Mouse studies show 3–4x greater lung toxicity from wildfire vs. ambient PM.

## 7. Contributions
- First study to assess wildfire vs. non-wildfire PM2.5 differential toxicity at zip code resolution over 14 years spanning multiple wildfires
- Compares four distinct analytical methods, finding consistent direction of effect
- Provides epidemiological evidence supporting the hypothesis that equal-mass exposures to wildfire PM2.5 cause greater health harm than ambient PM2.5

## 8. Replication Feasibility
- Health data (OSHPD): Available upon reasonable request
- PM2.5, CalFire, HMS, weather data: Publicly available (URLs in paper)
- Code: Available from corresponding author upon request
- No public replication archive

## Project Relevance
- **Critical for the capstone**: Provides the key justification for why BenMAP's COI-only unit values derived from ambient PM2.5 studies may *undervalue* wildfire smoke-attributable ED visits. If wildfire PM2.5 is up to 10x more toxic than the PM2.5 in the epidemiological studies underlying BenMAP's concentration-response functions, then applying those functions to wildfire smoke may underestimate actual health burden.
- The imputation result (10% per 10 μg/m³) vs. aggregated (0.76%) is the most frequently cited finding.
- OEHHA funding: This paper has an institutional link to the capstone's requesting agency.
- Chen et al. (2023) — the paper that provides the ED visit counts our capstone values — directly cites and builds on Aguilera et al. (2021).
