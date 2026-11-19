# Frutiger Aero Workspace 4.0

A Node.js + Express + Socket.IO Frutiger Aero desktop.

## Deploy on Render
- Runtime: Node
- Root Directory: leave blank
- Build Command: `npm install`
- Start Command: `npm start`
- Node: 20 or newer

## Workspace 4.0 additions
- Four visual variants: Frutiger Aero (original look), DORfic, Eco, and Aqua. The selection is saved locally.
- General Chat public lounge using Socket.IO, with basic filtering, reporting, and temporary in-memory messages.
- Fan Art gallery with PNG/JPG/WebP uploads up to 1.5 MB, basic reporting, and temporary in-memory posts.
- Local profile name, built-in avatars, and custom avatar upload.
- Two new standalone arcade games: Bubble Pop Blitz and Cloud Catcher.
- Bubble-pop sound effects and a victory fanfare.
- Fishy defaults to `gpt-4.1-mini` with the OpenAI Responses API.

## Important limitations and safety
- Chat and fan art are public to visitors, not private. Do not post personal details. Reporting hides content after multiple reports, but this is not a substitute for active human moderation. An adult administrator should supervise a school community and remove the public chat/gallery if moderation cannot be provided.
- Chat and gallery posts are held in server memory and clear on restart or redeploy. They are not permanent or account-authenticated.
- Profiles and custom avatars are local to each browser/device, not shared accounts.
- The server has no real user identity system. Nicknames are not verified.
- Fishy requires an adult-managed `OPENAI_API_KEY` in Render Environment. Never put the key in browser code, GitHub, or this ZIP. Add it in Render's Environment settings. The default model is `gpt-4.1-mini`; it can be overridden with `OPENAI_MODEL`.
- Basic chat filters are not perfect moderation. For a school deployment, add adult moderation and clear community rules before inviting students.
