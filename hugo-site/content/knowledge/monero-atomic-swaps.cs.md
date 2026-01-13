---
title: "Jak budou fungovat atomové swapy na Moneru"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Ve snaze o decentralizaci a vytvoření "permissionless" systému je jen málo věcí v kryptoměnovém prostoru tak žádaných jako decentralizované burzy a atomové swapy. Od svého založení se projekt Monero potýká s problémy s implementací atomových swapů, protože funkce ochrany osobních údajů vytvářejí jedinečné problémy při pokusu o návrh tohoto protokolu.

Nejdřív se ale podívejme zpátky. Co jsou atomové swapy? Atomický swap je protokol, pomocí kterého lze směňovat dvě různé kryptoměny na různých blockchainech důvěryhodným způsobem bez prostředníka. To znamená, že pokud by někdo chtěl vyměnit kryptoměnu A za kryptoměnu B, mohl by to udělat bez směny, centralizované nebo decentralizované. Jak si lze představit, vyžaduje to značný výzkum a veškeré technické detaily, které to umožňují, jsou značně komplikované. LocalMonero je zde opět, aby pomohl a poskytl jednoduché vysvětlení pro obyčejného člověka.

Pro začátek se podívejme na nejjednodušší formu atomového swapu, jak ji implementuje Bitcoin. Pokud chce někdo vyměnit bitcoiny za jiný coin, který používá stejnou technologii smlouvy hash time lock, může tak učinit následujícím způsobem. Alice má bitcoiny (BTC), ale chce Litecoin (LTC) a Bob má LTC, ale chce BTC. Rozhodnou se provést atomovou výměnu, takže každý dostane minci, kterou chce. Alice pošle své BTC na speciální adresu pomocí skriptů, které uzamknou finanční prostředky, takže k nim nemá přístup ani ona. Můžete si to představit tak, že Alice vloží své BTC do schránky. Když je skříňka vyrobena, dostane klíč a pošle hash tohoto klíče Bobovi. Nyní Bob nemá samotný klíč, pouze hash, takže zatím nemá přístup k prostředkům.

Bob používá tento hash jako seed, ze kterého si vygeneruje svůj vlastní lockbox a pošle tam svůj LTC, kde je také uzamčen. Vzhledem k tomu, že hash Alicina klíče byl použit jako seed, ze kterého byla vyrobena Bobova skříňka, může použít svůj klíč k získání LTC v Bobově skříňce. Její klíč sedí! Ale pomocí matematické voodoo magie, když použije svůj klíč k otevření zámku LTC, odhalí klíč Bobovi, který jej pak může použít k získání BTC, které vložila do své skříňky. Tímto způsobem, bez prostředníka, Alice a Bob úspěšně vyměnili svá aktiva.

Je tu ale malý problém. Co když Alice pošle do své skříňky a Bob se rozhodne, že už nechce obchodovat. Nyní, protože Alice nemůže získat přístup ke svým BTC, které zamkla, a Bob nedokončí svou část transakce, Alice navždy ztratí své peníze. Naštěstí má bitcoin malou technologii zvanou refundační transakce, a tak po určité době, pokud Bob nenárokuje BTC, mají skripty zabudovaný bezpečnostní systém, kde se BTC automaticky vrátí Alici. To byl hlavní retarder pro implementaci atomových swapů pro Monero. Kvůli technologii ochrany soukromí [ kroužkových podpisů ](/knowledge/ring-signatures) projektu Monero je odesílatel transakce vždy nejistý. Jak může protokol provést transakci vrácení peněz, když ani on neví, odkud transakce přišla?

V roce 2017 malá skupina výzkumníků nastínila jinou metodu, kterou by atomové swapy fungovaly na Moneru. Po několika letech zdokonalování vědci dokončili proces, pomocí kterého by Monero bylo schopno provádět atomové swapy s bitcoiny, a to i bez refundačních transakcí.

Jako u mnoha věcí této úrovně technické složitosti, naše vysvětlení některé věci příliš zjednoduší, aby zprostředkovalo myšlenku, ale přesto poskytne solidní představu o mechanismech, kterými by tento proces fungoval.

Alice (která má XMR a chce BTC) i Bob (která má BTC a chce XMR) si musí stáhnout a spustit program, který podporuje atomový swap. To může být implementováno do peněženek, decentralizovaných burz nebo speciálních specifických programů, ale software musí běžet s protokolem atomic swap. V prvním kroku se klienti Alice a Bob k sobě připojí a vytvoří několik sdílených tajemství a klíčů. V tomto kroku se vytvoří nová adresa Monero, přičemž Alice má jednu polovinu klíče a Bob druhou. Zatím tam ale není žádné Monero, takže není za co utrácet. Poslední věc, kterou je třeba k této adrese poznamenat, je, že oba mají klíč k zobrazení této peněženky, takže mohou oba nahlédnout dovnitř a zjistit, zda nebo kdy dorazí Monero.

Ve druhém kroku Bob odešle svůj BTC na speciální adresu, podobnou bitcoinovému atomickému swapovému protokolu, o kterém jsme již hovořili. Poté, co Alice uvidí, že BTC dorazí na tuto adresu na blockchainu, pošle své Monero na Monero adresu, ke které mají ona i Bob jednu polovinu klíče. Bob si může ověřit, že Monero dorazilo, protože má také klíč k prohlížení, a jakmile uvidí, že je Monero bezpečně v peněžence, pošle Alici kus klíče, který jí umožní vybrat bitcoiny. Podobně jako u jiného protokolu, proces nárokování bitcoinu odhaluje Bobovi její polovinu klíče Monero. Nyní má Bob obě poloviny, takže si může nárokovat Monero, zatímco Alice má jen svou polovinu, takže se ji nemůže pokusit vzít dříve než on.

Takže pokud jste se na to všechno podívali a jste stále trochu zmatení, jak Monero dokázalo obejít problém refundačních transakcí, odpověď je docela jednoduchá. Protože Monero samo o sobě nemá refundační transakce, čtenář by si měl všimnout, že bitcoin (který má refundační transakce) je odeslán jako první a teprve poté, co je ověřeno, že je na blockchainu, je odesláno Monero. To umožňuje Moneru využívat schopnost bitcoinu skriptovat při refundačních transakcích a využívat je, aniž by bylo nutné mít tyto schopnosti samo.

Výměna "atomů" je nyní dokončena, a odtud má Bob několik možností pro svůj nově nárokovaný XMR. Může tuto peněženku Monero používat tak, jak je, nebo přesunout XMR do jiné peněženky, kterou již vlastní. Bob s největší pravděpodobností přesune Monero do jiné peněženky, protože Alice má stále klíč zobrazení a vidí dovnitř.

Krása tohoto protokolu spočívá v tom, že je stále zcela nový a je zde spousta prostoru pro optimalizace. Je také poměrně flexibilní ve své architektuře, takže implementace v jiných peněženkách nebo decentralizovaných burzách by měla být jednoduchá a čistě zapadat do jejich stávající architektury.

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