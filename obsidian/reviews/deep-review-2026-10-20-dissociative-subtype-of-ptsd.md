---
title: "Deep Review - The Dissociative Subtype of PTSD and the Overmodulation Model"
created: 2026-10-20
modified: 2026-10-20
human_modified: null
ai_modified: 2026-10-20T10:55:29+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-20
last_curated: null
---

**Date**: 2026-10-20
**Article**: [[dissociative-subtype-of-ptsd|The Dissociative Subtype of PTSD and the Overmodulation Model]]
**Previous review**: Never (article created 2026-10-20 ~01:40Z by expand-topic from [[research/dissociative-subtype-of-ptsd-2026-10-09]]).

**Word count**: 3,256 → 3,281 (+25; concepts soft 2,500 / hard 3,500; `soft_warning` both before and after). Prose is about 2,200 words. The excess over soft is reference apparatus.

## Verification Method

Every DOI was resolved at Crossref. Abstracts for 24 papers were fetched raw from PubMed (efetch). Full texts were grep-checked where the quotation sits outside the abstract: Brewin et al. 2025 (UCL accepted manuscript, pdftotext), Dimitrova et al. 2023 (PMC9975991), Huntjens et al. 2022 (PMC9647544), Eder-Moreau et al. 2022 (PMC9234306), Lanius et al. 2010 (PMC3226703 author manuscript) and Reinders et al. 2022 (Amsterdam UMC repository PDF). For Shaw et al. 2023 the preprint abstract came from the OSF API. Quotations were matched by script after normalising whitespace and quote marks. The script also searched every other source, which is how the 70%/30% quotations were placed in Lanius 2002 rather than Lanius 2010. A deliberate miss ("with dissociative symptoms" is absent from Eder-Moreau) confirmed that the matcher can fail.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Attribution error, L87**: "Both sides call for a study of PTSD with and without dissociative amnesia". Huntjens et al. 2022 call for no such study; the full text was searched for "without", "future", "should" and "recommend". Only Reinders et al. 2022 recommend it, and their wording is "a study in PTSD with and without dissociative features is recommended to investigate if the association between CA1 volume and dissociative amnesia still holds". The research note (L197, L234, L270) carries the same error, so the article inherited it. **Fixed**: "Reinders et al. recommend the study that would test the PTSD confound, PTSD with and without dissociative features; none was found." The absence claim was re-checked with two PubMed searches, and neither returned a structural study of PTSD with versus without dissociative amnesia.
- **Dropped qualifier and superlative currency, L48**: "The largest prospective study to date scanned 145 survivors". The source's own phrase is narrower: "the largest prospective longitudinal biomarker study of persistent dissociation to date" (2022). It is a self-description, and its currency is unverified. **Fixed**: "A prospective study scanned 145 survivors".
- **Superlative drift, L60**: "The largest whole-brain resting-state study (197 participants)". The preprint says "the largest region of interest (ROI)-to-ROI analysis performed on a PTSD population to date", so the scope changed and the claim's currency is unknown. **Fixed**: "A whole-brain resting-state study of 197 participants".
- **Calibration (internal tension), L58/L66/L91**: L91 stated the defence-cascade account as fact ("The protectiveness is the passive end of an evolved defence cascade") and said the subtype literature "closes" the selectivity question. The article's own ledger reports the autonomic null (Beutler 2022), but L66 described every failure as being about "which circuitry implements the state". Beutler's review targets the passive-defence marker directly: "It is currently assumed that the initial passive reaction to a threat may coincide with a blunted autonomic response" (abstract), and Terpou 2019 defines passive defence by "decreased expression of the sympathetic nervous system". A reviewer who accepts the tenets would still flag "closes" as overstated, because the rival's functional rationale has lost its physiological marker. **Fixed**, three ways. (a) The ledger now reads "Passive defence predicts hypoarousal, but a systematic review of 28 studies found…". (b) L66 now reads "They concern how the state is implemented, not whether a brain-only account of it exists" and keeps "a less tidy rival is still a rival". (c) L91 now reads "tips it against the Map. On the rival's account, the protectiveness is…". **The verdict is unchanged**: the point still goes to the rival, the interface reading gains nothing, and the lead keeps "the point now belongs to the rival", which matches the description's "moves".
- **Accommodation stated as prediction, L36**: "The model predicts that datum from its core". The article's own history says the model "then acquired a reason" (Terpou 2019), and L93 already says "reaches it from its core". **Fixed**: "predicts" → "reaches" (0 words).

### Medium Issues Found

- **Unattributed quotations, L46**: the 70%/30% quotations were uncited in their sentence and read as the 2010 paper's words. They are verbatim in the Lanius 2002 abstract. Lanius 2010 paraphrases them differently: "Approximately 70% of patients had the subjective experience of reliving". **Fixed**: "Pilot work with script-driven trauma imagery, reported by Lanius et al. (2002), found that…", followed by "Their fMRI experiment then found…", with the trailing cite removed.
- **"the 2002 pilot", L56**: the 2002 paper is the fMRI study, and the pilot work was earlier. **Fixed**: "the 2002 study".
- **Treatment scope, L62**: Hoeboer 2020 covers psychotherapy only. Brewin's "may respond less well" covers psychotherapy and pharmacological treatment. **Fixed**: "21 psychotherapy trials" and "for psychotherapy the effect is small or null".
- **Chiba fidelity, L64**: Chiba et al. 2021 measure the overmodulatory pole as attentional bias away from threat and avoidance symptoms, not dissociation. They only suggest the model "may help elucidate" the subtype difference. **Fixed**: "…within the same patients, though their overmodulated pole is avoidance rather than dissociation." The next sentence, "Read that way…", still refers to the alternation model.
- **Word-sense collision, L79**: the article said Lotfinia's result that dissociative processing "cannot be localized" favours "Knappik's localist reading", which uses "local" in two opposite senses. **Fixed**: "Knappik's type-specific reading" (Knappik's own term, as used by the depersonalisation page; 0 words).

### Citation Ledger (publisher of record)

- APA 2013 via Eder-Moreau et al. 2022 (*Front Psychiatry* 13:862476): real-correct. Both specifier quotations appear verbatim in PMC9234306.
- Beutler et al. 2022 (*EJPT* 13(2):2132599): real-correct. 28 studies; both quotations are in the abstract. Result direction: null for hypoarousal.
- Brewin et al. 2025 (*World Psychiatry* 24(1):52–80): real-correct. All six quotations are verbatim in the UCL accepted manuscript. Stance: a clinical review, with no metaphysical commitment.
- Burton et al. 2018 (*JCCP* 86(5):439–451): real-correct. The quotation is in the abstract, and the direction (higher re-experiencing) is correct.
- Chalavi et al. 2015 (*HBM* 36(5):1692–1704): real-correct. The quotation is in the abstract, and PTSD-only patients with childhood trauma had smaller volumes.
- Chiba et al. 2021 (*Mol Psychiatry* 26(9):5023–5039): real-correct metadata. The fidelity defect is fixed (see above).
- Dimitrova et al. 2023 (*Psychol Med* 53(3):805–813): real-correct. The comorbidity sentence and the control exclusion "a history of trauma" are both verbatim in the full text.
- Felmingham et al. 2008 (*Psychol Med* 38(12):1771–1780): real-correct. 12 vs 11 patients; both quotations are in the abstract. The abstract also reports *enhanced* amygdala, insula and thalamus activity to non-conscious fear. The article's "only during conscious processing" covers this.
- Frewen et al. 2015 (*EJPT* 6:26406): real-correct. N = 557, and the factor names are verbatim. Crossref confirms that Knappik's reference list includes it.
- Hoeboer et al. 2020 (*BJPsych Open* 6(3):e53): real-correct. 21 trials, 1,714 patients; the null result is verbatim (r = 0.04).
- Huntjens et al. 2022 (*Psychol Med* 52(13):2835–2836): real-correct. The quotation is verbatim in the full text. The attribution error is fixed (see above).
- Knappik 2025/2022 (*Phenom Cogn Sci* 24(2):411–435): real-correct metadata at Crossref.
- Kozlowska et al. 2015 (*Harv Rev Psychiatry* 23(4):263–287): real-correct. The source has "responses of last resort to inescapable threat".
- Lanius et al. 2002 (*Biol Psychiatry* 52(4):305–311): real-correct. 7 PTSD vs 10 controls; the 70%/30% quotations are verbatim in this abstract. The attribution is fixed.
- Lanius et al. 2010 (*AJP* 167(6):640–647): real-correct. Three quotations are verbatim in the abstract. It cites Sierra & Berrios 1998 (reference 34 in the PMC author manuscript).
- Laurin et al. 2026 (*Neurosci Biobehav Rev* 182:106546): real-correct. The quotation is in the abstract, and the work is "a novel theoretical framework".
- Lebois et al. 2022 (*AJP* 179(9):661–672): real-correct. N = 145, scanned 2 weeks post-trauma; the quotation is verbatim. The superlative is fixed.
- Lotfinia et al. 2020 (*J Psychiatr Res* 128:5–15): real-correct. 33 articles; both quotations are in the abstract.
- Nicholson et al. 2017 (*HBM* 38(11):5551–5561): real-correct. N = 155 (62 PTSD, 41 PTSD+DS, 52 controls); both quotations are verbatim.
- Reinders et al. 2022 (*Psychol Med* 52(13):2837–2845): real-correct. "Here, we agree" and r = −0.398 (p = 0.015) are verbatim in the repository PDF.
- Shaw et al. 2023 (*Nature Mental Health* 1(10):711–721): real-correct metadata. The quotation and N = 197 are verbatim in the OSF preprint abstract (flagged on the page). The superlative is fixed.
- Sierra & Berrios 1998 (*Biol Psychiatry* 44(9):898–908): real-correct. The quotation is in the abstract.
- Stein et al. 2013 (*Biol Psychiatry* 73(4):302–312): real-correct. 25,018 respondents in 16 countries, 14.4%, and the quotation are verbatim.
- Terpou et al. 2019 (*J Neurosci Res* 97(9):1110–1140): real-correct. The quotation is verbatim in the abstract, and the paper comes from the Lanius laboratory.
- Weniger et al. 2008 (*Acta Psychiatr Scand* 118(4):281–290): real-correct. n = 13; the quotation is verbatim.
- White et al. 2022 (*Psychol Med* 52(9):1629–1644): real-correct. 49 studies, N = 8,214, 38.1%, 22.8% and 48.1% all match, and the quotation is verbatim.
- Inline ↔ References: no orphans in either direction. Entries 27–28 are Map self-citations.
- **Cited-author stance**: Lanius, Nicholson/Friston, Terpou, Laurin and Chiba all build brain-only models and are engaged as rivals, which the page states (L50). Brewin, Stein, White, Beutler and Hoeboer are clinical empiricists, and none is recruited for the Map.

### Reasoning-mode classification (editor-internal)

- Engagement with the overmodulation model: Mode Three for the bare Dualism thesis. The article honestly declares that the model "does not say why inhibited limbic output should feel unreal". On trauma-selectivity it concedes rather than refutes, the correct move inside the Map's own evidential discipline.
- The three co-optation traps are intact and correctly reasoned: "top-down" names a direction within the brain; "only during conscious processing" is an access-level finding, since backward masking changes global availability; and inhibition means more coupling, not disconnection.
- No label leakage. Grep for the forbidden vocabulary, "load-bearing" and the "This is not X" construction found 0 hits.

### Counterarguments Considered

- Physicalist (Dennett/Churchland): the page already concedes the point. The bare Dualism residue ("why inhibited output should feel unreal") is a framework-boundary claim and is not dressed as support.
- Empiricist (Popper): the accommodation-versus-prediction slip in the lead is fixed. The dynamic alternation model "survives" the co-elevation datum only in the sense of being consistent with it, and the Chiba qualifier now marks that its tested pole is avoidance.
- Buddhist (Nagarjuna): the page makes no claim that a persisting self is shown. The mine-ness standoff is explicitly left untouched.

## Optimistic Analysis Summary

### Strengths Preserved

- The ledger structure ("What Held and What Did Not") separates the held class and prefrontal signal from the failed autonomic, circuitry, treatment and mirror-image predictions. Each failure is then denied to the Map ("a less tidy rival is still a rival").
- The concession is made at full strength and scoped to depersonalisation and derealisation, with amnesia and DID explicitly not examined.
- The hippocampal specificity section uses Weniger's no-PTSD group and Dimitrova's own exclusion criteria to show the rung stands while its specificity does not.
- The Occam's Razor paragraph is applied symmetrically, to the rival's tidiness as much as to the Map's single-channel phrasing.
- The three co-optation traps are the page's most reusable contribution to the corpus.

### Enhancements Made

- Two fidelity tightenings: Chiba's pole and the psychotherapy scope.
- The verdict wording is recalibrated ("tips", "On the rival's account") without moving the point back toward the Map.

### Cross-links Added

- [[predictive-processing]]: a zero-word link on "predictive-processing form" (L50).
- [[phenomenal-output-causal-machinery-dissociation]]: a zero-word piped link on "four-level dissociation chain" (L95). This page's L187 states the chain. The evidential-status-discipline anchor was tried first and dropped, because its five anchor words count toward `analyze_length`.

## Remaining Items

- None on this page. Side lead: the research note's claim that "both sides call for" the PTSD with/without study is wrong (see Critical Issues). The note was not edited.

## Stability Notes

- The verdict, that the trauma-selectivity point for depersonalisation goes to the brain-only rival and the Map keeps only the bare Dualism thesis, is calibrated correctly and binding. Future reviews should not soften it further or restore "closes". The 2026-10-20 change from "closes" to "tips" registers the autonomic null's effect on the defence-cascade marker and does not reopen the question.
- The rival's circuitry failures give the Map nothing ("messier, not absent"). Do not re-flag this as under-crediting the Map.
- The physicalist complaint that the bare-Dualism residue is an appeal to the explanatory gap is a framework-boundary disagreement, not a defect.
- The Shaw 2023 quotation is flagged as preprint wording. Re-verify it against the published abstract if one becomes retrievable, but it is not a defect.

## Cross-review (integration), 2026-10-20 ~10:55Z

Integration-only pass, run as the expand-topic chain successor. The content fixes above were not reopened, and no second citation pass was run. The three co-optation traps (L100–102) and the verdict ("tips it against the Map"; "messier, not absent"; bare Dualism untouched) were re-read and are intact. The page body is unchanged, so `ai_modified` and `last_deep_review` keep their 10:33Z values.

**Inbound links (before → after: 2 → 3)**

- Existing, `[[concepts/depersonalisation]]` L57, anchor "post-traumatic numbing" (3,498 / 3,500, link-only). It matches page L80, which locates the numbing point in this field. It is not cited as Map support. Untouched.
- Existing, `[[topics/clinical-dissociation-as-systematic-evidence]]` L147, anchor "an affective-salience physicalism" (4,688, over the 4,000 hard threshold, link-only). It points at the rival account. Untouched. A lead is noted below.
- **Installed**, `[[concepts/metacognitive-access-versus-retention]]` L131: `[[dissociative-subtype-of-ptsd#the-hippocampal-question|not shown to be specific to DID]]` (3,216 → 3,216, +0). The host sentence already states the PTSD confound on Dimitrova 2023, and it is the confound that the page's Hippocampal Question section develops ("That rung stands; its specificity does not"). The link carries a specificity *caveat*, not support for the Map. Spot-check of the host's dependency: Dimitrova 2023 at PubMed (PMID 34165068) has "32 with DID and 43 matched healthy controls". 29 co-morbid plus 3 remitted equals 32, so the host's "Every patient… current or remitted PTSD" holds. The slug-dialect anchor was used because `count_words` splits on whitespace, and the heading-text form would add 2 words.

**Candidates rejected**

- `concepts/mine-ness` (3,499 / 3,500): no trauma, PTSD or subtype text. Its depersonalisation and Knappik passages (L72, L92) concern *what* comes apart, which page L82 leaves untouched.
- `topics/conversion-disorder-as-consciousness-side-fault` (3,814): the only dissociation passage (L115) is about FND comorbidity rates. The coupling-not-disconnection point is the page's own outbound link (L102) and has no host text there.
- `project/architecture-vs-significance-two-tier-discount` (3,612, over hard): its depersonalisation text (L41, L67) concerns mine-ness separability, not the subtype.
- `topics/clinical-dissociation-as-systematic-evidence` L88 (the Sierra–Berrios corticolimbic model): DPDR-specific, and the flagship already links the page at L147.
- `concepts/depersonalisation` L55 (Sierra–Berrios): excluded by the brief (touch only L57).
- `topics/clinical-phenomenology-and-altered-experience` (3,711): its depersonalisation section (L105) has no trauma content.
- `topics/phenomenology-of-forgetting` L79/L131 and `concepts/mental-imagery` L65: the PTSD mentions concern memory suppression and flashbacks, not the dissociative subtype.
- `project/evidential-status-discipline` L283: about the flagship's DID atrophy claim, not the subtype.

**Outbound / Further Reading.** Every inbound host (depersonalisation, the flagship, metacognitive) is already linked from the page's body and Further Reading, so no reciprocal is missing and the page was not edited.

**Lead (not actioned).** The flagship L147's closing clause, "which framework earns it the clinical data do not settle", now understates this page for depersonalisation and derealisation, where the subtype literature tips the point to the rival. The clause is accurate only for amnesia and DID, which are not examined here. The host is over its hard threshold, so any rescoping must be length-neutral (a refine-draft clause swap). It must also respect this page's calibration: scope the open choice to amnesia and DID, and do not restate it as settled for the Map.
