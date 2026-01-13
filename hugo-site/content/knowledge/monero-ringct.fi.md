---
title: "Kuinka RingCT piilottaa Monero-transaktiosummat"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Moneron yksityisyys ei riipu yhdestä yksittäisestä mekanismista, joka rikkoutuessaan paljastaisi transaktiot kokonaisuudessaan, vaan pikemminkin kolmesta eri tekniikasta, jotka toimivat rinnakkain tarjotakseen kokonaisvaltaista yksityisyyttä samalla kun kompensoidaan muiden osien heikkouksia. Tämä kolmiosainen lähestymistapa koostuu [sormusallekirjoituksista](/knowledge/ring-signatures), RingCT:stä ja ["stealth" osoitteista](/knowledge/monero-stealth-addresses). Nämä kolme tekniikkaa piilottavat todellisen ulostulon (lähettäjän), määrän ja vastaanottajan. Tänään puhumme RingCT:stä.

RingCT on luultavasti teknisin näistä kolmesta ja sitä voi olla vaikea ymmärtää, joten emme kerro sen toimintaa tarkasti, vaan pikemminkin näytämme kuinka on mahdollista olla tietämättä määrää ja silti vahvistaa asioita siitä. Ja älä huoli, käytämme paljon esimerkkejä kuten aina.

Selvitetään ensin, miksi on tärkeää tarkistaa summat. Miksi emme voi vain pitää niitä täysin salassa? Vastaus on, että on olemassa älykkäitä tapoja, joilla ihmiset voivat luoda rahaa tyhjästä, jos heille annetaan mahdollisuus. Miten tällainen voisi toimia? Katsotaanpa esimerkkiä.

Jos haluat ostaa jotain ystävältäsi ja hän haluaa siitä kymmenen dollaria, aloitat kymmenellä dollarilla ja hän aloittaa nollasta. Kun annat hänelle kymmenen dollaria, hänellä on kymmenen dollaria ja sinulla on nolla. Aloitit kymmenellä, ja nyt hänellä on kymmenen. Tässä tapahtumassa ei luotu tai tuhottu rahaa.

Kryptovaluutoilla älykäs henkilö voi antaa tuotteesta kymmenen dollaria, ja sen sijaan, että hän saisi nolla dollaria vaihtorahaa, hän voi saada kaksi dollaria takaisin. Sen sijaan, että 0 ja 10 johtaisivat 10:een ja 0:aan (tai 10=10), nyt 0 ja 10 johtaa 10:een ja 2:een (tai 10=12). Kaksi Moneroa luotiin aivan tyhjästä. Voit kuvitella, että jos henkilö tekisi tämän itselleen useita kertoja, hän voisi kerätä jättimäisen omaisuuden lyhyessä ajassa.

Bitcoinin ja muiden kanssa tämä olisi helppo nähdä tapahtuvan. Tarkastelet transaktioihin meneviä tuloja ja poistuvia ulostuloja varmistaen, että lähetetty vastaa vastaanotettua. Jos nämä summat salattiin eivätkä ne näkyneet, käyttäjällä ei ole mahdollisuutta varmistaa, että lähetettävä ja vastaanotettu seikka on sama.

Yrittääkseen lisätä Bitcoinin yksityisyyttä Gregory Maxwell loi Confidential Transactionsin (CT), uuden teknologian, joka mahdollistaa salattujen summien käytön samalla, kun hän todistaa ettei prosessissa luotu tai tuhottu mitään. Kuten useimmat yksityisyysteknologiat, se ei toteutunut Bitcoinissa, mutta Monero halusi ottaa sen käyttöön. Oli vain yksi ongelma. Jo toteutettu sormusallekirjoitustekniikka ei ollut yhteensopiva ehdotetun idean kanssa. Niinpä yksi silloisista MRL-tutkijoista, Shen Noether, muunsi CT:n RingCT:ksi, CT:n versioksi joka oli yhteensopiva sormusallekirjoitusten kanssa.

Jälleen kerran tämän toimintatapa on melko tekninen, ja sitä olisi vaikea selittää johdantoartikkelissa. Salausharrastajalle, joka välttämättä haluaa tietää, on Internetissä paljon perusteellisia artikkeleita CT:n sisäisestä toiminnasta. Meille muille tämä artikkeli näyttää, kuinka summat voi olla mahdollista piilottaa, mutta silti todistaa, ettei mitään luotu tai tuhottu.

Oletetaan, että Alice halusi lähettää Bobille rahaa. Alice lähettää 10 XMR Bobille, joka saa 10 XMR. 10=10 joten tässä ei ole mitään vikaa. Mutta Alice ei halua kenenkään tietävän, kuinka paljon hän lähettää. Joten hän ja Bob luovat yhteisen salaisuuden. Periaatteessa numero, jonka vain he kaksi tietävät. Oletetaan, että luku on 22. Nyt Alice kertoo 10:llä (mitä hän todella lähettää) 22 saadakseen 220. Tämä on numero, jonka hän jakaa verkon kanssa.

Louhijat eivät itse tiedä salaista numeroa. Jos he tietäisivät, he voisivat jakaa heille näytettävän numeron salaisella numerolla ja saada todellisen lähetettävän summan. Mutta koska he eivät tiedä, he eivät voi. He näkevät kuitenkin, että Bob saa 220. 220 lähetetty. 220 vastaanotettu. 220 = 220. Tällä tavalla verkko voi varmistaa, ettei Moneroa ole luotu tai tuhottu tietämättä todellista summaa, jonka Alice lähetti Bobille.

Koska Bob tietää jaetun salaisen numeron, vastaanottaessan rahat hän jakaa vain 22:lla saadakseen selville todellisen Alicen lähettämän summan, 10. Alice ja Bob tietävät molemmat, kuinka paljon lähetettiin ja kuinka paljon vastaanotettiin. Kaikille muille annetaan väärä numero.

Jälleen kerran, tämä ei ole varsinainen tapa, jolla CT toimii, mutta se antaa käsityksen siitä kuinka tällainen voisi olla mahdollista. Todellinen tapa sisältää asioita, kuten Pedersenin sitoumukset, kaksi lähetettyä summaa (yksi salattu summa vastaanottajalle ja yksi sitoutumissumma verkkoon) ja… joo, on jo helppo nähdä, kuinka tämä kaikki voi mennä yli hilseen.

Yksi huomioitava asia on kuitenkin se, että vaikka RingCT piilottaa transaktion kahden osapuolen välisen summan, se ei piilota kahta muuta numerosarjaa.

Ensimmäinen on kolikkopohjaiset tapahtumat. Jos tämä termi on sinulle tuntematon, se tarkoittaa periaatteessa palkkiota, jonka louhijat saavat seuraavan lohkon löytämisestä. Tätä numeroa ei ole piilotettu. Kuka tahansa näkee, kuinka paljon protokolla on myöntänyt louhijalle heidän työstään. Tällä tavalla olemassa olevan Moneron nykyinen määrä voidaan tietää laskemalla yhteen kaikki kolikkopohjaiset transaktiot. Niiden summa on yhtä suuri kuin nykyinen liikkeessä oleva Monero.

Toinen ei-piilotettu numero on maksu, joka maksetaan louhijoille, kun käyttäjä lähettää transaktion. Maksujen on oltava näkyvillä, jotta louhijat voivat tietää mitä priorisoida. Tämä on tapa, jolla käyttäjät voivat kuitenkin vahingoittaa heidän yksityisyyttään, sillä jos joku käyttää yksilöllistä louhimispalkkiota joka kerta kun hän lähettää transaktion (kuten 0,12345), hänen transaktiot voidaan linkittää.

Muuten kuin nämä tapaukset, RingCT on piilottanut Monero-summia vuodesta 2017 lähtien ja kollektiivinen yksityisyytemme on sitäkin vahvempi.

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