---
title: "Waarom Monero beter is dan Dash, Zcash, Zcoin (zelfs met Lelantus), Grin en Bitcoin Mixers zoals Wasabi (bijgewerkt mei 2020)"
slug: "why-monero-is-better"
date: "Sat Feb 01"
image: "/images/why-monero.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Niet alle op privacy gerichte munten kunnen 100% privacy, onvindbaarheid, veiligheid en fungibiliteit bieden in een 100% gedecentraliseerde munt met een betrouwbare opzet. Hier vindt u wat deze kenmerken zijn en waarom ze belangrijk zijn:

Privé
    Uw financiën zijn niet zichtbaar voor het publiek. Iemand die naar de blockchain van de munt kijkt, kan niet zien hoeveel geld u heeft.
Onvindbaar
    De munten zijn niet te traceren via blockchain analyse of controle.
Veilig
    Alle transacties zijn versleuteld en de portefeuille die uw geld bevat, is ook versleuteld.
Vervangbaar
    Alle munten zijn gelijk en hebben dezelfde waarde.
Gedecentraliseerd
    Alle knooppunten (een knooppunt is een lopende instantie van de blockchain van de munt) van het netwerk zijn gelijk. Er is geen superklasse van knooppunten die meer invloed of controle hebben over transacties of het systeem dan andere knooppunten.

## Munt analyse

Hier is een analyse van bekende cryptocurrencies die anonimiteit en/of onvindbaarheid claimen als hun belangrijkste onderscheidende factor. Bitcoin zelf valt niet binnen het bereik van deze analyse, aangezien er nooit is beweerd dat het anoniem is.

Deze site is gemaakt door gebruikers van Monero. Er was een tijd dat we geen Monero-gebruikers waren, maar ons zorgen maakten over financiële privacy. We hebben de munten onderzocht die beweerden privé te zijn en deze pagina is het resultaat van ons onderzoek. Daarom hebben we Monero verkozen boven de rest. Dus als we bevooroordeeld lijken, zijn we dat ook, maar we geloven dat die vooringenomenheid gebaseerd is op feiten die u hieronder kunt lezen en zelf kunt verifiëren.

### Overzicht

Selecteer een logo om naar de analyse van die munt te gaan.

| Privé| Onvindbaar| Veilig| Vervangbaar| Gedecentraliseerd  
---|---|---|---|---|---  
Monero| Ja| Ja| Ja| Ja| Ja  
DASH| Nee| Nee| Ja| Nee| Nee  
Zcash| Nee| Niet helemaal| Ja| Nee| Nee  
| Ja| Ja| Ja| Ja| Nee  
| Soms| Nee| Ja| Onzeker| Ja  
Bitcoin mixers| Nee| Nee| Ja| Nee| Soms  
  
### Monero

Privé
    Monero gebruikt een cryptografisch verantwoord systeem waarmee u geld kunt verzenden en ontvangen zonder dat uw transacties publiekelijk zichtbaar zijn op de blockchain (het gedistribueerde grootboek van transacties). Dit zorgt ervoor dat uw aankopen, bonnetjes en andere overschrijvingen standaard **privé blijven**. De afzender, ontvanger en het bedrag van de transactie zijn allemaal privé. Sommige munten hebben een "rijke lijst" waarmee iedereen kan zien welk account de meeste munten heeft. Omdat Monero privé is, kan er geen [ Monero-rijke lijst ](http://moneroblocks.info/richlist) bestaan.
Onvindbaar
    Door gebruik te maken van ringhandtekeningen (een speciale eigenschap van bepaalde soorten cryptografie), maakt Monero niet-traceerbare transacties mogelijk. Dit betekent dat het onduidelijk is welk geld er is uitgegeven, en het dus uiterst onwaarschijnlijk is dat een transactie aan een bepaalde gebruiker kan worden gekoppeld.
Veilig
    Met behulp van een gedistribueerd peer-to-peer consensusnetwerk is elke transactie cryptografisch beveiligd. Individuele accounts hebben een geheugensteuntje van 25 woorden dat wordt weergegeven wanneer ze worden gemaakt, dat kan worden opgeschreven om een back-up van het account te maken. Een wachtwoord is verplicht bij het aanmaken van een portefeuille en accountbestanden worden versleuteld met een wachtwoord zin om ervoor te zorgen dat ze waardeloos zijn als ze worden gestolen.
Vervangbaar
    Alle munten zijn gelijk en hebben dezelfde waarde. Een gebruiker, verkoper of een andere entiteit kan bepaalde Monero-munten niet blokkeren of op de zwarte lijst zetten, omdat de transactiegeschiedenis van Monero-munten dubbelzinnig is.
Gedecentraliseerd
    Alle Monero-knooppunten zijn gelijk. Er is geen superklasse van knooppunten die meer invloed of controle hebben over transacties dan andere knooppunten. Geen enkele persoon of entiteit kan transacties traceren door meerdere knooppunten te bezitten. Bovendien is er geen vertrouwde installatie. Dit betekent dat de noodzaak om een persoon of entiteit te vertrouwen geen factor is. De enige dingen die vertrouwd moeten worden, zijn de broncode (die door iedereen kan worden geverifieerd) en wiskunde.

Monero is vanaf het begin 100% open source geweest, wat betekent dat iedereen de [ broncode ](https://github.com/monero-project/bitmonero) van de software kan bekijken om te verifiëren dat er geen backdoors bestaan en dat de software veilig is.

Monero heeft ook [ collegiaal getoetste onderzoeksdocumenten ](https://lab.getmonero.org/) die alle bovengenoemde eigenschappen wiskundig en systematisch verifiëren.

### DASH

Privé
    

DASH heeft een [ rijke lijst ](https://bitinfocharts.com/top-100-richest-darkcoin-addresses.html), dus dit is geen privémunt. De financiële details van muntadressen zijn zichtbaar voor iedereen die de blockchain onderzoekt.

> DASH is cryptografisch helemaal niet privé. Eigenlijk had ik een dia in het deck die was van 'DASH, LOL' en echt niets anders ... het is slangenolie en ik ben er persoonlijk een beetje buiten mezelf over. 
> 
> **Gregory Maxwell** , Bitcoin Core-ontwikkelaar en cryptograaf, in een [ presentatie aan Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

**Peter Todd** , een andere Bitcoin Core-ontwikkelaar en cryptograaf, heeft een [ soortgelijke verklaring afgelegd](https://twitter.com/petertoddbtc/status/622022840330682368).

Onvindbaar
    Transacties worden gerouteerd via een reeks [ Masternodes ](https://www.dash.org/masternodes/) om ze onvindbaar te maken. Deze praktijk zou kunnen werken als alle masternode-operators alleen pure motieven hadden. Als een overheid, een groep hackers, een andere entiteit of zelfs een individu echter veel masternodes heeft gekocht (er zou geen manier zijn om te weten of dit is gebeurd) en als de transactie via een route is verlopen waarbij alle masternodes eigendom waren van die entiteit , dan kan de transactie worden getraceerd door die entiteit. Gezien de relatief lage kosten van masternodes en het enorme budget van overheden en sommige organisaties, is de mogelijkheid dat munten kunnen worden getraceerd reëel.
Veilig
    Transacties zijn cryptografisch beveiligd.
Vervangbaar
    Aangezien transacties niet privé zijn, bestaat het potentieel voor een entiteit om bepaalde munten te blokkeren of op de zwarte lijst te zetten, waardoor ze minder waardevol worden dan de andere. Zie de opmerking over het gebrek aan vervangbaarheid van Bitcoin hieronder, aangezien hetzelfde principe van toepassing is op DASH.
Gedecentraliseerd
    Niet alle DASH-knooppunten zijn gelijk. Er is een superklasse van knooppunten, genaamd _Masternodes_ waarvan de eigenaren meer invloed hebben op het systeem dan reguliere knooppuntoperators. Dit maakt DASH semi-gecentraliseerd in plaats van het ideale 100% gedecentraliseerde systeem.

### Zcash

Privé
    

Zcash-transacties zijn zichtbaar op hun blockchain. Ze maken wel verborgen transacties mogelijk, maar [ minder dan 1% van de transacties is volledig afgeschermd ](http://stat.bloxy.info/superset/dashboard/zcash/). Aangezien verborgen transacties optioneel zijn en niet de standaard (en zelden gebruikt), vallen de [ verborgen transacties op op hun blockchain ](http://weuse.cash/2016/06/09/btc-xmr-zcash/) en trekken ze de aandacht naar zichzelf.

> En trouwens, ik denk dat we Zcash met succes traceerbaar kunnen maken voor criminelen zoals WannaCry, maar nog steeds volledig privé & vervangbaar. 
> 
> **Zooko Wilcox** , CEO van Zcash, in een [ tweet ](https://twitter.com/zooko/status/863202798883577856)

Als Zcash "te traceerbaar" kan zijn, kan het niet volledig privé of vervangbaar zijn. 

Onvindbaar
    

Reguliere transacties zijn transparant. Verborgen transacties maken gebruik van zk-SNARKS, die weliswaar onder bepaalde voorwaarden robuuste privacygaranties hebben. De vraag is of aan deze voorwaarden wordt voldaan, en gezien het minuscule aantal mensen dat gebruik maakt van de afgeschermde mogelijkheden, blijft dit nog steeds onduidelijk.

Veilig
    Transacties zijn cryptografisch beveiligd.
Vervangbaar
    Aangezien niet alle transacties privé zijn, bestaat het potentieel voor een entiteit om bepaalde munten te blokkeren of op de zwarte lijst te zetten, waardoor ze minder waardevol worden dan de andere. Zie de opmerking over het gebrek aan vervangbaarheid van Bitcoin hieronder, aangezien hetzelfde principe van toepassing is op Zcash.
Gedecentraliseerd
    

Zcash is een bedrijf en neemt momenteel [ 20% van alle gedolven ZEC als beloning voor de oprichter ](https://z.cash/blog/funding.html). 

Zcash vereiste een **Trusted Setup**. Dit betekent dat u erop moet vertrouwen dat het systeem eerlijk is opgezet. Als het niet eerlijk was ingesteld, zouden [ onbeperkte hoeveelheden ZEC kunnen worden gemaakt zonder dat iemand het weet ](https://blog.okturtles.com/2016/03/the-zcash-catch/). Dit zou de hacker rijk maken en ZEC devalueren. Er is geen manier om te weten of de Trusted Setup eerlijk is uitgevoerd. We moeten ze op hun woord geloven. Dit introduceert een menselijk faalpunt in het systeem dat in strijd is met bijna elke andere cryptocurrency. U zou alleen wiskunde en verifieerbare broncodes in cryptocurrencies moeten vertrouwen, niet mensen. Zoals we hebben gezien bij vrijwel alle grote softwarebedrijven, zoals [ Microsoft](https://www.gnu.org/proprietary/proprietary-back-doors.en.html), [ Apple](http://www.digitaltrends.com/computing/apple-vs-fbi-backdoor-to-data-already-exists/) en zelfs overheden, die niet moeten worden vertrouwd. 

Peter Todd, een Bitcoin Core-ontwikkelaar die [ deelnam ](https://github.com/zcash/mpc/blob/master/README.md) aan de Zcash Trusted Setup, noemde het een " [ backdoor ](https://twitter.com/petertoddbtc/status/793584540891643906) ". 

> Zcash is niet onvoorwaardelijk gezond, dit kan ook niet met de huidige technologie... het vereist een vertrouwde setup … en moet de procedure [Trusted Setup] opnieuw uitvoeren om de crypto in de loop van de tijd te upgraden, dus het is een kwetsbaarheid. 
> 
> Gregory Maxwell, Bitcoin Core-ontwikkelaar en cryptograaf, in een [ presentatie aan Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

**Opmerking:** Zcoin verschuift van zijn huidige Sigma-schema naar een nieuw protocol dat vertrouwt op zijn nieuwe werk, Lelantus. Lelantus wordt in fasen geïmplementeerd en in dit artikel wordt ervan uitgegaan dat alle fasen voltooid en geïmplementeerd zijn voor goede vergelijkingen naast de verwachte implementatietijden.

De reden dat Zcoin deze luxe kreeg om beoordeeld te worden op zijn toekomstige protocol, en niet op Zcash, is omdat Zcoin een routekaart heeft met algemene timings voor activering, terwijl de 'privacy by default'-plannen van Zcash (nog steeds) vaag zijn.

Privé
    

Zcoin (XZC) zal geen uitgebreide lijst hebben, dus het zal privé zijn. Het wordt verwacht dat de verplichte privacy standaard in 2021 live gaat. Als deze eenmaal is geïmplementeerd, is het niet mogelijk om een uitgebreide lijst te maken (hoewel ze er momenteel [ wel een hebben ](https://www.coinexplorer.net/XZC/richlist)).

Onvindbaar
    Met de laatste fase van Lelantus, geïmplementeerd in 2021, zou Zcoin niet traceerbaar moeten zijn, alhoewel theoretische aanvallen nog niet zijn onderzocht omdat het nog niet is vrijgegeven of een tijd in het wild heeft gehad. Op dit moment is Zcoin traceerbaar als men een [Zcoin-adres ](https://explorer.zcoin.io/) in een blockchain-verkenner plaatst en u kunt het saldo en gerelateerde transacties zien.
Veilig
    Transacties zijn cryptografisch beveiligd.
Vervangbaar
    Nadat de laatste fase van Lelantus live gaat in 2021, wordt aangenomen dat Zcoin fungibel zal zijn vanwege de verplichte privacyhandhaving. In dit opzicht zal het een echte concurrent van Monero zijn. Echter...
Gedecentraliseerd
    Zcoin heeft Znodes geïmplementeerd, die op dezelfde manier werken als Dash-masternodes en meer macht hebben dan andere knooppunten op het netwerk. Aangezien niet alle knooppunten gelijk zijn gemaakt en de onderscheidende factor tussen hen de hoeveelheid geld is die een individu heeft (Znodes kosten 1000 XZC), is het netwerk semi-gecentraliseerd.

Privé
    Grin heeft geen lijst van rijken, wat zou duiden op enige vorm van privacy. Passieve aanvallers die de keten scannen, kunnen inderdaad niet zien welk adres hoeveel geld bevat, deels omdat bedragen worden verborgen via vertrouwelijke transacties, deels omdat adresgegevens niet in de keten zijn opgeslagen en deels vanwege Mimblewimble's cut-through-technologie, waarbij tussenliggende transacties uit de keten kunnen worden verwijderd, waardoor er weinig metadata overblijven van transacties uit het verleden.
Onvindbaar
    Grin verdedigt niet tegen een actieve aanvaller die een transactiegrafiek opbouwt. Het is voor zowel miners als een licht gewijzigde node mogelijk om elke transactie te bekijken, op te slaan voordat de cut-through-technologie in werking treedt en van hieruit een complete transactiegrafiek samen te stellen met behoud van alle 'cut-through'-gegevens. Ze zouden geen informatie kunnen onderscheiden voordat ze beginnen, maar alles nadat ze zijn begonnen, zal waardevolle metadata zijn waarmee ze mogelijk transacties kunnen koppelen.
Veilig
    Transacties zijn cryptografisch beveiligd.
Vervangbaar
    Aangezien alle transacties twijfelachtig privé en mogelijk traceerbaar zijn, bestaat er de mogelijkheid om een transactiegrafiek te bouwen, waaruit waardevolle informatie kan worden afgeleid die tegen een individu kan worden gebruikt met betrekking tot hun bestedingspatroon. Outputs kunnen vervolgens worden gekoppeld aan identiteiten, en hoewel bedragen niet worden gezien, betekent het feit dat een output kan worden gekoppeld aan een identiteit, dat de output kan worden aangetast, puur en alleen op basis van wie het vasthield. We denken dat dit betekent dat Grin niet vervangbaar is, omdat sommige outputs aangetast kunnen zijn en andere niet.
Gedecentraliseerd
    Grin heeft geen premine, beloning van de oprichter, masternodes of schatkist. Ze hadden geen ICO en worden beheerd op een manier die past bij een gedecentraliseerde gemeenschap. Grin is gedecentraliseerd.

### Bitcoin Mixers

Privé
    

Alle Bitcoin transacties zijn zichtbaar op de blockchain en er is een [ Bitcoin Rijken Lijst](http://www.bitcoinrichlist.com/top100), dus Bitcoin is niet privé. Bitcoin is [ pseudoniem ](https://bitcoin.org/en/you-need-to-know), niet anoniem. 

Voor **Bitcoin-mixers** moet u erop vertrouwen dat ze hun gegevens veilig kunnen bewaren en geen eigendom zijn van of samenwerken met een overheid, hackers of andere entiteiten. 

In juli 2017 kondigde de oprichter van de grootste Bitcoin-mixservice, BITMIXER.IO, aan dat ze gingen sluiten en gaf dit als reden: 

> … Nu begreep ik dat Bitcoin een transparant, niet-anoniem systeem **is door ontwerp**. Blockchain is een groot open boek … 
> 
> BITMIXER.IO, in een aankondiging van sluiting op [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (nadruk in het origineel). 

Een paar weken later, nadat hij de verschillende op privacy gerichte munten had overwogen, zei hij dit: 

> Na het grondige onderzoek bevestig ik dat MONERO de beste privacyvaluta is. Dus ik raad MONERO ten zeerste aan voor alle mensen die extra privacy nodig hebben. 
> 
> BITMIXER.IO, in een vervolgpost [ ](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Onvindbaar
    

Aangezien alle Bitcoin-transacties zichtbaar zijn op de blockchain, zijn ALLE Bitcoin-transacties te traceren. Een Bitcoin-mixer kan transacties zeer vertroebelen, waardoor het voor iemand veel moeilijker wordt om de Bitcoins te traceren, maar niet onmogelijk. Naarmate de technologie vordert en bedrijven die gespecialiseerd zijn in het traceren van Bitcoin-transacties vaker voorkomen, zullen zeer versluierde transacties relatief gemakkelijk traceerbaar worden: 

  * [ Wetshandhaving blijft investeren in Bitcoin Tracking Services ](https://news.bitcoin.com/law-enforcement-continues-invest-bitcoin-tracking-services/)
  * [ Time.com: Bitcoins zijn gemakkelijker te volgen dan u denkt ](http://time.com/3689359/bitcoins-track-anonymous/)
  * [ Elliptic: een bedrijf dat gespecialiseerd is in het traceren van Bitcoin voor wetshandhaving ](https://www.elliptic.co/)

Een Google-zoekopdracht zal tientallen artikelen zoals deze hierboven onthullen. En vergeet niet dat elke transactie die op enig moment in het verleden heeft plaatsgevonden, zich op de blockchain bevindt en kan worden getraceerd, zelfs als er een mengservice is gebruikt. Het gebruik van een mengservice zal waarschijnlijk de aandacht vestigen op die transacties. 

Veilig
    Transacties zijn cryptografisch beveiligd.
Vervangbaar
    

Niet alle Bitcoins zijn gelijk en hebben dezelfde waarde. Sommige Bitcoins zijn op de zwarte lijst gezet en geblokkeerd door verschillende entiteiten, waardoor die munten minder waard zijn dan de rest. Als u Bitcoins ontvangt die in het verleden voor illegale doeleinden zijn gebruikt, kunnen uw Bitcoins op de zwarte lijst worden gezet, ook al had u niets met de illegale activiteiten te maken. Of, stel dat een overheid, werkgever of een ander entiteit besluit om uw Bitcoins in de toekomst op de zwarte lijst te zetten, net zoals ze doen met het bevriezen of confisceren van activa. U zou niets kunnen doen. Aangezien een mixer het alleen maar moeilijker maakt om uw Bitcoins te traceren, is deze categorie gemarkeerd als "niet vervangbaar". 

  * Andreas Antonopoulos, een voormalige Bitcoin Core-ontwikkelaar die zeer gerespecteerd wordt in de Bitcoin- en andere cryptocurrency-gemeenschappen, erkent het probleem van de vervangbaarheid van Bitcoin in een [YouTube-video](https://www.youtube.com/watch?v=ak1iojpiHpM&feature=youtu .be&t=33m9s). 
  * Bespreking van het vervangbaarheidsprobleem van Bitcoin op [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=1190707.0)

Gedecentraliseerd
    Bitcoin zelf is gedecentraliseerd, maar de meeste mixservices zijn gecentraliseerd. Dit betekent dat u ze moet vertrouwen. Sommige nieuwere, zoals de Wasabi-portefeuille, zijn dat echter niet.

## Samenvatting

Naar onze mening is Monero de duidelijke keuze als u op zoek bent naar een privé, veilige, niet-traceerbare, fungibele, gedecentraliseerde cryptocurrency zonder dat er een vertrouwde configuratie vereist is. De rest brengt uw privacy en veiligheid in gevaar. Maar neem niet zomaar onze mening aan. Doe uw eigen onderzoek en ontdek het zelf. Houd er rekening mee dat Monero wordt onderschreven en gebruikt door entiteiten die afhankelijk zijn van privacy en onvindbaarheid, zoals: 

  * [ SIGAINT ](https://www.reddit.com/r/Monero/comments/4xqrzd/sigaint_launches_tor_monero_node_as_its_operators/)
  * [ Purisme ](https://puri.sm/posts/purism-collaborates-with-cryptocurrency-monero-to-enable-mobile-payments/)
  * [ Wikileaks ](https://shop.wikileaks.org/donate#db9)
  * AlphaBay Market (AB) werd in juli 2017 gesloten. De [ Federal Forfeiture Complaint ](https://assets.documentcloud.org/documents/3898109/AlphaBay-Cazes-Forfeiture-Complaint.pdf) tegen AB laat zien dat: 
    * **Monero is de enige privé en onvindbare cryptocurrency:**   
"In totaal namen de portefeuilles en computeragenten van CAZES de controle over ongeveer $8.800.000 in Bitcoin, Ethereum, Moreno [sic] en Zcash, als volgt verdeeld: 1.605.0503851 Bitcoin, 8.309.271639 Ethereum, 3.691.98 Zcash, _en een onbekende hoeveelheid Monero._ " (onderaan p. 20 en bovenaan p. 21, cursivering toegevoegd) 
    * **Bitcoin-transacties zijn niet privé en kunnen worden getraceerd:**   
"Federale agenten verkregen de warrants na het traceren van een aantal Bitcoin-transacties afkomstig van AlphaBay naar digitale valutarekeningen, en uiteindelijk bankrekeningen en andere materiële activa, aangehouden door CAZES en zijn vrouw. " (p. 17, regels 24- 26) 

LocalMonero pleit niet voor illegale activiteiten en moedigt deze ook niet aan. 

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

  * [Monero-Mining: Wat RandomX zo Speciaal Maakt](/knowledge/monero-mining-randomx)/

Niet alle op privacy gerichte munten kunnen 100% privacy, onvindbaarheid, veiligheid en fungibiliteit bieden in een 100% gedecentraliseerde munt met een betrouwbare opzet. Hier vindt u wat deze kenmerken zijn en waarom ze belangrijk zijn:

## Munt analyse

Hier is een analyse van bekende cryptocurrencies die anonimiteit en/of onvindbaarheid claimen als hun belangrijkste onderscheidende factor. Bitcoin zelf valt niet binnen het bereik van deze analyse, aangezien er nooit is beweerd dat het anoniem is.

Deze site is gemaakt door gebruikers van Monero. Er was een tijd dat we geen Monero-gebruikers waren, maar ons zorgen maakten over financiële privacy. We hebben de munten onderzocht die beweerden privé te zijn en deze pagina is het resultaat van ons onderzoek. Daarom hebben we Monero verkozen boven de rest. Dus als we bevooroordeeld lijken, zijn we dat ook, maar we geloven dat die vooringenomenheid gebaseerd is op feiten die u hieronder kunt lezen en zelf kunt verifiëren.

Deze site is gemaakt door gebruikers van Monero. Er was een tijd dat we geen Monero-gebruikers waren, maar ons zorgen maakten over financiële privacy. We hebben de munten onderzocht die beweerden privé te zijn en deze pagina is het resultaat van ons onderzoek. Daarom hebben we Monero verkozen boven de rest. Dus als we bevooroordeeld lijken, zijn we dat ook, maar we geloven dat die vooringenomenheid gebaseerd is op feiten die u hieronder kunt lezen en zelf kunt verifiëren.

### Overzicht

Selecteer een logo om naar de analyse van die munt te gaan.

### Monero

Monero is vanaf het begin 100% open source geweest, wat betekent dat iedereen de [ broncode ](https://github.com/monero-project/bitmonero) van de software kan bekijken om te verifiëren dat er geen backdoors bestaan en dat de software veilig is.

Monero heeft ook [ collegiaal getoetste onderzoeksdocumenten ](https://lab.getmonero.org/) die alle bovengenoemde eigenschappen wiskundig en systematisch verifiëren.

### DASH

DASH heeft een [ rijke lijst ](https://bitinfocharts.com/top-100-richest-darkcoin-addresses.html), dus dit is geen privémunt. De financiële details van muntadressen zijn zichtbaar voor iedereen die de blockchain onderzoekt.

> DASH is cryptografisch helemaal niet privé. Eigenlijk had ik een dia in het deck die was van 'DASH, LOL' en echt niets anders ... het is slangenolie en ik ben er persoonlijk een beetje buiten mezelf over. 
> 
> **Gregory Maxwell** , Bitcoin Core-ontwikkelaar en cryptograaf, in een [ presentatie aan Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

DASH is cryptografisch helemaal niet privé. Eigenlijk had ik een dia in het deck die was van 'DASH, LOL' en echt niets anders ... het is slangenolie en ik ben er persoonlijk een beetje buiten mezelf over. 

DASH is cryptografisch helemaal niet privé. Eigenlijk had ik een dia in het deck die was van 'DASH, LOL' en echt niets anders ... het is slangenolie en ik ben er persoonlijk een beetje buiten mezelf over. 

**Gregory Maxwell** , Bitcoin Core-ontwikkelaar en cryptograaf, in een [ presentatie aan Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

**Peter Todd** , een andere Bitcoin Core-ontwikkelaar en cryptograaf, heeft een [ soortgelijke verklaring afgelegd](https://twitter.com/petertoddbtc/status/622022840330682368).

### Zcash

Zcash-transacties zijn zichtbaar op hun blockchain. Ze maken wel verborgen transacties mogelijk, maar [ minder dan 1% van de transacties is volledig afgeschermd ](http://stat.bloxy.info/superset/dashboard/zcash/). Aangezien verborgen transacties optioneel zijn en niet de standaard (en zelden gebruikt), vallen de [ verborgen transacties op op hun blockchain ](http://weuse.cash/2016/06/09/btc-xmr-zcash/) en trekken ze de aandacht naar zichzelf.

> En trouwens, ik denk dat we Zcash met succes traceerbaar kunnen maken voor criminelen zoals WannaCry, maar nog steeds volledig privé & vervangbaar. 
> 
> **Zooko Wilcox** , CEO van Zcash, in een [ tweet ](https://twitter.com/zooko/status/863202798883577856)

En trouwens, ik denk dat we Zcash met succes traceerbaar kunnen maken voor criminelen zoals WannaCry, maar nog steeds volledig privé & vervangbaar. 

En trouwens, ik denk dat we Zcash met succes traceerbaar kunnen maken voor criminelen zoals WannaCry, maar nog steeds volledig privé & vervangbaar. 

**Zooko Wilcox** , CEO van Zcash, in een [ tweet ](https://twitter.com/zooko/status/863202798883577856)

Als Zcash "te traceerbaar" kan zijn, kan het niet volledig privé of vervangbaar zijn. 

Reguliere transacties zijn transparant. Verborgen transacties maken gebruik van zk-SNARKS, die weliswaar onder bepaalde voorwaarden robuuste privacygaranties hebben. De vraag is of aan deze voorwaarden wordt voldaan, en gezien het minuscule aantal mensen dat gebruik maakt van de afgeschermde mogelijkheden, blijft dit nog steeds onduidelijk.

Zcash is een bedrijf en neemt momenteel [ 20% van alle gedolven ZEC als beloning voor de oprichter ](https://z.cash/blog/funding.html). 

Zcash vereiste een **Trusted Setup**. Dit betekent dat u erop moet vertrouwen dat het systeem eerlijk is opgezet. Als het niet eerlijk was ingesteld, zouden [ onbeperkte hoeveelheden ZEC kunnen worden gemaakt zonder dat iemand het weet ](https://blog.okturtles.com/2016/03/the-zcash-catch/). Dit zou de hacker rijk maken en ZEC devalueren. Er is geen manier om te weten of de Trusted Setup eerlijk is uitgevoerd. We moeten ze op hun woord geloven. Dit introduceert een menselijk faalpunt in het systeem dat in strijd is met bijna elke andere cryptocurrency. U zou alleen wiskunde en verifieerbare broncodes in cryptocurrencies moeten vertrouwen, niet mensen. Zoals we hebben gezien bij vrijwel alle grote softwarebedrijven, zoals [ Microsoft](https://www.gnu.org/proprietary/proprietary-back-doors.en.html), [ Apple](http://www.digitaltrends.com/computing/apple-vs-fbi-backdoor-to-data-already-exists/) en zelfs overheden, die niet moeten worden vertrouwd. 

Peter Todd, een Bitcoin Core-ontwikkelaar die [ deelnam ](https://github.com/zcash/mpc/blob/master/README.md) aan de Zcash Trusted Setup, noemde het een " [ backdoor ](https://twitter.com/petertoddbtc/status/793584540891643906) ". 

> Zcash is niet onvoorwaardelijk gezond, dit kan ook niet met de huidige technologie... het vereist een vertrouwde setup … en moet de procedure [Trusted Setup] opnieuw uitvoeren om de crypto in de loop van de tijd te upgraden, dus het is een kwetsbaarheid. 
> 
> Gregory Maxwell, Bitcoin Core-ontwikkelaar en cryptograaf, in een [ presentatie aan Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

Zcash is niet onvoorwaardelijk gezond, dit kan ook niet met de huidige technologie... het vereist een vertrouwde setup … en moet de procedure [Trusted Setup] opnieuw uitvoeren om de crypto in de loop van de tijd te upgraden, dus het is een kwetsbaarheid. 

Zcash is niet onvoorwaardelijk gezond, dit kan ook niet met de huidige technologie... het vereist een vertrouwde setup … en moet de procedure [Trusted Setup] opnieuw uitvoeren om de crypto in de loop van de tijd te upgraden, dus het is een kwetsbaarheid. 

Gregory Maxwell, Bitcoin Core-ontwikkelaar en cryptograaf, in een [ presentatie aan Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

**Opmerking:** Zcoin verschuift van zijn huidige Sigma-schema naar een nieuw protocol dat vertrouwt op zijn nieuwe werk, Lelantus. Lelantus wordt in fasen geïmplementeerd en in dit artikel wordt ervan uitgegaan dat alle fasen voltooid en geïmplementeerd zijn voor goede vergelijkingen naast de verwachte implementatietijden.

De reden dat Zcoin deze luxe kreeg om beoordeeld te worden op zijn toekomstige protocol, en niet op Zcash, is omdat Zcoin een routekaart heeft met algemene timings voor activering, terwijl de 'privacy by default'-plannen van Zcash (nog steeds) vaag zijn.

Zcoin (XZC) zal geen uitgebreide lijst hebben, dus het zal privé zijn. Het wordt verwacht dat de verplichte privacy standaard in 2021 live gaat. Als deze eenmaal is geïmplementeerd, is het niet mogelijk om een uitgebreide lijst te maken (hoewel ze er momenteel [ wel een hebben ](https://www.coinexplorer.net/XZC/richlist)).

### Bitcoin Mixers

Alle Bitcoin transacties zijn zichtbaar op de blockchain en er is een [ Bitcoin Rijken Lijst](http://www.bitcoinrichlist.com/top100), dus Bitcoin is niet privé. Bitcoin is [ pseudoniem ](https://bitcoin.org/en/you-need-to-know), niet anoniem. 

Voor **Bitcoin-mixers** moet u erop vertrouwen dat ze hun gegevens veilig kunnen bewaren en geen eigendom zijn van of samenwerken met een overheid, hackers of andere entiteiten. 

In juli 2017 kondigde de oprichter van de grootste Bitcoin-mixservice, BITMIXER.IO, aan dat ze gingen sluiten en gaf dit als reden: 

> … Nu begreep ik dat Bitcoin een transparant, niet-anoniem systeem **is door ontwerp**. Blockchain is een groot open boek … 
> 
> BITMIXER.IO, in een aankondiging van sluiting op [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (nadruk in het origineel). 

… Nu begreep ik dat Bitcoin een transparant, niet-anoniem systeem **is door ontwerp**. Blockchain is een groot open boek … 

… Nu begreep ik dat Bitcoin een transparant, niet-anoniem systeem **is door ontwerp**. Blockchain is een groot open boek … 

BITMIXER.IO, in een aankondiging van sluiting op [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (nadruk in het origineel). 

Een paar weken later, nadat hij de verschillende op privacy gerichte munten had overwogen, zei hij dit: 

> Na het grondige onderzoek bevestig ik dat MONERO de beste privacyvaluta is. Dus ik raad MONERO ten zeerste aan voor alle mensen die extra privacy nodig hebben. 
> 
> BITMIXER.IO, in een vervolgpost [ ](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Na het grondige onderzoek bevestig ik dat MONERO de beste privacyvaluta is. Dus ik raad MONERO ten zeerste aan voor alle mensen die extra privacy nodig hebben. 

Na het grondige onderzoek bevestig ik dat MONERO de beste privacyvaluta is. Dus ik raad MONERO ten zeerste aan voor alle mensen die extra privacy nodig hebben. 

BITMIXER.IO, in een vervolgpost [ ](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Aangezien alle Bitcoin-transacties zichtbaar zijn op de blockchain, zijn ALLE Bitcoin-transacties te traceren. Een Bitcoin-mixer kan transacties zeer vertroebelen, waardoor het voor iemand veel moeilijker wordt om de Bitcoins te traceren, maar niet onmogelijk. Naarmate de technologie vordert en bedrijven die gespecialiseerd zijn in het traceren van Bitcoin-transacties vaker voorkomen, zullen zeer versluierde transacties relatief gemakkelijk traceerbaar worden: 

  * [ Wetshandhaving blijft investeren in Bitcoin Tracking Services ](https://news.bitcoin.com/law-enforcement-continues-invest-bitcoin-tracking-services/)
  * [ Time.com: Bitcoins zijn gemakkelijker te volgen dan u denkt ](http://time.com/3689359/bitcoins-track-anonymous/)
  * [ Elliptic: een bedrijf dat gespecialiseerd is in het traceren van Bitcoin voor wetshandhaving ](https://www.elliptic.co/)

Een Google-zoekopdracht zal tientallen artikelen zoals deze hierboven onthullen. En vergeet niet dat elke transactie die op enig moment in het verleden heeft plaatsgevonden, zich op de blockchain bevindt en kan worden getraceerd, zelfs als er een mengservice is gebruikt. Het gebruik van een mengservice zal waarschijnlijk de aandacht vestigen op die transacties. 

Niet alle Bitcoins zijn gelijk en hebben dezelfde waarde. Sommige Bitcoins zijn op de zwarte lijst gezet en geblokkeerd door verschillende entiteiten, waardoor die munten minder waard zijn dan de rest. Als u Bitcoins ontvangt die in het verleden voor illegale doeleinden zijn gebruikt, kunnen uw Bitcoins op de zwarte lijst worden gezet, ook al had u niets met de illegale activiteiten te maken. Of, stel dat een overheid, werkgever of een ander entiteit besluit om uw Bitcoins in de toekomst op de zwarte lijst te zetten, net zoals ze doen met het bevriezen of confisceren van activa. U zou niets kunnen doen. Aangezien een mixer het alleen maar moeilijker maakt om uw Bitcoins te traceren, is deze categorie gemarkeerd als "niet vervangbaar". 

  * Andreas Antonopoulos, een voormalige Bitcoin Core-ontwikkelaar die zeer gerespecteerd wordt in de Bitcoin- en andere cryptocurrency-gemeenschappen, erkent het probleem van de vervangbaarheid van Bitcoin in een [YouTube-video](https://www.youtube.com/watch?v=ak1iojpiHpM&feature=youtu .be&t=33m9s). 
  * Bespreking van het vervangbaarheidsprobleem van Bitcoin op [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=1190707.0)

## Samenvatting

Naar onze mening is Monero de duidelijke keuze als u op zoek bent naar een privé, veilige, niet-traceerbare, fungibele, gedecentraliseerde cryptocurrency zonder dat er een vertrouwde configuratie vereist is. De rest brengt uw privacy en veiligheid in gevaar. Maar neem niet zomaar onze mening aan. Doe uw eigen onderzoek en ontdek het zelf. Houd er rekening mee dat Monero wordt onderschreven en gebruikt door entiteiten die afhankelijk zijn van privacy en onvindbaarheid, zoals: 

  * [ SIGAINT ](https://www.reddit.com/r/Monero/comments/4xqrzd/sigaint_launches_tor_monero_node_as_its_operators/)
  * [ Purisme ](https://puri.sm/posts/purism-collaborates-with-cryptocurrency-monero-to-enable-mobile-payments/)
  * [ Wikileaks ](https://shop.wikileaks.org/donate#db9)
  * AlphaBay Market (AB) werd in juli 2017 gesloten. De [ Federal Forfeiture Complaint ](https://assets.documentcloud.org/documents/3898109/AlphaBay-Cazes-Forfeiture-Complaint.pdf) tegen AB laat zien dat: 
    * **Monero is de enige privé en onvindbare cryptocurrency:**   
"In totaal namen de portefeuilles en computeragenten van CAZES de controle over ongeveer $8.800.000 in Bitcoin, Ethereum, Moreno [sic] en Zcash, als volgt verdeeld: 1.605.0503851 Bitcoin, 8.309.271639 Ethereum, 3.691.98 Zcash, _en een onbekende hoeveelheid Monero._ " (onderaan p. 20 en bovenaan p. 21, cursivering toegevoegd) 
    * **Bitcoin-transacties zijn niet privé en kunnen worden getraceerd:**   
"Federale agenten verkregen de warrants na het traceren van een aantal Bitcoin-transacties afkomstig van AlphaBay naar digitale valutarekeningen, en uiteindelijk bankrekeningen en andere materiële activa, aangehouden door CAZES en zijn vrouw. " (p. 17, regels 24- 26) 

  * **Monero is de enige privé en onvindbare cryptocurrency:**   
"In totaal namen de portefeuilles en computeragenten van CAZES de controle over ongeveer $8.800.000 in Bitcoin, Ethereum, Moreno [sic] en Zcash, als volgt verdeeld: 1.605.0503851 Bitcoin, 8.309.271639 Ethereum, 3.691.98 Zcash, _en een onbekende hoeveelheid Monero._ " (onderaan p. 20 en bovenaan p. 21, cursivering toegevoegd) 
  * **Bitcoin-transacties zijn niet privé en kunnen worden getraceerd:**   
"Federale agenten verkregen de warrants na het traceren van een aantal Bitcoin-transacties afkomstig van AlphaBay naar digitale valutarekeningen, en uiteindelijk bankrekeningen en andere materiële activa, aangehouden door CAZES en zijn vrouw. " (p. 17, regels 24- 26) 

LocalMonero pleit niet voor illegale activiteiten en moedigt deze ook niet aan. 

LocalMonero pleit niet voor illegale activiteiten en moedigt deze ook niet aan. 

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

  * [Monero-Mining: Wat RandomX zo Speciaal Maakt](/knowledge/monero-mining-randomx)/

Verder lezen