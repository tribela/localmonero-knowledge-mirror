---
title: "Hoe Monero Stealth Adressen Uw Identiteit Beschermen"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero heeft een drieledige benadering van privacy geïmplementeerd. Deze technologieën zijn [ringhandtekeningen](/knowledge/ring-signatures), die de werkelijke output (afzender) verbergen, RingCT die de bedragen verbergt, en stealth-adressen, die de ontvanger verbergt. Vandaag bespreken we de laatste van deze genoemde technologieën: stealth-adressen.

Er zijn veel redenen waarom een persoon zou willen verbergen naar wie ze verzenden. We mogen ons nooit door iemand laten proberen te overtuigen dat alle voorbeelden hiervan onsmakelijk gedrag zijn. Dingen zoals het sturen naar een impopulaire politieke partij, het doneren aan liefdadigheidsinstellingen of het steunen van degenen die volgens de cultuur 'geannuleerd' zijn, zijn allemaal voorbeelden van waar men hun bestedingsgedrag zou willen verbergen uit angst voor repercussies, maar ze zijn volkomen legitiem van aard.

Op een transparante blockchain zijn de adressen waar iemand zijn transacties naartoe stuurt voor iedereen zichtbaar. Het is belangrijk om te bedenken dat als miners het zelf niet eens zijn met waar het geld naartoe gaat, ze ervoor kunnen kiezen om het niet in een blok te minen, waardoor deze transactie effectief wordt gecensureerd op een schijnbaar censuurbestendig platform. De enige manier om deze, weliswaar onwaarschijnlijke, censuur niet mogelijk te maken, is als miners geen onderscheid kunnen maken tussen transacties, omdat alle metagegevens op de keten op verschillende manieren worden verdoezeld. Iets waar Monero bekend om staat.

Monero lost dit probleem van transparante adressen op door stealth-adressen te implementeren, een technologie die oorspronkelijk in 2011 voor Bitcoin werd gemaakt door Bitcoin Talk-forumgebruiker ByteCoin (de relatie met Bytecoin, die later stealth-adressen zou integreren, is onbekend). De huidige vorm van stealth-adressen heeft echter verschillende verbeteringen ten opzichte van het oorspronkelijke idee. Maar laten we het eerst over toetsen hebben om te zien hoe ze werken.

Het is moeilijk om in de cryptocurrency-ruimte te zitten en niets over sleutels te horen. Zinnen als 'back-up van uw privésleutel' komen vaak voor, maar wanneer een gemiddelde Joe de woorden 'publieke sleutel' en 'privésleutel' hoort, worden ze bang en denken ze dat het te technisch en verwarrend zal zijn om te begrijpen. Maar maakt u geen zorgen. We doen het rustig aan en gebruiken veel voorbeelden.

De twee soorten sleutels die in cryptocurrencies worden gebruikt, zijn, zoals zojuist vermeld, openbaar en privé. Deze twee sleutels komen meestal in een paar, wat betekent dat een bepaalde publieke en private sleutel aan elkaar gekoppeld zijn. In feite is de openbare sleutel meestal afgeleid van de privésleutel, wat betekent dat als u de privésleutel kent, uw portefeuille handig kan rekenen en elke keer de juiste openbare sleutel kan vinden. 

Nu, zoals de namen impliceren, kan de openbare sleutel openbaar zijn zonder consequenties. Meestal is het een deel van het adres dat u deelt om geld in uw cryptocurrency-portemonnee te ontvangen. Ook in navolging van zijn naamgenoot is de privésleutel er een die niet mag worden gedeeld. Het is het ding waarmee je een transactie kunt ondertekenen en uitgeven, dus als het wordt gestolen of gedeeld, kan de lafhartige derde partij je geld uitgeven, meestal aan zichzelf.

Een gemakkelijke analogie hiervan is een hangslot en de sleutel die nodig is om het te ontgrendelen. Het open hangslot kan vrij worden gedeeld, en inderdaad kan alles worden afgesloten met dit hangslot, maar alleen de persoon met de sleutel kan alles openen waarop het hangslot is gesloten. Het hangslot kan worden gekopieerd en gedeeld, de sleutel niet.

Deze sleutels worden meestal geabstraheerd weg van de gebruiker, dus u ziet ze nooit echt. In Monero verschijnen ze helemaal niet als een enge alfanumerieke string. In Monero kent de gewone gebruiker de privésleutel als zijn seed. De seed (die u zou moeten opschrijven als u die niet heeft), is eigenlijk gewoon een door mensen leesbare privésleutel. 

Zie? Toch niet zo eng. Terug naar geheime adressen.

Zoals eerder vermeld, zijn stealth-adressen oorspronkelijk niet gemaakt voor Monero, maar voor Bitcoin. Zoals met de meeste nieuwe ideeën, had deze eerste iteratie echter problemen. De volgende poging kwam toen CryptoNote werd gemaakt door Nicholas van Saberhagan voor Bytecoin, de voorloper van Monero ([bekijk hier onze geschiedenis van Monero en Bytecoin](/knowledge/monero-history)), en hoewel het een duidelijke verbetering was ten opzichte van het origineel, had het zelfs enkele subtiele gebreken.

Uiteindelijk kwam er een laatste iteratie tot stand door een ontwikkelaar voor een andere inmiddels ter ziele gegane privacy-cryptocurrency, die de openstaande privacy- en beveiligingsproblemen met het idee oploste. Dit vond uiteindelijk zijn weg naar Monero en is wat tegenwoordig wordt gebruikt. 

Hoewel deze privacy- en beveiligingsproblemen waren opgelost, voegden stealth-adressen zelf een ander soort eigenaardigheid toe aan blockchain-technologieën, een die voorheen niet bestond. De noodzaak om te scannen. Aangezien ontvangende adressen niet openbaar worden weergegeven op de blockchain, weet de ontvanger nooit of een bepaalde transactie van hen is, dus moeten ze elke inkomende transactie met hun privésleutel scannen om te zien of deze van hen is.

Met transparantiemunten hoeven ze alleen maar te controleren of er een transactie naar uw adres wordt verzonden. Een makkelijke ja of nee vraag. Maar met stealth-adressen kan elke transactie mogelijk naar u worden verzonden, dus u moet elke transactie proberen te ontgrendelen met uw privésleutel om te zien of deze wordt geopend. 

Dit is een extra stap die Bitcoin en zijn derivaten niet hebben, en maakt de eerste setup van de portefeuille, samen met het synchroniseren van een portefeuille wanneer u deze een tijdje niet hebt geopend, veel langer dan Bitcoin. De afweging is echter nodig om de privacygaranties te ontgrendelen die het heeft. Het moet worden opgemerkt dat, in tegenstelling tot het zwakste punt van de privacytrifecta, ringhandtekeningen, stealth-adressen niet vatbaar zijn voor heuristiek. Het vertrouwt op beproefde elliptische curve-cryptografie, waar het hele internet op vertrouwt, dus het breken ervan zou een einde betekenen aan de computerbeveiliging in het algemeen, niet alleen aan Monero.

Verder lezen

  * [Hoe Monero op unieke wijze circulaire economieën mogelijk maakt](/knowledge/monero-circular-economies/)

  * [Monero's ringhandtekeningen versus CoinJoin zoals in Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Waarom (en hoe!) u uw eigen sleutels moet bezitten](/knowledge/hold-your-keys/)

  * [Bijdragen aan Monero](/knowledge/contributing-to-monero/)

  * [Hoe externe knooppunten de privacy van Monero beïnvloeden](/knowledge/remote-nodes-privacy/)

  * [Hoe Monero hard forks gebruikt om het netwerk te upgraden](/knowledge/network-upgrades/)

  * [Weergave tags: Hoe één byte de synchronisatietijden van de Monero portefeuille met meer dan 40% vermindert](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool en Zijn Rol bij het Decentraliseren van Monero Mining](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Wat Het Zal Doen voor Monero](/knowledge/seraphis-for-monero/)

  * [Is het Omzetten van Bitcoin naar Monero Net Zo Privé als het Rechtstreeks Kopen van Monero?](/knowledge/most-private-way-to-buy-monero/)

  * [Waarom Monero een Trustless Setup Gebruikt in Tegenstelling tot Zcash](/knowledge/monero-trustless-setup/)

  * [Waarom Monero een Betere Waardeopslag Is Dan Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Hoe Monero de Netwerkeffecten van Bitcoin Kan Overwinnen](/knowledge/network-effect/)

  * [Waarom Monero de Meest Kritische Denkgemeenschap Heeft](/knowledge/critical-thinking/)

  * [Oplichtingen Om Voor Uit Te Kijken Bij Gebruik van Monero](/knowledge/monero-scams/)

  * [Hoe Atomic Swaps Zullen Werken in Monero](/knowledge/monero-atomic-swaps/)

  * [Wat Elke Monero Gebruiker Moet Weten Als het om Netwerken Gaat](/knowledge/monero-networking/)

  * [Hoe RingCT Monero's Transactiebedragen verbergt](/knowledge/monero-ringct/)

  * [Hoe Monero's Subadressen Identiteitskoppeling Voorkomen](/knowledge/monero-subaddresses/)

  * [Monero-Outputs uitgelegd](/knowledge/monero-outputs/)

  * [Praktische Tips van Monero voor Beginners](/knowledge/monero-best-practices/)

  * [Hoe Ring-handtekeningen de Resultaten van Monero Verdoezelen](/knowledge/ring-signatures/)

  * [Hoe Monero het Probleem met de Blokgrootte Dat Bitcoin Plaagt Heeft Opgelost](/knowledge/dynamic-block-size/)

  * [Hoe CLSAG de Efficiëntie van Monero Zal Verbeteren](/knowledge/what-is-clsag/)

  * [Waarom Monero een Staartemissie Heeft](/knowledge/monero-tail-emission/)

  * [Een Korte Geschiedenis van Monero](/knowledge/monero-history/)

  * [Wired Magazine heeft Ongelijk over Monero, Dit is Waarom](/knowledge/wired-article-debunked/)

  * [Top 15 Monero Mythen en Zorgen Ontkracht](/knowledge/monero-myths-debunked/)

  * [Hoe Dandelion++ de Oorsprong van de Transacties van Monero Privé Houdt](/knowledge/monero-dandelion/)

  * [Waarom Monero Open Source en Dedecentraliseerd Is](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero-Mining: Wat RandomX zo Speciaal Maakt](/knowledge/monero-mining-randomx/)

  * [Waarom Monero beter is dan Dash, Zcash, Zcoin (zelfs met Lelantus), Grin en Bitcoin Mixers zoals Wasabi (bijgewerkt mei 2020)](/knowledge/why-monero-is-better/)