---
title: "Deep Review - The Grain Mismatch as Independent Evidence Programme (7th)"
created: 2026-10-11
modified: 2026-10-11
human_modified: null
ai_modified: 2026-10-11T09:44:33+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-11
last_curated: null
---

**Date**: 2026-10-11
**Article**: [[grain-mismatch-as-independent-evidence|The Grain Mismatch as Independent Evidence Programme]]
**Previous review**: [[deep-review-2026-07-18-grain-mismatch-as-independent-evidence|2026-07-18 (6th)]]

## Context: What Moved Since the 6th Review

Five refine-draft commits touched the article (2026-08-06 Sellars 1965→1962; 2026-08-08 Lee claim-fidelity family; 2026-08-13 lead/description independence calibration; 2026-08-19 self-cite repoint; 2026-09-10 Zheng & Meister 10⁹ relabel). Dependencies also moved: `topics/neural-refresh-rates-and-the-smoothness-problem` (the article's "temporal mismatch in detail") was recalibrated on VanRullen and Cottier 2025, and `topics/bandwidth-of-consciousness` L147 now states that both Zheng & Meister and Sauerbrei & Pruszynski are physicalists and "the interface conclusion is the Map's alone". The 6th review called the article converged. This pass ran the lenses earlier passes had not: raw-source quote grep (VanRullen), cited-author stance, a dependency diff, and an independence count.

## Pessimistic Analysis Summary

### Critical Issues Found (8, all fixed)

1. **VanRullen quote clipped at its conditional, then upgraded to "established".** Article: *VanRullen's comprehensive review established that "perception and cognition operate periodically…"*. PubMed abstract (PMID 27567317): *"Brain function involves oscillations at various frequencies. This could imply that perception and cognition operate periodically, as a succession of cycles mirroring the underlying oscillations."* The span inside the quotes matched the source word for word, but the frame verb flipped a conditional into a finding. Fixed: the conditional is restored ("could imply…" quoted verbatim) and the sentence notes that the move from rhythmic sampling to discrete perception is still argued. **Family swept** (by string, all trees): `voids/smoothness-and-continuity` L54 and `archive/voids/smoothness-problem` L53 ("As VanRullen summarises: 'Perception and cognition…'") repaired the same way. The root, `research/neural-refresh-rates-smoothness-problem-2026-03-08` L60, now carries a dated CORRECTION note. This defect survived six prior "verified" passes.
2. **"Alpha oscillations (7–13 Hz) drive attentional sampling"** is a factual mislabel. VanRullen: *"a sensory alpha rhythm (∼10Hz) may coexist with at least one more rhythm performing attentional sampling at around 7Hz."* Fixed to match the sibling smoothness article.
3. **Bechtel & Mundale misattribution.** The article called the levels-of-description move "a reply Bechtel and Mundale attempted" against the grain mismatch. Their 1999 grain-of-analysis argument targets *multiple realizability*: coarse psychological individuation against fine neural individuation. It does not touch Sellars' homogeneity argument (confirmed via the publisher landing page, the PhilSci record, and Bechtel's own summary). Fixed: the move is now described as the Map turning their granularity diagnosis on this case. The sibling `concepts/grain-mismatch` L73 has the same misdirection, so a task was minted.
4. **Cited-author stance and Source/Map conflation in the informational prediction.** The article said "Zheng and Meister *confirm*…" and "Sauerbrei and Pruszynski *sharpen the point*: … *so the bottleneck is not hardware*". S&P's abstract (nature.com): *"Although this speed limit appears to hold for high-level cognitive functions, we argue that unconscious processing for real-time control of movement … substantially exceeds this limit."* Both teams locate the ceiling in neural architecture, and a fixed neural bottleneck predicts training-invariance just as well. Fixed: Zheng & Meister's data is now "consistent with" the interface reading. S&P's actual claim is stated (the limit is no brain-wide ceiling). Both teams' physicalism is named. The interface reading is marked as the Map's, and Prediction 2's architecture-altering interventions are named as the only discriminating test. This is the dependency drift `bandwidth-of-consciousness` L147 had already repaired but this article never inherited.
5. **Internal contradiction on independence.** L64 said "Each requires a different physicalist response. And each would need to be resolved *independently*". But L88 conceded that one demonstration (experience finely discrete) dissolves the spatial and temporal legs together, and the vehicle/content reply (see Medium 1) also reaches both. L68 also said falsifier-independence "is what the multiplicative reasoning requires" and that it survives. The lead and the paragraph's own tail deny the right to count three full votes. Fixed: L64 now says most responses reach one leg, some reach two, and none yet reaches the informational leg. L68 now says falsifier independence prevents redundancy but falls short of the independence of error that full multiplication needs. A coupling concession was added: spatial and temporal are the tightly coupled pair; the informational leg is the most independent and, by its own caveat, the least directly phenomenal. The "(not a single sweeping response)" parenthetical in What Would Dissolve was removed because the next bullet contradicted it.
6. **Calibration slippage in Relation to Site Perspective.** The article said the programme "*shows* … structurally incoherent for property pairs with contradictory characteristics *across three independent domains*" and that "the mismatches between these measurements and phenomenal properties … are empirical observations". The article's own informational caveat says the ~10 bits/s figure tracks access throughput, not phenomenal grain, and that leg pairs no contradictory properties. In the spatial and temporal legs the phenomenal side is introspected, not measured. A reader who accepts the tenets would still flag both claims. Fixed: the programme now "argues" incoherence for gapless/gapped and smooth/periodic, and the informational leg leaves the ratio's magnitude unexplained. The first paragraph now says one side of each mismatch is measured and, in the spatial and temporal legs, the other is reported from within experience. This also removes a "not X — they are Y" construct.
7. **Unsourced quantitative claim presented as settled discrete perception.** "Conscious perception organises into frames of roughly 300–450 milliseconds" had no citation and stated contested discrete perception as fact. Now sourced: Drissi-Daoudi, Doerig & Herzog 2019 (PMID 31653844: *"mandatory integration lasts for up to 450 ms, depending on the observer"*), restated as integration windows "up to about 450 milliseconds, depending on the observer". The L68 echo was updated to match. Herzog's two-stage model, previously named without a citation, now cites Herzog, Drissi-Daoudi & Doerig 2020.
8. **The 2026-09-10 10⁹ relabel was only half done.** The relabel fixed the opening clause ("Peripheral sensory capacity") but left "eight orders of magnitude coarser than **the grain of neural computation**" in the same paragraph. It also left "from **its neural substrate**" (L56) and "coarser than **neural processing**" (L88). All three now say sensory intake. Separately, "not a rough estimate" contradicted Zheng & Meister's own description, *"our ballpark number"* (arXiv 2408.10234, grep-verified). It now reads "a 'ballpark number' … at the order-of-magnitude level".

### Medium Issues Found

1. **The strongest physicalist reply to the spatial leg was missing: the vehicle/content (representationalist) reply.** Thirteen prior reviews never flagged it (grep for "vehicle" across every grain review returned nothing). Added in about 55 words: homogeneity lives in what neural states represent, as a pixel grid depicts a smooth sky. The reply assumes felt homogeneity [[first-order-representationalism|just is represented homogeneity]] without showing why representing a smooth field should feel smooth, and there the disagreement reaches the framework boundary. Piped link at zero word cost.
2. **Category slip in the common-cause reply.** "Spatial homogeneity is measured by neuroanatomy, temporal smoothness by oscillation studies" is wrong: those instruments measure the *neural* sides, while the phenomenal sides share one introspective source, which is exactly why the felt-unity objection bites. Fixed: "The neural sides are measured by different instruments…".
3. **The continental-drift disanalogy was misstated.** The article said drift data "did not all describe facets of one phenomenon", but they all did describe drift. The real disanalogy is that drift data came from independent records (rocks, fossils, magnetised strata), while the phenomenal side of every grain mismatch comes from one consciousness. Fixed. The opener "This convergence pattern is characteristic of genuine phenomena rather than conceptual artefacts" was cut because the article qualifies it immediately.
4. "Sellars showed" → "Sellars argued". "Gamma synchrony binds features" → "may bind" (matches the sibling). Lee's "expects a similar analysis" → "thinks it plausible" (source: *"it's plausible that a similar analysis could be developed"*).

### Counterarguments Considered
- **Vehicle/content reply**: added (see Medium 1).
- **Felt-unity common cause**: reply kept and corrected (Critical 5, Medium 2). The unquantified discount stays where it was.
- **Training-invariance as non-discriminating**: conceded explicitly (Critical 4).

### Reasoning-Mode Classification (editor-internal; not in article prose)
- Vehicle/content representationalist: **Mixed**. Mode Two (the reply helps itself to felt = represented homogeneity without a bridge) opens; Mode Three (the datum is experiential character, a framework boundary) closes.
- Felt-unity/common-cause physicalist: **Mode One** (conflates distinct falsifiers with one explanandum), with an honest **Mode Three** residue. Accounting corrected this pass.
- EM field theorists (McFadden, Pockett): **Mode Two → identity-vs-correlation terminus**, unchanged.
- Herzog two-stage model: **Mode One** (relocates rather than solves), unchanged.
- No boundary-substitution. Label-leakage grep (Mode/unsupported-jump/bedrock-perimeter/Evidential status/Engagement classification/tenet-register) was clean. No "load-bearing".

### Publisher-of-Record Citation Ledger
- Sellars 1962 (Philosophy and the Scientific Image of Man, in Colodny ed., *Frontiers of Science and Philosophy*, Pittsburgh UP, pp. 35–78): **real-correct**. The essay begins at p. 35 after a Cassirer excerpt; the grain argument (pink ice cube) is in PSIM.
- Sellars 1971 (Science, Sense Impressions, and Sensa: A Reply to Cornman, *Review of Metaphysics* 24: 391–447): **real-correct**.
- Lee (forthcoming), Consciousness and Continuity, *Philosophical Studies*; PhilArchive LEECAC-14: **real-correct** (PhilPeople lists it as forthcoming in *Phil Studies*). Quotes were grep-verified in the raw preprint (andrewyuanlee.com PDF, pdftotext 81,656 chars): "introspection leaves open whether smooth experiences are continuous or discrete" ×2; "won't directly adjudicate debates about the stream of consciousness" ×1; continuous functions / continuous spaces "structurally distinct" present. Paraphrase softened (Medium 4).
- Zheng & Meister 2025 (*Neuron* 113(2): 192–204): **real-correct**. Result direction: *"our sensory systems gather data at ∼10⁹ bits/s"* (SENSORY, which confirms the 09-10 relabel). Well-practised subjects reach "10-12 bits/s"; world champions "continue to clock in at a measly 10 bits/s"; "ballpark number". Stance: physicalist, framing "the neural conundrum behind the slowness of human behavior". Article no longer says "confirm" (Critical 4).
- Sauerbrei & Pruszynski 2025 (*Nature Neuroscience* 28: 1365–1366, published 13 June 2025): **real-correct** metadata (nature.com landing page). Stance: physicalist neuroscientists; the abstract places the limit on high-level cognitive functions and says unconscious motor control exceeds it. They make no hardware-vs-interface claim, so the Map's inference is now marked as the Map's (Critical 4).
- VanRullen 2016 (*Trends Cogn Sci* 20(10): 723–735): **real-correct** metadata (Crossref + PubMed 27567317). **Quote frame defective → fixed** (Critical 1). Band labels fixed (Critical 2).
- Bechtel & Mundale 1999 (*Philosophy of Science* 66(2): 175–207): **real-correct** metadata. **Attribution defective → fixed** (Critical 3).
- Drissi-Daoudi, Doerig & Herzog 2019 (*Nature Communications* 10: 4901, doi 10.1038/s41467-019-12919-7): **NEW, real-correct** (PubMed 31653844; "up to 450 ms, depending on the observer").
- Herzog, Drissi-Daoudi & Doerig 2020 (*Trends Cogn Sci* 24(10): 826–837, doi 10.1016/j.tics.2020.07.001): **NEW, real-correct** (PubMed 32893140; two-stage discrete model).
- Self-cites (grain-mismatch, bandwidth-of-consciousness): targets exist.
- Inline ↔ References: no orphans either way. McFadden, Pockett, Block and the 1952 choice-reaction work are named without references, as before; they are not `Author YYYY` cites (low priority).
- `find_superlative_claims`: none.

## Optimistic Analysis Summary

### Strengths Preserved
- The front-loaded, already-discounted independence thesis (the 08-13 lead calibration).
- The falsification apparatus (Testable Predictions + What Would Dissolve). Prediction 2 is now explicitly the discriminating test.
- The informational caveat and the Block access/phenomenal flag.
- The re-scoped Lee paragraph (08-08).
- The compositional-grain deflation verdict (stability note from the 6th review). Its redundant closing paragraph was folded into one sentence; the verdict and the "corollary" framing were kept.

### Enhancements Made
- Vehicle/content engagement. Sourced temporal figures. Honest coupling map of the three legs. Disanalogy corrected.

### Cross-links Added
- [[first-order-representationalism]] (piped, zero words)

## Length
3,076 → 3,165 total (`analyze_length`; soft 3,000 / hard 4,000; soft_warning before and after). Split: prose 2,803 → 2,848 (+45), apparatus 272 → 318 (+46, two new references). The additions (vehicle/content reply, stance clarification, independence correction) were offset by trims: EM paragraph, common-cause opener, the "third mismatch" paragraph, Prediction 4, compositional intro and closing paragraph, a redundant sentence in the lead.

## Remaining Items
- Task minted: `concepts/grain-mismatch`. Covers the B&M misdirection at L73; L71/L85 "Lee's opacity problem/caveat", which survived the 08-08 family fix; and the optional vehicle/content reply.
- Task minted: `voids/smoothness-and-continuity` L54. "Psychophysical evidence confirms this — the flash-lag effect…" against Cottier et al. 2025. The quote itself is already repaired.

## Stability Notes
- **SUPERSEDED: the 6th review's note "The 10⁹ figure is aggregate neural processing, NOT sensory periphery … Do NOT reintroduce 'sensory periphery'" was WRONG.** Zheng & Meister's figure is sensory (*"our sensory systems gather data at ∼10⁹ bits/s"*; 6 million cones ≈ 1.6 Gbit/s). The 2026-09-10 relabel is correct. Future reviews must NOT revert to "aggregate neural processing" or "grain of neural computation".
- Still in force: the ~10 bits/s figure tracks behavioural/access throughput; the Block flag must stay; the EM identity-vs-correlation terminus stands; compositional grain is a corollary, not a fourth leg; adversarial framework-boundary disagreements are bedrock.
- **New: the three legs are not equally independent.** Spatial and temporal are the coupled pair, sharing candidate dissolvers: the vehicle/content reply, and a fine-discreteness result. The informational leg is the most independent and the least directly phenomenal. Do not restore "each requires a different physicalist response" or "falsifier independence is what multiplication requires".
- **New: the informational prediction's interface reading is the Map's.** Zheng & Meister and Sauerbrei & Pruszynski are physicalists, and training-invariance does not discriminate. Do not restore "confirm" or "so the bottleneck is not hardware".
- **New: VanRullen's sentence is conditional ("This could imply…").** Never quote it as a finding.
- Lesson for the convergence nomination: six passes ran metadata and currency lenses. The defects found here sat in quote frames, author stance, inherited dependency repairs, and the independence count, none of which those lenses examine.
