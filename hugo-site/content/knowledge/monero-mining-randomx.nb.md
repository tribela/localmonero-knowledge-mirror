---
title: "Monero Mining: Hva gjør RandomX så spesiell"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Den 30. november 2019 hadde Monero sin halvårlige hardgaffel, med den mest etterlengtede endringen en overgang fra den gamle PoW-algoritmen, cryptonight, til den helt nye, internt utviklede, RandomX. Monero-fellesskapet mener RandomX er et stort skritt mot egalitær gruvedrift, men la oss grave dypere for å se om det er tilfelle.

## Hensikt

For å bedømme om RandomX er en forbedring, må vi først forstå hva hensikten med gruvedrift er. Mining sikrer en blokkjede fra doble forbruk via Nakamoto Consensus. De nøyaktige vanskelighetene ved hvordan den gjør dette er utenfor rammen av denne artikkelen, men de kan læres fra mange forskjellige kilder rundt på internett. Det som betyr noe er at sikkerheten kommer fra hash generert av datamaskiner (gruvearbeidere), i konkurranse med hverandre for å finne den matematiske løsningen som er nødvendig for å lage en ny blokk. Mens de gjør dette, legger de til nye transaksjoner til blokkjeden. Til gjengjeld for sitt arbeid (hash) blir de kompensert med nypregede mynter.   
  
Det er en rekke problemer som kan oppstå med dette oppsettet, og de krever riktige insentiver for å fungere riktig, men vi skal fokusere på ett spesielt problem som kan oppstå. Hvis gruvedrift er ment å være en konkurranse, hva skjer når en gruvearbeider får en fordel?

## Bakgrunn

For kontekst, la oss snakke litt om gruvemaskinvare. Gruvearbeidere bruker datamaskiner for å gjøre jobben, men vi vet alle at ikke alle datamaskiner er laget like. Noen datamaskiner er kraftige nok til å kjøre AI-nettverk eller intense spill, mens andre sliter med selv enkle oppgaver. Disse forskjellene i datakraft påvirker også hashhastigheten, eller hastigheten de ser etter blokkløsninger med.   
  
Men selv disse forskjellene mellom datamaskiner blekner sammenlignet med hashhastighetene til spesialisert maskinvare, ellers kjent som Application Specific Integrated Circuits (ASICs), som utklasser vanlige datamaskiner med flere størrelsesordener.  
  
La oss ta litt tid til å utforske hva som gjør ASIC-er så kraftige. Se for deg at alle datamaskiner faller et sted på et spektrum, som spenner fra å kunne gjøre mange ting, men ingenting bra, til å gjøre bare én ting, men å gjøre det veldig bra. CPU-er og ASIC-er er i motsatte ender av dette spekteret.  
  
CPUer som er i alle standard datamaskiner er i den første enden. De kan gjøre mange ting, som å surfe på nettet, spille spill eller gjengi video, men ikke gjøre noen av dem spesielt godt. Men denne fleksibiliteten kommer på bekostning av effektivitet.  
  
ASIC-er er i den andre enden, hvor de bare kan én ting, men gjør det i en utrolig hastighet. De kan bare utføre én matematisk funksjon, men fordi de kan ignorere alt annet, er ytelsesgevinstene astronomiske. Denne effektiviteten kommer imidlertid på bekostning av fleksibilitet, så hvis funksjonen endres til og med litt - et eksempel er x + y = z endres til 2x + y = z - så vil ASIC slutte å fungere helt.   
  
Ikke alle eier en ASIC, men alle eier datamaskiner. Dette kan føre til en urettferdig fordel.

## En morsom analogi

Hvis dette fortsatt er forvirrende, vil kanskje følgende analogi hjelpe. Se for deg et lotteri hvor tusen dollar deles ut hver time, og dette lotteriet lar deg skrive ut dine egne lodd! Du begynner å skrive ut så mange billetter du kan på hjemmeskriveren, som kan skrive ut én billett per sekund. Etter å ha trukket fra strøm- og blekkkostnader ser du at du fortsatt kan tjene penger, selv om du bare vinner i lotto en gang med noen ukers mellomrom.  
  
Over tid utvider du driften til du har et helt rom dedikert til skrivere. 20 i alt. Alt er bra ... helt til en skjebnesvanger dag.  
  
Det er store nyheter. Noen har funnet opp en ny type skriver. Den kan kun skrive ut lodd. Den kan ikke skrive ut bilder eller kontordokumenter, eller gjøre dobbeltsidig utskrift. Kun lodd. Men den kan skrive dem ut med en hastighet på 1000 billetter per sekund. Du ser på det lille skriverrommet ditt. 20 skrivere. Du trenger 980 flere skrivere bare for å holde tritt med EN av disse monsterskriverne, og hvis noen har to...?  
  
Dessverre forlater du lottospillet siden du ikke lenger kan rettferdiggjøre strøm- og blekkkostnadene.  
  
Men vent! Et par uker senere er det flere nyheter! Utformingen av billetten er endret. Nå er tallene, som pleide å være på toppen, nå på bunnen. De nye monsterskriverne er så lite fleksible at de ikke kan gjøre det. De kunne bare lage det forrige designet. Det er ikke lenge før du igjen er fornøyd med å skrive ut. I hvert fall inntil noen lager en ny monsterprinter til det nye designet.

## RandomX

Hvor passer RandomX inn i alt dette? Den søker å jevne ut fordelen ved ASIC-er ved å gjøre ASIC-er veldig vanskelig å lage. Den gjør dette ved å kreve at gruvearbeidere lager og kjører tilfeldig kode i stedet for hashing basert på en algoritme.  
  
Det kan være forvirrende hvordan dette faktisk hjelper noe, så la oss gå tilbake til skriveranalogien vår. Husker du hva som skjedde da designet endret seg? De gamle monsterprinterne blir foreldet hver kveld, og nye måtte utvikles med tanke på det nye designet. Hva ville skje hvis hver nye lottopremie måtte følge en ny designstandard for hver ny jackpot?   
  
Å lage en ny monsterskriver ville blitt utrolig vanskelig. Du kan ikke bare planlegge på ett billettdesign lenger. Siden designet er tilfeldig, må produsentene av monsterskrivere legge til fargefunksjoner, måter å skrive ut forskjellige bokstaver og rammer og former og mer på. Kort sagt, maskinen de endte opp med å finne opp ville være en standard, vanlig skriver. Akkurat som alle andre har.  
  
Ved ganske enkelt å implementere denne tilfeldigheten i billettdesignet, reduserte vi den store fordelen som ble oppnådd med spesialisert maskinvare. RandomX gjør det samme, men med mining.  
  
På denne måten minimeres fordelene oppnådd av noen få utvalgte velstående mennesker, som om de investerer i å lage "ASICs" for gruvedrift av RandomX, vil de faktisk bare finne opp sterkere, bedre CPUer, noe som gagner verden for øvrig.  
[] X1455X] Dette betyr at den lille fyren med sine 20 billettskrivere er tilbake i spillet. Han kan fortsatt ha en vanskeligere tid siden disse velstående personene fortsatt kan kjøpe flere skrivere enn ham, men nå er han i det minste ikke utklasset av størrelsesordener bare fra én maskin. Han er konkurransedyktig på sin lille måte.  
  
Når vi vet at selv den lille fyren kan være konkurransedyktig i gruvedrift av Monero, oppfordrer vi alle til å ta en tur, enten i Monero GUI-lommeboken, som har støtte for solo mining, eller ved å laste ned programvare som vedlikeholdes av fellesskapet. Det er enkelt, konkurransedyktig og åpent for alle.

Videre lesning

  * [Hvordan Monero unikt muliggjør sirkulære økonomier](/knowledge/monero-circular-economies)/

  * [Moneros ringsignaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Hvorfor (og hvordan!) du bør holde dine egne nøkler](/knowledge/hold-your-keys)/

  * [Bidrar tilbake til Monero](/knowledge/contributing-to-monero)/

  * [Hvordan eksterne noder påvirker Moneros personvern](/knowledge/remote-nodes-privacy)/

  * [Hvordan Monero bruker hard-forks for å oppgradere nettverket](/knowledge/network-upgrades)/

  * [Se tagger: Hvordan én byte vil redusere Monero-lommeboksynkroniseringstiden med 40 %+](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool og dens rolle i desentralisering av Monero-gruvedrift](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Hva det vil gjøre for Monero](/knowledge/seraphis-for-monero)/

  * [Er det like privat å konvertere Bitcoin til Monero som å kjøpe Monero direkte?](/knowledge/most-private-way-to-buy-monero)/

  * [Hvorfor Monero bruker et tillitsløst oppsett i motsetning til Zcash](/knowledge/monero-trustless-setup)/

  * [Hvorfor Monero er en bedre butikk med verdi enn Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Hvordan Monero kan overvinne Bitcoins nettverkseffekter](/knowledge/network-effect)/

  * [Hvorfor Monero har det mest kritiske tenkningssamfunnet](/knowledge/critical-thinking)/

  * [Svindel å se etter når du bruker Monero](/knowledge/monero-scams)/

  * [Hvordan Atomic Swaps vil fungere i Monero](/knowledge/monero-atomic-swaps)/

  * [Hva enhver Monero-bruker trenger å vite når det kommer til nettverk](/knowledge/monero-networking)/

  * [Hvordan RingCT skjuler Monero-transaksjonsbeløp](/knowledge/monero-ringct)/

  * [Hvordan Monero Stealth-adresser beskytter identiteten din](/knowledge/monero-stealth-addresses)/

  * [Hvordan Monero-underadresser forhindrer identitetskobling](/knowledge/monero-subaddresses)/

  * [Monero-utganger forklart](/knowledge/monero-outputs)/

  * [Monero beste praksis for nybegynnere](/knowledge/monero-best-practices)/

  * [Hvordan ringsignaturer obskure Moneros utganger](/knowledge/ring-signatures)/

  * [Hvordan Monero løste blokkstørrelsesproblemet som plager Bitcoin](/knowledge/dynamic-block-size)/

  * [Hvordan CLSAG vil forbedre Moneros effektivitet](/knowledge/what-is-clsag)/

  * [Hvorfor Monero har en haleutslipp](/knowledge/monero-tail-emission)/

  * [En kort historie om Monero](/knowledge/monero-history)/

  * [Wired Magazine tar feil om Monero, her er hvorfor](/knowledge/wired-article-debunked)/

  * [Topp 15 Monero-myter og bekymringer avslørt](/knowledge/monero-myths-debunked)/

  * [Hvordan Dandelion++ holder Moneros transaksjonsopprinnelse privat](/knowledge/monero-dandelion)/

  * [Hvorfor Monero er åpen kildekode og desentralisert](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Hvorfor Monero er bedre enn Dash, Zcash, Zcoin (selv med Lelantus), Grin og Bitcoin-miksere som Wasabi (Oppdatert mai 2020)](/knowledge/why-monero-is-better)/