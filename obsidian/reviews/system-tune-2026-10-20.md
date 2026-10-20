---
title: "System Tuning Report - 2026-10-20"
created: 2026-10-20
modified: 2026-10-20
human_modified: null
ai_modified: 2026-10-20T06:15:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-20
last_curated: null
---

# System Tuning Report

**Date**: 2026-10-20
**Sessions analyzed**: the /loop run from 2026-10-19 07:23Z to 2026-10-20 06:07Z (session_count 22,916 → 22,996; ~80 cycle posts), after a 68-hour outage (2026-10-16 11:47Z → 2026-10-19 07:23Z) during which no loop was running
**Period covered**: 2026-10-14 (last tune) → 2026-10-20

## Executive Summary

The loop is healthy: `failed_tasks` is empty, there are no critical issues, and the only failure in the last 20 tasks is the driver's deliberate abandonment of a stalled Gemini review. This is the **twenty-first consecutive run with no Tier 1 change possible**: `cadences`, `overdue_thresholds`, `locked_settings` and replenishment weights are still absent from `evolution-state.yaml`. The new findings are all scheduling and pipeline gaps that needed driver intervention to get the 2026-10-20 outer-review cycle completed inside the Chrome window, and they are code- or skill-level, so they appear below as Tier 3 items.

## Metrics Overview

| Metric | Current | Previous (10-14) | Trend |
|--------|---------|----------|-------|
| failed_tasks | 0 | 0 | → |
| Recent-task failures (last 20) | 1 (driver abandon of stalled Gemini) | 1 (Gemini commission) | → |
| Critical / medium / low issues | 0 / 10 / 3 | 0 / 10 / 3 | → |
| topics / concepts / voids | 350/370, 361/370, 113/125 | — | +3 new articles + 1 concept on 10-19/20 |
| Outer-review cycles completed | 10-20 (2 of 3 collected, synthesis written) | 10-16 | resumed after a 3-day outage |
| Consecutive zero-Tier-1 tune runs | 21 | 20 | ↑ |

## Findings

### Cadence Analysis

- **The 30-day tune-system gate is still not enforced on the /loop path** (carried from 10-14). This run fired 6 days after the last one, via the every-6-cycles cycle trigger. Evidence: the last eight `no_change_runs` dates (09-27, 09-30, 10-03, 10-07, 10-10, 10-14, and now 10-20) are 3–7 days apart.
- **Outage, not cadence:** the 68-hour gap (10-16 11:47Z → 10-19 07:23Z) had no loop process running at all (the log has no entries for 10-17 and 10-18). As a result, the outer-review legs for 10-17, 10-18 and 10-19 were never commissioned. Commission triggers fire once per UTC day, so missed days are never caught up.

### Failure Pattern Analysis

- **Gemini Deep Research stall (new):** the 10-20 04:11Z Gemini commission stalled at "Starting research..." with page text byte-identical at 04:50, 04:52 and 05:07Z. The 4-hour abandon cutoff (08:11Z) falls after the Chrome window closes to new tasks at 07:00Z, so no in-window collect could have abandoned it, and `/combine-outer-reviews` would have stayed blocked. The driver ran `mark_abandoned` at 05:08Z. One occurrence so far, below the 3-occurrence threshold for a pattern, but the window/cutoff mismatch is structural.
- **The Claude weekly Fable limit is now handled in-skill:** the Opus fallback (Step 2.5, added 10-19) worked on its first live run at 03:10Z.

### Queue Health Analysis

- **P3 rows do get executed now (partially corrects the 10-14 finding).** On 10-19/20 the loop executed at least six P3 tasks from the queue:
  - the direction-of-interface-change, Tulving-attribution, vulnerability-ordering-dependents, O'Connor–Wong and memory-channel calibrations;
  - the dissociative-subtype expand-topic.

  The 10-14 "0 P3 headers removed" measurement reflected that window, not a hard rule.
- **Research → expand chain:** the deterministic chain (commit 7f0fc32b41, 10-19) fired correctly for queue research-topic notes:
  - logic-of-dissociation-inference → `article` → minted → written → cross-reviewed, all on 10-19;
  - Hesse → `refine` → nothing minted, as intended.

  It does **not** run for `research-voids` output (`tools/evolution/cycle_post.py` L402 gates on `kind == "queue" and skill == "research-topic"`). The 10-20 drift-void note declared `recommended_action: article` and was routed by hand to the voids-slot NEEDS-HUMAN.
- **Driver-minted follow-ups:** most new tasks on 10-19/20 came from fork side-findings that the driver minted by hand: cross-reviews after expand-topic, propagation tasks, check-tenets priorities, condense for an over-length page. This is the "sanctioned channel for fork-discovered follow-ups" gap carried from 10-10, still operating by hand.

### Review Finding Patterns

- **Corrections stay local.** Five or more distinct reviews on 10-19/20 found that a fix on one page had not reached the pages that copy or depend on it:
  - the Carter 2005 overstatement on 3 pages;
  - the choice-blindness pupillometry misreading on 4 pages, traced to a research note;
  - the co-optimization rewrite not reaching `bidirectional-interaction`;
  - the acquaintance narrowing not reaching `self-stultification-as-master-argument`;
  - the vulnerability-ordering calibration's dependents.

  Check 152 (tenet-check-2026-10-20) made "the window's best pages did not reach their dependents" its main finding. The 2026-10-20 outer-review synthesis (cluster 3) independently named the same gap: no canonical owner for constants and definitions.
- **Metadata-only reviews miss content errors.** Deep reviews that checked findings against primary texts, not just citation metadata, found reversed or invented empirical claims on pages that earlier reviews had passed:
  - Rochat's newborn self-touch result stated backwards;
  - a nonexistent "2015–2024 replication series" (pupillometry);
  - Valentini's framing reversed;
  - O'Connor & Wong's view misplaced.

### Convergence Progress

Content is growing within the caps (topics 350/370, concepts 361/370, voids 113/125). Three new articles were written and cross-reviewed on 10-19/20, and one concept on 10-20. The positions register (P-MC1) is behind the 10-19 acquaintance narrowing, and its file is 822 words over threshold (tenet-check 152, Note 2).

## Changes Applied (Tier 1)

*No changes applied.* There are still no `cadences`, `overdue_thresholds`, `locked_settings` or replenishment-weight keys in `evolution-state.yaml` for Tier 1 to act on (21st consecutive run).

## Recommendations (Tier 2)

### Mint check-tenets priority-list items at P2 by default (carried from 10-10; applied by hand on 10-20)
- **Proposed change**: when check-tenets writes a "What to Fix First" list, mint each item as a P2 refine-draft automatically.
- **Rationale**: reports-only items reach the queue only if a driver mints them. On 10-20 the driver did this by hand for check 152's top 4, folding one into an existing P3 and promoting it.
- **Risk**: Low.
- **To approve**: add a minting step to check-tenets, or a cycle_post hook that reads the report's top-4 list.

## Items for Human Review (Tier 3)

### Let due Chrome triggers pre-empt pending cycle triggers inside the automation window (new, verified in code)
- **Issue observed**: `tools/evolution/cycle_pick.py` drains `.unfin/pending-triggers.json` (step 2) before wall-clock triggers (step 3). On 10-20, check-links, research-voids and check-tenets queued ahead of the 02:00 ChatGPT commission, and the commissions and collects only finished in-window because the driver ran them out of order by hand.
- **Why human needed**: scheduling code change.
- **Suggested action**: within 00:00–06:59Z, evaluate commission/collect/combine triggers before pending cycle triggers, or defer long cycle triggers (check-tenets, tune-system, research-voids) until after 07:00.

### Clamp the outer-review abandon cutoff to the Chrome window (new)
- **Issue observed**: Gemini's 4-hour cutoff (08:11Z) fell after the window closed to new tasks. A stalled review would block `/combine-outer-reviews` until the next night.
- **Suggested action**: either a stall heuristic (for example, page text unchanged across two collect attempts 15+ minutes apart while still at "Starting research...") or a cutoff of `min(commissioned + 4h, window_end)`.

### Run the research → expand chain for research-voids notes (new, verified in code)
- **Issue observed**: `cycle_post.py` L402 gates the chain on queue research-topic, so voids notes declaring `recommended_action: article` are never minted. Their `pending_articles` entries are never read.
- **Suggested action**: extend the chain to `research-voids`, honouring section caps and the voids-slot NEEDS-HUMAN decision.

### Agentic-social selector keeps picking just-expired repeats (new)
- **Issue observed**: on 10-19/20 the eligible pool shrank from 28 to 12, and the selector picked exact ~7-day repeats several times with pools of 14–21. `consistent-histories-interpretation` was picked 3×, and the Neoplatonist page 2×. Forks overrode each pick, using up about 6 never-posted articles. About 32 never-posted articles remain.
- **Suggested action**: penalise URLs that left the 7-day window within the last 24–48 hours, or fall back to the URL-only pool when the main pool's top pick is a repeat.

### Account-wide Claude weekly limit (new, flag only)
- **Issue observed**: the Opus fallback works, but claude.ai showed the account-wide weekly limit at 75% used on 10-20. This 24/7 loop's own Claude Code usage draws on the same allowance, so the Claude review leg can still go dark later in the week.
- **Suggested action**: an operator decision, either usage credits or reduced loop cadence near the reset.

### Stale skill text (new, report only)
- **Gemini model**: `collect-gemini-review` and `tools/reviews/services.py` still hard-code `gemini-2-5-pro`; the model is 3.1 Pro. Gemini also now shows a "Thinking level" control, set to Low. Decide whether commissions should set High.
- **Claude menu**: claude.ai's `+` menu no longer has a "Web search" entry, which the commission skill's "Web search on by default" line assumes.
- **ChatGPT DOM**: the selectors changed in 2026-10, and the skills still describe the old DOM. Every brief has to supply the fallbacks.

### Carried, still open
- Wire the tune-system min-age gate into the /loop pick path (10-14).
- Forward all task fields to forks (10-03). On 10-19/20 the driver had to enrich thin `cycle_pick` args by hand for every expand-topic and cross-review.
- Sync inside `cycle_post` when `obsidian/` changed (10-10).
- Correct the Section Caps table and gating-function path in CLAUDE.md (10-14). The caps are now 370/370/125 and the gate is `tools.evolution.state.count_section_files`.
- check-links should read `_redirects` (10-10). The 10-20 run again found 376 of 424 raw 404s were redirect-covered.

## Next Tuning Session

- **Recommended**: 2026-11-19 (30 days out). The cycle trigger will fire sooner unless the min-age gate is wired.
- **Focus areas**:
  - whether the window-ordering fix lands;
  - Gemini stall recurrence;
  - the account-wide Claude limit;
  - the agentic-social never-posted stock (~32).
