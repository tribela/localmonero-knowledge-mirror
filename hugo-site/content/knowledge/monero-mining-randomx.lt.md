---
title: "Monero kasyba: kuo „RandomX“ toks ypatingas"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
2019 m. lapkričio 30 d. „Monero“ įvyko pusmetinis „hard fork“, kurio laukiamiausias pokytis buvo perėjimas nuo senojo PoW algoritmo „cryptonight“ prie visiškai naujo, viduje sukurto „RandomX“. Monero bendruomenė mano, kad RandomX yra didelis žingsnis link egalitarinės kasybos, tačiau pasigilinkime, kad pamatytume, ar taip yra.

## Tikslas

Norėdami nuspręsti, ar RandomX yra patobulinimas, pirmiausia turime suprasti, koks yra kasybos tikslas. Kasyba apsaugo blokų grandinę nuo dvigubų išlaidų per „Nakamoto Consensus“. Tikslios gudrybės, kaip tai padaryti, nepatenka į šio straipsnio taikymo sritį, tačiau jų galima sužinoti iš daugybės skirtingų šaltinių internete. Svarbu tai, kad saugumas gaunamas iš maišos, kurią generuoja kompiuteriai (mineriai), konkuruodami vieni su kitais ieškant matematinio sprendimo, reikalingo sukurti kitą bloką. Tai darydami jie prideda naujų operacijų į blokų grandinę. Už darbą (maišos) jiems atlyginama naujai nukaldintomis monetomis.   
  
Naudojant šią sąranką gali kilti daugybė problemų, todėl norint tinkamai veikti, joms reikia tinkamų paskatų, tačiau mes sutelksime dėmesį į vieną konkrečią problemą, kuri gali kilti. Jei kasyba turėtų būti konkurencija, kas atsitiks, kai vienas kalnakasys įgyja pranašumą?

## Fonas

Dėl konteksto pakalbėkime šiek tiek apie kasybos įrangą. Kalnakasiai darbui atlikti naudoja kompiuterius, tačiau visi žinome, kad ne visi kompiuteriai pagaminti vienodai. Kai kurie kompiuteriai yra pakankamai galingi, kad galėtų paleisti dirbtinio intelekto tinklus ar intensyvius žaidimus, o kiti susiduria su net paprastomis užduotimis. Šie skaičiavimo galios skirtumai taip pat turi įtakos maišos greičiui arba greičiui, kuriuo jie ieško blokinių sprendimų.   
  
Tačiau net ir šie skirtumai tarp kompiuterių nublanksta prieš specializuotos aparatinės įrangos, kitaip dar vadinamų Application Specific Integrated Circuits (ASIC), maišos rodiklius, kurie keliais dydžiais lenkia įprastus kompiuterius.  
  
Skirkime šiek tiek laiko ir išsiaiškinkime, kas daro ASIC tokias galingas. Įsivaizduokite, kad visi kompiuteriai patenka į kažkurį spektrą, kuris svyruoja nuo gebėjimo atlikti daug dalykų, bet nieko gero, iki atlikti tik vieną dalyką, bet tai daro labai gerai. CPU ir ASIC yra priešinguose šio spektro galuose.  
  
CPU, kurie yra visuose standartiniuose kompiuteriuose, yra pirmame gale. Jie gali atlikti daugybę dalykų, pvz., naršyti internete, žaisti žaidimus ar pateikti vaizdo įrašus, bet ne itin gerai. Tačiau šis lankstumas kainuoja efektyvumą.  
  
ASIC yra kitame gale, kur jie gali atlikti tik vieną dalyką, bet tai daro neįtikėtinu greičiu. Jie gali atlikti tik vieną matematinę funkciją, bet kadangi jie gali nepaisyti viso kito, našumo padidėjimas yra astronominis. Tačiau šis efektyvumas kainuoja lankstumą, taigi, jei funkcija nors ir šiek tiek pasikeičia (pavyzdžiui, x + y = z pasikeičia į 2x + y = z), ASIC visiškai nustos veikti.   
  
Ne visi turi ASIC, bet visi turi savo kompiuterius. Tai gali sukelti nesąžiningą pranašumą.

## Linksma analogija

Jei tai vis tiek klaidina, galbūt padės ši analogija. Įsivaizduokite loteriją, kurioje kas valandą skiriamas tūkstantis dolerių, o ši loterija leidžia atsispausdinti savo bilietus! Pradedate spausdinti kuo daugiau bilietų savo namų spausdintuvu, kuris gali atspausdinti vieną bilietą per sekundę. Atėmus elektros ir rašalo išlaidas, matote, kad vis tiek galite uždirbti pelno, net jei loterijoje laimite tik kartą per kelias savaites.  
  
Laikui bėgant plečiate savo veiklą, kol turėsite visą kambarį, skirtą spausdintuvams. iš viso 20. Viskas gerai...iki vienos lemtingos dienos.  
  
Yra didelių naujienų. Kažkas išrado naujo tipo spausdintuvą. Galima spausdinti tik loterijos bilietus. Jis negali spausdinti nuotraukų ar biuro dokumentų arba atlikti dvipusio spausdinimo. Tik loterijos bilietai. Tačiau jis gali juos spausdinti 1000 bilietų per sekundę greičiu. Jūs žiūrite į savo mažą spausdintuvų kambarį. 20 spausdintuvų. Jums reikia dar 980 spausdintuvų, kad galėtumėte neatsilikti nuo VIENO iš šių monstrų spausdintuvų, o jei kas nors turi du…?  
  
Deja, išeinate iš loterijos, nes nebegalite pateisinti elektros ir rašalo išlaidų.  
  
Bet palauk! Po poros savaičių bus daugiau naujienų! Pasikeitė bilieto dizainas. Dabar skaičiai, kurie anksčiau buvo viršuje, dabar yra apačioje. Naujieji monstriniai spausdintuvai yra tokie nelankstūs, kad negali to padaryti. Jie galėjo sukurti tik ankstesnį dizainą. Neilgai trukus vėl su džiaugsmu spausdinsite. Bent jau tol, kol kas nors pagamins naują pabaisą naujo dizaino spausdintuvą.

## RandomX

Kur „RandomX“ visa tai telpa? Juo siekiama išlyginti ASIC pranašumus, nes labai sunku sukurti ASIC. Tai atliekama reikalaujant, kad kalnakasiai sukurtų ir vykdytų atsitiktinį kodą, o ne maišą, pagrįstą algoritmu.  
  
Gali būti painu, kaip tai iš tikrųjų padeda, todėl grįžkime prie spausdintuvo analogijos. Prisiminkite, kas atsitiko, kai pasikeitė dizainas? Senieji monstriniai spausdintuvai pasensta kiekvieną naktį, o naujus reikėjo kurti atsižvelgiant į naują dizainą. Kas atsitiktų, jei kiekvienas naujas loterijos prizo bilietas turėtų laikytis naujo dizaino standarto kiekvienam naujam prizui?   
  
Sukurti naują monstrų spausdintuvą taptų neįtikėtinai sunku. Nebegalite planuoti tik vieno bilieto dizaino. Kadangi dizainas yra atsitiktinis, monstrų spausdintuvų gamintojai turėtų pridėti spalvų, skirtingų raidžių, kraštinių ir formų spausdinimo būdų ir dar daugiau. Trumpai tariant, mašina, kurią jie išrado, būtų standartinis, įprastas spausdintuvas. Kaip ir visi kiti.  
  
Paprasčiausiai įdiegę šį atsitiktinumą bilietų dizaine, iš esmės sumažinome didelį pranašumą, gautą iš specializuotos aparatinės įrangos. RandomX daro tą patį, bet su kasyba.  
  
Tokiu būdu sumažinami kelių atrinktų turtingų žmonių pranašumai, nes jie investuos į „ASIC“, skirtų „RandomX“ gavybai, kūrimą, jie iš tikrųjų tik išras stipresnius ir geresnius procesorius, kurie bus naudingi visam pasauliui.  
[ X1455X] Tai reiškia, kad mažasis vaikinas su savo 20 bilietų spausdintuvų grįžta į žaidimą. Jam vis dar gali būti sunkiau, nes šie turtingi asmenys vis tiek gali nusipirkti daugiau spausdintuvų nei jis, bet bent jau dabar jis nėra pranašesnis už vieną mašiną. Jis yra savotiškai konkurencingas.  
  
Žinodami, kad net ir mažas vaikinas gali būti konkurencingas kasdamas Monero, raginame visus pabandyti pasinaudoti Monero GUI piniginėje, kuri palaiko solo kasybą, arba atsisiunčiant bendruomenės palaikomą programinę įrangą. Tai lengva, konkurencinga ir atvira visiems.

Papildoma literatūra

  * [Kaip Monero unikaliai įgalina žiedinę ekonomiką](/knowledge/monero-circular-economies)/

  * [Monero žiedo parašai prieš CoinJoin kaip Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Kodėl (ir kaip!) turėtumėte turėti savo raktus](/knowledge/hold-your-keys)/

  * [Prisideda prie Monero](/knowledge/contributing-to-monero)/

  * [Kaip nuotoliniai mazgai veikia Monero privatumą](/knowledge/remote-nodes-privacy)/

  * [Kaip „Monero“ naudoja „hard-forks“ tinklui atnaujinti](/knowledge/network-upgrades)/

  * [Peržiūrėkite žymas: kaip vienas baitas sumažins Monero piniginės sinchronizavimo laiką 40%+](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool ir jo vaidmuo decentralizuojant Monero kasybą](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: ką tai padarys Monero](/knowledge/seraphis-for-monero)/

  * [Ar Bitcoin konvertavimas į Monero yra toks pat privatus, kaip ir tiesioginis Monero pirkimas?](/knowledge/most-private-way-to-buy-monero)/

  * [Kodėl Monero, skirtingai nei Zcash, naudoja patikimą sąranką](/knowledge/monero-trustless-setup)/

  * [Kodėl „Monero“ yra geresnė vertės parduotuvė nei „Bitcoin“.](/knowledge/monero-better-store-of-value)/

  * [Kaip Monero gali įveikti Bitcoin tinklo efektus](/knowledge/network-effect)/

  * [Kodėl Monero turi kritiškiausią mąstymo bendruomenę](/knowledge/critical-thinking)/

  * [Aferos, į kurias reikia atkreipti dėmesį naudojant Monero](/knowledge/monero-scams)/

  * [Kaip atominiai apsikeitimai veiks Monero](/knowledge/monero-atomic-swaps)/

  * [Ką kiekvienas „Monero“ vartotojas turi žinoti, kai kalbama apie tinklų kūrimą](/knowledge/monero-networking)/

  * [Kaip RingCT slepia Monero operacijų sumas](/knowledge/monero-ringct)/

  * [Kaip Monero Stealth Addresses apsaugo jūsų tapatybę](/knowledge/monero-stealth-addresses)/

  * [Kaip Monero subadresai užkerta kelią tapatybės susiejimui](/knowledge/monero-subaddresses)/

  * [Paaiškinti Monero išėjimai](/knowledge/monero-outputs)/

  * [„Monero“ geriausia praktika pradedantiesiems](/knowledge/monero-best-practices)/

  * [Kaip žiedo parašai užgožia Monero išvestis](/knowledge/ring-signatures)/

  * [Kaip Monero išsprendė bloko dydžio problemą, kuri kamuoja Bitcoin](/knowledge/dynamic-block-size)/

  * [Kaip CLSAG pagerins Monero efektyvumą](/knowledge/what-is-clsag)/

  * [Kodėl Monero turi uodegą](/knowledge/monero-tail-emission)/

  * [Trumpa Monero istorija](/knowledge/monero-history)/

  * [Žurnalas „Wired“ klysta dėl Monero, štai kodėl](/knowledge/wired-article-debunked)/

  * [15 populiariausių Monero mitų ir rūpesčių, kurie buvo paneigti](/knowledge/monero-myths-debunked)/

  * [Kaip Dandelion++ išlaiko Monero sandorio kilmę privačią](/knowledge/monero-dandelion)/

  * [Kodėl Monero yra atvirojo kodo ir decentralizuotas](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Kodėl „Monero“ yra geresnis nei „Dash“, „Zcash“, „Zcoin“ (net su „Lelantus“), „Grin“ ir „Bitcoin“ maišytuvai, tokie kaip „Wasabi“ (Atnaujinta 2020 m. gegužės mėn.)](/knowledge/why-monero-is-better)/