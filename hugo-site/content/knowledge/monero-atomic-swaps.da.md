---
title: "Hvordan Atomic Swaps Vil Arbejde i Monero"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
I jagten på decentralisering og et virkelig tilladelsesfrit system er få ting så eftertragtede i kryptovalutaområdet som decentraliserede udvekslinger og atomare swaps. Siden starten har Monero kæmpet med at implementere atomare swaps, da privatlivsfunktionerne skaber unikke problemer, når man forsøger at designe en protokol.

Men først, lad os tage backup. Hvad er atomswaps? En atomswap er en protokol, hvormed to forskellige kryptovalutaer, på forskellige blockchains, kan udveksles på en tillidsfri måde uden mellemled. Det betyder, at hvis nogen ønskede at udveksle kryptovaluta A med kryptovaluta B, ville de være i stand til at gøre det uden en centraliseret eller decentraliseret udveksling. Som man kunne forestille sig, kræver dette betydelig research, og de fulde tekniske detaljer, der gør det muligt, bliver ret kompliceret. Endnu en gang er LocalMonero her for at hjælpe og give en enkel forklaring til den almindelige person.

For at starte, lad os overveje den enkleste form for atomswap, som implementeret af Bitcoin. Hvis nogen ønsker at bytte Bitcoin til en anden mønt, der bruger den samme hash time lock kontrakt teknologi, kan de gøre det på følgende måde. Alice har Bitcoin (BTC), men vil have Litecoin (LTC), og Bob har LTC, men vil have BTC. De beslutter sig for at lave et atombytte, så hver enkelt får den mønt, de ønsker. Alice sender sin BTC til en speciel adresse ved at bruge scripts, der låser pengene væk, så selv hun ikke kan få adgang til det. Du kan tænke på det, som om Alice lægger sin BTC i en låseboks. Når låseboksen er lavet, får hun en nøgle og sender en hash af denne nøgle til Bob. Nu har Bob ikke selve nøglen, kun hashen, så han har endnu ikke adgang til pengene.

Bob bruger denne hash som en seed, hvorfra han genererer sin egen lockbox, og sender sin LTC dertil, hvor den også låses. Da hashen af Alices nøgle blev brugt som seed til at lave Bobs lockbox, kan hun bruge sin nøgle til at gøre krav på LTC'en i Bobs lockbox. Hendes nøgle passer! Men ved hjælp af matematisk voodoo-magi, når hun bruger sin nøgle til at åbne LTC-låsen, afslører hun nøglen for Bob, som derefter kan bruge den til at gøre krav på de BTC, som hun lagde i sin boks. På denne måde har Alice og Bob udvekslet deres aktiver uden mellemled.

Men der er et lille problem. Hvad hvis Alice sender til sin låseboks, og Bob beslutter sig for, at han ikke vil bytte mere. Nu, da Alice ikke kan få adgang til sin BTC, som hun låste væk, og Bob ikke vil fuldføre sin del af transaktionen, mister Alice bare sine penge for altid. Nå, heldigvis har Bitcoin en lille teknologi kaldet refusionstransaktioner, og så efter en periode, hvis BTC'en ikke gøres krav på af Bob, har scripts en fejlsikker indbygget, hvor BTC'en automatisk vil gå tilbage til Alice. Dette var det primære fartbump for Moneros implementering af atomswaps. På grund af Moneros [ringsignaturbeskyttelsesteknologi](/knowledge/ring-signatures) er afsenderen af en transaktion altid usikker. Hvordan kan protokollen foretage en refusionstransaktion, hvis selv den ikke ved, hvor transaktionen kom fra?

I 2017 skitserede en lille gruppe forskere en anden metode, hvormed atomare swaps kunne fungere i Monero. Efter flere års finpudsning færdiggjorde forskerne en proces, hvor Monero ville være i stand til at foretage atomare swaps med Bitcoin, selv uden refusions transaktioner.

Som med mange ting af dette niveau af teknisk kompleksitet, vil vores forklaring forenkle nogle ting for at formidle ideen, men den vil stadig give en solid idé om de mekanismer, hvormed denne proces ville fungere.

Både Alice (der har XMR og ønsker BTC) og Bob (der har BTC og ønsker XMR) skal downloade og køre et program, der understøtter atomswap. Dette kan implementeres i tegnebøger, decentraliserede børser eller specielle, specifikke programmer, men softwaren skal køre atomswap-protokollen. I det første trin forbinder Alice og Bobs klienter hinanden og laver flere fælles hemmeligheder og nøgler. I dette trin oprettes en ny Monero-adresse, hvor Alice har den ene halvdel af nøglen, og Bob har den anden. Der er dog ingen Monero derinde endnu, så der er ikke noget at bruge. En sidste ting at bemærke ved denne adresse er, at de begge har nøglen til denne pung, så de begge kan kigge ind for at se, om eller hvornår Monero ankommer.

I det andet trin sender Bob sin BTC til en speciel adresse, der ligner Bitcoin atomic swap-protokollen, vi allerede har diskuteret. Efter at Alice ser BTC ankomme til denne adresse på blockchain, sender hun sin Monero til Monero-adressen, som hun og Bob begge har den ene halvdel af en nøgle til. Bob kan bekræfte, at Moneroen ankom, da han også har visningsnøglen, og når han ser, at Moneroen er sikkert i tegnebogen, sender han Alice et stykke af en nøgle, der vil give hende mulighed for at hæve Bitcoinen. I lighed med den anden protokol afslører processen med at gøre krav på Bitcoinen hendes halvdel af Monero-nøglen til Bob. Nu har Bob begge halvdele, så han kan gøre krav på Monero, mens Alice kun har sin halvdel, så hun kan ikke prøve at tage den, før han gør.

Så hvis du kiggede på alt dette og stadig er en smule forvirret over, hvordan Monero var i stand til at omgå problemet med refusionstransaktioner, er svaret ret enkelt. Da Monero ikke selv har refusionstransaktioner, bør læseren bemærke, at Bitcoin (som har refusionstransaktioner) sendes først, og først efter at den er verificeret som værende på blockchain, sendes Monero. Dette gør det muligt for Monero at bruge Bitcoins evne til at scripte i refusionstransaktioner og drage fordel af dem uden selv at skulle have disse muligheder.

Atombyttet er nu afsluttet, men herfra har Bob et par muligheder for sin nyligt påberåbte XMR. Han kan bruge denne Monero-pung, som den er, eller flytte XMR til en anden pung, som han allerede ejer. Bob vil højst sandsynligt flytte Monero'en til en anden tegnebog, fordi Alice stadig har visningsnøglen og kan se indeni.

Det smukke ved denne protokol er, at den stadig er ret ny, og der er masser af plads til optimeringer. Den er også ret fleksibel i sin arkitektur, så implementering i andre tegnebøger eller decentraliserede børser bør være enkel og passe perfekt til deres eksisterende arkitektur.

Yderligere læsning

  * [Hvordan Monero unikt aktiverer cirkulær økonomier](/knowledge/monero-circular-economies)/

  * [Monero's ring signaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Hvorfor (og hvordan!) skal du holde dine egne nøgler](/knowledge/hold-your-keys)/

  * [Bidrager tilbage til Monero](/knowledge/contributing-to-monero)/

  * [Hvordan fjern noder påvirker Monero's privatliv](/knowledge/remote-nodes-privacy)/

  * [Hvordan Monero bruger hard-forks til at opgradere den netværk](/knowledge/network-upgrades)/

  * [Se tags: Hvordan en byte vil reducere Monero wallet-synkroniseringstider med 40 %+](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool og Dets rolle i Decentralisering Monero Minedrift](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Hvad Det Vil Gør for Monero](/knowledge/seraphis-for-monero)/

  * [Er konvertering af Bitcoin til Monero lige så privat som at købe Monero direkte?](/knowledge/most-private-way-to-buy-monero)/

  * [Hvorfor Monero Brug en Tillidsløs Opsætning i modsætning til Zcash](/knowledge/monero-trustless-setup)/

  * [Hvorfor Monero er en bedre butik af værdi end Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Hvordan Monero Kan Overvinde Bitcoin's Netværk Effekter](/knowledge/network-effect)/

  * [Hvorfor Monero Har Det Mest Kritiske Tænkning Fællesskab](/knowledge/critical-thinking)/

  * [Svindel til Se Ud for Når Bruger Monero](/knowledge/monero-scams)/

  * [Hvad enhver Monero-bruger har brug for at vide, når det kommer til netværk](/knowledge/monero-networking)/

  * [Hvordan RingCT Huder Monero Transaktion Beløb](/knowledge/monero-ringct)/

  * [Hvordan Monero Stealth Adresser Beskyt Din Identitet](/knowledge/monero-stealth-addresses)/

  * [Hvordan Monero Underadresser Forebyg Identitet Linking](/knowledge/monero-subaddresses)/

  * [Monero Outputs Forklaret](/knowledge/monero-outputs)/

  * [Monero Bedste Praksis for Begyndere](/knowledge/monero-best-practices)/

  * [Hvordan Ring Signaturer Obskure Monero's Outputs](/knowledge/ring-signatures)/

  * [Hvordan Monero løste blokstørrelsesproblemet, der plager Bitcoin](/knowledge/dynamic-block-size)/

  * [Hvordan CLSAG Vilje Forbedre Monero's Effektivitet](/knowledge/what-is-clsag)/

  * [Hvorfor Monero Har en Hale Emission](/knowledge/monero-tail-emission)/

  * [En kort historie om Monero](/knowledge/monero-history)/

  * [Wired Magazine er Forkert Om Monero, Her er Hvorfor](/knowledge/wired-article-debunked)/

  * [Top 15 Monero Myter og Bekymringer Afkræftet](/knowledge/monero-myths-debunked)/

  * [Hvordan Dandelion++ Holder Monero's Transaktion Oprindelse Privat](/knowledge/monero-dandelion)/

  * [Hvorfor Monero Er Open Source Og Decentraliseret](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: Hvad Gør RandomX så Speciel](/knowledge/monero-mining-randomx)/

  * [Hvorfor Monero er bedre end Dash, Zcash, Zcoin (selv med Lelantus), Grin og Bitcoin-mixere som Wasabi (Opdateret maj 2020)](/knowledge/why-monero-is-better)/

Yderligere læsning