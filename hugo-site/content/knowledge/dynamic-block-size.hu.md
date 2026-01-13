---
title: "A Monero megoldása a Bitcoint sújtó blokkméret-problémára"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Megjegyzés:** Erősen javasoljuk, hogy olvassa el a [„Miért van a Monero hálózaton utólagos kibocsátás?”](/knowledge/monero-tail-emission) és a [ „Monero bányaszat: Mitől olyan különleges a RandomX?” című cikkeinket.](/knowledge/monero-mining-randomx). Ez az írás az ott bemutatottakra épít._

Blokklánccal kapcsolatos problémákról disurálva, az egyik legelőször felbukkanó kifejezés a „skálázhatóság” lesz. Senki előtt nem titok, hogy a blokkláncok nem skálázódnak jól, de a legtöbben nem értik, miért.

Az igazság az, hogy ez valójában egy gyűjtőfogalom, amely két különböző kategóriát takar: protokoll áltl biztosított támogatás és technológiai támogatás egy adott időpontban. Ebben a cikkben az egyikre összpontosítjuk figyelmünket: a protokolltámogatás alapvetően annak mértéke, hogy a protokoll hány tranzakciót tud kezelni adott idő alatt.

A bitcoin blokkmérete korlátozott, ami azt jelenti, hogy amint elegendő tranzakció kerül egy blokkba, minden további tranzakciónak sorban kell állnia, hogy a következő blokkba kerülhessen. Megfelelő hasonlat lehet egy vonatra gondolni. A vonat beáll az állomásra, és a sorban állók elkezdenek felszállni. Ha a vonat megtelt, annak, aki kint maradt, meg kell várnia a következőt.

A Bitcoin a díjakat használja annak meghatározására, hogy ki kerül be egy blokkba. Visszaugorva a vonatos hasonlathoz, elképzelhető, hogy egy potenciális utas, aki éppen lemaradna, öt dollárt kínál a kalauznak, hogy helyet adjon neki. A többi utas követi a példát, végül árverés indul, hogy ki melyik helyet kapja. A kalauznak kell eldöntenie, hogy az érkezési sorrendet érvényesíti-e, de anyagi érdeke az, hogy a bevételét maximalizálja azáltal, hogy a legmagasabb ajánlatot tevőket veszi fel a fedélzetre.

Ebben a hasonlatban a bányászok felelnek meg a kalauznak. Tetszőleges tranzakciót beépíthetnek a blokkba, de általában azokat választják, amelyekért a legmagasabb díjakat fizetik.

Ugyanígy, ha a blokkok nincsenek tele, az embereknek nincs okuk arra, hogy magas díjat fizessenek, mert rengeteg szabad hely marad.

A 2017-es kriptovaluta-fellendülés csúcsán a Bitcoint elárasztották a tranzakciók, és a díjak az egekbe szöktek azoknak, akik a következőbe, vagy bármely közeljövőben esedékes blokkba akartak bekerülni. Akik nem voltak hajlandók magas díjat fizetni, azt tapasztalták, hogy tranzakcióik órákat, napokat várnak, vagy akár teljesen kikerülnek a sorból.

Ez egy megrázó betekintést nyújtott abba, hogy mi történne a Bitcoinnal, ha eljönne a gyakran emlegetett „tömeges elfogadás”. Ha a Bitcoint tömegek használnák, a dolgok még rosszabbul állnának, mint 2017-ben, a Bitcoinhoz a gazdagokon kívül senki sem férne hozzá, egyszerűen azért, mert a fix blokkméret miatt kicsi az áteresztőképesség, ezért a díjpiac dominál. .

A Monero előre látta ezt, és más megoldást keresett. Ezért a Monero fejlesztői dinamikus blokkméretet valósítottak meg.

A Monero blokkméretének is van határa, de ez egy képlékeny limit. Ha a várakozó tranzakciók sora túl hosszúra nyúlik, a bányászok megnövelhetik a blokkok méretét. Vonatos hasonlatunkkal, lehetséges több vasúti kocsit csatolni a szerelvényhez, hogy elférjenek a további utasok. Miután a sor kiürült, a blokkok visszatérnek eredeti méretükhöz.

Ha ez jó ötletnek tűnik, felmerülhet a kérdés, hogy miért a Monero az egyetlen kriptovaluta, amely ezt megvalósította. Miért nem valósítja meg a Bitcoin, hogy véget vessen az áteresztőképességi problémáknak?

Sajnos ez nem lehetséges. Ennek több oka is van, megpróbáljuk a lehető legjobban elmagyarázni.

A bányászoknak mindig az az érdeke, hogy a blokkok nagyok legyenek. A nagy blokkokba több tranzakció fér bele, így több pénzt kereshetnek a díjakból és a blokkjutalomból. Ez spamhez vezethet, amikor valaki sok kis tranzakciót küld alacsony díjakkal, hogy teleszemetelje a láncot. A bányászok növelnék a blokkok méretét, mert a pénz az pénz, legyen bármilyen kicsi is. Ez állandóan nagy blokkokhoz vezetne, elenyésző gazdasági haszonért cserébe. A Bitcoin ezt úgy oldja meg, hogy mesterségesen korlátozza a blokk méretét, ezáltal díjpiacot hoz létre. A spammel támadóknak túl kellene licitálniuk a többi felhasználót, így már nem éri meg. Ez azonban azt is jelenti, hogy a blokkok megtelnek, és némely tranzakciónak várakozni kell, ahogy fentebb említettük.

Szóval hogyan lehet a Moneronak dinamikus blokkmérete, úgy, hogy elkerüli a spam-alapú támadásokat? A megoldás egyszerű, mégis ravasz. A blokkjutalomból levonás történik, ha a blokk nagyobb méretű a szokásosnál. Ha egy bányász növelni akarja a blokkot, akkor a jutalom, ami a blokk megtalálásáért jár, kevesebb lesz, mint amit egyébként kapna. Így csak akkor növeli meg a blokkméretet, ha a felhasználók fizetett tranzakciós díjak kompenzálnák a blokkjutalom csökkenését. Például, ha a bányász 0,5 XMR-t veszítene a blokk méretének növelésével, és a további tranzakciós díjak összege 0,4 XMR, ez számára 0,1 XMR nettó veszteséggel járna, tehát nem teszi meg. Ezzel szemben, ha az összes tranzakciós díj összege 0,7 XMR, akkor 0,2 XMR nyeresége lenne, még akkor is, ha elveszít 0,5 XMR-t a blokkjutalomból, így érdemes megnövelie a blokkméretet.

A dinamikus blokkok lehetővé teszik a hálózat szerves növekedését, a blokkméret mesterséges korlátása nélkül, így díjpiac kikényszerítése nélkül, miközben megelőzik a spamtámadásokat is. Számos további szempontból is megvizsgálhatnánk ezt az ötletet, több oka is van annak, hogy miért nem tudja ezt megvalósítani a Bitcoin és leszármazottai, de reméljük, hogy az olvasónak sikerült ennyiből is átadni, hogyan kerüli meg Monero a Bitcoin számos problémáját, és miként tervezi az áteresztőképességét bővíteni a jövőben.

További olvasnivaló