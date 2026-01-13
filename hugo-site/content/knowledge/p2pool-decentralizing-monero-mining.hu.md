---
title: "A P2Pool és szerepe a Monerobányászat decentralizálásában"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
A Monero projekt egyik fő célja egy tisztességes, decentralizált és biztonságos hálózat megteremtése a proof-of-work (PoW) bányászat új és innovatív megközelítésein keresztül, amely ma a kriptovaluta hálózatok biztosításának legfontosabb módja.

Bár a különleges bányászati algoritmus [, mint a RandomX](/knowledge/monero-mining-randomx), rendkívül fontos eleme a cél megvalósításának – mivel garantálja, hogy bárki, aki rendelkezik számítógéppel, érdemben hozzájárulhasson a hálózat biztosításához – nem előzi meg a pool miningból fakadó problémákat. A pool mining messze a legelterjedtebb módja a kriptovaluták bányászatának, a Monero esetében is, szerencsére a p2pool bányászat megjelenése miatt ez hamarosan megváltozhat.

## Mit jelent a pool mining?

## Mit jelent a pool mining?

A pool mining egy megoldás arra, hogy a bányászok megosszák a feladatot, ami egy blokk megoldásához kell a hálózaton, egyenlően megosztva a jutalmat a megtalált blokkok után. Noha ez rendkívül sokat segít a bányászok fizetési gyakoriságának kiegyenlítésében az egyedi bányászatához képest, komoly központosítási problémákat vet fel.

Amikor a bányász hozzájárul a poolhoz, feladja az általa végzett munka és megtalált blokkok irányítását a poolnak, megbízva abban, hogy a bányászok között őszintén és méltányosan osztja meg a jutalmakat a bányászott mennyiség alapján. Ha minden jól megy, a pool üzemeltetője begyűjti a munkát minden bányásztól, elküldi a hálózatra, és egyenlő arányban osztja el a jutalmakat.

## Mi a probléma a pool mininggal?

## Mi a probléma a pool mininggal?

Sajnos ez teljes mértékben a bizalomra épül, és lehetővé teszi a pool üzemeltetője számára, hogy aljasságokat tegyen a bányászok által elvégzett munkával. Az üzemeltető felhasználhatja az elvégzett munkát a hálózat megtámadására, megkísérelheti források kétszeres elköltését (ha a pool elég nagy), vagy egyszerűen csak felhasználhatja a bányászok által végzett munkát a saját hasznára, nem jutalmazva megfelelően a bányászokat a munkájukért.

A hálózatot fenyegető legnagyobb kockázatot az jelenti, ha egy pool (vagy több együttműködésben) a hálózati hashrate több mint 51%-át irányítása alá vonja, mivel ezt csalásra és többszörös pénzköltésre használhatják fel, vagy megpróbálhatják megváltoztatni a hálózat szabályait.

## Mi az a p2pool?

## Mi az a p2pool?

p2pool egy olyan elképzelés, amelyet eredetileg Bitcoin bányászatához találtak ki 2011-ben, de soha nem terjedt el széles körben, és gyakorlatilag sehol nem használják a Bitcoin bányászatában. Szerencsére a RandomX egyik kulcsfontosságú fejlesztője, SCHernykh a nyaralását azzal töltötte, hogy megoldásokat találjon a Bitcoin p2pool implementációjával kapcsolatos problémákra, nulláról újraírva a programot.

A Monero p2pool bizalomnélküli módon teszi lehetővé a bányászok számára, hogy megosztott munkával blokkokat oldjanak meg és biztosítsák a Monero hálózatot a speciális p2pool csomópont használatával.

Ez egy saját blokklánc (ún. "oldallánc") segítségével történik, amely nyilvántartja az egyes bányászok által végzett munkát, a pénztárcák címét, és a keresett Monero mennyiségét, majd a jutalmat bizalommentes, elosztott módon fizeti ki. Mivel az oldalláncon jóval kevesebb bányász dolgozik, sokkal könnyeb blokkokat megtalálni és beküldeni rajta, mint a fő Monero hálózaton, így a bányászok könnyebben juthatnak stabil, egyenletes jutalomhoz, mintha egyedül dolgoznának.

## Hogyan oldja meg a p2pool a pool mining problémáját?

## Hogyan oldja meg a p2pool a pool mining problémáját?

A p2pool esetében nincs központosított pool, központi üzemeltető, vagy egyetlen személy, aki pénzeszközöket kezeli és a kifizetéseket kiosztja. A p2poolon keresztül bányászók által közösen végzett munkát a p2pool blokklánc és a többi csomópont-operátor ellenőrzi, hogy megbizonyosodjanak arról, hogy az érvényes, és amikor blokkot találnak minden bányász azonnali kifizetést kap az elvégzett munkájának megfelelően, közvetlenül a blokkért járó jutalmakból.

Amikor a bányászok a p2pool használatát választják a központosított megoldások helyett, megvonnak minden hatalmat és bizalmat a pool-üzemeltetőktől, és biztosítják, hogy a munkájuk hozzájáruljon a hálózat működéséhez, a jutalmukat biztosan megkapják, csökkentve a hálózati támadások és a munkájukkal visszaélés, vagy a nekik járó jutalom ellopásának kockázatát.

Ez nemcsak a saját érdekük, hanem csökkenti annak kockázatát is, amelyet a központosított bányászkészletek jelenthetnek a Monero hálózat egészére nézve. A p2pool használata szintén nagyban segít csökkenteni a kockázatot, amelyet a nemzetállamok vagy a szabályozó hatóságok jelenthetnek a hálózatra nézve, mivel nincsenek központosított entitások, nincs földrajzi koncentrációja a pooloknak, amelyekre nyomást gyakorolhatnak, vagy bármilyen más egyértelmű célpont amit a Monero ellen kihasználhatnak.

## Mik a hátrányai?

## Mik a hátrányai?

Szerencsére a Monero p2pool jól megtervezett és jól felépített, kiválóan működik! A p2pool bányászat fő hátránya azonban, hogy minden bányásznak, aki használni akarja, saját Monero csomópontot kell futtatnia, ami kicsit megnehezíti a folyamat elindítását. Ezt a csomópontot azonban ezután a blokkok felépítéséhez és ellenőrzéséhez szükséges összes információ kiszámításához is használja, biztosítja azt is, hogy a bányász teljes mértékben kézben tartsa az elvégzett munkát. Távoli csomópontként is használható a bányász saját pénztárcájához, hozzájárul a hálózat biztonságához és számos további előnye is van.

A másik lényeges különbség a központosított bányászathoz képest az, hogy a p2pool-t használó kicsi bányászoknak valamivel több "varianciája" lesz – vagyis a kifizetések közötti idő változatosabb, mint központi bányászatnál – de _rendkívül_ fontos megjegyezni, hogy ez nem jelent időegység alatt kevesebb bevételt! A p2pool kis bányászok számára ugyanolyan nyereséges, mint a központosított megoldások. Ezt a varianciát részben az is ellensúlyozza, hogy a p2pool alapértelmezetten 0%-os díjakkal működik, mivel nincs központi üzemeltető, akinek fizetni kell a szolgáltatásért!

## Hogyan kezdjem el?

## Hogyan kezdjem el?

Szerencsére, a Monero p2pool implementációjának kiváló tervezése és a közösség tagjainak erőfeszítései miatt, akik időt fordítottak a p2poolon történő bányászat egyszerűsítésére, az elindulás egyre könnyebb lesz az idő múlásával. Számos módja van a p2pool bányászat megkezdésének, de mivel a technikai részletek túlmutatnak a cikk keretein, az operációs rendszerétől függően nyissa meg a megfelelő hivatkozást (angol):

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## Hogyan tudhatok meg többet?

## Hogyan tudhatok meg többet?

Ha ez felkeltette a kíváncsiságát a p2pool bányászattal kapcsolatban, nézzen meg alább néhány további linket és magyarázatot a p2poolról, működéséről, és hogy mit jelent a Monero számára (angol):

  * [The official Github for p2pool](https://github.com/SChernykh/p2pool)
  * [The official docs on using p2pool](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool is now live](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, a "block explorer" of sorts for p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh: On his development of P2Pool a Decentralized XMR Mining Pool](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

További olvasnivaló

  * [A Monero egyedülálló módon teszi lehetővé a körkörös gazdaságokat](/knowledge/monero-circular-economies)/

  * [A Monero gyűrűs aláírásai kontra CoinJoin, mint a Wasabiban](/knowledge/ring-signatures-vs-coinjoin)/

  * [Miért (és hogyan!) érdemes a kulcsokat saját kézben tartani](/knowledge/hold-your-keys)/

  * [Hozzájárulás a Monerohoz](/knowledge/contributing-to-monero)/

  * [Hogyan befolyásolják a távoli csomópontok a Monero adatbiztonságát](/knowledge/remote-nodes-privacy)/

  * [Hogyan használja a Monero a hard forkokat a hálózat frissítéséhez](/knowledge/network-upgrades)/

  * [Nézetcímkék: Hogyan csökkenti egy byte adat a Monero tárcák szinkronizálási idejét 40+%-kal](/knowledge/view-tags-reduce-monero-sync-time)/

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

  * [Miért jobb a Monero, mint a Dash, a Zcash, a Zcoin (még Lelantussal is), a Grin és a Bitcoin mixerek, mint a Wasabi (Frissítve 2020 májusában)](/knowledge/why-monero-is-better)/

További olvasnivaló