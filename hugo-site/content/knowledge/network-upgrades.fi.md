---
title: "Kuinka Monero käyttää hard forkkeja verkon päivittämiseen"
slug: "network-upgrades"
date: "2022-02-10"
image: "/images/upgrades.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Yksi yleisimmin väärinymmärretyistä osista Moneron lähestymistavassa hajautetun, yksityisyyttä suojelevan ja suojatun kryptovaluutan rakentamisessa on hard forkkien (tai verkkopäivitysten) rooli.

Tässä viestissä käymme läpi, mitä "hard forkit" ovat, miksi ne ovat tärkeitä Monerolle ja mikä rooli sinulla voi olla niissä tulevaisuudessa.

## Miksi Moneron on jatkuvasti päivitettävä verkkoa?

Moneron yhteisö on sitoutunut iteroimaan ja parantamaan projektia ajan myötä ja näyttää siltä, että sitoutuminen tiivistyy kahteen yhteisön luonteenomaiseen osaan:

  1. Monero-projekti on viime kädessä ihmisten kirjoittama ohjelmisto – koodi. Tämä voi johtaa tarpeeseen korjata vikoja, lisätä ajan mittaan löydettyjä tai keksittyjä parannuksia, toteuttaa protokollan modernisointeja tai yksinkertaisesti ylläpitää projektia. Tämä on monella tapaa samanlainen kuin muut käyttämäsi ohjelmistot (kuten selain, jolla luet tätä!), joita on päivitettävä jatkuvasti uusien ominaisuuksien lisäämiseksi ja virheiden korjaamiseksi.

  2. Monero-projekti on tietosuojatyökalu, ja yksityisyys on jatkuvasti etenevä kilpavarustelu. Ihmiset ja ryhmät, jotka eivät halua muuta kuin riistää yksityisyyden maailmasta (sekä taloudellisen että henkilökohtaisen), parantavat, kehittävät ja keksivät jatkuvasti uusia tapoja hyökätä moderneihin lähestymistapoihin yksityisyyden säilyttämisessä, kuten Monerossa käytettyihin tapoihin. Kun yksityisyyden viholliset löytävät nämä uudet lähestymistavat, Monero-verkon on kyettävä mukautumaan ja kehittymään taistelemaan ja puolustamaan oikeuttamme taloudelliseen yksityisyyteen.

Monero-projekti on viime kädessä ihmisten kirjoittama ohjelmisto – koodi. Tämä voi johtaa tarpeeseen korjata vikoja, lisätä ajan mittaan löydettyjä tai keksittyjä parannuksia, toteuttaa protokollan modernisointeja tai yksinkertaisesti ylläpitää projektia. Tämä on monella tapaa samanlainen kuin muut käyttämäsi ohjelmistot (kuten selain, jolla luet tätä!), joita on päivitettävä jatkuvasti uusien ominaisuuksien lisäämiseksi ja virheiden korjaamiseksi.

Monero-projekti on tietosuojatyökalu, ja yksityisyys on jatkuvasti etenevä kilpavarustelu. Ihmiset ja ryhmät, jotka eivät halua muuta kuin riistää yksityisyyden maailmasta (sekä taloudellisen että henkilökohtaisen), parantavat, kehittävät ja keksivät jatkuvasti uusia tapoja hyökätä moderneihin lähestymistapoihin yksityisyyden säilyttämisessä, kuten Monerossa käytettyihin tapoihin. Kun yksityisyyden viholliset löytävät nämä uudet lähestymistavat, Monero-verkon on kyettävä mukautumaan ja kehittymään taistelemaan ja puolustamaan oikeuttamme taloudelliseen yksityisyyteen.

## Mikä on hard-fork?

Moneron päivitysten monimutkaisuus tulee voimaan kun ymmärrät, miten kryptovaluutan päivittäminen eroaa pelkän ohjelmistopäivityksen puskemisesta johonkin selaimeen.

Kryptovaluutoissa verkon säännöistä (kuten siitä, miltä transaktioiden pitäisi näyttää, miten louhinta toimii ja kuinka jokainen lohko tarkistetaan) on sovittava verkon kanssa, mitä kutsutaan "konsensukseksi". Kun mitä tahansa näistä säännöistä on muutettava tai päivitettävä, verkon on sovittava uusista säännöistä, mikä aiheuttaa "hard fork" -tilanteen, jossa verkko jakautuu kahteen lohkoketjuun - yksi vanhojen sääntöjen mukaan ja toinen uusien sääntöjen.

Kun kaikki yhteisön jäsenet ovat yhtä mieltä sääntömuutoksista, sitä kutsutaan "kiistattomaksi hard-forkiksi", ja lohkoketju jolla on edelleen vanhat säännöt, kuolee pois, eikä sitä louhita hard forkin jälkeen. Näin on käynyt melkein jokaisessa Moneron hard forkissa, ja ainoa jatko vanhoille säännöille oli projektit, joissa yritettiin hyötyä hard forkista.

Vaikka kiistattomat hard forkit ovat ainoa tapa todella päivittää Monero-verkon tärkeitä ominaisuuksia, niillä on myös turhauttava sivuvaikutus – vanha ohjelmisto, joka julkaistiin ennen hard forkin suunnittelua ei ymmärrä uuden verkon sääntöjä, joten se ei toimi hard forkin jälkeen! Tämä voi johtaa siihen, että käyttäjät ajattelevat varojen katoavan Monero-lohkoketjun pysähtyessä ja he eivät voi siirtää varoja ennen kuin he päivittävät lompakkoaan.

## Kuka päättää, milloin Monero-verkko päivitetään ja mitä se sisältää?

Koska Monerolla ei ole keskusviranomaista, toimitusjohtajaa tai muutakaan johtajaa, verkon päivityksen, sen sisällyttämisen ja toimenpiteiden tekeminen kuuluu _meille_ , niille henkilöille Monero-yhteisössä, jotka päättäävät osallistua ja olla vuorovaikutuksessa! Tämä on erittäin tärkeä osa hajautettua hanketta, sillä projektin suunnittelu ja päätöksenteko on viime kädessä hajautettua ja yhteisöstä ulkoistettua joukkotyötä.

Moneron jokaisen verkkopäivityksen ajoituksen ja ominaisuuksien suunnittelu tapahtuu kahdessa pääpaikassa:

  1. IRC:ssä ja Matrixissa, jotka ovat Monero-yhteisön eniten käytetyt keskustelualustat (jotka on yhdistetty toisiinsa). Nämä alustat mahdollistavat suuria ryhmäkeskusteluja, ja niissä pidetään kaikki suunnitellut Monero-yhteisökokoukset, kehittäjäkokoukset ja tutkimuslaboratorion kokoukset. Nämä tapaamiset ovat paras tapa kuunnella (tai osallistua!) Moneron verkkopäivitysten suunnitteluun ja keskusteluun.

  2. Githubissa, tärkein viestintäalusta pidempään jatkuviin Monero-keskusteluihin, suunnitteluun ja organisointiin. Monero-yhteisö käyttää Githubia tapaamisten järjestämiseen, uusien ominaisuuksien ja ideoiden keskusteluun sekä verkkopäivitysten suunnittelun koordinointiin Monero-projektin koodin tallentamisen lisäksi.

IRC:ssä ja Matrixissa, jotka ovat Monero-yhteisön eniten käytetyt keskustelualustat (jotka on yhdistetty toisiinsa). Nämä alustat mahdollistavat suuria ryhmäkeskusteluja, ja niissä pidetään kaikki suunnitellut Monero-yhteisökokoukset, kehittäjäkokoukset ja tutkimuslaboratorion kokoukset. Nämä tapaamiset ovat paras tapa kuunnella (tai osallistua!) Moneron verkkopäivitysten suunnitteluun ja keskusteluun.

Githubissa, tärkein viestintäalusta pidempään jatkuviin Monero-keskusteluihin, suunnitteluun ja organisointiin. Monero-yhteisö käyttää Githubia tapaamisten järjestämiseen, uusien ominaisuuksien ja ideoiden keskusteluun sekä verkkopäivitysten suunnittelun koordinointiin Monero-projektin koodin tallentamisen lisäksi.

Jos sinulla on hyvä idea verkkopäivitykseen liittyen, et pidä omaksutusta lähestymistavasta tai olet huolissasi päivityksen ajoituksesta, on tärkeää että puhut ja esität asiasi selkeästi yhteisölle! 

## Kuinka voin auttaa verkkopäivityksissä?

Koska Monero-verkkoon tehtävät päivitykset vaativat yhteisön koordinointia ja hyväksyntää ohjelmistopäivitysten ohella, on erittäin tärkeää, että mahdollisimman monet ihmiset osallistuvat verkkopäivitysten suunnitteluun, testaukseen ja viestintäprosessiin.

Tässä on muutamia helppoja tapoja, joilla voit helpottaa verkkopäivitystä:

  1. Liity suunnittelukokouksiin [, jotka on julkaistu Githubissa](https://github.com/monero-project/meta/issues), kuuntele ja osallistu, jos sinulla on jotain olennaista esitettäväksi.
  2. Kerro verkon päivityksen ajoituksen yksityiskohdista (kun olet päättänyt!) suosikkipörssillesi, lompakkoosi tai louhintapoolillesi. Voi olla vaikeaa ilmoittaa kaikille Monero-käyttäjille päivityksestä, joten on tärkeää, että me kaikki autamme paikoissa missä voimme saada sanan esiin.
  3. Testaa ohjelmisto ennen verkkopäivitystä. Testaajille järjestetään kutsu ennen verkkopäivitystä, sekä testnetissä että stagenetissä, jotta varmistetaan että päivityksen jokainen osa on oikein suunniteltu ja toteutettu ohjelmistossa. Mitä enemmän ihmiset osallistuvat ja testaavat uusia versioita perusteellisesti, sitä todennäköisemmin verkkopäivitys sujuu!
  4. Kun verkkopäivityksen kanssa yhteensopivat päivitykset on julkaistu, muista päivittää välittömästi! Mitä enemmän ihmisiä ovat päivittäneet ja valmiita verkkopäivitykseen, sitä sujuvammin verkko käsittelee sen ja sitä vähemmän käyttäjät kokevat päänsärkyä.

## Mitä voin odottaa seuraavassa Monero-verkkopäivityksessä?

Vaikka päivämäärää ei ole vielä kiveen hakattu, verkkopäivitys tulee pian, jotta Monerossa voidaan ottaa käyttöön muutamia tärkeitä päivityksiä ja ominaisuuksia:

  1. Sormuksen koon kasvaminen 11:stä 16:een, mikä lisää jokaisen verkossa tapahtuvan transaktion anonymiteetin perusjoukkoa (lue: uskottava kiellettävyys tai perustietosuoja)
  2. [Näkymätunnisteet, loistava tapa lyhentää lompakon synkronointiaikoja 30–40%](/knowledge/view-tags-reduce-monero-sync-time/)
  3. Kulumuutokset, jotka parantavat verkon turvallisuutta ja joustavuutta maksumarkkinoiden nopeille muutoksille tai haitallisten tahojen hyökkäyksille
  4. [Bulletproofs+, lisäparannuksia Monero-transaktioiden tehokkuuteen](https://www.getmonero.org/2020/12/24/Bulletproofs+-in-Monero.html)

Näillä pitkään riittävillä muutoksilla parannetaan verkon yksityisyyttä, tehokkuutta ja turvallisuutta, samalla kun se tasoittaa tietä [Seraphis](/knowledge/seraphis-for-monero/):lle, Moneron seuraavan sukupolven tapahtumaprotokollalle.

## Miten voin oppia lisää?

Aihe hard forkeista ja verkkopäivityksistä on laaja, niillä on pitkä ja tarinallinen historia Monerossa, joten muista kaivautua joihinkin seuraavista linkeistä, jos haluat tietää lisää tulevaa verkkopäivitystä varten meneillään olevasta historiasta, prosessista tai suunnittelusta!

  * [Monero v15 hard-fork -suunnittelu](https://github.com/monero-project/meta/issues/630)
  * [Ajoitetut ohjelmistopäivitykset (Monerossa)](https://github.com/monero-project/monero#scheduled-software-upgrades)
  * [Huomautus ajoitetuista protokollapäivityksistä](https://web.getmonero.org/2020/09/01/note-scheduled-upgrades.html)

Lue lisää

  * [Kuinka Monero ainutlaatuisesti mahdollistaa kiertotaloudet](/knowledge/monero-circular-economies/)

  * [Moneron sormusallekirjoitukset vs CoinJoin kuten Wasabissa](/knowledge/ring-signatures-vs-coinjoin/)

  * [Miksi (ja miten!) sinun pitäisi hallita omia avaimiasi](/knowledge/hold-your-keys/)

  * [Osallistuminen Moneroon](/knowledge/contributing-to-monero/)

  * [Kuinka etäsolmut vaikuttavat Moneron yksityisyyteen](/knowledge/remote-nodes-privacy/)

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

  * [Kuinka CLSAG parantaa Moneron tehokkuutta](/knowledge/what-is-clsag/)

  * [Miksi Monerolla on "Tail Emission"](/knowledge/monero-tail-emission/)

  * [Moneron lyhyt historia](/knowledge/monero-history/)

  * [Wired Magazine on väärässä Monerosta, tässä miksi](/knowledge/wired-article-debunked/)

  * [15 parasta Monero-myyttiä ja -huolia, jotka on kumottu](/knowledge/monero-myths-debunked/)

  * [Kuinka Dandelion++ pitää Moneron tapahtuman alkuperän yksityisenä](/knowledge/monero-dandelion/)

  * [Miksi Monero on avoimen lähdekoodin ja hajautettu](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Moneron louhinta: Mikä tekee RandomX:stä niin erityisen?](/knowledge/monero-mining-randomx/)

  * [Miksi Monero on parempi kuin Dash, Zcash, Zcoin (jopa Lelantuksen kanssa), Grin ja Bitcoin-mikserit kuten Wasabi (päivitetty toukokuussa 2020)](/knowledge/why-monero-is-better/)