---
title: "P2Pool a jeho úloha pri decentralizácii ťažby Monero"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Jedným z hlavných cieľov projektu Monero je umožniť spravodlivú, decentralizovanú a bezpečnú sieť prostredníctvom nových a inovatívnych prístupov k ťažbe typu proof-of-work (PoW), čo je hlavný spôsob, akým sú dnes zabezpečené siete kryptomien.

Zatiaľ čo jedinečný ťažobný algoritmus [ako RandomX](/knowledge/monero-mining-randomx) je pre tento cieľ mimoriadne dôležitý, pretože pomáha zabezpečiť, že ktokoľvek s počítačom môže prispieť slušnou čiastkou k bezpečnosti siete, RandomX tieto problémy nerieši. ktoré môžu nastať v dôsledku bazénovej ťažby. Pool mining je dnes zďaleka najbežnejším spôsobom ťažby kryptomien, vrátane Monero, ale našťastie to objavovanie sa p2pool miningu rýchlo mení.

## Čo je pool ťažba?

Pool mining je spôsob, akým sa baníci delia o úlohu pokusu vyriešiť blok v sieti a potom rovnomerne rozdelia odmeny pre všetky bloky, ktoré fond nájde. Aj keď to nesmierne pomáha vyrovnať frekvenciu, s akou sú baníci platení oproti ťažbe samotného Monera, nie je to bez vážnych problémov s centralizáciou.

Keďže každý baník prispieva prácou do fondu, vzdáva sa kontroly nad akoukoľvek prácou, ktorú vykonáva, a blokmi, ktoré nájde, do samotného fondu, pričom verí, že fond čestne a spravodlivo rozdelí odmeny medzi všetkých baníkov na základe množstva prácu, ktorú každý vykonal. Ak všetko pôjde dobre, prevádzkovateľ poolu zozbiera prácu od všetkých baníkov, odošle ju do siete a rovnomerne rozdelí odmeny.

## Aký je problém s poolovou ťažbou?

Nanešťastie to závisí výlučne od dôvery a umožňuje prevádzkovateľovi poolu robiť nekalé veci s prácou, ktorú vykonávajú baníci. Operátor poolu by mohol využiť vykonanú prácu na útok na sieť, pokúsiť sa zdvojnásobiť finančné prostriedky (ak je pool dostatočne veľký) alebo jednoducho využiť prácu, ktorú vykonávajú baníci, na zaplatenie seba a nikdy by baníkov za ich prácu riadne neodmeňoval. .

Najväčším rizikom pre sieť je riziko spoločného fondu (alebo viacerých spoločných fondov), ktoré majú pod kontrolou viac ako 51 % hashratov sietí, pretože by to mohli použiť na podvádzanie a míňanie prostriedkov dvakrát (dvojité míňanie útok) alebo pokus o zmenu pravidiel siete.

## Čo je p2pool?

p2pool je koncept, ktorý bol pôvodne vytvorený na ťažbu bitcoinov už v roku 2011, ale nikdy nezaznamenal široké uplatnenie a na bitcoinoch zostáva prakticky nepoužívaný. Našťastie, jeden z kľúčových vývojárov RandomX, SCernykh, strávil svoju dovolenku vymýšľaním riešení niektorých problémov s bitcoinovou implementáciou p2pool a prepisovaním všetkého softvéru od začiatku.

p2pool v Monero umožňuje baníkom úplne nedôveryhodným spôsobom spolupracovať pri riešení blokov a zabezpečení siete Monero pomocou špeciálneho softvéru uzlov pre p2pool, aby sa zdieľala práca.

To sa deje pomocou nového blockchainu („side-chain“), ktorý uchováva záznamy o práci, ktorú každý baník vykonáva, adresu ich peňaženky a koľko Monero zarobil, a potom vyplatí odmenu v truste - menej a decentralizovane. Keďže tento vedľajší reťazec má oveľa menej minerov, je oveľa jednoduchšie na ňom nájsť a odoslať bloky ako v hlavnej sieti Monero, čo uľahčuje baníkom konzistentné výplaty oproti ťažbe samotného Monera.

## Ako p2pool rieši problémy pool miningu?

V p2pool neexistuje centralizovaný pool, centralizovaný operátor poolu ani jedna osoba, ktorá drží prostriedky a rozdeľuje výplaty. Všetka práca, ktorú kolektívne vykonávajú tí, ktorí ťažia cez p2pool, je kontrolovaná blockchainom p2pool a inými operátormi uzlov, aby sa zabezpečilo, že je legitímna, a všetci baníci sú vyplatení podľa práce, ktorú vykonali okamžite, keď sa blok nájde priamo od. odmeny v nájdenom bloku.

Keď sa baníci rozhodnú používať p2pool namiesto centralizovaného fondu, odoberú prevádzkovateľom poolu všetku moc a dôveru a zabezpečia, aby ich práca prispievala k dobru siete a ich vlastným odmenám, znížili riziko sieťových útokov, zneužitia ich práce, alebo krádež odmien, ktoré im dlhujú.

Nielenže im to pomáha chrániť ich vlastné záujmy, ale znižuje to riziko, ktoré centralizované fondy môžu predstavovať pre sieť Monero ako celok. Využitie p2pool tiež výrazne pomáha znižovať riziko, ktoré by národné štáty alebo regulačné orgány mohli predstavovať pre zdravie siete, pretože neexistujú centralizovaní prevádzkovatelia poolov, ktorí by museli vyvíjať tlak, žiadna geografická koncentrácia poolov, o ktoré by sa dalo oprieť, ani žiadny iný ľahký bod tlaku, aby ich použili proti Moneru.

## Aké sú nevýhody?

Našťastie bol p2pool v Monero dobre navrhnutý a dobre skonštruovaný a funguje mimoriadne dobre! Hlavnou nevýhodou ťažby p2pool je však to, že každý baník, ktorý chce používať p2pool, musí prevádzkovať svoj vlastný uzol Monero, čo spôsobuje, že proces začínania je o niečo komplikovanejší. Tento uzol sa však potom používa na výpočet všetkých informácií potrebných na zostavenie a kontrolu blokov a zaisťuje, že baník má úplnú kontrolu nad vykonávanou prácou. Uzol môže fungovať aj ako vzdialený uzol pre vlastnú peňaženku baníkov, prispieva do siete a oveľa viac.

Ďalším kľúčovým rozdielom od centralizovanej ťažby je to, že malí baníci používajúci p2pool budú mať o niečo väčšiu "varianciu", čiže čas medzi výplatami, ako veľký centralizovaný fond – ale ' je _mimoriadne_ dôležité poznamenať, že to časom nepovedie k tomu, že budete zarábať menej Monero! p2pool bude časom rovnako ziskový aj pre malých ťažiarov ako centralizované pooly. Niektoré z týchto rozdielov sú tiež kompenzované tým, že p2pool má 0 % poplatky, keďže neexistuje žiadny centralizovaný prevádzkovateľ poolu, ktorý by za ich služby platil!

## Ako môžem začať?

Vďaka vynikajúcemu dizajnu implementácie p2pool spoločnosti Monero' a mnohým ľuďom v komunite, ktorí si našli čas na zjednodušenie procesu ťažby cez p2pool, je začiatok v priebehu času čoraz jednoduchší. Existuje niekoľko spôsobov, ako začať ťažiť pomocou p2pool, ale keďže technické podrobnosti presahujú rozsah tohto článku, v závislosti od vášho operačného systému môžete prejsť na nižšie uvedený odkaz:

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## Ako sa môžem dozvedieť viac?

Ak to vzbudilo vašu zvedavosť ohľadom ťažby p2pool, pozrite si nižšie niekoľko ďalších odkazov a vysvetlení o p2pool, ako to funguje a čo to znamená pre Monero:

  * [Oficiálny Github pre p2pool](https://github.com/SChernykh/p2pool)
  * [Oficiálne dokumenty o používaní p2pool](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool je teraz aktívny](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, "prieskumník blokov" svojho druhu pre p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh: O vývoji P2Pool a decentralizovaného fondu na ťažbu XMR](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

Ďalšie čítanie