---
title: "Monero žiedo parašai prieš CoinJoin kaip Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Kadangi „Bitcoin“ privatumo įrankiai sulaukė daugiau dėmesio ir jų naudojimo, jie buvo labiau kontroliuojami. Atlikus šį patikrinimą, [neseniai bitkoinų privatumo įrankis Wasabi Wallet paskelbė ](https://twitter.com/wasabiwallet/status/1503091503207432193), kad jie pradės cenzūruoti ir atmesti gaunamus mišinius, kurie, jų nuomone, yra neteisėti arba prieštarauja jų paslaugų teikimo sąlygoms, ir mokės už grandinės analizę. įmonei „pastebėti“ gaunamus mišinio dalyvius.

CoinJoin operacijų naudojimas siekiant paslėpti Bitcoin lėšų šaltinį jau daugelį metų buvo Bitcoin privatumo pagrindas, o su jo naudojimu susijusios problemos ir rizika yra keletas pagrindinių problemų, kurias Monero žiedo parašai ištaiso ir užkerta kelią. 

Šiame tinklaraščio įraše trumpai pažvelgsime į „CoinJoin“ ir žiedinių parašų palyginimą, taip pat į tai, kodėl Monero taikomas metodas padidina atsparumą cenzūrai, didesnį privatumą ir mažiau vargo vartotojams.

## Kas yra CoinJoin sandoris?

Kadangi visi Bitcoin sandoriai yra visiškai skaidrūs – atskleidžiamas siuntėjas, gavėjas ir sumos, vartotojai turi imtis papildomų veiksmų, kad apsaugotų savo privatumą nuo ankstesnių siuntėjų ir būsimų lėšų gavėjų arba rizikuotų cenzūra, priežiūra ar lėšų vagystė per fizinis smurtas.

Geriausias šiandieninis Bitcoin privatumo sprendimas yra įrankis, vadinamas [„CoinJoin“](https://bitcoiner.guide/qna/coinjoin/), kuriame 2 ar daugiau vartotojų dirba kartu (paprastai per centralizuotą koordinatorių), kad sukurtų specialią operaciją, kuri apsunkina pašalinius veiksmus. stebėtojai sujungti įėjimus su išėjimais. Kiekvienas dalyvis praneša, kad bendrai sudarys sandorį, neperduodamas savo lėšų saugojimo, ir pabaigoje gauna išvestį, kurios ankstesnė istorija dabar yra neaiški (arba užtemdyta) išorės stebėtojams.

Tai sulaužo konkrečių UTXO istoriją, todėl Bitcoin naudotojai gali įgyti šiek tiek išankstinės paslapties atliekant sandorius. Tačiau CoinJoin (kaip įdiegta Wasabi Wallet ir Samourai Wallet, dviejuose dažniausiai naudojamuose Bitcoin CoinJoin įrankiuose) turi keletą pagrindinių trūkumų: 

  * Kadangi CoinJoin operacijos yra visiškai pasirenkamos ir reikalauja aktyvaus dalyvavimo, bet kuris dalyvis būtinai parodo, kad siekia didesnio privatumo nei „paprasti“ Bitcoin vartotojai, todėl gali juos išskirti ir sukelti problemų išleidžiant lėšas daugelyje reguliuojamų biržų ar subjektų. Kiekvienas vartotojas negali neigti, kad dalyvavo „CoinJoin“ operacijoje.
  * Kad būtų galima rasti kitų, su kuriais būtų galima prisijungti prie „CoinJoin“, dauguma „CoinJoin“ metodų (įskaitant „Wasabi Wallet“) naudoja centralizuotą koordinatorių, kuris sujungia dalyvius ir padeda jiems bendrauti bei sukurti tinkamą „CoinJoin“ operaciją. Šis centralizuotas koordinatorius niekada nesaugo naudotojo lėšų, tačiau įgyja išsamių įžvalgų apie jų koordinuojamas operacijas, gali cenzūruoti gaunamus duomenis (kaip „Wasabi Wallet“ atveju) ir gali būti spaudžiamas rinkti arba dalytis informacija apie „CoinJoin“ dalyvius.[X2068X ] 
  * Naudotojams, turintiems daug lėšų CoinJoin, dažnai gali tekti laukti valandų (ar net dienų!), kad surastų pakankamai dalyvių, su kuriais galėtų prisijungti, ir dėl to labai vėluojama nuo to momento, kai vartotojas gauna lėšų, iki tada, kai gali jas išleisti privačiai. 
  * Privatumas, suteikiamas atliekant CoinJoin operaciją, laikui bėgant blogėja, nes kiti dalyviai išleidžia lėšas arba susieja savo išvesties duomenis su savo tapatybe per KYC mainus, prekybininkus, kuriems reikalingas ID ir kt. Tai reiškia, kad naudotojai idealiai palaiko savo lėšas nuolat mažėjančias atliekant CoinJoin operacijas. jų anonimiškumas („minia, kurioje reikia pasislėpti“) nustatytas kuo naujesnesnis.
  * Daugumoje „CoinJoin“ metodų dalyviai turi naudoti fiksuoto dydžio UTXO (t. y. 0,1 BTC), kad būtų sunkiau sujungti „CoinJoin“ operacijų įvestis ir išvestis. Tai lemia didesnius mokesčius (reikalingi daugiau atskirų operacijų vienam dideliam įvesties kiekiui), daugiau „toksiškų pokyčių“ (lėšos, kurių negalima išleisti be rimtos rizikos privatumui), ir gali būti, kad mažesni vartotojai apskritai negalės derinti, jei neturi minimalus reikalingas likutis.

## Kaip žiediniai parašai išsprendžia šias problemas?

Kadangi [ nuodugniai išnagrinėjome, kas yra žiedo parašai praeityje](/knowledge/ring-signatures), šiame tinklaraščio įraše nenagrinėsiu jų veikimo techninių aspektų. Vietoj to pažiūrėsime, kaip Monero taikomi metodai išsprendžia problemas, kurias aptaria aukščiau aptartas CoinJoin.

> „CoinJoin“ pasirenkama ir reikia dalyvauti

Monero skambėjimo parašai yra pagrindinė privatumo protokolo funkcija, o _kiekviena_ tinklo operacija juos naudoja. Tai reiškia, kad nė vienas vartotojo sandoris neišsiskiria siekdamas didesnio privatumo nei „paprasti“ Monero naudotojai, o visi vartotojai įtikinamai paneigti, kad išleido lėšas atlikdami bet kurią operaciją. Kadangi vartotojas, išleidžiantis lėšas, nekoordinuoja ir nedalyvauja su jais naudojamomis operacijomis, naudotojai, kuriems priklauso įvestis, kuri atsitiktinai buvo atrinkta kaip apgaulė, gali nuoširdžiai pasakyti, kad nedalyvavo toje operacijoje, stiprindami savo privatumą.

> Centrinio koordinatoriaus naudojimas

Kadangi Monero žiediniai parašai yra visiškai nekoordinuoti ir sandoriui sukurti reikia tik tikro lėšų išleidusio asmens, Monero centralizuoto koordinatoriaus nereikia. Taip užtikrinama, kad _niekas_ negalės jums uždrausti prieigos prie Monero privatumo ir nėra jokio centralizuoto subjekto, kuriam būtų galima daryti spaudimą, nėra lengvų Sybil atakų prieš likvidumą ir t. t. Tol, kol jūsų sandoris moka tinkamus mokesčius, jūs gaunate necenzūrinę prieigą prie privatumo, saugumo ir anonimiškumo Monero.

> „CoinJoin“ reikia likvidumo

„Likvidumas“, kurį gali naudoti visi, išleidžiantys „Monero“ kaip masalus, visada yra visas grandinėje esančių išėjimų rinkinys, todėl niekada netrūks jaukų, kuriuose būtų galima pasislėpti su Monero. Asmuo, norintis išleisti Monero, gali tai padaryti apie 20 minučių po lėšų gavimo ir nereikia atlikti jokių papildomų veiksmų, kad įgytų tvirtą Monero privatumą.

> „CoinJoin“ privatumas laikui bėgant blogėja

Kadangi „Monero“ išvesties tinklas niekada nenaudoja, todėl skambučio parašų suteikiamas privatumas laikui bėgant yra daug mažiau pablogėjęs. Naudotojui nereikia nuolat keisti išvesties Monero, o ne itin retais atvejais, laikui bėgant jis nepraranda privatumo.

Jei vartotojas nori „atnaujinti“ su išvestimi naudojamus jaukus, jis gali tiesiog grąžinti lėšas sau ir galės jas išleisti apie 20 minučių vėliau, kaip įprasta.

> CoinJoin paprastai reikia fiksuoto dydžio įvesties

Kadangi sumos yra paslėptos kiekvienoje operacijoje naudojant [„Confidential Transactions“](/knowledge/monero-ringct) („RingCT“ dalis), bet kokioje operacijoje naudojami jaukai gali būti bet kokio dydžio. Nėra jokios priežasties nerimauti dėl sumomis pagrįstos euristikos sistemoje „Monero“, todėl sandorius sudaryti daug paprasčiau ir jie gali panaudoti apgaulę bet kuriuo momentu ir bet kokios sumos Monero blokų grandinėje.

## Kaip galiu sužinoti daugiau?

Jei jums įdomu ir norite geriau suprasti skambučio parašus ar CoinJoin operacijas, žr. toliau pateiktas nuorodas, kur rasite puikių vietų pradėti:

  * [Kaip skambėjimo parašai uždengia Monero išvestis](/knowledge/ring-signatures)
  * [Žiedo parašas – Moneropedija](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [„Coinjoin Q+A“](https://bitcoiner.guide/qna/coinjoin/)
  * [ „CoinJoin“ apžvalga](https://6102bitcoin.com/coinjoin-overview/)

Papildoma literatūra