# Frutiger Aero Workspace 3.2

A Node.js/Express Frutiger Aero desktop-style website.

## Deploy on Render
- Runtime: Node
- Root Directory: leave blank
- Build Command: `npm install`
- Start Command: `npm start`
- Branch: `main`

Keep your existing 3.1 Render service and repository history. Upload/replace the files in this 3.2 package in the NEW 3.2 GitHub repository (or a separate branch/repository), then deploy the new service. Do not upload `node_modules` or a real `.env` file.

## 3.2 updates
- Settings tab with Sound Effects, Music, Graphics, Profile Visibility, and Fonts controls. Settings apply immediately and are saved in this browser.
- Audio test tone in Settings. Audio playback begins only after a user gesture, as required by mobile browsers.
- Music playlist can be renamed. Import an audio file into a track with its Import audio button. Imported files are saved in browser IndexedDB on that device/browser. They do not sync to other devices. Track titles are labels only; no copyrighted recordings are bundled.
- Aquarium page visibly offers Classic (10 levels), Timed (30 seconds), and Endless (avoid red bubbles). Selecting a mode carries into the Aquarium arcade game.
- Arcade start/restart handler is reinforced and game state feedback is explicit.

## Notes and limitations
- Profile Visibility is currently a local preference display only. Public profiles require a real account/profile backend and are not shared by this prototype.
- Graphics quality changes visual effects, not game rendering resolution.
- Frutiger uses Trebuchet MS as a broadly available fallback. Permanent Marker loads from Google Fonts when internet access is available, then falls back to cursive.
- Music imports are local to one browser profile/device. Choose audio files you have permission to use.
- Multiplayer is a lightweight room prototype, not private chat or persistent accounts.
- Fishy AI requires an adult-managed API key in the server environment. Never place API keys in browser code or GitHub.
