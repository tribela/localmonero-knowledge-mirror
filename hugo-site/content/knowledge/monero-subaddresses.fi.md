---
title: "Kuinka Monero-aliosoitteet estävät identiteetin yhdistämisen"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero on aina löytänyt innovatiivisia tapoja ratkaista vaikeita yksityisyysongelmia. Usein nämä innovaatiot johtavat muihin innovaatioihin, ja joskus näitä tuloksena olevia teknologioita voidaan käyttää jopa sellaisiin käyttötapauksiin joita ei ole aiemmin edes harkittu. Tästä ei Moneron aliosoiteteknologiaa parempaa esimerkkiä ole.

Kuvittele hypoteettinen yksityisyysongelma, jossa yhden osoitteen käyttö useilla alustoilla näennäisesti toisiinsa liittymättömiltä ihmisiltä voi johtaa mainittujen joukkojen yhdistämiseen ja tunnistamiseen. Yksinkertaisesti sanottuna, jos olisit henkilö nimeltä Billy Joe Bob ja myisit omenoita Bitcoinilla, saatat lähettää Bitcoin-osoitteesi julkiseen paikkaan, jotta asiakkaat voivat maksaa sinulle. Oletetaan, että osoite alkaa aakkosnumeerisella merkkijonolla 7XybV3... Mutta heittäen syrjään ilmeisen tietosuojariskin siitä, että kuka tahansa voi tarkistaa Bitcoin-saldosi ja nähdä kuinka paljon olet myynyt, on toinen asia, josta ei usein puhuta tietosuojariskinä. Oletetaan, että olet omenamyyjän lisäksi öisin hakkeri, jonka nimi on l33tz0r. Teet ilmiantotyötä, kerrot pahaa-aavistamattomalle väestölle hallituksen korruptiosta ja sinun on ehdottomasti pidettävä henkilöllisyytesi salassa. Hyväksyt Bitcoin-lahjoituksia työllesi ja julkaiset osoitteen julkisella foorumilla. Se on sama osoite, johon otat rahaa vastaan asiakkailta omenamyynnistä. Juuri tämä aiemmin mainittu 7XybV3... osoite.

Yksinkertainen, mutta tuhoisa tunnistushyökkäys olisi Internetin hakukoneen käyttäminen Bitcoin-osoitteesi etsimiseen. Osoitteen 7XybV3... lisääminen hakukoneeseen tuottaa kaksi erilaista tulosta. Omenaliiketoiminta ja l33tz0r. Tämä riittää yhdistämään nämä kaksi identiteettiä ja tunnistamaan hakkerin nimeltä l33tz0r, mikä saattaa aiheuttaa pelottavia seurauksia olemassa olevilta valtuuksilta.

On tärkeää huomata, että tämä hyökkäys on MYÖS mahdollista Monerolla. Vaikka Monero piilottaa suurimman osan lohkoketjun tiedoista, tämä hyökkäys ei käytä mitään tietoja. Se käyttää vain osoitetta, joka on jaettava maksun vastaanottamiseksi. Julkisesti anonyymien lahjoitusten tapauksessa. Tämä on yksi mahdollinen tapa, jolla Moneron käyttäjät voivat tahattomasti vahingoittaa omaa yksityisyyttään ja se on myös esimerkki siitä, kuinka Monero on yksityisyyden säilyttämisen huipputasolla, mutta se ei ole luodinkestävä.

Tavallinen tapa selvittää tämä ongelma oli omistaa useita lompakoita. Kun jokaiselle henkilöllisyydelle (tai käyttötapaukselle) on käytetty eri osoitteita, niitä ei voi yhdistää toisiinsa. Mutta tämä yksityisyys on voimassa vain, jos käyttäjä ei koskaan sekoita niitä. Väärän osoitteen vahingossa lähettämisellä olisi samat linkitysvaikutukset. Lisäksi jokaisen osoitteen seed on pidettävä turvassa, mikä lisää jokaisen uuden lompakon tarvittavaa InfoSec-työtä.

Moneron ratkaisu oli aliosoitteet. Mahdollisuus luoda aivan valtava määrä osoitteita pääosoitteen alle käyttämällä sitä eräänlaisena seedinä. Jokainen luotu aliosoite voi hyväksyä Moneroa, ja kaikki se menee samaan lompakkoon. Tällä menetelmällä yhdellä osoitteella toimivien identiteettien määrä on valtava, samalla kun InfoSec-työmäärä pysyy minimissä. Nämä osoitteet eivät myöskään ole matemaattisesti linkitettävissä, joten ellei käyttäjä huuda itse niiden yhteyttä julkisesti, ulkopuolisen tarkkailijan on todella vaikea yhdistää niitä.

Mutta toinen mielenkiintoinen käyttötapa syntyi alaosoitteista; se korvasi yleisesti vihatut maksutunnukset.

Maksutunnusten avulla kauppiaat pystyivät tunnistamaan, mikä asiakas lähetti minkäkin maksun. Koska Moneron tiedot ovat piilotettu lohkoketjussa, transaktion vastaanottaja ei näe, mikä osoite sen lähetti. Tämä tarkoittaa, että jos on samanhintaisia tuotteita ja useita tilauksia, voi olla mahdotonta tunnistaa, kuka osti mitä. Maksutunnukset ovat yksilöllinen, satunnainen merkkijono, jonka kauppias luo ja antaa asiakkaalle. Asiakas lisää tämän erilliseksi kenttään transaktiota lähettäessään. Tämä satunnainen merkkijono sijoitetaan lohkoketjuun osana transaktiota, ja tällä tavalla kauppias pystyy tunnistamaan ja lajittelemaan saapuvat tapahtumat.

Tässä menetelmässä oli useita virheitä. Ensinnäkin se heikentää lohkoketjussa olevien tietojen yhdenmukaisuutta. Ainutlaatuiset lisämetatiedot voivat saada jotkin transaktiot erottumaan joukosta, mikä mahdollistaa heuristisen analyysin. Tämä pätee erityisesti silloin, kun näitä metatietoja ei pakoteta kaikille. Tämän pakolliseksi tekeminen kaikille lisäisi kuitenkin tarpeetonta dataa lohkoketjuun, eikä sitä haluta. Lisäksi, jos maksutunnusta käytettäisiin uudelleen jostain syystä, olisi helppoa linkittää kaksi transaktiota toisiinsa. Tämä tapahtui tyypillisesti pörssitalletuksilla, ja kuka tahansa saattoi helposti linkittää transaktiot että talletukset pörssiin yhdeksi tietyksi henkilöksi.

Toiseksi UX-näkökulmasta maksutunnukset luovat toisen askeleen, johon muista kolikoista tulevat kryptovaluutan käyttäjät eivät ole tottuneet, ja jos ne unohtuvat, se aiheuttaa valtavaa päänsärkyä kauppiaalle, jonka on tunnistettava nämä transaktiot sitten muilla keinoin. Tämä tehtiin yleensä puhumalla suoraan jokaisen asiakkaan kanssa, joka unohti antaa maksutunnuksen ja vahvistamalla muut tunnistetiedot, jotka vain he saattoivat tietää, kuten summan, lähetyspäivämäärän ja transaktiotunnuksen yhdistelmän.

Tämä ylimääräinen vaihe jäi monilta väliin, ja mentiin siihen pisteeseen, että jotkin pörssit alkoivat veloittaa asiakkailta rahaa, jos heidän talletuksensa piti hakea manuaalisesti maksutunnuksen unohtamisen vuoksi. Toiset kiristelivät hampaitaan ja hyväksyivät ylimääräiset kustannukset, mutta kukaan ei ollut tyytyväinen niihin.

Tähän oli yksi ratkaisu, integroidut osoitteet, jotka yhdistävät osoitteen ja maksutunnuksen yhdeksi merkkijonoksi, joten sitä ei voitu unohtaa, mutta käyttöönotto oli melko heikkoa huolimatta siitä mitä etuja kauppiaat olisivat saaneet sen käyttöönotosta. 

Mielenkiintoisessa tilanteessa Moneron aliosoitteet pelastivat päivän. Mahdollisuus luoda suuria määriä aliosoitteita pääosoitetta kohden ja tunnistaa, mitkä transaktiot joutuivat mihinkin aliosoitteisiin, antoi kauppiaille mahdollisuuden päästä eroon maksutunnuksista tyylikkäällä tavalla samalla kun otettiin käyttöön seuraavan sukupolven Monero-tekniikka. Siitä lähtien useimmat pörssit ja kauppiaat ovat siirtyneet käyttämään aliosoitteita ensisijaisena tapana tunnistaa transaktioita.

Yksityisyysongelman ratkaisuna alkanut ratkaisu muuttui joksikin paljon isommaksi, mikä ratkaisi merkittävän UX-ongelman sekä kauppiaille että asiakkaille. Innovaatiot synnyttävät lisää innovaatioita, jotka voivat usein johtaa odottamattomiin voittoihin kaikille. Monero on nähnyt tämän kerta toisensa jälkeen ja näkee paljon vaivaa edistääkseen lohkoketjua mahdollisuuksien rajoissa. Kuka tietää, mitä muita asioita voimme kehittää yhdessä?

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