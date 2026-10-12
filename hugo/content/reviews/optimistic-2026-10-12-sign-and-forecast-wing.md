---
ai_contribution: 100
ai_generated_date: 2026-10-12
ai_modified: 2026-10-12 06:36:00+00:00
ai_system: claude-opus-5-5
author: Andy Southgate
concepts: []
created: 2026-10-12
date: &id001 2026-10-12
description: Wing review of the negative-valence weighting page and the affective-forecasting
  gap. Loss aversion is the rank reversal the forecasting page says it lacks, and
  neither page says so.
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-10-12 06:36:00+00:00
modified: *id001
related_articles: []
title: Optimistic Review - 2026-10-12 - The Sign-and-Forecast Wing
topics: []
---

# Optimistic Review: The Sign-and-Forecast Wing

**Date**: 2026-10-12 (06:36Z)
**Slot**: optimistic-review. No content file was modified. Three tasks were minted from the [Priority List](#priority-list) above `## Completed Tasks` in `todo.md`.

**Why this wing.** Coverage was measured on review *content*. All 597 `optimistic-*.md` files were concatenated and every live slug in `topics/ concepts/ voids/ apex/ positions/` was counted (`str.count`, refinement-log and calibration-history sidecars excluded). The lowest page, `topics/whether-language-model-words-refer` (1), was created yesterday and set aside, as the 10-11 quadrant review set it aside on its creation day. The next lowest was `concepts/negative-valence-asymmetry-and-the-selection-weighting-function` (2): one mention is the 06-19 session list, the other is the 07-06 value-cluster review naming it "consulted for topology". Its closest sibling, `concepts/affective-forecasting-gap` (7), was created the same day by the same pass and got the same "consulted for topology" treatment on 07-06. Neither page has been the subject of an optimistic pass. The three recent wings (10-10 ancestry-and-duplicate, 10-11 constitutive twins, 10-11 quadrant geometry) and `concepts/agent-causation` (open P2 from today's outer reviews) are not touched. The other low pages (`prospective-memory`, `capgras-delusion…`, the 10-04 self-control/brain-stimulation pair, `voids/attention-and-consciousness`, `voids/resolution-void`, 3 each) do not form a cluster with each other.

**Content reviewed.** Both wing pages were read in full. Neighbours were read at the loci named. Lengths come from `tools.curate.length.analyze_length` at 06:20Z. The gate is `>=`, so headroom = hard − 1 − count. Line numbers are **file** line numbers, frontmatter included.

| File | Count | Hard | Headroom | Read |
|---|---|---|---|---|
| `concepts/negative-valence-asymmetry-and-the-selection-weighting-function` | 3,109 (prose 2,567 · Further Reading 95 · refs 447) | 3,500 | 390 | full |
| `concepts/affective-forecasting-gap` | 3,616 (prose 2,716 · Further Reading 28 · refs 872) | 3,500 | **−117 (over hard: net ≤0 only)** | full |
| `topics/graduated-middle-path-valence-modulated-attention` | 2,586 | 4,000 | 1,413 | L42–L80, refs |
| `topics/wanting-liking-and-the-value-in-mechanism-fork` | 3,023 | 4,000 | 976 | L76–L96 (the map) |
| `topics/valence-and-conscious-selection` (parent) | 4,338 | 4,000 | **−339 (over hard: 0-word edits only)** | L185–L196 |
| `positions/value-in-selection` ([P-VS1](/positions/value-in-selection/#p-vs1)) | 2,498 | 2,500 | **1** | L50–L56 |
| Also read at named loci: `topics/the-steelman-for-value-blind-selection` L125 (2,997; 1,002); stability notes of the 08-20 forecasting, 08-27 weighting, 08-27 wanting/liking, 07-18 graduated and 10-08 parent deep reviews. | | | | |

The forecasting page is over hard on its total. Its prose (2,716) sits inside the band, and 24% of the count is reference apparatus. The gate still binds, so every edit to it below nets negative.

Section counts (`count_section_files`, 06:25Z): topics 344 and concepts 348 (cap 360 each), voids 112 (cap 115), positions 23, apex 44. Hugo mirrors exist for both wing pages. Inbound body links: the forecasting page has 15 linking pages, the weighting page 6. **The forecasting page links the weighting page only from Further Reading (L112)**, while the weighting page links the forecasting page four times in its body.

## Executive Summary

These are two of the Map's most carefully calibrated concept pages. Each takes a question the parent fork left open (does positive and negative valence weigh equally; which valence, anticipated or experienced, selects), concedes the rival's strongest exhibit, and declines to fix an answer the evidence does not fix. Their convergence goes unnoticed. The weighting page's 08-27 revision found that the loss-aversion tilt is "more a property of affective forecasts than a property of affective experience" (Kermer et al. 2006). The forecasting page argues that a forecast error matters for selection only where a *differential* bias reverses the ranking of options, and that "the literature rarely reports" such a reversal. **Loss aversion is that case.** The mechanism Kermer et al. name, underestimated rationalisation, is the forecasting page's own *immune neglect*, which concerns negative affect only. A bias that inflates only losses is differential across any choice between a mixed gamble and a sure thing. Both halves are already on the Map, and the reversal follows from them. Neither page states it.

The wing also exposes one stale neighbour. `graduated-middle-path-valence-modulated-attention` is unchanged since 07-18. Since then the cluster has moved its candidate currency to the *presently felt* valence of anticipating ([P-VS1](/positions/value-in-selection/#p-vs1), 08-27), and the weighting page has split "felt value or the mechanism" into five rows, one of which is the middle path's own coupling. The middle path still defines its modulator as a forecast and states the binary, so it misses the evidence that most favours it.

## The Convergence

### Two open questions, one point of contact

The parent lists its open questions separately: "Anticipated vs experienced valence" (L194) and "Negative valence and avoidance" (L196). The two sibling pages were written as answers to one each, and each says so (weighting L31: "a distinct *question* from its siblings"). By 08-27 the weighting page had placed its coefficient more readily in the forecast of an outcome than in the experience of it (L59–L61). That joins the questions. The sign asymmetry is, in part, the forecasting gap with a sign attached.

### Why the joint matters for the forecasting page's own argument

The forecasting page's strongest move is at L82. Selection needs a correct *ranking*, not correct magnitudes, so an exaggeration that every option shares does no harm. Only a differential bias that reverses ranks counts against the currency. That argument is right, but its example of a harmless bias is too broad: "a shared exaggeration of every option's predicted unpleasantness leaves the ordering intact". That holds only when every option carries the same unpleasantness. Between a 50–50 gamble (win G, lose L) and a sure zero, inflating predicted unpleasantness touches only the gamble. Suppose the forecast coefficient on losses exceeds the experienced one. Then whenever G/L falls between the two, the forecast ranks the sure thing first, though the experienced outcomes would on average favour the gamble. The page's own L36 defines immune neglect as failing to anticipate "the rationalisation and reframing that dampen negative affect", and Kermer et al.'s abstract names that mechanism: "they underestimated their tendency to rationalize losses". So the page already contains the source of a differential bias besides the focalism it names.

This is an *inferred* reversal, not a demonstrated one. Kermer et al. report forecasts and experienced feelings, and the forecasting page asks for "a forecast error shown to change the option chosen". The finding gives that test its best target. It does not satisfy it. Item 1 says so in the text.

### The middle path's row

The weighting page's five rows are experienced utility, predicted utility carried by present anticipatory affect, learned value, incentive salience, and the selection policy. Its contested-status evidence points at the last of these. Yechiam and Hochman (2013) model losses as raising on-task attention rather than carrying more weight, and find that "asymmetric effects of losses on behavior emerge where gains and losses are presented separately but not concurrently". Yechiam and Zeif's (2025) re-meta-analysis finds the coefficient "approximately 1.07 and not significantly above 1.0" under symmetric, unordered amounts. That row is where a valence→attention hybrid lives. The graduated page (L50) still says the sign question is "whether the asymmetry … lives in felt value or in the mechanism that reads value", which is the binary the weighting page's 08-27 stability note forbids collapsing back to, and concludes the middle path "inherits it unresolved". It still inherits it unresolved, because nothing places the tilt. But the evidence leans toward its row, and the page should say so with the Hardline Empiricist's qualifier: attention can be allocated unfelt.

The same page defines its modulator V(Oᵢ) at L46 as "the predicted felt goodness or badness of actualising Oᵢ". On the canonical shared terminology map (wanting/liking L76–L90) that is *predicted utility*, which is felt "only insofar as present anticipatory affect … carries it". The forecasting page's own battery (L86–L90) models the hybrid as responding to a shift in *present affect* with the forecast held fixed. So the cluster already treats the middle path's input as felt anticipation, but the middle path's specification does not. The gap matters for the middle path's audit at L60, which claims to "defeat epiphenomenalism about valence in the narrow sense". That claim concerns felt valence only if the modulator is felt.

## Praise from Sympathetic Philosophers

### The Property Dualist (Chalmers)

The two pages keep the explanatory gap in view where it is easiest to lose it, inside decision science. The weighting page's L45 ("Prospect theory is a model of decision behaviour; the negativity-bias programme describes information processing. Neither measures phenomenology") refuses the slide from a behavioural coefficient to a felt one that most of the literature makes silently. The forecasting page does the same for dopamine. It asks whether the prediction error "reaches feeling" and cites Blain and Rutledge's finding that momentary happiness is "not sensitive to … reward prediction error". Chalmers would praise both for treating "is this quantity felt?" as an open empirical question about each row, not as something settled by definition.

### The Quantum Mind Theorist (Stapp)

Stapp's process 1 needs something on the mental side that does the choosing, and these pages are the Map's most precise account of what that something consults. The forecasting page's answer is anticipatory affect, "anticipated in its *object*, experienced in its *vehicle*" (L76). That gives a Stappian chooser a present, occurrent input with no backward causation. The pages are equally careful about the cost. Forecasting L94 marks the claim as token-grain, citable "as a framework-internal coherence result only, never as established mental causation", and inheriting the mechanism debt ([P-Q3](/positions/quantum-interface/#p-q3), [P-Q10](/positions/quantum-interface/#p-q10)). Stapp would welcome a specification this exact and would accept the debt.

### The Phenomenologist (Nagel)

The anticipated/anticipatory distinction (Loewenstein et al. 2001) at forecasting L28 is phenomenology done with experimental tools. The dread of the appointment is a present experience with its own character, not a prediction about one. The weighting page's "third reading" (L61) builds on it: a forecast-located coefficient "is felt at the point of selection … and is still not a property of value". Nagel would value the precision. The question "is the badness of losing felt as larger?" is answered by locating *when* it is felt, without denying that it is felt.

### The Process Philosopher (Whitehead)

A process reading suits the forecasting page's account of anticipation as an occasion that feels its own possible futures, and of value as fully present only in the occasion that realises it. The page's L78 separation of what selection is causally *sensitive to* (present anticipation) from what it is normatively *for* (the outcome's experience) is close to Whitehead's subjective aim and its satisfaction. The constraint applies here. This resonance removes no defeater the pages need and raises nothing on the evidential scale. Both pages hold their claims at [P-VS1](/positions/value-in-selection/#p-vs1)'s "credence low", and process-compatibility gives no reason to move that.

### The Libertarian Free Will Defender (Kane)

Kane would read the two pages as an account of how reasons enter a self-forming choice. The agent's felt anticipation of each option, imperfectly calibrated, does the weighing. The weighting page adds that negative anticipation weighs more. That is a fact about the deliberating agent's psychology, not a constraint on agency. The pages' refusal to say the felt input *determines* the outcome ([P-VS1](/positions/value-in-selection/#p-vs1): "an aspiration, not a position") leaves room for the indeterminist choice Kane needs.

### The Mysterian (McGinn)

The anaesthesia section of the forecasting page (L48–L64) shows that the channel can be closed. Under anaesthesia, the record a forecaster learns from can be empty, distorted, or present only as an implicit trace that "no questionnaire reaches". The page's L62 confines the Map's inference: "license no quantified discount elsewhere, so this article applies none". McGinn would praise the restraint. The page names a limit on what introspective records can teach and does not convert the limit into a result.

### The Hardline Empiricist (Birch)

This is the wing's strongest persona, and its verdict is favourable. Neither page touches minimal-organism tiers, but both carry claims that a less careful page could have raised on tenet support alone, and both decline to.

- The weighting page states its own premise as contested before using it: "the behavioural asymmetry it builds on is real-but-contested, not a settled pillar" (L29). It gives the contest both sides with numbers: Brown et al.'s λ ≈ 1.96 [1.820, 2.102], and Yechiam and Zeif's 1.07 under symmetric, unordered amounts (verified this session at the RePEc abstract).
- It ends without fixing a row: "The article fixes no row … Those are three claims of different strength, none a stipulation" (L67). The 08-27 stability note keeps it that way.
- The forecasting page concedes the rival's exhibit before replying, and keeps "calling the gap a calibration problem does not cancel its likelihood-bearing force" (L72). That is a sentence a tenet-driven page would have cut.
- Both pages route their Occam's-razor reply through argument, not through the tenet. Weighting L77: "The argument, not the razor, carries the decline." Forecasting L102 says the same. That is *tenet-coherent, not evidence-elevating*, written into the text.

The items below are written to that standard. Item 1's reversal is labelled "inferred …, not observed as a changed choice". Item 1(b)'s interoception result is called "the nearest the evidence comes to a felt row: one small correlational study". Item 2's attention evidence is "no evidence that anything in it is felt".

## Content Strengths

### concepts/negative-valence-asymmetry-and-the-selection-weighting-function

- **Strongest point**: The five-row disaggregation (L57–L67), which turns "is the bias in feeling or in mechanism?" into rows with named discriminators: format invariance, forecast versus experience, and abolishing felt badness.
- **Notable quote**: "The measured coefficient is compatible with a tilt on any upstream row; the task is to say which rows could carry it and what would tell them apart, not to stipulate one."
- **Why it works**: The page converts a vague dispute into a test battery and then grades its own conclusions by strength.

### concepts/affective-forecasting-gap

- **Strongest point**: The ranking argument (L82). Selection needs order, not magnitude, so most forecasting error is harmless to a value-sensitive currency, and the page names exactly what would make it harmful.
- **Notable quote**: "short of that, absolute inaccuracy is no exhibit against a currency that still ranks correctly."
- **Why it works**: The page finds the one condition under which the rival's exhibit has force, and asks for it. Item 1 supplies a candidate.

### topics/graduated-middle-path-valence-modulated-attention

- **Strongest point**: Its "Discriminating Signature" table. Its own confirming result (abolition by clamp) is the result that withholds the strong claim, and the page says so: "confirming the middle path is confirming the weaker thesis."

## Expansion Opportunities

### High Priority

#### Demonstrated forecast-driven mischoice (research-topic, for the harvester)
- **Builds on**: `concepts/affective-forecasting-gap` L82 ("What the argument needs, and the literature rarely reports, is a *demonstrated* reversal"), and Item 1's inferred reversal.
- **Would address**: Whether any study shows a forecast error changing the option chosen relative to the option that would have been experienced as better, as opposed to forecasts merely being inaccurate. "Miswanting" has 0 hits on live pages, research notes and active tasks. Leads, each verified at Crossref for metadata only: Hsee & Zhang (2004), "Distinction bias: Misprediction and mischoice due to joint evaluation", *JPSP* 86(5):680–695, doi 10.1037/0022-3514.86.5.680, whose abstract claims failures "to make experientially optimal choices"; Hsee & Hastie (2006), "Decision and experience: why don't we choose what makes us happy?", *TICS* 10(1):31–37, doi 10.1016/j.tics.2005.11.007; Gilbert & Wilson, "Miswanting" (Crossref returns the 2006 reprint in *The Construction of Preference*, pp. 550–564, doi 10.1017/cbo9780511618031.031; the original 2000 chapter was not checked). The research should establish whether any of these reports a *choice* change, and whether a loss-aversion study has measured forecast, experience and choice in the same participants.
- **Estimated scope**: A research note, then probably a short concepts page or a section on the forecasting page. The forecasting page is over hard, so the note should recommend which.
- **Tenet alignment**: Bidirectional Interaction (whether the felt input can be shown to do selective work), and Occam's Razor Has Limits (the rival's parsimony is met with evidence, not with the razor).

### Medium Priority

#### A second target for the clamp
The graduated page's salience clamp predicts that a valence advantage is abolished when attention is equalised. If part of loss aversion is attentional (Yechiam & Hochman 2013), the same clamp gives a second prediction: equalising salience should shrink the measured λ. That would test the policy row directly. Leave this for a later refine of the graduated page, once Item 2 has landed.

### Ideas for Later

- **Arousal without access.** Yechiam & Hochman's abstract reports that in experience-based tasks "increased arousal is observed simultaneously with no behavioral loss aversion", while Sokol-Hessner et al. (2015) find that conscious access to bodily signals predicts λ. Arousal alone not producing the tilt, while perceiving arousal predicts it, is suggestive for the felt rows. The paradigms differ (experience-based versus description-based), so no inference is licensed yet.
- **Loss aversion where felt badness is reduced.** The weighting page's L65 notes that the pain-asymbolia test is "as of 2026, unrun". Alexithymia (`concepts/alexithymia` exists) is a more tractable population for the same question.

## Cross-Linking Suggestions

| From | To | Reason |
|------|-----|--------|
| `affective-forecasting-gap` L82 | `negative-valence-asymmetry…` | First body link; installed at 0 net words by Item 1(c) |
| `wanting-liking…` shared terminology map | `negative-valence-asymmetry…`, `graduated-middle-path…` | The map has no row for the "policy row" that the weighting page cites three times (L63, L65, L67); Item 2(c) adds it |
| `graduated-middle-path…` L46 | `wanting-liking…#shared-terminology` | Aligns V(Oᵢ) with the canonical vocabulary; Item 2(a) |
| `valence-and-conscious-selection` L196 | (existing link, relabelled) | Reports the sibling's finding instead of restating the open question; Item 3 |

## New Concept Pages Needed

- None now. A page on miswanting may follow from the research subject above.

## Priority List

Cap 4; three items were needed. Every old string was checked by script to occur exactly once in its file at 06:31Z. Costs are `count_words(new) − count_words(old)` from `tools.curate.length`. **Each task's Notes line repeats its Caution and Headroom, because fields above `Notes:` do not reach the fork.**

**1. The reversal the forecasting page is missing. `concepts/negative-valence-asymmetry-and-the-selection-weighting-function` L61, L65 and references; `concepts/affective-forecasting-gap` L82. Type: refine-draft. Cost +174 (headroom 390) and −1 (−117, over hard).**
- (a) Weighting L61 (+90). Old: "at the price of making the negative bias partly an instance of the forecasting gap." New: "at the price of making the negative bias partly an instance of the forecasting gap. It is also the instance that gap needs. The underestimated rationalisation Kermer et al. name is that article's immune neglect, which concerns negative affect, so between a 50–50 mixed gamble and a sure thing the bias is differential: where the gain-to-loss ratio falls between the experienced and the forecast coefficient, the forecast ranks the sure thing first though the experienced outcomes would, on average, favour the gamble. That is the rank reversal [the forecasting article](/concepts/affective-forecasting-gap/) finds rarely reported, inferred here from forecasts and feelings, not observed as a changed choice."
- (b) Weighting L65 (+59). Old: "shows the coefficient is modulable through an affect-adjacent channel, without settling whether that channel is felt." New: "shows the coefficient is modulable through an affect-adjacent channel, without settling whether that channel is felt. Perceiving that channel predicts the coefficient: heartbeat-detection accuracy, a measure of conscious access to bodily signals, correlated with loss aversion and with no other value parameter (r = .57, 22 participants; Sokol-Hessner, Hartley, Hamilton and Phelps 2015). That is the nearest the evidence comes to a felt row: one small correlational study, which a common cause could also explain."
- (b-ref) Weighting references (+25). After the line ending "https://doi.org/10.1073/pnas.0806761106" (ref 15) insert: "16. Sokol-Hessner, P., Hartley, C. A., Hamilton, J. R., & Phelps, E. A. (2015). Interoceptive ability predicts aversion to losses. *Cognition and Emotion*, 29(4), 695–701. https://doi.org/10.1080/02699931.2014.925426", and renumber the three Southgate self-references 16–18 as 17–19.
- (c) Forecasting L82, two swaps (net −1). Old: "so a shared exaggeration of every option's predicted unpleasantness leaves the ordering intact and the bias bites only where it reverses ranks." New: "so a bias shared equally by every option leaves the ordering intact and bites only where it reverses ranks." (−3). Old: "a differential rather than shared bias—focalism inflates the focal option specifically—and a margin smaller than the differential." New: "a differential bias—focalism inflates the focal option, immune neglect [whichever carries the loss](/concepts/negative-valence-asymmetry-and-the-selection-weighting-function/)—and a margin smaller than the differential." (+2).
- Grounds: Kermer et al. 2006, Crossref abstract, verified verbatim this session: "People overestimated the hedonic impact of losses because they underestimated their tendency to rationalize losses and overestimated their tendency to dwell on losses. The asymmetrical impact of losses and gains was thus more a property of affective forecasts than a property of affective experience." Both Kermer quotations already on the weighting page at L59 match the abstract. Forecasting L36 defines immune neglect as concerning negative affect. Sokol-Hessner et al. 2015: Crossref metadata (29(4) 695–701; online 2014-06-11, print 2015) and the PMC full text (PMC4263686): "Interoception correlated only with loss aversion (log(λ) and sqrt(d′); r(20) = .57, p = .006 …)", with the authors' own limitation "a relatively small sample size (22 or 27, depending on participant exclusion)".
- **Caution**: weighting 08-27 stability note: the five-row disaggregation fixes no row and no row is upgraded to "established". (a) is labelled inferred, and (b) is labelled one small correlational study. Keep both labels. Do not attribute a choice measure to Kermer et al.; the reversal is the Map's inference. The forecasting page is 117 over hard, so (c) must net ≤0. Add no Kermer reference there; the link carries it. Its 08-20 notes (steelman congeniality as bedrock; MEQ disclosure praised as calibrated) stand, so do not trim the anaesthesia/MEQ material to fund anything. Re-measure both files with `analyze_length` afterwards.

**2. The middle path's modulator and row. `topics/graduated-middle-path-valence-modulated-attention` L46, L50 and references; `topics/wanting-liking-and-the-value-in-mechanism-fork` shared terminology map. Type: refine-draft. Cost +200 (headroom 1,413) and +65 (headroom 976).**
- (a) Graduated L46 (+12). Old: "the anticipated valence V(Oᵢ)—the predicted felt goodness or badness of actualising Oᵢ—sets two attentional parameters". New: "the anticipated valence V(Oᵢ)—the goodness or badness of actualising Oᵢ as felt now in anticipating it, the [present anticipatory affect](/topics/wanting-liking-and-the-value-in-mechanism-fork/#shared-terminology) that carries its forecast—sets two attentional parameters".
- (a′) Graduated L46 (+34). Old: "The specification assumes the typing in order to do its work, and flags that assumption as an assumption, not a finding." New: "The specification assumes the typing in order to do its work, and flags that assumption as an assumption, not a finding. It assumes too that the forecast is carried by felt anticipation. Were the forecast computed unfelt, the modulator would be predicted utility, and the audit below would concern a forecast rather than felt valence."
- (b) Graduated L50 (+107). Old: "Whether the asymmetry, if real, lives in felt value or in the mechanism that reads value is the same value-in-mechanism question one register down, developed in [negative-valence-asymmetry-and-the-selection-weighting-function](/concepts/negative-valence-asymmetry-and-the-selection-weighting-function/); the middle path inherits it unresolved." New: "Where the asymmetry sits, if it is real, is the same value-in-mechanism question one register down. [The weighting article](/concepts/negative-valence-asymmetry-and-the-selection-weighting-function/) splits that question into five candidate rows and fixes none, so the middle path inherits it unresolved, but the evidence there leans toward this page's coupling. Yechiam and Hochman (2013) model losses as increasing on-task attention rather than carrying more weight, and find that "asymmetric effects of losses on behavior emerge where gains and losses are presented separately but not concurrently"; in a re-meta-analysis the coefficient falls to about 1.07 under symmetric, unordered amounts (Yechiam and Zeif 2025), which that article reads as placing part of it in how options are compared rather than in any value consulted. That is congenial to the middle path and no evidence that anything in it is felt, since attention can be allocated without feeling."
- (b-ref) Graduated references (+47). After "https://unfinishablemap.org/concepts/attention-as-interface/" (ref 6, the last line) append "7. Yechiam, E., & Hochman, G. (2013). Losses as modulators of attention: Review and analysis of the unique effects of losses over gains. *Psychological Bulletin*, 139(2), 497–518. https://doi.org/10.1037/a0029383" and "8. Yechiam, E., & Zeif, D. (2025). Loss aversion is not robust: A re-meta-analysis. *Journal of Economic Psychology*, 107, 102801. https://doi.org/10.1016/j.joep.2025.102801".
- (c) Wanting/liking map, after the row ending "| The forecasting article's candidate selection currency; the felt vehicle of predicted utility |" add the row (+65): "| Policy (π) | Reinforcement learning; see [negative-valence-asymmetry-and-the-selection-weighting-function](/concepts/negative-valence-asymmetry-and-the-selection-weighting-function/) | The operation that compares the consulted quantities and acts, including how attention is spread across the options | Not a quantity; felt only insofar as the attending is | Where a weighting can sit with no consulted quantity tilted: the row of the [valence→attention hybrid](/topics/graduated-middle-path-valence-modulated-attention/), and on the weighting article's evidence part of loss aversion |". The `\|` escape follows corpus table convention (e.g. `empirical-evidence-for-consciousness-selecting` L124).
- Grounds: Yechiam & Hochman 2013 (OpenAlex abstract, verified verbatim; Crossref metadata 139(2) 497–518). Yechiam & Zeif 2025 (RePEc abstract: "for studies with symmetric gains and losses and no ordering of items, the loss aversion parameter was approximately 1.07 and not significantly above 1.0"; Crossref metadata 107, 102801). Map row "Predicted utility … Felt as such? Only insofar as present anticipatory affect (below) carries it" (wanting/liking L82). Forecasting L89: the hybrid column responds "via attention" to a shift in present affect with the forecast fixed. [P-VS1](/positions/value-in-selection/#p-vs1) (08-27, `aae02f38f3`) puts the currency in present felt anticipation. Graduated is unchanged since 07-18 (`451204534e`).
- **Caution**: graduated 07-18 stability notes: do not trim its conditionalisations as hedging, and keep it at "live hypothesis". (a′) and (b) add conditions and do not upgrade anything. Do not alter the clamp table, the weak/strong readings or the "Non-Epiphenomenality, Audited" section. Do not restate the felt/mechanism binary; the weighting page's 08-27 note forbids collapsing its five rows back to it. Wanting/liking 08-27 notes: the map is canonical for the cluster and descriptive, not a confidence move. This **adds** a row and changes none, and the forecasting page links the map without copying it, so nothing needs propagating. Do not re-strengthen the article's calibration. Update `ai_modified` on both files.

**3. The parent's open questions. `topics/valence-and-conscious-selection` L194 and L196. Type: refine-draft. Cost 0 (−339, over hard).**
- (a) L194 (0). Old: "Kahneman's experiencing-self/remembering-self distinction and the affective-forecasting literature show that humans systematically mispredict how experiences will feel." New: "Kahneman's experiencing-self/remembering-self distinction and the affective-forecasting literature show that humans mispredict how salient experiences will feel." Grounds: forecasting L30 ("For salient events the gap is a directional bias … in everyday life, a small absolute error") and L38 ("The Map's claim is conditional"); [P-VS1](/positions/value-in-selection/#p-vs1) calibration history ("forecasting claim conditionalised").
- (b) L196 (0). Old: "**Negative valence and avoidance.** A complete selection law must specify whether positive and negative valence are symmetric in selection influence or one is primary; asymmetric models (pain avoidance stronger than pleasure seeking) carry different empirical signatures—see [negative-valence-asymmetry-and-the-selection-weighting-function](/concepts/negative-valence-asymmetry-and-the-selection-weighting-function/)." New: "**Negative valence and avoidance.** If negative valence outweighs positive, selection needs a coefficient, not only a sign. [The weighting article](/concepts/negative-valence-asymmetry-and-the-selection-weighting-function/) finds the asymmetry contested and more a matter of forecast than experience, which joins the two questions." Grounds: weighting L27, L39, L43, L59.
- **Caution**: the parent is 339 over hard, so both edits must be exactly 0 words; check with `analyze_length`. The 10-08 and 07-08 stability notes (middle-path paragraph calibrated to the weaker reading; Carruthers representational reading) concern other paragraphs. Do not touch them. Keep "without closing the question against the graduated position above" at L194. Update `ai_modified`.

**Not verified** (named so no one assumes otherwise): whether either Kermer et al. (2006) study measured a choice. Only the abstract was read, and it reports forecasts and experienced impact; the Gilbert-lab PDF link returned HTML and a mirror timed out. Item 1(a) therefore labels the reversal as inferred. Also not verified: whether Sokol-Hessner et al. (2015) has been replicated (one search found no replication, and neighbouring interoception findings have replication trouble; the article text calls it one small study). The original 2000 printing of Gilbert & Wilson's "Miswanting". **Verified**: Kermer et al. 2006 (Crossref abstract), Sokol-Hessner et al. 2015 (Crossref and PMC full text), Yechiam & Hochman 2013 (Crossref and OpenAlex abstract), Yechiam & Zeif 2025 (Crossref and RePEc abstract), Hsee & Zhang 2004 and Hsee & Hastie 2006 (Crossref, plus OpenAlex abstract for Hsee & Zhang).