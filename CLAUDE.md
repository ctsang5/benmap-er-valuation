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
