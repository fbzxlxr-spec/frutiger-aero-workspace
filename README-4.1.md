# Frutiger Aero Workspace 4.1 — Vista Aero Edition

Workspace 4.1 keeps the Workspace 4.0 application and server behavior while refreshing the visual layer with a Windows Vista / Windows 7 Aero-inspired treatment.

## What's new
- Translucent Aero glass surfaces with stronger blur, layered highlights, and beveled edges.
- Vista-inspired title bars and minimize / maximize / close-style controls.
- Glossy, two-tone buttons and polished input fields.
- Glassy cards, chat panels, game canvases, and startup screen.
- Theme-aware visual treatments for Frutiger Aero, DORfic, Eco, and Aqua.

## Preserved Workspace features
- Home page and Fishy assistant.
- Five arcade games and their existing game logic.
- Music player and aquarium.
- General Chat and Fan Art.
- Local profile and avatar settings.
- Four Frutiger variants and their saved selection.
- Existing Express / Socket.IO server and API routes.

## Deploy on Render
- Runtime: Node
- Root Directory: leave blank
- Build Command: `npm install`
- Start Command: `npm start`
- Node: 20 or newer

## Important notes
- This is a visual refresh of Workspace 4.0, not a replacement with the separate reference app.
- General Chat and Fan Art remain public features. Do not post private details. Adult moderation is recommended for a school community.
- Fishy requires an adult-managed `OPENAI_API_KEY` in Render Environment. Never put the key in browser code, GitHub, or this ZIP.
- The Gemini-provided HTML was used as a visual reference for the Vista glass, window chrome, glossy buttons, and desktop aesthetic. Its separate app logic and demo apps were not copied into Workspace.
