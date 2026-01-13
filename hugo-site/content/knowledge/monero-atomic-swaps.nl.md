---
title: "Hoe Atomic Swaps Zullen Werken in Monero"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
In het streven naar decentralisatie en een echt systeem zonder toestemming, zijn er maar een aantal dingen zo begeerd in de cryptocurrency-ruimte als gedecentraliseerde uitwisselingen en atomic swaps. Sinds hun oprichting heeft Monero moeite gehad om atomic swaps te implementeren, omdat de privacyfuncties unieke problemen veroorzaken bij het ontwerpen van een protocol.

Maar laten we eerst een back-up maken. Wat zijn atomic swaps? Een atomic swap is een protocol waarmee twee verschillende cryptocurrencies, op verschillende blockchains, op een betrouwbare manier zonder tussenpersoon kunnen worden uitgewisseld. Dit betekent dat als iemand cryptocurrency A zou willen ruilen voor cryptocurrency B, ze dit zouden kunnen doen zonder een centrale of gedecentraliseerde uitwisseling. Zoals je je misschien kunt voorstellen, is er veel onderzoek voor nodig, en de volledige technische details die het mogelijk maken, worden behoorlijk gecompliceerd. Nogmaals, LocalMonero is hier om te helpen en een eenvoudige uitleg te geven voor de gewone persoon.

Laten we om te beginnen eens kijken naar de meest eenvoudige vorm van een atomic swap, zoals geïmplementeerd door Bitcoin. Als iemand Bitcoin wil inwisselen voor een andere munt die dezelfde hash-tijdslotcontracttechnologie gebruikt, kan dat op de volgende manier. Alice heeft Bitcoin (BTC), maar wil Litecoin (LTC), en Bob heeft LTC, maar wil BTC. Ze besluiten een atomic swap uit te voeren, zodat ze allemaal de munt krijgen die ze willen. Alice stuurt haar BTC naar een speciaal adres, waarbij ze scripts gebruikt die het geld vergrendelen zodat zelfs zij er niet bij kan. Je kunt het ook zien alsof Alice haar BTC in een lockbox stopt. Als de lockbox is gemaakt, krijgt ze een sleutel en stuurt ze een hash van deze sleutel naar Bob. Nu heeft Bob niet de sleutel zelf, alleen de hash, dus hij heeft nog geen toegang tot het geld.

Bob gebruikt deze hash als seed waaruit hij zijn eigen lockbox genereert, en stuurt zijn LTC daarheen, waar hij ook wordt vergrendeld. Omdat de hash van Alice's sleutel werd gebruikt als het seed waarmee Bob's lockbox is gemaakt, kan ze haar sleutel gebruiken om de LTC in Bob's lockbox te claimen. Haar sleutel past! Maar met behulp van wiskundige voodoo-magie, wanneer ze haar sleutel gebruikt om het LTC-slot te openen, onthult ze de sleutel aan Bob, die deze vervolgens kan gebruiken om de BTC te claimen die ze in haar lockbox heeft gestopt. Op deze manier hebben Alice en Bob zonder tussenpersoon met succes hun activa uitgewisseld.

Maar er is een klein probleem. Wat als Alice naar haar lockbox stuurt en Bob besluit dat hij niet meer wil ruilen? Nu Alice geen toegang heeft tot haar BTC die ze heeft opgeborgen, en Bob zijn deel van de transactie niet wilt voltooien, verliest Alice haar geld voor altijd. Gelukkig heeft Bitcoin een kleine technologie die terugbetalingstransacties wordt genoemd, en dus als de BTC na een bepaalde tijd niet door Bob wordt geclaimd, hebben de scripts een ingebouwde fail-safe, waarbij de BTC automatisch teruggaat naar Alice. Dit was de belangrijkste verkeersdrempel voor de implementatie van de atomic swaps van Monero. Vanwege de [privacytechnologie voor ringhandtekeningen ](/knowledge/ring-signatures) van Monero is de afzender van een transactie altijd onzeker. Hoe kan het protocol een terugbetalingstransactie doen als het niet weet waar de transactie vandaan komt? 

In 2017 schetste een kleine groep onderzoekers een andere methode waarmee atomic swaps zouden werken in Monero. Na een aantal jaren van verfijning hebben de onderzoekers een proces voltooid waarmee Monero atomic swaps met Bitcoin zou kunnen doen, zelfs zonder terugbetalingstransacties. 

Zoals veel dingen op dit niveau van technische complexiteit, zal onze uitleg sommige dingen erg vereenvoudigen om het idee over te brengen, maar het zal nog steeds een goed idee geven van de mechanismen waarmee dit proces zou werken.

Zowel Alice (die XMR heeft en BTC wil) als Bob (die BTC heeft en XMR wil) moeten een programma downloaden en gebruiken dat de atomic swap ondersteunt. Dit kan worden geïmplementeerd in portefeuilles, gedecentraliseerde uitwisselingen of speciale, specifieke programma's, maar de software moet het atomic swap-protocol uitvoeren. In de eerste stap maken de klanten van Alice en Bob verbinding met elkaar en maken verschillende gedeelde geheimen en sleutels. In deze stap wordt een nieuw Monero-adres aangemaakt, waarbij Alice de ene helft van de sleutel heeft en Bob de andere. Er zit echter nog geen Monero in, dus er is niets te besteden. Een laatste ding om op te merken over dit adres, is dat ze allebei de sleutel tot deze portefeuille hebben, zodat ze allebei er in kunnen kijken om te zien of en wanneer Monero arriveert. 

In de tweede stap stuurt Bob zijn BTC naar een speciaal adres, vergelijkbaar met het Bitcoin atomic swap-protocol dat we al hebben besproken. Nadat Alice de BTC op dit adres op de blockchain ziet aankomen, stuurt ze haar Monero naar het Monero-adres waar zij en Bob allebei een halve sleutel van hebben. Bob kan verifiëren dat de Monero is aangekomen, aangezien hij ook de kijksleutel heeft, en zodra hij ziet dat de Monero veilig in de portefeuille zit, stuurt hij Alice een stuk van een sleutel waarmee ze de Bitcoin kan opnemen. Net als bij het andere protocol, onthult het proces van het claimen van de Bitcoin haar de helft van de Monero-sleutel aan Bob. Nu heeft Bob beide helften, dus hij kan de Monero claimen, terwijl Alice alleen haar helft heeft, dus ze kan niet proberen om het te claimen voordat hij het doet.

Dus als u dit allemaal heeft bekeken en nog steeds een beetje in de war bent over hoe Monero het probleem van terugbetalingstransacties kon omzeilen, is het antwoord vrij eenvoudig. Aangezien Monero zelf geen terugbetalingstransacties heeft, zou de lezer moeten opmerken dat de Bitcoin (die wel terugbetalingstransacties heeft) eerst wordt verzonden, en pas nadat er is geverifieerd dat deze zich op de blockchain bevindt, wordt de Monero verzonden. Hierdoor kan Monero gebruikmaken van de mogelijkheid van Bitcoin om terugbetalingstransacties te scripten en hiervan te profiteren, zonder dat ze zelf over deze mogelijkheden hoeven te beschikken.

De atomic swap is nu voltooid, maar vanaf hier heeft Bob een paar opties voor zijn nieuw geclaimde XMR. Hij kan deze Monero-portefeuille gebruiken zoals hij is, of de XMR verplaatsen naar een andere portefeuille die hij al bezit. Bob zal de Monero hoogstwaarschijnlijk naar een andere portefeuille verplaatsen, omdat Alice nog steeds de kijksleutel heeft en daarbij toegang krijgt.

Het mooie van dit protocol is dat het nog vrij nieuw is en dat er genoeg ruimte is voor optimalisaties. Het is ook vrij flexibel in zijn architectuur, dus implementatie in andere portefeuilles of gedecentraliseerde uitwisselingen zou eenvoudig moeten zijn en netjes moeten passen in hun bestaande architectuur.

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