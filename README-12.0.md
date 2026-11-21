# Frutiger Aero Workspace 12.0

A feature expansion of the supplied Workspace 11.0 project. The existing site structure, games, aquarium, AeroVice City, original ten-track Aero Playlist, community pages, profile, and Macintosh startup experience are retained.

## What's new in 12.0

- Reorganized the 11.0 apps: Aero Media Player is placed above the original ten-song Aero Playlist; the remaining 11.0 applications and desktop tools are on Home.
- Personalization & Start Up controls are in Settings. The duplicate Desktop Atmosphere selector is removed; Frutiger Variants remain the visual-world selector.
- Four additional variants: Four Colors, Helvetica Aqua Aero, Frutiger Aurora, and Frutiger Glacier. These are community-style interpretations, not official standardized palettes.
- Home Notification Center with local reminders and dismiss/read states.
- Interactive MSN Buddy / Fishy desktop pet with reactions, plus a Disable option in Settings.
- Universal Search for workspace pages, apps, settings, music tracks, and external web search.
- Personalization Center for accent color, glass transparency, animation level, and window style.
- Accessibility controls for reduced motion, text scaling, and higher contrast.
- System Information panel for browser/platform, screen size, approximate localStorage usage, and browser-exposed JS heap metrics.
- Loop choices for the local Aero Media Player: current song or player playlist.
- Variant-aware Victory and Game Over overlay styling, with separate win/loss states and corresponding sound effects.

## Run locally

Requires Node.js 20 or newer.

```bash
npm install
npm start
```

Open `http://localhost:3000`. The server health endpoint is `/health`.

## Storage and privacy

Workspace preferences, notifications, pet selection, and existing local game/profile data are stored in the browser on this device. The media player reads local audio files in the browser; it does not upload them. Weather remains optional and only uses location permission when the user requests it. System information is approximate and limited to what the browser exposes.

## Compatibility notes

Use a current Chromium-based browser, Firefox, or Safari. Audio playback may require a user gesture. Browser storage limits vary by device. The project includes the original 11.0 assets and Express/Socket.IO server. Test multiplayer/community behavior with your deployment settings before public launch.

The original ten-track playlist's built-in synthesized tracks use a 60-second listening cycle for the loop selector; user-supplied audio files use their actual audio end event. The separate Aero Media Player loops its current file or advances through the selected local-file playlist.
