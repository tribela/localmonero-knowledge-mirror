---
title: "Hva enhver Monero-bruker trenger å vite når det kommer til nettverk"
slug: "monero-networking"
date: "2020-11-11"
image: "/images/networking.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Det burde ikke komme som en overraskelse for noen at Monero, og faktisk all kryptovaluta, kjører på internett. Og likevel, selv om denne uttalelsen virker grunnleggende og åpenbar, vurderer mange ikke implikasjonene av hva dette betyr i forhold til deres privatliv. Med andre ord, det er noen ting Monero kan og ikke kan beskytte mot, bare av natur å kjøre på internett. Noen av disse hensynene er bare ulemper, mens andre er mye mer alvorlige i et scenario der absolutt personvern kreves. La oss ta oss tid til å bli kjent med hvordan Monero-brukere samhandler med hverandre på nettverket, og hva dette betyr for personvernet deres.

Begynner på den trivielle siden av ting, hvis en bruker ikke har tilgang til internett, kan de ikke laste ned nye blokker, spre transaksjoner på vegne av andre eller sende egne transaksjoner. En interessant ting å merke seg er at en bruker med en full node uten internettilgang kan konstruere en transaksjon offline som kan sendes senere. Dette er fordi en ringsignatur bare trenger utganger fra blokkjeden å gjemme seg med. En kort påminnelse om [hvordan ringesignaturer fungerer](/knowledge/ring-signatures), den skjuler den virkelige utgangen som en bruker sender blant en samling ikke-tilknyttede utganger valgt fra fortiden. Hvis brukeren har tilgang til disse utgangene i form av en fullstendig nedlastet blokkjede (full node), kan de lage ringsignaturen fra tidligere utganger, og når internettforbindelsen gjenopptas, spre transaksjonen til nettverket.

En bruker som bruker en ekstern node kan ikke gjøre dette, for når de konstruerer ringesignaturen sin, kontakter de den eksterne fullnoden for utganger som skal inkluderes i ringsignaturen. Ingen internett betyr at de ikke kan nå denne noden, så de har ikke konstruksjonsmuligheter for offline transaksjoner.

Før vi fortsetter med noen av personvernhensynene, la oss ha en kort innføring i hvordan internett fungerer som helhet. Hele internett er ikke annet enn datamaskiner som kobler seg til andre datamaskiner. Det er det. Bloggen du liker å lese? Bare noen filer som ligger på en annens datamaskin. Denne nettsiden du leser denne artikkelen på (LocalMonero)? Filer og kode lagret på en datamaskin et sted. Selv store gale nettsteder fungerer på denne måten. Ta YouTube for eksempel. Bare videofiler som ligger på Googles gigantiske datasystemer, og du kobler til dem for å laste ned videoen til din egen datamaskin slik at du kan se den.

Disse datamaskinene kan skille hverandre fordi hver eneste datamaskin som er koblet til internett, får et unikt identifikasjonsnummer som kalles en IP-adresse. Disse er vanligvis fire sett med tall atskilt med punktum, for eksempel: 172.66.35.7. Det er viktig å ha dette i bakhodet når vi vurderer hvordan Monero-informasjon flyttes rundt på internett. Monero er et peer-to-peer-nettverk (P2P), som betyr at datamaskiner kobles direkte til hverandre i stedet for å bruke en mellommann. Så når en brukers fulle node laster ned en nyoppdaget blokk, laster de den ikke ned fra en sentral server, men fra sine jevnaldrende. Ulempen med dette er at siden brukere kobler til hverandre direkte, kjenner de hverandres IP-adresser.

Vel? Hva er problemet? Det er bare et tall, ikke sant? Ikke akkurat. IP-adressene i seg selv inneholder informasjon om brukeren, for eksempel opprinnelseslandet og nettverksleverandøren, men enda verre, internettleverandører (ISP-er) vet IP-adressen til hver person som bruker deres tjenester. Dette betyr at disse Internett-leverandørene og de de jobber med kan se en brukers internetttrafikk og, ved hjelp av noen smarte taktikker, oppdage at de bruker Monero. Nå før du blir redd, legg merke til ordlyden der. Alt disse snokerne kan gjøre er å se at en person kobler seg til andre noder på Monero-nettverket. På grunn av Moneros personvernteknologi lekkes det ikke noe annet om individet. Ikke om de kjører en node eller ikke, eller om/når de sender transaksjoner, og hvis en transaksjon sendes, er ingen av informasjonen kjent. Alt disse Internett-leverandørene kan se er at en av brukerne deres kobler til Monero-nettverket.

Nå, for noen mennesker, noen steder, kan denne informasjonen alene være nok til å skade omdømme eller frihet. Eller kanskje ideen om at noen invaderer privatlivet ditt og hva du gjør på internett, uansett grunn, ikke er akseptabelt for deg. Disse personene oppfordres til kun å koble seg til Monero-nettverket ved å bruke VPN, Tor eller I2P, som alle er tjenester som skjuler en brukers IP-adresse for andre, samt skjuler hva en bruker gjør fra sin ISP. Forskjellene mellom disse tjenestene ligger utenfor rammen av denne artikkelen, men det er mange artikler av høy kvalitet skrevet om emnet, så bekymrede brukere oppfordres til å studere det!

For resten av oss tror vi kanskje at det ikke er så stor sak å ha andre som vet at vi er koblet til Monero-nettverket. Tross alt er det faktiske innholdet i transaksjonene våre, eller hvis vi i det hele tatt sender noen, skjult for offentligheten, så hva er skaden? Selv om dette kan være sant, oppfordres brukere til å vurdere det faktum at hovedtrekket for kryptovalutaer er å være deres egen bank. Når du holder din private nøkkel, og hvis noe skjer med den, kan ingen hjelpe deg med å gjenopprette dine tapte midler.

Å være din egen bank betyr å vurdere, ikke bare din digitale sikkerhet, men også din fysiske sikkerhet. Det kan godt være at kunnskapen om en person som kobler seg til Monero-nettverket kan bringe uønsket oppmerksomhet, ikke nødvendigvis fra storskalaaktører som nasjonalstater, men mindre aktører med egoistisk interesse, som hackere som ønsker å tjene penger. Det er faktisk utallige historier over hele kryptorommet om slike scenarier som faktisk finner sted.

Denne artikkelen er ikke ment å frykte eller skremme, men snarere oppfordre brukere til å undersøke hvilke metoder for nettsurfingbeskyttelse som er riktige for dem. Den gode nyheten er at disse ferdighetene også vil overføres til generell internettbruk, ikke bare Monero-bruk, og som sådan, i vår stadig mer Internett-tilkoblede verden, kan ikke en erfaren bruker gå galt med å samle riktig kunnskap og ferdigheter for å holde seg trygg og virkelig være deres egen bank.

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