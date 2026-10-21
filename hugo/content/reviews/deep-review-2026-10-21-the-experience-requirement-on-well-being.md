---
ai_contribution: 100
ai_generated_date: 2026-10-21
ai_modified: 2026-10-21 16:29:32+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-21
date: &id001 2026-10-21
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-21 16:29:32+00:00
modified: *id001
related_articles: []
title: Deep Review - The Experience Requirement on Well-Being
topics: []
---

**Date**: 2026-10-21
**Article**: [The Experience Requirement on Well-Being](/topics/the-experience-requirement-on-well-being/)
**Previous review**: [2026-09-06](/reviews/deep-review-2026-09-06-the-experience-requirement-on-well-being/) (plus [cross-review 2026-09-06](/reviews/cross-review-2026-09-06-the-experience-requirement-on-well-being/))
**Selection**: `deep_review.py next` returned `topics/phenomenology-of-moral-life`, which is on the driver's skip list. This was the next candidate (score 69). It was not edited today and has no open P0–P2 task (grepped `todo.md`).
**Length**: 3017 → **3015** by `analyze_length` (`soft_warning`; topics 3000 / 4000 / 6000). Prose 2533 → 2531; Further Reading plus References 485, unchanged. Length-neutral, as soft-warning mode requires.

## Why this pass was owed

Since 09-06 the body has changed only through the Kriegel re-date (10-06), the Mogensen print note (10-15) and one Further Reading line. The 09-06 ledger certified 16 quotations, but it checked the Lee, Mogensen and Kagan quotes against the research note's `[raw]` extracts, not against the papers. Per the driver brief, a ledger like that does not certify the quotes. So this pass re-checked every quotation against a raw primary text, and every empirical claim for the direction of its result.

## Sources obtained raw (pdftotext, whitespace-normalised, grep)

- Lee 2025: author's accepted PDF (andrewyuanlee.com, "Forthcoming in *Philosophers' Imprint*"). The journal galley is behind an Anubis bot wall, both by curl and by WebFetch.
- Mogensen 2025a: GPI Working Paper 24-2024 (globalprioritiesinstitute.org). The published Springer version is CC-BY, but Springer, PhilArchive and Wayback all returned bot challenges. So the quotes are verified in the author's working paper, not in the print text.
- Mogensen 2025b: GPI Working Paper 2-2025.
- van der Deijl 2019 and 2021: the Springer OA PDFs, via Wayback `id_` copies.
- De Brigard 2010: the author's PDF, via a Wayback copy of people.duke.edu/~fd13.
- Veit 2026: CentAUR (Reading) repository PDF.
- Goldstein & Kirk-Giannini: arXiv 2509.11913.
- SEP "Well-Being": the live HTML.
- Hawkins 2015: OpenAlex abstract.
- Weijers 2011/2014: Weijers's own 2018 workshop slides (Waikato research commons).
- Crossref for every DOI.

## Pessimistic Analysis Summary

### Critical Issues Found (all fixed)

**C1. De Brigard 2010 result reported in the wrong direction (L62).** The article had "De Brigard (2010) found most participants would stay plugged in once told they already were". The raw paper gives Neutral 54% back to reality and 46% remain. Positive was 50/50, Negative (prison) 87% remain, and Second Neutral 59% remain. De Brigard concedes the point himself: "the majority of participants (54%) preferred to go back to a real life they had no information about". "Most would stay" is true only of the prison and second-neutral vignettes. This is a §2.4 step-7 defect: the metadata is correct and the direction is wrong. The 09-06 ledger's "real-correct" line covered metadata only.
→ "Told they were already plugged in, De Brigard's (2010) participants split roughly evenly, and 87% stayed when real life was a prison; Weijers (2014), controlling for status-quo bias, found much the same."
Weijers check: his slides give "Stranger NSQ vs. Nozick's = 40% difference" against Nozick's 84% for reality, so Stranger NSQ lands near 44/56. "Roughly even" holds. Note that the NSQ choice is made on behalf of a stranger.

**C2. A spliced quotation with the wrong locator (L72, Lee 2025).** The article had "only conscious entities benefit from the satisfaction of those desires" (2025, n. 25). The raw text reads "but it's only conscious entities that benefit from the satisfaction of those desires". The cleft "it's … that" had been removed inside the quotation marks. The passage is also **body text** in §2 "Anti-Experientialism". Footnote 25 is "See Bradford [2022] for an example of this line of thought", and n. 24 is the Sumner note. The splice and the "n. 25" both came from the research note's "Against Bradford (fn 25)".
→ "it's only conscious entities that benefit from the satisfaction of those desires" (2025). The same sentence's "on which thermostats and bacteria have desires" now reads "can have desires", matching Lee's "can have desires".

**C3. A source/Map conflation: Mogensen 2025b does not generalise Kagan (L80).** The article had "Mogensen (2025b) generalises this into a pluralism". In the raw WP, Kagan appears only in the list of dissenters, in n. 12 ("Similar creatures are imagined by Kagan (2019: 13)") and in n. 20. Mogensen's autonomy is "a psychological capacity for self-government", drawn from Quinn's morality of respect, not Kagan's behavioural agency. And in 2025a Mogensen explicitly declines Kagan's lesson ("I share the intuition … However, I don't agree with the l[esson]").
→ "Mogensen (2025b) defends a pluralism on a richer ground — autonomy, a capacity for rational self-government, can confer moral status without welfare subjectivity — while noting …"

**C4. Internal logic error: "the pluralism collapses into sentientism" (L82).** Mogensen 2025b §4.2, "The Argument from Vulcanity", rests on Chalmers's Vulcan: "a conscious creature … incapable of experiencing any affective states. … Artemis might well be imagined as a Vulcan". If autonomy entails phenomenal consciousness, then, the result is a *consciousness* requirement, not sentientism, and the affectless Vulcan still has standing. That is the Vulcan limb [P-MS1](/positions/moral-status/#p-ms1) already lists, on which the Map bites the bullet (`concepts/sentientism` ^vulcans). Any reviewer who accepts the tenets would flag the original sentence, because it claimed the reply restored valence-necessity.
→ "Second, autonomy entailing phenomenal consciousness would preserve necessity only as a consciousness requirement: Mogensen's test case is Chalmers's affectless Vulcan, on which the Map [bites the bullet](/concepts/sentientism/#vulcans); its agency material treats genuine agency as felt authorship …" The residue is now a framework-boundary marking (Mode Three) rather than a claimed collapse.

**C5. An exploratory position presented as a commitment: Lee's reversal (L56).** The article had "Lee reverses it: a good must …". Lee's own words are "Let me offer a speculative hypothesis, if only to exemplify why I think the philosophical space is underexplored … The reader may decide for themselves whether the principle is plausible". His stated thesis is only that "it's not obvious that either theory is explanatorily prior".
→ "Lee's speculative hypothesis reverses it: if a good must 'affect whatever property makes x a welfare subject', the subject theory explains experientialism (2025)."

**C6. Boundary substitution in the Tenet 5 paragraph (L94).** The article had "Read as parsimony arguments — one declining to multiply welfare subjects beyond the conscious, the other counting theories as if convergence among them were evidence — both are the appeal the tenet disarms." Neither paper argues from economy. Control-checked grep: parsimon / simplic / Occam / Ockham / economy / fewer / multiply all return 0 in Veit (3457 words, "consciousness" 59 hits) and in G&K-G (12,626 words, "wellbeing" 117 hits). G&K-G's only "simpler" is a local limit on crediting microbes with desires. So the paragraph disposed of G&K-G by the tenet when their actual answer, Lee/Veit's decoupling, is already on the page.
→ "Neither rests its case on economy, and the tenet bars the Map from supplying one: that a census confined to conscious subjects is leaner is no evidence that it is right. The Map's 'no consciousness, no welfare' is held on its value premise; …"

**C7. Position strength: Mogensen's Samsung line misdescribed as "his reductio" (L74).** In the raw text the corporation worry motivates *a* reductio response ("An alternative response is to treat the argument as a reductio"). Mogensen then sets that response aside: "Rather than following the argument where it leads or treating it as a reductio, we might instead deny that Kagan and Bradford reason correctly".
→ "the corporation case he raises is the Map's gift — corporations desire in the behavioural sense, and 'we do not feel sympathy for Samsung'".

### Medium Issues Found (fixed)

- **M1. Lead truncation risk (L36).** "The *global* requirement is Eden Lin's supervenience thesis" could be read, if the page is cut off after one paragraph, as Lin holding it.
  → "the supervenience thesis Eden Lin formulates and rejects". This is supported by Lin's 2021 abstract ("no compelling case can be made for the requirement"), Lin 2026's abstract (real lives are better "than phenomenologically indistinguishable lives spent inside experience machines") and Lin 2016.
- **M2. "Lee says the question was malformed" (L54).** Lee says no such thing. His words are "the dialectical picture is more complex than what the authors above have assumed" and "a common thread is that they all assume …".
  → "Lee rejects a premise both sides share."
- **M3. Tenet 1 sentence attributed the phenomenal reading to Mogensen (L90).** "the phenomenal reading of 'felt attitude' that Lin's mechanism and Mogensen's rely on" credits Mogensen with that reading. Mogensen in fact gives "at least modest credence" to unconscious emotion.
  → "the phenomenal reading of the attitude on which Lin's mechanism and Mogensen's both turn."
- **M4. "unconfronted anywhere on the Map" (L60).** This is now false: this article confronts the machine, and `meaning-of-life` L85 engages Metz's use of it. It also sat uneasily with L64's "the meaning article makes the sibling move". Cut, −5 words.

### Trims (length-neutral payment)

- L62: "What the machine world lacks is another mind aware of you." (−11). It duplicated L64's "In the machine no second subject is conscious of you".
- L96: "[P-MS1](/positions/moral-status/#p-ms1)'s *Depends on* and its agency-pluralism rival both landed after this article." (−13). This was a dated process note. Fence (iv) is still carried by L56's "That is a decision the positions register owes" and by L96's surviving sentence.
- L46: "One consequence is a mis-gloss corrected here: the sentientism article called …" → "The sentientism article once mis-glossed Lin's alternative as …" (−5). `concepts/sentientism` no longer contains "desire-satisfaction theory" (0 hits), so the past tense is now accurate.

### Counterarguments Considered

- Lin on the global requirement: bedrock, per the 09-06 stability note. Not re-flagged.
- Nozick: the cost paragraph (L66) is untouched, and the reply is still not claimed as a refutation.
- Unconscious affect: still the conceded draw.

## §2.4 Publisher-of-Record Citation Ledger

- Bradford 2023, *Noûs* 57(4) 905–921 — real-correct (Crossref; abstract verbatim: "the View", "objectionably 'consciousist'")
- Crisp 2026, SEP "Well-Being" — real-correct ("substantive revision Tue Jan 13, 2026"; © Roger Crisp). The passage reads "consciousness can be valuable for non-hedonic reasons (see Kraut 2018; Kriegel 2019)". The article cites only Kraut, which is an incomplete citation, not an error. Left alone.
- De Brigard 2010, *Phil Psych* 23(1) 43–57 — **metadata real-correct; result direction WRONG → fixed (C1)**
- Goldstein & Kirk-Giannini 2025, *Asian J Phil* 4(1), art. 25 — real-correct. The abstract claim matches the arXiv text verbatim. No parsimony argument (C6).
- Hawkins 2015, Routledge Handbook — real-correct. The OpenAlex abstract confirms "no obvious way to do this without begging the question against the hedonist". Pages are unresolved (ch29 371–381 vs -34 355–365, two DOIs), and the article gives none.
- Kagan 2019 — real-correct. p. 20 ("dispositions to act in ways that tend – according to one's beliefs – to bring about specified states of affairs"), p. 28 (the robot quote) and p. 33 are all verified verbatim in Mogensen's WP with those page cites. The channel attribution is kept.
- Kraut 2018 — real-correct (SEP bibliography)
- Kriegel 2026 — real-correct. The title is from Lee's bibliography. The volume was published 3 Sep 2026, per the 10-06 review; Google Books was not re-run because the API quota is zero. The quote is verified in Lee (§2, "in discussing why zombies aren't welfare subjects").
- Lee 2025, *Phil Imprint* 25 — real-correct metadata (Crossref: Andrew Y Lee, Toronto). Quotes: capacity-version ✓, "logically independent" ✓, weight/mass ✓, Kriegel ✓, "affect whatever property makes x a welfare subject" ✓ (C5 context), houseplant ✓, "the same full-blooded sense of 'welfare'" ✓, n. 23 Lin ✓ (Lee's "Lin [2020]" is *The experience requirement on well-being*). The thermostat quote was **spliced and mislocated → fixed (C2)**.
- Lin 2016, *Utilitas* 28(3) 314–332 — real-correct (Crossref abstract)
- Lin 2017, *Noûs* 51(2) 354–377 — real-correct (Crossref, DOI 10.1111/nous.12131)
- Lin 2018, *Ethics* 128(2) 320–345 — real-correct. The abstract matches "Invariabilism is the view that the same theory of welfare is true of every welfare subject".
- Lin 2020a, *PPR* 100(3) 510–524 — real-correct. The p. 520 quote is verified in Mogensen's WP as "(Lin 2020a: 520)". Mogensen's 2020a is this paper and his 2020b is Lin 2021, which explains the article's orphan "a" suffix (harmless).
- Lin 2021, *Phil Studies* 178(3) 867–886 — real-correct (Crossref; online 2020-05-07). No abstract via Crossref, OpenAlex or Semantic Scholar (publisher-elided). The research note's verbatim abstract is consistent with the PhilPapers summary.
- Lin 2026, *PPR* 112(2) 346–357 — real-correct (Crossref abstract)
- Mogensen 2025a, *Phil Studies* 183(2) 511–529 — real-correct (Crossref: print 2026-02, online 2025-12-20). The quotes verified in the WP are: "partly constituted by a certain kind of phenomenology…", "recommend that we follow where it leads", "it isn't plausible that the satisfaction of merely behavioural desires is a welfare good", "at least modest credence", "We do not feel sympathy for Samsung", and "What does the work … saliently lack (pace Gilbert 2002): namely, emotion" (the ellipsis correctly elides "(pace Gilbert 2002)"). The Samsung *framing* was wrong → fixed (C7).
- Mogensen 2025b, *PPR* 111(1) 343–365 — real-correct metadata. The "generalises" framing was wrong → fixed (C3), and the consequence drawn from it was wrong → fixed (C4).
- Nozick 1974; Rawlette 2016 — real-correct. Rawlette is paraphrase-only per the 09-06 fence; not re-verified, since no raw text is reachable.
- van der Deijl 2019, *Phil Studies* 176(7) 1769–1787 — real-correct. Re-verified in the published PDF: "much less strong than it has long been seen", the Lin 2016 concession, the "broader experientialism" quote, "novelty … compassion … self-understanding" (split by footnote 1 across raw lines 82/101), and "pluralistic experientialism" (2 hits).
- van der Deijl 2021, *Phil Studies* 178(1) 187–208 — real-correct. Re-verified in the published PDF: the n. 2 definition, "a highly basic belief, and is therefore difficult to argue for" (the ellipsis correctly elides "is"), (3) and (4) verbatim, "knowledge, achievement, and friendship", and "Consider Chalmers's (1996) philosophical zombie".
- Veit 2026, *Asian J Phil* 5(1), art. 18 — real-correct. Veit's own sentence, quoting G&K-G p. 15, is "I hold that 'that consciousness is required to be a welfare subject even if it is not required for the possession of particular welfare goods'".
- Weijers 2014, *Phil Psych* 27(4) 513–535 — real-correct. "Roughly even" is supported by the author's own slide figures; the paper itself was not obtained.

**Coverage**: 24 quoted spans, all grep-matched in raw text after the fixes. Two had defects: the Lee splice (C2) and the Samsung framing (C7), whose words were verbatim but whose role was misdescribed. Zero fabricated.
**Coiner check**: "experience machine" is Nozick's; "invariabilism" is Lin's (2018); "consciousist" is Bradford's; "welfare neutral" is Lee's (van der Deijl's term was "neutral good") and does not appear in the article. "Chalmers's zombie" follows van der Deijl's own wording ("Consider Chalmers's (1996) philosophical zombie") and makes no claim about who coined the term. It was kept, per the 09-06 stability note, and the zombie is Kirk's coinage (1974) if anyone ever reworks that sentence. The "Vulcan" is credited to Chalmers, its coiner.
**Superlative sweep**: `find_superlative_claims` returned empty.
**Inline ↔ References**: unchanged and complete in both directions. No reference was added or removed. "Chalmers's affectless Vulcan" names the device without a year, and no Chalmers entry was added.

## §2.6 Reasoning-Mode Classification (editor-internal)

- Bradford — Mode One, via Lee's decoupling. Unchanged.
- Kagan (agency) — Mode One, via Mogensen's emotion diagnosis.
- Mogensen 2025b (autonomy pluralism) — **was a claimed collapse, now Mode Three**. The pluralism is met in-framework up to a consciousness requirement. The residue, the affectless Vulcan, is a framework boundary at which the Map bites a declared bullet.
- Goldstein & Kirk-Giannini — **was boundary substitution (C6), now Mode One** through Veit/Lee's decoupling, which denies the premise that whatever can accrue a good is a subject. Tenet 5 is now applied only to the Map's own side.
- Lin, Nozick and Mogensen 2025a — unchanged (Mode Three, Mode Three, and the conceded draw).
- **No label leakage.** All forbidden editor-vocabulary strings, "load-bearing" and "This is not X" return 0.

## Tenet calibration

- Tenet 3 paragraph (L92): already carries the `tenets#^tenet-3-standing` debt sentence, matching the tenet's own wording ("a posit the interface argument leaves open … inherit that debt"). It makes no overclaim and concedes no epiphenomenalism. Untouched.
- Tenet 1 paragraph: "The tenet removes a defeater without supplying the identity thesis" is preserved.
- No five-tier label appears, and no tenet-load upgrade was made.

## Optimistic Analysis Summary

### Strengths Preserved
- The lead's calibration close ("every verdict here holds only as firmly as that thesis").
- The experience-machine cost paragraph (L66).
- The conceded-draw handling of unconscious affect.
- The Lin threat/ally split.
- Lee's weight/mass analogy.

### Enhancements Made
- C4 now connects the agency rival to the Vulcan limb the register already holds. That makes the article's account of [P-MS1](/positions/moral-status/#p-ms1)'s rivals consistent with [P-MS1](/positions/moral-status/#p-ms1)'s own Would-shift-if.
- C6 replaces a forced Tenet 5 application with an accurate one: the tenet constrains the Map's own reasoning, not the opponents'.

### Cross-links Added
- [sentientism](/concepts/sentientism/#vulcans) (L82). It renders as `/concepts/sentientism/#vulcans`, and the target `<span id="vulcans">` is present in the Hugo copy.

## Remaining Items

None for this article. The leads for other pages are listed in this session's changelog entry. They were not minted as tasks, because they sit in positions files owned by positions-evolve.

## Stability Notes

- **De Brigard's figures are now exact** (54/46 neutral, 50/50 positive, 87% remain in the prison vignette). Do not restore "most would stay". It is true of the prison vignette only, and De Brigard himself concedes the neutral majority for reality.
- **The Lee thermostat sentence is body text in §2, not n. 25.** Do not restore the footnote locator, and keep "it's only … that" inside the quotation marks.
- **Mogensen 2025b's autonomy is not Kagan's agency.** Do not write "generalises". The autonomy-entails-consciousness reply reaches only a consciousness requirement; the Vulcan residue is answered by the bitten bullet, not by "collapse into sentientism".
- **Lee's reversal is a speculative hypothesis**, in Lee's own words.
- **Neither G&K-G nor Veit argues from parsimony.** A future pass should not reinstate a "read as parsimony" framing.
- The 09-06 stability notes still hold: "pluralistic experientialism" is van der Deijl's own term (re-verified, 2 hits), Chalmers's zombie is van der Deijl's own example, and Lin's disagreement is bedrock.