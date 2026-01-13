---
title: "Ako vzdialené uzly ovplyvňujú súkromie spoločnosti Monero"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Jednou z najväčších výhod, ktoré má Monero v porovnaní s inými kryptomenami, je súkromie v reťazci, ale premýšľali ste niekedy nad tým, ako funguje súkromie Monera, keď používate vzdialený uzol? Čo keby ste použili server „ľahkej peňaženky“ ako MyMonero?

V tomto príspevku sa ponoríme do niektorých detailov toho, ako Monero poskytuje výnimočné súkromie v reťazci aj pri použití vzdialeného uzla, ako aj na čo si dať pozor pri používaní vzdialených uzlov.

## Akú funkciu plnia uzly v Monero?

Pre tých, ktorí menej poznajú, ako Monero funguje, uzly (alebo servery) v sieti Monero môže prevádzkovať ktokoľvek a umožniť vlastníkovi uzla – alebo iným, s ktorými sa rozhodnú ho zdieľať! – synchronizovať kópiu blockchainu a poskytnúť túto kópiu ostatným v sieti. Tieto uzly tiež overujú všetky transakcie prebiehajúce v sieti, ako aj všetky bloky, ktoré sú zverejnené, a zabezpečujú, aby všetky dodržiavali pravidlá stanovené konsenzom.

Ďalšou funkciou, ktorú uzly slúžia v Monero, je spôsob, ako poskytnúť všetky údaje, ktoré vaša obľúbená peňaženka Monero potrebuje na správnu kontrolu transakcií, ktoré patria vám, a na uskutočnenie nových transakcií. Tieto údaje poskytujú uzly dvoma spôsobmi:

  * Údaje z každého bloku na blockchaine sú vyžiadané peňaženkou, naskenované na transakcie patriace vám a po kontrole peňaženkou zahodené. 
    * Tento krok bude čoskoro výrazne vylepšený vďaka [značkám zobrazenia](/knowledge/view-tags-reduce-monero-sync-time).
  * Pri odosielaní transakcií poskytuje uzol, ktorý používate, zoznam možných návnad (alebo falošných vstupov), ktoré sa majú použiť pri vytváraní transakcie, čím zaisťuje, že sa vždy, keď miniete Monero, budete môcť skryť. 
    * Tieto návnady sú súčasťou [prstenových podpisov](/knowledge/ring-signatures), dôležitej časti prístupu spoločnosti Monero k ochrane súkromia na reťazci.

## Aký je najsúkromnejší a najbezpečnejší spôsob používania Monero?

Najlepšia vec, ktorú môžete urobiť, dokonca aj so silným súkromím v reťazci poskytovaným spoločnosťou Monero pri používaní vzdialených uzlov, je spustiť svoj vlastný uzol Monero, aby ste sa uistili, že budete mať po ruke nedotknutú kópiu blockchainu Monero a že vaša IP adresa je dobre chránená. Ďalšou výhodou pri prevádzkovaní vlastného uzla je to, že môžete prispievať späť do siete, nechať ostatné uzly synchronizovať sa z vášho uzla alebo dokonca umožniť iným používateľom pripojiť sa k vášmu uzlu pomocou svojich peňaženiek.

Ako už bolo povedané, Monero stále poskytuje vynikajúce súkromie pri používaní vzdialeného uzla. Ak máte záujem spustiť svoj vlastný uzol Monero, tu je jednoduchý návod, ako to urobiť:

  * [Spustite uzol Monero](https://sethforprivacy.com/guides/run-a-monero-node/)

## Čo sa o mne môže vzdialený uzol dozvedieť?

Pri používaní vzdialeného uzla existuje niekoľko kľúčových informácií, ktoré sa dostanú do kontaktu so vzdialeným uzlom, a niekoľko kľúčových spôsobov, ktorými na vás môže uzol zaútočiť, zabrániť vám v transakcii a ďalšie.

Prvá vec, ktorú sa o vás môže vzdialený uzol dozvedieť, je vaša verejná IP adresa. Aj keď to bude, dúfajme, skryté prostredníctvom VPN alebo Tor, vzdialený uzol by mohol priradiť vašu verejnú IP adresu k transakcii, čo im pomôže zúžiť, odkiaľ transakcie vykonávate. Vzdialený uzol sa tiež môže naučiť posledný blok synchronizovaný s vašou peňaženkou a použiť ho na to, aby sa vás pokúsil kvalifikovane odhadnúť, napríklad kedy normálne používate Monero a kedy ste naposledy minuli Monero. Platí to najmä vtedy, ak vždy prichádzate z rovnakej adresy IP (napríklad z vášho domova). Posledná kľúčová vec, ktorú sa o vás vzdialený uzol môže dozvedieť, sú základné informácie o transakciách, ktoré cez neho posielate. Aj keď to môžu byť najzreteľnejšie údaje, ktoré o vás operátor vzdialeného uzla získa, je dôležité pochopiť, že to môže byť použité na vystopovanie odosielateľa transakcie pri kombinovaní týchto informácií s inými údajmi mimo reťazca. To môže byť obzvlášť nebezpečné, ak vzdialený uzol prevádzkuje zákerná entita, spoločnosť zaoberajúca sa analýzou blockchainu alebo utláčateľský národný štát.

Vzdialený uzol sa vám tiež môže pokúsiť spôsobiť problémy tým, že pred vami skryje bloky, vďaka čomu si vaša peňaženka bude myslieť, že bola synchronizovaná, aj keď to tak nebolo. To môže spôsobiť, že si budete myslieť, že finančné prostriedky sú stratené alebo vám zabráni míňať prostriedky, kým sa nepripojíte k inému uzlu. Posledná kľúčová vec, ktorú môže vzdialený uzol urobiť, je nakŕmiť vašu peňaženku zmanipulovaným zoznamom návnad. To by mohlo spôsobiť, že vaša peňaženka buď úplne zlyhá pri vytváraní transakcií (nemôžete minúť prostriedky), alebo by to mohlo umožniť vzdialenému uzlu, aby sa pokúsil poskytnúť návnady, o ktorých vie, že sú vynaložené na zníženie anonymity, ktorú dostávate pri každej transakcii.

## Aké záruky ochrany súkromia stále existujú pri používaní vzdialeného uzla?

Aj keď vás tento článok možno trochu vystrašil, je dôležité si uvedomiť, že súkromie, ktoré poskytuje Monero, je vynikajúce aj pri použití vzdialeného uzla a ďaleko prevyšuje akúkoľvek inú kryptomenu, keď sa používa týmto spôsobom. Stále získate silné súkromie v reťazci, ktoré poskytuje Monero, pretože vzdialený uzol nikdy nevie skutočný vstup (aké mince míňate), množstvo Monero vynaložené v transakcii alebo adresu príjemcu transakcie. Vonkajší pozorovatelia tiež nemôžu vidieť skutočný vstup, množstvo alebo príslušné adresy (bez ohľadu na to, aký typ uzla sa rozhodnete použiť!), čím sa zabezpečí, že mimo vzdialeného uzla aj vaša IP adresa, informácie o synchronizácii peňaženky a transakcie majú silné záruky ochrany osobných údajov. .

Vzdialený uzol tiež nikdy nemá prístup k predchádzajúcim transakciám, ktoré ste odoslali alebo prijali, ani k sume Monero, ktorá je momentálne vo vašej peňaženke, a stratí prehľad o vašich transakciách v momente, keď začnete používať iný uzol. Vzdialenému uzlu sa nikdy neposkytnú žiadne súkromné kľúče (či už výdavkové alebo prezeracie kľúče), takže vaša peňaženka zostáva súkromná, bezpečná a použiteľná. Bez ohľadu na vzdialený uzol vám tiež nikdy nehrozí, že prídete o Monero alebo vám ho ukradnú, pretože uzol nemôže upraviť adresu príjemcu, nikdy nemá prístup k vašim súkromným kľúčom peňaženky a nemôže vám žiadnym spôsobom skonfiškovať vaše Monero.

## Čo tak „ľahké peňaženky“ ako MyMonero?

Aj keď je téma trochu mimo rámec tohto článku, chcel som sa venovať jedinečnému typu peňaženky v Monero – ľahkým peňaženkám. Názov ľahká peňaženka pochádza zo skutočnosti, že vaša peňaženka (na telefóne alebo počítači) nemusí vykonávať žiadnu synchronizáciu blockchainu, vďaka čomu je zážitok rýchlejší a plynulejší.

Peňaženky, ako je táto, však v súčasnosti prichádzajú s vážnym kompromisom v oblasti ochrany osobných údajov – vaša peňaženka odošle kľúč súkromného zobrazenia na vzdialený server, ktorý používate (ako je predvolený v MyMonero), vďaka čomu má vzdialený server úplný prehľad o všetkých prijatých prostriedkoch od vytvorenia vašej peňaženky (a kým túto peňaženku alebo semienko prestanete používať). To drasticky znižuje súkromie, ktoré dostávate od operátora uzlu, a treba k tomu pristupovať opatrne.

Našťastie komunita Monero pracuje na zlepšení softvéru, ktorý môžete použiť na hosťovanie vlastného servera LWS (Light Wallet Server), čo vám umožní rýchlu synchronizáciu bez toho, aby ste dôverovali tretej strane kľúčom súkromného zobrazenia – spustí softvér, do ktorého vaša peňaženka odosiela kľúče súkromného zobrazenia!

Viac informácií o vlastnom serveri ľahkej peňaženky nájdete v nižšie uvedenom úložisku Github:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Ako sa môžem dozvedieť viac?

Ak ste zvedaví a chceli by ste lepšie pochopiť uzly v Monero a pozrieť sa na používanie vzdialeného uzla alebo spustenie vlastného uzla, pozrite si nižšie uvedené odkazy, kde nájdete skvelé miesta, kde začať:

  * [Monero World, zoznam komunitou prevádzkovaných vzdialených uzlov, ktoré možno použiť](https://moneroworld.com/#nodes)
  * [Monero uzly prevádzkované Seth For Privacy, autor tohto článku](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, zoznam vzdialených uzlov s často kontrolovaným stavom< /a>](https://monero.fail/)
  * [Ako sa pripojiť do vzdialeného uzla v rámci peňaženky GUI](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia – Remote Uzol](https://www.getmonero.org/resources/moneropedia/remote-node.html)

Ďalšie čítanie

  * [Ako Monero jedinečne umožňuje obehové ekonomiky](/knowledge/monero-circular-economies/)

  * [Moneroove prstenové podpisy vs CoinJoin ako vo Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Prečo (a ako!) by ste mali držať svoje vlastné kľúče](/knowledge/hold-your-keys/)

  * [Prispievame späť do Monero](/knowledge/contributing-to-monero/)

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

  * [Ako CLSAG zlepší efektivitu Monero](/knowledge/what-is-clsag/)

  * [Prečo má Monero chvostovú emisiu](/knowledge/monero-tail-emission/)

  * [Stručná história Monera](/knowledge/monero-history/)

  * [Wired Magazine sa o Monere mýli, tu je dôvod](/knowledge/wired-article-debunked/)

  * [Top 15 vyvrátených mýtov a obáv o Monero](/knowledge/monero-myths-debunked/)

  * [Ako Dandelion++ uchováva pôvod transakcií Monero v súkromí](/knowledge/monero-dandelion/)

  * [Prečo je Monero open source a decentralizované](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Čo robí RandomX tak výnimočným](/knowledge/monero-mining-randomx/)

  * [Prečo je Monero lepšie ako Dash, Zcash, Zcoin (dokonca aj s Lelantus), Grin a bitcoinové mixéry ako Wasabi (aktualizované v máji 2020)](/knowledge/why-monero-is-better/)