---
title: "Hur Monero löste problemet med blockstorlek som plågar Bitcoin"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Obs:** Det rekommenderas starkt att läsaren har läst våra artiklar ["Why Monero Has A Tail Emission"](/knowledge/monero-tail-emission) och ["Monero Mining: What Makes RandomX så speciell”](/knowledge/monero-mining-randomx). Den här artikeln bygger på de koncept som presenteras där._

När individer diskuterar problemen med blockchain kommer ett av de första orden att dyka upp vara "skalning". Det är ingen hemlighet att blockkedjor inte skalar bra, men de flesta vet inte varför.

Sanningen är att skalning faktiskt är ett paraplybegrepp som täcker två olika kategorier: Protokollstöd och tekniskt stöd vid en given tidpunkt. I den här artikeln kommer vi att fokusera vår uppmärksamhet på en, Protokollstöd är i grunden ett mått på hur många transaktioner protokollet kan hantera vid en given tidpunkt.

Bitcoin har en blockstorleksgräns, vilket innebär att när tillräckligt många transaktioner är inkluderade i ett block, måste alla ytterligare transaktioner vänta i kö till nästa block. En användbar analogi skulle vara att tänka på ett tåg. Ett tåg stannar till stationen och de som står i kö fyller sig in. När tåget är fullt måste alla som lämnas utanför vänta på nästa.

Bitcoin använder avgifter för att avgöra vem som kommer in i blocket eller inte. Om man hoppar tillbaka till tågliknelsen kan man föreställa sig att en potentiell passagerare, som är på väg att bli kvar, erbjuder tågingenjören fem dollar för att ge honom en plats. Andra passagerare följer efter, och så småningom blir det ett budkrig för att se vem som får vilka platser. Det är upp till föraren att bestämma om han vill respektera först till kvarn-principen, men det ligger i hans bästa ekonomiska intresse att maximera sin inkomst genom att ta de högstbjudande ombord.

I denna analogi är gruvarbetare lokförarna. De kan inkludera vilka transaktioner de vill i blocket, men de kommer i allmänhet att välja de som har högst betalda avgifter.

Alternativt, om blocken inte är särskilt fulla, har folk inga incitament att betala höga avgifter eftersom det finns gott om lediga platser att övergå.

I höjden av kryptovalutaboomen 2017 svämmades Bitcoin över av transaktioner, och avgifterna skjuter i höjden för dem som ville inkluderas i nästa block, eller vilket block som helst i en nära framtid för den delen. De som inte var villiga att betala höga avgifter såg att deras transaktioner trycktes tillbaka i timmar, dagar eller till och med hoppade ur kön helt och hållet.

Detta var en skrämmande insikt om hur Bitcoin skulle klara sig om den ofta omtalade "massadoptionen" skulle inträffa. Om Bitcoin skulle användas av massorna skulle det bli ännu värre än 2017, och Bitcoin skulle vara otillgängligt för alla andra än de rika, helt enkelt för att genomströmningen är liten på grund av en fast blockstorlek, vilket gör att avgiftsmarknaden tar över .

Monero förutsåg detta och ville göra något annorlunda. Så Monero-utvecklarna implementerade en dynamisk blockstorlek.

I grund och botten har Monero också en keps i blockstorlek, men det är en mjuk keps. När raden av väntande transaktioner blir för lång kan gruvarbetarna öka storleken på blocken. Med vår tåganalogi kan du tänka dig att lägga till fler tågvagnar för att passa de extra passagerarna. När kön är tom krymper blocken tillbaka till sin ursprungliga storlek framöver.

Om detta verkar vara en bra idé verkar det rimligt att fråga varför Monero är den enda kryptovalutan som har implementerat detta. Varför inte lägga till det på Bitcoin för att sätta stopp för genomströmningsproblemen?

Det här är tyvärr inte möjligt. Det finns flera anledningar till varför, och vi ska göra vårt bästa för att förklara.

Det är alltid i en gruvarbetares intresse att ha stora block. Med stora block kan de få plats med fler transaktioner och tjäna mer pengar på avgifterna, såväl som blockbelöningarna. Detta har potential att leda till spamattacker, där någon skickar många små transaktioner, med små avgifter, för att blåsa upp kedjan. Miner's skulle bara höja blockstorleken inkludera dem alla eftersom pengar är pengar, oavsett hur små de är. Detta skulle leda till genomgående stora block med liten ekonomisk nytta. Bitcoin löser detta genom att på konstgjord väg begränsa blockstorleken och därigenom generera en avgiftsmarknad. Skräppostangripare skulle behöva betala ut de andra användarna i avgifter, och det är inte längre billigt. Men detta innebär att blocken blir fulla och lämnar vissa transaktioner som väntar som nämnts ovan.

Så hur kan Monero ha dynamiska blockstorlekar men undvika skräppostattacker? Svaret är enkelt, men smart. En straffavgift på blockbelöningen införs när ett block är större än normalt. Om en gruvarbetare vill öka blockstorleken kommer belöningen de får för att hitta det blocket att vara mindre än de annars skulle få. Så de kommer bara att öka blockstorleken när de betalda transaktionsavgifterna för användarna uppväger den förlorade delen av blockbelöningen. Till exempel, om gruvarbetaren skulle förlora 0,5 XMR genom att höja blockstorleken, och summan av de betalda transaktionsavgifterna skulle vara 0,4 XMR, så skulle det bli en nettoförlust på 0,1 XMR om de skulle höja storleken, så att de skulle gör det inte. Omvänt, om de totala transaktionsavgifterna adderades till 0,7 XMR, skulle det finnas en nettovinst på 0,2 XMR, även om de förlorar 0,5 XMR från blockbelöningsstraffet, så gruvarbetaren kommer att öka storleken.

Dessa dynamiska block gör att nätverket kan växa organiskt, utan att begränsa blockstorleken för att skapa en påtvingad avgiftsmarknad, samtidigt som man undviker spamattacker. Det finns flera fler vinklar vi kan se den här idén från, och fler anledningar till varför det inte skulle vara möjligt att lägga till Bitcoin, men för tillfället hoppas vi att läsaren har en förståelse för hur Monero kringgår flera av problemen i Bitcoin och dess derivat, och hur den planerar att skala sin genomströmning in i framtiden.

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

  * [Monero Utgångar Förklaras](/knowledge/monero-outputs)/

  * [Monero bästa praxis för nybörjare](/knowledge/monero-best-practices)/

  * [Hur ringsignaturer obskyr Moneros utgångar](/knowledge/ring-signatures)/

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