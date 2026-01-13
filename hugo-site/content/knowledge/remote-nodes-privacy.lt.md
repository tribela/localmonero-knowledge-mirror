---
title: "Kaip nuotoliniai mazgai veikia Monero privatumą"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Vienas didžiausių Monero pranašumų, palyginti su kitomis kriptovaliutomis, yra grandinės privatumas, tačiau ar kada nors susimąstėte, kaip Monero privatumas išlieka, kai naudojate nuotolinį mazgą? O kaip būtų, jei naudotumėte „lengvos piniginės“ serverį, pvz., „MyMonero“?

Šiame įraše apžvelgsime kai kurias detales, kaip Monero užtikrina išskirtinį privatumą grandinėje net naudojant nuotolinį mazgą, taip pat į ką reikia atkreipti dėmesį naudojant nuotolinius mazgus.

## Kokias funkcijas atlieka mazgai Monero?

Tiems, kurie mažiau žino, kaip veikia „Monero“, „Monero“ tinklo mazgus (arba serverius) gali valdyti bet kas ir leisti mazgo savininkui arba kitiems, su kuriais jie pasirenka, bendrinti! – sinchronizuoti blokų grandinės kopiją ir pateikti tą kopiją kitiems tinkle. Šie mazgai taip pat patikrina visas tinkle vykstančias operacijas, taip pat visus paskelbtus blokus ir užtikrina, kad jie visi laikytųsi bendru sutarimu nustatytų taisyklių.

Kita funkcija, kurią mazgai atlieka Monero, yra būdas pateikti visus duomenis, kurių reikia jūsų mėgstamiausiai Monero piniginei, kad būtų galima tinkamai patikrinti jums priklausančias operacijas ir atlikti naujas operacijas. Šiuos duomenis mazgai teikia dviem būdais: 

  * Duomenų iš kiekvieno bloko grandinės bloko paprašo piniginė, jie nuskaito, ar nėra jums priklausančių operacijų, o tada išmeta, kai tik patikrina piniginė. 
    * Šis veiksmas netrukus bus smarkiai patobulintas dėl [peržiūros žymų](/knowledge/view-tags-reduce-monero-sync-time).
  * Siunčiant operacijas, jūsų naudojamas mazgas pateikia galimų jaukų (arba netikrų įvesties) sąrašą, kurį galima naudoti kuriant operaciją, užtikrinant, kad kiekvieną kartą išleisdami „Monero“ turėsite daug pasislėpti. 
    * Šie jaukai yra [ žiedinių parašų ](/knowledge/ring-signatures) dalis, svarbi Monero požiūrio į privatumą grandinėje dalis.

## Koks yra privatus ir saugiausias būdas naudoti Monero?

Geriausias dalykas, kurį reikia padaryti, net ir esant tvirtam grandinės privatumui, kurį teikia Monero naudojant nuotolinius mazgus, yra paleisti savo Monero mazgą, kad įsitikintumėte, jog turite nesugadintą Monero blokų grandinės kopiją ir kad jūsų IP adresas yra gerai apsaugotas. Kitas privalumas, kai naudojate savo mazgą, yra tai, kad galite prisidėti prie tinklo, leisdami kitiems mazgams sinchronizuotis iš jūsų mazgo arba netgi leisdami kitiems vartotojams prisijungti prie jūsų mazgo savo piniginėmis.

Todėl Monero vis tiek užtikrina puikų privatumą naudojant nuotolinį mazgą. Jei norite paleisti savo Monero mazgą, čia yra paprastas vadovas, kaip tai padaryti: 

  * [Paleiskite Monero mazgą](https://sethforprivacy.com/guides/run-a-monero-node/)

## Ką apie mane gali sužinoti nuotolinis mazgas?

Kai naudojate nuotolinį mazgą, yra kelios pagrindinės informacijos, kuri gali būti atskleista nuotoliniam mazgui, ir keli pagrindiniai būdai, kaip mazgas gali jus užpulti, neleisti jums atlikti sandorių ir dar daugiau.

Pirmas dalykas, kurį nuotolinis mazgas gali sužinoti apie jus, yra jūsų viešasis IP adresas. Nors tikimasi, kad tai bus paslėpta naudojant VPN arba Tor, nuotolinis mazgas gali susieti jūsų viešąjį IP adresą su operacija, padėdamas jiems susiaurinti, iš kur vykdote sandorius. Nuotolinis mazgas taip pat gali sužinoti paskutinį sinchronizuoto piniginės bloką ir panaudoti jį, kad galėtų pagrįstai spėti apie jus, pvz., kada įprastai naudojate Monero ir kada paskutinį kartą išleidote Monero. Tai ypač aktualu, jei visada ateinate iš to paties IP adreso (pvz., namų). Paskutinis svarbus dalykas, kurį nuotolinis mazgas gali sužinoti apie jus, yra pagrindinė informacija apie per jį siunčiamas operacijas. Nors tai gali būti akivaizdžiausi duomenys, kuriuos apie jus gauna nuotolinio mazgo operatorius, svarbu suprasti, kad jie gali būti naudojami siekiant padėti atsekti operacijos siuntėją, kai ši informacija derinama su kitais ne grandinės duomenimis. Tai gali būti ypač pavojinga, jei nuotolinį mazgą valdo kenkėjiškas subjektas, blokų grandinės analizės įmonė arba slegianti nacionalinė valstybė.

Nuotolinis mazgas taip pat gali bandyti sukelti problemų, slėpdamas blokus nuo jūsų, todėl jūsų piniginė manys, kad ji buvo sinchronizuota, o ne. Dėl to galite manyti, kad lėšos prarastos, arba negalėsite išleisti lėšų, kol neprisijungsite prie kito mazgo. Paskutinis svarbus dalykas, kurį galėtų padaryti nuotolinis mazgas, yra pateikti jūsų piniginei manipuliuojamą jaukų sąrašą. Dėl to jūsų piniginėje gali arba visiškai nepavykti sudaryti operacijų (todėl negalėsite išleisti lėšų), arba nuotolinis mazgas gali pabandyti pateikti jaukus, kuriuos jis žino, kad jie išleidžiami, kad sumažintų anonimiškumą, kurį gaunate atliekant kiekvieną operaciją.

## Kokios privatumo garantijos vis dar galioja naudojant nuotolinį mazgą?

Nors šis straipsnis jus šiek tiek išgąsdino, svarbu suprasti, kad Monero suteikiamas privatumas yra puikus net naudojant nuotolinį mazgą ir gerokai pranoksta bet kurią kitą kriptovaliutą tokiu būdu. Jūs vis tiek gaunate tvirtą Monero teikiamą privatumą tinkle, nes nuotolinis mazgas niekada nežino tikrosios įvesties (kokias monetas išleidžiate), operacijos metu išleistos Monero sumos ar operacijos gavėjo adreso. Išoriniai stebėtojai taip pat negali matyti tikrosios įvesties, sumos ar susijusių adresų (nesvarbu, kokio tipo mazgą pasirinksite naudoti!), užtikrinant, kad net jūsų IP adresas, piniginės sinchronizavimo informacija ir operacijos už nuotolinio mazgo ribų turi tvirtas privatumo garantijas. 

Nuotolinis mazgas taip pat niekada neturi prieigos prie ankstesnių jūsų išsiųstų ar gautų operacijų arba šiuo metu jūsų piniginėje esančios Monero sumos ir praranda bet kokį jūsų operacijų matomumą, kai pradedate naudoti kitą mazgą. Nuotoliniam mazgui niekada neteikiami jokie privatūs raktai (nei išlaidų, nei peržiūros raktai), todėl jūsų piniginė išlieka privati, saugi ir tinkama naudoti. Nesvarbu, koks yra nuotolinis mazgas, jums taip pat niekada negresia pavojus prarasti Monero arba jį pavogti, nes mazgas negali redaguoti gavėjo adreso, niekada neturi prieigos prie jūsų piniginės privačių raktų ir jokiu būdu negali konfiskuoti jūsų Monero.

## Kaip apie „lengvas pinigines“, tokias kaip „MyMonero“?

Nors tema šiek tiek nepatenka į šio straipsnio taikymo sritį, norėjau pakalbėti apie unikalų Monero piniginės tipą – lengvas pinigines. Lengvosios piniginės pavadinimas kilo dėl to, kad jūsų piniginei (telefone ar kompiuteryje) nereikia atlikti jokio blokų grandinės sinchronizavimo, todėl patirtis tampa greitesnė ir sklandesnė.

Tačiau kol kas tokios piniginės turi rimtą privatumo kompromisą – jūsų piniginė siunčia privatų peržiūros raktą į jūsų naudojamą nuotolinį serverį (kaip numatytasis MyMonero), suteikdamas nuotoliniam serveriui visišką bet kokių gautų lėšų matomumą. nuo jūsų piniginės sukūrimo (ir tol, kol nustosite naudoti tą piniginę ar sėklą). Tai labai sumažina privatumą, kurį gaunate iš mazgo operatoriaus, todėl reikia elgtis atsargiai.

Laimei, Monero bendruomenė tobulina programinę įrangą, kurią galite naudoti savo lengvosios piniginės serveriui (LWS) priglobti, o tai leis greitai sinchronizuoti nepasitikint trečiajai šaliai savo privačių peržiūros raktų. paleis programinę įrangą, kurioje jūsų piniginė siunčia privataus peržiūros raktus!

Daugiau apie tinkintą lengvosios piniginės serverį rasite toliau pateiktoje „Github“ saugykloje:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Kaip galiu sužinoti daugiau?

Jei jums įdomu ir norėtumėte geriau suprasti „Monero“ mazgus ir pabandyti naudoti nuotolinį mazgą ar paleisti savo, žr. toliau pateiktas nuorodas, kur rasite puikių vietų pradėti:

  * [Monero World, bendruomenės valdomų nuotolinių mazgų, kurie galima naudoti](https://moneroworld.com/#nodes)
  * [Monero mazgai, valdomi Seth For Privacy, šio straipsnio autorius](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, nuotolinių mazgų, kurių būsena dažnai tikrinama, sąrašas< /a>](https://monero.fail/)
  * [Kaip prisijungti į nuotolinį mazgą GUI piniginėje](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia – nuotolinis Mazgas](https://www.getmonero.org/resources/moneropedia/remote-node.html)

Papildoma literatūra

  * [Kaip Monero unikaliai įgalina žiedinę ekonomiką](/knowledge/monero-circular-economies/)

  * [Monero žiedo parašai prieš CoinJoin kaip Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Kodėl (ir kaip!) turėtumėte turėti savo raktus](/knowledge/hold-your-keys/)

  * [Prisideda prie Monero](/knowledge/contributing-to-monero/)

  * [Kaip „Monero“ naudoja „hard-forks“ tinklui atnaujinti](/knowledge/network-upgrades/)

  * [Peržiūrėkite žymas: kaip vienas baitas sumažins Monero piniginės sinchronizavimo laiką 40%+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool ir jo vaidmuo decentralizuojant Monero kasybą](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: ką tai padarys Monero](/knowledge/seraphis-for-monero/)

  * [Ar Bitcoin konvertavimas į Monero yra toks pat privatus, kaip ir tiesioginis Monero pirkimas?](/knowledge/most-private-way-to-buy-monero/)

  * [Kodėl Monero, skirtingai nei Zcash, naudoja patikimą sąranką](/knowledge/monero-trustless-setup/)

  * [Kodėl „Monero“ yra geresnė vertės parduotuvė nei „Bitcoin“.](/knowledge/monero-better-store-of-value/)

  * [Kaip Monero gali įveikti Bitcoin tinklo efektus](/knowledge/network-effect/)

  * [Kodėl Monero turi kritiškiausią mąstymo bendruomenę](/knowledge/critical-thinking/)

  * [Aferos, į kurias reikia atkreipti dėmesį naudojant Monero](/knowledge/monero-scams/)

  * [Kaip atominiai apsikeitimai veiks Monero](/knowledge/monero-atomic-swaps/)

  * [Ką kiekvienas „Monero“ vartotojas turi žinoti, kai kalbama apie tinklų kūrimą](/knowledge/monero-networking/)

  * [Kaip RingCT slepia Monero operacijų sumas](/knowledge/monero-ringct/)

  * [Kaip Monero Stealth Addresses apsaugo jūsų tapatybę](/knowledge/monero-stealth-addresses/)

  * [Kaip Monero subadresai užkerta kelią tapatybės susiejimui](/knowledge/monero-subaddresses/)

  * [Paaiškinti Monero išėjimai](/knowledge/monero-outputs/)

  * [„Monero“ geriausia praktika pradedantiesiems](/knowledge/monero-best-practices/)

  * [Kaip žiedo parašai užgožia Monero išvestis](/knowledge/ring-signatures/)

  * [Kaip Monero išsprendė bloko dydžio problemą, kuri kamuoja Bitcoin](/knowledge/dynamic-block-size/)

  * [Kaip CLSAG pagerins Monero efektyvumą](/knowledge/what-is-clsag/)

  * [Kodėl Monero turi uodegą](/knowledge/monero-tail-emission/)

  * [Trumpa Monero istorija](/knowledge/monero-history/)

  * [Žurnalas „Wired“ klysta dėl Monero, štai kodėl](/knowledge/wired-article-debunked/)

  * [15 populiariausių Monero mitų ir rūpesčių, kurie buvo paneigti](/knowledge/monero-myths-debunked/)

  * [Kaip Dandelion++ išlaiko Monero sandorio kilmę privačią](/knowledge/monero-dandelion/)

  * [Kodėl Monero yra atvirojo kodo ir decentralizuotas](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero kasyba: kuo „RandomX“ toks ypatingas](/knowledge/monero-mining-randomx/)

  * [Kodėl „Monero“ yra geresnis nei „Dash“, „Zcash“, „Zcoin“ (net su „Lelantus“), „Grin“ ir „Bitcoin“ maišytuvai, tokie kaip „Wasabi“ (Atnaujinta 2020 m. gegužės mėn.)](/knowledge/why-monero-is-better/)