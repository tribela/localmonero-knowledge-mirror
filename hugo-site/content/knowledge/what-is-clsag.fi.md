---
title: "Kuinka CLSAG parantaa Moneron tehokkuutta"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero on protokolla, joka on jatkuvassa kehityksessä. Monero-yhteisö tutkii sekä on-chain että off-chain-ratkaisuja etsien kehityskohteita, joiden avulla Monero voidaan tehdä entistä yksityisemmäksi, skaalautuvammaksi ja saataville kaikille. Yksi viimeaikaisista innovaatioista on linkitettävän sormusallekirjoitusjärjestelmän MLSAG:n korvaaminen drop-in-korvikkeella CLSAG:lla (Concise Linkable Spontaneous Anonymous Group), joka tekee Monerosta entistä yksityisemmän.

CLSAG:n toteutuksen takia yleisimpien 2 syötteen, 2 tulon siirtojen määrä vähenee 25%. Myös vahvistusajan odotetetaan vähenevän 10%. CLSAG:n toteutuksen tavoitteena on tehdä Monero-protokolla entistä yksityisemmäksi ja nopeammaksi.

Mutta mikä CLSAG oikeastaan on? Mitä se tekee ja miten se eroaa vanhasta MLSAG:sta? Otetaan hetki aikaa muistellaksemme, miksi ja miten sormusallekirjoitukset toimivat, jotta ymmärrämme tämän konseptin paremmin. Sormusallekirjoitukset mahdollistavat ei-välittömät, todistajilta erottamattomat syötteet käyttämällä allekirjoittajan valitsemia anonymiteettijooukkoja aiempien tulojen perusteella. Sanallisesti selitettynä sormusallekirjoitus mahdollistaa käyttäjän piilottaa siirtoonsa käytetyt tulot muiden tulojen joukkoon ilman, että muita osapuolia tarvitaan. Tarvitaan vain kopio lohkoketjusta. Nämä tulos näyttävät yleensä yhtä todennäköisiltä oikeana lähetettävänä, mikä piilottaa lähettäjän metadataa. 

Tämä aiheuttaa kuitenkin hieman ongelmaa. Mitä jos käyttäjä rakentaisi sormusallekirjoituksen, jossa kaikki decoy-tulot ovat mukana? Miten kukaan tietäisi, että tuntemattomalla lähettäjällä ei ole oikeutta lähettää mitään näsitä? Voisiko tämä käyttäjä kuluttaa tekaistua rahaa? Vastaus on ei. Sormusallekirjoitus sisältää menetelmän, jolla osoitetaan, että ainakin yhden tulojen joukosta omistaa tuntematon lähettäjä, ilman että se paljastaa, mitkä tulot ne ovat. CLSAG ja MLSAG (tästä eteenpäin SAG:t) ovat osa sormusallekirjoitusta, joka todistaa tämän. Mielenkiintoisesti samalla ne todistavat, että siirron määrä, vaikka se on piilotettu salaisiin siirtoihin (RingCT), tasapainottuu. SAG:it todistavat kahta asiaa, että yksi tulo kuuluu jollekin sormusallekirjoituksen osapuolelle ja että siirto tasapainottuu, on tärkeää ja oiekastaan siinä piilee myös koon ja vahvistusajan säästöt. Jos tämä alkaa tuntua sekavalta, älä huoli, saamme pian esimerkin jonka avulla asia tulee helposti ymmärretyksi.

Vanha allekirjoitusmalli MLSAG (Multilayered Linkable Spontaneous Anonymous Group) todistaa edellä mainitut kaksi asiaa sormusallekirjoituksessa, mutta tekee molemmat erikseen. Erillisten laskentojen käyttö allekirjoitus- ja sitoutumisavaimille tarkoittaa hitaampia operaatioita. Moderni tietokone voi suorittaa nämä laskutoimitukset muutamassa millisekunnissa, mikä ei kuulosta paljolta, ja todellakin yhden siirron kohdalla se ei olekaan. Kun huomioidaan Moneron lohkoketjun siirtojen määrä ja se, että lohkoketjusta alusta alkaen synkronoiva solmu joutuu lataamaan ja vahvistamaan jokaiset siirrot, tavut ja millisekunnit alkavat kasvaa nopeasti. CLSAG (Concise Linkable Spontaneous Anonymous Group) on uusi signatuurijärjestelmä, joka yhdistää nämä kaksi todistamista yhdeksi laskennaksi parantaakseen Moneron suorituskykyä ja tehokkuutta verrattuna MLSAG:hen.

CLSAG yhdistää tarvittavat matemaattiset laskutoimitukset molempien todistamiseen yhdeksi laskuksi ja suorittaa ne samanaikaisesti turvallisella tavalla. Mitä turvallinen tavoittelu tarkoittaa? No, selventääksemme asian ja toivottaaksemme samalla koko asian selvemmäksi, tutustutaan luvattuun hauskaan analogiaan.

Oletetaan, että sinun täytyy mennä sekä ruokakauppaan että rautakauppaan hakemaan kaksi eri asiaa: ruokaa ja myrkyllisiä puhdistuskemikaaleja. Et halua niiden sekoittuvan, sillä jos tapahtuu onnettomuus, kemikaalit roiskuvat ruoan päälle, jolloin ne eivät kelpaa. Päätät olla erittäin turvassa ja ajaa talostasi ruokakauppaan, ostaa ruokaa ja sitten ajaa takaisin kotiisi. Vasta kun olet purkanut ruuat, nouset takaisin autoon, ajat rautakauppaan ja takaisin kotiisi kemikaalien kanssa. Olet tehnyt kaksi erillistä matkaa varmistaaksesi kaikkien ostosten turvallisuuden. Vaikka se on todella turvallista, se on tehotonta. Tämä edustaa MLSAG:ta, johon tallennetaan kaksi erilaista matematiikkajoukkoa ja tehdään kaksi erilaista "matkaa" niiden laskemiseksi.

Päätät kuitenkin, että haluat tehdä tämän nopeamman tavan. Se on liikaa hukattua aikaa. Sen tekeminen kerran tai kahdesti ei tietenkään kaada elämääsi, mutta kun joudut tekemään tämän yhä uudelleen, tuntimäärät alkavat kasvaa. Alat miettimään, voitko tehdä yhden matkan sen sijaan. Kotoa, ruokakauppaan, rautakauppaan ja takaisin kotiin. Et voi vain mennä ja heittää kaikkea autoon sattumanvaraisesti. Se ei ole turvallista. Sen sijaan määrität autossasi eri paikkoja eri asioille ja varmistat, että kaikki mahtuu siististi paikoilleen. Näin voit tehdä turvallisesti yhden matkan molempiin liikkeisiin ja pitää tavarat poissa toisistaan. Tämä edustaa CLSAG:tä. Tähän tapahtumaan on nyt tallennettu vain yksi matematiikka näiden kahden asian todistamiseksi, ja se on tehty poispäin, etteivät ne häiritse toisiaan. Matka on vielä tehtävä, mutta olet vähentänyt niiden määrää melko rajusti.

Kaikki tämä kuulostaa melko jännittävältä. Onko mahdollista, että löydämme muita pikakuvakkeita tai muita tapoja säästää aikaa ja tilaa? Vastaus on kyllä ja ei. Nykyisten MRL-tutkijoiden mukaan SAG-tyyppisiä rakenteita ei todennäköisesti ole mahdollista muokata lisää koon tai nopeuden parantamiseksi; kuitenkin muut rakenteet, kuten Arcturus, Omniring, RCT3 tai Triptych, tuottavat paljon parempia koon skaalaus- ja varmennusetuja käyttämällä erilaisia matemaattisia menetelmiä. Jokaisella näistä "seuraavan sukupolven" lähestymistavoista allekirjoittajien moniselitteisiin protokolliin liittyy kuitenkin omat kompromissinsa toteutuksen yksityiskohdissa, ja niitä tutkitaan aktiivisesti.

Loppujen lopuksi Monero on aina innovoiva.

Lue lisää

  * [Kuinka Monero ainutlaatuisesti mahdollistaa kiertotaloudet](/knowledge/monero-circular-economies/)

  * [Moneron sormusallekirjoitukset vs CoinJoin kuten Wasabissa](/knowledge/ring-signatures-vs-coinjoin/)

  * [Miksi (ja miten!) sinun pitäisi hallita omia avaimiasi](/knowledge/hold-your-keys/)

  * [Osallistuminen Moneroon](/knowledge/contributing-to-monero/)

  * [Kuinka etäsolmut vaikuttavat Moneron yksityisyyteen](/knowledge/remote-nodes-privacy/)

  * [Kuinka Monero käyttää hard forkkeja verkon päivittämiseen](/knowledge/network-upgrades/)

  * [Katselutunnisteet: Kuinka yksi tavu vähentää Moneron lompakon synkronointiaikoja yli 40%](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool ja sen rooli Monero-louhinnan hajauttamisessa](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Mitä se tekee Monerolle](/knowledge/seraphis-for-monero/)

  * [Onko Bitcoinin muuntaminen Moneroksi yhtä yksityistä kuin Moneron ostaminen suoraan?](/knowledge/most-private-way-to-buy-monero/)

  * [Miksi Monero käyttää "Trustless" -asetusta toisin kuin Zcash](/knowledge/monero-trustless-setup/)

  * [Miksi Monero on parempi arvon säilyttäjä kuin Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Kuinka Monero voi voittaa Bitcoinin verkkovaikutukset](/knowledge/network-effect/)

  * [Miksi Monerolla on kriittisin ajatteluyhteisö](/knowledge/critical-thinking/)

  * [Huijaukset, joita kannattaa huomioida Moneroa käytettäessä](/knowledge/monero-scams/)

  * [Kuinka Atomic Swapit toimivat Monerossa](/knowledge/monero-atomic-swaps/)

  * [Mitä jokaisen Moneron käyttäjän on tiedettävä verkostoitumisesta](/knowledge/monero-networking/)

  * [Kuinka RingCT piilottaa Monero-transaktiosummat](/knowledge/monero-ringct/)

  * [Kuinka Monero Stealth -osoitteet suojaa identiteettiäsi](/knowledge/monero-stealth-addresses/)

  * [Kuinka Monero-aliosoitteet estävät identiteetin yhdistämisen](/knowledge/monero-subaddresses/)

  * [Moneron Outputit selitettynä](/knowledge/monero-outputs/)

  * [Moneron parhaat käytännöt aloittelijoille](/knowledge/monero-best-practices/)

  * [Kuinka sormusallekirjoitukset sekoittavat Moneron outputit](/knowledge/ring-signatures/)

  * [Kuinka Monero ratkaisi Bitcoinia vaivaavan lohkokoko-ongelman](/knowledge/dynamic-block-size/)

  * [Miksi Monerolla on "Tail Emission"](/knowledge/monero-tail-emission/)

  * [Moneron lyhyt historia](/knowledge/monero-history/)

  * [Wired Magazine on väärässä Monerosta, tässä miksi](/knowledge/wired-article-debunked/)

  * [15 parasta Monero-myyttiä ja -huolia, jotka on kumottu](/knowledge/monero-myths-debunked/)

  * [Kuinka Dandelion++ pitää Moneron tapahtuman alkuperän yksityisenä](/knowledge/monero-dandelion/)

  * [Miksi Monero on avoimen lähdekoodin ja hajautettu](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Moneron louhinta: Mikä tekee RandomX:stä niin erityisen?](/knowledge/monero-mining-randomx/)

  * [Miksi Monero on parempi kuin Dash, Zcash, Zcoin (jopa Lelantuksen kanssa), Grin ja Bitcoin-mikserit kuten Wasabi (päivitetty toukokuussa 2020)](/knowledge/why-monero-is-better/)