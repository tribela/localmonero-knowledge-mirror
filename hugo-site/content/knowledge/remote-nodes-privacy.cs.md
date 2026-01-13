---
title: "Jak vzdálené uzly ovlivňují soukromí Monero"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Jednou z největších výhod Monera oproti ostatním kryptoměnám je jeho soukromí na řetězci, ale zajímalo vás někdy, jak si Monero zachovává soukromí, když používáte vzdálený uzel? A co když používáte server "lehké peněženky", jako je MyMonero? 

V tomto příspěvku se seznámíme s některými podrobnostmi o tom, jak Monero zajišťuje výjimečné soukromí v řetězci i při použití vzdáleného uzlu, a také s tím, na co si dát při používání vzdálených uzlů pozor.

## Jakou funkci plní uzly v Moneru?

Pro ty, kteří nejsou tak dobře obeznámeni s tím, jak Monero funguje, uzly (nebo servery) v síti Monero může provozovat kdokoli a umožňuje vlastníkovi uzlu - nebo dalším osobám, které se rozhodnou jej sdílet! - synchronizovat kopii blockchainu a poskytovat ji ostatním v síti. Tyto uzly také ověřují všechny transakce probíhající v síti i všechny zveřejněné bloky a zajišťují, že všechny dodržují pravidla stanovená konsensem.

Druhou funkcí, kterou uzly v Moneru plní, je poskytování všech údajů, které vaše oblíbená peněženka Monero potřebuje ke správné kontrole transakcí, které vám patří, a k provádění nových transakcí. Tato data poskytují uzly dvěma způsoby:

  * Peněženka si vyžádá data z každého bloku v blockchainu, zkontroluje, zda v něm nejsou transakce, které vám patří, a po kontrole peněženkou je zahodí. 
    * Tento krok bude brzy výrazně vylepšen díky [tagům zobrazení](/knowledge/view-tags-reduce-monero-sync-time).
  * Při odesílání transakcí poskytuje uzel, který používáte, seznam možných návnad (nebo falešných vstupů), které se použijí při sestavování transakce, čímž je zajištěno, že se pokaždé, když utrácíte Monero, máte kam schovat. 
    * Tyto návnady jsou součástí [kruhových podpisů](/knowledge/ring-signatures), což je důležitá součást přístupu Monero k soukromí na řetězci.

  * Tento krok bude brzy výrazně vylepšen díky [tagům zobrazení](/knowledge/view-tags-reduce-monero-sync-time).

  * Tyto návnady jsou součástí [kruhových podpisů](/knowledge/ring-signatures), což je důležitá součást přístupu Monero k soukromí na řetězci.

## Jaký je nejprivátnější a nejbezpečnější způsob používání Monero?

Při používání vzdálených uzlů je i přes silné soukromí na řetězci, které Monero poskytuje, nejlepší spustit vlastní uzel Monero, abyste měli po ruce neporušenou kopii blockchainu Monero a aby vaše IP adresa byla dobře chráněna. Další výhodou při spuštění vlastního uzlu je, že můžete zpětně přispívat do sítě a umožnit ostatním uzlům synchronizaci z vašeho uzlu nebo dokonce umožnit ostatním uživatelům připojit se k vašemu uzlu pomocí svých peněženek.

Při použití vzdáleného uzlu však Monero stále poskytuje vynikající soukromí. Pokud máte zájem o spuštění vlastního uzlu Monero, zde je jednoduchý návod, jak na to:

  * [Spusťte uzel Monero](https://sethforprivacy.com/guides/run-a-monero-node/)

## Co se o mně může vzdálený uzel dozvědět?

Při používání vzdáleného uzlu existuje několik klíčových informací, které jsou vzdálenému uzlu zpřístupněny, a několik klíčových způsobů, jak vás může uzel napadnout, zabránit vám v transakci a podobně.

První, co se o vás může vzdálený uzel dozvědět, je vaše veřejná IP adresa. Ta bude, doufejme, skryta prostřednictvím sítě VPN nebo Tor, ale vzdálený uzel si může vaši veřejnou IP adresu spojit s transakcí, což mu pomůže zúžit místo, odkud transakci provádíte. Vzdálený uzel se také může dozvědět poslední blok, který vaše peněženka synchronizovala, a na základě toho se o vás pokusit odhadnout, například kdy Monero běžně používáte a kdy jste Monero naposledy utratili. To platí zejména v případě, že přicházíte stále ze stejné IP adresy (například z domova). Poslední klíčovou věcí, kterou se o vás může vzdálený uzel dozvědět, jsou základní informace o transakcích, které přes něj posíláte. I když to mohou být nejzřejmější údaje, které o vás provozovatel vzdáleného uzlu získá, je důležité si uvědomit, že při kombinaci těchto informací s dalšími údaji mimo řetězec by mohly být použity k vypátrání odesílatele transakce. To může být obzvláště nebezpečné, pokud je vzdálený uzel provozován škodlivým subjektem, analytickou společností blockchainu nebo represivním národním státem.

Vzdálený uzel se vám také může pokusit způsobit potíže tím, že před vámi skryje bloky, takže si vaše peněženka bude myslet, že byla synchronizována, i když tomu tak není. To může způsobit, že si budete myslet, že se prostředky ztratily, nebo vám zabrání v utrácení prostředků, dokud se nepřipojíte k jinému uzlu. Poslední klíčovou věcí, kterou může vzdálený uzel udělat, je nakrmit vaši peněženku zmanipulovaným seznamem návnad. To by mohlo způsobit, že vaše peněženka buď zcela selže při vytváření transakcí (což vám znemožní utrácet prostředky), nebo by se vzdálený uzel mohl pokusit poskytnout návnady, o kterých ví, že jsou utraceny, aby snížil anonymitu, kterou obdržíte při každé transakci.

## Jaké záruky soukromí ještě existují při použití vzdáleného uzlu?

Ačkoli vás tento článek možná trochu vyděsil, je důležité si uvědomit, že soukromí, které Monero poskytuje, je vynikající i při použití vzdáleného uzlu a při tomto způsobu použití daleko předčí jakoukoli jinou kryptoměnu. Stále získáváte silné soukromí na řetězci, které Monero poskytuje, protože vzdálený uzel nikdy nezná skutečný vstup (jaké mince utrácíte), částku Monero utracenou v transakci ani adresu příjemce transakce. Pozorovatelé zvenčí také nemohou vidět skutečný vstup, částku ani adresy zúčastněných (bez ohledu na to, jaký typ uzlu se rozhodnete použít!), což zajišťuje, že mimo vzdálený uzel mají i vaše IP adresa, informace o synchronizaci peněženky a transakce silné záruky soukromí.

Vzdálený uzel také nikdy nemá přístup k předchozím transakcím, které jste odeslali nebo přijali, ani k množství Monera, které máte aktuálně v peněžence, a v okamžiku, kdy začnete používat jiný uzel, ztratí veškerý přehled o vašich transakcích. Vzdálenému uzlu nejsou nikdy poskytnuty žádné soukromé klíče (ani klíče k útratě, ani klíče k prohlížení), a vaše peněženka tak zůstává soukromá, bezpečná a použitelná. Bez ohledu na vzdálený uzel vám také nikdy nehrozí ztráta nebo krádež Monera, protože uzel nemůže upravovat adresu příjemce, nikdy nemá přístup k soukromým klíčům vaší peněženky a nemůže vaše Monero nijak zabavit.

## Co třeba „lehké peněženky“ jako MyMonero?

Ačkoli je toto téma trochu mimo rámec tohoto článku, chtěli jsem se věnovat jedinečnému typu peněženek v Moneru - lehkým peněženkám. Název lehká peněženka vychází z toho, že vaše peněženka (v telefonu nebo počítači) nemusí provádět žádnou synchronizaci blockchainu, takže je práce s ní rychlejší a plynulejší.

Takové peněženky však prozatím přinášejí vážný kompromis v oblasti soukromí - vaše peněženka odesílá soukromý klíč pro zobrazení na vzdálený server, který používáte (jako je výchozí v MyMonero), čímž vzdálenému serveru poskytuje plný přehled o všech přijatých prostředcích od vytvoření vaší peněženky (a dokud nepřestanete tuto peněženku používat nebo seedovat). Tím se ovšem drasticky snižuje soukromí, které od provozovatele uzlu získáváte, a je třeba k němu přistupovat obezřetně.

Komunita Monero naštěstí pracuje na vylepšení softwaru, který můžete použít k hostování vlastního serveru lehké peněženky (LWS), což vám umožní rychlou synchronizaci, aniž byste museli důvěřovat třetí straně se svými soukromými klíči zobrazení - protože spustíte software, kam vaše peněženka posílá soukromé klíče zobrazení!

Další informace o vlastním serveru lehké peněženky naleznete v níže uvedeném úložišti Github:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Jak se mohu dozvědět více?

Pokud jste zvědaví a chtěli byste lépe porozumět uzlům v Moneru a podívat se na možnost využití vzdáleného uzlu nebo spuštění vlastního, podívejte se na níže uvedené odkazy, kde najdete skvělá místa, kde můžete začít:

  * [Monero World, seznam vzdálených komunitních uzlů, které lze použít](https://moneroworld.com/#nodes)
  * [Uzly Monero provozované Sethem For Privacy, autorem tohoto článku](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, seznam vzdálených uzlů s často kontrolovaným stavem< /a>](https://monero.fail/)
  * [Jak se připojit ke vzdálenému uzlu v rámci peněženky GUI](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia – vzdálený uzel](https://www.getmonero.org/resources/moneropedia/remote-node.html)

Další čtení