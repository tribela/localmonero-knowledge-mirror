---
title: "Cum previn subadresele Monero legătura de identitate"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero a găsit întotdeauna modalități inovatoare de a rezolva problemele dificile de confidențialitate. De multe ori, aceste inovații duc la alte inovații și, uneori, aceste tehnologii rezultate pot fi folosite pentru cazuri de utilizare care nu au fost luate în considerare anterior. Nicăieri nu este mai bine exemplificat acest lucru decât în cazul tehnologiei Monero de subadresare.

Să luăm în considerare o problemă ipotetică de confidențialitate, în care utilizarea unei adrese pe mai multe platforme de către persoane aparent fără legătură între ele poate duce la stabilirea unei legături și la eliminarea anonimatului acestor persoane. Mai simplu spus, dacă ați fi o persoană pe nume Billy Joe Bob și ați vinde mere pentru Bitcoin, ați putea să vă afișați adresa Bitcoin într-un loc public pentru ca clienții să vă plătească. Să spunem că adresa începe cu șirul alfanumeric 7XybV3... Dar, lăsând la o parte riscul evident de confidențialitate, care constă în faptul că oricine poate să vă verifice soldul Bitcoin și să vadă cât ați vândut, există un al doilea risc de confidențialitate, despre care nu se vorbește prea des. Să presupunem că sunteți și un hacker clandestin, cunoscut sub numele de l33tz0r. Faci muncă de informator, spunând unei populații neștiutoare despre corupția guvernamentală, și este imperativ să îți păstrezi identitatea secretă. Accepți donații în Bitcoin pentru munca ta și postezi adresa pe un forum public. Este aceeași adresă la care acceptați bani de la clienții dumneavoastră cu mere. Cea de la 7XybV3... una.

Un atac simplu, dar devastator, de deanonimizare ar fi utilizarea unui motor de căutare pe internet pentru a căuta adresa dumneavoastră Bitcoin. Introducerea adresei 7XybV3... în motorul de căutare aduce două rezultate diferite. Afacerea cu mere, și l33tz0r. Acest lucru este suficient pentru a lega cele două identități și pentru a-l deanonimiza pe l33tz0r, cu consecințe potențial înfricoșătoare din partea puterilor în stat.

Este important de reținut că acest atac este posibil ȘI cu Monero. Chiar dacă Monero ascunde majoritatea datelor de pe lanț, acest atac nu folosește niciuna. Folosește doar adresa, care trebuie partajată pentru a primi plata. În mod public în cazul donațiilor anonime. Aceasta este o modalitate potențială prin care utilizatorii Monero își pot afecta involuntar confidențialitatea și este, de asemenea, un exemplu al modului în care, chiar dacă Monero este de top în ceea ce privește păstrarea confidențialității, nu este antiglonț.

Modalitatea obișnuită de a evita această problemă era deținerea mai multor portofele. Cu adrese diferite postate pentru fiecare identitate (sau caz de utilizare), acestea nu pot fi legate între ele. Dar această confidențialitate este valabilă doar dacă utilizatorul nu le confundă niciodată. Postarea accidentală a unei adrese incorecte ar avea aceleași efecte de corelare. De asemenea, sămânța fiecărei adrese trebuie să fie păstrată în siguranță, ceea ce sporește munca de infosecuritate necesară pentru fiecare portofel nou creat.

Soluția lui Monero a fost subadresele. Capacitatea de a crea un număr absolut masiv de adrese sub adresa principală, folosind-o ca un fel de sămânță. Fiecare subadresă generată poate accepta Monero, iar toate acestea ajung în același portofel. Folosind această metodă, numărul de identități care pot fi operate sub o singură adresă este uriaș, menținând în același timp munca de infosecuritate la un nivel minim. De asemenea, aceste adrese nu pot fi legate matematic, astfel încât, dacă utilizatorul nu-și strigă conexiunea în lume, un observator extern va avea mari dificultăți în a le lega.

Dar un alt caz de utilizare interesant a apărut de la subadrese; ca o opțiune de înlocuire a ID-urilor de plată urâte de toată lumea.

ID-urile de plată erau o modalitate prin care comercianții puteau identifica ce client a trimis ce plată. Deoarece informațiile Monero sunt ascunse în lanț, destinatarul unei tranzacții nu poate vedea care este adresa care a trimis-o. Acest lucru înseamnă că, dacă există articole cu prețuri similare și comenzi multiple, poate deveni imposibil să se identifice cine a trimis ce anume. ID-urile de plată sunt un șir unic, aleatoriu, generat de comerciant și dat clientului. Clientul îl adaugă ca un câmp separat atunci când trimite tranzacția. Acest șir aleatoriu este plasat în blockchain ca parte a tranzacției și, în acest fel, comerciantul este capabil să identifice și să sorteze tranzacțiile primite.

Această metodă a fost defectă din mai multe puncte de vedere. În primul rând, aceasta diminuează uniformitatea datelor pe lanț. Metadatele suplimentare, unice, pot face ca unele tranzacții să se distingă de restul, permițând astfel o analiză euristică. Acest lucru este valabil mai ales atunci când aceste metadate nu sunt impuse ca fiind obligatorii pentru toți. Cu toate acestea, dacă ar fi obligatorii pentru toată lumea, s-ar adăuga spațiu inutil în lanțul de blocuri și nu s-a urmărit acest lucru. De asemenea, în cazul în care un ID de plată ar fi reutilizat vreodată, indiferent de motiv, ar fi banal să se lege două tranzacții ca fiind conectate. Acest lucru se întâmpla de obicei în cazul depozitelor la exchange, iar oricine ar putea lega cu ușurință tranzacțiile ca fiind atât un depozit la un exchange, cât și de la o anumită persoană.

În al doilea rând, din perspectiva UX, ID-urile de plată creează un al doilea pas cu care utilizatorii de criptomonede care provin din alte monede nu sunt obișnuiți, iar dacă acestea sunt uitate, atunci comerciantul care trebuie să identifice aceste tranzacții prin alte mijloace are mari bătăi de cap. De obicei, acest lucru se făcea vorbind direct cu fiecare client care a uitat să pună ID-ul de plată și confirmând alte informații de identificare pe care numai ei le puteau cunoaște, cum ar fi o combinație între sumă, data trimiterii și ID-ul tranzacției.

Acest pas suplimentar a fost ratat de mulți și s-a ajuns la punctul în care unele exchange-uri au început să taxeze clienții dacă banii lor trebuiau recuperați manual din cauza uitării unui ID de plată. Alții au strâns din dinți și au înghițit costurile suplimentare de asistență, dar nimeni nu a fost mulțumit de acest lucru.

A existat o soluție în acest sens, adresele integrate, care fuziona adresa și ID-ul de plată într-un singur șir de caractere, astfel încât să nu poată fi uitate, dar adoptarea a fost destul de slabă, în ciuda beneficiilor pe care comercianții le-ar fi obținut prin includerea acesteia.

Într-o turnură interesantă a evenimentelor, subadresele au intervenit pentru a salva situația. Capacitatea de a genera cantități mari de subadrese pentru fiecare adresă principală și de a identifica ce tranzacții au intrat în ce subadrese a permis comercianților să scape de ID-urile de plată într-un mod elegant, adoptând în același timp următoarea generație a tehnologiei Monero. De atunci, cele mai multe exchange-uri și instrumente pentru comercianți au trecut la subadrese ca modalitate principală de identificare a tranzacțiilor.

Ceea ce a început ca o soluție pentru o problemă de confidențialitate s-a transformat în ceva mult mai mult, care a rezolvat o problemă majoră de UX atât pentru comercianți, cât și pentru clienți. Inovația generează mai multă inovație, care poate adesea să se transforme în câștiguri neașteptate pentru toată lumea. Monero a văzut acest lucru de nenumărate ori și depune mari eforturi pentru a inova ceea ce este posibil pe blockchain. Cine știe ce alte lucruri putem debloca împreună?

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