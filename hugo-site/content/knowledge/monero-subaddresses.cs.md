---
title: "Jak subadresy Monero zabraňují propojení identity"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero vždy nacházelo inovativní způsoby řešení obtížných problémů se soukromím. Často tyto inovace vedou k dalším inovacím a někdy lze tyto výsledné technologie využít i pro případy použití, o kterých se dříve neuvažovalo. Nikde to není vidět lépe než v případě technologie subadres Monero.

Považte hypotetický problém ochrany soukromí, kdy používání jedné adresy na více platformách od zdánlivě nesouvisejících lidí může vést k propojení a deanonymizaci zmíněných lidí. Jednoduše řečeno, pokud byste byli osoba jménem Billy Joe Bob a prodávali byste jablka za Bitcoiny, mohli byste svou bitcoinovou adresu zveřejnit na veřejném místě, aby vám zákazníci mohli zaplatit. Řekněme, že adresa začíná alfanumerickým řetězcem 7XybV3... Když však pomineme zjevné riziko pro soukromí, že si kdokoli může zkontrolovat váš zůstatek v Bitcoinech a zjistit, kolik jste prodali, je tu ještě druhé riziko pro soukromí, o kterém se často nemluví. Řekněme, že jste také undergroundový hacker vystupující pod jménem l33tz0r. Děláte whistle blowing, informujete nic netušící obyvatelstvo o korupci ve vládě a je nutné, abyste udrželi svou identitu v tajnosti. Za svou práci přijímáte dary v bitcoinech a adresu zveřejňujete na veřejném fóru. Je to stejná adresa, na které přijímáte peníze od svých zákazníků z Applu. 7XybV3... jedna.

Jednoduchým, ale zničujícím deanonymizačním útokem by bylo použití internetového vyhledávače k vyhledání vaší bitcoinové adresy. Zadáte-li do vyhledávače adresu 7XybV3..., zobrazí se dva různé výsledky. Jablečný obchod a l33tz0r. To stačí k propojení obou identit a deanonymizaci l33tz0r s potenciálně děsivými důsledky ze strany mocných.

Důležité je poznamenat, že tento útok je možný i s měnou Monero. Přestože Monero skrývá většinu údajů na řetězci, tento útok žádné nepoužívá. Používá pouze adresu, kterou je nutné sdílet, aby bylo možné obdržet platbu. V případě anonymních darů veřejně. Jedná se o jeden z možných způsobů, jak mohou uživatelé Monera nevědomky poškodit své soukromí, a je také příkladem toho, že i když je Monero špičkové, pokud jde o zachování soukromí, není neprůstřelné.

Obvyklým způsobem, jak tento problém obejít, bylo vlastnictví více peněženek. Díky různým adresám zveřejněným pro každou identitu (nebo případ použití) je nelze propojit. Tato ochrana soukromí však platí pouze v případě, že je uživatel nikdy nezamění. Náhodné zveřejnění nesprávné adresy by mělo stejný efekt propojení. Stejně tak musí být zabezpečen seed každé adresy, čímž se zvyšuje práce s infosecem nutná s každou nově vytvořenou peněženkou.

Řešením Monera byly subadresy. Možnost vytvořit naprosto obrovské množství adres pod hlavní adresou a použít ji jako jakýsi seed. Každá vytvořená podadresa může přijímat Monero a všechny jdou do stejné peněženky. Při použití této metody je počet identit, které lze provozovat pod jednou adresou, obrovský, přičemž práce s infosecem je minimální. Tyto adresy také nejsou matematicky propojitelné, takže pokud uživatel nevykřičí své připojení do světa, vnější pozorovatel bude mít velké potíže s jejich propojením.

Z dílčích adres však vyplynul další zajímavý případ použití; jako možnost náhrady všeobecně nenáviděných platebních ID.

Platební ID představovaly pro obchodníky způsob, jak identifikovat, který zákazník odeslal jakou platbu. Vzhledem k tomu, že informace o Moneru jsou v řetězci zastřené, příjemce transakce není schopen zjistit, která adresa ji odeslala. To znamená, že pokud existují položky s podobnou cenou a více objednávek, může se stát, že nebude možné určit, kdo co poslal. ID platby je jedinečný náhodný řetězec vygenerovaný obchodníkem a předaný zákazníkovi. Zákazník jej přidá jako samostatné pole při odesílání transakce. Tento náhodný řetězec je umístěn do blockchainu jako součást transakce, a obchodník tak může identifikovat a třídit příchozí transakce.

Tato metoda byla chybná v několika ohledech. Zaprvé snižuje jednotnost údajů v řetězci. Dodatečná, jedinečná metadata mohou některé transakce odlišit od ostatních, a umožnit tak heuristickou analýzu. To platí zejména v případě, že tato metadata nejsou vynucována jako povinná pro všechny. Zavedení této povinnosti pro všechny by však zbytečně zvětšilo prostor v blockchainu, a proto se o to neusilovalo. Stejně tak, pokud by bylo ID platby někdy z nějakého důvodu použito opakovaně, bylo by triviální spojit dvě transakce jako propojené. K tomu typicky docházelo u vkladů na burze a kdokoli mohl snadno propojit transakce jako vklady na burze i od jedné konkrétní osoby.

Druhé, z hlediska UX vytvářejí platební ID druhý krok, na který uživatelé kryptoměn přicházející z jiných mincí nejsou zvyklí, a pokud se na ně zapomene, způsobuje to obrovské bolesti hlavy obchodníkovi, který musí tyto transakce identifikovat jinými prostředky. To se obvykle provádělo tak, že se s každým zákazníkem, který zapomněl uvést ID platby, přímo promluvilo a potvrdily se další identifikační údaje, které mohl znát pouze on, například kombinace částky, data odeslání a ID transakce.

Tento krok navíc mnozí opomíjeli a došlo to tak daleko, že některé burzy začaly zákazníkům účtovat peníze, pokud bylo nutné jejich peníze ručně získat zpět z důvodu zapomenutí ID platby. Jiné zatnuly zuby a překously dodatečné náklady na podporu, ale nikdo z toho nebyl nadšený.

Existovalo jedno řešení, integrované adresy, které spojovalo adresu a ID platby do jednoho řetězce, takže se na ně nedalo zapomenout, ale jeho přijetí bylo poměrně slabé, přestože by obchodníci měli z jeho začlenění výhody.

Zajímavým obratem přišly na řadu dílčí adresy, které situaci zachránily. Možnost generovat velké množství podadres na jednu hlavní adresu a identifikovat, které transakce přišly na které podadresy, umožnila obchodníkům zbavit se elegantním způsobem platebních ID a zároveň přijmout novou generaci technologie Monero. Od té doby většina burz a nástrojů pro obchodníky přešla na podadresy jako na primární způsob identifikace transakcí.

To, co začalo jako řešení problému se soukromím, se změnilo v něco mnohem víc, co vyřešilo hlavní problém UX pro obchodníky i zákazníky. Inovace plodí další inovace, které se často mohou nabalovat jako sněhová koule a přinášet nečekaná vítězství pro všechny. Společnost Monero se o tom opakovaně přesvědčila a vynakládá velké úsilí na inovace toho, co je na blockchainu možné. Kdo ví, co dalšího můžeme společně odemknout?

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

  * [Vysvětlení výstupů Monero](/knowledge/monero-outputs/)

  * [Osvědčené postupy pro začátečníky s Monero](/knowledge/monero-best-practices/)

  * [Jak kruhové podpisy zakrývají výstupy Monera](/knowledge/ring-signatures/)

  * [Jak Monero vyřešilo problém velikosti bloku, který sužuje bitcoiny](/knowledge/dynamic-block-size/)

  * [Jak CLSAG zlepší efektivitu Monero](/knowledge/what-is-clsag/)

  * [Proč má Monero ocasní emise](/knowledge/monero-tail-emission/)

  * [Stručná historie Monera](/knowledge/monero-history/)

  * [Wired Magazine se o Moneru mýlí, tady je důvod](/knowledge/wired-article-debunked/)

  * [15 vyvrácených mýtů a obav o Monero](/knowledge/monero-myths-debunked/)

  * [Jak Dandelion++ uchovává původ transakcí Monero v soukromí](/knowledge/monero-dandelion/)

  * [Proč je Monero open source a decentralizované](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Co dělá RandomX tak výjimečným](/knowledge/monero-mining-randomx/)

  * [Proč je Monero lepší než Dash, Zcash, Zcoin (i s Lelantusem), Grin a bitcoinové mixéry jako Wasabi (aktualizováno květen 2020)](/knowledge/why-monero-is-better/)