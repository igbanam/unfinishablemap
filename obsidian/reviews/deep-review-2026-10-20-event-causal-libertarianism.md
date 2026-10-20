---
title: "Deep Review - Event-Causal Libertarianism and the Taxonomy of Libertarian Free Will (2026-10-20)"
created: 2026-10-20
modified: 2026-10-20
human_modified:
ai_modified: 2026-10-20T14:17:08+00:00
draft: false
topics:
  - "[[free-will]]"
concepts:
  - "[[agent-causation]]"
  - "[[source-versus-leeway-incompatibilism]]"
  - "[[quantum-indeterminacy-free-will]]"
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-20
last_curated:
---

**Date**: 2026-10-20
**Article**: [[event-causal-libertarianism|Event-Causal Libertarianism and the Taxonomy of Libertarian Free Will]]
**Previous review**: [[deep-review-2026-08-19-event-causal-libertarianism|2026-08-19]] (and [[deep-review-2026-07-09-event-causal-libertarianism|2026-07-09]])
**Mode**: Third deep review. Selected by `deep_review.py next` (score 76; the body had changed since 08-19 through the 10-14 refine-draft `d6689c7f2b`, which rewrote the Tenet 3 and Tenet 5 paragraphs). Lens: taxonomy *placement* fidelity, meaning whether each named theorist sits in the wing the canonising source puts them in, checked against the raw SEP text (curl, then grep) and two reviews of Lowe 2008 (raw text). Also covers the open P3 calibration item at L80 from [[optimistic-2026-10-19-incompatibilism-repair-wing]].

## Verdict

**PASS after two critical fixes and five medium ones.** Word count 2581 → 2818 (topics soft 3000, hard 4000). The 10-14 Tenet 3 and Tenet 5 repairs hold, and the fence "Tenet 5 reaches only the parsimony strand" is honoured. This pass found what the two earlier citation passes could not see: one theorist was filed in the wrong wing, and one sentence claimed for the Map's own wing more than the literature or the Map's own register allows.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Lowe misfiled as an agent-causal libertarian (attribution error).** L64 listed "E.J. Lowe" among agent-causal libertarians and called his non-Cartesian substance dualism "a substance-dualist version" of agent-causal libertarianism. The article's own canonising source files Lowe with the **non-causal** theories. SEP §1 (raw text): "Other accounts of this type are advanced by Stewart Goetz …, E. J. Lowe (2008: chs. 6–9 and 2013), …". Two reviews of *Personal Agency* say the same thing in raw text. Griffith, *NDPR* 2009.06.15: "Lowe's view is somewhere in between the latter two [agent-causal, noncausal]. Like some noncausalists, Lowe posits uncaused volitions … Like agent causalists, Lowe argues in favor of substance causation", and "Lowe distances himself from agent causalism by asserting that agents do not cause actions. Instead, free actions are completely uncaused acts of will." *Philosophy in Review* XXX(4) 2010: "Surprisingly, Lowe does not endorse an agent-causal theory of free action … Neither an agent nor an event is the cause of any choice … a spontaneous power … (150) … a rational power because it is a power that is exercised in light of reason (155)." **Fixed**: Lowe is removed from the agent-causal list and its sentence. One sentence in the non-causal section now places him on that wing's border with the agent-causal one: he defends substance causation and a non-Cartesian substance dualism, holds that free volitions are uncaused, spontaneous exercises of a rational power, and SEP files his account with the non-causal theories. Lowe stays at L80 as a defender of fundamental substance causation, which is correct (SEP §3.3: "Lowe 2008: 143–46").
- **"agent-causal views defeat luck" (calibration error, possibility/probability slippage in the Map's favour).** L80's symmetry sentence said agent-causal views *defeat* luck. SEP §3.2 "Luck, Again" (raw text): "While the appeal to agent causation might be thought to solve the problem of luck, the objection has been raised that in fact it does not help at all (Haji 2004; Mele 2005 and 2006: ch. 3; van Inwagen 1983: 145 and 2000)." The Map's own register is narrower too: [[free-will]] L94 and [[consciousness-and-agency]] L115 say agent causation settles *who* decides, not *why* the choice went one way, and leave "a primitive whose modal structure is owed rather than supplied". A reviewer who accepts the tenets would still flag "defeat". **Fixed**: the symmetry is kept, and only the agent-causal half is narrowed. Agent-causal views now "answer its disappearing-agent form". The rollback form is "pressed against them too (van Inwagen 2000; Mele 2006)". Then come the agent-causalist reply (the difference is "the agent's exercising her free will differently", as in SEP §3.2) and the Map's owed primitive, linked to [[free-will]]. The section's opening sentence is scoped to match ("answers the disappearing agent"). This discharges the open P3 in `workflow/todo.md` ("L80 says 'agent-causal views defeat luck'"), including its optional Franklin item.

### Medium Issues Found

- **Dropped qualifier at L42.** "These accounts differ from event-causal compatibilist accounts only by adding that the relevant causation is indeterministic". SEP §2 says this of "The simplest event-causal incompatibilist theory", and Kane's account, the article's centrepiece, adds a good deal more. **Fixed**: "The simplest such account differs from a good event-causal compatibilist account only by adding …".
- **Unverifiable concession attributed to Clarke and Mele (L76).** "Critics (Clarke, Mele) grant that this shows the outcome is *voluntary* either way". No source was found for the *grant*. SEP's own text casts doubt on the rationality of trying to make two incompatible choices at once. SEP gives the Clarke/Mele reply to the active-effort move as: "what is needed is an account of the freedom with which the agent acts in making these efforts of will (Clarke 2002, 2003a, and 2003b: 89–92; Mele 2006: 51–52)". Haji and Mele add that the luck argument works without exact sameness. **Fixed** to the sourced content: an effort makes the choice free only if the effort is itself free, which the model leaves unexplained, and a choice voluntary either way still leaves *which* way unsettled.
- **Causal pluralism given one-sidedly (L80).** The article said "on which events cause things only as changes *in* substances". That is half of SEP §3.3's interdependence clause, and it reads like substance-causation monism. SEP: "events cause things only when the substances in which these events are changes cause those things, and substances cause things only when changes in those substances cause those things. The pluralist picture is not one of competition but of interdependence." **Fixed**: "equally fundamental and interdependent, so that a change in the agent can accompany her causing without competing with it". This also answers the section's own "if there is a triggering event, event-causation is back" worry in the pluralist's terms.
- **Interface answer to the intelligibility objection over-scoped (L88).** The article said the interface gives "a candidate answer to the intelligibility objection … it says where substance causation touches physics". The objection, as L80 states it, asks whether a substance can be a cause at all, and how it can be one at a particular time. Saying where answers neither question. **Fixed**: "part of an answer … though whether a substance can be a cause at all still rests on the substance-causation defences above, and the location is itself a hypothesis, not a proof." This makes the Map more exposed, not less.
- **Ginet's actish quality grounded the wrong thing (L68).** The article said "Freedom is a basic, uncaused feature of action. Ginet grounds it in …", with "it" read as freedom. SEP §1 says the actish quality characterises each *basic action* and bears on its activeness ("Might the actish feel of some occurrence itself constitute that event's activeness, the agent's exercise of active control?"). **Fixed**: "Ginet (1990) locates an action's activeness in an 'actish phenomenal quality' … that she is *directly* making the action happen" (SEP: "directly making happen").

### Low Issues Found (fixed)

- L46: bold removed from "torn decisions". "Torn decisions" is Balaguer's term of art, which L56 rightly calls "His"; Kane's 2012 reply to Balaguer is titled "Torn decisions, luck, and libertarian free will: comments on Balaguer…" (Crossref 10.1007/s11098-012-9896-5). In Kane's paragraph, bolding it implied Kane coined it. Kane's own term, "self-forming actions", stays bold.
- L48: "Most actions flow deterministically from a character …" → "Many free actions may flow deterministically …". Kane's claim is permissive (SEP §2.2: an agent "can be ultimately responsible for a decision that is causally determined by her possessing certain character traits"), not a frequency claim.
- L72: the rollback is now attributed to van Inwagen (2000), which also anchors the new L80 citation.
- L84: Franklin's (2011) rebuttal of four formulations of the luck argument has been added to the list of live event-causal replies. Franklin is already named as a proponent at L42. This balances the stronger L80.
- L64: "Roderick Chisholm and Timothy O'Connor, with Randolph Clarke …" (grammar after the Lowe removal).

### Publisher-of-Record Citation Ledger

Earlier ledgers (07-09 metadata, 08-19 reading fidelity) cover the unchanged entries. This pass re-read the SEP entry for *placement* and verified each new entry at Crossref, with abstracts from OpenAlex.

- Clarke, Capes & Swenson, SEP "Incompatibilist (Nondeterministic) Theories of Free Will" — **real-correct** (raw HTML, "substantive revision Wed Aug 18, 2021"). Placement and reading checks this pass:
  - Lowe in §1 non-causal: the article misfiled him, **fixed**.
  - "simplest" theory in §2: the qualifier had been dropped, **fixed**.
  - §3.2 luck against agent causation: overstated, **fixed**.
  - §3.3 pluralism: one-sided, **fixed**.
  - The Clarke/Mele effort-freedom reply in §2.2: replaced the unsourced "grant", **fixed**.
  - Ginet actish quality and its brain-stimulation case (§1): scope **fixed**.
  - Kane label rejection (§2.2): correct, unchanged.
- Lowe, E. J. (2008). *Personal Agency: The Metaphysics of Mind and Action*. OUP. DOI 10.1093/acprof:oso/9780199217144.001.0001 — **real-correct, newly added** (Crossref: title, author, OUP 2008, ISBN 9780199217144). Reading verified against raw text of Griffith's *NDPR* review and the *Philosophy in Review* 2010 review (quotes above). Lowe's stance: substance dualist (non-Cartesian), defender of substance causation, non-causal about free volition. He is not presented as endorsing the Map's agent-causal reading.
- van Inwagen, P. (2000). "Free Will Remains a Mystery." *Philosophical Perspectives* 14, 1–19. DOI 10.1111/0029-4624.34.s14.1 — **real-correct, newly added**. Crossref gives the container as *Noûs* 34 s14 (the *Philosophical Perspectives* supplement) and pages 1–19. SEP cites it as *Phil. Perspectives* 14: 1–19, and the conventional form is kept. Result direction: the replay argument is extended to agent causation, and agent causation "does not help". Sources: SEP §3.2; Speaks's lecture notes on the paper (raw PDF: "he suggests that adding in agent causation to the picture does not block the argument"); Griffith 2005, "Does Free Will Remain a Mystery? A Response to Van Inwagen", which replies to exactly this claim. Van Inwagen's stance: incompatibilist who believes in free will and holds it a mystery. He is not presented as supporting the Map.
- Mele, A. R. (2006). *Free Will and Luck*. OUP. DOI 10.1093/0195305043.001.0001 — **real-correct, newly added** (Crossref). Chapter 3, "Libertarianism, Luck, and Control", pp. 49–80, DOI …003.0003. Its OpenAlex abstract: it examines "Randolph Clarke, Robert Kane, and Timothy O'Connor … libertarians (agent causationists and others)" and argues "present luck … poses an as yet unresolved problem for libertarianism". Result direction: luck is pressed against agent-causationists too, which matches the article. Mele's stance: agnostic, not a libertarian.
- Franklin, C. E. (2011). "Farewell to the Luck (and *Mind*) Argument." *Philosophical Studies* 156(2), 199–230. DOI 10.1007/s11098-010-9583-3 — **real-correct, newly added**. Crossref puts it online in 2010 and in issue 156(2); SEP dates it 2011b. OpenAlex abstract: "I then consider four formulations of the luck argument and find them all wanting." Franklin's stance: event-causal libertarian, cited for the rival wing's reply.
- Ginet, C. (1990). *On Action*. CUP. DOI 10.1017/CBO9781139173780 — **real-correct, newly added** (Crossref; SEP bibliography). The quoted phrase "actish phenomenal quality" was confirmed as Ginet's own wording through the OpenAlex full-text index of Ginet 1997 ("Freedom, Responsibility, and Agency"). Its page in the 1990 book was **not** grep-verified (the archive.org copy is restricted). SEP §1 attributes the view to Ginet and cites 1990: 9 for the brain-stimulation case.
- All other entries (Kane 1996; Kane ed. 2002; Ekstrom 2000, 2019; Balaguer 2010; O'Connor 2000; Jacobs & O'Connor 2013; Chisholm 1964; Clarke 2003; Pereboom 2014; the three Map self-citations, whose created dates were checked as 2026-01-15, 2026-01-18 and 2026-07-09) — **real-correct** per the 07-09 and 08-19 ledgers. The text citing them is unchanged.

Inline ↔ References: every new inline year-cite (Ginet 1990, Lowe 2008, van Inwagen 2000, Mele 2006, Franklin 2011) has an entry, and every new entry is cited inline. The name-only mentions without years (Clarke, Mele at L76; McCann, Goetz) are unchanged from prior passes. Mele now also has an entry. No superlative or empirical-record claims (currency sweep N/A).

### Reasoning-Mode Classification (editor-internal)

- **Pereboom** (disappearing agent; parsimony strand; wild coincidences): Mode Three, honestly declared. The 10-14 repair is correct and unchanged.
- **Event-causal wing** (Kane, Ekstrom, Balaguer, Franklin): Mode Three, "framework-relative judgement rather than a demonstration". Adding Franklin to the live replies strengthens the honesty of this.
- **Luck pressed against the Map's own wing** (van Inwagen, Mele): newly engaged. Mode Three by concession: the Map does not claim to refute the rollback against agent causation, and names its reply as an owed primitive. No label leakage.

### Calibration Check

- **Before**: one slippage in the Map's favour ("defeat luck") and one over-scope (the interface "answer" to intelligibility). Both are fixed in the direction of more exposure.
- **After**: PASS. No tier upgrades anywhere.

## Optimistic Analysis Summary

### Strengths Preserved

- The structural symmetry "each wing buys an answer to one objection at the cost of exposure to another" ([[optimistic-2026-08-22-rival-route-wing]]). It is kept, and now holds more honestly, because the agent-causal half names its residual exposure.
- The 10-14 Tenet 5 split (luck is not a parsimony point; the wild-coincidences argument stays open), and the Tenet 3 concession that the tenet alone does not exclude the event-causal wing.
- Division of labour with [[agent-causation]], [[quantum-indeterminacy-free-will]] and [[free-will]]. The new L80 sentence links to the free-will hub rather than re-deriving its reply.

### Enhancements Made

- Lowe placed at the non-causal/agent-causal border. This is more accurate, and also more useful to the Map, because the volitionist structure the Map borrows from Lowe ([[philosophy-of-action-under-dualism]]) is exactly what makes him a border case.
- The luck objection now appears as the article's pivot in both directions: against the event-causal wing (disappearing agent), and against the Map's own wing (rollback).

### Cross-links Added

- [[free-will]] (L80, on the owed primitive). No sentences were installed in other articles.

## Remaining Items

None for this article. Leads for other files were reported to the driver and not edited here.

## Stability Notes

- Fences from 08-19 are still in force: event-causal libertarians and Pereboom reject the Map's luck reading from outside the tenets, and this must not be re-flagged.
- New fence: **Lowe is a border case** (substance causation + uncaused volitions; SEP files him non-causal). A future pass must not move him back into the agent-causal list without a primary-text reason.
- New fence: **agent-causal views answer the disappearing-agent form only.** The rollback form is pressed against them (van Inwagen 2000; Mele 2006), and the Map's reply is an owed primitive. Do not re-widen to "defeat" or "solve".
- New fence: **the interface answers *where*, not *whether*,** a substance can cause. Do not re-widen L88.
- Three reviews now. The article should be treated as converged unless its body is substantively modified or an outer review raises something new.
