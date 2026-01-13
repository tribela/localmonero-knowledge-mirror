---
title: "Hur Monero Stealth-adresser skyddar din identitet"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero har implementerat en tredelad strategi för integritet. Dessa teknologier är [ringsignaturer](/knowledge/ring-signatures), som döljer den sanna utdata (avsändaren), RingCT som döljer beloppen och smygadresser, som döljer mottagaren. Idag kommer vi att diskutera den sista av dessa nämnda tekniker: smyg adresser.

Det finns många anledningar till varför en individ kanske vill dölja vem de skickar till. Vi får aldrig låta någon försöka övertyga oss om att alla exempel på detta är osmakliga beteenden. Saker som att skicka till ett impopulärt politiskt parti, donera till välgörenhetsorganisationer eller stödja de som kulturen anser vara "inställda" är alla exempel på där man kanske vill dölja sina utgiftsbeteenden av rädsla för återverkningar, men är helt legitima till sin natur.

På en transparent blockkedja är adresserna dit man skickar sina transaktioner synliga för alla. Det är viktigt att tänka på att om gruvarbetare själva inte håller med om vart pengarna tar vägen, kan de välja att inte bryta dem i ett block, vilket effektivt censurerar denna transaktion på en till synes censurresistent plattform. Det enda sättet att göra denna, visserligen osannolika, censur inte möjlig är om gruvarbetare inte kan skilja mellan transaktioner eftersom all metadata i kedjan är skymd på olika sätt. Något som Monero är känt för.

Monero löser detta problem med transparenta adresser genom att implementera stealth-adresser, en teknik som faktiskt ursprungligen gjordes för Bitcoin 2011 av Bitcoin Talk-forumanvändaren ByteCoin (relationen till Bytecoin, som senare skulle integrera stealth-adresser, är okänd). Den nuvarande formen av stealth-adresser har dock flera förbättringar jämfört med den ursprungliga idén. Men först, för att se hur de fungerar, låt oss prata om nycklar.

Det är svårt att vara i kryptovalutan och inte höra talas om nycklar. Fraser som "säkerhetskopiera din privata nyckel" är vanliga, men när en vanlig Joe hör orden "offentlig nyckel" och "privat nyckel" blir de rädda och tror att det blir för tekniskt och förvirrande att förstå. Men oroa dig inte. Vi tar det långsamt och använder många exempel.

De två typerna av nycklar som används i kryptovalutor är, som nyss nämnts, offentliga och privata. Dessa två nycklar kommer vanligtvis i ett par, vilket innebär att en viss offentlig och privat nyckel är länkade till varandra. Faktum är att vanligtvis den publika nyckeln härleds från den privata, vilket innebär att om du känner till den privata nyckeln kan din plånbok göra lite fiffig matematik och hitta rätt offentlig nyckel varje gång.

Nu, som namnen antyder, kan den publika nyckeln vara offentlig utan konsekvenser. Vanligtvis är det en del av adressen som du delar för att få pengar till din kryptovaluta-plånbok. Också efter sin namne är den privata nyckeln en som inte bör delas. Det är det som gör att du kan skriva under och spendera en transaktion, så om den blir stulen eller delad kan den elak tredje parten spendera dina pengar, vanligtvis till sig själva.

En enkel analogi till detta skulle vara ett hänglås och nyckeln som behövs för att låsa upp det. Det öppna hänglåset kan delas fritt, och verkligen vad som helst kan låsas med detta hänglås, men bara personen med nyckeln kan öppna allt som hänglåset är stängt på. Hänglåset kan kopieras och delas, nyckeln ska inte vara det.

Dessa nycklar är vanligtvis borttagna från användaren, så du ser dem aldrig riktigt. I Monero visas de inte alls som en skrämmande alfanumerisk sträng. I Monero känner den vanliga användaren till den privata nyckeln som sitt frö. Fröet (som du bör skriva ner om du inte har gjort det), är faktiskt bara en mänsklig läsbar privat nyckel. 

Ser du? Inte så läskigt trots allt. Tillbaka till smyg adresser.

Som nämnts tidigare gjordes inte stealth-adresser ursprungligen för Monero, utan för Bitcoin. Men som med de flesta nystartade idéer hade denna första iteration problem. Nästa försök kom när CryptoNote skapades av Nicholas van Saberhagan för Bytecoin, föregångaren till Monero ([se vår historia av Monero och Bytecoin här](/knowledge/monero-history)), och även om det var en klar förbättring jämfört med originalet, hade det till och med några subtila brister.

Så småningom kom en sista iteration till från en utvecklare för en annan numera nedlagd, integritetskrypteringsvaluta, som fixade de utestående sekretess- och säkerhetsproblemen med idén. Detta tog så småningom vägen in i Monero, och är vad som används idag.

Även om dessa integritets- och säkerhetsproblem löstes, tillförde stealth-adresser i sig en annan typ av egenhet till blockchain-teknik, en som inte existerade tidigare. Behovet av att skanna. Eftersom mottagningsadresser inte visas offentligt i blockkedjan, vet mottagaren aldrig om någon given transaktion är deras, så de måste skanna alla inkommande transaktioner med sin privata nyckel för att se om det är deras.

Med transparensmynt behöver de bara kontrollera om en transaktion skickas till din adress. En lätt ja eller nej fråga. Men med smygadresser kan varje transaktion potentiellt vara en som skickas till dig, så du måste försöka låsa upp var och en med din privata nyckel för att se om den öppnas.

Detta är ett extra steg som Bitcoin och dess derivat inte har, och gör initiala plånboksinställningar, tillsammans med synkronisering av en plånbok när du inte har öppnat den på ett tag, mycket längre än Bitcoin. Avvägningen är dock nödvändig för att låsa upp de integritetsgarantier den har. Det bör noteras att, till skillnad från den svagaste punkten i sekretesstrifecta, är ringsignaturer, stealth-adresser inte mottagliga för heuristik. Den förlitar sig på beprövad och sann elliptisk kurvkryptografi, som hela internet förlitar sig på, så att bryta den skulle innebära ett slut på datorsäkerheten i allmänhet, inte bara Monero.

Vidare läsning