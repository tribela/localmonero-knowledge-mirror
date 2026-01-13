---
title: "Obročni ring podpisi Monero vs CoinJoin kot v Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Orodja za zasebnost v Bitcoinu so postala vse bolj opazna in uporabna, zato so se znašla pod regulativnim nadzorom. Ta nadzor je privedel do [nedavne objave](https://twitter.com/wasabiwallet/status/1503091503207432193) orodja za zasebnost Bitcoina, Wasabi Wallet, da bo začelo cenzurirati in zavračati vhodne vhode v mikse, za katere meni, da so nezakoniti ali v nasprotju z njihovim ToS, in da bo plačalo podjetju za analizo verige za "preverjanje" vhodnih udeležencev miksa.

Uporaba transakcij CoinJoin za prikrivanje vira sredstev v Bitcoinu je že več let jedro zasebnosti v Bitcoinu, težave in tveganja, povezana z njeno uporabo, pa so nekatere od glavnih težav, ki jih obročni podpisi Monero odpravljajo in preprečujejo.

V tem prispevku se bomo na kratko poglobili v primerjavo CoinJoina in obročnih podpisov ter pojasnili, zakaj pristop, uporabljen v Moneru, zagotavlja večjo odpornost cenzuri, večjo zasebnost in manj težav za uporabnike.

## Kaj je CoinJoin transakcija?

Ker so vse transakcije v Bitcoinu popolnoma pregledne - razkrivajo pošiljatelja, prejemnika in zneske -, morajo uporabniki sprejeti dodatne ukrepe za zaščito zasebnosti pred prejšnjimi pošiljatelji in prihodnjimi prejemniki svojih sredstev, sicer tvegajo cenzuro, nadzor ali krajo sredstev s fizičnim nasiljem.

Najboljša današnja rešitev za zasebnost v Bitcoinu je orodje, imenovano ["CoinJoin"](https://bitcoiner.guide/qna/coinjoin/), kjer dva ali več uporabnikov sodeluje (običajno prek centraliziranega koordinatorja) in ustvari posebno transakcijo, ki zunanjim opazovalcem otežuje povezavo med vhodi in izhodi. Vsak udeleženec komunicira, da bi skupaj ustvaril transakcijo, ne da bi predal skrbništvo nad svojimi sredstvi, na koncu pa prejme izhod, katerega prejšnja zgodovina je zdaj zunanjim opazovalcem nejasna (ali zakrita).

S tem se prekine zgodovina določenih UTXO, kar uporabnikom Bitcoina omogoča, da pri transakcijah pridobijo nekaj malega skrivnosti za naprej. Vendar ima CoinJoin (kot je implementiran v denarnici Wasabi Wallet in Samourai Wallet, dveh najpogosteje uporabljenih orodjih CoinJoin za Bitcoin) nekaj večjih pomanjkljivosti: 

  * Ker so transakcije CoinJoin popolnoma prostovoljne in zahtevajo aktivno udeležbo, vsak udeleženec neizbežno pokaže, da si prizadeva za večjo zasebnost kot "običajni" uporabniki bitcoinov, kar ga lahko izloči in povzroči težave pri porabi sredstev na številnih reguliranih borzah ali subjektih. Vsak uporabnik ne more zanikati, da je sodeloval v transakciji CoinJoin.
  * Da bi našli druge, s katerimi bi lahko opravili CoinJoin, večina pristopov k CoinJoinu (vključno z denarnico Wasabi) uporablja centraliziranega koordinatorja, ki povezuje udeležence in jim pomaga komunicirati ter vzpostaviti ustrezno transakcijo CoinJoin. Ta centralizirani koordinator nikoli nima skrbništva nad sredstvi uporabnikov, vendar ima obsežen vpogled v transakcije, ki jih koordinira, lahko cenzurira vhodne podatke (kot v primeru denarnice Wasabi) in je lahko pod pritiskom prisiljen zbirati ali deliti informacije o udeležencih CoinJoin.
  * Uporabniki z velikimi zneski sredstev za CoinJoin morajo pogosto čakati več ur (ali celo dni!), da najdejo dovolj udeležencev za CoinJoin, kar vodi do velikih zamud od trenutka, ko uporabnik prejme sredstva, do trenutka, ko jih lahko zasebno porabi. 
  * Zasebnost, ki jo zagotavlja transakcija CoinJoin, se sčasoma zmanjša, ko drugi udeleženci porabijo sredstva ali povežejo svoje izide s svojo identiteto prek borz KYC, trgovcev, ki zahtevajo identifikacijo, itd. To pomeni, da je idealno, če uporabniki svoja sredstva v transakcijah CoinJoin nenehno obračajo, da bi ohranili čim bolj svež nabor anonimnosti ("množico, v kateri se lahko skrijejo").
  * V večini pristopov k CoinJoinu morajo udeleženci uporabljati UTXO fiksne velikosti (npr. 0,1 BTC), da bi otežili povezovanje vhodov in izhodov transakcij CoinJoin. To vodi do višjih pristojbin (več ločenih transakcij, potrebnih za velik vhod), več "strupenih sprememb" (sredstva, ki jih ni mogoče porabiti brez resnih tveganj za zasebnost) in lahko manjšim uporabnikom sploh onemogoči mešanje, če nimajo zahtevanega minimalnega stanja.

## Kako obročni ali "ring" podpisi rešujejo te težave?

Ker[ smo se v preteklosti že poglobili v to, kaj so obročni podpisi](/knowledge/ring-signatures), zato v tem prispevku ne bomo podrobno opisovali tehničnih vidikov njihovega delovanja. Namesto tega si bomo ogledali kako pristopi, ki so jih uporabili v Moneru, rešujejo težave s CoinJoinom.

> CoinJoin je opt-in in zahteva sodelovanje 

Obročni ozr. Ring podpisi Monero so osrednja značilnost protokola zasebnosti in jih uporablja vsaka transakcija v omrežju. To pomeni, da transakcije nobenega uporabnika ne izstopajo zaradi iskanja večje zasebnosti od "običajnih" uporabnikov Monera, vsi uporabniki pa pridobijo verodostojno možnost zanikanja, da so pri posamezni transakciji porabili sredstva. Ker uporabnik, ki porabi sredstva, v transakciji ne usklajuje ali sodeluje z vložki za vabo, lahko tisti uporabniki, ki imajo v lasti vložke, ki so slučajno izbrani kot vabe, pošteno povedo, da niso sodelovali v tej transakciji, kar okrepi njihovo zasebnost.

> Uporaba centraliziranega koordinatorja

Ker obročni podpisi Monero v celoti niso koordinirani in za ustvarjanje transakcije potrebujejo le pravega porabnika sredstev, v Moneru ni potrebe po centraliziranem koordinatorju. To zagotavlja, da _nihče_ ne more preprečiti dostopa do zasebnosti v Moneru, prav tako ni centraliziranega subjekta, na katerega bi lahko pritiskali, ni enostavnih napadov Sybila na likvidnost itd. Dokler s svojo transakcijo plačujete ustrezne pristojbine, v Moneru pridobite necenzuriran dostop do zasebnosti, varnosti in anonimnosti.

> CoinJoin zahteva likvidnost 

"Likvidnost", ki je na voljo vsakomur, ki porabi Monero, da jo uporabi kot vabo, je vedno celoten nabor izhodov na verigi, zato nikoli ne zmanjka vabe, v katero se lahko skrijete z Monero. Nekdo, ki želi porabiti Monero, lahko to stori ~20min po prejemu sredstev in mu ni treba opraviti nobenih dodatnih korakov, da bi pridobil močno zasebnost v Moneru.

> Zasebnost CoinJoin se sčasoma poslabša

Ker izhodi Monero niso znani, je zasebnost, ki jo zagotavljajo obročni oz. "ring" podpisi, veliko manj dovzetna za poslabšanje s časom. Uporabniku ni treba nenehno spreminjati izhodov in ne izgublja zasebnosti, razen v izjemno redkih okoliščinah.

Če želi uporabnik "osvežiti" vabe, ki jih je uporabil z izhodom, lahko sredstva preprosto pošlje nazaj k sebi in jih kot običajno porabi cca 20 minut pozneje.

> CoinJoin običajno zahteva vnose fiksne velikosti 

Ker so zneski v vsaki transakciji skriti z uporabo [ "Zaupne transakcije "](/knowledge/monero-ringct) (del "RingCT"), so lahko vabe, uporabljene v posamezni transakciji, poljubno velike. V Moneru ni razloga, da bi bilo treba skrbeti za hevristiko, ki temelji na znesku, zato so transakcije veliko enostavnejše za izdelavo in lahko uporabljajo vabe iz katere koli točke v času in katere koli vrednosti v blokovni verigi Monero.

## Kako lahko izvem več?

Če ste radovedni in želite bolje razumeti obročne podpise ali transakcije CoinJoin, so spodnje povezave odlična mesta za začetek: 

  * [Kako obročni oz "ring" podpisi prikrijejo izhode Monera ](/knowledge/ring-signatures)
  * [Obročni ali "Ring" Podpis - Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [Pregled CoinJoin](https://6102bitcoin.com/coinjoin-overview/)

Nadaljnje branje