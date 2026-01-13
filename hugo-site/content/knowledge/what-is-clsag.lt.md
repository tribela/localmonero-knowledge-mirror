---
title: "Kaip CLSAG pagerins Monero efektyvumą"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Kaip protokolas, Monero šiuo metu yra nuolatinėje naujovių būsenoje. Naudodama mokslinius tyrimus tiek grandinėje, tiek ne grandininiuose sprendimuose, „Monero“ bendruomenė ieško sričių, kurias reikia tobulinti, kad „Monero“ būtų privatesnis, labiau keičiamas ir prieinamesnis visiems. Viena iš naujesnių naujovių yra susieto žiedinio parašo schemos MLSAG pakeitimas įleidžiama pakaitalu CLSAG, kuri reiškia Concise Linkable Spontaneous Anonymous Group.

Paviršiaus lygmeniu CLSAG įdiegimas sumažins dažniausiai pasitaikančias 2 įvesties, 2 išvesties operacijas 25%. Taip pat 10 % sutrumpės patvirtinimo laikas.

Bet kas tiksliai yra CLSAG? Ką jis veikia ir kuo jis skiriasi nuo senosios versijos MLSAG? Skirkime minutę, kad primintume sau, kodėl ir kaip parašyti žiedą, kad galėtume geriau suprasti šią sąvoką. Skambučio parašai leidžia įvesti neinteraktyvius, neatskiriamus duomenis, naudojant pasirašančiojo pasirinktus ankstesnių išėjimų anonimiškumo rinkinius. Žodžiu, tai leidžia vartotojui paslėpti sandoryje naudojamus rezultatus kartu su nesusijusiais išėjimais, ir jie gali visa tai padaryti nereikalaujant, kad kas nors kitas dalyvautų. Viskas, ko jums reikia, yra „blockchain“ kopija. Atrodo, kad kiekviena iš šių išėjimų yra vienodai tikėtina, kad bus siunčiama, todėl slepiami metaduomenys apie siuntėją.

Tačiau dėl to kyla problemų. O kas, jei vartotojas sukurtų žiedinį parašą su visais apgaulės išėjimais? Iš kur kas nors gali žinoti, kad nežinomas siuntėjas neturi teisės siųsti nė vieno iš jų? Ar šis vartotojas galėtų išleisti netikrus pinigus? Atsakymas yra ne. Žiedinis parašas apima metodą, įrodantį, kad bent vienas iš išvesčių priklauso nežinomam siuntėjui, neatskleidžiant, kuris iš jų yra. Tiesą sakant, tiek CLSAG, tiek MLSAG (nuo šiol žinomi kaip SAG) yra žiedinio parašo dalis, kuri tai įrodo. Įdomu tai, kad tuo pačiu metu tai įrodo, kad sandorio suma, nors ir paslėpta už konfidencialių sandorių (RingCT), balansuoja. Tai, kad SAG įrodo du dalykus, kad viena produkcija priklauso kažkam, dalyvaujančiam ringe, ir kad sandoris yra balansas, yra svarbu ir iš tikrųjų yra sutaupyta suma ir patikrinimas. Jei tai darosi painu, nesijaudinkite, netrukus pateiksime smagią ir lengvai suprantamą analogiją.

Senoji parašo schema MLSAG (daugiasluoksnė susiejama spontaniška anoniminė grupė) įrodo pirmiau minėtus du dalykus žiediniame paraše, tačiau daro kiekvieną atskirai. Atskirų skaičiavimų naudojimas pasirašymo ir įsipareigojimo raktams reiškia lėtesnes operacijas. Šiuolaikinis kompiuteris gali atlikti šiuos skaičiavimus per kelias milisekundes, o tai neatrodo daug, ir iš tikrųjų tai nėra viena operacija. Bet kai atsižvelgsime į didžiulį Monero blokų grandinės operacijų skaičių ir tai, kad nuo nulio sinchronizuojantis mazgas turės atsisiųsti ir patikrinti kiekvieną iš jų, baitai ir milisekundės greitai pradeda kauptis.

CLSAG sujungia matematiką, reikalingą abiem įrodyti į vieną, taip pat apskaičiuoja jas abi iš karto, ir tai daro saugiai. Ką tai reiškia saugiu būdu? Na, kad tai išsiaiškintume ir, tikiuosi, viskas būtų prasmingesnė, panagrinėkime tą žadėtą smagią analogiją.

Tarkime, kad reikia eiti ir į bakalėjos, ir į techninės įrangos parduotuvę, kad paimtumėte du skirtingus dalykus: maistą ir toksiškas valymo chemines medžiagas. Nenorite, kad jie susimaišytų, tarsi įvykus nelaimingam atsitikimui, cheminės medžiagos išsilies ant maisto, todėl jie bus nevalgomi. Nusprendžiate būti itin saugūs ir nuvažiuoti iš savo namų į bakalėjos parduotuvę, nusipirkti maisto ir grįžti į namus. Tik išsikrovę maistą grįžtate į automobilį, važiuojate į statybinių prekių parduotuvę ir su chemikalais grįžtate į namus. Išvykote dvi atskiras keliones, kad užtikrintumėte visų pirkinių saugumą. Nors tai tikrai saugu, tačiau neefektyvu. Tai reiškia MLSAG, kur saugomi du skirtingi matematikos rinkiniai ir atliekamos dvi skirtingos „kelionės“ joms apskaičiuoti.

Tačiau nusprendžiate, kad norite tai padaryti greičiau. Tai per daug sugaišto laiko. Žinoma, jei tai padarysite vieną ar du kartus, gyvybės nepavogsite, tačiau tai kartodami vėl ir vėl, valandų skaičius pradeda didėti. Pradedate svarstyti, ar galite leistis į vieną kelionę. Iš namų, į bakalėjos parduotuvę, į techninės įrangos parduotuvę ir atgal namo. Negalite tiesiog eiti ir atsitiktinai viską mesti į savo automobilį. Tai nesaugu. Vietoj to, savo automobilyje paskiriate skirtingas vietas skirtingiems dalykams ir įsitikinkite, kad viskas tvarkingai telpa į savo vietas. Tai darydami galite saugiai vieną kartą apsilankyti abiejose parduotuvėse ir laikyti daiktus atokiau vienas nuo kito. Tai reiškia CLSAG. Dabar šiame sandoryje saugomas tik vienas matematikos rinkinys, įrodantis šiuos du dalykus, ir tai daroma taip, kad jie netrukdytų vienas kitam. Kelionė vis tiek turi būti atlikta, bet jūs labai sumažinote jų skaičių.

Visa tai skamba gana įdomiai. Ar įmanoma rasti kitų nuorodų ar kitų būdų sutaupyti laiko ir vietos? Atsakymas yra taip ir ne. Pasak dabartinių DLK tyrėjų, greičiausiai neįmanoma toliau modifikuoti SAG tipo konstrukcijų, kad būtų geresnis dydis ar greitis; Tačiau kitos konstrukcijos, pvz., Arcturus, Omniring, RCT3 ar Triptych, suteikia daug geresnių dydžio mastelio ir tikrinimo pranašumų, naudojant skirtingus matematinius metodus. Tačiau kiekvienas iš šių „nex-gen“ metodų, susijusių su pasirašiusiųjų dviprasmiškais protokolais, turi savo kompromisų įgyvendinimo detalėse ir yra aktyviai tiriamas ir tiriamas.

Juk Monero visada kuria naujoves.

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

  * [Kaip Monero išsprendė bloko dydžio problemą, kuri kamuoja Bitcoin](/knowledge/dynamic-block-size/)

  * [Kodėl Monero turi uodegą](/knowledge/monero-tail-emission/)

  * [Trumpa Monero istorija](/knowledge/monero-history/)

  * [Žurnalas „Wired“ klysta dėl Monero, štai kodėl](/knowledge/wired-article-debunked/)

  * [15 populiariausių Monero mitų ir rūpesčių, kurie buvo paneigti](/knowledge/monero-myths-debunked/)

  * [Kaip Dandelion++ išlaiko Monero sandorio kilmę privačią](/knowledge/monero-dandelion/)

  * [Kodėl Monero yra atvirojo kodo ir decentralizuotas](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero kasyba: kuo „RandomX“ toks ypatingas](/knowledge/monero-mining-randomx/)

  * [Kodėl „Monero“ yra geresnis nei „Dash“, „Zcash“, „Zcoin“ (net su „Lelantus“), „Grin“ ir „Bitcoin“ maišytuvai, tokie kaip „Wasabi“ (Atnaujinta 2020 m. gegužės mėn.)](/knowledge/why-monero-is-better/)