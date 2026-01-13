---
title: "Monero Mining: Vad gör RandomX så speciellt"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Den 30 november 2019 hade Monero sin halvårsvisa hårdgaffel, med den mest efterlängtade förändringen att byta från den gamla PoW-algoritmen, cryptonight, till den helt nya, internt utvecklade, RandomX. Monero-gemenskapen tror att RandomX är ett stort steg mot jämlik gruvdrift, men låt oss gräva djupare för att se om så är fallet.

## Syfte

För att kunna bedöma om RandomX är en förbättring måste vi först förstå vad syftet med gruvdrift är. Mining säkrar en blockchain från dubbla utgifter via Nakamoto Consensus. De exakta krångligheterna i hur det gör detta ligger utanför ramen för denna artikel, men de kan läras från många olika källor runt om på internet. Det viktiga är att säkerheten kommer från hash som genereras av datorer (gruvarbetare), i konkurrens med varandra för att hitta den matematiska lösning som krävs för att skapa ytterligare ett block. När de gör detta lägger de till nya transaktioner till blockkedjan. I utbyte för sitt arbete (haschar) kompenseras de med nypräglade mynt.   
  
Det finns ett antal problem som kan uppstå med den här installationen, och de kräver lämpliga incitament för att fungera korrekt, men vi kommer att fokusera på ett särskilt problem som kan uppstå. Om gruvdrift är tänkt att vara en tävling, vad händer när en gruvarbetare får en fördel?

## Bakgrund

För sammanhanget, låt oss prata lite om gruvhårdvara. Gruvarbetare använder datorer för att göra jobbet, men vi vet alla att inte alla datorer är lika tillverkade. Vissa datorer är kraftfulla nog att köra AI-nätverk eller intensiva spel, medan andra kämpar med till och med enkla uppgifter. Dessa skillnader i datorkraft påverkar också hashhastigheten, eller den hastighet med vilken de letar efter blocklösningar.   
  
Men även dessa skillnader mellan datorer bleknar i jämförelse med hashhastigheterna för specialiserad hårdvara, även känd som Application Specific Integrated Circuits (ASIC), som utklassar vanliga datorer med flera storleksordningar.  
  
Låt oss ta lite tid att utforska vad som gör ASICs så kraftfulla. Föreställ dig att alla datorer faller någonstans på ett spektrum, som sträcker sig från att kunna göra många saker, men inget bra, till att bara göra en sak, men att göra det väldigt bra. CPU:er och ASIC:er finns i motsatta ändar av detta spektrum.  
  
CPU:er som finns i alla vanliga datorer är i första änden. De kan göra många saker, som att surfa på webben, spela spel eller rendera video, men inte göra någon av dem särskilt bra. Men denna flexibilitet kommer på kostnaden av effektivitet.  
  
ASICs är i andra änden, där de bara kan en sak, men gör det i en otrolig hastighet. De kan bara utföra en matematisk funktion, men eftersom de kan ignorera allt annat är prestationsvinsterna astronomiska. Denna effektivitet kommer dock på bekostnad av flexibilitet, så om funktionen ändras ens något – ett exempel är x + y = z ändras till 2x + y = z – så kommer ASIC att sluta fungera helt och hållet.   
  
Alla äger inte en ASIC, men alla äger datorer. Detta kan leda till en orättvis fördel.

## En rolig analogi

Om detta fortfarande är förvirrande, kanske följande analogi kan hjälpa. Föreställ dig ett lotteri där tusen dollar delas ut varje timme, och detta lotteri låter dig skriva ut dina egna lotter! Du börjar skriva ut så många biljetter du kan på din hemmaskrivare, som kan skriva ut en biljett per sekund. Efter att ha dragit av kostnader för el och bläck ser du att du fortfarande kan göra vinst, även om du bara vinner på lotteriet en gång varannan vecka.  
  
Med tiden utökar du din verksamhet tills du har ett helt rum dedikerat till skrivare. 20 totalt. Allt är bra...tills en ödesdiger dag.  
  
Det finns stora nyheter. Någon har uppfunnit en ny typ av skrivare. Den kan bara skriva ut lotter. Den kan inte skriva ut bilder eller kontorsdokument eller göra dubbelsidig utskrift. Endast lotter. Men den kan skriva ut dem med en hastighet av 1000 biljetter per sekund. Du tittar i ditt lilla skrivarrum. 20 skrivare. Du behöver 980 fler skrivare bara för att hålla jämna steg med EN av dessa monsterskrivare, och om någon har två...?  
  
Du lämnar tyvärr lotterispelet eftersom du inte längre kan motivera kostnaderna för el och bläck.  
  
Men vänta! Ett par veckor senare kommer fler nyheter! Utformningen av biljetten har ändrats. Nu är siffrorna, som brukade vara på toppen, nu på botten. De nya monsterskrivarna är så oflexibla att de inte kan göra det. De kunde bara göra den tidigare designen. Det dröjer inte länge innan du återigen glatt skriver ut. Åtminstone tills någon gör en ny monsterskrivare för den nya designen.

## RandomX

Var passar RandomX in i allt detta? Den försöker jämna ut fördelarna med ASIC:er genom att göra ASIC:er mycket svåra att göra. Den gör detta genom att kräva att gruvarbetare skapar och kör slumpmässig kod istället för hash baserad på en algoritm.  
  
Det kan vara förvirrande hur detta faktiskt hjälper någonting, så låt oss gå tillbaka till vår skrivaranalogi. Kommer du ihåg vad som hände när designen ändrades? De gamla monsterskrivarna blir föråldrade varje kväll, och nya måste utvecklas med den nya designen i åtanke. Vad skulle hända om varje ny lott var tvungen att följa en ny designstandard för varje ny jackpott?   
  
Att skapa en ny monsterskrivare skulle bli otroligt svårt. Du kan inte bara planera på en biljettdesign längre. Eftersom designen är slumpmässig måste tillverkarna av monsterskrivare lägga till färgfunktioner, sätt att skriva ut olika bokstäver och kanter och former med mera. Kort sagt, maskinen de slutade uppfinna skulle vara en vanlig, vanlig skrivare. Precis som alla andra har.  
  
Genom att helt enkelt implementera denna slumpmässighet i biljettdesignen minskade vi avsevärt den stora fördelen från specialiserad hårdvara. RandomX gör samma sak, men med mining.  
  
På detta sätt minimeras fördelarna som ett fåtal utvalda välbärgade människor får, som om de investerar i att skapa "ASIC" för att bryta RandomX, kommer de faktiskt bara att uppfinna starkare, bättre processorer, vilket gynnar världen i stort.  
[] X1455X] Det betyder att den lilla killen med sina 20 biljettskrivare är tillbaka i spelet. Han kan fortfarande ha en svårare tid eftersom dessa rika individer fortfarande kan köpa fler skrivare än han, men åtminstone nu är han inte utklassad av storleksordningar bara från en maskin. Han är konkurrenskraftig på sitt lilla sätt.  
  
Eftersom vi vet att även den lilla killen kan vara konkurrenskraftig i mining Monero, uppmuntrar vi alla att ge det en snurr, antingen i Monero GUI-plånboken, som har stöd för solo-mining, eller genom att ladda ner programvara som underhålls av communityn. Det är enkelt, konkurrenskraftigt och öppet för alla.

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

  * [Hur CLSAG kommer att förbättra Moneros effektivitet](/knowledge/what-is-clsag)/

  * [Varför Monero har en svans emission](/knowledge/monero-tail-emission)/

  * [En kort historia om Monero](/knowledge/monero-history)/

  * [Wired Magazine har fel om Monero, här är varför](/knowledge/wired-article-debunked)/

  * [Topp 15 Monero myter och bekymmer debunked](/knowledge/monero-myths-debunked)/

  * [Hur Dandelion++ håller Moneros transaktionsursprung privat](/knowledge/monero-dandelion)/

  * [Varför Monero är öppen källkod och decentraliserad](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Varför Monero är bättre än Dash, Zcash, Zcoin (även med Lelantus), Grin och Bitcoin Mixers som Wasabi (Uppdaterad maj 2020)](/knowledge/why-monero-is-better)/