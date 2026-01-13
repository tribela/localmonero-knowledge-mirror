---
title: "Seraphis: Wat Het Zal Doen voor Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: een modulaire ontwerpupgrade voor Monero transacties

## Seraphis: een modulaire ontwerpupgrade voor Monero transacties

Dit bericht beschrijft [Seraphis](https://github.com/UkoeHB/Seraphis), een reeks transactieprotocolstructuren en abstracties ontwikkeld door pseudonieme onderzoeksmedewerker [`koe`](https://github.com/UkoeHB) voor het Monero-ecosysteem, en met voortdurende beveiligingsanalyse door pseudonieme bijdrager [`coinstudent2048`](https://github.com/coinstudent2048).  
We maken enkele vereenvoudigingen en laten bepaalde technische details weg voor de duidelijkheid; om deze reden, en omdat het ontwerp van Seraphis nog in volle gang is, dienen geïnteresseerde lezers de documentatie van Seraphis te raadplegen voor de meest up-to-date informatie.

## Transacties in Monero

## Transacties in Monero

Protocollen zoals Bitcoin en Monero en andere vertrouwen op een zogenaamd "outputmodel" van de werking, waarbij een _output_ een representatie is van waarde die kan worden overgedragen.  
Transacties verbruiken een of meer outputs gecontroleerd door een afzender, en genereren nieuwe outputs gericht op ontvangers (of terug naar de afzender als wisselgeld); de transactie moet in evenwicht zijn aangezien verbruikte outputs een totale waarde moeten bevatten die exact gelijk is aan de waarde in nieuwe outputs (plus een door het netwerk opgelegde vergoeding).   
In veel protocollen, zoals Bitcoin, wordt de waarde in een output duidelijk geschreven, net als de ontvanger.  
Bovendien is het, door naar de blockchain te kijken, triviaal om te zien of en wanneer een output is uitgegeven (dat wil zeggen, of het is verbruikt in een latere transactie, en door welke transactie het is uitgegeven). 

Daarentegen introduceren protocollen zoals Monero een ander ontwerp:

  * Output-waarden zijn verborgen en niet zichtbaar op de blockchain
  * Ontvangeradressen worden verborgen door het gebruik van een eenmalig adresseringsprotocol
  * Of een output al dan niet is uitgegeven, wordt verdoezeld door het gebruik van dubbelzinnige handtekeningen

Het resultaat is dat het bij afwezigheid van externe informatie moeilijk is om te bepalen of een bepaalde output is uitgegeven, wat de waarde ervan is en wie de ontvanger is.

Het huidige Monero-transactieprotocol heet _RingCT_ en gebruikt verschillende cryptografische bouwstenen om deze ontwerpdoelen te bereiken.

  * _Verplichtingen_ verbergen bedragen op een wiskundig handige manier
  * _Bereikbewijzen_ voorkomen overloop waardoor de toevoer kan worden opgeblazen
  * _Koppelbare ringhandtekeningen_ zorgen voor dubbelzinnigheid bij de ondertekenaar en voorkomen dubbele uitgaven
  * _Commitment offsets_ stellen dat transacties in evenwicht zijn

Deze bouwstenen zijn zorgvuldig met elkaar verweven om het RingCT-protocol te bouwen.

Een handige eigenschap van het RingCT-protocol is dat sommige bouwstenen zodanig kunnen worden gewijzigd of geüpgraded dat het algehele ontwerp en de eigenschappen intact blijven, maar dat efficiëntie- of beveiligingsverbeteringen kan opleveren. In de geschiedenis van Monero zijn dit soort upgrades zelfs meerdere keren voorgekomen (of zijn gepland). Bereikbewijzen in het oorspronkelijke RingCT-protocol waren omvangrijk en traag; ze werden later geüpdatet naar een constructie genaamd [Bulletproofs](https://eprint.iacr.org/2017/1066) die transacties kleiner en sneller maakte met betere beveiligingsanalyse, en het is de bedoeling dat ze worden geüpdatet naar een nieuwere constructie genaamd [Bulletproofs+](https://eprint.iacr.org/2020/735) voor nog grotere efficiëntievoordelen. 

Een soortgelijk proces werd ondergaan met de bouwsteen van de koppelbare ringsignatuur. In het oorspronkelijke protocol werd een constructie met de naam [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34) gebruikt. Dit werd later geüpdatet naar een nieuwere constructie genaamd [CLSAG](https://eprint.iacr.org/2019/654) die sneller is, resulteert in kleinere transacties en een betere beveiligingsanalyse heeft. Er werd een nog nieuwere, koppelbare ringsignatuurconstructie voorgesteld, gebaseerd op [Triptych](https://eprint.iacr.org/2020/018), maar deze werd niet geselecteerd voor implementatie vanwege de gevolgen voor operaties met meerdere handtekeningen.

## Seraphis

## Seraphis

Seraphis gaat nog een stap verder met dit idee.  
In plaats van individuele bouwstenen van het bestaande RingCT-transactieprotocol bij te werken, introduceert het een ander protocol dat kan profiteren van verschillende bouwstenen en een verbeterde functionaliteit biedt.

## Bouwstenen

## Bouwstenen

Seraphis gebruikt een andere set cryptografische bouwstenen om zijn ontwerpdoelen te bereiken.

  * _Toezeggingen_ verbergen nog steeds bedragen
  * _Bereikbewijzen_ voorkomen nog steeds overloop en voorraadinflatie
  * _Lidmaatschapsbewijzen_ zorgen voor dubbelzinnigheid van de ondertekenaar
  * _Commitment offsets_ behouden nog steeds saldo
  * _Bewijzen autoriseren_ voorkomen dat dubbele uitgaven worden gedaan

Let op de verandering hier: koppelbare ringhandtekeningen worden vervangen door een combinatie van lidmaatschapsbewijzen en machtigingsbewijzen. Grofweg laten lidmaatschapsbewijzen zien dat een verbruikte output deel uitmaakt van een grotere set, vergelijkbaar met wat er gebeurt in RingCT. Maar in tegenstelling tot RingCT, hebben lidmaatschapsbewijzen helemaal geen linktag nodig! Autorisatiebewijzen tonen aan dat de linking tag geldig is en worden gebruikt om de uiteindelijke transactie te ondertekenen.

Omdat RingCT de koppelingstag in de dubbelzinnige handtekening bakt, zijn ondertekenings- (en multisignatuur-) bewerkingen meer rekenintensief en wordt het een grotere uitdaging om andere taggerelateerde functionaliteit te bouwen. Maar in Seraphis kan het samenstellen van lidmaatschapsbewijzen veilig worden gedelegeerd van zeer vertrouwde apparaten (die mogelijk beperkte rekenkracht hebben, zoals een hardware portefeuille) naar een minder vertrouwd apparaat, en ondertekenings- (en meervoudige handtekeningen) bewerkingen zijn veel eenvoudiger met behulp van het veel eenvoudigere autorisatiebewijs .

Gelukkig bestaan sommige van de bouwstenen die Seraphis nodig heeft al elders en hoeven ze niet vanaf nul te worden ontworpen. Zowel de Bulletproofs als de Bulletproofs+ constructies kunnen gebruikt worden als range proofs. Wijzigingen aan testsystemen van het Schnorr-type kunnen worden gebruikt voor het autoriseren van bewijzen. En een efficiënt [testsysteem](https://eprint.iacr.org/2015/643) dat al wordt gebruikt als basis voor Triptych, [Lelantus](https://eprint.iacr.org/2019/373) en [Spark](https://eprint.iacr.org/2021/1173)* kan worden aangepast voor lidmaatschapsbewijzen.

* Cypher Stack ontvangt financiering voor Spark-ontwikkeling.

## Adressering

## Adressering

Helaas zijn de momenteel in gebruik zijnde Monero-adressen niet compatibel met Seraphis. Gebruikers zouden nieuwe adressen moeten genereren uit hun portefeuillesleutels om Monero te ontvangen als Seraphis zou zijn geïmplementeerd. Deze ecosysteemkosten brengen echter tal van voordelen met zich mee.

Afgezien van de hierboven besproken structurele voordelen, is het Seraphis-ontwerp vatbaar voor veel verschillende adresconstructiemogelijkheden, die allemaal gepaard gaan met compromissen. Hoewel de definitieve adresconstructie die in Seraphis zal worden gebruikt [nog wordt besloten](https://github.com/monero-project/research-lab/issues/92) (een schema dat veel aandacht krijgt, heet [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), kunnen we enkele algemene en nuttige functies beschrijven.

U weet misschien dat Monero-adressen _weergavesleutel_ -functionaliteit bieden, waarmee u een apparaat of een derde partij een weergavesleutel kunt geven en deze namens u naar inkomende output kunt laten kijken, maar zonder de uitgaven op te geven Gezag. Dit is handig voor portefeuilles, die up-to-date kunnen blijven terwijl uw uitgavensleutel veilig wordt opgeborgen. Het is ook handig voor gevallen waarin u toegang wilt tot externe weergaven, zoals een openbare liefdadigheidsinstelling die transparantie biedt of een bedrijf met een boekhoudafdeling.

Het nadeel van Monero-weergavetoetsen is dat ze geen volledige of fijnmazige weergavetoegang bieden. Het is niet mogelijk om op betrouwbare wijze te detecteren wanneer een portemonnee geld uitgeeft, wat het moeilijk maakt om het saldo van de portefeuille correct te berekenen wanneer de bestedingssleutel niet beschikbaar is. Het is momenteel ook niet mogelijk om inkomende outputs te detecteren zonder ook de waarde in die outputs te leren (wat betekent dat derden die verantwoordelijk zijn voor het vinden van inkomende outputs precies weten hoeveel Monero u verwerft).

Seraphis adresseringsconstructies kunnen dit oplossen. Met Seraphis is uw adres uitgerust met verschillende sleutels die verschillende dingen kunnen doen:

  * Let op inkomende outputs maar verberg de waarde ervan
  * Let op inkomende outputs, maar toon hun waarde
  * Let op uitgaande outputs
  * Help u om transacties te genereren, maar niet om ze te ondertekenen
  * Genereer nieuwe adressen (handig voor winkeliers of uitwisselingen met veel klanten)

Als adreshouder mag u beslissen hoeveel bevoegdheid u delegeert aan andere apparaten of derden.

## Het grote plaatje

## Het grote plaatje

Seraphis is een grote verandering in het Monero-ecosysteem. Hoewel het aanpassingen aan adressen en transactiebouwstenen met zich meebrengt, biedt het ontwerp flexibiliteit en handige functionaliteit die niet mogelijk is met het huidige RingCT-protocol. Terwijl een groot deel van het ontwerp is voltooid en wordt ontwikkeld tot [een implementatie](https://github.com/UkoeHB/monero/tree/seraphis_lib), zijn adresontwerp en beveiligingsanalyse aan de gang. Seraphis biedt een uitstekende mogelijkheid om het Monero-ecosysteem vooruit te helpen! 

Verder lezen

  * [Hoe Monero op unieke wijze circulaire economieën mogelijk maakt](/knowledge/monero-circular-economies)/

  * [Monero's ringhandtekeningen versus CoinJoin zoals in Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Waarom (en hoe!) u uw eigen sleutels moet bezitten](/knowledge/hold-your-keys)/

  * [Bijdragen aan Monero](/knowledge/contributing-to-monero)/

  * [Hoe externe knooppunten de privacy van Monero beïnvloeden](/knowledge/remote-nodes-privacy)/

  * [Hoe Monero hard forks gebruikt om het netwerk te upgraden](/knowledge/network-upgrades)/

  * [Weergave tags: Hoe één byte de synchronisatietijden van de Monero portefeuille met meer dan 40% vermindert](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool en Zijn Rol bij het Decentraliseren van Monero Mining](/knowledge/p2pool-decentralizing-monero-mining)/

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