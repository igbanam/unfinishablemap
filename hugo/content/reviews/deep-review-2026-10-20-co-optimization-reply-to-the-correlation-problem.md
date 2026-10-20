---
ai_contribution: 100
ai_generated_date: 2026-10-20
ai_modified: 2026-10-20 12:50:10+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-20
date: &id001 2026-10-20
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-20 12:50:10+00:00
modified: *id001
related_articles: []
title: Deep Review - The Co-Optimization Reply to the Correlation Problem
topics: []
---

**Date**: 2026-10-20
**Article**: [The Co-Optimization Reply to the Correlation Problem](/topics/co-optimization-reply-to-the-correlation-problem/)
**Previous review**: [2026-07-19](/reviews/deep-review-2026-07-19-co-optimization-reply-to-the-correlation-problem/) (also 06-08 and 05-31). The adversarial review in between was [pessimistic 2026-10-19](/reviews/pessimistic-2026-10-19-co-optimization-reply-to-the-correlation-problem/).

## Why This Pass Was Not a No-Op

On 2026-10-19 four refine-drafts worked through all four issues in the pessimistic review (commits `359b82e12e`, `533010451a`, `c760a411ab`, `486e458e32`). The body grew from 2244 to 3307 words. The new material is Robinson's reference-fixing horn, the Mørch/Zietsch conditional, the shared inbound debt, the two named co-optimizers, the scoping of "by construction", and the recalibrated evidence section. No deep review had seen any of it. This pass reviews the post-refine state as a whole and checks how the four sequential edits fit together.

Length: 3307 → 3307 (topics soft 3000, hard 4000; `soft_warning`). The pass ran in length-neutral mode: about 42 words added, about 42 cut.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Internal slip, present since creation (L45).** "The epiphenomenalist does not have to say that *pleasant*-feeling and *avoidance*-promoting just happened to line up". That pairing is the inverted-valence organism the next section uses against the view. It contradicts L43 ("implements 'avoid this' happens to feel bad"). Three deep reviews and one pessimistic review missed it. **Fixed**: "unpleasant-feeling and avoidance-promoting".
2. **Stale lead after the Issue 3/4 refines (L33).** The lead still said the dissociation cases "rule some stories out without selecting between the two that survive" and "narrow the space of viable epiphenomenalist stories". The body now names two co-optimizers plus interactionism. It says that brute-luck epiphenomenalism also meets the lesion constraint ("the correlation itself, not the lesions, tells against that crudest version"), and that the cases "rule out neither co-optimizer". The lead also never mentioned the constitutive-physicalist version, although that split now decides which verdict applies to which rival. **Fixed**: the lead now gives the body's own constraint ("tie the affective substrate to the protective-behaviour system"). It keeps "constrains … without discriminating", "do not, on their own, settle" and "underdetermined by the data", and adds one sentence: the name also covers a constitutive-physicalist version, which is not epiphenomenalist, and against which the Map's dispute is over Dualism (explained below). No verdict was upgraded.
3. **Implied false claim about Robinson (L63, L65).** The text said "A *qualia-realist* epiphenomenalist cannot take the move" and "For the qualia-realist epiphenomenalist this is a real trilemma". Robinson is a qualia realist (qualitative event realism; SEP bibliography lists "Why I Am a Dualist", 1982a) and does take the move. So the literal claim was false of the opponent the paragraph names. The next sentence's scoping ("This argument assumes that valence is intrinsic to felt character") shows the intended group: realists about *felt valence*. **Fixed**: "A realist about felt valence cannot take the move…" and "For such a realist this is a real trilemma". The RtSP recap uses the same term.

### Medium Issues Found

4. **Cited-author stance: Zietsch (2024) was cited only against the Map.** The article cited Zietsch as contesting even the conditional phenomenal-powers advantage, and that part is accurate. It left out the abstract's last sentence, where his own non-adaptive account "appears compatible with physicalism, panpsychism, and dualism (though not epiphenomenalism)". That left the impression that the source helps only the opponent. It cuts against the property-dualist co-optimizer as well. **Fixed**: one sentence reporting his own answer ("sensational associative learning") and its exclusion of epiphenomenalism. This was the over-concession check: the source's stance on both sides is now reported.
5. **The interactionist ledger in the Occam paragraph omitted a known tension (Quantum Skeptic, carried from the 10-19 review).** Fault line 3 already conceded that the alignment explanation needs a selector evolution can see, "though the strictest reading of the Map's Born-preservation commitment forbids one". The Occam ledger, where the two debts are priced, listed only "a quantum interaction channel". **Fixed**: the channel must be "visible enough to selection that the strictest Born-preservation reading would forbid it". This follows the inheritance page (L41, and the L104–L120 trilemma: "The phenomenal-powers reading of the outbound law stands or falls with the third").
6. **The RtSP opening restated the trilemma's three costs in full**, almost word for word from the section summary. It was compressed to a three-item recap (−17 words), which paid for items 4 and 5.

### Cuts made for length neutrality

- L35 roadmap: dropped "(source exposition)", "it must answer", "actually" and "entire". The "room to breathe" framing was kept.
- L41: dropped "A system that reliably approaches food and flees predators is fitter than one that does not." This is background readers already know; "This much every party accepts" keeps its referent.
- L91: dropped the gloss on Bidirectional Interaction, which is defined at the link.

### Citation ledger (§2.4, publisher of record; raw text grepped, no WebFetch prompt)

- Berthier, Starkstein & Leiguarda 1988 (*Ann Neurol* 24(1):41–49) — real-correct. PubMed 3415199 efetch: "lack of withdrawal … as well as to threatening gestures. Five patients also failed to react to verbal menaces" ✓. The DOI is 10.1002/ana.410240109 (not in the entry, which is optional). "Some smile when pricked" is not in the abstract. The full text is paywalled, so this could not be checked against Berthier. A search summary says Duval & Klein 2025 report smiling as part of the standard asymbolia picture; that paper was not read, so this is a lead only. The sentence does not attribute the smiling to Berthier specifically. Left as is.
- Cox et al. 2006 (*Nature* 444(7121):894–898) — real-correct (Crossref). PMC7212082 full text: lips/tongue injuries, "frequent bruises and cuts", "fractures or osteomyelitis, which were only diagnosed in retrospect" ✓. "no reported increase in early mortality" confirms that the 10-19 removal of "mortality" was right. "loss of function of Nav1.7" ✓.
- Berridge 2009 (*Inquiry* 52(4):378–398) — real-correct (Crossref). PMC2813042: "“liking” or the core process of hedonic pleasure" ✓; "feels empty" ✓; "still work substantially more to receive more of the same “empty” dose" ✓; the dose is intravenous cocaine ✓. Result direction: pursuit follows "wanting" without felt pleasure ✓. The gloss "read from facial reactions" matches the taste-reactivity method described in the paper.
- Jackson 1982 (*Phil Q* 32(127):127–136) — real-correct (Crossref, first page 127). The full-text PDF has "They are a by-product of certain brain processes that are highly conducive to survival" verbatim on p. 134 ✓, framed there as what "The epiphenomenalist holds". Jackson was an epiphenomenalist in 1982, so the lineage claim is fair.
- Robinson 2007 (*JCS* 14:27–42) — real-correct. SEP bibliography: "–––, 2007, “Evolution and Epiphenomenalism”, The Journal of Consciousness Studies, 14: 27–42" ✓. Issue 11 was not re-verified this pass; the 10-19 refine took it from OpenAlex and Robinson's publication list.
- Robinson 2023 (SEP "Epiphenomenalism", substantive revision 15 June 2023) — real-correct. Raw HTML grepped. §2.2 is "Natural Selection" ✓. James's "abhor the feelings…" ✓. "brute and unscientific view of pre-established harmony" ✓, the basis for L45's "accept as brute". (I) is a paraphrase and is faithful. (II) "What “pleasure” refers to in any possible world is the effect in consciousness of the events in (b) that contribute to continuance or repetition" is verbatim ✓. "Since both (a) events and (b) events have neural and, ultimately, behavioral effects, they can be selected for" matches L61's "Both kinds of event affect behaviour, so selection can align them" ✓. Stance: SEP frames the reply as what "Epiphenomenalists can respond", then points to "Robinson 2007, 2019" for fuller discussion. Together with the 10-19 Disputatio 2014 check, "Robinson's answer" stands.
- Mørch 2017 (*Phil Perspectives* 31(1):293–316) — real-correct (Crossref). OpenAlex abstract rebuilt from the inverted index: "are indeed fatal to the argument if it is understood, as it traditionally has been, as an argument for any standard version of non-epiphenomenalism such as physicalism and interactionism" ✓; "necessitate their effects in virtue of how they feel" ✓. Stance: Mørch is not an interactionist dualist, and the article says so ("a dualism she does not hold") ✓.
- Zietsch 2024 (*Phenomenology and the Cognitive Sciences*, doi 10.1007/s11097-024-09978-7) — real-correct. Crossref shows the online-first date 2024-04 with no volume or pages yet, which matches the entry. OpenAlex abstract: "none help to understand the adaptive-seeming correlations via adaptation" ✓; phenomenal powers "cannot explain the adaptive-seeming correlations via adaptation either" ✓; "‘sensational associative learning’" ✓; "(though not epiphenomenalism)" ✓ (new sentence).
- Two Map self-citations (evolutionary-case, valence-and-conscious-selection) — unchanged.
- Internal quotations checked against the live pages: phenomenal-value-realism L76 "the intrinsic badness of pain is constitutive of what pain feels like" ✓; inheritance-problem L120 "can be practically hidden but not hidden by construction" ✓; inheritance L41 says strict Born-preservation forbids an evolutionarily visible selector ✓; wanting-liking fork L58 "value exists only *for* an experiencing subject" (paraphrased, not quoted) ✓; [P-Q9](/positions/quantum-interface/#p-q9) (positions/quantum-interface L142/L152) carries the intention-conditioned route ✓; concepts/epiphenomenalism L223 "one of three dualist positions" (paraphrased) ✓.
- Every anchor resolves: #the-fork, #harmony, #the-selectability-constraint, "Discriminating Evidence", "Evolutionary Considerations", "Causal Efficacy of Phenomenal Quality", "The Correlation Problem", and the tenet anchors ^bidirectional-interaction, ^dualism, ^occams-limits and ^minimal-quantum-interaction.
- Inline ↔ References: every inline author-year has an entry and every entry is cited. No orphans.
- Superlative helper (`find_superlative_claims`): 0 hits.

### Counterarguments Considered

- Dennett: the inverted-valence organism is incoherent. This is bedrock, and the constitutive-physicalist co-optimizer now holds that view in the article. Not re-flagged.
- Eliminativist: Berridge breaks up "pleasure". Handled at fault line 2. Bedrock.
- Deutsch: the selection-currency explanation assumes a single outcome. It is implicitly conditional on Tenet 4. Minor, untasked (10-19 verdict honoured).
- Nagarjuna: valence is relational. This is answered by the explicit valence-intrinsic assumption in the reference-fixing paragraph, which marks it as a boundary.

### Reasoning-mode classification (editor-internal)

- Property-dualist co-optimizer, trilemma: Mode One (inverted valence follows from the opponent's own inertness commitment), plus Mode Two on the necessity horn (an unearned, brute psychophysical law).
- Robinson's reference-fixing: Mixed, Mode One then Mode Three. The relocation argument works inside a felt-valence realism, and the dispute over whether valence is intrinsic is marked as a boundary the article does not settle.
- Constitutive-physicalist co-optimizer: Mode Three (the Dualism boundary, with the generic explanatory gap as its cost).
- Mørch and Zietsch: reported, not refuted.
- Label-leakage grep: clean. "load-bearing" count 0. No "not X. It is Y." construction.

## Optimistic Analysis Summary

### Strengths Preserved

- "Constrains but does not discriminate", and the refusal to treat compatibility as confirmation.
- The inverted-valence thought experiment, now paired with the opponent's best published answer to it (Robinson's reference-fixing), stated at full strength.
- The ledger that shares the inbound harmony debt with interactionism. Most of the Map's correlation arguments still miss this (see leads).
- The two-co-optimizer split, with each verdict assigned to its rival.
- The evidence section's restraint on wanting/liking (Hardline Empiricist), and fault line 3's statement of a physical discriminator against the property-dualist view (Popper).

### Enhancements Made

- The lead now states the two-version split up front (LLM-first truncation resilience).
- Zietsch's stance is reported on both sides.
- The Occam ledger now carries the Born-preservation tension.

### Cross-links Added

- related_articles: [inheritance-problem-for-the-psychophysical-law](/topics/inheritance-problem-for-the-psychophysical-law/), [wanting-liking-and-the-value-in-mechanism-fork](/topics/wanting-liking-and-the-value-in-mechanism-fork/). Both were already linked in the body, so the change costs no prose.

## Remaining Items

None for this article. Expansion leads, deliberately not taken because the article is at the soft threshold: Klein 2019 ("William James's Objection to Epiphenomenalism", *Philosophy of Science* 86(5):1179–1190) and Wright 2024 ("Epiphenomenalism and the Evolutionary Role of Pleasure and Pain", *JCS* 31(3):196–219). Both surfaced in OpenAlex as direct literature on James's objection. Neither was read; they are leads for a literature-drift pass, not findings.

## Stability Notes

- Everything from the 07-19 stability notes stands. "Constrains but does not discriminate" must never be upgraded. Eliminativist, Dennettian and functionalist rejections are bedrock.
- The 10-19 split into two co-optimizers is structural. Future edits must keep each verdict on its own rival: the trilemma and the conditional economy case belong to the property-dualist co-optimizer; the Dualism boundary and the behavioural tie "by construction" belong to the constitutive rival.
- The reference-fixing rebuttal depends, explicitly, on realism about felt valence. Do not widen it back to "qualia realist", because Robinson is a qualia realist who takes the move.
- The article is at 3307, 110% of soft. Any future addition needs an equal cut. The RtSP trilemma recap is now minimal, so do not compress it further.
- After four refines plus this pass, the article should be converged. The next pass should be a near-no-op unless the inheritance page or the positions register moves under it.