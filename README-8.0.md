# Workspace 8.1 • Vista Aero Edition

Workspace 8.0 is built on the supplied Workspace 5.3 package. It preserves the 5.3 app and server, then adds the new visual and gameplay upgrades described in README.md.

## Deploying

- Runtime: Node
- Build command: `npm install`
- Start command: `npm start`

Keep API keys in the hosting provider's private environment settings. Do not put secrets in the HTML, ZIP, or GitHub repository.

## Notes

Aero Dash offers 22 level cards; the first 10 are playable and the other 12 are marked as coming soon. Aero Dash icons, quest progress, coin rewards, and chest timers are stored in the local browser. The playlist wallpaper is bundled locally and works offline.


## Workspace 8.0 notes
- Based on the supplied Workspace 5.3 source.
- Includes a local Frutiger Aero landscape asset for Aero Playlist and a Macintosh-style Finder startup screen.
- Adds a Discord invite tile, themed variant atmosphere refresh, shared result overlay hooks, Fish Aquarium Classic/Timed/Endless HUD with 10 Classic levels and a bubble quest, original synthesized music for Aero Dash and AeroVice City, and a custom city audio picker.
- No external copyrighted music tracks are bundled.


## Workspace 8.1 startup and audio fixes
- Fixed the startup overlay hidden state so the completed boot screen can fade away reliably.
- Removed the old click-to-play Macintosh startup sound handlers. The startup sound now attempts to play after the full page load, with a first-interaction fallback for browsers that block autoplay.
- The final welcome message fades in using Times New Roman.
- Replaced the flat click effect with a short filtered-noise and pitch-drop bubble pop, and removed duplicate background-click playback.
- Added a timeout fallback so a delayed page resource cannot trap the workspace on the startup screen.
