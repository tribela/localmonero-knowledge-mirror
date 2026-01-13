---
title: "Hogyan rejtik el a gyűrűs aláírások a Monero kimeneteket"
slug: "ring-signatures"
date: "2020-09-08"
image: "/images/rings.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
A Monero messze földön ismeretes a kriptográfia világában, mint az adatvédelmi kriptok királya. Bár mindenki tudja, hogy a Monero kiváló adatbiztonságot kínál, sokan nem értik, hogyan működik ez.

Sok más adatvédelmi valuta összehasonlító táblázatos infografikákat tesz közzé, amely felsorolja az egyes láncok adatvédelmi technológiáinak nevét, és a legtöbb esetben a Monero technológiáját RingCT-ként jelölik meg, pedig ez csak az igazság egy része. A Monero valójában háromágú megközelítést alkalmaz. Egy technológia a tranzakció címzettjének elrejtésére, egy az elküldött összegek elrejtésére, a harmadik pedig a felhasznált kimenet elrejtésére: ezek a rejtőzködő címek, a RingCT és a gyűrűs aláírások.

Ez a három részből álló megközelítés azt jelenti, hogy ha az egyik technológia hibás is, a többiek nem feltétlenül osztoznak ebben. A gyűrűs aláírások a leggyengébb láncszeme az adatvédelmi rendszernek; a gyenge itt azt jelenti, hogy ez a legérzékenyebb a heurisztikus támadásokra. Szánjunk egy kis időt ezek felfedezésére, rendben?

Amint fentebb említettük, a gyűrűs aláírások célja, hogy elrejtsék a tranzakció során használt kimenetet. Ha a kriptovaluták „bemenet/kimenet” terminológiája zavaros az Ön számára, ne aggódjon. Valójában nem olyan bonyolult. Amikor meghallja az „output” (kimenet) szót, gondoljon egy csekkre. Ez egy, már nem túl gyakori, fizetésre használt eszköz. A csekkhez hasonlóan tetszőleges összeget meg lehet adni – 10 USD; 32,50 USD; stb. –, ez cserél gazdát a tranzakcióban részt vevő felek közt. A kriptovaluták esetében a kimenetek szolgálják ezt a funkciót .

Ha valaki 10 Monerot fizet önnek, egy 10 XMR értékű kimenetet fog kapni tőle. Ennek a kimenetnek van egy értéke (10), és ez az, amit a küldő pénztárcájából kikerül, ugyanúgy, mint amikor egy szolgáltatásért fizetve egy bankjegy elhagyja a fizikai pénztárcáját, és ahhoz kerül át, akitől vásárol.

A kimenet elrejtésének módja az elterelő kimenetek gyűrűjének (innen a neve) felépítése. De ezek nem egyszerűen hamisított kimenetek. Ezek a blokklánc valós múltbeli kimenetei, amelyeknek semmi közük a jelenlegi tranzakcióhoz, de egy külső szemlélő számára mindegyik kimenet ugyanolyan valósnak tűnhet, mint a tényleges. A terelőkimenetek halmazának méretét az igazit beleszámítva gyűrűméretnek hívják, ez jelenleg a Moneronál tizenegy. Tehát tíz álcázó kimenet minden igazihoz.

Miért nem növeljük meg ezt a számot 100-ra vagy akár 1000-re? Minél több, annál jobb, igaz? Nos, az adatvédelem szempontjából igen, de más tényezőket is figyelembe kell venni. Térjünk vissza a fizikai példához, hogy lássuk, miről van szó. Ha el akarja rejteni az egydolláros bankjegyét tíz hamis közé, nagyjából tizenegy dollárt kell cipelnie a pénztárcájában minden egyes elkölteni kívánt dollár után. Egy valódi bankó, tíz álca. Ez máris elég körülményessé válik, akkor is, ha csak néhány dollárt akar elkölteni. Képzelje el, hogy 1000-re növeljük az álbankjegyek számát. Minden egyes dollár után, amit el akar költeni, 1001 dollárt kellene hurcolni. Egy aktatáskát kéne magával cipelnie, hogy egy cukorkát vásároljon! Fontos megjegyezni, hogy a gyűrűs aláírások nem egészen így működnek, például a további kimenetek nem részei az aláírásnak, csak a hivatkozások rájuk, de reméljük, hogy ez a hasonlat segít az alapfogalmak elképzelésében.

A blokklánc terelőkimenetei hasonlóan működnek. Minden hozzáadott álcakimenet növeli a tranzakció ellenőrzésének idejét és költségét. Minden csomópontnak le kell töltenie a teljes gyűrűt minden egyes tranzakcióhoz, és minden gyűrűaláírás tartalmazza a valódi kimenetet, és az álcákat is. Nem merül ki ennyiben, hanem matematikailag igazolni is kell, hogy legalább az egyik kimenet valódi, a biztonyítási idő pedig a gyűrű méretével arányosan növekszik. Ez azt jelenti, hogy meg kell találnunk az arany középutat, ahol a gyűrűméret kellően nagy ahhoz, hogy megfelelően elrejtse a valódi kimenetet, még heurisztikus támadások ellen is, de megfelelően kicsi, hogy ne okozza a blokklánc masszív felfújódását. Nem elég hasraütésre egy számot kiválasztani, vagy a gyűrűméretet növelni, amikor az aláírás mérete csökken (mint a CLSAG bevezetésénél). A Monero közösség konkrét, matematikai bizonyítékokat szeretne arra vonatkozóan, hogy melyik gyűrűméret kínálja a legmegfelelőbb kompromisszumot. Válasszunk egy túl alacsony számot, és az adatbiztonság nem lesz elég erős a heurisztikus támadások ellen. Ha túl nagy, előfordulhat, hogy csak elenyésző előnyöket kapunk az adatvédelem terén, szükségtelen méretezési problémákért cserébe.

Az utolsó dolog, amit meg kell említenünk: Némelyik Monerot tárgyaló írás egyszerűsít, és azt állítja, hogy a gyűrűs aláírások a feladót rejtik el, de ez így nem teljesen igaz, és ez nem csak szőrszálhasogatás. A feladó (ember) és a kimenet (bankjegy) között nagy különbség van a magánélet tekintetében. Ugyan az egyes kimenet kötődik a feladójához, maga a kimenet nem azonos a feladóval. Tehát ha egy gyűrűs aláírást meg is törnek, az nem feltétlenül kapcsolódik személyazonossághoz, illetve az összeg és a címzett is rejtve marad, így minimálisra csökkentve a felek adatvédelmében történt kárt.

Ez nem jelenti azt, hogy a gyűrűs aláírások feltörése jelentéktelen. Minden metaadat-szivárgás baj, és több információt fedhet fel, mint elsőre gondolnánk, különösen más metaadatokkal együtt használva. Ezért minden tőlünk telhetőt megteszünk annak érdekében, hogy a választott gyűrűméret mögött akadémiai szigor legyen, az egyéb metaadatok szivárgását elkerüljük, és a felhasználói élmény alapértelmezés szerint a legbiztosabb választást kínálja.

Ha az aláírások feltörésének valószínűsége továbbra is aggasztja, nagyszerű híreink vannak. A következő generációs adatvédelmi protokollok, amelyek fejlesztés alatt vannak, mint a Triptych, az Arcturus, és a Lelantus, nagyon elegáns képességekkel rendelkeznek. Ezekben a protokollokban a helyfoglalás a gyűrűmérettel logaritmikusan skálázódik, nem lineárisan. Ez azt jelenti, hogy 100 álcázó kimenet elfér akkora helyen, ami korábban 10-hez kellett. Ez nagy különbség, ami jelentősen javítja az adatbiztonságot mindenütt.

A macska-egér játékban, ami az adatvédelem, a Monero folyamatosan fejleszti a megoldásait, hogy az élen maradhasson, mindenki számára a legjobb gyakorlati adatbiztonságot garantálva.

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

  * [Hogyan működnek az oszthatatlan cserék Moneroban](/knowledge/monero-atomic-swaps/)

  * [Amit minden Monero felhasználónak tudnia kell, amikor a hálózatról van szó](/knowledge/monero-networking/)

  * [Hogyan rejti el a RingCT a Monero tranzakciók összegét?](/knowledge/monero-ringct/)

  * [Hogyan védik a Monero rejtett címek a személyazonosságát](/knowledge/monero-stealth-addresses/)

  * [Hogyan akadályozzák meg a Monero alcímek az identitás összekapcsolását](/knowledge/monero-subaddresses/)

  * [Monero kimenetek magyarázata](/knowledge/monero-outputs/)

  * [Monero bevált módszerek kezdőknek](/knowledge/monero-best-practices/)

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