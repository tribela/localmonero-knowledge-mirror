---
title: "Monero Outputs Forklaret"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero bruger, ligesom andre kryptovalutaer, output som et middel til at tage højde for midler. Mange kryptokyndige brugere har sikkert hørt dette udtryk før, men ikke alle forstår, hvad de mener, og hvordan de fungerer. Som udforsket i vores [artikel om ringesignaturer](/knowledge/ring-signatures), er output den faktiske enhed, der udveksles på blockchainen mellem transaktionsparter. Svarende til en dollarseddel, men beløbet er ikke i en fast pålydende.

Hvis du får betalt $16 for et job, modtager du muligvis en dollarseddel, en femdollarseddel og en ti dollarseddel. Du har $16, men du har også tre forskellige sedler i din pung. Hvis du ville betale nogen 6 dollars, kunne du bruge 5- og 1-seddelen, men hvis du ville betale nogen $8, kunne du kun bruge $10 og modtage $2 tilbage i bytte. Til sidst, hvis du ville betale nogen $14, skulle du bruge alle tre regninger og ville modtage $2 tilbage i byttepenge, men et øjeblik, når du afleverer alle tre regninger, har du ingen penge i din tegnebog, før du får skift tilbage.

Monero fungerer på samme måde. Antag, at du driver en butik og laver tre salg på tre forskellige varer. Du modtager muligvis 1,5 XMR, 2,25 XMR og 5,25 XMR for i alt 9 XMR, men du har også tre forskellige udgange i din tegnebog af de tidligere nævnte værdier. Ligesom med dollars, vil du måske betale nogen 3 XMR. Du kan kun bruge 5,25 XMR output og modtage 2,25 XMR tilbage i ændring, eller du kan kombinere 1,5 og 2,25 XMR output og få 0,75 XMR tilbage i ændring.

Men så snart du sender transaktionen, bliver de output, du bruger, sat i en "låst" tilstand, hvilket betyder, at de er utilgængelige, indtil du modtager ændringen tilbage. Protokollen låser midlerne op (dvs. giver dig ændringen tilbage) efter 10 bekræftelser eller omkring 20 minutter. Ligesom når du har afleveret dollarsedlerne ud af din pung, kan du ikke bruge pengene igen, før du modtager vekslepengene tilbage fra kassereren, din Monero er utilgængelig, indtil du modtager vekslepengene tilbage.

Lad os gå tilbage til eksemplet med at sende 3 XMR til nogen, og du bruger 5.25 XMR-outputtet. Nu, mens du venter på din 1.75 XMR tilbage i forandring, kan du ikke bruge den. Denne 1,75 XMR er utilgængelig for dig. Men du kan stadig bruge 1,5 XMR og 2,25 XMR output, da disse ikke blev brugt. Hvis du går tilbage til dollar-eksemplet, hvis du betalte nogen $8, som i eksemplet før, ville du ikke være i stand til at bruge de $2, som du forventer tilbage i bytte, før det er givet til dig, men i dette eksempel har du stadig en $10-seddel, der er ubrugt i din tegnebog. Dette kan stadig bruges til at købe, hvad du vil, mens du venter på ændringen. Det samme med Monero.

Dette er ofte et forvirringspunkt for nye Monero-brugere. Ofte kan en bruger bare have ét output i sin tegnebog, modtaget fra en børs eller en ven. Lad os sige, at dette output er 20 XMR. De har ingen andre udgange i deres pung. De ønsker nu at give en donation til to af deres foretrukne velgørenhedsorganisationer. De sender 5 XMR til den første velgørende organisation og er så forvirrede, fordi selvom de skulle have 15 XMR tilbage, kan de ikke umiddelbart sende den næste donation til den anden velgørenhed. Som du måske har gættet, skyldes det, at 15 XMR er låst. Den kan ikke bruges før den er returneret som byttepenge (10 bekræftelser eller omkring 20 minutter). Når deres penge er låst op, vil de være i stand til at sende deres anden donation.

Bare for at gentage pointen, ville de ikke have haft dette problem, hvis de havde haft flere udgange i stedet, såsom to 10 XMR-udgange eller lignende. De ville være i stand til at sende begge donationer lige efter hinanden, fordi den første donation ville bruge en af de 10 XMR-udgange (og vente 10 bekræftelser på at modtage 5 XMR tilbage i bytte), og den anden donation ville bruge de andre 10 XMR output.

Nogle cryptocurrency wallets har en funktion kaldet 'output management', som blot viser en bruger, hvilke output de har i øjeblikket (ud over deres samlede sum), samt giver dem mulighed for at vælge, hvilke de vil bruge, når de bruger deres kryptovaluta.

På nuværende tidspunkt udfører Monero GUI outputvalg for brugere automatisk, da brugere, der vælger deres egne output, ofte fører til forvirring eller i nogle tilfælde skader privatlivets fred. Der er dog tegnebøger under opbygning, såsom det nye Feather wallet-projekt, der vil indeholde disse outputstyringsfunktioner.

Vi har talt meget om den afsendende del, men der sker noget fascinerende i den modtagende ende. Går vi tilbage til vores eksempel på at sende 3 XMR til nogen og bruge dine 1,5 XMR og 2,25 XMR output i transaktionen (mens man forventer 0,75 XMR i ændring), modtager modtageren IKKE to output på 1,5 XMR og 2,25 XMR. De modtager i stedet ONE 3 XMR output.

I baggrunden kombinerer protokollen alle output, der bruges til forbrug, og giver modtageren ét output af det betalte beløb, og sender ét ændringsoutput tilbage til afsenderen. Så afsenderen vil også modtage ét output tilbage som ændring, uanset om de brugte to, tre eller ti output til at sende transaktionen.

Vi håber, at dette har ryddet op i en vis forvirring omkring output, og hvordan den interne bogføring af protokollen fungerer, såvel som det almindelige bruger, der står over for problem med forvirring, når de støder på låste midler. I en anden artikel vil vi undersøge, hvordan du administrerer dine output for at minimere chancen for at skulle vente på ulåste midler, før du sender fremtidige transaktioner.

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