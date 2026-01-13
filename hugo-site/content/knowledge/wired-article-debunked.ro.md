---
title: "Revista Wired se înșeală în legătură cu Monero, iată de ce"
slug: "wired-article-debunked"
date: "2020-06-24"
image: "/images/wired.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Atât în domeniul confidențialității, cât și în cel al criptomonedelor, dezinformarea este adesea un fenomen răspândit. Avem [un articol care prezintă cincisprezece presupuneri comune incorecte sau învechite despre Monero](/knowledge/monero-myths-debunked), dar vrem să ne facem timp pentru a aborda un anumit articol care este adesea citat și distribuit de către scepticii Monero.

Publicația Wired a scos la iveală [un articol](https://www.wired.com/story/monero-privacy/) pe 27 martie 2018, care la rândul său a fost scris ca răspuns la o altă lucrare proaspăt scoasă de sub tipar și publicată de diverși academicieni, intitulată: "An Empirical Analysis of Traceability in the Monero Blockchain" ("O analiză empirică a posibilității de urmărire în blockchain-ul Monero").

Deși lucrarea a fost coautorată de persoane cu un conflict de interese clar (a se citi: sunt consilieri și au un interes în Zcash), lucrarea a fost moderat bine primită de comunitatea Monero, confirmând lucruri pe care comunitatea le știa deja și despre care a scris în propriile lor lucrări Monero Research Lab. ([MRL-0001](https://web.getmonero.org/resources/research-lab/pubs/MRL-0001.pdf) și [MRL-0004](https://web.getmonero.org/resources/research-lab/pubs/MRL-0004.pdf)) dintre care cel mai vechi a fost publicat cu patru ani înainte. Cu toate acestea, au existat, de asemenea, mai multe frustrări, în principal conflictul de interese, faptul că problemele erau deja cunoscute, discutate și - în unele cazuri - remediate, precum și caracterizarea greșită a garanțiilor de confidențialitate ale Monero la momentul respectiv. Comunitatea a comentat asupra pretipăririi lucrării, iar multe dintre recomandările lor au ajuns în lucrarea finală.

Dar ce anume a fost caracterizat greșit? Faptul că Monero nu a avut defectele discutate în lucrare de peste un an. Tranzacțiile de dinainte de 2017 au fost într-adevăr vulnerabile la o formă de scurgere de informații despre confidențialitate, dar la momentul publicării, Monero a rezolvat majoritatea problemelor. Pentru a fi corecți față de autori, aceștia discută într-o mică măsură despre remedierile Monero, dar nu suficient pentru a influența efectul pe care l-a avut asupra ciclului mediatic al criptomonedelor la momentul respectiv. De aici și articolul din Wired.

În timp ce putem examina articolul Wired în cauză ca pe un articol de epocă și cât de adevărat sau fals a fost la momentul respectiv, faptul că încă mai este împărtășit astăzi ca argument pentru a explica de ce garanțiile de confidențialitate ale Monero sunt slabe invită de fapt la o analiză a modului în care articolul rezistă în prezent. Acceptăm cu plăcere această invitație.

O citire rapidă a articolului arată mai multe rânduri senzaționale, cum ar fi "[Descoperirile] nu ar trebui să îngrijoreze doar pe oricine încearcă să cheltuiască Monero pe furiș astăzi" și întregul ton al articolului care postulează cercetarea ca fiind "nouă", bazată în mare parte pe publicație. Lucrarea academică în sine are recomandări precum avertizarea utilizatorilor de Monero cu privire la potențiala compromitere a anonimatului lor, în ciuda faptului că nu numai că aceste discuții au avut loc încă din 2014, dar că strigătul de alarmă al comunității a fost ca oamenii să nu cumpere Monero și că acesta era foarte experimental.

Dar cum rămâne cu criticile în sine? Realitatea este că multe dintre problemele legate de Monero ca monedă de confidențialitate fie nu mai sunt valabile pentru Monero, fie sunt probleme comune cu monedele de confidențialitate ca categorie de criptomonede bazate pe blockchain. Să începem să le abordăm.

Una dintre cele mai des citate critici la adresa Monero este că, datorită permanenței și imuabilității blockchain-ului, dacă o tehnologie viitoare ar încălca confidențialitatea, toate tranzacțiile anterioare ale Monero ar fi dezvăluite. Cu alte cuvinte, confidențialitatea dumneavoastră are un ceas care ticăie.

Nu putem sublinia suficient acest lucru. Practic, fiecare monedă de confidențialitate care folosește metode de ofuscare și confidențialitate pe lanț are acest defect, dar este adesea folosit împotriva Monero (în mod ironic, de multe ori de monede de confidențialitate concurente cu aceeași problemă) și este folosit și în acest articol. Răspunsul la această critică ar putea fi surprinzător pentru unii, dar Monero poate fi de fapt mai puțin vulnerabil decât alte monede de confidențialitate la acest lucru datorită faptului că are o abordare multiplă a confidențialității.

Monero ascunde ieșirile (expeditorii), sumele și destinatarii prin trei tehnologii diferite, respectiv semnăturile inelare, RingCT și adresele invizibile. Dintre acestea, semnăturile inelare sunt cele mai slabe și cele mai susceptibile atât la euristicile din zilele noastre, cât și la tehnologiile teoretice, viitoare, care încalcă confidențialitatea. Acest lucru este cunoscut de comunitatea Monero de ani de zile, iar cercetările active sunt în curs de desfășurare pentru a îmbunătăți sau a înlocui în întregime sistemul de semnături inelare.

Cu toate acestea, chiar dacă semnătura inelului ar fi fost spartă în întregime, doar adevărata ieșire ar fi fost dezvăluită. NU expeditorul (ca în cazul individului), ci ieșirea. Cuplarea unei ieșiri cu o identitate nu este imposibilă, dar ar necesita mai multe metadate și resurse. Împreună cu faptul că RingCT și adresa invizibilă NU ar fi dezvăluite, reduce și mai mult impactul.

Ar trebui remarcat faptul că articolul Wired discută ușor despre informațiile de mai sus în partea în care l-au contactat pe Riccardo "fluffyponypony" Spagni pentru comentarii, dar timpul acordat este scurt și aproape că pare să ignore această informație crucială. Lipsa de înțelegere este evidentă mai ales atunci când încerci să discuți aceste lucruri cu persoane care împărtășesc articolul cu voia întâmplării în zilele noastre.

O altă critică mult mai greu de abordat se referă la modul în care lumea exterioară vede Monero și cum se raportează aceasta la modul în care comunitatea din jurul Monero vede moneda. Pentru un exemplu în acest sens, cititorii nu trebuie să caute mai departe de titlul articolului însuși: “The Dark Web’s Favorite Currency Is Less Untraceable Than It Seems” ("Moneda preferată a Dark Web-ului este mai puțin de nedetectat decât pare").

Orice persoană care petrece o perioadă semnificativă de timp în comunitatea Monero poate atesta faptul că aceasta face eforturi mari pentru a arăta cât de greu este de obținut o confidențialitate reală, chiar în detrimentul eforturilor de marketing sau de adoptare. Dacă comunitatea oferă resurse ample în care se discută cu acuratețe despre monedă și deficiențele sale, la un moment dat, ignoranța devine vina utilizatorului care crede că moneda este tot ce are nevoie pentru a fi 100% privată.

Până în acest moment ar trebui să fie evident că comunitatea Monero ia în serios atât confidențialitatea, cât și onestitatea cu privire la punctele slabe ale acesteia și îmbunătățirile ulterioare. Articolele, precum cel în cauză, nu au deloc în vedere acest spirit de inovare în Monero. Acesta compară Monero cu droaia de alte criptomonede care fac afirmații grandioase, cu gândul doar la profit și la a profita de investitorii neinstruiți care se doresc investitori.

Realitatea nu ar putea fi mai diferită. Monero este perfect conștientă de slăbiciunile sale, caută să continue să construiască pentru a le îmbunătăți, să strângă legăturile slăbite și să atingă obiectivul foarte real, dar foarte greu de atins, de a oferi lumii o criptomonedă privată, fungibilă, care poate fi folosită de toată lumea și de a face totul într-un mod corect, descentralizat și condus de comunitate. Poate că este timpul să lăsăm deoparte senzaționalismul și împărtășirea articolelor ca mijloc de a face reclamă sacilor de bani și de a promova concurenții. Poate că este timpul să spunem o altă poveste.

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

  * [Cum va îmbunătăți CLSAG eficiența Monero](/knowledge/what-is-clsag)/

  * [De ce Monero are o emisie de coadă](/knowledge/monero-tail-emission)/

  * [O scurtă istorie a Monero](/knowledge/monero-history)/

  * [Top 15 mituri și îngrijorări legate de Monero dezmințite](/knowledge/monero-myths-debunked)/

  * [Cum păstrează Dandelion++ confidențialitatea originilor tranzacțiilor Monero](/knowledge/monero-dandelion)/

  * [De ce Monero este Open Source și descentralizat](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Mineritul Monero: Ce face ca RandomX să fie atât de special](/knowledge/monero-mining-randomx)/

  * [De ce Monero este mai bun decât Dash, Zcash, Zcoin (chiar și cu Lelantus), Grin și Bitcoin Mixers ca Wasabi (actualizat în mai 2020)](/knowledge/why-monero-is-better)/

Lecturi suplimentare