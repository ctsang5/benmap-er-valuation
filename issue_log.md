## Issues Log

### 2026-03-26: `python3` command fails on Windows, use `python`
- **Context:** Running the read_pdf skill's PyPDF2 split script.
- **Problem:** `python3 -c "..."` returned `ModuleNotFoundError: No module named 'PyPDF2'` even though PyPDF2 was installed under `C:\Users\chris\AppData\Roaming\Python\Python313\site-packages`.
- **Cause:** On this Windows environment, `python3` and `python` resolve differently. `python` is the correct command.
- **Resolution:** Switched to `python -c "..."` and the script ran successfully.
- **Takeaway:** Always use `python` (not `python3`) for scripts on this machine.

### 2026-03-27: Old markdown files were too jargon-heavy to be useful
- **Context:** The Summary and Deep Dive notes from Sessions 1-3 were written at a technical level that assumed familiarity with EPA methodology, health economics, and survey statistics.
- **Problem:** Terms like COI, WTP, CCR, ICD crosswalk, Taylor series linearization, Latin Hypercube Sampling, and survey estimation were used without explanation. Structure followed the source material's organization rather than a logical learning flow.
- **Solution:** Merged both files into a single `BenMAP_ER_Visit_Valuation.md` rewritten for a reader with no background. Every term is defined in plain language on first use. Sections are ordered by narrative logic (what is this → how does it work → where's the data → what are the numbers → how certain are we). Concrete examples and worked arithmetic replace abstract descriptions.
- **Takeaway:** Write notes as if explaining to a classmate, not summarizing for an expert. Define jargon before using it. Use concrete examples (e.g., $3,200 × 0.38 = $1,216) instead of describing procedures abstractly.

### 2026-03-27: Discharge weight explanation was misleading
- **Context:** The rewritten document initially explained discharge weights by saying rural hospitals get higher weights "because they're small."
- **Problem:** The weight has nothing to do with hospital size. It reflects how many similar hospitals exist nationally versus how many were sampled. A small rural hospital gets a high weight because few rural hospitals made it into the sample, so each one stands in for many others.
- **Solution:** Rewrote the discharge weight explanation in both the "Problem 3" section and the cardiovascular calculation walkthrough to focus on representativeness.
- **Takeaway:** When explaining statistical concepts, be precise about causation. "What drives X" is a different question than "what correlates with X."

### 2026-03-27: Two unrelated `capstone/` directories existed
- **Context:** `C:\Users\chris\capstone\` contained Bloomberg options data (a different project). `C:\Users\chris\OneDrive\Desktop\capstone\` is the EPA BenMAP capstone.
- **Problem:** Risk of confusion between the two.
- **Solution:** Deleted `C:\Users\chris\capstone\` after confirming with user.
- **Takeaway:** The active capstone directory is `C:\Users\chris\OneDrive\Desktop\capstone\`.

### 2026-03-27: WTP dollar figures were misattributed to the wrong paper
- **Context:** Initial web research for the WTP literature review attributed the $13/respiratory-symptom-day and $5,200/cardiac-admission figures to Johnson, Banzhaf & Desvousges (2000).
- **Problem:** These figures actually come from Stieb et al. (2002) in *Environmental Health*. Johnson et al. (2000) is the underlying *methodology* paper that developed the stated-preference framework; Stieb et al. is the *applied policy* paper that produced the dollar estimates. F. Reed Johnson is a co-author on both, which likely caused the confusion in secondary sources.
- **Resolution:** Ran three parallel verification agents to confirm exact citations, authorship, journal, and dollar figures against primary sources before writing the document. Correctly attributed all figures in `WTP_ER_Visit_Literature.md`.
- **Takeaway:** Always verify study details against primary sources (PubMed, journal websites) before citing. Secondary summaries and search results frequently misattribute findings, especially when the same authors appear on related papers.

### 2026-03-27: WTP figures from Stieb et al. are in Canadian dollars, not U.S. dollars
- **Context:** The Stieb et al. (2002) WTP estimates (CAN$13/symptom-day, CAN$5,200/cardiac admission) are in 1997 Canadian dollars.
- **Problem:** Treating these as U.S. dollars would overstate the converted 2015 USD values by roughly 40% (since 1 CAD ≈ 0.72 USD in 1997).
- **Solution:** Applied a two-step conversion in the document: (1) CAD → USD using the 1997 exchange rate (~0.72), then (2) 1997 USD → 2015 USD using the CPI-Medical inflation ratio (~1.90). Showed all arithmetic explicitly with a note that index values are approximate and should be verified against BLS Series CUUR0000SAM.
- **Takeaway:** Always check the currency and dollar-year of cited figures. Canadian and U.S. health economics papers look similar but use different currencies, and the exchange rate matters.

### 2026-03-27: Citation errors found in review essay
- **Context:** Verified all 10 references in `notes/review_essay.md` against primary sources (PubMed, journal websites).
- **Errors found and fixed:**
  1. **Van Houtven et al. (2006) — wrong study/estimate counts.** Essay said "~210 WTP estimates from ~40 studies." PubMed indicates **over 230 estimates from 17 studies**. The "~40" likely came from a Session 5 web search result that confused the number of estimates with the number of studies. Fixed in both `review_essay.md` and `WTP_ER_Visit_Literature.md`.
  2. **Stanford et al. (1999) — wrong issue number and page range.** Essay cited 160(3), 211–216. PubMed lists **160(1), 211–215**. Fixed in the essay bibliography.
- **Not fixed (flagged for review):**
  3. **Smith et al. (1997) — dollar figure ambiguity.** Essay says "~$155 per visit in 1987 dollars." Secondary sources report $290 in 1994 dollars. Both may be correct: the $155 figure comes from BenMAP Appendix H (which we read directly) and likely represents the unadjusted 1987-dollar amount from the underlying NMES survey, while the $290 is the same figure inflated to 1994 dollars as reported in the Smith paper itself. Needs full-text verification to confirm.
  4. **EPA SAB document numbers (2004, 2009).** EPA-SAB-COUNCIL-ADV-04-002 and EPA-SAB-09-012 could not be located via web search. These came from Appendix H which we read directly, so they are likely correct but unverifiable online.
- **Takeaway:** Numbers from web research (especially counts like "40 studies") are prone to drift from secondary sources. Always cross-check against the paper's own abstract on PubMed when available.

### 2026-03-27: Citation errors found in `benmap_theory_comparison.pdf`
- **Context:** Verified all 36 references in `C:\Users\chris\Downloads\benmap_theory_comparison.pdf` against primary sources. No fabricated citations, but five errors found.
- **Errors:**
  1. **Viscusi (2010) — wrong year.** The Handbook of the Economics of Risk and Uncertainty chapter was published in **2014**, not 2010. A related but different *Journal of Risk and Uncertainty* article exists from 2010.
  2. **Fleurbaey & Abi-Rafeh (2016) — wrong journal and pages.** Actually published in *Review of Environmental Economics and Policy* 10(2), 286–307, **not** *Journal of Political Economy* 124(6), 1603–1650. Co-author name is correct.
  3. **Harrington & Portney (1987) — missing from bibliography.** Cited in Section 3.2 text but absent from the references list. Full citation: *Journal of Urban Economics*, 22(1), 101–112.
  4. **Dickie & Gerking (2002) — missing from bibliography.** Cited in Section 3.2 text but no reference entry. Appears to be an unpublished 2002 workshop presentation, not a peer-reviewed article.
  5. **Dionisio, Chang & Baxter (2016) — possible author order error.** May be Dionisio, Baxter & Chang in the actual publication.
- **Takeaway:** Always verify citation metadata (journal, year, pages) against the actual publication, not secondary sources or reference managers. Metadata swaps between entries are a common failure mode.

### 2026-03-28: Source PDF was the wrong paper — twice
- **Context:** User provided `Alberini and Krupnick (2000).pdf` for reading with the /read_pdf skill.
- **Problem (attempt 1):** The PDF actually contained Krupnick et al. (2002), a mortality-risk paper — completely different topic, different authors.
- **Problem (attempt 2):** User replaced the file and re-invoked /read_pdf. After splitting and reading 3 batches, the paper turned out to be Alberini et al. (1997) from *JEEM* — a 7-author precursor study, not the 2-author 2000 *Land Economics* paper. Same research program but wrong paper.
- **How it was caught:** Compared the PDF's title, author list, journal, and year against the expected citation. The 1997 paper has 7 authors (Alberini, Cropper, Fu, Krupnick, Liu, Shaw, Harrington) and was published in *JEEM*; the 2000 paper has 2 authors (Alberini & Krupnick) and was published in *Land Economics*.
- **Resolution:** User downloaded the correct paper from JSTOR on the third attempt. Verified before proceeding: 2 authors, *Land Economics* 76(1), pp. 37-53.
- **Takeaway:** When a source PDF has a filename like "Author (Year).pdf", never trust the filename — always verify the actual title, journal, author list, and year from the PDF content before investing time in a full structured extraction. A quick check of the first split (abstract + introduction) would have caught both mismatches immediately.

### 2026-03-28: Alberini & Krupnick (2000) is behind a paywall
- **Context:** After discovering the source PDF was wrong twice, attempted to find the correct paper online for download.
- **Problem:** The paper is behind paywalls at JSTOR and University of Wisconsin Press. No free full-text PDF available through standard channels (Google Scholar, ResearchGate, author pages).
- **Resolution:** User downloaded it themselves from JSTOR (likely via university library access) and re-invoked /read_pdf.
- **Takeaway:** Many *Land Economics* papers are JSTOR-only. If a paper can't be found freely, provide the user with specific access options (JSTOR Register & Read for 3 free articles, university library proxy, interlibrary loan) rather than continuing to search.

### 2026-03-28: This capstone is about emergency department (ER) visits, not hospital admissions
- **Context:** The review essay compares Stieb et al.'s CAN$5,200 cardiac *hospital admission* figure with BenMAP's $1,161 cardiovascular *ER visit* figure to produce a "roughly six times" ratio.
- **Problem:** Hospital admissions and ER visits are different clinical endpoints with very different severity levels. The 6x ratio conflates two issues: (1) the COI-vs-WTP methodological gap, and (2) a severity difference between admissions and ER visits. This is misleading in a capstone focused on ER visit valuation.
- **Takeaway:** When citing WTP studies, always compare against the same clinical endpoint. Stieb et al. (2002) Table 5 reports ER-specific figures (cardiac ED visit: CAN$4,400; respiratory ED visit: CAN$2,000) that are the correct comparison points for this project. Hospital admission figures should only appear when explicitly discussing the severity gradient, clearly labeled as a different endpoint.

### 2026-03-28: Van Houtven et al. (2006) is a method paper, not a valuation paper
- **Context:** The review essay includes Van Houtven et al. (2006) in its WTP Challenge section (2000-2006). During Session 8, the user asked why this source is in the essay and how it relates to the project goal, since "it talks about creating a function to estimate WTP" rather than providing dollar values like the other sources.
- **Problem:** Van Houtven et al. plays a fundamentally different role than Alberini & Krupnick or Stieb et al. Those papers produce *dollar values* for specific health endpoints (WTP/COI ratios, ED visit valuations). Van Houtven produces *benefit transfer functions* --- regression equations that predict WTP from illness severity and duration. Conflating the two roles can confuse what each source contributes to the capstone.
- **Resolution:** Clarified in the reading notes (Section 9) that Van Houtven serves two distinct purposes: (1) in the review essay, it explains *why EPA could have switched to WTP but didn't* (the benefit-transfer off-ramp existed but was not adopted), and (2) for the valuation calculation, it is less directly useful than Stieb or Alberini & Krupnick because it provides a method for generating values rather than off-the-shelf numbers.
- **Takeaway:** When discussing sources in the capstone, distinguish between *valuation sources* (papers that produce dollar values you can plug into a calculation) and *methodology sources* (papers that develop frameworks or functions). Both matter, but for different reasons. Van Houtven belongs in the policy narrative, not the arithmetic.

### 2026-03-28: Van Houtven's severity-vs-duration asymmetry supports the capstone argument
- **Context:** Van Houtven et al. find that WTP elasticity w.r.t. illness severity (~2.0) is roughly 4x larger than the elasticity w.r.t. duration (~0.5). The QALY approach assumes both are 1.
- **Relevance:** ER visits are high-severity, short-duration events --- exactly the region where the severity elasticity dominates. This means the COI-vs-WTP gap should be *especially* large for ER visits, which is consistent with Stieb et al.'s 3-5x ratios for ED endpoints. This finding provides theoretical backing for the capstone's core argument that COI systematically undervalues ER visits.
- **Takeaway:** When writing the analysis section, cite the asymmetric elasticities as theoretical support for why the WTP/COI gap is large for ER visits specifically, not just for morbidity in general.

### 2026-03-28: Source organization settled — three-act argument structure
- **Context:** Discussed how all non-Chen sources contribute to the capstone goal and how to organize them conceptually.
- **Decision:** Argument-based grouping with three narrative acts plus a standalone calculation section:
  - **Act 1** ("Here's What EPA Does"): BenMAP Appendix H, BenMAP Manual → establishes COI baseline
  - **Act 2** ("Here's What the Economics Shows"): Alberini & Krupnick, Johnson et al., Stieb et al. → quantifies the WTP gap
  - **Act 3** ("Here's Why the Gap Persists"): Van Houtven et al., SAB advisories → explains institutional lock-in
  - **Calculation section** (separate, after Acts 1-3): applies both frameworks to Chen et al.'s EDV counts
- **Key insight:** Stieb et al. (2002) is the **keystone** WTP paper — uses Johnson et al.'s methodology, produces values consistent with Alberini & Krupnick's ratios, backed by Van Houtven's meta-regression.
- **Saved to:** `notes/source_organization.md`

### 2026-03-28: WTP literature research uncovered wildfire-specific studies with much larger COI-WTP gaps
- **Context:** Ran three parallel research agents to find additional WTP papers beyond the existing 2000-2006 sources.
- **Key discovery:** Wildfire-specific WTP studies show the COI-WTP gap is **5-31x** for wildfire smoke symptom days — much larger than the 2-4x from the general morbidity literature. The mechanism: wildfire smoke causes widespread minor symptoms where few seek medical care (COI → ~$0), but nearly everyone takes costly defensive actions.
- **Most important new papers found:**
  1. **Richardson, Champ & Loomis (2013)** — *Land Economics*. WTP $87-95/symptom-day vs COI $3-17/day. California Station Fire 2009. Both revealed and stated preference converge. **Read in full with /read_pdf.**
  2. **Kochi et al. (2012)** — *J Forest Economics*. WTP $84/day vs COI $9.50. 2003 SoCal wildfires.
  3. **Scasny et al. (2024)** — *J Benefit-Cost Analysis*. 7-country asthma WTP, $529/yr adult, 12,727 respondents.
  4. **Robinson, Eber & Hammitt (2022)** — *J Benefit-Cost Analysis*. QALY-to-WTP framework: mild case $5,300, hospitalized $11,000.
  5. **Deschenes, Greenstone & Shapiro (2017)** — *AER*. Revealed preference: defensive pharmaceutical spending >1/3 of total WTP.
- **Meta-findings:** No update to Van Houtven (2006) meta-regression exists. No study directly estimates WTP/COI for ED visits specifically. EPA announced Jan 2026 it will stop quantifying health benefits in air pollution rulemaking.
- **Takeaway:** The general literature's 2-5x COI-WTP gap is a *conservative lower bound* for wildfire smoke specifically. Richardson et al. recommend using 5x as a conservative wildfire-specific calibration factor. This adds a powerful wildfire-specific layer to Act 2 of the capstone argument.

### 2026-03-28: Richardson et al. (2013) — key details for the capstone
- **Context:** Full structured extraction via /read_pdf (25 pages, 7 splits).
- **Core finding:** WTP_DBM = $86.87, WTP_CVM = $95.03, COI_trad = $3.02, COI_comp = $16.87 (all per symptom day, 2009$).
- **Statistical tests:** DBM and CVM are NOT statistically different (combinatorial p = 0.62 — convergent validity). Both WTP values ARE statistically different from both COI values (CIs don't overlap at 90%).
- **Why the ratio is so large for wildfire smoke:** 89% of respondents took defensive actions but only 5% sought medical care. COI captures almost nothing; WTP captures the defensive spending, lost recreation, and disutility that dominate the welfare cost.
- **Method note:** The DBM WTP is based on a single defensive action (home air cleaner, −0.31 marginal effect on symptom days, $26.93 average cost). The endogeneity of air cleaner use is addressed via maximum simulated likelihood (Deb & Trivedi 2006). The CVM uses a log-normal probit on 157 respondents with dichotomous choice bids ($10-$750).
- **Limitation:** WTP values are per symptom day, not per ER visit. Connecting these to BenMAP's per-visit values ($875 respiratory, $1,161 cardiovascular) requires assumptions about symptom days per ER visit.
- **Saved to:** `notes/Richardson_Champ_Loomis_2013.md`

### 2026-03-28: Review essay removed — structural mismatch with project
- **Context:** After removing Alberini & Krupnick (2000) and Johnson et al. (2000) from Act 2 (both moved to `supplementary/`), reassessed whether `notes/review_essay.md` still fit the project.
- **Problem:** The essay was built around a chronological narrative where Alberini & Krupnick and Johnson et al. played central roles in the "WTP Challenge" section. With those sources demoted, the essay's scaffolding no longer matches the project structure. More fundamentally, the essay answers a different question ("how did the field arrive at using COI?") than the capstone ("how much does the COI choice cost us for California wildfire smoke EDVs?"). This is a structural mismatch, not something fixable by editing a few paragraphs.
- **Resolution:** Deleted `notes/review_essay.md`. Will write the capstone paper from scratch using the reading notes as raw material.
- **Takeaway:** When the source lineup changes significantly, check whether existing written products are still structurally sound. An essay organized around sources that are no longer in the main argument can't be patched — it needs to be rebuilt around the sources that remain.

### 2026-03-28: Richardson et al. (2013) role is not yet decided
- **Context:** Richardson et al. was added to `source_organization.md` as a provisional Act 2 source after the WTP literature research in Session 9.
- **Problem:** The source organization treats Richardson et al. as a confirmed Tier 1 source, but the user is still working to understand the paper and hasn't decided whether it belongs in the main argument.
- **Resolution:** Noted the provisional status. The source organization includes Richardson et al. but its role should not be assumed settled until explicitly confirmed.
- **Takeaway:** Don't build argument structure around a source the user hasn't finished evaluating. Mark provisional sources clearly and wait for confirmation before treating them as load-bearing.

### 2026-03-29: Essay outline created and revised (`paper/essay_outline.md`)
- **Context:** Created an eight-section chronological literature review outline with a calculation section. Then revised it through several rounds of structural editing.
- **Revisions made:**
  1. **Section III.A reframed:** Title changed from "The innovation: adding components, not multiplying" to "What costs does COI leave out?" The original framing emphasized double-counting avoidance, but Stieb et al. don't discuss double-counting in the paper — their argument is about comprehensiveness (COI misses pain, suffering, and defensive costs). The outline was attributing an argument to the paper that the authors don't make.
  2. **Hospital admission comparison moved from Section III to Section IV.C:** The comparison between ED visit ratios (1.9x) and hospital admission ratios (1.3x) was in Section III, but since the capstone is about ED visits specifically, the comparison only earns its place in Section IV where Van Houtven's elasticity asymmetry explains *why* the ratio differs. Section III now focuses purely on ED-specific findings.
  3. **All subsection titles rewritten as questions:** Labels like "ED-specific results" and "The endpoint-matching problem" were unclear about what the subsection would discuss. Replaced with questions like "How large is the gap for ED visits?" and "Can we compare these values directly to BenMAP's?"
  4. **Sections III, IV, and V split into two groups:** Each section mixes "what the paper found" with "what this means for the capstone." Added **The findings** and **Implications for the capstone** group labels to make the two-part structure visible.
  5. **All bullet points rewritten as writing instructions:** Bullets were originally reference notes (data points to look up). Rewritten in claim → evidence → connection format so each bullet tells the writer what to argue, what evidence to cite, and why it matters for the section's argument.
- **Takeaway:** Outline bullets should be writing instructions (what to argue), not reference notes (what data exists). The distinction matters because a data point doesn't tell the writer what claim to make or why it matters — it just sits there. A writing instruction tells the writer what to do with the data.

### 2026-03-29: WTP_ER_Visit_Literature.md moved to supplementary
- **Context:** `notes/WTP_ER_Visit_Literature.md` was written during Session 5 around Alberini & Krupnick and Johnson et al., both of which were demoted to supplementary in Session 10.
- **Resolution:** Moved to `supplementary/WTP_ER_Visit_Literature.md`. The WTP evidence that matters for the main argument now lives in the individual reading notes for Stieb et al. and Richardson et al.

### 2026-03-29: Three-agent comparison of Stieb et al. and Chen et al.
- **Context:** Ran three parallel agents to compare Stieb (valuation) and Chen (health burden) — one summarizing each paper, one identifying agreements/divergences/gaps.
- **Key findings:**
  1. **Strongest connection:** Chen's "all respiratory" (4,597 EDVs) maps cleanly onto Stieb's REDV (CAN$2,000); Chen's "all cardiovascular" (889 EDVs) maps onto Stieb's CEDV (CAN$4,400). Subcategory mapping is weaker.
  2. **Preliminary calculation:** COI total ~$5.05M vs. Stieb-based WTP total ~$17.93M (ratio ~3.6x).
  3. **8 of Chen's 19 endpoints have no Stieb valuation:** cerebrovascular, PVD, TIA, diabetes, and all 5 mental health categories.
  4. **Composition mismatch:** Chen's respiratory EDVs are ~26% asthma/COPD vs. Stieb's 44% assumption — slightly overvalues respiratory when applying Stieb's REDV.
  5. **Lag mismatch is not a problem:** Stieb's framework is atemporal; the dollar value of a cardiac ED visit is the same whether it occurs at lag 0 or lag 10.
- **Takeaway:** The capstone calculation should stay at the aggregate respiratory/cardiovascular level and flag the unvalued residual (mental health, metabolic endpoints) honestly.

### 2026-03-29: Source relevance scoring and cross-source comparison
- **Context:** Created `notes/auto-review/` directory with two reference files for writing.
- **Files created:**
  1. `relevance_scores.md` — 1-5 scoring of all 5 primary sources against the capstone question. BenMAP Appendix H and Chen et al. scored 5 (essential/irreplaceable). Stieb and Richardson scored 4 (important but substitutable). Van Houtven scored 3 (supporting — adds theoretical depth but changes no numbers).
  2. `cross_source_comparison.md` — Comparison table, 4 agreements, 4 tensions, 6 gaps, and full intellectual lineage. Most consequential gap: no source provides WTP specifically for wildfire smoke ER visits (Stieb has ED visits but not wildfire-specific; Richardson has wildfire-specific but not ED visits). Most consequential tension: the WTP/COI multiplier ranges from 1.3x (Stieb) to 31x (Richardson) depending on endpoint and COI denominator.
- **Takeaway:** The Johnson et al. (2000) survey is the connective tissue — it feeds directly into Stieb's applied valuations AND is the largest single source (67/236 estimates) in Van Houtven's meta-analysis. This makes the WTP evidence less independent than it first appears, worth acknowledging as a limitation.

### 2026-03-30: Verify before answering — don't guess from memory
- **Context:** Chris asked where Chen et al. got their health impact function. I answered from memory (saying it's a standard formula with no citation) before reading the paper to check.
- **Problem:** Chris had to ask me to read the paper, which was the whole point of the question — to find out whether a citation exists by looking, not guessing.
- **Resolution:** Read the full Chen paper, confirmed no citation. Then read BenMAP Appendix C and found the matching derivation.
- **Takeaway:** When Chris asks a factual question about a source, read the source first, then answer. Don't answer from memory and then verify — verify first.

### 2026-03-30: Full PDFs under ~15 pages can be read directly
- **Context:** The `pdftoppm` PDF renderer fails on this Windows machine, so reading PDFs with the `pages` parameter doesn't work. The split PDFs from `/read_pdf` were deleted during the session cleanup.
- **Problem:** Needed to read Chen et al. (11 pages) and BenMAP Appendix C (12 pages) without split files or the `pages` parameter.
- **Resolution:** Reading the full PDF with the Read tool (no `pages` parameter) works fine for papers under ~15 pages. Both PDFs rendered successfully.
- **Takeaway:** For short papers (under ~15 pages), read the full PDF directly. Only use `/read_pdf` splitting for longer papers where the full content would overwhelm context.
