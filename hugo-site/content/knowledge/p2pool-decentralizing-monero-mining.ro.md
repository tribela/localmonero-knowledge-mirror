---
title: "P2Pool și rolul său în descentralizarea mineritului Monero"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Unul dintre obiectivele de bază ale proiectului Monero este de a permite o rețea echitabilă, descentralizată și sigură prin abordări noi și inovatoare în ceea ce privește minarea proof-of-work (PoW), principalul mod în care sunt securizate în prezent rețelele de criptomonede.

În timp ce un algoritm unic de minerit [ca RandomX](/knowledge/monero-mining-randomx) este extrem de important în acest scop, deoarece ajută la asigurarea faptului că oricine are un calculator poate contribui în mod echitabil la securitatea rețelei, RandomX nu rezolvă problemele care pot apărea din cauza mineritului în grup. Mineritul în pool este de departe cel mai comun mod de a mina criptomonede în prezent, inclusiv Monero, dar, din fericire, apariția mineritului p2pool schimbă rapid această situație.

## Ce este mineritul în comun?

## Ce este mineritul în comun?

Mineritul în grup este o modalitate prin care minerii împart sarcina de a încerca să rezolve un bloc în rețea și apoi împart în mod egal recompensele pentru toate blocurile găsite în grup. Deși acest lucru ajută enorm la echilibrarea frecvenței cu care minerii sunt plătiți față de minarea Monero de unul singur, nu este lipsit de probleme serioase de centralizare.

Pe măsură ce fiecare miner contribuie cu muncă la fondul comun, acesta renunță la controlul asupra muncii pe care o depune și asupra blocurilor pe care le găsește în favoarea fondului comun, având încredere că acesta va împărți în mod cinstit și echitabil recompensele între toți minerii în funcție de cantitatea de muncă depusă de fiecare. Dacă totul merge bine, operatorul de pool colectează munca depusă de toți minerii, o transmite rețelei și împarte recompensele în mod egal.

## Care este problema cu mineritul în grup?

## Care este problema cu mineritul în grup?

Din nefericire, acest lucru se bazează în întregime pe încredere și permite operatorului de pool să facă lucruri nefaste cu munca depusă de mineri. Operatorul pool-ului ar putea folosi munca depusă pentru a ataca rețeaua, ar putea încerca să dubleze fondurile (dacă pool-ul este suficient de mare) sau pur și simplu ar putea folosi munca depusă de mineri pentru a se plăti pe sine însuși și nu ar putea recompensa niciodată minerii în mod corespunzător pentru munca lor.

Cel mai mare risc pentru rețea este acela ca un grup (sau mai multe grupuri care lucrează împreună) să dețină mai mult de 51% din hashrate-ul rețelei sub controlul lor, deoarece ar putea folosi acest lucru pentru a trișa și a cheltui fonduri de două ori (un atac de tip "double-spend") sau pentru a încerca să schimbe regulile rețelei.

## Ce este p2pool?

## Ce este p2pool?

p2pool este un concept care a fost creat inițial pentru mineritul Bitcoin în 2011, dar nu a fost niciodată adoptat pe scară largă și rămâne practic nefolosit în Bitcoin. Din fericire, unul dintre dezvoltatorii cheie din spatele RandomX, SChernykh, și-a petrecut vacanța venind cu soluții la unele dintre problemele legate de implementarea Bitcoin a p2pool și rescriind tot software-ul de la zero.

p2pool din Monero permite minerilor să lucreze împreună, fără să aibă încredere, pentru a rezolva blocuri și pentru a securiza rețeaua Monero, folosind un software special pentru p2pool, pentru a împărți munca.

Acest lucru se face cu ajutorul unui nou blockchain (un "side-chain") care ține o evidență a muncii pe care o depune fiecare miner, a adresei portofelului său și a cantității de Monero pe care a câștigat-o, iar apoi plătește recompensa într-un mod descentralizat și lipsit de încredere. Deoarece acest lanț secundar are mult mai puțini mineri, este mult mai ușor să găsești și să trimiți blocuri pe el decât în rețeaua principală Monero, ceea ce face ca minerii să obțină mai ușor plăți consistente decât dacă ar fi minat Monero singur.

## Cum rezolvă p2pool problemele de minerit în grup?

## Cum rezolvă p2pool problemele de minerit în grup?

În p2pool, nu există un fond centralizat, un operator centralizat sau o singură persoană care să păstreze fondurile și să distribuie plățile. Toată munca depusă în mod colectiv de cei care extrag prin intermediul p2pool este verificată de blockchain-ul p2pool și de alți operatori de noduri pentru a se asigura că este legitimă, iar toți minerii sunt plătiți în funcție de munca pe care au depus-o imediat ce se găsește un bloc, direct din recompensele din acel bloc găsit.

Atunci când minerii aleg să folosească p2pool în loc de un pool centralizat, aceștia elimină orice putere și încredere din partea operatorilor de pool și se asigură că munca lor contribuie la binele rețelei și la propriile recompense, reducând astfel riscul atacurilor în rețea, al utilizării abuzive a muncii lor sau al furtului recompenselor care le sunt datorate.

Nu numai că acest lucru îi ajută să își protejeze propriile interese, dar reduce și riscul pe care pool-urile centralizate îl pot reprezenta pentru rețeaua Monero ca întreg. Utilizarea p2pool ajută, de asemenea, la reducerea imensă a riscului pe care statele naționale sau autoritățile de reglementare l-ar putea reprezenta pentru sănătatea rețelei, deoarece nu există operatori de pool-uri centralizate asupra cărora să exercite presiuni, nu există o concentrare geografică a pool-urilor pe care să se bazeze sau orice alt punct de presiune ușor de folosit împotriva Monero.

## Care sunt dezavantajele?

## Care sunt dezavantajele?

Din fericire, p2pool în Monero a fost bine conceput și bine construit și funcționează extrem de bine! Cu toate acestea, principalul dezavantaj al mineritului p2pool este că fiecare miner care dorește să folosească p2pool trebuie să ruleze propriul nod Monero, ceea ce face ca procesul de pornire să fie un pic mai complicat. Cu toate acestea, acest nod este apoi folosit pentru a calcula toate informațiile necesare pentru construirea și verificarea blocurilor și asigură faptul că minerul deține controlul complet asupra activității sale în curs de desfășurare. Nodul poate funcționa, de asemenea, ca un nod la distanță pentru portofelul propriu al minerului, contribuie la rețea și multe altele.

Cealaltă diferență cheie față de mineritul centralizat este că micii mineri care folosesc p2pool vor avea un pic mai multă "varianță", sau timp între plăți, decât un pool centralizat mare - dar este _extrem de important_ să rețineți că acest lucru nu va duce la câștigarea mai puțin Monero în timp! p2pool va fi la fel de profitabil chiar și pentru micii mineri în timp ca și pool-urile centralizate. O parte din această variație este, de asemenea, compensată de faptul că p2pool are în mod nativ 0% taxe, deoarece nu există un operator de pool centralizat care să plătească pentru serviciile lor!

## Cum pot începe?

## Cum pot începe?

Din fericire, datorită designului excelent al implementării p2pool de la Monero și a numeroșilor oameni din comunitate care au investit timp pentru a ajuta la simplificarea procesului de minerit prin p2pool, începerea devine din ce în ce mai simplă în timp. Există mai multe modalități de a începe să mineri cu p2pool, dar cum detaliile tehnice depășesc scopul acestui articol, nu ezitați să săriți la un link de mai jos, în funcție de sistemul dumneavoastră de operare:

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## Cum pot afla mai multe?

## Cum pot afla mai multe?

Dacă acest lucru ți-a stârnit curiozitatea în jurul mineritului p2pool, aruncă o privire mai jos pentru câteva link-uri suplimentare și explicații despre p2pool, cum funcționează și ce înseamnă pentru Monero:

  * [Github-ul oficial pentru p2pool](https://github.com/SChernykh/p2pool)
  * [Documentele oficiale despre utilizarea p2pool](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool este acum live](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, a "block explorer" of sorts for p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Serghei Chernykh: Cu privire la dezvoltarea lui P2Pool, un pool minier descentralizat XMR](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

Lecturi suplimentare

  * [Cum permite Monero în mod unic economiile circulare](/knowledge/monero-circular-economies)/

  * [Semnături inelare Monero vs CoinJoin ca în Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [De ce (și cum!) ar trebui să vă păstrați propriile chei](/knowledge/hold-your-keys)/

  * [Contribuind înapoi la Monero](/knowledge/contributing-to-monero)/

  * [Cum afectează nodurile de la distanță confidențialitatea Monero](/knowledge/remote-nodes-privacy)/

  * [Cum folosește Monero hard-fork-urile pentru a moderniza rețeaua](/knowledge/network-upgrades)/

  * [Vezi etichete: Cum un singur octet va reduce timpii de sincronizare a portofelului Monero cu 40%+](/knowledge/view-tags-reduce-monero-sync-time)/

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