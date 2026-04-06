# Harrington & Portney (1987) — Reading Notes
*Journal of Urban Economics 22, 101–112 (1987)*
**THEORETICAL FOUNDATION: establishes COI as a lower bound on WTP**

## 1. Research Question
What is the relationship between the cost-of-illness (COI) approach — which sums direct medical costs and lost wages — and true willingness to pay (WTP) for health improvements from regulation? Is COI an underestimate, overestimate, or correct measure of true benefits?

## 2. Audience
Environmental economists and regulatory analysts. Funded in part by EPA's Office of Air Quality Planning and Standards. Directly motivated by the practical problem of valuing health benefits in regulatory cost-benefit analysis.

## 3. Method
Pure microeconomic theory — no data, no empirical estimation.

**Model setup**: Individual utility function U(X, L, S) where:
- X = expenditures on non-health goods
- L = leisure time
- S = time spent ill (S enters utility negatively: Uₛ < 0)
- P = pollution (environmental threat)
- D = defensive/averting expenditures (reduce illness)
- M = mS = medical expenses (daily cost m × days sick)
- S = S(D, P), where Sₐ < 0 (defense reduces illness), Sₚ > 0 (pollution increases illness)

The individual maximizes utility subject to a full-income constraint (Becker [1]).

**Benefit measure**: Compensating variation — income change I*(P) needed to hold utility constant as P changes. Marginal WTP = dI*/dP = −Sₚ/Sᴅ (Equation 17).

**COI measure**: dC/dP = (w + m)(dS/dP) — lost wages (w) plus medical costs (m) per unit change in illness days.

## 4. Data
None — theoretical paper only.

## 5. Key Results

**Central equation (22)**:
> dI*/dP = w(dS/dP) + m(dS/dP) − (Uₛ/λ)(dS/dP) + Dₚ

Where:
- First two terms = COI (lost wages + medical costs)
- −(Uₛ/λ)(dS/dP) = dollar value of **disutility** of illness (always positive, since Uₛ < 0 and dS/dP > 0)
- Dₚ = change in defensive expenditures from pollution increase

**Main finding**: If dS/dP > 0 (pollution increases illness), then:
> **WTP > COI + defensive expenditures**

COI + defensive expenditures **underestimate** true WTP because COI omits the disutility of illness. The only way COI + averting could *overestimate* WTP is if increased pollution somehow improved health (dS/dP < 0) — extremely unlikely in practice.

**Practical conclusion**: *"The cost-of-illness approach can be used as a lower bound for true benefits in most interesting cases."* (p. 112)

**Extensions (Section 3) — conclusion holds under:**
1. P enters utility directly (extra disutility of pollution per se makes underestimate even worse)
2. Illness affects the wage rate (COI must be reformulated but underestimate persists)
3. Paid sick leave (ambiguous, but still an underestimate when lost wages counted only during actual work hours, as is standard in COI studies)

## 6. Contributions
- First rigorous theoretical proof that COI is a lower bound on WTP for morbidity valuation
- Establishes the three components of true benefits: (1) COI, (2) defensive expenditures, (3) disutility of illness
- Provides the foundational justification for using WTP-based values in environmental regulation rather than COI
- The disutility term is unobservable — this is why empirical WTP studies (contingent valuation, etc.) are needed to capture it

## 7. Replication
No data, no code. Pure theory. 12 pages in Journal of Urban Economics.

## Project Relevance
- **The single most important theoretical paper** for the capstone's core argument: BenMAP uses COI-only values for ED visits ($36,000/admission), which Harrington & Portney (1987) prove is a **lower bound** on the true welfare cost of illness
- Provides the welfare-theoretic foundation for why WTP-based alternatives (Stieb et al., Richardson et al.) would yield higher unit values than BenMAP's COI
- The capstone question "are BenMAP's numbers the reasonable and best fit?" maps directly onto this paper: the answer is no if we want WTP, but yes if we want a lower-bound/conservative estimate
- Funded by EPA OAQPS — the same institutional context as BenMAP — making this an internal critique of COI practice
- **Key quote for the capstone**: "the cost-of-illness approach can be used as a lower bound for true benefits in most interesting cases" (p. 112)
