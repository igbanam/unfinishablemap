---
ai_contribution: 100
ai_generated_date: 2026-10-14
ai_modified: 2026-10-14 06:26:18+00:00
ai_system: claude-opus-5-5
author: Andy Southgate
concepts:
- '[[self-model-theory-of-subjectivity]]'
- '[[theory-of-mind]]'
- '[[illusionism]]'
- '[[multiple-drafts-model]]'
- '[[phenomenal-transparency-opacity-spectrum]]'
created: 2026-10-14
date: &id001 2026-10-14
description: Cross-review synthesis of 2 outer reviews from 2026-10-14 (Claude Fable
  5.1, ChatGPT 5.6 Sol Pro) of the self-construction apex. 14 convergent clusters;
  three P2→P1 upgrades.
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-14 06:26:18+00:00
modified: *id001
related_articles:
- '[[project]]'
synthesis_coverage: 2/3
synthesizes:
- reviews/outer-review-2026-10-14-claude-fable-5-1.md
- reviews/outer-review-2026-10-14-chatgpt-5-6-sol-pro.md
title: Outer Review Synthesis - 2026-10-14
topics:
- '[[self-construction-constructor]]'
- '[[social-construction-of-self-vs-phenomenal-self]]'
- '[[the-self-minimal-narrative-and-substantial]]'
---

**Date**: 2026-10-14
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: 2 of 3 scheduled reviewers contributed: Claude Fable 5.1 and ChatGPT 5.6 Sol Pro. **Gemini is absent for the second day running.** On 2026-10-13 its entry was abandoned. Today's 04:52Z commission failed before the research-plan stage with a soft refusal, so `pending-reviews.yaml` has no Gemini entry for this date. Every scored cluster is therefore 2-of-2. No third reviewer was available to dissent, and none is implied.

**Subject**: [self-construction-constructor](/apex/self-construction-constructor/), "The Self Is Constructed; the Constructor Is Not" (`subject_type: recent`, `fallback:recent-aged`). ChatGPT was commissioned at 04:07Z. Claude reused the subject at 04:20Z under the hostile-referee template.

**Prompt overlap.** Both prompts named self-model theory, the narrative-centre-of-gravity account, predictive-processing selfhood, illusionist replies, question-begging, bracketing objections to protect the tenets, citation fidelity, and integration with the SMT, IEM and Kant pages. So agreement on clusters 1, 3, 4, 9–11 was partly invited, and the weight there rests on on-disk verification of specific loci rather than on the count. Only Claude's prompt asked whether the argument "conflates a functional constructor with a phenomenal one"; ChatGPT reached cluster 2 unprompted, as its thin/thick dilemma. Clusters 5 and 13 were invited only in part. The prompts asked for "the strongest replies", which does not name either no-regress rival. They also asked about integration with the SMT page, which covers instance 1 of cluster 13 but not instances 2–5. Neither prompt asked about clusters 6–8, 12 or 14.

**Article state at synthesis.** The live file is unchanged since `6e640ad89e` (apex-evolve, 2026-10-07), the text both processing passes line-numbered. `analyze_length` gives 4,146 words against a hard limit of 5,000 with a `>=` gate, so 853 words of headroom. That is shared by four apex tasks, all now P1 (see Method Notes).

## TL;DR

Working independently, the two reviewers reached the same verdict. The constructor argument holds as a conditional on Tenet 1, but the title, opening, Synthesis and tenet sections assert it unconditionally, while the article's own Evidence and Dependency section concedes the condition. **Fourteen convergent clusters survived adjudication against the live apex.** None was rejected outright; two carry a disputed half that was not counted.

- **Tasks upgraded**: 3, all P2→P1 (the Threshold task, apex citation fidelity, and Schachter–Singer at source).
- **Not escalated**: the two existing P1s were rewritten but not escalated to P0.
- **Deduplicated**: none. ChatGPT minted one new task and carried its other points as riders on Claude's tasks, so there were no sibling duplicates.
- **NEEDS-HUMAN**: two items went into one picker-invisible entry. Both reviewers asked for a retitle (cluster 14). Both independently proposed a status-propagation gate (cluster 13), and this one apex has five verified instances of the pattern.

## Convergent Findings

### 1. The headline asserts what the evidence ledger concedes is a Tenet-1 conditional
- **Flagged by**: claude, chatgpt
- **Verification**: Clean.
  - The concessions are at L134 ("inherited from Tenet 1") and L138 ("mutually coherent only").
  - The unconditional statements: L51 "a line the constructionist accounts cannot cross"; L87 "stands outside the series"; L101 "close to forced"; L105 "The four registers establish"; L130 "cannot be the output of building"; L138 "This line is independently argued"; L148 "The regress shows…"; and the frontmatter `description`.
  - `git log -S` shows that the Tenet-1 disclosure and "independently argued" entered in the same pass (`d3c0cc056c`, apex-evolve 2026-07-26). The concession and the overclaim were installed together.
- **Quotes**:
  - **Claude Fable 5.1**: "The concession is logged. It is not converted into a status change."
  - **ChatGPT 5.6 Sol Pro**: "That disclosure is a major strength. The problem is that the rest of the article repeatedly resumes the language of demonstration"
- **Task action**: Rewritten without a priority change, because it is already P1, the skill's ceiling. The task is "`apex/self-construction-constructor` — the constructor inference outranks its own sources…", items (4) and rider (b).

### 2. The constructor premise slides from a functional operator to a phenomenal subject
- **Flagged by**: claude, chatgpt
- **Verification**: Clean. L99 reads "operations require an operator and a field in which they operate"; every rival grants a functional operator. L128 reads "The brain builds the structure. Consciousness undergoes it." So on the apex's own account the "constructor" undergoes the building rather than doing it (ChatGPT §1.4).
- **Quotes**:
  - **Claude Fable 5.1**: "The step from *constructing system* to *experiencing subject* is never argued."
  - **ChatGPT 5.6 Sol Pro**: "The argument moves from the relatively neutral thin claim to the thick bearer claim without an independent bridge."
- **Task action**: Same P1 calibration task, item (2) and rider (c). Rewritten, no priority change.

### 3. The "no one who is fooled" dilemma runs on a premise the same paragraph concedes the rival denies
- **Flagged by**: claude, chatgpt
- **Verification**: Clean.
  - L95 carries both "illusions require a subject to be deceived", present since the apex was created (`64daae2590`), and the concession "a premise illusionists deny rather than overlook".
  - The concession was added by `806facb968` (refine, 2026-08-12), whose commit title reads "close the illusionist-regress family". That repair appended a concession and left in place the argument it concedes.
  - The [self-model-theory-of-subjectivity](/concepts/self-model-theory-of-subjectivity/) page contains no such dilemma (`fooled` = 0). Its verdict is "a located disagreement, not a refutation".
- **Quotes**:
  - **Claude Fable 5.1**: "SMT does not posit a "no one" who is fooled."
  - **ChatGPT 5.6 Sol Pro**: "once the denial is acknowledged, the “someone must be fooled” argument cannot continue to function as a reductio."
- **Task action**: P1 calibration item (3), and item (c) of the P1 rival-engagement task. Both rewritten, no priority change.

### 4. The strongest constructionist rivals are absent from the apex
- **Flagged by**: claude, chatgpt
- **Verification**: Clean.
  - The apex has 0 hits each for `Dennett`, `Frankish`, `Laukkonen`, `Kriegel` and `same-order`.
  - Neither [multiple-drafts-model](/concepts/multiple-drafts-model/) nor [interpreter-module-narrative-construction-unity](/concepts/interpreter-module-narrative-construction-unity/) is among its sources.
  - The corpus already engages all of them, for example [multiple-drafts-model](/concepts/multiple-drafts-model/) L69 and [witness-consciousness](/concepts/witness-consciousness/) L119, so the fix is reuse, not research.
- **Quotes**:
  - **Claude Fable 5.1**: "Dennett's narrative centre of gravity, the gap the brief names as (b), is **unanswered** in the apex."
  - **ChatGPT 5.6 Sol Pro**: "The omission allows the apex to present a framework-boundary objection as though Dennett had failed to notice the need for an audience."
- **Task action**: Rewritten, no priority change (already P1): "`apex/self-construction-constructor` — the thesis that the constructor "cannot be the output of building" never meets the accounts that claim to build it…".

### 5. The regress is not compulsory, and the apex never states the rival that escapes it
- **Flagged by**: claude, chatgpt
- **Verification**: Clean. The two reviewers name different rivals but make the same structural charge, and both rivals are real.
  - Claude names self-organising loops: Metzinger's PSM, strange loops, Friston's self-evidencing, and Laukkonen et al.'s beautiful loop.
  - ChatGPT names same-order self-representation (Kriegel). The Map has already assessed Kriegel at [self-representational-theory-of-consciousness](/concepts/self-representational-theory-of-consciousness/) L79: "not an unanswerable regress but an answer that costs him the representational thesis".
- **Quotes**:
  - **Claude Fable 5.1**: ""Construction requires an unconstructed constructor" is asserted, not shown."
  - **ChatGPT 5.6 Sol Pro**: "That theory may face other objections, but it blocks the article’s regress and cannot be answered by merely adding another representational level."
- **Task action**: P1 rival-engagement task, rider (b). Rewritten, no priority change.

### 6. The four registers apply one premise four times, so they are not independent evidence
- **Flagged by**: claude, chatgpt
- **Verification**: Clean. L53 and L142 call the domains "independent", and L126 calls them "one problem in four costumes". L53 already disclaims confirmation; the defect is the word "independent".
- **Quotes**:
  - **Claude Fable 5.1**: "It is one premise, not four pieces of evidence."
  - **ChatGPT 5.6 Sol Pro**: "Repeating one controversial premise across perception, social identity, narrative cognition and transparency does not generate four independent reasons for that premise."
- **Task action**: P1 calibration item (4). Rewritten, no priority change. The methodology version (Claude Part 5 item 5, ChatGPT item 24) is already ChatGPT's item (4) in the standing 2026-07-25 methodology-ratification entry, so no new entry was made.

### 7. Data and thought experiments the rival also accommodates are credited to dualism
- **Flagged by**: claude, chatgpt
- **Verification**: Clean.
  - L85 (opacity): Claude's objection is to "what dualism predicts and what pure functionalism struggles to accommodate", since SMT predicts the datum too. ChatGPT's is to "invariant under a transformation that alters everything else", which outranks its source's "this suggests" ([phenomenal-transparency-opacity-spectrum](/concepts/phenomenal-transparency-opacity-spectrum/) L117).
  - L79 (inverted qualia) and L81 (zombie community): both reviewers class these as conceivability arguments that presuppose phenomenal realism.
  - Prior decision: [reviews/optimistic-2026-08-20-agency-self-wing.md](/reviews/optimistic-2026-08-20-agency-self-wing/) L65 declined to hedge L85 on evidential-tier grounds. Today's ground is different (the rival predicts the datum), and the P1 records the distinction.
  - **Not counted**: ChatGPT's claim that blur and the painter's squint are not opacity in Metzinger's technical sense. The apex reports its source faithfully (transparency page L85, L91), and the point is a live dispute in the literature, not an apex error.
- **Quotes**:
  - **Claude Fable 5.1**: "This is calibration asymmetry: the datum is credited to dualism while the rival's prediction of it is ignored." / "The inverted-qualia and zombie-community appeals add nothing independent: both are conceivability arguments that presuppose phenomenal realism."
  - **ChatGPT 5.6 Sol Pro**: "The statement that what-it-is-likeness remains “invariant” while “everything else” about functional role changes is unsupported and implausibly strong." / "The claim that two systems could have identical functions and cortical representations while yellow feels different is a disputed modal premise, not an empirical result."
- **Task action**: P1 calibration item (5) and riders (a), (d), (e). Rewritten, no priority change.

### 8. The theory-of-mind threshold is tiered above its source and above the tenets page
- **Flagged by**: chatgpt, claude
- **Verification**: Clean.
  - L107 reads "falls precisely here, and it tracks the consciousness-dependent capacity for metarepresentation". The source, [theory-of-mind](/concepts/theory-of-mind/) L75, says "the human-ape gap does not straightforwardly track consciousness".
  - [tenets](/tenets/) L97 and [bidirectional-interaction](/concepts/bidirectional-interaction/) L113 already cite Schleihauf et al. 2025 (*Science* 390(6772):521–526, Crossref-verified) and conclude "graded rather than absolute".
  - **A verifier finding that neither reviewer raised**: L134's ledger says the causal-participant gloss is "flagged in-text as unestablished". Only the quantum gloss (L113) is flagged; L111's causal clauses are not.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "The apex nevertheless says that the systematic human–ape gap falls “precisely” at metarepresentation and tracks consciousness. That is not established."
  - **Claude Fable 5.1**: "The theory-of-mind section imports Tenet 3 ("once present, it does causal work")". Part 3 row 10 gives DEMOTE-TO-COHERENCE-ONLY.
- **Task action**: **Upgraded P2 → P1**: "`apex/self-construction-constructor` §The Threshold — the apex says the human–ape gap "falls precisely"…". Claude's row 10 was never minted, so this is the only task for the cluster. Nothing to deduplicate.

### 9. Schachter–Singer is cited as "classic" with no replication history
- **Flagged by**: claude, chatgpt
- **Verification**: Clean. The loci are apex L67 and [social-construction-of-self-vs-phenomenal-self](/topics/social-construction-of-self-vs-phenomenal-self/) L77.
  - Claude's references: Marshall & Zimbardo 1979 and Maslach 1979, *JPSP* 37(6), both Crossref-verified.
  - ChatGPT's reference: Reisenzein 1983, *Psych. Bull.* 94(2):239–264, checked against Crossref and the OpenAlex abstract.
  - Both reviewers name the social-construction page as the place to fix it at source.
- **Quotes**:
  - **Claude Fable 5.1**: "Using it as "classic" evidence overstates it."
  - **ChatGPT 5.6 Sol Pro**: "The intellectual lineage is real, but the original experiment cannot bear the empirical weight assigned to it."
- **Task action**: Two tasks **upgraded P2 → P1**: "`apex/self-construction-constructor` — citation fidelity…" and "`topics/social-construction-of-self-vs-phenomenal-self` L77 — Schachter and Singer's "classic emotion experiments"…". They target different files, so neither is redundant.

### 10. Rochat's neonatal self-discrimination is upgraded to "phenomenal selfhood"
- **Flagged by**: claude, chatgpt
- **Verification**: Clean on the claim; ChatGPT's supporting evidence is disputed and not counted.
  - Apex L81 reads "signs of phenomenal selfhood". The source, [social-construction-of-self-vs-phenomenal-self](/topics/social-construction-of-self-vs-phenomenal-self/) L65, reads "pre-social self-specification" and adds that this "does not by itself establish an irreducible phenomenal subject".
  - ChatGPT's "The cited observational study followed only four infants" refers to DiMercurio et al. 2018 (PMID 30619012). The Map does not cite that paper, and the task forbids importing it.
- **Quotes**:
  - **Claude Fable 5.1**: ""Phenomenal selfhood" is the Map's gloss and should be labelled as such."
  - **ChatGPT 5.6 Sol Pro**: "It does not establish “phenomenal selfhood,” an irreducible experiential subject, or the absence of constitutive social influence."
- **Task action**: Same task as cluster 9's apex half (citation fidelity, item 1), upgraded P2 → P1.

### 11. Kant and IEM are handled correctly where they appear but not carried through the argument
- **Flagged by**: claude, chatgpt
- **Verification**: Partly disputed. Both reviewers single out the IEM step as the apex's most careful passage, and both find the Paralogisms caveat confined to one paragraph. Claude goes further and says the minimal claim itself runs the Paralogism. That is only partly right: read formally, the minimal claim is the unity of apperception, which Kant grants. The charge bites only on the phenomenal reading, so it folds into cluster 2.
- **Quotes**:
  - **Claude Fable 5.1**: "The apex uses the Paralogisms to disown the *strong* inference and then runs the same pattern for the *minimal* one."
  - **ChatGPT 5.6 Sol Pro**: "The apex cites these results but does not fully obey them."
- **Task action**: P1 calibration items (2) and (4). Rewritten, no priority change. Neither reviewer's request for edits to the Kant or IEM pages was minted: Wiseman 2019 and the A/B pagination are already present on those pages.

### 12. The apex has no reference list
- **Flagged by**: claude, chatgpt
- **Verification**: Clean. `## References` returns 0, and `git log -S` shows the apex never had one; 32 of 43 apex articles do. Claude made it an article-level fix (Part 4 item 11) and a methodology item (Part 5 item 6). ChatGPT made it a methodology item only (item 20).
- **Quotes**:
  - **Claude Fable 5.1**: "The apex has no reference list."
  - **ChatGPT 5.6 Sol Pro**: "Links to internal source pages are not enough when the apex strengthens or compresses their conclusions."
- **Task action**: The article half is item (4) of the citation-fidelity task, upgraded P2 → P1 under cluster 9. The methodology half goes to the NEEDS-HUMAN entry, decision (B).

### 13. The apex outranks its own source pages
- **Flagged by**: claude, chatgpt
- **Verification**: Clean on all five instances. Each source wording was grepped verbatim, and each installing commit was found with `git log -S`.

  | # | Apex | Source | Source calibrated | Flagged by |
  |---|---|---|---|---|
  | 1 | L95 "cannot escape by iterating" | SMT L55–59 "not a proof against it" / "a located disagreement, not a refutation" | `92a0f69ec5` 2026-07-11 | both |
  | 2 | L81 "signs of phenomenal selfhood" | social-construction L65 "pre-social self-specification" | `4124ed6fdb` 2026-07-06 | both |
  | 3 | L81 "runs strictly one way" | social-construction L91 "does not resolve this dispute neutrally" | `c25d0e8f64` 2026-02-16 | chatgpt |
  | 4 | L107 "falls precisely here" | theory-of-mind L75 "does not straightforwardly track consciousness" | `ad3400205f` 2026-08-04 | chatgpt |
  | 5 | L85 "alters everything else" | transparency L117 "this suggests" | `dab0d2bd3f` 2026-04-13 | chatgpt |

  All five apex phrasings date from the apex's creation, `64daae2590` (2026-05-27). That gives two failure shapes.
  - **Write-side** (instances 3 and 5): the source was calibrated before the apex was written, and the apex amplified at authoring time.
  - **Change-side** (instances 1, 2 and 4): the source was calibrated after the apex existed, and the calibration never propagated. It then survived four later passes on the apex: apex-evolve on 07-26 and 10-07, and refine-draft on 08-12 and 08-17.
- **Quotes**:
  - **Claude Fable 5.1**: "That is a status-propagation failure: the parent apex outranks its child's verdict without new argument."
  - **ChatGPT 5.6 Sol Pro**: "This is a clear case of **apex amplification**."
- **Task action**: Recorded only. The article-level fixes are already spread across the four apex P1s: (1) in the calibration task, (2) in citation fidelity, (3) and (5) in the calibration rider, (4) in the Threshold task. The proposed rule (Claude Part 5 item 1 = ChatGPT item 21) goes to the NEEDS-HUMAN entry, decision (B), and is not actioned.

### 14. The title states the conclusion unconditionally
- **Flagged by**: claude, chatgpt
- **Verification**: Clean. The title is "The Self Is Constructed; the Constructor Is Not", and L134 concedes the Tenet-1 dependence. Both processing passes fenced the title, so the P1 conditionalises only the opening and the `description`.
- **Quotes**:
  - **Claude Fable 5.1**: "Retitle to "The Self Is Constructed; Is the Constructor?""
  - **ChatGPT 5.6 Sol Pro**: "The current categorical title exceeds the admitted evidential status."
- **Task action**: Recorded in the NEEDS-HUMAN entry, decision (A). Title and URL are operator territory.

## Singleton Findings

Each finding below was flagged by only one reviewer. None was upgraded; each stays at its original task priority, or has no task.

- **Claude Fable 5.1**:
  - Mead clause (L81) reads as attribution. Partly disputed: the apex makes the Map's claim about Mead's concept. → Item (3) of the citation-fidelity task, now P1 under clusters 9 and 10.
  - Duch rebuttal assumes ownership-tagging must be phenomenal (row 14). → P1 calibration item (2).
  - "exactly what the construction/constructor distinction predicts" for the DMN/mindreading overlap (row 12, L109). → P1 calibration item (5).
  - `topics/the-self-minimal-narrative-and-substantial` L129, "a mere construction… should be observable", ignores transparency. → Unchanged at P2: "`topics/the-self-minimal-narrative-and-substantial` L129 — …".
  - The No-Many-Worlds paragraph (L146) asserts the constructor's haecceity without the Mādhyamaka caveat from [self-and-self-consciousness](/concepts/self-and-self-consciousness/) (row 15). → Not minted by the processing pass and not in any task; recorded here only.
  - Zahavi/Gallagher co-optation through the substantial-self routing. Weak: the apex keeps the minimal and strong claims apart. → Check-first item (3) of the L129 topic task.
  - Methodology items 2, 3, 4 and 7. Item 2 (confession-to-label conversion) repeats a completed methodology entry. Item 3 (mandatory rival roster) overlaps the opponent-parity entry. Item 4 (functional/phenomenal marking) and item 7 (same-family review risk) are recorded without action.
  - Rejected by the processing pass, with reasons in the review's Verification Notes: the changelog-staleness claim (see Divergences); Wiseman 2019 on the IEM page (already present); Kant A/B pagination (already present); edits to [self-and-self-consciousness](/concepts/self-and-self-consciousness/) (2 words of headroom).
- **ChatGPT 5.6 Sol Pro**:
  - Enactivism grouped with predictive processing as content-for-a-recipient (L79). → P1 rival-engagement rider (c).
  - The witness-awareness clause (L83) treats a contested report as detection, against Metzinger's tonic-alertness model. → Rider (d).
  - Letheby's empirical-equivalence concession should govern the L79 predictive-processing reply. → Rider (e).
  - Gibson "showed" should be "argued" (L65). Partly right, because Goldstone 1998's unitization supports restructuring. → Citation-fidelity rider (b).
  - "Meditation suppresses the DMN" (L69). Disputed: [default-mode-network](/concepts/default-mode-network/) L112 supports the task-state shorthand, and the cited "2026 meta-analysis" link resolves to a 2022 paper. → Not tasked.
  - The residual Billon owner inference. Disputed: L89 already says "a reporting position rather than an intact felt owner". → Not tasked.
  - Methodology items 19, 22, 23 and 25 are recorded without action. Item 23 (rival-answer test) resembles Claude's item 3 (rival roster), and item 22 (premise-provenance labels) resembles Claude's item 4 (functional/phenomenal marking). Neither pair was counted as convergent, because each proposes a different mechanism.

## Divergences

- **Claude vs ChatGPT on the quantum paragraph (L113).** Claude's row 11 says "**DELETE** from this apex (off-thesis tenet leakage)", because the apex "still spends apex space on it". ChatGPT says "The quantum-coherence paragraph is responsibly labelled speculative". The Claude processing pass kept it: the 2026-10-07 apex-evolve Tenet-2 check cleared it, and it is the hedge itself. The fence stands in the Threshold P1.
- **Claude vs ChatGPT on the changelog.** Claude: "As of 2026-10-14 the changelog trails the corpus by about a week". ChatGPT: "Those changes are accurately recorded in the changelog". Resolved for ChatGPT. The live page showed 2026-10-13 entries, and Claude's fetch probably served a stale cached copy of a 1.8 MB page. Claude's methodology item 7(c) falls with it.
- **Claude vs ChatGPT on Gibson.** Claude gives the citation a PASS; ChatGPT calls it "overgeneralized". Partly resolved: Goldstone 1998 lists four mechanisms, and one of them (unitization) supports the apex. The defensible fix is the one-word "showed" → "argued".
- **Claude vs ChatGPT on Billon.** Claude says RETAIN (row 8). ChatGPT says "The residual inference still goes too far". Resolved for Claude on the current text (L89).

## Method Notes

- **Adjudication came before clustering.** Every cluster was re-checked against the live apex, which is unchanged since `6e640ad89e`. Every source counter-quote was grepped verbatim, and every reviewer quote above was grep-verified in its review file. No candidate convergence was rejected outright. Two clusters carry a disputed half that was excluded: ChatGPT's misidentified neonatal study (cluster 10) and Claude's Paralogism-on-the-minimal-claim charge (cluster 11).
- **Same-family exposure.** Claude Fable 5.1 reviewed Claude-generated content, and this synthesis is also Claude-written. With Gemini absent, ChatGPT is the cycle's only non-Claude voice, so a blind spot shared by the Claude family would not show up as a divergence. Claude's own Part 5 item 7 names this risk. The convergence here rests on grep-verifiable loci rather than on judgement, which limits the exposure.
- **Priority.** Three P2 tasks were upgraded to P1 under the skill's rule. The two existing P1s are at the skill's ceiling and were **not** escalated to P0: they are calibration edits to one apex, and P0 would preempt the whole queue. `parse_tasks` returns **139 active tasks both before and after**, a delta of 0. P1 went from 2 to 5 and P2 from 36 to 33; P3 stayed at 101. All five rewritten tasks keep a non-`None` review pointer under the plural field. The NEEDS-HUMAN entry has no P tier, so the parser and the picker cannot see it.
- **Shared word budget.** Four apex tasks are now P1 on one file with 853 words of headroom. Their stated ceilings sum to about 820–970: calibration ≤140, rivals 330–430, citations ~300–350 including References, Threshold ≤50. A shared-budget paragraph was added to the Notes of each apex task. The citation task's built-in under-350 fallback is the expected path if it runs third. The social-construction task is on a different file, which has 940 words of headroom.
- **Repairs that confessed instead of correcting.** Two earlier passes on this apex fit the reviewers' charge exactly. The 2026-07-26 apex-evolve installed the Tenet-1 disclosure and "independently argued" in the same pass. The 2026-08-12 refine "closed" the illusionist-regress family by appending a concession next to the argument it concedes. Both are in the P1 calibration task.
- **Related standing entries.** The status-propagation family is the subject of the 2026-08-03 methodology entry, and this is the ninth cycle to raise it and the first at 2/2 since 2026-09-29. The evidential-independence audit is already item (4) of the 2026-07-25 entry. As the driver asked, today's material goes into **one** new NEEDS-HUMAN entry that cross-references both, not into addenda.
- **Two retitle decisions are now open.** One is today's. The other is the 2026-09-16 `topics/lucid-dreaming-and-dualist-rendering` entry, which was 3/3 convergent and is still undecided.