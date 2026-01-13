---
title: "Moneron Outputit selitettynä"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero, kuten muutkin kryptovaluutat, käyttää ulostuloja varojen kirjanpitoon. Monet kryptotaitajat ovat luultavasti kuulleet tämän termin aiemmin, mutta kaikki eivät ymmärrä, mitä se tarkoittaa ja miten se toimii. Kuten [sormusallekirjoituksia käsittelevässä artikkelissamme](/knowledge/ring-signatures) on tutkittu, ulostulot ovat todellisia yksiköitä, jotka vaihdetaan lohkoketjussa transaktioiden välillä. Samanlainen kuin dollariseteli, mutta summa ei ole kiinteässä nimellisarvossa.

Jos sinulle maksetaan 16 dollaria työstä, saatat saada yhden dollarin setelin, viiden dollarin setelin ja kymmenen dollarin setelin. Sinulla on 16 dollaria, mutta lompakossasi on myös kolme erilaista seteliä. Jos halusit maksaa jollekin 6 dollaria, voit käyttää viiden ja yhden dollarin seteliä, mutta jos halusit maksaa jollekin 8 dollaria, voit käyttää vain 10 dollaria ja saada 2 dollaria takaisin vaihtorahana. Lopuksi, jos haluat maksaa jollekulle 14 dollaria, sinun on käytettävä kaikki kolme seteliä ja saisit 2 dollaria takaisin vaihtorahana, mutta hetkeksi, kun luovutat kaikki kolme laskua, sinulla ei ole rahaa lompakossasi ennen kuin saat vaihtorahaa takaisin.

Monero toimii samalla tavalla. Oletetaan, että pyörität kauppaa ja myyt kolmesti kolmea eri tuotetta. Saatat saada 1,5 XMR, 2,25 XMR ja 5,25 XMR eli yhteensä 9 XMR:ää, mutta lompakossasi on myös kolme erilaista ulostuloa, jotka vastaavat aiemmin mainittuja arvoja. Aivan kuten dollareissa, saatat haluta maksaa jollekin 3 XMR. Voit käyttää vain 5,25 XMR-ulostuloa ja vastaanottaa 2,25 XMR takaisin vaihdossa tai voit yhdistää 1,5 ja 2,25 XMR-ulostulot ja saada 0,75 XMR takaisin muutoksessa.

Mutta heti kun lähetät transaktion, käyttämäsi ulostulot asetetaan "lukittuun" tilaan, mikä tarkoittaa, että niihin ei pääse käsiksi ennen kuin saat vaihtorahan takaisin. Protokolla vapauttaa varat (eli palauttaa muutoksen) 10 vahvistuksen jälkeen tai noin 20 minuutin kuluttua. Aivan kuten seteleitä luovutettaessa lompakosta, et voi käyttää rahoja uudelleen ennen kuin saat rahan takaisin kassalta, Moneroakaan ei voi käyttää ennen kuin saat rahat takaisin.

Palataanpa esimerkkiin, jossa lähetetään 3 XMR jollekin, ja käytät 5.25 XMR -ulostuloa. Nyt, kun odotat 1,75 XMR:ää takaisin muutoksessa, et voi käyttää sitä. Tämä 1.75 XMR ei ole käytettävissäsi. Mutta voit silti käyttää 1,5 XMR- ja 2,25 XMR -ulostuloja, koska niitä ei käytetty. Palatakseni dollariesimerkkiin, jos maksoit jollekulle 8 dollaria, kuten edellisessä esimerkissä, et voi käyttää 2 dollaria, jota odotat vaihtorahoina, ennen kuin se on annettu sinulle, mutta tässä esimerkissä sinulla on silti 10 dollarin seteli, joka on käyttämätön lompakossasi. Tällä voit silti ostaa mitä haluat, kun odotat vaihtorahoja. Sama Moneron kanssa.

Tämä aiheuttaa usein hämmennystä uusille Monero-käyttäjille. Usein käyttäjällä voi olla lompakossa vain yksi ulostulo, joka on saatu pörssistä tai ystävältä. Oletetaan, että tämä ulostulo on 20 XMR. Heillä ei ole muita ulostuloja lompakossa. He haluavat nyt tehdä lahjoituksen kahdelle suosikki hyväntekeväisyysjärjestölleen. He lähettävät 5 XMR:ää ensimmäiseen hyväntekeväisyysjärjestöön ja ovat sitten hämmentyneitä, koska vaikka heillä pitäisi olla 15 XMR:ää jäljellä, he eivät voi lähettää välittömästi seuraavaa lahjoitusta toiselle hyväntekeväisyysjärjestölle. Kuten saatat arvata, tämä johtuu siitä että 15 XMR on lukittu. Sitä ei voi käyttää ennen kuin se on palautettu vaihtorahoina (10 vahvistusta tai noin 20 minuuttia). Kun heidän varat on avattu, he voivat lähettää toisen lahjoituksensa.

Toistaakseni asian, heillä ei olisi ollut tätä ongelmaa, jos heillä olisi sen sijaan ollut useita ulostuloja, kuten kaksi 10 XMR-ulostuloa tai vastaavaa. He voisivat lähettää molemmat lahjoitukset peräkkäin, koska ensimmäinen lahjoitus käyttäisi yhtä 10 XMR-lähdöstä (ja odottaisi 10 vahvistusta saadakseen 5 XMR:ää takaisin vaihdossa), ja toinen lahjoitus käyttäisi toista 10 XMR:än ulostuloa.

Joissakin kryptovaluuttalompakoissa on ominaisuus nimeltä "ulostulon hallinta", joka yksinkertaisesti näyttää käyttäjälle, mitkä ulostulot heillä on tällä hetkellä (kokonaissumman lisäksi), sekä antaa käyttäjälle mahdollisuuden valita, mitä he haluavat käyttää kuluttaessaan heidän kryptovaluuttaansa.

Tästä lähtien Moneron graafinen käyttöliittymä tekee ulostulovalinnan käyttäjille automaattisesti, koska käyttäjät jotka valitsevat oman lähtönsä, päätyvät usein hämmentymään tai joissakin tapauksissa yksityisyyden loukkaamiseen. Rakenteilla on kuitenkin lompakoita, kuten uusi Feather-lompakkoprojekti, joka sisältää nämä ulostulojen hallintaominaisuudet.

Olemme puhuneet paljon lähetysosuudesta, mutta vastaanottavassa päässä tapahtuu jotain kiehtovaa. Palatakseni esimerkkiimme 3 XMR:n lähettämisestä jollekin ja 1,5 XMR:n ja 2,25 XMR:n ulostulojen käyttämisestä transaktiossa (samalla kun odotetaan 0,75 XMR:n vaihtorahaa), vastaanottaja EI saa kahta 1,5 XMR:n ja 2,25 XMR:n ulostuloa. Sen sijaan ne vastaanottavat YHDEN 3 XMR-ulostulon.

Protokolla yhdistää taustalla kaikki kulutukseen käytetyt ulostulot ja antaa vastaanottajalle yhden ulostulon maksetusta summasta ja lähettää yhden vaihtoulostulon takaisin lähettäjälle. Joten lähettäjä saa myös yhden ulostulon takaisin vaihtorahana riippumatta siitä, käyttikö hän tapahtuman lähettämiseen kahta, kolmea vai kymmentä ulostuloa.

Toivomme, että tämä on poistanut hämmennystä ulostuloista ja protokollan sisäisen kirjanpidon toiminnasta sekä yleisestä käyttäjän kohtaamasta hämmästyksestä, kun hän kohtaa lukitut varat. Toisessa artikkelissa tutkimme ulostulojesi hallintaa, jotta minimoidaan mahdollisuus joutua odottamaan lukitsemattomia varoja ennen tulevien transaktioiden lähettämistä.

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

  * [Kuinka Monero-aliosoitteet estävät identiteetin yhdistämisen](/knowledge/monero-subaddresses)/

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