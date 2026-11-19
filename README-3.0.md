# Frutiger Aero Workspace 3.0 (upload bundle)

This bundle contains a single self-contained `index.html` (all images embedded), plus a small Node.js server. The canvas games use vanilla JavaScript and draw their game art themselves.

## Included
- Windows 98-inspired startup screen: “Welcome, traveler.”
- Rich aqua/sky/hill/glass desktop and MSN Messenger-inspired buddy.
- Fishy, a Regal Blue Tang assistant PNG embedded in the page.
- Five games: Tic Tac Aero!, Mindsweeper, Fish Aquarium, Raise your Fish!, and AeroVice City.
- MENU, PLAY and GAMEOVER states, restart/pause, scoring, single-player play, temporary Socket.IO multiplayer rooms and per-game chat.
- Fish Aquarium collection saved in the current browser.
- Frutiger's Music with ten original synthesized soundscapes. The named commercial/game tracks are not bundled.
- Optional Fishy AI backend proxy using the OpenAI Responses API. The key remains server-side.

## Upload to your existing GitHub repository
Upload these files to the repository root: `server.js`, `package.json`, and `index.html`. You may also upload `.env.example`, `.gitignore`, and this README. Keep your old Python files and old Render service in place; they are not needed by the new Node service but can remain. Do not upload `node_modules` or a real `.env` file.

## Create a separate Render service
1. Choose **New + → Web Service**, not Blueprint.
2. Connect the same GitHub repository and choose branch `main`.
3. Runtime/language: **Node**. Root Directory: blank.
4. Build command: `npm install`. Start command: `npm start`.
5. Choose Free compute if available. The old Python site remains separate and is not replaced.

## Fishy AI (optional)
Without a server API key, the site works in demo mode. To enable AI replies, a parent/guardian or other adult account owner should decide whether to configure `OPENAI_API_KEY` in the Render service environment. API usage is billed separately from a ChatGPT subscription and may cost money. Never put an API key in the HTML, GitHub source, or chat. Optional `OPENAI_MODEL` defaults to `gpt-6-luna`. The backend uses `POST https://api.openai.com/v1/responses`.

## Limitations
Multiplayer rooms are temporary and stored in memory; there are no accounts, private rooms, persistent leaderboards, or full anti-cheat protections. Do not treat room chat as private. The game implementation is a fun prototype, not a production multiplayer platform.
