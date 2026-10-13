---
ai_contribution: 100
ai_generated_date: 2026-10-13
ai_modified: 2026-10-13 03:17:28+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-13
date: &id001 2026-10-13
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-13 03:17:28+00:00
modified: *id001
related_articles:
- '[[improper-vs-proper-mixtures]]'
title: Deep Review - Improper vs. Proper Mixtures
topics: []
---

**Date**: 2026-10-13
**Article**: [Improper vs. Proper Mixtures](/concepts/improper-vs-proper-mixtures/)
**Previous review**: [2026-09-03](/reviews/deep-review-2026-09-03-improper-vs-proper-mixtures/)

## Scope

This is the second deep review. The selector put `concepts/improper-vs-proper-mixtures` at rank 17 (score 61.5, 40 days unreviewed). Ranks 1–13 and 16 were on the driver's avoid list or had changed in the last 40 hours. Ranks 14–15 (arguments/epiphenomenalism-argument, concepts/default-mode-network) were eligible but had only small diffs since their last reviews (+5/−4 and +19/−13). They were passed over because the driver prefers real unreviewed change. This was not a cosmetic re-qualification. Seven commits since the 2026-09-03 review changed +45/−32 lines. They added:

- the Liu–Scarani–Bai retrodiction paragraph;
- the Chen density-matrix-realism premise;
- the Bohmian fourth defeater route;
- the Donadi Gran Sasso result;
- the active-inference "fifth defeater";
- the Local Friendliness clause in Relation to Site Perspective;
- a Schlosshauer 2004 verdict quote;
- the 2026-09-17 Tenet 2 repair at L58/L96.

None of this new prose had been deep-reviewed. All of it was audited this pass.

**Length**: analyze_length total 3287 → 3296 (+9). Concepts soft 2500, hard 3500, gate `>=`. Prose (body before Further Reading) went 2751 → 2743 (−8). References grew by about +17, all of it publisher-of-record metadata, for a net total of +9. The article stays in length-neutral mode, 203 words under hard.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Internal contradiction / Tenet 2 misstatement (L58).** The text read: Bell's "preferred exits were Bohmian mechanics and consciousness-free objective collapse, both of which the Map declines."
   - The Map does not decline consciousness-free objective collapse. tenets.md L125 makes "physical mechanisms (gravitational collapse, spontaneous localization…)" the baseline collapse throughout the universe. `post-decoherence-selection` L96 says "consciousness initiates no collapse." This page's own L96 says confirming objective collapse "would fix the baseline the Map's prebiotic resolution already assumes."
   - The 2026-09-17 refine-draft (`a9bb5bef1d`) only inserted "consciousness-free," which left the contradiction in place.
   - Fixed: "his preferred exits were Bohmian mechanics, which the Map declines, and objective collapse, which it adopts only as a baseline, not the whole story." L99 ("one of the two exits Bell preferred") still agrees.
2. **Dropped qualifier: Local Friendliness (L107).** The text read: "requiring the selected outcome to be absolute commits the framework to a departure from universal unitary evolution."
   - The source section it links (`post-decoherence-selection#absolute-outcomes-and-the-local-friendliness-theorem`) says "Holding absoluteness **while keeping locality and no-superdeterminism**…". Bong et al. 2020 constrain the triple, not absoluteness alone.
   - Without the qualifier, the sentence also contradicted this page's own L99. That Bohmian route has determinate outcomes with no departure from unitary evolution, because it pays in locality.
   - Fixed: "while keeping locality and no-superdeterminism" restored (+5).
3. **Dropped qualifier: Schlosshauer 2004 quote (L42).** The quote ended "…with no outcome having been singled out." The raw LaTeX (rmp_arxiv.tex) continues "**according to the {e-e} link**."
   - Schlosshauer defines the e-e link as "the interpretive rule of orthodox quantum mechanics that tells us when we can speak of outcomes." He also says it "is by no means forced upon us by the structure of quantum mechanics."
   - The truncation turned an orthodox-rule-relative claim into an interpretation-neutral fact about the formalism. That cut against L99 (Bohm) and L84 (state realism as a tacit premise).
   - Fixed: the verbatim span is unchanged, and the qualifier now sits outside the quotes: "…singled out" by the orthodox eigenvalue–eigenstate link. "after decoherence" was dropped because the preceding clause already says it (net +3).
4. **References numbering defect.** Two entries were numbered "17." (Schlosshauer 2019 and Tomaz 2025), which shifted every later entry. Renumbered 18–23.

### Publisher-of-Record Citation Ledger (§2.4)

Every quoted span was re-grepped this pass against a raw artefact. Sources: arXiv e-print LaTeX downloaded this run, or pdftotext of the publisher/archive PDF. No WebFetch-summariser verdict was used for any quote. Metadata was checked through the Crossref REST API and the arXiv API.

- **Liu, Scarani & Bai 2026** (PRL 136(6), 060203; doi:10.1103/xx43-p1py; Crossref published 2026-02-12).
  - State: real-correct. All three quoted spans are verbatim in the arXiv:2502.10030 abstract (main.tex).
  - Result-direction leg: the paper reports a retrodiction difference, which matches the article's direction.
  - Framing leg: the paper itself cites Kirkpatrick 2001 and Castellani 2023 as the indistinguishability claims it qualifies ("This indistinguishability has led some to view the distinction as purely interpretative … with no operational consequences. However, things become subtle when considering retrodiction"). The article's "bears on the shared operational-indistinguishability premise" is therefore the authors' own framing. "Lends the Map's reading no support" is correctly calibrated: the paper calls the effect "a purely quantum feature of Bayesian agency."
- **Chen 2021** (BJPS 72(4), 1155–1183; doi:10.1093/bjps/axy068). State: real-correct. "objective and impure" and "objective and pure" are verbatim in the arXiv:1712.01666 abstract. Stance leg: Chen proposes density-matrix realism as a quantum-ontology thesis with no dualist commitment, and the article presents him as a challenger, not an ally.
- **Donadi et al. 2020** (Nature Physics 17(1), 74–78; online 2020-09-07, print 2021-01). State: real-correct. "rules out the natural parameter-free version of the Diósi–Penrose model" matches the abstract (arXiv:2111.13490). Currency: not a superlative, and the result still stands. `topics/penrose-gravity-induced-collapse-empirical-prospects` dates the same paper 2021 (print). That is a year-convention split, not an error, because this page's entry states both dates.
- **Schlosshauer 2004** (RMP 76(4), 1267–1305).
  - State: real-correct (metadata).
  - Quote-fidelity: "ignorance-interpretable, or proper ensemble" is verbatim.
  - The newly added verdict "within the framework of the orthodox interpretation, decoherence cannot explain this crucial step…" is verbatim (rmp_arxiv.tex).
  - The "improper mixture, with no outcome having been singled out" quote had a dropped qualifier, now fixed (Critical 3).
- **Schlosshauer 2019** (Phys. Rep. 831, 1–57). State: real-correct. Both spans are verbatim, including the QBism footnote.
- **Castellani** — state: real-wrong-metadata (was "(2022) … arXiv:2201.04143; philsci-archive 20113"). Corrected to the publisher of record: *International Journal of Quantum Information* 21(4), 2350019 (2023), doi:10.1142/S0219749923500193 (Crossref: online 2023-04-14). The inline "Castellani (2022)" became "(2023)". Both quotes are verbatim in the arXiv LaTeX (properimproper.tex), and the first is also verbatim in the published abstract on Crossref. The lead to this was Liu et al.'s own bibitem `castellani2023all`.
- **d'Espagnat 2001, "A note on measurement"** — state: real-wrong-metadata (arXiv only). Publisher of record added: *Physics Letters A* 282(3), 133–137, doi:10.1016/S0375-9601(01)00105-0 (Crossref; the arXiv API lists the DOI). "proper mixtures with the requested properties do not exist" is verbatim (arXiv LaTeX).
- **d'Espagnat 2001, "Reply to K A Kirkpatrick"** (quant-ph/0111081; no journal version found). State: real-correct. "not mathematical but logico-semantical" and "cannot be given an ignorance interpretation. It is therefore this claim that my critics should aim at disproving" are both verbatim. The same sentence scopes the claim to "the partial traces of a composite system pure state statistical operator". That scoping is now used at L86 (see Enhancements).
- **Tomaz, Mattos & Barbatti 2025** — state: real-wrong-metadata (arXiv only). Publisher of record added: *Philosophical Magazine*, 1–38, doi:10.1080/14786435.2025.2601922 (Crossref online 2025-12-26; arXiv v3 journal_ref "Philosophical Magazine C (2025)"). Title case now follows the publisher. The two-sentence quote is verbatim in arXiv **v3** (post-acceptance), so it survived revision.
- **Bell 1990** (Physics World 3(8), 33–40). State: real-correct. All three quoted spans are verbatim (pdftotext of the full text).
  - Coiner leg: "Bell coined it in 'Against measurement'" is confirmed by the paper itself: "it is convenient to have an abbreviation for the last phrase: FOR ALL PRACTICAL PURPOSES = FAPP."
- **Grangier 2026** (arXiv:2601.20488, v1; no journal_ref). State: real-correct. "greatly reinforced" and "non-FAPP ontology" are verbatim. The FAPP paraphrase matches the source sentence: "the view that quantum mechanics works so well in practice that conceptual difficulties can be set aside."
- **Kirkpatrick 2001** (quant-ph/0109146; no journal version on Crossref). State: real-correct. Both spans are verbatim in the abstract (ImproperX.tex). The source subject is "d'Espagnat's argument"; the article paraphrases it outside the quotes as "inconsistency claim", which is acceptable.
- **Zeh 2006** (Séminaire Poincaré 1, 115–129). State: real-correct. The recoherence span is verbatim (Zeh+Cont.tex), and its referent ("this difference" = true vs apparent ensembles) matches the article's lead-in. The "an Everettian rather than an ally" characterisation is correct.
- **Bacciagaluppi 2012** (EJPS 3(1), 87–100; Crossref online 2012-06-26, print 2013-01). State: real-correct. Both spans are verbatim (pdftotext of philsci-archive 9121, "insolubility-absolutely_final_version.pdf"). The year follows the online date, which is acceptable.
- **Adler 2003; Hance & Hossenfelder 2022; Fortin & Lombardi 2014; Wallace 2010; Wallace 2012; d'Espagnat 1966/1976.** State: real-correct per the 2026-09-03 ledger, which names its sources (Crossref DOIs and raw artefacts). Not re-litigated, except:
  - Fortin & Lombardi: arXiv API journal_ref confirms Found. Phys. 44, 426–446.
  - Wallace: the undated inline mention now carries "(2010; 2012)", so both References entries have an inline (surname, year) pair.
- **Self-cites 22–23** — unchanged.

Cross-reference inline ↔ References is closed in both directions, checked by (surname, year). No retracted works. The superlative helper returned only "so far" (L86), and that sentence was rewritten.

### Medium Issues Found

- **L86 awkward self-reference.** The text read: "The gap argument as stated on this page is conditional on a premise the page has not so far named." The paragraph had just named the premise. It is now replaced, word-neutrally, by a sourced point: d'Espagnat's own claim is scoped to partial traces of a *pure* composite state, so the gap argument inherits that premise.
- **Redundant defeater-framing clause** (L90, "and stating the defeater precisely strengthens rather than softens it"). It duplicated L101's "sharpens the Map's honesty rather than retiring the risk." Cut (−10).

### Counterarguments Considered (reasoning mode; editor-internal)

- **Kirkpatrick / Castellani:** Mode One. The underdetermination point comes from their shared premise. Liu et al. now independently scope that premise to prediction.
- **Wallace / Everett:** Mode Three. Honestly routed to Tenet 4.
- **QBism (Schlosshauer 2019):** Mode Three. "lapses rather than fails."
- **Chen density-matrix realism:** honest concession. The Map has not defended its side, and the review left that concession intact.
- **Active inference (L103):** Mode Three. It is stated as conditional on a selecting principle being needed.
- **Label leakage:** grep for the editor-vocabulary terms came back clean.

### Calibration Check

The tenet-accepting reviewer test was applied to every addition since 2026-09-03. The Liu paragraph explicitly denies support to the Map's reading. The Chen paragraph concedes an undefended premise. The Bohm route says "declining is not refuting." The L107 fix lowers rather than raises: it restores a condition. No possibility/probability slippage was found.

## Optimistic Analysis Summary

### Strengths Preserved

- The FAPP-history section. Bell's own text now confirms that he coined the acronym in this paper.
- The two-directions underdetermination argument (Kirkpatrick to all-improper, Castellani to all-proper).
- The detectability split verdict (locally no; globally and in principle yes).
- The "three limits" on the Liu et al. result. This is model evidential discipline: a new result the Map could have recruited is explicitly denied that role.
- The Chen paragraph's candour about an undefended premise.
- "Declining is not refuting" on the Bohm route.

### Enhancements Made

- The L86 sentence now grounds the global-purity premise in d'Espagnat's own scoping, with a verbatim source in the Reply.
- The Wallace inline years were added.
- Three References entries were brought to their publisher of record.

### Cross-links Added

- [qbism](/concepts/qbism/) (zero-word pipe on "QBism", L82)
- [penrose-gravity-induced-collapse-empirical-prospects](/topics/penrose-gravity-induced-collapse-empirical-prospects/) (zero-word pipe on "Diósi–Penrose model", L96; that page carries the Donadi/Majorana/XENONnT detail)

## Remaining Items

- **Out of scope, not fixed:**
  - **Tomaz 2025 is cited arXiv-only on seven other live pages:**
    - apex/what-consciousness-tells-us-about-physics L278
    - topics/quantum-measurement-and-consciousness L229
    - concepts/measurement-problem L235
    - concepts/quantum-completeness L151
    - concepts/physics-as-disclosure L131 (quotes v1, and notes that v2–v3 revise the wording)
    - topics/forward-in-time-conscious-selection L218 (has the venue but no DOI)
    - concepts/prebiotic-collapse L233, which also drops two co-authors ("Tomaz, A. (2025)"), so that one is real-wrong-metadata
  - **The research note still carries the Castellani 2022/arXiv form** (L67, L110, L192 of research/improper-versus-proper-mixtures-2026-09-02).
  - **`concepts/wavefunction-realism-vs-primitive-ontology` never mentions density-matrix realism.** This page's L86 links it as the home of that dispute.
  - **`concepts/qbism` has no reciprocal link back here.** The page is on the current avoid list, so the link was not added.
- **Covered by the queue:**
  - The L107 framing "The Map holds the gap open" sits under an objective-reduction baseline that closes it outside neural systems. That is the corpus-level collapse-priority debt (todo L1734 research task), and this review does not adjust it.
  - The L107 "Dualism tenet reads…" wording sits next to the Tenet 3 wording question, which is blocked on a human decision.

## Stability Notes

- This review carries forward both 2026-09-03 notes: the ontological-weight commitment is a declared wager, and the two 1966 d'Espagnat items are a standing bibliographic trap.
- **The Castellani year is 2023 (IJQI), not 2022.** The arXiv posting is 2022. Do not revert on the strength of the research note or the arXiv ID.
- **Bell's exits:** the Map declines Bohm and adopts objective collapse *as baseline only*. Do not reintroduce "both of which the Map declines," with or without "consciousness-free." That phrasing contradicts tenets.md L125 and this page's L96.
- **The Schlosshauer 2004 "no outcome having been singled out" quote must keep its e-e-link qualifier** outside the quotation marks.
- **The L107 Local Friendliness consequence is conditional on locality plus no-superdeterminism.** Removing the condition re-creates a contradiction with the Bohm route at L99.