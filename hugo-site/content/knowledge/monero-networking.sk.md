---
title: "Čo potrebuje vedieť každý používateľ Monero, pokiaľ ide o vytváranie sietí"
slug: "monero-networking"
date: "2020-11-11"
image: "/images/networking.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Pre nikoho by nemalo byť prekvapením, že Monero a vlastne všetky kryptomeny fungujú na internete. A napriek tomu, aj keď sa toto vyhlásenie zdá byť základné a zrejmé, mnohí neuvažujú o dôsledkoch toho, čo to znamená v súvislosti s ich súkromím. Inými slovami, existuje niekoľko vecí, pred ktorými Monero môže a nemôže chrániť, už len z povahy prevádzky na internete. Niektoré z týchto úvah sú len nepríjemnosti, zatiaľ čo iné sú oveľa závažnejšie v situácii, keď sa vyžaduje absolútne súkromie. Urobme si čas, aby sme sa oboznámili s tým, ako používatelia Monero navzájom komunikujú v sieti a čo to znamená pre ich súkromie.

Počnúc triviálnou stránkou veci, ak používateľ nemá prístup na internet, nemôže sťahovať nové bloky, šíriť transakcie v mene iných ani odosielať svoje transakcie. Zaujímavosťou je, že používateľ s úplným uzlom bez prístupu na internet môže vytvoriť transakciu offline, ktorú možno odoslať neskôr. Je to preto, že prsteňový podpis potrebuje na skrytie iba výstupy z blockchainu. Krátke pripomenutie [ako fungujú kruhové podpisy](/knowledge/ring-signatures), skrýva skutočný výstup, ktorý používateľ posiela, medzi kolekciou nepridružených výstupov vybraných z minulosti. Ak má používateľ prístup k týmto výstupom vo forme úplne stiahnutého blockchainu (úplný uzol), potom môže vytvoriť vyzváňací podpis z minulých výstupov a po obnovení internetového pripojenia preniesť transakciu do siete.

Používateľ, ktorý používa vzdialený uzol, to nemôže urobiť, pretože keď vytvára svoj vyzváňací podpis, kontaktuje vzdialený úplný uzol, aby výstupy zahrnul do vyzváňacieho podpisu. Žiadny internet znamená, že nemôžu dosiahnuť tento uzol, takže nemajú možnosti vytvárania offline transakcií.

Skôr než budeme pokračovať v niektorých úvahách o ochrane osobných údajov, povedzme si krátky úvod o tom, ako funguje internet ako celok. Celý internet nie je nič iné ako počítače, ktoré sa pripájajú k iným počítačom. To je všetko. Blog, ktorý rád čítaš? Len niektoré súbory umiestnené na počítači niekoho iného. Táto webová stránka, na ktorej čítate tento článok (LocalMonero)? Súbory a kód hostené niekde v počítači. Takto fungujú aj veľké bláznivé stránky. Vezmite si napríklad YouTube. Stačí video súbory hostené na gigantických počítačových systémoch Google a vy sa k nim pripojíte, aby ste si stiahli video do svojho počítača, aby ste si ho mohli pozrieť.

Tieto počítače sa môžu navzájom odlíšiť, pretože každý počítač pripojený k internetu má pridelené jedinečné identifikačné číslo nazývané IP adresa. Zvyčajne ide o štyri sady čísel oddelené bodkami, napríklad: 172.66.35.7. Je dôležité mať to na pamäti, keď zvažujeme, ako sa informácie Monero presúvajú po internete. Monero je sieť typu peer-to-peer (P2P), čo znamená, že počítače sa pripájajú priamo k sebe, nie cez sprostredkovateľa. Takže keď úplný uzol používateľa sťahuje novoobjavený blok, nesťahuje ho z centrálneho servera, ale od svojich kolegov. Nevýhodou je, že používatelia sa k sebe pripájajú priamo, poznajú si navzájom svoje IP adresy.

No? O čo ide? Je to len číslo, však? Práve že nie. Samotné IP adresy obsahujú informácie o používateľovi, ako je krajina pôvodu a poskytovateľ siete, ale čo je ešte horšie, poskytovatelia internetových služieb (ISP) poznajú IP adresu každej osoby, ktorá ich služby využíva. To znamená, že títo poskytovatelia internetových služieb a tí, s ktorými spolupracujú, môžu sledovať internetovú prevádzku používateľa a pomocou nejakej šikovnej taktiky zistiť, že používajú Monero. Teraz, než sa zľaknete, všimnite si tam uvedené znenie. Všetko, čo títo snooperi dokážu, je vidieť, že sa osoba pripája k iným uzlom v sieti Monero. Kvôli technológii ochrany osobných údajov spoločnosti Monero o jednotlivcovi neuniká nič iné. Nie, či majú alebo nemajú spustený uzol, alebo či/keď odosielajú transakcie a ak je odoslaná transakcia, nie sú známe žiadne jej informácie. Všetci títo poskytovatelia internetových služieb vidia, že jeden z ich používateľov sa pripája k sieti Monero.

Niektorým ľuďom na niektorých miestach môže stačiť len táto informácia na poškodenie dobrého mena alebo slobody. Alebo možno nie je pre vás prijateľná myšlienka, že by niekto z akéhokoľvek dôvodu narušil vaše súkromie a to, čo robíte na internete. Týmto jednotlivcom sa odporúča, aby sa k sieti Monero pripájali iba pomocou sietí VPN, Tor alebo I2P, čo sú všetky služby, ktoré skrývajú IP adresu používateľa pred ostatnými, ako aj to, čo používateľ robí pred poskytovateľom internetových služieb. Rozdiely medzi týmito službami presahujú rámec tohto článku, ale na túto tému je napísaných veľa kvalitných článkov, takže dotknutým používateľom odporúčame, aby si to preštudovali!

Pre nás ostatných si možno myslíme, že to, že ostatní vedia, že sme pripojení k sieti Monero, nie je až taký problém. Koniec koncov, skutočný obsah našich transakcií, alebo ak vôbec nejaké posielame, je verejnosti skrytý, takže aká je škoda? Aj keď to môže byť pravda, používateľom sa odporúča, aby zvážili skutočnosť, že hlavným lákadlom kryptomien je vlastná banka. Keď držíte svoj súkromný kľúč a ak sa mu niečo stane, nikto vám nemôže pomôcť získať stratené prostriedky.

Byť vlastnou bankou znamená zvážiť nielen vašu digitálnu bezpečnosť, ale aj vašu fyzickú bezpečnosť. Je celkom možné, že znalosť jednotlivca pripájajúceho sa k sieti Monero môže priniesť nechcenú pozornosť, nie nevyhnutne veľkých aktérov, ako sú národné štáty, ale menších subjektov so sebeckým záujmom, ako sú hackeri, ktorí chcú ľahko zarobiť. V celom krypto priestore je skutočne nespočetné množstvo príbehov o takýchto scenároch, ktoré sa skutočne odohrávajú.

Cieľom tohto článku nie je vyvolať strach alebo vystrašiť, ale skôr povzbudiť používateľov, aby si urobili prieskum o tom, aké metódy ochrany pri surfovaní na webe sú pre nich vhodné. Dobrou správou je, že tieto zručnosti sa prenesú aj na všeobecné používanie internetu, nielen na používanie Monero, a preto v našom svete čoraz viac pripojenom na internet sa šikovný používateľ nemôže pokaziť, keď si nazhromaždí správne znalosti a zručnosti, aby zostal v bezpečí a naozaj bol svojou vlastnou bankou.

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