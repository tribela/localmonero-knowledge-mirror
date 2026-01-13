---
title: "Proč Monero na rozdíl od Zcash používá bezdůvěryhodné nastavení"
slug: "monero-trustless-setup"
date: "2021-02-13"
image: "/images/trust.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Málokteré myšlence v oblasti kryptoměn je věnováno tolik pozornosti a diskusí jako konceptu důvěry, a ne bezdůvodně. Vždyť celým smyslem blockchainu je eliminovat důvěru ve třetí strany.

Pro ty, kteří této myšlence plně nerozumějí, přinášíme lehký úvod. V tradičním finančním systému jsou třetí strany obecně využívány k různým úkolům. Banky slouží k tomu, aby vaším jménem zabezpečily peníze před krádeží, arbitři. Escrows se používají, aby mohly fungovat obchodní transakce mezi dvěma stranami, které si navzájem nedůvěřují. Společnosti vydávající kreditní karty vyplácejí peníze za zboží a služby vaším jménem a přebírají riziko, že je nemusíte vrátit.

Každý z těchto případů vyžaduje důvěru. V případě bank a zprostředkovatelů úschov důvěřujete, že oni sami neutečou s vašimi penězi, a v případě společností vydávajících kreditní karty důvěřujete, že vaším jménem nevyplatí peníze bez vašeho souhlasu, což je všechno velmi pravděpodobné. Děláme, co můžeme, abychom zajistili, že k těmto věcem nedojde. Spolupracujeme pouze s důvěryhodnými společnostmi a jednotlivci a legislativně se snažíme, aby výše uvedené scénáře byly nezákonné, a snažíme se zajistit důsledky pro pachatele, ale ne vždy jim to stejně zabrání.

Tyto služby navíc nejsou zadarmo. Schovatelé a banky si mohou za své služby účtovat poplatky a kreditní karty si za půjčené peníze účtují úroky.

Blockchain byl vytvořen proto, aby tyto prostředníky a s nimi spojenou důvěru a poplatky eliminoval. Díky síle konsensu mohou uživatelé sami vynucovat stav účetní knihy, aniž by někomu důvěřovali, že jim řekne, kolik mají peněz, a aniž by důvěryhodné třetí strany mohly potenciálně utéct s vašimi prostředky.

Na tuto nedůvěryhodnost je kladen tak velký důraz, že jakákoli změna nebo technologický doplněk, který do blockchainu opět přidává prvek důvěryhodnosti, se setkává s velkou skepsí a kritikou a některé projekty všechny takové představy rovnou odmítají. Je tedy zajímavé, že stejná pozornost není věnována ochraně soukromí.

Znovu se podíváme na zbytek světa a vidíme, že až příliš často je naše soukromí vydáno na milost a nemilost "důvěryhodným" třetím stranám. Když zadáváme své fyzické adresy pro zboží, které chceme, aby nám bylo zasláno, věříme, že daný obchod tyto informace nepoužije k nekalým účelům nebo je neprodá jiným osobám. Totéž platí pro naše osobní myšlenky nebo fotografie, které zveřejňujeme na sociálních sítích. Týká se to dokonce i našich financí, jak ukazuje několik hackerů v rámci účetnictví nebo finančních aplikací, které rovnou zveřejňují na interní veřejné nástěnce, za co lidé utrácejí peníze (např. Venmo).

Monero vnímá tento závazek k nedůvěryhodnosti blockchainu a podobný standard uplatňuje i v přístupu k ochraně soukromí. Naše soukromí by nemělo záviset na slibu třetí strany, že ho bude chránit, stejně jako by naše finance neměly záviset na slibu ostatních, že nám s nimi neutečou. Za tímto účelem Monero zajišťuje, že všechny implementované technologie pro ochranu soukromí jsou nedůvěryhodné.

Existují i další technologie ochrany soukromí. Důvěryhodné a, pravda, nejsou bez silných stránek. Zcash ve svém protokolu důvěrných transakcí používá jako stavební kameny určité typy systémů dokazování, které mají velmi silné záruky soukromí s velkými sadami anonymity a při správném použití by mohly být účinným způsobem, jak si zajistit soukromí. Nevýhodou tohoto přístupu však je, že v rámci počátečního nastavení této technologie je třeba zvolit a následně zapomenout sadu parametrů. Pokud by si někdo tento parametr ponechal, měl by možnost vytvářet falešné důkazy SNARK a efektivně tisknout peníze, aniž by byl někdo moudřejší, protože jsou skryté. Má to však vliv na soukromí? Někteří teoretici tvrdí, že ano, zatímco jiní, že ne, a nakonec je třeba provést další výzkum, abychom dospěli k definitivní odpovědi.

Nezávisle na tom zní tento proces minimalizace důvěryhodnosti stejně jako scénáře, o kterých jsme hovořili na začátku tohoto článku. Tradiční svět. Ten, od kterého se snažíme odejít. Blockchain sám o sobě důvěru ve třetí strany nesnižuje, ale spíše ji eliminuje. Komunita Monero si myslí, že stejný standard eliminace, nikoliv snížení, by měl být aplikován také na naše technologie ochrany soukromí. To, že není definitivně prokázáno, že důvěryhodná nastavení mohou nebo nemohou ohrozit soukromí, neznamená, že bychom měli být laxní k tomu, abychom v tomto ohledu důvěru do systému opět vpustili.

Jakýkoli pokrok v oblasti soukromí je samozřejmě zlepšením a často je důvěryhodné soukromí pouze odrazovým můstkem k nedůvěryhodnému soukromí a v těchto případech jsme rádi, že se tato oblast posouvá kupředu. A zároveň komunita Monero prostě nemůže s čistým svědomím nasadit v našem blockchainu technologii ochrany soukromí, která by oslabila samotný smysl naší revoluce.

Často dostáváme otázku, kdy Monero implementuje tu či onu novou technologii ochrany soukromí. Tyto otázky často přicházejí od neinformovaných lidí, kteří nerozumí kompromisům a pouze papouškují nové módní fráze o ochraně soukromí. Odpověď na tyto otázky je jednoduchá. Společnost Monero neustále zkoumá, reviduje a zkoumá nové protokoly ochrany soukromí, které by posílily záruky ochrany soukromí v řetězci Monero, ale nejsme ochotni se kvůli tomuto cíli pouštět do světa důvěryhodného soukromí, i když jsou záruky teoreticky silnější.

Někteří říkají, že se tento přístup ukáže jako zastaralý, ale my si myslíme, že takoví lidé ztratili příběh, proč jsme tady vlastně začali.

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

  * [Jak CLSAG zlepší efektivitu Monero](/knowledge/what-is-clsag/)

  * [Proč má Monero ocasní emise](/knowledge/monero-tail-emission/)

  * [Stručná historie Monera](/knowledge/monero-history/)

  * [Wired Magazine se o Moneru mýlí, tady je důvod](/knowledge/wired-article-debunked/)

  * [15 vyvrácených mýtů a obav o Monero](/knowledge/monero-myths-debunked/)

  * [Jak Dandelion++ uchovává původ transakcí Monero v soukromí](/knowledge/monero-dandelion/)

  * [Proč je Monero open source a decentralizované](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Co dělá RandomX tak výjimečným](/knowledge/monero-mining-randomx/)

  * [Proč je Monero lepší než Dash, Zcash, Zcoin (i s Lelantusem), Grin a bitcoinové mixéry jako Wasabi (aktualizováno květen 2020)](/knowledge/why-monero-is-better/)