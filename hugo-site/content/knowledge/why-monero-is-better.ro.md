---
title: "De ce Monero este mai bun decât Dash, Zcash, Zcoin (chiar și cu Lelantus), Grin și Bitcoin Mixers ca Wasabi (actualizat în mai 2020)"
slug: "why-monero-is-better"
date: "Sat Feb 01"
image: "/images/why-monero.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Nu toate monedele centrate pe confidențialitate pot oferi 100% confidențialitate, nedetectabilitate, securitate și fungibilitate într-o monedă 100% descentralizată cu o configurație lipsită de încredere. Iată care sunt aceste atribute și de ce sunt importante:

Privat
    Finanțele dumneavoastră nu sunt vizibile pentru public. O persoană care se uită la blockchain-ul monedei nu va putea vedea câți bani aveți.
Nedetectabil
    Monedele nu pot fi urmărite prin analiza blockchain sau prin monitorizarea blockchain.
Securizat
    Toate tranzacțiile sunt criptate, iar portofelul în care se află fondurile dumneavoastră este criptat.
Fungibil
    Toate monedele sunt egale și au aceeași valoare.
Descentralizat
    Toate nodurile (un nod este o instanță de funcționare a blockchain-ului monedei) din rețea sunt egale. Nu există o superclasă de noduri care să aibă mai multă influență sau control asupra tranzacțiilor sau a sistemului decât alte noduri.

## Analiza monedelor

Iată o analiză a criptomonedelor bine cunoscute care pretind că anonimatul și/sau imposibilitatea de a fi urmărite reprezintă principalul lor diferențiator. Bitcoin în sine nu intră în sfera de aplicare a acestei analize, deoarece nu a pretins niciodată că este anonimă.

Acest site a fost creat de utilizatorii Monero. A fost o vreme când nu eram utilizatori Monero, dar eram preocupați de confidențialitatea financiară. Am cercetat monedele care pretindeau că sunt private, iar această pagină este rezultatul cercetărilor noastre. Acesta este motivul pentru care am ales Monero în detrimentul celorlalte. Așadar, dacă părem părtinitori, suntem, dar credem că această părtinire se bazează pe fapte pe care le puteți citi mai jos și le puteți verifica singuri.

### Prezentare generală

Selectați un logo pentru a trece la analiza monedei respective.

| Privat| Nedetectabil| Securizat| Fungibil| Descentralizat  
---|---|---|---|---|---  
Monero| Da| Da| Da| Da| Da  
DASH| Nu| Nu| Da| Nu| Nu  
Zcash| Nu| Nu în totalitate| Da| Nu| Nu  
| Da| Da| Da| Da| Nu  
| Uneori| Nu| Da| Nesigur| Da  
Bitcoin mixers| Nu| Nu| Da| Nu| Uneori  
  
### Monero

Privat
    Monero folosește un sistem criptografic solid care vă permite să trimiteți și să primiți fonduri fără ca tranzacțiile dvs. să fie vizibile public pe blockchain (registrul distribuit al tranzacțiilor). Acest lucru garantează că achizițiile, încasările și alte transferuri ale dvs. rămân **private în mod implicit**. Expeditorul, destinatarul și suma tranzacției sunt private. Unele monede au o "listă bogată" care permite oricui să vadă care este contul care are cele mai multe monede. Deoarece Monero este privat, nu poate exista o [listă de bogătași](http://moneroblocks.info/richlist) Monero.
Nedetectabil
    Profitând de semnăturile inelare (o proprietate specială a anumitor tipuri de criptografie), Monero permite tranzacții nedetectabile. Acest lucru înseamnă că este ambiguu ce fonduri au fost cheltuite și, prin urmare, este extrem de puțin probabil ca o tranzacție să poată fi legată de un anumit utilizator.
Securizat
    Prin intermediul unei rețele distribuite de consens peer-to-peer, fiecare tranzacție este securizată criptografic. Conturile individuale au o sămânță mnemonică de 25 de cuvinte afișată în momentul creării, care poate fi scrisă pentru a face o copie de siguranță a contului. O parolă este obligatorie la crearea unui portofel, iar fișierele contului sunt criptate cu o frază de trecere pentru a se asigura că nu au nicio valoare dacă sunt furate.
Fungibil
    Toate monedele sunt egale și au aceeași valoare. Un utilizator, un vânzător sau orice altă entitate nu poate bloca sau pune pe lista neagră anumite monede Monero, deoarece istoricul tranzacțiilor cu monede Monero este ambiguu.
Descentralizat
    Toate nodurile Monero sunt egale. Nu există o superclasă de noduri care să aibă mai multă influență sau control asupra tranzacțiilor decât alte noduri. Nicio persoană sau entitate nu poate urmări tranzacțiile prin deținerea mai multor noduri. În plus, nu există o configurație de încredere. Acest lucru înseamnă că necesitatea de a avea încredere într-o persoană sau entitate nu este un factor. Singurele lucruri care trebuie să fie de încredere sunt codul sursă (care poate fi verificat de oricine) și matematica.

Monero a fost 100% open source încă de la începuturile sale, ceea ce înseamnă că oricine poate vedea [ codul sursă ](https://github.com/monero-project/bitmonero) pentru a verifica dacă nu există backdoors și dacă software-ul este sigur.

Monero are de asemenea [ lucrări de cercetare recenzate de colegi ](https://lab.getmonero.org/) care verifică matematic și sistematic toate proprietățile sale enumerate mai sus.

### DASH

Privat
    

DASH are o [ listă bogată](https://bitinfocharts.com/top-100-richest-darkcoin-addresses.html), deci nu este o monedă privată. Detaliile financiare ale adreselor de monede sunt vizibile pentru oricine examinează blockchain-ul.

> DASH nu este deloc privat din punct de vedere criptografic. De fapt, am avut un slide în pachet care spunea "DASH, LOL" și, ca și nimic altceva... este un fel de ulei de șarpe și, personal, nu prea îmi place. 
> 
> **Gregory Maxwell** , dezvoltator și criptograf Bitcoin Core, într-o prezentare [ la Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

**Peter Todd** , un alt dezvoltator și criptograf Bitcoin Core, a făcut o declarație similară [](https://twitter.com/petertoddbtc/status/622022840330682368).

Nedetectabil
    Tranzacțiile sunt direcționate printr-o serie de [ Masternode-uri ](https://www.dash.org/masternodes/) pentru a le face nedetectabile. Această practică ar putea funcționa dacă toți operatorii de noduri principale ar avea doar motive pure. Cu toate acestea, dacă un guvern, un grup de hackeri, o altă entitate sau chiar un individ ar cumpăra mai multe noduri master (nu ar exista nicio modalitate de a ști dacă acest lucru s-a întâmplat) și dacă tranzacția ar trece printr-o rută în care toate nodurile master ar fi deținute de acea entitate, atunci tranzacția ar putea fi urmărită de acea entitate. Având în vedere costul relativ scăzut al masternodurilor și bugetul enorm al guvernelor și al unor organizații, posibilitatea ca monedele să poată fi urmărite este reală.
Securizat
    Tranzacțiile sunt sigure din punct de vedere criptografic.
Fungibil
    Deoarece tranzacțiile nu sunt private, există posibilitatea ca o entitate să blocheze sau să pună pe lista neagră anumite monede, făcându-le mai puțin valoroase decât celelalte. A se vedea nota de mai jos privind lipsa de fungibilitate a Bitcoin, deoarece același principiu se aplică și în cazul DASH.
Descentralizat
    Nu toate nodurile DASH sunt egale. Există o superclasă de noduri, numită _Masternodes_ ai căror proprietari au o influență mai mare asupra sistemului decât operatorii de noduri obișnuite. Acest lucru face ca DASH să fie un sistem semicentralizat în loc de un sistem ideal 100% descentralizat.

### Zcash

Privat
    

Tranzacțiile Zcash sunt vizibile pe blockchain-ul lor. Ei permit tranzacții ascunse, dar [ mai puțin de 1% din tranzacții sunt complet protejate ](http://stat.bloxy.info/superset/dashboard/zcash/) . Deoarece tranzacțiile ascunse sunt opționale și nu sunt implicite (ca să nu mai spunem că sunt rar folosite), [ tranzacțiile ascunse ies în evidență pe blockchain ](http://weuse.cash/2016/06/09/btc-xmr-zcash/), atrăgând atenția asupra lor.

> Și apropo, cred că putem determina cu succes ca Zcash să fie prea ușor de urmărit pentru infractori precum WannaCry, dar să rămână complet privat și & fungibil. 
> 
> **Zooko Wilcox** , CEO Zcash, într-un [ tweet ](https://twitter.com/zooko/status/863202798883577856)

Dacă Zcash poate fi "prea ușor de urmărit", atunci nu poate fi complet privat sau fungibil. 

Nedetectabil
    

Tranzacțiile obișnuite sunt transparente. Tranzacțiile ascunse utilizează zk-SNARKS, care au garanții de confidențialitate solide în anumite condiții. Întrebarea este dacă aceste condiții sunt îndeplinite și, având în vedere numărul infim de persoane care utilizează capacitățile protejate, acest lucru rămâne sub semnul întrebării.

Securizat
    Tranzacțiile sunt sigure din punct de vedere criptografic.
Fungibil
    Deoarece toate tranzacțiile nu sunt private, există posibilitatea ca o entitate să blocheze sau să pună pe lista neagră anumite monede, făcându-le mai puțin valoroase decât celelalte. A se vedea nota de mai jos privind lipsa de fungibilitate a Bitcoin, deoarece același principiu se aplică și în cazul Zcash.
Descentralizat
    

Zcash este o companie și în prezent [ ia 20% din toate ZEC-urile extrase ca recompensă a fondatorului](https://z.cash/blog/funding.html). 

Zcash a avut nevoie de un **Sistem de Încredere**. Acest lucru înseamnă că trebuie să aveți încredere că sistemul a fost creat în mod onest. Dacă nu a fost creat în mod onest, [ ar putea fi create cantități nelimitate de ZEC fără ca nimeni să știe](https://blog.okturtles.com/2016/03/the-zcash-catch/). Acest lucru l-ar îmbogăți pe hacker și ar devaloriza ZEC. Nu există nicio modalitate de a ști dacă Configurarea de încredere a fost executată în mod onest. Trebuie să îi credem pe cuvânt. Acest lucru introduce un punct de eșec uman în sistem, ceea ce este contrar aproape tuturor celorlalte criptomonede. În criptomonede ar trebui să aveți încredere doar în matematică și în codul sursă verificabil, nu în oameni. Așa cum am văzut cu aproape toate companiile mari de software, cum ar fi [ Microsoft](https://www.gnu.org/proprietary/proprietary-back-doors.en.html), [ Apple](http://www.digitaltrends.com/computing/apple-vs-fbi-backdoor-to-data-already-exists/), și chiar și guvernele, nu ar trebui să fie de încredere. 

Peter Todd, un dezvoltator Bitcoin Core care [ a participat ](https://github.com/zcash/mpc/blob/master/README.md) la Configurarea de încredere Zcash, a numit-o un " [ backdoor ](https://twitter.com/petertoddbtc/status/793584540891643906) ". 

> Zcash nu este necondiționat solid, nu poate fi cu tehnologia actuală... necesită o configurare de încredere… va trebui să refacem procedura [Trusted Setup] pentru a actualiza criptografia în timp, deci este o vulnerabilitate. 
> 
> Gregory Maxwell, dezvoltator Bitcoin Core și criptograf, într-o [ prezentare la Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

**Notă:** Zcoin trece de la schema sa actuală Sigma la un nou protocol care se bazează pe noua sa lucrare, Lelantus. Lelantus va fi implementat în etape, iar acest articol va presupune că toate etapele sunt complete și implementate pentru comparații adecvate alături de termenele de implementare proiectate.

Motivul pentru care Zcoin și-a permis acest lux de a fi judecat pe baza viitorului său protocol, și nu Zcash, este că Zcoin are o foaie de parcurs cu termene generale de activare, în timp ce planurile de "confidențialitate implicită" ale Zcash sunt și continuă să fie nebuloase.

Privat
    

Zcoin (XZC) nu va avea o listă de bogătași, deci va fi privată. În mod implicit, confidențialitatea obligatorie este așteptată să intre în funcțiune în 2021. Odată implementată, o listă de bogăție nu va putea fi creată (deși în prezent [ei au unul](https://www.coinexplorer.net/XZC/richlist)).

Nedetectabil
    Odată cu implementarea etapei finale a Lelantus în 2021, Zcoin nu ar trebui să poată fi urmărit, deși atacurile teoretice nu au fost încă explorate, deoarece nu a fost încă lansat sau nu a avut timp să fie în spațiul public. În prezent, Zcoin este trasabil dacă se pune un [Adresa Zcoin](https://explorer.zcoin.io/) într-un explorator blockchain și puteți vedea soldul și tranzacțiile aferente.
Securizat
    Tranzacțiile sunt sigure din punct de vedere criptografic.
Fungibil
    După ce etapa finală a Lelantus va fi lansată în 2021, se presupune că Zcoin va fi fungibil datorită aplicării obligatorii a confidențialității. În acest sens, va fi un adevărat concurent pentru Monero. Cu toate acestea...
Descentralizat
    Zcoin a implementat Znode, care acționează în mod similar cu masternode Dash și au o putere mai mare decât alte noduri din rețea. Deoarece nu toate nodurile sunt create în mod egal, iar factorul de diferențiere între ele este suma de bani de care dispune o persoană (Znodes costă 1000 XZC), rețeaua este semicentralizată.

Privat
    Grin nu are o listă de bogătași, ceea ce ar indica o anumită formă de confidențialitate. Într-adevăr, atacatorii pasivi care scanează lanțul nu pot vedea ce adresă conține câți bani, parțial pentru că sumele sunt ofuscate prin intermediul tranzacțiilor confidențiale, parțial pentru că datele privind adresele nu sunt stocate în lanț și parțial datorită tehnologiei cut-through a Mimblewimble, prin care tranzacțiile intermediare pot fi eliminate din lanț, lăsând puține metadate din tranzacțiile anterioare.
Nedetectabil
    Grin nu se apără împotriva unui atacator activ care construiește un grafic de tranzacții. Este posibil ca atât minerii, cât și un nod ușor modificat să urmărească fiecare tranzacție, să o salveze înainte ca tehnologia "cut-through" să intre în funcțiune și să construiască de aici un grafic complet al tranzacțiilor, păstrând toate datele "cut-through". Ei nu ar putea discerne nicio informație înainte de momentul în care încep, dar tot ceea ce se întâmplă după ce încep va reprezenta metadate valoroase cu care ar putea lega tranzacțiile.
Securizat
    Tranzacțiile sunt sigure din punct de vedere criptografic.
Fungibil
    Deoarece toate tranzacțiile sunt în mod îndoielnic private și pot fi urmărite, există posibilitatea de a construi un grafic al tranzacțiilor, din care se pot extrage informații valoroase care pot fi folosite împotriva unei persoane în ceea ce privește obiceiurile sale de consum. Ieșirile pot fi apoi legate de identități și, chiar dacă sumele nu sunt vizibile, faptul că o ieșire poate fi legată de o identitate înseamnă că ieșirea poate fi afectată, doar pe baza persoanei care a deținut-o. Considerăm că acest lucru înseamnă că Grin nu este fungibil, deoarece unele ieșiri pot fi afectate, iar altele nu.
Descentralizat
    Grin nu are nici o premină, recompensă de fondator, masternode sau trezorerie. Nu au avut un ICO și sunt administrați într-un mod care se potrivește unei comunități descentralizate. Grin este descentralizat.

### Bitcoin Mixers

Privat
    

Toate tranzacțiile Bitcoin sunt vizibile pe blockchain și există o [ listă cu cei bogați în Bitcoin](http://www.bitcoinrichlist.com/top100), deci Bitcoin nu este privat. Bitcoin este [ pseudoanonim ](https://bitcoin.org/en/you-need-to-know), nu anonim. 

Pentru **mixerele Bitcoin** , trebuie să aveți încredere că își pot păstra datele în siguranță și că nu sunt deținute de, sau nu cooperează cu un guvern, hackeri sau alte entități. 

În iulie 2017, fondatorul celui mai mare serviciu de mixare a Bitcoin, BITMIXER.IO, a anunțat că se închide și a dat acest motiv: 

> … Acum am înțeles că Bitcoin este un sistem transparent și non-anonimic **prin design**. Blockchain este o mare carte deschisă… 
> 
> BITMIXER.IO, într-un anunț de închidere pe [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (sublinierea în original). 

Câteva săptămâni mai târziu, după ce a luat în considerare diferitele monede centrate pe confidențialitate, a spus următoarele: 

> După o investigație aprofundată, confirm că MONERO este cea mai bună monedă de confidențialitate. Așadar, recomand cu tărie MONERO tuturor celor care au nevoie de un plus de confidențialitate. 
> 
> BITMIXER.IO, într-un [ post următor](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Nedetectabil
    

Deoarece toate tranzacțiile Bitcoin sunt vizibile pe blockchain, TOATE tranzacțiile Bitcoin pot fi urmărite. Un mixer Bitcoin poate ascunde foarte mult tranzacțiile, ceea ce face mult mai dificilă urmărirea Bitcoin, dar nu imposibilă. Pe măsură ce tehnologia progresează și companiile specializate în urmărirea tranzacțiilor Bitcoin devin mai răspândite, tranzacțiile odată foarte ofuscate vor deveni relativ ușor de urmărit: 

  * [ Forțele de ordine continuă să investească în serviciile de urmărire Bitcoin ](https://news.bitcoin.com/law-enforcement-continues-invest-bitcoin-tracking-services/)
  * [ Time.com: Bitcoini sunt mai ușor de urmărit decât crezi ](http://time.com/3689359/bitcoins-track-anonymous/)
  * [ Elliptic: O companie specializată în urmărirea Bitcoin pentru aplicarea legii ](https://www.elliptic.co/)

O căutare pe Google va scoate la iveală zeci de articole ca cele de mai sus. Și nu uitați că orice tranzacție care a avut loc în orice moment în trecut se află în blockchain și poate fi urmărită, chiar dacă a fost folosit un serviciu de mixare. De fapt, utilizarea unui serviciu de mixare este posibil să atragă atenția asupra acelor tranzacții. 

Securizat
    Tranzacțiile sunt sigure din punct de vedere criptografic.
Fungibil
    

Nu toți Bitcoinii sunt egali și nu au aceeași valoare. Unii Bitcoini au fost trecuți pe lista neagră și blocați de mai multe entități, ceea ce face ca monedele respective să fie mai puțin valoroase decât restul. Dacă primiți Bitcoini care au fost folosiți în trecut în scopuri ilegale, atunci Bitcoinii dvs. ar putea fi trecuți pe lista neagră, chiar dacă nu ați avut nimic de-a face cu activitatea ilegală. Sau, să spunem că un guvern, un angajator sau o altă entitate decide să vă treacă pe lista neagră a Bitcoinilor în viitor, la fel cum se procedează în cazul înghețării sau confiscării activelor. Nu ați putea face nimic. Deoarece un mixer nu face decât să îngreuneze urmărirea Bitcoins, această categorie a fost marcată ca "nu este fungibil." 

  * Andreas Antonopoulos, un fost dezvoltator Bitcoin Core care este foarte respectat în Bitcoin și în alte comunități de criptomonede, recunoaște problema fungibilității Bitcoin într-un [ videoclip YouTube](https://www.youtube.com/watch?v=ak1iojpiHpM&feature=youtu.be&t=33m9s). 
  * Discuția despre problema fungibilității Bitcoin pe [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=1190707.0)

Descentralizat
    Bitcoin în sine este descentralizat, dar majoritatea serviciilor de mixare sunt centralizate. Acest lucru înseamnă că trebuie să aveți încredere în ele. Totuși, unele mai noi, precum Wasabi wallet, nu sunt.

## Rezumat

În opinia noastră, Monero este alegerea evidentă dacă căutați o criptomonedă privată, sigură, de neurmărit, fungibilă, descentralizată, pentru care nu este necesară nicio configurare de încredere. Orice altceva pune în pericol intimitatea și securitatea dvs. Dar nu vă bazati doar pe opinia noastră. Faceți-vă propriile cercetări și vedeți singuri. Luați în considerare faptul că Monero este aprobat și folosit de entități care depind de intimitate și imposibilitatea de a fi urmărit, cum ar fi:

  * [ SIGAINT ](https://www.reddit.com/r/Monero/comments/4xqrzd/sigaint_launches_tor_monero_node_as_its_operators/)
  * [ Purism ](https://puri.sm/posts/purism-collaborates-with-cryptocurrency-monero-to-enable-mobile-payments/)
  * [ Wikileaks ](https://shop.wikileaks.org/donate#db9)
  * AlphaBay Market (AB) a fost închis în iulie 2017. [ Plângerea federală de confiscare ](https://assets.documentcloud.org/documents/3898109/AlphaBay-Cazes-Forfeiture-Complaint.pdf) împotriva AB arată că: 
    * **Monero este singura criptomonedă privată și de neurmărit:**   
"În total, din portofelele lui CAZES și computerul agenților a fost preluată controlul asupra aproximativ 8,800,000 de dolari în Bitcoin, Ethereum, Moreno [sic] și Zcash, după cum urmează: 1,605.0503851 Bitcoin, 8,309.271639 Ethereum, 3,691.98 Zcash, _și o sumă necunoscută de Monero._ " (la sfârșitul paginii 20 și începutul paginii 21, accent adăugat) 
    * **Tranzacțiile cu Bitcoin nu sunt private și pot fi urmărite:**   
"Agenții federali au obținut mandatele după ce au urmărit un număr de tranzacții Bitcoin care începeau cu AlphaBay, conducând la conturi de monede digitale, iar în final la conturi bancare și alte active tangibile, deținute de CAZES și soția lui." (p. 17, liniile 24-26) 

LocalMonero nu susține sau nu încurajează nicio activitate ilegală. 

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

  * [Revista Wired se înșeală în legătură cu Monero, iată de ce](/knowledge/wired-article-debunked)/

  * [Top 15 mituri și îngrijorări legate de Monero dezmințite](/knowledge/monero-myths-debunked)/

  * [Cum păstrează Dandelion++ confidențialitatea originilor tranzacțiilor Monero](/knowledge/monero-dandelion)/

  * [De ce Monero este Open Source și descentralizat](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Mineritul Monero: Ce face ca RandomX să fie atât de special](/knowledge/monero-mining-randomx)/

Nu toate monedele centrate pe confidențialitate pot oferi 100% confidențialitate, nedetectabilitate, securitate și fungibilitate într-o monedă 100% descentralizată cu o configurație lipsită de încredere. Iată care sunt aceste atribute și de ce sunt importante:

## Analiza monedelor

Iată o analiză a criptomonedelor bine cunoscute care pretind că anonimatul și/sau imposibilitatea de a fi urmărite reprezintă principalul lor diferențiator. Bitcoin în sine nu intră în sfera de aplicare a acestei analize, deoarece nu a pretins niciodată că este anonimă.

Acest site a fost creat de utilizatorii Monero. A fost o vreme când nu eram utilizatori Monero, dar eram preocupați de confidențialitatea financiară. Am cercetat monedele care pretindeau că sunt private, iar această pagină este rezultatul cercetărilor noastre. Acesta este motivul pentru care am ales Monero în detrimentul celorlalte. Așadar, dacă părem părtinitori, suntem, dar credem că această părtinire se bazează pe fapte pe care le puteți citi mai jos și le puteți verifica singuri.

Acest site a fost creat de utilizatorii Monero. A fost o vreme când nu eram utilizatori Monero, dar eram preocupați de confidențialitatea financiară. Am cercetat monedele care pretindeau că sunt private, iar această pagină este rezultatul cercetărilor noastre. Acesta este motivul pentru care am ales Monero în detrimentul celorlalte. Așadar, dacă părem părtinitori, suntem, dar credem că această părtinire se bazează pe fapte pe care le puteți citi mai jos și le puteți verifica singuri.

### Prezentare generală

Selectați un logo pentru a trece la analiza monedei respective.

### Monero

Monero a fost 100% open source încă de la începuturile sale, ceea ce înseamnă că oricine poate vedea [ codul sursă ](https://github.com/monero-project/bitmonero) pentru a verifica dacă nu există backdoors și dacă software-ul este sigur.

Monero are de asemenea [ lucrări de cercetare recenzate de colegi ](https://lab.getmonero.org/) care verifică matematic și sistematic toate proprietățile sale enumerate mai sus.

### DASH

DASH are o [ listă bogată](https://bitinfocharts.com/top-100-richest-darkcoin-addresses.html), deci nu este o monedă privată. Detaliile financiare ale adreselor de monede sunt vizibile pentru oricine examinează blockchain-ul.

> DASH nu este deloc privat din punct de vedere criptografic. De fapt, am avut un slide în pachet care spunea "DASH, LOL" și, ca și nimic altceva... este un fel de ulei de șarpe și, personal, nu prea îmi place. 
> 
> **Gregory Maxwell** , dezvoltator și criptograf Bitcoin Core, într-o prezentare [ la Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

DASH nu este deloc privat din punct de vedere criptografic. De fapt, am avut un slide în pachet care spunea "DASH, LOL" și, ca și nimic altceva... este un fel de ulei de șarpe și, personal, nu prea îmi place. 

DASH nu este deloc privat din punct de vedere criptografic. De fapt, am avut un slide în pachet care spunea "DASH, LOL" și, ca și nimic altceva... este un fel de ulei de șarpe și, personal, nu prea îmi place. 

**Gregory Maxwell** , dezvoltator și criptograf Bitcoin Core, într-o prezentare [ la Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

**Peter Todd** , un alt dezvoltator și criptograf Bitcoin Core, a făcut o declarație similară [](https://twitter.com/petertoddbtc/status/622022840330682368).

### Zcash

Tranzacțiile Zcash sunt vizibile pe blockchain-ul lor. Ei permit tranzacții ascunse, dar [ mai puțin de 1% din tranzacții sunt complet protejate ](http://stat.bloxy.info/superset/dashboard/zcash/) . Deoarece tranzacțiile ascunse sunt opționale și nu sunt implicite (ca să nu mai spunem că sunt rar folosite), [ tranzacțiile ascunse ies în evidență pe blockchain ](http://weuse.cash/2016/06/09/btc-xmr-zcash/), atrăgând atenția asupra lor.

> Și apropo, cred că putem determina cu succes ca Zcash să fie prea ușor de urmărit pentru infractori precum WannaCry, dar să rămână complet privat și & fungibil. 
> 
> **Zooko Wilcox** , CEO Zcash, într-un [ tweet ](https://twitter.com/zooko/status/863202798883577856)

Și apropo, cred că putem determina cu succes ca Zcash să fie prea ușor de urmărit pentru infractori precum WannaCry, dar să rămână complet privat și & fungibil. 

Și apropo, cred că putem determina cu succes ca Zcash să fie prea ușor de urmărit pentru infractori precum WannaCry, dar să rămână complet privat și & fungibil. 

**Zooko Wilcox** , CEO Zcash, într-un [ tweet ](https://twitter.com/zooko/status/863202798883577856)

Dacă Zcash poate fi "prea ușor de urmărit", atunci nu poate fi complet privat sau fungibil. 

Tranzacțiile obișnuite sunt transparente. Tranzacțiile ascunse utilizează zk-SNARKS, care au garanții de confidențialitate solide în anumite condiții. Întrebarea este dacă aceste condiții sunt îndeplinite și, având în vedere numărul infim de persoane care utilizează capacitățile protejate, acest lucru rămâne sub semnul întrebării.

Zcash este o companie și în prezent [ ia 20% din toate ZEC-urile extrase ca recompensă a fondatorului](https://z.cash/blog/funding.html). 

Zcash a avut nevoie de un **Sistem de Încredere**. Acest lucru înseamnă că trebuie să aveți încredere că sistemul a fost creat în mod onest. Dacă nu a fost creat în mod onest, [ ar putea fi create cantități nelimitate de ZEC fără ca nimeni să știe](https://blog.okturtles.com/2016/03/the-zcash-catch/). Acest lucru l-ar îmbogăți pe hacker și ar devaloriza ZEC. Nu există nicio modalitate de a ști dacă Configurarea de încredere a fost executată în mod onest. Trebuie să îi credem pe cuvânt. Acest lucru introduce un punct de eșec uman în sistem, ceea ce este contrar aproape tuturor celorlalte criptomonede. În criptomonede ar trebui să aveți încredere doar în matematică și în codul sursă verificabil, nu în oameni. Așa cum am văzut cu aproape toate companiile mari de software, cum ar fi [ Microsoft](https://www.gnu.org/proprietary/proprietary-back-doors.en.html), [ Apple](http://www.digitaltrends.com/computing/apple-vs-fbi-backdoor-to-data-already-exists/), și chiar și guvernele, nu ar trebui să fie de încredere. 

Peter Todd, un dezvoltator Bitcoin Core care [ a participat ](https://github.com/zcash/mpc/blob/master/README.md) la Configurarea de încredere Zcash, a numit-o un " [ backdoor ](https://twitter.com/petertoddbtc/status/793584540891643906) ". 

> Zcash nu este necondiționat solid, nu poate fi cu tehnologia actuală... necesită o configurare de încredere… va trebui să refacem procedura [Trusted Setup] pentru a actualiza criptografia în timp, deci este o vulnerabilitate. 
> 
> Gregory Maxwell, dezvoltator Bitcoin Core și criptograf, într-o [ prezentare la Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

Zcash nu este necondiționat solid, nu poate fi cu tehnologia actuală... necesită o configurare de încredere… va trebui să refacem procedura [Trusted Setup] pentru a actualiza criptografia în timp, deci este o vulnerabilitate. 

Zcash nu este necondiționat solid, nu poate fi cu tehnologia actuală... necesită o configurare de încredere… va trebui să refacem procedura [Trusted Setup] pentru a actualiza criptografia în timp, deci este o vulnerabilitate. 

Gregory Maxwell, dezvoltator Bitcoin Core și criptograf, într-o [ prezentare la Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

**Notă:** Zcoin trece de la schema sa actuală Sigma la un nou protocol care se bazează pe noua sa lucrare, Lelantus. Lelantus va fi implementat în etape, iar acest articol va presupune că toate etapele sunt complete și implementate pentru comparații adecvate alături de termenele de implementare proiectate.

Motivul pentru care Zcoin și-a permis acest lux de a fi judecat pe baza viitorului său protocol, și nu Zcash, este că Zcoin are o foaie de parcurs cu termene generale de activare, în timp ce planurile de "confidențialitate implicită" ale Zcash sunt și continuă să fie nebuloase.

Zcoin (XZC) nu va avea o listă de bogătași, deci va fi privată. În mod implicit, confidențialitatea obligatorie este așteptată să intre în funcțiune în 2021. Odată implementată, o listă de bogăție nu va putea fi creată (deși în prezent [ei au unul](https://www.coinexplorer.net/XZC/richlist)).

### Bitcoin Mixers

Toate tranzacțiile Bitcoin sunt vizibile pe blockchain și există o [ listă cu cei bogați în Bitcoin](http://www.bitcoinrichlist.com/top100), deci Bitcoin nu este privat. Bitcoin este [ pseudoanonim ](https://bitcoin.org/en/you-need-to-know), nu anonim. 

Pentru **mixerele Bitcoin** , trebuie să aveți încredere că își pot păstra datele în siguranță și că nu sunt deținute de, sau nu cooperează cu un guvern, hackeri sau alte entități. 

În iulie 2017, fondatorul celui mai mare serviciu de mixare a Bitcoin, BITMIXER.IO, a anunțat că se închide și a dat acest motiv: 

> … Acum am înțeles că Bitcoin este un sistem transparent și non-anonimic **prin design**. Blockchain este o mare carte deschisă… 
> 
> BITMIXER.IO, într-un anunț de închidere pe [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (sublinierea în original). 

… Acum am înțeles că Bitcoin este un sistem transparent și non-anonimic **prin design**. Blockchain este o mare carte deschisă… 

… Acum am înțeles că Bitcoin este un sistem transparent și non-anonimic **prin design**. Blockchain este o mare carte deschisă… 

BITMIXER.IO, într-un anunț de închidere pe [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (sublinierea în original). 

Câteva săptămâni mai târziu, după ce a luat în considerare diferitele monede centrate pe confidențialitate, a spus următoarele: 

> După o investigație aprofundată, confirm că MONERO este cea mai bună monedă de confidențialitate. Așadar, recomand cu tărie MONERO tuturor celor care au nevoie de un plus de confidențialitate. 
> 
> BITMIXER.IO, într-un [ post următor](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

După o investigație aprofundată, confirm că MONERO este cea mai bună monedă de confidențialitate. Așadar, recomand cu tărie MONERO tuturor celor care au nevoie de un plus de confidențialitate. 

După o investigație aprofundată, confirm că MONERO este cea mai bună monedă de confidențialitate. Așadar, recomand cu tărie MONERO tuturor celor care au nevoie de un plus de confidențialitate. 

BITMIXER.IO, într-un [ post următor](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Deoarece toate tranzacțiile Bitcoin sunt vizibile pe blockchain, TOATE tranzacțiile Bitcoin pot fi urmărite. Un mixer Bitcoin poate ascunde foarte mult tranzacțiile, ceea ce face mult mai dificilă urmărirea Bitcoin, dar nu imposibilă. Pe măsură ce tehnologia progresează și companiile specializate în urmărirea tranzacțiilor Bitcoin devin mai răspândite, tranzacțiile odată foarte ofuscate vor deveni relativ ușor de urmărit: 

  * [ Forțele de ordine continuă să investească în serviciile de urmărire Bitcoin ](https://news.bitcoin.com/law-enforcement-continues-invest-bitcoin-tracking-services/)
  * [ Time.com: Bitcoini sunt mai ușor de urmărit decât crezi ](http://time.com/3689359/bitcoins-track-anonymous/)
  * [ Elliptic: O companie specializată în urmărirea Bitcoin pentru aplicarea legii ](https://www.elliptic.co/)

O căutare pe Google va scoate la iveală zeci de articole ca cele de mai sus. Și nu uitați că orice tranzacție care a avut loc în orice moment în trecut se află în blockchain și poate fi urmărită, chiar dacă a fost folosit un serviciu de mixare. De fapt, utilizarea unui serviciu de mixare este posibil să atragă atenția asupra acelor tranzacții. 

Nu toți Bitcoinii sunt egali și nu au aceeași valoare. Unii Bitcoini au fost trecuți pe lista neagră și blocați de mai multe entități, ceea ce face ca monedele respective să fie mai puțin valoroase decât restul. Dacă primiți Bitcoini care au fost folosiți în trecut în scopuri ilegale, atunci Bitcoinii dvs. ar putea fi trecuți pe lista neagră, chiar dacă nu ați avut nimic de-a face cu activitatea ilegală. Sau, să spunem că un guvern, un angajator sau o altă entitate decide să vă treacă pe lista neagră a Bitcoinilor în viitor, la fel cum se procedează în cazul înghețării sau confiscării activelor. Nu ați putea face nimic. Deoarece un mixer nu face decât să îngreuneze urmărirea Bitcoins, această categorie a fost marcată ca "nu este fungibil." 

  * Andreas Antonopoulos, un fost dezvoltator Bitcoin Core care este foarte respectat în Bitcoin și în alte comunități de criptomonede, recunoaște problema fungibilității Bitcoin într-un [ videoclip YouTube](https://www.youtube.com/watch?v=ak1iojpiHpM&feature=youtu.be&t=33m9s). 
  * Discuția despre problema fungibilității Bitcoin pe [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=1190707.0)

## Rezumat

În opinia noastră, Monero este alegerea evidentă dacă căutați o criptomonedă privată, sigură, de neurmărit, fungibilă, descentralizată, pentru care nu este necesară nicio configurare de încredere. Orice altceva pune în pericol intimitatea și securitatea dvs. Dar nu vă bazati doar pe opinia noastră. Faceți-vă propriile cercetări și vedeți singuri. Luați în considerare faptul că Monero este aprobat și folosit de entități care depind de intimitate și imposibilitatea de a fi urmărit, cum ar fi:

  * [ SIGAINT ](https://www.reddit.com/r/Monero/comments/4xqrzd/sigaint_launches_tor_monero_node_as_its_operators/)
  * [ Purism ](https://puri.sm/posts/purism-collaborates-with-cryptocurrency-monero-to-enable-mobile-payments/)
  * [ Wikileaks ](https://shop.wikileaks.org/donate#db9)
  * AlphaBay Market (AB) a fost închis în iulie 2017. [ Plângerea federală de confiscare ](https://assets.documentcloud.org/documents/3898109/AlphaBay-Cazes-Forfeiture-Complaint.pdf) împotriva AB arată că: 
    * **Monero este singura criptomonedă privată și de neurmărit:**   
"În total, din portofelele lui CAZES și computerul agenților a fost preluată controlul asupra aproximativ 8,800,000 de dolari în Bitcoin, Ethereum, Moreno [sic] și Zcash, după cum urmează: 1,605.0503851 Bitcoin, 8,309.271639 Ethereum, 3,691.98 Zcash, _și o sumă necunoscută de Monero._ " (la sfârșitul paginii 20 și începutul paginii 21, accent adăugat) 
    * **Tranzacțiile cu Bitcoin nu sunt private și pot fi urmărite:**   
"Agenții federali au obținut mandatele după ce au urmărit un număr de tranzacții Bitcoin care începeau cu AlphaBay, conducând la conturi de monede digitale, iar în final la conturi bancare și alte active tangibile, deținute de CAZES și soția lui." (p. 17, liniile 24-26) 

  * **Monero este singura criptomonedă privată și de neurmărit:**   
"În total, din portofelele lui CAZES și computerul agenților a fost preluată controlul asupra aproximativ 8,800,000 de dolari în Bitcoin, Ethereum, Moreno [sic] și Zcash, după cum urmează: 1,605.0503851 Bitcoin, 8,309.271639 Ethereum, 3,691.98 Zcash, _și o sumă necunoscută de Monero._ " (la sfârșitul paginii 20 și începutul paginii 21, accent adăugat) 
  * **Tranzacțiile cu Bitcoin nu sunt private și pot fi urmărite:**   
"Agenții federali au obținut mandatele după ce au urmărit un număr de tranzacții Bitcoin care începeau cu AlphaBay, conducând la conturi de monede digitale, iar în final la conturi bancare și alte active tangibile, deținute de CAZES și soția lui." (p. 17, liniile 24-26) 

LocalMonero nu susține sau nu încurajează nicio activitate ilegală. 

LocalMonero nu susține sau nu încurajează nicio activitate ilegală. 

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

  * [Revista Wired se înșeală în legătură cu Monero, iată de ce](/knowledge/wired-article-debunked)/

  * [Top 15 mituri și îngrijorări legate de Monero dezmințite](/knowledge/monero-myths-debunked)/

  * [Cum păstrează Dandelion++ confidențialitatea originilor tranzacțiilor Monero](/knowledge/monero-dandelion)/

  * [De ce Monero este Open Source și descentralizat](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Mineritul Monero: Ce face ca RandomX să fie atât de special](/knowledge/monero-mining-randomx)/

Lecturi suplimentare