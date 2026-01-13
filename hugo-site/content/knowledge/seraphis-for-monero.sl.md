---
title: "Seraphis: Kaj bo Naredil za Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: nadgradnja modularne zasnove za Monero transakcije

## Seraphis: nadgradnja modularne zasnove za Monero transakcije

Ta objava opisuje [Seraphis](https://github.com/UkoeHB/Seraphis), niz struktur transakcijskega protokola in abstrakcij, ki jih je razvil psevdonimni raziskovalec [`koe`](https://github.com/UkoeHB) za ekosistem Monero, in s stalno varnostno analizo avtor psevdonimnega sodelavca [`coinstudent2048`](https://github.com/coinstudent2048).  
Naredili smo nekaj poenostavitev in zaradi jasnosti izpustili nekatere tehnične podrobnosti; iz tega razloga in ker načrtovanje Seraphisa še vedno poteka, naj se zainteresirani bralci obrnejo na dokumentacijo Seraphis za najnovejše informacije.

## Transakcije v Moneru

## Transakcije v Moneru

Protokoli, kot sta Bitcoin in Monero ter drugi, temeljijo na tako imenovanem "izhodnem modelu" delovanja, kjer je _izhod_ predstavitev vrednosti, ki jo je mogoče prenesti.  
Transakcije porabijo enega ali več izhodov, ki jih nadzoruje pošiljatelj, in ustvarijo nove izhode, usmerjene proti prejemnikom (ali nazaj k pošiljatelju kot sprememba); transakcija mora biti uravnotežena tako, da morajo porabljeni izhodi vsebovati skupno vrednost, ki je natančno enaka vrednosti v novih izhodih (plus pristojbina, ki jo naloži omrežje).  
V mnogih protokolih, kot je Bitcoin, je vrednost, vsebovana v izhodu, zapisana v praznem jeziku, prav tako kot prejemnik.  
Poleg tega je s pogledom na verigo blokov nepomembno videti, ali in kdaj je bil izhod porabljen (to je, ali je bil porabljen v kasnejši transakciji in katera transakcija ga je porabila). 

Nasprotno pa protokoli, kot je Monero, uvajajo drugačno zasnovo: 

  * Izhodne vrednosti so skrite in niso vidne v verigi blokov 
  * Naslovi prejemnikov so skriti z uporabo protokola za enkratno naslavljanje 
  * Ne glede na to, ali je bil izhod porabljen ali ne, je zakrita z uporabo dvoumnih podpisov 

Posledica tega je, da je brez zunanjih informacij težko ugotoviti, ali je bil določen rezultat porabljen, kakšna je njegova vrednost in kdo je njegov prejemnik 

Trenutni transakcijski protokol Monero se imenuje _RingCT_ in uporablja več kriptografskih gradnikov za doseganje teh načrtovnih ciljev.

  * _Obveznosti_ skrijejo zneske na matematično uporaben način 
  * _Dokazila obsega_ preprečujejo prelivanje, ki bi lahko napihnilo zalogo 
  * _Povezljivi obročni podpisi_ zagotavljajo dvoumnost podpisnika in preprečujejo poskuse dvojne porabe 
  * _Pobotanja obveznosti_ potrjujejo, da je stanje transakcij 

Ti gradniki so skrbno prepleteni za izgradnjo protokola RingCT.

Uporabna lastnost protokola RingCT je, da je mogoče nekatere gradnike spremeniti ali nadgraditi na način, ki ohrani celotno zasnovo in lastnosti nedotaknjene, vendar lahko zagotovi izboljšave učinkovitosti ali varnosti. Pravzaprav so se tovrstne nadgradnje zgodile (ali so načrtovane) večkrat v zgodovini Monera. Preizkusi obsega v prvotnem protokolu RingCT so bili zajetni in počasni; pozneje so bili posodobljeni na konstrukcijo, imenovano [Bulletproofs](https://eprint.iacr.org/2017/1066), zaradi katere so bile transakcije manjše in hitrejše z boljšo varnostno analizo, načrtovana pa je tudi posodobitev na novejšo konstrukcijo, imenovano [Bulletproofs+](https://eprint.iacr.org/2020/735), za še večjo učinkovitost. 

Podoben postopek je bil izveden z gradnikom povezljivega obročnega podpisa. V prvotnem protokolu je bila uporabljena konstrukcija, imenovana [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34). To je bilo pozneje posodobljeno na novejšo konstrukcijo, imenovano [CLSAG](https://eprint.iacr.org/2019/654), ki je hitrejša, povzroči manjše transakcije in ima boljšo varnostno analizo. Predlagana je bila še novejša konstrukcija povezljivega obročnega podpisa, ki temelji na [Triptihu](https://eprint.iacr.org/2020/018), vendar ta ni bila izbrana za uvedbo zaradi vpliva na operacije z več podpisi 

## Seraphis

## Seraphis

Seraphis s to idejo gre še korak dlje.  
Namesto posodobitve posameznih gradnikov obstoječega transakcijskega protokola RingCT uvaja drugačen protokol, ki lahko izkoristi različne gradnike in ponudi izboljšano funkcionalnost.

## Gradniki

## Gradniki

Seraphis uporablja drugačen nabor kriptografskih gradnikov za doseganje svojih načrtovalskih ciljev.

  * _Obveznosti_ še vedno skrivajo zneske
  * _Dokazila obsega_ še vedno preprečujejo prelivanje in napihovanje dovoda 
  * _Dokazila o članstvu_ zagotavljajo dvoumnost podpisnika 
  * _Poravnave obveznosti_ še vedno uveljavljajo stanje 
  * _Odobritev dokazil_ preprečuje poskuse dvojne porabe 

Opazite spremembo tukaj: povezljivi obročni podpisi so nadomeščeni s kombinacijo dokazil o članstvu in dokazil o avtorizaciji. Grobo rečeno, dokazila o članstvu kažejo, da je porabljeni izhod del večjega niza, podobno kot se zgodi v RingCT. Toda za razliko od RingCT dokazila o članstvu sploh ne vključujejo povezovalne oznake! Dokazila o avtorizaciji kažejo, da je povezovalna oznaka veljavna in se uporabljajo za podpis končne transakcije.

Ker RingCT vpeče povezovalno oznako v dvoumen podpis, so operacije podpisovanja (in večpodpisov) računsko bolj intenzivne, izgradnja drugih funkcij, povezanih z oznakami, pa postane zahtevnejša. Toda v Seraphisu je mogoče izdelavo dokazil o članstvu varno prenesti iz zelo zaupanja vrednih naprav (ki imajo lahko omejeno računalniško moč, kot je denarnica strojne opreme) na manj zaupanja vredno napravo, operacije podpisovanja (in večpodpisov) pa so veliko lažje z uporabo veliko enostavnejšega avtorizacijskega dokaza 

Na srečo nekateri gradniki, ki jih zahteva Seraphis, že obstajajo drugje in jih ni treba načrtovati iz nič. Obe konstrukciji Bulletproofs in Bulletproofs+ se lahko uporabljata kot dokazila o dosegu. Spremembe dokaznih sistemov tipa Schnorr se lahko uporabljajo za avtorizacijo dokazov. In učinkovit [sistem dokazovanja](https://eprint.iacr.org/2015/643), ki je bil že uporabljen kot osnova za Triptych, [Lelantus](https://eprint.iacr.org/2019/373) in [Spark](https://eprint.iacr.org/2021/1173)*, je mogoče spremeniti za dokaze članstva.

* Cypher Stack prejme sredstva za razvoj Spark.

## Naslavljanje

## Naslavljanje

Na žalost naslovi Monero, ki so trenutno v uporabi, niso združljivi s Seraphis. Uporabniki bi morali ustvariti nove naslove iz svojih ključev denarnice, da bi prejeli Monero, če bi bil Seraphis implementiran. Vendar ima ta strošek ekosistema številne prednosti.

Poleg zgoraj omenjenih strukturnih prednosti je zasnova Seraphis primerna za številne različne možnosti gradnje naslovov, od katerih ima vsaka svoje kompromise. Medtem ko se končna konstrukcija naslova, ki bo uporabljena v Seraphisu, [še vedno odloča ](https://github.com/monero-project/research-lab/issues/92) (ena shema, ki je deležna veliko pozornosti, se imenuje [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), lahko opišemo nekaj skupnih in uporabnih funkcij.

Morda veste, da naslovi Monero ponujajo funkcijo _oglednega ključa_ , kjer lahko napravi ali tretji osebi zagotovite ogledni ključ in ji dovolite, da v vašem imenu opazuje dohodne izhode, vendar ne da bi se odrekli porabi. oblast. To je uporabno za denarnice, ki se lahko posodabljajo, medtem ko je vaš ključ porabe varno zaklenjen. Uporaben je tudi v primerih, ko želite dostop do zunanjega pogleda, kot je javna dobrodelna ustanova, ki ponuja preglednost, ali podjetje z računovodskim oddelkom.

Slaba stran ključev za ogled Monero je, da ne zagotavljajo popolnega ali natančnega dostopa do pogleda. Ni mogoče zanesljivo zaznati, kdaj denarnica porabi sredstva, zaradi česar je težko pravilno izračunati stanja denarnice, ko ključ porabe ni na voljo. Prav tako trenutno ni mogoče zaznati dohodnih izhodov, ne da bi se naučili tudi vrednosti, ki jo vsebujejo ti izhodi (kar pomeni, da bodo vse tretje osebe, odgovorne za iskanje dohodnih izhodov, natančno izvedele, koliko Monera pridobivate).

Konstrukcije naslavljanja Seraphis lahko to rešijo. S Seraphisom je vaš naslov opremljen z različnimi tipkami, ki lahko počnejo različne stvari: 

  * Pazi na dohodne izhode, vendar skrij njihovo vrednost
  * Pazi na dohodne izhode, vendar prikaži njihovo vrednost
  * Pazi na odhodne izhode
  * Pomaga vam ustvariti transakcije, ne pa jih podpisati
  * Ustvarjanje novih naslovov (uporabno za trgovce na drobno ali izmenjave s številnimi strankami)

Kot imetnik naslova se lahko odločite, koliko pooblastil boste prenesli na druge naprave ali tretje osebe.

## Velika slika

## Velika slika

Seraphis je velika sprememba v Monero ekosistemu. Čeprav vključuje spremembe naslovov in gradnikov transakcij, njegova zasnova ponuja prilagodljivost in uporabno funkcionalnost, ki ni mogoča z današnjim protokolom RingCT. Medtem ko je velik del zasnove dokončan in se razvija v [izvedbo](https://github.com/UkoeHB/monero/tree/seraphis_lib), načrtovanje naslovov in analiza varnosti še potekata. Seraphis ponuja odlično priložnost za pospešitev ekosistema Monero! 

Nadaljnje branje

  * [Kako Monero edinstveno omogoča krožna gospodarstva](/knowledge/monero-circular-economies)/

  * [Obročni ring podpisi Monero vs CoinJoin kot v Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Zakaj (in kako!) bi morali imeti svoje ključe](/knowledge/hold-your-keys)/

  * [Prispevek nazaj v Monero](/knowledge/contributing-to-monero)/

  * [Kako oddaljena vozlišča vplivajo na zasebnost Monera](/knowledge/remote-nodes-privacy)/

  * [Kako Monero uporablja hard-forke za nadgradnjo omrežja](/knowledge/network-upgrades)/

  * [Ogled oznak: Kako bo en bajt skrajšal čas sinhronizacije Monero denarnice za 40%+](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool in Njegova Vloga pri Decentralizaciji Monero Rudarjenja](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Ali je Pretvorba Bitcoina v Monero Enako Zasebna kot Neposredni Nakup Monera?](/knowledge/most-private-way-to-buy-monero)/

  * [Zakaj Monero Uporablja Nezaupljivo nNastavitev za Razliko od Zcasha](/knowledge/monero-trustless-setup)/

  * [Zakaj je Monero Boljši Hranilnik Vrednosti kot Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Kako lahko Monero premaga omrežne učinke Bitcoina](/knowledge/network-effect)/

  * [Zakaj ima Monero Najbolj Kritično Mislečo Skupnost](/knowledge/critical-thinking)/

  * [Prevare, na Katere Morate Biti Pozorni pri Uporabi Monera](/knowledge/monero-scams)/

  * [Kako Bodo Atomske Menjave v Monero Delovale](/knowledge/monero-atomic-swaps)/

  * [Kaj Mora Vsak Uporabnik Monera Vedeti, ko Gre za Mreženje](/knowledge/monero-networking)/

  * [Kako RingCT Prikrije Zneske Monero Transakcij](/knowledge/monero-ringct)/

  * [Kako Naslovi Monero Stealth Ščitijo Vašo Identiteto](/knowledge/monero-stealth-addresses)/

  * [Kako Monero Podnaslovi Preprečujejo Povezovanje Identitet](/knowledge/monero-subaddresses)/

  * [Pojasnjeni Monero Izhodi (Outputs)](/knowledge/monero-outputs)/

  * [Najboljše Monero Prakse za Začetnike](/knowledge/monero-best-practices)/

  * [Kako Obročni Podpisi Prikrijejo Izhode Monera](/knowledge/ring-signatures)/

  * [Kako je Monero Rešil Problem Velikosti Bloka, ki muči Bitcoin](/knowledge/dynamic-block-size)/

  * [Kako bo CLSAG Izboljšal Učinkovitost Monera](/knowledge/what-is-clsag)/

  * [Zakaj Ima Monero Tail Emisijo](/knowledge/monero-tail-emission)/

  * [Kratka zgodovina Monera](/knowledge/monero-history)/

  * [Wired Magazine se Moti Glede Monera. Evo, Zakaj](/knowledge/wired-article-debunked)/

  * [Razbijamo 15 glavnih mitov in pomislekov o Monero](/knowledge/monero-myths-debunked)/

  * [Kako Dandelion++ Ohranja Zasebnost Izvora Transakcije Monero](/knowledge/monero-dandelion)/

  * [Zakaj je Monero Odprtokoden in Decentraliziran](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero rudarjenje: zakaj je RandomX tako poseben](/knowledge/monero-mining-randomx)/

  * [Zakaj je Monero Boljši od Dash, Zcash, Zcoin (tudi z Lelantusom), Grin in Bitcoin Mikserji, kot je Wasabi (posodobljeno maja 2020)](/knowledge/why-monero-is-better)/

Nadaljnje branje