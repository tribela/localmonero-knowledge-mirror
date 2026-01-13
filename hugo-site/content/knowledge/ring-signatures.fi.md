---
title: "Kuinka sormusallekirjoitukset sekoittavat Moneron outputit"
slug: "ring-signatures"
date: "2020-09-08"
image: "/images/rings.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero tunnetaan kaikkialla kryptomaailmassa yksityisyyden kolikoiden kuninkaana. Vaikka kaikki tietävät, että Monero tarjoaa hyvän yksityisyyden, monet eivät ymmärrä miten yksityisyys toimii.

Monet muut yksityisyyttä suojaavat kolikot julkaisevat vertailukaavion infografioista, joissa luetellaan kunkin kolikon tietosuojatekniikan nimet, ja useimmissa niissä Moneron tekniikka merkitään RingCT:ksi, mutta tämä on vain osittain totta. Monerolla on itse asiassa kolmiosainen lähestymistapa yksityisyyteen. Yksi tekniikka piilottaa tapahtuman vastaanottajan, toinen piilottaa lähetetyn summan ja kolmas piilottaa käytetyn ulostulon. Nämä ovat siis yksinkertaisesti "stealth" osoitteet, RingCT-tekniikka ja sormusallekirjoitukset.

Tämä kolmiosainen lähestymistapa tarkoittaa, että jos jokin teknologioista rikkoutuu, muut eivät välttämättä jaa samaa kohtaloa. Sormusallekirjoitukset ovat tietosuojajärjestelmän heikoin lenkki; sana heikko tarkoittaa tässä kaikkein herkimpiä heuristisille hyökkäyksille. Otetaanpa hetki aikaa niiden tutkimiseen, eikö niin?

Kuten edellä mainittiin, sormusallekirjoitusten tarkoitus on peittää transaktiossa käytetty ulostulo. Jos kryptovaluutan "syöttö/ulostulo" -terminologia on hämmentävä sinulle, älä huoli. Se ei itse asiassa ole niin monimutkaista. Kun kuulet "ulostulo", ajattele vain shekkiä. Yksi niistä asioista, joka ei ole enää niin yleinen maksuväline. Shekin tavoin se voidaan merkitä mihin tahansa summaan - 10 dollaria, 32,50 dollaria jne. - ja se vaihdetaan tapahtuman osapuolten välillä. Kryptovaluuttojen ulostulot palvelevat näitä toimintoja.

Kun joku maksaa sinulle 10 Moneroa, saat 10 XMR-ulostulon. Tällä ulostulolla on arvo (10), ja se otetaan lähettäjän lompakosta, samalla tavalla kun maksat palvelusta, lasku lähtee fyysisestä lompakostasi ja se annetaan henkilölle, jolta ostat.

Tapa, jolla ulostulo piilotetaan, on rakentaa rinki (tästä nimi "sormus") syöttiulostuloja. Mutta nämä syötit eivät ole "väärennettyjä" ulostuloja. Ne ovat todellisia lohkoketjun menneitä ulostuloja, joilla ei ole mitään tekemistä nykyisen transaktion kanssa, mutta ulkopuoliselle tarkkailijalle jokainen näistä ulostuloista saattaa näyttää yhtä uskottavalta kuin todellinen. Syöttiulostulon kokoa sekä oikeaa kokoa kutsutaan sormuskooksi, ja tällä hetkellä Moneron sormuskoko on yksitoista. Tarjolla on siis kymmenen syöttiulostuloa ja yksi oikea.

Miksi emme vain nosta tätä lukua 100:aan tai jopa 1000:een? Mitä enemmän sen parempi, eikö? No, yksityisyyden näkökulmasta kyllä, mutta on muitakin huomioitavia asioita. Palataanpa fyysiseen esimerkkiin nähdäksesi mitä tarkoitan. Jos halusit piilottaa yhden dollarisetelisi kymmenen syötin joukkoon, sinun täytyy kuljettaa lompakossasi noin yksitoista dollaria jokaista haluamaasi dollaria kohden. Yksi oikea dollari ja kymmenen väärennettyä. Tämä on jo melko hankalaa, jos haluat käyttää edes muutaman dollarin. Kuvittele nyt, että nostimme syöttisumman 1000:een. Jokaista kulutettavaa dollaria kohden tarvitset noin 1001 dollaria. Sinun täytyy kuljettaa salkkua vain ostaaksesi yhden karkkipatukan! Tärkeää on huomata, että sormusallekirjoitukset eivät toimi aivan tällä tavalla, esim. syötit itsessään ei ole osa allekirjoitusta, vain viittauksia niihin, mutta toivomme että tästä analogiasta on jonkin verran apua peruskäsitteiden kuvaamisessa.< /p>

Lohkoketjun syötit toimivat samalla tavalla. Jokainen lisätty syötti lisää transaktion aikaa ja varmistuskustannuksia. Jokaisen solmun on ladattava koko sormusallekirjoitus jokaista transaktiota varten, ja jokainen sormusallekirjoitus sisältää todellisen ulostulon sekä syöttejä. Ei vain sitä, vaan sen on tarkistettava matematiikka, että ainakin yksi näistä ulostuloista on todellinen, ja myös matemaattinen varmistusaika pitenee jokaisen syötin myötä. Tämä tarkoittaa, että meidän on löydettävä kultainen keskitie, jossa sormuskoko on tarpeeksi suuri peittämään riittävästi todellista ulostuloa jopa monia heuristisia hyökkäyksiä vastaan, mutta tarpeeksi pieni, jotta lohkoketju ei kasva massiivisella nopeudella. Ei riitä, että valitset mielivaltaisen numeron tai vain nostamme sormuksen kokoa, kun pienennämme allekirjoitusta (kuten CLSAG:lla). Monero-yhteisö haluaa konkreettisia, matemaattisia todisteita siitä, mikä sormuskoko tarjoaa parhaat kompromissit. Luku on liian pieni ja yksityisyys ei ole tarpeeksi vahva heuristisia hyökkäyksiä vastaan. Liian suuri ja saatamme saada vain marginaalista hyötyä yksityisyyden puolella ja kärsiä tarpeettomasti skaalauksesta.

Viimeinen mainittava asia. Jotkut Monero-kirjallisuudet yksinkertaistavat ja sanovat, että sormusallekirjoitukset piilottavat lähettäjän, mutta tämä ei ole täysin totta, eikä ero ole vain pedanttinen. Ero lähettäjän (ihmisen) ja ulostulon (shekki) välillä on suuri yksityisyyden säilyttämisen kannalta. Vaikka ulostulolla voi olla yhteyksiä lähettäjään, ulostulo itsessään ei ole sama kuin lähettäjä. Joten vaikka sormusallekirjoitus rikottaisiin, se ei välttämättä liity lähettäjän henkilöllisyyteen, ja sekä summa että vastaanottaja ovat silti piilossa, mikä minimoi kaikkien osapuolten yksityisyydelle aiheutuvan vahingon.

Tämä ei tarkoita, että rikkinäinen sormusallekirjoitus olisi merkityksetön. Kaikki vuotaneet metatiedot ovat pahasta, ja ne voivat paljastaa enemmän tietoa kuin uskomme, varsinkin kun niitä käytetään yhdessä muiden metatietojen kanssa. Teemme siis parhaamme varmistaaksemme, että valitun sormuskoon päätöksen taustalla on akateeminen kurinalaisuus, muut metatietojen vuodot minimoidaan ja käyttäjäkokemukset toimivat oletusarvoisesti parhaiden mahdollisten toimintojen mukaisesti.

Mutta jos rikkinäisen allekirjoituksen todennäköisyys huolestuttaa sinua, horisontissa on uskomattomia uutisia. Seuraavan sukupolven tietosuojaprotokollat, joita kehitetään, kuten Triptych, Arcturus ja Lelantus, ovat todella siistejä ominaisuuksia. Näissä protokollissa koko skaalautuu logaritmisesti, ei lineaarisesti, kun sormuksen koko kasvaa. Tämä tarkoittaa, että mukaan mahtuu 100 syöttiä, mutta käytetty tila on lähempänä sormuskokoa 10 vanhassa tekniikassa. Se on melkoinen ero, ja se parantaa merkittävästi yksityisyyttä kaikkialla.

Kissa ja hiiri -pelissä, jota yksityisyys on, Monero tekee jatkuvasti innovaatioita pysyäkseen kehityksen kärjessä ja varmistaakseen parhaan käytännön yksityisyyden kaikille.

Lohkoketjun syötit toimivat samalla tavalla. Jokainen lisätty syötti lisää transaktion aikaa ja varmistuskustannuksia. Jokaisen solmun on ladattava koko sormusallekirjoitus jokaista transaktiota varten, ja jokainen sormusallekirjoitus sisältää todellisen ulostulon sekä syöttejä. Ei vain sitä, vaan sen on tarkistettava matematiikka, että ainakin yksi näistä ulostuloista on todellinen, ja myös matemaattinen varmistusaika pitenee jokaisen syötin myötä. Tämä tarkoittaa, että meidän on löydettävä kultainen keskitie, jossa sormuskoko on tarpeeksi suuri peittämään riittävästi todellista ulostuloa jopa monia heuristisia hyökkäyksiä vastaan, mutta tarpeeksi pieni, jotta lohkoketju ei kasva massiivisella nopeudella. Ei riitä, että valitset mielivaltaisen numeron tai vain nostamme sormuksen kokoa, kun pienennämme allekirjoitusta (kuten CLSAG:lla). Monero-yhteisö haluaa konkreettisia, matemaattisia todisteita siitä, mikä sormuskoko tarjoaa parhaat kompromissit. Luku on liian pieni ja yksityisyys ei ole tarpeeksi vahva heuristisia hyökkäyksiä vastaan. Liian suuri ja saatamme saada vain marginaalista hyötyä yksityisyyden puolella ja kärsiä tarpeettomasti skaalauksesta.

Viimeinen mainittava asia. Jotkut Monero-kirjallisuudet yksinkertaistavat ja sanovat, että sormusallekirjoitukset piilottavat lähettäjän, mutta tämä ei ole täysin totta, eikä ero ole vain pedanttinen. Ero lähettäjän (ihmisen) ja ulostulon (shekki) välillä on suuri yksityisyyden säilyttämisen kannalta. Vaikka ulostulolla voi olla yhteyksiä lähettäjään, ulostulo itsessään ei ole sama kuin lähettäjä. Joten vaikka sormusallekirjoitus rikottaisiin, se ei välttämättä liity lähettäjän henkilöllisyyteen, ja sekä summa että vastaanottaja ovat silti piilossa, mikä minimoi kaikkien osapuolten yksityisyydelle aiheutuvan vahingon.

Tämä ei tarkoita, että rikkinäinen sormusallekirjoitus olisi merkityksetön. Kaikki vuotaneet metatiedot ovat pahasta, ja ne voivat paljastaa enemmän tietoa kuin uskomme, varsinkin kun niitä käytetään yhdessä muiden metatietojen kanssa. Teemme siis parhaamme varmistaaksemme, että valitun sormuskoon päätöksen taustalla on akateeminen kurinalaisuus, muut metatietojen vuodot minimoidaan ja käyttäjäkokemukset toimivat oletusarvoisesti parhaiden mahdollisten toimintojen mukaisesti.

Mutta jos rikkinäisen allekirjoituksen todennäköisyys huolestuttaa sinua, horisontissa on uskomattomia uutisia. Seuraavan sukupolven tietosuojaprotokollat, joita kehitetään, kuten Triptych, Arcturus ja Lelantus, ovat todella siistejä ominaisuuksia. Näissä protokollissa koko skaalautuu logaritmisesti, ei lineaarisesti, kun sormuksen koko kasvaa. Tämä tarkoittaa, että mukaan mahtuu 100 syöttiä, mutta käytetty tila on lähempänä sormuskokoa 10 vanhassa tekniikassa. Se on melkoinen ero, ja se parantaa merkittävästi yksityisyyttä kaikkialla.

Kissa ja hiiri -pelissä, jota yksityisyys on, Monero tekee jatkuvasti innovaatioita pysyäkseen kehityksen kärjessä ja varmistaakseen parhaan käytännön yksityisyyden kaikille.

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