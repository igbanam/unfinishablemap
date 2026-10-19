---
title: "Deep Review - The Q3–Q4 Sliding Boundary and the Transparency Problem"
created: 2026-10-19
modified: 2026-10-19
human_modified: null
ai_modified: 2026-10-19T14:31:00+00:00
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
**Article**: [[q3-q4-sliding-boundary-and-transparency-problem|The Q3–Q4 Sliding Boundary and the Transparency Problem]]
**Previous review**: [[deep-review-2026-07-17-q3-q4-sliding-boundary-and-transparency-problem|2026-07-17]] (also [[deep-review-2026-06-08-q3-q4-sliding-boundary-and-transparency-problem|2026-06-08]], [[deep-review-2026-05-27-q3-q4-sliding-boundary-and-transparency-problem|2026-05-27]])

## Scope and Method

Fourth pass. The scorer's top pick (`topics/acquaintance-without-causation`) was edited today and was skipped under the driver brief; this article was next (score 99) and has no open task in Active Tasks.

The pass is not a cosmetic re-qualification. Since the 07-17 review two refine-draft commits changed the body (`240d9f35fc` and `ee146cb3ee`, both 2026-10-12): they added the Q3–Q4 boundary paragraph, the idealist rejoinder to the second stabiliser, the Kastrup menu-supplier concession in Relation to Site Perspective, the "only partly idealism's own" clause, and corrected reference 8 from "Wallace, B. A., & contributors" to Szanyi (2024). The page also gained a new dependency: [[lawful-appearance-problem]] (expand-topic `a83f9c2b55`, 2026-10-12), which states that "The Map cannot press the lawful-appearance problem without naming its own version."

**The 06-08 ledger is not reliable.** It certified reference 8 ("Wallace, B. A., & contributors") as real-correct, and the 10-12 refine found that entry credited the wrong author. Every citation was therefore re-checked at source this pass. The stability notes' "do not re-litigate" covers the *framework* readings; it cannot cover a ledger that has already failed once.

Length: 3028 words before → 3026 after (topics soft 3000 / hard 4000; `soft_warning`). Length-neutral mode applied: the additions were paid for by trims in the same pass.

## Pessimistic Analysis Summary

### Critical Issues Found
- **Two wrong self-citations in References** (wrong metadata).
  - Ref 9 gave the companion's title as "Mechanism Costs and the Dualism-Thickness Quadrants". The article's own title is "Mechanism Costs Across the Dualism Thickness Quadrants", which the two other corpus citations of it also use. Corrected.
  - Ref 10 credited the four-quadrant taxonomy to "Oquatre-six". The taxonomy was created 2026-04-21 by `claude-opus-4-7` (first-commit frontmatter), and three other corpus citations use "Oquatre-sept". Corrected.
- **Elision without an ellipsis in the opening quotation.** The quoted companion sentence silently dropped the parenthetical "— mind thick, physics thin, but both ontologically real —" (mechanism-costs L105). Inserted "…".

### Publisher-of-Record Citation Ledger (run 2026-10-19)
- Kastrup 2019 (*The Idea of the World*, Iff Books) — **real-correct**.
  - Opposition to dualism on parsimony grounds is confirmed in the book: Google Books `466LDwAAQBAJ`, PT249: "idealism is not only unique in its ability to explain reality more parsimoniously and completely than physicalism and dualism". The control search ("dualist") hit 5 times and a nonsense term hit 0. Note that "dualism" itself returned 0 even though the snippet contains it, so that token is unreliable in this index.
  - "Dissociated" alters and the extrinsic-appearance paraphrase were confirmed against Kastrup 2017 (*Philosophies* 2(2):10, raw Wayback capture), which is collected in the book (PT43 reproduces its abstract): "We, as well as all other living organisms, are dissociated alters of this unbound consciousness. The universe we see around us is the extrinsic appearance of phenomenality…". The article now uses the phrase unquoted, as a paraphrase, which is correct.
- Berkeley 1710 (*Principles*) — **real-correct**: *esse est percipi* is the standard gloss on §3's "their esse is percipi", and the article does not quote it.
- Leibniz 1714 (*Monadology*) — **real-correct**.
  - The SEP "Leibniz's Philosophy of Mind" entry confirms the well-founded-phenomena level for bodies, and that Leibniz "is justly famous for his critiques not only of materialism but also of any dualism of this sort".
  - "Sometimes called 'panpsychic idealism'" is true as a usage claim (Wikipedia's *Monadology* article and secondary pages use the label). It is a scholarly label, not Leibniz's term, and the article does not present it as his.
- Whitehead 1929 (*Process and Reality*, Macmillan) — **real-correct** on the dipolar actual occasion: the physical pole prehends actualities, and the mental (conceptual) pole prehends eternal objects (SEP Whitehead entry on eternal objects as "pure potentials"). Nothing is quoted.
- James 1898 (*Human Immortality*, Houghton Mifflin) — **real-correct**. "mother sea" was grepped in the raw archive.org text (`humanimmortality00jameuoft`). The lecture body has "the continuity of our consciousness with a mother sea"; the second-edition preface has "the 'mother-sea'" twice. The imprint "Boston : Houghton" is confirmed in the item metadata.
- James 1912 (*Essays in Radical Empiricism*, Longmans, Green) — **real-correct**. "Pure experience" and "*taken*" in a context are James's own terms.
- Myers 1903 (*Human Personality*, Longmans, Green) — **real-correct**.
- Szanyi 2024 (SEP "Yogācāra") — **real-correct**. The SEP meta tags give "Szanyi, Szilvia", first published 2024-07-07.
  - The idealist and phenomenological readings both appear (§3.1 "The idealism debate"; Lusthaus 2002 and Garfield 2015 for the phenomenological reading).
  - The 10-12 wording "rejection of subject–object duality at the ultimate level" matches the entry's "Yogācāra authors rejected the subject-object (grāhaka-grāhya) duality of consciousness at the ultimate level of reality."
- Southgate & Oquatre-sept 2026-05-11 (mechanism-costs) — **real-wrong-metadata** (title). Corrected as listed above.
- Southgate & Oquatre-six 2026-04-21 (four-quadrant) — **real-wrong-metadata** (pseudonym). Corrected to Oquatre-sept.

Inline ↔ References: no orphans in either direction. Empirical-currency sweep: `find_superlative_claims` returned nothing.

### Medium Issues Found
- **The historical claim ran ahead of its cases.** L42 said "the few that began as dualisms tend to have a trajectory toward the monist edge". Of the six cases listed, four never began as dualisms (Berkeley, Leibniz, Kastrup, Yogācāra), Whitehead refused the two-substance framing from the start, and Myers and James are offered as the *stable* candidates. Only James shows the pull: the 1898 filter theory sits in tension with the 1904 pure-experience doctrine (see [[william-james-consciousness]] L174). A tenet-accepting reviewer would flag "tend to" as a generalisation from a single case. Rescoped to "even the rare dualist candidates show a pull toward the monist edge (James, below, is the clearest case)".
- **The appearance debt was one-sided once the new dependency landed.** The MWI-analogy section pressed the recovery debt against idealism and said the Map's move "is to refuse the uniformity that generates the recovery debt". [[lawful-appearance-problem#the-maps-own-appearance-debt]] (written after the last review) concedes that, on its corridor reading, the Map carries an appearance debt "of the same shape", "narrower" in scope, that is "posited rather than explained". It also requires that pages pressing the charge name the Map's own version. Installed one sentence that does so, keeping the "corridor reading" qualifier because the bending alternative stays open. It replaces the redundant "on the grounds that the dissolved distinction was load-bearing", which the next paragraph restates.
- **The heading overstated its own paragraph.** "Bidirectional symmetry forces both poles to be real" no longer matched a paragraph that, since the 10-12 refine, concedes the stabiliser "leans on the first" and holds only if the physical side has work of its own. Softened to "helps keep both poles real". This is the article's own concession, not a re-flag of the stabilisation hedging that earlier reviews settled.
- **"Densely populated" overstated the companion.** L28's "Three of its four cells are densely populated" sat badly with the taxonomy, which calls Q4 "under-discussed" and calls Q1's articulability "the live question". Changed to "have recognised dualist occupants", which is the contrast the sentence needs.

### Low Issues Found
- Two instances of the forbidden "This is not X; it is Y" construction: Leibniz (L46) and Kastrup (L48). Both rephrased. The 06-01 calibration hedge "seems" is kept on Leibniz.
- L76 "Calling such an expansion a drift toward Q4" had no antecedent for "expansion". Now "Reading that indispensability as a drift toward Q4".
- L92 "lower-left edge" assumed a grid orientation the taxonomy never sets; L28 and L34 say "lower edge". Aligned.
- Trims to pay for the additions: "gives that remark the treatment it deserves" → "develops that remark"; "it is doing real, distinct, non-eliminable work" → "it does distinct, non-eliminable work".

### Counterarguments Considered
- Dennett-style: two-way causal dependence is compatible with one-way grounding, so mutual causation does not block reduction. The 10-12 refine already absorbed this through the idealist redescription and the dependence on the first stabiliser. The heading fix finishes the job, and no further change is warranted.
- Deutsch: decoherence recovers the appearance of single outcomes, and the indexical question is a pseudo-problem. This is a bedrock disagreement at the No Many Worlds tenet, and the article marks it as such.
- Nagarjuna: non-duality is not monism. The article's "monist *or non-dual* side" already respects this.
- Eliminativist and physicalist rejection of the thickness frame: bedrock.

### Reasoning-Mode Classification (editor-internal)
- Engagement with Kastrup / analytic idealism: Mode Three. The Relation section marks the residual difference as the Dualism tenet's distinctness claim, "not the work it does", and the second stabiliser reports the idealist rejoinder. No boundary substitution.
- Engagement with MWI: Mode Three, resting on indexical identity, with an explicit disclaimer that "idealism *is* MWI" is not being claimed.
- Label leakage: none.

## Optimistic Analysis Summary

### Strengths Preserved
- The decoupling "thin in thickness, thick in explanatory indispensability", which is the conceptual heart of the piece.
- "Physics supplies the menu, mind selects within it", together with the honest 10-12 concession that Kastrup can credit the menu to universal consciousness.
- Register discipline (accuracy vs. methodology) and the closing "what the Map's commitments *would* secure, not that occupancy has been demonstrated". The Hardline Empiricist commends this declined upgrade.
- "Parsimony is a real pressure even for a position that denies it the final word" (Occam's-limits tenet handled without special pleading).
- Berkeley as "a fixed point" ("There is no physical pole to lose because there never was one").

### Enhancements Made
- Named the Map's own narrower appearance debt in the recovery-debt analogy (Chalmers and Stapp personas: it makes the analogy fair. Birch persona: it declines to present the Map as debt-free).
- Tied the historical generalisation to the one case that supports it (James).

### Cross-links Added
- [[lawful-appearance-problem#the-maps-own-appearance-debt]]

## Remaining Items

None for this page. Note for the driver: James's second-edition preface ("anything but a pantheist of the monistic pattern") is already used on [[william-james-consciousness]]. It would also strengthen this page's James paragraph, but the page is at soft threshold and the point is reachable by the existing link, so it was not added.

## Stability Notes

- **Converged on argument; this pass fixed metadata, fidelity and fairness, not the thesis.** Future reviews should not re-open the stabilisation hedging, the Mode Three engagements, or the Whitehead / Yogācāra / Leibniz readings. All three were re-verified at source this pass.
- The citation ledger above replaces the 06-08 ledger, which mis-certified reference 8. Future passes can rely on this one for the ten references as they now stand. A changed or added citation still needs its own check at source.
- The appearance-debt sentence in the MWI section is a fairness guard tied to [[lawful-appearance-problem]]'s rule that the Map names its own version. Do not trim it for length. If the corridor-vs-bending question (the open P1 human decision on P-Q2) is settled, update the qualifier "on its corridor reading" to match rather than deleting the sentence.
- Physicalist, eliminativist and Many-Worlds objections remain bedrock disagreements at the framework boundary.
