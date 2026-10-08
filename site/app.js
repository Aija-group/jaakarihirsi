/* Jääkärihirsi – sivuston toiminnot (ei ulkoisia kirjastoja) */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var qs = new URLSearchParams(location.search);
  var SV = document.documentElement.lang === 'sv';

  /* Mobiilivalikko */
  var hdr = $('.hdr'), burger = $('.burger');
  function closeMenu() { hdr.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); document.documentElement.classList.remove('lock'); }
  if (burger) {
    burger.addEventListener('click', function () {
      var open = hdr.classList.toggle('open');
      burger.setAttribute('aria-expanded', open);
      document.documentElement.classList.toggle('lock', open);
    });
    $$('.mnav a').forEach(function (a) { a.addEventListener('click', closeMenu); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeMenu(); });
  }

  /* Ilmestymisanimaatiot (?shot = kuvakaappaustila ilman animaatioita) */
  if (/[?&]shot/.test(location.search)) { document.documentElement.classList.add('shot'); $$('img[loading=lazy]').forEach(function (i) { i.loading = 'eager'; }); }
  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { rootMargin: '0px 0px -6% 0px' }) : null;
  $$('.rv').forEach(function (el) { io ? io.observe(el) : el.classList.add('in'); });

  /* Lightbox: ryhmä = saman mallin kuvat */
  var lb = $('.lb'), lbImg = lb && $('img', lb), lbCap = lb && $('figcaption', lb), group = [], idx = 0;
  function show(i) { idx = (i + group.length) % group.length; var a = group[idx]; lbImg.src = a.getAttribute('href'); lbImg.alt = a.dataset.lb || ''; lbCap.textContent = (a.dataset.lb || '') + '  ·  ' + (idx + 1) + ' / ' + group.length; }
  function close() { lb.hidden = true; document.documentElement.classList.remove('lock'); }
  $$('a[data-lb]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      if (!lb) return;
      e.preventDefault();
      group = $$('a[data-lb]', a.closest('.model-gal') || document);
      lb.hidden = false; document.documentElement.classList.add('lock');
      show(group.indexOf(a));
    });
  });
  if (lb) {
    $('.lb-x', lb).addEventListener('click', close);
    $('.lb-p', lb).addEventListener('click', function () { show(idx - 1); });
    $('.lb-n', lb).addEventListener('click', function () { show(idx + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (lb.hidden) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(idx - 1);
      if (e.key === 'ArrowRight') show(idx + 1);
    });
    var tx = null;
    lb.addEventListener('touchstart', function (e) { tx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) { if (tx === null) return; var d = e.changedTouches[0].clientX - tx; if (Math.abs(d) > 50) show(idx + (d < 0 ? 1 : -1)); tx = null; });
  }

  /* Lomakkeet: tarkistus + esikatselutila */
  $$('form[name]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      var err = $('[data-err]', f), bad = [];
      $$('.bad', f).forEach(function (x) { x.classList.remove('bad'); });
      if (!f.nimi.value.trim()) bad.push(f.nimi);
      if (!f.puhelin.value.trim() && !f.email.value.trim()) bad.push(f.puhelin);
      var ts = $('input[type=checkbox][required]', f);
      if (ts && !ts.checked) bad.push(ts);
      if (bad.length) { bad.forEach(function (x) { x.classList.add('bad'); }); if (err) err.classList.add('show'); e.preventDefault(); bad[0].focus(); return; }
      if (f.dataset.preview) { e.preventDefault(); location.href = SV ? 'sv-tack.html' : 'kiitos.html'; }
    });
  });
  /* Palvelimen virheilmoitus (?virhe=1 kentät, ?virhe=2 tekninen) */
  var virhe = (location.search.match(/[?&]virhe=(\d)/) || [])[1];
  if (virhe) {
    var vf = $('form[name]');
    if (vf) { var el = $(virhe === '2' ? '.senderr' : '[data-err]', vf); if (el) el.classList.add('show'); }
  }

  /* ---------------- Tarjousvelho ---------------- */
  var cfgEl = $('#qcfg'), form = $('form.qform');
  if (!cfgEl || !form) return;
  var CFG = JSON.parse(cfgEl.textContent), Lb = CFG.L, P = {};
  CFG.products.forEach(function (p) { P[p.k] = p; });
  var dec = function (n, d) { return (Math.round(n * Math.pow(10, d || 1)) / Math.pow(10, d || 1)).toFixed(d === 0 ? 0 : (d || 1)).replace('.', ','); };
  var eur = function (v) { return String(v).replace(/\B(?=(\d{3})+(?!\d))/g, ' ') + ' €'; };
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var boxM = $('[data-models]', form), boxX = $('[data-extras]', form), mWrap = $('.q-models', form);
  var fW = form.leveys, fL = form.pituus, fN = form.maara;
  var plans = $$('.qplan'), dl = $('.qdl'), priceEls = $$('.qprice');
  var cur = null;

  function chips(name, items, type, checked) {
    return items.map(function (it, i) {
      var v = typeof it === 'string' ? it : it.n;
      return '<label class="ch"><input type="' + type + '" name="' + name + '" value="' + esc(v) + '" data-i="' + i + '"' + (checked(i, v) ? ' checked' : '') + '><span>' + esc(v) + '</span></label>';
    }).join('');
  }

  function setProduct(k, model) {
    cur = P[k];
    var multi = cur.t === 'count', def = 0;
    cur.m.forEach(function (m, i) { if (!def && m.p && !cur.m[0].p) def = i; });
    boxM.innerHTML = cur.m.length > 1 || multi ? chips('malli', cur.m, multi ? 'checkbox' : 'radio', function (i, v) { return model ? v === model : (!multi && i === def); }) : '';
    if (!boxM.innerHTML && cur.m.length === 1) boxM.innerHTML = chips('malli', cur.m, 'radio', function () { return true; });
    mWrap.classList.toggle('hide', cur.m.length < 2 && !multi);
    boxX.innerHTML = chips('lisat', cur.x, 'checkbox', function () { return false; });
    var building = ['sauna', 'building', 'octagon'].indexOf(cur.t) > -1;
    $('[data-dim=w]', form).hidden = !building;
    $('[data-dim=l]', form).hidden = !building || cur.t === 'octagon';
    $('[data-dim=n]', form).hidden = building;
    $('[data-opt=frame]', form).hidden = !building;
    $('[data-opt=roof]', form).hidden = !(building || cur.t === 'bins');
    $('[data-wl]', form).textContent = cur.t === 'octagon' ? Lb.diam : Lb.width;
    $('[data-nl]', form).textContent = cur.t === 'bins' ? Lb.bins : Lb.qty;
    fW.value = cur.w; fL.value = cur.l;
    fN.value = cur.t === 'bins' ? 2 : 1;
    if (form.runko) form.runko.selectedIndex = cur.t === 'sauna' ? 1 : (cur.t === 'octagon' ? 3 : 0);
    applyModel();
  }

  function selModel() { var r = $('input[name=malli]:checked', form); return r ? cur.m[+r.dataset.i] : null; }
  function applyModel() {
    var m = selModel();
    if (m && m.w) { fW.value = m.w; fL.value = m.l; }
    update();
  }

  function svgPlan() {
    var t = cur.t, ex = $$('input[name=lisat]:checked', form).map(function (c) { return c.dataset.i | 0; });
    var m = selModel();
    if (t === 'count' || (m && m.noplan)) return { svg: '<img src="' + cur.img + '" alt="">', area: null };
    var W = 340, H = 250, pad = 46, svg = '', area, areaT = 0, rows = [];
    var defs = '<defs><pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="7" height="7" fill="#f8f3ea"/><line x1="0" y1="0" x2="0" y2="7" stroke="#d8cbb6" stroke-width="2"/></pattern></defs>';
    if (t === 'octagon') {
      var D = Math.max(1.5, Math.min(6, parseFloat(String(fW.value).replace(',', '.')) || cur.w));
      area = 0.8284 * D * D;
      var s = Math.min(W - 2 * pad, H - 2 * pad + 10) / D, R = D * s / 2 / Math.cos(Math.PI / 8), cx = W / 2, cy = H / 2 - 8, pts = [];
      for (var i = 0; i < 8; i++) { var a = Math.PI / 8 + i * Math.PI / 4; pts.push((cx + R * Math.cos(a)).toFixed(1) + ',' + (cy + R * Math.sin(a)).toFixed(1)); }
      var half = D * s / 2;
      svg += '<polygon class="wall" points="' + pts.join(' ') + '"/>';
      svg += '<line class="dim" x1="' + (cx - half) + '" y1="' + (cy + half + 18) + '" x2="' + (cx + half) + '" y2="' + (cy + half + 18) + '"/><text x="' + cx + '" y="' + (cy + half + 34) + '" text-anchor="middle">⌀ ' + dec(D) + ' m</text>';
      svg += '<text class="rl" x="' + cx + '" y="' + (cy + 5) + '" text-anchor="middle">' + dec(area) + ' m²</text>';
      return { svg: '<svg viewBox="0 0 ' + W + ' ' + H + '">' + defs + svg + '</svg>', area: area, koko: '⌀ ' + dec(D) + ' m' };
    }
    var w, l;
    if (t === 'bins') {
      var n = Math.max(1, Math.min(4, parseInt(fN.value, 10) || 1));
      l = n * 0.85 + 0.2; w = 1.1;
    } else {
      w = Math.max(0.8, Math.min(12, parseFloat(String(fW.value).replace(',', '.')) || cur.w));
      l = Math.max(0.8, Math.min(15, parseFloat(String(fL.value).replace(',', '.')) || cur.l));
    }
    var hasT = t === 'sauna' && ex.indexOf(0) > -1, hasP = (t === 'sauna' && ex.indexOf(1) > -1) || (cur.k === 'leikkimokki' && ex.indexOf(0) > -1);
    var tD = hasT ? 1.5 : 0, pD = hasP && !hasT ? 1.2 : 0, ext = tD || pD;
    var s2 = Math.min((W - 2 * pad) / l, (H - 2 * pad + 6) / (w + ext));
    var bw = l * s2, bh = w * s2, x0 = (W - bw) / 2 + 6, y0 = (H - bh - ext * s2) / 2 - 6;
    svg += '<rect class="wall" x="' + x0 + '" y="' + y0 + '" width="' + bw + '" height="' + bh + '"/>';
    if (t === 'sauna' && l >= 2.2) {
      var sx = x0 + bw * 0.45;
      svg += '<line class="room" x1="' + sx + '" y1="' + y0 + '" x2="' + sx + '" y2="' + (y0 + bh) + '"/>';
      svg += '<text class="rl" x="' + (x0 + bw * 0.225) + '" y="' + (y0 + bh / 2 + 4) + '" text-anchor="middle">' + Lb.steam + '</text>';
      svg += '<text class="rl" x="' + (x0 + bw * 0.725) + '" y="' + (y0 + bh / 2 + 4) + '" text-anchor="middle">' + Lb.dress + '</text>';
    } else if (t === 'bins') {
      for (var b = 0; b < n; b++) svg += '<rect class="bin" x="' + (x0 + (0.1 + b * 0.85) * s2 + 4) + '" y="' + (y0 + 0.2 * s2) + '" width="' + (0.72 * s2) + '" height="' + (0.7 * s2) + '" rx="4"/>';
    } else {
      svg += '<text class="rl" x="' + (x0 + bw / 2) + '" y="' + (y0 + bh / 2 + 4) + '" text-anchor="middle">' + dec(w * l) + ' m²</text>';
    }
    if (ext) {
      var ew = hasT ? bw : Math.min(bw, 2.0 * s2), ex0 = hasT ? x0 : x0 + bw - ew;
      svg += '<rect class="terr" x="' + ex0 + '" y="' + (y0 + bh) + '" width="' + ew + '" height="' + (ext * s2) + '"/>';
      svg += '<text x="' + (ex0 + ew / 2) + '" y="' + (y0 + bh + ext * s2 / 2 + 4) + '" text-anchor="middle">' + (hasT ? Lb.terrace : Lb.porch) + '</text>';
      areaT = (ew / s2) * ext;
    }
    var yb = y0 + bh + ext * s2 + 16;
    svg += '<line class="dim" x1="' + x0 + '" y1="' + yb + '" x2="' + (x0 + bw) + '" y2="' + yb + '"/><line class="dim" x1="' + x0 + '" y1="' + (yb - 5) + '" x2="' + x0 + '" y2="' + (yb + 5) + '"/><line class="dim" x1="' + (x0 + bw) + '" y1="' + (yb - 5) + '" x2="' + (x0 + bw) + '" y2="' + (yb + 5) + '"/>';
    svg += '<text x="' + (x0 + bw / 2) + '" y="' + (yb + 16) + '" text-anchor="middle">' + dec(l) + ' m</text>';
    var xr = x0 - 14;
    svg += '<line class="dim" x1="' + xr + '" y1="' + y0 + '" x2="' + xr + '" y2="' + (y0 + bh) + '"/><line class="dim" x1="' + (xr - 5) + '" y1="' + y0 + '" x2="' + (xr + 5) + '" y2="' + y0 + '"/><line class="dim" x1="' + (xr - 5) + '" y1="' + (y0 + bh) + '" x2="' + (xr + 5) + '" y2="' + (y0 + bh) + '"/>';
    svg += '<text x="' + (xr - 6) + '" y="' + (y0 + bh / 2) + '" text-anchor="middle" transform="rotate(-90 ' + (xr - 6) + ' ' + (y0 + bh / 2) + ')">' + dec(w) + ' m</text>';
    area = w * l;
    var koko = dec(w) + ' × ' + dec(l) + ' m';
    if (t === 'bins') { koko = Lb.bins + ': ' + n; area = null; }
    return { svg: '<svg viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-label="' + esc(koko) + '">' + defs + svg + '</svg>', area: area, areaT: areaT, koko: koko };
  }

  function update() {
    if (!cur) return;
    var r = svgPlan();
    plans.forEach(function (p) { p.innerHTML = r.svg; });
    var ms = $$('input[name=malli]:checked', form).map(function (c) { return c.value; });
    var items = [];
    items.push([cur.n, ms.join(', ')]);
    if (r.koko) items.push([Lb.inner, r.koko]);
    if (r.area) items.push([Lb.area, dec(r.area) + ' m²' + (r.areaT ? ' + ' + dec(r.areaT) + ' m²' : '')]);
    if (cur.t === 'count') items.push([Lb.qty.replace(/ \(.*\)/, ''), (fN.value || 1) + '']);
    var del = $('input[name=toimitus]:checked', form);
    if (del) items.push([Lb.delivery, del.value]);
    dl.innerHTML = items.filter(function (x) { return x[1]; }).map(function (x) { return '<div><dt>' + esc(x[0]) + '</dt><dd>' + esc(x[1]) + '</dd></div>'; }).join('');
    var m = selModel(), price = (m && cur.t !== 'count') ? m.p : cur.p;
    if (cur.t === 'count' && ms.length) {
      var ps = $$('input[name=malli]:checked', form).map(function (c) { return cur.m[+c.dataset.i].p; });
      price = ps.length === 1 ? ps[0] : null;
    }
    var ph = price ? '<small>' + Lb.from + '</small> ' + eur(price) : '';
    priceEls.forEach(function (e) { e.innerHTML = ph; });
    form.koko.value = r.koko || '';
    form.ala.value = r.area ? dec(r.area) + ' m²' + (r.areaT ? ' + ' + (cur.t === 'sauna' ? Lb.terrace.toLowerCase() : Lb.porch.toLowerCase()) + ' ' + dec(r.areaT) + ' m²' : '') : '';
  }

  $$('input[name=tuote]', form).forEach(function (r) { r.addEventListener('change', function () { setProduct(r.dataset.k); }); });
  boxM.addEventListener('change', applyModel);
  form.addEventListener('input', function (e) { if (e.target.name !== 'tuote') update(); });
  form.addEventListener('change', function (e) { if (e.target.name === 'toimitus' || e.target.name === 'lisat') update(); });

  var k0 = qs.get('tuote');
  var start = $$('input[name=tuote]', form).filter(function (r) { return r.dataset.k === k0; })[0] || $('input[name=tuote]', form);
  start.checked = true;
  setProduct(start.dataset.k, qs.get('malli'));
})();
