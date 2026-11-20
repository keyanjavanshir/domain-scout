# Patterns for solo event-film systems

Agent teams that fit the work, by agent-architect's smallest-system levels. Build them in
this order; each earns trust for the next.

## Contents
- Teams
- Expert roles
- Anti-patterns

## Teams

**1. Sparring partner and vision one-pager** — one skill.
- A conversation, not a fan-out. Reads the brief and the person's reference films, pitches
  three angles, gives the strongest objection to the favoured one, then drafts the
  one-pager: intent in two sentences, look and feel, references, music direction (mood,
  tempo range, energy curve), two or three structures, and a shot wishlist per structure.
- Writes `vision.md`. The person edits and approves it; nothing else depends on its format.

**2. Footage-first logging and structures** — pipeline.
- Before the run, the person makes proxies.
- Wave 1, fan-out: one worker per batch of 25–40 proxy clips. For each clip: metadata,
  shot changes, stills (conversion LUT applied), speech transcript, then a description,
  shot type, subject, energy (1–5), faces, and usable moments with timecodes. Each worker
  writes only `log/batch-{item}.md`.
- Wave 2: one merger builds `moments.md` — the event's moments in order, with the
  strongest clips for each.
- Wave 3: one structure writer proposes two or three structures (build → peak → outro, or
  a story following one person or moment), each section naming its clips, plus what is
  missing. Optional: a marker timeline as OpenTimelineIO.
- Checkpoint: the person picks a structure.

**3. Plan-first check** — fan-out, after the shoot.
- The same logging as team 2, then one agent compares the log with the vision's shot
  wishlist: what was got, what was missed, what surprised. Structures are adjusted, not
  reinvented.

**4. Music and sound** — pipeline.
- Wave 1: a music scout searches the licensed library with the structure's mood, tempo
  range and energy curve and returns a shortlist of five to eight tracks with reasons.
  Read-only; the person listens and picks.
- Checkpoint: the chosen track is downloaded by the person.
- Wave 2: a beat mapper finds tempo, beats and the track's sections (intro, build, drop,
  outro) and lines them up with the structure's sections.
- Wave 3: a sound designer writes a cue list from the rough cut: ambience beds, natural
  sound moments to keep, J- and L-cuts, and where risers, whooshes and impacts belong —
  with a note to keep them sparse.

**5. Feedback to change list** — one skill.
- Transcribes voice messages locally, merges them with text messages, matches vague
  references ("the part with the DJ") to timecodes using the log, separates clear changes
  from questions, and flags anything that conflicts with the brief.
- The person answers the questions and makes the changes.

**6. Social versions** — fan-out.
- One worker per platform or length writes a version brief: duration, ratio, hook for the
  first seconds, what to cut, text on screen, safe areas. Briefs, not renders.

## Expert roles

- **Sparring partner** — the missing second creative voice: proposes, objects, offers an
  alternative, and never decides.
- **Assistant editor** — logs, builds selects and moment maps, finds clips on request.
- **Music scout** — knows tempo, mood and energy; searches only licensed libraries.
- **Sound designer** — thinks in layers (ambience, natural sound, effects, music) and in
  restraint.
- **Brief guardian** — checks the vision, the structures and the change list against the
  brief's must-haves.

## Anti-patterns

- **Opening the footage with no intention.** Leads to endless scrubbing; set an intent card
  or run footage-first logging before editing.
- **An agent choosing the structure, the track or the takes.** It ranks; the person picks.
- **Judging log footage without the conversion LUT.** Everything looks dull and
  underexposed; energy and look ratings come out wrong.
- **Logging every clip in one context.** A few hundred clips overflow it; batch and merge.
- **Uploading raw footage or stills to a cloud model to "watch" it.** Slow, costly and a
  breach of the client's trust; work locally.
- **Driving the open editor project with agents.** Use exported files and marker timelines.
- **Effects on every cut, cuts on every beat.** Flattens the energy curve the music gives.
- **Building the visual board or editor integration first.** Prove the plain one-pager and
  the log; add the rest once they are trusted.
