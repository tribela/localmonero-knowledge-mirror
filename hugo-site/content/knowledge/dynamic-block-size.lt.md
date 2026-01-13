---
title: "Kaip Monero išsprendė bloko dydžio problemą, kuri kamuoja Bitcoin"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Pastaba:** Labai rekomenduojama, kad skaitytojas perskaitytų mūsų straipsnius [ „Kodėl Monero turi uodegą“](/knowledge/monero-tail-emission) ir [ „Monero Mining: What Makes RandomX“ toks ypatingas“](/knowledge/monero-mining-randomx). Šis straipsnis paremtas jame pateiktomis sąvokomis._

Kai asmenys aptaria „blockchain“ problemas, vienas iš pirmųjų iššokančių žodžių bus „mastelis“. Ne paslaptis, kad „blockchains“ netinkamai keičiasi, tačiau dauguma žmonių nežino kodėl.

Tiesa ta, kad mastelio keitimas iš tikrųjų yra bendras terminas, apimantis dvi skirtingas kategorijas: protokolo palaikymą ir technologinį palaikymą tam tikru momentu. Šiame straipsnyje mes sutelksime dėmesį į vieną, protokolo palaikymas iš esmės yra matas, kiek operacijų protokolas gali apdoroti tam tikru metu.

Bitcoin turi bloko dydžio limitą, o tai reiškia, kad kai į bloką įtraukiama pakankamai operacijų, bet kokios papildomos operacijos turės laukti kito bloko eilėje. Naudinga analogija būtų galvojimas apie traukinį. Traukinys atvažiuoja į stotį, o eilėje esantys registruojasi. Kai traukinys bus pilnas, visi, likę lauke, turės laukti kito.

Bitcoin naudoja mokesčius, kad nustatytų, kas patenka į bloką, ar ne. Grįžtant prie traukinio analogijos, galima įsivaizduoti, kad vienas potencialus keleivis, kurį netrukus paliks, siūlo traukinio inžinieriui penkis dolerius, kad užleistų jam vietą. Kiti keleiviai seka jų pavyzdžiu, ir galiausiai vyksta varžytuvių karas, kad sužinotų, kas gauna kokias vietas. Vairuotojas turi nuspręsti, ar jis nori laikytis „pirmas atėjai, pirmas“ politikos, tačiau jo finansinis interesas yra maksimaliai padidinti savo pajamas, priimant didžiausią kainą pasiūliusius asmenis.

Pagal šią analogiją kalnakasiai yra traukinio mašinistai. Jie gali įtraukti į bloką bet kokias norimas operacijas, tačiau paprastai pasirenka tas, kurių mokesčiai yra didžiausi.

Arba, jei blokai nėra labai pilni, žmonės neturi paskatų mokėti didelių mokesčių, nes yra daug laisvų vietų. 

2017 m. kriptovaliutų bumo įkarštyje Bitcoin buvo užtvindytas sandorių, o mokesčiai išaugo tiems, kurie norėjo būti įtraukti į kitą bloką arba bet kurį artimiausią bloką. Tie, kurie nenorėjo mokėti didelių mokesčių, matė, kad jų operacijos buvo nustumtos valandomis, dienomis arba net iš viso iškrito iš eilės.

Tai buvo šiurpi įžvalga, kaip Bitcoin seksis, jei įvyktų dažnai kalbama apie „masinį įvaikinimą“. Jei bitkoiną naudotų masės, viskas būtų dar blogiau nei 2017 m., o Bitcoin būtų nepasiekiamas niekam, išskyrus turtinguosius, vien dėl to, kad pralaidumas yra mažas dėl fiksuoto bloko dydžio, todėl mokesčių rinka perimtų viršų. 

Monero tai numatė ir norėjo padaryti ką nors kitaip. Taigi Monero kūrėjai įdiegė dinaminį bloko dydį.

Iš esmės „Monero“ taip pat turi bloko dydžio dangtelį, tačiau tai minkšta. Kai laukiančių operacijų eilė tampa per ilga, kalnakasiai gali padidinti blokų dydį. Pagal mūsų traukinio analogiją galite įsivaizduoti, kad pridėsite daugiau traukinių vagonų, kad tilptų papildomi keleiviai. Ištuštėjus eilei, toliau blokai susitraukia iki pradinio dydžio.

Jei tai atrodo tvarkinga idėja, atrodo pagrįsta paklausti, kodėl Monero yra vienintelė kriptovaliuta, kuri tai įgyvendino. Kodėl nepridėjus jo prie „Bitcoin“, kad būtų sustabdytos pralaidumo problemos?

Deja, tai neįmanoma. Yra kelios priežastys, ir mes padarysime viską, kad paaiškintume.

Kasytojui visada naudinga turėti didelius blokus. Su dideliais blokais jie gali tilpti į daugiau operacijų ir uždirbti daugiau pinigų iš mokesčių bei blokų atlygio. Tai gali sukelti nepageidaujamo pašto atakas, kai kas nors siunčia daug mažų operacijų su nedideliais mokesčiais, kad išpūstų grandinę. Miner's tiesiog padidins bloko dydį, įtraukdamas juos visus, nes pinigai yra pinigai, nesvarbu, kokie maži. Tai leistų sukurti nuolat didelius blokus, o ne ekonominę naudą. Bitcoin tai išsprendžia dirbtinai apribodamas bloko dydį ir taip sukurdamas mokesčių rinką. Šlamšto užpuolikai turėtų sumokėti kitiems vartotojams mokesčius, ir tai nebėra pigu. Tačiau tai reiškia, kad blokai užpildomi, kai kurios operacijos lieka laukti, kaip minėta anksčiau.

Taigi kaip „Monero“ gali turėti dinaminius blokų dydžius, tačiau išvengti nepageidaujamo pašto atakų? Atsakymas paprastas, bet protingas. Bauda už bloko atlygį įvedama, kai blokas yra didesnis nei įprasta. Jei kalnakasys nori padidinti bloko dydį, atlygis, kurį jis gaus suradęs tą bloką, bus mažesnis, nei gautų kitu atveju. Taigi jie padidins bloko dydį tik tada, kai vartotojų sumokėti operacijų mokesčiai viršys prarastą bloko atlygio dalį. Pavyzdžiui, jei kalnakasys, padidinęs bloko dydį, prarastų 0,5 XMR, o sumokėtų operacijų mokesčių suma būtų 0,4 XMR, tada, padidinus bloko dydį, grynasis nuostolis būtų 0,1 XMR, taigi nedaryk to. Ir atvirkščiai, jei visi operacijos mokesčiai padidėtų 0,7 XMR, grynasis pelnas būtų 0,2 XMR, net jei jie praras 0,5 XMR iš bloko atlygio baudos, todėl kalnakasys padidins dydį.

Šie dinamiški blokai leidžia tinklui augti natūraliai, dirbtinai neribojant bloko dydžio, kad būtų sudaryta priverstinių mokesčių rinka, kartu išvengiant šiukšlių atakų. Yra dar keletas kampų, iš kurių galime pažvelgti į šią idėją, ir daugiau priežasčių, kodėl nebūtų įmanoma pridėti prie Bitcoin, tačiau kol kas tikimės, kad skaitytojas supras, kaip Monero apeina kelias Bitcoin problemas ir jos išvestinės priemonės ir kaip ji planuoja padidinti savo pralaidumą ateityje.

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

  * [Kaip atominiai apsikeitimai veiks Monero](/knowledge/monero-atomic-swaps/)

  * [Ką kiekvienas „Monero“ vartotojas turi žinoti, kai kalbama apie tinklų kūrimą](/knowledge/monero-networking/)

  * [Kaip RingCT slepia Monero operacijų sumas](/knowledge/monero-ringct/)

  * [Kaip Monero Stealth Addresses apsaugo jūsų tapatybę](/knowledge/monero-stealth-addresses/)

  * [Kaip Monero subadresai užkerta kelią tapatybės susiejimui](/knowledge/monero-subaddresses/)

  * [Paaiškinti Monero išėjimai](/knowledge/monero-outputs/)

  * [„Monero“ geriausia praktika pradedantiesiems](/knowledge/monero-best-practices/)

  * [Kaip žiedo parašai užgožia Monero išvestis](/knowledge/ring-signatures/)

  * [Kaip CLSAG pagerins Monero efektyvumą](/knowledge/what-is-clsag/)

  * [Kodėl Monero turi uodegą](/knowledge/monero-tail-emission/)

  * [Trumpa Monero istorija](/knowledge/monero-history/)

  * [Žurnalas „Wired“ klysta dėl Monero, štai kodėl](/knowledge/wired-article-debunked/)

  * [15 populiariausių Monero mitų ir rūpesčių, kurie buvo paneigti](/knowledge/monero-myths-debunked/)

  * [Kaip Dandelion++ išlaiko Monero sandorio kilmę privačią](/knowledge/monero-dandelion/)

  * [Kodėl Monero yra atvirojo kodo ir decentralizuotas](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero kasyba: kuo „RandomX“ toks ypatingas](/knowledge/monero-mining-randomx/)

  * [Kodėl „Monero“ yra geresnis nei „Dash“, „Zcash“, „Zcoin“ (net su „Lelantus“), „Grin“ ir „Bitcoin“ maišytuvai, tokie kaip „Wasabi“ (Atnaujinta 2020 m. gegužės mėn.)](/knowledge/why-monero-is-better/)