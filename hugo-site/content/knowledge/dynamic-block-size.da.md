---
title: "Hvordan Monero løste blokstørrelsesproblemet, der plager Bitcoin"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Bemærk:** Det anbefales stærkt, at læseren har læst vores artikler ["Why Monero Has A Tail Emission"](/knowledge/monero-tail-emission) og ["Monero Mining: What Makes RandomX så speciel"](/knowledge/monero-mining-randomx). Denne artikel bygger på de begreber, der præsenteres der._

Når enkeltpersoner diskuterer problemerne med blockchain, vil et af de første ord, der dukker op, være "skalering". Det er ikke en hemmelighed, at blockchains ikke skalerer godt, men de fleste ved hvorfor.

Sandheden er, at skalering faktisk er et paraplybegreb, der dækker to forskellige kategorier: Protokolstøtte og teknologisk støtte på et givet tidspunkt. I denne artikel vil vi fokusere vores opmærksomhed på én, Protokolsupport er dybest set et mål for, hvor mange transaktioner protokollen kan håndtere på et givet tidspunkt.

Bitcoin har en blokstørrelsesgrænse, hvilket betyder, at når nok transaktioner er inkluderet i en blok, skal eventuelle yderligere transaktioner vente i kø til næste blok. En nyttig analogi ville være at tænke på et tog. Et tog holder op til stationen, og dem, der står i kø, melder sig ind. Når toget er fyldt, skal enhver, der står udenfor, vente på den næste.

Bitcoin bruger gebyrer til at bestemme, hvem der kommer ind i blokken eller ej. Når man hopper tilbage til toganalogien, kan man forestille sig, at en potentiel passager, der er ved at blive efterladt, tilbyder togingeniøren fem dollars for at give ham en plads. Andre passagerer følger trop, og til sidst er der en budkrig for at se, hvem der får hvilke sæder. Det er op til chaufføren at beslutte, om han vil overholde først-til-mølle-politikken, men det er i hans bedste økonomiske interesse at maksimere sin indkomst ved at tage de højestbydende med ombord.

I denne analogi er minearbejdere lokoførerne. De kan inkludere hvilke transaktioner de ønsker i blokken, men de vil generelt vælge dem, der har de højest betalte gebyrer.

Alternativt, hvis blokkene ikke er meget fulde, har folk ikke noget incitament til at betale høje gebyrer, fordi der er masser af ledige pladser til overs.

På højden af kryptovalutaboomet i 2017 blev Bitcoin oversvømmet med transaktioner, og gebyrerne steg i vejret for dem, der ønskede at blive inkluderet i den næste blok, eller enhver nær fremtidig blok for den sags skyld. De, der ikke var villige til at betale høje gebyrer, så deres transaktioner skubbet tilbage i timer, dage eller endda helt falde ud af køen.

Dette var et rystende indblik i, hvordan Bitcoin ville klare sig, hvis den ofte omtalte 'masseadoption' skulle finde sted. Hvis Bitcoin skulle bruges af masserne, ville tingene være endnu værre end i 2017, og Bitcoin ville være utilgængelig for andre end de velhavende, simpelthen fordi gennemløbet er lille på grund af en fast blokstørrelse, hvilket får gebyrmarkedet til at tage over .

Monero forudså dette og ville gøre noget anderledes. Så Monero-udviklerne implementerede en dynamisk blokstørrelse.

Grundlæggende har Monero også en kasket i blokstørrelse, men det er en blød kasket. Når rækken af ventende transaktioner bliver for lang, kan minearbejderne øge størrelsen på blokkene. Med vores toganalogi kan du forestille dig at tilføje flere togvogne, så de passer til de ekstra passagerer. Når køen er tom, skrumper blokkene tilbage til deres oprindelige størrelse fremadrettet.

Hvis dette virker som en god idé, virker det rimeligt at spørge, hvorfor Monero er den eneste kryptovaluta, der har implementeret dette. Hvorfor ikke tilføje det på Bitcoin for at sætte en stopper for gennemstrømningsproblemerne?

Dette er desværre ikke muligt. Der er flere grunde til, og vi vil gøre vores bedste for at forklare.

Det er altid i en minearbejders interesse at have store blokke. Med store blokke kan de passe ind i flere transaktioner og tjene flere penge på gebyrerne såvel som blokbelønningerne. Dette har potentiale til at føre til spam-angreb, hvor nogen sender mange små transaktioner, med små gebyrer, for at blæse kæden op. Miner's ville bare hæve blokstørrelsen inkludere dem alle, fordi penge er penge, uanset hvor små de er. Dette ville føre til konsekvent store blokke med ringe økonomisk fordel. Bitcoin løser dette ved kunstigt at begrænse blokstørrelsen og derved generere et gebyrmarked. Spam-angribere skulle betale de andre brugere i gebyrer, og det er ikke længere billigt. Men det betyder, at blokke bliver fulde, hvilket lader nogle transaktioner vente som nævnt ovenfor.

Så hvordan kan Monero have dynamiske blokstørrelser, men undgå spam-angreb? Svaret er enkelt, men smart. En straf på blokbelønningen indføres, når en blokering er større end normalt. Hvis en minearbejder ønsker at øge blokstørrelsen, vil belønningen de får ved at finde den blok være mindre, end de ellers ville modtage. Så de vil kun øge blokstørrelsen, når brugernes betalte transaktionsgebyrer opvejer den tabte del af blokbelønningen. For eksempel, hvis minearbejderen ville miste 0,5 XMR ved at hæve blokstørrelsen, og summen af de betalte transaktionsgebyrer ville være 0,4 XMR, så ville der være et nettotab på 0,1 XMR, hvis de skulle hæve størrelsen, så de ville ikke ikke gør det. Omvendt, hvis de samlede transaktionsgebyrer lægges op til 0,7 XMR, så ville der være en nettogevinst på 0,2 XMR, selvom de mister 0,5 XMR fra blokbelønningsstraffen, så minearbejderen vil øge størrelsen.

Disse dynamiske blokeringer giver netværket mulighed for at vokse organisk, uden at begrænse blokstørrelsen for at skabe et tvunget gebyrmarked, samtidig med at spam-angreb undgås. Der er flere vinkler, vi kan se denne idé fra, og flere grunde til, at det ikke ville være muligt at tilføje til Bitcoin, men indtil videre håber vi, at læseren har en forståelse for, hvordan Monero omgår flere af problemerne i Bitcoin og dets derivater, og hvordan den planlægger at skalere sin gennemstrømning ind i fremtiden.

Yderligere læsning