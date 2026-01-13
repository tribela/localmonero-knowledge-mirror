---
title: "Seraphis: Čo to urobí pre Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: modulárny dizajnový upgrade pre transakcie Monero

Tento príspevok popisuje [Seraphis](https://github.com/UkoeHB/Seraphis), súbor štruktúr transakčných protokolov a abstrakcií vyvinutých pseudonymným výskumným prispievateľom [`koe`](https://github.com/UkoeHB) pre ekosystém Monero a s prebiehajúcou bezpečnostnou analýzou od pseudonymného prispievateľa [`coinstudent2048`](https://github.com/coinstudent2048).  
Z dôvodu prehľadnosti robíme určité zjednodušenia a vynechávame určité technické detaily; z tohto dôvodu a vzhľadom na to, že návrh Seraphisu stále prebieha, čitatelia, ktorí majú záujem, by si mali pozrieť najaktuálnejšie informácie v dokumentácii Seraphis.

## Transakcie v Monero

Protokoly ako Bitcoin a Monero a ďalšie sa spoliehajú na takzvaný „výstupný model“ fungovania, kde _výstup_ predstavuje reprezentáciu hodnoty, ktorú možno previesť.  
Transakcie spotrebujú jeden alebo viac výstupov riadených odosielateľom a generujú nové výstupy smerujúce k príjemcom (alebo späť k odosielateľovi ako zmena); transakcia musí byť v rovnováhe v tom, že spotrebované výstupy musia obsahovať celkovú hodnotu presne rovnajúcu sa hodnote v nových výstupoch (plus poplatok uložený sieťou).  
V mnohých protokoloch, ako je bitcoin, je hodnota obsiahnutá vo výstupe zapísaná jasne, rovnako ako príjemca.  
Okrem toho pri pohľade na blockchain je triviálne vidieť, či a kedy bol výstup spotrebovaný (to znamená, či bol spotrebovaný v neskoršej transakcii a ktorá transakcia ho minula).

Naproti tomu protokoly ako Monero zavádzajú iný dizajn:

  * Výstupné hodnoty sú skryté a nie sú viditeľné na blockchaine
  * Adresy príjemcov sú skryté pomocou jednorazového adresovacieho protokolu
  * To, či bol výstup vyčerpaný alebo nie, je zakryté použitím nejednoznačných podpisov

Výsledkom je, že bez externých informácií je ťažké určiť, či sa daný výstup minul, aká je jeho hodnota a kto je jeho príjemcom.

Aktuálny transakčný protokol Monero sa nazýva _RingCT_ a na dosiahnutie týchto cieľov návrhu používa niekoľko kryptografických stavebných blokov.

  * _Záväzky_ skrývajú sumy matematicky užitočným spôsobom
  * _Dosahové dôkazy_ zabraňujú pretečeniu, ktoré by mohlo nafúknuť zásobu
  * _Prepojiteľné kruhové podpisy_ poskytujú nejednoznačnosť podpisovateľa a zabraňujú pokusom o dvojité utratenie
  * _Kompenzácie záväzkov_ potvrdzujú, že transakcie sú vyrovnané

Tieto stavebné bloky sú starostlivo prepojené, aby vytvorili protokol RingCT.

Užitočnou vlastnosťou protokolu RingCT je to, že niektoré stavebné bloky možno zmeniť alebo upgradovať spôsobom, ktorý zachová celkový dizajn a vlastnosti nedotknuté, ale môže to priniesť zlepšenie efektívnosti alebo zabezpečenia. V skutočnosti sa tieto druhy upgradov vyskytli (alebo sa plánujú uskutočniť) niekoľkokrát v histórii spoločnosti Monero. Dôkazy rozsahu v pôvodnom protokole RingCT boli objemné a pomalé; neskôr boli aktualizované na konštrukciu nazvanú [Bulletproofs](https://eprint.iacr.org/2017/1066), vďaka ktorej boli transakcie menšie a rýchlejšie s lepšou bezpečnostnou analýzou, a plánuje sa ich aktualizácia na novšiu konštrukciu s názvom [Bulletproofs+](https://eprint.iacr.org/2020/735) pre ešte vyššiu efektivitu. 

Podobný proces bol vykonaný s prepojiteľným stavebným blokom kruhového podpisu. V pôvodnom protokole bola použitá konštrukcia nazvaná [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34). Toto bolo neskôr aktualizované na novšiu konštrukciu s názvom [CLSAG](https://eprint.iacr.org/2019/654), ktorá je rýchlejšia, vedie k menším transakciám a má lepšiu bezpečnostnú analýzu. Bola navrhnutá ešte novšia konštrukcia prepojiteľného kruhového podpisu založená na [Triptychu](https://eprint.iacr.org/2020/018), ale tento nebol vybraný na nasadenie kvôli jeho dopadom na operácie s viacerými podpismi.

## Seraphis (Serapis)

Seraphis posúva túto myšlienku o krok ďalej.  
Namiesto aktualizácie jednotlivých stavebných blokov existujúceho transakčného protokolu RingCT zavádza iný protokol, ktorý môže využívať výhody rôznych stavebných blokov a ponúka vylepšené funkcie.

## Stavebné bloky

Seraphis používa na dosiahnutie svojich návrhových cieľov inú sadu kryptografických stavebných blokov.

  * _Záväzky_ stále skrývajú sumy
  * _Dosahové dôkazy_ stále zabraňujú pretečeniu a inflácii ponuky
  * _Dôkazy o členstve_ poskytujú nejednoznačnosť podpisovateľa
  * _Kompenzácie záväzkov_ stále potvrdzujú rovnováhu
  * _Dôkazy o oprávnení_ zabraňujú pokusom o dvojité výdavky

Všimnite si zmenu tu: prepojiteľné kruhové podpisy sú nahradené kombináciou dokladov o členstve a dokladov o autorizácii. Zhruba povedané, dôkazy o členstve ukazujú, že spotrebovaný výstup je súčasťou väčšieho súboru, podobne ako v RingCT. Na rozdiel od RingCT však dôkazy o členstve vôbec nezahŕňajú prepojovaciu značku! Autorizačné dôkazy ukazujú, že prepájací tag je platný a používajú sa na podpísanie konečnej transakcie.

Keďže RingCT prepája značku do nejednoznačného podpisu, operácie podpisovania (a viacerých podpisov) sú výpočtovo náročnejšie a vytváranie ďalších funkcií súvisiacich so značkami je náročnejšie. Ale v Seraphise môže byť vytváranie dôkazov o členstve bezpečne delegované z vysoko dôveryhodných zariadení (ktoré môžu mať obmedzený výpočtový výkon, ako napríklad hardvérová peňaženka) na menej dôveryhodné zariadenie a operácie podpisovania (a viacnásobného podpisu) sú oveľa jednoduchšie pomocou oveľa jednoduchšieho overovania. .

Našťastie, niektoré stavebné bloky vyžadované spoločnosťou Seraphis už existujú inde a netreba ich navrhovať od začiatku. Ako nepriestrelné, tak aj nepriestrelné+ konštrukcie môžu byť použité ako dôkazy rozsahu. Úpravy dokazovacích systémov typu Schnorr možno použiť na autorizáciu dôkazov. A efektívny [provingový systém](https://eprint.iacr.org/2015/643), ktorý sa už používa ako základ pre Triptych, [Lelantus](https://eprint.iacr.org/2019/373) a [Spark](https://eprint.iacr.org/2021/1173)* môže byť upravený ako dôkaz členstva.

* Cypher Stack dostáva financie na vývoj Spark.

## Adresovanie

Momentálne používané adresy Monero žiaľ nie sú kompatibilné so Seraphis. Používatelia by museli vygenerovať nové adresy zo svojich kľúčov peňaženky, aby mohli dostať Monero, ak by bol implementovaný Seraphis. Tieto náklady na ekosystém však prinášajú množstvo výhod.

Okrem konštrukčných výhod diskutovaných vyššie je dizajn Seraphis prístupný mnohým rôznym možnostiam konštrukcie adries, z ktorých každá prichádza s kompromismi. Zatiaľ čo o konečnej konštrukcii adresy, ktorá sa má použiť v Seraphise [ sa stále rozhoduje](https://github.com/monero-project/research-lab/issues/92) (jedna schéma, ktorej sa venuje veľká pozornosť, sa nazýva [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), môžeme popísať niektoré bežné a užitočné funkcie.

Možno viete, že adresy Monero ponúkajú funkciu _kľúč zobrazenia_ , kde môžete poskytnúť kľúč zobrazenia zariadeniu alebo tretej strane a umožniť im sledovať prichádzajúce výstupy vo vašom mene, ale bez toho, aby ste museli utrácať autoritu. To je užitočné pre peňaženky, ktoré môžu zostať aktualizované a zároveň držať kľúč na výdavky bezpečne uzamknutý. Je to užitočné aj v prípadoch, keď chcete prístup k externému pohľadu, ako je napríklad verejná charitatívna organizácia ponúkajúca transparentnosť alebo spoločnosť s účtovným oddelením.

Nevýhodou tlačidiel zobrazenia Monero je, že neposkytujú úplný alebo podrobný prístup k zobrazeniam. Nie je možné spoľahlivo zistiť, kedy peňaženka míňa prostriedky, čo sťažuje správny výpočet zostatkov v peňaženke, keď kľúč na výdavky nie je k dispozícii. V súčasnosti tiež nie je možné zistiť prichádzajúce výstupy bez toho, aby ste sa naučili aj hodnotu obsiahnutú v týchto výstupoch (čo znamená, že akékoľvek tretie strany zodpovedné za vyhľadávanie prichádzajúcich výstupov sa presne dozvedia, koľko Monera získavate).

Adresujúce konštrukcie Seraphis to môžu vyriešiť. So Seraphis je vaša adresa vybavená rôznymi klávesmi, ktoré môžu robiť rôzne veci:

  * Sledujte prichádzajúce výstupy, ale skryte ich hodnotu
  * Sledujte prichádzajúce výstupy, ale ukážte ich hodnotu
  * Sledovať odchádzajúce výstupy
  * Pomôže vám generovať transakcie, ale nepodpísať ich
  * Generujte nové adresy (užitočné pre maloobchodníkov alebo burzy s mnohými zákazníkmi)

Ako držiteľ adresy sa môžete rozhodnúť, koľko právomocí delegujete na iné zariadenia alebo tretie strany.

## Veľký obraz

Seraphis je veľkou zmenou v ekosystéme Monero. Aj keď zahŕňa úpravy adries a stavebných blokov transakcií, jeho dizajn ponúka flexibilitu a užitočnú funkčnosť, ktorú dnešný protokol RingCT neumožňuje. Zatiaľ čo veľká časť návrhu je dokončená a vyvíja sa na [implementáciu](https://github.com/UkoeHB/monero/tree/seraphis_lib), návrh adries a analýza bezpečnosti stále prebiehajú. Seraphis ponúka vynikajúcu príležitosť posunúť ekosystém Monero dopredu!

Ďalšie čítanie