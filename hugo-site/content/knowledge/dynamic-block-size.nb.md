---
title: "Hvordan Monero løste blokkstørrelsesproblemet som plager Bitcoin"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Merk:** Det anbefales sterkt at leseren har lest artiklene våre ["Why Monero Has A Tail Emission"](/knowledge/monero-tail-emission) og ["Monero Mining: What Makes RandomX så spesiell"](/knowledge/monero-mining-randomx). Denne artikkelen bygger på konseptene som presenteres der._

Når enkeltpersoner diskuterer problemene med blokkjede, vil et av de første ordene som dukker opp være "skalering". Det er ikke en hemmelighet at blokkjeder ikke skalerer godt, men de fleste vet ikke hvorfor.

Sannheten er at skalering faktisk er et paraplybegrep som dekker to forskjellige kategorier: Protokollstøtte og teknologisk støtte på et gitt tidspunkt. I denne artikkelen skal vi fokusere vår oppmerksomhet på én. Protokollstøtte er i utgangspunktet et mål på hvor mange transaksjoner protokollen kan håndtere på et gitt tidspunkt.

Bitcoin har en blokkstørrelsesgrense, noe som betyr at når nok transaksjoner er inkludert i en blokk, må eventuelle ekstra transaksjoner stå i kø til neste blokk. En nyttig analogi ville være å tenke på et tog. Et tog kjører opp til stasjonen, og de som står i kø melder seg inn. Når toget er fullt, må alle som står utenfor vente på neste.

Bitcoin bruker gebyrer for å bestemme hvem som kommer inn i blokken eller ikke. Når man hopper tilbake til toganalogien, kan man forestille seg en potensiell passasjer, som er i ferd med å bli etterlatt, tilbyr togingeniøren fem dollar for å gi ham et sete. Andre passasjerer følger etter, og etter hvert blir det budkrig for å se hvem som får hvilke seter. Det er opp til sjåføren å avgjøre om han vil respektere først-til-mølla-policyen, men det er i hans beste økonomiske interesse å maksimere inntekten ved å ta de høyestbydende om bord.

I denne analogien er gruvearbeidere lokførerne. De kan inkludere hvilke transaksjoner de vil i blokken, men de vil vanligvis velge de som har høyest betalte avgifter.

Alternativt, hvis blokkene ikke er veldig fulle, har folk ingen insentiv til å betale høye avgifter fordi det er mange ledige seter til overs.

På høyden av kryptovalutaboomen i 2017 ble Bitcoin oversvømmet med transaksjoner, og gebyrene skjøt i været for de som ønsket å bli inkludert i neste blokk, eller en hvilken som helst nær fremtidig blokk for den saks skyld. De som ikke var villige til å betale høye gebyrer, så at transaksjonene deres ble presset tilbake i timer, dager eller til og med droppet ut av køen.

Dette var en opprivende innsikt i hvordan Bitcoin ville klare seg hvis den ofte omtalte «masseadopsjonen» skulle skje. Hvis Bitcoin skulle brukes av massene, ville ting vært enda verre enn i 2017, og Bitcoin ville være utilgjengelig for andre enn de velstående, rett og slett fordi gjennomstrømningen er liten på grunn av en fast blokkstørrelse, noe som får gebyrmarkedet til å ta over .

Monero forutså dette og ønsket å gjøre noe annerledes. Så Monero-utviklerne implementerte en dynamisk blokkstørrelse.

I utgangspunktet har Monero også en hette i blokkstørrelse, men det er en myk hette. Når køen av ventende transaksjoner blir for lang, kan gruvearbeiderne øke størrelsen på blokkene. Med vår toganalogi kan du tenke deg å legge til flere togvogner for å passe de ekstra passasjerene. Etter at køen er tom, krymper blokkene tilbake til sin opprinnelige størrelse fremover.

Hvis dette virker som en god idé, virker det rimelig å spørre hvorfor Monero er den eneste kryptovalutaen som har implementert dette. Hvorfor ikke legge det til på Bitcoin for å stoppe gjennomstrømningsproblemene?

Dette er dessverre ikke mulig. Det er flere grunner til hvorfor, og vi skal gjøre vårt beste for å forklare.

Det er alltid i en gruvearbeiders interesse å ha store blokker. Med store blokker kan de få plass til flere transaksjoner, og tjene mer penger på gebyrene, så vel som blokkbelønningene. Dette har potensial til å føre til spam-angrep, der noen sender mange små transaksjoner, med små gebyrer, for å blåse opp kjeden. Miner's ville bare øke blokkstørrelsen inkludere dem alle fordi penger er penger, uansett hvor lite det er. Dette vil føre til gjennomgående store blokker med liten økonomisk nytte. Bitcoin løser dette ved å kunstig begrense blokkstørrelsen, og dermed generere et gebyrmarked. Spam-angripere ville måtte betale de andre brukerne i avgifter, og det er ikke lenger billig. Men dette betyr at blokkene blir fulle og lar noen transaksjoner vente som nevnt ovenfor.

Så hvordan kan Monero ha dynamiske blokkstørrelser, men unngå spam-angrep? Svaret er enkelt, men smart. En straff på blokkbelønningen introduseres når en blokk er større enn normalt. Hvis en gruvearbeider ønsker å øke blokkstørrelsen, vil belønningen de får ved å finne den blokken være mindre enn de ellers ville fått. Så de vil bare øke blokkstørrelsen når de betalte transaksjonsgebyrene til brukerne oppveier den tapte delen av blokkbelønningen. For eksempel, hvis gruvearbeideren ville tape 0,5 XMR ved å øke blokkstørrelsen, og summen av de betalte transaksjonsgebyrene ville være 0,4 XMR, ville det være et nettotap på 0,1 XMR hvis de skulle øke størrelsen, slik at de ville ikke gjør det. Omvendt, hvis de totale transaksjonsgebyrene summeres til 0,7 XMR, vil det være en nettogevinst på 0,2 XMR, selv om de mister 0,5 XMR fra blokkbelønningsstraffen, så gruvearbeideren vil øke størrelsen.

Disse dynamiske blokkeringene lar nettverket vokse organisk, uten å begrense blokkstørrelsen for å lage et tvunget gebyrmarked, samtidig som spam-angrep unngås. Det er flere vinkler vi kan se denne ideen fra, og flere grunner til at det ikke ville være mulig å legge til Bitcoin, men foreløpig håper vi at leseren har forståelse for hvordan Monero omgår flere av problemene i Bitcoin og dens derivater, og hvordan den planlegger å skalere sin gjennomstrømning inn i fremtiden.

Videre lesning

  * [Hvordan Monero unikt muliggjør sirkulære økonomier](/knowledge/monero-circular-economies/)

  * [Moneros ringsignaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Hvorfor (og hvordan!) du bør holde dine egne nøkler](/knowledge/hold-your-keys/)

  * [Bidrar tilbake til Monero](/knowledge/contributing-to-monero/)

  * [Hvordan eksterne noder påvirker Moneros personvern](/knowledge/remote-nodes-privacy/)

  * [Hvordan Monero bruker hard-forks for å oppgradere nettverket](/knowledge/network-upgrades/)

  * [Se tagger: Hvordan én byte vil redusere Monero-lommeboksynkroniseringstiden med 40 %+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool og dens rolle i desentralisering av Monero-gruvedrift](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Hva det vil gjøre for Monero](/knowledge/seraphis-for-monero/)

  * [Er det like privat å konvertere Bitcoin til Monero som å kjøpe Monero direkte?](/knowledge/most-private-way-to-buy-monero/)

  * [Hvorfor Monero bruker et tillitsløst oppsett i motsetning til Zcash](/knowledge/monero-trustless-setup/)

  * [Hvorfor Monero er en bedre butikk med verdi enn Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Hvordan Monero kan overvinne Bitcoins nettverkseffekter](/knowledge/network-effect/)

  * [Hvorfor Monero har det mest kritiske tenkningssamfunnet](/knowledge/critical-thinking/)

  * [Svindel å se etter når du bruker Monero](/knowledge/monero-scams/)

  * [Hvordan Atomic Swaps vil fungere i Monero](/knowledge/monero-atomic-swaps/)

  * [Hva enhver Monero-bruker trenger å vite når det kommer til nettverk](/knowledge/monero-networking/)

  * [Hvordan RingCT skjuler Monero-transaksjonsbeløp](/knowledge/monero-ringct/)

  * [Hvordan Monero Stealth-adresser beskytter identiteten din](/knowledge/monero-stealth-addresses/)

  * [Hvordan Monero-underadresser forhindrer identitetskobling](/knowledge/monero-subaddresses/)

  * [Monero-utganger forklart](/knowledge/monero-outputs/)

  * [Monero beste praksis for nybegynnere](/knowledge/monero-best-practices/)

  * [Hvordan ringsignaturer obskure Moneros utganger](/knowledge/ring-signatures/)

  * [Hvordan CLSAG vil forbedre Moneros effektivitet](/knowledge/what-is-clsag/)

  * [Hvorfor Monero har en haleutslipp](/knowledge/monero-tail-emission/)

  * [En kort historie om Monero](/knowledge/monero-history/)

  * [Wired Magazine tar feil om Monero, her er hvorfor](/knowledge/wired-article-debunked/)

  * [Topp 15 Monero-myter og bekymringer avslørt](/knowledge/monero-myths-debunked/)

  * [Hvordan Dandelion++ holder Moneros transaksjonsopprinnelse privat](/knowledge/monero-dandelion/)

  * [Hvorfor Monero er åpen kildekode og desentralisert](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Hva gjør RandomX så spesiell](/knowledge/monero-mining-randomx/)

  * [Hvorfor Monero er bedre enn Dash, Zcash, Zcoin (selv med Lelantus), Grin og Bitcoin-miksere som Wasabi (Oppdatert mai 2020)](/knowledge/why-monero-is-better/)