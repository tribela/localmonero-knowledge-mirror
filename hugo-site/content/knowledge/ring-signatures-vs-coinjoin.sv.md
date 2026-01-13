---
title: "Moneros ringsignaturer vs CoinJoin som i Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Eftersom Bitcoins integritetsverktyg har fått mer uppmärksamhet och användning har de kommit under mer regulatorisk granskning. Denna granskning har lett till ett [nyligen tillkännagivande](https://twitter.com/wasabiwallet/status/1503091503207432193) av ett Bitcoin-integritetsverktyg, Wasabi Wallet, att de kommer att börja censurera och avvisa inkommande indata till blandningar som de anser vara olagliga eller mot deras användarvillkor, och kommer att betala en kedjeanalys företag för att "veta" inkommande mixdeltagare.

Användningen av CoinJoin-transaktioner för att fördunkla källan till pengar i Bitcoin har varit kärnan i Bitcoins integritet i många år nu, och de problem och risker som är inneboende i användningen är några av de kärnproblem som Moneros ringsignaturer korrigerar och förhindrar. .

I det här blogginlägget ska vi kort dyka ner i en jämförelse av CoinJoin och ringsignaturer, samt varför tillvägagångssättet i Monero leder till större censurmotstånd, större integritet och mindre krångel för användarna.

## Vad är en CoinJoin transaktion?

Eftersom alla transaktioner är helt transparenta i Bitcoin - avsändare, mottagare och belopp - måste användare vidta extra åtgärder för att skydda sin integritet från tidigare avsändare och framtida mottagare av deras pengar eller riskera censur, övervakning eller stöld av pengar genom fysiskt våld.

Den bästa lösningen idag för integritet på Bitcoin är ett verktyg som heter [“CoinJoin”](https://bitcoiner.guide/qna/coinjoin/), där 2 eller fler användare arbetar tillsammans (vanligtvis via en centraliserad koordinator) för att skapa en speciell transaktion som gör det svårt för utomstående observatörer att koppla samman ingångarna med utgångarna. Varje deltagare kommunicerar för att gemensamt bygga transaktionen utan att ge över kontrollen av sina medel, och får i slutet en output vars tidigare historia nu är oklar (eller fördunklad) för utomstående observatörer.

Detta bryter historiken för specifika UTXO:er, vilket gör att Bitcoin-användare kan få lite av framåtsekretess när de gör transaktioner. Men CoinJoin (som implementerat i Wasabi Wallet och Samourai Wallet, de två mest använda CoinJoin-verktygen för Bitcoin) har några stora nackdelar:

  * Eftersom CoinJoin-transaktioner är helt opt-in och kräver aktivt deltagande, visar alla deltagare nödvändigtvis att de söker större integritet än "normala" Bitcoin-användare, vilket potentiellt pekar ut dem och orsakar problem med att spendera pengar på många reglerade börser eller enheter. Varje användare kan inte förneka att de deltog i en CoinJoin-transaktion.
  * För att hitta andra att CoinJoin med använder de flesta metoder för CoinJoin (inklusive Wasabi Wallet) en centraliserad koordinator som kopplar samman deltagare och hjälper dem att kommunicera och bygga en riktig CoinJoin-transaktion. Denna centraliserade samordnare har aldrig förvaring av användarnas medel, men får omfattande insikt i de transaktioner de koordinerar, kan censurera inkommande indata (som i fallet med Wasabi Wallet) och kan pressas att samla in eller dela information om CoinJoin-deltagare.[X2068X ] 
  * Användare med stora mängder pengar till CoinJoin kan ofta behöva vänta timmar (eller till och med dagar!) för att hitta tillräckligt många deltagare att CoinJoin med, vilket leder till stora förseningar från det att en användare får pengar tills de kan spendera dem privat. 
  * Sekretessen som tillhandahålls av en CoinJoin-transaktion försämras med tiden när andra deltagare spenderar pengar eller länkar sina resultat till sin identitet genom KYC-utbyten, ID-krävande handlare, etc. Detta innebär att användare helst håller sina pengar ständigt samlade i CoinJoin-transaktioner för att behålla deras anonymitetsuppsättning ("publik att gömma sig i") så fräsch som möjligt.
  * I de flesta tillvägagångssätt för CoinJoin måste deltagarna använda en fast storlek UTXO (dvs. 0,1 BTC) för att göra det svårare att ansluta in- och utgångar för CoinJoin-transaktioner. Detta leder till högre avgifter (fler separata transaktioner krävs per stor insats), mer "giftig förändring" (medel som inte går att använda utan allvarliga risker för integriteten), och kan hindra mindre användare från att överhuvudtaget kunna blanda om de inte har det minsta saldo som krävs.

## Hur löser ringsignaturer dessa problem?

Som [vi har tittat djupt på vad ringsignaturer är tidigare](/knowledge/ring-signatures), kommer jag inte att gå in i detalj på de tekniska aspekterna av hur de fungerar i det här blogginlägget. Istället ska vi titta på hur tillvägagångssätten i Monero löser problemen med CoinJoin diskuterar ovan.

> CoinJoin är opt-in och kräver deltagande

Moneros ringsignaturer är en kärnfunktion i sekretessprotokollet, och _varje_ transaktion på nätverket använder dem. Detta innebär att ingen användares transaktioner sticker ut för att söka större integritet än "normala" Monero-användare, och alla användare får rimligt förnekande att de har spenderat pengar i en given transaktion. Eftersom en användare som spenderar pengar inte samordnar eller deltar med lockbetsingångarna i en transaktion, kan de användare som äger indata som råkar vara utvalda som lockbete ärligt säga att de inte deltog i den transaktionen, vilket stärker deras integritet.

> Användning av en centraliserad koordinator

Eftersom Moneros ringsignaturer är helt okoordinerade och endast kräver den verkliga spenderaren av pengar för att skapa transaktionen, finns det inget behov av en centraliserad koordinator i Monero. Detta säkerställer att _ingen_ kan neka dig tillgång till integritet i Monero, och det finns ingen centraliserad enhet som kan utsättas för press, inga lätta Sybil-attacker på likviditet, etc. Så länge din transaktion betalar de rätta avgifterna, du får ocensurerbar tillgång till integritet, säkerhet och anonymitet i Monero.

> CoinJoin kräver likviditet

Den "likviditet" som är tillgänglig för alla som spenderar Monero att använda som lockbete är alltid den totala uppsättningen av utgångar på kedjan så det finns aldrig brist på lockbeten att gömma sig i med Monero. Någon som vill spendera Monero kan göra det ~20 minuter efter att ha mottagit pengar och behöver inte utföra några ytterligare steg för att få stark sekretess i Monero.

> CoinJoin integritet försämras med tiden

Eftersom Moneros utgångar aldrig är kända förbrukade av nätverket, är integriteten som tillhandahålls av ringsignaturer mycket mindre mottaglig för försämring över tid. En användare behöver inte ständigt churna utdata i Monero, och utanför extremt sällsynta omständigheter förlorar han ingen integritet allt eftersom tiden går.

Om en användare vill "uppdatera" de lockbeten som används med en utdata, kan de bara skicka tillbaka pengarna till sig själva och kunna spendera dem ~20 minuter senare som vanligt.

> CoinJoin kräver vanligtvis ingångar med fast storlek

Eftersom belopp är dolda i varje transaktion med ["Konfidentiella transaktioner"](/knowledge/monero-ringct) (en del av "RingCT"), kan lockbetena som används i en given transaktion vara av vilken storlek som helst. Det finns ingen anledning att behöva vara orolig för beloppsbaserad heuristik i Monero, så transaktioner är mycket enklare att bygga och kan utnyttja lockbeten från vilken tidpunkt som helst och oavsett belopp på Monero blockchain.

## Hur kan jag lära mig mer?

Om du är nyfiken och vill bättre förstå ringsignaturer eller CoinJoin-transaktioner, se länkarna nedan för bra ställen att komma igång:

  * [Hur ringsignaturer obskyr Moneros utgångar](/knowledge/ring-signatures)
  * [Ringsignatur – Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [CoinJoin-översikt](https://6102bitcoin.com/coinjoin-overview/)

Vidare läsning