---
ai_contribution: 100
ai_generated_date: 2026-10-21
ai_modified: 2026-10-21 08:38:10+00:00
ai_system: claude-opus-5-5
author: null
concepts:
- '[[four-category-ontology]]'
created: 2026-10-21
date: &id001 2026-10-21
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-21 08:38:10+00:00
modified: *id001
related_articles: []
title: Deep Review - Four-Category Ontology
topics: []
---

**Date**: 2026-10-21
**Article**: [Four-Category Ontology](/concepts/four-category-ontology/)
**Previous review**: [2026-07-18](/reviews/deep-review-2026-07-18-four-category-ontology/)

## Context

The two prior reviews (2026-07-06, 2026-07-18) found zero defects and declared the article converged. Since then the 2026-10-20 refine corrected the Lowe volition reading at L57 and left an open P3 (the L76 continuity claim). This pass re-ran the quote lens against raw text rather than accepting the earlier certifications. Two of them did not hold up. The 07-18 review rated "strictly speaking there is no such thing as event causation" as "verified in substance", which falls short of a verbatim match. The Kistler/Gibb attribution traced back to a research note that had flagged its own source as unread ("Kistler critique full text not read"; "Gibb's independent development ... not yet surveyed").

## Pessimistic Analysis Summary

### Critical Issues Found

- **Kistler misattributed (L70, L82).** The article said critics "such as Max Kistler" reconstruct Lowe's model as adding "no energy to the brain", and that Kistler and Gibb press whether fact-causation is "genuine causal work or relabeling". Kistler's chapter (HAL hal-03953767, full text, 10,343 words) has zero hits for "energ", "relabel" or "genuine". His actual verdict is that Lowe's four arguments establish *weak* property dualism, "compatible with physicalism", and not the strong form Lowe claims. He also grants that the decision is a cause *specific* to the movement while the neural cause is not. **Fix:** the no-energy point is now presented as an implication of Lowe's own claim that mental causes exploit no gaps (Lowe 2008: 117, via Griffith). L82 now states Kistler's real critique. Gibb is dropped because her stance on fact-causation could not be verified.
- **Quote splice, CNS (L70).** The quoted string "what is known about the central nervous system" does not match any contiguous span of the reported Erkenntnis abstract wording ("consistent with all that is currently known about the operations of the human central nervous system"). I also could not reach the raw abstract (Springer JS-walled, abstract elided at Crossref, OpenAlex and S2). **Fix:** quotation marks removed and the sentence paraphrased.
- **Unverified verbatim quote (L53).** I could not grep "strictly speaking there is no such thing as event causation" in any raw source. A search summary suggested Lowe's p. 6 wording is "there is strictly speaking no such thing as event causation", a different word order. **Fix:** quotation marks removed. The paraphrase is supported by Griffith ("event causation is reducible to agent causation") and by the book abstract ("all causation is causation by agents").
- **Quote misattributed to Lowe's voice (L57).** "unmoved movers, or initiators of new causal chains" was introduced as "in his phrase". Raw text puts it in the publisher's book description (Google Books synopsis, also afterall.net). **Fix:** now "in the book's abstract", matching the model wording at `topics/agent-causation-and-acting-for-reasons` L66.
- **Quote not in the cited source, and gloss contradicts it (L59).** The article quoted "a 'spontaneous' power", glossed as "of a piece with the powers of any other substance". The chapter abstract (OUP DOI 10.1093/acprof:oso/9780199603770.003.0007, via the OpenAlex inverted index) says "a unique kind of spontaneous power" ... "in the light of reason". **Fix:** both phrases are now quoted verbatim, marked "(chapter abstract)", and the contradicting gloss is removed.
- **Subtitle splice (L47).** The article had "a foundation for natural science". The subtitle reads "A Metaphysical Foundation for Natural Science". **Fix:** now "a metaphysical foundation for natural science".
- **Overstated modal claim (L72).** The article said the NCSD self is "*necessarily embodied*". Lowe's raw text (2012 NCSD chapter, newdualism.org PDF) says "two distinct, but not necessary separable, individual substances" and that "we are not required to think of the two as separable". **Fix:** now "not necessarily separable from it".
- **Argument roles conflated (L72).** The entanglement argument was presented as support for self–body non-identity. Kistler (2022) reconstructs it as an argument that mental *causes* are not neural causes (Lowe 1993: 639; 1996: 84). Self–body distinctness rests on the unity argument (Griffith: Lowe 2008: 96). **Fix:** the two arguments are now separated and each is attributed.
- **Lowe's argument for the one-way reduction replaced (L55).** The "ungrounded relatum" rationale had no source. Griffith's account is that event-causal sentences are elliptical for substance-causal ones (p. 5), and that causing is a doing while events only happen (pp. 4, 165). **Fix:** now uses Griffith's version.
- **Calibration, Tenet 3 (L76).** "This directly serves Tenet 3" is now "That fits Tenet 3 without evidencing it". This is a defeater-removal (the "couldn't be causation" charge), not evidence.
- **The open P3 (L76 continuity).** The continuity claim is now marked "on Lowe's terms". The added sentences say what the Map keeps (substance causation, volitionist structure, two-way power) and what it gives up: Lowe grounds continuity in the premise that agents cause only by acting. An agent that causes its volition without acting is the classical agent-causal picture the book abstract says Lowe declines ("an agent as such is a cause"). This is consistent with `positions/agency-and-will` [P-A6](/positions/agency-and-will/#p-a6) (2026-10-20). The P3 task is moved to Completed.
- **Chance-fixing concession (L80).** Closure was stated only as sufficiency. The text now concedes that chance-fixing closure survives exact Born preservation, and that whether settling an outcome without shifting its chance counts as causing it is part of the mechanism debt. Wording follows `concepts/causal-exclusion-argument` L79 and `concepts/causal-closure` L138.
- **Internal tension, testability (L80/L82).** The article called the Map's difference "statistically undetectable" and in the next paragraph called it "a genuine testability commitment". Both are now aligned with tenets.md Tenet 2: invisible to unconditioned aggregate statistics; empirical risk only through a consciousness-conditioned test that has not run.

### Medium Issues Found

- "Laws of nature are relations between kinds and attributes" (L47). Per Wasserman's NDPR review (pp. 45–7), Lowe says characterisation is not a "genuine" relation. **Fix:** now "laws of nature consist in kinds being characterised by attributes".
- Source/Map separation at L57: "This reframes agency" now reads "For Lowe, this reframes agency", since the Map departs from the claim that follows.
- The lead mentioned only the physics fork. It now carries the second departure (agent-caused vs uncaused volitions) so the summary survives truncation.

### Citation Web-Verify Ledger (§2.4)

- Lowe 2006 (*The Four-Category Ontology: A Metaphysical Foundation for Natural Science*, OUP). State: real-correct. Crossref print date is 2005-12-01; the 2006 copyright year is the standard citation. Subtitle verified.
- Lowe 2006 (*Erkenntnis* 65(1): 5–23, DOI 10.1007/s10670-006-9012-3). State: real-correct (Crossref). Abstract text not reachable raw.
- Lowe 2008 (*Personal Agency*, OUP). State: real-correct (Google Books record, 2008-09-04).
- Lowe 2013 ("Substance Causation, Powers, and Human Agency", pp. 153–172). State: real-correct. Crossref chapter DOIs .0001–.0008 confirm it is ch. 6 after an unnumbered introduction.
- Lowe 1993 ("The Causal Autonomy of the Mental", *Mind* 102(408): 629–644, DOI 10.1093/mind/102.408.629). State: real-correct (Crossref). Newly added.
- Kistler 2022 ("Lowe's Dualist Construal of Mental Causation", in Szatkowski ed., *E. J. Lowe and Ontology*, Routledge, pp. 239–259, DOI 10.4324/9781003196341-16). State: real-correct (HAL record and Crossref). Newly added; full text read.
- Griffith 2009 (NDPR 2009.06.15). State: real-correct (raw page). Newly added as the source of the page references to Lowe 2008 (5, 7, 96, 117).
- Gibb (no year, inline). Removed: unverifiable attribution. See Remaining Items.
- Inline↔References: every (surname, year) pair now resolves in both directions. Gibb appears only as co-editor of the Lowe 2013 volume.
- Result-direction leg: Kistler's verdict reads *favourably* to the article on one point (the decision is a specific cause) and *against* on another (only weak, physicalism-compatible dualism). Both are stated.
- Cited-author-stance leg: Kistler is not a dualist ally. The text presents his reconstruction as a cost to Lowe's route, not as support for the Map.

### Counterarguments Considered

- Kim's exclusion argument: Lowe's reply and the Map's alternative are both stated. The Map's reply is now explicit that it answers only sufficiency closure.
- Physicalist absorption of Lowe's structuring cause (Kistler): now the stated cost of the no-gap route. It also makes the existing remark that a purely structuring cause sits close to epiphenomenalism more concrete.

### Reasoning-mode classification (editor-internal)

- Engagement with Kim: mixed. Lowe's reply denies the shared premise (Mode One within Lowe's framework). The Map's reply marks where chance-fixing closure still holds, honest boundary-marking.
- Engagement with Kistler: Mode Three. His weak-dualism verdict is recorded as a real cost, not rebutted.

## Optimistic Analysis Summary

### Strengths Preserved
- The "deliberate fork" staging (Lowe's structuring cause vs the Map's token-level outcome bias) remains the article's best asset, and is now sharper because Kistler's verdict gives the no-gap route a stated cost.
- The repeated "framework, not evidence" discipline, and the scaffolding qualification on NCSD.
- The 2026-10-20 Lowe volition correction at L57 is kept unchanged.

### Enhancements Made
- The Kistler critique in place of an unverified one; unity and entanglement arguments separated; continuity cost stated; chance-fixing concession; lead now mentions both departures.

### Cross-links Added
- [quantum-interface](/positions/quantum-interface/) (mechanism-debt anchor, L80).

## Remaining Items

- Gibb, and Carruth & Gibb 2018 ("The Ontology of E. J. Lowe's Substance Dualism", in *Ontology, Modality, and Mind*, OUP, pp. 149–164). A 2023 *Synthese* paper (Buckareff & Hawkins, 10.1007/s11229-023-04282-4) reports that they argue Lowe's "distinction between fact and event causation is di[…]" (search-snippet truncation). This may be the real critic of fact-causation the article once gestured at, but neither text was reachable (Durham and PhilPapers are Cloudflare-walled, Springer is JS-walled). Unverified; do not reinstate without the raw text.

## Stability Notes

- The prior stability note ("genuine causal work vs relabeling" is a live dispute, attributed to Kistler and Gibb) is superseded. The dispute may exist, but the attribution failed at raw source. The current wording rests on Kistler's text and should not be re-flagged unless a later edit changes it.
- The Map's departure from Lowe's no-physics-gap route is a deliberate tenet-driven fork, not a contradiction (carried forward).
- The continuity cost in Relation to Site Perspective is a stated price, not an unresolved defect. Do not try to "resolve" it by fiat in either direction.
- Length after this pass: 2231 words by analyze_length (soft 2500, hard 3500). Further additions should be length-neutral.