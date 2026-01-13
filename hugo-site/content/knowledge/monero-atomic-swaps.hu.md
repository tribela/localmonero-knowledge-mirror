---
title: "Hogyan működnek az oszthatatlan cserék Moneroban"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
A decentralizációra és egy ténylegesen engedélyezés nélküli rendszerre törekedve kevés dolog áhított annyira a kriptovaluták világában, mint az elosztott tőzsdék és az oszthatatlan cserék lehetősége. A Monero létrejötte óta küszködik az oszthatatlan cserék megvalósításával, mivel az adatvédelmi funkciói egyedi kihívásokat jelentenek a protokoll megtervezésében.

Előbb azonban ugorjunk vissza az elejére. Mit jelent az, hogy 'oszthatatlan csere'? Az oszthatatlan csere olyan protokoll, amellyel két különböző kriptovaluta - különböző blokkláncokon – bizalomnélküli módon, közvetítő nélkül kicserélhető. Ez azt jelenti, hogy ha valaki A kriptovalutát szeretne B kriptovalutára cserélni, azt – akár centralizált, akár decentralizált – tőzsde nélkül is megteheti. Nem meglepő módon, ehhez komoly kutatás szükséges, és a technikai megvalósítás részletei meglehetős bonyolultságot érhetnek el. A LocalMonero azért van itt, hogy segítsen és a hétköznapi emberek számára is érthető magyarázatot adjon .

Kezdésnek nézzük az oszthatatlan csere legegyszerűbb formáját, amelyet a Bitcoin valósít meg. Ha valaki Bitcoint szeretne cserélni másik valutára, amely ugyanazt a 'Hash Time Locked Contract' technológiát használja, azt a következőképpen teheti meg: Annának Bitcoinja van (BTC), de Litecoint (LTC) szeretne, Bélának pedig LTC-je, de BTC-t akar helyette. Úgy döntenek, hogy cserét hajtanak végre, így mindketten megkapják a kívánt valutát. Anna elküldi a BTC-jét egy speciális címre, olyan Scriptet használva, amely zárolja a forrásokat, hogy még ő maga sem férhet hozzá. Úgy lehet elképzelni, mintha Anna egy páncéldobozba tenné a BTC-jét. Amikor a páncéldoboz elkészül, kap egy kulcsot, és elküldi ennek a kulcsnak a kivonatát [hash] Bélának, akinek ehhez nincsen kulcsa, ezért nem tud hozzáférni.

Béla ezt a hash-t bemenetként használja, amiből saját páncéldobozt állít elő, amiben elhelyezi az LTC-jét. Mivel Anna kulcsának kivonatát használták a doboz lezárásához, ő ezt megszerezheti az LTC-t Béla dobozából. A kulcsa illeszkedik a zárba! Ugyanakkor, a matematikai fekete mágia hatására, amikor a kulcsával kinyitja az LTC-t védő zárat, egyúttal felfedi a másik láda kulcsát Bélának, aki így megszerzi belezárt a BTC-t. Ily módon, Anna és Béla sikeres cserét hajtottak végre közvetítő nélkül.

Ezzel van egy apró probléma. Mi történjen, ha Anna elküldi a lezárt dobozt, és közben Béla úgy dönt, mégsem szeretne kereskedni. Ebben a helyzetben, mivel Anna nem fér hozzá a BTC-hez, Béla pedig nem fogja befejezni a tranzakció rá eső részét, Anna örökre elveszítené a pénzét. Nos, szerencsére a Bitcoin protokollban van egy technológia, az úgynevezett visszatérítési tranzakciók, így egy idő után, ha a pénzért Béla nem jelentkezik, a BTC Script beépített biztonsági mechanizmusa visszajuttatja azt Annához. Ez volt az első akadály ami a Monero oszthatatlan csere megvalósításának útjába került . A Monero [gyűrűs aláírás technológiája](/knowledge/ring-signatures) miatt egy tranzakció feladója mindig kérdéses. Hogyan hajtson végre a protokoll egy visszatérítési tranzakciót, ha azt sem tudja, kitől származik az eredeti tranzakció?

2017-ben kutatók egy kis csoportja felvázolt egy másik módszert, amellyel az oszthatatlan cserék működhetnének Moneroban. Több évnyi finomítás után a kutatók véglegesítették azt a folyamatot, amellyel a Monero visszatérítési tranzakciók nélkül is képes oszthatatlan cserét bonyolítani a Bitcoinnal.

Mint minden ilyen bonyolultsági fokú dolog esetében, a magyarázatunk szükségszerűen le fog egyszerűsíteni néhány dolgot, hogy az ötletet átadhassuk, de így is a helyét megálló képet ad arról, hogy ez a folyamat milyen mechanizmusok révén működne.

Annának (akinek XMR-je van és BTC-t akar) és Bélának (akinek BTC-je van és XMR-t szeretne) le kell töltenie és futtatnia egy programot, amely támogatja az oszthatatlan cserét. Ez a megvalósítás helyet kaphat pénztárcákban, decentralizált tőzsdéken, vagy speciálisan erre a célra készült programokban, de a szoftvernek támogatnia kell az oszthatatlan csere protokollt. Az első lépésben Anna és Béla kliensei csatlakoznak egymáshoz, majd több közös titkot és kulcsot készítenek. Ebben a lépésben létrejön egy új Monero cím, ahol Annánál van a kulcs egyik fele, Bélánál a másik. Monero egyelőre nincs rajta, így nincs mit elkölteni. Még egy dolog, amit meg kell jegyezni ezzel a címmel kapcsolatban: mindkettőjüknek megvan a tárca megtekintő kulcsa, így mindketten bele tudnak nézni, hogy lássák, megérkezett-e a Monero.

A második lépésben Béla elküldi a BTC-jét egy speciális címre, hasonlóan a Bitcoin oszthatatlan csere protokollhoz, amelyről már beszéltünk. Amikor Anna látja a blokkláncon, hogy a BTC megérkezett erre a címre, elküldi Moneróját arra a címre, amelyhez neki és Bélának is van egy-egy fél kulcsa. Béla ellenőrizheti, hogy a Monero megérkezett, mivel nála is van megtekintő kulcs, majd amikor látja, hogy a Monero rendben megérkezett a tárcába, felfedi Annának a kulcsrészletet, amellyel Anna hozzáfér a Bitcoinhoz. A másik protokollhoz hasonlóan a Bitcoin kivételének folyamata felfedi Béla előtt a Monero kulcs másik felét. Így Bélának a kulcs mindkét fele megvan, elveheti a Monerót, míg Annának csak az egyik fele, aki így nem tudja elvinni előle.

Ha mindezt végigolvasta, és még mindig egy kicsit homályos, hogy a Monero hogyan tudta megkerülni a visszatérítési tranzakciók problémáját, a válasz meglehetősen egyszerű. Mivel magának a Moneronak nincsenek visszatérítési tranzakciói, figyeljük meg, hogy először a Bitcoint küldik el (amelynek vannak visszatérítési tranzakciói), és csak azután kerül küldésre a Monero, hogy a Bitcoin megérkezése megerősítést nyert a blokkláncon. Ez lehetővé teszi a Monero számára, hogy kihasználja a Bitcoin visszatérítési képességét, anélkül, hogy a saját protokolljának támogatnia kellene.

A csere befejeződött, innentől Bélának van néhány lehetősége az újonnan szerzett XMR-rel. Használhatja ezt a Monero pénztárcát úgy, ahogy van, vagy áthelyezheti az XMR-t egy másik birtokában lévő tárcába. Béla nagy valószínűséggel átteszi ezt a Monerót egy másik pénztárcába, mert Annának még mindig megvan a cseréhez használt tárca megtekintő kulcsa, így beleláthat.

A protokoll szépsége abban rejlik, hogy egészen új, bőven tartogat lehetőségeket az optimalizálásra. Az felépítése is meglehetősen rugalmas, így a megvalósítása más pénztárcákban vagy decentralizált tőzsdéken egyszerűnek ígérkezik, és problémamentesen illeszkedve a meglévő architektúrákhoz.

További olvasnivaló

  * [A Monero egyedülálló módon teszi lehetővé a körkörös gazdaságokat](/knowledge/monero-circular-economies/)

  * [A Monero gyűrűs aláírásai kontra CoinJoin, mint a Wasabiban](/knowledge/ring-signatures-vs-coinjoin/)

  * [Miért (és hogyan!) érdemes a kulcsokat saját kézben tartani](/knowledge/hold-your-keys/)

  * [Hozzájárulás a Monerohoz](/knowledge/contributing-to-monero/)

  * [Hogyan befolyásolják a távoli csomópontok a Monero adatbiztonságát](/knowledge/remote-nodes-privacy/)

  * [Hogyan használja a Monero a hard forkokat a hálózat frissítéséhez](/knowledge/network-upgrades/)

  * [Nézetcímkék: Hogyan csökkenti egy byte adat a Monero tárcák szinkronizálási idejét 40+%-kal](/knowledge/view-tags-reduce-monero-sync-time/)

  * [A P2Pool és szerepe a Monerobányászat decentralizálásában](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Mit fog elhozni Moneronak](/knowledge/seraphis-for-monero/)

  * [A Bitcoin Monerora váltása ugyanolyan privát, mint a közvetlen vásárlás?](/knowledge/most-private-way-to-buy-monero/)

  * [Miért bizalommentes a Monero (a Zcash-sel ellentétben)](/knowledge/monero-trustless-setup/)

  * [Miért jobb értékmegőrző a Monero , mint a Bitcoin?](/knowledge/monero-better-store-of-value/)

  * [Hogyan tudja a Monero legyőzni a Bitcoin hálózati hatásait?](/knowledge/network-effect/)

  * [Miért a Monero közösségnek van a legkritikusabb gondolkodása](/knowledge/critical-thinking/)

  * [Átverések, amelyekre figyelni kell a Monero használatakor](/knowledge/monero-scams/)

  * [Amit minden Monero felhasználónak tudnia kell, amikor a hálózatról van szó](/knowledge/monero-networking/)

  * [Hogyan rejti el a RingCT a Monero tranzakciók összegét?](/knowledge/monero-ringct/)

  * [Hogyan védik a Monero rejtett címek a személyazonosságát](/knowledge/monero-stealth-addresses/)

  * [Hogyan akadályozzák meg a Monero alcímek az identitás összekapcsolását](/knowledge/monero-subaddresses/)

  * [Monero kimenetek magyarázata](/knowledge/monero-outputs/)

  * [Monero bevált módszerek kezdőknek](/knowledge/monero-best-practices/)

  * [Hogyan rejtik el a gyűrűs aláírások a Monero kimeneteket](/knowledge/ring-signatures/)

  * [A Monero megoldása a Bitcoint sújtó blokkméret-problémára](/knowledge/dynamic-block-size/)

  * [Hogyan javítja a CLSAG a Monero hatékonyságát](/knowledge/what-is-clsag/)

  * [Miért van a Monero hálózaton utólagos kibocsátás](/knowledge/monero-tail-emission/)

  * [A Monero rövid története](/knowledge/monero-history/)

  * [A Wired Magazin téved a Moneroval kapcsolatban, mégpedig ezért](/knowledge/wired-article-debunked/)

  * [A 15 legnépszerűbb Monero mítosz és kétely, cáfolva](/knowledge/monero-myths-debunked/)

  * [Hogyan rejti el a Dandelion++ a Monero tranzakciók eredetét](/knowledge/monero-dandelion/)

  * [Miért nyílt forráskódú és decentralizált a Monero](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero bányaszat: Mitől olyan különleges a RandomX?](/knowledge/monero-mining-randomx/)

  * [Miért jobb a Monero, mint a Dash, a Zcash, a Zcoin (még Lelantussal is), a Grin és a Bitcoin mixerek, mint a Wasabi (Frissítve 2020 májusában)](/knowledge/why-monero-is-better/)