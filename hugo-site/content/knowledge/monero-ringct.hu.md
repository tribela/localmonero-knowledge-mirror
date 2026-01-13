---
title: "Hogyan rejti el a RingCT a Monero tranzakciók összegét?"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
A Monero adatvédelme nem múlik egyik egyedi mechanizmuson sem, amelynek feltörése a tranzakciókat teljesen felfedné, hanem három különböző technológiára épül, amelyek együttesen biztosítják a teljeskörű adatbiztonságot, miközben kompenzálják a többi rész gyengeségeit. Ez a háromágú megközelítés [gyűrűs aláírásokból](/knowledge/ring-signatures), RingCT-ből és a[rejtőzködó címekből](/knowledge/monero-stealth-addresses) áll. Ez a három technológia rejti el a valós kimenetet (a küldőt), mennyiséget és a fogadót. Ma a RingCT-ről fogunk beszélni.

A RingCT feltehetően a leginkább technikai a három közül, és nehéz lehet megérteni, ezért nem azt fogjuk bemutatni, hogyan működik pontosan, hanem megmutatjuk, miként lehetséges, hogy nem ismerünk egy összeget, és mégis be tudunk bizonyítani róla dolgokat. Ne aggódjon, rengeteg példát fogunk használni, mint mindig.

Először is vizsgáljuk meg, miért fontos bármit is ellenőrizni az összegekkel kapcsolatban. Miért nem tarthatjuk őket teljesen titokban? Azért, mert vannak trükkös módszerek arra, hogy az emberek a semmiből pénzt teremtsenek, ha lehetőséget kapnak rá. Hogyan működhet az ilyesmi? Nézzünk meg egy példát.

Ha szeretne vásárolni egy terméket a barátjától, és ő tíz dollárt akar érte, tehát kezdetben tíz dollárja van, neki pedig nulla. Miután átadja neki a tíz dollárt, neki lesz tíz dollárja, Önnek pedig nulla. Ön tízzel kezdett, most pedig a barátjánál van tíz. Ebben a tranzakcióban nem keletkezett vagy semmisült meg pénz.

Kriptovaluták esetén egy ravasz illető adhatna tíz dollárt az árucikkért, és ahelyett, hogy nulla dollárt kapna vissza, kettőt kap meg. A 0 és 10, majd 10 és 0 (vagyis 10=10) helyett 0 és 10, majd 10 és 2 (vagyis 10=12). Két Monero a semmiből jött létre. Elképzelheti, hogy ha az valaki ezt többször megteszi, rövid időn belül óriási vagyonra tehetne szert.

A Bitcoin és hasonlók esetében ez könnyen ellenőrizhető. Megnézzük a tranzakció bemeneteit és kimeneteit, és meg tudunk bizonyosodni, hogy az elküldött mennyiség megegyezik a fogadottal. Ha ezek az összegek titkosítva vannak és nem láthatók, akkor a felhasználó nem tudja ellenőrizni, hogy a küldött és a fogadott összeg megegyeznek-e.

A Bitcoin adatbiztonságát növelendő Gregory Maxwell megalkotta a Confidential Transactions [CT] (Bizalmas Tranzakciók) nevű új technológiát, amely lehetővé teszi az összegek titkosítását, miközben bizonyítani tudja, hogy a folyamat során semmi sem keletkezett vagy semmisült meg. Mint a legtöbb adatvédelmi technológia, végül ez sem került be a Bitcoinba, de Monero nagyon szívesen alkalmazta. Ezzel csak egy probléma volt: a meglévő gyűrűs aláírások technológialiag összeegyeztethetetlenek voltak az ötlettel. Ezért az egyik akkori Monero-kutató, Shen Noether a CT-t RingCT-vé alakította át, a CT egy olyan változatává, amely kompatibilis a gyűrűs aláírásokkal.

Megint csak, hogy ennek működése meglehetősen bonyolult, nehéz lenne elmagyarázni egy bevezető szintű cikkben. A kriptográfia-rajongó számára, aki feltétlenül meg akarja tudni, rengeteg részletes írás található az interneten a CT belső működéséről. A többiek számára ez a cikk csak bemutatja, hogyan lehet elrejteni az összegeket, de mégis bebizonyítani, hogy semmi sem keletkezett vagy semmisült meg.

Tegyük fel, hogy Anna pénzt akart küldeni Bélának. Anna 10 XMR-t küld Bélának, aki 10 XMR-t kap meg. 10=10 tehát nincs itt semmi baj. De Anna nem akarja, hogy mindenki megtudja, mennyit küld. Ezért ő és Béla készítenek egy közös titkot. Alapvetően ez egy szám, amit csak ők ketten ismernek. Tegyük fel, hogy ez a szám 22. Anna megszorozza 10-et (ami a valódi összeg) 22-vel, így 220-at kap. Ezt a számot osztja meg a hálózattal.

A bányászok maguk sem tudják a titkos számot. Ha tudnák, eloszthatnák a számukra látható értéket a titkos számmal, és megtudhatnák a valós összeget. De mivel nem tudják, nem tehetik ezt meg. Azt viszont látják, hogy Béla 220-at fog kapni. 220 lett elküldve. 220 érkezett meg. 220 = 220. Ily módon a hálózat ellenőrizheti, hogy nem jött létre vagy semmisült meg Monero, mindezt anélkül, hogy ismerné a valós összeget, amelyet Anna küldött Bélának .

Mivel Béla tudja a megosztott titkos számot, amikor megkapja a pénzt, csak elosztja 22-vel, hogy megkapja az Anna által küldött valós összeget, a 10-et. Anna és Béla is tudják, hogy mennyit küldtek és mennyit kaptak, míg mindenki más hamis számot lát.

Még egyszer, ez nem a CT tényleges működési módja, de ad egy képet arról, hogyan lehetséges az ilyesmi. A valódi módszer olyan dolgokból áll, mint a Pedersen-vállalások, két elküldött összeg (egy titkosított összeg a címzettnek és egy vállalási összeg a hálózatnak), és… igen, már most látszik, hogy könnyen bele lehet kavarodni.

Fontos megjegyezni, hogy bár a RingCT elrejti a tranzakcióban két fél között gazdát cserélő összeget, két másik csoporttal nem teszi ezt.

Az egyik a coinbase tranzakciók. Ha ez a kifejezés ismeretlen lenne: ez alapvetően azt a jutalmat jelenti, amelyet a bányászok kapnak a következő blokk megtalálásáért. Ez a szám nincs elrejtve. Bárki láthatja, hogy a protokoll mennyit jutalmat adott egy bányásznak a szolgálatáért. Ezáltal az összes coinbase-tranzakció összeadásával megállapítható a létező Monero jelenlegi mennyisége. Az összegük megegyezik a jelenleg forgalomban lévő Monero mennyiségével.

A másik nem rejtett összeg a bányászoknak fizetett díj, amit a tranzakciók megerősítéséért kapnak. Ezeknek egyértelműnek kell lenniük, hogy a bányászok tudhassák, melyiket részesítség előnyben. Ezzel azonban a felhasználók megsérthetik a magánéletüket, mivel ha valaki egyedi díjat használ minden egyes tranzakciója elküldésekor (például 0,12345), akkor tranzakciói összekapcsolhatók.

Ezeket kivéve a RingCT 2017 óta titokban tartja a Monero összegeket, mindannyiunk adatvédelmét erősítve.

További olvasnivaló

  * [A Monero egyedülálló módon teszi lehetővé a körkörös gazdaságokat](/knowledge/monero-circular-economies)/

  * [A Monero gyűrűs aláírásai kontra CoinJoin, mint a Wasabiban](/knowledge/ring-signatures-vs-coinjoin)/

  * [Miért (és hogyan!) érdemes a kulcsokat saját kézben tartani](/knowledge/hold-your-keys)/

  * [Hozzájárulás a Monerohoz](/knowledge/contributing-to-monero)/

  * [Hogyan befolyásolják a távoli csomópontok a Monero adatbiztonságát](/knowledge/remote-nodes-privacy)/

  * [Hogyan használja a Monero a hard forkokat a hálózat frissítéséhez](/knowledge/network-upgrades)/

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