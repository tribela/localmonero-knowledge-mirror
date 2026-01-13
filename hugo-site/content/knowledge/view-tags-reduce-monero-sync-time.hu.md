---
title: "Nézetcímkék: Hogyan csökkenti egy byte adat a Monero tárcák szinkronizálási idejét 40+%-kal"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Az egyik leggyakoribb panasz a Monero mindennapi használatával kapcsolatban, hogy mennyi időbe telhet a pénztárca szinkronizálása, mielőtt Monerot tudna küldeni. Szerencsére a Monero közösség fejlesztői és kutatói remek módszert találtak arra, hogy több mint 40%-kal csökkentsék a pénztárca szinkronizálásához szükséges időt további blokkméret-felfúvódás és díjak nélkül.

Jönnek a nézeti címkék (view tag), egy bájtot hozzáadva az minden tranzakció adataihoz – a következő hálózatfrissítéssel érkezik!

## Miért lassabb egy Monero pénztárca szinkronizálása, mint a Bitcoiné?

Az egyik első kérdés, amit meg kell válaszolnunk, hogy jobban megértsük az olyan megoldások szükségességét, mint a nézetcímkék, hogy miért lassabb egy Monero pénztárca szinkronizálása, mint a Bitcoiné.

A Bitcoin láncon, mivel minden tranzakció nyilvános, és felfedi az elköltött összegeket és a címeket, a Bitcoin pénztárcák egyszerűen megkereshetik az el nem költött tranzakciós kimeneteket (UTXO-kat) vagy a felhasznált címeket, gyorsan átkutatva a blokkláncot, csak az adott címekhez tartozó UTXO-kat átvizsgálva, hogy megtudják, melyik tartozik a pénztárcájához, és melyiket lehet elkölteni.

A Monero esetében azonban minden tranzakció titkosítja a felhasználó adatait azáltal, hogy elrejti a feladót, a címzettet és az egyes tranzakciókban érintett összegeket. Ez az adatvédelem, bár létfontosságú a hálózat felhasználóinak védelme szempontjából, a pénztárca lassabb szinkronizálását is eredményezi. A Monero pénztárcának meg kell vizsgálnia a hálózaton található összes tranzakciós kimenetet (TXO) a pénztárca privát kulcsaival.

Ez sok bonyolult matematikai és kriptográfiái műveletet igényel annak igazolására, hogy a kimenet valóban a felhasználóhoz tartozik, mivel minden összeg, cím, és elköltött kimenet rejtve van a Monero láncon.

## Mik a nézetcímkék?

A Monero pénztárcák szinkronizálási idejének csökkentése érdekében [egy UkoeHB nevű kutató új megközelítést dolgozott ki](https://github.com/monero-project/research-lab/issues/73) – minden tranzakcióhoz hozzáadunk egy byte-nyi „címkét” egy közös titok használatával, amit csak az adott tranzakció feladója és fogadója ismer.

Ezt a megosztott titkot a feladó generálja a fogadó által megadott cím alapján, és nem igényel aktív együttműködést a küldő és a fogadó részéről. A megosztott titok első byte-ja (vagy karaktere) ezután hozzáadódik a tranzakció adataihoz, amikor közzéteszik a Monero hálózaton.

Amikor a tranzakció egyik résztvevője szinkronizálni akarja a Monero blokkláncot a későbbiekben, ahelyett, hogy az összes bonyolult matematikai és kriptográfiai műveletet végre kellene hajtania a hálózat minden egyes TXO-ján, a pénztárcának így már csak ezt az 1 byte-os mezőt kell ellenőriznie minden tranzakcióban, és csak azokon a tranzakciókon végrehajtani az időigényes ellenőrzést, amelyek a megfelelő címkével rendelkeznek – pontosabban a tranzakciók 1/256-od részén!

Ez a címke nem árul el semmilyen információt a tranzakcióról a külső szemlélők számára, csupán 1 byte-ot (elhanyagolható mennyiséget) ad hozzá a tranzakciók méretéhez, mégis lehetővé teszi számunkra, hogy a szinkronizálási időket 40%-ot meghaladó mértékben javítsuk az összetett ellenőrzések számának csökkentésével!

## Nézetcímkék: egyszerűsített példa

Képzeljen el egy szobát, amiben 4096 doboz van, amelyből csak 5 a sajátja. A dobozok kívülről megkülönböztethetetlenek, és csak úgy lehet megállapítani, hogy hozzánk tartozik-e, ha kinyitjuk, és megoldjuk a benne található időigényes matematikai feladatot.

Most képzeljük, hogy úgy döntöttünk, hogy aki ezt az 5 dobozt küldi, generáljon egy speciális kódot a címünk alapján, majd a generált kódnak az első karakterét írja rá minden nekünk küldött doboz külsejére. Mindenki más ugyanígy tesz a saját dobozaival (annak érdekében, hogy az összes doboz továbbra is megkülönböztethetetlen legyen), de most egyszerűen megnézhetjük a doboz külső oldalán található egykarakteres kódot, és csak azokat a dobozokat kell kinyitni, amelyeken ez a karakter szerepel. 

Ugyan előfordul, hogy más dobozokon is ugyanaz a karakter van, pedig nem nekünk címezték, de most már csak 16 (1/256 doboz!) dobozt kell kinyitnunk és a feladatot kiszámolnunk az eddigi 4096 helyett. 

Így 16 dobozt nyitunk ki, megoldjuk a feladatokat, és megtartjuk azt az 5 dobozt, amely valóban a miénk a csoportból!

## Mikor lesznek elérhetők a megtekintési címkék Moneroban?

A nézetcímkék egy [közelgő hálózati frissítésben](https://github.com/monero-project/meta/issues/630) tervezett funkciók egyike, valamikor tavasszal fognak megjelenni. A [ közösség összegyűjtött 23.3XMR-t](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (a cikk írásakor), hogy ösztönözze a nézetcímkék fejlesztését és implementálását, ennek eredményeként a nézetcímkék Monero kódbázisba beépítéséhez szükséges munka túlnyomó többségét j-berman már el is készítette felülvizsgálókkal és kutatókkal együttműködésben.

Amint a hálózaton kötelezőek lesznek a nézetcímkék, a frissítés után küldött összes tranzakció részesülni fog a drasztikusan javuló szinkronizálási időből. Nem kell semmi különöset tennie a nézetcímkék használatához, a kedvenc Monero pénztárcája egyszerűen használni fogja őket a hálózat frissítése után!

## Hogyan tudhatok meg többet?

Ha ez felkeltette az érdeklődését a nézetcímkék iránt, tekintsen meg néhány további linket, amelyek a témával foglalkoznak (angol):

  * [Reduce scan times with 1-byte-per-output ‘view tag’](https://github.com/monero-project/research-lab/issues/73)
  * [Add view tags to outputs to reduce wallet scanning time](https://github.com/monero-project/monero/pull/8061)

További olvasnivaló

  * [A Monero egyedülálló módon teszi lehetővé a körkörös gazdaságokat](/knowledge/monero-circular-economies/)

  * [A Monero gyűrűs aláírásai kontra CoinJoin, mint a Wasabiban](/knowledge/ring-signatures-vs-coinjoin/)

  * [Miért (és hogyan!) érdemes a kulcsokat saját kézben tartani](/knowledge/hold-your-keys/)

  * [Hozzájárulás a Monerohoz](/knowledge/contributing-to-monero/)

  * [Hogyan befolyásolják a távoli csomópontok a Monero adatbiztonságát](/knowledge/remote-nodes-privacy/)

  * [Hogyan használja a Monero a hard forkokat a hálózat frissítéséhez](/knowledge/network-upgrades/)

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

  * [Monero bevált módszerek kezdőknek](/knowledge/monero-best-practices/)

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