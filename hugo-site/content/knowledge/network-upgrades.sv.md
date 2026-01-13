---
title: "Hur Monero använder hard-forks för att uppgradera nätverket"
slug: "network-upgrades"
date: "2022-02-10"
image: "/images/upgrades.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
En av de mest missförstådda delarna av Moneros strategi för att bygga en decentraliserad, integritetsbevarande och säker kryptovaluta är den roll som hårdgaffel (eller nätverksuppgraderingar) spelar.

I det här inlägget går vi igenom vad hårdgafflar är, varför de är viktiga för Monero och vilken roll du kan spela i dem i framtiden.

## Varför behöver Monero fortsätta att uppgradera nätverket?

Monero-communityt har förbundit sig att upprepa och förbättra projektet över tid, och det verkar som att engagemanget kokar ner till två nyckelaspekter av communityns etos:

  1. Monero-projektet är i slutändan mjukvara – kod – skriven av människor. Detta kan leda till ett behov av att fixa buggar, lägga till förbättringar som upptäcks eller uppfinns över tid, implementera moderniseringar av protokollet eller att helt enkelt underhålla projektet. Detta liknar på många sätt de andra programvarorna du använder (som webbläsaren du läser detta i!), som hela tiden måste uppdateras för att kunna lägga till nya funktioner och fixa buggar.

  2. Monero-projektet är ett sekretessverktyg och integritet är en ständigt framskridande kapprustning. De människor och grupper som inget hellre vill än att beröva världen av integritet (både ekonomiskt och personligt) förbättrar, utvecklar och uppfinner ständigt nya sätt att attackera moderna metoder för att bevara integriteten, som de som används i Monero. Eftersom privatlivets fiender hittar dessa nya tillvägagångssätt måste Monero-nätverket kunna anpassa sig och förbättras för att slå tillbaka och försvara vår rätt till ekonomisk integritet.

Monero-projektet är i slutändan mjukvara – kod – skriven av människor. Detta kan leda till ett behov av att fixa buggar, lägga till förbättringar som upptäcks eller uppfinns över tid, implementera moderniseringar av protokollet eller att helt enkelt underhålla projektet. Detta liknar på många sätt de andra programvarorna du använder (som webbläsaren du läser detta i!), som hela tiden måste uppdateras för att kunna lägga till nya funktioner och fixa buggar.

Monero-projektet är ett sekretessverktyg och integritet är en ständigt framskridande kapprustning. De människor och grupper som inget hellre vill än att beröva världen av integritet (både ekonomiskt och personligt) förbättrar, utvecklar och uppfinner ständigt nya sätt att attackera moderna metoder för att bevara integriteten, som de som används i Monero. Eftersom privatlivets fiender hittar dessa nya tillvägagångssätt måste Monero-nätverket kunna anpassa sig och förbättras för att slå tillbaka och försvara vår rätt till ekonomisk integritet.

## Vad är en hårdgaffel?

Komplexiteten i att uppgradera Monero träder i kraft när du förstår hur annorlunda det är att uppgradera en kryptovaluta jämfört med att bara skicka en mjukvaruuppdatering till något som en webbläsare.

I kryptovalutor måste nätverkets regler (saker som hur transaktioner ska se ut, hur gruvdrift fungerar och hur man verifierar varje block) överenskommas av nätverket, något som kallas "konsensus". När någon av dessa regler behöver ändras eller uppgraderas måste nätverket komma överens om de nya reglerna, vilket orsakar en "hard-fork" - en situation där nätverket faktiskt delas upp i två kedjor av block - en på de gamla reglerna, och en om de nya reglerna.

När alla i samhället är överens om regeländringarna kallas det en "icke-kontentiös hårdgaffel", och kedjan som fortfarande har de gamla reglerna dör ut och bryts inte efter hårdgaffeln. Detta har varit fallet för nästan varje Monero hårdgaffel, och den enda fortsättningen på gamla regler var genom projekt som försökte dra nytta av hårdgaffeln.

Medan ostridiga hårdgafflar är det enda sättet att korrekt uppgradera viktiga aspekter av Monero-nätverket, har de också en frustrerande bieffekt – gammal programvara, som släpptes innan hårdgaffeln planerades, kan inte förstå den nya regler för nätverket och så fungerar inte efter hårdgaffeln! Detta kan leda till att användare tror att pengar går förlorade, tror att Monero-blockkedjan har slutat och att de inte kan flytta pengar förrän de uppgraderar sin plånbok.

## Vem bestämmer när Monero-nätverket ska uppgraderas och vad som ska ingå?

Eftersom det inte finns någon central myndighet, VD eller president för Monero, faller arbetet kring att bestämma när nätverket ska uppgraderas, vad som ska inkluderas och hur det ska gå till _us_ , de personer i Monero-gemenskapen som väljer att engagera sig och interagera! Detta är både en extremt viktig del av ett decentraliserat projekt, eftersom planeringen och beslutsfattandet för projektet i slutändan är decentraliserat och samlat från samhället.

Planeringen av timing och funktioner som ingår i varje nätverksuppgradering i Monero sker på två huvudställen:

  1. På IRC och Matrix, de mest använda chattplattformarna i Monero-communityt (som är sammankopplade). Dessa plattformar tillåter stora gruppchattar och är där alla schemalagda Monero-gemenskapsmöten, utvecklarmöten och forskningslabbmöten hålls. Dessa möten är det bästa sättet för dig att lyssna på (eller bidra!) till planeringen och diskussionen kring nätverksuppgraderingar i Monero.

  2. På Github, den huvudsakliga kommunikationsplattformen för mer långvariga Monero-diskussioner, planering och organisation. Monero-communityt använder Github för att organisera möten, diskutera nya funktioner och idéer och koordinera planeringen av nätverksuppgraderingar förutom att lagra koden för Monero-projektet.

På IRC och Matrix, de mest använda chattplattformarna i Monero-communityt (som är sammankopplade). Dessa plattformar tillåter stora gruppchattar och är där alla schemalagda Monero-gemenskapsmöten, utvecklarmöten och forskningslabbmöten hålls. Dessa möten är det bästa sättet för dig att lyssna på (eller bidra!) till planeringen och diskussionen kring nätverksuppgraderingar i Monero.

På Github, den huvudsakliga kommunikationsplattformen för mer långvariga Monero-diskussioner, planering och organisation. Monero-communityt använder Github för att organisera möten, diskutera nya funktioner och idéer och koordinera planeringen av nätverksuppgraderingar förutom att lagra koden för Monero-projektet.

Om du har en viktig idé för en nätverksuppgradering, inte gillar ett tillvägagångssätt eller har funderingar kring tidpunkten för en uppgradering, är det viktigt att du säger till och presenterar ditt ärende tydligt för samhället![X1521X ]

## Hur kan jag hjälpa till med nätverksuppgraderingar?

Eftersom uppgraderingar av Monero-nätverket kräver gemenskapskoordinering och godkännande tillsammans med programuppdateringar, är det oerhört viktigt att så många människor som möjligt engagerar sig i planeringen, testningen och kommunikationsprocessen för nätverksuppgraderingar.

Här är några enkla sätt du kan hjälpa till att smidiga upp kring en nätverksuppgradering:

  1. Gå med i planeringsmötena [ som publicerades på Github](https://github.com/monero-project/meta/issues), lyssna in och bidra om du har något relevant att ta upp.
  2. Kommunicera detaljerna kring nätverksuppgraderingens timing (när du har bestämt dig!) till din favoritbörs, plånbok eller miningpool. Det kan vara svårt att informera alla Monero-användare om en uppgradering, så det är viktigt att vi alla hjälper till där vi kan för att få ut ordet.
  3. Testa programvaran innan nätverksuppgraderingen. Det kommer att skickas ut ett samtal till testare innan nätverksuppgraderingen, både på testnet och stagenet, för att säkerställa att varje aspekt av uppgraderingen har planerats ordentligt för och implementerats i mjukvaran. Ju fler som engagerar sig och testar de nya versionerna noggrant, desto mer sannolikt kommer nätverksuppgraderingen att gå smidigt!
  4. När utgåvor som är kompatibla med nätverksuppgraderingen har publicerats, se till att uppgradera omedelbart! Ju fler som är uppgraderade och redo för nätverksuppgraderingen, desto smidigare kommer nätverket att hantera det och desto mindre huvudvärk kommer användare att uppleva.

## Vad kan jag förvänta mig av nästa uppgradering av Monero-nätverket?

Även om det inte finns ett datum i sten än, kommer det snart att ske en nätverksuppgradering för att implementera några viktiga uppgraderingar och funktioner i Monero:

  1. En ökning av ringstorlek från 11 till 16, vilket ökar basanonymitetsuppsättningen (läs: rimlig förnekelse eller bassekretess) för varje transaktion på nätverket
  2. [Visa taggar, ett briljant sätt att minska plånbokssynkroniseringstider med 30–40 %](/knowledge/view-tags-reduce-monero-sync-time/)
  3. Avgiftsförändringar, förbättrar nätverkets säkerhet och motståndskraft mot snabba förändringar på avgiftsmarknaden eller attacker från skadliga enheter
  4. [Bulletproofs+, en ytterligare förbättring av effektiviteten för Monero-transaktioner](https://www.getmonero.org/2020/12/24/Bulletproofs+-in-Monero.html)

Dessa förändringar kommer att bidra långt till att öka integriteten, effektiviteten och säkerheten i nätverket, samtidigt som de banar väg för [Seraphis](/knowledge/seraphis-for-monero/), nästa generations transaktionsprotokoll för Monero.

## Hur kan jag lära mig mer?

Ämnet hårdgaffel och nätverksuppgraderingar är omfattande och det finns en lång och historisk historia av dem i Monero, så se till att gräva i några av följande länkar om du vill lära dig mer om historik, process eller planering som pågår för den kommande nätverksuppgraderingen!

  * [Monero v15 hårdgaffelplanering](https://github.com/monero-project/meta/issues/630)
  * [Schemalagda mjukvaruuppgraderingar (i Monero)](https://github.com/monero-project/monero#scheduled-software-upgrades)
  * [En notering om schemalagda protokolluppgraderingar](https://web.getmonero.org/2020/09/01/note-scheduled-upgrades.html)

Vidare läsning

  * [Hur Monero unikt möjliggör cirkulära ekonomier](/knowledge/monero-circular-economies/)

  * [Moneros ringsignaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Varför (och hur!) du ska hålla i dina egna nycklar](/knowledge/hold-your-keys/)

  * [Bidrar tillbaka till Monero](/knowledge/contributing-to-monero/)

  * [Hur fjärrnoder påverkar Moneros integritet](/knowledge/remote-nodes-privacy/)

  * [Visa taggar: Hur en byte kommer att minska Monero plånbokssynkroniseringstider med 40% +](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool och dess roll i decentraliseringen av Monero Mining](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Vad det kommer att göra för Monero](/knowledge/seraphis-for-monero/)

  * [Är konvertering av Bitcoin till Monero lika privat som att köpa Monero direkt?](/knowledge/most-private-way-to-buy-monero/)

  * [Varför Monero använder en tillitslös installation till skillnad från Zcash](/knowledge/monero-trustless-setup/)

  * [Varför Monero är en bättre värdebevarare än Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Hur Monero kan övervinna Bitcoins nätverkseffekter](/knowledge/network-effect/)

  * [Varför Monero har den mest kritiskt tänkande gemenskapen](/knowledge/critical-thinking/)

  * [Bedrägerier att se upp för när du använder Monero](/knowledge/monero-scams/)

  * [Hur atombyten kommer att fungera i Monero](/knowledge/monero-atomic-swaps/)

  * [Vad varje Monero-användare behöver veta när det gäller nätverkande](/knowledge/monero-networking/)

  * [Hur RingCT döljer Monero-transaktionsbelopp](/knowledge/monero-ringct/)

  * [Hur Monero Stealth-adresser skyddar din identitet](/knowledge/monero-stealth-addresses/)

  * [Hur Monero-underadresser förhindrar identitetslänkning](/knowledge/monero-subaddresses/)

  * [Monero Utgångar Förklaras](/knowledge/monero-outputs/)

  * [Monero bästa praxis för nybörjare](/knowledge/monero-best-practices/)

  * [Hur ringsignaturer obskyr Moneros utgångar](/knowledge/ring-signatures/)

  * [Hur Monero löste problemet med blockstorlek som plågar Bitcoin](/knowledge/dynamic-block-size/)

  * [Hur CLSAG kommer att förbättra Moneros effektivitet](/knowledge/what-is-clsag/)

  * [Varför Monero har en svans emission](/knowledge/monero-tail-emission/)

  * [En kort historia om Monero](/knowledge/monero-history/)

  * [Wired Magazine har fel om Monero, här är varför](/knowledge/wired-article-debunked/)

  * [Topp 15 Monero myter och bekymmer debunked](/knowledge/monero-myths-debunked/)

  * [Hur Dandelion++ håller Moneros transaktionsursprung privat](/knowledge/monero-dandelion/)

  * [Varför Monero är öppen källkod och decentraliserad](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Vad gör RandomX så speciellt](/knowledge/monero-mining-randomx/)

  * [Varför Monero är bättre än Dash, Zcash, Zcoin (även med Lelantus), Grin och Bitcoin Mixers som Wasabi (Uppdaterad maj 2020)](/knowledge/why-monero-is-better/)