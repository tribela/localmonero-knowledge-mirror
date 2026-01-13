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

## När kommer visningstaggar att finnas tillgängliga i Monero?

View-taggar är en av funktionerna som för närvarande planeras för inkludering i [kommande nätverksuppgradering](https://github.com/monero-project/meta/issues/630), och bör släppas någon gång i vår. Gemenskapen [höjde 23.3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (i skrivande stund) för att stimulera utvecklingen och implementeringen av visningstaggar, och som ett resultat av det har den stora majoriteten av arbetet med att inkludera visningstaggar i Monero-kodbasen redan varit färdigställt av j-berman i samarbete med granskare och forskare.

När visningstaggar har tillämpats av nätverket kommer alla transaktioner som skickas efter nätverksuppgraderingen att dra nytta av den drastiskt förbättrade plånbokssynkroniseringstiden. Du behöver inte göra något speciellt för att börja använda visningstaggar, din favoritplånbok för Monero kommer helt enkelt att börja använda dem efter nätverksuppgraderingen automatiskt!

## Hur kan jag lära mig mer?

Om detta har väckt din nyfikenhet kring visningstaggar, ta en titt nedan för ytterligare länkar som går på djupet i ämnet:

  * [Minska skanningstider med 1-byte per utdata "view-tagg"](https://github.com/monero-project/research-lab/issues/73)
  * [Lägg till visningstaggar till utgångar för att minska plånboksskanningstiden](https://github.com/monero-project/monero/pull/8061)

Vidare läsning