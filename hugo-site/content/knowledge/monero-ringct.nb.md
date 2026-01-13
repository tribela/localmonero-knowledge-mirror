---
title: "Hvordan RingCT skjuler Monero-transaksjonsbeløp"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Moneros personvern er ikke avhengig av én enkelt mekanisme som, hvis den brytes, vil avsløre hele transaksjonene, men snarere tre forskjellige teknologier som jobber sammen for å gi helhetlig personvern samtidig som de kompenserer for svakhetene til de andre delene. Denne tredelte tilnærmingen består av [ringsignaturer](/knowledge/ring-signatures), RingCT og [stealth-adresser](/knowledge/monero-stealth-addresses). Disse tre teknologiene skjuler henholdsvis den virkelige utgangen (sender), mengden og mottakeren. I dag skal vi snakke om RingCT.

RingCT er uten tvil den mest tekniske av de tre, og kan være vanskelig å forstå, så vi skal ikke dekke hvordan det fungerer nøyaktig, men heller vise hvordan det er mulig å ikke vite et beløp og likevel bekrefte ting om det . Og ikke bekymre deg, vi bruker mange eksempler som alltid.

La oss først undersøke hvorfor det er viktig å verifisere noe om beløpene. Hvorfor kan vi ikke bare holde dem helt hemmelige? Svaret er at det finnes smarte måter folk kan skape penger fra løse luften hvis de får muligheten. Hvordan kan noe slikt fungere? La oss se på et eksempel.

Hvis du vil kjøpe en vare fra vennen din, og han vil ha ti dollar for den, starter du med ti dollar, og han starter med null. Etter at du har gitt ham ti dollar, har han ti dollar og du har null. Du begynte med ti, og nå har han ti. Ingen penger ble opprettet eller ødelagt i denne transaksjonen.

Med kryptovalutaer kan en smart person gi ti dollar for varen, og i stedet for å motta null dollar i bytte, kan de få to dollar tilbake. I stedet for at 0 og 10 fører til 10 og 0 (eller 10=10), er det nå 0 og 10 fører til 10 og 2 (eller 10=12). To Monero ble nettopp skapt ut av løse luften. Du kan forestille deg at hvis individet skulle gjøre dette mot seg selv flere ganger, ville de kunne samle en gigantisk formue på kort tid.

Med Bitcoin og andre ville dette være lett å se. Du ser på inngangene som går inn i en transaksjon og utgangene som kommer ut og sørger for at det som sendes er likt det som mottas. Hvis disse beløpene var kryptert og ikke synlige, har en bruker ingen mulighet til å bekrefte at det som sendes og det som mottas er det samme.

I et forsøk på å øke Bitcoin-personvernet, opprettet Gregory Maxwell Confidential Transactions (CT), en ny teknologi som ville tillate krypterte beløp, samtidig som det beviste at ingenting ble opprettet eller ødelagt i prosessen. Som med de fleste personvernteknologier, kom den ikke inn i Bitcoin, men Monero var opptatt av å ta den i bruk. Det var bare ett problem. Den allerede implementerte teknologien for ringsignaturer var uforenlig med den foreslåtte ideen. Så en av MRL-forskerne på den tiden, Shen Noether, modifiserte CT til RingCT, en versjon av CT som var kompatibel med ringsignaturer.

Nok en gang er måten dette fungerer på ganske teknisk, og det vil være vanskelig å forklare i en innledende artikkel. For kryptografentusiasten som rett og slett må vite, er det mange dybdeartikler skrevet på internett om CTs indre virkemåte. For resten av oss vil denne artikkelen vise hvordan det kan være mulig å skjule beløpene, men likevel bevise at ingenting ble opprettet eller ødelagt.

La oss si at Alice ville sende penger til Bob. Alice vil sende 10 XMR til Bob, som vil motta 10 XMR. 10=10 så ingenting er galt her. Men Alice vil ikke at noen skal vite hvor mye hun sender. Så hun og Bob skaper en felles hemmelighet. I utgangspunktet et tall som bare de to kjenner. La oss si at tallet er 22. Nå multipliserer Alice 10 (det hun egentlig sender) med 22 for å få 220. Dette er tallet hun deler med nettverket.

Gruvearbeiderne selv vet ikke det hemmelige nummeret. Hvis de gjorde det, kunne de dele tallet de vises med det hemmelige tallet og få tilsendt det virkelige beløpet. Men siden de ikke gjør det, kan de ikke. De ser imidlertid at Bob vil motta 220. 220 sendt. 220 mottatt. 220 = 220. På denne måten kan nettverket verifisere at ingen Monero ble opprettet eller ødelagt, alt uten å vite det virkelige beløpet som Alice sendte Bob.

Siden Bob kjenner det delte hemmelige nummeret, når han mottar pengene, deler han bare på 22 for å få det virkelige beløpet som Alice sendte, 10. Alice og Bob vet begge hvor mye som ble sendt og hvor mye som ble mottatt. alle andre får et falskt tall.

Nok en gang, dette er ikke den faktiske måten CT fungerer på, men det gir en idé om hvordan noe slikt kan være mulig. Den virkelige måten involverer ting som Pedersen-forpliktelser, to sendte beløp (ett kryptert beløp til mottakeren og ett forpliktelsesbeløp til nettverket), og ... ja, det er allerede lett å se hvordan man kan gå seg vill i alt dette.

En ting å merke seg er imidlertid at mens RingCT skjuler beløpet som utføres mellom to parter i en transaksjon, skjuler det ikke to andre sett med tall.

Den første er myntbasetransaksjonene. Hvis dette begrepet ikke er kjent for deg, betyr det i utgangspunktet belønningen som gruvearbeidere får for å finne neste blokk. Dette nummeret er ikke skjult. Hvem som helst kan se hvor mye protokollen har tildelt en gruvearbeider for sin tjeneste. På denne måten kan den gjeldende mengden Monero som eksisterer bli kjent ved å legge sammen alle myntbasetransaksjonene. Summen deres vil tilsvare gjeldende Monero i omløp.

Det andre tallet som ikke skjules, er gebyret som betales til gruvearbeiderne når en bruker sender en transaksjon. Gebyrene må være tydelige slik at gruvearbeidere kan vite hvem de skal prioritere. Dette er en måte som brukere kan skade privatlivet deres, men som om noen bruker en unik gruveavgift hver gang de sender en transaksjon (som 0.12345), så kan transaksjonene deres kobles sammen.

Bortsett fra disse tilfellene har RingCT skjult Monero-beløp siden 2017, og vårt kollektive personvern er desto sterkere for det.

Videre lesning