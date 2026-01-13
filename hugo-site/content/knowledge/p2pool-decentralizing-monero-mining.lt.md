---
title: "P2Pool ir jo vaidmuo decentralizuojant Monero kasybą"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Vienas iš pagrindinių Monero projekto tikslų yra sukurti sąžiningą, decentralizuotą ir saugų tinklą taikant naujus ir novatoriškus darbo įrodymo (PoW) kasybos metodus, o tai yra pagrindinis būdas šiandien apsaugoti kriptovaliutų tinklus. X230X] 

Nors unikalus gavybos algoritmas [, pvz., RandomX](/knowledge/monero-mining-randomx), yra nepaprastai svarbus siekiant šio tikslo, nes padeda užtikrinti, kad kiekvienas, turintis kompiuterį, galėtų nemažai prisidėti prie tinklo saugumo, RandomX problemų neišsprendžia. kurios gali atsirasti dėl baseino kasybos. Kasyba baseine šiandien yra labiausiai paplitęs kriptovaliutų, įskaitant Monero, gavybos būdas, tačiau, laimei, p2pool kasybos atsiradimas tai greitai keičia.

Nors unikalus gavybos algoritmas [, pvz., RandomX](/knowledge/monero-mining-randomx), yra nepaprastai svarbus siekiant šio tikslo, nes padeda užtikrinti, kad kiekvienas, turintis kompiuterį, galėtų nemažai prisidėti prie tinklo saugumo, RandomX problemų neišsprendžia. kurios gali atsirasti dėl baseino kasybos. Kasyba baseine šiandien yra labiausiai paplitęs kriptovaliutų, įskaitant Monero, gavybos būdas, tačiau, laimei, p2pool kasybos atsiradimas tai greitai keičia.

## Kas yra baseino kasyba?

## Kas yra baseino kasyba?

Kasybos baseinas – tai būdas kalnakasiams pasidalyti užduotimi bandyti išspręsti bloką tinkle ir po to tolygiai pasidalyti atlygį už visus telkinio rastus blokus. Nors tai labai padeda išlyginti kalnakasių darbo užmokesčio dažnumą, palyginti su vien Monero kasimu, tai neapsieina be rimtų centralizavimo problemų.

Kadangi kiekvienas kalnakasys prisideda prie baseino darbo, jie atsisako bet kokio atliekamo darbo kontrolės ir blokuoja, ką randa pačiam baseinui, tikėdami, kad baseinas sąžiningai ir teisingai paskirstys atlygį visiems kalnakasiams, atsižvelgiant į kiekvieno atliktas darbas. Jei viskas klostosi gerai, baseino operatorius surenka visų kalnakasių darbą, pateikia jį tinklui ir po lygiai dalijasi atlygį.

## Kokia yra baseino kasybos problema?

## Kokia yra baseino kasybos problema?

Deja, tai visiškai priklauso nuo pasitikėjimo ir leidžia baseino operatoriui daryti niekšiškus darbus, atliekamus kalnakasių. Baseino operatorius gali panaudoti atliekamą darbą siekdamas atakuoti tinklą, bandyti dvigubai išleisti lėšas (jei fondas pakankamai didelis) arba tiesiog panaudoti kalnakasių atliekamą darbą, kad susimokėtų sau ir niekada tinkamai neapdovanotų kalnakasių už jų darbą. 

Didžiausia rizika tinklui yra ta, kad telkinys (arba keli telkiniai dirba kartu), kurių valdoma daugiau nei 51 % tinklų maišos, nes jie gali tai panaudoti sukčiavimui ir du kartus išleisti lėšas (dvigubos išlaidos) ataka) arba bandyti pakeisti tinklo taisykles.

## Kas yra p2pool?

## Kas yra p2pool?

p2pool yra koncepcija, kuri iš pradžių buvo sukurta Bitcoin kasybai dar 2011 m., tačiau niekada nebuvo plačiai pritaikyta ir praktiškai nenaudojama Bitcoin. Laimei, vienas iš pagrindinių RandomX kūrėjų, SCHernykh, praleido savo atostogas ieškodamas kai kurių problemų, susijusių su Bitcoin įdiegimu p2pool, ir perrašydamas visą programinę įrangą nuo nulio.

p2pool Monero leidžia kalnakasiams visiškai nepasitikinčiu būdu dirbti kartu sprendžiant blokus ir apsaugoti Monero tinklą naudojant specialią mazgo programinę įrangą, skirtą p2pool, kad būtų galima pasidalyti darbu.

Tai atliekama naudojant naują blokų grandinę („šoninę grandinę“), kuri registruoja kiekvieno kalnakasio atliekamą darbą, piniginės adresą ir uždirbtą „Monero“ sumą, o tada išmoka atlygį patikos fondu. - mažiau ir decentralizuotas būdas. Kadangi šioje šoninėje grandinėje yra daug mažiau kalnakasių, joje daug lengviau rasti ir pateikti blokus nei pagrindiniame Monero tinkle, todėl kalnakasiams lengviau gauti pastovius atlyginimus, palyginti su vien Monero kasyba.

## Kaip p2pool išsprendžia baseino kasybos problemas?

## Kaip p2pool išsprendžia baseino kasybos problemas?

P2pool nėra centralizuoto fondo, centralizuoto fondo operatoriaus ar vieno asmens, turinčio lėšų ir paskirstančio išmokas. Visą darbą, kurį bendrai atlieka tie kasyba per p2pool, tikrina p2pool blockchain ir kiti mazgų operatoriai, kad įsitikintų, jog jis yra teisėtas, ir visiems kalnakasiams išmokama pagal jų atliktą darbą iškart, kai blokas randamas tiesiai iš atlygiai tame rastame bloke.

Kai kalnakasiai pasirenka naudoti p2pool, o ne centralizuotą telkinį, jie atima visą fondo operatorių galią ir pasitikėjimą ir užtikrina, kad jų darbas prisidėtų prie tinklo gerovės ir jų pačių naudos, sumažintų tinklo atakų ir netinkamo naudojimo riziką. savo darbo arba atlygio, kurį jie turi mokėti, vagystės.

Tai ne tik padeda jiems apsaugoti savo interesus, bet ir sumažina riziką, kurią centralizuoti telkiniai gali kelti visam Monero tinklui. „p2pool“ naudojimas taip pat labai padeda sumažinti pavojų, kurį nacionalinės valstybės ar reguliavimo institucijos gali kelti tinklo sveikatai, nes nėra centralizuotų telkinių operatorių, kuriems būtų daromas spaudimas, nėra geografinės telkinių koncentracijos, į kurią būtų galima atsiremti, ar bet kokio kito lengvo spaudimo taško. kad jie galėtų naudoti prieš Monero.

## Kokie yra trūkumai?

## Kokie yra trūkumai?

Laimei, p2pool Monero buvo gerai suprojektuotas ir gerai pastatytas ir veikia labai gerai! Tačiau pagrindinis p2pool kasybos trūkumas yra tas, kad kiekvienas kalnakasys, norintis naudoti p2pool, turi paleisti savo Monero mazgą, todėl darbo pradžios procesas yra šiek tiek labiau įtrauktas. Tačiau šis mazgas naudojamas apskaičiuojant visą informaciją, reikalingą blokams kurti ir tikrinti, ir užtikrina, kad kalnakasys visiškai kontroliuoja savo atliekamą darbą. Mazgas taip pat gali veikti kaip nuotolinis kalnakasių piniginės mazgas, prisidėti prie tinklo ir daug daugiau.

Kitas pagrindinis skirtumas nuo centralizuoto kasybos yra tas, kad maži kalnakasiai, naudojantys p2pool, turės šiek tiek daugiau "variacijos" arba laiko tarp išmokėjimų, nei didelis centralizuotas telkinys, bet ' yra _labai_ svarbu atkreipti dėmesį, kad dėl to laikui bėgant neuždirbsite mažiau Monero! „p2pool“ laikui bėgant bus toks pat pelningas net ir mažiems kalnakasiams, kaip ir centralizuoti baseinai. Dalį šios nuokrypos taip pat kompensuoja „p2pool“ taikant 0% mokesčius, nes nėra centralizuoto telkinio operatoriaus, kuris apmokėtų už savo paslaugas!

## Kaip man pradėti?

## Kaip man pradėti?

Laimei, dėl puikaus Monero' p2pool diegimo dizaino ir daugybės bendruomenės žmonių, kurie skyrė laiko padėti supaprastinti gavybos per p2pool procesą, laikui bėgant pradėti vis lengviau. Yra keletas būdų, kaip pradėti gavybą naudojant p2pool, bet kadangi techninės detalės nepatenka į šio straipsnio taikymo sritį, nedvejodami pereikite prie toliau pateiktos nuorodos, atsižvelgiant į jūsų operacinę sistemą: 

  * [ „Windows“](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## Kaip galiu sužinoti daugiau?

## Kaip galiu sužinoti daugiau?

Jei tai sukėlė jūsų smalsumą apie p2pool kasybą, toliau ieškokite papildomų nuorodų ir paaiškinimų apie p2pool, kaip tai veikia ir ką tai reiškia Monero:

  * [Oficialus Github, skirtas p2pool](https://github.com/SChernykh/p2pool)
  * [Oficialūs dokumentai apie p2pool naudojimą](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool dabar veikia](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, "blokų tyrinėtojas", skirtas p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [ Sergejus Černychas: apie jo P2Pool decentralizuoto XMR kasybos baseino kūrimą](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

Papildoma literatūra

  * [Kaip Monero unikaliai įgalina žiedinę ekonomiką](/knowledge/monero-circular-economies)/

  * [Monero žiedo parašai prieš CoinJoin kaip Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Kodėl (ir kaip!) turėtumėte turėti savo raktus](/knowledge/hold-your-keys)/

  * [Prisideda prie Monero](/knowledge/contributing-to-monero)/

  * [Kaip nuotoliniai mazgai veikia Monero privatumą](/knowledge/remote-nodes-privacy)/

  * [Kaip „Monero“ naudoja „hard-forks“ tinklui atnaujinti](/knowledge/network-upgrades)/

  * [Peržiūrėkite žymas: kaip vienas baitas sumažins Monero piniginės sinchronizavimo laiką 40%+](/knowledge/view-tags-reduce-monero-sync-time)/

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

  * [Monero kasyba: kuo „RandomX“ toks ypatingas](/knowledge/monero-mining-randomx)/

  * [Kodėl „Monero“ yra geresnis nei „Dash“, „Zcash“, „Zcoin“ (net su „Lelantus“), „Grin“ ir „Bitcoin“ maišytuvai, tokie kaip „Wasabi“ (Atnaujinta 2020 m. gegužės mėn.)](/knowledge/why-monero-is-better)/

Papildoma literatūra