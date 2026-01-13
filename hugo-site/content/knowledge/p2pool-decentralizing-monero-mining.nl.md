---
title: "P2Pool en Zijn Rol bij het Decentraliseren van Monero Mining"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Een van de kerndoelen van het Monero-project is om een eerlijk, gedecentraliseerd en veilig netwerk mogelijk te maken door middel van nieuwe en innovatieve benaderingen van proof-of-work (PoW) mining, de belangrijkste manier waarop cryptocurrency-netwerken tegenwoordig worden beveiligd.

Hoewel een uniek mining-algoritme [ zoals RandomX ](/knowledge/monero-mining-randomx) uiterst belangrijk is voor dit doel, omdat het ervoor zorgt dat iedereen met een computer een behoorlijke bijdrage kan leveren aan de beveiliging van het netwerk, lost RandomX de problemen niet op die kunnen optreden als gevolg van poolmining. Pool-mining is tegenwoordig verreweg de meest gebruikelijke manier om cryptocurrencies te minen, waaronder Monero, maar gelukkig brengt de opkomst van p2pool-mining daar snel verandering in.

## Wat is pool mining?

Pool mining is een manier voor miners om de taak te delen om een blok op het netwerk op te lossen en vervolgens de beloningen gelijkmatig te verdelen voor alle blokken die de pool vindt. Hoewel dit enorm helpt om de frequentie waarmee miners worden betaald te verdelen in vergelijking met alleen Monero, is het niet zonder ernstige centralisatie problemen.

Terwijl elke miner werk bijdraagt aan de pool, geven ze de controle over al het werk dat ze doen op en blokkeren ze dat naar de pool zelf, in het vertrouwen dat de pool de beloningen eerlijk zal verdelen onder alle miners op basis van de hoeveelheid werk dat ze hebben gedaan. Als alles goed gaat, verzamelt de poolbeheerder het werk van alle miners, legt het voor aan het netwerk en verdeelt de beloningen gelijkelijk.

## Wat is het probleem met poolmining?

Helaas berust dit volledig op vertrouwen en stelt het de poolbeheerder in staat om snode dingen te doen met het werk dat door miners wordt gedaan. De poolbeheerder kan het werk dat wordt gedaan gebruiken om het netwerk aan te vallen, proberen om geld dubbel uit te geven (als de pool groot genoeg is), of gewoon het werk van de miners gebruiken om zichzelf te kunnen betalen en miners hierbij nooit correct te belonen voor hun werk .

Het grootste risico voor het netwerk is dat een pool (of meerdere pools die samenwerken) meer dan 51% van de hashrate van het netwerk onder hun controle heeft, omdat ze dit zouden kunnen gebruiken om vals te spelen en twee keer geld uit te geven (een dubbele uitgave aanval) of proberen de regels van het netwerk te wijzigen.

## Wat is p2pool?

p2pool is een concept dat oorspronkelijk in 2011 is gemaakt voor het minen van Bitcoin, maar dat nooit breed is geaccepteerd en praktisch ongebruikt blijft op Bitcoin. Gelukkig bracht een van de belangrijkste ontwikkelaars achter RandomX, SCHernykh, zijn vakantie door met het bedenken van oplossingen voor enkele problemen met de Bitcoin-implementatie van p2pool en het herschrijven van alle software vanaf nul. 

p2pool in Monero biedt miners een volledig vertrouwenloze manier om samen te werken om blokken op te lossen en het Monero-netwerk te beveiligen door een speciale knooppunt-software voor p2pool te gebruiken om het werk te delen. 

Dit wordt gedaan met behulp van een nieuwe blockchain (een "side-chain") die bijhoudt hoeveel werk elke miner doet, wat het adres van hun portefeuille is en hoeveel Monero ze hebben verdiend, en vervolgens wordt de beloning uitbetaald in een vertouwenloze en gedecentraliseerde manier. Omdat deze zijketen veel minder miners heeft, is het veel gemakkelijker om blokken te vinden en in te dienen dan op het hoofdnetwerk van Monero, waardoor het voor miners gemakkelijker wordt om consistente uitbetalingen te krijgen in vergelijking met het menen van alleen Monero.

## Hoe lost p2pool de problemen van poolmining op?

In p2pool is er geen gecentraliseerde pool, gecentraliseerde pooloperator of enkele persoon die fondsen vasthoudt en uitbetalingen verdeelt. Al het werk dat collectief wordt gedaan door degenen die via p2pool minen, wordt gecontroleerd door de p2pool-blockchain en andere knooppunt-operators om ervoor te zorgen dat het legitiem is, en alle miners direct worden uitbetaald op basis van het werk dat ze hebben gedaan wanneer een blok wordt gevonden door de beloningen in dat gevonden blok.

Wanneer miners ervoor kiezen om p2pool te gebruiken in plaats van een gecentraliseerde pool, verwijderen ze alle macht en vertrouwen van pooloperators en zorgen ze ervoor dat hun werk bijdraagt aan het welzijn van het netwerk en aan hun eigen beloningen, en verminderen ze het risico op netwerkaanvallen, misbruik van hun werk, of diefstal van beloningen die ze verschuldigd zijn. 

Dit helpt hen niet alleen hun eigen belangen te beschermen, het vermindert ook het risico dat gecentraliseerde pools kunnen vormen voor het Monero-netwerk als geheel. Het gebruik van p2pool helpt ook enorm om het risico te verminderen dat natiestaten of regelgevers kunnen vormen voor de gezondheid van het netwerk, aangezien er geen gecentraliseerde poolbeheerders zijn die onder druk kunnen worden gezet, geen geografische concentratie van pools om op te leunen of enig ander gemakkelijk drukpunt die ze tegen Monero kunnen gebruiken.

## Wat zijn de nadelen?

Gelukkig is p2pool in Monero goed ontworpen en gebouwd, en functioneert het daarbij ook buitengewoon goed! Het belangrijkste nadeel van p2pool-mining is echter wel dat elke miner die p2pool wilt gebruiken, zijn eigen Monero-knooppunt moet gebruiken, waardoor het proces om op gang te komen wat ingewikkelder is. Dit knooppunt wordt dan gebruikt om alle informatie te berekenen die nodig is voor het bouwen en controleren van blokken, en zorgt ervoor dat de miner de volledige controle heeft over zijn werk. Het knooppunt kan ook fungeren als een knooppunt op afstand voor de eigen portefeuille van de miner, draagt bij aan het netwerk en nog veel meer. 

Het andere belangrijke verschil met gecentraliseerde mining is dat kleine miners die p2pool gebruiken iets meer " variantie " hebben, of tijd tussen uitbetalingen, dan een grote gecentraliseerde pool -- het ' is _extreem_ belangrijk om op te merken dat dit er niet toe zal leiden dat u na verloop van tijd minder Monero verdient! P2pool zal in de loop van de tijd net zo winstgevend zijn voor zelfs kleine miners als gecentraliseerde pools. Een deel van deze variantie wordt ook gecompenseerd doordat p2pool native 0% kosten heeft, aangezien er geen gecentraliseerde pooloperator is om voor hun diensten te betalen! 

## Hoe ga ik aan de slag?

Dankzij het uitstekende ontwerp van Monero's p2pool-implementatie en de vele mensen in de gemeenschap die tijd hebben gestoken in het proces van minen via p2pool te helpen vereenvoudigen, wordt van start gaan in de loop van de tijd steeds eenvoudiger. Er zijn verschillende manieren om te beginnen te minen met p2pool, maar aangezien de technische details buiten het bereik van dit artikel vallen, voelt uzelf vrij om naar een onderstaande link te gaan, afhankelijk van uw besturingssysteem:

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## Hoe kan ik meer leren?

Als dit uw nieuwsgierigheid naar p2pool-mining heeft gewekt, kijk dan hieronder voor enkele extra links en uitleg over p2pool, hoe het werkt en wat het betekent voor Monero:

  * [De officiële Github voor p2pool](https://github.com/SChernykh/p2pool)
  * [De officiële documenten over het gebruik van p2pool](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool is nu live](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, een soort "blokverkenner" voor p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-samenstellen](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh: over zijn ontwikkeling van P2Pool, een gedecentraliseerde XMR-miningpool](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

Verder lezen