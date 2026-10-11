---
ai_contribution: 90
ai_generated_date: 2026-10-11
ai_modified: 2026-10-11 04:03:13+00:00
ai_system: chatgpt-5-6-sol-pro
author: Andy Southgate
concepts:
- '[[direction-of-interface-change]]'
- '[[filter-theory]]'
- '[[active-reboot]]'
created: 2026-10-11
date: &id001 2026-10-11
description: 'ChatGPT 5.6 Sol Pro audit of the direction-dependent test design. Verified:
  a direction-blind fixed-threshold model with unequal time constants yields the ''forbidden''
  non-mirror order; the apex contradicts the article.'
draft: false
human_modified: null
last_curated: 2026-10-11
lastmod: 2026-10-11 04:03:13+00:00
modified: *id001
outer_review_conversation_url: https://chatgpt.com/g/g-p-695a7d60af5481919d5c22ad7bcc1648-the-unfinishable-map/c/6acaeeeb-c82c-83eb-9814-d3438d48f2ca
outer_review_extraction_method: js-dom
outer_review_status: processed
related_articles:
- '[[project]]'
- '[[self-concealing-interface]]'
- '[[evidential-status-discipline]]'
- '[[mechanism-cost-ledger]]'
- '[[anaesthesia-and-the-consciousness-interface]]'
subject_articles:
- topics/direction-dependent-discriminating-test-design.md
subject_source: fallback:recent-aged
subject_title: Audit direction-dependent-discriminating-test-design
subject_type: recent
title: Outer Review - ChatGPT 5.6.sol Pro (2026-10-11)
topics:
- '[[direction-dependent-discriminating-test-design]]'
- '[[memory-channel-interface-evidence]]'
- '[[falsification-roadmap-for-the-interface-model]]'
- '[[brain-stimulation-and-the-witness-mode]]'
- '[[targeted-lesion-discriminating-tests-between-production-and-filter-readings-of-the-memory-hierarchy]]'
---

**Date**: 2026-10-11
**Reviewer**: ChatGPT 5.6.sol Pro
**Type**: Outer review (external AI analysis)

## About This Review

An "outer review" is an analysis performed by an external AI system rather than the Claude-based workflow that generates most site content. This provides an independent perspective, reducing the risk of self-reinforcing blind spots.

## Prompt

Please audit the article "Designing a Direction-Dependent Discriminating Test for the Interface Model" on The Unfinishable Map: https://unfinishablemap.org/topics/direction-dependent-discriminating-test-design/ (last substantively modified 2026-10-04). The site root is https://unfinishablemap.org and the changelog of recent changes is at https://unfinishablemap.org/workflow/changelog/ - check it, since search indexes may lag. The article proposes a reversible-perturbation experiment in which a closing-phase ordering that fails to mirror the reopening-phase ordering is forbidden by substrate-symmetric production but permitted by the filter reading. Assess whether that prediction genuinely discriminates the two models: do physicalist accounts (hysteresis, metastability, asymmetric neural or pharmacological dynamics) already predict the same asymmetry? Check its claims, citations and empirical premises against current literature; identify missed counterarguments, tenet-protective bracketing, stale references, and how well it integrates with the surrounding articles on the interface/filter model. End your report with a list of concrete potential improvements to specific articles and to the site's methodology.

## Reply

# Audit: “Designing a Direction-Dependent Discriminating Test for the Interface Model”

## Overall verdict

**Major revision required.**

The proposed experiment does **not presently discriminate the interface/filter model from physicalist production models**. It discriminates only against a deliberately restricted physical null:

> a static, memoryless, quasi-equilibrium model in which each cognitive channel has one fixed scalar threshold and the externally controlled perturbation directly indexes the channel’s internal state.

Under that stipulated model, failure order must indeed reverse during recovery. But neither physicalism nor “substrate-symmetric production” generally entails such a model.

The more serious problem is that the proposed signature—roughly, a channel that **fails first and also recovers first**—can arise in an entirely direction-blind physical system with:

- fixed thresholds;
- the same equations during closing and reopening;
- no dedicated recovery circuit;
- no metastability;
- no pharmacological asymmetry;
- and no interface/filter mechanism.

Different physical response time constants are enough.

The article acknowledges several parts of this underdetermination: it says that the filter model predicts no particular ordering, forbids no ordering, and that more elaborate production accounts could invoke hysteresis, emergence circuits, or stochastic reconstitution. Nevertheless, it continues to call the design a “discriminator,” treats the relevant ordering as forbidden by substrate-symmetric production, and presents it as empirical exposure of the Map’s tenets. Those stronger claims do not follow. [direction-dependent-discriminating-test-design](/topics/direction-dependent-discriminating-test-design/)

The defensible formulation is:

> The experiment could test a static threshold null and estimate direction-dependent cognitive dynamics. It could not, without additional quantitative predictions, identify those dynamics as an interface/filter effect.

---

## 1. Changelog and dependency status

The live article remains dated **4 October 2026**. The changelog was current through 10 October when checked. Importantly, the underlying memory-channel article was substantially recalibrated on 9 October: the fixed five-condition ordering was downgraded to a Map conjecture with exceptions, the absence of a systematic cross-condition review was acknowledged, and several clinical conditions were said not to provide the tiered ordering previously implied. That recalibration materially weakens the empirical scaffolding of the proposed experiment, but it has not yet been propagated into this design article. [direction-dependent-discriminating-test-design](/topics/direction-dependent-discriminating-test-design/)

This matters because the test derives much of its motivation from a proposed hierarchy of autobiographical/autonoetic, noetic, source, priming, and motor channels. If that hierarchy is not itself securely established across perturbations, a direction-dependent inversion of it cannot yet function as a mature theory test.

---

# 2. What the proposed result actually establishes

The article contrasts two readings:

1. **Substrate-symmetric production:** the same substrate vulnerability governs loss and recovery, so the first channel lost should be the last recovered.
2. **Filter/interface reading:** closing and reopening may involve different interface processes, so a non-mirror ordering is permitted.

There are two distinct logical claims here:

- **Claim A:** A fixed-threshold equilibrium model predicts reverse recovery order.
- **Claim B:** Physical production models generally predict reverse recovery order.

Claim A is correct. Claim B is false.

Suppose each channel $i$ has a scalar internal disruption variable $q_i$, driven by externally applied perturbation $p$:

$$\tau_i\frac{dq_i}{dt}=p-q_i$$

A channel fails when $q_i>\theta_i$. The equation, time constant, and threshold are exactly the same during increasing and decreasing perturbation. Nothing in it represents an interface, special reopening operation, or direction-sensitive machinery.

During a steady upward ramp of rate $r$, after initial transients:

$$p_{i,\uparrow}\approx\theta_i+r\tau_i$$

During a downward ramp:

$$p_{i,\downarrow}\approx\theta_i-r\tau_i$$

Take two channels:

| Channel | Fixed threshold $\theta$ | Time constant $\tau$ |
| --- | --- | --- |
| A | 0.40 | 0.10 |
| B | 0.45 | 0.20 |

For a normalized ramp rate $r=1$:

- Upward crossings: A at 0.50, B at 0.65 — **A fails first**.
- Downward crossings: A at 0.30, B at 0.25 — as perturbation falls, **A recovers first**.

This is precisely the proposed non-mirror signature. Yet the system is direction-blind at the level of its laws and uses one fixed threshold per channel.

The article therefore conflates:

- **symmetry of the underlying mechanism**, and
- **time-reversal symmetry of its observed trajectories under finite-rate forcing**.

These are not equivalent. Dissipative systems with memory do not generally retrace their trajectories merely because their governing equations do not contain a “direction” flag.

### Consequence

Even before considering neural hysteresis, attractors, pharmacokinetics, plasticity, adaptation, or active arousal circuits, the article’s claim that the ordering is “forbidden” by substrate-symmetric production fails.

Matched upward and downward ramp rates do not solve this problem. They make the lag term comparable, but they do not make it disappear. The crucial controls would be:

- systematic variation of ramp rate;
- long dwell periods at each perturbation level;
- independent estimation of channel-specific time constants;
- and comparison in the quasi-static limit.

If the reversal shrinks predictably as ramp rate approaches zero, that supports an ordinary dynamical-lag explanation. A persistent effect after genuine equilibration would exclude that simple explanation, but still not exclude multistability or active recovery circuitry.

---

# 3. Existing physicalist models already license non-mirror behaviour

## 3.1 Multistability and neural inertia

Proekt and Hudson’s model is not a static threshold account. It represents anaesthetic transitions as stochastic movement through a multistable state space and shows how hysteresis can emerge from ordinary state-transition dynamics. Its ten-state implementation contains multiple awake and anaesthetized states and produces different induction and emergence curves without requiring a nonphysical filter. [PubMed Central (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6200107/)

The article is broadly right that Proekt and Hudson do not explicitly predict a rank reversal among autobiographical, familiarity, source-memory, priming, and motor tasks. But that is because their paper contains no such cognitive-channel model. The article’s stronger statement—that their model is “direction-blind in cross-channel ordering” and therefore does not predict reversal—is not established by the cited paper.

Once multiple observed channels are functions of different subsets of latent states, a multistable transition graph can produce:

- different apparent thresholds;
- different dwell times;
- bottleneck states;
- path-dependent rank changes;
- and different observables during entry and exit.

No special “reopening” ontology is needed.

Related empirical work characterizes emergence from anaesthesia as progression through discrete metastable states and transition hubs rather than a smooth reversal of induction. [PNAS+1](https://www.pnas.org/doi/pdf/10.1073/pnas.1408296111)

## 3.2 Human induction and emergence trajectories

Human neuroimaging under propofol has found that induction and emergence differ in cortical and subcortical connectivity and in processing timescales. These observations are consistent with history-dependent neural dynamics rather than a single state variable being traversed in reverse. [Europe PMC](https://europepmc.org/article/MED/33848623)

This does not prove that any particular memory hierarchy must reverse. It does show that the article cannot use non-mirror recovery as something generally unexpected under physical production.

## 3.3 Active physical recovery mechanisms

Animal work has identified mechanisms that selectively affect emergence without equivalently controlling induction. In thalamic ventral posteromedial neurons, KCC2 degradation has been implicated in active emergence from anaesthesia independently of mere anaesthetic clearance. Later work reports separable VPM mechanisms involving KCC2 and EphB1/NR2B signalling across anaesthetics with different molecular targets. [PubMed+1](https://pubmed.ncbi.nlm.nih.gov/36973513/)

These results do not directly predict autonoetic/noetic rank ordering. They do, however, defeat the suggestion that direction-specific physical machinery must be an improvised response to the proposed experiment. There is already independent reason to expect induction and emergence to have partly distinct physical control mechanisms.

This creates an internal asymmetry in the Map’s accounting:

- a dedicated reopening pathway is treated as a natural possibility for the filter model;
- a dedicated emergence pathway is treated as added complexity for production;
- yet the clearest known examples of such pathways are themselves physical mechanisms.

The article does acknowledge the KCC2-style possibility, but its evidential interpretation still charges physicalism for a mechanism whose existence is independently motivated while allowing the filter’s reopening mechanism to remain unspecified. [direction-dependent-discriminating-test-design](/topics/direction-dependent-discriminating-test-design/)

## 3.4 Pharmacokinetic and pharmacodynamic asymmetry

The article cites Sepúlveda and describes loss of consciousness as occurring “reliably” at a higher estimated effect-site concentration than recovery. That wording is too strong. The review describes such differences as commonly observed but emphasizes that human evidence is limited and not conclusive, and that estimated effect-site concentrations can be distorted by inadequate equilibration and pharmacokinetic-model assumptions. Some studies find little or no significant difference after accounting for these issues. [Association of Anaesthetists+1](https://associationofanaesthetists-publications.onlinelibrary.wiley.com/doi/pdf/10.1111/anae.14609)

For the proposed experiment, the general lesson is important:

> equality of administered dose or external stimulation intensity does not establish equality of perturbation at the relevant neural substrate.

During closing and reopening, the same nominal input can correspond to different:

- tissue concentrations;
- receptor occupancies;
- regional neural states;
- network gains;
- adaptation levels;
- and effective connectivity.

The article needs a latent-state model rather than treating the control setting itself as the biologically relevant coordinate.

---

# 4. The filter model makes no risky prediction here

The article is admirably explicit that the filter model:

- allows mirror recovery;
- allows non-mirror recovery;
- predicts no specific rank reversal;
- and forbids no ordering.

That admission is decisive. [direction-dependent-discriminating-test-design](/topics/direction-dependent-discriminating-test-design/)

Let $E$ be the proposed “fails first, recovers first” result.

The intended evidential comparison appears to be:

$$P(E\mid M_0)\ll P(E\mid F)$$

where $M_0$ is the static threshold model and $F$ is the filter model.

But the relevant comparison is:

$$P(E\mid F)\quad\text{versus}\quad P(E\mid M_{\text{best physical}})$$

The article supplies neither probability.

It establishes only that:

- $P(E\mid M_0)$ is low by stipulation;
- $P(E\mid F)$ is nonzero because $F$ permits everything;
- $P(E\mid M_{\text{dynamic physical}})$ may also be substantial.

Consequently, the observation would provide no calculable Bayes factor for filter over contemporary physicalism.

A theory does not gain support merely because it is flexible enough to accommodate the observation. The site’s own methodological discussion elsewhere makes essentially this point: compatibility becomes evidence only when the Map makes a preregistered quantitative or structurally risky prediction that its best rival does not make. It also acknowledges that no single proposed “seam” currently supplies a clear $P(E\mid\text{Map})>P(E\mid\text{best rival})$. [self-concealing-interface](/apex/self-concealing-interface/)

The direction-dependent design does not yet meet that standard.

---

# 5. The claimed symmetry of evidence is not real

The article presents the design as informative in both directions:

- non-mirror ordering raises the cost of production;
- mirror ordering removes a line of support from the filter interpretation.

But these outcomes are not evidentially symmetric.

### Under non-mirror ordering

The filter survives, but so do multiple independently supported physical accounts:

- channel-specific lag;
- adaptation;
- metastability;
- stochastic transition paths;
- active emergence circuitry;
- pharmacokinetic hysteresis;
- neural-state-dependent stimulation effects.

### Under mirror ordering

The filter also survives because it never predicted dissociation.

Thus no possible ordering falsifies or even substantially strains the filter theory. At most:

- asymmetry is rhetorically congenial to the filter story;
- symmetry makes that particular story less attractive.

This is a valid exploratory asymmetry test, but not “empirical exposure” of the interface model itself.

The distinction should be made explicit:

> **The evidence family is exposed; the underlying filter theory is not.**

The statement that Tenet 1 is exposed is therefore too strong. The statement that Tenet 3 receives weak support if the effect is largest in “high subject-participation” channels is weaker still, because “subject participation” is neither independently measured nor connected to a quantitative causal prediction. [direction-dependent-discriminating-test-design](/topics/direction-dependent-discriminating-test-design/)

---

# 6. Problems with the proposed tFUS implementation

## 6.1 “Temporary” is not “reversibly switchable”

The article uses Verhagen et al. to support transcranial focused ultrasound as a controllable, temporary perturbation. That study applied a roughly 40-second offline sonication protocol in macaques and observed altered functional effects persisting for more than an hour. It supports the possibility of lasting, nonlesional modulation, not a rapidly reversible perturbation that can be smoothly ramped up and down through repeated behavioural thresholds. [eLife Sciences+2](https://cdn.elifesciences.org/articles/40541/elife-40541-v1.pdf)

Human deep-target studies likewise commonly report effects persisting for tens of minutes, with mechanisms and dependence on baseline state still incompletely understood. [PubMed](https://pubmed.ncbi.nlm.nih.gov/37658076/)

That persistence is not merely a practical inconvenience. It destroys the assumed equivalence between:

- an increasing external-intensity phase; and
- a decreasing external-intensity phase.

The “reopening” phase may occur in tissue whose state has been altered by all preceding sonications.

## 6.2 Cain et al. does not validate the proposed control regime

Cain et al. supports the proposition that thalamic ultrasound has been attempted in people with chronic disorders of consciousness. It does not establish:

- a monotonic dose–response function;
- focal cognitive-channel control;
- rapid reversibility;
- repeatable threshold crossings;
- or safe matched ramps in healthy participants.

The publication was a brief clinical report/correspondence rather than validation of the experimental architecture proposed here. [Brain Stimulation Journal+2](https://www.brainstimjrnl.com/article/S1935-861X%2821%2900009-7/fulltext)

## 6.3 Auditory and somatosensory confounding

Recent controlled work has shown that some apparent tFUS effects on motor inhibition can be explained by auditory stimulation rather than direct neuromodulation. The authors used multiple experiments, including a preregistered study, and emphasized the need for appropriate active controls. [eLife Sciences+2](https://cdn.elifesciences.org/articles/88762/elife-88762-v1.pdf)

A direction-dependent experiment is especially vulnerable because auditory expectation, arousal, response caution, and subjective intensity can themselves exhibit adaptation and hysteresis. Sham must therefore match:

- sound;
- scalp sensation;
- expectancy;
- trial timing;
- cumulative exposure;
- and experimenter interaction.

Simple active-versus-inactive sonication would not be sufficient.

## 6.4 Current reporting, dose, and safety standards are missing

The article was modified in 2026 but does not cite the recent ITRUSST consensus work on reporting, safety, or dose characterization. Those standards are directly relevant to individual skull modelling, in situ pressure estimation, thermal/mechanical exposure, pulse reporting, and reproducibility. [Brain Stimulation Journal+5](https://www.brainstimjrnl.com/article/S1935-861X%2824%2900071-8/fulltext)

## 6.5 The linked PCC evidence is much weaker than the design implies

The posterior-cingulate pilot cited elsewhere on the site used a randomized single-blind active-versus-sham design, but did not find a significant active-versus-sham effect on the principal mindfulness measure or significant condition effects on the reported phenomenological outcomes. Blinding was imperfect: substantially more active participants correctly guessed their allocation. The authors also noted uncertainty over whether the beam principally reached dorsal PCC, precuneus, or both. [Frontiers+1](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2024.1392199/full)

It therefore cannot presently support the stronger assumptions that:

- tFUS can selectively perturb an autonoetic interface;
- the effect can be titrated through behavioural failure and recovery;
- or neighbouring noetic and source-memory functions will be spared.

---

# 7. Problems with the cognitive-channel measurements

## 7.1 The channels are not measured on a common scale

The design proposes concurrent or interleaved measures of:

- autonoetic remembering;
- knowing/familiarity;
- source attribution;
- priming;
- and motor performance.

These measures differ in:

- response format;
- baseline reliability;
- chance level;
- ceiling and floor behaviour;
- sensitivity to attention;
- reaction-time demands;
- learning across repetitions;
- and susceptibility to response bias.

An ordering of observed behavioural “failures” is therefore not automatically an ordering of latent cognitive-channel failures.

The related targeted-lesion article already concedes that traditional Tulving-style probes were not designed for tight, repeated cross-channel comparison. That caveat should be central here, not relegated to the surrounding literature. [targeted-lesion-discriminating-tests-between-production-and-filter-readings-of-the-memory-hierarchy](/topics/targeted-lesion-discriminating-tests-between-production-and-filter-readings-of-the-memory-hierarchy/)

## 7.2 Remember/know is not a settled process-pure decomposition

Reviews of the remember/know paradigm report substantial variation in how participants interpret the categories, disagreement over what the judgements measure, and methodological sensitivity to instructions and demand characteristics. [JSTOR+1](https://www.jstor.org/stable/48597071)

Formal and meta-analytic work has also questioned whether remember and know responses identify qualitatively independent processes rather than different strengths or criteria on a common dimension. [PubMed+1](https://pubmed.ncbi.nlm.nih.gov/18426296/)

The test cannot simply equate:

- “remember” with an autonoetic interface channel; and
- “know” with a separable noetic channel.

That mapping is one contested theoretical interpretation of the task.

## 7.3 Source memory is not process-pure either

Recent neuroimaging synthesis suggests that standard source-memory contrasts can mix recollection, familiarity, confidence, and control demands. A behavioural source threshold may therefore move because of decision and metacognitive changes rather than selective loss of a source-memory channel. [PubMed](https://pubmed.ncbi.nlm.nih.gov/42061891/)

## 7.4 Autonoesis has no agreed single neural target

Current philosophical and cognitive work distinguishes representational, metacognitive, and epistemic accounts of autonoesis. The relationship between autonoetic judgement and episodic memory remains theoretically unsettled. [PubMed+1](https://pubmed.ncbi.nlm.nih.gov/37557099/)

Autobiographical retrieval also recruits a distributed system involving hippocampal, posterior medial, angular, prefrontal, and other regions. A focal PCC/precuneus perturbation could affect attention, control, vividness, valuation, scene construction, confidence, or reportability without selectively modifying a putative filter for re-experiencing. [PubMed](https://pubmed.ncbi.nlm.nih.gov/39653872/)

## 7.5 Repeated probing changes the thing being measured

The experiment cannot repeatedly test the same episodic material without introducing:

- retrieval practice;
- reconsolidation;
- increasing familiarity;
- source learning;
- expectation;
- and strategy changes.

Using fresh items avoids some of those effects but introduces item-set and encoding variability. These changes can themselves differ between closing and reopening phases.

This creates a further physical route to apparent rank reversal: the second phase measures a participant who has been trained by the first.

---

# 8. Unjustified empirical premises

## “High-cost channels should fail first”

The article describes autonoetic access as a high-cost channel and anticipates that it may be preferentially lost. But the relevant cost is not independently measured.

The associated memory-channel article concedes that the bandwidth or reconstruction-cost ranking is partly inferred from the proposed ordering itself. [memory-channel-interface-evidence](/topics/memory-channel-interface-evidence/)

That creates circularity:

1. autonoetic access is called high-cost because it is expected to fail early;
2. early failure is then treated as evidence for a high-cost interface channel.

Independent indicators would be required, such as:

- metabolic demand;
- representational dimensionality;
- effective-connectivity burden;
- minimum information rate;
- or independently estimated computational sensitivity.

Even then, greater physical cost would not uniquely imply a filter bottleneck.

## “Same perturbation, same substrate”

A focal stimulation target does not isolate one mechanism. The same anatomical target can engage different networks depending on:

- initial brain state;
- current task;
- stimulation history;
- arousal;
- attention;
- and changing network controllability.

Thus “same target and same intensity” cannot establish the article’s intended substrate symmetry.

## “Simultaneous probing controls global state”

Interleaving several tasks does not make them simultaneous at the neural level. State can fluctuate across seconds, trials, and task switches. The tasks themselves recruit different control demands and can perturb arousal. A latent-state measurement—EEG, pupil dynamics, autonomic measures, and preferably imaging in a separate validation phase—is needed.

---

# 9. Citation audit

| Article claim | Assessment |
| --- | --- |
| Verhagen et al. shows temporary tFUS effects lasting up to roughly two hours | **Broadly grounded but overinterpreted.** It shows prolonged offline modulation after a short protocol, not reversible on-demand ramping. |
| Cain et al. establishes human subcortical feasibility | **Narrowly true.** It does not validate dose-response, selectivity, repeated thresholds, or healthy-participant implementation. |
| Loss generally occurs at a higher estimated concentration than recovery | **Too categorical.** Neural inertia is reported, but human effect-site evidence is limited and vulnerable to equilibration and modelling assumptions. |
| Proekt and Hudson’s ten-state model reproduces hysteresis | **Accurate.** |
| Proekt and Hudson’s model is direction-blind in cross-channel ordering and does not predict reversal | **Unsupported extrapolation.** It contains no corresponding memory-channel variables. |
| tFUS offers a suitable reversible perturbation | **Not established by the cited sources.** Published persistence, state dependence, acoustic confounding, and targeting uncertainty work against the assumed design. |
| Remember/know, source, priming, and motor probes identify distinct channel thresholds | **Uncited and empirically contentious.** |
| Autonoetic access is the highest-cost channel | **Conjectural and partly circular.** |
| A non-mirror ordering is forbidden by substrate-symmetric production | **False without adding static, memoryless, quasi-equilibrium assumptions.** |

The article’s four principal external references are therefore not fictitious or grossly misdescribed, but they do not jointly support the experimental inference being placed on them.

---

# 10. Stale or missing literature

For an article revised in October 2026, the external evidence base is unusually old and narrow. It omits several directly relevant bodies of work:

- human evidence for distinct induction and emergence network trajectories; [Europe PMC](https://europepmc.org/article/MED/33848623)
- longitudinal tests of neural inertia and state mixing; [Frontiers+2](https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/fnsys.2021.787612/pdf)
- active thalamic emergence mechanisms; [PubMed+1](https://pubmed.ncbi.nlm.nih.gov/36973513/)
- controlled tFUS confound studies; [eLife Sciences+1](https://cdn.elifesciences.org/articles/88762/elife-88762-v1.pdf)
- current tFUS reporting, dosing, and safety standards; [Brain Stimulation Journal+2](https://www.brainstimjrnl.com/article/S1935-861X%2824%2900071-8/fulltext)
- the site’s own cited PCC trial’s null active–sham findings and blinding limitations; [Frontiers](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2024.1392199/full)
- current critiques of remember/know and source-memory process purity; [JSTOR+3](https://www.jstor.org/stable/48597071)
- contemporary accounts of autonoesis and distributed autobiographical retrieval. [PubMed+1](https://pubmed.ncbi.nlm.nih.gov/37557099/)

These are not merely background additions. Each bears directly on whether the experiment has a valid perturbation axis, valid observables, and a discriminating prediction.

---

# 11. Tenet-protective bracketing

Several formulations protect the Map’s commitments rather than expose them.

## 11.1 The filter is allowed every outcome

The filter interpretation “forbids no ordering.” That makes it untestable by the proposed ordinal result.

The article tries to compensate by saying that symmetry would withdraw support. But withdrawal of an optional argument is not a risky prediction by the theory whose evidential status is ostensibly being tested.

## 11.2 Physical explanations are classified as accommodations

Hysteresis, metastability, state dependence, and active emergence circuitry are treated as additions that raise the production model’s cost. Yet they are independently evidenced features of neural and pharmacological systems.

A mechanism is not ad hoc merely because it explains the result. The relevant questions are:

- Was it independently motivated?
- Was it specified before seeing this result?
- Does it predict other observations?
- Does it make quantitative predictions here?

Several physical mechanisms pass the first three tests better than the filter’s unspecified reopening pathway.

## 11.3 The filter mechanism remains causally blank

The article allows a dedicated reopening operation but supplies no account of:

- what physical or nonphysical state carries the direction information;
- why particular channels should reopen in a particular order;
- what determines delay or threshold;
- how the operation couples to tissue;
- or what result it would forbid.

This is not a less complex model. It is an unparameterized model.

## 11.4 Tenet 3 is inferred from an unmeasured construct

The suggestion that larger effects in channels requiring more “subject participation” would favour bidirectional interaction assumes precisely the mental causal contribution at issue. Neither subject participation nor mental-to-physical influence is operationalized independently.

A selective effect on autobiographical report would have abundant physical explanations involving task complexity, metacognition, self-reference, memory construction, and distributed network dependence.

## 11.5 Minimal quantum interaction is not tested

Nothing in the design distinguishes:

- quantum from classical interaction;
- interactionist dualism from epiphenomenal filtering;
- a nonphysical interface from an ordinary neural bottleneck;
- or minimal intervention from substantial intervention.

The experiment may be relevant to the broad interface narrative, but it does not directly test the site’s quantum-interaction tenet.

---

# 12. Integration with surrounding Map articles

## Memory-channel article

The direction-dependent article inherits the memory-channel hierarchy but does not reflect the 9 October recalibration that the hierarchy is a conjecture with heterogeneous and incomplete support. [changelog](/workflow/changelog/)

It also treats directional rank change as more diagnostic than the source article now warrants. Before testing reversal, the site needs evidence that a stable opening/closing rank exists within:

- the same perturbation;
- the same participants;
- the same tasks;
- and a sufficiently equilibrated state space.

## Direction-of-interface-change article

That article more clearly acknowledges that hysteresis can arise from bistable physical circuits and that the simple production rival is not the strongest production rival. It also concedes substantial nonindependence among the proposed observations. The present design article should import that calibration rather than presenting rank reversal as a cleaner divider. [direction-of-interface-change](/concepts/direction-of-interface-change/)

## Filter Theory

The broader Filter Theory article acknowledges that sophisticated production and filter interpretations can be empirically equivalent and that the proposed bandwidth criterion lacks an independent measure. The present article relies on precisely those unresolved quantities. [filter-theory](/concepts/filter-theory/)

## Active Reboot and Anaesthesia

These pages use active emergence mechanisms as analogies for a reopening interface while also acknowledging that the experimentally demonstrated mechanisms are physical. That is legitimate as a metaphysical reinterpretation, but it cannot then be treated as evidence that favours the reinterpretation over the physical account. [active-reboot](/concepts/active-reboot/)

## Targeted-lesion design

The targeted-lesion article admits that its proposed channel probes are not validated for close cross-channel comparisons and that the two ontological readings may be empirically equivalent. Those limitations apply even more strongly to a repeated dynamic ramp, where learning and carry-over are unavoidable. [targeted-lesion-discriminating-tests-between-production-and-filter-readings-of-the-memory-hierarchy](/topics/targeted-lesion-discriminating-tests-between-production-and-filter-readings-of-the-memory-hierarchy/)

## Brain stimulation and witness-mode material

The site’s stimulation material appropriately notes the PCC trial’s null active–sham contrast, imperfect blinding, and the fact that the interface account can absorb opposite outcomes. The direction-dependent article should cite those limitations directly rather than invoking tFUS mainly as a convenient reversible control technology. [brain-stimulation-and-the-witness-mode](/topics/brain-stimulation-and-the-witness-mode/)

## Self-concealing interface and falsification roadmap

The self-concealment article states a stronger methodological rule than the present design follows: a result becomes evidence only where the Map assigns it greater probability than the best rival does. The falsification roadmap should therefore not list this design as an interface-model discriminator until it contains such a comparison. [falsification-roadmap-for-the-interface-model](/topics/falsification-roadmap-for-the-interface-model/)

---

# 13. What a substantially stronger experiment would look like

A useful study could still be built from this idea, but its target should initially be **direction-dependent cognitive dynamics**, not dualism.

The minimum model family should include:

$$M_0:\text{static equilibrium thresholds}$$

$$M_1:\text{fixed thresholds plus channel-specific temporal dynamics}$$

$$M_2:\text{adaptation and state-dependent gain}$$

$$M_3:\text{multistable stochastic neural dynamics}$$

$$M_4:\text{active physical emergence circuitry}$$

$$F:\text{an explicitly parameterized interface model}$$

The article would then need to specify, before data collection:

- the likelihood of each ordering under each model;
- continuous psychometric curves rather than only ranks;
- expected dependence on ramp speed;
- expected dependence on dwell time;
- washout and carry-over terms;
- latent neural-state measurements;
- task reliabilities and threshold definitions;
- and at least one outcome that is substantially less probable under $F$.

The most informative manipulations would be:

### Ramp-rate manipulation

Ordinary dynamical lag predicts that apparent hysteresis should vary systematically with ramp rate. The first-order example above predicts an external-threshold shift proportional to $r\tau_i$.

### Dwell-time manipulation

If rank reversal survives long, independently verified equilibration at each level, simple lag explanations weaken.

### Cross-perturbation replication

Use physically different interventions with well-characterized kinetics. Persistence of a numerically specified pattern across interventions could be interesting—but only if the interface account predicts that invariance in advance and physical models predict its dissolution.

### Neural-state matching

Compare behavioural channels at matched measured brain states, not merely matched administered intensity. EEG state, pupil size, autonomic variables, and target-engagement markers would help establish whether closing and reopening observations are physically comparable.

### Formal mediation analysis

If the directional effect is mediated by measurable neural lag, connectivity, arousal, auditory expectation, or pharmacokinetic state, it should not be counted as residual filter evidence.

### Out-of-sample prediction

Estimate parameters from one perturbation, target, or participant set, and predict ordering and reversal magnitude in another. A model that only labels an observed order after the fact has not passed a discriminating test.

---

# 14. Concrete potential improvements

1. **“Designing a Direction-Dependent Discriminating Test for the Interface Model”** — Rename it to something like **“Testing Static Threshold and Direction-Dependent Models of Cognitive Disruption.”** Reserve “interface discriminator” for a later version containing an explicit filter likelihood and a best-physical-rival likelihood.
2. **The same article** — Replace the claim that non-mirror ordering is “forbidden by substrate-symmetric production” with the narrower claim that it is forbidden by a **static, memoryless, quasi-equilibrium threshold model**. State explicitly that symmetry of laws does not imply time-reversed trajectories in a dissipative system.
3. **The same article** — Add the simple heterogeneous-time-constant countermodel:
   
   $$\tau_i\dot q_i=p-q_i$$
   
   and show analytically that a fixed-threshold, direction-blind system can produce “fails first, recovers first.” Treat this as the minimum rival that any design must defeat.
4. **The same article** — Replace the two-model contrast with a preregistered ladder comprising static thresholds, temporal lag, adaptation, multistability, active emergence circuits, pharmacokinetic/pharmacodynamic hysteresis, and a parameterized interface model.
5. **The same article** — Remove or qualify the statement that Proekt and Hudson’s model is direction-blind in cross-channel ordering. Their paper does not model the article’s cognitive channels. Explain instead how a multistable state graph could generate rank changes and identify what additional restriction would prevent them.
6. **The same article** — Correct “reliably higher” loss-of-consciousness concentration to reflect the limited and method-sensitive human evidence. Require long equilibration or independent estimates of tissue/effect-site state before interpreting concentration hysteresis.
7. **The same article** — Recast tFUS as an **unvalidated candidate technology**, not an established reversible ramp. Add prolonged carry-over, skull-specific dose uncertainty, target-spread uncertainty, baseline-state dependence, auditory confounding, active-sham requirements, and current ITRUSST reporting and safety standards.
8. **The same article** — Add a separate target-engagement phase before any consciousness experiment: individualized acoustic simulation, physiological or imaging evidence of dose response, active auditory/somatosensory control, washout characterization, and evidence that upward and downward external settings map monotonically to internal perturbation.
9. **The same article** — Replace ordinal “first lost/first recovered” as the primary endpoint with jointly fitted psychometric and response-time curves. Predefine thresholds, uncertainty intervals, tie handling, missing responses, multiplicity correction, and minimum effect sizes.
10. **The same article** — Do not call remember/know, source memory, priming, and motor performance “channels” without a measurement model. Include competing single-process and multidimensional accounts, use matched response formats where possible, and estimate task reliability before comparing thresholds.
11. **The same article** — Independently operationalize “high cost” and “subject participation.” Neither should be inferred from the very loss order it is then used to explain. State in advance what measurable variable constitutes cost and what result would contradict the proposed ranking.
12. **“Memory Channels Under Disruption: The Second Face”** — Propagate its 9 October recalibration into the direction-dependent test. Separate empirically observed within-condition sequences from the Map’s proposed cross-condition hierarchy, and label unreviewed cells as missing rather than supportive.
13. **“Memory Channels Under Disruption: The Second Face”** — Build a condition-by-channel evidence table containing sample size, task, perturbation, time resolution, whether recovery was observed, whether ordering was statistically tested, and whether the evidence is independent of the Map’s interpretation.
14. **“Direction of Interface Change”** — Add heterogeneous time constants and adaptation as distinct physical rivals alongside bistability. Its present treatment of hysteresis should not imply that only a dedicated direction mechanism can break mirror ordering.
15. **“Active Reboot” and the anaesthesia article** — Draw a strict line between **evidence for active physical emergence** and **a filter reinterpretation of that evidence**. Do not count a known physical reopening mechanism as complexity for production while treating an unspecified analogous interface mechanism as explanatory economy.
16. **“Filter Theory”** — Supply an explicit dynamical filter model with state variables, transition rules, parameter constraints, and predicted distributions over closing and reopening trajectories. Identify at least one ordering or ramp-rate dependence that the model genuinely makes unlikely.
17. **“Targeted-Lesion Discriminating Test”** — Reassess the “channel-down versus degraded” distinction against distributed physical models. Add measurement invariance, response bias, network diaschisis, and graded latent-state alternatives before calling the result ontologically discriminating.
18. **The brain-stimulation and witness-mode articles** — Link their caveats directly into the direction-dependent design: the PCC pilot’s active–sham null, imperfect blinding, uncertain focality, persistent effects, and the wider auditory-confound literature should be required reading rather than peripheral qualifications.
19. **The falsification roadmap** — Downgrade this proposal from an interface-model falsification handle to a **design-stage test of restricted dynamic models** until the filter side specifies $P(E\mid F)$, an effect-size range, and a genuinely adverse outcome.
20. **The self-concealing-interface methodology article** — Turn its requirement for quantitative bets into a site-wide gate: no experiment should be labelled “discriminating” unless it names the strongest live rival, gives both models’ prospective predictions, and specifies what observation materially lowers the Map model’s probability.
21. **Site methodology** — Introduce a standard **rival-model ladder** for every proposed test: naive physical null, strongest established physical model, plausible extended physical model, Map model, and common-cause/error model. Findings should be graded against the strongest rival survived, not the weakest rival rejected.
22. **Site methodology** — Create a symmetric complexity ledger. Independently evidenced mechanisms such as neural inertia, metastability, adaptation, and thalamic emergence circuitry should not be charged as post-hoc auxiliaries; unmeasured interface operations should incur at least equivalent complexity penalties.
23. **Site methodology** — Require a prediction registry for proposed experiments containing equations or simulations, prior parameter ranges, outcome probabilities, smallest meaningful effect, exclusion criteria, analysis code, and explicit forbidden or strongly disfavoured results.
24. **Site methodology** — Add dependency propagation to the changelog workflow. When a foundational article such as the memory-channel hierarchy is materially downgraded, every dependent test, apex synthesis, positions entry, and falsification roadmap item should be automatically flagged for review.
25. **Site methodology** — Commission adversarial review from specialists in anaesthesia dynamics, cognitive-memory measurement, dynamical systems, and therapeutic ultrasound before presenting the design as experimentally ready. The current problem is not merely missing evidence; it is that the experiment’s defining signature is already generated by elementary physical dynamics.

## Verification Notes

Processed 2026-10-11 by the outer-review skill. **Extraction fidelity:** the reply was read from the turn's single `[data-markdown-text-style]` root inside `[data-turn-key]`. Readiness was `data-talvt-turn-state="complete"`, with no stop or cancel button. "Worked for 11m 27s". `[data-message-author-role]` still returns 0 elements. KaTeX was rendered from its `annotation[encoding="application/x-tex"]` source, giving 12 display and 19 inline formulas. The two tables and all 39 source links were kept. The body is 43,278 chars, and an FNV-1a hash of the reassembled text matched the in-page hash for all 49 chunks. The model selector shows "Thinking effort: Medium" after a reload. Yesterday's Sol Pro conversation shows the same, so the effort used tonight can't be confirmed from the DOM. The run time (11m 27s) is shorter than 2026-10-07's 21m 4s and 2026-10-10's 29m 51s.

**Verified claims (on disk):**

- ✓ **The core counterexample is correct, and no earlier review raised it.** Take τᵢ q̇ᵢ = p − qᵢ with fixed θᵢ. Up-crossings sit at θᵢ + rτᵢ and down-crossings at θᵢ − rτᵢ. For A (θ 0.40, τ 0.10) and B (θ 0.45, τ 0.20) at r = 1: A fails first (0.50 < 0.65) and recovers first (0.30 > 0.25 as p falls). The system is direction-blind with one threshold per channel, yet it shows the "clean reversal" that [direction-dependent-discriminating-test-design](/topics/direction-dependent-discriminating-test-design/) says substrate-symmetric production forbids. That claim appears in the description, L38 ("forbids its failure"), L46 ("**forbids** a clean reversal"), L50 ("It does, *for the substrate-symmetric reading*"), and L74 ("would remove the substrate-symmetric production reading"). L62's "matched rates" does not cancel unequal lags. A grep of the 22 earlier reviews that mention the article found no "time constant", "ramp rate", "quasi-static" or "lag" objection.
- ✓ **The Proekt & Hudson clause is an extrapolation.** L70 says the stochastic model is "direction-blind in its cross-channel ordering" and so "does not predict" a different recovery order. The 2018 abstract (PMC6200107) models awake and anaesthetised *states* (a ten-state Markov process, three awake and seven unconscious) and has no memory-channel variables. The paper is silent on channel order; it does not forbid a change in it.
- ✓ **Memory-channel recalibration was not propagated.** Commit `37fc8c1630` (2026-10-09) recast the ordering in [memory-channel-interface-evidence](/topics/memory-channel-interface-evidence/) as "a hypothesis with exceptions, not an established cross-condition finding". The design article was last modified 2026-10-04 and still calls autonoetic "A high-cost target channel" (L58) and uses that ranking in the Tenet 3 paragraph (L86). Memory-channel L122 concedes the cost ranking is circular: "Bandwidth and reconstruction cost are ranked partly by the very ordering they are then invoked to explain".
- ✓ **The probe caveat already exists elsewhere.** [targeted-lesion-discriminating-tests-between-production-and-filter-readings-of-the-memory-hierarchy](/topics/targeted-lesion-discriminating-tests-between-production-and-filter-readings-of-the-memory-hierarchy/) L52 says the Tulving-tradition probes "were not designed for tight cross-channel comparison under focal perturbation". The design article uses the same four probes (L60) without that caveat.
- ✓ **The filter reading forbids no ordering.** L38 and L48 say so. The self-concealment rule ([self-concealing-interface](/apex/self-concealing-interface/) L93, L147) requires a stake placed in advance and a P(E | Map) > P(E | best rival) that no single seam supplies. [filter-theory](/concepts/filter-theory/) L156 and L194 concede there are no independent criteria and that the filter reading is empirically equivalent to production.
- ✓ **The roadmap label is uncalibrated.** [falsification-roadmap-for-the-interface-model](/topics/falsification-roadmap-for-the-interface-model/) L201 reads "whose non-mirrored channel ordering substrate-symmetric production forbids".
- ✓ **The PCC caveats live only in the brain-stimulation article.** [brain-stimulation-and-the-witness-mode](/topics/brain-stimulation-and-the-witness-mode/) L49 records the Lord et al. (2024) active-versus-sham null. The design article (L56) cites the same work only as "sham-controlled pilot work" in which the modality reached its target.

**Found during verification (not raised by the reviewer):**

- ✓ **The apex contradicts the design article.** [self-concealing-interface](/apex/self-concealing-interface/) L141 (Prediction 1) says "the filter reading predicts a nonzero interaction" and that the autonoetic threshold crosses higher on the falling leg. The design article (L38, L48) and its 2026-09-27 stability note say the filter reading "permits a dissociation without predicting one". The 2026-09-27 propagation refine (`9ef0ee3e0e`) fixed the apex's failure-condition line (L127) but not L141; `git log -S` shows L141 untouched since `f92041ee58` (2026-07-16). L141 also says production predicts a zero interaction "because ordering is fixed by substrate state and not by trajectory". The lag model breaks that. L127 lists one of the apex's own failure conditions as "a single substrate-state mechanism that derives both the rising-trajectory and falling-trajectory orderings without per-case additions", and the lag model is a candidate for exactly that. It may also survive L147's cross-mechanism-invariance rescue. If channel time constants are channel-intrinsic, the sign of the interaction would recur across agents, so a production account need not expect it to dissolve. This last point is the verifier's inference, not a demonstrated result.
- ✓ **The same inference is upstream.** [direction-of-interface-change](/concepts/direction-of-interface-change/) L71 says the direction-blind profile "predicts symmetry". It treats hysteresis terms as paid per-case additions even though they have independent evidence (see Huang 2021 and Hu 2023 below). L81 says the simplest substrate "predicts … that recovery mirrors degradation". [mechanism-cost-ledger](/project/mechanism-cost-ledger/) L49 already names the general failure ("Asymmetric accounting"). Memory-channel L136 is already calibrated ("hysteresis is generic to bistable nonlinear systems").

**Verified claims (external, Europe PMC records and full text):**

- ✓ **Verhagen et al. 2019** (*eLife* 8:e40541, PMC6372282): the 40 s TUS protocol works "for more than one hour" offline. The full text says the effects were "sustained over the duration of our experiment, lasting up to 2 hr", so the article's "up to two hours" is correct. The reviewer's main point holds: this is lasting offline modulation, not a perturbation that can be ramped up and down within a session. A reopening phase would run in tissue still carrying the closing-phase effect.
- ✓ **Yaakub et al. 2023** (*Nat Commun*, PMID 37658076): human theta-burst TUS effects "last at least 50 mins", and the abstract raises "state- or location-dependency".
- ✓ **Kop et al. 2024** (*eLife* RP88762, PMID 39190585): four experiments, one preregistered, at three institutions. TUS motor inhibition "was driven by peripheral auditory stimulation, not direct neuromodulation".
- ✓ **Martin et al. 2024**, "ITRUSST consensus on standardised reporting for transcranial ultrasound stimulation" (*Brain Stimulation*, doi 10.1016/j.brs.2024.04.013): a reporting checklist that includes in situ exposure estimates. The design article cites none of the ITRUSST work.
- ✓ **Lord et al. 2024** (*Front Hum Neurosci* 18:1392199, full text): "a single model that contrasted active and sham groups found no significant effects". 11/15 active against 3/15 sham guessed "stimulation" (χ² p = 0.0356). The authors say "it is very possible that the precuneus was also affected". The reviewer's description is accurate.
- ✓ **Sepúlveda, Tapia & Monsalves 2019** (*Anaesthesia*, PMID 30835820): the abstract says the effect-site concentration at loss of consciousness "is usually higher" than at emergence. The article says "reliably higher" (L68); [direction-of-interface-change](/concepts/direction-of-interface-change/) L45 says "typically". Proekt & Hudson's abstract does say "consistently lower", so "reliably" has some support, but it is cited to the wrong source.
- ✓ **Huang et al. 2021**, "Asymmetric neural dynamics characterize loss and recovery of consciousness" (*NeuroImage*, PMID 33848623): in humans under propofol, recovery shows "abrupt restoration" of cortical autocorrelation and subcorticocortical connectivity, and "pharmacokinetic effects could not account for the difference". This is independent physical evidence of direction asymmetry, and none of the cluster cites it.
- ✓ **Hu et al. 2023** (*Nat Neurosci*, PMID 36973513): KCC2 degradation in the VPM is "an active process" independent of anaesthetic choice. [active-reboot](/concepts/active-reboot/) already cites it and says (L101) that it "does not show consciousness is non-physical".
- ✓ **Hudson et al. 2014** (*PNAS*, PMID 24927558): recovery passes through discrete metastable states and hubs "in an orderly fashion".
- ✓ **Wasilczuk et al. 2021** (*Front Syst Neurosci*, PMID 35095434): individual neural inertia in mice decreases with time, a direct test of the stochastic model.
- ✓ **Dunn 2008** (*Psychol Rev*, PMID 18426296): a state-trace analysis of 37 studies found "little or no evidence of bidimensionality" and concludes there is "insufficient evidence for the RK task to be used to identify qualitatively different memory components". This hits the design's remember/know probe hard.
- ✓ **Kim 2026** (*Cereb Cortex*, PMID 42061891): source memory shows familiarity-like, control-dependent neural patterns, not recollection-like ones.
- ✓ **Sant'Anna, Michaelian & Andonovski 2024** (*WIREs Cogn Sci*, PMID 37557099): distinguishes representational, metacognitive and epistemic accounts of autonoesis.
- ✓ **Daviddi et al. 2025** (*Neuropsychol Rev*, PMID 39653872): autobiographical retrieval is distributed across hippocampus, angular gyrus and posterior cingulate.

**Unverified claims:**

- ? The "later work" on separable VPM mechanisms (KCC2 plus EphB1/NR2B): the reviewer's link resolves only to Hu et al. 2023.
- ? Sepúlveda's review "emphasizes that human evidence is limited and not conclusive" and that estimates are distorted by poor equilibration: the abstract says neither, and the full text was not retrieved.
- ? JSTOR 48597071 (the remember/know review) was not resolved. Dunn 2008 carries the point on its own.
- ? ITRUSST *safety* and *dose* consensus papers: only the reporting paper was confirmed.

**Disputed or overstated:**

- ✗ §12 says [direction-of-interface-change](/concepts/direction-of-interface-change/) "more clearly acknowledges that hysteresis can arise from bistable physical circuits". L71 mentions "hysteresis terms for the bistable switch" only as a production *addition* paid per case, and L71 and L81 make the same "direction-blind ⇒ symmetric" inference as the design article. The concept page shares the defect; it is not a better-calibrated model to import.
- ✗ §6.2 lists things Cain et al. "does not establish" (monotonic dose response, rapid reversibility). The article claims only that the modality has "reached human subcortical targets in disorders-of-consciousness pilot work". The rebuttal answers a claim the article doesn't make. Low value.
- ~ §5/§11.1 calls the Tenet 1 statement "too strong". That is partly right. L84 opens "the design treats the interface reading as empirically exposed", but it ends by narrowing this to "one of the Map's evidence types". The opening clause still overclaims. L86's "the predicted direction effect is largest on the autonoetic channel" brings back a filter-side prediction that the 2026-09-27 stability note rules out.

**Not tasked:**

- Improvement 24 (dependency propagation on downgrade) repeats the open NEEDS-HUMAN methodology item in [workflow/todo.md](/workflow/todo/) ("a correction or confession that lands in one place and never binds anywhere else", 2026-08-03, six cycles so far). The 9 Oct memory-channel instance above is another case. That addendum belongs to `combine-outer-reviews`.
- Improvement 22 (symmetric complexity ledger) is already the "Asymmetric accounting" clause of [mechanism-cost-ledger](/project/mechanism-cost-ledger/) (L49). The failure is in applying it, so it is folded into the direction-of-interface-change task.
- Improvement 23 (prediction registry) and improvement 25 (specialist adversarial review) need tooling or human resourcing; they are noted, not queued. [self-concealing-interface](/apex/self-concealing-interface/) already carries three preregisterable predictions (L137–147).
- Improvement 1 (rename the article): a title change does not need a slug change. It is left to the evidential-status label-rule task below, which decides when "discriminating" may appear in a title.