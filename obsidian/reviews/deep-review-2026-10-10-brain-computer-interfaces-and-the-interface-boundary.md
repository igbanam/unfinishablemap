---
title: "Deep Review - Brain-Computer Interfaces and the Interface Boundary"
created: 2026-10-10
modified: 2026-10-10
human_modified: null
ai_modified: 2026-10-10T21:48:35+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-10
last_curated: null
---

**Date**: 2026-10-10
**Article**: [[brain-computer-interfaces-and-the-interface-boundary|Brain-Computer Interfaces and the Interface Boundary]]
**Previous review**: [[deep-review-2026-07-26-brain-computer-interfaces-and-the-interface-boundary|2026-07-26]] (this is the sixth deep review)

## Convergence Context

The 2026-07-26 review said the article was stable. Since then the article changed substantially. Commit `4650f1ac25` (refine-draft, 2026-08-21) added the whole "Whose Action Is a Decoded Movement?" section, a fourth "What BCIs Cannot Do" clause and twelve new References entries (8–19). The section came from `research/deviant-causation-bci-mediated-action-2026-08-20`. On the same day, the deep review of [[philosophy-of-action-under-dualism]] corrected the Yashin paraphrase here as a family fix. **No deep review had yet run publisher-of-record checks on the other ten new citations.** This pass did that, and it also re-read the older body for currency drift and for dependents that earlier fixes left stranded.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Dependents left stranded by the 2026-07-26 Golub fix (L77).** The "same data, rival readings" paragraph was written on 2026-06-19, while the Golub paragraph still claimed overnight consolidation. The 07-26 review corrected Golub but left three spans in L77 that relied on the retracted claim: "the manifold and consolidation data establish", "the overnight consolidation", and "the manifold or consolidation results". So the article was still citing as evidence a finding that the 07-26 stability note says must never be reintroduced. **Fixed**: all three now refer to reassociation and the reuse of an existing repertoire.
2. **Unsupported overclaim on sensory feedback (L81).** The original said: "Without it, performance degrades catastrophically. Remove visual feedback from a cursor-control BCI, and accuracy drops to near chance." It gave no citation. The canonical open- vs closed-loop comparison (Taylor, Tillery & Schwartz 2002) says open-loop trajectories "went toward the correct targets more often than they would have by chance". Closed-loop trajectories hit 49% of targets, against 27% open-loop. **Fixed**: the passage now states that finding with the citation. The "This is not incidental—it reveals…" construction was also removed (style guide).
3. **Factual error: somatoparaphrenia "while retaining motor control" (L99).** Somatoparaphrenia is typically a delusion about a *paralysed* contralesional limb (Vallar & Ronchi 2009 review). Its documented dissociations are from anosognosia and neglect, not from paralysis, so it is not an example of ownership lost with control intact. **Fixed**: the ownership/control dissociation is now carried by Kalckert & Ehrsson (2012), whose abstract was verified: the moving rubber-hand illusion shows a double dissociation of ownership and agency. Somatoparaphrenia is kept only as lesion-induced disownership.
4. **Empirical-record currency drift: "BrainGate users achieve … roughly 1-3 bits per second … far below natural motor bandwidth" (L109).** The figures were checked at the publisher. Pandarinath et al. 2017 (eLife 6:e18554) reports grid-task averages of 1.4–3.7 bps, and 4.16 bps on a dense grid. Neuralink's 2024 PRIME progress report (company-reported, not peer-reviewed) gives 4.6 bps on day one, rising to 8.0, against "~10 BPS" for Neuralink engineers using a mouse. That is the decision-limited rate of able-bodied hand control on the same task. The present-tense figure is out of date, and "far below natural motor control" no longer holds on the selection metric. The 07-26 currency sweep missed this because the claim contains no superlative keyword. **Fixed**: the second observation is re-scoped to "BCIs open no new bandwidth". It dates both figures and marks the company figure as company-reported. It keeps the 2026-06-19 settled wording ("same order of magnitude as, though not a measure of") and says the convergence is also predicted by a physicalist who locates the bottleneck in cortical decision circuitry. The unsupported "rough, effortful quality … partially adapted interface" inference was removed.
5. **Falsifier that has already been met, and a false "None of these has been demonstrated" (L123, L161).** The third falsifier was "a device reading from muscle, skin, or external sensors … achieving the same quality of willed control as cortical BCIs". Myoelectric prostheses and gaze trackers already give fluent willed control, so the article's closing "None of these has been demonstrated" was false as worded. The body clause made the same slip: it lumped EMG with galvanic skin response as capturing "not volitional selection". A tenet-accepting reviewer would flag this, because muscle and gaze signals sit downstream of the neural selection and so cannot test where the interface is. **Fixed**: the falsifier is restated as willed control by a route with *no* neural link (the psychokinesis case the brain-specialness boundary excludes). The body clause now says muscle- and gaze-driven control works *because* it carries the brain's motor output.
6. **Dropped qualifier: Evans et al. 2015 (L137).** The article said "users claim authorship of outcomes their neural activity did not produce *whenever the display says so*". The verified Europe PMC abstract says discrepancies between decoded activity and feedback generally *decrease* the sense of agency. Agency stays high, and rises, only "if the feedback discrepancy serves to correct a poorly controlled BMI-action". **Fixed** to the conditional form. **Family resolution**: the same overgeneralisation ("whenever the display reports it") was in [[penfield-interactionist-dualism]] L66, and a related one was in the source research note's Evans entry. Both were corrected in this pass.
7. **Dropped qualifier: Buller 2020 (L135).** The article said "BCI behaviour counts as action, he argues, *only* 'if we can equate imagining movement with trying to move' … leave that equation *unearned*". The verified publisher abstract reads: "BCI-mediated behavior can be accommodated by a Volitionist account of action if we can equate imagining movement with trying to move. The argument presented is that the novelty, and limited functionality and sensory feedback of present BCIs challenges this equation." **Fixed** to "On a volitionist account, he argues, BCI behaviour counts as action 'if …', and the novelty, limited functionality and impoverished feedback of present systems challenge that equation." The objection still lands on the Map, because the Map is volitionist.

### §2.4 Publisher-of-Record Citation Web-Verify (per-cite ledger)

New since the last deep review. Metadata comes from the Crossref API unless noted:
- Steinert, Bublitz, Jox & Friedrich 2019 (*Philosophy & Technology* 32(3):457-482) — **real-correct** (online 2018-03-10, print 2019-09). Quotes grep-verified in the Springer PDF text: "it may initiate movements by predictive interpretation of brain signals" (sixth peculiarity) and "events mediated by passive BCIs are no actions" (fourth peculiarity, §4.2 close). The executory/guidance/veto taxonomy is confirmed. Note: the HTML full-text rendering drops the second quote's sentence. Grep the PDF, not the HTML.
- Buller 2020 (*Neuroethics* 14(2):155-165) — **real-correct** under the online-first year convention (published online 2020-05-04; issue July 2021). Quote "the proximate cause of action in present BCI-mediated behavior is not the person's intention" verified verbatim in the publisher abstract. **Paraphrase corrected** (Critical 7).
- Rainey, Maslen & Savulescu 2020 (*AJOB Neuroscience* 11(1):46-58) — **real-correct**. Continuity and the controllability/foreseeability residue confirmed against the OpenAlex abstract.
- Mehta 2025 (*Oxford Open Neuroscience*) — **real-wrong-metadata** (incomplete). The article had no volume or article number; corrected to **4, kvaf002** per Crossref. The contemplation-conundrum paraphrase was grep-verified in the Europe PMC full text (PMC12199723): "No known neuroscientific marker distinguishes one pattern of motor imagery from the other except the retrospective ascription of an 'intention to act'". "Voluntary yet unintentional" outputs: faithful.
- Evans, Gale, Schurger & Blanke 2015 (*PLoS ONE* 10(6):e0130019) — **real-correct** metadata. **Paraphrase corrected** (Critical 6). Full text: PMC4466540.
- Serino et al. 2022 (*Nature Human Behaviour* 6(4):565-578) — **real-correct**. The abstract (Europe PMC, PMID 35046522) supports M1 processing of agency signals and that "Neural signals processing the sense of agency affected the proficiency of the brain-machine interface". The article's "the participant's sense of agency feeding back into decoder proficiency" was tightened to "agency-related neural signals affecting decoder proficiency".
- Willett et al. 2023 (*Nature* 620(7976):1031-1036) — **real-correct**. LM prior verified in the full text (PMC10468393): phoneme probabilities "combined with a large-vocabulary language model (a custom, 125,000-word trigram model…) to decode the most probable sentence."
- Metzger et al. 2023 (*Nature* 620(7976):1037-1046) — **real-correct**. The author-contributions statement confirms a trained language model in the text decoder (KenLM n-gram cited). No figures from this paper are used, which honours the research note's ceiling.
- Piñeros Glasscock & Tenenbaum 2023 (SEP "Action") — **real-correct** (first published 11 Jan 2023; © 2023 both authors). "Primary deviance" / "secondary deviance" terminology verified in the live entry, attributed there to Mele & Moser 1994. The secondary-deviance gloss is faithful.
- Davidson 1980 (*Essays on Actions and Events*, incl. "Freedom to Act" 1973) — **real-correct**. The SEP quotes the climber as Davidson 1973, 153–4.
- Yashin 2025 — carried forward: verified with full-text grep in the 2026-08-21 deep review of [[philosophy-of-action-under-dualism]] and unchanged since.

Added this pass (all verified at Crossref and against the claim made):
- Taylor, Tillery & Schwartz 2002 (*Science* 296(5574):1829-1832) — real-correct. 49±17% vs 27±9% targets hit, closed- vs open-loop, from the paper's table.
- Kalckert & Ehrsson 2012 (*Frontiers in Human Neuroscience* 6:40) — real-correct. "double dissociation of ownership and agency" is in the abstract.
- Pandarinath et al. 2017 (*eLife* 6:e18554) — real-correct. 2.2/3.7/1.4 bps for T6/T5/T7, and 4.16 bps on the dense grid.
- Neuralink 2024-05-08 PRIME progress update — company report, labelled as such in the References. 4.6 → 8.0 BPS; engineers using a mouse ~10 BPS.

Older citations (Sadtler 2014, Golub 2018, Collinger 2013, Iriki 1996, Clark & Chalmers 1998): the References block is unchanged, so the 2026-06-19 ledger and the 2026-07-26 Golub/Sadtler fidelity checks stand. Clark & Chalmers is now named as co-authors in the body. Before, "Andy Clark's extended mind thesis" credited only one of the two authors of the cited paper.

Inline ↔ References cross-check: all 23 entries are cited inline or are Map self-citations reached by wikilink. No orphans.

**Result-direction leg**: Taylor (closed > open), Pandarinath (bps values), Kalckert (double dissociation), Evans (conditional rise in agency), Serino (agency signals → proficiency), Willett/Metzger (LM in decoding), Mehta (no marker). Each was checked for the direction the article states. Two were corrected (Evans, Buller).

**Cited-author-stance leg**: none of Steinert, Buller, Rainey, Mehta, Evans, Serino or Yashin is presented as endorsing dualism. The Yashin answer is marked as coming "from outside his framework". The Serino "brain-side, where the Map locates the interface" gloss is marked as the Map's own.

**Superlative helper**: only "so far" (L47, a generic hedge). The currency defect in Critical 4 was found by reading, not by the helper.

### Medium Issues Found

- **Self-undermining anaesthesia argument (L121 ↔ L151).** This is not a re-flag of the bedrock disagreement. The 2026-05-19 hedge put "the cortical activity patterns that decoders rely on degrade" into L121, which is the physicalist's explanation. L151 still listed "why it disappears under anaesthesia" among the features the simpler story "leaves unexplained". That is an internal tension, left behind when the earlier fix was not carried through. **Fixed**: L121 now says the anaesthesia loss fits the Map's prediction but cannot confirm it, because consciousness and the decoded patterns go together. L151 now puts the weight on the felt effort. The L77 forward reference now points at the Occam's-razor tenet paragraph by anchor, instead of an "argument developed below" that is two sentences long. The falsifier "Volitional BCI control persisted under general anaesthesia" is kept. It is a valid one-sided test.
- **Dualism tenet paragraph overclaim.** It said that under identity theory the distinction between "consciousness controls the brain which controls the device" and "consciousness controls the device" "would be meaningless". An identity theorist can draw that mediated/direct distinction perfectly well. The paragraph also clashed with L77's concession that the plasticity data are neutral. **Fixed**: BCIs now *illustrate* the distinction rather than *establish* it. The "do not challenge dualism—they illuminate it" construction was removed.
- Minor calibration: "BCI evidence supports the minimality constraint" → "fits". "exactly what bidirectional interaction predicts" → "what". "would not support volitional control" → "should not" (it is a prediction, not an observation).

### Reasoning-Mode Classification (editor-internal, not in article)

- Clark & Chalmers (extended mind): Mode Three. It concedes functional extension and marks the phenomenal/computational distinction as the Map's commitment. Unchanged.
- No-interface physicalist on the plasticity data (L77): Mode Three, with an explicit concession that the data are neutral. Unchanged apart from the stranded-premise repair.
- "Just neural plasticity" (Occam paragraph): Mode Two. The rival story helps itself to felt effort without explaining why there is felt effort at all. It is now honest that the anaesthesia evidence does not discriminate.
- Yashin: Mode Three ("from outside his framework … not a refutation of reliability strategies on their own ground"). Unchanged.
- Buller: concession plus Mode Three. The objection is granted to land, and the Map's residual vocabulary is offered without claiming a test. Unchanged in structure; quotation qualifier restored.
- Rainey et al. and Steinert et al.: reported positions, not opponents. Steinert's passive-BCI verdict is used in agreement.
- MWI: Mode Three. Unchanged (settled 2026-06-19).
- Label-leakage grep: clean.

## Optimistic Analysis Summary

### Strengths Preserved
- The "same data, rival readings" paragraph (L77). Declining to use a tenet as an evidence upgrade is still the article's best calibration move. It is now internally consistent again.
- The "Whose Action Is a Decoded Movement?" section. The relocation thesis and its four consequences are a distinctive contribution no source states. The Buller concession and the "stating it is not a test for it" admission are exemplary restraint (Hardline Empiricist).
- The Sadtler/Golub pairing: constraint plus mechanism.
- "What Would Challenge This View". Its three falsifiers are now all live and well-specified.

### Enhancements Made
- The sensory-feedback claim now rests on a real, quantified result instead of an unsupported superlative.
- The ownership/control dissociation now rests on a clean experimental double dissociation (Kalckert & Ehrsson 2012) instead of a misdescribed lesion syndrome.
- The bandwidth observation now does honest work: convergence on the decision ceiling, dated figures, and the physicalist parity stated.
- The non-neural-route clause and its falsifier now make a coherent claim.

### Cross-links Added
- [[brain-specialness-boundary]] (from the restated third falsifier, the psychokinesis case). Anchor link to the Occam's-razor tenet paragraph from L77.

## Length

- Before: 3826 words total (prose 3461 + references 378).
- After: 3933 words total (prose ~3480 + references 472).
- The prose stayed roughly length-neutral (+~15 words). This was done by trimming the redundant sentences in L63, L69, L75, L87 and L97 and by rewriting the Dualism paragraph more tightly. Four verified references were added (+94 words of apparatus).
- Status: soft_warning. Headroom to the hard threshold: 66 words. The next editor should treat the article as **length-neutral** and should **not** add references without matching cuts.

## Remaining Items

- L91 (Collinger 2013, settled 2026-05-19): the lead clause "BCI users sometimes report a sense of ownership or agency … particularly with robotic limbs that provide haptic feedback" has no citation of its own. Collinger 2013 had no haptic feedback. It is not re-flagged as critical because of the 05-19 settlement. A future pass with headroom could cite a sensory-feedback ownership study (e.g. Flesher et al. 2021, *Science*) or soften the clause.
- Hugo sync not run by this fork. The orchestrator's sync and commit carry the changes.

## Stability Notes

- **Golub 2018 is a within-session *reassociation* finding.** No span anywhere in the article may refer to "consolidation" data. The 07-26 fix stranded three such spans in L77, and they were repaired this pass. Grep "consolidat" after any edit to L73–L77.
- **BCI throughput figures are currency-sensitive.** Re-check the Pandarinath/Neuralink figures when this article is next reviewed. The comparability wording ("same order of magnitude as, though not a measure of") is settled and must not be re-litigated. The *numbers* are not settled.
- **The third falsifier is about routes with no neural link.** Do not revert it to "non-neural tissue". Muscle- and gaze-driven control already gives fluent willed control and cannot test the interface's location.
- **The anaesthesia evidence does not discriminate**, and the article now says so in both places. The bedrock disagreement (physicalists reject that loss of consciousness explains loss of control) remains bedrock. Do not re-flag it as critical.
- **Evans 2015 is conditional**: agency persists only when the feedback correction serves the goal. Any sibling paraphrase reading "whenever the display says so" is an error. Fixed here and in [[penfield-interactionist-dualism]].
- **Buller's equation is the volitionist route and "challenges", not "unearned".** Do not restore "only if".
- Clark/extended mind, MWI indexicality and the eliminativist "just plasticity" responses remain bedrock framework-boundary disagreements. Do not re-flag them.
- This article is now a *secondary host* for imported material (the 08-21 fold). After any future import, diff since `last_deep_review` and treat every inserted citation as unverified until it has been checked at the publisher of record.
