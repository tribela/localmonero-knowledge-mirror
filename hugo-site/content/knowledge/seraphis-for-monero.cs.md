---
title: "Seraphis: Co to udělá pro Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: upgrade modulárního designu pro transakce Monero

Tento příspěvek popisuje [Seraphis](https://github.com/UkoeHB/Seraphis), sadu struktur a abstrakcí transakčních protokolů vyvinutých pseudonymním výzkumným přispěvatelem [`koe`](https://github.com/UkoeHB) pro ekosystém Monero a s probíhající bezpečnostní analýzou od pseudonymního přispěvatele [`coinstudent2048`](https://github.com/coinstudent2048).  
V zájmu přehlednosti se dopouštíme některých zjednodušení a vynecháváme některé technické detaily; z tohoto důvodu a vzhledem k tomu, že na návrhu systému Seraphis se stále pracuje, by se zájemci měli obrátit na dokumentaci systému Seraphis, kde naleznou nejaktuálnější informace.

## Transakce v Monero

Protokoly jako Bitcoin a Monero a další spoléhají na takzvaný „výstupní model“ provozu, kde _výstup_ představuje reprezentaci hodnoty, kterou lze převést.  
Transakce spotřebovávají jeden nebo více výstupů kontrolovaných odesílatelem a vytvářejí nové výstupy směřující k příjemcům (nebo zpět k odesílateli jako změna); transakce musí být vyvážená v tom smyslu, že spotřebované výstupy musí obsahovat celkovou hodnotu přesně rovnou hodnotě v nových výstupech (plus síťový poplatek).  
V mnoha protokolech, jako je Bitcoin, je hodnota obsažená ve výstupu zapsána otevřeně, stejně jako příjemce.  
Kromě toho je při pohledu do blockchainu triviální zjistit, zda a kdy byl výstup utracen (tj. zda byl spotřebován v pozdější transakci a která transakce jej utratila).

Naproti tomu protokoly jako Monero zavádějí jiný design:

  * Výstupní hodnoty jsou skryté a nejsou viditelné na blockchainu
  * Adresy příjemců jsou skryté pomocí jednorázového adresovacího protokolu
  * To, zda byl výstup utracen či nikoli, je zakryto použitím nejednoznačných podpisů

Výsledkem je, že bez vnějších informací je obtížné určit, zda byl daný výstup vynaložen, jaká je jeho hodnota a kdo je jeho příjemce.

Aktuální transakční protokol Monero se nazývá _RingCT_ a k dosažení těchto cílů návrhu používá několik kryptografických stavebních bloků.

  * _Závazky_ skrývají částky matematicky užitečným způsobem
  * _Důkazy dosahu_ zabraňují přetečení, které by mohlo nafouknout nabídku
  * _Propojitelné kruhové podpisy_ zajišťují nejednoznačnost signatáře a zabraňují pokusům o dvojnásobnou útratu
  * _Kompenzace závazků_ tvrdí, že transakce jsou vyrovnané

Tyto stavební bloky jsou pečlivě propojeny, aby vytvořily protokol RingCT.

Užitečnou vlastností protokolu RingCT je to, že některé stavební bloky lze změnit nebo upgradovat způsobem, který zachová celkový design a vlastnosti nedotčené, ale může to zajistit zlepšení účinnosti nebo zabezpečení. Ve skutečnosti k těmto druhům upgradů došlo (nebo se plánuje, že k nim dojde) několikrát v historii společnosti Monero. Důkazy rozsahu v původním protokolu RingCT byly objemné a pomalé; později byly aktualizovány na konstrukci nazvanou [Bulletproofs](https://eprint.iacr.org/2017/1066), která zmenšila a zrychlila transakce s lepší analýzou zabezpečení, a plánuje se jejich aktualizace na novější konstrukci nazvanou [Bulletproofs+](https://eprint.iacr.org/2020/735) pro ještě vyšší efektivitu. 

Podobný proces byl proveden se stavebním blokem propojitelného kruhového podpisu. V původním protokolu byla použita konstrukce nazvaná [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34). Toto bylo později aktualizováno na novější konstrukci nazvanou [CLSAG](https://eprint.iacr.org/2019/654), která je rychlejší, vede k menším transakcím a má lepší analýzu zabezpečení. Byla navržena ještě novější konstrukce propojitelného kruhového podpisu založená na [Triptychu](https://eprint.iacr.org/2020/018), která však nebyla vybrána pro nasazení kvůli jejím dopadům na operace s více podpisy.

## Seraphis

Seraphis jde v této myšlence ještě dál.  
Namísto aktualizace jednotlivých stavebních bloků stávajícího transakčního protokolu RingCT zavádí jiný protokol, který může využívat různé stavební bloky a nabízet lepší funkce.

## Stavební bloky

Seraphis používá k dosažení svých cílů jinou sadu kryptografických bloků.

  * _Závazky_ stále skrývají částky
  * _Důkazy dosahu_ stále brání přetečení a inflaci nabídky
  * _Důkazy o členství_ poskytují nejednoznačnost signatáře
  * _Kompenzace závazků_ stále uplatňují rovnováhu
  * _Důkazy o autorizaci_ zabraňují pokusům o dvojnásobnou útratu

Všimněte si změny: propojitelné kruhové podpisy jsou nahrazeny kombinací důkazů členství a autorizačních důkazů. Zhruba řečeno, důkazy o členství ukazují, že spotřebovaný výstup je součástí větší množiny, podobně jako je tomu v RingCT. Na rozdíl od RingCT však důkazy o členství vůbec nezahrnují propojovací značku! Důkazy o autorizace ukazují, že propojovací značka je platná, a používají se k podpisu konečné transakce.

Protože RingCT zapracovává propojovací značku do nejednoznačného podpisu, jsou operace podepisování (a vícepodepisování) výpočetně náročnější a je náročnější vytvořit další funkce související se značkou. V Seraphis však lze konstrukci důkazů o členství bezpečně delegovat z vysoce důvěryhodných zařízení (která mohou mít omezený výpočetní výkon, jako například hardwarová peněženka) na méně důvěryhodné zařízení a operace podepisování (a vícepodepisování) jsou mnohem jednodušší pomocí mnohem jednoduššího autorizačního důkazu.

Některé stavební bloky požadované Seraphisem již naštěstí existují jinde a není třeba je navrhovat od začátku. Konstrukce Bulletproofs i Bulletproofs+ mohou být použity jako nátisky. Pro autorizační nátisky lze použít modifikace dokazovacích systémů typu Schnorr. A účinný [provingový systém](https://eprint.iacr.org/2015/643) používaný již jako základ pro Triptych, [Lelantus](https://eprint.iacr.org/2019/373) a [Spark](https://eprint.iacr.org/2021/1173)* může být upraven pro důkazy o členství.

* Cypher Stack získává finanční prostředky na vývoj Spark.

## Adresování

Aktuálně používané adresy Monero bohužel nejsou se Seraphis kompatibilní. Uživatelé by si museli vygenerovat nové adresy ze svých klíčů peněženek, aby mohli přijímat Monero, pokud by byl Seraphis implementován. Tyto náklady na ekosystém však s sebou nesou řadu výhod.

Kromě výše uvedených konstrukčních výhod je konstrukce Seraphis vhodná pro mnoho různých možností konstrukce adres, z nichž každá má své kompromisy. Zatímco konečná konstrukce adresy, která bude použita v systému Seraphis, je [ stále rozhodována](https://github.com/monero-project/research-lab/issues/92) (jedno schéma, kterému je věnována velká pozornost, se nazývá [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), můžeme popsat některé běžné a užitečné funkce.

Možná víte, že adresy Monero nabízejí funkci _klíč zobrazení_ , kdy můžete zařízení nebo třetí straně poskytnout klíč pro zobrazení a umožnit jí sledovat příchozí výstupy vaším jménem, aniž byste se vzdali pravomocí k utrácení. To je užitečné pro peněženky, které mohou zůstat aktualizované, zatímco váš výdajový klíč zůstane bezpečně uzamčen. Je to užitečné také v případech, kdy chcete mít přístup k zobrazení zvenčí, například pro veřejnou charitu nabízející transparentnost nebo pro společnost s účetním oddělením.

Nevýhodou klíčů zobrazení Monero je, že neposkytují úplný nebo jemný přístup k zobrazení. Není možné spolehlivě zjistit, kdy peněženka utrácí prostředky, což ztěžuje správný výpočet zůstatků peněženek, když není k dispozici klíč pro utrácení. V současné době také není možné zjistit příchozí výstupy, aniž by se zároveň nezjistila hodnota obsažená v těchto výstupech (což znamená, že jakákoli třetí strana odpovědná za zjišťování příchozích výstupů se dozví, kolik přesně Monero získáváte).

Adresní konstrukce Seraphis to mohou vyřešit. Díky systému Seraphis je vaše adresa vybavena různými klíči, které mohou dělat různé věci:

  * Sledovat příchozí výstupy, ale skrýt jejich hodnotu
  * Sledovat příchozí výstupy, ale ukázat jejich hodnotu
  * Sledovat odchozí výstupy
  * Pomoci vám generovat transakce, ale nepodepisovat je
  * Generovat nové adresy (užitečné pro maloobchodníky nebo burzy s mnoha zákazníky)

Jako držitel adresy se můžete rozhodnout, kolik pravomocí delegujete na jiná zařízení nebo třetí strany.

## Celkový obraz

Seraphis je velkou změnou v ekosystému Monero. I když zahrnuje úpravy adres a stavebních bloků transakcí, jeho design nabízí flexibilitu a užitečné funkce, které dnešní protokol RingCT neumožňuje. Zatímco velká část návrhu je dokončena a rozvíjena do [implementace](https://github.com/UkoeHB/monero/tree/seraphis_lib), návrh adres a analýza zabezpečení stále pokračují. Seraphis nabízí vynikající příležitost, jak posunout ekosystém Monero vpřed!

Další čtení