# -*- coding: utf-8 -*-
"""Jääkärihirsi Oy (jaakarihirsi.com): sivuston sisällöt suomeksi ja ruotsiksi.

Lähde: vanha Duda-sivu (fi + sv) + asiakkaan ohjeistus 9.10.2026 (hirsikoot, toimitustavat, alkaen-hinnat,
poistetut tuotteet: kärrysauna Tuomas 10, huvimajat, keinut). SHOW_PRICES = False piilottaa kaikki hinnat.
Hinnat ovat asiakkaan ilmoittamia tuoteryhmän alkaen-hintoja ("from"); mallikohtaisia hintoja ei ole.
Kuvat: src/kuvat/, kaikki asiakkaan omia (Drive 9.10.2026 + vanha sivu).
"""

SHOW_PRICES = True

COMPANY = {
    "name": "Jääkärihirsi Oy", "short": "Jääkärihirsi", "domain": "jaakarihirsi.com",
    "phone": "045 119 7289", "intl": "+358451197289", "email": "info@jaakarihirsi.com",
    "street": "Puusepäntie 32", "zip": "62420", "city": "Kortesjärvi", "town": "Kauhava", "region": "Etelä-Pohjanmaa",
    "ytunnus": "2386106-5", "geo": (63.3127, 23.1695),
}

# Tuotteet: avain, sivun polku fi/sv, kuva, (ei käytössä), tyyppi, oletusmitat (leveys, pituus)
# type: building = mitat + pohjakuva, sauna = building + saunavalinnat, count = kappalemäärä, bins = astioiden määrä
PRODUCTS = [
    ("pihasauna", "/pihasaunat/", "/sv/gardsbastur/", "tuomas20-1", None, "sauna", (3.0, 4.0)),
    ("pihavarasto", "/piharakennukset/pihavarastot/", "/sv/gardsbyggnader/forrad/", "varasto-1", None, "building", (2.1, 4.2)),
    ("leikkimokki", "/piharakennukset/leikkimokit/", "/sv/gardsbyggnader/lekstugor/", "leikkimokki-a", None, "building", (1.8, 2.5)),
    ("wc", "/piharakennukset/ulko-wc/", "/sv/gardsbyggnader/utedass/", "wc-a", None, "building", (1.2, 1.5)),
    ("roskakatos", "/piharakennukset/roskakatokset/", "/sv/gardsbyggnader/sopskjul/", "roskakatos-a", None, "bins", (1.0, 2.0)),
    ("kalusteet", "/hirsikalusteet/", "/sv/timmermoebler/", "poyta-a", None, "count", (0, 0)),
    ("koristeet", "/pihakoristeet/", "/sv/gardsdekorationer/", "maitolaituri-a", None, "count", (0, 0)),
]
PROD = {p[0]: p for p in PRODUCTS}
BUILDINGS = ["pihavarasto", "leikkimokki", "wc", "roskakatos"]

# Vanhan sivun osoitteet → uudet (server.js / _redirects). Säilyneet: /pihasaunat, /piharakennukset, /hirsikalusteet, /pihakoristeet, /yhteystiedot, /sv/...
REDIRECTS = {
    "/evasteet/": "/tietosuoja/#evasteet",
    "/sv/kontakt-1/": "/sv/kontakt/",
}

# Hintojen järjestys tarjousvelhon pientuotteille (asiakkaan ilmoittamat)
ITEM_PRICES = {"kalusteet": [400, None], "koristeet": [500, 450, 120]}

T = {}  # kielikohtaiset tekstit

# =====================================================================================================
# SUOMI
# =====================================================================================================
T["fi"] = {
    "lang": "fi", "locale": "fi_FI", "home": "/", "other": "sv", "other_label": "Svenska", "other_short": "SV",
    "nav": [("Pihasaunat", "/pihasaunat/"), ("Piharakennukset", "/piharakennukset/"), ("Kalusteet", "/hirsikalusteet/"),
            ("Pihakoristeet", "/pihakoristeet/"), ("Yritys", "/yritys/"), ("Yhteystiedot", "/yhteystiedot/")],
    "paths": {"quote": "/tarjouspyynto/", "contact": "/yhteystiedot/", "company": "/yritys/", "privacy": "/tietosuoja/",
              "thanks": "/kiitos/", "hub": "/piharakennukset/"},
    "ui": {
        "quote": "Pyydä tarjous", "call": "Soita", "menu": "Valikko", "skip": "Siirry sisältöön", "from": "alkaen",
        "ask_price": "Hinta tarjouksella", "vat": "Hinnat sis. alv 25,5 %.", "more": "Lue lisää", "products": "Tuotteet",
        "other_products": "Muut tuotteet", "faq": "Usein kysyttyä", "ask_this": "Pyydä tarjous tästä", "gallery": "Kuvia toteutuksista",
        "home": "Etusivu", "close": "Sulje", "prev": "Edellinen", "next": "Seuraava", "company": "Yritys", "contact": "Yhteystiedot",
        "privacy": "Tietosuoja", "cookies": "Evästeasetukset", "weekdays": "Arkisin 7–18", "reach": "Meidät tavoittaa aina puhelimitse.",
        "demo": "Sivustoehdotus: Äijä Group. Tämä on esikatseluversio.", "open_map": "Avaa kartalla", "mobile_quote": "Tarjous",
        "made_in": "Tehty Kortesjärvellä kotimaisesta hirrestä.",
    },
    "home_title": "Pihasaunat ja piharakennukset hirrestä, Kortesjärvi | Jääkärihirsi",
    "home_desc": "Jääkärihirsi Oy valmistaa pihasaunat, pihavarastot, leikkimökit, ulko-WC:t, roskakatokset ja hirsikalusteet mittatilauksena kotimaisesta höylähirrestä Kortesjärvellä. Avaimet käteen tai runkotoimituksena.",
    "hero_h1": "Pihasaunat ja piharakennukset <em>hirrestä</em>",
    "hero_lead": "Valmistamme Kortesjärvellä kotimaisesta höylähirrestä saunat, varastot ja leikkimökit mittojesi mukaan. Saat rakennuksen valmiiksi koottuna tai runkona.",
    "hero_cta": "Suunnittele ja pyydä tarjous",
    "products_h": "Mitä <em>tarvitset?</em>",
    "products_p": "Kaikki tuotteet tehdään mittatilauksena. Hinnat sisältävät arvonlisäveron.",
    "why_h": "Hirsirakentaja <em>Kortesjärveltä</em>",
    "why": [
        ("Kotimainen höylähirsi", "Rungot 45 × 145 tai 70 × 145 mm höylähirrestä tai 20 × 95 ja 20 × 120 mm ulkovuoripaneelista. Raaka-aineet ovat kotimaisia."),
        ("Mittasi mukaan", "Vakiomallit ovat lähtökohta, ja koko, ikkunat, terassi ja katemateriaali sovitaan toiveidesi mukaan."),
        ("Valmiina tai runkona", "Toimitamme rakennuksen valmiiksi koottuna avaimet käteen tai runkona osina. Toimitamme koko Suomeen."),
    ],
    "why_img": ("sauna-sisa-1", "Pihasaunan kuusilauteet"),
    "steps_h": "Näin tilaus <em>etenee</em>",
    "steps": [
        ("Kerro toiveet", "Valitse tuote ja mitat tarjouspyynnössä tai soita. Kuvat ja luonnokset auttavat."),
        ("Tarjous ja sopimus", "Saat tarjouksen, jossa runko, varustelu ja toimitustapa on eritelty."),
        ("Valmistus Kortesjärvellä", "Rakennus tehdään omassa hallissamme Kortesjärvellä."),
        ("Toimitus valmiina tai osina", "Toimitamme rakennuksen valmiiksi koottuna avaimet käteen tai runkona osina itse koottavaksi."),
    ],
    "steps_img": ("varasto-7", "Pihavarasto valmistumassa Jääkärihirren hallissa"),
    "contact_h": "Kysy <em>tarjous</em>",
    "contact_p": "Soita tai jätä viesti, niin vastaamme mahdollisimman nopeasti. Kerro tuote, likimääräiset mitat ja toimituspaikkakunta.",
    "form": {
        "send": "Lähetä viesti", "name": "Nimi *", "phone": "Puhelin", "email": "Sähköposti", "town": "Paikkakunta",
        "msg": "Viesti", "product": "Tuote", "choose": "Valitse tuote", "other": "Muu / en tiedä vielä",
        "consent": 'Hyväksyn tietojeni käsittelyn <a class="link" href="/tietosuoja/">tietosuojaselosteen</a> mukaisesti.',
        "err": "Täytä nimi ja joko puhelin tai sähköposti.", "senderr": "Lähetys epäonnistui. Soita 045 119 7289 tai yritä uudelleen.",
        "title": "Lähetä viesti",
    },
}

DELIV_FAQ_FI = ("Mitä eroa on avaimet käteen -toimituksella ja runkotoimituksella?",
                "Avaimet käteen -toimituksessa rakennus toimitetaan valmiiksi koottuna. Runkotoimituksessa saat rakennuksen osina itse koottavaksi tai oman rakentajasi koottavaksi. Toimitustapa sovitaan tarjouksessa.")

# Tuotesivut (fi). models: nimi, teksti, varustelu, hinta (None = ei mallihintaa), kuvat. "from" = tuoteryhmän alkaen-hinta.
P_FI = {
    "pihasauna": {
        "name": "Pihasaunat", "card": "Pihasauna", "short": "Hirsisaunat koti- ja mökkipihaan mittatilauksena.", "from": 7500, "hero_pos": "50% 32%",
        "title": "Pihasauna hirrestä mittatilauksena, avaimet käteen | Jääkärihirsi, Kortesjärvi",
        "desc": "Pihasaunat kotimaisesta höylähirrestä (45 × 145 tai 70 × 145 mm) mittojesi mukaan. Puukiuas, kuusilauteet, pukuhuone ja terassi. Avaimet käteen tai runkotoimituksena, alkaen 7 500 €.",
        "h1": "Pihasaunat <em>hirrestä</em>",
        "lead": "Hirsisauna koti- tai mökkipihaan mittojesi mukaan. Saat saunan valmiiksi koottuna avaimet käteen tai runkona osina.",
        "intro_h": "Sauna, joka kestää <em>sukupolvelta toiselle</em>", "intro_img": "sauna-sisa-2",
        "intro": [
            "Hirsirakenteiset pihasaunat ovat suosituimpia tuotteitamme. Valmistamme saunat Kortesjärvellä asiakkaan mittojen mukaan höylähirrestä, jonka vahvuus on 70 × 145 mm tai 45 × 145 mm.",
            "Höylähirsi on kestävä materiaali ja sopii ulkonäöltään suomalaiseen pihapiiriin. Saunassa on kuusilauteet ja puukiuas vesisäiliöllä tai hormisäiliöllä. Rakennukseen mahtuu pukuhuone ja halutessasi terassi.",
        ],
        "list_h": "Vakiovarustelu",
        "list": ["Hirsirunko 45 × 145 tai 70 × 145 mm", "Lankkulattia, saunassa viemäröinti", "Kuusilauteet ja kuusipanelointi katossa",
                 "Villat + tinapaperi yläpohjassa", "Avattavat ikkunat, saunassa lasiovi", "Puukiuas vesi- tai hormisäiliöllä + piippu",
                 "Palosuojalevyt kiukaan takana ja alla", "Palahuopakate"],
        "models_h": "Saunamallit",
        "models": [
            ("Pihasauna Tuomas 15", "Katettu kuisti ja tilava pukuhuone. Saatavana avaimet käteen tai runkotoimituksena.",
             ["Hirsirunko 45 × 145 tai 70 × 145 mm", "Katettu kuisti", "Kiuas vesisäiliöllä tai hormisäiliöllä"], None,
             ["tuomas15-1", "tuomas15-2", "tuomas15-3", "tuomas15-4"]),
            ("Pihasauna Tuomas 20", "Suurempi malli: terassi kaiteineen ja tilaa usealle saunojalle.",
             ["Hirsirunko 45 × 145 tai 70 × 145 mm", "Terassi kaiteineen", "Kiuas vesisäiliöllä tai hormisäiliöllä"], None,
             ["tuomas20-1", "tuomas20-2", "tuomas20-3", "tuomas20-4", "tuomas20-5"]),
        ],
        "gallery_h": "Toteutettuja saunoja",
        "gallery": [("sauna-1", "Pihasauna kuistilla"), ("sauna-2", "Pihasauna pariovella"), ("sauna-3", "Pihasauna pulpettikatolla"),
                    ("sauna-4", "Pihasauna pulpettikatolla"), ("sauna-5", "Pihasauna talvella"), ("sauna-6", "Pihasauna lasiovella"),
                    ("sauna-7", "Pihasauna"), ("sauna-runko", "Saunan hirsirunko terasseineen"),
                    ("sauna-sisa-1", "Kuusilauteet"), ("sauna-sisa-3", "Puukiuas ja lauteet"), ("sauna-sisa-4", "Saunan lauteet"),
                    ("sauna-sisa-5", "Puukiuas hormisäiliöllä"), ("sauna-sisa-6", "Saunan lasiovi"), ("sauna-sisa-7", "Saunan sisätila"),
                    ("sauna-sisa-8", "Puukiuas ja lauteet")],
        "band": ("tuomas15-3", "Löylyt ympäri vuoden", "Kesällä terassilla vilvoitellen, talvella hankeen hyppien."),
        "faq": [
            DELIV_FAQ_FI,
            ("Minkä vahvuisesta hirrestä sauna tehdään?", "Höylähirrestä, jonka vahvuus on 70 × 145 mm tai 45 × 145 mm. Paksumpi hirsi sopii erityisesti ympärivuotiseen käyttöön, joten kerro käyttötarkoitus, niin suosittelemme sopivan."),
            ("Voiko saunan koon ja pohjan päättää itse?", "Kyllä. Teemme saunat aina mittatilaustyönä, joten koko, ikkunat, terassi ja pukuhuoneen koko sovitaan toiveidesi mukaan."),
            ("Mihin saunoja toimitetaan?", "Toimitamme pihasaunat koko Suomeen Kauhavan seudulta, joko valmiiksi koottuna tai runkona osina."),
            ("Tarvitaanko pihasaunalle rakennuslupa?", "Lupakäytäntö riippuu kunnasta ja rakennuksen koosta. Tarkista oman kuntasi rakennusvalvonnasta ennen tilausta. Tarvittaessa saat meiltä rakennuksen mitat ja kuvat lupaa varten."),
        ],
    },
    "pihavarasto": {
        "name": "Pihavarastot ja puuladot", "card": "Pihavarasto", "short": "Varastot ja puuladot hirrestä tai paneelista.", "from": 2000,
        "title": "Pihavarasto ja puulato hirrestä mittojen mukaan | Jääkärihirsi",
        "desc": "Pihavarastot 45 × 145 höylähirrestä tai 20 × 95 ulkovuoripaneelista ja puuladot kevythirrestä asiakkaan mitoilla. Pihavarasto alkaen 2 700 €, puulato alkaen 2 000 €.",
        "h1": "Pihavarastot ja <em>puuladot</em>",
        "lead": "Hirsi- ja puurakenteiset varastot ja puuladot mittatilauksena. Saat ne valmiiksi koottuina, jotta pääset käyttämään niitä heti.",
        "intro_h": "Tilaa tavaroille ja <em>polttopuille</em>",
        "intro": [
            "Valmistamme pihavarastot 45 × 145 höylähirrestä tai 20 × 95 ulkovuoripaneelista asiakkaan mitoilla. Puuladot tehdään hienosahatusta kevythirrestä joko rakoseinällä polttopuiden kuivumista varten tai umpiseinällä.",
            "Toimitamme rakennuksen valmiiksi koottuna tai runkona osina.",
        ],
        "list_h": "Valinnat",
        "list": ["Runko 45 × 145 mm hirsi tai 20 × 95 mm ulkovuoripaneeli", "Puuladossa 50 × 125 mm seinä 15 mm raolla tai umpinainen",
                 "Lautalattia", "Palahuopa- tai peltikate", "Mitat asiakkaan mukaan"],
        "models_h": "Mallit",
        "models": [
            ("Pihavarasto", "Pihavarasto asiakkaan mitoilla hirrestä tai ulkovuoripaneelista, ovellisena tai pariovin.",
             ["Runko 45 × 145 hirsi tai 20 × 95 paneeli", "Lautalattia", "Palahuopakate"], 2700,
             ["varasto-1", "varasto-2", "varasto-3", "varasto-4", "varasto-5", "varasto-6", "varasto-7", "varasto-8", "varasto-9",
              "varasto-10", "varasto-11", "varasto-12", "varasto-13", "varasto-14"]),
            ("Puulato", "Puulato polttopuille. Vakiokoko 2 × 3 m, myös asiakkaan mitoilla.",
             ["Runko 50 × 125 mm lankku", "Lattia 22 × 100 mm lauta", "Musta peltikate"], 2000,
             ["puulato-a", "puulato-b", "puulato-1", "puulato-2"]),
        ],
        "faq": [
            DELIV_FAQ_FI,
            ("Tarvitaanko pihavarastolle lupa?", "Pienet talousrakennukset ovat monessa kunnassa luvanvaraisia vasta tietyn koon ylittäessä, mutta rajat vaihtelevat. Tarkista oman kuntasi rakennusvalvonnasta."),
            ("Voiko puuladon tehdä umpiseinällä?", "Kyllä. Seinä tehdään joko 15 mm raolla, jolloin polttopuut tuulettuvat, tai umpinaisena."),
        ],
    },
    "leikkimokki": {
        "name": "Leikkimökit ja hiekkalaatikot", "card": "Leikkimökki", "short": "Leikkimökit ja hiekkalaatikot lapsille.", "from": 1500,
        "title": "Leikkimökki hirrestä tai paneelista mittojen mukaan | Jääkärihirsi",
        "desc": "Leikkimökit 45 × 145 hirrestä tai paneelielementeistä, vakiomitta 2 500 × 1 800 mm tai omilla mitoilla. Myös hiekkalaatikot kotimaisesta kestopuusta. Leikkimökit alkaen 1 500 €.",
        "h1": "Leikkimökit ja <em>hiekkalaatikot</em>",
        "lead": "Hirsi- tai paneelirunkoiset leikkimökit vakiomitoilla tai omien mittojesi mukaan sekä hiekkalaatikot perheen pienimmille.",
        "intro_h": "Oma mökki <em>lapsille</em>",
        "intro": [
            "Valmistamme leikkimökit hirrestä ja paneelista asiakkaan mittojen mukaan. Myös vakiomitta löytyy, esimerkiksi 2 500 × 1 800 mm.",
            "Mökin saa puunvärisenä tai maalattuna. Kuvissa on myös perinteinen punamulta valkoisin listoin ja kuistikaitein.",
        ],
        "list_h": "Leikkimökki sisältää",
        "list": ["Hirsirunko 45 × 145 mm tai paneelielementtirunko", "Ikkunat muovilevyä", "Lautalattia + muovimatto", "Palahuopakate"],
        "models_h": "Mallit",
        "models": [
            ("Leikkimökki", "Hirsi- tai paneelirunkoinen leikkimökki, esimerkiksi 2 500 × 1 800 mm. Kuistilla tai ilman, myös mansardikatolla.",
             ["Hirsi 45 × 145 mm tai paneeli", "Muovilevyikkunat", "Lautalattia + muovimatto"], 1500,
             ["leikkimokki-a", "leikkimokki-b", "leikkimokki-c", "leikkimokki-d", "leikkimokki-e", "leikkimokki-f", "leikkimokki-g",
              "leikkimokki-h", "leikkimokki-i", "leikkimokki-j", "leikkimokki-k"]),
            ("Hiekkalaatikko", "Kulmikas tai neliön mallinen hiekkalaatikko kotimaisesta kestopuusta, myös asiakkaan mitoilla.",
             ["Kuusi- tai nelikulmainen", "Kotimainen kestopuu", "Mitat toiveen mukaan"], None,
             ["hiekkalaatikko"]),
        ],
        "faq": [
            ("Miksi ikkunat ovat muovilevyä?", "Muovilevy on lasia turvallisempi lasten leikeissä eikä särky."),
            ("Voiko leikkimökin maalata valmiiksi?", "Kyllä, väri sovitaan tilatessa. Mökin saa myös puunvärisenä."),
        ],
    },
    "wc": {
        "name": "Ulko-WC:t", "card": "Ulko-WC", "short": "Ulkovessat hirrestä tai paneelista.", "from": 1200,
        "title": "Ulko-WC ja ulkohuussi hirrestä, kompostoiva käymälä | Jääkärihirsi",
        "desc": "Ulkovessat 45 × 145 hirrestä tai 20 × 120 ulkovuoripaneelista. Euromakki HD -käymäläelementti tai muiden valmistajien laitteisiin sopiva rakennus. Alkaen 1 200 €.",
        "h1": "Ulko-WC:t <em>mökille</em> ja pihaan",
        "lead": "Ulkovessat hirrestä tai ulkovuoripaneelista, valmiina käymäläelementin kanssa tai valitsemaasi laitteeseen sopivina.",
        "intro_h": "Siisti ja toimiva <em>ulkohuussi</em>",
        "intro": [
            "Valmistamme ulkovessat 45 × 145 hirrestä tai 20 × 120 ulkovuoripaneelista. Käytämme Euromakki HD -muovisekoitteesta valmistettua käymäläelementtiä.",
            "Teemme myös muiden valmistajien elementteihin soveltuvia WC-rakennuksia hirrestä tai ulkovuoripaneelista sopimuksen mukaisesti.",
        ],
        "list_h": "Valinnat",
        "list": ["Runko 45 × 145 hirsi tai 20 × 120 paneeli", "Euromakki HD -käymäläelementti", "Sopii myös muiden ekokäymälävalmistajien laitteisiin", "Palahuopakate"],
        "models_h": "Toteutuksia",
        "models": [
            ("Ulko-WC", "Ulkovessa käymäläelementillä, puunvärisenä tai maalattuna. Portaat ja huoltoluukku tarpeen mukaan.",
             ["45 × 145 hirsi tai 20 × 120 paneeli", "Euromakki HD -elementti", "Maalattuna tai puunvärisenä"], 1200,
             ["wc-a", "wc-b", "wc-c", "wc-d"]),
        ],
        "faq": [
            ("Mihin käymälälaitteisiin rakennus sopii?", "Vakiona käytämme Euromakki HD -elementtiä. Teemme rakennuksen myös muiden valmistajien laitteisiin sopivaksi, joten kerro valitsemasi laite."),
            ("Voiko ulko-WC:n saada paneelista?", "Kyllä, 20 × 120 ulkovuoripaneelista tai 45 × 145 hirrestä."),
        ],
    },
    "roskakatos": {
        "name": "Roskakatokset", "card": "Roskakatos", "short": "Katokset yhdelle tai useammalle astialle.", "from": 550,
        "title": "Roskakatos puusta yhdelle tai useammalle jäteastialle | Jääkärihirsi",
        "desc": "Roskalaatikkokatokset yhdelle tai useammalle jäteastialle, ovellisena tai ilman. Toimitetaan myös maalattuna. Alkaen 550 €.",
        "h1": "<em>Roskakatokset</em> kotipihaan",
        "lead": "Siisti katos yhdelle tai useammalle jäteastialle, ovellisena tai ilman, puunvärisenä tai maalattuna.",
        "intro_h": "Tuo pihapiiriin <em>ryhtiä</em>",
        "intro": [
            "Roskalaatikkokatos on paitsi kätevä myös siisti ja tuo pihapiiriin ryhtiä. Valmistamme katokset niin yhdelle kuin useammallekin laatikolle, ovellisena tai ilman ovea.",
            "Toimitamme katoksia myös maalattuna, esimerkiksi talon värityksen mukaan.",
        ],
        "list_h": "Valinnat",
        "list": ["Yhdelle tai useammalle astialle", "Ovellinen tai avoin", "Puunvärinen tai maalattu", "Koristeelliset räystäslaudat ja säleiköt"],
        "models_h": "Toteutuksia",
        "models": [
            ("Roskakatos", "Katos jäteastioille säleiköin ja koristeräystäin. Mitoitetaan astioiden määrän mukaan.",
             ["Yhdelle tai useammalle astialle", "Ovellinen tai avoin", "Maalattuna"], 550,
             ["roskakatos-a", "roskakatos-b", "roskakatos-c", "roskakatos-d", "roskakatos-e", "roskakatos-f", "roskakatos-g", "roskakatos-h"]),
        ],
        "faq": [
            ("Mihin kokoisille astioille katos sopii?", "Katos mitoitetaan astioidesi mukaan. Kerro tarjouspyynnössä astioiden määrä ja koko (esim. 240 l tai 660 l)."),
        ],
    },
    "kalusteet": {
        "name": "Hirsikalusteet", "card": "Hirsipöytäsarja", "short": "Hirsiset pöytäsarjat pihalle ja terassille.", "from": 400,
        "title": "Hirsikalusteet ja hirsipöytäsarjat pihalle | Jääkärihirsi",
        "desc": "Hirsipöytäsarjat ja puutarhakalusteet 70 × 145 höylähirrestä Kortesjärveltä. Värillisinä tai ilman, mittatilauksena. Alkaen 400 €.",
        "h1": "Hirsikalusteet <em>pihalle</em>",
        "lead": "Aikaa ja säätä kestävät hirsipöytäsarjat kotimaisesta hirrestä, valmiiksi koottuina.",
        "intro_h": "Kalusteet, jotka <em>kestävät</em>",
        "intro": [
            "Valmistamme aikaa ja säätä kestävät hirsikalusteet Kortesjärvellä. Kaikki kalusteet valmistetaan kotimaisesta 70 × 145 höylähirrestä.",
            "Hirsikalusteet sopivat pihapiiriin ja erilaisille terasseille. Saat ne värillisinä tai ilman väriä, oman makusi mukaan räätälöityinä.",
        ],
        "list_h": "Hyvä tietää",
        "list": ["Kalusteet 70 × 145 höylähirrestä", "Petsattuina tai puunvärisinä", "Valmiiksi koottuina", "Mitat toiveen mukaan", "Toimitus koko Suomeen"],
        "models_h": "Tuotteet",
        "models": [
            ("Hirsipöytäsarja", "Pöytä ja kaksi penkkiä pihapiiriin ja terassille. Hyvin hoidettuina ne kestävät aikaa ja säätä vuosikausia.",
             ["70 × 145 höylähirsi", "Petsattuna tai ilman", "Mittatilauksena"], 400,
             ["poyta-b", "poyta-a", "poyta-c", "poyta-d", "poyta-e"]),
        ],
        "faq": [
            ("Miten hirsikalusteita hoidetaan?", "Kun hoidat hirsikalusteitasi hyvin, kestävät ne aikaa sekä säätä vuosikausia. Puunsuoja-aineen uusiminen muutaman vuoden välein pitää pinnan kunnossa."),
            ("Toimitatteko kalusteita kauemmas?", "Kyllä, pientavarat toimitamme kuljetuksineen koko Suomeen."),
        ],
    },
    "koristeet": {
        "name": "Pihakoristeet", "card": "Pihakoristeet", "short": "Maitolaiturit, koristekaivot ja postilaatikkotelineet.", "from": 120,
        "title": "Maitolaituri, koristekaivo ja postilaatikkoteline puusta | Jääkärihirsi",
        "desc": "Pihakoristeet mittatilaustyönä Kortesjärveltä: maitolaiturit alkaen 500 €, koristekaivot 80–100 cm kaivonrenkaalle alkaen 450 € ja postilaatikkotelineet alkaen 120 €.",
        "h1": "Maitolaiturit ja <em>pihakoristeet</em>",
        "lead": "Maitolaiturit, koristekaivot ja postilaatikkotelineet mittatilaustyönä kotimaisesta puusta, valmiiksi koottuina ja maalattuina.",
        "intro_h": "Pala suomalaista <em>pihaperinnettä</em>",
        "intro": [
            "Haaveiletko tunnelmallisesta maitolaiturista tai koristekaivosta? Kaipaako naapurustosi siistiä postilaatikkotelinettä? Valmistamme pihakoristeet toiveittesi mukaan pääasiassa kotimaisista raaka-aineista.",
            "Saat ne valmiiksi koottuina ja maalattuina.",
        ],
        "list_h": "Hyvä tietää",
        "list": ["Valmiiksi koottuina ja maalattuina", "Värin voi valita", "Kotimaisesta puusta", "Pientavarat kuljetuksineen koko Suomeen"],
        "models_h": "Tuotteet",
        "models": [
            ("Maitolaituri", "Vanhan ajan maitolaiturit ovat pala suomalaista identiteettiä. Valmistamme ne käsityönä paneelista aidon näköisinä.",
             ["Paneelista käsityönä", "Palahuopakate", "Mitat toiveen mukaan"], 500,
             ["maitolaituri-a", "maitolaituri-b", "maitolaituri-c", "maitolaituri-d", "maitolaituri-e", "maitolaituri-f"]),
            ("Koristekaivo", "Koristekaivolla piristät pihan yleisilmettä. Kaivot valmistetaan sopiviksi 80–100 cm kaivonrenkaan päälle, valmiiksi koottuina ja maalattuina.",
             ["80–100 cm renkaalle", "Valmiiksi koottu", "Maalattu tai puunvärinen"], 450,
             ["kaivo-1", "kaivo-2", "kaivo-3", "kaivo-4", "kaivo-5", "kaivo-6", "kaivo-7", "kaivo-8", "kaivo-9", "kaivo-10"]),
            ("Postilaatikkoteline", "Postilaatikkoteline elävöittää talon julkisivua. Telineet saat valmiiksi maalattuna haluamallasi värillä.",
             ["Valmiiksi koottu", "Maalattu valitsemallasi värillä"], 120,
             ["postilaatikkoteline-a", "postilaatikkoteline"]),
        ],
        "faq": [
            ("Minkä kokoiselle kaivonrenkaalle koristekaivo sopii?", "Kaivot valmistetaan sopiviksi 80–100 cm kaivonrenkaan päälle."),
            ("Voiko värin valita?", "Kyllä. Kuvissa on punamultaisia ja puunvärisiä malleja, ja väri sovitaan tilatessa."),
        ],
    },
}
T["fi"]["P"] = P_FI

T["fi"]["hub"] = {
    "title": "Piharakennukset mittatilauksena: varastot, leikkimökit, ulko-WC, roskakatokset | Jääkärihirsi",
    "desc": "Hirsi- ja puurakenteiset piharakennukset Kortesjärveltä: pihavarastot, puuladot, leikkimökit, ulko-WC:t ja roskakatokset mittatilauksena, valmiiksi koottuina tai runkona.",
    "h1": "Piharakennukset <em>mittatilauksena</em>",
    "lead": "Hirsi- tai puurakenteiset piharakennukset kodin ja kesämökin pihapiiriin. Toimitamme rakennuksen valmiiksi koottuna tai runkona osina.",
    "img": ("varasto-2", "Pihavarasto pariovilla"),
}

T["fi"]["company"] = {
    "title": "Jääkärihirsi Oy | Hirsirakentaja Kortesjärvellä, Kauhava",
    "desc": "Jääkärihirsi Oy on piharakennusten, hirsikalusteiden ja pihakoristeiden valmistaja Kauhavan Kortesjärvellä. Kotimainen höylähirsi, mittatilaus, toimitus valmiina tai runkona.",
    "h1": "Hirsirakentaja <em>Kortesjärveltä</em>",
    "lead": "Jääkärihirsi Oy on piharakennusten, -kalusteiden ja -koristeiden hirsirakentaja Kauhavan Kortesjärvellä.",
    "img": ("sauna-runko", "Saunan hirsirunko Jääkärihirren pihalla"),
    "p": [
        "Olemme erikoistuneet laadukkaiden hirsi- ja puurakennusten valmistamiseen. Teemme kotimaisena laatutyönä, asiakkaan toiveiden mukaan niin pihasaunat, pihavarastot kuin hirsikalusteet ja -koristeet.",
        "Tiedämme, miten rakennetaan hengittävä ja kestävä hirsirakennus, joka palvelee käyttäjäänsä sukupolvelta toiselle. Käytämme aina kotimaisia raaka-aineita, jotka kestävät suomalaisen sään vaihtelut vuodesta toiseen.",
        "Tilaamalla piharakennuksen, hiekkalaatikon tai vaikkapa saunan mökillesi Jääkärihirreltä tuet aitoa kotimaista työtä.",
    ],
    "mat_h": "Materiaalit",
    "mat": [("Höylähirsi 70 × 145 mm", "Saunat ja hirsikalusteet"),
            ("Höylähirsi 45 × 145 mm", "Saunat, varastot, leikkimökit, ulko-WC:t"),
            ("Ulkovuoripaneeli 20 × 95 mm", "Varastot"), ("Ulkovuoripaneeli 20 × 120 mm", "Ulko-WC:t ja muut paneelirakennukset"),
            ("Kevythirsi 50 × 125 mm", "Puuladot"), ("Kotimainen kestopuu", "Hiekkalaatikot")],
    "deliv_h": "Toimitustavat",
    "deliv": [("Avaimet käteen", "Toimitamme rakennuksen valmiiksi koottuna."),
              ("Runkotoimitus", "Saat rakennuksen osina itse koottavaksi tai oman rakentajasi koottavaksi."),
              ("Pientavarat rahtina", "Kalusteet ja pihakoristeet kuljetuksineen koko Suomeen.")],
    "deliv_img": ("tuomas20-1", "Valmis pihasauna asiakkaan pihalla"),
}

T["fi"]["quote"] = {
    "title": "Tarjouspyyntö: suunnittele pihasauna tai piharakennus | Jääkärihirsi",
    "desc": "Valitse tuote, mitat ja varustelu, niin näet pohjakuvan ja pinta-alan heti. Lähetä tarjouspyyntö Jääkärihirrelle Kortesjärvelle.",
    "h1": "Suunnittele ja <em>pyydä tarjous</em>",
    "lead": "Valitse tuote ja mitat, niin näet pohjakuvan ja pinta-alan heti. Tarkennetaan yksityiskohdat yhdessä ennen tarjousta.",
    "s1": "Mitä olet tilaamassa?", "s2": "Mitat ja varustelu", "s3": "Toimitus", "s4": "Yhteystiedot",
    "width": "Leveys (m)", "length": "Pituus (m)", "diam": "Halkaisija (m)", "frame": "Runko", "roof": "Katto", "extras": "Lisävalinnat",
    "model": "Malli", "delivery": "Toimitustapa", "town": "Toimituspaikkakunta", "town_ph": "Esim. Lapua",
    "when": "Aikataulu", "when_ph": "Esim. kesäkuu 2027", "more": "Lisätietoja", "more_ph": "Esim. ikkunoiden paikat, väri, tontin kulkuyhteys",
    "send": "Lähetä tarjouspyyntö", "summary": "Yhteenveto", "area": "Pinta-ala", "inner": "Rakennus",
    "terrace": "Terassi", "porch": "Kuisti", "steam": "Löylyhuone", "dress": "Pukuhuone",
    "qty": "Määrä (kpl)", "bins": "Jäteastioita", "price_note": "Alkaen-hinta on suuntaa antava. Lopullinen hinta tarjouksella.",
    "plan_note": "Pohjakuva on havainnollistava.",
    "items": {
        "kalusteet": ["Hirsipöytäsarja", "Muu hirsikaluste"],
        "koristeet": ["Maitolaituri", "Koristekaivo", "Postilaatikkoteline"],
    },
    "frames": ["Höylähirsi 45 × 145 mm", "Höylähirsi 70 × 145 mm", "Ulkovuoripaneeli 20 × 95 mm", "Ulkovuoripaneeli 20 × 120 mm"],
    "roofs": ["Palahuopa", "Peltikate"],
    "deliveries": ["Avaimet käteen (valmiiksi koottuna)", "Runkotoimitus (osina)"],
    "extras_by": {
        "pihasauna": ["Terassi", "Katettu kuisti", "Kiuas vesisäiliöllä", "Kiuas hormisäiliöllä", "Lasiovi saunaan"],
        "pihavarasto": ["Rakoseinä (puulato)", "Pariovet", "Ikkuna"],
        "leikkimokki": ["Kuisti", "Maalattu (punamulta + valkoiset listat)", "Hiekkalaatikko"],
        "wc": ["Euromakki HD -elementti", "Oma käymälälaite"],
        "roskakatos": ["Ovet", "Maalattu"],
        "kalusteet": ["Petsattu"],
        "koristeet": ["Maalattu valitsemallani värillä"],
    },
}

T["fi"]["contact"] = {
    "title": "Yhteystiedot | Jääkärihirsi Oy, Kortesjärvi",
    "desc": "Jääkärihirsi Oy, Puusepäntie 32, 62420 Kortesjärvi. Puh. 045 119 7289, info@jaakarihirsi.com. Arkisin 7–18.",
    "h1": "Ota <em>yhteyttä</em>",
    "lead": "Meidät tavoittaa aina puhelimitse. Kerro tuote, likimääräiset mitat ja paikkakunta, niin palaamme asiaan nopeasti.",
    "hours": "Aukioloajat", "hours_v": "Maanantai–perjantai 7.00–18.00",
}

T["fi"]["privacy"] = {
    "title": "Tietosuojaseloste | Jääkärihirsi Oy",
    "h1": "Tietosuojaseloste",
    "lead": "Jääkärihirsi Oy:n asiakasrekisterin tietosuojaseloste (EU:n yleinen tietosuoja-asetus).",
    "sections": [
        ("Rekisterinpitäjä", "Jääkärihirsi Oy, Puusepäntie 32, 62420 Kortesjärvi. Y-tunnus 2386106-5. Yhteyshenkilö: info@jaakarihirsi.com, 045 119 7289."),
        ("Käyttötarkoitus", "Henkilötietoja käsitellään yhteydenottoihin vastaamiseen, tarjousten laatimiseen, tilausten toimittamiseen ja laskutukseen. Tietoja ei käytetä automatisoituun päätöksentekoon tai profilointiin."),
        ("Käsittelyn peruste", "Asiakkaan pyyntö (tarjous), sopimuksen täytäntöönpano tai rekisterinpitäjän oikeutettu etu asiakassuhteen hoitamisessa."),
        ("Tietosisältö", "Nimi, puhelinnumero, sähköpostiosoite, paikkakunta sekä lomakkeella annetut tiedot tilattavasta tuotteesta."),
        ("Säilytys", "Tarjouspyyntöjä säilytetään niin kauan kuin se on asiakassuhteen ja kirjanpitolain kannalta tarpeen."),
        ("Luovutukset", "Tietoja ei luovuteta ulkopuolisille, paitsi viranomaisten niin edellyttäessä. Sivuston ja sähköpostin palveluntarjoajat käsittelevät tietoja lukuumme."),
        ("Evästeet", "Sivusto käyttää evästeitä sivuston toimintaan, kävijäseurantaan (Google Analytics Google Tag Managerin kautta) ja chat-palveluun (Groweo). Analytiikka- ja markkinointievästeet asetetaan vain suostumuksellasi, jonka voit muuttaa milloin tahansa sivun alareunan Evästeasetukset-linkistä."),
        ("Rekisteröidyn oikeudet", "Sinulla on oikeus tarkastaa, korjata ja pyytää poistamaan tietosi sekä vastustaa käsittelyä. Voit tehdä valituksen tietosuojavaltuutetulle."),
    ],
    "cookie_h": "Evästeseloste",
    "thanks_h": "Kiitos <em>viestistäsi!</em>", "thanks_p": "Palaamme asiaan mahdollisimman pian. Kiireellisissä asioissa soita 045 119 7289.",
    "nf_h": "Sivua ei <em>löytynyt</em>", "nf_p": "Sivusto on uudistunut, ja osa osoitteista on muuttunut.",
}

# =====================================================================================================
# SVENSKA
# =====================================================================================================
T["sv"] = {
    "lang": "sv", "locale": "sv_FI", "home": "/sv/", "other": "fi", "other_label": "Suomi", "other_short": "FI",
    "nav": [("Gårdsbastur", "/sv/gardsbastur/"), ("Gårdsbyggnader", "/sv/gardsbyggnader/"), ("Möbler", "/sv/timmermoebler/"),
            ("Dekorationer", "/sv/gardsdekorationer/"), ("Företaget", "/sv/foretaget/"), ("Kontakt", "/sv/kontakt/")],
    "paths": {"quote": "/sv/offert/", "contact": "/sv/kontakt/", "company": "/sv/foretaget/", "privacy": "/sv/dataskydd/",
              "thanks": "/sv/tack/", "hub": "/sv/gardsbyggnader/"},
    "ui": {
        "quote": "Be om offert", "call": "Ring", "menu": "Meny", "skip": "Hoppa till innehållet", "from": "från",
        "ask_price": "Pris enligt offert", "vat": "Priserna inkl. moms 25,5 %.", "more": "Läs mer", "products": "Produkter",
        "other_products": "Andra produkter", "faq": "Vanliga frågor", "ask_this": "Be om offert på denna", "gallery": "Bilder",
        "home": "Hem", "close": "Stäng", "prev": "Föregående", "next": "Nästa", "company": "Företaget", "contact": "Kontakt",
        "privacy": "Dataskydd", "cookies": "Cookie-inställningar", "weekdays": "Vardagar 7–18", "reach": "Du når oss alltid per telefon.",
        "demo": "Webbplatsförslag: Äijä Group. Detta är en förhandsversion.", "open_map": "Öppna kartan", "mobile_quote": "Offert",
        "made_in": "Tillverkat i Kortesjärvi av inhemskt timmer.",
    },
    "home_title": "Gårdsbastur och gårdsbyggnader av timmer, Kortesjärvi | Jääkärihirsi",
    "home_desc": "Jääkärihirsi Oy tillverkar gårdsbastur, förråd, lekstugor, utedass, sopskjul och timmermöbler enligt måttbeställning av inhemskt planhyvlat timmer i Kortesjärvi. Nyckelfärdigt eller som stomleverans.",
    "hero_h1": "Gårdsbastur och gårdsbyggnader <em>av timmer</em>",
    "hero_lead": "Vi tillverkar bastur, förråd och lekstugor av inhemskt planhyvlat timmer i Kortesjärvi enligt dina mått. Du får byggnaden färdigt hopsatt eller som stomme.",
    "hero_cta": "Planera och be om offert",
    "products_h": "Vad <em>behöver du?</em>",
    "products_p": "Alla produkter tillverkas enligt måttbeställning. Priserna inkluderar moms.",
    "why_h": "Timringsföretag <em>från Kortesjärvi</em>",
    "why": [
        ("Inhemskt planhyvlat timmer", "Stommar av 45 × 145 eller 70 × 145 mm planhyvlat timmer eller 20 × 95 och 20 × 120 mm ytterpanel. Råvarorna är inhemska."),
        ("Enligt dina mått", "Standardmodellerna är en utgångspunkt, och storlek, fönster, terrass och takmaterial avtalas enligt dina önskemål."),
        ("Färdig eller som stomme", "Vi levererar byggnaden färdigt hopsatt nyckelfärdigt eller som stomme i delar. Vi levererar till hela Finland."),
    ],
    "why_img": ("sauna-sisa-1", "Granlavar i en gårdsbastu"),
    "steps_h": "Så går <em>beställningen till</em>",
    "steps": [
        ("Berätta om dina önskemål", "Välj produkt och mått i offertförfrågan eller ring. Bilder och skisser hjälper."),
        ("Offert och avtal", "Du får en offert där stomme, utrustning och leveranssätt är specificerade."),
        ("Tillverkning i Kortesjärvi", "Byggnaden tillverkas i vår egen hall i Kortesjärvi."),
        ("Leverans färdig eller i delar", "Vi levererar byggnaden färdigt hopsatt nyckelfärdigt eller som stomme i delar för egen montering."),
    ],
    "steps_img": ("varasto-7", "Gårdsförråd under tillverkning i Jääkärihirsis hall"),
    "contact_h": "Be om <em>offert</em>",
    "contact_p": "Ring eller skicka ett meddelande, så svarar vi så snabbt som möjligt. Berätta produkt, ungefärliga mått och leveransort.",
    "form": {
        "send": "Skicka meddelande", "name": "Namn *", "phone": "Telefon", "email": "E-post", "town": "Ort",
        "msg": "Meddelande", "product": "Produkt", "choose": "Välj produkt", "other": "Annat / vet inte ännu",
        "consent": 'Jag godkänner behandlingen av mina uppgifter enligt <a class="link" href="/sv/dataskydd/">dataskyddsbeskrivningen</a>.',
        "err": "Fyll i namn och telefon eller e-post.", "senderr": "Det gick inte att skicka. Ring 045 119 7289 eller försök igen.",
        "title": "Skicka meddelande",
    },
}

DELIV_FAQ_SV = ("Vad är skillnaden mellan nyckelfärdig leverans och stomleverans?",
                "Vid nyckelfärdig leverans levereras byggnaden färdigt hopsatt. Vid stomleverans får du byggnaden i delar för egen montering eller för din egen byggare. Leveranssättet avtalas i offerten.")

P_SV = {
    "pihasauna": {
        "name": "Gårdsbastur", "card": "Gårdsbastu", "short": "Timmerbastur för gården och stugan enligt mått.", "from": 7500, "hero_pos": "50% 32%",
        "title": "Gårdsbastu av timmer enligt måttbeställning, nyckelfärdig | Jääkärihirsi, Kortesjärvi",
        "desc": "Gårdsbastur av inhemskt planhyvlat timmer (45 × 145 eller 70 × 145 mm) enligt dina mått. Vedeldat aggregat, granlavar, omklädningsrum och terrass. Nyckelfärdigt eller som stomleverans, från 7 500 €.",
        "h1": "Gårdsbastur <em>av timmer</em>",
        "lead": "Timmerbastu till gården eller stugan enligt dina mått. Du får bastun färdigt hopsatt nyckelfärdigt eller som stomme i delar.",
        "intro_h": "En bastu som består <em>i generationer</em>", "intro_img": "sauna-sisa-2",
        "intro": [
            "Gårdsbastur av timmer hör till våra populäraste produkter. Vi tillverkar basturna i Kortesjärvi enligt kundens mått av planhyvlat timmer i måtten 70 × 145 mm eller 45 × 145 mm.",
            "Planhyvlat timmer är ett hållbart material som passar fint in i den finska gårdsmiljön. I bastun finns granlavar och ett vedeldat aggregat med vattenbehållare eller rörbehållare. I byggnaden ryms ett omklädningsrum och vid önskemål en terrass.",
        ],
        "list_h": "Standardutrustning",
        "list": ["Timmerstomme 45 × 145 eller 70 × 145 mm", "Brädgolv, avlopp i bastun", "Granlavar och granpanel i taket",
                 "Ull + aluminiumfolie i mellantaket", "Fönster som går att öppna, glasdörr till bastun", "Vedeldat aggregat med vatten- eller rörbehållare + skorsten",
                 "Skyddsplåt bakom och under aggregatet", "Takpapp"],
        "models_h": "Bastumodeller",
        "models": [
            ("Gårdsbastu Tuomas 15", "Täckt veranda och rymligt omklädningsrum. Nyckelfärdigt eller som stomleverans.",
             ["Timmerstomme 45 × 145 eller 70 × 145 mm", "Täckt veranda", "Aggregat med vatten- eller rörbehållare"], None,
             ["tuomas15-1", "tuomas15-2", "tuomas15-3", "tuomas15-4"]),
            ("Gårdsbastu Tuomas 20", "Större modell: terrass med räcke och plats för flera bastubadare.",
             ["Timmerstomme 45 × 145 eller 70 × 145 mm", "Terrass med räcke", "Aggregat med vatten- eller rörbehållare"], None,
             ["tuomas20-1", "tuomas20-2", "tuomas20-3", "tuomas20-4", "tuomas20-5"]),
        ],
        "gallery_h": "Bastur vi har byggt",
        "gallery": [("sauna-1", "Gårdsbastu med veranda"), ("sauna-2", "Gårdsbastu med pardörr"), ("sauna-3", "Gårdsbastu med pulpettak"),
                    ("sauna-4", "Gårdsbastu med pulpettak"), ("sauna-5", "Gårdsbastu på vintern"), ("sauna-6", "Gårdsbastu med glasdörr"),
                    ("sauna-7", "Gårdsbastu"), ("sauna-runko", "Bastustomme med terrass"),
                    ("sauna-sisa-1", "Granlavar"), ("sauna-sisa-3", "Vedeldat aggregat och lavar"), ("sauna-sisa-4", "Bastulavar"),
                    ("sauna-sisa-5", "Aggregat med rörbehållare"), ("sauna-sisa-6", "Glasdörr till bastun"), ("sauna-sisa-7", "Bastuns interiör"),
                    ("sauna-sisa-8", "Aggregat och lavar")],
        "band": ("tuomas15-3", "Bastubad året om", "På sommaren svalkande på terrassen, på vintern ett dopp i snön."),
        "faq": [
            DELIV_FAQ_SV,
            ("Av hur tjockt timmer tillverkas bastun?", "Av planhyvlat timmer i måtten 70 × 145 mm eller 45 × 145 mm. Tjockare timmer passar särskilt för året runt-bruk, så berätta hur bastun ska användas så rekommenderar vi rätt."),
            ("Kan jag själv bestämma storlek och planlösning?", "Ja. Vi tillverkar alltid basturna enligt måttbeställning, så storlek, fönster, terrass och omklädningsrummets storlek avtalas enligt dina önskemål."),
            ("Vart levererar ni bastur?", "Vi levererar gårdsbastur till hela Finland från Kauhava-regionen, antingen färdigt hopsatta eller som stomme i delar."),
            ("Behövs bygglov för en gårdsbastu?", "Det beror på kommunen och byggnadens storlek. Kontrollera med byggnadstillsynen i din kommun före beställning. Vid behov får du mått och bilder av oss för ansökan."),
        ],
    },
    "pihavarasto": {
        "name": "Gårdsförråd och vedlador", "card": "Gårdsförråd", "short": "Förråd och vedlador av timmer eller panel.", "from": 2000,
        "title": "Gårdsförråd och vedlada av timmer enligt mått | Jääkärihirsi",
        "desc": "Gårdsförråd av 45 × 145 planhyvlat timmer eller 20 × 95 ytterpanel och vedlador av lätt timmer enligt kundens mått. Gårdsförråd från 2 700 €, vedlada från 2 000 €.",
        "h1": "Gårdsförråd och <em>vedlador</em>",
        "lead": "Förråd och vedlador av timmer eller trä enligt måttbeställning. Du får dem färdigt hopsatta så att du kan använda dem direkt.",
        "intro_h": "Plats för saker <em>och ved</em>",
        "intro": [
            "Vi tillverkar förråd av 45 × 145 planhyvlat timmer eller 20 × 95 ytterpanel enligt kundens mått. Vedladorna tillverkas av finsågat lätt timmer, antingen med springa så att veden torkar eller med täta väggar.",
            "Vi levererar byggnaden färdigt hopsatt eller som stomme i delar.",
        ],
        "list_h": "Alternativ",
        "list": ["Stomme 45 × 145 mm timmer eller 20 × 95 mm ytterpanel", "Vedlada: vägg 50 × 125 mm med 15 mm springa eller tät",
                 "Brädgolv", "Takpapp eller plåttak", "Mått enligt kunden"],
        "models_h": "Modeller",
        "models": [
            ("Gårdsförråd", "Gårdsförråd enligt kundens mått av timmer eller ytterpanel, med dörr eller pardörrar.",
             ["Stomme 45 × 145 timmer eller 20 × 95 panel", "Brädgolv", "Takpapp"], 2700,
             ["varasto-1", "varasto-2", "varasto-3", "varasto-4", "varasto-5", "varasto-6", "varasto-7", "varasto-8", "varasto-9",
              "varasto-10", "varasto-11", "varasto-12", "varasto-13", "varasto-14"]),
            ("Vedlada", "Vedlada för brännved. Standardstorlek 2 × 3 m, även enligt kundens mått.",
             ["Stomme 50 × 125 mm planka", "Golv 22 × 100 mm bräda", "Svart plåttak"], 2000,
             ["puulato-a", "puulato-b", "puulato-1", "puulato-2"]),
        ],
        "faq": [
            DELIV_FAQ_SV,
            ("Behövs bygglov för ett förråd?", "Mindre ekonomibyggnader kräver i många kommuner lov först över en viss storlek, men gränserna varierar. Kontrollera med byggnadstillsynen i din kommun."),
            ("Kan vedladan byggas med täta väggar?", "Ja. Väggen görs antingen med 15 mm springa så att veden luftas, eller helt tät."),
        ],
    },
    "leikkimokki": {
        "name": "Lekstugor och sandlådor", "card": "Lekstuga", "short": "Lekstugor och sandlådor för barn.", "from": 1500,
        "title": "Lekstuga av timmer eller panel enligt mått | Jääkärihirsi",
        "desc": "Lekstugor av 45 × 145 timmer eller panelelement, standardmått 2 500 × 1 800 mm eller egna mått. Även sandlådor av inhemskt hållbart trä. Lekstugor från 1 500 €.",
        "h1": "Lekstugor och <em>sandlådor</em>",
        "lead": "Lekstugor med timmer- eller panelstomme i standardmått eller enligt dina mått samt sandlådor för de minsta.",
        "intro_h": "En egen stuga <em>för barnen</em>",
        "intro": [
            "Vi tillverkar lekstugorna av timmer och panel enligt kundens mått. Vi erbjuder även standardmått, till exempel 2 500 × 1 800 mm.",
            "Stugan finns i träfärg eller målad. På bilderna finns också traditionell rödmylla med vita lister och verandaräcken.",
        ],
        "list_h": "Lekstugan innehåller",
        "list": ["Timmerstomme 45 × 145 mm eller panelelementstomme", "Fönster av plastskiva", "Brädgolv + plastmatta", "Takpapp"],
        "models_h": "Modeller",
        "models": [
            ("Lekstuga", "Lekstuga med timmer- eller panelstomme, till exempel 2 500 × 1 800 mm. Med eller utan veranda, även med mansardtak.",
             ["Timmer 45 × 145 mm eller panel", "Fönster av plastskiva", "Brädgolv + plastmatta"], 1500,
             ["leikkimokki-a", "leikkimokki-b", "leikkimokki-c", "leikkimokki-d", "leikkimokki-e", "leikkimokki-f", "leikkimokki-g",
              "leikkimokki-h", "leikkimokki-i", "leikkimokki-j", "leikkimokki-k"]),
            ("Sandlåda", "Flerkantig eller fyrkantig sandlåda av inhemskt hållbart trä, även enligt kundens mått.",
             ["Sex- eller fyrkantig", "Inhemskt hållbart trä", "Mått enligt önskemål"], None,
             ["hiekkalaatikko"]),
        ],
        "faq": [
            ("Varför är fönstren av plastskiva?", "Plastskiva är säkrare än glas när barnen leker och går inte sönder."),
            ("Kan lekstugan levereras målad?", "Ja, färgen avtalas vid beställning. Stugan finns också i träfärg."),
        ],
    },
    "wc": {
        "name": "Utedass", "card": "Utedass", "short": "Utedass av timmer eller panel.", "from": 1200,
        "title": "Utedass av timmer, komposterande toalett | Jääkärihirsi",
        "desc": "Utedass av 45 × 145 timmer eller 20 × 120 ytterpanel. Euromakki HD-toalettelement eller byggnad som passar andra tillverkares utrustning. Från 1 200 €.",
        "h1": "Utedass för <em>stugan</em> och gården",
        "lead": "Utedass av timmer eller ytterpanel, färdigt med toalettelement eller anpassat till den utrustning du valt.",
        "intro_h": "Ett snyggt och fungerande <em>utedass</em>",
        "intro": [
            "Vi tillverkar utedass av 45 × 145 timmer eller 20 × 120 ytterpanel. Vi använder dasselement tillverkat av Euromakki HD-plastblandning.",
            "Vi bygger även, enligt överenskommelse, dass som lämpar sig för andra tillverkares element, av timmer eller ytterpanel.",
        ],
        "list_h": "Alternativ",
        "list": ["Stomme 45 × 145 timmer eller 20 × 120 panel", "Euromakki HD-toalettelement", "Passar även andra tillverkares ekotoaletter", "Takpapp"],
        "models_h": "Utföranden",
        "models": [
            ("Utedass", "Utedass med toalettelement, målat eller i träfärg. Trappsteg och servicelucka vid behov.",
             ["45 × 145 timmer eller 20 × 120 panel", "Euromakki HD-element", "Målat eller i träfärg"], 1200,
             ["wc-a", "wc-b", "wc-c", "wc-d"]),
        ],
        "faq": [
            ("Vilken toalettutrustning passar byggnaden?", "Som standard använder vi Euromakki HD-elementet. Vi anpassar också byggnaden till andra tillverkares utrustning, så berätta vilken du valt."),
            ("Kan utedasset byggas av panel?", "Ja, av 20 × 120 ytterpanel eller 45 × 145 timmer."),
        ],
    },
    "roskakatos": {
        "name": "Sopskjul", "card": "Sopskjul", "short": "Skjul för en eller flera soptunnor.", "from": 550,
        "title": "Sopskjul av trä för en eller flera soptunnor | Jääkärihirsi",
        "desc": "Sopskjul för en eller flera soptunnor, med eller utan dörr. Levereras även målade. Från 550 €.",
        "h1": "<em>Sopskjul</em> för gården",
        "lead": "Ett snyggt skjul för en eller flera soptunnor, med eller utan dörr, i träfärg eller målat.",
        "intro_h": "Ordning och reda <em>på gården</em>",
        "intro": [
            "Ett sopskjul är behändigt men även snyggt och berikar gårdsmiljön. Vi tillverkar skjulen för en eller flera soplådor, med eller utan dörr.",
            "Vi levererar även skjulen färdigt målade, till exempel i husets färger.",
        ],
        "list_h": "Alternativ",
        "list": ["För en eller flera tunnor", "Med dörr eller öppet", "Träfärg eller målat", "Dekorativa takfotsbräder och spaljéer"],
        "models_h": "Utföranden",
        "models": [
            ("Sopskjul", "Skjul för soptunnor med spaljé och dekorativ takfot. Dimensioneras efter antalet tunnor.",
             ["För en eller flera tunnor", "Med dörr eller öppet", "Målat"], 550,
             ["roskakatos-a", "roskakatos-b", "roskakatos-c", "roskakatos-d", "roskakatos-e", "roskakatos-f", "roskakatos-g", "roskakatos-h"]),
        ],
        "faq": [
            ("För hur stora kärl passar skjulet?", "Skjulet dimensioneras efter dina kärl. Berätta antal och storlek (t.ex. 240 l eller 660 l) i offertförfrågan."),
        ],
    },
    "kalusteet": {
        "name": "Timmermöbler", "card": "Bordsgrupp av timmer", "short": "Bordsgrupper av timmer för gården och terrassen.", "from": 400,
        "title": "Timmermöbler och bordsgrupper av timmer för gården | Jääkärihirsi",
        "desc": "Bordsgrupper och trädgårdsmöbler av 70 × 145 planhyvlat timmer från Kortesjärvi. Med eller utan färg, enligt måttbeställning. Från 400 €.",
        "h1": "Timmermöbler <em>för gården</em>",
        "lead": "Bordsgrupper av inhemskt timmer som tål väder och vind, levererade färdigt hopsatta.",
        "intro_h": "Möbler som <em>håller</em>",
        "intro": [
            "I Kortesjärvi tillverkar vi hållbara timmermöbler som tål väder och vind. Alla möbler tillverkas av inhemskt 70 × 145 planhyvlat timmer.",
            "Timmermöblerna passar på gården och på olika terrasser. Du får dem med eller utan färg, anpassade enligt din smak.",
        ],
        "list_h": "Bra att veta",
        "list": ["Möbler av 70 × 145 planhyvlat timmer", "Betsade eller i träfärg", "Levereras färdigt hopsatta", "Mått enligt önskemål", "Leverans till hela Finland"],
        "models_h": "Produkter",
        "models": [
            ("Bordsgrupp av timmer", "Bord och två bänkar för gården och terrassen. Väl omskötta håller de i flera år.",
             ["70 × 145 planhyvlat timmer", "Betsad eller utan färg", "Enligt måttbeställning"], 400,
             ["poyta-b", "poyta-a", "poyta-c", "poyta-d", "poyta-e"]),
        ],
        "faq": [
            ("Hur sköter man timmermöbler?", "Väl omskötta timmermöbler tål väder och vind i flera år. Att förnya träskyddet med några års mellanrum håller ytan i skick."),
            ("Levererar ni möbler längre bort?", "Ja, mindre produkter levererar vi med transport till hela Finland."),
        ],
    },
    "koristeet": {
        "name": "Gårdsdekorationer", "card": "Gårdsdekorationer", "short": "Mjölkbord, dekorativa brunnar och postlådeställ.", "from": 120,
        "title": "Mjölkbord, dekorativ brunn och postlådeställ av trä | Jääkärihirsi",
        "desc": "Gårdsdekorationer enligt måttbeställning från Kortesjärvi: mjölkbord från 500 €, dekorativa brunnar för 80–100 cm brunnsring från 450 € och postlådeställ från 120 €.",
        "h1": "Mjölkbord och <em>gårdsdekorationer</em>",
        "lead": "Mjölkbord, dekorativa brunnar och postlådeställ enligt måttbeställning av inhemskt trä, färdigt hopsatta och målade.",
        "intro_h": "En bit finsk <em>gårdstradition</em>",
        "intro": [
            "Drömmer du om ett trivsamt mjölkbord eller en dekorativ brunn? Behöver kvarteret ett snyggt postlådeställ? Vi tillverkar gårdsdekorationerna enligt dina önskemål, huvudsakligen av inhemska råvaror.",
            "Du får dem färdigt hopsatta och målade.",
        ],
        "list_h": "Bra att veta",
        "list": ["Färdigt hopsatta och målade", "Du kan välja färg", "Av inhemskt trä", "Mindre produkter med transport till hela Finland"],
        "models_h": "Produkter",
        "models": [
            ("Mjölkbord", "Gammaldags mjölkbord är en del av finsk identitet. Vi tillverkar dem hantverksmässigt av panel med autentiskt utseende.",
             ["Hantverk av panel", "Takpapp", "Mått enligt önskemål"], 500,
             ["maitolaituri-a", "maitolaituri-b", "maitolaituri-c", "maitolaituri-d", "maitolaituri-e", "maitolaituri-f"]),
            ("Dekorativ brunn", "En dekorativ brunn piggar upp gården. Brunnarna passar för brunnsringar på 80–100 cm och levereras färdigt hopsatta och målade.",
             ["För 80–100 cm ring", "Färdigt hopsatt", "Målad eller i träfärg"], 450,
             ["kaivo-1", "kaivo-2", "kaivo-3", "kaivo-4", "kaivo-5", "kaivo-6", "kaivo-7", "kaivo-8", "kaivo-9", "kaivo-10"]),
            ("Postlådeställ", "Ett postlådeställ livar upp husets fasad. Ställen levereras färdigt målade i önskad färg.",
             ["Färdigt hopsatt", "Målat i önskad färg"], 120,
             ["postilaatikkoteline-a", "postilaatikkoteline"]),
        ],
        "faq": [
            ("För hur stor brunnsring passar den dekorativa brunnen?", "Brunnarna tillverkas för brunnsringar på 80–100 cm."),
            ("Kan man välja färg?", "Ja. På bilderna finns modeller i rödmylla och i träfärg, och färgen avtalas vid beställning."),
        ],
    },
}
T["sv"]["P"] = P_SV

T["sv"]["hub"] = {
    "title": "Gårdsbyggnader enligt måttbeställning: förråd, lekstugor, utedass, sopskjul | Jääkärihirsi",
    "desc": "Gårdsbyggnader av timmer och trä från Kortesjärvi: förråd, vedlador, lekstugor, utedass och sopskjul enligt måttbeställning, färdigt hopsatta eller som stomme.",
    "h1": "Gårdsbyggnader <em>enligt mått</em>",
    "lead": "Gårdsbyggnader av timmer eller trä för hemmet och sommarstugan. Vi levererar byggnaden färdigt hopsatt eller som stomme i delar.",
    "img": ("varasto-2", "Gårdsförråd med pardörrar"),
}

T["sv"]["company"] = {
    "title": "Jääkärihirsi Oy | Timringsföretag i Kortesjärvi, Kauhava",
    "desc": "Jääkärihirsi Oy tillverkar gårdsbyggnader, timmermöbler och gårdsdekorationer i Kortesjärvi, Kauhava. Inhemskt planhyvlat timmer, måttbeställning, leverans färdig eller som stomme.",
    "h1": "Timringsföretag <em>från Kortesjärvi</em>",
    "lead": "Jääkärihirsi Oy är ett timringsföretag i Kortesjärvi, Kauhava, med expertis inom gårdsbyggnader, -möbler och -dekorationer.",
    "img": ("sauna-runko", "Bastustomme på Jääkärihirsis gård"),
    "p": [
        "Vår specialitet är tillverkning av högklassiga timmer- och träbyggnader. Vi bygger som inhemskt kvalitetsarbete enligt kundens önskemål, från gårdsbastur och förråd till timmermöbler och dekorationer.",
        "Vi vet hur man bygger en andningsbar och hållbar timmerbyggnad som betjänar sin användare i flera generationer. Vi använder alltid inhemska råvaror som klarar det finländska klimatet år efter år.",
        "När du beställer en gårdsbyggnad, sandlåda eller bastu av Jääkärihirsi stöder du äkta inhemskt arbete.",
    ],
    "mat_h": "Material",
    "mat": [("Planhyvlat timmer 70 × 145 mm", "Bastur och timmermöbler"),
            ("Planhyvlat timmer 45 × 145 mm", "Bastur, förråd, lekstugor, utedass"),
            ("Ytterpanel 20 × 95 mm", "Förråd"), ("Ytterpanel 20 × 120 mm", "Utedass och andra panelbyggnader"),
            ("Lätt timmer 50 × 125 mm", "Vedlador"), ("Inhemskt hållbart trä", "Sandlådor")],
    "deliv_h": "Leveranssätt",
    "deliv": [("Nyckelfärdigt", "Vi levererar byggnaden färdigt hopsatt."),
              ("Stomleverans", "Du får byggnaden i delar för egen montering eller för din egen byggare."),
              ("Mindre produkter som frakt", "Möbler och gårdsdekorationer med transport till hela Finland.")],
    "deliv_img": ("tuomas20-1", "Färdig gårdsbastu på kundens gård"),
}

T["sv"]["quote"] = {
    "title": "Offertförfrågan: planera gårdsbastu eller gårdsbyggnad | Jääkärihirsi",
    "desc": "Välj produkt, mått och utrustning, så ser du planritningen och ytan direkt. Skicka offertförfrågan till Jääkärihirsi i Kortesjärvi.",
    "h1": "Planera och <em>be om offert</em>",
    "lead": "Välj produkt och mått, så ser du planritningen och ytan direkt. Vi preciserar detaljerna tillsammans före offerten.",
    "s1": "Vad vill du beställa?", "s2": "Mått och utrustning", "s3": "Leverans", "s4": "Kontaktuppgifter",
    "width": "Bredd (m)", "length": "Längd (m)", "diam": "Diameter (m)", "frame": "Stomme", "roof": "Tak", "extras": "Tillval",
    "model": "Modell", "delivery": "Leveranssätt", "town": "Leveransort", "town_ph": "T.ex. Nykarleby",
    "when": "Tidtabell", "when_ph": "T.ex. juni 2027", "more": "Mer information", "more_ph": "T.ex. fönstrens placering, färg, tillfart till tomten",
    "send": "Skicka offertförfrågan", "summary": "Sammanfattning", "area": "Yta", "inner": "Byggnad",
    "terrace": "Terrass", "porch": "Veranda", "steam": "Bastu", "dress": "Omklädningsrum",
    "qty": "Antal (st.)", "bins": "Soptunnor", "price_note": "Från-priset är riktgivande. Slutligt pris enligt offert.",
    "plan_note": "Planritningen är illustrativ.",
    "items": {
        "kalusteet": ["Bordsgrupp av timmer", "Annan timmermöbel"],
        "koristeet": ["Mjölkbord", "Dekorativ brunn", "Postlådeställ"],
    },
    "frames": ["Planhyvlat timmer 45 × 145 mm", "Planhyvlat timmer 70 × 145 mm", "Ytterpanel 20 × 95 mm", "Ytterpanel 20 × 120 mm"],
    "roofs": ["Takpapp", "Plåttak"],
    "deliveries": ["Nyckelfärdigt (färdigt hopsatt)", "Stomleverans (i delar)"],
    "extras_by": {
        "pihasauna": ["Terrass", "Täckt veranda", "Aggregat med vattenbehållare", "Aggregat med rörbehållare", "Glasdörr till bastun"],
        "pihavarasto": ["Springvägg (vedlada)", "Pardörrar", "Fönster"],
        "leikkimokki": ["Veranda", "Målad (rödmylla + vita lister)", "Sandlåda"],
        "wc": ["Euromakki HD-element", "Egen toalettutrustning"],
        "roskakatos": ["Dörrar", "Målat"],
        "kalusteet": ["Betsat"],
        "koristeet": ["Målat i önskad färg"],
    },
}

T["sv"]["contact"] = {
    "title": "Kontakt | Jääkärihirsi Oy, Kortesjärvi",
    "desc": "Jääkärihirsi Oy, Puusepäntie 32, 62420 Kortesjärvi. Tfn 045 119 7289, info@jaakarihirsi.com. Vardagar 7–18.",
    "h1": "Ta <em>kontakt</em>",
    "lead": "Du når oss alltid per telefon. Berätta produkt, ungefärliga mått och ort, så återkommer vi snabbt.",
    "hours": "Öppettider", "hours_v": "Måndag–fredag 7.00–18.00",
}

T["sv"]["privacy"] = {
    "title": "Dataskyddsbeskrivning | Jääkärihirsi Oy",
    "h1": "Dataskyddsbeskrivning",
    "lead": "Dataskyddsbeskrivning för Jääkärihirsi Oy:s kundregister (EU:s allmänna dataskyddsförordning).",
    "sections": [
        ("Personuppgiftsansvarig", "Jääkärihirsi Oy, Puusepäntie 32, 62420 Kortesjärvi. FO-nummer 2386106-5. Kontaktperson: info@jaakarihirsi.com, 045 119 7289."),
        ("Ändamål", "Personuppgifter behandlas för att besvara kontakter, upprätta offerter, leverera beställningar och fakturera. Uppgifterna används inte för automatiserat beslutsfattande eller profilering."),
        ("Rättslig grund", "Kundens begäran (offert), fullgörande av avtal eller den personuppgiftsansvariges berättigade intresse."),
        ("Uppgifter", "Namn, telefonnummer, e-postadress, ort samt uppgifter om den beställda produkten som lämnats i formuläret."),
        ("Lagring", "Offertförfrågningar sparas så länge det behövs för kundrelationen och enligt bokföringslagen."),
        ("Utlämnande", "Uppgifterna lämnas inte ut till utomstående, utom när myndigheter kräver det. Leverantörerna av webbplatsen och e-posten behandlar uppgifter för vår räkning."),
        ("Kakor", "Webbplatsen använder kakor för webbplatsens funktion, besöksstatistik (Google Analytics via Google Tag Manager) och chattjänsten (Groweo). Statistik- och marknadsföringskakor sätts endast med ditt samtycke, som du kan ändra när som helst via länken Cookie-inställningar längst ned på sidan."),
        ("Dina rättigheter", "Du har rätt att granska, rätta och begära radering av dina uppgifter samt att invända mot behandlingen. Du kan lämna klagomål till dataombudsmannen."),
    ],
    "cookie_h": "Kakdeklaration",
    "thanks_h": "Tack för <em>ditt meddelande!</em>", "thanks_p": "Vi återkommer så snart som möjligt. I brådskande ärenden, ring 045 119 7289.",
    "nf_h": "Sidan <em>hittades inte</em>", "nf_p": "Webbplatsen har förnyats och en del adresser har ändrats.",
}
