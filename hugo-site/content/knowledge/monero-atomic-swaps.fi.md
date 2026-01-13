---
title: "Kuinka Atomic Swapit toimivat Monerossa"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Kryptovaluutta-maailmassa hajautetun ja valtuuttoman järjestelmän tavoittelussa harvat asiat ovat niin haluttuja kuin hajautetut pörssit ja "Atomic Swapit". Perustamisestaan lähtien Monero on kamppaillut "Atomic Swappien" toteuttamisessa, sillä yksityisyysominaisuudet luovat ainutlaatuisia ongelmia protokollaa suunniteltaessa.

Mutta pakitetaan ensin. Mitä ovat "Atomic Swapit"? Atomic swap on operaatio, jonka avulla kahden eri lohkoketjun kryptovaluutat voidaan vaihtaa keskenään ilman kolmannen osapuolen apua. Tämä tarkoittaa, että jos joku haluaisi vaihtaa kryptovaluutan A kryptovaluuttaan B, hän voisi tehdä sen ilman keskitettyä tai hajautettua vaihtoa. Kuten voisi kuvitella, tämä vaatii huomattavasti tutkimusta ja kaikki tekniset yksityiskohdat jotka mahdollistavat sen, ovat melko monimutkaisia. Jälleen kerran LocalMonero on täällä auttamassa ja antamassa yksinkertaisen selityksen tavalliselle ihmiselle.

Aluksi tarkastellaan yksinkertaisinta Atomic Swapin muotoa, jonka Bitcoin on toteuttanut. Jos joku haluaa vaihtaa Bitcoinin toiseen kolikkoon, joka käyttää samaa "hash time lock contract" -tekniikkaa, hän voi tehdä sen seuraavalla tavalla. Alicella on Bitcoin (BTC), mutta hän haluaa Litecoinin (LTC) ja Bobilla on LTC, mutta hän haluaa BTC:n. He päättävät tehdä Atomic Swapin, jotta jokainen saa haluamansa kolikon. Alice lähettää BTC:nsä erityiseen osoitteeseen käyttämällä skriptejä, jotka lukitsevat varat pois niin, ettei hänkään pääse niihin käsiksi. Voit ajatella sitä kuin Alice laittaisi BTC:nsä lukittuun laatikkoon. Kun lukkolaatikko on tehty, hän saa avaimen ja lähettää tämän avaimen hashin Bobille. Nyt Bobilla ei ole itse avainta, vain hash, joten hän ei voi vielä käyttää varoja.

Bob käyttää tätä hashia "seedinä", josta hän luo oman lukituslaatikon ja lähettää LTC:nsä sinne, missä se myös lukitaan. Koska Alicen avaimen hashia käytettiin seedinä, jolla Bobin lukkolaatikko luotiin, hän voi käyttää avaimensa lunastaakseen LTC:n Bobin lukkolaatikosta. Hänen avaimensa sopii! Mutta käyttämällä matemaattista voodoo-taikaa, kun hän avaa avaimellaan LTC-lukon, hän paljastaa avaimen Bobille, joka voi sitten käyttää sitä lunastaakseen BTC:n, jonka hän laittoi lukkolaatikkoonsa. Tällä tavalla, ilman välittäjää, Alice ja Bob ovat onnistuneesti vaihtaneet omaisuutensa.

Mutta siinä on pieni ongelma. Mitä jos Alice lähettää lukkolaatikkoonsa ja Bob päättää, ettei halua enää käydä kauppaa. Nyt koska Alice ei pääse käsiksi BTC:ään, jonka hän lukitsi ja Bob ei suorita osuuttaan kaupasta, Alice menettää rahansa ikuisesti. No, onneksi Bitcoinissa on tekniikka, jota kutsutaan palautustransaktioiksi joten tietyn ajan kuluttua, jos Bob ei ole lunastanut BTC:tä, skripteihin on sisäänrakennettu vikasieto, jossa BTC palaa automaattisesti Alicelle. Tämä oli Moneron ydinswap-toteutuksen ensisijainen tavoite. Moneron [ring allekirjoitusten tietosuojateknologian](/knowledge/ring-signatures) ansiosta tapahtuman lähettäjä on aina tuntematon. Kuinka protokolla voi suorittaa hyvitystapahtuman, jos se ei edes tiedä, mistä tapahtuma tuli?

Vuonna 2017 pieni ryhmä tutkijoita hahmotteli erilaisen menetelmän, jolla Atomic Swap toimisi Monerossa. Useiden vuosien tutkimisen jälkeen tutkijat viimeistelivät prosessin, jolla Monero pystyisi tekemään Atomic Swappeja Bitcoinin kanssa jopa ilman palautustapahtumia.

Kuten monien tämän tason teknisen monimutkaisten asioiden kohdalla, selityksemme yksinkertaistaa joitain asioita liikaa idean välittämiseksi, mutta se antaa silti vankan käsityksen mekanismeista, joilla tämä prosessi toimisi.

Sekä Alicen (jolla on XMR ja haluaa BTC:n) että Bobin (jolla on BTC ja haluaa XMR:n) on ladattava ja suoritettava ohjelma, joka tukee Atomic Swappia. Tämä voidaan toteuttaa lompakoissa, hajautetuissa vaihtokeskuksissa tai tietyissä erityisohjelmissa, mutta ohjelmiston on käytettävä Atomic Swapin protokollaa. Ensimmäisessä vaiheessa Alicen ja Bobin asiakkaat muodostavat yhteyden toisiinsa ja tekevät useita yhteisiä salauksia ja avaimia. Tässä vaiheessa luodaan uusi Monero-osoite, jossa Alicella on toinen puoli avaimesta ja Bobilla toinen. Siellä ei kuitenkaan ole vielä Moneroa, joten ei ole mitään kulutettavaa. Viimeinen asia, joka on huomioitava tästä osoitteesta, on se, että molemmilla on tämän lompakon katseluavain, joten he voivat molemmat kurkistaa sisään nähdäkseen, saapuuko Monero tai milloin se saapuu.

Toisessa vaiheessa Bob lähettää BTC:nsä erityiseen osoitteeseen, joka on samanlainen kuin Bitcoinin Atomic Swap protokolla, josta olemme jo keskustelleet. Kun Alice näkee BTC:n saapuvan tähän osoitteeseen lohkoketjussa, hän lähettää Moneronsa Monero-osoitteeseen, johon hänellä ja Bobilla on molemmilla puolikas avain. Bob voi varmistaa, että Monero saapui koska hänellä on myös katseluavain, ja kun hän näkee Moneron olevan turvallisesti lompakossa, hän lähettää Alicelle avaimenpalan, jonka avulla tämä voi nostaa Bitcoinin. Kuten toisessa protokollassa, Bitcoinin lunastusprosessi paljastaa hänen puolet Monero-avaimesta Bobille. Nyt Bobilla on molemmat puolikkaat, joten hän voi lunastaa Moneron, kun taas Alicella on vain hänen puolikas, joten hän ei voi yrittää ottaa sitä ennen Bobia.

Jos tarkastelet tätä kaikkea ja olet edelleen hieman hämmentynyt siitä, kuinka Monero pystyi kiertämään hyvitystapahtumien ongelman, vastaus on melko yksinkertainen. Koska Monerolla itsessään ei ole hyvitystapahtumia, lukijan tulisi huomata, että Bitcoin (jolla on hyvitystapahtumia) lähetetään ensin, ja vasta sen jälkeen, kun sen on varmistettu olevan lohkoketjussa, lähetetään Monero. Tämän ansiosta Monero voi hyödyntää Bitcoinin kykyä palautustapahtumissa ja hyödyntää niitä ilman, että sillä itsellään tarvitsee olla näitä ominaisuuksia.

Atomic Swap on nyt valmis, mutta tästä lähtien Bobilla on pari vaihtoehtoa äskettäin hankkimaansa XMR:ään. Hän voi käyttää tätä Monero-lompakkoa sellaisenaan tai siirtää XMR:n toiseen lompakkoon, jonka hän jo omistaa. Bob todennäköisesti siirtää Moneron toiseen lompakkoon, koska Alicella on edelleen katseluavain ja hän näkee nykyiseen Monero-lompakkoon.

Tämän protokollan kauneus on, että se on vielä melko uusi, ja siinä on runsaasti tilaa optimoinnille. Se on myös melko joustava arkkitehtuuriltaan, joten toteutus muissa lompakoissa tai hajautetuissa keskuksissa tulisi olla yksinkertaista ja sopia selkeästi niiden olemassa olevaan arkkitehtuuriin.

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