---
title: "Katselutunnisteet: Kuinka yksi tavu vähentää Moneron lompakon synkronointiaikoja yli 40%"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Yksi yleisimmistä valituksista Moneron päivittäisessä käytössä on aika, joka voi kestää lompakon synkronoinnissa ennen kuin Moneron lähettäminen onnistuu. Onneksi Monero-yhteisön kehittäjät ja tutkijat ovat löytäneet loistavan tavan lyhentää lompakkosi synkronointiin kuluvaa aikaa yli 40% ilman lohkoketjun paisumista, lisättyjä maksuja jne.

Esittelyssä "näkymätunnisteet", yhden tavun lisäys jokaisen transaktion tietoihin – tulossa Moneroon seuraavassa verkkopäivityksessä!

## Miksi Moneron lompakon synkronointi on hitaampaa kuin Bitcoinin?

## Miksi Moneron lompakon synkronointi on hitaampaa kuin Bitcoinin?

Yksi ensimmäisistä kysymyksistä, joihin meidän on vastattava ymmärtääksemme paremmin näkymätunnisteiden kaltaisten ratkaisujen tarvetta on se, miksi Moneron lompakon synkronointi on hitaampaa kuin Bitcoinin kaltaiset kryptovaluutat.

Koska Bitcoinissa kaikki transaktiot eivät ole yksityisiä ja paljastavat käytetyt kolikot, summat ja ketjussa mukana olevat osoitteet, Bitcoin-lompakot voivat yksinkertaisesti etsiä käyttämättömiä transaktioulostuloja (UTXO) tai käytettyjä osoitteita tietylle lompakolle, skannata nopeasti lohkoketjusta vain kyseisten osoitteiden omistamia UTXO-kolikoita selvittääkseen, mitkä kolikot kuuluvat lompakkoosi ja jotka voidaan käyttää.

Monerossa kaikki transaktiot kuitenkin säilyttävät käyttäjän yksityisyyden piilottamalla lähettäjän, vastaanottajan ja kuhunkin transaktioon liittyvät summat. Tämä yksityisyys, joka on elintärkeää verkon käyttäjien suojelemiseksi, myös hidastaa lompakon synkronointia. Monerossa lompakkosi on verrattava jokaista verkossa olevaa transaktioulostuloa (TXO) lompakkosi yksityisiin avaimiin.

Tämä vertailu sisältää paljon monimutkaista matematiikkaa ja kryptografiaa sen vahvistamiseksi, että ulostulo on todella sinun, koska kaikki summat, osoitteet ja tunnetut käytetyt ulostulot (tai kolikot) on piilotettu Moneron ketjuun.

## Mitä näkymätunnisteet ovat?

## Mitä näkymätunnisteet ovat?

Vähentääkseen Monero-lompakoiden synkronointiaikaa [tutkija nimeltä UkoeHB keksi uudenlaisen lähestymistavan](https://github.com/monero-project/research-lab/issues/73) – lisäämällä 1-tavuisen "tagin" jokaiseen transaktioon käyttämällä vain tunnettua jaettua salaisuutta tapahtuman lähettäjälle ja vastaanottajalle.

Lähettäjä luo tämän jaetun salaisuuden käyttämällä vastaanottajan hänelle antamaa osoitetta, eikä se vaadi aktiivista yhteistyötä lähettäjältä ja vastaanottajalta. Tämän jaetun salaisuuden ensimmäinen tavu (tai merkki) lisätään sitten transaktion tietoihin, kun se julkaistaan Monero-verkkoon.

Kun joku transaktion osallistujista haluaa synkronoida lompakkonsa Monero-lohkoketjun kanssa sen sijaan, että hänen olisi suoritettava monimutkainen matematiikka ja kryptografia jokaiselle verkon TXO:lle, lompakko voi nyt vain tarkistaa, onko tuo 1-tavuinen kenttä jokaisessa transaktiossa ja vasta sitten suorittaa aikaa vievän tarkistuksen transaktioille, joissa on kyseinen tunniste – 1/256 TXO:ta verkossa, tarkalleen ottaen!

Tämä tunniste ei paljasta transaktioita koskevia tietoja ulkopuolisille katsojille, vaan se lisää vain 1 tavun (mitätön määrä) transaktiokokoihin, ja silti antaa meille mahdollisuuden lyhentää synkronointiaikoja yli 40% vähentämällä monimutkaisia välttämättömiä vahvistuksia!

## Näkymätunnisteet: yksinkertaistettu esimerkki

## Näkymätunnisteet: yksinkertaistettu esimerkki

Kuvittele, että sinulla on huoneessa 4 096 laatikkoa, joista vain 5 kuuluu sinulle. Kaikki laatikot eivät ole täysin erotettavissa ulkopuolelta ja ainoa tapa tietää onko laatikko sinua varten, on avata se ja ratkaista aikaa vievä matemaattinen tehtävä, joka on kirjoitettu sisälle varmistaaksesi, että se on sinun.

Kuvittele nyt, että päätät, että henkilö joka lähettää sinulle nuo 5 laatikkoa, luo erikoiskoodin käyttämällä osoitettasi ja laittaa sitten vain tuon koodin ensimmäisen merkin jokaisen sinulle lähetettävän laatikon ulkopuolelle. Kaikki muut tekevät saman asian laatikoilleen (varmistaakseen, että kaikki laatikot ovat edelleen erotettavissa), mutta nyt voit yksinkertaisesti katsoa yhden merkin koodia laatikon ulkopuolella ja avata vain ne laatikot, joissa kyseinen merkki on. 

Vaikka muut laatikot vastaavat koodiasi, jopa jotkut, jotka eivät ole sinun, avattava laatikoiden määrä ja ratkaistavien matemaattisten tehtävien määrä on nyt vain 16 (1/256 laatikkoa!) kaikkien 4 096 sijaan. 

Nyt avaat ne 16 laatikkoa, ratkaiset matemaattiset tehtävät ja pidät 5 laatikkoa, jotka todella kuuluvat sinulle tästä ryhmästä!

## Milloin näkymätunnisteet ovat saatavilla Monerossa?

## Milloin näkymätunnisteet ovat saatavilla Monerossa?

Näkymätunnisteet ovat yksi ominaisuuksista, joita tällä hetkellä suunnitellaan sisällytettäväksi [tulevaan verkkopäivitykseen](https://github.com/monero-project/meta/issues/630), ja ne pitäisi julkaista joskus tänä keväänä. Yhteisö [ keräsi 23.3XMR:ää](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (kirjoitushetkellä) kannustaakseen näkymätunnisteiden kehittämistä ja käyttöönottoa, ja tämän seurauksena suurin osa työstä näkymätunnisteiden sisällyttämiseksi Monero-koodipohjaan on jo tehty. Työn viimeisteli "j-berman" yhteistyössä arvioijien ja tutkijoiden kanssa.

Kun verkko on pakottanut näkymätunnisteet, kaikki verkkopäivityksen jälkeen lähetetyt transaktiot hyötyvät huomattavasti parannetusta lompakon synkronointiajasta. Sinun ei tarvitse tehdä mitään erityistä aloittaaksesi näkymätunnisteiden käyttö, vaan suosikki Monero-lompakkosi alkaa käyttää niitä automaattisesti verkkopäivityksen jälkeen!

## Miten voin oppia lisää?

## Miten voin oppia lisää?

Jos tämä on herättänyt uteliaisuutesi näkymätunnisteiden suhteen, katso alta muutamia lisälinkkejä, jotka käsittelevät aihetta syvällisesti:

  * [Reduce scan times with 1-byte-per-output ‘view tag’ ](https://github.com/monero-project/research-lab/issues/73)
  * [Add view tags to outputs to reduce wallet scanning time](https://github.com/monero-project/monero/pull/8061)

Lue lisää

  * [Kuinka Monero ainutlaatuisesti mahdollistaa kiertotaloudet](/knowledge/monero-circular-economies)/

  * [Moneron sormusallekirjoitukset vs CoinJoin kuten Wasabissa](/knowledge/ring-signatures-vs-coinjoin)/

  * [Miksi (ja miten!) sinun pitäisi hallita omia avaimiasi](/knowledge/hold-your-keys)/

  * [Osallistuminen Moneroon](/knowledge/contributing-to-monero)/

  * [Kuinka etäsolmut vaikuttavat Moneron yksityisyyteen](/knowledge/remote-nodes-privacy)/

  * [Kuinka Monero käyttää hard forkkeja verkon päivittämiseen](/knowledge/network-upgrades)/

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