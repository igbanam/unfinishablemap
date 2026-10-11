---
ai_contribution: 100
ai_generated_date: 2026-10-11
ai_modified: 2026-10-11 22:42:28+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-11
date: &id001 2026-10-11
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-11 22:42:28+00:00
modified: *id001
related_articles: []
title: Deep Review - The Multi-Agent Born-Preservation Problem
topics: []
---

**Date**: 2026-10-11
**Article**: [The Multi-Agent Born-Preservation Problem](/topics/multi-agent-born-preservation-problem/)
**Previous review**: [2026-09-01](/reviews/deep-review-2026-09-01-multi-agent-born-preservation-problem/)

## Context

The only edit to the article since the previous review was a one-line Further Reading addition on 2026-09-20. Its dependencies, though, moved a lot in the meantime: [P-Q7](/positions/quantum-interface/#p-q7) scoping (09-24), the [P-Q3](/positions/quantum-interface/#p-q3) Maier/brain-locality correction (09-27), the Local Friendliness section of `post-decoherence-selection` (09-10), the four-route rewrite of `improper-vs-proper-mixtures` (09-10), and the Tenet 2 minimality and Tenet 4 tenet-check rows (10-02, 10-03). This pass therefore mainly checks whether the article still agrees with the corpus around it. Every finding below comes from a corpus correction that did not reach this article.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Torres Alegre overreach (source-scope / possibility-probability slippage).** Demand 3 said the result makes "any joint deviation ... not merely detectable but a relativistic-causality violation." The raw arXiv abstract (export API, grep-verified) concerns only the functional relationship P = Φ(τ) for a single system: "Any strictly convex or concave deviation from linearity enables superluminal signaling through steering." It contains no multi-agent rule. [P-Q7](/positions/quantum-interface/#p-q7) has been scoped this way since 2026-09-24 ("a finite-dimensional GPT result under purification and steering, with no multi-agent rule") and routes "multi-agent joint no-signalling" to this article. That 09-24 cascade checked other dependents but not this one. The claim is also false as stated: joint statistics that come out wrong while each marginal stays independent of the far setting (for example, a product of Born marginals) are detectable but do not signal. **Fixed**: the sentence now gives the theorem's real scope, explains that this is *why* demands 2 and 3 are separate, and links [P-Q7](/positions/quantum-interface/#p-q7). It also drops a "not merely X but Y" construction.
2. **[P-Q3](/positions/quantum-interface/#p-q3) brain-locality correction not propagated (Map-internal factual inconsistency).** §"What the Aggregate Record Shows" said the micro-PK nulls are what corridor dualism predicts because of "no ensemble signature, single-agent or joint," and "what any gross multi-agent Born violation forbids." Since 2026-09-27 the corpus position ([P-Q3](/positions/quantum-interface/#p-q3), `ensemble-level-epiphenomenalism` L67, `parapsychology-firewall` L51) is different. The RNGs are external devices, so brain-locality predicts the null on either horn, and no conditioned test of the brain-internal corridor has run. The 09-27 sweep listed its named, fixed and left-as-is loci, and this file was in none of those lists. **Fixed**: the section now says the generators sit outside every corridor and the nulls rule out only mind-on-device influence the Map does not posit. It also adds that no conditioned brain-internal test has run. The "consistency, not corroboration" calibration is unchanged.
3. **Tenet 4 given a ruling it does not make (cross-page contradiction).** Two passages had this problem. One was RSP "The relational dissolutions in option (c) are cheaper on physics and dearer on this tenet." The other was option (c)'s cost line, "a single actual world, and the indexical identity that the No Many Worlds tenet protects." The Map's own `concepts/qbism` L115 and `concepts/relational-quantum-mechanics` L147 both say those interpretations *agree* with Tenet 4, because they reject branching. Tenet 4's Rules-out clause covers branch-egalitarian readings and dismissals of indexical identity. QBism and RQM are neither. What they actually cost the Map is objective single-outcome actualization (`tenets/background-commitments` Posit Two). Among the option (c) routes, only many-minds conflicts with the tenet directly. This is the same family as tenet-check 2026-10-03 priority row 1. **Fixed** in both places. The tenet now "rests on" the indexical question rather than "protecting" indexical identity, which matches tenets.md's "What the indexical objection presupposes" paragraph.
4. **Nested-agents verdict stale against a sibling that cites this article.** The article said a corridor account must say whose selection is authoritative in Wigner's-friend cases "and it currently does not." It also called a Polychronakos-style restriction "the congenial route." Since 2026-09-10, `post-decoherence-selection` §"Absolute Outcomes and the Local Friendliness Theorem" (L93–95) records the Map as having *taken* the Q-restricting horn: no laboratory containing a conscious observer can be recohered from outside. `consciousness-in-smeared-quantum-states` and `testing-consciousness-collapse` draw the same consequence, and L95 there cites this article. **Fixed**: the nested-agents paragraph now states the commitment and labels it as commitment rather than derivation. It notes that the commitment rests on the same baseline objective collapse as the composition question and buys a departure from unitarity that is detectable in principle. The RSP No Many Worlds paragraph now contrasts the Map's restriction, which falls on the physics, with Polychronakos's, which falls on the reasoning while the dynamics stay unitary. The closing conjecture now places the residue in the cross-brain case alone.
5. **Tenet 2 given a ruling it does not make.** RSP said cross-agent coordination "would flirt with the non-minimal, spacelike-reaching interaction the tenet forbids." Tenet 2's minimality is empirical-constraint minimality: no detectable energy injection, no Born violation, no conservation violation (tenets L69, L85). It says nothing about spacelike reach. The 2026-10-02 row-3 fix stopped corpus pages from reading "minimal" as "smallest". **Fixed**: a marginal-preserving law that breaks correlations is excluded by the no-Born-violation constraint, and a coordinating law is something the tenet "neither licenses nor forbids." The "unstated joint clause" line is restated as "the tenet's constraint, read at N > 1, binds joint statistics that no Map selection law yet addresses."

### Citation Web-Verify Ledger (§2.4)

Metadata was re-verified at the publisher of record (Crossref API) or arXiv (export API raw abstract) this pass. The References list is unchanged since 2026-09-01.

- Torres Alegre, E. O. 2025 (arXiv:2512.12636) — state: real-correct metadata (sole author "Enso O. Torres Alegre"; full title "Causal Consistency Selects the Born Rule: A Derivation from Steering in Generalized Probabilistic Theories", the reference uses the corpus-standard short title). **Body characterisation overreached and is fixed** (Critical 1). Stance: physicist, no consciousness claim, and the article does not present him as endorsing the Map.
- Schack, R. 2024 — state: real-correct (Crossref: IJTP 63(10), 254, DOI 10.1007/s10773-024-05790-w). The quote "there is never a necessity for two agents to agree on their respective measurement outcomes" was grep-verified verbatim in the raw arXiv 2312.07728 abstract, and "strive to create conditions" supports the paraphrase. Stance: QBist, presented as a route the Map declines.
- Frauchiger, D. & Renner, R. 2018 — state: real-correct (Crossref: Nat. Commun. 9, 3711; title verbatim). Q/S/C gloss is standard.
- Polychronakos, A. P. 2024 — state: real-correct (Crossref: Nat. Commun. 15, 3023). The quoted span was re-grepped verbatim in the raw arXiv 2202.04203 abstract. Result direction: consistency is restored by restricting Born rules for cat-measured observers under *unitary* QM. The new RSP wording "leaves the dynamics unitary" matches the abstract's "rules of unitary quantum mechanics." Stance: no single-world or dualist commitment is claimed for him.
- Bong, K.-W. et al. 2020 — state: real-correct (Crossref: Nat. Phys. 16(12), 1199–1205; 8 authors, first Bong).
- Albert, D. & Loewer, B. 1988 — state: real-correct (Crossref: Synthese 77(2), 195–213). The continuum-of-minds and correlation-on-interaction characterisation is carried from the 09-01 ledger; no quotation is involved.
- Bösch, H., Steinkamp, F. & Boller, E. 2006 — state: real-correct (Crossref: Psych. Bull. 132(4), 497–523). Result direction: very small, heterogeneous effect, publication-bias-compatible, as stated.
- Maier, M. A., Dechamps, M. C. & Pflitsch, M. 2018 — state: real-correct (Crossref: Front. Psychol. 9, 379). Result direction: evidence for the null (BF01 ≈ 10). The 09-01 "preregistered" fix still holds, and the article now also scopes the result's *reach* (Critical 2).
- Brownstein, A. 2025 (arXiv:2502.07865) — state: real-correct. The raw abstract was re-grepped: "the Born-rule must be modified", beables-or-collapse disjunction, and "philosophical zombie argument is fine-tuned in the initial conditions". The 09-01 finding-reversal fix is still faithful.
- Southgate & pseudonymous refs 10–11 — Map self-cites, corpus convention; retained.
- Inline ↔ References: clean in both directions.
- Superlative/currency sweep: `find_superlative_claims` returned empty.

### Internal-Claim Verification

- Agency-budget elided quote "would need ... argued rather than assumed": still verbatim at `concepts/agency-budget` L83 ("would need the no-signalling desideratum argued rather than assumed, because the classical coupling framework has no notion of measurement context at all"). An early probe with `cut -c1-600` falsely showed it as absent. A full-line read confirmed it is there.
- Multi-mind brain-to-brain falsifier: still at `concepts/multi-mind-collapse-problem` L139.
- [P-Q10](/positions/quantum-interface/#p-q10) N≥2 extension: present in `positions/quantum-interface` [P-Q10](/positions/quantum-interface/#p-q10) roadmap (2026-09-02). The link now targets `#^p-q10` directly instead of the apex.
- Born-rule article still calls the corridor the "endorsed working hypothesis" (L197 after the 10-02 fix), which is consistent with L41.

### Reasoning-mode classification (editor-internal)

- Engagement with QBism/RQM/many-minds (option c): Mode Three. The disagreement sits at the framework boundary and is now correctly located in objective single-outcome actualization, not in Tenet 4 for QBism and RQM.
- Engagement with superdeterminism-style coordination (option a): Mode Two. A coordinating law is shown to need either Bell-type nonlocal dependence or advance arrangement. The earlier wording named only superdeterminism, and the Bell-nonlocality horn was added (Medium 2).
- No label leakage found.

### Medium Issues Found

1. Lead and L41 left the corridor's Born-exactness unscoped ("long-run statistics stay exactly", "ensemble-invisible by construction"). **Fixed** by adding "unconditioned", matching tenets L75/L81 and [P-Q7](/positions/quantum-interface/#p-q7) (+3 words).
2. Option (a) said cross-agent coordination "has the structure of superdeterminism's measurement-dependence". That is one horn only. A law reproducing Born correlations for arbitrary settings must either make each selection answer to the far setting (Bell nonlocality) or be fixed in advance (measurement dependence). **Fixed.**
3. Demand 2 said wrong correlations are detectable "in a way marginal deviations are not". Marginal deviations are detectable too; the intended contrast is with marginal-*preserving* selection. **Fixed.**
4. Further Reading called `improper-vs-proper-mixtures` a "trilemma"; it has listed four live routes since 2026-09-10. **Fixed**, and route 1 is still objective collapse.

### Counterarguments Considered

- Everettian/relational dissolution: still bedrock (09-01 stability note honoured). This pass only corrected *which* Map commitment each dissolution costs.
- Controllable-outcome signalling (Shimony-style): considered as a sharpening of demand 3. It was not installed, because the per-context quantifier in `selection-only-channel` L76 and `agency-budget` L34 already blocks message-encoding through outcome selection for any publicly conditionable variable. Adding a citation-bearing paragraph would have gilded the article without closing a gap.

## Optimistic Analysis Summary

### Strengths Preserved

- The three-demands decomposition. The Torres Alegre rewrite makes the 2-versus-3 distinction sharper by giving a concrete case of wrong correlations without signalling.
- "Coverage before residue" in the interface-locality section (optimistic 2026-09-04's strongest point).
- The option space (a)–(d), each with its cost owned; the (d) plurality question is unchanged.
- The front-loaded double calibration and the "consistency, not corroboration" discipline.

### Enhancements Made

- The nested-agents case now reports the Map's actual commitment, the Q-restricting local-friendliness horn, with its conditionality and price. The closing conjecture's residue narrows to the cross-brain case.
- The sign problem's magnitude/direction point is extended to N > 1 in one sentence: where two corridors share one entangled state, a joint law must say whose selection fixes the outcome when they conflict. Optimistic 2026-09-04 had recorded this as an unminted argumentative gap.
- [P-Q7](/positions/quantum-interface/#p-q7) is wired in as the register entry that routes multi-agent joint no-signalling here.

### Cross-links Added

- [P-Q7](/positions/quantum-interface/#p-q7) (reciprocal; [P-Q7](/positions/quantum-interface/#p-q7) already linked here)
- [P-Q10](/positions/quantum-interface/#p-q10) (direct anchor replacing the apex proxy)
- [post-decoherence-selection §Local Friendliness](/concepts/post-decoherence-selection/#absolute-outcomes-and-the-local-friendliness-theorem) (reciprocal; L95 there already cites this article)
- [brain-interface-boundary](/concepts/brain-interface-boundary/)
- [sign-problem-for-conscious-observation](/concepts/sign-problem-for-conscious-observation/)
- [background-commitments](/tenets/background-commitments/)
- [local-tomography-and-the-consciousness-physics-interface](/concepts/local-tomography-and-the-consciousness-physics-interface/) (Further Reading; reciprocal of its L109)

Word count: 2639 → 2976 (+337). The draft reached 3015, above the 3000 soft threshold, and was trimmed back under it. Status `ok`.

## Remaining Items

- Out of scope, for the driver: "preregistered" Maier et al. (2018) wording survives in about 15 live loci. Examples are `concepts/ensemble-level-epiphenomenalism` L61, `topics/born-rule-and-the-consciousness-interface` L187, `topics/selection-only-mind-influence` L105 ("pre-registered Bayesian replication"), `positions/quantum-interface` L78 and `topics/parapsychology-firewall` L73. The 2026-09-24 apex fix verified the Frontiers paper carries no registration. The 09-01 review found that "pre-registered" in the raw HTML refers to Maier & Dechamps (J. Sci. Explor. 2018) Study 2, so some loci may intend that paper. Each locus needs disambiguation; a blind sweep-edit would be wrong. Not minted.

## Stability Notes

- The 09-01 notes stand. The Everettian/relational dissolution is bedrock, and the "unspecified / open debt" verdict must not be pushed toward resolution or refutation.
- The nested-agents answer is a *commitment* (the Q-restricting horn) conditional on baseline objective collapse. Future reviews should not upgrade it to "solved" or downgrade it back to "currently does not". Both directions misreport `post-decoherence-selection` L93–95.
- Tenet 4 binds many-minds only among the option (c) routes. QBism and RQM are declined over Posit Two (objective single-outcome actualization). Do not reattach them to Tenet 4.
- Torres Alegre is single-system. Any future wording that makes it bind joint statistics reintroduces Critical 1.