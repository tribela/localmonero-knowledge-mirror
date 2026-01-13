---
title: "Zakaj je Monero Boljši od Dash, Zcash, Zcoin (tudi z Lelantusom), Grin in Bitcoin Mikserji, kot je Wasabi (posodobljeno maja 2020)"
slug: "why-monero-is-better"
date: "2024-01-01"
image: "/images/why-monero.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Vsi kovanci, osredotočeni na zasebnost, ne morejo zagotoviti 100% zasebnosti, nesledljivosti, varnosti in zamenljivosti v 100-odstotno decentraliziranem kovancu z nastavitvijo brez zaupanja. Kaj so ti atributi in zakaj so pomembni:

## Analiza kovancev

Tukaj je analiza znanih kriptovalut, ki kot svojo ključno razlikovalno lastnost navajajo anonimnost in/ali neizsledljivost. Bitcoin sam ne spada v okvir te analize, saj nikoli ni trdil, da je anonimen.

To spletno mesto so ustvarili uporabniki Monera. Včasih nismo bili uporabniki Monera, a nas je skrbelo za finančno zasebnost. Raziskovali smo kovance, ki so trdili, da so zasebni, in ta stran je rezultat naše raziskave. To je razlog, zakaj smo se odločili za Monero v primerjavi z ostalimi. Če se torej zdi, da smo pristranski, smo, vendar menimo, da ta pristranskost temelji na dejstvih, ki jih lahko preberete spodaj in se tako prepričate sami.

### Pregled

Izberite logotip, da skočite na analizo tega kovanca.

### Monero

Monero je že od samega začetka 100% odprtokoden - kar pomeni, da si lahko kdorkoli ogleda [ izvorno kodo ](https://github.com/monero-project/bitmonero) programske opreme, da preveri, da ne obstajajo stranska vrata in ali je programska oprema varna.

Monero ima tudi [ strokovno pregledane raziskovalne dokumente ](https://lab.getmonero.org/), ki matematično in sistematično preverjajo vse zgoraj navedene lastnosti.

### DASH

DASH ima [ "rich list" ](https://bitinfocharts.com/top-100-richest-darkcoin-addresses.html), zato to ni zasebni kovanec. Finančne podrobnosti naslovov kovancev so vidne vsem, ki pregledujejo verigo blokov.

> DASH sploh ni kriptografsko zaseben. Pravzaprav sem imel diapozitiv, ki je dejal "DASH, LOL," in nič drugega ... to je kačje olje in osebno sem glede tega nekako iz sebe. 
> 
> **Gregory Maxwell** , razvijalec in kriptograf Bitcoin Core, v [ predstavitvi za Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

DASH sploh ni kriptografsko zaseben. Pravzaprav sem imel diapozitiv, ki je dejal "DASH, LOL," in nič drugega ... to je kačje olje in osebno sem glede tega nekako iz sebe. 

**Gregory Maxwell** , razvijalec in kriptograf Bitcoin Core, v [ predstavitvi za Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

**Peter Todd** , še en razvijalec in kriptograf Bitcoin Core, je podal [ podobno izjavo](https://twitter.com/petertoddbtc/status/622022840330682368).

### Zcash

Transakcije Zcash so vidne v blockchainu. Resda omogočajo skrite transakcije, vendar je [ manj kot 1 % transakcij popolnoma zaščitenih ](http://stat.bloxy.info/superset/dashboard/zcash/). Ker skrite transakcije niso obvezne in niso privzete (da ne omenjamo, da se redko uporabljajo), skrite transakcije [ izstopajo v njihovi verigi blokov ](http://weuse.cash/2016/06/09/btc-xmr-zcash/) in pritegnejo pozornost nase.

> In mimogrede, mislim, da lahko Zcash uspešno naredimo preveč sledljivega za kriminalce, kot je WannaCry, a še vedno popolnoma zasebnega & zamenljivega. 
> 
> **Zooko Wilcox** , izvršna direktorica Zcash, v tvitu [ ](https://twitter.com/zooko/status/863202798883577856)

In mimogrede, mislim, da lahko Zcash uspešno naredimo preveč sledljivega za kriminalce, kot je WannaCry, a še vedno popolnoma zasebnega & zamenljivega. 

**Zooko Wilcox** , izvršna direktorica Zcash, v tvitu [ ](https://twitter.com/zooko/status/863202798883577856)

Če je lahko Zcash "preveč sledljiv", potem ne more biti povsem zaseben ali zamenljiv. 

Redne transakcije so transparentne. Skrite transakcije uporabljajo zk-SNARKS, ki imajo pod določenimi pogoji zanesljiva jamstva za zasebnost. Vprašanje je, ali so ti pogoji izpolnjeni, in glede na majhno število ljudi, ki uporabljajo zaščitene zmogljivosti, to ostaja vprašljivo.

Zcash je podjetje in trenutno [ prejme 20 % vseh izrudiranih ZEC kot nagrado ustanovitelju ](https://z.cash/blog/funding.html). 

Zcash je zahteval **Trusted Setup**. To pomeni, da morate zaupati, da je bil sistem postavljen pošteno. Če ne bi bilo pošteno nastavljeno, bi [ lahko ustvarili neomejene količine ZEC, ne da bi kdo vedel ](https://blog.okturtles.com/2016/03/the-zcash-catch/). S tem bi heker obogatel in razvrednotil ZEC. Ni mogoče vedeti, ali je bila Trusted Setup izvedena pošteno. Moramo jim verjeti na besedo. To v sistem vnese človeško točko napake, ki je v nasprotju s skoraj vsako drugo kriptovaluto. Zaupati bi morali samo matematiki in preverljivi izvorni kodi kriptovalut, ne pa ljudem. Kot smo videli pri skoraj vseh velikih programskih podjetjih, kot so [ Microsoft](https://www.gnu.org/proprietary/proprietary-back-doors.en.html), [Apple](http://www.digitaltrends.com/computing/apple-vs-fbi-backdoor-to-data-already-exists/), in celo vladah, jim ne bi smeli zaupati. 

Peter Todd, razvijalec Bitcoin Core, ki je [ sodeloval ](https://github.com/zcash/mpc/blob/master/README.md) pri Zcash Trusted Setup, je to poimenoval " [ stranska vrata](https://twitter.com/petertoddbtc/status/793584540891643906) ". 

> Zcash ni brezpogojno zdrav, ne more biti s trenutno tehnologijo... zahteva zaupanja vredno nastavitev … bo moral ponoviti postopek [Trusted Setup] za nadgradnjo kriptovalute čez čas, tako da je ranljivost. 
> 
> Gregory Maxwell, razvijalec in kriptograf Bitcoin Core, v [ predstavitvi za Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

Zcash ni brezpogojno zdrav, ne more biti s trenutno tehnologijo... zahteva zaupanja vredno nastavitev … bo moral ponoviti postopek [Trusted Setup] za nadgradnjo kriptovalute čez čas, tako da je ranljivost. 

Gregory Maxwell, razvijalec in kriptograf Bitcoin Core, v [ predstavitvi za Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

### Zcoin

**Opomba:** Zcoin prehaja s svoje trenutne sheme Sigma na nov protokol, ki temelji na njegovem novem delu, Lelantus. Lelantus bo implementiran po stopnjah, ta članek bo predvideval, da so vse faze dokončane in implementirane za ustrezne primerjave skupaj s predvidenimi časi implementacije.

Razlog, da je Zcoin dobil to razkošje, da ga ocenjujejo na podlagi njegovega prihodnjega protokola in ne Zcasha, je ta, da ima Zcoin načrt s splošnimi časovnimi razporedi za aktivacijo, medtem ko so Zcashovi načrti 'privzete zasebnosti' nejasni in ostajajo nejasni.

Zcoin (XZC) ne bo imel seznama bogatih, zato bo zaseben. Privzeto obvezna zasebnost naj bi zaživela leta 2021. Ko bo uvedena, obogatenega seznama ne bo mogoče ustvariti (čeprav ga trenutno [imajo ](https://www.coinexplorer.net/XZC/richlist)).

### Grin

### Bitcoin Mixers

Vse transakcije z bitcoini so vidne v blockchainu in obstaja [ Bitcoin rich list ](http://www.bitcoinrichlist.com/top100), tako da Bitcoin ni zaseben. Bitcoin je [ psevdononimen ](https://bitcoin.org/en/you-need-to-know), ne pa anonimen. 

Za **Mešalnikom Bitcoinov** morate zaupati, da lahko varujejo svoje podatke in niso v lasti vlade, hekerjev ali drugih subjektov ali sodelujejo z njimi. 

Julija 2017 je ustanovitelj največje storitve za mešanje Bitcoinov, BITMIXER.IO, objavil, da se zapirajo, in to navedel kot razlog: 

> … Zdaj sem ugotovil, da je Bitcoin transparenten neanonimni sistem **po zasnovi**. Blockchain je odlična odprta knjiga … 
> 
> BITMIXER.IO, v obvestilu o zaprtju na [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (poudarek v izvirniku). 

… Zdaj sem ugotovil, da je Bitcoin transparenten neanonimni sistem **po zasnovi**. Blockchain je odlična odprta knjiga … 

BITMIXER.IO, v obvestilu o zaprtju na [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (poudarek v izvirniku). 

Nekaj tednov pozneje je po preučitvi različnih kovancev, osredotočenih na zasebnost, rekel tole: 

> Po temeljiti preiskavi potrjujem, da je MONERO najboljša valuta za zasebnost. Zato toplo priporočam MONERO vsem ljudem, ki potrebujejo dodatno zasebnost. 
> 
> BITMIXER.IO, v [ nadaljnji objavi ](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Po temeljiti preiskavi potrjujem, da je MONERO najboljša valuta za zasebnost. Zato toplo priporočam MONERO vsem ljudem, ki potrebujejo dodatno zasebnost. 

BITMIXER.IO, v [ nadaljnji objavi ](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Ker so vse Bitcoin transakcije vidne v blockchainu, je VSEM Bitcoin transakcijam mogoče slediti. Mešalnik Bitcoinov lahko zelo zamegli transakcije, zaradi česar je nekdo veliko težje izslediti Bitcoine, vendar ni nemogoče. Ko tehnologija napreduje in podjetja, specializirana za sledenje transakcij Bitcoinov, postajajo vse bolj razširjena, bodo nekoč zelo prikrite transakcije postale razmeroma lahko sledljive: 

  * [ Organi pregona še naprej vlagajo v storitve sledenja Bitcoinom ](https://news.bitcoin.com/law-enforcement-continues-invest-bitcoin-tracking-services/)
  * [ Time.com: Bitcoinom je lažje slediti, kot si mislite ](http://time.com/3689359/bitcoins-track-anonymous/)
  * [ Elliptic: podjetje, specializirano za sledenje Bitcoinom za organe pregona ](https://www.elliptic.co/)

Iskanje v Googlu bo razkrilo na desetine člankov, podobnih zgornjim. In ne pozabite, da je vsaka transakcija, ki se je zgodila kadar koli v preteklosti zapisana v verigi blokov in jo je mogoče izslediti, tudi če je bila uporabljena storitev mešanja. Pravzaprav bo uporaba storitve mešanja verjetno pritegnila pozornost na te transakcije. 

Vsi Bitcoini niso enaki in nimajo enake vrednosti. Nekatere Bitcoine je več subjektov uvrstilo na črno listo in jih blokiralo, zaradi česar so ti kovanci manj vredni od ostalih. Če prejmete Bitcoine, ki so bili v preteklosti uporabljeni v nezakonite namene, so lahko vaši bitcoini uvrščeni na črni seznam, čeprav niste imeli nič opraviti z nezakonito dejavnostjo. Ali pa se recimo vlada, delodajalec ali kakšen drug subjekt odloči, da bo vaše bitcoine v prihodnosti uvrstil na črni seznam, podobno kot storijo z zamrznitvijo ali zaplembo sredstev. Ničesar ne bi mogli narediti. Ker mešalnik le oteži sledenje vašim Bitcoinom, je bila ta kategorija označena kot "ni zamenljiva." 

  * Andreas Antonopoulos, nekdanji razvijalec Bitcoin Core, ki je zelo cenjen v skupnosti bitcoinov in drugih kriptovalut, priznava problem zamenljivosti bitcoinov v [ videoposnetek YouTube](https://www.youtube.com/watch?v=ak1iojpiHpM&feature=youtu .be&t=33m9s). 
  * Razprava o problemu zamenljivosti bitcoinov na [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=1190707.0)

## Povzetek

Po našem mnenju je Monero jasna izbira, če iščete zasebno, varno, neizsledljivo, zamenljivo, decentralizirano kriptovaluto, ki ne zahteva zaupanja vredne nastavitve. Vse drugo ogroža vašo zasebnost in varnost. Vendar ne upoštevajte le našega mnenja. Naredite lastno raziskavo in se prepričajte sami. Upoštevajte, da Monero podpirajo in uporabljajo subjekti, ki so odvisni od zasebnosti in nesledljivosti, kot so: 

  * [ SIGAINT ](https://www.reddit.com/r/Monero/comments/4xqrzd/sigaint_launches_tor_monero_node_as_its_operators/)
  * [ Purism ](https://puri.sm/posts/purism-collaborates-with-cryptocurrency-monero-to-enable-mobile-payments/)
  * [ Wikileaks ](https://shop.wikileaks.org/donate#db9)
  * AlphaBay Market (AB) je bil zaprt julija 2017. [ Zvezna pritožba glede zaplembe ](https://assets.documentcloud.org/documents/3898109/AlphaBay-Cazes-Forfeiture-Complaint.pdf) proti AB kaže, da: 
    * **Monero je edina zasebna in neizsledljiva kriptovaluta:**   
"Iz denarnic in računalniških agentov CAZES so skupaj prevzeli nadzor nad približno 8.800.000 $ v Bitcoinih, Ethereumu, Morenu [sic] in Zcashu, razdeljenih na naslednji način: 1.605,0503851 Bitcoin, 8.309,271639 Ethereum, 3.691,98 Zcash, _in neznana količina Monera._ " (dno str. 20 in vrh str. 21, poudarek dodan) 
    * **Bitcoin transakcije niso zasebne in jih je mogoče izslediti:**   
"Zvezni agenti so pridobili naloge, potem ko so sledili številnim transakcijam z bitcoini, ki izvirajo iz AlphaBaya, do računov v digitalni valuti in nazadnje do bančnih računov in drugih opredmetenih sredstev, ki jih imata CAZES in njegova žena." (str. 17, vrstice 24- 26) 

  * **Monero je edina zasebna in neizsledljiva kriptovaluta:**   
"Iz denarnic in računalniških agentov CAZES so skupaj prevzeli nadzor nad približno 8.800.000 $ v Bitcoinih, Ethereumu, Morenu [sic] in Zcashu, razdeljenih na naslednji način: 1.605,0503851 Bitcoin, 8.309,271639 Ethereum, 3.691,98 Zcash, _in neznana količina Monera._ " (dno str. 20 in vrh str. 21, poudarek dodan) 
  * **Bitcoin transakcije niso zasebne in jih je mogoče izslediti:**   
"Zvezni agenti so pridobili naloge, potem ko so sledili številnim transakcijam z bitcoini, ki izvirajo iz AlphaBaya, do računov v digitalni valuti in nazadnje do bančnih računov in drugih opredmetenih sredstev, ki jih imata CAZES in njegova žena." (str. 17, vrstice 24- 26) 

LocalMonero ne zagovarja ali spodbuja nezakonite dejavnosti. 

Nadaljnje branje

  * [Kako Monero edinstveno omogoča krožna gospodarstva](/knowledge/monero-circular-economies/)

  * [Obročni ring podpisi Monero vs CoinJoin kot v Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Zakaj (in kako!) bi morali imeti svoje ključe](/knowledge/hold-your-keys/)

  * [Prispevek nazaj v Monero](/knowledge/contributing-to-monero/)

  * [Kako oddaljena vozlišča vplivajo na zasebnost Monera](/knowledge/remote-nodes-privacy/)

  * [Kako Monero uporablja hard-forke za nadgradnjo omrežja](/knowledge/network-upgrades/)

  * [Ogled oznak: Kako bo en bajt skrajšal čas sinhronizacije Monero denarnice za 40%+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool in Njegova Vloga pri Decentralizaciji Monero Rudarjenja](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Kaj bo Naredil za Monero](/knowledge/seraphis-for-monero/)

  * [Ali je Pretvorba Bitcoina v Monero Enako Zasebna kot Neposredni Nakup Monera?](/knowledge/most-private-way-to-buy-monero/)

  * [Zakaj Monero Uporablja Nezaupljivo nNastavitev za Razliko od Zcasha](/knowledge/monero-trustless-setup/)

  * [Zakaj je Monero Boljši Hranilnik Vrednosti kot Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Kako lahko Monero premaga omrežne učinke Bitcoina](/knowledge/network-effect/)

  * [Zakaj ima Monero Najbolj Kritično Mislečo Skupnost](/knowledge/critical-thinking/)

  * [Prevare, na Katere Morate Biti Pozorni pri Uporabi Monera](/knowledge/monero-scams/)

  * [Kako Bodo Atomske Menjave v Monero Delovale](/knowledge/monero-atomic-swaps/)

  * [Kaj Mora Vsak Uporabnik Monera Vedeti, ko Gre za Mreženje](/knowledge/monero-networking/)

  * [Kako RingCT Prikrije Zneske Monero Transakcij](/knowledge/monero-ringct/)

  * [Kako Naslovi Monero Stealth Ščitijo Vašo Identiteto](/knowledge/monero-stealth-addresses/)

  * [Kako Monero Podnaslovi Preprečujejo Povezovanje Identitet](/knowledge/monero-subaddresses/)

  * [Pojasnjeni Monero Izhodi (Outputs)](/knowledge/monero-outputs/)

  * [Najboljše Monero Prakse za Začetnike](/knowledge/monero-best-practices/)

  * [Kako Obročni Podpisi Prikrijejo Izhode Monera](/knowledge/ring-signatures/)

  * [Kako je Monero Rešil Problem Velikosti Bloka, ki muči Bitcoin](/knowledge/dynamic-block-size/)

  * [Kako bo CLSAG Izboljšal Učinkovitost Monera](/knowledge/what-is-clsag/)

  * [Zakaj Ima Monero Tail Emisijo](/knowledge/monero-tail-emission/)

  * [Kratka zgodovina Monera](/knowledge/monero-history/)

  * [Wired Magazine se Moti Glede Monera. Evo, Zakaj](/knowledge/wired-article-debunked/)

  * [Razbijamo 15 glavnih mitov in pomislekov o Monero](/knowledge/monero-myths-debunked/)

  * [Kako Dandelion++ Ohranja Zasebnost Izvora Transakcije Monero](/knowledge/monero-dandelion/)

  * [Zakaj je Monero Odprtokoden in Decentraliziran](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero rudarjenje: zakaj je RandomX tako poseben](/knowledge/monero-mining-randomx/)