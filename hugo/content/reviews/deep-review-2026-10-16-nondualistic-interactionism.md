---
ai_contribution: 100
ai_generated_date: 2026-10-16
ai_modified: 2026-10-16 11:43:41+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-16
date: &id001 2026-10-16
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-16 11:43:41+00:00
modified: *id001
related_articles:
- '[[nondualistic-interactionism]]'
- '[[nondualistic-interactionism-2026-10-13]]'
- '[[tenet-check-2026-10-15]]'
title: Deep Review - Nondualistic Interactionism
topics: []
---

**Date**: 2026-10-16
**Article**: [Nondualistic Interactionism](/concepts/nondualistic-interactionism/)
**Previous review**: Never. This is the first deep review. The article has one commit, its creation on 2026-10-14 (`e446a9b6b3`). The reports-only passes that touch it are [tenet-check-2026-10-15](/reviews/tenet-check-2026-10-15/) (it raised no defect) and the pre-creation [optimistic-2026-10-13-process-wing](/reviews/optimistic-2026-10-13-process-wing/).
**Selection**: chosen by the shipped scorer (`scripts/deep_review.py next`). Score 101, never reviewed.
**Length**: 2,294 → 2,436 (+142) by `analyze_length`. The concepts thresholds are soft 2,500 and hard 3,500, and the gate is `>=`. The article is still below soft, with 64 words of headroom.

## Method

Every quotation was grep-verified as one exact string against raw full text, by script:
- **Griffin 1998.** I fetched the publisher e-edition and the newdualism.org copy fresh this run (`publishing.cdlib.org … docId=ft8c6009k3 … doc.view=entire_text`). Pages come from the e-edition's `JD_Page_N` markers. Each quote has 1 hit in each copy, and each page matches the article.
- **Kim 1999.** I checked the religion-online.org text (`?p=8626`).
- **Chalmers 2003.** I checked consc.net/papers/nature.html. Both passages fall in §11 "Type-F Monism", between offsets 101,693 and 116,036.

I did not reuse the research note's quotation table. I also read each quotation's surrounding passage. The three critical findings below all come from that context reading: in each, the verbatim quote was correct but the words around it qualified it.

## Pessimistic Analysis Summary

### Citation ledger (§2.4)

- **Griffin 1998** (*Unsnarling the World-Knot*). State: real-correct. The e-edition's "Preferred Citation" gives "Berkeley, Calif: University of California Press, 1998". Open Library ISBN 9780520209442 gives UC Press, 1998, 266 pp.
  - Quotations checked: p. 47, 48, 51 (×2), 82, 155, 172 (×4), 181, 186 (×3, including the new "the most obvious examples"), 188 (×2, including the new "especially humans and other higher animals"), 193, 205, 214, 237, 238, 241. All are verbatim at the stated page.
  - "numerically one through time" has 2 hits, on pp. 114 and 172. The article's p. 172 is the right one, because it sits inside the Q5 sentence.
- **Chalmers 2003** ("Consciousness and its Place in Nature"). State: real-correct. Crossref 10.1002/9780470998762.ch5 gives pp. 102–142, 2003, *The Blackwell Guide to Philosophy of Mind*. All three quotations are verbatim. The Griffin listing is in a footnote of §11, the same section as the high-level passage.
- **Kim 1999** ("Physicalism and Panexperientialism: Response to David Ray Griffin"). State: real-correct. Crossref 10.5840/process1999281/222 gives *Process Studies* 28, pp. 28–34, 1999. The religion-online header reads "Vol. 28, Number 1-2, Spring-Summer, 1999".
  - All three quotations are verbatim.
  - The article's gloss "Without one, the dominant occasion names the thing to be explained" follows Kim's "I suppose that Griffin's notion of a 'compound' must do most of the work … But what I don't see is how this really helps". It is a fair gloss, so I left it.
- **Griffin 1997** (*Parapsychology, Philosophy, and Spirituality: A Postmodern Exploration*). New reference. State: real-correct at the metadata level (Open Library: State University of New York Press, 1997, ISBN 9780791433157). The body was **not read**. The claim it supports comes from the publisher's jacket copy, quoted in Open Library's work record: "on the basis of a nondualistic distinction between mind and brain, which makes the idea of life after death conceivable". The article paraphrases that claim and does not quote it.
- **Result-direction leg.** No empirical results are cited, so this leg does not apply.
- **Cited-author-stance leg.**
  - Kim is a physicalist. He is presented as pressing the composition demand against Griffin, not as endorsing the Map.
  - Chalmers is presented as listing Griffin under type-F. The type-D placement is explicitly marked as the Map's reading ("Chalmers does not say this of Griffin").
  - Griffin is presented throughout as the rival, never as an ally on kind.
- **Inline ↔ References.** Every inline author-year cite has an entry: Griffin 1998, Griffin 1997, Kim 1999, Chalmers 2003. The two Map-page entries are wikilinked in the body. There are no orphans in either direction.
- **Superlatives.** `find_superlative_claims` returned nothing.

### Critical Issues Found

1. **Dropped qualifier, p. 193 (L56).** The article said: What is new at the human level is "a new kind of causal relation" (p. 193). Griffin's sentence continues without a break: "or, more precisely, an extreme exemplification of a kind of causal relation that had become increasingly important in the evolution of the higher animals". Griffin corrects his own phrase, and the correction is what keeps it consistent with his "one of degree, not of kind" (p. 241). The next clause in the article quotes p. 241, so the truncation set up a tension Griffin had already resolved. **Fixed.** The article now quotes the corrected phrase.
2. **Misattribution of Griffin's main objection (L94).** The article said: "Griffin's main case against dualism is that it 'violates the principle of continuity …'" (p. 51). Griffin numbers his charges on pp. 49–51. "1. The chief problem of dualism has always been to understand how two totally different types of things could causally influence each other"; "2. Dualism also violates the principle of continuity". So continuity is his second charge. **Fixed:** "Griffin's second charge against dualism, after the interaction of unlike things, …". I also changed "Tenet 5 counts as unreliable" to "of the kind Tenet 5 treats as defeasible", because Tenet 5's Rules-out clause binds parsimony, and continuity is a related heuristic rather than parsimony itself.
3. **Universal absence claim contradicted by a footnote (L88).** The article said: "Quantum indeterminacy appears in the book as room for a mental pole in elementary particles, never as the locus of the mind's action." I swept all 58 "quantum" hits in the book, endnotes included. The footnote at p. 191 (the index confirms "Elsasser, Walter, 191 n.") borrows Elsasser's point that quantum laws "do not uniquely determine the happenings on the microscopic level". Griffin uses it to show that the mind's influence on the body's electrons (Whitehead's "plan of the body", pp. 190–191) violates no physical law. That passage is quantum underdetermination doing compatibility work for the mind's downward reach, which is the structural move the Map makes. It is not a mechanism and it is not minimal, but it falsifies "never".
   - **Fixed:** "chiefly as room for a mental pole …; the mind's reach into the body's particles gets one footnote … (p. 191n); no mechanism is given". I also changed "Griffin does not [graft a quantum locus]" to "Griffin goes no further than that footnote".
   - The Tenet 2 verdict holds: the influence is neither minimal nor located at a quantum interface. Note that a second endnote treats Seager's quantum coherence as possibly "a necessary but not sufficient condition of the emergence of a unified experience". That one concerns unity, not action, so it is not imported.

### Medium Issues Found

- **"Closest rival" superlative (L40, description).** The article's own table shows Hasker's emergent dualism agreeing with the Map on all four columns, while Griffin differs on kind. **Fixed** to "closest non-dualist rival" and "nearest non-dualist rival".
- **"No brain, no dominant occasions" (L78).** This phrasing implies Griffin holds that the mind ceases with the brain. His 1997 book treats the nondualistic distinction as making life after death conceivable. Griffin sits with Hasker on *origin* (p. 186), which is what the `emergent-dualism` axis tracks ("does the Map's consciousness *emerge from* neural complexity"). **Fixed**, with the 1997 book added as a reference. Its body was not read; see the ledger.
- **Apparent contradiction between "Closure Kept" and Chalmers's criterion (L66).** The section heading says Griffin keeps closure, but Chalmers's condition requires "a denial of microphysical causal closure". They are compatible: Griffin keeps closure *to non-physical causes* in his enlarged sense of "physical" (p. 237), and denies that physics can give a complete causal account (p. 238). In Chalmers's terms that is a denial of microphysical closure: "every microphysical state has a microphysical sufficient cause". **Fixed** with one bridging clause.
- **Chalmers qualifier (L66).** The article said "a type-F monist who avoids the combination problem". Chalmers wrote "Some type-F monists appear to hold that they can avoid", and then judged the view "untenable" unless closure is denied. **Fixed** to "type-F monists who hope to avoid". I re-checked the pronoun: "it" became "that position".
- **Compound-individual scope (L54, L58).** The article said "Animals and cells are compound individuals." Griffin: "Animals with central nervous systems are the most obvious examples"; cells only "(by hypothesis)" (p. 186). It also said "the organism is the one place where that self-determination makes a difference". Griffin: "in compound individuals, especially humans and other higher animals" (p. 188). **Both fixed.**
- **Workflow artefact in article prose (L84).** "The 2026-10-02 review of [the-steelman-for-process-monism](/topics/the-steelman-for-process-monism/) recorded that …" cited an internal review file to readers. **Fixed:** "Tenet 1 alone does not say 'in kind' …". The steelman is still linked from Further Reading and the frontmatter.
- **"Griffin's psi chapter" (L96).** The book has no psi chapter. The psi material is a set of data items in ch. 5, "Data": §IV, "The Apparent Capacity of the Mind for Nonsensory Perception", plus psychokinesis at pp. 45 and 60. **Fixed.**

### Counterarguments Considered

- **Churchland and Dennett.** They would say Griffin's "hard-core commonsense" is folk psychology dressed as bedrock. The article already notes its kinship with the Map's self-stultification reasoning. This is a framework-boundary disagreement, not a defect.
- **Tegmark.** He would say neither view has a mechanism. The article already concedes this for both views, and the new footnote sentence makes Griffin's position more exact.
- **Deutsch.** Tenet 4 is "unaddressed". I verified 0 hits for "many worlds", "many-worlds", "Everett" and "many minds" in the book.
- **Popper's ghost.** He would say the selector reading in the "positions register" paragraph is unfalsifiable bookkeeping. It is explicitly labelled "The Map speculates", and the register seams are queued as a HUMAN LENGTH DECISION task (todo L2237).
- **Nagarjuna.** He would say Griffin's serially ordered society of occasions is closer to non-self than the Map's persisting subject. The article already marks the persisting subject as the Map's downstream commitment, not a Tenet 1 entailment.

### Reasoning-mode classification (editor-internal)

- **Kim's composition demand: Mode Two.** The dominant occasion is posited rather than derived, so it is an unsupported foundational move by the standard of Griffin's own explanatory ambitions.
- **Chalmers's high-level caveat: Mode One** within Chalmers's taxonomy (Griffin is type-D by Chalmers's own structural criterion), **ending at Mode Three** (Griffin's ontological criterion differs). The article states this split honestly.
- **Griffin's conservation stance and the kind axis: Mode Three.** These are a difference in risk tolerance and a framework boundary, and the article names them as such.
- I found no label leakage and no boundary-substitution.

## Optimistic Analysis Summary

### Strengths Preserved

- **The two-theses split** (Q2, p. 47) set beside the Map's own tenet sentence. It is the cleanest demonstration on the site that "distinct yet causally connected" does not entail "different in kind".
- **The neighbours table.** It is compact and columnar, and it is now also what justifies the "non-dualist" qualifier.
- **The [P-D2](/positions/arguments-for-dualism/#p-d2)/[P-MC3](/positions/arguments-for-mental-causation/#p-mc3) analysis.** It applies the register's own terms and labels its repair as speculation.
- **The type-F/type-D paragraph,** which marks the Map's reading explicitly as the Map's (praised by the Chalmers and Birch personas).
- **"What the Map should not claim"**, which refuses to treat the composition demand as a refutation. The Hardline Empiricist persona praised this.
- **Tenet 5 applied symmetrically.**

### Enhancements Made

- The three critical fixes and seven medium fixes listed above.
- The Tenet 2 contrast is now sharper. Griffin and the Map share the "quantum laws underdetermine micro-events, so downward influence breaks no law" move. They differ on minimality, on mechanism, and on conservation.

### Cross-links Added

- None. The page is already wired to every neighbour the research note named.

## Remaining Items (follow-ups, not actioned)

1. **The research note carries the p. 193 truncation.** `research/nondualistic-interactionism-2026-10-13` has it at L168 ("a high-level actual entity with 'a new kind of causal relation' (p. 193)"), L209 (Q12 ends before "or, more precisely"), and L244 ("The human mind's novelty is 'a new kind of causal relation', not a new kind of stuff"). The same note's L267 ("It is never the locus of the mind's action on the brain") is contradicted by the p. 191 Elsasser footnote. The note also lists the continuity charge as Griffin's "main case" at L306 ("Griffin's main case against dualism leans on continuity"). That is the seed of critical issue 2.
2. **The steelman's L85 inference** ("The difference in kind is the Map's further claim, drawn from pairing that tenet with Bidirectional Interaction") is the inference this page counterexamples. It stays queued for the steelman's next review, per research-note seam 3. I did not touch it here.

## Stability Notes

- **The kind axis is a bedrock disagreement.** Griffin's degree-not-kind ontology and the Map's kind claim will not converge. Future reviews should not flag "the article does not refute Griffin" as a defect, because the article says so on purpose.
- **The Tenet 2 divergence is calibrated as risk tolerance, not incompatibility.** The p. 191n footnote now in the text is the boundary of what Griffin offers on quantum compatibility. Do not upgrade it to "Griffin proposes a quantum mechanism", and do not restore "never".
- **Context-check every quote.** Every Griffin quotation in this article has now been checked in its surrounding passage, not only as a verbatim string. Future reviews should re-verify any newly added quotation the same way: two of this review's three critical issues were verbatim-correct quotes whose next clause or numbered list qualified them.