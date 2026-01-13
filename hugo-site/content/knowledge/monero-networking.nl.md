---
title: "Wat Elke Monero Gebruiker Moet Weten Als het om Netwerken Gaat"
slug: "monero-networking"
date: "2020-11-11"
image: "/images/networking.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Het zou voor niemand als een verrassing moeten komen dat Monero, en inderdaad alle cryptocurrency, op het internet leven. En toch, ook al lijkt deze verklaring basaal en voor de hand liggend, staan velen niet stil bij de implicaties van wat dit betekent met betrekking tot hun privacy. Met andere woorden, er zijn dingen waar Monero wel en niet tegen kan beschermen, simpelweg vanwege de aard van het internet. Sommige van deze overwegingen zijn slechts ongemakken, terwijl andere veel ernstiger zijn in een scenario waarin absolute privacy vereist is. Laten we de tijd nemen om vertrouwd te raken met hoe Monero-gebruikers met elkaar omgaan op het netwerk en wat dit betekent voor hun privacy.

Om te beginnen: als een gebruiker geen toegang tot internet heeft, kan hij geen nieuwe blokken downloaden, geen transacties namens anderen verspreiden of zelf transacties verzenden. Een interessant ding om op te merken is dat een gebruiker met een volledig knooppunt, zonder internettoegang, offline een transactie kan opzetten die later kan worden verzonden. Dit komt omdat een ringhandtekening alleen een output van de blockchain nodig heeft om mee te verbergen. Een korte herinnering aan [ hoe ringhandtekeningen werken ](/knowledge/ring-signatures), het verbergt de echte output die een gebruiker verzendt tussen een verzameling niet-gelieerde outputs die uit het verleden zijn gekozen. Als de gebruiker toegang heeft tot deze outputs in de vorm van een volledig gedownloade blockchain (volledig knooppunt), dan kunnen ze de ringhandtekening maken van de eerdere outputs, en zodra de internetverbinding is hervat, de transactie doorgeven aan het netwerk.

Een gebruiker die een remote knooppunt gebruikt, kan dit niet doen, omdat hij bij het samenstellen van zijn ringhandtekening contact opneemt met het volledige knooppunt om outputs op te nemen in de ringhandtekening. Geen internet betekent dat ze dit knooppunt niet kunnen bereiken, dus ze hebben geen mogelijkheden om offline transacties te maken.

Voordat we verder gaan op enkele privacyoverwegingen, laten we een korte inleiding geven over hoe het internet als geheel werkt. Het internet is niets meer dan computers die verbinding maken met andere computers. Dat is het. Het blog dat u graag leest? Dit zijn slechts enkele bestanden die op de computer van iemand anders worden gehost. Op welke website leest u dit artikel (LocalMonero)? Dit zijn bestanden en codes die ergens op een computer worden gehost. Zelfs grote gekke sites werken op deze manier. Neem bijvoorbeeld YouTube. Het zijn alleen videobestanden die worden gehost op de gigantische computersystemen van Google, en u maakt er verbinding mee om de video naar uw eigen computer te downloaden, zodat u deze kunt bekijken.

Deze computers kunnen elkaar onderscheiden omdat elke computer die met het internet is verbonden een uniek identificatienummer krijgt, oftewel een IP-adres. Dit zijn doorgaans vier reeksen getallen gescheiden door punten, bijvoorbeeld: 172.66.35.7. Het is belangrijk om dit in gedachten te houden als we bedenken hoe Monero-informatie over het internet wordt verspreid. Monero is een peer-to-peer netwerk (P2P), wat inhoudt dat computers rechtstreeks met elkaar verbonden zijn in plaats van een tussenpersoon te gebruiken. Dus wanneer het volledige knooppunt van een gebruiker een nieuw ontdekt blok downloadt, downloaden ze het niet van een centrale server, maar van hun collega's. Het nadeel hiervan is dat, omdat gebruikers rechtstreeks met elkaar verbinden, ze elkaars IP-adressen kennen.

Nou? Wat is dan het probleem? Het is maar een getal toch? Niet helemaal. IP-adressen bevatten informatie over de gebruiker, zoals het land van herkomst en netwerkprovider, maar nog erger, internetserviceproviders (ISP's) kennen het IP-adres van elke persoon die hun diensten gebruikt. Dit betekent dat deze ISP's en degenen waarmee ze werken het internetverkeer van een gebruiker kunnen bekijken en, met behulp van een aantal slimme tactieken, kunnen ontdekken dat ze Monero gebruiken. Let voordat u bang wordt op de bewoordingen. Het enige wat deze snoopers kunnen doen, is zien dat een persoon verbinding maakt met andere knooppunten op het Monero-netwerk. Vanwege de privacytechnologie van Monero wordt er verder niets gelekt over het individu. Niet of ze een knooppunt draaien, of/wanneer ze transacties verzenden, en of er een transactie wordt verzonden, geen enkel deel van deze informatie wordt bekend gemaakt. Het enige wat deze ISP's kunnen zien, is dat een van hun gebruikers verbinding maakt met het Monero-netwerk.

Nu, voor sommige mensen, op sommige locaties, kan deze informatie alleen genoeg zijn om reputatieschade of vrijheid te schaden. Of misschien is het idee dat iemand inbreuk maakt op uw privacy en wat u op internet doet, om welke reden dan ook, niet acceptabel voor u. Deze personen worden aangemoedigd om alleen verbinding te maken met het Monero-netwerk via VPN's, Tor of I2P, dit zijn allemaal services die het IP-adres van een gebruiker verbergen voor anderen en dus ook verbergen wat een gebruiker doet voor zijn ISP. De verschillen tussen deze services vallen buiten het bereik van dit artikel, maar er zijn tal van artikelen van hoge kwaliteit over het onderwerp geschreven, dus bezorgde gebruikers worden aangemoedigd om hier meer over te lezen! 

De rest van ons denkt misschien dat het niet zo'n groot probleem is als anderen weten dat we verbonden zijn met het Monero-netwerk. De daadwerkelijke inhoud van onze transacties, of als we er een verzenden, is tenslotte verborgen voor het publiek, dus wat kan het kwaad? Hoewel dit waar kan zijn, worden gebruikers aangemoedigd om te overwegen dat de belangrijkste aantrekkingskracht van cryptocurrencies hun eigen bank is. Wanneer u uw privésleutel bezit en er iets mee gebeurt, kan niemand u helpen uw verloren geld terug te vorderen.

Uw eigen bank zijn betekent niet alleen nadenken over uw digitale veiligheid, maar ook over uw fysieke veiligheid. Het zou heel goed kunnen dat de kennis van een persoon die verbinding maakt met het Monero-netwerk ongewenste aandacht kan trekken, niet noodzakelijkerwijs van grootschalige actoren zoals natiestaten, maar kleinere actoren met egoïstische belangen, zoals hackers die op een gemakkelijk wijze geld willen verdienen. Er zijn inderdaad talloze verhalen over de hele crypto-ruimte van dergelijke scenario's die daadwerkelijk plaatsvinden. 

Dit artikel is niet bedoeld om angst aan te jagen of u bang te maken, maar gebruikers aan te moedigen om onderzoek te doen naar welke methoden van bescherming voor internetsurfen voor hen geschikt zijn. Het goede nieuws is dat deze vaardigheden ook zullen worden overgedragen op algemeen internetgebruik, en niet alleen op Monero-gebruik, en in onze wereld die steeds meer via het internet verbonden is, kan een slimme gebruiker niet de fout in gaan door de juiste kennis en vaardigheden te verzamelen om veilig te blijven, en daadwerkelijk hun eigen bank zijn. 

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

  * [Hoe RingCT Monero's Transactiebedragen verbergt](/knowledge/monero-ringct/)

  * [Hoe Monero Stealth Adressen Uw Identiteit Beschermen](/knowledge/monero-stealth-addresses/)

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