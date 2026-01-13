---
title: "Monerové kruhové podpisy vs CoinJoin jako ve Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
S tím, jak si nástroje pro ochranu soukromí u Bitcoinu získaly větší pozornost a používání, dostaly se pod větší kontrolu regulačních orgánů. Tato kontrola vedla k [ nedávnému oznámení](https://twitter.com/wasabiwallet/status/1503091503207432193) nástroje pro ochranu soukromí Bitcoinu, peněženky Wasabi, že začne cenzurovat a odmítat příchozí vstupy do mixů, které považuje za nezákonné nebo v rozporu se svými ToS, a bude platit společnosti zabývající se analýzou řetězců, aby "prověřovala" příchozí účastníky mixů.

Používání transakcí CoinJoin k zastření zdroje finančních prostředků v Bitcoinu je již mnoho let jádrem soukromí Bitcoinu a problémy a rizika spojená s jeho používáním patří k základním problémům, které kruhové podpisy Monero napravují a zabraňují jim.

V tomto blogovém příspěvku se krátce podíváme na srovnání CoinJoinu a kruhových podpisů a také na to, proč přístup použitý v Moneru vede k větší odolnosti vůči cenzuře, většímu soukromí a menším potížím pro uživatele.

## Co je to transakce CoinJoin?

Jelikož jsou všechny transakce v Bitcoinu zcela transparentní - odhalují odesílatele, příjemce a částky -, musí uživatelé podniknout další kroky k ochraně svého soukromí před předchozími odesílateli a budoucími příjemci svých prostředků, jinak riskují cenzuru, sledování nebo krádež prostředků prostřednictvím fyzického násilí.

Nejlepším řešením ochrany soukromí v Bitcoinu je dnes nástroj zvaný ["CoinJoin"](https://bitcoiner.guide/qna/coinjoin/), kde dva nebo více uživatelů spolupracují (obvykle prostřednictvím centralizovaného koordinátora) na vytvoření speciální transakce, která vnějším pozorovatelům ztěžuje propojení vstupů s výstupy. Každý účastník komunikuje, aby společně vytvořil transakci, aniž by předal dohled nad svými prostředky, a na konci obdrží výstup, jehož předchozí historie je nyní pro vnější pozorovatele nejasná (nebo zastřená).

Tím se přeruší historie konkrétních UTXO, což uživatelům Bitcoinu umožní získat při transakcích určitou míru utajení. CoinJoin (jak je implementován v peněžence Wasabi a peněžence Samourai, dvou nejpoužívanějších nástrojích CoinJoin pro Bitcoin) má však několik zásadních nevýhod:

  * Vzhledem k tomu, že transakce CoinJoin jsou zcela opt-in a vyžadují aktivní účast, každý účastník nutně ukazuje, že usiluje o větší soukromí než "normální" uživatelé Bitcoinu, což je může vyčlenit a způsobit problémy s utrácením finančních prostředků na mnoha regulovaných burzách nebo u mnoha subjektů. Každý uživatel nemůže popřít, že se zúčastnil transakce CoinJoin.
  * Většina přístupů k CoinJoinu (včetně peněženky Wasabi) využívá centralizovaného koordinátora, který spojuje účastníky a pomáhá jim komunikovat a vytvořit správnou transakci CoinJoinu. Tento centralizovaný koordinátor nikdy nedisponuje finančními prostředky uživatelů, ale získává rozsáhlý přehled o transakcích, které koordinuje, může cenzurovat příchozí vstupy (jako v případě Wasabi Wallet) a může na něj být vyvíjen nátlak, aby shromažďoval nebo sdílel informace o účastnících CoinJoinu.
. ] 
  * Uživatelé s velkým množstvím finančních prostředků na CoinJoin mohou často čekat hodiny (nebo dokonce dny!), než najdou dostatek účastníků na CoinJoin, což vede k velkým prodlevám od okamžiku, kdy uživatel obdrží finanční prostředky, do okamžiku, kdy je může soukromě utratit.
  * Soukromí poskytované transakcí CoinJoin se v průběhu času zhoršuje, protože ostatní účastníci utrácejí finanční prostředky nebo spojují své výstupy se svou identitou prostřednictvím burz KYC, obchodníků vyžadujících průkaz totožnosti atd. To znamená, že uživatelé v ideálním případě udržují své prostředky v transakcích CoinJoin neustále v chodu, aby byla jejich sada anonymity ("dav, v němž se mohou skrývat") co nejčerstvější.
  * Ve většině přístupů k CoinJoinu musí účastníci používat UTXO pevné velikosti (tj. 0,1 BTC), aby bylo obtížnější propojit vstupy a výstupy transakcí CoinJoinu. To vede k vyšším poplatkům (na jeden velký vstup je potřeba více samostatných transakcí), většímu množství "toxických drobných" (prostředků, které nelze utratit bez vážného ohrožení soukromí) a může vyloučit, aby menší uživatelé vůbec mohli mixovat, pokud nemají požadovaný minimální zůstatek.

## Jak kruhové podpisy řeší tyto problémy?

Protože [v minulosti jsme se již podrobně zabývali tím, co jsou kruhové podpisy](/znalosti/kroužkové podpisy), nebudu se v tomto příspěvku věnovat technickým aspektům jejich fungování. Místo toho se podíváme na to, jak přístupy použité v Moneru řeší problémy s CoinJoin, o kterých je řeč výše.

> CoinJoin je opt-in a vyžaduje účast

Kruhové podpisy Monero jsou základním prvkem protokolu pro ochranu soukromí a _každá_ transakce v síti je používá. To znamená, že transakce žádného uživatele nevynikají snahou o větší soukromí než u "běžných" uživatelů Monera a všichni uživatelé získávají věrohodné popření, že v dané transakci utratili finanční prostředky. Vzhledem k tomu, že uživatel, který utrácí finanční prostředky, nekoordinuje ani se nepodílí na transakci s návnadovými vstupy, mohou ti uživatelé, kteří vlastní vstupy, jež byly náhodou vybrány jako návnady, čestně prohlásit, že se dané transakce neúčastnili, což posiluje jejich soukromí.

> Použití centralizovaného koordinátora

Protože kruhové podpisy Monero jsou zcela nekoordinované a k vytvoření transakce je zapotřebí pouze skutečný odesílatel prostředků, není v Moneru potřeba žádný centralizovaný koordinátor. To zajišťuje, že vám _nikdo_ nemůže odepřít přístup k soukromí v Moneru a neexistuje žádný centralizovaný subjekt, na který by bylo možné vyvíjet nátlak, žádné snadné útoky Sybil na likviditu atd. Pokud za svou transakci zaplatíte příslušné poplatky, získáte v Moneru necenzurovatelný přístup k soukromí, bezpečnosti a anonymitě.

> CoinJoin vyžaduje likviditu

"Likvidita", kterou může každý, kdo utrácí Monero, použít jako návnady, je vždy celková sada výstupů v řetězci, takže nikdy není nedostatek návnad, do kterých se lze s Monerem schovat. Někdo, kdo chce utratit Monero, tak může učinit ~20min po obdržení prostředků a nemusí provádět žádné další kroky, aby získal silné soukromí v Moneru.

> Soukromí CoinJoin se časem snižuje

Jelikož výstupy Monero nejsou nikdy známé a síť je nikdy nevydá, je soukromí poskytované kruhovými podpisy mnohem méně náchylné k degradaci v průběhu času. Uživatel nemusí neustále měnit výstupy v Moneru a mimo extrémně vzácné okolnosti neztrácí s postupem času žádné soukromí.

Pokud však uživatel chce "obnovit" návnady použité s výstupem, může si pouze poslat prostředky zpět a může je utratit o ~20min později jako obvykle.

> CoinJoin obvykle vyžaduje vstupy pevné velikosti

Jelikož jsou částky v každé transakci skryty pomocí ["Důvěrné transakce"](/znalosti/monero-ringct) (součást "RingCT"), mohou být návnady použité v dané transakci libovolně velké. V Moneru není žádný důvod, proč by se měl někdo obávat heuristiky založené na množství, a proto je sestavování transakcí mnohem jednodušší a v blockchainu Monero mohou být použity návnady z libovolného časového bodu a o libovolném množství.

## Jak se mohu dozvědět více?

Pokud jste zvědaví a chcete lépe porozumět kruhovým podpisům nebo transakcím CoinJoin, podívejte se na níže uvedené odkazy, kde najdete skvělá místa kde začít:

  * [Jak prstenové podpisy zakrývají výstupy Monera](/knowledge/ring-signatures)
  * [Ring Signature – Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [Přehled CoinJoin](https://6102bitcoin.com/coinjoin-overview/)

Další čtení