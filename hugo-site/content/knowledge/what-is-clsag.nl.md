---
title: "Hoe CLSAG de Efficiëntie van Monero Zal Verbeteren"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Als protocol bevindt Monero zich momenteel in een constante staat van innovatie. Gebruikmakend van onderzoek over zowel on-chain als off-chain oplossingen, zoekt de Monero-gemeenschap naar verbeterpunten om Monero meer privé, schaalbaard en toegankelijker voor iedereen te maken. Een van de meer recente innovaties is de vervanging van het koppelbare ringsignatuurschema, MLSAG, door een drop-in vervanging CLSAG, wat staat voor Concise Linkable Spontaneous Anonymous Group.

In eerste instantie zal de implementatie van CLSAG de meest voorkomende 2 input, 2 output transacties met 25% verminderen. We zullen ook een afname van 10% in de verificatietijd zien.

Maar wat is CLSAG precies? Wat doet het en hoe verschilt het van de oude versie, MLSAG? Laten we even de tijd nemen om onszelf te herinneren aan het waarom en hoe van ringhandtekeningen, zodat we dit concept beter kunnen begrijpen. Ring-handtekeningen maken niet-interactieve, niet-onderscheidbare getuige invoer mogelijk door gebruik te maken van door de ondertekenaar geselecteerde anonimiteit sets van eerdere outputs. In de termen van laymen, stelt het een gebruiker in staat om zijn outputs die in een transactie worden gebruikt te verbergen naast niet-gerelateerde outputs, en kunnen ze dit allemaal doen zonder dat iemand anders hoeft deel te nemen. Het enige wat u nodig heeft is een kopie van de blockchain. Elk van deze outputs lijken even waarschijnlijk als de daadwerkelijke output te zijn die wordt verzonden, waardoor metagegevens over de afzender worden verborgen. 

Dit veroorzaakt echter een klein probleem. Wat als een gebruiker een ringhandtekening zou maken met alle lokaas outputs? Hoe kan iemand weten dat de onbekende afzender niet bevoegd is om ze te verzenden? Zou deze gebruiker nepgeld kunnen uitgeven? Het antwoord is nee. De ringhandtekening bevat een methode om te bewijzen dat ten minste één van de outputs eigendom is van de onbekende afzender, zonder te onthullen welke het is. In feite zijn zowel CLSAG als MLSAG (hierna bekend als de SAG's) het deel van de ringsignatuur dat dit bewijst. Interessant genoeg bewijst het tegelijkertijd dat het bedrag van de transactie, hoewel verborgen achter vertrouwelijke transacties (RingCT), in evenwicht is. Dat de SAG's twee dingen bewijzen, dat één output eigendom is van iemand in de ring, en dat de transactie in evenwicht is, is belangrijk, en eigenlijk waar de omvang en verificatiebesparingen liggen. Als dit verwarrend wordt, maakt u geen zorgen, we komen binnenkort bij een leuke en gemakkelijk te begrijpen analogie. 

Het oude handtekeningschema, MLSAG (Multilayered Linkable Spontaneous Anonymous Group) bewijst de bovengenoemde twee dingen in een ringhandtekening, maar het doet het elk afzonderlijk. Het gebruik van afzonderlijke berekeningen voor ondertekenings- en toezeggingssleutels betekent tragere bewerkingen. Een moderne computer kan deze berekeningen in een kwestie van milliseconden doen, wat niet veel lijkt, en dat is het inderdaad voor één transactie ook niet. Maar als we kijken naar het enorm grote aantal transacties op de Monero-blockchain, en dat een vanaf nul gesynchroniseerd knooppunt ze allemaal moet downloaden en verifiëren, beginnen de bytes en milliseconden zich snel op te stapelen.

CLSAG combineert de wiskunde die nodig is om twee in één te bewijzen, en berekent beide dus tegelijkertijd, op een veilige manier. Wat betekent op een veilige manier? Nou, om dit op te helderen en hopelijk de hele zaak logischer te maken, laten we die beloofde leuke analogie onderzoeken. 

Stel dat u zowel naar de supermarkt als naar de bouwmarkt moet om twee verschillende dingen op te halen: voedsel en giftige schoonmaakmiddelen. U wilt niet dat ze zich vermengen, want als er een ongeluk gebeurt, zullen de chemicaliën op het voedsel morsen, waardoor ze oneetbaar worden. U besluit extra veilig te zijn en rijdt van uw huis naar de supermarkt, koopt het eten en rijdt dan weer terug naar huis. Pas nadat u het eten heeft uitgeladen, stapt u weer in de auto, rijdt u naar de bouwmarkt en weer terug naar huis met de chemicaliën. U heeft twee afzonderlijke reizen gemaakt om de veiligheid van alle aankopen te garanderen. Hoewel het inderdaad veilig is, is het ook inefficiënt. Dit vertegenwoordigt MLSAG, waar twee verschillende reeksen wiskunde worden opgeslagen en twee verschillende 'trips' worden gemaakt om ze te berekenen. 

U besluit echter dat u een snellere manier wilt om dit te doen. Het is een te grote tijdverspilling. Natuurlijk zal het een of twee keer doen uw leven niet wegnemen, maar als u dit keer op keer moet doen, beginnen de uren op te tellen. U begint u af te vragen of u in plaats daarvan één reis kunt maken. Van uw huis, naar de supermarkt, naar de bouwmarkt en weer terug naar huis. U kunt dan niet zomaar alles lukraak in uw auto gooien. Dat is niet veilig. In plaats daarvan kiest u verschillende plekken in uw auto voor verschillende dingen en zorgt u ervoor dat alles netjes op zijn plaats past. Door dit te doen, kunt u veilig één reis naar beide winkels maken en dingen uit elkaar houden. Dit vertegenwoordigt CLSAG. Er is nu slechts één set wiskunde opgeslagen in deze transactie om deze twee dingen te bewijzen, en het is zo gedaan dat ze elkaar niet hinderen. Er moet alsnog een reis worden gemaakt, maar u heeft het aantal drastisch geminimaliseerd.

Dit klinkt allemaal best spannend. Is het mogelijk dat we andere snelkoppelingen kunnen vinden, of dat er andere manieren zijn om tijd en ruimte te besparen? Het antwoord is ja en nee. Volgens de huidige MRL-onderzoekers is het waarschijnlijk niet mogelijk om de constructies van het SAG-type verder aan te passen voor een betere afmeting of snelheid; andere constructies zoals Arcturus, Omniring, RCT3 of Triptych produceren echter veel betere schaalvergroting en verificatievoordelen met behulp van verschillende wiskundige methoden. Elk van deze 'next-gen'-benaderingen van ondertekenaar-dubbelzinnige protocollen heeft echter zijn eigen compromissen in implementatiedetails en wordt actief onderzocht en onderzocht. 

Monero is tenslotte altijd aan het innoveren.

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

  * [Hoe Monero's Subadressen Identiteitskoppeling Voorkomen](/knowledge/monero-subaddresses/)

  * [Monero-Outputs uitgelegd](/knowledge/monero-outputs/)

  * [Praktische Tips van Monero voor Beginners](/knowledge/monero-best-practices/)

  * [Hoe Ring-handtekeningen de Resultaten van Monero Verdoezelen](/knowledge/ring-signatures/)

  * [Hoe Monero het Probleem met de Blokgrootte Dat Bitcoin Plaagt Heeft Opgelost](/knowledge/dynamic-block-size/)

  * [Waarom Monero een Staartemissie Heeft](/knowledge/monero-tail-emission/)

  * [Een Korte Geschiedenis van Monero](/knowledge/monero-history/)

  * [Wired Magazine heeft Ongelijk over Monero, Dit is Waarom](/knowledge/wired-article-debunked/)

  * [Top 15 Monero Mythen en Zorgen Ontkracht](/knowledge/monero-myths-debunked/)

  * [Hoe Dandelion++ de Oorsprong van de Transacties van Monero Privé Houdt](/knowledge/monero-dandelion/)

  * [Waarom Monero Open Source en Dedecentraliseerd Is](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero-Mining: Wat RandomX zo Speciaal Maakt](/knowledge/monero-mining-randomx/)

  * [Waarom Monero beter is dan Dash, Zcash, Zcoin (zelfs met Lelantus), Grin en Bitcoin Mixers zoals Wasabi (bijgewerkt mei 2020)](/knowledge/why-monero-is-better/)