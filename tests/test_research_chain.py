"""Tests for tools.research.chain (research → expand-topic minting)."""

import subprocess
from pathlib import Path

import pytest

from tools.research.chain import LogicFlawError, chain_new_research_notes, chain_note

CAPS = {"topics": 370, "concepts": 370, "voids": 125}
TODO = "# Todo\n\n## Active Tasks\n\n### P2: Existing task\n- **Type**: refine-draft\n\n## Completed Tasks\n"


def _repo(tmp_path: Path) -> Path:
    for d in ("research", "topics", "concepts", "voids", "workflow"):
        (tmp_path / "obsidian" / d).mkdir(parents=True)
    (tmp_path / "obsidian" / "workflow" / "todo.md").write_text(TODO)
    return tmp_path


def _note(repo: Path, name: str, fm: str) -> Path:
    p = repo / "obsidian" / "research" / f"{name}.md"
    p.write_text(f"---\ntitle: \"Research Notes: Some Topic\"\n{fm}---\n\nBody\n")
    return p


def test_article_mints_with_declared_slug_and_section(tmp_path):
    repo = _repo(tmp_path)
    note = _note(repo, "foo-bar-2026-10-19",
                 "recommended_action: article\ntarget_section: concepts\ntarget_slug: foo\n")
    result, block = chain_note(note, TODO, CAPS, "2026-10-19", repo)
    assert result.minted and result.reason == "minted"
    assert block.startswith("### P2: Write `concepts/foo` — Some Topic\n")
    assert "- **Type**: expand-topic\n" in block
    assert f"- **File**: {note}\n" in block


@pytest.mark.parametrize("action", ["fold", "refine", "none"])
def test_non_article_actions_do_not_mint(tmp_path, action):
    repo = _repo(tmp_path)
    note = _note(repo, "x-2026-10-19", f"recommended_action: {action}\n")
    result, block = chain_note(note, TODO, CAPS, "2026-10-19", repo)
    assert not result.minted and block is None


def test_unknown_action_raises(tmp_path):
    repo = _repo(tmp_path)
    note = _note(repo, "x-2026-10-19", "recommended_action: maybe\n")
    with pytest.raises(LogicFlawError):
        chain_note(note, TODO, CAPS, "2026-10-19", repo)


def test_missing_action_mints_with_assess_first_and_slug_from_filename(tmp_path):
    repo = _repo(tmp_path)
    note = _note(repo, "inner-speech-2026-10-19", "")
    result, block = chain_note(note, TODO, CAPS, "2026-10-19", repo)
    assert result.minted and "no recommended_action" in result.reason
    assert "`topics/inner-speech`" in block
    assert "read its recommendation first" in block


def test_skips_when_todo_already_references_note(tmp_path):
    repo = _repo(tmp_path)
    note = _note(repo, "foo-2026-10-19", "recommended_action: article\n")
    todo = TODO + f"\n- **File**: obsidian/research/{note.name}\n"
    result, block = chain_note(note, todo, CAPS, "2026-10-19", repo)
    assert not result.minted and block is None


def test_skips_existing_article_and_full_section(tmp_path):
    repo = _repo(tmp_path)
    (repo / "obsidian" / "topics" / "foo.md").write_text("x")
    note = _note(repo, "foo-2026-10-19", "recommended_action: article\n")
    assert not chain_note(note, TODO, CAPS, "2026-10-19", repo)[0].minted

    note2 = _note(repo, "bar-2026-10-19", "recommended_action: article\n")
    assert not chain_note(note2, TODO, {**CAPS, "topics": 1}, "2026-10-19", repo)[0].minted


def test_chain_new_research_notes_inserts_only_untracked_notes(tmp_path):
    repo = _repo(tmp_path)
    old = _note(repo, "old-2026-10-01", "recommended_action: article\n")
    subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
    subprocess.run(["git", "add", "-A"], cwd=repo, check=True)
    subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "i"],
                   cwd=repo, check=True)
    _note(repo, "new-topic-2026-10-19", "recommended_action: article\n")

    todo_path = repo / "obsidian" / "workflow" / "todo.md"
    results = chain_new_research_notes(CAPS, "2026-10-19", repo, todo_path)
    assert [r.minted for r in results] == [True]
    text = todo_path.read_text()
    assert text.index("`topics/new-topic`") < text.index("### P2: Existing task")
    assert old.stem not in text
