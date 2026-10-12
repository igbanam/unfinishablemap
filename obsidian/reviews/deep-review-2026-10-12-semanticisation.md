---
title: "Deep Review - Semanticisation"
created: 2026-10-12
modified: 2026-10-12
human_modified: null
ai_modified: 2026-10-12T13:55:55+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-12
last_curated: null
---

**Date**: 2026-10-12
**Article**: [[semanticisation|Semanticisation]]
**Previous review**: [[deep-review-2026-09-02-semanticisation|2026-09-02]]

## Selection Note

The selector's top candidate (`topics/q3-q4-sliding-boundary-and-transparency-problem`) was on the driver's edited-today list. The runner-up (`topics/pupillometry-behavioural-channel`, 5 prior reviews) had changed since its 2026-07-24 review only through today's check-links anchor fix, which is a cosmetic bump on a converged article. `arguments/epiphenomenalism-argument` (6 prior reviews; post-review edits were a roster fix and the topics field) tied with this article at 62. This article was chosen because it has only ONE prior review, and a substantive refine-draft fold (`11c59e7618`, 2026-09-02 18:53Z) landed about 5.5 h AFTER that review. The fold added 10 citations, 3 verbatim quotes and the falsifier-design paragraph, and none of it had ever been reviewed. Its source note (`research/diary-and-reinstatement-phenomenology-tracking-2026-09-02`) said explicitly that "publisher-grep verification [is] owed before any quote moves into an article". This pass pays that debt.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Dropped qualifier — Frankenberg et al. 2022** (L56): the article said Frankenberg "watched the same healthy participants shift from specific toward general memories across a decade". The abstract (Europe PMC, PMID 33402012) restricts the effect: "age-related semantization effects with a significantly lower number of specific and thereby a higher number of general AMs **exclusively from young-old to old age**". The study followed two cohorts (baseline ages ~55 and ~74, re-examined after 9 ± 0.9 years), and only the older one showed the shift. The authors frame it as an ageing effect ("AM changes in healthy aging accelerate during the transition from young-old to old age"). The restriction matters for the article's use: the shift is not a general time-since-encoding finding. Fixed: "following two healthy cohorts for a decade, saw specific memories give way to general ones only in the older—as narrative category counts, not felt re-experiencing."
- **Lead omitted adverse evidence the fold added** (L32): after the fold, the body reports Talarico & Rubin's everyday-memory recollection and vividness declining by degrees ("the falsifier's adverse direction, at the report level, access uncontrolled"). The lead still summarised only the favourable evidence (discreteness, the access reading). A truncating LLM reader would get a one-sided ledger. A tenet-accepting reviewer would flag this, so it is a calibration defect, not a bedrock disagreement. Fixed by inserting "(report-level fading is recorded, access uncontrolled)" after "has not been made". Per the 2026-09-02 stability note, the "strongest phenomenal evidence … points toward discreteness" clause and the section header were NOT touched; this pass adds the missing adverse item and changes nothing else.

### Medium Issues Found

- **Dangling reference — "the August survey"** (L56): the fold removed the sentence that introduced the August 2026 OpenAlex/Crossref/Europe PMC survey but kept "the vocabularies the August survey named as its ceiling". No antecedent existed anywhere in the article (grep: L56 was the only "August"). Rewritten as "a September 2026 search beyond semanticisation vocabulary" (−8 words). "Each half" and "a higher stated ceiling" still read correctly against the implied earlier search.
- **Question-begging premise — Willander & Larsson** (L70): the odour-cued memories were described as "the oldest, least-rehearsed, most thoroughly semanticised memories a person has". The source supports "oldest" ("most odor-cued memories were located to the first decade of life") and "least-rehearsed" ("had been thought of less often"). "Most thoroughly semanticised" is the transformation reading's premise, which the paragraph is arguing against. Moved into the conditional: "On the transformation reading, memories that old are the most semanticised, with the least re-experiencing left to give". The access-reading contrast is unchanged.
- **Ambiguity misreadable as longitudinal — Coane et al. 2022** (L58): the fold changed "spanning twelve years" to "across twelve years". Per the abstract, participants rated "events occurring over the previous 12 years", a cross-sectional design. "Across twelve years" can read as a 12-year follow-up, in an article whose central claim is that no within-memory longitudinal phenomenology study exists. Restored "spanning" (word-neutral).
- **Revision narration** (L70 "and now in quantitative form"; L72 "which can now be specified"): the "now" refers to the article's own pre-fold state, which is meaningless to a fresh reader. Cut (−3 words, which paid for the critical fixes).

### Counterarguments Considered

- *The flashbulb dissociation is equally at home on a functionalist reading* (reported reliving as a metacognitive confidence signal; Talarico & Rubin themselves gloss it as *perceived* accuracy). The research note flagged this ("the dissociation constrains, it does not decide"), and the fold did not carry the sentence across. Considered and left unchanged. The article calls the finding "the manner/content independence the Map argues from", which identifies a premise and does not claim a verdict. The paragraph closes with "the serious live countermodel stands at the level of interpretation", and L44 already routes functionalist re-readings to the Map's standing reply. With 10 words of headroom, adding the counter-reading would mean cutting calibration text of equal weight. Recorded here so a future pass with headroom can add one clause.
- *The access reading is called "the one the empirical record most directly supports" (L68) yet "still resting on a small evidence base" (L72).* These are not contradictory: the claim is comparative among three readings, and the small base is stated. The sentence was unchanged by the fold and preserved by the prior review, so it is not re-flagged.

## §2.4 Publisher-of-Record Citation Ledger

**Scope:** the 10 citations and 3 quotes added by the post-review fold, plus Coane 2022, whose sentence the fold reworded. The 19 citations verified on 2026-09-02 (Crossref, plus Europe PMC and the Gentry & Buckner full-text XML for quotes) were not re-fetched because their sentences changed only in trims. Metadata comes from raw Crossref JSON (`api.crossref.org/works/{doi}`). Quotes were grepped against raw abstract text: the Crossref-carried abstract where present, otherwise the Europe PMC `resultType=core` abstract, otherwise the OpenAlex inverted index for Conway.

- Berntsen & Hall 2004 (The episodic nature of involuntary autobiographical memories) — state: real-correct (Mem Cogn 32(5): 789–803). Quote "the way autobiographical memories are sampled greatly affects the findings" verbatim (Europe PMC, PMID 15552356). The comparison really is "voluntary word-cued memories" (Study 1), and specificity, physical reaction and mood impact all hold in the stated direction.
- Conway, Gardiner, Perfect, Anderson & Cohen 1997 (Changes in memory awareness during learning) — state: real-correct (JEP:General 126(4): 393–413). This resolves the research note's open pagination flag (Crossref page 393–413). The abstract (OpenAlex) reports "a shift from remembering to knowing … an underlying shift in knowledge representation from episodic to semantic memory", which supports "tracks semanticisation directly".
- Dewhurst, Conway & Brandt 2009 (Tracking the R-to-K shift) — state: real-correct (ACP 23(6): 849–858; online 2008, print 2009, matching the article's print-year convention). Tests ran at 5 min, 4 wk, 8 wk and 6 months; remember responses fell and know responses rose.
- Frankenberg, Knebel, Degen, Siebert, Wahl & Schröder 2022 (Autobiographical memory in healthy aging) — state: real-correct metadata (ANC 29(1): 158–179; online 2021, print 2022); **qualifier dropped in body — fixed** (see Critical).
- Frinco, Muzzulini, Tinti, Luminet & Schmidt 2024 (A review of longitudinal studies on flashbulb memories) — state: real-correct (ACP 38(4), article e4233). "57 test–retest studies on FBMs for public events" matches "fifty-seven test–retest studies of memory for public events". The entry lacks the article number e4233 (optional completion, not an error).
- Marcotti & St. Jacques 2018 (Shifting visual perspective during memory retrieval) — state: real-correct (Memory 26(3): 330–341; online 2017, print 2018). The abstract supports the paraphrase: shifting "reduced the accuracy of subsequent memories" and "reductions in vividness when shifting visual perspective during retrieval predicted these changes in the accuracy of memories". Note: the events were lab-encoded "mini-events"; the article claims nothing broader.
- Talarico & Rubin 2003 (Confidence, not consistency, characterizes flashbulb memories) — state: real-correct (Psych Sci 14(5): 455–461). Quote "Flashbulb memories are not special in their accuracy, as previously claimed, but only in their perceived accuracy" verbatim (Crossref-carried abstract). Delays were 1, 6 or 32 weeks. Consistency declined for both memory types, while vividness, recollection and belief declined "only for everyday memories", matching the article's direction.
- Talarico & Rubin 2007 (Flashbulb memories are special after all) — state: real-correct (ACP 21(5): 557–578; online 2006, print 2007). Its abstract's "declining over the following year" supports the article's "at delays up to a year". The 2003 paper alone reaches only 32 weeks, so the joint "(2003; 2007)" cite carries the claim.
- Thomsen, Jensen, Holm, Olesen, Schnieber & Tønnesvang 2015 (A 3.5 year diary study) — state: real-correct (Conscious Cogn 36: 180–195). Reliving was measured once at the 3.5-year follow-up (Europe PMC, PMID 26164104), which matches "rated reliving once, at a 3.5-year follow-up". Weekly diary ratings support "sampling at encoding by diary".
- Willander & Larsson 2006 (Smell your way back to childhood) — state: real-correct (PBR 13(2): 240–244). "brought back in time" verbatim; "first decade of life" and "thought of less often" also verbatim (Europe PMC, PMID 16892988). Premise placement fixed (see Medium).
- Coane, Umanath, Cimenian & Chang 2022 (Using the phenomenology of memory for recent events) — state: real-correct (Mem Cogn 50(3): 495–511). The design is cross-sectional ("events occurring over the previous 12 years"); "spanning" restored (see Medium). "Equal in terms of subjective strength" and the unprompted definitions finding both hold.

**Inline ↔ References, both directions:** every (surname, year) pair in References has an inline hit and every inline cite has an entry (scripted check; the Southgate self-cites are intentional and wikilinked). No orphans.

**Coiner checks:** Tulving 1985 coined "autonoetic"/"noetic" ✓. "Repisodic" is credited to Neisser, inside Gentry & Buckner's instancing ✓. The R-to-K shift is from Conway et al. 1997 ✓. SDAM is from Palombo et al. 2015 ✓. "Personal semantics" and "trace transformation" are cited to representative statements and no coinage is claimed ✓.

**Empirical-currency sweep:** `find_superlative_claims` returned no candidates.

**Cited-author stance:** Talarico & Rubin frame their dissociation as *perceived* accuracy, and the article presents the manner/content reading as the Map's ("the independence the Map argues from"), not theirs ✓. Folville's quote is "close to the Map's thesis", not endorsement of it ✓. For Willander & Larsson the access gloss is marked "on the access reading" ✓. Gentry & Buckner, De Brigard and Cheng are correctly placed as opponents or non-allies ✓.

## Reasoning-Mode Classification (changelog-internal record)

Unchanged from 2026-09-02. For Gentry & Buckner: Mode One with an honest boundary residue (error theory argued by citation, not measurement). For De Brigard: Mode One (Zaman 2024 answers the construct-validity limb) mixed with honest concession (SDAM "serves the other side"). Label-leakage grep returned 0 hits.

## Optimistic Analysis Summary

### Strengths Preserved (unchanged)

- The three-verdict calibration split in Relation to Site Perspective.
- "A claim of that strength owes the world a way of losing" (L44).
- Reporting the everyday-fade limb and the flashbulb-dissociation limb from the same dataset together, "the falsifier's adverse direction, at the report level, access uncontrolled". This is exemplary evidential honesty. The fold got it right in the body, and this pass carries it into the lead.
- The falsifier-design paragraph: the R/K "categorical by construction" point (a graded fade and a discrete flip yield identical R/K data), the retrieval-alters-the-object confound, and the transformation-vs-access sort by reinstatement probe. All components are verified as published (ledger above).
- "The Map's sharpest available test is unrun—with an instrument that exists."

### Enhancements Made

- The lead now front-loads the adverse report-level evidence.
- The Frankenberg qualifier was restored, the Coane design-scope ambiguity removed, and the Willander premise moved into the reading it belongs to.
- The research note's two open verification flags are resolved: Conway 1997 pagination is confirmed 393–413, and all three fold quotes are grep-verified in raw abstract text.

### Cross-links Added

None. The article is at the length gate and its link set is complete; the outbound claim about [[consciousness-and-memory]] L140 ("the time course beneath it is not a smooth decay") was verified as present.

## Length

`analyze_length`: 3489 → 3489 (net 0), status soft_warning, concepts hard threshold 3500 (gate `>=`, headroom 10). The additions were lead +5 (6 added, "actually" dropped), Frankenberg +4 and Willander +1. They were paid for by the dangling-reference rewrite (−8) and the revision-narration cuts (−3). The hand tally is −1; `analyze_length` strips markup and reports 0. Raw split of the current text: prose ~2665, Further Reading ~44, References ~806. The soft_warning comes mostly from reference apparatus (31 entries), not prose.

## Remaining Items

- Optional: add the article number e4233 to the Frinco et al. 2024 References entry (+1 word; not an error).
- Optional, when headroom allows: one clause noting that the flashbulb dissociation also fits a metacognitive-confidence reading (see Counterarguments).

## Stability Notes

- All 2026-09-02 stability notes still hold: the gradation camp is bedrock; the discreteness header stands with its two cautions; "unrefuted and untested" must not be upgraded.
- NEW: the lead's parenthesis "(report-level fading is recorded, access uncontrolled)" is the calibration counterweight to the discreteness clause. Do not remove it unless the body's Talarico & Rubin everyday-fade report is removed too.
- NEW: Frankenberg 2022's shift is older-cohort-only and age-framed by its authors. Do not restore "the same healthy participants … across a decade" without the restriction.
- The fold's 10 citations and 3 quotes are now publisher-verified (ledger above). Future passes need not re-fetch them unless the sentences change.
