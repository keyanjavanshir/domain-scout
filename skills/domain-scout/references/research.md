# Research method

How to research a field so the pack is accurate, current and in your own words.

## Contents
- Source kinds and what each is good for
- Order of work
- Verifying claims
- Freshness
- Writing in your own words

## Source kinds and what each is good for

| Kind | Good for | Watch out for |
|---|---|---|
| Practitioner guides, trade press, courses | Workflows, roles, vocabulary, habits | Vendor marketing posing as a guide; one region's habits |
| Standards bodies, regulators, law firms | Rules, thresholds, legal duties | Superseded versions; jurisdiction |
| Vendor documentation | What a tool does, its API, its auth | Features in beta or on paid plans only |
| MCP registry | Which servers exist, who publishes them | Many unofficial servers with similar names |
| Skill and plugin catalogues | Skills that already do the field's work | Quality varies; check the licence |
| The user's own documents | How *this* team works | Company-specific detail belongs in a project overlay |

AI-generated listicles and ranking sites are leads, never sources. Follow them to the
primary page or drop the claim.

## Order of work

1. **Map the work** from practitioner sources: stages, artefacts, roles, hand-offs.
2. **Find the rules** that apply: rights, safety, privacy, accessibility, sector rules.
   Prefer the standard or regulator's own page.
3. **List the tools** practitioners name repeatedly, then check each one: vendor docs for
   API and auth, the MCP registry for servers.
4. **Check catalogues** for existing skills covering the field's tasks.
5. **Draft questions last**, from what you learned: every risk, hand-off and tool choice
   suggests a question the generic interview would miss.

## Verifying claims

- A number, threshold or legal duty needs a primary source (the standard, the regulator,
  the vendor). Otherwise mark it unverified.
- Two secondary sources that disagree: say so in the pack, do not pick one silently.
- MCP servers: an entry in the registry under the vendor's namespace (e.g. `com.figma/…`)
  or a vendor docs page counts as official. Everything else is unofficial.
- Record negative results ("no MCP server found for X, 2026-11-20"). They save the next
  person a search and tell agent-architect to suggest an API or file export instead.

## Freshness

- Put today's date in `checked:` in `DOMAIN.md` and `sources.md`.
- Tool rows carry their own date: tools change faster than workflows.
- A pack older than 180 days is refreshed before use: re-check tools and rules first; roles
  and workflows rarely change.

## Writing in your own words

- Read, close the page, then write. Do not paste and edit.
- Use the field's terms (they are vocabulary, not copied text), but explain them yourself.
- Never reproduce a source's checklist or table structure wholesale; build your own from
  several sources.
- Each source in `sources.md` says what it informed, so a reviewer can check the claim.
