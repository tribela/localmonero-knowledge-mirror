---
title: "Hur Monero-underadresser förhindrar identitetslänkning"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero har alltid hittat innovativa sätt att lösa svåra integritetsproblem. Ofta leder dessa innovationer till andra innovationer, och ibland kan dessa resulterande tekniker till och med användas för användningsområden som inte tidigare övervägts. Ingenstans exemplifieras detta mer än i fallet med Moneros subadressteknik.

Tänk på ett hypotetiskt integritetsproblem, där användning av en adress på flera plattformar från till synes orelaterade personer kan leda till sammankoppling och avanonymisering av nämnda personer. Enkelt uttryckt, om du var en person som heter Billy Joe Bob och sålde äpplen för Bitcoin, skulle du kunna publicera din Bitcoin-adress på en offentlig plats så att kunderna kan betala dig. Låt oss säga att adressen börjar med den alfanumeriska strängen 7XybV3... Men om vi bortser från den uppenbara integritetsrisken med att vem som helst kan kontrollera ditt Bitcoin-saldo och se hur mycket du har sålt, finns det en annan, inte så ofta omtalad integritetsrisk. Låt oss säga att du också var en underjordisk hackare som gick under namnet l33tz0r. Du gör visselblåsningsarbete och berättar för en intet ont anande befolkning om regeringskorruption, och det är absolut nödvändigt att du håller din identitet hemlig. Du accepterar Bitcoin-donationer för ditt arbete och publicerar adressen på ett offentligt forum. Det är samma adress som du accepterar pengar från dina Apple-kunder. Den 7XybV3... en.

En enkel, men förödande deanonymiseringsattack skulle vara att använda en internetsökmotor för att söka efter din Bitcoin-adress. Om du anger adressen 7XybV3... i sökmotorn får du upp två olika resultat. The apple business och l33tz0r. Detta är tillräckligt för att länka de två identiteterna och avanonymisera l33tz0r, med potentiellt skrämmande konsekvenser från de krafter som är.

Det är viktigt att notera att denna attack OCKSÅ är möjlig med Monero. Även om Monero döljer de flesta on-chain data, använder denna attack inte någon. Den använder bara adressen, som måste delas för att ta emot betalning. Offentligt när det gäller anonyma donationer. Detta är ett potentiellt sätt på vilket Monero-användare oavsiktligt kan skada sin integritet, och är också ett exempel på hur, även om Monero är i toppklass när det gäller integritetsbevarande, det inte är skottsäkert.

Det vanliga sättet att komma runt detta problem var att äga flera plånböcker. Med olika adresser för varje identitet (eller användarfall) kan de inte kopplas samman. Men denna sekretess gäller bara om användaren aldrig blandar ihop dem. Att av misstag publicera fel adress skulle ha samma kopplingseffekter. Dessutom måste fröet till varje adress hållas säkert, vilket ökar det infosec-arbete som krävs för varje ny plånbok som skapas.

Moneros lösning var underadresser. Möjligheten att skapa ett helt enormt antal adresser under huvudadressen och använda den som ett slags frö. Varje genererad underadress kan acceptera Monero, och allt går till samma plånbok. Med hjälp av denna metod är antalet identiteter som kan drivas under en adress enormt samtidigt som infosec-arbetet hålls till ett minimum. Dessa adresser är inte heller matematiskt länkbara, så om inte användaren skriker ut sin anslutning till världen, kommer en utomstående observatör att ha stora svårigheter att länka dem.

Men subadresserna har också fått ett annat intressant användningsområde: som ersättningsalternativ för de allmänt förhatliga betalnings-ID:na.

Betalnings-ID var ett sätt för handlare att identifiera vilken kund som skickat vilken betalning. Eftersom Monero-informationen är dold i kedjan kan mottagaren av en transaktion inte se vilken adress som skickade den. Det innebär att om det finns varor med liknande pris och flera beställningar kan det bli omöjligt att identifiera vem som skickade vad. Betalnings-ID är en unik, slumpmässig sträng som genereras av handlaren och ges till kunden. Kunden lägger till detta som ett separat fält när transaktionen skickas. Den slumpmässiga strängen placeras i blockkedjan som en del av transaktionen, och på så sätt kan handlaren identifiera och sortera inkommande transaktioner.

Denna metod var bristfällig på flera sätt. För det första minskar den enhetligheten i data från kedjan. Ytterligare, unika metadata kan göra att vissa transaktioner sticker ut från mängden, vilket möjliggör heuristisk analys. Detta gäller särskilt när dessa metadata inte är obligatoriska för alla. Att göra detta obligatoriskt för alla skulle dock lägga till onödigt utrymme i blockkedjan och var inte aktuellt. Om ett betalnings-ID någonsin återanvändes av någon anledning skulle det dessutom vara trivialt att länka två transaktioner som sammankopplade. Detta inträffade vanligtvis med insättningar på börsen, och vem som helst kunde enkelt länka transaktioner som både en insättning på en börs och från en viss individ.

För det andra, ur ett UX-perspektiv, skapar betalnings-ID ett andra steg som kryptovalutaanvändare som kommer från andra mynt inte är vana vid, och om de glöms bort orsakar det en enorm huvudvärk för handlaren som måste identifiera dessa transaktioner på annat sätt. Detta gjordes vanligtvis genom att tala direkt med varje kund som glömt att ange betalnings-ID och bekräfta annan identifierande information som bara de kunde känna till, till exempel en kombination av belopp, avsändningsdatum och transaktions-ID.

Detta extra steg missades av många, och det gick så långt att vissa växlar började ta betalt av kunderna om deras pengar behövde hämtas manuellt på grund av att de glömt ett betalnings-ID. Andra bet ihop tänderna och tog de extra supportkostnaderna, men ingen var glad över det.

Det fanns en lösning på detta, integrerade adresser, som slog samman adressen och betalnings-ID:t till en sträng, så att det inte kunde glömmas bort, men införandet var ganska svagt, trots de fördelar som handlarna skulle ha fått av att inkludera det.

I en intressant händelseutveckling kom underadresser in för att rädda dagen. Möjligheten att generera stora mängder underadresser per huvudadress och identifiera vilka transaktioner som kom in i vilka underadresser gjorde att handlarna kunde göra sig av med betalnings-ID på ett elegant sätt, samtidigt som de införde nästa generation av Monero-teknik. Sedan dess har de flesta börser och verktyg för handlare gått över till underadresser som det primära sättet att identifiera transaktioner.

Det som började som en lösning på ett integritetsproblem förvandlades till något mycket mer, som löste ett stort UX-problem för både handlare och kunder. Innovation föder mer innovation, vilket ofta kan leda till oväntade vinster för alla. Monero har sett detta gång på gång och lägger stor kraft på att förnya vad som är möjligt på blockkedjan. Vem vet vilka andra saker vi kan låsa upp tillsammans? 

Vidare läsning

  * [Hur Monero unikt möjliggör cirkulära ekonomier](/knowledge/monero-circular-economies/)

  * [Moneros ringsignaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Varför (och hur!) du ska hålla i dina egna nycklar](/knowledge/hold-your-keys/)

  * [Bidrar tillbaka till Monero](/knowledge/contributing-to-monero/)

  * [Hur fjärrnoder påverkar Moneros integritet](/knowledge/remote-nodes-privacy/)

  * [Hur Monero använder hard-forks för att uppgradera nätverket](/knowledge/network-upgrades/)

  * [Visa taggar: Hur en byte kommer att minska Monero plånbokssynkroniseringstider med 40% +](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool och dess roll i decentraliseringen av Monero Mining](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Vad det kommer att göra för Monero](/knowledge/seraphis-for-monero/)

  * [Är konvertering av Bitcoin till Monero lika privat som att köpa Monero direkt?](/knowledge/most-private-way-to-buy-monero/)

  * [Varför Monero använder en tillitslös installation till skillnad från Zcash](/knowledge/monero-trustless-setup/)

  * [Varför Monero är en bättre värdebevarare än Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Hur Monero kan övervinna Bitcoins nätverkseffekter](/knowledge/network-effect/)

  * [Varför Monero har den mest kritiskt tänkande gemenskapen](/knowledge/critical-thinking/)

  * [Bedrägerier att se upp för när du använder Monero](/knowledge/monero-scams/)

  * [Hur atombyten kommer att fungera i Monero](/knowledge/monero-atomic-swaps/)

  * [Vad varje Monero-användare behöver veta när det gäller nätverkande](/knowledge/monero-networking/)

  * [Hur RingCT döljer Monero-transaktionsbelopp](/knowledge/monero-ringct/)

  * [Hur Monero Stealth-adresser skyddar din identitet](/knowledge/monero-stealth-addresses/)

  * [Monero Utgångar Förklaras](/knowledge/monero-outputs/)

  * [Monero bästa praxis för nybörjare](/knowledge/monero-best-practices/)

  * [Hur ringsignaturer obskyr Moneros utgångar](/knowledge/ring-signatures/)

  * [Hur Monero löste problemet med blockstorlek som plågar Bitcoin](/knowledge/dynamic-block-size/)

  * [Hur CLSAG kommer att förbättra Moneros effektivitet](/knowledge/what-is-clsag/)

  * [Varför Monero har en svans emission](/knowledge/monero-tail-emission/)

  * [En kort historia om Monero](/knowledge/monero-history/)

  * [Wired Magazine har fel om Monero, här är varför](/knowledge/wired-article-debunked/)

  * [Topp 15 Monero myter och bekymmer debunked](/knowledge/monero-myths-debunked/)

  * [Hur Dandelion++ håller Moneros transaktionsursprung privat](/knowledge/monero-dandelion/)

  * [Varför Monero är öppen källkod och decentraliserad](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Vad gör RandomX så speciellt](/knowledge/monero-mining-randomx/)

  * [Varför Monero är bättre än Dash, Zcash, Zcoin (även med Lelantus), Grin och Bitcoin Mixers som Wasabi (Uppdaterad maj 2020)](/knowledge/why-monero-is-better/)