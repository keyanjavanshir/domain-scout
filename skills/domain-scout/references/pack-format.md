# Pack format

The contract between domain-scout (which writes packs) and agent-architect (which reads
them). `scripts/validate_pack.py` checks every rule marked **(checked)**.

## Contents
- Layout
- DOMAIN.md
- questions.md
- tools.md
- patterns.md
- sources.md
- How agent-architect uses a pack

## Layout

```
domains/<name>/
├── DOMAIN.md
├── sources.md
└── references/
    ├── questions.md
    ├── tools.md
    └── patterns.md
```

`<name>` is lowercase kebab-case and names a field plus its focus, e.g.
`creative-direction-film`, `finance-period-close`. **(checked)**

## DOMAIN.md

At most 200 lines. **(checked)** Frontmatter:

```yaml
---
name: creative-direction-film        # equals the folder name (checked)
title: Creative direction — film and video
description: One or two sentences: the field and what the pack covers.
keywords: [creative director, video production, commercial, post-production]
status: draft                        # draft | reviewed (checked)
checked: 2026-11-20                  # date the research was last done (checked)
reviewed: 2026-11-21                 # required when status is reviewed (checked)
related: [marketing-brand]           # optional: neighbouring packs
---
```

`keywords` are what a request is matched against, so include the words a user would type
("videographer", "brand film"), not only the trade's own terms.

Required sections, as `##` headings, in this order **(checked)**:

1. **Scope** — what the pack covers and, as important, what it does not.
2. **Roles** — who does what; note how roles collapse in small teams.
3. **Workflows** — the stages of the work, each with its artefacts and who approves.
4. **Vocabulary** — terms an agent must use correctly. One line each.
5. **What good looks like** — the bar a practitioner holds work to.
6. **Risks and compliance** — rights, regulation, safety, irreversible actions.
7. **Where agents help** — work suited to agents, and decisions that stay with people.
8. **References** — links to the three reference files and `sources.md`. **(checked)**

## questions.md

Interview questions an expert in the field would ask, added to agent-architect's design
tree. Group them under `##` headings that are exactly the tree's branch names
**(checked)**: Outcome, Trigger and inputs, Decomposition, Roles, Knowledge, Tools and data,
Risk and permissions, Verification, Environment. Skip branches the field adds nothing to.

Each question is one bullet, with a recommended answer **(checked)**:

```markdown
- **Is the deliverables matrix agreed before the shoot?** Recommended: yes, and the
  system reads it as input — cutdowns and aspect ratios decide what must be shot.
```

At least ten questions. **(checked)** Ask for decisions, not essays.

## tools.md

One table per tool category, with exactly these columns **(checked)**:

| Tool | Used for | Integration | Auth | Checked |
|---|---|---|---|---|

- **Integration:** the MCP server's registry name (official ones first), else the API or
  CLI, else "none found". Say "unofficial" for community servers.
- **Auth:** the kind only: OAuth, API key in `${VAR}`, local app, none.
- **Checked:** where and when it was confirmed, e.g. `registry 2026-11-20`,
  `vendor docs 2026-11-20`, or `unverified`. **(checked: never empty)**

After the tables, a short section on how the field's tools behave for agents (desktop apps
driven by local servers, cloud tools behind OAuth, file interchange formats).

## patterns.md

- **Teams** — agent teams that fit the field's work, each named with its smallest-system
  level (one skill, fan-out, waves), its units of work, what each agent owns and where the
  human checkpoints sit.
- **Expert roles** — points of view worth turning into an agent (a brief guardian, a
  deliverables checker).
- **Anti-patterns** — designs that fail in this field and why.

## sources.md

A `checked:` line, then one bullet per source: link, kind, and what it informed. At least
eight distinct URLs **(checked)**, across at least three kinds (practitioner, standard or
regulator, vendor docs, registry, catalogue, user document).

## How agent-architect uses a pack

- **Take stock:** match the request against `keywords`; load `DOMAIN.md` of the best one
  or two packs.
- **Interview:** merge `questions.md` into the design tree, branch by branch.
- **Reuse before you build:** `tools.md` seeds the MCP and skill search.
- **Blueprint:** `patterns.md` informs decomposition and checkpoints; risks become
  checkpoints and never-do rules in agent briefs.
