---
title: "Hvordan Ring Signaturer Obskure Monero's Outputs"
slug: "ring-signatures"
date: "2020-09-08"
image: "/images/rings.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero er kendt vidt og bredt over hele kryptoområdet som værende kongen af privatlivsmønter. Selvom alle ved, at Monero tilbyder godt privatliv, er der ikke så mange, der forstår, hvordan privatlivets fred fungerer.

Mange andre privatlivsmønter udgiver infografik til sammenligningsdiagrammer, som viser navnene på hver mønts privatlivsteknologi, og i de fleste mærker de Moneros teknologi som RingCT, men dette er kun delvist sandt. Monero har faktisk en tre-benet tilgang til privatliv. Én teknologi til at skjule modtageren af en transaktion, én til at skjule det sendte beløb og én til at skjule det anvendte output, disse er hhv stealth-adresser, RingCT og ringesignaturer.

Denne trestrengede tilgang betyder, at hvis en af teknologierne er brudt, deler de andre ikke nødvendigvis samme skæbne. Ringsignaturer er det svageste led i privatlivsordningen; ordet svag betyder her den mest modtagelige for heuristiske angreb. Lad os tage lidt tid til at udforske dem, skal vi?

Som nævnt ovenfor er målet med ringesignaturer at skjule et output, der bruges i en transaktion. Hvis 'input/output'-terminologien for kryptovaluta er forvirrende for dig, skal du ikke bekymre dig. Det er faktisk ikke så kompliceret. Når du hører 'output', tænk bare på en check. En af de ting, der ikke er helt så almindelig længere, som folk plejer at betale med. Ligesom en check kan den angives i et hvilket som helst beløb - $10, $32,50 osv. - og udveksles mellem transaktionsparter. For kryptovalutaer tjener output disse funktioner.

Når nogen betaler dig 10 Monero, modtager du et 10 XMR-output. Dette output har en værdi (10), og er det, der tages fra afsenderens tegnebog, på samme måde, når du betaler for en tjeneste, forlader en regning din fysiske tegnebog og gives til den person, du køber hos.

Måden outputtet skjules på er ved at konstruere en ring (deraf navnet) af lokkeoutput. Men disse lokkefugle er ikke 'falske' output'. De er reelle tidligere output fra blockchain, som ikke har noget at gøre med den nuværende transaktion, men for en ekstern observatør kan hver af disse output se lige så sandsynlige ud som den virkelige. Størrelsen på sættet af lokkeudgange plus den rigtige kaldes ringestørrelsen, og i øjeblikket er Monero's elleve. Så der er ti lokkeudgange og en rigtig én.

Hvorfor øger vi ikke bare dette tal til 100 eller endda 1000? Jo flere jo bedre, ikke? Nå, fra et privatlivsperspektiv, ja, men der er andre ting at overveje. Lad os gå tilbage til et fysisk eksempel for at se, hvad jeg mener. Hvis du ville gemme en af dine dollarsedler blandt ti lokkefugle, skulle du have omkring elleve dollars i din tegnebog for hver dollar, du ville bruge. En rigtig dollar og ti falske. Dette bliver allerede ret besværligt, hvis du vil bruge blot et par dollars. Forestil dig nu, at vi øgede lokkebeløbet til 1000. For hver en dollar du ville bruge, skulle du have omkring 1001 dollars med. Du bliver nødt til at bære rundt på en dokumentmappe bare for at købe en slikbar! Det er vigtigt at bemærke, at ringsignaturer ikke fungerer helt på denne måde, f.eks. er lokkefuglene i sig selv ikke en del af signaturen, kun referencer til dem, men vi håber, at denne analogi kan være en smule nyttig til at forestille sig de grundlæggende begreber.< /p>

Lækkene på blockchain fungerer på samme måde. Hvert tilføjet lokkemiddel øger tiden og verifikationsomkostningerne for transaktionen. Hver node skal downloade hele ringesignaturen for hver transaktion, og hver ringesignatur indeholder det reelle output, såvel som lokkefuglene. Ikke kun det, men det skal verificere matematikken, at mindst én af disse udgange er ægte, og den matematiske verifikationstid stiger også med hvert lokkemiddel. Det betyder, at vi er nødt til at finde en lykkelig mellemvej, hvor ringstørrelsen er stor nok til tilstrækkeligt at skjule det reelle output, selv mod mange heuristiske angreb, men lille nok til ikke at få blockchain til at stige med en massiv hastighed. Det er ikke nok at vælge et vilkårligt tal eller blot at øge ringstørrelsen, når vi gør signaturen mindre (såsom med CLSAG). Monero-fællesskabet ønsker konkrete, matematiske beviser for, hvilken ringstørrelse der giver de bedste kompromiser. Et tal for lille, og privatlivet vil ikke være stærkt nok mod heuristiske angreb. For stor, og vi får muligvis kun marginale fordele på privatlivssiden og lider unødigt i forhold til skalering.

En sidste ting at nævne. Noget Monero-litteratur forenkler og siger, at ringsignaturer skjuler afsenderen, men det er ikke helt sandt, og forskellen er ikke kun pedantisk. Forskellen mellem afsenderen (et menneske) og et output (en regning) er stor, når det kommer til at bevare privatlivets fred. Mens et output kan have bånd til en afsender, er et output i sig selv ikke lig med en afsender. Så selvom en ringesignatur skulle brydes, er den ikke nødvendigvis forbundet med en persons identitet, og både beløbet og modtageren er stadig skjult, hvilket minimerer skaden på alle parters privatliv.

Det betyder ikke, at en ødelagt ringesignatur er insubetydelige. Eventuelle lækkede metadata er dårlige og har potentialet til at afsløre mere information, end vi tror, især når de bruges sammen med andre metadata. Så vi gør vores bedste for at sikre, at den valgte ringestørrelse har en akademisk stringens bag beslutningen, at anden metadatalækage minimeres, og at brugeren oplever, at standarderne er de bedst mulige handlinger.

Men hvis sandsynligheden for en ødelagt signatur stadig bekymrer dig, så er der nogle utrolige nyheder i horisonten. Den næste generation af privatlivsprotokoller, der arbejdes på, såsom Triptych, Arcturus og Lelantus, har virkelig pæne muligheder. I disse protokoller skaleres størrelsen logaritmisk, ikke lineært, efterhånden som ringstørrelsen øges. Det betyder, at vi kan få plads til 100 lokkefugle, men den brugte plads er tættere på ringstørrelse 10 i den gamle tech. Det er noget af forskellen, og det vil forbedre privatlivets fred betydeligt.

I katte- og mus-spillet, der er privatliv, innoverer Monero løbende for at være på forkant og sikre det bedste praktiske privatliv for alle.

Lækkene på blockchain fungerer på samme måde. Hvert tilføjet lokkemiddel øger tiden og verifikationsomkostningerne for transaktionen. Hver node skal downloade hele ringesignaturen for hver transaktion, og hver ringesignatur indeholder det reelle output, såvel som lokkefuglene. Ikke kun det, men det skal verificere matematikken, at mindst én af disse udgange er ægte, og den matematiske verifikationstid stiger også med hvert lokkemiddel. Det betyder, at vi er nødt til at finde en lykkelig mellemvej, hvor ringstørrelsen er stor nok til tilstrækkeligt at skjule det reelle output, selv mod mange heuristiske angreb, men lille nok til ikke at få blockchain til at stige med en massiv hastighed. Det er ikke nok at vælge et vilkårligt tal eller blot at øge ringstørrelsen, når vi gør signaturen mindre (såsom med CLSAG). Monero-fællesskabet ønsker konkrete, matematiske beviser for, hvilken ringstørrelse der giver de bedste kompromiser. Et tal for lille, og privatlivet vil ikke være stærkt nok mod heuristiske angreb. For stor, og vi får muligvis kun marginale fordele på privatlivssiden og lider unødigt i forhold til skalering.

En sidste ting at nævne. Noget Monero-litteratur forenkler og siger, at ringsignaturer skjuler afsenderen, men det er ikke helt sandt, og forskellen er ikke kun pedantisk. Forskellen mellem afsenderen (et menneske) og et output (en regning) er stor, når det kommer til at bevare privatlivets fred. Mens et output kan have bånd til en afsender, er et output i sig selv ikke lig med en afsender. Så selvom en ringesignatur skulle brydes, er den ikke nødvendigvis forbundet med en persons identitet, og både beløbet og modtageren er stadig skjult, hvilket minimerer skaden på alle parters privatliv.

Det betyder ikke, at en ødelagt ringesignatur er insubetydelige. Eventuelle lækkede metadata er dårlige og har potentialet til at afsløre mere information, end vi tror, især når de bruges sammen med andre metadata. Så vi gør vores bedste for at sikre, at den valgte ringestørrelse har en akademisk stringens bag beslutningen, at anden metadatalækage minimeres, og at brugeren oplever, at standarderne er de bedst mulige handlinger.

Men hvis sandsynligheden for en ødelagt signatur stadig bekymrer dig, så er der nogle utrolige nyheder i horisonten. Den næste generation af privatlivsprotokoller, der arbejdes på, såsom Triptych, Arcturus og Lelantus, har virkelig pæne muligheder. I disse protokoller skaleres størrelsen logaritmisk, ikke lineært, efterhånden som ringstørrelsen øges. Det betyder, at vi kan få plads til 100 lokkefugle, men den brugte plads er tættere på ringstørrelse 10 i den gamle tech. Det er noget af forskellen, og det vil forbedre privatlivets fred betydeligt.

I katte- og mus-spillet, der er privatliv, innoverer Monero løbende for at være på forkant og sikre det bedste praktiske privatliv for alle.

Yderligere læsning

  * [Hvordan Monero unikt aktiverer cirkulær økonomier](/knowledge/monero-circular-economies/)

  * [Monero's ring signaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Hvorfor (og hvordan!) skal du holde dine egne nøgler](/knowledge/hold-your-keys/)

  * [Bidrager tilbage til Monero](/knowledge/contributing-to-monero/)

  * [Hvordan fjern noder påvirker Monero's privatliv](/knowledge/remote-nodes-privacy/)

  * [Hvordan Monero bruger hard-forks til at opgradere den netværk](/knowledge/network-upgrades/)

  * [Se tags: Hvordan en byte vil reducere Monero wallet-synkroniseringstider med 40 %+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool og Dets rolle i Decentralisering Monero Minedrift](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Hvad Det Vil Gør for Monero](/knowledge/seraphis-for-monero/)

  * [Er konvertering af Bitcoin til Monero lige så privat som at købe Monero direkte?](/knowledge/most-private-way-to-buy-monero/)

  * [Hvorfor Monero Brug en Tillidsløs Opsætning i modsætning til Zcash](/knowledge/monero-trustless-setup/)

  * [Hvorfor Monero er en bedre butik af værdi end Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Hvordan Monero Kan Overvinde Bitcoin's Netværk Effekter](/knowledge/network-effect/)

  * [Hvorfor Monero Har Det Mest Kritiske Tænkning Fællesskab](/knowledge/critical-thinking/)

  * [Svindel til Se Ud for Når Bruger Monero](/knowledge/monero-scams/)

  * [Hvordan Atomic Swaps Vil Arbejde i Monero](/knowledge/monero-atomic-swaps/)

  * [Hvad enhver Monero-bruger har brug for at vide, når det kommer til netværk](/knowledge/monero-networking/)

  * [Hvordan RingCT Huder Monero Transaktion Beløb](/knowledge/monero-ringct/)

  * [Hvordan Monero Stealth Adresser Beskyt Din Identitet](/knowledge/monero-stealth-addresses/)

  * [Hvordan Monero Underadresser Forebyg Identitet Linking](/knowledge/monero-subaddresses/)

  * [Monero Outputs Forklaret](/knowledge/monero-outputs/)

  * [Monero Bedste Praksis for Begyndere](/knowledge/monero-best-practices/)

  * [Hvordan Monero løste blokstørrelsesproblemet, der plager Bitcoin](/knowledge/dynamic-block-size/)

  * [Hvordan CLSAG Vilje Forbedre Monero's Effektivitet](/knowledge/what-is-clsag/)

  * [Hvorfor Monero Har en Hale Emission](/knowledge/monero-tail-emission/)

  * [En kort historie om Monero](/knowledge/monero-history/)

  * [Wired Magazine er Forkert Om Monero, Her er Hvorfor](/knowledge/wired-article-debunked/)

  * [Top 15 Monero Myter og Bekymringer Afkræftet](/knowledge/monero-myths-debunked/)

  * [Hvordan Dandelion++ Holder Monero's Transaktion Oprindelse Privat](/knowledge/monero-dandelion/)

  * [Hvorfor Monero Er Open Source Og Decentraliseret](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Hvad Gør RandomX så Speciel](/knowledge/monero-mining-randomx/)

  * [Hvorfor Monero er bedre end Dash, Zcash, Zcoin (selv med Lelantus), Grin og Bitcoin-mixere som Wasabi (Opdateret maj 2020)](/knowledge/why-monero-is-better/)