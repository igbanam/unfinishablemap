---
name: research-topic
description: Research a philosophical topic using web search. Outputs research notes, not finished content.
context: fork
agent: general-purpose
---

# Research Topic

Conduct web research on a philosophical topic and produce structured research notes.

## When to Use

- Before writing a new article
- When a todo item is type `research-topic`
- When `/research-topic [topic]` is invoked
- Monthly gap research

## Instructions

### 1. Clarify the Topic

If a specific topic is provided, use it directly.

If invoked from todo.md, extract the topic from the task description.

### 2. Web Research

Use WebSearch to find:

#### Primary Academic Sources
- Stanford Encyclopedia of Philosophy (plato.stanford.edu)
- Internet Encyclopedia of Philosophy (iep.utm.edu)
- PhilPapers (philpapers.org)

#### Key Thinkers
- Who are the major philosophers on this topic?
- What are their main positions?
- What are the key debates?

#### Historical Context
- How has thinking evolved on this topic?
- What are the major milestones?

#### Scientific Connections
- What relevant scientific research exists?
- How do empirical findings inform the philosophy?

#### Contemporary Discussions
- What are current debates?
- Are there recent developments?

### 3. Evaluate Sources Against Tenets

For each major position found, note:
- Does it align with site tenets?
- Does it conflict with any tenet?
- How would site tenets respond to this view?

### 4. Generate Research Notes

Create notes at `obsidian/research/[TOPIC-SLUG]-YYYY-MM-DD.md`:

```markdown
---
title: Research Notes - [Topic]
created: YYYY-MM-DD
draft: false
ai_contribution: 100
ai_system: [current model]
recommended_action: article   # article | fold | refine | none — see "Declare the verdict" below
target_section: topics        # topics | concepts | voids (used when recommended_action is article)
target_slug: [kebab-slug]     # the article's slug; must be free in that section (check_slug)
---

# Research: [Topic]

**Date**: YYYY-MM-DD
**Search queries used**: [list]

## Executive Summary

[3-5 sentence overview of what was found]

## Key Sources

### [Source Title]
- **URL**: [url]
- **Type**: Encyclopedia/Paper/Book/Article
- **Key points**:
  - Point 1
  - Point 2
- **Tenet alignment**: Aligns/Conflicts/Neutral with [tenet]
- **Quote**: "[notable quote]"

## Major Positions

### [Position Name] (e.g., "Physicalism")
- **Proponents**: [names]
- **Core claim**: [summary]
- **Key arguments**: [list]
- **Relation to site tenets**: [analysis]

### [Position Name] (e.g., "Property Dualism")
[Similar format]

## Key Debates

### [Debate Title]
- **Sides**: [who argues what]
- **Core disagreement**: [what they disagree about]
- **Current state**: [resolved? ongoing?]

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| YYYY | [event] | [why it matters] |

## Potential Article Angles

Based on this research, an article could:
1. [Angle 1 - how it would align with tenets]
2. [Angle 2 - alternative approach]

When writing the article, follow `obsidian/project/writing-style.md` for:
- Named-anchor summary technique for forward references
- Background vs. novelty decisions (what to include/omit)
- Tenet alignment requirements
- LLM optimization (front-load important information)

## Gaps in Research

- [What couldn't be found]
- [What needs deeper investigation]

## Citations

[Full citation list in consistent format]
```

#### Declare the verdict (frontmatter)

The three frontmatter fields above are read by code: after this skill returns,
`cycle_post.py` (`tools/research/chain.py`) mints a P2 `expand-topic` task for
the note when `recommended_action` is `article`. Set them deliberately:

- `article` — the subject deserves a standalone page. Give `target_section` and a
  free `target_slug` (`uv run python scripts/check_slug.py <slug> <section>`).
- `fold` — the material belongs inside an existing article; `refine` — the note
  mainly corrects existing pages; `none` — not worth a page. These mint nothing,
  so say in the note which pages should absorb it.

Do **not** add the expand-topic task to `todo.md` yourself; the chain does it
(and skips notes a todo task already references). Put every guard the article
writer must respect (author stances, quote status, coiner/populariser warnings,
integration passages) in the note itself, because the minted task points the
writer at the note.

### 5. Do Not Mark Todo Complete

Leave the originating todo task untouched. The orchestrator
(`cycle_post.py`) marks it complete after this skill returns.

### 6. Log to Changelog

Prepend entry to `obsidian/workflow/changelog.md` (add immediately after frontmatter, before existing entries):

```markdown
## [current time from prompt] - research-topic
- **Status**: Success
- **Topic**: [topic name]
- **Output**: [[filepath without .md extension]]
- **Sources consulted**: [count]
```

## Important

- This skill ONLY produces research notes
- Does NOT generate article content
- Use `/expand-topic` to write articles based on research
- Always cite sources with URLs
- Be honest about tenet conflicts - don't hide opposing views
- Note where research is incomplete
