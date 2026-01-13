---
title: "Cum îți protejează identitatea adresele Monero invizibile"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero a implementat o abordare în trei direcții în ceea ce privește confidențialitatea. Aceste tehnologii sunt [semnături inelare](/knowledge/ring-signatures), care ascund adevărata ieșire (expeditor), RingCT, care ascunde sumele, și adrese invizibile, care ascund destinatarul. Astăzi vom discuta despre ultima dintre aceste tehnologii menționate: adresele invizibile.

Există multe motive pentru care o persoană ar putea dori să ascundă cui trimite mesaje. Nu trebuie să lăsăm niciodată pe nimeni să încerce să ne convingă că toate exemplele de acest gen sunt comportamente neplăcute. Lucruri precum trimiterea către un partid politic nepopular, donarea către organizații de caritate sau sprijinirea celor pe care cultura îi consideră "respinși" sunt toate exemple de cazuri în care o persoană ar putea dori să își ascundă comportamentele de cheltuieli de teama repercusiunilor, dar sunt perfect legitime în natură.

Pe un blockchain transparent, adresele la care cineva își trimite tranzacțiile sunt vizibile pentru toți. Este important de luat în considerare faptul că, dacă minerii nu sunt de acord cu destinația banilor, ei pot alege să nu îi extragă într-un bloc, cenzurând efectiv această tranzacție pe o platformă aparent rezistentă la cenzură. Singura modalitate de a face ca această cenzură, puțin probabilă, să nu fie posibilă este ca minerii să nu poată distinge între tranzacții, deoarece toate metadatele de pe lanț sunt ascunse prin diverse mijloace. Lucru pentru care Monero este cunoscut.

Monero rezolvă această problemă a adreselor transparente prin implementarea adreselor invizibile, o tehnologie care a fost de fapt realizată inițial pentru Bitcoin în 2011 de către utilizatorul forumului Bitcoin Talk, ByteCoin (nu se știe care este relația cu Bytecoin, care va integra mai târziu adrese invizibile). Forma actuală a adreselor invizibile are însă mai multe îmbunătățiri față de ideea inițială. Dar mai întâi, pentru a vedea cum funcționează, să vorbim despre chei.

Este greu să fii în spațiul criptomonedelor și să nu auzi de chei. Fraze precum "faceți o copie de rezervă a cheii private" sunt comune, dar când un cetățean obișnuit aude cuvintele "cheie publică" și "cheie privată" se sperie și crede că va fi prea tehnic și confuz pentru a înțelege. Dar nu vă faceți griji. O vom lua încet și vom folosi o mulțime de exemple.

Cele două tipuri de chei utilizate în criptomonede sunt, după cum tocmai am menționat, publice și private. Aceste două chei sunt de obicei prezentate în perechi, ceea ce înseamnă că o anumită cheie publică și una privată sunt legate una de cealaltă. De fapt, de obicei, cheia publică este derivată din cea privată, ceea ce înseamnă că, dacă știți cheia privată, portofelul dvs. poate face niște calcule inteligente și poate obține de fiecare dată cheia publică corectă.

Acum, după cum sugerează și numele, cheia publică poate fi publică fără consecințe. De obicei, este o parte a adresei pe care o partajați pentru a primi bani în portofelul dvs. de criptomonede. De asemenea, urmându-și omonimul, cheia privată este una care nu trebuie să fie împărțită. Este cea care vă permite să semnați și să cheltuiți o tranzacție, așa că, dacă este furată sau împărtășită, atunci terța parte nefastă vă poate cheltui banii, de obicei pentru ei înșiși.

O analogie simplă ar fi un lacăt și cheia necesară pentru a-l deschide. Lacătul deschis poate fi împărțit liber și, într-adevăr, orice poate fi închis cu acest lacăt, dar numai persoana care deține cheia poate deschide orice lucru pe care este închis lacătul. Lacătul poate fi copiat și împărțit, dar cheia nu ar trebui să fie copiată.

Aceste chei sunt, de obicei, abstractizate față de utilizator, astfel încât acesta nu le vede niciodată. În Monero, ele nu apar deloc ca un șir alfanumeric înfricoșător. În Monero, utilizatorul obișnuit cunoaște cheia privată ca fiind sămânța sa. Semința (pe care ar trebui să o scrieți dacă nu ați făcut-o), este de fapt doar o cheie privată lizibilă pentru oameni. 

Vezi? Nu este atât de înfricoșător până la urmă. Înapoi la adresele invizibile.

După cum am menționat mai devreme, adresele invizibile nu au fost create inițial pentru Monero, ci pentru Bitcoin. Ca în cazul majorității ideilor începătoare însă, această primă iterație a avut probleme. Următoarea încercare a venit când CryptoNote a fost creat de Nicholas van Saberhagan pentru Bytecoin, precursorul lui Monero ([vezi istoricul nostru despre Monero și Bytecoin aici](/knowledge/monero-history)), și, deși a fost o îmbunătățire clară față de original, chiar și acesta a avut câteva defecte subtile.

În cele din urmă, a apărut o ultimă iterație de la un dezvoltator pentru o altă criptomonedă de confidențialitate, acum dispărută, care a rezolvat problemele de confidențialitate și securitate ale ideii. Aceasta a ajuns în cele din urmă în Monero și este cea folosită astăzi.

Deși aceste probleme de confidențialitate și securitate au fost rezolvate, adresele invizibile au adăugat un alt tip de ciudățenie tehnologiilor blockchain, una care nu exista înainte. Necesitatea de a scana. Deoarece adresele de primire nu sunt afișate public pe blockchain, destinatarul nu știe niciodată dacă o anumită tranzacție este a sa, așa că trebuie să scaneze fiecare tranzacție primită cu cheia sa privată pentru a vedea dacă este a sa.

În cazul monedelor de transparență, tot ce trebuie să facă este să verifice dacă o tranzacție este trimisă la adresa dumneavoastră. O întrebare simplă de tip da sau nu. Dar, în cazul adreselor invizibile, fiecare tranzacție ar putea fi una care vă este trimisă, așa că trebuie să încercați să o deblocați pe fiecare cu cheia dvs. privată pentru a vedea dacă se deschide.

Acesta este un pas suplimentar pe care Bitcoin și derivatele sale nu îl au și face ca configurarea inițială a portofelului, împreună cu sincronizarea unui portofel atunci când nu l-ați deschis de ceva timp, să fie mult mai lungă decât în cazul Bitcoin. Compromisul este totuși necesar pentru a debloca garanțiile de confidențialitate pe care le are. Trebuie remarcat faptul că, spre deosebire de cel mai slab punct al triplei de confidențialitate, semnăturile inelare, adresele invizibile nu sunt sensibile la euristică. Ea se bazează pe criptografia cu curbă eliptică, care a fost testată și verificată, pe care se bazează întregul internet, astfel încât spargerea ei ar însemna sfârșitul securității informatice în general, nu doar a Monero.

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

  * [Ce trebuie să știe fiecare utilizator Monero atunci când vine vorba de rețea](/knowledge/monero-networking/)

  * [Cum ascunde RingCT sumele tranzacțiilor Monero](/knowledge/monero-ringct/)

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