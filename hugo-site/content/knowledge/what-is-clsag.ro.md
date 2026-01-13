---
title: "Cum va îmbunătăți CLSAG eficiența Monero"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Ca protocol, Monero se află în prezent într-o stare constantă de inovare. Utilizând cercetarea atât în soluțiile on-chain, cât și în cele off-chain, comunitatea Monero caută domenii de îmbunătățire pentru a face Monero mai privat, mai scalabil și mai accesibil tuturor. Una dintre cele mai recente inovații este înlocuirea schemei de semnătură inelară linkable, MLSAG, cu un înlocuitor drop-in CLSAG, care înseamnă Concise Linkable Spontaneous Anonymous Group.

La nivel superficial, implementarea CLSAG va reduce cu 25% cele mai frecvente tranzacții cu 2 intrări, 2 ieșiri. De asemenea, vom observa o scădere cu 10% a timpului de verificare.

Dar ce este mai exact CLSAG? Ce face și cum diferă de vechea versiune, MLSAG? Să luăm un minut pentru a ne reaminti de ce și cum funcționează semnăturile inelare, astfel încât să putem înțelege mai bine acest concept. Semnăturile în inel permit intrări non-interactive, cu martori care nu se pot distinge, prin utilizarea seturilor de anonimat selectate de semnatar pentru ieșirile anterioare. În termeni simpli, aceasta permite unui utilizator să își ascundă ieșirile utilizate într-o tranzacție alături de ieșiri fără legătură între ele, și poate face toate acestea fără a avea nevoie de participarea altor persoane. Tot ce aveți nevoie este o copie a blockchain-ului. Fiecare dintre aceste ieșiri pare în mare parte să aibă aceeași probabilitate de a fi cea trimisă efectiv, ascunzând astfel metadatele despre expeditor.

Aceasta generează totuși o mică problemă. Ce s-ar întâmpla dacă un utilizator ar construi o semnătură inelară cu toate ieșirile momeală? Cum ar putea ști cineva că expeditorul necunoscut nu are autoritatea de a trimite niciuna dintre ele? Ar putea acest utilizator să cheltuiască bani falși? Răspunsul este nu. Semnătura inelară include o metodă pentru a dovedi că cel puțin una dintre ieșiri este deținută de expeditorul necunoscut, fără a dezvălui care este aceasta. De fapt, atât CLSAG, cât și MLSAG (denumite în continuare SAG) reprezintă partea din semnătura inelară care dovedește acest lucru. Interesant este că, în același timp, se dovedește că suma tranzacției, deși ascunsă în spatele tranzacțiilor confidențiale (RingCT), se echilibrează. Faptul că SAG-urile dovedesc două lucruri, că o ieșire este deținută de cineva din inel și că tranzacția este echilibrată, este important și, de fapt, acolo unde se află economiile de dimensiune și verificare. Dacă acest lucru devine confuz, nu vă faceți griji, vom ajunge în curând la o analogie amuzantă și ușor de înțeles.

Vechiul sistem de semnătură, MLSAG (Multilayered Linkable Spontaneous Anonymous Group) dovedește cele două lucruri menționate mai sus într-o semnătură inelară, dar le face pe fiecare separat. Folosirea unor calcule separate pentru cheile de semnare și de angajament înseamnă operațiuni mai lente. Un computer modern poate efectua aceste calcule în câteva milisecunde, ceea ce nu pare mult și, într-adevăr, pentru o tranzacție nu este. Dar dacă luăm în considerare numărul mare de tranzacții de pe blockchain-ul Monero și faptul că un nod care se sincronizează de la zero va trebui să descarce și să verifice fiecare dintre ele, octeții și milisecundele încep să se adune rapid.

CLSAG combină calculele matematice necesare pentru a le dovedi pe amândouă într-unul singur, precum și le calculează pe amândouă deodată, și face acest lucru într-un mod sigur. Ce înseamnă într-o manieră sigură? Ei bine, pentru a clarifica acest lucru, precum și, sperăm, pentru a face ca totul să aibă mai mult sens, să explorăm acea analogie amuzantă promisă.

Să spunem că trebuie să mergeți atât la magazinul alimentar, cât și la magazinul de feronerie, pentru a lua două lucruri diferite: alimente și produse chimice toxice de curățare. Nu vreți ca acestea să se amestece, deoarece, dacă se întâmplă un accident, substanțele chimice se vor vărsa pe alimente, făcându-le necomestibile. Decideți să fiți super sigur și să conduceți de acasă până la magazinul alimentar, să cumpărați alimentele și apoi să vă întoarceți acasă. Abia după ce ați descărcat mâncarea, vă urcați din nou în mașină, mergeți la magazinul de feronerie și vă întoarceți acasă cu produsele chimice. Ați făcut două călătorii separate pentru a asigura siguranța tuturor achizițiilor. Deși este într-adevăr sigur, acest lucru este ineficient. Acest lucru reprezintă MLSAG, unde sunt stocate două seturi diferite de calcule matematice și se fac două "călătorii" diferite pentru a le calcula.

Decideți însă că doriți o modalitate mai rapidă de a face acest lucru. Este prea mult timp pierdut. Sigur că dacă o faci o dată sau de două ori nu-ți va fura viața, dar dacă trebuie să faci asta de nenumărate ori, orele încep să se adune. Începi să te întrebi dacă nu poți face o singură călătorie în schimb. De la casă, la magazinul alimentar, la magazinul de feronerie și înapoi acasă. Nu poți să te duci și să arunci totul la întâmplare în mașină. Nu este sigur. În schimb, desemnează diferite locuri în mașină pentru diferite lucruri și asigură-te că totul se potrivește frumos la locul său. În acest fel, reușești să faci o singură călătorie în siguranță la ambele magazine și să ții lucrurile departe una de cealaltă. Acest lucru reprezintă CLSAG. Există acum un singur set de calcule matematice stocate în această tranzacție pentru a dovedi aceste două lucruri, iar acest lucru se face la distanță, astfel încât să nu interfereze unul cu celălalt. Încă mai trebuie să se facă o călătorie, dar ați redus numărul acestora destul de drastic.

Toate acestea sună foarte interesant. Este posibil să găsim și alte scurtături sau alte modalități de a economisi timp și spațiu? Răspunsul este da și nu. Potrivit cercetătorilor actuali ai MRL, probabil că nu este posibil să modificăm în continuare construcțiile de tip SAG pentru a obține o dimensiune sau o viteză mai bună; cu toate acestea, alte construcții, cum ar fi Arcturus, Omniring, RCT3 sau Triptych, produc o scalare mult mai bună a dimensiunilor și beneficii de verificare folosind metode matematice diferite. Cu toate acestea, fiecare dintre aceste abordări "next-gen" ale protocoalelor ambigue pentru semnatari vine cu propriile compromisuri în ceea ce privește detaliile de implementare și sunt în curs de cercetare și investigare activă.

După toate acestea, Monero inovează mereu.

Lecturi suplimentare

  * [Cum permite Monero în mod unic economiile circulare](/knowledge/monero-circular-economies)/

  * [Semnături inelare Monero vs CoinJoin ca în Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [De ce (și cum!) ar trebui să vă păstrați propriile chei](/knowledge/hold-your-keys)/

  * [Contribuind înapoi la Monero](/knowledge/contributing-to-monero)/

  * [Cum afectează nodurile de la distanță confidențialitatea Monero](/knowledge/remote-nodes-privacy)/

  * [Cum folosește Monero hard-fork-urile pentru a moderniza rețeaua](/knowledge/network-upgrades)/

  * [Vezi etichete: Cum un singur octet va reduce timpii de sincronizare a portofelului Monero cu 40%+](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool și rolul său în descentralizarea mineritului Monero](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Ce va face pentru Monero](/knowledge/seraphis-for-monero)/

  * [Este convertirea Bitcoin în Monero la fel de privată ca și cumpărarea directă de Monero?](/knowledge/most-private-way-to-buy-monero)/

  * [De ce Monero folosește o configurație fără încredere, spre deosebire de Zcash](/knowledge/monero-trustless-setup)/

  * [De ce Monero este un depozit de valoare mai bun decât Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Cum poate Monero să depășească efectele de rețea ale Bitcoin](/knowledge/network-effect)/

  * [De ce Monero are cea mai mare comunitate cu gândire critică](/knowledge/critical-thinking)/

  * [Escrocherii la care să fii atent când folosești Monero](/knowledge/monero-scams)/

  * [Cum vor funcționa schimburile atomice în Monero](/knowledge/monero-atomic-swaps)/

  * [Ce trebuie să știe fiecare utilizator Monero atunci când vine vorba de rețea](/knowledge/monero-networking)/

  * [Cum ascunde RingCT sumele tranzacțiilor Monero](/knowledge/monero-ringct)/

  * [Cum îți protejează identitatea adresele Monero invizibile](/knowledge/monero-stealth-addresses)/

  * [Cum previn subadresele Monero legătura de identitate](/knowledge/monero-subaddresses)/

  * [Explicații despre ieșirile Monero](/knowledge/monero-outputs)/

  * [Cele mai bune practici Monero pentru începători](/knowledge/monero-best-practices)/

  * [Modul în care semnăturile inelare ascund ieșirile Monero](/knowledge/ring-signatures)/

  * [Cum a rezolvat Monero problema dimensiunii blocurilor care afectează Bitcoin](/knowledge/dynamic-block-size)/

  * [De ce Monero are o emisie de coadă](/knowledge/monero-tail-emission)/

  * [O scurtă istorie a Monero](/knowledge/monero-history)/

  * [Revista Wired se înșeală în legătură cu Monero, iată de ce](/knowledge/wired-article-debunked)/

  * [Top 15 mituri și îngrijorări legate de Monero dezmințite](/knowledge/monero-myths-debunked)/

  * [Cum păstrează Dandelion++ confidențialitatea originilor tranzacțiilor Monero](/knowledge/monero-dandelion)/

  * [De ce Monero este Open Source și descentralizat](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Mineritul Monero: Ce face ca RandomX să fie atât de special](/knowledge/monero-mining-randomx)/

  * [De ce Monero este mai bun decât Dash, Zcash, Zcoin (chiar și cu Lelantus), Grin și Bitcoin Mixers ca Wasabi (actualizat în mai 2020)](/knowledge/why-monero-is-better)/

Lecturi suplimentare