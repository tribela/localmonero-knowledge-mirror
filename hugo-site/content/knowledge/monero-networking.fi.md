---
title: "Mitä jokaisen Moneron käyttäjän on tiedettävä verkostoitumisesta"
slug: "monero-networking"
date: "2020-11-11"
image: "/images/networking.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Sen ei pitäisi tulla kenellekään yllätyksenä, että Monero ja itse asiassa kaikki kryptovaluutat toimivat Internetissä. Ja silti, vaikka tämä lausunto näyttää perustavanlaatuiselta ja ilmeiseltä, monet eivät ota huomioon mitä tämä tarkoittaa heidän yksityisyytensä suhteen. Toisin sanoen on olemassa asioita, joilta Monero voi ja ei voi suojautua, vain Internetissä olemisen vuoksi. Jotkut näistä näkökohdista ovat pelkkiä pieniä haittoja, kun taas toiset ovat paljon vakavampia tilanteessa, jossa vaaditaan ehdotonta yksityisyyttä. Otetaan aikaa tutustuaksemme siihen, kuinka Monero-käyttäjät ovat vuorovaikutuksessa keskenään verkossa ja mitä tämä tarkoittaa heidän yksityisyytensä kannalta.

Asioiden triviaalilta puolelta alkaen, jos käyttäjällä ei ole pääsyä Internetiin, hän ei voi ladata uusia lohkoja, levittää transaktioita muiden puolesta tai lähettää omia transaktioita. Mielenkiintoinen asia on huomata, että käyttäjä jolla on täydellinen solmu ilman Internet-yhteyttä, voi rakentaa transaktion offline-tilassa, joka voidaan lähettää myöhemmin. Tämä johtuu siitä, että sormusallekirjoitus tarvitsee vain ulostulot lohkoketjusta piiloutuakseen. Lyhyt muistutus [sormusallekirjoitusten toiminnasta](/knowledge/ring-signatures), se piilottaa käyttäjän lähettämän todellisen lähdön menneisyydestä valittujen liittämättömien tulosteiden joukosta. Jos käyttäjällä on pääsy näihin lähtöihin täysin ladatun lohkoketjun (täysi solmu) muodossa, hän voi luoda sormuksen aiemmista lähdöistä, ja kun Internet-yhteys palautuu, siirtää transaktio verkkoon.

Etäsolmua käyttävä käyttäjä ei voi tehdä tätä, sillä kun hän muodostaa sormusallekirjoituksensa, hän ottaa yhteyttä etäsolmuun saadakseen lähdöt sisällytettäväksi sormusallekirjoitukseen. Internetin puuttuminen tarkoittaa, että he eivät voi tavoittaa tätä solmua, joten heillä ei ole offline-transaktioiden luomisominaisuuksia.

Ennen kuin jatkamme joihinkin yksityisyyteen liittyviin seikkoihin, kerrotaan lyhyesti Internetin toiminnasta kokonaisuudessaan. Koko internet ei ole muuta kuin tietokoneita, jotka muodostavat yhteyden muihin tietokoneisiin. Se siitä. Blogi jota tykkäät lukea? Vain joitain tiedostoja joita isännöidään jonkun toisen tietokoneella. Tämä verkkosivusto, jolla luet tätä artikkelia (LocalMonero)? Tiedostot ja koodi isännöidään jossain tietokoneessa. Jopa suuret hullut sivustot toimivat tällä tavalla. Otetaan esimerkiksi YouTube. Vain videotiedostoja, joita isännöidään Googlen jättimäisissä tietokonejärjestelmissä, ja yhdistät niihin ladataksesi videon omalle tietokoneellesi jotta voit katsella sitä.

Nämä tietokoneet voivat erottaa toisistaan, koska jokaiselle Internetiin yhdistetylle tietokoneelle annetaan yksilöllinen tunnistenumero, jota kutsutaan IP-osoitteeksi. Nämä ovat yleensä neljä numerosarjaa, jotka on erotettu pisteillä, esimerkiksi: 172.66.35.7. On tärkeää pitää tämä mielessä, kun pohdimme kuinka Monero-tietoa siirretään Internetissä. Monero on vertaisverkko (P2P), mikä tarkoittaa että tietokoneet muodostavat yhteyden suoraan toisiinsa välittäjän sijaan. Joten kun käyttäjän täysi solmu lataa äskettäin löydettyä lohkoa, hän ei lataa sitä keskuspalvelimelta, vaan vertaisilta. Huono puoli tässä on, että koska käyttäjät muodostavat yhteyden suoraan toisiinsa, he tietävät toistensa IP-osoitteet.

No? Miksi se on niin iso juttu? Se on vain numero, eikö? Ei oikeastaan. IP-osoitteet itsessään sisältävät tietoja käyttäjästä, kuten alkuperämaasta ja verkkopalveluntarjoajasta, mutta mikä pahempaa, Internet-palveluntarjoajat (ISP) tietävät jokaisen palvelujaan käyttävän henkilön IP-osoitteen. Tämä tarkoittaa, että nämä Internet-palveluntarjoajat ja ne joiden kanssa he työskentelevät, voivat seurata käyttäjän Internet-liikennettä ja ovelaa taktiikkaa käyttäen havaita käyttävänsä Moneroa. Nyt ennen kuin pelkäät, pane merkille sanamuoto. Nämä nuuhkijat voivat vain nähdä, että henkilö muodostaa yhteyden muihin Monero-verkon solmuihin. Moneron tietosuojatekniikan vuoksi henkilöstä ei vuoda mitään muuta. Ei tiedetä ajavatko he solmua tai lähettävätkö/milloin lähettävät transaktioita, ja jos transaktio lähetetään, mitään sen tiedoista ei tiedetä. Nämä Internet-palveluntarjoajat näkevät vain sen, että yksi heidän käyttäjistään muodostaa yhteyden Monero-verkkoon.

Joillekin ihmisille joissakin tilanteissa nämä tiedot voivat yksinään riittää vahingoittamaan mainetta tai vapautta. Tai ehkä ajatus siitä että joku loukkaa yksityisyyttäsi ja tietää mitä teet Internetissä mistä tahansa syystä, ei ole sinulle hyväksyttävä. Näitä henkilöitä kannustetaan muodostamaan yhteys Monero-verkkoon vain VPN:n, Torin tai I2P:n avulla, jotka kaikki ovat palveluita, jotka piilottavat käyttäjän IP-osoitteen muilta sekä piilottavat käyttäjän tekemät asiat Internet-palveluntarjoajalta. Näiden palvelujen väliset erot eivät kuulu tämän artikkelin piiriin, mutta aiheesta on kirjoitettu paljon korkealaatuisia artikkeleita, joten huolestuneita käyttäjiä kehotetaan perehtymään tarkemmin näihin!

Me muut saatamme ajatella, että se, että muut tietävät meidän olevan yhteydessä Monero-verkkoon, ei ole kovin iso juttu. Loppujen lopuksi transaktioidemme varsinainen sisältö, tai jos edes lähetämme sellaista, on piilotettu, joten mitä haittaa siitä on? Vaikka tämä saattaa olla totta, käyttäjiä rohkaistaan ottamaan huomioon, että kryptovaluuttojen tärkein vetovoima on olla itse itsesi pankki. Kun pidät yksityisen avaimesi itselläsi ja sille tapahtuu jotain, kukaan ei voi auttaa sinua palauttamaan menetettyjä varoja.

Olemalla oma pankkisi tarkoittaa digitaalisen turvallisuutesi lisäksi myös fyysisen turvallisuutesi huomioon ottamista. Voi hyvinkin olla, että Monero-verkkoon liittyneen yksilön tieto saattaa herättää ei-toivottua huomiota, ei välttämättä suurilta toimijoilta, kuten kansallisvaltioilta, vaan pienemmiltä itsekkäästi kiinnostuneilta yksilöiltä, kuten helposti tienaavia hakkereita. Salausmaailmassa on todellakin lukemattomia tarinoita tällaisista skenaarioista tosimaailmasta.

Tämän artikkelin tarkoituksena ei ole pelotella, vaan pikemminkin rohkaista käyttäjiä tutkimaan mitkä verkkoselailusuojausmenetelmät sopivat heille. Hyvä uutinen on, että nämä taidot siirtyvät myös yleiseen internetin käyttöön, eikä vain Moneron käyttöön. Yhä enemmän Internetiin yhdistetyssä maailmassamme taitava käyttäjä ei voi mennä pieleen opiskelemalla tarvittavia tietoja ja taitoja turvallisuuden säilyttämiseksi. Ja todella olla heidän oma pankkinsa.

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

  * [Kuinka RingCT piilottaa Monero-transaktiosummat](/knowledge/monero-ringct/)

  * [Kuinka Monero Stealth -osoitteet suojaa identiteettiäsi](/knowledge/monero-stealth-addresses/)

  * [Kuinka Monero-aliosoitteet estävät identiteetin yhdistämisen](/knowledge/monero-subaddresses/)

  * [Moneron Outputit selitettynä](/knowledge/monero-outputs/)

  * [Moneron parhaat käytännöt aloittelijoille](/knowledge/monero-best-practices/)

  * [Kuinka sormusallekirjoitukset sekoittavat Moneron outputit](/knowledge/ring-signatures/)

  * [Kuinka Monero ratkaisi Bitcoinia vaivaavan lohkokoko-ongelman](/knowledge/dynamic-block-size/)

  * [Kuinka CLSAG parantaa Moneron tehokkuutta](/knowledge/what-is-clsag/)

  * [Miksi Monerolla on "Tail Emission"](/knowledge/monero-tail-emission/)

  * [Moneron lyhyt historia](/knowledge/monero-history/)

  * [Wired Magazine on väärässä Monerosta, tässä miksi](/knowledge/wired-article-debunked/)

  * [15 parasta Monero-myyttiä ja -huolia, jotka on kumottu](/knowledge/monero-myths-debunked/)

  * [Kuinka Dandelion++ pitää Moneron tapahtuman alkuperän yksityisenä](/knowledge/monero-dandelion/)

  * [Miksi Monero on avoimen lähdekoodin ja hajautettu](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Moneron louhinta: Mikä tekee RandomX:stä niin erityisen?](/knowledge/monero-mining-randomx/)

  * [Miksi Monero on parempi kuin Dash, Zcash, Zcoin (jopa Lelantuksen kanssa), Grin ja Bitcoin-mikserit kuten Wasabi (päivitetty toukokuussa 2020)](/knowledge/why-monero-is-better/)