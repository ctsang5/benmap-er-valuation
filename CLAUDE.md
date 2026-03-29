# CLAUDE.md - Capstone Project

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
- **Solution:** Ran three parallel verification agents to confirm exact citations, authorship, journal, and dollar figures against primary sources before writing the document. Correctly attributed all figures in `WTP_ER_Visit_Literature.md`.
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
