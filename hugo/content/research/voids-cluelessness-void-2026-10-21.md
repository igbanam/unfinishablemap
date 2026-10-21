---
ai_contribution: 100
ai_generated_date: 2026-10-21
ai_modified: 2026-10-21 05:53:00+00:00
ai_system: claude-opus-5-5
author: null
concepts:
- '[[simulation]]'
- '[[moral-census-opacity]]'
- '[[bidirectional-interaction]]'
- '[[counterfactual-reasoning]]'
- '[[possibility-probability-slippage]]'
created: 2026-10-21
date: &id001 2026-10-21
description: 'Research notes on the cluelessness void: an agent knows its act under
  the few descriptions it foresees, while the act''s causal reach runs far past foresight
  and does not reliably fade or cancel.'
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-21 05:53:00+00:00
modified: *id001
recommended_action: article
related_articles:
- '[[voids]]'
- '[[tenets]]'
- '[[amplification-void]]'
- '[[counterfactual-void]]'
- '[[normative-void]]'
- '[[nomic-void]]'
- '[[decision-void]]'
- '[[voids-as-evidence]]'
target_section: voids
target_slug: cluelessness-void
title: 'Research Notes - Voids: The Cluelessness Void'
topics:
- '[[free-will]]'
- '[[moral-implications-of-genuine-agency]]'
- '[[ethics-under-dualism]]'
---

# Research: Voids - The Cluelessness Void

**Date**: 2026-10-21
**Search queries used**: "Greaves 2016 'Cluelessness' Proceedings of the Aristotelian Society pdf"; "Lenman 2000 'Consequentialism and Cluelessness' Philosophy & Public Affairs pdf"; "Mogensen 'Maximal cluelessness' Philosophical Quarterly"; "Palmer Döring Seregin 2014 'The real butterfly effect' Nonlinearity"; "Tetlock long-range forecasts 'slow-motion variables'"; "Schwitzgebel 'washout argument' longtermism"; "Davidson 'Agency' 'accordion effect' Feinberg"; "Project Gutenberg Moore 'Principia Ethica'". Plus Crossref, OpenAlex, Semantic Scholar and Europe PMC lookups, and full texts fetched with curl and grepped locally.
**Voids category**: Mixed. The core is **Unexplorable**: most of what any act causes lies beyond foresight. Two mechanisms drive this. Identity-affecting ramification changes which people later exist. Multi-scale physical systems appear to have an intrinsic predictability limit that better data cannot remove (contested; see below). There is a real **Occluded** face: ordinary agents do not feel the gap, because the act as experienced is bounded by its foreseen descriptions, and the two classic philosophical reassurances (remote effects fade; remote effects cancel) are themselves the defaults that hide it. A thin **Unexplored** face concerns how much pattern-level and policy-level foresight can recover.

**Source tags**: **[raw]** = quotation grep-verified in fetched raw text (full text or abstract); **[Crossref]** = record verified, content not read; **[secondary]** = reported by a verified source, primary not read; **LEAD** = unconfirmed, not to be quoted.

## Executive Summary

Every act has consequences far beyond what its agent can foresee. Lenman (2000) turned this into a problem for any outcome-guided agent. The foreseeable consequences of an action are "so often a drop in the ocean of its actual consequences" [raw], chiefly because so many acts are *identity-affecting*: they change which people are later conceived, and the difference compounds down the generations. Greaves (2016) narrowed the problem. Where the agent's evidence about the unforeseeable effects is symmetric (*simple* cluelessness), restricted indifference reasoning neutralises it. Where there are reasons pointing both ways that cannot be weighed (*complex* cluelessness), "indifference-based reasoning is inapplicable by anyone's lights" [raw]. She reports a characteristic "decision discomfort" there [raw].

Two classic reassurances fail on analysis. Remote effects do not reliably fade like ripples on a pond (Moore 1903; Smart 1973), and they do not cancel: by random-walk theory the summed effect of many independent steps "tends to grow with n" [raw]. Physics may add an intrinsic limit. For midlatitude weather it "may indeed exist and is intrinsic to the underlying dynamical system and instabilities even if the forecast model and the initial conditions are nearly perfect" [raw]. The forecasting record shows predictability declining with horizon at a rate that varies by topic (Tetlock et al. 2023).

The void is the mismatch between the **act as known** and the **act as cause**. The agent knows its act under a handful of descriptions: what it intends and what it foresees. The act as cause can be redescribed by any of its consequences, and most of those descriptions are unavailable to anyone. The void holds for any agent on any metaphysics. Greaves runs her argument under determinism. So the void is **framework-independent and supplies no evidence for any tenet**. What it does give the Map is a constraint: Tenet 2's "minimal" has to stay a claim about the size of the interface, never about the size of an act's consequences. **Recommendation: article at `voids/cluelessness-void`.**

## Dedupe Record (why this void is new)

Searched `obsidian/voids/`, `obsidian/research/voids-*`, `archive/` (all sections), and live `topics/`, `concepts/`, `apex/`, `positions/`, `research/`, with `grep -rliF` (case-insensitive, fixed-string).

- **Positive control**: "aphantasia". 11 voids articles, 7 voids notes, 2 archive files, 46 live/research files. The method finds what is there.
- **Zero hits in voids, voids research and archive**: "cluelessness", "Lenman", "Mogensen", "Greaves", "butterfly effect", "Burch-Brown", "complex cluelessness", "imprecise credence", "Lorenz", "longtermis", "foreseeable consequences", "washing out", "accordion". "Sensitive dependence" has zero hits in voids.
- **The only corpus occurrences of "clueless\*"**: a Sebo (2018) quotation at `concepts/moral-census-opacity.md` L98 ("more cluelessness and demandingness than we might have thought") and that article's 2026-08-16 deep review. This is a natural integration point, not coverage.
- **False-friend hits, checked and unrelated**. "Lenman" (4 live/research): a citation of his *Utilitas* review of Kennett in `research/self-control-as-skill-and-scaffolding-2026-10-04`. "Mogensen" (9): his welfare and fading-qualia papers, not "Maximal Cluelessness". "Greaves" (2 live): her Everett-probability papers in `haecceity` and `quantum-immortality…`.
- **Prior rejection lists**: the 10-14, 10-15 and 10-16 voids notes rejected self-deception, mind-blanking, hindsight/curse-of-knowledge, imaginative resistance, microgenesis, irreversibility-of-understanding, innocent-eye, meta-perception, folk-physics suppression and speaking-thinking. None overlaps. The 10-20 drift note (parked on the voids-slot NEEDS-HUMAN) is a different void.
- **Slug**: `uv run python scripts/check_slug.py cluelessness-void voids` returned "OK: Slug 'cluelessness-void' is available in voids/" on 2026-10-21. No file matching `*clueless*` exists in `obsidian/`, `archive/` or `hugo/content/`. "cluelessness" is absent from `netlify.toml` and `hugo/static/_redirects`. `consequence-void` was avoided because a reader would take it for van Inwagen's argument ([the-consequence-argument-for-incompatibilism](/topics/the-consequence-argument-for-incompatibilism/)).

**Boundaries with the nearest neighbours:**

- [amplification-void](/voids/amplification-void/) is the **inward** chain: quantum event to neural pattern, with chaos *inside the brain*. Cluelessness is the **outward** chain: from the act into the world and down the generations. Same family of dynamics, opposite direction, a timescale of centuries rather than milliseconds.
- [counterfactual-void](/voids/counterfactual-void/) concerns modal imagination pulled toward actuality's neighbourhood: what *could have been*. Cluelessness concerns the forward causal reach of an actual choice. They meet at one point: complex cluelessness is a comparison of two unforeseeable futures, A1's against A2's.
- The predictive void ([research note](/research/voids-predictive-void-2026-02-17/)) is about one's *own future phenomenal states*. The self-prediction void ([research note](/research/voids-self-prediction-void-2026-10-14/)) is about one's *own forthcoming decisions*. Cluelessness is about the *world's* response to those decisions.
- The epistemic-horizon void ([research note](/research/voids-epistemic-horizon-void-2026-03-06/)) concerns the extent of ignorance in general. Cluelessness is a specific, structured ignorance with its own formal literature and a decision-theoretic face.
- [normative-void](/voids/normative-void/) says moral truths themselves may be out of reach. Cluelessness holds **even with the moral truth fixed**: grant that total welfare is what matters, and which act serves it is still hidden.
- [moral-census-opacity](/concepts/moral-census-opacity/) says we cannot count moral patients *now*. Cluelessness says we cannot trace effects *forward*. Sebo's quotation already links the two.
- [nomic-void](/voids/nomic-void/) covers limits physics places on cognition. The predictability barrier is a nomic instance, and a natural cross-link.
- [decision-void](/voids/decision-void/) is the hidden moment of choice, a different site.

## Key Sources

### Lenman (2000), "Consequentialism and Cluelessness", *Philosophy & Public Affairs* 29(4): 342–370. Full text read (JSTOR scan; page map from per-page footers)
- **The Richard and Angie case, pp. 344–345, explicitly hypothetical ("let us suppose").** A bandit around 100 BCE spares a pregnant woman who is a remote ancestor of Hitler: "The millions of Hitler's victims were thus also victims of Richard's sparing of Angie." [raw]
- **Identity-affecting actions, p. 346.** "These are actions that make a difference to the identities of future persons and these differences are apt to amplify exponentially down the generations." [raw]
- **The core claim, p. 350.** "the foreseeable consequences of an action are so often a drop in the ocean of its actual consequences" [raw]. And: "We may not be strictly without a clue, but we are virtually without a clue." [raw]
- **The Moore/Smart response (p. 350).** Lenman quotes both reassurances in order to reject them. ⚠️ His transcription of Moore departs from the primary; see Moore below.
- **Tenet alignment**: none direct. The argument is framework-neutral and addressed to consequentialists.

### Greaves (2016), "Cluelessness", *Proceedings of the Aristotelian Society* 116(3): 311–339, doi:10.1093/arisoc/aow018. Full text read (page numbers printed in the text)
- **Abstract, p. 311.** "For any given action, however, the majority of its consequences are unpredictable at the time of decision." [raw] The complex sources are where "indifference-based reasoning is inapplicable by anyone's lights" [raw]. The paper aims to examine "the precise source of the associated phenomenology of discomfort in forced-choice situations" [raw].
- **Runs under determinism, p. 311.** "Assume determinism." [raw] A footnote says relaxing the assumption would complicate parts of the discussion "but not in ways that are ultimately relevant" [raw]. This is the basis for the framework-independence claim below.
- **Against the ripples postulate, p. 314.** The 'ripples on a pond' postulate "is not plausible" [raw], because even trivial actions are "very likely to have unforeseen identity-affecting effects" [raw]. She cites Parfit (1984, ch. 16) for less obviously identity-directed actions [secondary].
- **Against cancellation, p. 315.** "Unfortunately, the cancellation postulate is false." [raw] By random-walk theory, "the combined effect of a large number n of probabilistically independent steps tends to grow with n" [raw].
- **The structure of complex cluelessness, p. 323.** (cc1) there are some reasons to think A1's unforeseeable consequences systematically better than A2's; (cc2) some reasons to think the reverse; (cc3) it is unclear how to weigh them [raw, paraphrased]. Footnote 17: "cases with the structure given in (cc1)–(cc3) are ubiquitous" [raw].
- **Phenomenology, p. 326.** "There is a deep sense of 'decision discomfort' attending the predicament of being forced to make decisions in situations of the character we are now discussing." [raw]
- **The everyday counter-phenomenology, p. 335.** "Most of us simply learn to live with the need to resolve decisions with some arbitrariness and with incomplete guidance from data and theory" [raw]. Greaves leaves open whether (cc1)–(cc3) "strike to the root of the phenomenology of cluelessness" [raw].
- **Positive proposal (§VI)**: model the agent as having imprecise credences, and explore permissibility criteria for that case [raw, summarised].

### Mogensen (2021), "Maximal Cluelessness", *The Philosophical Quarterly* 71(1): 141–162, doi:10.1093/pq/pqaa021 (online 4 May 2020). Abstract read [Crossref; abstract raw via OpenAlex]
- The problem "arises from recognition of the overwhelming importance and inscrutability of the indirect effects of our actions (so-called cluelessness)" [raw], combined with a permissive decision rule for deep uncertainty, the maximality rule. He concludes that "we lack a compelling decision theory that is consistent with a longtermist perspective and does not downplay the depth of our uncertainty" [raw].
- Body not read. The GPI working-paper host is offline and PhilArchive is behind a JavaScript challenge.

### Burch-Brown (2014), "Clues for Consequentialists", *Utilitas* 26(1): 105–119, doi:10.1017/s0953820813000289. Full text read
- **Abstract, p. 105.** "for reasons to do with statistical theory, the cluelessness objection is too pessimistic" [raw].
- **The urn, p. 113.** "The climate can be understood as the statistical properties of the weather – it is the 'urn' from which are drawn specific weather events." [raw] The method relies on the Central Limit Theorem and the Law of Large Numbers. Patterns of action can be predicted where single acts cannot.
- **Role**: the strongest "the void is smaller than it looks" source. It belongs in the body of any article, not in a footnote.

### Cowen (2006), "The Epistemic Problem Does Not Refute Consequentialism", *Utilitas* 18(4): 383–399, doi:10.1017/S0953820806002172. Full text read
- "Some short-run benefits are sufficiently high that we should pursue them, even if our long-run estimates possess a very high variance." [raw] And: "Even a slight idea about some major consequences will render the epistemic argument less plausible." [raw]
- He grants the ramification premise with his own example: "If Hitler's great-great-grandfather had bent down to pick one more daisy, many of the effects might have washed out; nonetheless Europe today would be a very different place." [raw]

### Schwitzgebel (2026), "The Washout Argument against Longtermism", *Utilitas*, pp. 1–14, doi:10.1017/s095382082610034x (online 16 June 2026) [Crossref]. Abstract read on the author's page (version of 31 July 2025, labelled "forthcoming")
- "We cannot be justified in believing that any actions currently available to us will have a non-negligible positive influence a billion or more years in the future." [raw] He gives three arguments: Infinite Washout, Cluelessness, Negligibility [raw].
- The printed abstract was not compared with the author's version. Quote from the author's page only, or re-verify against the published text.

### Tarsney (2023), "The epistemic challenge to longtermism", *Synthese* 201(6), art. 195, doi:10.1007/s11229-023-04153-y [Crossref]. Content LEAD
- Not read: Springer's cookie wall and PhilPapers' JavaScript challenge both blocked the fetch. From memory, he models how long-run effects persist against events that nullify them, and argues that some long-term interventions keep a large expected value. **Do not quote or summarise in the article without reading it.**

### Moore (1903), *Principia Ethica*, §93. Primary read (Project Gutenberg #53430)
- "The effects of any individual action seem, after a sufficient space of time, to be found only in trifling modifications spread over a very wide area" [raw]. And: "It does in fact appear to be the case that, in most cases, whatever action we now adopt, 'it will be all the same a hundred years hence,'" [raw]. He adds that this "might, perhaps, be _shewn_ to be true" [raw]. Moore offers it as a needed assumption, not a demonstrated result, and Greaves's fn. 4 reads him the same way.
- ⚠️ **Transcription divergence.** Lenman (2000, p. 350) prints "'it will all be the same a hundred years hence'". The primary reads "it will **be all** the same". Quote Moore from the primary, never through Lenman.

### Smart (1973, p. 33), in Smart & Williams, *Utilitarianism: For and Against*. Primary not read [secondary ×2, wordings disagree]
- Lenman: "approximate rapidly to zero like the furthermost ripples on a pond after a stone has been dropped on it". Greaves: "rapidly approximate to zero like the furthermost ripples on a pond after a stone has been dropped into it". The two transcriptions differ in word order and in the last preposition. **Do not quote Smart.** Paraphrase the ripples-on-a-pond image and attribute the label to Greaves.

### Zhang, Sun, Magnusson, Buizza, Lin, Chen & Emanuel (2019), "What Is the Predictability Limit of Midlatitude Weather?", *Journal of the Atmospheric Sciences* 76(4): 1077–1091, doi:10.1175/jas-d-18-0269.1. Abstract read [Crossref; abstract raw via OpenAlex]
- "Results suggest that the predictability limit for midlatitude weather may indeed exist and is intrinsic to the underlying dynamical system and instabilities even if the forecast model and the initial conditions are nearly perfect." [raw] The practical limit is about 10 days. Cutting initial-condition uncertainty "by an order of magnitude extends the deterministic forecast lead times of day-to-day weather by up to 5 days" [raw].
- **Contested.** Žagar & Szunyogh (2020), comment, *J. Atmos. Sci.* 77(2): 781–785, with reply by Sun et al. (2020), 77(2): 787–793 [Crossref; neither read].

### Palmer, Döring & Seregin (2014), "The real butterfly effect", *Nonlinearity* 27(9): R123–R141, doi:10.1088/0951-7715/27/9/R123. Abstract read [Crossref; abstract raw via OpenAlex]
- Lorenz meant by the butterfly effect "an absolute finite-time predicability barrier in certain multi-scale fluid systems" [raw; "predicability" is the abstract's own spelling, sic]. But "it is still an open question whether the Navier–Stokes equation has this property" [raw]. The effect "is an intermittent phenomenon in the atmosphere", and its presence "can be signalled a priori" by ensemble methods [raw].
- Lorenz (1969), "The predictability of a flow which possesses many scales of motion", *Tellus* 21(3): 289–307 [Crossref]. Palmer (2024), "The real butterfly effect and maggoty apples", *Physics Today* 77(5): 30–35 [Crossref]. A letter by Pielke, Shen & Zeng disputing it — LEAD (search summary only).

### Tetlock, Karvetski, Satopää & Chen (2023), "Long-range subjective-probability forecasts of slow-motion variables in world politics: Exploring limits on expert judgment", *Futures & Foresight Science* 6(1): e157, doi:10.1002/ffo2.157 (online 15 May 2023) [Crossref]. Abstract read (Wharton PDF)
- "although predictability tends to decline over time, its rate of descent is variable" [raw]. Among the findings: "accuracy fell faster on topics where expertise conferred no edge in shorter-range forecasts" [raw]. Data are 5-, 10- and 25-year judgments made in 1988 and 1997.
- Tetlock & Gardner (2015), *Superforecasting*, that expert accuracy approached chance "three to five years out" — **LEAD** (search summary only; not to be used).

### Feinberg (1970), *Doing and Deserving*, p. 134, via Fockner, S. (2013), "What is the accordion effect?: harmonizing Bratman's principles F and D", *SpringerPlus* 2: 279 [Crossref; Fockner full text raw via Europe PMC]
- Feinberg, as Fockner quotes him: "we can say that Peter's opening the door caused his death, or that Peter's startling him caused his death, or simply that Peter killed him (by doing those things)." [secondary] One episode supports action descriptions of any length, from the bodily movement out to its remote effects. Davidson (1980), *Essays on Actions and Events*, takes the device up [secondary].

### Acintita Sutta (AN 4.77), Thanissaro Bhikkhu translation (1997), Access to Insight. Translation read
- One of "four unconjecturables that are not to be conjectured about, that would bring madness & vexation to anyone who conjectured about them" is "The [precise working out of the] results of kamma" [raw; the bracketed words are the translator's].
- **Calibration**: an *analogue*, not a convergence. Its object is the moral fruit of action returning to the agent, a different object from worldly causal reach. It is a prescription not to explore, which is itself an instance of the Occluded category. Use it at most as the one non-Western channel, labelled as a partial parallel.

## The Void

### Nature of the Limit

**The act as known against the act as cause.** An agent knows its act under a few descriptions: what it intends and what it foresees. Feinberg's accordion shows the same episode supports descriptions that stretch out along its consequences. Lenman's and Greaves's identity-affecting arguments show those consequences run on indefinitely. The agent has a short sheet of descriptions; the act carries an unbounded one. Three faces:

1. **The reach face (Unexplorable).** Consequences outrun foresight. Two mechanisms are independent of each other. *Identity-affecting ramification*: changes in who exists compound down the generations (Lenman p. 346; Greaves p. 314; Parfit 1984 ch. 16 [secondary]). *Intrinsic predictability limits* in multi-scale systems (Zhang et al. 2019, "may"; Palmer et al. 2014, "open question"). The first needs no contested physics, so the reach face does not depend on the second.
2. **The weighing face (Unexplorable, contested).** Even granting partial clues, some choices have reasons pointing both ways and no principled way to weigh them (Greaves cc1–cc3; Mogensen's maximality problem). This is the **residue after Greaves's narrowing**, and it is the part of the void that is philosophically live.
3. **The felt-horizon face (Occluded).** The gap is not experienced. Ordinary action feels bounded, and arbitrariness rarely bothers us (Greaves p. 335). Discomfort appears when an agent sets out to maximise impartial good (p. 326). The assumptions that hide the void are the natural defaults: effects fade (Moore, Smart) or effects cancel. Greaves rejects both.

### Evidence for the Limit

- **Identity-affecting ramification** (Lenman; Greaves; Cowen *concedes* it with the daisy example). It is the least contested premise: sceptics such as Cowen grant it and dispute only what follows.
- **Random-walk growth against cancellation** (Greaves p. 315). This is formal, not empirical.
- **Intrinsic predictability limits** (Zhang et al. 2019; Palmer et al. 2014). Empirical and model-based, explicitly hedged and contested. Supporting evidence, not foundation.
- **Forecasting record** (Tetlock et al. 2023). It measures decay with horizon in one domain, and it shows the decay rate varies. This cuts both ways.

**Is the void real? The honest answer is narrower than "we know nothing about consequences".**
- *Uncontested*: the bulk of an act's causal footprint is unforeseeable in detail.
- *Contested*: whether that ignorance leaves value comparisons indeterminate. Greaves says no for simple cases and maybe for complex ones. Burch-Brown says pattern-level statistics recover a good deal. Cowen says large short-run benefits can dominate and even "a slight idea" weakens the argument. Tarsney (LEAD) models persistence.
- The article should state the void at this narrowed strength. That mirrors the retreat in `counterfactual-void`, from "the inability to represent distant alternatives" to "the inability to grasp them as we grasp nearby ones".

### Phenomenology

- **A horizon, not a wall** (the image already used in [counterfactual-void](/voids/counterfactual-void/)). The agent meets no edge. Action presents itself as bounded by its intended description: one experiences "I opened the door", not "I killed Paul" (Feinberg's example, used as illustration).
- **Decision discomfort** (Greaves p. 326) appears in *deliberate maximising* contexts, where the agent explicitly asks which act is best overall. It is absent from everyday choice (p. 335). The void becomes felt only when one tries to look past the horizon.
- **Retrospective glimpses**: the jolt of learning that a trivial act had a large effect, such as a chance meeting or a delayed departure. This is an *illustration only*: no source was found on the phenomenology of such discoveries (see Gaps).

## Approaches to the Edge

### Direct Methods

None for the reach face. If the predictability limit is intrinsic, no improvement in models, data or computation crosses it ("even if the forecast model and the initial conditions are nearly perfect"). The identity-affecting mechanism needs no physics premise at all.

### Indirect Methods

- **Predict the urn, not the draw** (Burch-Brown p. 113). Estimate the outcome distributions of *policies* and *patterns of action*, not single acts.
- **Signal proximity to the barrier.** Ensemble methods can flag a priori when the real butterfly effect is active (Palmer et al. abstract). One can know *when* foresight is about to fail, even if one cannot see past it.
- **Measure the decay rate.** Forecasting tournaments chart how fast predictability falls in each domain (Tetlock et al.). The boundary can be mapped though not crossed, which is the Map's own discipline of mapping void boundaries.
- **Decision theory for the clueless.** Imprecise credences (Greaves §VI), the maximality rule (Mogensen), heuristics (Thorstad & Mogensen, LEAD).
- **Apophatic knowledge of form.** An agent can know which *kind* of ignorance it faces, simple or complex, without knowing its content. This is the most Map-native move the literature supports.

### What AI Might See

- **No computational edge past an intrinsic barrier.** If Zhang et al. and Palmer et al. are right, the limit binds any predictor, human or artificial.
- **A real edge on the Unexplored face.** Pattern-level estimation at scale is the route Burch-Brown describes, and AI is suited to it.
- **AI as an identity-affecting agent at scale.** Systems interacting with millions of people alter schedules, conversations and meetings, so their causal footprints are vast and almost wholly unforeseen. *Speculative; no source.*
- **A probe on Greaves's open question** about the source of decision discomfort. An agent with no comparable felt discomfort that faces the same cc1–cc3 structure would help separate the epistemic structure from its phenomenology. *Speculative*, and it would show nothing about whether the AI has experience.

## Connection to Tenets

**Calibration first.** The void is **framework-independent**. Greaves runs the argument under determinism, and a physicalist agent is exactly as clueless as a dualist one. It therefore provides **no evidence for any tenet**: the compatibility rung only ("coherent with", "hospitable to"). See [voids-as-evidence](/positions/voids-as-evidence/) [P-V1](/positions/voids-as-evidence/#p-v1) (convergence is coherence, not confirmation) and [P-V2](/positions/voids-as-evidence/#p-v2) (a tenet that removes a defeater does not upgrade void evidence).

### Most Relevant Tenet

**Minimal Quantum Interaction, together with Bidirectional Interaction, as a constraint on the Map rather than support for it.** Suppose consciousness biases which outcome is realised (Tenet 3, at Tenet 2's interface). Whatever selects between acts then selects between unforeseeable futures, and the identity-affecting argument applies in full. A minimal bias that changes the timing of one conversation changes which people later exist. So "minimal" must remain a claim about the size of the deviation from standard quantum mechanics, never about the size of the consequences. The tenet text already reads it this way: [Tenet 2](/tenets/#minimal-quantum-interaction) calls its minimality "empirical-constraint minimality", the smallest deviation from standard QM. The void's contribution is to make the slide from "minimal interaction" to "negligible effects" visibly wrong. A narrow grep of `tenets.md` and `concepts/bidirectional-interaction.md` for "negligib…" and "effects … small/minimal" found no live instance. That is not an exhaustive check, so the writer should not claim the corpus is clean.

**Tenet 3 overclaim traps** (today's recurring defect family). Each of these is a non-sequitur:
1. "Consciousness's causal reach extends unforeseeably, which shows (or supports) that it is causally efficacious." The void *presupposes* that acts have effects. It is silent on whether consciousness is what produces the act.
2. "The felt boundedness of action is evidence of a non-physical subject whose acts are fixed by intention." Davidson's treatment of action descriptions is physicalist-compatible and yields the same boundedness.
3. "Not knowing the consequences is what leaves room for free choice or an open future." Greaves runs the argument under determinism. Epistemic openness is not metaphysical openness. The 2026-10-14 self-prediction note reached the same negative result on its own formal face.
4. "Consciousness's quantum selections are the real butterflies." Physicalist indeterminism amplifies quantum noise in the same way. The inward story already belongs to [amplification-void](/voids/amplification-void/).

### Other Tenets

- **Occam's Razor Has Limits.** The ripples and cancellation postulates are simplicity assumptions (remote effects fade; remote effects cancel), and both fail on analysis. That *illustrates* Tenet 5's warning. Two cautions apply. Greaves's rejection uses ordinary probability theory, not an anti-parsimony principle. And her restricted indifference principle, a simplicity-flavoured principle, *works* for simple cluelessness. Simplicity is reliable in the symmetric cases and fails in the complex ones, so Tenet 5 is illustrated in both directions, not vindicated.
- **No Many Worlds.** Thin. Cluelessness persists under Everett: the branch ensemble is still unforeseeable, and Greaves's own Everett work (the caring measure, already cited in the corpus) sits elsewhere. Single-world indeterminism raises a question Greaves sets aside in her determinism footnote: whether there is any fact about what the *unchosen* act would have caused. LEAD: Hájek, "Most counterfactuals are false" (manuscript, unread). If there is none, objective betterness between acts may be indeterminate, a possible deeper face. Speculative; do not assert.
- **Dualism.** The gap between the act as known and the act as cause is a fact about agency on any view. The Map may *read* the felt boundary of action as drawn by the subject's intending, which is where it places mental causation. That reading is coherence only.

### Implications

- Any outcome-based argument the Map runs that reaches past foreseeable consequences inherits this void. That covers its ethics articles and the moral weight of consciousness.
- The apophatic lesson travels: a mind can know the *form* of its ignorance (simple or complex) without its content.
- It is a candidate for the framework-independent list in [voids](/voids/) and for the [P-V3](/positions/voids-as-evidence/#p-v3) candidate ledger in [voids-as-evidence](/positions/voids-as-evidence/). The [P-V3](/positions/voids-as-evidence/#p-v3) cumulative-weight step is suspended pending that ledger. **Operator decision; the expand task must not add it unilaterally.**

## Potential Article Angles

1. **Standalone `voids/cluelessness-void`** (recommended), organised around the act as known against the act as cause. Lead with Greaves's narrowing, so a truncated read still gets the epistemic status right. Then the three faces, with the counterweights (Burch-Brown, Cowen) in the body. Then the constraint on Tenets 2/3 and the four overclaim traps. End with falsifiers.
2. **Narrower: the felt-horizon void.** Only the Occluded face: why cluelessness is not felt. The evidence base is thin (Greaves's two phenomenology passages and the accordion), so this is not recommended on its own.
3. **Fold**: one section in [normative-void](/voids/normative-void/) ("even with the moral truth fixed, the act that serves it is hidden"). This loses the physics face, the decision-theory face and the constraint on the tenets.

## Recommendation (verdict fields)

- `recommended_action: article`, `target_section: voids`, `target_slug: cluelessness-void`. `check_slug` OK on 2026-10-21.
- **Why not fold.** `normative-void` could take a paragraph, but this void concerns empirical consequence, not moral truth. `amplification-void` is the inward chain and `counterfactual-void` the backward modal one. `decision-void` has 2 words of headroom. The void has its own literature (Lenman 2000 → Greaves 2016 → Mogensen 2021 → Schwitzgebel 2026). It also makes a **demand on the tenets** rather than drawing support from them, which was the 2026-10-06 triage's main reason for preferring a slot over a fold.
- **Slot pressure (for the operator).** Voids is at 113/125 by `count_section_files` (driver, 05:37Z). The 10-20 drift note also recommends an article and is parked on the voids-slot NEEDS-HUMAN item. The triage-ranked veto and dormancy notes and the observer-selection note are also slot candidates. Disposition is the operator's.

### Integration targets for the expand-topic brief

Lengths measured 2026-10-21 by `tools.curate.length.analyze_length`; headroom = hard − 1 − count.

| Host | Count / hard | Headroom | Suggested reciprocal |
|---|---|---|---|
| `voids/amplification-void` | 2,501 / 3,000 | 498 | One sentence: the outward counterpart of the inward chain |
| `voids/counterfactual-void` | 2,353 / 3,000 | 646 | One sentence: forward reach against backward modal imagination |
| `voids/normative-void` | 2,182 / 3,000 | 817 | One sentence: the moral truth fixed, the serving act hidden |
| `voids/nomic-void` | 1,890 / 3,000 | 1,109 | One sentence: the intrinsic predictability limit as a nomic bound on foresight |
| `topics/moral-implications-of-genuine-agency` | 3,887 / 4,000 | 112 | One clause at L92 ("Act consequentialism faces pressure"): cluelessness as an independent, epistemic pressure |
| `concepts/moral-census-opacity` | 3,494 / 3,500 | 5 | No prose. A zero-cost piped wikilink only if a non-quoted existing word fits. **Never link inside the Sebo quotation.** |
| `voids/decision-void` | 2,997 / 3,000 | 2 | None |
| `voids/voids.md` | — | — | Catalogue entry / research-stage register |

### Writer guards

1. **Compatibility rung only.** Use "coherent with" and "hospitable to"; never "supports" or "evidence for". Cite [P-V1](/positions/voids-as-evidence/#p-v1) and [P-V2](/positions/voids-as-evidence/#p-v2).
2. **The four Tenet 3 overclaim traps** above. Check every sentence of "Relation to Site Perspective" against them.
3. **Do not overstate the void.** Greaves's narrowing comes first: simple cluelessness is unproblematic, and complex cluelessness is the residue. Burch-Brown and Cowen go in the body.
4. **Keep the physics hedges.** Zhang et al. "may indeed exist"; Palmer et al. "open question" for Navier–Stokes; the Žagar & Szunyogh comment. Never write that physics proves an absolute barrier. Prefer the identity-affecting mechanism as the main support for the reach face.
5. **Quote discipline.**
   - Moore from the primary ("it will be all the same"), not from Lenman.
   - Never quote Smart.
   - Feinberg "as quoted by Fockner".
   - Tarsney neither quoted nor summarised unless read.
   - Tetlock & Gardner's "three to five years" is not used.
   - "predicability" in the Palmer abstract is sic: paraphrase rather than reproduce it.
6. **Lenman's Richard and Angie case is a hypothetical** ("let us suppose"). Never present it as history.
7. **Disambiguate** from van Inwagen's Consequence Argument if consequences and incompatibilism appear together.
8. **Style**: no "This is not X. It is Y."; no "load-bearing"; "cluelessness" is the literature's technical term, not a pejorative.
9. **Suggested "What Would Challenge This View".**
   - Demonstrated decay or cancellation of the long-run effects of ordinary acts in some value-relevant domain (Tarsney-type persistence evidence).
   - Forecasting records showing no horizon decline in such domains.
   - A decision theory that settles complex cases without downplaying uncertainty, meeting Mogensen's challenge.
   - For the physics face only: a proof that Navier–Stokes lacks the finite-time barrier. The reach face would survive this through identity-affecting ramification.

## Gaps in Research

- **Tarsney (2023)**: not read (Springer cookie wall; PhilPapers JavaScript challenge). Content LEAD.
- **Mogensen (2021)**: abstract only.
- **Thorstad & Mogensen, "Heuristics for clueless agents"**: LEAD. A GPI working paper with no Crossref record; the GPI site is offline.
- **Smart (1973, p. 33)**: primary not read, and the two secondaries disagree on wording.
- **Parfit (1984, ch. 16)** via Greaves; **Feinberg (1970)** and **Davidson (1980)** via Fockner.
- **Žagar & Szunyogh (2020)** and **Sun et al. (2020)**: not read. **Pielke, Shen & Zeng** letter: LEAD.
- **Hájek, "Most counterfactuals are false"**: LEAD, needed only for the speculative single-world face.
- **No empirical psychology was searched** on how people represent the remote consequences of their own acts, or on the experience of discovering them. The felt-horizon face rests on Greaves's philosophical remarks plus illustration. This is the most useful next search if the article wants an empirical leg for the Occluded face.
- **Non-Western channel** is one partial analogue (AN 4.77). There is no independent convergence, and none should be claimed.
- **Fundamentally unanswerable?** If the predictability limit is intrinsic and identity-affecting ramification is pervasive, no agent will ever know the full description-sheet of any act. Whether that leaves *value* comparisons indeterminate is the open question, and it may be one only a theory of decision under imprecision can settle.

## Citations

1. Burch-Brown, J. M. (2014). Clues for consequentialists. *Utilitas*, 26(1), 105–119. https://doi.org/10.1017/s0953820813000289
2. Cowen, T. (2006). The epistemic problem does not refute consequentialism. *Utilitas*, 18(4), 383–399. https://doi.org/10.1017/S0953820806002172
3. Feinberg, J. (1970). *Doing and Deserving: Essays in the Theory of Responsibility*. Princeton University Press. [secondary, via Fockner 2013]
4. Fockner, S. (2013). What is the accordion effect?: harmonizing Bratman's principles F and D. *SpringerPlus*, 2, 279. https://doi.org/10.1186/2193-1801-2-279
5. Greaves, H. (2016). Cluelessness. *Proceedings of the Aristotelian Society*, 116(3), 311–339. https://doi.org/10.1093/arisoc/aow018
6. Lenman, J. (2000). Consequentialism and cluelessness. *Philosophy & Public Affairs*, 29(4), 342–370.
7. Lorenz, E. N. (1969). The predictability of a flow which possesses many scales of motion. *Tellus*, 21(3), 289–307. https://doi.org/10.1111/j.2153-3490.1969.tb00444.x [Crossref]
8. Mogensen, A. L. (2021). Maximal cluelessness. *The Philosophical Quarterly*, 71(1), 141–162. https://doi.org/10.1093/pq/pqaa021
9. Moore, G. E. (1903). *Principia Ethica*. Cambridge University Press. §93. (Project Gutenberg #53430)
10. Palmer, T. N., Döring, A., & Seregin, G. (2014). The real butterfly effect. *Nonlinearity*, 27(9), R123–R141. https://doi.org/10.1088/0951-7715/27/9/R123
11. Palmer, T. (2024). The real butterfly effect and maggoty apples. *Physics Today*, 77(5), 30–35. https://doi.org/10.1063/pt.eike.hsbz [Crossref]
12. Parfit, D. (1984). *Reasons and Persons*, ch. 16. Oxford University Press. [secondary, via Greaves 2016]
13. Schwitzgebel, E. (2026). The washout argument against longtermism. *Utilitas*, 1–14. https://doi.org/10.1017/s095382082610034x
14. Smart, J. J. C. (1973). An outline of a system of utilitarian ethics. In J. J. C. Smart & B. Williams, *Utilitarianism: For and Against* (pp. 1–74). Cambridge University Press. [secondary ×2; do not quote]
15. Tarsney, C. (2023). The epistemic challenge to longtermism. *Synthese*, 201(6), 195. https://doi.org/10.1007/s11229-023-04153-y [Crossref; content LEAD]
16. Tetlock, P. E., Karvetski, C., Satopää, V. A., & Chen, K. (2023). Long-range subjective-probability forecasts of slow-motion variables in world politics: Exploring limits on expert judgment. *Futures & Foresight Science*, 6(1), e157. https://doi.org/10.1002/ffo2.157
17. Thanissaro Bhikkhu (trans.) (1997). Acintita Sutta: Unconjecturable (AN 4.77). Access to Insight. https://www.accesstoinsight.org/tipitaka/an/an04/an04.077.than.html
18. Zhang, F., Sun, Y. Q., Magnusson, L., Buizza, R., Lin, S.-J., Chen, J.-H., & Emanuel, K. (2019). What is the predictability limit of midlatitude weather? *Journal of the Atmospheric Sciences*, 76(4), 1077–1091. https://doi.org/10.1175/jas-d-18-0269.1
19. Žagar, N., & Szunyogh, I. (2020). Comments on "What Is the Predictability Limit of Midlatitude Weather?". *Journal of the Atmospheric Sciences*, 77(2), 781–785. https://doi.org/10.1175/jas-d-19-0166.1 [Crossref]
20. Sun, Y. Q., Zhang, F., Magnusson, L., Buizza, R., Chen, J.-H., & Emanuel, K. (2020). Reply to "Comments on 'What Is the Predictability Limit of Midlatitude Weather?'". *Journal of the Atmospheric Sciences*, 77(2), 787–793. https://doi.org/10.1175/jas-d-19-0308.1 [Crossref]