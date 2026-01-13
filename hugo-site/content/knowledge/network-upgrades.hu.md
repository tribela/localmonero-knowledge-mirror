---
title: "Hogyan használja a Monero a hard forkokat a hálózat frissítéséhez"
slug: "network-upgrades"
date: "2022-02-10"
image: "/images/upgrades.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero decentralizált, a magánéletet megőrző és biztonságos kriptovaluta felépítésére vonatkozó törekvéseinek a leggyakrabban félreértett része a hard forkok (hálózati frissítések) szerepe.

Ebben a bejegyzésben bemutatjuk, mik azok a hard forkok, miért fontosak Monero számára, és milyen szerepet játszhat bennük a jövőben.

## Miért kell a Moneronak rendszeresen frissítenie a hálózatot?

## Miért kell a Moneronak rendszeresen frissítenie a hálózatot?

A Monero közösség elkötelezte magát amellett, hogy folyamatosan mozgásban tartja és fejleszti a projektet, és úgy tűnik, ez az elhivatottság a közösség szellemiségének két fő aspektusára vezethető vissza:

  1. A Monero projekt végső soron szoftver – kód –, amit emberek írnak. Ez azt jelenti, hogy szükséges esetleges hibákat kijavítani, újonnan felfedezett vagy kitalált fejlesztéseket hozzáadni, a protokollt modernizálni, és általában a projektet karbantartani. Ez sok tekintetben hasonlít az Ön által használt többi szoftverhez (mint a böngésző, amivel ezt olvassa!), amelyeket folyamatosan frissíteni kell az új funkciók hozzáadásához és a hibák kijavításához.

  2. A Monero projekt egy adatvédelmi eszköz, az adatvédelem pedig egy folyamatosan haladó fegyverkezési verseny. Azok az egyének és csoportok, akik semmi mást nem szeretnének, mint mindenkit megfosztani a magánélettől (mind az anyagi, mind a személyes értelemben), folyamatos javításokkal, fejlesztésekkel, és új módszerekkel dolgoznak azon, hogy megtámadják a magánélet védelmének korszerű módszereit, amilyeneket a Monero is használ. Ahogy a magánszféra ellenségei kitalálják ezeket az új megközelítéseket, a Monero hálózatnak képesnek kell lennie arra, hogy alkalmazkodjon és fejlődjön, hogy megvédhesse a pénzügyi magánélethez való jogunkat.

A Monero projekt végső soron szoftver – kód –, amit emberek írnak. Ez azt jelenti, hogy szükséges esetleges hibákat kijavítani, újonnan felfedezett vagy kitalált fejlesztéseket hozzáadni, a protokollt modernizálni, és általában a projektet karbantartani. Ez sok tekintetben hasonlít az Ön által használt többi szoftverhez (mint a böngésző, amivel ezt olvassa!), amelyeket folyamatosan frissíteni kell az új funkciók hozzáadásához és a hibák kijavításához.

A Monero projekt egy adatvédelmi eszköz, az adatvédelem pedig egy folyamatosan haladó fegyverkezési verseny. Azok az egyének és csoportok, akik semmi mást nem szeretnének, mint mindenkit megfosztani a magánélettől (mind az anyagi, mind a személyes értelemben), folyamatos javításokkal, fejlesztésekkel, és új módszerekkel dolgoznak azon, hogy megtámadják a magánélet védelmének korszerű módszereit, amilyeneket a Monero is használ. Ahogy a magánszféra ellenségei kitalálják ezeket az új megközelítéseket, a Monero hálózatnak képesnek kell lennie arra, hogy alkalmazkodjon és fejlődjön, hogy megvédhesse a pénzügyi magánélethez való jogunkat.

## Mit jelent a hard fork?

## Mit jelent a hard fork?

A Monero frissítésének összetettsége akkor kerül felszínre, amikor megérti, miben más egy kriptovaluta frissítése, mint a szoftverfrissítés egy egyszerű alkalmazás, pl. böngésző esetén.

A kriptovalutáknál a hálózat szabályairól (például a tranzakciók felépítése, a bányászat működése és az egyes blokkok ellenőrzésének módja) a teljes hálózatnak meg kell állapodnia, ezt „konszenzusnak” nevezzük. Ha e szabályok bármelyikét módosítani vagy cserélni kell, a csomópontoknak egyetértésben kell lennie az új szabályokról, ami „hard forkhoz” vezet – ez egy olyan helyzet, amikor a hálózat két blokkláncra szakad – az egyik a régi szabályok szerint működik, a másik új szabályokkal.

Amikor a közösség minden tagja egyetért a szabálymódosításokkal, azt „barátságos hard forknak” nevezzük, és a lánc, amelyen még mindig a régi szabályok érvényesek, elhal, nem bányásszák tovább a hard fork után. Ez történt szinte minden Monero hard-fork esetében, és a régi szabályok továbbélése csak akkor fordult elő, amikor más projektek profitálni próbáltak az elágazásból.

Noha a barátságos hard forkok jelentik az egyetlen utat a Monero hálózat egyes elemeinek megfelelő frissítésére, van egy bosszantó mellékhatásuk: a régi szoftverek, amiket a hard fork előtt adtak ki, nem értik a hálózat új szabályait, így nem működőképesek a hard fork után! Ez ahhoz vezethet, hogy a felhasználók azt hiszik, hogy pénzt vesztettek el, mivel úgy látják, hogy a Monero blokklánc megállt, és nem tudnak pénzt mozgatni, amíg nem frissítik pénztárcájukat.

## Ki dönti el, hogy a Monero hálózat mikor vált verziót és milyen feljesztések kerülnek be?

## Ki dönti el, hogy a Monero hálózat mikor vált verziót és milyen feljesztések kerülnek be?

Mivel a Moneronak nincs központi hatósága, vezérigazgatója vagy elnöke, annak eldöntése, hogy mikor lesz frissítve a hálózat, milyen fejlesztések kerülnek be, és hogyan, _ránk_ , azokra az emberekre hárul akik a Monero közösség aktív tagjai! Ez rendkívül fontos része egy decentralizált projektnek, mivel a projekt megtervezése és vezetése végső soron elosztott, közvetlenül a közösségtől ered.

A Monero egyes hálózati frissítéseihez tartozó funkciók tervezése és időzítése két fő helyen történik:

  1. Az IRC-n és a Matrixon, a Monero közösség leggyakrabban használt csevegőplatformjain (amelyek össze vannak kapcsolva). Ezek a platformok nagylétszámú csoportos beszelgetést tesznek lehetővé, itt tartják az összes tervezett Monero közösségi megbeszélést, fejlesztői értekezletet és kutatólaboratóriumi találkozót. Ezek a találkozók a legjobb módja annak, hogy belehallgasson (vagy akár hozzászóljon!) a Monero hálózatfrissítésekkel kapcsolatos tervezéshez és eszmecseréhez.

  2. Githubon, ami a fő kommunikációs platform a hosszabb távú Monero megbeszélésekhez, tervezéshez és szervezéshez. A Monero közösség a Githubot használja találkozók szervezésére, új funkciók és ötletek megvitatására, valamint a hálózati frissítések tervezésének koordinálására amellett, hogy a Monero kódját is tárolja.

Az IRC-n és a Matrixon, a Monero közösség leggyakrabban használt csevegőplatformjain (amelyek össze vannak kapcsolva). Ezek a platformok nagylétszámú csoportos beszelgetést tesznek lehetővé, itt tartják az összes tervezett Monero közösségi megbeszélést, fejlesztői értekezletet és kutatólaboratóriumi találkozót. Ezek a találkozók a legjobb módja annak, hogy belehallgasson (vagy akár hozzászóljon!) a Monero hálózatfrissítésekkel kapcsolatos tervezéshez és eszmecseréhez.

Githubon, ami a fő kommunikációs platform a hosszabb távú Monero megbeszélésekhez, tervezéshez és szervezéshez. A Monero közösség a Githubot használja találkozók szervezésére, új funkciók és ötletek megvitatására, valamint a hálózati frissítések tervezésének koordinálására amellett, hogy a Monero kódját is tárolja.

Ha fontos ötlete van a hálózatfrissítéssel kapcsolatban, vagy egy megközelítés nem tetszik, esetleg aggályai vannak a frissítés időzítésével kapcsolatban, fontos, hogy felszólaljon, és ossza meg érveit a közösséggel!

## Hogyan segíthetek a hálózat frissítésében?

## Hogyan segíthetek a hálózat frissítésében?

Mivel a Monero hálózatfrissítései a szoftverfrissítésekkel együtt közösségi koordinációt és jóváhagyást igényelnek, rendkívül fontos, hogy minél többen vegyék ki részüket a frissítések megtervezésében, tesztelésében és lebonyolításában.

Íme néhány egyszerű módszer, amely a hálózatfrissítéssel kapcsolatos problémák kezelését megkönnyítheti:

  1. Csatlakozzon a [Githubon meghirdetett tervezési értekezletekhez](https://github.com/monero-project/meta/issues), hallgasson bele, és szóljon hozzá, ha valami fontos mondandója akad.
  2. Terjessze a hálózatfrissítés időzítésével kapcsolatos részleteket (miután a döntés megtörtént!) kedvenc tőzsdéjén, pénztárca vagy bányászati közösségében. Nehéznek bizonyulhat minden Monero felhasználót megfelelően értesíteni a frissítésről, ezért fontos, hogy mindannyian segítsünk, ahol tudunk.
  3. Tesztelje le a szoftvert a hálózati frissítés előtt. A hálózati frissítés előtt felhívást tesznek közzé a tesztelőknek, a testneten, és a stageneten is, hogy megbizonyosodjanak arról, hogy a frissítés minden aspektusa megfelelően van megtervezve és implementálva. Minél többen vesznek részt az új verziók alaposan tesztelésében, annál valószínűbb, hogy a hálózatfrissítés zökkenőmentes lesz!
  4. Amikor megjelenik a hálózati frissítéssel ellátott verzió, haladéktalanul frissítsen! Minél többen vannak a friss verzión és állnak készen, annál gördülékenyebben kezeli a hálózat az átállást, és annál kevesebb problémát fognak tapasztalni a felhasználók.

## Mire számíthatok a következő Monero hálózatfrissítéskor?

## Mire számíthatok a következő Monero hálózatfrissítéskor?

Bár még nincs kőbe vésett dátum, hamarosan hálózatfrissítésre kerül sor, amely néhány kulcsfontosságú újítást és funkciót valósít majd meg a Moneroban:

  1. A gyűrű méretének növelése 11-ről 16-ra, növelve az alap anonimitási készletet (értsd: hihető tagadhatóság vagy bázis-adatvédelem) a hálózaton végrehajtott minden tranzakciónál
  2. [Nézetcímkék: zseniális módja annak, hogy 30-40%-kal csökkenjen a pénztárcák szinkronizálási ideje](https://localmonero.co/knowledge/view-tags-reduce-monero-sync-time)
  3. Díjváltozások, a hálózat biztonságának és rugalmasságának javítása a díjpiac gyors változásaival vagy a rosszindulatú szereplők támadásaival szemben
  4. [Bulletproofs+, a Monero-tranzakciók hatékonyságának további javítása](https://www.getmonero.org/2020/12/24/Bulletproofs+-in-Monero.html)

Ezek a változtatások nagyban hozzájárulnak a hálózat adatvédelmének, hatékonyságának és biztonságának növeléséhez, miközben megnyitják az utat a [Seraphis](https://localmonero.co/knowledge/seraphis-for-monero), a Monero következő generációs tranzakciós protokollja előtt.

## Hogyan tudhatok meg többet?

## Hogyan tudhatok meg többet?

A hard-forkok és a hálózati frissítések témája hatalmas, és Moneróban hosszú és legendás története van, ezért érdemes megnézni az alábbi linkeket, ha többet szeretne megtudni a a közelgő hálózati frissítés előzményeiről, folyamatáról vagy tervezéséről! (angol)

  * [Monero v15 hard-fork planning](https://github.com/monero-project/meta/issues/630)
  * [Scheduled software upgrades (in Monero)](https://github.com/monero-project/monero#scheduled-software-upgrades)
  * [A note on scheduled protocol upgrades](https://web.getmonero.org/2020/09/01/note-scheduled-upgrades.html)

További olvasnivaló

  * [A Monero egyedülálló módon teszi lehetővé a körkörös gazdaságokat](/knowledge/monero-circular-economies)/

  * [A Monero gyűrűs aláírásai kontra CoinJoin, mint a Wasabiban](/knowledge/ring-signatures-vs-coinjoin)/

  * [Miért (és hogyan!) érdemes a kulcsokat saját kézben tartani](/knowledge/hold-your-keys)/

  * [Hozzájárulás a Monerohoz](/knowledge/contributing-to-monero)/

  * [Hogyan befolyásolják a távoli csomópontok a Monero adatbiztonságát](/knowledge/remote-nodes-privacy)/

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

  * [Monero bányaszat: Mitől olyan különleges a RandomX?](/knowledge/monero-mining-randomx)/

  * [Miért jobb a Monero, mint a Dash, a Zcash, a Zcoin (még Lelantussal is), a Grin és a Bitcoin mixerek, mint a Wasabi (Frissítve 2020 májusában)](/knowledge/why-monero-is-better)/

További olvasnivaló