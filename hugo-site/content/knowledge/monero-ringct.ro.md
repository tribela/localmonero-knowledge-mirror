---
title: "Cum ascunde RingCT sumele tranzacțiilor Monero"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Confidențialitatea Monero nu depinde de un singur mecanism care, odată compromis, ar dezvălui totalitatea tranzacțiilor, ci de trei tehnologii diferite care lucrează împreună pentru a oferi confidențialitate holistică, compensând astfel punctele slabe ale celorlalte componente. Această abordare tridentă constă în [semnături inele](/knowledge/ring-signatures), RingCT și [adrese furtive](/knowledge/monero-stealth-addresses). Aceste trei tehnologii ascund respectiv expeditorului real (emisia), suma și destinatarul. Astăzi vom vorbi despre RingCT.

RingCT este, probabil, cel mai tehnic dintre cele trei și poate fi dificil de înțeles, așa că nu vom explica exact cum funcționează, ci vom arăta cum este posibil să nu știi o sumă și să confirmi totuși lucruri despre ea. Și nu vă faceți griji, vom folosi din plin exemple, ca întotdeauna.

În primul rând, să explorăm de ce este important să verificăm orice despre sumele implicate. De ce nu le păstrăm pur și simplu complet secrete? Răspunsul este că există modalități ingenioase prin care oamenii pot crea bani din nimic dacă li se oferă ocazia. Cum ar putea funcționa așa ceva? Să vedem un exemplu.

Dacă dorești să achiziționezi un obiect de la un prieten și acesta vrea zece dolari pentru el, atunci tu începi cu zece dolari și el începe cu zero. După ce îi dai zece dolari, el are zece dolari și tu ai zero. Ai început cu zece și acum el are zece. Niciun ban nu a fost creat sau distrus în această tranzacție.

În cazul criptomonedelor, o persoană ingenioasă poate da zece dolari pentru articol și, în loc să primească zero dolari înapoi, pot primi doi dolari înapoi. În loc de 0 și 10 care duc la 10 și 0 (adica 10 egal 10), acum avem 0 și 10 care duce la 10 și 2 (adica 10 egal 12). Doi Monero au fost creați din nimic. Îți poți imagina că dacă individul ar face acest lucru de mai multe ori, ar putea acumula o avere imensă într-un timp scurt.

În cazul Bitcoin și al altora, acest lucru ar fi ușor de văzut. Te uiți la intrările care merg într-o tranzacție și la ieșirile care ies și te asiguri că ce este trimis este egal cu ceea ce este primit. Dacă aceste sume ar fi criptate și nu vizibile atunci, un utilizator nu are nicio modalitate de a verifica că ceea ce este trimis și ceea ce este primit este același lucru.

Într-o încercare de a crește confidențialitatea Bitcoin, Gregory Maxwell a creat Confidential Transactions (CT), o nouă tehnologie care ar permite sumelor criptate, în timp ce demonstrează că nimic nu a fost creat sau distrus în proces. Așa cum se întâmplă cu majoritatea tehnologiilor de confidențialitate, nu a fost introdusă în Bitcoin, dar Monero era interesat să o adopte. A existat doar o problemă. Tehnologia deja implementată a semnăturilor inelare era incompatibilă cu ideea propusă. Astfel, unul dintre cercetătorii MRL de la acea vreme, Shen Noether, a modificat CT în RingCT, o versiune a CT care era compatibilă cu semnăturile inelare.

Din nou, modul în care funcționează acesta este destul de tehnic și ar fi dificil de explicat într-un articol introductiv. Pentru entuziaștii de criptografie care pur și simplu trebuie să știe, există multe articole pe internet despre modul în care funcționează CT. Pentru restul dintre noi, acest articol va arăta cum ar putea fi posibil să ascunzi sumele, dar totuși să demonstrezi că nimic nu a fost creat sau distrus.

Să presupunem că Alice dorește să îi trimită lui Bob bani. Alice va trimite 10 XMR lui Bob, care va primi 10 XMR. 10 egal 10, deci nimic nu este în neregulă aici. Dar Alice nu vrea ca nimeni să știe cât trimite ea. Așa că ea și Bob creează un secret comun. Practic, un număr pe care doar ei doi îl știu. Să spunem că numărul este 22. Acum, Alice înmulțește 10 (cât trimite ea de fapt) cu 22 pentru a obține 220. Acesta este numărul pe care-l împărtășește cu rețeaua.

Minerii înșiși nu știu numărul secret. Dacă ar ști, ar putea împărți numărul pe care îl văd cu numărul secret și ar obține suma reală trimisă. Dar din moment ce nu știu, nu pot. Ei văd, totuși, că Bob va primi 220. S-au trimis 220. S-au primit 220. 220 egal 220. În acest fel, rețeaua poate verifica că niciun Monero nu a fost creat sau distrus, fără a cunoaște suma reală pe care Alice a trimis-o lui Bob.

Din moment ce Bob cunoaște numărul secret comun, când primește banii, el doar împarte la 22 pentru a obține suma reală pe care Alice a trimis-o, 10. Alice și Bob știu amândoi cât a fost trimis și cât a fost primit, în timp ce toți ceilalți primesc un număr fals.

Din nou, aceasta nu este modalitatea reală în care funcționează CT, dar oferă o idee despre cum ar fi posibil așa ceva. Modul real implică lucruri precum angajamente Pedersen, două sume trimise (o sumă criptată destinatarului și o sumă de angajament pentru rețea) și ... da, este deja ușor de văzut cum ai putea te-ai pierde în toate acestea.

Un aspect de notat însă este că, în timp ce RingCT ascunde suma tranzacționată între două părți într-o tranzacție, nu ascunde alte două seturi de numere.

Primul este tranzacțiile coinbase. Dacă acest termen nu îți este familiar, înseamnă practic recompensa pe care minerii o primesc pentru găsirea următorului bloc. Acest număr nu este ascuns. Oricine poate vedea cât a acordat protocolul unui miner pentru serviciul lor. În acest fel, suma actuală de Monero existentă poate fi cunoscută prin adăugarea tuturor tranzacțiilor coinbase. Suma lor va fi egală cu Monero actual în circulație.

Al doilea număr care nu este ascuns este taxa plătită minerilor atunci când un utilizator trimite o tranzacție. Taxele trebuie să fie transparente astfel încât minerii să știe pe cine să prioritizeze. Acesta este un mod prin care utilizatorii își pot prejudicia confidențialitatea, deoarece dacă cineva folosește o taxă de minerit unică de fiecare dată când trimite o tranzacție (cum ar fi 0.12345), atunci tranzacțiile lor pot fi legate.

În afara acestor cazuri, RingCT a ascuns sumele Monero din 2017, iar confidențialitatea noastră colectivă este cu atât mai puternică pentru asta.

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

  * [Cum îți protejează identitatea adresele Monero invizibile](/knowledge/monero-stealth-addresses)/

  * [Cum previn subadresele Monero legătura de identitate](/knowledge/monero-subaddresses)/

  * [Explicații despre ieșirile Monero](/knowledge/monero-outputs)/

  * [Cele mai bune practici Monero pentru începători](/knowledge/monero-best-practices)/

  * [Modul în care semnăturile inelare ascund ieșirile Monero](/knowledge/ring-signatures)/

  * [Cum a rezolvat Monero problema dimensiunii blocurilor care afectează Bitcoin](/knowledge/dynamic-block-size)/

  * [Cum va îmbunătăți CLSAG eficiența Monero](/knowledge/what-is-clsag)/

  * [De ce Monero are o emisie de coadă](/knowledge/monero-tail-emission)/

  * [O scurtă istorie a Monero](/knowledge/monero-history)/

  * [Revista Wired se înșeală în legătură cu Monero, iată de ce](/knowledge/wired-article-debunked)/

  * [Top 15 mituri și îngrijorări legate de Monero dezmințite](/knowledge/monero-myths-debunked)/

  * [Cum păstrează Dandelion++ confidențialitatea originilor tranzacțiilor Monero](/knowledge/monero-dandelion)/

  * [De ce Monero este Open Source și descentralizat](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Mineritul Monero: Ce face ca RandomX să fie atât de special](/knowledge/monero-mining-randomx)/

  * [De ce Monero este mai bun decât Dash, Zcash, Zcoin (chiar și cu Lelantus), Grin și Bitcoin Mixers ca Wasabi (actualizat în mai 2020)](/knowledge/why-monero-is-better)/

Lecturi suplimentare