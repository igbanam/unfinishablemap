---
title: "Deep Review - Source versus Leeway Incompatibilism (2026-10-15)"
created: 2026-10-15
modified: 2026-10-15
human_modified: null
ai_modified: 2026-10-15T12:09:16+00:00
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
**Article**: [[source-versus-leeway-incompatibilism|Source versus Leeway Incompatibilism]]
**Previous review**: [[deep-review-2026-07-19-source-versus-leeway-incompatibilism|2026-07-19]] (and [[deep-review-2026-07-09-source-versus-leeway-incompatibilism|2026-07-09]])
**Word count**: 2,096 → 2,147 (+51); concepts band soft 2,500 / hard 3,500; headroom to the hard gate 1,352

**Mode**: Post-07-19 delta pass. One commit landed since the last deep review: `d6689c7f2b` (2026-10-14 refine-draft), which discharged Issues 3, 4 and 7 of [[pessimistic-2026-10-13-incompatibilism-arguments-wing|the 10-13 wing review]] at L58 and L82 and added two References entries (Timpe 2007, Pereboom 2003). This pass (a) checked L82 against `tenets.md` L131 and the two sibling articles, (b) swept the file for stranded string siblings of the 10-14 fix, the defect shape both sibling deep reviews found today ([[deep-review-2026-10-15-the-manipulation-argument-and-hard-incompatibilism|manipulation]], [[deep-review-2026-10-15-the-consequence-argument-for-incompatibilism|consequence]]), (c) web-verified the new References surface and re-verified the one verbatim quote in the body at the raw source, and (d) worked through the wing review's two unqueued low notes on this article (its table rows for L44 and L74).

## Pessimistic Analysis Summary

### Critical Issues Found

- **Quote fidelity at L51 (critical, fixed).** The body quoted Pereboom as saying the agent's action "results from a deterministic causal process that traces back to factors beyond his control". Google Books search-within-volume on *Living Without Free Will* (id `WTfvhJw9kiAC`; control query "Professor Plum" returned pp. 106, 111, 121) returns **0 hits** for "traces back to factors beyond his control" and 8 for "deterministic causal process that traces back"; the verbatim span is p. 3, "result from a deterministic causal process that traces back to factors beyond **one's** control", with the condition restated at pp. 34 and 54 as "a deterministic process that traces back to causal factors beyond the agent's control". *Free Will, Agency, and Meaning in Life* (`XrmcAgAAQBAJ`) has "traces back to factors beyond the agent's control" (pp. 6, 73). The article's "his" and "results" were silent adaptations inside the quotation marks (the research note L73 carries the same adapted string). **Fixed**: the quotation marks now enclose only the verbatim span, "a deterministic causal process that traces back to factors beyond one's control", with "(Pereboom 2001, p. 3)" added. Zero net change in sense; the sentence's gloss ("across the four cases", "a claim about causal *history*") was not inside the quotes and is correct (2014 p. 6 states the manipulation argument's core idea in exactly those terms).

- **Stranded string sibling of the 10-14 Tenet 5 fix at L66 (critical, fixed).** The 10-14 edit scoped the luck objection at L82: "Pereboom aims his luck objection at event-causal sourcehood and grants that agent causation could answer it", with the case against agent causation split into a parsimony strand (Tenet 5 reaches it) and the wild-coincidences strand (Tenet 5 does not). L66 still carried the pre-10-14 unscoped form: "the indeterminism our physics might supply cannot restore it (it adds luck, not control)", which presents the luck objection as Pereboom's whole case against indeterministic restoration and so contradicts L82 within the same article. Same shape as the consequence article's L97 "divergence literal" sentence found this morning. **Fixed**: L66 now reads "event-causal indeterminism adds luck rather than control, and agent causation, which he grants could in principle supply the control, would on his view require coincidences too wild to credit." The paraphrase is anchored to the verified text: 2001 p. 80 "wild coincidences implied by this proposal make it incredible", p. 82 "coincidences so wild as to render the proposal incredible" (search-within, 5 hits for "wild coincidences"). No other line in the file now lets Tenet 5 answer the coincidences strand: the only Tenet 5 occurrence is L82, and the only "luck" occurrences are L66 (now scoped) and L84 ("luck and manipulation debates", a pointer).

### L82 Alignment Check (the primary lens)

- `tenets.md` L131: "Simplicity is not a reliable guide to truth when knowledge is incomplete." L82 confines Tenet 5 to "a parsimony judgement Tenet 5 lets the Map decline to treat as decisive", with the symmetric concession ("buys the Map no positive support either") intact, and names the wild-coincidences argument as "not a parsimony point and which Tenet 5 does not answer". Faithful to the tenet.
- Sibling wording: `topics/the-manipulation-argument-and-hard-incompatibilism` L70 and `topics/event-causal-libertarianism` L90 both carry the `[[the-manipulation-argument-and-hard-incompatibilism|wild-coincidences argument]]` sentence (grep: 1 hit each, plus L82 here). The three are consistent; the manipulation review's new fence (Tenet 5 reaches only the parsimony strand) is honoured.
- Tenet 3 at L82: "is why the Map wants sourcehood, though it does not entail it: the tenet commits only to outcome-selection" — matches `agent-causation` L61 and `tenets.md` L57's "does not entail" scoping, and the lead's "located among the options rather than proved by them". L80's "That is a sourcehood commitment, and it is what agent causation supplies" states what the Map wants, not what a tenet forces; no stranded "non-negotiable" sibling survives (grep: 0).

### Citation Web-Verify (per-cite ledger)

Trigger: the References block changed on 10-14 (two entries added) and L58 was rewritten from Timpe 2007. Entries the 07-09 pass balloted at the publisher and the 07-19 stability note fences (Timpe 2008, Pereboom 2001/2014 ISBNs, Fischer & Ravizza 1998, McKenna & Pereboom 2016, McKenna & Coates SEP) were not re-balloted for metadata.

- Timpe 2007, "Source Incompatibilism and Its Alternatives", *APQ* 44(2), 143–155 — **real-correct**. The PDF on Timpe's site was fetched and extracted locally (`pdftotext`, 5,722 words); greps confirm all three L58 claims: "widely accepted taxonomy" (L73 of the extract), "Through a series of papers beginning in 2001, Michael McKenna has cemented the term 'Source Incompatibilism' into the current taxonomy", and the Pereboom passage "We might call those incompatibilists who incline towards the view that an alternative possibilities condition has the more important role ... leeway incompatibilists, and those ... source incompatibilists" with note 3 "Pereboom 2003: p. 186". The "coincidences so wild as to make it incredible" quotation the wing review relied on is also present.
- Pereboom 2003, "Source Incompatibilism and Alternative Possibilities", in Widerker & McKenna (eds), *Moral Responsibility and Alternative Possibilities*, Ashgate — **real-correct** (pp. 185–199; Timpe's note 3 cites p. 186, inside that range). Page range not added to the entry; optional.
- Pereboom 2001, *Living Without Free Will* — **real-correct metadata; body quote was real-wrong-wording**, corrected as above (p. 3 added inline).
- Frankfurt 1969 — **inline ↔ References orphan, fixed**: "In 1969 Harry Frankfurt constructed" had no References entry across three reviews. Added in the form the sibling Frankfurt-cases article uses (family-consistent): *The Journal of Philosophy*, 66(23), 829–839, doi 10.2307/2023833.
- Vihvelin, SEP "Arguments for Incompatibilism" — the L38 paraphrase ("lacking the ability to do otherwise could undermine the self-determining control that sourcehood requires") was grep-confirmed against SEP §2 by the 10-13 wing review (its L53 low note); today's WebFetch of the entry returned the sourcehood/"ultimate source" passages consistent with it. **real-correct**.
- Result-direction leg: Pereboom 2001 and 2014 both report the manipulation argument as a causal-history (source) argument, in the direction L51 states; 2014 p. 6 calls this "the core idea". Cited-author-stance leg: Pereboom is presented as a source incompatibilist who denies free will (L66–68), which is his stance; Fischer is presented as a semicompatibilist (L74), which is his; Timpe as defending "a version of source incompatibilism" (L58), which is his (wide source incompatibilism). No author is presented as endorsing the Map's conclusion.
- Superlative sweep: `find_superlative_claims` not run — the file has no "record / largest / first to / to date" claims by inspection (the only "first" is "the first step" at L28 and "first instinct" at L80, neither empirical).
- Kane and Stump (named in the driver brief) are not cited in this article; nothing to verify.

### Medium Issues Found (wing review's unqueued low notes on this file)

- **L44 "Most compatibilists were persuaded; most incompatibilists were not"** — a survey claim with no survey behind it, and in tension with the next sentence, which has incompatibilists retreating to source (i.e. conceding). **Fixed**: "Compatibilists largely welcomed the result; incompatibilists split between resisting it and conceding it." The following clause already documents both halves (flicker/dilemma defences = resisting; retreat to source = conceding).
- **L74 "Fischer's own template is the one every source theorist builds on"** — a false universal; Kane's ultimacy condition and G. Strawson's Basic Argument are source-style and were not built on *Responsibility and Control*. **Fixed**: "The actual-sequence emphasis is shared across the aisle rather than owned by either side", which keeps the sentence's actual point (the taxonomy is not a proprietary incompatibilist device) without the overclaim. The preceding "structurally, what you get by taking Fischer's actual-sequence emphasis and *adding* ..." is a structural description and stands.

### Counterarguments Considered

- Eliminative Materialist / Hard-Nosed Physicalist (wing review L58: "ultimate source" is a folk posit with no neural counterpart) — bedrock; the article already says the taxonomy "carries no commitment to dualism" and does not claim the condition is met. Not re-flagged.
- Buddhist Philosopher (wing review L73: "the causal buck never stops with her" treats the absence of an originator as a defect) — L36 is exposition of the source-incompatibilist intuition, not the Map's verdict; bedrock. Not re-flagged.
- Quantum Skeptic / Many-Worlds Defender — the article makes no quantum or branching claim beyond pointing to the tenets at L80 and deferring the "is it met" question to the quantum-interface article at L84. Nothing to engage.
- Empiricist — the two survey/universal claims at L44 and L74 were the empiricist's targets and are fixed above.

### Reasoning-Mode Classification (editor-internal)

- Engagement with Pereboom (hard incompatibilism, L66–68 and L82): **Mixed** — the parsimony strand is Mode Three (Tenet 5 boundary-marking, verdict unchanged, symmetric concession kept); the wild-coincidences strand is Mode Three with the cost left open ("which Tenet 5 does not answer"); L66 now describes both of his strands in his own terms without answering either. No boundary-substitution; label-leakage grep 0 hits.
- Engagement with Fischer (semicompatibilism, L72–74): exposition, not reply; the article uses his framework to show the taxonomy's neutrality. No mode to assign.

## Optimistic Analysis Summary

### Strengths Preserved

- The lead's "located among the options rather than proved by them" and the "Source Incompatibilism Is Not Libertarianism" section remain the article's sharpest calibration points (Birch persona: the Map's own position is named as a bet throughout; no tier is upgraded on tenet-load).
- The hub structure (L46–54) that maps the three topic arguments onto leeway / source / pivot is unchanged.
- The wide-source placement at L80 (Chalmers / Kane personas) is kept exactly as the 07-09 and 07-19 passes left it.

### Enhancements Made

- L51 now carries a page-cited verbatim Pereboom span rather than an adapted one.
- L66 now states both of Pereboom's strands against indeterministic sourcehood in the same scoping L82 uses, so a reader meets no contradiction between the two sections.
- References block now closes the Frankfurt 1969 orphan.

### Cross-links Added

- None. The Further Reading block already covers every sibling in the wing; no new link was warranted.

## Remaining Items

None. The research note `research/source-versus-leeway-incompatibilism-2026-07-09` L73 still carries the adapted quote string; research notes are not reviewed in this pass and the note is a working document, so it is left as is.

## Stability Notes

- Fences from 07-09 and 07-19 hold: physicalist / hard-incompatibilist / semicompatibilist resistance to the wide-source-libertarian bet is bedrock; the article concedes it does not show the sourcehood condition is met; Pereboom's reply is granted undischarged by design.
- From the 10-13 wing review and today's manipulation review, confirmed here: **Tenet 5 reaches only the parsimony strand** of Pereboom's case against agent causation. L66 and L82 are now the two places this article describes his case; both scope the luck objection to event-causal sourcehood and leave the wild-coincidences strand open. Do not re-widen either, and do not re-flag "Tenet 5 does not answer the coincidences strand" as a defect.
- Pereboom quote at L51 is verbatim to 2001 p. 3 as of this pass (search-within-volume, control run). A future review need not re-grep it unless the string changes.
- Frankfurt 1969 is in References as of this pass; "In 1969 Harry Frankfurt" is no longer an orphan.
- Three deep reviews now; the file has converged. A cosmetic cross-link bump elsewhere should not re-trigger a pass unless the body or References block changes.
