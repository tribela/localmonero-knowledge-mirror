---
title: "Seraphis: Hvad Det Vil Gør for Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: en modulær design opgradere for Monero transaktioner

Dette indlæg beskriver [Seraphis](https://github.com/UkoeHB/Seraphis), et sæt af transaktionsprotokolstrukturer og abstraktioner udviklet af pseudonym forskningsbidragyder [`koe`](https://github.com/UkoeHB) for Monero-økosystemet og med løbende sikkerhedsanalyse af pseudonym bidragyder [`coinstudent2048`](https://github.com/coinstudent2048).  
Vi foretager nogle forenklinger og udelader visse tekniske detaljer for overskuelighedens skyld; af denne grund, og fordi designet af Seraphis stadig er i gang, bør interesserede læsere henvise til Seraphis-dokumentationen for at få den mest opdaterede information.

## Transaktioner i Monero

Protokoller som Bitcoin og Monero og andre er afhængige af en såkaldt "outputmodel", hvor et _output_ er en repræsentation af værdi, der kan overføres.  
Transaktioner forbruger et eller flere output styret af en afsender og genererer nye output rettet mod modtagere (eller tilbage til afsenderen som ændring); transaktionen skal balancere ved, at forbrugte output skal indeholde en samlet værdi, der nøjagtigt svarer til værdien i nye output (plus et netværkspålagt gebyr).  
I mange protokoller som Bitcoin er værdien indeholdt i et output skrevet i det klare, og det samme er modtageren.  
Ved at se på blockchain er det desuden trivielt at se, om og hvornår et output er blevet brugt (det vil sige, om det er blevet forbrugt i en senere transaktion, og hvilken transaktion brugt det).

Derimod introducerer protokoller som Monero et andet design:

  * Outputværdier er skjulte og ikke synlige på blockchain
  * Modtageradresser er skjult ved brug af en engangsadresseringsprotokol
  * Hvorvidt et output er blevet brugt eller ej, skjules af brugen af tvetydige signaturer

Resultatet er, at det, uden ekstern information, er vanskeligt at afgøre, om et givent output er blevet brugt, hvad dets værdi er, og hvem dets modtager er.

Den nuværende Monero-transaktionsprotokol kaldes _RingCT_ og bruger flere kryptografiske byggeklodser til at nå disse designmål.

  * _Forpligtelser_ skjuler beløb på en matematisk nyttig måde
  * _Rækkeviddebevis_ forhindrer overløb, der kan puste forsyningen op
  * _Ringsignaturer, der kan knyttes_ , giver underskriverens tvetydighed og forhindrer dobbeltforbrugsforsøg
  * _Forpligtelsesudligninger_ hævder, at transaktionerne balancerer

Disse byggeklodser er omhyggeligt sammenflettet for at bygge RingCT-protokollen.

En nyttig egenskab ved RingCT-protokollen er, at nogle byggeklodser kan ændres eller opgraderes på en måde, der holder det overordnede design og egenskaber intakte, men som kan give effektivitets- eller sikkerhedsforbedringer. Faktisk er denne slags opgraderinger forekommet (eller er planlagt til at forekomme) flere gange i Moneros historie. Rækkeviddebeviser i den originale RingCT-protokol var omfangsrige og langsomme; de blev senere opdateret til en konstruktion kaldet [Bulletproofs](https://eprint.iacr.org/2017/1066) der gjorde transaktioner mindre og hurtigere med bedre sikkerhedsanalyse og er planlagt til at blive opdateret til en nyere konstruktion kaldet [Bulletproofs+](https://eprint.iacr.org/2020/735) for endnu større effektivitetsfordele.

En lignende proces blev gennemgået med den sammenknyttede ringsignaturbyggeblok. I den originale protokol, en konstruktion kaldet [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34 ) blev brugt. Dette blev senere opdateret til en nyere konstruktion kaldet [CLSAG](https://eprint.iacr.org/2019/654) det er hurtigere, resulterer i mindre transaktioner og har bedre sikkerhedsanalyse. En endnu nyere linkbar ringsignaturkonstruktion baseret på [Triptykon](https://eprint.iacr.org/2020/018) blev foreslået, men dette blev ikke valgt til implementering på grund af dets indvirkning på multisignaturoperationer.

## Seraphis

Seraphis tager denne idé et skridt videre.  
I stedet for at opdatere individuelle byggeklodser i den eksisterende RingCT-transaktionsprotokol introducerer den en anden protokol, der kan drage fordel af forskellige byggeklodser og tilbyde forbedret funktionalitet.

## Byggeklodser

Seraphis bruger et andet sæt kryptografiske byggeklodser til at nå sine designmål.

  * _Forpligtelser_ skjuler stadig beløb
  * _Rangebevis_ forhindrer stadig overløb og forsyningsinflation
  * _Medlemskabsbeviser_ giver underskriverens uklarhed
  * _Forpligtelsesforskydninger_ hævder stadig balance
  * _Godkendende beviser_ forhindrer dobbeltforbrugsforsøg

Bemærk ændringen her: linkbare ringesignaturer erstattes med en kombination af medlemskabsbeviser og autoriserende beviser. Groft sagt viser medlemsbeviser, at et forbrugt output er en del af et større sæt, svarende til hvad der sker i RingCT. Men i modsætning til RingCT involverer medlemskabsbeviser slet ikke linkings-tagget! Godkendelsesbeviser viser, at det linkende tag er gyldigt og bruges til at underskrive den endelige transaktion.

Fordi RingCT bager linking-tagget ind i den tvetydige signatur, er signerings- (og multisignatur-) operationer mere beregningsintensive, og det bliver mere udfordrende at bygge anden tag-relateret funktionalitet. Men i Seraphis kan konstruktion af medlemskabsbeviser sikkert delegeres fra højt betroede enheder (som kan have begrænset computerkraft, som en hardware tegnebog) til en mindre betroet enhed, og signering (og multisignatur) operationer er langt nemmere ved at bruge det meget simplere godkendelsesbevis .

Heldigvis findes nogle af de byggeklodser, der kræves af Seraphis, allerede andre steder og behøver ikke at designes fra bunden. Både Bulletproofs og Bulletproofs+ konstruktionerne kan bruges som rækkeviddebevis. Ændringer af bevissystemer af Schnorr-typen kan bruges til at godkende beviser. Og et effektivt [prøvesystem](https://eprint.iacr.org/2015/643), der allerede bruges som grundlaget for Triptykon, [Lelantus](https://eprint.iacr.org/2019/373) og [Spark](https://eprint.iacr.org/2021/1173)* kan modificeres for medlemskabsbeviser.

* Cypher Stack modtager støtte til Spark-udvikling.

## Adressering

Desværre er Monero-adresser, der er i brug, ikke kompatible med Seraphis. Brugere ville skulle generere nye adresser fra deres tegnebogsnøgler for at modtage Monero, hvis Seraphis blev implementeret. Disse økosystemomkostninger kommer dog med en række fordele.

Bortset fra de strukturelle fordele, der er diskuteret ovenfor, er Seraphis-designet modtageligt for mange forskellige adressekonstruktionsmuligheder, som hver især kommer med afvejninger. Mens den endelige adressekonstruktion, der skal bruges i Seraphis, er [besluttes stadig](https://github.com/monero-project/research-lab/ issues/92) (en ordning, der får meget opmærksomhed, kaldes [JAMTIS](https://gist .github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), kan vi beskrive nogle almindelige og nyttige funktioner.

Du ved måske, at Monero-adresser tilbyder _visningsnøgle_ -funktionalitet, hvor du kan levere en visningsnøgle til en enhed eller tredjepart og tillade den at se efter indgående udgange på dine vegne, men uden at give op bruge myndighed. Dette er nyttigt til tegnebøger, som kan holde sig opdateret, mens du holder din forbrugsnøgle sikkert låst væk. Det er også nyttigt i tilfælde, hvor du ønsker ekstern visningsadgang, såsom en offentlig velgørenhedsorganisation, der tilbyder gennemsigtighed, eller en virksomhed med en regnskabsafdeling.

Ulempen ved Monero-visningsnøgler er, at de ikke giver fuldstændig eller finmasket visningsadgang. Det er ikke muligt pålideligt at registrere, hvornår en tegnebog bruger penge, hvilket gør det vanskeligt at beregne tegnebogssaldi korrekt, når forbrugsnøglen ikke er tilgængelig. Det er heller ikke i øjeblikket muligt at detektere indgående output uden også at lære værdien indeholdt i disse output (hvilket betyder, at enhver tredjepart, der er ansvarlig for at finde indgående output, vil lære præcis, hvor meget Monero du erhverver).

Seraphis adresseringskonstruktioner kan løse dette. Med Seraphis er din adresse udstyret med forskellige nøgler, der kan gøre forskellige ting:

  * Hold øje med indgående output, men skjul deres værdi
  * Hold øje med indgående output, men vis deres værdi
  * Hold øje med udgående udgange
  * Hjælpe dig med at generere transaktioner, men ikke underskrive dem
  * Generer nye adresser (nyttigt for forhandlere eller børser med mange kunder)

Som adresseindehaver kan du bestemme, hvor meget autoritet du uddelegerer til andre enheder eller tredjeparter.

## Det stor billede

Seraphis er en stor ændring af Monero-økosystemet. Selvom det involverer ændringer af adresser og transaktionsbyggeblokke, tilbyder dets design fleksibilitet og nyttig funktionalitet, som ikke er mulig med dagens RingCT-protokol. Mens meget af designet er færdiggjort og udviklet til [en implementering](https://github.com/UkoeHB/monero/tree/seraphis_lib), adressedesign og sikkerhedsanalyse er i gang. Seraphis tilbyder en fremragende mulighed for at skubbe Monero-økosystemet fremad!

Yderligere læsning

  * [Hvordan Monero unikt aktiverer cirkulær økonomier](/knowledge/monero-circular-economies/)

  * [Monero's ring signaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Hvorfor (og hvordan!) skal du holde dine egne nøgler](/knowledge/hold-your-keys/)

  * [Bidrager tilbage til Monero](/knowledge/contributing-to-monero/)

  * [Hvordan fjern noder påvirker Monero's privatliv](/knowledge/remote-nodes-privacy/)

  * [Hvordan Monero bruger hard-forks til at opgradere den netværk](/knowledge/network-upgrades/)

  * [Se tags: Hvordan en byte vil reducere Monero wallet-synkroniseringstider med 40 %+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool og Dets rolle i Decentralisering Monero Minedrift](/knowledge/p2pool-decentralizing-monero-mining/)

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