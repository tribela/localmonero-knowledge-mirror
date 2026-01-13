---
title: "Moneron louhinta: Mikä tekee RandomX:stä niin erityisen?"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
30\. marraskuuta 2019 Monerolla oli puolivuosittainen "hard fork", ja odotetuin muutos oli siirtyminen vanhasta PoW-algoritmista, "cryptonight", täysin uuteen, sisäisesti kehitettyyn RandomX:ään. Monero-yhteisö uskoo, että RandomX on iso askel kohti tasa-arvoista louhintaa, mutta kaivataanpa syvemmälle, onko näin.

## Tarkoitus

Jotta voimme arvioida, onko RandomX parannus, meidän on ensin ymmärrettävä louhinnan tarkoitus. Louhinta turvaa lohkoketjun kaksinkertaisilta kuluilta Nakamoto Consensuksen kautta. Nämä tekniset tarkat yksityiskohdat eivät kuulu tämän artikkelin piiriin, mutta ne voidaan oppia monista eri lähteistä Internetissä. Tärkeää on, että tietoturva tulee tietokoneiden (louhijoiden) luomista hasheista, jotka kilpailevat keskenään löytääkseen matemaattisen ratkaisun, joka tarvitaan toisen lohkon luomiseen. Kun he tekevät tämän, he lisäävät uusia transaktioita lohkoketjuun. Vastineeksi työstään (hashista) he saavat korvauksen vasta luoduista kolikoista.   
  
Tämän järjestelyn yhteydessä voi esiintyä useita ongelmia, ja ne edellyttävät asianmukaisia kannustimia toimiakseen oikein, mutta keskitymme yhteen tiettyyn ongelmaan, joka saattaa syntyä tulevaisuudessa. Jos louhinnan oletetaan olevan kilpailu, mitä tapahtuu, kun yksi louhija saa edun?

## Tausta

Kontekstia varten puhutaan vähän louhintalaitteistosta. Louhijat käyttävät tietokoneita työhönsä, mutta me kaikki tiedämme että kaikkia tietokoneita ei ole valmistettu samalla tavalla. Jotkut tietokoneet ovat tarpeeksi tehokkaita suorittamaan tekoälyverkkoja tai intensiivisiä pelejä, kun taas toiset kamppailevat jopa yksinkertaisten tehtävien kanssa. Nämä erot laskentatehossa vaikuttavat myös hajautusnopeuteen tai nopeuteen, jolla he etsivät lohkoratkaisuja.   
  
Mutta jopa nämä erot tietokoneiden välillä haalistuvat erikoislaitteistojen, jotka tunnetaan myös nimellä Application Specific Integrated Circuits (ASIC) hajautusnopeudet, jotka ylittävät tavallisia tietokoneita useilla suuruusluokilla.  
  
Otetaan hetki ja tutkitaan, mikä tekee ASIC:ista niin tehokkaan.Kuvittele kaikki tietokoneet jossain spektrissä, joka vaihtelee kyvystä tehdä monia asioita yhtäaikaa, mutta ei mitään hyvin tai kyvystä tehdä vain yksi asia, mutta tekee sen erittäin hyvin. Prosessorit ja ASIC:t ovat tämän spektrin vastakkaisissa päissä.  
  
Prosessorit, jotka ovat kaikissa vakiotietokoneissa, ovat ensimmäisessä päässä. Ne voivat tehdä monia asioita, kuten selata verkkoa, pelata pelejä tai renderöidä videoita, mutta eivät tee mitään niistä erityisen hyvin. Mutta tämä joustavuus tulee tehokkuuden kustannuksella.  
  
ASIC:t ovat toisessa päässä, jossa ne voivat tehdä vain yhden asian, mutta tekevät sen uskomattomalla nopeudella. Ne voivat suorittaa vain yhden matemaattisen funktion, mutta koska he voivat jättää huomioimatta kaiken muun, suorituskyvyn lisäykset ovat tähtitieteellisiä. Tämä tehokkuus kuitenkin tulee joustavuuden kustannuksella, joten jos funktio muuttuu edes vähän – esimerkki on x + y = z muuttuu 2x + y = z:ksi – niin ASIC lakkaa toimimasta kokonaan.   
  
Kaikilla ei ole ASIC:ia, mutta kaikilla on omat tietokoneet. Tämä voi johtaa epäreiluun etulyöntiasemaan.

## Hauska analogia

Jos tämä on edelleen hämmentävää, ehkä seuraava analogia auttaa. Kuvittele lotto, jossa joka tunti palkitaan tuhat dollaria, ja tässä lotossa voit tulostaa omat lippusi! Aloitat tulostamaan niin monta lippua kuin voit tulostaa kotitulostimellasi, joka tulostaa yhden lipun sekunnissa. Kun vähennät sähkö- ja mustekustannukset voit silti ansaita voittoa, vaikka voittaisit lotossa vain muutaman viikon välein.  
  
Ajan myötä laajennat toimintaasi, kunnes sinulla on tulostimille omistettu kokonainen huone. 20 yhteensä. Kaikki on hyvin... yhteen kohtalokkaaseen päivään asti.  
  
Tulee suuria uutisia. Joku on keksinyt uudenlaisen tulostimen. Se voi tulostaa vain arpajaislippuja. Se ei voi tulostaa kuvia tai toimistoasiakirjoja tai tehdä kaksipuolista tulostusta. Vain lottolippuja. Mutta se voi tulostaa niitä nopeudella 1000 lippua sekunnissa. Katsot pieneen tulostinhuoneeseesi. 20 tulostinta. Tarvitset 980 tulostinta lisää pysyäksesi YHDEN hirviötulostimen vauhdissa, ja jos jollakulla on kaksi…?  
  
Poistut valitettavasti lotosta, koska et voi enää perustella sähkö- ja mustekustannuksia.  
  
Mutta odota! Parin viikon päästä tuleekin lisää uutisia! Lipun ulkoasu on muuttunut. Nyt numerot, jotka ennen olivat ylhäällä, ovat nyt alhaalla. Uudet hirviötulostimet ovat niin joustamattomia, etteivät he pysty siihen muutokseen. He pystyivät vain tekemään edellisen mallin. Ei kestä kauan, kun tulostat jälleen iloisena. Ainakin kunnes joku tekee uuden hirviötulostimen.

## RandomX

Miten RandomX sopii tähän kaikkeen? Se pyrkii tasoittamaan ASIC:ien etua tekemällä ASIC:ien tekemisestä erittäin vaikeaa. Se tekee tämän vaatimalla louhijoita tekemään ja suorittamaan satunnaista koodia algoritmiin perustuvan hajautuskoodin sijaan.  
  
Voi vaikuttaa hämmentävältä, kuinka tämä todella auttaa mihinkään, joten palataanpa tulostimen analogiaan. Muistatko mitä tapahtui, kun suunnittelu muuttui? Vanhat hirviötulostimet vanhenivat joka ilta ja uusia piti kehittää lipun uutta muotoilua silmällä pitäen. Mitä tapahtuisi, jos jokaisen uuden loton voittolipun täytyisi noudattaa uutta suunnittelustandardia jokaiselle uudelle jättipotille?   
  
Uuden hirviötulostimen luomisesta tulee uskomattoman vaikeaa. Et voi enää suunnitella vain yhtä lippumallia. Koska malli on satunnainen, hirviötulostimien valmistajien olisi lisättävä väriominaisuuksia, tapoja tulostaa erilaisia kirjaimia, reunuksia ja muotoja ja paljon muuta. Lyhyesti sanottuna kone, jonka he päätyivät keksimään, olisi tavallinen tulostin. Aivan kuten kaikki muutkin.  
  
Pelkästään toteuttamalla tämä satunnaisuus lippujen suunnittelussa pienensimme oleellisesti erikoislaitteistosta saatua suurta etua. RandomX tekee saman, mutta louhinnan kanssa.  
  
Tällä tavalla muutamien valittujen varakkaiden ihmisten saamat edut minimoidaan, sillä jos he investoivat "ASIC:iden" luomiseen RandomX:n louhintaa varten, he itse asiassa vain keksivät vahvempia ja parempia suorittimia, mikä hyödyttää koko maailmaa.  
[ X1455X] Tämä tarkoittaa, että pikkumies 20 lipputulostimensa kanssa on palannut peliin. Hänellä saattaa silti olla vaikeampaa, koska nämä varakkaat henkilöt voivat silti ostaa enemmän tulostimia kuin hän, mutta ainakaan nyt hän ei ole yltänyt suuruusluokkiin pelkästään yhdestä koneesta. Hän on kilpailukykyinen pienellä tavallaan.  
  
Tietäen, että pienikin kaveri voi olla kilpailukykyinen Moneron louhinnassa, rohkaisemme kaikkia kokeilemaan sitä joko Monero GUI -lompakossa, jossa on tuki yksinlouhintaan, tai lataamalla yhteisön ylläpitämiä ohjelmistoja. Se on helppoa, kilpailukykyistä ja kaikille avointa.

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

  * [Kuinka Monero ratkaisi Bitcoinia vaivaavan lohkokoko-ongelman](/knowledge/dynamic-block-size)/

  * [Kuinka CLSAG parantaa Moneron tehokkuutta](/knowledge/what-is-clsag)/

  * [Miksi Monerolla on "Tail Emission"](/knowledge/monero-tail-emission)/

  * [Moneron lyhyt historia](/knowledge/monero-history)/

  * [Wired Magazine on väärässä Monerosta, tässä miksi](/knowledge/wired-article-debunked)/

  * [15 parasta Monero-myyttiä ja -huolia, jotka on kumottu](/knowledge/monero-myths-debunked)/

  * [Kuinka Dandelion++ pitää Moneron tapahtuman alkuperän yksityisenä](/knowledge/monero-dandelion)/

  * [Miksi Monero on avoimen lähdekoodin ja hajautettu](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Miksi Monero on parempi kuin Dash, Zcash, Zcoin (jopa Lelantuksen kanssa), Grin ja Bitcoin-mikserit kuten Wasabi (päivitetty toukokuussa 2020)](/knowledge/why-monero-is-better)/