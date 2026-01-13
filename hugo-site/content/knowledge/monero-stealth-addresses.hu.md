---
title: "Hogyan védik a Monero rejtett címek a személyazonosságát"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
A Monero háromágú megközelítést alkalmaz az adatbiztonság megvalósítására. Az erre használt technológiák a [gyűrűs aláírások](/knowledge/ring-signatures), amelyek elrejtik a valós kimenetet (a küldőt), a RingCT, amely elrejti az összegeket, és a rejtőzködő címek, amelyek elrejtik a fogadó kilétét. Ma az említettek közül az utolsóról fogunk beszélni: a rejtőzködő címekről.

Sok oka lehet annak, hogy valaki titokban kívánja tartani, hogy kinek küld pénzt. Soha ne hagyjuk meggyőzni magunkat arról, hogy ez minden esetben valamiféle gyanús viselkedés. Az olyan dolgok, mint például egy népszerűtlen politikai pártnak adakozás, jótékonysági szervezeteknek adományozás vagy a kultúrálisan „töröltnek” ítélt szervezetek támogatása, mind olyasmi, amit valaki el akarhat rejteni a következményektől tartva, pedig teljesen legitim tevékenységek.

Egy nyílt blokkláncon mindenki láthatja azokat a címeket, amelyre valaki a tranzakcióit küldi. Fontos figyelembe venni, hogy ha maguk a bányászok nem értenek egyet azzal, hová megy a pénz, akkor dönthetnek úgy, hogy nem bányásszák blokkba, így hatásában cenzúrázva ezt a tranzakciót egy elvileg cenzúraálló platformon. Az egyetlen módja annak, hogy ez a – igaz, valószínűtlen – cenzúra ne legyen lehetséges, ha a bányászok nem tudnak különbséget tenni a tranzakciók között, mivel az összes láncon belüli metaadat el van rejtve különféle eszközökkel. Ez olyasmi, amiről Monero nevezetes.

A Monero az átlátszó címek problémáját a rejtőzködő címek megvalósításával oldja meg, egy olyan technológiával, amelyet eredetileg a bitcoinhoz készített 2011-ben a Bitcoin Talk fórum egy felhasználója, ByteCoin (hogy van-e köze a Bytecoinhoz, amely később ezt integrálta, nem tudjuk). A rejtett címek jelenlegi formája azonban számos fejlesztést tartalmaz az eredeti elképzeléshez képest. De először is, hogy lássuk, hogyan működnek, beszélnünk kell a kulcsokról.

Nehéz a kriptovaluták közelében lenni, és soha nem hallani kulcsokról. Gyakoriak az olyan mondások, mint hogy „készítsen biztonsági másolatot a privát kulcsáról”, ennek ellenére amikor egy átlagember meghallja a „nyilvános kulcs” és a „privát kulcs” kifejezéseket, gyakran megijed, és úgy hiszi, hogy ez túlságosan szakmai és összetett ahhoz, hogy megértse. Aggodalomra semmi ok. Lassan fogunk haladni, és rengeteg példát használunk majd.

A kriptográfiában használt kétféle kulcs, amint az imént említettük, a nyilvános és a privát. Ez a két kulcs általában párban van, ami azt jelenti, hogy egy adott nyilvános és privát kulcs összetartozik. Általában a nyilvános kulcs a privát kulcsból származtatott, ami azt jelenti, hogy a privát kulcs ismeretében a pénztárcája rafinált matematikia műveletek segítségével bármikor eló tudja állítani a megfelelő nyilvános kulcsot.

Tehát, ahogy a nevek is sugallják, a nyilvános kulcs probléma nélkül nyilvánoságra hozható. Általában része a címnek, amit tranzakciók fogadásához megoszt. Ugyanígy, nevének megfelelően a privát kulcs olyan, amit nem szabad megosztani a világgal. Ez teszi lehetővé tranzakciók aláírását és elköltését, tehát ha ellopják, akkor egy alávaló harmadik fél el tudja küldeni a pénzét, általában saját magának.

Ennek egyszerű analógiája egy lakat és a nyíitásához szükséges kulcs. A nyitott lakat szabadon megosztható, és bármit le lehet zárni ezzel a lakattal, de csak a kulccsal rendelkező személy fér hozzá bármihez, ami a lakattal le vanzárva. A lakat másolható és megosztható, a kulccsal ne tegyen ilyet.

Ezek a kulcsok általában el vannak rejtve a felhasználó elől, így nem találkozik velük igazán. A Monero esetén egyáltalán nem jelennek meg félelmetes alfanumerikus karakterláncként. Az átlagos Monero felhasználó az emlékeztető seedjeként ismeri a privát kulcsát. A seed (amelyet jegyezzen fel, ha még nem tette volna meg), valójában csak a privát kulcs egy ember által olvasható formája. 

Ugye, nem is olyan ijesztő. Térjünk vissza a rejtőzködő címekhez.

Ahogy korábban említettük, a rejtőzködő címeket eredetileg nem Monerohoz, hanem Bitcoinhoz tervezték. Mint a legtöbb újkeletű ötletnél, első iterációban itt is voltak problémák. A következő próbálkozás az volt, amikor Nicholas van Saberhagan megalkotta a CryptoNote-ot a Bytecoin számára, ami a Monero előfutára ([lásd a Monero és a Bytecoin történetét itt](/knowledge/monero-history)), és bár ez határozott előrelépés volt az eredetihez képest, maradt néhány lappangó probléma.

Végül a legutolsó iteráció egy másik, már megszűnt, adatvédelmi kriptovalutához jött létre, amelynek sikerólt megoldani az ötlettel kapcsolatos fennmaradó adatbiztonsági problémákat. Ez a megoldás került be a Moneroba, és ezt használjuk a mai napig.

Bár az adatvédelmi és biztonsági problémák megoldódtak, maguk a rejtett címek egy új sajátosságot adtak a blokklánc-technológiához, ami eddig nem létezett. A pásztázás követelményét. Mivel a fogadó címe nem jelenik meg nyilvánosan a blokkláncon, a fogadó nem tudhatja, hogy egy adott tranzakció hozzá tartozik-e, ezért minden bejövő tranzakciót meg kell vizsgálnia a privát kulcsával, hogy megtudja, az övé-e.

A nyílt láncoknál mindössze annyit kell tenni, hogy megnézzük, a tranzakció a címünkre érkezik-e. Egyszerű igen-nem kérdés. A rejtőzködő címekkel azonban bármelyik tranzakció lehet nekünk címezve, ezért mindegyiket meg kell próbálni a privát kulccsal feloldani, hogy kiderüljön, megnyílik-e.

Ez egy további lépés, amit a Bitcoinnak és leszármazottainak nem kell megtenni, amely a pénztárca kezdeti beállítását, és szinkronizálását – ha sokáig nem nyitotta ki – jelentősen meghosszabbítja ezekhez képest. Ez az ára azonban az adatbiztonsági garanciáknak. Meg kell jegyeznünk, hogy az adatvédelmi mesterhármas leggyengébb pontjával – a gyűrűs aláírásokkal – ellentétben a rejtőzködő címek nem érzékenyek a heurisztikai támadásokra. A jól bevált elliptikus görbe alapú kriptográfiára támaszkodik, amelyre az egész internet is, így ennek feltörése a számítógépes biztonság általános végét jelentené, nem csak a Moneroét.

További olvasnivaló