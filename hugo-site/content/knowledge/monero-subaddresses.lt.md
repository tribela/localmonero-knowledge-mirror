---
title: "Kaip Monero subadresai užkerta kelią tapatybės susiejimui"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero visada rasdavo naujoviškų būdų, kaip išspręsti sudėtingas privatumo problemas. Dažnai šios naujovės veda prie kitų naujovių, o kartais šios sukurtos technologijos netgi gali būti naudojamos anksčiau neapsvarstytais atvejais. Niekur tai nėra labiau pavyzdžiu, kaip Monero antrinių adresų technologijos atveju.

Apsvarstykite hipotetinę privatumo problemą, kai vieno adreso naudojimas keliose platformose iš iš pažiūros nesusijusių žmonių gali susieti ir deanonimizuoti minėtas tautas. Paprasčiau tariant, jei būtumėte asmuo, vardu Billy Joe Bob, ir pardavinėjote obuolius už Bitcoin, galite paskelbti savo Bitcoin adresą viešoje vietoje, kad klientai jums sumokėtų. Tarkime, adresas prasideda raidine ir skaitmenine eilute 7XybV3... Tačiau atmetus akivaizdžią privatumo riziką, kai kas nors galės patikrinti jūsų Bitcoin likutį ir pamatyti, kiek jūs pardavėte, yra antras, nedažnai kalbamas apie privatumo riziką. Tarkime, kad jūs taip pat buvote pogrindinis įsilaužėlis, vardu l33tz0r. Atliekate švilpimo darbus, pasakojate nieko neįtariantiems žmonėms apie vyriausybės korupciją, todėl būtina išlaikyti savo tapatybę paslaptyje. Jūs priimate Bitcoin aukas už savo darbą ir paskelbiate adresą viešame forume. Tai yra tas pats adresas, kuriuo priimate pinigus iš savo „Apple“ klientų. 7XybV3... vienas.

Paprasta, bet pražūtinga deanonimizacijos ataka būtų naudoti interneto paieškos variklį ieškant jūsų Bitcoin adreso. Įdėjus 7XybV3... adresą į variklį, gaunami du skirtingi rezultatai. Obuolių verslas ir l33tz0r. To pakanka susieti dvi tapatybes ir deanonimizuoti l33tz0r, o tai gali turėti baisių pasekmių iš galių.

Svarbu pažymėti, kad ši ataka TAIP PAT įmanoma naudojant Monero. Nors „Monero“ slepia daugumą grandinės duomenų, ši ataka jų nenaudoja. Jis naudoja tik adresą, kurį reikia bendrinti, kad gautų mokėjimą. Viešai anoniminių aukų atveju. Tai yra vienas iš galimų būdų, kaip Monero vartotojai gali nesąmoningai pakenkti savo privatumui, taip pat yra pavyzdys, kaip, nors Monero yra aukščiausio lygio privatumo išsaugojimo srityje, jis nėra neperšaunamas.

Įprastas būdas išspręsti šią problemą buvo turėti kelias pinigines. Kiekvienai tapatybei (arba naudojimo atvejui) paskelbus skirtingus adresus, jų negalima susieti. Tačiau šis privatumas galioja tik tuo atveju, jei vartotojas niekada jų nesumaišo. Atsitiktinai paskelbus neteisingą adresą, susiejimo poveikis būtų toks pat. Be to, kiekvieno adreso pradinė dalis turi būti saugi, todėl su kiekviena nauja pinigine reikia daugiau informacijos apie darbą.

Monero sprendimas buvo subadresai. Galimybė sukurti absoliučiai didžiulį adresų skaičių po pagrindiniu adresu, naudojant jį kaip tam tikrą sėklą. Kiekvienas sugeneruotas antrinis adresas gali priimti Monero, ir visa tai patenka į tą pačią piniginę. Naudojant šį metodą, vienu adresu galima valdyti labai daug tapatybių, tuo pačiu sumažinant infosec darbą iki minimumo. Šie adresai taip pat nėra matematiškai susieti, todėl nebent vartotojas šauktų savo ryšį su pasauliu, pašalinis stebėtojas turės didelių sunkumų juos susiejant.

Tačiau iš antrinių adresų atsirado dar vienas įdomus naudojimo atvejis; kaip visuotinai nekenčiamų mokėjimo ID pakeitimo parinktis.

Mokėjimo ID buvo būdas prekybininkams nustatyti, kuris klientas atsiuntė kurį mokėjimą. Kadangi Monero informacija grandinėje yra užslėpta, operacijos gavėjas negali matyti, kuriuo adresu ji buvo išsiųsta. Tai reiškia, kad jei yra panašios kainos prekių ir keli užsakymai, gali tapti neįmanoma nustatyti, kas ką atsiuntė. Mokėjimo ID yra unikali, atsitiktinė eilutė, kurią sugeneruoja prekybininkas ir suteikia klientui. Klientas tai prideda kaip atskirą lauką siųsdamas operaciją. Ši atsitiktinė eilutė įtraukiama į blokų grandinę kaip operacijos dalis, todėl prekybininkas gali identifikuoti ir rūšiuoti gaunamas operacijas.

Šis metodas buvo klaidingas keliais atžvilgiais. Pirma, tai sumažina grandinės duomenų vienodumą. Dėl papildomų, unikalių metaduomenų kai kurios operacijos gali išsiskirti iš daugybės, todėl galima atlikti euristinę analizę. Tai ypač aktualu, kai šie metaduomenys nėra taikomi kaip privalomi visiems. Vis dėlto, jei tai būtų privaloma visiems, „blockchain“ būtų pridėta nereikalingos vietos, ir to nebuvo siekiama. Be to, jei mokėjimo ID kada nors buvo pakartotinai naudojamas dėl kokios nors priežasties, būtų nereikšminga susieti dvi operacijas kaip sujungtas. Paprastai tai atsitiko su keitimo indėliais, ir bet kas galėjo lengvai susieti operacijas kaip indėlius biržoje ir iš vieno konkretaus asmens.

Antra, iš UX perspektyvos mokėjimo ID sukuria antrą žingsnį, prie kurio kriptovaliutų vartotojai, atvykstantys iš kitų monetų, nėra pripratę, o jei jie pamirštami, tai sukelia didžiulį galvos skausmą prekybininkui, kuris turi identifikuoti šias operacijas kitomis priemonėmis. . Paprastai tai buvo daroma tiesiogiai pasikalbant su kiekvienu klientu, pamiršusiu įvesti mokėjimo ID, ir patvirtinant kitą identifikuojančią informaciją, kurią galėjo žinoti tik jie, pvz., sumos, išsiuntimo datos ir operacijos ID derinį.

Daugelis šio papildomo veiksmo praleido, todėl kai kurios biržos pradėjo apmokestinti pinigus iš klientų, jei jų pinigus reikėjo nuskaityti rankiniu būdu, nes pamiršta mokėjimo ID. Kiti griežia dantis ir valgė papildomas paramos išlaidas, bet niekas tuo nebuvo patenkintas.

Buvo vienas sprendimas, integruoti adresai, kurie sujungė adresą ir mokėjimo ID į vieną eilutę, todėl negalėjo būti pamiršta, tačiau pritaikymas buvo gana silpnas, nepaisant naudos, kurią prekybininkai būtų gavę jį įtraukę. 

Įdomiu įvykių posūkiu, kad išgelbėtų dieną, atsirado antriniai adresai. Galimybė generuoti didelius antrinių adresų kiekius vienam pagrindiniam adresui ir identifikuoti, kokiais subadresais buvo atliekamos operacijos, leido prekybininkams elegantiškai atsikratyti mokėjimo ID, o taikant naujos kartos Monero technologiją. Nuo to laiko dauguma biržų ir prekybininkų įrankių perėjo prie antrinių adresų kaip pagrindinio operacijos identifikavimo būdo.

Tai, kas prasidėjo kaip privatumo problemos sprendimas, virto daug daugiau, o tai išsprendė didelę prekybininkų ir klientų UX problemą. Naujovės gimdo daugiau naujovių, kurios dažnai gali tapti netikėtomis laimėjimais visiems. „Monero“ tai ne kartą matė ir deda daug pastangų siekdamas naujovių, kas įmanoma „blockchain“. Kas žino, kokius dar dalykus galime atrakinti kartu?

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