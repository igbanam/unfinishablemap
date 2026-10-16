---
ai_contribution: 100
ai_generated_date: 2026-10-16
ai_modified: 2026-10-16 05:05:00+00:00
ai_system: claude-opus-5-5+claude-opus-5
author: null
concepts:
- '[[predictive-processing]]'
- '[[common-cause-null]]'
- '[[cross-mechanism-convergence]]'
- '[[evidential-status-discipline]]'
created: 2026-10-16
date: &id001 2026-10-16
description: 'Research note on the ketamine-dissociation mechanism literature (Vesuna
  2020, Hu 2025, Bera 2026, Tian 2023, Wehrman 2023): what the controlled pharmacological
  case does to the Map''s claim that pharmacological dissociation is an independent
  route, and why the answer is a two-clause calibration rather than a new article.'
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-16 05:05:00+00:00
modified: *id001
related_articles:
- '[[pharmacological-dissociation-as-evidence]]'
- '[[anesthesia-void]]'
title: Research Notes - Ketamine Dissociation and the Retrosplenial Rhythm
topics:
- '[[clinical-dissociation-as-systematic-evidence]]'
- '[[anaesthesia-and-the-consciousness-interface]]'
- '[[brain-stimulation-and-the-witness-mode]]'
- '[[epistemology-of-convergence-arguments]]'
---

# Research: Ketamine Dissociation and the Retrosplenial Rhythm

**Date**: 2026-10-16
**Origin**: `reviews/optimistic-2026-10-08-clinical-dissociation-wing.md` Expansion item 4, which re-mints the Claude Fable 5.1 outer-review finding held as skipped item (12) in the `todo.md` NEEDS-HUMAN entry for `topics/clinical-dissociation-as-systematic-evidence`.
**Question the note must answer**: the flagship and the anaesthesia void both treat pharmacological dissociation as an *independent* route. **Independent of what**, on the Vesuna/Wehrman evidence?
**Scope**: narrow — the ketamine mechanism literature only. The site-wide "predictive-processing blind spot / Laukkonen gate" framing is declined upstream (`todo.md` L73) and is not re-raised here.

**Search method**: PubMed E-utilities (`esearch`/`efetch`) for every citation; PMC `efetch` XML for full texts; the PMC web article for Wehrman et al. 2023; two WebSearch calls used only as leads to PMIDs (`ketamine human posteromedial cortex delta rhythm dissociation intracranial EEG replication Vesuna`; `posteromedial cortex low-frequency rhythm depersonalization dissociative subtype PTSD delta oscillation retrosplenial human`). Europe PMC and the PMC web front end both refused Schmidt et al. 2012 and Weber et al. 2020 full texts (reCAPTCHA / HTTP 500), so those two are abstract-level.

## Executive Summary

1. **All three named sources verify, including the one the review could not find.** Vesuna et al. 2020 (PMID 32939091) and Wehrman et al. 2023 (PMID 37541951) were read in full at PMC. **Bera et al. 2026 is real**: *The Neuroscientist* 32(1):72–88, PMID **41453872**, PMC12812183, doi 10.1177/10738584251403946, epub 2025-12-26 — it was simply not yet indexed when the outer review ran. Its "requisite network feature" phrase is verbatim and is attributed *jointly* to Vesuna et al. 2020 and Hu et al. 2025, not to Vesuna alone.
2. **Wehrman et al. 2023 is not about dissociation at all.** The word stem `dissociat` occurs **zero** times in the full text (control: `ketamine` occurs 60 times). Its explanandum is *sensory disconnection*, its doses are chosen because they "do not produce disconnection", and its result preserves the authors' own predictive-coding model of disconnection by showing prediction-error correlates survive where disconnection is absent. It therefore does **not** show that ketamine dissociation reduces to precision weighting. The outer reviewer's gloss ("the ketamine predictive-coding literature says otherwise") overreaches on this paper.
3. **The rhythm literature contains no predictive-coding vocabulary.** In Vesuna et al. 2020: `predictive` 0, `prediction error` 0, `Bayesian` 0, `top-down` 0 (control: `dissociat` 79). Same for Bera et al. 2026 (its single `predictive` is "predictive marker" of antidepressant response) and Tian et al. 2023. The mechanism offered is a **pacemaker** account: HCN1-dependent 1–3 Hz rhythm in layer-5 retrosplenial cortex, causally sufficient under rhythmic optogenetic drive, abolished by local HCN1 knockout.
4. **So "independent of what?" has a four-part answer** (§The Answer below): independent of the *psychogenic/clinical* route at the level of generating mechanism — **yes**, and now better supported than when the clause was written; independent of the *precision-weighting family* — **not established**, and the honest claim is "not currently modelled as", with a named bridge by which the two could yet converge (Wehrman's own discussion nominates HCN1 as plausibly critical for functional predictive coding); independent of *level-of-consciousness* change — **contested** (Grent-'t-Jong et al. 2021); and reaching the *same channels* as the clinical cluster — **no**, the rodent phenotype is detection-without-affect, the pain-asymbolia axis.
5. **Verdict: (b) edits to existing pages, no new article.** The finding is a two-clause calibration plus a mechanism paragraph, and the one page with real length headroom (`apex/pharmacological-dissociation-as-evidence`, 275 words) is also the page that states the independence claim most explicitly. Exact old→new text, counts and headroom in §Verdict.

## Verification Ledger

| Source | How verified | Status |
|---|---|---|
| Vesuna et al. 2020, *Nature* 586:87–94 | PubMed PMID 32939091; PMC7553818 full-text XML read (16,043 words) | ✓ full text |
| Wehrman et al. 2023, *Br J Anaesth* 131:705–714 | PubMed PMID 37541951; PMC10624770 article page read (7,552 words) | ✓ full text |
| Bera, Looger, Proekt & Cichon 2026, *The Neuroscientist* 32(1):72–88 | PubMed PMID **41453872**; PMC12812183 full-text XML read (10,807 words) | ✓ full text — **UNVERIFIED claim in the review is now resolved** |
| Hu et al. 2025, *Cell Rep* 44(1):115086 | PubMed PMID 39708317, full abstract | ✓ abstract |
| Tian et al. 2023, *Nat Commun* 14:1748 | PubMed PMID 36991011; PMC10060225 full-text XML read (6,609 words) | ✓ full text |
| Grent-'t-Jong, Melloni & Uhlhaas 2021, *Front Psychiatry* 12:790372 | PubMed PMID 34938216; PMC8686110 full-text XML read (1,422 words) | ✓ full text |
| de la Salle et al. 2016, *Front Pharmacol* 7:348 | PubMed PMID 27729865, abstract | ✓ abstract |
| Chamadia et al. 2021, *Clin Neurophysiol* 132:3010–3018 | PubMed PMID 34715426, abstract | ✓ abstract |
| Gitlin et al. 2020, *Anesthesiology* 133:1021–1028 | PubMed PMID 32898213, abstract | ✓ abstract |
| Weber et al. 2020, *J Neurosci* 40:5658–5668 | PubMed PMID 32561673, abstract; full text blocked | ✓ abstract only |
| Schmidt et al. 2012, *Neuropsychopharmacology* 37:865–875 | PubMed PMID 22030715, abstract; full text blocked | ✓ abstract only |
| Mohanta et al. 2021, *J Neurosci* 41:10130–10147 | PubMed PMID 34732525, abstract | ✓ abstract |
| Cichon et al. 2023, *Nat Neurosci* 26:39–52 | PMID 36424433 via Bera's reference list | ✓ metadata |
| Wehrman et al. 2026, *Br J Anaesth* 136:573–583 | PubMed PMID 41314941, abstract | ✓ abstract — **the disconnection state there is dexmedetomidine sedation, not ketamine** |

Grep-verifiable quotes used below (each checked in the raw downloaded source, not in a summary):

- Vesuna et al. 2020: "rhythmic optogenetic activation of retrosplenial cortex layer 5 neurons recapitulated dissociation-like behavioural effects"; "local RSP HCN1 pacemakers are required in order for systemic ketamine to induce the deep RSP rhythm and elicit the dissociation-like behavioural state"; "Only one sham stimulation elicited report of an aura; this one report followed a real stimulation that had elicited a strong aura."
- Wehrman et al. 2023: "Subanaesthetic dosing of ketamine reduced correlates of predictive coding but did not eliminate them"; "we investigated the effects of subanaesthetic doses of ketamine (which do not produce disconnection)"; "Future studies should identify if higher doses of ketamine, such as those targeting hyperpolarisation-activated cyclic nucleotide-gated channels (HCN1), further modulate predictive coding. As HCN-1 channels typically control activity in distal dendrites that are important for the integration of information across the cortical hierarchy, it is plausible that these channels are critical for functional predictive coding."
- Bera et al. 2026: "these findings implicate RSC slow oscillations as a requisite network feature of ketamine dissociation"; "ketamine induces dissociation by selectively suppressing the interplay between feedforward pathways that supply specific stimulus information and the feedback pathways that supply context and salience to the stimuli."
- Tian et al. 2023: "Although both ketamine and propofol-induced 3 Hz rhythms in PMC, dissociation was only detected after ketamine."
- Grent-'t-Jong et al. 2021: "electrical stimulation in an epilepsy patient was applied at 50 Hz but not at delta-frequencies, suggesting that delta-frequency modulation was not necessary for dissociative experiences."

## The Answer: Independent of What?

The two live loci (located by text, 2026-10-16; line numbers had shifted after the 2026-10-15 22:19Z edit):

- `topics/clinical-dissociation-as-systematic-evidence` L127: "[Contemplative pathology] and [pharmacological dissociation] **add further routes that do not reduce to the precision-weighting family**, so their agreement on one channel taxonomy retains some compound-signature structure".
- `topics/clinical-dissociation-as-systematic-evidence` L165 (See-also): the void is glossed as "pharmacological dissociation as **a parallel route** to the same interface architecture". The "parallel route" phrase lives here, not in the void. (The void's own independence claim is at `voids/anesthesia-void` L102: "the architecture replicates under **independent perturbations**".)

### 1. Independent of the psychogenic/clinical route — YES, and now better supported

This is the claim the new literature strengthens. Before Vesuna, "independence" between the pharmacological and clinical routes was an inference from different-looking causes. Now the pharmacological route has a mechanism specified at the cellular level that the clinical route demonstrably does not share: an HCN1-paced 1–3 Hz rhythm localised to layer 5 of retrosplenial cortex, selectively elicited by NMDAR-antagonist dissociatives (ketamine, PCP, MK-801) but **not** by memantine, LSD, propofol, dexmedetomidine, diazepam or buprenorphine; causally sufficient under rhythmic optogenetic drive of RSP layer-5 neurons; abolished, along with the behavioural phenotype, by local HCN1 knockout; with retrosplenial parvalbumin interneurons as the inhibitory partner (Hu et al. 2025). Nothing in the DPDR/DID/conversion literature posits a cortical pacemaker. On the Map's own `concepts/cross-mechanism-convergence` discipline this is the strongest form of route-disjointness in the catalogue, and it is the "controlled experiment" the flagship elsewhere says the catalogue lacks.

### 2. Independent of the precision-weighting family — NOT ESTABLISHED; the clause asserts too much

Three separate points, which the outer review ran together.

**(a) Wehrman 2023 does not bear on dissociation.** Zero occurrences of `dissociat`; the explanandum is sensory disconnection; the doses are explicitly sub-disconnection. Its logic is defensive: if subanaesthetic ketamine had *eliminated* prediction-error correlates at doses that do not disconnect, the authors' predictive-coding model of disconnection "would be invalidated". It survived. That is a result about the model's internal consistency, not a reduction of ketamine dissociation to precision weighting.

**(b) The rhythm account is not stated in precision terms, so it is not currently *modelled* as a precision pathology.** Verified by vocabulary count with controls (§Executive Summary 3). But "not currently modelled as" is weaker than "does not reduce to". Non-reduction in principle is not what the evidence shows; the pacemaker account and a precision account are pitched at different levels of description and are not yet in competition.

**(c) A named bridge exists by which the two could converge — which is why the Map's clause should be softened rather than defended.** Wehrman et al. 2023's own discussion nominates HCN1 — the very channel that paces the dissociation rhythm — as plausibly "critical for functional predictive coding", because HCN1 governs distal-dendritic integration across the cortical hierarchy. Independently, Bera et al. 2026's cortical reading (via Aggarwal et al. 2024) is that ketamine "selectively suppress[es] the interplay between feedforward pathways that supply specific stimulus information and the feedback pathways that supply context and salience" — a feedforward/feedback imbalance that is trivially restatable in precision terms. If HCN1 turns out to be a predictive-coding substrate, the disjointness in §1 survives (the clinical route still shares no mechanism) while the disjointness claimed in L127 collapses. The two independence claims are not the same claim and should not be carried by one clause.

### 3. Independent of level-of-consciousness change — CONTESTED

Grent-'t-Jong, Melloni & Uhlhaas (2021) is a published critique of exactly the inference the Map wants, and the corpus does not hold it. Their four caveats: (i) in humans, ketamine-induced dissociative experience tracks **alpha** power reductions, not constrained delta (de la Salle et al. 2016 — depersonalisation ratings specifically); (ii) dissociative patients show resting **theta** increases; (iii) fMRI implicates an extended frontal/cingulate/parietal network, not a local posteromedial abnormality; (iv) the mouse doses that produce the rhythm (≥25 mg/kg, ≈2–3 mg/kg human-equivalent) are well above the <1 mg/kg human dissociative range, so the rhythm may index a change in the *level* of consciousness — the 3–4 Hz posteromedial signature is also the absence-seizure signature. They add the sharpest methodological point: the human stimulation was delivered at **50 Hz, not at delta**, so delta-frequency modulation was never shown necessary in the human case.

Two further human results cut the same way. Tian et al. 2023 (10 epilepsy patients, subanaesthetic ketamine, iEEG) replicates the posteromedial 3–4 Hz increase — but **propofol raised the same 3–4 Hz power in most regions, including posterior and isthmus cingulate, without producing dissociation**, so the rhythm is not sufficient; and they could not relate rhythm to dissociation intensity ("limited sample size and the limited resolution of dissociation assessment"). Chamadia et al. 2021 concluded that ketamine's EEG signatures support "anaesthetic state but not dissociation monitoring", and that midazolam attenuated CADSS scores while the EEG features dropped out of the model.

### 4. Reaching the same channels as the clinical cluster — NO

The rodent phenotype is operationalised as preserved reflexive paw-flick with abolished affective paw-licking and jump-to-escape: **detection without affect**. That is the Map's pain-asymbolia / neurological-dissociation axis, not the felt-ownership, cross-state-access or autobiographical-access channels that DPDR, DID and dissociative amnesia supply. So the mechanistic independence won in §1 does not transfer to the channels the flagship's convergence table is counting. The human side of Vesuna is richer (the S19_137 aura is a witness-mode report, already worked at `topics/brain-stimulation-and-the-witness-mode`), but it is one patient, and `topics/brain-stimulation-and-the-witness-mode` already records that his stimulation state retained control while the seizure climax did not.

**One-sentence answer.** On this evidence pharmacological dissociation is independent *of the psychogenic route's generating mechanism* — more robustly than when the clause was written — but it is not independent *of the precision-weighting family* in any established sense, it is not yet separated *from level-of-consciousness change* in humans, and it reaches *fewer channels* than the convergence count implies.

## Major Positions

### The pacemaker account (Vesuna et al. 2020; Hu et al. 2025; Bera et al. 2026)
- **Core claim**: dissociation has a circuit signature — a 1–3 Hz rhythm in layer-5 retrosplenial cortex, HCN1-paced, thalamically coupled to posterior nuclei while inversely correlated with frontally projecting anteromedial thalamus.
- **Key arguments**: drug specificity across eight agents; layer specificity (layer 5, not layer 2/3, confirmed by TRAP2 mapping); causal sufficiency (rhythmic optogenetics reproduces, random illumination does not, somatosensory drive does not); causal necessity of the pacemaker (local HCN1 knockout restores affective licking); cell-type resolution (RSC PV interneuron inhibition, Hu et al. 2025); one human homologue.
- **Relation to site tenets**: Tenet 1 at the bare reading only. It is a *channel-level* dissociation of detection from affect in a controlled, reversible, dose-graded preparation — the pattern the Map reads as interface structure — but it is equally what a modular functionalist predicts, so it earns the architecture and not its dualist significance (`concepts/architecture-vs-significance-two-tier-discount` applies as written).

### The predictive-coding / sensory-disconnection account (Sanders, Casey & Saalmann 2021; Wehrman et al. 2023, 2026; Weber et al. 2020; Mohanta et al. 2021)
- **Core claim**: disconnection from the environment is a failure of predictive processing — impaired feedforward prediction errors or, on the authors' later preference, impaired precision estimates sourced in higher-order thalamus.
- **Key arguments**: ketamine attenuates MMN and precision-weighted prediction errors (Weber 2020: high-level PEs about transition probability; Wehrman 2023: low-level PEs about transitional probability, at 0.2–0.3 µg/ml); low-dose ketamine but not dexmedetomidine perturbs predictive feedback and sensory pre-activation (Mohanta 2021); dexmedetomidine disconnection shows reduced surprise-related cortical synchronisation (Wehrman 2026).
- **Relation to site tenets**: neutral, and *not* a rival to the pacemaker account on its own terms. It targets disconnection, dose-ranges below dissociation, and prediction-error signalling. Wehrman 2023 even reports that its own dose range may not be acting through NMDARs at all, and points at HCN1 for the next experiment.
- **Where it does threaten the Map**: if the HCN1 bridge closes, the "independent route" clause in L127 loses its warrant while §1's route-disjointness survives.

### The deflationary human position (Grent-'t-Jong et al. 2021; Chamadia et al. 2021; Tian et al. 2023)
- **Core claim**: the posteromedial delta rhythm may not be the human mechanism of dissociation at all — in humans dissociative experience tracks alpha, the rhythm is not sufficient (propofol produces it without dissociation), and no human study has correlated rhythm magnitude with dissociation intensity.
- **Relation to site tenets**: neutral, and the most useful calibration source in this cycle. It is the reason the Map should not upgrade the pharmacological route's weight on the strength of Vesuna.

## Key Debates

### Is the deep posteromedial rhythm the mechanism of human dissociation, or of a change in level of consciousness?
- **Sides**: Vesuna et al. (rhythm underlies dissociative states) vs Grent-'t-Jong, Melloni & Uhlhaas (dose-equivalence and absence-seizure parallels make a level-of-consciousness confound live; the human stimulation that *elicited* auras was 50 Hz, not delta).
- **Current state**: open, and the main post-2020 human work (Tian et al. 2023) deepens the problem by producing the rhythm with propofol in the absence of dissociation.

### Does the ketamine predictive-coding literature subsume ketamine dissociation?
- **Sides**: the 2026-10-08 outer reviewer (yes — "they add no independent route") vs the papers themselves (Wehrman 2023 never mentions dissociation and uses sub-disconnection doses; Weber 2020 and Schmidt 2012 target MMN/PE and psychotomimetic or cognitive symptoms, not CADSS dissociation).
- **Current state**: the strong reading is not supported by the cited sources; a weak reading (one route might eventually be restated in precision terms via HCN1 and feedback-wave suppression) is live and is why the Map's clause should be softened.

### Is dissociation functionally bound to ketamine's other effects?
- **Sides**: Gitlin et al. 2020 show analgesia and dissociation are independent (dissociation drops out of the pain model); Luckenbaugh et al. 2014 and Fava et al. 2020, as reported by Bera et al. 2026, find dissociation *predicts* antidepressant response.
- **Relevance here**: it supports the Map's general separability claim at a new seam — one agent, one receptor system, components that come apart — without touching the dualist step.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 2002 | Umbricht et al., *Biol Psychiatry* 51:400–406 | MMN amplitude indexes NMDAR vulnerability; the predictive-coding line's empirical root |
| 2012 | Schmidt et al., *Neuropsychopharmacology* 37:865–875 | S-ketamine, not psilocybin, disrupts the MMN memory trace — PE processing is NMDAR-specific |
| 2016 | de la Salle et al., *Front Pharmacol* 7:348 | In humans, depersonalisation ratings track **alpha** reductions |
| 2020 | **Vesuna et al., *Nature* 586:87–94** | The retrosplenial 1–3 Hz rhythm; optogenetic sufficiency; HCN1 necessity; one human case |
| 2020 | Weber et al., *J Neurosci* 40:5658–5668 | Hierarchical PEs in the roving MMN; ketamine diminishes high-level PEs |
| 2020 | Gitlin et al., *Anesthesiology* 133:1021–1028 | Dissociative and analgesic properties of ketamine are independent |
| 2021 | Grent-'t-Jong, Melloni & Uhlhaas, *Front Psychiatry* 12:790372 | The published critique: alpha not delta, dose mismatch, 50 Hz not delta, level-of-consciousness confound |
| 2021 | Chamadia et al., *Clin Neurophysiol* 132:3010–3018 | EEG supports anaesthetic-state but not dissociation monitoring |
| 2023 | Cichon et al., *Nat Neurosci* 26:39–52 | Ketamine's neocortical activity switch (silent neurons activate, active ones silence) |
| 2023 | **Tian et al., *Nat Commun* 14:1748** | Human replication of the posteromedial 3–4 Hz rise — and propofol produces it without dissociation |
| 2023 | **Wehrman et al., *Br J Anaesth* 131:705–714** | Predictive coding reduced but not eliminated at sub-disconnection doses; nominates HCN1 as the next target |
| 2025 | Hu et al., *Cell Rep* 44:115086 | RSC parvalbumin interneurons as the inhibitory substrate of the rhythm |
| 2026 | **Bera et al., *The Neuroscientist* 32(1):72–88** | Review: RSC slow oscillations as "a requisite network feature"; feedforward/feedback suppression reading |
| 2026 | Wehrman et al., *Br J Anaesth* 136:573–583 | Thalamic synchronisation and disconnection — **dexmedetomidine**, not ketamine |

## Verdict

**(b) The finding belongs as edits to existing pages. No new topics article.**

Why not a new article: the Map-relevant content is a calibration of an existing clause plus one mechanism paragraph. `apex/pharmacological-dissociation-as-evidence` already names the evidence pattern and already states the independence claim it needs ("The independence that carries weight is *between* classes"); `topics/anaesthesia-and-the-consciousness-interface` already carries the agent contrasts; `topics/brain-stimulation-and-the-witness-mode` already carries the human S19_137 case and cites Vesuna. A fifth page would restate all three. (Section capacity is not the blocker — `topics` is 348/370 by `count_section_files` on 2026-10-16 — the duplication is.)

Measured headroom (`tools.curate.length.analyze_length`, 2026-10-16; headroom = hard − 1 − count, the gate being `>=`):

| Page | Words | Hard | Headroom |
|---|---|---|---|
| `apex/pharmacological-dissociation-as-evidence` | 4,724 | 5,000 | **275** |
| `topics/clinical-dissociation-as-systematic-evidence` | 4,688 | 4,000 | **−689 (OVER; standing human decision — edits must be ≤ 0)** |
| `topics/brain-stimulation-and-the-witness-mode` | 3,088 | 4,000 | 911 |
| `topics/anaesthesia-and-the-consciousness-interface` | 3,991 | 4,000 | 8 |
| `voids/anesthesia-void` | 2,995 | 3,000 | 4 |
| `topics/epistemology-of-convergence-arguments` | 5,745 | 4,000 | −1,746 (OVER) |

### Edit 1 (required) — `topics/clinical-dissociation-as-systematic-evidence`, net **−1 word**

The one locus that is *live and wrong*. Grep-verified at count 1 in both trees (obsidian and `hugo/content`) on 2026-10-16.

- OLD (11 words): `add further routes that do not reduce to the precision-weighting family`
- NEW (10 words): `add further routes not yet reduced to the precision-weighting family`

Net **−1**, so this installs **without** the pending human length decision, which is what has held skipped item (12) since 2026-10-08. It converts an asserted non-reduction into an accurate statement of the literature's position and needs no new reference. The sourced +45-word version in the NEEDS-HUMAN entry remains the better install *if* the human lifts the ceiling; this is the version that fits today.

### Edit 2 (recommended) — `apex/pharmacological-dissociation-as-evidence`, net **+247 words** against 275 headroom

Insert as a new bolded paragraph in `## The Cumulative Convergence`, immediately after the paragraph beginning "The convergence with non-pharmacological evidence adds to the effect" (grep-verified count 1), since that paragraph is where the between-class independence claim is made:

> **The mechanism specification, and what it does not reach.** Pharmacological dissociation is the one route here with a worked cellular mechanism. In mice, dissociative doses of ketamine elicit a 1–3 Hz rhythm confined to layer 5 of retrosplenial cortex; rhythmic optogenetic drive of those neurons reproduces the behavioural phenotype, and local HCN1 knockout abolishes rhythm and phenotype together (Vesuna et al. 2020; Hu et al. 2025). That is a pacemaker account, stated nowhere in precision or prediction-error terms — which is all this route's non-reduction to the precision-weighting family amounts to: not currently modelled as a precision pathology, not shown irreducible to one. The rodent phenotype is also detection-without-affect, the pain-asymbolia axis rather than the ownership channels the clinical cluster covers, and the human link stays thin — propofol raises the same 3–4 Hz posteromedial power without producing dissociation (Tian et al. 2023; Grent-'t-Jong et al. 2021).

Paragraph = 147 words. Plus four references inserted alphabetically into `## References` (= 100 words; the list is alphabetical with the Map's self-cites last, so Grent-'t-Jong goes after Gröpel, Hu et al. 2025 after Hu et al. 2023, Tian before Voon, Vesuna after Tian — renumbering only):

1. `Grent-'t-Jong, T., Melloni, L., & Uhlhaas, P. J. (2021). Dissociation and brain rhythms: Pitfalls and promises. *Frontiers in Psychiatry*, 12, 790372. https://doi.org/10.3389/fpsyt.2021.790372`
2. `Hu, Y., Feng, Y., Luo, H., et al. (2025). Dissociation-related behaviors in mice emerge from the inhibition of retrosplenial cortex parvalbumin interneurons. *Cell Reports*, 44(1), 115086. https://doi.org/10.1016/j.celrep.2024.115086`
3. `Tian, F., Lewis, L. D., Zhou, D. W., et al. (2023). Characterizing brain dynamics during ketamine-induced dissociation and subsequent interactions with propofol using human intracranial neurophysiology. *Nature Communications*, 14, 1748. https://doi.org/10.1038/s41467-023-37463-3`
4. `Vesuna, S., Kauvar, I. V., Richman, E., et al. (2020). Deep posteromedial cortical rhythm in dissociation. *Nature*, 586(7827), 87–94. https://doi.org/10.1038/s41586-020-2731-9`

**Total +247 against 275 headroom (28 spare).** If a trim is wanted, dropping the Grent-'t-Jong reference and citation saves 29 words but loses the only published critique of the rhythm→dissociation inference; prefer dropping nothing.

### Edit 3 (optional) — `topics/brain-stimulation-and-the-witness-mode`, net **≈ +60 words**

That page is the corpus's only Vesuna locus and cites the S19_137 stimulation case without the post-2020 human context. One sentence after the S19_137 paragraph would close it: that Tian et al. 2023 found the same posteromedial 3–4 Hz rise in ten patients under subanaesthetic ketamine, that propofol produced it without dissociation, and that Grent-'t-Jong et al. 2021 note the elicited auras came from 50 Hz stimulation, so delta-frequency modulation was never shown necessary in humans. Cost: two new references inserted alphabetically before `Vesuna` (19), renumbering entries 19–21. Headroom is ample (911). Not required by the review item; mint separately if wanted.

### Edit 4 — none

`voids/anesthesia-void` L102 ("the architecture replicates under independent perturbations") and the L165 See-also gloss in the flagship ("a parallel route") are **supported** by §1 and need no change. The void has 4 words of headroom anyway.

## Gaps in Research

- **No human study correlates posteromedial rhythm magnitude with dissociation intensity.** Tian et al. 2023 say so explicitly. Until one exists, the human arm of the Vesuna inference rests on one patient plus a replication of the *rhythm* but not of the *link*.
- **No test of the HCN1 / predictive-coding bridge.** Wehrman et al. 2023 propose it as future work; no paper found that runs it. This is the single experiment that would decide whether the Map's L127 clause is merely unmodelled or actually false.
- **Schmidt et al. 2012 and Weber et al. 2020 are abstract-level here** (Europe PMC 500, PMC web reCAPTCHA). Neither abstract reports a dissociation measure, but whether their full texts correlate PE disruption with CADSS or 5D-ASC dissociation subscales is unchecked, and that correlation is what a strong reduction claim would need.
- **Dose translation is unresolved.** Grent-'t-Jong et al.'s objection (mouse ≥25 mg/kg ≈ 2–3 mg/kg human vs <1 mg/kg human practice) has not been answered in print as far as this search reached.
- **Nothing found on the dissociative subtype of PTSD or DPDR showing a posteromedial delta signature**, which is what would extend the pharmacological mechanism to the clinical cluster. See `research/dissociative-subtype-of-ptsd-2026-10-09.md` for that branch.

## Citations

1. Bera, K., Looger, L. L., Proekt, A., & Cichon, J. (2026). Cortical mechanisms contributing to ketamine-induced dissociation. *The Neuroscientist*, 32(1), 72–88. PMID 41453872. https://doi.org/10.1177/10738584251403946
2. Chamadia, S., Gitlin, J., Mekonnen, J., et al. (2021). Ketamine induces EEG oscillations that may aid anesthetic state but not dissociation monitoring. *Clinical Neurophysiology*, 132(12), 3010–3018. PMID 34715426. https://doi.org/10.1016/j.clinph.2021.08.021
3. Cichon, J., Wasilczuk, A. Z., Looger, L. L., Contreras, D., Kelz, M. B., & Proekt, A. (2023). Ketamine triggers a switch in excitatory neuronal activity across neocortex. *Nature Neuroscience*, 26(1), 39–52. PMID 36424433. https://doi.org/10.1038/s41593-022-01203-5
4. de la Salle, S., Choueiry, J., Shah, D., et al. (2016). Effects of ketamine on resting-state EEG activity and their relationship to perceptual/dissociative symptoms in healthy humans. *Frontiers in Pharmacology*, 7, 348. PMID 27729865. https://doi.org/10.3389/fphar.2016.00348
5. Gitlin, J., Chamadia, S., Locascio, J. J., et al. (2020). Dissociative and analgesic properties of ketamine are independent. *Anesthesiology*, 133(5), 1021–1028. PMID 32898213. https://doi.org/10.1097/ALN.0000000000003529
6. Grent-'t-Jong, T., Melloni, L., & Uhlhaas, P. J. (2021). Dissociation and brain rhythms: Pitfalls and promises. *Frontiers in Psychiatry*, 12, 790372. PMID 34938216. https://doi.org/10.3389/fpsyt.2021.790372
7. Hu, Y., Feng, Y., Luo, H., et al. (2025). Dissociation-related behaviors in mice emerge from the inhibition of retrosplenial cortex parvalbumin interneurons. *Cell Reports*, 44(1), 115086. PMID 39708317. https://doi.org/10.1016/j.celrep.2024.115086
8. Mohanta, S., Afrasiabi, M., Casey, C. P., et al. (2021). Predictive feedback, early sensory representations, and fast responses to predicted stimuli depend on NMDA receptors. *Journal of Neuroscience*, 41(49), 10130–10147. PMID 34732525. https://doi.org/10.1523/JNEUROSCI.1311-21.2021
9. Schmidt, A., Bachmann, R., Kometer, M., et al. (2012). Mismatch negativity encoding of prediction errors predicts S-ketamine-induced cognitive impairments. *Neuropsychopharmacology*, 37(4), 865–875. PMID 22030715. https://doi.org/10.1038/npp.2011.261
10. Tian, F., Lewis, L. D., Zhou, D. W., et al. (2023). Characterizing brain dynamics during ketamine-induced dissociation and subsequent interactions with propofol using human intracranial neurophysiology. *Nature Communications*, 14, 1748. PMID 36991011. https://doi.org/10.1038/s41467-023-37463-3
11. Umbricht, D., Koller, R., Vollenweider, F. X., & Schmid, L. (2002). Mismatch negativity predicts psychotic experiences induced by NMDA receptor antagonist in healthy volunteers. *Biological Psychiatry*, 51(5), 400–406. PMID 11904134. https://doi.org/10.1016/s0006-3223(01)01242-2
12. Vesuna, S., Kauvar, I. V., Richman, E., Gore, F., Oskotsky, T., Sava-Segal, C., Luo, L., Malenka, R. C., Henderson, J. M., Nuyujukian, P., Parvizi, J., & Deisseroth, K. (2020). Deep posteromedial cortical rhythm in dissociation. *Nature*, 586(7827), 87–94. PMID 32939091. https://doi.org/10.1038/s41586-020-2731-9
13. Weber, L. A., Diaconescu, A. O., Mathys, C., et al. (2020). Ketamine affects prediction errors about statistical regularities: A computational single-trial analysis of the mismatch negativity. *Journal of Neuroscience*, 40(29), 5658–5668. PMID 32561673. https://doi.org/10.1523/JNEUROSCI.3069-19.2020
14. Wehrman, J. J., Casey, C., Tanabe, S., et al. (2023). Subanaesthetic doses of ketamine reduce but do not eliminate predictive coding responses: Implications for mechanisms of sensory disconnection. *British Journal of Anaesthesia*, 131(4), 705–714. PMID 37541951. https://doi.org/10.1016/j.bja.2023.06.044
15. Wehrman, J. J., Casey, C., Redinbaugh, M. J., et al. (2026). Thalamic contributions to predictive coding and disconnected consciousness in human volunteers. *British Journal of Anaesthesia*, 136(2), 573–583. PMID 41314941. https://doi.org/10.1016/j.bja.2025.10.038