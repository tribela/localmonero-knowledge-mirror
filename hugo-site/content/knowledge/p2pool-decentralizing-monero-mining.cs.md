---
title: "P2Pool a jeho role v decentralizaci těžby Monera"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Jedním z hlavních cílů projektu Monero je umožnit spravedlivou, decentralizovanou a bezpečnou síť prostřednictvím nových a inovativních přístupů k těžbě metodou proof-of-work (PoW), která je dnes hlavním způsobem zabezpečení kryptoměnových sítí.

Zatímco jedinečný těžební algoritmus [jako je RandomX](/knowledge/monero-mining-randomx) je pro tento cíl nesmírně důležitý, protože pomáhá zajistit, aby každý, kdo má počítač, mohl přispět přiměřenou částkou k bezpečnosti sítě, RandomX neřeší problémy, které mohou nastat v důsledku těžby v poolu. Poolová těžba je dnes zdaleka nejběžnějším způsobem těžby kryptoměn, včetně Monera, ale nástup p2poolové těžby to naštěstí rychle mění.

## Co je poolová těžba?

Těžba v poolu je způsob, jakým se těžaři dělí o úkol vyřešit blok v síti a poté rovnoměrně rozdělují odměny za všechny bloky, které pool najde. To sice nesmírně pomáhá vyrovnat četnost výplat těžařům oproti těžbě samotného Monera, ale není to bez vážných problémů s centralizací.

Když každý těžař přispívá do poolu, vzdává se kontroly nad svou prací a nalezenými bloky ve prospěch samotného poolu a věří, že pool bude poctivě a spravedlivě rozdělovat odměny mezi všechny těžaře na základě množství práce, kterou každý z nich odvedl. Pokud vše proběhne v pořádku, provozovatel poolu shromáždí práci od všech těžařů, předá ji do sítě a odměny rozdělí rovným dílem.

## Jaký je problém s těžbou v poolu?

Naneštěstí je to zcela závislé na důvěře a umožňuje to provozovateli poolu dělat s prací těžařů nekalé věci. Provozovatel poolu může odvedenou práci využít k útoku na síť, může se pokusit o dvojí utracení prostředků (pokud je pool dostatečně velký) nebo jednoduše využít práci odvedenou těžaři k tomu, aby zaplatil sám sobě a těžaře za jejich práci nikdy řádně neodměnil.

Největší riziko pro síť představuje skupina (nebo více skupin spolupracujících), která má pod kontrolou více než 51 % hashrate sítě, protože by toho mohla využít k podvádění a utrácení prostředků dvakrát (double-spend attack) nebo k pokusu o změnu pravidel sítě.

## Co je p2pool?

p2pool je koncept, který byl původně vytvořen pro těžbu Bitcoinu již v roce 2011, ale nikdy se nedočkal širokého přijetí a v Bitcoinu zůstává prakticky nevyužitý. Naštěstí jeden z klíčových vývojářů stojících za RandomX, SChernykh, strávil svou dovolenou vymýšlením řešení některých problémů s implementací p2pool v Bitcoinu a přepsal celý software od základu.

p2pool v Moneru umožňuje zcela bezdůvěryhodný způsob spolupráce těžařů při řešení bloků a zabezpečení sítě Monero pomocí speciálního softwaru uzlů pro p2pool za účelem sdílení práce.

To se provádí pomocí nového blockchainu ("side-chain"), který uchovává záznamy o práci, kterou každý těžař vykonal, adresu jeho peněženky a kolik Monero vydělal, a poté vyplácí odměnu decentralizovaným způsobem bez důvěry. Protože tento side-chain má mnohem méně těžařů, je mnohem snazší najít a odeslat bloky v něm než v hlavní síti Monero, což těžařům usnadňuje konzistentní výplaty oproti těžbě samotného Monera.

## Jak p2pool řeší problémy těžby v poolu?

V p2poolu neexistuje žádný centralizovaný pool, centralizovaný provozovatel poolu ani jediná osoba, která by držela finanční prostředky a rozdělovala výplaty. Veškerá práce, kterou těžaři kolektivně vykonávají prostřednictvím p2poolu, je kontrolována blockchainem p2poolu a ostatními provozovateli uzlů, aby bylo zajištěno, že je legitimní, a všem těžařům jsou vyplaceny peníze podle jimi vykonané práce okamžitě po nalezení bloku přímo z odměn v tomto nalezeném bloku.

Když se těžaři rozhodnou používat p2pool namísto centralizovaného poolu, zbaví provozovatele poolu veškeré moci a důvěry a zajistí, že jejich práce přispěje k dobru sítě a k jejich vlastní odměně, sníží riziko útoků na síť, zneužití jejich práce nebo krádeže odměn, které jim náleží.

Pomáhá jim to nejen chránit vlastní zájmy, ale také snižuje riziko, které mohou centralizované pooly představovat pro síť Monero jako celek. Používání p2pool také výrazně pomáhá snižovat riziko, které by pro zdraví sítě mohly představovat národní státy nebo regulační orgány, protože neexistují žádní provozovatelé centralizovaných poolů, na které by mohli tlačit, žádná geografická koncentrace poolů, o kterou by se mohli opřít, ani žádný jiný snadný bod nátlaku, který by mohli použít proti Moneru.

## Jaké jsou nevýhody?

Naštěstí byl p2pool v Moneru dobře navržen a sestaven a funguje velmi dobře! Hlavní nevýhodou těžby p2pool však je, že každý těžař, který chce p2pool používat, musí provozovat svůj vlastní uzel Monero, což způsobuje, že proces zahájení těžby je o něco náročnější. Tento uzel však následně slouží k výpočtu všech informací potřebných pro sestavení a kontrolu bloků a zajišťuje, že těžař má naprostou kontrolu nad prováděnou prací. Uzel může také fungovat jako vzdálený uzel pro vlastní peněženku těžaře, přispívá do sítě a mnoho dalšího.

Dalším klíčovým rozdílem oproti centralizované těžbě je to, že malí těžaři využívající p2pool budou mít o něco větší "rozptyl", neboli čas mezi výplatami, než velký centralizovaný pool - je však _nesmírně_ důležité si uvědomit, že to nepovede k tomu, že by časem vydělávali méně Monera! p2pool bude časem stejně ziskový i pro malé těžaře jako centralizované pooly. Část tohoto rozdílu je také kompenzována tím, že p2pool má nativně 0 % poplatků, protože neexistuje žádný provozovatel centralizovaného poolu, který by musel platit za své služby!

## Jak mohu začít?

Naštěstí se díky skvělému návrhu implementace Monero p2pool a mnoha lidem v komunitě, kteří věnovali čas zjednodušení procesu těžby prostřednictvím p2pool, začíná těžit stále jednodušeji. Existuje několik způsobů, jak začít těžit pomocí p2poolu, ale protože technické podrobnosti přesahují rámec tohoto článku, neváhejte a přejděte na níže uvedený odkaz v závislosti na vašem operačním systému:

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## Jak se mohu dozvědět více?

Pokud ve vás tato informace vzbudila zvědavost ohledně těžby p2pool, podívejte se níže na několik dalších odkazů a vysvětlení o p2pool, jak funguje a co to znamená pro Monero:

  * [Oficiální Github pro p2pool](https://github.com/SChernykh/p2pool)
  * [Oficiální dokumenty o používání p2pool](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool je nyní aktivní](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, "průzkumník bloků" svého druhu pro p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh: O jeho vývoji p2pool a decentralizovaného těžebního fondu XMR](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

Další čtení

  * [Jak Monero jedinečně umožňuje cirkulární ekonomiky](/knowledge/monero-circular-economies/)

  * [Monerové kruhové podpisy vs CoinJoin jako ve Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Proč (a jak!) byste měli držet své vlastní klíče](/knowledge/hold-your-keys/)

  * [Přispíváme zpět do Monera](/knowledge/contributing-to-monero/)

  * [Jak vzdálené uzly ovlivňují soukromí Monero](/knowledge/remote-nodes-privacy/)

  * [Jak Monero používá hard-forky k upgradu sítě](/knowledge/network-upgrades/)

  * [Značky zobrazení: Jak jeden bajt zkrátí dobu synchronizace peněženky Monero o více než 40 %](/knowledge/view-tags-reduce-monero-sync-time/)

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

  * [Jak CLSAG zlepší efektivitu Monero](/knowledge/what-is-clsag/)

  * [Proč má Monero ocasní emise](/knowledge/monero-tail-emission/)

  * [Stručná historie Monera](/knowledge/monero-history/)

  * [Wired Magazine se o Moneru mýlí, tady je důvod](/knowledge/wired-article-debunked/)

  * [15 vyvrácených mýtů a obav o Monero](/knowledge/monero-myths-debunked/)

  * [Jak Dandelion++ uchovává původ transakcí Monero v soukromí](/knowledge/monero-dandelion/)

  * [Proč je Monero open source a decentralizované](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Co dělá RandomX tak výjimečným](/knowledge/monero-mining-randomx/)

  * [Proč je Monero lepší než Dash, Zcash, Zcoin (i s Lelantusem), Grin a bitcoinové mixéry jako Wasabi (aktualizováno květen 2020)](/knowledge/why-monero-is-better/)