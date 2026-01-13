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