---
title: "Monero bevált módszerek kezdőknek"
slug: "monero-best-practices"
date: "2020-09-18"
image: "/images/practices.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Sok felhasználó megdöbbenhet, amikor megtudja, hogy a szakértők szerint lehetséges egy kriptovaluta helytelen használata. Attól függően, hogy a felhasználó mi ellen védekezik, bizonyos lépéseket és óvintézkedéseket kell tenni a magánélet megőrzése, csalások elkerülése, valamint a tranzakciók megfelelő és időben történő kézbesítésének biztosítására. Szerencsére a Monero fejlesztői mindent megtettek annak érdekében, hogy ésszerű alapértékeket adjanak meg ezeken a területeken, így a pénztárcát a "gyári" állapotában használó felhasználók is a legtöbb esetben biztonságban lesznek. Ezzel együtt, érdemesnek tartjuk időt szánni arra, hogy megvizsgáljunk néhány olyan esetet, amikor hasznos lehet egy kicsit átgondoltabban költeni.

## JEGYEZZE FEL A SEEDET!

Az első és legfontosabb módja annak, hogy kriptovalutáját biztonságban tartsa, az emlékeztető seed feljegyzése, amely egy rövid szólista, ami akkor jelenik meg, amikor először létrehozza pénztárcáját. Ha megvan ez a seed, és a számítógépe/telefonja elromlik, akkor vissza tudja szerezni Moneroját. Ha nincs meg, és elveszíti a pénztárcáját, akkor a Monero elveszett, és senki sem segíthet visszaszerezni. Ugyanezért ne ossza meg a seedet senkivel. Ha rendelkeznek ezzel a szólistával, akkor teljes hozzáférést és elköltési jogot szereznek Monerojához. Sokan óvatlanok voltak a biztonságukkal, és az elvesztett pénzeszközök félelmetes valóságával kellett szembesülniük, mert valaki kifosztotta őket. Mi azt javasoljuk, hogy írja fel. Fizikailag, papírra. Ne tárolja digitálisan, és gondoskodjon arról, hogy több másolat legyen különböző helyeken. Ez az első számú dolog, amit megtehet biztonsága érdekében. ÍRJA FEL AZ EMLÉKEZTETŐ SEEDJÉT!

## Ellenőrizze a címeit még egyszer

Egyes csalások olyan rosszindulatú programokat használnak a számítógépén, amik megváltoztatják a másolás/beillesztés funkció működését, és a rosszindulatú program létrehozójának címét illesztik be a szándékolt címzett helyett. Mivel a Monero címei hosszúak és nehézkesek, csábító lehet, hogy csak az első néhány számot és betűt ellenőrizzük, és jónak gondoljuk, esetleg egyáltalán nem ellenőrizzük le a címet. Valószínűleg nem szükséges a teljes címet ellenőrizni, legtöbb esetben elegendő a cím első és utolsó tucat karakterének vizsgálata. Olyan címek használatához, amelyekre gyakran küld, sok pénztárca rendelkezik címjegyzék funkcióval, így automatikusan be lehet íratni a kiválasztott címet. Ennek ellenére mindig érdemes egy gyors ellenőrzést végezni.

## Ismerje meg a különbséget a hideg és meleg pénztárcák között

A meleg és hideg pénztárcák elterjedt terminológia a kriptovaluták terén, a koncepció valójában meglehetősen egyszerű. A meleg tárca gyakran kerül elő és van használatban. "Meleg", mert a farzsebben van. A hideg pénztárcák olyanok, amelyekhez nem nyúlunk túl gyakran, a bankban tartott pénzhez hasonlóan. Ahogyan nem tanácsos több száz dollárt a fizikai pénztárcában hordani, de elfogadható egy bankszámlán, a felhasználóknak érdemes megfontolniuk, hogy mennyi Monerot érdemes forró, mobil tárcában tartani, és mennyi az, amit a legjobb otthonhagyni egy második, hidegpénztárcában. Ilyen módon egy telefon elvesztése, egy lopás vagy más baleset nem okoz teljes pénzvesztést.

## Jó választás-e Önnek egy hardveres pénztárca?

Ha megijeszti az ötlet, hogy digitális környezetét teljesen mentesen kell tartania a vírusoktól és más rosszindulatú programoktól, hogy megvédje Moneroját, akkor érdemes lehet hardveres pénztárcát használnia. Alapvetően a hardveres pénztárca lényege, hogy az eszközön tartja a privát kulcsokat, a számítógéptől távol . Tehát még ha számítógépe veszélybe kerül is, a támadó nem férhet hozzá a kulcshoz. Csak akkor tud költeni, ha a hardveres pénztárca csatlakoztatva van a számítógéphez, és aláírja a tranzakciót. Ezzel a mindenre használt, nagy támadási felülettel rendelkező számítógépről a kulcsok biztonsága átkerül a hardveres pénztárcába, ami csak egy dologra használható, és sokkal kisebb a támadási felülete. Azok számára, akik nem ismerik a számítógépes biztonság csínját-bínját, hatékony megoldás lehet pénzeszközeik biztonságban tartására.

## Ha kétségei vannak, használja az alapértelmezett beállításokat (Moneroval)

A magánélet világában gyakran túlságosan könnyű véletlenül kiszivárogtatni vagy felfedni olyan adatokat, amelyek alapján azonosítani lehet minket. Régebbi példa, amely már nem érvényes a Monerora, az egyedi gyűrűméret. Ha az alapértelmezett méret 11, és mindenki 11-et használ, de Ön következetesen 54-et, ugyan ez a szám magasabb, így az anonimitási készlet is nagyobb, de ezzel kitűnik a tömegből, és tranzakciói könnyebben azonosíthatók. A Monero azóta rögzítette a gyűrűméretet 11-re, így minden tranzakció ugyanúgy néz ki.

Más kriptovaluták esetén, például a Bitcoinnál több hibát is elkövethet, amivel véletlenül megsérti a magánéletét. Egy jó hírnevű keverő kiválasztása, beszerzés nem KYC/AML csatornákon , a címek újrafelhasználásának mellőzése és a megfelelő kimenetkezelés mind-mind szükséges ahhoz, hogy minimalizálja a metaadatok kiszivárgásának esélyét. A Monero a legtöbb ilyen problémát megkerüli azáltal, hogy kötelezővé teszi az adatrejtési funkciókat, és előnyös alapértelmezett értékeket állít be az átlagos felhasználók számára. A fenti példa a rögzített gyűrűméret használatával azt jelenti, hogy a végfelhasználóknak nem kell azon gondolkodniuk, hogyan érhetik el a lehető legjobb adatvédelmet. A pénztárca ezt automatikusan elvégzi helyettük.

Furcsának tűnhet erről beszélni. A legtöbb felhasználónak megbocsátható, ha azt gondolja, hogy minden szoftver automatikusan az ő érdekében dolgozik, nem ellene. Sajnos ennél semmi sem állhat távolabb a valóságtól, ami a magánélet védelmét illeti, szinte minden kriptovaluta súlyos hiányosságokkal küzd. Egy átlagos felhasználó számára általában túl sok erőfeszítésbe kerül, hogy elérje a személyes adatainak védelmét. Ez gyakran még más adatvédelmi kriptovaluták esetében is így van! A Monero gondoskodik arról, hogy az adatbiztonság automatikusan érvényesüljön, a felhasználó közreműködése nélkül, ahol lehet, protokollszinten, ahol nem, ott a pénztárcák ésszerű alapértelmezett beállításaival. Ha nem biztos a dolgában, használja a pénztárca alapértelmezett értékeit, és ne habozzon kérdéseket feltenni.

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