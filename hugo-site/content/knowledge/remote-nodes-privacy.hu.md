---
title: "Hogyan befolyásolják a távoli csomópontok a Monero adatbiztonságát"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
A Monero egyik legnagyobb előnye más kriptovalutákkal szemben a láncon megvalósuló adatbiztonság, de gondolkozott-e már azon, hogy a Monero adatvédelme mennyire érvényesül, amikor távoli csomópontot használ? Mi történik, ha egy „könnyű pénztárcát” használ, mint amilyen a MyMonero?

Ebben a bejegyzésben bemutatjuk annak részleteit, ahogy a Monero kivételes adatvédelmet biztosít távoli csomópontok használatakor is, valamint azt is, hogy mire kell figyelni távoli csomópontok használatánál.

## Milyen funkciókat látnak el a Monero csomópontok?

Azok számára, akik kevésbé ismerik a Monero működését: a hálózat csomópontjait (vagyis szervereit) bárki futtathatja, ez lehetővé teszi a csomópont tulajdonosának – vagy másoknak, akikkel megosztja azt! – a blokklánc egy példányának szinkronizálását, és a másolat továbbítását a hálózatnak. Ezek a csomópontok ellenőrzik a hálózaton zajló összes tranzakciót, valamint az összes közzétett blokkot, és biztosítják, hogy mindegyik megfeleljen a konszenzusban meghatározott szabályoknak.

A másik funkció, amit a Monero csomópontok ellátnak, hogy biztosítják azokat az adatokat, amelyekre kedvenc Monero pénztárcájának szüksége van az Önhöz tartozó tranzakciók megfelelő ellenőrzéséhez és az új tranzakciók létrehozásához. Ezeket az adatokat a csomópontok két helyen biztosítják:

  * A lánc blokkjaihoz tartozó adatokat a pénztárca lekéri, átvizsgálja az Önhöz tartozó tranzakciókat, majd az ellenőrzés után eldobja a blokkokat. 
    * Ez a művelet hamarosan drasztikusan javulni fog a [nézetcímkéknek](/knowledge/view-tags-reduce-monero-sync-time) köszönhetően.
  * Tranzakciók küldésekor az Ön által használt csomópont szolgáltatja a lehetséges csalik (hamis bemenetek) listáját, amelyeket a tranzakció felépítésére használ, így biztosítva, hogy minden Monero elköltésekor elbújhasson a tömegben. 
    * Ezek a csalik a [gyűrűs aláírások](/knowledge/ring-signatures) részét képezik, ami fontos része Monero láncon történő adatvédelmének.

  * Ez a művelet hamarosan drasztikusan javulni fog a [nézetcímkéknek](/knowledge/view-tags-reduce-monero-sync-time) köszönhetően.

  * Ezek a csalik a [gyűrűs aláírások](/knowledge/ring-signatures) részét képezik, ami fontos része Monero láncon történő adatvédelmének.

## Mi a legprivátabb és legbiztonságosabb módja a Monero használatának?

A Monero által biztosított, távoli csomópontok használatakor is erős adatvédelem ellenére is a legjobb saját Monero csomópontot futtatni, hogy kéznél legyen a Monero blokklánc érintetlen példánya, és hogy az IP címe rejtve maradjon. A másik előnye a saját csomópont futtatának, hogy hozzájárul a hálózathoz, lehetővé teszi, hogy más csomópontok szinkronizáljanak az Önéről, vagy akár megengedheti nekik, hogy pénztárcájukkal csatlakozhazzak a csomóponthoz.

Ezt szem előtt tartva, a Monero akkor is kiváló adatvédelmet biztosít, ha távoli csomópontot használ. Ha érdeklődik saját Monero csomópontjának futtatása irant, itt található egy útmutató (angol): 

  * [Monero Node futtatása](https://sethforprivacy.com/guides/run-a-monero-node/)

## Mit tudhat meg rólam egy távoli csomópont?

Távoli csomópont használatakor van néhány kulcsfontosságú információ, amely a távoli csomópont számára hozzáférhetővé válik, és néhány fontos módja annak, ahogy a csomópont megtámadhatja Önt, pl megakadályozhatja a tranzakciók küldését, és így tovább.

Az első dolog, amit egy távoli csomópont megtud Önről, az a nyilvános IP-címe. Bár ezt remélhetőleg VPN-en vagy Toron keresztül rejtve marad, a távoli csomópont társíthatja a nyilvános IP-címét a tranzakcióhoz, megkönnyítve nekik, hogy leszűkítsék a tranzakció eredetének lehetséges helyét. A távoli csomópont azt is megtudhatja, hogy a pénztárca melyik blokkot szinkronizálta utoljára, ennek segítségével megalapozott feltételezésekkel élhet Önről, például, hogy mikor használja általában a Monerot, vagy mikor költött belőle utoljára. Ez különösen igaz, ha mindig ugyanarról az IP-címről érkezik (például otthonából). Az utolsó fontos tétel, amit a távoli csomópont megtudhat Önről, az a rajta keresztül küldött tranzakciók alapvető információi. Bár ezek a legtriviálisabb adatok, amelyeket a csomópont üzemeltetője megszerez Önről, fontos látni, hogy ezek felhasználhatók egy tranzakció feladójának azonosítására, ha ezeket az információkat más, láncon kívüli adatokkal kombinálják. Ez különösen veszélyes lehet, ha a távoli csomópontot rosszindulatú entitás, például egy blokklánc-elemző cég vagy egy elnyomó nemzetállam üzemelteti.

Egy távoli csomópont azzal is megkísérelhet problémát okozni, hogy blokkokat rejt el Ön elől, így a pénztárcája tévesen azt hiszi, hogy szinkronizálva van. Emiatt azt hiheti, hogy pénzeszközök vesztek el, vagy megakadályozhatja, hogy pénzt költsön, amíg nem csatlakozik másik csomóponthoz. Az utolsó, amit egy távoli csomópont tehet Ön ellen, hogy a pénztárcáját manipulált elterelőkimenetekkel látja el. Ez azt eredményezheti, hogy a pénztárcája nem lesz képes tranzakciót létrehozni (ami miatt nem tud pénzt elkölteni), vagy lehetővé teheti a távoli csomópont számára, hogy olyan terelőkimeneteket biztosítson, amelyekről tudja, hogy már elköltötték, így csökkentve az egyes tranzakciók során biztosított névtelenséget.

## Milyen adatvédelmi garanciák maradnak meg távoli csomópont használatakor?

Bár ez a cikk megijeszthette egy kicsit, fontos látni, hogy a Monero által biztosított adatvédelem még távoli csomópont használatakor is kimagasló, messze felülmúl minden más kriptovalutát, akkor is, ha így használjuk. Továbbra is élvezheti a Monero által biztosított erős adatvédelmet, mivel a távoli csomópont soha nem ismeri a valódi bemenetet (hogy mit költ el), a tranzakcióban elköltött Monero összegét vagy a tranzakció címzettjét. A külső megfigyelők sem láthatják a valódi bemenetet, az összeget vagy az érintett címeket (függetlenül attól, hogy milyen csomópontot használ!), biztosítva, hogy a távoli csomóponton kívül az Ön IP-címe, szinkronizálási információi és tranzakciói is erős adatvédelmi garanciákat élveznek.

A távoli csomópont továbbá soha nem fér hozzá az Ön által küldött vagy fogadott korábbi tranzakciókhoz, illetve a pénztárcájában jelenleg lévő Monero összegéhez, és elveszíti rálátását a tranzakcióira abban a pillanatban, amikor másik csomópontra vált. A távoli csomópont soha nem kap meg privát kulcsokat (sem a költési, sem a megtekintési kulcsokat), így a pénztárca privát és biztonságos marad. A csomóponttól függetlenül soha nem fenyegeti a Monero elvesztésének vagy ellopásának veszélye, mivel a csomópont nem tudja átírni a címzettet, soha nem fér hozzá a pénztárca privát kulcsaihoz, és semmilyen módon nem fér hozzá Monerojához.

## Mi a helyzet a „könnyű” pénztárcákkal, mint a MyMonero?

Bár a téma egy kicsit túlmutat ennek a cikknek a hatókörén, szeretnék a Monero tárcák különleges változatával foglalkozni – a könnyített pénztárcákkal. A könnyű pénztárca elnevezés onnan ered, hogy a pénztárcának (a telefonon vagy a számítógépen) nem kell végrehajtania a blokklánc szinkronizálását, így az élmény gyorsabb és gördülékenyebb.

Az ehhez hasonló pénztárcák azonban komoly adatvédelmi kompromisszummal járnak – a pénztárca elküldi a privát megtekintő kulcsát az Ön által használt távoli szervernek (ez az alapértelmezett a MyMoneroban), így a távoli szerver láthatja a kapott pénzeszközöket, pénztárcája létrehozása óta (és a jövőben is, amíg abba nem hagyja ennek a tárcának a használatát). Ez drasztikusan csökkenti a csomópont üzemeltetőjével szembeni adatvédelmet, ezért óvatosan kell eljárni.

Szerencsére a Monero közösség dolgozik azon, hogy javítson a szoftveren, hogy saját könnyű szerverét (LWS) futtathassa, így lehetővé téve a gyors szinkronizálást anélkül, hogy egy harmadik félre bízná privát megtekintő kulcsait – mivel Ön futtatja azt a szoftvert, amelynek a pénztárcája elküldi a privát kulcsait!

Ha többet szeretne megtudni erről, tekintse meg az alábbi Github repot:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Hogyan tudhatok meg többet?

Ha kíváncsi, és szeretné jobban megérteni a Monero csomópontok működését, szeretne egy távoli csomópontot használni vagy sajátot futtatni, tekintse meg az alábbi linkeket, nagyszerű forrásokat találhat a kezdéshez (angol):

  * [Monero World, a közösség által működtetett távoli csomópontok listája](https://moneroworld.com/#nodes)
  * [Seth For Privacy Monero csomópontjai , aki a cikk szerzője](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, gyakran ellenőrzött állapotú távoli csomópontok listája< /a>](https://monero.fail/)
  * [Hogyan kell csatlakozni egy távoli csomóponthoz a grafikus felületű tárcával](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia – Távoli Csomópontok](https://www.getmonero.org/resources/moneropedia/remote-node.html)

További olvasnivaló