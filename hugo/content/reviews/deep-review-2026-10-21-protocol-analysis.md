---
ai_contribution: 100
ai_generated_date: 2026-10-21
ai_modified: 2026-10-21 18:15:46+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-21
date: &id001 2026-10-21
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-21 18:15:46+00:00
modified: *id001
related_articles: []
title: 'Deep Review - Protocol Analysis: When Verbal Reports Are Data'
topics: []
---

**Date**: 2026-10-21
**Article**: [Protocol Analysis: When Verbal Reports Are Data](/topics/protocol-analysis/)
**Previous review**: Never (written 2026-10-21 ~17:50Z). This review is also the cross-review of the eight hosts that link the page.
**Word count**: 2,427 → 2,487 (+60; topics soft 3,000, hard 4,000)

## Pessimistic Analysis Summary

### Critical Issues Found

- **Dropped qualifier, Schooler 2011.** The page had "suggested that William James would have seen thinking aloud as 'a scientifically rigorous form of introspection'". The abstract reads "James would likely view the think-aloud procedure as a scientifically rigorous form of introspection". Restored as "would likely have seen".
- **Dropped scope qualifiers, E&S 1980 pp. 246–247.** "The questions supplied enough background…" is "In some of these studies, the questions presented to subjects contain considerable background information" in the scan. "And the lag between process and probe was long" is "in most of the studies reviewed by Nisbett and Wilson, the time lag … was sufficiently great". Both are now "Some questions…" and "in most of the studies…".
- **Dropped qualifier, Fox et al. 2011.** "Every procedure added time" is, in the abstract, "All verbal reporting procedures tend to increase times to complete tasks". Changed to "All reporting procedures tended to add time."
- **Host attribution error, contemplative-epistemology L81.** The host said microphenomenology "shares two of their [Ericsson and Simon's] safeguards, a specific episode and 'how' in place of 'why'". Ericsson and Simon recommend no "how" safeguard. E&S 1980 p. 221 names "How did you do these tasks?" as interpretive probing that "cannot be relied on to produce data stemming directly from the subjects' actual sequences of thought processes". On their model process is never reported; the analyst infers it. This edges onto check (b). Fixed to "a specific episode and no 'why' questions".

### Medium Issues Found

- **Lead precision.** "thinking aloud leaves performance unchanged" read as including speed, but the meta-analysis found that time increased. Changed to "task accuracy", matching Fox et al.'s own gloss ("objectively measurable performance (accuracy)") and the body's caution.
- **Verbal overshadowing listed as an exception without saying why.** The bullet called it "a Level 3 procedure", which the model predicts to be reactive, so it looked like a non-exception under an "exceptions" heading. Added: the model expects reactivity, and it is an exception *in direction*, since Fox et al. found that describing raised performance.
- **The page's two senses of "content".** E&S p. 245 accept Nisbett and Wilson's "private facts" (focus of attention, *current sensations, emotions*, evaluations, plans) as STM contents. The Limits gloss ("symbols, operands and intermediate results") left those out, so a reader could take the Scope paragraph as validating sensation reports *as phenomenal reports*. Added one sentence: heeded sensations and emotions enter the model as items to be voiced, not as descriptions of what they are like (check (a)).
- **Host overclaim, process-content-distinction L97.** "protocol analysis shows that whether a report draws on memory or on inference depends on…" was stronger than the page ("That is their reading of the literature, not an independent finding"; White 1988 judged the question open). Changed "shows" to "holds".
- **Stranded dependent, process-content-distinction L114.** The write-time edit rescoped L97 so that what is negotiable is report validity, while "process itself stays a matter for third-person inference". Further Reading still said microphenomenology "can move the content/process line". Changed to "can extend content access into apparent process-territory", matching L97's own "territory that looks like process-territory from outside". No other page uses the "move the line" phrasing (grep outside `reviews/` and `workflow/`).
- **Self-citation authorship.** Reference 16 (process-content-distinction) listed Oquatre-sept and Ocinq. The host's `ai_system` gained `claude-opus-5-5` in the same commit, so the list now ends "…Ocinq, C., & Ocinq-cinq, C." per writing-style.md.

### Citation ledger (publisher of record: Crossref metadata, OpenAlex abstracts, the SEP HTML, and the psu.edu scan of E&S 1980 read page-by-page)

- Alogna et al. 2014 (Registered replication report, *PPS* 9(5) 556–578): real-correct. Abstract: "a robust verbal overshadowing effect that is strongly influenced by the relative timing of the tasks". Direction (impairment) correct.
- Ericsson & Fox 2011 (*Psych. Bull.* 137(2) 351–354): real-correct. Title and the "involves only focusing…" quote verbatim. The paraphrase "neither inner observation nor generated descriptions or explanations" is faithful to "does not require inner observation or generation of descriptions and explanations". Stance: denies that think-aloud is introspection, as the page says.
- Ericsson & Simon 1980 (*Psych. Rev.* 87(3) 215–251): real-correct. Four abstract quotes verbatim ("central proposal", "within the theoretical framework…" with a hyphenation artefact only, "Verbalizing information…", "The inaccurate reports…"). Scan pages read: p. 217 (no "privileged status as a direct observation"; fn. 1 "heeded"); p. 221 ("interpretive probing … cannot be relied on"); p. 225 (17×45 example, automation, "much less about neuronal events"); p. 227 (Level 1/2/3 definitions and predictions); p. 230 (Gagné & Smith: "greatly improved performance on the transfer task"); p. 245 (no definite model, undefined "content"/"process", the list, the one missing item); pp. 246–247 (three differences, the shock example, Smith & Miller "agreeing generally", "careless charge of 'introspection'"). All page-level paraphrases hold, with the two qualifier repairs above.
- Ericsson & Simon 1993 (*Protocol Analysis*, rev. ed., 1st ed. 1984): cited only as the book edition; no page claims. Not re-verified (the research note confirms 1984 via the Denzin review and the 1993 DOI).
- Fox & Charness 2010 (*ANC* 17(2) 191–204): real-correct. d = 0.73 and 0.92 verbatim; direction "raised" correct.
- Fox, Ericsson & Best 2011 (*Psych. Bull.* 137(2) 316–344): real-correct (OpenAlex dates it 2010 as online-first; the issue year is 2011). 94 studies, "nearly 3,500", r = −.03, and the describe/explain quote are verbatim; time qualifier repaired.
- Gagné & Smith 1962 (*JEP* 63(1) 12–18): real-correct (Crossref). No abstract in OpenAlex. The result is cited "as Ericsson and Simon discuss it" and matches p. 230.
- Nisbett & Wilson 1977 (*Psych. Rev.* 84(3) 231–259): real-correct; "a priori, implicit causal theories" in the abstract.
- Schooler 2011 (*Psych. Bull.* 137(2) 345–350): real-correct. Three quotes verbatim; the "likely" qualifier restored. Stance: sympathetic ("introspection finally getting the scientific grounding"), as the page says.
- Schooler, Ohlsson & Brooks 1993 (*JEP:G* 122(2) 166–183): real-correct; insight quote verbatim.
- Schwitzgebel 2011 (*Perplexities*, MIT Press): real-correct. The "Unreliability of Naive Introspection" chapter (author's PDF, grepped) covers colour in dreams, centre/periphery clarity, and inner-speech structure.
- Schwitzgebel SEP "Introspection": real-correct. "First published Tue Feb 2, 2010; substantive revision Thu Apr 25, 2024". The quote is verbatim with the curly apostrophe. "Turns at once to counter-evidence" holds: after the Hamilton & Sanford example comes "On the other hand, Flavell, Green, and Flavell (1995)…".
- Smith & Miller 1978 (*Psych. Rev.* 85(4) 355–362): real-correct; quote verbatim.
- White 1988 (*BJP* 79(1) 13–45): real-correct; both quotes verbatim.
- Wilson & Schooler 1991 (*JPSP* 60(2) 181–192): real-correct; quote verbatim. "Lowered the quality of preferences" matches "agreed less with the experts" and the title.
- **Quote count**: all 17 substantive quoted spans re-grepped against raw sources (the brief asked for ≥8). The single-word quotes "content", "process", "introspection" and "interpretive" were checked against scan pp. 245, 247 and 221.
- **(surname, year) both ways**: every inline author-year pair resolves to an entry, and every entry 1–16 is cited inline (16 is the self-citation behind the process-content-distinction links). No orphans.
- **Superlatives**: none in the empirical-currency sense. "The strongest exception at Levels 1–2" is the Map's comparative judgement within the page's own list, and no post-2011 reactivity meta-analysis was found by the research pass.

### Counterarguments Considered

- *Physicalist*: protocol analysis is a physicalist information-processing model, so it cannot help a dualist map. The page already concedes this ("sits comfortably within the information-processing model it was built on") and claims only an evidential-hygiene role. This is bedrock agreement, not a defect.
- *Epiphenomenalist inference from silence*: the Relation section blocks it with an argument that holds inside the model ("says nothing about what that information is like").
- *Eliminativist / Dennett*: none of the page's claims depend on a reply to Dennett. The heterophenomenology host's "parallel stance" sentence asserts no influence.
- *Empiricist*: "Did E&S refute N&W?" The page lets White's verdict stand. Good calibration.

## Optimistic Analysis Summary

### Strengths Preserved
- The architectural/procedural split ("The line is architectural; access to it is procedural"), which is the page's central contribution.
- Keeping reactivity and validity apart (the Schooler quote) and the Fox et al. accuracy caveat.
- Coiner discipline: thinking aloud predates E&S, and the term's origin is left unsettled.
- Tenet section: Tenet 1 is served "in one way only", and Tenets 2/3 "fit without evidencing". Epiphenomenalism is refused, not conceded.
- The table of reportable and non-reportable items.

### Enhancements Made
- Qualifier fidelity (four repairs), the lead's precision on accuracy, the direction of the verbal-overshadowing exception, and the sensation/emotion clarifier for check (a).

### Cross-links Added
- None. The page already links all eight hosts, and they all link back.

## Cross-review of the eight hosts (checks a–f)

| Host | (a) | (b) | (c) | (d) | (e) | (f) | Edit |
|---|---|---|---|---|---|---|---|
| process-content-distinction | pass | pass after fix | pass | n/a | n/a | n/a | L97 "shows" → "holds"; L114 FR "can move the content/process line" → "can extend content access into apparent process-territory" |
| contemplative-epistemology | pass | fix | pass | n/a | n/a | n/a | L81 "'how' in place of 'why'" → "no 'why' questions" |
| apophatic-cartography-four-criteria | pass | pass | pass | n/a | n/a | pass (12 refs, contiguous; no numeric body cross-refs) | none |
| descriptive-experience-sampling | pass | pass | pass | n/a | n/a | pass (26 refs, contiguous; Ericsson 1980 → #2) | none |
| microphenomenological-interview-method | pass | pass | pass | n/a | n/a | n/a | none (link-only, as briefed) |
| introspection | pass | pass | pass | n/a | n/a | n/a | none (link-only, as briefed) |
| confabulation-void | pass | pass | pass | n/a | n/a | pass (17 refs, contiguous; Ericsson 1980 → #2) | none |
| heterophenomenology | pass | pass | pass | pass (parallel stance only) | n/a | n/a | none |

## Remaining Items

- Pre-existing and outside this edit: apophatic-cartography-four-criteria L63 cites "Wallace identified in 1870" with no reference entry.
- Lead only: Ericsson 2003 (*JCS* 10(9–10), 1–18) appears in the same *JCS* issue as Dennett's "Who's on First?" (19–30), the issue the SEP cites as Jack and Roepstorff (eds.) 2003. If a later pass wants a Dennett–E&S link for heterophenomenology, that issue is where to look. Whether Dennett cites E&S is still unverified, so make no claim.
- The separate P3 for concepts/introspection L71 was left alone as instructed.

## Stability Notes

- The page is neutral between dualism and physicalism by design. Physicalist personas who say "this helps physicalism more" are restating the page's own concession and should not be re-flagged.
- "Did E&S refute N&W?" is left open, following White 1988. A future review should not push it to either verdict.
- Whether thinking aloud is introspection (Ericsson & Fox vs Schooler and SEP) is presented as an open dispute on purpose. The Map does not settle it.
- Verbal overshadowing is a Level 3 case and an exception only in direction. Do not move it out of the exceptions list, and do not restate it as a Level 1–2 counterexample.