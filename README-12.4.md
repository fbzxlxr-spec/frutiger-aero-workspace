# Frutiger Aero Workspace 12.4

A feature-preserving repair release based on the supplied Workspace 12.2 project.

## 12.4 repairs

- Reintegrated the supplied artwork using stable, relative `assets/` URLs.
- Corrected the MSN Buddy image mapping: the green-and-blue two-person artwork is used for the desktop buddy. The separate Finder face remains separate.
- Removed the remaining backgrounds from the Settings gear and MSN Buddy artwork while preserving their original appearance.
- Added the sunflower as the default profile picture when no custom picture or non-default avatar is selected.
- Added the supplied Discord, Messages, Fish, Music, and Controller artwork to their requested locations.
- Added Messages artwork to every chat window titlebar.
- Repaired delegated tab navigation and made dynamically inserted navigation controls work.
- Fixed the startup overlay so a blocked or unavailable startup sound cannot leave the overlay covering the workspace forever.
- Retained the supplied 12.2 content, games, audio, server, and project structure.

## Run locally

Requires Node.js 20 or newer.

```bash
npm install
npm start
```

Open `http://localhost:3000`.

## Asset files

The eight supplied transparent PNGs are in `assets/`:
`sunflower.png`, `settings.png`, `msn-buddy.png`, `controller.png`, `fish.png`, `messages.png`, `discord.png`, and `music.png`.

The separate `finder-icon.png` supplied with the project is not repurposed as the MSN Buddy.

## Validation

JavaScript syntax, local image loading, navigation clicks, and the startup-overlay fallback were tested in a Chromium browser harness. The Socket.IO multiplayer/community experience still needs a full two-client test against a deployed server.


## QA

See `QA-12.4.md` for the checks completed and the remaining multiplayer/device checks.
