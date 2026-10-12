---
ai_contribution: 100
ai_generated_date: 2026-10-12
ai_modified: 2026-10-12 19:01:00+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-12
date: &id001 2026-10-12
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-12 19:01:00+00:00
modified: *id001
related_articles: []
title: Deep Review - The Observer-Witness in Meditation
topics: []
---

**Date**: 2026-10-12
**Article**: [The Observer-Witness in Meditation](/topics/the-observer-witness-in-meditation/)
**Previous review**: [2026-07-18](/reviews/deep-review-2026-07-18-the-observer-witness-in-meditation/) (also 2026-06-13, 2026-05-26, 2026-04-05, 2026-03-11, 2026-02-05)

## Summary

Seventh deep review. This was the first review of four commits made since 2026-07-18 that no review had examined:
- 091a82dd6c (10-03): the "must still steer a little" carry, which touched the description only.
- 871577643f (10-04): the S19_137 correction at L157.
- 2647461d9f (10-07): the felt-doing wording at L50, the effort-axis table at L60–63, DMN meditation-generality at L83, and two zero-word links.
- 4c64d92e45 (10-04): an expand-topic sibling. Its diff on this file is nil.

Selection: the selector's top pick (`concepts/lawful-appearance-problem`) and #2 (`q3-q4-sliding-boundary…`) were on today's avoid list. Pupillometry had only an anchor fix since its last review. Fitness-beats-truth was edited today. This article was the highest-ranked candidate that had substantive unreviewed changes, was not edited today, and was not on the list.

Length: 3,300 → 3,342 words (+42). The topics thresholds are soft 3,000 and hard 4,000, with the gate at `>=`, so headroom is now 657. The article is in the soft band, so this pass ran in length-neutral mode. About 45 words of trims offset most of the additions.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Result fidelity: Garrison et al. 2013 was misreported at L52.**
   - The article credited Garrison with "the default mode network quieted through disengagement rather than active suppression". Garrison measured the PCC only. The paper says "Further studies will also investigate other regions of the default mode network". In the PMC full text (PMC3734786), "suppress" and "disengag" have zero hits in the body; they appear only in metadata and one reference title.
   - The sentence "the brain signature of witnessing has been reported to differ from that of concentrated effort" gets Garrison's grouping backwards. The abstract places "concentration" with "not efforting" on the PCC-deactivation side. PCC activation goes with "efforting", "controlling", "distraction" and "interpreting".
   - Rodriguez-Larios 2020 compares meditation with rest and with arithmetic, not witnessing with concentration.
   - Rewritten: n = 10 is stated; "not efforting" and "concentration" are shown with deactivation and "efforting" and "distraction" with activation; and the text says "the measure tracks effort and distraction, and in these adepts focused concentration fell on the effortless side".
   - The rewrite also explains why the 10-07 table column is headed "(effort axis)". It agrees with the developmental account at L99–103, where effortful concentration becomes effortless in adepts.
   - Every quoted term was grepped in the OpenAlex and Europe PMC abstract.

2. **Attribution: the Krishnamurti claims at L113 were not in the cited book.**
   - The article said Krishnamurti claimed choiceless awareness "is the only true freedom—that choice itself perpetuates the chooser". I grepped both English scans of the 1954 Gollancz edition (archive.org `dli.ernet.505958` and `jiddu-krishnamurti-the-first-and-last-freedom`, djvu text).
   - "choiceless awareness" occurs 5 times, all in Aldous Huxley's Foreword, before CHAPTER I. Huxley credits the phrase to Krishnamurti ("as Krishnamurti calls it").
   - "chooser" occurs once: "The chooser is in confusion, therefore he chooses". The causal direction there runs from confusion to choosing, and from choice to conflict. That is not "choice perpetuates the chooser".
   - "true freedom" and "freedom is not" have zero hits.
   - Replaced with two verbatim spans, each found once in both scans: "to be aware without choice, because choice brings about conflict" and "The chooser is in confusion, therefore he chooses". A negative control ("The chooser is in delight, therefore he chooses") returned 0. A "(Krishnamurti 1954)" cite was added. The Map's reply at L115 still reads correctly against the corrected statement.

3. **Orphaned References: Gupta 1998 and Stapp 2007 had no inline citation, and Krishnamurti 1954 had no year.**
   - The 07-18 review said "No body↔reference orphans". Checked on (surname, year) in both directions, that was false for three entries.
   - Anchored "(Stapp 2007)" at the quantum Zeno mechanism (L56). This credits the proposal to its originator.
   - Anchored "(Gupta 1998)" at the Advaita *sakshi* exposition (L123).
   - Krishnamurti is now cited as 1954 (see 2). Every References entry is now cited inline, and every inline cite has a References entry.

4. **Cross-article calibration: condition (3) at L157 was treated as a working falsifier, but the sibling article it links to says it is not one.**
   - [brain-stimulation-and-the-witness-mode](/topics/brain-stimulation-and-the-witness-mode/) (L96, L110) argues that the falsifier "tests training-dependence, which the interface reading does not entail". It also says Dualism has "No bearing", because "a stimulation-induced witness would still have" the witness's structure.
   - This page still offered condition (3) as something that would make the dualist reading "face difficulty". A reviewer who accepts the tenets would still flag that as overstated testability.
   - The pointer now reports the sibling's verdict: condition (3) is "weaker than stated", because it tests training-dependence, which the interface reading does not entail, and a stimulated witness would keep the structure the dualist reading cites.
   - Condition (3) itself was kept in the list, so the article still says what evidence would matter.

### Medium Issues Found

- **L195 Summary had not been updated to match the corrected neuroscience.** It still said "what neuroscience now correlates with distinctive brain signatures" and "measurable in the brain". L52 calls the evidence a "thin base … suggestive", and L83 says the DMN correlate is "meditation-general rather than witness-specific". The Summary now reads "what small neuroscience studies have begun to correlate with brain activity along an effort axis" and "has suggestive neural correlates".
- **L185 overstated decentering.** The text said "This 'decentering' is the mechanism of mindfulness-based therapies." Gu et al. 2015 (*Clin Psychol Rev*, mediation meta-analysis; Europe PMC abstract) found strong evidence for cognitive and emotional reactivity, and moderate evidence for mindfulness, rumination and worry. Decentering is not among the mechanisms it lists. Changed to "one proposed mechanism".
- **L183 used undefined abbreviations.** "FA meditation" and "OM meditation" became "Focused-attention practices" and "open-monitoring practices" (−3 words).
- **Trims to offset the additions:**
  - L127: a redundant restatement of the Map/Buddhist contrast was merged into the two-truths clause (−14).
  - L131: a doubled underdetermination clause was compressed (−8). Its meaning was kept, because the 07-18 review relied on it as a calibration flag.
  - L187: a selfhood paragraph that duplicated §"The Self Is Constructed" was compressed (−15).

### Covered by the queue (not fixed)

**Blocked P3 at todo.md L1482.** The task is "the-observer-witness-in-meditation and meditation-and-consciousness-modes still argue the witness 'refrains from influencing matter'". It is blocked on the operator's decision about the Tenet 3 quantifier. Several loci on this page are held under it:
- L3 (description), L36, L38, L42, L58, L65, L89, L111, L147, L169, L189 and L193.
- Each still says, in some form, that the witness does not act ("without selecting", "present yet not acting", "can refrain from influencing matter", "available without intervening").

The description was changed on 10-03 to "yet enough steering to cause its own reports". The lead and summary still say "without selecting". The two disagree, and that disagreement is the subject of the held task. None of these loci was touched.

L65 also carries a "These are not X. They are Y." construction, but it is a held locus and was left alone.

None of the driver's three named queue items is present in this article: no Tegmark decoherence figure, no Zeno arithmetic, no Maier 2018.

### Citation ledger (publisher of record / full text, this run)

- Garrison, K. A., Santoyo, J. F., Davis, J. H., Thornhill, T. A., Kerr, C. E. & Brewer, J. A. (2013), *Front. Hum. Neurosci.* 7, 440, DOI 10.3389/fnhum.2013.00440.
  - Metadata: real-correct (Crossref).
  - Result direction: the article's prior gloss was WRONG (Critical 1) and is now corrected against the abstract and PMC3734786 full text.
  - Cited-author stance: neurophenomenology. The authors draw no metaphysical conclusion, and the article presents none as theirs.
- Rodriguez-Larios, J., Faber, P., Achermann, P., Tei, S. & Alaerts, K. (2020), *Sci. Rep.* 10, 5419, DOI 10.1038/s41598-020-62392-2.
  - Metadata: real-correct (Crossref).
  - Result direction: correct. The full text (PMC7096392) has "alpha and theta instantaneous frequencies tended to converge in the upper theta/lower alpha band (i.e. 7–9 Hz)". The abstract gives n = 43 "highly experienced meditators" and "meditation < rest < arithmetic" for 2:1 occurrence.
- Brewer, J. A., Worhunsky, P. D., Gray, J. R., Tang, Y.-Y., Weber, J. & Kober, H. (2011), *PNAS* 108(50), 20254–20259, DOI 10.1073/pnas.1112029108.
  - Metadata: real-correct (Crossref).
  - Result direction: correct. The abstract says the main DMN nodes were "relatively deactivated in experienced meditators across all meditation types (Concentration, Loving-Kindness, Choiceless Awareness)", which supports L83's "found it quieting in concentration practice too".
- Gupta, B. (1998), *The Disinterested Witness: A Fragment of Advaita Vedānta Phenomenology*, Northwestern University Press. Real-correct (Open Library). It was an orphan and is now cited inline.
- Krishnamurti, J. (1954), *The First and Last Freedom*, Harper & Brothers.
  - Metadata: real-correct. The US Harper edition and the UK Gollancz edition both appeared in 1954, and the Gollancz scan's title page shows 1954.
  - Content: the body's attribution was WRONG (Critical 2) and is now replaced with verbatim spans.
- Stapp, H. P. (2007), *Mindful Universe: Quantum Mechanics and the Participating Observer*, Springer, DOI 10.1007/978-3-540-72414-8. Real-correct (Crossref, 2007; the 2011 second edition is 10.1007/978-3-642-18076-7). It was an orphan and is now cited inline.
- L157 stimulation claims: S19_137 had "reproducibly" induced states, and "only one sham stimulation elicited report of an aura".
  - These are not cited in this article. They rest on [deep-review-2026-10-04-brain-stimulation-and-the-witness-mode](/reviews/deep-review-2026-10-04-brain-stimulation-and-the-witness-mode/), which names its sources: the Vesuna 2020 and Parvizi 2021 full texts, 44 quoted spans string-matched, with a negative control.
  - This article's paraphrase was checked against those quotes and matches.

The `find_superlative_claims` currency sweep was not re-run, because no new empirical superlatives were added. The 07-18 run returned none.

### Reasoning-mode classification (editor-internal)

- Physicalist self-model reading (L73, L165): Mode Three. Unchanged.
- Buddhist no-self (L125–127): Mode Three, with explicit underdetermination. A redundant sentence was trimmed and the boundary is unchanged.
- Krishnamurti (L113–115): Mode Three with constructive reframing. His position is now stated in his own words, so the Map's reply engages what he actually wrote rather than a gloss.
- Production / active-inference readings of stimulation (L157): Mode Three. The article now concedes, as the sibling article does, that condition (3) does not discriminate between them.
- Epiphenomenalist (L147): Mode One with a residue clause. This is a held locus and was not touched.
- No label leakage.

## Optimistic Analysis Summary

### Strengths Preserved

- The two-mode framework and its developmental resolution of the effort paradox (L95–105). The corrected Garrison finding fits it: adepts' concentration sits on the effortless side.
- The honest underdetermination framing in the Eastern-philosophy section.
- The Construction Challenge's distinction between the witness mode and consciousness itself.
- The four-tenet Relation section.

### Enhancements Made

- L52 now gives the reader the effort axis directly, which makes the 10-07 table header "(effort axis)" self-explanatory.
- Krishnamurti's challenge is now stated in his own words.
- All Reference entries are now cited inline.

### Cross-links Added

None. All body wikilinks resolve, and both anchors are live: `meditation-and-consciousness-modes#passive-witnessing` and tenets `^dualism` / `^bidirectional-interaction`.

## Remaining Items (out of scope — reported, not minted)

- `obsidian/apex/altered-states-as-interface-evidence.md` L108 still carries the signature retired from this page on 10-07: "frontal theta, ACC activation", "alpha increase" (where Rodriguez-Larios reports alpha–theta convergence), and "DMN quieting through disengagement rather than suppression". That last clause is the same unsourced gloss removed from L52 here. DMN quieting is meditation-general (Brewer 2011).
- `obsidian/concepts/meditation-and-consciousness-modes.md` L157 has the same Krishnamurti gloss: "'choiceless awareness' is the only true freedom, and any technique … perpetuates the chooser". The cited 1954 book does not say this; see Critical 2. That page has 7 words of headroom against the concepts gate, so any fix there must be net-zero.
- `obsidian/concepts/witness-consciousness.md` L162 states the same stimulation falsifier, condition (2), with no note of the sibling article's training-dependence and "no bearing on Dualism" verdict.
- todo.md L6738 is a pending P3, "Cross-links from optimistic review 2026-07-18 (contemplative-phenomenology cluster)", which adds `non-temporal-consciousness` to this page's `related_articles`. It sits below `## Completed Tasks`, so the parser will probably never select it. The link is still absent.

## Stability Notes

- Carried forward: MWI, eliminativist, physicalist ("adopter/homunculus") and Buddhist no-self objections are bedrock disagreements. Do not re-flag them.
- The Garrison 2013 reading is now the verified one: concentration and not-efforting go with PCC deactivation, efforting and distraction with activation, and the paper says nothing about wider-DMN "disengagement". Do not reintroduce a witnessing-versus-concentration contrast or a DMN-suppression claim attributed to Garrison.
- The Krishnamurti wording is verbatim from the 1954 text and verified in two scans. In that book "choiceless awareness" is Huxley's Foreword phrase crediting Krishnamurti. Do not restore "only true freedom" or "perpetuates the chooser".
- The Tenet 3 "refrains / without selecting" loci are held for the operator. Until the blocked P3 is unblocked, treat them as queued, not as review findings.
- The article stays in the soft band (3,342 words). Further additions should be funded by trims.