---
title: "Deep Review - Compatibilism"
created: 2026-10-19
modified: 2026-10-19
human_modified: null
ai_modified: 2026-10-19T17:30:50+00:00
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
**Article**: [[compatibilism|Compatibilism]]
**Previous review**: [[deep-review-2026-08-02-compatibilism|2026-08-02]] (and [[deep-review-2026-07-13-compatibilism|2026-07-13]])

## Scope Determination

The 08-02 review declared the article converged and said a third pass should be triggered "only by substantive body edits". One body edit has landed since: the 2026-10-14 refine-draft rider (commit `d6689c7f2b`) rescoped L101 from "is what makes the ability-to-do-otherwise *categorical*" to "is what could make … *categorical*, not conditional", because Tenet 3 commits only to outcome-selection. That is a calibration edit with a reason, so it justifies a pass. The question it raises is whether the repair reached the rest of the file. It had not: the same entailment claim survived in the lead (L25) and in the organizing-axis section (L39). The file therefore contradicted itself after the repair, with L101 saying "could make" and L25/L39 saying "requires" and "makes".

Two lenses not run by either prior pass were also applied: a raw-text check of the dispositionalism section against the SEP "Abilities" entry, and a sibling-consistency check against pages created since 08-02 (`assent-before-descartes`, `doxastic-voluntarism`).

## Pessimistic Analysis Summary

### Critical Issues Found

- **Tenet 3 entailment claim left live in two loci after the 10-14 repair (calibration; internal inconsistency).** L25 (lead): "consciousness genuinely selects among quantum-open alternatives, which requires the categorical ability-to-do-otherwise". L39: "because Tenet 3 makes that ability real and physical". `tenets.md` (Bidirectional Interaction definition) commits only to outcome-selection. `concepts/agent-causation` L61 and `topics/event-causal-libertarianism` L88 state that the agency cluster reads the tenet agent-causally, and `topics/the-consequence-argument-for-incompatibilism` L91 notes that a dualist who held conscious contributions fixed by prior mental states could accept the tenet. A tenet-accepting reviewer would flag both sentences. **Fixed**: L25 now says the agency cluster *reads* the selection as the categorical ability and that the tenet itself commits only to outcome-selection, citing [[where-the-substance-commitment-enters]]. L39 now says "the Map's agent-causal reading of Tenet 3 takes that ability to be real". "Genuinely" was dropped from the lead, per `tenets.md` ^tenet-3-standing. A corpus sweep found no other page carrying this defect; positive control: `categorical` grep across the six free-will hubs returns their unrelated uses. `concepts/compatibilism` was the last host.
- **Mask/fink conflation in the dispositionalism section (factual error, anachronistic).** L57 said Vihvelin engineers the analysis "to dodge the 'mask' and 'fink' counterexamples that sank the old conditional analysis". SEP "Abilities" (Maier & Kikkert), read as raw downloaded text, separates the two. The conditional analysis of *ability* (CA) fell to local counterexamples such as Lehrer's 1968 sugar-ball case ("if I had chosen to take the red sugar ball, I would have taken one, but, not so choosing, I am utterly unable to touch one"). Finks (Martin 1994) and masks (Johnston 1992) are counterexamples to the conditional analysis of *dispositions* (CD), and they postdate the CA's refutation by decades. The new-dispositionalist move is a *re-diagnosis*: "it may be that the failures of the conditional analysis of ability were not due to any fact about abilities, but rather to a shortcoming of conditional analyses generally". **Fixed**: the sentence now says the analysis draws on the 1990s metaphysics of dispositions, where masks and finks defeat simple conditional analyses of any disposition, and that the new dispositionalists diagnose the counterexamples that sank the CA as failures of that general kind. The Fara sentence installed by an earlier pass is untouched.

### Medium Issues Found

- **Dispositionalism carried the thinnest reply in the article (08-02 Remaining Item).** The article calls new dispositionalism "among the strongest live challenges" to the Map's premise, and its only reply was a routing to the Consequence Argument. **Fixed in place** with Clarke's reply, adapted from the research note's Host A passage but reworded to what the source supports. The research note glossed Clarke as saying the analysis leaves open "whether the *trying* is up to the agent". The verifiable text, SEP "Abilities" quoting Clarke 2009 p. 339, concerns whether *exercising* the capacity is up to the agent: "even if I have a capacity to A, it is not up to me whether I exercise that capacity". The installed wording follows p. 339 together with the abstract (OpenAlex inverted index: "although there is a kind of capacity to act possession of which is a matter of having a disposition, the new dispositionalism leaves unresolved the main points of dispute concerning free will"). "Who named the view" rests on SEP "Abilities" ("Following Clarke (2009), we may label this view as the 'new dispositionalism'"). Cited-author stance: Clarke is a libertarian-sympathetic theorist who does not claim incompatibilism wins. The text says the analysis leaves the dispute "unresolved rather than settled for either side", and the clause placing leeway at the choosing is marked as the Map's. The "no dedicated page" sentence is kept because it is still true (see Verified Clean).
- **L105 called categorical openness "the very datum" that phenomenology reports.** The clause was attributed ("that the Map takes … to report"), but the Tenet 5 paragraph used it as the ground for discounting parsimony. The Map's own [[free-will]] hub (L82) concedes that "the deliberative data is arguably compatible with both readings". **Fixed**: "datum" became "feature", and the clause now adds "a reading the deliberative data does not settle on its own, as the [[free-will]] hub concedes". Tenet 5 now does only what it licenses, which is to remove the parsimony defeater without upgrading the phenomenological evidence.
- **"The oldest strand, running from Hobbes" contradicted a sibling.** `topics/assent-before-descartes` L112 calls Chrysippus's cylinder "an early compatibilism", and SEP "Compatibilism" §2 dates classical compatibilism "in the modern era" to Hobbes and Hume. **Fixed**: "The classical strand, anticipated by Chrysippus's [[assent-before-descartes|cylinder]] and running in modern philosophy from Hobbes through Hume to A. J. Ayer". This also installs the reciprocal link to a page that links here.

### Low Issues Found

- "Ayer gives *the* crisp twentieth-century statement" became "*a* crisp …". SEP "Compatibilism" cites Hume, Ayer 1954 and Hobart 1934 together for the conditional analysis. Zero words.
- Strawson's in-body parenthetical repeated both paginations, which the References entry already carries. It is trimmed to "(*Proceedings of the British Academy*, 1962)". The dual pagination the 07-13 pass verified stays in References.
- Further Reading gains [[doxastic-voluntarism]], which links here as "the conditions doxastic compatibilists transfer to belief".

### Counterarguments Considered

- Dennett / Churchland: categorical openness is not something introspection reports. This is now conceded in the text through the hub's concession (L105). It remains bedrock beyond that.
- Tegmark: decoherence leaves no quantum-open alternatives at neural scale. Tenet-level bedrock, handled at `tenets.md` and the quantum cluster, and not re-litigated here.
- Deutsch: physics is deterministic under unitary evolution. Tenet 4 bedrock.
- Popper: categorical leeway is unfalsifiable. Bounded by `tenets.md` ^tenet-3-standing. The lead no longer says "genuinely selects".
- Nagarjuna: no persisting agent to own the leeway. Framework boundary, and [[where-the-substance-commitment-enters]] now sits in the lead.

## §2.4 Citation Ledger

The References block and body cites were unchanged since the 07-13 two-pass verification, apart from the one cite added this pass. The journal items were re-resolved at Crossref this pass. The book items carry forward the 07-13 publisher check and were not re-run.

- Clarke, R. 2009 (Dispositions, Abilities to Act, and Free Will: The New Dispositionalism) — **new this pass**, real-correct. Crossref doi 10.1093/mind/fzp034, *Mind* 118(470): 323–351. Content verified via the OpenAlex abstract and the SEP "Abilities" quotation of p. 339. The body paraphrase follows those two sources, not the research note's "trying" gloss.
- Fara, M. 2008 (Masked Abilities and Compatibilism) — real-correct. Crossref doi 10.1093/mind/fzn078, *Mind* 117(468): 843–865.
- Frankfurt, H. G. 1971 (Freedom of the Will and the Concept of a Person) — real-correct. Crossref doi 10.2307/2024717, *JPhil* 68(1), first page 5.
- Bourget, D. & Chalmers, D. 2023 (Philosophers on Philosophy: The 2020 PhilPapers Survey) — real-correct. Crossref and OpenAlex deposit vol 23 **issue 1**, while PhilArchive (the authors' record) gives "23 (11)". The journal numbers articles within a volume, and the Crossref "issue 1" is the platform's single annual issue, so the article's 23(11) follows the journal's convention. No change. The publisher landing page is behind a bot wall (Anubis), so it was not read this pass. The 59% figure was verified twice on 07-13 and is unchanged.
- Strawson, P. F. 1962 — real-correct (07-13 dual-pagination verification carried). Crossref query returned no parseable record this pass, so no new check.
- Ayer 1954, Vihvelin 2013, Fischer & Ravizza 1998, Dennett 1984 and 2003, List 2019 — real-correct, carried from the 07-13 publisher pass and not re-run. Result-direction for Ayer: SEP "Compatibilism" §2.2 cites Ayer 1954 as a classical conditional analysis.
- Inline↔References: Clarke 2009 is cited inline and in References. No orphans in either direction. Superlative scan (`find_superlative_claims`): none.

## §2.6 Reasoning-Mode Classification

- **Vihvelin / Fara (new dispositionalism)**: upgraded from Mode Three with routing to **Mixed**. Clarke's objection is internal to the theory of abilities (Mode One: the analysis does not deliver the "up to me" connection its own target notion needs). The residue is declared as unresolved rather than won, and the Map's placement of leeway is marked as the Map's.
- **List**: Mode One (unchanged; the 08-02 classification stands).
- **Fischer (semicompatibilism)**: Mode Three, honestly declared (unchanged).
- **Frankfurt / Strawson / Dennett**: exposition plus cross-reference (unchanged).
- Label leakage: none. No editor vocabulary in article prose.

## Optimistic Analysis Summary

### Strengths Preserved

- The reinterpret / bypass / relocate axis, including the 08-02 Strawson outlier clause.
- The concede-the-morals, contest-the-metaphysics framing in Relation to Site Perspective.
- Semicompatibilism named as the hardest challenge to the Map's own apparatus.
- The PhilPapers subset-inflation caveat.
- The Fara "co-canonical" sentence and the L101 "could make" rescope (10-14).

### Enhancements Made

- The lead and the axis section now state the tenet's commitment at its actual strength, matching L101 and the free-will siblings.
- Dispositionalism has an in-framework reply instead of only a routing.
- The Tenet 5 paragraph no longer rests parsimony-discounting on a contested datum.
- Stoic precedent acknowledged, consistent with `assent-before-descartes`.

### Cross-links Added

- [[where-the-substance-commitment-enters]] (lead)
- [[assent-before-descartes]] (classical strand)
- [[free-will]] (inline at L105; it was already in Further Reading)
- [[doxastic-voluntarism]] (Further Reading)

## Length

2499 → **2652 words** (`soft_warning`, 106% of the concepts 2500 soft target; hard 3500, headroom 848). The two critical fixes cost about +55, the Clarke reply and reference about +85, and the L105 clause about +13. The Strawson pagination trim paid back about 20.

## Remaining Items

- **No expand-topic task exists for `concepts/new-dispositionalism`.** `research/new-dispositionalism-ability-to-do-otherwise-2026-09-14` recorded the route judgement "build `concepts/new-dispositionalism`; apply Hosts B, C and D regardless". Its changelog entry says "Todo task left for cycle_post", but no such task is in `todo.md` (grep `vihvelin|dispositionalis` over Active Tasks: zero). Hosts B, C and D are unapplied. Clarke 2009 appears nowhere else in the live corpus (keyed on surname+year and on the title "New Dispositionalism"); Clarke's other works appear in six other files. If the article is built, this page's "it has no dedicated page elsewhere in the lattice" clause must become a link. Driver to queue. This is out of contract for deep-review.
- **Research-note gloss to correct before reuse.** The note's Host A–C passages attribute to Clarke the claim that the trying is left unaddressed. The verifiable text (Clarke 2009 p. 339, via SEP "Abilities") concerns the *exercise* of the capacity. Any expand or insert from the note should use the p. 339 wording.
- **Sibling orphan reference (report only).** `concepts/phenomenology-of-choice-and-volition` L198 lists Nahmias, Morris, Nadelhoffer & Turner 2004 ("The phenomenology of free will", *JCS*) in References. None of the four surnames, the title or the year occurs in the body. That page has open todo tasks, so it was not edited. The paper is also the natural citation for the free-will hub's concession that the deliberative data is compatible with both readings.

## Stability Notes

Carried forward from 07-13 and 08-02 and reaffirmed: the compatibilism/Map disagreement (categorical versus conditional or emergent leeway) is a bedrock framework-boundary disagreement. Fischer's "the quantum interface is unnecessary", "the categorical premise is unmotivated" and "List is a cheaper route" are not to be re-flagged as critical.

New this pass:
- The categorical ability is the Map's **agent-causal reading** of Tenet 3, not the tenet's content. All three loci (L25, L39, L101) now agree. A future edit restoring "Tenet 3 requires/makes … categorical" reintroduces the 10-14 defect.
- The dispositionalism paragraph's history is now CA-versus-CD correct. Do not revert to "the mask and fink counterexamples that sank the old conditional analysis".
- The Clarke sentence's "leaves … unresolved rather than settled for either side" is a stance guard and must not be trimmed for length.
- The article is converged on structure and voice. This pass's fixes were propagation and precision defects that a sibling repair and a raw-source lens exposed. Absent a new body edit, the next pass should be skipped, not re-run.
