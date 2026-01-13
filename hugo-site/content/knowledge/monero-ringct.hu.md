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