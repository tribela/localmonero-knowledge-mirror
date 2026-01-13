---
title: "Miért jobb a Monero, mint a Dash, a Zcash, a Zcoin (még Lelantussal is), a Grin és a Bitcoin mixerek, mint a Wasabi (Frissítve 2020 májusában)"
slug: "why-monero-is-better"
date: "Sat Feb 01"
image: "/images/why-monero.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Nem minden adatvédelmi fókuszú érme képes 100%-os védelmet, követhetetlenséget, biztonságot és helyettesíthetőséget biztosítani egy 100%-ban decentralizált valutával, bizalommentes rendszerben. Íme, ezek jelentése, és hogy miért fontosak:

Privát
    Pénzügyei nem láthatóak a nyilvánosság számára. Ha valaki megnézi a blokkláncot, nem fogja látni, mennyi pénze van.
Lenyomozhatatlan
    Az eszközöket nem lehet nyomon követni blokkláncelemzéssel vagy blokkláncfigyeléssel.
Biztonságos
    Minden tranzakció titkosított, és az Ön pénzét tároló pénztárca is titkosított.
Felcserélhető
    Minden egység egyforma és azonos értékű.
Decentralizált
    A hálózat összes csomópontja (a csomópont a blokklánc egy futó példánya) egyenlő. A csomópontoknak nincs olyan magasabb osztálya, amely nagyobb befolyással vagy ellenőrzéssel bírna a tranzakciók vagy a rendszer felett.

## Kriptopénz elemzés

Íme egy elemzés azokról az ismert kriptovalutákról, amelyek anonimitást és/vagy nyomon követhetetlenséget ígérnek. Maga a Bitcoin nem tartozik ennek az elemzésnek a körébe, mivel soha nem állította, hogy névtelen lenne.

Ezt az oldalt Monero felhasználók készítették. Volt idő, amikor nem voltunk Monero felhasználók, de aggódtunk a pénzügyi adatvédelem miatt. Kerestük azokat a kriptovalutákat, amelyek privátak, és ez az oldal lett a kutatásunk eredménye. Ezért választottuk Monerót. Tehát, elfogultnak tűnhetünk, tán azok is vagyunk, de úgy látjuk, hogy ez az elfogultság olyan tényeken alapul, amelyekről alább olvashat, és saját maga is megerősíthet.

### Áttekintés

Válassza ki a logót, hogy a valuta elemzéséhez ugorjon.

| Privát| Lenyomozhatatlan| Biztonságos| Felcserélhető| Decentralizált  
---|---|---|---|---|---  
Monero| Igen| Igen| Igen| Igen| Igen  
DASH| Nem| Nem| Igen| Nem| Nem  
Zcash| Nem| Nem teljesen| Igen| Nem| Nem  
| Igen| Igen| Igen| Igen| Nem  
| Néha| Nem| Igen| Bizonytalan| Igen  
Bitcoin mixers| Nem| Nem| Igen| Nem| Néha  
  
### Monero

Privát
    A Monero megbízható kriptográfiát használ, amely lehetővé teszi pénzek küldését és fogadását anélkül, hogy tranzakciói nyilvánosan láthatóak lennének a blokkláncon (a tranzakciók elosztott főkönyvében). Ez biztosítja, hogy vásárlásai, nyugtái és egyéb átutalásai **alapértelmezetten privátak maradnak**. A feladó, a címzett és a tranzakció összege mind rejtve marad. Egyes kriptovalutáknak van "gazdaglistája", amely lehetővé teszi bárki számára, hogy megnézze, melyik fiók rendelkezik a legtöbbel a valutából. Mivel a Monero privát, [Monero gazdaglista](http://moneroblocks.info/richlist) nem lehetséges.
Lenyomozhatatlan
    A gyűrűs aláírások (egyes titkosítások speciális tulajdonsága) kihasználásával a Monero nyomon követhetetlen tranzakciókat tesz lehetővé. Ez azt jelenti, hogy nem egyértelmű, hogy milyen összegeket költöttek el, így rendkívül valószínűtlen, hogy egy tranzakciót egy adott felhasználóhoz lehet kapcsolni.
Biztonságos
    Az elosztott peer-to-peer konszenzusos hálózat használatával minden tranzakció kriptográfiailag biztosított. Az egyéni fiókok létrehozásakor egy 25 szavas emlékeztető seed jelenik meg, amelyet fel lehet jegyezni a fiók biztonsági mentéséhez. A jelszó megadása kötelező a pénztárca létrehozásakor, a fiók titkosított, hogy lopás esetén értéktelenek legyenek.
Felcserélhető
    Minden egység egyforma és azonos értékű. Egy felhasználó, beszállító vagy bárki más nem tud blokkolni vagy feketelistázni bizonyos Monero tranzakciókat, mivel a Monero kimenetek előzményei nem egyértelműek.
Decentralizált
    Minden Monero csomópont egyenlő. A csomópontoknak nincs olyan szuperosztálya, amely nagyobb befolyással vagy ellenőrzéssel bírna a tranzakciókra, mint a többiek. Egy személy vagy szereplő sem tudja követni a tranzakciókat azáltal, hogy több csomópontot birtokol. Ezenkívül nincs bizalmi alapú beállítás. Ez azt jelenti, hogy személyekbe vagy szereplőkbe vetett bizalom nem szükséges. Csak a forráskódban (amit bárki ellenőrizhet) és a matematikában kell megbízni.

A Monero a kezdetektől fogva 100%-ban nyílt forráskódú, ami azt jelenti, hogy bárki megtekintheti a [forráskódját](https://github.com/monero-project/bitmonero), így ellenőrizheti, hogy nincsenek benne hátsó ajtók, és hogy a szoftver biztonságos.

A Moneronak [lektorált kutatási cikkei ](https://lab.getmonero.org/) is vannak, amelyek matematikailag és módszeresen igazolják a fent felsorolt összes tulajdonságot.

### DASH

Privát
    

A DASH-nek van egy [ gazdaglistája](https://bitinfocharts.com/top-100-richest-darkcoin-addresses.html), tehát egyértelműen nem privát lánc. Az címek pénzügyi adatait bárki láthatja, aki megvizsgálja a blokkláncot.

> A DASH egyáltalán nem privát. Volt egy dia a prezentációban, amin csak annyi volt: "DASH, LOL", és semmi más... ez kígyóolaj, én személy szerint magamon kívül vagyok tőle. 
> 
> **Gregory Maxwell** , Bitcoin Core fejlesztő és kriptográfus [ egy Coinbase-nek tartott előadásában ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

**Peter Todd** , egy másik Bitcoin fejlesztő és kriptográfus [ hasonló kijelentést tett](https://twitter.com/petertoddbtc/status/622022840330682368).

Lenyomozhatatlan
    A tranzakciók [mestercsomópontok](https://www.dash.org/masternodes/) sorozatán vannak keresztülirányítva, hogy nyomon követhetetlenek legyenek. Ez a gyakorlat akkor működhet, ha az összes mestercsomópont kezelője jószándékú. Ha azonban egy kormány, hackercsoport, más szereplő vagy akár egy magánszemély sok főcsomópontot vásárolt (és nem lehet tudni, hogy történt-e ilyen), és ha a tranzakció olyan útvonalon megy keresztül, ahol az összes csomópont az adott szereplő tulajdonában volt, akkor nyomon követheti a tranzakciót. Tekintettel a masternode-ok viszonylag alacsony árára, valamint a kormányok és egyes szervezetek hatalmas költségvetésére, ez a lehetőség nagyon is valós.
Biztonságos
    A tranzakciók biztonságosan titkosítottak.
Felcserélhető
    Mivel a tranzakciók nem titkosak, fennáll annak lehetősége, hogy egy szereplő blokkoljon vagy feketelistázzon egyes kimeneteket, maik ezáltal kevésbé értékesek, mint a többi. Lásd az alábbi megjegyzést a Bitcoin helyettesíthetőségének hiányáról, mivel ugyanez vonatkozik a DASH-re is.
Decentralizált
    Nem minden DASH csomópont egyenlő. Létezik a csomópontoknak egy magasabb osztálya, a _Mestercsomópontok_ (masternode), amelyek tulajdonosai nagyobb befolyással bírnak a rendszerre, mint a többiek. Ezáltal a DASH rendszere félig központosított az ideális teljesen decentralizált helyett.

### Zcash

Privát
    

A Zcash tranzakciók láthatók a blokkláncukon. Van lehetőség rejtett tranzakciókra, de [ az összes tranzakció kevesebb, mint 1%-a védett](http://stat.bloxy.info/superset/dashboard/zcash/). Mivel a rejtőzködés nem kötelező, és nem az alapértelmezett (nem beszélve arról, hogy ritkán használt), [kirívóak a blokkláncon](http://weuse.cash/2016/06/09/btc-xmr-zcash/), felhívják magukra a figyelmet.

> Mellesleg úgy gondolom, hogy a Zcash-t túl követhetővé tehetjük az olyan bűnözők esetében, mint a WannaCry, de közben teljesen privát & helyettesíthető maradhat. 
> 
> **Zooko Wilcox** , a Zcash vezérigazgatója egy [ tweetben ](https://twitter.com/zooko/status/863202798883577856)

Ha a Zcash „túl követhető” lehet, akkor nem lehet egyben teljesen privát vagy helyettesíthető. 

Lenyomozhatatlan
    

A szokványos tranzakciók átlátszóak. A rejtett tranzakciók a zk-SNARKS-ot használják, amely bizonyos feltételek mellett határozottan adatvédelmi garanciákat biztosít. A kérdés az, hogy ezek a feltételek általában teljesülnek-e, és látva, hogy milyen kevesen használják az árnyékolási képességeket, ez továbbra is bizonytalan.

Biztonságos
    A tranzakciók biztonságosan titkosítottak.
Felcserélhető
    Mivel nem minden tranzakció nem titkosətott, fennáll annak a lehetősége, hogy egy szerepl[ blokkoljon vagy feketelistázzon tegyen bizonyos kimeneteket, így azok kevésbé lesznek értékesek, mint a többi. Lásd az alábbi megjegyzést a Bitcoin helyettesíthetőségének hiányáról, mivel ugyanez vonatkozik Zcash-re is.
Decentralizált
    

A Zcash egy vállalat, és jelenleg [ az összes kibányászott ZEC 20%-át veszi el alapítói jutalomként](https://z.cash/blog/funding.html). 

A Zcash **megbízható beállítást** igényel. Ez azt jelenti, hogy meg kell bíznia abban, hogy a rendszer tisztességesen lett összeállítva. Ha nem így történt, [korlátlan mennyiségű ZEC hozható létre anélkül, hogy bárki tudna róla](https://blog.okturtles.com/2016/03/the-zcash-catch/). Ez gazdaggá tenné az elkövetőt és leértékelné a ZEC-t. Nincs mód megtudni, hogy a beállítást becsületesen hajtották-e végre. Meg kell bízni az adott szavukban. Ez emberi hibalehetőséget vezet be a rendszerbe, szinte minden más kriptovalutával ellentétben. A kriptovaluták kapcsán csak a matematikában és az ellenőrizhető forráskódban kellene megbízni, emberekben nem. Amint azt gyakorlatilag az összes nagy szoftvercég, mint a [Microsoft](https://www.gnu.org/proprietary/proprietary-back-doors.en.html), az [Apple](http://www.digitaltrends.com/computing/apple-vs-fbi-backdoor-to-data-already-exists/), sőt, a kormányok esetében is láttuk, nem szabad megbíznunk bennük. 

Peter Todd, a Bitcoin Core egy fejlesztője, aki [részt vett](https://github.com/zcash/mpc/blob/master/README.md) a Zcash beállításában, " [hátsó ajtónak](https://twitter.com/petertoddbtc/status/793584540891643906) " nevezte. 

> A Zcash nem feltétel nélkül megbízható, a jelenlegi technológiával ez nem lehetséges...megbízható beállítást igényel… újra el kell végeznie a folyamatot a titkosítás frissítéséhez, ez sebezhetőséget jelent. 
> 
> Gregory Maxwell, Bitcoin Core fejlesztő és kriptográfus, [a Coinbase-nek tartott előadásában](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

**Megjegyzés:** A Zcoin jelenlegi Sigma rendszerről egy új protokollra készül váltani, amely az új kutatási munkájára, a Lelantusra alapul. A Lelantus bevezetése szakaszokban fog történni, ez a cikk azt feltételezi, hogy minden szakasz befejeződött és elkészült az előzetes ütemterv szerint, az összehasonlítások ennek megfelelően történnek.

Amiért a Zcoinnak megadjuk ezt a jóindulatot, hogy a jövőbeli protokollja alapján ítéljük meg, míg a Zcash-nek nem, az az, hogy a Zcoinnak kész ütemterve van az átállás időzítésére, eközben a Zcash tervei az „alapértelmezetten adatvédelemmel” kapcsolatban továbbra is homályosak. 

Privát
    

A Zcoin (XZC) esetén nem lesz gazdaglista, ezért priváttá válik. Az alapértelmezett, kötelező adatvédelem várhatóan 2021-ben lép életbe. A megvalósítást követően nem lehet majd ilyen listát létrehozni (bár jelenleg [létezik](https://www.coinexplorer.net/XZC/richlist)).

Lenyomozhatatlan
    A Lelantus 2021-ben megvalósuló utolsó szakaszával a Zcoin nem lesz nyomon követhető, bár a támadások elméleti lehetőségeit még nem tárták fel, mivel még nem lett szabadjára engedve "a vadonban". Jelenleg a Zcoin követhető, ha valaki beír egy [Zcoin-címet](https://explorer.zcoin.io/) egy blokklánc-böngészőbe, láthatja annak egyenlegét és a kapcsolódó tranzakciókat.
Biztonságos
    A tranzakciók biztonságosan titkosítottak.
Felcserélhető
    Miután a Lelantus utolsó szakasza 2021-ben élesítve lesz, feltételezhető, hogy a Zcoin helyettesíthetővé válik a kötelező adatbiztonság miatt. Ebben a tekintetben a Monero valódi vetélytársa lesz. Ennek ellenére...
Decentralizált
    A Zcoin Znode-okat használ, amelyek a Dash masternode-okhoz hasonlóan működnek, nagyobb hatalmúak, mint a hálózat többi csomópontja. Mivel nem minden csomópont egyenlő, és a különbséget az egyén pénzének mennyisége határozza meg (egy Znode ára 1000 XZC), a hálózat részben központosított.

Privát
    Grinnek nincs gazdaglistája, ami az adatbiztonság valamilyen szintjére utal. Valóban, a láncot átvizsgáló passzív támadók nem láthatják, melyik címen mennyi pénz van, egyrészt azért, mert az összegeket bizalmas tranzakciók rejtik el, másrészt, mert a címadatok nem tárolódnak a láncon, illetve a Mimblewimble keresztülhasító technológiája miatt, ami lehetővé teszi a köztes tranzakciók eltávolítását a láncból, így kevés metaadat marad meg a korábbi tranzakciókból.
Lenyomozhatatlan
    A Grin nem véd egy tranzakciós gráfot építő aktív támadó ellen. Lehetőség van mind a bányászok, mind a módosított csomópontok üzemeltetői számára a tranzakciók figyelésére, elmentésére, még mielőtt a keresztülhasító technológia kifejti a hatását, innen teljes tranzakciós gráfot készíthet, az összes 'keresztülhasított' adat megtartásával együtt. Nem tudnának semmilyen információt az indulásuk előtti időkról, de az indulás utáni összes metaadat értékes lehet, amivel összekapcsolhatják a tranzakciókat.
Biztonságos
    A tranzakciók biztonságosan titkosítottak.
Felcserélhető
    Mivel minden tranzakció megkérdőjelezhetően zártkörű, és potenciálisan nyomon követhető, lehetőség van egy tranzakciós grafikon felépítésére, amelyből értékes információk gyűjthetők össze, amelyek felhasználhatók az egyén költési szokásaira vonatkozóan. A kimenetek ezután identitásokhoz kapcsolhatók, és bár az összegek nem láthatók, az a tény, hogy egy kimenet egy identitáshoz kapcsolható, azt jelenti, hogy a kimenet szennyezett lehet, éppen attól függően, hogy ki birtokolta. Úgy gondoljuk, hogy ez azt jelenti, hogy a Grin nem helyettesíthető, mivel egyes kimenetek szennyeződhetnek, míg mások nem.
Decentralizált
    A Grinnél nem volt előbányászat, alapítói jutalék, mestercsomópont vagy kincstár. Nem volt ICO-juk, és egy decentralizált közösséghez illő módon működnek. Tehát a Grin decentralizált.

### Bitcoin Mixers

Privát
    

Minden Bitcoin-tranzakció látható a blokkláncon, és létezik [gazdaglistája](http://www.bitcoinrichlist.com/top100), tehát a Bitcoin nem privát. A Bitcoin [pszeudonim](https://bitcoin.org/en/you-need-to-know), nem anonim. 

Az **Bitcoin keverők** esetében bíznia kell abban, hogy adataikat biztonságban tudják tartani, és nem kormány, bűnozők vagy más szereplők tulajdonában vannak, illetve nem működnek esetleg együtt velük. 

2017 júliusában a legnagyobb Bitcoinkeverő szolgáltatás, a BITMIXER.IO alapítója bejelentette, hogy bezárnak, ezzel az indoklással: 

> … Mostanra rájöttem, hogy a Bitcoin teljesen nyílt, nem névtelen rendszer, **így van megtervezve**. A blokklánc egy nagy nyitott könyv. 
> 
> A BITMIXER.IO, a [Bitcointalk.org](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093)-on bezárásáról szóló bejelentésben (kiemelés az eredetiben). 

Néhány héttel később, miután átgondolta a különböző adatvédelmi lehetőségeket, ezt mondta: 

> A mélyreható vizsgálat után megerősítem, hogy a MONERO a legjobb adatvédelmi valuta. Erősen ajánlom tehát a MONERO-t mindazoknak, akiknek extra magánéletre van szükségük. 
> 
> BITMIXER.IO, egy [későbbi bejegyzésben](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Lenyomozhatatlan
    

Mivel az összes Bitcoin-tranzakció látható a blokkláncon, MINDEN Bitcoin-tranzakció nyomon követhető. Egy Bitcoin-keverő nagymértékben elhomályosíthatja a tranzakciókat, ami megnehezíti a Bitcoinok követését, de nem teszi lehetetlenné. A technológia fejlődésével és a Bitcoin-tranzakciók nyomon követésére szakosodott vállalatok terjedésével, az korábban erőszen homályos tranzakciók viszonylag könnyen nyomon követhetők lesznek: 

  * [ A bűnüldöző szervek továbbra is fektetnek Bitcoin nyomkövetési szolgáltatásokba](https://news.bitcoin.com/law-enforcement-continues-invest-bitcoin-tracking-services/)
  * [ Time.com: A bitcoint könnyebb követni, mint gondolná](http://time.com/3689359/bitcoins-track-anonymous/)
  * [Elliptic: Bitcoin bűnüldözési célú nyomon követésére szakosodott vállalat](https://www.elliptic.co/)

Egy Google-keresés a fentiekhez hasonló cikkek tucatjait tárja fel. Ne feledje, minden olyan tranzakció, amely a múltban valamikor megtörtént, a blokkláncon megmarad, és követhető lehet, még akkor is, ha keverési szolgáltatást használtak. Valójában egy keverési szolgáltatás használata valószínűleg még jobban fel is hívja a figyelmet ezekre a tranzakciókra. 

Biztonságos
    A tranzakciók biztonságosan titkosítottak.
Felcserélhető
    

Nem minden bitcoin egyenlő és egyforma értékű. Némelyik Bitcoint több szereplő feketelistára tett és blokkolt, így ezek kevésbé értékesek, mint a többi. Ha olyan Bitcoint kap, amelyet korábban illegális célokra használtak fel, akkor bitcoinjai feketelistán lehetnek, akkor is, ha semmi köze nem volt az eredeti tevékenységhez. Vagy mondjuk egy kormány, munkáltató vagy egyéb szervezet úgy dönt, hogy a jövőben feketelistára teszi a bitcoinjait, hasonlóan az eszközök befagyasztásához vagy elkobzásához. Nem tudna mit tenni. Mivel egy mixer csak a Bitcoinok nyomon követését nehezíti meg, ez a kategória „nem helyettesíthető”-ként lett megjelölve.

  * Andreas Antonopoulos, a Bitcoin Core volt fejlesztője, aki nagy tiszteletnek örvend a Bitcoin és más kriptovaluta közösségekben, elismeri a Bitcoin helyettesíthetőségi problémáját egy [ YouTube-videóban](https://www.youtube.com/watch?v=ak1iojpiHpM&feature=youtu .be&t=33m9s). 
  * Vita a Bitcoin helyettesíthetőségi problémájáról a [Bitcointalk.org oldalon](https://bitcointalk.org/index.php?topic=1190707.0)

Decentralizált
    Maga a Bitcoin decentralizált, de a legtöbb keverőszolgáltatás központosított. Ez azt jelenti, hogy meg kell bíznia bennük. Némelyik újabb, mint a Wasabi tárca, azonban nem ilyen.

## Összefoglaló

Véleményünk szerint a Monero az egyértelmű választás, ha privát, biztonságos, nyomon követhetetlen, helyettesíthető egységekből álló, decentralizált kriptovalutát keres, amelyhez nem szükséges felhasználói hozzáértés a megbízható beállításra. Bármi más kockára teszi magánéletét és biztonságát. De ne fogadja el a véleményünket. járjon utána, és győződjön meg róla a saját szemével. Vegye figyelembe, hogy a Monerot olyan szervezetek is támogatják és használják, amelyeknek a privát működés és a követhetetlenség létkérdés, például: 

  * [ SIGAINT ](https://www.reddit.com/r/Monero/comments/4xqrzd/sigaint_launches_tor_monero_node_as_its_operators/)
  * [ Purism ](https://puri.sm/posts/purism-collaborates-with-cryptocurrency-monero-to-enable-mobile-payments/)
  * [ Wikileaks ](https://shop.wikileaks.org/donate#db9)
  * Az AlphaBay Marketet (AB) 2017 júliusában lekapcsolták. Az AB ellen benyújtott [ Federal Forfeiture Complaint [Szövetségi Elkobzási Feljelentés] ](https://assets.documentcloud.org/documents/3898109/AlphaBay-Cazes-Forfeiture-Complaint.pdf) a következő részleteket tartalmazza: 
    * **A Monero az egyetlen privát és követhetetlen kriptovaluta:**  
"CAZES pénztárcái és számítógépes ügynökei összesen körülbelül 8 800 000 dollár értékű Bitcoin, Ethereum, Moreno [sic] és Zcash felett rendelkeztek, a következő bontásban: 1605,0503851 Bitcoin, 8309,271639 ETH, 3691,98 ZEC _és ismeretlen mennyiségű Monero._ " (20. oldal alja és 21. oldal teteje, kiemelés tőlem) 
    * **A Bitcoin-tranzakciók nem magánjellegűek, és nyomon követhetők:**  
"A szövetségi ügynökök azután szerezték meg a végzést, miután számos, az AlphaBay-ről származó Bitcoin-tranzakciót tudtak digitális valutaszámlákhoz, végül bankszámlákhoz és egyéb tárgyi eszközökhöz kötni, amelyek CAZES és felesége birtokában voltak." (17. o., 24-26. sor)) 

A LocalMonero nem támogat és nem bátorít semmilyen illegális tevékenységet 

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

Nem minden adatvédelmi fókuszú érme képes 100%-os védelmet, követhetetlenséget, biztonságot és helyettesíthetőséget biztosítani egy 100%-ban decentralizált valutával, bizalommentes rendszerben. Íme, ezek jelentése, és hogy miért fontosak:

## Kriptopénz elemzés

Íme egy elemzés azokról az ismert kriptovalutákról, amelyek anonimitást és/vagy nyomon követhetetlenséget ígérnek. Maga a Bitcoin nem tartozik ennek az elemzésnek a körébe, mivel soha nem állította, hogy névtelen lenne.

Ezt az oldalt Monero felhasználók készítették. Volt idő, amikor nem voltunk Monero felhasználók, de aggódtunk a pénzügyi adatvédelem miatt. Kerestük azokat a kriptovalutákat, amelyek privátak, és ez az oldal lett a kutatásunk eredménye. Ezért választottuk Monerót. Tehát, elfogultnak tűnhetünk, tán azok is vagyunk, de úgy látjuk, hogy ez az elfogultság olyan tényeken alapul, amelyekről alább olvashat, és saját maga is megerősíthet.

Ezt az oldalt Monero felhasználók készítették. Volt idő, amikor nem voltunk Monero felhasználók, de aggódtunk a pénzügyi adatvédelem miatt. Kerestük azokat a kriptovalutákat, amelyek privátak, és ez az oldal lett a kutatásunk eredménye. Ezért választottuk Monerót. Tehát, elfogultnak tűnhetünk, tán azok is vagyunk, de úgy látjuk, hogy ez az elfogultság olyan tényeken alapul, amelyekről alább olvashat, és saját maga is megerősíthet.

### Áttekintés

Válassza ki a logót, hogy a valuta elemzéséhez ugorjon.

### Monero

A Monero a kezdetektől fogva 100%-ban nyílt forráskódú, ami azt jelenti, hogy bárki megtekintheti a [forráskódját](https://github.com/monero-project/bitmonero), így ellenőrizheti, hogy nincsenek benne hátsó ajtók, és hogy a szoftver biztonságos.

A Moneronak [lektorált kutatási cikkei ](https://lab.getmonero.org/) is vannak, amelyek matematikailag és módszeresen igazolják a fent felsorolt összes tulajdonságot.

### DASH

A DASH-nek van egy [ gazdaglistája](https://bitinfocharts.com/top-100-richest-darkcoin-addresses.html), tehát egyértelműen nem privát lánc. Az címek pénzügyi adatait bárki láthatja, aki megvizsgálja a blokkláncot.

> A DASH egyáltalán nem privát. Volt egy dia a prezentációban, amin csak annyi volt: "DASH, LOL", és semmi más... ez kígyóolaj, én személy szerint magamon kívül vagyok tőle. 
> 
> **Gregory Maxwell** , Bitcoin Core fejlesztő és kriptográfus [ egy Coinbase-nek tartott előadásában ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

A DASH egyáltalán nem privát. Volt egy dia a prezentációban, amin csak annyi volt: "DASH, LOL", és semmi más... ez kígyóolaj, én személy szerint magamon kívül vagyok tőle. 

A DASH egyáltalán nem privát. Volt egy dia a prezentációban, amin csak annyi volt: "DASH, LOL", és semmi más... ez kígyóolaj, én személy szerint magamon kívül vagyok tőle. 

**Gregory Maxwell** , Bitcoin Core fejlesztő és kriptográfus [ egy Coinbase-nek tartott előadásában ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

**Peter Todd** , egy másik Bitcoin fejlesztő és kriptográfus [ hasonló kijelentést tett](https://twitter.com/petertoddbtc/status/622022840330682368).

### Zcash

A Zcash tranzakciók láthatók a blokkláncukon. Van lehetőség rejtett tranzakciókra, de [ az összes tranzakció kevesebb, mint 1%-a védett](http://stat.bloxy.info/superset/dashboard/zcash/). Mivel a rejtőzködés nem kötelező, és nem az alapértelmezett (nem beszélve arról, hogy ritkán használt), [kirívóak a blokkláncon](http://weuse.cash/2016/06/09/btc-xmr-zcash/), felhívják magukra a figyelmet.

> Mellesleg úgy gondolom, hogy a Zcash-t túl követhetővé tehetjük az olyan bűnözők esetében, mint a WannaCry, de közben teljesen privát & helyettesíthető maradhat. 
> 
> **Zooko Wilcox** , a Zcash vezérigazgatója egy [ tweetben ](https://twitter.com/zooko/status/863202798883577856)

Mellesleg úgy gondolom, hogy a Zcash-t túl követhetővé tehetjük az olyan bűnözők esetében, mint a WannaCry, de közben teljesen privát & helyettesíthető maradhat. 

Mellesleg úgy gondolom, hogy a Zcash-t túl követhetővé tehetjük az olyan bűnözők esetében, mint a WannaCry, de közben teljesen privát & helyettesíthető maradhat. 

**Zooko Wilcox** , a Zcash vezérigazgatója egy [ tweetben ](https://twitter.com/zooko/status/863202798883577856)

Ha a Zcash „túl követhető” lehet, akkor nem lehet egyben teljesen privát vagy helyettesíthető. 

A szokványos tranzakciók átlátszóak. A rejtett tranzakciók a zk-SNARKS-ot használják, amely bizonyos feltételek mellett határozottan adatvédelmi garanciákat biztosít. A kérdés az, hogy ezek a feltételek általában teljesülnek-e, és látva, hogy milyen kevesen használják az árnyékolási képességeket, ez továbbra is bizonytalan.

A Zcash egy vállalat, és jelenleg [ az összes kibányászott ZEC 20%-át veszi el alapítói jutalomként](https://z.cash/blog/funding.html). 

A Zcash **megbízható beállítást** igényel. Ez azt jelenti, hogy meg kell bíznia abban, hogy a rendszer tisztességesen lett összeállítva. Ha nem így történt, [korlátlan mennyiségű ZEC hozható létre anélkül, hogy bárki tudna róla](https://blog.okturtles.com/2016/03/the-zcash-catch/). Ez gazdaggá tenné az elkövetőt és leértékelné a ZEC-t. Nincs mód megtudni, hogy a beállítást becsületesen hajtották-e végre. Meg kell bízni az adott szavukban. Ez emberi hibalehetőséget vezet be a rendszerbe, szinte minden más kriptovalutával ellentétben. A kriptovaluták kapcsán csak a matematikában és az ellenőrizhető forráskódban kellene megbízni, emberekben nem. Amint azt gyakorlatilag az összes nagy szoftvercég, mint a [Microsoft](https://www.gnu.org/proprietary/proprietary-back-doors.en.html), az [Apple](http://www.digitaltrends.com/computing/apple-vs-fbi-backdoor-to-data-already-exists/), sőt, a kormányok esetében is láttuk, nem szabad megbíznunk bennük. 

Peter Todd, a Bitcoin Core egy fejlesztője, aki [részt vett](https://github.com/zcash/mpc/blob/master/README.md) a Zcash beállításában, " [hátsó ajtónak](https://twitter.com/petertoddbtc/status/793584540891643906) " nevezte. 

> A Zcash nem feltétel nélkül megbízható, a jelenlegi technológiával ez nem lehetséges...megbízható beállítást igényel… újra el kell végeznie a folyamatot a titkosítás frissítéséhez, ez sebezhetőséget jelent. 
> 
> Gregory Maxwell, Bitcoin Core fejlesztő és kriptográfus, [a Coinbase-nek tartott előadásában](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

A Zcash nem feltétel nélkül megbízható, a jelenlegi technológiával ez nem lehetséges...megbízható beállítást igényel… újra el kell végeznie a folyamatot a titkosítás frissítéséhez, ez sebezhetőséget jelent. 

A Zcash nem feltétel nélkül megbízható, a jelenlegi technológiával ez nem lehetséges...megbízható beállítást igényel… újra el kell végeznie a folyamatot a titkosítás frissítéséhez, ez sebezhetőséget jelent. 

Gregory Maxwell, Bitcoin Core fejlesztő és kriptográfus, [a Coinbase-nek tartott előadásában](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

**Megjegyzés:** A Zcoin jelenlegi Sigma rendszerről egy új protokollra készül váltani, amely az új kutatási munkájára, a Lelantusra alapul. A Lelantus bevezetése szakaszokban fog történni, ez a cikk azt feltételezi, hogy minden szakasz befejeződött és elkészült az előzetes ütemterv szerint, az összehasonlítások ennek megfelelően történnek.

Amiért a Zcoinnak megadjuk ezt a jóindulatot, hogy a jövőbeli protokollja alapján ítéljük meg, míg a Zcash-nek nem, az az, hogy a Zcoinnak kész ütemterve van az átállás időzítésére, eközben a Zcash tervei az „alapértelmezetten adatvédelemmel” kapcsolatban továbbra is homályosak. 

A Zcoin (XZC) esetén nem lesz gazdaglista, ezért priváttá válik. Az alapértelmezett, kötelező adatvédelem várhatóan 2021-ben lép életbe. A megvalósítást követően nem lehet majd ilyen listát létrehozni (bár jelenleg [létezik](https://www.coinexplorer.net/XZC/richlist)).

### Bitcoin Mixers

Minden Bitcoin-tranzakció látható a blokkláncon, és létezik [gazdaglistája](http://www.bitcoinrichlist.com/top100), tehát a Bitcoin nem privát. A Bitcoin [pszeudonim](https://bitcoin.org/en/you-need-to-know), nem anonim. 

Az **Bitcoin keverők** esetében bíznia kell abban, hogy adataikat biztonságban tudják tartani, és nem kormány, bűnozők vagy más szereplők tulajdonában vannak, illetve nem működnek esetleg együtt velük. 

2017 júliusában a legnagyobb Bitcoinkeverő szolgáltatás, a BITMIXER.IO alapítója bejelentette, hogy bezárnak, ezzel az indoklással: 

> … Mostanra rájöttem, hogy a Bitcoin teljesen nyílt, nem névtelen rendszer, **így van megtervezve**. A blokklánc egy nagy nyitott könyv. 
> 
> A BITMIXER.IO, a [Bitcointalk.org](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093)-on bezárásáról szóló bejelentésben (kiemelés az eredetiben). 

… Mostanra rájöttem, hogy a Bitcoin teljesen nyílt, nem névtelen rendszer, **így van megtervezve**. A blokklánc egy nagy nyitott könyv. 

… Mostanra rájöttem, hogy a Bitcoin teljesen nyílt, nem névtelen rendszer, **így van megtervezve**. A blokklánc egy nagy nyitott könyv. 

A BITMIXER.IO, a [Bitcointalk.org](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093)-on bezárásáról szóló bejelentésben (kiemelés az eredetiben). 

Néhány héttel később, miután átgondolta a különböző adatvédelmi lehetőségeket, ezt mondta: 

> A mélyreható vizsgálat után megerősítem, hogy a MONERO a legjobb adatvédelmi valuta. Erősen ajánlom tehát a MONERO-t mindazoknak, akiknek extra magánéletre van szükségük. 
> 
> BITMIXER.IO, egy [későbbi bejegyzésben](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

A mélyreható vizsgálat után megerősítem, hogy a MONERO a legjobb adatvédelmi valuta. Erősen ajánlom tehát a MONERO-t mindazoknak, akiknek extra magánéletre van szükségük. 

A mélyreható vizsgálat után megerősítem, hogy a MONERO a legjobb adatvédelmi valuta. Erősen ajánlom tehát a MONERO-t mindazoknak, akiknek extra magánéletre van szükségük. 

BITMIXER.IO, egy [későbbi bejegyzésben](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Mivel az összes Bitcoin-tranzakció látható a blokkláncon, MINDEN Bitcoin-tranzakció nyomon követhető. Egy Bitcoin-keverő nagymértékben elhomályosíthatja a tranzakciókat, ami megnehezíti a Bitcoinok követését, de nem teszi lehetetlenné. A technológia fejlődésével és a Bitcoin-tranzakciók nyomon követésére szakosodott vállalatok terjedésével, az korábban erőszen homályos tranzakciók viszonylag könnyen nyomon követhetők lesznek: 

  * [ A bűnüldöző szervek továbbra is fektetnek Bitcoin nyomkövetési szolgáltatásokba](https://news.bitcoin.com/law-enforcement-continues-invest-bitcoin-tracking-services/)
  * [ Time.com: A bitcoint könnyebb követni, mint gondolná](http://time.com/3689359/bitcoins-track-anonymous/)
  * [Elliptic: Bitcoin bűnüldözési célú nyomon követésére szakosodott vállalat](https://www.elliptic.co/)

Egy Google-keresés a fentiekhez hasonló cikkek tucatjait tárja fel. Ne feledje, minden olyan tranzakció, amely a múltban valamikor megtörtént, a blokkláncon megmarad, és követhető lehet, még akkor is, ha keverési szolgáltatást használtak. Valójában egy keverési szolgáltatás használata valószínűleg még jobban fel is hívja a figyelmet ezekre a tranzakciókra. 

Nem minden bitcoin egyenlő és egyforma értékű. Némelyik Bitcoint több szereplő feketelistára tett és blokkolt, így ezek kevésbé értékesek, mint a többi. Ha olyan Bitcoint kap, amelyet korábban illegális célokra használtak fel, akkor bitcoinjai feketelistán lehetnek, akkor is, ha semmi köze nem volt az eredeti tevékenységhez. Vagy mondjuk egy kormány, munkáltató vagy egyéb szervezet úgy dönt, hogy a jövőben feketelistára teszi a bitcoinjait, hasonlóan az eszközök befagyasztásához vagy elkobzásához. Nem tudna mit tenni. Mivel egy mixer csak a Bitcoinok nyomon követését nehezíti meg, ez a kategória „nem helyettesíthető”-ként lett megjelölve.

  * Andreas Antonopoulos, a Bitcoin Core volt fejlesztője, aki nagy tiszteletnek örvend a Bitcoin és más kriptovaluta közösségekben, elismeri a Bitcoin helyettesíthetőségi problémáját egy [ YouTube-videóban](https://www.youtube.com/watch?v=ak1iojpiHpM&feature=youtu .be&t=33m9s). 
  * Vita a Bitcoin helyettesíthetőségi problémájáról a [Bitcointalk.org oldalon](https://bitcointalk.org/index.php?topic=1190707.0)

## Összefoglaló

Véleményünk szerint a Monero az egyértelmű választás, ha privát, biztonságos, nyomon követhetetlen, helyettesíthető egységekből álló, decentralizált kriptovalutát keres, amelyhez nem szükséges felhasználói hozzáértés a megbízható beállításra. Bármi más kockára teszi magánéletét és biztonságát. De ne fogadja el a véleményünket. járjon utána, és győződjön meg róla a saját szemével. Vegye figyelembe, hogy a Monerot olyan szervezetek is támogatják és használják, amelyeknek a privát működés és a követhetetlenség létkérdés, például: 

  * [ SIGAINT ](https://www.reddit.com/r/Monero/comments/4xqrzd/sigaint_launches_tor_monero_node_as_its_operators/)
  * [ Purism ](https://puri.sm/posts/purism-collaborates-with-cryptocurrency-monero-to-enable-mobile-payments/)
  * [ Wikileaks ](https://shop.wikileaks.org/donate#db9)
  * Az AlphaBay Marketet (AB) 2017 júliusában lekapcsolták. Az AB ellen benyújtott [ Federal Forfeiture Complaint [Szövetségi Elkobzási Feljelentés] ](https://assets.documentcloud.org/documents/3898109/AlphaBay-Cazes-Forfeiture-Complaint.pdf) a következő részleteket tartalmazza: 
    * **A Monero az egyetlen privát és követhetetlen kriptovaluta:**  
"CAZES pénztárcái és számítógépes ügynökei összesen körülbelül 8 800 000 dollár értékű Bitcoin, Ethereum, Moreno [sic] és Zcash felett rendelkeztek, a következő bontásban: 1605,0503851 Bitcoin, 8309,271639 ETH, 3691,98 ZEC _és ismeretlen mennyiségű Monero._ " (20. oldal alja és 21. oldal teteje, kiemelés tőlem) 
    * **A Bitcoin-tranzakciók nem magánjellegűek, és nyomon követhetők:**  
"A szövetségi ügynökök azután szerezték meg a végzést, miután számos, az AlphaBay-ről származó Bitcoin-tranzakciót tudtak digitális valutaszámlákhoz, végül bankszámlákhoz és egyéb tárgyi eszközökhöz kötni, amelyek CAZES és felesége birtokában voltak." (17. o., 24-26. sor)) 

  * **A Monero az egyetlen privát és követhetetlen kriptovaluta:**  
"CAZES pénztárcái és számítógépes ügynökei összesen körülbelül 8 800 000 dollár értékű Bitcoin, Ethereum, Moreno [sic] és Zcash felett rendelkeztek, a következő bontásban: 1605,0503851 Bitcoin, 8309,271639 ETH, 3691,98 ZEC _és ismeretlen mennyiségű Monero._ " (20. oldal alja és 21. oldal teteje, kiemelés tőlem) 
  * **A Bitcoin-tranzakciók nem magánjellegűek, és nyomon követhetők:**  
"A szövetségi ügynökök azután szerezték meg a végzést, miután számos, az AlphaBay-ről származó Bitcoin-tranzakciót tudtak digitális valutaszámlákhoz, végül bankszámlákhoz és egyéb tárgyi eszközökhöz kötni, amelyek CAZES és felesége birtokában voltak." (17. o., 24-26. sor)) 

A LocalMonero nem támogat és nem bátorít semmilyen illegális tevékenységet 

A LocalMonero nem támogat és nem bátorít semmilyen illegális tevékenységet 

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

További olvasnivaló