---
title: "Wired Magazine er Forkert Om Monero, Her er Hvorfor"
slug: "wired-article-debunked"
date: "2020-06-24"
image: "/images/wired.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Både inden for privatliv og kryptovaluta er misinformation ofte udbredt. Vi har [en artikel, der skitserer femten almindelige forkerte eller forældede antagelser om Monero](/knowledge/monero-myths-debunked), men vi vil tage os tid til at tage fat på en bestemt artikel, som ofte citeres og cirkuleres af Monero skeptikere.

Publikationen Wired udgav [en artikel](https://www.wired.com/story/monero-privacy/)den 27 marts 2018, som i sig selv blev skrevet som svar på en anden dugfrisk artikel udgivet af forskellige akademikere med titlen: "An Empirical Analysis of Traceability in the Monero Blockchain".

Selvom avisen var medforfatter af personer med tydelig interessekonflikt (læs: de er rådgivere for og har en andel i Zcash), blev avisen moderat godt modtaget af Monero-samfundet, da det bekræfter ting, som fællesskabet allerede har vidst. og skrevet om i deres egne Monero Research Lab-artikler ([MRL-0001](https://web.getmonero.org/resources/research-lab/pubs/MRL-0001.pdf) og [MRL-0004](https://web.getmonero.org/resources/research-lab/pubs/MRL-0004.pdf)), hvoraf den tidligste blev offentliggjort fire år tidligere.Der var dog også flere frustrationer over det, primært interessekonflikten, det faktum, at problemerne allerede var kendt, diskuteret og - i nogle tilfælde - afhjulpet, og den grove fejlbeskrivelse af Moneros privatlivsgarantier på det tidspunkt. Samfundet kommenterede på det foreløbige tryk af arbejdet, og mange af deres anbefalinger kom med i det endelige papir.

Men hvad var det lige, der blev misforstået? Det faktum, at Monero ikke havde haft de fejl, der blev diskuteret i artiklen, i over et år. Transaktioner før 2017 var faktisk sårbare over for en form for privatlivslækage, men på udgivelsestidspunktet havde Monero adresseret de fleste af bekymringerne. For at være fair over for forfatterne, diskuterer de Moneros løsninger i en lille grad, men ikke nok til at påvirke den effekt, det havde på kryptovaluta-mediecyklussen på det tidspunkt. Derfor Wired-artiklen.

Mens vi kan undersøge den pågældende Wired-artikel som et stykke fra perioden, og hvor sand eller usand den var på det tidspunkt, inviterer det faktum, at den stadig bliver delt i dag som begrundelse for, hvorfor Moneros privatlivsgarantier er svage, faktisk til en analyse af, hvordan stykket holder i nutiden. Vi tager med glæde imod denne invitation.

En hurtig læsning af artiklen viser flere sensationelle linjer, såsom "[Resultaterne] bør ikke kun bekymre nogen, der forsøger at snige sig til at bruge Monero i dag" og hele tonen i artiklen, der postulerer forskningen som 'ny', stort set baseret på publikationen. Selve den akademiske artikel har anbefalinger såsom at advare Monero-brugere om den potentielle kompromittering af deres anonymitet, på trods af at disse diskussioner ikke kun havde fundet sted siden 2014, men at fællesskabets råb var, at folk ikke skulle købe Monero, og at det var meget eksperimentelt.

Men hvad med selve kritikken? Virkeligheden er, at mange af problemerne med Monero som en privacy coin enten ikke længere gælder for Monero, eller er fælles bekymringer med privacy coins som en kategori af blockchain-baserede kryptovalutaer. Lad os begynde med at adressere disse

Et af de oftest citerede kritikpunkter af Monero er, at hvis en fremtidig teknologi skulle bryde privatlivets fred, ville alle Moneros tidligere transaktioner blive blotlagt på grund af blockchainens permanens og uforanderlighed. Med andre ord har dit privatliv et tikkende ur.

Vi kan ikke understrege dette nok. Bogstaveligt talt alle privacy coins, der anvender on-chain-metoder til obfuskering og privacy, har denne fejl, og alligevel bliver den ofte brugt mod Monero (ironisk nok mange gange af konkurrerende privacy coins med samme problem), og den bliver også brugt i denne artikel. Svaret på denne kritik kan være overraskende for nogle, men Monero er faktisk mindre sårbar end andre privacy coins over for dette, fordi den har en flerstrenget tilgang til privacy.

Monero skjuler output (afsendere), beløb og modtagere gennem tre forskellige teknologier, henholdsvis ringsignaturer, RingCT og stealth-adresser. Af disse er ringsignaturer de svageste og mest modtagelige for både moderne heuristikker og teoretiske, fremtidige teknologier, der bryder privatlivets fred. Det har Monero-community'et vidst i årevis, og der forskes aktivt i at forbedre eller helt erstatte ringsignatur ordningen.

Men selv hvis ringsignaturen blev brudt helt, ville kun det sande output blive afsløret. IKKE afsenderen (som i individ), men outputtet. At koble et output med en identitet er ikke umuligt, men det ville kræve flere metadata og ressourcer. Kombineret med det faktum, at RingCT og stealth-adressen IKKE ville blive afsløret, mindsker det effekten yderligere.

Det skal bemærkes, at Wired-artiklen diskuterer ovenstående oplysninger lidt i den del, hvor de kontaktede Riccardo 'fluffypony' Spagni for en kommentar, men den tid, der er afsat til det, er kort, og det ser næsten ud til, at denne vigtige information viftes væk. Den manglende forståelse er især tydelig, når man forsøger at diskutere disse ting med folk, der deler artiklen i flæng i dag.

En anden kritik, som er meget sværere at forholde sig til, er, hvordan omverdenen ser på Monero, og hvordan det hænger sammen med, hvordan fællesskabet omkring Monero ser på mønten. For at få et eksempel på dette behøver læserne ikke at kigge længere end til selve artiklens titel: "Det mørke webs yndlingsvaluta er mindre usporlig, end den ser ud til".

Enhver person, der tilbringer en betydelig mængde tid i Monero-communitiet, kan bevidne, at Monero-communitiet går langt for at vise, hvor svært det er at opnå ægte privatliv, selv til skade for markedsførings- eller adoptionsindsatsen. Hvis fællesskabet leverer rigelige ressourcer til at diskutere mønten og dens mangler nøjagtigt, bliver uvidenheden på et tidspunkt brugerens skyld, fordi vedkommende tror, at mønten er alt, hvad de behøver for at være 100% private.

å dette tidspunkt burde det være tydeligt, at Monero-samfundet tager både sit privatliv og sin ærlighed omkring svaghederne og de efterfølgende forbedringer alvorligt. Artikler, som den pågældende, savner fuldstændig denne ånd af innovation i Monero. Den sammenligner Monero med de mange andre kryptovalutaer, der kommer med storslåede påstande, og som kun tænker på profit og på at udnytte uvidende investor-wannabes.

Yderligere læsning

  * [Hvordan Monero unikt aktiverer cirkulær økonomier](/knowledge/monero-circular-economies)/

  * [Monero's ring signaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Hvorfor (og hvordan!) skal du holde dine egne nøgler](/knowledge/hold-your-keys)/

  * [Bidrager tilbage til Monero](/knowledge/contributing-to-monero)/

  * [Hvordan fjern noder påvirker Monero's privatliv](/knowledge/remote-nodes-privacy)/

  * [Hvordan Monero bruger hard-forks til at opgradere den netværk](/knowledge/network-upgrades)/

  * [Se tags: Hvordan en byte vil reducere Monero wallet-synkroniseringstider med 40 %+](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool og Dets rolle i Decentralisering Monero Minedrift](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Hvad Det Vil Gør for Monero](/knowledge/seraphis-for-monero)/

  * [Er konvertering af Bitcoin til Monero lige så privat som at købe Monero direkte?](/knowledge/most-private-way-to-buy-monero)/

  * [Hvorfor Monero Brug en Tillidsløs Opsætning i modsætning til Zcash](/knowledge/monero-trustless-setup)/

  * [Hvorfor Monero er en bedre butik af værdi end Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Hvordan Monero Kan Overvinde Bitcoin's Netværk Effekter](/knowledge/network-effect)/

  * [Hvorfor Monero Har Det Mest Kritiske Tænkning Fællesskab](/knowledge/critical-thinking)/

  * [Svindel til Se Ud for Når Bruger Monero](/knowledge/monero-scams)/

  * [Hvordan Atomic Swaps Vil Arbejde i Monero](/knowledge/monero-atomic-swaps)/

  * [Hvad enhver Monero-bruger har brug for at vide, når det kommer til netværk](/knowledge/monero-networking)/

  * [Hvordan RingCT Huder Monero Transaktion Beløb](/knowledge/monero-ringct)/

  * [Hvordan Monero Stealth Adresser Beskyt Din Identitet](/knowledge/monero-stealth-addresses)/

  * [Hvordan Monero Underadresser Forebyg Identitet Linking](/knowledge/monero-subaddresses)/

  * [Monero Outputs Forklaret](/knowledge/monero-outputs)/

  * [Monero Bedste Praksis for Begyndere](/knowledge/monero-best-practices)/

  * [Hvordan Ring Signaturer Obskure Monero's Outputs](/knowledge/ring-signatures)/

  * [Hvordan Monero løste blokstørrelsesproblemet, der plager Bitcoin](/knowledge/dynamic-block-size)/

  * [Hvordan CLSAG Vilje Forbedre Monero's Effektivitet](/knowledge/what-is-clsag)/

  * [Hvorfor Monero Har en Hale Emission](/knowledge/monero-tail-emission)/

  * [En kort historie om Monero](/knowledge/monero-history)/

  * [Top 15 Monero Myter og Bekymringer Afkræftet](/knowledge/monero-myths-debunked)/

  * [Hvordan Dandelion++ Holder Monero's Transaktion Oprindelse Privat](/knowledge/monero-dandelion)/

  * [Hvorfor Monero Er Open Source Og Decentraliseret](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: Hvad Gør RandomX så Speciel](/knowledge/monero-mining-randomx)/

  * [Hvorfor Monero er bedre end Dash, Zcash, Zcoin (selv med Lelantus), Grin og Bitcoin-mixere som Wasabi (Opdateret maj 2020)](/knowledge/why-monero-is-better)/

Yderligere læsning