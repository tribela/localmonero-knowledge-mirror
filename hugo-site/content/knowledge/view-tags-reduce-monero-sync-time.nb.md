---
title: "Se tagger: Hvordan én byte vil redusere Monero-lommeboksynkroniseringstiden med 40 %+"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
En av de vanligste klagene rundt bruk av Monero daglig er tiden det kan ta å synkronisere en lommebok før du kan sende Monero. Heldigvis har utviklere og forskere i Monero-fellesskapet funnet en glimrende måte å redusere tiden det tar deg å synkronisere lommeboken din med 40 %+ uten ekstra blokkjedeoppblåsthet, gebyrer osv.

Skriv inn «vis tags», et tillegg på én byte til dataene for hver transaksjon – kommer til Monero i neste nettverksoppgradering!

## Hvorfor er Moneros lommeboksynkronisering tregere enn Bitcoins?

Et av de første spørsmålene vi må svare på for å bedre forstå behovet for en løsning som visningskoder, er hvorfor Moneros lommeboksynkronisering er tregere enn kryptovalutaer som Bitcoin.

I Bitcoin, siden alle transaksjoner ikke er private og avslører myntene som brukes, beløpene og adressene som er involvert på kjeden, kan Bitcoin-lommebøker ganske enkelt se etter ubrukte transaksjonsutganger (UTXOs) eller brukte adresser for en gitt lommebok , skanner raskt blokkjeden for bare UTXO-er som eies av disse adressene for å finne ut hvilke mynter som tilhører lommeboken din og kan brukes.

I Monero bevarer imidlertid alle transaksjoner brukerens personvern ved å skjule avsender, mottaker og beløp involvert i hver transaksjon. Dette personvernet, selv om det er avgjørende for å beskytte brukerne av nettverket, introduserer også tregere lommeboksynkronisering. I Monero må lommeboken din sammenligne hver transaksjonsutgang (TXO) som finnes på nettverket med lommebokens private nøkler.

Denne sammenligningen involverer mye kompleks matematikk og kryptografi for å validere at en utdata virkelig er din, siden alle beløp, adresser og kjente brukte utdata (eller mynter) er skjult på kjeden i Monero.

## Hva er visningstagger?

Som en måte å redusere synkroniseringstiden for Monero-lommebøker, kom [en forsker ved navn UkoeHB med en ny tilnærming](https://github.com/monero-project/research-lab/issues/73) – legg til en 1-byte "tag" til hver transaksjon ved å bruke en delt hemmelighet som kun er kjent til avsender og mottaker av transaksjonen.

Denne delte hemmeligheten genereres av avsenderen ved å bruke adressen oppgitt til dem av mottakeren, og krever ikke noe aktivt samarbeid fra avsender og mottaker. Den første byten (eller tegnet) til denne delte hemmeligheten legges deretter til transaksjonens data når den publiseres til Monero-nettverket.

Når en av deltakerne i den transaksjonen ønsker å synkronisere lommeboken sin med Monero-blokkjeden etterpå, i stedet for å måtte utføre all den komplekse matematikken og kryptografien for hver TXO på nettverket, kan lommeboken nå bare se etter det 1-byte-feltet i hver transaksjon og bare deretter utføre den tidkrevende verifiseringen på transaksjoner som har den taggen – 1/256 TXO-er på nettverket, for å være presis!

Denne taggen avslører ingen informasjon om transaksjonen til eksterne seere, den legger bare til 1-byte (et ubetydelig beløp) til transaksjonsstørrelser, og lar oss likevel redusere synkroniseringstiden med 40 %+ ved å kutte ned på komplekse verifikasjoner nødvendig!

## Vis tagger: et forenklet eksempel

Se for deg at du har 4096 bokser i et rom, hvorav kun 5 bokser tilhører deg. Boksene er alle helt umulige å skille fra utsiden, og den eneste måten å finne ut om en boks er noe for deg er å åpne den og løse et tidkrevende matteproblem skrevet ned på innsiden for å sikre at den er din.

Forestill deg nå at du bestemmer deg for å la personen som sender deg de 5 boksene generere en spesiell kode ved hjelp av adressen din, og deretter sette bare det første tegnet i den genererte koden på utsiden av hver boks som sendes til deg. Alle andre gjør det samme for boksene sine (for å sikre at alle boksene fortsatt ikke kan skilles fra hverandre), men nå kan du ganske enkelt se på den ene tegnkoden på utsiden av boksen, og bare åpne de boksene som har det tegnet på seg.[ X753X] 

Selv om andre bokser vil matche koden din, til og med noen som ikke eies av deg, er antallet bokser du trenger for å åpne og løse et matematikkproblem nå bare 16 (1/256 bokser!) i stedet for alle 4096. 

Nå åpner du de 16 boksene, løser matematikkoppgavene og beholder de 5 boksene som faktisk tilhører deg fra den gruppen!

## Når vil visningstagger være tilgjengelige i Monero?

View-tagger er en av funksjonene som for øyeblikket er planlagt inkludert i [den kommende nettverksoppgraderingen](https://github.com/monero-project/meta/issues/630), og bør utgis en gang denne våren. Fellesskapet [hevet 23.3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (i skrivende stund) for å stimulere utviklingen og implementeringen av visningstagger, og som et resultat har det store flertallet av arbeidet med å inkludere visningstagger i Monero-kodebasen allerede vært fullført av j-berman i samarbeid med anmeldere og forskere.

Når visningstagger er håndhevet av nettverket, vil alle transaksjoner som sendes etter nettverksoppgraderingen dra nytte av den drastisk forbedrede lommeboksynkroniseringstiden. Du trenger ikke å gjøre noe spesielt for å begynne å bruke visningstagger, favorittlommeboken din for Monero vil ganske enkelt begynne å bruke dem automatisk etter nettverksoppgraderingen!

## Hvordan kan jeg lære mer?

Hvis dette har vakt nysgjerrigheten din rundt visningstagger, ta en titt nedenfor for noen ekstra linker som går i dybden på emnet:

  * [Reduser skannetidene med 1-byte-per-utgang «view tag»](https://github.com/monero-project/research-lab/issues/73)
  * [Legg til visningstagger til utganger for å redusere skannetiden for lommeboken](https://github.com/monero-project/monero/pull/8061)

Videre lesning