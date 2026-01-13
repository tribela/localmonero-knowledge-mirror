---
title: "Ako CLSAG zlepší efektivitu Monero"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Ako protokol je Monero v súčasnosti v neustálom stave inovácií. Komunita Monero využíva výskum v on-chain aj off-chain riešeniach a hľadá oblasti, ktoré treba zlepšiť, aby sa Monero stalo súkromnejším, škálovateľnejším a prístupnejším pre všetkých. Jednou z najnovších inovácií je nahradenie schémy prepojiteľného kruhového podpisu, MLSAG, náhradou CLSAG, čo znamená Concise Linkable Spontaneous Anonymous Group.

Na povrchovej úrovni, implementácia CLSAG zníži najčastejšie 2 vstupné a 2 výstupné transakcie o 25 %. Zaznamenáme tiež 10 % skrátenie času overenia.

Ale čo presne je CLSAG? Čo robí a ako sa líši od starej verzie, MLSAG? Venujme si chvíľku, aby sme si pripomenuli, prečo a ako prstencové podpisy, aby sme lepšie porozumeli tomuto konceptu. Krúžkové podpisy umožňujú neinteraktívne, svedkom nerozoznateľné vstupy pomocou sád anonymity predchádzajúcich výstupov vybratých podpisovateľom. Laicky povedané, umožňuje používateľovi skryť svoje výstupy použité v transakcii spolu s nesúvisiacimi výstupmi, a to všetko môže urobiť bez toho, aby sa musel zúčastniť niekto iný. Všetko, čo potrebujete, je kópia blockchainu. Každý z týchto výstupov sa väčšinou javí ako rovnako pravdepodobný, že ide o skutočný odosielaný výstup, čím sa skrývajú metadáta o odosielateľovi.

To však spôsobuje trochu problém. Čo ak má používateľ vytvoriť kruhový podpis so všetkými výstupmi návnady? Ako môže niekto vedieť, že neznámy odosielateľ nemá oprávnenie na odoslanie žiadneho z nich? Mohol by tento používateľ minúť falošné peniaze? Odpoveď je nie. Vyzváňací podpis zahŕňa metódu na preukázanie, že aspoň jeden z výstupov vlastní neznámy odosielateľ, bez toho, aby sa odhalilo, ktorý to je. V skutočnosti sú CLSAG aj MLSAG (odteraz známe ako SAG) súčasťou kruhového podpisu, ktorý to dokazuje. Je zaujímavé, že zároveň dokazuje, že suma transakcie, hoci je skrytá za dôvernými transakciami (RingCT), sa vyrovnáva. To, že SAG dokazujú dve veci, že jeden výstup vlastní niekto v ringu a že transakcia je v rovnováhe, je dôležité, a kde vlastne spočívajú úspory veľkosti a overovania. Ak to začína byť mätúce, nebojte sa, čoskoro sa dostaneme k zábavnej a ľahko pochopiteľnej analógii.

Stará schéma podpisu, MLSAG (Multilayered Linkable Spontaneous Anonymous Group) dokazuje vyššie uvedené dve veci v kruhovom podpise, ale robí každú samostatne. Použitie samostatných výpočtov pre podpisové a záväzné kľúče znamená pomalšie operácie. Moderný počítač dokáže tieto výpočty vykonať v priebehu milisekúnd, čo sa nezdá byť veľa a v prípade jednej transakcie to tak nie je. Keď však vezmeme do úvahy množstvo transakcií na blockchaine Monero a to, že uzol, ktorý sa synchronizuje od začiatku, bude musieť stiahnuť a overiť každú z nich, bajty a milisekúndy sa začnú rýchlo hromadiť.

CLSAG spája matematiku potrebnú na dokázanie oboch do jednej, ako aj počíta obe naraz, a to bezpečným spôsobom. Čo to znamená bezpečným spôsobom? Aby sme si to vyjasnili a dúfajme, že celá vec dáva väčší zmysel, poďme preskúmať tú sľubovanú zábavnú analógiu.

Povedzme, že musíte ísť do obchodu s potravinami aj do železiarstva, aby ste si vyzdvihli dve rôzne veci: jedlo a toxické čistiace chemikálie. Nechcete, aby sa zmiešali, ako keby došlo k nehode, chemikálie sa rozlejú na jedlo, čím sa stanú nepožívateľnými. Rozhodnete sa byť super v bezpečí a odveziete sa zo svojho domu do obchodu s potravinami, kúpite si jedlo a potom sa odveziete späť do svojho domu. Až po vyložení jedla sa vrátite do auta, odveziete sa do železiarstva a s chemikáliami späť do svojho domu. Absolvovali ste dve samostatné cesty, aby ste zaistili bezpečnosť všetkých nákupov. Aj keď je to skutočne bezpečné, je to neefektívne. Toto predstavuje MLSAG, kde sú uložené dve rôzne sady matematických údajov a na ich výpočet sa vykonajú dve rôzne „výlety“.

Rozhodnete sa však, že to chcete urobiť rýchlejšie. Je to príliš veľa strateného času. Ak to urobíte raz alebo dvakrát, neukradnete vám život, ale keď to budete musieť robiť znova a znova, hodiny začnú pribúdať. Začnete uvažovať, či si namiesto toho môžete urobiť jeden výlet. Z vášho domu, do obchodu s potravinami, do železiarstva a späť domov. Nemôžete ísť len tak náhodne hodiť všetko do auta. nie je to bezpečné. Namiesto toho určíte rôzne miesta v aute pre rôzne veci a uistíte sa, že všetko úhľadne sedí na svojom mieste. Môžete tak bezpečne podniknúť jednu cestu do oboch obchodov a držať veci ďalej od seba. Toto predstavuje CLSAG. V tejto transakcii je teraz uložená iba jedna sada matematiky, ktorá dokazuje tieto dve veci, a je skončené, že sa navzájom nerušia. Ešte je potrebné urobiť výlet, ale dosť drasticky ste ich znížili.

To všetko znie celkom vzrušujúco. Je možné, že nájdeme iné skratky alebo iné spôsoby, ako ušetriť čas a priestor? Odpoveď je áno aj nie. Podľa súčasných výskumníkov MRL pravdepodobne nie je možné ďalej upravovať konštrukcie typu SAG pre lepšiu veľkosť alebo rýchlosť; avšak iné konštrukcie ako Arcturus, Omniring, RCT3 alebo Triptych prinášajú oveľa lepšie škálovanie veľkosti a výhody overovania pomocou rôznych matematických metód. Každý z týchto prístupov novej generácie k protokolom nejednoznačným pre signatárov však prichádza so svojimi vlastnými kompromismi v implementačných detailoch a prechádza aktívnym výskumom a skúmaním.

Koniec koncov, Monero neustále inovuje.

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

  * [Ako Monero vyriešilo problém veľkosti bloku, ktorý trápi Bitcoin](/knowledge/dynamic-block-size/)

  * [Prečo má Monero chvostovú emisiu](/knowledge/monero-tail-emission/)

  * [Stručná história Monera](/knowledge/monero-history/)

  * [Wired Magazine sa o Monere mýli, tu je dôvod](/knowledge/wired-article-debunked/)

  * [Top 15 vyvrátených mýtov a obáv o Monero](/knowledge/monero-myths-debunked/)

  * [Ako Dandelion++ uchováva pôvod transakcií Monero v súkromí](/knowledge/monero-dandelion/)

  * [Prečo je Monero open source a decentralizované](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Čo robí RandomX tak výnimočným](/knowledge/monero-mining-randomx/)

  * [Prečo je Monero lepšie ako Dash, Zcash, Zcoin (dokonca aj s Lelantus), Grin a bitcoinové mixéry ako Wasabi (aktualizované v máji 2020)](/knowledge/why-monero-is-better/)