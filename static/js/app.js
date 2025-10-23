let token = null;
let citySocket = null;

async function login(evt){
  evt.preventDefault();
  const form = evt.target;
  const data = new URLSearchParams(new FormData(form));
  const res = await fetch('/api/auth/login', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: data });
  if(!res.ok){
    document.getElementById('login-error').textContent = 'Login failed';
    return;
  }
  const json = await res.json();
  token = json.access_token;
  document.getElementById('auth').classList.add('hidden');
  document.getElementById('dashboard').classList.remove('hidden');
  await afterLogin();
}

async function register(evt){
  evt.preventDefault();
  const form = evt.target;
  const payload = {
    full_name: form.full_name.value || null,
    email: form.email.value,
    password: form.password.value,
  };
  const res = await fetch('/api/auth/register', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
  if(!res.ok){
    document.getElementById('register-error').textContent = 'Registration failed';
    return;
  }
  // auto-login
  const data = new URLSearchParams();
  data.set('username', payload.email);
  data.set('password', payload.password);
  const lres = await fetch('/api/auth/login', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: data });
  if(lres.ok){
    const json = await lres.json();
    token = json.access_token;
    document.getElementById('auth').classList.add('hidden');
    document.getElementById('dashboard').classList.remove('hidden');
    await afterLogin();
  }
}

async function loadCities(){
  const res = await fetch('/api/cities', { headers: token ? { 'Authorization': `Bearer ${token}` } : {} });
  const cities = await res.json();
  const sel = document.getElementById('city-select');
  sel.innerHTML='';
  for(const c of cities){
    const opt = document.createElement('option');
    opt.value = c.id; opt.textContent = c.name;
    sel.appendChild(opt);
  }
  if(cities.length){ 
    await loadLots(cities[0].id);
    openCitySocket(cities[0].id);
  }
}

async function loadLots(cityId){
  const res = await fetch(`/api/lots?city_id=${cityId}`, { headers: token ? { 'Authorization': `Bearer ${token}` } : {} });
  const lots = await res.json();
  const ul = document.getElementById('lots-list');
  ul.innerHTML='';
  for(const lot of lots){
    const li = document.createElement('li');
    li.innerHTML = `<strong>${lot.name}</strong> — ${lot.available_slots}/${lot.total_slots} available @ $${lot.pricing_per_hour}/hr`;
    ul.appendChild(li);
  }
}

function openCitySocket(cityId){
  try{ if(citySocket){ citySocket.close(); } }catch(e){}
  citySocket = new WebSocket(`ws://${location.host}/api/realtime/cities/${cityId}`);
  citySocket.onmessage = async (ev)=>{
    const msg = JSON.parse(ev.data);
    if(msg.type === 'lot_added' || msg.type === 'lot_update'){
      await loadLots(cityId);
    }
  };
}

async function afterLogin(){
  // discover role
  try{
    const me = await fetch('/api/auth/me', { headers: { 'Authorization': `Bearer ${token}` } });
    if(me.ok){
      const user = await me.json();
      if(user.role === 'admin'){
        document.getElementById('admin-tools').classList.remove('hidden');
      }
    }
  }catch(e){}
  await loadCities();
}

function bind(){
  document.getElementById('login-form').addEventListener('submit', login);
  document.getElementById('register-form').addEventListener('submit', register);
  document.getElementById('refresh-cities').addEventListener('click', loadCities);
  document.getElementById('city-select').addEventListener('change', (e)=> { loadLots(e.target.value); openCitySocket(e.target.value); });
  // admin forms
  const cityForm = document.getElementById('create-city-form');
  const lotForm = document.getElementById('create-lot-form');
  if(cityForm){ cityForm.addEventListener('submit', async (e)=>{
    e.preventDefault();
    const form = e.target;
    const payload = { name: form.name.value, state: form.state.value || null, country: form.country.value || null };
    const res = await fetch('/api/cities', { method: 'POST', headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' }, body: JSON.stringify(payload)});
    if(res.ok){ await loadCities(); form.reset(); }
  }); }
  if(lotForm){ lotForm.addEventListener('submit', async (e)=>{
    e.preventDefault();
    const form = e.target;
    const cityId = document.getElementById('city-select').value;
    const payload = { city_id: cityId, name: form.name.value, address: form.address.value, total_slots: Number(form.total_slots.value), pricing_per_hour: Number(form.pricing_per_hour.value) };
    const res = await fetch('/api/lots', { method: 'POST', headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' }, body: JSON.stringify(payload)});
    if(res.ok){ await loadLots(cityId); form.reset(); }
  }); }
}

bind();
