---
title: "P2Pool ja sen rooli Monero-louhinnan hajauttamisessa"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Yksi Monero-projektin ydintavoitteista on mahdollistaa oikeudenmukainen, hajautettu ja turvallinen verkko uusien ja innovatiivisten lähestymistapojen avulla proof-of-work (PoW) -louhimistoimintaan, mikä on tärkein tapa, jolla kryptovaluuttaverkot suojataan nykyään. 

Vaikka ainutlaatuinen louhinta-algoritmi [, kuten RandomX](/knowledge/monero-mining-randomx) on äärimmäisen tärkeä tälle tavoitteelle auttauessaan varmistamaan että kuka tahansa, jolla on tietokone, voi osallistua kohtuullisesti verkon turvallisuuteen, RandomX ei ratkaise ongelmia, jotka voivat johtua poolin louhinnasta. Poolin louhinta on ylivoimaisesti yleisin tapa louhia kryptovaluuttoja nykyään, mukaan lukien Moneroa, mutta onneksi p2poolin louhinta muuttaa tätä nopeasti.

## Mitä on poolin louhinta?

## Mitä on poolin louhinta?

Poolin louhinta on tapa, jolla louhijat voivat jakaa tehtävän ratkaista verkon lohko ja jakaa sitten palkinnot tasaisesti kaikille poolin löytämille lohkoille. Vaikka tämä auttaa valtavasti tasoittamaan louhijoiden palkkaustiheyttä verrattuna yksin Moneron louhintatoimintaan, se ei tule ilman vakavia keskittämisongelmia.

Kun jokainen louhija tekee työtä pooliin, he luopuvat tekemästään työskentelyn ja löytämistään lohkojen hallinnasta itse poolille, luottaen siihen että pooli jakaa palkinnot rehellisesti ja oikeudenmukaisesti kaikkien työtä tehneiden louhijoiden kesken. Jos kaikki menee hyvin, poolin ylläpitäjä kerää työt kaikilta louhijoilta, lähettää ne verkkoon ja jakaa palkinnot tasan.

## Mikä ongelma poolin louhinnassa on?

## Mikä ongelma poolin louhinnassa on?

Valitettavasti tämä perustuu täysin luottamukseen ja sallii poolin operaattorin tehdä ilkeitä asioita louhijoiden työssä. Poolin operaattori voisi käyttää tekemää työtä hyökätäkseen verkkoon, yrittää kaksinkertaistaa varoja (jos pooli on tarpeeksi suuri) tai yksinkertaisesti käyttää louhijoiden tekemää työtä maksaakseen itselleen eikä koskaan palkita louhijoita kunnolla heidän työstään. 

Suurin riski verkkoon on pooli (tai useat yhdessä toimivat poolit), joiden hallinnassaan on yli 51% verkon hashratesta, koska he voivat käyttää tätä huijaamiseen ja varojen käyttämiseen kahdesti (tuplakulutus) tai yrittää muuttaa verkon sääntöjä.

## Mikä on p2pool?

## Mikä on p2pool?

p2pool on konsepti, joka luotiin alun perin Bitcoinin louhintaan vuonna 2011, mutta jota ei koskaan otettu laajalti käyttöön ja se on käytännössä käyttämätön Bitcoinissa. Onneksi yksi RandomX:n avainkehittäjistä, SCHernykh, vietti lomansa keksiäkseen ratkaisuja joihinkin p2poolin Bitcoin-toteutukseen liittyviin ongelmiin ja kirjoittamalla kaikki ohjelmistot uudelleen alusta.

p2pool Monerossa mahdollistaa louhijoille täysin luottamattoman tavan työskennellä yhdessä lohkojen ratkaisemiseksi ja Monero-verkon turvaamiseksi käyttämällä erityistä solmuohjelmistoa p2poolille työn jakamiseksi.

Tämä tehdään käyttämällä uutta lohkoketjua ("sivuketjua"), joka pitää kirjaa kunkin louhijan tekemästä työstä, lompakko-osoitteestaan ja siitä, kuinka paljon Moneroa hän on ansainnut ja maksaa sitten palkkion rahastoon. Koska tässä sivuketjussa on paljon vähemmän kaivostyöntekijöitä, siitä on paljon helpompi löytää ja lähettää lohkoja kuin Monero-pääverkossa, mikä tekee louhijoille helpommaksi saada johdonmukaisia maksuja verrattuna Moneron louhintaan.

## Miten p2pool ratkaisee poolin louhinnan ongelmat?

## Miten p2pool ratkaisee poolin louhinnan ongelmat?

P2poolissa ei ole keskitettyä poolia, keskitettyä poolioperaattoria tai yksittäistä henkilöä, joka pitää hallussaan varoja ja jakaa maksuja. P2poolin lohkoketju ja muut solmuoperaattorit tarkastavat louhijoiden kollektiivisesti tekemän työn p2poolin kautta varmistaakseen sen laillisuuden, ja kaikille louhijoille maksetaan heidän tekemänsä työn mukaan välittömästi palkinnot suoraan lohkosta, kun lohko löytyy.

Kun louhijat päättävät käyttää p2poolia keskitetyn poolin sijaan, he poistavat kaiken vallan ja luottamuksen poolin operaattoreilta ja varmistavat, että heidän työnsä edistää verkon etua ja omia palkintojaan, sekä vähentää verkkohyökkäysten ja väärinkäytösten riskiä.

Tämä ei ainoastaan auta heitä suojelemaan omia etujaan, vaan se vähentää riskiä, jonka keskitetyt poolit voivat aiheuttaa Monero-verkolle kokonaisuudessaan. P2poolin käyttö auttaa myös vähentämään huomattavasti riskiä, jonka kansallisvaltiot tai sääntelyviranomaiset voivat aiheuttaa verkon terveydelle, koska siellä ei ole keskitettyjä poolien operaattoreita, joita painostaa, ei ole maantieteellistä keskittymää poolien varaan tai muita helppoja painepisteitä, joita he voivat käyttää Moneroa vastaan.

## Mitä ovat haitat?

## Mitä ovat haitat?

Onneksi p2pool Monerossa on hyvin suunniteltu ja hyvin rakennettu, ja se toimii erittäin hyvin! P2poolin louhinnan suurin haittapuoli on kuitenkin se, että jokaisen louhijan, joka haluaa käyttää p2poolia, on käytettävä omaa Monero-solmuaan, mikä tekee osallistumisen alkuprosessista hieman työläämpää. Tämän solmun avulla lasketaan kuitenkin sitten kaikki lohkojen rakentamiseen ja tarkistamiseen tarvittavat tiedot, ja varmistetaan että louhija hallitsee itse täysin työtään. Solmu voi toimia myös etäsolmuna louhijoiden omalle lompakolle, edistää verkkoa ja paljon muuta.

Toinen keskeinen ero keskitettyyn louhintaan on se, että p2poolia käyttävillä pienillä louhijoilla on hieman enemmän "varianssia" eli maksujen välistä aikaa kuin suurella keskitetyllä poolilla – mutta se' on _äärimmäisen_ tärkeää huomata, että tämä ei johda ansaitsemaan vähemmän Moneroa ajan myötä! P2pool on ajan mittaan yhtä kannattava pienillekin louhijoille kuin keskitetyt poolit. Osa tästä vaihtelusta kompensoituu myös sillä, että p2poolin natiivikulut ovat 0%, koska keskitetty poolioperaattori ei maksa palveluistaan!

## Miten pääsen alkuun?

## Miten pääsen alkuun?

Onneksi Moneron' p2pool-toteutuksen erinomaisen suunnittelun ja monien yhteisön ihmisten ansiosta, jotka ovat käyttäneet aikaa auttaakseen louhintaprosessia yksinkertaistamaan p2poolin kautta, aloittaminen helpottuu ajan myötä. On olemassa useita tapoja aloittaa louhiminen p2poolin avulla, mutta koska tekniset yksityiskohdat eivät kuulu tämän artikkelin piiriin, voit siirtyä alla olevaan linkkiin käyttöjärjestelmästäsi riippuen:

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## Miten voin oppia lisää?

## Miten voin oppia lisää?

Jos tämä on herättänyt uteliaisuutesi p2poolin louhimisesta, katso alta lisää linkkejä ja selityksiä p2poolista, miten se toimii ja mitä se tarkoittaa Monerolle:

  * [P2poolin virallinen Github](https://github.com/SChernykh/p2pool)
  * [Viralliset asiakirjat p2poolin käytöstä](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool on nyt live-tilassa](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, eräänlainen "lohkotutkija" p2poolille](https://p2pool.observer/)
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [ Sergei Chernykh: P2Poolin hajautetun XMR-kaivospoolin kehittämisestä](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

Lue lisää

  * [Kuinka Monero ainutlaatuisesti mahdollistaa kiertotaloudet](/knowledge/monero-circular-economies)/

  * [Moneron sormusallekirjoitukset vs CoinJoin kuten Wasabissa](/knowledge/ring-signatures-vs-coinjoin)/

  * [Miksi (ja miten!) sinun pitäisi hallita omia avaimiasi](/knowledge/hold-your-keys)/

  * [Osallistuminen Moneroon](/knowledge/contributing-to-monero)/

  * [Kuinka etäsolmut vaikuttavat Moneron yksityisyyteen](/knowledge/remote-nodes-privacy)/

  * [Kuinka Monero käyttää hard forkkeja verkon päivittämiseen](/knowledge/network-upgrades)/

  * [Katselutunnisteet: Kuinka yksi tavu vähentää Moneron lompakon synkronointiaikoja yli 40%](/knowledge/view-tags-reduce-monero-sync-time)/

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

  * [Moneron louhinta: Mikä tekee RandomX:stä niin erityisen?](/knowledge/monero-mining-randomx)/

  * [Miksi Monero on parempi kuin Dash, Zcash, Zcoin (jopa Lelantuksen kanssa), Grin ja Bitcoin-mikserit kuten Wasabi (päivitetty toukokuussa 2020)](/knowledge/why-monero-is-better)/

Lue lisää