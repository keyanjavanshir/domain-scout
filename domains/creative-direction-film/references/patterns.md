# Patterns for film and video systems

Agent teams that fit the work, named by agent-architect's smallest-system levels: one
skill, orchestrator + parallel workers (fan-out), or pipeline in waves.

## Contents
- Teams
- Expert roles
- Anti-patterns

## Teams

**Reference and mood-board research** — fan-out.
- Unit: one reference axis (tone, colour and light, camera and framing, editing rhythm,
  sound and music, casting), or one creative route.
- Workers each write `references/<axis>.md` with specific shots, sources and why each fits.
- A synthesiser builds one board or document per route. Checkpoint: the CD picks.

**Script to shot list and breakdown** — one skill.
- Sequential and small enough for one context: scenes, shots, coverage, props, cast,
  locations, and flags for anything needing clearance. A team adds nothing here.

**Review-round consolidation** — pipeline.
- Wave 1: read every comment on the cut from the review tool, grouped by reviewer.
- Wave 2: one consolidator merges them into a single timecoded list, flags conflicts, and
  tags each note as brief-related or taste.
- Checkpoint: the CD resolves conflicts and approves the list.
- Wave 3: a publisher posts the approved list or replies. Read-only until the checkpoint.

**Deliverables QC** — fan-out.
- Unit: one exported file from the deliverables matrix.
- Workers run ffprobe and a loudness measurement, compare against the spec sheet
  (resolution, frame rate, duration, codec, audio layout, loudness, captions present) and
  return pass/fail with reasons. Read-only; they never re-encode or overwrite.
- The orchestrator writes one QC report. Checkpoint: the producer before sending.

**Clearance tracking** — pipeline.
- Wave 1, in parallel: scan the script, shot list and the cut's EDL or XML for people,
  locations, logos, artwork, footage and music needing clearance.
- Wave 2: one agent updates the tracker (one row per item, status "needs clearance").
- Checkpoint: the producer or legal marks items cleared. Agents never do.

**Interview-led edit preparation** — fan-out.
- Unit: one interview. Workers transcribe or read the transcript, pull selects by theme
  with timecodes, and note strong moments.
- A synthesiser drafts a paper edit against the brief's story. The editor takes it from there.

**Versioning and social adaptation** — fan-out.
- Unit: one platform or one row of the matrix. Workers write a version brief: length,
  ratio, safe areas, what to cut, supers and caption copy.
- They prepare briefs for editors, not renders.

## Expert roles

Points of view worth making into an agent:

- **Brief guardian** — checks any output against the brief's objective, message and
  mandatories; reports drift. Useful in every team above.
- **Deliverables checker** — knows the spec sheet; reports mismatches, never fixes them.
- **Clearance spotter** — notices what needs permission: faces, brands, art, music, places.
- **Continuity checker** — compares versions or scenes for mismatches in supers, legal
  lines, product shots and end cards.
- **Devil's advocate** — argues against a creative route using the brief and audience, so
  the CD hears the objections before the client does.

## Anti-patterns

- **An agent deciding taste.** Picking the take, the music or the grade. Agents present
  options with reasons; the CD chooses.
- **Agents driving the live edit project.** Parallel agents in one NLE project corrupt it,
  and one agent can break a session the editor is in. Use exported files.
- **Uploading unreleased footage to run an agent.** Breaks embargoes and client contracts.
- **Generative output in the final film without approval and disclosure.** Legal and
  reputational risk; keep it in previs unless the client signs off.
- **Auto-sending to the client.** Every message, share link or upload to the client goes
  through a person.
- **One mega-agent for the whole production.** Stages have different tools, artefacts and
  approvers; build one system per stage.
- **Re-encoding masters to "fix" QC failures.** Generation loss and silent changes; report
  and let a person re-export.
