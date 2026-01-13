---
title: "Hur atombyten kommer att fungera i Monero"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
I jakten på decentralisering och ett verkligt tillståndslöst system är få saker så eftertraktade i kryptovalutaområdet som decentraliserade utbyten och atomswappar. Sedan starten har Monero kämpat för att implementera atomswappar, eftersom integritetsfunktionerna skapar unika problem när man försöker designa ett protokoll.

Men först, låt oss säkerhetskopiera. Vad är atombyten? En atomswap är ett protokoll genom vilket två olika kryptovalutor, på olika blockkedjor, kan bytas ut på ett tillitslöst sätt utan någon mellanhand. Det betyder att om någon ville byta kryptovaluta A mot kryptovaluta B, skulle de kunna göra det utan ett utbyte, centraliserat eller decentraliserat. Som man kan föreställa sig kräver detta avsevärd forskning, och de fullständiga tekniska detaljerna som gör det möjligt blir ganska komplicerat. Återigen, LocalMonero är här för att hjälpa och ge en enkel förklaring för den vanliga personen.

Bob använder denna hash som ett frö från vilket han genererar sin egen lockbox, och skickar sin LTC dit, där den också är låst. Eftersom hashen av Alices nyckel användes som fröet som Bobs låslåda gjordes av, kan hon använda sin nyckel för att göra anspråk på LTC i Bobs låslåda. Hennes nyckel passar! Men med hjälp av matematisk voodoo-magi, när hon använder sin nyckel för att öppna LTC-låset, avslöjar hon nyckeln för Bob, som sedan kan använda den för att göra anspråk på BTC som hon lade i sin låslåda. På detta sätt, utan någon mellanhand, har Alice och Bob framgångsrikt bytt ut sina tillgångar.

Men det finns ett litet problem. Tänk om Alice skickar till sin låsbox och Bob bestämmer sig för att han inte vill handla längre. Nu, eftersom Alice inte kan komma åt sin BTC som hon låste, och Bob inte kommer att slutföra sin del av transaktionen, förlorar Alice bara sina pengar för alltid. Tja, lyckligtvis har Bitcoin en liten teknik som kallas återbetalningstransaktioner, och så efter en tid, om BTC inte görs anspråk på av Bob, har skripten en inbyggd felsäker, där BTC automatiskt går tillbaka till Alice. Detta var den primära fartbulten för Moneros implementering av atomswappar. På grund av Moneros [ringsignaturers sekretessteknologi](/knowledge/ring-signatures) är avsändaren av en transaktion alltid osäker. Hur kan protokollet göra en återbetalningstransaktion om den inte ens vet var transaktionen kom ifrån?

Under 2017 beskrev en liten grupp forskare en annan metod med vilken atombyten skulle fungera i Monero. Efter flera års förfining slutförde forskarna en process genom vilken Monero skulle kunna göra atomswappar med Bitcoin, även utan återbetalningstransaktioner.

Som med många saker på den här nivån av teknisk komplexitet kommer vår förklaring att förenkla vissa saker för att förmedla idén, men den kommer fortfarande att ge en solid uppfattning om de mekanismer genom vilka denna process skulle fungera.

Både Alice (som har XMR och vill ha BTC) och Bob (som har BTC och vill ha XMR) måste ladda ner och köra ett program som stöder atomic swap. Detta kan implementeras i plånböcker, decentraliserade börser eller speciella, specifika program, men programvaran måste köra atomic swap-protokollet. I det första steget ansluter Alice och Bobs klienter till varandra och skapar flera delade hemligheter och nycklar. I det här steget skapas en ny Monero-adress, där Alice har ena halvan av nyckeln och Bob har den andra. Det finns dock inga Monero där ännu, så det finns inget att spendera. En sista sak att notera om den här adressen är att de båda har nyckeln till den här plånboken, så de kan båda kika in för att se om eller när Monero anländer.

I det andra steget skickar Bob sina BTC till en speciell adress, liknande Bitcoin atomic swap-protokollet som vi redan har diskuterat. När Alice ser BTC anlända till denna adress på blockkedjan skickar hon sin Monero till den Monero-adress som hon och Bob båda har hälften av en nyckel till. Bob kan verifiera att Monero anlänt eftersom han också har visningsnyckeln, och när han ser att Monero är säkert i hans plånbok skickar han Alice en bit av en nyckel som gör det möjligt för henne att ta ut Bitcoin. På samma sätt som i det andra protokollet avslöjar Alice sin halva av Monero-nyckeln för Bob när hon gör anspråk på Bitcoin. Nu har Bob båda halvorna, så han kan göra anspråk på Monero, medan Alice bara har sin halva, så hon kan inte försöka ta den innan han gör det.

Så om du tittat på allt detta och fortfarande är lite förvirrad över hur Monero kunde komma runt problemet med återbetalningstransaktioner, är svaret ganska enkelt. Eftersom Monero själv inte har återbetalningstransaktioner bör läsaren märka att Bitcoin (som har återbetalningstransaktioner) skickas först, och först efter att det har verifierats att det finns på blockkedjan skickas Monero. Detta gör att Monero kan använda Bitcoins förmåga att skriva in återbetalningstransaktioner och dra nytta av dem, utan att behöva ha dessa förmågor själv.

Atombytet är nu slutfört, men nu har Bob ett par alternativ för sin nya XMR. Han kan använda den här Monero-plånboken som den är, eller flytta XMR till en annan plånbok som han redan äger. Bob kommer troligtvis att flytta Monero till en annan plånbok, eftersom Alice fortfarande har nyckeln och kan se in i den.

Det fina med detta protokoll är att det fortfarande är ganska nytt, och det finns gott om utrymme för optimeringar. Det är också ganska flexibelt i sin arkitektur, så implementering i andra plånböcker eller decentraliserade börser bör vara enkel och passa rent med deras befintliga arkitektur.

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

  * [Vad varje Monero-användare behöver veta när det gäller nätverkande](/knowledge/monero-networking/)

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