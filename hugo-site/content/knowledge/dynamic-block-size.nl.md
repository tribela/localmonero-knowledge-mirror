---
title: "Hoe Monero het Probleem met de Blokgrootte Dat Bitcoin Plaagt Heeft Opgelost"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Opmerking:** Het wordt ten zeerste aanbevolen dat de lezer de volgende artikelen leest ["Waarom Monero Een 'Tail Emission' Heeft"](/knowledge/monero-tail-emission) en [“Monero Mining: Wat RandomX zo Speciaal Maakt”](/knowledge/monero-mining-randomx). Dit artikel bouwt voort op de concepten die daarin worden gepresenteerd._

Telkens wanneer individuelen de problemen met blockchain bespreken, is 'scaling' een van de eerste woorden die opduikt. Het is geen geheim dat blockchains niet goed 'scalen', maar de meeste mensen weten niet waarom.

De waarheid is dat scaling eigenlijk een overkoepelende term is die twee verschillende categorieën omvat: protocolondersteuning en technologische ondersteuning op een gegeven moment. In dit artikel gaan we onze aandacht richten op één: protocolondersteuning is in feite een maat voor het aantal transacties dat het protocol op een bepaald moment aankan. 

Bitcoin heeft een limiet voor de blokgrootte, wat betekent dat zodra er voldoende transacties in een blok zijn opgenomen, eventuele extra transacties in de rij moeten wachten op het volgende blok. Een nuttige analogie zou zijn om aan een trein te denken. Er stopt een trein op het station, en degenen die in de rij staan, komen binnen. Als de trein eenmaal vol is, moet iedereen die buiten staat wachten op de volgende.

Bitcoin gebruikt vergoedingen om te bepalen wie er in het blok komt of niet. Terugkomend op de treinanalogie, kan men zich voorstellen dat een potentiële passagier, die op het punt staat achter te blijven, de treinmachinist vijf dollar aanbiedt om hem een zitplaats te geven. Andere passagiers volgen, en uiteindelijk is er een biedingsoorlog om te zien wie welke plek krijgt. Het is aan de chauffeur om te beslissen of hij het 'wie het eerst komt, het eerst maalt'-beleid wil honoreren, maar het is in zijn beste financiële belang om zijn inkomen te maximaliseren door de hoogste bieders aan boord te nemen.

In deze analogie zijn 'miners' de treinbestuurders. Ze kunnen elke gewenste transactie in het blok opnemen, maar over het algemeen kiezen ze degene met de best betaalde kosten. 

Als alternatief, als blokken niet erg vol zijn, hebben mensen geen reden om hoge kosten te betalen omdat er voldoende vrije plaatsen over zijn.

Op het hoogtepunt van de cryptocurrency-boom van 2017 werd Bitcoin overspoeld met transacties, en de vergoedingen schoten omhoog voor degenen die wilden worden opgenomen in het volgende blok, of welk blok dan ook in de nabije toekomst. Degenen die niet bereid waren hoge kosten te betalen, zagen hun transacties uren of dagen vertraagd worden, of zelfs helemaal uit de wachtrij vallen.

Dit was een schrijnend inzicht in hoe het met Bitcoin zou gaan als de vaak genoemde 'massa-adoptie' zou plaatsvinden. Als Bitcoin door de massa zou worden gebruikt, zou het nog erger zijn dan in 2017, en zou Bitcoin voor niemand toegankelijk zijn behalve voor de rijken, simpelweg omdat de doorvoer klein is vanwege een vaste blokgrootte, waardoor de vergoedingsmarkt het overneemt .

Monero voorzag dit en wilde iets anders doen. Daarom hebben de Monero-ontwikkelaars een dynamische blokgrootte geïmplementeerd.

Kortom, Monero heeft ook een limiet van blokformaat, maar het is een zachte limiet. Wanneer de rij wachtende transacties te lang wordt, kunnen de 'miners' de blokken vergroten. Met onze treinanalogie kunt u uzelf voorstellen dat u meer treinwagons toevoegt om de extra passagiers te passen. Nadat de wachtrij leeg is, krimpen de blokken in de toekomst terug naar hun oorspronkelijke grootte.

Als dit een zo'n goed idee was, is het redelijk om te vragen waarom Monero de enige cryptocurrency is die dit heeft geïmplementeerd. Waarom zou u het niet toevoegen aan Bitcoin om een einde te maken aan de doorvoerproblemen? 

Helaas is dit niet mogelijk. Er zijn verschillende redenen waarom, en we zullen ons best doen om het uit te leggen. 

Het is altijd van belang voor een 'miner' om grote blokken te hebben. Met grote blokken kunnen ze meer transacties passen en meer geld verdienen aan de vergoedingen, evenals aan de blokbeloningen. Dit kan leiden tot spamaanvallen, waarbij iemand veel kleine transacties tegen kleine vergoedingen verzendt om de keten op te blazen. 'Miners' zouden gewoon de blokgrootte verhogen, en ze allemaal includeren, omdat geld geld is, hoe klein het bedrag dan ook. Dit zou leiden tot consistent grote blokken met weinig economisch voordeel. Bitcoin lost dit op door de blokgrootte kunstmatig te beperken en zo een vergoedingsmarkt te genereren. Spamaanvallers zouden de andere gebruikers moeten betalen, en dit is niet meer goedkoop. Maar dit betekent wel dat blokken eventueel vol raken, waardoor sommige transacties moeten wachten, zoals hierboven vermeld. 

Dus hoe kan Monero dynamische blokgroottes hebben, maar spamaanvallen vermijden? Het antwoord is simpel, maar slim. Een straf op de blokbeloning wordt geïntroduceerd wanneer een blok groter is dan normaal. Als een 'miner' de blokgrootte wil vergroten, zal de beloning die ze krijgen voor het vinden van dat blok lager zijn dan ze anders zouden ontvangen. Ze zullen de blokgrootte dus alleen vergroten wanneer de betaalde transactiekosten van de gebruikers opwegen tegen het verloren deel van de blokbeloning. Als de 'miner' bijvoorbeeld 0,5 XMR zou verliezen door de blokbeloning te verhogen, en de som van de betaalde transactiekosten zou 0,4 XMR zijn, dan zou er een nettoverlies zijn van 0,1 XMR als ze de grootte zouden verhogen, dus ze doen het niet. Omgekeerd, als de totale transactiekosten optellen tot 0,7 XMR, dan zou er een nettowinst zijn van 0,2 XMR, ook al verliezen ze de 0,5 XMR van de blokbeloningsboete, dus de 'miner' zal de blok groter maken.

Deze dynamische blokken zorgen ervoor dat het netwerk organisch kan groeien, zonder de blokken artificieel te beperken om een geforceerde vergoedingsmarkt te creëren, terwijl spamaanvallen worden vermeden. Er zijn nog meer invalshoeken van waaruit we dit idee kunnen bekijken, en meer redenen waarom het niet mogelijk zou zijn om iets toe te voegen aan Bitcoin, maar voor nu hopen we dat de lezer begrijpt hoe Monero verschillende problemen in Bitcoin omzeilt en zijn afgeleiden, en hoe het van plan is hun doorvoer naar de toekomst te 'scalen'. 

Verder lezen

  * [Hoe Monero op unieke wijze circulaire economieën mogelijk maakt](/knowledge/monero-circular-economies)/

  * [Monero's ringhandtekeningen versus CoinJoin zoals in Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Waarom (en hoe!) u uw eigen sleutels moet bezitten](/knowledge/hold-your-keys)/

  * [Bijdragen aan Monero](/knowledge/contributing-to-monero)/

  * [Hoe externe knooppunten de privacy van Monero beïnvloeden](/knowledge/remote-nodes-privacy)/

  * [Hoe Monero hard forks gebruikt om het netwerk te upgraden](/knowledge/network-upgrades)/

  * [Weergave tags: Hoe één byte de synchronisatietijden van de Monero portefeuille met meer dan 40% vermindert](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool en Zijn Rol bij het Decentraliseren van Monero Mining](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Wat Het Zal Doen voor Monero](/knowledge/seraphis-for-monero)/

  * [Is het Omzetten van Bitcoin naar Monero Net Zo Privé als het Rechtstreeks Kopen van Monero?](/knowledge/most-private-way-to-buy-monero)/

  * [Waarom Monero een Trustless Setup Gebruikt in Tegenstelling tot Zcash](/knowledge/monero-trustless-setup)/

  * [Waarom Monero een Betere Waardeopslag Is Dan Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Hoe Monero de Netwerkeffecten van Bitcoin Kan Overwinnen](/knowledge/network-effect)/

  * [Waarom Monero de Meest Kritische Denkgemeenschap Heeft](/knowledge/critical-thinking)/

  * [Oplichtingen Om Voor Uit Te Kijken Bij Gebruik van Monero](/knowledge/monero-scams)/

  * [Hoe Atomic Swaps Zullen Werken in Monero](/knowledge/monero-atomic-swaps)/

  * [Wat Elke Monero Gebruiker Moet Weten Als het om Netwerken Gaat](/knowledge/monero-networking)/

  * [Hoe RingCT Monero's Transactiebedragen verbergt](/knowledge/monero-ringct)/

  * [Hoe Monero Stealth Adressen Uw Identiteit Beschermen](/knowledge/monero-stealth-addresses)/

  * [Hoe Monero's Subadressen Identiteitskoppeling Voorkomen](/knowledge/monero-subaddresses)/

  * [Monero-Outputs uitgelegd](/knowledge/monero-outputs)/

  * [Praktische Tips van Monero voor Beginners](/knowledge/monero-best-practices)/

  * [Hoe Ring-handtekeningen de Resultaten van Monero Verdoezelen](/knowledge/ring-signatures)/

  * [Hoe CLSAG de Efficiëntie van Monero Zal Verbeteren](/knowledge/what-is-clsag)/

  * [Waarom Monero een Staartemissie Heeft](/knowledge/monero-tail-emission)/

  * [Een Korte Geschiedenis van Monero](/knowledge/monero-history)/

  * [Wired Magazine heeft Ongelijk over Monero, Dit is Waarom](/knowledge/wired-article-debunked)/

  * [Top 15 Monero Mythen en Zorgen Ontkracht](/knowledge/monero-myths-debunked)/

  * [Hoe Dandelion++ de Oorsprong van de Transacties van Monero Privé Houdt](/knowledge/monero-dandelion)/

  * [Waarom Monero Open Source en Dedecentraliseerd Is](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero-Mining: Wat RandomX zo Speciaal Maakt](/knowledge/monero-mining-randomx)/

  * [Waarom Monero beter is dan Dash, Zcash, Zcoin (zelfs met Lelantus), Grin en Bitcoin Mixers zoals Wasabi (bijgewerkt mei 2020)](/knowledge/why-monero-is-better)/

Verder lezen