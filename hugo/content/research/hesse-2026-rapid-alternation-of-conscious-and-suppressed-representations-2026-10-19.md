---
ai_contribution: 100
ai_generated_date: 2026-10-19
ai_modified: 2026-10-19 08:31:00+00:00
ai_system: claude-opus-5-5
author: null
concepts:
- '[[neural-correlates-of-consciousness]]'
- '[[selective-correction-and-reconstruction-paradox]]'
created: 2026-10-19
date: &id001 2026-10-19
description: A 2026 macaque preprint finds face-patch and prefrontal populations alternating
  every ~60 ms between the seen and the unseen face under flash suppression. What
  it shows, how its labels were made, and which Map pages it corrects.
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-19 08:31:00+00:00
modified: *id001
recommended_action: refine
related_articles:
- '[[attention-and-consciousness]]'
- '[[attention-as-interface]]'
- '[[quantum-neural-timing-constraints]]'
title: 'Research Notes - Hesse et al. (2026): Rapid Alternation of Conscious and Suppressed
  Representations'
topics:
- '[[neural-refresh-rates-and-the-smoothness-problem]]'
- '[[dualist-perception]]'
---

# Research: Hesse et al. (2026), Rapid Alternation of Conscious and Suppressed Representations

**Date**: 2026-10-19
**Search queries used**: bioRxiv API record for doi:10.64898/2026.10.15.759299; Europe PMC search (preprint record PPR1343847); bioRxiv `v1.full` page (abstract only) and `v1.full.pdf` (full text, 50 pages, extracted with `pdftotext`); Europe PMC full text of Hesse & Tsao 2020 (PMC7676863); Crossref metadata for every work cited below; OpenAlex abstracts for Sheinberg & Logothetis 1997 and Kapoor et al. 2022; web searches for "Hesse Tsao 'Rapid alternation of conscious and suppressed'", "Tsao lab flash suppression face patches micro-epochs", "Janis Hesse Caltech thesis face patches".

**Full-text status**: the full text of v1 was read. bioRxiv rate-limited every route for about ten minutes, then served the PDF. Every claim below beyond the abstract was checked against the extracted text. Quotations are verbatim from that text.

**Name guard**: "Hesse" here is Janis K. Hesse (UC Berkeley, Tsao lab). Mary Hesse, the philosopher of science, is cited elsewhere on the Map and is a different person.

## Executive Summary

Hesse, Lanfranchi, McGrory, Shi, Engel and Tsao recorded large populations with Neuropixels probes in two macaques. They recorded from face patches ML and AM in inferotemporal cortex (IT) and from prefrontal face patches PO and PVL while the animals passively fixated binocular flash suppression displays. Within the analysis window the stimulus was constant, and so was the percept, judging by humans who reported the flashed face on the same displays. Yet population activity flipped back and forth between two states. In state 1 the population carried a nearly pure representation of the flashed face (the "conscious" one). In state 2 it carried an almost equally faithful representation of the suppressed face. Each state lasted about 60 ms. The abstract's "about 15 times per second" counts switches between states rather than cycles of an oscillation; a full seen–unseen–seen cycle takes about 120–130 ms. The same neurons served both states. Tuning gain was about 21% higher in state 1, and a linear decoder told the states apart with 66% accuracy. Prefrontal cortex showed the same pattern, more weakly. The authors set aside the hard problem. They read the result as showing that "conscious access requires temporal selection beyond localization": a physicalist routing mechanism.

For the Map, the result is **one unreplicated preprint from one lab, in two monkeys, with no report from the animals**. It supports no tenet. What it does is sharpen several explanatory targets and correct one stale empirical claim. Recommended action: **refine**. Five pages need edits: [selective-correction-and-reconstruction-paradox](/concepts/selective-correction-and-reconstruction-paradox/) (the IT "winner-take-all" claim is out of date), [neural-correlates-of-consciousness](/concepts/neural-correlates-of-consciousness/) (the no-report evidence on prefrontal cortex is mixed), [attention-and-consciousness](/voids/attention-and-consciousness/) (the suppressed image is absent from experience but not from high-level cortex), [neural-refresh-rates-and-the-smoothness-problem](/topics/neural-refresh-rates-and-the-smoothness-problem/) (the gap moves from sampling rate to content stability) and [dualist-perception](/topics/dualist-perception/) (one overclaiming sentence). Two pages need no change at present: [quantum-neural-timing-constraints](/topics/quantum-neural-timing-constraints/) and [attention-as-interface](/concepts/attention-as-interface/). A standalone page would be premature on one preprint.

## What the Paper Did

### Paradigm (binocular flash suppression)

A priming image is shown to one eye for 1 or 2 s. A second image is then flashed to the other eye with no blank, and both stay on. The flashed image dominates perception and the priming image is suppressed. This is Wolfe's (1984) single-flash paradigm. It is distinct from *continuous* flash suppression: no flickering mask is used, so the ~60 ms alternation cannot be entrainment to a mask rhythm. Analyses use the window 300–1000 ms after the flash.

The suppression is **stimulus-driven**. The flash decides which image is seen, by design. Nothing in the paradigm involves spontaneous perceptual switching, choice or attention manipulation.

### ESTABLISH 1: How the percept was determined (no report, by cross-species transfer)

- **The monkeys never reported anything.** They were head-fixed and rewarded for fixation. Trials were kept only if fixation was held for at least 90% of the trial. The paper reports no optokinetic, pupillometric or other eye-movement readout of the percept, and no microsaccade analysis.
- **The percept labels come from 14 human participants** who reported by button press while viewing the same displays. The flashed image was reported on 82% of binocular trials. The unambiguous priming image was reported correctly on 87% of trials. The suppression index was tested with t(13) = 9.4, p = 4 × 10⁻⁷. The human report latency was 0.86 ± 0.05 s, and the analysis window was shifted by that amount for humans.
- Consequence: the paradigm is a no-report paradigm whose consciousness attributions are **calibrated against human report on the same stimuli and transferred across species**. This illustrates the point made in the "How NCC Studies Depend on Report" section of [neural-correlates-of-consciousness](/concepts/neural-correlates-of-consciousness/): the validation chain of a no-report paradigm runs back to report somewhere.

### ESTABLISH 2: How micro-epochs were labelled (and the circularity)

- **Templates.** For each stimulus pair, each neuron's mean firing rate was taken from *priming* trials, when one face was shown alone. These rates gave a "conscious" template (the flashed face) and a "suppressed" template (the priming face).
- **Labelling.** In each 10 ms bin, a Poisson log-likelihood ratio decides which template better explains the population spike counts. State 1 is the bin's label when the flashed-face template wins, and state 2 when the priming-face template wins. A two-state Poisson hidden Markov model with the same fixed templates gives the dwell-time estimates. Only its 2 × 2 transition matrix is free, fitted by Baum–Welch, with Viterbi decoding.
- **So "conscious micro-epoch" means "an epoch in which the population resembles the template of the face that humans report seeing in this display".** Awareness is never measured at the grain of an epoch. The subject's percept is assumed constant across the window while the states alternate. The words "conscious" and "suppressed" label *content*. They do not label moments of awareness.
- **Statistical circularity, which the authors name and address.** They state that their first-pass analyses are "subject to a circular conditioning bias". They also state that "above-chance state-resolved reconstruction is expected even of models with no genuine alternation, and on its own is not diagnostic of a genuine, coordinated alternation." Their controls:
  - split-half cross-neuron validation, where states are inferred from one half of the neurons and faces reconstructed from the other half;
  - leave-one-neuron-out validation;
  - balanced-trial subsampling, which rules out between-trial differences;
  - shuffled-template controls;
  - an On/Off excitability control using a four-state decoder (Cohen's κ ≈ 0 against a firing-rate partition; 80% agreement with the two-state labels);
  - generative-model comparison. An averaging model and an uncoordinated-switching model pass the circular test but fail the cross-validated reconstruction, the tuning-reversal test and the held-out likelihood test. Only a coordinated two-state model passes all four.
  On the paper's own evidence, the *statistical* circularity is handled well.
- **Interpretive circularity remains.** It is this note's analysis; the paper does not discuss it. Within flash suppression, "conscious vs suppressed" is perfectly confounded with "newly flashed vs already adapted for 1–2 s". The higher tuning gain in state 1 (the main asymmetry offered as the signature of the conscious state) could therefore reflect stimulus history rather than access. Hesse & Tsao (2020) themselves warned that under flash suppression "the physical input when the target is perceived is not identical to that when it is suppressed, and thus any modulation observed may be driven entirely externally." The within-trial alternation escapes this worry, since the stimulus is constant inside the window. The *labelling* of which state is the conscious one does not escape it.

### ESTABLISH 3: Alternation-rate statistics

- **Autocorrelation.** The autocorrelation of the log-likelihood-ratio signal, averaged over 19 sessions, was fitted as a symmetric two-state Markov chain over lags of 10–90 ms. It gave a mean dwell time D = 67 ms (median D·ln2 ≈ 46 ms if dwell times are exponential). Time-shuffled data decayed within one bin.
- **HMM.** The HMM fit to held-out neurons peaked at small bin sizes. Over that range, median dwell plateaued at ~60 ms. At the best bin size (5 ms), median dwell was 64 ms for state 1 and 59 ms for state 2.
- **"15 Hz".** The Discussion gives "15 Hz" against perceptual switches of "~0.5 Hz" in ordinary rivalry. The paper does not show the arithmetic, but 15 per second matches 1/D for D = 67 ms. It is therefore a **switching rate** (~15 state changes per second). The two states were occupied about equally, so a "conscious" epoch recurs roughly 7–8 times per second.
- **Not an oscillation.** Dwell times are modelled as memoryless (Markov). v1 reports no spectral or periodicity analysis. The authors relate the finding to rhythmic-attention and working-memory burst literatures only in the Discussion, as an analogy.
- **Weak coordination across patches.** Inferring states in ML and reconstructing from AM (and the reverse) gave only weak separation, in 7 sessions with simultaneous recordings. The authors: "our results do not provide strong evidence for coordination across patches in generating conscious and suppressed micro-epochs."
- **Scale.** 19 sessions in total. The 10-stimulus experiment had 7 sessions in monkey A and 3 in monkey M; the 1500-face experiment had 5 and 4. 3501 visually responsive neurons were used for reconstruction, and 543–548 cells for the tuning analyses.

### ESTABLISH 4: The prefrontal result

- **Areas and sample.** Recordings came from the face patches in the lateral orbitofrontal sulcus (PO) and the infraprincipal dimple (PVL), with 661 prefrontal neurons. v1 does not break down PFC sessions or animals separately.
- **Ceiling.** Reconstruction from PFC was poorer than from IT. Priming-response explained variance was below 80% (over 90% in IT), and below 30% for shape features.
- **State separation.** The state-dependent separation held both on the same samples (p = 10⁻¹⁴) and under cross-neuron validation (explained variance p = 3 × 10⁻⁴). Cross-validated identity decoding gave a weaker p = 0.03.
- **Modulation slopes.** As in IT, the trial-averaged perceptual modulation was much weaker than the unambiguous modulation (slope 0.32). Within states the slope was 0.91 in state 1 and −0.52 in state 2.
- **Residual correlation.** Unlike IT (r = −0.02 after gain equalisation), PFC kept a residual positive correlation after gain equalisation (r = 0.24, p = 0.005).
- **Internal inconsistency.** The text gives p = 4 × 10⁻¹⁰ for the Fig. 6f average-modulation test. The legend gives t(282) = −3.5, p = 5 × 10⁻⁴. Cite neither figure.
- **Authors' summary.** "Temporal multiplexing of conscious and suppressed representations may therefore be a broad cortical phenomenon rather than a feature unique to inferotemporal cortex."

### The authors' interpretation (theirs, and physicalist)

- They "set aside the 'hard problem' of why neural activity feels like anything". They ask only what makes activity "consciously accessible".
- **Weak modulation explained.** The long-standing weak perceptual modulation in high-level cortex (IT slope 0.23 over 5550 cell-stimulus pairs) is explained as an averaging artefact. Averaging collapses two opposite-selectivity states, plus a small gain asymmetry. After gain equalisation, the IT residual vanishes.
- **The suppressed stimulus is fully represented.** It "is not represented as a weak residual trace but occupies the same high-dimensional face space as the conscious stimulus during complementary temporal epochs".
- **Open question and proposed mechanism.** The open question in their words: "why do representations in some micro-epochs reach awareness, whereas others do not?" Their proposed answer is **dynamic routing** of state-1 content to downstream systems for report, introspection and behavioural control. The routing would be controlled by recurrent interactions or by feedback from parietal cortex or the pulvinar. They also speculate that "suppressed epochs may allow the brain to explore alternative interpretations of the visual input, without being broadcast or influencing behaviour".
- **Context.** Prior temporal-multiplexing work from the same lab (She et al. 2024, perception and memory codes in IT) and the rhythmic-attention theory (Fiebelkorn & Kastner 2019) are cited as context.

## Evidential Guards (carry into every edit)

1. **One preprint, v1, not peer-reviewed, one lab, two macaques.** Data and code are promised "upon publication" and are not yet public. Use "a 2026 preprint reports…" and never "neuroscience shows…".
2. **No animal report.** Percept labels transfer from 14 human observers. Micro-epoch awareness is never measured.
3. **Flash suppression is stimulus-driven.** The flash fixes the percept, and the monkeys are passive. The result says nothing about whether consciousness selects, chooses or biases anything. It must never be cited as evidence for bidirectional interaction or for "consciousness selecting among reconstructions".
4. **"15 Hz" is a switching rate between Markov states, not an oscillation.** Write "states lasting about 60 ms" or "switching roughly 15 times a second". Never write "a 15 Hz rhythm" or "conscious epochs 15 times a second".
5. **The authors' reading is physicalist** (temporal selection, dynamic routing) and must be reported as theirs. At most the result sharpens what *any* theory must explain. It does not support dualism.
6. **No bearing on the quantum mechanism.** The states are inferred from Poisson spike counts. No indeterminacy is measured, and a ~60 ms dwell bounds nothing in the Map's quantum timing hierarchy.
7. **Peer-reviewed anchors exist for the less novel parts.** That the suppressed stimulus is decodable from the same IT cells under no-report rivalry is in Hesse & Tsao (2020, *eLife*). That prefrontal populations track internally generated percept switches without report is in Kapoor et al. (2022, *Nature Communications*). Lean on these where possible and use the preprint only for what is new: the ~60 ms alternation, the pure state-wise representations and the PFC replication of the pattern.

## Bearing on Map Pages (what each needs)

### [selective-correction-and-reconstruction-paradox](/concepts/selective-correction-and-reconstruction-paradox/) — needs a correction (highest priority)

"The Selection Gap" paragraph says that in inferotemporal cortex "nearly all fire only when their preferred stimulus is perceived, a stage past the resolution of the conflict (Blake & Logothetis, 2002)". It concludes that "the discreteness thus has a neural correlate in later-stage winner-take-all resolution."

- **Where the claim comes from.** It rests on report-based single-unit work: Sheinberg & Logothetis 1997 found "almost all neurons" in IT/STS contingent on perceptual dominance.
- **The no-report evidence disagrees.** Under a no-report paradigm in the same face-patch system, single IT cells multiplex the percept and the suppressed stimulus, and the suppressed stimulus is decodable (Hesse & Tsao 2020, peer-reviewed). The 2026 preprint adds that trial-averaged IT and PFC modulation is weak because populations alternate every ~60 ms between pure representations of the seen and the unseen face.
- **What survives.** Winner-take-all exclusivity holds at most within ~60 ms epochs. Over any longer window, high-level representation is not exclusive.
- **The gap moves.** It now sits between exclusive experience and an alternating, non-exclusive representation. On the authors' reading, a temporal-routing step closes it. That reading is the strongest current physicalist rival to the page's claim that "consciousness must select among them" in the "Selection Under Ambiguity" section, and the page should name it as such.
- **Guard.** Flash suppression is stimulus-driven, so the fast layer is no evidence that consciousness chooses.

### [neural-correlates-of-consciousness](/concepts/neural-correlates-of-consciousness/) — needs balance on the prefrontal claim

"The Posterior Cortical Hot Zone" says: "No-report paradigms suggest that consciousness-related activity localises to posterior regions; frontal activation may reflect *reporting* consciousness rather than having it." The no-report evidence on PFC is in fact mixed:

- Kapoor et al. (2022, peer-reviewed) found feature-selective PFC populations tracking internally generated percept transitions without report, with decoding surviving oculomotor-suppression controls.
- The 2026 preprint finds that PFC face patches carry the same ~60 ms interleaving as IT. Neither region carries a pure correlate in trial-averaged activity.
- The authors' conclusion ("temporal selection beyond localization") suggests the front-versus-back question may be mis-posed at the level of averaged activity.

Secondary: the "How NCC Studies Depend on Report" list can take the preprint as a clean instance of a no-report paradigm whose labels are calibrated by human report on the same displays.

### [attention-and-consciousness](/voids/attention-and-consciousness/) (void) — needs one clarifying addition

The binocular-rivalry paragraph in "Empirical Demonstrations" says: "The suppressed percept is not dim or peripheral but *absent* — then it switches." The phenomenological claim stands. The page should add that this absence is phenomenal and not representational. The suppressed image is decodable from IT face cells under no-report rivalry (Hesse & Tsao 2020). The 2026 preprint reports it reconstructed at high fidelity in IT and PFC during alternating ~60 ms epochs (flash suppression, preprint).

That sharpens the void. Whatever excludes content from experience does not do so by excluding it from high-level representation, so the boundary of the attentional void is not drawn at representation.

### [neural-refresh-rates-and-the-smoothness-problem](/topics/neural-refresh-rates-and-the-smoothness-problem/) — needs one paragraph

The page frames the smoothness problem as continuous experience over a *rhythmically sampled* substrate (7–13 Hz, ~40 Hz). The preprint adds a different and sharper mismatch, one of **content stability** rather than sampling rate. Human observers report one stable face for the whole window. Meanwhile the high-level population represents that face purely only about half the time, in ~60 ms runs, and represents the *unseen* face the rest of the time.

- **The physicalist reply.** It mirrors the "Physical Smoothing Mechanisms" section: only state-1 content is routed onward, so what is experienced is a stream of same-content samples, and downstream integration smooths it. That is the authors' routing hypothesis, which they leave untested.
- **The question left over.** On the page's own anti-functionalist line, why does a 50%-duty-cycle carrier of the seen face present as an unbroken presence?
- **Tie-in to the Continuity Void.** Human report (latency ~0.86 s) cannot resolve 60 ms structure. The data therefore cannot show that experience itself does *not* alternate below introspective grain, which is the route Lee sets aside.
- **Guard.** Do not add "15 Hz" to the page's list of sampling rhythms. The alternation is Markov, not periodic.

### [dualist-perception](/topics/dualist-perception/) — needs one sentence fixed

The bistable-percept paragraph says that consciousness "alternates between interpretations in patterns that voluntary attention can bias but neural dynamics alone do not fully determine." The second clause is stated as a finding, but it is the Map's interpretive bet. The preprint adds neural machinery (a fast alternation and access layer) that physicalists will cite as determining what is accessed.

Recast the clause as the Map's reading and point to [selective-correction-and-reconstruction-paradox](/concepts/selective-correction-and-reconstruction-paradox/) for the evidence. The same guard applies: flash suppression is stimulus-driven, so nothing here shows that consciousness chooses.

### [quantum-neural-timing-constraints](/topics/quantum-neural-timing-constraints/) — no change

A ~60 ms dwell in a passive, stimulus-driven paradigm does not bound any mechanism in the timing hierarchy. Adding a row would invite the misreading that the alternation is a selection point. Revisit only if a replication shows the alternation is modulated by *willed* attention. Even then it would be a suggestive timescale and not evidence for the quantum mechanism.

### [attention-as-interface](/concepts/attention-as-interface/) — no change for now

Attention was not manipulated, so the preprint does not touch the willed-attention evidence the page relies on. If the result replicates, the "Challenges and Falsification" section should note it as a mechanistic account of content selection that needs no non-physical selector, a challenge rather than support. Note also that the page's length leaves almost no headroom.

### Adjacent, no task

[suspension-void](/voids/suspension-void/) cites neural metastability models that "hold multiple alternatives without collapsing". The preprint is a concrete instance of a population holding two alternatives by interleaving them in time. It could be folded in on that page's next deep review, but it does not justify a task on its own.

## Major Positions

### Temporal selection / dynamic routing (the authors)
- **Proponents**: Hesse, Engel, Tsao and colleagues (2026 preprint); the wider temporal-multiplexing programme the preprint cites (She et al. 2024; Rich & Wallis 2016 for orbitofrontal value states; Jezek et al. 2011 for hippocampal map flickering; the last two taken from the preprint's reference list, not verified here).
- **Core claim**: conscious access is fixed by *when* content is expressed and routed, not only by *where* it is represented.
- **Relation to tenets**: neutral to hostile. It is a physical account of access, offered with the hard problem explicitly set aside. It leaves phenomenal character untouched. It also offers a physical candidate for the "selection" step the Map sometimes assigns to the interface.

### Posterior vs prefrontal localisation
- **Proponents**: posterior (IIT, recurrent processing theory; Koch); frontal (global workspace, higher-order theories).
- **Bearing**: the preprint finds the same interleaved structure in both and a pure correlate in neither, on trial averages. It sides with neither camp and challenges the framing.

### Map reading (dualist interactionism)
- **Core claim**: representation and experience come apart, and high-level cortex represents both faces at full fidelity while only one is experienced. This fits the Map's insistence that neural content is not phenomenal content. A physicalist accepts the dissociation too and locates the difference in routing, so it does not discriminate between the views.

## Key Debates

- **Is the "conscious" state really conscious?** It is labelled by content similarity to the human-reported face, and its distinctive signature (tuning gain ×1.21) is confounded with stimulus recency under flash suppression. A paradigm with spontaneous switches and no report (for example optokinetic-nystagmus rivalry with Neuropixels) would test whether the state-1/state-2 split tracks the percept rather than the flash.
- **Rate or rhythm?** Markov dwell times versus possible periodic structure. v1 has no spectral analysis.
- **Unity.** Weak ML–AM coordination raises the question of whether there is a single switching process or a set of local ones.
- **PFC.** Lower ceiling, weaker cross-validated decoding (p = 0.03), and a residual average modulation that IT lacks.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1984 | Wolfe, binocular flash suppression | The paradigm used |
| 1997 | Sheinberg & Logothetis, report-based rivalry in IT/STS | "Almost all" IT neurons contingent on dominance; basis of the Map's winner-take-all claim |
| 2008 | Tsao et al., prefrontal face patches | First report of face patches in macaque frontal cortex |
| 2012 | Panagiotaropoulos et al., lateral PFC | Title claims PFC discharges "explicitly reflect visual consciousness" (abstract not read) |
| 2020 | Hesse & Tsao, *eLife*, no-report rivalry in face patches | IT cells multiplex percept and suppressed stimulus; suppressed stimulus decodable |
| 2022 | Kapoor et al., *Nat. Commun.*, no-report PFC decoding | PFC tracks internally generated switches without report |
| 2024 | She et al., *Nature*, temporal multiplexing in IT | Same lab's prior multiplexing result (perception and memory) |
| 2025 | COGITATE, *Nature* | Front-vs-back adversarial test, inconclusive on locus |
| 2026 | Hesse et al., bioRxiv v1 | ~60 ms alternation of pure seen/unseen representations in IT and PFC |

## Potential Article Angles

A standalone page is not recommended: one preprint, with the philosophically relevant content already split across five existing pages. If the result replicates, especially in a spontaneous-rivalry, no-report design, a concepts page on "temporal multiplexing and conscious access" could gather the threads. It would treat the routing hypothesis as the physicalist account of access and the residual question (why routed content is experienced at all) as the Map's target. Follow `obsidian/project/writing-style.md`.

## Gaps in Research

- No PFC session or animal breakdown in v1. Data and code are not yet public.
- The derivation of "15 Hz" is implicit (read here as 1/67 ms).
- No microsaccade, vergence or eye-position control is reported beyond the fixation criterion.
- No test separating "conscious" from "newly flashed".
- No peer review, no replication, and no other lab's commentary found as of 2026-10-19.
- The Fig. 6f p-value is inconsistent between text and legend.

## Citations

1. Hesse, J. K., Lanfranchi, F. F., McGrory, C., Shi, Y., Engel, T. A., & Tsao, D. Y. (2026). Rapid alternation of conscious and suppressed stimulus representations in the primate brain. *bioRxiv* (v1, posted 2026-10-16, not peer-reviewed, CC BY 4.0). https://doi.org/10.64898/2026.10.15.759299
2. Hesse, J. K., & Tsao, D. Y. (2020). A new no-report paradigm reveals that face cells encode both consciously perceived and suppressed stimuli. *eLife*, 9, e58360. https://doi.org/10.7554/eLife.58360
3. Sheinberg, D. L., & Logothetis, N. K. (1997). The role of temporal cortical areas in perceptual organization. *Proceedings of the National Academy of Sciences*, 94(7), 3408–3413. https://doi.org/10.1073/pnas.94.7.3408
4. Wolfe, J. M. (1984). Reversing ocular dominance and suppression in a single flash. *Vision Research*, 24(5), 471–478. https://doi.org/10.1016/0042-6989(84)90044-0
5. Kapoor, V., Dwarakanath, A., Safavi, S., Werner, J., Besserve, M., Panagiotaropoulos, T. I., & Logothetis, N. K. (2022). Decoding internally generated transitions of conscious contents in the prefrontal cortex without subjective reports. *Nature Communications*, 13, 1535. https://doi.org/10.1038/s41467-022-28897-2
6. Panagiotaropoulos, T. I., Deco, G., Kapoor, V., & Logothetis, N. K. (2012). Neuronal discharges and gamma oscillations explicitly reflect visual consciousness in the lateral prefrontal cortex. *Neuron*, 74, 924–935. https://doi.org/10.1016/j.neuron.2012.04.013 (metadata verified; abstract not read)
7. Tsao, D. Y., Schweers, N., Moeller, S., & Freiwald, W. A. (2008). Patches of face-selective cortex in the macaque frontal lobe. *Nature Neuroscience*, 11(8), 877–879. https://doi.org/10.1038/nn.2158
8. She, L., Benna, M. K., Shi, Y., Fusi, S., & Tsao, D. Y. (2024). Temporal multiplexing of perception and memory codes in IT cortex. *Nature*, 629, 861–868. https://doi.org/10.1038/s41586-024-07349-5 (metadata verified; not read)