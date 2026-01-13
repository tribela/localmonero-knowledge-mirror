---
title: "Monero Utgångar Förklaras"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero, liksom andra kryptovalutor, använder utdata som ett sätt att redovisa pengar. Många kryptokunniga användare har säkert hört den här termen förut, men alla förstår inte vad de menar och hur de fungerar. Som utforskats i vår [ringsignaturartikel](/knowledge/ring-signatures), är utdata den faktiska enhet som utbyts på blockkedjan mellan transaktionsparter. Liknar en dollarsedel, men beloppet är inte i en fast valör.

Om du får 16 dollar för ett jobb kan du få en endollarsedel, en femdollarsedel och en tiodollarsedel. Du har 16 dollar, men du har också tre olika sedlar i din plånbok. Om du vill betala någon 6 dollar kan du använda 5 och 1-sedeln, men om du vill betala någon 8 dollar kan du bara använda 10 dollar och få tillbaka 2 dollar i växel. Slutligen, om du vill betala någon 14 dollar måste du använda alla tre sedlarna och får tillbaka 2 dollar i växel, men för ett ögonblick, när du lämnar över alla tre sedlarna, har du inga pengar i plånboken förrän du får tillbaka växeln.

Monero fungerar på liknande sätt. Antag att du driver en butik och gör tre försäljningar på tre olika artiklar. Du kanske får 1,5 XMR, 2,25 XMR och 5,25 XMR för totalt 9 XMR, men du har också tre olika utgångar i din plånbok av de valörer som nämnts tidigare. Precis som med dollar kanske du vill betala någon 3 XMR. Du kan använda bara 5,25 XMR och få tillbaka 2,25 XMR i växel, eller så kan du kombinera 1,5 och 2,25 XMR och få tillbaka 0,75 XMR i växel.

Men så snart du skickar transaktionen försätts de utgångar som du använder i ett "låst" tillstånd, vilket innebär att de är oåtkomliga tills du får tillbaka växelpengarna. Protokollet låser upp medlen (dvs. ger dig tillbaka växelpengarna) efter 10 bekräftelser, eller cirka 20 minuter. Precis som när du lämnar över dollarsedlarna ur din plånbok kan du inte använda pengarna igen förrän du får tillbaka växeln från kassören, din Monero är oåtkomlig tills du får tillbaka växeln..

Låt oss gå tillbaka till exemplet med att skicka 3 XMR till någon, och du använder de 5,25 XMR som kommer ut. Nu, medan du väntar på att få tillbaka 1,75 XMR i växel, kan du inte använda den. Dessa 1,75 XMR är oåtkomliga för dig. Men du kan fortfarande använda 1,5 XMR och 2,25 XMR, eftersom dessa inte har spenderats. Om vi återgår till dollarexemplet och du betalar någon 8 USD, som i exemplet ovan, kan du inte använda de 2 USD som du förväntar dig i växel förrän du får tillbaka dem, men i det här exemplet har du fortfarande en oanvänd 10-dollarsedel i plånboken. Detta kan fortfarande användas för att köpa vad du vill medan du väntar på förändringen. Samma sak med Monero.

Detta är ofta en förvirringspunkt för nya Monero-användare. Ofta kan en användare bara ha en output i sin plånbok, mottagen från en börs eller en vän. Låt oss säga att denna output är 20 XMR. De har inga andra utgångar i sin plånbok. De vill nu göra en donation till två av sina favoritvälgörenhetsorganisationer. De skickar 5 XMR till den första välgörenhetsorganisationen och blir sedan förvirrade eftersom de, trots att de borde ha 15 XMR kvar, inte omedelbart kan skicka nästa donation till den andra välgörenhetsorganisationen. Som du kanske har gissat beror detta på att de 15 XMR är låsta. De kan inte spenderas förrän de returneras som växel (10 bekräftelser eller cirka 20 minuter). När deras pengar har låsts upp kan de skicka sin andra donation.

Bara för att upprepa poängen, de skulle inte ha haft detta problem om de hade haft flera utgångar istället, till exempel två 10 XMR-utgångar eller liknande. De skulle kunna skicka båda donationerna direkt efter varandra, eftersom den första donationen skulle använda en av 10 XMR-utgångarna (och vänta 10 bekräftelser för att få 5 XMR tillbaka i växel), och den andra donationen skulle använda den andra 10 XMR utgången.

Vissa kryptovalutaplånböcker har en funktion som kallas "output management", som helt enkelt visar användaren vilka outputs de har för närvarande (utöver deras totala summa), samt låter dem välja vilka de vill använda när de spenderar sin kryptovaluta.

Från och med nu gör Moneros GUI automatiskt val av utdata för användare, eftersom användare som väljer sina egna utdata ofta leder till förvirring eller, i vissa fall, skadad integritet. Det finns dock plånböcker under konstruktion, såsom det nya Feather-plånboksprojektet, som kommer att innehålla dessa funktioner för utmatningshantering.

Vi har pratat en hel del om sändningsdelen, men något fascinerande händer i mottagaränden. Om vi återgår till vårt exempel med att skicka 3 XMR till någon och använda dina 1,5 XMR och 2,25 XMR-utgångar i transaktionen (medan du förväntar dig 0,75 XMR i växel), får mottagaren INTE två utgångar på 1,5 XMR och 2,25 XMR. De får istället EN 3 XMR-utgång.

I bakgrunden kombinerar protokollet alla utgångar som använts för utgifterna och ger mottagaren en utgång av det betalda beloppet och skickar en växelutgång tillbaka till avsändaren. Avsändaren får alltså också tillbaka en output som växel, oavsett om han eller hon använde två, tre eller tio outputs för att skicka transaktionen.

Vi hoppas att detta har skingrat en del förvirring kring outputs och hur protokollets interna redovisning fungerar, samt det vanliga användarproblemet med förvirring när man stöter på låsta medel. I en annan artikel kommer vi att undersöka hur du hanterar dina utdata så att du minimerar risken för att behöva vänta på upplåsta medel innan du skickar framtida transaktioner.

Vidare läsning

  * [Hur Monero unikt möjliggör cirkulära ekonomier](/knowledge/monero-circular-economies)/

  * [Moneros ringsignaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Varför (och hur!) du ska hålla i dina egna nycklar](/knowledge/hold-your-keys)/

  * [Bidrar tillbaka till Monero](/knowledge/contributing-to-monero)/

  * [Hur fjärrnoder påverkar Moneros integritet](/knowledge/remote-nodes-privacy)/

  * [Hur Monero använder hard-forks för att uppgradera nätverket](/knowledge/network-upgrades)/

  * [Visa taggar: Hur en byte kommer att minska Monero plånbokssynkroniseringstider med 40% +](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool och dess roll i decentraliseringen av Monero Mining](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Vad det kommer att göra för Monero](/knowledge/seraphis-for-monero)/

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