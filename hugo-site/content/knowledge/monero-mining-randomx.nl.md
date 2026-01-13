---
title: "Monero-Mining: Wat RandomX zo Speciaal Maakt"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Op 30 november 2019 had Monero zijn halfjaarlijkse hard fork, met als meest verwachte verandering een overstap van het oude PoW-algoritme, cryptonight, naar het volledig nieuwe, intern ontwikkelde algoritme, RandomX. De Monero-gemeenschap gelooft dat RandomX een grote stap is in de richting van egalitaire mining, maar laten we eerst dieper graven om te zien of dat het geval is.

## Doel

Om te beoordelen of RandomX een verbetering is, moeten we eerst begrijpen wat het doel van mining is. Mining beveiligt een blockchain tegen dubbele uitgaven via Nakamoto Consensus. De exacte fijne kneepjes van hoe het dit doet, vallen buiten het bereik van dit artikel, maar ze kunnen uit veel verschillende bronnen op het internet worden geleerd. Waar het om gaat is dat de beveiliging afkomstig is van hashes die worden gegenereerd door computers (miners), die met elkaar concurreren om de wiskundige oplossing te vinden die nodig is om nog een blok te maken. Terwijl ze dit doen, voegen ze nieuwe transacties toe aan de blockchain. In ruil voor hun werk (hashes) worden ze gecompenseerd met nieuw geslagen munten.   
  
Er zijn een aantal problemen die kunnen optreden bij deze opstelling, en ze hebben de juiste prikkels nodig om correct te werken, maar we gaan ons concentreren op een bepaald probleem dat zich zou kunnen voordoen. Als mining een wedstrijd zou moeten zijn, wat gebeurt er dan als een miner een voordeel behaalt?

## Achtergrond

Laten we het voor de context even hebben over mining-hardware. Miners gebruiken computers om het werk te doen, maar we weten allemaal dat niet elke computer gelijk gemaakt is. Sommige computers zijn krachtig genoeg om AI-netwerken of intense games uit te voeren, terwijl andere worstelen met zelfs eenvoudige taken. Deze verschillen in rekenkracht hebben ook invloed op de hash-snelheid, of de snelheid waarmee ze naar blokoplossingen zoeken.   
  
Maar zelfs deze verschillen tussen computers verbleken in vergelijking met de hash-snelheden van gespecialiseerde hardware, ook wel bekend als Application Specific Integrated Circuits (ASIC's), die gewone computers met vele ordes van grootte overtreffen.  
  
Laten we even de tijd nemen om te onderzoeken wat ASIC's zo krachtig maakt. Stelt u voor dat alle computers ergens in een bepaald spectrum vallen, dat varieert van veel dingen kunnen doen, maar niets goed, tot slechts één ding doen, maar het heel goed doen. CPU's en ASIC's bevinden zich aan weerszijden van dit spectrum.  
  
CPU's die zich in alle standaardcomputers zitten, bevinden zich aan het eerste uiteinde. Ze kunnen veel dingen, zoals surfen op het web, games spelen of video renderen, maar ze kunnen geen van deze dingen bijzonder goed. Maar deze flexibiliteit gaat ten koste van efficiëntie.  
  
ASIC's, aan de andere kant, kunnen maar één ding, maar doen het met een ongelooflijke snelheid. Ze kunnen maar één wiskundige functie uitvoeren, maar omdat ze al het andere kunnen negeren, zijn de prestatiewinsten astronomisch. Deze efficiëntie gaat echter ten koste van flexibiliteit, dus als de functie ook maar een klein beetje verandert – een voorbeeld is x + y = z verandert in 2x + y = z – dan zal de ASIC helemaal niet meer functioneren.   
  
Niet iedereen bezit een ASIC, maar iedereen bezit computers. Dit kan dus leiden tot een oneerlijk voordeel.

## Een leuke analogie

Als dit nog steeds verwarrend is, kan de volgende analogie misschien helpen. Stelt u een loterij voor waar elk uur duizend dollar wordt toegekend, en met deze loterij kun u uw eigen loten printen! U begint zoveel mogelijk tickets af te drukken op uw thuisprinter, die één ticket per seconde kan afdrukken. Na aftrek van elektriciteits- en inktkosten, ziet u dat u nog steeds winst kunt maken, zelfs als u maar eens in de zoveel weken de loterij wint.  
  
Na verloop van tijd breidt u uw bedrijf uit totdat u een hele ruimte voor printers heeft. 20 in totaal. Alles is in orde...tot op een noodlottige dag.  
  
Er is groot nieuws. Iemand heeft een nieuw soort printer uitgevonden. Het kan alleen loten printen. Het kan geen foto's of kantoordocumenten afdrukken, of dubbelzijdig afdrukken. Alleen loten. Maar het kan ze afdrukken met een snelheid van 1000 tickets per seconde. U kijkt in uw kleine printerkamer. 20 drukkers. U heeft 980 extra printers nodig om EEN van deze monsterprinters bij te houden, en wat als iemand er twee heeft...?  
  
U verlaat helaas het loterijspel omdat u de elektriciteits- en inktkosten niet langer kunt rechtvaardigen.  
  
Maar wacht! Een paar weken later is er meer nieuws! Het ontwerp van het ticket is gewijzigd. Nu staan de cijfers, die vroeger bovenaan stonden, nu onderaan. De nieuwe monsterprinters zijn zo inflexibel dat ze het niet kunnen. Ze konden alleen het vorige ontwerp maken. Het duurt niet lang voordat u weer vrolijk aan het printen bent. Tenminste, totdat iemand een nieuwe monsterprinter maakt voor het nieuwe ontwerp.

## RandomX

Waar past RandomX in al dit? Het probeert het voordeel van ASIC's te egaliseren door het maken van ASIC's erg moeilijk te maken. Het doet dit door miners te verplichten willekeurige code te maken en uit te voeren in plaats van hashing op basis van een algoritme.  
  
Het kan verwarrend zijn hoe dit eigenlijk iets helpt, dus laten we teruggaan naar onze printeranalogie. Weet u nog wat er gebeurde toen het ontwerp veranderde? De oude monsterprinters raken elke nacht verouderd en er moesten nieuwe worden ontwikkeld met het nieuwe ontwerp in gedachten. Wat zou er gebeuren als elk nieuw loterijprijskaartje voor elke nieuwe jackpot aan een nieuwe ontwerpstandaard zou moeten voldoen?   
  
Het maken van een nieuwe monsterprinter zou ongelooflijk moeilijk worden. U kunt niet meer op één ticketontwerp plannen. Aangezien het ontwerp willekeurig is, zouden de makers van monsterprinters kleurmogelijkheden moeten toevoegen, manieren om verschillende letters, randen en vormen af te drukken en meer. Kortom, de machine die ze uiteindelijk uitvonden, zou een standaard, gewone printer zijn. Net als die van iedereen.  
  
Door simpelweg deze willekeur in het ticketontwerp te implementeren, hebben we het grote voordeel van gespecialiseerde hardware aanzienlijk verminderd. RandomX doet hetzelfde, maar dan met mining.  
  
Op deze manier worden de voordelen van een select aantal welvarende mensen geminimaliseerd, alsof ze investeren in het creëren van "ASIC's" voor het minen van RandomX, die in feite alleen maar sterkere, betere CPU's zullen uitvinden, wat de hele wereld ten goede komt.   
  
Dit betekent dat de man met zijn 20 ticketprinters weer terug is in het spel. Hij heeft het misschien nog steeds moeilijker omdat deze rijke individuen nog steeds meer printers kunnen kopen dan hij, maar nu wordt hij tenminste niet overklast door simpelweg één machine. Hij is competitief op zijn eigen manier.  
  
Wetende dat zelfs de man competitief kan zijn in het minen van Monero, moedigen we iedereen aan om het eens te proberen, hetzij in de Monero GUI-portefeuille, die ondersteuning biedt voor solo-mining, of door de gemeenschap onderhouden software te downloaden. Het is gemakkelijk, competitief en voor iedereen toegankelijk.

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

  * [Waarom Monero beter is dan Dash, Zcash, Zcoin (zelfs met Lelantus), Grin en Bitcoin Mixers zoals Wasabi (bijgewerkt mei 2020)](/knowledge/why-monero-is-better)/