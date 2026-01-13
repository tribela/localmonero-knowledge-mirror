---
title: "Kako RingCT Prikrije Zneske Monero Transakcij"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Zasebnost Monera ni odvisna od enega samega mehanizma, ki bi, če bi bil pokvarjen, razkril celotno transakcijo, ampak od treh različnih tehnologij, ki delujejo v tandemu in zagotavljajo celovito zasebnost, hkrati pa kompenzirajo slabosti drugih delov. Ta trikraki pristop je sestavljen iz [podpisov zvonjenja](/knowledge/ring-signatures), RingCT in [prikritih naslovov](/knowledge/monero-stealth-addresses). Te tri tehnologije skrijejo dejanski rezultat (pošiljatelja), količino oziroma prejemnika. Danes bomo govorili o RingCT.

RingCT je nedvomno najbolj tehničen od treh in ga je lahko težko razumeti, zato ne bomo natančno opisali, kako deluje, temveč bomo pokazali, kako je mogoče ne poznati zneska in vseeno potrditi stvari o njem . In ne skrbite, kot vedno bomo uporabili veliko primerov.

Najprej raziščimo, zakaj je pomembno preveriti kar koli o zneskih. Zakaj jih preprosto ne moremo ohraniti popolnoma skrivnostne? Odgovor je, da obstajajo pametni načini, s katerimi lahko ljudje ustvarijo denar iz zraka, če imajo priložnost. Kako lahko kaj takega deluje? Poglejmo primer.

Če želite kupiti predmet od prijatelja in on zanj želi deset dolarjev, potem začnete vi z desetimi dolarji, on pa z nič. Ko mu daš deset dolarjev, ima on deset dolarjev, ti pa nič. Začeli ste z desetimi, zdaj jih ima on deset. V tej transakciji ni bil ustvarjen ali uničen noben denar.

S kriptovalutami lahko pameten posameznik da deset dolarjev za predmet in namesto da bi prejel nič dolarjev drobiža, lahko prejme dva dolarja nazaj. Namesto 0 in 10, ki vodita do 10 in 0 (ali 10=10), je zdaj 0 in 10 vodi do 10 in 2 (ali 10=12). Dva Monera sta bila pravkar ustvarjena iz nič. Lahko si predstavljate, da če bi si posameznik večkrat to storil, bi lahko v kratkem času nagrabil velikansko bogastvo.

Z Bitcoinom in drugimi bi bilo to enostavno videti. Ogledate si vhode, ki gredo v transakcije, in izhode, ki izhajajo, ter se prepričate, da je poslano enako prejetemu. Če so bili ti zneski šifrirani in niso vidni, potem uporabnik ne more preveriti, ali je poslano in prejeto isto.

V poskusu povečanja zasebnosti Bitcoina je Gregory Maxwell ustvaril Confidential Transactions (CT), novo tehnologijo, ki bi omogočala šifrirane zneske, hkrati pa dokazala, da v procesu ni bilo nič ustvarjeno ali uničeno. Tako kot pri večini tehnologij za zasebnost tudi ta ni prešla v Bitcoin, vendar jo je Monero želel sprejeti. Bil je samo en problem. Že implementirana tehnologija obročnih podpisov je bila nezdružljiva s predlagano idejo. Tako je eden od takratnih raziskovalcev MRL, Shen Noether, spremenil CT v RingCT, različico CT, ki je bila združljiva s podpisi obročev 

Ponavljam, način delovanja je precej tehničen in bi ga bilo težko razložiti v uvodnem članku. Za ljubitelje kriptografije, ki preprosto morajo vedeti, je na internetu napisanih veliko poglobljenih člankov o notranjem delovanju CT. Za vse nas bo ta članek pokazal, kako bi bilo možno skriti zneske, a vseeno dokazati, da ni bilo nič ustvarjeno ali uničeno.

Recimo, da je Alice želela Bobu poslati denar. Alice bo poslala 10 XMR Bobu, ki bo prejel 10 XMR. 10=10, torej tukaj ni nič narobe. Toda Alice ne želi, da bi kdo vedel, koliko pošilja. Tako z Bobom ustvarita skupno skrivnost. V bistvu številka, ki jo poznata samo onadva. Recimo, da je to število 22. Zdaj Alice pomnoži 10 (kar v resnici pošilja) z 22, da dobi 220. To je število, ki ga deli z omrežjem.

Rudarji sami ne poznajo tajne številke. Če bi to storili, bi lahko število, ki jim je prikazano, delili s skrivno številko in dobili dejanski poslan znesek. Ker pa ne, ne morejo. Vendar vidijo, da bo Bob prejel 220. 220 poslano. 220 prejetih. 220 = 220. Na ta način lahko omrežje preveri, da ni bil ustvarjen ali uničen noben Monero, ne da bi vedeli pravi znesek, ki ga je Alice poslala Bobu.

Ker Bob pozna skupno tajno številko, ko prejme denar, samo deli z 22, da dobi pravi znesek, ki ga je poslala Alice, 10. Alice in Bob ves čas vesta, koliko je bilo poslano in koliko prejeto vsi ostali dobijo lažno številko.

Še enkrat, to ni dejanski način, na katerega CT deluje, vendar daje idejo o tem, kako bi bilo kaj takega mogoče. Pravi način vključuje stvari, kot so Pedersenove obveznosti, dva poslana zneska (en šifriran znesek prejemniku in en znesek obveznosti omrežju) in ... ja, že zlahka je videti, kako se lahko človek izgubi v vsem tem.

Ena stvar, ki jo je treba upoštevati, je, da medtem ko RingCT res skrije znesek transakcije med dvema strankama v transakciji, ne skrije dveh drugih nizov številk.

Prva so transakcije coinbase. Če vam ta izraz ni znan, v bistvu pomeni nagrado, ki jo rudarji prejmejo, ko najdejo naslednji blok. Ta številka ni skrita. Vsak lahko vidi, koliko je protokol nagradil rudarja za njihovo storitev. Na ta način je mogoče ugotoviti trenutno obstoječo količino Monera s seštevanjem vseh transakcij coinbase. Njihova vsota bo enaka trenutnemu Monero v obtoku.

Druga številka, ki ni skrita, je nadomestilo, plačano rudarjem, ko uporabnik pošlje transakcijo. Provizije morajo biti jasne, da lahko rudarji vedo, komu dati prednost. To je način, na katerega lahko uporabniki škodijo svoji zasebnosti, saj če nekdo uporabi edinstveno provizijo za rudarje vsakič, ko pošlje transakcijo (na primer 0,12345), se njegove transakcije lahko povežejo.

Razen teh primerov RingCT od leta 2017 skriva zneske Monero, zato je naša kolektivna zasebnost še toliko močnejša.

Nadaljnje branje