---
title: "Hvordan CLSAG vil forbedre Moneros effektivitet"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Som en protokoll er Monero for tiden i en konstant innovasjonstilstand. Ved å bruke forskning i både on-chain og off-chain løsninger, ser Monero-fellesskapet etter områder som kan forbedres for å gjøre Monero mer privat, mer skalerbar og mer tilgjengelig for alle. En av de nyere innovasjonene er erstatningen av den sammenkoblede ringsignaturordningen, MLSAG, med en drop-in-erstatning CLSAG, som står for Concise Linkable Spontaneous Anonymous Group.

På overflatenivå vil implementeringen av CLSAG redusere de vanligste 2 input, 2 output transaksjonene med 25 %. Vi vil også se en reduksjon på 10 % i bekreftelsestiden.

Men hva er egentlig CLSAG? Hva gjør den, og hvordan skiller den seg fra den gamle versjonen, MLSAG? La oss bruke et minutt på å minne oss selv på hvorfor og hvordan ringsignaturer, slik at vi bedre kan forstå dette konseptet. Ringsignaturer gir mulighet for ikke-interaktive, vitne utskillelige innganger ved bruk av signer-valgte anonymitetssett av tidligere utganger. I lekmenns termer lar det en bruker skjule sine utdata som brukes i en transaksjon sammen med ikke-relaterte utganger, og de kan gjøre alt dette uten at noen andre trenger å delta. Alt du trenger er en kopi av blokkjeden. Hver av disse utgangene ser for det meste ut til å være like sannsynlig å være den faktiske som sendes, og skjuler dermed metadata om avsenderen.

Dette skaper imidlertid litt av et problem. Hva om en bruker skulle konstruere en ringsignatur med alle lokkeutganger? Hvordan kan noen vite at den ukjente avsenderen ikke har myndighet til å sende noen av dem? Ville denne brukeren kunne bruke falske penger? Svaret er nei. Ringsignaturen inkluderer en metode for å bevise at minst én av utgangene eies av den ukjente avsenderen, uten å avsløre hvilken det er. Faktisk er både CLSAG og MLSAG (heretter kjent som SAG-ene) den delen av ringsignaturen som beviser dette. Interessant nok beviser det samtidig at transaksjonsbeløpet, selv om det er skjult bak konfidensielle transaksjoner (RingCT), balanserer. At SAG-ene beviser to ting, at den ene produksjonen eies av noen i ringen, og at transaksjonen balanserer, er viktig, og faktisk hvor størrelsen og verifikasjonsbesparelsene ligger. Hvis dette blir forvirrende, ikke bekymre deg, vi kommer snart til en morsom og lettfattelig analogi.

Det gamle signaturskjemaet, MLSAG (Multilayered Linkable Spontaneous Anonymous Group) beviser de nevnte to tingene i en ringsignatur, men den gjør hver for seg. Bruken av separate beregninger for signering og forpliktelsesnøkler betyr tregere operasjoner. En moderne datamaskin kan gjøre disse beregningene i løpet av millisekunder, noe som ikke virker som mye, og det er det faktisk ikke for en transaksjon. Men når vi tar i betraktning det store antallet transaksjoner på Monero-blokkjeden, og at en node som synkroniseres fra bunnen av må laste ned og verifisere hver av dem, begynner byte og millisekunder å hope seg opp raskt.

CLSAG kombinerer matematikken som er nødvendig for å bevise begge til én, i tillegg til å beregne begge samtidig, og det gjør det på en sikker måte. Hva betyr dette på en sikker måte? Vel, for å rydde opp i dette, samt forhåpentligvis gjøre det hele mer fornuftig, la oss utforske den lovede morsomme analogien.

La oss si at du må gå til både matbutikken og jernvarebutikken for å kjøpe to forskjellige ting: mat og giftige rengjøringskjemikalier. Du vil ikke at de skal blandes sammen, som om det er en ulykke, vil kjemikaliene søle på maten, noe som gjør dem uspiselige. Du bestemmer deg for å være supertrygg og kjøre fra huset til matbutikken, kjøpe maten og deretter kjøre tilbake til huset ditt. Først etter at du har losset maten, setter du deg tilbake i bilen, kjører til jernvarehandelen og tilbake til huset ditt med kjemikaliene. Du har tatt to separate turer for å sikre sikkerheten ved alle kjøp. Selv om det faktisk er trygt, er det ineffektivt. Dette representerer MLSAG, der to forskjellige sett med matematikk er lagret og to forskjellige "turer" blir gjort for å beregne dem.

Du bestemmer deg for at du vil ha en raskere måte å gjøre dette på. Det er for mye bortkastet tid. At du gjør det en eller to ganger kommer ikke til å stjele livet ditt, men å måtte gjøre dette om og om igjen, timene begynner å øke. Du begynner å lure på om du kan ta en tur i stedet. Fra huset ditt, til matbutikken, til jernvarehandelen og hjem igjen. Du kan ikke bare gå og kaste alt i bilen din tilfeldig. Det er ikke trygt. I stedet utpeker du forskjellige steder i bilen din for forskjellige ting, og sørger for at alt passer pent på sin plass. Ved å gjøre det kan du trygt ta en tur til begge butikkene, og holde ting unna hverandre. Dette representerer CLSAG. Det er nå bare ett sett med matematikk lagret i denne transaksjonen for å bevise disse to tingene, og det er gjort på en måte at de ikke forstyrrer hverandre. En tur må fortsatt gjøres, men du har redusert antallet ganske drastisk.

Alt dette høres ganske spennende ut. Er det mulig vi kan finne andre snarveier, eller andre måter å spare tid og plass på? Svaret er ja og nei. Ifølge nåværende MRL-forskere er det sannsynligvis ikke mulig å ytterligere modifisere SAG-type konstruksjoner for bedre størrelse eller hastighet; Imidlertid gir andre konstruksjoner som Arcturus, Omniring, RCT3 eller Triptych mye bedre størrelsesskalering og verifikasjonsfordeler ved bruk av forskjellige matematiske metoder. Hver av disse "neste generasjons"-tilnærmingene til underskriver-tvetydige protokoller kommer imidlertid med sine egne avveininger i implementeringsdetaljer, og er under aktiv forskning og etterforskning.

Tross alt er Monero alltid nyskapende.

Videre lesning

  * [Hvordan Monero unikt muliggjør sirkulære økonomier](/knowledge/monero-circular-economies/)

  * [Moneros ringsignaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Hvorfor (og hvordan!) du bør holde dine egne nøkler](/knowledge/hold-your-keys/)

  * [Bidrar tilbake til Monero](/knowledge/contributing-to-monero/)

  * [Hvordan eksterne noder påvirker Moneros personvern](/knowledge/remote-nodes-privacy/)

  * [Hvordan Monero bruker hard-forks for å oppgradere nettverket](/knowledge/network-upgrades/)

  * [Se tagger: Hvordan én byte vil redusere Monero-lommeboksynkroniseringstiden med 40 %+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool og dens rolle i desentralisering av Monero-gruvedrift](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Hva det vil gjøre for Monero](/knowledge/seraphis-for-monero/)

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

  * [Hvorfor Monero har en haleutslipp](/knowledge/monero-tail-emission/)

  * [En kort historie om Monero](/knowledge/monero-history/)

  * [Wired Magazine tar feil om Monero, her er hvorfor](/knowledge/wired-article-debunked/)

  * [Topp 15 Monero-myter og bekymringer avslørt](/knowledge/monero-myths-debunked/)

  * [Hvordan Dandelion++ holder Moneros transaksjonsopprinnelse privat](/knowledge/monero-dandelion/)

  * [Hvorfor Monero er åpen kildekode og desentralisert](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Hva gjør RandomX så spesiell](/knowledge/monero-mining-randomx/)

  * [Hvorfor Monero er bedre enn Dash, Zcash, Zcoin (selv med Lelantus), Grin og Bitcoin-miksere som Wasabi (Oppdatert mai 2020)](/knowledge/why-monero-is-better/)