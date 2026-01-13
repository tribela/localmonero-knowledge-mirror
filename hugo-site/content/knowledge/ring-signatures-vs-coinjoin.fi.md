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

Koska kaikki Bitcoinissa tapahtuvat tapahtumat ovat täysin läpinäkyviä – paljastaen lähettäjän, vastaanottajan ja summat – käyttäjien on ryhdyttävä ylimääräisiin toimiin suojellakseen yksityisyyttään varojensa aiemmilta lähettäjiltä ja tulevilta vastaanottajilta tai uhkaavat sensuurin, valvonnan tai varojen varastamisen fyysistä väkivaltaa.

Paras ratkaisu bitcoinin yksityisyyteen tänään on työkalu nimeltä ["CoinJoin"](https://bitcoiner.guide/qna/coinjoin/), jossa vähintään kaksi käyttäjää työskentelee yhdessä (yleensä keskitetyn koordinaattorin kautta) luodakseen erityisen tapahtuman, joka vaikeuttaa ulkopuolisten tarkkailijoiden yhdistämistä tulot lähtöihin. Jokainen osallistuja kommunikoi rakentavansa tapahtuman yhdessä luovuttamatta varojensa säilytysoikeutta ja saa lopussa tulosteen, jonka aikaisempi historia on nyt epäselvä (tai sekoittunut) ulkopuolisille tarkkailijoille.

Tämä rikkoo tiettyjen UTXO:iden historian, jolloin Bitcoin-käyttäjät voivat saada jonkin verran eteenpäin suuntautuvaa salaisuutta asioidessaan. CoinJoinilla (jotka toteutetaan Wasabi Walletissa ja Samourai Walletissa, kahdessa eniten käytetyssä CoinJoin-työkalussa Bitcoinille) on kuitenkin muutamia merkittäviä haittoja:

  * Koska CoinJoin-tapahtumat ovat täysin vapaaehtoisia ja edellyttävät aktiivista osallistumista, jokainen osallistuja osoittaa väistämättä pyrkivänsä parempaan yksityisyyteen kuin "normaalit" Bitcoin-käyttäjät, mikä mahdollisesti erottaa heidät ja aiheuttaa ongelmia varojen käyttämisessä monissa säännellyissä pörsseissä tai yhteisöissä. Jokainen käyttäjä ei voi kiistää osallistuneensa CoinJoin-tapahtumaan.
  * Löytääkseen muita CoinJoinin kanssa useimmat CoinJoin-lähestymistavat (mukaan lukien Wasabi Wallet) käyttävät keskitettyä koordinaattoria, joka yhdistää osallistujat ja auttaa heitä kommunikoimaan ja rakentamaan kunnollisen CoinJoin-tapahtuman. Tämä keskitetty koordinaattori ei koskaan valvo käyttäjien varoja, mutta hän saa laajan käsityksen koordinoimistaan tapahtumista, voi sensuroida saapuvat tiedot (kuten Wasabi Walletin tapauksessa) ja sitä voidaan painostaa keräämään tai jakamaan tietoja CoinJoin-osallistujista.
  * Käyttäjät, joilla on suuria määriä varoja CoinJoinille, voivat usein joutua odottamaan tunteja (tai jopa päiviä!) löytääkseen tarpeeksi osallistujia CoinJoinille, mikä johtaa suuriin viiveisiin siitä hetkestä, jolloin käyttäjä saa varoja siihen, kun hän voi käyttää ne yksityisesti. 
  * CoinJoin-tapahtuman tarjoama yksityisyys heikkenee ajan myötä, kun muut osallistujat käyttävät varoja tai linkittävät tuotoksensa identiteettiinsä KYC-pörssien, tunnukset vaativien kauppiaiden jne. kautta. Tämä tarkoittaa, että käyttäjät pitävät ihanteellisesti varansa jatkuvassa CoinJoin-tapahtumissa. heidän nimettömyytensä ("crowd to hide in") on asetettu mahdollisimman tuoreeksi.
  * Useimmissa CoinJoin-lähestymistavoissa osallistujien on käytettävä kiinteän kokoista UTXO:ta (eli 0,1 BTC), jotta CoinJoin-tapahtumien tulojen ja lähtöjen yhdistäminen vaikeutuu. Tämä johtaa korkeampiin maksuihin (enemmän erillisiä tapahtumia tarvitaan isoa syöttöä kohti), enemmän "myrkyllisiin muutoksiin" (varoihin, joita ei voida käyttää ilman vakavia riskejä yksityisyydelle) ja voi estää pienempiä käyttäjiä ollenkaan sekoittumasta, jos heillä ei ole vaadittava vähimmäissaldo.

## Miten sormusallekirjoitukset ratkaisevat nämä ongelmat?

Koska [ olemme tutkineet perinpohjaisesti, mitä sormusallekirjoitukset ovat menneisyydessä](/knowledge/ring-signatures), en tässä blogiviestissä käsittele yksityiskohtaisesti niiden toimivuuden teknisiä näkökohtia. Sen sijaan katsomme, kuinka Monerossa otetut lähestymistavat ratkaisevat CoinJoinin ongelmat yllä.

> CoinJoin on mukana ja vaatii osallistumisen

Moneron sormusallekirjoitukset ovat yksityisyysprotokollan ydinominaisuus, ja _jokainen_ verkon tapahtuma käyttää niitä. Tämä tarkoittaa, että yksikään käyttäjä ei erotu siitä, että hän pyrkii parempaan yksityisyyteen kuin "normaalit" Monero-käyttäjät, ja kaikki käyttäjät saavat uskottavan epäilyksen, että he olisivat käyttäneet varoja missä tahansa tapahtumassa. Koska varoja käyttävä käyttäjä ei koordinoi tai osallistu tapahtumaan syöttisyötteisiin, käyttäjät, jotka omistavat syöttiksi valittuja syötteitä, voivat rehellisesti sanoa, että he eivät osallistuneet kyseiseen tapahtumaan, mikä vahvistaa heidän yksityisyyttään.

> Keskitetyn koordinaattorin käyttö

Koska Moneron sormusallekirjoitukset ovat täysin koordinoimattomia ja vaativat vain todellisen varojen käyttäjän tapahtuman luomiseen, Monerossa ei tarvita keskitettyä koordinaattoria. Tämä varmistaa, että _kukaan_ ei voi estää sinua pääsemästä yksityisyyteen Monerossa, eikä ole olemassa keskitettyä kokonaisuutta, jota voidaan painostaa, ei helppoja Sybil-hyökkäyksiä likviditeettiä vastaan jne. Niin kauan kuin tapahtumasi maksaa asianmukaiset maksut, saat sensuroimattoman pääsyn yksityisyyteen, tietoturvaan ja nimettömyyteen Monerossa.

> CoinJoin vaatii likviditeettiä

Jokaisen Moneron houkuttimina käyttävien käytettävissä oleva "likviditeetti" on aina ketjussa olevien tulosteiden kokonaismäärä, joten Moneron kanssa piiloutuvista houkuttimista ei ole koskaan pulaa. Joku, joka haluaa käyttää Moneroa, voi tehdä sen noin 20 minuuttia varojen vastaanottamisen jälkeen, eikä hänen tarvitse suorittaa mitään lisätoimenpiteitä saadakseen vahvan yksityisyyden Monerossa.

> CoinJoinin tietosuoja heikkenee ajan myötä

Koska verkko ei koskaan tunne Moneron lähtöjä, soittoäänien tarjoama yksityisyys on paljon vähemmän herkkä huonontumaan ajan myötä. Käyttäjän ei tarvitse jatkuvasti vaimentaa Moneron lähtöjä, ja äärimmäisen harvinaisten olosuhteiden ulkopuolella hän ei menetä yksityisyyttä ajan myötä.

Jos käyttäjä haluaa "päivittää" lähdön kanssa käytettyjä houkuttimia, hän voi kuitenkin vain lähettää varat takaisin itselleen ja käyttää ne tavalliseen tapaan ~20 minuuttia myöhemmin.

> CoinJoin vaatii yleensä kiinteän kokoisia tuloja

Koska summat piilotetaan jokaisessa ["Luottamuksellisia tapahtumia"](/knowledge/monero-ringct) käyttävässä tapahtumassa (osa "RingCT:tä"), missä tahansa tapahtumassa käytettävät houkuttimet voivat olla minkä kokoisia tahansa. Ei ole mitään syytä olla huolissaan Moneron määräperusteisista heuristioista, joten tapahtumat ovat paljon yksinkertaisempia rakentaa ja voivat hyödyntää houkuttimia mistä tahansa ajankohdasta ja minkä tahansa summan Monero-lohkoketjussa.

## Miten voin oppia lisää?

Jos olet utelias ja haluat ymmärtää paremmin sormusallekirjoituksia tai CoinJoin-transaktioita, katso alla olevista linkeistä upeita paikkoja aloittaa:

  * [How Ring Signatures Obscure Monero’s Outputs](/knowledge/ring-signatures)
  * [Ring Signature – Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [CoinJoin Overview](https://6102bitcoin.com/coinjoin-overview/)

Lue lisää