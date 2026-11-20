import express from 'express';
import http from 'node:http';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { Server } from 'socket.io';
import helmet from 'helmet';
import rateLimit from 'express-rate-limit';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const app = express();
const server = http.createServer(app);
const io = new Server(server, { cors: { origin: false }, maxHttpBufferSize: 2.2e6 });
const PORT = Number(process.env.PORT || 3000);

app.use(helmet({ contentSecurityPolicy: false }));
app.use(express.json({ limit: '3mb' }));
app.get('/', (_req, res) => res.sendFile(path.join(__dirname, 'index.html')));
app.get('/index.html', (_req, res) => res.sendFile(path.join(__dirname, 'index.html')));
app.get('/health', (_req, res) => res.json({ ok: true, service: 'Frutiger Aero Workspace 4.0' }));

const chatLimiter = rateLimit({ windowMs: 60_000, limit: 12, standardHeaders: 'draft-7', legacyHeaders: false });
app.post('/api/fishy', chatLimiter, async (req, res) => {
  const message = typeof req.body?.message === 'string' ? req.body.message.trim() : '';
  const history = Array.isArray(req.body?.history) ? req.body.history.slice(-8) : [];
  if (!message || message.length > 1200) return res.status(400).json({ error: 'Please enter a message under 1,200 characters.' });
  if (!process.env.OPENAI_API_KEY) { const lower = message.toLowerCase(); let reply = 'Blub! I am in demo mode right now. I can still help with the Workspace buttons, games, aquarium care, and basic navigation. An adult site administrator can connect the AI service for open-ended answers.'; if (/hello|hi\b|hey/.test(lower)) reply = 'Hello, traveler! 🐠 Welcome back to the aqua desktop. What are we exploring today?'; else if (/save|progress/.test(lower)) reply = 'Press Save Progress! at the top of the Arcade. Your local game and fish-care progress will be stored in this browser.'; else if (/fish|aquarium|tank/.test(lower)) reply = 'Keep your fish fed, clean the tank when it gets dirty, and collect bubbles to adopt more fish. Happy fish make happy bubbles!'; else if (/music|song|playlist/.test(lower)) reply = 'Open Frutiger’s Music, choose Add audio beside a track, select an audio file you have permission to use, then press Play.'; else if (/game|arcade/.test(lower)) reply = 'Visit Aero Arcade, choose a game, and press Start. Fish Aquarium has Classic, Timed, and Endless modes.'; return res.json({ reply, mode: 'demo' }); }

  try {
    const input = history
      .filter(item => item && ['user', 'assistant'].includes(item.role) && typeof item.content === 'string')
      .map(item => ({ role: item.role, content: item.content.slice(0, 1200) }));
    input.push({ role: 'user', content: message });
    const response = await fetch('https://api.openai.com/v1/responses', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${process.env.OPENAI_API_KEY}` },
      body: JSON.stringify({
        model: process.env.OPENAI_MODEL || 'gpt-4.1-mini',
        instructions: 'You are Fishy, a cheerful, age-appropriate Regal Blue Tang fish assistant inside a nostalgic Frutiger Aero desktop. Be kind, concise, safe for younger users, and never ask for private information. Do not encourage dangerous activities. You can help with the website, games, and general questions.',
        input
      })
    });
    const data = await response.json();
    if (!response.ok) return res.status(502).json({ error: 'Fishy could not reach the AI service. Please try again later.' });
    return res.json({ reply: data.output_text || 'Blub! I could not find a reply that time.' });
  } catch (error) {
    console.error('Fishy API error:', error.message);
    return res.status(500).json({ error: 'Fishy had a little connection wobble. Please try again.' });
  }
});

const rooms = new Map();
const roomStates = new Map();
const rematchVotesByRoom = new Map();
const rematchRequirements = { 'Tic Tac Aero!': 2, 'Mindsweeper': 3, 'Fish Aquarium': 4, 'Raise your Fish!': 5, 'AeroVice City': 6 };
function safeRoom(value) { return String(value || '').toUpperCase().replace(/[^A-Z0-9]/g, '').slice(0, 8) || 'AERO'; }

// Workspace 4.0 community features. These in-memory collections reset on server restart.
const communityMessages = [];
const fanArtPosts = [];
const reportCounts = new Map();
const communityBlocked = new Map();
let communityId = 0;
const blockedPatterns = [/(?:\b\d{3}[-. ]?\d{3}[-. ]?\d{4}\b)/i, /\b(?:address|home address|school name|password)\s*[:=]/i, /\b(?:kill yourself|kys|slur-placeholder)\b/i];
function cleanCommunityText(value, max=240) { return String(value || '').replace(/[<>]/g, '').replace(/\s+/g, ' ').trim().slice(0,max); }
function communitySafe(text) { return !blockedPatterns.some(re => re.test(text)); }
function emitNotice(socket, text) { socket.emit('community:notice', text); }

io.on('connection', socket => {

  socket.emit('community:history', communityMessages.slice(-60));
  socket.emit('art:history', fanArtPosts.slice(-30));
  socket.on('community:send', payload => {
    const now = Date.now();
    if ((communityBlocked.get(socket.id) || 0) > now) return emitNotice(socket, 'Chat is temporarily paused for this connection.');
    const nick = cleanCommunityText(payload?.nick,18) || 'Traveler';
    const text = cleanCommunityText(payload?.text,240);
    if (!text) return;
    if (!communitySafe(text)) { communityBlocked.set(socket.id, now + 60_000); return emitNotice(socket, 'That message was blocked to protect personal information and keep chat respectful.'); }
    const msg = { id: String(++communityId), nick, text, at: now };
    communityMessages.push(msg); if (communityMessages.length > 100) communityMessages.shift();
    io.emit('community:message', msg);
  });
  socket.on('community:report', payload => {
    const id = String(payload?.id || ''); if (!id) return;
    reportCounts.set('chat:'+id, (reportCounts.get('chat:'+id) || 0) + 1);
    const msg = communityMessages.find(m => m.id === id);
    if (msg && reportCounts.get('chat:'+id) >= 3) { communityMessages.splice(communityMessages.indexOf(msg),1); io.emit('community:remove', { id }); }
  });
  socket.on('art:submit', payload => {
    const title = cleanCommunityText(payload?.title,48), artist = cleanCommunityText(payload?.artist,18) || 'Traveler';
    const data = typeof payload?.data === 'string' ? payload.data : '';
    if (!title || !/^data:image\/(png|jpeg|webp);base64,[A-Za-z0-9+/=]+$/.test(data) || data.length > 2_100_000) return emitNotice(socket, 'Artwork upload rejected. Use a PNG, JPG, or WebP under 1.5 MB.');
    if (!communitySafe(title) || !communitySafe(artist)) return emitNotice(socket, 'That title or artist name could expose private information.');
    const post = { id: String(++communityId), title, artist, data, at: Date.now() };
    fanArtPosts.push(post); if (fanArtPosts.length > 30) fanArtPosts.shift();
    io.emit('art:new', post); emitNotice(socket, 'Artwork added to the temporary gallery.');
  });
  socket.on('art:report', payload => {
    const id = String(payload?.id || ''); if (!id) return;
    reportCounts.set('art:'+id, (reportCounts.get('art:'+id) || 0) + 1);
    const post = fanArtPosts.find(p => p.id === id);
    if (post && reportCounts.get('art:'+id) >= 3) { fanArtPosts.splice(fanArtPosts.indexOf(post),1); io.emit('art:remove', { id }); }
  });

  socket.on('room:join', ({ room, game, nickname } = {}) => {
    const roomId = safeRoom(room);
    const gameId = String(game || 'lobby').slice(0, 32);
    const nick = String(nickname || 'Traveler').replace(/[<>]/g, '').slice(0, 18) || 'Traveler';
    const key = `${roomId}:${gameId}`;
    socket.join(key);
    socket.data.roomKey = key;
    socket.data.nick = nick;
    if (!rooms.has(key)) rooms.set(key, new Set());
    rooms.get(key).add(socket.id);
    io.to(key).emit('room:presence', { count: rooms.get(key).size, nickname: nick });
    socket.emit('room:joined', { room: roomId, game: gameId, count: rooms.get(key).size });
    if (roomStates.has(key)) socket.emit('game:state', roomStates.get(key));
  });
  socket.on('game:state', payload => {
    const key = socket.data.roomKey;
    if (!key || !payload || typeof payload !== 'object') return;
    roomStates.set(key, payload);
    socket.to(key).emit('game:state', payload);
  });
  socket.on('game:chat', payload => {
    const key = socket.data.roomKey;
    if (!key) return;
    const text = String(payload?.text || '').trim().slice(0, 240);
    if (!text) return;
    io.to(key).emit('game:chat', { nickname: socket.data.nick || 'Traveler', text, at: Date.now() });
  });
  socket.on('rematch:vote', payload => {
    const key = socket.data.roomKey;
    if (!key) return;
    const gameId = String(payload?.game || '').slice(0, 32);
    if (!key.endsWith(':' + gameId)) return;
    if (!rematchVotesByRoom.has(key)) rematchVotesByRoom.set(key, new Set());
    const votes = rematchVotesByRoom.get(key);
    votes.add(socket.id);
    const required = rematchRequirements[gameId] || 2;
    const roomCount = rooms.get(key)?.size || 0;
    io.to(key).emit('rematch:count', { votes: votes.size, required, players: roomCount });
    if (votes.size >= required && roomCount >= required) {
      votes.clear();
      roomStates.delete(key);
      io.to(key).emit('rematch:start', { game: gameId });
    }
  });
  socket.on('disconnect', () => {
    const key = socket.data.roomKey;
    if (!key || !rooms.has(key)) return;
    rooms.get(key).delete(socket.id);
    const count = rooms.get(key).size;
    rematchVotesByRoom.get(key)?.delete(socket.id);
    if (!count) { rooms.delete(key); roomStates.delete(key); rematchVotesByRoom.delete(key); }
    else io.to(key).emit('room:presence', { count });
  });
});

server.listen(PORT, '0.0.0.0', () => console.log(`Frutiger Aero Workspace 3.0 listening on ${PORT}`));
