# Working on domain-scout

Instructions for coding agents (and humans) changing this repository.

## Layout

- `skills/domain-scout/` — the skill users install. `SKILL.md` is the entry point;
  `references/` hold detail loaded on demand; `scripts/` are run, not read;
  `templates/pack/` is copied to start a new pack.
- `domains/<name>/` — one domain pack per folder. Format:
  `skills/domain-scout/references/pack-format.md`.
- `tests/` — `python3 -m unittest discover -s tests`.

## Rules

- Keep `SKILL.md` under 200 lines and each skill reference under 300. Link every reference
  directly from `SKILL.md`; references never link to other references.
- Pack limits are in the validator: `DOMAIN.md` ≤ 200 lines, pack references ≤ 300 with a
  Contents list past 100, at least 10 questions and 8 sources.
- When you change the pack format, update `pack-format.md`, `validate_pack.py`, the
  template and the tests together, and re-validate every pack.
- Packs are paraphrased. No text copied from sources; credit them in the pack's `sources.md`
  and, for ideas the project itself uses, in `CREDITS.md`.
- Never state an MCP server, API, rule or number as fact without a source. Mark it
  unverified otherwise.
- Scripts use only the standard library plus PyYAML, and Python 3.11+.
- Run the tests and `validate_pack.py domains/* --strict` before committing.
- agent-architect's `validate.py --out .` warns that `templates/pack/DOMAIN.md` links two
  levels deep. That file is a pack template, not a skill reference; the warning is expected.
