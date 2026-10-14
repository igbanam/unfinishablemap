---
title: "Deep Review - The Graduated Middle Path: Valence-Modulated Attention"
created: 2026-10-14
modified: 2026-10-14
human_modified: null
ai_modified: 2026-10-14T06:41:40+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-14
last_curated: null
---

**Date**: 2026-10-14
**Article**: [[graduated-middle-path-valence-modulated-attention|The Graduated Middle Path: Valence-Modulated Attention]]
**Previous review**: [[deep-review-2026-07-18-graduated-middle-path-valence-modulated-attention|2026-07-18]]

## Convergence Context

The article's own text was stable from 07-18 until the refine-draft of 2026-10-12 (`d748342294`), which redefined the modulator V(Oᵢ) at L46 as present felt anticipation (per P-VS1) and reworked L50's sign-asymmetry paragraph against the weighting article's five rows, adding Yechiam & Hochman 2013 and Yechiam & Zeif 2025. This pass reviewed that refine and, more importantly, what moved *under* the article. The parent `topics/valence-and-conscious-selection` was rewritten by refine-draft `db12a423dc` (2026-09-05 21:10Z), which removed two passages this article quotes verbatim and changed the status of the equal-salience test this article builds on. The L46 redefinition also changed what "valence" means in the clamp design (§"The Discriminating Signature"), which nobody had re-read in that light.

Word count 2786 → 2902 (+116), below the topics soft threshold of 3000.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Broken verbatim quote of the parent (L68): CRITICAL, fixed.** The article quoted the parent as saying "valenced options should be selected more readily than neutral options **of equal attentional salience**." That text was removed from the parent in `db12a423dc`. The parent now reads (L164) "valenced options should be selected more readily than equally salient neutral options—which every rival above also predicts, so only the operationalised form below discriminates." The quote is now the live wording, and the article reports the parent's concession.
2. **Discrimination claim contradicted by the parent's update (L68): CRITICAL calibration error, fixed.** "Read carefully, an equal-salience design is the discriminating instrument" now conflicts with the parent's statement that every mechanism-sufficient rival predicts the bare equal-salience advantage. It is rescoped to "Equal salience is still the instrument that separates the horns within the fork". That is true: the clamp separates the three within-fork rows, which P-VS2 and the steelman both confirm.
3. **Felt anticipation not discriminated from value-blind selection (L68), introduced by the L46 redefinition: CRITICAL calibration error, fixed.** Once V(Oᵢ) means present felt anticipation, a "valence selection advantage" measured without controlling learned value and the unfelt forecast cannot be attributed to felt valence. The canonical terminology map (`wanting-liking-and-the-value-in-mechanism-fork#shared-terminology`) lists learned value (V/Q) as "the value-blind rival's chooser input". An unfelt value signal can therefore produce the middle path's row (acting through attention) or the value-sensitive horn's row (entering choice directly). A tenet-accepting reviewer would still flag the old text, which makes this calibration rather than bedrock. Two sentences were added: the advantage counts only if it tracks present affect with the unfelt forecast and learned value measured and held, which is the input dissociation `concepts/affective-forecasting-gap` L84–91 sets out; without that control "the battery cannot tell value-blind selection from felt anticipation." This also governs L79's residual branch, so "residual advantage" now means the controlled one, which is consistent with parent L113's "at neural-value indifference choice tracks independently reported anticipatory affect".
4. **Broken verbatim quote of the parent (L58): CRITICAL, fixed.** 'valence is what the parent article calls "upstream infrastructure."' That phrase was removed in `db12a423dc`. It is replaced with the parent's live wording (parent L147): 'value is, in the parent article's words, "a cause of selection via attention rather than a bystander."' The subject was kept as "value" to match the source sentence.
5. **Stale currency phrasing contradicting P-VS1 and the article's own L46 (L58): CRITICAL internal contradiction, fixed.** "outcomes selected because of how they would feel" was missed by the 10-12 refine. P-VS1 now says outcomes "are selected by how anticipating them now feels, not by how they would feel". It now reads "outcomes selected because of how anticipating them feels".

### Medium Issues Found

- **L50 leaned toward the middle path on evidence the rival shares: fixed.** The weighting article (L69, L79) places attention allocation on the policy row among the "rows the rival already owns", as a "genuine parsimony advantage for the rival". The article's "the evidence there leans toward this page's coupling … congenial to the middle path" let the Yechiam evidence read as favouring the middle path over value-blind selection. It now reads "part of the evidence there points to the row this page's coupling occupies" (the weighting article itself places other evidence on the forecast row) and adds "without favouring it over value-blind selection, which the weighting article grants can carry the same tilt by attention allocation alone". The existing "no evidence that anything in it is felt" guard is kept.
- **"two-paragraph sketch" (L38, L101): fixed, word-neutral.** The parent's middle-path section has grown past two paragraphs (it now includes the aDDM product-term sentence). Changed to "brief sketch".

### Checks that passed

- **L46 against P-VS1 and the weighting/terminology pages:** matches. "the goodness or badness of actualising Oᵢ as felt now in anticipating it, the present anticipatory affect that carries its forecast" agrees with P-VS1 ("the *presently felt* valence of anticipating each outcome — an occurrent state at choice") and with the terminology map's "Present anticipatory affect" row ("the felt vehicle of predicted utility"). The anchor `#shared-terminology` exists (`{#shared-terminology}` at wanting-liking L76). The fallback sentence, "Were the forecast computed unfelt, the modulator would be predicted utility", agrees with the map's predicted-utility row ("Felt as such? Only insofar as present anticipatory affect … carries it").
- **L50 against the weighting article:** "splits that question into five candidate rows and fixes none" matches weighting L69 ("The article fixes no row"). The Yechiam characterisations match weighting L43/L65/L67, and "which that article reads as placing part of it in how options are compared" correctly attributes the policy-row reading to the Map article, not to Yechiam & Zeif (whose abstract says only "suggesting similar weighting of gains and losses").
- **"doubly non-epiphenomenal—real as experienced *and* efficacious as selector"**: verbatim at parent L129. **"the most defensible current stance"**: verbatim at parent L190.
- **P-VS2 consistency:** the table's rows and the steelman co-extensiveness concession match P-VS2 tier (1) and steelman L103. P-VS2's "the clamp limit above, is demonstrated rather than feared" is already reflected at L77.
- **Style:** no "This is not X. It is Y."; zero "load-bearing". The anchoring audit was not consulted and no hedges were padded (`anchoring_audit_exempt: true` respected).

### Publisher-of-Record Citation Web-Verify (§2.4)

References changed since the last deep review (refs 7–8 added), so the pass was mandatory. Ledger:

- Yechiam, E. & Hochman, G. (2013). Losses as modulators of attention… *Psychological Bulletin* 139(2), 497–518, doi:10.1037/a0029383 — **real-correct** (Crossref: authors, title, venue, vol/issue/pages, 2013-03). **Quote verified verbatim** against the OpenAlex abstract (inverted index): "asymmetric effects of losses on behavior emerge where gains and losses are presented separately but not concurrently." The paraphrase "model losses as increasing on-task attention rather than carrying more weight" is faithful: the abstract contrasts the "commonly explained" view that "losses are given more weight" with their "attention-allocation model … losses increase on-task attention". Result direction correct. Stance: decision psychologists, no metaphysical commitment, not presented as endorsing the Map; "congenial" is the article's own reading.
- Yechiam, E. & Zeif, D. (2025). Loss aversion is not robust: A re-meta-analysis. *Journal of Economic Psychology* 107, 102801, doi:10.1016/j.joep.2025.102801 — **real-correct** (Crossref: authors, title, venue, vol, article number, 2025-03). The abstract was verified via RePEc/IDEAS (ScienceDirect 403; OpenAlex/S2 carry no abstract): "for studies with symmetric gains and losses and no ordering of items, the loss aversion parameter was approximately 1.07 and not significantly above 1.0". The article's "falls to about 1.07 under symmetric, unordered amounts" is faithful, and the result direction is correct. The re-meta-analysis is of Brown et al. 2024's dataset (84 papers, 163 estimates); the article does not restate that and need not.
- Stapp, H.P. (2007). *Mindful Universe*. Springer — **real-correct** (Crossref finds the 2011 second edition, doi:10.1007/978-3-642-18076-7; the 2007 first edition in The Frontiers Collection is the original; unchanged since 07-18).
- Joffily, M. & Coricelli, G. (2013). *PLOS Comput Biol* 9(6) e1003094 — **real-correct** (Crossref re-checked; paraphrase verified 07-18).
- Sandved-Smith, L. et al. (2021). *Neurosci Conscious* 2021(1) niab018 — **real-correct** (Crossref re-checked: six authors, venue, article number; characterisation verified 07-18).
- Refs 4–6: Map self-cites (AI-pseudonym convention), intact.

Inline ↔ References: all five external works are cited inline and listed, with no orphans in either direction. The superlative-claim helper returned nothing.

### Counterarguments Considered

- **Hard-Nosed Physicalist / Eliminative Materialist**: "a felt-anticipation modulator and an unfelt forecast predict the same data." Previously this was implicit; it is now stated at L68 and conceded as a limit of the battery. This is calibration, handled inside the framework.
- **Empiricist (Popper)**: "the clamp is unfalsifiable as a test of feeling." Answered by naming the input dissociation that would make it a test of feeling (from the forecasting article), not by claiming the clamp alone does so.
- **MWI Defender / physicalist same-architecture**: bedrock, per the 07-18 Stability Notes; not re-flagged.

### Reasoning-Mode Classification (§2.6)

Engagement with active inference / predictive processing (§"The Physicalist Rival the Test Cannot Reach"): unchanged, **Mode Three**, honest boundary-marking. The new L68 sentences add an in-framework concession about the Map's own battery; they are not an opponent engagement. No editor-vocabulary label leakage.

## Optimistic Analysis Summary

### Strengths Preserved

- The front-loaded deflationary verdict and the "abolition-by-clamp *is* the demotion" loop-closure (L79), untouched.
- The 10-12 refine's L46 redefinition and its explicit flagging of the felt-anticipation assumption; the new L68 sentences complete it by saying what would test that assumption.
- L50's closing guard ("attention can be allocated without feeling") is kept verbatim inside the expanded sentence.

### Enhancements Made

- L68 now points readers to the corpus's actual felt-versus-computed discriminator (the forecasting article's input-dissociation rows), which links the clamp to the P-VS2 battery more precisely.

### Cross-links Added

- [[affective-forecasting-gap]] (body, L68)

## Remaining Items

- **Out of scope, minted (P3 positions-evolve):** P-VS2's tier-(1) first leg still states that the bare equal-salience advantage "supports value-sensitive selection", which the parent has denied since `db12a423dc` (17h after P-VS2's last edit). The register file is at 2,498 of the 2,500 hard limit, so the fix must be net-zero or go in the calibration-history sidecar. P-VS1 defers with "each as qualified there", so it needs no edit.
- No live sibling carries the two dropped parent quotes. They survive only in `archive/topics/value-blind-vs-value-sensitive-selection.md` and `archive/topics/valence-as-selection-currency.md`, the pre-coalesce originals they came from, where they are correct.

## Stability Notes

- The 07-18 notes stand: the MWI / genuine-indeterminacy and physicalist "same architecture, no primitive" objections are bedrock; the conditionalisations are calibration, not hedging.
- **New:** the clamp battery separates the three within-fork rows *conditional on* an input-dissociated valence measure; it never separates felt anticipation from an unfelt value signal by itself. Future passes should not strengthen L68/L79 back toward "the equal-salience design discriminates" without that control. Conversely, do not read the L68 control sentence as hedging to trim.
- **Watch the parent.** This article quotes `topics/valence-and-conscious-selection` verbatim in several places (L38, L56, L58, L68). A refine of the parent can silently break them, as `db12a423dc` did for two. Grep each quoted string against the parent on every pass.
