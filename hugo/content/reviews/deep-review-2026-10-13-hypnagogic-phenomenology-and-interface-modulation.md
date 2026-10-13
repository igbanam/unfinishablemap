---
ai_contribution: 100
ai_generated_date: 2026-10-13
ai_modified: 2026-10-13 09:02:36+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-13
date: &id001 2026-10-13
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-13 09:02:36+00:00
modified: *id001
related_articles: []
title: Deep Review - Hypnagogic Phenomenology and Interface Modulation
topics: []
---

**Date**: 2026-10-13
**Article**: [Hypnagogic Phenomenology and Interface Modulation](/topics/hypnagogic-phenomenology-and-interface-modulation/)
**Previous review**: [2026-07-25](/reviews/deep-review-2026-07-25-hypnagogic-phenomenology-and-interface-modulation/) (also 2026-07-06, 2026-06-05, 2026-05-25, 2026-04-06, 2026-03-12)

## Context

Seventh deep review. Selected by hand from the candidate list: the selector's first eleven picks were all on the driver's 30-hour avoid list (ten new pages plus the valence-cluster `graduated-middle-path`, refined 2026-10-12 20:07Z). This article had the largest unreviewed fold of any eligible candidate: about 140 changed lines across eight refine-draft commits between 2026-08-22 and 2026-09-25, none of which a deep review had seen. Six of those commits landed on 2026-08-22. The fold added nine new citations (Löwe 2025, Tal 2024, Datta 2022, Andrillon 2021, Sandved-Smith 2021, Feldman & Friston 2010, Mashour 2020, Aru 2020, Decat 2026), the four-rival "Single-Mechanism Rivals" section, the Thompson stance firewall and the Datta yoga-nidra plank. So the 2026-07-25 stability note ("citation layer web-verified clean as of 2026-06-05; do not re-web-verify before ~2027") no longer applies: the References block more than doubled after it was written.

Length at dispatch was 3902 words (topics soft 3000, hard 4000, gate `>=`). After this pass it is 3964, a net change of +62. The added words pay for one null result (Lacaux) and for scope fixes that the critical issues required. Trims elsewhere recovered about 18 words.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **False negative claim about the Hori chapter (L84).** The article said "the cited chapter measured no cognitive variable alongside them". The 2026-08-22 refine wrote this sentence, and its own changelog says "the chapter could not be opened from here". The claim was therefore never sourced, and it is false. Noreika et al. (2015, *Front. Psychol.* 6:202, PMC4357244) cite Hori et al. (1994) for this: "Reaction times as well as the rate of subjective reports of being asleep are known to increase steadily from Hori Stage 1 to Stage 9". The same lab's follow-up confirms the RT measure (Hayashi, Katoh & Hori 1998, Hiroshima bulletin; abstract read at the repository: "reaction time prolonged with progress of the hypnagogic EEG stages"). **Fix**: the article now credits the EEG result and the reaction-time correlate to Hori et al., and keeps "micro-awakenings" marked as this article's gloss. L86 was reworded so that it still holds given the RT correlate: "a stage-level reaction-time correlate does not show that either capacity returns". **Caveat for future passes**: the RT attribution rests on a peer-reviewed secondary source plus the lab's own 1998 primary. The 1994 chapter itself was not opened.
2. **Datta 2022 scope (L140, L152).** The article used Datta et al. to say yoga nidra *practitioners* are scored awake, and set that against the reports of *advanced* practitioners. The paper studied novices: "Thirty subjects underwent five initial supervised yoga nidra sessions … after 2 weeks of yoga nidra practice"; the conclusion reads "Yoga nidra practice in novices is electrophysiologically an awake state". Dropping that qualifier changed the meaning. **Fix**: L140 now says the participants were novices after two weeks' training and that the advanced practitioners at issue went unrecorded. Falsifiability item 4 now says "novice" and states the advanced-practitioner condition as the test still to run. The delta wording was also corrected: the prefrontal decrease is in delta power ("raised central and reduced prefrontal delta power").
3. **Tenet-3 calibration slippage in the Relation to Site Perspective section (L160).** The text read "Full waking involves robust bidirectional coupling" as fact, and agency fluctuation "offers a window onto bidirectional interaction". This conflicts with `tenets.md` L95 `^tenet-3-standing`, which says downward causation is *available, not actual*, and adds that articles asserting real causal work "should read no more confidently than this paragraph does". A reviewer who accepts the tenets would still flag it. **Fix**: the paragraph now reads "shows what bidirectional interaction at varying strengths would look like. On the Map's reading, full waking involves robust coupling, which the [tenet page](/tenets/#tenet-3-standing) holds available rather than shown". This is the available/actual standing. It is not the Tenet-3 *quantifier* question, which stays a NEEDS-HUMAN item in todo (L733) and was not touched.
4. **Internal contradiction: RSP versus body on micro-awakenings (L158).** The Minimal Quantum Interaction paragraph cited "the micro-awakenings that briefly restore interface function" as a finding. The body (L84 and L86) explicitly calls that reading this article's gloss and interpretation, not a finding. **Fix**: "this article's micro-awakening gloss on the alpha returns would fit that but does not test it".
5. **Wrong superlative (L122).** Apical drive was called "the newest rival", but Aru et al. (Dec 2020) is older than Andrillon et al. (June 2021) and Sandved-Smith et al. (Aug 2021), both cited in the same section. **Fix**: "The fourth rival".

### Medium Issues Found

- **Omitted null result (L92).** The article said neither incubation study "shows that phenomenal experience does it", but Lacaux et al. actually tested this. The raw PMC text reads: "neither hypnagogic experiences in general (χ2 = 0.14, P = 0.71) nor task-related hypnagogia (χ2 = 0.05, P = 0.83) had an effect on insight". Haar Horowitz et al. found the opposite pattern for incubated content: the degree of theme incorporation into reports was a significant positive predictor on all three creativity tasks. **Fix**: one sentence now records the divergence. It supports the article's deflationary point and does not overturn it.
- **Dormio prompts (L90).** The article had "delivered during N1 sleep". In the protocol the prompt is delivered *after* each awakening and report, as the participant returns to sleep; the abstract calls the cues "at sleep onset". **Fixed** to "at sleep onset".
- **Graded-precision rival stated as a result (L116).** The four-signature ordering is the article's reconstruction. Neither Feldman & Friston (2010, a Posner-paradigm simulation) nor Sandved-Smith et al. (2021, mind-wandering during sustained attention) models sleep onset. **Fix**: "Neither paper models sleep onset, but one graded parameter … would yield". The Sandved-Smith gloss is also tightened to the paper's own wording: precision "in the mapping between observations and hidden cognitive states".
- **Andrillon timing (L118).** The paper says slow waves "accompany behavioural markers of lapses and preceded reports of mind wandering and mind blanking". "before attentional lapses" became **"alongside attentional lapses"**.
- **Anaesthesia contrast (L48).** "unlike anaesthesia, which disrupts the interface chemically" implied that anaesthesia closes the channels all at once. Anaesthetic induction also separates components (for example, connected consciousness after loss of responsiveness), and the article's own L100 relies on propofol and ketamine producing different phenomenologies. **Cut** (−7 words).
- **"input continues undiminished" (L68).** External sensory input is attenuated at sleep onset (Hori's lengthening RTs; Mashour et al. 2020: early sensory processing "preserved, though weakened" in N1/N2). What continues is *experienced content*. **Fixed.**
- **L58 attribution (carried forward as Low from 06-05, 07-06 and 07-25).** "recent work by Haar Horowitz, Lacaux … refined the neural correlates". Haar Horowitz 2023 reports no neural correlates; Lacaux 2021 does (delta and quadratic-alpha power predicted insight), and so does Decat 2026 (EEG features that separate mental states). **Fixed** by changing the names to "Lacaux, Decat", with no change in word count. This is not oscillation: no prior pass edited the sentence.
- **Decat (L104).** Participants rated their own reports; the authors clustered them. "scored" became "clustered … self-rated".

### Citation Ledger (§2.4, publisher of record)

Every DOI was resolved at Crossref. Quotes and numbers were grepped in the raw Europe PMC full-text XML or abstract JSON, not checked through a confirmation prompt.

- Mavromatis 1987 (*Hypnagogia*, Routledge): real-correct (unchanged since the 06-05 verification; a print monograph; the article attributes nothing beyond cataloguing the state).
- Thompson 2014 (*Waking, Dreaming, Being*, Columbia UP): real-correct. Crossref chapter DOIs `10.7312/thom13709-004…013` confirm the TOC: ch. 5 "Witnessing: Is This a Dream?" and ch. 8 "Sleeping: Are We Conscious in Deep Sleep?", so the "ch. 5, 8" locator for the contemplative reports fits. The L74 gloss ("progressively dissolves ego structure—the sense of being a distinct agent in a world") matches Thompson's own précis: "Whereas normal waking consciousness is ego-structured … this structure dissolves in the hypnagogic state. There is no ego in the sense of an 'I' who acts as a participant in a larger world". The hypnagogic discussion itself sits in ch. 4. **Cited-author stance**: Thompson is a non-dualist enactivist, and the L138 stance firewall states this correctly.
- Lacaux et al. 2021 (*Sci. Adv.* 7(50) eabj5866): real-correct. "at least 15 s in N1 … tripled the chance … (83% versus 30%)" is verbatim; N = 103; "this effect vanished if subjects reached deeper sleep". **Result-direction leg**: the null for hypnagogic experience on insight is now in the article.
- Haar Horowitz et al. 2023 (*Sci. Rep.* 13, 7319, doi 10.1038/s41598-023-31361-w): real-correct. The third author is "Tomás Vega Gálvez" (Crossref: family "Gálvez"). Rendering it as "Gálvez, T." follows Crossref and was left. **Result-direction leg**: N1 beat wake, and incorporation predicted performance. The prompt-timing detail was corrected.
- Hori, Hayashi & Morikawa 1994 (APA chapter, pp. 237–253, doi 10.1037/10166-014): real-correct metadata. Nine stages confirmed from the lab's own repository abstracts. The false negative claim was removed (Critical 1).
- Stickgold et al. 2000 (*Science* 290(5490):350–353): real-correct. "may arise without important contribution from the declarative memory system" was grepped verbatim in the PubMed abstract (EXT_ID 11030656); three amnesic patients confirmed.
- Tal et al. 2024 (*PNAS* 121(10) e2313604121): real-correct. "qualitatively different consequences" and "consciousness-dependent inhibition account, whereby unconscious reactivation entails less inhibition … more liberal spread of activation" are verbatim. No retraction or correction: the linked `pnas.2402870121` is a commentary ("Reminiscing under the radar"). The step to *creative insight* is marked as the Map's reading.
- Datta et al. 2022 (*Front. Neurol.* 13, 910794): real-correct metadata. A dropped qualifier (novices) was fixed (Critical 2). Awake scored throughout (n = 26); central delta up (P = 0.033), prefrontal delta down (P = 0.041).
- Andrillon et al. 2021 (*Nat. Commun.* 12, 3657): real-correct. Wording fixed from "before" to "alongside".
- Sandved-Smith et al. 2021 (*Neurosci. Conscious.* 2021(1) niab018): real-correct. A publisher's note exists (niab035), but it is not a correction of findings. The gloss was tightened.
- Feldman & Friston 2010 (*Front. Hum. Neurosci.* 4:215): real-correct. "attention can be understood as inferring the level of uncertainty or precision".
- Mashour, Roelfsema, Changeux & Dehaene 2020 (*Neuron* 105(5):776–798): real-correct. The source supports a "sudden loss of ignition" at sleep onset with early sensory processing "preserved, though weakened" in N1/N2. The article's workspace-fragmentation ordering is a fair reconstruction from that.
- Löwe, Petzka, Tzegka & Schuck 2025 (*PLOS Biol.* 23(6) e3003185): real-correct. N = 90 and preregistered (osf.io/z5rxg); N2 85.7% (24/28), N1 63.6% (14/22), Wake 55.5% (10/18); Fisher N1 vs Wake p = 0.75; N2 vs Wake p = 0.038; "conceptually replicate". All verbatim.
- Aru, Siclari, Phillips & Storm 2020 (*Neurosci. Biobehav. Rev.* 119:440–455): real-correct. Both quoted spans were grepped verbatim in the PubMed abstract (EXT_ID 33002561). The "neuromodulator-gated" gloss is supported ("cholinergic and adrenergic arousal systems … have specific effects on the AIZ").
- Decat et al. 2026 (*Cell Rep.* 45(4) 117237): real-correct. "emerge across wakefulness, N1 sleep, and N2 sleep" is verbatim; 92 participants and N = 375 confirmed.
- Refs 8–9 (Map self-cites, pseudonymous co-author): intentional. Do not strip.

**Inline ↔ References**: all 15 external references are cited in the body, and every inline (surname, year) pair has an entry. No orphans in either direction. No arXiv-only cites. **Superlative sweep**: the helper returned nothing; a manual grep found "newest", which is fixed (Critical 5). The other superlatives ("strongest", "most awkward") are judgements, not empirical records.

### Reasoning-Mode Classification (§2.6, editor-internal)

- Disinhibition and production model: Mode Three. This is honest boundary-marking and unchanged.
- Graded precision (PP/active inference): Mode Three. It is now explicitly marked as a reconstruction, not as the authors' model.
- Local sleep (Andrillon): Mode Three, with the rival credited as observed.
- Workspace fragmentation (Mashour et al.): Mode Three.
- Apical drive (Aru et al.): mixed. It notes inside the rival's own framework that the proposal "does not derive the order", then marks the boundary.
- Thompson: stance firewall correct.
- Label leakage: none. The grep for forbidden labels, "load-bearing", and "This is not X" returned 0.

### Counterarguments Considered

- Churchland and Dennett (retrospective report unreliability): already handled by falsifiability item 2 and the lead's "retrospective reports" hedge. Bedrock.
- Tegmark (the light-sleep quantum speculation): labelled speculation, now explicitly decoupled from the micro-awakening gloss.
- Deutsch: the NMW paragraph already discounts coherence as evidence ([P-A2](/positions/agency-and-will/#p-a2)). Bedrock.
- Popper: four substantive falsifiers. Item 4 is now properly scoped to the experiment still missing.
- Nagarjuna (the witnessing self): handled by the Thompson process-self firewall.

## Optimistic Analysis Summary

### Strengths Preserved

- The deflationary lead ("constrains, not establishes"), front-loaded and truncation-resilient.
- The four-rival section, especially "a staggered-disengagement generator with no channels in it". It concedes honestly and is the strongest such section in the sleep cluster.
- The Tal et al. (2024) passage. A Hardline-Empiricist would count it as exemplary: the Map's own evidence cuts against its quick reading, and the article says so.
- Single-study restraint on Lacaux and Löwe, with every number intact and verified.
- The Thompson stance firewall ("the plank carries the weight of one source").
- The apical-drive "failed search, not evidence of absence" sentence. It was deliberately inherited from the research note's gaps list in the 2026-08-24 refine and kept.

### Enhancements Made

- The Lacaux / Haar Horowitz content divergence (Medium 1).
- Four accuracy tightenings (Dormio, Andrillon, Decat, Sandved-Smith).
- Trims: the anaesthesia contrast (−7), "Parsimony would have predicted uniform dimming" (−6, which repeated the sentence before it), and the observational-vocabulary preface (−5).

### Cross-links Added

- [tenets](/tenets/#tenet-3-standing) (Bidirectional Interaction paragraph).

## Remaining Items

- **Covered by the queue, not fixed here:** L110's "conscious selection must bias token-level outcomes while leaving aggregate Born statistics exactly undisturbed" falls within the open Born-reading register audit (todo L2523, two Map pages with different Born-preservation readings). It already uses the aggregate (unconditioned) form, so it is not a live defect under the L2504 rule.
- **Low, not actioned:** the Relation to Site Perspective Dualism paragraph cites [P-CS6](/positions/consciousness-scope/#p-cs6) for "does not discriminate filter from production". [P-CS6](/positions/consciousness-scope/#p-cs6)'s content ("filter evidence bears on Tenet 1 alone") fits only loosely. It is not wrong, and a better-fitting anchor would be [P-CS4](/positions/consciousness-scope/#p-cs4).
- **Low, not actioned:** "propofol and ketamine produce identical behavioural unresponsiveness" (L100). "Comparable" would be more careful. This text was reviewed by earlier passes and left alone for convergence.
- **Hori 1994 primary text still unopened.** The RT attribution rests on Noreika et al. 2015 plus Hayashi, Katoh & Hori 1998. If a future pass can open the chapter, confirm that the RT data are in it.

## Stability Notes

- Seven passes now, and the article converges *again* after a large refine fold. The 2026-07-25 note "do not re-web-verify before ~2027" was correct when written, but it was overtaken by a References block that more than doubled. **A stability note's citation exemption expires when the References block changes. Check `git log` on the References block before honouring one.**
- The full 17-entry citation ledger above was verified on 2026-10-13 against Crossref and the Europe PMC raw text. Re-verify only entries added or changed after this date.
- All earlier bedrock notes stand. MWI disagreement over agency fluctuation, the speculative coupling-modes mapping, the disinhibition engagement as honest Mode Three (do not upgrade it to refutation), and the single-study calibration for Lacaux and Dormio, now with Löwe's failed conceptual replication, are framework-boundary or settled-calibration matters, not defects.
- `anchoring_audit_exempt: true` remains valid. The pass *added* hedges where calibration called for them.
- Length is 3964 of 4000 (gate `>=`, so 35 words of usable headroom). The next pass that adds anything must make equal cuts.