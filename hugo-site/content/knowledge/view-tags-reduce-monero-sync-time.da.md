---
title: "Se tags: Hvordan en byte vil reducere Monero wallet-synkroniseringstider med 40 %+"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
En af de mest almindelige klager omkring brugen af Monero dagligt er den tid, det kan tage at synkronisere en tegnebog, før man kan sende Monero. Heldigvis har udviklere og forskere i Monero-fællesskabet fundet en genial måde at reducere den tid, det tager dig at synkronisere din tegnebog med 40 %+ uden ekstra blockchain-bloat, gebyrer osv.

Indtast "se tags", en tilføjelse på én byte til dataene for hver transaktion – kommer til Monero i den næste netværksopgradering!

## Hvorfor er Monero's tegnebog synkronisering langsommere end Bitcoin's?

## Hvorfor er Monero's tegnebog synkronisering langsommere end Bitcoin's?

Et af de første spørgsmål, vi skal besvare for bedre at forstå behovet for en løsning som visningstags, er, hvorfor Moneros tegnebogssynkronisering er langsommere end kryptovalutaer som Bitcoin.

I Bitcoin, da alle transaktioner ikke er private og afslører de brugte mønter, beløbene og de involverede adresser på kæden, kan Bitcoin-punge simpelthen lede efter ubrugte transaktionsoutput (UTXO'er) eller brugte adresser for en given tegnebog , hurtigt at scanne blockchainen for kun UTXO'er, der ejes af disse adresser, for at finde ud af, hvilke mønter der hører til din tegnebog og kan bruges.

I Monero bevarer alle transaktioner brugerens privatliv ved at skjule afsender, modtager og beløb involveret i hver transaktion. Selvom dette privatliv er afgørende for at beskytte brugerne af netværket, introducerer det også langsommere tegnebogssynkronisering. I Monero skal din tegnebog sammenligne alle transaktionsoutput (TXO), der findes på netværket, med din tegnebogs private nøgler.

Denne sammenligning involverer en masse kompleks matematik og kryptografi for at validere, at et output virkelig er dit, da alle beløb, adresser og kendte brugte output (eller mønter) er skjult på kæden i Monero.

## Hvad er udsigt tags?

## Hvad er udsigt tags?

Som en måde at hjælpe med at reducere synkroniseringstiden for Monero tegnebøger, [en forsker ved navn UkoeHB fandt på en ny tilgang](https://github.com/monero-project/research-lab/issues/73) – tilføj et 1-byte "tag" til hver transaktion ved hjælp af en fælles hemmelighed, som kun er kendt af afsenderen og modtageren af den pågældende transaktion .

Denne delte hemmelighed genereres af afsenderen ved hjælp af den adresse, som modtageren har givet dem, og kræver ikke noget aktivt samarbejde fra afsender og modtager. Den første byte (eller karakter) af denne delte hemmelighed føjes derefter til transaktionens data, når den udgives til Monero-netværket.

Når en af deltagerne i den transaktion ønsker at synkronisere deres tegnebog med Monero blockchain bagefter, i stedet for at skulle udføre al den komplekse matematik og kryptografi for hver eneste TXO på netværket, kan tegnebogen nu bare tjekke efter det 1-byte felt i hver transaktion og først derefter udføre den tidskrævende verifikation på transaktioner, der har det tag – 1/256 TXO'er på netværket, for at være præcis!

Dette tag afslører ingen information om transaktionen til eksterne seere, føjer kun 1-byte (et ubetydeligt beløb) til transaktionsstørrelser og giver os alligevel mulighed for at reducere synkroniseringstider med 40 %+ ved at skære ned på de komplekse verifikationer nødvendigt!

## Se tags: en forenklede eksempel

## Se tags: en forenklede eksempel

Forestil dig, at du har 4.096 kasser i et rum, hvoraf kun 5 kasser tilhører dig. Kasserne er alle fuldstændig uadskillelige udefra, og den eneste måde at finde ud af, om en boks er noget for dig, er at åbne den og løse et tidskrævende matematisk problem skrevet ned indeni for at sikre, at det er din.

Forestil dig nu, at du beslutter dig for at få den person, der sender dig disse 5 kasser, til at generere en speciel kode ved hjælp af din adresse, og derefter kun sætte det første tegn i den genererede kode uden på hver boks, der sendes til dig. Alle andre gør det samme for deres kasser (for at sikre, at alle kasser stadig ikke kan skelnes), men nu kan du blot se på den ene tegnkode på ydersiden af boksen og kun åbne de kasser, der har det pågældende tegn på.

Mens andre bokse vil matche din kode, selv nogle der ikke ejes af dig, er antallet af bokse, du skal åbne og løse et matematisk problem på, nu kun 16 (1/256 felter!) i stedet for alle 4.096. 

Nu åbner du de 16 kasser, løser de matematiske problemer og beholder de 5 kasser, der faktisk tilhører dig fra den gruppe!

## Hvornår vil udsigt tags være tilgængelig i Monero?

## Hvornår vil udsigt tags være tilgængelig i Monero?

Se-tags er en af de funktioner, der i øjeblikket er planlagt til medtagelse i [kommende netværksopgradering](https://github.com/monero-project/meta/issues/630), og skulle udgives et stykke tid til foråret. Fællesskabet [hævede 23.3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (i skrivende stund) for at tilskynde til udvikling og implementering af view tags, og som et resultat heraf langt størstedelen af arbejdet med at inkludere view tags i Monero kodebase er allerede færdiggjort af j-berman i samarbejde med anmeldere og forskere.

Når visningstags er håndhævet af netværket, vil alle transaktioner, der sendes efter netværksopgraderingen, drage fordel af den drastisk forbedrede tegnebogssynkroniseringstid. Du behøver ikke at gøre noget særligt for at begynde at bruge visningstags, din yndlingspung til Monero vil simpelthen begynde at bruge dem efter netværksopgraderingen automatisk!

## Hvordan kan jeg lære mere?

## Hvordan kan jeg lære mere?

Hvis dette har vakt din nysgerrighed omkring visningstags, så tag et kig nedenfor for nogle yderligere links, der går i dybden med emnet:

  * [Reducer scanningstider med 1-byte-per-output 'view-tag'](https://github.com/monero-project/research-lab/issues/73)
  * [Føj visningstags til output for at reducere tegnebogens scanningstid](https://github.com/monero-project/monero/pull/8061)

Yderligere læsning

  * [Hvordan Monero unikt aktiverer cirkulær økonomier](/knowledge/monero-circular-economies)/

  * [Monero's ring signaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Hvorfor (og hvordan!) skal du holde dine egne nøgler](/knowledge/hold-your-keys)/

  * [Bidrager tilbage til Monero](/knowledge/contributing-to-monero)/

  * [Hvordan fjern noder påvirker Monero's privatliv](/knowledge/remote-nodes-privacy)/

  * [Hvordan Monero bruger hard-forks til at opgradere den netværk](/knowledge/network-upgrades)/

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