---
title: "Seraphis: Hva det vil gjøre for Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: en modulær designoppgradering for Monero-transaksjoner

Dette innlegget beskriver [Seraphis](https://github.com/UkoeHB/Seraphis), et sett med transaksjonsprotokollstrukturer og abstraksjoner utviklet av pseudonym forskningsbidragsyter [`koe`](https://github.com/UkoeHB) for Monero-økosystemet, og med pågående sikkerhetsanalyse av pseudonym bidragsyter [`coinstudent2048`](https://github.com/coinstudent2048).  
Vi gjør noen forenklinger og utelater visse tekniske detaljer for oversiktens skyld; av denne grunn, og fordi utformingen av Seraphis fortsatt pågår, bør interesserte lesere henvise til Seraphis-dokumentasjonen for den mest oppdaterte informasjonen.

## Transaksjoner i Monero

Protokoller som Bitcoin og Monero og andre er avhengige av en såkalt "output modell" for operasjon, der en _output_ er en representasjon av verdi som kan overføres.  
Transaksjoner bruker en eller flere utdata kontrollert av en avsender, og genererer nye utdata rettet mot mottakere (eller tilbake til avsenderen som endring); transaksjonen må balansere ved at forbrukte utdata må inneholde en totalverdi nøyaktig lik verdien i nye utganger (pluss et nettverkspålagt gebyr).  
I mange protokoller som Bitcoin, er verdien i en utgang skrevet i klartekst, og det samme er mottakeren.  
Videre, ved å se på blokkjeden, er det trivielt å se om og når en utgang har blitt brukt (det vil si om den har blitt konsumert i en senere transaksjon, og hvilken transaksjon som brukte den).

Derimot introduserer protokoller som Monero en annen design:

  * Utdataverdier er skjult og ikke synlige på blokkjeden
  * Mottakeradresser skjules ved bruk av en engangsadresseringsprotokoll
  * Hvorvidt en utdata er brukt eller ikke, skjules av bruken av tvetydige signaturer

Resultatet er at, fravær av ekstern informasjon, er det vanskelig å fastslå om en gitt utgang er brukt, hva verdien er, og hvem mottakeren er.

Den nåværende Monero-transaksjonsprotokollen kalles _RingCT_ , og bruker flere kryptografiske byggeklosser for å oppnå disse designmålene.

  * _Forpliktelser_ skjuler beløp på en matematisk nyttig måte
  * _Rekkeviddeprøver_ forhindrer overløp som kan blåse opp forsyningen
  * _Ringssignaturer som kan kobles til_ gir undertegner tvetydighet og forhindrer dobbeltbruksforsøk
  * _Forpliktelsesforskyvninger_ hevder at transaksjoner balanserer

Disse byggeklossene er nøye sammenvevd for å bygge RingCT-protokollen.

En nyttig egenskap ved RingCT-protokollen er at noen byggeklosser kan endres eller oppgraderes på en måte som holder den generelle designen og egenskapene intakte, men som kan gi effektivitet eller sikkerhetsforbedringer. Faktisk har denne typen oppgraderinger skjedd (eller er planlagt å skje) flere ganger i Moneros historie. Rekkeviddebevisene i den originale RingCT-protokollen var store og trege; de ble senere oppdatert til en konstruksjon kalt [Bulletproofs](https://eprint.iacr.org/2017/1066) som gjorde transaksjoner mindre og raskere med bedre sikkerhetsanalyse, og er planlagt å bli oppdatert til en nyere konstruksjon kalt [Bulletproofs+](https://eprint.iacr.org/2020/735) for enda større effektivitetsfordeler. 

En lignende prosess ble gjennomgått med byggeblokken for koblingssignatur. I den opprinnelige protokollen ble en konstruksjon kalt [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34) brukt. Denne ble senere oppdatert til en nyere konstruksjon kalt [CLSAG](https://eprint.iacr.org/2019/654) som er raskere, resulterer i mindre transaksjoner og har bedre sikkerhetsanalyse. En enda nyere koblingsbar ringsignaturkonstruksjon basert på [Triptych](https://eprint.iacr.org/2020/018) ble foreslått, men denne ble ikke valgt for distribusjon på grunn av dens innvirkning på multisignaturoperasjoner.

## Seraphis

Seraphis tar denne ideen et skritt videre.  
I stedet for å oppdatere individuelle byggeblokker i den eksisterende RingCT-transaksjonsprotokollen, introduserer den en annen protokoll som kan dra nytte av forskjellige byggeklosser og tilby forbedret funksjonalitet.

## Byggeklosser

Seraphis bruker et annet sett med kryptografiske byggeklosser for å oppnå designmålene sine.

  * _Forpliktelser_ skjuler fortsatt beløp
  * _Rekkeviddeprøver_ forhindrer fortsatt overløp og forsyningsoppblåsing
  * _Medlemskapsbevis_ gir underskriver tvetydighet
  * _Forpliktelsesforskyvninger_ hevder fortsatt balanse
  * _Autoriserende prøvetrykk_ forhindrer dobbeltbruksforsøk

Legg merke til endringen her: koblingsbare ringsignaturer erstattes med en kombinasjon av medlemskapsbevis og autoriserende bevis. Grovt sett viser medlemsbevis at en forbrukt produksjon er en del av et større sett, likt det som skjer i RingCT. Men i motsetning til RingCT, involverer ikke medlemsbevis koblingskoden i det hele tatt! Godkjenningsbevis viser at koblingskoden er gyldig og brukes til å signere den endelige transaksjonen.

Fordi RingCT baker koblingskoden inn i den tvetydige signaturen, er signeringsoperasjoner (og multisignatur) mer beregningsintensive, og det blir mer utfordrende å bygge annen tag-relatert funksjonalitet. Men i Seraphis kan konstruksjon av medlemskapsbevis trygt delegeres fra svært pålitelige enheter (som kan ha begrenset datakraft, som en maskinvarelommebok) til en mindre pålitelig enhet, og signering (og multisignatur) operasjoner er langt enklere ved å bruke det mye enklere autorisasjonsbeviset .

Heldigvis finnes noen av byggeklossene som kreves av Seraphis allerede andre steder, og trenger ikke å designes fra bunnen av. Både Bulletproofs og Bulletproofs+-konstruksjonene kan brukes som rekkeviddebevis. Modifikasjoner av bevissystemer av Schnorr-typen kan brukes for å autorisere bevis. Og et effektivt [prøvesystem](https://eprint.iacr.org/2015/643) som allerede er brukt som grunnlag for Triptych, [Lelantus](https://eprint.iacr.org/2019/373), og [Spark](https://eprint.iacr.org/2021/1173)* kan modifiseres for medlemskapsbevis. X2127X] 

* Cypher Stack mottar midler til Spark-utvikling.

* Cypher Stack mottar midler til Spark-utvikling.

## Adressering

Dessverre er Monero-adresser som er i bruk ikke kompatible med Seraphis. Brukere må generere nye adresser fra lommeboknøklene for å motta Monero hvis Seraphis ble implementert. Denne økosystemkostnaden kommer imidlertid med en rekke fordeler.

Bortsett fra de strukturelle fordelene som er diskutert ovenfor, er Seraphis-designen tilgjengelig for mange forskjellige adressekonstruksjonsmuligheter, som hver kommer med avveininger. Mens den endelige adressekonstruksjonen som skal brukes i Seraphis er [fremdeles under avgjørelse](https://github.com/monero-project/research-lab/issues/92) (ett opplegg som får mye oppmerksomhet kalles [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), kan vi beskrive noen vanlige og nyttige funksjoner.[X908X ] 

Du vet kanskje at Monero-adresser tilbyr _visningsnøkkel_ -funksjonalitet, der du kan gi en visningsnøkkel til en enhet eller tredjepart og la den se etter innkommende utganger på dine vegne, men uten å gi opp forbruk autoritet. Dette er nyttig for lommebøker, som kan holde seg oppdatert samtidig som du holder forbruksnøkkelen din trygt låst. Det er også nyttig for tilfeller der du ønsker ekstern visningstilgang, som en offentlig veldedig organisasjon som tilbyr åpenhet eller et selskap med en regnskapsavdeling.

Ulempen med Monero-visningstaster er at de ikke gir fullstendig eller finmasket visningstilgang. Det er ikke mulig å pålitelig oppdage når en lommebok bruker penger, noe som gjør det vanskelig å beregne lommeboksaldoene riktig når forbruksnøkkelen ikke er tilgjengelig. Det er heller ikke for øyeblikket mulig å oppdage innkommende utdata uten også å lære verdien i disse utdataene (noe som betyr at tredjeparter som er ansvarlige for å finne innkommende utdata vil lære nøyaktig hvor mye Monero du anskaffer).

Seraphis adresseringskonstruksjoner kan løse dette. Med Seraphis er adressen din utstyrt med forskjellige nøkler som kan gjøre forskjellige ting:

  * Se etter innkommende utganger, men skjul verdien deres
  * Se etter innkommende utganger, men vis verdien deres
  * Se etter utgående utganger
  * Hjelpe deg å generere transaksjoner, men ikke signere dem
  * Generer nye adresser (nyttig for forhandlere eller børser med mange kunder)

Som adresseinnehaver kan du bestemme hvor mye autoritet du delegerer til andre enheter eller tredjeparter.

Du vet kanskje at Monero-adresser tilbyr _visningsnøkkel_ -funksjonalitet, der du kan gi en visningsnøkkel til en enhet eller tredjepart og la den se etter innkommende utganger på dine vegne, men uten å gi opp forbruk autoritet. Dette er nyttig for lommebøker, som kan holde seg oppdatert samtidig som du holder forbruksnøkkelen din trygt låst. Det er også nyttig for tilfeller der du ønsker ekstern visningstilgang, som en offentlig veldedig organisasjon som tilbyr åpenhet eller et selskap med en regnskapsavdeling.

Ulempen med Monero-visningstaster er at de ikke gir fullstendig eller finmasket visningstilgang. Det er ikke mulig å pålitelig oppdage når en lommebok bruker penger, noe som gjør det vanskelig å beregne lommeboksaldoene riktig når forbruksnøkkelen ikke er tilgjengelig. Det er heller ikke for øyeblikket mulig å oppdage innkommende utdata uten også å lære verdien i disse utdataene (noe som betyr at tredjeparter som er ansvarlige for å finne innkommende utdata vil lære nøyaktig hvor mye Monero du anskaffer).

Seraphis adresseringskonstruksjoner kan løse dette. Med Seraphis er adressen din utstyrt med forskjellige nøkler som kan gjøre forskjellige ting:

  * Se etter innkommende utganger, men skjul verdien deres
  * Se etter innkommende utganger, men vis verdien deres
  * Se etter utgående utganger
  * Hjelpe deg å generere transaksjoner, men ikke signere dem
  * Generer nye adresser (nyttig for forhandlere eller børser med mange kunder)

Som adresseinnehaver kan du bestemme hvor mye autoritet du delegerer til andre enheter eller tredjeparter.

## Det store bildet

Seraphis er en stor endring i Monero-økosystemet. Selv om det innebærer modifikasjoner av adresser og transaksjonsbyggeblokker, tilbyr designen fleksibilitet og nyttig funksjonalitet som ikke er mulig med dagens RingCT-protokoll. Mens mye av designet er ferdigstilt og utviklet til [en implementering](https://github.com/UkoeHB/monero/tree/seraphis_lib), pågår adressedesign og sikkerhetsanalyse. Seraphis tilbyr en utmerket mulighet til å presse Monero-økosystemet fremover!

Videre lesning

  * [Hvordan Monero unikt muliggjør sirkulære økonomier](/knowledge/monero-circular-economies/)

  * [Moneros ringsignaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Hvorfor (og hvordan!) du bør holde dine egne nøkler](/knowledge/hold-your-keys/)

  * [Bidrar tilbake til Monero](/knowledge/contributing-to-monero/)

  * [Hvordan eksterne noder påvirker Moneros personvern](/knowledge/remote-nodes-privacy/)

  * [Hvordan Monero bruker hard-forks for å oppgradere nettverket](/knowledge/network-upgrades/)

  * [Se tagger: Hvordan én byte vil redusere Monero-lommeboksynkroniseringstiden med 40 %+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool og dens rolle i desentralisering av Monero-gruvedrift](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Er det like privat å konvertere Bitcoin til Monero som å kjøpe Monero direkte?](/knowledge/most-private-way-to-buy-monero/)

  * [Hvorfor Monero bruker et tillitsløst oppsett i motsetning til Zcash](/knowledge/monero-trustless-setup/)

  * [Hvorfor Monero er en bedre butikk med verdi enn Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Hvordan Monero kan overvinne Bitcoins nettverkseffekter](/knowledge/network-effect/)

  * [Hvorfor Monero har det mest kritiske tenkningssamfunnet](/knowledge/critical-thinking/)

  * [Svindel å se etter når du bruker Monero](/knowledge/monero-scams/)

  * [Hvordan Atomic Swaps vil fungere i Monero](/knowledge/monero-atomic-swaps/)

  * [Hva enhver Monero-bruker trenger å vite når det kommer til nettverk](/knowledge/monero-networking/)

  * [Hvordan RingCT skjuler Monero-transaksjonsbeløp](/knowledge/monero-ringct/)

  * [Hvordan Monero Stealth-adresser beskytter identiteten din](/knowledge/monero-stealth-addresses/)

  * [Hvordan Monero-underadresser forhindrer identitetskobling](/knowledge/monero-subaddresses/)

  * [Monero-utganger forklart](/knowledge/monero-outputs/)

  * [Monero beste praksis for nybegynnere](/knowledge/monero-best-practices/)

  * [Hvordan ringsignaturer obskure Moneros utganger](/knowledge/ring-signatures/)

  * [Hvordan Monero løste blokkstørrelsesproblemet som plager Bitcoin](/knowledge/dynamic-block-size/)

  * [Hvordan CLSAG vil forbedre Moneros effektivitet](/knowledge/what-is-clsag/)

  * [Hvorfor Monero har en haleutslipp](/knowledge/monero-tail-emission/)

  * [En kort historie om Monero](/knowledge/monero-history/)

  * [Wired Magazine tar feil om Monero, her er hvorfor](/knowledge/wired-article-debunked/)

  * [Topp 15 Monero-myter og bekymringer avslørt](/knowledge/monero-myths-debunked/)

  * [Hvordan Dandelion++ holder Moneros transaksjonsopprinnelse privat](/knowledge/monero-dandelion/)

  * [Hvorfor Monero er åpen kildekode og desentralisert](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Hva gjør RandomX så spesiell](/knowledge/monero-mining-randomx/)

  * [Hvorfor Monero er bedre enn Dash, Zcash, Zcoin (selv med Lelantus), Grin og Bitcoin-miksere som Wasabi (Oppdatert mai 2020)](/knowledge/why-monero-is-better/)