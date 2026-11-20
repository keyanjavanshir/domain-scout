# CLAUDE.md

@AGENTS.md

## What this project is

domain-scout holds **domain packs** for agent-architect (github.com/keyanjavanshir/architect)
and the `domain-scout` skill that researches and writes them. A pack tells agent-architect
how a field works — roles, workflows, vocabulary, tools, risks — and which questions an
expert would ask, so its interview and tool suggestions fit the field.

Split out of agent-architect on 2026-11-20 (idea 2 in architect's `docs/ideas.md`).

## Why it is built this way

- **Separate repository.** Packs version, grow and take contributions independently, and
  never bloat agent-architect. agent-architect fetches only the packs a request needs and
  falls back to its generic interview when offline.
- **Packs inform design, they do not do the work.** Collections such as
  anthropics/knowledge-work-plugins and alirezarezvani/claude-skills already provide
  experts that do the work; a pack points to them in `tools.md` instead of rebuilding them.
- **questions.md uses agent-architect's design-tree branch names** as headings, so the
  architect can merge questions branch by branch. If architect renames a branch, change
  `BRANCHES` in `validate_pack.py` and every pack.
- **Draft until a person reviews it.** The scout never marks a pack reviewed on its own.
- **Negative results are recorded** ("no MCP server found, date"), so the architect can
  suggest an API or file export instead.

## Next work

1. agent-architect integration: in "take stock", match the request against pack
   `keywords`, load `DOMAIN.md`, merge `questions.md` into the interview, seed MCP search
   from `tools.md`. Decide how packs are fetched (git sparse checkout, raw URL, or a local
   clone) and the project overlay format (`.agent-architect/domains/<name>/`).
2. Review `creative-direction-film` with the owner and mark it reviewed.
3. Evals: run the same agent-architect interview with and without a pack and compare the
   questions asked and tools suggested.
4. More packs; a refresh flow for packs past 180 days.
