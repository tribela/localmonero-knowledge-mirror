---
title: "Kako Obročni Podpisi Prikrijejo Izhode Monera"
slug: "ring-signatures"
date: "2020-09-08"
image: "/images/rings.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero je znan daleč naokoli po vsem kripto prostoru kot kralj kovancev za zasebnost. Čeprav vsi vedo, da Monero ponuja dobro zasebnost, jih le malo razume, kako zasebnost deluje.

Številni drugi kovanci za zasebnost objavljajo infografike primerjalnih grafikonov, ki navajajo imena tehnologije zasebnosti vsakega kovanca, v večini pa tehnologijo Monero označujejo kot RingCT, vendar je to le delno res. Monero ima dejansko tristranski pristop k zasebnosti. Ena tehnologija za skrivanje prejemnika transakcije, ena za skrivanje poslanega zneska in ena za skrivanje uporabljenega izhoda, to so prikriti naslovi, RingCT oziroma obročni podpisi.

Ta tristranski pristop pomeni, da če ena od tehnologij pokvari, ostale nimajo nujno enake usode. Podpisi obročev so najšibkejši člen v shemi zasebnosti; beseda šibek tukaj pomeni najbolj dovzeten za hevristične napade. Vzemimo si nekaj časa, da jih raziščemo, kajne?

Kot je omenjeno zgoraj, je cilj obročnih podpisov zakriti izhod, uporabljen v transakciji. Če vas terminologija „vhod/izhod“ kriptovalute zmede, ne skrbite. Pravzaprav ni tako zapleteno. Ko slišite "izhod", samo pomislite na ček. Ena tistih stvari, ki niso več tako pogoste, s katerimi ljudje plačujejo. Tako kot ček je lahko označen v poljubnem znesku - 10 $, 32,50 $ itd. - in se izmenjuje med pogodbenimi strankami. Za kriptovalute izhodi služijo tem funkcijam.

Ko vam nekdo plača 10 Monero, prejmete izhod 10 XMR. Ta izhod ima vrednost (10) in je tisto, kar je vzeto iz denarnice pošiljatelja, na enak način, ko plačate storitev, račun zapusti vašo fizično denarnico in se izroči osebi, pri kateri kupujete.

Izhod je skrit tako, da sestavi obroč (od tod tudi ime "ring") izhodov za vabo. Vendar te vabe niso 'ponarejeni' rezultati. Gre za resnične pretekle izhode iz verige blokov, ki nimajo nobene zveze s sedanjo transakcijo, toda zunanjemu opazovalcu se lahko vsak od teh izhodov zdi enako verjeten kot resnični. Velikost nabora vabnih izhodov, skupaj s pravim, se imenuje velikost obroča, trenutno pa je Monero enajst. Torej obstaja deset izhodov za vabo in en pravi.

Zakaj tega števila preprosto ne povečamo na 100 ali celo 1000? Več kot je, bolje je, kajne? No, z vidika zasebnosti, da, vendar je treba upoštevati še druge stvari. Vrnimo se k fizičnemu primeru, da vidimo, kaj mislim. Če bi želeli enega od svojih dolarskih bankovcev skriti med deset vab, bi morali v denarnici nositi približno enajst dolarjev za vsak dolar, ki bi ga želeli porabiti. En pravi dolar in deset lažnih. Že to postane precej okorno, če želite porabiti celo nekaj dolarjev. Zdaj pa si predstavljajte, da smo znesek za vabo povečali na 1000. Za vsak en dolar, ki ste ga želeli porabiti, bi morali imeti pri sebi približno 1001 dolar. S seboj bi morali nositi aktovko, da bi kupili samo eno sladkarije! Pomembno je omeniti, da prstanski podpisi ne delujejo povsem na ta način, na primer, vabe same niso del podpisa, le sklicevanja nanje, vendar upamo, da bo ta analogija nekoliko v pomoč pri predstavitvi osnovnih konceptov.< /p>

Vabe na blockchainu delujejo podobno. Vsaka dodana vaba poveča čas in stroške preverjanja transakcije. Vsako vozlišče mora prenesti celoten obročni podpis za vsako transakcijo in vsak obročni podpis vsebuje dejanski izhod ter vabe. Ne samo to, ampak mora preveriti matematiko, ali je vsaj eden od teh izhodov resničen, čas preverjanja matematike pa se prav tako poveča z vsako vabo. To pomeni, da moramo najti srečno srednjo pot, kjer je velikost obroča dovolj velika, da ustrezno zakrije dejanski izhod, tudi pred številnimi hevrističnimi napadi, vendar dovolj majhna, da ne povzroči hitrega povečevanja verige blokov. Ni dovolj, da izberemo poljubno število ali samo povečamo velikost obroča, ko zmanjšamo podpis (kot na primer pri CLSAG). Skupnost Monero želi konkretne, matematične dokaze o tem, katera velikost obroča ponuja najboljše kompromise. Število premajhno in zasebnost ne bo dovolj močna proti hevrističnim napadom. Prevelik in morda bomo imeli le obrobno korist na strani zasebnosti in po nepotrebnem trpeli v zvezi s skaliranjem.

Še zadnja stvar, ki jo je treba omeniti. Nekatera literatura Monero poenostavlja in pravi, da obročni podpisi skrivajo pošiljatelja, vendar to ni povsem res in razlika ni samo pedantna. Razlika med pošiljateljem (človekom) in izhodom (računom) je velika, ko gre za ohranjanje zasebnosti. Čeprav je izhod lahko povezan s pošiljateljem, izhod sam po sebi ni enak pošiljatelju. Torej, tudi če bi bil podpis obročka prelomljen, ni nujno, da je povezan z identiteto osebe, znesek in prejemnik pa sta še vedno skrita, kar zmanjšuje škodo, povzročeno zasebnosti vseh strani.

To ne pomeni, da je pokvarjen prstanski podpis nepomemben. Vsi razkriti metapodatki so slabi in lahko razkrijejo več informacij, kot si mislimo, zlasti če se uporabljajo v povezavi z drugimi metapodatki. Zato se po najboljših močeh trudimo zagotoviti, da je za odločitvijo izbrane velikosti prstana akademska strogost, da je uhajanje drugih metapodatkov čim manjše in da uporabniška izkušnja privzeto uporablja najboljša možna dejanja.

Če pa vas verjetnost pokvarjenega podpisa še vedno skrbi, je na obzorju nekaj neverjetnih novic. Naslednja generacija protokolov za zasebnost, na katerih se dela, kot so Triptych, Arcturus in Lelantus, ima res čudovite zmogljivosti. V teh protokolih se velikost spreminja logaritemsko in ne linearno, ko se velikost prstana povečuje. To pomeni, da lahko namestimo 100 vab, vendar je uporabljeni prostor bližje velikosti obroča 10 v stari tehnologiji. To je precejšnja razlika in bo znatno izboljšala zasebnost povsod.

V igri mačke in miši, ki je zasebnost, Monero nenehno uvaja inovacije, da ostane pred krivuljo in zagotovi najboljšo praktično zasebnost za vse.

Vabe na blockchainu delujejo podobno. Vsaka dodana vaba poveča čas in stroške preverjanja transakcije. Vsako vozlišče mora prenesti celoten obročni podpis za vsako transakcijo in vsak obročni podpis vsebuje dejanski izhod ter vabe. Ne samo to, ampak mora preveriti matematiko, ali je vsaj eden od teh izhodov resničen, čas preverjanja matematike pa se prav tako poveča z vsako vabo. To pomeni, da moramo najti srečno srednjo pot, kjer je velikost obroča dovolj velika, da ustrezno zakrije dejanski izhod, tudi pred številnimi hevrističnimi napadi, vendar dovolj majhna, da ne povzroči hitrega povečevanja verige blokov. Ni dovolj, da izberemo poljubno število ali samo povečamo velikost obroča, ko zmanjšamo podpis (kot na primer pri CLSAG). Skupnost Monero želi konkretne, matematične dokaze o tem, katera velikost obroča ponuja najboljše kompromise. Število premajhno in zasebnost ne bo dovolj močna proti hevrističnim napadom. Prevelik in morda bomo imeli le obrobno korist na strani zasebnosti in po nepotrebnem trpeli v zvezi s skaliranjem.

Še zadnja stvar, ki jo je treba omeniti. Nekatera literatura Monero poenostavlja in pravi, da obročni podpisi skrivajo pošiljatelja, vendar to ni povsem res in razlika ni samo pedantna. Razlika med pošiljateljem (človekom) in izhodom (računom) je velika, ko gre za ohranjanje zasebnosti. Čeprav je izhod lahko povezan s pošiljateljem, izhod sam po sebi ni enak pošiljatelju. Torej, tudi če bi bil podpis obročka prelomljen, ni nujno, da je povezan z identiteto osebe, znesek in prejemnik pa sta še vedno skrita, kar zmanjšuje škodo, povzročeno zasebnosti vseh strani.

To ne pomeni, da je pokvarjen prstanski podpis nepomemben. Vsi razkriti metapodatki so slabi in lahko razkrijejo več informacij, kot si mislimo, zlasti če se uporabljajo v povezavi z drugimi metapodatki. Zato se po najboljših močeh trudimo zagotoviti, da je za odločitvijo izbrane velikosti prstana akademska strogost, da je uhajanje drugih metapodatkov čim manjše in da uporabniška izkušnja privzeto uporablja najboljša možna dejanja.

Če pa vas verjetnost pokvarjenega podpisa še vedno skrbi, je na obzorju nekaj neverjetnih novic. Naslednja generacija protokolov za zasebnost, na katerih se dela, kot so Triptych, Arcturus in Lelantus, ima res čudovite zmogljivosti. V teh protokolih se velikost spreminja logaritemsko in ne linearno, ko se velikost prstana povečuje. To pomeni, da lahko namestimo 100 vab, vendar je uporabljeni prostor bližje velikosti obroča 10 v stari tehnologiji. To je precejšnja razlika in bo znatno izboljšala zasebnost povsod.

V igri mačke in miši, ki je zasebnost, Monero nenehno uvaja inovacije, da ostane pred krivuljo in zagotovi najboljšo praktično zasebnost za vse.

Nadaljnje branje

  * [Kako Monero edinstveno omogoča krožna gospodarstva](/knowledge/monero-circular-economies)/

  * [Obročni ring podpisi Monero vs CoinJoin kot v Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Zakaj (in kako!) bi morali imeti svoje ključe](/knowledge/hold-your-keys)/

  * [Prispevek nazaj v Monero](/knowledge/contributing-to-monero)/

  * [Kako oddaljena vozlišča vplivajo na zasebnost Monera](/knowledge/remote-nodes-privacy)/

  * [Kako Monero uporablja hard-forke za nadgradnjo omrežja](/knowledge/network-upgrades)/

  * [Ogled oznak: Kako bo en bajt skrajšal čas sinhronizacije Monero denarnice za 40%+](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool in Njegova Vloga pri Decentralizaciji Monero Rudarjenja](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Kaj bo Naredil za Monero](/knowledge/seraphis-for-monero)/

  * [Ali je Pretvorba Bitcoina v Monero Enako Zasebna kot Neposredni Nakup Monera?](/knowledge/most-private-way-to-buy-monero)/

  * [Zakaj Monero Uporablja Nezaupljivo nNastavitev za Razliko od Zcasha](/knowledge/monero-trustless-setup)/

  * [Zakaj je Monero Boljši Hranilnik Vrednosti kot Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Kako lahko Monero premaga omrežne učinke Bitcoina](/knowledge/network-effect)/

  * [Zakaj ima Monero Najbolj Kritično Mislečo Skupnost](/knowledge/critical-thinking)/

  * [Prevare, na Katere Morate Biti Pozorni pri Uporabi Monera](/knowledge/monero-scams)/

  * [Kako Bodo Atomske Menjave v Monero Delovale](/knowledge/monero-atomic-swaps)/

  * [Kaj Mora Vsak Uporabnik Monera Vedeti, ko Gre za Mreženje](/knowledge/monero-networking)/

  * [Kako RingCT Prikrije Zneske Monero Transakcij](/knowledge/monero-ringct)/

  * [Kako Naslovi Monero Stealth Ščitijo Vašo Identiteto](/knowledge/monero-stealth-addresses)/

  * [Kako Monero Podnaslovi Preprečujejo Povezovanje Identitet](/knowledge/monero-subaddresses)/

  * [Pojasnjeni Monero Izhodi (Outputs)](/knowledge/monero-outputs)/

  * [Najboljše Monero Prakse za Začetnike](/knowledge/monero-best-practices)/

  * [Kako je Monero Rešil Problem Velikosti Bloka, ki muči Bitcoin](/knowledge/dynamic-block-size)/

  * [Kako bo CLSAG Izboljšal Učinkovitost Monera](/knowledge/what-is-clsag)/

  * [Zakaj Ima Monero Tail Emisijo](/knowledge/monero-tail-emission)/

  * [Kratka zgodovina Monera](/knowledge/monero-history)/

  * [Wired Magazine se Moti Glede Monera. Evo, Zakaj](/knowledge/wired-article-debunked)/

  * [Razbijamo 15 glavnih mitov in pomislekov o Monero](/knowledge/monero-myths-debunked)/

  * [Kako Dandelion++ Ohranja Zasebnost Izvora Transakcije Monero](/knowledge/monero-dandelion)/

  * [Zakaj je Monero Odprtokoden in Decentraliziran](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero rudarjenje: zakaj je RandomX tako poseben](/knowledge/monero-mining-randomx)/

  * [Zakaj je Monero Boljši od Dash, Zcash, Zcoin (tudi z Lelantusom), Grin in Bitcoin Mikserji, kot je Wasabi (posodobljeno maja 2020)](/knowledge/why-monero-is-better)/

Nadaljnje branje