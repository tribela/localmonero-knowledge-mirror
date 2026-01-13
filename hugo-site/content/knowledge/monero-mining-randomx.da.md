---
title: "Monero Mining: Hvad Gør RandomX så Speciel"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Den 30. november 2019 havde Monero sin halvårlige hårde gaffel, hvor den mest forventede ændring var et skifte fra den gamle PoW-algoritme, cryptonight, til den helt nye, internt udviklede, RandomX. Monero-samfundet mener, at RandomX er et stort skridt i retning af egalitær minedrift, men lad os grave dybere for at se, om det er tilfældet.

## Formål

For at kunne vurdere, om RandomX er en forbedring, skal vi først forstå, hvad formålet med minedrift er. Mining sikrer en blockchain fra dobbeltudgifter via Nakamoto Consensus. De nøjagtige forviklinger af, hvordan det gør dette, ligger uden for rammerne af denne artikel, men de kan læres fra mange forskellige kilder rundt om på internettet. Det vigtige er, at sikkerheden kommer fra hashes genereret af computere (minearbejdere), i konkurrence med hinanden for at finde den matematiske løsning, der er nødvendig for at skabe endnu en blok. Mens de gør dette, tilføjer de nye transaktioner til blockchain. Til gengæld for deres arbejde (hash) bliver de kompenseret med nyslåede mønter.   
  
Der er en række problemer, der kan opstå med denne opsætning, og de kræver passende incitamenter for at fungere korrekt, men vi vil fokusere på et bestemt problem, der kan opstå. Hvis minedrift formodes at være en konkurrence, hvad sker der så, når én minearbejder opnår en fordel?

## Baggrund

For kontekst, lad os tale lidt om minedriftshardware. Minearbejdere bruger computere til at udføre arbejdet, men vi ved alle, at ikke alle computere lavet lige. Nogle computere er kraftige nok til at køre AI-netværk eller intense spil, mens andre kæmper med selv simple opgaver. Disse forskelle i computerkraft påvirker også hash-hastigheden eller den hastighed, hvormed de leder efter blokløsninger.   
  
Men selv disse forskelle mellem computere blegner sammenlignet med hash-raterne for specialiseret hardware, også kendt som Application Specific Integrated Circuits (ASIC'), som udklasser almindelige computere i flere størrelsesordener.  
  
Lad os bruge lidt tid på at udforske, hvad der gør ASIC'er så kraftfulde. Forestil dig, at alle computere falder et sted på et spektrum, som spænder fra at kunne gøre mange ting, men intet godt, til kun at gøre én ting, men at gøre det meget godt. CPU'er og ASIC' i hver sin ende af dette spektrum.  
  
CPU'er, der i alle standardcomputere, i den første ende. De kan gøre mange ting, såsom at surfe på nettet, spille spil eller gengive video, men ikke gøre nogen af dem særlig godt. Men denne fleksibilitet kommer på bekostning af effektivitet.  
  
ASIC'er i den anden ende, hvor de kun kan én ting, men gør det med en utrolig hastighed. De kan kun udføre én matematisk funktion, men fordi de kan ignorere alt andet, præstationsgevinsterne astronomiske. Denne effektivitet kommer dog på bekostning af fleksibilitet, så hvis funktionen ændrer sig lidt – et eksempel x + y = z ændres til 2x + y = z – så vil ASIC helt ophøre med at fungere.   
  
Ikke alle ejer en ASIC, men alle ejer computere. Dette kan føre til en uretfærdig fordel.

## A sjov analogi

If this still is confusing, perhaps the following analogy will help. Imagine a lottery where one thousand dollars is awarded every hour, and this lottery allows you to print your own tickets! You start printing as many tickets as you can on your home printer, which can print one ticket per second. After subtracting electricity and ink costs, you see that you can still make a profit, even if you only win the lottery once every few weeks.  
  
Over time, you expand your operation until you have an entire room dedicated to printers. 20 in all. Everything is fine...until one fateful day.  
  
There’s big news. Someone has invented a new kind of printer. It can only print lottery tickets. It can’t print pictures, or office documents, or do double sided printing. Only lottery tickets. But it can print them at a rate of 1000 tickets per second. You look in your little printer room. 20 printers. You need 980 more printers just to keep up with ONE of these monster printers, and if someone has two…?  
  
You sadly exit the lottery game as you can no longer justify the electricity and ink costs.  
  
But wait! A couple of weeks later there’s more news! The design of the ticket has changed. Now the numbers, which used to be on the top, are now on the bottom. The new monster printers are so inflexible they can’t do it. They could only make the previous design. It’s not long before you’re once again happily printing away. At least until someone makes a new monster printer for the new design.

## RandomX

Hvor passer RandomX ind i alt dette? Det søger at udjævne fordelene ved ASIC'er ved at gøre ASIC'er meget vanskelige at lave. Det gør det ved at kræve, at minearbejdere laver og udfører tilfældig kode i stedet for hashing baseret på en algoritme.  
  
Det kan være forvirrende, hvordan dette faktisk hjælper noget, så lad os gå tilbage til vores printeranalogi. Kan du huske, hvad der skete, da designet ændrede sig? De gamle monsterprintere bliver forældede hver nat, og nye skulle udvikles med det nye design for øje. Hvad ville der ske, hvis hver ny lotteripræmieseddel skulle overholde en ny designstandard for hver ny jackpot?   
  
At skabe en ny monsterprinter ville blive utrolig vanskelig. Du kan ikke bare planlægge et enkelt billetdesign længere. Da designet er tilfældigt, bliver monsterprinterproducenterne nødt til at tilføje farvefunktioner, måder at udskrive forskellige bogstaver og kanter og former på og mere. Kort sagt, den maskine, de endte med at opfinde, ville være en , almindelig printer. Ligesom alle andre har.  
  
Ved blot at implementere denne tilfældighed i billetdesignet, reducerede vi væsentligt den store fordel opnået ved specialiseret hardware. RandomX gør det samme, men med minedrift.  
  
På denne måde minimeres fordelene opnået af nogle få udvalgte velhavende mennesker, som hvis de investerer i at skabe "ASIC'er" til minedrift af RandomX, vil de faktisk blot opfinde stærkere, bedre CPU'er, hvilket gavner verden som helhed.  
  
Det betyder, at den lille fyr med sine 20 billetprintere er tilbage i spillet. Han kan stadig have en sværere tid, da disse velhavende personer stadig kan købe flere printere end ham, men i det mindste nu er han ikke udklasset af størrelsesordener blot fra én maskine. Han er konkurrencedygtig på sin lille måde.  
  
Da vi ved, at selv den lille fyr kan være konkurrencedygtig i minedrift af Monero, opfordrer vi alle til at give det et spin, enten i Monero GUI-pungen, som understøtter solo-mining, eller ved at downloade software, der vedligeholdes af fællesskabet. Det er nemt, konkurrencedygtigt og åbent for alle.

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

  * [Wired Magazine er Forkert Om Monero, Her er Hvorfor](/knowledge/wired-article-debunked)/

  * [Top 15 Monero Myter og Bekymringer Afkræftet](/knowledge/monero-myths-debunked)/

  * [Hvordan Dandelion++ Holder Monero's Transaktion Oprindelse Privat](/knowledge/monero-dandelion)/

  * [Hvorfor Monero Er Open Source Og Decentraliseret](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Hvorfor Monero er bedre end Dash, Zcash, Zcoin (selv med Lelantus), Grin og Bitcoin-mixere som Wasabi (Opdateret maj 2020)](/knowledge/why-monero-is-better)/