---
title: "Hur RingCT döljer Monero-transaktionsbelopp"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Moneros integritet är inte beroende av en enda mekanism som, om den bryts, skulle avslöja alla transaktioner, utan snarare av tre olika tekniker som fungerar tillsammans för att ge en holistisk integritet samtidigt som de kompenserar för svagheterna i de andra delarna. Denna tredelade strategi består av [ringsignaturer](/knowledge/ring-signatures), RingCT och [stealth-adresser](/knowledge/monero-stealth-addresses). Dessa tre teknologier döljer den verkliga utsignalen (avsändaren), mängden respektive mottagaren. Idag ska vi prata om RingCT.

RingCT är utan tvekan den mest tekniska av de tre och kan vara svår att förstå, så vi kommer inte att gå igenom exakt hur den fungerar, utan snarare visa hur det är möjligt att inte veta ett belopp och ändå bekräfta saker om det. Och oroa dig inte, vi kommer att använda massor av exempel som alltid.

Först, låt oss undersöka varför det är viktigt att verifiera någonting om beloppen. Varför kan vi inte bara hålla dem helt hemliga? Svaret är att det finns smarta sätt för människor att skapa pengar ur tomma intet om de får möjlighet. Hur kan något sådant fungera? Låt oss titta på ett exempel.

Om du vill köpa ett föremål av din vän och han vill ha tio dollar för det, då börjar du med tio dollar och han börjar med noll. När du har gett honom tio dollar har han tio dollar och du har noll. Du började med tio och nu har han tio. Inga pengar skapades eller förstördes i denna transaktion.

Med kryptovalutor kan en smart person ge tio dollar för varan och istället för att få noll dollar i växel kan de få två dollar tillbaka. Istället för att 0 och 10 leder till 10 och 0 (eller 10=10), är det nu 0 och 10 som leder till 10 och 2 (eller 10=12). Två Monero skapades helt enkelt ur tomma intet. Man kan föreställa sig att om individen skulle göra detta mot sig själv flera gånger, skulle de kunna samla en gigantisk förmögenhet på kort tid.

Med Bitcoin och andra skulle detta vara lätt att se. Du tittar på ingångarna som går in i en transaktion och utgångarna som kommer ut och ser till att det som skickas är lika med det som tas emot. Om dessa belopp är krypterade och inte synliga har en användare inget sätt att verifiera att det som skickas och det som tas emot är detsamma.

I ett försök att öka Bitcoins integritet skapade Gregory Maxwell Confidential Transactions (CT), en ny teknik som skulle möjliggöra krypterade belopp och samtidigt bevisa att ingenting skapades eller förstördes i processen. Som med de flesta integritetstekniker kom den inte med i Bitcoin, men Monero var angelägna om att anta den. Det fanns bara ett problem. Den redan implementerade tekniken med ringsignaturer var inte kompatibel med den föreslagna idén. Så en av MRL-forskarna vid den tiden, Shen Noether, modifierade CT till RingCT, en version av CT som var kompatibel med ringsignaturer.

En gång till, hur detta fungerar är ganska tekniskt, och skulle vara svårt att förklara i en inledande artikel. För den kryptografientusiast som bara måste veta finns det gott om djupgående artiklar skrivna på internet om CT:s inre arbete. För oss andra kommer den här artikeln att visa hur det kan vara möjligt att dölja beloppen, men ändå bevisa att ingenting har skapats eller förstörts.

Låt oss säga att Alice ville skicka pengar till Bob. Alice kommer att skicka 10 XMR till Bob, som kommer att få 10 XMR. 10=10 så inget är fel här. Men Alice vill inte att någon ska veta hur mycket hon skickar. Så hon och Bob skapar en gemensam hemlighet. I princip en siffra som bara de två känner till. Låt oss säga att talet är 22. Nu multiplicerar Alice 10 (vad hon verkligen skickar) med 22 för att få 220. Det här är talet hon delar med nätverket.

Gruvarbetarna själva känner inte till det hemliga numret. Om de gjorde det kunde de dela talet de visas med det hemliga numret och få det verkliga beloppet skickat. Men eftersom de inte gör det kan de inte. De ser dock att Bob kommer att få 220. 220 skickade. 220 mottagna. 220 = 220. På detta sätt kan nätverket verifiera att ingen Monero skapades eller förstördes, allt utan att veta det verkliga beloppet som Alice skickade Bob.

Eftersom Bob känner till det delade hemliga numret, när han tar emot pengarna, dividerar han bara med 22 för att få det verkliga beloppet som Alice skickade, 10. Alice och Bob vet båda hur mycket som skickades och hur mycket som togs emot, hela tiden alla andra får ett falskt nummer.

Återigen, detta är inte det faktiska sättet som CT fungerar på, men det ger en uppfattning om hur något sådant här kan vara möjligt. Det verkliga sättet involverar saker som Pedersen-åtaganden, två skickade belopp (ett krypterat belopp till mottagaren och ett åtagandebelopp till nätverket), och...ja, det är redan lätt att se hur man kan gå vilse i allt det där.

En sak att notera är dock att även om RingCT döljer det belopp som överförts mellan två parter i en transaktion, döljer det inte två andra uppsättningar siffror.

Den första är coinbase-transaktionerna. Om denna term är obekant för dig betyder det i princip den belöning som gruvarbetare får för att hitta nästa block. Detta nummer är inte dolt. Vem som helst kan se hur mycket protokollet har tilldelat en gruvarbetare för deras tjänst. På detta sätt kan den aktuella mängden Monero som finns vara känd genom att lägga till alla coinbase-transaktioner. Deras summa kommer att motsvara den nuvarande Monero i omlopp.

Den andra siffran som inte är dold är den avgift som betalas till miners när en användare skickar en transaktion. Avgifterna måste vara tydliga så att miners kan veta vem de ska prioritera. Detta är dock ett sätt som användare kan skada sin integritet, eftersom om någon använder en unik mineravgift varje gång de skickar en transaktion (som 0,12345), kan deras transaktioner länkas.

Utöver dessa fall har RingCT dolt Monero-belopp sedan 2017, och vår kollektiva integritet är desto starkare för det.

Vidare läsning