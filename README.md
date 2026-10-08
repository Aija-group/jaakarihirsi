# Jääkärihirsi Oy – jaakarihirsi.com (hirsirakentaja, Kortesjärvi)

Uudistettu sivusto, tehty 3.10.2026 (Äijä Group). Vanha sivu: **Duda** (fi + sv, 6 + 6 sivua), DNS AWS Route 53 (Amazon Registrar).
**Posti on Microsoft 365:ssä** (MX jaakarihirsi-com.mail.protection.outlook.com) → MX, autodiscover ja SPF/DKIM säilytettävä DNS-muutoksessa.
Y-tunnus 2386106-5 · Puusepäntie 32, 62420 Kortesjärvi · 045 119 7289 · info@jaakarihirsi.com.

- `content.py` kaikki tekstit suomeksi ja ruotsiksi (`T["fi"]`, `T["sv"]`), tuotteet ja hinnat; `build.py` generaattori; `src/` tyylit, skriptit, kuvat, Suomen ääriviiva (`fin_rings.json`).
- `python3 build.py` → `site/` NordicHostin AI App Hostingiin (server.js, site/ commitoidaan) + `../jaakarihirsi-nordichost.zip`.
- `HOSTING=netlify python3 build.py --preview --artifact` → `preview/` (Claude-artifakti). Aja lopuksi oletus-build.
- Paikallinen testaus: `MAIL_DRYRUN=1 PORT=8995 node server.js`.

## Rakenne (14 sivua / kieli, 28 indeksoitavaa)
| Suomi | Svenska | Sisältö |
|---|---|---|
| `/` | `/sv/` | etusivu |
| `/pihasaunat/` | `/sv/gardsbastur/` | Tuomas 10 / 15 / 20 |
| `/piharakennukset/` | `/sv/gardsbyggnader/` | koontisivu |
| `/piharakennukset/pihavarastot/` | `…/forrad/` | pihavarasto + puulato |
| `/piharakennukset/huvimajat/` | `…/lusthus/` | 6- ja 8-kulmaiset |
| `/piharakennukset/leikkimokit/` | `…/lekstugor/` | leikkimökki + hiekkalaatikko |
| `/piharakennukset/ulko-wc/` | `…/utedass/` | ulkovessat |
| `/piharakennukset/roskakatokset/` | `…/sopskjul/` | roskakatokset |
| `/hirsikalusteet/` | `/sv/timmermoebler/` | keinut + puutarhakalusteet |
| `/pihakoristeet/` | `/sv/gardsdekorationer/` | maitolaituri, koristekaivo, postilaatikkoteline |
| `/tarjouspyynto/` | `/sv/offert/` | tarjousvelho |
| `/yritys/` | `/sv/foretaget/` | materiaalit, toimitustavat, kartta |
| `/yhteystiedot/` | `/sv/kontakt/` | |
| `/tietosuoja/` | `/sv/dataskydd/` | |

Vanhat osoitteet säilyivät (Duda ilman kauttaviivaa → server.js lisää kauttaviivan 301:llä). `/evasteet` → `/tietosuoja/`. Kanoninen **www.jaakarihirsi.com** (kuten vanhalla sivulla). hreflang fi/sv + sitemap.

**Miksi tämä jako:** pihasauna, pihavarasto/puuvaja, huvimaja, leikkimökki, ulko-WC ja roskakatos ovat erikseen haettuja tuotteita → omat sivut. Puulato ja pihavarasto ovat samaa hakuaihetta, hiekkalaatikko kuuluu leikkimökkien kanssa samaan ostotilanteeseen, keinut + kalusteet ja pihakoristeet ovat pieniä tuotteita, joille riittää yksi sivu.

## Myyntiä tukevat toiminnot
- **Tarjousvelho** (`/tarjouspyynto/`): tuote kuvakortilla → malli, mitat, runko, katto, lisävalinnat → toimitustapa ja paikkakunta. Sivupaneeli piirtää **pohjakuvan mitoilla ja pinta-alalla** (sauna: löylyhuone + pukuhuone + terassi/kuisti, huvimaja: kahdeksankulmio, roskakatos: astioiden määrä) ja näyttää alkaen-hinnan. Tuotesivujen napit esivalitsevat tuotteen ja mallin (`?tuote=pihasauna&malli=…`).
- **Alkaen-hinnat vain siellä, missä asiakas on ne itse ilmoittanut** (mallikohtaisesti). Tuoteryhmän kortissa hinta näkyy vain, jos kaikilla ryhmän malleilla on ilmoitettu hinta – esim. pihasaunoissa ei, koska Tuomas 10:n hinta puuttuu. Velho ei laske yhteen eikä arvioi hintoja. `SHOW_PRICES` content.py:ssä piilottaa kaikki.
- **Toimitusaluekartta**: 200 km säde Kortesjärveltä + pientavarat koko Suomeen.
- Mallikohtaiset kuvagalleriat lightboxilla, FAQ (FAQPage-schema), soitto + tarjous -palkki mobiilissa.
- Lomakkeet `yhteydenotto` ja `tarjous` → info@jaakarihirsi.com (NordicHostissa SMTP_*-muuttujat). Ruotsinkielinen lomake ohjaa `/sv/tack/`, aiherivillä "(svenska)".

## Kuvat
63 asiakkaan omaa kuvaa vanhalta sivulta (kaikki tuotekuvat). Ne ovat pieniä (640 px) → käytetty vain malligallerioissa ja korteissa.
Higgsfield-kuvat (gpt_image_2_5, nimessä `-ai`): hero-järvisauna, talvisauna, saunan sisäkuva, pihavarasto, huvimaja, leikkimökki, ulko-WC, roskakatos, maitolaituri, työpaja. Rakennukset pyydetty höylähirtenä (ei pyöröhirttä), jotta ne vastaavat asiakkaan tuotteita.
Logo: vanhan logon mukainen sanamerkki JÄÄKÄRIHIRSI + vihreä hirsipalkki (#31714b, logon vihreä). Favicon = kolme hirttä.

## Vahvistettavaa asiakkaalta
1. **Hinnat**: alkaen-hinnat ovat vanhan sivun RUOTSINKIELISISTÄ versioista (Tuomas 15 5 600 €, Tuomas 20 5 800 €, puulato 1 400 €, pihavarasto 1 890 €, huvimaja 2 100 €, leikkimökki 950 €, WC 880 €, maitolaituri 650 €, koristekaivo 585 €, roskakatos 600 €, postilaatikkoteline 180 €, hiekkalaatikko 145 €, lasten keinu 580 €). Suomenkielisiltä sivuilta ne puuttuivat – ovatko ajan tasalla? Tuomas 10:n ja puutarhakalusteiden hinta puuttuu.
2. **Saunamallien mitat** (Tuomas 10/15/20) – sivulla ei ole kokoja, koska niitä ei ollut vanhallakaan sivulla. Mallien lyhyet kuvaukset (kuisti/terassi) on päätelty kuvista.
3. **Verkkokauppa** jaakarihirsi.vilkasstore.com ei toimi (404, sertifikaattivirhe) → linkit poistettu. Onko kauppa lopetettu?
4. Toimitusalue "noin 200 km säteellä" ja "pientavarat koko Suomeen" ovat vanhalta sivulta – pätevätkö yhä?
5. Velhon lisävalinnat (terassi, kuisti, pariovet, ikkuna, maalaus…) ovat toiveita tarjouspyyntöön, eivät lupauksia – tarkista, ettei listalla ole mitään, mitä ette tee.
6. FAQ:n lupa-vastaus ohjaa kunnan rakennusvalvontaan (ei lupausta luvattomuudesta).
7. Omia uudempia valokuvia kannattaa pyytää – nykyiset ovat pieniä ja osin vanhoja; AI-kuvat voi korvata oikeilla.
8. Ennen DNS-muutosta: M365-postin tietueet (MX, autodiscover, SPF, DKIM) talteen Route 53:sta.
