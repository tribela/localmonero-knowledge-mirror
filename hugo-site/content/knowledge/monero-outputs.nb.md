---
title: "Monero-utganger forklart"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero, i likhet med andre kryptovalutaer, bruker utdata som et middel til å regnskapsføre midler. Mange kryptokyndige brukere har sikkert hørt dette begrepet før, men ikke alle forstår hva de mener og hvordan de fungerer. Som utforsket i vår [ringsignaturartikkel](/knowledge/ring-signatures), er utdata den faktiske enheten som utveksles på blokkjeden mellom transaksjonspartnere. Ligner på en dollarseddel, men beløpet er ikke i en fast valør.

Hvis du får betalt $16 for en jobb, kan du motta en dollarseddel, en femdollarseddel og en tidollarseddel. Du har $16, men du har også tre forskjellige sedler i lommeboken. Hvis du ønsket å betale noen 6 dollar, kunne du bruke 5- og 1-regningen, men hvis du ville betale noen $8, kunne du bare bruke $10 og motta $2 tilbake i bytte. Til slutt, hvis du ønsket å betale noen $14, ville du måtte bruke alle tre regningene, og ville motta $2 tilbake i bytte, men for et øyeblikk, når du overleverer alle tre regningene, har du ingen penger i lommeboken før du får endre tilbake.

Monero fungerer på samme måte. Tenk deg at du driver en butikk og gjør tre salg på tre forskjellige varer. Du kan motta 1,5 XMR, 2,25 XMR og 5,25 XMR for totalt 9 XMR, men du har også tre forskjellige utganger i lommeboken med de valørene som er oppgitt tidligere. Akkurat som med dollar, vil du kanskje betale noen 3 XMR. Du kan bare bruke 5,25 XMR-utgangen og motta 2,25 XMR tilbake i endring, eller du kan kombinere 1,5 og 2,25 XMR-utgangene og få 0,75 XMR tilbake i endring.

Men så snart du sender transaksjonen, settes utdataene du bruker i en "låst" tilstand, noe som betyr at de er utilgjengelige før du mottar endringen tilbake. Protokollen låser opp midlene (dvs. gir deg tilbake endringen) etter 10 bekreftelser, eller rundt 20 minutter. Akkurat som når du har overlevert dollarsedlene fra lommeboken din, kan du ikke bruke pengene igjen før du får vekslepengene tilbake fra kassereren, Monero er utilgjengelig før du får vekslingen tilbake.

La oss gå tilbake til eksemplet med å sende 3 XMR til noen, og du bruker 5,25 XMR-utgangen. Nå, mens du venter på at 1.75 XMR er tilbake i endring, kan du ikke bruke den. Denne 1,75 XMR er utilgjengelig for deg. Men du kan fortsatt bruke 1,5 XMR- og 2,25 XMR-utgangene, siden disse ikke ble brukt. Hvis du går tilbake til dollareksemplet, hvis du betalte noen $8, som i eksemplet før, ville du ikke kunne bruke $2 som du forventer tilbake i endring før det er gitt til deg, men i dette eksemplet har du fortsatt en $10-seddel som er ubrukt i lommeboken din. Dette kan fortsatt brukes til å kjøpe hva du vil mens du venter på endringen. Det samme med Monero.

Dette er ofte et forvirringspunkt for nye Monero-brukere. Ofte kan en bruker bare ha én utgang i lommeboken, mottatt fra en børs eller en venn. La oss si at denne utgangen er 20 XMR. De har ingen andre utganger i lommeboken. De ønsker nå å gi en donasjon til to av favorittorganisasjonene deres. De sender 5 XMR til den første veldedige organisasjonen og blir deretter forvirret fordi, selv om de burde ha 15 XMR igjen, kan de ikke umiddelbart sende den neste donasjonen til den andre veldedige organisasjonen. Som du kanskje har gjettet, er dette fordi 15 XMR er låst. Den kan ikke brukes før den er returnert som veksel (10 bekreftelser eller rundt 20 minutter). Etter at pengene deres er låst opp, vil de kunne sende sin andre donasjon.

Bare for å gjenta poenget, de ville ikke hatt dette problemet hvis de hadde hatt flere utganger i stedet, for eksempel to 10 XMR-utganger eller lignende. De ville kunne sende begge donasjonene rett etter hverandre, fordi den første donasjonen ville bruke en av de 10 XMR-utgangene (og vente 10 bekreftelser for å motta 5 XMR tilbake i endring), og den andre donasjonen ville bruke de andre 10 XMR utgang.

Noen kryptovaluta-lommebøker har en funksjon kalt "output management", som ganske enkelt viser en bruker hvilke utganger de har for øyeblikket (i tillegg til totalsummen), samt lar dem velge hvilke de vil bruke når de bruker deres kryptovaluta.

Fra nå av gjør Monero GUI utvalg for brukere automatisk, ettersom brukere som velger sine egne utganger ofte fører til forvirring eller i noen tilfeller skadet personvernet. Det er imidlertid lommebøker under konstruksjon, slik som det nye Feather-lommebokprosjektet, som vil inneholde disse utdatabehandlingsfunksjonene.

Vi har snakket mye om sendingsdelen, men noe fascinerende skjer på mottakersiden. Går tilbake til vårt eksempel på å sende 3 XMR til noen, og bruke dine 1,5 XMR og 2,25 XMR utganger i transaksjonen (mens du forventer 0,75 XMR i endring), mottar mottakeren IKKE to utganger på 1,5 XMR og 2,25 XMR. De mottar i stedet EN 3 XMR-utgang.

I bakgrunnen kombinerer protokollen alle utdataene som brukes til utgifter, og gir mottakeren én utgang av det betalte beløpet, og sender én endringsutgang tilbake til avsenderen. Så avsenderen vil også motta en utgang tilbake som endring, uavhengig av om de brukte to, tre eller ti utganger for å sende transaksjonen.

Vi håper dette har ryddet opp i litt forvirring om utdata og hvordan den interne regnskapsføringen av protokollen fungerer, samt det vanlige brukeren som står overfor problemet med forvirring når de møter låste midler. I en annen artikkel vil vi utforske hvordan du administrerer utdataene dine for å minimere sjansen for å måtte vente på ulåste midler før du sender fremtidige transaksjoner.

Videre lesning

  * [Hvordan Monero unikt muliggjør sirkulære økonomier](/knowledge/monero-circular-economies)/

  * [Moneros ringsignaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Hvorfor (og hvordan!) du bør holde dine egne nøkler](/knowledge/hold-your-keys)/

  * [Bidrar tilbake til Monero](/knowledge/contributing-to-monero)/

  * [Hvordan eksterne noder påvirker Moneros personvern](/knowledge/remote-nodes-privacy)/

  * [Hvordan Monero bruker hard-forks for å oppgradere nettverket](/knowledge/network-upgrades)/

  * [Se tagger: Hvordan én byte vil redusere Monero-lommeboksynkroniseringstiden med 40 %+](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool og dens rolle i desentralisering av Monero-gruvedrift](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Hva det vil gjøre for Monero](/knowledge/seraphis-for-monero)/

  * [Er det like privat å konvertere Bitcoin til Monero som å kjøpe Monero direkte?](/knowledge/most-private-way-to-buy-monero)/

  * [Hvorfor Monero bruker et tillitsløst oppsett i motsetning til Zcash](/knowledge/monero-trustless-setup)/

  * [Hvorfor Monero er en bedre butikk med verdi enn Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Hvordan Monero kan overvinne Bitcoins nettverkseffekter](/knowledge/network-effect)/

  * [Hvorfor Monero har det mest kritiske tenkningssamfunnet](/knowledge/critical-thinking)/

  * [Svindel å se etter når du bruker Monero](/knowledge/monero-scams)/

  * [Hvordan Atomic Swaps vil fungere i Monero](/knowledge/monero-atomic-swaps)/

  * [Hva enhver Monero-bruker trenger å vite når det kommer til nettverk](/knowledge/monero-networking)/

  * [Hvordan RingCT skjuler Monero-transaksjonsbeløp](/knowledge/monero-ringct)/

  * [Hvordan Monero Stealth-adresser beskytter identiteten din](/knowledge/monero-stealth-addresses)/

  * [Hvordan Monero-underadresser forhindrer identitetskobling](/knowledge/monero-subaddresses)/

  * [Monero beste praksis for nybegynnere](/knowledge/monero-best-practices)/

  * [Hvordan ringsignaturer obskure Moneros utganger](/knowledge/ring-signatures)/

  * [Hvordan Monero løste blokkstørrelsesproblemet som plager Bitcoin](/knowledge/dynamic-block-size)/

  * [Hvordan CLSAG vil forbedre Moneros effektivitet](/knowledge/what-is-clsag)/

  * [Hvorfor Monero har en haleutslipp](/knowledge/monero-tail-emission)/

  * [En kort historie om Monero](/knowledge/monero-history)/

  * [Wired Magazine tar feil om Monero, her er hvorfor](/knowledge/wired-article-debunked)/

  * [Topp 15 Monero-myter og bekymringer avslørt](/knowledge/monero-myths-debunked)/

  * [Hvordan Dandelion++ holder Moneros transaksjonsopprinnelse privat](/knowledge/monero-dandelion)/

  * [Hvorfor Monero er åpen kildekode og desentralisert](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: Hva gjør RandomX så spesiell](/knowledge/monero-mining-randomx)/

  * [Hvorfor Monero er bedre enn Dash, Zcash, Zcoin (selv med Lelantus), Grin og Bitcoin-miksere som Wasabi (Oppdatert mai 2020)](/knowledge/why-monero-is-better)/

Videre lesning