---
title: "Deep Review - The Consequence Argument for Incompatibilism"
created: 2026-10-15
modified: 2026-10-15
human_modified: null
ai_modified: 2026-10-15T10:23:57+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-fable-5-1
ai_generated_date: 2026-10-15
last_curated: null
---

**Date**: 2026-10-15
**Article**: [[the-consequence-argument-for-incompatibilism|The Consequence Argument for Incompatibilism]]
**Previous review**: [[deep-review-2026-07-19-the-consequence-argument-for-incompatibilism|2026-07-19]] (and 2026-07-09)
**Mode**: Post-07-19 delta pass. Two commits landed since the last deep review: `fb3c21520d` (2026-08-18 coalesce, link-only: `[[luck-objection]]` re-pointed to `[[quantum-indeterminacy-free-will]]`) and `b9d71676f5` (2026-10-14 refine-draft, which discharged Issues 1, 2, 4 and 6 of [[pessimistic-2026-10-13-incompatibilism-arguments-wing|the 10-13 wing review]] plus its L111 language fix). This pass (a) audited the 10-14 rewrite of the modal derivation, (b) checked the 10-14 fixes for stranded string siblings, and (c) worked through the wing review's four *unqueued* low-severity notes on this article, which no task covered.

## Audit of the 10-14 modal derivation (L50)

Checked step by step against the SEP "Arguments for Incompatibilism" step list (fetched live): (1) `□((P0 ∧ L) → A)` by determinism; (2) `□(P0 → (L → A))` by exportation; (3) `N(P0 → (L → A))` by Alpha; (4) `NP0`; (5) `N(L → A)` by Beta from 3, 4; (6) `NL`; (7) `NA` by Beta from 5, 6. The article's rewrite matches this exactly: Alpha is applied only to the necessitated conditional, the past and laws enter as two separate `N` premises, and Beta is applied twice with the right instantiations (`p = P0, q = (L → A)`; then `p = L, q = A`). The closing sentence—that combining `NP0` and `NL` into `N(P0 ∧ L)` would itself be agglomeration—is correct. **No defect.** Note for future passes: the derivation of agglomeration from Beta strictly also uses Alpha (on `□(p → (q → (p ∧ q)))`), but the SEP states the result as "Beta entails Agglomeration" and the article follows that phrasing; since Alpha is uncontested, blaming Beta is the standard and correct attribution. Not a defect; not changed.

## Citation Web-Verify Ledger (publisher of record)

The 07-19 stability note #3 fences the six existing citations as verified; I did not re-verify metadata on those. New or newly load-bearing cites this pass:

- van Inwagen, P. (1975) "The Incompatibility of Free Will and Determinism", *Philosophical Studies* 27(3): 185–199, DOI 10.1007/BF01624156 — **real-correct; added**. The JSTOR/Springer scan was read (first page: "Mar., 1975, Vol. 27, No. 3, pp. 185-199"; opening sentence: "argue that it is incompatible with the thesis that we are able to act otherwise than we do"). The paper uses the "could have rendered … false" vocabulary the article's prose version (L37, "render a law of nature false") inherits. SEP bibliography entry matches.
- van Inwagen, P. (2000) "Free Will Remains a Mystery", *Philosophical Perspectives* 14: 1–19, DOI 10.1111/0029-4624.34.s14.1 — **real-correct; added**. Crossref: "The Eighth Philosophical Perspectives Lecture: Free Will Remains a Mystery", *Noûs* 34 (s14): 1–19, October 2000 (Philosophical Perspectives 14 is the *Noûs* supplement). Claim-match: SEP §5 states verbatim "van Inwagen has conceded that Beta is invalid (van Inwagen 2000)". The article's new sentence says exactly that and no more.
- Finch, A., & Warfield, T. A. (1998) "The *Mind* Argument and Libertarianism", *Mind* 107(427): 515–528, DOI 10.1093/mind/107.427.515 — **real-correct; added**. Crossref confirms title, volume, issue, pages, authors (A. Finch, T. A. Warfield). Claim-match: SEP §5 states "It has also been suggested (Finch & Warfield 1998) that the Consequence argument can be repaired by keeping N and replacing Beta with Beta 2". The article now attributes Beta-2 to them parenthetically instead of leaving "a Beta-2" authorless.
- Fara, M. (2008), *Mind* 117(468): 843–865 — metadata fenced; **content re-checked** at Oxford Academic for the L79 rewrite. Abstract: "the paper concludes by using the dispositional analysis of abilities to argue for compatibilism, and to show why the 'master argument' for incompatibilism is unsound." The abstract does not name a premise. The rewritten L79 therefore says the dispositional reading makes "she could have done otherwise" true of a determined agent and that "the argument's conclusion fails on the reading of 'can' they defend"—which is what the abstract licenses—rather than the old sentence's claim that the "no choice about the laws" premise specifically "trades on an ability … had the triggering circumstances been apt", which named a premise the sources do not single out and did not parse as a claim about that premise anyway (wing review low note).
- Vihvelin, K. (2013) — metadata fenced; **content re-checked** via the NDPR review (Franklin): "to have a narrow ability to act is to have a disposition or bundle of dispositions … determinism is compatible with the narrow ability to do otherwise"; she "focuses her discussion on … van Inwagen's influential third version of the consequence argument that turns on … Beta". Consistent with the rewrite. SEP "Compatibilism" on the new dispositionalists (Smith, Vihvelin, Fara): "we hold fixed the relevant causal base or underlying structure of an agent's disposition … and we consider various counterfactual conditions in which that causal base … operates unimpaired"—the source of the rewrite's "intrinsic properties in virtue of which she would act differently if she tried".
- Lewis (1981) — metadata fenced; **target checked**: the philarchive abstract says Lewis's "incompatibilist opponent is modeled partly after Peter van Inwagen and partly on himself when he first worried about van Inwagen's argument". Lewis (1981) precedes the *Essay* (1983), so the article's L68 "an earlier version of van Inwagen's argument" was right, and it was L27 ("formulated … in *An Essay on Free Will* (1983)") that was wrong. L27 now reads "first set out … in a 1975 paper and given its canonical form in *An Essay on Free Will* (1983)". Internal consistency restored.
- McKay & Johnson (1996) — metadata fenced; PDC landing page re-reached (24(2), Fall 1996, 113–122, DOI 10.5840/philtopics199624219); the DOI is not in the References entry and was not added (the 07-19 ledger verified the entry without it; harmless omission).

**Inline ↔ References**: every inline `Author YYYY` now has an entry (1975, 1983, 2000, Finch & Warfield 1998 added; Lewis, McKay–Johnson, Merlussi, Vihvelin, Fara already present). The "(2008, 2015)" gesture remains a generic pointer per stability note #4.

**Empirical-currency sweep**: `find_superlative_claims` was not needed—the 07-19 run returned nothing and no superlative was added. "widely regarded as the strongest single argument" is attributed reputation, unchanged.

## Pessimistic Analysis Summary

### Critical Issues Found
- **Internal inconsistency on the argument's origin** (L27 vs L68): fixed as above. Factual, not philosophical; the 1975 paper is the origin and Lewis answers it.
- **Stranded string sibling of the 10-14 Lewis fix** (L97). The 10-14 refine replaced the closing "minimally owned miracle" sentence with one saying "no violation is needed … a lawful selection among outcomes physics leaves open", but left the preceding sentence saying the interface is "a lawful-looking but not physically-determined departure from what the prior physical state alone would fix" and that the Map "makes that divergence literal". Under the indeterminism the Map posits the prior physical state fixes no single outcome, so there is nothing to depart from; and Tenet 2's rules-out clause (no Born-statistics violation) means the influence is lawful, not "lawful-looking". The two sentences contradicted each other on whether a law is broken. Rewritten: the interface "settles an outcome the prior physical state alone leaves open, within the Born statistics rather than against them". Tenet-alignment check against `tenets.md` Minimal Quantum Interaction ("biasing otherwise indeterminate outcomes without injecting energy or violating conservation laws"; rules-out: "no Born-statistics violation") passes.
- **Tenet alignment of L91 (10-14 rewrite)**: checked against `tenets.md` Bidirectional Interaction—"The tenet commits to the *that*, not a unique *how*—but it does commit to a *kind* of how: *outcome-selection*", rationale resting on self-stultification and mental causation. The article's "Tenet 3 rests on mental causation, not free will, and commits only to outcome-selection, which a dualist who held conscious contributions to be fixed by prior mental states could also accept" is faithful. The Map's libertarian discharge is correctly presented as a *separate* indeterminist premise plus agent-causal account, not as something Tenets 2–3 force. No calibration slippage: a tenet-accepting reviewer would not flag any claim as overstated.

### Medium Issues Found
- **Banned "This is not X. It is Y." construct** at L64 (wing review low note): "This result does not refute incompatibilism. It refutes *this formulation* of the argument." → "The result refutes *this formulation* of the argument, not incompatibilism."
- **Van Inwagen's own concession omitted** (wing review low note): the section reported repairs without saying the author conceded Beta invalid. One clause added with the 2000 reference. Distinct from stability note #4 (which fences only the "(2008, 2015)" gestures).
- **Dispositional-compatibilist sentence did not parse** (wing review low note) and named a premise the sources do not single out: rewritten per the ledger.

### Counterarguments Considered
- *Many-Worlds Defender*: Everett gives the richest alternative structure — fenced (07-19 note #2), not re-raised.
- *Quantum Skeptic*: "miracle" implies law violation — the 10-14 fix plus this pass's sibling repair now state explicitly that no violation occurs and the Born statistics are respected.
- *Hard-Nosed Physicalist* / *Eliminativist*: the L91 rewrite removes the "whole apparatus … unmotivated" hostage; the remaining disagreement is bedrock.
- *Empiricist*: no empirical claims are made in this article; the luck objection is owned as undischarged (L95).
- *Buddhist Philosopher*: bedrock; not applicable to a leeway-argument exposition.

### Reasoning-mode (editor-internal)
Expository article; no named-opponent refutation is dressed as in-framework. Lewis is engaged as a suggestive parallel with the inversion now marked (Mode Three honesty: the Map's picture needs no miracle because it denies determinism, which is a framework difference, not a refutation of Lewis). Dispositional compatibilists are reported, with their analysis of "can" contested but not refuted. Grep for forbidden editor-vocabulary labels: clean.

## Optimistic Analysis Summary

### Strengths Preserved
- The hard-determinist/libertarian *shared*-argument spine (L87) and the "clears the ground / positive building elsewhere" division of labour (L29, L93).
- The 10-14 modal derivation is now a correct, self-contained statement of van Inwagen's third argument and explains *why* it avoids agglomeration—a genuine improvement a reader can check against SEP.
- The luck-objection calibration (L95) that the 07-11 refine installed and the 07-19 review praised.

### Enhancements Made
- Lewis bridge now internally consistent on lawfulness (L97).
- Beta section now records van Inwagen's 2000 concession and attributes Beta-2.
- Lead now gives the argument's actual origin.
- Three verified references added (1975, 2000, Finch & Warfield 1998).

### Cross-links Added
None—the free-will lattice links were already complete; no new wikilink targets were warranted.

## Length
2,591 → 2,684 words (+93); topics band soft 3,000 / hard 4,000; status ok; headroom to the hard gate 1,315. Below soft threshold, so additive edits were permitted; all four prose edits were near-neutral and the growth is the three reference lines plus one clause.

## Remaining Items
None. The wing review's Issue 3 and Issue 5 concern the sibling articles, discharged in [[deep-review-2026-10-15-the-manipulation-argument-and-hard-incompatibilism|this morning's manipulation-argument review]] and the 10-14/10-15 refines; nothing in this article is left open.

## Stability Notes
Standing fences from 07-09 and 07-19 hold (Pereboom reply not decisive; Everett framing; citation set; "(2008, 2015)" gestures). New fences from this pass:

1. **Origin and derivation are now settled**: 1975 paper as origin, 1983 as canonical form, Lewis 1981 answering the earlier version; the L50 derivation matches SEP's step list. Do not re-flag "formulated in 1983" against "earlier version", and do not re-raise agglomeration at L50.
2. **"Beta entails agglomeration" phrasing** follows SEP; the role of Alpha in that derivation is a footnote-level nicety, not a defect.
3. **Lewis bridge lawfulness**: both sentences at L97 now say no law is violated and the Born statistics hold. A future review must not reintroduce "miracle"/"departure from what the prior state would fix" language for the Map's interface.
4. **Dispositional compatibilists are reported at the level their abstracts license** (ability as disposition; master argument unsound on that reading of "can"). Do not re-specify which premise they reject without reading Vihvelin 2013 ch. 6 or Fara 2008 §6 in full.

**Frontmatter disposition**: body changed → `ai_modified` and `last_deep_review` both set to 2026-10-15T10:23:57+00:00. `ai_system` left as `claude-opus-4-8+claude-fable-5-1` (`claude-fable-5-1` already present). `ai_contribution` unchanged at 100.
