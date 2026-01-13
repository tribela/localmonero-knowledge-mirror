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

Een van de eerste vragen die we moeten beantwoorden om de behoefte aan een oplossing zoals weergave tags beter te begrijpen, is waarom de synchronisatie van de portefeuille van Monero langzamer is dan cryptocurrencies zoals Bitcoin.

In Bitcoin, aangezien alle transacties niet privé zijn en de munten die worden uitgegeven, de bedragen en de betrokken adressen in de keten onthuld worden, kunnen Bitcoin-portefeuilles eenvoudig zoeken naar ongebruikte transactie-outputs (UTXO's) of gebruikte adressen voor een bepaalde portefeuille, door snel de blockchain te scannen op alleen UTXO's die eigendom zijn van die adressen om erachter te komen welke munten bij uw portefeuille horen en kunnen worden uitgegeven. 

In Monero behouden alle transacties echter de privacy van de gebruiker door de afzender, ontvanger en bedragen die bij elke transactie betrokken zijn, te verbergen. Hoewel deze privacy van vitaal belang is voor de bescherming van de gebruikers van het netwerk, wordt ook de synchronisatie van de portefeuille langzamer. In Monero moet uw portefeuille elke transactie-output (TXO) die op het netwerk bestaat, vergelijken met de privésleutels van uw portefeuille.

Deze vergelijking omvat veel complexe wiskunde en cryptografie om te valideren dat een output echt van u is, aangezien alle bedragen, adressen en bekende uitgegeven outputs (of munten) on-chain verborgen zijn in Monero.

## Wat zijn weergavetags?

Als poging om de synchronisatietijd voor Monero-portefeuilles te verkorten, bedacht [een onderzoeker genaamd UkoeHB een nieuwe aanpak](https://github.com/monero-project/research-lab/issues/73) – voeg een 1-byte "tag" toe aan elke transactie met behulp van een gedeeld geheim dat alleen bekend is naar de afzender en ontvanger van die transactie.

Dit gedeelde geheim wordt gegenereerd door de afzender met behulp van het adres dat hem door de ontvanger is verstrekt en vereist geen actieve samenwerking tussen de afzender en de ontvanger. De eerste byte (of het eerste teken) van dit gedeelde geheim wordt vervolgens toegevoegd aan de transactiegegevens wanneer deze wordt gepubliceerd op het Monero-netwerk.

Als een van de deelnemers aan die transactie zijn portefeuille achteraf wil synchroniseren met de Monero-blockchain, in plaats van alle complexe wiskunde en cryptografie voor elke TXO op het netwerk uit te voeren, kan de portefeuille nu gewoon controleren op dat veld van 1 byte in elke transactie en voer dan pas de tijdrovende verificatie uit op transacties die deze tag hebben – 1/256 TXO's op het netwerk, om precies te zijn!

Deze tag onthult geen informatie over de transactie aan externe kijkers, voegt slechts 1 byte (een te verwaarlozen hoeveelheid) toe aan transactiegroottes, en stelt ons toch in staat de synchronisatietijden met meer dan 40% te verminderen door de nodige complexe verificaties te verminderen!

## Weergave tags: een vereenvoudigd voorbeeld

Stelt u voor dat u 4.096 dozen in een kamer hebt staan, waarvan er maar 5 van jou zijn. De dozen zijn aan de buitenkant allemaal niet van elkaar te onderscheiden, en de enige manier om te zien of een doos voor u is, is door hem te openen en een tijdrovend wiskundig probleem op te lossen dat binnenin is opgeschreven om er zeker van te zijn dat hij van u is. 

Stelt u nu voor dat u besluit om de persoon die u die 5 dozen stuurt een speciale code te laten genereren met behulp van uw adres, en dan alleen het eerste teken van die gegenereerde code op de buitenkant van elke doos te zetten die naar u wordt verzonden. Alle anderen doen hetzelfde voor hun dozen (om ervoor te zorgen dat alle dozen nog steeds niet van elkaar te onderscheiden zijn), maar nu kunt u gewoon naar de code van één teken op de buitenkant van de doos kijken en alleen die dozen openen die dat teken erop hebben.

Terwijl andere dozen overeenkomen met uw code, zelfs sommige die niet van u zijn, is het aantal dozen dat u nodig heeft om een wiskundig probleem te openen en op te lossen nu slechts 16 (1/256 dozen!) in plaats van alle 4.096. 

Nu opent u die 16 dozen, lost u de rekensommetjes op en houdt u de 5 dozen die echt bij u horen uit die groep!

## Wanneer zullen weergavetags beschikbaar zijn in Monero?

Weergave tags zijn een van de functies die momenteel zijn gepland voor opname in de [aankomende netwerkupgrade](https://github.com/monero-project/meta/issues/630), en zouden ergens dit voorjaar moeten worden vrijgegeven. De community [ heeft 23.3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) opgehaald (op het moment van schrijven) om de ontwikkeling en implementatie van weergave tags te stimuleren. voltooid door j-berman in samenwerking met recensenten en onderzoekers.

Zodra de weergavetags door het netwerk zijn afgedwongen, zullen alle transacties die na de netwerkupgrade worden verzonden, profiteren van de drastisch verbeterde portefeuillesynchronisatietijd. U hoeft niets speciaals te doen om weergave tags te gaan gebruiken, uw favoriete Monero portefeuille gaat ze gewoon automatisch gebruiken na de netwerkupgrade!

## Hoe kan ik meer leren?

Als dit uw nieuwsgierigheid naar weergavetags heeft gewekt, kijk dan hieronder voor enkele aanvullende links die er dieper op ingaan:

  * [Scantijden verkorten met 'view tag' van 1 byte per uitvoer ](https://github.com/monero-project/research-lab/issues/73)
  * [Voeg weergavetags toe aan output om de scantijd van de portefeuille te verkorten](https://github.com/monero-project/monero/pull/8061)

Verder lezen