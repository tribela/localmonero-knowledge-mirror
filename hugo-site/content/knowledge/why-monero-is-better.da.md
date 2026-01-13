---
title: "Hvorfor Monero er bedre end Dash, Zcash, Zcoin (selv med Lelantus), Grin og Bitcoin-mixere som Wasabi (Opdateret maj 2020)"
slug: "why-monero-is-better"
date: "2024-01-01"
image: "/images/why-monero.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Ikke alle privatlivscentrerede mønter kan levere 100 % privatliv, usporbarhed, sikkerhed og fungibilitet i en 100 % decentral mønt med en tillidsfri opsætning. Her er, hvad disse egenskaber er, og hvorfor de er vigtige:

## Mønt analyse

Her er en analyse af velkendte kryptovalutaer, som hævder anonymitet og/eller usporbarhed som deres vigtigste differentiator. Bitcoin i sig selv er ikke inden for rammerne af denne analyse, da det aldrig hævdes at være anonymt.

Denne side er lavet af Monero-brugere. Der var engang, hvor vi ikke var Monero-brugere, men var bekymrede for økonomisk privatliv. Vi undersøgte de mønter, der hævdede at være private, og denne side er resultatet af vores forskning. Det er derfor, vi valgte Monero frem for resten. Så hvis vi ser ud til at være partiske, er vi det, men vi mener, at bias er baseret på fakta, som du kan læse nedenfor og selv verificere.

### Overblik

Vælg et logo for at gå til analysen af den pågældende mønt.

### Monero

Monero har været 100 % open source fra starten, hvilket betyder, at alle kan se softwarens [ kildekode ](https://github.com/monero-project/bitmonero) for at bekræfte, at der ikke findes bagdøre og at softwaren er sikker.

Monero har også [ peer-reviewed research papers ](https://lab.getmonero.org/), som matematisk og systematisk verificerer alle dets egenskaber, der er anført ovenfor.

### DASH

DASH har en [ rig liste](https://bitinfocharts.com/top-100-richest-darkcoin-addresses.html), så dette er ikke en privat mønt. De økonomiske detaljer om møntadresser er synlige for alle, der undersøger blockchain.

> DASH er slet ikke kryptografisk privat. Faktisk havde jeg en rutsjebane i dækket, der var ligesom 'DASH, LOL' og som intet andet... det er slangeolie, og jeg er personligt lidt ude af mig selv. 
> 
> **Gregory Maxwell** , Bitcoin Core-udvikler og kryptograf, i en [ præsentation til Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

DASH er slet ikke kryptografisk privat. Faktisk havde jeg en rutsjebane i dækket, der var ligesom 'DASH, LOL' og som intet andet... det er slangeolie, og jeg er personligt lidt ude af mig selv. 

**Gregory Maxwell** , Bitcoin Core-udvikler og kryptograf, i en [ præsentation til Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

**Peter Todd** , en anden Bitcoin Core-udvikler og kryptograf, har lavet en [ lignende erklæring](https://twitter.com/petertoddbtc/status/622022840330682368).

### Zcash

Zcash-transaktioner er synlige på deres blockchain. De aktiverer skjulte transaktioner, men [ mindre end 1 % af transaktionerne er fuldt afskærmet ](http://stat.bloxy.info/superset/dashboard/zcash/) . Da skjulte transaktioner er valgfrie og ikke standard (for ikke at nævne sjældent brugte), skiller de [ skjulte transaktioner sig ud på deres blockchain](http://weuse.cash/2016/06/09/btc-xmr-zcash/), der gør opmærksom på sig selv.

> Og i øvrigt tror jeg, at vi med succes kan gøre Zcash for sporbar for kriminelle som WannaCry, men stadig helt privat & ombytteligt. 
> 
> **Zooko Wilcox** , Zcash CEO, i et [ tweet ](https://twitter.com/zooko/status/863202798883577856)

Og i øvrigt tror jeg, at vi med succes kan gøre Zcash for sporbar for kriminelle som WannaCry, men stadig helt privat & ombytteligt. 

**Zooko Wilcox** , Zcash CEO, i et [ tweet ](https://twitter.com/zooko/status/863202798883577856)

Hvis Zcash kan være "for sporbar", så kan den ikke være helt privat eller fungibel. 

Regelmæssige transaktioner er gennemsigtige. Skjulte transaktioner bruger zk-SNARKS, som ganske vist har robuste privatlivsgarantier under visse betingelser. Spørgsmålet er, om disse betingelser er opfyldt, og i betragtning af den minimale mængde mennesker, der bruger de afskærmede kapaciteter, er dette stadig i tvivl.

Zcash er en virksomhed, og i øjeblikket tager den [ 20 % af alle ZEC udvundet som en grundlæggers belønning](https://z.cash/blog/funding.html). 

Zcash krævede en **Trusted Setup**. Det betyder, at du skal stole på, at systemet er sat ærligt op. Hvis det ikke var konfigureret ærligt, kunne der oprettes [ ubegrænsede mængder af ZEC, uden at nogen ved det](https://blog.okturtles.com/2016/03/the-zcash-catch/) . Dette ville gøre hackeren rig og devaluere ZEC. Der er ingen måde at vide, om Trusted Setup blev udført ærligt. Vi må tage dem på ordet. Dette introducerer et menneskeligt fejlpunkt i systemet, som er i modstrid med næsten enhver anden kryptovaluta. Du skal kun stole på matematik og verificerbar kildekode i kryptovalutaer, ikke mennesker. Som vi har set med stort set alle store softwarevirksomheder, såsom [ Microsoft](https://www.gnu.org/proprietary/proprietary-back-doors.en.html), [ Apple](http://www.digitaltrends.com/computing/apple-vs-fbi-backdoor-to-data-already-exists/) og endda regeringer, de bør ikke stole på. 

Peter Todd, en Bitcoin Core-udvikler, som [ deltog ](https://github.com/zcash/mpc/blob/master/README.md) i Zcash Trusted Setup, har kaldt det en" ; [ bagdør ](https://twitter.com/petertoddbtc/status/793584540891643906) ". 

> Zcash er ikke ubetinget sund, kan ikke være med den nuværende teknologi...kræver en pålidelig opsætning … bliver nødt til at gentage proceduren [Trusted Setup] for at opgradere kryptoen over tid, så det er en sårbarhed. 
> 
> Gregory Maxwell, Bitcoin Core-udvikler og kryptograf, i en [ præsentation til Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

Zcash er ikke ubetinget sund, kan ikke være med den nuværende teknologi...kræver en pålidelig opsætning … bliver nødt til at gentage proceduren [Trusted Setup] for at opgradere kryptoen over tid, så det er en sårbarhed. 

Gregory Maxwell, Bitcoin Core-udvikler og kryptograf, i en [ præsentation til Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

### Zcoin

**Bemærk:** Zcoin skifter fra sit nuværende Sigma-skema til en ny protokol, der er afhængig af sit nye arbejde, Lelantus. Lelantus vil blive implementeret i etaper, og denne artikel vil antage, at alle faser er færdige og implementeret til korrekte sammenligninger sammen med forventede implementeringstider.

Grunden til, at Zcoin fik denne luksus at blive bedømt på sin fremtidige protokol, og ikke Zcash, er fordi Zcoin har en køreplan med generelle timings for aktivering, hvorimod Zcash's 'privatliv som standard'-planer er og fortsat er tågelige.

Zcoin (XZC) vil ikke have en rig liste, så den vil være privat. Som standard forventes obligatorisk privatliv at gå live i 2021. Når den er implementeret, vil en rig liste ikke være mulig at oprette (selvom [de pt. har en](https://www.coinexplorer.net/XZC/richlist)).

### Grin

### Bitcoin Mixers

Alle Bitcoin-transaktioner er synlige på blockchain, og der er en [ Bitcoin Rich List](http://www.bitcoinrichlist.com/top100), så Bitcoin er ikke privat. Bitcoin er [ pseudononym](https://bitcoin.org/en/you-need-to-know), ikke anonymt. 

For **Bitcoin-mixere** skal du stole på, at de kan holde deres data sikre og ikke ejes af eller samarbejder med en regering, hackere eller andre enheder. 

I juli 2017 annoncerede grundlæggeren af den største Bitcoin-blandingstjeneste, BITMIXER.IO, at de var ved at lukke og gav dette som deres grund: 

> … Nu forstod jeg, at Bitcoin er et gennemsigtigt ikke-anonymt system **ved design**. Blockchain er en fantastisk åben bog… 
> 
> BITMIXER.IO, i en meddelelse om lukning på [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (fremhævet i originalen). 

… Nu forstod jeg, at Bitcoin er et gennemsigtigt ikke-anonymt system **ved design**. Blockchain er en fantastisk åben bog… 

BITMIXER.IO, i en meddelelse om lukning på [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (fremhævet i originalen). 

Et par uger senere, efter at have overvejet de forskellige privatlivscentrerede mønter, sagde han dette: 

> Efter den dybe undersøgelse bekræfter jeg, at MONERO er den bedste privatlivsvaluta. Så jeg anbefaler stærkt MONERO til alle mennesker, der har brug for ekstra privatliv. 
> 
> BITMIXER.IO, i et [ opfølgende indlæg](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Efter den dybe undersøgelse bekræfter jeg, at MONERO er den bedste privatlivsvaluta. Så jeg anbefaler stærkt MONERO til alle mennesker, der har brug for ekstra privatliv. 

BITMIXER.IO, i et [ opfølgende indlæg](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Da alle Bitcoin-transaktioner er synlige på blockchainen, kan ALLE Bitcoin-transaktioner spores. En Bitcoin-mixer kan meget sløre transaktioner, hvilket gør det meget sværere for nogen at spore Bitcoins, men ikke umuligt. Efterhånden som teknologien skrider frem, og virksomheder, der specialiserer sig i at spore Bitcoin-transaktioner, bliver mere udbredte, vil en gang stærkt slørede transaktioner blive relativt let sporbare: 

  * [ Lovhåndhævelse fortsætter med at investere i Bitcoin-sporingstjenester ](https://news.bitcoin.com/law-enforcement-continues-invest-bitcoin-tracking-services/)
  * [ Time.com: Bitcoins er nemmere at spore, end du tror ](http://time.com/3689359/bitcoins-track-anonymous/)
  * [ Elliptic: En virksomhed med speciale i at spore Bitcoin til retshåndhævelse ](https://www.elliptic.co/)

En Google-søgning vil afsløre snesevis af artikler som dem ovenfor. Og husk, enhver transaktion, der fandt sted på et hvilket som helst tidspunkt i fortiden, er på blockchain og har potentiale til at blive sporet, selvom en blandingstjeneste blev brugt. Faktisk vil brugen af en blandingstjeneste sandsynligvis henlede opmærksomheden på disse transaktioner. 

Ikke alle Bitcoins er lige og har samme værdi. Nogle Bitcoins er blevet sortlistet og blokeret af flere enheder, hvilket gør disse mønter mindre værdifulde end resten. Hvis du modtager Bitcoins, der tidligere blev brugt til ulovlige formål, så kunne dine Bitcoins blive sortlistet, selvom du ikke havde noget at gøre med den ulovlige aktivitet. Eller for eksempel, en regering, en arbejdsgiver eller en anden enhed beslutter at blackliste dine Bitcoins i fremtiden, ligesom de gør med indefrysning eller konfiskation af aktiver. Der ville ikke være noget, du kunne gøre. Da en mixer kun gør det sværere at spore dine Bitcoins, er denne kategori blevet markeret som "ikke fungibel". 

  * Andreas Antonopoulos, en tidligere Bitcoin Core-udvikler, som er velrespekteret i Bitcoin og andre kryptovaluta-samfund, anerkender Bitcoin-fungibilitetsproblemet i en [ YouTube-video](https://www.youtube.com/watch?v=ak1iojpiHpM&feature=youtu .be&t=33m9s). 
  * Diskussion af Bitcoin-fungibilitetsproblemet på [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=1190707.0)

## Oversigt

Efter vores mening er Monero det klare valg, hvis du leder efter en privat, sikker, usporbar, ombyttelig, decentraliseret kryptovaluta uden krav om pålidelig opsætning. Alt andet sætter dit privatliv og sikkerhed i fare. Men tag ikke kun vores mening. Lav din egen research og se selv. Overvej, at Monero er godkendt og brugt af enheder, der er afhængige af privatliv og usporbarhed, såsom: 

  * [ SIGAINT ](https://www.reddit.com/r/Monero/comments/4xqrzd/sigaint_launches_tor_monero_node_as_its_operators/)
  * [ Purisme ](https://puri.sm/posts/purism-collaborates-with-cryptocurrency-monero-to-enable-mobile-payments/)
  * [ Wikileaks ](https://shop.wikileaks.org/donate#db9)
  * AlphaBay Market (AB) blev lukket i juli 2017. [ Federal Forfeiture Complaint ](https://assets.documentcloud.org/documents/3898109/AlphaBay-Cazes-Forfeiture-Complaint.pdf) mod AB viser, at: 
    * **Monero er den eneste private og usporbare kryptovaluta:**   
"I alt overtog CAZES' tegnebøger og computeragenter kontrollen over cirka $8.800.000 i Bitcoin, Ethereum, Moreno [sic] og Zcash, fordelt som følger: 1.605.0503851 Bitcoin, 8.309.271639 Ethereum, _ancash, 3.691 og ukendt. mængde Monero._ " (nederst på s. 20 og øverst på s. 21, fremhævelse tilføjet) 
    * **Bitcoin-transaktioner er ikke private og kan spores:**   
"Federale agenter opnåede warrants efter sporing af en række Bitcoin-transaktioner, der stammer fra AlphaBay, til digitale valutakonti og i sidste ende bankkonti og andre materielle aktiver, som er indeholdt af CAZES og hans kone." (s. 17, linje 24-26) 

  * **Monero er den eneste private og usporbare kryptovaluta:**   
"I alt overtog CAZES' tegnebøger og computeragenter kontrollen over cirka $8.800.000 i Bitcoin, Ethereum, Moreno [sic] og Zcash, fordelt som følger: 1.605.0503851 Bitcoin, 8.309.271639 Ethereum, _ancash, 3.691 og ukendt. mængde Monero._ " (nederst på s. 20 og øverst på s. 21, fremhævelse tilføjet) 
  * **Bitcoin-transaktioner er ikke private og kan spores:**   
"Federale agenter opnåede warrants efter sporing af en række Bitcoin-transaktioner, der stammer fra AlphaBay, til digitale valutakonti og i sidste ende bankkonti og andre materielle aktiver, som er indeholdt af CAZES og hans kone." (s. 17, linje 24-26) 

LocalMonero går ikke ind for eller opfordrer til ulovlig aktivitet. 

Yderligere læsning

  * [Hvordan Monero unikt aktiverer cirkulær økonomier](/knowledge/monero-circular-economies/)

  * [Monero's ring signaturer vs CoinJoin som i Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Hvorfor (og hvordan!) skal du holde dine egne nøgler](/knowledge/hold-your-keys/)

  * [Bidrager tilbage til Monero](/knowledge/contributing-to-monero/)

  * [Hvordan fjern noder påvirker Monero's privatliv](/knowledge/remote-nodes-privacy/)

  * [Hvordan Monero bruger hard-forks til at opgradere den netværk](/knowledge/network-upgrades/)

  * [Se tags: Hvordan en byte vil reducere Monero wallet-synkroniseringstider med 40 %+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool og Dets rolle i Decentralisering Monero Minedrift](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Hvad Det Vil Gør for Monero](/knowledge/seraphis-for-monero/)

  * [Er konvertering af Bitcoin til Monero lige så privat som at købe Monero direkte?](/knowledge/most-private-way-to-buy-monero/)

  * [Hvorfor Monero Brug en Tillidsløs Opsætning i modsætning til Zcash](/knowledge/monero-trustless-setup/)

  * [Hvorfor Monero er en bedre butik af værdi end Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Hvordan Monero Kan Overvinde Bitcoin's Netværk Effekter](/knowledge/network-effect/)

  * [Hvorfor Monero Har Det Mest Kritiske Tænkning Fællesskab](/knowledge/critical-thinking/)

  * [Svindel til Se Ud for Når Bruger Monero](/knowledge/monero-scams/)

  * [Hvordan Atomic Swaps Vil Arbejde i Monero](/knowledge/monero-atomic-swaps/)

  * [Hvad enhver Monero-bruger har brug for at vide, når det kommer til netværk](/knowledge/monero-networking/)

  * [Hvordan RingCT Huder Monero Transaktion Beløb](/knowledge/monero-ringct/)

  * [Hvordan Monero Stealth Adresser Beskyt Din Identitet](/knowledge/monero-stealth-addresses/)

  * [Hvordan Monero Underadresser Forebyg Identitet Linking](/knowledge/monero-subaddresses/)

  * [Monero Outputs Forklaret](/knowledge/monero-outputs/)

  * [Monero Bedste Praksis for Begyndere](/knowledge/monero-best-practices/)

  * [Hvordan Ring Signaturer Obskure Monero's Outputs](/knowledge/ring-signatures/)

  * [Hvordan Monero løste blokstørrelsesproblemet, der plager Bitcoin](/knowledge/dynamic-block-size/)

  * [Hvordan CLSAG Vilje Forbedre Monero's Effektivitet](/knowledge/what-is-clsag/)

  * [Hvorfor Monero Har en Hale Emission](/knowledge/monero-tail-emission/)

  * [En kort historie om Monero](/knowledge/monero-history/)

  * [Wired Magazine er Forkert Om Monero, Her er Hvorfor](/knowledge/wired-article-debunked/)

  * [Top 15 Monero Myter og Bekymringer Afkræftet](/knowledge/monero-myths-debunked/)

  * [Hvordan Dandelion++ Holder Monero's Transaktion Oprindelse Privat](/knowledge/monero-dandelion/)

  * [Hvorfor Monero Er Open Source Og Decentraliseret](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Hvad Gør RandomX så Speciel](/knowledge/monero-mining-randomx/)