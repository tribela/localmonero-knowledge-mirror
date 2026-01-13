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