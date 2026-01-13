---
title: "Hvordan Monero Stealth-adresser beskytter identiteten din"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero har implementert en tredelt tilnærming til personvern. Disse teknologiene er [ringsignaturer](/knowledge/ring-signatures), som skjuler den sanne utgangen (sender), RingCT som skjuler beløpene, og stealth-adresser, som skjuler mottakeren. I dag skal vi diskutere den siste av disse nevnte teknologiene: stealth-adresser.

Det er mange grunner til at en person ønsker å skjule hvem de sender til. Vi må aldri la noen prøve å overbevise oss om at alle eksempler på dette er usmakelig oppførsel. Ting som å sende til et upopulært politisk parti, donere til veldedige organisasjoner eller støtte de som kulturen anser som "kansellert" er alle eksempler på hvor man kanskje ønsker å skjule forbruksatferden sin av frykt for ettervirkninger, men er helt legitime av natur.[X840X ] 

På en gjennomsiktig blokkjede er adressene man sender transaksjonene sine til, synlige for alle. Det er viktig å tenke på at hvis gruvearbeidere selv er uenige i hvor pengene går, kan de velge å ikke gruve dem inn i en blokk, og effektivt sensurere denne transaksjonen på en tilsynelatende sensurbestandig plattform. Den eneste måten å gjøre denne, riktignok usannsynlige, sensur ikke mulig er hvis gruvearbeidere ikke kan skille mellom transaksjoner fordi alle metadata i kjeden er skjult på forskjellige måter. Noe som Monero er kjent for.

Monero løser dette problemet med transparente adresser ved å implementere stealth-adresser, en teknologi som faktisk opprinnelig ble laget for Bitcoin i 2011 av Bitcoin Talk-forumbrukeren ByteCoin (forholdet til Bytecoin, som senere skulle integrere stealth-adresser, er ukjent). Den nåværende formen for stealth-adresser har imidlertid flere forbedringer i forhold til den opprinnelige ideen. Men først, for å se hvordan de fungerer, la oss snakke om nøkler.

Det er vanskelig å være i kryptovaluta-området og ikke høre om nøkler. Fraser som "sikkerhetskopier din private nøkkel" er vanlige, men når en gjennomsnittlig Joe hører ordene "offentlig nøkkel" og "privat nøkkel" blir de redde og tror det blir for teknisk og forvirrende å forstå. Men ikke bekymre deg. Vi tar det sakte og bruker mange eksempler.

De to typene nøkler som brukes i kryptovalutaer er, som nevnt, offentlige og private. Disse to nøklene kommer vanligvis i et par, noe som betyr at en bestemt offentlig og privat nøkkel er knyttet til hverandre. Faktisk er vanligvis den offentlige nøkkelen avledet fra den private, noe som betyr at hvis du kjenner den private nøkkelen, kan lommeboken din gjøre litt fin matematikk og komme opp med den riktige offentlige nøkkelen hver gang.

Nå, som navnene tilsier, kan den offentlige nøkkelen være offentlig uten konsekvens. Vanligvis er det en del av adressen du deler for å motta penger i kryptovaluta-lommeboken din. Også etter navnebror, er den private nøkkelen en som ikke bør deles. Det er tingen som lar deg signere og bruke en transaksjon, så hvis den blir stjålet eller delt, kan den elendige tredjeparten bruke pengene dine, vanligvis til seg selv.

En enkel analogi til dette ville være en hengelås og nøkkelen som trengs for å låse den opp. Den åpne hengelåsen kan deles fritt, og faktisk kan alt låses med denne hengelåsen, men bare personen med nøkkelen kan åpne alt hengelåsen er lukket på. Hengelåsen kan kopieres og deles, nøkkelen skal ikke være det.

Disse nøklene er vanligvis abstrahert bort fra brukeren, slik at du aldri ser dem. I Monero fremstår de ikke som en skummel alfanumerisk streng i det hele tatt. I Monero kjenner den vanlige brukeren den private nøkkelen som sitt frø. Frøet (som du bør skrive ned hvis du ikke har det), er faktisk bare en personlig lesbar privat nøkkel. 

Ser du? Ikke så skummelt likevel. Tilbake til stealth-adresser.

Som nevnt før, ble ikke stealth-adresser opprinnelig laget for Monero, men Bitcoin. Som med de fleste nye ideer, hadde denne første iterasjonen problemer. Det neste forsøket kom da CryptoNote ble opprettet av Nicholas van Saberhagan for Bytecoin, forløperen til Monero ([se vår historie om Monero og Bytecoin her](/knowledge/monero-history)), og selv om det var en klar forbedring i forhold til originalen, hadde det til og med noen subtile feil.

Til slutt kom en siste iterasjon fra en utvikler for en annen nå nedlagt, privat kryptovaluta, som fikset de utestående personvern- og sikkerhetsproblemene med ideen. Dette kom til slutt inn i Monero, og er det som brukes i dag.

Selv om disse personvern- og sikkerhetsproblemene ble løst, ga stealth-adresser i seg selv en annen type særpreg til blockchain-teknologier, en som ikke eksisterte før. Behovet for å skanne. Siden mottakeradresser ikke vises offentlig på blokkjeden, vet mottakeren aldri om en gitt transaksjon er deres, så de må skanne alle innkommende transaksjoner med deres private nøkkel for å se om den er deres.

Med gjennomsiktighetsmynter trenger de bare å sjekke om en transaksjon sendes til adressen din. Et enkelt ja eller nei spørsmål. Men med stealth-adresser kan hver transaksjon potensielt være en som sendes til deg, så du må prøve å låse opp hver enkelt med din private nøkkel for å se om den åpnes.

Dette er et ekstra trinn som Bitcoin og dens derivater ikke har, og gjør det første oppsett av lommebok, sammen med synkronisering av en lommebok når du ikke har åpnet den på en stund, mye lenger enn Bitcoin. Avveiningen er imidlertid nødvendig for å låse opp personverngarantiene den har. Det skal bemerkes at, i motsetning til det svakeste punktet i personverntrifectaen, er ringsignaturer, stealth-adresser ikke utsatt for heuristikk. Den er avhengig av utprøvd og ekte elliptisk kurvekryptografi, som hele internett er avhengig av, så å bryte den vil bety en slutt på datasikkerhet generelt, ikke bare Monero.

På en gjennomsiktig blokkjede er adressene man sender transaksjonene sine til, synlige for alle. Det er viktig å tenke på at hvis gruvearbeidere selv er uenige i hvor pengene går, kan de velge å ikke gruve dem inn i en blokk, og effektivt sensurere denne transaksjonen på en tilsynelatende sensurbestandig plattform. Den eneste måten å gjøre denne, riktignok usannsynlige, sensur ikke mulig er hvis gruvearbeidere ikke kan skille mellom transaksjoner fordi alle metadata i kjeden er skjult på forskjellige måter. Noe som Monero er kjent for.

Monero løser dette problemet med transparente adresser ved å implementere stealth-adresser, en teknologi som faktisk opprinnelig ble laget for Bitcoin i 2011 av Bitcoin Talk-forumbrukeren ByteCoin (forholdet til Bytecoin, som senere skulle integrere stealth-adresser, er ukjent). Den nåværende formen for stealth-adresser har imidlertid flere forbedringer i forhold til den opprinnelige ideen. Men først, for å se hvordan de fungerer, la oss snakke om nøkler.

Det er vanskelig å være i kryptovaluta-området og ikke høre om nøkler. Fraser som "sikkerhetskopier din private nøkkel" er vanlige, men når en gjennomsnittlig Joe hører ordene "offentlig nøkkel" og "privat nøkkel" blir de redde og tror det blir for teknisk og forvirrende å forstå. Men ikke bekymre deg. Vi tar det sakte og bruker mange eksempler.

De to typene nøkler som brukes i kryptovalutaer er, som nevnt, offentlige og private. Disse to nøklene kommer vanligvis i et par, noe som betyr at en bestemt offentlig og privat nøkkel er knyttet til hverandre. Faktisk er vanligvis den offentlige nøkkelen avledet fra den private, noe som betyr at hvis du kjenner den private nøkkelen, kan lommeboken din gjøre litt fin matematikk og komme opp med den riktige offentlige nøkkelen hver gang.

Nå, som navnene tilsier, kan den offentlige nøkkelen være offentlig uten konsekvens. Vanligvis er det en del av adressen du deler for å motta penger i kryptovaluta-lommeboken din. Også etter navnebror, er den private nøkkelen en som ikke bør deles. Det er tingen som lar deg signere og bruke en transaksjon, så hvis den blir stjålet eller delt, kan den elendige tredjeparten bruke pengene dine, vanligvis til seg selv.

En enkel analogi til dette ville være en hengelås og nøkkelen som trengs for å låse den opp. Den åpne hengelåsen kan deles fritt, og faktisk kan alt låses med denne hengelåsen, men bare personen med nøkkelen kan åpne alt hengelåsen er lukket på. Hengelåsen kan kopieres og deles, nøkkelen skal ikke være det.

Disse nøklene er vanligvis abstrahert bort fra brukeren, slik at du aldri ser dem. I Monero fremstår de ikke som en skummel alfanumerisk streng i det hele tatt. I Monero kjenner den vanlige brukeren den private nøkkelen som sitt frø. Frøet (som du bør skrive ned hvis du ikke har det), er faktisk bare en personlig lesbar privat nøkkel. 

Ser du? Ikke så skummelt likevel. Tilbake til stealth-adresser.

Som nevnt før, ble ikke stealth-adresser opprinnelig laget for Monero, men Bitcoin. Som med de fleste nye ideer, hadde denne første iterasjonen problemer. Det neste forsøket kom da CryptoNote ble opprettet av Nicholas van Saberhagan for Bytecoin, forløperen til Monero ([se vår historie om Monero og Bytecoin her](/knowledge/monero-history)), og selv om det var en klar forbedring i forhold til originalen, hadde det til og med noen subtile feil.

Til slutt kom en siste iterasjon fra en utvikler for en annen nå nedlagt, privat kryptovaluta, som fikset de utestående personvern- og sikkerhetsproblemene med ideen. Dette kom til slutt inn i Monero, og er det som brukes i dag.

Selv om disse personvern- og sikkerhetsproblemene ble løst, ga stealth-adresser i seg selv en annen type særpreg til blockchain-teknologier, en som ikke eksisterte før. Behovet for å skanne. Siden mottakeradresser ikke vises offentlig på blokkjeden, vet mottakeren aldri om en gitt transaksjon er deres, så de må skanne alle innkommende transaksjoner med deres private nøkkel for å se om den er deres.

Med gjennomsiktighetsmynter trenger de bare å sjekke om en transaksjon sendes til adressen din. Et enkelt ja eller nei spørsmål. Men med stealth-adresser kan hver transaksjon potensielt være en som sendes til deg, så du må prøve å låse opp hver enkelt med din private nøkkel for å se om den åpnes.

Dette er et ekstra trinn som Bitcoin og dens derivater ikke har, og gjør det første oppsett av lommebok, sammen med synkronisering av en lommebok når du ikke har åpnet den på en stund, mye lenger enn Bitcoin. Avveiningen er imidlertid nødvendig for å låse opp personverngarantiene den har. Det skal bemerkes at, i motsetning til det svakeste punktet i personverntrifectaen, er ringsignaturer, stealth-adresser ikke utsatt for heuristikk. Den er avhengig av utprøvd og ekte elliptisk kurvekryptografi, som hele internett er avhengig av, så å bryte den vil bety en slutt på datasikkerhet generelt, ikke bare Monero.

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

  * [Hvordan Monero-underadresser forhindrer identitetskobling](/knowledge/monero-subaddresses/)

  * [Monero-utganger forklart](/knowledge/monero-outputs/)

  * [Monero beste praksis for nybegynnere](/knowledge/monero-best-practices/)

  * [Hvordan ringsignaturer obskure Moneros utganger](/knowledge/ring-signatures/)

  * [Hvordan Monero løste blokkstørrelsesproblemet som plager Bitcoin](/knowledge/dynamic-block-size/)

  * [Hvordan CLSAG vil forbedre Moneros effektivitet](/knowledge/what-is-clsag/)

  * [Hvorfor Monero har en haleutslipp](/knowledge/monero-tail-emission/)

  * [En kort historie om Monero](/knowledge/monero-history/)

  * [Wired Magazine tar feil om Monero, her er hvorfor](/knowledge/wired-article-debunked/)

  * [Topp 15 Monero-myter og bekymringer avslørt](/knowledge/monero-myths-debunked/)

  * [Hvordan Dandelion++ holder Moneros transaksjonsopprinnelse privat](/knowledge/monero-dandelion/)

  * [Hvorfor Monero er åpen kildekode og desentralisert](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Hva gjør RandomX så spesiell](/knowledge/monero-mining-randomx/)

  * [Hvorfor Monero er bedre enn Dash, Zcash, Zcoin (selv med Lelantus), Grin og Bitcoin-miksere som Wasabi (Oppdatert mai 2020)](/knowledge/why-monero-is-better/)