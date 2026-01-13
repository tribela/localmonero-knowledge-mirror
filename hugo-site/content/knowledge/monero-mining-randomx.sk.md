---
title: "Monero Mining: Čo robí RandomX tak výnimočným"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
30\. novembra 2019 malo Monero svoj polročný hard fork, pričom najočakávanejšou zmenou bol prechod zo starého algoritmu PoW, cryptonight, na úplne nový, interne vyvinutý, RandomX. Komunita Monero verí, že RandomX je veľkým krokom smerom k rovnostárskej ťažbe, ale poďme hlbšie zistiť, či je to tak.

## Účel

Aby sme mohli posúdiť, či je RandomX vylepšením, musíme najprv pochopiť, aký je účel ťažby. Ťažba zabezpečuje blockchain z dvojitých výdavkov prostredníctvom konsenzu Nakamoto. Presné zložitosti, ako to robí, presahujú rámec tohto článku, ale možno ich zistiť z mnohých rôznych zdrojov na internete. Dôležité je, že bezpečnosť pochádza z hashov generovaných počítačmi (baníkmi), ktoré si navzájom konkurujú pri hľadaní matematického riešenia potrebného na vytvorenie ďalšieho bloku. Ako to robia, pridávajú do blockchainu nové transakcie. Na oplátku za svoju prácu (haše) sú odmeňovaní novo vyrazenými mincami.   
  
S týmto nastavením sa môže vyskytnúť množstvo problémov, ktoré si vyžadujú správne stimuly, aby fungovali správne, ale zameriame sa na jeden konkrétny problém, ktorý môže nastať. Ak má byť ťažba súťažou, čo sa stane, keď jeden baník získa výhodu?

## Pozadie

Pre kontext si povedzme niečo o ťažobnom hardvéri. Baníci používajú na prácu počítače, ale všetci vieme, že nie každý počítač je vyrobený rovnako. Niektoré počítače sú dostatočne výkonné na spustenie sietí AI alebo náročných hier, zatiaľ čo iné bojujú aj s jednoduchými úlohami. Tieto rozdiely vo výpočtovom výkone ovplyvňujú aj hash rate, čiže rýchlosť, akou hľadajú blokové riešenia.   
  
Ale aj tieto rozdiely medzi počítačmi blednú v porovnaní s mierou hash špecializovaného hardvéru, inak známeho ako Application Specific Integrated Circuits (ASIC), ktorý predstihuje bežné počítače o niekoľko rádov.  
  
Venujme nejaký čas preskúmaniu toho, prečo sú ASIC také výkonné. Predstavte si, že všetky počítače spadajú niekde do spektra, ktoré siaha od schopnosti robiť veľa vecí, ale nič dobre, až po robiť len jednu vec, ale robiť to veľmi dobre. CPU a ASIC sú na opačných koncoch tohto spektra.  
  
CPU, ktoré sú vo všetkých štandardných počítačoch, sú na prvom konci. Môžu robiť veľa vecí, napríklad prehliadať web, hrať hry alebo vykresľovať video, no žiadnu z nich nerobia obzvlášť dobre. Táto flexibilita však prichádza na úkor efektívnosti.  
  
ASIC sú na druhom konci, kde môžu len jednu vec, ale robia to neuveriteľnou rýchlosťou. Môžu vykonávať iba jednu matematickú funkciu, ale pretože môžu ignorovať všetko ostatné, zisky z výkonu sú astronomické. Táto efektívnosť však prichádza na úkor flexibility, takže ak sa funkcia čo i len mierne zmení – príkladom je x + y = z sa zmení na 2x + y = z – potom ASIC prestane fungovať úplne.   
  
Nie každý vlastní ASIC, ale každý má počítače. To môže viesť k nespravodlivej výhode.

## Zábavná analógia

Ak je to stále mätúce, možno pomôže nasledujúce prirovnanie. Predstavte si lotériu, kde sa každú hodinu udeľuje tisíc dolárov a táto lotéria vám umožňuje vytlačiť si vlastné tikety! Začnete tlačiť čo najviac lístkov na svojej domácej tlačiarni, ktorá dokáže vytlačiť jeden lístok za sekundu. Po odpočítaní nákladov na elektrinu a atrament vidíte, že stále môžete dosiahnuť zisk, aj keď vyhráte v lotérii iba raz za niekoľko týždňov.  
  
Postupom času rozširujete svoju prevádzku, až kým nebudete mať celú miestnosť vyhradenú pre tlačiarne. Spolu 20 tlačiarní. Všetko je v poriadku...až do jedného osudného dňa.  
  
Sú tu veľké novinky. Niekto vynašiel nový druh tlačiarne. Môže tlačiť iba žrebové lístky. Nemôže tlačiť obrázky alebo kancelárske dokumenty ani vykonávať obojstrannú tlač. Iba losy. Dokáže ich však vytlačiť rýchlosťou 1000 lístkov za sekundu. Pozrieš sa do svojej malej miestnosti s tlačiarňou. 20 tlačiarní. Potrebujete ďalších 980 tlačiarní, aby ste udržali krok s JEDNOU z týchto príšerných tlačiarní, a ak má niekto dve...?  
  
Smutne opúšťate lotériovú hru, pretože už nemôžete ospravedlniť náklady na elektrinu a atrament.  
  
Ale počkaj! O pár týždňov neskôr sú tu ďalšie novinky! Dizajn lístka sa zmenil. Čísla, ktoré boli predtým hore sú teraz dole. Nové tlačiarne monster sú také neflexibilné, že to nedokážu. Mohli urobiť iba predchádzajúci dizajn. Netrvá dlho a budete opäť veselo tlačiť. Aspoň kým niekto nevyrobí novú tlačiareň monštier pre nový dizajn.

## RandomX (NáhodnéX)

Kde do toho všetkého zapadá RandomX? Snaží sa vyrovnať výhodu ASIC tým, že veľmi sťažuje výrobu ASIC. Robí to tak, že od baníkov vyžaduje, aby vytvorili a spustili náhodný kód namiesto hašovania založeného na algoritme.  
  
Môže byť mätúce, ako to v skutočnosti niečomu pomáha, takže sa vráťme k našej analógii s tlačiarňou. Pamätáte si, čo sa stalo, keď sa zmenil dizajn? Staré tlačiarne príšer každú noc zastarávajú a nové bolo potrebné vyvinúť s ohľadom na nový dizajn. Čo by sa stalo, keby každý nový výherný tiket do lotérie musel spĺňať nový štandard dizajnu pre každý nový jackpot?   
  
Vytvorenie novej tlačiarne monštier by bolo neuveriteľne ťažké. Už nemôžete plánovať len jeden návrh lístka. Keďže dizajn je náhodný, výrobcovia príšerných tlačiarní by museli pridať možnosti farieb, spôsoby tlače rôznych nápisov, okrajov a tvarov a ďalšie. Stručne povedané, stroj, ktorý nakoniec vynašli, by bol štandardnou, bežnou tlačiarňou. Rovnako ako všetci ostatní.  
  
Jednoduchou implementáciou tejto náhodnosti do návrhu lístka sme podstatne znížili veľkú výhodu získanú zo špecializovaného hardvéru. RandomX robí to isté, ale s ťažbou.  
  
Týmto spôsobom sú výhody získané niekoľkými vybranými bohatými ľuďmi minimalizované, pretože ak investujú do vytvárania „ASIC“ na ťažbu RandomX, v skutočnosti len vymyslia silnejšie a lepšie CPU, z čoho má úžitok celý svet.  
  
To znamená, že malý chlapík so svojimi 20 tlačiarňami lístkov je späť v hre. Stále to môže mať ťažšie, pretože títo bohatí jednotlivci si stále môžu kúpiť viac tlačiarní ako on, ale aspoň teraz nie je rádovo prekonaný len z jedného stroja. Je konkurencieschopný svojím malým spôsobom.  
  
S vedomím, že aj ten malý chlapec môže byť konkurencieschopný v ťažbe Monera, odporúčame každému, aby si to vyskúšal, buď v peňaženke GUI Monero, ktorá má podporu pre sólo ťažbu, alebo stiahnutím komunitou udržiavaného softvéru. Je to jednoduché, konkurencieschopné a otvorené pre všetkých.

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

  * [Ako prstencové podpisy zakrývajú výstupy Monera](/knowledge/ring-signatures)/

  * [Ako Monero vyriešilo problém veľkosti bloku, ktorý trápi Bitcoin](/knowledge/dynamic-block-size)/

  * [Ako CLSAG zlepší efektivitu Monero](/knowledge/what-is-clsag)/

  * [Prečo má Monero chvostovú emisiu](/knowledge/monero-tail-emission)/

  * [Stručná história Monera](/knowledge/monero-history)/

  * [Wired Magazine sa o Monere mýli, tu je dôvod](/knowledge/wired-article-debunked)/

  * [Top 15 vyvrátených mýtov a obáv o Monero](/knowledge/monero-myths-debunked)/

  * [Ako Dandelion++ uchováva pôvod transakcií Monero v súkromí](/knowledge/monero-dandelion)/

  * [Prečo je Monero open source a decentralizované](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Prečo je Monero lepšie ako Dash, Zcash, Zcoin (dokonca aj s Lelantus), Grin a bitcoinové mixéry ako Wasabi (aktualizované v máji 2020)](/knowledge/why-monero-is-better)/