---
ai_contribution: 100
ai_generated_date: 2026-10-11
ai_modified: 2026-10-11 15:42:43+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-11
date: &id001 2026-10-11
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-11 15:42:43+00:00
modified: *id001
related_articles: []
title: Deep Review - Whether Language-Model Words Refer
topics: []
---

**Date**: 2026-10-11
**Article**: [Whether Language-Model Words Refer](/topics/whether-language-model-words-refer/)
**Previous review**: Never (article published 2026-10-11 12:47 by expand-topic)

## Pessimistic Analysis Summary

### Critical Issues Found

- **Reader-route misattribution (L72, source fidelity)**: the article said that reader-centred accounts "such as Cappelen and Dever's (2021)", according to Lederman and Mahowald, "cannot tell a person's sand-writing from the wind's". At p. 1095 Lederman and Mahowald say the reverse about Cappelen and Dever. A *simplistic* interpreter-focused account fails the sand/wind case, but "The more sophisticated approach developed by Cappelen and Dever handles this case" through knowledge maximisation. It fails only on the frog whose croak predicts rain. **Fixed**: the simple account now gets the sand/wind failure, and Cappelen and Dever's knowledge-maximising version gets the frog failure, cited p. 1095. The defect began in the research note (L109), which compressed the two cases into one. The note is corrected too.

No other critical issues. Specifically:
- **Calibration audit**: the verdict is conditioned on [P-AC1](/positions/ai-consciousness-scope/#p-ac1) in the lead, as "low-probability but not ruled out" and "internal to its own framework". [P-AC1](/positions/ai-consciousness-scope/#p-ac1)'s dependence on the quantum-interface programme is disclosed in Relation to Site Perspective. [P-CS7](/positions/consciousness-scope/#p-cs7) ("moderate credence") is the stated basis for Swampman's cell. The dominant-causal-source reply is marked as the Map's own untested proposal, and the cost is stated if it fails. No step uses tenet-coherence to upgrade a tier. `evaluate_anchoring` returns no flags.
- **Method/history necessity vocabulary**: none ("structurally", "inevitable" and "cannot in principle" are absent). "Cannot refer by deference" is a framework-conditional implication of moderate PIT, Kripke's condition and [P-AC1](/positions/ai-consciousness-scope/#p-ac1), and the lead now names Kripke's condition as the premise it rests on.
- **Label leakage**: none.

### Medium Issues Found

- **Asymmetric hedge in the second paragraph**: Swampman "has the conscious source" was unhedged, while the LLM's lack of one was hedged "on the Map's assessment". The sibling [swampman](/concepts/swampman/) says the verdict is only as strong as [P-CS7](/positions/consciousness-scope/#p-cs7). **Fixed**: one "On the Map's assessment" now covers both halves.
- **Kripke's condition stated flatly in the lead**: "because borrowing needs the borrower's own intention". Koch, Cappelen & Deutsch and Pepp all contest this premise, and the Map's tenets do not settle it. **Fixed**: "because borrowing, on Kripke's condition, needs…".
- **"Accepts Koch's argument"**: Koch argues that reference is *transmitted to* the LLM without intentions, which the Map's step 3 denies is borrowing. **Fixed**: "accepts Koch's continuity mechanism and reclassifies what it delivers".
- **Cappelen & Deutsch named as a pro-reference position but never answered**. **Fixed**: one sentence says that, on moderate PIT, deference-free sharing by a system with no phenomenal source is inheritance (a Mode Three reclassification, explicitly framework-conditional).
- **First-person tokens overclaimed** (Tenet 4 paragraph): "first-person words are where derived reference visibly fails". Assistant-tuned models are trained on text whose authors meant "I" to pick out the system, so a derived artefact referent is available. That case is the exception to L72's "designers explain the mechanism, not the referent". **Fixed**: "most strained", and trainers' conventions can at most point "I" at the deployed system, as a talking sign's "I" points at the sign. L72 now says "mostly". The haecceity point stands: there is no subject referent.
- **"Together the cases show that the ordinary speaker needs both halves"**: a framework-conditional illustration presented as a demonstration. **Fixed**: "illustrate why, on the hybrid,".
- **"A conscious LLM would … [be] able to borrow by deference"**: consciousness makes an LLM eligible, not able. Krzanowski 2025 (research note) argues consciousness may not suffice for intrinsic semantics. **Fixed**: "eligible to borrow".
- **Unclear sentence (L114)**: "Nothing has come in to test this; it is unresolved…" had an unclear antecedent. **Fixed**: the paragraph now closes with "No result yet bears on any of the three, so the verdict is untested rather than confirmed."
- **Ostertag "doubts both antecedents"**: Ostertag has one disjunctive antecedent ("my concern is … with the antecedent, about which I have doubts", p. 659). **Fixed**: "its two-part antecedent; each pro-reference position takes one part".
- **Grindrod quotation**: it comes from the footnote that describes "The Evansian picture I consider". **Fixed**: "and, applying Evans, that…". Grindrod's main text (§4.1) endorses the consumer-only status, so the attribution stands.
- **Pepp modality**: the abstract has "whether LLMs *can* achieve". **Fixed**.

### Low Issues Fixed

- Nested double quotes inside the Mandelkern & Linzen "beech" quotation are now single quotes.
- Davidson is now cited inline as (1987), which matches the References entry.
- The lead's "names an LLM coins for itself" could be misread as self-naming. It now reads "new names an LLM coins".
- The Hattiangadi & Schoubye volume title now includes the subtitle *Philosophical Perspectives*, which matches the arXiv title page.
- The duplicate credit sentence at the head of the inverse-Swampman section was folded into the table lead-in. The lead already credits the addition.

### Citation Ledger (§2.4 publisher-of-record web-verify)

Metadata came from Crossref (DataCite for Koch). Every direct quotation was substring-checked against raw primary text fetched this run, after whitespace, quote and ligature normalisation. A planted negative control returned 0. Pages were mapped from PDF page to printed page with `pdftotext -f/-l`.

- Mandelkern & Linzen 2024 (CL 50(3) 1191–1200, doi 10.1162/coli_a_00522). State: real-correct. ACL Anthology PDF; 10 quotations verified. Pages confirmed: 1191 (lead), 1192 (speaker reference), 1193 ("a decisive argument"), 1195 (beech), 1196 (Luke), 1197 ("the key question" for lightweight intention, "We leave this as an open question", children), 1198 (Izzy introduced; "right kinds of experiences"), 1199 ("directly sensitive to his brainwaves", "In the same way…"). The article's "pp. 1198–1199" is correct.
- Kripke 1980 (*Naming and Necessity*, HUP). State: real-correct. archive.org djvu text; the quotation sits under the running head "96 NAMING AND NECESSITY".
- Ostertag 2025 (CL 51(2) 651–659, doi 10.1162/coli_a_00551). State: real-correct. Pages 652 (ineliminable), 656 (water/oxygen, Earthians, so human speakers) and 659 (conditional). Antecedent wording adjusted (see Medium).
- Lederman & Mahowald 2024 (TACL 12 1087–1103, doi 10.1162/tacl_a_00690). Metadata real-correct. ACL Anthology PDF; 5 quotations verified at 1087 (abstract, "differs sharply…"), 1088 ("These new names…"), 1090 (bibliotechnism), 1091 (sand) and 1098 (conclusion). The Marion Starlight details (18th century, pamphlet, Committee of Public Safety, Thermidorian Reaction) are at p. 1093. **Framing defect at p. 1095 fixed** (see Critical).
- Cappelen & Dever 2021 (*Making AI Intelligible*, OUP, doi 10.1093/oso/9780192894724.001.0001). State: real-correct. arXiv 2406.08134 OA PDF; the principle quotation carries book folio 111.
- Cappelen & Deutsch 2025 (*Oxford Handbook of Contemporary Philosophy of Language*, 241–257, doi 10.1093/oxfordhb/9780192856852.013.33). State: real-correct. Quotation verified against the OpenAlex abstract.
- Chalmers 2023 (*Proc. & Addresses APA* 97, 22–45). State: real-correct. The arXiv 2408.09605 PDF carries journal pagination. "pure thinkers would be conscious" is on p. 31 and "require separate treatment" on p. 38. Context checked: the listed arguments run from "lack consciousness or communicative intent" to "stochastic parrots".
- Coelho Mollo & Millière 2026 (*PhiMiSci* 7(1), doi 10.33735/phimisci.2026.12307, published online 2026-02-27). State: real-correct. Publisher HTML galley; §7.1 "Parameter-identical duplicates" and all 3 quotations verified.
- Davidson 1987 (*Proc. & Addresses APA* 60(3) 441–458, doi 10.2307/3131782). State: real-correct (Crossref: first page 441).
- Grindrod 2024 (*Synthese* 204(2) art. 71, doi 10.1007/s11229-024-04723-8). State: real-correct. University of Reading VoR PDF. The quotation is verified in the footnote describing the Evansian picture; consciousness is "set aside" in the main text.
- Hattiangadi & Schoubye (forthcoming, arXiv 2509.22206). State: real-correct. The quotation was verified against the arXiv abstract page (the PDF text layer corrupts ligatures). The Muhammad and mental-file objections were read in the body: no stored information "to assemble in even a metaphorical mental file", and "there may be no dominant causal source … Or … a famous boxer". The article's paraphrase "no dominant causal source, or the wrong one" is faithful.
- Koch 2025 (*Philosophy of AI* 1, 19–33, doi 10.18716/ojs/phai/2025.2325, DataCite). State: real-correct. Journal PDF; the quotation is on p. 27.
- Pepp 2026 (*Inquiry* 69(6) 2945–2963, online 2025-01-09, print 2026-07-03, doi 10.1080/0020174X.2024.2448482). State: real-correct. Quotation verified against the OpenAlex abstract; "can" restored.
- Baggio & Murphy 2024 (arXiv 2406.00159). State: real-correct. Title and quotation verified in the arXiv PDF.
- Southgate et al. (Map self-citations: Swampman, Content Externalism). State: real-correct (live corpus pages).
- **Inline ↔ References**: no orphans in either direction after Davidson (1987) was added inline. Searle and Putnam are named as background without a year and are not cited.
- **Superlative/currency sweep**: `find_superlative_claims` returns nothing.
- **Result-direction leg**: there are no empirical results. The one reported "datum", GPT-4's Marion Starlight output, matches Lederman & Mahowald's report (p. 1093).
- **Cited-author-stance leg**: Mandelkern & Linzen, Koch, Pepp, Cappelen & Deutsch, Cappelen & Dever, Coelho Mollo & Millière and Grindrod are pro-reference and are never presented as endorsing the Map. Ostertag and Hattiangadi & Schoubye are sceptics who give no consciousness argument, and the article says "a ground they do not use". Chalmers is presented with his explicit bracketing, and Lederman & Mahowald stay neutral on consciousness ("topics about which we make no claims").

### Counterarguments Considered

- **Interpretationist / Dennettian**: functional intentions are real intentions. The article grants them as functional states, like the [P-AC4](/positions/ai-consciousness-scope/#p-ac4) signatures, and denies on moderate PIT that they are original. The disagreement is honestly framework-conditional.
- **Pure externalism / Koch / Pepp**: reference without intention. Koch and Cappelen & Deutsch are now reclassified as delivering derived reference. Pepp is left as a live rival the Map has not refuted.
- **Teleosemantics (Coelho Mollo & Millière)**: handled by pointer to the two-normativities reply on [teleosemantics](/concepts/teleosemantics/).
- **Novel reference (Lederman & Mahowald)**: the article names it as the hardest case and states the cost to moderate PIT if the derivation routes fail.

## Optimistic Analysis Summary

### Strengths Preserved

- The lead states the conditional verdict, its premise chain and its hardest test in one paragraph, which suits the LLM-first audience.
- The five-step argument in "Derived, Not Borrowed" makes every premise visible.
- The two senses of "derive" (intrapersonal PIT derivation vs interpersonal Searlean derivation) are kept apart.
- The "Conscious Subjects in the Intuition Pumps" section is fair: both disclaimers are quoted, "neither is an error", and the children point answers Mandelkern & Linzen on their own standard ([P-CS3](/positions/consciousness-scope/#p-cs3)). The Phenomenologist and Mysterian personas would single this section out.
- The inverse-Swampman table: the Map's addition is credited as such, and the Swamp LLM is credited to Coelho Mollo & Millière.
- Novel reference has ranked options, and the cost is stated rather than buried. The Hardline Empiricist persona would single out "untested rather than confirmed" and "the price if it fails" as the right restraint.
- Relation to Site Perspective discloses that the verdict depends on the quantum-interface programme and that the Bidirectional Interaction link is weak.

### Enhancements Made

- The Cappelen & Deutsch reply was added (one sentence).
- First-person derived reference is now treated precisely: an artefact referent is available, a subject referent is not.
- Kripke's condition is labelled as the contested premise in the lead.

### Cross-links Added

- None new. The existing links are dense and every wikilink target resolves. The four inbound piped links installed by expand-topic stand.

## Remaining Items

- The cross-review follow-ons from expand-topic are already queued in todo.md: [intentionality](/concepts/intentionality/) L141, [symbol-grounding-problem](/concepts/symbol-grounding-problem/) L125, [language-and-consciousness](/concepts/language-and-consciousness/) L49, [chinese-room-argument](/concepts/chinese-room-argument/) L133, and [ai-consciousness](/topics/ai-consciousness/) L82.
- The research note `research/whether-language-model-words-refer-2026-10-11` was corrected in passing: p. 1092→1088, p. 1097→1098, Chalmers p. 38→39, and the L109 reader-route compression.
- Length is now 3,051 by `analyze_length` (soft 3,000, hard 4,000; soft_warning). Future passes should be length-neutral.

## Stability Notes

- Physicalists, interpretationists and teleosemanticists will always reject moderate PIT's claim that original intentionality needs a phenomenal source. That is a bedrock framework disagreement. Do not re-flag it as critical.
- Whether Kripke's intention condition is essential is a live dispute in the literature. The article takes a side and labels it ("on Kripke's condition"). Future reviews should not demand a refutation of Koch, Pepp or Cappelen & Deutsch. The article reclassifies two of them and openly leaves Pepp as unrefuted.
- The novel reference problem is an acknowledged open cost, not a defect. Do not "resolve" it by upgrading the dominant-causal-source proposal from "untested".
- The Tenet 4 connection (indexicals) is deliberately modest. Do not strengthen it.
- The citation ledger above was verified against raw primary text on 2026-10-11. Re-verify only entries whose wording changes.