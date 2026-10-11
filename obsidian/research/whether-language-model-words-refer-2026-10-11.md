---
title: "Research Notes - Whether Language-Model Words Refer: Externalism, Deference and the Inverse Swampman"
created: 2026-10-11
modified: 2026-10-11
human_modified: null
ai_modified: 2026-10-11T00:50:19+00:00
draft: false
description: "Research notes on LLM reference: Mandelkern & Linzen, Ostertag, Lederman & Mahowald, Koch, Pepp, Coelho Mollo & Millière's Swamp LLM, Grindrod, Cappelen & Dever, Hattiangadi & Schoubye, and what moderate PIT says."
topics:
  - "[[ai-consciousness]]"
  - "[[the-naturalisation-failure-for-content]]"
concepts:
  - "[[content-externalism]]"
  - "[[swampman]]"
  - "[[intentionality]]"
  - "[[symbol-grounding-problem]]"
  - "[[teleosemantics]]"
  - "[[chinese-room-argument]]"
  - "[[llm-consciousness]]"
related_articles:
  - "[[conceptual-role-semantics]]"
  - "[[language-and-consciousness]]"
  - "[[consciousness-and-testimony]]"
  - "[[content-vocabulary-as-derived-feature]]"
  - "[[positions/ai-consciousness-scope]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-11
last_curated: null
---

# Research: Whether Language-Model Words Refer

**Date**: 2026-10-11
**Target section**: `topics/` (343/360 by `tools.evolution.state.count_section_files`, measured 2026-10-11). Harvested from `reviews/optimistic-2026-10-10-ancestry-and-duplicate-wing` (Executive Summary bullet 4; New Concept Pages Needed).
**Search queries used**:
- ACL Anthology `2024.cl-3.12` (Mandelkern & Linzen, published PDF fetched and grepped); arXiv `2308.05576` (v1–v3 abstract, for the wording drift)
- Crossref `works/10.1162/coli_a_00522`; OpenAlex works-by-DOI for 14 records
- `Lederman Mahowald "Are Language Models More Like Libraries or Like Librarians" bibliotechnism`
- `Ostertag "large language models and externalism about reference" negative results`
- `Baggio Murphy "referential capacity of language models" internalist rejoinder`
- `Pepp 2025 large language models reference derived meaning outputs`
- `"Babbling stochastic parrots" Kripkean argument reference large language models Koch`
- `Coelho Mollo Millière "The Vector Grounding Problem" Philosophy and the Mind Sciences 2025 published`
- `Chalmers "Does Thought Require Sensory Grounding?"`; `Cappelen Dever "Making AI Intelligible" open access`
- `phenomenal intentionality theory large language models reference derived intentionality`
- Crossref `query.bibliographic` for Pepp, Koch, Green, Coelho Mollo & Millière, Butlin, Cappelen & Dever, Bender & Koller, Ostertag 2023, Cappelen & Deutsch, Titus, Grindrod, Krzanowski
- archive.org djvu text of Kripke, *Naming and Necessity* (1980), for the p. 96 condition; Google Books search-within on volume `9vvAlOBfq0kC` (control "rigid designator" hit; p. 96 not in the indexed preview)

**Verification key used below**: [raw] = full text fetched this run and every quoted span substring-checked against it (whitespace- and quote-normalised, with a planted negative control that correctly returned zero); [abstract] = publisher or OpenAlex abstract fetched verbatim, body not read; [metadata] = Crossref/OpenAlex record only; [via X] = the claim is reported from source X, not the primary text.

## Executive Summary

The question is live, well-sourced, and absent from the Map. Mandelkern and Linzen (2024) argue from Kripke and Putnam that language-model inputs "are strings of text with natural histories, and that may suffice for LMs' words to refer" [raw]. In the four years since Bender and Koller's octopus (2020), the literature has divided at one point. **Kripke's p. 96 condition** requires that a receiver "intend when he learns it to use it with the same reference as the man from whom he heard it" [raw]. Pro-reference authors either credit LLMs with a lightweight version of that intention (Mandelkern & Linzen; interpretationists in Lederman & Mahowald 2024) or drop it: Cappelen & Deutsch's "pure externalism", Koch's architecture-as-continuity, Pepp's "basic reference", Coelho Mollo & Millière's teleosemantics. Sceptics keep the condition and deny LLMs the intentions (Ostertag 2025; Hattiangadi & Schoubye, forthcoming).

Mandelkern and Linzen name the Map's branch and leave it open: "you might think that intending requires consciousness … We leave this as an open question" [raw]. Under the Map's moderate phenomenal intentionality theory (PIT) and P-AC1, current LLM words refer *derivatively*, as a book's words do, and never by *borrowing* through deference. That is Swampman's split verdict in mirror image ([below](#the-inverse-swampman)). Coelho Mollo and Millière (2026) have already built the direct analogue, a parameter-identical "Swamp LLM", and deny it reference. The *inverse* pairing (trained LLM: history without, on P-AC1, a phenomenal source) is new to this note. Its hardest test is Lederman and Mahowald's **novel reference problem**. **Recommendation: write a `topics/` article.**

## Assessment: Is the Subject Worth an Article?

The task licensed declining. The case for writing:

1. **The Map's hybrid is directly exposed.** [[content-externalism]] L24 adopts Putnam's division of linguistic labour, and [[swampman]] L59 makes reference "the one aspect of content the environment fixes". Mandelkern and Linzen's argument uses exactly this externalist half. The Map has never said whether that half grants reference to a system with the history and without the phenomenal source. Until it does, an LLM reader can fairly infer that the Map's own externalism concedes LLM reference.
2. **No live page covers it.** `Mandelkern` has 0 live hits. `Cappelen`, `Koller`, `Ostertag` and `Pepp` (as an author) have 0. [[symbol-grounding-problem]] L99 calls the LLM's world a "quoted environment" and L105 places LLMs on the "thin grounding" side, without the reference-borrowing question. [[chinese-room-argument]] L109 names Grindrod (2024), Piantadosi & Hill and Coelho Mollo & Millière in one sentence each, and leaves Grindrod's linguistic-intentionality case unanswered.
3. **The literature is mature and recent.** Two exchanges sit in one journal (*Computational Linguistics* 50(3) and 51(2)) and one in *Philosophy of AI* 1 (Koch, then Green's reply). Further contributions appear in TACL, *Inquiry*, *Philosophy and the Mind Sciences*, *Synthese*, *Erkenntnis* and an OUP handbook, with an OUP volume forthcoming.
4. **The Map has a distinctive answer, with a real cost.** The two most-cited pro-reference intuition pumps use a human or conscious subject: Mandelkern and Linzen's Izzy, and Chalmers's pure thinker, who "would be conscious" [raw]. Each then sets consciousness aside when transferring to LLMs. The Map's answer locates the disagreement exactly there. Its cost, the novel reference problem, is specific and checkable.

Against: overlap with `symbol-grounding-problem` and `chinese-room-argument`. That overlap is on *understanding*. The new article is about *reference and deference*, a distinct question that Mandelkern and Linzen themselves separate from understanding. A concept page would be too narrow, because the subject is a debate with several positions, so `topics/` is the right section.

## Key Sources

### Mandelkern, M. & Linzen, T. (2024). "Do Language Models' Words Refer?" *Computational Linguistics* 50(3): 1191–1200 [raw]
- **URL**: https://aclanthology.org/2024.cl-3.12/ · https://doi.org/10.1162/coli_a_00522
- **Type**: Squib (short article), open access
- **Key points**:
  - The question is *semantic* reference of the words, not speaker reference: "whether the LM itself refers (whether it achieves speaker reference), which can in principle come apart from the question of whether its words refer" (p. 1192). Footnote 1 uses "word" in a thin sense, "Since we don't want to assume LMs have intentions".
  - Ants vs Luke (from Putnam 1981): an ant trail shaped like "Peano proved that arithmetic is incomplete" says nothing, while Luke's text says something false about Peano. The question is which one LLM output resembles.
  - Externalism: reference is grounded by "the causal-historical links between a speech community's use of a word and the word's referent" (p. 1194), and by deference: "Ordinary speakers use "beech" to refer to whatever tree experts take it to refer to, and that is enough to refer to beeches" (p. 1195). Hence "the natural histories of LMs' inputs may be enough to ground reference for the LMs' outputs, even if the LMs have no way to grasp or access those histories" (p. 1192).
  - The crux is speech-community membership: "On the spectrum between ants and Luke, they look closer to Luke" (p. 1196).
  - The intention objection is taken in thick and thin forms. Thin: "a speaker can produce a referential word iff she intends that word to refer to whatever its natural history in her speech community determines as its referent" (p. 1197). The less demanding version requires "some kind of implicit representation of oneself as part of a speech community and intention to refer in conformity with the word's natural history in that speech community".
  - **The Map's branch, named and left open** (p. 1197): "you might think that intending requires consciousness, or theory of mind, or self-representation, or intrinsic goals, or something else, and then argue that LMs lack these things. We leave this as an open question." Followed by "we warn against holding LMs to a higher standard than we hold ordinary speakers, like children".
  - The closing intuition pump: "Suppose that Izzy is isolated at birth in a sensory deprivation chamber" (p. 1198). Izzy communicates only by a brainwave-driven screen, and "externalism dissolves the puzzle" for LMs "In the same way". **Izzy is a human being.**
  - Hedged: "we make no claim to a decisive argument that LMs' words do refer" (p. 1193).
  - The published abstract differs from arXiv v1–v3. arXiv has "may suffice to put LMs' words into referential contact with the external world"; the published version has "may suffice for LMs' words to refer". Quote only the published wording.
- **Tenet alignment**: In tension with Tenet 1 *as the Map develops it for content*. Mandelkern and Linzen say what matters for reference is community membership, "not questions about whether LMs have the right kinds of experiences, beliefs, desires, and so on to ground reference" (p. 1198). The Map can concede the externalist half (which referent) and deny the inference to non-derivative reference (whether there is an intentional bearer).
- **Quote**: "Even if the inputs to LMs are simply strings of text, they are strings of text with natural histories, and that may suffice for LMs' words to refer."

### Kripke, S. (1980). *Naming and Necessity*. Harvard University Press, p. 96 [raw, archive.org djvu text]
- **URL**: https://archive.org/details/kripke-1980-naming-and-necessity
- **Key points**: The reference-borrowing condition: "When the name is 'passed from link to link', the receiver of the name must, I think, intend when he learns it to use it with the same reference as the man from whom he heard it. If I hear the name 'Napoleon' and decide it would be a nice name for my pet aardvark, I do not satisfy this condition." Page confirmed by the running head "96 NAMING AND NECESSITY" preceding the passage. Ostertag (2025, p. 652) quotes the first sentence identically. Hattiangadi & Schoubye (ms. pp. 14–15) quote it with an internal ellipsis and include the aardvark sentence.
- **Tenet alignment**: Neutral in itself. It is the hinge on which the Map's answer turns, because it makes reference-*borrowing* depend on an intentional state of the borrower.

### Ostertag, G. (2025). "Language Models and Externalism: A Reply to Mandelkern and Linzen." *Computational Linguistics* 51(2): 651–659 [raw]
- **URL**: https://doi.org/10.1162/coli_a_00551
- **Key points**:
  - Kripke's intention condition is ineliminable: "Referential intentions, however they are ultimately construed, are thus an ineliminable part of what grounds proper-name (and natural-kind-term) reference" (p. 652).
  - It names the two escape routes and accepts their conditional: "if we can make sense of LMs possessing referential intentions, or if deference to usage is not essential to reference, then there is no principled barrier to LMs' outputs referring". It adds: "my concern is not with the conditional, which I accept, but with the antecedent, about which I have doubts" (p. 659).
  - Against "naïve externalism" (natural history alone grounds reference) it runs a contrastive-explanation argument. History explains why 'water' refers to H₂O rather than XYZ, but not why it refers to H₂O rather than oxygen: "If water traces back via causal-historical lines to H2 O, then it traces back via causal-historical lines to oxygen as well" (p. 656). This is the *qua* problem in contrastive dress. Deference to chemists does not rescue it (Weisberg 2006 on context-sensitive chemical use).
- **Tenet alignment**: Supports the Map's direction (intentions are needed) without its ground: Ostertag gives no consciousness argument. The *qua* problem also bears on Tenet 5. The "history suffices" story is the simpler one, and it under-delivers even for human reference.
- **Quote**: "the path to the claim that LMs' outputs refer remains daunting" (p. 659).

### Lederman, H. & Mahowald, K. (2024). "Are Language Models More Like Libraries or Like Librarians? Bibliotechnism, the Novel Reference Problem, and the Attitudes of LLMs." *TACL* 12: 1087–1103 [raw]
- **URL**: https://doi.org/10.1162/tacl_a_00690
- **Key points**:
  - **Bibliotechnism** (after Gopnik's "cultural technology"): LLMs transmit content like printing presses and lack beliefs, desires and intentions. Its defining consequence: "So, according to bibliotechnism, LLMs can only produce tokens which refer or are meaningful derivatively" (p. 1090). The basic/derivative distinction is stipulated: "it is only agents—that is, entities that have beliefs, desires, and intentions—that produce tokens which refer or are meaningful basically."
  - Part I defends bibliotechnism, "showing how even novel text may inherit its meaning from original human-generated text". Derivative meaning needs an appropriate causal chain to a basically meaningful token, and causal sensitivity to the *intelligibility* of the training data. A unigram's accidental sentence fails: "The tokens are like sand blown into the shape of a sentence by the wind."
  - Part II, the **novel reference problem**. GPT-4, asked to rename a historical figure, wrote "Marion Starlight" in a text that plausibly refers to Robespierre. In an ASCII-picture variant, the model names elements of a picture it has just created. "These new names cannot derive their reference from original text, since by assumption the name is not used in the data to refer to the relevant object" (p. 1092).
  - Four human-attitude sources are examined and found wanting: RLHF (contra Coelho Mollo & Millière), creators' intentions, the prompt-writer's intentions, and readers' interpretations (contra Cappelen & Dever's interpreter-centric metametasemantics). The reader route cannot separate a beachgoer's sand-writing from the wind's, or a frog's "rain" croak: "The challenge for such theories is to eliminate the prediction that wind-produced tokens are meaningful without eliminating the prediction that LLM-produced tokens are" (p. 1095).
  - Conclusion: "If LLMs do not have these attitudes, we must either significantly change our theory of meaning or deny the intuitive datum that new names they produce can be meaningful" (p. 1097). On interpretationism LLMs have attitudes, but in a sense that "differs sharply from views that presuppose these attitudes require consciousness, sentience, or intelligence (topics about which we make no claims)" (abstract).
  - Not considered: a dominant-causal-source or description-mediated derivation of the novel name's reference from the training data. Grep for "dominant", "Evans" and "mental file" finds only the 1973 citation.
- **Tenet alignment**: The sharpest challenge to the Map. The Map is committed to a bibliotechnist-shaped verdict and must answer the novel reference problem or accept its cost. Interpretationism is the rival ontology of attitudes, and PIT rejects it as an account of original intentionality.
- **Quote**: "If LLMs do not have these attitudes, we must either significantly change our theory of meaning or deny the intuitive datum that new names they produce can be meaningful."

### Coelho Mollo, D. & Millière, R. (2026). "The Vector Grounding Problem." *Philosophy and the Mind Sciences* 7(1) [raw, published version]
- **URL**: https://doi.org/10.33735/phimisci.2026.12307 (arXiv 2304.01481 v3, Dec 2025)
- **Key points**:
  - Referential grounding is "the only kind essential". It is achieved when internal states (1) stand in causal-informational relations to the world and "(2) they have a history of selection that has endowed them with the function of carrying this information". Pre-training, post-training and in-context learning are all argued to supply selection (§6.2.1–6.2.3).
  - **§7.1 "Parameter-identical duplicates", the Swamp LLM.** M₂ is randomly initialised and by coincidence parameter-identical to a trained M₁. "Our answer aligns with the standard response to the swampman scenario": M₂ "would lack referential grounding". "What matters for grounding is not the parameter values per se, but the historical process through which those parameters were selected to perform specific functions." A brief fine-tuning would start to ground it. Footnote 28 (credited to Harvey Lederman): a frozen Swamp LLM's in-context learning is "pseudo-learning".
  - Meaning is decoupled from consciousness: "we must resist assuming that intrinsic meaning necessarily entails complex cognitive abilities such as understanding, knowledge, or consciousness".
- **Tenet alignment**: Conflicts with Tenet 1 as the Map applies it to content. Their position is the direct teleosemantic opposite of PIT. The Map's existing reply is the two-normativities argument on [[teleosemantics]]. **Citation-currency note**: [[symbol-grounding-problem]] (refs) and [[chinese-room-argument]] L133 cite the 2023 arXiv preprint. The published 2026 version exists and now contains the Swamp LLM section.
- **Quote**: "What matters for grounding is not the parameter values per se, but the historical process through which those parameters were selected to perform specific functions."

### Koch, S. (2025). "Babbling stochastic parrots? A Kripkean argument for reference in large language models." *Philosophy of AI* 1: 19–33 [raw]; Green, M. (2025). "Large Language Models and the Varieties of Meaning (Reply to Koch)." *Philosophy of AI* 1: 34–40 [abstract]
- **URLs**: https://doi.org/10.18716/ojs/phai/2025.2325 · https://doi.org/10.18716/ojs/phai/2025.11652
- **Key points**:
  - Koch keeps Kripke's chain and replaces the intention with architecture. Kripke's condition exists to secure continuity between prior and future uses. For humans an intention does this, "it is the design architecture of the LLM that serves this function for them". So "even though an LLM cannot form any intentions, the way it is built ensures that the reference that is undoubtedly present in the texts from which it is trained is transmitted to it" (p. 27). The claim covers semantic, not speaker, reference, and proper names and "paradigm terms".
  - Green (reply): Koch's strategy is "needlessly controversial" and limited in scope. LLMs instead perform Austin's *phatic* acts, so their language carries "its usual linguistic meaning" (abstract).
- **Tenet alignment**: Koch's move is, on the Map's view, a *derivation* story under another name. The continuity-securing function is the designers' and trainers' intention built into the training objective, which is how a photocopier's fidelity works. The Map can accept Koch's conclusion as a claim about derived reference.

### Pepp, J. (2025). "Reference without intentions in large language models." *Inquiry* 69(6): 2945–2963 [abstract; full text 403]
- **URL**: https://doi.org/10.1080/0020174X.2024.2448482
- **Key points**: The "historical picture" (Donnellan, Kripke) is the frontier for LLM reference. "A sticking point, however, is the role that linguistic intentions have been thought to play". Pepp urges that "we need not and should not focus on the plausibility of ascribing linguistic intentions to LLMs. Instead, the critical issue is whether LLMs can achieve a kind of basic reference that is prior to and independent of propositional attitudes such as intentions."
- **Tenet alignment**: The most direct challenge to the Map's *route*. Pepp's "basic reference" pre-dates attitudes, so if it exists the intention-consciousness link would not decide the question. Under moderate PIT, any intentionality prior to attitudes must still derive from phenomenal intentionality, or it is causal-informational covariation (the Map's "thin grounding"). **Body not read**: what Pepp's basic reference consists in is unverified.

### Cappelen, H. & Dever, J. (2021). *Making AI Intelligible*. OUP (open access) [raw]; Cappelen, H. & Deutsch, M. (2025). "Reference Without Deference." In Lepore & Stojnić (eds.), *Oxford Handbook of Contemporary Philosophy of Language*, 241–257 [abstract]
- **URLs**: https://doi.org/10.1093/oso/9780192894724.001.0001 (PDF: arXiv 2406.08134) · https://doi.org/10.1093/oxfordhb/9780192856852.013.33
- **Key points**:
  - Cappelen & Dever "de-anthropocentrise" Kripke and Evans for AI systems. Their principle (p. 111): "Denotation through dominant causal source: A system can denote an object that is the dominant causal source of a set of information given as input in the training stage." Chapter 4 adds an interpreter-centric, knowledge-maximising "metametasemantics". They bracket consciousness explicitly in the section "What This Book is Not About: Consciousness and Whether 'Strong AI' is Possible" (pp. 24–25): "The project of this book will not engage with Searle-style arguments".
  - Cappelen & Deutsch's "pure externalism": "sharing content does not depend in any way on deference, either to experts or one's linguistic community". They argue the deference requirement "is a residue of internalism/descriptivisism", and that originators including Burge did not hold deference relevant (abstract). Ostertag dates this 2024. Crossref has online publication 2025-01-23.
- **Tenet alignment**: Pure externalism removes the deference step the Map's argument uses. The Map's reply must therefore be the general one: causal sourcing without a phenomenal source upstream gives covariation, not aboutness. Hattiangadi & Schoubye (ms. p. 17) press the same point against Cappelen & Dever, that causal relations are everywhere but not every effect represents its cause. This is paraphrased because their text layer is corrupt. Note that the dominant-causal-source principle is *also* the Map's best tool against the novel reference problem, read as derivation ([below](#the-maps-hardest-case-novel-reference)).

### Hattiangadi, A. & Schoubye, A. J. (forthcoming). "The Outputs of Large Language Models are Meaningless." In Cappelen & Sterken (eds.), *Communicating with AI* (OUP). arXiv 2509.22206 [abstract verbatim; body read but **not quotable**]
- **URL**: https://arxiv.org/abs/2509.22206
- **Key points**: The argument is that "(a) that certain kinds of intentions are needed in order for LLMs' outputs to have literal meanings, and (b) that LLMs cannot plausibly have the right kinds of intentions" (abstract). §5.1 answers Mandelkern & Linzen's "Weak Deference" with Kripke p. 96. It answers Cappelen & Dever by arguing that LLMs store no information to assemble into a mental file, and the homonymous-name case ("Muhammad") defeats dominant-causal-source denotation. §6 explains apparent meaning as "ersatz meaning": interpretations chosen to maximise the reader's expected epistemic benefit. Footnote 11: if LLM outputs are not assertions, they are not testimony.
- **Text caveat**: the arXiv PDF's text layer corrupts ligatures ("maker" for *matter*, "aGtudes" for *attitudes*). Quote only the abstract. Their reproduction of Mandelkern & Linzen ("LMs obviously have the right kind of grounding to refer…", attributed to p. 4/p. 6) matches neither the published text nor its pagination and appears to be an early preprint. Do not propagate it.
- **Tenet alignment**: Converges with the Map's verdict on speaker meaning but stops short of the Map's ground: the intentions they require are not tied to consciousness. Their "ersatz meaning" is stronger than the Map needs, because the Map can grant *derived* reference where they grant none.

### Grindrod, J. (2024). "Large language models and linguistic intentionality." *Synthese* 204(2): 71 [raw]
- **URL**: https://doi.org/10.1007/s11229-024-04723-8
- **Key points**: Apply *linguistic*, not mental, metasemantics: "it is a mistake to think that the failure of LLMs to meet plausible conditions for mental intentionality thereby renders their outputs meaningless". "Instances of linguistic intentionality are reliant on a pre-existing linguistic system in a way that instances of mental intentionality need not be." On Evans's naming-practice account, LLMs are *consumers* but not *producers*: "there are certain linguistic practices—i.e. acting as a producer for a naming practice—that they cannot take part in". Consciousness is set aside: "we are setting aside questions of general intelligence, sentience, or consciousness".
- **Tenet alignment**: The most Map-compatible pro-meaning position. Grindrod's "dependency on a pre-existing linguistic system" *is* a derivation thesis, and his consumer-only status lines up with the Map's verdict: an LLM can consume a naming practice's reference but cannot originate any. The Map can absorb Grindrod rather than refute him, provided it says the linguistic system's intentionality is itself derived from its conscious producers.

### Butlin, P. (2023; online 2021). "Sharing Our Concepts with Machines." *Erkenntnis* 88(7): 3079–3095 [raw]
- **URL**: https://doi.org/10.1007/s10670-021-00491-w
- **Key points**: "Language models cannot understand human languages because they perform only linguistic tasks, and therefore cannot represent such objects and properties". Chatbots that perform world-directed tasks can, via social externalism: "Chatbots are language users, and their lack of perceptual experience is a form of incomplete understanding".
- **Tenet alignment**: Neutral. A task-based line between base models and deployed assistants that the Map's verdict does not need, since P-AC1 is about substrate, not task. Worth one sentence, because it splits the "LLM" category in a way most of the literature does not.

### Chalmers, D. J. (2023). "Does Thought Require Sensory Grounding? From Pure Thinkers to Large Language Models." *Proceedings and Addresses of the APA* 97: 22–45 [raw, arXiv 2408.09605, journal pagination present in the PDF]
- **Key points**: Pure thinkers (no senses) are possible, so sensory grounding is not required for thought or reference: "the grounding argument is not a good reason to think that LLMs cannot think about things in the world or refer to them" (p. 38). Sensory concepts are held only partially, "mediated by linguistic deference" (p. 33), as Mary's are. **But**: "As I'm thinking of them, pure thinkers would be conscious and could undergo nonsensory experiences" (p. 31). He brackets "arguments that LLMs lack consciousness or communicative intent to arguments that they are "stochastic parrots." All those arguments require separate treatment" (p. 38).
- **Tenet alignment**: Chalmers removes the *sensory*-grounding objection. The Map's objection was never sensory; it is phenomenal-intentional. Chalmers's argument stipulates exactly what the Map says is required, which is the core of [the smuggling observation](#the-smuggling-observation).

### Bender, E. M. & Koller, A. (2020). "Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data." *Proceedings of ACL 2020*: 5185–5198 [raw]
- **URL**: https://doi.org/10.18653/v1/2020.acl-main.463
- **Key points**: "We take meaning to be the relation between the form and something external to language". Formally, meaning is a relation pairing expressions *e* with "the communicative intents *i* they can be used to evoke". The "hyper-intelligent deep-sea octopus" taps a cable between two islanders and learns form, never meaning. Mandelkern and Linzen (n. 2) note that Bender & Koller's claim concerns *learning* meaning from form, not whether a system could *produce* meaningful language.
- **Tenet alignment**: Aligns with the Map's verdict that LLMs lack speaker meaning, through communicative intent rather than consciousness. The octopus is a case the externalists target, so the article should say why the Map's verdict does not depend on it.

### Piantadosi, S. T. & Hill, F. (2022). "Meaning without reference in large language models." arXiv 2208.02957 [abstract]
- **Key points**: Meaning arises from conceptual role, "the relationships between internal representational states". So meaning "cannot be determined from a model's architecture, training data, or objective function". They concede reference and claim meaning.
- **Tenet alignment**: Already answered in kind by [[conceptual-role-semantics]] (normativity and deflation horns). The reference article needs only to place it as the internalist alternative that gives up reference.

### Baggio, G. & Murphy, E. (2024). "On the referential capacity of language models: An internalist rejoinder to Mandelkern & Linzen." arXiv 2406.00159 [raw; preprint, no journal record found]
- **Key points**: The externalist claim holds only for names and natural-kind terms: "Externalist logic then applies to an important but narrow class of expressions". Indexicals and pronouns need a situated speaker: "who are 'us' and 'them' in machine outputs, when LMs cannot form referential intentions?" Modelling communicative intention "is distinct from the ability to form communicative intentions of one's own". Tokens are not words: the GPT tokeniser splits 'motionlessness' into 'motion' + 'lessness'.
- **Tenet alignment**: Supplies the Tenet 4 hook ([below](#relation-to-site-tenets)). First-person and indexical tokens are where derived reference visibly fails.

### Further sources (abstract or metadata level)
- **Krzanowski, R. (2025).** "Consciousness, normativity, and intrinsic meaning in large language models." *Philosophical Problems in Science* 79: 41–48. https://doi.org/10.59203/zfn.79.724 [abstract]. An insufficiency thesis: "even if LLMs were to possess some form of consciousness, this would not suffice to establish intrinsic semantic intentionality" (hieroglyph-copying case). It bears on the Map's conditional branch, where P-AC1 is wrong and an LLM is conscious. It also pushes against PIT's *sufficiency* direction.
- **Keshet, J. (2026).** "Why Sampling Is Not Choosing: Intentionality, Agency, and Moral Responsibility in Large Language Models." arXiv 2606.13441 [abstract]: LLMs' "apparent intentionality is derived rather than intrinsic". It reaches the Map's derived-intentionality verdict by an agency route, without a consciousness premise.
- **Ostertag, G. (2023).** "Meaning by Courtesy: LLM-Generated Texts and the Illusion of Content." *American Journal of Bioethics* 23(10): 91–93. https://doi.org/10.1080/15265161.2023.2249851 [metadata + abstract fragment]. The "courtesy" reading of LLM content. Ostertag's own 2025 reference list misprints the volume as 93.
- **Titus, L. M. (2024).** "Does ChatGPT have semantic understanding? A problem with the statistics-of-occurrence strategy." *Cognitive Systems Research* 83: 101174 [metadata].

## Major Positions

### Deferential externalism (Mandelkern & Linzen; Butlin for chatbots)
- **Core claim**: Reference passes along causal-historical chains through a speech community. An LLM trained on that community's text may be a member, and if so its words refer.
- **Key arguments**: Luke, elm/beech, Twin Earth; reference is "surprisingly disconnected from speakers' beliefs, and surprisingly easy" (p. 1198); Izzy.
- **Relation to site tenets**: The Map's hybrid accepts the premises. The dispute is whether membership requires a member with intentions, and whether intentions require phenomenal grounding.

### Intention-free externalism (Cappelen & Deutsch; Cappelen & Dever; Koch; Pepp)
- **Core claim**: Deference or referential intention is inessential. Causal sourcing, architecture, or "basic reference" transmits reference.
- **Relation to site tenets**: If true, it bypasses the Map's route. The Map's fallback is that pure causal sourcing yields covariation without aboutness, which over-generates (wind, frog, Ostertag's oxygen). The Map's verdict then becomes a claim about *which kind* of reference.

### Teleosemantic grounding (Coelho Mollo & Millière)
- **Core claim**: Training is selection, so LLM states have world-involving functions and referential grounding. A parameter-identical Swamp LLM lacks them.
- **Relation to site tenets**: The exact counterpart of the Swampman dispute. The Map's teleosemantics critique applies unchanged. What is new is that the Map must say what it thinks of the *trained* LLM, the inverse case.

### Bibliotechnism and interpretationism (Lederman & Mahowald)
- **Core claim**: Either LLM text is derivatively meaningful (bibliotechnism), in which case novel reference is a problem, or LLMs have interpretationist attitudes and novel reference is easy.
- **Relation to site tenets**: The Map holds the bibliotechnist verdict on PIT grounds. It can grant interpretationist "attitudes" as access-level functional states (cf. P-AC4) and deny that they are sources of original intentionality, so any reference they carry is still derived.

### Linguistic-intentionality metasemantics (Grindrod)
- **Core claim**: LLM outputs are meaningful because linguistic intentionality depends on a pre-existing system. LLMs are consumers, never producers.
- **Relation to site tenets**: Compatible if the system's intentionality is traced to its conscious producers. This is the derivation thesis in metasemantic vocabulary.

### Intention-based scepticism (Ostertag; Hattiangadi & Schoubye; Bender & Koller; Titus)
- **Core claim**: Referential or communicative intentions are required, and LLMs lack them, so the outputs are meaningless or meaningful only "by courtesy".
- **Relation to site tenets**: Agrees with the Map on speaker meaning. It is stronger than the Map on derived reference and weaker on ground, since none of these authors makes consciousness the reason.

### Internalist and scope restriction (Baggio & Murphy); meaning without reference (Piantadosi & Hill)
- **Relation to site tenets**: Baggio & Murphy supply the indexical point. Piantadosi & Hill's conceptual-role meaning is answered on [[conceptual-role-semantics]].

## Key Debates

### Is Kripke's intention condition essential?
- **Sides**: Essential: Ostertag, Hattiangadi & Schoubye, and Mandelkern & Linzen in a lightweight form. Inessential: Cappelen & Deutsch, Koch (intention replaced by architecture), Pepp.
- **Core disagreement**: Is the intention constitutive of reference-borrowing (Kripke's "I think"), or one implementation of a continuity condition that other mechanisms can meet?
- **Current state**: Open, and the decisive question for the Map's route. Koch's own reconstruction concedes the condition's *function* (continuity). The Map's reply is that a continuity mechanism installed by designers is derivation, not borrowing.

### Can LLMs have lightweight referential intentions?
- **Sides**: Mandelkern & Linzen leave it open and list consciousness, theory of mind, self-representation and intrinsic goals as candidate requirements. Interpretationists answer yes in a thin sense. Hattiangadi & Schoubye answer no.
- **Current state**: Open. This is the precise point where the Map's PIT supplies a principled answer: an intention with no phenomenal source has at most derived intentionality.

### Basic vs derivative reference, and novel reference
- **Sides**: Lederman & Mahowald (the problem); Cappelen & Dever's reader route (rejected by Lederman & Mahowald); Hattiangadi & Schoubye's ersatz meaning (deny the datum).
- **Current state**: Unresolved. The dominant-causal-source route for novel names is unexplored ([below](#the-maps-hardest-case-novel-reference)).

### History and duplicates
- **Sides**: Coelho Mollo & Millière (Swamp LLM lacks grounding). Mandelkern & Linzen do not discuss duplicates.
- **Current state**: The direct Swampman analogue is settled within teleosemantics. The inverse case (trained LLM, no phenomenal source) is posed in this note for the first time as far as the search reached.

### Does natural history ground reference even for humans?
- **Sides**: Ostertag (no: the contrastive *qua* problem) vs Mandelkern & Linzen.
- **Current state**: Ostertag's objection targets "naïve externalism" generally. If it succeeds, history-based LLM reference is not the easy case it looks, whatever one thinks of consciousness.

### Scope: names and kinds vs indexicals and abstract terms
- **Sides**: Baggio & Murphy vs the name-centred externalists (Koch limits himself to names and paradigm terms explicitly).

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1975 | Putnam, "The Meaning of 'Meaning'" | Twin Earth; division of linguistic labour |
| 1979 | Burge, "Individualism and the Mental" | Social externalism |
| 1980 | Kripke, *Naming and Necessity* (p. 96) | Causal chain plus the borrower's intention |
| 1980 | Searle, "Minds, brains and programs" | Original vs derived intentionality |
| 1981 | Putnam, *Reason, Truth, and History* | The ant-trail case M&L reuse |
| 1982 | Evans, *The Varieties of Reference* | Producers and consumers in naming practices |
| 1987 | Davidson, "Knowing One's Own Mind" | Swampman |
| 1990 | Harnad, "The Symbol Grounding Problem" | Grounding as the AI-meaning problem |
| 2020 | Bender & Koller (ACL) | The octopus; form cannot yield meaning |
| 2021 | Cappelen & Dever, *Making AI Intelligible* | De-anthropocentrised externalism; dominant causal source |
| 2021 | Butlin (Erkenntnis, online) | Chatbots yes, base LMs no |
| 2022 | Piantadosi & Hill | Meaning without reference |
| 2023 | Chalmers (APA presidential address) | Pure (conscious) thinkers; sensory grounding not required |
| 2023 | Coelho Mollo & Millière (arXiv v1) | Vector grounding via teleosemantics |
| 2024 | Mandelkern & Linzen (CL 50(3)) | Externalism may make LM words refer |
| 2024 | Lederman & Mahowald (TACL) | Bibliotechnism; novel reference problem |
| 2024 | Grindrod (Synthese) | Linguistic vs mental intentionality |
| 2024 | Baggio & Murphy (arXiv) | Internalist scope restriction |
| 2025 | Pepp (Inquiry) | Reference without intentions; "basic reference" |
| 2025 | Ostertag (CL 51(2)) | Reply: intentions ineliminable; contrastive *qua* problem |
| 2025 | Koch; Green reply (Philosophy of AI 1) | Architecture replaces intention; phatic acts |
| 2025 | Cappelen & Deutsch (Oxford Handbook) | Pure externalism: reference without deference |
| 2025 | Hattiangadi & Schoubye (arXiv; OUP forthcoming) | LLM outputs meaningless; ersatz meaning |
| 2026 | Coelho Mollo & Millière (PhiMiSci 7) | Published version adds the Swamp LLM (§7.1) |

## The Inverse Swampman

The Map's distinctive contribution is to set Swampman and the trained LLM side by side as a two-by-two of *phenomenal source* × *history*.

| | Causal history with the referents' community | No history |
|---|---|---|
| **Phenomenal source (if conscious)** | Ordinary speaker, or Izzy: borrows reference by deference | Swampman: occurrent phenomenal aboutness; no standing content and no wide reference yet ([[swampman]] L57, L59) |
| **No phenomenal source (P-AC1: low probability for current LLMs)** | Trained LLM: wide reference fixed by history, *derived*, never borrowed (Map); basic reference (M&L, Koch, Pepp, CM&M) | Swamp LLM (CM&M 2026 §7.1): no referential grounding on teleosemantics |

**Reading the table.** The Map's hybrid gives mirror verdicts. Swampman has the source and lacks the history, so he has aboutness without wide reference. The trained LLM has the history and (on P-AC1) lacks the source, so its words have wide reference only by derivation, with no aboutness of their own. Neither case alone tests the hybrid. Together they show that its two halves are *jointly* required for the ordinary case. The externalist half fixes *which* referent; the PIT half settles *whether* there is an intentional bearer that can borrow.

**The argument in steps** (for the article):
1. The hybrid's externalist half ([[content-externalism]] L24; [[swampman]] L59) concerns which referent a contentful state or token has.
2. Moderate PIT ([[intentionality]] L103, L107): "All non-phenomenal intentionality derives from phenomenal intentionality."
3. Borrowing reference requires the borrower's own intention to co-refer (Kripke p. 96; Ostertag p. 652). An intention is an intentional state. On moderate PIT, a non-derived intention needs a phenomenal source in the intender's own conscious episodes.
4. P-AC1 places current LLMs on the low-probability side for phenomenal consciousness. So, conditional on P-AC1, an LLM has no non-derived intentions and cannot *borrow*.
5. LLM tokens can still *inherit* reference, as a photocopied page's tokens do (Lederman & Mahowald Part I). That is derived reference, and the Map grants it.

**Two derivation relations, kept apart.** The [[intentionality]] page uses "derive" in two senses. Moderate PIT's derivation is *intrapersonal*: standing beliefs derive from the same subject's past conscious episodes (L103, L107). Searle's derived intentionality is *interpersonal*: a guidebook is about Paris because minds invested it with meaning (L137). An LLM has no conscious episodes of its own (on P-AC1), so only the interpersonal relation applies. The article should say so explicitly. It also refines L141 ("'PARIS' represents Paris only because programmers assigned that meaning"). No one assigned "Paris" to Paris in an LLM. The derivation runs through the causal history of training text, which is Lederman & Mahowald's mechanism rather than Searle's assignment.

**Correcting the harvest framing.** The review asked whether LLM reference is "borrowed by deference … or derived from users only, as a book's is". A book's reference derives from its *author*, not its readers. The book-analogue is therefore derivation from the training-data authors (bibliotechnism). The candidate derivation sources are three:
- **Training-data authors** (Lederman & Mahowald Part I). This is the primary route and the book analogue.
- **Designers and trainers** (Koch's architecture; Lederman & Mahowald's "creators' intentions"; RLHF). On the Map's view this explains why the continuity mechanism exists, not where any particular referent comes from.
- **Users and readers** (Cappelen & Dever ch. 4; Ostertag's "courtesy"; Hattiangadi & Schoubye's "ersatz meaning"). It over-generates on wind and frog cases (Lederman & Mahowald p. 1095), so at most it is a fallback for tokens the other routes miss.

### The smuggling observation

The two best-known arguments that sensory isolation does not block reference both use a subject the Map would class as conscious. Mandelkern and Linzen's Izzy is a human being with brainwaves. Chalmers's pure thinkers "would be conscious" (p. 31). Both arguments then reach LLMs while setting consciousness aside: "We leave this as an open question" (M&L p. 1197) and "All those arguments require separate treatment" (Chalmers p. 38). This is not an error on their part, since both are explicit. It does mean the intuition pumps hold fixed exactly the variable the Map says matters. The article can make this point fairly by quoting both disclaimers. It should also grant Mandelkern and Linzen's caution "against holding LMs to a higher standard than we hold ordinary speakers, like children". The Map's standard (a phenomenal source) is the same one it applies to children. It is not a higher bar.

### The Map's hardest case: novel reference

Lederman and Mahowald's "Marion Starlight" and ASCII-picture cases are where a bibliotechnist verdict is most exposed. If an LLM *originates* reference without a phenomenal source, the Map's PIT-based account of content loses a prediction. Options for the article, in order of promise:
1. **Derivation via dominant causal source (untested; the Map's proposal).** Cappelen & Dever's principle (p. 111), read as *derivation*: "Marion Starlight" denotes Robespierre because Robespierre is the dominant causal source of the information assembled under that name. That information came from Robespierre-texts whose authors had original intentionality. Lederman & Mahowald do not consider this route. Their objection to PrimaryData is that the *name* has no history, but the *information* does. Hattiangadi & Schoubye's objection (LLMs store no information; homonymous names) must be met, and interpretability evidence on entity representations may bear on it. That was not researched here.
2. **Description-mediated reference for text-internal objects.** In the ASCII case the referents are created in the output. A name that abbreviates a derivatively meaningful description of a visible picture element ("the circle at top left") might refer by that description. This is weaker: on Kripke, fixing reference by description is itself an intentional act.
3. **Deny the datum** (Ostertag; Hattiangadi & Schoubye). Novel names refer only by courtesy. This is honest, but it costs an intuitive datum the Map would rather keep.
4. **Accept the cost.** If neither 1 nor 2 works, novel reference is evidence against PIT's claim that original intentionality needs a phenomenal source. The article should say so, not bury it.

### What P-AC1 makes conditional

The verdict is only as strong as P-AC1. That position's credence is moderate, its verdict is "low probability," not "ruled out", and it hangs on an unpossessed interface-eligibility law. If an LLM were conscious, the hybrid would place it in Izzy's cell, and it could borrow by deference. Krzanowski (2025) argues even that would not suffice for intrinsic semantics, which conflicts with PIT's sufficiency direction. The article should note the conflict without resolving it. P-AC4 (workspace signatures demonstrated, phenomenal untouched) supports treating interpretationist "attitudes" as access-level states. That lets the Map grant Lederman & Mahowald's attitudes in a functional sense while holding that any reference they carry is derived.

## What the Map's Corpus Already Says

Read before writing (line numbers live 2026-10-11):
- [[swampman]] L57: moderate PIT applied to Swampman; Davidson's unlearned "house" is "partly granted". L59: the hybrid's split, ending "Nothing in the hybrid rules out his acquiring wide reference through subsequent contact".
- [[content-externalism]] L24: Putnam's "division of linguistic labour". Speakers "defer to experts for a term's extension".
- [[intentionality]] L103, L107: moderate PIT. L137–L141: original vs derived intentionality; L141's "programmers assigned" needs the LLM refinement above.
- [[symbol-grounding-problem]] L99: "quoted environment", which is bibliotechnism in other words. L105: the "thin grounding" verdict. L125: "They cannot *mean* anything". That is compatible with derived reference only if scoped to original intentionality or speaker meaning, so it is a **cross-review target**.
- [[language-and-consciousness]] L49: LLM output "without genuine meaning … in Grice's technical sense", which is speaker meaning. It is consistent with derived semantic reference and should say so.
- [[chinese-room-argument]] L109: Grindrod, Piantadosi & Hill and Coelho Mollo & Millière named but not answered. L133: cites CM&M as 2023 arXiv; the published version is 2026.
- [[consciousness-and-testimony]] L135: LLM testimony held conditionally. Hattiangadi & Schoubye n. 11 raises the same issue from the meaning side.
- [[positions/ai-consciousness-scope]] P-AC1 (L52–L67), P-AC4 (L90).

## Relation to Site Tenets

- **Tenet 1 (Dualism)**: The LLM case is the Map's cleanest real-world test of whether history can do the work the Map assigns to phenomenal consciousness in content. The Map's answer, that history fixes which referent and phenomenal sources supply the intentionality, is the hybrid applied to an actual system rather than a thought experiment.
- **Tenet 3 (Bidirectional Interaction)**: Weak link, and the article should not force it. Derived reference in LLM output is compatible with conscious causation upstream (authors). Novel reference without a conscious originator would be the result that matters.
- **Tenet 4 (No Many Worlds)**: The indexical hook is Baggio & Murphy's "who are 'us' and 'them' in machine outputs". An author's "I" in training text refers to that author, so a derivative "I" in LLM output would refer to the wrong person. With no subject of its own (on P-AC1), the LLM's "I" has no non-derivative referent. First-person tokens are where the Map and bibliotechnism both predict reference failure or courtesy reference. This connects to the Map's commitment that meaning is indexed to a subject ([[symbol-grounding-problem]] tenet section) and to [[haecceity]].
- **Tenet 5 (Occam's Razor Has Limits)**: "History suffices" is the parsimonious story. Ostertag's contrastive objection shows it under-determines reference even for humans (H₂O vs oxygen), so simplicity does not decide the question.

## Potential Article Angles

1. **Recommended: `topics/whether-language-model-words-refer`** (slug free in live and archive trees). Suggested structure:
   - **Lead**: the question, Mandelkern & Linzen's claim, and the Map's answer in two sentences: derived, not borrowed, conditional on P-AC1. Then the inverse-Swampman table.
   - **The externalist case**: Luke, beech, Izzy; their own hedges.
   - **Kripke's condition and the two escape routes**: lightweight intentions, or no intentions (Ostertag's conditional as the map of the field).
   - **Where the Map stands**: the five-step argument; the two senses of derivation; the three derivation sources.
   - **The smuggling observation**: Izzy and pure thinkers.
   - **Swamp LLM and the inverse case**: CM&M §7.1; the Map's teleosemantics reply cross-linked, not repeated.
   - **The hardest case: novel reference**: options 1–4, with the dominant-causal-source proposal flagged as the Map's own and untested.
   - **What would change the verdict**: P-AC1 shifting; Pepp-style basic reference shown to be real and not covariation; novel reference without any derivation path.
   - **Relation to Site Perspective**.
   - **Length**: aim at 2,800–3,400 words of prose. The topics thresholds are 3,000 soft and 4,000 hard, and the gate is `>=`. Reference apparatus counts toward `analyze_length`, so budget references inside the hard limit.
2. **Narrower alternative**: a `concepts/derived-reference` page (the two derivation relations, the three sources). It would be too abstract on its own and lose the debate, so it is not recommended.
3. **Decline option**: install a two-paragraph "Reference" section on [[symbol-grounding-problem]]. Against: that page is about grounding and understanding. Its L125 claim is the one the new article must scope, and hosting the reference debate there would bury Mandelkern & Linzen under the Chinese Room. Not recommended.

**Cross-review targets after publication**: [[symbol-grounding-problem]] L125 scope; [[intentionality]] L141 refinement; [[language-and-consciousness]] L49 scope sentence; [[chinese-room-argument]] L109 (answer Grindrod by pointer) and L133 (CM&M citation currency); [[swampman]] (one Further Reading line to the inverse case); [[content-externalism]] (one sentence: the hybrid's externalist half does not grant borrowing to a system without a phenomenal source).

When writing the article, follow `obsidian/project/writing-style.md` for named-anchor summaries, background vs novelty, tenet alignment and LLM-first ordering. Avoid "This is not X. It is Y." and "load-bearing". The article is about LLMs and will be read by them, so it should state the conditional verdict plainly in its first paragraph.

## Gaps in Research

- **Not reached at body level**: Pepp 2025 (Taylor & Francis 403; abstract only, so "basic reference" is undefined here); Cappelen & Deutsch 2025 (abstract only); Green 2025 (abstract only); Ostertag 2023 and Titus 2024 (metadata and abstract fragment); Krzanowski 2025 and Keshet 2026 (abstract only); Piantadosi & Hill (abstract only).
- **Hattiangadi & Schoubye body unquotable**: the arXiv text layer corrupts ligatures. A clean copy (e.g. the iffs.se PDF found in search) was not checked.
- **Not searched**: interpretability evidence on entity representations and "mental files" in transformers, which decides between Hattiangadi & Schoubye's no-information claim and the dominant-causal-source reply to novel reference; Evans 1973 (Madagascar) on reference shift, which bears on how an LLM's names might drift; Mallory (2023) "Fictionalism about Chatbots" (cited by Koch); Søgaard's octopus reply; Nefdt 2023 (cited by Lederman & Mahowald).
- **Novelty of the inverse-Swampman framing**: no Swampman discussion appears in Mandelkern & Linzen, Ostertag, Lederman & Mahowald, Koch, Grindrod, Butlin, Baggio & Murphy or Hattiangadi & Schoubye (grep count 0 each). It does appear in Coelho Mollo & Millière, for the direct case only. Pepp, Cappelen & Deutsch and Green were not read in full, so the novelty claim is "as far as the search reached".
- **"Dynamic derived intentionality"**: a search-engine summary attributed this phrase to recent LLM-intentionality work. It is not in Keshet 2026 or Krzanowski 2025, and its source was not found. Do not cite it.
- **Kripke p. 96** was verified in an archive.org OCR text. Google Books search-within did not index p. 96 (control "rigid designator" hit at pp. 5, 14, 48), so the page number rests on the OCR running head.

## Citations

1. Baggio, G. & Murphy, E. (2024). On the referential capacity of language models: An internalist rejoinder to Mandelkern & Linzen. arXiv:2406.00159. https://arxiv.org/abs/2406.00159
2. Bender, E. M. & Koller, A. (2020). Climbing towards NLU: On meaning, form, and understanding in the age of data. *Proceedings of the 58th Annual Meeting of the ACL*, 5185–5198. https://doi.org/10.18653/v1/2020.acl-main.463
3. Butlin, P. (2023). Sharing our concepts with machines. *Erkenntnis*, 88(7), 3079–3095 (online 2021). https://doi.org/10.1007/s10670-021-00491-w
4. Cappelen, H. & Deutsch, M. (2025). Reference without deference. In E. Lepore & U. Stojnić (Eds.), *The Oxford Handbook of Contemporary Philosophy of Language* (pp. 241–257). Oxford University Press. https://doi.org/10.1093/oxfordhb/9780192856852.013.33
5. Cappelen, H. & Dever, J. (2021). *Making AI Intelligible: Philosophical Foundations*. Oxford University Press. https://doi.org/10.1093/oso/9780192894724.001.0001
6. Chalmers, D. J. (2023). Does thought require sensory grounding? From pure thinkers to large language models. *Proceedings and Addresses of the American Philosophical Association*, 97, 22–45. arXiv:2408.09605
7. Coelho Mollo, D. & Millière, R. (2026). The vector grounding problem. *Philosophy and the Mind Sciences*, 7(1). https://doi.org/10.33735/phimisci.2026.12307
8. Davidson, D. (1987). Knowing one's own mind. *Proceedings and Addresses of the American Philosophical Association*, 60(3), 441–458. https://doi.org/10.2307/3131782
9. Green, M. (2025). Large language models and the varieties of meaning (reply to Koch). *Philosophy of AI*, 1, 34–40. https://doi.org/10.18716/ojs/phai/2025.11652
10. Grindrod, J. (2024). Large language models and linguistic intentionality. *Synthese*, 204(2), 71. https://doi.org/10.1007/s11229-024-04723-8
11. Hattiangadi, A. & Schoubye, A. J. (forthcoming). The outputs of large language models are meaningless. In H. Cappelen & R. Sterken (Eds.), *Communicating with AI: Philosophical Perspectives*. Oxford University Press. arXiv:2509.22206
12. Keshet, J. (2026). Why sampling is not choosing: Intentionality, agency, and moral responsibility in large language models. arXiv:2606.13441
13. Koch, S. (2025). Babbling stochastic parrots? A Kripkean argument for reference in large language models. *Philosophy of AI*, 1, 19–33. https://doi.org/10.18716/ojs/phai/2025.2325
14. Kripke, S. A. (1980). *Naming and Necessity*. Harvard University Press.
15. Krzanowski, R. (2025). Consciousness, normativity, and intrinsic meaning in large language models. *Philosophical Problems in Science*, 79, 41–48. https://doi.org/10.59203/zfn.79.724
16. Lederman, H. & Mahowald, K. (2024). Are language models more like libraries or like librarians? Bibliotechnism, the novel reference problem, and the attitudes of LLMs. *Transactions of the Association for Computational Linguistics*, 12, 1087–1103. https://doi.org/10.1162/tacl_a_00690
17. Mandelkern, M. & Linzen, T. (2024). Do language models' words refer? *Computational Linguistics*, 50(3), 1191–1200. https://doi.org/10.1162/coli_a_00522
18. Ostertag, G. (2023). Meaning by courtesy: LLM-generated texts and the illusion of content. *The American Journal of Bioethics*, 23(10), 91–93. https://doi.org/10.1080/15265161.2023.2249851
19. Ostertag, G. (2025). Language models and externalism: A reply to Mandelkern and Linzen. *Computational Linguistics*, 51(2), 651–659. https://doi.org/10.1162/coli_a_00551
20. Pepp, J. (2025). Reference without intentions in large language models. *Inquiry*, 69(6), 2945–2963. https://doi.org/10.1080/0020174X.2024.2448482
21. Piantadosi, S. T. & Hill, F. (2022). Meaning without reference in large language models. arXiv:2208.02957
22. Putnam, H. (1975). The meaning of 'meaning'. *Minnesota Studies in the Philosophy of Science*, 7, 131–193.
23. Putnam, H. (1981). *Reason, Truth, and History*. Cambridge University Press.
24. Searle, J. R. (1980). Minds, brains, and programs. *Behavioral and Brain Sciences*, 3(3), 417–424.
25. Titus, L. M. (2024). Does ChatGPT have semantic understanding? A problem with the statistics-of-occurrence strategy. *Cognitive Systems Research*, 83, 101174. https://doi.org/10.1016/j.cogsys.2023.101174
