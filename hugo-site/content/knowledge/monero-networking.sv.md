---
title: "Vad varje Monero-användare behöver veta när det gäller nätverkande"
slug: "monero-networking"
date: "2020-11-11"
image: "/images/networking.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Om vi börjar på den triviala sidan av saken, om en användare inte har tillgång till internet, kan de inte ladda ner nya block, sprida transaktioner på uppdrag av andra eller skicka egna transaktioner. En intressant sak att notera är att en användare med en fullständig nod, utan internetåtkomst, kan konstruera en transaktion offline som kan skickas senare. Detta beror på att en ringsignatur bara behöver utdata från blockkedjan för att gömma sig med. En kort påminnelse om [hur ringsignaturer fungerar, den döljer den verkliga utdata som en användare skickar bland en samling av oberoende utdata som valts från det förflutna. Om användaren har tillgång till dessa utdata i form av en fullständigt nedladdad blockkedja (fullständig nod) kan de skapa ringsignaturen från de tidigare utdata, och när internetanslutningen återupptas, sprida transaktionen till nätverket. En användare som använder en fjärrnod kan inte göra detta, eftersom när de konstruerar sin ringsignatur kontaktar de den fullständiga fjärrnoden för utdata som ska inkluderas i ringsignaturen. Inget internet innebär att de inte kan nå den här noden, så de har inga möjligheter att skapa offline transaktioner. Innan vi går in på några av integritetsaspekterna ska vi ge en kort introduktion till hur internet fungerar som helhet. Hela internet är inget annat än datorer som ansluter till andra datorer. Det är allt. Bloggen du gillar att läsa? Bara några filer som finns på någon annans dator. Den här webbplatsen som du läser den här artikeln på (LocalMonero)? Filer och kod som finns på en dator någonstans. Även stora galna webbplatser fungerar på detta sätt. Ta YouTube till exempel. Bara videofiler som finns på Googles gigantiska datorsystem, och du ansluter till dem för att ladda ner videon till din egen dator så att du kan titta på den. Dessa datorer kan skilja varandra åt eftersom varje dator som är ansluten till Internet har ett unikt identifikationsnummer som kallas IP-adress. Dessa är vanligtvis fyra uppsättningar siffror separerade med punkter, till exempel: 172.66.35.7. Det är viktigt att ha detta i åtanke när vi tittar på hur Moneros information flyttas runt på internet. Monero är ett peer-to-peer-nätverk (P2P), vilket innebär att datorer ansluter direkt till varandra i stället för att använda en mellanhand. Så när en användares fulla nod laddar ner ett nyupptäckt block laddar de inte ner det från en central server, utan från sina kamrater. Nackdelen med detta är att eftersom användarna ansluter direkt till varandra känner de till varandras IP adresser. Nå? Vad är det som är så viktigt? Det är bara en siffra, eller hur? Inte riktigt. IP-adresser innehåller i sig information om användaren, t.ex. ursprungsland och nätverksleverantör, men ännu värre är att internetleverantörer känner till IP-adressen för varje person som använder deras tjänster. Det innebär att dessa internetleverantörer och de som de samarbetar med kan övervaka en användares internettrafik och med hjälp av en smart taktik upptäcka att de använder Monero. Innan du blir rädd, notera formuleringen där. Allt dessa snokare kan göra är att se att en person ansluter till andra noder i Moneronätverket. På grund av Moneros integritetsteknik läcker inget annat ut om individen. Inte om de kör en nod eller inte, eller om/när de skickar transaktioner, och om en transaktion skickas är ingen av dess information känd. Allt dessa internetleverantörer kan se är att en av deras användare ansluter till Moneros nätverk. Nu, För vissa människor, på vissa platser, kan enbart denna information vara tillräcklig för att skada deras rykte eller frihet. Eller så kanske tanken på att någon ska inkräkta på din integritet och vad du gör på internet, oavsett anledning, inte är acceptabel för dig. Dessa personer uppmanas att endast ansluta till Monero-nätverket med VPN, Tor eller I2P, som alla är tjänster som döljer en användares IP-adress för andra samt döljer vad en användare gör för sin internetleverantör. Skillnaderna mellan dessa tjänster ligger utanför ramen för denna artikel, men det finns gott om högkvalitativa artiklar skrivna om ämnet, så berörda användare uppmuntras att studera upp! För resten av oss kanske vi tycker att det inte är så farligt att andra vet att vi är anslutna till Monero-nätverket. När allt kommer omkring är det faktiska innehållet i våra transaktioner, eller om vi skickar några alls, dolt för allmänheten, så vad är skadan? Även om detta kan vara sant, uppmuntras användare att överväga det faktum att den största dragningen av kryptovalutor är att vara sin egen bank. När du håller din privata nyckel, och om något händer med den, kan ingen hjälpa dig att återställa dina förlorade medel. Att vara sin egen bank innebär att man inte bara måste tänka på sin digitala säkerhet, utan även på sin fysiska säkerhet. Det kan mycket väl vara så att kunskapen om att en individ ansluter till Monero-nätverket kan ge oönskad uppmärksamhet, inte nödvändigtvis från storskaliga aktörer som nationalstater, utan mindre med själviska intressen, som hackare som vill tjäna en enkel peng. Det finns verkligen otaliga berättelser över hela kryptoutrymmet om sådana scenarier som faktiskt äger rum. Den här artikeln är inte avsedd att skrämmas, utan snarare att uppmuntra användare att undersöka vilka metoder för skydd mot webbsurfning som är rätt för dem. Den goda nyheten är att dessa färdigheter också kommer att överföras till allmän internetanvändning, inte bara Monero-användning, och som sådan, i vår alltmer internetanslutna värld, kan en kunnig användare inte gå fel och samla rätt kunskap och färdigheter för att hålla sig säker och verkligen vara sin egen bank.](/knowledge/ring-signatures)

, den döljer den verkliga utdata som en användare skickar bland en samling av oberoende utdata som valts från det förflutna. Om användaren har tillgång till dessa utdata i form av en fullständigt nedladdad blockkedja (fullständig nod) kan de skapa ringsignaturen från de tidigare utdata, och när internetanslutningen återupptas, sprida transaktionen till nätverket.

En användare som använder en fjärrnod kan inte göra detta, eftersom när de konstruerar sin ringsignatur kontaktar de den fullständiga fjärrnoden för utdata som ska inkluderas i ringsignaturen. Inget internet innebär att de inte kan nå den här noden, så de har inga möjligheter att skapa offline transaktioner.

Innan vi går in på några av integritetsaspekterna ska vi ge en kort introduktion till hur internet fungerar som helhet. Hela internet är inget annat än datorer som ansluter till andra datorer. Det är allt. Bloggen du gillar att läsa? Bara några filer som finns på någon annans dator. Den här webbplatsen som du läser den här artikeln på (LocalMonero)? Filer och kod som finns på en dator någonstans. Även stora galna webbplatser fungerar på detta sätt. Ta YouTube till exempel. Bara videofiler som finns på Googles gigantiska datorsystem, och du ansluter till dem för att ladda ner videon till din egen dator så att du kan titta på den.

Dessa datorer kan skilja varandra åt eftersom varje dator som är ansluten till Internet har ett unikt identifikationsnummer som kallas IP-adress. Dessa är vanligtvis fyra uppsättningar siffror separerade med punkter, till exempel: 172.66.35.7. Det är viktigt att ha detta i åtanke när vi tittar på hur Moneros information flyttas runt på internet. Monero är ett peer-to-peer-nätverk (P2P), vilket innebär att datorer ansluter direkt till varandra i stället för att använda en mellanhand. Så när en användares fulla nod laddar ner ett nyupptäckt block laddar de inte ner det från en central server, utan från sina kamrater. Nackdelen med detta är att eftersom användarna ansluter direkt till varandra känner de till varandras IP adresser.

Nå? Vad är det som är så viktigt? Det är bara en siffra, eller hur? Inte riktigt. IP-adresser innehåller i sig information om användaren, t.ex. ursprungsland och nätverksleverantör, men ännu värre är att internetleverantörer känner till IP-adressen för varje person som använder deras tjänster. Det innebär att dessa internetleverantörer och de som de samarbetar med kan övervaka en användares internettrafik och med hjälp av en smart taktik upptäcka att de använder Monero. Innan du blir rädd, notera formuleringen där. Allt dessa snokare kan göra är att se att en person ansluter till andra noder i Moneronätverket. På grund av Moneros integritetsteknik läcker inget annat ut om individen. Inte om de kör en nod eller inte, eller om/när de skickar transaktioner, och om en transaktion skickas är ingen av dess information känd. Allt dessa internetleverantörer kan se är att en av deras användare ansluter till Moneros nätverk.

Nu, För vissa människor, på vissa platser, kan enbart denna information vara tillräcklig för att skada deras rykte eller frihet. Eller så kanske tanken på att någon ska inkräkta på din integritet och vad du gör på internet, oavsett anledning, inte är acceptabel för dig. Dessa personer uppmanas att endast ansluta till Monero-nätverket med VPN, Tor eller I2P, som alla är tjänster som döljer en användares IP-adress för andra samt döljer vad en användare gör för sin internetleverantör. Skillnaderna mellan dessa tjänster ligger utanför ramen för denna artikel, men det finns gott om högkvalitativa artiklar skrivna om ämnet, så berörda användare uppmuntras att studera upp!

För resten av oss kanske vi tycker att det inte är så farligt att andra vet att vi är anslutna till Monero-nätverket. När allt kommer omkring är det faktiska innehållet i våra transaktioner, eller om vi skickar några alls, dolt för allmänheten, så vad är skadan? Även om detta kan vara sant, uppmuntras användare att överväga det faktum att den största dragningen av kryptovalutor är att vara sin egen bank. När du håller din privata nyckel, och om något händer med den, kan ingen hjälpa dig att återställa dina förlorade medel.

Att vara sin egen bank innebär att man inte bara måste tänka på sin digitala säkerhet, utan även på sin fysiska säkerhet. Det kan mycket väl vara så att kunskapen om att en individ ansluter till Monero-nätverket kan ge oönskad uppmärksamhet, inte nödvändigtvis från storskaliga aktörer som nationalstater, utan mindre med själviska intressen, som hackare som vill tjäna en enkel peng. Det finns verkligen otaliga berättelser över hela kryptoutrymmet om sådana scenarier som faktiskt äger rum.

Den här artikeln är inte avsedd att skrämmas, utan snarare att uppmuntra användare att undersöka vilka metoder för skydd mot webbsurfning som är rätt för dem. Den goda nyheten är att dessa färdigheter också kommer att överföras till allmän internetanvändning, inte bara Monero-användning, och som sådan, i vår alltmer internetanslutna värld, kan en kunnig användare inte gå fel och samla rätt kunskap och färdigheter för att hålla sig säker och verkligen vara sin egen bank.

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

  * [Hur RingCT döljer Monero-transaktionsbelopp](/knowledge/monero-ringct/)

  * [Hur Monero Stealth-adresser skyddar din identitet](/knowledge/monero-stealth-addresses/)

  * [Hur Monero-underadresser förhindrar identitetslänkning](/knowledge/monero-subaddresses/)

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