---
title: "Seraphis: Ce va face pentru Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: un upgrade de design modular pentru tranzacțiile Monero

Această postare descrie [Seraphis](https://github.com/UkoeHB/Seraphis), un set de structuri și abstracțiuni ale protocoalelor de tranzacționare dezvoltate de un colaborator pseudonim în domeniul cercetării [`koe`](https://github.com/UkoeHB) pentru ecosistemul Monero, și cu o analiză de securitate în curs de desfășurare de către un contribuitor pseudonim [`coinstudent2048`](https://github.com/coinstudent2048).  
Facem unele simplificări și omitem anumite detalii tehnice din motive de claritate; din acest motiv, și pentru că proiectarea Seraphis este încă în curs de desfășurare, cititorii interesați ar trebui să consulte documentația Seraphis pentru cele mai recente informații.

## Tranzacții în Monero

Protocoale precum Bitcoin și Monero și altele se bazează pe un așa-numit "model de ieșire" de funcționare, unde o _ieșire_ este o reprezentare a valorii care poate fi transferată.  
Tranzacțiile consumă una sau mai multe ieșiri controlate de un expeditor și generează noi ieșiri direcționate către destinatari (sau înapoi la expeditor sub formă de schimbare); tranzacția trebuie să fie echilibrată în sensul că ieșirile consumate trebuie să conțină o valoare totală exact egală cu valoarea noilor ieșiri (plus o taxă impusă de rețea).  
În multe protocoale, cum ar fi Bitcoin, valoarea conținută într-o ieșire este scrisă în clar, la fel ca și destinatarul.  
În plus, prin consultarea blockchain-ului, este banal să se vadă dacă și când a fost cheltuită o ieșire (adică dacă a fost consumată într-o tranzacție ulterioară și ce tranzacție a cheltuit-o).

În schimb, protocoale precum Monero introduc un design diferit:

  * Valorile de ieșire sunt ascunse și nu sunt vizibile pe blockchain
  * Adresele destinatarilor sunt ascunse prin utilizarea unui protocol de adresare unică.
  * Utilizarea unor semnături ambigue nu permite să se știe dacă o ieșire a fost sau nu cheltuită.

Rezultatul este că, în absența unor informații externe, este dificil să se stabilească dacă un anumit produs a fost cheltuit, care este valoarea acestuia și cine este destinatarul său.

Actualul protocol de tranzacționare Monero se numește _RingCT_ și utilizează mai multe blocuri criptografice pentru a atinge aceste obiective de proiectare.

  * _Angajamentele_ ascund sumele într-un mod util din punct de vedere matematic
. 
  * _Probele de gamă_ previn revărsarea care ar putea umfla oferta
  * _Semnături inelare cu legături_ asigură ambiguitatea semnatarului și previne încercările de cheltuire dublă
  * _Compensațiile de angajament_ afirmă că tranzacțiile se echilibrează
. 

Aceste elemente constitutive sunt întrepătrunse cu grijă pentru a construi protocolul RingCT.

O proprietate utilă a protocolului RingCT constă în faptul că unele elemente constitutive pot fi modificate sau îmbunătățite într-un mod care păstrează intacte designul și proprietățile generale, dar care pot aduce îmbunătățiri în ceea ce privește eficiența sau securitatea. De fapt, aceste tipuri de actualizări au avut loc (sau sunt planificate să aibă loc) de mai multe ori în istoria Monero. Dovezile de interval din protocolul original RingCT erau voluminoase și lente; acestea au fost actualizate ulterior la o construcție numită [Bulletproofs](https://eprint.iacr.org/2017/1066) care a făcut ca tranzacțiile să fie mai mici și mai rapide, cu o analiză de securitate mai bună, și sunt planificate pentru a fi actualizate la o construcție mai nouă numită [Bulletproofs+](https://eprint.iacr.org/2020/735) pentru beneficii și mai mari în materie de eficiență.

Un proces similar a fost efectuat cu blocul de construcție al semnăturii inelare cu legături. În protocolul original, o construcție numită [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34) a fost folosită. Aceasta a fost ulterior actualizată la o construcție mai nouă numită [CLSAG](https://eprint.iacr.org/2019/654) care este mai rapidă, are ca rezultat tranzacții mai mici și dispune de o analiză de securitate mai bună. O construcție și mai nouă de semnătură inelară cu legături bazată pe [Triptych](https://eprint.iacr.org/2020/018) a fost propusă, dar aceasta nu a fost selectată pentru implementare din cauza impactului său asupra operațiunilor cu mai multe semnături.

## Seraphis

Seraphis duce această idee cu un pas mai departe.  
În loc să actualizeze elementele constitutive individuale ale protocolului de tranzacționare RingCT existent, acesta introduce un protocol diferit care poate profita de diferite elemente constitutive și poate oferi o funcționalitate îmbunătățită.

## Blocuri de construcție

Seraphis utilizează un set diferit de blocuri criptografice pentru a-și atinge obiectivele de proiectare.

  * _Angajamentele_ ascund încă sumele
. 
  * _Dovezile de gamă_ previn încă depășirea și inflația de aprovizionare
  * _Dovezile de apartenență_ asigură ambiguitatea semnatarului
  * _Compensațiile de angajament_ încă mai afirmă echilibrul
. 
  * _Dovezile de autorizare_ previn încercările de cheltuieli duble

Observați schimbarea de aici: semnăturile inelare legate sunt înlocuite cu o combinație de dovezi de apartenență și dovezi de autorizare. În linii mari, dovezile de apartenență arată că o ieșire consumată face parte dintr-un set mai mare, similar cu ceea ce se întâmplă în RingCT. Dar, spre deosebire de RingCT, dovezile de apartenență nu implică deloc eticheta de legătură! Dovezile de autorizare arată că eticheta de legătură este validă și sunt utilizate pentru a semna tranzacția finală.

Deoarece RingCT integrează eticheta de legătură în semnătura ambiguă, operațiunile de semnare (și cele cu mai multe semnături) sunt mai intensive din punct de vedere computațional și devine mai dificil să se creeze alte funcționalități legate de etichete. Dar în Seraphis, construirea dovezilor de apartenență poate fi delegată în siguranță de la dispozitive de mare încredere (care pot avea o putere de calcul limitată, cum ar fi un portofel hardware) la un dispozitiv mai puțin de încredere, iar operațiunile de semnare (și de semnătură multiplă) sunt mult mai ușoare folosind dovada de autorizare mult mai simplă.

Din fericire, unele dintre elementele constitutive necesare pentru Seraphis există deja în altă parte și nu trebuie să fie proiectate de la zero. Atât construcțiile Bulletproofs, cât și Bulletproofs+ pot fi folosite ca dovezi de interval. Modificările aduse sistemelor de demonstrație de tip Schnorr pot fi utilizate pentru a autoriza dovezi. Și un sistem eficient [de dovedire](https://eprint.iacr.org/2015/643) folosit deja ca bază pentru Triptych, [Lelantus](https://eprint.iacr.org/2019/373), și [Spark](https://eprint.iacr.org/2021/1173)* poate fi modificat pentru dovezile de apartenență.

* Cypher Stack primește finanțare pentru dezvoltarea Spark.

## Adresându-se la

Din păcate, adresele Monero utilizate în prezent nu sunt compatibile cu Seraphis. În cazul în care Seraphis ar fi implementat, utilizatorii ar trebui să genereze noi adrese din cheile portofelului lor pentru a primi Monero. Cu toate acestea, acest cost de ecosistem vine cu o serie de beneficii.

În afară de avantajele structurale discutate mai sus, designul Seraphis se pretează la mai multe posibilități de construcție a adreselor, fiecare dintre acestea venind la pachet cu compromisuri. În timp ce construcția finală a adresei care va fi utilizată în Seraphis este [încă în curs de decizie](https://github.com/monero-project/research-lab/issues/92) (o schemă care se bucură de multă atenție se numește [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), putem descrie câteva caracteristici comune și utile.

Poate că știți că adresele Monero oferă funcționalitatea _cheie de vizualizare_ , prin care puteți furniza o cheie de vizualizare unui dispozitiv sau unei terțe părți și îi permite să urmărească ieșirile primite în numele dumneavoastră, dar fără a renunța la autoritatea de cheltuire. Acest lucru este util pentru portofele, care pot rămâne actualizate în timp ce vă păstrați cheia de cheltuieli în siguranță. De asemenea, este util pentru cazurile în care doriți acces extern la vizualizare, cum ar fi o organizație caritabilă publică care oferă transparență sau o companie cu un departament de contabilitate.

Dezavantajul cheilor de vizualizare Monero este că nu oferă acces complet sau fin la vizualizare. Nu este posibilă detectarea fiabilă a momentului în care un portofel cheltuiește fonduri, ceea ce face dificilă calcularea corectă a soldurilor portofelului atunci când cheia de cheltuieli nu este disponibilă. De asemenea, în prezent, nu este posibil să se detecteze ieșirile primite fără a afla și valoarea conținută în aceste ieșiri (ceea ce înseamnă că orice terți responsabili de găsirea ieșirilor primite vor afla exact cât Monero achiziționați).

Construcțiile de adresare Seraphis pot rezolva această problemă. Cu Seraphis, adresa dvs. este echipată cu diferite chei care pot face lucruri diferite:

  * Urmăriți ieșirile primite, dar ascundeți valoarea lor
  * Urmăriți ieșirile primite, dar arătați valoarea lor
  * Urmăriți ieșirile de ieșire
  * Vă ajută să generați tranzacții, dar nu să le semnați
  * Generarea de noi adrese (util pentru comercianții sau pentru exchange-urile cu mulți clienți)

În calitate de deținător al adresei, puteți decide câtă autoritate delegați altor dispozitive sau părți terțe.

## Imaginea de ansamblu

Seraphis reprezintă o schimbare majoră în ecosistemul Monero. Deși implică modificări ale adreselor și ale blocurilor de construcție ale tranzacțiilor, designul său oferă flexibilitate și funcționalități utile care nu sunt posibile cu protocolul RingCT actual. În timp ce o mare parte din design este finalizat și este dezvoltat [într-o implementare](https://github.com/UkoeHB/monero/tree/seraphis_lib), proiectarea adreselor și analiza de securitate sunt în curs de desfășurare. Seraphis oferă o oportunitate excelentă de a împinge ecosistemul Monero înainte!

Lecturi suplimentare