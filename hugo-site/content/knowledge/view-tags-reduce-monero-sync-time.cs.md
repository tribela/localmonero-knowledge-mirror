---
title: "Značky zobrazení: Jak jeden bajt zkrátí dobu synchronizace peněženky Monero o více než 40 %"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Jednou z nejčastějších stížností na každodenní používání měny Monero je doba, kterou může trvat synchronizace peněženky před odesláním měny Monero. Vývojáři a výzkumníci z komunity Monero naštěstí našli skvělý způsob, jak zkrátit dobu, kterou vám zabere synchronizace peněženky, o více než 40 %, a to bez jakéhokoli dalšího blockchainového bloatu, poplatků atd.

Vstupte do "značek zobrazení", jednobajtového přídavku k datům každé transakce - přijde do Monera v příštím upgradu sítě!

## Proč je synchronizace peněženky Monero pomalejší než u Bitcoinu?

Jednou z prvních otázek, na které si musíme odpovědět, abychom lépe pochopili potřebu řešení, jako jsou značky zobrazení, je, proč je synchronizace peněženky Monero pomalejší než u kryptoměn, jako je Bitcoin.

V Bitcoinu nejsou všechny transakce soukromé a odhalují utrácené mince, jejich množství a zapojené adresy v řetězci, proto mohou peněženky Bitcoinu jednoduše vyhledat všechny neutracené výstupy transakcí (UTXO) nebo použité adresy pro danou peněženku a rychle prohledat blockchain pouze pro UTXO vlastněné těmito adresami, aby zjistily, které mince patří do vaší peněženky a mohou být utraceny.

V Moneru však všechny transakce zachovávají soukromí uživatele tím, že skrývají odesílatele, příjemce a částky, kterých se každá transakce týká. Toto soukromí je sice důležité pro ochranu uživatelů sítě, ale zároveň zavádí pomalejší synchronizaci peněženek. V Moneru musí peněženka porovnávat každý výstup transakce (TXO), který v síti existuje, s privátními klíči vaší peněženky.

Toto porovnávání zahrnuje spoustu složitých matematických a kryptografických úkonů k ověření, že výstup je skutečně váš, protože všechny částky, adresy a známé utracené výstupy (nebo mince) jsou v Moneru ukryty na řetězci.

## Co jsou značky zobrazení?

Jako způsob, jak zkrátit dobu synchronizace peněženek Monero, přišel [výzkumník jménem UkoeHB s novým přístupem](https://github.com/monero-project/research-lab/issues/73) \- přidat ke každé transakci jednobajtový "tag" pomocí sdíleného tajemství, které znají pouze odesílatel a příjemce dané transakce.

Toto sdílené tajemství generuje odesílatel pomocí adresy, kterou mu poskytne příjemce, a nevyžaduje žádnou aktivní spolupráci odesílatele a příjemce. První bajt (nebo znak) tohoto sdíleného tajemství je pak přidán k datům transakce při jejím zveřejnění v síti Monero.

Když chce některý z účastníků této transakce následně synchronizovat svou peněženku s blockchainem Monero, místo aby musel provádět veškerou složitou matematiku a kryptografii pro každý TXO v síti, může nyní peněženka pouze zkontrolovat toto jednobajtové pole v každé transakci a následně provést časově náročné ověření pouze u transakcí, které mají tento znak - přesněji 1/256 TXO v síti!

Tato značka neprozrazuje vnějším pozorovatelům žádné informace o transakci, přidává k velikosti transakce pouze 1 bajt (zanedbatelné množství), a přesto nám umožňuje zkrátit dobu synchronizace o více než 40 % tím, že omezí nutné složité ověřování!

## Značky zobrazení: zjednodušený příklad

Představte si, že máte v místnosti 4 096 krabic, z nichž pouze 5 patří vám. Všechny krabice jsou zvenčí zcela nerozeznatelné a jediný způsob, jak zjistit, zda je krabice vaše, je otevřít ji a vyřešit časově náročnou matematickou úlohu napsanou uvnitř, abyste se ujistili, že je vaše.

Nyní si představte, že se rozhodnete nechat osobu, která vám těchto 5 krabic posílá, vygenerovat speciální kód pomocí vaší adresy a poté na vnější stranu každé z krabic, které vám posílá, umístit pouze první znak tohoto vygenerovaného kódu. Všichni ostatní udělají totéž pro své krabice (aby se zajistilo, že všechny krabice budou stále nerozlišitelné), ale nyní se můžete jednoduše podívat na jeden znak kódu na vnější straně krabice a otevřít pouze ty krabice, které mají tento znak.

Ačkoli ostatní krabice budou odpovídat vašemu kódu, dokonce i ty, které nevlastníte, počet krabic, které musíte otevřít a vyřešit na nich matematickou úlohu, je nyní pouze 16 (1/256 krabic!) místo všech 4 096.

Nyní otevřete těchto 16 krabic, vyřešíte matematické úlohy a ponecháte si 5 krabic, které vám z této skupiny skutečně patří!

## Kdy budou v Monero k dispozici značky zobrazení?

Značky zobrazení jsou jednou z funkcí, která se aktuálně plánuje zahrnout do [chystaného upgradu sítě](https://github.com/monero-project/meta/issues/630) a měla by být vydána někdy na jaře. Komunita [ vybrala 23.3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (v době psaní článku), aby motivovala vývoj a implementaci tagů pro zobrazení, a díky tomu již j-berman ve spolupráci s recenzenty a výzkumníky dokončil převážnou většinu práce na začlenění tagů pro zobrazení do kódové základny Monero.

Jakmile budou značky zobrazení v síti zavedeny, budou všechny transakce odeslané po aktualizaci sítě těžit z výrazně lepšího času synchronizace peněženky. Nebudete muset dělat nic speciálního, abyste začali používat značky zobrazení, vaše oblíbená peněženka pro Monero je prostě začne po upgradu sítě používat automaticky!

## Jak se mohu dozvědět více?

Pokud to vzbudilo vaši zvědavost ohledně značek zobrazení, podívejte se níže na několik dalších odkazů, které jdou do hloubky tématu:

  * [Zkrácení doby skenování pomocí "značky zobrazení" s 1 bajtem na výstup](https://github.com/monero-project/research-lab/issues/73)
  * [Přidejte k výstupům značky zobrazení, abyste zkrátili dobu skenování peněženky](https://github.com/monero-project/monero/pull/8061)

Další čtení