---
title: "Visa taggar: Hur en byte kommer att minska Monero plånbokssynkroniseringstider med 40% +"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Ett av de vanligaste klagomålen kring att använda Monero dagligen är den tid det kan ta att synkronisera en plånbok innan man kan skicka Monero. Tack och lov har utvecklare och forskare inom Monero-communityt hittat ett briljant sätt att minska tiden det tar dig att synkronisera din plånbok med 40 %+ utan extra blockchain-bloat, avgifter, etc.

Ange "visa taggar", ett tillägg på en byte till data för varje transaktion – kommer till Monero i nästa nätverksuppgradering!

## Varför är Moneros plånbokssynkronisering långsammare än Bitcoins?

En av de första frågorna vi måste svara på för att bättre förstå behovet av en lösning som visningstaggar är varför Moneros plånbokssynkronisering är långsammare än kryptovalutor som Bitcoin.

I Bitcoin, eftersom alla transaktioner inte är privata och avslöjar de mynt som spenderas, beloppen och adresserna som är involverade i kedjan, kan Bitcoin-plånböcker helt enkelt leta efter eventuella outnyttjade transaktionsutdata (UTXO) eller använda adresser för en given plånbok , snabbt skanna blockkedjan efter endast UTXO:er som ägs av dessa adresser för att ta reda på vilka mynt som tillhör din plånbok och kan användas.

I Monero bevarar dock alla transaktioner användarens integritet genom att dölja avsändaren, mottagaren och beloppen som är involverade i varje transaktion. Denna integritet, även om den är avgörande för att skydda användarna av nätverket, introducerar också långsammare plånbokssynkronisering. I Monero måste din plånbok jämföra varje transaktionsutdata (TXO) som finns på nätverket med din plånboks privata nycklar.

Denna jämförelse involverar mycket komplex matematik och kryptografi för att validera att en utdata verkligen är din, eftersom alla belopp, adresser och kända uttag (eller mynt) är dolda i kedjan i Monero.

## Vad är visnings taggar?

Som ett sätt att minska synkroniseringstiden för Monero-plånböcker, kom [en forskare vid namn UkoeHB på ett nytt tillvägagångssätt](https://github.com/monero-project/research-lab/issues/73) – lägg till en 1-byte "tagg" till varje transaktion med hjälp av en delad hemlighet som endast är känd till avsändaren och mottagaren av transaktionen.

Denna delade hemligheten genereras av avsändaren med den adress som mottagaren har gett dem och kräver inget aktivt samarbete av avsändaren och mottagaren. Den första byten (eller tecknet) av denna delade hemlighet läggs sedan till transaktionens data när den publiceras på Monero-nätverket.

När en av deltagarna i den transaktionen vill synkronisera sin plånbok med Monero blockchain efteråt, istället för att behöva utföra all komplex matematik och kryptografi för varje TXO på nätverket, kan plånboken nu bara kontrollera efter det 1-byte-fältet i varje transaktion och först därefter utföra den tidskrävande verifieringen på transaktioner som har den taggen – 1/256 TSO på nätverket, för att vara exakt!

Den här taggen avslöjar ingen information om transaktionen för externa tittare, lägger bara till 1-byte (ett försumbart belopp) till transaktionsstorlekar, och ändå tillåter oss att minska synkroniseringstiderna med 40 %+ genom att minska på de komplexa verifieringarna nödvändigt!

## Visa taggar: ett förenklat exempel

Föreställ dig att du har 4 096 lådor i ett rum, varav endast 5 lådor tillhör dig. Lådorna är alla helt omöjliga att särskilja från utsidan, och det enda sättet att se om en låda är något för dig är att öppna den och lösa ett tidskrävande matematiskt problem nedskrivet inuti för att säkerställa att den är din.

Föreställ dig nu att du bestämmer dig för att låta personen som skickar de här 5 lådorna till dig generera en speciell kod med din adress och sedan sätta bara det första tecknet i den genererade koden på utsidan av varje ruta som skickas till dig. Alla andra gör samma sak för sina rutor (för att säkerställa att alla rutor fortfarande inte går att särskilja), men nu kan du helt enkelt titta på en teckenkod på utsidan av rutan, och bara öppna de rutor som har det tecknet på sig.[ X753X] 

Medan andra rutor kommer att matcha din kod, även några som inte ägs av dig, är antalet rutor du behöver för att öppna och lösa ett matematiskt problem på nu bara 16 (1/256 rutor!) istället för alla 4 096. 

Nu öppnar du de 16 rutorna, löser matematikproblemen och behåller de 5 rutorna som faktiskt tillhör dig från den gruppen!

Medan andra rutor kommer att matcha din kod, även några som inte ägs av dig, är antalet rutor du behöver för att öppna och lösa ett matematiskt problem på nu bara 16 (1/256 rutor!) istället för alla 4 096. 

Nu öppnar du de 16 rutorna, löser matematikproblemen och behåller de 5 rutorna som faktiskt tillhör dig från den gruppen!

## När kommer visningstaggar att finnas tillgängliga i Monero?

View-taggar är en av funktionerna som för närvarande planeras för inkludering i [kommande nätverksuppgradering](https://github.com/monero-project/meta/issues/630), och bör släppas någon gång i vår. Gemenskapen [höjde 23.3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (i skrivande stund) för att stimulera utvecklingen och implementeringen av visningstaggar, och som ett resultat av det har den stora majoriteten av arbetet med att inkludera visningstaggar i Monero-kodbasen redan varit färdigställt av j-berman i samarbete med granskare och forskare.

När visningstaggar har tillämpats av nätverket kommer alla transaktioner som skickas efter nätverksuppgraderingen att dra nytta av den drastiskt förbättrade plånbokssynkroniseringstiden. Du behöver inte göra något speciellt för att börja använda visningstaggar, din favoritplånbok för Monero kommer helt enkelt att börja använda dem efter nätverksuppgraderingen automatiskt!

## Hur kan jag lära mig mer?

Om detta har väckt din nyfikenhet kring visningstaggar, ta en titt nedan för ytterligare länkar som går på djupet i ämnet:

  * [Minska skanningstider med 1-byte per utdata "view-tagg"](https://github.com/monero-project/research-lab/issues/73)
  * [Lägg till visningstaggar till utgångar för att minska plånboksskanningstiden](https://github.com/monero-project/monero/pull/8061)

Vidare läsning

  * [Hur Monero unikt möjliggör cirkulära ekonomier](/knowledge/monero-circular-economies/)

  * [Moneros ringsignaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Varför (och hur!) du ska hålla i dina egna nycklar](/knowledge/hold-your-keys/)

  * [Bidrar tillbaka till Monero](/knowledge/contributing-to-monero/)

  * [Hur fjärrnoder påverkar Moneros integritet](/knowledge/remote-nodes-privacy/)

  * [Hur Monero använder hard-forks för att uppgradera nätverket](/knowledge/network-upgrades/)

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