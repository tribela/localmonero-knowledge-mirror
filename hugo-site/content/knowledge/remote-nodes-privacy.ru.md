---
title: "Cum afectează nodurile de la distanță confidențialitatea Monero"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Unul dintre cele mai mari avantaje pe care Monero le are față de alte criptomonede este confidențialitatea pe lanț, dar v-ați întrebat vreodată cum rezistă confidențialitatea lui Monero atunci când folosiți un nod la distanță? Dar dacă folosiți un server "portofel ușor" precum MyMonero?

În această postare vom analiza unele dintre detaliile din spatele modului în care Monero oferă o confidențialitate excepțională pe lanț, chiar și atunci când se utilizează un nod la distanță, precum și la ce trebuie să fim atenți atunci când folosim noduri la distanță.

## Ce funcție au nodurile în Monero?

## Ce funcție au nodurile în Monero?

Pentru cei mai puțin familiarizați cu modul în care funcționează Monero, nodurile (sau serverele) din rețeaua Monero pot fi administrate de oricine și permit proprietarului nodului - sau altor persoane cu care acesta alege să îl împartă! - să sincronizeze o copie a lanțului de blocuri și să furnizeze această copie celorlalți din rețea. Aceste noduri verifică, de asemenea, toate tranzacțiile care au loc în rețea, precum și toate blocurile care sunt publicate și se asigură că toate acestea respectă regulile stabilite prin consens.

Cealaltă funcție pe care o îndeplinesc nodurile în Monero este aceea de a furniza toate datele de care are nevoie portofelul Monero preferat pentru a verifica în mod corespunzător tranzacțiile care vă aparțin și pentru a face tranzacții noi. Aceste date sunt furnizate de noduri în două moduri:

  * Datele din fiecare bloc de pe blockchain sunt solicitate de către portofel, scanate în căutarea tranzacțiilor care vă aparțin și apoi aruncate după ce sunt verificate de către portofel. 
    * Această etapă va fi în curând îmbunătățită drastic, datorită [vezi etichete](/knowledge/view-tags-reduce-monero-sync-time).
  * Atunci când trimiteți tranzacții, nodul pe care îl utilizați oferă o listă de posibile momeli (sau intrări false) pe care să le folosiți atunci când construiți tranzacția, asigurându-vă că aveți o mulțime bună în care să vă ascundeți de fiecare dată când cheltuiți Monero. 
    * Aceste momeli fac parte din [semnăturile inelare](/knowledge/ring-signatures), o piesă importantă a abordării Monero în ceea ce privește confidențialitatea pe lanț.

  * Această etapă va fi în curând îmbunătățită drastic, datorită [vezi etichete](/knowledge/view-tags-reduce-monero-sync-time).

  * Aceste momeli fac parte din [semnăturile inelare](/knowledge/ring-signatures), o piesă importantă a abordării Monero în ceea ce privește confidențialitatea pe lanț.

## Care este cel mai privat și sigur mod de a utiliza Monero?

## Care este cel mai privat și sigur mod de a utiliza Monero?

The best thing to do, even with the strong on-chain privacy provided by Monero when using remote nodes, is to run your own Monero node to ensure that you have a pristine copy of the Monero blockchain handy and that your IP address is well protected. The other benefit when running your own node is that you can contribute back to the network, letting other nodes synchronize from your node or even letting other users connect to your node with their wallets.

Acestea fiind spuse, Monero oferă în continuare o confidențialitate excelentă atunci când se utilizează un nod la distanță. Dacă sunteți interesat să vă rulați propriul nod Monero, iată un ghid ușor de urmat pentru a face acest lucru:

  * [Rulați un nod Monero](https://sethforprivacy.com/guides/run-a-monero-node/)

## Ce poate afla un nod la distanță despre mine?

## Ce poate afla un nod la distanță despre mine?

Atunci când folosiți un nod la distanță, există câteva informații cheie care sunt expuse unui nod la distanță și câteva moduri cheie prin care acel nod vă poate ataca, vă poate împiedica să efectuați tranzacții și multe altele.

Primul lucru pe care un nod la distanță îl poate afla despre dvs. este adresa IP publică. Deși sperăm că aceasta va fi ascunsă prin intermediul unui VPN sau Tor, nodul de la distanță ar putea asocia adresa IP publică a dvs. cu tranzacția, ajutându-l să afle de unde efectuați tranzacția. Nodul de la distanță poate afla, de asemenea, ultimul bloc pe care l-ați sincronizat în portofelul dvs. și poate folosi acest lucru pentru a încerca să facă presupuneri despre dvs., cum ar fi momentul în care utilizați Monero în mod normal și când ați cheltuit Monero ultima dată. Acest lucru este valabil mai ales dacă veniți mereu de la aceeași adresă IP (cum ar fi cea de acasă). Ultimul lucru cheie pe care un nod la distanță îl poate afla despre dvs. sunt informațiile de bază despre tranzacțiile pe care le trimiteți prin intermediul său. Deși acestea pot fi cele mai evidente date pe care operatorul nodului la distanță le obține despre dumneavoastră, este important să înțelegeți că acestea ar putea fi folosite pentru a ajuta la depistarea expeditorului tranzacției atunci când se combină aceste informații cu alte date din afara lanțului. Acest lucru poate fi deosebit de periculos dacă nodul de la distanță este condus de o entitate rău intenționată, de o companie de analiză a lanțului de blocuri sau de un stat-națiune opresiv.

Un nod la distanță poate încerca, de asemenea, să vă creeze probleme ascunzând blocuri de dvs., făcându-vă să credeți că portofelul dvs. a fost sincronizat când nu a fost așa. Acest lucru vă poate face să credeți că fondurile sunt pierdute sau vă poate împiedica să cheltuiți fonduri până când vă conectați la un alt nod. Ultimul lucru cheie pe care îl poate face un nod de la distanță este să vă furnizeze portofelului dvs. o listă manipulată de momeli. Acest lucru ar putea face ca portofelul dvs. să nu reușească complet să creeze tranzacții (ceea ce vă împiedică să cheltuiți fonduri) sau ar putea permite nodului de la distanță să încerce să furnizeze momeli despre care știe că sunt cheltuite pentru a reduce anonimatul pe care îl primiți în fiecare tranzacție.

## Ce garanții de confidențialitate mai există atunci când se utilizează un nod la distanță?

## Ce garanții de confidențialitate mai există atunci când se utilizează un nod la distanță?

Deși acest articol poate că v-a speriat puțin, este important să realizați că intimitatea oferită de Monero este excelentă chiar și atunci când se utilizează un nod la distanță și depășește cu mult orice altă criptomonedă atunci când este utilizată în acest mod. Obțineți în continuare confidențialitatea puternică pe lanț oferită de Monero, deoarece nodul de la distanță nu cunoaște niciodată adevărata intrare (ce monede cheltuiți), suma de Monero cheltuită în tranzacție sau adresa destinatarului tranzacției. De asemenea, observatorii externi nu pot vedea adevărata intrare, suma sau adresele implicate (indiferent de tipul de nod pe care alegeți să îl utilizați!), asigurând că, în afara nodului la distanță, chiar și adresa IP, informațiile de sincronizare a portofelului și tranzacțiile au garanții puternice de confidențialitate.

De asemenea, nodul de la distanță nu are niciodată acces la tranzacțiile anterioare pe care le-ați trimis sau primit sau la suma de Monero aflată în portofelul dvs. și își pierde orice vizibilitate asupra tranzacțiilor dvs. în momentul în care începeți să utilizați un alt nod. Nicio cheie privată (fie că este vorba de chei de cheltuieli sau de vizualizare) nu este furnizată vreodată nodului la distanță, astfel încât portofelul dumneavoastră rămâne privat, sigur și utilizabil. Indiferent de nodul de la distanță, de asemenea, nu riscați niciodată să pierdeți Monero sau să vi se fure, deoarece nodul nu poate modifica adresa destinatarului, nu are niciodată acces la cheile private ale portofelului dumneavoastră și nu vă poate confisca Monero în niciun fel.

## Ce zici de "portofele ușoare" precum MyMonero?

## Ce zici de "portofele ușoare" precum MyMonero?

Deși subiectul este puțin în afara scopului acestui articol, am vrut să abordez un tip unic de portofel în Monero - portofelele ușoare. Denumirea de portofel ușor vine de la faptul că portofelul tău (de pe telefon sau calculator) nu trebuie să efectueze niciuna dintre sincronizările blockchain, ceea ce face ca experiența să fie mai rapidă și mai fluidă.

Cu toate acestea, portofelele de acest tip vin cu un compromis sever în ceea ce privește confidențialitatea, deocamdată - portofelul dvs. trimite cheia privată de vizualizare către serverul la distanță pe care îl utilizați (cum este cel implicit din MyMonero), oferind serverului la distanță vizibilitate totală asupra tuturor fondurilor primite de la crearea portofelului dvs. (și până când încetați să mai utilizați acel portofel sau sămânță). Acest lucru reduce drastic confidențialitatea pe care o primiți de la operatorul de nod și trebuie abordat cu prudență.

Din fericire, comunitatea Monero lucrează la îmbunătățirea software-ului pe care îl puteți utiliza pentru a vă găzdui propriul server de portofel ușor (LWS), care vă va permite să aveți o sincronizare rapidă fără a avea încredere într-o terță parte cu cheile de vizualizare privată - deoarece veți rula software-ul în care portofelul dvs. trimite cheile de vizualizare privată!

Pentru mai multe informații despre serverul personalizat de portofel ușor, consultați depozitul Github de mai jos:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Cum pot afla mai multe?

## Cum pot afla mai multe?

Dacă sunteți curioși și doriți să înțelegeți mai bine nodurile din Monero și să încercați să folosiți un nod de la distanță sau să vă rulați propriul nod, consultați linkurile de mai jos pentru a găsi locuri excelente pentru a începe:

  * [Monero World, a list of community-run remote nodes that can be used](https://moneroworld.com/#nodes)
  * [Monero nodes run by Seth For Privacy, the author of this article](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, a list of remote nodes with frequently checked status](https://monero.fail/)
  * [How to connect to a remote node within GUI wallet](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia - Remote Node](https://www.getmonero.org/resources/moneropedia/remote-node.html)

Lecturi suplimentare

  * [Cum permite Monero în mod unic economiile circulare](/knowledge/monero-circular-economies)/

  * [Semnături inelare Monero vs CoinJoin ca în Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [De ce (și cum!) ar trebui să vă păstrați propriile chei](/knowledge/hold-your-keys)/

  * [Contribuind înapoi la Monero](/knowledge/contributing-to-monero)/

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