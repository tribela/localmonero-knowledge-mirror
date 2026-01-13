---
title: "Kaj Mora Vsak Uporabnik Monera Vedeti, ko Gre za Mreženje"
slug: "monero-networking"
date: "2020-11-11"
image: "/images/networking.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Nikogar ne bi smelo presenetiti, da Monero in pravzaprav vsaka kriptovaluta deluje na internetu. In vendar, čeprav se ta izjava zdi osnovna in očitna, mnogi ne upoštevajo posledic, ki jih to pomeni v zvezi z njihovo zasebnostjo. Z drugimi besedami, pred nekaterimi stvarmi se Monero lahko zaščiti in pred nekaterimi ne, že zaradi narave delovanja v internetu. Nekateri od teh pomislekov so zgolj nevšečnosti, drugi pa so veliko resnejši v scenariju, kjer je potrebna popolna zasebnost. Vzemimo si čas in se seznanimo s tem, kako uporabniki Monera komunicirajo drug z drugim v omrežju in kaj to pomeni za njihovo zasebnost.

Če uporabnik nima dostopa do interneta, ne more prenašati novih blokov, razširjati transakcij v imenu drugih ali pošiljati lastnih transakcij. Zanimivo je, da lahko uporabnik s polnim vozliščem in brez dostopa do interneta sestavi transakcijo brez povezave, ki jo lahko pošlje pozneje. To je zato, ker obročni podpis potrebuje samo izhode iz verige blokov, s katerimi se lahko skrije. Kratek opomnik o [kako delujejo obročni (ring) podpisi ](/knowledge/ring-signatures), skrije dejanski izhod, ki ga uporabnik pošilja med zbirko nepovezanih izhodov, izbranih iz preteklosti. Če ima uporabnik dostop do teh izhodov v obliki popolnoma prenesene verige blokov (polno vozlišče), potem lahko ustvari podpis obroča iz preteklih izhodov in, ko se internetna povezljivost znova vzpostavi, razširi transakcijo v omrežje.

Uporabnik, ki uporablja oddaljeno vozlišče, tega ne more storiti, saj se pri sestavljanju obročnega podpisa obrne na oddaljeno polno vozlišče, da bi v obročni podpis vključil izhodne podatke. Če ni interneta, pomeni, da ne more priti do tega vozlišča, zato nima možnosti konstruiranja transakcij brez povezave.

Preden nadaljujemo z nekaterimi vidiki zasebnosti, si na kratko oglejmo, kako deluje internet kot celota. Celoten internet ni nič drugega kot računalniki, ki se povezujejo z drugimi računalniki. To je to. Blog, ki ga radi berete? Samo nekaj datotek, ki gostujejo v računalniku nekoga drugega. Spletno mesto, na katerem berete ta članek (LocalMonero)? Datoteke in koda, ki gostujejo nekje v računalniku. Tako delujejo celo velika in nora spletna mesta. Vzemimo na primer YouTube. Samo video datoteke, ki gostujejo v Googlovih velikanskih računalniških sistemih, vi pa se povežete z njimi in prenesete video na svoj računalnik, da si ga lahko ogledate.

Ti računalniki se med seboj razlikujejo, ker ima vsak računalnik, ki je povezan v internet, edinstveno identifikacijsko številko, imenovano naslov IP. To so običajno štirje sklopi številk, ločeni s piko, na primer: 172.66.35.7. To je pomembno upoštevati, ko razmišljamo o tem, kako se informacije o Moneru premikajo po internetu. Monero je omrežje peer-to-peer (P2P), kar pomeni, da se računalniki med seboj povezujejo neposredno in ne s pomočjo posrednika. Ko torej uporabnikovo polno vozlišče prenese novo odkriti blok, ga ne prenese iz osrednjega strežnika, temveč od svojih vrstnikov. Slaba stran tega je, da uporabniki, ki se med seboj povezujejo neposredno, poznajo naslove IP drug drugega.

Na kaj? Kaj je v tem velikega? To je le številka, kajne? Ne ravno. Naslovi IP sami po sebi vsebujejo informacije o uporabniku, kot so država izvora in ponudnik omrežja, še huje pa je, da ponudniki internetnih storitev (ISP) poznajo naslov IP vsake osebe, ki uporablja njihove storitve. To pomeni, da lahko ti ponudniki internetnih storitev in tisti, s katerimi sodelujejo, spremljajo uporabnikov internetni promet in z nekaj spretnimi taktikami ugotovijo, da uporablja Monero. Preden se prestrašite, si oglejte besedilo. Vse, kar lahko ti vohuni storijo, je, da vidijo, da se oseba povezuje z drugimi vozlišči v omrežju Monero. Zaradi tehnologije zasebnosti Monero se o posamezniku ne razkrije nič drugega. Ne to, ali upravlja vozlišče ali ne, ne to, ali/kdaj pošilja transakcije, in če je transakcija poslana, ni znana nobena od njenih informacij. Vse, kar lahko ti ponudniki internetnih storitev vidijo, je, da se eden od njihovih uporabnikov povezuje z omrežjem Monero.

Tudi na nekaterih mestih je lahko za nekatere ljudi že ta informacija dovolj, da škoduje ugledu ali svobodi. Morda pa je za vas nesprejemljiva že sama zamisel, da bi kdo iz kakršnega koli razloga posegal v vašo zasebnost in to, kar počnete v internetu. Te posameznike pozivamo, naj se v omrežje Monero povežejo le prek omrežij VPN, Tor ali I2P, kar so storitve, ki pred drugimi skrijejo uporabnikov naslov IP in pred ponudniki internetnih storitev skrijejo, kaj uporabnik počne. Razlike med temi storitvami presegajo okvir tega članka, vendar je na to temo napisanih veliko kakovostnih člankov, zato zainteresiranim uporabnikom priporočamo, da se podučijo!

Za ostale morda mislimo, da to, da drugi vedo, da smo povezani z omrežjem Monero, ni tako velik problem. Navsezadnje je dejanska vsebina naših transakcij ali če sploh kakšno pošiljamo, skrita javnosti, tako da kaj je narobe? Čeprav je to morda res, naj uporabniki upoštevajo dejstvo, da je glavna privlačnost kriptovalut v tem, da smo sami sebi banka. Ko imate v rokah svoj zasebni ključ in če se z njim kaj zgodi, vam nihče ne more pomagati povrniti izgubljenih sredstev.

Biti lastna banka pomeni, da ne upoštevate le svoje digitalne varnosti, temveč tudi svojo fizično varnost. Prav lahko se zgodi, da lahko vedenje o posamezniku, ki se je povezal z omrežjem Monero, prinese neželeno pozornost, ne nujno velikih akterjev, kot so nacionalne države, temveč manjših akterjev s sebičnimi interesi, kot so hekerji, ki želijo na enostaven način zaslužiti denar. Po vsem kriptografskem prostoru je namreč nešteto zgodb, ko so se takšni scenariji dejansko zgodili.

Ta članek ni namenjen vzbujanju strahu ali ustrahovanju, temveč spodbujanju uporabnikov, da opravijo nekaj raziskav o tem, katere metode zaščite pri brskanju po spletu so primerne zanje. Dobra novica je, da se bodo te veščine prenesle tudi na splošno uporabo interneta, ne le na uporabo Monera, zato v našem vse bolj z internetom povezanem svetu spreten uporabnik ne more zgrešiti, če si nabere ustrezno znanje in veščine, da ostane varen in je resnično sam sebi banka.

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