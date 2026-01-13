---
title: "Ce trebuie să știe fiecare utilizator Monero atunci când vine vorba de rețea"
slug: "monero-networking"
date: "2020-11-11"
image: "/images/networking.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Nu ar trebui să fie o surpriză pentru nimeni faptul că Monero și, de fapt, toate criptomonedele, funcționează pe internet. Și totuși, chiar dacă această afirmație pare elementară și evidentă, mulți nu iau în considerare implicațiile pe care acest lucru le are în ceea ce privește confidențialitatea lor. Cu alte cuvinte, există unele lucruri împotriva cărora Monero poate și nu poate să se protejeze, doar prin natura funcționării pe internet. Unele dintre aceste considerații sunt simple inconveniente, în timp ce altele sunt mult mai grave într-un scenariu în care este necesară o confidențialitate absolută. Haideți să ne facem timp pentru a ne familiariza cu modul în care utilizatorii Monero interacționează între ei în rețea și ce înseamnă acest lucru pentru confidențialitatea lor.

Începând cu partea trivială a lucrurilor, dacă un utilizator nu are acces la internet, acesta nu poate descărca blocuri noi, nu poate propaga tranzacții în numele altora și nici nu poate trimite propriile tranzacții. Un lucru interesant de remarcat este că un utilizator cu un nod complet, fără acces la internet, poate construi o tranzacție offline care poate fi trimisă ulterior. Acest lucru se datorează faptului că o semnătură inelară are nevoie doar de ieșiri din blockchain pentru a se ascunde cu. O scurtă reamintire cu privire la [modul de funcționare a semnăturilor inelare](/knowledge/ring-signatures), ascunde rezultatul real pe care îl trimite un utilizator printre o colecție de rezultate neafiliate alese din trecut. Dacă utilizatorul are acces la aceste ieșiri sub forma unui blockchain complet descărcat (nod complet), atunci poate crea semnătura inelară din ieșirile din trecut și, odată cu reluarea conectivității la internet, poate propaga tranzacția în rețea.

Un utilizator care utilizează un nod la distanță nu poate face acest lucru, deoarece, atunci când își construiește semnătura inelară, acesta contactează nodul complet la distanță pentru a obține ieșirile pe care să le includă în semnătura inelară. Lipsa internetului înseamnă că nu poate ajunge la acest nod, deci nu are capacitatea de a construi tranzacții offline.

Înainte de a continua cu unele dintre considerațiile legate de confidențialitate, să facem o scurtă introducere în modul în care funcționează internetul în ansamblu. Întregul internet nu este altceva decât computere care se conectează la alte computere. Asta este tot. Blogul pe care vă place să îl citiți? Doar niște fișiere găzduite pe computerul altcuiva. Site-ul pe care citești acest articol (LocalMonero)? Fișiere și coduri găzduite pe un computer undeva. Chiar și site-urile mari și nebunești funcționează în acest fel. Să luăm de exemplu YouTube. Doar fișiere video găzduite pe sistemele gigantice de calculatoare ale Google, iar tu te conectezi la ele pentru a descărca videoclipul pe propriul computer pentru a-l putea viziona.

Aceste computere se pot deosebi între ele deoarece fiecare computer conectat la internet primește un număr unic de identificare numit adresă IP. Acestea sunt, de obicei, patru seturi de numere separate prin puncte, de exemplu: 172.66.35.7. Este important să ținem cont de acest lucru atunci când ne gândim la modul în care informațiile Monero se deplasează pe internet. Monero este o rețea peer-to-peer (P2P), ceea ce înseamnă că calculatoarele se conectează direct între ele, în loc să folosească un intermediar. Astfel, atunci când nodul complet al unui utilizator descarcă un bloc nou descoperit, acesta nu îl descarcă de la un server central, ci de la colegii săi. Dezavantajul este că, din moment ce utilizatorii se conectează direct între ei, aceștia își cunosc reciproc adresele IP.

Ce zici? Care-i problema? E doar un număr, nu? Nu chiar. Adresele IP conțin în sine informații despre utilizator, cum ar fi țara de origine și furnizorul de rețea, dar, și mai rău, furnizorii de servicii de internet (ISP) cunosc adresa IP a fiecărei persoane care le utilizează serviciile. Acest lucru înseamnă că acești furnizori de servicii de internet și cei cu care lucrează pot urmări traficul de internet al unui utilizator și, folosind câteva tactici inteligente, pot descoperi că acesta folosește Monero. Acum, înainte de a vă speria, observați formularea de aici. Tot ceea ce pot face acești spioni este să vadă că o persoană se conectează la alte noduri din rețeaua Monero. Datorită tehnologiei de confidențialitate a Monero, nu se scurge nimic altceva despre persoana respectivă. Nici dacă rulează sau nu un nod, nici dacă/când trimite tranzacții, iar dacă o tranzacție este trimisă, nu se știe nimic despre ea. Tot ceea ce pot vedea acești furnizori de servicii de internet este că unul dintre utilizatorii lor se conectează la rețeaua Monero.

Acum, pentru unele persoane, în anumite locații, această informație poate fi suficientă pentru a aduce daune reputației sau libertății. Sau poate că ideea ca cineva să vă invadeze intimitatea și ceea ce faceți pe internet, indiferent de motiv, nu este acceptabilă pentru dumneavoastră. Aceste persoane sunt încurajate să se conecteze la rețeaua Monero doar folosind VPN, Tor sau I2P, toate acestea fiind servicii care ascund adresa IP a unui utilizator de ceilalți, precum și ceea ce face un utilizator față de ISP-ul său. Diferențele dintre aceste servicii depășesc sfera de aplicare a acestui articol, dar există o mulțime de articole de înaltă calitate scrise pe această temă, așa că utilizatorii interesați sunt încurajați să studieze!

Pentru restul dintre noi, putem crede că faptul că alții știu că suntem conectați la rețeaua Monero nu este o problemă atât de mare. La urma urmei, conținutul real al tranzacțiilor noastre, sau dacă trimitem vreuna, este ascuns publicului, așa că care este răul? Deși acest lucru poate fi adevărat, utilizatorii sunt încurajați să ia în considerare faptul că principala atracție a criptomonedelor este aceea de a fi propria lor bancă. Atunci când vă dețineți cheia privată și dacă i se întâmplă ceva, nimeni nu vă poate ajuta să vă recuperați fondurile pierdute.

A fi propria ta bancă înseamnă să ai în vedere nu doar securitatea ta digitală, ci și securitatea fizică. S-ar putea foarte bine ca știrea că o persoană se conectează la rețeaua Monero să atragă atenția nedorită, nu neapărat din partea unor actori la scară largă, cum ar fi statele naționale, ci din partea unor actori mai mici cu interese egoiste, cum ar fi hackerii care caută să facă un ban ușor. Există într-adevăr nenumărate povești în tot spațiul criptografic despre astfel de scenarii care au avut loc în realitate.

Acest articol nu are scopul de a provoca teamă, ci mai degrabă de a încuraja utilizatorii să facă cercetări cu privire la metodele de protecție pentru navigarea pe internet care sunt potrivite pentru ei. Vestea bună este că aceste abilități se vor transfera și la utilizarea generală a internetului, nu doar la utilizarea Monero și, ca atare, în lumea noastră din ce în ce mai conectată la internet, un utilizator avizat nu poate da greș acumulând cunoștințele și abilitățile adecvate pentru a fi în siguranță și pentru a fi cu adevărat propria bancă.

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

  * [Cum vor funcționa schimburile atomice în Monero](/knowledge/monero-atomic-swaps/)

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