# Frutiger Aero Workspace 11.0

A feature-rich continuation of the supplied 10.0 workspace. The original games, aquarium, AeroVice City, playlist, profiles, community pages, and startup experience are retained.

## New in 11.0

- Workspace 11.0 Welcome Center and app launcher
- Draggable desktop shortcuts with rename, add, and saved layout
- Enhanced glass styling and six atmosphere presets
- Aero Media Player with local audio-file playlist
- Aero Photo Gallery for local images
- Editable Sticky Notes and a Recycle Bin with restore
- Desktop gadgets: live clock, calendar, optional location-based weather, and browser system monitor
- Interactive aquarium with swimming fish, feeding, and bubbles
- Draggable, rotating illustrated Aero Globe
- Custom startup sound selection, preview, and restore-original option
- Optional idle screensaver and reduced-motion setting
- Welcome Center shortcuts and desktop window controls

## Run locally

Requires Node.js 20 or newer.

```bash
npm install
npm start
```

Open `http://localhost:3000`. The server includes a health endpoint at `/health`.

## Storage and privacy

Notes, photo gallery entries, desktop layout, theme, and startup sound selection are stored in this browser on this device. Photos are limited to 900 KB each and custom startup audio to 3.5 MB to avoid exhausting browser storage. The media player reads audio files locally and does not upload them. Weather is optional: when requested, the browser asks for location permission and queries Open-Meteo for current conditions. Location is not saved by this feature.

The Aero Globe is an illustrative interactive graphic, not a geographic navigation tool. The system monitor reports browser-side metrics only where the browser exposes them.

## Notes

The supplied 10.0 `index.html`, `loading.mp3`, and Finder artwork are retained. This package includes a small Express/Socket.IO server so the supplied Socket.IO client route and existing community features have a server entry point. Test multiplayer/community behavior with your own deployment settings before public launch.
