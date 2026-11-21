# Frutiger Aero Workspace 8.2

A best-effort 8.2 rebuild based on the available Workspace 5.3 archive, with documented Workspace 8.0/8.1 additions retained where the source archive already contains them. This is not a byte-for-byte continuation of the unavailable 8.1 Fixed archive.

## What's included

- Existing Workspace 5.3 desktop, Settings, games, community features, aquarium, AeroVice City, Aero Dash, playlist, profile and visual variants are preserved.
- Reworked startup overlay with the bundled `loading.mp3`, an autoplay attempt on page load, and a first-interaction fallback for browsers that block autoplay.
- “Welcome to the 2000s.” appears in large Times New Roman and fades in after the startup audio finishes.
- Settings and its controls are layered above decorative bubbles and fish so the effects do not cover or intercept the interface.
- Removes source-preview/code-display elements from Settings without removing executable application code.
- Refined bubble-pop sound effect.
- Version metadata updated to 8.2.0.

## Run locally

- Install Node.js 20 or newer.
- Run `npm install`.
- Run `npm start`.
- Open the local address printed by the server.

## Deploy to Render

- Runtime: Node
- Build command: `npm install`
- Start command: `npm start`

Keep private keys in the hosting provider's environment settings. Do not put secrets in browser code or commit them to GitHub.

## Important rebuild note

The original `Frutiger-Aero-Workspace-8.1-Fixed.zip` was not available in the current workspace, so this archive was reconstructed from the available 5.3 ZIP and the documented later-version requirements. If a feature from 8.1 is missing, we can carry it forward into a 9.0 build once that exact 8.1 archive becomes available.
