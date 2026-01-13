---
title: "Hoe Monero's Subadressen Identiteitskoppeling Voorkomen"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero heeft altijd innovatieve manieren gevonden om lastige privacyproblemen op te lossen. Vaak leiden deze innovaties tot andere innovaties, en soms kunnen deze resulterende technologieën zelfs worden gebruikt voor use-cases die nog niet eerder waren overwogen. Nergens wordt dit beter geïllustreerd dan in het geval van de subadrestechnologie van Monero. 

Beschouw een hypothetisch privacyprobleem, waarbij het gebruik van één adres op meerdere platforms van ogenschijnlijk niet-verwante mensen kan leiden tot koppeling en deanonimisering van die mensen. Simpel gezegd, als u een persoon was die Billy Joe Bob heette en u appels verkocht voor Bitcoin, zou u uw Bitcoin-adres op een openbare plaats kunnen plaatsen zodat klanten u kunnen betalen. Laten we zeggen dat het adres begint met de alfanumerieke reeks 7XybV3... Maar afgezien van het voor de hand liggende privacyrisico dat iemand uw Bitcoin-saldo kan controleren en zien hoeveel u heeft verkocht, is er een tweede, niet vaak besproken privacyrisico. Laten we zeggen dat u ook een ondergrondse hacker was met de naam l33tz0r. U doet klokkenluiderswerk, en vertelt een nietsvermoedende bevolking over corruptie bij de overheid, waarbij het absoluut noodzakelijk is dat u uw identiteit geheim houdt. U accepteert Bitcoin-donaties voor uw werk en plaatst het adres op een openbaar forum. Het is hetzelfde adres waarop u geld accepteert van uw Apple-klanten. Dezelfde 7XybV3... reeks.

Een eenvoudige, maar verwoestende deanonimiseringsaanval zou zijn om een internetzoekmachine te gebruiken om naar uw Bitcoin-adres te zoeken. Als u het adres van 7XybV3... in de engine invoert, krijgt u twee verschillende resultaten. De appelhandel, en l33tz0r. Dit is genoeg om de twee identiteiten te koppelen en l33tz0r te deanonimiseren, met mogelijk angstaanjagende gevolgen van de heersende machten.

Het is belangrijk op te merken dat deze aanval OOK mogelijk is met Monero. Hoewel Monero de meeste on-chain-gegevens verbergt, gebruikt deze aanval er geen. Het gebruikt alleen het adres, dat moet worden gedeeld om de betaling te ontvangen. Openbaar in het geval van anonieme donaties. Dit is een mogelijke manier waarop Monero-gebruikers onbewust hun privacy kunnen schaden, en het is ook een voorbeeld van hoe, hoewel Monero het beste is wat betreft privacybehoud, het niet waterdicht is.

De gebruikelijke manier om dit probleem te omzeilen was het bezit van meerdere portefeuilles. Omdat er voor elke identiteit (of usecase) verschillende adressen zijn gepost, kunnen ze niet worden gekoppeld. Maar deze privacy geldt alleen als de gebruiker ze nooit door elkaar haalt. Het per ongeluk posten van het onjuiste adres zou dezelfde koppelingseffecten hebben. Ook moet de seed van elk adres veilig worden bewaard, waardoor het infosec-werk dat nodig is bij elke nieuwe portemonnee die wordt gemaakt, toeneemt. 

Monero's oplossing was subadressen. De mogelijkheid om een absoluut enorm aantal adressen onder het hoofdadres aan te maken en dit als een soort zaadje te gebruiken. Elk gegenereerd subadres kan Monero accepteren en alles gaat naar dezelfde portemonnee. Met deze methode is het aantal identiteiten dat onder één adres kan worden beheerd enorm, terwijl het infosec-werk tot een minimum wordt beperkt. Deze adressen zijn ook niet wiskundig koppelbaar, dus tenzij de gebruiker hun verbinding met de wereld roept, zal een externe waarnemer grote moeite hebben om ze te koppelen.

Maar een andere interessante usecase kwam voort uit subadressen; als vervangingsoptie van de universeel gehate betalings-ID's. 

Betalings-ID's waren een manier voor verkopers om te identificeren welke klant welke betaling heeft verzonden. Omdat Monero-informatie op de ketting verborgen is, kan de ontvanger van een transactie niet zien welk adres het heeft verzonden. Dit betekent dat als er artikelen met een vergelijkbare prijs en meerdere bestellingen zijn, het onmogelijk kan worden om te identificeren wie wat heeft verzonden. Betalings-ID's zijn een unieke, willekeurige reeks die door de handelaar wordt gegenereerd en aan de klant wordt gegeven. De klant voegt dit als een apart veld toe bij het versturen van de transactie. Deze willekeurige reeks wordt op de blockchain geplaatst als onderdeel van de transactie, en op deze manier kan de handelaar inkomende transacties identificeren en sorteren.

Deze methode was op verschillende manieren gebrekkig. Ten eerste doet het afbreuk aan de uniformiteit van on-chain data. Aanvullende, unieke metadata kunnen ervoor zorgen dat sommige transacties zich onderscheiden van de massa, waardoor heuristische analyse mogelijk wordt. Dit is met name het geval wanneer deze metadata niet voor iedereen als verplicht wordt afgedwongen. Dit verplicht stellen voor iedereen zou echter onnodige ruimte aan de blockchain toevoegen en werd niet nagestreefd. En als een betalings-ID ooit om welke reden dan ook opnieuw zou worden gebruikt, zou het triviaal zijn om twee transacties als verbonden te koppelen. Dit gebeurde meestal met wisseldeposito's, en iedereen kon gemakkelijk transacties koppelen als zowel een storting op een beurs als van een bepaalde persoon. 

Ten tweede, vanuit een UX-perspectief creëren betalings-ID's een tweede stap waaraan cryptocurrency-gebruikers die van andere munten komen niet gewend zijn, en als ze het vergeten, veroorzaakt dit een enorme hoofdpijn voor de handelaar die deze transacties op een andere manier moet identificeren. Dit werd meestal gedaan door rechtstreeks met elke klant te spreken die de betalings-ID was vergeten in te voeren en andere identificerende informatie te bevestigen die alleen zij konden weten, zoals een combinatie van het bedrag, de verzenddatum en de transactie-ID.

Deze extra stap werd door velen over het hoofd gezien en het kwam op het punt dat sommige exchanges klanten geld in rekening brachten als hun geld handmatig moest worden opgehaald omdat ze een betalings-ID waren vergeten. Anderen knarsetandden en aten de extra ondersteuningskosten, maar niemand was er blij mee.

Er was één oplossing hiervoor, geïntegreerde adressen, die het adres en de betalings-ID samenvoegden tot één string, zodat het niet vergeten kon worden, maar de acceptatie was tamelijk zwak, ondanks de voordelen die verkopers zouden hebben gehad als ze het zouden opnemen. 

In een interessante gang van zaken kwamen subadressen binnen om de dag te redden. De mogelijkheid om grote hoeveelheden subadressen per hoofdadres te genereren en te identificeren welke transacties op welke subadressen binnenkwamen, stelde verkopers in staat om zich op een elegante manier te ontdoen van betalings-ID's, terwijl ze de volgende generatie Monero-technologie adopteerden. Sindsdien zijn de meeste exchanges en merchant tools overgeschakeld naar subadressen als primaire manier van transactie-identificatie.

Wat begon als een oplossing voor een privacyprobleem, veranderde in iets veel meer, dat een groot UX-probleem oploste voor zowel verkopers als klanten. Innovatie brengt meer innovatie voort, wat vaak kan leiden tot onverwachte overwinningen voor iedereen. Monero heeft dit keer op keer gezien en steekt veel energie in het innoveren van wat mogelijk is op de blockchain. Wie weet welke andere dingen we samen kunnen ontgrendelen?

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

  * [Hoe Monero Stealth Adressen Uw Identiteit Beschermen](/knowledge/monero-stealth-addresses/)

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