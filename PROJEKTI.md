# Jääkärihirsi: projektin tausta ja päätökset

Kopio Äijä Groupin projektimuistiosta. Asiakkaan linjaukset ja tehdyt päätökset.

Jääkärihirsi Oy (Y 2386106-5, Puusepäntie 32 62420 Kortesjärvi, 045 119 7289, info@jaakarihirsi.com). Vanha sivu Duda fi+sv, DNS Route 53, posti M365. Verkkokauppa vilkasstore = 404 → linkit poistettu.
Tehty 3.10.2026 project-procad-sivustouudistus-koodipohjalla, vaalea (feedback-klinininen-ilme-vahan-pikkutekstia): logon vihreä #31714b, Schibsted Grotesk + Inter, sanamerkki JÄÄKÄRIHIRSI + vihreä hirsipalkki.
content.py: T["fi"]/T["sv"] samalla rakenteella (feedback-kieliversiot-samalla-sisallolla); vanhat URL:t säilyivät (myös /sv/timmermoebler). 8 tuotesivua: pihasaunat, piharakennukset/{pihavarastot,huvimajat,leikkimokit,ulko-wc,roskakatokset}, hirsikalusteet, pihakoristeet.
Myyntitoiminnot: tarjousvelho (SVG-pohjakuva mitoilla, terassi/kuisti, huvimaja-kahdeksankulmio, alkaen-hinta), 200 km toimitusaluekartta, alkaen-hinnat vain asiakkaan ilmoittamat (SV-sivuilta), ei johdettuja (cat_price näyttää ryhmähinnan vain jos kaikilla malleilla hinta). v2 6.10.: lämmin vaalea pohja #faf7f2. Obsidian-kortti Postly/Asiakkaat/Jääkärihirsi Oy.md.
Kuvat: 63 omaa (pieniä 640 px) + 11 Higgsfield-kuvaa; AI:lle pitää sanoa "flat-faced rectangular planed logs, NOT round" tai se tekee pyöröhirttä.
Preview https://claude.ai/artifact/UxWS9X17683YSCRVttQpWa, zip jaakarihirsi-nordichost.zip, README 8 vahvistettavaa.

**9.10.2026 KAUPPA:** repo github.com/Aija-group/jaakarihirsi (pushattu, git iCloud-kansiossa, scratchpad siivottu). Groweo (asiakkaan markkinointikumppani) asentanut vanhalle sivulle Groweo-chatin (workspace 69170e21fa3dbe6f156a884a), GTM-PTT7B5V (GA4 G-8FRK563X4T) ja Cookiebot 55b15f94-… → siirretty uuteen sivuun tuotantobuildiin (TRACKING = not DEMO). Opetus: tarkista vanhan sivun kolmannen osapuolen skriptit (chat, GTM, CMP) jo kartoitusvaiheessa.

**9.10.2026 asiakkaan muutokset (commit 5a52aa0):** pois Tuomas 10 (kärrysauna), huvimajat, keinut, kaikki AI-kuvat; hirsi 45×145/70×145, paneeli 20×95/20×120; ei pystytystä eikä km-rajaa (toimitus valmiina tai runkona osina); asiakkaan alkaen-hinnat P[...]["from"] + ITEM_PRICES; 87 kuvaa asiakkaan Drivestä (julkinen kansio → embeddedfolderview?id= listaa kaikki, lataus drive.usercontent.google.com/download?id=&confirm=t). Auki: postilaatikkoteline (Sulo: ei tehdä, asiakkaan hintalista: 120 €) ja Tuomas 15/20 -kuvien kohdistus.

Hero 9.10.: asiakkaan oma saunakuva (tuomas20-2) muokattu Higgsfield gpt_image_2_5 + image_references: rakennus ennallaan, 16:9, kepit/muta pois, sininen taivas (`sauna-hero`, iltaversio _materiaali/). Mobiilissa object-position 74%.

**How to apply:** muokkaa suoraan Jaakarihirsi/-kansiossa (git-repo), python3 build.py, commit + push; launch.json "jaakarihirsi-site" portti 8995.

- 2026-10-24: Groweon asennuskoodit (Jonni Sairio, Groweo) lisätty: Global-skripti oli jo (sama workspace), uutena Smart Flow -div etusivulle ja tuotesivuille tuotekorttien/mallien jälkeen ja Smart Chat -div samoille sivuille ennen yhteydenottoa. Vain tuotantobuildissa.
- 2026-10-26: Asiakas hyväksyi sivut julkaistavaksi. Pyyntö: pariovellinen varastorakennus (kuvat sauna-2 ja tuomas15-4, sama rakennus) siirrettiin pihasaunoista pihavarastoihin (varasto-15, varasto-16). Asiakas kysyi irtisanomisesta → ohje: vasta kun domain siirretty ja uusi sivu toimii.
