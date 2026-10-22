---
ai_contribution: 100
ai_generated_date: 2026-10-22
ai_modified: 2026-10-22 05:16:23+00:00
ai_system: claude-opus-5-5
author: Andy Southgate
concepts:
- '[[miswanting]]'
- '[[affective-forecasting-gap]]'
- '[[psychophysical-social-choice-problem]]'
- '[[negative-valence-asymmetry-and-the-selection-weighting-function]]'
created: 2026-10-22
date: &id001 2026-10-22
description: Cross-review synthesis of 2 outer reviews from 2026-10-22 (ChatGPT 5.6
  Sol Pro, Claude Fable 5.1) of miswanting. 7 verified convergent clusters, three
  P2→P1 upgrades, 4 convergences rejected.
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-22 05:16:23+00:00
modified: *id001
related_articles:
- '[[project]]'
- '[[outer-review-2026-10-22-chatgpt-5-6-sol-pro]]'
- '[[outer-review-2026-10-22-claude-fable-5-1]]'
synthesis_coverage: 2/3
synthesizes:
- reviews/outer-review-2026-10-22-chatgpt-5-6-sol-pro.md
- reviews/outer-review-2026-10-22-claude-fable-5-1.md
title: Outer Review Synthesis - 2026-10-22
topics:
- '[[valence-and-conscious-selection]]'
- '[[wanting-liking-and-the-value-in-mechanism-fork]]'
- '[[the-steelman-for-value-blind-selection]]'
- '[[inheritance-problem-for-the-psychophysical-law]]'
---

**Date**: 2026-10-22
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Subject**: "Audit miswanting" ([concepts/miswanting.md](/concepts/miswanting/), `fallback:recent-aged`; Claude reused ChatGPT's subject).
**Coverage**: 2 of 3 commissioned reviewers contributed.

- **ChatGPT 5.6 Sol Pro**: commissioned 02:10Z, collected 03:57Z, processed by 04:10Z. Its processing minted five tasks, one P1 and four P2.
- **Claude Fable 5.1** (Research, 224 sources, 10m 22s): commissioned 03:11Z, collected 04:24Z, processed by 04:35Z. Its processing minted nothing and annotated three of ChatGPT's tasks with cross-service corroboration.
- **Gemini 3.1 Pro Deep Research**: commissioned 04:13Z, **abandoned** at 05:07Z after two collect attempts. "Creating your report..." stayed byte-identical for more than 30 minutes after research had finished. `failure_reason` is null. This is the third consecutive Gemini abandonment (see Method Notes, operator item).

## TL;DR

Both reviewers independently find miswanting's two headline claims false as worded: that forecast-driven mischoice "rests on one unreplicated study", and that "no design measured felt anticipation at choice". Their evidence is disjoint. ChatGPT cites Dorison 2019, Schlösser 2013 and Young 2019. Claude cites Mellers 1999, Wilson 1993 and Shiv & Huber 2000. Neither reviewer uses a counterexample the other cites.

Both reviewers also leave the same narrow residue standing:

- Hsee and Zhang's Study 3 has no *independent* replication.
- No located design dissociates felt anticipation at choice from forecast content and learned value, and sets it against later experience.

The open P1 already rewrites the article to exactly that residue.

- **Clusters**: 7 convergent, each 2-of-2 and each verified on disk. There are also 4 rejected convergences and 4 divergences.
- **Tasks**: 3 upgraded P2→P1 and 1 P1 annotated (already at the ceiling). None were deduplicated, since no two tasks edit the same passage, and none were minted. One optional item became required: the rankings clause in the countermodel task.
- **Calibration**: no cluster moves [P-VS1](/positions/value-in-selection/#p-vs1). The newly cited measurements fit its candidate currency without evidencing it, and no task concedes that the feeling is idle.

## Convergent Findings

### 1. The exclusivity claims about forecast-driven mischoice (L3, L31, L37, L47 heading)

- **Flagged by**: chatgpt, claude
- **Verification**: clean on the core claim; each reviewer has detail corrections.
    - On disk at synthesis time, each at count 1:
        - L3 "forecast-driven mischoice rests on one unreplicated study";
        - L31 "The only reversal shown to be carried by a forecast, Hsee and Zhang's (2004) Study 3, has no independent replication on record";
        - L37 "Only Hsee and Zhang measured forecasts, choices and experiences together";
        - L47 "### Comparison Mode: The One Forecast-Driven Case".
    - ChatGPT's counterexample is Dorison, Minson & Rogers 2019 (*Cognition* 188), which the ChatGPT processing pass verified in full text. The reviewer under-reports the caveats. In Study 4 the treatment also moved reported experience, and Study 5 and the replication measured no forecasts. The reviewer's "34%" figure is disputed and must not be carried.
    - The Claude processing pass verified Claude's counterexamples:
        - Mellers & McGraw 2001 (full text) found laboratory predictions "quite accurate". The one design that measured forecasts, choices and experiences together therefore found no misranking.
        - Wilson et al. 1993 (abstract) is between-subjects, not "within-person" as the reviewer says, and it measured no forecast.
    - Both reviewers agree the narrow claim survives. Study 3 has no *independent* replication; Anvari et al. 2021 replicated Studies 1–2 only. The loose word is the description's bare "unreplicated". ChatGPT adds that Hsee & Zhang's own unpublished 2003 audiovisual replication exists, which is why "independent" matters.
- **Quotes**:
    - **ChatGPT 5.6 Sol Pro** (Overall assessment): "The claim that Hsee and Zhang’s Study 3 is the sole forecast-driven case is false under the ordinary meaning of “a forecast error changes choice.”"
    - **Claude Fable 5.1** (§2.3): "That directly falsifies the article’s sentence “Only Hsee and Zhang measured forecasts, choices and experiences together”". (Part 1): "Claim A (“forecast-driven mischoice rests on one unreplicated study”) holds only as a narrow claim about Hsee & Zhang 2004 Study 3, and the article’s own headline metadata overstates it."
- **Task action**: Recorded on the P1, which is already at the ceiling, so it was not upgraded. Its fields were rewritten to `Review files` and `Synthesis`, and a convergence prefix was added to Notes. Heading: "`concepts/miswanting` description, lede (L31), L37, L47 heading and L67 claim Hsee & Zhang is the only forecast-driven case …"

### 2. "No design measured felt anticipation at choice" (L3, L31, L67, and two dependent pages)

- **Flagged by**: chatgpt, claude
- **Verification**: clean on the scoping defect; Claude's evidence is partly discounted.
    - On disk, each at count 1:
        - L3 "no design measured felt anticipation at choice";
        - L31 "No study found for this article measured the felt anticipation present at choice";
        - L67 "No study found measured the felt state at choice alongside later experience".
    - Two dependent pages state the claim with no hedge:
        - `topics/inheritance-problem-for-the-psychophysical-law` L88: "No study has yet measured the felt anticipation present at choice";
        - `concepts/psychophysical-social-choice-problem` L40: "no study has yet measured the input it names, the felt anticipation present at choice".
    - ChatGPT's instances meet the article's own felt scope:
        - Schlösser et al. 2013, abstract verified, define immediate emotions as "the 'hot' visceral feelings people feel as they contemplate a specific decision option at the cusp of making a decision".
        - Young et al. 2019, full text, presented present-tense option probes "prior to participants' decision".
        - ChatGPT's Schlösser Study 4 details (108 participants, post-outcome emotion) come from a 2009 dissertation and are leads only.
    - Claude's instances do not meet that scope. Bechara 1997 (skin conductance) and Knutson 2007 (fMRI) are not felt-state reports, and the Claude processing pass rejected Claude's rival-favouring reading of them. Claude's share of this cluster therefore rests on its scoping verdict: the claim holds only on an unstated narrow reading, and the metadata drops the qualifier. That verdict is independent and lands on the same defect.
    - Both reviewers name the same surviving residue, and L83 already states it; the P1 keeps L83.
        - ChatGPT's version: a felt anticipatory misranking that causes the choice independently of learned value, beliefs and attention, and that later experience contradicts.
        - Claude's version: a concurrent introspective felt report, paired within-person with later experience.
    - Propagation sweep: fixed strings over live `obsidian/` and `archive/`, excluding `reviews/`, `workflow/` and `research/`. The positive control "felt anticipation present at choice" matched 3 files.
        - The two dependent pages and miswanting are the only live carriers.
        - The research note `research/miswanting-and-forecast-driven-mischoice-2026-10-12` also carries the claim in its description ("none measured the felt anticipation [P-VS1](/positions/value-in-selection/#p-vs1) names"). It is a dated record, so it is logged as a lead and not tasked.
- **Quotes**:
    - **ChatGPT 5.6 Sol Pro** (Overall assessment): "The claim that nobody measured felt anticipation at choice is false." (§2): "No located study cleanly demonstrates that a *misranked consciously felt anticipatory valence* causes a choice"
    - **Claude Fable 5.1** (§2.3): "So Claim B is **true only on a narrow phenomenological reading**: concurrent *introspective* report of *felt* anticipatory valence, within the choosing trial, paired within-person with later experience." Also: "its metadata (“no design measured felt anticipation at choice”) drops even the “alongside later experience” qualifier". (Part 1): "Until it is fixed, no other Map article should cite it as evidence."
- **Task action**:
    - The miswanting P1 was annotated, as in cluster 1.
    - The dependent-pages task was upgraded P2→P1. Heading: "Two pages repeat miswanting's absence claim, unscoped: …". Its suggested NEW wording ("dissociates … from forecast content and learned value") matches the shared residue, so it can safely land before or after the P1.

### 3. "No study manipulated a forecast … the forecast's causal role is everywhere inferred" (L37)

- **Flagged by**: chatgpt, claude
- **Verification**: clean on the core claim.
    - On disk, at count 1: "so the forecast's causal role is everywhere inferred."
    - ChatGPT cites Dorison: a randomised forecast-correcting treatment changed a real choice (Study 4, p = .028 on the forecast shift), though it also moved reported experience.
    - Claude cites two studies:
        - Wilson et al. 1993 randomised a pre-choice manipulation, reasons analysis, that changed a real poster choice and lowered satisfaction three weeks later.
        - Shiv & Huber 2000 evoked anticipated satisfaction and shifted choice, but had no experienced-outcome measure.
    - Both reviewers allow that a stricter claim may survive: no intervention isolated the forecast from beliefs, present affect and learned value. That is what the P1 asks the rewrite to say.
- **Quotes**:
    - **ChatGPT 5.6 Sol Pro** (§3): "Dorison and colleagues randomised forecast-correcting information and observed changed behavioural choices."
    - **Claude Fable 5.1** (§2.3): "The article’s claim that “No study manipulated a forecast while holding the other inputs fixed” survives only by defining “forecast” so narrowly that manipulating the *basis* of predicted liking does not count."
- **Task action**: The P1 was annotated; this is its defect 3. It was not upgraded, since it is already P1.

### 4. Gilbert–Wilson wanting is not "the reverse" of Berridge's (L29)

- **Flagged by**: chatgpt, claude
- **Verification**: clean.
    - On disk, at count 1: "the reverse of Berridge's incentive-salience "wanting", which can decouple from predictions of outcome value altogether."
    - The shared terminology map in `topics/wanting-liking-and-the-value-in-mechanism-fork` contains no "reverse"; the framing exists only on this page.
    - Both reviewers accept the substantive Berridge content, and Berridge 2023 (*TICS*, PMC full text) supports "can decouple". The defect is the word "reverse".
- **Quotes**:
    - **ChatGPT 5.6 Sol Pro** (§6): "Gilbert–Wilson wanting and Berridge “wanting” are therefore not reversals of one another."
    - **Claude Fable 5.1** (§2.4): "The two concepts are orthogonal, not inverse: incentive salience is not on the predicted-utility row at all."
- **Task action**: Upgraded P2→P1. This is item (3) of "`concepts/miswanting` misses the emotions-as-outcome countermodel (Davis, Love & Maddox 2009); L81 calls miswanting "the demonstrated cost" …; L29 calls Gilbert–Wilson wanting "the reverse" of Berridge's".

### 5. "Miswanting is the demonstrated cost of that driver" overstates (L81)

- **Flagged by**: chatgpt, claude
- **Verification**: clean.
    - On disk, at count 1: "miswanting is the demonstrated cost of that driver."
    - The article's own L67 says it "is unknown" whether the felt vehicle carried the misranking. L81 itself says the demonstrations "neither support nor undercut the claim that the feeling selects". Inside the conditional, then, the cost is one the driver *would inherit*.
    - This is the Tenet 3 calibration: fit without evidencing. The fix narrows a word and does not concede that the feeling is idle.
- **Quotes**:
    - **ChatGPT 5.6 Sol Pro** (§8): "That is a framework-internal implication, not a demonstrated cost of an empirically established driver."
    - **Claude Fable 5.1** (Part 3, the "Dualist payoff" row, on "miswanting as “the demonstrated cost” of a felt selector"): "*Compatible*, and no more."
- **Task action**: Upgraded P2→P1, as item (2) of the same countermodel task.

### 6. Forecasts wrong in level can still rank correctly (omitted)

- **Flagged by**: chatgpt, claude
- **Verification**: clean.
    - Miswanting has 0 hits for "relative accura". It defines miswanting by ranking (L29, "ranking the options differently"), but it never says that most documented forecast error is absolute and leaves rankings intact.
    - [affective-forecasting-gap](/concepts/affective-forecasting-gap/) L82 makes the argument ("a bias shared equally by every option leaves the ordering intact and bites only where it reverses ranks"). It cites Moeck et al. 2026 and Carlson et al. 2023, which the ChatGPT processing pass verified at abstract level, and it links back to miswanting.
    - The reviewers' sources are disjoint: ChatGPT uses Carlson and Moeck, Claude uses Mathieu & Gosling 2012. Mathieu & Gosling's figures are unchecked, so it is a lead only.
    - This is the least prompt-seeded convergence of the cycle; neither prompt mentions relative accuracy.
    - The point supports the article's own "rarely" thesis, so adding it strengthens the page and retracts nothing.
- **Quotes**:
    - **ChatGPT 5.6 Sol Pro** (§4): "a selector needs the correct ordering of options, not exact magnitude calibration". (§7 heading): "Forecasts can be wrong in magnitude but right for choice". (§4): "The neighbouring forecasting article already recognises this point, but the miswanting article does not import it."
    - **Claude Fable 5.1** (§2.3): "A forecast can be wrong in level yet still *rank* options correctly, and ranking is all that choice needs." (§2.7): "The miswanting article inherits none of that caution."
- **Task action**: The ChatGPT pass never tasked this point, and the Claude processing pass folded it in as OPTIONAL item (6) of the countermodel task. It is now **REQUIRED**: about +15 words, linking the gap page, with no new citation. It is upgraded P2→P1 along with its task.

### 7. Absence and exclusivity claims need a stated criterion and a search that licenses them (methodology)

- **Flagged by**: chatgpt, claude
- **Verification**: clean.
    - [project/writing-style.md](/project/writing-style/) has 0 hits for "no study|exhaustive|absence claim|exclusivity", against a positive-control term with 8 hits. The rule is absent.
    - The failure path is on record:
        - The research note's queries were author/title lookups.
        - Its Gaps section said the absence "was not specifically searched".
        - The description stated the absence anyway.
        - Two pages then restated it without the hedge.
- **Quotes**:
    - **ChatGPT 5.6 Sol Pro** (improvement 23): "Use “No study meeting criterion X was located in searches Y and Z as of [date]” rather than “no study measured” or “the only case.”"
    - **Claude Fable 5.1** (Part 5): "Any “only”, “no study” or “single study” sentence must state its inclusion criterion inline, and the metadata must carry the same qualifier." Also: "run a “known controversy” query (meta-analyses, artifact critiques, replications) before drafting"
- **Task action**: Upgraded P2→P1: "Writing-style guide has no rule for literature absence and exclusivity claims; …". This is not an operator-reserved ratification. AI refine-drafts have added rules to this file before: a5d33abc36 on 2026-10-06, itself a ChatGPT+Claude methodology convergence, and 24dc713806 on 2026-10-07.

### Rejected convergences

Both reviewers raised each of these, and both processing passes rejected them. The Claude pass read the ChatGPT pass first, so the two rejections are not independent. Each was therefore re-adjudicated here against disk.

- **R1. Reference 1 "conflates editions" (DOI mismatch).** Rejected as correlated error.
    - ChatGPT (§5): "but attaches the DOI belonging to Chapter 30 of *The Construction of Preference*". Claude (§2.2): "It does not resolve to the 2000 Forgas original whose pages are cited."
    - On disk, ref 1 gives the 2000 Forgas chapter (pp. 178–197), then "Reprinted in … (2006, pp. 550–564)", then the reprint's DOI. The 2000 chapter has no Crossref DOI; the ChatGPT pass ran three queries. The quoted pp. 182–184 fall in the 2000 range. Both reviewers' tools resolved the DOI to the 2006 reprint and inferred a mismatch the reference does not contain.
- **R2. The No-Many-Worlds paragraph is extraneous.** Rejected.
    - ChatGPT (§8 heading): "The Many-Worlds passage is extraneous and overcompressed". Claude (§2.5): "The paragraph exists because the template demands a tenet section, not because the subject warrants one."
    - Relation to Site Perspective is mandatory. The paragraph scopes its claim to the Map's selection question ("asking which valence selects has a referent only if one outcome is really selected"). It grants the Everettian relativisation and says the objection is "not anything this literature supplies". The 2026-10-15 deep review's Stability Notes mark it as bedrock.
    - Residual lead, not tasked: both reviewers read the opening "Miswanting presupposes a forgone option" as a claim about the psychological phenomenon. Two independent misreadings of one sentence are weak evidence of a clarity problem in that clause. It is worth a look if a future pass is already editing L85.
- **R3. Revealed preference (the welfare standard) is left unexamined.** Rejected.
    - ChatGPT (§7): "The article acknowledges revealed preference but leaves the objection unexamined." Claude (§2.4): "that objection is threshold, not peripheral".
    - L69 already makes every reversal relative to a named standard: total utility, immediate happiness ratings, liking days later. L45 grants that the colonoscopy shift is desirable by a health standard. The article therefore claims hedonic rank reversal against a stated standard, not all-things-considered welfare loss. ChatGPT itself puts Hsee and Zhang at "something close to" hedonic rank reversal, not welfare loss. The Stability Notes record the scope decision.
- **R4. Calibration asymmetry ("no confidence update"; a symmetric-bar rule).** Rejected.
    - ChatGPT (§8): "Tenet 5 may reject a simplistic “fewer entities always wins” rule, but it does not license assigning the mechanistic account no evidential advantage." Claude (§2.5): "The rival’s evidence is graded on a scale that nothing passes; the Map’s own commitment is not graded at all."
    - L81 grades [P-VS1](/positions/value-in-selection/#p-vs1) explicitly: it is held "on prior commitments at low credence". L83 credits the rival with "a genuine parsimony advantage". Non-discriminating evidence licenses leaving a coarse band unchanged, and ChatGPT reaches the same verdict in §9. Claude's case for lowering the band rests on its disputed Knutson/Bechara reading (see D1).
    - Two related points survive only as prospective cautions, and both are already in tasks:
        - ChatGPT's asymmetric-standard point is in the P1, which reads: Do NOT set aside present-tense reports of one's own feeling as "cool judgements".
        - Claude's point on L77, "Misattribution describes a cost [P-VS1](/positions/value-in-selection/#p-vs1) accepts rather than evidence against it", is item (5) of the countermodel task, which asks for a stated defeater.

## Singleton Findings

These were not upgraded, except where they share a task with a convergent cluster (noted).

- **ChatGPT 5.6 Sol Pro**:
    - The emotions-as-outcome countermodel (Davis, Love & Maddox 2009). It is item (1) of the countermodel task and rides in that task's P2→P1 upgrade. The ChatGPT pass recorded its limits: it contrasts stimulus risk with response, not value, and measures skin conductance, not felt valence.
    - If post-outcome self-report counts as experienced valence, present-tense self-report must count as evidence of anticipatory valence. This is carried into the P1 as a prospective caution.
    - Add Schlösser, Young and Dorison to the affective-forecasting gap page. Task: "`concepts/affective-forecasting-gap` has no measured instance of its own candidate currency …" (**P2, unchanged**; length-neutral at 3,615/3,500). Claude asked for the gap page to be audited for the same absence claims (its item 14). The synthesis audit found none ("no study" has 0 hits on the page), so there is no convergence here.
    - Rejected by the ChatGPT pass (reasons in its Verification Notes):
        - Gilbert–Wilson "experienced utility" is a translation;
        - the opening is in tension with Gilbert and Wilson's hybrid model;
        - "predicts" should be "accommodates";
        - add a measurement-reactivity subsection;
        - build an evidence ladder and an evidence matrix;
        - make adversarial review mandatory;
        - revise the valence-and-conscious-selection and negative-valence pages.
    - Leads only, unchecked: Issa et al. 2026 (PubMed 42330892); the 2025 White Rose longitudinal health-behaviour study.
- **Claude Fable 5.1**:
    - L73's "the one place in this literature" is false (Loewenstein et al. 2001, risk-as-feelings). Folded into the P1 as defect (f).
    - No Berridge source is cited, and L77's hunger claim is unattributed (Berridge 2023, PMC full text). Item (4) of the countermodel task.
    - As worded, L77's "a cost [P-VS1](/positions/value-in-selection/#p-vs1) accepts" lets no misattribution result count against [P-VS1](/positions/value-in-selection/#p-vs1). Item (5) of the countermodel task, as a stated defeater.
    - Rejected by the Claude pass:
        - the PP/active-inference "blocking gate", and calling the L83 experiment "ill-posed";
        - "Before Distortion" undercutting Claim B;
        - memory routes as a "scope slip";
        - focalism and the impact bias missing (both are covered in the gap page, L34–38);
        - co-optation of "gut reactions";
        - collapsing the [P-VS1](/positions/value-in-selection/#p-vs1) badges (they render site-wide);
        - cutting the loss-aversion section to a link;
        - linking valence to miswanting and adding Laukkonen there;
        - lowering [P-VS1](/positions/value-in-selection/#p-vs1) (see D1);
        - optional tenet sections, auto-tasking confessions, and an apex ladder.
    - Leads only:
        - Mathieu & Gosling 2012 (figures unchecked);
        - Charpentier et al.'s "predicted choice better than existing value-based models";
        - Bechara et al. 1997, whose rebuttal by Maia & McClelland 2004 the corpus already carries in `concepts/somatic-interface`.

## Divergences

- **D1. ChatGPT vs Claude on [P-VS1](/positions/value-in-selection/#p-vs1)'s confidence band.**
    - ChatGPT (§9): "The correction should therefore change the Map’s account of the existing experiments, but not upgrade [P-VS1](/positions/value-in-selection/#p-vs1)." Claude (Part 3): "On the evidence, the band should arguably *drop*".
    - The live text sides with holding the band. Claude's reason is that neural predictors outperform self-report (Knutson 2007). But Knutson's own abstract reads those signals as "circuits related to anticipatory affect" that precede and support purchases. That does not show choice running without the felt state, so it does not move a felt-currency position either way.
    - Under the Tenet 3 calibration, the evidence fits without evidencing, and epiphenomenalism is never conceded. No task changes the band.
- **D2. ChatGPT vs Claude on whether the rival "predicts" the reversals.**
    - ChatGPT (improvement 16): "Reserve “predicts” for a model that supplies direction, boundary conditions and quantitative effects before observing the data." Claude's active-inference reading, by contrast, "predicts every reversal the article catalogues;".
    - L65's "predicts" stands. The routes (evaluability, peak-end) are prior, independently motivated mechanisms. The Stability Notes record the rival's predicting every reversal as the article's thesis. The non-discrimination verdict is the same under either verb.
- **D3. ChatGPT vs Claude on Gilbert and Wilson's "gut reactions".**
    - ChatGPT says the opening under-reads the affective ingredient: "But their own model is hybrid: imagery, beliefs and present affect all contribute." Claude says L73 and L77 over-read it: "Gilbert and Wilson treat such feelings as information in a fully naturalistic model; nothing in their account makes “felt” a non-physical selection currency."
    - The two charges pull in opposite directions, and the page sits between them. The opening places their wanting on the predicted-utility row. The shared terminology map's "Felt as such?" cell covers the mixed case. L77 labels the felt-currency reading "The Map reads …", not as theirs.
    - Only the exclusivity half of Claude's charge was accepted (L73's "the one place"), and it is in the P1.
- **D4. ChatGPT vs Claude on the loss-aversion section.**
    - ChatGPT would widen it: "The current literature therefore does not support a simple Kermer-versus-Charpentier fork". Claude would cut it: "Cut miswanting’s “Loss Aversion” section to two sentences and a link."
    - Both processing passes declined both prescriptions. The section answers a question specific to this page: whether loss aversion is miswanting at all. The weighting page already runs a six-row account, and length does not constrain the choice (2,346/3,500). No task.

## Headroom Check

`analyze_length` at synthesis time; the gate is `>=`, and headroom is hard − 1 − count.

| File | Now | Hard | Open edits (budgets from task notes) | After |
|---|---|---|---|---|
| concepts/miswanting | 2,346 | 3,500 | P1 ≈ +320; countermodel ≈ +170 | ≈ 2,836 (≈ 663 left) |
| topics/inheritance-problem-for-the-psychophysical-law | 3,400 | 4,000 | ≈ +5 | ≈ 3,405 |
| concepts/psychophysical-social-choice-problem | 2,937 | 3,500 | ≈ +5 | ≈ 2,942 |
| concepts/affective-forecasting-gap | 3,615 | 3,500 | net ≤ 0 (P2, unchanged) | ≤ 3,615 |
| project/writing-style | 9,808 | 3,500 (already critical) | ≤ +120 | ≤ 9,928 |

## Method Notes

- **Gemini has now been abandoned three nights running (operator item).**
    - On 2026-10-20 (full-site audit), 2026-10-21 (`concepts/intrinsic-nature`) and 2026-10-22 (this subject), the Gemini leg ended `status: abandoned` with `failure_reason: null` in `pending-reviews.yaml`.
    - The stall stage moved. On 10-20 and 10-21, Deep Research sat at "Starting research..." with no sources for about 56 and 42 minutes. Tonight research finished, and the run stalled at "Creating your report...". The report-generation stage did not complete.
    - Because the failure reason is null, the pattern is invisible to anything that reads the ledger rather than the changelog. The collector should record a reason string when it abandons a run (e.g. "start stall" or "report-generation stall").
    - Gemini's absence is recorded as absence, not dissent.
- **Prompt seeding.** Both prompts named the two headline claims, the Gilbert–Wilson and Berridge readings, and "bracketing", so clusters 1–5 were seeded at the topic level. Their weight lies in the evidence, and the two counterexample sets are disjoint:
    - ChatGPT: Dorison, Ellis 2018, Schlösser, Young, Asutay, Grimani, Davis.
    - Claude: Mellers, Wilson 1993, Shiv & Huber, Loewenstein, Bechara, Knutson, Berridge 2023.
    - Cluster 6 was not prompted. Cluster 7 answers both prompts' generic request for methodology improvements.
- **Independence.** Claude was commissioned at 03:11Z and its research ran 10m 22s. The ChatGPT reply was collected at 03:57Z and committed at 04:10Z, so the Claude reviewer cannot have seen ChatGPT's findings. The two processing passes are not independent, which is why R1–R4 were re-adjudicated here.
- **Claude's standing frame.** Claude's verdict vocabulary does not appear in its commission prompt. That includes "REVISE-HARD", "gate-blocked", the "Laukkonen–Friston–Chandaria 2025 blocking gate", "DEMOTE-TO-COHERENCE-ONLY" and "co-optation firewall". The vocabulary comes from the claude.ai project's standing instructions. The PP-gate failure is therefore a structural demand of that frame, not an independent discovery. It was rejected on the merits: the article names and engages the strongest physicalist rival, and the steelman page engages active inference.
- **Prior art.** The 2026-10-15 deep review's Stability Notes already settle R2, R3 and D2: the rival predicts every reversal, revealed preference is deliberately out of scope, and Many-Worlds is bedrock. Both reviewers re-raised these points anyway, which is expected of reviewers who never see Stability Notes.
- **What the corrected reviews agree on.** Miswanting's central methodological claim survives: forecast error alone is not evidence of a changed choice, and neither establishes that felt anticipation did the selecting. Its literature verdicts overreach, and the open tasks narrow them. The four upgraded or annotated tasks run in file order (L2912, L2921, L2930, L2947). The miswanting edits leave about 663 words of headroom.
- **Leads, not tasked**: the research note's description (cluster 2); the L85 "forgone option" clause (R2); Mathieu & Gosling 2012; Issa et al. 2026; the details of Schlösser's dissertation Study 4.