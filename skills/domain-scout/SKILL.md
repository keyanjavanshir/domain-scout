---
name: domain-scout
description: Researches a professional field (its roles, workflows, vocabulary, tools, risks and the questions an expert would ask) and writes a "domain pack" that agent-architect uses to design multi-agent systems for that field. Use when someone asks what an industry needs, wants a domain pack created or refreshed, or when agent-architect finds no pack for the user's domain.
license: MIT
metadata:
  version: "0.1.0"
---

# Domain Scout

You research a professional field and write a **domain pack**: a small, sourced
description of how people in that field work, which tools they use, and which questions an
expert would ask before automating any of it. agent-architect loads packs during its
interview, so the pack changes the questions asked and the tools suggested.

A pack informs design; it does not do the work. It describes the field, not a solution.

Scripts live next to this file. Run them with `python3 scripts/<name>.py` from this skill's
directory, or pass absolute paths. They need Python 3.11+ and PyYAML.

## Workflow

Track these phases as a checklist the user can see.

### 1. Look for an existing pack

- Search `domains/` in the domain-scout repository and `.agent-architect/domains/` in the
  user's project. Match on the `keywords` in each `DOMAIN.md`.
- A match with `checked:` under 180 days old: use it and stop. Older: offer a refresh
  (repeat steps 3–6 for what changed, keep the rest).
- A neighbouring pack (same field, different focus): offer to extend it rather than start a
  new one.

### 2. Scope the field with the user

One question at a time, each with your recommended answer and a one-line reason. Usually
four or five are enough:

- Which part of the field? (e.g. "design" → brand identity, product UI, or film?)
- Team shape: solo, small studio, agency, in-house team, enterprise?
- Which tools do they already use? Which workflows hurt most today?
- Jurisdictions and sectors that bring rules (EU, US, regulated clients)?
- Any documents of their own to learn from (process docs, templates, past briefs)?

Write the answers into the pack's `## Scope` section. Never ask what the user's files or a
quick search can answer.

### 3. Research — read [references/research.md](references/research.md)

Plan sources before searching: practitioner guides, standards bodies and regulators, vendor
documentation, the MCP registry, skill catalogues, and the user's own documents. Need at
least eight sources across at least three of those kinds.

- **MCP servers:** if agent-architect is installed, run its `scripts/mcp_search.py
  "<tool>"` for every tool the field relies on. Otherwise query
  `https://registry.modelcontextprotocol.io/v0.1/servers?search=<tool>`. Record what you
  found *and* what you did not find.
- **Existing skills and plugins:** check catalogues for skills that already do the field's
  work, so the pack can point to them instead of anyone rebuilding them.
- If the harness can run sub-agents, research the four pack files in parallel, one agent
  each, each writing only its own file.

### 4. Write the pack — read [references/pack-format.md](references/pack-format.md)

Copy [templates/pack/](templates/pack/) to `domains/<name>/` and fill it in:

| File | Holds |
|---|---|
| `DOMAIN.md` | Scope, roles, workflows, vocabulary, what good looks like, risks. ≤ 200 lines. |
| `references/questions.md` | Interview questions, grouped by agent-architect's design-tree branches. |
| `references/tools.md` | The field's tools mapped to MCP servers, APIs, CLIs and auth. |
| `references/patterns.md` | Agent teams that fit the field, expert roles, anti-patterns. |
| `sources.md` | Every source with its URL and what it informed. |

Set `status: draft` and today's date in `checked:`.

### 5. Validate

```bash
python3 scripts/validate_pack.py domains/<name>
```

Fix every error. Warnings are worth fixing too; `--strict` makes them errors.

### 6. Review with the user

Walk through the pack in this order: scope, risks, questions, tools. Ask what is wrong or
missing, one point at a time. Only when the user says it is right, set `status: reviewed`
and `reviewed: <date>`. A draft pack may be used, but say that it is a draft.

### 7. Save

- **Project-only:** `.agent-architect/domains/<name>/` in the user's project.
- **For everyone:** a pull request to the domain-scout repository adding `domains/<name>/`.
  Ask before opening it; it publishes the pack.

## Hard rules

- **Paraphrase, never copy.** Write every sentence yourself. Quote nothing longer than a
  term or a standard's name. Credit sources in `sources.md`.
- **Mark what you did not verify.** A tool, server or rule you could not confirm in a
  primary source is labelled unverified, never stated as fact.
- **Never invent MCP servers.** List only servers you found in the registry or in vendor
  docs; otherwise write "none found" and the date you looked.
- **Date everything that changes**: tools, limits, rules, prices.
- **No credentials** in a pack. Auth is described by kind (OAuth, API key in `${VAR}`).
- **Describe the field, not one company.** Company-specific terms and approval chains
  belong in the user's project overlay, not in a shared pack.
