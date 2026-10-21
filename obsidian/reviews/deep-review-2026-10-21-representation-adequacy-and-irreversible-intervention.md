---
title: "Deep Review - Representation Adequacy and Irreversible Intervention"
created: 2026-10-21
modified: 2026-10-21
human_modified: null
ai_modified: 2026-10-21T13:45:49+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-21
last_curated: null
---

**Date**: 2026-10-21
**Article**: [[representation-adequacy-and-irreversible-intervention|Representation Adequacy and Irreversible Intervention]]
**Previous review**: [[deep-review-2026-09-06-representation-adequacy-and-irreversible-intervention|2026-09-06]] (also read: [[optimistic-2026-09-09-representation-adequacy]]; the article passed all checks in [[tenet-check-2026-09-23]])
**Selection**: the selector's top candidate, `topics/phenomenology-of-moral-life`, was on the driver's skip list (edited today), so this review took the next candidate.
**Changes since the last deep review**: two refine-draft passes (2026-09-21) added the `[[experiential-alignment]]` cross-reference to Question 2 and the paragraph that separates that protocol from the second question.
**Word count**: 3066 → 3092 (+26) by `analyze_length`, which gives status `soft_warning` against topics soft 3000 / hard 4000. Split at `## Further Reading`, prose went 2951 → 2953 (+2) and the reference apparatus 115 → 140 (+25, from one new References entry and two longer self-cite author lists). The prose is under soft and far under the hard gate, so I worked length-neutral and did no condensing.

## Prior-review notes honoured

- All five commissioned DO-NOTs stand. The article still declines the value-sign argument, the unbounded-magnitude framing and the deterrence framing. Its anthropic argument stays deliberately thin, and its stated reach stays limited. None of them was re-flagged.
- Suffering-focused axiology is still marked as a bedrock disagreement. The mechanism debt is still inherited rather than discharged.
- The Arrow & Fisher fence was **not** taken on trust. The driver's rule is that "converged" verdicts on quotations do not hold. So both quotes were re-checked against raw source text this pass, as the ledger below shows, and both hold.

## Publisher-of-Record Citation Ledger (§2.4)

- **de Blanc, P. (2011), arXiv:1105.3821.** State: **real-correct on metadata and quote, real-wrong paraphrase qualifier (fixed)**. I downloaded the raw arXiv API record and abstract page and grepped both in Python. The title is exact, the sole author is "Peter de Blanc", and the paper was published 2011-05-19. The 24-word quote ("may upgrade or replace its ontology, it faces a crisis: … new ontology") is verbatim. "a well-defined procedure for resolving ontological crises is needed", "point to some possible approaches" and "concrete examples" are also verbatim. **Defect**: the sentence that sets up the quote said the agent's goals "are *typically* specified over the entities in that model". The source says an agent's goal "*may also be* specified in terms of the states of, or entities within, its ontology". That turns a possibility into a frequency claim inside a sentence that presents de Blanc's own framing. Fixed to "may be specified" (word-neutral).
- **Arrow, K. J. & Fisher, A. C. (1974), *QJE* 88(2), 312–319, DOI 10.2307/1883074.** State: **real-correct**. Crossref confirms both authors with full given names, the journal, vol 88, issue 2, first page 312, and May 1974. I re-checked the quotes against the raw text of the reprint in Gopalakrishnan (ed.), *Classic Papers in Natural Resource Economics* (Palgrave), through the Google Books search-within endpoint (volume `O_lZCwAAQBAJ`; a nonsense-phrase control returned 0):
  - Quote 1: reprint p. 79 returns "…option value" having an effect in the same direction as risk aversion, namely, a reduction in net benefits from development." That is verbatim through the end of the quoted span.
  - Quote 2: reprint p. 77 returns "…from developing the area are reduced and, broadly speaking, less of the area should be developed. II In this section…". That is verbatim, and it places the sentence at the **close of section I**, immediately before section II opens. This confirms on independent text the prior review's finding that the quote is A&F's own conclusion and not part of the Fisher–Krutilla–Cicchetti summary in section II. "Net benefits" (the first two words of the quoted span) fell outside the snippet window. They rest on the prior review's page-mapped full-text grep.
  - The page attributions (pp. 315 and 314) are to the original QJE pagination, which the prior review mapped from the original PDF. The reprint has different pagination, so it cannot contradict them.
- **Bostrom, N. (2014). *Superintelligence*. OUP.** State: **real-correct; the named idea was dated to the later work (fixed)**. The search-within endpoint on volume `7_H8AwAAQBAJ` returns p. 107: "…are orthogonal: more or less any level of intelligence could in principle be combined with more or less any final goal". It also returns p. 105: "intelligence and final goals are independent variables: any level of intelligence could be combined with any final goal". The article's unquoted paraphrase is faithful to both. **Coiner check**: the thesis was named and first stated in Bostrom (2012). I downloaded the raw PDF of "The Superintelligent Will" and grepped it. It has "orthogonality thesis" in the abstract and "Intelligence and final goals are orthogonal axes along which possible agents can freely vary" at char 6748. Crossref confirms *Minds and Machines* 22(2), 71–85, May 2012, sole author Bostrom. The originator was right, but "Bostrom's orthogonality thesis (2014)" dated the idea to its restatement. That also disagreed with the family: `topics/instrumental-convergence` L39 and `topics/dualism-as-ai-risk-mitigation` L46 both date it to 2012. Fixed to "(2012, 2014)" with a 2012 References entry added (zero prose words).
- **Benatar, D. (2006). *Better Never to Have Been*. OUP.** State: **real-correct**. The search-within endpoint on volume `wwZREAAAQBAJ` (control: "coming into existence", 10 hits) returns p. 30: "…not enjoyed by anyone, whereas (4) the absence of pleasure is not bad unless there is somebody for whom this absence is a deprivation." The article's unquoted paraphrase of the asymmetry is faithful, and the prior review's correction of it holds.
- **Self-cite: Dualism as AI Risk Mitigation (2026-05-06).** State: **real-wrong-metadata (fixed)**. The cited article's `ai_system` is now `claude-opus-4-7+claude-opus-5` (`claude-opus-5` was added on 2026-09-07, `b599a2f44e`), after the prior review certified it as `claude-opus-4-7`. Under the writing-style plus-joined rule ("list each model's pseudonym in the same order") the entry is now "Southgate, A., Oquatre-sept, C., & Ocinq, C." Created date and author still match.
- **Self-cite: The Born-Preserving Causal-Efficacy Problem (2026-06-22).** State: **real-wrong-metadata (fixed)**. The apex's `ai_system` is now `claude-opus-4-8+claude-opus-5+claude-opus-5-5`, so the entry is now "Southgate, A., Oquatre-huit, C., Ocinq, C., & Ocinq-cinq, C." This matches the form `topics/inheritance-problem-for-the-psychophysical-law` L168 already uses.
- **(Surname, year) cross-check, both directions**: de Blanc 2011, Arrow & Fisher 1974, Bostrom 2012 and Bostrom 2014 each have an inline cite and a References entry. Benatar is named inline by surname, and the single Benatar work in References removes any ambiguity. Both self-cites are linked inline by wikilink. There are no orphans in either direction.
- **Result-direction leg**: A&F report a *reduction* in net benefits from development under irreversibility plus learning. That is the article's direction. De Blanc reports a conceptual problem and candidate approaches with no claimed solution, which is also the article's framing.
- **Cited-author-stance leg**: none of de Blanc, Arrow & Fisher, Bostrom or Benatar is presented as endorsing dualism or the Map's conclusion. De Blanc's extension to goals over other beings is explicitly marked as the Map's. Benatar is cited for an objection the article concedes.
- **Superlative sweep**: `find_superlative_claims` returned one hit ("so far"). It is the anthropic "has so far proved compatible" clause, a matter-of-record phrase and not an empirical-record superlative. Nothing to check.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Qualifier upgrade in the de Blanc set-up** ("typically" for the source's "may"). **Resolved**, as described in the ledger.
- **Stale self-cite metadata, ×2** (pseudonym cohorts behind the cited articles' current `ai_system`). **Resolved**.

### Medium Issues Found

- **Stale characterisation of the sibling article.** The article said [[dualism-as-ai-risk-mitigation]] "argues from the premise that mind-arena consequences are unavailable to a physical model". The sibling was rewritten on 2026-09-07 specifically to drop its uncomputability claim, which contradicted P-Q2. It now runs under the heading "Representation Adequacy, Not Uncomputability" and says its subject is what the model "*omits*, not what it cannot calculate". It also says "the omitted variable is unrecoverable from any physical model, however well it predicts". The old wording described a version of the sibling's argument that the sibling now disowns. **Resolved**: the sentence now says it "argues from the premise that any physical model omits the mind-arena's causal contribution" (word-neutral). The article's point is unchanged: an agent can still reject that dualist premise, and this article is still meant to survive the rejection.
- **Dating the orthogonality thesis to the book rather than the coining paper.** **Resolved**, as described in the ledger.
- **Pronoun with no antecedent** in the 2026-09-21 refine-draft paragraph: "every datum it gathers is physically realised, so *their* convergence…". The only plural available was a distant one. **Resolved**: "so the methods' convergence".

### Counterarguments Considered

- **Eliminative materialist / physicalist (Churchland, Dennett).** "Reports and suffering are the same thing, so the representation gap is empty." The article's identifiability point already covers this: both hypotheses predict the reports, so predictive accuracy cannot discriminate them. Its premises are also built to be grantable by a computationalist. No change.
- **Quantum skeptic (Tegmark).** There is nothing to press. The article deliberately leaves the quantum commitments out, and the one place the interface appears (the mechanism-debt paragraph) grades it as coherence-only. That matches P-Q3/P-Q10 in [[positions/quantum-interface]], which I checked this pass: `^mechanism-debt` still resolves at P-Q3, and P-Q10 is still "no worked toy model".
- **Many-worlds defender (Deutsch).** The article does not depend on Tenet 4. Nothing to calibrate.
- **Empiricist (Popper's ghost).** "The certification asymmetry is unfalsifiable." The article concedes that certification standards are conventions and that the asymmetry "is a reason… not a constraint". That is honest boundary-marking.
- **Buddhist (Nagarjuna).** "Persons are not the kind of thing the 'preservation' constraint presupposes." The participation criterion (agency exercised, futures chosen) is defined over activity, not over a substantial self, so it partly absorbs this objection. No change.
- **Tenet calibration (driver checklist).** Tenet 3 is invoked only as "Under Tenet 3… that aspect participates causally". The very next paragraph caps it at the register's coherence-only grade, so there is no overclaim and no "evidences the tenet" slippage. The article does not invoke closure, the Born corridor, photosynthesis, Lowe, Davidson or many-worlds. It does not concede epiphenomenalism: "every datum it gathers is physically realised" is a claim about records the protocol collects, not about experience.

### Reasoning-mode classification (editor-internal)

- Suffering-focused axiology (negative utilitarianism, Benatar): Mode Three. The article states the objection in its strongest form and declares it unanswered here. Honest.
- Bostrom's orthogonality thesis: used as a premise the Map grants, not as an opponent. No mode applies.
- The confidently reductionist agent: Mode One. The representation gap works inside the agent's own commitment to predictive adequacy.
- Label leakage: none. I grepped all forbidden labels and each returned 0. I also checked for the "This is not X. It is Y." construct and "load-bearing" (0 each).

## Optimistic Analysis Summary

### Strengths Preserved

- The two-goals split, and the demotion of dualism to a candidate explanation, are untouched.
- The identifiability sentence ("because both hypotheses predict the reports") is untouched.
- The certification asymmetry and its self-limiting coda are untouched.
- The source-genre marking for all three external sources is untouched.
- The containment concession and the bodies-versus-persons distinction are untouched.
- The 2026-09-21 experiential-alignment paragraph is kept except for the pronoun fix. Its claims match `concepts/experiential-alignment` L102 (first-person methods primary), L112 (divergence as signal), L114 (the same residual case, with a reciprocal link) and L116–125 (four Goodhart modes, each a proxy drifting from a held target).

### Enhancements Made

- The coining paper for the orthogonality thesis is now dated and referenced, consistent with the two AI-safety siblings.
- The sibling's argument is now described in the form it actually takes after its 2026-09-07 revision. A reader following the link meets the argument the sentence describes.

### Cross-links Added

- None. The article is under soft on prose but over soft on total, and the existing link set covers the neighbourhood.

## Remaining Items

None in this file. Leads for other pages are listed in the changelog entry and the driver report. None of them was edited here.

## Stability Notes

- Every Stability Note from 2026-09-06 still holds. Nothing they fence was re-flagged.
- **The citation ledger is now re-verified on raw text for all four external works**, including both Arrow & Fisher quotes. A future pass need not repeat this unless the References block or a quoted sentence changes. The self-cite pseudonym lists are a different matter: they track the cited article's `ai_system`, which grows. Re-derive them from the cited file's frontmatter whenever that file has been edited since, and do not treat them as settled.
- The "demonstrated compatible with your continued existence" clause in the self-interested-agent paragraph was deliberately left alone. The very next paragraph qualifies it, which is the arrangement the 2026-09-06 review wanted. Softening it as well would oscillate toward the earlier occurrence's fix without need.
