# -*- coding: utf-8 -*-
"""Jääkärihirsi Oy (jaakarihirsi.com) – sivuston sisällöt suomeksi ja ruotsiksi.

Lähde: vanha Duda-sivu (fi + sv, 3.10.2026). Hinnat "alkaen" ovat vanhan sivun RUOTSINKIELISISTÄ versioista –
suomenkielisiltä sivuilta ne puuttuivat. SHOW_PRICES = False piilottaa kaikki hinnat.
Kuvat: src/kuvat/ (-ai = Higgsfield-kuva, muut asiakkaan omia).
"""

SHOW_PRICES = True

COMPANY = {
    "name": "Jääkärihirsi Oy", "short": "Jääkärihirsi", "domain": "jaakarihirsi.com",
    "phone": "045 119 7289", "intl": "+358451197289", "email": "info@jaakarihirsi.com",
    "street": "Puusepäntie 32", "zip": "62420", "city": "Kortesjärvi", "town": "Kauhava", "region": "Etelä-Pohjanmaa",
    "ytunnus": "2386106-5", "geo": (63.3127, 23.1695), "radius": 200,
}

# Tuotteet: slug-avain, sivun polku fi/sv, kuva, hinta alkaen (None = kysy)
# type: building = mitat + pohjakuva, sauna = building + saunavalinnat, octagon = huvimaja, count = kappalemäärä, bins = astioiden määrä
PRODUCTS = [
    # key, fi-path, sv-path, img, price, type, defaults (leveys, pituus)
    ("pihasauna", "/pihasaunat/", "/sv/gardsbastur/", "pihasauna-jarvi-ai", 5600, "sauna", (3.0, 4.0)),
    ("pihavarasto", "/piharakennukset/pihavarastot/", "/sv/gardsbyggnader/forrad/", "pihavarasto-ai", 1400, "building", (2.1, 4.2)),
    ("huvimaja", "/piharakennukset/huvimajat/", "/sv/gardsbyggnader/lusthus/", "huvimaja-ai", 2100, "octagon", (3.0, 3.0)),
    ("leikkimokki", "/piharakennukset/leikkimokit/", "/sv/gardsbyggnader/lekstugor/", "leikkimokki-ai", 950, "building", (1.8, 2.5)),
    ("wc", "/piharakennukset/ulko-wc/", "/sv/gardsbyggnader/utedass/", "wc-ai", 880, "building", (1.2, 1.5)),
    ("roskakatos", "/piharakennukset/roskakatokset/", "/sv/gardsbyggnader/sopskjul/", "roskakatos-ai", 600, "bins", (1.0, 2.0)),
    ("kalusteet", "/hirsikalusteet/", "/sv/timmermoebler/", "kalusteet-4", 580, "count", (0, 0)),
    ("koristeet", "/pihakoristeet/", "/sv/gardsdekorationer/", "maitolaituri-ai", 180, "count", (0, 0)),
]
PROD = {p[0]: p for p in PRODUCTS}
BUILDINGS = ["pihavarasto", "huvimaja", "leikkimokki", "wc", "roskakatos"]

# Vanhan sivun osoitteet → uudet (server.js / _redirects). Säilyneet: /pihasaunat, /piharakennukset, /hirsikalusteet, /pihakoristeet, /yhteystiedot, /sv/...
REDIRECTS = {
    "/evasteet/": "/tietosuoja/#evasteet",
    "/sv/kontakt-1/": "/sv/kontakt/",
}

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
        "demo": "Sivustoehdotus – Äijä Group. Tämä on esikatseluversio.", "open_map": "Avaa kartalla", "mobile_quote": "Tarjous",
        "made_in": "Tehty Kortesjärvellä kotimaisesta hirrestä.",
    },
    "home_title": "Pihasaunat ja piharakennukset hirrestä – Kortesjärvi | Jääkärihirsi",
    "home_desc": "Jääkärihirsi Oy valmistaa pihasaunat, pihavarastot, huvimajat, leikkimökit, ulko-WC:t ja hirsikalusteet mittatilauksena kotimaisesta höylähirrestä Kortesjärvellä. Avaimet käteen tai runkotoimituksena.",
    "hero_h1": "Pihasaunat ja piharakennukset <em>hirrestä</em>",
    "hero_lead": "Valmistamme Kortesjärvellä kotimaisesta höylähirrestä saunat, varastot, huvimajat ja leikkimökit mittojesi mukaan – avaimet käteen tai runkotoimituksena.",
    "hero_cta": "Suunnittele ja pyydä tarjous",
    "products_h": "Mitä <em>tarvitset?</em>",
    "products_p": "Kaikki tuotteet tehdään mittatilauksena. Hinnat sisältävät arvonlisäveron.",
    "why_h": "Hirsirakentaja <em>Kortesjärveltä</em>",
    "why": [
        ("Kotimainen höylähirsi", "Rungot 45, 58 tai 70 mm höylähirrestä tai ulkovuoripaneelista. Raaka-aineet ovat kotimaisia."),
        ("Mittasi mukaan", "Vakiomallit ovat lähtökohta – koko, ikkunat, terassi ja katemateriaali sovitaan toiveidesi mukaan."),
        ("Avaimet käteen tai runkona", "Pystytämme rakennuksen valmiiksi noin 200 km säteellä Kortesjärveltä. Pientavarat toimitamme koko Suomeen."),
    ],
    "map_label": "Pystytys noin 200 km säteellä",
    "map_note": "Pientavarat kuljetuksineen koko Suomeen.",
    "steps_h": "Näin tilaus <em>etenee</em>",
    "steps": [
        ("Kerro toiveet", "Valitse tuote ja mitat tarjouspyynnössä tai soita – kuvat ja luonnokset auttavat."),
        ("Tarjous ja sopimus", "Saat tarjouksen, jossa runko, varustelu ja toimitustapa on eritelty."),
        ("Valmistus Kortesjärvellä", "Rakennus tehdään omassa hallissamme ja kuljetetaan perille."),
        ("Pystytys tai runkotoimitus", "Pystytämme valmiiksi tai toimitamme rungon itse koottavaksi sopimuksen mukaan."),
    ],
    "contact_h": "Kysy <em>tarjous</em>",
    "contact_p": "Soita tai jätä viesti – vastaamme mahdollisimman nopeasti. Kerro tuote, likimääräiset mitat ja toimituspaikkakunta.",
    "form": {
        "send": "Lähetä viesti", "name": "Nimi *", "phone": "Puhelin", "email": "Sähköposti", "town": "Paikkakunta",
        "msg": "Viesti", "product": "Tuote", "choose": "Valitse tuote", "other": "Muu / en tiedä vielä",
        "consent": 'Hyväksyn tietojeni käsittelyn <a class="link" href="/tietosuoja/">tietosuojaselosteen</a> mukaisesti.',
        "err": "Täytä nimi ja joko puhelin tai sähköposti.", "senderr": "Lähetys epäonnistui. Soita 045 119 7289 tai yritä uudelleen.",
        "title": "Lähetä viesti",
    },
}

# Tuotesivut (fi). models: nimi, teksti, varustelu, hinta, kuvat
P_FI = {
    "pihasauna": {
        "name": "Pihasaunat", "card": "Pihasauna", "short": "Hirsisaunat koti- ja mökkipihaan mittatilauksena.",
        "title": "Pihasauna hirrestä mittatilauksena – avaimet käteen | Jääkärihirsi, Kortesjärvi",
        "desc": "Pihasaunat kotimaisesta höylähirrestä (45, 58 tai 70 mm) mittojesi mukaan. Puukiuas, kuusilauteet, pukuhuone ja terassi. Avaimet käteen tai runkotoimituksena.",
        "h1": "Pihasaunat <em>hirrestä</em>",
        "lead": "Hirsisauna koti- tai mökkipihaan mittojesi mukaan – valmiiksi pystytettynä avaimet käteen tai runkotoimituksena.",
        "intro_h": "Sauna, joka kestää <em>sukupolvelta toiselle</em>", "intro_img": "sauna-sisa-ai",
        "intro": [
            "Hirsirakenteiset pihasaunat ovat suosituimpia tuotteitamme. Valmistamme saunat Kortesjärvellä asiakkaan mittojen mukaan pääsääntöisesti höylähirrestä, jonka vahvuus on 70 × 150 mm, 58 mm tai 45 × 150 mm.",
            "Höylähirsi on kestävä materiaali ja sopii ulkonäöltään suomalaiseen pihapiiriin. Saunassa on kuusilauteet ja puukiuas vesisäiliöllä tai hormisäiliöllä. Rakennukseen mahtuu pukuhuone ja halutessasi terassi.",
        ],
        "list_h": "Vakiovarustelu",
        "list": ["Hirsirunko 45–70 mm", "Lankkulattia, saunassa viemäröinti", "Kuusilauteet ja kuusipanelointi katossa",
                 "Villat + tinapaperi yläpohjassa", "Avattavat ikkunat, saunassa lasiovi", "Puukiuas vesi- tai hormisäiliöllä + piippu",
                 "Palosuojalevyt kiukaan takana ja alla", "Palahuopakate"],
        "models_h": "Saunamallit",
        "models": [
            ("Pihasauna Tuomas 10", "Kompakti hirsisauna kotipihaan tai mökille. Valmistetaan asiakkaan mittojen mukaan.",
             ["Hirsirunko 58 mm", "Pukuhuone ja löylyhuone", "Kiuas vesisäiliöllä tai hormisäiliöllä"], None,
             ["pihasauna-1", "pihasauna-2", "pihasauna-3", "pihasauna-4"]),
            ("Pihasauna Tuomas 15", "Katettu kuisti ja tilava pukuhuone. Saatavana avaimet käteen tai runkotoimituksena.",
             ["Hirsirunko 58 mm", "Katettu kuisti", "Kiuas vesisäiliöllä tai hormisäiliöllä"], 5600,
             ["pihasauna-kuisti", "pihasauna-terassi", "sauna-pukuhuone", "sauna-lauteet"]),
            ("Pihasauna Tuomas 20", "Suurin malli: terassi kaiteineen ja tilaa usealle saunojalle.",
             ["Hirsirunko 45–70 mm", "Terassi kaiteineen", "Kiuas vesisäiliöllä tai hormisäiliöllä"], 5800,
             ["pihasauna-talvi-1", "pihasauna-talvi-2", "sauna-kiuas", "sauna-lasiovi"]),
        ],
        "band": ("pihasauna-talvi-ai", "Löylyt ympäri vuoden", "Kesällä terassilla vilvoitellen, talvella hankeen hyppien."),
        "faq": [
            ("Mitä eroa on avaimet käteen -toimituksella ja runkotoimituksella?", "Avaimet käteen -toimituksessa pystytämme saunan valmiiksi paikalleen. Runkotoimituksessa saat saunan rungon ja osat itse koottavaksi tai oman rakentajasi koottavaksi. Toimitustapa sovitaan tarjouksessa."),
            ("Minkä vahvuisesta hirrestä sauna tehdään?", "Pääsääntöisesti 70 × 150 mm, 58 mm tai 45 × 150 mm höylähirrestä. Paksumpi hirsi sopii erityisesti ympärivuotiseen käyttöön – kerro käyttötarkoitus, niin suosittelemme sopivan."),
            ("Voiko saunan koon ja pohjan päättää itse?", "Kyllä. Teemme saunat aina mittatilaustyönä, joten koko, ikkunat, terassi ja pukuhuoneen koko sovitaan toiveidesi mukaan."),
            ("Mihin saunoja toimitetaan?", "Toimitamme pihasaunat koko Suomeen Kauhavan seudulta. Pystytys onnistuu noin 200 km säteellä Kortesjärveltä; kauemmas kysy runkotoimitusta."),
            ("Tarvitaanko pihasaunalle rakennuslupa?", "Lupakäytäntö riippuu kunnasta ja rakennuksen koosta. Tarkista oman kuntasi rakennusvalvonnasta ennen tilausta – tarvittaessa saat meiltä rakennuksen mitat ja kuvat lupaa varten."),
        ],
    },
    "pihavarasto": {
        "name": "Pihavarastot ja puuvajat", "card": "Pihavarasto", "short": "Varastot ja puuladot hirrestä tai paneelista.",
        "title": "Pihavarasto ja puuvaja hirrestä mittojen mukaan | Jääkärihirsi",
        "desc": "Pihavarastot 45 × 150 höylähirrestä tai ulkovuoripaneelista ja puuladot kevythirrestä asiakkaan mitoilla. Valmiiksi pystytettynä. Puulato alk. 1 400 €, pihavarasto alk. 1 890 €.",
        "h1": "Pihavarastot ja <em>puuvajat</em>",
        "lead": "Hirsi- ja puurakenteiset varastot ja puuladot mittatilauksena – valmiiksi pystytettynä, jotta pääset käyttämään niitä heti.",
        "intro_h": "Tilaa tavaroille ja <em>polttopuille</em>",
        "intro": [
            "Valmistamme pihavarastot 45 × 150 höylähirrestä tai ulkovuoripaneelista asiakkaan mitoilla. Puuladot tehdään hienosahatusta kevythirrestä joko rakoseinällä polttopuiden kuivumista varten tai umpiseinällä.",
            "Toimitamme valmiin työn kotiisi asti ja halutessasi valmiiksi pystytettynä.",
        ],
        "list_h": "Valinnat",
        "list": ["Runko 45 mm hirsi tai ulkovuoripaneeli", "Puuladossa 50 × 125 mm seinä 15 mm raolla tai umpinainen",
                 "Lautalattia", "Palahuopa- tai peltikate", "Mitat asiakkaan mukaan"],
        "models_h": "Mallit",
        "models": [
            ("Pihavarasto", "Hirsinen pihavarasto asiakkaan mitoilla. Kuvan varasto on 4 200 × 2 100 mm.",
             ["Runko 45 mm hirsi", "Lautalattia", "Ovi 8 × 19", "Palahuopakate"], 1890,
             ["pihavarasto-1", "pihavarasto-2", "pihavarasto-3", "pihavarasto-4", "pihavarasto-5", "pihavarasto-6"]),
            ("Puulato", "Puuvaja polttopuille. Vakiokoko 2 × 3 m, myös asiakkaan mitoilla.",
             ["Runko 50 × 125 mm lankku", "Lattia 22 × 100 mm lauta", "Musta peltikate"], 1400,
             ["puulato-1", "puulato-2", "puulato-3", "puulato-runko"]),
        ],
        "faq": [
            ("Tarvitaanko pihavarastolle lupa?", "Pienet talousrakennukset ovat monessa kunnassa luvanvaraisia vain tietyn koon ylittäessä, mutta rajat vaihtelevat. Tarkista oman kuntasi rakennusvalvonnasta."),
            ("Millä perustuksella varasto pystytetään?", "Kuvissa varastot seisovat betoniharkkojen tai -anturoiden päällä. Perustustapa sovitaan tontin mukaan tarjousvaiheessa."),
            ("Voiko puuladon tehdä umpiseinällä?", "Kyllä. Seinä tehdään joko 15 mm raolla, jolloin polttopuut tuulettuvat, tai umpinaisena."),
        ],
    },
    "huvimaja": {
        "name": "Huvimajat", "card": "Huvimaja", "short": "Kuusi- tai kahdeksankulmaiset huvimajat.",
        "title": "Huvimaja hirrestä tai paneelista – 6- ja 8-kulmainen | Jääkärihirsi",
        "desc": "Kuusi- tai kahdeksankulmaiset huvimajat paneeli- tai hirsiversiona, kaari- tai neliöikkunoin. Toimitus avaimet käteen, lisävarusteena grilli-huuvapaketti. Alk. 2 100 €.",
        "h1": "<em>Huvimajat</em> pihaan ja mökille",
        "lead": "Kuusi- tai kahdeksankulmainen huvimaja paneeli- tai hirsiversiona. Toimitamme majat avaimet käteen -toimituksena.",
        "intro_h": "Kesäillan <em>kokoontumispaikka</em>",
        "intro": [
            "Huvimajoja on saatavana paneeli- tai hirsiversiona. Ikkunavaihtoehdot ovat kaari tai neliö. Maja on saatavana kuusi- tai kahdeksankulmaisena ainoastaan avaimet käteen -toimituksena.",
            "Lisävarusteena saat grilli-huuvapaketin, jolloin majasta tulee grillikatos sateen varalle.",
        ],
        "list_h": "Elementtivalmis huvimaja sisältää",
        "list": ["Lattia: 2 elementtiä, kyllästetty 28 × 95 mm tai 28 × 95 mm lattialankku", "Seinät: 8 elementtiä ikkunoilla tai ilman",
                 "Katto: 8 elementtiä + palahuopakate", "Ovi 1 kpl", "Lisävaruste: grilli-huuvapaketti"],
        "models_h": "Toteutuksia",
        "models": [
            ("Huvimaja", "Kahdeksankulmainen huvimaja kaari-ikkunoin. Paneeli- tai hirsiversiona, maalattuna tai puunvärisenä.",
             ["6- tai 8-kulmainen", "Kaari- tai neliöikkunat", "Avaimet käteen -toimitus"], 2100,
             ["huvimaja-1", "huvimaja-2", "huvimaja-3", "huvimaja-4", "huvimaja-5", "huvimaja-6", "huvimaja-7"]),
        ],
        "faq": [
            ("Voiko huvimajan saada runkotoimituksena?", "Ei – huvimajat toimitetaan ainoastaan avaimet käteen -toimituksena."),
            ("Saako huvimajaan grillin?", "Kyllä, lisävarusteena on grilli-huuvapaketti."),
            ("Voiko huvimajan maalata?", "Kyllä. Kuvissa on sekä puunvärisiä että maalattuja majoja – väri sovitaan tilatessa."),
        ],
    },
    "leikkimokki": {
        "name": "Leikkimökit ja hiekkalaatikot", "card": "Leikkimökki", "short": "Leikkimökit ja hiekkalaatikot lapsille.",
        "title": "Leikkimökki hirrestä tai paneelista mittojen mukaan | Jääkärihirsi",
        "desc": "Leikkimökit 45 mm hirrestä tai paneelielementeistä, vakiomitta 2 500 × 1 800 mm tai omilla mitoilla. Myös hiekkalaatikot kotimaisesta kestopuusta. Leikkimökki alk. 950 €, hiekkalaatikko alk. 145 €.",
        "h1": "Leikkimökit ja <em>hiekkalaatikot</em>",
        "lead": "Hirsi- tai paneelirunkoiset leikkimökit vakiomitoilla tai omien mittojesi mukaan – sekä hiekkalaatikot perheen pienimmille.",
        "intro_h": "Oma mökki <em>lapsille</em>",
        "intro": [
            "Valmistamme leikkimökit hirrestä ja paneelista asiakkaan mittojen mukaan. Myös vakiomitta löytyy, esimerkiksi 2 500 × 1 800 mm.",
            "Mökin saa puunvärisenä tai maalattuna – kuvissa perinteinen punamulta valkoisin listoin ja kuistikaitein.",
        ],
        "list_h": "Leikkimökki sisältää",
        "list": ["45 mm hirsirunko tai paneelielementtirunko", "Ikkunat muovilevyä", "Lautalattia + muovimatto", "Palahuopakate"],
        "models_h": "Mallit",
        "models": [
            ("Leikkimökki", "Hirsi- tai paneelirunkoinen leikkimökki, esimerkiksi 2 500 × 1 800 mm. Kuistilla tai ilman.",
             ["45 mm hirsi tai paneeli", "Muovilevyikkunat", "Lautalattia + muovimatto"], 950,
             ["leikkimokki-1", "leikkimokki-4", "leikkimokki-2", "leikkimokki-3", "leikkimokki-5", "leikkimokki-6", "leikkimokki-7"]),
            ("Hiekkalaatikko", "Kulmikas tai neliön mallinen hiekkalaatikko kotimaisesta kestopuusta, myös asiakkaan mitoilla.",
             ["Kuusi- tai nelikulmainen", "Kotimainen kestopuu", "Mitat toiveen mukaan"], 145,
             ["hiekkalaatikko"]),
        ],
        "faq": [
            ("Miksi ikkunat ovat muovilevyä?", "Muovilevy on lasia turvallisempi lasten leikeissä eikä särky."),
            ("Voiko leikkimökin maalata valmiiksi?", "Kyllä, väri sovitaan tilatessa. Mökin saa myös puunvärisenä."),
        ],
    },
    "wc": {
        "name": "Ulko-WC:t", "card": "Ulko-WC", "short": "Ulkovessat hirrestä tai paneelista.",
        "title": "Ulko-WC ja ulkohuussi hirrestä – kompostoiva käymälä | Jääkärihirsi",
        "desc": "Ulkovessat 45 × 150 hirrestä tai 22 × 120 ulkovuoripaneelista. Euromakki HD -käymäläelementti tai muiden valmistajien laitteisiin sopiva rakennus. Alk. 880 €.",
        "h1": "Ulko-WC:t <em>mökille</em> ja pihaan",
        "lead": "Ulkovessat hirrestä tai ulkovuoripaneelista – valmiina käymäläelementin kanssa tai sopimaan valitsemaasi laitteeseen.",
        "intro_h": "Siisti ja toimiva <em>ulkohuussi</em>",
        "intro": [
            "Valmistamme ulkovessat 45 × 150 hirrestä tai 22 × 120 paneelista. Käytämme Euromakki HD -muovisekoitteesta valmistettua käymäläelementtiä.",
            "Teemme myös muiden valmistajien elementteihin soveltuvia WC-rakennuksia hirrestä tai ulkovuoripaneelista sopimuksen mukaisesti.",
        ],
        "list_h": "Valinnat",
        "list": ["Runko 45 × 150 hirsi tai 22 × 120 paneeli", "Euromakki HD -käymäläelementti", "Sopii myös muiden ekokäymälävalmistajien laitteisiin", "Palahuopakate"],
        "models_h": "Toteutuksia",
        "models": [
            ("Ulko-WC", "Hirsinen ulkovessa käymäläelementillä. Huoltoluukku takana, istuin ja kansi valmiina.",
             ["45 × 150 hirsi tai paneeli", "Euromakki HD -elementti", "Huoltoluukku"], 880,
             ["wc-4", "wc-5", "wc-1", "wc-2", "wc-3", "wc-6", "wc-7", "wc-8"]),
        ],
        "faq": [
            ("Mihin käymälälaitteisiin rakennus sopii?", "Vakiona käytämme Euromakki HD -elementtiä. Teemme rakennuksen myös muiden valmistajien laitteisiin sopivaksi – kerro valitsemasi laite."),
            ("Voiko ulko-WC:n saada paneelista?", "Kyllä, 22 × 120 ulkovuoripaneelista tai 45 × 150 hirrestä."),
        ],
    },
    "roskakatos": {
        "name": "Roskakatokset", "card": "Roskakatos", "short": "Katokset yhdelle tai useammalle astialle.",
        "title": "Roskakatos puusta – yhdelle tai useammalle jäteastialle | Jääkärihirsi",
        "desc": "Roskalaatikkokatokset yhdelle tai useammalle jäteastialle, ovellisena tai ilman. Toimitetaan myös maalattuna. Alk. 600 €.",
        "h1": "<em>Roskakatokset</em> kotipihaan",
        "lead": "Siisti katos yhdelle tai useammalle jäteastialle – ovellisena tai ilman, puunvärisenä tai maalattuna.",
        "intro_h": "Tuo pihapiiriin <em>ryhtiä</em>",
        "intro": [
            "Roskalaatikkokatos on paitsi kätevä myös siisti ja tuo pihapiiriin ryhtiä. Valmistamme katokset niin yhdelle kuin useammallekin laatikolle, ovellisena tai ilman ovea.",
            "Toimitamme katoksia myös maalattuna – esimerkiksi talon värityksen mukaan.",
        ],
        "list_h": "Valinnat",
        "list": ["1–4 jäteastialle", "Ovellinen tai avoin", "Puunvärinen tai maalattu", "Koristeelliset räystäslaudat"],
        "models_h": "Toteutuksia",
        "models": [
            ("Roskakatos", "Katos jäteastioille ristikkoseinin ja koristeräystäin. Mitoitetaan astioiden määrän mukaan.",
             ["1–4 astialle", "Ovellinen tai avoin", "Maalattuna"], 600,
             ["roskakatos-3", "roskakatos-1", "roskakatos-2"]),
        ],
        "faq": [
            ("Mihin kokoisille astioille katos sopii?", "Katos mitoitetaan astioidesi mukaan. Kerro tarjouspyynnössä astioiden määrä ja koko (esim. 240 l tai 660 l)."),
        ],
    },
    "kalusteet": {
        "name": "Pihakalusteet ja keinut", "card": "Kalusteet ja keinut", "short": "Pihakeinut ja hirsiset puutarhakalusteet.",
        "title": "Hirsikalusteet ja pihakeinut – puutarhakalusteet hirrestä | Jääkärihirsi",
        "desc": "Pihakeinut lapsille ja aikuisille sekä puutarhakalusteet 70 × 150 höylähirrestä Kortesjärveltä. Värillisinä tai ilman, mittatilauksena. Lasten keinu alk. 580 €.",
        "h1": "Pihakalusteet ja <em>keinut</em>",
        "lead": "Aikaa ja säätä kestävät pihakeinut ja hirsiset puutarhakalusteet kotimaisesta puusta – valmiiksi koottuina.",
        "intro_h": "Kalusteet, jotka <em>kestävät</em>",
        "intro": [
            "Valmistamme aikaa ja säätä kestävät hirsikalusteet Kortesjärvellä. Kaikki tuotteemme valmistetaan kotimaisista raaka-aineista, joko puusta tai hirrestä.",
            "Valikoimasta löydät pihakeinuja lapsille sekä puutarhakalusteita. Valmistamme pyynnöstä pihakeinuja myös aikuisille mitoitettuina.",
        ],
        "list_h": "Hyvä tietää",
        "list": ["Kalusteet 70 × 150 höylähirrestä", "Keinut kotimaisesta kestopuusta", "Värillisinä tai ilman väriä", "Valmiiksi koottuina", "Mitat toiveen mukaan"],
        "models_h": "Tuotteet",
        "models": [
            ("Lasten keinu", "Hauska ja käytännöllinen yksityiskohta kodin tai kesämökin pihamaalle. Keinuun on saatavana myös katto, ja sen voi toimittaa aikuisten mallina.",
             ["Kotimainen kestopuu", "Katto lisävarusteena", "Myös aikuisten malli"], 580,
             ["keinu-1", "keinu-2", "keinu-3"]),
            ("Puutarhakalusteet hirrestä", "Pöytäryhmät ja penkit pihapiiriin ja terassille. Hyvin hoidettuina ne kestävät aikaa ja säätä vuosikausia.",
             ["70 × 150 höylähirsi", "Värillisenä tai ilman", "Mittatilauksena"], None,
             ["kalusteet-4", "kalusteet-1", "kalusteet-2", "kalusteet-3"]),
        ],
        "faq": [
            ("Miten hirsikalusteita hoidetaan?", "Kun hoidat hirsikalusteitasi hyvin, kestävät ne aikaa sekä säätä vuosikausia. Puunsuoja-aineen uusiminen muutaman vuoden välein pitää pinnan kunnossa."),
            ("Toimitatteko kalusteita kauemmas?", "Kyllä – pientavarat toimitamme kuljetuksineen koko Suomeen."),
        ],
    },
    "koristeet": {
        "name": "Pihakoristeet", "card": "Pihakoristeet", "short": "Maitolaiturit, koristekaivot ja postilaatikkotelineet.",
        "title": "Maitolaituri, koristekaivo ja postilaatikkoteline puusta | Jääkärihirsi",
        "desc": "Pihakoristeet mittatilaustyönä Kortesjärveltä: maitolaiturit (alk. 650 €), koristekaivot 80–100 cm kaivonrenkaalle (alk. 585 €) ja postilaatikkotelineet (alk. 180 €), valmiiksi maalattuina.",
        "h1": "Maitolaiturit ja <em>pihakoristeet</em>",
        "lead": "Maitolaiturit, koristekaivot ja postilaatikkotelineet mittatilaustyönä kotimaisesta puusta – valmiiksi koottuina ja maalattuina.",
        "intro_h": "Pala suomalaista <em>pihaperinnettä</em>",
        "intro": [
            "Haaveiletko tunnelmallisesta maitolaiturista tai koristekaivosta? Kaipaako naapurustosi siistiä postilaatikkotelinettä? Valmistamme pihakoristeet toiveittesi mukaan pääasiassa kotimaisista raaka-aineista.",
            "Saat ratkaisut valmiiksi pystytettyinä – nopeasti, luotettavasti ja kestävästi.",
        ],
        "list_h": "Hyvä tietää",
        "list": ["Valmiiksi koottuina ja maalattuina", "Värin voi valita", "Kotimaisesta puusta", "Pientavarat kuljetuksineen koko Suomeen"],
        "models_h": "Tuotteet",
        "models": [
            ("Maitolaituri", "Vanhan ajan maitolaiturit ovat pala suomalaista identiteettiä. Valmistamme ne käsityönä paneelista aidon näköisinä. Kuvassa puuvalmis koristelaituri palahuopakatteella.",
             ["Paneelista käsityönä", "Palahuopakate", "Mitat toiveen mukaan"], 650,
             ["maitolaituri"]),
            ("Koristekaivo", "Koristekaivolla piristät pihan yleisilmettä. Kaivot valmistetaan sopiviksi 80–100 cm kaivonrenkaan päälle, valmiiksi koottuina ja maalattuina.",
             ["80–100 cm renkaalle", "Valmiiksi koottu", "Maalattu"], 585,
             ["koristekaivo-3", "koristekaivo-1", "koristekaivo-2"]),
            ("Postilaatikkoteline", "Postilaatikkoteline elävöittää talon julkisivua. Telineet saat valmiiksi maalattuna haluamallasi värillä. Laatikot ja jalustat kuuluvat toimitukseen.",
             ["Laatikot ja jalustat mukana", "Maalattu valitsemallasi värillä"], 180,
             ["postilaatikkoteline"]),
        ],
        "faq": [
            ("Kuuluvatko postilaatikot telineen toimitukseen?", "Kyllä, laatikot ja jalustat kuuluvat toimitukseen."),
            ("Minkä kokoiselle kaivonrenkaalle koristekaivo sopii?", "Kaivot valmistetaan sopiviksi 80–100 cm kaivonrenkaan päälle."),
        ],
    },
}
T["fi"]["P"] = P_FI

T["fi"]["hub"] = {
    "title": "Piharakennukset mittatilauksena – varastot, huvimajat, leikkimökit, ulko-WC | Jääkärihirsi",
    "desc": "Hirsi- ja puurakenteiset piharakennukset Kortesjärveltä: pihavarastot, puuladot, huvimajat, leikkimökit, ulko-WC:t ja roskakatokset mittatilauksena, valmiiksi pystytettyinä.",
    "h1": "Piharakennukset <em>mittatilauksena</em>",
    "lead": "Hirsi- tai puurakenteiset piharakennukset kodin ja kesämökin pihapiiriin. Toimitamme valmiin työn perille kannettuna ja halutessasi valmiiksi pystytettynä.",
}

T["fi"]["company"] = {
    "title": "Jääkärihirsi Oy – hirsirakentaja Kortesjärvellä, Kauhava",
    "desc": "Jääkärihirsi Oy on piharakennusten, hirsikalusteiden ja pihakoristeiden valmistaja Kauhavan Kortesjärvellä. Kotimainen höylähirsi, mittatilaus, pystytys noin 200 km säteellä.",
    "h1": "Hirsirakentaja <em>Kortesjärveltä</em>",
    "lead": "Jääkärihirsi Oy on piharakennusten, -kalusteiden ja -koristeiden hirsirakentaja Kauhavan Kortesjärvellä.",
    "p": [
        "Olemme erikoistuneet laadukkaiden hirsi- ja puurakennusten valmistamiseen. Teemme kotimaisena laatutyönä, asiakkaan toiveiden mukaan niin pihasaunat, pihavarastot kuin hirsikalusteet ja -koristeet.",
        "Tiedämme, miten rakennetaan hengittävä ja kestävä hirsirakennus, joka palvelee käyttäjäänsä sukupolvelta toiselle. Käytämme aina kotimaisia raaka-aineita, jotka kestävät suomalaisen sään vaihtelut vuodesta toiseen.",
        "Tilaamalla piharakennuksen, hiekkalaatikon tai vaikkapa saunan mökillesi Jääkärihirreltä tuet aitoa kotimaista työtä.",
    ],
    "mat_h": "Materiaalit",
    "mat": [("Höylähirsi 70 × 150 mm", "Saunat ja hirsikalusteet"), ("Höylähirsi 58 mm", "Pihasaunat"),
            ("Höylähirsi 45 × 150 mm", "Saunat, varastot, leikkimökit, ulko-WC:t"), ("Kevythirsi 50 × 125 mm", "Puuladot"),
            ("Ulkovuoripaneeli 22 × 120 mm", "Varastot, huvimajat, leikkimökit, ulko-WC:t"), ("Kotimainen kestopuu", "Keinut ja hiekkalaatikot")],
    "deliv_h": "Toimitustavat",
    "deliv": [("Avaimet käteen", "Pystytämme rakennuksen valmiiksi paikalleen noin 200 km säteellä Kortesjärveltä."),
              ("Runkotoimitus", "Saat rungon ja osat itse koottavaksi – sopii myös kauemmas."),
              ("Pientavarat rahtina", "Keinut, kalusteet ja pihakoristeet kuljetuksineen koko Suomeen.")],
}

T["fi"]["quote"] = {
    "title": "Tarjouspyyntö – suunnittele pihasauna tai piharakennus | Jääkärihirsi",
    "desc": "Valitse tuote, mitat ja varustelu – näet pohjakuvan ja pinta-alan heti. Lähetä tarjouspyyntö Jääkärihirrelle Kortesjärvelle.",
    "h1": "Suunnittele ja <em>pyydä tarjous</em>",
    "lead": "Valitse tuote ja mitat – näet pohjakuvan ja pinta-alan heti. Tarkennetaan yksityiskohdat yhdessä ennen tarjousta.",
    "s1": "Mitä olet tilaamassa?", "s2": "Mitat ja varustelu", "s3": "Toimitus", "s4": "Yhteystiedot",
    "width": "Leveys (m)", "length": "Pituus (m)", "diam": "Halkaisija (m)", "frame": "Runko", "roof": "Katto", "extras": "Lisävalinnat",
    "model": "Malli", "delivery": "Toimitustapa", "town": "Toimituspaikkakunta", "town_ph": "Esim. Lapua",
    "when": "Aikataulu", "when_ph": "Esim. kesäkuu 2027", "more": "Lisätietoja", "more_ph": "Esim. ikkunoiden paikat, väri, tontin kulkuyhteys",
    "send": "Lähetä tarjouspyyntö", "summary": "Yhteenveto", "area": "Pinta-ala", "inner": "Rakennus",
    "terrace": "Terassi", "porch": "Kuisti", "steam": "Löylyhuone", "dress": "Pukuhuone",
    "qty": "Määrä (kpl)", "bins": "Jäteastioita", "price_note": "Alkaen-hinta on suuntaa antava. Lopullinen hinta tarjouksella.",
    "plan_note": "Pohjakuva on havainnollistava.",
    "items": {
        "kalusteet": ["Lasten keinu", "Aikuisten keinu", "Keinu katolla", "Pöytäryhmä hirrestä", "Penkki hirrestä"],
        "koristeet": ["Maitolaituri", "Koristekaivo", "Postilaatikkoteline"],
        "leikkimokki_x": "Hiekkalaatikko lisäksi",
    },
    "frames": ["Höylähirsi 45 mm", "Höylähirsi 58 mm", "Höylähirsi 70 mm", "Ulkovuoripaneeli"],
    "roofs": ["Palahuopa", "Peltikate"],
    "deliveries": ["Avaimet käteen (pystytys)", "Runkotoimitus", "Nouto Kortesjärveltä"],
    "extras_by": {
        "pihasauna": ["Terassi", "Katettu kuisti", "Kiuas vesisäiliöllä", "Kiuas hormisäiliöllä", "Lasiovi saunaan"],
        "pihavarasto": ["Rakoseinä (puulato)", "Pariovet", "Ikkuna"],
        "huvimaja": ["Kaari-ikkunat", "Neliöikkunat", "Grilli-huuvapaketti", "Maalattu"],
        "leikkimokki": ["Kuisti", "Maalattu (punamulta + valkoiset listat)", "Hiekkalaatikko"],
        "wc": ["Euromakki HD -elementti", "Oma käymälälaite"],
        "roskakatos": ["Ovet", "Maalattu"],
        "kalusteet": ["Maalattu / petsattu", "Katto keinuun"],
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
        "demo": "Webbplatsförslag – Äijä Group. Detta är en förhandsversion.", "open_map": "Öppna kartan", "mobile_quote": "Offert",
        "made_in": "Tillverkat i Kortesjärvi av inhemskt timmer.",
    },
    "home_title": "Gårdsbastur och gårdsbyggnader av timmer – Kortesjärvi | Jääkärihirsi",
    "home_desc": "Jääkärihirsi Oy tillverkar gårdsbastur, förråd, lusthus, lekstugor, utedass och timmermöbler enligt måttbeställning av inhemskt planhyvlat timmer i Kortesjärvi. Nyckelfärdigt eller som stomleverans.",
    "hero_h1": "Gårdsbastur och gårdsbyggnader <em>av timmer</em>",
    "hero_lead": "Vi tillverkar bastur, förråd, lusthus och lekstugor av inhemskt planhyvlat timmer i Kortesjärvi enligt dina mått – nyckelfärdigt eller som stomleverans.",
    "hero_cta": "Planera och be om offert",
    "products_h": "Vad <em>behöver du?</em>",
    "products_p": "Alla produkter tillverkas enligt måttbeställning. Priserna inkluderar moms.",
    "why_h": "Timringsföretag <em>från Kortesjärvi</em>",
    "why": [
        ("Inhemskt planhyvlat timmer", "Stommar av 45, 58 eller 70 mm planhyvlat timmer eller ytterpanel. Råvarorna är inhemska."),
        ("Enligt dina mått", "Standardmodellerna är en utgångspunkt – storlek, fönster, terrass och takmaterial enligt dina önskemål."),
        ("Nyckelfärdigt eller som stomme", "Vi reser byggnaden färdig inom cirka 200 km från Kortesjärvi. Mindre produkter levererar vi till hela Finland."),
    ],
    "map_label": "Montering inom cirka 200 km",
    "map_note": "Mindre produkter med transport till hela Finland.",
    "steps_h": "Så går <em>beställningen till</em>",
    "steps": [
        ("Berätta om dina önskemål", "Välj produkt och mått i offertförfrågan eller ring – bilder och skisser hjälper."),
        ("Offert och avtal", "Du får en offert där stomme, utrustning och leveranssätt är specificerade."),
        ("Tillverkning i Kortesjärvi", "Byggnaden tillverkas i vår egen hall och transporteras till platsen."),
        ("Montering eller stomleverans", "Vi reser byggnaden färdig eller levererar stommen för egen montering enligt avtal."),
    ],
    "contact_h": "Be om <em>offert</em>",
    "contact_p": "Ring eller skicka ett meddelande – vi svarar så snabbt som möjligt. Berätta produkt, ungefärliga mått och leveransort.",
    "form": {
        "send": "Skicka meddelande", "name": "Namn *", "phone": "Telefon", "email": "E-post", "town": "Ort",
        "msg": "Meddelande", "product": "Produkt", "choose": "Välj produkt", "other": "Annat / vet inte ännu",
        "consent": 'Jag godkänner behandlingen av mina uppgifter enligt <a class="link" href="/sv/dataskydd/">dataskyddsbeskrivningen</a>.',
        "err": "Fyll i namn och telefon eller e-post.", "senderr": "Det gick inte att skicka. Ring 045 119 7289 eller försök igen.",
        "title": "Skicka meddelande",
    },
}

P_SV = {
    "pihasauna": {
        "name": "Gårdsbastur", "card": "Gårdsbastu", "short": "Timmerbastur för gården och stugan enligt mått.",
        "title": "Gårdsbastu av timmer enligt måttbeställning – nyckelfärdig | Jääkärihirsi, Kortesjärvi",
        "desc": "Gårdsbastur av inhemskt planhyvlat timmer (45, 58 eller 70 mm) enligt dina mått. Vedeldat aggregat, granlavar, omklädningsrum och terrass. Nyckelfärdigt eller som stomleverans.",
        "h1": "Gårdsbastur <em>av timmer</em>",
        "lead": "Timmerbastu till gården eller stugan enligt dina mått – färdigt uppförd enligt nycklar-i-hand-konceptet eller som stomleverans.",
        "intro_h": "En bastu som består <em>i generationer</em>", "intro_img": "sauna-sisa-ai",
        "intro": [
            "Gårdsbastur av timmer hör till våra populäraste produkter. Vi tillverkar basturna i Kortesjärvi enligt kundens mått, huvudsakligen av planhyvlat timmer i måtten 70 × 150 mm, 58 mm eller 45 × 150 mm.",
            "Planhyvlat timmer är ett hållbart material som passar fint in i den finska gårdsmiljön. I bastun finns granlavar och ett vedeldat aggregat med vattenbehållare eller rörbehållare. I byggnaden ryms ett omklädningsrum och vid önskemål en terrass.",
        ],
        "list_h": "Standardutrustning",
        "list": ["Timmerstomme 45–70 mm", "Brädgolv, avlopp i bastun", "Granlavar och granpanel i taket",
                 "Ull + aluminiumfolie i mellantaket", "Fönster som går att öppna, glasdörr till bastun", "Vedeldat aggregat med vatten- eller rörbehållare + skorsten",
                 "Skyddsplåt bakom och under aggregatet", "Takpapp"],
        "models_h": "Bastumodeller",
        "models": [
            ("Gårdsbastu Tuomas 10", "Kompakt timmerbastu för hemmet eller stugan. Tillverkas enligt kundens mått.",
             ["Timmerstomme 58 mm", "Omklädningsrum och bastu", "Aggregat med vatten- eller rörbehållare"], None,
             ["pihasauna-1", "pihasauna-2", "pihasauna-3", "pihasauna-4"]),
            ("Gårdsbastu Tuomas 15", "Täckt veranda och rymligt omklädningsrum. Nyckelfärdigt eller som stomleverans.",
             ["Timmerstomme 58 mm", "Täckt veranda", "Aggregat med vatten- eller rörbehållare"], 5600,
             ["pihasauna-kuisti", "pihasauna-terassi", "sauna-pukuhuone", "sauna-lauteet"]),
            ("Gårdsbastu Tuomas 20", "Den största modellen: terrass med räcke och plats för flera bastubadare.",
             ["Timmerstomme 45–70 mm", "Terrass med räcke", "Aggregat med vatten- eller rörbehållare"], 5800,
             ["pihasauna-talvi-1", "pihasauna-talvi-2", "sauna-kiuas", "sauna-lasiovi"]),
        ],
        "band": ("pihasauna-talvi-ai", "Bastubad året om", "På sommaren svalkande på terrassen, på vintern ett dopp i snön."),
        "faq": [
            ("Vad är skillnaden mellan nyckelfärdig leverans och stomleverans?", "Vid nyckelfärdig leverans reser vi bastun färdig på plats. Vid stomleverans får du stommen och delarna för egen montering eller för din egen byggare. Leveranssättet avtalas i offerten."),
            ("Av hur tjockt timmer tillverkas bastun?", "Huvudsakligen av 70 × 150 mm, 58 mm eller 45 × 150 mm planhyvlat timmer. Tjockare timmer passar särskilt för året runt-bruk – berätta hur bastun ska användas så rekommenderar vi rätt."),
            ("Kan jag själv bestämma storlek och planlösning?", "Ja. Vi tillverkar alltid basturna enligt måttbeställning, så storlek, fönster, terrass och omklädningsrummets storlek avtalas enligt dina önskemål."),
            ("Vart levererar ni bastur?", "Vi levererar gårdsbastur till hela Finland från Kauhava-regionen. Montering inom cirka 200 km från Kortesjärvi; längre bort rekommenderar vi stomleverans."),
            ("Behövs bygglov för en gårdsbastu?", "Det beror på kommunen och byggnadens storlek. Kontrollera med byggnadstillsynen i din kommun före beställning – vid behov får du mått och bilder av oss för ansökan."),
        ],
    },
    "pihavarasto": {
        "name": "Gårdsförråd och vedbodar", "card": "Gårdsförråd", "short": "Förråd och vedlador av timmer eller panel.",
        "title": "Gårdsförråd och vedbod av timmer enligt mått | Jääkärihirsi",
        "desc": "Gårdsförråd av 45 × 150 planhyvlat timmer eller ytterpanel och vedlador av lätt timmer enligt kundens mått. Färdigt uppförda. Vedlada från 1 400 €, förråd från 1 890 €.",
        "h1": "Gårdsförråd och <em>vedbodar</em>",
        "lead": "Förråd och vedlador av timmer eller trä enligt måttbeställning – färdigt uppförda så att du kan använda dem direkt.",
        "intro_h": "Plats för saker <em>och ved</em>",
        "intro": [
            "Vi tillverkar förråd av 45 × 150 planhyvlat timmer eller ytterpanel enligt kundens mått. Vedladorna tillverkas av finsågat lätt timmer, antingen med springa så att veden torkar eller med täta väggar.",
            "Vi levererar det färdiga arbetet hem till dig och vid önskemål färdigt uppfört.",
        ],
        "list_h": "Alternativ",
        "list": ["Stomme 45 mm timmer eller ytterpanel", "Vedlada: vägg 50 × 125 mm med 15 mm springa eller tät",
                 "Brädgolv", "Takpapp eller plåttak", "Mått enligt kunden"],
        "models_h": "Modeller",
        "models": [
            ("Gårdsförråd", "Förråd av timmer enligt kundens mått. Förrådet på bilden är 4 200 × 2 100 mm.",
             ["Stomme 45 mm timmer", "Brädgolv", "Dörr 8 × 19", "Takpapp"], 1890,
             ["pihavarasto-1", "pihavarasto-2", "pihavarasto-3", "pihavarasto-4", "pihavarasto-5", "pihavarasto-6"]),
            ("Vedlada", "Vedbod för brännved. Standardstorlek 2 × 3 m, även enligt kundens mått.",
             ["Stomme 50 × 125 mm planka", "Golv 22 × 100 mm bräda", "Svart plåttak"], 1400,
             ["puulato-1", "puulato-2", "puulato-3", "puulato-runko"]),
        ],
        "faq": [
            ("Behövs bygglov för ett förråd?", "Mindre ekonomibyggnader kräver i många kommuner lov först över en viss storlek, men gränserna varierar. Kontrollera med byggnadstillsynen i din kommun."),
            ("Vilken grund används?", "På bilderna står förråden på betongblock eller plintar. Grunden avtalas enligt tomten i offertskedet."),
            ("Kan vedladan byggas med täta väggar?", "Ja. Väggen görs antingen med 15 mm springa så att veden luftas, eller helt tät."),
        ],
    },
    "huvimaja": {
        "name": "Lusthus", "card": "Lusthus", "short": "Sex- eller åttkantiga lusthus.",
        "title": "Lusthus av timmer eller panel – sex- och åttkantigt | Jääkärihirsi",
        "desc": "Sex- eller åttkantiga lusthus av panel eller timmer, med båg- eller fyrkantsfönster. Nyckelfärdig leverans, som tillbehör grill- och ventilationspaket. Från 2 100 €.",
        "h1": "<em>Lusthus</em> för gården och stugan",
        "lead": "Sex- eller åttkantigt lusthus av panel eller timmer. Vi levererar lusthusen nyckelfärdiga.",
        "intro_h": "Samlingsplatsen <em>en sommarkväll</em>",
        "intro": [
            "Vi erbjuder lusthus av både panel och timmer. Fönsteralternativen är båge eller fyrkant. Lusthusen finns som sex- eller åttkantiga och levereras endast nyckelfärdiga.",
            "Som tillbehör erbjuds ett grill- och ventilationspaket, så att lusthuset fungerar som grillplats även när det regnar.",
        ],
        "list_h": "Det elementfärdiga lusthuset innehåller",
        "list": ["Golv: 2 element, impregnerat 28 × 95 mm eller 28 × 95 mm golvbräda", "Väggar: 8 element med eller utan fönster",
                 "Tak: 8 element + takpapp", "Dörr 1 st.", "Tillbehör: grill- och ventilationspaket"],
        "models_h": "Utföranden",
        "models": [
            ("Lusthus", "Åttkantigt lusthus med bågfönster. Av panel eller timmer, målat eller i träfärg.",
             ["Sex- eller åttkantigt", "Båg- eller fyrkantsfönster", "Nyckelfärdig leverans"], 2100,
             ["huvimaja-1", "huvimaja-2", "huvimaja-3", "huvimaja-4", "huvimaja-5", "huvimaja-6", "huvimaja-7"]),
        ],
        "faq": [
            ("Kan lusthuset levereras som stomme?", "Nej – lusthusen levereras endast nyckelfärdiga."),
            ("Kan man få grill i lusthuset?", "Ja, som tillbehör finns ett grill- och ventilationspaket."),
            ("Kan lusthuset målas?", "Ja. På bilderna finns både lusthus i träfärg och målade – färgen avtalas vid beställning."),
        ],
    },
    "leikkimokki": {
        "name": "Lekstugor och sandlådor", "card": "Lekstuga", "short": "Lekstugor och sandlådor för barn.",
        "title": "Lekstuga av timmer eller panel enligt mått | Jääkärihirsi",
        "desc": "Lekstugor av 45 mm timmer eller panelelement, standardmått 2 500 × 1 800 mm eller egna mått. Även sandlådor av inhemskt hållbart trä. Lekstuga från 950 €, sandlåda från 145 €.",
        "h1": "Lekstugor och <em>sandlådor</em>",
        "lead": "Lekstugor med timmer- eller panelstomme i standardmått eller enligt dina mått – och sandlådor för de minsta.",
        "intro_h": "En egen stuga <em>för barnen</em>",
        "intro": [
            "Vi tillverkar lekstugorna av timmer och panel enligt kundens mått. Vi erbjuder även standardmått, till exempel 2 500 × 1 800 mm.",
            "Stugan finns i träfärg eller målad – på bilderna traditionell rödmylla med vita lister och verandaräcken.",
        ],
        "list_h": "Lekstugan innehåller",
        "list": ["45 mm timmerstomme eller panelelementstomme", "Fönster av plastskiva", "Brädgolv + plastmatta", "Takpapp"],
        "models_h": "Modeller",
        "models": [
            ("Lekstuga", "Lekstuga med timmer- eller panelstomme, till exempel 2 500 × 1 800 mm. Med eller utan veranda.",
             ["45 mm timmer eller panel", "Fönster av plastskiva", "Brädgolv + plastmatta"], 950,
             ["leikkimokki-1", "leikkimokki-4", "leikkimokki-2", "leikkimokki-3", "leikkimokki-5", "leikkimokki-6", "leikkimokki-7"]),
            ("Sandlåda", "Flerkantig eller fyrkantig sandlåda av inhemskt hållbart trä, även enligt kundens mått.",
             ["Sex- eller fyrkantig", "Inhemskt hållbart trä", "Mått enligt önskemål"], 145,
             ["hiekkalaatikko"]),
        ],
        "faq": [
            ("Varför är fönstren av plastskiva?", "Plastskiva är säkrare än glas när barnen leker och går inte sönder."),
            ("Kan lekstugan levereras målad?", "Ja, färgen avtalas vid beställning. Stugan finns också i träfärg."),
        ],
    },
    "wc": {
        "name": "Utedass", "card": "Utedass", "short": "Utedass av timmer eller panel.",
        "title": "Utedass av timmer – komposterande toalett | Jääkärihirsi",
        "desc": "Utedass av 45 × 150 timmer eller 22 × 120 ytterpanel. Euromakki HD-toalettelement eller byggnad som passar andra tillverkares utrustning. Från 880 €.",
        "h1": "Utedass för <em>stugan</em> och gården",
        "lead": "Utedass av timmer eller ytterpanel – färdigt med toalettelement eller anpassat till den utrustning du valt.",
        "intro_h": "Ett snyggt och fungerande <em>utedass</em>",
        "intro": [
            "Vi tillverkar utedass av 45 × 150 timmer eller 22 × 120 panel. Vi använder dasselement tillverkat av Euromakki HD-plastblandning.",
            "Vi bygger även, enligt överenskommelse, dass som lämpar sig för andra tillverkares element, av timmer eller ytterpanel.",
        ],
        "list_h": "Alternativ",
        "list": ["Stomme 45 × 150 timmer eller 22 × 120 panel", "Euromakki HD-toalettelement", "Passar även andra tillverkares ekotoaletter", "Takpapp"],
        "models_h": "Utföranden",
        "models": [
            ("Utedass", "Utedass av timmer med toalettelement. Servicelucka på baksidan, sits och lock färdiga.",
             ["45 × 150 timmer eller panel", "Euromakki HD-element", "Servicelucka"], 880,
             ["wc-4", "wc-5", "wc-1", "wc-2", "wc-3", "wc-6", "wc-7", "wc-8"]),
        ],
        "faq": [
            ("Vilken toalettutrustning passar byggnaden?", "Som standard använder vi Euromakki HD-elementet. Vi anpassar också byggnaden till andra tillverkares utrustning – berätta vilken du valt."),
            ("Kan utedasset byggas av panel?", "Ja, av 22 × 120 ytterpanel eller 45 × 150 timmer."),
        ],
    },
    "roskakatos": {
        "name": "Sopskjul", "card": "Sopskjul", "short": "Skjul för en eller flera soptunnor.",
        "title": "Sopskjul av trä – för en eller flera soptunnor | Jääkärihirsi",
        "desc": "Sopskjul för en eller flera soptunnor, med eller utan dörr. Levereras även målade. Från 600 €.",
        "h1": "<em>Sopskjul</em> för gården",
        "lead": "Ett snyggt skjul för en eller flera soptunnor – med eller utan dörr, i träfärg eller målat.",
        "intro_h": "Ordning och reda <em>på gården</em>",
        "intro": [
            "Ett sopskjul är behändigt men även snyggt och berikar gårdsmiljön. Vi tillverkar skjulen för en eller flera soplådor, med eller utan dörr.",
            "Vi levererar även skjulen färdigt målade – till exempel i husets färger.",
        ],
        "list_h": "Alternativ",
        "list": ["För 1–4 soptunnor", "Med dörr eller öppet", "Träfärg eller målat", "Dekorativa takfotsbräder"],
        "models_h": "Utföranden",
        "models": [
            ("Sopskjul", "Skjul för soptunnor med spjälväggar och dekorativ takfot. Dimensioneras efter antalet tunnor.",
             ["För 1–4 tunnor", "Med dörr eller öppet", "Målat"], 600,
             ["roskakatos-3", "roskakatos-1", "roskakatos-2"]),
        ],
        "faq": [
            ("För hur stora kärl passar skjulet?", "Skjulet dimensioneras efter dina kärl. Berätta antal och storlek (t.ex. 240 l eller 660 l) i offertförfrågan."),
        ],
    },
    "kalusteet": {
        "name": "Gårdsmöbler och gungor", "card": "Möbler och gungor", "short": "Gårdsgungor och trädgårdsmöbler av timmer.",
        "title": "Timmermöbler och gårdsgungor – trädgårdsmöbler av timmer | Jääkärihirsi",
        "desc": "Gårdsgungor för barn och vuxna samt trädgårdsmöbler av 70 × 150 planhyvlat timmer från Kortesjärvi. Med eller utan färg, enligt måttbeställning. Barngunga från 580 €.",
        "h1": "Gårdsmöbler och <em>gungor</em>",
        "lead": "Gårdsgungor och trädgårdsmöbler av timmer som tål väder och vind – tillverkade av inhemskt trä och levererade färdigbyggda.",
        "intro_h": "Möbler som <em>håller</em>",
        "intro": [
            "I Kortesjärvi tillverkar vi hållbara timmermöbler som tål väder och vind. Alla våra produkter tillverkas av inhemska råvaror, av antingen timmer eller trä.",
            "I sortimentet finns gårdsgungor för barn samt trädgårdsmöbler. Vi tillverkar även gungor med vuxenmått på begäran.",
        ],
        "list_h": "Bra att veta",
        "list": ["Möbler av 70 × 150 planhyvlat timmer", "Gungor av inhemskt hållbart trä", "Med eller utan färg", "Levereras färdigbyggda", "Mått enligt önskemål"],
        "models_h": "Produkter",
        "models": [
            ("Barngunga", "En rolig och praktisk detalj på gården vid hemmet eller stugan. Gungan finns även med tak och som modell för vuxna.",
             ["Inhemskt hållbart trä", "Tak som tillbehör", "Även vuxenmodell"], 580,
             ["keinu-1", "keinu-2", "keinu-3"]),
            ("Trädgårdsmöbler av timmer", "Bordsgrupper och bänkar för gården och terrassen. Väl omskötta håller de i flera år.",
             ["70 × 150 planhyvlat timmer", "Med eller utan färg", "Enligt måttbeställning"], None,
             ["kalusteet-4", "kalusteet-1", "kalusteet-2", "kalusteet-3"]),
        ],
        "faq": [
            ("Hur sköter man timmermöbler?", "Väl omskötta timmermöbler tål väder och vind i flera år. Att förnya träskyddet med några års mellanrum håller ytan i skick."),
            ("Levererar ni möbler längre bort?", "Ja – mindre produkter levererar vi med transport till hela Finland."),
        ],
    },
    "koristeet": {
        "name": "Gårdsdekorationer", "card": "Gårdsdekorationer", "short": "Mjölkbord, dekorativa brunnar och postlådeställ.",
        "title": "Mjölkbord, dekorativ brunn och postlådeställ av trä | Jääkärihirsi",
        "desc": "Gårdsdekorationer enligt måttbeställning från Kortesjärvi: mjölkbord (från 650 €), dekorativa brunnar för 80–100 cm brunnsring (från 585 €) och postlådeställ (från 180 €), färdigt målade.",
        "h1": "Mjölkbord och <em>gårdsdekorationer</em>",
        "lead": "Mjölkbord, dekorativa brunnar och postlådeställ enligt måttbeställning av inhemskt trä – färdigt ihopsatta och målade.",
        "intro_h": "En bit finsk <em>gårdstradition</em>",
        "intro": [
            "Drömmer du om ett trivsamt mjölkbord eller en dekorativ brunn? Behöver kvarteret ett snyggt postlådeställ? Vi tillverkar gårdsdekorationerna enligt dina önskemål, huvudsakligen av inhemska råvaror.",
            "Du får lösningarna färdigt uppställda – snabbt, pålitligt och hållbart.",
        ],
        "list_h": "Bra att veta",
        "list": ["Färdigt ihopsatta och målade", "Du kan välja färg", "Av inhemskt trä", "Mindre produkter med transport till hela Finland"],
        "models_h": "Produkter",
        "models": [
            ("Mjölkbord", "Gammaldags mjölkbord är en del av finsk identitet. Vi tillverkar dem hantverksmässigt av panel med autentiskt utseende. På bilden ett mjölkbord i träfärg med takpapp.",
             ["Hantverk av panel", "Takpapp", "Mått enligt önskemål"], 650,
             ["maitolaituri"]),
            ("Dekorativ brunn", "En dekorativ brunn piggar upp gården. Brunnarna passar för brunnsringar på 80–100 cm och levereras färdigt ihopsatta och målade.",
             ["För 80–100 cm ring", "Färdigt ihopsatt", "Målad"], 585,
             ["koristekaivo-3", "koristekaivo-1", "koristekaivo-2"]),
            ("Postlådeställ", "Ett postlådeställ livar upp husets fasad. Ställen levereras färdigt målade i önskad färg. Lådorna och piedestalerna ingår.",
             ["Lådor och piedestaler ingår", "Målat i önskad färg"], 180,
             ["postilaatikkoteline"]),
        ],
        "faq": [
            ("Ingår postlådorna i leveransen?", "Ja, lådorna och piedestalerna ingår."),
            ("För hur stor brunnsring passar den dekorativa brunnen?", "Brunnarna tillverkas för brunnsringar på 80–100 cm."),
        ],
    },
}
T["sv"]["P"] = P_SV

T["sv"]["hub"] = {
    "title": "Gårdsbyggnader enligt måttbeställning – förråd, lusthus, lekstugor, utedass | Jääkärihirsi",
    "desc": "Gårdsbyggnader av timmer och trä från Kortesjärvi: förråd, vedlador, lusthus, lekstugor, utedass och sopskjul enligt måttbeställning, färdigt uppförda.",
    "h1": "Gårdsbyggnader <em>enligt mått</em>",
    "lead": "Gårdsbyggnader av timmer eller trä för hemmet och sommarstugan. Vi levererar det färdiga arbetet till platsen och vid önskemål färdigt uppfört.",
}

T["sv"]["company"] = {
    "title": "Jääkärihirsi Oy – timringsföretag i Kortesjärvi, Kauhava",
    "desc": "Jääkärihirsi Oy tillverkar gårdsbyggnader, timmermöbler och gårdsdekorationer i Kortesjärvi, Kauhava. Inhemskt planhyvlat timmer, måttbeställning, montering inom cirka 200 km.",
    "h1": "Timringsföretag <em>från Kortesjärvi</em>",
    "lead": "Jääkärihirsi Oy är ett timringsföretag i Kortesjärvi, Kauhava, med expertis inom gårdsbyggnader, -möbler och -dekorationer.",
    "p": [
        "Vår specialitet är tillverkning av högklassiga timmer- och träbyggnader. Inhemskt kvalitetsarbete – vi bygger enligt kundens önskemål, från gårdsbastur och förråd till timmermöbler och dekorationer.",
        "Vi vet hur man bygger en andningsbar och hållbar timmerbyggnad som betjänar sin användare i flera generationer. Vi använder alltid inhemska råvaror som klarar det finländska klimatet år efter år.",
        "När du beställer en gårdsbyggnad, sandlåda eller bastu av Jääkärihirsi stöder du äkta inhemskt arbete.",
    ],
    "mat_h": "Material",
    "mat": [("Planhyvlat timmer 70 × 150 mm", "Bastur och timmermöbler"), ("Planhyvlat timmer 58 mm", "Gårdsbastur"),
            ("Planhyvlat timmer 45 × 150 mm", "Bastur, förråd, lekstugor, utedass"), ("Lätt timmer 50 × 125 mm", "Vedlador"),
            ("Ytterpanel 22 × 120 mm", "Förråd, lusthus, lekstugor, utedass"), ("Inhemskt hållbart trä", "Gungor och sandlådor")],
    "deliv_h": "Leveranssätt",
    "deliv": [("Nyckelfärdigt", "Vi reser byggnaden färdig på plats inom cirka 200 km från Kortesjärvi."),
              ("Stomleverans", "Du får stommen och delarna för egen montering – passar även längre bort."),
              ("Mindre produkter som frakt", "Gungor, möbler och gårdsdekorationer med transport till hela Finland.")],
}

T["sv"]["quote"] = {
    "title": "Offertförfrågan – planera gårdsbastu eller gårdsbyggnad | Jääkärihirsi",
    "desc": "Välj produkt, mått och utrustning – du ser planritningen och ytan direkt. Skicka offertförfrågan till Jääkärihirsi i Kortesjärvi.",
    "h1": "Planera och <em>be om offert</em>",
    "lead": "Välj produkt och mått – du ser planritningen och ytan direkt. Vi preciserar detaljerna tillsammans före offerten.",
    "s1": "Vad vill du beställa?", "s2": "Mått och utrustning", "s3": "Leverans", "s4": "Kontaktuppgifter",
    "width": "Bredd (m)", "length": "Längd (m)", "diam": "Diameter (m)", "frame": "Stomme", "roof": "Tak", "extras": "Tillval",
    "model": "Modell", "delivery": "Leveranssätt", "town": "Leveransort", "town_ph": "T.ex. Nykarleby",
    "when": "Tidtabell", "when_ph": "T.ex. juni 2027", "more": "Mer information", "more_ph": "T.ex. fönstrens placering, färg, tillfart till tomten",
    "send": "Skicka offertförfrågan", "summary": "Sammanfattning", "area": "Yta", "inner": "Byggnad",
    "terrace": "Terrass", "porch": "Veranda", "steam": "Bastu", "dress": "Omklädningsrum",
    "qty": "Antal (st.)", "bins": "Soptunnor", "price_note": "Från-priset är riktgivande. Slutligt pris enligt offert.",
    "plan_note": "Planritningen är illustrativ.",
    "items": {
        "kalusteet": ["Barngunga", "Vuxengunga", "Gunga med tak", "Bordsgrupp av timmer", "Bänk av timmer"],
        "koristeet": ["Mjölkbord", "Dekorativ brunn", "Postlådeställ"],
    },
    "frames": ["Planhyvlat timmer 45 mm", "Planhyvlat timmer 58 mm", "Planhyvlat timmer 70 mm", "Ytterpanel"],
    "roofs": ["Takpapp", "Plåttak"],
    "deliveries": ["Nyckelfärdigt (montering)", "Stomleverans", "Hämtning i Kortesjärvi"],
    "extras_by": {
        "pihasauna": ["Terrass", "Täckt veranda", "Aggregat med vattenbehållare", "Aggregat med rörbehållare", "Glasdörr till bastun"],
        "pihavarasto": ["Springvägg (vedlada)", "Pardörrar", "Fönster"],
        "huvimaja": ["Bågfönster", "Fyrkantsfönster", "Grill- och ventilationspaket", "Målat"],
        "leikkimokki": ["Veranda", "Målad (rödmylla + vita lister)", "Sandlåda"],
        "wc": ["Euromakki HD-element", "Egen toalettutrustning"],
        "roskakatos": ["Dörrar", "Målat"],
        "kalusteet": ["Målat / betsat", "Tak till gungan"],
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
