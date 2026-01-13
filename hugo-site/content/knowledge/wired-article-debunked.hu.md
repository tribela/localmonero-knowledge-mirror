---
title: "A Wired Magazin téved a Moneroval kapcsolatban, mégpedig ezért"
slug: "wired-article-debunked"
date: "2020-06-24"
image: "/images/wired.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Mind az adatvédelem, mind a kriptovaluták világában gyakori a félretájékoztatás. Közzétettünk [ egy írást, amely tizenöt gyakran felmerülő helytelen vagy elavult feltételezést vázol fel a Moneroval kapcsolatban](/knowledge/monero-myths-debunked), de most szeretnénk időt szakítani egy konkrét cikkre is, amelyet a Monero-szkeptikusok előszeretettel idéznek és terjesztenek.

A Wired nevű kiadvány 2018. március 27-én közzétett [egy cikket](https://www.wired.com/story/monero-privacy/), amely maga is egy másik, akadémikusok által kiadott friss tanulmányra válaszul íródott: „A Monero blokklánc nyomon követhetőségének empirikus elemzése ”.

Noha a dolgozat társszerzői olyan személyek, akiknek egyértelmű összeférhetetlensége van (értsd: tanácsadói a Zcash projektnek és részesedéssel rendelkeznek benne), a Monero közösség mérsékelten jól fogadta a tanulmányt, mivel megerősített olyan dolgokat, amelyeket a közösség régóta tudott és a Monero Kutatólabor (Monero Research Lab) (az [MRL-0001](https://web.getmonero.org/resources/research-lab/pubs/MRL-0001.pdf) és [MRL-0004](https://web.getmonero.org/resources/research-lab/pubs/MRL-0004.pdf) tanulmányaiban, amelyek közül a legkorábbi négy éve jelent meg) már publikált. Ugyanakkor több dolgot is kifogásoltak, elsősorban az összeférhetetlenséget, vagy hogy ezek a problémák már ismertek, megvitatottak és – esetenként – már megoldottak, valamint a Monero akkori adatvédelmi garanciáinak durva félreismertetése. A közösség a mű előnyomatát véleményzete, több javaslatuk végül bekerült a kész dolgozatba.

De pontosan mi is volt megtévesztő? Elhallgatták a tényt, hogy az említett hiányosságok a Moneroban már több mint egy éve nem voltak jelen. A 2017 előtti tranzakciók valóban ki voltak téve adatszivárgás veszélyének, de a közzététel időpontjában a Monero már javította a legtöbb problélmát. Legyünk igazságosak a szerzőkkel, néhol említést tettek arról, hogy a Monero orvosolta a problémákat, de közel nem elég hangsúlyosan ahhoz, hogy befolyásolják a cikk akkori hatását a kriptovaluta-médiára. Innen a Wired cikk.

Bár a kérdéses Wired-cikket vizsgálhatnánk korhű darabként, hogy mennyire állta meg a helyét akkoriban, a helyzet az, hogy a mai napig megosztásra kerül a Monero gyengeségeit alátámasztandó, ezért érdemes megnézni, mennyire állta ki az idő próbáját. Örömmel teszünk eleget ennek a meghívásnak.

A cikket gyorsan átfutva is számos szenzációtkeltő sort veszünk észer, például: „[A megállapítások] nem csak akkor adnak okot aggodalomra , ha valaki ma szeretne titokban Monerót költeni”, továbbá a cikk teljes hangvétele olyan, mintha a kutatás új lenne, nagyrészt a tanulmányra alapozva. Maga az akadémiai dolgozat is tartalmaz ajánlásokat, mint a Monero-felhasználók figyelmeztetése, hogy névtelenségük esetleg sérülhet, annak ellenére, hogy ezek a beszélgetések nemcsak hogy 2014 óta zajlanak, hanem a közösség ajánlása végig az volt, hogy az emberek ne vegyenek Monerot, amíg az kísérleti fázisban van.

Mi a helyzet magával a kritikával? A valóság az, hogy a Moneroval mint lenyomozhatatlan pénzzel kapcsolatos számos probléma vagy már nem igaz a Monero-ra, vagy egységesen jellemző az összes adatvédelem-központú blokklánc-alapú kriptovalutára. Nézzük meg ezeket.

Az egyik leggyakrabban felhozott bírálat Moneroval szemben az, hogy a blokklánc állandósága és megváltoztathatatlansága miatt ha egy jövőbeli technológia bármikor megtörné a védelmet, Monero összes múltbeli tranzakciója nyilvánossá válna. Más szóval, a magánéleti garanciáknak korlátozott szavatossága van.

Nem tudjuk eléggé kihangsúlyozni: Szó szerint minden adatvédelmi kriptopénz, amelyik a láncon belüli technikákat alkalmaz a zavarásra és a privátszféra fenntartására, ki van téve ennek a sebezhetőségnek, mégis gyakran használják Monero ellenében (ironikus módon gyakran a problémában osztozó versenytársakkal összevetésben), így ebben a cikkben is. Az erre a kritikára adott válasz meglepő lehet egyesek számára, de lehetséges, hogy a Monero valójában kevésbé sérülékeny, mint a többi privát kriptopénz, mivel sokrétű megközelítést használ az adatvédelemre.

A Monero elrejti a kimeneteket (feladókat), az összegeket, és a fogadókat is, három különböző technológia használatával: gyűrűs aláírássokkal, RingCT-vel és a rejtett címekkel. Ezek közül a gyűrűs aláírások a leggyengébbek, és a leginkább érzékenyek mind a ma létező heurisztikákra, mind az lehetséges jövőbeli titoktörő technológiákra. A a Monero közösség ezzel évek óta tisztában van, és aktív kutatásokat folytat a gyűrűs aláírási rendszer tökéletesítésére vagy teljes cseréjére.

Azonban még ha a gyűrűs aláírásokat teljesen feltörik, csak a valós kimenetre derül fény, a feladó személyére NEM. Egy kimenet személyes identitáshoz kapcsolása nem lehetetlen, de további metaadatokra és erőforrásokra van hozzá szükség. Az a tény, hogy a RingCT és a rejtett címek védelme NEM sérül , még tovább enyhíti a hatást.

Megjegyzendő, hogy a Wired cikk futólag említést tesz a fentiekről abban a részben, ahol Riccardo „fluffypony” Spagni a megkeresükre adott válaszait tárgyalják, de az erre szánt idő rövid, és szinte a szőnyeg alá söpri ezt a fontos információt. A megértés hiánya különösen szembetűnő, amikor a cikket meggondolatlanul megosztogató emberekkel próbáljuk megvitatni ezeket a kérdéseket.

Egy másik kritika, amelyre sokkal nehezebb választ adni, az a külvilág álláspontja a Moneroval kapcsolatban, és ennek kapcsolata ahhoz, ahogyan a Monero közösség látja azt. Az olvasónak nem kell messzebbre mennie ennek illusztrációjáért, mint magának a cikknek a címe: „A Darknet kedvenc pénze kevésbé lenyomozhatatlan, mint amilyennek látszik”.

Bárki, aki jelentős időt tölt a Monero közösségben, tanúsíthatja, hogy a Monero közösség igyekszik mindent megtenni azért, hogy megmutassa, milyen nehéz a tényleges titoktartást megvalósítani, még a marketing- és terjesztési erőfeszítések rovására is. Mivel a közösség bőséges alapanyagot biztosít a hiányosságok alapos megvitatásához, egy ponton túl a tudatlanság már a felhasználó hibája, ha úgy gondolja, hogy a Monero az egyetlen dolog, ami a 100%-os adatbiztonsághoz szükséges.

Eddigre nyilvánvalónak kell lennie, hogy a Monero közösség komolyan veszi a magánélet védelmét, és az ezzel kapcsolatos gyengeségekkel illetve ezek megoldási lehetőségeivel kapcsolatos őszinteségét. A szóban forgó cikkek és a hozzá hasonlók tökéletesen figyelmen kívül hagyják a Monero innovatív szellemiségét. A Monerot olyan kriptovaluták hordáihoz hasonlítja, amelyek hangzatos ígéreteket tesznek, a pénzügyi haszonra és tapasztalatlan befektető-palánták pénzére utazva .

Mi sem állhatna távolabb a valóságtól. A Monero nagyon is tisztában van gyengeségeivel, fáradhatatlanul igyekszik folytatni az építkezést, hogy a hibákat kijavítsa, a laza csavarokat meghúzza, és elérje azt a nagyon is valós, de nagyon nehéz célt, hogy a világnak egy privát, helyettesíthető egységekből álló kriptovalutát adjon, amit bárki használhat, mindezt igazságos, decentralizált, és közösség által meghatározott módon. Talán itt az ideje, hogy félretegyük a szenzációhajhászást és a versenytársakat népszerűsítő cikkek megosztását. Tán itt az idő, hogy másféle történetet meséljünk.

További olvasnivaló