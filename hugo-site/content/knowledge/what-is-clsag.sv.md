---
title: "Hur CLSAG kommer att förbättra Moneros effektivitet"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Som protokoll befinner sig Monero för närvarande i ett konstant tillstånd av innovation. Genom att använda forskning inom både on-chain- och off-chain-lösningar letar Monero-gemenskapen efter områden att förbättra för att göra Monero mer privat, mer skalbar och mer tillgänglig för alla. En av de senaste innovationerna är ersättningen av det länkbara ringsignaturschemat MLSAG med en drop-in-ersättning CLSAG, som står för Concise Linkable Spontaneous Anonymous Group.

På ytnivå kommer implementeringen av CLSAG att minska de vanligaste 2 input, 2 output-transaktionerna med 25%. Vi kommer också att se en minskning av verifieringstiden med 10 %.

Men vad är egentligen CLSAG? Vad gör den och hur skiljer den sig från den gamla versionen, MLSAG? Låt oss ta en minut och påminna oss själva om varför och hur ringsignaturer fungerar så att vi bättre kan förstå detta koncept. Ringsignaturer möjliggör icke-interaktiva ingångar som inte kan särskiljas av vittnen med hjälp av anonymitetsuppsättningar från tidigare utgångar som valts av undertecknaren. Enkelt uttryckt innebär det att en användare kan dölja sina utdata som används i en transaktion tillsammans med orelaterade utdata, och de kan göra allt detta utan att någon annan behöver delta. Allt du behöver är en kopia av blockchain. Var och en av dessa utgångar verkar oftast vara lika sannolik att vara den faktiska som skickas, och döljer därmed metadata om avsändaren.

Detta medför dock ett litet problem. Vad händer om en användare konstruerar en ringsignatur med alla falska utgångar? Hur skulle någon kunna veta att den okände avsändaren inte har rätt att skicka någon av dem? Skulle den här användaren kunna spendera falska pengar? Svaret är nej. Ringsignaturen innehåller en metod för att bevisa att minst en av utgångarna ägs av den okände avsändaren, utan att avslöja vilken det är. Faktum är att både CLSAG och MLSAG (hädanefter kända som SAG) är den del av ringsignaturen som bevisar detta. Intressant nog bevisar den samtidigt att transaktionsbeloppet, även om det är dolt bakom konfidentiella transaktioner (RingCT), balanserar. Att SAGs bevisar två saker, att en utgång ägs av någon i ringen, och att transaktionen balanserar, är viktigt och faktiskt där besparingarna i storlek och verifiering ligger. Om det här börjar bli förvirrande, oroa dig inte, vi kommer snart till en rolig och lättförståelig analogi.

Det gamla signaturschemat MLSAG (Multilayered Linkable Spontaneous Anonymous Group) bevisar de två ovannämnda sakerna i en ringsignatur, men det gör varje sak separat. Användningen av separata beräkningar för signerings- och åtagandenycklar innebär långsammare operationer. En modern dator kan göra dessa beräkningar på några millisekunder, vilket inte verkar vara mycket, och för en transaktion är det faktiskt inte det. Men när vi tänker på det stora antalet transaktioner i Moneros blockkedja, och att en nod som synkroniserar från grunden måste ladda ner och verifiera var och en av dem, börjar bytes och millisekunder snabbt att staplas upp.

CLSAG kombinerar den matematik som krävs för att bevisa båda till en, samt beräknar båda på en gång, och den gör det på ett säkert sätt. Vad betyder detta på ett säkert sätt? För att reda ut detta, och förhoppningsvis göra det hela mer begripligt, ska vi utforska den utlovade roliga analogin.

Låt oss säga att du behöver gå till både livsmedelsbutiken och järnhandeln för att köpa två olika saker: mat och giftiga rengöringskemikalier. Du vill inte att de ska blandas, för om det sker en olycka kommer kemikalierna att spillas på maten och göra den oätlig. Du bestämmer dig för att vara supersäker och kör från ditt hus till mataffären, köper maten och kör sedan tillbaka till ditt hus. Först när du har lastat av maten sätter du dig i bilen igen, kör till järnaffären och tillbaka till ditt hus med kemikalierna. Du har gjort två separata resor för att säkerställa att alla inköp är säkra. Även om det verkligen är säkert är det ineffektivt. Detta representerar MLSAG, där två olika uppsättningar matematik lagras och två olika "resor" görs för att beräkna dem.

Men du bestämmer dig för att du vill ha ett snabbare sätt att göra det på. Det är för mycket bortkastad tid. Visst, att göra det en eller två gånger kommer inte att stjäla ditt liv, men att behöva göra det om och om igen, timmarna börjar lägga upp. Du börjar undra om du kan göra en resa istället. Från ditt hus, till mataffären, till järnaffären och tillbaka hem. Du kan inte bara slänga in allt i bilen på måfå. Det är inte säkert. Istället anger du olika platser i bilen för olika saker, och ser till att allt passar snyggt på sin plats. På så sätt kan du på ett säkert sätt göra en resa till båda butikerna och hålla sakerna borta från varandra. Detta representerar CLSAG. Det finns nu bara en uppsättning matematik lagrad i denna transaktion för att bevisa dessa två saker, och det görs på ett sådant sätt att de inte stör varandra. En resa måste fortfarande göras, men du har minskat antalet ganska drastiskt.

Allt detta låter ganska spännande. Är det möjligt att vi kan hitta andra genvägar, eller andra sätt att spara tid och utrymme? Svaret är både ja och nej. Enligt nuvarande MRL-forskare är det sannolikt inte möjligt att ytterligare modifiera konstruktionerna av SAG-typ för bättre storlek eller hastighet, men andra konstruktioner som Arcturus, Omniring, RCT3 eller Triptych ger mycket bättre storleksskalning och verifieringsfördelar med hjälp av andra matematiska metoder. Var och en av dessa "nästa generations" metoder för entydiga undertecknarprotokoll har dock sina egna kompromisser i implementeringsdetaljer och genomgår aktiv forskning och utredning.

Monero är trots allt alltid nyskapande.

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

  * [Hur Monero löste problemet med blockstorlek som plågar Bitcoin](/knowledge/dynamic-block-size)/

  * [Varför Monero har en svans emission](/knowledge/monero-tail-emission)/

  * [En kort historia om Monero](/knowledge/monero-history)/

  * [Wired Magazine har fel om Monero, här är varför](/knowledge/wired-article-debunked)/

  * [Topp 15 Monero myter och bekymmer debunked](/knowledge/monero-myths-debunked)/

  * [Hur Dandelion++ håller Moneros transaktionsursprung privat](/knowledge/monero-dandelion)/

  * [Varför Monero är öppen källkod och decentraliserad](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: Vad gör RandomX så speciellt](/knowledge/monero-mining-randomx)/

  * [Varför Monero är bättre än Dash, Zcash, Zcoin (även med Lelantus), Grin och Bitcoin Mixers som Wasabi (Uppdaterad maj 2020)](/knowledge/why-monero-is-better)/

Vidare läsning