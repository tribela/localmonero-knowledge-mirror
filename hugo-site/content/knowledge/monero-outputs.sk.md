---
title: "Vysvetlenie výstupov Monero"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero, podobne ako iné kryptomeny, používa výstupy ako prostriedok účtovania finančných prostriedkov. Mnoho používateľov znalých kryptomien tento termín už pravdepodobne počulo, no nie každý rozumie tomu, čo znamenajú a ako fungujú. Ako sme skúmali v našom [článku o kruhových podpisoch](/knowledge/ring-signatures), výstupy sú skutočnou jednotkou vymieňanou na blockchaine medzi zúčastnenými stranami. Podobné ako dolárová bankovka, ale suma nie je v pevnej nominálnej hodnote.

Ak dostanete za prácu zaplatené 16 dolárov, môžete dostať jednodolárovú, päťdolárovú a desaťdolárovú bankovku. Máte 16 dolárov, no v peňaženke máte aj tri rôzne bankovky. Ak ste chceli niekomu zaplatiť 6 dolárov, mohli by ste použiť 5 a 1 účet, ale ak ste chceli niekomu zaplatiť 8 dolárov, mohli ste použiť iba 10 dolárov a dostať späť 2 doláre. Nakoniec, ak by ste chceli niekomu zaplatiť 14 dolárov, museli by ste použiť všetky tri bankovky a dostali by ste 2 doláre späť v drobných, ale na chvíľu, keď odovzdáte všetky tri bankovky, nebudete mať v peňaženke žiadne peniaze, kým nedostanete zmeniť späť.

Monero funguje podobne. Predpokladajme, že prevádzkujete obchod a uskutočňujete tri predaje troch rôznych položiek. Môžete získať 1,5 XMR, 2,25 XMR a 5,25 XMR za celkovo 9 XMR, ale vo svojej peňaženke máte aj tri rôzne výstupy s nominálnymi hodnotami uvedenými vyššie. Rovnako ako v prípade dolárov, možno budete chcieť niekomu zaplatiť 3 XMR. Môžete použiť len výstup 5,25 XMR a získať späť 2,25 XMR v zmene, alebo môžete skombinovať výstupy 1,5 a 2,25 XMR a získať späť 0,75 XMR v zmene.

Akonáhle však odošlete transakciu, výstupy, ktoré používate, sa uvedú do „uzamknutého“ stavu, čo znamená, že sú nedostupné, kým nedostanete späť zmenu. Protokol odblokuje prostriedky (t. j. vráti vám zmenu) po 10 potvrdeniach alebo približne 20 minútach. Rovnako ako po odovzdaní dolárových bankoviek z peňaženky nemôžete peniaze znova použiť, kým nedostanete drobné späť od pokladníka, vaše Monero je nedostupné, kým nedostanete späť drobné.

Vráťme sa k príkladu odoslania 3 XMR niekomu a vy použijete výstup 5,25 XMR. Teraz, keď čakáte, že dostanete späť 1,75 XMR, nemôžete ich použiť. Tento 1,75 XMR je pre vás neprístupný. Stále však môžete použiť výstupy 1,5 XMR a 2,25 XMR, pretože tieto neboli vyčerpané. Vráťme sa k príkladu s dolármi, ak ste niekomu zaplatili 8 USD, ako v predchádzajúcom príklade, nemohli by ste použiť 2 doláre, ktoré očakávate späť, kým vám ich nebudú poskytnuté, ale v tomto príklade stále máte 10 dolárovú bankovku, ktorá je nepoužitá vo vašej peňaženke. Počas čakania na zmenu sa dá stále nakupovať, čo chcete. To isté s Monero.

Toto je často bod zmätku pre nových používateľov Monero. Používateľ môže mať často vo svojej peňaženke iba jeden výstup, ktorý dostal z burzy alebo od priateľa. Povedzme, že tento výstup je 20 XMR. Iné výstupy v peňaženke nemajú. Teraz chcú prispieť dvom svojim obľúbeným charitatívnym organizáciám. Pošlú 5 XMR prvej charitatívnej organizácii a potom sú zmätení, pretože aj keď by im malo zostať 15 XMR, nemôžu okamžite poslať ďalší dar druhej charite. Ako ste možno uhádli, je to preto, že 15 XMR je uzamknutý. Nemôže sa minúť, kým sa nevráti ako drobné (10 potvrdení alebo približne 20 minút). Po odomknutí ich prostriedkov budú môcť poslať svoj druhý dar.

Len na zopakovanie, tento problém by nemali, ak by namiesto toho mali viacero výstupov, ako napríklad dva 10 XMR výstupy alebo podobne. Oba dary by mohli posielať jeden po druhom, pretože pri prvom odbere by sa použil jeden z 10 výstupov XMR (a čakalo by sa 10 potvrdení, aby sa im vrátilo 5 XMR v drobných), a pri druhom odbere by sa použilo ďalších 10 XM ako výstup.

Niektoré kryptomenové peňaženky majú funkciu nazvanú „správa výstupov“, ktorá jednoducho ukazuje používateľovi, ktoré výstupy momentálne má (okrem ich celkového súčtu), a zároveň im umožňuje vybrať si, ktoré z nich chce použiť, keď sa utráca ich kryptomena.

Odteraz GUI Monero vykonáva výber výstupov pre používateľov automaticky, pretože používatelia, ktorí si vyberajú svoje vlastné výstupy, často vedú k zmätku alebo v niektorých prípadoch k narušeniu súkromia. Vo výstavbe sú však peňaženky, ako napríklad nový projekt peňaženky Feather, ktorý bude obsahovať tieto funkcie správy výstupov.

Veľa sme hovorili o odosielacej časti, ale na prijímacej strane sa stane niečo fascinujúce. Vráťme sa k nášmu príkladu odoslania 3 XMR niekomu a použitím vašich výstupov 1,5 XMR a 2,25 XMR v transakcii (pri očakávaní zmeny 0,75 XMR), prijímač NEPRÍJEM dva výstupy 1,5 XMR a 2,25 XMR. Namiesto toho dostanú JEDEN 3 výstup XMR.

Protokol na pozadí kombinuje všetky výstupy používané na míňanie a dáva príjemcovi jeden výstup zaplatenej sumy a odosiela jeden výstup zmeny späť odosielateľovi. Odosielateľ teda tiež dostane jeden výstup späť ako zmenu bez ohľadu na to, či na odoslanie transakcie použil dva, tri alebo desať výstupov.

Dúfame, že to vyjasnilo nejaké nejasnosti týkajúce sa výstupov a fungovania interného účtovania protokolu, ako aj bežného používateľa, ktorý čelí problému zmätku, keď narazí na uzamknuté prostriedky. V inom článku preskúmame správu vašich výstupov, aby sme minimalizovali možnosť, že budete musieť čakať na odomknuté prostriedky pred odoslaním budúcich transakcií.

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

  * [Monero osvedčené postupy pre začiatočníkov](/knowledge/monero-best-practices/)

  * [Ako prstencové podpisy zakrývajú výstupy Monera](/knowledge/ring-signatures/)

  * [Ako Monero vyriešilo problém veľkosti bloku, ktorý trápi Bitcoin](/knowledge/dynamic-block-size/)

  * [Ako CLSAG zlepší efektivitu Monero](/knowledge/what-is-clsag/)

  * [Prečo má Monero chvostovú emisiu](/knowledge/monero-tail-emission/)

  * [Stručná história Monera](/knowledge/monero-history/)

  * [Wired Magazine sa o Monere mýli, tu je dôvod](/knowledge/wired-article-debunked/)

  * [Top 15 vyvrátených mýtov a obáv o Monero](/knowledge/monero-myths-debunked/)

  * [Ako Dandelion++ uchováva pôvod transakcií Monero v súkromí](/knowledge/monero-dandelion/)

  * [Prečo je Monero open source a decentralizované](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Čo robí RandomX tak výnimočným](/knowledge/monero-mining-randomx/)

  * [Prečo je Monero lepšie ako Dash, Zcash, Zcoin (dokonca aj s Lelantus), Grin a bitcoinové mixéry ako Wasabi (aktualizované v máji 2020)](/knowledge/why-monero-is-better/)