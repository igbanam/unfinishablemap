"""Deterministic research → expand-topic chaining.

After a `research-topic` queue task succeeds, `cycle_post.py` calls
`chain_new_research_notes()` to mint a P2 `expand-topic` task for each new
research note that recommends a standalone article.

Why this lives in code: the research-topic skill runs in a fork, and forks
reliably write the note but unreliably remember a follow-on todo edit. The
only other route — replenish-queue's `unconsumed_research` source — fires only
when P0–P2 drops below 3, which the steady refine-draft stream almost never
allows. Notes therefore accumulated with no article task (~30 by 2026-10-12).

The research note declares its own verdict in frontmatter:

    recommended_action: article   # article | fold | refine | none
    target_section: concepts      # topics | concepts | voids
    target_slug: some-slug

`article` (or a missing field, treated as `article` with a warning, since the
large majority of notes recommend one) mints a task; `fold` / `refine` /
`none` mint nothing.
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).parent.parent.parent
RESEARCH_DIR = REPO_ROOT / "obsidian" / "research"
TODO_PATH = REPO_ROOT / "obsidian" / "workflow" / "todo.md"

ARTICLE_SECTIONS = ("topics", "concepts", "voids")
MINTING_ACTIONS = ("article",)
NON_MINTING_ACTIONS = ("fold", "refine", "none")


class LogicFlawError(Exception):
    """Raised for cases that indicate a programming or contract error."""


@dataclass
class ChainResult:
    note: str
    minted: bool
    reason: str


def new_research_notes(repo_root: Path = REPO_ROOT) -> list[Path]:
    """Research notes that are new (untracked or added) in the working tree."""
    out = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=all", "--", "obsidian/research/"],
        capture_output=True,
        text=True,
        cwd=repo_root,
        check=True,
    ).stdout
    notes = []
    for line in out.splitlines():
        code, path = line[:2], line[3:].strip()
        if ("?" in code or "A" in code) and path.endswith(".md"):
            notes.append(repo_root / path)
    return notes


def read_frontmatter(path: Path) -> dict:
    text = path.read_text()
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    data = yaml.safe_load(text[4:end]) or {}
    return data if isinstance(data, dict) else {}


def _expand_task_block(note: Path, title: str, section: str, slug: str, today: str,
                       count: int, cap: int, action_declared: bool) -> str:
    verdict = (
        "The note's frontmatter declares `recommended_action: article`."
        if action_declared
        else "The note declares no `recommended_action`; read its recommendation first, "
        "and if it advises a fold or refinement rather than a standalone article, do that "
        "instead (as refine-draft) and say so."
    )
    return (
        f"### P2: Write `{section}/{slug}` — {title}\n"
        f"- **Type**: expand-topic\n"
        f"- **File**: {note}\n"
        f"- **Target section**: {section}\n"
        f"- **Section**: {section}\n"
        f"- **Status**: pending\n"
        f"- **Source**: research-chain (auto-minted by cycle_post after research-topic)\n"
        f"- **Generated**: {today}\n"
        f"- **Headroom**: {section} {count}/{cap} at mint (count_section_files). "
        f"Re-measure before writing; stop at the cap.\n"
        f"- **Notes**: {verdict} Follow the note's recommended angle and every guard it "
        f"records (author-stance, quote-status and coiner warnings); quote only material "
        f"the note marks verified, and grep the raw source for anything else. Apply the "
        f"note's integration passages where length-safe. Frontmatter per the CLAUDE.md "
        f"schema (`topics:` bare slugs, non-empty); ai_system = the model you actually run "
        f"as. Sync, verify both obsidian and hugo trees, and register in "
        f"task_chains.pending_cross_reviews.\n"
    )


def chain_note(note: Path, todo_text: str, caps: dict[str, int], today: str,
               repo_root: Path = REPO_ROOT) -> tuple[ChainResult, str | None]:
    """Decide whether `note` gets an expand-topic task. Returns (result, block-or-None)."""
    rel = str(note.relative_to(repo_root))
    fm = read_frontmatter(note)
    action = fm.get("recommended_action")
    if action is not None:
        action = str(action).strip().lower()

    if action in NON_MINTING_ACTIONS:
        return ChainResult(rel, False, f"recommended_action={action}"), None
    if action is not None and action not in MINTING_ACTIONS:
        raise LogicFlawError(f"{rel}: unknown recommended_action {action!r}")

    if note.stem in todo_text:
        return ChainResult(rel, False, "a todo task already references this note"), None

    section = str(fm.get("target_section") or "topics").strip()
    if section not in ARTICLE_SECTIONS:
        return ChainResult(rel, False, f"target_section {section!r} not an article section"), None
    slug = str(fm.get("target_slug") or "").strip()
    if not slug:
        # research-topic names notes <slug>-YYYY-MM-DD
        slug = note.stem[:-11] if note.stem[-11:-10] == "-" else note.stem
    if (repo_root / "obsidian" / section / f"{slug}.md").exists():
        return ChainResult(rel, False, f"{section}/{slug}.md already exists"), None

    section_dir = repo_root / "obsidian" / section
    count = sum(
        1 for p in section_dir.iterdir()
        if p.suffix == ".md" and p.name != "_index.md" and p.stem != section
    )
    cap = caps[section]
    if count >= cap:
        return ChainResult(rel, False, f"{section} at cap ({count}/{cap})"), None

    title = str(fm.get("title") or slug).strip()
    for prefix in ("Research Notes:", "Research Notes -", "Research:"):
        if title.startswith(prefix):
            title = title[len(prefix):].strip()
    block = _expand_task_block(
        repo_root / rel, title, section, slug, today, count, cap, action is not None
    )
    reason = "minted" if action is not None else "minted (no recommended_action declared)"
    return ChainResult(rel, True, reason), block


def chain_new_research_notes(caps: dict[str, int], today: str,
                             repo_root: Path = REPO_ROOT,
                             todo_path: Path = TODO_PATH) -> list[ChainResult]:
    """Mint expand-topic tasks for new research notes; insert at top of Active Tasks."""
    notes = new_research_notes(repo_root)
    if not notes:
        return []
    todo = todo_path.read_text()
    results: list[ChainResult] = []
    blocks: list[str] = []
    for note in notes:
        result, block = chain_note(note, todo + "".join(blocks), caps, today, repo_root)
        results.append(result)
        if block:
            blocks.append(block)
    if blocks:
        marker = "## Active Tasks\n"
        idx = todo.find(marker)
        if idx == -1:
            raise LogicFlawError("todo.md has no '## Active Tasks' section")
        insert_at = idx + len(marker)
        todo_path.write_text(todo[:insert_at] + "\n" + "\n".join(blocks) + todo[insert_at:])
    return results
