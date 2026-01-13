---
title: "Vysvětlení výstupů Monero"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero, stejně jako ostatní kryptoměny, používá výstupy jako prostředek pro účtování finančních prostředků. Mnoho uživatelů znalých kryptoměn tento termín pravděpodobně již někdy slyšelo, ale ne každý rozumí tomu, co znamenají a jak fungují. Jak jsme prozkoumali v našem [článku o kruhových podpisech](/knowledge/ring-signatures), výstupy jsou skutečné jednotky vyměňované v blockchainu mezi transakčními stranami. Podobně jako u dolarové bankovky, ale částka nemá pevnou nominální hodnotu.

Pokud dostanete za práci 16 $, můžete dostat jednodolarovou, pětidolarovou a desetidolarovou bankovku. Máte 16 $, ale zároveň máte v peněžence tři různé bankovky. Pokud byste chtěli někomu zaplatit 6 $, mohli byste použít pětidolarovou a jednodolarovou bankovku, ale pokud byste chtěli někomu zaplatit 8 $, mohli byste použít pouze desetidolarovou bankovku a dostat zpět 2 $ v drobných. A konečně, pokud byste chtěli někomu zaplatit 14 $, museli byste použít všechny tři bankovky a dostali byste zpět 2 $ v drobných, ale na okamžik, kdy předáte všechny tři bankovky, nemáte v peněžence žádné peníze, dokud nedostanete zpět drobné.

Monero funguje podobně. Předpokládejme, že provozujete obchod a uskutečníte tři prodeje tří různých položek. Můžete obdržet 1,5 XMR, 2,25 XMR a 5,25 XMR v celkové hodnotě 9 XMR, ale zároveň máte v peněžence tři různé výstupy v dříve uvedených hodnotách. Stejně jako u dolarů můžete chtít někomu zaplatit 3 XMR. Můžete použít pouze výstup 5,25 XMR a získat zpět v drobných 2,25 XMR, nebo můžete kombinovat výstupy 1,5 a 2,25 XMR a získat zpět v drobných 0,75 XMR.

Jakmile však odešlete transakci, výstupy, které používáte, se uvedou do stavu "uzamčeno", což znamená, že jsou nepřístupné, dokud neobdržíte změnu zpět. Protokol prostředky odemkne (tj. vrátí vám drobné) po 10 potvrzeních, tedy přibližně po 20 minutách. Stejně jako když jednou předáte dolarové bankovky z peněženky, nemůžete peníze znovu použít, dokud nedostanete od pokladníka zpět drobné, je vaše Monero nepřístupné, dokud nedostanete zpět drobné.

Vraťme se k příkladu, kdy někomu posíláte 3 XMR a používáte výstup 5,25 XMR. Nyní, zatímco čekáte na to, až se vám 1,75 XMR vrátí v drobných, nemůžete je použít. Těchto 1,75 XMR je pro vás nedostupných. Stále však můžete používat výstupy 1,5 XMR a 2,25 XMR, protože ty nebyly utraceny. Vrátíme-li se k příkladu s dolary, pokud byste někomu zaplatili 8 $, jako v předchozím příkladu, nemohli byste použít 2 $, které očekáváte zpět v drobných, dokud by vám nebyly vydány, ale v tomto příkladu máte v peněžence stále 10 $ bankovku, která je nepoužitá. Tu můžete stále použít k nákupu čehokoli, co chcete, zatímco čekáte na rozměnění. Stejně tak je tomu u měny Monero.

Toto je pro nové uživatele Monera často matoucím bodem. Často se může stát, že uživatel má v peněžence pouze jeden výstup, který obdržel z burzy nebo od přítele. Řekněme, že tento výstup je 20 XMR. Žádné další výstupy ve své peněžence nemají. Nyní chtějí přispět dvěma svým oblíbeným charitativním organizacím. Na první charitu pošlou 5 XMR a pak jsou zmateni, protože i když by jim mělo zbýt 15 XMR, nemohou okamžitě poslat další dar na druhou charitu. Jak jste možná uhodli, je to proto, že 15 XMR je zablokováno. Nelze je utratit, dokud se nevrátí jako drobné (10 potvrzení nebo přibližně 20 minut). Po odemčení jejich prostředků by mohli odeslat druhý dar.

Jen bych zopakoval, že by tento problém neměli, kdyby místo toho měli více výstupů, například dva výstupy 10 XMR nebo podobné. Mohli by poslat oba dary hned po sobě, protože první dar by použil jeden z výstupů 10 XMR (a čekal by 10 potvrzení, aby dostal zpět 5 XMR v drobných), a druhý dar by použil druhý výstup 10 XMR.

Některé kryptoměnové peněženky mají funkci nazvanou "správa výstupů", která uživateli jednoduše ukáže, které výstupy má aktuálně k dispozici (kromě jejich celkové částky), a umožní mu vybrat si, které z nich chce při utrácení kryptoměn použít.

Od nynějška provádí GUI Monero výběr výstupů za uživatele automaticky, protože výběr vlastních výstupů vede často ke zmatkům nebo v některých případech k poškození soukromí. Existují však peněženky ve výstavbě, například nový projekt peněženky Feather, které budou tyto funkce správy výstupů obsahovat.

Mluvili jsme hodně o odesílací části, ale něco fascinujícího se děje i na přijímací straně. Vrátíme-li se k našemu příkladu, kdy někomu posíláte 3 XMR a v transakci použijete své výstupy 1,5 XMR a 2,25 XMR (přičemž očekáváte 0,75 XMR v drobných), příjemce NEobdrží dva výstupy 1,5 XMR a 2,25 XMR. Místo toho obdrží JEDEN výstup 3 XMR.

Protokol na pozadí sloučí všechny výstupy použité pro útratu a vydá příjemci jeden výstup zaplacené částky a pošle jeden výstup změny zpět odesílateli. Odesílatel tedy také obdrží zpět jeden výstup jako drobné, bez ohledu na to, zda k odeslání transakce použil dva, tři nebo deset výstupů.

Doufáme, že jsme tím vyjasnili nejasnosti ohledně výstupů a fungování interního účetnictví protokolu, stejně jako častý problém uživatelů, kteří se setkávají se zmatkem při setkání se zablokovanými prostředky. V dalším článku se budeme zabývat správou výstupů tak, abyste minimalizovali možnost, že budete muset před odesláním budoucích transakcí čekat na odemčené prostředky.

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