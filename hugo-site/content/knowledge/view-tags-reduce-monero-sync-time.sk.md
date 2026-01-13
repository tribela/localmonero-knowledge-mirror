---
title: "Zobraziť značky: Ako jeden bajt zníži časy synchronizácie peňaženky Monero o 40 % a viac"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Jednou z najčastejších sťažností v súvislosti s každodenným používaním služby Monero je čas, ktorý môže trvať synchronizácia peňaženky, kým bude možné odoslať službu Monero. Našťastie developeri a výskumníci v komunite Monero našli skvelý spôsob, ako skrátiť čas potrebný na synchronizáciu vašej peňaženky o 40 % a viac bez akéhokoľvek dodatočného nafúknutia blockchainu, poplatkov atď.

Zadajte „zobraziť značky“, jednobajtový prídavok k údajom každej transakcie – prichádza do Monera v rámci ďalšej inovácie siete!

## Prečo je synchronizácia peňaženky Monero pomalšia ako synchronizácia bitcoinov?

## Prečo je synchronizácia peňaženky Monero pomalšia ako synchronizácia bitcoinov?

Jednou z prvých otázok, na ktoré musíme odpovedať, aby sme lepšie porozumeli potrebe riešenia, akým sú napríklad značky zobrazenia, je dôvod, prečo je synchronizácia peňaženky Monero pomalšia ako pri kryptomenách, ako je Bitcoin.

V bitcoine, keďže všetky transakcie nie sú súkromné a odhaľujú míňané mince, sumy a adresy zapojené do reťazca, bitcoinové peňaženky môžu jednoducho hľadať akékoľvek nevyčerpané transakčné výstupy (UTXO) alebo použité adresy pre danú peňaženku, rýchlo naskenujte blockchain, aby ste našli iba UTXO vlastnené týmito adresami, aby ste zistili, ktoré mince patria do vašej peňaženky a možno ich minúť.

V Monero však všetky transakcie chránia súkromie používateľa tým, že skryjú odosielateľa, príjemcu a čiastky zahrnuté v každej transakcii. Toto súkromie, hoci je nevyhnutné na ochranu používateľov siete, tiež prináša pomalšiu synchronizáciu peňaženky. V Monero musí vaša peňaženka porovnať každý výstup transakcie (TXO), ktorý existuje v sieti, so súkromnými kľúčmi vašej peňaženky.

Toto porovnanie zahŕňa veľa komplexnej matematiky a kryptografie na overenie, že výstup je skutočne váš, pretože všetky sumy, adresy a známe vynaložené výstupy (alebo mince) sú v Monero skryté v reťazci.

## Čo sú značky zobrazenia?

## Čo sú značky zobrazenia?

Ako pomôcť skrátiť čas synchronizácie pre peňaženky Monero, [developer menom UkoeHB prišiel s novým prístupom](https://github.com/monero-project/research-lab/issues/73) – pridať 1-bajtový „tag“ ku každej transakcii pomocou zdieľaného tajomstva, ktoré je známe iba odosielateľovi a príjemcovi tejto transakcie.

Toto zdieľané tajomstvo generuje odosielateľ pomocou adresy, ktorú mu poskytol príjemca, a nevyžaduje žiadnu aktívnu spoluprácu zo strany odosielateľa a príjemcu. Prvý bajt (alebo znak) tohto zdieľaného tajomstva sa potom pridá k údajom transakcie pri jej zverejnení v sieti Monero.

Keď jeden z účastníkov tejto transakcie chce následne synchronizovať svoju peňaženku s Monero blockchainom, namiesto toho, aby musel vykonávať všetky zložité matematiky a kryptografiu pre každý TXO v sieti, môže teraz peňaženka len skontrolovať to 1-bajtové pole v každej transakcii a až potom vykonajte časovo náročné overenie transakcií, ktoré majú túto značku – presnejšie 1/256 TXO v sieti!

Táto značka neprezrádza žiadne informácie o transakcii vonkajším divákom, iba pridáva 1 bajt (zanedbateľné množstvo) k veľkostiam transakcie, a napriek tomu nám umožňuje skrátiť časy synchronizácie o viac ako 40 % znížením potrebných komplexných overovaní!

## Zobraziť značky: zjednodušený príklad

## Zobraziť značky: zjednodušený príklad

Predstavte si, že máte v miestnosti 4 096 škatúľ, z ktorých iba 5 patrí vám. Všetky krabice sú zvonku úplne na nerozoznanie a jediný spôsob, ako zistiť, či je krabica pre vás, je otvoriť ju a vyriešiť časovo náročný matematický problém zapísaný vo vnútri, aby ste sa uistili, že je vaša.

Teraz si predstavte, že sa rozhodnete, že osoba, ktorá vám pošle týchto 5 políčok, vygeneruje špeciálny kód pomocou vašej adresy a potom umiestnite iba prvý znak tohto vygenerovaného kódu na vonkajšiu stranu každej schránky, ktorú vám pošleme. Všetci ostatní robia to isté so svojimi krabicami (aby sa zabezpečilo, že všetky krabice sú stále nerozoznateľné), ale teraz sa môžete jednoducho pozrieť na kód jedného znaku na vonkajšej strane krabice a otvoriť iba tie krabice, na ktorých je daný znak.

Zatiaľ čo iné boxy budú zodpovedať vášmu kódu, dokonca aj tie, ktoré nevlastníte, počet boxov, ktoré potrebujete na otvorenie a vyriešenie matematického problému, je teraz iba 16 (1/256 boxov!) namiesto všetkých 4 096. 

Teraz otvoríte týchto 16 políčok, vyriešite matematické úlohy a ponecháte si z tejto skupiny 5 políčok, ktoré vám skutočne patria!

## Kedy budú značky zobrazenia dostupné v Monero?

## Kedy budú značky zobrazenia dostupné v Monero?

Značky zobrazenia sú jednou z funkcií, ktoré sa momentálne plánujú zahrnúť do [chystanej inovácie siete](https://github.com/monero-project/meta/issues/630) a mali by byť vydané niekedy na jar. Komunita [ vytvorila 23.3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (v čase písania tohto článku), aby podnietila vývoj a implementáciu značiek zobrazenia, a výsledkom je, že veľká väčšina práce na zahrnutí značiek zobrazenia do základne kódu Monero už bola vykonaná. dokončil j-berman v spolupráci s recenzentmi a developermi.

Po vynútení značiek zobrazenia sieťou budú všetky transakcie odoslané po inovácii siete profitovať z výrazne zlepšeného času synchronizácie peňaženky. Ak chcete začať používať značky zobrazenia, nemusíte robiť nič špeciálne, vaša obľúbená peňaženka pre Monero ich jednoducho začne používať po aktualizácii siete automaticky!

## Ako sa môžem dozvedieť viac?

## Ako sa môžem dozvedieť viac?

Ak to vzbudilo vašu zvedavosť v súvislosti so značkami zobrazenia, pozrite sa nižšie na niekoľko ďalších odkazov, ktoré idú do hĺbky tejto témy:

  * [Znížte časy skenovania pomocou „značky zobrazenia“ 1 bajt na výstup](https://github.com/monero-project/research-lab/issues/73)
  * [Pridajte k výstupom značky zobrazenia, aby ste skrátili čas skenovania peňaženky](https://github.com/monero-project/monero/pull/8061)

Ďalšie čítanie

  * [Ako Monero jedinečne umožňuje obehové ekonomiky](/knowledge/monero-circular-economies)/

  * [Moneroove prstenové podpisy vs CoinJoin ako vo Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Prečo (a ako!) by ste mali držať svoje vlastné kľúče](/knowledge/hold-your-keys)/

  * [Prispievame späť do Monero](/knowledge/contributing-to-monero)/

  * [Ako vzdialené uzly ovplyvňujú súkromie spoločnosti Monero](/knowledge/remote-nodes-privacy)/

  * [Ako Monero používa hard-forky na aktualizáciu siete](/knowledge/network-upgrades)/

  * [P2Pool a jeho úloha pri decentralizácii ťažby Monero](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Čo to urobí pre Monero](/knowledge/seraphis-for-monero)/

  * [Je prevod bitcoinu na monero rovnako súkromný ako priamy nákup monera?](/knowledge/most-private-way-to-buy-monero)/

  * [Prečo Monero používa Trustless Setup na rozdiel od Zcash](/knowledge/monero-trustless-setup)/

  * [Prečo je Monero lepším uchovávateľom hodnoty ako Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Ako môže Monero prekonať sieťové efekty bitcoinu](/knowledge/network-effect)/

  * [Prečo má Monero komunitu najkritickejšieho myslenia](/knowledge/critical-thinking)/

  * [Podvody na ktoré si treba dať pozor pri používaní Monero](/knowledge/monero-scams)/

  * [Ako budú fungovať atómové swapy v Monero](/knowledge/monero-atomic-swaps)/

  * [Čo potrebuje vedieť každý používateľ Monero, pokiaľ ide o vytváranie sietí](/knowledge/monero-networking)/

  * [Ako RingCT skrýva sumy transakcií Monero](/knowledge/monero-ringct)/

  * [Ako Monero Stealth adresy chránia vašu identitu](/knowledge/monero-stealth-addresses)/

  * [Ako podadresy Monero zabraňujú prepojeniu identity](/knowledge/monero-subaddresses)/

  * [Vysvetlenie výstupov Monero](/knowledge/monero-outputs)/

  * [Monero osvedčené postupy pre začiatočníkov](/knowledge/monero-best-practices)/

  * [Ako prstencové podpisy zakrývajú výstupy Monera](/knowledge/ring-signatures)/

  * [Ako Monero vyriešilo problém veľkosti bloku, ktorý trápi Bitcoin](/knowledge/dynamic-block-size)/

  * [Ako CLSAG zlepší efektivitu Monero](/knowledge/what-is-clsag)/

  * [Prečo má Monero chvostovú emisiu](/knowledge/monero-tail-emission)/

  * [Stručná história Monera](/knowledge/monero-history)/

  * [Wired Magazine sa o Monere mýli, tu je dôvod](/knowledge/wired-article-debunked)/

  * [Top 15 vyvrátených mýtov a obáv o Monero](/knowledge/monero-myths-debunked)/

  * [Ako Dandelion++ uchováva pôvod transakcií Monero v súkromí](/knowledge/monero-dandelion)/

  * [Prečo je Monero open source a decentralizované](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: Čo robí RandomX tak výnimočným](/knowledge/monero-mining-randomx)/

  * [Prečo je Monero lepšie ako Dash, Zcash, Zcoin (dokonca aj s Lelantus), Grin a bitcoinové mixéry ako Wasabi (aktualizované v máji 2020)](/knowledge/why-monero-is-better)/

Ďalšie čítanie