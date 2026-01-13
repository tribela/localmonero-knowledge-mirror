---
title: "Hoe externe knooppunten de privacy van Monero beïnvloeden"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Een van de grootste voordelen die Monero heeft ten opzichte van andere cryptocurrencies, is de on-chain privacy, maar heeft u zich ooit afgevraagd hoe de privacy van Monero standhoudt wanneer u een extern knooppunt gebruikt? Hoe zit het als u een "light wallet"-server zoals MyMonero gebruikt?

In dit bericht gaan we dieper in op enkele details achter hoe Monero uitzonderlijke on-chain privacy biedt, zelfs bij gebruik van een extern knooppunt, en waar u op moet letten bij het gebruik van externe knooppunten.

## Welke functie hebben knooppunten in Monero?

## Welke functie hebben knooppunten in Monero?

Voor degenen die minder bekend zijn met hoe Monero werkt: de knooppunten (of servers) in het Monero-netwerk kunnen door iedereen worden beheerd en kan de eigenaar van het knooppunt toestaan - of anderen waarmee ze het willen delen! – om een kopie van de blockchain te synchroniseren en deze aan anderen op het netwerk te verstrekken. Deze knooppunten verifiëren ook alle transacties die op het netwerk plaatsvinden, evenals alle blokken die worden gepubliceerd, en zorgen ervoor dat ze allemaal de regels volgen zoals vastgesteld door consensus.

De andere functie die knooppunten in Monero hebben, is een manier om alle gegevens te verstrekken die uw favoriete Monero-portefeuille nodig heeft om correct te controleren op transacties die van u zijn en om nieuwe transacties te doen. Deze gegevens worden op twee manieren door knooppunten geleverd: 

  * De gegevens van elk blok op de blockchain worden door de portefeuille opgevraagd, gescand op transacties die van u zijn en vervolgens weggegooid zodra ze door de portefeuille zijn gecontroleerd. 
    * Deze stap wordt binnenkort drastisch verbeterd, dankzij [weergave tags](/knowledge/view-tags-reduce-monero-sync-time).
  * Bij het verzenden van transacties biedt het knooppunt dat u gebruikt een lijst met mogelijke lokvogels (of nepinvoer) die u kunt gebruiken bij het bouwen van de transactie, zodat u een goede menigte hebt om u in te verstoppen elke keer dat u Monero uitgeeft. 
    * Deze lokvogels maken deel uit van [ringhandtekeningen](/knowledge/ring-signatures), een belangrijk onderdeel van Monero's benadering van privacy on-chain.

  * Deze stap wordt binnenkort drastisch verbeterd, dankzij [weergave tags](/knowledge/view-tags-reduce-monero-sync-time).

  * Deze lokvogels maken deel uit van [ringhandtekeningen](/knowledge/ring-signatures), een belangrijk onderdeel van Monero's benadering van privacy on-chain.

## Wat is de meest privé en veilige manier om Monero te gebruiken?

## Wat is de meest privé en veilige manier om Monero te gebruiken?

Het beste wat u kunt doen, zelfs met de sterke on-chain privacy die door Monero wordt geboden bij het gebruik van externe knooppunten, is uw eigen Monero-knooppunt te gebruiken om ervoor te zorgen dat u een ongerepte kopie van de Monero-blockchain bij de hand hebt en dat uw IP-adres goed wordt beschermd. Het andere voordeel bij het runnen van uw eigen knooppunt is dat u kunt bijdragen aan het netwerk, andere knooppunten kunt laten synchroniseren vanaf uw knooppunt of zelfs andere gebruikers met hun portefeuille verbinding kunnen laten maken met uw knooppunt.

Dat gezegd hebbende, biedt Monero nog steeds uitstekende privacy bij gebruik van een extern knooppunt. Als u geïnteresseerd bent in het runnen van uw eigen Monero knooppunt, is hier een eenvoudig te volgen gids om dit te doen:

  * [Een Monero-knooppunt uitvoeren](https://sethforprivacy.com/guides/run-a-monero-node/)

## Wat kan een extern knooppunt over mij te weten komen?

## Wat kan een extern knooppunt over mij te weten komen?

Bij gebruik van een extern knooppunt zijn er enkele belangrijke stukken informatie die worden blootgesteld aan een extern knooppunt en een aantal belangrijke manieren waarop het knooppunt u kan aanvallen, kan voorkomen dat u transacties uitvoert en meer.

Het eerste dat een extern knooppunt over u te weten kan komen, is uw openbare IP-adres. Hoewel dit hopelijk wordt verborgen via een VPN of Tor, kan het externe knooppunt uw openbare IP-adres aan de transactie koppelen, waardoor ze kunnen achterhalen waar u vandaan komt. Het externe knooppunt kan ook het laatste blok leren dat uw portefeuille heeft gesynchroniseerd en dit gebruiken om gefundeerde gissingen over u te maken, bijvoorbeeld wanneer u normaal gesproken Monero gebruikt en wanneer u voor het laatst Monero heeft uitgegeven. Dit is vooral het geval als u altijd vanaf hetzelfde IP-adres komt (zoals uw huis). Het laatste belangrijke dat een extern knooppunt over u kan leren, is basisinformatie over de transacties die u er doorheen verzendt. Hoewel dit de meest voor de hand liggende gegevens zijn die de extern knooppunt-operator over u krijgt, is het belangrijk om te begrijpen dat dit kan worden gebruikt om de afzender van de transactie op te sporen bij het combineren van die informatie met andere off-chain-gegevens. Dit kan met name gevaarlijk zijn als het externe knooppunt wordt beheerd door een kwaadwillende entiteit, een blockchain-analysebedrijf of een onderdrukkende natiestaat.

Een extern knooppunt kan ook proberen u problemen te bezorgen door blokken voor u te verbergen, waardoor uw portefeuille denkt dat het is gesynchroniseerd terwijl dit niet het geval is. Dit kan u laten denken dat er geld verloren is of u ervan weerhouden geld uit te geven totdat u verbinding maakt met een ander knooppunt. Het laatste belangrijke dat een extern knooppunt kan doen, is uw portefeuille een gemanipuleerde lijst met lokvogels geven. Dit kan ertoe leiden dat uw portefeuille ofwel volledig faalt om transacties op te bouwen (waardoor u geen geld kunt uitgeven), of dat het externe knooppunt kan proberen lokvogels aan te bieden waarvan het weet dat ze zijn uitgegeven om de anonimiteit die u bij elke transactie ontvangt te verminderen. 

## Welke privacygaranties zijn er nog bij het gebruik van een extern knooppunt?

## Welke privacygaranties zijn er nog bij het gebruik van een extern knooppunt?

Hoewel dit artikel u misschien een beetje heeft laten schrikken, is het belangrijk om te beseffen dat de privacy die door Monero wordt geboden uitstekend is, zelfs bij gebruik van een extern knooppunt, en elke andere cryptocurrency ver overtreft wanneer het op deze manier wordt gebruikt. U krijgt nog steeds de sterke on-chain privacy die door Monero wordt geboden, omdat het externe knooppunt nooit de echte input weet (welke munten u uitgeeft), het bedrag aan Monero dat aan de transactie is uitgegeven of het adres van de ontvanger van de transactie. Externe waarnemers kunnen ook de werkelijke input, hoeveelheid of adressen niet zien (ongeacht het type knooppunt dat u kiest om te gebruiken!), wat ervoor zorgt dat zelfs buiten het externe knooppunt uw IP-adres, portefeuille-synchronisatie-informatie en transacties sterke privacygaranties hebben .

Het externe knooppunt heeft ook nooit toegang tot de eerdere transacties die u heeft verzonden of ontvangen, of de hoeveelheid Monero die momenteel in uw portefeuille zit, en verliest alle zichtbaarheid in uw transacties op het moment dat u een ander knooppunt gaat gebruiken. Er worden nooit privésleutels (uitgave- of weergavesleutels) aan het externe knooppunt verstrekt, en dus blijft uw portefeuille privé, veilig en bruikbaar. Ongeacht het externe knooppunt, loopt u ook nooit het risico Monero te verliezen of ervan beroofd te worden, aangezien het knooppunt het adres van de ontvanger niet kan bewerken, nooit toegang heeft tot de privésleutels van uw portefeuille en uw Monero op geen enkele manier in beslag kan nemen.

## Hoe zit het met "lichte portefeuilles" zoals MyMonero?

## Hoe zit het met "lichte portefeuilles" zoals MyMonero?

Hoewel het onderwerp een beetje buiten het bereik van dit artikel valt, wilde ik het toch hebben over een uniek type portefeuille in Monero: lichte portefeuille ("light wallet"). De naam van het feit dat uw portefeuille (op uw telefoon of computer) geen blockchain-synchronisatie hoeft uit te voeren, waardoor de ervaring sneller en vloeiender wordt.

Voor dit soort portefeuilles is er echter een serieuze privacyafweging: uw portefeuille stuurt de privéweergavesleutel naar de externe server die u gebruikt (zoals de standaard in MyMonero), waardoor de externe server volledig inzicht krijgt in het eventueel ontvangen geld sinds de creatie van uw portefeuille (en verder totdat u stopt met het gebruik van die portefeuille of seed). Dit vermindert de privacy die u ontvangt van de knooppunt-operator drastisch en moet met de nodige voorzichtigheid worden benaderd. 

Gelukkig werkt de Monero-community aan het verbeteren van de software die u kunt gebruiken om uw eigen lichte portefeuille-server (LWS) te hosten, waardoor u snel kunt synchroniseren zonder dat u een derde partij vertrouwt met uw privésleutels - aangezien u de software zult controleren waar uw portefeuille de privé weergavesleutels naartoe stuurt! 

Voor meer informatie over de aangepaste LWS, zie het onderstaande Github-archief:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Hoe kan ik meer leren?

## Hoe kan ik meer leren?

Als je nieuwsgierig bent en knooppunten in Monero beter wilt begrijpen, wilt kijken of u een knooppunt op afstand kunt gebruiken of uw eigen knooppunt wilt kunnen gebruiken, bekijk dan de onderstaande links voor goede plekken om van start te gaan:

Verder lezen

  * [Hoe Monero op unieke wijze circulaire economieën mogelijk maakt](/knowledge/monero-circular-economies)/

  * [Monero's ringhandtekeningen versus CoinJoin zoals in Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Waarom (en hoe!) u uw eigen sleutels moet bezitten](/knowledge/hold-your-keys)/

  * [Bijdragen aan Monero](/knowledge/contributing-to-monero)/

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

  * [Hoe Monero het Probleem met de Blokgrootte Dat Bitcoin Plaagt Heeft Opgelost](/knowledge/dynamic-block-size)/

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