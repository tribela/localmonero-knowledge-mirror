---
title: "Monero rudarjenje: zakaj je RandomX tako poseben"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
30\. novembra 2019 je imel Monero svoj polletni hard fork, pri čemer je bila najbolj pričakovana sprememba prehod s starega algoritma PoW, cryptonight, na popolnoma novega, interno razvitega, RandomX. Skupnost Monero verjame, da je RandomX velik korak k enakopravnemu rudarjenju, a poglejmo globlje, da vidimo, ali je temu res tako.

## Namen

Da bi lahko presodili, ali je RandomX izboljšava, moramo najprej razumeti, kakšen je namen rudarjenja. Rudarjenje varuje verigo blokov pred dvojno porabo prek Nakamotovega soglasja. Natančne podrobnosti, kako to počne, presegajo okvir tega članka, vendar jih je mogoče izvedeti iz številnih različnih virov po internetu. Pomembno je, da varnost izhaja iz hešev, ki jih ustvarijo računalniki (rudarji), ki med seboj tekmujejo, da bi našli matematično rešitev, potrebno za ustvarjanje drugega bloka. Pri tem v verigo blokov dodajajo nove transakcije. V zameno za svoje delo (hashe) so nagrajeni z novo skovanimi kovanci.   
  
Pri tej nastavitvi se lahko pojavijo številne težave, ki za pravilno delovanje zahtevajo ustrezne spodbude, vendar se bomo osredotočili na eno posebno težavo, ki se lahko pojavi. Če naj bi bilo rudarjenje tekmovanje, kaj se zgodi, ko en rudar pridobi prednost?

## Ozadje

Za kontekst se pogovorimo o strojni opremi za rudarjenje. Rudarji uporabljajo računalnike za opravljanje dela, vendar vsi vemo, da niso vsi računalniki narejeni enako. Nekateri računalniki so dovolj zmogljivi za izvajanje omrežij AI ali intenzivnih iger, medtem ko se drugi težje spopadajo s preprostimi nalogami. Te razlike v računalniški moči vplivajo tudi na hitrost zgoščevanja ali hitrost, s katero iščejo blokovne rešitve.   
  
Toda tudi te razlike med računalniki zbledijo v primerjavi s stopnjami zgoščevanja specializirane strojne opreme, znane tudi kot specifična integrirana vezja (ASIC), ki presegajo običajne računalnike za več magnitud velikosti.  
  
Vzemimo si nekaj časa, da raziščemo, zakaj so ASIC-ji tako močni. Predstavljajte si, da vsi računalniki padejo nekje na spekter, ki sega od tega, da lahko počnejo veliko stvari, a nič dobro, do tega, da delajo samo eno stvar, a jo delajo zelo dobro. CPU-ji in ASIC-ji so na nasprotnih koncih tega spektra.  
  
CPU, ki so v vseh standardnih računalnikih, so na prvem koncu. Počnejo lahko veliko stvari, na primer brskanje po spletu, igranje iger, vendar nobene od njih ne počnejo posebej dobro. Vendar je ta prilagodljivost na račun učinkovitosti.  
  
ASIC so na drugi strani, kjer zmorejo samo eno stvar, vendar to počnejo z neverjetno hitrostjo. Izvajajo lahko samo eno matematično funkcijo, ker pa lahko zanemarijo vse ostalo, so povečanja zmogljivosti astronomska. Ta učinkovitost pa gre na račun prilagodljivosti, tako da če se funkcija vsaj malo spremeni - primer: x + y = z se spremeni v 2x + y = z -, bo ASIC v celoti prenehal delovati.   
  
Nimajo vsi ASIC, vendar imajo vsi računalnike. To lahko vodi do nepoštene prednosti.

## Zabavna analogija

Če vas to še vedno zmede, vam bo morda v pomoč naslednja analogija. Predstavljajte si loterijo, na kateri se vsako uro podeli tisoč dolarjev, in ta loterija vam omogoča, da si sami natisnete srečke! Na domačem tiskalniku, ki lahko natisne eno srečko na sekundo, začnete tiskati čim več srečk. Ko odštejete stroške elektrike in črnila, ugotovite, da lahko še vedno ustvarite dobiček, tudi če na loteriji zmagate le enkrat na nekaj tednov.  
  
Sčasoma razširite svoje delovanje, dokler nimate celotne sobe, namenjene tiskalnikom. 20 skupaj. Vse je v redu ... do nekega usodnega dne.  
  
Velika novica. Nekdo je izumil novo vrsto tiskalnika. Natisne lahko samo loterijske srečke. Ne more tiskati slik, pisarniških dokumentov ali obojestranskega tiskanja. Samo loterijske srečke. Vendar jih lahko natisne s hitrostjo 1000 srečk na sekundo. Pogledate v svojo majhno tiskarno. 20 tiskalnikov. Potrebujete še 980 tiskalnikov, da lahko sledite enemu od teh pošastnih tiskalnikov, in če ima nekdo dva...?   
  
Na žalost ste zapustili loterijsko igro, saj ne morete več upravičiti stroškov elektrike in črnila.  
  
Toda počakajte! Nekaj tednov pozneje je tu še več novic! Oblika srečke se je spremenila. Številke, ki so bile prej na vrhu, so zdaj na dnu. Novi tiskalniki so tako neprilagodljivi, da tega ne zmorejo. Izdelali so lahko le prejšnjo obliko. Kmalu zatem boste spet veselo tiskali naprej. Vsaj dokler nekdo ne izdela novega tiskalnika za novo obliko.

## RandomX

Kje se RandomX prilega vsemu temu? Prizadeva si izenačiti prednost ASIC tako, da jih je zelo težko izdelati. To naredi tako, da od rudarjev zahteva, da ustvarijo in izvedejo naključno kodo namesto zgoščevanja, ki temelji na algoritmu.  
  
Morda vas bo zmedlo, kako to dejansko pomaga, zato se vrnimo k naši analogiji s tiskalnikom. Se spomnite, kaj se je zgodilo, ko se je spremenila zasnova? Stari pošastni tiskalniki so vsak večer postali zastareli, zato je bilo treba razviti nove z upoštevanjem nove zasnove. Kaj bi se zgodilo, če bi moral vsak nov loterijski listek upoštevati nov oblikovni standard za vsak nov glavni dobitek?   
  
Ustvarjanje novega pošastnega tiskalnika bi bilo izjemno težavno. Ne morete več načrtovati samo enega dizajna srečke. Ker je zasnova naključna, bi morali izdelovalci pošastnih tiskalnikov dodati barvne možnosti, načine tiskanja različnih napisov, robov, oblik in še več. Skratka, naprava, ki bi jo na koncu izumili, bi bila standardni, običajni tiskalnik. Takšen, kot ga imajo vsi drugi.  
  
S preprosto implementacijo te naključnosti v zasnovo srečke smo bistveno zmanjšali veliko prednost, ki jo prinaša specializirana strojna oprema. RandomX počne enako, vendar z rudarjenjem.   
  
Na ta način se zmanjšajo prednosti, ki jih ima peščica izbranih premožnih ljudi, saj bodo, če bodo vlagali v izdelavo "ASIC-ov" za rudarjenje RandomX, dejansko le izumili močnejše in boljše CPU-je, kar bo koristilo vsemu svetu.  
  
To pomeni, da se mali podjetnik s tiskalniki za 20 srečk vrača v igro. Morda bo imel še vedno težje čase, saj lahko ti bogati posamezniki še vedno kupijo več tiskalnikov kot on, vendar zdaj vsaj ni več v večjem razredu samo zaradi enega stroja. Na svoj mali način je konkurenčen.  
  
Ker vemo, da je lahko tudi mali človek konkurenčen pri rudarjenju Monero, spodbujamo vse, da se preizkusijo v denarnici Monero GUI, ki ima podporo za samostojno rudarjenje, ali s prenosom programske opreme, ki jo vzdržuje skupnost. Rudarjenje je preprosto, konkurenčno in odprto za vse.

Nadaljnje branje

  * [Kako Monero edinstveno omogoča krožna gospodarstva](/knowledge/monero-circular-economies)/

  * [Obročni ring podpisi Monero vs CoinJoin kot v Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Zakaj (in kako!) bi morali imeti svoje ključe](/knowledge/hold-your-keys)/

  * [Prispevek nazaj v Monero](/knowledge/contributing-to-monero)/

  * [Kako oddaljena vozlišča vplivajo na zasebnost Monera](/knowledge/remote-nodes-privacy)/

  * [Kako Monero uporablja hard-forke za nadgradnjo omrežja](/knowledge/network-upgrades)/

  * [Ogled oznak: Kako bo en bajt skrajšal čas sinhronizacije Monero denarnice za 40%+](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool in Njegova Vloga pri Decentralizaciji Monero Rudarjenja](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Kaj bo Naredil za Monero](/knowledge/seraphis-for-monero)/

  * [Ali je Pretvorba Bitcoina v Monero Enako Zasebna kot Neposredni Nakup Monera?](/knowledge/most-private-way-to-buy-monero)/

  * [Zakaj Monero Uporablja Nezaupljivo nNastavitev za Razliko od Zcasha](/knowledge/monero-trustless-setup)/

  * [Zakaj je Monero Boljši Hranilnik Vrednosti kot Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Kako lahko Monero premaga omrežne učinke Bitcoina](/knowledge/network-effect)/

  * [Zakaj ima Monero Najbolj Kritično Mislečo Skupnost](/knowledge/critical-thinking)/

  * [Prevare, na Katere Morate Biti Pozorni pri Uporabi Monera](/knowledge/monero-scams)/

  * [Kako Bodo Atomske Menjave v Monero Delovale](/knowledge/monero-atomic-swaps)/

  * [Kaj Mora Vsak Uporabnik Monera Vedeti, ko Gre za Mreženje](/knowledge/monero-networking)/

  * [Kako RingCT Prikrije Zneske Monero Transakcij](/knowledge/monero-ringct)/

  * [Kako Naslovi Monero Stealth Ščitijo Vašo Identiteto](/knowledge/monero-stealth-addresses)/

  * [Kako Monero Podnaslovi Preprečujejo Povezovanje Identitet](/knowledge/monero-subaddresses)/

  * [Pojasnjeni Monero Izhodi (Outputs)](/knowledge/monero-outputs)/

  * [Najboljše Monero Prakse za Začetnike](/knowledge/monero-best-practices)/

  * [Kako Obročni Podpisi Prikrijejo Izhode Monera](/knowledge/ring-signatures)/

  * [Kako je Monero Rešil Problem Velikosti Bloka, ki muči Bitcoin](/knowledge/dynamic-block-size)/

  * [Kako bo CLSAG Izboljšal Učinkovitost Monera](/knowledge/what-is-clsag)/

  * [Zakaj Ima Monero Tail Emisijo](/knowledge/monero-tail-emission)/

  * [Kratka zgodovina Monera](/knowledge/monero-history)/

  * [Wired Magazine se Moti Glede Monera. Evo, Zakaj](/knowledge/wired-article-debunked)/

  * [Razbijamo 15 glavnih mitov in pomislekov o Monero](/knowledge/monero-myths-debunked)/

  * [Kako Dandelion++ Ohranja Zasebnost Izvora Transakcije Monero](/knowledge/monero-dandelion)/

  * [Zakaj je Monero Odprtokoden in Decentraliziran](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Zakaj je Monero Boljši od Dash, Zcash, Zcoin (tudi z Lelantusom), Grin in Bitcoin Mikserji, kot je Wasabi (posodobljeno maja 2020)](/knowledge/why-monero-is-better)/