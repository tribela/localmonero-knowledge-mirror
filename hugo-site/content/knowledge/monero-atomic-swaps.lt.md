---
title: "Kaip atominiai apsikeitimai veiks Monero"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Siekiant decentralizacijos ir tikrai neleistinos sistemos, mažai dalykų kriptovaliutų erdvėje taip trokštama kaip decentralizuotos biržos ir atominiai apsikeitimo sandoriai. Nuo pat įkūrimo Monero sunkiai įgyvendino atominius apsikeitimo sandorius, nes privatumo funkcijos sukuria unikalių problemų kuriant protokolą.

Tačiau pirmiausia sukurkime atsarginę kopiją. Kas yra atominiai mainai? Atominis apsikeitimas yra protokolas, pagal kurį dvi skirtingos kriptovaliutos skirtingose blokų grandinėse gali būti keičiamos nepatikimais be tarpininkų. Tai reiškia, kad jei kas nors norėtų iškeisti kriptovaliutą A į kriptovaliutą B, jis galėtų tai padaryti be centralizuoto ar decentralizuoto keitimo. Kaip galima įsivaizduoti, tam reikia daug tyrimų, o visos techninės detalės, leidžiančios tai padaryti, tampa gana sudėtingos. Dar kartą „LocalMonero“ yra čia, kad padėtų ir paprastam žmogui paaiškintų.

Norėdami pradėti, panagrinėkime paprasčiausią atominio apsikeitimo formą, kurią įgyvendina Bitcoin. Jei kas nors nori iškeisti Bitcoin į kitą monetą, kuri naudoja tą pačią maišos laiko užrakto sutarties technologiją, jie gali tai padaryti tokiu būdu. Alisa turi Bitcoin (BTC), bet nori Litecoin (LTC), o Bobas turi LTC, bet nori BTC. Jie nusprendžia atlikti atominį apsikeitimą, kad kiekvienas gautų norimą monetą. Alisa siunčia savo BTC specialiu adresu, naudodama scenarijus, kurie užrakina lėšas, kad net ji negalėtų jo pasiekti. Galite galvoti apie tai taip, kaip Alisa įdeda savo BTC į užrakinimo dėžutę. Kai užraktas yra pagamintas, ji gauna raktą ir nusiunčia šio rakto maišą Bobui. Dabar Bobas neturi paties rakto, tik maišą, todėl jis dar negali pasiekti lėšų.

Bob naudoja šią maišą kaip sėklą, iš kurios sukuria savo užrakinimo dėžutę, ir siunčia ten savo LTC, kur jis taip pat užrakinamas. Kadangi Alisos rakto maiša buvo naudojama kaip sėkla, iš kurios buvo pagaminta Bobo užrakto dėžė, ji gali naudoti savo raktą, kad gautų LTC Bobo užrakto dėžėje. Jos raktas tinka! Tačiau naudodama matematikos „voodoo“ magiją, kai ji naudoja savo raktą, kad atidarytų LTC užraktą, ji atskleidžia raktą Bobui, kuris gali jį panaudoti, kad paimtų BTC, kurį įdėjo į savo užrakto dėžutę. Tokiu būdu, be tarpininko, Alisa ir Bobas sėkmingai apsikeitė savo turtu.

Tačiau yra nedidelė problema. O kas, jei Alisa nusiųs į savo užraktą, o Bobas nuspręs, kad nebenori prekiauti. Kadangi Alisa negali pasiekti savo BTC, kurį ji užrakino, o Bobas nebaigs savo sandorio dalies, Alisa tiesiog praranda savo pinigus amžiams. Laimei, Bitcoin turi mažą technologiją, vadinamą pinigų grąžinimo operacijomis, taigi po tam tikro laiko, jei Bobas nepareikalaus BTC, scenarijuose yra įmontuotas saugiklis, kuriame BTC automatiškai grįš Alisai. Tai buvo pagrindinis Monero atominių apsikeitimo sandorių įgyvendinimo greitis. Dėl Monero [ žiedinių parašų privatumo technologijos](/knowledge/ring-signatures) operacijos siuntėjas visada yra neaiškus. Kaip protokolas gali atlikti pinigų grąžinimo operaciją, jei net nežino, iš kur buvo atlikta operacija?

2017 m. nedidelė tyrėjų grupė apibūdino kitokį metodą, pagal kurį būtų galima atlikti atomų apsikeitimą Monero mieste. Po kelerių metų tobulinimo mokslininkai užbaigė procesą, kurio metu Monero galėtų atlikti atominius apsikeitimo sandorius su Bitcoin, net ir be pinigų grąžinimo operacijų.

Kaip ir daugelis tokio techninio sudėtingumo dalykų, mūsų paaiškinimas per daug supaprastins kai kuriuos dalykus, kad perteiktų idėją, bet vis tiek suteiks tvirtą supratimą apie mechanizmus, kuriais šis procesas veiks.

Tiek Alisa (kuri turi XMR ir nori BTC), tiek Bobas (turi BTC ir nori XMR) turi atsisiųsti ir paleisti programą, kuri palaiko atominį apsikeitimą. Tai gali būti įdiegta į pinigines, decentralizuotus mainus arba specialias, specifines programas, tačiau programinėje įrangoje turi būti paleistas atominio apsikeitimo protokolas. Pirmame žingsnyje Alisos ir Bobo klientai susijungia vienas su kitu ir sukuria keletą bendrų paslapčių bei raktų. Šiame žingsnyje sukuriamas naujas Monero adresas, kuriame Alisa turi vieną rakto pusę, o Bobas – kitą. Vis dėlto ten dar nėra Monero, todėl nėra ko išleisti. Paskutinis dalykas, kurį reikia atkreipti dėmesį į šį adresą, yra tai, kad jie abu turi šios piniginės peržiūros raktą, todėl jie abu gali žvilgtelėti į vidų, kad pamatytų, ar Monero atvyks ir kada jis atvyks.

Antrame žingsnyje Bobas siunčia savo BTC specialiu adresu, panašiu į Bitcoin atominio apsikeitimo protokolą, kurį jau aptarėme. Kai Alisa pamato, kad BTC atkeliauja šiuo adresu blokų grandinėje, ji nusiunčia savo Monero tuo Monero adresu, kurį abu su Bobu turi po pusę rakto. Bobas gali patikrinti, ar Monero atvyko, nes taip pat turi peržiūros raktą, o kai pamato, kad Monero saugiai yra piniginėje, jis nusiunčia Alice rakto gabalėlį, kuris leis jai atsiimti Bitcoin. Panašiai kaip ir kitame protokole, Bitcoin reikalavimo procesas atskleidžia Bobui pusę Monero rakto. Dabar Bobas turi abi puses, todėl jis gali pretenduoti į Monero, o Alisa turi tik jos pusę, todėl ji negali pabandyti paimti jo anksčiau, nei jis tai padarys.

Taigi, jei pažvelgsite į visa tai ir vis dar esate šiek tiek sumišę, kaip Monero sugebėjo išspręsti pinigų grąžinimo operacijų problemą, atsakymas yra gana paprastas. Kadangi pats Monero neturi pinigų grąžinimo operacijų, skaitytojas turėtų pastebėti, kad pirmiausia išsiunčiamas Bitcoin (kuris turi pinigų grąžinimo operacijas), o tik patikrinus, ar jis yra blokų grandinėje, siunčiamas Monero. Tai leidžia Monero panaudoti „Bitcoin“ galimybę rašyti scenarijus atliekant pinigų grąžinimo operacijas ir jomis pasinaudoti, nereikalaujant pačiam turėti šių galimybių.

Atominis apsikeitimas dabar baigtas, bet nuo čia Bobas turi keletą savo naujai pareikšto XMR parinkčių. Jis gali naudoti šią Monero piniginę tokią, kokia yra, arba perkelti XMR į kitą jam jau priklausančią piniginę. Bobas greičiausiai perkels Monero į kitą piniginę, nes Alisa vis dar turi peržiūros raktą ir gali matyti viduje.

Šio protokolo grožis yra tas, kad jis vis dar gana naujas ir yra daug vietos optimizavimui. Ji taip pat gana lanksti savo architektūra, todėl diegimas kitose piniginėse ar decentralizuotose biržose turėtų būti paprastas ir puikiai derėtų prie esamos architektūros.

Papildoma literatūra

  * [Kaip Monero unikaliai įgalina žiedinę ekonomiką](/knowledge/monero-circular-economies/)

  * [Monero žiedo parašai prieš CoinJoin kaip Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Kodėl (ir kaip!) turėtumėte turėti savo raktus](/knowledge/hold-your-keys/)

  * [Prisideda prie Monero](/knowledge/contributing-to-monero/)

  * [Kaip nuotoliniai mazgai veikia Monero privatumą](/knowledge/remote-nodes-privacy/)

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