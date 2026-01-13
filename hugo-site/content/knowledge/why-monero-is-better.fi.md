---
title: "Miksi Monero on parempi kuin Dash, Zcash, Zcoin (jopa Lelantuksen kanssa), Grin ja Bitcoin-mikserit kuten Wasabi (päivitetty toukokuussa 2020)"
slug: "why-monero-is-better"
date: "2024-01-01"
image: "/images/why-monero.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Moneron lisäksi yksikään yksityisyyteen keskittyvä kolikko ei tarjoa 100-prosenttista yksityisyyttä, jäljittämättömyyttä, turvallisuutta ja vaihdettavuutta 100-prosenttisesti hajautetussa kolikossa, luotettavilla asetuksilla. Tässä on mitä nämä attribuutit tarkoittavat ja miksi ne ovat tärkeitä:

## Kolikon analyysi

Tässä on analyysi tunnetuista kryptovaluutoista, jotka väittävät anonymiteetin ja/tai jäljittämättömyyden olevan erottavana avaintekijänä. Bitcoin itsessään ei kuulu tämän analyysin piiriin, koska sen ei ole koskaan väitetty olevan anonyymi.

Tämä sivusto on luotu Monero käyttäjien toimesta. Oli aika, jolloin emme olleet Moneron käyttäjiä, mutta olimme huolissamme taloudellisesta yksityisyydestä. Tutkimme kolikoita, jotka väittivät olevansa yksityisiä ja tämä sivu on tutkimuksemme tulos. Siksi valitsimme Moneron muiden sijaan. Joten jos vaikutamme puolueellisilta, olemme sitä, mutta uskomme että puolueettomuus perustuu tosiasioihin, jotka voit lukea alta ja tarkistaa itse.

### Yleiskatsaus

Valitse logo siirtyäksesi kyseisen kolikon analyysiin.

### Monero

Monero on ollut 100% avoimella lähdekoodilla alusta alkaen, mikä tarkoittaa että kuka tahansa voi tarkastella ohjelmiston [ lähdekoodia ](https://github.com/monero-project/bitmonero) varmistaakseen, ettei takaovia ole olemassa ja että ohjelmisto on turvallinen.

Monerolla on myös [ vertaisarvioituja tutkimuspapereita ](https://lab.getmonero.org/), jotka varmistavat matemaattisesti ja systemaattisesti kaikki sen yllä luetellut ominaisuudet.

### DASH

DASHilla on [ "rikas lista"](https://bitinfocharts.com/top-100-richest-darkcoin-addresses.html), joten tämä ei ole yksityinen kolikko. Kolikko-osoitteiden taloudelliset tiedot näkyvät kaikille lohkoketjua tutkiville.

> DASH isn't cryptographically private at all. Actually I had a slide in the deck that was like 'DASH, LOL,' and like nothing else... it's snakeoil and I'm just sort of beside myself about it, personally. 
> 
> **Gregory Maxwell** , Bitcoin Coren kehittäjä ja kryptografi [-esityksessä Coinbaselle ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

DASH isn't cryptographically private at all. Actually I had a slide in the deck that was like 'DASH, LOL,' and like nothing else... it's snakeoil and I'm just sort of beside myself about it, personally. 

**Gregory Maxwell** , Bitcoin Coren kehittäjä ja kryptografi [-esityksessä Coinbaselle ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

**Peter Todd** , toinen Bitcoin Core -kehittäjä ja kryptografi, on antanut [ samanlaisen lausunnon](https://twitter.com/petertoddbtc/status/622022840330682368).

### Zcash

Zcash-transaktiot ovat näkyvillä heidän lohkoketjussaan. Ne mahdollistavat piilotetut transaktiot, mutta [ alle 1% transaktioista on täysin suojattuja ](http://stat.bloxy.info/superset/dashboard/zcash/) . Koska piilotetut transaktiot ovat valinnaisia eivätkä oletuksena piilotettuja (harvoin käytetyistä puhumattakaan), [ piilotetut transaktiot erottuvat lohkoketjussa](http://weuse.cash/2016/06/09/btc-xmr-zcash/) ja kiinnittävät huomiota itseensä.

> Ja ohimennen, uskon että voimme onnistuneesti tehdä Zcashista tarpeeksi jäljitettävissä olevan WannaCryn kaltaisille rikollisille, mutta silti täysin yksityisesti & vaihdettavan. 
> 
> **Zooko Wilcox** , Zcashin toimitusjohtaja, [-twiitissä ](https://twitter.com/zooko/status/863202798883577856)

Ja ohimennen, uskon että voimme onnistuneesti tehdä Zcashista tarpeeksi jäljitettävissä olevan WannaCryn kaltaisille rikollisille, mutta silti täysin yksityisesti & vaihdettavan. 

**Zooko Wilcox** , Zcashin toimitusjohtaja, [-twiitissä ](https://twitter.com/zooko/status/863202798883577856)

Jos Zcash voi olla "liian jäljitettävissä", se ei voi olla täysin yksityinen tai vaihdettavissa. 

Tavalliset transaktiot ovat läpinäkyviä. Piilotetut transaktiot käyttävät zk-SNARKSia, jolla on vankat tietosuojatakuut tietyissä olosuhteissa. Kysymys kuuluu, täyttyykö näiden olosuhteiden ehdot, ja kun nähdään kuinka pieni määrä ihmisiä käyttää suojattuja ominaisuuksia, tämä jää kyseenalaiseksi.

Zcash on yritys, ja tällä hetkellä se [ ottaa 20% kaikesta louhitusta ZEC:stä perustajan palkkiona](https://z.cash/blog/funding.html). 

Zcash vaatii **Luotetun asennuksen**. Tämä tarkoittaa että sinun täytyy luottaa siihen, että järjestelmä on asennettu rehellisesti. Jos sitä ei määritetty rehellisesti, [ voitaisiin luoda rajoittamaton määrä ZEC:tä kenenkään tietämättä ](https://blog.okturtles.com/2016/03/the-zcash-catch/). Tämä tekisi hakkereista rikkaan ja alentaisi ZEC:n arvoa. Ei ole mahdollista tietää, suoritettiinko Trusted Setup rehellisesti. Meidän on luotettava heidän sanoihinsa. Tämä tuo järjestelmään inhimillisen vikapisteen, joka on vastoin melkein kaikkia muita kryptovaluuttoja. Sinun tulee luottaa vain kryptovaluuttojen matematiikkaan ja todennettavissa olevaan lähdekoodiin, ei ihmisiin. Kuten olemme nähneet käytännössä kaikkien suurten ohjelmistoyritysten, kuten [ Microsoftin](https://www.gnu.org/proprietary/proprietary-back-doors.en.html), [ Applen](http://www.digitaltrends.com/computing/apple-vs-fbi-backdoor-to-data-already-exists/) ja jopa hallitusten kohdalla, niihin ei pidä luottaa. 

Peter Todd, Bitcoin Core -kehittäjä, joka [ osallistui ](https://github.com/zcash/mpc/blob/master/README.md) Zcash Trusted Setupiin, on kutsunut sitä " [takaoveksi ](https://twitter.com/petertoddbtc/status/793584540891643906) ". 

> Zcash is not unconditionally sound, can't be with current tech...requires a trusted setup… will need to redo the procedure [Trusted Setup] to upgrade the crypto over time so it's a vulnerability. 
> 
> Gregory Maxwell, Bitcoin Core -kehittäjä ja kryptografi, [-esityksessä Coinbaselle](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

Zcash is not unconditionally sound, can't be with current tech...requires a trusted setup… will need to redo the procedure [Trusted Setup] to upgrade the crypto over time so it's a vulnerability. 

Gregory Maxwell, Bitcoin Core -kehittäjä ja kryptografi, [-esityksessä Coinbaselle](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

### Zcoin

**Huom:** Zcoin siirtyy nykyisestä Sigma-järjestelmästään uuteen protokollaan, joka perustuu sen uuteen työhön, Lelantukseen. Lelantus otetaan käyttöön vaiheittain, ja tässä artikkelissa oletetaan että kaikki vaiheet ovat valmiita ja toteutettu asianmukaisten vertailujen ja ennakoitujen toteutusaikojen rinnalla.

Syy, miksi Zcoinille annettiin tämä ylellisyys tulla arvostelluksi sen tulevan protokollan eikä nykyisen Zcashin perusteella johtuu siitä, että Zcoinilla on etenemissuunnitelma yleisillä aktivointiajoilla, kun taas Zcashin "yksityisyydensuojaus oletusarvoisesti" -suunnitelmat olivat ja ovat edelleen epäselviä. 

Zcoinilla (XZC) ei ole "rikasta listaa" (listaa henkilöistä tai organisaatioista, jotka hallitsevat merkittäviä määriä tiettyä kryptovaluuttaa), joten se on yksityinen. Oletuksena pakollisen tietosuojan odotetaan tulevan käyttöön vuonna 2021. Kun se on otettu käyttöön, Rikasta listaa ei voi luoda (vaikka tällä hetkellä [heillä on sellainen](https://www.coinexplorer.net/XZC/richlist)).

### Grin

### Bitcoin Mixers

Kaikki Bitcoin-tapahtumat näkyvät lohkoketjussa ja lohkoketjussa on [ Bitcoin rikkaiden lista](http://www.bitcoinrichlist.com/top100), joten Bitcoin ei ole yksityinen. Bitcoin on [ pseudonyymi](https://bitcoin.org/en/you-need-to-know), ei anonyymi. 

**Bitcoin-sekoittimien** kohdalla sinun täytyy luottaa siihen, että ne onnistuvat pitämään tietonsa turvassa eivätkä ne ole hallituksen, hakkereiden tai muiden tahojen omistuksessa tai yhteistyössä niiden kanssa. 

Heinäkuussa 2017 suurimman Bitcoin-sekoituspalvelun, BITMIXER.IO:n, perustaja ilmoitti sulkevansa ja antoi tämän syyksi: 

> … Now I grasped that Bitcoin is transparent non-anonymous system **by design**. Blockchain is a great open book… 
> 
> BITMIXER.IO, ilmoituksessa [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) -sivuston sulkemisesta (korostus alkuperäisessä). 

… Now I grasped that Bitcoin is transparent non-anonymous system **by design**. Blockchain is a great open book… 

BITMIXER.IO, ilmoituksessa [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) -sivuston sulkemisesta (korostus alkuperäisessä). 

Muutamaa viikkoa myöhemmin, harkittuaan erilaisia yksityisyyteen liittyviä kolikoita, hän sanoi tämän: 

> After the deep investigation I confirm that MONERO is the best privacy currency. So I strongly recommend MONERO for all people who need extra privacy. 
> 
> BITMIXER.IO, [-seurantaviestissä](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

After the deep investigation I confirm that MONERO is the best privacy currency. So I strongly recommend MONERO for all people who need extra privacy. 

BITMIXER.IO, [-seurantaviestissä](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Koska kaikki Bitcoin-tapahtumat näkyvät lohkoketjussa, KAIKKI Bitcoin-transaktiot voidaan jäljittää. Bitcoin-sekoitin voi hämärtää liiketoimia, mikä tekee Bitcoinien jäljittämisestä paljon vaikeampaa, mutta ei mahdotonta. Teknologian kehittyessä ja Bitcoin-transaktioiden jäljittämiseen erikoistuneiden yritysten yleistyessä erittäin hämärät tapahtumat tulevat suhteellisen helposti jäljitettäviksi: 

  * [ Lainvalvontaviranomaiset investoivat edelleen Bitcoin-seurantapalveluihin ](https://news.bitcoin.com/law-enforcement-continues-invest-bitcoin-tracking-services/)
  * [ Time.com: Bitcoineja on helpompi seurata kuin luulet ](http://time.com/3689359/bitcoins-track-anonymous/)
  * [ Elliptic: Yritys, joka on erikoistunut Bitcoinin jäljittämiseen lainvalvontaa varten ](https://www.elliptic.co/)

Google-haku paljastaa kymmeniä yllä olevien kaltaisia artikkeleita. Ja muista, että kaikki transaktiot, jotka tapahtuivat milloin tahansa aiemmin, ovat lohkoketjussa ja ne voidaan jäljittää, vaikka käytettäisiin sekoituspalvelua. Itse asiassa sekoituspalvelun käyttö kiinnittää huomion näihin liiketoimiin. 

Kaikki Bitcoinit eivät ole tasa-arvoisia samalla rahallisella arvolla. Useat tahot ovat lisänneet jotkin Bitcoinit mustalle listalle ja estäneet ne, mikä tekee niistä vähemmän arvokkaita kuin muut bitcoinit. Jos saat Bitcoineja, joita käytettiin aiemmin laittomiin tarkoituksiin, Bitcoinisi voi joutua mustalle listalle, vaikka sinulla ei ollut mitään tekemistä laittoman toiminnan kanssa. Tai esimerkiksi hallitus, työnantaja tai jokin muu taho päättää laittaa Bitcoinisi mustalle listalle tulevaisuudessa, aivan kuten varojen jäädyttämisen tai takavarikoinnin yhteydessä tapahtuu. Et voisi tehdä asialle mitään. Koska mikseri vain vaikeuttaa Bitcoinien jäljittämistä, tämä kategoria on merkitty "ei vaihdettavaksi". 

  * Andreas Antonopoulos, entinen Bitcoin Core -kehittäjä, jota arvostetaan hyvin Bitcoinissa ja muissa kryptovaluuttayhteisöissä, tunnustaa Bitcoinin vaihdettavuusongelman [ YouTube-video](https://www.youtube.com/watch?v=ak1iojpiHpM&feature=youtu .be&t=33m9s). 
  * Keskustelu Bitcoinin vaihdettavuusongelmasta osoitteessa [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=1190707.0)

## Yhteenveto

Mielestämme Monero on selkeä valinta jos etsit yksityistä, turvallista, jäljittämätöntä, vaihdettavaa, hajautettua kryptovaluuttaa ilman luotettavaa asennusta. Kaikki muu vaarantaa yksityisyytesi ja turvallisuutesi. Mutta älä usko vain meidän mielipidettämme. Tee omaa tutkimusta ja selvitä itse. Ota huomioon, että Moneroa tukevat ja käyttävät yhteisöt, jotka ovat riippuvaisia yksityisyydestä ja jäljittämättömyydestä, kuten: 

  * [ SIGAINT ](https://www.reddit.com/r/Monero/comments/4xqrzd/sigaint_launches_tor_monero_node_as_its_operators/)
  * [ Purism ](https://puri.sm/posts/purism-collaborates-with-cryptocurrency-monero-to-enable-mobile-payments/)
  * [ Wikileaks ](https://shop.wikileaks.org/donate#db9)
  * AlphaBay Market (AB) suljettiin heinäkuussa 2017. [ Federal Forfeiture Complaint ](https://assets.documentcloud.org/documents/3898109/AlphaBay-Cazes-Forfeiture-Complaint.pdf) AB:tä vastaan osoittaa, että: 
    * **Monero on ainoa yksityinen ja jäljittämätön kryptovaluutta:**   
"In total, from CAZES' wallets and computer agents took control of approximately $8,800,000 in Bitcoin, Ethereum, Moreno [sic], and Zcash, broken down as follows: 1,605.0503851 Bitcoin, 8,309.271639 Ethereum, 3,691.98 Zcash, _and an unknown amount of Monero._ " (bottom of p. 20 and top of p. 21, emphasis added) 
    * **Bitcoin-tapahtumat eivät ole yksityisiä, ja ne voidaan jäljittää:**   
"Federal agents obtained the warrants after tracing a number of Bitcoin transactions originating with AlphaBay to digital currency accounts, and ultimately bank accounts and other tangible assets, held by CAZES and his wife." (p. 17, lines 24-26) 

  * **Monero on ainoa yksityinen ja jäljittämätön kryptovaluutta:**   
"In total, from CAZES' wallets and computer agents took control of approximately $8,800,000 in Bitcoin, Ethereum, Moreno [sic], and Zcash, broken down as follows: 1,605.0503851 Bitcoin, 8,309.271639 Ethereum, 3,691.98 Zcash, _and an unknown amount of Monero._ " (bottom of p. 20 and top of p. 21, emphasis added) 
  * **Bitcoin-tapahtumat eivät ole yksityisiä, ja ne voidaan jäljittää:**   
"Federal agents obtained the warrants after tracing a number of Bitcoin transactions originating with AlphaBay to digital currency accounts, and ultimately bank accounts and other tangible assets, held by CAZES and his wife." (p. 17, lines 24-26) 

LocalMonero ei suosittele tai rohkaise laitottomaan toimintaan. 

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

  * [Kuinka CLSAG parantaa Moneron tehokkuutta](/knowledge/what-is-clsag/)

  * [Miksi Monerolla on "Tail Emission"](/knowledge/monero-tail-emission/)

  * [Moneron lyhyt historia](/knowledge/monero-history/)

  * [Wired Magazine on väärässä Monerosta, tässä miksi](/knowledge/wired-article-debunked/)

  * [15 parasta Monero-myyttiä ja -huolia, jotka on kumottu](/knowledge/monero-myths-debunked/)

  * [Kuinka Dandelion++ pitää Moneron tapahtuman alkuperän yksityisenä](/knowledge/monero-dandelion/)

  * [Miksi Monero on avoimen lähdekoodin ja hajautettu](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Moneron louhinta: Mikä tekee RandomX:stä niin erityisen?](/knowledge/monero-mining-randomx/)