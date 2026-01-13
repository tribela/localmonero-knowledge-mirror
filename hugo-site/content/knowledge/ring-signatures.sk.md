---
title: "Ako prstencové podpisy zakrývajú výstupy Monera"
slug: "ring-signatures"
date: "2020-09-08"
image: "/images/rings.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero je široko-ďaleko známy v krypto priestore ako kráľ mincí na ochranu súkromia. Hoci každý vie, že Monero ponúka dobré súkromie, nie tak veľa ľudí rozumie tomu, ako ochrana osobných údajov funguje.

Mnoho ďalších mincí na ochranu osobných údajov zverejňuje infografiku porovnávacej tabuľky, v ktorej sú uvedené názvy technológie ochrany osobných údajov jednotlivých mincí a vo väčšine prípadov označujú technológiu spoločnosti Monero ako RingCT, ale je to len čiastočne pravda. Monero má v skutočnosti trojaký prístup k súkromiu. Jedna technológia na skrytie príjemcu transakcie, jedna na skrytie odoslanej sumy a jedna na skrytie použitého výstupu, to sú stealth adresy, RingCT a podpisy zvonenia.

Tento trojrozmerný prístup znamená, že ak sa jedna z technológií pokazí, ostatné nemusia nevyhnutne zdieľať rovnaký osud. Krúžkové podpisy sú najslabším článkom v schéme ochrany osobných údajov; slovo slabý tu znamená najviac náchylný na heuristické útoky. Nájdime si čas na ich preskúmanie.

Ako je uvedené vyššie, cieľom kruhových podpisov je zakryť výstup použitý v transakcii. Ak je pre vás terminológia „vstup/výstup“ kryptomeny mätúca, nebojte sa. V skutočnosti to nie je také zložité. Keď počujete „výstup“, myslite na kontrolu. Jedna z vecí, ktorá už nie je taká bežná, s ktorou ľudia platia. Rovnako ako šek môže byť označený v akejkoľvek sume - 10 USD, 32,50 USD atď. - a vymieňa si ho medzi stranami transakcie. V prípade kryptomien slúžia výstupy týmto funkciám.

Keď vám niekto zaplatí 10 Monero, dostanete výstup 10 XMR. Tento výstup má hodnotu (10) a je to to, čo sa vyberie z peňaženky odosielateľa, rovnako ako keď platíte za službu, účet opustí vašu fyzickú peňaženku a dostane ho osoba, od ktorej nakupujete.

Spôsob, akým je výstup skrytý, je vytvorenie kruhu (odtiaľ názov) výstupov návnady. Tieto návnady však nie sú „falošnými“ výstupmi. Sú to skutočné minulé výstupy z blockchainu, ktoré nemajú nič spoločné so súčasnou transakciou, ale pre vonkajšieho pozorovateľa môže každý z týchto výstupov vyzerať rovnako pravdepodobne ako ten skutočný. Veľkosť sady výstupov návnady plus skutočný sa nazýva ringsize a momentálne je Monerov jedenásty. Existuje teda desať výstupov návnady a jeden skutočný.

Prečo to číslo jednoducho nezvýšime na 100 alebo dokonca 1 000? Čím viac, tým lepšie, nie? Z hľadiska súkromia áno, ale treba zvážiť aj iné veci. Vráťme sa k fyzickému príkladu, aby sme videli, čo tým myslím. Ak by ste chceli skryť jednu zo svojich dolárových bankoviek medzi desiatimi návnadami, museli by ste mať v peňaženke približne jedenásť dolárov za každý dolár, ktorý ste chceli minúť. Jeden skutočný dolár a desať falošných. To už je dosť ťažkopádne, ak chcete minúť čo i len pár dolárov. Teraz si predstavte, že sme zvýšili návnadu na 1 000. Na každý jeden dolár, ktorý ste chceli minúť, by ste museli nosiť okolo 1 001 dolárov. Na to, aby ste si kúpili jednu sladkosť, by ste museli nosiť kufrík! Je dôležité si uvedomiť, že prsteňové podpisy nefungujú celkom týmto spôsobom, napríklad samotné návnady nie sú súčasťou podpisu, iba odkazmi na ne, ale dúfame, že táto analógia môže byť trochu nápomocná pri predstavení základných pojmov.< /p>

Návnady na blockchaine fungujú podobne. Každá pridaná návnada zvyšuje čas a náklady na overenie transakcie. Každý uzol musí stiahnuť celý kruhový podpis pre každú transakciu a každý kruhový podpis obsahuje skutočný výstup, ako aj návnady. Nielen to, ale musí matematicky overiť, že aspoň jeden z týchto výstupov je skutočný, a čas matematického overenia sa tiež zvyšuje s každou návnadou. To znamená, že musíme nájsť šťastnú strednú cestu, kde je veľkosť prstenca dostatočne veľká na to, aby primerane zakryla skutočný výstup, dokonca aj proti mnohým heuristickým útokom, ale dostatočne malá na to, aby nespôsobila nárast blockchainu masívnym tempom. Nestačí vybrať ľubovoľné číslo alebo len zväčšiť veľkosť prsteňa, keď zmenšíme podpis (napríklad pri CLSAG). Komunita Monero chce konkrétne, matematické dôkazy o tom, ktorá veľkosť prstenca ponúka najlepšie kompromisy. Číslo je príliš malé a súkromie nebude dostatočne silné proti heuristickým útokom. Príliš veľké a možno máme len okrajové výhody na strane ochrany osobných údajov a zbytočne trpíme, pokiaľ ide o škálovanie.

Je potrebné spomenúť ešte jednu vec. Niektorá literatúra Monero zjednodušuje a hovorí, že prstencové podpisy skrývajú odosielateľa, ale to nie je úplne pravda a rozdiel nie je len pedantský. Rozdiel medzi odosielateľom (človek) a výstupom (účtom) je veľký, pokiaľ ide o ochranu súkromia. Zatiaľ čo výstup môže mať väzby na odosielateľa, samotný výstup sa nerovná odosielateľovi. Takže aj keby bol vyzváňací podpis porušený, nemusí sa nevyhnutne spájať s identitou osoby a suma aj príjemca sú stále skryté, čím sa minimalizuje poškodenie súkromia všetkých strán.

To neznamená, že zlomený prsteňový podpis je bezvýznamný. Akékoľvek uniknuté metadáta sú zlé a majú potenciál odhaliť viac informácií, než si myslíme, najmä ak sa použijú v spojení s inými metaúdajmi. Snažíme sa teda zabezpečiť, aby zvolená veľkosť prsteňa zodpovedala za rozhodovanie akademickej prísnosti, aby sa minimalizoval únik iných metadát a používateľ mal predvolené nastavenia na najlepšie možné akcie.

Ak vás však pravdepodobnosť pokazenia podpisu stále znepokojuje, na obzore sú neuveriteľné správy. Ďalšia generácia protokolov ochrany osobných údajov, na ktorých sa pracuje, ako napríklad Triptych, Arcturus a Lelantus, má skutočne elegantné možnosti. V týchto protokoloch sa veľkosť škáluje logaritmicky, nie lineárne, keď sa veľkosť prstenca zvyšuje. To znamená, že sa do nás zmestí 100 návnad, ale použitý priestor je v starej technológii bližšie k veľkosti 10. To je podstatný rozdiel a výrazne to zlepší súkromie všade okolo.

V hre na mačku a myš, ktorou je súkromie, spoločnosť Monero neustále inovuje, aby si udržala náskok a zabezpečila to najlepšie praktické súkromie pre všetkých.

Návnady na blockchaine fungujú podobne. Každá pridaná návnada zvyšuje čas a náklady na overenie transakcie. Každý uzol musí stiahnuť celý kruhový podpis pre každú transakciu a každý kruhový podpis obsahuje skutočný výstup, ako aj návnady. Nielen to, ale musí matematicky overiť, že aspoň jeden z týchto výstupov je skutočný, a čas matematického overenia sa tiež zvyšuje s každou návnadou. To znamená, že musíme nájsť šťastnú strednú cestu, kde je veľkosť prstenca dostatočne veľká na to, aby primerane zakryla skutočný výstup, dokonca aj proti mnohým heuristickým útokom, ale dostatočne malá na to, aby nespôsobila nárast blockchainu masívnym tempom. Nestačí vybrať ľubovoľné číslo alebo len zväčšiť veľkosť prsteňa, keď zmenšíme podpis (napríklad pri CLSAG). Komunita Monero chce konkrétne, matematické dôkazy o tom, ktorá veľkosť prstenca ponúka najlepšie kompromisy. Číslo je príliš malé a súkromie nebude dostatočne silné proti heuristickým útokom. Príliš veľké a možno máme len okrajové výhody na strane ochrany osobných údajov a zbytočne trpíme, pokiaľ ide o škálovanie.

Je potrebné spomenúť ešte jednu vec. Niektorá literatúra Monero zjednodušuje a hovorí, že prstencové podpisy skrývajú odosielateľa, ale to nie je úplne pravda a rozdiel nie je len pedantský. Rozdiel medzi odosielateľom (človek) a výstupom (účtom) je veľký, pokiaľ ide o ochranu súkromia. Zatiaľ čo výstup môže mať väzby na odosielateľa, samotný výstup sa nerovná odosielateľovi. Takže aj keby bol vyzváňací podpis porušený, nemusí sa nevyhnutne spájať s identitou osoby a suma aj príjemca sú stále skryté, čím sa minimalizuje poškodenie súkromia všetkých strán.

To neznamená, že zlomený prsteňový podpis je bezvýznamný. Akékoľvek uniknuté metadáta sú zlé a majú potenciál odhaliť viac informácií, než si myslíme, najmä ak sa použijú v spojení s inými metaúdajmi. Snažíme sa teda zabezpečiť, aby zvolená veľkosť prsteňa zodpovedala za rozhodovanie akademickej prísnosti, aby sa minimalizoval únik iných metadát a používateľ mal predvolené nastavenia na najlepšie možné akcie.

Ak vás však pravdepodobnosť pokazenia podpisu stále znepokojuje, na obzore sú neuveriteľné správy. Ďalšia generácia protokolov ochrany osobných údajov, na ktorých sa pracuje, ako napríklad Triptych, Arcturus a Lelantus, má skutočne elegantné možnosti. V týchto protokoloch sa veľkosť škáluje logaritmicky, nie lineárne, keď sa veľkosť prstenca zvyšuje. To znamená, že sa do nás zmestí 100 návnad, ale použitý priestor je v starej technológii bližšie k veľkosti 10. To je podstatný rozdiel a výrazne to zlepší súkromie všade okolo.

V hre na mačku a myš, ktorou je súkromie, spoločnosť Monero neustále inovuje, aby si udržala náskok a zabezpečila to najlepšie praktické súkromie pre všetkých.

Ďalšie čítanie

  * [Ako Monero jedinečne umožňuje obehové ekonomiky](/knowledge/monero-circular-economies)/

  * [Moneroove prstenové podpisy vs CoinJoin ako vo Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Prečo (a ako!) by ste mali držať svoje vlastné kľúče](/knowledge/hold-your-keys)/

  * [Prispievame späť do Monero](/knowledge/contributing-to-monero)/

  * [Ako vzdialené uzly ovplyvňujú súkromie spoločnosti Monero](/knowledge/remote-nodes-privacy)/

  * [Ako Monero používa hard-forky na aktualizáciu siete](/knowledge/network-upgrades)/

  * [Zobraziť značky: Ako jeden bajt zníži časy synchronizácie peňaženky Monero o 40 % a viac](/knowledge/view-tags-reduce-monero-sync-time)/

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