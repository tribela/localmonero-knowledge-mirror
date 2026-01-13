---
title: "Hogyan akadályozzák meg a Monero alcímek az identitás összekapcsolását"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
A Monero mindig talált innovatív módszereket a nehéz adatvédelmi problémák megoldására. Gyakran ezek az innovációk további újításokhoz vezetnek, és néha ezek a technológiák olyan felhasználásra is alkalmasak, amelyekre korábban senki nem gondolt. Ennek a legjobb példája a Monero alcím-technológiája.

Tekintsünk egy feltételezett problémát, amelyben egy cím több platformon keresztüli használata látszólag nem összefüggő emberektől az említettek összekapcsolásához és deanonimizálásához vezethet. Leegyszerűsítve, ha Ön Billy Joe Bob, aki almát ad el Bitcoinért, akkor nyilvános helyen közzé kellett tennie Bitcoin-címét, hogy az ügyfelek fizetni tudjanak Önnek. Tegyük fel, hogy a cím a 7XybV3 alfanumerikus karakterlánccal kezdődik... Félretéve azt a nyilvánvaló kockázatot, hogy bárki megnézheti a Bitcoin-egyenlegét, és láthatja, mennyit adott el, van egy második, ritkán emlegetett adatvédelmi kockázat. Tegyük fel, hogy Ön egy egyben egy underground hacker, l33tz0r néven. Leleplező munkát végez, a gyanútlan lakosságnak beszámolva a kormányzati korrupcióról, és elengedhetetlen, hogy titokban tartsa személyazonosságát. Bitcoin adományokat fogad el a munkájához, ezért közzéteszi a címet egy nyilvános fórumon. Ez ugyanaz a cím, ahova az almás ügyfeleitől fogad pénzt, a 7XybV3... kezdetű.

Egy egyszerű, de pusztító deanonimizálási támadás lenne, ha egy internetes keresővel utánakeresnek a Bitcoin címnek. A 7XybV3... címre két különböző találat lesz. Az almás üzlet, és l33tz0r. Ez elég a két identitás összekapcsolásához és l33tz0r deanonimizálásához, ami a hatalom részéről ijesztő következményekkel járhat.

Fontos megjegyezni, hogy ez a támadás a Moneronál IS lehetséges. Annak ellenére, hogy a Monero elrejti a legtöbb láncon lévő adatot, ez a támadás nem használja ki azokat. Csak a címmel dolgozik, amelyet meg kell osztani a fogadásához. Névtelen adományok esetén nyilvánosan. Ez egy lehetséges módja annak, hogy a Monero felhasználók akaratlanul is megsértsék a magánéletüket, és arra is példa, hogy bár a Monero a legmagasabb szinten van adatvédelem terén, azért nem csodaszer.

A probléma megkerülésének megszokott módja a több pénztárca használata volt. Ha minden identitáshoz (vagy felhasználáshoz) különböző címeket adunk meg, nem lesznek összekapcsolhatók. De ez az adatvédelem csak akkor működik, ha a felhasználó soha nem téveszti össze őket. A nem megfelelő cím véletlen közzététele ugyanazt az összekapcsolást teszi lehetővé. Továbbá az egyes címekhez tartozó seedeket is mind biztonságban kell tartani, ami minden egyes további pénztárcánál megnöveli a szükséges biztonsági erőfeszítést.

A Monero megoldása az alcímek bevezetése volt. A képesség, hogy az elsődleges cím alapján számtalan alcímet hozhassunk létre, forrásként használva azt. Mindegyik alcímre lehet Monerot fogadni, és mind ugyanabba a pénztárcába kerül. Ezzel a módszerrel óriási az egy cím alatt működtethető identitások száma, miközben az adatbiztonsági munka nem szokszorozódik meg. Ezek a címek matematikailag sem kapcsolhatók össze, így ha a felhasználó nem kiáltja világgá, akkor egy külső szemlélőnek komoly nehézségekbe ütközik az összekapcsolásuk.

De egy másik érdekes felhasználása is megjelent az alcímeknek: a széles körben megvetett fizetési azonosítók kiváltása.

A fizetési azonosítók segítségével a kereskedők azonosítani tudják, melyik ügyfél melyik befizetést küldte. Mivel a Monero információk a láncon rejtve vannak, a tranzakció címzettje nem láthatja, melyik címről érkezett. Ez azt jelenti, hogy hasonló árú cikkek és több rendelés esetén lehetetlenné válhat annak azonosítása, melyik kihez tartozik. A fizetési azonosító egy egyedi, véletlenszerű karakterlánc, amelyet a kereskedő generál és ad át az ügyfélnek. Az ügyfél ezt külön mezőben adja hozzá a tranzakció elküldésekor. Ez a véletlenszerű karakterlánc a tranzakció részeként rákerül a blokkláncra, így a kereskedő azonosítani és rendszerezni tudja a bejövő tranzakciókat.

Ennek a módszernek több hibája is volt. Először is, rontja a láncon lévő adatok egyformaságát. A további, egyedi metaadatok egyes tranzakciókat kiemelhetnek a tömegből, ezáltal lehetővé téve a heurisztikus elemzést. Ez különösen akkor igaz, ha ezek a metaadatok nem mindenki számára kötelezőek. Ha ez mindenki számára kötelező lenne, az feleslegesen növelné a blokklánc helyfoglalását, ezért nem lett bevezetve. Továbbá, ha egy fizetési azonosítót bármilyen okból újrahasználnak, triviális lenne két tranzakciót összekapcsolni. Ez jellemzően tőzsdei betéteknél fordult elő, és bárki könnyen összekapcsolhatta a tranzakciókat, egyrészt tőzsdei betétként, másrészt adott személytől származóként.

Másodszor, a felhasználói élmény szemszögéből a fizetési azonosítók egy további lépést iktatnak be, amihez nincsenek hozzászokva a más láncokról érkező kriptovaluta felhasználók, és ha elfelejtődik, az hatalmas fejfájást okoz a kereskedőnek, akinek más megoldást kell találnia a tranzakciók azonosítására. Ez általában úgy történik, hogy közvetlenül beszél minden olyan ügyféllel, aki elfelejtette megadni a fizetési azonosítót, és egyéb csak általuk ismert információkra – például összeg, a küldés dátuma, tranzakcióazonosító – kérdez rá az azonosításhoz.

Az extra lépést sokan kihagyták, ez odáig fajult, hogy egyes tőzsdék további költségeket kezdtek felszámítani az ügyfeleknek, ha a pénzüket manuálisan kellett lekérni, mert elfelejtették a fizetési azonosítót megadni. Mások a fogukat csikorgatva lenyelték a megnövekedett támogatási költségeket, de a helyzet senkit nem tett boldoggá.

Létezett egy megoldás volt erre, az integrált címek, amelyek egy karakterláncba egyesítették a címet és a fizetési azonosítót, így nem lehetett elfelejteni a megadást, de az elterjedése meglehetősen gyér volt, annak ellenére, hogy a kereskedők jól jártak volna a támogatásával. 

Az események érdekes fordulatként az alcímek jelentek meg, hogy megoldják a helyzetet. A képesség, hogy főcímenként nagy mennyiségű alcímet lehet generálni, és azonosítani, mely tranzakciók melyik alcímre érkeztek, lehetővé tette a kereskedők számára, hogy elegáns módon megszabaduljanak a fizetési azonosítóktól, miközben bevezetik a Monero technológia következő generációját. Azóta a legtöbb tőzsde és kereskedői eszköz az alcímeket használja, mint a tranzakciók azonosításának elsődleges módját.

Ami egy adatvédelmi probléma megoldásaként indult, az sokkal többé vált, megoldott egy a kereskedők és az ügyfelek számára egyaránt fontos problémát a felhasználói élmény kapcsán. Az innováció még több innovációt szül, ami gyakran mindenki számára váratlan előnyöket eredményezhet. Monero újra és újra megtapasztalta ezt, és komoly erőfeszítéseket tesz a blokkláncon lehetséges innovációk elősegítésére. Ki tudja, milyen dolgokat tárhatunk még fel együtt?

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

  * [Monero bányaszat: Mitől olyan különleges a RandomX?](/knowledge/monero-mining-randomx)/

  * [Miért jobb a Monero, mint a Dash, a Zcash, a Zcoin (még Lelantussal is), a Grin és a Bitcoin mixerek, mint a Wasabi (Frissítve 2020 májusában)](/knowledge/why-monero-is-better)/

További olvasnivaló