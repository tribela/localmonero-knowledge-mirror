---
title: "Co by měl každý uživatel Monero vědět, pokud jde o vytváření sítí"
slug: "monero-networking"
date: "2020-11-11"
image: "/images/networking.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Nikoho by nemělo překvapit, že Monero, a vlastně všechny kryptoměny, běží na internetu. A přestože se toto tvrzení zdá být základní a samozřejmé, mnozí nezvažují důsledky toho, co to znamená s ohledem na jejich soukromí. Jinými slovy, existují věci, před kterými Monero může a nemůže chránit, už z podstaty toho, že běží na internetu. Některé z těchto úvah jsou pouhé nepříjemnosti, zatímco jiné jsou mnohem závažnější ve scénáři, kdy je vyžadováno absolutní soukromí. Pojďme se seznámit s tím, jak spolu uživatelé Monera v síti komunikují a co to znamená pro jejich soukromí.

Začneme-li triviální stránkou věci, pokud uživatel nemá přístup k internetu, nemůže stahovat nové bloky, šířit transakce jménem ostatních ani odesílat vlastní transakce. Zajímavé je, že uživatel s plným uzlem bez přístupu k internetu může zkonstruovat transakci offline, kterou může odeslat později. Je to proto, že kruhový podpis potřebuje pouze výstupy z blockchainu, s nimiž se může skrývat. Krátká připomínka, [jak fungují kruhové podpisy](/knowledge/ring-signatures), skrývá skutečný výstup, který uživatel odesílá, mezi kolekcí nesouvisejících výstupů vybraných z minulosti. Pokud má uživatel přístup k těmto výstupům v podobě plně staženého blockchainu (plného uzlu), může z minulých výstupů vytvořit kruhový podpis a po obnovení připojení k internetu rozšířit transakci do sítě.

Uživatel, který používá vzdálený uzel, to nemůže udělat, protože při sestavování svého kruhového podpisu kontaktuje vzdálený úplný uzel, aby do kruhového podpisu zahrnul výstupy. Absence internetu znamená, že se s tímto uzlem nemůže spojit, takže nemá možnost konstruovat transakce offline.

Než se budeme věnovat některým aspektům ochrany osobních údajů, podívejme se stručně na to, jak internet funguje jako celek. Celý internet není nic jiného než počítače, které se připojují k jiným počítačům. To je vše. Blog, který rádi čtete? Jen nějaké soubory umístěné na počítači někoho jiného. Webová stránka, na které čtete tento článek (LocalMonero)? Soubory a kód umístěné někde na počítači. Takto fungují i šíleně velké weby. Vezměte si například YouTube. Pouze video soubory hostované v obřích počítačových systémech společnosti Google, ke kterým se připojíte a stáhnete si video do svého počítače, abyste se na něj mohli podívat.

Tyto počítače se navzájem rozlišují, protože každý počítač připojený k internetu má přiděleno jedinečné identifikační číslo, které se nazývá IP adresa. Obvykle se jedná o čtyři sady čísel oddělených tečkami, například: 172.66.35.7. To je důležité mít na paměti, když uvažujeme o tom, jak se informace o měně Monero pohybují po internetu. Monero je síť typu peer-to-peer (P2P), což znamená, že se počítače mezi sebou spojují přímo, nikoli pomocí prostředníka. Když tedy plný uzel uživatele stahuje nově objevený blok, nestahuje ho z centrálního serveru, ale od svých vrstevníků. Nevýhodou je, že jelikož se uživatelé připojují přímo k sobě navzájem, znají navzájem své IP adresy.

No a? O co jde? Je to jen číslo, ne? Ne tak docela. Samotné IP adresy obsahují informace o uživateli, jako je země původu a poskytovatel sítě, ale co je ještě horší, poskytovatelé internetových služeb (ISP) znají IP adresu každé osoby, která využívá jejich služby. To znamená, že tito poskytovatelé internetu a ti, se kterými spolupracují, mohou sledovat internetový provoz uživatele a pomocí chytré taktiky zjistit, že používá Monero. Než se vyděsíte, všimněte si, jaká je tam formulace. Jediné, co tito slídilové mohou udělat, je zjistit, že se daná osoba připojuje k jiným uzlům sítě Monero. Díky technologii ochrany osobních údajů v síti Monero o dané osobě nic jiného neunikne. Ani to, zda provozuje uzel, ani to, zda/kdy odesílá transakce, a pokud je transakce odeslána, nejsou známy žádné její informace. Jediné, co tito poskytovatelé internetových služeb vidí, je, že se jeden z jejich uživatelů připojuje k síti Monero.

Na některých místech může být pro některé lidi samotná tato informace dostatečným důvodem k poškození pověsti nebo svobody. Nebo je pro vás možná nepřijatelná představa, že by někdo z jakéhokoli důvodu narušoval vaše soukromí a to, co děláte na internetu. Těmto osobám doporučujeme, aby se k síti Monero připojovali pouze pomocí sítí VPN, Tor nebo I2P, což jsou služby, které skrývají IP adresu uživatele před ostatními a také skrývají to, co uživatel dělá, před jeho poskytovatelem internetových služeb. Rozdíly mezi těmito službami přesahují rámec tohoto článku, ale na toto téma bylo napsáno mnoho kvalitních článků, takže zainteresovaným uživatelům doporučujeme, aby si něco nastudovali!

Našinec si může myslet, že to, že ostatní vědí, že jsme připojeni k síti Monero, není až tak velký problém. Koneckonců skutečný obsah našich transakcí, nebo pokud vůbec nějaké posíláme, je veřejnosti skrytý, tak co je na tom špatného? To sice může být pravda, ale uživatelům doporučujeme zvážit skutečnost, že hlavním tahákem kryptoměn je být vlastní bankou. Když máte svůj soukromý klíč a něco se s ním stane, nikdo vám nepomůže ztracené prostředky získat zpět.

Být vlastní bankou znamená brát ohled nejen na digitální, ale i na fyzické zabezpečení. Může se velmi dobře stát, že vědomí o připojení jednotlivce k síti Monero může přivolat nežádoucí pozornost, ne nutně od velkých aktérů, jako jsou národní státy, ale od menších aktérů se sobeckým zájmem, jako jsou hackeři, kteří chtějí snadno vydělat peníze. V celém kryptografickém prostoru skutečně existuje nespočet příběhů, kdy k takovým scénářům skutečně došlo.

Tento článek nemá za cíl nahánět strach nebo děsit, ale spíše povzbudit uživatele, aby si udělali průzkum, jaké metody ochrany při surfování na webu jsou pro ně vhodné. Dobrou zprávou je, že tyto dovednosti se přenesou i na obecné používání internetu, nejen na používání měny Monero, a proto v našem stále více internetem propojeném světě nemůže bystrý uživatel udělat chybu, když nashromáždí patřičné znalosti a dovednosti, aby zůstal v bezpečí a byl skutečně svou vlastní bankou.

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