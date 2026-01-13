---
title: "Seraphis: Mitä se tekee Monerolle"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: modulaarinen suunnittelupäivitys Monero-transaktioihin

## Seraphis: modulaarinen suunnittelupäivitys Monero-transaktioihin

Tässä viestissä kuvataan [Seraphis](https://github.com/UkoeHB/Seraphis), joukko transaktioprotokollarakenteita ja abstraktioita, jotka on kehittänyt pseudonyymitutkimuksen avustaja [`kokeellista`](https://github.com/UkoeHB) Monero-ekosysteemiä ja jatkuvaa tietoturva-analyysia varten. Pseudonyymi kirjoittaja [`coinstudent2048`](https://github.com/coinstudent2048).  
Teemme joitain yksinkertaistuksia ja jätämme pois tiettyjä teknisiä yksityiskohtia selvyyden vuoksi. Ja koska Seraphisin suunnittelu on vielä kesken, kiinnostuneiden lukijoiden kannattaa katsoa Seraphis-dokumentaatiosta uusimmat tiedot.

## Transaktiot Monerossa

## Transaktiot Monerossa

Protokollat, kuten Bitcoin, Monero ja muut, perustuvat ns. "ulostulomalliin", jossa _ulostulo_ on esitys arvosta, joka voidaan siirtää.  
Transaktiot kuluttavat yhtä tai useampaa lähettäjän ohjaamaa ulostuloa ja luovat uusia ulostuloja, jotka on suunnattu vastaanottajille (tai takaisin lähettäjälle vaihdossa); transaktion on oltava tasapainossa siten, että kulutettujen tuotosten on sisällettävä kokonaisarvo, joka on täsmälleen sama kuin uusien ulostulojen arvo (plus verkon määräämä maksu).  
Monissa protokollissa, kuten Bitcoinissa, ulostulon sisältämä arvo kirjoitetaan julkisesti, samoin kuin vastaanottaja.  
Lisäksi lohkoketjua katsomalla on helppoa nähdä, onko tuotos käytetty ja milloin se on käytetty (eli onko se kulutettu myöhemmässä transaktiossa ja mikä transaktio kulutti sen).

Sitä vastoin Moneron kaltaisissa protokollissa on erilainen tyyli:

  * Ulostulojen arvot ovat piilotettuja eivätkä näy lohkoketjussa
  * Vastaanottajien osoitteet piilotetaan kertaluonteisen osoiteprotokollan avulla
  * Epäselvät allekirjoitukset peittävät sen, onko ulostulo käytetty vai ei 

Seurauksena on, että ulkoisen tiedon puuttuessa on vaikea määrittää, onko tietty ulostulo käytetty, mikä sen arvo on ja kuka sen vastaanottaja on.

Nykyinen Monero-tapahtumaprotokolla on nimeltään _RingCT_ , ja se käyttää useita kryptograafisia rakennuspalikoita näiden suunnittelutavoitteiden saavuttamiseksi.

  * _Sitoumukset_ piilottavat summat matemaattisesti hyödyllisellä tavalla
  * _Etäisyyssuojat_ estävät ylivuodon, joka voi täyttää syöttöä 
  * _Linkitettävät sormusallekirjoitukset_ tarjoavat allekirjoittajien epäselvyyttä ja estävät kaksinkertaisen kulutuksen
  * _Sitoumuspoikkeamat_ vakuuttavat transaktioiden saldon

Nämä rakennuspalikat on huolellisesti kiedottu yhteen RingCT-protokollan rakentamiseksi.

RingCT-protokollan hyödyllinen ominaisuus on, että joitain rakennuspalikoita voidaan muuttaa tai päivittää tavalla, joka säilyttää yleisen suunnittelun ja ominaisuudet ennallaan, mutta joka voi parantaa tehokkuutta tai turvallisuutta. Itse asiassa tällaisia päivityksiä on tapahtunut (ja suunnitellaan tapahtuvan) useita kertoja Moneron historiassa. Alkuperäisen RingCT-protokollan etäisyystodistukset olivat mittavia ja hitaita; ne päivitettiin myöhemmin [Bulletproofs](https://eprint.iacr.org/2017/1066)-nimiseen rakenteeseen, joka pienensi ja nopeutti tapahtumia paremmalla tietoturva-analyysillä, ja aiotaan päivittää uudempaan rakenteeseen nimeltä [Bulletproofs+](https://eprint.iacr.org/2020/735) tehokkuuden parantamiseksi. 

Samanlainen prosessi käytiin läpi linkitettävän sormusallekirjoituksen rakennuspalkin kanssa. Alkuperäisessä protokollassa käytettiin rakennetta nimeltä [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34). Tämä päivitettiin myöhemmin uudempaan rakenteeseen nimeltä [CLSAG](https://eprint.iacr.org/2019/654), joka on nopeampi, johtaa pienempiin transaktioihin ja jolla on parempi tietoturva-analyysi. Vielä uudempaa linkitettävää sormusallekirjoitusrakennetta, joka perustuu [Triptychiin](https://eprint.iacr.org/2020/018), ehdotettiin, mutta tätä ei otettu käyttöön, koska se vaikuttaa usean allekirjoituksen toimintaan.

## Seraphis

## Seraphis

Seraphis vie tämän idean askeleen pidemmälle.  
Sen sijaan, että päivitettäisiin olemassa olevan RingCT-tapahtumaprotokollan yksittäisiä palikoita, se ottaa käyttöön erilaisen protokollan, joka voi hyödyntää erilaisia rakennuspalikoita ja tarjota parannettuja toimintoja.

## Rakennuspalikoita

## Rakennuspalikoita

Seraphis käyttää erilaisia kryptografisia rakennuspalikoita saavuttaakseen suunnittelutavoitteensa.

  * _Sitoumukset_ piilottavat edelleen summia
  * _Kantamanvarmistus_ estää edelleen ylivuodon ja syöttötuloksen
  * _Jäsenyystodistukset_ tarjoavat allekirjoittajien epäselvyyttä
  * _Sitoumuspoikkeamat_ vahvistavat edelleen saldon
  * _Valtuutetut todisteet_ estävät kaksinkertaisen kulutuksen

Huomaa muutos tässä: linkitettävät sormusallekirjoitukset korvataan jäsentodisteiden ja valtuutustodistusten yhdistelmällä. Karkeasti ottaen jäsenyystodisteet osoittavat, että kulutettu tuotos on osa suurempaa joukkoa, samoin kuin RingCT:ssä. Mutta toisin kuin RingCT, jäsenyystodistukset eivät sisällä linkitystagia ollenkaan! Valtuuttavat todisteet osoittavat, että linkitystagi on kelvollinen ja että niitä käytetään lopullisen tapahtuman allekirjoittamiseen.

Koska RingCT lisää linkitystagin epäselväksi allekirjoitukseksi, allekirjoitus (ja usean allekirjoituksen) toiminnot ovat laskennallisesti intensiivisempiä, ja muiden tunnisteisiin liittyvien toimintojen rakentaminen tulee haastavammaksi. Mutta Seraphisissa jäsentodisteiden rakentaminen voidaan siirtää turvallisesti erittäin luotettavilta laitteilta (joilla voi olla rajoitettu laskentateho, kuten fyysinen lompakko) vähemmän luotetulle laitteelle, ja allekirjoitus (ja moniallekirjoitus) on paljon helpompaa käyttämällä paljon yksinkertaisempaa valtuutustodistusta.

Onneksi jotkin Seraphisin vaatimista rakennuspalikoista ovat jo olemassa muualla, eikä niitä tarvitse suunnitella tyhjästä. Sekä Bulletproofs- että Bulletproofs+ -rakenteita voidaan käyttää etäisyydenkestävänä. Schnorr-tyyppisiin todistusjärjestelmiin tehtyjä muutoksia voidaan käyttää todistusten hyväksyntään. Ja tehokas [todistusjärjestelmä](https://eprint.iacr.org/2015/643), jota on jo käytetty Triptychin, [Lelantuksen](https://eprint.iacr.org/2019/373) ja [Sparkin](http/ps://eprint.iacr.org/2021/1173)* perustana, voidaan muokata.

* Cypher Stack saa rahoitusta Spark-kehitykseen.

## Osoitteet

## Osoitteet

Valitettavasti tällä hetkellä käytössä olevat Monero-osoitteet eivät ole yhteensopivia Seraphisin kanssa. Käyttäjien on luotava uusia osoitteita lompakkoavaimistaan saadakseen Monerot, jos Seraphis otetaan käyttöön. Näillä ekosysteemikustannuksilla on kuitenkin monia etuja.

Yllä käsiteltyjen rakenteellisten etujen lisäksi Seraphis-suunnittelu soveltuu moniin erilaisiin osoitteiden rakentamismahdollisuuksiin, joista jokainen sisältää kompromisseja. Vaikka lopullinen Seraphisissa käytettävä osoiterakenne on [ vielä päättämättä](https://github.com/monero-project/research-lab/issues/92) (yksi paljon huomiota saava malli on nimeltään [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), voimme kuvata joitain yleisiä ja hyödyllisiä ominaisuuksia.

Saatat tietää, että Monero-osoitteet tarjoavat _katseluavain_ -toiminnon, jossa voit antaa katseluavaimen laitteelle tai kolmannelle osapuolelle ja antaa sen katsella saapuvia tulosteita puolestasi, antamatta valtuuksia kuluttaa varoja. Tämä on hyödyllistä lompakoille, jotta voit pysyä ajan tasalla ja pitää kuluavaimesi turvallisesti lukittuna. Se on hyödyllinen myös tapauksissa, joissa haluat ulkopuolisen näkymän, kuten julkinen hyväntekeväisyysjärjestö joka tarjoaa avoimuutta tai yritykselle, jolla on tilitoimisto.

Monero-näkymäavainten haittapuoli on, että ne eivät tarjoa täydellistä tai hienorakeista näkymää. Ei ole mahdollista havaita luotettavasti, milloin lompakko käyttää varoja, mikä vaikeuttaa lompakon saldojen laskemista oikein, kun kuluavainta ei ole saatavilla. Tällä hetkellä ei myöskään ole mahdollista havaita saapuvia lähtöjä ilman, että myös näiden lähtöjen arvot opitaan (mikä tarkoittaa, että saapuvien lähtöjen löytämisestä vastaavat kolmannet osapuolet oppivat tarkalleen, kuinka paljon Moneroa hankit).

Seraphis, joka käsittelee rakenteita, voi ratkaista tämän. Seraphisissa osoitteesi on varustettu erilaisilla avaimilla, joilla voidaan tehdä erilaisia asioita:

  * Katsoa saapuvia lähtöjä, mutta piilottaa niiden arvo
  * Katsoa saapuvat lähtöjä, mutta näyttää niiden arvo
  * Katsoa lähtevät ulostulot
  * Auttaa sinua luomaan tapahtumia, mutta ei allekirjoittamaan niitä
  * Luo uusia osoitteita (hyödyllinen vähittäiskauppiaille tai monien asiakkaiden kanssa tapahtuville vaihdoille)

Osoitteen haltijana voit päättää, kuinka paljon valtuuksia annat muille laitteille tai kolmansille osapuolille.

## Kokonaiskuva

## Kokonaiskuva

Seraphis on merkittävä muutos Monero-ekosysteemiin. Vaikka se sisältää muutoksia osoitteisiin ja transaktioita rakentaviin lohkoihin, sen suunnittelu tarjoaa joustavuutta ja hyödyllisiä toimintoja, jotka eivät ole mahdollisia nykypäivän RingCT-protokollalla. Vaikka suuri osa suunnittelusta on viimeistelty ja sitä kehitetään [toteutukseksi](https://github.com/UkoeHB/monero/tree/seraphis_lib), osoitesuunnittelu ja suojausanalyysi ovat käynnissä. Seraphis tarjoaa erinomaisen mahdollisuuden viedä Monero-ekosysteemiä eteenpäin!

Lue lisää

  * [Kuinka Monero ainutlaatuisesti mahdollistaa kiertotaloudet](/knowledge/monero-circular-economies)/

  * [Moneron sormusallekirjoitukset vs CoinJoin kuten Wasabissa](/knowledge/ring-signatures-vs-coinjoin)/

  * [Miksi (ja miten!) sinun pitäisi hallita omia avaimiasi](/knowledge/hold-your-keys)/

  * [Osallistuminen Moneroon](/knowledge/contributing-to-monero)/

  * [Kuinka etäsolmut vaikuttavat Moneron yksityisyyteen](/knowledge/remote-nodes-privacy)/

  * [Kuinka Monero käyttää hard forkkeja verkon päivittämiseen](/knowledge/network-upgrades)/

  * [Katselutunnisteet: Kuinka yksi tavu vähentää Moneron lompakon synkronointiaikoja yli 40%](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool ja sen rooli Monero-louhinnan hajauttamisessa](/knowledge/p2pool-decentralizing-monero-mining)/

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

  * [Kuinka Monero ratkaisi Bitcoinia vaivaavan lohkokoko-ongelman](/knowledge/dynamic-block-size)/

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