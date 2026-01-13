---
title: "Cum folosește Monero hard-fork-urile pentru a moderniza rețeaua"
slug: "network-upgrades"
date: "2022-02-10"
image: "/images/upgrades.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Una dintre cele mai des neînțelese părți ale abordării Monero de a construi o criptomonedă descentralizată, care să păstreze confidențialitatea și să fie sigură este rolul pe care îl joacă bifurcațiile tari (sau actualizările de rețea).

În această postare vom trece în revistă ce sunt bifurcațiile tari, de ce sunt importante pentru Monero și ce rol puteți juca în ele în viitor.

## De ce trebuie ca Monero să continue să își modernizeze rețeaua?

Comunitatea Monero s-a angajat să itereze și să îmbunătățească proiectul de-a lungul timpului și se pare că acest angajament se rezumă la două aspecte cheie ale etosului comunității:

  1. Proiectul Monero este, în cele din urmă, un software - cod - scris de oameni. Acest lucru poate duce la necesitatea de a corecta bug-uri, de a adăuga îmbunătățiri descoperite sau inventate în timp, de a implementa modernizări ale protocolului sau pur și simplu de a întreține proiectul. Acest lucru este similar, în multe privințe, cu celelalte bucăți de software pe care le folosiți (cum ar fi browserul în care citiți aceste rânduri!), care trebuie să fie actualizate în mod constant pentru a adăuga noi caracteristici și a remedia bug-uri.

  2. Proiectul Monero este un instrument de confidențialitate, iar confidențialitatea este o cursă a înarmării în continuă evoluție. Persoanele și grupurile care nu ar dori nimic mai mult decât să răpească lumea de confidențialitate (atât financiară, cât și personală) îmbunătățesc, dezvoltă și inventează în mod constant noi modalități de a ataca abordările moderne de păstrare a confidențialității, cum ar fi cele utilizate în Monero. Pe măsură ce dușmanii confidențialității găsesc aceste noi abordări, rețeaua Monero trebuie să fie capabilă să se adapteze și să se îmbunătățească pentru a riposta și a ne apăra dreptul la confidențialitate financiară.

Proiectul Monero este, în cele din urmă, un software - cod - scris de oameni. Acest lucru poate duce la necesitatea de a corecta bug-uri, de a adăuga îmbunătățiri descoperite sau inventate în timp, de a implementa modernizări ale protocolului sau pur și simplu de a întreține proiectul. Acest lucru este similar, în multe privințe, cu celelalte bucăți de software pe care le folosiți (cum ar fi browserul în care citiți aceste rânduri!), care trebuie să fie actualizate în mod constant pentru a adăuga noi caracteristici și a remedia bug-uri.

Proiectul Monero este un instrument de confidențialitate, iar confidențialitatea este o cursă a înarmării în continuă evoluție. Persoanele și grupurile care nu ar dori nimic mai mult decât să răpească lumea de confidențialitate (atât financiară, cât și personală) îmbunătățesc, dezvoltă și inventează în mod constant noi modalități de a ataca abordările moderne de păstrare a confidențialității, cum ar fi cele utilizate în Monero. Pe măsură ce dușmanii confidențialității găsesc aceste noi abordări, rețeaua Monero trebuie să fie capabilă să se adapteze și să se îmbunătățească pentru a riposta și a ne apăra dreptul la confidențialitate financiară.

## Ce este un hard-fork (bifurcație tare)?

Complexitatea actualizării Monero intră în vigoare odată ce înțelegi cât de diferită este actualizarea unei criptomonede față de o simplă actualizare de software pentru ceva precum un browser.

În cazul criptomonedelor, regulile rețelei (cum ar fi modul în care ar trebui să arate tranzacțiile, cum funcționează mineritul și cum se verifică fiecare bloc) trebuie să fie aprobate de către rețea, ceea ce se numește "consens". Atunci când oricare dintre aceste reguli trebuie să fie schimbate sau actualizate, rețeaua trebuie să cadă de acord asupra noilor reguli, ceea ce provoacă o bifurcare tare ("hard-fork") - o situație în care rețeaua se împarte de fapt în două lanțuri de blocuri - unul pe baza vechilor reguli și altul pe baza noilor reguli.

Atunci când toată lumea din comunitate este de acord cu schimbările de reguli, se numește "hard-fork necontencios", iar lanțul care încă mai are vechile reguli se stinge și nu mai este minat după hard-fork. Acesta a fost cazul pentru aproape toate hard-fork-urile Monero, iar singura continuare a vechilor reguli a fost cea a proiectelor care au încercat să profite de pe urma hard-fork-ului.

În timp ce hard-fork-urile necontencioase sunt singura modalitate de a actualiza în mod corespunzător aspecte importante ale rețelei Monero, ele au și un efect secundar frustrant - software-ul vechi, lansat înainte ca hard-fork-ul să fie planificat, nu poate înțelege noile reguli ale rețelei și astfel nu funcționează după hard-fork! Acest lucru îi poate face pe utilizatori să creadă că fondurile sunt pierdute, că lanțul de blocuri Monero s-a oprit și că nu pot muta fonduri până când nu-și actualizează portofelul.

## Cine decide când se actualizează rețeaua Monero și ce este inclus?

Deoarece nu există o autoritate centrală, un CEO sau un președinte al Monero, munca în jurul deciziei de a decide când să actualizeze rețeaua, ce să includă și cum să facă acest lucru ce cade în sarcina _noastră_ , acei oameni din comunitatea Monero care aleg să se implice și să interacționeze! Aceasta este o parte extrem de importantă a unui proiect descentralizat, deoarece planificarea și luarea deciziilor pentru proiect este în cele din urmă descentralizată și provenită de la mulțime din partea comunității.

Planificarea calendaristică și a caracteristicilor incluse în fiecare actualizare a rețelei Monero are loc în două locuri principale:

  1. Pe IRC și Matrix, cele mai utilizate platforme de chat în comunitatea Monero (care sunt conectate împreună). Aceste platforme permit discuții în grupuri mari și sunt locul unde au loc toate întâlnirile programate ale comunității Monero, întâlnirile de dezvoltare și întâlnirile laboratoarelor de cercetare. Aceste întâlniri reprezintă cea mai bună modalitate de a asculta (sau de a contribui!) la planificarea și discuțiile în jurul actualizărilor de rețea în Monero.

  2. Pe Github, principala platformă de comunicare pentru discuții, planificare și organizare Monero de lungă durată. Comunitatea Monero folosește Github pentru a organiza întâlniri, pentru a discuta noi caracteristici și idei și pentru a coordona planificarea actualizărilor rețelei, pe lângă stocarea codului pentru proiectul Monero.

Pe IRC și Matrix, cele mai utilizate platforme de chat în comunitatea Monero (care sunt conectate împreună). Aceste platforme permit discuții în grupuri mari și sunt locul unde au loc toate întâlnirile programate ale comunității Monero, întâlnirile de dezvoltare și întâlnirile laboratoarelor de cercetare. Aceste întâlniri reprezintă cea mai bună modalitate de a asculta (sau de a contribui!) la planificarea și discuțiile în jurul actualizărilor de rețea în Monero.

Pe Github, principala platformă de comunicare pentru discuții, planificare și organizare Monero de lungă durată. Comunitatea Monero folosește Github pentru a organiza întâlniri, pentru a discuta noi caracteristici și idei și pentru a coordona planificarea actualizărilor rețelei, pe lângă stocarea codului pentru proiectul Monero.

Dacă aveți o idee importantă pentru o modernizare a rețelei, dacă nu vă place o abordare adoptată sau dacă sunteți îngrijorat cu privire la planificarea unei modernizări, este important să vă exprimați și să vă prezentați cazul în mod clar în fața comunității!

## Cum pot ajuta la modernizarea rețelei?

Deoarece actualizările rețelei Monero necesită coordonarea și aprobarea comunității împreună cu actualizările de software, este extrem de important ca un număr cât mai mare de persoane să se implice în procesul de planificare, testare și comunicare a actualizărilor rețelei.

Iată câteva modalități simple prin care puteți ajuta la îmbunătățirea rețelei:

  1. Participați la reuniunile de planificare [publicate pe Github](https://github.com/monero-project/meta/issues), ascultați și contribuiți dacă aveți ceva relevant de adus în discuție.
  2. Comunicați detaliile legate de planificarea actualizării rețelei (după ce se va decide!) către exchange-ul, portofelul sau pool-ul minier preferat. Poate fi complicat să notificăm în mod corespunzător toți utilizatorii Monero cu privire la o actualizare, așa că este important să ajutăm cu toții, acolo unde putem, pentru a răspândi vestea.
  3. Testați software-ul înainte de actualizarea rețelei. Se va lansa un apel pentru testeri înainte de actualizarea rețelei, atât pe testnet, cât și pe stagenet, pentru a se asigura că fiecare aspect al actualizării a fost planificat și implementat în mod corespunzător în software. Cu cât mai multe persoane se implică și testează cu atenție noile versiuni, cu atât mai multe șanse ca actualizarea rețelei să se desfășoare fără probleme!
  4. Odată ce sunt publicate versiunile compatibile cu actualizarea rețelei, asigurați-vă că faceți actualizarea imediat! Cu cât mai multe persoane sunt actualizate și pregătite pentru actualizarea rețelei, cu atât mai ușor va fi gestionată rețeaua și cu atât mai puține dureri de cap vor avea utilizatorii.

## La ce mă pot aștepta la următoarea actualizare a rețelei Monero?

Deși nu există încă o dată fixată în piatră, va avea loc în curând o actualizare a rețelei pentru a implementa câteva actualizări și caracteristici cheie în Monero:

  1. O creștere a mărimii inelului de la 11 la 16, crescând setul de anonimat de bază (a se citi: negare plauzibilă sau confidențialitate de bază) al fiecărei tranzacții din rețea.
  2. [Vizualizarea etichetelor, o modalitate strălucită de a reduce timpul de sincronizare a portofelului cu 30-40%.](https://localmonero.co/knowledge/view-tags-reduce-monero-sync-time)
  3. Modificări ale taxelor, îmbunătățind securitatea și rezistența rețelei la schimbările rapide de pe piața taxelor sau la atacurile unor entități rău intenționate.
  4. [Bulletproofs+, o nouă îmbunătățire a eficienței tranzacțiilor Monero](https://www.getmonero.org/2020/12/24/Bulletproofs+-in-Monero.html)

Aceste schimbări vor contribui în mare măsură la creșterea confidențialității, eficienței și securității rețelei, deschizând în același timp calea către [Seraphis](https://localmonero.co/knowledge/seraphis-for-monero), protocolul de tranzacționare de ultimă generație pentru Monero.

## Cum pot afla mai multe?

Subiectul hard-fork-urilor și al actualizărilor de rețea este unul vast și există o istorie lungă și istorică a acestora în Monero, așa că nu uitați să accesați unele dintre următoarele link-uri dacă doriți să aflați mai multe despre istoria, procesul sau planificarea în curs pentru viitoarea actualizare a rețelei!

  * [Monero v15 planificare hard-fork](https://github.com/monero-project/meta/issues/630)
  * [Actualizări software programate (în Monero)](https://github.com/monero-project/monero#scheduled-software-upgrades)
  * [O notă privind actualizările de protocol programate](https://web.getmonero.org/2020/09/01/note-scheduled-upgrades.html)

Lecturi suplimentare