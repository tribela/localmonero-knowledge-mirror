---
title: "Explicații despre ieșirile Monero"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero, ca și alte criptomonede, utilizează ieșirile ca mijloc de contabilizare a fondurilor. Mulți utilizatori cunoscători de criptomonede au auzit probabil acest termen înainte, dar nu toată lumea înțelege ce înseamnă și cum funcționează. Așa cum am explorat în articolul nostru despre [semnăturile inelare](/knowledge/ring-signatures), ieșirile sunt unitatea reală schimbată pe blockchain între părțile implicate în tranzacții. Similar cu o bancnotă de un dolar, dar suma nu este într-o valoare nominală fixă.

Dacă sunteți plătit cu 16 dolari pentru o slujbă, s-ar putea să primiți o bancnotă de un dolar, una de cinci dolari și una de zece dolari. Aveți 16 dolari, dar aveți și trei bancnote diferite în portofel. Dacă vrei să plătești pe cineva cu 6 dolari, poți folosi bancnota de 5 și cea de 1, dar dacă vrei să plătești pe cineva cu 8 dolari, poți folosi doar bancnota de 10 dolari și primești înapoi 2 dolari în rest. În cele din urmă, dacă ai vrea să plătești cuiva 14 dolari, ar trebui să folosești toate cele trei bancnote și ai primi înapoi 2 dolari în rest, dar pentru un moment, când dai toate cele trei bancnote, nu mai ai niciun ban în portofel până când nu primești restul înapoi.

Monero funcționează în mod similar. Să presupunem că aveți un magazin și că efectuați trei vânzări pentru trei articole diferite. S-ar putea să primiți 1,5 XMR, 2,25 XMR și 5,25 XMR pentru un total de 9 XMR, dar aveți, de asemenea, trei ieșiri diferite în portofelul dvs. cu valorile menționate anterior. La fel ca în cazul dolarilor, s-ar putea să doriți să plătiți cuiva 3 XMR. Ați putea folosi doar ieșirea de 5,25 XMR și să primiți înapoi 2,25 XMR în rest sau ați putea combina ieșirile de 1,5 și 2,25 XMR și să primiți înapoi 0,75 XMR în rest.

Dar, imediat ce trimiteți tranzacția, ieșirile pe care le utilizați sunt puse într-o stare "blocată", ceea ce înseamnă că sunt inaccesibile până când primiți înapoi modificarea. Protocolul deblochează fondurile (adică vă restituie restul) după 10 confirmări, adică după aproximativ 20 de minute. La fel cum, odată ce dai bancnotele de un dolar din portofel, nu mai poți folosi banii până când nu primești restul înapoi de la casierie, Monero este inaccesibil până când primești înapoi restul.

Să ne întoarcem la exemplul în care trimiteți 3 XMR cuiva și folosiți ieșirea de 5,25 XMR. Acum, în timp ce așteptați să primiți înapoi 1,75 XMR în rest, nu îi puteți folosi. Acești 1,75 XMR sunt inaccesibili pentru dumneavoastră. Dar puteți folosi în continuare ieșirile de 1,5 XMR și 2,25 XMR, deoarece acestea nu au fost cheltuite. Revenind la exemplul dolarului, dacă ați plătit cuiva 8 dolari, ca în exemplul anterior, nu ați putea folosi cei 2 dolari pe care îi așteptați înapoi în rest până când nu vi se dau, dar în acest exemplu, aveți încă o bancnotă de 10 dolari care nu este folosită în portofel. Aceasta poate fi folosită în continuare pentru a cumpăra orice doriți în timp ce așteptați restul. Același lucru se întâmplă și cu Monero.

Acesta este adesea un punct de confuzie pentru noii utilizatori Monero. Adesea, un utilizator poate avea doar o singură ieșire în portofelul său, primită de la un exchange sau de la un prieten. Să spunem că această ieșire este de 20 XMR. Acesta nu are alte ieșiri în portofelul său. Acum doresc să facă o donație către două dintre organizațiile caritabile preferate. Ei trimit 5 XMR către prima organizație caritabilă și apoi sunt confuzi pentru că, deși ar trebui să mai aibă 15 XMR, nu pot trimite imediat următoarea donație către a doua organizație caritabilă. După cum probabil ați ghicit, acest lucru se datorează faptului că cei 15 XMR sunt blocați. Aceștia nu pot fi cheltuiți până când nu sunt returnați ca rest (10 confirmări sau aproximativ 20 de minute). După ce fondurile lor sunt deblocate, vor putea trimite a doua donație.

Doar pentru a reitera punctul de vedere, nu ar fi avut această problemă dacă ar fi avut mai multe ieșiri, cum ar fi două ieșiri de 10 XMR sau similare. Ar fi putut trimite ambele donații una după alta, deoarece prima donație ar fi folosit una dintre ieșirile de 10 XMR (și ar fi așteptat 10 confirmări pentru a primi înapoi 5 XMR în rest), iar cea de-a doua donație ar fi folosit cealaltă ieșire de 10 XMR.

Unele portofele de criptomonede au o funcție numită "gestionarea ieșirii", care arată pur și simplu utilizatorului ce ieșiri are în prezent (pe lângă suma totală) și îi permite să aleagă pe care dorește să le folosească atunci când își cheltuie criptomoneda.

Deocamdată, GUI Monero selectează automat ieșirile pentru utilizatori, deoarece utilizatorii care își selectează singuri ieșirile duc adesea la confuzie sau, în unele cazuri, la afectarea confidențialității. Cu toate acestea, există portofele în construcție, cum ar fi noul proiect de portofel Feather, care vor conține aceste funcții de gestionare a ieșirilor.

Am vorbit mult despre partea de trimitere, dar ceva fascinant se întâmplă la partea de primire. Revenind la exemplul nostru de a trimite 3 XMR cuiva și de a folosi ieșirile de 1,5 XMR și 2,25 XMR în tranzacție (așteptând 0,75 XMR în rest), destinatarul NU primește două ieșiri de 1,5 XMR și 2,25 XMR. În schimb, primește UN singur rezultat de 3 XMR.

În fundal, protocolul combină toate ieșirile utilizate pentru cheltuieli și oferă destinatarului o ieșire cu suma plătită și trimite înapoi la expeditor o ieșire de schimb. Astfel, expeditorul va primi înapoi o ieșire ca rest, indiferent dacă a folosit două, trei sau zece ieșiri pentru a trimite tranzacția.

Sperăm că acest lucru a clarificat unele confuzii cu privire la ieșiri și la modul în care funcționează contabilitatea internă a protocolului, precum și la problema obișnuită a utilizatorilor care se confruntă cu confuzia atunci când se confruntă cu fonduri blocate. Într-un alt articol, vom explora gestionarea ieșirilor, astfel încât să reducem la minimum șansa de a fi nevoiți să așteptați fonduri deblocate înainte de a trimite tranzacții viitoare.

Lecturi suplimentare