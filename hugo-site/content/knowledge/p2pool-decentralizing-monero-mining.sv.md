---
title: "P2Pool och dess roll i decentraliseringen av Monero Mining"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Ett av kärnmålen i Monero-projektet är att möjliggöra ett rättvist, decentraliserat och säkert nätverk genom nya och innovativa metoder för proof-of-work (PoW) mining, det huvudsakliga sättet att säkra kryptovalutanätverk idag.[ X230X] 

Medan en unik gruvalgoritm [som RandomX](/knowledge/monero-mining-randomx) är extremt viktig för detta mål eftersom den hjälper till att säkerställa att alla som har en dator kan bidra med en hel del till säkerheten i nätverket, men RandomX löser inte problemen som kan uppstå på grund av poolbrytning. Poolutvinning är det i särklass vanligaste sättet att bryta kryptovalutor idag, inklusive Monero, men tack och lov förändrar uppkomsten av p2pool-mining det snabbt.

## Vad är pool mining?

Pool mining är ett sätt för gruvarbetare att dela på uppgiften att försöka lösa ett block på nätverket och sedan dela belöningarna jämnt för alla block som poolen hittar. Även om detta hjälper enormt att jämna ut frekvensen med vilken gruvarbetare får betalt jämfört med att bryta Monero enbart, är det inte utan allvarliga centraliseringsproblem.

När varje gruvarbetare bidrar med arbete till poolen, ger de upp kontrollen över allt arbete de gör och blockeringar som de hittar till själva poolen, och litar på att poolen ärligt och rättvist kommer att dela belöningarna mellan alla gruvarbetare baserat på mängden arbete var och en har gjort. Om allt går bra samlar pooloperatören in arbetet från alla gruvarbetare, skickar det till nätverket och delar lika på belöningarna.

## Vad är problemet med pool mining?

Tyvärr är detta helt beroende av förtroende och gör det möjligt för pooloperatören att göra otrevliga saker med det arbete som utförs av gruvarbetare. Pooloperatören kan använda det arbete som görs för att attackera nätverket, försöka dubbla pengar (om poolen är tillräckligt stor), eller helt enkelt använda det arbete som utförs av gruvarbetarna för att betala sig själva och aldrig belöna gruvarbetare ordentligt för deras arbete .

Den största risken för nätverket är att en pool (eller flera pooler arbetar tillsammans) som har mer än 51 % av nätverkens hashrate under sin kontroll, eftersom de skulle kunna använda detta för att fuska och spendera pengar två gånger (en dubbelutgift) attack) eller försök att ändra reglerna för nätverket.

## Vad är p2pool?

p2pool är ett koncept som ursprungligen skapades för att bryta Bitcoin redan 2011, men som aldrig har använts i stor utsträckning och som förblir praktiskt taget oanvänt på Bitcoin. Tack och lov tillbringade en av nyckelutvecklarna bakom RandomX, SChernykh, sin semester med att hitta lösningar på några av problemen med Bitcoin-implementeringen av p2pool och att skriva om all programvara från grunden.

p2pool i Monero möjliggör ett helt tillitslöst sätt för gruvarbetare att arbeta tillsammans för att lösa blockeringar och säkra Monero-nätverket genom att använda speciell nodmjukvara för p2pool för att dela arbetet.

Detta görs med hjälp av en ny blockkedja (en "sidokedja") som håller ett register över det arbete varje gruvarbetare utför, deras plånboksadress och hur mycket Monero de har tjänat, och sedan betalar ut belöningen i ett förtroende -mindre och decentraliserat sätt. Eftersom den här sidokedjan har mycket färre gruvarbetare är det mycket lättare att hitta och skicka in block på den än på det huvudsakliga Monero-nätverket, vilket gör det lättare för gruvarbetare att få konsekventa utbetalningar jämfört med att bara bryta Monero.

## Hur löser p2pool problemen med pool mining?

I p2pool finns det ingen centraliserad pool, centraliserad pooloperatör eller enskild person som håller i pengar och delar ut utbetalningar. Allt arbete som gemensamt utförs av de som gruvdrift via p2pool kontrolleras av p2pool blockchain och andra nodoperatörer för att säkerställa att det är legitimt, och alla gruvarbetare betalas ut enligt det arbete de har gjort omedelbart när ett block hittas direkt från belöningarna i det hittade blocket.

När gruvarbetare väljer att använda p2pool istället för en centraliserad pool tar de bort all makt och förtroende från pooloperatörer och ser till att deras arbete bidrar till nätverkets bästa och till deras egna belöningar, minskar risken för nätverksattacker, missbruk av deras arbete, eller stöld av belöningar som de är skyldiga.

Det här hjälper dem inte bara att skydda sina egna intressen, det minskar risken att centraliserade pooler kan utgöra för Monero-nätverket som helhet. p2pool-användning hjälper också oerhört mycket till att minska risken som nationalstater eller tillsynsmyndigheter kan utgöra för nätverkets hälsa, eftersom det inte finns några centraliserade pooloperatörer att trycka på, ingen geografisk koncentration av pooler att luta sig mot eller någon annan lätt tryckpunkt för dem att använda mot Monero.

## Vilka är nackdelarna?

Tack och lov har p2pool i Monero varit väldesignad och välbyggd och fungerar extremt bra! Den största nackdelen med p2pool-mining är dock att varje gruvarbetare som vill använda p2pool måste köra sin egen Monero-nod, vilket gör att processen att komma igång blir lite mer involverad. Men denna nod används sedan för att beräkna all information som behövs för att bygga och kontrollera block, och säkerställer att gruvarbetaren har fullständig kontroll över sitt arbete som utförs. Noden kan också fungera som en fjärrnod för gruvarbetarnas egen plånbok, bidrar till nätverket och mycket mer.

Den andra viktiga skillnaden från centraliserad gruvdrift är att små gruvarbetare som använder p2pool kommer att ha lite mer "varians", eller tid mellan utbetalningar, än en stor centraliserad pool – men det's _extremt_ viktigt att notera att detta inte kommer att leda till att man tjänar mindre Monero över tid! p2pool kommer att vara lika lönsamt för även små gruvarbetare över tid som centraliserade pooler. En del av denna avvikelse kompenseras också av att p2pool har 0 % avgifter, eftersom det inte finns någon centraliserad pooloperatör som kan betala för deras tjänster!

## Hur kommer jag igång?

Tack och lov, tack vare den utmärkta designen av Monero's p2pool-implementering och de många människor i samhället som har lagt ner tid för att hjälpa till att förenkla processen för gruvdrift via p2pool, blir det enklare med tiden att komma igång. Det finns flera sätt att komma igång med mining med p2pool, men eftersom de tekniska detaljerna ligger utanför ramen för denna artikel, hoppa gärna in på en länk nedan beroende på ditt operativsystem:

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## Hur kan jag lära mig mer?

Om detta har väckt din nyfikenhet kring p2pool-brytning, ta en titt nedan för ytterligare länkar och förklarare om p2pool, hur det fungerar och vad det betyder för Monero:

  * [Den officiella Github för p2pool](https://github.com/SChernykh/p2pool)
  * [De officiella dokumenten om att använda p2pool](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool är nu live](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, en sorts "blockutforskare" för p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh: Om hans utveckling av P2Pool en decentraliserad XMR-gruvpool](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

Vidare läsning