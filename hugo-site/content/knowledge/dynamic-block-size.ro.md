---
title: "Cum a rezolvat Monero problema dimensiunii blocurilor care afectează Bitcoin"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Notă:** Este foarte recomandat ca cititorul să fi citit articolele noastre ["De ce Monero are o emisie de coadă"](/knowledge/monero-tail-emission) și ["Minarea Monero: Ce face RandomX atât de special"](/knowledge/monero-mining-randomx). Acest articol se bazează pe conceptele prezentate acolo._

De fiecare dată când indivizii discută problemele cu blockchain, unul dintre primele cuvinte care apar va fi 'scalarea'. Nu este un secret că blockchains nu scalează bine, dar majoritatea oamenilor nu știu de ce.

Adevărul este că scalarea este de fapt un termen umbrelă care acoperă două categorii diferite: suportul protocolului și suportul tehnologic la un moment dat. În acest articol, ne vom concentra atenția pe una, suportul protocolului este practic o măsură a cât de multe tranzacții poate gestiona protocolul la un moment dat.

Bitcoin are o limită a dimensiunii blocului, ceea ce înseamnă că odată ce sunt incluse suficiente tranzacții într-un bloc, orice tranzacții suplimentare vor trebui să aștepte la rând pentru următorul bloc. O analogie utilă ar fi să te gândești la un tren. Un tren ajunge la stație și cei din coadă intră. Odată ce trenul este plin, oricine este lăsat afară va trebui să aștepte următorul.

Bitcoin folosește taxe pentru a determina cine intră în bloc sau nu. Să revenim la analogia cu trenul, putem imagina un potențial pasager, care este pe punctul de a fi lăsat în urmă, oferă mecanicului de tren cinci dolari pentru a-i oferi un loc. Alți pasageri urmează exemplul, și în cele din urmă se ajunge la o licitație pentru a vedea cine ocupă care locuri. Este la latitudinea șoferului să decidă dacă vrea să respecte politica de primul venit, primul servit, dar este în cel mai bun interes financiar al său să-și maximizeze venitul luând la bord licitatorii cu cele mai mari oferte.

În această analogie, mineri sunt șoferii de tren. Ei pot include oricare tranzacții doresc în bloc, dar în general vor alege cele care au taxele plătite cele mai mari.

Alternativ, dacă blocurile nu sunt foarte pline, oamenii nu au niciun stimulent să plătească taxe mari deoarece sunt suficiente locuri gratuite disponibile.

În vârful boomului criptomonedelor din 2017, Bitcoin a fost inundat cu tranzacții, iar taxele au crescut pentru cei care doreau să fie incluși în următorul bloc, sau orice bloc apropiat de viitor. Cei care nu erau dispuși să plătească taxe mari și-au văzut tranzacțiile amânate cu ore, zile, sau chiar scoase complet din coadă.

Aceasta a fost o perspectivă înfricoșătoare asupra modului în care Bitcoin ar funcționa dacă adesea discutata 'adoptare în masă' ar avea loc. Dacă Bitcoin ar fi folosit de mase, lucrurile ar fi și mai rele decât în 2017, și Bitcoin ar fi inaccesibil pentru oricine în afara celor bogați, pur și simplu pentru că debitul este mic din cauza unei dimensiuni fixe a blocului, determinând piața taxelor să preia controlul.

Monero a prevăzut aceasta și a dorit să facă ceva diferit. Așadar, dezvoltatorii Monero au implementat un bloc dinamic.

Practic, Monero are și o limită a dimensiunii blocului, dar este o limită moale. Când coada tranzacțiilor în așteptare devine prea lungă, minatorii pot crește dimensiunea blocurilor. Folosind analogia noastră cu trenul, te poți imagina adăugând mai multe vagoane pentru a se potrivi cu pasagerii extra. După ce coada este golită, blocurile se micsorează la dimensiunea lor originală.

Dacă aceasta pare o idee bună, pare rezonabil să întrebăm de ce Monero este singura criptomonedă care a implementat acest lucru. De ce să nu-l adăugăm pe Bitcoin pentru a pune capăt problemelor de debit?

Din păcate, acest lucru nu este posibil. Există mai multe motive pentru care, și vom face tot posibilul să explicăm.

Este întotdeauna în cel mai bun interes al unui miner să aibă blocuri mari. Cu blocuri mari ei pot include mai multe tranzacții și pot face mai mulți bani din taxe, precum și din recompensele blocului. Acest lucru are potențialul de a duce la atacuri spam, unde cineva trimite multe tranzacții mici, cu taxe mici, pentru a umfla lanțul. Minatorii ar crește doar dimensiunea blocului pentru a le include pe toate pentru că banii sunt bani, indiferent cât de mici. Aceasta ar duce la blocuri consistent mari cu puțin beneficiu economic. Bitcoin rezolvă aceasta prin restricționarea artificială a dimensiunii blocului, generând astfel o piață a taxelor. Atacatorii spam ar trebui să plătească mai mult decât ceilalți utilizatori în taxe, și nu mai este ieftin. Dar asta înseamnă că blocurile devin pline lăsând unele tranzacții în așteptare cum am menționat mai sus.

Așadar, cum poate Monero să aibă blocuri dinamice, dar să evite atacurile spam? Răspunsul este simplu, dar ingenios. O penalitate asupra recompensei blocului este introdusă atunci când un bloc este mai mare decât normal. Dacă un miner vrea să crească dimensiunea blocului, recompensa pe care o obține din găsirea acelui bloc va fi mai mică decât ar fi primit altfel. Așadar, ei vor crește dimensiunea blocului doar atunci când taxele plătite de utilizatori pentru tranzacții depășesc partea pierdută a recompensei blocului. De exemplu, dacă minerul ar pierde 0.5 XMR ridicând dimensiunea blocului, și suma taxelor plătite pentru tranzacții ar fi 0.4 XMR, atunci ar exista o pierdere netă de 0.1 XMR dacă ar crește dimensiunea, așadar ei nu ar face asta. Pe de altă parte, dacă totalul taxelor de tranzacție se ridică la 0.7 XMR, atunci ar exista un câștig net de 0.2 XMR, chiar dacă ei pierd 0.5 XMR din penalitatea recompensei blocului, așadar minerul va crește dimensiunea.

Aceste blocuri dinamice permit rețelei să crească organic, fără a restricționa artificial dimensiunea blocului pentru a crea o piață de taxe forțată, în timp ce evită totuși atacurile spam. Există mai multe perspective din care putem privi această idee, și mai multe motive pentru care nu ar fi posibil să fie adăugat la Bitcoin, dar pentru moment, sperăm că cititorul are o înțelegere asupra felului în care Monero evită mai multe dintre problemele din Bitcoin și derivatele acestuia, și cum intenționează să-și scaleze debitul în viitor.

Lecturi suplimentare