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

Voor degenen die minder bekend zijn met hoe Monero werkt: de knooppunten (of servers) in het Monero-netwerk kunnen door iedereen worden beheerd en kan de eigenaar van het knooppunt toestaan - of anderen waarmee ze het willen delen! – om een kopie van de blockchain te synchroniseren en deze aan anderen op het netwerk te verstrekken. Deze knooppunten verifiëren ook alle transacties die op het netwerk plaatsvinden, evenals alle blokken die worden gepubliceerd, en zorgen ervoor dat ze allemaal de regels volgen zoals vastgesteld door consensus.

De andere functie die knooppunten in Monero hebben, is een manier om alle gegevens te verstrekken die uw favoriete Monero-portefeuille nodig heeft om correct te controleren op transacties die van u zijn en om nieuwe transacties te doen. Deze gegevens worden op twee manieren door knooppunten geleverd: 

  * De gegevens van elk blok op de blockchain worden door de portefeuille opgevraagd, gescand op transacties die van u zijn en vervolgens weggegooid zodra ze door de portefeuille zijn gecontroleerd. 
    * Deze stap wordt binnenkort drastisch verbeterd, dankzij [weergave tags](/knowledge/view-tags-reduce-monero-sync-time).
  * Bij het verzenden van transacties biedt het knooppunt dat u gebruikt een lijst met mogelijke lokvogels (of nepinvoer) die u kunt gebruiken bij het bouwen van de transactie, zodat u een goede menigte hebt om u in te verstoppen elke keer dat u Monero uitgeeft. 
    * Deze lokvogels maken deel uit van [ringhandtekeningen](/knowledge/ring-signatures), een belangrijk onderdeel van Monero's benadering van privacy on-chain.

  * Deze stap wordt binnenkort drastisch verbeterd, dankzij [weergave tags](/knowledge/view-tags-reduce-monero-sync-time).

  * Deze lokvogels maken deel uit van [ringhandtekeningen](/knowledge/ring-signatures), een belangrijk onderdeel van Monero's benadering van privacy on-chain.

## Wat is de meest privé en veilige manier om Monero te gebruiken?

Het beste wat u kunt doen, zelfs met de sterke on-chain privacy die door Monero wordt geboden bij het gebruik van externe knooppunten, is uw eigen Monero-knooppunt te gebruiken om ervoor te zorgen dat u een ongerepte kopie van de Monero-blockchain bij de hand hebt en dat uw IP-adres goed wordt beschermd. Het andere voordeel bij het runnen van uw eigen knooppunt is dat u kunt bijdragen aan het netwerk, andere knooppunten kunt laten synchroniseren vanaf uw knooppunt of zelfs andere gebruikers met hun portefeuille verbinding kunnen laten maken met uw knooppunt.

Dat gezegd hebbende, biedt Monero nog steeds uitstekende privacy bij gebruik van een extern knooppunt. Als u geïnteresseerd bent in het runnen van uw eigen Monero knooppunt, is hier een eenvoudig te volgen gids om dit te doen:

  * [Een Monero-knooppunt uitvoeren](https://sethforprivacy.com/guides/run-a-monero-node/)

## Wat kan een extern knooppunt over mij te weten komen?

Bij gebruik van een extern knooppunt zijn er enkele belangrijke stukken informatie die worden blootgesteld aan een extern knooppunt en een aantal belangrijke manieren waarop het knooppunt u kan aanvallen, kan voorkomen dat u transacties uitvoert en meer.

Het eerste dat een extern knooppunt over u te weten kan komen, is uw openbare IP-adres. Hoewel dit hopelijk wordt verborgen via een VPN of Tor, kan het externe knooppunt uw openbare IP-adres aan de transactie koppelen, waardoor ze kunnen achterhalen waar u vandaan komt. Het externe knooppunt kan ook het laatste blok leren dat uw portefeuille heeft gesynchroniseerd en dit gebruiken om gefundeerde gissingen over u te maken, bijvoorbeeld wanneer u normaal gesproken Monero gebruikt en wanneer u voor het laatst Monero heeft uitgegeven. Dit is vooral het geval als u altijd vanaf hetzelfde IP-adres komt (zoals uw huis). Het laatste belangrijke dat een extern knooppunt over u kan leren, is basisinformatie over de transacties die u er doorheen verzendt. Hoewel dit de meest voor de hand liggende gegevens zijn die de extern knooppunt-operator over u krijgt, is het belangrijk om te begrijpen dat dit kan worden gebruikt om de afzender van de transactie op te sporen bij het combineren van die informatie met andere off-chain-gegevens. Dit kan met name gevaarlijk zijn als het externe knooppunt wordt beheerd door een kwaadwillende entiteit, een blockchain-analysebedrijf of een onderdrukkende natiestaat.

Een extern knooppunt kan ook proberen u problemen te bezorgen door blokken voor u te verbergen, waardoor uw portefeuille denkt dat het is gesynchroniseerd terwijl dit niet het geval is. Dit kan u laten denken dat er geld verloren is of u ervan weerhouden geld uit te geven totdat u verbinding maakt met een ander knooppunt. Het laatste belangrijke dat een extern knooppunt kan doen, is uw portefeuille een gemanipuleerde lijst met lokvogels geven. Dit kan ertoe leiden dat uw portefeuille ofwel volledig faalt om transacties op te bouwen (waardoor u geen geld kunt uitgeven), of dat het externe knooppunt kan proberen lokvogels aan te bieden waarvan het weet dat ze zijn uitgegeven om de anonimiteit die u bij elke transactie ontvangt te verminderen. 

## Welke privacygaranties zijn er nog bij het gebruik van een extern knooppunt?

Hoewel dit artikel u misschien een beetje heeft laten schrikken, is het belangrijk om te beseffen dat de privacy die door Monero wordt geboden uitstekend is, zelfs bij gebruik van een extern knooppunt, en elke andere cryptocurrency ver overtreft wanneer het op deze manier wordt gebruikt. U krijgt nog steeds de sterke on-chain privacy die door Monero wordt geboden, omdat het externe knooppunt nooit de echte input weet (welke munten u uitgeeft), het bedrag aan Monero dat aan de transactie is uitgegeven of het adres van de ontvanger van de transactie. Externe waarnemers kunnen ook de werkelijke input, hoeveelheid of adressen niet zien (ongeacht het type knooppunt dat u kiest om te gebruiken!), wat ervoor zorgt dat zelfs buiten het externe knooppunt uw IP-adres, portefeuille-synchronisatie-informatie en transacties sterke privacygaranties hebben .

Het externe knooppunt heeft ook nooit toegang tot de eerdere transacties die u heeft verzonden of ontvangen, of de hoeveelheid Monero die momenteel in uw portefeuille zit, en verliest alle zichtbaarheid in uw transacties op het moment dat u een ander knooppunt gaat gebruiken. Er worden nooit privésleutels (uitgave- of weergavesleutels) aan het externe knooppunt verstrekt, en dus blijft uw portefeuille privé, veilig en bruikbaar. Ongeacht het externe knooppunt, loopt u ook nooit het risico Monero te verliezen of ervan beroofd te worden, aangezien het knooppunt het adres van de ontvanger niet kan bewerken, nooit toegang heeft tot de privésleutels van uw portefeuille en uw Monero op geen enkele manier in beslag kan nemen.

## Hoe zit het met "lichte portefeuilles" zoals MyMonero?

Hoewel het onderwerp een beetje buiten het bereik van dit artikel valt, wilde ik het toch hebben over een uniek type portefeuille in Monero: lichte portefeuille ("light wallet"). De naam van het feit dat uw portefeuille (op uw telefoon of computer) geen blockchain-synchronisatie hoeft uit te voeren, waardoor de ervaring sneller en vloeiender wordt.

Voor dit soort portefeuilles is er echter een serieuze privacyafweging: uw portefeuille stuurt de privéweergavesleutel naar de externe server die u gebruikt (zoals de standaard in MyMonero), waardoor de externe server volledig inzicht krijgt in het eventueel ontvangen geld sinds de creatie van uw portefeuille (en verder totdat u stopt met het gebruik van die portefeuille of seed). Dit vermindert de privacy die u ontvangt van de knooppunt-operator drastisch en moet met de nodige voorzichtigheid worden benaderd. 

Gelukkig werkt de Monero-community aan het verbeteren van de software die u kunt gebruiken om uw eigen lichte portefeuille-server (LWS) te hosten, waardoor u snel kunt synchroniseren zonder dat u een derde partij vertrouwt met uw privésleutels - aangezien u de software zult controleren waar uw portefeuille de privé weergavesleutels naartoe stuurt! 

Voor meer informatie over de aangepaste LWS, zie het onderstaande Github-archief:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Hoe kan ik meer leren?

Als je nieuwsgierig bent en knooppunten in Monero beter wilt begrijpen, wilt kijken of u een knooppunt op afstand kunt gebruiken of uw eigen knooppunt wilt kunnen gebruiken, bekijk dan de onderstaande links voor goede plekken om van start te gaan:

Verder lezen