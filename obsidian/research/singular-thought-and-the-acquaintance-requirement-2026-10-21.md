---
title: "Research Notes - Singular Thought and the Acquaintance Requirement"
created: 2026-10-21
modified: 2026-10-21
human_modified: null
ai_modified: 2026-10-21T14:08:37+00:00
draft: false
description: "Singular thought read at source: Russell's acquaintance, Evans's Russell's Principle, Lewis and Recanati's informational acquaintance, Jeshion and Hawthorne-Manley liberalism, Campbell and Smithies on demonstratives, and LLM entity files."
topics:
  - "[[whether-language-model-words-refer]]"
  - "[[philosophy-of-language-under-dualism]]"
  - "[[ai-consciousness]]"
concepts:
  - "[[phenomenal-acquaintance]]"
  - "[[naturalist-relationalism]]"
  - "[[indexical-knowledge-and-identity]]"
  - "[[intentionality]]"
  - "[[content-externalism]]"
  - "[[symbol-grounding-problem]]"
  - "[[immunity-to-error-through-misidentification]]"
  - "[[cognitive-phenomenology]]"
related_articles:
  - "[[tenets]]"
  - "[[acquaintance-void]]"
  - "[[haecceity]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-21
last_curated: null
last_deep_review: null
recommended_action: article
target_section: topics
target_slug: singular-thought-and-acquaintance
---

# Research: Singular Thought and the Acquaintance Requirement

**Date**: 2026-10-21
**Origin**: harvested research-topic (todo L40, 13:08Z), from `reviews/optimistic-2026-10-21-structure-and-source-wing.md` (§"Singular thought and the acquaintance requirement", High Priority).

**Sources fetched raw and read.** Every quotation marked *verified* below was checked by `grep -F` against these files, after normalising whitespace:
- Russell 1910–11, "Knowledge by Acquaintance and Knowledge by Description". Read as reprinted in *Mysticism and Logic* (1917), ch. X, Project Gutenberg #25447, plain text. That edition confirms the original venue (*Proceedings of the Aristotelian Society* 1910–11). It has no page numbers.
- Russell 1912, *The Problems of Philosophy*, ch. 5, Project Gutenberg #5827, plain text.
- Recanati 2009, "(Anti-)Descriptivism, Mental Files, and the Communication of Singular Thoughts", *Manuscrito* 32(1): 7–32. Full PDF from the Unicamp OJS, read page by page. Journal page = PDF page + 6.
- Hattiangadi and Schoubye, arXiv:2509.22206. Full PDF; the HTML version returns 404.
- SEP, "Singular Propositions" (Fitch and Nelson; substantive revision 27 Sep 2013). Full HTML.
- Hurry 2021, PhD thesis, Western University. Full PDF. It is the only raw text in which Evans 1982 was seen, and only as Hurry quotes it.
- Four NDPR reviews, full HTML:
  - Ninan 2011, of Jeshion (ed.) 2010.
  - Abbott 2013, of Hawthorne and Manley 2012.
  - Leonardi 2013, of Recanati 2012.
  - Palmira 2020, of Goodman, Genone and Kroll (eds.) 2020.
- Abstracts:
  - Crossref: Campbell 2002, Jeshion (ed.) 2010, Sawyer 2012.
  - OpenAlex inverted-index abstracts: Smithies 2011, Barkasi 2019, Jeshion 2010 (chapter), Recanati 2010 (chapter), Goodman 2016, Dickie 2015 (chapter), Azzouni 2011.
  - arXiv `citation_abstract` meta: Ferrando et al., Meng et al., Feng and Steinhardt, Sakata et al., Yona et al., Bogdan and Lindsey.
- Crossref metadata: Kaplan 1978, Kahneman, Treisman and Gibbs 1992, Pylyshyn 2001, Crane 2011, Goodman 2016, Smithies 2011, and the four OUP monographs.

**Search queries used**:
- Russell "Knowledge by Acquaintance and Knowledge by Description" "composed wholly of constituents".
- SEP singular thought acquaintance Russell's Principle Evans Jeshion Hawthorne Manley.
- Smithies "What is the role of consciousness in demonstrative thought".
- Campbell "Reference and Consciousness" conscious attention "knowledge of reference".
- Jeshion "Singular Thought: Acquaintance, Semantic Instrumentalism, and Cognitivism".
- large language models "singular thought" OR "mental files".
- "Do I Know This Entity" knowledge awareness.
- "phenomenal intentionality" "singular thought".
- chatbots language models "de re" OR "singular thought" OR "acquaintance".
- Lewis "I call such relations as these relations of acquaintance".
- language models aliases entity representation activation patching.

**Not usable this run**:
- *Evans 1982*: the Internet Archive item `varietiesofrefer0000evan` is lending-restricted, and search-inside returned 403.
- *Google Books*: the `SearchWithinVolume2` endpoint returned 0 for **every** query, including the known-good control from memory (Hirsch, `rX9MCAAAQBAJ`, "variability or plasticity"). It is down today, and no zero from it means absence. The Books API quota was exhausted (429).
- *PhilPapers and PhilArchive* (Smithies 2011, Barkasi 2019, Goodman 2016, Sawyer 2012 PDFs): Cloudflare 403.
- *HAL* (`ijn_00352830`, the author copy of Recanati 2010): an Anubis anti-bot wall for both curl and WebFetch. I did not attempt to bypass it. Recanati 2009 in *Manuscrito* overlaps it heavily; its abstract is near-identical to the 2010 chapter's.
- *Kelly's review of Campbell* (scholar.harvard.edu): 403. Campbell's blindsight argument therefore remains unverified.

## Verdict (assess-first) {#verdict}

**Write the article.** It should be a topics page, `topics/singular-thought-and-acquaintance`, titled "Singular Thought and the Acquaintance Requirement", at **2,600–3,000 words by `analyze_length`** (prose about 2,250–2,600 plus about 350–400 of apparatus). The topics soft gate is 3,000 and the hard gate 4,000. The slug is free (`scripts/check_slug.py`, 14:0xZ), with no archive file or hugo/content match. Topics stand at **353/370** by `tools.evolution.state.count_section_files("topics")`.

Why a standalone page:
- **Zero live coverage.** Re-measured at 13:5xZ over topics, concepts, apex, voids, positions and tenets (counts are live / research / archive):
  - 0/0/0: "singular thought", "Russell's Principle", "acquaintance requirement", "Jeshion", "Reference Book", "Generality Constraint".
  - "Recanati" 0/1/0; "Manley" 0/2/0; "demonstrative thought" 0/1/0.
  - "mental file" 1/1/0: the LLM page L106 and its research note.
  - Positive controls: "Varieties of Reference" 3/7/2, "knowledge by description" 5/5/8.
- **Three live pages lean on the theory without stating it.**
  - `whether-language-model-words-refer` L106 turns on Hattiangadi and Schoubye's mental-file objection.
  - `phenomenal-acquaintance` treats Russell 1910 as a theory of knowing *qualities* only (L44–L52).
  - `naturalist-relationalism` L47 has the corpus's only sentence on Campbell's demonstrative thesis.
- **The subject has a structure that makes its dualist relevance narrow and conditional** (see [the conditional, mapped](#conditional)). That calibration needs stating once, on one page, so the three borrowers can point to it.

Why not fold it in:
- **`whether-language-model-words-refer`** (3,051 total, 2,666 prose, headroom 948, already at soft warning). The theory of singular thought is about human thinkers first. Housing it there would blur the distinction the page must keep, between an LLM's *words* referring and the system having singular *thought*.
- **`phenomenal-acquaintance`** (3,031 total, 2,594 prose, headroom 468). Its subject is acquaintance with qualities. Grafting acquaintance with particulars onto it invites exactly the equivocation flagged in [the guards](#guards).
- **`naturalist-relationalism`** is about perception, and **`indexical-knowledge-and-identity`** is about *de se* knowledge (headroom 311).

## Executive Summary

- **The question.** Can one think *about* a particular, as opposed to thinking whatever satisfies a description, without being acquainted with it?
  - Bach's terms (via Recanati 2009): a descriptive thought's object is fixed *satisfactionally*, a singular (*de re*) thought's object *relationally*.
- **Russell's answer was yes, acquaintance is required, and his acquaintance is presentation.** He says so explicitly (*verified*). But the objects of acquaintance were sense-data, universals and perhaps the self. So Russell's requirement made thought about Bismarck or Caesar *descriptive*.
- **Every later view that restores ordinary singular thought does so by relaxing what acquaintance is.**
  - Evans keeps "Russell's Principle", his label for Russell's requirement, as discriminating knowledge. One of its sufficient conditions is knowing distinguishing facts.
  - Lewis, Bach and Recanati turn acquaintance into an information-bearing causal channel, "accurate information" or "misinformation" alike (Lewis, as quoted by Recanati).
  - The liberal views remove the requirement altogether: Kaplan-style semantic instrumentalism, Jeshion's cognitivism, and the liberalism of Hawthorne and Manley.
- **Consequence for the Map (its own synthesis):** a *scope–phenomenality trade-off*. The more phenomenal the acquaintance relation, the narrower the range of singular thought it licenses.
  - The one place where the requirement plausibly carries a phenomenal condition is **perceptual demonstrative thought**.
  - There, Campbell (2002) and Smithies (2011) both hold consciousness essential. Neither is a dualist: Campbell is a relationalist, and Smithies gives consciousness an *epistemic* role.
- **The Map's conditional therefore holds only in a narrow form.** If singular thought needs acquaintance, and acquaintance is phenomenal presentation, then singular thought has a phenomenal condition. Its second premise fails for every broad-scope acquaintance view. Even where it holds, the result is *consciousness-dependence*, which physicalists can accept, not dualism.
- **The language-model case divides cleanly.**
  - On the informational views, a trained LLM arguably stands in causal channels to Robespierre through its training texts.
  - What it lacks on the Map's view is a *thinker* (P-AC1, moderate PIT), not acquaintance.
  - The mental-file framework gives the LLM page's option 1 a mechanism: a coined name attached to an existing entity representation inherits its referent, derivatively.
  - Interpretability work (Meng et al. 2022; Ferrando et al. 2025; Sakata et al. 2025; Yona et al. 2026, preprint) finds entity-indexed, alias-invariant, causally used representations. This tells against Hattiangadi and Schoubye's no-files premise at the level of functional architecture. It does not address their deeper worry that causal covariation is not representation, and it says nothing about thought.
- **Tenet 4.** First-person reference is the *cheapest* singular reference. Perry's SELF file is based on identity, a non-phenomenal relation (via Recanati 2009). Singular-thought theory therefore neither supports nor threatens the indexical objection. The objection asks a question that reference semantics presupposes answered.

## The Conditional, Mapped {#conditional}

This is the analysis the article should carry. It is the Map's own framing, assembled from the sources below, and must be labelled as such.

**The argument the harvest proposed:**
- P1 (acquaintance requirement): singular thought about *o* requires acquaintance with *o*.
- P2 (phenomenal reading): acquaintance, in the sense P1 needs, is phenomenal presentation.
- C: singular thought has a phenomenal condition.
- The dualist step would need a further P3: phenomenal presentation is not physical. That is argued, and contested, on `phenomenal-acquaintance` (the Loar section, L92–L98), not here.

**Finding 1: the scope–phenomenality trade-off.**
- Russell holds both P1 and P2. His acquaintance is "the sort which constitutes presentation" (*verified*). The price is scope: Bismarck's friend knew Bismarck's body and mind "by description" (*verified*), and we cannot think about Caesar except through "some description of Julius Caesar" (1912, *verified*).
- Each move that restores singular thought about ordinary external things gives up P2:
  - Evans: discriminating knowledge, satisfiable by perception, recognition, *or knowing distinguishing facts* (Evans p. 89, via Hurry).
  - Lewis: any causal channel "of a sort which would permit a flow of information", where "still the channel is there" even with misinformation (via Recanati 2009, p. 18).
  - Bach: perception, memory and testimony (via Ninan).
  - Recanati: relations that are "epistemically rewarding in that they enable the subject to gain information from the object" (2009, p. 18, *verified*).
  - Sawyer 2012: "trace-based" acquaintance (abstract, *verified*).
- P1 and P2 are jointly defensible only for a narrow class: perceptual demonstratives, and possibly the self (Russell hedged in both 1910–11 and 1912, *verified*).

**Finding 2: where a phenomenal condition survives.**
- In perceptual demonstrative thought:
  - Campbell: "Conscious attention to an object, singling it out in experience, provides knowledge of the reference of a demonstrative term", and "only experience of objects can provide this kind of acquaintance with individual substances" (2002 abstract, *verified*).
  - Smithies: three accounts, Evans's, Campbell's and his own, "agree that consciousness is essential for demonstrative thought, but disagree about why it is". His own makes the role epistemic (abstract, *verified*).
- Live dissent:
  - Barkasi 2019 argues "experience is not the only way in which visual information could be accessed for the voluntary control of attention" (abstract, *verified*).
  - Pylyshyn's preconceptual visual indexes (2001; metadata verified, content not read) are the standard sub-personal model of demonstrative-like reference.
- Neither Campbell nor Smithies is an ally of dualism. The Map can use them as independent, non-dualist support for consciousness-dependence in one domain, and no further.

**Finding 3: the thinker condition, not the acquaintance condition, does the Map's work.**
- The liberal views remove the *acquaintance* condition, but none removes the *thinker* condition.
  - Jeshion's replacement is explicitly psychological. Its limits are "cognitive, associated with the goals, interests, plans, and affective states of the thinker" (chapter abstract, *verified*).
  - Semantic instrumentalism needs a stipulating agent.
  - Hawthorne and Manley make singular thought cheap, but it remains a thinker's thought.
- Russell chose "acquaintance" over "presentation" because it "emphasises the need of a subject which is acquainted" (*verified*).
- On moderate PIT, the Map's stance on `intentionality` L103–L107, a phenomenal condition enters singular thought through the thinker, not through the object-relation.
- Consequence: the liberal views are rivals only to the narrow thesis that *acquaintance* is the route by which consciousness enters singular thought. They do not touch the Map's PIT-based route. Present this as the Map's reading, not a result.

**Finding 4: the triviality worry.**
- Ninan notes of the file view: "So it follows almost by definition that singular thought requires acquaintance" (NDPR 2011, *verified*, Ninan's words).
- An acquaintance requirement made true by definition carries no phenomenal payload. The substantive question moves to what counts as an acquaintance relation.

## Terminology and Coinage {#coinage}

| Term | Coiner / source (as verified) | Guard |
|---|---|---|
| acquaintance; knowledge by acquaintance / description | Russell 1910–11 (the distinction is older: Russell's own debts are not checked here) | Russell's acquaintance is a *presentation* relation to sense-data, universals and perhaps the self. It is not Lewis's channel. |
| the "fundamental epistemological principle" | Russell 1910–11 ("Every proposition which we can understand must be composed wholly of constituents with which we are acquainted", *verified*); restated 1912 | Russell's own name for it is "fundamental principle". |
| **Russell's Principle** | **Evans's label** (1982), for the requirement he attributes to Russell. Hurry: "what Evans (1982) has labelled 'Russell's Principle'" (*verified* in Hurry) | Never "Russell's Principle (Russell 1912)". Write "what Evans calls Russell's Principle". |
| discriminating knowledge | Evans 1982, p. 89 (via Hurry) | Evans's sufficient conditions include *knowing distinguishing facts*, so the principle is no phenomenal requirement. |
| mental file / dossier | Grice 1969, introduced "rather incidentally"; Strawson 1974, "first detailed articulation"; Perry 1980, "most influential source"; then Bach 1987, Forbes 1990, Recanati 1993 and 2012 (all per Recanati 2009, p. 17, *verified*) | **Not Recanati's coinage.** He systematised it. The titles of Grice 1969 and Strawson 1974 are not checked here. |
| object file | Kahneman, Treisman and Gibbs 1992 (Crossref; Kahneman and Treisman 1984 per Recanati fn 3) | A vision-science, mid-level representation, **distinct** from philosophical mental files. Murez, Smortchkova and Strickland 2020 argue the analogy "only holds for a very limited range of cases" (Palmira's paraphrase). |
| epistemically rewarding (relations) | Recanati (2009, p. 18, *verified*; 2012 per Leonardi) | Informational, not phenomenal. |
| relations of acquaintance (liberalised) | Lewis (quoted by Recanati 2009, p. 18, citing "Lewis 1999: 380-81") | The original locus is uncertain. The 1999 page span falls inside the reprint of Lewis 1983, "Individuation by Acquaintance and by Stipulation". A similar passage is often attributed to Lewis 1979. Verify before naming the original. |
| satisfactional / relational | Bach (Recanati 2009 fn 7: "'Satisfactional' comes from Bach 1987"; Leonardi credits Bach 1986) | Cite as Bach 1986/1987. |
| Semantic Instrumentalism; Cognitivism | Jeshion 2010 (chapter abstract, *verified*) | Both are her labels. |
| liberalism (about singular thought); "constraint" | Hawthorne and Manley 2012. Hurry fn 6: they "are responsible for the 'Liberalist' terminology" (*verified* in Hurry) | **Name collision**: P-TU1 (`positions/thought-and-understanding`) uses "qualified liberalism" for *cognitive phenomenology*. Always write "liberalism about singular thought". |
| latitudinarianism | used in the *de re* literature (Ninan) | Coiner not checked. Do not attribute. |
| dthat; Newman1 | Kaplan. "Dthat" is **1978**, *Syntax and Semantics* 9: *Pragmatics*, 221–243 (Crossref, doi:10.1163/9789004368873_008). Newman1 is credited to Kaplan by Ninan (as "Kaplan (1977)") | The SEP bibliography dates "Dthat" **1975b** and NDPR dates it **1970**. Both are wrong; do not copy either. |
| reduplication argument | Strawson 1959, *Individuals*, pp. 20–22 (SEP) | Strawson used it for the fundamentality of demonstrative identification. |
| Le Verrier / Neptune | standard case (SEP; Abbott) | A descriptive name, per Jeshion as Leonardi reports her. |

## Key Sources {#sources}

### Russell (1910–11), "Knowledge by Acquaintance and Knowledge by Description"
- **URL**: https://www.gutenberg.org/cache/epub/25447/pg25447.txt (reprint in *Mysticism and Logic*, ch. X)
- **Type**: paper, *Proc. Aristotelian Society* 11: 108–128
- **Key points**:
  - Acquaintance is a presentation relation: "to say that S has acquaintance with O is essentially the same thing as to say that O is presented to S".
  - The principle: understanding requires acquaintance with every constituent.
  - Bismarck himself might name himself directly, "Assuming that there is such a thing as direct acquaintance with oneself". His friends knew him by description.
  - Russell is undecided on self-acquaintance: "It is difficult, but probably not impossible, to account for plain facts if we assume that we do not have acquaintance with ourselves."
- **Tenet alignment**: P2 holds for Russell's acquaintance, but his scope is tiny, which is Finding 1.
- **Verified quotes** (no page numbers in this edition):
  - "I say that I am _acquainted_ with an object when I have a direct cognitive relation to that object, i.e. when I am directly aware of the object itself."
  - "I do not mean the sort of relation which constitutes judgment, but the sort which constitutes presentation."
  - "Every proposition which we can understand must be composed wholly of constituents with which we are acquainted."
  - "it seems scarcely possible to believe that we can make a judgment or entertain a supposition without knowing what it is that we are judging or supposing about."
  - "it emphasises the need of a subject which is acquainted."
  - "Now I wish to preserve the dualism of subject and object in my terminology". **Do not recruit this for mind–body dualism.** See [the guards](#guards).

### Russell (1912), *The Problems of Philosophy*, ch. 5
- **URL**: https://www.gutenberg.org/cache/epub/5827/pg5827.txt
- **Verified quotes**:
  - "it is scarcely conceivable that we can make a judgement or entertain a supposition without knowing what it is that we are judging or supposing about."
  - "we make a statement about Julius Caesar, it is plain that Julius Caesar himself is not before our minds, since we are not acquainted with him."
  - "although acquaintance with ourselves seems _probably_ to occur, it is not wise to assert that it undoubtedly does occur."
- **Guard**: the 1910–11 and 1912 wordings differ ("seems scarcely possible to believe" against "is scarcely conceivable"). Hurry 2021 quotes the 1912 wording. Never splice the two.

### Evans (1982), *The Varieties of Reference* (ed. McDowell), Clarendon Press
- **Read only as quoted in Hurry 2021**, which gives page numbers:
  - Russell's Principle: one must know which object one is thinking about (p. 65).
  - "Adherence to Russell's Principle is fundamental" to his account of Russellian reference (p. 84).
  - Discriminating knowledge: a capacity to distinguish the object from all other things. Sufficient conditions: perceiving it now, being able to recognise it, knowing distinguishing facts (p. 89).
- **Tenet alignment**: neutral. Evans's view is no phenomenal requirement, since descriptive identification can satisfy it.
- **Note**: per Smithies's abstract, Evans also gives consciousness an essential role in demonstrative thought. The details are not read.

### Lewis on "relations of acquaintance" (as quoted by Recanati 2009, p. 18)
- *Verified in Recanati*: "In each case there are causal chains from him to me of a sort which would permit a flow of information. Perhaps I do get accurate information; perhaps I get misinformation, but still the channel is there. I call such relations as these relations of acquaintance".
- **Tenet alignment**: conflicts with P2. This is the cleanest statement of informational acquaintance, and the one that makes the LLM question live.

### Recanati (2009), "(Anti-)Descriptivism, Mental Files, and the Communication of Singular Thoughts", *Manuscrito* 32(1): 7–32
- **URL**: https://periodicos.sbu.unicamp.br/ojs/index.php/manuscrito/article/download/8642058/9549/13324
- **Key points**:
  - Singularism against Descriptivism (p. 9).
  - The lineage of the file idea (p. 17).
  - Files are based on epistemically rewarding relations (p. 18).
  - The SELF file, based on identity (p. 19, citing Perry 2000).
  - Quine's elimination of singular terms as the descriptivist programme (p. 8, "as Quine recommended (Quine 1960: 181-6)").
- **Verified quotes**:
  - "singular thought about an object involves nondescriptive or de re ways of thinking of that object, that is, modes of presentation resting on contextual relations of 'acquaintance' to the object" (abstract; the 2010 chapter abstract uses the same words).
  - "We can think of them directly, if we are acquainted with them in experience; or we can think of them indirectly, qua bearers of such and such properties." (p. 9)
  - "Some of these relations — the acquaintance relations — are epistemically rewarding in that they enable the subject to gain information from the object." (p. 18)
  - "The role of a mental file based on a certain acquaintance relation is to store information acquired in virtue of that relation." (p. 18)
  - "According to Perry (2000), the concept of self is a type of mental file that is based upon a special relation which every individual bears to himself or herself, namely identity." (p. 19)
- **Tenet alignment**: neutral to conflicting with P2. Recanati's own gloss on singularism says "in experience", but his acquaintance is informational.

### Recanati (2010), "Singular Thought: In Defence of Acquaintance", in Jeshion (ed.) 2010, pp. 141–190 (OpenAlex), doi:10.1093/acprof:oso/9780199567881.003.0006
- The abstract was verified (OpenAlex). The full text was not read; HAL sits behind Anubis.
- **Via Ninan 2011** (paraphrase only):
  - Intuitions about cases are unstable.
  - Recanati's Ann/tennis example (p. 168), offered as a reductio of Hawthorne and Manley's report-based test.
  - Files give a characterisation "independent of our reporting practices" (p. 169).
- **Via Leonardi 2013, on the 2012 book**: Recanati allows acquaintanceless singular thought in some cases: expected acquaintance ("Jack the Ripper"), imagined acquaintance, and others.

### Recanati (2012), *Mental Files*, OUP, doi:10.1093/acprof:oso/9780199659982.001.0001
- Not read. The OUP blurb (OpenAlex) is the **publisher's** wording, not Recanati's.
- From Leonardi's review (*verified* as Leonardi's words): "Perceptual acquaintance is the paradigm case of an epistemically rewarding relation."
- Leonardi also reports encyclopedic files based on a "higher-order epistemically rewarding relation" (p. 74). Paraphrase this. Encyclopedic files are the file type that most of our Robespierre-thoughts would use.

### Jeshion (2010), "Singular Thought: Acquaintance, Semantic Instrumentalism, and Cognitivism", in Jeshion (ed.) 2010, pp. 105–140, doi:10.1093/acprof:oso/9780199567881.003.0005
- **Chapter abstract, verified (OpenAlex)**:
  - "The reigning view is that singular thinking is limited to objects of acquaintance."
  - "Like acquaintance views, Cognitivism limits singular thought, but the limitations are not strictly epistemic, but rather, cognitive, associated with the goals, interests, plans, and affective states of the thinker."
  - It also says Cognitivism "supports a mental file analysis of singular thought" and draws on vision science.
- **Via Ninan only** (paraphrase): the significance condition (p. 136); the bear-scat campsite case (p. 117); her rejection of semantic instrumentalism, in agreement with Salmon.
- **Critics** (abstracts verified):
  - Sawyer 2012, *Mind & Language* 27(3): 264–283. A revised acquaintance theory with "'trace‐based' acquaintance" that distinguishes "unsuccessful thoughts of singular form from successful singular thoughts".
  - Goodman 2016, *Phil. Quarterly* 66(263): 236–260 (online 2015). The "connection she makes between significance and singularity does not hold".

### Hawthorne and Manley (2012), *The Reference Book*, OUP, doi:10.1093/acprof:oso/9780199693672.001.0001
- Not read. **Via Abbott 2013 only**:
  - "Liberalism": no general acquaintance restriction on reference or singular thought (p. 24).
  - The target principle "constraint": having a singular thought about an object requires acquaintance with it (p. 37).
  - They answer the spy argument and the Neptune argument.
  - Ch. 3 attacks epistemic acquaintance, Evans's discrimination view included.
  - Part II gives a quantificational semantics for names, demonstratives and descriptions.
- **Verified, Abbott's words**: their first objective is "to demolish the common assumption, following Bertrand Russell, that some kind of acquaintance is required for both (singular) reference and singular thought."
- **Tenet alignment**: a rival to P1, presented on its merits.

### Campbell (2002), *Reference and Consciousness*, OUP, doi:10.1093/0199243816.001.0001
- **Abstract, verified (Crossref)**:
  - "Conscious attention to an object, singling it out in experience, provides knowledge of the reference of a demonstrative term."
  - "Knowledge of reference demands acquaintance with the individual, categorical substances around us, and not merely collections of affordances."
  - "I argue that only experience of objects can provide this kind of acquaintance with individual substances."
  - Knowledge of reference grounds "the ability to act on the object".
- **Tenet alignment**: supports a consciousness condition for demonstratives. Campbell is a **relationalist**: `naturalist-relationalism` engages him as the strongest non-dualist rival. The blindsight argument is not verified this run.

### Smithies (2011), "What Is the Role of Consciousness in Demonstrative Thought?", *J. Phil.* 108(1): 5–34, doi:10.5840/jphil201110811
- **Abstract, verified (OpenAlex)**:
  - "Does perception enable demonstrative thought only if it is conscious?"
  - The three accounts "agree that consciousness is essential for demonstrative thought, but disagree about why it is".
  - He rejects Evans's and Campbell's accounts.
  - "My proposal is that consciousness plays an essential epistemic role in explaining the capacity for demonstrative thought about an object by enabling the subject to form immediately justified beliefs about the object".
- **Tenet alignment**: supports consciousness-dependence through an epistemic route. Do not describe Smithies's metaphysics (not checked).

### Barkasi (2019), "The role of experience in demonstrative thought", *Mind & Language* 34(5): 648–666, doi:10.1111/mila.12228
- **Abstract, verified**: "Attention plays a role in demonstrative thought: It sets the targets." Also: "Campbell and Smithies also identify roles for experience, but they further argue that only experience can play those roles." He denies the *only*.
- **Tenet alignment**: the live rival to Finding 2.

### Hattiangadi and Schoubye (forthcoming), "The Outputs of Large Language Models are Meaningless", arXiv:2509.22206
- **Verified in the raw PDF** (manuscript pp. 15–16; the PDF uses "ﬁ" ligatures):
  - Cappelen and Dever "combine this account with the suggestion that names are associated with mental files (Recanati, 2012)".
  - LLMs "cannot store semantic information either implicitly or explicitly".
  - "have no information to assemble in even a metaphorical mental file".
  - The homonym case: "Though there are millions of people called Muhammad, an LLM will have just one vector encoding of the name."
  - The deeper worry: "there are causal relations all over the place, but not every effect of a cause is a representation of its cause."
- **Consistency**: matches the LLM page L106's gloss exactly.

### Interpretability on entity representations (arXiv abstracts, verified)
- **Meng, Bau, Andonian and Belinkov 2022** (arXiv:2202.05262; NeurIPS 2022). Factual associations sit in "a distinct set of steps in middle-layer feed-forward modules that mediate factual predictions while processing subject tokens."
- **Ferrando, Obeso, Rajamanoharan and Nanda** (arXiv:2411.14257; ICLR 2025).
  - Entity recognition is "where the model detects if an entity is one it can recall facts about".
  - The directions are "causally relevant".
  - "Self-knowledge" is the authors' gloss. Do not import it.
- **Sakata, Heinzerling, Yokoi, Ito and Inui** (arXiv:2506.02701; ACL 2025 Findings).
  - "mentions of the same entity cluster together and mentions of different entities remain separated", with "precision and recall ranging from 0.66 to 0.9".
  - This bears on the Muhammad objection. H&S's "one vector encoding" is true of the token embedding, but contextual representations partly separate same-name mentions. That reading is the Map's, not Sakata et al.'s.
- **Yona, Barzilay, Karasik and Geva** (arXiv:2604.01404, **April 2026 preprint**, not peer-reviewed). Entity cells are "recovered under aliases, acronyms, misspellings, and multilingual surface forms". The authors read this as encoding "canonical entity identity rather than surface token patterns". The aliases tested are attested ones, **not names coined in context**.
- **Feng and Steinhardt** (arXiv:2310.17191; ICLR 2024 per standard citation, venue not verified). In-context "binding ID vectors" attach to entities and attributes.
- **Bogdan and Lindsey** (arXiv:2604.21139, **2026 preprint**). Current-entity and prior-entity "slots". They report "a gap between information that is available in activations and information the model actually uses". This bears directly on what "storing information" should mean in the H&S debate.

### Secondary surveys (verified raw)
- **SEP "Singular Propositions"** (Fitch and Nelson). The spectrum runs "from Russell's restrictive view of direct reference, according to which an agent can only think directly about her occurrent sense data, to the liberal view of direct reference held by Kaplan and Jeshion, according to which objects that have never been perceived can be thought about directly." The section on Strawson's reduplication argument is there too.
- **Palmira 2020** (NDPR): "Mental files are mental representations whose main function is to enable the collection and storage of information about the particular object they refer to." Also Sainsbury's and Reimer's deflationary chapters (2020), which ask whether singular-thought debates are substantive.
- **Azzouni 2011 abstract**: "Tim Crane (2011) characterizes the cognitive role of singular thought via singular mental files". Crane 2011 itself is not read; metadata verified.
- **Dickie 2015**, ch. 7 abstract: names "the two main extant views of the nature of singular thought: the extended acquaintance view; and 'cognitivism'".

## Major Positions {#positions}

### Strict Russellian acquaintance
- **Proponents**: Russell 1910–11 and 1912.
- **Core claim**: P1 plus P2. The objects of acquaintance are sense-data, universals and perhaps the self.
- **Relation to tenets**: the only view on which P2 is plainly true, and the one with the narrowest scope.

### Evans: Russell's Principle as discriminating knowledge
- **Proponents**: Evans 1982 (defended exegetically by Hurry 2021).
- **Core claim**: thinking about an object requires knowing which object. Perception, recognition or distinguishing facts can supply it.
- **Relation to tenets**: no phenomenal requirement in general. Per Smithies, Evans does give consciousness a role for demonstratives.

### Extended, informational acquaintance and mental files
- **Proponents**: Lewis; Bach (perception, memory, testimony; the "representation connection"); Recanati; Dickie (three thought-enabling relations, including testimony and description, per Walker's review abstract); Sawyer (trace-based).
- **Core claim**: P1 with a non-phenomenal acquaintance: an information-bearing causal relation. Singular thought is thinking through a file.
- **Relation to tenets**: denies P2. This makes LLM acquaintance a live question.

### Consciousness-based accounts of demonstrative thought
- **Proponents**: Campbell 2002; Smithies 2011.
- **Core claim**: perceptual demonstrative thought requires consciousness. Campbell: experience provides acquaintance with substances. Smithies: consciousness provides immediate justification.
- **Relation to tenets**: the only branch on which C holds. Both authors are non-dualists.

### Semantic Instrumentalism
- **Proponents**: Kaplan ("Dthat" 1978; Newman1; Le Verrier's "Neptune"); Jeshion's label.
- **Core claim**: introducing a directly referential term by a uniquely satisfied description puts one in a position to have singular thoughts.
- **Relation to tenets**: denies P1. Rejected by Jeshion, Salmon and Recanati (via Ninan).

### Cognitivism
- **Proponents**: Jeshion 2010.
- **Core claim**: no acquaintance requirement, but a *significance* condition tied to the thinker's goals, plans and affective states. This supports a mental-file analysis.
- **Relation to tenets**: denies P1, yet makes singular thought *more* subject-involving (Finding 3).

### Liberalism about singular thought
- **Proponents**: Hawthorne and Manley 2012.
- **Core claim**: there is no general acquaintance restriction on reference or singular thought. The spy and Neptune arguments for the constraint fail.
- **Relation to tenets**: denies P1. Present it on its merits, as a live rival.

### Deflationary and non-unitary views
- **Proponents**: Sainsbury 2020 and Reimer 2020 (via Palmira); Moldovan 2015 (referential fitness against success, after Taylor 2010 and Crane 2013); Azzouni 2011 ("objects-directed thought").
- **Core claim**: "singular" names several phenomena. Some disputes may not be substantive.
- **Relation to tenets**: a caution against building any Map conclusion on a single notion of singularity.

## Key Debates {#debates}

### Is acquaintance necessary?
- **Sides**: Russell, Evans, Recanati and Sawyer (yes, variously construed) against Kaplan, Jeshion, and Hawthorne and Manley (no).
- **Core disagreement**: whether Neptune-, Newman1- and bear-scat-type cases are genuine singular thoughts.
- **Current state**: open. Recanati's methodological point is that intuitions about cases are "not particularly robust" (Ninan's words, *verified*).

### Is the acquaintance requirement trivial on file views?
- **Sides**: Ninan (the worry) against Recanati (files independently characterised).
- **Current state**: open. The question moves to what counts as an acquaintance relation.

### Does demonstrative thought require consciousness, and why?
- **Sides**: Campbell (experience gives acquaintance with substances), Smithies (epistemic) and Evans (per Smithies) against Barkasi (experience is not the only route). Pylyshyn's visual indexes are the sub-personal model in the background.
- **Current state**: open. This is the Map's best foothold, and it is supplied by non-dualists.

### Are mental files empirically respectable?
- **Sides**: Jeshion and Recanati (files modelled on object files) against Murez, Smortchkova and Strickland 2020 (the analogy holds only for a limited range; via Palmira).
- **Current state**: partial support for perceptual-demonstrative files. Memory and communication files are unsettled.

### Do language models have anything like files?
- **Sides**: Cappelen and Dever (dominant causal source, combined with files) against Hattiangadi and Schoubye (no information to file). Interpretability work is now relevant evidence.
- **Current state**: the vehicle-level evidence favours file-like organisation. Whether that organisation stores *information* in H&S's sense, rather than causal covariation, is untouched. See [the LLM bearing](#llm).

## Bearing on the Language-Model Page {#llm}

The article must stay consistent with `whether-language-model-words-refer`, which I read on disk this run. That page holds that current LLM words refer *derivatively*, as a book's words do, and never by deference. The verdict holds only if current LLMs are not conscious (P-AC1). Novel reference is the hardest case. Option 1 there, derivation through the dominant causal source, is "the Map's proposal, untested" and must meet Hattiangadi and Schoubye's two objections.

1. **Words against thought.** The LLM page answers whether an LLM's *words* carry singular reference (derivatively, through authors). This topic asks whether there is singular *thought*.
   - On the Map's view, a current LLM has no singular thought of its own, if P-AC1 holds, because there is no thinker (moderate PIT).
   - It does **not** follow from lacking acquaintance. On Lewis's or Recanati's informational notion, a trained LLM arguably stands in causal channels to Robespierre through its training texts.
   - The article should say plainly that the Map's verdict rests on the thinker condition (Finding 3).
2. **The file mechanism for option 1** (the Map's proposal, untested).
   - Cappelen and Dever already pair their principle with files (per H&S, verified).
   - A name coined for an object already represented inherits that representation's referent. "Marion Starlight", attached to a Robespierre representation, would pick out Robespierre derivatively, with the referential relation running through the training texts' authors.
   - Recanati's encyclopedic files (via Leonardi) show the human case of a name attaching to an existing body of information.
   - **Prediction**: in a model that coins such a name, the coined name should route through the same internal entity representation as "Robespierre" (testable by activation patching).
   - **No study found tests a name coined in context.** Yona et al. test attested aliases only.
3. **What the interpretability work does and does not show.**
   - **Does**: entity-keyed storage (Meng et al.), a recognised-entity signal that the model uses (Ferrando et al.), clustering of mentions of the same entity (Sakata et al.), alias-invariant entity units (Yona et al., preprint), and in-context binding (Feng and Steinhardt; Bogdan and Lindsey, preprint). These tell against H&S's premise that LLMs "cannot store semantic information either implicitly or explicitly", *at the level of functional architecture*.
   - **Does not**: settle H&S's deeper point that "not every effect of a cause is a representation of its cause". That is the Map's own "thin grounding" line on `symbol-grounding-problem`, and the Map cannot use the interpretability results against H&S without giving up that line. Nor does the work show a thinker.
   - The Murez–Smortchkova–Strickland caution about the object-file analogy applies equally to reading these as "files".
4. **The Muhammad objection.** Sakata et al.'s ambiguity results suggest that contextual representations partly separate mentions of different people who share a name. This weakens the "just one vector encoding" premise, read as a claim about processing rather than input embeddings. The scores are 0.66 to 0.9, so the separation is partial. This is the Map's reading.
5. **Expressible versus impressible.** Reimer (2020, via Palmira) separates singular content a term *expresses* from singular thought anyone *has* through it. This gives the Map a precise way to say that a novel name can express singular content derivatively while no singular thought is had through it. Paraphrase only.

## Bearing on Tenet 4 {#tenet-4}

- **First person.**
  - Russell was undecided about self-acquaintance in 1910–11 and gave it only "_probably_" in 1912 (*verified*).
  - On the Perry and Recanati SELF file, "I" is anchored in *identity*, a relation every individual bears to itself (*verified*, Recanati 2009, p. 19).
  - First-person singular reference is therefore secured by a non-phenomenal relation, and is the cheapest case of all.
  - If a subject branched, each successor's SELF file would refer to that successor. So the theory presupposes the determinate bearer that the Tenet 4 indexical question asks about (`tenets.md` L117: the framework's resources "presuppose the very centred subject the question asks after").
  - **Article line**: singular-thought theory neither supports nor threatens Tenet 4. It shows that the indexical question lies beyond reference semantics. Link `indexical-knowledge-and-identity` (*de se*) and `immunity-to-error-through-misidentification` (Evans).
- **Demonstratives.**
  - Strawson's reduplication argument (SEP, verified) shows that purely qualitative descriptions cannot tell Bill from his duplicate Bill*. Only a relational, demonstrative tie picks one out.
  - The *structure* parallels the indexical objection: qualitative information underdetermines *which*. Present it as a parallel, not as support. Many-worlds branches are not qualitative duplicates.

## Historical Timeline

| Year | Event / Publication | Significance |
|------|---------------------|--------------|
| 1910–11 | Russell, "Knowledge by Acquaintance and Knowledge by Description" | Acquaintance as presentation; the fundamental principle. |
| 1912 | Russell, *Problems of Philosophy*, ch. 5 | Restated principle. Self-acquaintance "probably". |
| 1959 | Strawson, *Individuals* (pp. 20–22) | Reduplication argument; demonstrative identification fundamental. |
| 1960 | Quine, *Word and Object* (181–6, per Recanati) | Elimination of singular terms: the descriptivist programme. |
| 1968 | Kaplan, "Quantifying In" (*Synthese* 19) | *De re* belief; the photograph analogy (per Salmon via Ninan). |
| 1969 | Grice (p. 140, per Recanati) | "Dossier" introduced incidentally. |
| 1974 | Strawson (pp. 54–56, per Recanati) | First detailed file articulation. |
| 1977/1989 | Kaplan, "Demonstratives" | Direct reference; Newman1 (per Ninan). |
| 1978 | Kaplan, "Dthat" | Semantic instrumentalism's root. |
| 1980 | Perry, "A Problem about Continued Belief" (*PPQ* 61) | The most influential file source. |
| 1982 | Evans, *The Varieties of Reference* | Russell's Principle; discriminating knowledge. |
| 1986–87 | Bach, "Thought and Object"; *Thought and Reference* | Relational against satisfactional. |
| 1992 | Kahneman, Treisman and Gibbs, "The reviewing of object files" | Vision-science object files. |
| 2001 | Pylyshyn, "Visual indexes, preconceptual objects, and situated vision" | Sub-personal indexing. |
| 2002 | Campbell, *Reference and Consciousness*; Jeshion, "Acquaintanceless De Re Belief" | Consciousness for demonstratives; the anti-acquaintance turn. |
| 2009–10 | Recanati, *Manuscrito*; Jeshion (ed.), *New Essays on Singular Thought* | Files and acquaintance; cognitivism. |
| 2011 | Smithies, *J. Phil.*; Crane, *PAS Supp.* | The epistemic role of consciousness; singularity as cognitive role. |
| 2012 | Recanati, *Mental Files*; Hawthorne and Manley, *The Reference Book*; Sawyer | Mature file theory; liberalism; trace-based acquaintance. |
| 2015–16 | Dickie, *Fixing Reference*; Goodman, *PQ* | Extended acquaintance; a critique of cognitivism. |
| 2020 | Goodman, Genone and Kroll (eds.), *Singular Thought and Mental Files* | The file framework stress-tested. |
| 2021 | Cappelen and Dever, *Making AI Intelligible* | Dominant-causal-source denotation for AI. |
| 2022–26 | Meng et al.; Feng and Steinhardt; Ferrando et al.; Sakata et al.; Yona et al.; Bogdan and Lindsey | Entity representations in LLMs. |
| 2024–25 | Lederman and Mahowald ("Marion Starlight"); Hattiangadi and Schoubye | The novel-reference problem; the no-files objection. |

## Potential Article Angles

**Recommended**: angle 1, with angle 2 compressed into one section.

1. **"How much acquaintance does thinking about a thing need?"** Survey the requirement and its rivals, then run the scope–phenomenality trade-off as the Map's synthesis. It ends with the narrow conditional, the thinker-condition point, the LLM application, and Tenet 4.
2. **"Words, files and thinkers."** Lead with the LLM case. This risks duplicating the LLM page, so use it only as the closing applied section.

**Suggested outline** (section anchors in braces; about 2,600–3,000 words in total):
1. Lead, front-loaded. State the question, the conditional in one sentence, the verdict (narrow, conditional, and consciousness-dependence rather than dualism), and the LLM upshot. Use named anchors: "explained below" links to the trade-off and the LLM section.
2. What singular thought is {#what}. Relational against satisfactional (Bach), Neptune, Newman1, and the reduplication argument. About 250 words.
3. Russell's requirement {#russell}. Presentation, the principle and the narrow scope. About 300 words.
4. Evans and Russell's Principle {#evans}. About 200 words.
5. Acquaintance as an information channel {#channels}. Lewis, Bach, Recanati files, Sawyer, and Ninan's triviality worry. About 350 words.
6. The liberal views {#liberal}. Semantic instrumentalism, cognitivism and liberalism, on their merits, with the critics (Sawyer, Goodman). About 350 words.
7. Where consciousness enters: demonstratives {#demonstratives}. Campbell, Smithies, Barkasi and Pylyshyn. About 300 words.
8. The scope–phenomenality trade-off {#trade-off}, the Map's synthesis. Findings 1–4. About 300 words.
9. Language models: words, files and thinkers {#language-models}. About 350 words.
10. Relation to Site Perspective:
    - *Dualism*: the conditional only.
    - *No Many Worlds*: the SELF file presupposes the centred subject; the reduplication parallel.
    - *Occam's Razor Has Limits*: the descriptivist, Quinean elimination is the simpler story, and the reduplication argument shows qualitative description underdetermining reference.
    - *Bidirectional Interaction*: weak. Campbell ties knowledge of reference to "the ability to act on the object", which is suggestive only; Campbell is no interactionist.
    - *Minimal Quantum Interaction*: not engaged. Say so, or omit.
11. Further Reading and References.

## Guards for the Article Writer {#guards}

**Calibration rule (binding):**
- The dualist result is **conditional and narrow**. State the conditional (P1 and P2, hence C) and say that P2 fails for every broad-scope acquaintance view. Where C holds (perceptual demonstratives), it yields consciousness-dependence, which Campbell and Smithies, both non-dualists, accept. The step to dualism needs P3, argued elsewhere.
- **Never present any of this as evidence for dualism.**
- Present the liberal views (Jeshion; Hawthorne and Manley; Kaplan) as live rivals on their merits, with their arguments (the spy argument, the Neptune argument, the bear case) and their critics.
- Findings 1–4 and the file mechanism for option 1 are **the Map's own framings**. Label them ("the Map's reading", "on the Map's synthesis").
- **LLM**: keep words and thought apart.
  - The Map's position (LLM words refer derivatively; P-AC1) is about *words*.
  - The singular-thought verdict for current LLMs (no singular thought of their own) follows from the **thinker** condition, not from a lack of acquaintance.
  - The interpretability evidence concerns vehicles. It shows neither semantic information in H&S's sense nor thought.
  - The coined-name routing prediction is **untested**.
  - Yona et al. and Bogdan and Lindsey are 2026 **preprints**.

**Author stances:**
- **Russell**: "the dualism of subject and object" is a claim about the relational structure of cognition, made to avoid materialism *and* idealism (the same paragraph, *verified*). **Do not cite it as mind–body dualism.** Russell's later metaphysics is not checked here; do not characterise it.
- **Evans**: not a phenomenal-acquaintance theorist. Distinguishing facts can satisfy his principle.
- **Campbell**: a naive realist (relationalist), engaged as a rival on `naturalist-relationalism`. His "experience" is a relation to the object.
- **Smithies**: the role of consciousness is *epistemic*, through immediate justification. Do not describe his metaphysics.
- **Recanati**: an anti-descriptivist singularist. His acquaintance is informational, and he allows some acquaintanceless cases (via Leonardi).
- **Jeshion**: rejects both the acquaintance requirement and semantic instrumentalism. Cognitivism is her middle path.
- **Hawthorne and Manley**: liberals about singular thought. They also argue that names, demonstratives and descriptions are quantificational. Do not describe them as denying singular thought exists.
- **Lewis**: a physicalist. His acquaintance relations are causal channels.
- **Hattiangadi and Schoubye**: argue that LLM outputs are meaningless, on intention-based grounds. They are not dualists.
- **Ferrando et al.**: "self-knowledge" is their gloss. Do not echo it.

**Do-not-quote list.** Paraphrase these, or quote only with an "as quoted in" attribution:
- Evans's formulations of Russell's Principle (pp. 65, 84, 89), seen only in Hurry 2021. The term "discriminating knowledge" may be used, attributed to Evans.
- Hawthorne and Manley's definitions of "liberalism" (p. 24) and "constraint" (p. 37), seen only in Abbott.
- Jeshion's significance formula (p. 136) and the bear case (p. 117), seen only in Ninan. Her **chapter-abstract** sentences above are quotable, as "the chapter abstract".
- Recanati's Ann example (p. 168) and "independent of our reporting practices" (p. 169), via Ninan.
- Bach's "representation connection" passage (p. 58), via Ninan. Bach's "RELATIONALLY" sentence comes via Recanati 2009 fn 7.
- Lewis's "relations of acquaintance" passage. Quotable only as "quoted in Recanati 2009, p. 18". The original locus is unverified.
- Reimer's "expressible … impressible", via Palmira.
- The *Mental Files* OUP blurb is the publisher's wording.
- Campbell on blindsight: unverified. Do not describe his blindsight argument.
- Russell: give **no page numbers** for single quotations; the editions read have none. Never splice the 1910–11 and 1912 wordings.

**Coiner and populariser:**
- "Russell's Principle" is Evans's label for a principle he attributes to Russell. Write "what Evans calls Russell's Principle".
- The mental file is not Recanati's coinage: Grice 1969, then Strawson 1974, then Perry 1980.
- "Liberalism" in this sense is Hawthorne and Manley's. "Semantic Instrumentalism" and "Cognitivism" are Jeshion's.
- "Dthat" is Kaplan's, dated **1978**.

**Conflations to avoid:**
- Acquaintance with *qualities* (`phenomenal-acquaintance`) against acquaintance with *particulars* (this topic).
- McDowell and Kelly's *demonstrative concepts* of shades (`phenomenal-acquaintance` L102) against demonstrative singular thought about objects.
- Object files (vision science, sub-personal) against mental files (personal-level modes of presentation).
- *De re* against *de se*.
- Reference of names (Kripkean chains) against singularity of thought.
- The two senses of "liberalism" (singular thought; cognitive phenomenology in P-TU1).

**House style**: do not use the "This is not X. It is Y." construct. Use "load-bearing" only where it is structural.

## Integration (for the expand-topic writer and later refines) {#integration}

Host lengths are measured by `analyze_length` at 14:0xZ. Headroom = hard − 1 − total.

| Host | Total / prose / apparatus | Hard | Headroom | Suggested change |
|---|---|---|---|---|
| `topics/whether-language-model-words-refer` | 3,051 / 2,666 / 385 (soft warning) | 4,000 | 948 | In §Novel Reference option 1 (L106), add one sentence: the file reading of option 1 and the untested routing prediction, linking the new page (about 35–50 words). Add a Further Reading line. |
| `concepts/phenomenal-acquaintance` | 3,031 / 2,594 / 437 | 3,500 | 468 | In §Russell's Original Distinction (L50–L52), add one sentence: Russell also made acquaintance a condition on *understanding propositions about particulars*, which is the root of the singular-thought debate, with a piped link (about 30 words). |
| `concepts/naturalist-relationalism` | 2,433 / 2,229 / 204 | 3,500 | 1,066 | At L47, pipe "think demonstratively about objects" to the new page. Zero words. |
| `topics/philosophy-of-language-under-dualism` | 2,725 / 2,431 / 294 | 4,000 | 1,274 | Add a 1–2 sentence pointer in §Meaning as Requiring Consciousness or §The Semantic Gap. |
| `concepts/indexical-knowledge-and-identity` | 3,188 / 2,879 / 309 | 3,500 | 311 | Further Reading line on *de re* against *de se* (about 12 words). |
| `concepts/symbol-grounding-problem` | 2,565 / 2,250 / 315 | 3,500 | 934 | Further Reading line. |
| `concepts/immunity-to-error-through-misidentification` | 2,925 / 2,421 / 504 | 3,500 | 574 | Optional Further Reading line (Evans). |
| `voids/acquaintance-void` | 2,345 / 2,032 / 313 | 3,000 | 654 | Optional. |
| `concepts/intentionality` | 3,488 / 2,990 / 498 | 3,500 | **11** | **Length-neutral only**: a piped link inside existing text, or skip. |

## Gaps in Research

- Primary texts were not read for Evans 1982, Recanati 2010 and 2012, Jeshion 2010, Hawthorne and Manley 2012, Campbell 2002 (abstract only) and Smithies 2011 (abstract only). Positions are reported via verified reviews, abstracts and theses.
- Campbell's blindsight argument and any explicit Campbell–Pylyshyn exchange are not checked.
- The original locus of Lewis's "relations of acquaintance" passage (1979 or 1983) is not verified.
- No study was found that tests whether an LLM's *coined-in-context* name routes through an existing entity representation. That is the experiment that would decide option 1 against H&S at the vehicle level.
- No philosophical paper was found that applies the singular-thought literature to LLMs directly (two searches). The Map's application may be early. Say "no paper found", not "none exists".
- Literature on phenomenal intentionality and singular thought (Kriegel, Mendelovici, Horgan–Tienson) was not found in one search. Do not claim PIT theorists have addressed singular thought until that is checked.
- The titles of Grice 1969 and Strawson 1974 are not checked.

## Citations

1. Abbott, B. (2013). Review of Hawthorne & Manley, *The Reference Book*. *Notre Dame Philosophical Reviews* 2013.02.10. https://ndpr.nd.edu/reviews/the-reference-book/
1. Azzouni, J. (2011). Singular thoughts (objects-directed thoughts). *Aristotelian Society Supplementary Volume* 85(1): 45–61. https://doi.org/10.1111/j.1467-8349.2011.00195.x
1. Bach, K. (1987). *Thought and Reference*. Oxford University Press. (Cited via Recanati 2009.)
1. Barkasi, M. (2019). The role of experience in demonstrative thought. *Mind & Language* 34(5): 648–666. https://doi.org/10.1111/mila.12228
1. Bogdan, P. C. & Lindsey, J. (2026). Slot machines: How LLMs keep track of multiple entities. arXiv:2604.21139 (preprint).
1. Campbell, J. (2002). *Reference and Consciousness*. Oxford University Press. https://doi.org/10.1093/0199243816.001.0001
1. Cappelen, H. & Dever, J. (2021). *Making AI Intelligible*. Oxford University Press. https://doi.org/10.1093/oso/9780192894724.001.0001
1. Crane, T. (2011). The singularity of singular thought. *Aristotelian Society Supplementary Volume* 85(1): 21–43. https://doi.org/10.1111/j.1467-8349.2011.00194.x
1. Dickie, I. (2015). Descriptions and singular thought. In *Fixing Reference*, ch. 7, pp. 247–272. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780198755616.003.0007
1. Evans, G. (1982). *The Varieties of Reference* (J. McDowell, Ed.). Clarendon Press. (Read via Hurry 2021.)
1. Feng, J. & Steinhardt, J. (2023). How do language models bind entities in context? arXiv:2310.17191.
1. Ferrando, J., Obeso, O., Rajamanoharan, S. & Nanda, N. (2025). Do I know this entity? Knowledge awareness and hallucinations in language models. *ICLR 2025*. arXiv:2411.14257.
1. Fitch, G. W. & Nelson, M. (1997/2013). Singular propositions. *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/propositions-singular/
1. Goodman, R. (2016). Cognitivism, significance and singular thought. *Philosophical Quarterly* 66(263): 236–260. https://doi.org/10.1093/pq/pqv074
1. Goodman, R., Genone, J. & Kroll, N. (Eds.) (2020). *Singular Thought and Mental Files*. Oxford University Press. (Via Palmira 2020.)
1. Hattiangadi, A. & Schoubye, A. J. (forthcoming). The outputs of large language models are meaningless. In H. Cappelen & R. Sterken (Eds.), *Communicating with AI*. Oxford University Press. arXiv:2509.22206.
1. Hawthorne, J. & Manley, D. (2012). *The Reference Book*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199693672.001.0001
1. Hurry, D. A. (2021). *Vindicating Evans: A Defence of Evans' Theory of Singular Thought*. PhD thesis, Western University. https://ir.lib.uwo.ca/etd/7655
1. Jeshion, R. (2002). Acquaintanceless de re belief. In J. Campbell, M. O'Rourke & D. Shier (Eds.), *Meaning and Truth* (pp. 53–78). Seven Bridges Press. (Via SEP.)
1. Jeshion, R. (Ed.) (2010). *New Essays on Singular Thought*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199567881.001.0001
1. Jeshion, R. (2010). Singular thought: Acquaintance, semantic instrumentalism, and cognitivism. In Jeshion (Ed.) 2010, pp. 105–140. https://doi.org/10.1093/acprof:oso/9780199567881.003.0005
1. Kahneman, D., Treisman, A. & Gibbs, B. J. (1992). The reviewing of object files: Object-specific integration of information. *Cognitive Psychology* 24: 175–219. https://doi.org/10.1016/0010-0285(92)90007-O
1. Kaplan, D. (1978). Dthat. In P. Cole (Ed.), *Syntax and Semantics 9: Pragmatics* (pp. 221–243). Academic Press. https://doi.org/10.1163/9789004368873_008
1. Kaplan, D. (1989). Demonstratives. In J. Almog, J. Perry & H. Wettstein (Eds.), *Themes from Kaplan* (pp. 481–563). Oxford University Press.
1. Lederman, H. & Mahowald, K. (2024). Are language models more like libraries or like librarians? *TACL* 12: 1087–1103. https://doi.org/10.1162/tacl_a_00690
1. Leonardi, P. (2013). Review of Recanati, *Mental Files*. *Notre Dame Philosophical Reviews* 2013.07.18. https://ndpr.nd.edu/reviews/mental-files/
1. Lewis, D. (1999). *Papers in Metaphysics and Epistemology*. Cambridge University Press, pp. 380–81 (as cited by Recanati 2009; the original locus is unverified).
1. Meng, K., Bau, D., Andonian, A. & Belinkov, Y. (2022). Locating and editing factual associations in GPT. arXiv:2202.05262.
1. Ninan, D. (2011). Review of Jeshion (Ed.), *New Essays on Singular Thought*. *Notre Dame Philosophical Reviews* 2011.09.25. https://ndpr.nd.edu/reviews/new-essays-on-singular-thought/
1. Palmira, M. (2020). Review of Goodman, Genone & Kroll (Eds.), *Singular Thought and Mental Files*. *Notre Dame Philosophical Reviews* 2020.06.21. https://ndpr.nd.edu/reviews/singular-thought-and-mental-files/
1. Perry, J. (1980). A problem about continued belief. *Pacific Philosophical Quarterly* 61: 317–332. (Via Leonardi and Recanati.)
1. Pylyshyn, Z. W. (2001). Visual indexes, preconceptual objects, and situated vision. *Cognition* 80: 127–158. https://doi.org/10.1016/S0010-0277(00)00156-6
1. Recanati, F. (2009). (Anti-)descriptivism, mental files, and the communication of singular thoughts. *Manuscrito* 32(1): 7–32. https://periodicos.sbu.unicamp.br/ojs/index.php/manuscrito/article/download/8642058/9549/13324
1. Recanati, F. (2010). Singular thought: In defence of acquaintance. In Jeshion (Ed.) 2010, pp. 141–190. https://doi.org/10.1093/acprof:oso/9780199567881.003.0006
1. Recanati, F. (2012). *Mental Files*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199659982.001.0001
1. Russell, B. (1910–11). Knowledge by acquaintance and knowledge by description. *Proceedings of the Aristotelian Society* 11: 108–128. Reprinted in *Mysticism and Logic* (1917), ch. X.
1. Russell, B. (1912). *The Problems of Philosophy*. Williams and Norgate, ch. 5.
1. Sakata, M., Heinzerling, B., Yokoi, S., Ito, T. & Inui, K. (2025). On entity identification in language models. *Findings of ACL 2025*. arXiv:2506.02701.
1. Sawyer, S. (2012). Cognitivism: A new theory of singular thought? *Mind & Language* 27(3): 264–283. https://doi.org/10.1111/j.1468-0017.2012.01444.x
1. Smithies, D. (2011). What is the role of consciousness in demonstrative thought? *Journal of Philosophy* 108(1): 5–34. https://doi.org/10.5840/jphil201110811
1. Strawson, P. F. (1959). *Individuals*. Methuen. (Via SEP.)
1. Walker, E. (2017). Review of Imogen Dickie, *Fixing Reference*. PhilPapers record WALIDF (abstract read via OpenAlex; full text not read).
1. Yona, I., Barzilay, D., Karasik, M. & Geva, M. (2026). Friends and grandmothers in silico: Localizing entity cells in language models. arXiv:2604.01404 (preprint).
