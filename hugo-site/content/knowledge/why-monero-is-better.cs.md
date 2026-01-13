---
title: "Proč je Monero lepší než Dash, Zcash, Zcoin (i s Lelantusem), Grin a bitcoinové mixéry jako Wasabi (aktualizováno květen 2020)"
slug: "why-monero-is-better"
date: "2024-01-01"
image: "/images/why-monero.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Ne všechny mince zaměřené na ochranu soukromí dokážou zajistit 100% soukromí, nevystopovatelnost, bezpečnost a zaměnitelnost ve 100% decentralizované minci s bezdůvěryhodným nastavením. Zde se dozvíte, jaké jsou tyto atributy a proč jsou důležité:

## Analýza mincí

Zde je analýza známých kryptoměn, které prohlašují anonymitu a/nebo nevystopovatelnost za svůj klíčový rozlišovací znak. Samotný Bitcoin do této analýzy nespadá, protože o sobě nikdy netvrdil, že je anonymní.

Tuto stránku vytvořili uživatelé Monera. Byly doby, kdy jsme nebyli uživateli Monera, ale zajímalo nás finanční soukromí. Zkoumali jsme mince, které o sobě tvrdily, že jsou soukromé, a tato stránka je výsledkem našeho výzkumu. To je důvod, proč jsme si vybrali Monero místo ostatních. Pokud se tedy zdá, že jsme zaujatí, jsme, ale věříme, že tato zaujatost je založena na faktech, která si můžete přečíst níže a sami si je ověřit.

### Přehled

Vyberte logo a přejděte na analýzu této mince.

### Monero

Monero je od svého počátku 100% open source, což znamená, že kdokoli si může prohlédnout zdrojový kód softwaru [ ](https://github.com/monero-project/bitmonero) a ověřit, že neexistují žádná zadní vrátka a že je software bezpečný.

Monero má také [ recenzované výzkumné práce ](https://lab.getmonero.org/), které matematicky a systematicky ověřují všechny jeho vlastnosti uvedené výše.

### DASH

DASH má [ bohatý seznam](https://bitinfocharts.com/top-100-richest-darkcoin-addresses.html), takže se nejedná o soukromou minci. Finanční detaily coinových adres jsou viditelné pro každého, kdo zkoumá blockchain.

> DASH není vůbec kryptograficky soukromý. Vlastně jsem měl v balíčku slajd, na kterém bylo "DASH, LOL," a jako nic jiného... je to snakeoil a já osobně jsem z toho tak nějak vedle. 
> 
> **Gregory Maxwell** , vývojář bitcoinového jádra a kryptograf, v prezentaci [ pro Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

DASH není vůbec kryptograficky soukromý. Vlastně jsem měl v balíčku slajd, na kterém bylo "DASH, LOL," a jako nic jiného... je to snakeoil a já osobně jsem z toho tak nějak vedle. 

**Gregory Maxwell** , vývojář bitcoinového jádra a kryptograf, v prezentaci [ pro Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

**Peter Todd** , další vývojář bitcoinového jádra a kryptograf, učinil [ podobné prohlášení](https://twitter.com/petertoddbtc/status/622022840330682368).

### Zcash

Transakce Zcash jsou viditelné na jejich blockchainu. Umožňují skryté transakce, ale [ méně než 1 % transakcí je plně chráněno ](http://stat.bloxy.info/superset/dashboard/zcash/) . Vzhledem k tomu, že skryté transakce jsou volitelné a nikoli výchozí (nemluvě o řídkém používaní), skryté transakce [ vynikají na jejich blockchainu](http://weuse.cash/2016/06/09/btc-xmr-zcash/) a přitahují na sebe pozornost.

> A mimochodem, myslím, že můžeme úspěšně udělat, aby Zcash příliš sledovatelný pro zločince jako WannaCry, ale stále zcela soukromý & zaměnitelný. 
> 
> **Zooko Wilcox** , CEO Zcash, v [ tweetu ](https://twitter.com/zooko/status/863202798883577856)

A mimochodem, myslím, že můžeme úspěšně udělat, aby Zcash příliš sledovatelný pro zločince jako WannaCry, ale stále zcela soukromý & zaměnitelný. 

**Zooko Wilcox** , CEO Zcash, v [ tweetu ](https://twitter.com/zooko/status/863202798883577856)

Pokud může být Zcash "příliš sledovatelný", pak nemůže být zcela soukromý nebo zaměnitelný. 

Pravidelné transakce jsou transparentní. Skryté transakce používají zk-SNARKS, které mají za určitých podmínek robustní záruky soukromí. Otázkou je, zda jsou tyto podmínky splněny, a vzhledem k nepatrnému množství lidí, kteří využívají stíněné možnosti, to zůstává otázkou.

Zcash je společnost a v současnosti [ bere 20 % všech vytěžených ZEC jako odměnu zakladatele ](https://z.cash/blog/funding.html). 

Zcash vyžadoval **Trusted Setup**. To znamená, že musíte věřit, že systém byl nastaven poctivě. Pokud by nebyl nastaven poctivě, mohlo by být vytvořeno neomezené množství ZEC [, aniž by o tom kdokoli věděl](https://blog.okturtles.com/2016/03/the-zcash-catch/). Tím by hacker zbohatl a znehodnotil by ZEC. Neexistuje žádný způsob, jak zjistit, zda bylo důvěryhodné nastavení provedeno poctivě. Musíme jim věřit na slovo. Tím se do systému zavádí lidský bod selhání, což je v rozporu s téměř každou jinou kryptoměnou. V kryptoměnách byste měli věřit pouze matematice a ověřitelnému zdrojovému kódu, nikoliv lidem. Jak jsme viděli prakticky u všech velkých softwarových společností, jako je [ Microsoft](https://www.gnu.org/proprietary/proprietary-back-doors.en.html), [ Apple](http://www.digitaltrends.com/computing/apple-vs-fbi-backdoor-to-data-already-exists/) a dokonce i vlády, nemělo by se jim věřit. 

Peter Todd, vývojář Bitcoin Core, který se [ účastnil ](https://github.com/zcash/mpc/blob/master/README.md) v Zcash Trusted Setup, to nazval " [ backdoor ](https://twitter.com/petertoddbtc/status/793584540891643906) ". 

> Zcash není bezpodmínečně zdravý, nemůže být se současnou technologií...vyžaduje důvěryhodné nastavení… bude muset zopakovat postup [Trusted Setup] pro upgrade krypto v průběhu času, takže se jedná o zranitelnost. 
> 
> Gregory Maxwell, vývojář bitcoinového jádra a kryptograf, v prezentaci [ pro Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

Zcash není bezpodmínečně zdravý, nemůže být se současnou technologií...vyžaduje důvěryhodné nastavení… bude muset zopakovat postup [Trusted Setup] pro upgrade krypto v průběhu času, takže se jedná o zranitelnost. 

Gregory Maxwell, vývojář bitcoinového jádra a kryptograf, v prezentaci [ pro Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

### Zcoin

**Poznámka:** Zcoin přechází ze současného schématu Sigma na nový protokol, který se opírá o jeho novou práci, Lelantus. Lelantus bude implementován v několika etapách a tento článek bude předpokládat, že všechny etapy jsou dokončeny a implementovány, aby bylo možné je řádně porovnat spolu s předpokládanými časy implementace.

Důvodem, proč byl Zcoinu dopřán tento luxus být posuzován na základě jeho budoucího protokolu, a ne Zcash, je to, že Zcoin má plán s obecnými časovými údaji pro aktivaci, zatímco plány Zcash týkající se "standardního soukromí" jsou a nadále zůstávají mlhavé.

Zcoin (XZC) nebude mít bohatý seznam, takže bude soukromý. Ve výchozím nastavení se očekává, že povinné soukromí bude spuštěno v roce 2021. Po zavedení nebude možné vytvořit bohatý seznam (ačkoli v současnosti [ jeden mají](https://www.coinexplorer.net/XZC/richlist)).

### Grin

### Bitcoin Mixers

Všechny bitcoinové transakce jsou viditelné na blockchainu a existuje [ seznam bohatých s Bitcoiny](http://www.bitcoinrichlist.com/top100), takže Bitcoiny nejsou soukromé. Bitcoin je [ pseudononymní](https://bitcoin.org/en/you-need-to-know), není anonymní. 

U **mixérů bitcoinů** musíte věřit, že mohou uchovávat svá data v bezpečí a nejsou ve vlastnictví vlády, hackerů nebo jiných subjektů ani s nimi nespolupracují. 

V červenci 2017 zakladatel největší služby pro míchání bitcoinů, BITMIXER.IO, oznámil, že končí, a jako důvod uvedl toto: 

> … Teď jsem pochopil, že Bitcoin je transparentní neanonymní systém **podle návrhu**. Blockchain je skvělá otevřená kniha… 
> 
> BITMIXER.IO, v oznámení o uzavření na [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (zvýraznění v originále). 

… Teď jsem pochopil, že Bitcoin je transparentní neanonymní systém **podle návrhu**. Blockchain je skvělá otevřená kniha… 

BITMIXER.IO, v oznámení o uzavření na [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (zvýraznění v originále). 

O několik týdnů později, po zvážení různých mincí zaměřených na soukromí, řekl toto: 

> Po důkladném vyšetřování potvrzuji, že MONERO je nejlepší měnou na ochranu soukromí. Takže vřele doporučuji MONERO všem lidem, kteří potřebují extra soukromí. 
> 
> BITMIXER.IO, v [ navazujícím příspěvku](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Po důkladném vyšetřování potvrzuji, že MONERO je nejlepší měnou na ochranu soukromí. Takže vřele doporučuji MONERO všem lidem, kteří potřebují extra soukromí. 

BITMIXER.IO, v [ navazujícím příspěvku](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Vzhledem k tomu, že všechny transakce Bitcoinu jsou viditelné v blockchainu, lze vysledovat VŠECHNY transakce Bitcoinu. Mixér Bitcoinů může transakce značně zastřít, což někomu značně ztěžuje, ale ne znemožňuje, aby Bitcoiny vystopoval. Jak technologie postupuje a společnosti, které se specializují na sledování transakcí Bitcoinu, se stávají stále rozšířenějšími, kdysi vysoce zastřené transakce budou relativně snadno dohledatelné. 

  * [ Vymáhání práva nadále investuje do služeb sledování Bitcoinů ](https://news.bitcoin.com/law-enforcement-continues-invest-bitcoin-tracking-services/)
  * [ Time.com: Bitcoiny je snazší sledovat, než si myslíte ](http://time.com/3689359/bitcoins-track-anonymous/)
  * [ Elliptic: Společnost specializující se na sledování Bitcoinů pro účely vymáhání práva ](https://www.elliptic.co/)

Vyhledávání na Googlu odhalí desítky článků, jako jsou ty výše uvedené. A nezapomeňte, že jakákoli transakce, která proběhla kdykoli v minulosti, je v blockchainu a je možné ji vystopovat, i když byla použita směšovací služba. Ve skutečnosti je pravděpodobné, že použití směšovací služby na tyto transakce upozorní. 

Ne všechny Bitcoiny jsou stejné a mají stejnou hodnotu. Některé Bitcoiny byly zařazeny na černou listinu a zablokovány několika subjekty, takže tyto mince mají nižší hodnotu než ostatní. Pokud obdržíte Bitcoiny, které byly v minulosti použity k nezákonným účelům, mohou být vaše Bitcoiny zařazeny na černou listinu, i když jste s nezákonnou činností neměli nic společného. Nebo řekněme, že se vláda, zaměstnavatel nebo jiný subjekt rozhodne vaše Bitcoiny v budoucnu zařadit na černou listinu, podobně jako to dělají při zmrazení nebo konfiskaci majetku. Nemohli byste s tím nic dělat. Vzhledem k tomu, že mixér pouze ztěžuje dohledání vašich Bitcoinů, byla tato kategorie označena jako "nezaměnitelné." 

  * Andreas Antonopoulos, bývalý vývojář jádra Bitcoinu, který je v komunitách Bitcoinu a dalších kryptoměn velmi uznávaný, uznává problém zaměnitelnosti Bitcoinu v [YouTube videu](https://www.youtube.com/watch?v=ak1iojpiHpM&feature=youtu .be&t=33m9s). 
  * Diskuse o problému zaměnitelnosti bitcoinů na [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=1190707.0)

## Shrnutí

Podle našeho názoru je Monero jasnou volbou, pokud hledáte soukromou, bezpečnou, nevystopovatelnou, zastupitelnou, decentralizovanou kryptoměnu bez nutnosti důvěryhodného nastavení. Cokoli jiného ohrožuje vaše soukromí a bezpečnost. Ale neřiďte se jen naším názorem. Udělejte si vlastní průzkum a přesvědčte se sami. Vezměte v úvahu, že Monero podporují a používají subjekty, které si zakládají na soukromí a nevystopovatelnosti, jako např: 

  * [ SIGAINT ](https://www.reddit.com/r/Monero/comments/4xqrzd/sigaint_launches_tor_monero_node_as_its_operators/)
  * [ Purismus ](https://puri.sm/posts/purism-collaborates-with-cryptocurrency-monero-to-enable-mobile-payments/)
  * [ Wikileaks ](https://shop.wikileaks.org/donate#db9)
  * AlphaBay Market (AB) byl uzavřen v červenci 2017. [ Federal Forfeiture Complaint ](https://assets.documentcloud.org/documents/3898109/AlphaBay-Cazes-Forfeiture-Complaint.pdf) proti AB ukazuje, že: 
    * **Monero je jediná soukromá a nevysledovatelná kryptoměna:**   
"Celkem z peněženek a počítačových agentů CAZES převzal kontrolu nad přibližně 8 800 000 $ v Bitcoinech, Ethereu, Morenu [sic] a Zcash, rozdělených následovně: 1 605,0503851 Bitcoinů, 8 309,271639 Etherea, 3 691,98 Zcash, _a neznámé množství Monero._ " (dole na str. 20 a nahoře na str. 21, zvýraznění přidáno)
    * **Bitcoinové transakce nejsou soukromé a lze je sledovat:**   
"Federální agenti získali zatykače poté, co vystopovali řadu transakcí s Bitcoiny z AlphaBay na účty v digitální měně a nakonec i na bankovní účty a další hmotný majetek CAZESe a jeho manželky." (str. 17, řádky 24- 26) 

  * **Monero je jediná soukromá a nevysledovatelná kryptoměna:**   
"Celkem z peněženek a počítačových agentů CAZES převzal kontrolu nad přibližně 8 800 000 $ v Bitcoinech, Ethereu, Morenu [sic] a Zcash, rozdělených následovně: 1 605,0503851 Bitcoinů, 8 309,271639 Etherea, 3 691,98 Zcash, _a neznámé množství Monero._ " (dole na str. 20 a nahoře na str. 21, zvýraznění přidáno)
  * **Bitcoinové transakce nejsou soukromé a lze je sledovat:**   
"Federální agenti získali zatykače poté, co vystopovali řadu transakcí s Bitcoiny z AlphaBay na účty v digitální měně a nakonec i na bankovní účty a další hmotný majetek CAZESe a jeho manželky." (str. 17, řádky 24- 26) 

LocalMonero neobhajuje ani nepodporuje žádnou nezákonnou činnost. 

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