---
title: "Seraphis: Vad det kommer att göra för Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: en modulär designuppgradering för Monero-transaktioner

## Seraphis: en modulär designuppgradering för Monero-transaktioner

Det här inlägget beskriver [Seraphis](https://github.com/UkoeHB/Seraphis), en uppsättning transaktionsprotokollstrukturer och abstraktioner utvecklade av pseudonym forskningsbidragsgivare [`koe`](https://github.com/UkoeHB) för Monero-ekosystemet, och med pågående säkerhetsanalys av pseudonym bidragsgivare [`coinstudent2048`](https://github.com/coinstudent2048).  
Vi gör vissa förenklingar och utelämnar vissa tekniska detaljer för tydlighetens skull; av denna anledning, och eftersom designen av Seraphis fortfarande pågår, bör intresserade läsare hänvisa till Seraphis dokumentation för den senaste informationen.

## Transaktioner i Monero

## Transaktioner i Monero

Protokoll som Bitcoin och Monero och andra förlitar sig på en så kallad "utgångsmodell" för drift, där en _utgång_ är en representation av värde som kan överföras.  
Transaktioner förbrukar en eller flera utdata som kontrolleras av en avsändare och genererar nya utdata riktade mot mottagare (eller tillbaka till avsändaren som ändring); transaktionen måste balansera genom att förbrukade utdata måste innehålla ett totalt värde som är exakt lika med värdet i nya utdata (plus en nätverkspålagd avgift).  
I många protokoll som Bitcoin skrivs värdet i en utdata i klartext, liksom mottagaren.  
Dessutom, genom att titta på blockkedjan, är det trivialt att se om och när en utdata har förbrukats (det vill säga om den har förbrukats i en senare transaktion, och vilken transaktion som använde den).

Däremot introducerar protokoll som Monero en annan design:

  * Utdatavärden är dolda och inte synliga i blockkedjan
  * Mottagaradresser är dolda genom användning av ett engångsadresseringsprotokoll
  * Om en utdata har förbrukats eller inte fördunklas av användningen av tvetydiga signaturer

Resultatet är att det, i frånvaro av extern information, är svårt att avgöra om en given utdata har spenderats, vad dess värde är och vem dess mottagare är.

Det nuvarande Monero-transaktionsprotokollet kallas _RingCT_ och använder flera kryptografiska byggstenar för att uppnå dessa designmål.

  * _Åtaganden_ döljer belopp på ett matematiskt användbart sätt
  * _Räckviddssäkringar_ förhindrar spill som kan blåsa upp försörjningen
  * _Länkbara ringsignaturer_ ger undertecknarens tvetydighet och förhindrar försök med dubbla utgifter
  * _Åtagandeförskjutningar_ hävdar att transaktioner balanserar

Dessa byggstenar är noggrant sammanflätade för att bygga RingCT-protokollet.

En användbar egenskap hos RingCT-protokollet är att vissa byggstenar kan ändras eller uppgraderas på ett sätt som håller den övergripande designen och egenskaperna intakta, men som kan ge effektivitets- eller säkerhetsförbättringar. Faktum är att den här typen av uppgraderingar har inträffat (eller planeras att ske) flera gånger i Moneros historia. Räckviddsbevis i det ursprungliga RingCT-protokollet var skrymmande och långsamma; de uppdaterades senare till en konstruktion som heter [Bulletproofs](https://eprint.iacr.org/2017/1066) som gjorde transaktioner mindre och snabbare med bättre säkerhetsanalys, och är planerade att uppdateras till en nyare konstruktion som heter [Bulletproofs+](https://eprint.iacr.org/2020/735) för ännu större effektivitetsfördelar. 

En liknande process genomgicks med den länkbara ringsignaturbyggstenen. I det ursprungliga protokollet användes en konstruktion som heter [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34). Detta uppdaterades senare till en nyare konstruktion som heter [CLSAG](https://eprint.iacr.org/2019/654) som är snabbare, resulterar i mindre transaktioner och har bättre säkerhetsanalys. En ännu nyare länkbar ringsignaturkonstruktion baserad på [Triptyk](https://eprint.iacr.org/2020/018) föreslogs, men denna valdes inte för distribution på grund av dess inverkan på multisignaturoperationer.

## Seraphis

## Seraphis

Seraphis tar denna idé ett steg längre.  
Istället för att uppdatera enskilda byggstenar i det befintliga transaktionsprotokollet RingCT, introduceras ett nytt protokoll som kan dra nytta av olika byggstenar och erbjuda förbättrad funktionalitet.

## Byggklossar

## Byggklossar

Seraphis använder en annan uppsättning kryptografiska byggstenar för att uppnå sina designmål.

  * _Åtaganden_ döljer fortfarande belopp
  * _Räckviddssäkringar_ förhindrar fortfarande översvämning och försörjningsuppblåsning
  * _Medlemskapsbevis_ ger undertecknarens tvetydighet
  * _Åtagandeförskjutningar_ hävdar fortfarande balans
  * _Auktoriserande korrektur_ förhindrar försök med dubbla utgifter

Lägg märke till ändringen här: länkbara ringsignaturer ersätts med en kombination av medlemskapsbevis och auktoriseringsbevis. Grovt sett visar medlemsbevis att en konsumerad utdata är en del av en större uppsättning, liknande vad som händer i RingCT. Men till skillnad från RingCT involverar medlemskapsbevis inte länktaggen alls! Auktoriseringsbevis visar att länktaggen är giltig och används för att underteckna den slutliga transaktionen.

Eftersom RingCT bakar in länktaggen i den tvetydiga signaturen, är signering (och multisignatur) operationer mer beräkningsintensiva, och det blir mer utmanande att bygga andra taggrelaterade funktioner. Men i Seraphis kan konstruktion av medlemsbevis på ett säkert sätt delegeras från mycket pålitliga enheter (som kan ha begränsad datorkraft, som en hårdvaruplånbok) till en mindre pålitlig enhet, och signering (och multisignatur) är mycket enklare med det mycket enklare auktoriseringsbeviset .

Lyckligtvis finns några av byggstenarna som krävs av Seraphis redan någon annanstans och behöver inte designas från grunden. Både Bulletproofs och Bulletproofs+ konstruktionerna kan användas som räckviddsbevis. Modifieringar av provningssystem av Schnorr-typ kan användas för att auktorisera bevis. Och ett effektivt [provningssystem](https://eprint.iacr.org/2015/643) som redan används som bas för Triptych, [Lelantus](https://eprint.iacr.org/2019/373) och [Spark](https://eprint.iacr.org/2021/1173)* kan modifieras för medlemskapsbevis. X2127X] 

* Cypher Stack får finansiering för Spark-utveckling.

Seraphis använder en annan uppsättning kryptografiska byggstenar för att uppnå sina designmål.

  * _Åtaganden_ döljer fortfarande belopp
  * _Räckviddssäkringar_ förhindrar fortfarande översvämning och försörjningsuppblåsning
  * _Medlemskapsbevis_ ger undertecknarens tvetydighet
  * _Åtagandeförskjutningar_ hävdar fortfarande balans
  * _Auktoriserande korrektur_ förhindrar försök med dubbla utgifter

Lägg märke till ändringen här: länkbara ringsignaturer ersätts med en kombination av medlemskapsbevis och auktoriseringsbevis. Grovt sett visar medlemsbevis att en konsumerad utdata är en del av en större uppsättning, liknande vad som händer i RingCT. Men till skillnad från RingCT involverar medlemskapsbevis inte länktaggen alls! Auktoriseringsbevis visar att länktaggen är giltig och används för att underteckna den slutliga transaktionen.

Eftersom RingCT bakar in länktaggen i den tvetydiga signaturen, är signering (och multisignatur) operationer mer beräkningsintensiva, och det blir mer utmanande att bygga andra taggrelaterade funktioner. Men i Seraphis kan konstruktion av medlemsbevis på ett säkert sätt delegeras från mycket pålitliga enheter (som kan ha begränsad datorkraft, som en hårdvaruplånbok) till en mindre pålitlig enhet, och signering (och multisignatur) är mycket enklare med det mycket enklare auktoriseringsbeviset .

Lyckligtvis finns några av byggstenarna som krävs av Seraphis redan någon annanstans och behöver inte designas från grunden. Både Bulletproofs och Bulletproofs+ konstruktionerna kan användas som räckviddsbevis. Modifieringar av provningssystem av Schnorr-typ kan användas för att auktorisera bevis. Och ett effektivt [provningssystem](https://eprint.iacr.org/2015/643) som redan används som bas för Triptych, [Lelantus](https://eprint.iacr.org/2019/373) och [Spark](https://eprint.iacr.org/2021/1173)* kan modifieras för medlemskapsbevis. X2127X] 

* Cypher Stack får finansiering för Spark-utveckling.

* Cypher Stack får finansiering för Spark-utveckling.

## Adressering

## Adressering

Tyvärr är de Monero-adresser som används för närvarande inte kompatibla med Seraphis. Användarna skulle behöva generera nya adresser från sina plånboksnycklar för att kunna ta emot Monero om Seraphis implementerades. Denna kostnad för ekosystemet kommer dock med en mängd fördelar.

Bortsett från de strukturella fördelar som diskuterats ovan, är Seraphis design mottaglig för många olika adresskonstruktionsmöjligheter, som var och en kommer med kompromisser. Även om den slutliga adresskonstruktionen som ska användas i Seraphis är [beslutas fortfarande](https://github.com/monero-project/research-lab/issues/92) (ett schema som får mycket uppmärksamhet kallas [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), kan vi beskriva några vanliga och användbara funktioner.[X908X ] 

Du kanske vet att Monero-adresser erbjuder _vynyckel_ -funktion, där du kan tillhandahålla en vynyckel till en enhet eller tredje part och låta den titta efter inkommande utdata för din räkning, men utan att ge upp utgifterna auktoritet. Detta är användbart för plånböcker, som kan hålla sig uppdaterade samtidigt som du håller din utgiftsnyckel säkert inlåst. Det är också användbart för fall där du vill ha tillgång till extern vy, som en offentlig välgörenhetsorganisation som erbjuder transparens eller ett företag med en redovisningsavdelning.

Nackdelen med Monero-vynycklar är att de inte ger fullständig eller finkornig vyåtkomst. Det är inte möjligt att på ett tillförlitligt sätt upptäcka när en plånbok spenderar pengar, vilket gör det svårt att beräkna plånbokssaldon ordentligt när utgiftsnyckeln inte är tillgänglig. Det är för närvarande inte heller möjligt att upptäcka inkommande utdata utan att också lära sig värdet som finns i dessa utdata (vilket innebär att alla tredje parter som ansvarar för att hitta inkommande utdata kommer att lära sig exakt hur mycket Monero du skaffar).

Seraphis adresseringskonstruktioner kan lösa detta. Med Seraphis är din adress utrustad med olika nycklar som kan göra olika saker:

  * Se upp för inkommande utgångar, men dölj deras värde
  * Se upp för inkommande utgångar, men visa deras värde
  * Se upp för utgående utgångar
  * Hjälper dig att generera transaktioner, men inte signera dem
  * Skapa nya adresser (användbart för återförsäljare eller utbyten med många kunder)

Som adressinnehavare får du bestämma hur mycket behörighet du delegerar till andra enheter eller tredje part.

Du kanske vet att Monero-adresser erbjuder _vynyckel_ -funktion, där du kan tillhandahålla en vynyckel till en enhet eller tredje part och låta den titta efter inkommande utdata för din räkning, men utan att ge upp utgifterna auktoritet. Detta är användbart för plånböcker, som kan hålla sig uppdaterade samtidigt som du håller din utgiftsnyckel säkert inlåst. Det är också användbart för fall där du vill ha tillgång till extern vy, som en offentlig välgörenhetsorganisation som erbjuder transparens eller ett företag med en redovisningsavdelning.

Nackdelen med Monero-vynycklar är att de inte ger fullständig eller finkornig vyåtkomst. Det är inte möjligt att på ett tillförlitligt sätt upptäcka när en plånbok spenderar pengar, vilket gör det svårt att beräkna plånbokssaldon ordentligt när utgiftsnyckeln inte är tillgänglig. Det är för närvarande inte heller möjligt att upptäcka inkommande utdata utan att också lära sig värdet som finns i dessa utdata (vilket innebär att alla tredje parter som ansvarar för att hitta inkommande utdata kommer att lära sig exakt hur mycket Monero du skaffar).

Seraphis adresseringskonstruktioner kan lösa detta. Med Seraphis är din adress utrustad med olika nycklar som kan göra olika saker:

  * Se upp för inkommande utgångar, men dölj deras värde
  * Se upp för inkommande utgångar, men visa deras värde
  * Se upp för utgående utgångar
  * Hjälper dig att generera transaktioner, men inte signera dem
  * Skapa nya adresser (användbart för återförsäljare eller utbyten med många kunder)

Som adressinnehavare får du bestämma hur mycket behörighet du delegerar till andra enheter eller tredje part.

## Den stora bilden

## Den stora bilden

Seraphis är en stor förändring av Monero-ekosystemet. Även om det innebär ändringar av adresser och transaktionsbyggstenar, erbjuder dess design flexibilitet och användbar funktionalitet som inte är möjliga med dagens RingCT-protokoll. Även om mycket av designen är färdigställd och utvecklas till [en implementering](https://github.com/UkoeHB/monero/tree/seraphis_lib), pågår adressdesign och säkerhetsanalys. Seraphis erbjuder ett utmärkt tillfälle att driva Monero-ekosystemet framåt!

Vidare läsning

  * [Hur Monero unikt möjliggör cirkulära ekonomier](/knowledge/monero-circular-economies)/

  * [Moneros ringsignaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Varför (och hur!) du ska hålla i dina egna nycklar](/knowledge/hold-your-keys)/

  * [Bidrar tillbaka till Monero](/knowledge/contributing-to-monero)/

  * [Hur fjärrnoder påverkar Moneros integritet](/knowledge/remote-nodes-privacy)/

  * [Hur Monero använder hard-forks för att uppgradera nätverket](/knowledge/network-upgrades)/

  * [Visa taggar: Hur en byte kommer att minska Monero plånbokssynkroniseringstider med 40% +](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool och dess roll i decentraliseringen av Monero Mining](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Är konvertering av Bitcoin till Monero lika privat som att köpa Monero direkt?](/knowledge/most-private-way-to-buy-monero)/

  * [Varför Monero använder en tillitslös installation till skillnad från Zcash](/knowledge/monero-trustless-setup)/

  * [Varför Monero är en bättre värdebevarare än Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Hur Monero kan övervinna Bitcoins nätverkseffekter](/knowledge/network-effect)/

  * [Varför Monero har den mest kritiskt tänkande gemenskapen](/knowledge/critical-thinking)/

  * [Bedrägerier att se upp för när du använder Monero](/knowledge/monero-scams)/

  * [Hur atombyten kommer att fungera i Monero](/knowledge/monero-atomic-swaps)/

  * [Vad varje Monero-användare behöver veta när det gäller nätverkande](/knowledge/monero-networking)/

  * [Hur RingCT döljer Monero-transaktionsbelopp](/knowledge/monero-ringct)/

  * [Hur Monero Stealth-adresser skyddar din identitet](/knowledge/monero-stealth-addresses)/

  * [Hur Monero-underadresser förhindrar identitetslänkning](/knowledge/monero-subaddresses)/

  * [Monero Utgångar Förklaras](/knowledge/monero-outputs)/

  * [Monero bästa praxis för nybörjare](/knowledge/monero-best-practices)/

  * [Hur ringsignaturer obskyr Moneros utgångar](/knowledge/ring-signatures)/

  * [Hur Monero löste problemet med blockstorlek som plågar Bitcoin](/knowledge/dynamic-block-size)/

  * [Hur CLSAG kommer att förbättra Moneros effektivitet](/knowledge/what-is-clsag)/

  * [Varför Monero har en svans emission](/knowledge/monero-tail-emission)/

  * [En kort historia om Monero](/knowledge/monero-history)/

  * [Wired Magazine har fel om Monero, här är varför](/knowledge/wired-article-debunked)/

  * [Topp 15 Monero myter och bekymmer debunked](/knowledge/monero-myths-debunked)/

  * [Hur Dandelion++ håller Moneros transaktionsursprung privat](/knowledge/monero-dandelion)/

  * [Varför Monero är öppen källkod och decentraliserad](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: Vad gör RandomX så speciellt](/knowledge/monero-mining-randomx)/

  * [Varför Monero är bättre än Dash, Zcash, Zcoin (även med Lelantus), Grin och Bitcoin Mixers som Wasabi (Uppdaterad maj 2020)](/knowledge/why-monero-is-better)/

Vidare läsning