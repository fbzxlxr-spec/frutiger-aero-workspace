# Frutiger Aero Workspace 12.2

A feature-preserving expansion based on the supplied Workspace 12.0.1 source files.

## 12.2 work included

- Added a delegated, keyboard-accessible safety net for the main `[data-page]` tabs, so navigation still works if earlier scripts replace or fail to bind a tab button.
- Unified selection and saved-state restoration for all 12 Frutiger variants, including Four Colors, Helvetica Aqua Aero, Frutiger Aurora, and Frutiger Glacier.
- Added Cube / Ship / Wave mode controls to Aero Dash. Ship is introduced from level 5 and Wave from level 8; the mode icons can be unlocked through dedicated quests, occasional chest bonus drops, level progress, or purchased with Aero coins in the Icon Garage.
- Added distinct Ship and Wave movement and visual forms, hold-to-fly / hold-to-wave controls, mobile pointer support, and more forgiving central collision boxes.
- Reworked Bubble Pop Blitz into a timed bubble-target game with moving targets, bonus bubbles, hazards, combo scoring, and touch support.
- Reworked Cloud Catcher into a basket-catching game with moving sunshine drops, storm hazards, combo scoring, and pointer/touch movement.
- Added visible keyboard focus styling and reduced-motion-aware tab scrolling.

## Run locally

Requires Node.js 20 or newer.

```bash
npm install
npm start
```

Open `http://localhost:3000`. The server health endpoint is `/health`.

## Validation notes

All 13 inline JavaScript blocks pass `node --check`, and `server.js` passes `node --check`. A full interactive browser QA pass was not completed in this environment, so please test the complete game flow and community features on your deployment before announcing the release. The project retains the supplied assets and original source content.
