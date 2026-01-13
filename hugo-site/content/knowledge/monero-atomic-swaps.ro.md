---
title: "Cum vor funcționa schimburile atomice în Monero"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
În căutarea descentralizării și a unui sistem cu adevărat fără permisiuni, puține lucruri sunt la fel de râvnite în spațiul criptomonedei precum schimburile descentralizate și schimburile atomice. De la apariția sa, Monero a avut dificultăți în implementarea schimburilor atomice, deoarece caracteristicile de confidențialitate creează probleme unice atunci când încerci să proiectezi un protocol.

Dar mai întâi, să ne lămurim. Ce sunt schimburile atomice? Un schimb atomic este un protocol prin care două criptomonede diferite, pe blockchain-uri diferite, pot fi schimbate într-o manieră fără încredere, fără niciun intermediar. Acest lucru înseamnă că dacă cineva vrea să schimbe criptomoneda A pentru criptomoneda B, ar putea face acest lucru fără o bursă, centralizată sau descentralizată. După cum vă puteți imagina, aceasta necesită o cercetare considerabilă, iar detaliile tehnice care o fac posibilă devin destul de complicate. Din nou, LocalMonero este aici pentru a ajuta și oferă o explicație simplă pentru persoana obișnuită.

Ca să începem, haideți să considerăm forma cea mai simplă de schimb atomic, așa cum este implementat de Bitcoin. Dacă cineva vrea să schimbe Bitcoin cu o altă monedă care utilizează aceeași tehnologie de contract hash time lock, poate face acest lucru în următorul mod. Alice are Bitcoin (BTC), dar vrea Litecoin (LTC), iar Bob are LTC, dar vrea BTC. Ei decid să facă un schimb atomic astfel încât fiecare să obțină moneda pe care o dorește. Alice trimite BTC-ul ei la o adresă specială, folosind scripturi care blochează fondurile astfel încât nici măcar ea nu poate să-l acceseze. Puteți considera că Alice își pune BTC-ul într-un seif. Când seiful este creat, ea obține o cheie, și trimite un cod hash al acestei chei lui Bob. Acum, Bob nu are cheia însăși, doar codul hash, așa că încă nu poate accesa fondurile.

Bob folosește acest cod hash ca o sămânță de la care își generează propriul seif, și își trimite LTC-ul acolo, unde este de asemenea blocat. Deoarece codul hash al cheii lui Alice a fost folosit ca sămânță prin care a fost creat seiful lui Bob, ea își poate folosi cheia pentru a revendica LTC-ul din seiful lui Bob. Cheia ei se potrivește! Dar, folosind magia matematicii, când ea își folosește cheia pentru a deschide seiful LTC, îi dezvăluie cheia lui Bob, care apoi poate să o folosească pentru a revendica BTC-ul pe care l-a pus în seiful ei. Astfel, fără nici un intermediar, Alice și Bob și-au schimbat cu succes activele.

Dar există o mică problemă. Ce se întâmplă dacă Alice trimite BTC-ul în seiful ei, și Bob decide că nu mai vrea să facă tranzacția. Acum, deoarece Alice nu poate accesa BTC-ul pe care l-a blocat, iar Bob nu își va finaliza partea de tranzacție, Alice își pierde pur și simplu banii pentru totdeauna. Ei bine, din fericire, Bitcoin are o tehnică numită tranzacții de rambursare, și astfel, după o perioadă de timp, dacă BTC-ul nu este revendicat de Bob, scripturile au o rețea de siguranță integrată, unde BTC-ul va reveni automat la Alice. Acesta a fost obstacolul principal pentru implementarea schimburilor atomice de câtre Monero. Din cauza [tehnologiei de confidențialitate a semnăturilor circulare a Monero](/knowledge/ring-signatures), expeditorul unei tranzacții este întotdeauna incert. Cum poate protocolul să facă o tranzacție de rambursare dacă nici măcar nu știe de unde a venit tranzacția?

În 2017, un mic grup de cercetători a conturat o metodă diferită prin care schimburile atomice ar funcționa în Monero. După mai mulți ani de rafinare, cercetătorii au finalizat un proces prin care Monero ar putea face schimburi atomice cu Bitcoin, chiar și fără tranzacții de rambursare.

Ca și în multe alte lucruri de acest nivel de complexitate tehnică, explicația noastră va simplifica foarte mult unele lucruri pentru a transmite ideea, dar va oferi totuși o idee solidă despre mecanismele prin care acest proces ar funcționa.

Alice (care are XMR și dorește BTC) și Bob (care are BTC și dorește XMR) trebuie să descarce și să ruleze un program care suportă schimbul atomic. Acest lucru poate fi implementat în portofele, schimburi descentralizate sau programe speciale, dar software-ul trebuie să ruleze protocolul de schimb atomic. În primul pas, clienții Alinei și lui Bob se conectează unul la altul și fac mai multe secrete și chei comune. În acest pas, se creează o nouă adresă Monero, având Alice cu o jumătate de cheie, iar Bob pe cealaltă. Încă nu există niciun Monero în acolo, așa că nu este nimic de cheltuit. Un ultim lucru de notat despre această adresă, este că ambii au cheia de vizualizare a acestui portofel, așa că pot amândoi să se uite în interior pentru a vedea dacă sau când sosește Monero.

În al doilea pas, Bob trimite BTC-ul său la o adresă specială, similară cu protocolul de schimb atomic Bitcoin pe care l-am discutat deja. După ce Alice vede că BTC-ul a ajuns la acea adresă pe blockchain, ea își trimite Monero-ul la adresa Monero la care ea și Bob au amândoi o jumătate de cheie. Bob poate verifica că Monero a ajuns deoarece are și el cheia de vizualizare, și odată ce vede că Monero este în siguranță în portofel, el îi trimite Alicei o parte a unei chei care îi va permite să retragă Bitcoin-ul. Similar cu celălalt protocol, procesul de revendicare a Bitcoin-ului îi dezvăluie lui Bob jumătatea Monero a Alicei. Acum, Bob are ambele jumătăți, deci poate să revendice Monero, în timp ce Alice are doar jumătatea ei, de aceea nu poate încerca să o ia înainte de a o lua el.

Dacă ați citit tot acest lucru și sunteți încă ușor confuz despre cum a reușit Monero să ocolească problema tranzacțiilor de rambursare, răspunsul este destul de simplu. Deoarece Monero în sine nu are tranzacții de rambursare, cititorul ar trebui să observe că Bitcoin (care are tranzacții de rambursare) este trimis mai întâi și doar după ce este verificat că se află pe blockchain, se trimite Monero. Acest lucru permite Monero să utilizeze capacitatea Bitcoin de a înregistra tranzacții de rambursare și să profite de ele, fără a avea aceste capacități în sine.

Schimbul atomic este acum complet, dar de aici, Bob are câteva opțiuni pentru XMR-ul său proaspăt revendicat. El poate folosi acest portofel Monero așa cum este, sau poate muta XMR-ul în alt portofel pe care îl deține deja. Probabil că Bob va muta Monero într-un alt portofel, pentru că Alice încă are cheia de vizualizare și poate vedea în interior.

Frumusețea acestui protocol este că este încă destul de nou, iar există mult loc pentru optimizări. De asemenea, este destul de flexibil în arhitectura sa, deci implementarea în alte portofele sau schimburi descentralizate ar trebui să fie simplă și să se potrivească perfect cu arhitectura lor existentă.

Lecturi suplimentare

  * [Cum permite Monero în mod unic economiile circulare](/knowledge/monero-circular-economies/)

  * [Semnături inelare Monero vs CoinJoin ca în Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [De ce (și cum!) ar trebui să vă păstrați propriile chei](/knowledge/hold-your-keys/)

  * [Contribuind înapoi la Monero](/knowledge/contributing-to-monero/)

  * [Cum afectează nodurile de la distanță confidențialitatea Monero](/knowledge/remote-nodes-privacy/)

  * [Cum folosește Monero hard-fork-urile pentru a moderniza rețeaua](/knowledge/network-upgrades/)

  * [Vezi etichete: Cum un singur octet va reduce timpii de sincronizare a portofelului Monero cu 40%+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool și rolul său în descentralizarea mineritului Monero](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Ce va face pentru Monero](/knowledge/seraphis-for-monero/)

  * [Este convertirea Bitcoin în Monero la fel de privată ca și cumpărarea directă de Monero?](/knowledge/most-private-way-to-buy-monero/)

  * [De ce Monero folosește o configurație fără încredere, spre deosebire de Zcash](/knowledge/monero-trustless-setup/)

  * [De ce Monero este un depozit de valoare mai bun decât Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Cum poate Monero să depășească efectele de rețea ale Bitcoin](/knowledge/network-effect/)

  * [De ce Monero are cea mai mare comunitate cu gândire critică](/knowledge/critical-thinking/)

  * [Escrocherii la care să fii atent când folosești Monero](/knowledge/monero-scams/)

  * [Ce trebuie să știe fiecare utilizator Monero atunci când vine vorba de rețea](/knowledge/monero-networking/)

  * [Cum ascunde RingCT sumele tranzacțiilor Monero](/knowledge/monero-ringct/)

  * [Cum îți protejează identitatea adresele Monero invizibile](/knowledge/monero-stealth-addresses/)

  * [Cum previn subadresele Monero legătura de identitate](/knowledge/monero-subaddresses/)

  * [Explicații despre ieșirile Monero](/knowledge/monero-outputs/)

  * [Cele mai bune practici Monero pentru începători](/knowledge/monero-best-practices/)

  * [Modul în care semnăturile inelare ascund ieșirile Monero](/knowledge/ring-signatures/)

  * [Cum a rezolvat Monero problema dimensiunii blocurilor care afectează Bitcoin](/knowledge/dynamic-block-size/)

  * [Cum va îmbunătăți CLSAG eficiența Monero](/knowledge/what-is-clsag/)

  * [De ce Monero are o emisie de coadă](/knowledge/monero-tail-emission/)

  * [O scurtă istorie a Monero](/knowledge/monero-history/)

  * [Revista Wired se înșeală în legătură cu Monero, iată de ce](/knowledge/wired-article-debunked/)

  * [Top 15 mituri și îngrijorări legate de Monero dezmințite](/knowledge/monero-myths-debunked/)

  * [Cum păstrează Dandelion++ confidențialitatea originilor tranzacțiilor Monero](/knowledge/monero-dandelion/)

  * [De ce Monero este Open Source și descentralizat](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Mineritul Monero: Ce face ca RandomX să fie atât de special](/knowledge/monero-mining-randomx/)

  * [De ce Monero este mai bun decât Dash, Zcash, Zcoin (chiar și cu Lelantus), Grin și Bitcoin Mixers ca Wasabi (actualizat în mai 2020)](/knowledge/why-monero-is-better/)