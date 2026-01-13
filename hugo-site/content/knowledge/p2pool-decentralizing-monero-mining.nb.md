---
title: "P2Pool og dens rolle i desentralisering av Monero-gruvedrift"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Et av kjernemålene i Monero-prosjektet er å muliggjøre et rettferdig, desentralisert og sikkert nettverk gjennom nye og innovative tilnærminger til proof-of-work (PoW) mining, den viktigste måten kryptovalutanettverk er sikret i dag.[ X230X] 

Selv om en unik gruvealgoritme [som RandomX](/knowledge/monero-mining-randomx) er ekstremt viktig for dette målet, da den bidrar til å sikre at alle med en datamaskin kan bidra med en god del til sikkerheten til nettverket, løser ikke RandomX problemene som kan oppstå på grunn av bassengutvinning. Pool mining er den desidert vanligste måten å utvinne kryptovalutaer i dag, inkludert Monero, men heldigvis endrer fremveksten av p2pool mining det raskt.

## Hva er bassenggruvedrift?

Pool mining er en måte for gruvearbeidere å dele oppgaven med å prøve å løse en blokk på nettverket og deretter dele belønningene jevnt for alle blokkene som bassenget finner. Selv om dette hjelper enormt med å jevne ut frekvensen som gruvearbeidere blir betalt med kontra mining av Monero alene, er det ikke uten alvorlige sentraliseringsproblemer.

Når hver gruvearbeider bidrar med arbeid til bassenget, gir de opp kontrollen over alt arbeid de gjør og blokkeringer de finner til selve bassenget, og stoler på at bassenget ærlig og rettferdig vil dele belønningene mellom alle gruvearbeidere basert på mengden av arbeid hver har gjort. Hvis alt går bra, samler bassengoperatøren inn arbeidet fra alle gruvearbeidere, sender det til nettverket og deler belønningene likt.

## Hva er problemet med bassengutvinning?

Dessverre er dette helt avhengig av tillit og lar bassengoperatøren gjøre grusomme ting med arbeidet som utføres av gruvearbeidere. Bassengoperatøren kan bruke arbeidet som gjøres til å angripe nettverket, forsøke å dobbeltbruke midler (hvis bassenget er stort nok), eller ganske enkelt bruke arbeidet som gjøres av gruvearbeiderne til å betale seg selv og aldri belønne gruvearbeidere ordentlig for arbeidet deres. .

Den største risikoen for nettverket er at en pool (eller flere bassenger som jobber sammen) har mer enn 51 % av nettverkets hashrate under kontroll, da de kan bruke dette til å jukse og bruke midler to ganger (dobbeltforbruk) angrep) eller forsøk å endre reglene for nettverket.

## Hva er p2pool?

p2pool er et konsept som opprinnelig ble opprettet for å utvinne Bitcoin tilbake i 2011, men som aldri så bred adopsjon og forblir praktisk talt ubrukt på Bitcoin. Heldigvis brukte en av nøkkelutviklerne bak RandomX, SChernykh, ferien sin på å finne løsninger på noen av problemene med Bitcoin-implementeringen av p2pool og skrive om all programvare fra bunnen av.

p2pool i Monero gir mulighet for en helt tillitsløs måte for gruvearbeidere å jobbe sammen for å løse blokker og sikre Monero-nettverket ved å bruke spesiell nodeprogramvare for p2pool for å dele arbeidet.

Dette gjøres ved å bruke en ny blokkjede (en "sidekjede") som holder oversikt over arbeidet hver gruvearbeider utfører, deres lommebokadresse og hvor mye Monero de har tjent, og deretter betaler belønningen ut i en trust -mindre og desentralisert måte. Siden denne sidekjeden har langt færre gruvearbeidere, er det mye enklere å finne og sende inn blokker på den enn på Monero-hovednettverket, noe som gjør det lettere for gruvearbeidere å få konsekvente utbetalinger i forhold til å gruve Monero alene.

## Hvordan løser p2pool problemene med bassenggruvedrift?

I p2pool er det ingen sentralisert pool, sentralisert pooloperatør eller enkeltperson som holder på midler og distribuerer utbetalinger. Alt arbeidet som gjøres kollektivt av de som gruver via p2pool, blir sjekket av p2pool-blokkjeden og andre nodeoperatører for å sikre at det er legitimt, og alle gruvearbeidere blir betalt ut i henhold til arbeidet de har gjort umiddelbart når en blokk blir funnet direkte fra belønningene i den funnet blokken.

Når gruvearbeidere velger å bruke p2pool i stedet for et sentralisert basseng, fjerner de all makt og tillit fra bassengoperatørene og sikrer at arbeidet deres bidrar til nettverkets beste og til deres egne belønninger, reduserer risikoen for nettverksangrep, misbruk av arbeidet deres, eller tyveri av belønninger de skylder.

Ikke bare hjelper dette dem å beskytte sine egne interesser, det reduserer risikoen for at sentraliserte bassenger kan utgjøre for Monero-nettverket som helhet. p2pool-bruk hjelper også enormt med å redusere risikoen som nasjonalstater eller regulatorer kan utgjøre for helsen til nettverket, ettersom det ikke er noen sentraliserte bassengoperatører å presse på, ingen geografisk konsentrasjon av bassenger å støtte seg på, eller noe annet lett presspunkt. for dem å bruke mot Monero.

## Hva er ulempene?

Heldigvis har p2pool i Monero blitt godt designet og godt bygget, og fungerer ekstremt bra! Den største ulempen med p2pool-gruvedrift er imidlertid at hver gruvearbeider som ønsker å bruke p2pool må kjøre sin egen Monero-node, noe som fører til at prosessen med å komme i gang blir litt mer involvert. Imidlertid brukes denne noden til å beregne all informasjon som er nødvendig for å bygge og sjekke blokker, og sikrer at gruvearbeideren har full kontroll over arbeidet som utføres. Noden kan også fungere som en ekstern node for gruvearbeiderens egen lommebok, bidrar til nettverket og mye mer.

Den andre viktige forskjellen fra sentralisert gruvedrift er at små gruvearbeidere som bruker p2pool vil ha litt mer "varians", eller tid mellom utbetalinger, enn en stor sentralisert pool – men det's _ekstremt_ viktig å merke seg at dette ikke vil føre til å tjene mindre Monero over tid! p2pool vil være like lønnsomt for selv små gruvearbeidere over tid som sentraliserte bassenger. Noe av denne variansen blir også oppveid av at p2pool har 0 % avgifter, siden det ikke er noen sentralisert bassengoperatør som betaler for tjenestene deres!

## Hvordan kan jeg komme i gang?

Heldigvis, på grunn av den utmerkede utformingen av Monero's p2pool-implementering og de mange menneskene i samfunnet som har brukt tid på å hjelpe til med å forenkle prosessen med gruvedrift via p2pool, blir det enklere med tiden å komme i gang. Det er flere måter å komme i gang med mining med p2pool, men siden de tekniske detaljene er utenfor rammen av denne artikkelen, kan du gjerne hoppe inn i en lenke nedenfor avhengig av operativsystemet ditt:

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## Hvordan kan jeg lære mer?

Hvis dette har vakt nysgjerrigheten din rundt p2pool-gruvedrift, ta en titt nedenfor for noen flere linker og forklaringer om p2pool, hvordan det fungerer og hva det betyr for Monero:

  * [Den offisielle Github for p2pool](https://github.com/SChernykh/p2pool)
  * [De offisielle dokumentene om bruk av p2pool](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool er nå live](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, en slags "blokkutforsker" for p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-komponer](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh: Om hans utvikling av P2Pool en desentralisert XMR-gruvepool](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

Videre lesning