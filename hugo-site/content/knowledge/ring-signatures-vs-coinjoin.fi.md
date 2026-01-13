---
title: "Moneron sormusallekirjoitukset vs CoinJoin kuten Wasabissa"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Kun Bitcoinin tietosuojatyökalut ovat saaneet enemmän huomiota ja käyttöä, ne ovat joutuneet aiempaa enemmän sääntelyn valvonnan alle. Tämä tarkastelu on johtanut Bitcoin-tietosuojatyökalun Wasabi Walletin [äskettäiseen ilmoitukseen](https://twitter.com/wasabiwallet/status/1503091503207432193), jonka mukaan he alkavat sensuroida ja hylätä saapuvia syöttöjä sekoituksiin, joita he pitävät laittomina tai käyttöehtojensa vastaisina, ja maksavat ketjuanalyysin yritykselle "tarkastaakseen" saapuvat mix-osallistujat.

CoinJoin-tapahtumien käyttö Bitcoinin varojen lähteen hämärtämiseen on ollut Bitcoin-yksityisyyden ydin jo useiden vuosien ajan, ja sen käyttöön liittyvät ongelmat ja riskit ovat joitakin ydinongelmista, joita Moneron sormusallekirjoitukset korjaavat ja estävät. .

Tässä blogiviestissä sukellamme lyhyesti CoinJoin- ja sormusallekirjoitusten vertailuun sekä siihen, miksi Moneron lähestymistapa johtaa parempaan sensuurin vastustuskykyyn, parempaan yksityisyyteen ja vähempään vaivaan käyttäjille.

## Mikä on CoinJoin-transaktio?

## Mikä on CoinJoin-transaktio?

Koska kaikki Bitcoinissa tapahtuvat tapahtumat ovat täysin läpinäkyviä – paljastaen lähettäjän, vastaanottajan ja summat – käyttäjien on ryhdyttävä ylimääräisiin toimiin suojellakseen yksityisyyttään varojensa aiemmilta lähettäjiltä ja tulevilta vastaanottajilta tai uhkaavat sensuurin, valvonnan tai varojen varastamisen fyysistä väkivaltaa.

Paras ratkaisu bitcoinin yksityisyyteen tänään on työkalu nimeltä ["CoinJoin"](https://bitcoiner.guide/qna/coinjoin/), jossa vähintään kaksi käyttäjää työskentelee yhdessä (yleensä keskitetyn koordinaattorin kautta) luodakseen erityisen tapahtuman, joka vaikeuttaa ulkopuolisten tarkkailijoiden yhdistämistä tulot lähtöihin. Jokainen osallistuja kommunikoi rakentavansa tapahtuman yhdessä luovuttamatta varojensa säilytysoikeutta ja saa lopussa tulosteen, jonka aikaisempi historia on nyt epäselvä (tai sekoittunut) ulkopuolisille tarkkailijoille.

Tämä rikkoo tiettyjen UTXO:iden historian, jolloin Bitcoin-käyttäjät voivat saada jonkin verran eteenpäin suuntautuvaa salaisuutta asioidessaan. CoinJoinilla (jotka toteutetaan Wasabi Walletissa ja Samourai Walletissa, kahdessa eniten käytetyssä CoinJoin-työkalussa Bitcoinille) on kuitenkin muutamia merkittäviä haittoja:

  * Koska CoinJoin-tapahtumat ovat täysin vapaaehtoisia ja edellyttävät aktiivista osallistumista, jokainen osallistuja osoittaa väistämättä pyrkivänsä parempaan yksityisyyteen kuin "normaalit" Bitcoin-käyttäjät, mikä mahdollisesti erottaa heidät ja aiheuttaa ongelmia varojen käyttämisessä monissa säännellyissä pörsseissä tai yhteisöissä. Jokainen käyttäjä ei voi kiistää osallistuneensa CoinJoin-tapahtumaan.
  * Löytääkseen muita CoinJoinin kanssa useimmat CoinJoin-lähestymistavat (mukaan lukien Wasabi Wallet) käyttävät keskitettyä koordinaattoria, joka yhdistää osallistujat ja auttaa heitä kommunikoimaan ja rakentamaan kunnollisen CoinJoin-tapahtuman. Tämä keskitetty koordinaattori ei koskaan valvo käyttäjien varoja, mutta hän saa laajan käsityksen koordinoimistaan tapahtumista, voi sensuroida saapuvat tiedot (kuten Wasabi Walletin tapauksessa) ja sitä voidaan painostaa keräämään tai jakamaan tietoja CoinJoin-osallistujista.
  * Käyttäjät, joilla on suuria määriä varoja CoinJoinille, voivat usein joutua odottamaan tunteja (tai jopa päiviä!) löytääkseen tarpeeksi osallistujia CoinJoinille, mikä johtaa suuriin viiveisiin siitä hetkestä, jolloin käyttäjä saa varoja siihen, kun hän voi käyttää ne yksityisesti. 
  * CoinJoin-tapahtuman tarjoama yksityisyys heikkenee ajan myötä, kun muut osallistujat käyttävät varoja tai linkittävät tuotoksensa identiteettiinsä KYC-pörssien, tunnukset vaativien kauppiaiden jne. kautta. Tämä tarkoittaa, että käyttäjät pitävät ihanteellisesti varansa jatkuvassa CoinJoin-tapahtumissa. heidän nimettömyytensä ("crowd to hide in") on asetettu mahdollisimman tuoreeksi.
  * Useimmissa CoinJoin-lähestymistavoissa osallistujien on käytettävä kiinteän kokoista UTXO:ta (eli 0,1 BTC), jotta CoinJoin-tapahtumien tulojen ja lähtöjen yhdistäminen vaikeutuu. Tämä johtaa korkeampiin maksuihin (enemmän erillisiä tapahtumia tarvitaan isoa syöttöä kohti), enemmän "myrkyllisiin muutoksiin" (varoihin, joita ei voida käyttää ilman vakavia riskejä yksityisyydelle) ja voi estää pienempiä käyttäjiä ollenkaan sekoittumasta, jos heillä ei ole vaadittava vähimmäissaldo.

## Miten sormusallekirjoitukset ratkaisevat nämä ongelmat?

## Miten sormusallekirjoitukset ratkaisevat nämä ongelmat?

Koska [ olemme tutkineet perinpohjaisesti, mitä sormusallekirjoitukset ovat menneisyydessä](/knowledge/ring-signatures), en tässä blogiviestissä käsittele yksityiskohtaisesti niiden toimivuuden teknisiä näkökohtia. Sen sijaan katsomme, kuinka Monerossa otetut lähestymistavat ratkaisevat CoinJoinin ongelmat yllä.

> CoinJoin on mukana ja vaatii osallistumisen

CoinJoin on mukana ja vaatii osallistumisen

Moneron sormusallekirjoitukset ovat yksityisyysprotokollan ydinominaisuus, ja _jokainen_ verkon tapahtuma käyttää niitä. Tämä tarkoittaa, että yksikään käyttäjä ei erotu siitä, että hän pyrkii parempaan yksityisyyteen kuin "normaalit" Monero-käyttäjät, ja kaikki käyttäjät saavat uskottavan epäilyksen, että he olisivat käyttäneet varoja missä tahansa tapahtumassa. Koska varoja käyttävä käyttäjä ei koordinoi tai osallistu tapahtumaan syöttisyötteisiin, käyttäjät, jotka omistavat syöttiksi valittuja syötteitä, voivat rehellisesti sanoa, että he eivät osallistuneet kyseiseen tapahtumaan, mikä vahvistaa heidän yksityisyyttään.

> Keskitetyn koordinaattorin käyttö

Keskitetyn koordinaattorin käyttö

Koska Moneron sormusallekirjoitukset ovat täysin koordinoimattomia ja vaativat vain todellisen varojen käyttäjän tapahtuman luomiseen, Monerossa ei tarvita keskitettyä koordinaattoria. Tämä varmistaa, että _kukaan_ ei voi estää sinua pääsemästä yksityisyyteen Monerossa, eikä ole olemassa keskitettyä kokonaisuutta, jota voidaan painostaa, ei helppoja Sybil-hyökkäyksiä likviditeettiä vastaan jne. Niin kauan kuin tapahtumasi maksaa asianmukaiset maksut, saat sensuroimattoman pääsyn yksityisyyteen, tietoturvaan ja nimettömyyteen Monerossa.

> CoinJoin vaatii likviditeettiä

CoinJoin vaatii likviditeettiä

Jokaisen Moneron houkuttimina käyttävien käytettävissä oleva "likviditeetti" on aina ketjussa olevien tulosteiden kokonaismäärä, joten Moneron kanssa piiloutuvista houkuttimista ei ole koskaan pulaa. Joku, joka haluaa käyttää Moneroa, voi tehdä sen noin 20 minuuttia varojen vastaanottamisen jälkeen, eikä hänen tarvitse suorittaa mitään lisätoimenpiteitä saadakseen vahvan yksityisyyden Monerossa.

> CoinJoinin tietosuoja heikkenee ajan myötä

CoinJoinin tietosuoja heikkenee ajan myötä

Koska verkko ei koskaan tunne Moneron lähtöjä, soittoäänien tarjoama yksityisyys on paljon vähemmän herkkä huonontumaan ajan myötä. Käyttäjän ei tarvitse jatkuvasti vaimentaa Moneron lähtöjä, ja äärimmäisen harvinaisten olosuhteiden ulkopuolella hän ei menetä yksityisyyttä ajan myötä.

Jos käyttäjä haluaa "päivittää" lähdön kanssa käytettyjä houkuttimia, hän voi kuitenkin vain lähettää varat takaisin itselleen ja käyttää ne tavalliseen tapaan ~20 minuuttia myöhemmin.

> CoinJoin vaatii yleensä kiinteän kokoisia tuloja

CoinJoin vaatii yleensä kiinteän kokoisia tuloja

Koska summat piilotetaan jokaisessa ["Luottamuksellisia tapahtumia"](/knowledge/monero-ringct) käyttävässä tapahtumassa (osa "RingCT:tä"), missä tahansa tapahtumassa käytettävät houkuttimet voivat olla minkä kokoisia tahansa. Ei ole mitään syytä olla huolissaan Moneron määräperusteisista heuristioista, joten tapahtumat ovat paljon yksinkertaisempia rakentaa ja voivat hyödyntää houkuttimia mistä tahansa ajankohdasta ja minkä tahansa summan Monero-lohkoketjussa.

## Miten voin oppia lisää?

## Miten voin oppia lisää?

Jos olet utelias ja haluat ymmärtää paremmin sormusallekirjoituksia tai CoinJoin-transaktioita, katso alla olevista linkeistä upeita paikkoja aloittaa:

  * [How Ring Signatures Obscure Monero’s Outputs](/knowledge/ring-signatures)
  * [Ring Signature – Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [CoinJoin Overview](https://6102bitcoin.com/coinjoin-overview/)

Lue lisää

  * [Kuinka Monero ainutlaatuisesti mahdollistaa kiertotaloudet](/knowledge/monero-circular-economies)/

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