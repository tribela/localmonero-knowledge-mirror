---
title: "Seraphis: Mit fog elhozni Moneronak"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: moduláris felépítésű Monero tranzakciók

## Seraphis: moduláris felépítésű Monero tranzakciók

Ez a bejegyzés a [Seraphis](https://github.com/UkoeHB/Seraphis)t mutatja be, tranzakciós protokoll-struktúrák és eljárások egy csoportját, amelyet a [`koe`](https://github.com/UkoeHB) álnevű közreműködő kutató fejlesztett ki a Monero számára, a [`coinstudent2048`](https://github.com/coinstudent2048) álnevű közreműködő folyamatos biztonsági elemzése mellett.  
Néhol egyszerűsíteni fogunk, és az érthetőség kedvéért kihagyunk bizonyos technikai részleteket. Ezért, és mert a Seraphis kialakítása még folyamatban van, az érdeklődő olvasónak érdemes a Seraphis dokumentációjában utánajárni a legfrissebb információknak.

## Monero tranzakciók

## Monero tranzakciók

A Bitcoin, a Monero, és több másik protokoll az úgynevezett „kimenet” modellre épül, ahol a _kimenet_ testesíti meg az átvihető értéket.  
A tranzakciók egy vagy több, a feladó tulajdonában lévő kimenetet fogyasztanak el, és új kimeneteket hoznak létre a címzettek oldalán (illetve visszajáróként a feladónál); a tranzakciónak egyensúlyban kell lennie oly módon, hogy az elfogyasztott kimenetek összértékének pontosan meg kell egyezni az új kimenetek értékével (a hálózat által kiszabott díjat is figyelembe véve).  
Sok protokollnál, például a Bitcoinéban, a kimenet értéke titkosítatlan, ahogy a címzett is.  
Ezért a blokkláncot vizsgálva triviális megtudni, hogy egy kimenetet elköltöttek-e, és ha igen, mikor (vagyis, hogy egy későbbi tranzakció során felhasználták-e, és melyik tranzakció költötte el).

Ezzel szemben az olyan protokollok, mint a Monero, más megoldást használnak:

  * A kimenetek értéke rejtett, nem látható a blokkláncon
  * A címzettek el vannak rejtve egyszer használatos címzési protokoll használatával
  * Azt, hogy egy kimenetet elköltöttek-e vagy sem, a kétértelmű aláírások használata takarja el

Ennek eredményeképpen külső információ hiányában nehéz megállapítani, hogy egy adott kimenetet elköltöttek-e, mi az értéke, és ki a címzettje.

A jelenlegi Monero tranzakciós protokoll neve _RingCT_ , és számos kriptográfiai építőelemet használ a fenti célok eléréséhez.

  * _A kötelezettségvállalások_ elrejtik az összegeket matematikailag hasznos módon
  * _A tartomány-bizonyítékok_ megakadályozzák a túlcsordulást, ami a kínálat inflációjához vezethetne
  * _Az összekapcsolható gyűrűs aláírások_ az aláíró kétértelműségét biztosítják, és megakadályozzák a dupla költekezést
  * _A kötelezettségvállalás-eltolások_ biztosítják, hogy a tranzakció egyensúlyban van

Ezeknek az elemeknek a kifinomult szövedéke a RingCT protokoll.

A RingCT hasznos tulajdonsága, hogy egyes építőelemek megváltoztathatók vagy kicserélhetők oly módon, hogy az általános kialakítás és a tulajdonságok érintetlenek maradjanak, de hatékonysági vagy a biztonsági fejlődést biztosíthatnak. Ilyen jellegű frissítések többször előfordultak (és továbbiak vannak tervben) a Monero történetében. Az eredeti RingCT protokollban a tartománybizonyítás ormótlan és lomha volt; később cserélték le a [Bulletproofs](https://eprint.iacr.org/2017/1066) nevű konstrukcióra, amely jobb biztonsági elemzéssel kisebbé és gyorsabbá tette a tranzakciókat, és a tervek szerint egy újabb [Bulletproofs+](https://eprint.iacr.org/2020/735) nevű változatra lesz frissítve további hatékonyságnövekedés érdekében. 

Hasonló folyamat ment végbe a gyűrűs aláírásokkal. Az eredeti protokollban az [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34) nevű megvalósítást használták. Ezt később az újabb, [CLSAG](https://eprint.iacr.org/2019/654) nevű konstrukció váltotta, amely szintén gyorsabb, kisebb tranzakciókat eredményez, a körültekintőbb biztonsági elemzés következtében. Egy ennél is újabb, [Triptych](https://eprint.iacr.org/2020/018) alapú összekapcsolható gyűrűs megoldás is felmerült, de ez nem kerül bevezetésre, a többes aláírási műveleteket érintő mellékhatásai miatt.

## Seraphis

## Seraphis

A Seraphis egy lépéssel előrébb viszi ezt az ötletet.  
A meglévő RingCT tranzakciós protokoll egyes elemeinek frissítése helyett egy másik protokollt vezet be, amely képes kihasználni a különböző építőelemek előnyeit, és továbbfejlesztett funkcionalitást kínál.

## Építőelemek

## Építőelemek

A Seraphis másféle kriptográfiai elemeket használ a tervezett céljainak eléréséhez.

  * _A kötelezettségvállalások_ elrejtik az összegeket
  * _A tartomány-bizonyítékok_ megakadályozzák a túltermelást és a kínálat felfújását
  * _A tagság-bizonyítékok_ az aláíró személyének bizonytalanságát biztosítják
  * _A kötelezettségvállalás ellentételezései_ igazolják az egyenleget
  * _A jogosultsági bizonyítékok_ megakadályozzák a dupla költekezési kísérleteket

Vegye észre a különbséget: a linkelhető gyűrűs aláírásokat a tagsági igazolások és az jogosultsági igazolások kombinációja váltja fel. Durván fogalmazva, a tagsági bizonyítások azt mutatják meg, hogy az elhasznált kimenet része egy nagyobb halmaznak , hasonlóan ahhoz, ami a RingCT-ben történik. A RingCT-vel ellentétben a tagsági bizonyítványok egyáltalán nem használják a kapcsolási címkét! A jogosultsági bizonyítékok megmutatják, hogy az összekapcsoló címke érvényes, és a végső tranzakció aláírásához fel volt használva.

Mivel a RingCT a kapcsolási címkét a kétséges aláírásba építi be, az aláírási (és a többes aláírási) műveletek számításigényesebbek, és nagyobb kihívást jelent a címkékkel kapcsolatos egyéb funkciók felépítése. A Seraphis lehetővé teszi a tagsági igazolások létrehozásának biztonságos delegációját, hogy a kiemelten megbízható eszközök helyett (amelyek általában korlátozott számítási teljesítménnyel bírnak, például egy hardver pénztárca) egy kevésbé megbízható eszköz végezze el, míg az aláírási műveletek sokkal könnyebbek az egyszerűbb jogosultsági bizonyítással.

Szerencsére a Seraphis által igényelt építőelemek egy része már létezik máshol, és nem kell őket nulláról megtervezni. Mind a Bulletproofs, mind a Bulletproofs+ megoldások használhatók tartományi bizonyítékokként. A Schnorr típusú bizonyítási rendszerek változatai felhasználhatók a jogultsági bizonyításokra. A hatékony [megoldás](https://eprint.iacr.org/2015/643), ami a Triptych, a [Lelantus](https://eprint.iacr.org/2019/373), és a [Spark](https://eprint.iacr.org/2021/1173)* alapját is képezi, módosítható úgy, hogy alkalmas legyen tagság bizonyítására. 

* A Cypher Stack támogatást kap a Spark fejlesztésére.

## Címzés

## Címzés

Sajnos a jelenleg használt Monero címek nem kompatibilisek a Seraphis-szal. A felhasználóknak új címeket kellene generálniuk pénztárcájukhoz tartozó kulcsaikból ahhoz, hogy Monerot fogadhassanak, ha a Seraphis bevezetésre kerülne. Azonban ennek a költségnek a megfizetése számos előnnyel is járna.

A fent tárgyalt strukturális előnyök mellett a Seraphis kialakítása számos különböző címépítési megoldást is lehetővé tesz, amelyek mindegyike más kompromisszumokkal jár. Bár a Seraphisban használatos végső konstrukció [egyelőre vita tárgya](https://github.com/monero-project/research-lab/issues/92) (az egyik figyelmet keltő változat a [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), beszámolhatunk néhány közös és hasznos funkcióról.

Mint azt Ön is tudhatja, a Monero-címek _megtekintő kulcsot_ tartalmaznak, amivel biztosíthatja egy eszköznek vagy harmadik félnek, hogy az Ön nevében figyelje a beérkező kimeneteket, anélkül, hogy átadná a költekezési jogkörét is. Ez hasznos pénztárcákhoz, amelyek naprakészek maradhatnak, miközben a költési kulcsát biztonságosan elzárva tartja. Olyan esetekben is jól jön, amikor megtekintési hozzáférést szeretne adni, például egy átláthatóan működő nyilvános jótékonysági szervezet esetén vagy egy vállalat könyvelési részlegén.

A Monero megtekintési kulcsok hátránya, hogy nem biztosítanak teljes vagy nagyfelbontású hozzáférést. Nem lehet megbízhatóan észlelni, hogy a pénztárca mikor költ pénzt, ami megnehezíti a pénztárca egyenlegének kiszámítását, amikor a költési kulcs nem áll rendelkezésre. Jelenleg szintén nem lehetséges a bejövő kimenetek észlelése anélkül, hogy ne tudná meg az ezeknek a kimeneteknek az értékét is (ami azt jelenti, hogy a bejövő kimenetek megtalálásáért felelős harmadik fél azt is megtudja, pontosan mennyi Monerot kap).

A Seraphis címzési konstrukciók megoldhatják ezt. A Seraphis használatával a címek különböző kulcsokkal érkeznek, amelyek különböző dolgokra képesek:

  * Figyelje a bejövő kimeneteket, de tartsa rejtve értéküket
  * Figyelje a bejövő kimeneteket, és mutassa meg az értéküket is
  * Figyelje a küldött kimeneteket
  * Segítsen a tranzakciók generálásában, de ne tudja aláírni azokat
  * Generáljon új címeket (kiskereskedők számára vagy sok ügyféllel kapcsolatban lévő tőzsdéknek hasznos)

A cím tulajdonosaként Ön dönti el, hogy mennyi jogosultságot ruház át egy eszközre vagy harmadik félre.

## Az átfogó kép

## Az átfogó kép

A Seraphis jelentős változást jelent a Monero világában. Bár a címek és a tranzakciós építőelemek módosításával is jár, kialakítása olyan rugalmasságot és hasznos funkcionalitást kínál, amely a meglévő RingCT protokollal nem lehetséges. Míg a tervezés nagy része már végleges és [megvalósítása](https://github.com/UkoeHB/monero/tree/seraphis_lib) elkezdődött, a címtervezés és a biztonsági elemzés még folyamatban van. A Seraphis kiváló lehetőség a Monero előmozdítására!

További olvasnivaló

  * [A Monero egyedülálló módon teszi lehetővé a körkörös gazdaságokat](/knowledge/monero-circular-economies)/

  * [A Monero gyűrűs aláírásai kontra CoinJoin, mint a Wasabiban](/knowledge/ring-signatures-vs-coinjoin)/

  * [Miért (és hogyan!) érdemes a kulcsokat saját kézben tartani](/knowledge/hold-your-keys)/

  * [Hozzájárulás a Monerohoz](/knowledge/contributing-to-monero)/

  * [Hogyan befolyásolják a távoli csomópontok a Monero adatbiztonságát](/knowledge/remote-nodes-privacy)/

  * [Hogyan használja a Monero a hard forkokat a hálózat frissítéséhez](/knowledge/network-upgrades)/

  * [Nézetcímkék: Hogyan csökkenti egy byte adat a Monero tárcák szinkronizálási idejét 40+%-kal](/knowledge/view-tags-reduce-monero-sync-time)/

  * [A P2Pool és szerepe a Monerobányászat decentralizálásában](/knowledge/p2pool-decentralizing-monero-mining)/

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