---
title: "Hoe Ring-handtekeningen de Resultaten van Monero Verdoezelen"
slug: "ring-signatures"
date: "2020-09-08"
image: "/images/rings.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero staat wijd en zijd bekend in de cryptowereld als de koning van de privacymunten. Hoewel iedereen weet dat Monero goede privacy biedt, begrijpen niet zo veel mensen precies hoe de privacy werkt.

Veel andere privacymunten publiceren vergelijkingsgrafiek-infographics, die de namen van de privacytechnologie van elke munt vermelden, en in de meeste bestempelen ze de technologie van Monero als RingCT, maar dit is slechts gedeeltelijk waar. Monero heeft eigenlijk een drieledige benadering van privacy. Eén technologie om de ontvanger van een transactie te verbergen, één om het verzonden bedrag te verbergen en één om de gebruikte uitvoer te verbergen. Dit zijn respectievelijk stealth-adressen, RingCT en ringhandtekeningen.

Deze drieledige aanpak houdt in dat als een van de technologieën niet werkt, de andere niet noodzakelijkerwijs hetzelfde lot ondergaan. Ringhandtekeningen zijn de zwakste schakel in het privacyschema; het woord zwak betekent hier het meest vatbaar voor heuristische aanvallen. Laten we even de tijd nemen om ze te verkennen, oké?

Zoals hierboven vermeld is, is het doel van ringhandtekeningen om een output die in een transactie wordt gebruikt, te verbergen. Maakt u geen zorgen als de 'input/output'-terminologie van cryptocurrency verwarrend voor u is. Het is eigenlijk niet zo ingewikkeld. Als u 'output' hoort, denk dan even na. Een van die dingen, niet meer zo gewoon, waarmee mensen vroeger betaalden. Net als een cheque kan het in elk bedrag worden genoteerd - $ 10, $ 32,50, enz. - en wordt het uitgewisseld tussen partijen die transacties uitvoeren. Voor cryptocurrencies hebben outputs deze functies.

Als iemand u 10 Monero betaalt, ontvangt u 10 XMR-output. Deze output heeft een waarde (10) en is wat uit de portefeuille van de afzender wordt gehaald, net zoals wanneer u voor een dienst betaalt, een rekening uw fysieke portemonnee verlaat en wordt gegeven aan de persoon van wie u koopt.

De manier waarop de uitvoer wordt verborgen, is door een ring (vandaar de naam) van lokuitgangen te construeren. Maar deze lokvogels zijn geen 'nep'-uitvoer'. Het zijn echte outputs uit het verleden van de blockchain die niets te maken hebben met de huidige transactie, maar voor een externe waarnemer kan elk van deze outputs er even waarschijnlijk uitzien als de echte. De grootte van de set lokoutputs, plus de echte, wordt de ringmaat genoemd, en die van Monero is momenteel elf. Er zijn dus tien lokaasuitgangen en één echte.

Waarom verhogen we dit aantal niet gewoon tot 100 of zelfs 1000? Hoe meer hoe beter, toch? Welnu, vanuit het oogpunt van privacy, maar er zijn andere dingen waarmee u rekening moet houden. Laten we teruggaan naar een fysiek voorbeeld om te zien wat ik bedoel. Als u een van uw dollarbiljetten tussen tien lokvogels zou willen verstoppen, zou u ongeveer elf dollar in uw portefeuille moeten hebben voor elke dollar die u wilt uitgeven. Een echte dollar en tien neppe. Dit wordt al behoorlijk omslachtig als u zelfs maar een paar dollar wilt uitgeven. Stelt u nu voor dat we het lokaasbedrag hebben verhoogd naar 1000. Voor elke dollar die u wilt uitgeven, zou u ongeveer 1001 dollar bij u moeten hebben. U zou een koffer moeten meenemen om één reep snoep te kopen! Het is belangrijk op te merken dat ringhandtekeningen niet helemaal op deze manier werken, de lokvogels zelf maken bijvoorbeeld geen deel uit van de handtekening, maar zijn alleen verwijzingen ernaar, maar we hopen dat deze analogie enigszins nuttig kan zijn bij het weergeven van de basisconcepten.< /p>

De lokvogels op de blockchain werken op dezelfde manier. Elke toegevoegde lokvogel verhoogt de tijd en verificatiekosten van de transactie. Elk knooppunt moet de volledige ringhandtekening voor elke transactie downloaden en elke ringhandtekening bevat de echte uitvoer, evenals de lokvogels. Niet alleen dat, maar het moet de wiskunde verifiëren dat ten minste één van deze uitgangen echt is, en de wiskundige verificatietijd neemt ook toe met elke lokvogel. Dit betekent dat we een goede middenweg moeten vinden, waarbij de ringmaat groot genoeg is om de werkelijke output adequaat te verdoezelen, zelfs tegen vele heuristische aanvallen, maar klein genoeg om de blockchain niet enorm te laten toenemen. Het is niet genoeg om een willekeurig nummer te kiezen, of om alleen de ringmaat te vergroten als we de handtekening kleiner maken (zoals bij CLSAG). De Monero-gemeenschap wil concreet, wiskundig bewijs voor welke ringmaat de beste afwegingen zijn. Een aantal te klein en de privacy zal niet sterk genoeg zijn tegen heuristische aanvallen. Te groot, en we krijgen misschien slechts marginale voordelen op het gebied van privacy, en onnodig lijden met betrekking tot schaalvergroting.

Nog een laatste ding om te vermelden. Sommige Monero-literatuur vereenvoudigt nog wel wat en zegt dat ringhandtekeningen de afzender verbergen, maar dit is niet helemaal waar, en het verschil is niet alleen belerend. Het verschil tussen de afzender (een mens) en een output (een factuur) is groot als het gaat om het behoud van privacy. Hoewel een output banden kan hebben met een afzender, is een output zelf niet gelijk aan een afzender. Dus zelfs als een ringhandtekening zou worden verbroken, hoeft deze niet noodzakelijkerwijs te worden gekoppeld aan de identiteit van een persoon, en zowel het bedrag als de ontvanger zijn nog steeds verborgen, waardoor de schade aan de privacy van alle partijen tot een minimum wordt beperkt.

Dat wil niet zeggen dat een gebroken ringhandtekening onbelangrijk is. Alle gelekte metadata zijn slecht en hebben het potentieel om meer informatie te onthullen dan we denken, vooral wanneer ze worden gebruikt in combinatie met andere metadata. Daarom doen we ons best om ervoor te zorgen dat de gekozen ringmaat academisch streng is voor de beslissing, dat het lekken van andere metadata tot een minimum wordt beperkt en dat de gebruiker standaard de best mogelijke acties ervaart.

Maar als de kans op een gebroken handtekening u nog steeds zorgen baart, dan is er ongelooflijk nieuws aan de horizon. De volgende generatie privacyprotocollen waaraan wordt gewerkt, zoals Triptych, Arcturus en Lelantus, hebben hele mooie mogelijkheden. In deze protocollen schaalt de grootte logaritmisch, niet lineair, naarmate de ringmaat toeneemt. Dit betekent dat we 100 lokvogels kunnen plaatsen, maar de gebruikte ruimte is dichter bij ringmaat 10 in de oude technologie. Dat is nogal een verschil en zal de privacy rondom aanzienlijk verbeteren.

In het kat-en-muisspel dat privacy heet, innoveert Monero continu om de concurrentie voor te blijven en de beste praktische privacy voor iedereen te garanderen.

De lokvogels op de blockchain werken op dezelfde manier. Elke toegevoegde lokvogel verhoogt de tijd en verificatiekosten van de transactie. Elk knooppunt moet de volledige ringhandtekening voor elke transactie downloaden en elke ringhandtekening bevat de echte uitvoer, evenals de lokvogels. Niet alleen dat, maar het moet de wiskunde verifiëren dat ten minste één van deze uitgangen echt is, en de wiskundige verificatietijd neemt ook toe met elke lokvogel. Dit betekent dat we een goede middenweg moeten vinden, waarbij de ringmaat groot genoeg is om de werkelijke output adequaat te verdoezelen, zelfs tegen vele heuristische aanvallen, maar klein genoeg om de blockchain niet enorm te laten toenemen. Het is niet genoeg om een willekeurig nummer te kiezen, of om alleen de ringmaat te vergroten als we de handtekening kleiner maken (zoals bij CLSAG). De Monero-gemeenschap wil concreet, wiskundig bewijs voor welke ringmaat de beste afwegingen zijn. Een aantal te klein en de privacy zal niet sterk genoeg zijn tegen heuristische aanvallen. Te groot, en we krijgen misschien slechts marginale voordelen op het gebied van privacy, en onnodig lijden met betrekking tot schaalvergroting.

Nog een laatste ding om te vermelden. Sommige Monero-literatuur vereenvoudigt nog wel wat en zegt dat ringhandtekeningen de afzender verbergen, maar dit is niet helemaal waar, en het verschil is niet alleen belerend. Het verschil tussen de afzender (een mens) en een output (een factuur) is groot als het gaat om het behoud van privacy. Hoewel een output banden kan hebben met een afzender, is een output zelf niet gelijk aan een afzender. Dus zelfs als een ringhandtekening zou worden verbroken, hoeft deze niet noodzakelijkerwijs te worden gekoppeld aan de identiteit van een persoon, en zowel het bedrag als de ontvanger zijn nog steeds verborgen, waardoor de schade aan de privacy van alle partijen tot een minimum wordt beperkt.

Dat wil niet zeggen dat een gebroken ringhandtekening onbelangrijk is. Alle gelekte metadata zijn slecht en hebben het potentieel om meer informatie te onthullen dan we denken, vooral wanneer ze worden gebruikt in combinatie met andere metadata. Daarom doen we ons best om ervoor te zorgen dat de gekozen ringmaat academisch streng is voor de beslissing, dat het lekken van andere metadata tot een minimum wordt beperkt en dat de gebruiker standaard de best mogelijke acties ervaart.

Maar als de kans op een gebroken handtekening u nog steeds zorgen baart, dan is er ongelooflijk nieuws aan de horizon. De volgende generatie privacyprotocollen waaraan wordt gewerkt, zoals Triptych, Arcturus en Lelantus, hebben hele mooie mogelijkheden. In deze protocollen schaalt de grootte logaritmisch, niet lineair, naarmate de ringmaat toeneemt. Dit betekent dat we 100 lokvogels kunnen plaatsen, maar de gebruikte ruimte is dichter bij ringmaat 10 in de oude technologie. Dat is nogal een verschil en zal de privacy rondom aanzienlijk verbeteren.

In het kat-en-muisspel dat privacy heet, innoveert Monero continu om de concurrentie voor te blijven en de beste praktische privacy voor iedereen te garanderen.

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