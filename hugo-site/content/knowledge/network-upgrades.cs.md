---
title: "Jak Monero používá hard-forky k upgradu sítě"
slug: "network-upgrades"
date: "2022-02-10"
image: "/images/upgrades.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Jednou z nejčastěji nepochopených částí přístupu Monera k budování decentralizované, soukromí zachovávající a bezpečné kryptoměny je role, kterou hrají hard-forky (neboli upgrady sítě).

V tomto příspěvku si projdeme, co jsou hard-forky, proč jsou pro Monero důležité a jakou roli v nich můžete v budoucnu hrát.

## Proč Monero potřebuje síť neustále upgradovat?

Komunita Monero se zavázala k iteracím a vylepšování projektu v průběhu času a zdá se, že tento závazek spočívá ve dvou klíčových aspektech etiky komunity:

  1. Projekt Monero je v konečném důsledku software - kód - napsaný lidmi. To může vést k potřebě opravovat chyby, přidávat vylepšení, která jsou v průběhu času objevena nebo vynalezena, implementovat modernizace protokolu nebo jednoduše udržovat projekt. To je v mnoha ohledech podobné jako u jiných částí softwaru, které používáte (například prohlížeče, ve kterém čtete tento článek!), které je třeba neustále aktualizovat, aby bylo možné přidávat nové funkce a opravovat chyby.

  2. Projekt Monero je nástrojem pro ochranu soukromí a ochrana soukromí je neustále se rozvíjejícím závodem ve zbrojení. Lidé a skupiny, kteří by si nepřáli nic jiného než zbavit svět soukromí (finančního i osobního), neustále vylepšují, vyvíjejí a vymýšlejí nové způsoby, jak napadnout moderní přístupy k ochraně soukromí, jako jsou ty, které se používají v Moneru. Jakmile nepřátelé soukromí tyto nové přístupy najdou, musí se síť Monero umět přizpůsobit a zdokonalit, aby se mohla bránit a bránit naše právo na finanční soukromí.

Projekt Monero je v konečném důsledku software - kód - napsaný lidmi. To může vést k potřebě opravovat chyby, přidávat vylepšení, která jsou v průběhu času objevena nebo vynalezena, implementovat modernizace protokolu nebo jednoduše udržovat projekt. To je v mnoha ohledech podobné jako u jiných částí softwaru, které používáte (například prohlížeče, ve kterém čtete tento článek!), které je třeba neustále aktualizovat, aby bylo možné přidávat nové funkce a opravovat chyby.

Projekt Monero je nástrojem pro ochranu soukromí a ochrana soukromí je neustále se rozvíjejícím závodem ve zbrojení. Lidé a skupiny, kteří by si nepřáli nic jiného než zbavit svět soukromí (finančního i osobního), neustále vylepšují, vyvíjejí a vymýšlejí nové způsoby, jak napadnout moderní přístupy k ochraně soukromí, jako jsou ty, které se používají v Moneru. Jakmile nepřátelé soukromí tyto nové přístupy najdou, musí se síť Monero umět přizpůsobit a zdokonalit, aby se mohla bránit a bránit naše právo na finanční soukromí.

## Co je to hard-fork?

Složitost aktualizace Monera se projeví, jakmile pochopíte, jak moc se liší aktualizace kryptoměny od pouhého spuštění aktualizace softwaru v něčem, jako je prohlížeč.

V kryptoměnách se na pravidlech sítě (například na tom, jak mají vypadat transakce, jak funguje těžba a jak se ověřuje každý blok) musí shodnout celá síť, což se nazývá "konsensus". Když je třeba některá z těchto pravidel změnit nebo aktualizovat, musí se síť dohodnout na nových pravidlech, což způsobí "hard-fork" - situaci, kdy se síť skutečně rozdělí na dva řetězce bloků - jeden podle starých a druhý podle nových pravidel.

Když se na změnách pravidel shodnou všichni členové komunity, nazývá se to "nesmlouvavý hard-fork" a řetězec, který má stále stará pravidla, zanikne a po hard-forku se v něm netěží. Tak tomu bylo téměř u každého hard-forku Monero a jediným pokračováním starých pravidel byly projekty, které se snažily na hard-forku vydělat.

Ačkoli jsou nesmlouvavé hard-forky jediným způsobem, jak řádně aktualizovat důležité aspekty sítě Monero, mají také frustrující vedlejší účinek - starý software, vydaný před plánovaným hard-forkem, nedokáže pochopit nová pravidla sítě, a tak po hard-forku nefunguje! To může vést k tomu, že si uživatelé budou myslet, že se prostředky ztratily, budou si myslet, že se blockchain Monero zastavil, a nebudou moci přesouvat prostředky, dokud si neupgradují peněženku.

## Kdo rozhoduje o tom, kdy se síť Monero aktualizuje a co je její součástí?

Jelikož neexistuje žádná centrální autorita, generální ředitel ani prezident společnosti Monero, je rozhodování o tom, kdy síť aktualizovat, co do ní zahrnout a jak postupovat, na _nás_ , na lidech z komunity Monero, kteří se rozhodnou zapojit a komunikovat! To je obojí nesmírně důležitá součást decentralizovaného projektu, protože plánování a rozhodování o projektu je v konečném důsledku decentralizované a pochází od komunity.

K plánování načasování a funkcí zahrnutých do každé aktualizace sítě Monero dochází na dvou hlavních místech:

  1. Na IRC a Matrixu, nejpoužívanějších chatovacích platformách v komunitě Monero (které jsou propojeny). Tyto platformy umožňují chatování ve velkých skupinách a konají se na nich všechny plánované schůzky komunity Monero, schůzky vývojářů a schůzky výzkumných laboratoří. Tyto schůzky jsou nejlepším způsobem, jak si můžete poslechnout (nebo přispět!) k plánování a diskusi o vylepšeních sítě Monero.

  2. Na Githubu, hlavní komunikační platformě pro dlouhodobější diskuse, plánování a organizaci projektu Monero. Komunita Monero kromě ukládání kódu projektu Monero využívá Github k pořádání schůzek, diskusi o nových funkcích a nápadech a koordinaci plánování aktualizací sítě.

Na IRC a Matrixu, nejpoužívanějších chatovacích platformách v komunitě Monero (které jsou propojeny). Tyto platformy umožňují chatování ve velkých skupinách a konají se na nich všechny plánované schůzky komunity Monero, schůzky vývojářů a schůzky výzkumných laboratoří. Tyto schůzky jsou nejlepším způsobem, jak si můžete poslechnout (nebo přispět!) k plánování a diskusi o vylepšeních sítě Monero.

Na Githubu, hlavní komunikační platformě pro dlouhodobější diskuse, plánování a organizaci projektu Monero. Komunita Monero kromě ukládání kódu projektu Monero využívá Github k pořádání schůzek, diskusi o nových funkcích a nápadech a koordinaci plánování aktualizací sítě.

Pokud máte důležitý nápad na aktualizaci sítě, nelíbí se vám nějaký přístup nebo máte obavy ohledně načasování aktualizace, je důležité, abyste se ozvali a jasně komunitě představili svůj názor!

## Jak mohu pomoci s upgradem sítě?

Jelikož upgrady sítě Monero vyžadují koordinaci a schválení komunitou spolu s aktualizacemi softwaru, je nesmírně důležité, aby se do procesu plánování, testování a komunikace upgradů sítě zapojilo co nejvíce lidí.

Níže uvádíme několik jednoduchých způsobů, jak můžete usnadnit situaci kolem upgradu sítě:

  1. Připojte se k plánovacím schůzkám [uveřejněným na Githubu](https://github.com/monero-project/meta/issues), poslouchejte je a přispějte, pokud máte něco relevantního, co byste chtěli uvést.
  2. Sdělte podrobnosti o načasování upgradu sítě (jakmile bude rozhodnuto!) své oblíbené burze, peněžence nebo těžebnímu poolu. Může být složité řádně informovat všechny uživatele Monera o upgradu, proto je důležité, abychom všichni pomohli, kde můžeme, a rozšířili tak informace.
  3. Před aktualizací sítě otestujte software. Před aktualizací sítě bude na testnetu i stagenetu zveřejněna výzva pro testery, aby bylo zajištěno, že všechny aspekty aktualizace byly řádně naplánovány a implementovány do softwaru. Čím více lidí se zapojí a důkladně otestuje nové verze, tím větší je pravděpodobnost, že upgrade sítě proběhne hladce!
  4. JJakmile budou zveřejněny verze kompatibilní s aktualizací sítě, nezapomeňte okamžitě provést aktualizaci! Čím více lidí bude aktualizováno a připraveno na upgrade sítě, tím hladčeji jej síť zvládne a tím méně budou mít uživatelé problémů.

## Co mohu očekávat od příští aktualizace sítě Monero?

Ačkoli zatím není datum pevně stanoveno, brzy dojde k upgradu sítě, který implementuje několik klíčových vylepšení a funkcí v měně Monero:

  1. Zvýšení velikosti kruhu z 11 na 16, čímž se zvýší základní sada anonymity (čtěte: věrohodná popíratelnost nebo základní soukromí) každé transakce v síti
  2. [Značky zobrazení, skvělý způsob, jak zkrátit dobu synchronizace peněženky o 30–40 %](https://localmonero.co/knowledge/view-tags-reduce-monero-sync-time)
  3. Změny poplatků, zvýšení bezpečnosti a odolnosti sítě vůči rychlým změnám na trhu s poplatky nebo útokům škodlivých subjektů
  4. [Bulletproofs+, další zlepšení efektivity transakcí Monero](https://www.getmonero.org/2020/12/24/Bulletproofs+-in-Monero.html)

Tyto změny výrazně zvýší soukromí, efektivitu a bezpečnost sítě a zároveň připraví půdu pro [Seraphis](https://localmonero.co/knowledge/seraphis-for-monero), transakční protokol nové generace pro Monero.

## Jak se mohu dozvědět více?

Téma hard-forků a upgradů sítě je rozsáhlé a v Moneru má dlouhou a bohatou historii, takže pokud se chcete dozvědět více o historii, procesu nebo plánování nadcházejícího upgradu sítě, určitě se podívejte na některé z následujících odkazů!

  * [Plánování hard forku Monero v15](https://github.com/monero-project/meta/issues/630)
  * [Plánované aktualizace softwaru (v Monero)](https://github.com/monero-project/monero#scheduled-software-upgrades)
  * [Poznámka k plánovaným upgradům protokolu](https://web.getmonero.org/2020/09/01/note-scheduled-upgrades.html)

Další čtení