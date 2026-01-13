---
title: "Ako podadresy Monero zabraňujú prepojeniu identity"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero vždy nachádzalo inovatívne spôsoby riešenia zložitých problémov so súkromím. Tieto inovácie často vedú k ďalším inováciám a niekedy možno tieto výsledné technológie dokonca použiť na prípady, o ktorých sa predtým neuvažovalo. Nikde to nie je doložené viac ako v prípade technológie podadresy Monero.

Zvážte hypotetický problém ochrany osobných údajov, kde použitie jednej adresy na viacerých platformách od zdanlivo nesúvisiacich ľudí môže viesť k prepojeniu a deanonymizácii uvedených ľudí. Zjednodušene povedané, ak by ste boli osoba menom Billy Joe Bob a predávali ste jablká za bitcoiny, mohli by ste svoju bitcoinovú adresu zverejniť na verejnom mieste, aby vám zákazníci mohli zaplatiť. Povedzme, že adresa začína alfanumerickým reťazcom 7XybV3... Ale ak odmyslíme zjavné riziko ochrany osobných údajov, že ktokoľvek bude môcť skontrolovať váš zostatok v bitcoinoch a zistiť, koľko ste predali, je tu druhé, o riziku ochrany osobných údajov, o ktorom sa často nehovorí. Povedzme, že ste boli tiež podzemným hackerom pod menom l33tz0r. Robíte udavačskú prácu, hovoríte nič netušiacemu ľudu o vládnej korupcii a je nevyhnutné, aby ste udržali svoju identitu v tajnosti. Prijímate bitcoinové dary za svoju prácu a adresu zverejníte na verejnom fóre. Je to tá istá adresa, na ktorej prijímate peniaze od svojich zákazníkov Apple. 7XybV3... jeden.

Jednoduchým, ale zničujúcim deanonymizačným útokom by bolo použitie internetového vyhľadávača na vyhľadanie vašej bitcoinovej adresy. Vloženie adresy 7XybV3... do motora prináša dva rôzne výsledky. Obchod s jablkami a l33tz0r. To stačí na prepojenie dvoch identít a deanonymizáciu l33tz0r s potenciálne desivými následkami zo strany mocností.

Je dôležité poznamenať, že tento útok je možný AJ s Monero. Aj keď Monero skrýva väčšinu údajov v reťazci, tento útok nepoužíva žiadne. Používa iba adresu, ktorá musí byť zdieľaná, aby bolo možné prijať platbu. Verejne v prípade anonymných darov. Toto je jeden z možných spôsobov, ako môžu používatelia Monero nevedomky poškodiť svoje súkromie, a je to tiež príklad toho, že aj keď je Monero na najvyššej úrovni, pokiaľ ide o zachovanie súkromia, nie je nepriestrelné.

Zvyčajným spôsobom, ako tento problém obísť, bolo vlastníctvo viacerých peňaženiek. S rôznymi adresami zverejnenými pre každú identitu (alebo prípad použitia) ich nemožno prepojiť. Toto súkromie však platí iba vtedy, ak ich používateľ nikdy nezmieša. Náhodné uverejnenie nesprávnej adresy by malo rovnaké účinky prepojenia. Okrem toho musí byť základ každej adresy zabezpečený, čím sa zvyšuje potreba informačnej bezpečnosti s každou novou vyrobenou peňaženkou.

Riešením spoločnosti Monero boli podadresy. Schopnosť vytvoriť absolútne obrovské množstvo adries pod hlavnou adresou a použiť ju ako zárodok. Každá vygenerovaná podadresa môže akceptovať Monero a všetko ide do rovnakej peňaženky. Pri použití tejto metódy je počet identít, ktoré je možné prevádzkovať pod jednou adresou, obrovský, pričom práca s infosec je obmedzená na minimum. Tieto adresy tiež nie sú matematicky prepojiteľné, takže pokiaľ používateľ nezakričí svoje spojenie so svetom, vonkajší pozorovateľ bude mať veľké problémy s ich prepojením.

Ale ďalší zaujímavý prípad použitia sa objavil z podadries; ako náhradná možnosť všeobecne nenávidených platobných identifikátorov.

Identifikátory platieb predstavovali pre obchodníkov spôsob, ako identifikovať, ktorý zákazník odoslal ktorú platbu. Keďže informácie Monero sú v reťazci zakryté, príjemca transakcie nemôže vidieť, ktorá adresa ju odoslala. To znamená, že ak existujú položky s podobnou cenou a viacero objednávok, môže byť nemožné identifikovať, kto čo poslal. Platobné ID sú jedinečný, náhodný reťazec vygenerovaný obchodníkom a odovzdaný zákazníkovi. Zákazník to pridá ako samostatné pole pri odosielaní transakcie. Tento náhodný reťazec je umiestnený na blockchaine ako súčasť transakcie a týmto spôsobom je obchodník schopný identifikovať a triediť prichádzajúce transakcie.

Táto metóda bola chybná v niekoľkých smeroch. Po prvé, znižuje jednotnosť údajov v reťazci. Dodatočné jedinečné metaúdaje môžu spôsobiť, že niektoré transakcie budú stáť mimo davu, čím sa umožní heuristická analýza. To platí najmä vtedy, keď tieto metaúdaje nie sú povinné pre všetkých. Ak by sa to stalo povinným pre každého, pridalo by sa do blockchainu zbytočný priestor a nesledovalo sa to. Ak by sa platobné ID niekedy z akéhokoľvek dôvodu znova použilo, bolo by triviálne prepojiť dve transakcie ako prepojené. K tomu zvyčajne dochádzalo pri vkladoch na burze a ktokoľvek mohol jednoducho prepojiť transakcie ako vklad na burzu a od jedného konkrétneho jednotlivca.

Po druhé, z pohľadu UX vytvárajú ID platby už druhý krok, na ktorý nie sú používatelia kryptomien prichádzajúci z iných coinov zvyknutí, a ak na ne zabudnú, spôsobí to obchodníkovi obrovské bolesti hlavy, ktorý musí tieto transakcie identifikovať inými prostriedkami. Zvyčajne sa to uskutočnilo tak, že sa porozprávali priamo s každým zákazníkom, ktorý zabudol zadať ID platby, a potvrdili sa ďalšie identifikačné informácie, ktoré mohli poznať iba oni, ako napríklad kombinácia sumy, dátumu odoslania a ID transakcie.

Mnohí tento krok navyše zmeškali a dostali sa do bodu, keď niektoré zmenárne začali účtovať zákazníkom peniaze, ak ich peniaze museli manuálne získať kvôli zabudnutiu platobného ID. Iní zaťali zuby a zjedli dodatočné náklady na podporu, ale nikto z toho nemal radosť.

Existovalo na to jedno riešenie, integrované adresy, ktoré zlúčili adresu a ID platby do jedného reťazca, takže sa na to nedalo zabudnúť, ale prijatie bolo dosť slabé, napriek výhodám, ktoré by obchodníci získali z jeho zahrnutia. 

V zaujímavom zvrate udalostí prišli podadresy, aby zachránili situáciu. Schopnosť generovať veľké množstvo podadries na hlavnú adresu a identifikovať, ktoré transakcie prichádzali na ktoré podadresy, umožnila obchodníkom zbaviť sa platobných ID elegantným spôsobom a zároveň prijať novú generáciu technológie Monero. Odvtedy väčšina búrz a obchodných nástrojov prešla na podadresy ako primárny spôsob identifikácie transakcie.

To, čo začalo ako riešenie problému ochrany osobných údajov, sa zmenilo na niečo oveľa viac, čo vyriešilo veľký problém UX pre obchodníkov aj zákazníkov. Inovácia plodí viac inovácií, ktoré môžu často viesť k neočakávaným výhram pre každého. Monero to videlo znova a znova a vynakladá veľké úsilie na inováciu toho, čo je na blockchaine možné. Kto vie, aké ďalšie veci môžeme spoločne odomknúť?

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