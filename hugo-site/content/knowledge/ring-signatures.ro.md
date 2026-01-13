---
title: "Modul în care semnăturile inelare ascund ieșirile Monero"
slug: "ring-signatures"
date: "2020-09-08"
image: "/images/rings.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero este cunoscut pe scară largă în spațiul criptografic ca fiind regele monedelor de confidențialitate. Deși toată lumea știe că Monero oferă o bună confidențialitate, nu la fel de mulți înțeleg cum funcționează această confidențialitate.

Multe alte monede de confidențialitate publică infografice cu diagrame de comparație, care enumeră numele tehnologiei de confidențialitate a fiecărei monede, iar în cele mai multe dintre ele etichetează tehnologia Monero ca fiind RingCT, dar acest lucru este doar parțial adevărat. Monero are, de fapt, o abordare în trei direcții a confidențialității. O tehnologie pentru a ascunde destinatarul unei tranzacții, una pentru a ascunde suma trimisă și una pentru a ascunde ieșirea utilizată, acestea fiind adrese invizibile, RingCT și, respectiv, semnături inelare.

Această abordare pe trei direcții înseamnă că, dacă una dintre tehnologii este afectată, celelalte nu au neapărat aceeași soartă. Semnăturile inelare sunt cea mai slabă verigă a sistemului de confidențialitate; cuvântul slab însemnând aici cea mai susceptibilă la atacuri euristice. Haideți să ne luăm ceva timp pentru a le explora, nu-i așa?

După cum s-a menționat mai sus, scopul semnăturilor inelare este de a ascunde un rezultat utilizat într-o tranzacție. Dacă terminologia "intrare/ieșire" a criptomonedelor este confuză pentru dumneavoastră, nu vă faceți griji. De fapt, nu este atât de complicat. Când auziți "ieșire", gândiți-vă doar la un cec. Unul dintre acele lucruri, care nu mai sunt atât de comune, cu care oamenii obișnuiesc să plătească. La fel ca un cec, poate fi notat în orice sumă - 10 dolari, 32,50 dolari etc. - și este schimbat între părțile implicate în tranzacție. În cazul criptomonedelor, ieșirile îndeplinesc aceste funcții.

Atunci când cineva vă plătește 10 Monero, primiți o ieșire de 10 XMR. Această ieșire are o valoare (10) și este ceea ce se ia din portofelul expeditorului, la fel cum, atunci când plătiți un serviciu, o factură părăsește portofelul fizic și este dată persoanei de la care cumpărați.

Modul în care este ascunsă ieșirea este prin construirea unui inel (de unde și numele) de ieșiri momeală. Dar aceste momeli nu sunt ieșiri "false". Ele sunt ieșiri reale din trecut din blockchain care nu au nicio legătură cu tranzacția actuală, dar pentru un observator extern, fiecare dintre aceste ieșiri ar putea părea la fel de probabilă ca cea reală. Dimensiunea setului de ieșiri momeală, plus cea reală, se numește "ringsize", iar în prezent Monero are 11. Așadar, există zece ieșiri momeală și una reală.

De ce să nu mărim acest număr la 100 sau chiar la 1000? Cu cât mai mulți, cu atât mai bine, nu? Ei bine, din punct de vedere al confidențialității, da, dar mai sunt și alte lucruri de luat în considerare. Să ne întoarcem la un exemplu fizic pentru a vedea la ce mă refer. Dacă ați dori să ascundeți una dintre bancnotele de un dolar printre zece momeli, ar trebui să aveți la dumneavoastră în portofel unsprezece dolari pentru fiecare dolar pe care doriți să îl cheltuiți. Un dolar real și zece falși. Acest lucru devine deja destul de greoi dacă doriți să cheltuiți chiar și câțiva dolari. Imaginați-vă acum că am mărit suma momeală la 1000. Pentru fiecare dolar pe care doriți să îl cheltuiți, ar trebui să aveți la dumneavoastră 1001 de dolari. Ar trebui să cari cu tine o servietă doar pentru a cumpăra un baton de ciocolată! Este important de reținut că semnăturile inelare nu funcționează chiar în acest mod, de exemplu, momelile în sine nu fac parte din semnătură, ci doar referințele la ele, dar sperăm că această analogie poate fi oarecum utilă pentru a vă imagina conceptele de bază.

Momeala de pe blockchain funcționează în mod similar. Fiecare momeală adăugată crește timpul și costul de verificare al tranzacției. Fiecare nod trebuie să descarce întreaga semnătură inelară pentru fiecare tranzacție, iar fiecare semnătură inelară conține ieșirea reală, precum și momelile. Nu numai atât, dar trebuie să verifice matematic că cel puțin una dintre aceste ieșiri este reală, iar timpul de verificare matematică crește, de asemenea, cu fiecare momeală. Acest lucru înseamnă că trebuie să găsim o cale de mijloc fericită, în care dimensiunea inelelor să fie suficient de mare pentru a ascunde în mod adecvat ieșirea reală, chiar și împotriva multor atacuri euristice, dar suficient de mică pentru a nu determina creșterea masivă a blockchain-ului. Nu este suficient să alegem un număr arbitrar sau să creștem pur și simplu dimensiunea inelului atunci când facem semnătura mai mică (cum ar fi în cazul CLSAG). Comunitatea Monero dorește dovezi concrete, matematice, cu privire la care mărime a inelelor oferă cele mai bune compromisuri. Un număr prea mic, iar confidențialitatea nu va fi suficient de puternică împotriva atacurilor euristice. Un număr prea mare ar putea aduce doar un beneficiu marginal în ceea ce privește confidențialitatea și ar putea avea de suferit inutil în ceea ce privește scalarea.

Un ultim lucru de menționat. O parte din literatura Monero simplifică și spune că semnăturile inelare ascund expeditorul, dar acest lucru nu este în întregime adevărat, iar diferența nu este doar pedantă. Diferența dintre expeditor (un om) și un rezultat (o bancnotă) este una importantă atunci când vine vorba de păstrarea confidențialității. În timp ce un rezultat poate avea legături cu un expeditor, un rezultat în sine nu este egal cu un expeditor. Așadar, chiar dacă o semnătură inelară ar fi spartă, aceasta nu are neapărat legătură cu identitatea unei persoane, iar atât suma, cât și destinatarul sunt în continuare ascunse, minimizând daunele aduse vieții private a tuturor părților.

Asta nu înseamnă că o semnătură de inel ruptă este nesemnificativă. Orice metadate scurse sunt rele și au potențialul de a dezvălui mai multe informații decât credem, în special atunci când sunt folosite împreună cu alte metadate. Așadar, facem tot posibilul pentru a ne asigura că dimensiunea inelului ales are în spatele deciziei o rigoare academică, că scurgerea altor metadate este redusă la minimum, iar experiențele utilizatorilor se orientează spre cele mai bune acțiuni posibile.

Dar dacă probabilitatea unei semnături sparte vă îngrijorează în continuare, există o veste incredibilă la orizont. Următoarea generație de protocoale de confidențialitate la care se lucrează, cum ar fi Triptych, Arcturus și Lelantus, are capacități foarte bune. În aceste protocoale, dimensiunea scalează logaritmic, nu liniar, pe măsură ce crește dimensiunea inelului. Acest lucru înseamnă că putem introduce 100 de momeli, dar spațiul utilizat este mai apropiat de dimensiunea inelului 10 din vechea tehnologie. Aceasta este o diferență destul de mare și va îmbunătăți semnificativ confidențialitatea în general.

În jocul de-a șoarecele și pisica, care este confidențialitatea, Monero inovează continuu pentru a rămâne în fața curbei și pentru a asigura cea mai bună confidențialitate practică pentru toți.

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