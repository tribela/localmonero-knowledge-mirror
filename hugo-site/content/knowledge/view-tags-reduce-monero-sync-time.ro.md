---
title: "Vezi etichete: Cum un singur octet va reduce timpii de sincronizare a portofelului Monero cu 40%+"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Una dintre cele mai frecvente plângeri legate de utilizarea zilnică a Monero este timpul necesar pentru a sincroniza un portofel înainte de a putea trimite Monero. Din fericire, dezvoltatorii și cercetătorii din comunitatea Monero au găsit o modalitate strălucită de a reduce timpul de sincronizare a portofelului cu peste 40%, fără a se adăuga blocaje blockchain, taxe etc.

Introduceți " view tags", o adăugare de un octet la datele fiecărei tranzacții - care va fi introdusă în Monero în următoarea actualizare a rețelei!

## De ce este sincronizarea portofelului Monero mai lentă decât cea a Bitcoin?

Una dintre primele întrebări la care trebuie să răspundem pentru a înțelege mai bine necesitatea unei soluții precum view tags este de ce sincronizarea portofelului Monero este mai lentă decât cea a criptomonedelor precum Bitcoin.

În Bitcoin, deoarece toate tranzacțiile nu sunt private și dezvăluie monedele cheltuite, sumele și adresele implicate pe lanț, portofelele Bitcoin pot căuta pur și simplu orice ieșire de tranzacție necheltuită (UTXO) sau adrese folosite pentru un anumit portofel, scanând rapid lanțul de blocuri doar pentru UTXO deținute de acele adrese pentru a afla ce monede aparțin portofelului dvs. și pot fi cheltuite.

Cu toate acestea, în Monero, toate tranzacțiile păstrează confidențialitatea utilizatorului prin ascunderea expeditorului, a destinatarului și a sumelor implicate în fiecare tranzacție. Această confidențialitate, deși este vitală pentru protejarea utilizatorilor rețelei, introduce, de asemenea, o sincronizare mai lentă a portofelului. În Monero, portofelul dvs. trebuie să compare fiecare ieșire de tranzacție (TXO) care există în rețea cu cheile private ale portofelului dvs.

Această comparație implică o mulțime de calcule matematice complexe și criptografie pentru a valida faptul că o ieșire este cu adevărat a ta, deoarece toate sumele, adresele și ieșirile (sau monedele) cheltuite sunt ascunse pe lanț în Monero.

## Ce sunt etichetele de vizualizare?

Ca o modalitate de a ajuta la reducerea timpului de sincronizare pentru portofelele Monero, [un cercetător pe nume UkoeHB a venit cu o abordare nouă](https://github.com/monero-project/research-lab/issues/73) – adaugă o "etichetă" de 1 octet la fiecare tranzacție folosind un secret comun cunoscut doar de expeditorul și destinatarul tranzacției respective.

Acest secret comun este generat de către expeditor folosind adresa furnizată de către destinatar și nu necesită o colaborare activă din partea expeditorului și a destinatarului. Primul octet (sau caracter) al acestui secret partajat este apoi adăugat la datele tranzacției atunci când aceasta este publicată în rețeaua Monero.

Atunci când unul dintre participanții la acea tranzacție dorește să-și sincronizeze portofelul cu lanțul de blocuri Monero, în loc să fie nevoie să efectueze toate calculele matematice și criptografice complexe pentru fiecare TXO din rețea, portofelul poate acum doar să verifice dacă există acel câmp de 1 octet în fiecare tranzacție și doar atunci să efectueze verificarea care necesită mult timp pentru tranzacțiile care au acea etichetă - 1/256 TXO-uri din rețea, mai exact!

Această etichetă nu dezvăluie nici o informație despre tranzacție pentru observatorii externi, adaugă doar 1 octet (o cantitate neglijabilă) la dimensiunile tranzacțiilor, și totuși ne permite să reducem timpul de sincronizare cu peste 40% prin reducerea verificărilor complexe necesare!

## Vezi tag-urile: un exemplu simplificat

Imaginați-vă că aveți 4 096 de cutii într-o cameră, din care doar 5 cutii vă aparțin. Toate cutiile sunt complet imposibil de distins din exterior, iar singura modalitate de a afla dacă o cutie vă aparține este să o deschideți și să rezolvați o problemă matematică lungă scrisă înăuntru pentru a vă asigura că este a dumneavoastră.

Acum, imaginați-vă că decideți ca persoana care vă trimite cele 5 cutii să genereze un cod special folosind adresa dvs. și apoi să pună doar primul caracter al codului generat pe partea exterioară a fiecărei cutii care vă este trimisă. Toți ceilalți fac același lucru pentru cutiile lor (pentru a se asigura că toate cutiile sunt în continuare imposibil de distins), dar acum puteți pur și simplu să vă uitați la codul cu un singur caracter de pe exteriorul cutiei și să deschideți doar acele cutii care au acel caracter pe ele.

În timp ce alte cutii se vor potrivi cu codul tău, chiar și unele care nu sunt deținute de tine, numărul de cutii pe care trebuie să le deschizi și să rezolvi o problemă de matematică este acum de numai 16 (1/256 de cutii!) în loc de toate cele 4.096.

Acum deschideți cele 16 cutii, rezolvați problemele de matematică și păstrați cele 5 cutii care vă aparțin de fapt din acel grup!

## Când vor fi disponibile etichetele de vizualizare (view tags) în Monero?

Etichetele de vizualizare (view tags) reprezintă una dintre caracteristicile planificate în prezent pentru a fi incluse în [modernizarea viitoare a rețelei](https://github.com/monero-project/meta/issues/630), și ar trebui să fie lansat în această primăvară. Comunitatea [a ridicat 23.3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (la momentul redactării) pentru a stimula dezvoltarea și punerea în aplicare a etichetelor de vizualizare și, prin urmare, marea majoritate a activității de includere a etichetelor de vizualizare în baza de cod Monero a fost deja finalizată de j-berman în colaborare cu recenzori și cercetători.

Odată ce etichetele de vizualizare vor fi aplicate de rețea, toate tranzacțiile trimise după actualizarea rețelei vor beneficia de o îmbunătățire drastică a timpului de sincronizare a portofelului. Nu va trebui să faceți nimic special pentru a începe să folosiți etichetele de vizualizare, portofelul dvs. preferat pentru Monero va începe pur și simplu să le folosească automat după actualizarea rețelei!

## Cum pot afla mai multe?

Dacă acest lucru v-a stârnit curiozitatea în ceea ce privește etichetele de vizualizare, aruncați o privire mai jos pentru câteva link-uri suplimentare care analizează în profunzime acest subiect:

  * [Reducerea timpilor de scanare cu "eticheta de vizualizare" de 1 octet pe ieșire](https://github.com/monero-project/research-lab/issues/73)
  * [Adăugați etichete de vizualizare la ieșiri pentru a reduce timpul de scanare a portofelului](https://github.com/monero-project/monero/pull/8061)

Lecturi suplimentare