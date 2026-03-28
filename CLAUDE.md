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

### 2026-03-27: Citation errors found in `benmap_theory_comparison.pdf`
- **Context:** Verified all 36 references in `C:\Users\chris\Downloads\benmap_theory_comparison.pdf` against primary sources. No fabricated citations, but five errors found.
- **Errors:**
  1. **Viscusi (2010) — wrong year.** The Handbook of the Economics of Risk and Uncertainty chapter was published in **2014**, not 2010. A related but different *Journal of Risk and Uncertainty* article exists from 2010.
  2. **Fleurbaey & Abi-Rafeh (2016) — wrong journal and pages.** Actually published in *Review of Environmental Economics and Policy* 10(2), 286–307, **not** *Journal of Political Economy* 124(6), 1603–1650. Co-author name is correct.
  3. **Harrington & Portney (1987) — missing from bibliography.** Cited in Section 3.2 text but absent from the references list. Full citation: *Journal of Urban Economics*, 22(1), 101–112.
  4. **Dickie & Gerking (2002) — missing from bibliography.** Cited in Section 3.2 text but no reference entry. Appears to be an unpublished 2002 workshop presentation, not a peer-reviewed article.
  5. **Dionisio, Chang & Baxter (2016) — possible author order error.** May be Dionisio, Baxter & Chang in the actual publication.
- **Takeaway:** Always verify citation metadata (journal, year, pages) against the actual publication, not secondary sources or reference managers. Metadata swaps between entries are a common failure mode.
