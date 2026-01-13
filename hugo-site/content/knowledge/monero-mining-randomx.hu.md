---
title: "Monero bányaszat: Mitől olyan különleges a RandomX?"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
2019\. november 30-án megtörtént a Monero féléves hard forkja, a leginkább várt változással, az átállással a régi PoW algoritmusról (cryptonight) a teljesen új, saját fejlesztésű RandomX-re. A Monero közösség úgy látja, hogy a RandomX nagy lépés az egalitárius bányászat felé, de vizsgáljuk meg közelebbről, hogy ez-e a helyzet.

## Cél

Annak megítéléséhez, hogy a RandomX előrelépés-e, először meg kell értenünk, mi a bányászat célja. A bányászat megvédi a blokkláncot a többszörös költésektől a Nakamoto Konszenzus révén. Ennek pontos részletei túlmutatnak ezen cikk keretein, de az interneten számos különböző forrásból megtudhatja őket. A lényeg hogy a biztonságot a számítógépek (bányászok) által generált hashek biztosítják, akik egymással versengve keresik az újabb blokk létrehozásához szükséges matematikai megoldást. Ennek során új tranzakciókat adnak hozzá a blokklánchoz. Munkájukért (a hashek) cserébe újonnan vert érméket kapnak.   
  
Számos probléma fordulhat ebben a felállásban, a megfelelő ösztönzőket kritikusak a működéshez, de most egy konkrét problémára fogunk összpontosítani, amely felmerülhet. Ha a bányászat verseny, mi történik, amikor egy bányász előnybe kerül?

## Háttér

Az érthetőség kedvéért beszéljünk egy kicsit a bányász hardvekről. A bányászok számítógépeket használnak a munkájukhoz, de mindannyian tudjuk, hogy nem minden számítógép egyenlő. Egyes számítógépek elég erősek mesterséges intelligencia hálózatok vagy intenzív játékok futtatásához, míg mások még egyszerű feladatokkal is megszenvednek. Ezek a teljesítménybeli különbségek a hashelési sebességet is befolyásolják, vagyis azt a sebességet, amellyel a blokkmegoldásokat keresik.   
  
De még ezek a számítógépek közötti különbségek is elhalványulnak a célhardverek, más néven alkalmazásspecifikus integrált áramkörök (ASIC) hash-arányaihoz képest, amelyek több nagyságrenddel felülmúlják a hagyományos számítógépeket.  
  
Szánjunk egy kis időt annak vizsgálatára, hogy mi teszi az ASIC-eket ennyivel erősebbé. Képzeljen el egy spektrumot, amin minden számítógép valahol elhelyezkedik, attól kezdve, hogy sok mindenre alkalmas, de egyikben sem különösen jó, odáig, hogy csak egy dolgot tud, de azt nagyon jól. A CPU-k és az ASIC-ek ennek a spektrumnak a két átellenes végén találhatók.  
  
A szabványos számítógépekben található CPU-k az első végén vannak. Sok mindenre képesek, például böngészhetnek az interneten, játékokat futtathatnak vagy videót jeleníthetnek meg, de egyikben sem különösen jók. Ennek a rugalmasságnak az ára a csökkentett hatékonyság.  
  
Az ASIC-ek a másik végletben vannak, ahol csak egy dologra képesek, de azt hihetetlen teljesítménnyel. Csak egyetlen matematikai függvényt tudnak végrehajtani, de mivel minden mást figyelmen kívül hagyhatnak, a sebesség csillagászati. Ennek a hatékonyságnak az ára a rugalmasság hiánya, tehát ha a függvény csak kis mértékben is megváltozik – például x + y = z helyett 2x + y = z-re változik –, akkor az ASIC teljesen haszontalanná válik.   
  
Nem mindenkinek van ASIC-je, de mindenki rendelkezik számítógéppel. Ez tisztességtelen előnyhöz vezethet.

## Egy mókás hasonlat

Ha ez még mindig zavaros, talán a következő hasonlat segíthet. Képzeljen el egy lottót, ahol óránként ezer dollárt osztanak ki, és a lottó megengedi, hogy saját szelvényeket nyomtasson! Ezért elkezd annyit nyomtatni, amennyit csak tud otthoni nyomtatóján, amely másodpercenként egy szelvényt tud kinyomtatni. Az elektromos áram és a tinta költségeinek levonása után azt látja, hogy még akkor is profitál, ha csak párhetente nyer a lottón.  
  
Idővel addig bővíti az üzemét, amíg egy egész helyiséget nem tart fenn a nyomtatóknak. Összesen 20-nak. Minden rendben megy... egészen egy végzetes napig.  
  
Nagy hírek érkeznek. Valaki feltalált egy új típusú nyomtatót. Csak sorsjegyeket tud nyomtatni. Nem tud képeket vagy irodai dokumentumokat kinyomtatni, vagy kétoldalas nyomtatást végezni. Csak sorsjegyeket. De abból másodpercenként 1000 kinyomtatására képes. Benéz a kis nyomtatószobájába. 20 nyomtató. 980 további nyomtatóra lenne szüksége ahhoz, hogy lépést tartson EGYETLEN ilyen szörnynyomtatóval, hát még ha valakinek kettő is van…  
  
Szomorúan kiszáll a játékból, mert már nem tudja kitermelni az áram- és tintaköltségeket.  
  
De várjunk! Pár hét múlva újabb hírek érkeznek! A jegy kialakítása megváltozott. Mostantól a számok, amelyek korábban fent voltak, alul vannak. Az új szörnynyomtatók annyira rugalmatlanok, hogy képtelenek kinyomtatni. Csak az előző terv alapján tudnak nyomtatni. Nemsokára ismét boldogan nyomtathat. Legalábbis addig, amíg valaki nem készít egy szörnynyomtatót az új dizájnhoz.

## RandomX

Hogy jön a RandomX ehhez az egészhez? Arra hivatott, hogy semlegesítse az ASIC-ek előnyeit azáltal, hogy rendkívől megnehezíti az elkészítésüket. Ennek érdekében, azt követeli meg a bányászoktól, hogy véletlenszerű kódot készítsenek el és futtassanak, nem egy fix algoritmust.  
  
Nem biztos, hogy egyértelmú, hogy ez miben is segít valójában, ezért térjünk vissza a nyomtatós hasonlathoz. Mi történt, amikor a design megváltozott? A régi óriásnyomtatók minden este elavultak, és újakat kellett fejleszteni. Mi történne, ha minden új lottószelvénynek minden egyes jackpot esetében új tervezési szabványhoz kellene megfelelnie?   
  
Új óriásnyomtatók létrehozása hihetetlenül nehéz lesz, már nem lehet egyetlen jegytervre készülni. Mivel a kinézet véletlenszerű, az óriásnyomtató-gyártóknak fel kell készülniük színes nyomtatásra, különböző betűtípusokra, szegélyek és formák nyomtatására és egyebekre. Röviden: a gép, amit a folyamat végén elkészül, egy szabványos, rendes nyomtató lenne. Mint ami mindenki másnak is van.  
  
Ennek a véletlenszerűségnek jegytervezésnek a megvalósításával lényegesen csökkentettük a speciális hardver használatából származó előnyt. A RandomX ugyanezt teszi a bányászattal.  
  
Ily módon a néhány kiváltságos jómódú ember által megszerzett előnyök minimálisra csökkennek, mivel ha a RandomX bányászatához szükséges ASIC-ek létrehozásába fektetnek, akkor valójában csak erősebb, jobb CPU-kat eredményeznek, ami a világ számára is előnyös.  
  
Ez azt jelenti, hogy a kisember a 20 nyomtatójával ismét játékban van. Valószínűleg még mindig nehezebb dolga van, hiszen a gazdagabbak több nyomtatót engedhetnek meg maguknak, mint ő, de legalább most nincs nagyságrendekkel lekörözve egyetlen eszközzel. A maga szerény módján versenyképes marad.  
  
Szem előtt tartva, hogy a Monero bányászatában még a kis hal is versenyképes lehet, mindenkit arra biztatunk, próbálja ki, akár a grafikus Monero tárcájában, amely támogatja az egyéni bányászatot, akár a közösség által karbantartott szoftverek letöltésével. Egyszerű, versenyképes, és mindenki számára elérhető.

További olvasnivaló

  * [A Monero egyedülálló módon teszi lehetővé a körkörös gazdaságokat](/knowledge/monero-circular-economies)/

  * [A Monero gyűrűs aláírásai kontra CoinJoin, mint a Wasabiban](/knowledge/ring-signatures-vs-coinjoin)/

  * [Miért (és hogyan!) érdemes a kulcsokat saját kézben tartani](/knowledge/hold-your-keys)/

  * [Hozzájárulás a Monerohoz](/knowledge/contributing-to-monero)/

  * [Hogyan befolyásolják a távoli csomópontok a Monero adatbiztonságát](/knowledge/remote-nodes-privacy)/

  * [Hogyan használja a Monero a hard forkokat a hálózat frissítéséhez](/knowledge/network-upgrades)/

  * [Nézetcímkék: Hogyan csökkenti egy byte adat a Monero tárcák szinkronizálási idejét 40+%-kal](/knowledge/view-tags-reduce-monero-sync-time)/

  * [A P2Pool és szerepe a Monerobányászat decentralizálásában](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Mit fog elhozni Moneronak](/knowledge/seraphis-for-monero)/

  * [A Bitcoin Monerora váltása ugyanolyan privát, mint a közvetlen vásárlás?](/knowledge/most-private-way-to-buy-monero)/

  * [Miért bizalommentes a Monero (a Zcash-sel ellentétben)](/knowledge/monero-trustless-setup)/

  * [Miért jobb értékmegőrző a Monero , mint a Bitcoin?](/knowledge/monero-better-store-of-value)/

  * [Hogyan tudja a Monero legyőzni a Bitcoin hálózati hatásait?](/knowledge/network-effect)/

  * [Miért a Monero közösségnek van a legkritikusabb gondolkodása](/knowledge/critical-thinking)/

  * [Átverések, amelyekre figyelni kell a Monero használatakor](/knowledge/monero-scams)/

  * [Hogyan működnek az oszthatatlan cserék Moneroban](/knowledge/monero-atomic-swaps)/

  * [Amit minden Monero felhasználónak tudnia kell, amikor a hálózatról van szó](/knowledge/monero-networking)/

  * [Hogyan rejti el a RingCT a Monero tranzakciók összegét?](/knowledge/monero-ringct)/

  * [Hogyan védik a Monero rejtett címek a személyazonosságát](/knowledge/monero-stealth-addresses)/

  * [Hogyan akadályozzák meg a Monero alcímek az identitás összekapcsolását](/knowledge/monero-subaddresses)/

  * [Monero kimenetek magyarázata](/knowledge/monero-outputs)/

  * [Monero bevált módszerek kezdőknek](/knowledge/monero-best-practices)/

  * [Hogyan rejtik el a gyűrűs aláírások a Monero kimeneteket](/knowledge/ring-signatures)/

  * [A Monero megoldása a Bitcoint sújtó blokkméret-problémára](/knowledge/dynamic-block-size)/

  * [Hogyan javítja a CLSAG a Monero hatékonyságát](/knowledge/what-is-clsag)/

  * [Miért van a Monero hálózaton utólagos kibocsátás](/knowledge/monero-tail-emission)/

  * [A Monero rövid története](/knowledge/monero-history)/

  * [A Wired Magazin téved a Moneroval kapcsolatban, mégpedig ezért](/knowledge/wired-article-debunked)/

  * [A 15 legnépszerűbb Monero mítosz és kétely, cáfolva](/knowledge/monero-myths-debunked)/

  * [Hogyan rejti el a Dandelion++ a Monero tranzakciók eredetét](/knowledge/monero-dandelion)/

  * [Miért nyílt forráskódú és decentralizált a Monero](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Miért jobb a Monero, mint a Dash, a Zcash, a Zcoin (még Lelantussal is), a Grin és a Bitcoin mixerek, mint a Wasabi (Frissítve 2020 májusában)](/knowledge/why-monero-is-better)/