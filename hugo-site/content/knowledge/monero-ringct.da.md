---
title: "Hvordan RingCT Huder Monero Transaktion Beløb"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Moneros privatliv afhænger ikke af én enkelt mekanisme, der, hvis den brydes, ville afsløre alle transaktioner, men snarere tre forskellige teknologier, der arbejder sammen for at give holistisk privatliv, mens de kompenserer for svaghederne i de andre dele. Denne trestrengede tilgang består af [ringsignaturer](/knowledge/ring-signatures), RingCT og [stealth-adresser](/knowledge/monero-stealth-addresses). Disse tre teknologier skjuler henholdsvis det reelle output (afsender), mængde og modtager. I dag skal vi tale om RingCT.

RingCT er uden tvivl den mest tekniske af de tre, og kan være svær at forstå, så vi vil ikke dække, hvordan det fungerer præcist, men snarere vise, hvordan det er muligt ikke at vide et beløb og stadig bekræfte ting om det . Og bare rolig, vi vil bruge masser af eksempler som altid.

Lad os først undersøge, hvorfor det er vigtigt at verificere noget om beløbene. Hvorfor kan vi ikke bare holde dem helt hemmelige? Svaret er, at der er smarte måder, hvorpå folk kan skabe penge fra den blå luft, hvis de får muligheden. Hvordan kan sådan noget fungere? Lad os se på et eksempel.

Hvis du vil købe en vare fra din ven, og han vil have ti dollars for den, så starter du med ti dollars, og han starter med nul. Når du har givet ham de ti dollars, har han ti dollars, og du har nul. Du startede med ti, og nu har han ti. Ingen penge blev oprettet eller ødelagt i denne transaktion.

Med kryptovalutaer kan en klog person give ti dollars for varen, og i stedet for at modtage nul dollars i byttepenge, kan de modtage to dollars tilbage. I stedet for at 0 og 10 fører til 10 og 0 (eller 10=10), er det nu 0 og 10 fører til 10 og 2 (eller 10=12). To Monero blev bare skabt ud af den blå luft. Du kan forestille dig, at hvis individet skulle gøre dette mod sig selv flere gange, ville de være i stand til at samle en gigantisk formue på kort tid.

Med Bitcoin og andre ville dette være nemt at se. Du ser på input, der går ind i en transaktion og output, der kommer ud og sikrer dig, at det, der sendes, svarer til det, der modtages. Hvis disse beløb var krypteret og ikke synlige, har en bruger ingen mulighed for at bekræfte, at det, der sendes, og det, der modtages, er det samme.

I et forsøg på at øge privatlivets fred, skabte Gregory Maxwell Confidential Transactions (CT), en ny teknologi, der ville tillade krypterede beløb, samtidig med at beviste, at intet blev oprettet eller ødelagt i processen. Som med de fleste privatlivsteknologier blev det ikke til Bitcoin, men Monero var opsat på at adoptere det. Der var kun et problem. Den allerede implementerede teknologi med ringsignaturer var uforenelig med den foreslåede idé. Så en af MRL-forskerne på det tidspunkt, Shen Noether, modificerede CT til RingCT, en version af CT, der var kompatibel med ringsignaturer.

Igen er den måde, dette fungerer på, ret teknisk og ville være svær at forklare i en indledende artikel. For kryptografientusiasten, der simpelthen skal vide det, er der masser af dybdegående artikler skrevet på internettet om CT's indre funktioner. For resten af os vil denne artikel vise, hvordan det kan være muligt at skjule beløbene, men stadig bevise, at intet blev skabt eller ødelagt.

Lad os sige, at Alice ville sende Bob penge. Alice sender 10 XMR til Bob, som vil modtage 10 XMR. 10=10 så der er intet galt her. Men Alice ønsker ikke, at nogen skal vide, hvor meget hun sender. Så hun og Bob skaber en fælles hemmelighed. Dybest set et tal, som kun de to kender. Lad os sige, at tallet er 22. Nu gange Alice 10 (hvad hun virkelig sender) med 22 for at få 220. Dette er det tal, hun deler med netværket.

Minearbejderne kender ikke selv det hemmelige nummer. Hvis de gjorde det, kunne de dividere det tal, de får vist, med det hemmelige tal og få det rigtige beløb tilsendt. Men da de ikke gør det, kan de ikke. De ser dog, at Bob vil modtage 220. 220 sendt. 220 modtaget 200= 220. På denne måde kan netværket bekræfte, at ingen Monero blev oprettet eller ødelagt, alt sammen uden at kende det reelle beløb, som Alice sendte Bob.

Da Bob kender det delte hemmelige nummer, når han modtager pengene, dividerer han bare med 22 for at få det rigtige beløb, som Alice sendte, 10. Alice og Bob ved begge, hvor meget der blev sendt, og hvor meget der blev modtaget, alt imens alle andre får et falsk nummer.

Igen, dette er ikke den faktiske måde, hvorpå CT fungerer, men det giver en idé om, hvordan sådan noget kan være muligt. Den rigtige måde involverer ting som Pedersen-forpligtelser, to sendte beløb (et krypteret beløb til modtageren og et forpligtelsesbeløb til netværket), og ... ja, det er allerede let at se, hvordan man kunne fare vild i alt det.

En ting at bemærke er dog, at mens RingCT skjuler det beløb, der er gennemført mellem to parter i en transaktion, skjuler det ikke to andre sæt tal.

Den første er møntbase-transaktionerne. Hvis dette udtryk ikke er bekendt for dig, betyder det dybest set den belønning, minearbejdere får for at finde den næste blok. Dette nummer er ikke skjult. Enhver kan se, hvor meget protokollen har tildelt en minearbejder for deres tjeneste. På denne måde kan den nuværende mængde Monero, der eksisterer, kendes ved at lægge alle møntbase-transaktionerne sammen. Deres sum vil svare til den nuværende Monero i omløb.

Det andet tal, der ikke er skjult, er det gebyr, der betales til minearbejderne, når en bruger sender en transaktion. Gebyrerne skal være klare, så minearbejdere kan vide, hvem de skal prioritere. Dette er dog en måde, hvorpå brugere kan skade deres privatliv, som hvis nogen bruger et unikt minearbejdergebyr, hver gang de sender en transaktion (som 0.12345), så kan deres transaktioner sammenkædes.

Udover disse tilfælde har RingCT skjult Monero-beløb siden 2017, og vores kollektive privatliv er så meget desto stærkere for det.

Yderligere læsning