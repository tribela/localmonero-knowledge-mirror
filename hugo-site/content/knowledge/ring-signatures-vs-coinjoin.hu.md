---
title: "A Monero gyűrűs aláírásai kontra CoinJoin, mint a Wasabiban"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Mivel a Bitcoin adatvédelmi eszközei egyre nagyobb figyelmet kapnak elterjed a használatuk, egyre komolyabb szabályozási ellenőrzés alá kerülnek. Ez figyelem egy [közelmúltbeli bejelentéshez](https://twitter.com/wasabiwallet/status/1503091503207432193) vezetett az egyik eszköz, a Wasabi Wallet részéről, miszerint elkezdik cenzúrázni és elutasítani az általuk tiltottnak tartott vagy az Általános Szerződési Feltételeikbe ütköző bemeneteket, és fizetni fognak egy láncelemző cégnek a mix bejövő résztvevőinek „átvilágítására”.

A CoinJoin tranzakciók használata a Bitcoin pénzeszközök eredetének elhomályosítására már évek óta a Bitcoin adatvédelmének alapja, és a használatában rejlő problémák és kockázatok azok az alapvető gondok, amelyeket a Monero gyűrűs aláírásai javítani vagy megelőzni hivatottak. 

Ebben a blogbejegyzésben röviden összehasonlítjuk a CoinJoint és a gyűrűs aláírásokat, valamint azt, hogy a Monero által alkalmazott megközelítés miért vezet erősebb cenzúraálláshoz, jobb adatvédelemhez és kevesebb bosszúsághoz a felhasználók számára.

## Mi az a CoinJoin tranzakció?

## Mi az a CoinJoin tranzakció?

Mivel a Bitcoin protokollon minden tranzakció teljesen nyilvános – megmutatva a feladót, a címzettet és az összeget – a felhasználóknak további lépéseket kell tenniük, hogy megőrizzék magánszférájukat a korábbi feladókkal és jövőbeni címzettekkel szemben, vagy kénytelenek a cenzúrát, megfigyelés vagy fizikai erőszak kockázatát vállalni.

A bitcoin adatvédelemre a ma elérhető legjobb megoldás az ún. ['CoinJoin'](https://bitcoiner.guide/qna/coinjoin/), ahol 2 vagy több felhasználó együttesen (általában egy központi koordinátoron keresztül), hoz létre egy speciális tranzakciót, amely megnehezíti a külső szemlélők számára, hogy összekapcsolják a kimeneteket a bemenetekkel. A tranzakció létrehozásához a résztvevők olyan módon dolgoznak össze, hogy eközben a forrásaikat ne kelljen megőrzésre átadni harmadik félnek. A tranzakció lebonyolítása után a kimenetek története külső szemlélők számára átláthatatlanná (vagy legalábbis zavarosabbá) válik-

Ezzel megszakad az egyes UTXO-k követhetősége, lehetővé téve a Bitcoin-felhasználók számára, hogy egy csepp forward secrecy-t biztosítsanak maguknak a tranzakciók során. A CoinJoin (ahogyan a Wasabi Wallet és a Samourai Wallet - az erre a célra leggyakrabban használt két eszköz - megvalósítja) azonban jelentős hátrányokkal bír: 

  * Mivel a CoinJoin tranzakciók teljes mértékben önkéntesek, és aktív erőfeszítést igényelnek, minden résztvevő szükségszerűen világgá kürtöli, hogy nagyobb diszkrécióra törekszik, mint a „normál” Bitcoin-felhasználók, ami potenciálisan kiemeli őket a tömegből, és a legtöbb szabályozott tőzsdén vagy platformon gondot okozhat. A felhasználók nem tudják letagadni, hogy CoinJoin tranzakcióban vettek részt.
  * Annak érdekében, hogy partnereket találjanak a CoinJoinhoz, a legtöbb megvalósítás (beleértve a Wasabi Walletet is) egy központi koordinációs mechanizmust használ, amely összeköti a résztvevőket, segítve őket a kommunikációban és a megfelelő CoinJoin tranzakció kialakításában. Bár ez a központi entitás soha nem kezeli a felhasználók pénzét, de kiterjedt betekintést nyer az általuk koordinált tranzakciókba, cenzúrázhatja a bejövő adatokat (mint a Wasabi Wallet esetében), és nyomást gyakorolhatnak rá a CoinJoin résztvevőivel kapcsolatos információk begyűjtésére vagy megosztására.
  * Azoknak a felhasználóknak, akiknek nagy összegű pénzük van a CoinJoinhoz, gyakran órákat (vagy akár napokat!) kell várniuk, hogy elegendő résztvevőt találjanak egy CoinJoinhoz, ami nagy késésekhez vezet attól az időponttól kezdve, amikor a felhasználó pénzt kap, egészen addig, amíg el tudja azokat költeni privát módon . 
  * A CoinJoin-tranzakciók által biztosított védelem idővel leromlik, ahogy a többi résztvevő pénzt költ, vagy kimeneteket személyazonosságukhoz kötik KYC-tőzsdéken, azonosítást igénylő kereskedőknél, stb. Ez azt jelenti, hogy a felhasználóknak folyamosan forgatni kell a forrásaikat, hogy anonimitásukat a lehető legfrissebben tartsák (meglegyen a szükséges „tömeg, amiben el lehet bújni”).
  * A legtöbb esetben a CoinJoin résztvevőinek fix méretű UTXO-kat (pl. 0,1 BTC-t) kell használniuk, hogy megnehezítsék a tranzakció be- és kimeneteinek összekapcsolását. Ez magasabb díjakhoz vezet (több külön tranzakció szükséges egy nagy bemenethez), több „mérgező apró”-hoz (a diszkráció komoly kockáztatása nélkül elkölthetetlen források), és megakadályozhatja, hogy a kisebb felhasználók vegyíthessenek, ha nincs meg a szükséges minimális egyenlegük.

## Hogyan oldják meg ezeket a problémákat a gyűrűs aláírások?

## Hogyan oldják meg ezeket a problémákat a gyűrűs aláírások?

Mivel korábban [alaposan megvizsgáltuk a gyűrűs aláírásokat](/knowledge/ring-signatures), ebben a bejegyzésben nem megyek bele a működésük technikai részleteibe. Ehelyett nézzük meg, hogy a Monero által alkalmazott megközelítések hogyan kerülik meg a CoinJoin fent tárgyalt problémáit.

> A CoinJoin választható és aktív részvétel szükséges hozzá

A CoinJoin választható és aktív részvétel szükséges hozzá

A gyűrűs aláírás a Monero adatvédelmi protokoll alapvető tulajdonsága, és _a hálózat összes_ tranzakciója használja. Ez azt jelenti, hogy egyetlen felhasználó tranzakciója sem tűnik ki azzal, hogy nagyobb adatvédelemre törekszik, mint a „normál” Monero-felhasználók, és minden felhasználó hihetően tagadhatja, hogy pénzeszközöket költött egy adott tranzakció során. Mivel a pénzeszközöket elköltő felhasználó nem vesz részt a csali bemenetek eredeti tranzakcióiban és nem egyeztet velük, azok a felhasználók, akiknek a bemenetei csaliként kiválasztásra kerülnek őszintén mondhatják, hogy nem vettek részt a tranzakcióban, ezzel erősítve adatvédelmüket.

> Központosított koordinátor használata

Központosított koordinátor használata

Mivel a Monero gyűrűs aláírásai nem koordináltak, és csak a valódi pénzköltőre van szükség a tranzakció létrehozásához, nincs szükség központi szervezésre. Ez biztosítja, hogy _senki_ nem tagadhatja meg Öntől a Monero adatvédelméhez való hozzáférést, és nincs központi entitás, amelyre nyomást lehet gyakorolni, nem lehetséges egyszerű Sybil-támadás a likviditás ellen, stb. Mindaddig, amíg a tranzakció kifizeti a hálózati díjat, cenzúrázhatatlan hozzáférést kap a magánélethez, a biztonsághoz és a névtelenséghez.

> A CoinJoinhoz likviditás kell

A CoinJoinhoz likviditás kell

A „likviditás”, amely mindenki számára elérhető, akinek csalikra van szüksége, mindig a láncon lévő kimenetek teljes készlete, így soha nem lesz hiány csaliból, amik között a Monero tranzakció megbújhat. Ha valaki Monerot akar elkölteni, azt a pénz beérkezése után körülbelül 20 perccel megteheti, és nem kell további lépéseket tennie ahhoz, hogy erős adatvédelmet élvezzen.

> A CoinJoin adatbiztonsága idővel gyengül

A CoinJoin adatbiztonsága idővel gyengül

Mivel a Monero kimenetei soha nem nyilvánosan ismertek a hálózaton, a gyűrűs aláírások által biztosított adatvédelem sokkal kevésbé hajlamos az idő múlásával történő romlásra. A felhasználónak nem kell állandóan forgatnia a Monero kimeneteket, és rendkívül ritka körülményeket leszámítva az idő múlásával sem veszít pénzügyei magánjellegéből.

Ha a felhasználó mégis szeretné „frissíteni” a kimenettel használt csalikat, akkor egyszerűen elküldheti önmagának az összeget, és a szokásos módon ~20 perccel később el tudja költeni.

> A CoinJoin rendszerint fix méretű bemeneteket igényel

A CoinJoin rendszerint fix méretű bemeneteket igényel

Mivel a [„Bizalmas tranzakciók”](/knowledge/monero-ringct) (a „RingCT” része) használatával az összegek minden tranzakcióban el vannak rejtve, az adott tranzakcióban használt csali bármilyen méretű lehet. Nem kell aggódni a mennyiségalapú heurisztikák miatt, így a tranzakciók sokkal egyszerűbben felépíthetők, és a Monero blokkláncon bármely időpontból tetszőleges összegű csalikkal használhatók.

## Hogyan tudhatok meg többet?

## Hogyan tudhatok meg többet?

Ha kíváncsi, és szeretné jobban megérteni a gyűrűs aláírásokat vagy a CoinJoin tranzakciókat, tekintse meg az alábbi linkeket, nagyszerű helyek a kezdéshez:

  * [Hogyan rejtik el a gyűrűs aláírások Monero kimeneteit](/knowledge/ring-signatures)
  * [Ring Signature – Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html) (angol)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/) (angol)
  * [CoinJoin Overview](https://6102bitcoin.com/coinjoin-overview/) (angol)

További olvasnivaló

  * [A Monero egyedülálló módon teszi lehetővé a körkörös gazdaságokat](/knowledge/monero-circular-economies)/

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

  * [Miért jobb a Monero, mint a Dash, a Zcash, a Zcoin (még Lelantussal is), a Grin és a Bitcoin mixerek, mint a Wasabi (Frissítve 2020 májusában)](/knowledge/why-monero-is-better)/

További olvasnivaló