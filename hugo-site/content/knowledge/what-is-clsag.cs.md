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