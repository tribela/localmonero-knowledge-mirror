---
title: "Hur ringsignaturer obskyr Moneros utgångar"
slug: "ring-signatures"
date: "2020-09-08"
image: "/images/rings.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero är vida känt över kryptorummet som kungen av integritetsmynt. Medan alla vet att Monero erbjuder bra integritet, är det inte lika många som förstår hur integriteten fungerar.

Många andra integritetsmynt publicerar infografik med jämförelsediagram, som listar namnen på varje mynts integritetsteknik, och i de flesta märker de Moneros teknik som RingCT, men detta är bara delvis sant. Monero har faktiskt en tredelad strategi för integritet. En teknik för att dölja mottagaren av en transaktion, en för att dölja det skickade beloppet och en för att dölja den använda utgången, dessa är stealth-adresser, RingCT respektive ringsignaturer.

Denna tredelade strategi innebär att om en av teknikerna bryts, behöver de andra inte nödvändigtvis dela samma öde. Ringsignaturer är den svagaste länken i integritetssystemet; ordet svag betyder här att den är mest mottaglig för heuristiska attacker. Låt oss ta oss lite tid att utforska dem, eller hur?

Som nämnts ovan är målet med ringsignaturer att dölja en output som används i en transaktion. Om terminologin "input/output" för kryptovalutor är förvirrande för dig, oroa dig inte. Det är faktiskt inte så komplicerat. När du hör "output" tänker du bara på en check. En av de saker, inte så vanliga längre, som människor använder för att betala med. Liksom en check kan den anges i vilket belopp som helst - $ 10, $ 32.50, etc - och utbyts mellan transakterande parter. För kryptovalutor tjänar utgångar dessa funktioner.

När någon betalar dig 10 Monero får du en 10 XMR-utgång. Denna output har ett värde (10), och är vad som tas från avsändarens plånbok, på samma sätt som när du betalar för en tjänst, en räkning lämnar din fysiska plånbok och ges till den person du köper från.

Sättet att dölja output är att konstruera en ring (därav namnet) av decoy-output. Men dessa lockbeten är inte "falska" utgångar. De är verkliga tidigare utdata från blockkedjan som inte har något att göra med den aktuella transaktionen, men för en utomstående observatör kan var och en av dessa utdata se lika sannolik ut som den verkliga. Storleken på uppsättningen av decoy-utgångar, plus den verkliga, kallas ringsize, och för närvarande är Moneros elva. Det finns alltså tio falska utgångar och en riktig.

Varför ökar vi inte bara detta antal till 100 eller till och med 1000? Ju fler desto bättre, eller hur? Tja, ur ett integritetsperspektiv, ja, men det finns andra saker att tänka på. Låt oss gå tillbaka till ett fysiskt exempel för att se vad jag menar. Om du vill gömma en av dina dollarsedlar bland tio attrapper, skulle du behöva bära runt på elva dollar i plånboken för varje dollar du vill spendera. En riktig dollar och tio falska. Detta blir redan ganska besvärligt om du vill spendera ens några få dollar. Föreställ dig nu att vi ökar beloppet till 1000. För varje dollar du vill spendera skulle du behöva bära runt på 1001 dollar. Du skulle behöva bära runt på en portfölj bara för att köpa en godisbit! Det är viktigt att notera att ringsignaturer inte fungerar riktigt på detta sätt, till exempel är lockbetena själva inte en del av signaturen, utan endast referenser till dem, men vi hoppas att denna analogi kan vara till viss hjälp för att föreställa sig de grundläggande begreppen.

Dockorna på blockkedjan fungerar på samma sätt. Varje tillagd decoy ökar tiden och verifieringskostnaden för transaktionen. Varje nod måste ladda ner hela ringsignaturen för varje transaktion, och varje ringsignatur innehåller den verkliga utdata, såväl som lockbete. Inte nog med det, den måste också verifiera matematiken att minst en av dessa utgångar är verklig, och den matematiska verifieringstiden ökar också med varje lockbete. Det betyder att vi måste hitta en bra medelväg, där ringstorleken är tillräckligt stor för att dölja den verkliga utgången, även mot många heuristiska attacker, men tillräckligt liten för att inte orsaka att blockkedjan ökar i en enorm takt. Det räcker inte att välja ett godtyckligt tal, eller att bara öka ringstorleken när vi gör signaturen mindre (som med CLSAG). Moneros community vill ha konkreta, matematiska bevis på vilken ringstorlek som ger de bästa avvägningarna. Ett för litet antal och integriteten kommer inte att vara tillräckligt stark mot heuristiska attacker. För stort, och vi kanske bara får marginella fördelar på integritetssidan, och onödigt lidande när det gäller skalning.

En sista sak att nämna. En del Monero-litteratur förenklar och säger att ringsignaturer döljer avsändaren, men detta är inte helt sant, och skillnaden är inte bara pedantisk. Skillnaden mellan avsändaren (en människa) och en output (en räkning) är stor när det gäller att bevara integriteten. Även om en output kan ha kopplingar till en avsändare, är en output i sig inte detsamma som en avsändare. Så även om en ringsignatur skulle brytas är den inte nödvändigtvis kopplad till en persons identitet, och både beloppet och mottagaren är fortfarande dolda, vilket minimerar skadan på integriteten för alla parter.

Det är inte att säga att en trasig ringsignatur är obetydlig. Alla metadata som läcker ut är dåliga och har potential att avslöja mer information än vi tror, särskilt när de används tillsammans med andra metadata. Därför gör vi vårt bästa för att säkerställa att den valda ringstorleken har akademisk stringens bakom beslutet, att läckage av andra metadata minimeras och att användarupplevelsen standardiseras till bästa möjliga åtgärder.

Men om sannolikheten för en trasig signatur fortfarande oroar dig, ja, då finns det några otroliga nyheter i horisonten. Nästa generation av sekretessprotokoll som vi arbetar med, till exempel Triptych, Arcturus och Lelantus, har riktigt fina funktioner. I dessa protokoll skalar storleken logaritmiskt, inte linjärt, när ringstorleken ökar. Det innebär att vi kan få plats med 100 lockbeten, men att det utrymme som används är närmare ringstorlek 10 i den gamla tekniken. Det är en stor skillnad och kommer att förbättra integriteten avsevärt.

I den katt- och råttalek som integritet är, innoverar Monero kontinuerligt för att hålla sig före kurvan och säkerställa den bästa praktiska integriteten för alla.

Vidare läsning

  * [Hur Monero unikt möjliggör cirkulära ekonomier](/knowledge/monero-circular-economies)/

  * [Moneros ringsignaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Varför (och hur!) du ska hålla i dina egna nycklar](/knowledge/hold-your-keys)/

  * [Bidrar tillbaka till Monero](/knowledge/contributing-to-monero)/

  * [Hur fjärrnoder påverkar Moneros integritet](/knowledge/remote-nodes-privacy)/

  * [Hur Monero använder hard-forks för att uppgradera nätverket](/knowledge/network-upgrades)/

  * [Visa taggar: Hur en byte kommer att minska Monero plånbokssynkroniseringstider med 40% +](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool och dess roll i decentraliseringen av Monero Mining](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Vad det kommer att göra för Monero](/knowledge/seraphis-for-monero)/

  * [Är konvertering av Bitcoin till Monero lika privat som att köpa Monero direkt?](/knowledge/most-private-way-to-buy-monero)/

  * [Varför Monero använder en tillitslös installation till skillnad från Zcash](/knowledge/monero-trustless-setup)/

  * [Varför Monero är en bättre värdebevarare än Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Hur Monero kan övervinna Bitcoins nätverkseffekter](/knowledge/network-effect)/

  * [Varför Monero har den mest kritiskt tänkande gemenskapen](/knowledge/critical-thinking)/

  * [Bedrägerier att se upp för när du använder Monero](/knowledge/monero-scams)/

  * [Hur atombyten kommer att fungera i Monero](/knowledge/monero-atomic-swaps)/

  * [Vad varje Monero-användare behöver veta när det gäller nätverkande](/knowledge/monero-networking)/

  * [Hur RingCT döljer Monero-transaktionsbelopp](/knowledge/monero-ringct)/

  * [Hur Monero Stealth-adresser skyddar din identitet](/knowledge/monero-stealth-addresses)/

  * [Hur Monero-underadresser förhindrar identitetslänkning](/knowledge/monero-subaddresses)/

  * [Monero Utgångar Förklaras](/knowledge/monero-outputs)/

  * [Monero bästa praxis för nybörjare](/knowledge/monero-best-practices)/

  * [Hur Monero löste problemet med blockstorlek som plågar Bitcoin](/knowledge/dynamic-block-size)/

  * [Hur CLSAG kommer att förbättra Moneros effektivitet](/knowledge/what-is-clsag)/

  * [Varför Monero har en svans emission](/knowledge/monero-tail-emission)/

  * [En kort historia om Monero](/knowledge/monero-history)/

  * [Wired Magazine har fel om Monero, här är varför](/knowledge/wired-article-debunked)/

  * [Topp 15 Monero myter och bekymmer debunked](/knowledge/monero-myths-debunked)/

  * [Hur Dandelion++ håller Moneros transaktionsursprung privat](/knowledge/monero-dandelion)/

  * [Varför Monero är öppen källkod och decentraliserad](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: Vad gör RandomX så speciellt](/knowledge/monero-mining-randomx)/

  * [Varför Monero är bättre än Dash, Zcash, Zcoin (även med Lelantus), Grin och Bitcoin Mixers som Wasabi (Uppdaterad maj 2020)](/knowledge/why-monero-is-better)/

Vidare läsning