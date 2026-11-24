# Frutiger Aero Workspace 12.3

A feature-preserving visual and asset update based on the supplied Workspace 12.2 project.

## 12.3 update

- Replaced the requested workspace emoji/icon placements with the user's supplied PNG artwork: sunflower default profile picture, Discord logo, Messages emblem, fish artwork, Aero Playlist music disc, controller, MSN Buddy, and settings gear.
- Removed the original image backgrounds and exported the artwork as transparent PNG assets in `assets/`.
- Added the supplied MSN Buddy artwork to the upper-right desktop companion and the assistant/pet presentation.
- Added the fish artwork to the AI companion, interactive pet, aquarium headings, and Feed the Fish heading.
- Added the Messages artwork to every chat log panel.
- Refreshed the Home, Games, Settings, and all twelve Frutiger variant visual treatments with more dimensional glass, reflections, richer lighting, and coordinated palette styling.
- Strengthened delegated tab navigation, active states, and hash-based page restoration.
- Preserved the existing 12.2 apps, game logic, local storage behavior, audio features, community features, and server routes.

## Run locally

Requires Node.js 20 or newer.

```bash
npm install
npm start
```

Open `http://localhost:3000`. The server health endpoint is `/health`.

## Assets

The `assets/` directory contains the transparent user-supplied artwork used by the workspace. The bottom-right blue-marked collage item was not used.

## Validation

All inline JavaScript blocks and `server.js` pass `node --check`. A full interactive browser QA pass is still recommended before public deployment, especially for multiplayer/community behavior.
