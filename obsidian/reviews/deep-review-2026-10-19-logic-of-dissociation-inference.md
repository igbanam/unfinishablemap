---
title: "Deep Review - The Logic of Dissociation Inference"
created: 2026-10-19
modified: 2026-10-19
human_modified: null
ai_modified: 2026-10-19T18:17:56+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-19
last_curated: null
---

**Date**: 2026-10-19
**Article**: [[logic-of-dissociation-inference|The Logic of Dissociation Inference]]
**Previous review**: Never (article created 2026-10-19 ~17:06Z). Run as the cross-review chain successor: integrate the article into the clinical-dissociation cluster, plus the full deep-review pass.

## Pessimistic Analysis Summary

Every quoted string (58 after edits) was re-grepped by this review against the raw cached texts: full texts of Shallice 1991, Plaut 1995, Chater 2003, Parr et al. 2018, Fotopoulou 2014 (accepted manuscript), Jonas & Kording 2017 (PLOS XML) and the Gregory 2006 transcript; OpenAlex abstracts, split per DOI so that each quote was matched to the paper it is attributed to; PubMed efetch abstracts for Price & Friston, Carrera & Tononi and Boes et al.; the Michel & Lau abstract; and the OpenAlex abstract of van den Heuvel et al. 2026. 58/58 found, each in the attributed source. The two Map-internal quotes were matched in the hub (L180) and in `concepts/disconnection-neuroscience` (L69). The defects below are fidelity-of-reading defects that a verbatim check cannot see. All of them were found by reading each quote in its surrounding source text.

### Critical Issues Found

- **Dropped qualifier, Shallice 1991 (Defence section)**: "He names three ways to choose among architectures" left out the sentence that follows in the source: "To my knowledge no attempt has been made to distinguish between rival architectures along these lines." The omission made the defence look better equipped than Shallice said it was. Resolution: now "three lines of inquiry that could in principle choose among architectures ... though, to his knowledge, none had yet been tried for that purpose". This also supports the article's own tier-two rule (earned only where rivals have actually been tested).
- **Dropped qualifier, Davies 2010**: "lesion-location findings 'may enhance...'" left out the abstract's "Given such assumptions" (assumptions that "go beyond the subject matter of cognitive psychology"). In an article about bridge assumptions, that condition matters. Resolution: restored as "given assumptions that go beyond cognitive psychology".
- **Scope overreach and dropped qualifier, Bullinaria & Chater 1995**: "argued that such effects depend on scale ... so small-network cases 'are merely artefacts of scale'" generalised from their own rule/exception networks to small-network demonstrations in general. It also dropped "in this context" from "Thus, in this context, connectionism appears to create no additional problems". Resolution: the sentence now names their networks (trained on rules and exceptions), says "their small-network cases", and restores "In that context".
- **Attribution overreach (L80)**: "defenders and critics alike treat the inference as abductive, and none defends a deductive reading" assigned an abductive view to Caramazza, Coltheart and Bullinaria & Chater. Caramazza's own abstract is framed as a claim about *valid* inference "given certain assumptions", and the Coltheart and B&C abstracts make no abductive claim. Resolution: replaced with the claim the sources do support. None holds that a dissociation *by itself* entails a component: Caramazza's validity claim is conditional, Shallice denies entailment, Davies makes the step IBE.
- **Attribution framing, Van Orden, Pennington & Stone 2001**: the article set their "predicated on modularity being true" against Shallice ("a reading Shallice's 'in no way entails' passage resists"). But their abstract attributes the predicate claim *to* Shallice: "(T. Shallice, 1988)". The two claims are also logically compatible: if dissociations do not entail modules, inferring modules requires presupposing them. Resolution: now "Citing Shallice (1988), they hold that ...", with the parenthetical dropped. Their "questions the utility of assuming modularity" is added from the abstract, and the fractionation clause is re-worded to the abstract's causal structure ("modularity's failure to converge perpetuates ..."). Shallice 1988 is added to References (Crossref 10.1017/CBO9780511526817, CUP), so the inline citation is paired.

### Medium Issues Found

- **Gregory framing (L62)**: "A classic statement of the transparency worry is itself a radio analogy" presented a 2006 interview as the classic statement. The 1961 paper was not seen, and it has not been verified that it uses a radio. Resolution: "Richard Gregory, whom Shallice cites for the transparency worry, states it with a radio analogy". Shallice 1991: "Gregory (1961) has pointed out that this is often not the case in machines" (raw text).
- **Shallice's lapse scoped too narrowly (L96)**: "marks this domain as the one where it runs without its safeguards", in a consciousness section, read as consciousness-specific. In the source, the scruples lapse across Chapters 12–16 (knowledge, visual attention, supervisory operations, memory and consciousness). Resolution: "marks these higher-level domains, consciousness among them". A redundant clause repeating the functionalist conclusion was also trimmed.
- **Superlative "the field's leading methodologist"**: softened to "one of the field's leading methodologists". The later "leading defender" is now "A leading defender".
- **Transparency gloss duplicated the subtractivity gloss (L44)**: "the impaired performance shows the normal structure minus what was lost" was nearly word-for-word the subtractivity gloss in L46. Resolution: "impaired performance reveals which part was damaged", which follows Shallice's wording ("the relation between damage to a subcomponent and impaired task performance is fairly transparent").
- **Carrera & Tononi comparator missing**: "seems to relate more consistently" had no comparator. The abstract's comparator is focal diaschisis. Added "than the focal form".
- **Lesion network mapping currency (open item 1)**: Boes et al. 2015 carried the anatomical non-locality claim with no mention of the live specificity dispute. Resolution: a hedged three-sentence addition. (a) van den Heuvel et al. 2026 (*Nature Neuroscience* 29(5):1237–1247; Crossref verified) argue that LNM maps local changes onto "the same nonspecific properties" of the normative connectivity data (OpenAlex abstract, raw). (b) Boes, Fox and colleagues reply in a bioRxiv preprint that specificity testing supports it (Siddiqi et al. 2026, doi 10.64898/2026.02.24.707529; Crossref `posted-content`, institution bioRxiv; abstract: "LNM provides evidence for meaningful differences using specificity testing"). (c) The diaschisis evidence predates the method (2014 vs 2015) and does not rest on it. Also seen and not cited: Petersen et al. medRxiv 2026 (2,950 stroke patients; one-sample designs reproduce the convergence, case-control designs do not), Treeratana et al. bioRxiv 2026 (symptom-LNM convergence on the connectome's first principal component), Cui et al. bioRxiv 2026, Edelman et al. medRxiv 2026. The dispute is unsettled, and the hedge says only that.
- **"The criterion presupposes comparable measures" (L42)**: the referent was ambiguous. Now "The double-dissociation criterion".

### Citation Ledger (publisher of record: Crossref API for all DOIs; content as noted)

- Boes et al. 2015 (*Brain* 138(10):3061–3075) — real-correct. Quote verified against the PubMed abstract (PMID 26264514).
- Bullinaria & Chater 1995 (*Lang Cogn Process* 10(3–4):227–264) — real-correct metadata; body reading fixed (critical issue above).
- Caramazza 1986 (*Brain and Cognition* 5(1):41–66) — real-correct. The *Brain and Language* misprint in Coltheart's abstract was not propagated.
- Carrera & Tononi 2014 (*Brain* 137(9):2408–2422) — real-correct; comparator restored.
- Chater 2003 (*Cortex* 39(1):167–169) — real-correct. Quotes and the three constructions checked against the full text (prawn/peanut, javelin/shot-put, backup strategies). The "different parts of one hand" gloss paraphrases Chater's "patterns of pressure on the skin ... are different".
- Coltheart 2017 (*Cogn Neuropsychol* 34(7–8):397–402) — real-correct.
- Davies 2010 (*Mind & Language* 25(5):500–540) — real-correct metadata; qualifier restored.
- Dunn & Kirsner 1988 (*Psychol Rev* 95(1):91–101) — real-correct.
- Farah 1994 (*BBS* 17(1):43–61) — real-correct. "More plausible ... when the locality assumption is abandoned" matches the abstract.
- Fotopoulou 2014 (*J Neuropsychol* 8(1):1–19) — real-correct. Her non-dualist use of "mind-brain interface" is not recruited.
- Gregory 2006 interview (Web of Stories, story 42) — real-correct. Transcript re-read: "very, very broadly" refers to localisation.
- Jonas & Kording 2017 (*PLOS Comput Biol* 13(1):e1005268) — real-correct. "A subset of transistors that makes one of the behaviors (games) impossible" supports "abolished exactly one game".
- Machery 2012 (*Phil Sci* 79(4):490–518) — real-correct, direction checked. "The former" in his abstract is the function-to-structure (imaging) inferences, which fare worse. The article has the direction right, and Machery is a relative defender.
- Michel & Lau 2021 (*Psychol Rev* 128(3):585–591) — real-correct.
- Parr, Rees & Friston 2018 (*Front Hum Neurosci* 12:61) — real-correct.
- Phillips 2021 (*Psychol Rev* 128(3):558–584; OpenAlex lists the 2020 online year) — real-correct.
- Plaut 1995 (*J Clin Exp Neuropsychol* 17(2):291–321) — real-correct. "Contrary to Caramazza's (1986) transparency assumption" and "different random instances of equivalent lesions can have qualitatively different effects" are in the full text.
- Price & Friston 2002 (*TiCS* 6(10):416–421) — real-correct.
- Shallice 1988 (CUP, doi 10.1017/CBO9780511526817) — real-correct, newly added; cited only as Van Orden et al.'s source, not quoted.
- Shallice 1991 (*BBS* 14(3):429–438) — real-correct metadata; qualifier restored (critical issue above).
- Shallice 2015 (*Cogn Neuropsychol* 32(7–8):385–411) — real-correct. "The bridge principles" is in his abstract.
- Siddiqi et al. 2026 (bioRxiv preprint) — real-correct, newly added, labelled as a preprint.
- Teuber 1955 (*Annu Rev Psychol* 6:267–296) — real-correct (volume 6, not Plaut's misprinted 9). Credit only.
- van den Heuvel et al. 2026 (*Nature Neuroscience* 29(5):1237–1247) — real-correct, newly added.
- Van Orden, Pennington & Stone 2001 (*Cognitive Science* 25(1):111–172) — real-correct metadata; framing fixed (critical issue above).
- Inline ↔ References: 25 external entries, each cited inline; every inline author-year has an entry. No orphans in either direction (checked on author-year pairs).
- Superlative/currency sweep: the only superlatives are "the weakest at tier three" (a Map comparative, argued in its section) and the softened "leading" phrasings. The empirical currency item was LNM, now handled.
- Result-direction leg: Machery's direction, Bullinaria & Chater's (large networks: single dissociation only), Price & Friston's (lesions hide degenerate systems), and Phillips vs Michel & Lau were each checked against the abstract. No inversions.
- Cited-author-stance leg: Shallice, Coltheart, Machery and Bullinaria & Chater defend the method. Plaut, Chater, Dunn & Kirsner and Van Orden et al. press against it, and each keeps a role for dissociations. Farah offers an alternative inference scheme. Parr/Friston and Fotopoulou are physicalist lesion-modellers, labelled as such. None is presented as endorsing the Map's conclusion.

### Counterarguments Considered

- **Churchland / Dennett (report-based measures)**: the consciousness section already concedes that awareness is measured by report and that criterion shifts can make or unmake dissociations (Phillips vs Michel & Lau). No change needed.
- **Popper's ghost (is the tier scheme testable?)**: tier two is defined by modelled-and-failed rivals, which makes it falsifiable case by case. The Shallice qualifier restored above makes that criterion bite on the defence too.
- **Nagarjuna (reification of components)**: this is the article's own thesis at tier three; nothing to add.
- **Tegmark / Deutsch**: no quantum or MWI claims. The Minimal Quantum Interaction paragraph only removes an extent inference. No No-Many-Worlds paragraph, correctly (no substantive connection).
- **Method/history necessity audit**: no necessity vocabulary ("inevitable", "built into", "cannot in principle", "structurally" all absent). "Why Consciousness Dissociations Sit Lowest" is a *Map reconstruction*: same bridge assumptions plus an extra report-criterion hurdle, and Shallice's lapse. It is argued in its section, and the tiers are labelled "the Map's construction". It passes the transition check, since no origin-to-validity step is made.
- **Reasoning mode (editor-internal)**: engagement with the functionalist reading is Mode Three. Both readings presuppose tier three, and the article declares that neither gains. No label leakage (forbidden-label grep: 0 hits).

## Optimistic Analysis Summary

### Strengths Preserved

- The neutrality frame: the article "calibrates the Map's own inference and argues neither against dualism nor for it". The Hardline Empiricist persona singles out this restraint: tenet-coherence is never used to upgrade anything.
- The Occam's-limits paragraph, which turns the Map's fifth tenet on its own evidence ("owes the same caution to a parsimony inference that happens to favour its interface vocabulary"). The Mysterian and Property Dualist personas rate this the page's most distinctive move.
- The three-tier scheme, labelled as the Map's construction, and the "None of this makes dissociations uninformative" anti-overcorrection paragraph.
- Gregory's radio, turned against the hub's radio. The Jonas & Kording designed-system counterpart.
- Scope discipline on predictive processing: one paragraph, lesion model only.

### Enhancements Made

- Five critical fidelity repairs and six medium repairs (above). The LNM specificity dispute is now hedged at source.
- The `{#three-tiers}` and `{#bridge-assumptions}` heading IDs and both heading texts are unchanged (driver item a). The hub's three anchored links resolve in the Hugo copy.

### Cross-links Added (inbound, to this article)

- [[disconnection-neuroscience]] — one new sentence closing the production-vs-channel paragraph (L67): both readings presuppose that a syndrome isolates one discrete component, a step that needs contested bridge assumptions. It links `#bridge-assumptions`. 1880 → 1919 words (concepts, ok).
- [[blindsight]] — zero-word piped link on "double dissociation" (blindsight vs lucid dreaming, L68). 2930 → 2930.
- [[recognition-void]] — zero-word piped link on "fractionates into separately damageable sub-systems" (Relation to Site Perspective, Dualism, L118). 2478 → 2478.
- [[thought-insertion]] — zero-word piped link on "double dissociation" (L78, where the page already questions the cited dissociation). 3135 → 3135.
- [[anarchic-hand-and-action-ownership]] — zero-word piped link on "double dissociation" (L68, "That double dissociation is the structural point"). 2649 → 2649.
- Skipped: `capgras-delusion-and-the-affective-recognition-channel` (it defers the Capgras–prosopagnosia double-dissociation argument to recognition-void, which now carries the link); `apex/cross-modal-capability-division` (5004, over hard; low relevance); `anosognosia-and-the-reversible-self-monitoring-channel` (its "a few double dissociations appeared" reports data, so a methodology link adds little).

### Hub consistency check (driver item a)

`topics/neurological-dissociations-as-interface-architecture` now cites this article at L49 ("only on contested assumptions, which are architecturally distinct", linked to `#three-tiers`), L172 ("separate failure is earned robustly, the channel architecture only on contested assumptions", linked to `#bridge-assumptions`) and L198 (finite, individually disableable components "presupposes transparency and locality"). All three match the article: tier one robust, tier three needs bridge assumptions, and L108's minimal-quantum sentence is nearly verbatim. L61's piped text ("the specific way it breaks reveals its internal structure") is the folk reading the article qualifies. That is acceptable as a pointer to the critique. The hub was not edited.

## Length

`analyze_length` 3071 → 3262 (topics soft 3000 / hard 4000; gate at ≥4000, 737 words of headroom). Split (whitespace tokens, same method before and after): prose 2541 → 2664 (+123, still below soft), References + Further Reading 551 → 622 (+71, three new entries). The prose growth funds the five critical repairs and the driver-requested LNM hedge. Two redundant clauses were trimmed to offset part of it.

## Remaining Items

- A P3 refine-draft follow-up was minted for tier-three double-dissociation phrasings in four cluster hosts (recognition-void L118 and capgras L37 "establishes"; blindsight L68's cross-literature blindsight/lucid-dreaming pairing; anarchic-hand L88 "which shows authorship is an interface signal").
- Report-only: `concepts/disconnection-neuroscience` L65 calls the hub's reading "the four-channel reading", while the hub and this article say six channels. This may mean four channel *groups* (the hub lead's ascending/descending/self-model/bilateral). Not changed.

## Stability Notes

- The tier scheme is the Map's construction. Future reviews should not re-flag "no author proposes three tiers": the article says so at the head of the section.
- Physicalist and functionalist personas will reject the Map's interface vocabulary. The article does not argue for it, so that is bedrock, not a defect here.
- The LNM specificity dispute is live (2026). Re-check currency at the next review rather than treating the hedge as settled. Do not upgrade either side without a peer-reviewed resolution.
- The Van Orden et al. passage rests on their abstract only (full text Cloudflare-blocked). Do not reinstate a Shallice-contrast reading of it without the full text.
