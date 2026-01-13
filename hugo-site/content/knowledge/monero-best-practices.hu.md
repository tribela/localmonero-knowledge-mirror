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