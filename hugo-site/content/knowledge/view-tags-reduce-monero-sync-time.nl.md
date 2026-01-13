---
title: "Weergave tags: Hoe één byte de synchronisatietijden van de Monero portefeuille met meer dan 40% vermindert"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Een van de meest voorkomende klachten over het dagelijkse gebruik van Monero is de tijd die het kan kosten om een portefeuille te synchroniseren voordat je Monero kunt verzenden. Gelukkig hebben ontwikkelaars en onderzoekers in de Monero-gemeenschap een briljante manier gevonden om de tijd die u nodig heeft om uw portefeuille te synchroniseren met meer dan 40% te verminderen zonder extra blockchain-bloat, kosten, enz. 

Voer "view tags" in, een toevoeging van één byte aan de gegevens van elke transactie - komt naar Monero in de volgende netwerkupgrade!

## Waarom is de synchronisatie van de portefeuille van Monero langzamer dan die van Bitcoin?

## Waarom is de synchronisatie van de portefeuille van Monero langzamer dan die van Bitcoin?

Een van de eerste vragen die we moeten beantwoorden om de behoefte aan een oplossing zoals weergave tags beter te begrijpen, is waarom de synchronisatie van de portefeuille van Monero langzamer is dan cryptocurrencies zoals Bitcoin.

In Bitcoin, aangezien alle transacties niet privé zijn en de munten die worden uitgegeven, de bedragen en de betrokken adressen in de keten onthuld worden, kunnen Bitcoin-portefeuilles eenvoudig zoeken naar ongebruikte transactie-outputs (UTXO's) of gebruikte adressen voor een bepaalde portefeuille, door snel de blockchain te scannen op alleen UTXO's die eigendom zijn van die adressen om erachter te komen welke munten bij uw portefeuille horen en kunnen worden uitgegeven. 

In Monero behouden alle transacties echter de privacy van de gebruiker door de afzender, ontvanger en bedragen die bij elke transactie betrokken zijn, te verbergen. Hoewel deze privacy van vitaal belang is voor de bescherming van de gebruikers van het netwerk, wordt ook de synchronisatie van de portefeuille langzamer. In Monero moet uw portefeuille elke transactie-output (TXO) die op het netwerk bestaat, vergelijken met de privésleutels van uw portefeuille.

Deze vergelijking omvat veel complexe wiskunde en cryptografie om te valideren dat een output echt van u is, aangezien alle bedragen, adressen en bekende uitgegeven outputs (of munten) on-chain verborgen zijn in Monero.

## Wat zijn weergavetags?

## Wat zijn weergavetags?

Als poging om de synchronisatietijd voor Monero-portefeuilles te verkorten, bedacht [een onderzoeker genaamd UkoeHB een nieuwe aanpak](https://github.com/monero-project/research-lab/issues/73) – voeg een 1-byte "tag" toe aan elke transactie met behulp van een gedeeld geheim dat alleen bekend is naar de afzender en ontvanger van die transactie.

Dit gedeelde geheim wordt gegenereerd door de afzender met behulp van het adres dat hem door de ontvanger is verstrekt en vereist geen actieve samenwerking tussen de afzender en de ontvanger. De eerste byte (of het eerste teken) van dit gedeelde geheim wordt vervolgens toegevoegd aan de transactiegegevens wanneer deze wordt gepubliceerd op het Monero-netwerk.

Als een van de deelnemers aan die transactie zijn portefeuille achteraf wil synchroniseren met de Monero-blockchain, in plaats van alle complexe wiskunde en cryptografie voor elke TXO op het netwerk uit te voeren, kan de portefeuille nu gewoon controleren op dat veld van 1 byte in elke transactie en voer dan pas de tijdrovende verificatie uit op transacties die deze tag hebben – 1/256 TXO's op het netwerk, om precies te zijn!

Deze tag onthult geen informatie over de transactie aan externe kijkers, voegt slechts 1 byte (een te verwaarlozen hoeveelheid) toe aan transactiegroottes, en stelt ons toch in staat de synchronisatietijden met meer dan 40% te verminderen door de nodige complexe verificaties te verminderen!

## Weergave tags: een vereenvoudigd voorbeeld

## Weergave tags: een vereenvoudigd voorbeeld

Stelt u voor dat u 4.096 dozen in een kamer hebt staan, waarvan er maar 5 van jou zijn. De dozen zijn aan de buitenkant allemaal niet van elkaar te onderscheiden, en de enige manier om te zien of een doos voor u is, is door hem te openen en een tijdrovend wiskundig probleem op te lossen dat binnenin is opgeschreven om er zeker van te zijn dat hij van u is. 

Stelt u nu voor dat u besluit om de persoon die u die 5 dozen stuurt een speciale code te laten genereren met behulp van uw adres, en dan alleen het eerste teken van die gegenereerde code op de buitenkant van elke doos te zetten die naar u wordt verzonden. Alle anderen doen hetzelfde voor hun dozen (om ervoor te zorgen dat alle dozen nog steeds niet van elkaar te onderscheiden zijn), maar nu kunt u gewoon naar de code van één teken op de buitenkant van de doos kijken en alleen die dozen openen die dat teken erop hebben.

Terwijl andere dozen overeenkomen met uw code, zelfs sommige die niet van u zijn, is het aantal dozen dat u nodig heeft om een wiskundig probleem te openen en op te lossen nu slechts 16 (1/256 dozen!) in plaats van alle 4.096. 

Nu opent u die 16 dozen, lost u de rekensommetjes op en houdt u de 5 dozen die echt bij u horen uit die groep!

## Wanneer zullen weergavetags beschikbaar zijn in Monero?

## Wanneer zullen weergavetags beschikbaar zijn in Monero?

Weergave tags zijn een van de functies die momenteel zijn gepland voor opname in de [aankomende netwerkupgrade](https://github.com/monero-project/meta/issues/630), en zouden ergens dit voorjaar moeten worden vrijgegeven. De community [ heeft 23.3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) opgehaald (op het moment van schrijven) om de ontwikkeling en implementatie van weergave tags te stimuleren. voltooid door j-berman in samenwerking met recensenten en onderzoekers.

Zodra de weergavetags door het netwerk zijn afgedwongen, zullen alle transacties die na de netwerkupgrade worden verzonden, profiteren van de drastisch verbeterde portefeuillesynchronisatietijd. U hoeft niets speciaals te doen om weergave tags te gaan gebruiken, uw favoriete Monero portefeuille gaat ze gewoon automatisch gebruiken na de netwerkupgrade!

## Hoe kan ik meer leren?

## Hoe kan ik meer leren?

Als dit uw nieuwsgierigheid naar weergavetags heeft gewekt, kijk dan hieronder voor enkele aanvullende links die er dieper op ingaan:

  * [Scantijden verkorten met 'view tag' van 1 byte per uitvoer ](https://github.com/monero-project/research-lab/issues/73)
  * [Voeg weergavetags toe aan output om de scantijd van de portefeuille te verkorten](https://github.com/monero-project/monero/pull/8061)

Verder lezen

  * [Hoe Monero op unieke wijze circulaire economieën mogelijk maakt](/knowledge/monero-circular-economies)/

  * [Monero's ringhandtekeningen versus CoinJoin zoals in Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Waarom (en hoe!) u uw eigen sleutels moet bezitten](/knowledge/hold-your-keys)/

  * [Bijdragen aan Monero](/knowledge/contributing-to-monero)/

  * [Hoe externe knooppunten de privacy van Monero beïnvloeden](/knowledge/remote-nodes-privacy)/

  * [Hoe Monero hard forks gebruikt om het netwerk te upgraden](/knowledge/network-upgrades)/

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

  * [Monero-Mining: Wat RandomX zo Speciaal Maakt](/knowledge/monero-mining-randomx)/

  * [Waarom Monero beter is dan Dash, Zcash, Zcoin (zelfs met Lelantus), Grin en Bitcoin Mixers zoals Wasabi (bijgewerkt mei 2020)](/knowledge/why-monero-is-better)/

Verder lezen