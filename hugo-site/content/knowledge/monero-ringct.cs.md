---
title: "Jak RingCT skrývá částky transakcí Monero"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Soukromí Monero nezávisí na jednom jediném mechanismu, který by v případě prolomení odhalil všechny transakce, ale spíše na třech různých technologiích, které pracují v tandemu a zajišťují komplexní soukromí, přičemž kompenzují slabiny ostatních částí. Tento tříbodový přístup se skládá z [kruhových podpisů](/knowledge/ring-signatures), RingCT a [skrytých adres](/knowledge/monero-stealth-addresses). Tyto tři technologie skrývají skutečný výstup (odesílatel), množství a příjemce. Dnes budeme mluvit o RingCT.

RingCT je pravděpodobně nejtechničtější z těchto tří metod a může být obtížné mu porozumět, takže se nebudeme zabývat tím, jak přesně funguje, ale spíše si ukážeme, jak je možné neznat částku a přesto si o ní něco potvrdit. A nebojte se, jako vždy použijeme spoustu příkladů.

Nejdříve prozkoumejme, proč je důležité ověřit cokoli o částkách. Proč je prostě nemůžeme nechat zcela v tajnosti? Odpověď zní, že existují chytré způsoby, jak mohou lidé vytvářet peníze ze vzduchu, pokud k tomu mají příležitost. Jak by něco takového mohlo fungovat? Podívejme se na příklad.

Pokud si chcete od kamaráda koupit nějakou věc a on za ni chce deset dolarů, pak začínáte s deseti dolary a on s nulou. Poté, co mu těch deset dolarů dáte, bude mít on deset dolarů a vy nulu. Vy jste začínali s deseti a on má nyní deset. Při této transakci nebyly vytvořeny ani zničeny žádné peníze.

Díky kryptoměnám může chytrý člověk dát za položku deset dolarů a místo nuly dolarů v drobných může dostat dva dolary zpět. Místo 0 a 10 vede k 10 a 0 (nebo 10=10), nyní je to 0 a 10 vede k 10 a 2 (nebo 10=12). Dvě Monera byla vytvořena jen tak ze vzduchu. Dovedete si představit, že kdyby si to jednotlivec udělal několikrát, dokázal by v krátké době nashromáždit gigantické jmění.

U Bitcoinu a dalších by to bylo snadno dohledatelné. Podíváte se na vstupy vstupující do transakcí a výstupy vycházející z transakcí a ujistíte se, že to, co je odesláno, se rovná tomu, co je přijato. Pokud by tyto částky byly zašifrované a nebyly viditelné, pak uživatel nemá možnost ověřit, že to, co je odesláno, a to, co je přijato, je stejné.

Ve snaze zvýšit soukromí Bitcoinu vytvořil Gregory Maxwell novou technologii Confidential Transactions (CT), která by umožnila šifrovat částky a zároveň prokázat, že při tomto procesu nebylo nic vytvořeno ani zničeno. Stejně jako většina technologií pro ochranu soukromí se do Bitcoinu nedostala, ale Monero ji chtělo přijmout. Byl tu jen jeden problém. Již zavedená technologie kruhových podpisů byla s navrhovanou myšlenkou nekompatibilní. Jeden z tehdejších výzkumníků MRL, Shen Noether, proto upravil CT na RingCT, verzi CT, která byla kompatibilní s kruhovými podpisy.

Znovu opakuji, že způsob, jakým to funguje, je poměrně technický a bylo by obtížné jej vysvětlit v úvodním článku. Pro nadšence do kryptografie, kteří to prostě musí vědět, je na internetu napsána spousta podrobných článků o vnitřním fungování CT. Nám ostatním tento článek ukáže, jak by bylo možné částky skrýt, ale přesto dokázat, že nic nebylo vytvořeno ani zničeno.

Řekněme, že Alice chce Bobovi poslat peníze. Alice pošle Bobovi 10 XMR a ten obdrží 10 XMR. 10=10, takže zde není nic špatně. Alice však nechce, aby někdo věděl, kolik posílá. Proto si s Bobem vytvoří sdílené tajemství. V podstatě číslo, které znají jen oni dva. Řekněme, že toto číslo je 22. Nyní Alice vynásobí 10 (to, co skutečně posílá) číslem 22 a získá číslo 220. To je číslo, které sdílí se sítí.

Sami těžaři tajné číslo neznají. Kdyby to věděli, mohli by vydělit zobrazené číslo tajným číslem a získat skutečnou odeslanou částku. Ale protože to nevědí, nemohou to udělat. Vidí však, že Bob obdrží 220. 220 odesláno. 220 přijato. 220 = 220. Tímto způsobem může síť ověřit, že žádné Monero nebylo vytvořeno ani zničeno, a to vše bez znalosti skutečné částky, kterou Alice Bobovi poslala.

Jelikož Bob zná sdílené tajné číslo, po obdržení peněz pouze vydělí 22 a získá skutečnou částku, kterou Alice poslala, tedy 10. Alice i Bob tedy vědí, kolik bylo odesláno a kolik bylo přijato, zatímco všichni ostatní mají k dispozici falešné číslo.

Znovu opakuji, že toto není skutečný způsob, jakým CT funguje, ale dává to představu, jak by něco takového mohlo být možné. Skutečný způsob zahrnuje věci jako Pedersenovy závazky, dvě odeslané částky (jednu zašifrovanou částku příjemci a jednu částku závazku do sítě) a... ano, už je snadné si představit, jak by se v tom všem dalo ztratit.

Jediná věc, kterou je třeba si uvědomit, je, že RingCT sice skrývá částku, která byla v rámci transakce mezi dvěma stranami převedena, ale neskrývá dvě další sady čísel.

První jsou transakce na coinbase. Pokud je vám tento pojem neznámý, znamená v podstatě odměnu, kterou těžaři dostávají za nalezení dalšího bloku. Toto číslo není skryté. Každý se může podívat, kolik protokol udělil těžaři za jeho službu. Aktuální množství existujícího Monera tak lze zjistit sečtením všech transakcí coinbase. Jejich součet se bude rovnat aktuálnímu množství Monera v oběhu.

Druhým neskrývaným číslem je poplatek, který se platí těžařům, když uživatel odešle transakci. Poplatky musí být jasné, aby těžaři věděli, koho mají upřednostnit. Tímto způsobem si však uživatelé mohou poškodit soukromí, protože pokud někdo při každém odeslání transakce použije jedinečný poplatek pro těžaře (například 0,12345), lze jeho transakce propojit.

Kromě těchto případů RingCT skrývá částky v měně Monero již od roku 2017 a naše kolektivní soukromí je díky tomu ještě silnější.

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

  * [Monero Mining: Co dělá RandomX tak výjimečným](/knowledge/monero-mining-randomx)/

  * [Proč je Monero lepší než Dash, Zcash, Zcoin (i s Lelantusem), Grin a bitcoinové mixéry jako Wasabi (aktualizováno květen 2020)](/knowledge/why-monero-is-better)/

Další čtení