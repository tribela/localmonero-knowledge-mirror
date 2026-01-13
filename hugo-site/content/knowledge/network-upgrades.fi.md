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
  2. [Näkymätunnisteet, loistava tapa lyhentää lompakon synkronointiaikoja 30–40%](https://localmonero.co/knowledge/view-tags-reduce-monero-sync-time)
  3. Kulumuutokset, jotka parantavat verkon turvallisuutta ja joustavuutta maksumarkkinoiden nopeille muutoksille tai haitallisten tahojen hyökkäyksille
  4. [Bulletproofs+, lisäparannuksia Monero-transaktioiden tehokkuuteen](https://www.getmonero.org/2020/12/24/Bulletproofs+-in-Monero.html)

Näillä pitkään riittävillä muutoksilla parannetaan verkon yksityisyyttä, tehokkuutta ja turvallisuutta, samalla kun se tasoittaa tietä [Seraphis](https://localmonero.co/knowledge/seraphis-for-monero):lle, Moneron seuraavan sukupolven tapahtumaprotokollalle.

## Miten voin oppia lisää?

Aihe hard forkeista ja verkkopäivityksistä on laaja, niillä on pitkä ja tarinallinen historia Monerossa, joten muista kaivautua joihinkin seuraavista linkeistä, jos haluat tietää lisää tulevaa verkkopäivitystä varten meneillään olevasta historiasta, prosessista tai suunnittelusta!

  * [Monero v15 hard-fork -suunnittelu](https://github.com/monero-project/meta/issues/630)
  * [Ajoitetut ohjelmistopäivitykset (Monerossa)](https://github.com/monero-project/monero#scheduled-software-upgrades)
  * [Huomautus ajoitetuista protokollapäivityksistä](https://web.getmonero.org/2020/09/01/note-scheduled-upgrades.html)

Lue lisää