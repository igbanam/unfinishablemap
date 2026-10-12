---
ai_contribution: 100
ai_generated_date: 2026-10-12
ai_modified: 2026-10-12 20:32:00+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-12
date: &id001 2026-10-12
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-12 20:32:00+00:00
modified: *id001
related_articles: []
title: Deep Review - Tenet Falsification Conditions (Post-Fold Pass)
topics: []
---

**Date**: 2026-10-12
**Article**: [Tenet Falsification Conditions](/concepts/tenet-falsification-conditions/)
**Previous review**: [2026-07-17 (No-Op Convergence Recheck)](/reviews/deep-review-2026-07-17-tenet-falsification-conditions/)

Seventh review. **No review had seen the article since three refine-drafts landed after the 2026-07-17 pass**: a7409360f4 on 08-03 (Tenet 5 self-binding in the MWI line), 682d7a1d5c on 08-21 (Tenet 2 un-flattened, plus the strict-corridor and conditional-register paragraphs) and 4b359aa841 on 08-22 (coherence separated from indeterminacy in "Decisive falsification"). The 07-17 review's stability note ("future reviews should trigger only on … a citation change") does not cover them. This pass examined that fold, and it also found defects in the stable text that six earlier reviews had passed. Two of those reviews (06-24 and 07-17) said there were no inline↔References orphans, and that was false.

Word count 2030 → 2385 (+355; concepts soft threshold 2500, so the article stays under it). About 120 of the added words are four new References entries.

## Pessimistic Analysis Summary

### Critical Issues Found (8, all fixed)

1. **The corridor's "no signature" claim was unscoped, which contradicts the article's own L72 and the canonical tenet** (L34 lead, L70). The article said the default reading "predicts no statistical signature by construction" and that it is exposed only to "motivation-loss rather than refutation". L72 of the same article says a *conditional* register remains testable. `tenets.md` L75 says preservation "binds only that unconditioned marginal" and that "a deviation *conditioned* on intention, task or subject would test the corridor itself". The register's [P-Q7](/positions/quantum-interface/#p-q7) update of 2026-09-09 repaired the same defect in its own entry ("silenced a channel the canonical tenet holds open"), but that repair did not reach this page, which was written on 08-21/22. **Fix:** L34 now says "no signature in unconditioned Born statistics". L70 now says "exactly in the unconditioned aggregate … not Popper-refutable by aggregate Born-rule tests. At that register …". L96 adds "accumulating nulls in conditioned tests" as an adverse-evidence route. L104 says the corridor "stays exposed through conditioned tests".
2. **The page said the dualism and Many-Worlds tenets generate predictions, while their own sections say otherwise** (L34, L94, L104). The lead and "Why Honest Asymmetry Matters" credited "the quantum-level tenets (2, 3, 4)" with generating predictions that "experimentalists are already investigating", and L104 said they "anchor the framework to experimental reality". Their own sections disagree. Tenet 3 is "indirect empirical implications". Tenet 4 is a choice whose rivals "make identical predictions for all feasible experiments" and whose rejection is "motivated primarily by philosophical concerns". The 08-21 fold fixed this flattening for Tenet 2 but left it in place for Tenets 3 and 4 and in L104, the same kind of leftover named in sweep-fixes-the-disclaimer-and-strands-its-dependents. **Fix:** the lead now separates MQI (predictions in its mechanism-committed readings) from Tenets 3–4 (indirect only). L94 now reads "bear on experiments already under way, but unequally … Tenets 3 and 4 are touched only indirectly, by evidence they do not themselves predict". L104 now names only Tenet 2's mechanism-committed readings, plus the corridor's conditioned-test exposure.
3. **The No Many Worlds section contradicted itself** (L84). It said "many-worlds and collapse interpretations make identical predictions for all feasible experiments" one sentence after saying a levitated-optomechanical blueprint may test objective collapse. Donadi et al. 2021, cited at L68, is itself a feasible test of a collapse model. **Fix:** the page now distinguishes objective-collapse *theories* (they modify the dynamics, so they can be tested) from collapse *interpretations* (identical predictions). L98's "collapse interpretations" now reads consistently with this.
4. **Pitts 2020 was credited with a response he does not give** (L78). The page said Pitts "surveys the conservation law challenge …, providing the analytical framework for this response", where "this response" was the Map's no-energy-injection commitment. The publisher abstract (via OpenAlex) shows that Pitts's reply is Noether-conditional: conservation holds only where the laws are symmetric, and expecting it in the brain "simply assumes the falsehood of Cartesianism. Hence Leibniz's objection begs the question." That route *tolerates* local violation, which is the opposite of the Map's move. The 06-24 review recorded this exact over-attribution in the roadmap sibling ("Pitts does NOT discuss the energetically-equivalent-selection move") but missed it here. **Fix:** the sentence now presents Pitts as "a different route", quotes the verified clause, and states that his reply tolerates local violation, which the Map's commitment does not need.
5. **The Hameroff 2020 attribution went beyond what could be verified** (L68). The page attributed "Orch OR generated 20 testable predictions (originally published in 1998)" to Hameroff (2020). The 20-predictions / six-confirmed tally is verified for **Hameroff & Penrose 2014**. Elsevier's 16 Jan 2014 press release for the PLR review says it "reviews 20 testable predictions of Orch OR published in 1998 -- of these, six are confirmed and none refuted". The Hameroff 2020 commentary is paywalled (tandfonline returned 403), and its abstract and title support only "easily falsifiable". **Fix:** Hameroff 2020 is now credited with its title claim ("the most easily falsifiable theory"), and the tally is credited to the 2014 review alone.
6. **"Independent evaluation … remains limited" left out the critical independent record** (L68). The Map's own register (P-Q-Orch, `positions/quantum-interface` L102) demotes Orch OR because of independent biophysical critiques. The article set the proponents' "none refuted" against no counterweight, a calibration gap that a reviewer accepting the tenets would flag. **Fix:** the page now cites Reimers et al. 2009 (PNAS 106(11):4219–4224, verified at Crossref, with the abstract via OpenAlex). The qualifier is kept: models are "untenable" *insofar as they embody coherent Fröhlich condensation as an essential element*. The page also links the register's ranking.
7. **The page attributed to `tenets.md` words it does not contain** (L40). It said "The tenet page is explicit on the point: decoherence suppresses superposition and fixes a preferred basis without settling why one outcome rather than another becomes actual". `tenets.md` has no "preferred basis" and no such sentence, and `git log -S "preferred basis"` on it returns nothing. The physics is correct, but it was presented as the tenet page's claim. **Fix:** the physics gloss is now in the article's own voice. The tenet-page attribution is now limited to what L71/L77 actually say, including the verbatim "matters only for candidate mechanisms that require *pre-decoherence* coherence". I also added "experimental" to "condition reaching every reading", because `tenets.md` falsifier (b), theoretical supersession, also reaches every reading, so the unqualified "would have to" was false.
8. **Inline↔References orphans** (two earlier reviews said there were none):
   - "Deutsch's 1985" (L40) had no References entry. **Added.**
   - The 2023 IIT letter (L50) had no cite and no entry. **Added** "(Fleming et al., 2023)" and the entry.
   - "Kleiner (2021)" dropped the co-author. The References entry is Kleiner & Hoel. **Fixed** to "Kleiner and Hoel (2021)".
   - arXiv:2512.02838 was cited by ID with no author. **Added** "Horchani, 2025, an unrefereed preprint" and the entry.
   - The reverse direction is clean. The one References entry with no inline (surname, year) mention is the Map's self-citation of the roadmap (#7), which is linked by wikilink and kept by convention.

### Medium Issues Found (fixed)

- **The Kleiner & Hoel paraphrase widened its scope.** "Affects all consciousness theories" became "generally". The paper says the fragility "affects many contemporary theories". "If inference assumes the theory, falsification becomes circular" now reads "strictly dependent … unfalsifiable", which is the paper's own term. The word "show" replaced "argues" (the abstract says "we show").
- **The letter was characterised more strongly than its text.** "Calling IIT unfalsifiable pseudoscience" now reads "applying the 'pseudoscience' label to IIT until 'the theory as a whole' becomes empirically testable". The quoted phrases were checked with grep against the letter PDF from OSF. The letter conditions the label on testability and does not claim in-principle unfalsifiability. The sibling `topics/consciousness-and-the-metaphysics-of-composition` already reads it this way.
- **The Cogitate result was understated.** "Neither … decisively confirmed or falsified" now includes the abstract's "substantially challenging key tenets of both" (verbatim). That supports the article's point more strongly.
- **"Dualism already predicts all of these"** (anaesthesia, lesion, NCC data) now says the theory *accommodates* them and that this earns it no evidential credit. Calling it prediction treated accommodation as prediction.
- **"Mental causation should violate Noether's theorem"** was a technical misstatement, since a theorem cannot be violated. It now reads "would break the energy conservation Noether's theorem ties to time-symmetric laws". "Without adding or removing energy" now matches the sibling `concepts/conservation-laws-and-mental-causation` L97 (ensemble expectation preserved, single trials may differ) and links it.
- **The banned-construct opener** "This is not a special embarrassment for dualism." now reads "The difficulty is no special embarrassment for dualism."

### Publisher-of-Record Citation Ledger (all cites)

- Kleiner & Hoel 2021 ("Falsification and consciousness", *Neurosci. Conscious.* 2021(1) niab001) — real-correct in References. Inline was **real-wrong-metadata** ("Kleiner (2021)", co-author dropped), corrected. Crossref plus the PMC abstract, read verbatim. Result direction: independent → "automatically falsified", strictly dependent → "unfalsifiable". The article now matches.
- Hameroff 2020 ("'Orch OR' is the most complete, and most easily falsifiable theory of consciousness", *Cogn. Neurosci.* 12(2):74–76) — real-correct. Crossref: online 2020-11-24, print 2021-04. Year 2020 is kept as the online year. The claim was **narrowed to the title claim** because the full text could not be reached (403).
- Hameroff & Penrose 2014 (*Phys. Life Rev.* 11(1):39–78) — real-correct (Crossref). The 20/6/0 tally was verified through the publisher press release quoted on ScienceDaily (16 Jan 2014). The full text is Elsevier-blocked to curl, so the press release is the strongest source reached. The claim is presented as the proponents' self-assessment.
- Donadi et al. 2021 (*Nat. Phys.* 17(1):74–78) — real-correct (Crossref). I added the issue number and DOI. "Constrains specific collapse models" is a faithful summary (it rules out the parameter-free Diósi–Penrose model).
- Cogitate Consortium (Ferrante, Gorska-Klimowska, et al.) 2025 (*Nature* 642(8066):133–142) — real-correct (Crossref; the abstract via OpenAlex, read verbatim). Result direction is mixed ("align with some predictions … substantially challenging key tenets of both"), and the article now quotes it.
- Pitts 2020 (*Philosophia* 48(2):673–707) — metadata real-correct (Crossref). The **framing was over-attributed** and is corrected (Critical 4). Pitts's stance: the a priori conservation objection begs the question; local violation is tolerable; "Empirical neuroscience is another matter."
- Deutsch 1985 ("Quantum theory as a universal physical theory", *IJTP* 24(1):1–41) — real-correct (Crossref). It was an **orphan**, and the entry is now added. Stance: Everettian. The article presents his experiment as pressure *against* Tenet 4, which is correct.
- Fleming et al. 2023 ("The Integrated Information Theory of Consciousness as Pseudoscience", PsyArXiv, doi 10.31234/osf.io/zsr78) — real-correct (Crossref lists the group author "IIT-Concerned" and ten named authors; the PDF was read). It was an **orphan**, and the entry is now added. The 124-signatory count matches *Scientific American*'s report.
- Reimers et al. 2009 (*PNAS* 106(11):4219–4224) — **new cite**, real-correct (Crossref, with the abstract via OpenAlex). The quoted "untenable" is kept with its conditional qualifier.
- Horchani 2025 (arXiv:2512.02838, "Experimental Blueprint for Distinguishing Decoherence from Objective Collapse") — real-correct (arXiv API: single author, posted 2025-12-02, CSL in a levitated nanosphere). "May test" is softened to "proposes to test", and the item is marked unrefereed.
- Southgate & Oquatre-six 2026-04-09 (roadmap self-cite) — matches the roadmap's `created:` date.
- `find_superlative_claims`: empty. No currency sweep needed.

### Cited-Author-Stance Leg

None of these authors is presented as endorsing the Map's conclusions:

- Kleiner & Hoel: methodological, framework-neutral.
- Hameroff/Penrose: proponents of Orch OR. The tally is labelled as their own assessment.
- Pitts: now explicitly presented as taking a different route from the Map.
- Deutsch: Everettian.
- Fleming et al.: IIT critics.
- Reimers et al.: Orch OR critics.
- Cogitate: theory-neutral consortium.

### Reasoning-Mode Classification (editor-internal)

- **Physicalism (L98):** Mode Two. Physicalism lacks an agreed falsification condition, so the reply holds physicalism to its own falsifiability standard. Unchanged.
- **Many-worlds (L84, L98):** Mode Three, an honest boundary marker ("motivated primarily by philosophical concerns"). Unchanged.
- **Label leakage:** none (grep clean, and no "load-bearing").

### Counterarguments Considered

- *An Everettian objects that Deutsch's experiment would refute consciousness-collapse readings rather than "Tenet 4" as such.* Bohm-type single-world views would survive it. This was left alone as a framework-level judgement already hedged ("under severe pressure"), consistent with the stability note.
- *An empiricist objects that the corridor is unfalsifiable.* This is answered in the text, now consistently: it is untestable at the aggregate register, testable at the conditional register, and also exposed to motivation-loss.

## Optimistic Analysis Summary

### Strengths Preserved

- The decisive / cumulative / structural taxonomy.
- The 08-21/22 fold's reading-by-reading split of Tenet 2. It is accurate against the roadmap (L77–L89) and `brain-internal-born-rule-testing` (L114–L124), and this pass only scoped it.
- "Why Honest Asymmetry Matters", which turns uneven testability into a credibility asset. It is now truer, because the asymmetry is stated accurately for Tenets 3 and 4 as well.
- The Tenet 5 self-binding in the MWI line, from the 08-03 fold.

### Enhancements Made

- The counterweight of an independent Orch OR assessment (Reimers 2009), linked to the register's ranking.
- Pitts's empirical opening ("leaves the question to empirical neuroscience") now sits in a falsification-conditions page, which is where it belongs.

### Cross-links Added

- [conservation-laws-and-mental-causation](/concepts/conservation-laws-and-mental-causation/) (body, L78)
- The [quantum-interface](/positions/quantum-interface/) Orch OR ranking (body, L68; this link already existed elsewhere in the page)

## Remaining Items / Out-of-Scope Findings

- **The unscoped "no Born-statistical signature by construction" also appears in siblings** that are on today's avoid list or were edited today. These were not touched:
  - `obsidian/topics/brain-internal-born-rule-testing.md`: L3 (description), L106, L116 ("predicts no Born-statistical signature, so no single Born-rule experiment can directly refute it")
  - `obsidian/topics/falsification-roadmap-for-the-interface-model.md`: L87, L142

  Each needs the same "unconditioned aggregate" scoping as `tenets.md` L75 and [P-Q7](/positions/quantum-interface/#p-q7)'s 09-09 update. These are candidates for a refine-draft sweep.
- **`obsidian/topics/falsification-roadmap-for-the-interface-model.md` L91** credits the "20 testable predictions published in 1998" to Hameroff (2020), the same unverified attribution fixed here. It also says "Independent assessment of these claims remains limited", the same calibration gap fixed here.
- **`obsidian/workflow/todo.md` L1019** (operator decision, epistemology bedrock immunity) notes that this page's falsification criteria differ from the epistemology hub's report-prediction test and that the two "need reconciling". That task is queued and awaiting a human, so it was not touched here.
- The Hameroff 2020 full text is still unread, because it is paywalled. If someone gets access, they should check whether it restates the 20/6/0 tally. The current wording does not depend on it.

## Stability Notes

- Bedrock, not to be re-flagged: the MWI rejection being philosophically motivated, and the vagueness inherent in "cumulative falsification".
- **The corridor wording is now register-scoped.** Untestable at the aggregate register, exposed at the conditional register, and also exposed to motivation-loss. Do not "simplify" it back to "no signature by construction" without the scope, because that reopens a contradiction with `tenets.md` L75.
- **"Quantum-level tenets generate predictions" must not return for Tenets 3 and 4.** Their own sections say "indirect" and "identical predictions".
- Citation ledger above is complete as of 2026-10-12. Re-verify on any content-changing pass (see quote-fidelity-defects-survive-metadata-reviews): two prior "no orphans" claims were false.
- Watch item, carried over: an independent (non-proponent) evaluation of Orch OR's predictions, or a levitated-optomechanical collapse result. Neither exists as of 2026-10-12; Horchani 2025 is a blueprint.