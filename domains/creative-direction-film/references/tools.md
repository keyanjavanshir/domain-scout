# Tools for film and video work

Checked 2026-11-20 against the official MCP registry
(`registry.modelcontextprotocol.io`) and vendor documentation. "Unofficial" means a
community server not published by the vendor; review its code before using it.

## Contents
- Review and approval
- Editing, grading and motion
- Pre-production and planning
- Storage and transfer
- Audio and music
- Generative and previs
- Command-line utilities
- How these tools behave for agents

## Review and approval

| Tool | Used for | Integration | Auth | Checked |
|---|---|---|---|---|
| Frame.io (V4) | Review and approval, timecoded comments, versions, sharing | Official remote MCP server (public beta, V4 accounts only) at `https://mcp.frame.io/v1/mcp`; REST API V4. Not listed in the MCP registry. | OAuth (Adobe account) | vendor docs 2026-11-20 |
| Vimeo | Hosting, private review links | Unofficial: `dev.cotlet/vimeo`, `io.github.pipeworx-io/vimeo`; REST API | OAuth or access token in `${VIMEO_TOKEN}` | registry 2026-11-20 |

## Editing, grading and motion

| Tool | Used for | Integration | Auth | Checked |
|---|---|---|---|---|
| Adobe Premiere Pro | Editing | Unofficial local servers: `io.github.leancoderkavy/premiere-pro`, `io.github.Immersive-Media-Technologies/premiere-mcp-imt`; exports EDL, XML, AAF | local app | registry 2026-11-20 |
| DaVinci Resolve | Editing, grading, finishing | Unofficial local servers: `io.github.Aedelon/davinci-mcp` and others, through Resolve's scripting API; entries disagree on free-edition support | local app | registry 2026-11-20 |
| Adobe After Effects and Creative Cloud | Motion graphics, compositing | Unofficial: `io.github.AJSMonty/adobe-mcp` | local app | registry 2026-11-20 |
| Final Cut Pro, Avid Media Composer | Editing | none found; use FCPXML or AAF/EDL exports | local app | registry 2026-11-20 |

## Pre-production and planning

| Tool | Used for | Integration | Auth | Checked |
|---|---|---|---|---|
| Figma / FigJam | Mood boards, frame layouts, title and super design | Official: `com.figma.mcp/mcp` (remote) | OAuth | registry 2026-11-20 |
| Boords | Storyboards, animatics, shot lists | Public REST API (beta, paid plans) at `https://app.boords.com/v1`, webhooks; no MCP server found | API key in `${BOORDS_API_KEY}` | vendor docs 2026-11-20 |
| StudioBinder | Shot lists, call sheets, schedules | none found; PDF and spreadsheet export | — | vendor site 2026-11-20 |
| Celtx | Scripts, breakdowns, scheduling | none found | — | unverified |
| Notion | Production bibles, trackers, treatments | Official: `com.notion/mcp` (remote) | OAuth | registry 2026-11-20 |
| Airtable | Clearance, version and deliverables trackers | Official: `com.airtable/mcp` (remote) | OAuth | registry 2026-11-20 |

## Storage and transfer

| Tool | Used for | Integration | Auth | Checked |
|---|---|---|---|---|
| Dropbox | Footage and file transfer | Registry lists only unofficial servers; an official remote server at `mcp.dropbox.com` is reported by secondary sources | OAuth | unverified |
| Google Drive | Documents, decks, small media | none official found in the registry; some harnesses ship a built-in connector | OAuth | registry 2026-11-20 |

## Audio and music

| Tool | Used for | Integration | Auth | Checked |
|---|---|---|---|---|
| ElevenLabs | Scratch voice-over, temp voices, dubbing tests | Official: `io.elevenlabs/mcp` (remote) | API key in `${ELEVENLABS_API_KEY}` | registry 2026-11-20 |
| Music libraries (e.g. Artlist, Musicbed, Epidemic Sound) | Licensed library music | none checked; licence terms differ per track and per project | account | unverified |

## Generative and previs

| Tool | Used for | Integration | Auth | Checked |
|---|---|---|---|---|
| Runway and similar video models | Previs, concept frames, temp shots | Unofficial: `io.github.mindstone/mcp-server-runway` | API key in `${RUNWAY_API_KEY}` | registry 2026-11-20 |

## Command-line utilities

| Tool | Used for | Integration | Auth | Checked |
|---|---|---|---|---|
| ffmpeg / ffprobe | Reading technical metadata, making proxies, measuring loudness (`ebur128` filter) | CLI | none | not re-checked |
| MediaInfo | Technical metadata reports | CLI | none | not re-checked |

## How these tools behave for agents

- **Editing and grading apps are desktop programs.** Their MCP servers run locally and
  control the project that is open. That is write access to the team's live work: start
  read-only, work on a duplicated project, and never let two agents drive the same app.
- **Interchange files are the safer integration.** EDL, XML, AAF, FCPXML, transcripts and
  caption files can be read and written without touching the open project.
- **Cloud review tools sit behind OAuth.** Comments are easy to read; replies and shares
  are visible to the client, so they need a checkpoint.
- **Footage is large and confidential.** Agents work from metadata, proxies and stills, and
  never copy camera originals to new services.
- **Many creative tools have no API.** Shot-list and scheduling apps often export only PDF
  or spreadsheets; plan around exports or a tracker the team already uses.
