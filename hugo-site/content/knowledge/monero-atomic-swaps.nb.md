---
title: "Hvordan Atomic Swaps vil fungere i Monero"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
I jakten på desentralisering og et virkelig tillatelsesløst system er det få ting som er så ettertraktet i kryptovaluta-området som desentraliserte børser og atombytter. Siden starten har Monero slitt med å implementere atombytte, ettersom personvernfunksjonene skaper unike problemer når de prøver å designe en protokoll.

Men først, la oss sikkerhetskopiere. Hva er atombytter? En atombytte er en protokoll der to forskjellige kryptovalutaer, på forskjellige blokkkjeder, kan utveksles på en tillitsløs måte uten mellomledd. Dette betyr at hvis noen ønsket å bytte kryptovaluta A mot kryptovaluta B, ville de kunne gjøre det uten en sentralisert eller desentralisert utveksling. Som man kan forestille seg, krever dette betydelig forskning, og de fulle tekniske detaljene som gjør det mulig blir ganske komplisert. Nok en gang er LocalMonero her for å hjelpe og gi en enkel forklaring for den vanlige personen.

For å starte, la oss vurdere den enkleste formen for atombytte, som implementert av Bitcoin. Hvis noen ønsker å bytte Bitcoin mot en annen mynt som bruker samme hash time lock kontrakt teknologi, kan de gjøre det på følgende måte. Alice har Bitcoin (BTC), men vil ha Litecoin (LTC), og Bob har LTC, men vil ha BTC. De bestemmer seg for å gjøre et atombytte slik at hver enkelt får den mynten de vil ha. Alice sender BTC-en sin til en spesiell adresse, ved å bruke skript som låser pengene slik at selv hun ikke får tilgang til den. Du kan tenke på det som at Alice legger BTC-en sin i en låseboks. Når låseboksen er laget, får hun en nøkkel, og sender en hash av denne nøkkelen til Bob. Nå har ikke Bob selve nøkkelen, bare hashen, så han har ikke tilgang til pengene ennå.

Bob bruker denne hashen som et frø som han genererer sin egen låseboks fra, og sender sin LTC dit, hvor den også er låst. Siden hashen til Alices nøkkel ble brukt som frøet som Bobs låseboks ble laget av, kan hun bruke nøkkelen sin til å kreve LTC i Bobs låseboks. Nøkkelen hennes passer! Men ved å bruke matematisk voodoo-magi, når hun bruker nøkkelen sin til å åpne LTC-låsen, avslører hun nøkkelen til Bob, som deretter kan bruke den til å kreve BTC-en hun la i låseboksen. På denne måten, uten mellomledd, har Alice og Bob lykkes med å bytte ut sine eiendeler.

Men det er et lite problem. Hva om Alice sender til låseboksen hennes, og Bob bestemmer seg for at han ikke vil bytte mer. Nå, siden Alice ikke har tilgang til BTC-en sin som hun låste, og Bob ikke vil fullføre sin del av transaksjonen, mister Alice bare pengene sine for alltid. Vel, heldigvis har Bitcoin en liten teknologi som kalles refusjonstransaksjoner, og så etter en periode, hvis BTC ikke er gjort krav på av Bob, har skriptene en feilsikker innebygd, hvor BTC automatisk vil gå tilbake til Alice. Dette var den primære fartshumpen for Moneros atombytteimplementering. På grunn av Moneros [ringsignaturer personvernteknologi](/knowledge/ring-signatures), er avsenderen av en transaksjon alltid usikker. Hvordan kan protokollen utføre en refusjonstransaksjon hvis den ikke vet hvor transaksjonen kom fra?

I 2017 skisserte en liten gruppe forskere en annen metode for atombytte i Monero. Etter flere år med foredling, fullførte forskerne en prosess der Monero ville være i stand til å gjøre atombytte med Bitcoin, selv uten refusjonstransaksjoner.

Som med mange ting av dette nivået av teknisk kompleksitet, vil forklaringen vår forenkle noen ting for å formidle ideen, men den vil fortsatt gi en solid idé om mekanismene som denne prosessen vil fungere med.

Både Alice (som har XMR og vil ha BTC) og Bob (som har BTC og vil ha XMR) må laste ned og kjøre et program som støtter atombytte. Dette kan implementeres i lommebøker, desentraliserte børser eller spesielle, spesifikke programmer, men programvaren må kjøre atombytteprotokollen. I det første trinnet kobler Alice og Bobs klienter seg til hverandre og lager flere felles hemmeligheter og nøkler. I dette trinnet opprettes en ny Monero-adresse, der Alice har den ene halvdelen av nøkkelen, og Bob har den andre. Ingen Monero er der ennå, så det er ingenting å bruke. En siste ting å merke seg om denne adressen, er at de begge har visningsnøkkelen til denne lommeboken, slik at de begge kan titte inn for å se om eller når Monero kommer.

I det andre trinnet sender Bob sin BTC til en spesiell adresse, som ligner på Bitcoin atomic swap-protokollen vi allerede har diskutert. Etter at Alice ser at BTC kommer til denne adressen på blokkjeden, sender hun Moneroen sin til Monero-adressen som hun og Bob begge har en halvdel av nøkkelen til. Bob kan bekrefte at Moneroen ankom siden han også har visningsnøkkelen, og når han ser at Moneroen er trygt i lommeboken, sender han Alice en del av en nøkkel som lar henne ta ut Bitcoinen. I likhet med den andre protokollen avslører prosessen med å kreve Bitcoinen hennes halvparten av Monero-nøkkelen til Bob. Nå har Bob begge halvdelene, så han kan kreve Monero, mens Alice bare har halvparten sin, så hun kan ikke prøve å ta den før han gjør det.

Så hvis du så på alt dette og fortsatt er litt forvirret over hvordan Monero klarte å omgå problemet med refusjonstransaksjoner, er svaret ganske enkelt. Siden Monero selv ikke har refusjonstransaksjoner, bør leseren legge merke til at Bitcoin (som har refusjonstransaksjoner) sendes først, og først etter at det er bekreftet at det er på blokkjeden, sendes Monero. Dette gjør at Monero kan bruke Bitcoins evne til å skripte i refusjonstransaksjoner og dra nytte av dem, uten å måtte ha disse egenskapene selv.

Atombyttet er nå fullført, men herfra har Bob et par alternativer for sin nylig påberopte XMR. Han kan bruke denne Monero-lommeboken som den er, eller flytte XMR-en til en annen lommebok som han allerede eier. Bob vil mest sannsynlig flytte Monero til en annen lommebok, fordi Alice fortsatt har visningsnøkkelen og kan se innsiden.

Det fine med denne protokollen er at den fortsatt er ganske ny, og det er god plass for optimaliseringer. Den er også ganske fleksibel i sin arkitektur, så implementering i andre lommebøker eller desentraliserte børser bør være enkel og passe rent med deres eksisterende arkitektur.

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

  * [Hva enhver Monero-bruker trenger å vite når det kommer til nettverk](/knowledge/monero-networking/)

  * [Hvordan RingCT skjuler Monero-transaksjonsbeløp](/knowledge/monero-ringct/)

  * [Hvordan Monero Stealth-adresser beskytter identiteten din](/knowledge/monero-stealth-addresses/)

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