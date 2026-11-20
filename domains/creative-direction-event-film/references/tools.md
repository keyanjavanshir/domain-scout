# Tools for solo event-film work

Checked 2026-11-20 against the official MCP registry
(`registry.modelcontextprotocol.io`) and vendor documentation. "Unofficial" means a
community server not published by the vendor; review its code before using it.

## Contents
- Editing and interchange
- Footage analysis (local)
- Music and sound effects
- Vision, delivery and feedback
- How these tools behave for agents

## Editing and interchange

| Tool | Used for | Integration | Auth | Checked |
|---|---|---|---|---|
| Adobe Premiere Pro | Editing | OpenTimelineIO import and export (released after a public beta); FCP7 XML; unofficial local MCP servers exist (see creative-direction-film) | local app | vendor forum 2026-11-20 |
| DaVinci Resolve | Editing, grading | OpenTimelineIO import and export; scripting API; unofficial local MCP servers | local app | secondary 2026-11-20 |
| OpenTimelineIO | Writing a proposed structure as a timeline with markers to import into the editor | Python library with adapters (FCP7 XML via plugins) | none | docs 2026-11-20 |

## Footage analysis (local)

| Tool | Used for | Integration | Auth | Checked |
|---|---|---|---|---|
| ffmpeg / ffprobe | Clip metadata, still frames, applying a conversion LUT to stills (`lut3d` filter), audio extraction | CLI | none | not re-checked |
| PySceneDetect | Finding shot changes inside long clips | CLI `scenedetect` and Python library | none | docs 2026-11-20 |
| Whisper (local: faster-whisper, whisper.cpp) | Transcribing speech in clips and voice messages | CLI or Python; unofficial MCP servers: `io.github.OrihuelaConde/local-whisper-mcp`, `io.github.ZahiriNatZuke/whisper-transcribe-mcp` | none (local) | registry 2026-11-20 |
| librosa | Tempo and beat positions of a chosen track (`beat_track`; `plp` for changing tempo) | Python library | none | docs 2026-11-20 |
| Panasonic V-Log to V-709 LUT | Converting V-Log / V-Log L stills to a normal image before judging them | Official LUT download from Panasonic support; also built into Lumix cameras as `Vlog_709` | none | vendor docs 2026-11-20 |

## Music and sound effects

| Tool | Used for | Integration | Auth | Checked |
|---|---|---|---|---|
| Epidemic Sound | Licensed music and sound effects; search by mood, BPM, genre, key or a reference track | Official: `com.epidemicsound/mcp-server` (remote, beta); also a REST API | OAuth (account) or MCP API key in `${EPIDEMIC_SOUND_API_KEY}`; downloads need a paid subscription | registry and vendor docs 2026-11-20 |
| Artlist | Licensed music and sound effects | none found | account | registry 2026-11-20 |
| Musicbed, Soundstripe | Licensed music | none found | account | registry 2026-11-20 |

## Vision, delivery and feedback

| Tool | Used for | Integration | Auth | Checked |
|---|---|---|---|---|
| Plain Markdown or text document | The vision one-pager, logs, structures, change lists | Files on disk | none | not applicable |
| Figma / FigJam | A visual mood board, later | Official: `com.figma.mcp/mcp` (remote) | OAuth | registry 2026-11-20 |
| SwissTransfer, WeTransfer | Sending cuts and masters to the client | none found; the person uploads | — | registry 2026-11-20 |

## How these tools behave for agents

- **Everything heavy runs locally.** Stills, scene detection, transcription and beat
  tracking need no cloud service, which keeps footage private and costs nothing per run.
- **Agents cannot watch video.** They read still frames, transcripts, audio features and
  metadata. A log is only as good as the stills sampled: take several per clip, more for
  long clips, and one per detected shot change.
- **Log footage must be converted first.** Judge exposure, colour and mood on stills with
  the conversion LUT applied; leave the proxies and originals untouched.
- **Interchange files survive editor changes.** A structure written as OpenTimelineIO or
  FCP7 XML with markers imports into Premiere and Resolve. Test the round trip on your own
  versions; one user reported a Premiere-exported OTIO file that Resolve rejected until a
  `file://` prefix was removed.
- **Music search is the only outside call.** It sends text queries, not media. Downloading
  and licensing tracks is done by the person.
