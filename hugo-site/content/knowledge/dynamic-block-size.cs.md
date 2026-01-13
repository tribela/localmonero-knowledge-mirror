---
title: "Jak Monero vyřešilo problém velikosti bloku, který sužuje bitcoiny"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Poznámka:** Důrazně doporučujeme, aby si čtenář přečetl naše články [„Proč má Monero koncovou emisi“](/knowledge/monero-tail-emission) a [„Těžba Monero: Co dělá RandomX tak speciální“](/knowledge/monero-mining-randomx). Tento článek staví na konceptech zde uvedených._

Kdykoli jednotlivci diskutují o problémech s blockchainem, jedním z prvních slov, které se objeví, bude „škálování“. Není tajemstvím, že blockchainy se špatně škálují, ale většina lidí neví proč.

Pravdou je, že škálování je ve skutečnosti zastřešující pojem, který pokrývá dvě různé kategorie: Podpora protokolu a technologická podpora v daném okamžiku. V tomto článku zaměříme svou pozornost na jeden, podpora protokolu je v podstatě měřítkem toho, kolik transakcí protokol dokáže v daném čase zpracovat.

Bitcoin má limit velikosti bloku, což znamená, že jakmile je v bloku zahrnuto dostatečné množství transakcí, jakékoli další transakce budou muset čekat ve frontě na další blok. Užitečnou analogií by bylo uvažování o vlaku. Vlak přijíždí ke stanici a ti, co jsou na řadě, se zařadí dovnitř. Jakmile bude vlak plný, kdokoli, kdo zůstane venku, bude muset čekat na další.

Bitcoin používá poplatky k určení, kdo se do bloku dostane nebo ne. Když se vrátíme k analogii s vlakem, lze si představit, že jeden potenciální cestující, který má být opuštěn, nabídne strojníkovi pět dolarů, aby mu dal místo. Ostatní pasažéři následují příklad a nakonec dojde k nabídkové válce o to, kdo dostane která místa. Je na řidiči, aby se rozhodl, zda chce dodržet zásadu „kdo dřív přijde, je dřív na řadě“, ale je v jeho nejlepším finančním zájmu maximalizovat svůj příjem tím, že na palubu vezme ty nejvyšší nabídky.

V této analogii jsou horníci strojvedoucí. Mohou do bloku zahrnout jakékoli transakce, které chtějí, ale obecně si vyberou ty, které mají nejvyšší placené poplatky.

Alternativně, pokud bloky nejsou příliš plné, lidé nemají motivaci platit vysoké poplatky, protože je k dispozici spousta volných míst.

V době největšího rozmachu kryptoměn v roce 2017 byl bitcoin zaplaven transakcemi a poplatky raketově vzrostly pro ty, kteří chtěli být zahrnuti do dalšího bloku nebo do jakéhokoli bloku blízké budoucnosti. Ti, kteří nebyli ochotni platit vysoké poplatky, viděli, že jejich transakce byly posunuty o hodiny, dny nebo dokonce úplně vypadly z fronty.

Byl to otřesný pohled na to, jak by se Bitcoinu dařilo, kdyby se často hovořilo o „masové adopci“. Pokud by bitcoiny měly být používány masy, věci by byly ještě horší než v roce 2017 a bitcoiny by byly nedostupné pro kohokoli kromě bohatých, jednoduše proto, že propustnost je malá kvůli pevné velikosti bloku, což způsobí, že trh s poplatky převezme kontrolu. .

Monero to předvídalo a chtělo udělat něco jiného. Vývojáři Monera tedy implementovali dynamickou velikost bloků.

V zásadě má Monero také uzávěr velikosti bloku, ale je to měkký uzávěr. Když se řada čekajících transakcí příliš prodlouží, těžaři mohou zvětšit velikost bloků. S naší analogií vlaku si dokážete představit přidání dalších vlakových vozů, aby se vešly další cestující. Poté, co je fronta prázdná, se bloky zmenšují zpět na původní velikost.

Pokud se vám to zdá jako dobrý nápad, zdá se rozumné se ptát, proč je Monero jedinou kryptoměnou, která to implementovala. Proč to nepřidat na bitcoiny, aby se zastavily problémy s propustností?

Bohužel to není možné. Existuje několik důvodů a my se je pokusíme vysvětlit.

Vždy je v nejlepším zájmu těžaře mít velké bloky. S velkými bloky se vejdou do více transakcí a vydělají více peněz na poplatcích a také na odměnách za bloky. To může vést k spamovým útokům, kdy někdo zasílá mnoho malých transakcí s malými poplatky, čímž nafoukne řetězec. Miner's by jen zvýšil velikost bloku, aby je všechny zahrnoval, protože peníze jsou peníze, bez ohledu na to, jak malé jsou. To by vedlo k trvale velkým blokům s malým ekonomickým přínosem. Bitcoin to řeší umělým omezením velikosti bloku, čímž generuje trh s poplatky. Spamoví útočníci by museli přeplatit ostatní uživatele na poplatcích a to už není levné. To ale znamená, že se bloky zaplní a některé transakce čekají, jak je uvedeno výše.

Jak tedy může mít Monero dynamické velikosti bloků, ale vyhnout se útokům spamu? Odpověď je jednoduchá, ale chytrá. Je zavedena pokuta na odměnu za blok, když je blok větší než normálně. Pokud chce těžař zvětšit velikost bloku, odměna, kterou dostane za nalezení tohoto bloku, bude menší, než by jinak obdržel. Velikost bloků tedy zvýší pouze tehdy, když zaplacené transakční poplatky uživatelů převáží ztracenou část odměny za blokování. Pokud by například těžař ztratil 0,5 XMR zvýšením velikosti bloku a součet zaplacených transakčních poplatků by byl 0,4 XMR, pak by došlo k čisté ztrátě 0,1 XMR, pokud by zvětšili velikost, tj. by to nedělali. Naopak, pokud by celkové transakční poplatky dosáhly 0,7 XMR, pak by byl čistý zisk 0,2 XMR, i když ztratí 0,5 XMR z pokuty za blokovou odměnu, takže těžař raději zvětší velikost.

Tyto dynamické bloky umožňují, aby síť organicky rostla, aniž by se aritificky omezovala velikost bloků, aby se vytvořil trh s vynucenými poplatky, a přitom se stále vyhýbají útokům spamu. Existuje několik dalších úhlů pohledu, ze kterých můžeme na tuto myšlenku nahlížet, a více důvodů, proč by nebylo možné přidat do bitcoinu, ale prozatím doufáme, že čtenář chápe, jak Monero obchází několik problémů v bitcoinech a jeho deriváty a jak plánuje rozšířit svou propustnost do budoucna.

Další čtení

  * [Jak Monero jedinečně umožňuje cirkulární ekonomiky](/knowledge/monero-circular-economies)/

  * [Monerové kruhové podpisy vs CoinJoin jako ve Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Proč (a jak!) byste měli držet své vlastní klíče](/knowledge/hold-your-keys)/

  * [Přispíváme zpět do Monera](/knowledge/contributing-to-monero)/

  * [Jak vzdálené uzly ovlivňují soukromí Monero](/knowledge/remote-nodes-privacy)/

  * [Jak Monero používá hard-forky k upgradu sítě](/knowledge/network-upgrades)/

  * [Značky zobrazení: Jak jeden bajt zkrátí dobu synchronizace peněženky Monero o více než 40 %](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool a jeho role v decentralizaci těžby Monera](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Co to udělá pro Monero](/knowledge/seraphis-for-monero)/

  * [Je převod bitcoinu na monero stejně soukromý jako přímý nákup monera?](/knowledge/most-private-way-to-buy-monero)/

  * [Proč Monero na rozdíl od Zcash používá bezdůvěryhodné nastavení](/knowledge/monero-trustless-setup)/

  * [Proč je Monero lepší uchovatel hodnoty než bitcoin](/knowledge/monero-better-store-of-value)/

  * [Jak může Monero překonat síťové efekty Bitcoinu](/knowledge/network-effect)/

  * [Proč má Monero komunitu nejkritičtějšího myšlení](/knowledge/critical-thinking)/

  * [Podvody, na které si dát pozor při používání Monero](/knowledge/monero-scams)/

  * [Jak budou fungovat atomové swapy na Moneru](/knowledge/monero-atomic-swaps)/

  * [Co by měl každý uživatel Monero vědět, pokud jde o vytváření sítí](/knowledge/monero-networking)/

  * [Jak RingCT skrývá částky transakcí Monero](/knowledge/monero-ringct)/

  * [Jak skryté adresy Monero chrání vaši identitu](/knowledge/monero-stealth-addresses)/

  * [Jak subadresy Monero zabraňují propojení identity](/knowledge/monero-subaddresses)/

  * [Vysvětlení výstupů Monero](/knowledge/monero-outputs)/

  * [Osvědčené postupy pro začátečníky s Monero](/knowledge/monero-best-practices)/

  * [Jak kruhové podpisy zakrývají výstupy Monera](/knowledge/ring-signatures)/

  * [Jak CLSAG zlepší efektivitu Monero](/knowledge/what-is-clsag)/

  * [Proč má Monero ocasní emise](/knowledge/monero-tail-emission)/

  * [Stručná historie Monera](/knowledge/monero-history)/

  * [Wired Magazine se o Moneru mýlí, tady je důvod](/knowledge/wired-article-debunked)/

  * [15 vyvrácených mýtů a obav o Monero](/knowledge/monero-myths-debunked)/

  * [Jak Dandelion++ uchovává původ transakcí Monero v soukromí](/knowledge/monero-dandelion)/

  * [Proč je Monero open source a decentralizované](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: Co dělá RandomX tak výjimečným](/knowledge/monero-mining-randomx)/

  * [Proč je Monero lepší než Dash, Zcash, Zcoin (i s Lelantusem), Grin a bitcoinové mixéry jako Wasabi (aktualizováno květen 2020)](/knowledge/why-monero-is-better)/

Další čtení