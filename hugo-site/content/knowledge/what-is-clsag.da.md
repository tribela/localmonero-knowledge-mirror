---
title: "Hvordan CLSAG Vilje Forbedre Monero's Effektivitet"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Som en protokol er Monero i øjeblikket i en konstant tilstand af innovation. Ved at bruge forskning i både on-chain og off-chain-løsninger leder Monero-fællesskabet efter områder, der kan forbedres for at gøre Monero mere privat, mere skalerbar og mere tilgængelig for alle. En af de nyere innovationer er udskiftningen af den linkbare ringsignaturordning, MLSAG, med en drop-in erstatning CLSAG, som står for Concise Linkable Spontaneous Anonymous Group.

På overfladeniveau vil implementeringen af CLSAG reducere de mest almindelige 2 input, 2 output transaktioner med 25 %. Vi vil også se et fald på 10 % i bekræftelsestiden.

Men hvad er CLSAG helt præcist? Hvad gør det, og hvordan adskiller det sig fra den gamle version, MLSAG? Lad os tage et øjeblik på at minde os selv om hvorfor og hvordan ringsignaturer, så vi bedre kan forstå dette koncept. Ringsignaturer giver mulighed for ikke-interaktive input, der ikke kan skelnes fra vidner ved brug af underskriver-valgte anonymitetssæt af tidligere output. I lægmandssprog giver det en bruger mulighed for at skjule deres output brugt i en transaktion sammen med ikke-relaterede output, og de kan gøre alt dette uden at have behov for, at andre deltager. Alt du behøver er en kopi af blockchain. Hvert af disse output ser for det meste ud til at være lige sandsynligt at være det faktiske, der sendes, og skjuler derved metadata om afsenderen.

Dette afføder dog lidt af et problem. Hvad hvis en bruger skulle konstruere en ringsignatur med alle lokkeudgange? Hvordan kan nogen vide, at den ukendte afsender ikke har autoritet til at sende nogen af dem? Ville denne bruger være i stand til at bruge falske penge? Svaret er nej. Ringsignaturen inkluderer en metode til at bevise, at mindst et af outputtene ejes af den ukendte afsender, uden at afsløre hvilken det er. Faktisk er både CLSAG og MLSAG (fremover kendt som SAG'erne) den del af ringsignaturen, der beviser dette. Interessant nok beviser det samtidig, at transaktionsbeløbet, selvom det er skjult bag fortrolige transaktioner (RingCT), balancerer. At SAG'erne beviser to ting, at det ene output ejes af nogen i ringen, og at transaktionen balancerer, er vigtig, og faktisk hvor størrelsen og verifikationsbesparelserne ligger. Hvis dette bliver forvirrende, så fortvivl ikke, vi kommer snart til en sjov og letforståelig analogi.

Det gamle signaturskema, MLSAG (Multilayered Linkable Spontaneous Anonymous Group) beviser de førnævnte to ting i en ringsignatur, men den gør hver for sig. Brugen af separate beregninger til signering og forpligtelsesnøgler betyder langsommere operationer. En moderne computer kan udføre disse beregninger i løbet af millisekunder, hvilket ikke virker af meget, og det er det faktisk ikke for en transaktion. Men når vi overvejer det store antal transaktioner på Monero blockchain, og at en node, der synkroniserer fra bunden, skal downloade og verificere hver af dem, begynder bytes og millisekunder hurtigt at hobe sig op.

CLSAG kombinerer den matematik, der er nødvendig for at bevise begge i én, samt beregner dem begge på én gang, og det gør det på en sikker måde. Hvad betyder dette på en sikker måde? Nå, for at opklare dette, samt forhåbentlig få det hele til at give mere mening, lad os udforske den lovede sjove analogi.

Lad os sige, at du skal gå til både købmanden og isenkræmmeren for at hente to forskellige ting: mad og giftige rengøringskemikalier. Du vil ikke have, at de blander sig, som hvis der er et uheld, vil kemikalierne spildes på maden, hvilket gør dem uspiselige. Du beslutter dig for at være super sikker og køre fra dit hus til købmanden, købe maden og derefter køre tilbage til dit hus. Først efter du har læsset maden af, sætter du dig tilbage i bilen, kører til isenkræmmeren og tilbage til dit hus med kemikalierne. Du har taget to separate ture for at sikre sikkerheden ved alle køb. Selvom det faktisk er sikkert, er det ineffektivt. Dette repræsenterer MLSAG, hvor to forskellige sæt matematik er gemt, og to forskellige 'ture' foretages for at beregne dem.

Du beslutter dig dog for, at du vil have en hurtigere måde at gøre dette på. Det er for meget spildtid. Sikker på at gøre det en eller to gange vil ikke stjæle dit liv væk, men at skulle gøre dette igen og igen, begynder timerne at tikke op. Du begynder at spekulere på, om du kan tage en tur i stedet for. Fra dit hus, til købmanden, til isenkræmmeren og derhjemme. Du kan ikke bare gå og smide alt i din bil tilfældigt. Det er ikke sikkert. I stedet udpeger du forskellige steder i din bil til forskellige ting, og sørger for, at alt passer pænt på sin plads. På den måde er du i stand til sikkert at tage én tur til begge butikker og holde tingene væk fra hinanden. Dette repræsenterer CLSAG. Der er nu kun ét sæt matematik gemt i denne transaktion for at bevise disse to ting, og det er gjort med det samme, at de ikke forstyrrer hinanden. En tur skal stadig foretages, men du har reduceret antallet af dem ganske drastisk.

Alt dette lyder ret spændende. Er det muligt, at vi kan finde andre genveje, eller andre måder at spare tid og plads på? Svaret er ja og nej. Ifølge nuværende MRL-forskere er det sandsynligvis ikke muligt at ændre SAG-typen yderligere for bedre størrelse eller hastighed; dog giver andre konstruktioner som Arcturus, Omniring, RCT3 eller Triptych meget bedre størrelsesskalering og verifikationsfordele ved brug af forskellige matematiske metoder. Men hver af disse 'næste-generations' tilgange til underskriver-tvetydige protokoller kommer med sine egne afvejninger i implementeringsdetaljer og er under aktiv forskning og undersøgelse.

Monero er jo altid innovativt.

Yderligere læsning

  * [Hvordan Monero unikt aktiverer cirkulær økonomier](/knowledge/monero-circular-economies/)

  * [Monero's ring signaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Hvorfor (og hvordan!) skal du holde dine egne nøgler](/knowledge/hold-your-keys/)

  * [Bidrager tilbage til Monero](/knowledge/contributing-to-monero/)

  * [Hvordan fjern noder påvirker Monero's privatliv](/knowledge/remote-nodes-privacy/)

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

  * [Hvorfor Monero Har en Hale Emission](/knowledge/monero-tail-emission/)

  * [En kort historie om Monero](/knowledge/monero-history/)

  * [Wired Magazine er Forkert Om Monero, Her er Hvorfor](/knowledge/wired-article-debunked/)

  * [Top 15 Monero Myter og Bekymringer Afkræftet](/knowledge/monero-myths-debunked/)

  * [Hvordan Dandelion++ Holder Monero's Transaktion Oprindelse Privat](/knowledge/monero-dandelion/)

  * [Hvorfor Monero Er Open Source Og Decentraliseret](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Hvad Gør RandomX så Speciel](/knowledge/monero-mining-randomx/)

  * [Hvorfor Monero er bedre end Dash, Zcash, Zcoin (selv med Lelantus), Grin og Bitcoin-mixere som Wasabi (Opdateret maj 2020)](/knowledge/why-monero-is-better/)