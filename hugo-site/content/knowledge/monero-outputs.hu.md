---
title: "Monero kimenetek magyarázata"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
A Monero más kriptovalutákhoz hasonlóan kimeneteket használ a pénzeszközök elszámolására. Sok kriptoban jártas felhasználó valószínűleg hallotta már ezt a kifejezést, de nem mindenki érti, mit jelent és hogyan működik. A [gyűrűs aláírásokról szóló cikkünkben](/knowledge/ring-signatures) leírtaknak megfelelően, a kimenetek a blokkláncon lévő tényleges egységek, amik a tranzakcióban részt vevő felek között gazdát cserélnek. Hasonlít az egydolláros bankjegyekhez, de itt a címlet nem fix összeg .

Ha 16 dollárt kap munkájáért, kaphat például egy egydollárost, egy ötdollárost és egy tízdollárost. 16 dollárja van, és három különböző bankjegy is van a pénztárcájában. Ha valakinek 6 dollárt fizetne, használhatja az 5-ös és az 1-es bankjegyet, de ha valakinek 8 dollárt akar fizetni, akkor csak a 10 dollárost tudja használni, és 2 dollárt kap vissza váltópénzként. Végül, ha 14 dollárt szeretne fizetni valakinek, mindhárom bankjegyet fel kell használnia, és 2 dollárt kap vissza, de egy pillanatig, amikor mindhárom bankjegyet átadta, nincs pénz a tárcájában, amíg meg nem kapja a visszajárót.

A Monero hasonlóan működik. Tegyük fel, hogy egy boltot üzemeltet, és három különböző terméket adott el. Kapott értük 1.5 XMR-t, 2.25 XMR-t és 5.25 XMR-t összesen 9 XMR értékben, de három másik kimenet is van a pénztárcájában a korábban említett címletekből. Csakúgy, mint a dollárnál, valakinek tervezhet 3 XMR-t fizetni. Használhatja csak az 5.25 XMR kimenetet, és 2.25 XMR-t kap vissza, vagy kombinálhatja az 1.5 és 2.25 XMR kimeneteket, így 0.75 XMR-t kapva vissza.

De amint elküldi a tranzakciót, a használt kimenetek „zárolt” állapotba kerülnek, ami azt jelenti, hogy nem érhetők el, amíg nem kapja meg a visszajárót. A protokoll 10 megerősítés után, azaz körülbelül 20 perc múlva oldja fel a pénzeszközöket (folyósítja a visszajárót). Csakúgy, mint amikor átadja a dolláros bankjegyeket a pénztárcájából, addig nem használhatja fel újra őket, amíg vissza nem kapja a különbözetet a pénztárostól, ugyanígy a Monerojához addig nem tud hozzáférni, amíg vissza nem kapja a váltópénzt.

Térjünk vissza ahhoz a példához, amikor 3 XMR-t küldünk valakinek, és az 5.25 XMR kimenetet használjuk. Most, amíg várja az 1.75 XMR váltópénzt, nem tudja azt használni. 1.75 XMR nem érhető el az Ön számára. De továbbra is használhatja az 1.5 XMR és 2.25 XMR kimeneteit, mivel ezek nincsenek elköltve. Visszatérve a dolláros példához, ha fizet valakinek 8 dollárt, mint az előző példában, akkor nem használhatja fel azt a 2 dollárt, amelyet váltásként vár vissza, amíg azt nem kapja meg, de még mindig van egy kihasználatlan 5 dolláros bankjegy a pénztárcájában. Ezzel továbbra is megvásárolhat bármit, amit csak szeretne, amíg a visszajárót várja. Ugyanígy működik a Monero is.

Ez gyakran összezavarja az új Monero-felhasználókat. Előfordul, hogy a felhasználónak csak egy kimenete van a pénztárcájában, amelyet egy tőzsdéről vagy egy barátjától kapott. Tegyük fel, hogy ez a kimenet 20 XMR értékű. Más kimenet nincs a pénztárcában. Szeretne a két kedvenc jótékonysági szervezetének adományozni. 5 XMR-t küld az első szervezetnek, majd értetlenül áll, mert hiába kellett volna 15 XMR-nek megmaradnia, nem tudja azonnal elküldeni a következő adományt a második jótékonysági szervezetnek. Amint azt sejtheti, ez azért van, mert a 15 XMR még zárolva van. Nem költhető el mindaddig, amíg a visszajáró meg nem érkezik (10 megerősítés vagyis körülbelül 20 perc múlva). A pénzeszközök feloldása után el tudja küldeni a második adományt.

Megismételve a lényeget: ez nem lett volna probléma, ha több kimenettel is rendelkezett volna, például két 10 XMR értékűvel, vagy hasonlóval. Mindkét adományt el tudta volna küldeni, mert az első adomány a 10 XMR-es kimenetek egyikét használja fel (és vár 10 megerősítést, hogy 5 XMR-t visszakapjon), a második adomány pedig a másik 10-es kimenetet használná.

Egyes kriptovaluta tárcák rendelkeznek egy „kimenetkezelés” nevű funkcióval, amely megmutatja a felhasználónak, hogy jelenleg milyen kimenetekkel rendelkeznek (a teljes összegen felül), valamint lehetővé teszi számukra, hogy megválasszák, melyiket kívánják használni, amikor költenek.

Jelenleg a Monero grafikus felület automatikusan választja ki a kimenetet a felhasználók számára, mivel a saját kimeneteik megválasztása gyakran problémát okoz, vagy egyes esetekben ronthatja a magánéletet. Vannak azonban olyan fejlesztés alatt álló pénztárcák, például a Feather projekt, amelyek támogatni fogják ezeket a kimenetkezelési funkciókat.

Sokat beszéltünk a küldő részéről, de valami lenyűgöző történik a fogadó oldalon is. Visszatérve a példánkra, amikor 3 XMR-t küld valakinek, az 1.5 XMR és 2.25 XMR kimeneteit használva a tranzakcióban (miközben 0.75 XMR visszajáróra számít), a fogadó NEM két kimenetet kap 1.5 XMR értékben. Helyette EGY 3 XMR értékű kimenetet fogad.

A háttérben a protokoll egyesíti a kiadáshoz használt összes kimenetet, és a fogadónak egy kimenetet ad a befizetett összegből, és egy váltókimenetet küld vissza a feladónak. Így a feladó is egy kimenetet kap visszajáróként, függetlenül attól, hogy kettő, három, vagy tíz kimenetet használt a tranzakció elküldéséhez.

Reméljük, hogy ezzel sikerült tisztáznunk néhány félreértést a kimenetekkel és a protokoll belső elszámolásának működésével kapcsolatban, valamint megmagyarázni azt a gyakori problémát, amikor a felhasználók zárolt pénzeszközökkel találkoznak. Egy másik cikkben megvizsgáljuk azt is, hogyan érdemes a kimeneteket kezelni annak érdekében, hogy minimálisra csökkentsük annak esélyét, hogy a jövőbeni tranzakciók elküldése előtt várni kelljen a feloldott pénzeszközökre.

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