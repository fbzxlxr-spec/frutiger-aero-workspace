# Frutiger Aero Workspace 12.6

Workspace 12.6 builds on the supplied 12.4 project and keeps its existing pages, navigation, aquarium, profile, chats, playlist, desktop tools, and arcade code.

## Run locally

Requirements: Node.js 20 or newer.

```bash
npm install
npm start
```

Open `http://localhost:3000`.

## Accounts and guest mode

- Visitors can continue as guests. Guest preferences and progress remain in that browser on that device.
- Workspace accounts use a username and password. Passwords are stored as salted scrypt hashes, never as plain text.
- When signed in through the Node server, supported localStorage workspace preferences are synchronized to `data/accounts.json`.
- The account file contains private user data. Keep it out of public source-control repositories and configure persistent private storage on your host.
- Sessions are held by the running server process; users may need to sign in again after a server restart.
- Google, Gmail, iPhone/Apple ID, Yahoo, and Opera buttons are shown in the sign-in screen. Actual third-party sign-in requires OAuth client credentials, redirect/callback URLs, and provider configuration from the site owner. The buttons explain this rather than pretending to authenticate users. Gmail uses Google's identity provider.
- This project does not collect or store users' Google, Apple, Yahoo, or Opera passwords.

## User-supplied art

The five supplied background images are copied byte-for-byte into `assets/` and assigned to Frutiger Aero, Eco, DORfic, Aqua, and Metro. They are displayed edge-to-edge without cropping. The eight existing icon PNGs from 12.4 are preserved byte-for-byte; their transparent alpha channels are kept intact.

## Screensavers

Screensavers can be switched on/off, set to follow the active variant, or explicitly set to Aero, Eco, DORfic, Aqua, or Metro. The default is On and follows the selected desktop variant. The inactivity delay is configurable.

## Arcade

Bubble Blitz and Cloud Catcher have ten selectable stages, an Aero Dash-style HTML level HUD, score goals, unlock progress, and the existing bubble-pop / sunshine-catching gameplay.

## Fonts

The existing font options remain. Ten more are added: Type writer, Italic, Empire, Helvetica, Arial, Georgia, Verdana, Courier New, Futura, and Ceveat.

## Tests

Run the static checks:

```bash
npm test
```

The smoke test expects the server to be running at `http://localhost:3000` (or set `WORKSPACE_URL`). It checks the health endpoint, HTML page, all five background images, and the eight icon assets.
