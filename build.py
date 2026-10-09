# -*- coding: utf-8 -*-
"""Staattisen sivuston generaattori – Jääkärihirsi Oy (jaakarihirsi.com), hirsirakentaja Kortesjärvi.

    python3 build.py                    -> site/ NordicHostiin (Node, server.js) + ../jaakarihirsi-nordichost.zip
    HOSTING=webhotelli python3 build.py -> tavallinen webhotelli (PHP-lomake + .htaccess)
    HOSTING=netlify python3 build.py --preview --artifact -> esikatselu Claude-artifaktina (preview/)

Tekstit (fi + sv): content.py. Kuvat: src/kuvat/ (-ai = Higgsfield-kuva). Tyylit src/style.css, toiminnot src/app.js.
"""
import json
import math
import os
import re
import shutil
import sys
import zipfile

from PIL import Image, ImageDraw, ImageFont, ImageOps

from content import BUILDINGS, COMPANY, ITEM_PRICES, PROD, PRODUCTS, REDIRECTS, SHOW_PRICES, T
os.environ.setdefault("HOSTING", "nordichost")
from hosting import HOSTING, form_attrs, hidden_fields, write_host_files

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")
SRC = os.path.join(ROOT, "src")
KUVAT = os.path.join(SRC, "kuvat")
IMG_OUT = os.path.join(SITE, "img")
BASE_URL = f"https://www.{COMPANY['domain']}"
DEMO = HOSTING == "netlify"
TEL = f"tel:{COMPANY['intl']}"
PHONE = COMPANY["phone"]
SITEMAP = []
VERSION = "1"
WIDTHS = [480, 800, 1200, 1600, 2000]
IMG_DIMS, IMG_WS = {}, {}
YEAR = 2026
TODAY = "2026-10-03"
GREEN = (49, 113, 75)
# Groweon asentamat seuranta ja chat (vanhalta sivulta 9.10.2026): GTM (GA4 tagin kautta), Cookiebot + Google consent mode, Groweo-chatti.
# Vain tuotantobuildissa – ei Netlify-/artifakti-esikatselussa.
TRACKING = not DEMO
GTM_ID = "GTM-PTT7B5V"
GA4_ID = "G-8FRK563X4T"
COOKIEBOT_ID = "55b15f94-16e4-4f7f-9de3-434403dc6c79"
GROWEO_WS = "69170e21fa3dbe6f156a884a"


def tracking_head():
    if not TRACKING:
        return ""
    return f'''<script data-cookieconsent="ignore">window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}
gtag("consent","default",{{ad_personalization:"denied",ad_storage:"denied",ad_user_data:"denied",analytics_storage:"denied",functionality_storage:"denied",personalization_storage:"denied",security_storage:"denied",wait_for_update:500}});
gtag("set","ads_data_redaction",true);gtag("set","url_passthrough",true);
dataLayer.push({{"event":"pageload","ga4-id":"{GA4_ID}"}});</script>
<script id="Cookiebot" src="https://consent.cookiebot.com/uc.js" data-cbid="{COOKIEBOT_ID}" data-culture="{L["lang"].upper()}" data-blockingmode="auto" type="text/javascript"></script>
<script data-cookieconsent="ignore">(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{GTM_ID}');</script>'''


def tracking_body_start():
    if not TRACKING:
        return ""
    return (f'<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}" height="0" width="0" '
            'style="display:none;visibility:hidden"></iframe></noscript>')


def tracking_body_end():
    if not TRACKING:
        return ""
    return f'<script src="https://engine.groweo.com/groweoApp/groweoApp.js" workspaceid="{GROWEO_WS}" data-cookieconsent="ignore"></script>'

L = T["fi"]  # nykyinen kieli (asetetaan build_lang():ssa)

# Sivuparit hreflangia ja kielivalitsinta varten: avain -> (fi, sv)
PAIRS = {"home": ("/", "/sv/"), "hub": ("/piharakennukset/", "/sv/gardsbyggnader/"), "company": ("/yritys/", "/sv/foretaget/"),
         "quote": ("/tarjouspyynto/", "/sv/offert/"), "contact": ("/yhteystiedot/", "/sv/kontakt/"),
         "privacy": ("/tietosuoja/", "/sv/dataskydd/"), "thanks": ("/kiitos/", "/sv/tack/")}
for _p in PRODUCTS:
    PAIRS[_p[0]] = (_p[1], _p[2])
PATH_KEY = {v: k for k, pair in PAIRS.items() for v in pair}


def esc(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def strip(t):
    return re.sub("<[^>]+>", "", t)


def eur(v):
    return f"{v:,}".replace(",", " ") + " €"


def ppath(key, lang=None):
    return PAIRS[key][0 if (lang or L["lang"]) == "fi" else 1]


ICONS = {
    "phone": '<path d="M4 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L14 13l5 2v4a2 2 0 0 1-2 2C9.5 21 3 14.5 3 6a2 2 0 0 1 1-2Z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "pin": '<path d="M12 21s-6-5.5-6-11a6 6 0 0 1 12 0c0 5.5-6 11-6 11z"/><circle cx="12" cy="10" r="2.2"/>',
    "clock": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    "x": '<path d="M6 6l12 12M18 6 6 18"/>',
    "left": '<path d="m15 5-7 7 7 7"/>',
    "right": '<path d="m9 5 7 7-7 7"/>',
    "down": '<path d="m6 9 6 6 6-6"/>',
    "globe": '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.5 2.6 3.6 5.4 3.6 8.5s-1.1 5.9-3.6 8.5c-2.5-2.6-3.6-5.4-3.6-8.5s1.1-5.9 3.6-8.5Z"/>',
    "log": '<rect x="3" y="5" width="18" height="4" rx="2"/><rect x="3" y="10" width="18" height="4" rx="2"/><rect x="3" y="15" width="18" height="4" rx="2"/>',
    "ruler": '<path d="M3 16 16 3l5 5L8 21z"/><path d="m7 12 2 2M10 9l2 2M13 6l2 2"/>',
    "truck": '<path d="M3 6h11v10H3zM14 9h4l3 3v4h-7"/><circle cx="7" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>',
}


def icon(name, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'


def logo(cls="brand"):
    """Vanhan logon henkeen: sanamerkki JÄÄKÄRIHIRSI + vihreä hirsipalkki."""
    return (f'<a class="{cls}" href="{L["home"]}" aria-label="{COMPANY["name"]}, {L["ui"]["home"].lower()}">'
            f'<span class="wm"><b>JÄÄKÄRIHIRSI</b><small>KORTESJÄRVI</small></span></a>')


# ---------------------------------------------------------------------------
# Kuvat
# ---------------------------------------------------------------------------

IMG_SRC = {os.path.splitext(f)[0]: os.path.join(KUVAT, f) for f in sorted(os.listdir(KUVAT))
           if f.lower().endswith((".jpg", ".jpeg", ".png"))}


def _resize_set(name, path):
    meta = os.path.join(IMG_OUT, f".{name}.json")
    if os.path.exists(meta) and os.path.getmtime(meta) > os.path.getmtime(path):
        d = json.load(open(meta))
        IMG_DIMS[name], IMG_WS[name] = tuple(d["dims"]), d["ws"]
        if all(os.path.exists(os.path.join(IMG_OUT, f"{name}-{w}.webp")) for w in d["ws"]):
            return
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    if im.width > WIDTHS[-1]:
        im = im.resize((WIDTHS[-1], round(im.height * WIDTHS[-1] / im.width)), Image.LANCZOS)
    IMG_DIMS[name] = im.size
    ws = [w for w in WIDTHS if w < im.width] + [im.width]
    IMG_WS[name] = ws
    for w in ws:
        im.resize((w, round(im.height * w / im.width)), Image.LANCZOS).save(
            os.path.join(IMG_OUT, f"{name}-{w}.webp"), "WEBP", quality=80, method=5)
    json.dump({"dims": im.size, "ws": ws}, open(meta, "w"))


def build_images():
    os.makedirs(IMG_OUT, exist_ok=True)
    for f in os.listdir(IMG_OUT):  # poista kuvat, joiden lähde on poistettu
        base = re.sub(r"-\d+\.webp$", "", f[1:-5] if f.startswith(".") and f.endswith(".json") else f)
        if f not in ("og.jpg", "logo-512.png") and base not in IMG_SRC:
            os.remove(os.path.join(IMG_OUT, f))
    for name, path in IMG_SRC.items():
        _resize_set(name, path)


def img(name, alt, sizes="100vw", cls="", eager=False, style=""):
    w0, h0 = IMG_DIMS[name]
    ws = IMG_WS[name]
    srcset = ", ".join(f"/img/{name}-{w}.webp {w}w" for w in ws)
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    st = f' style="{style}"' if style else ""
    return (f'<img{c} src="/img/{name}-{ws[min(1, len(ws) - 1)]}.webp" srcset="{srcset}" sizes="{sizes}" '
            f'width="{w0}" height="{h0}" alt="{esc(alt)}" {load}{st}>')


def src_of(name, i=-1):
    return f"/img/{name}-{IMG_WS[name][i]}.webp"


# ---------------------------------------------------------------------------
# Yhteiset palat
# ---------------------------------------------------------------------------

def btn(label, href, cls="btn btn-primary", ic="arrow"):
    return f'<a class="{cls}" href="{href}">{label}{icon(ic) if ic else ""}</a>'


def btn_call(cls="btn btn-line", label=None):
    return f'<a class="{cls}" href="{TEL}">{icon("phone")}<span>{label or PHONE}</span></a>'


def price_html(price, cls="price"):
    if not SHOW_PRICES:
        return ""
    if price is None:
        return ""
    return f'<span class="{cls}"><small>{L["ui"]["from"]}</small> {eur(price)}</span>'


def cat_price(key):
    """Tuoteryhmän alkaen-hinta vain, jos jokaisella mallilla on asiakkaan ilmoittama hinta (ei johdettuja hintoja)."""
    P = T["fi"]["P"][key]
    if P.get("from"):
        return P["from"]
    ps = [m[3] for m in P["models"]]
    return min(ps) if ps and all(ps) else None


def quote_url(key=None, model=None):
    u = L["paths"]["quote"]
    if key:
        u += f"?tuote={key}"
        if model:
            u += "&malli=" + model.replace(" ", "+")
    return u + "#lomake"


def header(current):
    P = L["P"]
    sub = "".join(f'<a href="{ppath(k)}"{" aria-current=page" if current == ppath(k) else ""}>'
                  f'{img(PROD[k][3], P[k]["card"], "64px")}<span><b>{P[k]["name"]}</b><small>{P[k]["short"]}</small></span></a>'
                  for k in BUILDINGS)
    links = []
    for t, u in L["nav"]:
        cur = " aria-current=page" if current == u or (u == L["paths"]["hub"] and current.startswith(u)) else ""
        if u == L["paths"]["hub"]:
            links.append(f'<div class="dd"><a href="{u}"{cur}>{t}{icon("down")}</a><div class="dd-menu">{sub}</div></div>')
        else:
            links.append(f'<a href="{u}"{cur}>{t}</a>')
    key = PATH_KEY.get(current, "home")
    other = ppath(key, L["other"])
    lang = (f'<a class="lang" href="{other}" hreflang="{L["other"]}" lang="{L["other"]}" title="{L["other_label"]}">'
            f'{icon("globe")}<span>{L["other_short"]}</span></a>')
    mlinks = "".join(f'<a href="{u}">{t}{icon("arrow")}</a>' for t, u in L["nav"])
    msub = "".join(f'<a class="msub" href="{ppath(k)}">{P[k]["name"]}</a>' for k in BUILDINGS)
    return f'''<header class="hdr">
  <div class="hdr-in">
    {logo()}
    <nav class="nav" aria-label="Menu">{"".join(links)}</nav>
    {lang}
    <a class="btn btn-primary btn-sm hdr-q" href="{L["paths"]["quote"]}">{L["ui"]["quote"]}</a>
    <button class="burger" aria-label="{L["ui"]["menu"]}" aria-expanded="false"><span></span><span></span></button>
  </div>
  <nav class="mnav" aria-label="{L["ui"]["menu"]}">{mlinks}<div class="msubs">{msub}</div>
    <a class="mlang" href="{other}" lang="{L["other"]}">{icon("globe")}{L["other_label"]}</a>
    <div class="mnav-foot">{btn_call("btn btn-primary", L["ui"]["call"] + " " + PHONE)}{btn(L["ui"]["quote"], L["paths"]["quote"], "btn btn-line", "")}</div></nav>
</header>'''


def footer():
    u = L["ui"]
    P = L["P"]
    demo = f'<p class="demo-note">{u["demo"]}</p>' if DEMO else ""
    prods = "".join(f'<li><a href="{ppath(p[0])}">{P[p[0]]["name"]}</a></li>' for p in PRODUCTS)
    return f'''<footer class="ftr">
  <div class="wrap">
    <div class="ftr-grid">
      <div class="ftr-brand">{logo("brand brand-ftr")}<p>{u["made_in"]}</p>{btn(u["quote"], L["paths"]["quote"], "btn btn-primary")}</div>
      <div><h3>{u["products"]}</h3><ul>{prods}</ul></div>
      <div><h3>{u["contact"]}</h3><ul><li><a href="{TEL}">{PHONE}</a></li>
        <li><a href="mailto:{COMPANY["email"]}">{COMPANY["email"]}</a></li>
        <li>{COMPANY["street"]}<br>{COMPANY["zip"]} {COMPANY["city"]}</li><li>{u["weekdays"]}</li></ul></div>
    </div>
    <div class="ftr-bottom"><span>© {YEAR} {COMPANY["name"]} · Y-tunnus {COMPANY["ytunnus"]}</span>
      <span><a href="{L["paths"]["company"]}">{u["company"]}</a> · <a href="{L["paths"]["privacy"]}">{u["privacy"]}</a> · {f'<a href="javascript:Cookiebot.renew()">{u["cookies"]}</a> · ' if TRACKING else ""}<a href="{ppath("home", L["other"])}" lang="{L["other"]}">{L["other_label"]}</a></span></div>
    {demo}
  </div>
</footer>
<div class="mbar"><a class="btn btn-line" href="{TEL}">{icon("phone")}<span>{u["call"]}</span></a>
  <a class="btn btn-primary" href="{L["paths"]["quote"]}">{icon("ruler")}<span>{u["quote"]}</span></a></div>
<div class="lb" hidden><button class="lb-x" aria-label="{u["close"]}">{icon("x")}</button><button class="lb-p" aria-label="{u["prev"]}">{icon("left")}</button>
<figure><img alt=""><figcaption></figcaption></figure><button class="lb-n" aria-label="{u["next"]}">{icon("right")}</button></div>'''


def org_schema():
    return {
        "@context": "https://schema.org", "@type": "HomeAndConstructionBusiness", "@id": BASE_URL + "/#yritys",
        "name": COMPANY["name"], "alternateName": "Jääkärihirsi",
        "url": BASE_URL + "/", "telephone": COMPANY["intl"], "email": COMPANY["email"], "image": BASE_URL + "/img/og.jpg",
        "logo": BASE_URL + "/img/logo-512.png", "taxID": COMPANY["ytunnus"],
        "description": "Hirsirakentaja Kauhavan Kortesjärvellä: pihasaunat, pihavarastot, leikkimökit, ulko-WC:t, roskakatokset, hirsikalusteet ja pihakoristeet mittatilauksena kotimaisesta höylähirrestä.",
        "address": {"@type": "PostalAddress", "streetAddress": COMPANY["street"], "postalCode": COMPANY["zip"],
                    "addressLocality": COMPANY["city"], "addressRegion": COMPANY["region"], "addressCountry": "FI"},
        "geo": {"@type": "GeoCoordinates", "latitude": COMPANY["geo"][0], "longitude": COMPANY["geo"][1]},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                                       "opens": "07:00", "closes": "18:00"}],
        "areaServed": {"@type": "Country", "name": "Suomi"},
        "knowsAbout": ["Pihasauna", "Hirsisauna", "Pihavarasto", "Puuvaja", "Leikkimökki", "Ulko-WC", "Roskakatos",
                       "Hirsikalusteet", "Maitolaituri", "Koristekaivo", "Höylähirsi"],
    }


def breadcrumb(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": BASE_URL + u} for i, (n, u) in enumerate(items)]}


def faq_schema(faq):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": a, "acceptedAnswer": {"@type": "Answer", "text": b}} for a, b in faq]}


def page(path, title, description, body, schema=None, noindex=False, cls="", preload=None):
    if not noindex and path != "/404.html":
        SITEMAP.append(path)
    robots = '<meta name="robots" content="noindex">' if (noindex or DEMO) else '<meta name="robots" content="max-image-preview:large">'
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>'
                 for s in [org_schema()] + (schema or []))
    key = PATH_KEY.get(path)
    alts = ""
    if key and not noindex:
        fi, sv = PAIRS[key]
        alts = (f'<link rel="alternate" hreflang="fi" href="{BASE_URL}{fi}">\n<link rel="alternate" hreflang="sv" href="{BASE_URL}{sv}">\n'
                f'<link rel="alternate" hreflang="x-default" href="{BASE_URL}{fi}">')
    pre = ""
    if preload:
        pre = (f'<link rel="preload" as="image" imagesrcset="{", ".join(f"/img/{preload}-{w}.webp {w}w" for w in IMG_WS[preload])}" '
               f'imagesizes="(max-width:900px) 100vw, 60vw" fetchpriority="high">')
    html = f'''<!doctype html>
<html lang="{L["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{BASE_URL}{path if path != '/404.html' else '/'}">
{alts}
{robots}
<meta name="theme-color" content="#faf7f2">
<meta property="og:type" content="website">
<meta property="og:locale" content="{L["locale"]}">
<meta property="og:site_name" content="{COMPANY["name"]}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{BASE_URL}{path}">
<meta property="og:image" content="{BASE_URL}/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
{tracking_head()}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" data-cookieconsent="ignore">
<link rel="stylesheet" href="/style.css?v={VERSION}">
{pre}
{ld}
</head>
<body class="{cls}">
{tracking_body_start()}
<a class="skip" href="#main">{L["ui"]["skip"]}</a>
{header(path)}
<main id="main">
{body}
</main>
{footer()}
<script src="/app.js?v={VERSION}" defer data-cookieconsent="ignore"></script>
{tracking_body_end()}
</body>
</html>
'''
    out = os.path.join(SITE, path.strip("/"), "index.html") if not path.endswith(".html") else os.path.join(SITE, path.strip("/"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)


def accent(t):
    """Kaksisävyinen otsikko: viimeinen sana vihreällä (ellei otsikossa jo ole <em>)."""
    if "<em>" in t or " " not in t:
        return t
    head, last = t.rsplit(" ", 1)
    return f"{head} <em>{last}</em>"


def sec_head(title, text=""):
    right = f'<p>{text}</p>' if text else ""
    return f'<div class="sec-head"><h2>{accent(title)}</h2>{right}</div>'


def checks(items, cls="checks"):
    return f'<ul class="{cls}">' + "".join(f"<li>{icon('check')}{esc(b)}</li>" for b in items) + "</ul>"


def faq_html(faq):
    return '<div class="faq">' + "".join(
        f'<details class="rv"><summary>{esc(a)}{icon("down")}</summary><p>{esc(b)}</p></details>' for a, b in faq) + "</div>"


def hero(h1, lead, image, alt, pos="center", ctas="", extra=""):
    """Alasivun hero: pyöristetty kehys, vaalea tekstipaneeli vasemmalla, kuva oikealla."""
    return f'''<section class="shero"><div class="shero-in">
  <div class="shero-txt">
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    {extra}{ctas}
  </div>
  <figure class="shero-img">{img(image, alt, "(max-width:900px) 100vw, 60vw", eager=True, style=f"object-position:{pos}")}</figure>
</div></section>'''


def plain_hero(h1, lead=""):
    lead = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<section class="phero"><div class="wrap"><h1>{accent(h1)}</h1>{lead}</div></section>'


def product_tiles(keys, cls="tiles"):
    P = L["P"]
    out = []
    for i, k in enumerate(keys):
        p = PROD[k]
        out.append(f'''<a class="tile rv" style="--d:{(i % 4) * 50}ms" href="{ppath(k)}">
  <div class="tile-img">{img(p[3], P[k]["card"], "(max-width:700px) 50vw, 25vw")}</div>
  <div class="tile-b"><h3>{P[k]["name"]}</h3><p>{P[k]["short"]}</p>{price_html(cat_price(k))}</div></a>''')
    return f'<div class="{cls}">' + "".join(out) + "</div>"


# ---------------------------------------------------------------------------
# Kartta: Suomi + 200 km säde Kortesjärveltä
# ---------------------------------------------------------------------------

LON0, LON1, LAT0, LAT1 = 19.4, 31.7, 59.65, 70.15
K_LAT = math.cos(math.radians(64.5))
MW = 400
MS = MW / ((LON1 - LON0) * K_LAT)
MH = round((LAT1 - LAT0) * MS)
CITIES = [("Vaasa", 63.096, 21.616), ("Kokkola", 63.838, 23.131), ("Seinäjoki", 62.790, 22.840), ("Jyväskylä", 62.242, 25.747),
          ("Oulu", 65.012, 25.465), ("Tampere", 61.498, 23.761), ("Helsinki", 60.170, 24.938), ("Rovaniemi", 66.503, 25.729)]


def mxy(lat, lon):
    return (lon - LON0) * K_LAT * MS, (LAT1 - lat) * MS


def svg_map():
    rings = json.load(open(os.path.join(SRC, "fin_rings.json")))
    paths = []
    for r in rings:
        pts = [mxy(lat, lon) for lon, lat in r]
        paths.append("M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + "Z")
    hx, hy = mxy(*COMPANY["geo"])
    rr = COMPANY["radius"] / 111.2 * MS
    cities = []
    for n, la, lo in CITIES:
        x, y = mxy(la, lo)
        d = math.hypot((la - COMPANY["geo"][0]) * 111.2, (lo - COMPANY["geo"][1]) * 111.2 * math.cos(math.radians(63.3)))
        inside = " in" if d <= COMPANY["radius"] else ""
        anchor = "end" if n in ("Vaasa",) else "start"
        dx = -7 if anchor == "end" else 7
        cities.append(f'<g class="city{inside}"><circle cx="{x:.1f}" cy="{y:.1f}" r="3"/><text x="{x + dx:.1f}" y="{y + 4:.1f}" text-anchor="{anchor}">{n}</text></g>')
    return f'''<svg viewBox="0 0 {MW} {MH}" role="img" aria-label="{esc(L["map_label"])}">
<defs><radialGradient id="rg"><stop offset="0" stop-color="#31714b" stop-opacity=".32"/><stop offset="1" stop-color="#31714b" stop-opacity=".1"/></radialGradient></defs>
<path class="land" d="{" ".join(paths)}"/>
<circle class="radius" cx="{hx:.1f}" cy="{hy:.1f}" r="{rr:.1f}" fill="url(#rg)"/>
{"".join(cities)}
<g class="hq"><circle cx="{hx:.1f}" cy="{hy:.1f}" r="11" class="halo"/><circle cx="{hx:.1f}" cy="{hy:.1f}" r="6"/>
<text x="{hx + 14:.1f}" y="{hy - 10:.1f}">Kortesjärvi</text></g></svg>'''


# ---------------------------------------------------------------------------
# Lomakkeet
# ---------------------------------------------------------------------------

def consent(fid):
    return f'<p class="check"><input type="checkbox" id="{fid}" required><label for="{fid}">{L["form"]["consent"]}</label></p>'


def contact_form(fid="ts-c", product=None):
    F = L["form"]
    P = L["P"]
    opts = f'<option value="">{F["choose"]}</option>' + "".join(
        f'<option{" selected" if k == product else ""}>{P[k]["name"]}</option>' for k in PROD) + f'<option>{F["other"]}</option>'
    return f'''<form class="panel form" id="lomake" name="yhteydenotto" method="POST" {form_attrs()} novalidate>
      {hidden_fields("yhteydenotto")}<input type="hidden" name="lomake" value="yhteydenotto"><input type="hidden" name="kieli" value="{L["lang"]}">
      <h3>{F["title"]}</h3>
      <p class="err" data-err>{F["err"]}</p><p class="err senderr">{F["senderr"]}</p>
      <div class="fgrid">
        <label class="f">{F["name"]}<input name="nimi" required autocomplete="name"></label>
        <label class="f">{F["phone"]}<input name="puhelin" type="tel" autocomplete="tel"></label>
        <label class="f">{F["email"]}<input name="email" type="email" autocomplete="email"></label>
        <label class="f">{F["town"]}<input name="paikkakunta" autocomplete="address-level2"></label>
        <label class="f full">{F["product"]}<select name="tuote">{opts}</select></label>
        <label class="f full">{F["msg"]}<textarea name="viesti" rows="4"></textarea></label>
      </div>
      {consent(fid)}
      <button class="btn btn-primary" type="submit">{F["send"]}{icon("arrow")}</button>
    </form>'''


def contact_section(product=None):
    return f'''<section class="sec alt" id="yhteys"><div class="wrap contact-grid">
  <div class="contact-info rv">
    <h2>{L["contact_h"]}</h2>
    <p class="muted">{L["contact_p"]}</p>
    <a class="big-tel" href="{TEL}">{icon("phone")}{PHONE}</a>
    <a class="mail" href="mailto:{COMPANY["email"]}">{icon("mail")}{COMPANY["email"]}</a>
    <p class="addr">{icon("clock")}{L["ui"]["weekdays"]} · {L["ui"]["reach"]}</p>
    <p class="addr">{icon("pin")}{COMPANY["street"]}, {COMPANY["zip"]} {COMPANY["city"]}</p>
  </div>
  {contact_form(product=product)}
</div></section>'''


# ---------------------------------------------------------------------------
# Sivut
# ---------------------------------------------------------------------------

def build_home():
    why = "".join(f'<li class="rv" style="--d:{i * 60}ms">{icon(ic, "ic why-ic")}<div><h3>{t}</h3><p>{d}</p></div></li>'
                  for i, ((t, d), ic) in enumerate(zip(L["why"], ["log", "ruler", "truck"])))
    steps = "".join(f'<li class="rv" style="--d:{i * 60}ms"><span class="n">{i + 1}</span><h3>{t}</h3><p>{d}</p></li>'
                    for i, (t, d) in enumerate(L["steps"]))
    body = f'''<section class="xhero"><div class="xhero-in">
  <div class="xhero-img">{img("tuomas20-2", L["P"]["pihasauna"]["card"], "100vw", eager=True, style="object-position:50% 30%")}</div>
  <div class="xhero-b">
    <h1>{L["hero_h1"]}</h1>
    <div class="xhero-side">
      <p>{L["hero_lead"]}</p>
      <div class="btns">{btn(L["hero_cta"], L["paths"]["quote"] + "#lomake", "btn btn-white")}{btn_call("btn btn-glass")}</div>
    </div>
  </div>
</div></section>

<section class="sec" id="tuotteet"><div class="wrap">
  {sec_head(L["products_h"], L["products_p"])}
  {product_tiles([p[0] for p in PRODUCTS])}
</div></section>

<section class="sec alt"><div class="wrap why-grid">
  <div class="why-txt">
    <h2>{L["why_h"]}</h2>
    <ul class="why">{why}</ul>
  </div>
  <figure class="split-img why-img rv">{img(L["why_img"][0], L["why_img"][1], "(max-width:900px) 100vw, 45vw")}</figure>
</div></section>

<section class="sec"><div class="wrap">
  <div class="process">
    <figure class="process-img rv">{img(L["steps_img"][0], L["steps_img"][1], "(max-width:900px) 100vw, 45vw")}</figure>
    <div class="process-b"><h2>{L["steps_h"]}</h2><ol class="steps">{steps}</ol>
      <div class="btns">{btn(L["ui"]["quote"], L["paths"]["quote"] + "#lomake")}</div></div>
  </div>
</div></section>
{contact_section()}'''
    page(L["home"], L["home_title"], L["home_desc"], body, preload="tuomas20-2", cls="home")


def model_block(key, i, m):
    name, text, specs, price, ims = m
    main = ims[0]
    thumbs = "".join(f'<a class="th" href="{src_of(n)}" data-lb="{esc(name)}">{img(n, name, "120px")}</a>' for n in ims[1:5])
    more = "".join(f'<a href="{src_of(n)}" data-lb="{esc(name)}" hidden></a>' for n in ims[5:])
    return f'''<article class="model rv" id="{re.sub("[^a-z0-9]+", "-", name.lower())}">
  <div class="model-gal"><a class="main" href="{src_of(main)}" data-lb="{esc(name)}">{img(main, name, "(max-width:900px) 100vw, 50vw")}</a>
    {f'<div class="thumbs">{thumbs}</div>' if thumbs else ""}{more}</div>
  <div class="model-b">
    <h3>{name}</h3>
    <p>{text}</p>
    {checks(specs)}
    <div class="model-foot">{price_html(price, "price big")}{btn(L["ui"]["ask_this"], quote_url(key, name))}</div>
  </div>
</article>'''


def build_product(key):
    P = L["P"][key]
    p = PROD[key]
    url = ppath(key)
    crumbs = [(L["ui"]["home"], L["home"])]
    if key in BUILDINGS:
        crumbs.append((L["nav"][1][0], L["paths"]["hub"]))
    crumbs.append((P["name"], url))
    hero_img = p[3]
    pr = price_html(cat_price(key), "price hero-price") if SHOW_PRICES else ""
    ctas = f'<div class="btns">{btn(L["ui"]["quote"], quote_url(key))}{btn_call()}</div>'
    body = hero(P["h1"], P["lead"], hero_img, P["card"], P.get("hero_pos", "55% 50%"), ctas, pr)
    intro = "".join(f'<p{" class=big" if i == 0 else ""}>{t}</p>' for i, t in enumerate(P["intro"]))
    body += f'''<section class="sec"><div class="wrap split">
  <div class="split-txt rv"><h2>{P["intro_h"]}</h2>{intro}</div>
  <div class="listbox rv"><h3>{P["list_h"]}</h3>{checks(P["list"])}</div>
</div></section>'''
    if P.get("intro_img"):
        body = body.replace(f'<div class="listbox rv"><h3>{P["list_h"]}</h3>{checks(P["list"])}</div>\n</div></section>',
                            f'<figure class="split-img rv">{img(P["intro_img"], strip(P["intro_h"]), "(max-width:900px) 100vw, 45vw")}</figure>\n</div>'
                            f'<div class="wrap"><div class="listbox wide rv"><h3>{P["list_h"]}</h3>{checks(P["list"], "checks cols")}</div></div></section>')
    models = "".join(model_block(key, i, m) for i, m in enumerate(P["models"]))
    vat = f'<p class="muted small vat">{L["ui"]["vat"]}</p>' if SHOW_PRICES else ""
    body += f'<section class="sec pt0" id="mallit"><div class="wrap">{sec_head(P["models_h"])}<div class="models">{models}</div>{vat}</div></section>'
    if P.get("gallery"):
        gal = "".join(f'<a class="g rv" href="{src_of(n)}" data-lb="{esc(a)}">{img(n, a, "(max-width:700px) 50vw, 25vw")}</a>' for n, a in P["gallery"])
        body += f'<section class="sec pt0"><div class="wrap">{sec_head(P["gallery_h"])}<div class="gal model-gal">{gal}</div></div></section>'
    if P.get("band"):
        b_img, b_h, b_p = P["band"]
        body += f'''<section class="sec pt0"><div class="wrap"><a class="band rv" href="{quote_url(key)}"><div class="band-img">{img(b_img, b_h, "100vw")}</div>
  <div class="band-b"><h2>{b_h}</h2><p>{b_p}</p><span class="btn btn-white">{L["hero_cta"]}{icon("arrow")}</span></div></a></div></section>'''
    if P["faq"]:
        body += f'<section class="sec pt0"><div class="wrap narrow">{sec_head(L["ui"]["faq"])}{faq_html(P["faq"])}</div></section>'
    others = [k for k in PROD if k != key]
    body += f'<section class="sec pt0"><div class="wrap"><h2 class="h-sm">{L["ui"]["other_products"]}</h2>{product_tiles(others, "tiles tiles-sm")}</div></section>'
    body += contact_section(product=key)
    offers = [{"@type": "Offer", "price": m[3], "priceCurrency": "EUR", "name": m[0],
               "priceSpecification": {"@type": "PriceSpecification", "minPrice": m[3], "priceCurrency": "EUR", "valueAddedTaxIncluded": True}}
              for m in P["models"] if m[3] and SHOW_PRICES]
    schema = [breadcrumb(crumbs), faq_schema(P["faq"]),
              {"@context": "https://schema.org", "@type": "Service", "name": P["name"], "serviceType": P["name"],
               "provider": {"@id": BASE_URL + "/#yritys"}, "areaServed": {"@type": "Country", "name": "Suomi"},
               "description": P["desc"], "url": BASE_URL + url, "image": BASE_URL + src_of(hero_img, 1),
               **({"offers": offers} if offers else {})}]
    page(url, P["title"], P["desc"], body, schema=schema, preload=hero_img)


def build_hub():
    H = L["hub"]
    P = L["P"]
    url = L["paths"]["hub"]
    crumbs = [(L["ui"]["home"], L["home"]), (L["nav"][1][0], url)]
    rows = "".join(f'''<a class="srow rv" href="{ppath(k)}"><div class="srow-img">{img(PROD[k][3], P[k]["card"], "(max-width:700px) 100vw, 30vw")}</div>
  <div class="srow-b"><h2>{P[k]["name"]}</h2><p>{P[k]["lead"]}</p>{price_html(cat_price(k))}</div><span class="srow-go">{icon("arrow")}</span></a>''' for k in BUILDINGS)
    body = hero(H["h1"], H["lead"], H["img"][0], H["img"][1], "50% 60%",
                f'<div class="btns">{btn(L["ui"]["quote"], quote_url())}{btn_call()}</div>')
    body += f'<section class="sec"><div class="wrap"><div class="srows">{rows}</div></div></section>{contact_section()}'
    page(url, H["title"], H["desc"], body, schema=[breadcrumb(crumbs)], preload=H["img"][0])


def build_company():
    C = L["company"]
    url = L["paths"]["company"]
    crumbs = [(L["ui"]["home"], L["home"]), (L["ui"]["company"], url)]
    ps = "".join(f'<p{" class=big" if i == 0 else ""}>{t}</p>' for i, t in enumerate(C["p"]))
    mat = "".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in C["mat"])
    deliv = "".join(f'<li class="rv">{icon(ic, "ic why-ic")}<div><h3>{a}</h3><p>{b}</p></div></li>'
                    for (a, b), ic in zip(C["deliv"], ["log", "ruler", "truck"]))
    body = hero(C["h1"], C["lead"], C["img"][0], C["img"][1], "50% 50%",
                f'<div class="btns">{btn(L["ui"]["quote"], quote_url())}{btn_call()}</div>')
    body += f'''<section class="sec"><div class="wrap split">
  <div class="split-txt rv">{ps}</div>
  <div class="listbox rv"><h3>{C["mat_h"]}</h3><table class="mat">{mat}</table></div>
</div></section>
<section class="sec alt"><div class="wrap why-grid">
  <div class="why-txt"><h2>{C["deliv_h"]}</h2><ul class="why">{deliv}</ul></div>
  <figure class="split-img why-img rv">{img(C["deliv_img"][0], C["deliv_img"][1], "(max-width:900px) 100vw, 45vw")}</figure>
</div></section>
<section class="sec"><div class="wrap">{sec_head(L["products_h"])}{product_tiles([p[0] for p in PRODUCTS])}</div></section>
{contact_section()}'''
    page(url, C["title"], C["desc"], body, schema=[breadcrumb(crumbs)], preload=C["img"][0])


def quote_config():
    """Tarjousvelhon tuotetiedot JS:lle."""
    Q = L["quote"]
    P = L["P"]
    out = []
    for key, fi, sv, im, price, typ, (w, l) in PRODUCTS:
        models = [{"n": m[0], "p": m[3] if SHOW_PRICES else None} for m in P[key]["models"]]
        if key == "pihavarasto":
            models[0].update(w=2.1, l=4.2)
            models[1].update(w=2.0, l=3.0)
        if key == "leikkimokki":
            models[1].update(noplan=True, np=True)
        if typ == "count":
            ip = ITEM_PRICES[key]  # vain asiakkaan ilmoittamat hinnat
            models = [{"n": n, "p": pp if SHOW_PRICES else None} for n, pp in zip(Q["items"][key], ip)]
        out.append({"k": key, "n": P[key]["card"], "img": src_of(im, 0), "p": cat_price(key) if SHOW_PRICES else None, "t": typ,
                    "w": w, "l": l, "m": models, "x": Q["extras_by"][key]})
    return out


def build_quote():
    Q = L["quote"]
    url = L["paths"]["quote"]
    crumbs = [(L["ui"]["home"], L["home"]), (L["ui"]["quote"], url)]
    F = L["form"]
    cards = "".join(f'''<label class="pc"><input type="radio" name="tuote" value="{esc(L["P"][p[0]]["card"])}" data-k="{p[0]}"{" checked" if i == 0 else ""}>
  <span class="pc-in">{img(p[3], L["P"][p[0]]["card"], "160px")}<b>{L["P"][p[0]]["card"]}</b>{price_html(cat_price(p[0]))}</span></label>''' for i, p in enumerate(PRODUCTS))
    frames = "".join(f'<option{" selected" if i == 1 else ""}>{f}</option>' for i, f in enumerate(Q["frames"]))
    roofs = "".join(f"<option>{r}</option>" for r in Q["roofs"])
    deliv = "".join(f'<label class="ch"><input type="radio" name="toimitus" value="{esc(d)}"{" checked" if i == 0 else ""}><span>{d}</span></label>'
                    for i, d in enumerate(Q["deliveries"]))
    labels = {k: Q[k] for k in ("width", "length", "diam", "area", "inner", "terrace", "porch", "steam", "dress", "qty", "bins")}
    labels["from"] = L["ui"]["from"]
    labels["ask"] = L["ui"]["ask_price"]
    labels["delivery"] = Q["delivery"]
    cfg = json.dumps({"products": quote_config(), "L": labels}, ensure_ascii=False)
    body = plain_hero(Q["h1"], Q["lead"])
    body += f'''<section class="sec pt0"><div class="wrap qwrap">
<form class="qform" id="lomake" name="tarjous" method="POST" {form_attrs()} novalidate>
  {hidden_fields("tarjous")}<input type="hidden" name="lomake" value="tarjous"><input type="hidden" name="kieli" value="{L["lang"]}">
  <input type="hidden" name="koko"><input type="hidden" name="ala">
  <div class="qstep panel"><h2 class="qh"><span>1</span>{Q["s1"]}</h2><div class="pcs">{cards}</div></div>
  <div class="qstep panel"><h2 class="qh"><span>2</span>{Q["s2"]}</h2>
    <div class="q-models"><p class="lbl">{Q["model"]}</p><div class="chs" data-models></div></div>
    <div class="fgrid q-dims">
      <label class="f" data-dim="w"><span data-wl>{Q["width"]}</span><input name="leveys" type="number" inputmode="decimal" step="0.1" min="0.5" max="12"></label>
      <label class="f" data-dim="l">{Q["length"]}<input name="pituus" type="number" inputmode="decimal" step="0.1" min="0.5" max="15"></label>
      <label class="f" data-dim="n"><span data-nl>{Q["qty"]}</span><input name="maara" type="number" inputmode="numeric" min="1" max="20" value="1"></label>
      <label class="f" data-opt="frame">{Q["frame"]}<select name="runko">{frames}</select></label>
      <label class="f" data-opt="roof">{Q["roof"]}<select name="katto">{roofs}</select></label>
    </div>
    <p class="lbl">{Q["extras"]}</p><div class="chs" data-extras></div>
    <div class="qplan qplan-m" aria-hidden="true"></div><p class="qprice qprice-m"></p>
  </div>
  <div class="qstep panel"><h2 class="qh"><span>3</span>{Q["s3"]}</h2>
    <div class="chs">{deliv}</div>
    <div class="fgrid">
      <label class="f">{Q["town"]}<input name="paikkakunta" placeholder="{Q["town_ph"]}" autocomplete="address-level2"></label>
      <label class="f">{Q["when"]}<input name="aikataulu" placeholder="{Q["when_ph"]}"></label>
      <label class="f full">{Q["more"]}<textarea name="viesti" rows="3" placeholder="{Q["more_ph"]}"></textarea></label>
    </div>
  </div>
  <div class="qstep panel"><h2 class="qh"><span>4</span>{Q["s4"]}</h2>
    <p class="err" data-err>{F["err"]}</p><p class="err senderr">{F["senderr"]}</p>
    <div class="fgrid">
      <label class="f">{F["name"]}<input name="nimi" required autocomplete="name"></label>
      <label class="f">{F["phone"]}<input name="puhelin" type="tel" autocomplete="tel"></label>
      <label class="f full">{F["email"]}<input name="email" type="email" autocomplete="email"></label>
    </div>
    {consent("ts-q")}
    <button class="btn btn-primary" type="submit">{Q["send"]}{icon("arrow")}</button>
  </div>
</form>
<aside class="qside"><div class="panel qsum">
  <h3>{Q["summary"]}</h3>
  <div class="qplan" aria-live="polite"></div>
  <dl class="qdl"></dl>
  <p class="qprice"></p>
  <p class="muted small">{Q["price_note"] if SHOW_PRICES else ""} {Q["plan_note"]}</p>
  <a class="big-tel" href="{TEL}">{icon("phone")}{PHONE}</a>
</div></aside>
</div></section>
<script type="application/json" id="qcfg">{cfg}</script>'''
    page(url, Q["title"], Q["desc"], body, schema=[breadcrumb(crumbs)], cls="quote")


def build_contact():
    C = L["contact"]
    url = L["paths"]["contact"]
    crumbs = [(L["ui"]["home"], L["home"]), (L["ui"]["contact"], url)]
    maps = "https://www.google.com/maps/search/?api=1&query=" + f"{COMPANY['street']} {COMPANY['zip']} {COMPANY['city']}".replace(" ", "+")
    body = plain_hero(C["h1"], C["lead"])
    body += f'''<section class="sec pt0"><div class="wrap contact-grid">
  <div class="contact-info">
    <a class="big-tel" href="{TEL}">{icon("phone")}{PHONE}</a>
    <a class="mail" href="mailto:{COMPANY["email"]}">{icon("mail")}{COMPANY["email"]}</a>
    <p class="addr">{icon("pin")}<span>{COMPANY["name"]}<br>{COMPANY["street"]}, {COMPANY["zip"]} {COMPANY["city"]}<br><a class="link" href="{maps}" target="_blank" rel="noopener">{L["ui"]["open_map"]}</a></span></p>
    <p class="addr">{icon("clock")}<span><b>{C["hours"]}</b><br>{C["hours_v"]}<br>{L["ui"]["reach"]}</span></p>
    <p class="muted small">Y-tunnus {COMPANY["ytunnus"]}</p>
  </div>
  {contact_form(fid="ts-y")}
</div></section>'''
    page(url, C["title"], C["desc"], body, schema=[breadcrumb(crumbs)])


def build_simple():
    R = L["privacy"]
    secs = "".join(f"<h2>{i + 1}. {h}</h2><p>{t}</p>" for i, (h, t) in enumerate(R["sections"]))
    if TRACKING:
        secs += (f'<h2 id="evasteet">{R["cookie_h"]}</h2><p><a class="btn btn-line" href="javascript:Cookiebot.renew()">{L["ui"]["cookies"]}</a></p>'
                 f'<script id="CookieDeclaration" src="https://consent.cookiebot.com/{COOKIEBOT_ID}/cd.js" data-culture="{L["lang"].upper()}" type="text/javascript" async></script>')
    body = plain_hero(R["h1"], R["lead"]) + f'<section class="sec pt0"><div class="wrap narrow prose">{secs}</div></section>'
    page(L["paths"]["privacy"], R["title"], R["lead"], body)
    ok = plain_hero(R["thanks_h"], R["thanks_p"]).replace(
        "</div></section>", f'<div class="btns">{btn(L["ui"]["home"], L["home"])}{btn_call()}</div></div></section>')
    page(L["paths"]["thanks"], strip(R["thanks_h"]) + " | Jääkärihirsi", R["thanks_p"], ok, noindex=True)
    if L["lang"] == "fi":
        nf = plain_hero(R["nf_h"], R["nf_p"]).replace(
            "</div></section>", f'<div class="btns">{btn(L["ui"]["home"], "/")}{btn(L["ui"]["quote"], L["paths"]["quote"], "btn btn-line", "")}</div></div></section>')
        page("/404.html", "Sivua ei löytynyt | Jääkärihirsi", R["nf_p"], nf, noindex=True)


# ---------------------------------------------------------------------------
# OG-kuva, favicon, sitemap
# ---------------------------------------------------------------------------

def font(name, size, wght=None):
    path = os.path.join(SRC, "fonts", name)
    if not os.path.exists(path):
        path = os.path.join(SRC, "fonts", "Inter.ttf")
    f = ImageFont.truetype(path, size)
    if wght:
        try:
            f.set_variation_by_axes([wght])
        except Exception:
            pass
    return f


def icon_png(size):
    s = 4 * size
    im = Image.new("RGBA", (s, s), GREEN + (255,))
    d = ImageDraw.Draw(im)
    for i, y in enumerate((.27, .45, .63)):
        d.rounded_rectangle([s * .18, s * y, s * .82, s * (y + .13)], radius=s * .065, fill=(255, 255, 255, 255))
    return im.resize((size, size), Image.LANCZOS)


def og_image():
    W, H = 1200, 630
    bg = ImageOps.fit(Image.open(IMG_SRC["tuomas20-2"]).convert("RGB"), (W, H), Image.LANCZOS, centering=(.6, .5))
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    for x in range(W):
        a = int(max(0, 200 * (1 - x / 760)))
        d.line([(x, 0), (x, H)], fill=(10, 20, 14, a))
    bg = Image.alpha_composite(bg.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(bg)
    d.text((70, 70), "JÄÄKÄRIHIRSI", font=font("InterTight.ttf", 46, 800), fill=(255, 255, 255))
    d.rectangle([72, 128, 418, 150], fill=GREEN)
    d.text((245, 139), "KORTESJÄRVI", font=font("Inter.ttf", 14, 600), fill=(255, 255, 255), anchor="mm")
    for i, t in enumerate(["Pihasaunat ja", "piharakennukset", "hirrestä"]):
        d.text((70, 260 + i * 64), t, font=font("InterTight.ttf", 58, 700), fill=(255, 255, 255))
    d.text((70, 520), f"Mittatilauksena · {PHONE}", font=font("Inter.ttf", 26, 500), fill=(225, 235, 228))
    bg.save(os.path.join(IMG_OUT, "og.jpg"), quality=86)


def build_assets():
    og_image()
    icon_png(64).save(os.path.join(SITE, "favicon.png"))
    icon_png(180).save(os.path.join(SITE, "apple-touch-icon.png"))
    icon_png(512).save(os.path.join(IMG_OUT, "logo-512.png"))
    shutil.copy(os.path.join(SRC, "style.css"), os.path.join(SITE, "style.css"))
    shutil.copy(os.path.join(SRC, "app.js"), os.path.join(SITE, "app.js"))
    with open(os.path.join(SITE, "robots.txt"), "w") as f:
        f.write("User-agent: *\nDisallow: /\n" if DEMO else f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml\n")
    with open(os.path.join(SITE, "sitemap.xml"), "w") as f:
        urls = []
        for p in SITEMAP:
            key = PATH_KEY.get(p)
            alt = ""
            if key:
                alt = "".join(f'<xhtml:link rel="alternate" hreflang="{lg}" href="{BASE_URL}{PAIRS[key][i]}"/>' for i, lg in enumerate(("fi", "sv")))
            urls.append(f"<url><loc>{BASE_URL}{p}</loc><lastmod>{TODAY}</lastmod>{alt}</url>")
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                f'xmlns:xhtml="http://www.w3.org/1999/xhtml">{"".join(urls)}</urlset>\n')


def build_lang(lang):
    global L
    L = T[lang]
    build_home()
    for key in PROD:
        build_product(key)
    build_hub()
    build_company()
    build_quote()
    build_contact()
    build_simple()


def build():
    global VERSION
    VERSION = str(int(max(os.path.getmtime(os.path.join(SRC, f)) for f in ("style.css", "app.js"))))
    for f in os.listdir(SITE) if os.path.isdir(SITE) else []:
        if f != "img":
            p = os.path.join(SITE, f)
            shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    os.makedirs(SITE, exist_ok=True)
    build_images()
    for lang in ("fi", "sv"):
        build_lang(lang)
    build_assets()
    with open(os.path.join(SITE, "redirects.json"), "w") as f:
        json.dump(REDIRECTS, f, ensure_ascii=False, indent=1)
    target = write_host_files(SITE, vastaanottaja=COMPANY["email"], domain=COMPANY["domain"], sivusto=COMPANY["name"],
                              redirects=REDIRECTS, www_to_apex=False)
    print(f"Rakennettu {len(SITEMAP)} indeksoitavaa sivua → site/ ({target})")
    if "--preview" not in sys.argv:
        name = os.path.join(ROOT, "..", f"jaakarihirsi-{target}.zip")
        with zipfile.ZipFile(name, "w", zipfile.ZIP_DEFLATED) as z:
            for base, _, files in os.walk(SITE):
                for fn in files:
                    if fn.startswith("."):
                        continue
                    full = os.path.join(base, fn)
                    z.write(full, os.path.relpath(full, SITE))
        print("Zip:", os.path.abspath(name))


def build_artifact():
    """Esikatselu Claude-artifaktina: litteät sivut, suhteelliset polut, lomakkeet eivät lähetä mitään."""
    pv = os.path.join(ROOT, "preview")
    if os.path.exists(pv):
        shutil.rmtree(pv)
    os.makedirs(os.path.join(pv, "img"))
    for f in ("style.css", "app.js", "favicon.png", "apple-touch-icon.png"):
        shutil.copy(os.path.join(SITE, f), os.path.join(pv, f))

    def flat(path):
        path = path.strip("/")
        return "index.html" if path == "" else path if path.endswith(".html") else path.replace("/", "-") + ".html"

    def fix(m):
        attr, path, frag = m.group(1), m.group(2), m.group(3) or ""
        if path.startswith(("img/", "style.css", "app.js", "favicon", "apple-touch")):
            return f'{attr}="{path}{frag}"'
        qs = ""
        if "?" in path:
            path, qs = path.split("?", 1)
            qs = "?" + qs
        return f'{attr}="{flat(path)}{qs}{frag}"'

    pages = []
    for dp, _, fs in os.walk(SITE):
        for f in fs:
            if f.endswith(".html"):
                pages.append(os.path.relpath(os.path.join(dp, f), SITE))
    for rel in pages:
        h = open(os.path.join(SITE, rel), encoding="utf-8").read()
        h = re.sub(r'(href|src|srcset|action|imagesrcset|poster)="/([^"#]*)(#[^"]*)?"', fix, h)
        h = re.sub(r'(\s|,|")/img/', r'\1img/', h)
        h = re.sub(r'<form ([^>]*?)method="POST"[^>]*>', lambda m: f'<form {m.group(1)}data-preview="1" novalidate>', h)
        h = re.sub(r'<!doctype html>\s*<html[^>]*>\s*<head>\s*', "", h)
        h = h.replace("</head>", "").replace("</body>", "").replace("</html>", "")
        h = re.sub(r'<body([^>]*)>', lambda m: f'<div id="__b"{m.group(1)}></div><script>document.body.className=document.getElementById("__b").className</script>', h)
        if rel == "index.html":
            h = re.sub(r"<title>[^<]*</title>", "<title>Jääkärihirsi</title>", h, count=1)
        h = re.sub(r'<img([^>]*?)src="img/([\w.-]+)-(\d+)\.webp"([^>]*?)fetchpriority="high"',
                   lambda m: f'<img{m.group(1)}src="img/{m.group(2)}-{IMG_WS[m.group(2)][min(2, len(IMG_WS[m.group(2)]) - 1)]}.webp"{m.group(4)}fetchpriority="high"', h)
        h = re.sub(r'\s(srcset|imagesrcset|sizes|imagesizes)="[^"]*"', "", h)
        h = re.sub(r'<link rel="preload" as="image"[^>]*>', "", h)
        name = "index.html" if rel == "index.html" else ("404.html" if rel == "404.html" else flat(rel[:-len("index.html")]))
        if name != "index.html":
            h = "<!doctype html>\n" + h
        open(os.path.join(pv, name), "w", encoding="utf-8").write(h)
    used = set()
    for f in os.listdir(pv):
        if f.endswith((".html", ".css", ".js")):
            used |= set(re.findall(r'img/([\w.-]+\.(?:webp|png|jpg|svg))', open(os.path.join(pv, f), encoding="utf-8").read()))
    for u in used:
        if os.path.exists(os.path.join(SITE, "img", u)):
            shutil.copy(os.path.join(SITE, "img", u), os.path.join(pv, "img", u))
    n = sum(len(fs) for _, _, fs in os.walk(pv))
    print(f"ARTIFACT: {len(pages)} sivua, {len(used)} kuvaa, {n} tiedostoa -> {pv}")


if __name__ == "__main__":
    build()
    if "--artifact" in sys.argv:
        build_artifact()
