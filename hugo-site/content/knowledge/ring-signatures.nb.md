---
title: "Hvordan ringsignaturer obskure Moneros utganger"
slug: "ring-signatures"
date: "2020-09-08"
image: "/images/rings.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero er kjent over hele kryptoområdet som kongen av personvernmynter. Selv om alle vet at Monero tilbyr godt personvern, er det ikke så mange som forstår hvordan personvernet fungerer.

Mange andre personvernmynter publiserer sammenligningskartinfografikk, som viser navnene på hver mynts personvernteknologi, og i de fleste merker de Moneros teknologi som RingCT, men dette er bare delvis sant. Monero har faktisk en tredelt tilnærming til personvern. Én teknologi for å skjule mottakeren av en transaksjon, én for å skjule beløpet som sendes, og én for å skjule utdataene som brukes, dette er henholdsvis stealth-adresser, RingCT og ringesignaturer.

Denne tredelte tilnærmingen betyr at hvis en av teknologiene er ødelagt, deler ikke de andre nødvendigvis samme skjebne. Ringsignaturer er det svakeste leddet i personvernordningen; ordet svak betyr her den mest utsatte for heuristiske angrep. La oss ta litt tid til å utforske dem, skal vi?

Som nevnt ovenfor, er målet med ringesignaturer å skjule en utgang som brukes i en transaksjon. Hvis "input/output"-terminologien til kryptovaluta er forvirrende for deg, ikke bekymre deg. Det er faktisk ikke så komplisert. Når du hører "output", tenk bare en sjekk. En av de tingene, ikke fullt så vanlig lenger, som folk bruker å betale med. Som en sjekk kan den angis i et hvilket som helst beløp - $10, $32,50, etc - og utveksles mellom transaksjonspartnere. For kryptovalutaer tjener utdata disse funksjonene.

Når noen betaler deg 10 Monero, mottar du en 10 XMR-utgang. Denne utgangen har en verdi (10), og er det som tas fra avsenderens lommebok, på samme måte når du betaler for en tjeneste, forlater en regning din fysiske lommebok og gis til personen du kjøper fra.

Måten utdataene skjules på er ved å konstruere en ring (derav navnet) av lokkeutganger. Men disse lokkefuglene er ikke "falske" utganger. De er reelle tidligere utdata fra blokkjeden som ikke har noe å gjøre med den nåværende transaksjonen, men for en ekstern observatør kan hver av disse utgangene se like sannsynlige ut som den virkelige. Størrelsen på settet med lokkeutganger, pluss den ekte, kalles ringstørrelse, og for øyeblikket er Monero's elleve. Så det er ti lokkeutganger og en ekte.

Hvorfor øker vi ikke dette tallet til 100 eller til og med 1000? Jo flere jo bedre, ikke sant? Vel, fra et personvernperspektiv, ja, men det er andre ting å vurdere. La oss gå tilbake til et fysisk eksempel for å se hva jeg mener. Hvis du ville gjemme en av dollarsedlene dine blant ti lokkefugler, måtte du ha med deg rundt elleve dollar i lommeboken for hver dollar du ville bruke. En ekte dollar og ti falske. Dette blir allerede ganske tungvint hvis du vil bruke enda noen få dollar. Tenk deg nå at vi økte lokkebeløpet til 1000. For hver en dollar du ønsker å bruke, må du bære rundt 1001 dollar. Du må ha med deg en koffert bare for å kjøpe en godteri! Det er viktig å merke seg at ringsignaturer ikke fungerer helt på denne måten, for eksempel er lokkefuglene i seg selv ikke en del av signaturen, bare referanser til dem, men vi håper denne analogien kan være til litt hjelp for å se de grunnleggende konseptene.< /p>

Lokkedrene på blokkjeden fungerer på samme måte. Hvert ekstra lokkemiddel øker tiden og bekreftelseskostnadene for transaksjonen. Hver node må laste ned hele ringsignaturen for hver transaksjon, og hver ringesignatur inneholder den virkelige utgangen, så vel som lokkefuglene. Ikke bare det, men den må verifisere matematikken at minst én av disse utgangene er ekte, og matematikkverifiseringstiden øker også med hvert lokkemiddel. Dette betyr at vi må finne en lykkelig mellomting, der ringstørrelsen er stor nok til å skjule den virkelige produksjonen, selv mot mange heuristiske angrep, men liten nok til å ikke få blokkjeden til å øke i en enorm hastighet. Det er ikke nok å velge et vilkårlig tall, eller å bare øke ringstørrelsen når vi gjør signaturen mindre (for eksempel med CLSAG). Monero-fellesskapet ønsker konkrete, matematiske bevis på hvilken ringstørrelse som gir de beste avveiningene. Et tall for lite, og personvernet vil ikke være sterkt nok mot heuristiske angrep. For stor, og vi får kanskje bare marginale fordeler på personvernsiden, og lider unødvendig med hensyn til skalering.

En siste ting å nevne. Noe Monero-litteratur forenkler og sier at ringsignaturer skjuler avsenderen, men dette er ikke helt sant, og forskjellen er ikke bare pedantisk. Forskjellen mellom avsenderen (et menneske) og en utgang (en regning) er stor når det gjelder å bevare personvernet. Mens en utgang kan ha bånd til en avsender, er ikke en utgang lik en avsender. Så selv om en ringesignatur skulle bli brutt, kobler den ikke nødvendigvis til en persons identitet, og både beløpet og mottakeren er fortsatt skjult, noe som minimerer skaden på personvernet til alle parter.

Det betyr ikke at en ødelagt ringsignatur er ubetydelig. Eventuelle lekkede metadata er dårlige, og har potensial til å avsløre mer informasjon enn vi tror, spesielt når de brukes sammen med andre metadata. Så vi gjør vårt beste for å sikre at den valgte ringestørrelsen har akademisk strenghet bak avgjørelsen, annen metadatalekkasje minimeres, og brukeropplevelsen misligholder de best mulige handlingene.

Men hvis sannsynligheten for en ødelagt signatur fortsatt bekymrer deg, vel, det er noen utrolige nyheter i horisonten. Den neste generasjonen av personvernprotokoller som det jobbes med, som Triptych, Arcturus og Lelantus, har virkelig fine funksjoner. I disse protokollene skaleres størrelsen logaritmisk, ikke lineært, ettersom ringstørrelsen øker. Dette betyr at vi har plass til 100 lokkefugler, men plassen som brukes er nærmere ringstørrelse 10 i den gamle teknologien. Det er ganske forskjellen, og vil forbedre personvernet betydelig.

I katte- og mus-spillet som er privatliv, innoverer Monero kontinuerlig for å ligge i forkant og sikre det beste praktiske personvernet for alle.

Videre lesning