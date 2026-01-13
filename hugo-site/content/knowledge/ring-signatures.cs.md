---
title: "Jak kruhové podpisy zakrývají výstupy Monera"
slug: "ring-signatures"
date: "2020-09-08"
image: "/images/rings.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero je v celém kryptografickém prostoru známé jako král soukromých mincí. I když každý ví, že Monero nabízí dobré soukromí, ne tolik lidí rozumí tomu, jak přesně toto soukromí funguje.

Mnoho jiných mincí pro ochranu soukromí zveřejňuje infografiky s porovnávacími grafy, které uvádějí názvy technologií pro ochranu soukromí jednotlivých mincí, a ve většině z nich je technologie Monero označena jako RingCT, což je však pravda jen částečně. Monero má ve skutečnosti trojí přístup k ochraně soukromí. Jedna technologie slouží ke skrytí příjemce transakce, druhá ke skrytí odeslané částky a třetí ke skrytí použitého výstupu, což jsou stealth adresy, RingCT, respektive kruhové podpisy.

Tento trojí přístup znamená, že pokud dojde k poruše jedné z technologií, nemusí ostatní nutně čekat stejný osud. Kruhové podpisy jsou nejslabším článkem schématu ochrany soukromí; slovo slabý zde znamená nejnáchylnější k heuristickým útokům. Věnujme jim trochu času a prozkoumejme je, ano?

Jak bylo uvedeno výše, cílem kruhových podpisů je zastřít výstup použitý v transakci. Pokud je pro vás terminologie "vstup/výstup" kryptoměn matoucí, nezoufejte. Ve skutečnosti to není tak složité. Když slyšíte "výstup", stačí si představit šek. Jeden z těch, dnes už ne zcela běžných, kterými lidé platí. Stejně jako šek může být označen libovolnou částkou - 10 dolarů, 32, 50 dolarů atd. a je vyměňován mezi transakčními stranami. U kryptoměn plní tyto funkce výstupy.

Když vám někdo zaplatí 10 Monero, obdržíte 10 XMR. Tento výstup má hodnotu (10) a je to to, co je odebráno z peněženky odesílatele, stejně jako když platíte za službu, účet opustí vaši fyzickou peněženku a je předán osobě, od které nakupujete.

Způsob, jakým se výstup skryje, spočívá v konstrukci kruhu (odtud název) návnadových výstupů. Tyto návnady však nejsou "falešnými" výstupy". Jsou to skutečné minulé výstupy z blockchainu, které nemají nic společného se současnou transakcí, ale pro vnějšího pozorovatele může každý z těchto výstupů vypadat stejně pravděpodobně jako ten skutečný. Velikost množiny návnadových výstupů plus těch skutečných se nazývá ringsize a v současné době je u Monera jedenáct. Existuje tedy deset návnadových výstupů a jeden skutečný.

Proč prostě nezvýšíme toto číslo na 100 nebo dokonce 1000? Čím více, tím lépe, že? Z hlediska ochrany osobních údajů ano, ale je třeba zvážit i další věci. Vraťme se k fyzickému příkladu, abychom viděli, co mám na mysli. Kdybyste chtěli schovat jednu dolarovou bankovku mezi deset návnad, museli byste v peněžence nosit jedenáct dolarů na každý dolar, který chcete utratit. Jeden pravý dolar a deset falešných. To už začíná být dost těžkopádné, pokud chcete utratit byť jen několik dolarů. Nyní si představte, že bychom zvýšili počet návnad na 1000. Na každý jeden dolar, který byste chtěli utratit, byste museli mít u sebe 1001 dolarů. Museli byste s sebou nosit kufřík jen proto, abyste si mohli koupit jednu tyčinku! Je důležité si uvědomit, že kruhové podpisy nefungují zcela takto, například samotné vábničky nejsou součástí podpisu, pouze odkazy na ně, ale doufáme, že tato analogie může být poněkud nápomocná při představě základních pojmů.

Podobně fungují i návnady v blockchainu. Každá přidaná návnada zvyšuje čas a náklady na ověření transakce. Každý uzel musí pro každou transakci stáhnout celý kruhový podpis a každý kruhový podpis obsahuje skutečný výstup i návnady. Nejen to, ale musí také ověřit matematiku, že alespoň jeden z těchto výstupů je skutečný, a čas ověření matematiky se také zvyšuje s každou návnadou. To znamená, že musíme najít šťastnou střední cestu, kdy je velikost kruhu dostatečně velká, aby dostatečně zakryla skutečný výstup i proti mnoha heuristickým útokům, ale dostatečně malá, aby nezpůsobila masivní nárůst blockchainu. Nestačí zvolit libovolné číslo nebo prostě zvětšit ringsize, když zmenšíme podpis (jako například u CLSAG). Komunita Monero chce konkrétní, matematické důkazy o tom, která velikost kruhu nabízí nejlepší kompromisy. Příliš malé číslo a soukromí nebude dostatečně silné proti heuristickým útokům. Příliš velké, a možná získáme jen okrajový přínos na straně soukromí a budeme zbytečně trpět, pokud jde o škálování.

Ještě jedna věc, kterou je třeba zmínit. Některá literatura o Moneru zjednodušuje a říká, že kruhové podpisy skrývají odesílatele, ale to není úplně pravda a rozdíl není jen pedantický. Rozdíl mezi odesílatelem (člověkem) a výstupem (bankovkou) je velký, pokud jde o zachování soukromí. Zatímco výstup může mít vazbu na odesílatele, výstup sám o sobě se nerovná odesílateli. Takže i kdyby došlo k prolomení kruhového podpisu, nemusí nutně souviset s identitou člověka a částka i příjemce jsou stále skryti, což minimalizuje škody způsobené na soukromí všech stran.

To neznamená, že by porušený kruhový podpis byl bezvýznamný. Jakákoli uniklá metadata jsou špatná a mají potenciál odhalit více informací, než si myslíme, zejména pokud jsou použita ve spojení s jinými metadaty. Proto se snažíme zajistit, aby za rozhodnutím o zvolené velikosti kruhu stála akademická přísnost, únik dalších metadat byl minimalizován a uživatelská zkušenost byla výchozí pro nejlepší možné akce.

Pokud vás však pravděpodobnost poškozeného podpisu stále znepokojuje, na obzoru se objevují neuvěřitelné novinky. Nová generace protokolů pro ochranu soukromí, na které se pracuje, jako jsou Triptych, Arcturus a Lelantus, má opravdu skvělé možnosti. V těchto protokolech se velikost škáluje logaritmicky, nikoli lineárně, jak se zvětšuje velikost kruhu. To znamená, že se nám tam vejde 100 návnad, ale použitý prostor se blíží velikosti kruhu 10 ve staré technologii. To je docela velký rozdíl, který výrazně zlepší soukromí všech uživatelů.

V této hře na kočku a myš, kterou je soukromí, Monero neustále inovuje, aby si udrželo náskok a zajistilo nejlepší praktické soukromí pro všechny.

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