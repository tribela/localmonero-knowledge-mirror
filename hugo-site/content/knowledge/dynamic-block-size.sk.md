---
title: "Ako Monero vyriešilo problém veľkosti bloku, ktorý trápi Bitcoin"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Poznámka:** Dôrazne odporúčame, aby si čitateľ prečítal naše články [„Prečo má Monero chvostové emisie“](/knowledge/monero-tail-emission) a [„Ťažba Monero: Čo robí RandomX tak špeciálne“](/knowledge/monero-mining-randomx). Tento článok stavia na konceptoch v ňom uvedených._

Vždy, keď jednotlivci diskutujú o problémoch s blockchainom, jedným z prvých slov, ktoré sa objavia, bude „škálovanie“. Nie je tajomstvom, že blockchainy sa neškálujú dobre, ale väčšina ľudí nevie prečo.

Pravdou je, že škálovanie je v skutočnosti zastrešujúci pojem, ktorý pokrýva dve rôzne kategórie: Podpora protokolu a technologická podpora v danom časovom bode. V tomto článku zameriame svoju pozornosť na to prvé, podporu protokolu, je to v podstate mierou toho, koľko transakcií protokol dokáže v danom čase spracovať.

Bitcoin má limit veľkosti bloku, čo znamená, že akonáhle je v bloku zahrnutý dostatok transakcií, akékoľvek ďalšie transakcie budú musieť čakať v rade na ďalší blok. Užitočnou analógiou by bolo uvažovanie o vlaku. Vlak pristaví na stanicu a tí, čo sú v rade, sa prihlásia. Keď sa vlak naplní, každý, kto zostane vonku, bude musieť čakať na ďalší.

Bitcoin používa poplatky na určenie toho, kto sa dostane do bloku alebo nie. Skočíme späť k analógii s vlakom, možno si predstaviť, že jeden potenciálny cestujúci, ktorý má zostať pozadu, ponúka strojníkovi päť dolárov, aby mu dal miesto. Ostatní pasažieri nasledujú príklad a nakoniec dôjde k boju o to, kto dostane aké miesta. Je na vodičovi, aby sa rozhodol, či chce dodržať zásadu „kto prv príde, ten prv berie“, ale je v jeho najlepšom finančnom záujme maximalizovať svoj príjem tým, že na palubu vezme tých, ktorí ponúknu najvyššiu cenu.

V tejto analógii sú baníci rušňovodiči. Do bloku môžu zahrnúť akékoľvek transakcie, ktoré chcú, ale vo všeobecnosti si vyberú tie, ktoré majú najvyššie platené poplatky.

Alternatívne, ak bloky nie sú príliš plné, ľudia nemajú motiváciu platiť vysoké poplatky, pretože je tam veľa voľných miest na rezervu.

Vo vrchole rozmachu kryptomien v roku 2017 bol bitcoin zaplavený transakciami a poplatky vyleteli pre tých, ktorí chceli byť zaradení do ďalšieho bloku alebo do akéhokoľvek bloku blízkej budúcnosti. Tí, ktorí neboli ochotní platiť vysoké poplatky, videli, že ich transakcie boli posunuté späť o hodiny, dni alebo dokonca úplne vypadli z radu.

Bol to otrasný pohľad na to, ako by sa bitcoinom darilo, ak by sa často hovorilo o „masovej adopcii“. Ak by mal Bitcoin používať masy, veci by boli ešte horšie ako v roku 2017 a Bitcoin by bol nedostupný pre kohokoľvek okrem bohatých, jednoducho preto, že priepustnosť je malá kvôli pevnej veľkosti bloku, čo spôsobí, že trh s poplatkami prevezme kontrolu. .

Monero to predvídal a chcel urobiť niečo iné. Developeri Monero teda implementovali dynamickú veľkosť blokov.

Monero má v podstate aj uzáver veľkosti bloku, ale je to mäkký uzáver. Keď je rad čakajúcich transakcií príliš dlhý, baníci môžu zväčšiť veľkosť blokov. S našou analógiou vlaku si viete predstaviť pridanie ďalších vlakových vozňov, aby sa zmestili ďalší cestujúci. Po vyprázdnení frontu sa bloky zmenšia späť na pôvodnú veľkosť.

Ak sa to zdá ako dobrý nápad, zdá sa rozumné položiť si otázku, prečo je Monero jedinou kryptomenou, ktorá to implementovala. Prečo to nepridať na bitcoiny, aby ste zastavili problémy s priepustnosťou?

Bohužiaľ to nie je možné. Existuje niekoľko dôvodov a my sa ich pokúsime vysvetliť.

Vždy je v najlepšom záujme baníkov mať veľké bloky. S veľkými blokmi sa zmestia do viacerých transakcií a zarobia viac peňazí z poplatkov, ako aj z odmien za bloky. To môže viesť k spamovým útokom, pri ktorých niekto posiela veľa malých transakcií s malými poplatkami, čím nafúkne reťazec. Baník by len zvýšil veľkosť bloku, aby ich zahŕňal všetky, pretože peniaze sú peniaze, bez ohľadu na to, aké malé sú. To by viedlo k trvalo veľkým blokom s malým ekonomickým prínosom. Bitcoin to rieši umelým obmedzením veľkosti bloku, čím sa generuje trh s poplatkami. Spamoví útočníci by museli preplatiť ostatných používateľov na poplatkoch a to už nie je lacné. To však znamená, že bloky sa zaplnia a niektoré transakcie budú čakať, ako je uvedené vyššie.

Ako teda môže mať Monero dynamické veľkosti blokov, ale vyhnúť sa spamovým útokom? Odpoveď je jednoduchá, ale šikovná. Pokuta za odmenu za blok je zavedená, keď je blok väčší ako normálne. Ak chce tažiar zväčšiť veľkosť bloku, odmena, ktorú získa za nájdenie tohto bloku, bude menšia, ako by inak dostal. Veľkosť blokov teda zvýšia len vtedy, keď zaplatené transakčné poplatky používateľov prevážia stratenú časť odmeny za blokovanie. Napríklad, ak by ťažiar stratil 0,5 XMR zvýšením blokovej odmeny a súčet zaplatených transakčných poplatkov by bol 0,4 XMR, potom by došlo k čistej strate 0,1 XMR, ak by zvýšili veľkosť, takže by nerob to. Naopak, ak by sa celkové transakčné poplatky zvýšili na 0,7 XMR, potom by bol čistý zisk 0,2 XMR, aj keď stratia 0,5 XMR z pokuty za blokovú odmenu, takže baník zväčší veľkosť.

Tieto dynamické bloky umožňujú, aby sieť organicky rástla, bez aritifikovaného obmedzovania veľkosti blokov, aby sa vytvoril trh s vynútenými poplatkami, pričom sa stále vyhýbajú útokom spamu. Existuje niekoľko ďalších uhlov, z ktorých sa môžeme na túto myšlienku pozerať, a viac dôvodov, prečo by nebolo možné pridať do Bitcoinu, ale zatiaľ dúfame, že čitateľ chápe, ako Monero obchádza niekoľko problémov v Bitcoine a jeho deriváty a ako plánuje rozšíriť svoju priepustnosť do budúcnosti.

Ďalšie čítanie

  * [Ako Monero jedinečne umožňuje obehové ekonomiky](/knowledge/monero-circular-economies/)

  * [Moneroove prstenové podpisy vs CoinJoin ako vo Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Prečo (a ako!) by ste mali držať svoje vlastné kľúče](/knowledge/hold-your-keys/)

  * [Prispievame späť do Monero](/knowledge/contributing-to-monero/)

  * [Ako vzdialené uzly ovplyvňujú súkromie spoločnosti Monero](/knowledge/remote-nodes-privacy/)

  * [Ako Monero používa hard-forky na aktualizáciu siete](/knowledge/network-upgrades/)

  * [Zobraziť značky: Ako jeden bajt zníži časy synchronizácie peňaženky Monero o 40 % a viac](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool a jeho úloha pri decentralizácii ťažby Monero](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Čo to urobí pre Monero](/knowledge/seraphis-for-monero/)

  * [Je prevod bitcoinu na monero rovnako súkromný ako priamy nákup monera?](/knowledge/most-private-way-to-buy-monero/)

  * [Prečo Monero používa Trustless Setup na rozdiel od Zcash](/knowledge/monero-trustless-setup/)

  * [Prečo je Monero lepším uchovávateľom hodnoty ako Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Ako môže Monero prekonať sieťové efekty bitcoinu](/knowledge/network-effect/)

  * [Prečo má Monero komunitu najkritickejšieho myslenia](/knowledge/critical-thinking/)

  * [Podvody na ktoré si treba dať pozor pri používaní Monero](/knowledge/monero-scams/)

  * [Ako budú fungovať atómové swapy v Monero](/knowledge/monero-atomic-swaps/)

  * [Čo potrebuje vedieť každý používateľ Monero, pokiaľ ide o vytváranie sietí](/knowledge/monero-networking/)

  * [Ako RingCT skrýva sumy transakcií Monero](/knowledge/monero-ringct/)

  * [Ako Monero Stealth adresy chránia vašu identitu](/knowledge/monero-stealth-addresses/)

  * [Ako podadresy Monero zabraňujú prepojeniu identity](/knowledge/monero-subaddresses/)

  * [Vysvetlenie výstupov Monero](/knowledge/monero-outputs/)

  * [Monero osvedčené postupy pre začiatočníkov](/knowledge/monero-best-practices/)

  * [Ako prstencové podpisy zakrývajú výstupy Monera](/knowledge/ring-signatures/)

  * [Ako CLSAG zlepší efektivitu Monero](/knowledge/what-is-clsag/)

  * [Prečo má Monero chvostovú emisiu](/knowledge/monero-tail-emission/)

  * [Stručná história Monera](/knowledge/monero-history/)

  * [Wired Magazine sa o Monere mýli, tu je dôvod](/knowledge/wired-article-debunked/)

  * [Top 15 vyvrátených mýtov a obáv o Monero](/knowledge/monero-myths-debunked/)

  * [Ako Dandelion++ uchováva pôvod transakcií Monero v súkromí](/knowledge/monero-dandelion/)

  * [Prečo je Monero open source a decentralizované](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Čo robí RandomX tak výnimočným](/knowledge/monero-mining-randomx/)

  * [Prečo je Monero lepšie ako Dash, Zcash, Zcoin (dokonca aj s Lelantus), Grin a bitcoinové mixéry ako Wasabi (aktualizované v máji 2020)](/knowledge/why-monero-is-better/)