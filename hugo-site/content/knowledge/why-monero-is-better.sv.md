---
title: "Varför Monero är bättre än Dash, Zcash, Zcoin (även med Lelantus), Grin och Bitcoin Mixers som Wasabi (Uppdaterad maj 2020)"
slug: "why-monero-is-better"
date: "2024-01-01"
image: "/images/why-monero.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Inte alla integritetscentrerade mynt kan leverera 100% integritet, ospårbarhet, säkerhet och fungibilitet i ett 100% decentraliserat mynt med en tillitslös inställning. Här är vad dessa attribut är och varför de är viktiga:

## Mynt analys

Här är en analys av välkända kryptovalutor som hävdar anonymitet och/eller ospårbarhet som sin viktigaste differentiator. Bitcoin i sig omfattas inte av denna analys eftersom den aldrig har påstått sig vara anonym.

Den här sidan skapades av Monero-användare. Det fanns en tid då vi inte var Monero-användare utan var oroliga för ekonomisk integritet. Vi undersökte mynten som påstod sig vara privata och den här sidan är resultatet av vår forskning. Det är därför vi valde Monero framför resten. Så om vi verkar vara partiska är vi det, men vi tror att partiskhet är baserad på fakta som du kan läsa nedan och verifiera själv.

### Översikt

Välj en logotyp för att hoppa till analysen av det myntet.

### Monero

Monero har varit 100% öppen källkod sedan starten, vilket innebär att vem som helst kan se programvarans [ källkod ](https://github.com/monero-project/bitmonero) för att verifiera att det inte finns några bakdörrar och att programvaran är säker.

Monero har också [ kollegialt granskade forskningsrapporter ](https://lab.getmonero.org/) som matematiskt och systematiskt verifierar alla de egenskaper som anges ovan.

### DASH

DASH har en [ rik lista](https://bitinfocharts.com/top-100-richest-darkcoin-addresses.html), så detta är inte ett privat mynt. De finansiella detaljerna för myntadresser är synliga för alla som undersöker blockkedjan.

> DASH är inte kryptografiskt privat alls. Egentligen hade jag en rutschkana i kortleken som var som "DASH, LOL", och som inget annat... det är snakeoil och jag är helt enkelt utom mig om det personligen. 
> 
> **Gregory Maxwell** , Bitcoin Core-utvecklare och kryptograf, i en [-presentation till Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

DASH är inte kryptografiskt privat alls. Egentligen hade jag en rutschkana i kortleken som var som "DASH, LOL", och som inget annat... det är snakeoil och jag är helt enkelt utom mig om det personligen. 

**Gregory Maxwell** , Bitcoin Core-utvecklare och kryptograf, i en [-presentation till Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

**Peter Todd** , en annan Bitcoin Core-utvecklare och kryptograf, har gjort ett [ liknande uttalande](https://twitter.com/petertoddbtc/status/622022840330682368).

### Zcash

Zcash-transaktioner är synliga på deras blockchain. De möjliggör dolda transaktioner, men [ mindre än 1 % av transaktionerna är helt skärmade ](http://stat.bloxy.info/superset/dashboard/zcash/) . Eftersom dolda transaktioner är valfria och inte standard (för att inte nämna sällan används), sticker de [ dolda transaktionerna ut i sin blockchain](http://weuse.cash/2016/06/09/btc-xmr-zcash/) och drar uppmärksamheten till sig själva.

> Och förresten, jag tror att vi framgångsrikt kan göra Zcash för spårbart för brottslingar som WannaCry, men fortfarande helt privat & fungibel. 
> 
> **Zooko Wilcox** , Zcash VD, i en [ tweet ](https://twitter.com/zooko/status/863202798883577856)

Och förresten, jag tror att vi framgångsrikt kan göra Zcash för spårbart för brottslingar som WannaCry, men fortfarande helt privat & fungibel. 

**Zooko Wilcox** , Zcash VD, i en [ tweet ](https://twitter.com/zooko/status/863202798883577856)

Om Zcash kan vara "för spårbart", så kan det inte vara helt privat eller fungibelt. 

Regelbundna transaktioner är transparenta. Dolda transaktioner använder zk-SNARKS, som visserligen har robusta integritetsgarantier under vissa villkor. Frågan är om dessa villkor är uppfyllda, och med tanke på den minimala mängden människor som använder de avskärmade funktionerna är detta fortfarande ifrågasatt.

Zcash är ett företag och för närvarande tar det [ 20 % av alla ZEC som utvinns som en grundares belöning](https://z.cash/blog/funding.html). 

Zcash krävde en **Trusted Setup**. Det betyder att du måste lita på att systemet är ärligt uppsatt. Om det inte var uppriktigt konfigurerat kunde [ obegränsade mängder ZEC skapas utan att någon visste det](https://blog.okturtles.com/2016/03/the-zcash-catch/). Detta skulle göra hackaren rik och devalvera ZEC. Det finns inget sätt att veta om Trusted Setup utfördes ärligt. Vi måste ta dem på ordet. Detta introducerar en mänsklig punkt av misslyckande i systemet som strider mot nästan alla andra kryptovalutor. Du ska bara behöva lita på matematik och verifierbar källkod i kryptovalutor, inte människor. Som vi har sett med praktiskt taget alla stora mjukvaruföretag, som [ Microsoft](https://www.gnu.org/proprietary/proprietary-back-doors.en.html), [ Apple](http://www.digitaltrends.com/computing/apple-vs-fbi-backdoor-to-data-already-exists/), och till och med regeringar, bör de inte lita på. 

Peter Todd, en Bitcoin Core-utvecklare som [ deltog ](https://github.com/zcash/mpc/blob/master/README.md) i Zcash Trusted Setup, har kallat det en " [ bakdörr ](https://twitter.com/petertoddbtc/status/793584540891643906) ". 

> Zcash är inte ovillkorligt bra, kan inte vara med nuvarande teknik...kräver en pålitlig installation… kommer att behöva göra om proceduren [Trusted Setup] för att uppgradera kryptot över tid så det är en sårbarhet. 
> 
> Gregory Maxwell, Bitcoin Core-utvecklare och kryptograf, i en [-presentation till Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

Zcash är inte ovillkorligt bra, kan inte vara med nuvarande teknik...kräver en pålitlig installation… kommer att behöva göra om proceduren [Trusted Setup] för att uppgradera kryptot över tid så det är en sårbarhet. 

Gregory Maxwell, Bitcoin Core-utvecklare och kryptograf, i en [-presentation till Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

### Zcoin

**Obs:** Zcoin går från sitt nuvarande Sigma-schema till ett nytt protokoll som förlitar sig på sitt nya arbete, Lelantus. Lelantus kommer att implementeras i etapper, och den här artikeln kommer att anta att alla steg är kompletta och implementerade för korrekta jämförelser tillsammans med beräknade implementeringstider.

Anledningen till att Zcoin fick den här lyxen att bedömas utifrån dess framtida protokoll, och inte Zcash, är att Zcoin har en färdplan med allmänna tidpunkter för aktivering, medan Zcashs "privacy by default"-planer är och fortsätter att vara oklara.[ X563X]

Zcoin (XZC) kommer inte att ha en rik lista, så den kommer att vara privat. Som standard förväntas obligatorisk integritet aktiveras 2021. När den väl har implementerats kommer en rik lista inte att vara möjlig att skapa (även om för närvarande [de har en](https://www.coinexplorer.net/XZC/richlist)).

### Grin

### Bitcoin Mixers

Alla Bitcoin-transaktioner är synliga på blockkedjan och det finns en [ Bitcoin-rik lista](http://www.bitcoinrichlist.com/top100), så Bitcoin är inte privat. Bitcoin är [ pseudononym](https://bitcoin.org/en/you-need-to-know), inte anonym. 

För **Bitcoin-mixers** måste du lita på att de kan hålla sin data säker och inte ägs av eller samarbetar med en regering, hackare eller andra enheter. 

I juli 2017 meddelade grundaren av den största Bitcoin-blandningstjänsten, BITMIXER.IO, att de stänger och angav detta som sin anledning: 

> … Nu förstod jag att Bitcoin är ett transparent icke-anonymt system **av design**. Blockchain är en fantastisk öppen bok… 
> 
> BITMIXER.IO, i ett tillkännagivande om stängning på [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (betoning i originalet). 

… Nu förstod jag att Bitcoin är ett transparent icke-anonymt system **av design**. Blockchain är en fantastisk öppen bok… 

BITMIXER.IO, i ett tillkännagivande om stängning på [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (betoning i originalet). 

Några veckor senare, efter att ha övervägt de olika integritetscentrerade mynten, sa han detta: 

> Efter den djupa undersökningen bekräftar jag att MONERO är den bästa sekretessvalutan. Så jag rekommenderar starkt MONERO för alla människor som behöver extra integritet. 
> 
> BITMIXER.IO, i ett [ uppföljningsinlägg](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Efter den djupa undersökningen bekräftar jag att MONERO är den bästa sekretessvalutan. Så jag rekommenderar starkt MONERO för alla människor som behöver extra integritet. 

BITMIXER.IO, i ett [ uppföljningsinlägg](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Eftersom alla Bitcoin-transaktioner är synliga på blockkedjan kan ALLA Bitcoin-transaktioner spåras. En Bitcoin-mixer kan i hög grad fördunkla transaktioner, vilket gör det mycket svårare för någon att spåra Bitcoins, men inte omöjligt. Allt eftersom tekniken fortskrider och företag som specialiserar sig på att spåra Bitcoin-transaktioner blir vanligare, kommer transaktioner som är mycket obfuskerade att bli relativt lätta att spåra: 

  * [ Brottsbekämpning fortsätter att investera i Bitcoin-spårningstjänster ](https://news.bitcoin.com/law-enforcement-continues-invest-bitcoin-tracking-services/)
  * [ Time.com: Bitcoins är enklare att spåra än du tror ](http://time.com/3689359/bitcoins-track-anonymous/)
  * [ Elliptic: Ett företag som specialiserat sig på att spåra Bitcoin för brottsbekämpning ](https://www.elliptic.co/)

En sökning på Google kommer att avslöja dussintals artiklar som de ovan. Och kom ihåg, alla transaktioner som inträffade någon gång i det förflutna finns i blockkedjan och har potential att spåras, även om en blandningstjänst användes. Faktum är att användningen av en blandningstjänst sannolikt kommer att uppmärksamma dessa transaktioner. 

Alla Bitcoins är inte lika och har samma värde. Vissa Bitcoins har svartlistats och blockerats av flera enheter, vilket gör dessa mynt mindre värda än resten. Om du tar emot Bitcoins som användes tidigare i olagliga syften, kan dina Bitcoins svartlistas även om du inte hade något med den illegala aktiviteten att göra. Eller, säg att en regering, arbetsgivare eller någon annan enhet bestämmer sig för att svartlista dina Bitcoins i framtiden, ungefär som de gör med frysning eller konfiskering av tillgångar. Det skulle inte finnas något du kunde göra. Eftersom en mixer bara gör det svårare att spåra dina Bitcoins, har den här kategorin markerats som "inte fungibel." 

  * Andreas Antonopoulos, en före detta Bitcoin Core-utvecklare som är välrespekterad i Bitcoin och andra kryptovalutagemenskaper, erkänner Bitcoin-fungibilitetsproblemet i en [ YouTube-video](https://www.youtube.com/watch?v=ak1iojpiHpM&feature=youtu .be&t=33m9s). 
  * Diskussion om Bitcoin-fungibilitetsproblemet på [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=1190707.0)

## Sammanfattning

Enligt vår åsikt är Monero det tydliga valet om du letar efter en privat, säker, ospårbar, fungibel, decentraliserad kryptovaluta utan någon pålitlig installation som krävs. Allt annat sätter din integritet och säkerhet på spel. Men ta inte bara vår åsikt. Gör din egen forskning och se själv. Tänk på att Monero stöds och används av enheter som är beroende av integritet och ospårbarhet, till exempel: 

  * [ SIGAINT ](https://www.reddit.com/r/Monero/comments/4xqrzd/sigaint_launches_tor_monero_node_as_its_operators/)
  * [ Purism ](https://puri.sm/posts/purism-collaborates-with-cryptocurrency-monero-to-enable-mobile-payments/)
  * [ Wikileaks ](https://shop.wikileaks.org/donate#db9)
  * AlphaBay Market (AB) stängdes i juli 2017. [ Federal Forfeiture Complaint ](https://assets.documentcloud.org/documents/3898109/AlphaBay-Cazes-Forfeiture-Complaint.pdf) mot AB visar att: 
    * **Monero är den enda privata och ospårbara kryptovalutan:**   
"Totalt från CAZES plånböcker och datoragenter tog kontroll över cirka 8 800 000 $ i Bitcoin, Ethereum, Moreno [sic] och Zcash, uppdelat enligt följande: 1 605,0503851 Bitcoin, 8 309,271639 Ethereum, [3,691, [3,691, 8,691, X och 8,691, 8,691, 8,691, 8,691, 8,691 och okänd mängd Monero." (längst ner på s. 20 och överst på s. 21, kursivering tillagd) 
    * **Bitcoin-transaktioner är inte privata och kan spåras:**   
"Federala agenter erhöll teckningsoptionerna efter att ha spårat ett antal Bitcoin-transaktioner som härrörde från AlphaBay till digitala valutakonton, och slutligen bankkonton och andra materiella tillgångar, som innehas av CAZES och hans fru." (sid. 17, rad 24- 26) 

  * **Monero är den enda privata och ospårbara kryptovalutan:**   
"Totalt från CAZES plånböcker och datoragenter tog kontroll över cirka 8 800 000 $ i Bitcoin, Ethereum, Moreno [sic] och Zcash, uppdelat enligt följande: 1 605,0503851 Bitcoin, 8 309,271639 Ethereum, [3,691, [3,691, 8,691, X och 8,691, 8,691, 8,691, 8,691, 8,691 och okänd mängd Monero." (längst ner på s. 20 och överst på s. 21, kursivering tillagd) 
  * **Bitcoin-transaktioner är inte privata och kan spåras:**   
"Federala agenter erhöll teckningsoptionerna efter att ha spårat ett antal Bitcoin-transaktioner som härrörde från AlphaBay till digitala valutakonton, och slutligen bankkonton och andra materiella tillgångar, som innehas av CAZES och hans fru." (sid. 17, rad 24- 26) 

LocalMonero förespråkar eller uppmuntrar inte någon olaglig aktivitet. 

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