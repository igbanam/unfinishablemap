---
ai_contribution: 100
ai_generated_date: 2026-10-21
ai_modified: 2026-10-21 19:05:00+00:00
ai_system: claude-opus-5-5
author: Andy Southgate
concepts: []
created: 2026-10-21
date: &id001 2026-10-21
description: 'Tenet check 153: no Errors. An eight-family sweep found today''s repairs
  (closure, Born-preserving selection, Lowe, Posit Three) still missing from apex,
  argument and register pages outside the deep-review pool.'
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-10-21 19:05:00+00:00
modified: *id001
related_articles: []
title: Tenet Alignment Check - 2026-10-21
topics: []
---

# Tenet Alignment Check

**Date**: 2026-10-21. This is check 153. The previous one, [reviews/tenet-check-2026-10-20.md](/reviews/tenet-check-2026-10-20/), was check 152.

**Files checked**: 908 content files plus `tenets.md` and [tenets/background-commitments.md](/tenets/background-commitments/).
- **Scope.** Every `.md` file in `topics/` (355), `concepts/` (363), `positions/` (25), `apex/` (45), `voids/` (114) and `arguments/` (6). The one `.refinement-log` sidecar was excluded.
- **Method.** This check ran as a family sweep, set by the driver brief, not as a window diff. For each of the eight known defect families, a full-output regex scan ran over all 908 files. Every hit line in `apex/`, `positions/` and `arguments/` was then read in full. Hits in `topics/`, `concepts/` and `voids/` were read in context, at least ±250 characters around the match. No conclusion of absence rests on a truncated read. Each family has a positive control: a known instance, either queued or fixed today, that the scan had to find.
- **New pages today.** `topics/singular-thought-and-acquaintance`, `topics/protocol-analysis` and `topics/hempels-dilemma` were read in full in their Relation to Site Perspective sections.
- **Today's settled points**, checked on disk and not re-raised:
  - the intrinsic-nature recalibration (intrinsic-nature, russellian-monism, russellian-monism-versus-bi-aspectual-dualism, bi-aspectual-ontology);
  - the three Montero fixes;
  - Davidson's *strict*;
  - the Lowe/Kistler fixes on four-category-ontology;
  - Posit Three on phenomenology-of-moral-life L135.
- **Tenet 1 / Hempel.** The Tenet 1 wording problem is already the NEEDS-HUMAN doctrine P2 at todo L2814. It is cross-referenced below, not re-raised.
- **Quote checks.** Every quoted OLD string in the Priority List was confirmed by `grep -c -F`. Each occurs exactly once, at the line given. Lengths come from `tools.curate.length.analyze_length`. Headroom means hard threshold − 1 − count. Word deltas are whitespace counts.

**Errors**: 0

**Warnings**: 14 entries covering 63 distinct files, all of them Over-reach or calibration drift. No page contradicts a tenet.
- **Tier A (8 entries):** apex, arguments and positions.
- **Tier B (6 group entries):** topics, concepts and voids.

**Notes**: 12

## Summary

Today's repairs installed four settled wordings:
- **Closure.** Closure stated as sufficiency fails at a quantum indeterminacy, but closure stated as chance-fixing survives.
- **Born-preserving selection.** Consciousness biases *which* outcome actualises within the Born distribution. It does not bias "the probabilities".
- **Lowe.** Lowe holds free volitions uncaused. The agent-caused volition is the Map's addition.
- **Posit Three.** Many-worlds can restate deliberation branch-locally. What branching cannot supply is global exclusion, which the Map adopts as a posit.

Each wording now sits on the pages that were repaired. The sweep finds the older wordings intact on the pages nobody repaired. The worst-placed cases are on apex and argument pages that the deep-review pool cannot reach (`deep_review.py` excludes apex, voids and positions).

Four findings stand out:
- **`apex/minds-without-words` L141** has the clearest Tenet 3 evidential overclaim left in an apex. It says "provides positive evidence for consciousness doing causal work", and adds that a meta-analysis "strengthens this". `tenets.md` says the same comparative-cognition evidence "corroborates the tenet rather than establishing it".
- **`arguments/epiphenomenalism-argument` L201–L215**, the "Against Epiphenomenalism" page, makes two errors:
  - it denies causal closure with no chance-fixing concession;
  - it says "the arguments against epiphenomenalism depend on collapse being real". `tenets/background-commitments` (Posit Three) says the opposite: an Everettian dualist can grant mental causation.
- **`apex/moral-architecture-of-consciousness` L190** repeats the queued `ethics-under-dualism` L206 opening word for word ("No Many Worlds preserves moral urgency"). It ends on "Graded responsibility requires singular outcomes", the flat reading that Posit Three retired. It is not in the queued three-page sweep.
- **`apex/consciousness-and-agency` L101** says "E.J. Lowe goes further" than the agent-causal terminus. That reads Lowe as an agent-causalist, though he holds volitions uncaused. The apex has no Lowe correction anywhere.

Family by family:
- **Biasing probabilities.** Six Map-voice pages describe Tenet 2 as "biasing probabilities". The worst is `concepts/emergence` L175, which also calls Tenet 2's constraint "parsimony". `tenets.md` says Tenet 2's minimality "is not the kind of minimality Tenet 5 declares unreliable."
- **Closure.** Twenty concept and topic pages state the quantum defeat of closure or Kim with no chance-fixing concession. The positions register is the source: [P-MC3](/positions/arguments-for-mental-causation/#p-mc3) says "The Map denies (2)" with no scope. The tenets page itself, at L67 (Tenet 2 Rationale), states closure only as sufficiency.
- **Davidson and photosynthesis.** No new hits. Every Davidson hit is queued, and the 2026-10-20 synthesis already ruled on the photosynthesis residue.

## Method: counts per family, with controls

| # | Family | Regex hits (lines / files) | After reading: new defect loci | apex / positions / arguments | Positive control (found?) |
|---|---|---|---|---|---|
| 1 | Tenet 3 evidential overclaim | 116 / ~90; 28 hedged on-line | 16 concept/topic/void files + 2 apex files (+7 nav labels/headings, Note 6) | 3 apex loci (minds-without-words L141, L115; phenomenology-of-consciousness-doing-work L183) | `concepts/epistemic-emotions` L135 (queued L2680) ✓; `topics/phenomenology-of-resistance-across-domains` L39 (queued L2720) ✓ |
| 2 | Closure as sufficiency only | 134 / 80; 8 of those files carry a concession somewhere | 20 concept/topic files + `tenets.md` L67 | apex what-consciousness-tells-us-about-physics L232; arguments/epiphenomenalism-argument L201/L211; positions/arguments-for-mental-causation L46/L81 | `concepts/mental-causation-and-downward-causation` L111/L115 (queued L2742) ✓; concession detector caught phenomenology-mechanism-bridge L114/L132 and hempels-dilemma L115 ✓ |
| 3 | "Biasing probabilities" vs [P-Q2](/positions/quantum-interface/#p-q2) | 51 + 23 variant / 46 | 6 files, 9 loci (+3 Notes) | 0 | `mental-causation-and-downward-causation` L200 (queued L2742) ✓ |
| 4 | Photosynthesis as precedent | 85 / 31 | 0 new Warnings (1 Note) | 0 (machine-question L147, research-programme L96 already carry the retreat) | decoherence-and-macroscopic-superposition L31/L85 ✓. Blind spot: that file's queued L75 (todo L2577) uses no keyword. |
| 5 | Lowe read as agent-causalist | 94 body mentions / 23 files (four-category-ontology excluded) | 1 Warning + 2 Notes | apex consciousness-and-agency L101 | agent-causation L83 (queued L2756) ✓; fixed phenomenology-mechanism-bridge L130 ✓ |
| 6 | Davidson without "strict" | 37 targeted + 14 broad (every Davidson+law line lacking "strict") | **0 new** | 0 (no Davidson in positions; apex hits are R. J. Davidson the neuroscientist) | the three queued loci, philosophy-of-action L45, supervenience L131, type-token-causation L159 (todo L2799) ✓ |
| 7 | MWI dissolves deliberation (vs Posit Three) | 145 / ~110; 50 marked calibrated on-line | 11 files + 1 apex (moral-architecture L190, found by a separate apex/positions probe without the dissolution-verb filter) + arguments L215 | apex moral-architecture L190; arguments/epiphenomenalism-argument L215 | ethics-under-dualism L206, nihilism-and-existentialism L130, normative-void L126 (queued L2777) all ✓; fixed phenomenology-of-moral-life L135 correctly *not* hit |
| 8 | Tenet 5 as refutation of non-parsimony arguments | 463 Tenet-5-plus-refutation-verb lines; 129 with ≤1 parsimony word; 22 aimed at a non-parsimony target | 6 files (+4 Note loci, 2 of them apex; apex L175 sits in Warning 8) | 0 Warnings in positions (all 13 hits calibrated) | hempels-dilemma L115 and anomalous-monism L79 (correct uses) detected ✓; check 151's minds-without-words L157 instance now reads 0 (fixed) |

Every regex count is lexical and an upper bound. The "after reading" column is a lower bound: it holds what reading confirmed, not proof that nothing else exists.

## Errors

None. No page endorses eliminativism, epiphenomenalism, many-worlds, quantum woo, or parsimony as decisive against dualism.

## Warnings

### A. Apex, arguments and positions

#### 1. `apex/minds-without-words` L141: Tenet 3 evidential overclaim plus an undiscriminated "fits well"
- **Family**: 1. Ladder rung earned: **compatible**.
- **Quote**: "Multiple independent origins across vertebrates, cephalopods, and arthropods fit poorly with emergence from specific neural structures and well with interface dualism. The type-specific correspondence between consciousness-dependent capacities and the human-ape gap provides positive evidence for consciousness doing causal work. The Streicher et al. (2025) meta-analysis strengthens this — genuinely unconscious processing is more limited than assumed."
- **Issue**: Convergent origins are predicted equally by functionalist physicalism, so "well with interface dualism" names no discriminator. "Provides positive evidence" sits above `tenets.md` L97, which grades the baseline-cognition correspondence "suggestive but contested corroboration". The same paragraph records the epiphenomenalist's structural counter, that one substrate could produce both. Streicher et al. narrows unconscious processing. It does not choose between the causal and the parallel readings. The page's own L101 uses Streicher only to say unconscious processing is limited.
- **Recommendation**: Priority 1.

#### 2. `apex/minds-without-words` L115: asymbolia as "evidence for" Bidirectional Interaction
- **Family**: 1.
- **Quote**: "evidence for [Bidirectional Interaction](/tenets/#bidirectional-interaction), not a demonstration of it."
- **Issue**: The sentence first says asymbolia "constrains identity readings of valence rather than establishing that phenomenal properties do real causal work". It then upgrades that to evidence for Tenet 3. A constraint on identity theories of valence fits Tenet 3 without evidencing it, because the co-optimization reply absorbs it.
- **Sibling**: `topics/emotion-and-dualism` L57 makes the same move. Its "though all functional machinery remains intact" is also at odds with the open P3 at todo L2641, which says asymbolia impairs avoidance.
- **Recommendation**: Fold into Priority 1's task. Replace "evidence for Bidirectional Interaction, not a demonstration of it." with "which fits Bidirectional Interaction without evidencing it." (−2). Emotion-and-dualism L57 is a secondary file.

#### 3. `apex/moral-architecture-of-consciousness` L190: graded responsibility "requires singular outcomes"
- **Family**: 7.
- **Quote**: "Graded responsibility requires singular outcomes: desert attaches to *this* agent's *this* choice in *this* world."
- **Issue**: `tenets/background-commitments` Posit Three says ownership of the actual action and reasons-responsiveness "are available branch-locally". What separates the Map from Everett is the posited global exclusion. The paragraph's first sentence ("No Many Worlds preserves moral urgency") is identical to queued `ethics-under-dualism` L206. The apex was not among that sweep's three candidates, and apex pages are outside the deep-review pool.
- **Recommendation**: Priority 3.

#### 4. `apex/consciousness-and-agency` L101: Lowe "goes further" than the agent-causal terminus
- **Family**: 5.
- **Quote**: "E.J. Lowe goes further: *all* causation is fundamentally [substance causation](/concepts/agent-causation/#substance-causation-the-metaphysical-foundation), so agent causation is paradigmatic rather than exceptional, a conclusion Whitehead's [process philosophy](/concepts/process-philosophy/) reaches from different premises."
- **Issue**: "Goes further" follows the claim that "the agent selected for reasons" is a legitimate terminus. That places Lowe inside the agent-causal camp. Lowe holds free volitions wholly uncaused and denies that reasons are causes. The corrected wording is on `apex/phenomenology-mechanism-bridge` L130 and `topics/philosophy-of-action-under-dualism` L77. This apex has no other Lowe line and no Lowe correction. The trailing Whitehead clause is loose, because Whitehead's premises are anti-substance (Note 9).
- **Recommendation**: Priority 4.

#### 5. `arguments/epiphenomenalism-argument` L201, L211, L215: unconceded closure defeat, and a dependency Posit Three denies
- **Families**: 2 and 7.
- **Quotes**:
  - L201: "The Map's response: deny causal closure at quantum indeterminacies. … At these points, physics is genuinely incomplete. Consciousness can cause physical events precisely where physics leaves room."
  - L211: "it operates precisely where [causal-closure](/concepts/causal-closure/) doesn't apply—at quantum indeterminacies."
  - L215: "The arguments against epiphenomenalism depend on collapse being real: consciousness causes *this* outcome rather than *that*."
- **Issue**: The page states the closure defeat with no chance-fixing concession anywhere in the file, against the wording installed today on `concepts/causal-exclusion-argument` L79/L88 and `apex/phenomenology-mechanism-bridge` L114/L132. L215 makes the anti-epiphenomenalist arguments depend on collapse. Posit Three says conscious causation "is not the point of difference either: an Everettian dualist could grant that mind makes a causal difference and keep the branching". Only the Map's *selection* reply needs collapse.
- **Lesser point**: L207 ("The arguments against epiphenomenalism directly support the Map's framework") is mild Family-1 phrasing. It is left as is.
- **Recommendation**: Priority 2.

#### 6. `positions/arguments-for-mental-causation` [P-MC3](/positions/arguments-for-mental-causation/#p-mc3) L81 and L46: the register's denial of closure is unscoped
- **Family**: 2.
- **Quotes**:
  - L81: "The Map denies (2): physics is ontologically incomplete at quantum indeterminacies, and consciousness biases which physically permissible outcome actualises."
  - L46: "by denying that physical events always have sufficient physical causes".
- **Issue**: [P-MC3](/positions/arguments-for-mental-causation/#p-mc3)'s gravity-well diagnostic is stated only in sufficiency form. Restated with chance-fixing closure, the Map stays inside the well, and that remaining pressure is exactly [P-Q3](/positions/quantum-interface/#p-q3). The entry points at the mechanism debt ("inherits the quantum-interface mechanism debt in full") but never says which closure it escapes. Three pages copy this diagnostic: `topics/the-epiphenomenalist-threat` L127/L135, `concepts/nondualistic-interactionism` L87 and `topics/self-stultification-as-master-argument`. The register is therefore the source of much of the Family-2 tail in Group B.
- **Recommendation**: **Fold-in, not a new task.** The file is 3,321 against a positions hard threshold of 2,500. It is already blocked by the P2 HUMAN LENGTH DECISION on positions-register seams (todo, [P-D2](/positions/arguments-for-dualism/#p-d2) / [P-MC3](/positions/arguments-for-mental-causation/#p-mc3), Status: blocked). Append this as a third seam:
  - L81 OLD → "The Map denies (2) in its sufficiency form only: physics is ontologically incomplete at quantum indeterminacies, and consciousness biases which physically permissible outcome actualises. Stated as chance-fixing, (2) survives, since exact Born preservation ([P-Q2](/positions/quantum-interface/#p-q2)) leaves physics fixing every chance; whether settling an outcome without shifting its chance supplies the missing difference-making point is the open [P-Q3](/positions/quantum-interface/#mechanism-debt) question." (+38)
  - L46: add "(sufficiency, not chance-fixing, closure)" (+4).
  - A dated Updated note (+~29).
  - Net about +71. It cannot be done length-neutrally.

#### 7. `apex/what-consciousness-tells-us-about-physics` L232: "causal closure fails precisely at measurement"
- **Family**: 2.
- **Quote**: "If this picture is correct, causal closure fails precisely at measurement, because measurement is where physics meets its complement."
- **Issue**: The sentence is conditional but unscoped. No chance-fixing concession appears in the file. Its L112 is fine, because it uses Saad's universal/observational split.
- **Recommendation**: "…causal closure stated as sufficiency fails precisely at measurement, while closure stated as chance-fixing survives, because…" (+9). Low priority. The apex has 4,9xx words; measure before tasking.

#### 8. `apex/phenomenology-of-consciousness-doing-work` L183 (label) and L175
- **Families**: 1 and 8.
- **Quotes**:
  - L183: "Why natural selection provides evidence that consciousness does real causal work".
  - L175: "Sometimes the more complex explanation — that consciousness does genuine work and its phenomenology tracks that work — fits the evidence better."
- **Issue**: The Further Reading label carries the claim that the 10-19 co-optimization rewrite withdrew from the evolutionary case; check 152's Warning 2 was the same family. L175 sits in the Tenet 5 paragraph and runs anti-parsimony forward as evidence. The matrix in `tenets.md` (L172, conceivability row) says the self-binding forbids that.
- **Recommendation**: L183 label → "Why natural selection bears on whether consciousness does real causal work" (+0). For L175, cut "fits the evidence better" down to "may be correct" (−2). Headroom is 301.

### B. Topics, concepts and voids, grouped by family

#### 9. Family 3: Tenet 2 described as "biasing probabilities" in the Map's own voice (6 files, 9 loci)
[P-Q2](/positions/quantum-interface/#p-q2) (credence high) says the interaction "biases *which* outcome becomes actual, but outcome frequencies stay Born-exact". These pages put the bias on the probabilities themselves:
- **`concepts/emergence`** (headroom 545). The worst of the set, because it also gets Tenet 5 wrong:
  - L175: "The constraint is parsimony: consciousness biases probabilities rather than injecting energy." `tenets.md` L69 says Tenet 2's minimality is empirical-constraint minimality, "not the kind of minimality Tenet 5 declares unreliable".
  - L109: "The Minimal Quantum Interaction tenet locates consciousness's influence here—biasing probabilities rather than injecting energy."
- **`concepts/cumulative-culture`** L204 (headroom 161): "…the smallest possible intervention—biasing quantum probabilities rather than introducing new energy." The same file's L36 is a Family-1 overclaim (entry 12).
- **`concepts/islamic-sufi-philosophy-of-consciousness`** L103 (headroom 958): "…the Map's model of consciousness biasing quantum probability distributions."
- **`concepts/substance-property-dualism`** L173: "…an irreducible property (of what?) biasing probabilities."
- **`topics/consciousness-and-causal-powers`** (headroom 26):
  - L84: "consciousness shifting probabilities against statistical noise…";
  - L136: "since biasing probabilities leaves voluntary action able to fail".
- **`voids/tenet-generated-voids`** (headroom 500):
  - L63: "*How* does a non-physical influence bias quantum probabilities?";
  - L65: "…can alter probability distributions over physical outcomes."

Excluded after reading, because they are attributions or explicitly outside the corridor: Beck–Eccles (amplification-mechanisms L73, history-of-the-interaction-problem L110, popper L70, conservation-laws L121), the coupling-modes and channel-class taxonomies, the probability-bias channels (brain-internal-born-rule-testing L68, sorkin-delta L81), and the-psychophysical-control-law's Eccles controller.

Recommendation: the "Next in line" item below.

#### 10. Family 7: branching said to dissolve deliberation, choice-weight or moral meaning, stated flat rather than as the global-exclusion posit (8 files)
- `concepts/anoetic-noetic-autonoetic-consciousness` L130: "If every plan is executed by countless branching copies, the felt urgency of deliberation loses its rational basis." This is the most direct, since Posit Three says deliberation "is reasons-responsive" branch-locally.
- `concepts/consciousness-as-amplifier` L179: "the phenomenology of settling … becomes illusory".
- `topics/authentic-vs-inauthentic-choice` L200: "dissolving the weight that authentic choice carries".
- `topics/consciousness-and-cognitive-distinctiveness` L188: "Many-worlds eliminates this distinction". Headroom is 15.
- `topics/consciousness-and-normative-force` L163: "Many-worlds dissolves this … Deliberation matters because *this* agent…".
- `topics/phenomenal-value-realism` L181: "moral urgency dissolves". Headroom is 20.
- `topics/purpose-and-alignment` L151: "alignment loses its normative force".
- `topics/analytic-idealism-and-mind-centric-metaphysics` L128: "your choices don't genuinel[y matter]".

`topics/meaning-of-life` L102 ("threatens to dissolve") and `topics/pragmatisms-path-to-dualism` L169 (which names the non-deflationary-subject presupposition) are hedged enough to pass. Lines saying MWI leaves nothing for *outcome-selection* to do pass, because Posit Three agrees that "outcome-selection needs an outcome to be excluded". These include motor-selection L210, interface-friction L118, valence-and-conscious-selection L208 and quantum-neural-timing L175.

Recommendation: a P3 sweep after the queued L2777 lands, transferring its settled second sentence.

#### 11. Family 7, stronger form: "MWI eliminates mental causation" (3 files)
These go further than the deliberation family. They contradict Posit Three's explicit sentence that conscious causation "is not the point of difference".
- `topics/quantum-measurement-and-consciousness` L128: "[mental causation](/concepts/mental-causation-and-downward-causation/) is eliminated independently of whether probability is rescued: if every choice branches into all alternatives, preferring one cannot differentially bring it about". Headroom is 401.
- `concepts/measurement-problem` L117, objection (3): "eliminates [mental causation](/concepts/mental-causation-and-downward-causation/)". The file is 3,653, already over the hard threshold of 3,500.
- `concepts/prebiotic-collapse` L106: "MWI eliminates the causal role for consciousness entirely". The file is 3,605, already over hard.

Recommendation: scope each to "eliminates outcome-selection, the Map's mechanism; a branching dualist would route mental causation elsewhere ([Posit Three](/tenets/background-commitments/))". The two concept files need net-negative edits.

#### 12. Family 1: Map-voice Tenet 3 evidential claims where the fix is "fits the tenet without evidencing it" (16 files)
- `concepts/cumulative-culture` L36: "provides strong evidence for the … Bidirectional Interaction tenet".
- `concepts/direction-of-fit` L33: "The Unfinishable Map holds that direction of fit … provides evidence for the … Bidirectional Interaction tenet".
- `concepts/jourdain-hypothesis` L129: "the human-ape gap provides evidence that consciousness causally contributes".
- `concepts/theory-of-mind` L164: "Theory of mind provides evidence".
- `concepts/phenomenal-depth` L86: "gains support".
- `concepts/quantum-biology-and-neural-mechanisms` L126: "Consciousness could bias tunneling probabilities, influencing which synapses fire—directly supporting [Bidirectional Interaction](/concepts/interactionist-dualism/)". This is also Family 3. Headroom is 50.
- `topics/consciousness-and-the-physics-of-information` L108: "gain support".
- `topics/consciousness-in-simple-organisms` L255: "The UAL framework strongly supports the view … its correlation with flexible learning would be inexplicable". The co-optimization reply explains exactly that correlation.
- `topics/phenomenology-of-cognitive-capacity` L119: "The Map interprets this as evidence for bidirectional interaction."
- `topics/phenomenology-of-intellectual-life` L214: "gains support from the causal efficacy of intellectual effort".
- `topics/phenomenology-of-linguistic-failure` L123: "requires consciousness to causally interact".
- `topics/self-reference-and-the-limits-of-physical-description` L136: "supports bidirectional causation".
- `topics/emotion-and-dualism` L57: see entry 2.
- `topics/phenomenology-of-resistance-across-domains` L117: "The Map takes resistance as phenomenological evidence for bidirectional causation … An epiphenomenal consciousness could not encounter resistance". This is the same page as queued L2720 (L39) and should be folded into that task.
- `voids/disappearance-voids` L164: "demonstrating that consciousness actively selects its own mode of operation".
- `voids/acquaintance-void` L146: "that it shapes behaviour suggests a genuine causal relation". This is mild.

Already queued, so not re-listed: epistemic-emotions L135, phenomenology-of-resistance L39, bidirectional-interaction L119.

#### 13. Family 2: the quantum defeat of closure or Kim stated with no chance-fixing concession (20 files)
None of these files contains the concession anywhere. Each needs the one-clause addition: closure stated as chance-fixing survives, and whether settling counts as causing is [P-Q3](/positions/quantum-interface/#p-q3).
- concepts: `agent-causation` L89, `bi-aspectual-ontology` L76, `bidirectional-interaction` L132 (headroom 1), `measurement-problem` L161, `meta-problem-of-consciousness` L115, `objections-to-interactionism` L157 and L190, `philosophy-of-mind` L73 ("quantum mechanics undermines it"), `psychophysical-laws` L108 ("consciousness causes collapse without violating closure"), `quantum-indeterminacy-free-will` L152 ("with neither overdetermination nor exclusion"; headroom 3), `reasons-responsiveness` L114, `reductionism` L188, `supervenience` L101, `type-token-causation` L76, L80, L90 and L96 (L90: "Quantum mechanics already supplies the denial."), `interactionist-dualism` L191, `agent-teleology` L124, `consciousness-bandwidth-architecture` L141, `mind-arena` L55.
- topics: `consciousness-and-integrated-information` L76 and L80, `the-epiphenomenalist-threat` L133, L135 and L180 (copies [P-MC3](/positions/arguments-for-mental-causation/#p-mc3)), `philosophy-of-action-under-dualism` L93 ("This dissolves the exclusion worry").

The hub-first order is `type-token-causation`, then `the-epiphenomenalist-threat`, then `quantum-indeterminacy-free-will`. Several are at their length lines, so the sweep must be clause-sized and run in batches.

#### 14. Family 8: Tenet 5 aimed at arguments that do not rest on parsimony, or run forward as evidence (6 files)
- `concepts/decoherence` L199: "The decoherence objection was taken as decisive partly because dismissing quantum consciousness seemed simpler than investigating whether biology might manage decoherence." Tegmark's objection is a calculation, and Tenet 5 cannot answer it. The tenet bears only on a further step from "coherence is implausible" to "interaction is the less economical hypothesis". Headroom is 15, so any edit must be net-negative.
- `topics/brain-computer-interfaces-and-the-interface-boundary` L151: Tenet 5 is aimed at "just neural plasticity", an explanatory account and not a simplicity claim.
- `topics/consciousness-and-normative-force` L165: Tenet 5 is aimed at evolutionary debunking.
- `topics/evaluative-qualia-phenomenal-normativity-across-traditions` L130: "demands an explanation at least as complex as accepting evaluative qualia". This counts complexity forward inside the Tenet 5 paragraph.
- `concepts/introspection` L167: "The … Occam's Razor Has Limits tenet gains support from training literature". A parsimony tenet cannot gain support from introspection-accuracy data.
- `voids/what-voids-reveal` L148: "Occam's Razor Has Limits is supported on the methodological front".

## Notes

1. **`tenets.md` L67 (Tenet 2 Rationale) states closure only as sufficiency.** The text: "Crucially, this tenet rejects the strong causal closure of physics that [epiphenomenalism](/concepts/epiphenomenalism/) depends on: the claim that every physical event has a sufficient physical cause. Physics is *not* complete at quantum indeterminacies—and that's where consciousness acts." (count 1). Today's concession lives only on dependents: causal-closure L138, causal-exclusion-argument L79/L88, phenomenology-mechanism-bridge, hempels-dilemma, four-category-ontology and materialism-argument. Downstream pages copy the tenet text, so the tail in entry 13 will regrow unless the source carries the scope. This is doctrine-level text. It belongs as an **addendum to the NEEDS-HUMAN doctrine P2 at todo L2814** (Tenet 1 / Hempel), not as a new task. Suggested clause: "Closure stated as chance-fixing is untouched: Born-preserving selection ([P-Q2](/positions/quantum-interface/#p-q2)) grants it, and the Map's claim is the token-level one about which outcome is actual, whose causal standing is [P-Q3](/positions/quantum-interface/#p-q3)."
2. **Photosynthesis residue: settled, not re-raised.**
   - The 2026-10-20 synthesis ([reviews/outer-review-synthesis-2026-10-20.md](/reviews/outer-review-synthesis-2026-10-20/) L72) deliberately left `concepts/libet-experiments` L129 (hedged) and `voids/amplification-void` L45 (no coherence claim). That is respected here.
   - One narrow tension remains. `concepts/objections-to-interactionism` L111 says light-harvesting coherence "survives longer than naive thermal estimates predicted". `topics/decoherence-and-macroscopic-superposition` L85 says "the orthodox picture of light harvesting already expected coherence this brief". The line's use, loosening the categorical "warm forbids coherence" assumption, is the use `concepts/quantum-biology-and-neural-mechanisms` L68 allows. The tension is a factual nicety, not precedent drift.
3. **Lowe, lesser loci.**
   - `concepts/agent-causation` L95 lists "**Lowe** (2008)" in the agent-causation lineage (Reid, Chisholm, O'Connor, Lowe, Hasker). The sentence itself is accurate, and the L83 correction sits two paragraphs above.
   - `topics/event-causal-libertarianism` L80 lists Lowe among "Defenders" replying to the agent-causal timing objection. Its own L68 has the correction.
   - `topics/causal-closure-debate-historical-survey` L101 glosses Lowe (2000) as "influencing outcomes rather than injecting forces — then even the strongest plausible closure principles would leave room". This is unverified. It is a lead only, not to be cited until read in the raw text. The Montero repair at L99 did not touch it.
4. **Family 2 apex loci that pass or nearly pass.**
   - `apex/consciousness-and-agency` L127 passes. Its L131 carries "Born-preserving selection leaves probabilistic closure intact".
   - `apex/attention-as-causal-bridge` L185 passes ("closure holds only probabilistically—fixing the statistics").
   - `apex/dualism-cartography` L93 passes ("the dynamics fix the probability distribution but leave the token open").
   - `apex/interface-specification-programme` L108 says "Kim's exclusion objection does not need to be answered so much as dissolved" with the aggregate statistics fixed. There is no [P-Q3](/positions/quantum-interface/#p-q3) pointer in the paragraph, but the file is 5,108, over its hard threshold of 5,000.
   - `apex/judging-the-map-as-science` L58 ("the causal closure the Map denies") is overbroad by one word.
   - Neither failing locus is tasked.
5. **Family 3, mild loci.**
   - `voids/causal-interface` L148 ("how something non-physical biases quantum probabilities") is a void's resolution condition.
   - `topics/amplification-mechanisms-consciousness-physics` L109 ("it tilts probabilities") is reconciled in its next sentence.
   - `concepts/epistemology` L83 ("that it alters probabilities — the Map takes the third in the restricted form … within the Born distribution") is a wording tension only.
6. **Family 1 headings and navigation labels.** These carry the claim, but renaming a heading breaks its anchor:
   - `concepts/implicit-memory` L77 heading "Choking Under Pressure: Evidence for Bidirectional Interaction" is anchor-linked from `concepts/global-workspace-theory` L144. Rename both together.
   - `topics/consciousness-and-counterfactual-reasoning` L72 heading.
   - Labels at implicit-memory L198, skill-delegation L146, `voids/expertise-and-its-occlusion` L144, volitional-control L168 and philosophy-of-science-under-dualism L135.
7. **Family 8, apex forward-running** (Tenet 5 paragraphs that assert explanatory superiority):
   - `apex/testing-the-map-from-inside` L258 ("Saying 'it's just what brain states feel like' doesn't explain the specific structure");
   - `apex/living-with-the-map` L204 ("The framework is complex because consciousness is complex");
   - `concepts/neurophenomenology-and-contemplative-neuroscience` L201 and `concepts/intersubjectivity` L126 are the same move.
   - Each is defeater-removal phrased as support.
8. **Positions Tenet 5 usage is clean.** All 13 positions hits state Tenet 5 as symmetric, a defeater-remover that never upgrades a tier ([P-M1](/positions/methodology-and-calibration/#p-m1), [P-CS5](/positions/consciousness-scope/#p-cs5), P-VS, [P-Q11](/positions/quantum-interface/#p-q11)). No change.
9. **Co-optation firewall.**
   - `concepts/process-philosophy` L158 ("Process philosophy strongly supports the claim that experience makes a difference") passes the firewall, because L152–L154 state Whitehead's processual monism. "Supports" there means *endorses*, not *evidences*, and could read "holds" for clarity.
   - The Whitehead clause at `apex/consciousness-and-agency` L101 credits anti-substance premises with a substance-causation conclusion. Priority 4's wording keeps the clause, and a later apex pass should decide whether to drop it.
10. **Today's new pages are clean.**
    - `topics/singular-thought-and-acquaintance`: Campbell is flagged "no interactionist", and the Bidirectional paragraph "fits the tenet without evidencing it".
    - `topics/protocol-analysis`: "fits both tenets without evidencing either".
    - `topics/hempels-dilemma`: carries the full chance-fixing concession and binds Tenet 5 symmetrically against Gyenis's razor.
11. **Check 152 carry-over.**
    - Fixed since check 152: its Warning 2 (`concepts/bidirectional-interaction` "positive support", 0 hits) and Warning 3 (`voids/attention-and-consciousness` "Every attention void is evidence of mental causation", 0 hits).
    - Still live: Warning 1 (`topics/self-stultification-as-master-argument` L169 "cannot be rationally held") and Warning 4 (`concepts/selective-correction-and-reconstruction-paradox` L109 "the cleanest case of conscious influence", count 1).
12. **Scan limitations, stated so the zeros are not over-read.**
    - The Family 4 regex cannot see `topics/decoherence-and-macroscopic-superposition` L75 (queued, todo L2577), which uses no keyword.
    - The Family 7 calibration-marker regex tags `topics/motor-control-quantum-zeno` L129, the queued sweep's own reference wording, as uncalibrated. It was read and judged compliant.
    - Family 6's zero rests on two probes: the targeted pattern, plus every line co-mentioning Davidson and "law" without "strict". Both returned only the queued loci or compliant lines.

## Files Passing All Checks

This was a family sweep, not a full read of 908 files, so "passing" here means: **no hit in any of the eight families survived reading**. Read in full or in their tenet sections and found clean:
- **Today's new pages:** `topics/singular-thought-and-acquaintance`, `topics/protocol-analysis`, `topics/hempels-dilemma`.
- **Today's recalibrated pages:** `concepts/intrinsic-nature`, `concepts/russellian-monism`, `topics/russellian-monism-versus-bi-aspectual-dualism`, `concepts/bi-aspectual-ontology`.
- **Today's fixed pages:** `concepts/four-category-ontology`, `concepts/anomalous-monism-and-the-denial-of-strict-psychophysical-laws`, `topics/phenomenology-of-moral-life` (L135), `concepts/causal-exclusion-argument`, `apex/phenomenology-mechanism-bridge`.
- **Earlier pages that already carried the wordings:** `apex/born-preserving-causal-efficacy`, `apex/one-world-wager`, `apex/research-programme-decisions-under-the-map`, `apex/steelmanning-as-method`, `apex/moral-status-of-edge-cases`, `apex/attention-as-causal-bridge`, `apex/dualism-cartography`.
- **Positions** (on Families 1, 3, 4, 5, 6, 7 and 8; only [P-MC3](/positions/arguments-for-mental-causation/#p-mc3) fails Family 2): `positions/quantum-interface`, `positions/agency-and-will`, `positions/arguments-for-dualism`, `positions/methodology-and-calibration`, `positions/consciousness-scope`, `positions/value-in-selection`.

## Priority List

Each OLD string below was confirmed with `grep -c -F` = 1 at the line given.

1. **`apex/minds-without-words` L141 (+ L115).** Family 1 and Over-reach. 4,115 against apex hard 5,000, so headroom is 884.
   - OLD (L141, a): `Multiple independent origins across vertebrates, cephalopods, and arthropods fit poorly with emergence from specific neural structures and well with interface dualism.`
   - NEW: `Multiple independent origins across vertebrates, cephalopods, and arthropods fit poorly with emergence from specific neural structures, though functionalist physicalism predicts them as readily as interface dualism does.` (+6)
   - OLD (L141, b): `The type-specific correspondence between consciousness-dependent capacities and the human-ape gap provides positive evidence for consciousness doing causal work. The Streicher et al. (2025) meta-analysis strengthens this — genuinely unconscious processing is more limited than assumed.`
   - NEW: `The type-specific correspondence between consciousness-dependent capacities and the human-ape gap fits consciousness doing causal work without evidencing it, since an epiphenomenalist reads it as the substrate's work, the counter [[tenets#^bidirectional-interaction|Tenet 3's rationale]] records. The Streicher et al. (2025) meta-analysis sharpens the correspondence — genuinely unconscious processing is more limited than assumed — without choosing between those readings.` (+22)
   - OLD (L115): `evidence for [[tenets#^bidirectional-interaction|Bidirectional Interaction]], not a demonstration of it.`
   - NEW: `which fits [[tenets#^bidirectional-interaction|Bidirectional Interaction]] without evidencing it.` (−2)
   - Net: **+26**.
   - Secondary file: `topics/emotion-and-dualism` L57, the same move. Its "though all functional machinery remains intact" conflicts with todo L2641, so coordinate with that task.
   - Guard: do not concede epiphenomenalism. The fix only narrows the evidential grade.
2. **`arguments/epiphenomenalism-argument` L201, L211, L215.** Families 2 and 7. 2,950 against arguments hard 3,500, so headroom is 549.
   - OLD: `The Map's response: deny causal closure at quantum indeterminacies.`
   - NEW: `The Map's response: deny causal closure, stated as sufficiency, at quantum indeterminacies.` (+3)
   - OLD: `Consciousness can cause physical events precisely where physics leaves room.`
   - NEW: the same sentence, plus `Closure stated as chance-fixing survives, since exact Born preservation leaves physics fixing every chance; whether settling which outcome is actual counts as causing it is the open [[positions/quantum-interface#^mechanism-debt|bias-without-deviation question]].` (+29)
   - OLD: `it operates precisely where [[causal-closure]] doesn't apply—at quantum indeterminacies.`
   - NEW: `it operates where [[causal-closure]] stated as sufficiency doesn't apply—at quantum indeterminacies.` (+2)
   - OLD: `The arguments against epiphenomenalism depend on collapse being real: consciousness causes *this* outcome rather than *that*.`
   - NEW: `The Map's selection reply depends on collapse being real: consciousness settles *this* outcome rather than *that*. The self-stultification argument does not, since an Everettian dualist could grant mental causation and route it elsewhere ([[tenets/background-commitments|Posit Three]]).` (+19)
   - Net: **+53**.
   - Coordination: the pending P3 on the same file (L109/L115/L131/L139/L142, net +35, from [reviews/optimistic-2026-10-16-self-stultification-repair-wing.md](/reviews/optimistic-2026-10-16-self-stultification-repair-wing/)) touches different lines. Combined net +88 against 549. Either fold the two tasks together or run them back to back.
3. **`apex/moral-architecture-of-consciousness` L190.** Family 7. 4,569 against apex hard 5,000, so headroom is 430.
   - OLD: `Graded responsibility requires singular outcomes: desert attaches to *this* agent's *this* choice in *this* world.`
   - NEW: `Graded responsibility can be restated branch-locally: within each branch, desert attaches to that agent's choice. What branching cannot supply is the global exclusion of the unchosen options, which the Map adopts as a [[tenets/background-commitments|posit]] rather than derives from desert.` (**+24**)
   - The new second sentence is the settled `phenomenology-of-moral-life` L135 sentence, adapted.
   - The cheapest way to do this is to **append it to the queued P3 sweep (todo L2777) as a fourth file**, since its opening sentence is identical to that sweep's primary locus, `ethics-under-dualism` L206. Mint a standalone task only if that sweep has already been picked.
4. **`apex/consciousness-and-agency` L101.** Family 5. 4,921 against apex hard 5,000, so headroom is 78.
   - OLD: `E.J. Lowe goes further: *all* causation is fundamentally [[agent-causation#Substance Causation: The Metaphysical Foundation|substance causation]], so agent causation is paradigmatic rather than exceptional, a conclusion Whitehead's [[process-philosophy|process philosophy]] reaches from different premises.`
   - NEW: the same sentence, plus `Lowe stops short of the Map's step, though: he holds free volitions wholly uncaused, so the agent-caused choice is the Map's addition ([[philosophy-of-action-under-dualism]]).` (**+23**)
   - Linking, not citing, avoids a new References entry. The apex has no Lowe reference and no existing link to philosophy-of-action-under-dualism.
   - Optional, at zero words: `goes further` → `generalises the point`.

**Next in line, if a slot opens: the Family 3 sweep.** Primary file `concepts/emergence` (2,954 against concepts hard 3,500, headroom 545).
- **Primary file:**
  - L175 OLD `The constraint is parsimony: consciousness biases probabilities rather than injecting energy.` → `The constraint is empirical, not parsimony (Tenet 2's minimality is not the kind Tenet 5 disarms): consciousness biases which outcome actualises within the Born distribution rather than injecting energy.` (+18)
  - L109 OLD `The Minimal Quantum Interaction tenet locates consciousness's influence here—biasing probabilities rather than injecting energy.` → `…—biasing which outcome actualises within the Born distribution rather than injecting energy.` (+6)
- **Secondary files**, each OLD at count 1:
  - `concepts/cumulative-culture` L204 `biasing quantum probabilities rather than introducing new energy` → `biasing which quantum outcome actualises within the Born distribution rather than introducing new energy` (+6; headroom 161);
  - `concepts/islamic-sufi-philosophy-of-consciousness` L103 `consciousness biasing quantum probability distributions.` → `consciousness biasing which quantum outcome actualises within the Born distribution.` (+5);
  - `concepts/substance-property-dualism` L173 `(of what?) biasing probabilities.` → `(of what?) biasing which outcome actualises.` (+2);
  - `topics/consciousness-and-causal-powers` L84 `consciousness shifting probabilities against` → `consciousness biasing which outcome actualises against` (+2), and L136 `since biasing probabilities leaves` → `since biasing which outcome actualises leaves` (+2); headroom 26;
  - `voids/tenet-generated-voids` L63 `bias quantum probabilities?` → `bias which quantum outcome actualises?` (+2) and L65 `can alter probability distributions over physical outcomes.` → `can settle which physical outcome actualises.` (−1).
- The sweep can also absorb `concepts/quantum-biology-and-neural-mechanisms` L126 (entry 12): `—directly supporting [[interactionist-dualism|Bidirectional Interaction]].` → `—a route that would fit [[interactionist-dualism|Bidirectional Interaction]] without evidencing it.` (+6; headroom 50).
- Run it after queued L2742 (mental-causation L200) and match its wording.

**Fold-ins, not new tasks:**
- [P-MC3](/positions/arguments-for-mental-causation/#p-mc3) L46/L81 → append to the blocked P2 HUMAN LENGTH DECISION on positions-register seams (entry 6).
- `tenets.md` L67 → addendum to the NEEDS-HUMAN doctrine P2 at L2814 (Note 1).
- `phenomenology-of-resistance-across-domains` L117 → add to the queued L2720.
- `apex/minds-without-words` L115 is already inside Priority 1.