import express from 'express';
import helmet from 'helmet';
import rateLimit from 'express-rate-limit';
import { createServer } from 'node:http';
import { Server } from 'socket.io';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { randomBytes, scrypt as scryptCallback, timingSafeEqual, createHash } from 'node:crypto';
import { promisify } from 'node:util';
import { readFile, writeFile, mkdir, rename } from 'node:fs/promises';
const scrypt=promisify(scryptCallback);
const __dirname=path.dirname(fileURLToPath(import.meta.url));
const app=express();
app.disable('x-powered-by');
app.use(helmet({contentSecurityPolicy:false,crossOriginEmbedderPolicy:false}));
app.use(rateLimit({windowMs:60_000,limit:180,standardHeaders:true,legacyHeaders:false}));
app.use(express.json({limit:'600kb'}));
const DB=path.join(__dirname,'data','accounts.json');
const sessions=new Map();
const authLimiter=rateLimit({windowMs:15*60_000,limit:15,standardHeaders:true,legacyHeaders:false,message:{error:'Too many sign-in attempts. Wait a little and try again.'}});
async function readDb(){try{return JSON.parse(await readFile(DB,'utf8'))}catch{return {users:{}}}}
async function writeDb(db){await mkdir(path.dirname(DB),{recursive:true});const tmp=DB+'.tmp';await writeFile(tmp,JSON.stringify(db,null,2),'utf8');await rename(tmp,DB)}
function cookieToken(req){const c=(req.headers.cookie||'').split(';').map(x=>x.trim()).find(x=>x.startsWith('fa_workspace_session='));return c?c.slice('fa_workspace_session='.length):''}
function userFor(req){const t=cookieToken(req);return t?sessions.get(createHash('sha256').update(t).digest('hex'))||null:null}
function setCookie(res,t){const secure=process.env.NODE_ENV==='production'?' Secure':'';res.setHeader('Set-Cookie',`fa_workspace_session=${t}; HttpOnly; SameSite=Lax; Path=/; Max-Age=604800${secure}`)}
function newSession(res,key){const token=randomBytes(32).toString('hex');sessions.set(createHash('sha256').update(token).digest('hex'),key);setCookie(res,token)}
app.post('/api/auth/register',authLimiter,async(req,res)=>{
 const {username,password}=req.body||{};
 if(typeof username!=='string'||!/^[a-zA-Z0-9_.-]{3,24}$/.test(username))return res.status(400).json({error:'Username must be 3–24 characters and use letters, numbers, dots, dashes, or underscores.'});
 if(typeof password!=='string'||password.length<8||password.length>128)return res.status(400).json({error:'Password must be 8–128 characters.'});
 const key=username.toLowerCase(),db=await readDb();if(db.users[key])return res.status(409).json({error:'That username is already registered.'});
 const salt=randomBytes(16),hash=await scrypt(password,salt,64);
 db.users[key]={username,salt:salt.toString('hex'),hash:Buffer.from(hash).toString('hex'),createdAt:new Date().toISOString(),localStorage:{}};
 await writeDb(db);newSession(res,key);res.status(201).json({ok:true,username});
});
app.post('/api/auth/login',authLimiter,async(req,res)=>{
 const {username,password}=req.body||{};if(typeof username!=='string'||typeof password!=='string')return res.status(400).json({error:'Enter your username and password.'});
 const key=username.toLowerCase(),db=await readDb(),record=db.users[key];if(!record)return res.status(401).json({error:'Incorrect username or password.'});
 const expected=Buffer.from(record.hash,'hex'),actual=Buffer.from(await scrypt(password,Buffer.from(record.salt,'hex'),64));
 if(expected.length!==actual.length||!timingSafeEqual(expected,actual))return res.status(401).json({error:'Incorrect username or password.'});
 newSession(res,key);res.json({ok:true,username:record.username});
});
app.get('/api/auth/me',async(req,res)=>{const key=userFor(req);if(!key)return res.status(401).json({error:'Not signed in.'});const db=await readDb();if(!db.users[key])return res.status(401).json({error:'Account not found.'});res.json({username:db.users[key].username})});
app.get('/api/data',async(req,res)=>{const key=userFor(req);if(!key)return res.status(401).json({error:'Sign in to sync workspace data.'});const db=await readDb();if(!db.users[key])return res.status(401).json({error:'Account not found.'});res.json({localStorage:db.users[key].localStorage||{}})});
async function saveData(req,res){const key=userFor(req);if(!key)return res.status(401).json({error:'Sign in to sync workspace data.'});const incoming=req.body?.localStorage;if(!incoming||typeof incoming!=='object'||Array.isArray(incoming))return res.status(400).json({error:'Invalid workspace data.'});const db=await readDb();if(!db.users[key])return res.status(401).json({error:'Account not found.'});const safe={};let total=0;for(const [k,v] of Object.entries(incoming).slice(0,500)){if(typeof k!=='string'||k.length>160||typeof v!=='string'||v.length>180000)continue;total+=k.length+v.length;if(total>420000)break;safe[k]=v}db.users[key].localStorage=safe;db.users[key].updatedAt=new Date().toISOString();await writeDb(db);res.json({ok:true,savedKeys:Object.keys(safe).length})}
app.put('/api/data',saveData);app.post('/api/data',saveData);
app.post('/api/auth/logout',(req,res)=>{const t=cookieToken(req);if(t)sessions.delete(createHash('sha256').update(t).digest('hex'));res.setHeader('Set-Cookie','fa_workspace_session=; HttpOnly; SameSite=Lax; Path=/; Max-Age=0');res.json({ok:true})});
app.get('/health',(req,res)=>res.json({ok:true,version:'12.6.0'}));
app.use(express.static(__dirname,{extensions:['html']}));
const server=createServer(app),io=new Server(server,{maxHttpBufferSize:1e6});
io.on('connection',socket=>{socket.on('join-room',({room,nickname}={})=>{if(typeof room!=='string'||!room.trim())return;const key=room.trim().slice(0,32);socket.join(key);socket.data.room=key;socket.data.nickname=String(nickname||'Traveler').slice(0,24);socket.to(key).emit('chat-message',{nickname:'Workspace',message:`${socket.data.nickname} joined the room.`})});socket.on('chat-message',payload=>{const room=socket.data.room;if(!room||!payload)return;const message=String(payload.message||'').slice(0,500);if(message.trim())io.to(room).emit('chat-message',{nickname:socket.data.nickname||'Traveler',message})});socket.on('disconnect',()=>{if(socket.data.room)socket.to(socket.data.room).emit('chat-message',{nickname:'Workspace',message:`${socket.data.nickname||'A traveler'} left the room.`})})});
const port=Number(process.env.PORT)||3000;server.listen(port,'0.0.0.0',()=>console.log(`Frutiger Aero Workspace 12.6 running on ${port}`));
