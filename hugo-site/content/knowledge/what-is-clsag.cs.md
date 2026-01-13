---
title: "Jak CLSAG zlepší efektivitu Monero"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Jako protokol je Monero v současné době v neustálém stavu inovací. Komunita Monero s využitím výzkumu v řetězcích i mimořetězových řešeních hledá oblasti ke zlepšení, aby bylo Monero soukromější, škálovatelnější a přístupnější pro všechny. Jednou z novějších inovací je nahrazení schématu propojitelného kruhového podpisového schématu MLSAG drop-in náhradou CLSAG, což je zkratka pro Concise Linkable Spontaneous Anonymous Group.

Na povrchové úrovni sníží implementace CLSAG nejběžnější transakce se 2 vstupy a 2 výstupy o 25 %. Rovněž dojde ke snížení doby ověřování o 10 %.

Ale co přesně je CLSAG? Co dělá a jak se liší od staré verze MLSAG? Pojďme si na chvíli připomenout, proč a jak se používají kruhové podpisy, abychom tento koncept lépe pochopili. Kruhové podpisy umožňují neinteraktivní, svědecky nerozlišitelné vstupy pomocí podepisujícími osobami vybraných sad anonymity předchozích výstupů. Laicky řečeno, umožňuje uživateli skrýt své výstupy použité v transakci vedle nesouvisejících výstupů, a to vše může udělat, aniž by k tomu potřeboval účast kohokoli dalšího. Jediné, co potřebujete, je kopie blockchainu. Každý z těchto výstupů se většinou jeví jako stejně pravděpodobný jako ten skutečně odeslaný, čímž se skryjí metadata o odesílateli.

To však přináší menší problém. Co kdyby uživatel zkonstruoval kruhový podpis se všemi výstupy návnady? Jak by někdo poznal, že neznámý odesílatel nemá oprávnění odeslat žádný z nich? Byl by tento uživatel schopen vydat falešné peníze? Odpověď zní ne. Kruhový podpis obsahuje metodu, která prokazuje, že alespoň jeden z výstupů je vlastnictvím neznámého odesílatele, aniž by prozradila, který to je. Ve skutečnosti jsou jak CLSAG, tak MLSAG (dále jen SAG) součástí kruhového podpisu, který toto dokazuje. Zajímavé je, že zároveň dokazují, že částka transakce, byť skrytá za důvěrnými transakcemi (RingCT), se vyrovnává. To, že SAG dokazují dvě věci, že jeden výstup je vlastněn někým v kruhu a že transakce je vyrovnaná, je důležité a ve skutečnosti v tom spočívá úspora velikosti a ověření. Pokud vás to začíná mást, nebojte se, brzy se dostaneme k zábavné a snadno pochopitelné analogii.

Staré podpisové schéma MLSAG (Multilayered Linkable Spontaneous Anonymous Group) dokazuje obě výše uvedené věci v kruhovém podpisu, ale každou z nich provádí zvlášť. Použití samostatných výpočtů pro podpisový a závazkový klíč znamená pomalejší operace. Moderní počítač dokáže tyto výpočty provést v řádu milisekund, což se nezdá být mnoho, a skutečně, pro jednu transakci tomu tak není. Když ale vezmeme v úvahu obrovské množství transakcí v blockchainu Monero a to, že uzel synchronizující od nuly bude muset stáhnout a ověřit každou z nich, začnou se bajty a milisekundy rychle hromadit.

CLSAG spojuje matematiku potřebnou k důkazu obou do jednoho a počítá obojí najednou, a to bezpečným způsobem. Co to znamená bezpečným způsobem? No, abychom si to vyjasnili a také doufejme, že celá věc bude dávat větší smysl, prozkoumejme onu slíbenou zábavnou analogii.

Řekněme, že potřebujete jít do obchodu s potravinami i do železářství pro dvě různé věci: potraviny a toxické čisticí prostředky. Nechcete, aby se smísily, protože v případě nehody se chemikálie vylijí na potraviny a ty se stanou nepoživatelnými. Rozhodnete se, že budete superbezpeční a pojedete z domu do obchodu s potravinami, nakoupíte potraviny a pak se vrátíte domů. Teprve poté, co potraviny vyložíte, nasednete zpět do auta, odjedete do železářství a s chemikáliemi se vrátíte zpět do svého domu. Podnikli jste dvě samostatné cesty, abyste zajistili bezpečnost všech nákupů. I když je to skutečně bezpečné, je to neefektivní. To představuje MLSAG, kde jsou uloženy dvě různé sady matematiky a k jejich výpočtu jsou vykonány dvě různé "cesty".

Rozhodnete se však, že to chcete udělat rychleji. Je to příliš mnoho promarněného času. Jistě, když to uděláte jednou nebo dvakrát, neukradne vám to život, ale když to musíte dělat pořád dokola, hodiny se začnou sčítat. Začnete přemýšlet, jestli byste místo toho nemohli udělat jednu cestu. Z domu do obchodu s potravinami, do železářství a zpět domů. Nemůžete jen tak jít a nahodit všechno do auta. Není to bezpečné. Místo toho si v autě určete různá místa pro různé věci a ujistěte se, že vše úhledně zapadá na své místo. Tímto způsobem jste schopni bezpečně absolvovat jednu cestu do obou obchodů a udržet věci od sebe. To představuje CLSAG. V této transakci je nyní uložena pouze jedna sada matematiky, která má tyto dvě věci dokázat, a to tak, že se navzájem neruší. Stále je třeba provést cestu, ale jejich počet jste poměrně drasticky snížili.

Všechno to zní docela zajímavě. Je možné najít další zkratky nebo jiné způsoby, jak ušetřit čas a místo? Odpověď zní ano i ne. Podle současných výzkumníků v oblasti MRL pravděpodobně není možné konstrukce typu SAG dále upravit pro lepší velikost nebo rychlost; jiné konstrukce jako Arcturus, Omniring, RCT3 nebo Triptych však přinášejí mnohem lepší škálování velikosti a výhody při ověřování pomocí jiných matematických metod. Každý z těchto přístupů "nové generace" k podpisově jednoznačným protokolům však přináší vlastní kompromisy v implementačních detailech a je předmětem aktivního výzkumu a zkoumání.

Koneckonců, Monero neustále inovuje.

Další čtení

  * [Jak Monero jedinečně umožňuje cirkulární ekonomiky](/knowledge/monero-circular-economies/)

  * [Monerové kruhové podpisy vs CoinJoin jako ve Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Proč (a jak!) byste měli držet své vlastní klíče](/knowledge/hold-your-keys/)

  * [Přispíváme zpět do Monera](/knowledge/contributing-to-monero/)

  * [Jak vzdálené uzly ovlivňují soukromí Monero](/knowledge/remote-nodes-privacy/)

  * [Jak Monero používá hard-forky k upgradu sítě](/knowledge/network-upgrades/)

  * [Značky zobrazení: Jak jeden bajt zkrátí dobu synchronizace peněženky Monero o více než 40 %](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool a jeho role v decentralizaci těžby Monera](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Co to udělá pro Monero](/knowledge/seraphis-for-monero/)

  * [Je převod bitcoinu na monero stejně soukromý jako přímý nákup monera?](/knowledge/most-private-way-to-buy-monero/)

  * [Proč Monero na rozdíl od Zcash používá bezdůvěryhodné nastavení](/knowledge/monero-trustless-setup/)

  * [Proč je Monero lepší uchovatel hodnoty než bitcoin](/knowledge/monero-better-store-of-value/)

  * [Jak může Monero překonat síťové efekty Bitcoinu](/knowledge/network-effect/)

  * [Proč má Monero komunitu nejkritičtějšího myšlení](/knowledge/critical-thinking/)

  * [Podvody, na které si dát pozor při používání Monero](/knowledge/monero-scams/)

  * [Jak budou fungovat atomové swapy na Moneru](/knowledge/monero-atomic-swaps/)

  * [Co by měl každý uživatel Monero vědět, pokud jde o vytváření sítí](/knowledge/monero-networking/)

  * [Jak RingCT skrývá částky transakcí Monero](/knowledge/monero-ringct/)

  * [Jak skryté adresy Monero chrání vaši identitu](/knowledge/monero-stealth-addresses/)

  * [Jak subadresy Monero zabraňují propojení identity](/knowledge/monero-subaddresses/)

  * [Vysvětlení výstupů Monero](/knowledge/monero-outputs/)

  * [Osvědčené postupy pro začátečníky s Monero](/knowledge/monero-best-practices/)

  * [Jak kruhové podpisy zakrývají výstupy Monera](/knowledge/ring-signatures/)

  * [Jak Monero vyřešilo problém velikosti bloku, který sužuje bitcoiny](/knowledge/dynamic-block-size/)

  * [Proč má Monero ocasní emise](/knowledge/monero-tail-emission/)

  * [Stručná historie Monera](/knowledge/monero-history/)

  * [Wired Magazine se o Moneru mýlí, tady je důvod](/knowledge/wired-article-debunked/)

  * [15 vyvrácených mýtů a obav o Monero](/knowledge/monero-myths-debunked/)

  * [Jak Dandelion++ uchovává původ transakcí Monero v soukromí](/knowledge/monero-dandelion/)

  * [Proč je Monero open source a decentralizované](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Co dělá RandomX tak výjimečným](/knowledge/monero-mining-randomx/)

  * [Proč je Monero lepší než Dash, Zcash, Zcoin (i s Lelantusem), Grin a bitcoinové mixéry jako Wasabi (aktualizováno květen 2020)](/knowledge/why-monero-is-better/)