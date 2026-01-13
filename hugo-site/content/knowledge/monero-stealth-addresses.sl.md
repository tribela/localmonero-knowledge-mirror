---
title: "Kako Naslovi Monero Stealth Ščitijo Vašo Identiteto"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero je implementiral tristranski pristop k zasebnosti. Te tehnologije so [podpisi zvonjenja ](/knowledge/ring-signatures), ki skrijejo pravi izhod (pošiljatelja), RingCT, ki skrije zneske, in prikriti naslovi, ki skrijejo prejemnika. Danes bomo razpravljali o zadnji od teh omenjenih tehnologij: prikritih naslovih.

Obstaja veliko razlogov, zakaj posameznik morda želi skriti, komu pošilja. Nikoli ne smemo dovoliti, da nas kdorkoli prepriča, da so vsi primeri tega neprijetna vedenja. Stvari, kot je pošiljanje nepriljubljeni politični stranki, darovanje dobrodelnim organizacijam ali podpora tistim, za katere kultura meni, da so "preklicane", so vse primeri, ko bi nekdo morda želel skriti svoje vedenje zapravljanja zaradi strahu pred posledicami, vendar so po naravi popolnoma legitimne.

Na pregledni verigi blokov so naslovi, kamor nekdo pošilja svoje transakcije, vidni vsem. Pomembno je upoštevati, da če se rudarji sami ne strinjajo s tem, kam gre denar, se lahko odločijo, da ga ne bodo rudarili v blok, s čimer učinkovito cenzurirajo to transakcijo na platformi, ki je na videz odporna na cenzuro. Edini način, da ta, resda malo verjetna, cenzura postane nemogoča je, če rudarji ne morejo razlikovati med transakcijami, ker so vsi metapodatki v verigi zakriti na različne načine. Nekaj, po čemer je Monero znan.

Monero rešuje to težavo preglednih naslovov z implementacijo prikritih naslovov, tehnologije, ki jo je za Bitcoin leta 2011 dejansko izdelal uporabnik foruma Bitcoin Talk ByteCoin (povezava z Bytecoinom, ki bi kasneje integriral prikrite naslove, ni znana). Trenutna oblika prikritih naslovov pa ima več izboljšav glede na prvotno idejo. Toda najprej, da bi videli, kako delujejo, se pogovorimo o ključih.

Težko je biti v prostoru kriptovalut in ne slišati o ključih. Besedne zveze, kot je "varnostno kopirajte svoj zasebni ključ", so običajne, a ko povprečen Joe sliši besedi "javni ključ" in "zasebni ključ", se prestraši in misli, da bo preveč tehnično in zmedeno za razumevanje. Ampak ne skrbi. Šli bomo počasi in uporabili veliko primerov.

Dve vrsti ključev, ki se uporabljata v kriptovalutah, sta, kot je bilo pravkar omenjeno, javni in zasebni. Ta dva ključa sta običajno v paru, kar pomeni, da sta določen javni in zasebni ključ povezana drug z drugim. Pravzaprav je javni ključ običajno izpeljan iz zasebnega, kar pomeni, da če poznate zasebni ključ, lahko vaša denarnica naredi nekaj izvrstne matematike in vsakič prikaže pravilen javni ključ.

Zdaj, kot pove že ime, je javni ključ lahko javen brez posledic. Običajno je to del naslova, ki ga delite za prejemanje denarja v svojo denarnico za kriptovalute. Po njegovem soimenjaku je zasebni ključ tisti, ki ga ne bi smeli deliti. To je stvar, ki vam omogoča, da podpišete in porabite transakcijo, tako da, če je ukradena ali deljena, lahko podla tretja oseba porabi vaš denar, običajno zase.

Enostavna analogija s tem bi bila ključavnica in ključ, potreben za odklepanje. Odprto ključavnico lahko svobodno delite in s to ključavnico je res mogoče zakleniti karkoli, toda samo oseba s ključem lahko odpre vse, na kar je ključavnica zaprta. Ključavnico je mogoče kopirati in deliti, ključa pa ne.

Ti ključi so običajno abstrahirani stran od uporabnika, tako da jih nikoli zares ne vidite. V Moneru se sploh ne pojavljajo kot strašljiv alfanumerični niz. V Monero običajen uporabnik pozna zasebni ključ kot svoje seme. Seed (ki bi ga morali zapisati, če ga niste) je pravzaprav le človeku berljiv zasebni ključ. 

Vidite? Konec koncev ni tako strašno. Nazaj na prikrite naslove.

Kot že omenjeno, prikriti naslovi prvotno niso bili narejeni za Monero, ampak za Bitcoin. Kot pri večini novonastalih zamisli je imela tudi ta prva ponovitev težave. Naslednji poskus je bil, ko je Nicholas van Saberhagan ustvaril CryptoNote za Bytecoin, predhodnika Monera ([tukaj si oglejte našo zgodovino Monera in Bytecoina](/knowledge/monero-history)), in čeprav je bil nedvomno izboljšan v primerjavi z izvirnikom, je imel celo nekaj subtilnih napak.

Razvijalec je sčasoma ustvaril še zadnjo ponovitev za drugo zdaj nedelujočo kriptovaluto za zasebnost, ki je odpravila izjemne težave z zasebnostjo in varnostjo z idejo. To se je sčasoma prebilo v Monero in se uporablja danes.

Čeprav so bila ta vprašanja glede zasebnosti in varnosti rešena, so prikriti naslovi tehnologiji veriženja blokov dodali drugačno posebnost, ki prej ni obstajala. Potreba po skeniranju. Ker prejemni naslovi niso javno prikazani v verigi blokov, prejemnik nikoli ne ve, ali je katera koli transakcija njegova, zato mora pregledati vse dohodne transakcije s svojim zasebnim ključem, da vidi, ali je njihov.

Pri prosojnih kovancih morajo le preveriti, ali se transakcija pošilja na vaš naslov. Enostavno vprašanje z da ali ne. Toda s prikritimi naslovi je lahko vsaka transakcija tista, ki je poslana vam, zato morate poskusiti vsako odkleniti s svojim zasebnim ključem, da vidite, ali se odpre.

To je dodaten korak, ki ga Bitcoin in njegovi derivati nimajo, in omogoča začetno nastavitev denarnice, skupaj s sinhronizacijo denarnice, ko je niste odprli nekaj časa, veliko dlje kot Bitcoin. Kompromis pa je potreben, da sprostite jamstva za zasebnost, ki jih ima. Opozoriti je treba, da za razliko od najšibkejše točke trifekta zasebnosti, podpisov zvonjenja, prikriti naslovi niso dovzetni za hevristiko. Zanaša se na preizkušeno in pravo kriptografijo eliptične krivulje, na katero se zanaša celoten internet, zato bi njeno zlom pomenil konec računalniške varnosti na splošno, ne le Monera.

Nadaljnje branje

  * [Kako Monero edinstveno omogoča krožna gospodarstva](/knowledge/monero-circular-economies)/

  * [Obročni ring podpisi Monero vs CoinJoin kot v Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Zakaj (in kako!) bi morali imeti svoje ključe](/knowledge/hold-your-keys)/

  * [Prispevek nazaj v Monero](/knowledge/contributing-to-monero)/

  * [Kako oddaljena vozlišča vplivajo na zasebnost Monera](/knowledge/remote-nodes-privacy)/

  * [Kako Monero uporablja hard-forke za nadgradnjo omrežja](/knowledge/network-upgrades)/

  * [Ogled oznak: Kako bo en bajt skrajšal čas sinhronizacije Monero denarnice za 40%+](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool in Njegova Vloga pri Decentralizaciji Monero Rudarjenja](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Kaj bo Naredil za Monero](/knowledge/seraphis-for-monero)/

  * [Ali je Pretvorba Bitcoina v Monero Enako Zasebna kot Neposredni Nakup Monera?](/knowledge/most-private-way-to-buy-monero)/

  * [Zakaj Monero Uporablja Nezaupljivo nNastavitev za Razliko od Zcasha](/knowledge/monero-trustless-setup)/

  * [Zakaj je Monero Boljši Hranilnik Vrednosti kot Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Kako lahko Monero premaga omrežne učinke Bitcoina](/knowledge/network-effect)/

  * [Zakaj ima Monero Najbolj Kritično Mislečo Skupnost](/knowledge/critical-thinking)/

  * [Prevare, na Katere Morate Biti Pozorni pri Uporabi Monera](/knowledge/monero-scams)/

  * [Kako Bodo Atomske Menjave v Monero Delovale](/knowledge/monero-atomic-swaps)/

  * [Kaj Mora Vsak Uporabnik Monera Vedeti, ko Gre za Mreženje](/knowledge/monero-networking)/

  * [Kako RingCT Prikrije Zneske Monero Transakcij](/knowledge/monero-ringct)/

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