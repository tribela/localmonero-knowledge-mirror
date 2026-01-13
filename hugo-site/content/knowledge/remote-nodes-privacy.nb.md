---
title: "Hvordan eksterne noder påvirker Moneros personvern"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
En av de største fordelene Monero har i forhold til andre kryptovalutaer er at det er personvern på kjeden, men har du noen gang lurt på hvordan Moneros personvern holder seg når du bruker en ekstern node? Hva med om du bruker en «lett lommebok»-server som MyMonero?

I dette innlegget skal vi dykke ned i noen av detaljene bak hvordan Monero gir eksepsjonelt personvern i kjeden selv når du bruker en ekstern node, samt hva du bør passe på når du bruker eksterne noder.

## Hvilken funksjon har noder i Monero?

## Hvilken funksjon har noder i Monero?

For de som er mindre kjent med hvordan Monero fungerer, kan nodene (eller serverne) i Monero-nettverket drives av hvem som helst og la eieren av noden – eller andre de velger å dele den med! – å synkronisere en kopi av blokkjeden og gi den kopien til andre på nettverket. Disse nodene verifiserer også alle transaksjoner som skjer på nettverket, samt alle blokker som er publisert og sikrer at de alle følger reglene som er fastsatt ved konsensus.

Den andre funksjonen som noder tjener i Monero, er som en måte å gi alle dataene din favoritt Monero-lommebok trenger for å se etter transaksjoner som tilhører deg og foreta nye transaksjoner. Disse dataene leveres av noder på to måter:

  * Dataene fra hver blokk i blokkjeden blir forespurt av lommeboken, skannet for transaksjoner som tilhører deg, og deretter forkastet når de er kontrollert av lommeboken. 
    * Dette trinnet vil snart bli drastisk forbedret, takket være [visningstagger](/knowledge/view-tags-reduce-monero-sync-time).
  * Når du sender transaksjoner, gir noden du bruker en liste over mulige lokkemidler (eller falske innganger) du kan bruke når du bygger transaksjonen, og sikrer at du har en god mengde å gjemme deg i hver gang du bruker Monero. 
    * Disse lokkefuglene er en del av [ringsignaturer](/knowledge/ring-signatures), en viktig del av Moneros tilnærming til personvern på kjeden.

  * Dette trinnet vil snart bli drastisk forbedret, takket være [visningstagger](/knowledge/view-tags-reduce-monero-sync-time).

  * Disse lokkefuglene er en del av [ringsignaturer](/knowledge/ring-signatures), en viktig del av Moneros tilnærming til personvern på kjeden.

## Hva er den mest private og sikre måten å bruke Monero på?

## Hva er den mest private og sikre måten å bruke Monero på?

Det beste du kan gjøre, selv med det sterke personvernet på kjeden som tilbys av Monero når du bruker eksterne noder, er å kjøre din egen Monero-node for å sikre at du har en uberørt kopi av Monero blockchain tilgjengelig og at din IP-adresse er godt beskyttet. Den andre fordelen når du kjører din egen node er at du kan bidra tilbake til nettverket, la andre noder synkronisere fra noden din eller til og med la andre brukere koble til noden din med lommeboken.

Når det er sagt, gir Monero fortsatt utmerket personvern når du bruker en ekstern node. Hvis du er interessert i å kjøre din egen Monero-node, her er en enkel å følge guide for å gjøre det:

  * [Kjør en Monero Node](https://sethforprivacy.com/guides/run-a-monero-node/)

## Hva kan en ekstern node lære om meg?

## Hva kan en ekstern node lære om meg?

Når du bruker en ekstern node, er det noen få viktige opplysninger som blir eksponert for en ekstern node og et par viktige måter noden kan angripe deg på, hindre deg i å utføre transaksjoner og mer.

Det første en ekstern node kan lære om deg, er den offentlige IP-adressen din. Selv om dette forhåpentligvis vil bli skjult via en VPN eller Tor, kan den eksterne noden knytte din offentlige IP-adresse til transaksjonen, og hjelpe dem med å begrense hvor du handler fra. Den eksterne noden kan også lære den siste blokken lommeboken din synkroniserte og bruke denne til å prøve å gjøre utdannede gjetninger om deg, for eksempel når du vanligvis bruker Monero og når du sist brukte Monero. Dette gjelder spesielt hvis du alltid kommer fra samme IP-adresse (som hjemmet ditt). Den siste nøkkelen som en ekstern node kan lære om deg, er grunnleggende informasjon om transaksjonene du sender gjennom den. Selv om dette kan være de mest åpenbare dataene som den eksterne nodeoperatøren får om deg, er det viktig å forstå at dette kan brukes til å hjelpe med å spore opp avsenderen av transaksjonen når du kombinerer denne informasjonen med andre data utenfor kjeden. Dette kan være spesielt farlig hvis den eksterne noden drives av en ondsinnet enhet, et blokkjedeanalyseselskap eller en undertrykkende nasjonalstat.

En ekstern node kan også forsøke å forårsake problemer ved å skjule blokker for deg, slik at lommeboken din tror at den var synkronisert når den ikke var det. Dette kan få deg til å tro at midler er tapt eller hindre deg i å bruke midler før du kobler til en annen node. Den siste nøkkelen en ekstern node kan gjøre er å mate lommeboken din med en manipulert liste over lokkefugler. Dette kan føre til at lommeboken din enten mislykkes i å bygge transaksjoner (noe som gjør at du ikke kan bruke penger), eller kan tillate den eksterne noden å prøve å gi lokkemidler den vet blir brukt for å redusere anonymiteten du mottar i hver transaksjon.

## Hvilke personverngarantier eksisterer fortsatt når du bruker en ekstern node?

## Hvilke personverngarantier eksisterer fortsatt når du bruker en ekstern node?

Selv om denne artikkelen kan ha skremt deg litt, er det viktig å innse at personvernet levert av Monero er utmerket selv når du bruker en ekstern node, og langt overgår enhver annen kryptovaluta når den brukes på denne måten. Du oppnår fortsatt det sterke personvernet på kjeden levert av Monero, siden den eksterne noden aldri vet den sanne inngangen (hvilke mynter du bruker), mengden Monero brukt i transaksjonen, eller adressen til mottakeren av transaksjonen. Utenfor observatører kan heller ikke se den sanne inngangen, beløpet eller adressene som er involvert (uansett hvilken type node du velger å bruke!), og sikrer at utenfor den eksterne noden til og med din IP-adresse, lommeboksynkroniseringsinformasjon og transaksjoner har sterke personverngarantier .

Den eksterne noden har heller aldri tilgang til de tidligere transaksjonene du har sendt eller mottatt eller mengden Monero i lommeboken din, og mister all synlighet til transaksjonene dine i det øyeblikket du begynner å bruke en annen node. Ingen private nøkler (verken forbruks- eller visningsnøkler) blir noen gang gitt til den eksterne noden, og derfor forblir lommeboken din privat, sikker og brukbar. Uansett ekstern node, er du heller aldri i fare for å miste Monero eller få den stjålet, siden noden ikke kan redigere mottakeradressen, aldri har tilgang til lommebokens private nøkler og ikke kan konfiskere Monero på noen måte.

## Hva med "lette lommebøker" som MyMonero?

## Hva med "lette lommebøker" som MyMonero?

Selv om emnet er litt utenfor rammen av denne artikkelen, ønsket jeg å ta opp en unik type lommebok i Monero – lette lommebøker. Navnet light wallet kommer fra det faktum at lommeboken din (på telefonen eller datamaskinen) ikke trenger å utføre blokkjedesynkronisering, noe som gjør opplevelsen raskere og mer flytende.

Men lommebøker som dette kommer med en alvorlig personvernavveining for nå - lommeboken din sender den private visningsnøkkelen til den eksterne serveren du bruker (som standard i MyMonero), og gir den eksterne serveren full innsyn i alle mottatte midler siden opprettelsen av lommeboken din (og til du slutter å bruke den lommeboken eller frøet). Dette reduserer personvernet du mottar fra nodeoperatøren drastisk, og bør behandles med forsiktighet.

Heldigvis jobber Monero-fellesskapet med å forbedre programvaren du kan bruke til å være vert for din egen light wallet-server (LWS), som lar deg ha rask synkronisering uten å stole på en tredjepart med dine private visningsnøkler – mens du vil kjøre programvaren der lommeboken sender de private visningsnøklene!

For mer om den tilpassede lette lommebokserveren, se Github-depotet nedenfor:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Hvordan kan jeg lære mer?

## Hvordan kan jeg lære mer?

Hvis du er nysgjerrig og gjerne vil forstå noder i Monero bedre og se på hvordan du kan bruke en ekstern node eller kjøre din egen, kan du se koblingene nedenfor for gode steder å komme i gang:

  * [Monero World, en liste over fellesskapsdrevne eksterne noder som kan brukes](https://moneroworld.com/#nodes)
  * [Monero-noder drevet av Seth For Privacy, forfatteren av denne artikkelen](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, en liste over eksterne noder med ofte sjekket status< /a>](https://monero.fail/)
  * [Hvordan koble til til en ekstern node i GUI-lommeboken](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia – ekstern Node](https://www.getmonero.org/resources/moneropedia/remote-node.html)

Videre lesning

  * [Hvordan Monero unikt muliggjør sirkulære økonomier](/knowledge/monero-circular-economies)/

  * [Moneros ringsignaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Hvorfor (og hvordan!) du bør holde dine egne nøkler](/knowledge/hold-your-keys)/

  * [Bidrar tilbake til Monero](/knowledge/contributing-to-monero)/

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

  * [Monero Mining: Hva gjør RandomX så spesiell](/knowledge/monero-mining-randomx)/

  * [Hvorfor Monero er bedre enn Dash, Zcash, Zcoin (selv med Lelantus), Grin og Bitcoin-miksere som Wasabi (Oppdatert mai 2020)](/knowledge/why-monero-is-better)/

Videre lesning