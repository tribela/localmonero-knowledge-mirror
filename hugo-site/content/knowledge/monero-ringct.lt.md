---
title: "Kaip RingCT slepia Monero operacijų sumas"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero privatumas nepriklauso nuo vieno vienintelio mechanizmo, kurį sugedus būtų atskleista visa operacijų visuma, o veikiau nuo trijų skirtingų technologijų, kurios veikia kartu, kad užtikrintų holistinį privatumą ir kompensuotų kitų dalių trūkumus. Šį trijų dalių metodą sudaro [ skambėjimo parašai](/knowledge/ring-signatures), RingCT ir [ slapti adresai ](/knowledge/monero-stealth-addresses). Šios trys technologijos atitinkamai paslepia tikrąją išvestį (siuntėją), kiekį ir gavėją. Šiandien kalbėsime apie RingCT.

RingCT yra neabejotinai pats techniniausias iš trijų ir gali būti sunkiai suprantamas, todėl neaprašysime, kaip jis tiksliai veikia, o parodysime, kaip galima nežinoti sumos ir vis tiek patvirtinti dalykus. . Ir nesijaudinkite, kaip visada naudosime daugybę pavyzdžių.

Pirmiausia išsiaiškinkime, kodėl svarbu ką nors patikrinti apie sumas. Kodėl negalime jų laikyti visiškai paslaptyje? Atsakymas yra tas, kad yra protingų būdų, kaip žmonės gali susikurti pinigų iš oro, jei jiems suteikiama galimybė. Kaip kažkas panašaus gali veikti? Pažiūrėkime į pavyzdį.

Jei norite nusipirkti prekę iš savo draugo, o jis nori už tai dešimt dolerių, tada jūs pradedate nuo dešimties dolerių, o jis pradeda nuo nulio. Kai duodate jam dešimt dolerių, jis turi dešimt dolerių, o jūs – nulį. Jūs pradėjote nuo dešimties, o dabar jis turi dešimt. Per šią operaciją pinigai nebuvo sukurti ar sunaikinti.

Naudodamas kriptovaliutas, sumanus asmuo už prekę gali duoti dešimt dolerių ir užuot gavęs nulį keitimo dolerių, gali atgauti du dolerius. Vietoj 0 ir 10, vedančių į 10 ir 0 (arba 10 = 10), dabar 0 ir 10 veda į 10 ir 2 (arba 10 = 12). Du Monero buvo ką tik sukurti iš oro. Galite įsivaizduoti, kad jei asmuo tai padarytų sau kelis kartus, jis greitai galėtų sukaupti milžinišką turtą.

Naudojant Bitcoin ir kitus, tai būtų lengva pamatyti. Jūs žiūrite į įvestis, patenkančias į sandorius, ir išeinančias išvestis, ir įsitikinkite, kad tai, kas siunčiama, yra lygi tam, kas gaunama. Jei šios sumos buvo užšifruotos ir nematomos, vartotojas negali patikrinti, ar tai, kas siunčiama ir kas gaunama, yra vienodi.

Siekdamas padidinti Bitcoin privatumą, Gregory Maxwell sukūrė Confidential Transactions (CT) – naują technologiją, kuri leistų užšifruoti sumas, kartu įrodant, kad nieko nebuvo sukurta ar sunaikinta. Kaip ir dauguma privatumo technologijų, ji nepateko į „Bitcoin“, tačiau Monero norėjo ją pritaikyti. Buvo tik viena problema. Jau įdiegta žiedinių parašų technologija buvo nesuderinama su pasiūlyta idėja. Taigi, vienas iš DLK tyrėjų tuo metu, Shen Noether, modifikavo CT į RingCT, CT versiją, suderinamą su žiedo parašais.

Dar kartą pakartosiu, kaip tai veikia gana techniškai ir būtų sunku paaiškinti įvadiniame straipsnyje. Kriptografijos entuziastams, kuris tiesiog privalo žinoti, internete yra daug išsamių straipsnių apie kompiuterinės tomografijos veikimą. Mums, likusiems, šis straipsnis parodys, kaip galima paslėpti sumas, bet vis tiek įrodyti, kad niekas nebuvo sukurta ar sunaikinta.

Tarkime, Alisa norėjo nusiųsti Bobui pinigų. Alisa nusiųs 10 XMR Bobui, kuris gaus 10 XMR. 10=10, taigi nieko čia blogo. Tačiau Alisa nenori, kad kas nors žinotų, kiek ji siunčia. Taigi ji ir Bobas sukuria bendrą paslaptį. Iš esmės skaičius, kurį žino tik jiedu. Tarkime, kad šis skaičius yra 22. Dabar Alisa 10 (ką ji iš tikrųjų siunčia) padaugina iš 22, kad gautų 220. Tai yra skaičius, kurį ji bendrina su tinklu.

Patys kalnakasiai nežino slapto numerio. Jei tai padarytų, rodomą skaičių jie galėtų padalinti iš slapto skaičiaus ir gauti tikrąją išsiųstą sumą. Bet kadangi jie to nedaro, jie negali. Tačiau jie mato, kad Bobas gaus 220. 220 išsiųsta. gauta 220. 220 = 220. Tokiu būdu tinklas gali patikrinti, ar nebuvo sukurtas ar sunaikintas Monero, nežinant tikrosios sumos, kurią Alisa atsiuntė Bobui.

Kadangi Bobas žino bendrinamą slaptą numerį, gavęs pinigus jis tiesiog padalija iš 22, kad gautų tikrąją Alisa išsiųstą sumą – 10. Alisa ir Bobas žino, kiek buvo išsiųsta ir kiek gauta. visiems kitiems suteikiamas klaidingas numeris.

Dar kartą pakartosiu, kad tai nėra tikrasis KT veikimo būdas, tačiau jis suteikia idėją, kaip kažkas panašaus gali būti įmanoma. Tikrasis būdas apima tokius dalykus kaip Pedersen įsipareigojimai, dvi išsiųstos sumos (viena užšifruota suma gavėjui ir kita įsipareigojimo suma tinklui) ir... taip, jau lengva suprasti, kaip galima pasiklysti visame tame.

Tačiau reikia atkreipti dėmesį į tai, kad nors RingCT slepia sumą, perduotą tarp dviejų sandorio šalių, ji neslepia dviejų kitų skaičių rinkinių.

Pirmasis yra monetų bazės operacijos. Jei šis terminas jums nepažįstamas, tai iš esmės reiškia atlygį, kurį kalnakasiai gauna už kito bloko radimą. Šis numeris nėra paslėptas. Kiekvienas gali pamatyti, kiek protokolas atlygino kalnakasiui už jų paslaugą. Tokiu būdu dabartinę Monero sumą galima sužinoti sudėjus visas monetų bazės operacijas. Jų suma bus lygi dabartinei apyvartoje esančiai Monero.

Antras nepaslėptas skaičius yra mokestis, mokamas kalnakasiams, kai vartotojas siunčia operaciją. Mokesčiai turi būti aiškūs, kad kalnakasiai žinotų, kam teikti pirmenybę. Tačiau tai yra būdas, kuriuo vartotojai gali pakenkti savo privatumui, nes jei kas nors naudoja unikalų kasybos mokestį kiekvieną kartą, kai siunčia operaciją (pvz., 0,12345), tada jų operacijos gali būti susietos.

Išskyrus šiuos atvejus, RingCT slepia Monero sumas nuo 2017 m., todėl mūsų kolektyvinis privatumas yra dar stipresnis.

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