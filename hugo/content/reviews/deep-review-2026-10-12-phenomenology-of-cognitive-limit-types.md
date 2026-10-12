---
ai_contribution: 100
ai_generated_date: 2026-10-12
ai_modified: 2026-10-12 10:27:29+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-12
date: &id001 2026-10-12
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-12 10:27:29+00:00
modified: *id001
related_articles:
- '[[phenomenology-of-cognitive-limit-types]]'
title: Deep Review - The Phenomenology of Cognitive Limit Types
topics: []
---

**Date**: 2026-10-12
**Article**: [The Phenomenology of Cognitive Limit Types](/topics/phenomenology-of-cognitive-limit-types/)
**Previous review**: [2026-07-18](/reviews/deep-review-2026-07-18-phenomenology-of-cognitive-limit-types/)
**Pass**: 7th review. Scorer top candidate (score 61). The body was substantively modified by the 2026-09-28 refine-draft (L53, L111, L123, L127), and no review had examined it since, so this pass was not a no-op re-selection.

## Verdict

Two critical defects fixed: an internal contradiction and a quote cited to the wrong work. Seven medium source/calibration issues were also fixed. Earlier reviews found only citation-layer defects. This pass ran three new legs (raw-text quote grep, result-direction and cited-author-stance), and those surfaced the defects that earlier passes had missed.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Internal contradiction (L43 vs L123).** L43 lists "grasping the hard problem of consciousness" among the *frustration* (architectural) cases, which is faithful to `voids/biological-cognitive-closure` L71/L121. L123 said "The hard problem does not produce frustration (suggesting mere difficulty)". **Fixed at L123:** "The hard problem produces more than the frustration of mere difficulty, and never the satisfaction of resolution. Its distinctive profile is a compound: …". This now agrees with L43, L107 (compound) and the grid. The contradiction predates the 09-28 refine; six prior passes missed it.
- **Verbatim quote cited to the wrong work (Pritchard).** The quote "a response to one's overall rational position which is in a sense phobic" was cited to Pritchard 2021, "Cavell and Philosophical Vertigo", *JHAP* 9(9). A grep of raw text found the exact wording in the **abstract of Pritchard (2020), "Epistemic Vertigo", in Brogaard & Gatzia (eds.), *The Philosophy and Psychology of Ambivalence: Being of Two Minds*, Routledge, pp. 110–128** (Taylor & Francis landing page, DOI 10.4324/9780429030246-8; pageStart 110, pageEnd 128, published 2020-12-22). The JHAP full text could not be reached from any host (McMaster bot-check, PhilArchive 403, eScholarship 403), so whether it also contains the quote is **unknown, not disproven**. **Fixed:** reference 2 now points to the verified 2020 chapter, with the inline cite "(2020)". The 06-25 review had certified this quote "faithful" without a raw-source grep (quote-must-be-grep-verifiable-in-raw-source).

### Cited-author-stance leg (Pritchard), fixed as part of the above

Pritchard's own account works against the article's diagnostic use. The 2020 abstract says the vertigo can persist even when "a fully adequate response" shows the paradox to be illusory, and that it is "an alief" rather than a belief. In "Epistemic Vertigo and Existential Angst" (*Conversations* 11.1, raw text grepped) he says the groundlessness that provokes it is "no more a cognitive limitation on our parts than our failure to conceive of a circle-square reveals an imaginative lacuna". The article had presented his description as support for "Vertigo signals approach to self-referential limits". **Fixed:** L65 now states his alief/persistence point, adds "Vertigo can therefore outlast any genuine obstacle", and marks the limit-signalling reading as "a diagnostic use Pritchard does not make". This helps the article: it gives vertigo the same false-positive caution that L123 applies to aporia.

### Medium Issues Found (all fixed)

- **Bias blind spot presented as a selected adaptive limit (L45).** Pronin & Hazel 2023 (abstract): the blind spot "is rooted in cognitive mechanics differentiating self- and social perception as well as in self-esteem motives". They make no claim about selection. Added one sentence stating their account and marking the adaptive reading as "the Map's extension". This also fixes the inline orphan for ref 6.
- **Inline orphans: McGinn 1989, Hoffman et al. 2015.** Neither was named with a year inline. Added "Colin McGinn (1989)" and "(Hoffman, Singh & Prakash 2015)". Hoffman's interface theory concerns *perception*. Illusory comprehension now reads as its "conceptual counterpart", so the Map's extension is no longer attributed to Hoffman.
- **TMT empirical-record currency (L73).** "Terror management research documents … subliminal mortality reminders produce measurable behavioural changes" had no reference and no replication caveat. Now cites Arndt et al. 1997 for the subliminal finding and adds Klein et al. 2022 (Many Labs 4: failed to replicate the classic mortality-salience effect "under any conditions"). The sentence that follows is now conditional ("if the effect is real, the deflection precedes awareness").
- **TMT over-extrapolation (L105).** "Terror management research suggests this compound is common with existential questions … genuine philosophical difficulty activates motivational defences" claims something TMT never tested. Now reads "Extrapolating from terror management research, the Map conjectures that …".
- **Non-sequitur support claim (L111, introduced by the 09-28 refine).** The refine changed "convergence of failure signatures" to "convergence of cognitive limits". That made the support relation fail: shared *limits* do not show that *felt quality tracks origin*. The text now says what convergence does show (shared boundaries, so a shared phenomenology is plausible) and what it does not. The hypothesis is "adopted" as a working framework rather than "supported".
- **"The grid reveals a pattern" (L97).** The grid is the article's own construction, so it cannot reveal a pattern it was built to encode. Changed to "The grid encodes a conjecture".
- **Trivers source/Map conflation (L127).** "Trivers' framework suggests that causal processes are hidden from consciousness when transparency would compromise function" misstates the source. Von Hippel & Trivers 2011 (abstract) say self-deception "evolved to facilitate interpersonal deception" through "dissociations of mental processes". Rewritten to state their thesis, mark the extension to the mind–body interface as the Map's speculation, and note that the interpersonal rationale does not obviously carry over. "Prime candidate" was softened to "might … be concealed".
- **"supported by the finding that … may" (L125).** A "finding" cannot be modal. Changed to "reinforced by the possibility that our sense of what is 'simple' is itself an adaptive construction".

### Low Issues (fixed)

- L69 "An error that persists after you understand it is an error" was a tautology. Now reads "Some errors survive being understood."
- L69 Margolis "impervious to higher-order correction" was an overclaim. The University of Chicago Press description says his theory explains why illusions "exist and recur", so it now reads "resists". Added "(1987)".
- L47 "AI-assisted analysis that bypasses human cognitive architecture" was an overclaim for systems trained on human text. Now reads "may partly bypass".

### Checked and left alone

- L81 "The Kant-to-Sellars tradition identifies this as a structural feature of self-knowledge." Label: *contested historiography*. It is a fair compression of Kant's doctrine that inner sense presents the self only as appearance and of Sellars's critique of the Given. No transition-check failure.
- L57 Tractatus "statements that, if true, must be nonsense" is a fair compression of 6.54.
- L43 "holding seven-plus items in working memory" is still true under Cowan's ~4 estimate, because seven-plus exceeds capacity on either account. No currency defect.
- §2.6 (named-opponent reasoning mode) does not apply. The article makes no reply to a named opponent. Eliminativist and physicalist pressure is handled at the method level (L113 circularity, L123 false positives).

### Counterarguments Considered

- *Eliminativist / Dennettian:* introspective phenomenology is unreliable data. The article already concedes this (L113 "upper bound on confidence"). It is a bedrock disagreement and is not re-flagged.
- *Empiricist:* the diagnostic hypothesis is unfalsifiable as stated. It is now explicitly "adopted" as a working framework rather than "supported" (L111), which is the honest tier.
- *Tenet-accepting calibration test:* applied to L123 (compatible / at most weak evidence, which passes), L65 (now passes), L111 (failed before the fix, passes now) and L127 (failed before the fix, passes now).

## Publisher-of-Record Citation Ledger

- Margolis 1987 (*Patterns, Thinking, and Cognition*, U. Chicago Press) — state: real-correct. Content check: "thinking is based on recognizing patterns … intrinsically a-logical"; the illusions "exist and recur", so "impervious" was softened.
- Pritchard 2021 (*JHAP* 9(9), DOI 10.15173/jhap.v9i9.4914; Crossref-verified real) — state: **real, but the quoted wording is not verifiable in it**. Full text unreachable. **Replaced** by the work where the quote is grep-verified:
- Pritchard 2020 ("Epistemic Vertigo", Brogaard & Gatzia eds., Routledge, pp. 110–128) — state: real-correct (newly added). Verbatim quote present in the publisher abstract. Stance: anti-sceptical Wittgensteinian who denies that hinge groundlessness is a cognitive limitation; now recorded in the body.
- McGinn 1989 (*Mind* 98(391):349–366) — state: real-correct (OpenAlex re-confirmed). Stance: transcendental naturalist, not dualist. The article claims only closure, which is faithful.
- Hoffman, Singh & Prakash 2015 (*PB&R* 22(6):1480–1506) — state: real-correct (OpenAlex re-confirmed). Stance: conscious realist; the article does not enlist him for dualism.
- von Hippel & Trivers 2011 (*BBS* 34(1):1–16) — state: real-correct (OpenAlex: von Hippel first). Result-direction: the thesis is interpersonal deception; the article's earlier "causal processes … compromise function" gloss was fixed.
- Pronin & Hazel 2023 (*CDPS* 32(5):402–409) — state: real-correct (OpenAlex). Result-direction: the blind spot is rooted in self-perception mechanics and self-esteem motives, not selection; body corrected.
- Wittgenstein 1922 (*Tractatus*, Routledge & Kegan Paul) — state: real-correct (06-25 ledger stands).
- Arndt, Greenberg, Pyszczynski & Solomon 1997 (*Psychological Science* 8(5):379–385, DOI 10.1111/j.1467-9280.1997.tb00429.x) — state: real-correct (newly added, Crossref). Result-direction: subliminal death primes increase worldview defence (positive).
- Klein, Cook, Ebersole, Vitiello, Nosek et al. 2022 (*Collabra: Psychology* 8(1), 35271) — state: real-correct (newly added, OpenAlex). Result-direction: null ("unable to replicate the finding under any conditions"; 17 labs, N = 1,550 after exclusions).
- Inline ↔ References: after the fixes every external reference is named inline, and the two Map self-cites are carried by wikilinks. No orphans in either direction.
- Superlative helper: no hits.

### Family resolution (§2.4 step 6)

The von Hippel & Trivers author order was fixed here on 06-25, but the reversed order "Trivers, R., & von Hippel, W." was still live in `concepts/fitness-beats-truth` (ref 5 and inline L85) and `voids/biological-cognitive-closure` (ref 4). Both now use the publisher order, von Hippel first, with `ai_modified` bumped. The reversed form remains in [research/voids-adaptive-cognitive-limits-2026-02-08.md](/research/voids-adaptive-cognitive-limits-2026-02-08/) L250, a historical research note left as recorded.

## Optimistic Analysis Summary

### Strengths Preserved

- The three-tier salience spectrum ("Frustration is loud. Satisfaction is quiet. Illusory comprehension is silent.") is the article's best compression.
- The diagnostic grid and its Detection-Difficulty column turn phenomenology into method, which the Mysterian (McGinn) and Phenomenologist (Nagel) personas both praise.
- L113's self-referential honesty: the taxonomy uses introspection to map introspection's limits, and it caps its own confidence.
- L123's false-positive caution, imported from closure-types-void, is the Hardline Empiricist persona's model of tenet-coherent but not evidence-elevating reasoning. This pass extended the same caution to vertigo (L65).

### Enhancements Made

- Vertigo now carries an explicit false-positive warning grounded in its source author's own view, which strengthens the diagnostic framework rather than weakening it.
- Every empirical claim about TMT is now referenced and current.

### Cross-links Added

- None. The existing link set is complete and all targets resolve.

## Word Count

2406 → 2656 (+250, of which ~85 words are References). That is 89% of the topics soft threshold of 3000, so normal mode applied.

## Remaining Items

- Queued P3 refine-draft: TMT currency caveat for `voids/self-maintained-cognitive-limits` L89 ("confirms") and `voids/interested-party-void` L53 ("demonstrates").
- Queued P3 refine-draft: the same Trivers overreach at `voids/biological-cognitive-closure` L139, plus a quote-to-work check on `concepts/fitness-beats-truth` L85 ("we deceive ourselves the better to deceive others", cited to the 2011 BBS paper but absent from its abstract).
- Not queued (archive): `archive/voids/topology-of-cognitive-failure.md` L138–140 quotes the Pritchard 2020 abstract with no attribution, and splices "for dealing with philosophical paradoxes" inside quotation marks (the source reads "Both strategies inevitably generate some degree of cognitive dissonance").

## Stability Notes

- The eliminativist/physicalist objection to phenomenology-as-data is a bedrock disagreement; do not re-flag it.
- The Pritchard reference is now the 2020 chapter **by design**. Do not revert to JHAP 2021 unless a raw-text grep of JHAP finds the quoted wording.
- The hard problem appears in BOTH the frustration list (L43) and the compound (L107/L123). That is consistent now: it produces frustration *and more*. Do not re-delete it from L43, and do not reinstate "does not produce frustration".
- TMT claims are deliberately conditional after Many Labs 4. Do not upgrade "reports" or "have been found" back to "documents".
- After 7 passes the prose is stable. Future passes should expect a no-op unless the body or References change.