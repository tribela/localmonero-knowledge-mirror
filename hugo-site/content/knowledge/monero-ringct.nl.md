---
title: "Hoe RingCT Monero's Transactiebedragen verbergt"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
De privacy van Monero is niet afhankelijk van één enkel mechanisme dat, als het wordt verbroken, alle transacties zou onthullen, maar eerder van drie verschillende technologieën die samenwerken om holistische privacy te bieden en tegelijkertijd de zwakke punten van de andere onderdelen te compenseren. Deze benadering met drie punten bestaat uit [ringhandtekeningen](/knowledge/ring-signatures), RingCT en [stealth-adressen](/knowledge/monero-stealth-addresses). Deze drie technologieën verbergen respectievelijk de werkelijke output (afzender), hoeveelheid en ontvanger. Vandaag hebben we het over RingCT.

RingCT is misschien wel de meest technische van de drie, en kan moeilijk te begrijpen zijn, dus we zullen niet bespreken hoe het precies werkt, maar laten zien hoe het mogelijk is om een bedrag niet te weten te komen en er toch dingen over te kunnen bevestigen . En maakt u geen zorgen, we zullen zoals altijd genoeg voorbeelden gebruiken.

Laten we eerst eens kijken waarom het belangrijk is om iets over de bedragen te verifiëren. Waarom kunnen we ze niet gewoon volledig geheim houden? Het antwoord is dat er slimme manieren zijn waarop mensen uit het niets geld kunnen creëren als ze de kans krijgen. Hoe zou zoiets kunnen werken? Laten we naar een voorbeeld kijken.

Als u een item van uw vriend wilt kopen, en hij wil er tien dollar voor, dan begint u met tien dollar en begint hij met nul. Nadat u hem de tien dollar heeft gegeven, heeft hij tien dollar en u heeft nul. U begon met tien, en nu heeft hij er tien. Bij deze transactie is geen geld gecreëerd of vernietigd.

Met cryptocurrencies kan een slimme persoon tien dollar geven voor een item en in plaats van nul dollar wisselgeld te krijgen, kan hij twee dollar terugkrijgen. In plaats van dat 0 en 10 leiden tot 10 en 0 (of 10=10), is het nu 0 en 10 leidt tot 10 en 2 (of 10=12). Twee Monero is zojuist uit het niets ontstaan. U kunt u voorstellen dat als het individu zichzelf dit meerdere keren zou aandoen, ze in korte tijd een gigantisch fortuin zouden kunnen vergaren.

Met Bitcoin en anderen zou dit gemakkelijk te zien zijn. U kijkt naar de input die in een transactie gaat en de output die eruit komt en zorgt ervoor dat wat wordt verzonden gelijk is aan wat wordt ontvangen. Als deze bedragen zijn versleuteld en niet zichtbaar zijn, kan een gebruiker niet controleren of wat wordt verzonden en wat wordt ontvangen hetzelfde is.

In een poging om de privacy van Bitcoin te vergroten, creëerde Gregory Maxwell Confidential Transactions (CT), een nieuwe technologie die versleutelde bedragen mogelijk maakt, terwijl hij bewijst dat er tijdens het proces niets is gemaakt of vernietigd. Zoals met de meeste privacytechnologie, heeft het Bitcoin niet gehaald, maar Monero wilde het graag gebruiken. Er was slechts één probleem. De reeds geïmplementeerde technologie van ringhandtekeningen was onverenigbaar met het voorgestelde idee. Een van de toenmalige MRL-onderzoekers, Shen Noether, veranderde CT in RingCT, een versie van CT die compatibel was met ringhandtekeningen.

Nogmaals, de manier waarop dit werkt is vrij technisch en zou moeilijk uit te leggen zijn in een inleidend artikel. Voor de liefhebber van cryptografie die het echt wilt weten, zijn er tal van diepgaande artikelen op internet geschreven over de innerlijke werking van CT. Voor de rest van ons laat dit artikel zien hoe het mogelijk is om de bedragen te verbergen, maar toch te bewijzen dat er niets is gemaakt of vernietigd.

Stel dat Alice Bob geld wilde sturen. Alice stuurt 10 XMR naar Bob, die 10 XMR ontvangt. 10=10, dus hier is niets aan de hand. Maar Alice wil niet dat iemand weet hoeveel ze stuurt. Dus creëren zij en Bob een gedeeld geheim. Eigenlijk een nummer dat alleen zij twee kennen. Laten we zeggen dat dit getal 22 is. Nu vermenigvuldigt Alice 10 (wat ze werkelijk verzendt) met 22 om 220 te krijgen. Dit is het getal dat ze deelt met het netwerk.

De miners zelf kennen het geheime nummer niet. Als ze dat wel deden, zouden ze het nummer dat ze zien, kunnen delen door het geheime nummer en het echte bedrag ontvangen. Maar aangezien ze dat niet zien, kunnen ze dat niet. Wel zien ze dat Bob 220 krijgt. 220 verzonden. 220 ontvangen. 220 = 220. Op deze manier kan het netwerk verifiëren dat er geen Monero is gemaakt of vernietigd, en dat allemaal zonder het werkelijke bedrag te kennen dat Alice Bob heeft gestuurd.

Aangezien Bob het gedeelde geheime nummer kent, deelt hij het geld gewoon door 22 om het werkelijke bedrag te krijgen dat Alice heeft gestuurd, 10. Alice en Bob weten allebei hoeveel er is verzonden en hoeveel er is ontvangen, terwijl alle anderen krijgen een vals nummer.

Nogmaals, dit is niet de feitelijke manier waarop CT werkt, maar het geeft een idee van hoe zoiets mogelijk zou kunnen zijn. De echte manier omvat zaken als Pedersen-toezeggingen, twee verzonden bedragen (één gecodeerd bedrag naar de ontvanger en één toezeggingsbedrag naar het netwerk), en ... ja, het is al gemakkelijk in te zien hoe u daarin kunt verdwalen. 

Een ding om op te merken is echter dat hoewel RingCT het bedrag verbergt dat tussen twee partijen in een transactie is afgehandeld, het niet twee andere reeksen getallen verbergt.

De eerste zijn de coinbase-transacties. Als deze term u niet bekend is, betekent dit in feite de beloning die miners krijgen voor het vinden van het volgende blok. Dit nummer is niet verborgen. Iedereen kan zien hoeveel het protocol een miner heeft toegekend voor hun service. Op deze manier kan de huidige hoeveelheid bestaande Monero worden bepaald door alle coinbase-transacties bij elkaar op te tellen. Hun som is gelijk aan de huidige Monero die in omloop is.

Het tweede niet-verborgen getal is de vergoeding die aan de miners wordt betaald wanneer een gebruiker een transactie verzendt. De vergoedingen moeten duidelijk zijn, zodat miners kunnen weten aan wie ze prioriteit moeten geven. Dit is echter een manier waarop gebruikers hun privacy kunnen schaden, alsof iemand een unieke miner-vergoeding gebruikt elke keer dat ze een transactie verzenden (zoals 0,12345), dan kunnen hun transacties worden gekoppeld.

Afgezien van deze gevallen verbergt RingCT sinds 2017 Monero-bedragen, en onze collectieve privacy is daardoor des te sterker.

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