---
title: "Monero's ringhandtekeningen versus CoinJoin zoals in Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Naarmate de privacytools van Bitcoin meer aandacht en gebruik hebben gekregen, komen ze onder meer regelgevend toezicht te staan. Dit onderzoek heeft geleid tot een [recente aankondiging](https://twitter.com/wasabiwallet/status/1503091503207432193) van een Bitcoin-privacytool, Wasabi Wallet, dat ze zullen beginnen met het censureren en weigeren van inkomende inputs van mixen die ze als ongeoorloofd beschouwen of tegen hun ToS ingaan, en dat ze een bedrijf zullen betalen om kettinganalyse van inkomende mixdeelnemers te "doorlichten". 

Het gebruik van CoinJoin-transacties om de bron van fondsen in Bitcoin te verdoezelen, is al vele jaren de kern van Bitcoin-privacy, en de problemen en risico's die inherent zijn aan het gebruik ervan zijn een aantal van de kernproblemen die de ringhandtekeningen van Monero corrigeren en voorkomen .

In deze blogpost gaan we kort in op een vergelijking van CoinJoin- en ringhandtekeningen, en waarom de benadering die in Monero wordt gehanteerd, leidt tot meer weerstand tegen censuur, meer privacy en minder gedoe voor gebruikers.

## Wat is een CoinJoin-transactie?

## Wat is een CoinJoin-transactie?

Aangezien alle transacties in Bitcoin volledig transparant zijn - waarbij de afzender, ontvanger en bedragen worden onthuld - moeten gebruikers extra maatregelen nemen om hun privacy te beschermen tegen eerdere afzenders en toekomstige ontvangers van hun geld, anders riskeren ze censuur, toezicht of diefstal van geld via fysiek geweld.

De beste oplossing voor privacy op Bitcoin is tegenwoordig een tool genaamd [“CoinJoin”](https://bitcoiner.guide/qna/coinjoin/), waar 2 of meer gebruikers samenwerken (meestal via een gecentraliseerde coördinator) om een speciale transactie te creëren die het moeilijk maakt voor externe waarnemers om de inputs met de outputs te verbinden. Elke deelnemer communiceert om gezamenlijk de transactie op te bouwen zonder hun geld uit handen te geven, en ontvangt aan het einde een output waarvan de voorgeschiedenis nu onduidelijk (of versluierd) is voor externe waarnemers. 

Dit doorbreekt de geschiedenis van specifieke UTXO's, waardoor Bitcoin-gebruikers wat voorwaartse geheimhouding kunnen krijgen bij transacties. CoinJoin (zoals geïmplementeerd in Wasabi Wallet en Samourai Wallet, de twee meest gebruikte CoinJoin-tools voor Bitcoin) heeft echter een paar grote nadelen:

  * Aangezien CoinJoin-transacties volledig opt-in zijn en actieve deelname vereisen, laat elke deelnemer automatisch zien dat hij meer privacy zoekt dan die van "normale" Bitcoin-gebruikers, waardoor ze mogelijk worden uitgepikt en problemen veroorzaken bij het uitgeven van geld bij veel gereguleerde beurzen of entiteiten. Gebruikers kunnen niet ontkennen dat ze hebben deelgenomen aan een CoinJoin-transactie.
  * Om andere CoinJoin-partners te vinden, gebruiken de meeste benaderingen van CoinJoin (inclusief Wasabi Wallet) een gecentraliseerde coördinator die deelnemers met elkaar verbindt en hen helpt te communiceren om een goede CoinJoin-transactie op te bouwen. Deze gecentraliseerde coördinator heeft nooit de autonomie over het geld van de gebruiker, maar krijgt wel uitgebreid inzicht in de transacties die hij coördineert, kan binnenkomende inputs censureren (zoals in het geval van Wasabi Wallet) en kan onder druk worden gezet om informatie over CoinJoin-deelnemers te verzamelen of te delen.
  * Gebruikers met grote bedragen of fondsen aan CoinJoin kunnen vaak uren (of zelfs dagen!) wachten om genoeg deelnemers te vinden om mee te doen aan CoinJoin, wat leidt tot grote vertragingen vanaf het moment dat een gebruiker geld ontvangt tot wanneer ze deze privé kunnen uitgeven. 
  * De privacy die wordt geboden door een CoinJoin-transactie neemt in de loop van de tijd af naarmate andere deelnemers geld uitgeven of hun output koppelen aan hun identiteit via KYC-uitwisselingen, handelaars die een ID vereisen, enz. Dit betekent dat gebruikers beter hun geld constant in CoinJoin-transacties kunnen laten draaien om hun anonimiteit set zo 'vers' als mogelijk te houden (oftewel een "menigte om zich in te verstoppen"). 
  * Bij de meeste benaderingen van CoinJoin moeten deelnemers een UTXO van vaste grootte (d.w.z. 0,1 BTC) gebruiken om het moeilijker te maken om inputs en outputs van CoinJoin-transacties met elkaar te verbinden. Dit leidt tot hogere vergoedingen (meer afzonderlijke transacties nodig per grote invoer), meer "toxische verandering" (fondsen die niet kunnen worden besteed zonder ernstige risico's voor de privacy), en kan voorkomen dat kleinere gebruikers zich kunnen mengen in de mix als ze niet het minimaal vereiste saldo hebben. 

## Hoe lossen ringhandtekeningen deze problemen op?

## Hoe lossen ringhandtekeningen deze problemen op?

Aangezien we al [ diep hebben gekeken naar wat ringhandtekeningen zijn in het verleden ](/knowledge/ring-signatures), zal ik in deze blogpost niet in detail gaan op de technische aspecten van hoe ze werken. In plaats daarvan zullen we kijken hoe de aanpak van Monero de problemen met CoinJoin oplost die hierboven zijn besproken.

> CoinJoin is opt-in en vereist deelname

CoinJoin is opt-in en vereist deelname

Monero's ringhandtekeningen zijn een kernkenmerk van het privacyprotocol en _elke_ transactie op het netwerknaakt er gebruik van. Dit betekent dat de transacties van geen enkele gebruiker opvallen door het zoeken naar meer privacy dan "normale" Monero-gebruikers, en alle gebruikers krijgen aannemelijke ontkenning dat ze geld hebben uitgegeven aan een bepaalde transactie. Aangezien het geld dat een gebruiker uitgeeft niet coördineert of deelneemt aan de lokaas inputs in een transactie, kunnen gebruikers die eigenaar zijn van inputs die toch toevallig als lokmiddelen zijn geselecteerd, eerlijk aangeven dat ze niet hebben deelgenomen aan die transactie, waardoor hun privacy wordt versterkt. 

> Gebruik van een gecentraliseerde coördinator

Gebruik van een gecentraliseerde coördinator

Aangezien de ringhandtekeningen van Monero volledig niet-gecoördineerd zijn en alleen de echte gelduitgever nodig hebben om de transactie te creëren, is er geen centrale coördinator nodig in Monero. Dit zorgt ervoor dat _niemand_ uw toegang tot privacy in Monero kan ontzeggen, en er is geen gecentraliseerde entiteit die onder druk kan worden gezet, geen gemakkelijke Sybil-aanvallen op liquiditeit, enz. Zolang u transactie de juiste kosten betaalt, krijgt u ongecensureerde toegang tot privacy, veiligheid en anonimiteit in Monero.

> CoinJoin vereist liquiditeit

CoinJoin vereist liquiditeit

De "liquiditeit" die beschikbaar is voor iedereen die Monero uitgeeft om als lokmiddelen te gebruiken, is altijd de totale set outputs in de keten, dus er is nooit een tekort aan lokmiddelen om u met Monero in te verstoppen. Iemand die Monero wilt uitgeven, kan dit ongeveer 20 minuten na ontvangst van het geld doen en hoeft geen extra stappen te ondernemen om sterke privacy in Monero te verkrijgen.

> CoinJoin-privacy verslechtert na verloop van tijd

CoinJoin-privacy verslechtert na verloop van tijd

Aangezien de uitvoer van Monero nooit door het netwerk wordt uitgegeven, is de privacy die wordt geboden door ringhandtekeningen veel minder vatbaar voor verslechtering in de loop van de tijd. Een gebruiker hoeft niet constant outputs te draaien in Monero, en buiten uiterst zeldzame omstandigheden verliest hij na verloop van tijd geen privacy.

Als een gebruiker de lokaas die met een output wordt gebruikt echter wil "verversen", kan hij het geld gewoon naar zichzelf terugsturen en het zoals gewoonlijk ~ 20 minuten later uitgeven. 

> CoinJoin vereist meestal invoer met een vaste grootte 

CoinJoin vereist meestal invoer met een vaste grootte 

Aangezien bedragen in elke transactie worden verborgen met behulp van ["Vertrouwelijke transacties"](/knowledge/monero-ringct) (een onderdeel van "RingCT"), kunnen de lokmiddelen die bij een bepaalde transactie worden gebruikt van elke grootte zijn. Er is geen reden om u zorgen te maken over op bedragen gebaseerde heuristiek in Monero, dus transacties zijn veel eenvoudiger te bouwen en kunnen lokmiddelen gebruiken vanaf elk moment en van elk bedrag op de Monero-blockchain.

## Hoe kan ik meer leren?

## Hoe kan ik meer leren?

Als u nieuwsgierig bent en ringhandtekeningen of CoinJoin-transacties beter wilt begrijpen, bekijk dan de onderstaande links voor goede plekken om van start te gaan:

  * [Hoe beltonen de output van Monero verdoezelen](/knowledge/ring-signatures)
  * [Ringhandtekening - Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [CoinJoin-overzicht](https://6102bitcoin.com/coinjoin-overview/)

Verder lezen

  * [Hoe Monero op unieke wijze circulaire economieën mogelijk maakt](/knowledge/monero-circular-economies)/

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

  * [Monero-Mining: Wat RandomX zo Speciaal Maakt](/knowledge/monero-mining-randomx)/

  * [Waarom Monero beter is dan Dash, Zcash, Zcoin (zelfs met Lelantus), Grin en Bitcoin Mixers zoals Wasabi (bijgewerkt mei 2020)](/knowledge/why-monero-is-better)/

Verder lezen