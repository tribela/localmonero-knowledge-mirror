---
title: "Kako oddaljena vozlišča vplivajo na zasebnost Monera"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Ena največjih prednosti Monera v primerjavi z drugimi kriptovalutami je on-chain zasebnost, vendar ali ste se kdaj vprašali, kako je z zasebnostjo Monera, če uporabljate oddaljeno vozlišče? Kaj pa če uporabljate strežnik "lahke denarnice", kot je MyMonero?

V tej objavi se bomo poglobili v nekatere podrobnosti o tem, kako Monero zagotavlja izjemno on-chain zasebnost tudi pri uporabi oddaljenega vozlišča, in tudi na kaj moramo biti pozorni pri uporabi oddaljenih vozlišč.

## Kakšno funkcijo opravljajo vozlišča (nodes) v Monero?

Za tiste, ki niso tako dobro seznanjeni z delovanjem Monera, lahko vozlišča (ali strežnike) v omrežju Monero upravlja kdor koli in lastniku vozlišča - ali drugim, ki se odločijo, da ga bodo delili z njim! - sinhronizirati kopijo blockchaina in to kopijo posredovati drugim v omrežju. Ta vozlišča tudi preverjajo vse transakcije, ki se izvajajo v omrežju, in vse objavljene bloke ter zagotavljajo, da vsi sledijo pravilom, določenim s konsenzom.

Druga funkcija vozlišč v Moneru je zagotavljanje vseh podatkov, ki jih vaša priljubljena Monero denarnica potrebuje za pravilno preverjanje transakcij, ki vam pripadajo in izvajanje novih transakcij. Te podatke vozlišča zagotavljajo na dva načina: 

  * Podatke iz vsakega bloka v blockchainu zahteva denarnica, pregleda jih za transakcije, ki pripadajo vam in jih nato zavrže, ko jih preveri denarnica. 
    * Ta korak bo kmalu drastično izboljšan zahvaljujoč [oglednim oznakam](/knowledge/view-tags-reduce-monero-sync-time).
  * Pri pošiljanju transakcij vozlišče, ki ga uporabljate, ponudi seznam možnih vab (ali lažnih vnosov), ki jih lahko uporabite pri ustvarjanju transakcije, kar zagotavlja, da imate dobro množico, v katero se lahko skrijete vsakič, ko porabite Monero. 
    * Te vabe so del [Ring podpisov](/knowledge/ring-signatures), pomembnega dela Monerovega pristopa k on-chain zasebnosti.

## Kateri je najbolj zaseben in varen način uporabe Monera?

Najboljša stvar, ki jo lahko naredite, je kljub močni zasebnosti v verigi, ki jo zagotavlja Monero pri uporabi oddaljenih vozlišč, zagnati lastno vozlišče Monero, da zagotovite, da imate pri roki nedotaknjeno kopijo verige blokov Monero in da vaš naslov IP je dobro zaščiten. Druga prednost pri izvajanju lastnega vozlišča je, da lahko prispevate nazaj v omrežje, tako da drugim vozliščem omogočite sinhronizacijo iz vašega vozlišča ali celo dovolite drugim uporabnikom, da se povežejo z vašim vozliščem s svojimi denarnicami.

Kot rečeno, Monero še vedno zagotavlja odlično zasebnost pri uporabi oddaljenega vozlišča. Če vas zanima vodenje lastnega vozlišča Monero, je tukaj preprost vodnik za to: 

  * [Zaženite vozlišče Monero](https://sethforprivacy.com/guides/run-a-monero-node/)

## Kaj lahko oddaljeno vozlišče (node) izve o meni?

Pri uporabi oddaljenega vozlišča je nekaj ključnih informacij, ki so izpostavljene oddaljenemu vozlišču, in nekaj ključnih načinov, kako vas lahko vozlišče napade, prepreči transakcijo in drugo.

Prva stvar, ki jo lahko oddaljeno vozlišče izve o vas, je vaš javni naslov IP. Čeprav bo to, upajmo, prikrito prek VPN ali Tor, bi lahko oddaljeno vozlišče vaš javni naslov IP povezalo s transakcijo, kar bi jim pomagalo zožiti, od koder opravljate transakcije. Oddaljeno vozlišče se lahko nauči tudi zadnjega bloka, ki je bil sinhroniziran z vašo denarnico, in to uporabi, da poskusi in utemeljeno ugiba o vas, na primer, kdaj običajno uporabljate Monero in kdaj ste nazadnje porabili Monero. To še posebej velja, če vedno prihajate z istega naslova IP (kot je vaš dom). Zadnja ključna stvar, ki jo lahko oddaljeno vozlišče izve o vas, so osnovne informacije o transakcijah, ki jih pošiljate prek njega. Čeprav so to morda najočitnejši podatki, ki jih operater oddaljenega vozlišča dobi o vas, je pomembno razumeti, da bi jih lahko uporabili za pomoč pri izsleditvi pošiljatelja transakcije pri združevanju teh informacij z drugimi podatki izven verige. To je lahko še posebej nevarno, če oddaljeno vozlišče upravlja zlonamerna entiteta, podjetje za analizo verige blokov ali represivna nacionalna država.

Oddaljeno vozlišče vam lahko tudi poskuša povzročiti težave tako, da pred vami skrije bloke, zaradi česar vaša denarnica misli, da je sinhronizirana, čeprav ni bila. Zaradi tega lahko mislite, da so sredstva izgubljena, ali vam prepreči porabo sredstev, dokler se ne povežete z drugim vozliščem. Zadnja ključna stvar, ki jo lahko naredi oddaljeno vozlišče, je, da vašo denarnico napolni z manipuliranim seznamom vab. To lahko povzroči, da vaša denarnica popolnoma ne uspe zgraditi transakcij (zaradi česar ne morete porabiti sredstev) ali pa lahko oddaljenemu vozlišču omogoči, da poskusi zagotoviti vabe, za katere ve, da so porabljene, da zmanjša anonimnost, ki ste jo deležni pri vsaki transakciji.

## Kakšna jamstva za zasebnost še obstajajo pri uporabi oddaljenega vozlišča?

Čeprav vas je ta članek morda nekoliko prestrašil, se je pomembno zavedati, da je zasebnost, ki jo zagotavlja Monero, odlična tudi pri uporabi oddaljenega vozlišča in daleč presega katero koli drugo kriptovaluto, če se uporablja na ta način. Še vedno pridobite močno zasebnost v verigi, ki jo zagotavlja Monero, saj oddaljeno vozlišče nikoli ne ve pravega vnosa (katere kovance porabite), zneska Monera, porabljenega v transakciji, ali naslova prejemnika transakcije. Zunanji opazovalci prav tako ne morejo videti pravega vnosa, zneska ali vključenih naslovov (ne glede na vrsto vozlišča, ki ga izberete!), kar zagotavlja, da imajo zunaj oddaljenega vozlišča celo vaš naslov IP, informacije o sinhronizaciji denarnice in transakcije močno zagotovljeno zasebnost 

Oddaljeno vozlišče tudi nikoli nima dostopa do prejšnjih transakcij, ki ste jih poslali ali prejeli, ali količine Monera, ki je trenutno v vaši denarnici, in izgubi vso vidljivost v vaših transakcijah v trenutku, ko začnete uporabljati drugo vozlišče. Oddaljenemu vozlišču nikoli niso posredovani nobeni zasebni ključi (bodisi ključi za porabo ali ogled), tako da vaša denarnica ostane zasebna, varna in uporabna. Ne glede na oddaljeno vozlišče prav tako nikoli niste v nevarnosti, da bi Monero izgubili ali vam ga ukradli, saj vozlišče ne more urejati naslova prejemnika, nikoli nima dostopa do zasebnih ključev vaših denarnic in vam na noben način ne more zapleniti vašega Monera.

## Kaj pa "lahke denarnice", kot je MyMonero?

Čeprav je tema nekoliko zunaj obsega tega članka, sem želel obravnavati edinstveno vrsto denarnice v Monero – lahke denarnice. Ime lahka denarnica izhaja iz dejstva, da vaši denarnici (v telefonu ali računalniku) ni treba izvajati nobene sinhronizacije verige blokov, zaradi česar je izkušnja hitrejša in bolj tekoča.

Vendar imajo denarnice, kot je ta, zaenkrat velik kompromis glede zasebnosti – vaša denarnica pošlje ključ zasebnega pogleda na oddaljeni strežnik, ki ga uporabljate (kot je privzeto v MyMonero), kar daje oddaljenemu strežniku popoln vpogled v vsa prejeta sredstva od izdelave vaše denarnice (in dokler ne prenehate uporabljati te denarnice ali semena). To drastično zmanjša zasebnost, ki jo prejmete od operaterja vozlišča, in k temu pristopite previdno.

K sreči si skupnost Monero prizadeva izboljšati programsko opremo, ki jo lahko uporabite za gostovanje lastnega strežnika lahke denarnice (LWS), kar vam bo omogočilo hitro sinhronizacijo, ne da bi tretji osebi zaupali svoje zasebne ključe za ogled – ko bo zagnal programsko opremo, kamor vaša denarnica pošlje zasebne ključe za ogled!

Za več informacij o strežniku lahke denarnice po meri glejte spodnji repozitorij Github: 

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Kako lahko izvem več?

Če ste radovedni in bi radi bolje razumeli vozlišča v Monero ter razmislili o uporabi oddaljenega vozlišča ali izvajanju lastnega, si oglejte spodnje povezave za odlična mesta za začetek:

  * [Monero World, seznam oddaljenih vozlišč, ki jih vodi skupnost, se lahko uporablja](https://moneroworld.com/#nodes)
  * [Vozlišča Monero, ki jih vodi Seth For Privacy, avtor tega članka](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, seznam oddaljenih vozlišč s pogosto preverjanim stanjem< /a>](https://monero.fail/)
  * [Kako vzpostaviti povezavo na oddaljeno vozlišče v denarnici GUI](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia – oddaljeno Vozlišče](https://www.getmonero.org/resources/moneropedia/remote-node.html)

Nadaljnje branje

  * [Kako Monero edinstveno omogoča krožna gospodarstva](/knowledge/monero-circular-economies/)

  * [Obročni ring podpisi Monero vs CoinJoin kot v Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Zakaj (in kako!) bi morali imeti svoje ključe](/knowledge/hold-your-keys/)

  * [Prispevek nazaj v Monero](/knowledge/contributing-to-monero/)

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

  * [Zakaj je Monero Boljši od Dash, Zcash, Zcoin (tudi z Lelantusom), Grin in Bitcoin Mikserji, kot je Wasabi (posodobljeno maja 2020)](/knowledge/why-monero-is-better/)