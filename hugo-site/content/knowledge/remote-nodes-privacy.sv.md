---
title: "Hur fjärrnoder påverkar Moneros integritet"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
En av de största fördelarna som Monero har jämfört med andra kryptovalutor är att det är on-chain integritet, men har du någonsin undrat hur Moneros integritet håller sig när du använder en fjärrnod? Vad sägs om om du använder en "light wallet"-server som MyMonero?

I det här inlägget kommer vi att dyka ner i några av detaljerna bakom hur Monero ger exceptionell integritet i kedjan även när du använder en fjärrnod, samt vad du ska se upp med när du använder fjärrnoder.

## Vilken funktion har noder i Monero?

## Vilken funktion har noder i Monero?

För de som är mindre bekanta med hur Monero fungerar, kan noderna (eller servrarna) i Monero-nätverket drivas av vem som helst och låta ägaren av noden – eller andra de väljer att dela den med! – att synkronisera en kopia av blockkedjan och tillhandahålla den kopian till andra på nätverket. Dessa noder verifierar också alla transaktioner som sker på nätverket, såväl som alla block som publiceras och säkerställer att de alla följer reglerna enligt konsensus.

Den andra funktionen som noder tjänar i Monero är ett sätt att tillhandahålla all data som din favorit Monero-plånbok behöver för att korrekt kontrollera transaktioner som tillhör dig och göra nya transaktioner. Dessa data tillhandahålls av noder på två sätt:

  * Datan från varje block i blockkedjan begärs av plånboken, skannas efter transaktioner som tillhör dig och kasseras sedan när de kontrollerats av plånboken. 
    * Det här steget kommer snart att förbättras drastiskt, tack vare [visningstaggar](/knowledge/view-tags-reduce-monero-sync-time).
  * När du skickar transaktioner tillhandahåller den nod du använder en lista över möjliga decoys (eller falska ingångar) att använda när du bygger transaktionen, vilket säkerställer att du har en bra folkmassa att gömma dig i varje gång du spenderar Monero. 
    * Dessa lockbeten är en del av [ringsignaturer](/knowledge/ring-signatures), en viktig del av Moneros syn på integritet på kedjan.

  * Det här steget kommer snart att förbättras drastiskt, tack vare [visningstaggar](/knowledge/view-tags-reduce-monero-sync-time).

  * Dessa lockbeten är en del av [ringsignaturer](/knowledge/ring-signatures), en viktig del av Moneros syn på integritet på kedjan.

## Vad är det mest privata och säkra sättet att använda Monero?

## Vad är det mest privata och säkra sättet att använda Monero?

Det bästa du kan göra, även med den starka on-chain integritet som tillhandahålls av Monero när du använder fjärrnoder, är att köra din egen Monero-nod för att säkerställa att du har en ren kopia av Monero blockchain till hands och att din IP-adress är väl skyddad. Den andra fördelen med att köra din egen nod är att du kan bidra tillbaka till nätverket, låta andra noder synkronisera från din nod eller till och med låta andra användare ansluta till din nod med sina plånböcker.

Med det sagt ger Monero fortfarande utmärkt sekretess när du använder en fjärrnod. Om du är intresserad av att köra din egen Monero-nod, här är en enkel guide för att göra det:

  * [Kör en Monero Node](https://sethforprivacy.com/guides/run-a-monero-node/)

## Vad kan en avlägsen nod få veta om mig?

## Vad kan en avlägsen nod få veta om mig?

När du använder en fjärrnod finns det några viktiga delar av information som exponeras för en fjärrnod och ett par viktiga sätt som noden kan attackera dig, hindra dig från att göra transaktioner och mer.

Det första en fjärrnod kan lära sig om dig är din offentliga IP-adress. Även om detta förhoppningsvis kommer att döljas via en VPN eller Tor, kan fjärrnoden associera din offentliga IP-adress med transaktionen, vilket hjälper dem att begränsa var du gör transaktioner från. Fjärrnoden kan också lära sig det sista blocket som din plånbok synkroniserades och använda detta för att försöka göra välgrundade gissningar om dig, som när du normalt använder Monero och när du senast spenderade Monero. Detta gäller särskilt om du alltid kommer från samma IP-adress (som ditt hem). Det sista viktiga som en fjärrnod kan lära sig om dig är grundläggande information om de transaktioner du skickar genom den. Även om detta kan vara den mest uppenbara informationen som fjärrnodoperatören får om dig, är det viktigt att förstå att detta kan användas för att hjälpa till att spåra avsändaren av transaktionen när man kombinerar den informationen med annan data utanför kedjan. Detta kan vara särskilt farligt om fjärrnoden drivs av en skadlig enhet, ett blockkedjeanalysföretag eller en förtryckande nationalstat.

En fjärrnod kan också försöka orsaka dig problem genom att dölja block för dig, vilket får din plånbok att tro att den var synkroniserad när den inte var det. Detta kan få dig att tro att pengar går förlorade eller hindra dig från att spendera pengar tills du ansluter till en annan nod. Det sista viktiga som en fjärrnod kan göra är att mata din plånbok med en manipulerad lista med lockbeten. Detta kan göra att din plånbok antingen misslyckas helt med att skapa transaktioner (vilket gör att du inte kan spendera pengar), eller så kan fjärrnoden försöka tillhandahålla lockbeten som den vet spenderas för att minska anonymiteten du får i varje transaktion.

## Vilka integritetsgarantier finns fortfarande när man använder en fjärrnod?

## Vilka integritetsgarantier finns fortfarande när man använder en fjärrnod?

Även om den här artikeln kan ha skrämt dig lite, är det viktigt att inse att integriteten som tillhandahålls av Monero är utmärkt även när du använder en fjärrnod, och vida överträffar alla andra kryptovalutor när den används på detta sätt. Du får fortfarande den starka integriteten på kedjan som tillhandahålls av Monero, eftersom fjärrnoden aldrig vet den verkliga ingången (vilka mynt du spenderar), mängden Monero som spenderas i transaktionen eller adressen till mottagaren av transaktionen. Utomstående observatörer kan inte heller se den verkliga inmatningen, mängden eller adresserna som är involverade (oavsett vilken typ av nod du väljer att använda!), vilket säkerställer att utanför fjärrnoden även din IP-adress, plånbokssynkroniseringsinformation och transaktioner har starka integritetsgarantier .

Fjärrnoden har heller aldrig tillgång till de tidigare transaktionerna du har skickat eller tagit emot eller mängden Monero som för närvarande finns i din plånbok, och förlorar all insyn i dina transaktioner i samma ögonblick som du börjar använda en annan nod. Inga privata nycklar (varken spend- eller visningsnycklar) tillhandahålls någonsin till fjärrnoden, så din plånbok förblir privat, säker och användbar. Oavsett fjärrnod riskerar du heller aldrig att förlora Monero eller få den stulen, eftersom noden inte kan redigera mottagaradressen, aldrig har tillgång till dina plånboksnycklar och inte kan konfiskera din Monero på något sätt.

## Vad sägs om "lätta plånböcker" som MyMonero?

## Vad sägs om "lätta plånböcker" som MyMonero?

Även om ämnet ligger lite utanför ramen för den här artikeln, ville jag ta upp en unik typ av plånbok i Monero – lätta plånböcker. Namnet light wallet kommer från det faktum att din plånbok (på din telefon eller dator) inte behöver utföra någon blockchain-synkronisering, vilket gör upplevelsen snabbare och mer flytande.

Men plånböcker som denna kommer med en allvarlig kompromiss med sekretess för tillfället – din plånbok skickar den privata vynyckeln till fjärrservern du använder (som standarden i MyMonero), vilket ger fjärrservern full insyn i alla mottagna pengar sedan du skapade din plånbok (och tills du slutar använda den plånboken eller fröet). Detta minskar integriteten du får från nodoperatören drastiskt och bör behandlas med försiktighet.

Tack och lov arbetar Monero-communityt på att förbättra programvaran du kan använda för att vara värd för din egen lätta plånboksserver (LWS), som gör att du kan ha snabb synkronisering utan att lita på en tredje part med dina privata vynycklar – när du kommer att köra programvaran dit din plånbok skickar de privata vynycklarna!

För mer om den anpassade lätta plånboksservern, se Github-förrådet nedan:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Hur kan jag lära mig mer?

## Hur kan jag lära mig mer?

Om du är nyfiken och skulle älska att bättre förstå noder i Monero och titta på att använda en fjärrnod eller köra din egen, se länkarna nedan för bra ställen att komma igång:

  * [Monero World, en lista över gemenskapsdrivna fjärrnoder som kan användas](https://moneroworld.com/#nodes)
  * [Monero-noder som drivs av Seth For Privacy, författaren till den här artikeln](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, en lista över fjärrnoder med ofta kontrollerad status< /a>](https://monero.fail/)
  * [Så här ansluter du till en fjärrnod i GUI-plånboken](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia – fjärrkontroll Nod](https://www.getmonero.org/resources/moneropedia/remote-node.html)

Vidare läsning

  * [Hur Monero unikt möjliggör cirkulära ekonomier](/knowledge/monero-circular-economies)/

  * [Moneros ringsignaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Varför (och hur!) du ska hålla i dina egna nycklar](/knowledge/hold-your-keys)/

  * [Bidrar tillbaka till Monero](/knowledge/contributing-to-monero)/

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

  * [Hur ringsignaturer obskyr Moneros utgångar](/knowledge/ring-signatures)/

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