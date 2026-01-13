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