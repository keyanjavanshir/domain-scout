# domain-scout

Domain packs for [agent-architect](https://github.com/keyanjavanshir/architect), and the
skill that researches and writes them.

agent-architect interviews you about a workflow and generates the multi-agent system to run
it. Its interview asks good structural questions, but not the ones an expert in your field
would ask. A **domain pack** fills that gap: a short, sourced description of how a field
works — roles, workflows, vocabulary, tools, risks — plus the questions to ask before
automating any of it.

Other skill collections give you experts that *do the work* in a field. Packs here *inform
the design* of a system for that field.

## Packs

| Pack | Field | Status | Checked |
|---|---|---|---|
| [creative-direction-film](domains/creative-direction-film/DOMAIN.md) | Creative direction for film and video: commercials, brand films, social video | draft | 2026-11-20 |

## What is in a pack

```
domains/<name>/
├── DOMAIN.md              scope, roles, workflows, vocabulary, what good looks like, risks
├── sources.md             every source and what it informed
└── references/
    ├── questions.md       interview questions, by agent-architect's design-tree branch
    ├── tools.md           the field's tools mapped to MCP servers, APIs, CLIs and auth
    └── patterns.md        agent teams that fit the field, expert roles, anti-patterns
```

The full contract is in
[skills/domain-scout/references/pack-format.md](skills/domain-scout/references/pack-format.md).

## The domain-scout skill

`skills/domain-scout/` is an [Agent Skill](https://agentskills.io/specification). Given a
field, it grills you about it — briefly for a generic pack, or in depth for a narrow
expert; you can skip any question — then researches it (practitioner guides, standards, vendor docs,
the MCP registry, skill catalogues, your own documents), writes a pack from the template,
validates it, and reviews it with you before marking it `reviewed`. Answers about your own
team, clients and tools go into a private `OVERLAY.md` in your project, never into the
shared pack.

Install it by copying or symlinking the folder into your harness's skills directory, e.g.
`.agents/skills/domain-scout` or `.claude/skills/domain-scout`, then ask for a domain pack.

## Validate a pack

```bash
python3 skills/domain-scout/scripts/validate_pack.py domains/<name>
```

Needs Python 3.11+ and PyYAML. Checks frontmatter, required sections, size limits, question
format, tool tables, source count and literal credentials. Tests:
`python3 -m unittest discover -s tests`.

## Contributing a pack

Run the skill, review the pack yourself, then open a pull request adding
`domains/<name>/`. Packs are paraphrased — no copied text — and every claim that a rule,
number or tool exists needs a source in `sources.md`.

## Status

v0.1. agent-architect does not load packs yet; that integration is the next step.

## License

MIT. See [CREDITS.md](CREDITS.md) for the projects whose ideas this builds on.
