---
title: "Semnături inelare Monero vs CoinJoin ca în Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Pe măsură ce instrumentele de confidențialitate ale Bitcoin au câștigat mai multă atenție și utilizare, acestea au intrat sub o mai mare supraveghere de reglementare. Acest control a dus la un [anunț recent](https://twitter.com/wasabiwallet/status/1503091503207432193) al unui instrument de confidențialitate Bitcoin, Wasabi Wallet, că va începe să cenzureze și să respingă intrările de intrare în amestecuri pe care le consideră ilicite sau împotriva ToS, și va plăti o companie de analiză a lanțului pentru a "verifica" participanții la amestecul de intrare.

Utilizarea tranzacțiilor CoinJoin pentru a ascunde sursa fondurilor în Bitcoin a fost de mulți ani nucleul confidențialității Bitcoin, iar problemele și riscurile inerente utilizării sale sunt unele dintre problemele de bază pe care semnăturile inelare Monero le corectează și le previn.

În această postare pe blog vom face o scurtă comparație între CoinJoin și semnăturile inelare, precum și de ce abordarea adoptată în Monero duce la o mai mare rezistență la cenzură, la o mai mare confidențialitate și la mai puține probleme pentru utilizatori.

## Ce este o tranzacție CoinJoin?

## Ce este o tranzacție CoinJoin?

Deoarece toate tranzacțiile sunt complet transparente în Bitcoin - dezvăluind expeditorul, destinatarul și sumele - utilizatorii trebuie să ia măsuri suplimentare pentru a-și păstra confidențialitatea față de expeditorii anteriori și viitorii destinatari ai fondurilor lor sau riscă cenzura, supravegherea sau furtul fondurilor prin violență fizică.

Cea mai bună soluție de astăzi pentru confidențialitate pe Bitcoin este un instrument numit [„CoinJoin”](https://bitcoiner.guide/qna/coinjoin/), unde 2 sau mai mulți utilizatori lucrează împreună (de obicei prin intermediul unui coordonator centralizat) pentru a crea o tranzacție specială care face dificilă pentru observatorii externi conectarea intrărilor cu ieșirile. Fiecare participant comunică pentru a construi împreună tranzacția fără a ceda custodia fondurilor sale și primește la final un rezultat al cărui istoric anterior este acum neclar (sau obscur) pentru observatorii externi.

Aceasta rupe istoricul UTXO-urilor specifice, permițând utilizatorilor Bitcoin să obțină un minim de secretizare în viitor atunci când tranzacționează. Cu toate acestea, CoinJoin (așa cum este implementat în Wasabi Wallet și Samourai Wallet, cele două instrumente CoinJoin cele mai utilizate pentru Bitcoin) are câteva dezavantaje majore:

  * Întrucât tranzacțiile CoinJoin sunt complet opționale și necesită o participare activă, orice participant arată în mod necesar că urmărește o confidențialitate mai mare decât cea a utilizatorilor "normali" de Bitcoin, ceea ce ar putea să îi scoată în evidență și să cauzeze probleme în ceea ce privește cheltuirea fondurilor la multe burse sau entități reglementate. Fiecare utilizator nu poate nega faptul că a participat la o tranzacție CoinJoin.
  * Utilizatorii cu sume mari de fonduri pentru CoinJoin pot fi nevoiți să aștepte ore (sau chiar zile!) pentru a găsi suficienți participanți cu care să facă CoinJoin, ceea ce duce la întârzieri mari între momentul în care un utilizator primește fonduri și momentul în care le poate cheltui în mod privat.
  * Utilizatorii cu sume mari de fonduri pentru CoinJoin pot fi nevoiți să aștepte ore (sau chiar zile!) pentru a găsi suficienți participanți cu care să facă CoinJoin, ceea ce duce la întârzieri mari de la momentul în care un utilizator primește fonduri până când le poate cheltui în mod privat.
  * Confidențialitatea oferită de o tranzacție CoinJoin se degradează în timp, pe măsură ce alți participanți cheltuiesc fonduri sau leagă ieșirile lor de identitatea lor prin intermediul schimburilor KYC, al comercianților care solicită ID-uri etc. Acest lucru înseamnă că, în mod ideal, utilizatorii ar trebui să își mențină fondurile în mod constant în tranzacții CoinJoin pentru a-și păstra setul de anonimat ("mulțimea în care să se ascundă") cât mai proaspăt posibil.
  * În majoritatea abordărilor CoinJoin, participanții trebuie să utilizeze un UTXO de mărime fixă (de exemplu, 0,1 BTC) pentru a îngreuna conectarea intrărilor și ieșirilor tranzacțiilor CoinJoin. Acest lucru duce la comisioane mai mari (mai multe tranzacții separate necesare pentru fiecare intrare mare), mai mult "mărunțiș toxic" (fonduri care nu pot fi cheltuite fără riscuri serioase pentru confidențialitate) și poate împiedica utilizatorii mai mici să se poată amesteca deloc dacă nu au soldul minim necesar.

## Cum rezolvă semnăturile inelare aceste probleme?

## Cum rezolvă semnăturile inelare aceste probleme?

Așa [cum am analizat în profunzime ce sunt semnăturile inelare în trecut](/knowledge/ring-signatures), Nu voi intra în detalii despre aspectele tehnice ale modului în care funcționează în această postare pe blog. În schimb, vom analiza modul în care abordările adoptate în Monero rezolvă problemele cu CoinJoin discutate mai sus.

> CoinJoin este opt-in și necesită participare

CoinJoin este opt-in și necesită participare

Semnăturile inelare ale Monero sunt o caracteristică de bază a protocolului de confidențialitate, iar _fiecare_ fiecare tranzacție din rețea le folosește. Acest lucru înseamnă că tranzacțiile niciunui utilizator nu se remarcă prin faptul că urmărește o mai mare confidențialitate decât utilizatorii "normali" de Monero, iar toți utilizatorii pot nega în mod plauzibil faptul că au cheltuit fonduri în orice tranzacție dată. Deoarece un utilizator care cheltuiește fonduri nu coordonează sau participă cu intrările momeală într-o tranzacție, acei utilizatori care dețin intrări care se întâmplă să fie selectate ca momeală pot spune cu onestitate că nu au participat la acea tranzacție, consolidându-și astfel confidențialitatea.

> Utilizarea unui coordonator centralizat

Utilizarea unui coordonator centralizat

Deoarece semnăturile inelare Monero sunt complet necoordonate și necesită doar ca adevăratul cheltuitor de fonduri să creeze tranzacția, nu este nevoie de un coordonator centralizat în Monero. Acest lucru garantează că _nimeni_ nu vă poate refuza accesul la confidențialitate în Monero și că nu există nicio entitate centralizată care să poată fi supusă la presiuni, niciun atac Sybil ușor asupra lichidității etc. Atâta timp cât tranzacția dvs. plătește taxele corespunzătoare, obțineți un acces necenzurabil la confidențialitate, securitate și anonimat în Monero.

> CoinJoin necesită lichidități

CoinJoin necesită lichidități

"Lichiditatea" disponibilă pentru oricine cheltuiește Monero pentru a o folosi ca momeală este întotdeauna setul total de ieșiri pe lanț, astfel încât nu există niciodată o lipsă de momeală în care să te ascunzi cu Monero. Cineva care dorește să cheltuiască Monero poate face acest lucru la ~20 de minute după ce a primit fondurile și nu trebuie să efectueze niciun pas suplimentar pentru a obține o confidențialitate puternică în Monero.

> Confidențialitatea CoinJoin se degradează în timp

Confidențialitatea CoinJoin se degradează în timp

Întrucât ieșirile Monero nu sunt niciodată cunoscute și cheltuite de către rețea, confidențialitatea oferită de semnăturile inelare este mult mai puțin susceptibilă la degradare în timp. Un utilizator nu este nevoit să își schimbe în mod constant ieșirile în Monero și, în afara unor circumstanțe extrem de rare, nu își pierde confidențialitatea pe măsură ce trece timpul.

Cu toate acestea, în cazul în care un utilizator dorește să "reîmprospăteze" momelile folosite cu o ieșire, acesta poate pur și simplu să își trimită fondurile înapoi și să le poată cheltui ~20 de minute mai târziu, ca de obicei.

> CoinJoin necesită, de obicei, intrări de dimensiuni fixe

CoinJoin necesită, de obicei, intrări de dimensiuni fixe

Deoarece sumele sunt ascunse în fiecare tranzacție folosind [“Tranzacții confidențiale”](/knowledge/monero-ringct) (o parte din "RingCT"), momelile utilizate în orice tranzacție pot fi de orice dimensiune. În Monero nu există niciun motiv de îngrijorare cu privire la euristica bazată pe cantitate, astfel încât tranzacțiile sunt mult mai simplu de construit și pot folosi momeli din orice moment și de orice valoare pe Monero blockchain.

## Cum pot afla mai multe?

## Cum pot afla mai multe?

Dacă sunteți curioși și doriți să înțelegeți mai bine semnăturile inelare sau tranzacțiile CoinJoin, consultați linkurile de mai jos pentru a începe:

  * [Modul în care semnăturile inelare ascund ieșirile Monero](/knowledge/ring-signatures)
  * [Semnătura inelate - Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [CoinJoin Prezentare generală](https://6102bitcoin.com/coinjoin-overview/)

Lecturi suplimentare

  * [Cum permite Monero în mod unic economiile circulare](/knowledge/monero-circular-economies)/

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

  * [De ce Monero este mai bun decât Dash, Zcash, Zcoin (chiar și cu Lelantus), Grin și Bitcoin Mixers ca Wasabi (actualizat în mai 2020)](/knowledge/why-monero-is-better)/

Lecturi suplimentare