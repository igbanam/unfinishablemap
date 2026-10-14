---
title: "System Tuning Report - 2026-10-14"
created: 2026-10-14
modified: 2026-10-14
human_modified: null
ai_modified: 2026-10-14T09:21:29+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-fable-5-1
ai_generated_date: 2026-10-14
last_curated: null
---

# System Tuning Report

**Date**: 2026-10-14
**Sessions analyzed**: 255 loop posts (`cycle_post done` lines in `../unfinishablemap_log/evolve_loop.log` after 2026-10-10 15:21 UTC)
**Period covered**: 2026-10-10 15:21 → 2026-10-14 09:21 UTC (3.75 days)

## Executive Summary

The loop is healthy: 254 of 255 posts succeeded, `failed_tasks` is empty, there are no critical issues, and the one failure was a Chrome-driven Gemini commission. This is the **twentieth consecutive run with no Tier 1 change**, because the four Tier 1 levers (`cadences`, `overdue_thresholds`, `locked_settings`, replenishment weights) are still absent from `evolution-state.yaml` (re-checked with grep). Two things moved this window: the operator raised all four section caps on 2026-10-12, and the coalesce abandon streak ended with two merges on 2026-10-11. Two things did not: P3 tasks are still never executed (0 of 52 P3 rows closed in the window while the P3 count rose to 103), and the root cause of tune-system's 3–4 day cadence is now located in code: the min-age gate exists but is wired only into the Python orchestrator, not the `/loop` pick path.

## Metrics Overview

| Metric | Current | Previous (10-10) | Trend |
|--------|---------|------------------|-------|
| Loop posts in window | 255 (3.75 d) | 245 (3.5 d) | → (~68/day) |
| Post status | 254 SUCCESS / 1 FAILURE | 241 / 4 | ↓ failures (one Gemini commission) |
| `failed_tasks` | {} | {} | → |
| Kind mix | queue 102 · trigger 50 · cycle 42 · social 37 · collect 12 · commission 9 · combine 3 | queue 102 · trigger 46 · cycle 42 · social 36 · commission 10 · collect 6 · combine 3 | → (queue share 40%) |
| Quality | critical 0 · medium 10 · low 3 | critical 0 · medium 10 · low 3 | → |
| Sections (`count_section_files`) | topics 347/370 · concepts 357/370 · voids 112/125 · positions 23/90 | 343/360 · 349/360 · 113/115 · 23/80 | caps +10 each (operator, 10-12); voids freed 1 by coalesce |
| Active tasks (parse_tasks) | 138: P1 1 · P2 34 (26 pending, 8 blocked) · P3 103 (95 pending, 8 blocked) | 73: P2 21 · P3 52 | ↑ P3 doubled |
| Todo churn (git, window) | P2 rows removed 96, added 108; P3 rows removed **0**, added 51; ✓ entries added 103 | — | P3 execution rate 0 |
| `task_chains.pending_articles` | 13 | 12 | ↑ (stalled, replenish idle since 09-29) |
| Coalesce | 2 merges (10-11), then 4 abandons | ≈42 consecutive abandons | streak ended |
| Driver hand-commits | 9 `auto(todo)` · 6 `auto(sync)` · 2 `fix(...)` · 1 `auto(state)` of 277 | 4 in one session; 15 of 273 | → |
| tune-system interval | 3.75 d (30-day cadence) | 3.5 d | gate inert (cause located, below) |

## Findings

### Cadence Analysis

- **No cadence configuration exists to tune.** `cadences:`, `overdue_thresholds:`, `locked_settings:` and any replenishment weight key are absent from `evolution-state.yaml` (grep-verified this run). Cadence lives in code (`tools/evolution/cycle.py`, `time_trigger.py`).
- **tune-system fired 3.75 days after the previous run, and the cause is now specific.** `tools/evolution/cycle.py` defines `TRIGGER_MIN_AGE_HOURS = {"tune-system": 30 * 24}` and `filter_triggers_by_min_age()`, with a comment saying the gate was added precisely because tune-system "was running daily (9 reports in 9 days)". The only caller is `scripts/evolve_loop.py:1370`. `tools/evolution/cycle_pick.py` and `cycle_post.py` never call it, so on the `/loop` path the every-6-cycles trigger fires ungated. Twenty runs at 3–4.3-day intervals follow from this one omission. Carried to Tier 3 with the exact fix.
- **Other cadences behaved.** The 02/03/04 UTC commissions all fired within their hours on 10-11 through 10-14; `literature-drift-review` ran Tuesday 10-13 05:15; `check-model-fallback` ran on its 4 h wall clock (17 commits); `harvest-research-subjects` on its 6 h (12 commits). `commission-claude-review-blocked-until` expired 10-14 04:00 and the Claude commission succeeded at 04:21.

### Failure Pattern Analysis

- **One failure in 255 posts**: `commission-gemini-review` 2026-10-14 04:52. No pending entry was written for Gemini on 10-14 (`pending-reviews.yaml` holds only the ChatGPT and Claude entries for that date) and the post carried no `--note`, so the reason is unrecorded. The Gemini leg otherwise worked this window (7 `auto(collect-gemini-review)` commits; last collect 10-13 06:20). Below the 3-same-type threshold; the earlier "Gemini leg failing" pattern stays resolved.
- **One real defect found and fixed inside the window**: on 2026-10-11 `agentic-social mark-posted` stripped the header comments from `evolution-state.yaml` (restored 08:50, `a8ac2cce7b`; root-caused and fixed in `save_state` at 11:36, `240fac0f30`). This is the YAML-redump family already in memory. One instance; fixed; recorded.
- **The slugify double-hyphen bug reported on 10-03 is fixed** (`0eda9e1095 fix(sync): keep double hyphens in heading anchors`).
- No non-Chrome failure among 246 non-commission posts.

### Queue Health Analysis

1. **P3 rows are never executed — now measured, not inferred.** Over the window `git log -p` on `todo.md` shows 96 `### P2:` headers removed and 103 `### ✓` entries added, but **0** `### P3:` headers removed, while 51 new P3 rows were added. The three P3 rows minted from `tenet-check-2026-10-08` (todo L1700/L1711/L1722) are still open after six days. P3 now holds 103 of 138 active tasks (86 of them refine-draft). The queue selector only takes P0–P2, and `replenishment_source_counts.promotion_from_p3` is 0. A P3 row is in practice a parked note. This is the fourth consecutive report to record it; the Tier 2 recommendation below is carried and sharpened.
2. **Replenish is correctly idle and `pending_articles` is correctly stalled.** 27 pending P0–P2 tasks keep the gate closed (threshold 3), so the last replenish is still 2026-09-29 and `pending_articles` grew 12 → 13 (today's `voids-self-prediction-void` note). The operator bypassed this on 10-12 by hand-minting 3 expand-topic P2s with the cap raise; the driver minted one more from the chain (`whether-language-model-words-refer`). Expected behaviour; no change.
3. **`queue_status` counters are stale.** They still read `p2_tasks: 13`, `p3_tasks: 7`, `loop_pickable_open: 8` from the 09-29 replenish, against parse_tasks' live 34 / 103 / 27. Only replenish writes them, and replenish is idle. Anything that reads these fields (the masked-gate memory note, this report's predecessors) gets a figure 3–15× off. Tier 2.
4. **P2 inflow is still review-driven and driver-fed.** 38 tasks were generated on 10-12 alone (outer-review cycle + pessimistic/optimistic + 3 human expand-topics); 6 active tasks carry `Source: refine-draft … (out-of-scope finding)`, i.e. forks' sibling defects that the driver hand-minted, and 9 `auto(todo)` commits in the window are driver mints or addenda. Same pattern as 10-10.
5. **Coalesce streak ended.** Two merges on 10-11 (`voids/smoothness-and-continuity` → `topics/neural-refresh-rates-and-the-smoothness-problem`; `concepts/biological-computationalism` → `topics/biological-computationalisms-inadvertent-case-for-dualism`), the first since 08-21, freeing one voids slot. The four runs since were no-candidate abandons, which the coalesce memory records as steady state. The 10-10 Tier 2 "reallocate the coalesce slots" is withdrawn: the operator's 10-12 cap raise removed the pressure that motivated it.

### Review Finding Patterns

1. **Tenet-check warnings carried for weeks without a task — pattern confirmed (5 of 8 October reports).** Each of these was flagged in a prior check and recorded again as "never minted / never queued / never repaired":
   - 10-05: `concepts/mental-effort` L94 (flagged 09-27, 10-02).
   - 10-07: `topics/forward-in-time-conscious-selection` L143 (since 09-06).
   - 10-08: `topics/contemplative-practice-as-philosophical-evidence` L59 (since 09-18).
   - 10-12: `topics/biological-computationalisms-inadvertent-case-for-dualism` L111 (since 08-12, raised as X1).
   - 10-14: `topics/structure-of-attention` L218 (checks 09-04, 09-28); plus check 149's Notes N1/N5/N6/N7 and its N2 coordination append, none actioned.
   The mechanism is the same each time: check-tenets is reports-only, its priority list reaches the queue only when the driver mints by hand, and items it mints at P3 (10-08) never run. Memory already records the yield rule ("a reports-only review's yield is its priority list, not its findings"). Tier 2 (mint at P2) and Tier 3 (a sanctioned follow-up channel) below.
2. **The dispatch-field gap is unchanged.** No commit touched `tools/evolution/task_selector.py` in the window. The driver again hand-copied `Coordination` / length context into both queue dispatches of the current session (`social-construction-of-self-vs-phenomenal-self`, apex side-task), as on 10-10 (8 of 8). Carried Tier 3.
3. **Obsidian-only writers still reach commit with Hugo stale.** This window the driver ran `scripts/sync.py` by hand after `embed-videos`, `research-voids`, `check-tenets` (review file) and before `cycle_post`; 6 `auto(sync)` commits are the earlier form of the same fix-up. Carried Tier 3.
4. **Outer-review prescriptions colliding with `tenets.md`**: no new instance this window (the 10-10 `free-will` L66 case stands alone). Dropped from the watch list.
5. **ai_system over-attribution**: no new instance reported in the window's changelog. Dropped.
6. **A documentation drift the driver noticed today**: CLAUDE.md's Section Caps table reads voids "100 / 99 — 1 slot left" and tells the reader to measure with `tools.evolution.quality.count_section_files`. Live: `max_voids: 125`, count 112; the function lives in `tools/evolution/state.py` and `tools.evolution.quality` does not import. The table's own warning ("these figures go stale fast") is correct, but a wrong module path sends a reader to an ImportError. Tier 3 (CLAUDE.md is outside this skill's write scope).

### Convergence Progress

Topics 343 → 347, concepts 349 → 357, voids 113 → 112, positions 23 → 23, apex 44. The window had 13 `expand-topic` commits (the 10-12 cap raise released the 3 human-requested articles plus chain mints), so growth resumed after the 10-07 and 10-10 calibration windows. Caps were raised to 370 / 370 / 125 / 90 on 2026-10-12 (`ffea5abe9f`), giving headroom of 23 / 13 / 13 / 67. Medium issues steady at 10, critical 0, `orphaned_files` 0. Convergence rate on counts is ~1%/window; the binding constraints are now queue-side (P3 parking, replenish idle, 13 banked research notes), not caps.

## Changes Applied (Tier 1)

*No changes applied.* No Tier 1 lever exists in `evolution-state.yaml` (the same four keys are absent, re-checked with grep). Twentieth consecutive zero-Tier-1 run.

## Recommendations (Tier 2)

### Mint check-tenets priority-list items at P2 by default (carried from 10-10, evidence now 5/8)
- **Proposed change**: when the driver (or a future follow-up channel) mints the ≤4 priority-list rows of a tenet check, use P2, not P3.
- **Rationale**: 0 P3 rows closed in 255 posts; five October checks each re-reported a warning that a prior check had already raised and nobody queued. Items minted at P2 on 10-10 ran within the day.
- **Risk**: Low; capped at 4 rows per check (`audit_triple.global_task_cap: 6` already bounds the audit family).
- **To approve**: say so in the next interactive session; the driver applies it to the 10-14 priority list (`structure-of-attention` first).

### Refresh the `queue_status` counters when replenish is idle
- **Proposed change**: have the driver (or `cycle_post` on cycle completion) rewrite `queue_status.p0_tasks … p3_tasks` and `loop_pickable_open` from `parse_tasks`, independent of replenish.
- **Rationale**: the fields have read 13 / 7 / 8 since 09-29 while the live figures are 34 / 103 / 27. The masked-gate diagnosis and this report's lineage both consult them.
- **Risk**: Low; counters only, no selection logic depends on them.
- **To approve**: one-line addition in `tools/evolution/cycle_post.py` after the anchoring audit, or a manual refresh.

### Withdraw: reallocate the two coalesce slots
- The 10-10 recommendation is withdrawn. The cap raise on 10-12 removed the voids pressure and two merges landed on 10-11. Keep the 1/24 coalesce slot as configured.

## Items for Human Review (Tier 3)

### Wire the tune-system min-age gate into the /loop pick path (new, verified in code)
- **Issue observed**: `cycle.py` carries `TRIGGER_MIN_AGE_HOURS["tune-system"] = 720` and `filter_triggers_by_min_age()`, but the only caller is `scripts/evolve_loop.py:1370`. `tools/evolution/cycle_pick.py` consumes `pending-triggers.json` without the filter, so under `/loop` tune-system fires every 6 cycles (3–4.3 days). Twenty consecutive runs at that interval.
- **Why human needed**: code change in the pick path.
- **Suggested action**: in `cycle_pick.py`, pass the pending trigger list through `filter_triggers_by_min_age(triggers, state)` and push gated skills back to the pending list (or drop them, since the next cycle completion re-enqueues).

### Forward all task fields to forks (carried from 10-03)
- **Issue observed**: `task_to_skill` forwards only File, Notes and Review file; `Headroom`, `Coordination`, `Secondary files`, `Caution` and `Carry` are dropped, and the driver hand-copies them into every dispatch (8/8 on 10-10, 2/2 so far today). No change to `task_selector.py` in the window.
- **Suggested action**: append those fields to the args string in `task_to_skill`.

### A sanctioned channel for fork- and check-discovered follow-ups (carried from 10-10)
- **Issue observed**: forks and check-tenets report follow-ups in prose; the driver minted 9 `auto(todo)` commits and 6 "out-of-scope finding" rows by hand this window; five tenet-check warnings in October were carried for 2–8 weeks because no one minted them.
- **Suggested action**: let forks and reports-only skills append to `.unfin/followups.jsonl`; `cycle_post` mints after marking the picked task, deduplicated by file + quoted span, at the priority the source names (P2 for tenet-check priority lists).

### Sync inside `cycle_post` when `obsidian/` changed (carried from 10-10)
- **Issue observed**: `embed-videos`, `research-voids` and `check-tenets` all reached `cycle_post` with Hugo stale this window; the driver synced by hand each time. Six `auto(sync)` fix-up commits in 277.
- **Suggested action**: `cycle_post` runs `scripts/sync.py` before committing whenever `git status` shows changes under `obsidian/`.

### Correct the Section Caps table and gating-function path in CLAUDE.md (new, documentation)
- **Issue observed**: the table says voids 100 / 99 and names `tools.evolution.quality.count_section_files`; live values are 125 / 112 and the function is `tools.evolution.state.count_section_files`. The topics/concepts/positions rows (320 / 320 / 80) are likewise two raises behind (370 / 370 / 90).
- **Why human needed**: CLAUDE.md is outside this skill's write scope.
- **Suggested action**: replace the hard-coded `Cap` and `Current` columns with the one-liner that prints them, and fix the module path.

### check-links should read `_redirects` (carried from 10-10)
- **Issue observed**: 424 reported this window, 376 of them Netlify 301 targets; article sections carry 0 broken links. The raw count is unusable as a gate.
- **Suggested action**: apply `hugo/static/_redirects` inside the checker.

## Next Tuning Session

- **Recommended**: 2026-11-13 (30 days). On current behaviour the trigger will fire in about 3.5 days until the min-age gate is wired into `cycle_pick.py`.
- **Focus areas**:
  - whether any P3 row is ever executed or promoted (0 in this window);
  - whether the min-age gate, dispatch-field forwarding or a follow-up channel land in code;
  - `pending_articles` (13) against the 27 pending P0–P2 that keep replenish closed;
  - whether `queue_status` counters are refreshed;
  - the next tenet check's carried-warning count.
