---
title: "Kako bo CLSAG Izboljšal Učinkovitost Monera"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero kot protokol je trenutno v stalnem procesu inovacij. Skupnost Monero z raziskavami rešitev na verigi in zunaj nje išče področja, ki jih je mogoče izboljšati, da bi Monero postal zasebnejši, bolj razširljiv in dostopnejši vsem. Ena od novejših inovacij je zamenjava sheme povezljivega obročnega podpisa MLSAG z nadomestno shemo CLSAG (kratica za Concise Linkable Spontaneous Anonymous Group).

Na prvi pogled bo izvajanje CLSAG za 25 % zmanjšalo najpogostejši dve vhodni in dve izhodni transakciji. Prav tako se bo za 10 % zmanjšal čas preverjanja.

Kaj je pravzaprav CLSAG? Kaj počne in kako se razlikuje od stare različice MLSAG? Vzemimo si minuto časa in se spomnimo, zakaj in kako pri obročnih podpisih, da bomo bolje razumeli ta koncept. Obročni podpisi omogočajo neinteraktivne vhode, ki se ne razlikujejo med pričami, z uporabo anonimnih nizov prejšnjih izhodov, ki jih izbere podpisnik. Laično povedano, uporabniku omogoča, da skrije svoje izpise, uporabljene v transakciji, skupaj z nepovezanimi izpisi, in vse to lahko stori, ne da bi pri tem potreboval sodelovanje kogar koli drugega. Vse, kar potrebujete, je kopija verige blokov. Vsak od teh izpisov je večinoma videti enako verjeten kot dejanski izpis, ki je bil poslan, s čimer se skrijejo metapodatki o pošiljatelju.

To pa povzroča manjšo težavo. Kaj če bi uporabnik sestavil obročni podpis z vsemi izpisi vab? Kako bi kdo vedel, da neznani pošiljatelj ni pooblaščen za pošiljanje katerega koli od njih? Ali bi ta uporabnik lahko porabil lažni denar? Odgovor je ne. Obročni podpis vključuje metodo za dokazovanje, da je vsaj eden od izhodov v lasti neznanega pošiljatelja, ne da bi razkril, kateri je to. Dejansko sta tako CLSAG kot MLSAG (v nadaljevanju imenovana SAG) del obročnega podpisa, ki to dokazuje. Zanimivo je, da hkrati dokazujeta, da je znesek transakcije, čeprav skrit za zaupnimi transakcijami (RingCT), uravnotežen je. To, da SAG dokazujejo dve stvari, in sicer da je en izpis v lasti nekoga v obroču in da je transakcija uravnotežena, je pomembno in pravzaprav pomeni prihranek pri velikosti in preverjanju. Če vas to zmede, ne skrbite, kmalu bomo prišli do zabavne in lahko razumljive analogije.

Stara podpisna shema MLSAG (Multilayered Linkable Spontaneous Anonymous Group) dokazuje zgoraj omenjeni dve stvari v obročnem podpisu, vendar vsako posebej. Uporaba ločenih izračunov za ključe podpisovanja in ključe zavezanosti pomeni počasnejše operacije. Sodoben računalnik lahko te izračune opravi v nekaj milisekundah, kar se ne zdi veliko in dejansko za eno transakcijo ni. Toda če upoštevamo ogromno število transakcij v verigi blokov Monero in dejstvo, da bo moralo vozlišče, ki se sinhronizira od začetka, prenesti in preveriti vsako od njih, se bajti in milisekunde začnejo hitro kopičiti.

CLSAG združi matematične postopke, potrebne za dokazovanje obojega v enega in izračuna oboje hkrati ter to stori na varen način. Kaj to pomeni na varen način? Da bi to razjasnili in upamo, da bo celotna stvar postala bolj smiselna, raziščimo obljubljeno zabavno analogijo.

Nazadnje morate iti v trgovino z živili in v trgovino s strojno opremo po dve različni stvari: hrano in strupene kemikalije za čiščenje. Ne želite, da se mešata, saj se bodo v primeru nesreče kemikalije razlile po hrani, zaradi česar bo ta postala neužitna. Odločite se, da boste zelo varni in se od hiše do trgovine z živili odpeljete z avtomobilom, kupite hrano in se nato vrnete do hiše. Šele ko raztovorite hrano, se vrnete v avto, se odpeljete do trgovine s strojno opremo in se s kemikalijami vrnete v svojo hišo. Opravili ste dve ločeni vožnji, da bi zagotovili varnost vseh nakupov. Čeprav je to res varno, je neučinkovito. To predstavlja MLSAG, kjer sta shranjena dva različna niza matematičnih podatkov, za njihov izračun pa sta opravljena dva različna "izleta".

Izvedeli ste, da želite hitrejši način izvedbe. To je preveč izgubljenega časa. Seveda vam to, da to storite enkrat ali dvakrat, ne bo ukradlo življenja, toda če morate to početi znova in znova, se ure začnejo seštevati. Začnete se spraševati, ali lahko namesto tega opravite eno samo potovanje. Od doma do trgovine z živili, do trgovine s strojno opremo in nazaj domov. Ne morete iti in vse naključno vreči v avto. To ni varno. Namesto tega določite različna mesta v avtomobilu za različne stvari in poskrbite, da vse lepo sede na svoje mesto. Tako lahko varno opravite en izlet v obe trgovini in ohranite stvari stran od drugih. To predstavlja CLSAG. V tej transakciji je zdaj shranjen samo en niz matematičnih podatkov, ki dokazujejo ti dve stvari, in to tako, da se ne motita druga druge. Še vedno je treba opraviti potovanje, vendar ste njihovo število precej drastično zmanjšali.

Vse to se sliši zelo zanimivo. Ali je mogoče najti druge bližnjice ali druge načine za prihranek časa in prostora? Odgovor je Da in Ne. Po mnenju sedanjih raziskovalcev MRL verjetno ni mogoče dodatno spremeniti konstrukcij tipa SAG za boljšo velikost ali hitrost; vendar druge konstrukcije, kot so Arcturus, Omniring, RCT3 ali Triptych, z uporabo različnih matematičnih metod ustvarjajo veliko boljše prednosti pri skaliranju velikosti in preverjanju. Vendar ima vsak od teh pristopov "naslednje generacije" k protokolom z nedvoumnim podpisnikom svoje lastne kompromise pri podrobnostih izvajanja, zato se aktivno raziskujejo in proučujejo.

Konec koncev, Monero bo vedno inovativen.

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

  * [Kako Naslovi Monero Stealth Ščitijo Vašo Identiteto](/knowledge/monero-stealth-addresses)/

  * [Kako Monero Podnaslovi Preprečujejo Povezovanje Identitet](/knowledge/monero-subaddresses)/

  * [Pojasnjeni Monero Izhodi (Outputs)](/knowledge/monero-outputs)/

  * [Najboljše Monero Prakse za Začetnike](/knowledge/monero-best-practices)/

  * [Kako Obročni Podpisi Prikrijejo Izhode Monera](/knowledge/ring-signatures)/

  * [Kako je Monero Rešil Problem Velikosti Bloka, ki muči Bitcoin](/knowledge/dynamic-block-size)/

  * [Zakaj Ima Monero Tail Emisijo](/knowledge/monero-tail-emission)/

  * [Kratka zgodovina Monera](/knowledge/monero-history)/

  * [Wired Magazine se Moti Glede Monera. Evo, Zakaj](/knowledge/wired-article-debunked)/

  * [Razbijamo 15 glavnih mitov in pomislekov o Monero](/knowledge/monero-myths-debunked)/

  * [Kako Dandelion++ Ohranja Zasebnost Izvora Transakcije Monero](/knowledge/monero-dandelion)/

  * [Zakaj je Monero Odprtokoden in Decentraliziran](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero rudarjenje: zakaj je RandomX tako poseben](/knowledge/monero-mining-randomx)/

  * [Zakaj je Monero Boljši od Dash, Zcash, Zcoin (tudi z Lelantusom), Grin in Bitcoin Mikserji, kot je Wasabi (posodobljeno maja 2020)](/knowledge/why-monero-is-better)/

Nadaljnje branje