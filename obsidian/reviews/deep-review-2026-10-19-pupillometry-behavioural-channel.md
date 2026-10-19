---
title: "Deep Review - Pupillometry as Behavioural-Channel Detection of What the Verbal Channel Misses"
created: 2026-10-19
modified: 2026-10-19
human_modified:
ai_modified: 2026-10-19T20:17:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[topics/pupillometry-behavioural-channel]]"
ai_contribution: 100
author:
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-19
last_curated:
---

**Date**: 2026-10-19
**Article**: [[topics/pupillometry-behavioural-channel|Pupillometry as Behavioural-Channel Detection of What the Verbal Channel Misses]]
**Previous review**: [[deep-review-2026-07-24-pupillometry-behavioural-channel|2026-07-24]] (fifth review, convergence no-op). Earlier: 2026-07-07, 2026-06-03, 2026-05-16 (single-doc), 2026-05-16 (cross-review).
**Word count**: 2443 → 2973 (`analyze_length`; topics soft 3000, hard 4000; status `ok` before and after). Most of the growth is the corrected empirical account plus five new References entries.
**Outcome**: Substantive correction. The article's central empirical claim had never been checked against a primary source, and when checked it did not match. Both `ai_modified` and `last_deep_review` were bumped.

## Why This Target

This was the top deep-review candidate after the driver's exclusions (the scorer's top three were edited today or have open tasks). The only change since 07-24 was a check-links anchor fix. The prior five reviews checked citation **metadata**, but none ever checked the **empirical claims** in the choice-blindness section against a primary source. The 2026-05-16 review could not verify the attribution to Johansson and colleagues, so it softened it to "subsequent groups" without confirming that any such study existed. That made the result-direction and cited-author-stance legs of §2.4 genuinely owed, and they had never been run on this article.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **The core empirical claim was uncited, and its framing conflicted with the primary sources.** The old text said: "Subsequent groups … found that the pupillary channel registers covert detection … on average and at trial-level resolution, in the same participants who proceed to confabulate justifications." It then claimed (old L60) that the pupil shows the swap "was registered by sub-cortical machinery the participant has no first-person access to", which distinguishes it from content the introspector "cannot in principle reach".
   - **The real studies** are Pärnamets, Johansson, Strandberg, Balkenius & Hall 2023 (PsyArXiv preprint) and Grassi, Hoeppe, Baytimur & Bartels 2025 (*Frontiers in Psychology*). The research note had mis-cited the second as "Stedmon et al." and "2024".
   - **The two groups read the pupil effect in opposite ways.** Pärnamets et al. see "effortful rationalization" and say the data "allow us to reject notions that participants are aware of, but fail to report, the manipulations". Grassi et al. see surprise at a noticed mismatch: nearly all participants said afterwards that they had noticed manipulations, the authors conclude "hesitance of reporting" rather than failed detection, and they describe participants as "less introspectively blind than originally portrayed".
   - **Neither group holds the article's reading** of detection without first-person access. The "cannot in principle" contrast was an unlabelled necessity claim.
   - **Trial-level accuracy was overstated.** Grassi Exp. 1 classified manipulated vs control trials at 65.5% and did not predict concurrent report above chance (51.4%).
   - **The no-report trials were weakest in the very experiment the claim relies on.** In Exp. 1, the swaps that were never reported (16 trials from 11 participants) gave a non-significant pupil increase (β = 0.248, p = 0.177).
   - This is source/Map conflation plus a calibration error, so it is CRITICAL.
   - **Fix**: the section was rewritten to cite both studies. It reports their effects and their opposed interpretations, and it names the Map's registration-without-awareness reading as a third reading. That reading is consistent with Rebouillat et al. 2021 ("internal variables continue to be monitored … during CB episodes"), but the pupillary data do not select it. The Relation section now holds it at the tier of *live hypothesis*.
2. **Fabricated literature narrative (old L62).** The old text read: "narrowed and extended across the 2015–2024 window. Some early effect sizes have been revised downward in pre-registered replications; the structural dissociation has survived these revisions in the published series … The literature has converged". No such series exists. The record is two research programmes, one still a preprint, and both are computerised. **Fix**: the paragraph was replaced with the actual evidence base and its limits. These include Grassi's finding that design details strongly modulate choice blindness, with coloured photographs "almost completely" abolishing it. The cautious "not a trial-level lie-detector" conclusion was kept and is now grounded in Grassi's classifier result.
3. **Pattern 2 ("Verbal reports, pupil does not") was contradicted by the one study that measured it.** The old claim was that confabulated content is reported "often without the pupillary signature of effortful problem-solving or surprise". Pärnamets et al. 2023 found *larger* pupil responses and longer RTs on accepted manipulations. **Fix**: the pattern was renamed "Verbal confidence, bodily cost". It now pairs Rebouillat 2021 (failed introspective reports carry higher confidence than genuine ones) with the Pärnamets pupil and RT result, which the authors read tentatively as effortful rationalisation.
4. **Unverifiable quotation (Beatty 1982).** The phrase "task-evoked pupillary responses provide a reliable and sensitive indication of within-task processing load" was in quotation marks. The 07-07 review certified it only as a "faithful paraphrase-grade gloss", which is not verification. It is absent from the abstract (OpenAlex inverted index), and the full text is paywalled; a WebSearch found no source text containing it. **Fix**: the quotation was replaced by a paraphrase of the verified abstract (the TEPR tracks within-task, between-task and between-individual variations in processing demands). The unverified "three decades of work" was dropped.
5. **Dropped qualifier (Joshi et al. 2016).** The old text read: "LC supplies the principal neural correlate: phasic pupil-dilation tracks the LC's burst firing … and in human pharmacological manipulation studies". The abstract says "this relationship is not specific to the LC". It found similar relationships, with later timing, in the inferior and superior colliculi and the anterior and posterior cingulate cortex. The pharmacology clause was uncited and garbled, since pharmacological studies do not record LC firing. **Fix**: the qualifier was restored and the clause dropped.
6. **Wrong citation metadata introduced by a prior review (Mathôt 2018).** The 07-07 review "corrected" the article number from 16 to 18 by reading the DOI suffix (`joc.18`) as the article number. The publisher's JATS XML gives `<elocation-id>16</elocation-id>`, and Crossref gives article-number 16. Grassi et al. 2025 also cite it as "J. Cogn. 1:16". **Fix**: restored to 1(1), 16, with DOI 10.5334/joc.18 kept. **The 07-07 and 07-24 stability notes saying "Mathôt is 1(1), 18" are overturned.**
7. **Misdescribed sibling page (old L102/L104).** The article said the confabulation void's *detection face* cites the choice-blindness pupillometry. In fact the detection face (§"Detection — The Felt Signal Operates Inversely") cites Rebouillat. The pupillometry sits under "Why the Limit Is Genuinely Structural / Replication-survival". **Fix**: both sentences were reworded. L104's "one of the load-bearing empirical anchors" became "one of the empirical anchors", which matches the reduced evidential weight.

### Medium Issues Found

- **"masked emotional faces" (old L68).** The supporting study is Tamietto et al. 2009: unseen expressions shown to the blind hemifield of two cortically blind patients, with arousal measured by pupil dilation. Those faces were not masked. Corrected and cited. The auditory-oddball claim was also cited (Liao et al. 2016: the pupil dilation response to deviants occurs "irrespective whether attention is directed to the sounds or not"). The pattern sentence now flags that unavailable-to-report and merely-unreported are separate questions.
- **Pattern 3's uncited "correlation is positive but partial".** The sign was ambiguous, since the pupil tracks uncertainty, which is the inverse of confidence. It was replaced with Lempert, Chen & Fleming 2015: pupil dilation tracks the inverse of confidence before but not after a decision, and the post-decision link is tighter in better metacognisers. Urai's wording was tightened from "proportional to … weakness" to "scales with decision uncertainty", after the abstract's "after choice but before external feedback".
- **Relation to Site Perspective, internal tension.** The text said the Map "does not over-claim that pupillometry favours its reading", yet also that Dualism "accommodates it more naturally than a reductive identity claim". Since the article itself concedes that a physicalist functional-architecture reading fits the data, the second sentence now says the physicalist architecture predicts the same asymmetry and "the fit is one of consistency, not support".
- **Necessity overclaim.** "the confabulation void guarantees that the verbal channel will retroactively label every action" became "means the verbal channel can retroactively label actions".
- **Lede.** The old lede said pupillometry lets *confabulation* be demonstrated, but the pupil does not demonstrate confabulation. The new lede says it demonstrates a report/body gap, and it front-loads the interpretation split with a named-anchor forward reference. Two "This is not X. It is Y." constructions (lede, and L74 "not a more accurate version … It is a different channel") were rephrased.

### Citation Ledger (publisher of record)

- Beatty 1982 (*Psychological Bulletin* 91(2), 276–292; DOI 10.1037/0033-2909.91.2.276; Crossref): **real-correct** metadata. **Quote unverifiable**, so it was de-quoted (see Critical 4).
- Rebouillat, Leonetti & Kouider 2021 (*Neurosci. Conscious.* 2021(1), niab004; Crossref): **real-correct**. Direction leg: the abstract states "introspective failures are associated with higher confidence than genuine introspective reports", and the article's use matches that direction. Stance: the authors conclude introspection is "neither a direct reading of internal variables nor a mere retrospective illusion", and they are not enlisted for dualism.
- Johansson, Hall, Sikström & Olsson 2005 (*Science* 310(5745), 116–119; PubMed 16210542): **real-correct**. The description of the protocol matches the abstract.
- Joshi, Li, Kalwani & Gold 2016 (*Neuron* 89(1), 221–234; PubMed 26711118): **real-correct** metadata. **Qualifier dropped** in the body; restored (Critical 5).
- Mathôt 2018 (*J. Cogn.* 1(1), **16**; DOI 10.5334/joc.18; publisher JATS plus Crossref): **real-wrong-metadata**. It was 18 (introduced 07-07) and is corrected back to 16.
- Urai, Braun & Donner 2017 (*Nat. Commun.* 8, 14637; Crossref): **real-correct**. Direction leg: pupil dilation reflects decision uncertainty after choice, and the article's use matches.
- Grassi, Hoeppe, Baytimur & Bartels 2025 (*Front. Psychol.* 16, 1598254; DOI 10.3389/fpsyg.2025.1598254; Crossref, published 2025-12-04): **added**. The full PDF was downloaded, and every figure used (65.5%, 16 trials, the "almost completely abolish CB" finding, "less introspectively blind than originally portrayed", "hesitance of reporting") was grepped in the raw text or abstract.
- Pärnamets, Johansson, Strandberg, Balkenius & Hall 2023 (PsyArXiv, DOI 10.31234/osf.io/v85sz, posted 2023-05-31; Crossref): **added**. The record type is preprint, and OpenAlex shows no journal version. The claims used come from the abstract.
- Tamietto, Castelli, Vighetti, Perozzo, Geminiani, Weiskrantz & de Gelder 2009 (*PNAS* 106(42), 17661–17666; Crossref): **added**. Direction: unseen stimuli evoked *higher* arousal (pupil) than seen ones.
- Liao, Yoneya, Kidani, Kashino & Furukawa 2016 (*Front. Neurosci.* 10, 43; Crossref): **added**.
- Lempert, Chen & Fleming 2015 (*PLoS ONE* 10(5), e0126588; Crossref): **added**.
- Inline ↔ References: every inline cite has an entry. Mathôt 2018 is still not cited inline; it is a bibliographic anchor, low priority, and unchanged.
- Empirical-currency helper: zero superlative claims.

### Counterarguments Considered

- **Heterophenomenology (Dennett)**: unchanged, Mode Three. Pupillometry forces attention to channel-level dissociation but does not refute the method.
- **Physicalist deflation**: Mode Three, now applied consistently in the Relation section ("consistency, not support").
- **Grassi-style deflation of choice blindness itself** (participants are less blind than portrayed): new, and now stated at full strength in the body as the source authors' own conclusion.

### Reasoning-Mode Classification (editor-internal)

- Heterophenomenology: Mode Three.
- Physicalist functional-architecture reading: Mode Three (honestly conceded).
- Pärnamets and Grassi interpretations: reported as the source authors' readings, with no refutation attempted. The Map's reading is labelled a third reading that the data do not select.
- No label leakage.

## Optimistic Analysis Summary

### Strengths Preserved

- "The pupil does not register the content of a thought; it registers the cost of having had it." This line now matches the evidence better: Pärnamets' effort reading supports exactly this cost framing.
- The conjunction-probe framing and the negation discipline of "What the Pupillary Channel Does Not Settle", both untouched.
- The three-pattern catalogue structure. Pattern 2's content was corrected, but the structure is unchanged.

### Strength Modified

- "The body knows; the verbal channel does not." became "The body registers the swap; the verbal channel does not say so." The old line rested on the unverified covert-detection-without-access reading. Under Grassi, participants often knew too, and the report simply did not say so. The revised line is accurate under both published interpretations.

### Cross-links Added

- [[topics/authorship-of-action-divergence]]: added to related_articles and Further Reading. It already cites Grassi 2025 and reads it at the same contested register, so the link is reciprocal.

## Remaining Items (report to driver; not edited here)

1. **voids/confabulation-void L79** ("Replication-survival"). It says the choice-blindness finding "has been narrowed by 2020–2021 replication work, but the structural finding is *strengthened* rather than weakened. Pupillometry follow-ups show *covert* detection… The body knows; the verbal channel does not."
   - Grassi et al. 2025 conclude the opposite of "strengthened": their results "cast doubt on the general validity of CB", and participants are "less introspectively blind than originally portrayed".
   - The "2020–2021 replication work" is unidentified. It traces to the research note's "Pärnamets/Stedmon-style" entry, whose quoted phrase about stimulus discriminability looks like Grassi's own work.
   - Not edited: an open P3 task targets confabulation-void (L1662), and the fix is not length-neutral.
2. **concepts/introspection L65**: "pupil dilation tracks manipulated trials even when the verbal channel later misses them … so the figure indexes failed post-hoc verbal access". This applies results from computerised tasks to the 2005 sleight-of-hand figure, and it omits the interpretation split. Not edited: the page is at its gate (3,504/3,500).
3. **apex/introspection-architecture-void-cluster L93**: "Johansson and Hall's pupillometric follow-ups". This is defensible for Pärnamets et al. 2023, where both are co-authors, but not for Grassi 2025. Low priority.
4. **research/voids-confabulation-void-2026-05-14** L107/L112/L227/L314: Grassi 2025 is mis-cited as "Stedmon, A. et al." and as a "2024" paper. These are the seed of the propagation. Research notes are not rendered as articles, but the note will keep seeding errors.
5. narrative-void L54, source-attribution-void L70, introspection-architecture-independence-scoring L87 and authorship-of-action-divergence L59 say the autonomic channel "can register the swap" without the verbal channel flagging it. **These are accurate under both readings, and no action is needed.**

## Stability Notes

- **The choice-blindness pupil effect has two primary sources with opposed interpretations** (Pärnamets 2023: effortful rationalisation without awareness; Grassi 2025: noticed but withheld). Future reviews must not restore a single "covert detection without first-person access" reading. Nor should they present that reading as the literature's, or as anything above *live hypothesis*.
- **Mathôt 2018 is J. Cogn. 1(1), 16** (publisher JATS elocation-id 16; DOI suffix `joc.18` is the submission ID, not the article number). This supersedes the 07-07 and 07-24 notes.
- **The Beatty 1982 quotation must stay de-quoted** unless someone greps the phrase in the full text.
- Carried forward: physicalist disagreement is bedrock (Mode Three); pupillometry is channel/proxy evidence, not a consciousness readout; Rebouillat 2021 is correct (do not revert toward Coutinho).
- The article sits at 2973 words, 99% of soft. Future additions must be length-neutral.
