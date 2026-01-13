---
title: "Paaiškinti Monero išėjimai"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero, kaip ir kitos kriptovaliutos, išvestis naudoja kaip lėšų apskaitos priemonę. Daugelis kriptovaliutų išmanančių vartotojų tikriausiai yra girdėję šį terminą, tačiau ne visi supranta, ką jis reiškia ir kaip veikia. Kaip išnagrinėta mūsų [ žiedinių parašų straipsnyje](/knowledge/ring-signatures), išvestis yra tikrasis bloko grandinės vienetas, kuriuo keičiasi sandorio šalys. Panašus į dolerio banknotą, tačiau suma nėra fiksuota nominaliąja verte.

Jei už darbą gausite 16 USD, galite gauti vieno dolerio, penkių ir dešimties dolerių banknotą. Jūs turite 16 USD, bet savo piniginėje taip pat turite tris skirtingas kupiūras. Jei norite sumokėti kam nors 6 dolerius, galite naudoti 5 ir 1 banknotus, bet jei norėtumėte sumokėti 8 USD, galite panaudoti tik 10 USD ir atgauti 2 USD. Galiausiai, jei norėtumėte sumokėti kam nors 14 USD, turėsite panaudoti visas tris sąskaitas ir atgautumėte 2 USD keitimu, tačiau akimirką, kai atiduosite visas tris sąskaitas, jūsų piniginėje nėra pinigų, kol negausite pakeisti atgal.

Monero veikia panašiai. Tarkime, turite parduotuvę ir tris kartus išparduodate tris skirtingas prekes. Iš viso galite gauti 1,5 XMR, 2,25 XMR ir 5,25 XMR už 9 XMR, tačiau piniginėje taip pat turite tris skirtingus anksčiau nurodytų nominalų išvestis. Kaip ir su doleriais, galbūt norėsite kam nors sumokėti 3 XMR. Galite naudoti tik 5,25 XMR išvestį ir sugrąžinti 2,25 XMR, arba galite sujungti 1,5 ir 2,25 XMR išvestis ir gauti 0,75 XMR pakeitimą.

Tačiau kai tik išsiųsite operaciją, jūsų naudojami išėjimai perkeliami į „užrakinimo“ būseną, o tai reiškia, kad jie bus nepasiekiami, kol negrąžinsite pakeitimo. Protokolas atrakina lėšas (t. y. grąžina pakeitimą) po 10 patvirtinimų arba maždaug 20 minučių. Lygiai taip pat, kaip išdavus dolerio kupiūras iš savo piniginės, pinigų nebegalite panaudoti tol, kol negrąžinsite keitimo iš kasos, jūsų Monero nepasieksite, kol neatgausite keitimo.

Grįžkime prie pavyzdžio, kai kam nors siunčiate 3 XMR, o jūs naudojate 5,25 XMR išvestį. Dabar, kol laukiate, kol 1,75 XMR vėl pasikeis, negalite jo naudoti. Šis 1,75 XMR jums nepasiekiamas. Tačiau vis tiek galite naudoti 1,5 XMR ir 2,25 XMR išėjimus, nes jie nebuvo išleisti. Grįžtant prie dolerio pavyzdžio, jei sumokėjote kam nors 8 USD, kaip ir ankstesniame pavyzdyje, negalėsite panaudoti 2 USD, kurių tikitės grąžinti pakeitimu, kol jie jums nebus suteikti, tačiau šiame pavyzdyje vis tiek turite 10 USD banknotas, kuris yra nepanaudotas jūsų piniginėje. Kol laukiate pakeitimo, tai vis tiek galite naudoti norėdami įsigyti bet ką, ko norite. Tas pats su Monero.

Tai dažnai kelia painiavą naujiems Monero naudotojams. Dažnai vartotojas savo piniginėje gali turėti tik vieną išvestį, gautą iš mainų ar draugo. Tarkime, kad ši išvestis yra 20 XMR. Kitų išėjimų jie savo piniginėje neturi. Dabar jie nori paaukoti dviem savo mėgstamoms labdaros organizacijoms. Jie išsiunčia 5 XMR pirmajai labdaros organizacijai, o paskui sutrinka, nes, nors jiems turėtų likti 15 XMR, jie negali iš karto išsiųsti kitos aukos antrajai labdarai. Kaip jau galėjote atspėti, taip yra todėl, kad 15 XMR yra užrakintas. Jis negali būti išleistas, kol jis nebus grąžintas kaip pakeitimas (10 patvirtinimų arba maždaug 20 minučių). Kai jų lėšos bus atblokuotos, jie galės išsiųsti antrąją auką.

Pakartotinai, jie nebūtų turėję šios problemos, jei vietoj to būtų turėję kelis išėjimus, pvz., du 10 XMR išvesties ar panašiai. Jie galėtų siųsti abi aukas vieną iš karto po kitos, nes pirmą kartą paaukojus būtų naudojamas vienas iš 10 XMR išėjimų (ir lauktų 10 patvirtinimų, kad būtų grąžinti 5 XMR pakeitimai), o antroji auka naudotų kitus 10 XMR. išvestis.

Kai kurios kriptovaliutų piniginės turi funkciją, vadinamą „išvesties valdymu“, kuri tiesiog parodo vartotojui, kokius išėjimus jis šiuo metu turi (be bendros sumos), taip pat leidžia pasirinkti, kurias iš jų nori naudoti išleisdamas. jų kriptovaliuta.

Nuo šiol „Monero“ GUI išvesties pasirenka vartotojams automatiškai, nes vartotojai, pasirenkantys savo išvestis, dažnai sukelia painiavą arba kai kuriais atvejais pažeidžia privatumą. Tačiau yra kuriamos piniginės, pvz., naujasis „Feather“ piniginės projektas, kuriame bus šios išvesties valdymo funkcijos.

Daug kalbėjome apie siuntimo dalį, bet kažkas įspūdingo nutinka gavimo pusėje. Grįžtant prie mūsų pavyzdžio, kai kam nors buvo siunčiami 3 XMR ir naudojant jūsų 1,5 XMR ir 2,25 XMR išėjimus (nors tikimasi 0,75 XMR pokyčio), imtuvas negauna dviejų 1,5 XMR ir 2,25 XMR išėjimų. Vietoj to jie gauna VIENĄ 3 XMR išvestį.

Fone protokolas sujungia visas išlaidoms panaudotas išvestis ir suteikia gavėjui vieną išvestį nuo sumokėtos sumos, o vieną pakeitimo išvestį siunčia atgal siuntėjui. Taigi siuntėjas taip pat gaus vieną išvestį atgal kaip pakeitimą, neatsižvelgiant į tai, ar transakcijai išsiųsti naudojo du, tris ar dešimt išvesties.

Tikimės, kad tai išsklaidė tam tikrą painiavą dėl išvesties ir kaip veikia vidinė protokolo apskaita, taip pat į dažną vartotojo painiavos problemą, kai susiduria su užrakintomis lėšomis. Kitame straipsnyje mes išnagrinėsime jūsų išvesties tvarkymą, kad sumažintume tikimybę, kad prieš siunčiant būsimas operacijas teks laukti atblokuotų lėšų.

Papildoma literatūra