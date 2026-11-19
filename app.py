import os
from flask import Flask, render_template_string, jsonify, request
from datetime import datetime, timezone

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024

PAGE = r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#75dce9">
<meta name="description" content="A glossy aquatic desktop for ideas, creativity and tiny fish.">
<title>Frutiger Aero Workspace</title>
<style>
:root{--ink:#12465c;--aqua:#16a8ca;--deep:#08769d;--glass:rgba(255,255,255,.57);--edge:rgba(255,255,255,.9);--shadow:0 16px 32px rgba(0,83,120,.22),0 3px 8px #fff9 inset;--shine:linear-gradient(145deg,#fff 0%,#ffffff9c 23%,#ffffff20 48%,#5bd7e333 100%)}
*{box-sizing:border-box}
body{margin:0;min-height:100vh;color:var(--ink);font-family:"Trebuchet MS",Segoe UI,Arial,sans-serif;background:radial-gradient(ellipse at 18% 5%,#fff 0,transparent 28%),radial-gradient(ellipse at 85% 18%,#e9ffff 0,transparent 23%),linear-gradient(145deg,#b7f5e9,#77d9ed 45%,#b8e9ff 78%,#e7fcff);background-attachment:fixed}
body:before{content:"";position:fixed;inset:0;pointer-events:none;opacity:.27;background-image:radial-gradient(circle at 12% 30%,#fff 0 2px,transparent 3px),radial-gradient(circle at 75% 65%,#fff 0 3px,transparent 4px);background-size:170px 160px,230px 210px}
button,input,textarea,select{font:inherit}
button{cursor:pointer;color:#075b7b;border:1px solid #fff;background:linear-gradient(#fff 0%,#e9fcff 40%,#a7eafa 100%);border-radius:13px;padding:9px 14px;box-shadow:0 4px 0 #7bb9cc,0 7px 13px #005d8229,inset 0 2px 2px white;transition:.15s}
button:hover{filter:brightness(1.04);transform:translateY(-1px)}button:active{transform:translateY(2px);box-shadow:0 2px 0 #7bb9cc,inset 0 2px 5px #4aa8c655}
button.primary{color:white;background:linear-gradient(#a5f4ff,#29b9db 48%,#087da8);text-shadow:0 1px 2px #07506a;border-color:#e7ffff}
button.danger{color:#8a3451;background:linear-gradient(#fff,#ffe5ed)}
input,textarea,select{width:100%;border:1px solid #fff;border-radius:12px;background:linear-gradient(145deg,#ffffffd9,#e7fbffb8);padding:11px;color:#12465c;box-shadow:inset 0 2px 7px #247b9b20,0 1px 0 #fff}
textarea{min-height:120px;resize:vertical}
header{max-width:1450px;margin:auto;padding:20px 4vw;display:flex;justify-content:space-between;align-items:center;gap:15px}
.brand{display:flex;align-items:center;gap:13px}.logo{width:54px;height:54px;border-radius:18px;background:linear-gradient(145deg,#fff,#9af0f5 45%,#0797c4);box-shadow:inset 4px 4px 8px white,inset -5px -7px 12px #087da8,0 9px 18px #057ca744;position:relative}.logo:after{content:"";position:absolute;left:9px;top:8px;width:32px;height:12px;border-radius:100%;background:#ffffffc9;transform:rotate(-25deg)}
h1{font-size:clamp(20px,3vw,30px);margin:0;letter-spacing:-.8px;text-shadow:0 1px white}.tag{font-size:11px;letter-spacing:1.4px;opacity:.7;margin-top:4px}
.shell{max-width:1450px;width:94vw;margin:0 auto 38px;display:grid;grid-template-columns:minmax(0,1.45fr) minmax(290px,.85fr);gap:18px}
.glass{background:var(--glass);border:1px solid var(--edge);border-radius:23px;box-shadow:var(--shadow);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px)}
.panel{padding:18px}.panel h2{font-size:17px;margin:0}.panel-head{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:13px}.muted{font-size:12px;opacity:.68}
.maincol,.side{display:flex;flex-direction:column;gap:17px}.room{padding:20px;overflow:hidden}.scene{height:350px;margin-top:15px;border-radius:20px;position:relative;overflow:hidden;background:linear-gradient(#aef4ff 0%,#63d8e9 51%,#078eb5 52%,#075a83);box-shadow:inset 0 0 35px #fff9,inset 0 -20px 40px #034a7055}
.sun{position:absolute;right:12%;top:9%;width:95px;height:95px;border-radius:50%;background:radial-gradient(circle at 30% 25%,white,#fff4b8 45%,#ffbf7d);box-shadow:0 0 45px #fff9}
.cloud{position:absolute;top:23%;left:12%;width:140px;height:31px;border-radius:40px;background:#ffffffb8}.cloud:before,.cloud:after{content:"";position:absolute;background:inherit;border-radius:50%;width:55px;height:55px;top:-25px;left:25px}.cloud:after{width:45px;height:45px;left:75px;top:-15px}
.hill{position:absolute;bottom:36%;width:68%;height:90px;border-radius:50% 50% 0 0;background:linear-gradient(#69dfaa,#169f8c)}.hill.a{left:-10%;transform:rotate(-7deg)}.hill.b{right:-15%;height:120px;background:linear-gradient(#53c9b4,#087d91);transform:rotate(8deg)}
.water{position:absolute;inset:auto 0 0;height:37%;background:repeating-linear-gradient(175deg,transparent 0 15px,#c4fbff77 16px 18px)}
.fish{position:absolute;left:-8%;top:65%;font-size:32px;animation:swim 16s linear infinite;filter:drop-shadow(0 5px 4px #004b6b66)}.fish.f2{top:76%;font-size:23px;animation-duration:21s;animation-delay:-9s}
@keyframes swim{0%{left:-8%;transform:scaleX(1)}49%{transform:scaleX(1)}50%{transform:scaleX(-1)}100%{left:105%;transform:scaleX(-1)}}
.bubble{position:absolute;border:1px solid #fff;background:radial-gradient(circle at 30% 25%,#fff9,#b7f8ff22 60%,#fff5);border-radius:50%;box-shadow:inset -4px -5px 9px #fff8,0 0 12px #fff8;animation:rise 9s linear infinite}@keyframes rise{from{transform:translateY(45px);opacity:0}15%{opacity:.8}to{transform:translateY(-400px);opacity:0}}
.scene-avatar{position:absolute;bottom:12%;left:47%;font-size:52px;z-index:2;filter:drop-shadow(0 7px 5px #004b6b66)}.scene-name{position:absolute;bottom:7%;left:50%;transform:translateX(-50%);z-index:2;background:#ffffffc9;border-radius:20px;padding:4px 12px;font-size:11px;white-space:nowrap}
.scene-tools{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}.profile{display:flex;align-items:center;gap:10px;flex-wrap:wrap}.avatar-preview{width:45px;height:45px;border-radius:50%;object-fit:cover;border:3px solid white;box-shadow:0 4px 12px #126b8b44;background:#d9faff}.avatar-upload{max-width:230px;font-size:11px;padding:6px}
.side{min-width:0}.chatlog{height:145px;overflow:auto;display:flex;flex-direction:column;gap:7px}.msg{background:#ffffffad;border:1px solid white;border-radius:13px;padding:8px 10px;font-size:13px;overflow-wrap:anywhere}.chatform{display:flex;gap:7px;margin-top:9px}.chatform input{flex:1}
.widgetgrid{display:grid;grid-template-columns:1fr 1fr;gap:9px}.widget{padding:12px;border-radius:15px;background:#ffffffa8;border:1px solid white;box-shadow:inset 0 1px 0 white,0 4px 10px #2d91aa20}.big{font-size:22px;font-weight:bold}
.gamegrid{display:grid;grid-template-columns:1fr 1fr;gap:9px}.game{padding:12px;border-radius:15px;background:linear-gradient(145deg,#ffffffd9,#c8f7f7a8);border:1px solid white;text-align:center}.game .emoji{font-size:30px}
.idea-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:12px;align-items:start}.idea-card{position:relative;min-height:145px;padding:14px;border-radius:16px;border:1px solid #fff;background:linear-gradient(145deg,#fffde0ed,#ffed9be8 65%,#f7d975e8);box-shadow:5px 7px 0 #bca85c55,0 12px 20px #4e6e692b,inset 0 3px 8px white;cursor:grab;touch-action:pan-y}.idea-card.pinned{outline:3px solid #ffffffd9;box-shadow:0 0 0 5px #49bfd455,5px 7px 0 #bca85c55,0 12px 20px #4e6e692b}.idea-card h3{margin:0 0 8px;font-size:15px}.idea-card p{font-size:13px;white-space:pre-wrap;overflow-wrap:anywhere;margin:0 0 12px}.card-actions{display:flex;gap:6px;flex-wrap:wrap}.card-actions button{font-size:11px;padding:5px 8px}.empty{border:2px dashed #ffffffbd;border-radius:16px;padding:20px;text-align:center;opacity:.7}
.whiteboard{width:100%;height:150px;border-radius:14px;border:1px solid white;background:#ffffffb8;touch-action:none}
footer{text-align:center;font-size:11px;opacity:.65;padding:12px 15px 28px}
#splash{position:fixed;z-index:99;inset:0;background:radial-gradient(ellipse at 50% 20%,#1a789b,#063b62 55%,#031b37);color:#e8ffff;display:flex;align-items:center;justify-content:center;padding:20px;transition:opacity .8s,visibility .8s}#splash.hide{opacity:0;visibility:hidden}.boot{width:min(570px,94vw);padding:32px;border:1px solid #8df6ff;border-radius:17px;background:linear-gradient(145deg,#ffffff22,#ffffff08);box-shadow:0 0 45px #45dfff44,inset 0 1px 0 #fff8;text-align:center}.bootlogo{font-size:42px;text-shadow:0 0 22px #6dfaff}.boot h2{font-size:clamp(23px,5vw,38px);margin:12px 0;text-shadow:0 0 15px #83edff}.boot p{opacity:.8;font-size:13px}.progress{height:13px;border-radius:20px;background:#001d35;overflow:hidden;border:1px solid #9cefff;margin:20px 0}.progress span{display:block;height:100%;width:0;background:linear-gradient(90deg,#42c9ef,#e6ffff);box-shadow:0 0 14px #72f4ff;transition:width 1.1s}.boot button{margin-top:10px}
.modal{position:fixed;inset:0;z-index:50;background:#03415b88;display:none;align-items:center;justify-content:center;padding:16px}.modal.open{display:flex}.editor{width:min(620px,100%);padding:20px}.editor label{display:block;font-size:12px;margin:10px 0 5px}.editor-actions{display:flex;gap:8px;justify-content:flex-end;margin-top:12px}
#toast{position:fixed;bottom:16px;left:50%;transform:translateX(-50%);background:#075477;color:white;border-radius:20px;padding:10px 16px;opacity:0;transition:.2s;z-index:120;pointer-events:none}#toast.show{opacity:1}
.mine{display:grid;grid-template-columns:repeat(5,1fr);gap:4px;margin-top:8px}.mine button{padding:8px 0;border-radius:7px}.mine button.revealed{background:#d8f9f7;box-shadow:inset 0 2px 5px #287b9444}
@media(max-width:850px){.shell{grid-template-columns:1fr}.scene{height:310px}}@media(max-width:480px){header{align-items:flex-start}.tag{font-size:9px}.room{padding:13px}.panel{padding:14px}.scene{height:285px}.widgetgrid{grid-template-columns:1fr 1fr}}
</style>
</head>
<body>
<div id="splash"><div class="boot"><div class="bootlogo">◉ ✧ 🌐 ✧ ◉</div><h2>WELCOME, DEAR TRAVELER.</h2><p>FRUTIGER AERO WORKSPACE · STARTING YOUR DIGITAL OCEAN</p><div class="progress"><span id="bootbar"></span></div><p id="boottext">Polishing glass surfaces...</p><button class="primary" id="enterBtn">Enter Workspace →</button></div></div>

<header><div class="brand"><div class="logo"></div><div><h1>Frutiger Aero Workspace</h1><div class="tag">A LITTLE DIGITAL OCEAN FOR YOUR IDEAS</div></div></div><span class="muted">✦ WEB EDITION 2.0</span></header>
<main class="shell">
 <div class="maincol">
  <section class="glass room">
   <div class="panel-head"><div><h2>🌊 Ocean Atrium</h2><div class="muted">A glossy place to gather and create</div></div><span class="muted">AQUARIUM ONLINE</span></div>
   <div class="scene" id="scene"><div class="sun"></div><div class="cloud"></div><div class="hill a"></div><div class="hill b"></div><div class="water"></div><div class="fish">🐠</div><div class="fish f2">🐟</div><div class="scene-avatar" id="sceneAvatar">🧑🏻‍🚀</div><div class="scene-name" id="sceneName">Aero Explorer</div></div>
   <div class="scene-tools"><button id="feedFish">🐟 Feed fish</button><button id="collectFish" class="primary">＋ Collect fish</button><span class="muted" id="fishCount">Fish collected: 0</span></div>
   <div class="profile" style="margin-top:13px"><img class="avatar-preview" id="avatarPreview" alt="Profile picture" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='80' height='80'%3E%3Crect width='80' height='80' rx='40' fill='%239be8ef'/%3E%3Ctext x='40' y='54' text-anchor='middle' font-size='42'%3E🧑🏻‍🚀%3C/text%3E%3C/svg%3E"><input id="profileImage" class="avatar-upload" type="file" accept="image/png,image/jpeg,image/webp"><input id="displayName" style="max-width:170px" maxlength="22" value="Aero Explorer" aria-label="Display name"><button id="saveProfile" class="small">Save profile</button></div>
  </section>
  <section class="glass panel">
   <div class="panel-head"><div><h2>📝 Idea Garden</h2><div class="muted">Your notes become floating desktop cards</div></div><button class="primary" id="newIdea">＋ New Idea</button></div>
   <div id="ideaGrid" class="idea-grid"><div class="empty">Your idea garden is waiting to bloom. Create your first note!</div></div>
  </section>
  <section class="glass panel"><div class="panel-head"><h2>🫧 Bubble Pop Screen Saver</h2><span class="muted">TAP TO POP</span></div><div id="bubbleGame" class="scene" style="height:190px;margin:0;background:linear-gradient(#b8f7ff,#24b6d1 55%,#087ba7);cursor:pointer"><div class="water"></div></div><div class="muted" style="margin-top:7px">Pop the floating water bubbles. Score: <b id="bubbleScore">0</b></div></section>
 </div>
 <aside class="side">
  <section class="glass panel"><div class="panel-head"><h2>💬 Glass Chat Feed</h2><span class="muted">LOCAL DEMO</span></div><div id="chatLog" class="chatlog"></div><form id="chatForm" class="chatform"><input id="chatInput" maxlength="220" placeholder="Send a message..."><button class="primary">Send</button></form><div class="muted" style="margin-top:6px">Demo chat is saved in this browser only.</div></section>
  <section class="glass panel"><div class="panel-head"><h2>🪟 Aero Widgets</h2></div><div class="widgetgrid"><div class="widget"><div class="muted">LOCAL TIME</div><div class="big" id="clock">--:--</div></div><div class="widget"><div class="muted">FOCUS TIMER</div><div class="big" id="timer">25:00</div><button class="small" id="timerBtn">Start</button></div></div><div class="scene-tools"><button id="musicBtn">♫ Ambient synth</button><button id="toggleClock">Hide clock</button></div></section>
  <section class="glass panel"><div class="panel-head"><h2>🎮 Desktop Mini-Games</h2></div><div class="gamegrid"><div class="game"><div class="emoji">💣</div><b>Minesweeper</b><div class="muted">Tiny 5×5 puzzle</div><button class="small" id="newMine">Play</button><div id="mineBoard" class="mine"></div></div><div class="game"><div class="emoji">🐠</div><b>Fish Tank</b><div class="muted">Collect & feed fish</div><button class="small" id="fishGame">Visit tank</button></div></div></section>
  <section class="glass panel"><div class="panel-head"><h2>✏️ Bubble Whiteboard</h2><button class="small" id="clearBoard">Clear</button></div><canvas id="board" class="whiteboard"></canvas><div class="muted">Draw with your finger or mouse. Saved on this device.</div></section>
 </aside>
</main>
<footer>FRUTIGER AERO WORKSPACE 2.0 · KEEP IT GLOSSY, KEEP IT KIND ✦</footer>

<div class="modal" id="ideaModal"><div class="glass editor"><div class="panel-head"><h2>✨ New Idea Document</h2><button id="closeEditor">✕</button></div><label for="ideaTitle">Document title</label><input id="ideaTitle" maxlength="70" placeholder="A bright idea..."><label for="ideaBody">Your idea</label><textarea id="ideaBody" maxlength="4000" placeholder="Write your thoughts here..."></textarea><div class="editor-actions"><button id="cancelIdea">Cancel</button><button class="primary" id="postIdea">Post to Workspace</button></div></div></div>
<div id="toast"></div>
<script>
const $=id=>document.getElementById(id), toast=t=>{const el=$('toast');el.textContent=t;el.classList.add('show');setTimeout(()=>el.classList.remove('show'),1900)};
const read=(k,d)=>{try{return JSON.parse(localStorage.getItem(k))??d}catch{return d}},write=(k,v)=>localStorage.setItem(k,JSON.stringify(v));
let ideas=read('fa_ideas',[]), profile=read('fa_profile',{name:'Aero Explorer',avatar:'🧑🏻‍🚀',image:''}), fish=read('fa_fish',0), messages=read('fa_chat',[]), bubbleScore=0;
function bubbles(target,count){for(let i=0;i<count;i++){let b=document.createElement('i');b.className='bubble';let s=9+Math.random()*25;b.style.width=s+'px';b.style.height=s+'px';b.style.left=Math.random()*94+'%';b.style.bottom=(-10-Math.random()*30)+'px';b.style.animationDelay=(-Math.random()*8)+'s';b.style.animationDuration=(6+Math.random()*6)+'s';target.appendChild(b)}}
bubbles($('scene'),16);
function showProfile(){ $('displayName').value=profile.name;$('sceneName').textContent=profile.name;$('sceneAvatar').textContent=profile.avatar;if(profile.image)$('avatarPreview').src=profile.image; }
showProfile();
$('profileImage').addEventListener('change',e=>{const f=e.target.files[0];if(!f)return;if(!/^image\/(png|jpeg|webp)$/.test(f.type)){toast('Choose a PNG, JPG or WebP image');return}if(f.size>900000){toast('Please choose an image smaller than 900 KB');e.target.value='';return}const r=new FileReader();r.onload=()=>{profile.image=r.result;$('avatarPreview').src=profile.image};r.readAsDataURL(f)});
$('saveProfile').onclick=()=>{profile.name=$('displayName').value.trim()||'Aero Explorer';write('fa_profile',profile);showProfile();toast('Profile saved on this device ✨')};
function renderIdeas(){const grid=$('ideaGrid');grid.innerHTML='';if(!ideas.length){grid.innerHTML='<div class="empty">Your idea garden is waiting to bloom. Create your first note!</div>';return}
 ideas.forEach(item=>{const card=document.createElement('article');card.className='idea-card'+(item.pinned?' pinned':'');card.draggable=true;card.dataset.id=item.id;
 const title=document.createElement('h3');title.textContent=item.title;const body=document.createElement('p');body.textContent=item.body;
 const actions=document.createElement('div');actions.className='card-actions';
 const pin=document.createElement('button');pin.textContent=item.pinned?'Unpin':'📌 Pin';pin.onclick=()=>{item.pinned=!item.pinned;write('fa_ideas',ideas);renderIdeas()};
 const edit=document.createElement('button');edit.textContent='✎ Edit';edit.onclick=()=>openEditor(item);
 const del=document.createElement('button');del.className='danger';del.textContent='Delete';del.onclick=()=>{ideas=ideas.filter(x=>x.id!==item.id);write('fa_ideas',ideas);renderIdeas();toast('Idea deleted')};
 actions.append(pin,edit,del);card.append(title,body,actions);
 card.addEventListener('dragstart',e=>{e.dataTransfer.setData('text/plain',item.id);card.style.opacity='.55'});
 card.addEventListener('dragend',()=>card.style.opacity='1');
 grid.append(card);
 });
}
$('ideaGrid').addEventListener('dragover',e=>e.preventDefault());
$('ideaGrid').addEventListener('drop',e=>{e.preventDefault();const id=e.dataTransfer.getData('text/plain');const idx=ideas.findIndex(x=>x.id===id);if(idx<0)return;const [item]=ideas.splice(idx,1);ideas.push(item);write('fa_ideas',ideas);renderIdeas()});
let editingId=null;
function openEditor(item=null){editingId=item?.id??null;$('ideaTitle').value=item?.title??'';$('ideaBody').value=item?.body??'';$('ideaModal').classList.add('open');$('ideaTitle').focus()}
function closeEditor(){$('ideaModal').classList.remove('open')}
$('newIdea').onclick=()=>openEditor();$('closeEditor').onclick=closeEditor;$('cancelIdea').onclick=closeEditor;
$('postIdea').onclick=()=>{const title=$('ideaTitle').value.trim(),body=$('ideaBody').value.trim();if(!title||!body){toast('Add a title and some idea text first');return}
 if(editingId){const item=ideas.find(x=>x.id===editingId);if(item){item.title=title;item.body=body}}
 else ideas.unshift({id:crypto.randomUUID?crypto.randomUUID():String(Date.now()),title,body,pinned:false,created:new Date().toISOString()});
 write('fa_ideas',ideas);renderIdeas();closeEditor();toast(editingId?'Idea updated':'Posted to workspace! 🫧')
};
renderIdeas();
function renderChat(){const log=$('chatLog');log.innerHTML='';messages.slice(-35).forEach(m=>{const div=document.createElement('div');div.className='msg';const b=document.createElement('b');b.textContent=m.name+': ';const span=document.createElement('span');span.textContent=m.text;div.append(b,span);log.append(div)});log.scrollTop=log.scrollHeight}
$('chatForm').onsubmit=e=>{e.preventDefault();const text=$('chatInput').value.trim();if(!text)return;messages.push({name:profile.name,text});messages=messages.slice(-60);write('fa_chat',messages);$('chatInput').value='';renderChat()};renderChat();
$('collectFish').onclick=()=>{fish++;write('fa_fish',fish);$('fishCount').textContent='Fish collected: '+fish;toast('A new fish joined your aquarium! 🐠')};
$('fishCount').textContent='Fish collected: '+fish;
$('feedFish').onclick=()=>toast(fish?'Your fish are happily nibbling! 🫧':'Collect a fish first!');
$('fishGame').onclick=()=>{fish++;write('fa_fish',fish);$('fishCount').textContent='Fish collected: '+fish;toast('You found a little aquarium friend! 🐟')};
$('bubbleGame').onclick=e=>{if(e.target.closest('button'))return;bubbleScore++;$('bubbleScore').textContent=bubbleScore;const b=document.createElement('span');b.textContent='✦';b.style.cssText=`position:absolute;left:${e.offsetX}px;top:${e.offsetY}px;color:white;font-size:28px;pointer-events:none`;e.currentTarget.append(b);setTimeout(()=>b.remove(),500)};
function clock(){$('clock').textContent=new Date().toLocaleTimeString([],{hour:'2-digit',minute:'2-digit'})}clock();setInterval(clock,1000);
let seconds=1500,timer=null;$('timerBtn').onclick=()=>{if(timer){clearInterval(timer);timer=null;$('timerBtn').textContent='Resume';return}$('timerBtn').textContent='Pause';timer=setInterval(()=>{seconds=Math.max(0,seconds-1);$('timer').textContent=String(Math.floor(seconds/60)).padStart(2,'0')+':'+String(seconds%60).padStart(2,'0');if(!seconds){clearInterval(timer);timer=null;$('timerBtn').textContent='Restart';toast('Focus session complete! 🌟')}},1000);if(seconds===0){seconds=1500}};
$('toggleClock').onclick=()=>{const w=$('clock').parentElement;w.hidden=!w.hidden;$('toggleClock').textContent=w.hidden?'Show clock':'Hide clock'};
let audio=null,music=false;$('musicBtn').onclick=()=>{const AC=window.AudioContext||window.webkitAudioContext;if(!AC){toast('Audio unavailable in this browser');return}if(!audio)audio=new AC();if(music){audio.suspend();music=false;$('musicBtn').textContent='♫ Ambient synth';return}audio.resume();music=true;const master=audio.createGain();master.gain.value=.025;master.connect(audio.destination);[110,164.81,220].forEach((f,i)=>{const o=audio.createOscillator(),g=audio.createGain();o.type='sine';o.frequency.value=f;g.gain.value=[.45,.25,.15][i];o.connect(g);g.connect(master);o.start()});$('musicBtn').textContent='♫ Pause synth';toast('Ambient tones enabled')};
// Simple touch/mouse whiteboard; the drawing is stored in this browser's localStorage.
const c=$('board'),ctx=c.getContext('2d');function fit(){const r=c.getBoundingClientRect(),d=devicePixelRatio||1;c.width=r.width*d;c.height=r.height*d;ctx.scale(d,d);ctx.strokeStyle='#078dbb';ctx.lineWidth=3;ctx.lineCap='round';const saved=read('fa_board',[]);saved.forEach(line=>{ctx.beginPath();line.forEach((p,i)=>i?ctx.lineTo(p.x*r.width,p.y*r.height):ctx.moveTo(p.x*r.width,p.y*r.height));ctx.stroke()})}fit();window.addEventListener('resize',()=>{const saved=read('fa_board',[]);fit();});
let drawing=false,current=[];function pos(e){const r=c.getBoundingClientRect();return{x:(e.clientX-r.left)/r.width,y:(e.clientY-r.top)/r.height}}
c.onpointerdown=e=>{drawing=true;current=[pos(e)];c.setPointerCapture(e.pointerId)};c.onpointermove=e=>{if(!drawing)return;const p=pos(e),r=c.getBoundingClientRect();ctx.beginPath();const a=current[current.length-1];ctx.moveTo(a.x*r.width,a.y*r.height);ctx.lineTo(p.x*r.width,p.y*r.height);ctx.stroke();current.push(p)};function end(){if(!drawing)return;drawing=false;const saved=read('fa_board',[]);saved.push(current);write('fa_board',saved.slice(-100));current=[]}c.onpointerup=end;c.onpointercancel=end;
$('clearBoard').onclick=()=>{ctx.clearRect(0,0,c.width,c.height);write('fa_board',[]);toast('Whiteboard cleared')};
// Small beginner-friendly 5x5 minesweeper.
let mineSet=[],revealed=new Set();$('newMine').onclick=()=>{mineSet=[];revealed=new Set();while(mineSet.length<5){let n=Math.floor(Math.random()*25);if(!mineSet.includes(n))mineSet.push(n)}renderMine();};
function renderMine(){const el=$('mineBoard');el.innerHTML='';for(let i=0;i<25;i++){const b=document.createElement('button');b.textContent=revealed.has(i)?(mineSet.includes(i)?'💣':adj(i)||'·'):'?';if(revealed.has(i))b.classList.add('revealed');b.onclick=()=>{if(revealed.has(i))return;revealed.add(i);renderMine();if(mineSet.includes(i))toast('Boom! Start a new board 💥');else if(revealed.size===20)toast('You cleared the board! 🏆')};el.append(b)}}
function adj(i){let x=i%5,y=Math.floor(i/5),n=0;for(let dy=-1;dy<=1;dy++)for(let dx=-1;dx<=1;dx++){let xx=x+dx,yy=y+dy;if(xx>=0&&xx<5&&yy>=0&&yy<5&&mineSet.includes(yy*5+xx))n++}return n}
$('newMine').click();
// Retro startup sequence shown on every fresh page load.
const splash=$('splash');let progress=0;const bar=$('bootbar');const bootText=$('boottext');const steps=['Polishing glass surfaces...','Waking the aquarium...','Gathering your ideas...','Opening the digital ocean...'];const boot=setInterval(()=>{progress=Math.min(100,progress+25);bar.style.width=progress+'%';bootText.textContent=steps[Math.min(3,Math.floor(progress/25)-1)];if(progress>=100){clearInterval(boot);$('enterBtn').textContent='Enter Workspace →'}},350);
$('enterBtn').onclick=()=>splash.classList.add('hide');setTimeout(()=>splash.classList.add('hide'),6500);
</script>
</body></html>
"""

@app.get("/")
def home():
    return render_template_string(PAGE)

@app.get("/health")
def health():
    return jsonify({"status":"ok","app":"Frutiger Aero Workspace","version":"2.0"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
