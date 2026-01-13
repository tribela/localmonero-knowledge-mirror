---
title: "Kuinka Monero ratkaisi Bitcoinia vaivaavan lohkokoko-ongelman"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Huomaa:** On erittäin suositeltavaa, että lukija on lukenut artikkelimme ["Why Monero has Tail Emission"](/knowledge/monero-tail-emission) ja [“Monero Mining: What Makes RandomX so Special”](/knowledge/monero-mining-randomx). Tämä artikkeli perustuu siinä esitettyihin käsitteisiin._

Aina kun ihmiset keskustelevat lohkoketjun ongelmista, yksi ensimmäisistä avainsanoista on "skaalaus". Ei ole mikään salaisuus, että lohkoketjut eivät skaalaudu hyvin, mutta useimmat ihmiset eivät tiedä miksi.

Totuus on, että skaalaus on itse asiassa termi, joka kattaa kaksi eri alaluokkaa: protokollatuki ja tekninen tuki tietyllä hetkellä. Tässä artikkelissa keskitämme huomiomme yhteen, Protokollatuki on pohjimmiltaan mitta siitä, kuinka monta tapahtumaa protokolla pystyy käsittelemään tietyllä hetkellä.

Bitcoinilla on lohkon kokorajoitus, mikä tarkoittaa, että kun lohkoon on sisällytetty tarpeeksi tapahtumia, kaikkien lisätapahtumien on odotettava jonossa seuraavaa lohkoa varten. Hyödyllinen analogia olisi ajatella junaa. Juna saapuu asemalle ja jonossa olevat ilmoittautuvat sisään. Kun juna on täynnä, kaikkien ulkopuolelle jääneiden on odotettava seuraavaa.

Bitcoin käyttää maksuja määrittääkseen, kuka pääsee lohkoon ja kuka ei. Hyppäämällä takaisin juna-analogiaan, voidaan kuvitella, että yksi mahdollinen matkustaja, joka on jäämässä jälkeen, tarjoaa junainsinöörille viisi dollaria, jotta hän antaisi hänelle paikan. Muut matkustajat seuraavat perässä, ja lopulta käydään tarjoussota siitä, kuka saa mitkäkin paikat. Kuljettajan on päätettävä, haluaako hän noudattaa saapumisjärjestystä, mutta hänen parhaan taloudellisen edunsa mukaista on maksimoida tulonsa ottamalla mukaan korkeimman tarjouksen tekijät.

Tässä analogiassa louhijat ovat junankuljettajia. He voivat sisällyttää lohkoon mitä tahansa tapahtumia, mutta yleensä he valitsevat ne, joiden maksut ovat korkeimmat.

Vaihtoehtoisesti, jos junat eivät ole kovin täynnä, ihmisillä ei ole kannustimia maksaa korkeita maksuja, koska vapaita paikkoja on runsaasti jäljellä.

Vuoden 2017 kryptovaluuttabuumin huipulla Bitcoin transaktiot tulvivat ja maksut nousivat pilviin niiltä, jotka halusivat tulla mukaan seuraavaan lohkoon tai mihin tahansa lohkoon lähitulevaisuudessa. Ne jotka eivät halunneet maksaa korkeita maksuja, näkivät, että heidän tapahtumansa lykkääntyivät tunteja, päiviä tai jopa putosivat jonosta kokonaan.

Tämä oli tuskallinen näkemys siitä, kuinka Bitcoinille kävisi, jos usein puhuttu "massa-adoptio" tapahtuisi. Jos Bitcoinin ottaisi käyttöön massat, asiat olisivat vielä huonommin kuin vuonna 2017 ja Bitcoin olisi muiden kuin varakkaiden ulottumattomissa, yksinkertaisesti siksi, että läpijuoksu on pieni kiinteän lohkokoon vuoksi, jolloin maksumarkkinat ottavat vallan. 

Monero näki tämän ja halusi tehdä jotain erilaista. Joten Monero-kehittäjät ottivat käyttöön dynaamisen lohkokoon.

Periaatteessa Monerossa on myös lohkokoon raja, mutta se on pehmeä raja. Kun odottavien tapahtumien jono tulee liian pitkäksi, louhijat voivat suurentaa lohkojen kokoa. Juna-analogiamme avulla voit kuvitella lisääväsi junavaunuja ylimääräisille matkustajille. Kun jono on tyhjä, lohkot pienenevät takaisin alkuperäiseen kokoonsa eteenpäin.

Jos tämä vaikuttaa siistiltä ajatukselta, on järkevää kysyä, miksi Monero on ainoa kryptovaluutta, joka on toteuttanut tämän? Mikset lisäisi sitä Bitcoiniin suorituskyvyn ongelmien lopettamiseksi?

Valitettavasti tämä ei ole mahdollista. Syitä siihen on useita ja teemme parhaamme selittääksemme sen.

On aina louhijan edun mukaista hankkia suuria lohkoja. Suurilla lohkoilla ne mahtuvat useampaan tapahtumaan ja ansaitsevat enemmän rahaa maksuista sekä lohkopalkkioista. Tämä voi johtaa spämmihyökkäyksiin, joissa joku lähettää monia pieniä tapahtumia pienillä kuluilla turvottaakseen ketjua. Louhijat vain nostaisi lohkon kokoa, ottaen mukaan ne kaikki tapahtumat, koska raha on rahaa, olipa se kuinka pieni määrä tahansa. Tämä johtaisi jatkuvasti suuriin lohkoihin, joista olisi vain vähän taloudellista hyötyä. Bitcoin ratkaisee tämän rajoittamalla keinotekoisesti lohkon kokoa, jolloin syntyy maksumarkkinat. Spämmihyökkääjät joutuisivat maksamaan muille käyttäjille maksuja, eikä se ole enää halpaa. Mutta tämä tarkoittaa että lohkot täyttyvät, joten jotkut tapahtumat jäävät odottamaan kuten yllä mainittiin.

Kuinka Monerolla voi olla dynaamisia lohkokokoja mutta välttää spämmihyökkäykset? Vastaus on yksinkertainen, mutta fiksu. Lohkopalkkion rangaistus otetaan käyttöön, kun lohko on normaalia suurempi. Jos louhija haluaa suurentaa lohkon kokoa, palkkio jonka hän saa lohkon löytämisestä, on pienempi kuin mitä he muuten saisivat. Joten ne lisäävät lohkon kokoa vain, kun käyttäjien maksamat tapahtumamaksut ovat suuremmat kuin lohkopalkkion menetetty osuus. Jos louhija esimerkiksi menettäisi 0,5 XMR nostamalla lohkon kokoa ja maksettujen transaktiomaksujen summa olisi 0,4 XMR, nettotappio olisi 0,1 XMR jos he nostavat kokoa, joten he eivät tee sitä. Päinvastoin, jos transaktiomaksujen yhteenlaskettu summa on 0,7 XMR, nettovoitto on 0,2 XMR, vaikka he menettävät 0,5 XMR:n lohkopalkkion rangaistuksesta, joten louhija kasvattaa kokoa.

Näiden dynaamisten lohkojen avulla verkko voi kasvaa orgaanisesti ilman, että se rajoittaa keinotekoisesti lohkon kokoa pakollisten maksujen muodostamiseksi ja välttää samalla spämmihyökkäyksiä. On monia muita näkökulmia joista voimme tarkastella tätä ideaa ja enemmän syitä, miksi sitä ei olisi mahdollista lisätä Bitcoiniin, mutta tällä hetkellä toivomme, että lukija ymmärtää kuinka Monero ohittaa useita Bitcoinin ongelmia ja kuinka se aikoo skaalata suorituskykyään tulevaisuuteen.

Lue lisää

  * [Kuinka Monero ainutlaatuisesti mahdollistaa kiertotaloudet](/knowledge/monero-circular-economies)/

  * [Moneron sormusallekirjoitukset vs CoinJoin kuten Wasabissa](/knowledge/ring-signatures-vs-coinjoin)/

  * [Miksi (ja miten!) sinun pitäisi hallita omia avaimiasi](/knowledge/hold-your-keys)/

  * [Osallistuminen Moneroon](/knowledge/contributing-to-monero)/

  * [Kuinka etäsolmut vaikuttavat Moneron yksityisyyteen](/knowledge/remote-nodes-privacy)/

  * [Kuinka Monero käyttää hard forkkeja verkon päivittämiseen](/knowledge/network-upgrades)/

  * [Katselutunnisteet: Kuinka yksi tavu vähentää Moneron lompakon synkronointiaikoja yli 40%](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool ja sen rooli Monero-louhinnan hajauttamisessa](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Mitä se tekee Monerolle](/knowledge/seraphis-for-monero)/

  * [Onko Bitcoinin muuntaminen Moneroksi yhtä yksityistä kuin Moneron ostaminen suoraan?](/knowledge/most-private-way-to-buy-monero)/

  * [Miksi Monero käyttää "Trustless" -asetusta toisin kuin Zcash](/knowledge/monero-trustless-setup)/

  * [Miksi Monero on parempi arvon säilyttäjä kuin Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Kuinka Monero voi voittaa Bitcoinin verkkovaikutukset](/knowledge/network-effect)/

  * [Miksi Monerolla on kriittisin ajatteluyhteisö](/knowledge/critical-thinking)/

  * [Huijaukset, joita kannattaa huomioida Moneroa käytettäessä](/knowledge/monero-scams)/

  * [Kuinka Atomic Swapit toimivat Monerossa](/knowledge/monero-atomic-swaps)/

  * [Mitä jokaisen Moneron käyttäjän on tiedettävä verkostoitumisesta](/knowledge/monero-networking)/

  * [Kuinka RingCT piilottaa Monero-transaktiosummat](/knowledge/monero-ringct)/

  * [Kuinka Monero Stealth -osoitteet suojaa identiteettiäsi](/knowledge/monero-stealth-addresses)/

  * [Kuinka Monero-aliosoitteet estävät identiteetin yhdistämisen](/knowledge/monero-subaddresses)/

  * [Moneron Outputit selitettynä](/knowledge/monero-outputs)/

  * [Moneron parhaat käytännöt aloittelijoille](/knowledge/monero-best-practices)/

  * [Kuinka sormusallekirjoitukset sekoittavat Moneron outputit](/knowledge/ring-signatures)/

  * [Kuinka CLSAG parantaa Moneron tehokkuutta](/knowledge/what-is-clsag)/

  * [Miksi Monerolla on "Tail Emission"](/knowledge/monero-tail-emission)/

  * [Moneron lyhyt historia](/knowledge/monero-history)/

  * [Wired Magazine on väärässä Monerosta, tässä miksi](/knowledge/wired-article-debunked)/

  * [15 parasta Monero-myyttiä ja -huolia, jotka on kumottu](/knowledge/monero-myths-debunked)/

  * [Kuinka Dandelion++ pitää Moneron tapahtuman alkuperän yksityisenä](/knowledge/monero-dandelion)/

  * [Miksi Monero on avoimen lähdekoodin ja hajautettu](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Moneron louhinta: Mikä tekee RandomX:stä niin erityisen?](/knowledge/monero-mining-randomx)/

  * [Miksi Monero on parempi kuin Dash, Zcash, Zcoin (jopa Lelantuksen kanssa), Grin ja Bitcoin-mikserit kuten Wasabi (päivitetty toukokuussa 2020)](/knowledge/why-monero-is-better)/

Lue lisää