---
title: "Moneroove prstenové podpisy vs CoinJoin ako vo Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Keďže nástroje ochrany osobných údajov spoločnosti Bitcoin získali väčšiu pozornosť a používanie, dostali sa pod väčšiu regulačnú kontrolu. Táto kontrola viedla k [nedávnemu oznámeniu](https://twitter.com/wasabiwallet/status/1503091503207432193) zo strany nástroja na ochranu osobných údajov bitcoinov, Wasabi Wallet, že začnú cenzúrovať a odmietať prichádzajúce vstupy do mixov, ktoré považujú za nezákonné alebo v rozpore s ich zmluvnými podmienkami, a zaplatia reťazovú analýzu, spoločnosť na „preverenie“ prichádzajúcich účastníkov mixu.

Používanie transakcií CoinJoin na zahmlievanie zdroja finančných prostriedkov v bitcoine je jadrom ochrany osobných údajov bitcoinu už mnoho rokov a problémy a riziká spojené s jeho používaním sú niektoré z kľúčových problémov, ktoré podpisy krúžkov spoločnosti Monero opravujú a bránia im .

V tomto blogovom príspevku sa stručne ponoríme do porovnania podpisov CoinJoin a prsteňov, ako aj toho, prečo prístup použitý v Monero vedie k väčšej odolnosti voči cenzúre, väčšiemu súkromiu a menším problémom pre používateľov.

## Čo je to transakcia CoinJoin?

## Čo je to transakcia CoinJoin?

Vzhľadom na to, že všetky transakcie sú v bitcoinoch úplne transparentné – odhaľujú odosielateľa, príjemcu a sumy – používatelia musia podniknúť ďalšie kroky, aby si zachovali svoje súkromie pred predchádzajúcimi odosielateľmi a budúcimi príjemcami ich finančných prostriedkov alebo riskovali cenzúru, sledovanie alebo krádež finančných prostriedkov prostredníctvom fyzického násilia.

Súčasné najlepšie riešenie pre súkromie na bitcoinoch je nástroj s názvom [“CoinJoin”](https://bitcoiner.guide/qna/coinjoin/), v ktorom 2 alebo viacerí používatelia spolupracujú (zvyčajne prostredníctvom centralizovaného koordinátora) na vytvorení špeciálnej transakcie, ktorá sťažuje prístup pozorovateľov zvonka, aby prepojili vstupy s výstupmi. Každý účastník komunikuje, aby spoločne vytvoril transakciu bez toho, aby odovzdal úschovu svojich prostriedkov, a na konci dostane výstup, ktorého predchádzajúca história je teraz pre vonkajších pozorovateľov nejasná (alebo zahmlená).

Toto prelomí históriu konkrétnych UTXO, čo umožňuje používateľom bitcoínov získať pri transakciách určitú mieru utajenia. CoinJoin (ako je implementovaný vo Wasabi Wallet a Samourai Wallet, dvoch najpoužívanejších nástrojoch CoinJoin pre bitcoiny) má však niekoľko hlavných nevýhod:

  * Keďže transakcie CoinJoin sú úplne voliteľné a vyžadujú si aktívnu účasť, každý účastník nevyhnutne preukáže, že sa snaží o väčšie súkromie ako u „normálnych“ používateľov bitcoinov, potenciálne ich vyčlení a spôsobí problémy s míňaním prostriedkov na mnohých regulovaných burzách alebo subjektoch. Každý používateľ nemôže poprieť, že sa zúčastnil transakcie CoinJoin.
  * Na to, aby ste našli ostatných, s ktorými môžete CoinJoin, väčšina prístupov k CoinJoin (vrátane Wasabi Wallet) využíva centralizovaného koordinátora, ktorý spája účastníkov a pomáha im komunikovať a vybudovať správnu transakciu CoinJoin. Tento centralizovaný koordinátor nikdy nemá v správe finančné prostriedky používateľov, ale získava rozsiahly prehľad o transakciách, ktoré koordinuje, môže cenzurovať prichádzajúce vstupy (ako v prípade Wasabi Wallet) a môže byť donútený zbierať alebo zdieľať informácie o účastníkoch CoinJoin.
  *   * Používatelia s veľkými sumami finančných prostriedkov na CoinJoin môžu často čakať hodiny (alebo dokonca dni!), aby našli dostatok účastníkov na CoinJoin, čo vedie k veľkým oneskoreniam od času, keď používateľ dostane finančné prostriedky, až po čas, keď ich môže minúť súkromne. 
  * Ochrana súkromia, ktorú poskytuje transakcia CoinJoin, sa časom zhoršuje, pretože ostatní účastníci míňajú prostriedky alebo spájajú svoje výstupy so svojou identitou prostredníctvom výmen KYC, obchodníkov vyžadujúcich ID atď. ich anonymita („dav sa schovať“) čo najčerstvejšie.
  * Vo väčšine prístupov k CoinJoin musia účastníci používať UTXO s pevnou veľkosťou (t.j. 0,1 BTC), aby sa sťažilo pripojenie vstupov a výstupov transakcií CoinJoin. To vedie k vyšším poplatkom (viac samostatných transakcií potrebných na jeden veľký vstup), „toxickejším zmenám“ (finančné prostriedky, ktoré sú nevyčerpateľné bez vážneho rizika pre súkromie) a môže zabrániť tomu, aby sa menší používatelia vôbec mohli miešať, ak nemajú minimálny požadovaný zostatok.

## Ako tieto problémy riešia prsteňové podpisy?

## Ako tieto problémy riešia prsteňové podpisy?

Keďže [ sme v minulosti dôkladne preskúmali, aké sú prsteňové podpisy](/knowledge/ring-signatures), nebudem v tomto blogovom príspevku zachádzať do veľkých podrobností o technických aspektoch ich fungovania. Namiesto toho sa pozrieme na to, ako prístupy prijaté v Monero riešia problémy s CoinJoin, o ktorých sa hovorí vyššie.

> CoinJoin je prihlásený a vyžaduje účasť

CoinJoin je prihlásený a vyžaduje účasť

Vyzváňacie podpisy Monera sú základnou funkciou protokolu ochrany osobných údajov a _každá_ transakcia v sieti ich používa. To znamená, že žiadne transakcie používateľa nevynikajú snahou o väčšie súkromie ako „normálni“ používatelia Monero a všetci používatelia získajú hodnoverné popieranie, že minuli finančné prostriedky v danej transakcii. Keďže používateľ míňajúci prostriedky nekoordinuje ani sa nezúčastňuje na vstupoch návnady v transakcii, tí používatelia, ktorí vlastnia vstupy, ktoré boli náhodou vybrané ako návnady, môžu úprimne povedať, že sa na transakcii nezúčastnili, čím sa posilní ich súkromie.

> Použitie centralizovaného koordinátora

Použitie centralizovaného koordinátora

Keďže kruhové podpisy spoločnosti Monero sú úplne nekoordinované a na vytvorenie transakcie si vyžadujú len skutočné výdavky, v Monero nie je potrebný centralizovaný koordinátor. To zaisťuje, že _nikto_ vám nemôže odoprieť prístup k súkromiu v Monero a neexistuje žiadna centralizovaná entita, na ktorú by bolo možné vyvíjať nátlak, žiadne jednoduché útoky Sybil na likviditu atď. Pokiaľ vaša transakcia platí správne poplatky, získate necenzurovateľný prístup k súkromiu, bezpečnosti a anonymite v Monero.

> CoinJoin vyžaduje likviditu

CoinJoin vyžaduje likviditu

„Likvidita“ dostupná pre každého, kto utráca Monero na použitie ako návnady, je vždy celkovým súborom výstupov v reťazci, takže nikdy nebude nedostatok návnad, v ktorých sa dá schovať v Monero. Niekto, kto chce minúť Monero, tak môže urobiť ~20 minút po prijatí finančných prostriedkov a nemusí vykonať žiadne ďalšie kroky na získanie silného súkromia v Monero.

> Ochrana súkromia CoinJoin sa časom zhoršuje

Ochrana súkromia CoinJoin sa časom zhoršuje

Vzhľadom na to, že výstupy Monero nie sú nikdy vynakladané sieťou, súkromie poskytované kruhovými podpismi je v priebehu času oveľa menej náchylné na degradáciu. Používateľ nemusí neustále vracať výstupy v Monero a okrem mimoriadne zriedkavých okolností nestráca v priebehu času žiadne súkromie.

Ak však používateľ chce „obnoviť“ použité návnady pomocou výstupu, môže si prostriedky jednoducho poslať späť a minúť ich o ~20 minút neskôr ako zvyčajne.

> CoinJoin zvyčajne vyžaduje vstupy s pevnou veľkosťou

CoinJoin zvyčajne vyžaduje vstupy s pevnou veľkosťou

Keďže sumy sú skryté v každej transakcii pomocou [„Dôverné transakcie“](/knowledge/monero-ringct) (súčasť „RingCT“), návnady použité v danej transakcii môžu mať akúkoľvek veľkosť. Nie je dôvod sa obávať heuristiky založenej na sume v Monero, a preto sa transakcie vytvárajú oveľa jednoduchšie a môžu využiť návnady z akéhokoľvek bodu v čase a akéhokoľvek množstva na blockchaine Monero.

## Ako sa môžem dozvedieť viac?

## Ako sa môžem dozvedieť viac?

Ak ste zvedaví a chcete lepšie porozumieť prsteňovým podpisom alebo transakciám CoinJoin, pozrite si nižšie uvedené odkazy, kde nájdete skvelé miesta, kde začať:

  * [Ako prstencové podpisy zakrývajú výstupy Monera](/knowledge/ring-signatures)
  * [Prstenný podpis – Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [Prehľad CoinJoin](https://6102bitcoin.com/coinjoin-overview/)

Ďalšie čítanie

  * [Ako Monero jedinečne umožňuje obehové ekonomiky](/knowledge/monero-circular-economies)/

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

  * [Monero Mining: Čo robí RandomX tak výnimočným](/knowledge/monero-mining-randomx)/

  * [Prečo je Monero lepšie ako Dash, Zcash, Zcoin (dokonca aj s Lelantus), Grin a bitcoinové mixéry ako Wasabi (aktualizované v máji 2020)](/knowledge/why-monero-is-better)/

Ďalšie čítanie