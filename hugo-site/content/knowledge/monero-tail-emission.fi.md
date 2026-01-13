---
title: "Miksi Monerolla on \"Tail Emission\""
slug: "monero-tail-emission"
date: "2020-07-30"
image: "/images/emission.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Kun useimmat ihmiset ajattelevat sitä, mikä erottaa Moneron muista, he ajattelevat Moneron tietosuojatekniikkaa. Itse asiassa useimmat pitävät yksityisyyttä ja sen vapauttamaa vaihdettavuutta Moneron määrittävänä ominaisuutena ja tärkeimpänä aseena, jonka se tuo kehään muihin kolikoihin verrattuna. Useimmat ihmiset eivät ehkä tiedä, että Monero sisältää muita protokollaeroja Bitcoinista ja sen johdannaisista, joiden jotkut saattavat väittää olevan yhtä tärkeitä kuin Moneron tietosuojatekniikat. Tässä artikkelissa tarkastelemme yhtä näistä: "Tail emission".

Määritetään ensin, mitä tämä termi tarkoittaa. Tail emissio on lakkaamaton tuki lohkopalkkioille, jopa sen jälkeen, kun "viimeinen" Monero on louhittu. Toisin sanoen Moneron lohkopalkkio ei koskaan putoa nollaan, vaan laskee, kunnes se saavuttaa 0,6 XMR:ää lohkoa kohden, ja pysyy sitten siellä ikuisesti. Louhijoille maksetaan aina palkkaa Moneron louhimisesta, eikä heidän koskaan tarvitse luottaa pelkästään maksumarkkinoihin.

Mutta mennään hetkeksi taaksepäin ja katsotaan louhimistoimintaa erittäin korkealla tasolla. Monero-louhijoita kannustetaan turvaamaan verkko hashien louhinnalla. Kannustimena on mahdollisuus tehdä Moneroa, jos he löytävät uuden lohkon. Tämä Monero palkitaan kahdella tavalla. Ensinnäkin louhija saa maksetut maksut jokaiselta käyttäjältä, joka maksoi tapahtumansa sisällyttämisestä lohkoon. Nämä ovat transaktiomaksuja, jotka maksat, kun lähetät transaktion. Toiseksi louhija saa ennalta määrätyn määrän Moneroa itse protokollasta. Useimmissa tapauksissa tämä "lohkopalkkio" on huomattavasti korkeampi kuin käyttäjän transaktiomaksut, ja niillä louhijat tienaavat eniten. Tämä lohkopalkkio auttaa pitämään louhijat taloudellisesti kiinnostuneina ketjun turvallisuudesta, mutta myös saamaan liikkeelle uusia kolikoita.

Useimmissa kryptovaluuttaprotokollissa tämä lohkopalkkio on asetettu pienenemään ajan myötä. Useimmilla Bitcoin-johdannaisilla on ns. puolittuminen, ennalta määrätyt ajankohdat, jolloin lohkopalkkio puolittuu (kuten 20 BTC:stä 10 BTC:hen). Nämä puolittumiset tapahtuvat muutaman vuoden välein, ja joka kerta kun se tapahtuu, verkon turvallisuus heikkenee. Miksi? Kannustamme lukijaa lukemaan [-artikkelimme louhinnasta ja RandomX](/knowledge/monero-mining-randomx):stä, ja näin tehdessään he oppivat, että louhinta on kilpailua. Lohkopalkintoja jaetaan vain niille jotka löytävät lohkon, ja monet tahot kilpailevat siitä. Kun palkinnot ovat korkeammat, useammat ihmiset ovat kiinnostuneita pelaamaan tätä peliä, kun taas kun palkinnot ovat alhaiset, vähemmän ihmisiä on valmiita käyttämään aikaansa ja resurssejaan voittaakseen vähäisen voiton.

Alamme jo raapia Moneron Tail emission syytä. Monerolla on myös laskeva lohkopalkkio, vaikka toisin kuin Bitcoinissa, siinä ei ole puoliintumista. Sen sijaan jokainen lohkopalkkio on pienen summan pienempi kuin edellinen, joten vähennys on paljon tasaisempaa. Mutta kysymys kaikille kryptovaluutoille on: "Mitä tapahtuu, kun lohkopalkkio osuu nollaan?" Tämä on outo tilanne, jossa me sekä tiedämme että emme tiedä vastausta. Tiedämme, että lohkopalkkiotukea ei enää tule, mikä tarkoittaa, että louhijoita on kannustettava pelkästään käyttäjämaksuilla. Emme tiedä, ovatko nämä määrät riittävät pitämään louhijat varmistamassa ketjua.

Kuten aiemmin mainittiin, tällä hetkellä lohkopalkkio ylittää transaktiomaksut huomattavalla summalla, joten toivotaan, että kun yhä useammat käyttäjät käyttävät ketjua, maksut nousevat ja korotettujen maksujen myötä louhijat pitävät louhimista kannattavana. Tällä skenaariolla on kuitenkin toinen puoli, käyttäjien puoli. Jos maksut nousevat, kryptovaluuttakaupan tekemisestä tulee paljon kalliimpaa kaikille, mikä saattaa eristää sen niiltä, joilla ei ole riittäviä resursseja. Mutta toisaalta, jos maksut pysyvät alhaisina ja lohkopalkkio jää nollaan, hyvin harvat louhijat suojaavat verkkoa, mikä jättää sen alttiiksi 51% hyökkäyksille ja käänteisille transaktiolle.

Kenelläkään ei ole hyviä vastauksia tähän skenaarioon, eikä mikään suuri kolikko ole vielä päässyt kryptovaluuttansa elämän tähän vaiheeseen, joten meillä ei ole myöskään todellista kokemusta siitä. Kaikki on spekulaatiota. Arpapeliä. Bitcoin lyö vetoa, että maksut riittävät louhijoiden elättämiseen, vaikka se tarkoittaisi köyhien sulkemista pois. Monero tekee toisenlaisen vedon. Monero vetoaa, että maksut eivät yksin riittäisi ketjun turvallisuuteen, joten se sisältää Tail emission osana protokollaa.

Muistutamme lukijaa, että lohkopalkkio ei koskaan laske alle 0,6 XMR:tä lohkoa kohden. Riittääkö tämä louhijoiden kannustamiseen? Emme tiedä, mutta se on varmasti parempi kuin 0, mitä melkein kaikki muut valuutat ovat sisällyttäneet protokollaan.

Tälle lähestymistavalle kohdistettu pääasiallinen kritiikki on se, että tämä tarkoittaa, että Moneron tarjonta on teoriassa ääretön, mikä aiheuttaa inflaatiota ajan myötä, kun taas lohkopalkkion rajoittavilla kolikoilla on rajallinen tarjonta, ja niiden niukkuus lisää arvoa ajan myötä. Mielestämme tämä argumentti on riittämätön useista syistä.

Ensinnäkin, mitä hyötyä on vähäisestä, arvokkaasta kolikosta, johon on helppo hyökätä, se on sensuroitu ja kaatuu heikon turvallisuuden vuoksi? Alhainen turvallisuus alentaisi arvoa, enemmän kuin niukkuus sitä lisäisi. Toiseksi, vaikka Moneron tarjonta on teoriassa ääretön, inflaatio on lineaarinen ja suuntautuu kohti nollaa vuotuisena prosenttiosuutena, toisin kuin fiat, jonka inflaatio on eksponentiaalinen.

Moneron inflaatio tiedetään tarkasti etukäteen ja se voidaan ennustaa tarkasti, toisin kuin fiatin, joka voi nousta enemmän tai vähemmän tiettynä vuonna vallitsevien voimien mielijohteesta riippuen. Monero säilyttää edelleen cyberpunk-hengen, joka poistaa inhimillisen korruption mahdollisuuden protokollavalvontatekniikan avulla. Lisäetu on mielenrauha, että Moneron lohkoketjun suoja louhinnan kautta on olemassa niin kauan kuin maailma tarvitsee sitä.

Viimeinen asia jota haluamme käsitellä, on oikeudenmukaisuus. Rahaa käytetään monella tapaa, arvon säilyttäjänä, vaihtovälineenä ja laskentayksikkönä. Järjestelmässä jossa tarjonta on rajallinen, inflaatio pysähtyy, mikä tarkoittaa että ne, jotka käyttävät sitä arvon säilyttäjänä, käyttävät järjestelmää ilmaiseksi. He hyötyvät louhijoiden tarjoamasta jatkuvasta turvallisuudesta maksamatta siitä mitään, koska ilman inflaatiota heidän rahansa eivät menetä arvoaan hitaasti ajan myötä. Sitä vastoin jokainen joka käyttää valuuttaa vaihtovälineenä, saa rangaistuksen (mahdollisesti korkeiden transaktiomaksujen kautta). Tämä rohkaisee ihmisiä pitämään, mutta ei kuluttamaan, ja vääristää järjestelmän oikeudenmukaisuutta haltijoille. Tail emissio tasoittaa tämän yhtälön. Nyt haltijat maksavat myös pienen veron inflaation kautta järjestelmän turvallisuudesta. Tail emissio tekee siitä oikeudenmukaisempaa kaikille.

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

  * [Moneron lyhyt historia](/knowledge/monero-history)/

  * [Wired Magazine on väärässä Monerosta, tässä miksi](/knowledge/wired-article-debunked)/

  * [15 parasta Monero-myyttiä ja -huolia, jotka on kumottu](/knowledge/monero-myths-debunked)/

  * [Kuinka Dandelion++ pitää Moneron tapahtuman alkuperän yksityisenä](/knowledge/monero-dandelion)/

  * [Miksi Monero on avoimen lähdekoodin ja hajautettu](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Moneron louhinta: Mikä tekee RandomX:stä niin erityisen?](/knowledge/monero-mining-randomx)/

  * [Miksi Monero on parempi kuin Dash, Zcash, Zcoin (jopa Lelantuksen kanssa), Grin ja Bitcoin-mikserit kuten Wasabi (päivitetty toukokuussa 2020)](/knowledge/why-monero-is-better)/

Lue lisää