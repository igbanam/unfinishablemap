---
ai_contribution: 100
ai_generated_date: 2026-10-15
ai_modified: 2026-10-15 07:37:16+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-10-15
date: &id001 2026-10-15
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-15 07:37:16+00:00
modified: *id001
related_articles: []
title: Deep Review - The Manipulation Argument and Hard Incompatibilism
topics: []
---

**Date**: 2026-10-15
**Article**: [The Manipulation Argument and Hard Incompatibilism](/topics/the-manipulation-argument-and-hard-incompatibilism/)
**Previous review**: [2026-07-19](/reviews/deep-review-2026-07-19-the-manipulation-argument-and-hard-incompatibilism/) (and [2026-07-09](/reviews/deep-review-2026-07-09-the-manipulation-argument-and-hard-incompatibilism/))
**Mode**: Post-refine verification pass. The article re-qualified because the 2026-10-14 refine-draft (commit `ac333fd8bd`) moved `ai_modified` past `last_deep_review`. The primary lens is that delta; the secondary lenses are citation fidelity at the publisher of record and tenet alignment.

## Delta Since Previous Review

`git log --since=2026-07-19` on the file shows two commits:

- `fb3c21520d` (2026-08-18, coalesce): link-only. `[[luck-objection]]` re-pointed to `[[quantum-indeterminacy-free-will]]` in `concepts`, the body and Further Reading after the luck-objection concept was merged. No prose change.
- `ac333fd8bd` (2026-10-14, refine-draft, from [pessimistic-2026-10-13-incompatibilism-arguments-wing](/reviews/pessimistic-2026-10-13-incompatibilism-arguments-wing/) Priority items 2 and 4): three body loci.
  - L58: Mickelson (Demetriou) 2010 re-glossed. The old text placed her seam "usually at the 3→4 transition" and in "the involvement of a designing agent"; the new text locates it in an ambiguity in Case 1 whose every coherent resolution involves suppressive, agency-undermining manipulation, and adds that her diagnosis targets the foundational case for every viable version.
  - L60: Jeppsson 2020 re-glossed from a grounding thesis ("grounding responsibility in the agent's own deliberative standpoint") to an epistemic one about which intuitions to trust (engaged identification with fleshed-out fictional manipulated agents vs. the detached stance).
  - L70: Pereboom's case against agent causation split into two strands. The "no positive scientific reason" strand is the parsimony judgement Tenet 5 governs; the wild-coincidences strand is marked as a likelihood argument Tenet 5 does not touch, with the Map's Born-preserving design on that horn. The silent widening of Tenet 5 to "antecedent plausibility" was removed.

The sibling loci the same wing review named were fixed in the same string family: `concepts/source-versus-leeway-incompatibilism` L82 and `topics/event-causal-libertarianism` L90 both now carry the `[[the-manipulation-argument-and-hard-incompatibilism|wild-coincidences argument]]` sentence (1 hit each). The wing is consistent; nothing in this article now contradicts either sibling.

## Pessimistic Analysis Summary

### Verification of the 10-14 Delta

- **L58 Mickelson gloss is faithful.** OpenAlex abstract for DOI 10.1080/00048400903382691 (AJP record), fetched independently this pass: resilience is "the ill-gotten gain from an ambiguity in the description of the causal relations found in the argument's foundational case"; "every metaphysically coherent interpretation invites either a hard- or soft-line reply"; "all viable interpretations of the manipulation cases ... each involves a type of manipulation which undermines the victim's agency"; no argument using "the suppressive variety of manipulation found in Pereboom's argument offers a threat to compatibilism". The article's "description of Case 1 is ambiguous", "every coherent way of resolving it involves a *suppressive* manipulation that undermines Plum's agency" and "aimed at the foundational case itself and is meant to hold for every viable version of it" each track a sentence of the abstract. The closing sentence correctly prevents Pereboom's tune-the-cases rejoinder from reading as an answer to her.
- **L60 Jeppsson gloss is faithful.** OpenAlex abstract for DOI 10.1007/s11098-019-01292-2: "fully fleshed-out manipulated characters in fiction can seem morally responsible"; "we identify with such characters, and therefore focus on their options and the reasons for which they act rather than the manipulation"; "we ought to focus this way when interacting with other agents"; "no reason to trust the incompatibilist intuitions that arise when we regard manipulated agents from a much more detached perspective". The article's epistemic framing ("about which intuitions to trust") is correct and the old grounding gloss is gone.
- **L70 Tenet 5 split is faithful to the tenet.** `tenets.md` L131 reads "Simplicity is not a reliable guide to truth when knowledge is incomplete"; the article now says "Tenet 5 holds that simplicity is an unreliable guide to truth where our knowledge is incomplete" and confines the tenet to the parsimony strand. The symmetric concession ("buys no positive support for agent causation either") survives. The wild-coincidences strand is correctly described as a claim that "the match between free choices and physical statistics would go unexplained", matching L50's exposition of Pereboom, and is left as an open cost. This is the calibration the 07-09 and 07-19 fences protect (reply not decisive), made more exposed rather than less.
- **L68's "live hypothesis pending a toy model" claim still matches its source.** `tenets.md` L107: the strong "genuine selection" claim "is held as a live hypothesis pending a worked toy model rather than as an established result". Faithful.
- **Wikilink targets**: all nine Further Reading / body targets resolve on disk (`free-will`, `the-consequence-argument-for-incompatibilism`, `frankfurt-cases-and-the-principle-of-alternate-possibilities`, `source-versus-leeway-incompatibilism`, `frankfurt-hierarchical-mesh-theory-of-the-will`, `quantum-indeterminacy-free-will`, `agent-causation`, `moral-responsibility`, `tenets`). Tenet anchors `^minimal-quantum-interaction` (L63), `^bidirectional-interaction` (L89), `^occams-limits` (L131) all exist.

### Critical Issues Found
None. The six personas were run against the post-refine text. The Eliminative Materialist, Physicalist, Quantum Skeptic and Many-Worlds Defender all land at the framework boundary (the interface-as-selection reply is a tenet-dependent bet, and the article says so in four places). The Empiricist's one pressure point, that Born-preserving selection is empirically indistinguishable from chance, is conceded in L68 and L70 and is the article's own calibration. The Buddhist Philosopher's no-self challenge to the "genuine originator" is a bedrock disagreement already fenced in `tenets.md` L121. Diagnostic test: a tenet-accepting reviewer would flag nothing as overstated; no possibility/probability slippage.

### Medium Issues Found
None.

### Low Issues Found
- **Lead used the "This is not X. It is Y." construct** (L27: "The danger to the Map is not the incompatibilist conclusion, which the Map already accepts. The danger is hard incompatibilism's second front: ..."). Flagged by CLAUDE.md / the writing-style guide's overused-constructions section; neither prior review touched it. **Fixed**: rephrased as "Since the Map already accepts the incompatibilist conclusion, the danger lies on hard incompatibilism's second front: ...". Same claim, same wikilink, −6 words. "load-bearing": 0 hits before and after.
- **Van Inwagen's rollback (L48) is named without a reference entry.** It is a passing attribution rather than an `Author YYYY` cite, and the rollback is treated at length in [quantum-indeterminacy-free-will](/concepts/quantum-indeterminacy-free-will/), which the sentence links. Not fixed; listed so a future pass does not read it as an orphan cite.

### Citation Web-Verify Ledger (§2.4)

Trigger met: the body around two References entries was modified since the 07-19 review. All four journal entries re-verified at Crossref (publisher-of-record metadata) this pass; the two re-glossed papers also had their abstracts re-fetched from OpenAlex (above).

- Pereboom 1995 (Determinism al Dente) — state: real-correct. Crossref: *Noûs* 29(1), p. 21, issued 1995-03, DOI 10.2307/2215725. (Crossref carries only the first page; 21–45 is the standard range and is unchanged from the 07-09 ledger.)
- Pereboom 2001 (*Living Without Free Will*, CUP, ISBN 9780521791984) — state: real-correct (monograph; unchanged from 07-09 ledger, no web re-check needed).
- Pereboom 2014 (*Free Will, Agency, and Meaning in Life*, OUP, ISBN 9780199685516) — state: real-correct (monograph; unchanged from 07-09 ledger).
- McKenna 2008 (A Hard-line Reply to Pereboom's Four-Case Manipulation Argument) — state: real-correct. Crossref: *PPR* 77(1), 142–159, issued 2008-07, DOI 10.1111/j.1933-1592.2008.00179.x. No abstract at OpenAlex; the gloss (Case 1 as an open question, Case 4 confidence transferring backwards) is unchanged since 07-09 and was not re-litigated.
- Mickelson (Demetriou) 2010 (The Soft-Line Solution to Pereboom's Four-Case Argument) — state: real-correct. Crossref: author "Demetriou", *AJP* 88(4), 595–617, issued 2010-12, DOI 10.1080/00048400903382691. The References entry's "Mickelson (Demetriou), K." correctly records the publication-name/current-name pair. **Content gloss re-verified against the abstract: faithful** (see above).
- Jeppsson 2020 (The agential perspective) — state: real-correct. Crossref: *Philosophical Studies* 177(7), 1935–1951, DOI 10.1007/s11098-019-01292-2; Crossref `issued` is 2019-04-03 (online-first), the issue is 2020, so the article's year is the correct print year. **Content gloss re-verified against the abstract: faithful.**
- Southgate & Oquatre-cinq 2026 / Southgate & Oquatre-huit 2026 — Map self-cites; targets exist.

Inline ↔ References cross-check: every inline year-cite (1995, 2001, 2014, 2008, 2010, 2020) has a References entry and every References entry is cited inline. No orphans. Superlative / currency sweep (`find_superlative_claims`): 0 candidates.

### Attribution Checks (§2.5)
- "wild coincidences" and "disappearing agent" are Pereboom's own terms; the article attributes both to him and presents his concession about agent causation ("could in principle secure the enhanced control ... not incoherent") with the qualifier intact.
- Source/Map separation holds: the interface-as-selection reply is confined to "Relation to Site Perspective" and labelled "one contested answer, not a refutation", "a contested bet rather than a demonstration".
- No self-contradiction: L50 (Pereboom grants that agent causation answers the disappearing-agent worry) and L70 (the Map's leverage is confined to the parsimony strand) are now consistent with each other and with both siblings.

### Reasoning-Mode Classification (§2.6, editor-internal)
- Engagement with Pereboom (hard incompatibilism): **Mixed**. The disappearing-agent objection gets an in-framework answer-candidate (the interface names the settler) that the article explicitly holds at bet strength; the parsimony strand is Mode Three (Tenet 5 boundary-marking, verdict unchanged); the wild-coincidences strand is Mode Three with an explicit open cost. No boundary-substitution, no label leakage (grep for the forbidden editor-vocabulary terms: 0 hits).
- Engagement with compatibilist repliers (Mickelson, McKenna, Jeppsson): expository, not adversarial; no mode to assign.

## Optimistic Analysis Summary

### Strengths Preserved
- The two-front structure and the "partial ally / most dangerous opponent" framing (Chalmers, Kane personas): the article keeps the incompatibilist premise shared and isolates the real disagreement at the luck/control question.
- The post-refine L70 is now the clearest statement in the free-will cluster of what Tenet 5 can and cannot do against Pereboom (Birch persona): it declines a parsimony verdict without claiming support, and leaves the likelihood argument standing. This is the "tenet-coherent, not evidence-elevating" pattern done correctly.
- The soft-line/hard-line taxonomy with three faithful author glosses (Nagel, McGinn personas): the article now gives a reader the actual shape of each reply rather than a Map-convenient version.
- The Stapp persona's point, that the Born-preserving design is simultaneously the Map's escape from the timing objection and the horn of the wild-coincidences argument, is already stated in L68/L70; nothing to add.

### Enhancements Made
- Lead cliché construct removed (one sentence).

### Cross-links Added
None. The Further Reading block already covers every sibling in the cluster; the one reciprocal gap on record (`moral-implications-of-genuine-agency` → this article) is owned by an existing open todo task (todo L7145 notes) and is not minted twice here.

## Length
`analyze_length` (body-only): 2,507 → 2,501 words (−6). Topics band soft 3,000 / hard 4,000; headroom to the hard gate 1,498. Status ok; normal mode.

## Remaining Items
None requiring a task. The van Inwagen rollback mention (low, above) is recorded for information only.

## Stability Notes
- Standing fences from 07-09 and 07-19 hold: Pereboom's luck/disappearing-agent and wild-coincidences objections are granted forceful and undischarged **by design**. Do not re-flag "the Map's reply to Pereboom is not decisive" as critical.
- New fence from the 10-13 wing review, confirmed this pass: **Tenet 5 reaches only the parsimony strand** of Pereboom's case against agent causation. A future review must not re-widen L70 so that Tenet 5 appears to answer the wild-coincidences argument, and must not re-flag "Tenet 5 does not answer the coincidences strand" as a defect; that exposure is the correct calibration and is now mirrored in `concepts/source-versus-leeway-incompatibilism` L82 and `topics/event-causal-libertarianism` L90.
- The Mickelson and Jeppsson glosses are now abstract-faithful; the per-cite ledger above records the verifying sentences so the next pass can skip re-litigation unless L58/L60 change.

## Frontmatter Disposition
Body changed (lead rewording) → `ai_modified` and `last_deep_review` both set to 2026-10-15T07:37:16+00:00. `ai_system` left as `claude-opus-4-8+claude-fable-5-1` (the `claude-fable-5-1` component was already present). `ai_contribution` unchanged at 100.