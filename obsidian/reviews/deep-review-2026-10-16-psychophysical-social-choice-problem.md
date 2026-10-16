---
title: "Deep Review - The Psychophysical Social-Choice Problem (2026-10-16)"
created: 2026-10-16
modified: 2026-10-16
human_modified: null
ai_modified: 2026-10-16T00:10:38+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-16
last_curated: null
---

**Date**: 2026-10-16
**Article**: [[psychophysical-social-choice-problem|The Psychophysical Social-Choice Problem]]
**Previous review**: Never. The article was written 2026-10-13 by expand-topic from [[research/psychophysical-social-choice-problem-2026-09-15]]. Two prior reports touch it: tenet-check-2026-10-14 (listed it "clean") and pessimistic-2026-10-14-quantum-interface-p-q2-reading Issue 4 (L79, "Which reading the register holds is open"). The P1 HUMAN DECISION task on P-Q2's quantifier says not to propagate the 17:25 reading to L79 until the operator decides, so L79 was left as it is.
**Word count**: 2,937 → 2,937 (net 0; `analyze_length`). Concepts thresholds: soft 2,500, hard 3,500, and the gate is `>=`. The article sits in the soft band, so the review worked in length-neutral mode. The two additions (+8 at L73, +1 at L113) are paid for by trims at L37 (−4) and L61 (−9) and by the shorter References entry #1 (−3). The +3 at L57 is covered by the same trims.

**Mode**: First-pass review of a fresh, citation-heavy concept article. All 12 external References entries were checked at the publisher of record: Crossref for every DOI, RePEc for the Gibbard and Sen 1977 page ranges, and the Cowles Foundation catalogue and CiNii for Arrow. Every quotation was grepped against a raw source: the Econometric Society abstract page for Gibbard, Bostrom's own PDF, the arXiv PDF of Chalmers & McQueen, and the live SEP HTML for List 2022. Internal quotations were grepped in the live positions files (P-SC2, P-AC3, P-VS1, P-VS4, P-MS1/2) and the sibling concept files.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Internal contradiction on lexical priority (L61 vs L87).** L61 said lexical priority is "the only option on which a subject's moral standing and causal standing would coincide". L87 then exempted lexical priority from the claim that "causal leverage varies with the census, with anatomy, with attentional architecture or with felt intensity, while moral status stays the same for everyone above the threshold P-MS2 sets". The article's own definitions refute both. The L85 anchor is `moral-and-causal-standing`, and there "moral standing" means P-MS1/P-MS2 status, which is a threshold. Under lexical priority, two subjects of equal status get unequal leverage: whoever is in severe suffering dominates. Leverage therefore varies with felt intensity, and what it tracks is *stakes*, the third quantity L87 itself distinguishes. **Fix**: L61 now reads "It lets moral urgency fix causal priority outright, and it builds a rights structure into physics" (−9). L87 now reads "On every rule above, lexical priority included, causal leverage varies…" (±0). The "Status, stakes and leverage are three different things" sentence now holds without exception.
- **Arrow (1963) References entry #1 had the wrong publisher (real-wrong-metadata).** It read "Yale University Press. (1st ed. Wiley, 1951.)". The Cowles Foundation's own catalogue page for CFM 12.2 (2nd ed.) lists "John Wiley & Sons, Publication Date January 1963", and CiNii holds the 2nd edition as "Wiley, c1963". The entry was corrected to "Wiley. (1st ed. 1951.)". Family check: no other live page cites Arrow 1951/1963. The research note carries the same error (see Remaining Items).

### Medium Issues Found

- **L37 "pricing rules of that shape, and none of them is neutral".** There were two problems. (a) "Rules of that shape" refers back to stochastic decision schemes, which have been studied since about 1969–1977, not for "more than seventy years". The seventy years are true of aggregation rules in general (Arrow 1951). (b) "Neutral" is a technical term in social choice: May's theorem makes majority rule *neutral*. A specialist reader would take "none of them is neutral" as false. **Fix**: "pricing aggregation rules, and none comes free" (−4). The next three sentences still list the prices.
- **L73 priced the locality confinement on only one of its two bets.** The QRNG exemption runs "through baseline objective collapse". The sibling [[multi-agent-born-preservation-problem]] L66 calls that baseline "itself a contested empirical bet (GRW/CSL parameter space is being narrowed by experiment; gravitational collapse is unconfirmed)". The article cited only the sibling's L62 neural-physics bet. A reader who accepts the tenets would still flag that omission as understating the conditionality, so it is a calibration fix. **Fix**: "The confinement rests on two bets the multi-agent article names: an empirical bet about neural physics, and baseline objective collapse, which is itself contested." (+8)
- **L113 "rules out a group subject"** was unscoped, while L95 carefully says that "the denial targets a *phenomenal* group subject only" and that List and Pettit's functional group agent "needs nothing the Map denies". **Fix**: "rules out a phenomenal group subject" (+1).

### Low Issues Found

- **L57 "This is the "utilitarian natural law" reading".** The quotation marks presented an internal coinage, from outer-review-2026-09-14-chatgpt-5-6-sol-pro §4.1 via the research note, as if it were an external term of art with a source. **Fix**: "This rule would make utilitarianism a law of nature" (+3). The next pronoun, "its precondition", still refers to the rule (or to utilitarianism), and both readings are correct.
- **L65 "joint-level [[ensemble-level-epiphenomenalism|ensemble-level epiphenomenalism]]"**: the doubled "-level" read badly. Reordered to "ensemble-level epiphenomenalism at the joint level" (±0).

### Citation ledger (§2.4)

- Arrow 1963 (*Social Choice and Individual Values*, 2nd ed.): real-wrong-metadata. The publisher was Yale UP; corrected to Wiley (Cowles CFM 12.2 page; CiNii BA02983626). The 1st edition, 1951, was also Wiley.
- Bostrom 2006 (*Minds and Machines* 16(2), 185–200, doi 10.1007/s11023-006-9036-0): real-correct. The Duplication quotation is verbatim in the author's PDF (nickbostrom.com/papers/experience.pdf). Stance: computationalist, and not presented as endorsing the Map.
- Chalmers & McQueen 2022 (in Gao (Ed.), *Consciousness and Quantum Mechanics*, OUP, pp. 11–63, doi 10.1093/oso/9780197501665.003.0002): real-correct per Crossref. "with probabilities given by the Born rule" is verbatim in arXiv 2105.02314 (three occurrences). The article treats them as a collapse-*trigger* rival, which matches their super-resistance model. They explore the model rather than endorse the Map.
- Gibbard 1977 (*Econometrica* 45(3), 665–681, doi 10.2307/1911681): real-correct. The pages are confirmed by RePEc and the Econometric Society page. Both quotations are verbatim in the abstract on the Econometric Society page, and the "only one individual can affect the outcome" gloss matches it. The abstract's further clause, "If it guarantees Pareto optimal outcomes, it is a probability mixture of dictatorial schemes", is consistent with the random-unilateral menu entry. The article deliberately does not invoke it.
- Harsanyi 1955 (*JPE* 63(4), 309–321, doi 10.1086/257678): real-correct. It is paraphrased only (aggregation theorem, with weights requiring interpersonal comparison), which is the standard reading.
- List 2022 (SEP "Social Choice Theory"): real-correct. The live page header reads "First published Wed Dec 18, 2013; substantive revision Fri Oct 14, 2022". "Arrow's impossibility can therefore be traced to a lack of interpersonal comparability (for detailed analyses, see Sen 1977 …)" is verbatim, and it carries the source's "In a welfare-aggregation context" scope, which the article's context preserves. The Sen 1970a theorem (universal domain, acyclicity, weak Pareto, minimal liberalism), the at-least-two-individuals definition of minimal liberalism, and the "not 'meddlesome'" domain restriction are all verbatim in the raw HTML.
- List & Pettit 2002 (*Economics and Philosophy* 18(1), 89–110): real-correct. The paraphrase matches the OpenAlex abstract ("interconnected questions"; "a general impossibility theorem").
- List & Pettit 2011 (*Group Agency*, OUP, doi 10.1093/acprof:oso/9780199591565.001.0001): real-correct. Stance: functionalist group agency, explicitly marked at L95 as needing nothing the Map denies.
- Okasha 2011 (*Mind* 120(477), 83–115, doi 10.1093/mind/fzr010): real-correct. The OpenAlex abstract reads "the problem of theory choice as posed by Kuhn is formally identical to a standard social choice problem", which supports the "criteria in place of voters" paraphrase.
- Roelofs & Sebo 2024 (*Philosophical Studies* 181(6–7), 1487–1506, doi 10.1007/s11098-024-02167-x): real-correct. "Count once or twice" matches the abstract's "count the value of those states twice … once".
- Sen 1970 (*JPE* 78(1), 152–157, doi 10.1086/259614): real-correct.
- Sen 1977 (*Econometrica* 45(7), 1539–1572, doi 10.2307/1913949): real-correct. RePEc confirms 1539–72.
- Internal #13–14 (Southgate et al.): the author strings match the `ai_system` fields of `topics/multi-agent-born-preservation-problem` (fable-5) and `concepts/selection-only-channel` (4 models), and the dates match their `created` fields.
- Inline ↔ References: no orphan in either direction.
- Superlative helper: no candidates.
- Absence claim (L39, "no external literature treats a psychophysical law as a social-choice function"): one control search (2026-10-16) returned only the Map's own two pages plus general consciousness-collapse material. The claim stands at search level, and it is phrased as the Map's own synthesis.

### Internal-quotation and register checks

The following were all verified in live files: P-SC2's "where two subjects hold contrary intentions bearing on one physical event, there is no composition rule" (verbatim; the article's "accumulate, dilute or renormalise" omits P-SC2's "cancel", a harmless paraphrase); P-SC1's "subject-sensitive balancing law it has not written"; P-AC3 (copies morally additive, conditional on closed individualism); P-VS1 (credence low; felt anticipation at choice; the micro-valence shift condition); P-VS4 (six dimensions, no common hedonic currency); P-MS1 (who can be wronged) and P-MS2 (threshold); multi-mind-collapse L37 "each consciousness interfaces only with its own brain" (verbatim); subject-fusion L71 (two subjects with coupled channels, neutral on shared tokens) and L75 (whole number at every moment); moral-census-opacity (determinate, unreadable); miswanting L31/L67 (no study measured felt anticipation at choice); measurement-standards L84 (no shared phenomenal reference point); tenets L91 (Tenet 3 commits to outcome-selection); and the `^mechanism-debt` block anchor in positions/quantum-interface L79.

### Born-favours-fixed-weights derivation (checked)

E[w·P₁(O|C₁) + (1−w)·P₂(O|C₂)] = w·Born + (1−w)·Born, for any joint distribution of (C₁, C₂). Each term depends only on its own marginal, so the result holds whatever the correlation. Once w depends on (C₁, C₂), the factorisation fails. A convex mixture can never exceed the larger single-subject deviation, so "accumulation" is out of reach, as the article says. The per-context/pooled distinction at L79 is also right: on the pooled reading, context-varying weights break the cancellation of per-context deviations. The L79 attribution sentence is fenced (P1 human decision) and was not touched.

### Reasoning-mode classification (editor-internal)

- Chalmers & McQueen (collapse-trigger rival, L93): boundary-marking. The price is giving up outcome-selection, which Tenet 3 (tenets L91) commits to. This is stated honestly as a cost, not as a refutation.
- List & Pettit (group agent, L95): mixed. The phenomenal group subject is set aside on the Map's non-compositionality commitment, which is boundary-marking. The functional group agent is conceded as compatible, and is excluded as selector only by the Map's own account of selection. The article now scopes the tenet summary (L113) to match.
- Value-blind reading (L91): boundary-marking at P-VS1's low credence ("the Map leans the other way").
- No label leakage. No "This is not X. It is Y." construct. No "load-bearing".

### Counterarguments Considered

- *Subjects could cultivate stronger feelings to gain leverage under intensity weighting.* This is genuine, but it is not Gibbard's misrepresentation sense. The article's "His motive was manipulation, which lapses for a law that reads phenomenal states rather than reports" is accurate as stated. Not added (length-neutral).
- *Equal weight, not lexical priority, is the rule on which per-subject leverage mirrors equal status at a single event.* Partly true: leverage is equal among the subjects paired to one event but varies with n across events, so L87's "varies with the census" stands. Not added.

## Optimistic Analysis Summary

### Strengths Preserved

- The structural identification of a multi-subject selection law with a Gibbard *decision scheme*, and the observation that the Born-preservation budget has no analogue in ordinary social choice.
- The Map's own result (§born-favours-fixed-weights): correct, modestly stated ("favours"), and conditional on the reading of Born preservation in force. The Hardline Empiricist praises the refusal to pick a reading.
- The three front-loaded calibrations (Map-internal synthesis; normative only on the low-credence value-sensitive reading; the mechanism debt). This is the Birch-style "tenet-coherent, not evidence-elevating" pattern done well.
- The disputed-implications split ("two follow from the definition alone … four follow only on the Map's reading").
- Okasha's criteria-as-voters move, which relocates the Arrovian problem inside a single subject if the scalar currency fails. The Mysterian and the Property Dualist both single it out.
- The sign-problem line in the Minimal Quantum Interaction paragraph ("with two subjects, the direction is contested").

### Enhancements Made

- The status/stakes/leverage triad is now consistent across L61 and L87.
- The locality confinement is priced on both of its bets.
- The tenet paragraph's group-subject denial is scoped to match the body.

### Cross-links Added

- None (length-neutral pass; the existing link set is adequate). Expansion opportunities noted but not taken: [[voids/boundary-and-projection]] as the external name of the pairing gap at the Jurisdiction entry, and Nozick's utility monster as the standard objection to intensity weighting. The research note marks the latter "cite from the book only if a page is checked".

## Remaining Items

- **Research note, same Arrow error**: `obsidian/research/psychophysical-social-choice-problem-2026-09-15.md` L51 ("Yale University Press 1963, Cowles Foundation Monograph 12") and L228 ("(2nd ed.). Yale University Press (Cowles Foundation Monograph 12)"). The 2nd edition is Wiley (Cowles CFM 12.2 page). Not edited here; it is a research-note correction for a later pass.
- **L79** ("Which reading the register holds is open, and this article does not settle it"): held pending the P1 HUMAN DECISION on P-Q2's quantifier (todo, "do not propagate the 17:25 reading to … L79").
- The P3 positions-evolve task registering this article's bearings on P-SC2/P-MS1/P-VS4 remains open and is unaffected.

## Stability Notes

- Physicalists, eliminativists and Many-Worlds defenders will reject the premise that a psychophysical law exists to be composed. That is bedrock disagreement, so do not re-flag it.
- The value-blind reading treating composition as "purely technical" is a live rival the article already states at P-VS1's credence. Do not upgrade it to a defect.
- The "none comes free" lead and the lexical-priority/moral-urgency wording are deliberate fixes. A future pass should not restore "neutral" (a technical term in social choice) or the "moral standing and causal standing would coincide" claim (contradicted by the article's own status/stakes/leverage distinction).
- Arrow 1963 = Wiley (Cowles CFM 12.2). Do not revert to Yale UP.
