import assert from 'node:assert/strict';
const base=(process.env.WORKSPACE_URL||'http://127.0.0.1:3000').replace(/\/$/,'');
const assets=['background-frutiger-aero.jpg','background-frutiger-eco.jpg','background-frutiger-dorfic.jpg','background-frutiger-aqua.jpg','background-frutiger-metro.jpg','controller.png','discord.png','fish.png','messages.png','msn-buddy.png','music.png','settings.png','sunflower.png'];
const health=await fetch(base+'/health');assert.equal(health.status,200,'health endpoint should respond');const hv=await health.json();assert.equal(hv.version,'12.6.0','server should report Workspace 12.6');
const html=await fetch(base+'/index.html');assert.equal(html.status,200,'index.html should be served');const source=await html.text();for(const marker of ['fa126AuthGate','fa126Screensaver','fa126LevelSelect','background-frutiger-aero.jpg','data-variant="eco"'])assert.ok(source.includes(marker),`index.html should include ${marker}`);
for(const file of assets){const r=await fetch(base+'/assets/'+file);assert.equal(r.status,200,`asset ${file} should load`);assert.ok(Number(r.headers.get('content-length')||0)>0,`asset ${file} should not be empty`)}
console.log(`Workspace 12.6 smoke test passed: health, index, ${assets.length} artwork assets.`);
