---
title: "Monero's ring signaturer vs CoinJoin som i Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
I takt med at Bitcoins privatlivsværktøjer har fået mere opmærksomhed og brug, er de kommet under mere lovgivningsmæssig kontrol. Denne undersøgelse har ført til en [nylig meddelelse](https://twitter.com/wasabiwallet/status/1503091503207432193) af et Bitcoin-privatlivsværktøj, Wasabi Wallet, at de vil begynde at censurere og afvise indgående input til blandinger, som de anser for ulovlige eller imod deres ToS, og vil betale et kædeanalysefirma for at "dyrlægge" indgående mix-deltagere.

Brugen af CoinJoin-transaktioner til at sløre kilden til midler i Bitcoin har været kernen i Bitcoins privatliv i mange år nu, og de problemer og risici, der er forbundet med dets brug, er nogle af de kerneproblemer, som Moneros ringsignaturer korrigerer og forhindrer. .

I dette blogindlæg vil vi kort dykke ned i en sammenligning af CoinJoin og ringsignaturer, samt hvorfor tilgangen i Monero fører til større censurmodstand, større privatliv og mindre besvær for brugerne.

## Hvad er en CoinJoin transaktion?

## Hvad er en CoinJoin transaktion?

Da alle transaktioner er fuldstændig gennemsigtige i Bitcoin - afslører afsender, modtager og beløb - skal brugere tage ekstra skridt for at bevare deres privatliv fra tidligere afsendere og fremtidige modtagere af deres midler eller risikere censur, overvågning eller tyveri af midler via fysisk vold.

Den bedste løsning i dag til privatliv på Bitcoin er et værktøj kaldet [“CoinJoin”](https://bitcoiner.guide/qna/coinjoin/ ), hvor 2 eller flere brugere arbejder sammen (normalt via en centraliseret koordinator) for at skabe en særlig transaktion, der gør det vanskeligt for eksterne observatører at forbinde inputs med output. Hver deltager kommunikerer for i fællesskab at bygge transaktionen uden at give afkald på forældremyndigheden over deres midler og modtager et output i slutningen, hvis tidligere historie nu er uklar (eller sløret) for eksterne observatører.

Dette bryder historien om specifikke UTXO'er, hvilket giver Bitcoin-brugere mulighed for at få en vis fremadrettet hemmeligholdelse, når de handler. CoinJoin (som implementeret i Wasabi Wallet og Samourai Wallet, de to mest brugte CoinJoin-værktøjer til Bitcoin) har dog et par store ulemper:

  * Da CoinJoin-transaktioner er fuldstændig opt-in og kræver aktiv deltagelse, viser enhver deltager nødvendigvis, at de søger større privatliv end "normale" Bitcoin-brugere, hvilket potentielt udskiller dem og forårsager problemer med at bruge penge på mange regulerede børser eller enheder. Hver bruger kan ikke afvise, at de deltog i en CoinJoin-transaktion.
  * For at finde andre at CoinJoin med, bruger de fleste tilgange til CoinJoin (inklusive Wasabi Wallet) en centraliseret koordinator, der forbinder deltagere og hjælper dem med at kommunikere og opbygge en ordentlig CoinJoin-transaktion. Denne centraliserede koordinator har aldrig forældremyndigheden over brugerens midler, men får omfattende indsigt i de transaktioner, de koordinerer, kan censurere indgående input (som i tilfældet med Wasabi Wallet) og kan blive presset til at indsamle eller dele oplysninger om CoinJoin-deltagere.
  * Brugere med store mængder midler til CoinJoin kan ofte skulle vente timer (eller endda dage!) for at finde nok deltagere at CoinJoin med, hvilket fører til store forsinkelser fra det tidspunkt, hvor en bruger modtager midler, til de kan bruge dem privat. 
  * Det privatliv, som en CoinJoin-transaktion giver, forringes over tid, efterhånden som andre deltagere bruger midler eller forbinder deres output med deres identitet gennem KYC-udvekslinger, ID-krævende købmænd osv. Dette betyder, at brugere ideelt set holder deres midler konstant i gang med CoinJoin-transaktioner for at beholde deres anonymitetssæt ("crowd to hide in") så frisk som muligt.
  * I de fleste tilgange til CoinJoin skal deltagerne bruge en fast størrelse UTXO (dvs. 0,1 BTC) for at gøre det sværere at forbinde input og output af CoinJoin transaktioner. Dette fører til højere gebyrer (flere separate transaktioner nødvendige pr. stort input), mere "giftige ændringer" (midler, der ikke kan bruges uden alvorlige risici for privatlivets fred), og kan udelukke mindre brugere fra overhovedet at kunne blande sig, hvis de ikke har den krævede minimumsaldo.

## Hvordan gør ring signaturer solve disse problemer?

## Hvordan gør ring signaturer solve disse problemer?

Som [har vi tidligere set dybt ind i, hvad ringsignaturer er](/knowledge/ring-signatures), jeg vil ikke gå i detaljer om de tekniske aspekter af, hvordan de fungerer i dette blogindlæg. I stedet vil vi se på, hvordan tilgangene i Monero løser problemerne med CoinJoin diskuterer ovenfor.

> CoinJoin er opt-in og kræver deltagelse

CoinJoin er opt-in og kræver deltagelse

Moneros ringesignaturer er en kernefunktion i privatlivsprotokollen, og _hver_ transaktion på netværket bruger dem. Dette betyder, at ingen brugers transaktioner skiller sig ud for at søge større privatliv end "normale" Monero-brugere, og alle brugere får sandsynligt fornægtelse af, at de har brugt penge i en given transaktion. Da en bruger, der bruger midler, ikke koordinerer eller deltager med lokkedueinput i en transaktion, kan de brugere, der ejer input, der tilfældigvis er valgt som lokkefugle, ærligt sige, at de ikke deltog i den pågældende transaktion, hvilket styrker deres privatliv.

> Brug af en centraliseret koordinator

Brug af en centraliseret koordinator

Da Moneros ringsignaturer er fuldstændig ikke-koordinerede og kun kræver den sande bruger af midler til at oprette transaktionen, er der ikke behov for en centraliseret koordinator i Monero. Dette sikrer, at _ingen_ kan nægte dig adgang til privatlivets fred i Monero, og der er ingen centraliseret enhed, der kan presses, ingen nemme Sybil-angreb på likviditet osv. Så længe din transaktion betaler de korrekte gebyrer , får du ucensurerbar adgang til privatliv, sikkerhed og anonymitet i Monero.

CoinJoin kræver likviditet

Den "likviditet", der er tilgængelig for enhver, der bruger Monero til at bruge som lokkefugle, er altid det samlede sæt af output på kæden, så der er aldrig mangel på lokkefugle at gemme sig i med Monero. En person, der søger at bruge Monero, kan gøre det ~20 minutter efter at have modtaget penge og behøver ikke at udføre yderligere trin for at opnå et stærkt privatliv i Monero.

> CoinJoin privatliv forringes over tid

CoinJoin privatliv forringes over tid

Da Moneros output aldrig er kendt-brugt af netværket, er privatlivets fred, som ringesignaturer giver, meget mindre modtageligt for forringelse over tid. En bruger behøver ikke konstant at churne output i Monero, og uden for ekstremt sjældne omstændigheder mister han intet privatliv, som tiden går.

Hvis en bruger ønsker at "opfriske" lokkefuglene, der bruges med et output, kan de imidlertid blot sende pengene tilbage til sig selv og være i stand til at bruge dem ~20 minutter senere som normalt.

> CoinJoin kræver normalt input i fast størrelse

CoinJoin kræver normalt input i fast størrelse

Da beløb er skjult i hver transaktion ved hjælp af ["Fortrolige transaktioner"](/knowledge/monero-ringct) (en del af "RingCT"), kan lokkefuglene, der bruges i enhver given transaktion, være af enhver størrelse. Der er ingen grund til at være bekymret for beløbsbaserede heuristik i Monero, og så transaktioner er meget nemmere at bygge og kan udnytte lokkefugle fra ethvert tidspunkt og af ethvert beløb på Monero blockchain.

## Hvordan kan jeg lære mere?

## Hvordan kan jeg lære mere?

Hvis du er nysgerrig og vil bedre forstå ringesignaturer eller CoinJoin-transaktioner, kan du se nedenstående links for gode steder at komme i gang:

  * [Hvordan ringesignaturer obskurerer Monero's output](/knowledge/ring-signatures)
  * [Ringsignatur – Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [CoinJoin-oversigt](https://6102bitcoin.com/coinjoin-overview/)

Yderligere læsning

  * [Hvordan Monero unikt aktiverer cirkulær økonomier](/knowledge/monero-circular-economies)/

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

  * [Monero Mining: Hvad Gør RandomX så Speciel](/knowledge/monero-mining-randomx)/

  * [Hvorfor Monero er bedre end Dash, Zcash, Zcoin (selv med Lelantus), Grin og Bitcoin-mixere som Wasabi (Opdateret maj 2020)](/knowledge/why-monero-is-better)/

Yderligere læsning