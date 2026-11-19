# Frutiger Aero Workspace 2.0

A mobile-friendly, glossy Frutiger Aero-inspired web workspace built with Python, Flask, HTML, CSS and JavaScript.

## What's new
- Retro startup screen reading **WELCOME, DEAR TRAVELER.**
- Glossy aqua gradients, reflections, translucent glass panels and skeuomorphic shadows
- Idea document editor: create, edit, delete, pin and drag sticky-note cards
- Local browser storage for ideas, profile, chat demo, fish count and whiteboard
- Profile picture upload (PNG, JPG or WebP, under 900 KB)
- Interactive fish collecting and feeding
- Bubble-popping mini-game
- Tiny 5×5 Minesweeper
- Focus timer, local clock and browser-generated ambient synth tones
- Responsive layout for phones, tablets and desktop browsers
- Render deployment files included

## Run on Android (Pydroid 3)
1. Extract this ZIP.
2. Open Pydroid 3 and install Flask and Gunicorn from its Pip interface, or run `pip install -r requirements.txt` in its terminal.
3. Open `app.py` in Pydroid 3 and press Run.
4. In Chrome on the same phone, visit `http://127.0.0.1:5000`.

## Publish it so other people can visit
This project includes `render.yaml` and a `Procfile` for deployment on Render.
1. Create a GitHub account if you don't already have one.
2. Create a new repository and upload the files in this folder.
3. Create a Render account and choose **New + → Blueprint**.
4. Connect the GitHub repository containing this project.
5. Render reads `render.yaml`, installs dependencies and deploys the site.
6. When deployment finishes, Render gives you a public `https://...onrender.com` address. Share that address with others.

You can do the GitHub and Render steps from a mobile browser, although a computer is often more convenient. Hosting providers may change their free-plan limits or require a payment method.

## Important storage and collaboration details
- **Ideas and settings use browser localStorage.** They persist after refresh on the same browser/device, but do not automatically sync to other devices or other people's accounts.
- The chat is a local demo, not a real multi-user chat service.
- Fish collection, profile picture, whiteboard and idea cards are currently saved locally in each browser.
- A public URL makes the website reachable worldwide, but it does not make local browser data shared.
- To support true shared accounts, cross-device idea sync, shared fish collections and real-time collaboration, a next version needs user accounts, a database and server-side APIs. Do not store passwords or private information in this prototype.
- Uploaded profile images are stored in localStorage on the current device. Keep images under 900 KB.
- This is a 2D CSS aquatic scene with a 3D-inspired look, not a full 3D engine.

## Troubleshooting
- If Flask is missing: `pip install Flask`
- If the server starts but the page doesn't open, check that the terminal says it is running and use `http://127.0.0.1:5000`.
- Keep the Python app running while you use the local website.
