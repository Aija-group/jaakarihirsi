# Jääkärihirsi Oy – jaakarihirsi.com (hirsirakentaja, Kortesjärvi)

Uudistettu sivusto, tehty 3.10.2026 (Äijä Group). Vanha sivu: **Duda** (fi + sv, 6 + 6 sivua), DNS AWS Route 53 (Amazon Registrar).
**Posti on Microsoft 365:ssä** (MX jaakarihirsi-com.mail.protection.outlook.com) → MX, autodiscover ja SPF/DKIM säilytettävä DNS-muutoksessa.
Y-tunnus 2386106-5 · Puusepäntie 32, 62420 Kortesjärvi · 045 119 7289 · info@jaakarihirsi.com.

- `content.py` kaikki tekstit suomeksi ja ruotsiksi (`T["fi"]`, `T["sv"]`), tuotteet ja hinnat; `build.py` generaattori; `src/` tyylit, skriptit, kuvat, Suomen ääriviiva (`fin_rings.json`).
- `python3 build.py` → `site/` NordicHostin AI App Hostingiin (server.js, site/ commitoidaan) + `../jaakarihirsi-nordichost.zip`.
- `HOSTING=netlify python3 build.py --preview --artifact` → `preview/` (Claude-artifakti). Aja lopuksi oletus-build.
- Paikallinen testaus: `MAIL_DRYRUN=1 PORT=8995 node server.js`.

## Rakenne (13 sivua / kieli, 26 indeksoitavaa)
| Suomi | Svenska | Sisältö |
|---|---|---|
| `/` | `/sv/` | etusivu |
| `/pihasaunat/` | `/sv/gardsbastur/` | Tuomas 15 ja 20 + toteutusgalleria |
| `/piharakennukset/` | `/sv/gardsbyggnader/` | koontisivu |
| `/piharakennukset/pihavarastot/` | `…/forrad/` | pihavarasto + puulato |
| `/piharakennukset/leikkimokit/` | `…/lekstugor/` | leikkimökki + hiekkalaatikko |
| `/piharakennukset/ulko-wc/` | `…/utedass/` | ulkovessat |
| `/piharakennukset/roskakatokset/` | `…/sopskjul/` | roskakatokset |
| `/hirsikalusteet/` | `/sv/timmermoebler/` | hirsipöytäsarjat |
| `/pihakoristeet/` | `/sv/gardsdekorationer/` | maitolaituri, koristekaivo, postilaatikkoteline |
| `/tarjouspyynto/` | `/sv/offert/` | tarjousvelho |
| `/yritys/` | `/sv/foretaget/` | materiaalit, toimitustavat |
| `/yhteystiedot/` | `/sv/kontakt/` | |
| `/tietosuoja/` | `/sv/dataskydd/` | sis. Cookiebot-evästeseloste |

Vanhat osoitteet säilyivät. `/evasteet` → `/tietosuoja/#evasteet`. Kanoninen **www.jaakarihirsi.com**. hreflang fi/sv + sitemap.

**Asiakkaan muutokset 9.10.2026:** poistettu kärrysauna Tuomas 10, huvimajat ja keinut. Hirsikoot 45 × 145 ja 70 × 145 mm, ulkovuoripaneeli 20 × 95 tai 20 × 120 mm (58 mm pois). Pystytystä ei tehdä eikä kilometrirajaa mainita: toimitus joko valmiiksi koottuna (avaimet käteen) tai runkona osina. Pihavarasto 45 × 145 hirsi tai 20 × 95 paneeli.

## Myyntiä tukevat toiminnot
- **Tarjousvelho** (`/tarjouspyynto/`): tuote kuvakortilla → malli, mitat, runko, katto, lisävalinnat → toimitustapa ja paikkakunta. Sivupaneeli piirtää **pohjakuvan mitoilla ja pinta-alalla** (sauna: löylyhuone + pukuhuone + terassi/kuisti, huvimaja: kahdeksankulmio, roskakatos: astioiden määrä) ja näyttää alkaen-hinnan. Tuotesivujen napit esivalitsevat tuotteen ja mallin (`?tuote=pihasauna&malli=…`).
- **Alkaen-hinnat asiakkaan listan mukaan (9.10.2026):** sauna 7 500 €, leikkimökki 1 500 €, maitolaituri 500 €, postilaatikkoteline 120 €, varasto 2 700 €, hirsipöytäsarja 400 €, koristekaivo 450 €, roskakatos 550 €, puulato 2 000 €, ulko-WC 1 200 €. Tuoteryhmän hinta `from`-kentässä (content.py), mallihinnat malleissa; hiekkalaatikolla ei hintaa. Velho ei laske yhteen eikä arvioi hintoja. `SHOW_PRICES` piilottaa kaikki.
- Mallikohtaiset kuvagalleriat lightboxilla, FAQ (FAQPage-schema), soitto + tarjous -palkki mobiilissa.
- Lomakkeet `yhteydenotto` ja `tarjous` → info@jaakarihirsi.com (NordicHostissa SMTP_*-muuttujat). Ruotsinkielinen lomake ohjaa `/sv/tack/`, aiherivillä "(svenska)".

## Seuranta, evästeet ja chat (Groweo)
Asiakkaan markkinointikumppani Groweo on asentanut vanhalle sivulle nämä, ja ne on siirretty uuteen sivuun samoilla tunnuksilla (`build.py`: `tracking_head()` jne.):
- **Groweo-chatti** `engine.groweo.com/groweoApp/groweoApp.js`, workspaceid `69170e21fa3dbe6f156a884a` (joka sivulla, fi + sv)
- **Google Tag Manager** `GTM-PTT7B5V` (GA4 `G-8FRK563X4T` dataLayerissa `ga4-id`, kuten vanhalla sivulla)
- **Cookiebot** `55b15f94-16e4-4f7f-9de3-434403dc6c79`, blockingmode auto, Google consent mode oletuksena kaikki denied; kieli fi/sv sivun mukaan. Evästeseloste (CookieDeclaration) tietosuojasivulla `#evasteet`, footerissa Evästeasetukset-linkki.
- Vain tuotantobuildissa (`python3 build.py`) – Netlify-/artifakti-esikatselussa ei seurantaa. Chatti ja banneri näkyvät vain jaakarihirsi.com-domainissa (Groweo/Cookiebot sidottu domainiin).
- Vanha /evasteet (Fonectan vakioteksti) → `/tietosuoja/#evasteet`.
- **Groweolle tiedoksi:** sivupolut ja lomakkeet muuttuvat (uusi tarjousvelho `/tarjouspyynto/`, kiitossivut `/kiitos/` ja `/sv/tack/`) → GTM-konversiotagit kannattaa tarkistaa julkaisun jälkeen.

## Kuvat
Kaikki kuvat ovat asiakkaan omia: 87 kuvaa asiakkaan Drive-kansiosta 9.10.2026 (`_materiaali/` ei repossa) + 4 vanhalta sivulta (hiekkalaatikko, puulato-1/2, vanha postilaatikkoteline). Tekoälykuvat poistettu kokonaan (Äijä Groupin linjaus: ei AI-rakennuksia). Kuvat skaalattu max 1800 px.
Drive-kuvien tiedostonimet olivat satunnaisia (esim. "kkkk.jpeg") → lajiteltu tuotteittain silmämääräisesti. 3 kuvaa jätetty pois tekstipäällysteen vuoksi (asdf, ddddd, dsa).

## Vahvistettavaa asiakkaalta
1. **Tuomas 15 / Tuomas 20 -kuvat**: mallien kuvat on valittu Drive-kuvista ulkonäön perusteella (15 = katettu kuisti, 20 = terassi kaiteineen). Tarkista, että oikeat kuvat ovat oikean mallin alla.
2. **Postilaatikkoteline**: Sulon muistiinpanoissa "postilaatikkotelineitä eivät tee", mutta asiakkaan omassa hintalistassa on "Postilaatikkotelineen hinnat alkaen 120 €" ja Drivessä on kuva telineestä → jätetty sivulle. Poistetaan, jos ei tehdä.
3. **Saunamallien mitat** (Tuomas 15/20): sivulla ei kokoja.
4. **Puulato**: runko 50 × 125 mm kevythirsi ja lattia 22 × 100 mm ovat vanhalta sivulta (ei muutettu).
5. **Verkkokauppa** vilkasstore ei toimi → linkit poistettu.
6. Velhon lisävalinnat (terassi, kuisti, pariovet, ikkuna, maalaus…) ovat toiveita tarjouspyyntöön, eivät lupauksia.
7. Ennen DNS-muutosta: M365-postin tietueet (MX, autodiscover, SPF, DKIM) talteen Route 53:sta.
