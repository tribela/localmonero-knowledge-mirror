---
title: "Peržiūrėkite žymas: kaip vienas baitas sumažins Monero piniginės sinchronizavimo laiką 40%+"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Vienas iš dažniausiai pasitaikančių nusiskundimų, susijusių su Monero naudojimu kasdien, yra laikas, per kurį gali prireikti sinchronizuoti piniginę, kol bus galima išsiųsti Monero. Laimei, Monero bendruomenės kūrėjai ir tyrėjai rado puikų būdą, kaip sumažinti piniginės sinchronizavimo laiką 40%+ be jokio papildomo blokų grandinės išpūtimo, mokesčių ir kt.

Įveskite „view tags“ – kiekvienos operacijos duomenų papildymą vienu baitu – ateinantį į „Monero“ kitą tinklo naujinimą!

## Kodėl Monero piniginės sinchronizavimas yra lėtesnis nei Bitcoin?

Vienas iš pirmųjų klausimų, į kurį turime atsakyti, kad geriau suprastume tokio sprendimo, kaip peržiūros žymos, poreikį yra tai, kodėl Monero piniginės sinchronizavimas yra lėtesnis nei kriptovaliutų, pvz., Bitcoin.

Bitcoin, kadangi visos operacijos nėra privačios ir atskleidžia išleidžiamas monetas, sumas ir grandinėje dalyvaujančius adresus, „Bitcoin“ piniginės gali tiesiog ieškoti bet kokių nepanaudotų operacijų rezultatų (UTXO) arba panaudotų tam tikros piniginės adresų. , greitai nuskaitydami blokų grandinę ir ieškodami tik tiems adresams priklausančių UTXO, kad išsiaiškintumėte, kurios monetos priklauso jūsų piniginei ir kurias galima išleisti.

Tačiau „Monero“ sistemoje visos operacijos išsaugo vartotojo privatumą, nes paslepia siuntėją, gavėją ir su kiekviena operacija susijusias sumas. Šis privatumas, nors ir gyvybiškai svarbus siekiant apsaugoti tinklo vartotojus, taip pat įveda lėtesnį piniginės sinchronizavimą. Monero jūsų piniginė turi palyginti kiekvieną tinkle esančią operacijos išvestį (TXO) su jūsų piniginės privačiais raktais.

Šis palyginimas apima daugybę sudėtingų matematikos ir kriptografijos metodų, kad patvirtintumėte, jog išvestis tikrai priklauso jums, nes visos sumos, adresai ir žinomos išleistos išvesties (arba monetos) yra paslėptos grandinėje Monero.

## Kas yra peržiūros žymos?

Siekdamas sumažinti Monero piniginių sinchronizavimo laiką, [tyrėjas, vardu UkoeHB, pasiūlė naują metodą](https://github.com/monero-project/research-lab/issues/73) – prie kiekvienos operacijos pridėkite 1 baito „žymą“ naudodami tik žinomą bendrinamą paslaptį. tos operacijos siuntėjui ir gavėjui.

Šią bendrinamą paslaptį sugeneruoja siuntėjas, naudodamas adresą, kurį jam suteikė gavėjas, ir jai nereikia aktyvaus siuntėjo ir gavėjo bendradarbiavimo. Tada pirmasis šios bendrinamos paslapties baitas (arba simbolis) pridedamas prie operacijos duomenų, kai jis skelbiamas Monero tinkle.

Kai vienas iš tos operacijos dalyvių nori vėliau sinchronizuoti savo piniginę su Monero blokų grandine, o ne atlikti visą sudėtingą matematiką ir kriptografiją kiekvienam tinkle esančiam TXO, piniginė dabar gali tiesiog patikrinti, ar nėra tą 1 baito lauką kiekvienoje operacijoje ir tik tada atlikite daug laiko reikalaujantį operacijų su ta žyma patikrinimą – tiksliau 1/256 TXO tinkle!

Ši žyma pašaliniams žiūrintiesiems neatskleidžia jokios informacijos apie operaciją, tik prideda 1 baitą (nedidelę sumą) prie operacijų dydžio ir vis dėlto leidžia sumažinti sinchronizavimo laiką 40 % ir daugiau, sumažinant sudėtingų patvirtinimų skaičių. būtina!

## Žymų peržiūra: supaprastintas pavyzdys

Įsivaizduokite, kad kambaryje turite 4 096 dėžes, iš kurių tik 5 dėžės priklauso jums. Dėžutės visiškai nesiskiria nuo išorės, ir vienintelis būdas sužinoti, ar dėžutė jums skirta, yra ją atidaryti ir išspręsti daug laiko reikalaujančią matematikos užduotį, užrašytą viduje, kad įsitikintumėte, jog tai jūsų.

Dabar įsivaizduokite, kad nusprendėte, kad asmuo, siunčiantis jums tuos 5 langelius, sugeneruotų specialų kodą naudodamas jūsų adresą, o tada kiekvieno jums siunčiamo dėžutės išorėje įdėkite tik pirmąjį to sugeneruoto kodo simbolį. Visi kiti daro tą patį su savo dėžutėmis (siekdami užtikrinti, kad visi langeliai būtų neatskiriami), bet dabar galite tiesiog pažvelgti į vieno simbolio kodą dėžutės išorėje ir atidaryti tik tuos langelius, kuriuose yra tas simbolis. X753X] 

Nors kiti langeliai atitiks jūsų kodą, net kai kurie jums nepriklauso, laukelių, kuriuos reikia atidaryti ir išspręsti matematikos uždavinį, skaičius dabar yra tik 16 (1/256 langelių!), o ne visi 4096. 

Dabar atidarote tuos 16 langelių, išspręsite matematikos uždavinius ir pasilikite 5 langelius, kurie iš tikrųjų priklauso jums iš tos grupės!

## Kada peržiūros žymos bus pasiekiamos Monero?

Žymės peržiūros yra viena iš funkcijų, kurias šiuo metu planuojama įtraukti į [būsimą tinklo naujinimą](https://github.com/monero-project/meta/issues/630) ir turėtų būti išleistas kurį laiką šį pavasarį. Bendruomenė [ iškėlė 23.3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (rašymo metu), kad paskatintų kurti ir diegti rodinio žymas, todėl didžioji dalis darbo įtraukiant peržiūros žymas į Monero kodo bazę jau buvo atlikta. užbaigė j-berman, bendradarbiaudamas su recenzentais ir tyrinėtojais.

Kai tinklas pritaiko peržiūros žymas, visoms operacijoms, išsiųstoms po tinklo naujinimo, bus naudingas žymiai pailgėjęs piniginės sinchronizavimo laikas. Jums nereikės nieko ypatingo, kad pradėtumėte naudoti peržiūros žymas, jūsų mėgstamiausia „Monero“ piniginė tiesiog pradės jas naudoti po tinklo atnaujinimo automatiškai!

## Kaip galiu sužinoti daugiau?

Jei tai sukėlė jūsų smalsumą dėl peržiūros žymų, peržiūrėkite toliau pateiktas papildomas nuorodas, kuriose išsamiai aprašoma tema:

  * [Sumažinkite nuskaitymo laiką naudodami 1 baitą už išvestį „peržiūros žyma“ ](https://github.com/monero-project/research-lab/issues/73)
  * [Pridėkite peržiūros žymas prie išvesties, kad sumažintumėte piniginės nuskaitymo laiką](https://github.com/monero-project/monero/pull/8061)

Papildoma literatūra