/* Jääkärihirsi Oy (jaakarihirsi.com) – NordicHost cPanel "AI App Hosting" -palvelin.
 *
 * Tarjoilee valmiiksi rakennetun sivuston site/-kansiosta ja käsittelee yhteydenottolomakkeen (POST /lahetys).
 * Sivusto rakennetaan omalla koneella (python3 build.py) ja site/ commitoidaan repoon – palvelimella ei tarvita Pythonia.
 *
 * Ympäristömuuttujat (cPanel → sovelluksen asetukset):
 *   PORT            palvelimen antama portti (asettuu yleensä automaattisesti)
 *   MAIL_TO         mihin yhteydenotot ja tarjouspyynnöt tulevat (oletus info@jaakarihirsi.com)
 *   MAIL_FROM       lähettäjä, saman domainin osoite (oletus no-reply@jaakarihirsi.com)
 *   SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS
 *                   cPanelin sähköpostitilin SMTP-tiedot. Jos puuttuvat, käytetään palvelimen sendmailia.
 *   MAIL_DRYRUN=1   testaus: viestiä ei lähetetä
 */
'use strict';
const http = require('http');
const fs = require('fs');
const path = require('path');
const { URLSearchParams } = require('url');

const ROOT = path.join(__dirname, 'site');
const PORT = process.env.PORT || 3000;
const MAIL_TO = process.env.MAIL_TO || 'info@jaakarihirsi.com';
const MAIL_FROM = process.env.MAIL_FROM || 'no-reply@jaakarihirsi.com';
const SITE_NAME = 'Jääkärihirsi';
const THANKS = '/kiitos/';
const THANKS_SV = '/sv/tack/';
// Lomakkeet: piilokenttä "lomake" valitsee kentät. Oletus = yhteydenotto.
const FORMS = {
  yhteydenotto: {
    subject: 'Yhteydenotto verkkosivulta', error: '/yhteystiedot/?virhe=1#lomake', errorSv: '/sv/kontakt/?virhe=1#lomake',
    fields: [['tuote', 'Tuote'], ['nimi', 'Nimi'], ['puhelin', 'Puhelin'], ['email', 'Sähköposti'], ['paikkakunta', 'Paikkakunta'], ['viesti', 'Viesti'], ['sivu', 'Lähetetty sivulta']],
  },
  tarjous: {
    subject: 'Tarjouspyyntö verkkosivulta', error: '/tarjouspyynto/?virhe=1#lomake', errorSv: '/sv/offert/?virhe=1#lomake',
    fields: [['tuote', 'Tuote'], ['malli', 'Malli'], ['koko', 'Koko (leveys × pituus)'], ['ala', 'Pinta-ala'], ['runko', 'Runko'],
      ['katto', 'Katto'], ['lisat', 'Lisävalinnat'], ['toimitus', 'Toimitustapa'], ['paikkakunta', 'Toimituspaikkakunta'], ['aikataulu', 'Aikataulu'],
      ['viesti', 'Lisätietoja'], ['nimi', 'Nimi'], ['puhelin', 'Puhelin'], ['email', 'Sähköposti'], ['sivu', 'Lähetetty sivulta']],
  },
};
// Vanhan sivuston osoitteet (build.py kirjoittaa site/redirects.json)
let REDIRECTS = {};
try { REDIRECTS = JSON.parse(fs.readFileSync(path.join(ROOT, 'redirects.json'), 'utf8')); } catch (e) {}

const TYPES = {
  '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8', '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json', '.xml': 'application/xml; charset=utf-8', '.txt': 'text/plain; charset=utf-8',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon', '.mp4': 'video/mp4', '.woff2': 'font/woff2', '.pdf': 'application/pdf',
};
const SECURITY = {
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'X-Frame-Options': 'SAMEORIGIN',
};

let transport = null;
function mailer() {
  if (transport) return transport;
  const nodemailer = require('nodemailer');
  if (process.env.MAIL_DRYRUN) return (transport = nodemailer.createTransport({ jsonTransport: true }));
  transport = process.env.SMTP_HOST
    ? nodemailer.createTransport({
        host: process.env.SMTP_HOST, port: +(process.env.SMTP_PORT || 465), secure: +(process.env.SMTP_PORT || 465) === 465,
        auth: { user: process.env.SMTP_USER, pass: process.env.SMTP_PASS },
      })
    : nodemailer.createTransport({ sendmail: true, newline: 'unix', path: '/usr/sbin/sendmail' });
  return transport;
}

function redirect(res, to, code = 303) {
  res.writeHead(code, { Location: to, ...SECURITY });
  res.end();
}

function send(res, status, file, extra = {}, req = null, size = 0) {
  const ext = path.extname(file).toLowerCase();
  const headers = { 'Content-Type': TYPES[ext] || 'application/octet-stream', ...SECURITY, ...extra };
  if (ext === '.html') headers['Cache-Control'] = 'no-cache';
  else if (file.includes(`${path.sep}img${path.sep}`)) headers['Cache-Control'] = 'public, max-age=31536000, immutable';
  else headers['Cache-Control'] = 'public, max-age=86400';
  // Video: Range-tuki (Safari/iOS ei toista videota ilman 206-vastauksia)
  if (ext === '.mp4' && size) {
    headers['Accept-Ranges'] = 'bytes';
    const m = /^bytes=(\d*)-(\d*)$/.exec((req && req.headers.range) || '');
    if (m) {
      let start = m[1] === '' ? size - +m[2] : +m[1];
      let end = m[1] !== '' && m[2] !== '' ? Math.min(+m[2], size - 1) : size - 1;
      if (start >= size || start > end) { res.writeHead(416, { 'Content-Range': `bytes */${size}`, ...SECURITY }); return res.end(); }
      res.writeHead(206, { ...headers, 'Content-Range': `bytes ${start}-${end}/${size}`, 'Content-Length': end - start + 1 });
      return fs.createReadStream(file, { start, end }).pipe(res);
    }
    headers['Content-Length'] = size;
  }
  res.writeHead(status, headers);
  if (req && req.method === 'HEAD') return res.end();
  fs.createReadStream(file).pipe(res);
}

function notFound(res) {
  send(res, 404, path.join(ROOT, '404.html'));
}

function serveStatic(req, res, url) {
  let rel;
  try { rel = decodeURIComponent(url.pathname); } catch { return notFound(res); }
  const file = path.normalize(path.join(ROOT, rel));
  if (!file.startsWith(ROOT)) return notFound(res);
  fs.stat(file, (err, st) => {
    if (!err && st.isFile()) return send(res, 200, file, {}, req, st.size);
    if (!err && st.isDirectory()) {
      if (!rel.endsWith('/')) return redirect(res, rel + '/' + url.search, 301);
      const index = path.join(file, 'index.html');
      return fs.stat(index, (e2, s2) => (!e2 && s2.isFile() ? send(res, 200, index) : notFound(res)));
    }
    notFound(res);
  });
}

function clean(s) {
  return String(s || '').replace(/[\r\n]+/g, ' ').trim();
}

function handleForm(req, res) {
  let body = '';
  req.on('data', (c) => {
    body += c;
    if (body.length > 50000) req.destroy();
  });
  req.on('end', async () => {
    const sp = new URLSearchParams(body);
    const f = {};
    for (const [k, v] of sp) f[k] = f[k] ? `${f[k]}, ${v}` : v;
    // Roskapostisuoja: piilokenttä täytetty tai lomake täytetty alle 3 sekunnissa → hiljainen "kiitos"
    const sv = f.kieli === 'sv';
    const OK = sv ? THANKS_SV : THANKS;
    if (f['bot-field']) return redirect(res, OK);
    const ts = parseInt(f.ts, 10);
    if (ts && Date.now() / 1000 - ts < 3) return redirect(res, OK);
    const form = FORMS[f.lomake] || FORMS.yhteydenotto;
    const ERROR = sv ? form.errorSv : form.error;
    // Pakollinen: nimi + puhelin tai sähköposti
    if (!clean(f.nimi) || (!clean(f.puhelin) && !clean(f.email))) return redirect(res, ERROR);
    if (clean(f.email) && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(clean(f.email))) return redirect(res, ERROR);

    const text = form.fields.filter(([k]) => String(f[k] || '').trim())
      .map(([k, label]) => `${label}:\n${String(f[k]).trim()}`).join('\n\n');
    try {
      await mailer().sendMail({
        from: `"${SITE_NAME} – verkkosivu" <${MAIL_FROM}>`,
        to: MAIL_TO,
        replyTo: clean(f.email) || undefined,
        subject: `${form.subject}${sv ? ' (svenska)' : ''}: ${clean(f.tuote) ? clean(f.tuote) + ' – ' : ''}${clean(f.nimi)}`,
        text: `${text}\n\n—\nLähetetty verkkosivun lomakkeella (${SITE_NAME}).`,
      });
      redirect(res, OK);
    } catch (e) {
      console.error('Lomakkeen lähetys epäonnistui:', e.message);
      redirect(res, ERROR.replace('virhe=1', 'virhe=2'));
    }
  });
}

const server = http.createServer((req, res) => {
  const url = new URL(req.url, 'http://localhost');
  // juuri → www (kanoninen osoite on www.jaakarihirsi.com, kuten vanhalla sivulla)
  const host = (req.headers.host || '').toLowerCase();
  if (host === 'jaakarihirsi.com') return redirect(res, `https://www.jaakarihirsi.com${req.url}`, 301);
  const rp = url.pathname.endsWith('/') ? url.pathname : url.pathname + '/';
  if (rp === '/redirects.json/') return notFound(res);
  if (REDIRECTS[rp]) return redirect(res, REDIRECTS[rp], 301);
  if (req.method === 'POST' && url.pathname === '/lahetys') return handleForm(req, res);
  if (req.method !== 'GET' && req.method !== 'HEAD') {
    res.writeHead(405, { Allow: 'GET, HEAD', ...SECURITY });
    return res.end();
  }
  serveStatic(req, res, url);
});

server.listen(PORT, () => console.log(`Jääkärihirsi käynnissä portissa ${PORT}`));
