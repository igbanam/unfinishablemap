---
ai_contribution: 100
ai_generated_date: 2026-10-13
ai_modified: 2026-10-13 00:02:15+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-13
date: &id001 2026-10-13
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-13 00:02:15+00:00
modified: *id001
related_articles: []
title: Deep Review - Clinical Evidence Quality Standards in Consciousness Research
topics: []
---

**Date**: 2026-10-13
**Article**: [Clinical Evidence Quality Standards in Consciousness Research](/topics/clinical-evidence-quality-standards-consciousness-research/)
**Previous review**: [2026-07-28](/reviews/deep-review-2026-07-28-clinical-evidence-quality-standards-consciousness-research/)

## Scope and Selection

This is the seventh review. The selector's top picks (graduated-middle-path, the four new files of 2026-10-12, q3-q4, pupillometry, islamic-sufi, quantum-non-equilibrium) were all created, edited or reviewed on 2026-10-12, so they were skipped. This article was the highest-scoring eligible candidate with substantive, never-reviewed changes since its last deep review:

- `5f05958b54` (09-02): the Nakatani 2003 narrowing of "never independently replicated" at Standard 1.
- `70863a06c5` (09-07): a whole new **Unblinding Problem** subsection (~700 words), eleven new references (refs 17–27), four verbatim quotations, a Standard 2 extension and a retraction example in "Selective citation".
- `76f8f15aac`/`703cfd47d4` (09-25/27): the sham-neurofeedback clause in "The missing comparator".

The 07-28 pass was currency-only and predates all of these. No deep review has examined the new material until now. The 07-28 stability notes were read and respected: the Kerskens/Wiest wording and the DoC scoping were not touched.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Van Elk & Yaden (2022) misrepresented (attribution / position-strength).** The article said the review "affirms genuine mechanisms at three levels" and that "what bites is its preference for pluralistic causation over a unifying account: where several mechanisms each suffice to explain a phenomenon, no one of them is uniquely supported by it."
   - The source reviews "several *possible* mechanisms".
   - The source explicitly states "we support efforts to discover a comprehensive theory of how psychedelics exert their effects". It says only that "the field may need to look to pluralistic models of causation". That is not a preference.
   - It defines pluralism as "multiple complementary pathways are *necessary*", which is the reverse of the article's "several mechanisms each suffice".
   - The source does carry the interpretive-range point the article wanted, in its own words: existing theories "are currently underdetermined by the data".
   - **Fix**: "surveys candidate mechanisms"; the final sentence was rewritten as its "caution about a unifying account", with the two verbatim phrases, followed by "The filter reading is then not uniquely supported." All six phrases were grep-verified in the open-access CC-BY PDF (Leiden repository, hdl 1887/3515020), with soft hyphens and line breaks normalised.
2. **Butler, Jelen & Rucker (2022): dropped qualifier.** The source says trials "are *likely* to significantly overestimate treatment effects by design"; the article had "granting that these trials overestimate by design". **Fix**: "likely overestimate".
3. **Magnetoreception calibrated above the Map's own register.** L152 said quantum biological effects "are established in … avian magnetoreception". The positions register (`positions/quantum-interface` [P-Q8](/positions/quantum-interface/#p-q8), band review 2026-10-11) grades cryptochrome radical-pair magnetoreception as "a leading model unsettled in vivo". "Established" sits one tier higher, in the very section that turns the five standards on the Map's own quantum claims. A tenet-accepting reviewer would flag it, so this is a calibration error, not a bedrock disagreement. **Fix**: "established in enzyme catalysis and are the leading account of avian magnetoreception, though unsettled in vivo". Duan 2017 (photosynthesis) was already handled correctly by the 07-30 sweep.
4. **"The Map cites no retracted work" contradicts the article and the corpus.** The article's own ref 27 is a retracted work (Shafiee 2024, cited as an example). `topics/clinical-neuroplasticity-evidence-for-bidirectional-causation` L161 also cites a retracted meta-analysis. The sentence is also an unverifiable universal claim about the whole corpus. **Fix**: clause deleted. The surviving sentence keeps the point: "The obligation is periodic re-checking rather than one-time verification."

### Medium Issues Found

- **Unsupported superlatives at L74.**
  - "The most extreme control-adequacy failure documented in the consciousness-relevant clinical literature" had no source.
  - "Orsini et al. (2026), the first systematic review of blinding integrity" asserted priority in the Map's voice. Orsini's abstract calls itself the "first evaluation of blinding integrity", but Muthukumaraswamy et al. (2021), cited in the same section, "conduct[ed] systematic reviews of psychedelic RCTs" on whether blinding success was reported.
  - The `find_superlative_claims` helper returned empty and missed both.
  - **Fix**: "An extreme control-adequacy failure in …" and "a systematic review of …".
- **Expectancy / phenomenal-character slide, and a soft strawman (L80).** The sentence moved from "phenomenal character does causal work" to "subtracting expectancy subtracts part of the mechanism" without the link. It then said "the orthodox framing forecloses by assumption", but mainstream psychedelic science openly debates whether subjective effects are necessary for therapeutic effect, in physicalist terms. What the drug-versus-placebo design does is set expectancy aside by construction. **Fix**: "part of what trials subtract as expectancy may be mechanism — a possibility [Tenet 3] leaves open and the drug-versus-placebo design sets aside by construction."
- **Szigeti et al. (2021), "what changes when the blind holds".** The abstract reports that the acute microdose–placebo differences "can be explained by participants breaking blind", so the blind held only partly. **Fix**: "holds better".
- **Van Elk & Fried (2023), "sort ten problems … by the kind of validity".** The source groups the problems as easy/moderate/hard and *shows how* each threatens a validity type. **Fix**: "map … onto".

### Low Issues Fixed

- Stray comma before an em dash after the Muthukumaraswamy quote (`expectancy," —`).
- Tegmark was named inline with no year. Now "Tegmark's (2000)", which closes the (surname, year) pairing.
- The bare 10⁻¹³ s at L152 is now scoped as "microtubule". The pairing was already correct (Hagan's revision is of Tegmark's microtubule figure, eq. 22). Without the scope it read like the class-B mislabel the open Tegmark sweep targets. This file is **not** on the batch 2 list.
- Berghofer 2019 pages added (98-117, Crossref).
- Two trims for length-neutrality: "This consistency matters." and the self-praising "The honesty of this position is itself a strength:". The substance of the self-application paragraph is kept.

### Checked and Held (no change)

- **Nakatani 2003, "the lone out-of-group convergence" (09-02 sweep wording).** Checked against Poli et al. 2022, the *Frontiers in Psychiatry* systematic review of CBT neurobiological outcomes in OCD (PMC9780289). The only other out-of-UCLA caudate finding is Freyer et al. 2011 (Lübeck, fMRI), and it runs in the opposite direction (caudate activity *increased*), so it is not a convergence. Rangaprakash 2021 is a UCLA (Feusner) paper. The wording holds.
- **Claims about sibling articles.**
  - `psychedelics-and-the-filter-model` L95 does withdraw "therapeutic durability" on the ground that several mechanisms each predict durable single-dose change.
  - The sham-neurofeedback lead does describe the sham arm as keeping effort and removing the contingency.
  - "the Map's case for bidirectional interaction does not depend on" appears verbatim in `clinical-neuroplasticity` (grep count 1).
- **Orsini figures.** 112 RCTs, 29.5% (n=33), 57.1% (n=64), ">90%" for psilocybin, LSD and ayahuasca among participants and raters, inert-placebo MDMA ">85%", and the closing quote all match the JATS abstract at Crossref verbatim. One nuance is not stated in the article but is not misstated either: 78 of the 112 trials are ketamine trials, and midazolam controls partly preserved blinding there.

### Publisher-of-Record Citation Ledger

Sources: **XR** = Crossref API with every field printed (no author-list slicing). **OA** = OpenAlex abstract inverted index, rebuilt to raw text. **EPMC** = Europe PMC MEDLINE record.

- Schwartz et al. 1996 (*Arch Gen Psychiatry* 53(2):109-113; doi 10.1001/archpsyc.1996.01830020023004) — real-correct (XR; Crossref holds only the first author).
- Kral et al. 2022 (*Sci Adv* 8(20) eabk3316) — real-correct (XR).
- Goyal et al. 2014 (*JAMA Intern Med* 174(3):357-368) — real-correct (XR).
- Van Dam et al. 2018 (*Perspect Psychol Sci* 13(1):36-61; online 2017) — real-correct (XR).
- Varela 1996 (*JCS* 3(4):330-349) — real-correct. JCS has no DOI, and the XR bibliographic query returned a different item, so this rests on the canonical record and is unchanged from 07-13.
- Berghofer 2019 (*Eur J Philos* 27(1):98-117; doi 10.1111/ejop.12405) — real-wrong-metadata (incomplete; pages added) (XR).
- Lazar et al. 2005 (*NeuroReport* 16(17):1893-1897) — real-correct (XR).
- Hölzel et al. 2011 (*Psychiatry Res Neuroimaging* 191(1):36-43; doi 10.1016/j.pscychresns.2010.08.006) — real-correct (XR).
- Schwartz, Stapp & Beauregard 2005 (*Phil Trans R Soc B* 360(1458):1309-1327) — real-correct (XR).
- Southgate & Oquatre-six 2026 — the Map's own article, cited by wikilink; live slug.
- Tegmark 2000 (*Phys Rev E* 61(4):4194-4206) — real-correct (XR); inline year now added.
- Hagan, Hameroff & Tuszyński 2002 (*Phys Rev E* 65(6):061901) — real-correct (XR).
- Kerskens & López Pérez 2022 (*J Phys Commun* 6(10):105001; doi 10.1088/2399-6528/ac94be) — real-correct (XR).
- Warren 2023 (*J Phys Commun* 7(3):038001) — real-correct (XR). Crossref's title has "function" in the singular inside the comment title; this was left as is.
- Khan et al. 2024 (*eNeuro* 11(8), ENEURO.0291-24.2024) — real-correct (XR). The last author is Wiest, so "await independent replication" is exactly right.
- Wiest 2025 (*Neurosci Conscious* 2025(1) niaf011) — real-correct (XR).
- Duan et al. 2017 (*PNAS* 114(32):8493-8498; seven authors as listed) — real-correct (XR). The result direction is confirmed (OA abstract): "rapidly decaying electronic quantum coherence on a timescale of 60 fs … give no hint that electronic quantum coherence plays any biofunctional role".
- Nakatani et al. 2003 (*Psychiatry Res Neuroimaging* 124(2):113-120; doi 10.1016/s0925-4927(03)00069-6) — real-correct (XR).
- Orsini et al. 2026 (*JAMA Psychiatry* 83(7):755-769; subtitle "A Systematic Review"; 18 authors) — real-correct. Pages were confirmed at EPMC, because Crossref and OpenAlex give only "755". All figures and the quote were checked against the XR JATS abstract. "First" was de-superlatived (see Medium).
- Muthukumaraswamy, Forsyth & Lumley 2021 (*Expert Rev Clin Pharmacol* 14(9):1133-1152) — real-correct (XR). The quote is verbatim (OA): "treatment effect sizes in psychedelic RCTs are likely over-estimated due to de-blinding of participants and high levels of response expectancy".
- Szigeti et al. 2021 (*eLife* 10:e62878; eight authors) — real-correct (XR). The result is confirmed (OA): n=191 completed, both groups improved, "no significant between-groups differences". The acute differences are attributed to blind-breaking, which prompted the "holds better" fix.
- Szigeti, Nutt, Carhart-Harris & Erritzoe 2023 (*Sci Rep* 13:12107) — real-correct (XR). The distinction and the modelling are confirmed (OA): computational modelling shows activated expectancy bias "can inflate estimates of treatment effects and create false positive findings".
- Butler, Jelen & Rucker 2022 (*Psychopharmacology* 239(10):3047-3055) — real-correct metadata (XR). The dropped "likely" was restored (Critical 2).
- van Elk & Fried 2023 (*Ther Adv Psychopharmacol* 13:20451253231198466; erratum 10.1177/20451253231223609 linked by an XR update-to) — real-correct. The "ten problems" and the four validity types are confirmed (OA). "sort by" was corrected to "map onto".
- van Elk & Yaden 2022 (*Neurosci Biobehav Rev* 140:104793) — real-correct metadata (XR, OA, EPMC). The **characterisation was wrong** (Critical 1); both quotes are verbatim in the full text.
- Belinger et al. 2026 (*Eur Neuropsychopharmacol* 111:112879; issued 2026-10; eleven authors) — real-correct (XR). OA confirms methylphenidate as an active placebo and that "overall blinding was insufficient".
- Shafiee et al. 2024 (*J Psychopharmacol* 38(5):425-431; seven authors, given names checked) — real-correct (XR). The retraction is confirmed: notice doi 10.1177/02698811251341228, issued 2025-05-15, linked by an XR update-to of type "retraction".

(surname, year) pairs were checked mechanically in both directions. There are no orphans in either direction (Southgate 2026 is cited by wikilink). Empirical-currency helper: empty, but it missed two superlatives at L74 (see Medium).

### Reasoning-Mode Classification (editor-internal)

- **Muthukumaraswamy et al. critique**: Mode One. The article reads their own text ("over-estimated", not "placebo") against the stronger reading of it.
- **Physicalist reply at Standard 3**: Mode Three, an honest boundary marking (unchanged).
- **Van Elk & Yaden's underdetermination**: conceded on its own terms and turned on the Map's own material. It is honest, not boundary-substitution.
- **Label leakage**: none found by grep. There are no "This is not X. It is Y." constructions and zero uses of "load-bearing".

### Cited-Author Stance

- Van Elk & Yaden: naturalistic psychedelic science; framed as "metaphysically neutral".
- Butler et al.: clinical trialists; the inference is marked "the Map's … rather than theirs".
- Schwartz/Stapp/Beauregard: interactionist; their reading is attributed to them.
- Varela: enactivist, not dualist; framed as a pragmatic method.
- Wiest: a quantum-consciousness proponent; framed as awaiting replication.

None of them is presented as endorsing the Map's conclusion.

## Optimistic Analysis Summary

### Strengths Preserved

- **The Unblinding subsection's architecture.** It runs evidence (Orsini), then a conceptual distinction (Szigeti's placebo group versus placebo control), then the critique's own calibration turned back on it (Muthukumaraswamy as recalibration, not refutation), then the counter-pressure (Butler), then the field's response, then a precise statement of what the critique does and does not touch in the Map's own psychedelic material. This is the five standards demonstrated live. The Hardline Empiricist persona would single out the line "The withdrawal was not forced by the blinding literature and should not be presented as a concession to it" as exemplary bookkeeping.
- **The Standard 2 extension**, "a placebo group rather than a placebo control". It is a compact generalisation that carries to any intervention with unmistakable subjective effects, including meditation.
- **All 07-28 strengths**: the quantum-section negative claims ("living neural tissue", "have not been independently confirmed"), the Standard 5 bounded-work paragraph, and the three-part inferential-gap frame. None of them was touched.

### Enhancements Made

- The van Elk & Yaden paragraph now gives the challenge in the source's own words, and it is sharper for it: underdetermination is exactly the interpretive-range standard.
- The magnetoreception line now matches the positions register.
- The microtubule scope protects the decoherence-timescale sentence from a class-B misreading.

### Cross-links Added

None. The article's link set is complete for its declared scope, and the length budget (31 words of headroom) argued against additions.

## Length

3968 words → 3972 words (+4). Hard threshold 4000 (gate `>=`); status `soft_warning`. The work ran in length-neutral mode: the additions ("likely", "better", the van Elk & Yaden rewrite, the magnetoreception qualifier, the Tegmark year, the microtubule scope, the Berghofer pages) were offset by four trims (the retracted-work clause, "This consistency matters.", the self-praise clause, and the two superlatives).

## Remaining Items

None owed in this article.

## Stability Notes

- All 07-28 stability notes stand. Do not "update" the Kerskens claim on the strength of Wiest 2025. The DoC omission is deliberate scoping.
- **Nakatani "lone out-of-group convergence" was checked and holds** against Poli et al. 2022. Freyer 2011 is out-of-group but opposite in direction, and Rangaprakash 2021 is UCLA. Do not re-flag it without a new out-of-group caudate *decrease* finding.
- **The van Elk & Yaden paragraph now quotes the source on underdetermination.** Do not restore "preference for pluralistic causation" or an "each suffices" gloss. The full text supports neither.
- **Magnetoreception wording is tied to [P-Q8](/positions/quantum-interface/#p-q8).** If the open P3 positions-evolve task on Hiscock et al. 2017 recalibrates [P-Q8](/positions/quantum-interface/#p-q8), this line should follow it in either direction.
- Bedrock (unchanged): the unfalsifiability of "the philosophical case remains"; the separable-consciousness presupposition behind the missing comparator; the Western-empiricist framing of evidence hierarchies.