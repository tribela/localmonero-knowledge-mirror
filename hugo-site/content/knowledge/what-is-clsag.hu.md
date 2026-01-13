---
title: "Hogyan javítja a CLSAG a Monero hatékonyságát"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Protokollként a Monero folyamatos innováció alatt van. Mind a láncon belüli, mind a láncon kívüli megoldások kutatási eredményeit felhasználva a Monero közösség olyan területeket keres, amin javítani lehet, hogy a Monero privátabbá, skálázhatóbbá és széles körben elérhetőbbé váljon. Az egyik frissebb fejlesztés az összekapcsolható gyűrűs aláírási séma, az MLSAG lecserélése a CLSAG-ra, ami a Concise Linkable Spontaneous Anonymous Group rövidítése.

A felszínen a CLSAG megvalósítása 25%-kal csökkenti a leggyakoribb '2 bemenet - 2 kimenet' tranzakciók méretét. A megerősítéshez szükséges idő is 10%-kal csökken.

De mi is a CLSAG? Hogyan működik és miben különbözik a régi verziótól, az MLSAG-tól? Szánjunk egy percet rá, és emlékezzünk vissza a gyűrűs aláírások miértjére és mikéntjére, hogy jobban megérthessük a fogalmat. A gyűrűs aláírások lehetővé teszik a megkülönböztethetetlen bemeneteket az aláíró által nem-interaktívan kiválasztott korábbi kimeneteket anonimitáskészletként használva. Laikus kifejezéssel élve, lehetővé teszi a felhasználó számára, hogy elrejtse a tranzakció során használt kimeneteit más nem kapcsolódó kimenetek között, mindezt anélkül, hogy bárki mással együtt kellene működnie. Csak a blokklánc másolatára van szükség. Kívülről úgy tűnik, hogy mindegyik kimenet nagyjából egyformán valószínű, hogy ténylegesen elküldésre került, így rejtve el a feladó metaadatait.

Ez azonban problémát okozhat. Mi történik, ha a felhasználó olyan gyűrű aláírást készít, ahol az összes kimenet hamis? Honnan tudhatná bárki, hogy az ismeretlen feladónak nincs joga elküldeni egyiket sem? Képes lenne ez a felhasználó hamis pénzt költeni? A válasz: nem. A gyűrűs aláírás bizonyítékot tartalmaz, hogy a kimenetek közül legalább az egyik a feladó tulajdona, anélkül, hogy felfedné, melyik az. Valójában mind a CLSAG, mind az MLSAG (a továbbiakban: SAG) az a része a gyűrűs aláírásnak, amely ezt bizonyítja. Érdekes módon ugyanakkor azt is ez bizonyítja, hogy a tranzakció – bár az összege bizalmas tranzakciók (RingCT) mögé van rejtve – egyensúlyban van. Az, hogy az SAG-k két dolgot bizonyítanak, miszerint az egyik kimenet a gyűrűben valakinek a tulajdonában van, és hogy a tranzakció egyensúlyban van, nagyon fontos, igazából ebben rejlik a méretbeli és ellenőrzési megtakarítás lehetősége. Ha ez kezd zavarossá válni, ne aggódjon, hamarosan egy szórakoztató és könnyen érthető hasonlatot mutatunk be.

A régi aláírási séma, az MLSAG (Multilayered Linkable Spontaneous Anonymous Group) bebizonyítja a fenti két dolgot a gyűrűs aláírásban, de mindegyiket külön-külön. A külön számítások használata az aláírási és kötelezettségvállalási kulcsokhoz lassabb műveletekhez vezet. Egy modern számítógép ezredmásodpercek alatt képes elvégezni ezeket a számításokat, ami nem tűnik soknak, egyetlen tranzakciónál nem is az. De ha figyelembe vesszük a Monero blokklánc tranzakcióinak számát, és azt, hogy egy nulláról szinkronizáló csomópontnak mindegyiket le kell töltenie és ellenőriznie, a byte-ok és ezredmásodpercek gyorsan felhalmozódnak.

A CLSAG a két bizonyításához szükséges matematikát egyesíti, mindkettőt egyszerre számítja ki, és ezt biztonságos módon teszi. Mit jelent, hogy biztonságos módon? Nos, ennek tisztázása érdekében, és remélhetőleg az egésznek értelmet adva, vizsgáljuk meg a beígért szórakoztató analógiát.

Tegyük fel, hogy el kell mennie az élelmiszerboltba és vasáruért is, hogy két különböző dolgot vegyen: élelmiszert és mérgező tisztítószereket. Nem szeretné, hogy ezek összekeveredjenek, mert ha baleset történik, és a vegyszerek az ételre fröccsennek, ehetetlenné teszik őket. Úgy dönt, hogy rendkívül óvatos lesz, autóval elmegy otthonról az élelmiszerboltba, megveszi az ételt, majd hazaviszi. Csak miután kipakolta az élelmiszert, ül vissza az autóba, és megy el a másik boltba, majd a vegyszerekkel vissza otthonába. Két külön utat tett meg, hogy a vásárlás biztonságát garantálja. Bár ez valóban biztonságos, nem igazán hatékony. Ez az MLSAG-nak felel meg, ami két különböző matematikai halmazt tárol, két különböző „utazást” hajt végre azok kiszámításához.

Ön azonban úgy dönt, hogy szeretné ezt gyorsabban megoldani. Túl sok lenne az elvesztegetett idő. Persze, egyszer vagy kétszer, nem megy rá az egész élet, de ha ezt újra és újra meg kell tenni, az órák összeadódnak. Azon tűnődik, meg lehetne-e oldani egy utazással. Otthonról az élelmiszerboltba, tovább a vasáruért, majd haza. Nem lehet mindent bedobálni az autóba ötletszerűen. Nem lenne biztonságos. Ehelyett különböző helyeket jelöl ki az autójában a különböző áruk számára, gondoskodva arról, hogy minden elférjen a rendelt helyén. Ezáltal biztonságosan mehet el egy úttal mindkét üzletbe, távol tartva egymástól a vásárolt dolgokat. Ez a CLSAG. Így már csak egy számítási halmaz van tárolva a tranzakcióban, amely bizonyítja mindkét dolgot, olyan módon, hogy ezek nem zavarják egymást. Egy utazást így is meg kell tenni, de összességében a számuk drasztikusan csökkent.

Mindez elég izgalmasan hangzik. Lehetséges, hogy találunk más rövidítéseket, vagy egyéb módokat, amikkel időt és helyet spórolhatunk? A válasz egyszerre igen és nem. Jelenleg az MRL-kutatók szerint valószínűleg nem lehetséges tovább módosítani az SAG-típusú konstrukciókat a méret vagy sebesség érdekében; viszont más megoldások, mint az Arcturus, az Omniring, az RCT3, vagy a Triptych sokkal jobb méretezési és ellenőrzési tulajdonságokat biztosítanak különböző matematikai módszerek használatával. A 'félreérthető aláíró' protokollok „következő generációs” megközelítéseinek azonban megvannak a maguk hátrányai a megvalósítás részleteit illetően, ezért is aktív kutatás és vizsgálat alatt állnak.

Végső soron a Monero mindig fejlődésben van.

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

  * [Miért van a Monero hálózaton utólagos kibocsátás](/knowledge/monero-tail-emission)/

  * [A Monero rövid története](/knowledge/monero-history)/

  * [A Wired Magazin téved a Moneroval kapcsolatban, mégpedig ezért](/knowledge/wired-article-debunked)/

  * [A 15 legnépszerűbb Monero mítosz és kétely, cáfolva](/knowledge/monero-myths-debunked)/

  * [Hogyan rejti el a Dandelion++ a Monero tranzakciók eredetét](/knowledge/monero-dandelion)/

  * [Miért nyílt forráskódú és decentralizált a Monero](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero bányaszat: Mitől olyan különleges a RandomX?](/knowledge/monero-mining-randomx)/

  * [Miért jobb a Monero, mint a Dash, a Zcash, a Zcoin (még Lelantussal is), a Grin és a Bitcoin mixerek, mint a Wasabi (Frissítve 2020 májusában)](/knowledge/why-monero-is-better)/

További olvasnivaló