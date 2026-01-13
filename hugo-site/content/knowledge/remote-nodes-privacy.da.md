---
title: "Hvordan fjern noder påvirker Monero's privatliv"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
En af de største fordele, Monero har i forhold til andre kryptovalutaer, er, at det er on-chain privatliv, men har du nogensinde undret dig over, hvordan Moneros privatliv holder sig, når du bruger en ekstern node? Hvad med, hvis du bruger en "light wallet"-server som MyMonero?

I dette indlæg vil vi dykke ned i nogle af detaljerne bag, hvordan Monero giver enestående privatliv i kæden, selv når du bruger en fjernknude, samt hvad du skal være opmærksom på, når du bruger fjernknudepunkter.

## Hvad funktion gør noder tjene i Monero?

For dem, der er mindre fortrolige med, hvordan Monero fungerer, kan noderne (eller serverne) i Monero-netværket køres af alle og tillade ejeren af noden – eller andre, de vælger at dele den med! – at synkronisere en kopi af blockchain og give den kopi til andre på netværket. Disse noder verificerer også alle de transaktioner, der sker på netværket, såvel som alle blokeringer, der offentliggøres, og sikrer, at de alle følger reglerne som fastsat ved konsensus.

Den anden funktion, som noder tjener i Monero, er som en måde at levere alle de data, din foretrukne Monero-pung har brug korrekt at tjekke for transaktioner, der tilhører dig, og foretage nye transaktioner. Disse data leveres af noder på to måder:

  * Dataene fra hver blok på blockchainen anmodes om af tegnebogen, scannes for transaktioner, der tilhører dig, og kasseres derefter, når de er kontrolleret af tegnebogen. 
    * Dette trin vil snart blive drastisk forbedret, takket være [se tags](/knowledge/view-tags-reduce-monero-sync-time).
  * Når du sender transaktioner, giver den node, du bruger, en liste over mulige lokkemidler (eller falske input), som du kan bruge, når du bygger transaktionen, hvilket sikrer, at du har en god skare at gemme dig i, hver gang du bruger Monero. 
    * Disse lokkefugle er en del af [ringsignaturer](/knowledge/ring-signatures), en vigtig del af Moneros tilgang til privatliv på -kæde.

## Hvad er den mest private og sikre måde at bruge Monero på?

Det bedste at gøre, selv med det stærke on-chain privatliv, som Monero giver, når du bruger fjernknudepunkter, er at køre din egen Monero-node for at sikre, at du har en uberørt kopi af Monero blockchain ved hånden, og at din IP-adresse er godt beskyttet. Den anden fordel ved at køre din egen node er, at du kan bidrage tilbage til netværket, lade andre noder synkronisere fra din node eller endda lade andre brugere oprette forbindelse til din node med deres tegnebøger.

Når det er sagt, giver Monero stadig fremragende privatliv, når du bruger en fjernknude. Hvis du er interesseret i at køre din egen Monero-node, er her en nem at følge guide til at gøre det:

  * [Kør en Monero Node ](https://sethforprivacy.com/guides/run-a-monero-node/)

## Hvad kan en fjern node lære om mig?

Når du bruger en fjernknude, er der nogle få vigtige oplysninger, der bliver eksponeret for en fjernknude, og et par vigtige måder, hvorpå knudepunktet kan angribe dig, forhindre dig i at handle og mere.

Det første, en fjernknude kan lære om dig, er din offentlige IP-adresse. Selvom dette forhåbentlig vil blive skjult via en VPN eller Tor, kan den eksterne node knytte din offentlige IP-adresse til transaktionen og hjælpe dem med at indsnævre, hvor du handler fra. Fjernnoden kan også lære den sidste blok, din tegnebog synkroniserede, og bruge denne til at forsøge at gætte dig, som f.eks. hvornår du normalt bruger Monero, og hvornår du sidst brugte Monero. Dette gælder især, hvis du altid kommer fra den samme IP-adresse (såsom dit hjem). Den sidste vigtige ting, som en fjernknude kan lære om dig, er grundlæggende oplysninger om de transaktioner, du sender gennem den. Selvom dette kan være de mest åbenlyse data, som fjernknudeoperatøren får om dig, er det vigtigt at forstå, at dette kan bruges til at hjælpe med at spore afsenderen af transaktionen, når de kombinerer disse oplysninger med andre off-chain data. Dette kan være særligt farligt, hvis den eksterne node drives af en ondsindet enhed, et blockchain-analysefirma eller en undertrykkende nationalstat.

En fjernknude kan også forsøge at give dig problemer ved at skjule blokke for dig, hvilket får din tegnebog til at tro, at den var synkroniseret, mens den ikke var det. Dette kan få dig til at tro, at penge er tabt eller forhindre dig i at bruge penge, indtil du opretter forbindelse til en anden node. Den sidste vigtige ting, en fjernknude kan gøre, er at give din tegnebog en manipuleret liste over lokkefugle. Dette kan medføre, at din tegnebog enten mislykkes med at opbygge transaktioner (hvilket gør dig ude af stand til at bruge penge), eller det kan tillade den eksterne node at forsøge at give lokkemidler, som den ved bliver brugt for at reducere den anonymitet, du modtager i hver transaktion.

## Hvilke privatlivsgarantier eksisterer stadig, når du bruger en fjernknude?

Selvom denne artikel måske har skræmt dig en smule, er det vigtigt at indse, at privatlivets fred, som Monero tilbyder, er fremragende, selv når du bruger en fjernknude, og langt overgår enhver anden kryptovaluta, når den bruges på denne måde. Du opnår stadig det stærke on-chain privatliv, som Monero giver, da den eksterne node aldrig kender det sande input (hvilke mønter du bruger), mængden af Monero brugt i transaktionen eller adressen på modtageren af transaktionen. Eksterne observatører kan heller ikke se det sande input, beløb eller adresser, der er involveret (uanset hvilken type node du vælger at bruge!), hvilket sikrer, at uden for den eksterne node selv din IP-adresse, tegnebogssynkroniseringsoplysninger og transaktioner har stærke privatlivsgarantier .

Den eksterne node har heller aldrig adgang til de tidligere transaktioner, du har sendt eller modtaget, eller mængden af Monero i din pung, og mister al synlighed i dine transaktioner i det øjeblik, du begynder at bruge en anden node. Ingen private nøgler (hverken forbrugsnøgler eller visningsnøgler) leveres nogensinde til den eksterne node, og din tegnebog forbliver derfor privat, sikker og brugbar. Uanset fjernknudepunktet, risikerer du heller aldrig at miste Monero eller få den stjålet, da noden ikke kan redigere modtageradressen, aldrig har adgang til dine punges private nøgler og ikke på nogen måde kan konfiskere din Monero.

## Hvordan om "lette tegnebøger" som MyMonero?

Mens emnet ligger lidt uden for denne artikels omfang, ville jeg gerne tage fat på en unik type tegnebog i Monero – lette tegnebøger. Navnet light wallet kommer fra det faktum, at din pung (på din telefon eller computer) ikke skal udføre nogen af blockchain-synkroniseringen, hvilket gør oplevelsen hurtigere og mere flydende.

Men punge som denne kommer med en alvorlig afvejning af privatlivets fred for nu – din tegnebog sender den private visningsnøgle til den fjernserver, du bruger (som standarden i MyMonero), hvilket giver fjernserveren fuld synlighed i alle modtagne midler siden oprettelsen af din tegnebog (og indtil du holder op med at bruge den pung eller frø). Dette reducerer det privatliv, du modtager fra nodeoperatøren drastisk, og bør behandles med forsigtighed.

Heldigvis arbejder Monero-fællesskabet på at forbedre den software, du kan bruge til at være vært for din egen light wallet-server (LWS), som giver dig mulighed for hurtig synkronisering uden at stole på en tredjepart med dine private visningsnøgler – mens du vil køre softwaren, hvor din tegnebog sender de private visningsnøgler!

For mere om den brugerdefinerede light wallet-server, se nedenstående Github-lager:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Hvordan kan jeg lære mere?

Hvis du er nysgerrig og ville elske at forstå noder i Monero bedre og se nærmere på at bruge en fjernknude eller køre din egen, kan du se nedenstående links for gode steder at komme i gang:

  * [Monero World, en liste over fællesskabsdrevne eksterne noder, der kan bruges](https://moneroworld.com/#nodes)
  * [Monero-noder drevet af Seth For Privacy, forfatteren af denne artikel](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, en liste over eksterne noder med hyppigt kontrolleret status< /a>](https://monero.fail/)
  * [Sådan opretter du forbindelse til en ekstern node i GUI-tegnebogen](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia – fjernbetjening Node](https://www.getmonero.org/resources/moneropedia/remote-node.html)

Yderligere læsning

  * [Hvordan Monero unikt aktiverer cirkulær økonomier](/knowledge/monero-circular-economies/)

  * [Monero's ring signaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Hvorfor (og hvordan!) skal du holde dine egne nøgler](/knowledge/hold-your-keys/)

  * [Bidrager tilbage til Monero](/knowledge/contributing-to-monero/)

  * [Hvordan Monero bruger hard-forks til at opgradere den netværk](/knowledge/network-upgrades/)

  * [Se tags: Hvordan en byte vil reducere Monero wallet-synkroniseringstider med 40 %+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool og Dets rolle i Decentralisering Monero Minedrift](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Hvad Det Vil Gør for Monero](/knowledge/seraphis-for-monero/)

  * [Er konvertering af Bitcoin til Monero lige så privat som at købe Monero direkte?](/knowledge/most-private-way-to-buy-monero/)

  * [Hvorfor Monero Brug en Tillidsløs Opsætning i modsætning til Zcash](/knowledge/monero-trustless-setup/)

  * [Hvorfor Monero er en bedre butik af værdi end Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Hvordan Monero Kan Overvinde Bitcoin's Netværk Effekter](/knowledge/network-effect/)

  * [Hvorfor Monero Har Det Mest Kritiske Tænkning Fællesskab](/knowledge/critical-thinking/)

  * [Svindel til Se Ud for Når Bruger Monero](/knowledge/monero-scams/)

  * [Hvordan Atomic Swaps Vil Arbejde i Monero](/knowledge/monero-atomic-swaps/)

  * [Hvad enhver Monero-bruger har brug for at vide, når det kommer til netværk](/knowledge/monero-networking/)

  * [Hvordan RingCT Huder Monero Transaktion Beløb](/knowledge/monero-ringct/)

  * [Hvordan Monero Stealth Adresser Beskyt Din Identitet](/knowledge/monero-stealth-addresses/)

  * [Hvordan Monero Underadresser Forebyg Identitet Linking](/knowledge/monero-subaddresses/)

  * [Monero Outputs Forklaret](/knowledge/monero-outputs/)

  * [Monero Bedste Praksis for Begyndere](/knowledge/monero-best-practices/)

  * [Hvordan Ring Signaturer Obskure Monero's Outputs](/knowledge/ring-signatures/)

  * [Hvordan Monero løste blokstørrelsesproblemet, der plager Bitcoin](/knowledge/dynamic-block-size/)

  * [Hvordan CLSAG Vilje Forbedre Monero's Effektivitet](/knowledge/what-is-clsag/)

  * [Hvorfor Monero Har en Hale Emission](/knowledge/monero-tail-emission/)

  * [En kort historie om Monero](/knowledge/monero-history/)

  * [Wired Magazine er Forkert Om Monero, Her er Hvorfor](/knowledge/wired-article-debunked/)

  * [Top 15 Monero Myter og Bekymringer Afkræftet](/knowledge/monero-myths-debunked/)

  * [Hvordan Dandelion++ Holder Monero's Transaktion Oprindelse Privat](/knowledge/monero-dandelion/)

  * [Hvorfor Monero Er Open Source Og Decentraliseret](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Hvad Gør RandomX så Speciel](/knowledge/monero-mining-randomx/)

  * [Hvorfor Monero er bedre end Dash, Zcash, Zcoin (selv med Lelantus), Grin og Bitcoin-mixere som Wasabi (Opdateret maj 2020)](/knowledge/why-monero-is-better/)