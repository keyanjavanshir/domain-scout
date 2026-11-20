# Grilling the user about their field

The scout's interview. It decides how specific the expert becomes. Every question can be
skipped; a skipped question gets the field's usual answer, recorded as an assumption.

## Contents
- Depth: the user chooses
- How to ask
- The domain tree
- Where each answer goes
- Ending the grill

## Depth: the user chooses

Open with one question: how specific should the expert be?

- **Quick** — two or three questions to place the field, then research. Produces a generic
  pack. Right when the user wants a starting point or has no time.
- **Deep** (recommended when the user will use the expert for real work) — walk the whole
  tree below until no branch is open. Produces a narrow pack, and an overlay if the user
  describes their own team.

The user can switch at any point: "that's enough" ends the grill, "ask me more" deepens it.

## How to ask

- **One question per turn**, with two to four options and your recommended answer marked,
  plus a one-line reason. The user can answer in their own words.
- **"Skip" is always an option.** Record a skipped question's usual answer under
  "Assumed, not asked" in the pack's Scope section.
- **Look before you ask.** Read documents the user provides and anything agent-architect
  already learned (it may pass its decision log). Never re-ask a question already answered.
- **Follow the branch.** An answer that narrows the field ("only music videos") opens its
  own follow-ups before you move on.
- **Ask about practice, not opinion.** "Who signs off the grade?" beats "How do you feel
  about grading?"
- **Keep a log**: one line per answer with where it goes (pack or overlay).

## The domain tree

Cover the branches that apply. Each one shapes named parts of the pack.

**Sub-field and focus** → pack name, Scope
- Which part of the field? Which kinds of work, and which never?
- Typical size of a piece of work (a day, a month, a year)?

**Team and roles** → Roles
- Solo, studio, agency, in-house, enterprise? Which roles exist, and who holds several?
- Who approves each stage?

**Clients and stakeholders** → Workflows, Risks
- Who is the work for? How many review rounds are normal? Who has the final say?

**Workflow and stages** → Workflows
- Walk one recent piece of work from start to finish. Where did it stall?
- Which stages are skipped or merged here, compared with the textbook?

**Tools in use** → tools.md
- Which tools does the team use at each stage? Which are mandated by clients?
- What is the system of record (tracker, drive, review tool)?

**Rules and risks** → Risks and compliance
- Jurisdictions and sectors (EU, US, regulated clients)? Union or guild work?
- What has gone wrong before (a rights claim, a leak, a missed spec)?

**Quality bar** → What good looks like
- What separates great work from acceptable here? Show me an example you are proud of.
- What do clients complain about most?

**Pain and automation** → Where agents help, patterns.md
- Which recurring tasks take the most time? Which would you never hand to an agent?

**Language** → Vocabulary
- Terms your team uses differently from the textbook, or that outsiders get wrong?

## Where each answer goes

| The answer is about… | Goes into | Example |
|---|---|---|
| The field or sub-field in general | The pack | "Music videos rarely have a client legal review." |
| This team, its clients, its tools or its people | The overlay | "Our label's A&R approves every cut." |
| Something confidential | Nowhere, or the overlay only | Client names, budgets, unreleased work. |

If the answers narrow the field a lot, name the pack for the narrower focus
(`creative-direction-music-video`) and set `related:` to the broader pack.

Never put names of people or clients, budgets, or unreleased work in a pack. Packs can be
shared publicly; overlays stay in the user's project.

## Ending the grill

Stop when the user says so or no branch is open. Then play back, in five lines or fewer:
the focus, the team shape, the main tools, the rules that apply, and what goes into the
overlay. Ask for a yes, then research. Questions you could not settle become research
questions in step 3.
