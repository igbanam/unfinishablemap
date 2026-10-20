---
title: "Deep Review - Ontic Structural Realism"
created: 2026-10-20
modified: 2026-10-20
human_modified:
ai_modified: 2026-10-20T17:47:28+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-20
last_curated:
---

**Date**: 2026-10-20
**Article**: [[ontic-structural-realism|Ontic Structural Realism]]
**Previous review**: [[deep-review-2026-09-05-ontic-structural-realism|2026-09-05]] (plus the reciprocal-wiring [[cross-review-2026-09-06-ontic-structural-realism|cross-review of 2026-09-06]], which did not edit the article)

**Selection note.** The selector's top pick was `topics/agent-causation-and-acting-for-reasons` (score 100, created today). It was skipped because its own queued P2 cross-review already asks for a full deep-review pass, so running one here would duplicate that task. This article was the next candidate (score 69).

**Scope.** The article changed after the 09-05 review in four commits: the 09-07 refine-draft rewrite of §constructed-rival (new Lyre, Kleiner, Fink & Lee and Chalmers material), the 09-08 Newman DOI, the 10-12 mad-dog parallel at L79, and the 10-13 structuralism link at L97. The 09-05 ledger's raw-grep certifications for refs 1–21 stand and were not repeated, apart from spot re-greps of Loorits, Lyre and Unger. This pass worked on the new material.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **A false universal negative, contradicted by the article's own primary source.** Three loci asserted that no OSR theorist carries the thesis across to experience: L37 ("no OSR theorist carries the thesis across to experience"; "only the joining is unpublished"), L51 ("no OSR theorist carries the physics thesis across to experience"), and L105 ("the join to OSR about physics remains nobody's published project"). L59 also called Beni (2026) "the likeliest candidate" for having staged the join. Ladyman's own SEP entry, the source of the article's census, names the counterexample in its prose: "Tegmark (2008) explicitly embraces a Pythagorean form of OSR" (raw-grep, 1 hit). Tegmark's paper (arXiv 0704.0646, raw-grep) places the MUH in "the 'ontic' version of universal structural realism". It treats observers as "self-aware substructures" (the frog "itself must be merely a thick bundle of pasta"). It holds that "the subjective perceptions of SAS's" could in principle be derived by "an infinitely intelligent mathematician". The same text has "experience" 0 hits, "qualia" 0 and "conscious" 3, all in passing. So Tegmark asserts the join in outline and never argues it for phenomenal character. **Resolution**: L37 now says the joining is "published only in outline" and names Tegmark as an OSR theorist who carries the thesis to observers by assertion. L51 names Tegmark, cited through the SEP's own sentence. L59 says the join is "sketched by Tegmark but not argued", rescopes the Beni question to whether anyone has *argued* the join for phenomenal character, and changes "five" to "six". L105 records the falsifier as "mostly failed". Reference 25 was appended, and Tegmark was added to the sourcing-gaps paragraph (arXiv text only; later consciousness papers unread). The census itself is untouched and was re-verified: the 170,502-character extraction matches "roughly 170,000", and the revision date of 18 May 2023 matches.

### Medium Issues Found

2. **Fink & Lee gloss slightly overstated (source fidelity).** L57 read "the 2025 … volume on structuralism in consciousness science — whose "ontic structuralists" hold "that all there is to consciousness is structure"". That makes the ontic structuralists the volume's own. The raw galley (12733 → 12419) has the phrase as a taxonomic example: "there are many varieties of structuralism. As examples, methodological structuralists think …, while ontic structuralists think that all there is to consciousness is structure". **Resolution**: now "Fink and Lee count "ontic structuralists", who think "that all there is to consciousness is structure", among structuralism's varieties". The sibling page `structuralism-about-phenomenal-character` L44 already read it correctly.
3. **Page-history narration in article prose.** The 09-07 rewrite left six phrases about the page's own past: "an earlier version of this page said otherwise" (in the lead), "the other half was misread here, and the misreading ran against the Map's own interest", "the distinction this page had supposed undrawn", "the two overstatements this page has been near", "narrower than this page once claimed", and "What the page can no longer say". These cost words, give an LLM reader nothing it can use, and age badly (writing-style "Relative terms … age poorly"). **Resolution**: five were restated as present-tense claims, and the L57 framing sentence was cut as redundant with that paragraph's closing line. The record of the retraction stays where it belongs, in "What Would Change This View" ("has been tested since this page was written and mostly failed").

### Publisher-of-Record Citation Ledger (§2.4) — this pass

Raw artefacts were fetched with curl and grepped in Python. No summariser was used to confirm any quotation.

- Lyre 2022, *Neurosci. Conscious.* niac012 (Europe PMC PMC9396309 XML) — **real-correct**. All nine quoted spans are verbatim, including the 09-07 additions: "family resemblance … place in a Q-structure", "realism about the phenomenal", "the Q-structure plays no causal role at all", "consistent with a reduction of the phenomenal to the neural". Reading-check: "The short answer is: no" is followed immediately by "In particular, neurophenomenal structuralism is no realism about the phenomenal". After the definitional paragraph comes the family-resemblance admission, then mirroring and exclusion, then "Therefore … no realism about the phenomenal (be it structural or otherwise)". The article's account (declines the SR label, holds a reductive view) fits the passage.
- Loorits 2014, *Front. Psychol.* 5:237 (PMC3957492 XML) — **real-correct**. All four quotes are verbatim. Author-stance check: "Loorits asserts the metaphysics outright" is supported by his "A fully structural account (in the sense that it does not contain any irreducibly non-structural elements) of consciousness and qualia". The "small minority" line is about "scientific object structuralism", as the article says.
- Kleiner 2025, *PhiMiSci* 6, DOI 10.33735/phimisci.2025.11827 — **real-correct**. The EPSR/OPSR definition is verbatim in galley 12403 (reading-order extraction). It is introduced as "Following terminology of philosophy of science, we might designate …", which supports "coins the taxonomy". A web search for the two labels found no earlier use. Crossref `issued` is 2026-01-30, but the publisher's `citation_date` is 2025, vol. 6. The publisher form is canonical (same pattern as Esfeld & Lam in the 09-05 ledger).
- Fink & Lee 2025, *PhiMiSci* 6, DOI 10.33735/phimisci.2025.12733 — **real-correct** metadata (title "Structuralism in the science of consciousness. Editorial introduction"; Sascha Benjamin Fink, Andrew Y. Lee; Crossref `issued` 2026-02-09, publisher 2025). Both quotes are verbatim. The gloss was corrected (Medium 2).
- Chalmers 2012, "Phenomenal structuralism", *Constructing the World* pp. 412–422 — **real-correct (secondhand)**. Confirmed in Fink & Lee's reference list (raw galley) and independently by the PhilArchive section record (pp. 412–422). The consc.net TOC lists chapters only. A 2012 Chalmers seminar syllabus assigns ch. 8 "especially 8.7", which fits a late-chapter section. The article already marks it as unread.
- Tegmark 2008, *Foundations of Physics* 38(2) 101–150, DOI 10.1007/s10701-007-9186-9 — **added** (Crossref-verified; print Feb 2008, online Nov 2007). Quotes "self-aware substructures" and "subjective perceptions" are verbatim in arXiv 0704.0646.
- Ladyman 2023, SEP *Structural Realism* — **real-correct**, re-fetched. "Tegmark (2008) explicitly embraces a Pythagorean form of OSR" and the Unger sentence are verbatim. Counts are unchanged: consciousness 0, conscious 0, experience 0, qualia 1.
- Newman 1928 DOI (added 09-08) — not re-litigated. The 09-08 refine-draft verified it.
- Refs 1–21 otherwise — carried from the 09-05 ledger (raw-grep-verified then).

**Empirical-record currency sweep**: none needed. The article makes no superlative or record claims beyond its own census, which was re-measured exactly.

**Result-direction leg**: no empirical results are cited.

**Cited-author-stance leg**:
- Lyre: reductive physicalist; declines realism about the phenomenal. Not presented as an ally.
- Loorits: anti-dualist structuralist ("the threat of dualism can be avoided"). Presented as an opponent.
- Kleiner: coins OPSR without declaring for it. The article says so.
- Tegmark: physicalist mathematical monist. Presented as the sketcher of the rival, not as an ally.
- Stanciu: cited as an ally only for an epistemic framing, not for dualism. Unchanged.
- Chalmers: "more generous to this rival than the Map". Unchanged.

### Counterarguments Considered

- *Quantum Skeptic (Tegmark)*: "Your rival is not a construction; I published it." This produced Critical 1. It is correct about the join in outline and wrong about the phenomenal half, which his 2008 paper does not argue. The article now says exactly that.
- *Eliminative Materialist / Hard-Nosed Physicalist*: Loorits's debunking of apparent monadicity is the Dennettian move. The article already concedes "The dispute is open inside the structuralist's framework, not closed by the Map". This is bedrock (see the 09-05 stability notes) and was not re-flagged.
- *Many-Worlds Defender*: the indexical line in the No Many Worlds paragraph is already flagged as the Map's own, with the "indexicality may itself be structural" caution. Tegmark's MUH, which joins OSR to a multiverse, would make the line's target concrete. Noted as an expansion opportunity and not taken (see Remaining Items).
- *Empiricist*: falsifiers are explicit, and the new Tegmark finding was booked as a partial falsification of a stated claim. That is the section working as designed.
- *Buddhist Philosopher*: OSR's denial of intrinsic natures parallels Madhyamaka's denial of svabhāva, and the Map's acquaintance claim posits exactly one svabhāva. This is bedrock and was not added (length).

### Calibration and Method/History Audit

- No possibility/probability slippage. The defeater-removal booking ("losing it costs a defeater-removal rather than a premise") is correct, and the Tegmark addition upgrades nothing.
- Method/history necessity check on §relocate-abolish: "physics works without secondary qualities because it was built not to need them" is attributed to the galilean-exclusion page (*Map reconstruction*). The Galileo-relocates reading is attributed to SEP Bolton (*contested historiography*, labelled as SEP's reading). No origin ⇒ validity inference is drawn; the article uses the history only to sharpen a contrast, and it says the relocation reading "complicates" its sibling's gloss.

### Reasoning-Mode Classification (editor-internal)

- Tegmark: Mode Three. The article names his sketch as the rival in outline and refutes nothing.
- Lyre: Mode One, unchanged from 09-07. His own family-resemblance admission and exclusion argument defeat the earlier misuse of his disavowal.
- Kleiner: Mode Three, unchanged.
- Newman engagement against OSR: still marked "a reply rather than a refutation". Correct.
- No editor vocabulary leaks into prose (grep of the forbidden-label list returns 0).

## Optimistic Analysis Summary

### Strengths Preserved

- The route/conclusion separation in the lead and §what-is-lost. It is the article's central calibration and is untouched.
- The census paragraph, now carrying one more fact taken from its own source.
- The Lyre reading installed on 09-07, checked against raw text and accurate.
- The Chalmers calibration point: "The Map should not be more confident against a position than the philosopher whose argument it borrows".
- "What Would Change This View, and What Went Unread". The Tegmark finding landed there as a recorded partial falsification, which is the section doing its job.

### Enhancements Made

- The Tegmark correction (Critical 1) also improves the dialectic: the rival now has a published sketch, and the open question narrows to whether anyone has *argued* the join for phenomenal character.

### Cross-links Added

None. All wikilinks resolve. `#constructed-rival`, `#what-is-lost`, `#newman` and `#the-choice` are intact.

## Word Count

`analyze_length`: 3301 → 3350 (+49), concepts 2500/3500/5000, `soft_warning` before and after, 150 under hard. The Tegmark correction plus its reference and sourcing-gap note added about 100 words. Removing page-history narration and the redundant L57 framing sentence recovered about 50.

## Remaining Items

- **Tegmark and the No Many Worlds paragraph.** The MUH entails a Level IV multiverse ("In the context of the MUH, the existence of the Level IV multiverse is not optional", verbatim) and joins OSR to many-worlds. That would make the indexical line's "structuralism generally, not only many-worlds" concrete. Not taken: the article is 150 words under hard, and the line is flagged as the Map's own and still speculative.
- **Tegmark 2015 ("Consciousness as a state of matter") unread.** If it argues structure-only about experience, the article's "no source consulted here argues it for phenomenal character" would need revisiting.
- **Brüntrup (2011), "Panpsychism and Structural Realism"** (in Blamauer ed., *The Mental as Fundamental*), is cited in Kleiner's reference list. It is the likeliest place where a panpsychist meets OSR directly. Unread.
- Carried forward from 09-05: Ladyman & Ross (2007) unread, Beni (2026) abstract-only.

## Stability Notes

- **The two-literature framing is now settled at three positions, and future passes should not re-open it.** (a) The OSR literature is silent on experience, with Tegmark's outline sketch as the one crossing named in Ladyman's survey. (b) The ontic claim about phenomenal character is held in print (Loorits) and named (Kleiner). (c) Nobody consulted argues the full composite for phenomenal character. Re-flag only if a new source moves one of (a)–(c).
- **The page-history narration was removed deliberately, not as a stylistic preference to oscillate on.** The retraction record lives in "What Would Change This View". Do not re-insert "an earlier version of this page" phrasing in the lead or body.
- **Length.** 520 of the 3350 words are reference apparatus (Further Reading plus 25 references), leaving 2853 words of body prose, as the 09-05 stability note anticipated. Do not condense on the strength of `soft_warning` alone.
- Bedrock disagreements from 09-05 (eliminativist, physicalist and MWI objections at the framework boundary) remain bedrock and were not re-flagged.
