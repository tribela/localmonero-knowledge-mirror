---
title: "Kuinka etäsolmut vaikuttavat Moneron yksityisyyteen"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Yksi Moneron suurimmista eduista muihin kryptovaluuttoihin verrattuna on sen lohkoketjun yksityisyys, mutta oletko koskaan miettinyt, kuinka Moneron yksityisyys säilyy, kun käytät etäsolmua? Entä jos käyttäisit "kevyt lompakko" -palvelinta, kuten MyMonero?

Tässä viestissä sukellamme joihinkin yksityiskohtiin liittyen siihen, miten Monero tarjoaa poikkeuksellista lohkoketjun yksityisyyttä myös käytettäessä etäsolmua, sekä mitä tulee huomioida käytettäessä etäsolmuja.

## Mitä toimintoa solmut palvelevat Monerossa?

Moneron toimintaan vähemmän perehtyneille tiedoksi; Monero-verkon solmuja (tai palvelimia) voi käyttää kuka tahansa ja sallia solmun omistajan (tai muiden, joiden kanssa he haluavat jakaa sen!) synkronoida lohkoketjun kopio ja toimittaa sen muille verkossa. Nämä solmut myös tarkistavat kaikki verkossa tapahtuvat transaktiot sekä kaikki julkaistut lohkot ja varmistavat, että ne kaikki noudattavat konsensuksen mukaisia sääntöjä.

Toinen toiminto jota solmut palvelevat Monerossa, on tapa tarjota kaikki tiedot, joita suosikki Monero-lompakkosi tarvitsee tarkistaakseen sinulle kuuluvat transaktiot ja tehdäkseen uusia transaktioita. Solmut tarjoavat nämä tiedot kahdella tavalla:

  * Lompakko pyytää tietoja jokaisesta lohkoketjun lohkosta, n skannataan sinulle kuuluvien transaktioiden varalta ja hylätään sitten, kun lompakko on tarkistanut ne. 
    * Tätä vaihetta parannetaan pian huomattavasti ["view tagien"](/knowledge/view-tags-reduce-monero-sync-time) ansiosta.
  * Kun lähetät transaktioita, käyttämäsi solmu tarjoaa luettelon mahdollisista houkuttimista (tai väärennetyistä syötteistä), joita voidaan käyttää transaktion rakentamiseen. Näin varmistetaan, että sinulla on hyvä joukko piiloutua joka kerta, kun käytät Moneroa. 
    * Nämä houkuttimet ovat osa [sormusallekirjoituksia](/knowledge/ring-signatures), joka on tärkeä osa Moneron lähestymistapaa ketjun yksityisyyteen.

  * Tätä vaihetta parannetaan pian huomattavasti ["view tagien"](/knowledge/view-tags-reduce-monero-sync-time) ansiosta.

  * Nämä houkuttimet ovat osa [sormusallekirjoituksia](/knowledge/ring-signatures), joka on tärkeä osa Moneron lähestymistapaa ketjun yksityisyyteen.

## Mikä on yksityisin ja turvallisin tapa käyttää Moneroa?

Paras asia tehdä, vaikka Monero tarjoaakin vahvan lohkoketjun yksityisyyden etäsolmuja käytettäessä, on käyttää omaa Monero-solmua varmistaaksesi, että sinulla on koskematon kopio Monero-lohkoketjusta ja että IP-osoitteesi on hyvin suojattu. Toinen etu, kun käytät omaa solmuasi on se, että voit osallistua takaisin verkkoon ja antaa muiden solmujen synkronoida solmuasi tai jopa antaa muiden käyttäjien muodostaa yhteyden solmuun lompakoillaan.

Monero tarjoaa silti erinomaisen yksityisyyden etäsolmua käytettäessä. Jos olet kiinnostunut oman Monero-solmun käyttämisestä, tässä on helppokäyttöinen opas sen tekemiseen:

  * [Aja Monero Nodea](https://sethforprivacy.com/guides/run-a-monero-node/)

## Mitä etäsolmu voi oppia minusta?

Etäsolmua käytettäessä muutama keskeinen tieto altistuu etäsolmulle ja on pari keskeistä tapaa, joilla solmu voi hyökätä kimppuun, estää transaktiosi ja paljon muuta.

Ensimmäinen asia, jonka etäsolmu voi oppia sinusta, on julkinen IP-osoitteesi. Vaikka tämä toivottavasti piilotetaan VPN:n tai Torin kautta, etäsolmu voi liittää julkisen IP-osoitteesi transaktion, mikä auttaa heitä rajaamaan, missä olet liikenteessä. Etäsolmu voi myös oppia viimeisimmän lohkon jossa lompakkosi sykronoitiin ja sen avulla yrittää tehdä valistuneita arvauksia sinusta, kuten milloin käytät normaalisti Moneroa ja milloin viimeksi käytit Moneroa. Tämä pätee erityisesti, jos tulet aina samasta IP-osoitteesta (kuten kotoa). Viimeinen avainasia, jonka etäsolmu voi oppia sinusta, on perustiedot sen kautta lähettämistäsi transaktioista. Vaikka tämä saattaa olla ilmeisin tieto, jonka etäsolmun operaattori saa sinusta, on tärkeää ymmärtää että tätä voidaan käyttää apuna transaktion lähettäjän jäljittämisessä, kun nämä tiedot yhdistetään muihin ketjun ulkopuolisiin tietoihin. Tämä voi olla erityisen vaarallista, jos etäsolmua pyörittää haitallinen taho, blockchain-analytiikkayritys tai sortava kansallisvaltio.

Etäsolmu voi myös yrittää aiheuttaa sinulle ongelmia piilottamalla lohkoja sinulta, jolloin lompakkosi luulee olleensa synkronoitu, vaikka se ei sitä ei ollut. Tämä voi saada sinut ajattelemaan, että varat ovat kadonneet tai estää sinua käyttämästä varoja ennen kuin muodostat yhteyden toiseen solmuun. Viimeinen avainasia, jonka etäsolmu voi tehdä, on syöttää lompakkoosi manipuloidun listan syöttejä. Tämä voi aiheuttaa sen, että lompakkosi ei pysty rakentamaan transaktioita kokonaan (jotta et pysty käyttämään varoja) tai se voi antaa etäsolmun yrittää tarjota syöttejä, joiden se tietää vähentäneen kussakin transaktiossa saamaasi anonymiteettiä.

## Mitä tietosuojatakuita on edelleen olemassa käytettäessä etäsolmua?

Vaikka tämä artikkeli on saattanut hieman pelottaa sinua, on tärkeää ymmärtää että Moneron tarjoama yksityisyys on erinomaista myös etäsolmua käytettäessä ja ylittää selvästi kaikki muut kryptovaluutat tällä tavalla käytettynä. Saat silti Moneron tarjoaman vahvan lohkoketjun yksityisyyden, koska etäsolmu ei koskaan tiedä todellista syötettä (mitä kolikoita käytät), transaktioon käytetyn Moneron määrää tai transaktion vastaanottajan osoitetta. Ulkopuoliset tarkkailijat eivät myöskään näe todellista syötettä, määrää tai osoitteita (riippumatta siitä, minkä tyyppisen solmun valitset!), mikä varmistaa, että etäsolmun ulkopuolella jopa IP-osoitteesi, lompakon synkronointitiedot ja transaktiot takaavat vahvan tietosuojan. 

Etäsolmulla ei myöskään ole koskaan pääsyä aikaisempiin lähettämiisi tai vastaanottamiisi transaktioihin tai lompakossasi olevaan Moneron määrään ja se menettää kaiken näkyvyyden transaktioihisi heti, kun alat käyttää toista solmua. Yksityisiä avaimia (joko kulutus- tai katseluavaimia) ei koskaan toimiteta etäsolmulle, joten lompakkosi pysyy yksityisenä, suojattuna ja käyttökelpoisena. Riippumatta etäsolmusta et ole koskaan vaarassa menettää Moneroa tai sen joutumista varkauden uhriksi, koska solmu ei voi muokata vastaanottajan osoitetta, sillä ei ole koskaan pääsyä lompakon yksityisiin avaimiin eikä se voi takavarikoida Moneroasi millään tavalla.

## Entä "kevyet lompakot", kuten MyMonero?

Vaikka aihe on hieman tämän artikkelin ulkopuolella, halusin kuitenkin käsitellä ainutlaatuista lompakkotyyppiä Monerossa – kevyitä lompakoita. Nimi "kevyt lompakko" tulee siitä, että lompakkosi (puhelimessa tai tietokoneessa) ei tarvitse suorittaa lohkoketjusynkronointia, mikä tekee kokemuksesta nopeamman ja sujuvamman.

Tällaisiin lompakoihin liittyy kuitenkin toistaiseksi vakava kompromissi yksityisyyden suojaan – lompakkosi lähettää yksityisen katseluavaimen käyttämällesi etäpalvelimelle (kuten MyMoneron oletuksena), jolloin etäpalvelin näkee kaikki vastaanotetut varat lompakkosi luomisesta lähtien (ja kunnes lopetat kyseisen lompakon tai seedin käytön). Tämä vähentää huomattavasti solmuoperaattorilta saamaasi yksityisyyttä, ja siihen tulee suhtautua varoen.

Onneksi Monero-yhteisö pyrkii parantamaan ohjelmistoa, jolla voit isännöidä omaa kevyttä lompakkopalvelintasi (LWS), mikä mahdollistaa nopean synkronoinnin luottamatta kolmanteen osapuoleen yksityisten katseluavaimiesi kanssa, koska kun ajat ohjelmiston, lompakkosi lähettää itse yksityiset katseluavaimet!

Lisätietoja mukautetusta kevyestä lompakkopalvelimesta on alla olevassa Githubin arkistossa:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Miten voin oppia lisää?

Jos olet utelias ja haluat ymmärtää paremmin Moneron solmuja ja harkita etäsolmun käyttöä tai omaa solmua, katso alla olevista linkeistä upeita aloituspaikkoja:

  * [Monero World, luettelo yhteisön ylläpitämistä etäsolmuista joita voidaan käyttää](https://moneroworld.com/#nodes)
  * [Monero-solmut, joita ylläpitää Seth For Privacy, tämän artikkelin kirjoittaja](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, luettelo etäsolmuista, joiden tila tarkistetaan usein< /a>](https://monero.fail/)
  * [Yhteyden muodostaminen GUI-lompakon etäsolmuun](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia - Etäsolmu](https://www.getmonero.org/resources/moneropedia/remote-node.html)

Lue lisää