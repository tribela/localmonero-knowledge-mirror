---
title: "Moneros ringsignaturer vs CoinJoin som i Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Ettersom Bitcoins personvernverktøy har fått mer oppmerksomhet og bruk, har de kommet under mer regulatorisk gransking. Denne granskingen har ført til en [nylig kunngjøring](https://twitter.com/wasabiwallet/status/1503091503207432193) fra et Bitcoin personvernverktøy, Wasabi Wallet, om at de vil begynne å sensurere og avvise innkommende innganger til blandinger som de anser som ulovlige eller mot deres ToS, og vil betale en kjedeanalyse selskap for å "veterlege" innkommende miksdeltakere.

Bruken av CoinJoin-transaksjoner for å skjule kilden til midler i Bitcoin har vært kjernen i Bitcoins personvern i mange år nå, og problemene og risikoene som ligger i bruken av det er noen av kjerneproblemene som Moneros ringsignaturer korrigerer og forhindrer. .

I dette blogginnlegget skal vi kort dykke ned i en sammenligning av CoinJoin og ringsignaturer, samt hvorfor tilnærmingen i Monero fører til større sensurmotstand, større personvern og mindre problemer for brukerne.

## Hva er en CoinJoin-transaksjon?

Ettersom alle transaksjoner er helt gjennomsiktige i Bitcoin – som avslører avsender, mottaker og beløp – må brukere ta ekstra skritt for å bevare personvernet sitt fra tidligere avsendere og fremtidige mottakere av deres midler eller risikere sensur, overvåking eller tyveri av midler via fysisk vold.

Den beste løsningen i dag for personvern på Bitcoin er et verktøy kalt [“CoinJoin”](https://bitcoiner.guide/qna/coinjoin/), der 2 eller flere brukere jobber sammen (vanligvis via en sentralisert koordinator) for å lage en spesiell transaksjon som gjør det vanskelig for utenforstående. observatører for å koble inngangene til utgangene. Hver deltaker kommuniserer for å bygge transaksjonen i fellesskap uten å gi fra seg forvaring av sine midler, og mottar et utdata på slutten hvis tidligere historie nå er uklar (eller tilslørt) for observatører utenfor.

Dette bryter historien til spesifikke UTXO-er, og lar Bitcoin-brukere få en viss hemmelighold når de handler. Imidlertid har CoinJoin (som implementert i Wasabi Wallet og Samourai Wallet, de to mest brukte CoinJoin-verktøyene for Bitcoin) noen få store ulemper:

  * Ettersom CoinJoin-transaksjoner er fullstendig opt-in og krever aktiv deltakelse, viser enhver deltaker nødvendigvis at de søker større privatliv enn "normale" Bitcoin-brukere, og potensielt skiller dem ut og forårsake problemer med å bruke penger på mange regulerte børser eller enheter. Hver bruker kan ikke benekte at de deltok i en CoinJoin-transaksjon.
  * For å finne andre å CoinJoin med, bruker de fleste tilnærminger til CoinJoin (inkludert Wasabi Wallet) en sentralisert koordinator som forbinder deltakerne og hjelper dem med å kommunisere og bygge en skikkelig CoinJoin-transaksjon. Denne sentraliserte koordinatoren har aldri varetekt over brukerens midler, men får omfattende innsikt i transaksjonene de koordinerer, kan sensurere innkommende inndata (som i tilfellet med Wasabi Wallet), og kan bli presset til å samle eller dele informasjon om CoinJoin-deltakere.[X2068X ] 
  * Brukere med store mengder midler til CoinJoin kan ofte måtte vente timer (eller til og med dager!) for å finne nok deltakere å CoinJoin med, noe som fører til store forsinkelser fra det tidspunktet en bruker mottar midler til de kan bruke dem privat. 
  * Personvernet som tilbys av en CoinJoin-transaksjon forringes over tid ettersom andre deltakere bruker midler eller kobler utdataene deres til identiteten deres gjennom KYC-utvekslinger, ID-krevende selgere osv. Dette betyr at brukerne ideelt sett holder pengene sine konstant i CoinJoin-transaksjoner for å beholde anonymitetssettet deres («publikum å gjemme seg i») så ferskt som mulig.
  * I de fleste tilnærminger til CoinJoin må deltakerne bruke en fast størrelse UTXO (dvs. 0,1 BTC) for å gjøre det vanskeligere å koble til innganger og utganger for CoinJoin-transaksjoner. Dette fører til høyere gebyrer (flere separate transaksjoner nødvendig per stor innsats), mer "giftig endring" (midler som ikke kan brukes uten alvorlig risiko for personvernet), og kan hindre mindre brukere fra å kunne blande seg i det hele tatt hvis de ikke har minimumssaldoen som kreves.

## Hvordan løser ringsignaturer disse problemene?

Som [vi har sett dypt på hva ringsignaturer er tidligere](/knowledge/ring-signatures), vil jeg ikke gå i detalj på de tekniske aspektene ved hvordan de fungerer i dette blogginnlegget. I stedet skal vi se på hvordan tilnærmingene tatt i Monero løser problemene med CoinJoin diskuterer ovenfor.

> CoinJoin er opt-in og krever deltakelse

Moneros ringesignaturer er en kjernefunksjon i personvernprotokollen, og _hver_ transaksjon på nettverket bruker dem. Dette betyr at ingen brukers transaksjoner skiller seg ut for å søke større personvern enn "normale" Monero-brukere, og alle brukere får sannsynlig benektelse for at de brukte penger i en gitt transaksjon. Siden en bruker som bruker penger ikke koordinerer eller deltar med lokkeinndataene i en transaksjon, kan de brukerne som eier input som tilfeldigvis er valgt som lokkefugler ærlig si at de ikke deltok i den transaksjonen, noe som styrker deres personvern.

> Bruk av en sentralisert koordinator

Ettersom Moneros ringsignaturer er fullstendig ikke-koordinerte og bare krever den sanne pengebrukeren for å opprette transaksjonen, er det ikke behov for en sentralisert koordinator i Monero. Dette sikrer at _ingen_ kan nekte deg tilgang til personvern i Monero, og det er ingen sentralisert enhet som kan bli presset, ingen enkle Sybil-angrep på likviditet osv. Så lenge transaksjonen din betaler de riktige gebyrene, du får usensurerbar tilgang til personvern, sikkerhet og anonymitet i Monero.

> CoinJoin krever likviditet

"Likviditeten" som er tilgjengelig for alle som bruker Monero for å bruke som lokkeduer er alltid det totale settet med utganger på kjeden, så det er aldri mangel på lokkeduer å gjemme seg i med Monero. Noen som ønsker å bruke Monero kan gjøre det ca. 20 minutter etter å ha mottatt midler, og trenger ikke å utføre noen ekstra trinn for å få et sterkt personvern i Monero.

> CoinJoin-personvernet forringes over tid

Ettersom Moneros utganger aldri er kjent-brukt av nettverket, er personvernet gitt av ringsignaturer mye mindre utsatt for forringelse over tid. En bruker trenger ikke konstant å churne utganger i Monero, og utenom ekstremt sjeldne omstendigheter mister han ikke noe privatliv ettersom tiden går.

Hvis en bruker ønsker å "oppdatere" lokkefuglene som brukes med en utgang, kan de imidlertid bare sende pengene tilbake til seg selv og bruke dem ~20 minutter senere som vanlig.

> CoinJoin krever vanligvis innganger med fast størrelse

Ettersom beløp er skjult i hver transaksjon som bruker [«Konfidensielle transaksjoner»](/knowledge/monero-ringct) (en del av «RingCT»), kan lokkefuglene som brukes i en gitt transaksjon være av hvilken som helst størrelse. Det er ingen grunn til å være bekymret for beløpsbaserte heuristikk i Monero, og derfor er transaksjoner mye enklere å bygge og kan utnytte lokkeduer fra ethvert tidspunkt og uansett beløp på Monero-blokkjeden.

## Hvordan kan jeg lære mer?

Hvis du er nysgjerrig og ønsker å bedre forstå ringsignaturer eller CoinJoin-transaksjoner, se lenkene nedenfor for gode steder å komme i gang:

  * [Hvordan ringesignaturer obskurer Moneros utganger](/knowledge/ring-signatures)
  * [Ringsignatur – Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [CoinJoin-oversikt](https://6102bitcoin.com/coinjoin-overview/)

Videre lesning