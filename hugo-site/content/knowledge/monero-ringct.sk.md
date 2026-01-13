---
title: "Ako RingCT skrýva sumy transakcií Monero"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Ochrana súkromia spoločnosti Monero nezávisí od jedného jediného mechanizmu, ktorý by v prípade porušenia odhalil všetky transakcie, ale skôr od troch rôznych technológií, ktoré spolupracujú, aby poskytovali holistické súkromie a zároveň kompenzovali slabé stránky ostatných častí. Tento trojitý prístup pozostáva z [podpisov zvonenia](/knowledge/ring-signatures), RingCT a [skrytých adries](/knowledge/monero-stealth-addresses). Tieto tri technológie skrývajú skutočný výstup (odosielateľ), množstvo a prijímač. Dnes budeme hovoriť o RingCT.

RingCT je pravdepodobne najtechnickejší z týchto troch a môže byť ťažké ho pochopiť, takže nebudeme hovoriť o tom, ako presne to funguje, ale skôr ukážeme, ako je možné nevedieť veľa ale stále si o ňom niečo potvrdiť . A nebojte sa, ako vždy použijeme množstvo príkladov.

Najprv sa pozrime, prečo je dôležité overovať si čokoľvek o sumách. Prečo ich nemôžeme udržať úplne v tajnosti? Odpoveď je, že existujú šikovné spôsoby, ako môžu ľudia vytvárať peniaze zo vzduchu, ak dostanú príležitosť. Ako môže niečo také fungovať? Pozrime sa na príklad.

Ak si chcete kúpiť položku od svojho priateľa a on za to chce desať dolárov, potom začnete s desiatimi dolármi a on začne s nulou. Keď mu dáte desať dolárov, on má desať dolárov a vy nulu. Začal si s desiatimi a on ich má teraz desať. Pri tejto transakcii neboli vytvorené ani zničené žiadne peniaze.

S kryptomenami môže šikovný jednotlivec dať desať dolárov za položku a namiesto toho, aby dostal nula dolárov v drobných, môže dostať dva doláre späť. Namiesto toho, aby 0 a 10 viedli k 10 a 0 (alebo 10=10), je to teraz 0 a 10 vedie k 10 a 2 (alebo 10=12). Two Monero bolo stvorené len tak zo vzduchu. Môžete si predstaviť, že ak by to jednotlivec urobil sám sebe niekoľkokrát, bol by schopný v krátkom čase nahromadiť obrovský majetok.

S Bitcoinom a ďalšími by to bolo ľahko vidieť. Pozeráte sa na vstupy vstupujúce do transakcie a výstupy a uistite sa, že to, čo je odoslané, sa rovná tomu, čo je prijaté. Ak boli tieto sumy zašifrované a neboli viditeľné, používateľ nemá žiadny spôsob, ako overiť, či to, čo sa odosiela a čo prijíma, je rovnaké.

V snahe zvýšiť súkromie bitcoinov Gregory Maxwell vytvoril dôverné transakcie (CT), novú technológiu, ktorá by umožňovala šifrované sumy a zároveň dokázala, že v tomto procese nebolo nič vytvorené ani zničené. Rovnako ako väčšina technológií na ochranu osobných údajov sa nedostala do bitcoinu, ale spoločnosť Monero mala záujem o jej prijatie. Bol tu len jeden problém. Už implementovaná technológia krúžkových podpisov bola nezlučiteľná s navrhovanou myšlienkou. Takže jeden z vtedajších výskumníkov MRL, Shen Noether, upravil CT na RingCT, verziu CT, ktorá bola kompatibilná s kruhovými podpismi.

Znova, spôsob, akým to funguje, je dosť technický a bolo by ťažké ho vysvetliť v úvodnom článku. Pre nadšencov kryptografie, ktorí to jednoducho musia vedieť, existuje na internete množstvo podrobných článkov o vnútornom fungovaní CT. Nám ostatným tento článok ukáže, ako by bolo možné skryť sumy, no zároveň dokázať, že nič nebolo vytvorené ani zničené.

Povedzme, že Alica chcela poslať Bobovi peniaze. Alica pošle 10 XMR Bobovi, ktorý dostane 10 XMR. 10=10, takže tu nie je nič zlé. Ale Alica nechce, aby niekto vedel, koľko posiela. Takže ona a Bob vytvoria spoločné tajomstvo. V podstate číslo, ktoré poznajú len oni dvaja. Povedzme, že to číslo je 22. Teraz Alica vynásobí 10 (to, čo skutočne posiela) 22, čím dostane 220. Toto je číslo, ktoré zdieľa so sieťou.

Samotní baníci nepoznajú tajné číslo. Ak tak urobili, mohli by číslo, ktoré sa im zobrazuje, vydeliť tajným číslom a získať tak zaslanú skutočnú sumu. Ale keďže nepoznajú tak nemôžu. Vidia však, že Bob dostane 220 prijatých. 220 = 220. Týmto spôsobom môže sieť overiť, že žiadne Monero nebolo vytvorené alebo zničené, a to všetko bez toho, aby vedela skutočnú sumu, ktorú Alica poslala Bobovi.

Keďže Bob pozná zdieľané tajné číslo, keď dostane peniaze, jednoducho ich vydelí 22, aby získal skutočnú sumu, ktorú Alica poslala, 10. Alica aj Bob vedia, koľko bolo poslaných a koľko bolo prijatých a všetci ostatní dostanú falošné číslo.

Ešte raz, toto nie je skutočný spôsob, akým CT funguje, ale dáva predstavu o tom, ako by niečo také mohlo byť možné. Skutočný spôsob zahŕňa veci ako Pedersenove záväzky, dve odoslané čiastky (jedna zašifrovaná čiastka príjemcovi a jedna čiastka záväzku do siete) a...áno, už teraz je ľahké vidieť, ako sa v tom všetkom môžete stratiť.

Jedna vec, ktorú je potrebné poznamenať, je, že zatiaľ čo RingCT skrýva sumu transakcie medzi dvoma stranami v transakcii, neskrýva dve ďalšie sady čísel.

Prvou sú transakcie coinbase. Ak vám tento pojem nie je známy, znamená to v podstate odmenu, ktorú baníci dostávajú za nájdenie ďalšieho bloku. Toto číslo nie je skryté. Každý môže vidieť, koľko protokol ocenil baníka za jeho službu. Týmto spôsobom je možné zistiť aktuálnu existujúcu sumu Monero sčítaním všetkých transakcií coinbase. Ich súčet sa bude rovnať aktuálnemu Monero v obehu.

Druhé číslo, ktoré nie je skryté, je poplatok zaplatený baníkom, keď používateľ odošle transakciu. Poplatky musia byť jasné, aby ťažiari vedeli, koho majú uprednostniť. Toto je spôsob, ktorým si používatelia môžu poškodiť svoje súkromie, pretože ak niekto použije jedinečný poplatok za baníka zakaždým, keď odošle transakciu (napríklad 0,12345), ich transakcie môžu byť prepojené.

Okrem týchto prípadov spoločnosť RingCT od roku 2017 skrýva sumy Monero a naše kolektívne súkromie je o to silnejšie.

Ďalšie čítanie