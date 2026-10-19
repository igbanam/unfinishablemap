---
title: "Deep Review - Quantum Non-Equilibrium and the Contingency of the Born Rule"
created: 2026-10-19
modified: 2026-10-19
human_modified: null
ai_modified: 2026-10-19T22:17:51+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-19
last_curated: null
---

**Date**: 2026-10-19
**Article**: [[quantum-non-equilibrium-and-the-contingency-of-the-born-rule|Quantum Non-Equilibrium and the Contingency of the Born Rule]]
**Previous review**: [[deep-review-2026-09-02-quantum-non-equilibrium-and-the-contingency-of-the-born-rule|2026-09-02]]. Also read: [[pessimistic-2026-10-12-quantum-non-equilibrium-and-the-contingency-of-the-born-rule|pessimistic 2026-10-12]]. All six of its Priority List items (1a, 1b, 2, 3a, 3b, 4) were applied by refine-draft `c0c0e7260b` the same day.
**Why this target**: top-ranked candidate (score 72) after excluding files edited on 2026-10-19 and files with open tasks. `topics/frankfurt-cases…` was edited today, and `topics/event-causal-libertarianism` is the target of an open P3. The only open-task mention of this slug is incidental: P3 "Valentini's … signal-locality theorem … in two siblings" targets `concepts/agency-budget` and `positions/quantum-interface`. The second review since creation, and the first since the 10-12 refine-draft installed three references and five quoted spans.
**Length**: 2,832 → 2,956 words (`analyze_length`, body-only; topics 3000 / 4000; status `ok` before and after).

## Pessimistic Analysis Summary

The 10-12 pessimistic review's fixes hold. Every quoted span it installed was grepped verbatim in the primary text this run. Four new defects turned up, and none was visible to a check of metadata or abstracts alone. The first is a framing the article attributed to a source that says the reverse, which was present from creation and passed by both prior reviews. The second is a physical mechanism misattributed, also present from creation. The third is a seam left by the 10-12 install, where the sentence after the newly reported test still called the hypothesis "untested". The fourth is a dropped qualifier I introduced myself while editing and then corrected.

### Critical Issues Found

1. **Attribution inverted (L43).** The article said: "Valentini's 2020 chapter frames the debate explicitly — a philosophical argument over the foundations of the theory's statistical mechanics, not a disagreement about any prediction accessible today." The chapter argues the opposite. From the arXiv:1906.10761 full text (pdftotext, grep):
   - "Thus the existence of initial equilibrium or nonequilibrium is an empirical question – not only in principle but also in practice."
   - "The question of the existence or otherwise of primordial quantum nonequilbrium is empirical. It will be answered by detailed work in theoretical and observational cosmology, not by foundational debates about the meaning of probability and related topics."
   - The abstract ends: "We argue that the existence or otherwise of quantum nonequilibrium in our world is an empirical question to be settled by experiment."

   Valentini calls the meaning-of-probability question "a valid and interesting philosophical question" and the typicality school's emphasis on it "a distraction". **Fixed**: the chapter now frames the dispute as one over the foundations of statistical mechanics while insisting the open question is empirical, with the verbatim "an empirical question – not only in principle but also in practice" quoted.

2. **Map framing contradicted by the source and by the article's own later sections (L49).** "The dispute is unresolved and largely philosophical, since the two schools agree about everything measurable today." Valentini's whole cosmological programme exists because the schools differ about what the early universe could hold, and L65–67 report the programme's fit to Planck data. **Fixed**: "The two schools agree about every laboratory result so far and part over the early universe, where relaxation leaves room for relic non-equilibrium that typicality counts as atypical." The same paragraph's "cosmological history happened to erase" became "has largely erased", because L63–65 discuss surviving long-wavelength residues.

3. **Physical mechanism misstated (L63).** "Long-wavelength cosmological modes are exactly such few-mode systems — the physical basis for conjecturing that primordial non-equilibrium could survive at the largest scales." The two senses of "mode" were conflated: energy eigenstates in the oscillator numerics, Fourier modes in cosmology. The programme gives a different basis for large-scale survival.
   - Colin & Valentini 2013 (*PRD* 88, 103515) abstract: "the time evolution of a field mode on expanding space is mathematically equivalent to that of a standard harmonic oscillator with a 'retarded time' that depends on the wavelength of the mode. In the far super-Hubble regime the equivalent oscillator evolves over only one Hubble time, yielding a simple mechanism whereby relaxation to the Born rule can be suppressed on very large scales."
   - Valentini 2020 §3: "for long wavelengths λphys ≳ H⁻¹ we find tret(t, k) < t and relaxation is retarded or suppressed."

   **Fixed**: the sentence now gives the retarded-time super-Hubble suppression, citing Colin & Valentini 2013 (new reference 17). The preceding few-state residue result is untouched.

4. **Internal contradiction, a seam from the 10-12 install (L67).** The paragraph reports the Vitenti, Peter & Valentini (2019) fit to Planck data, then closes: "nothing has come in: the non-equilibrium hypothesis is unrefuted and untested". The pessimistic review had recommended "tested once, inconclusive, leaning null", but the install kept the old close. By `project/writing-style.md` §"Falsifier Sections: Distinguish the Three Negative States", this is state 3 (too thin to decide), not state 1. **Fixed**: "the evidence is too thin to decide: the programme's own test of its prediction settled nothing in either direction, so the non-equilibrium hypothesis is unrefuted but has not survived a test." The lede's evidential-floor sentence (L29) now adds "an inconclusive fit to cosmological data" to "theorems-with-premises, numerical simulations". This keeps the front-loaded summary consistent with the body.

### Medium Issues Found

- **Paraphrase drift (L37).** "gravitational corrections" became "quantum-gravitational corrections", matching the 2023 abstract's wording ("quantum-gravitational corrections to the Schrödinger approximation"). Word count unchanged.
- **Incomplete account of the 2019 result (L67).** The article said only that the best fit was "a sudden step". The authors' headline claim is "what appears to be substantial evidence, according to the Jeffreys' scale" for a sharp ~20% reduction above ~350 Mpc. The body says "statistical significance ranging from substantial to strong", with the "conservative conclusion" that it is "only 'substantial'". **Fixed** with the abstract's hedged phrase verbatim. A first draft of this edit read "which they rate substantial evidence", which dropped "what appears to be". I caught and corrected that before finishing. Logged here as a self-introduced qualifier drop.
- **Reference metadata incomplete.** Valentini 2020 lacked its editor and pages. Added "V. Allori (ed.)" and 423–477 (Crossref pp. 423–477; the editor is on the chapter's arXiv title page).

### Publisher-of-Record Citation Ledger (§2.4)

Metadata was checked at Crossref this run for all DOI-bearing entries. Quotes were grepped in raw text. "Abstract" means the arXiv API or the OpenAlex inverted index; "full text" means arXiv PDF via pdftotext.

- Valentini 1991 I (*Phys. Lett. A* 156, 5–11) — real-correct (Crossref)
- Valentini 1991 II (*Phys. Lett. A* 158, 1–8) — real-correct (Crossref)
- Dürr, Goldstein & Zanghì 1992 (*J. Stat. Phys.* 67, 843–907) — real-correct (Crossref)
- Valentini 2002 (Placek & Butterfield, Kluwer, 81–103; quant-ph/0112151) — real-correct (arXiv journal-ref). Both quoted spans grepped in the abstract. "signal-locality is true only in equilibrium" is stated there of pilot-wave theory, which is the article's context.
- Valentini 2020 (World Scientific, 423–477) — real-correct-but-incomplete (editor and pages added). "inherently circular and physically misguided" was grepped in the abstract. **The L43 framing was inverted (Critical 1).**
- Towler, Russell & Valentini 2012 (*Proc. R. Soc. A* 468, 990–1013) — real-correct (Crossref). L61 was verified by pessimistic-10-12 against the full text and not re-read.
- Abraham, Colin & Valentini 2014 (*J. Phys. A* 47, 395306) — real-correct. Abstract result-direction: a residue "exceeding 10%" depending on phases, "less likely … for larger numbers of energy states". This matches L63.
- Colin & Valentini 2013 (*PRD* 88, 103515) — **new**, real-correct (Crossref); abstract as quoted above.
- Colin & Valentini 2015 (*PRD* 92, 043520) — real-correct. Abstract: radiation-dominated pre-inflationary era, inverse-tangent deficit, "possible explanation for the reported large-scale anomalies". "The extent to which the data might support our scenario is left as a question for future work." This matches L65.
- Colin & Valentini 2016 (*IJMPD* 25, 1650068) — real-correct. The "likely to be a fairly general and robust signature…" span was grepped in the abstract, as were the subquantum-width and radiation-dominated conditions.
- Underwood & Valentini 2020 (*PRD* 101, 043004) — real-correct. The abstract (relic particles' line spectra, broadening and narrowing) matches L65.
- Lustosa, Pinto-Neto & Valentini 2023 (*Proc. R. Soc. A* 479, 20220411) — real-correct. Abstract: "interactions can delay or even prevent complete relaxation for some initial states". This matches "extended to coupled oscillators".
- Valentini 2010 (*Many Worlds?*, OUP, 476–509) — real-correct (Crossref). The abstract's reply to "Deutsch, Zeh, Brown and Wallace" matches L79.
- Valentini 2008 (Craig & Smith, Routledge, 125–155; quant-ph/0504011) — real-correct (arXiv journal-ref; not in Crossref). "an operational definition of absolute simultaneity" and the preferred-foliation clause were grepped in the abstract. The arXiv title reads "Spacetime", and Valentini's own 2020 bibliography gives "space-time"; the article's form is left as is.
- Vitenti, Peter & Valentini 2019 (*PRD* 100, 043506) — real-correct (Crossref). Full text, reading-order extraction: "2 − 3σ level in favor of our quantum relaxation model" (temperature-only Planck with H0/BAO), "statistically inconclusive results", and "This suggests that the effect is probably a statistical fluctuation". All are verbatim and the direction matches. The "sudden jump" passage and the Jeffreys-scale evidence were also verified. The layout-mode extraction produced a false zero for "statistically inconclusive" (two-column interleave). Raw mode found it, so absence was never asserted.
- Valentini 2023 (*Found. Phys.* 53, 6) — real-correct (Crossref). "to be created from a prior equilibrium" and "very tiny and difficult to observe in practice" were grepped in the abstract.
- Goldstein, SEP "Bohmian Mechanics" — real-correct. Both spans were re-grepped this run in the raw live HTML (one hit each).
- Two Map self-citations (refs 18–19) — site convention, retained.
- Internal cross-claims checked: the `qm-interpretations-beyond-many-worlds` L63 "most hostile"; `causal-consistency-constraint`'s "not-yet-refereed arXiv preprint"; and the "non-affine" gloss against the Torres Alegre arXiv:2512.12636 abstract, where "the only such relationship consistent with no-signaling is the identity".

**Superlative sweep**: "every experiment to date" (L29) is self-scoping. The new "every laboratory result so far" is likewise scoped.

**Cited-author stance**: Valentini is a deterministic pilot-wave realist and Goldstein a Bohmian of the typicality school. Neither is presented as endorsing anything about mind. The article's firewall sentence ("nothing in this literature is about consciousness") stands.

### Counterarguments Considered (six personas)

- **Eliminative Materialist**: the "modal lesson" for Tenet 3 remains a Map-only inference, and the article fences it with three honesty notes. Bedrock, not re-flagged.
- **Hard-Nosed Physicalist**: the price-list point was resolved by the 10-12 fix, which made Valentini a worked analogue and the steering result the Map's in-class argument. It holds.
- **Quantum Skeptic**: would have caught Critical 3. The few-state result describes a laboratory oscillator, and the cosmological survival story rests on expansion. With the corrected mechanism, the Map's "never in brains" note is better supported, since nothing in a brain is super-Hubble.
- **Many-Worlds Defender**: Valentini's 2010 reply leans on non-equilibrium. This is a framing point that pessimistic-10-12 recorded, not a defect.
- **Empiricist**: would have caught Critical 4. The falsifier ledger now names state 3 correctly.
- **Buddhist Philosopher**: no change. The typicality regress charge is reported, not adjudicated.

**Reasoning-mode classification (editor-internal)**: no named-opponent refutation is attempted. The typicality engagement is reportage plus boundary-marking (Mode Three, honest). The Bohmian-determinism mismatch is boundary-marked in the lede and in the Relation section. No label leakage. "load-bearing" and "This is not" both have zero hits.

## Optimistic Analysis Summary

### Strengths Preserved

- The front-loaded conditional, with the Map's non-endorsement in the first paragraph.
- The firewall stating that nothing in this literature concerns consciousness (Mysterian and Hardline Empiricist both praise it).
- The 10-12 scope repair (Valentini as worked analogue; the causal-consistency steering result as the in-class argument; "neither covers the other's ground"). It was untouched.
- The three honesty notes on the Bidirectional Interaction speculation, and the Tenet 5 symmetry ("must not quietly convert 'coherently violable' into 'probably violated'"). Untouched.
- Hardline Empiricist (Birch): the corrected falsifier ledger is now a model instance of state-3 reporting. Process Philosopher: the contingency-as-equilibrium reading is unchanged. The two are not in tension on any edited passage, because no tier was moved.

### Enhancements Made

- L43 and L49 now report Valentini's own empirical framing, which makes the cosmological window the natural next section rather than a surprise after "nothing measurable".
- The L63 mechanism is corrected (super-Hubble retarded time).
- The lede now reflects the one data-level result.

### Cross-links Added

- None. All outbound links resolve, and the article is integrated (nine outbound wikilinks; inbound from agency-budget, born-rule-and-the-consciousness-interface and sorkin-higher-order-interference).

## Remaining Items (for the driver, not edited here)

1. **`positions/quantum-interface` P-Q11 Calibration (L173)** still reads "dated derived predictions whose current observational standing the Map has not surveyed". This went stale when the 10-12 install surveyed Vitenti, Peter & Valentini (2019) in the "Argued in" article. The register is the secondary file of the open P3 at todo L1962, so it was not edited. That P3 could absorb it as an optional item: "…whose one published test, Vitenti, Peter & Valentini 2019, was statistically inconclusive". The register needs a dated Updated note.
2. **`topics/born-rule-and-the-consciousness-interface` L128: flagged, not asserted. Look, then decide.** It reads "Valentini's (1991) relaxation cannot explain why the universe began near equilibrium". On Valentini's own account the universe began *out* of equilibrium and relaxed. What relaxation needs is an initial-condition assumption: no fine-grained microstructure. Valentini 2020: "non-relaxing initial conditions … are ruled out empirically, not by theoretical fiat". The sentence may intend that assumption, but as written it misdescribes the programme. Not edited: different file, not this review's target.
3. **`research/bohmian-quantum-equilibrium-and-non-equilibrium-2026-07-19` L108** groups "few-mode, long-wavelength, cosmological" as one side of a list. That is the probable seed of Critical 3. It is a research note, so it is left as is and recorded here.

## Stability Notes

- All 2026-09-02 stability notes stand: Bohmian determinism versus the tenets, the unresolved typicality dispute, and the "never observed" floor.
- **The dispute is now framed as Valentini frames it** (empirical, cosmological) and is still unadjudicated. Future reviews should not reintroduce "largely philosophical" or "agree about everything measurable" as the article's voice. Any Map judgment that the dispute is philosophical must be labelled as the Map's and must not be attributed to Valentini.
- **Falsifier state is 3 (too thin to decide), not 1.** Future edits should keep "unrefuted but has not survived a test". Do not revert to "untested" while the Vitenti 2019 result is reported.
- The post-2019 literature (other groups' CMB analyses, laboratory proposals) remains deliberately unsurveyed, and the article says so. That is honest scoping, not a defect.
- Convergence: with these fixes, the article's empirical sections have been checked against full text or abstract for every cited result. The next review should expect a no-op unless the body changes or the post-2019 survey is undertaken.
