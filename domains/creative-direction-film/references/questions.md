# Questions for film and video systems

Add these to agent-architect's design tree. Each has a recommended answer for a typical
small-to-mid studio; adjust to what the user tells you.

## Contents
- Outcome
- Trigger and inputs
- Decomposition
- Roles
- Knowledge
- Tools and data
- Risk and permissions
- Verification
- Environment

## Outcome

- **Which stage of the work should this system serve: concept, pre-production, post, or
  delivery?** Recommended: one stage per system — the artefacts, tools and approvers differ
  too much between stages to serve well at once.
- **What artefact does a run produce, and in what form will the CD look at it?**
  Recommended: a document or board the CD already uses (deck, Notion page, Frame.io
  comments), not a new format they must learn.
- **Who approves the output before anyone outside the team sees it?** Recommended: the CD,
  always; the system never sends to the client on its own.

## Trigger and inputs

- **Is there a written brief, and does the system read it?** Recommended: yes — make the
  brief a required input and check every output against it.
- **Is the deliverables matrix agreed, and is it an input?** Recommended: yes; lengths,
  ratios and languages decide what to shoot and what to check at delivery.
- **What starts a run: a new brief, a new cut uploaded for review, or a delivery
  deadline?** Recommended: a person typing the command with a project or cut link; event
  triggers only once the manual run is trusted.

## Decomposition

- **What is one unit of work: a reference axis, a scene, a reviewer's comments, an
  interview, a deliverable?** Recommended: pick the unit that varies most per project;
  deliverables and interviews fan out well.
- **How many units in a large project?** Recommended: plan for the deliverables matrix
  (often 20–100 versions) — it caps fan-out width and cost.
- **Do routes or options get explored in parallel?** Recommended: yes for concept work
  (two or three routes), each researched independently, then compared by one agent.

## Roles

- **Which roles does the team really have, and who holds each?** Recommended: map agents to
  the role whose work they prepare, and to the person who approves it.
- **Should any agent judge creative quality?** Recommended: no; agents check against the
  brief, specs and consistency, and flag taste questions for the CD.
- **Is a "brief guardian" wanted — an agent that checks each output against the brief?**
  Recommended: yes for concept and review work; it catches drift early.

## Knowledge

- **Is there a house style for treatments, decks and shot lists?** Recommended: capture it
  as a skill with one good example; agents imitate examples better than rules.
- **Are the client's brand guidelines available (logo use, colour, type, tone)?**
  Recommended: required input for supers, titles and social versions.
- **Which delivery specs apply: broadcast (EBU R128, ATSC A/85), platform spec sheets, the
  client's own?** Recommended: store the client's spec sheet as a reference the QC agent
  reads; never hard-code numbers in prompts.

## Tools and data

- **Where do cuts go for review (Frame.io, Vimeo, a shared drive)?** Recommended: read
  comments through the review tool's API or MCP server; write replies only after approval.
- **Which editing and grading software does the team use?** Recommended: integrate through
  exported files (EDL, XML, AAF, transcripts) rather than driving the open project.
- **Where is footage stored, and how big is it?** Recommended: agents read metadata and
  proxies, never move or copy camera originals.
- **Is there a tracker for clearances, versions and deliverables (Airtable, Notion,
  spreadsheet)?** Recommended: yes, one table per project that agents update and people
  approve.

## Risk and permissions

- **Can any footage, script or product information leave the team's approved tools?**
  Recommended: no by default; list approved services explicitly in every brief.
- **May the system use generative AI for frames, voices or music, and is that in the final
  film or only in previs?** Recommended: previs and temp only, unless the client approves in
  writing; disclosure and consent rules apply to anything in the final film.
- **Which actions need a checkpoint: sending to client, publishing, deleting media,
  buying stock or licences?** Recommended: all of them.
- **Who confirms clearances are complete before delivery?** Recommended: the producer, from
  a checklist the system prepares; the system never marks an item cleared on its own.

## Verification

- **How is a delivered file checked?** Recommended: automated technical QC with ffprobe and
  a loudness measurement against the spec sheet, then a human watch-down.
- **How are conflicting client notes handled?** Recommended: the consolidator flags the
  conflict and the CD resolves it before the editor sees the list.
- **What happens when one deliverable fails QC?** Recommended: report it and continue with
  the rest; never re-encode or overwrite a master automatically.

## Environment

- **Do the people running it work in a terminal or only in desktop apps?** Recommended: if
  only desktop apps, keep the system to one command and outputs in tools they already open.
- **Is footage on a local machine, a NAS or the cloud?** Recommended: run agents where the
  metadata and proxies are; do not upload footage to run an agent.
- **What does a run cost in time and money, and who pays?** Recommended: set a per-run
  budget before allowing fan-out across the whole deliverables matrix.
