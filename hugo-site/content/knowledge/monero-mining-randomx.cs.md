---
title: "Monero Mining: Co dělá RandomX tak výjimečným"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
30\. listopadu 2019 mělo Monero svůj půlroční hard fork, přičemž nejočekávanější změnou byl přechod ze starého PoW algoritmu, cryptonight, na zcela nový, interně vyvinutý, RandomX. Komunita Monero věří, že RandomX je velkým krokem směrem k rovnostářské těžbě, ale pojďme se podívat hlouběji, abychom zjistili, zda tomu tak je.

## Účel

Abychom mohli posoudit, zda je RandomX vylepšením, musíme nejprve pochopit, jaký je účel těžby. Těžba zajišťuje blockchain od dvojitých útrat prostřednictvím Nakamoto Consensus. Přesné složitosti toho, jak to dělá, přesahují rámec tohoto článku, ale lze je zjistit z mnoha různých zdrojů na internetu. Důležité je, že zabezpečení pochází z hashů generovaných počítači (těžaři), kteří spolu soutěží o nalezení matematického řešení nezbytného k vytvoření dalšího bloku. Jak to dělají, přidávají do blockchainu nové transakce. Na oplátku za svou práci (haše) jsou odměňováni nově vyraženými mincemi.   
  
S tímto nastavením se může vyskytnout řada problémů, které vyžadují správné pobídky, aby fungovaly správně, ale my se zaměříme na jeden konkrétní problém, který by mohl nastat. Pokud má být těžba soutěží, co se stane, když jeden těžař získá výhodu?

## Pozadí

Pro kontext si řekněme něco o těžebním hardwaru. Těžaři používají k práci počítače, ale všichni víme, že ne každý počítač je vyroben stejně. Některé počítače jsou dostatečně výkonné, aby na nich mohly běžet sítě umělé inteligence nebo náročné hry, zatímco jiné mají problémy i s jednoduchými úkoly. Tyto rozdíly ve výpočetním výkonu ovlivňují také hash rate neboli rychlost, s jakou hledají bloková řešení.   
  
Ale i tyto rozdíly mezi počítači blednou ve srovnání s rychlostí hašování specializovaného hardwaru, jinak známého jako aplikačně specifické integrované obvody (ASIC), které překonávají běžné počítače o několik řádů.  
  
Podívejme se na to, co dělá procesory ASIC tak výkonnými. Představte si, že všechny počítače se nacházejí někde ve spektru, které sahá od schopnosti dělat mnoho věcí, ale nic dobře, až po schopnost dělat pouze jednu věc, ale zato velmi dobře. Procesory a ASIC jsou na opačných koncích tohoto spektra.  
  
Procesory, které jsou ve všech standardních počítačích, jsou na prvním konci. Zvládnou mnoho věcí, například prohlížení webu, hraní her nebo renderování videa, ale žádnou z nich nedělají nijak zvlášť dobře. Tato flexibilita je však na úkor efektivity.  
  
Na druhém konci jsou ASICy, které umí jen jednu věc, ale dělají ji neuvěřitelnou rychlostí. Dokážou vykonávat pouze jednu matematickou funkci, ale protože mohou ignorovat vše ostatní, je nárůst výkonu astronomický. Tato efektivita je však na úkor flexibility, takže pokud se funkce byť jen nepatrně změní - příkladem je x + y = z se změní na 2x + y = z - pak ASIC přestane fungovat úplně.  
  
Ne každý vlastní ASIC, ale každý vlastní počítač. To může vést k nespravedlivé výhodě.

## Zábavná analogie

Pokud je to pro vás stále matoucí, možná vám pomůže následující analogie. Představte si loterii, kde se každou hodinu rozdává tisíc dolarů, a tato loterie vám umožní vytisknout si vlastní losy! Začnete tisknout tolik tiketů, kolik jen dokážete, na své domácí tiskárně, která dokáže vytisknout jeden tiket za sekundu. Po odečtení nákladů na elektřinu a inkoust zjistíte, že můžete stále vydělávat, i když v loterii vyhrajete jen jednou za několik týdnů.  
  
Postupem času budete provoz rozšiřovat, až budete mít celou místnost vyhrazenou pro tiskárny. Celkem 20. Všechno je v pořádku... až do jednoho osudného dne.  
  
Velká novinka. Někdo vynalezl nový druh tiskárny. Umí tisknout pouze losy. Neumí tisknout obrázky, kancelářské dokumenty ani oboustranný tisk. Pouze losy. Ale dokáže je tisknout rychlostí 1000 losů za sekundu. Podívejte se do své malé místnosti s tiskárnami. 20 tiskáren. Potřebujete dalších 980 tiskáren, abyste udrželi krok s JEDNOU z těchto monstrózních tiskáren, a pokud má někdo dvě...?  
  
Z loterie bohužel odejdete, protože už nedokážete ospravedlnit náklady na elektřinu a inkoust.  
  
Ale počkejte! O pár týdnů později jsou tu další novinky! Design tiketu se změnil. Čísla, která byla dříve nahoře, jsou nyní dole. Nové monstrózní tiskárny jsou tak nepružné, že to nedokážou. Dokázaly vyrobit pouze předchozí design. Netrvá dlouho a opět se vesele tiskne dál. Alespoň do té doby, než někdo vyrobí novou monstrózní tiskárnu pro nový design.

## RandomX

Jak do toho všeho zapadá RandomX? Snaží se vyrovnat výhodu ASIC tím, že velmi ztěžuje jejich výrobu. Toho dosahuje tím, že vyžaduje, aby těžaři vytvářeli a prováděli náhodný kód namísto hashování na základě algoritmu.  
  
Může být matoucí, jak to vlastně něčemu pomůže, takže se vraťme k naší analogii s tiskárnou. Vzpomínáte si, co se stalo, když se změnil design? Staré monstrózní tiskárny každou noc zastarávaly a musely být vyvinuty nové s ohledem na nový design. Co by se stalo, kdyby se každý nový výherní los musel řídit novým designovým standardem pro každý nový jackpot?   
  
Vytvořit novou monstrózní tiskárnu by bylo neuvěřitelně obtížné. Už nelze plánovat jen jeden design tiketu. Vzhledem k tomu, že návrh je náhodný, museli by tvůrci monstrozní tiskárny přidat možnosti barevného tisku, způsoby tisku různých nápisů a rámečků a tvarů a další. Stručně řečeno, stroj, který by nakonec vynalezli, by byl standardní, běžnou tiskárnou. Takovou, jakou mají všichni ostatní.  
  
Jednoduchým zavedením této náhodnosti do návrhu tiketu jsme podstatně snížili velkou výhodu získanou díky specializovanému hardwaru. RandomX dělá totéž, ale s těžbou.  
  
Tímto způsobem se minimalizují výhody, které získává několik vybraných bohatých lidí, protože pokud investují do vytvoření "ASIC" pro těžbu RandomX, ve skutečnosti pouze vynaleznou silnější a lepší procesory, z čehož těží celý svět.  
  
To znamená, že se do hry vrací malý chlapík s tiskárnami na 20 tiketů. Možná to bude mít stále těžší, protože tito bohatí jedinci si stále mohou koupit více tiskáren než on, ale nyní alespoň není řádově překonán jen díky jednomu stroji. Svým malým způsobem je konkurenceschopný.  
  
Protože víme, že i malý chlapík může být v těžbě Monera konkurenceschopný, doporučujeme všem, aby si to vyzkoušeli buď v peněžence s grafickým rozhraním Monero, která má podporu pro samostatnou těžbu, nebo stažením softwaru spravovaného komunitou. Je to snadné, konkurenceschopné a otevřené pro všechny.

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

  * [Jak Monero vyřešilo problém velikosti bloku, který sužuje bitcoiny](/knowledge/dynamic-block-size)/

  * [Jak CLSAG zlepší efektivitu Monero](/knowledge/what-is-clsag)/

  * [Proč má Monero ocasní emise](/knowledge/monero-tail-emission)/

  * [Stručná historie Monera](/knowledge/monero-history)/

  * [Wired Magazine se o Moneru mýlí, tady je důvod](/knowledge/wired-article-debunked)/

  * [15 vyvrácených mýtů a obav o Monero](/knowledge/monero-myths-debunked)/

  * [Jak Dandelion++ uchovává původ transakcí Monero v soukromí](/knowledge/monero-dandelion)/

  * [Proč je Monero open source a decentralizované](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Proč je Monero lepší než Dash, Zcash, Zcoin (i s Lelantusem), Grin a bitcoinové mixéry jako Wasabi (aktualizováno květen 2020)](/knowledge/why-monero-is-better)/