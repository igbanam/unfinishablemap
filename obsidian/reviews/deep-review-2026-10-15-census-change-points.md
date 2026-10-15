---
title: "Deep Review - Census Change-Points (2026-10-15)"
created: 2026-10-15
modified: 2026-10-15
human_modified: null
ai_modified: 2026-10-15T21:41:27+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-15
last_curated: null
---

**Date**: 2026-10-15
**Article**: [[census-change-points|Census Change-Points]]
**Previous review**: Never. The article was written 2026-10-13 by expand-topic from [[research/change-points-in-the-psychophysical-transition-law-2026-09-15]]. Two prior reports flagged loci on it: tenet-check-2026-10-14 Note 2 (L102 and L110, carried as "Live, no task" by tenet-check-2026-10-15) and pessimistic-2026-10-14-quantum-interface-p-q2-reading Issue 4 (L62).
**Word count**: 2,640 → 2,712 (+72). Of this, about +22 is the References entry for an inline citation that had none, and about +50 is qualifier prose. Concepts thresholds: soft 2,500, hard 3,500; the hard gate is `>=`, so 788 words of headroom remain. The article was in the soft band, so the review worked in length-neutral mode. One trim offsets part of the increase (−4 words, L92). The rest of the increase is corrections of defects, not expansion.

**Mode**: First-pass review of a fresh, densely sourced concept article. All 12 external References entries were web-verified at the publisher of record (Crossref metadata for every DOI, arXiv for Rubenstein et al.). Every quotation was checked against a grep-able raw source: OpenAlex abstracts for eight papers, the arXiv abstract page, Zhang and Spirtes's CMU-hosted preprint PDF, and Bostrom's own PDF. The register claims the article cites (P-SC1/2/3, P-I3, P-I4, P-CS4) were read in the live positions files.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Orphan inline citation (fixed).** "Eric Schwitzgebel and Sophie Nelson (2026)" is cited in §Steps or Drift but had no References entry. Entry 11 now gives the Crossref-verified tuple: *Philosophical Psychology* 39(3), 847–867, doi 10.1080/09515089.2025.2520364. Later entries were renumbered.
- **Necessity claim resting on an unstated proviso (calibration, fixed).** The lede and §Trilemma said, without qualification, that "the Map cannot hold P-SC1 together with the idle horn". The argument runs through causal minimality. Zhang and Spirtes derive minimality from interventionism only "provided that the actual probability distribution is strictly positive", and the article's own L72 notes that deterministic relationships break it. Whether the census is fixed deterministically from the substrate is exactly what P-SC2's missing pairing law leaves open. A reviewer who accepts the tenets would still flag the unconditional "cannot", so this is not bedrock disagreement. Repairs:
  - L41: "given a strictly positive distribution" added.
  - L72: "leaving minimality only a pragmatic justification" added. This is Zhang and Spirtes's own fallback for the non-positive case, and stating it stops the retraction from widening into a licence for horn (b).
  - L74: "Unless the owed pairing law (P-SC2) fixes the census deterministically, the Map cannot hold…".
  - L98 ("Under minimality…") and L104 ("which minimality makes…") were already conditional and are unchanged.
- **Dropped qualifier on the minimality source (fixed).** L110 said "minimality follows from what a cause is". Zhang and Spirtes's claim is that it follows "from the substantive interventionist theses". The sentence now reads "follows from [[interventionist-and-counterfactual-dualism|the interventionist account]] of what a cause is". The link costs no extra words; the qualifier costs four.

### Medium Issues Found

- **Tenet-check-2026-10-14 Note 2, L102 (fixed).** "The controls make the claim testable in principle: a dualist census should leave something at onset…" drew a prediction from Dualism alone. The prediction needs P-SC1 and Tenet 3, and horn (a). The sentence now reads: "On horn (a), and only with P-SC1 and Bidirectional Interaction, a dualist census should leave something at onset that it does not leave at induction, which the controls would test." The conditional "would" fits the article's own admission (L94, table row "no independent access to a newborn's states") that no real case can yet be checked.
- **Tenet-check-2026-10-14 Note 2, L110 (fixed).** "A graded census would be simpler; the Map declines it, as in [[subject-fusion]], because knowledge of subject boundaries is incomplete" used Tenet 5 as a reason *for* the whole-number census. It now reads "the tenet only bars simplicity from settling the matter; the whole-number census rests on the commitments set out `[[#steps-or-drift|above]]`", which matches L82's cleaner form ("Those commitments, not data, license the prediction of steps"). `subject-fusion` L95 has the same Tenet 5 framing. It is outside this review's scope and is noted under Remaining Items.
- **Bayne et al. 2023: view-description quoted as the paper's verdict (fixed).** In the abstract, "likely to be in place at birth (or shortly after)" describes the *early-onset account*, and the paper's own conclusion is that recent research "points in favor of early-onset accounts". L58 now reads "Recent work favours early-onset accounts, on which infant consciousness is 'likely to be in place…'" (+4).
- **Pinto et al. 2017 "conclude" → "suggest" (fixed).** The abstract reads "These findings suggest that…", from two patients. The change costs no words.
- **Schwitzgebel & Nelson qualifier dropped (fixed).** Their abstract reads "an accident of *typical* vertebrate biology". The article had dropped "typical", which turns their claim about atypical cases into a claim about vertebrates generally (+1).
- **Bostrom counts experiences, not subjects (fixed).** Bostrom's duplication and fractional theses are about "phenomenal experiences". The article ran them into a subject census without saying so. L80 now says "with Bostrom's carried from experiences to subjects". L82's "agrees with the Map that a copy is a new subject" became "a copy adds to the count" (0 words), so it no longer attributes a subject claim to him.

### Low Issues Found

- L92: "since the count stays at two, a whole number throughout" → "since the count stays at two" (−4). The clause was redundant.

### Held, Not Changed

- **L62 "Which reading the register holds is open, and this article does not settle it."** Pessimistic-2026-10-14 Issue 4 found this sentence false once P-Q2 was strengthened on 2026-10-14, at 17:25. The resulting todo task, *P1: HUMAN DECISION — P-Q2's Born-preservation quantifier* (Status blocked), says explicitly: "Until decided, do not propagate the 17:25 reading to … `concepts/census-change-points` L62". The sentence stays until the operator chooses between option (a) and option (b). While the decision is pending, its literal content (that the reading is unsettled) is defensible.

### Counterarguments Considered

- **Dennett/Churchland: the census is a posit that P-I3 makes unreadable, so it is immunised from test.** The article already concedes this ("none of these predictions can be checked against a real case… They mark where frameworks part"; "All of this is framework-internal"). The concession is honest, so nothing was added.
- **Popper: an idle census is unfalsifiable.** The article's minimality argument is the Map's own reply: an idle census drops out of the causal model. That reply is now properly conditioned on positivity, as described above.
- **Deutsch: branching multiplies observers, so every measurement is a census event.** This is bedrock disagreement. The article states the Map's declination (L108) and marks it as the Map's view.
- **Nagarjuna/Parfit: subjects are conventional, so there is no further fact about events.** Parfit is presented as a rival verdict in the fission bullets and is not dismissed.

### Reasoning-mode classification (editor-internal)

- Engagement with Bostrom: Mode Three. The fractional thesis is called the "direct rival", "unrefuted", and the Map's whole-number census is grounded in its own commitments, not in data.
- Engagement with Schwitzgebel & Nelson: Mode Three. The article flags the same boundary and defers the discussion to [[subject-fusion]].
- Engagement with Parfit: Mode Three. The rival verdict is stated and the framework boundary marked.
- Engagement with horn (b) / epiphenomenalism: Mode Two. It uses the interventionist's own minimality condition against an idle-but-real census, now with that condition's positivity proviso stated.
- No label leakage was found. No editor vocabulary appears in the article prose.

### Citation Ledger (publisher of record)

- Andersen 2013 (*When to expect violations of causal faithfulness and why it matters*, *Phil. Sci.* 80(5) 672–683) — state: real-correct. Crossref tuple matches. Quote "mechanisms for maintaining equilibrium states are highly likely to violate" grep-verified in the OpenAlex abstract. Result direction: the abstract says CF violations are "highly likely" in such systems, which matches the article. Stance: a philosopher of science, not a dualist. The article marks the horn-(c) mapping as "the Map's own; none of the authors cited proposes it".
- Bayne, Frohlich, Cusack, Moser & Naci 2023 (*TiCS* 27(12) 1135–1149) — state: real-correct metadata, framing corrected (see Medium Issues). The quote is verbatim in the OpenAlex abstract.
- Beckers & Halpern 2019 (*Abstracting causal models*, AAAI 33(1) 2678–2685) — state: real-correct. Quote verbatim in the OpenAlex abstract. The source's curly inner quotes appear as single quotes, a standard nesting convention.
- Bostrom 2006 (*Quantity of experience*, *Minds & Machines* 16(2) 185–200) — state: real-correct. Both quotes ("There are two, I argue"; "a fractional (non-integer) number of qualitatively identical phenomenal experiences") were grep-verified in the author's PDF. Stance: computationalist, which the article states. The count is of experiences, and the scope was corrected accordingly.
- Croxford & Bayne 2024 (*Neuroethics* 17, art. 13) — state: real-correct. The paraphrase "disembodied neural organoids are not plausible candidates for consciousness" is verbatim in the OpenAlex abstract.
- Green 1995 (*Biometrika* 82(4) 711–732) — state: real-correct. The quote is verbatim in the OpenAlex abstract. "Change-point analysis as a worked example" matches "illustrated with applications to multiple change-point analysis".
- Hudson, Calderon, Pfaff & Proekt 2014 (*PNAS* 111(25) 9283–9288) — state: real-correct. The abstract confirms "recovery from pharmacologically induced coma" through "discrete metastable states".
- Pinto et al. 2017 (*Brain* 140(5) 1231–1237) — state: real-correct. Volume, issue and pages were confirmed at Europe PMC, since the Crossref record lacks them. The quote is verbatim in the OpenAlex abstract. The verb was corrected to "suggest".
- Rubenstein, Weichwald, Bongers, Mooij, Janzing, Grosse-Wentrup & Schölkopf 2017 (UAI 2017, arXiv:1707.00819) — state: real-correct. The author list matches the arXiv page, and "have been marginalised out" is verbatim in the arXiv abstract.
- Scheffer et al. 2009 (*Nature* 461(7260) 53–59) — state: real-correct. The Crossref tuple matches. The Europe PMC abstract confirms "generic early-warning signals". The variance and autocorrelation indicators come from the paper's body (critical slowing down) and are not quoted.
- Schwitzgebel & Nelson 2026 (*Philosophical Psychology* 39(3) 847–867) — state: was an orphan; References entry added from Crossref (print 2026-04-03, online 2025-06-16). "Accident of typical vertebrate biology" is verbatim in the OpenAlex abstract, and "typical" has been restored.
- Xu et al. 2023 (*PNAS* 120(19) e2216268120) — state: real-correct. "Two of the four patients exhibited a rapid and marked surge of gamma power, surge of cross-frequency coupling" is in the OpenAlex abstract, and the direction matches.
- Zhang & Spirtes 2011 (*Synthese* 182(3) 335–347; online 2010) — state: real-correct. Both quotes ("is not Markov to any proper subgraph"; "rather than an add-on methodological assumption of simplicity, necessarily follows from the substantive interventionist theses, provided that the actual probability distribution is strictly positive") were grep-verified in the CMU-hosted preprint. The preprint also has the non-positive-case "pragmatic justification" now cited in L72. Stance: interventionist; no dualist commitment is claimed for them.
- Inline ↔ References cross-check: all 13 external inline cites now have entries, and every entry is cited inline. The two Map self-citations (selection-only-channel, subject-fusion) are linked in the body.
- Superlative helper (`find_superlative_claims`): no hits.
- Register quotations: P-SC1 "is not fixed until the count and the pairing are" and "metaphysical description doing no identifiable causal work" were verified in `positions/subject-census.md` L47. P-SC2's census-circularity gap and P-SC3's phenomenality-not-pairing claim were verified at L59 and L69. P-I3's "no anatomical or behavioural measure settles it" and P-I4's re-pairing shift condition were verified. P-CS4's interface-disruption reading was verified.

## Optimistic Analysis Summary

### Strengths Preserved

- The **arity / state-change distinction** in the lede. It keeps census events apart from direction-of-interface-change signatures and is what makes anaesthesia and sleep into controls instead of evidence.
- The **controls table**. It is an honest register-derived classification, with each row's difficulty stated in the paragraph after it.
- **Horn (c) as a predicted faithfulness violation**, with source and Map clearly separated ("The following mapping is the Map's own").
- The **conjecture flagged as conjecture** ("The Map conjectures, without proof…") for the abstraction criterion.
- The **events-not-counts analysis of fission**: rival verdicts agree on net arity and part only where subjects carry something individual across time.
- The **What Follows, and From What** section, which separates what follows from the definition alone from what holds only on the Map's reading.

### Enhancements Made

- The positivity proviso, with its pragmatic fallback, now runs through the lede and §Trilemma.
- The Tenet 5 paragraph now treats simplicity as barred from deciding, not as a ground.
- Source-scope fixes for Bayne, Pinto, Schwitzgebel & Nelson and Bostrom.

### Cross-links Added

- [[interventionist-and-counterfactual-dualism]] (piped onto existing text in the Occam paragraph)
- `#steps-or-drift` (internal anchor in the Occam paragraph)

## Remaining Items

- **L62 is held pending the P1 HUMAN DECISION on P-Q2's quantifier** (todo, Status blocked). When it resolves, apply pessimistic-2026-10-14 Priority 4's wording to L62. Under option (a), the next sentence ("A detector reading public outcome statistics then has no power at a census event by construction") becomes the register's own entailment and needs no change.
- **`concepts/subject-fusion.md` L95** reads, under the Tenet 5 heading, "The graded picture is simpler… The Map declines it because knowledge here is incomplete". This is the same Tenet-5-as-reason framing fixed here at L110. It is a string-sibling outside this review's scope. A net-zero fix modelled on this page's new L110 would align them. No task was minted because reports from a deep-review fork go to the driver.

## Stability Notes

- Bostrom's fractional thesis and Schwitzgebel & Nelson's indeterminate count are the standing rivals to the whole-number census. The article marks them unrefuted, and that is a framework-boundary disagreement. Future reviews should not treat "the Map has not refuted fractional counts" as a defect.
- Everettian objections to L108 ("a quantum measurement is never a census event") are bedrock (Tenet 4).
- The positivity proviso is now explicit. Future reviews should not strengthen "unless the owed pairing law fixes the census deterministically" back into an unconditional incompatibility. They should also not widen it into "horn (b) is available", because Zhang and Spirtes's pragmatic justification still applies in the deterministic case.
