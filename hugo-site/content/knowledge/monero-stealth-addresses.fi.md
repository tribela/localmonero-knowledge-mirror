---
title: "Kuinka Monero Stealth -osoitteet suojaa identiteettiäsi"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero on ottanut käyttöön kolmiosaisen lähestymistavan yksityisyyteen. Nämä tekniikat ovat [sormusallekirjoitukset](/knowledge/ring-signatures), jotka piilottavat todellisen ulostulon (lähettäjä), RingCT, joka piilottaa summat, ja "stealth" osoitteet, jotka piilottavat vastaanottajan. Tänään keskustelemme viimeisestä mainituista teknologioista: "stealth" osoitteista eli salatuista osotteista.

On monia syitä miksi henkilö saattaa haluta piilottaa kenelle he lähettävät varojaan. Emme saa koskaan antaa kenenkään yrittää vakuuttaa meille, että kaikki esimerkit tästä ovat hämärää käytöstä. Asiat, kuten lähettäminen epäsuosittuun poliittiseen puolueeseen, lahjoittaminen hyväntekeväisyyteen tai "canceloitujen" ihmisten tukeminen ovat kaikki esimerkkejä siitä, missä voidaan haluta piilottaa kulutuskäyttäytymisensä seurausten pelossa, mutta ne ovat luonteeltaan täysin laillisia. 

Läpinäkyvässä lohkoketjussa osoitteet, joihin transaktiot lähetetään, näkyvät kaikille. On tärkeää ottaa huomioon, että joslouhijat itse ovat eri mieltä siitä, mihin rahat menevät, he voivat päättää olla louhimatta niitä lohkoksi, mikä sensuroi tämän transaktion tehokkaasti sensuuria kestävällä alustalla. Ainoa tapa tehdä tämä etätodennäköinen temppu sensuurimahdottomaksi on, jos louhijat eivät pysty erottamaan transaktioita, koska kaikki ketjun metatiedot peitetään eri tavoin. Tästä Monero tunnetaan.

Monero ratkaisee tämän läpinäkyvien osoitteiden ongelman ottamalla käyttöön salaiset osoitteet, teknologian, jonka Bitcoin Talk -foorumin käyttäjä "ByteCoin" kehitti alun perin Bitcoinille vuonna 2011 (suhdetta Bytecoiniin, joka myöhemmin integroi salaiset osoitteet, ei tunneta). Nykyisessä salaavien osoitteiden muodossa on kuitenkin useita parannuksia alkuperäiseen ideaan verrattuna. Mutta ensin, jotta ymmärretään kuinka salatut osoitteet toimivat, puhutaanpa avaimista.

On vaikeaa olla kryptovaluuttamaailmassa kuulematta avaimista. Lausahdukset, kuten "varmuuskopioi yksityinen avaimesi", ovat yleisiä, mutta kun tavallinen Joe kuulee sanat "julkinen avain" ja "yksityinen avain", hän pelkää ja ajattelee, että se on liian teknistä ja hämmentävää ymmärtääkseen. Mutta älä huoli. Otamme ne hitaasti käsittelyyn ja käytämme paljon esimerkkejä.

Kahdet kryptovaluutoissa käytettävät avaimet ovat, kuten juuri mainittiin, julkisia ja yksityisiä. Nämä kaksi avainta tulevat yleensä pareina, mikä tarkoittaa, että tietty julkinen ja yksityinen avain on linkitetty toisiinsa. Itse asiassa yleensä julkinen avain johdetaan yksityisestä avaimesta, eli jos tiedät yksityisen avaimen, lompakkosi pystyy laskemaan ja keksimään oikean julkisen avaimen joka kerta.

Nyt, kuten nimet antavat ymmärtää, julkinen avain voi olla julkinen ilman seurauksia. Yleensä se on osa osoitetta, jonka jaat saadaksesi rahaa kryptovaluuttalompakkoosi. Myös yksityinen avain on nimensä mukaan sellainen, jota ei pidä jakaa. Se on asia, jonka avulla voit allekirjoittaa ja toteuttaa transaktion, joten jos se varastetaan tai jaetaan, ilkeä kolmas osapuoli voi viedä rahasi, yleensä itselleen.

Helppo analogia tähän olisi riippulukko ja sen avaamiseen tarvittava avain. Avoin riippulukko voidaan jakaa vapaasti, ja tällä riippulukolla voidaan lukita mitä tahansa, mutta vain avaimella voi avata kaiken, missä riippulukko on kiinni. Riippulukko voidaan kopioida ja jakaa, avainta ei kannata.

Nämä avaimet on yleensä vedetty pois käyttäjältä, joten et luultavasti edes koskaan näe niitä. Monerossa ne eivät näy ollenkaan pelottavana aakkosnumeerisena merkkijonona. Monerossa tavallinen käyttäjä tietää yksityisen avaimen seedinään. Seed (eli palautelause, joka sinun tulee kirjoittaa muistiin, jos et ole tehnyt sitä) on itse asiassa vain ihmisen luettavissa oleva yksityinen avain. 

Näetkö? Ei loppujen lopuksi niin pelottavaa. Takaisin salattuihin osoitteisiin.

Kuten aiemmin mainittiin, salattuja osoitteita ei tehty alun perin Monerolle, vaan Bitcoinille. Kuten useimmissa uusissa ideoissa, tämänkin ensimmäisessä iteraatiossa oli ongelmia. Seuraava yritys tuli, kun Nicholas van Saberhagan loi CryptoNoten Bytecoinille, Moneron edeltäjälle ([katso Moneron ja Bytecoinin historia tästä](/knowledge/monero-history)), ja vaikka se oli selvä parannus alkuperäiseen, siinäkin oli jotain pieniä puutteita.

Iteraatio toisensa jälkeen viimein syntyi lopullinen iteraatio, nyt lakkautetun, yksityisyyden suojaavan kryptovaluutan kehittäjältä, joka korjasi ideaan liittyvät yksityisyys- ja turvallisuusongelmat. Tämä päätyi lopulta Moneroon ja sitä käytetään nykyäänkin.

Vaikka nämä tietosuoja- ja turvallisuusongelmat ratkesivat, salatut osoitteet lisäsivät lohkoketjuteknologioihin toisenlaisen omituisuuden, jota ei ennen ollut olemassa. Tarve skannata. Koska vastaanottavia osoitteita ei näytetä julkisesti lohkoketjussa, vastaanottaja ei koskaan tiedä, onko jokin tietty transaktio hänen, joten hänen on skannattava kaikki saapuvat transaktiot yksityisellä avaimellaan nähdäkseen, onko se hänen.

Käytettäessä läpinäkyviä kolikoita heidän tarvitsee vain tarkistaa, lähetetäänkö transaktio osoitteeseesi. Helppo kyllä tai ei kysymys. Mutta salaisilla osoitteilla jokainen transaktio voi olla sellainen, joka lähetetään sinulle, joten sinun on yritettävä avata jokaisen lukitus yksityisellä avaimella nähdäksesi, avautuuko se.

Tämä on ylimääräinen vaihe, jota Bitcoinilla ja sen johdannaisilla ei ole, ja se tekee lompakon alustavasta asennuksesta sekä lompakon synkronoinnista pidemmän prosessin kuin Bitcoinissa (etenkin jos et ole avannut lompakkoa vähään aikaan). Kompromissi on kuitenkin välttämätön, jotta sillä on yksityisyyteen liittyvät takuut. On huomattava, että toisin kuin yksityisyyden kolminaisuuden heikoin kohta, sormusallekirjoitukset, salatut osoitteet eivät ole herkkiä heuristiikalle. Se perustuu hyväksi havaittuun ja todelliseen elliptisen käyrän salakirjoitukseen, johon koko internet luottaa, joten sen rikkominen merkitsisi tietoturvan loppua kokonaisuudessaan, ei vain Moneron loppua.

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