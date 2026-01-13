---
title: "Ką kiekvienas „Monero“ vartotojas turi žinoti, kai kalbama apie tinklų kūrimą"
slug: "monero-networking"
date: "2020-11-11"
image: "/images/networking.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Niekam neturėtų būti netikėta, kad „Monero“ ir iš tikrųjų visa kriptovaliuta veikia internete. Ir vis dėlto, nors šis teiginys atrodo pagrindinis ir akivaizdus, daugelis nesvarsto, ką tai reiškia jų privatumui. Kitaip tariant, yra kai kurių dalykų, nuo kurių Monero gali ir negali apsisaugoti, vien dėl veikimo internete pobūdžio. Kai kurie iš šių svarstymų yra tik nepatogumai, o kiti yra daug rimtesni scenarijuje, kai reikalingas visiškas privatumas. Skirkime laiko ir susipažinkime su tuo, kaip „Monero“ vartotojai sąveikauja tarpusavyje tinkle ir ką tai reiškia jų privatumui.

Pradedant nuo trivialios dalykų pusės, jei vartotojas neturi prieigos prie interneto, jis negali atsisiųsti naujų blokų, platinti operacijų kitų vardu arba siųsti savo operacijų. Įdomu tai, kad vartotojas, turintis visą mazgą ir neturintis prieigos prie interneto, gali sukurti operaciją neprisijungęs, kurią bus galima išsiųsti vėliau. Taip yra todėl, kad žiediniam parašui reikia tik išvesties iš blokų grandinės, kad būtų galima pasislėpti. Trumpas priminimas apie [, kaip veikia skambėjimo parašai](/knowledge/ring-signatures). Jis paslepia tikrąją vartotojo siunčiamą išvestį tarp nesusijusių išėjimų, pasirinktų iš praeities, rinkinio. Jei vartotojas turi prieigą prie šių išėjimų visiškai atsisiųstos blokų grandinės (viso mazgo) pavidalu, jis gali sukurti skambėjimo parašą iš ankstesnių išėjimų ir, atnaujinus interneto ryšį, perduoti operaciją į tinklą.

Naudotojas, kuris naudoja nuotolinį mazgą, negali to padaryti, nes kurdamas žiedinį parašą jis susisiekia su nuotoliniu pilnu mazgu, kad išvestys būtų įtrauktos į žiedo parašą. Nėra interneto reiškia, kad jie negali pasiekti šio mazgo, todėl jie neturi operacijų kūrimo neprisijungus galimybių.

Prieš tęsdami kai kuriuos privatumo klausimus, trumpai apžvelgsime, kaip veikia internetas kaip visuma. Visas internetas yra ne kas kita, kaip kompiuteriai, jungiantys prie kitų kompiuterių. Viskas. Tinklaraštis, kurį mėgstate skaityti? Tik kai kurie failai priglobti kieno nors kito kompiuteryje. Ši svetainė, kurioje skaitote šį straipsnį (LocalMonero)? Failai ir kodas kažkur talpinami kompiuteryje. Taip veikia net didelės beprotiškos svetainės. Paimkite, pavyzdžiui, „YouTube“. Tiesiog vaizdo įrašų failai, priglobti milžiniškose „Google“ kompiuterių sistemose, ir jūs prie jų prisijungiate, kad atsisiųstumėte vaizdo įrašą į savo kompiuterį ir galėtumėte jį žiūrėti.

Šie kompiuteriai gali atskirti vienas kitą, nes kiekvienam prie interneto prijungtam kompiuteriui suteikiamas unikalus identifikavimo numeris, vadinamas IP adresu. Paprastai tai yra keturi skaičių rinkiniai, atskirti taškais, pavyzdžiui: 172.66.35.7. Svarbu tai turėti omenyje, kai svarstome, kaip „Monero“ informacija perkeliama internete. Monero yra lygiavertis tinklas (P2P), o tai reiškia, kad kompiuteriai jungiasi tiesiogiai vienas prie kito, o ne naudodamiesi tarpininku. Taigi, kai visas vartotojo mazgas atsisiunčia naujai atrastą bloką, jis atsisiunčia jį ne iš centrinio serverio, o iš savo kolegų. Neigiama yra tai, kad vartotojai jungiasi vienas su kitu tiesiogiai, todėl jie žino vienas kito IP adresus.

Na? Koks tas svarbus reikalas? Tai tik skaičius, tiesa? Ne visai. Pačiuose IP adresuose yra informacijos apie vartotoją, pvz., kilmės šalį ir tinklo teikėją, tačiau, dar blogiau, interneto paslaugų teikėjai (IPT) žino kiekvieno asmens, besinaudojančio jų paslaugomis, IP adresą. Tai reiškia, kad šie interneto paslaugų teikėjai ir tie, su kuriais jie dirba, gali stebėti vartotojo interneto srautą ir, naudodami tam tikrą protingą taktiką, sužinoti, kad jie naudoja Monero. Prieš išsigąsdami, atkreipkite dėmesį į formuluotę. Viskas, ką šie šniukštinėja gali padaryti, tai pamatyti, kad žmogus jungiasi prie kitų Monero tinklo mazgų. Dėl Monero privatumo technologijos nieko daugiau apie asmenį nenutekėjo. Ne tai, ar jie naudoja mazgą, ar (kai) siunčia operacijas, o jei operacija siunčiama, jokia informacija nėra žinoma. IPT gali matyti tik tai, kad vienas iš jų vartotojų jungiasi prie Monero tinklo.

Dabar kai kuriems žmonėms kai kuriose vietose vien šios informacijos gali pakakti, kad būtų pakenkta reputacijai ar laisvei. Arba galbūt jums nepriimtina mintis, kad kas nors dėl kokių nors priežasčių kėsinasi į jūsų privatumą ir tai, ką darote internete. Šie asmenys raginami prisijungti prie Monero tinklo tik naudojant VPN, Tor arba I2P, kurios visos yra paslaugos, kurios slepia vartotojo IP adresą nuo kitų, taip pat slepia tai, ką vartotojas daro nuo savo IPT. Šių paslaugų skirtumai nepatenka į šio straipsnio taikymo sritį, tačiau šia tema parašyta daug aukštos kokybės straipsnių, todėl susirūpinę vartotojai raginami pasidomėti!

Likusiems galime manyti, kad tai, kad kiti žino, kad esame prisijungę prie Monero tinklo, nėra toks didelis dalykas. Galų gale, tikrasis mūsų operacijų turinys arba, jei iš viso siunčiame, yra paslėptas viešai, taigi kokia žala? Nors tai gali būti tiesa, vartotojai raginami atsižvelgti į tai, kad pagrindinis kriptovaliutų pritraukimas yra jų pačių bankas. Kai laikote privatų raktą ir su juo kas nors atsitiks, niekas negali padėti susigrąžinti prarastų lėšų.

Būti savo banku reiškia atsižvelgti ne tik į skaitmeninę, bet ir į fizinę apsaugą. Labai gali būti, kad asmens, prisijungusio prie Monero tinklo, žinios gali pritraukti nepageidaujamo dėmesio, nebūtinai iš didelio masto veikėjų, tokių kaip nacionalinės valstybės, bet iš mažesnių, turinčių savanaudiškų interesų, pavyzdžiui, įsilaužėlių, norinčių lengvai užsidirbti. Visoje kriptovaliutų erdvėje iš tiesų yra daugybė istorijų apie tokius iš tikrųjų vykstančius scenarijus.

Šis straipsnis nėra skirtas baimintis ar išgąsdinti, o paskatinti vartotojus atlikti tam tikrą tyrimą, kokie apsaugos nuo naršymo internete metodai jiems tinka. Geros naujienos yra tai, kad šie įgūdžiai bus perkeliami ir į bendrą interneto naudojimą, o ne tik naudojant „Monero“, todėl mūsų pasaulyje, kuriame vis dažniau prisijungiama prie interneto, išmanus vartotojas negali suklysti, kaupdamas reikiamas žinias ir įgūdžius, kad išliktų saugus. ir tikrai būti savo banku.

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