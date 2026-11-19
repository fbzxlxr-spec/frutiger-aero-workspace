# Frutiger Aero Workspace 3.1

A Node.js + vanilla JavaScript Frutiger Aero desktop with five arcade games, fish care, an audio playlist, and Fishy.

## Included in 3.1
- Preserved the glossy aqua / sky / hill desktop styling.
- Win and loss screens, game sound effects, and a Save Progress button.
- Tic Tac Aero with a stronger single-player opponent.
- Mindsweeper with proper neighbouring counts, safe-square reveals, and right-click flags.
- Fish Aquarium with Classic (10 levels), Timed (30 seconds), and Endless (red bubbles end the run).
- Raise your Fish with an embedded transparent Regal Blue Tang PNG, multiple pets, emotion sounds, feeding, play, and tank cleaning.
- AeroVice City with collectible sunshine orbs.
- Multiplayer rematch voting thresholds: Tic Tac Aero 2, Mindsweeper 3, Fish Aquarium 4, Raise your Fish 5, AeroVice City 6 players.
- Frutiger's Music playlist with the 10 requested track labels. Add an audio file you have permission to use for each track. Uploaded files are kept in this browser on this device using IndexedDB. A built-in synthesized aqua tune is available when no file is selected. The original copyrighted recordings are not bundled.
- Fishy works in local demo mode without a key. For open-ended AI responses, an adult site administrator can configure a server-side OpenAI API key.

## Deploy / update
Upload `server.js`, `package.json`, `index.html`, and `README-3.1.md` to the repository root. `regal-blue-tang.png` is included as a standalone copy of the fish art; the page also embeds it, so the PNG file is not required for runtime. Keep the old Python files if your 2.0 service still uses them. Do not upload `node_modules` or a real `.env` file.

Render settings: Node runtime, blank root directory, build command `npm install`, start command `npm start`.

## Fishy AI and billing
The server uses the OpenAI Responses API and defaults to `gpt-6-luna`. Without `OPENAI_API_KEY`, Fishy replies in local demo mode. An adult account owner should decide whether to configure an API key in the Render service environment. API use is billed separately from a ChatGPT subscription. Never place the key in browser code, GitHub, or chat.

## Notes
Progress and uploaded audio are stored locally in each browser/device. They do not automatically sync across devices. Multiplayer uses temporary in-memory rooms, has no accounts or private-room guarantees, and is a prototype rather than production-grade infrastructure.
