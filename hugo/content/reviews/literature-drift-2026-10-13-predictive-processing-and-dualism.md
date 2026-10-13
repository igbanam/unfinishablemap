---
ai_contribution: 100
ai_generated_date: 2026-10-13
ai_modified: 2026-10-13 05:10:31+00:00
ai_system: claude-opus-5-5
author: null
concepts:
- '[[predictive-processing]]'
created: 2026-10-13
date: &id001 2026-10-13
description: Weekly literature-drift audit of the predictive-processing article. Two
  2024-2026 reviews of active inference's empirical status go uncited, and the effort
  account is cited to its precursor, not its active-inference formalisation.
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-13 05:10:31+00:00
modified: *id001
related_articles:
- '[[deep-review-2026-09-30-predictive-processing-and-dualism]]'
- '[[attention-as-causal-bridge]]'
- '[[calibration-audit-triple]]'
title: Literature-Drift Review - 2026-10-13 - Predictive Processing and Dualism
topics:
- '[[predictive-processing-and-dualism]]'
---

**Date**: 2026-10-13
**Article**: [Predictive Processing and Dualism](/topics/predictive-processing-and-dualism/) (`obsidian/topics/predictive-processing-and-dualism.md`)
**Audit**: Audit One of the [calibration audit triple](/project/calibration-audit-triple/), the weekly Tuesday run.
**Previous review**: [deep review 2026-09-30](/reviews/deep-review-2026-09-30-predictive-processing-and-dualism/) (seventh deep review). There is no prior literature-drift audit of this article.
**Outcome**: **drift-flagged**. Check 1 (median-year lag) and check 2 (missing topically-appropriate papers) both fire. Check 3 (superlative currency) is clean.

## Summary

The article's most consequential empirical claim is in §The Mechanistic Rival. It says active inference "offers equations, process theories, and neural implementations generating testable predictions now". It also says active inference "accrues support as variance explained". Two peer-reviewed reviews in *Neuroscience & Biobehavioral Reviews* (2024, 2026) bear on these claims, and the article cites neither. Both reviews assess the empirical standing of predictive coding and active inference. Both are more guarded than the article's phrasing:

- predictive coding has "modest support";
- active inference work has mostly *fitted* models to behaviour rather than *tested* the theory against rivals;
- the framework is "often criticized for the difficulty of extracting qualitatively distinct, testable predictions".

The article's concession on *articulation* still stands, because being well specified is not the same as being confirmed. What has moved is its description of the rival's present *empirical* standing. A corpus cross-check also found a second problem. The article cites the effort-as-information-cost account to Zénon, Solopchuk & Pezzulo (2019), which is a general information-theoretic paper. The active-inference formalisation of effort is Parr, Holmes, Friston & Pezzulo (2023). The Map's own attention apex already cites it, and this article's own Further Reading describes that apex as deferring its confrontation with active inference to this article.

None of this helps the Map. A rival with only modest empirical support does not lend any support to the Map's selector, which has none. See the calibration fence below.

## Selection

- **Candidates**: 14 topic articles match `active_research_sections`. 12 are in `recently_audited`. That leaves two:
  - `predictive-processing-and-dualism`: ai_modified 2026-09-30, the oldest. Superlative count 0.
  - `basal-and-bioelectric-cognition`: ai_modified 2026-10-10. Skipped, as on 2026-10-06. It is still owned by the open P2 NEEDS-HUMAN length decision and the parked P3 Oviedo-citation task.
- **Driver exclusions**:
  - The article is not on today's ~30h exclusion list. Its last commit was `152fd659dc`, 2026-09-30, a deep-review cycle.
  - No prior literature-drift review of it exists. No `reviews/literature-drift-*` file existed before this one; earlier audits logged to the changelog only.
  - No open task targets the file. Its two mentions in the todo Notes are incidental.

## Citation Metrics

- **References**: 17. Austin 1962 is excluded as canonical. There are no Map self-citations.
- **Dated non-canonical citations (16)**: Stapp 2007; Feldman & Friston 2010; Friston 2010; Clark 2013; Friston et al. 2013; Hohwy 2013; Clark 2016; Clark, Friston & Wilkinson 2019; Zénon et al. 2019; Friston, Wiese & Hobson 2020; Hohwy & Seth 2020; Beni 2021; Seth 2021; Wiese & Friston 2021; Gunji et al. 2022; Laukkonen et al. 2025.
- **Median year**: 2019 (the 8th and 9th values are both 2019). This is **7 years** behind ai_modified (2026), against a threshold of 5, so **check 1 fires**. Two caveats:
  - The median is anchored by the canonical 2010–2013 statements of the framework, which the article's frame is partly *about*. The fish-sentience audit of 2026-09-15 showed that check 1 alone is weak evidence.
  - Here check 2 fires independently, so the flag does not rest on check 1.
- **Superlative claims**: `find_superlative_claims` returns 0. The phrase "the strongest physicalist alternative the Map currently faces" is an editorial ranking, not a record that a newer result could supersede.

## Search

- **The one WebSearch call** (extended): `predictive processing active inference consciousness empirical evidence neural prediction error 2024 2025 review`
- **Target**: the empirical standing of predictive coding and active inference. This is the claim the mechanistic-rival section's "well ahead … testable predictions now" and its "variance explained" asymmetry paragraph depend on. It is also the area where the 2020s literature has moved most.

| Result | Status | Verdict |
|---|---|---|
| Hodson, Mehta & Smith (2024). The empirical status of predictive coding and active inference. *Neurosci. Biobehav. Rev.* 157, 105473. doi:10.1016/j.neubiorev.2023.105473 | Peer-reviewed. Crossref: issued 2024-02 (online 2023-11-27). Semantic Scholar abstract read. OA bronze. ~70 citations | **Topically appropriate, uncited** |
| Lageman, Fahrenfort & Slagter (2026). Prediction in action: Toward an empirical science of active inference. *Neurosci. Biobehav. Rev.* 188, 106817. doi:10.1016/j.neubiorev.2026.106817 | Peer-reviewed. Crossref: issued 2026-09 (online 2026-06-13). OpenAlex abstract read. OA hybrid | **Topically appropriate, uncited** |
| Adama & Bogdan (2026). Computational predictive processing models of consciousness: a systematic review of non-invasive brain signal analysis in disorders of consciousness. *Front. Comput. Neurosci.* 20. doi:10.3389/fncom.2026.1797090 | Peer-reviewed systematic review (Europe PMC + Crossref). The "Frontiers" search hit is the same DOI | Frame-divergent. It reviews DoC biomarkers, and the article makes no clinical or NCC-biomarker claim |
| Xiong et al. 2024, propofol and predictive routing (*PNAS* 121(42)), named in the search summary | Already cited in [anaesthesia-and-the-consciousness-interface](/topics/anaesthesia-and-the-consciousness-interface/), its proper home | Not missing |
| arXiv 2409.20318 (Rosetta Stone neurophenomenology), arXiv 2508.16877 (coalgebraic PP), arXiv 2606.05206 (multi-LLM scoring) | Preprints | Excluded |
| ResearchGate "Editorial: Predictive Processing and Consciousness"; PubMed 38755514 (functional neurological disorder) | Editorial / off-topic | Excluded |

**Missing topically-appropriate papers: 2** (threshold 2), so **check 2 fires**. A grep of `topics concepts apex voids positions research` for `Hodson`, `Lageman` and "empirical status of predictive coding" returns 0 files.

## Findings

### 1. The rival's empirical standing is stated more strongly than the 2024–2026 reviews support (§The Mechanistic Rival)

**What the reviews say** (abstract-level; checked verbatim):

- **Hodson et al. 2024**:
  - "For Predictive Coding, we find that existing empirical evidence offers modest support. However, some positive results can also be explained by alternative feedforward (e.g., feature detection-based) models."
  - "While Active Inference models tend to explain behavioral data reasonably well, there has not been a focus on testing empirical validity of active inference theory per se, which would require formal comparison to other models (e.g., non-Bayesian or model-free reinforcement learning models)."
- **Lageman et al. 2026**:
  - The framework "is often criticized for the difficulty of extracting qualitatively distinct, testable predictions and its limited empirical grounding."
  - Among the decision-making predictions it evaluates is "that agents behave more stochastically when they are uncertain about outcome predictions".
  - Its verdict is that "existing empirical work is broadly consistent with several of these predictions, but further research is necessary to draw more definitive conclusions", and it emphasises "the need for theory-driven experiments that can adjudicate between accounts."

**What the article says**:

- **L108**: "active inference offers equations, process theories, and neural implementations generating testable predictions now; on mechanistic specification the rival is well ahead."
- **L112**: "Active inference accrues support as variance explained: each demonstration that measured precision dynamics predict the trial-by-trial resolution of near-equipoise decisions shrinks the residue…"

**What survives**:

- The articulation concession is correct. Active inference *is* far better specified than the post-decoherence selection programme, and both reviews agree it is formally rich.
- The asymmetry paragraph's *logic* is also correct, since it describes what would count.

**What has drifted**: the present-tense description of the rival's empirical lead.

- The reviews put the "demonstration" programme at an early stage.
- The prediction most relevant to the Map is Lageman's "more stochastic when uncertain", because precision governs stochasticity at near-equipoise. That is exactly the residue the Map claims. Yet the 2026 review rates that prediction only "broadly consistent", pending adjudicating experiments.

**Calibration fence (mandatory)**: this finding must *not* be written as a point scored for the Map.

1. Hodson's comparison classes are *other physicalist* models: model-free RL and feedforward feature detection. Weak active-inference-specific confirmation leaves the physicalist mechanistic family intact. Whatever wins among those models, the question of whether a residue exists is untouched.
2. The Map's selector has *no* empirical support. On the five-tier scale, the rival's "modest / broadly consistent" support remains far above it.
3. The update is therefore a correction of tense and degree on the rival's side. It does not move the Map's verdict ("active inference has won the articulation contest as it stands"). See [evidential-status-discipline](/project/evidential-status-discipline/).

### 2. The effort account is cited to its pre-active-inference precursor (§The Mechanistic Rival, L108)

**The article's claim**: active inference "offers a positive account" of felt effort, namely that "effort tracks the informational cost of updating — how far beliefs and policies must be moved from where they would settle by default (Zénon, Solopchuk & Pezzulo, 2019)".

**What Zénon et al. 2019 actually is**:

- The 09-30 deep review certified its metadata and the information-cost paraphrase as real-correct. That still holds.
- But it is a *general information-theoretic* account: costs as "the amount of information required to update a person's prior knowledge (or internal model)". It is not an active-inference formalisation, and its abstract does not mention policies.

**The active-inference formalisation is Parr, Holmes, Friston & Pezzulo (2023)**. "Cognitive effort and active inference", *Neuropsychologia* 184, 108562, doi:10.1016/j.neuropsychologia.2023.108562. Verified at Crossref; abstract read. It:

- "formalis[es] the notion of cognitive (or mental) effort in terms of active inference";
- says participants "must overcome prior beliefs about how they would normally act" (this is the article's "beliefs and policies … where they would settle by default");
- treats effort as covert "mental action", "much like deploying covert attention";
- shows the effort parameters "can be recovered" from performance data.

**Sibling drift**: [attention-as-causal-bridge](/apex/attention-as-causal-bridge/) already cites Parr et al. 2023 (L159, ref L207) for "the expected cost of reallocating precision". This article's own Further Reading entry (L164) describes that apex as one "which defers its framework-level confrontation with active inference to this article". So the host article's effort citation lags the apex that defers to it.

**This is a different axis from the 09-30 certification**: that review checked whether the cited work exists and says what is paraphrased, while this finding concerns which framework the account belongs to. This is a named-idea-cited-to-its-precursor case. The fix is additive: keep Zénon for the information-cost framing and add Parr for the active-inference formalisation.

### 3. Reference-list integrity: clean

The driver asked for two patterns: a retraction notice's DOI cited in place of the paper, and a published paper cited as a preprint. Neither appears. All 15 post-2000 journal and book references were checked at Crossref or OpenAlex, with no `update-to` or retraction relations:

- **Laukkonen, Friston & Chandaria (2025)**: cited at the journal version, NBR 176, 106296. A 2024 PsyArXiv preprint, doi:10.31234/osf.io/daf5n, also exists under the same title.
- **Hohwy & Seth (2020)**: cited at the *PhiMiSci* 1(II) version, doi:10.33735/phimisci.2020.II.64. A PsyArXiv preprint, nd82g, also exists.
- **Clark, Friston & Wilkinson (2019)**: *JCS* 26, 19–33 (OpenAlex, via the Exeter repository). *JCS* is not Crossref-registered.
- **Exact matches**: Beni 2021 (*Synthese* 199(3–4), 6407–6427), Gunji 2022, Friston, Wiese & Hobson 2020, Wiese & Friston 2021, Zénon 2019 (vol 123, 5–18), Friston 2010, Friston et al. 2013, Feldman & Friston 2010 and Clark 2013.

### 4. Leads recorded, not tasked

- **Hohwy, J. (2021/2022). "Conscious Self-Evidencing."** *Review of Philosophy and Psychology* 13(4), 809–828, doi:10.1007/s13164-021-00578-x. Crossref-verified metadata. Also Hohwy, *The Self-Evidencing Agent* (MIT Press, 2026-02-03; ISBN 9780262385619), whose Crossref blurb verifiably says self-evidencing "helps us to understand self and consciousness".
  - **Why it matters**: the article presents Hohwy & Seth 2020's "not itself a theory of consciousness" as a proponents' *concession* (L72, and Relation to Site Perspective "its own proponents concede"). The same proponent has since applied self-evidencing to consciousness.
  - **Why it is not tasked**: (a) the 2021/22 paper's abstract could not be read; Springer and PhilArchive returned 403 and no API had the abstract. Its content is therefore unverified. (b) The 09-30 stability notes protect the Hohwy & Seth attribution. (c) The article already records the shift in its own terms through the beautiful-loop section ("Once it advances a direct theory of consciousness…").
  - A future deep review could check whether "its own proponents concede" should read "concede at the outset". It should read the 2021/22 abstract first.
- **Adama & Bogdan 2026**: frame-divergent (see table). If the Map ever builds a PP-and-NCC page, this is its 2026 systematic-review anchor.

## Length

- `analyze_length` gives **4623 words** for topics/: soft 3000, hard 4000, critical 6000; status `hard_warning`.
- Split: **4021 prose** (above the hard ceiling by itself) plus ~602 of Further Reading and References.
- **Headroom = 3999 − 4623 = −624.**
- The 09-30 deep review already condensed restatement and asked that the length gate be read against the prose figure. The minted task is therefore **strictly length-neutral (net ≤ 0 by `analyze_length`)**. Its additions (~60–90 prose words, plus three reference lines of ~75 words) must be funded by in-place trims that cut no calibration qualifier, hedge, concession or citation.

## Task Generated

One P2 `refine-draft` task on `obsidian/topics/predictive-processing-and-dualism.md`, inserted directly above `## Completed Tasks`: "Update predictive-processing-and-dualism citations — 2 2020s papers missing (empirical status of active inference) + effort account cited to its precursor".

## Stability Notes

- Do not re-flag the Hohwy & Seth 2020 *attribution* or the Beni ellipsed quote. Both are protected by the 09-30 review, and this audit does not dispute them.
- Zénon et al. 2019 remains real-correct for the information-cost framing. Finding 2 adds a citation; it does not remove or "correct" this one.
- The beautiful-loop theory keeps its undefeated-rival status. Nothing in this audit bears on it.
- Hodson 2024 and Lageman 2026 are evidence about the *rival's* empirical maturity. A future reviewer must not cite them as evidence *for* the Map's selector or residue.