---
title: "Seraphis: ką tai padarys Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: modulinis dizaino atnaujinimas Monero sandoriams

## Seraphis: modulinis dizaino atnaujinimas Monero sandoriams

Šiame įraše aprašomas [Seraphis](https://github.com/UkoeHB/Seraphis) – operacijų protokolų struktūrų ir abstrakcijų rinkinys, kurį sukūrė pseudoniminis tyrimo bendradarbis [`koe`](https://github.com/UkoeHB), skirtas Monero ekosistemai ir atliekama saugumo analizė. pseudoniminis bendradarbis [`coinstudent2048`](https://github.com/coinstudent2048).  
Siekdami aiškumo, šiek tiek supaprastiname ir praleidžiame tam tikras technines detales; Dėl šios priežasties ir dėl to, kad Seraphis dizainas vis dar vyksta, suinteresuoti skaitytojai turėtų ieškoti naujausios informacijos Seraphis dokumentacijoje.

## Sandoriai Monero

## Sandoriai Monero

Protokolai, tokie kaip Bitcoin, Monero ir kiti, remiasi vadinamuoju „išvesties modeliu“, kai _išvestis_ yra vertės, kurią galima perduoti, atvaizdas.  
Operacijos sunaudoja vieną ar daugiau siuntėjo valdomų išėjimų ir generuoja naujus išėjimus, nukreiptus į gavėjus (arba atgal į siuntėją kaip pasikeitimą); sandoris turi būti subalansuotas taip, kad sunaudotų išėjimų bendra vertė turi būti lygi naujų išėjimų vertei (plius tinklo nustatytas mokestis).  
Daugelyje protokolų, pvz., Bitcoin, išvestyje esanti reikšmė, kaip ir gavėjas, rašoma aiškiai.  
Be to, pažvelgus į blokų grandinę, yra trivialu pamatyti, ar ir kada išvestis buvo išleista (ty ar ji buvo sunaudota atliekant vėlesnę operaciją ir kuri operacija ją išleido).

Priešingai, tokie protokolai kaip Monero pateikia kitokį dizainą:

  * Išvesties reikšmės yra paslėptos ir nematomos blokų grandinėje
  * Gavėjų adresai paslepiami naudojant vienkartinį adresavimo protokolą
  * Nesvarbu, ar išvestis buvo išleista, ar ne, slepia dviprasmiški parašai

Todėl, jei nėra išorinės informacijos, sunku nustatyti, ar tam tikra produkcija buvo išleista, kokia jos vertė ir kas jos gavėjas.

Dabartinis Monero operacijų protokolas vadinamas _RingCT_ ir naudoja kelis kriptografinius blokus šiems projektavimo tikslams pasiekti.

  * _Įsipareigojimai_ slepia sumas matematiškai naudingu būdu
  * _Atstumo patikrinimas_ apsaugo nuo perpildymo, dėl kurio gali padidėti tiekimas
  * _Susiejami skambučio parašai_ suteikia pasirašiusiųjų neaiškumą ir neleidžia dvigubai išleisti pinigų
  * _Įsipareigojimų užskaita_ patvirtinama, kad operacijų likutis

Šie blokai yra kruopščiai susipynę, kad būtų sukurtas RingCT protokolas.

Naudinga RingCT protokolo savybė yra ta, kad kai kuriuos konstrukcinius blokus galima pakeisti arba atnaujinti taip, kad bendras dizainas ir savybės išliktų nepakitusios, tačiau tai gali pagerinti efektyvumą ar saugumą. Tiesą sakant, tokie atnaujinimai įvyko (arba planuojami) kelis kartus Monero istorijoje. Pradiniame RingCT protokole diapazono įrodymai buvo dideli ir lėti; vėliau jie buvo atnaujinti į konstrukciją, pavadintą [Bulletproofs](https://eprint.iacr.org/2017/1066), dėl kurios operacijos buvo mažesnės ir greitesnės, atlikus geresnę saugumo analizę, ir planuojama atnaujinti į naujesnę konstrukciją, pavadintą [Bulletproofs+](https://eprint.iacr.org/2020/735), kad būtų dar daugiau efektyvumo. 

Panašus procesas buvo atliktas su susiejamu žiedo parašo kūrimo bloku. Pradiniame protokole buvo naudojama konstrukcija, vadinama [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34). Vėliau ji buvo atnaujinta į naujesnę konstrukciją, pavadintą [CLSAG](https://eprint.iacr.org/2019/654), kuri yra greitesnė, mažesnės operacijos ir geresnė saugumo analizė. Buvo pasiūlyta dar naujesnė susieta žiedinio parašo konstrukcija, pagrįsta [Triptiku](https://eprint.iacr.org/2020/018), tačiau ji nebuvo pasirinkta diegti dėl poveikio kelių parašų operacijoms.

## Serafis

## Serafis

Seraphis šią idėją žengia dar žingsnį.  
Užuot atnaujinę atskirus esamo RingCT operacijų protokolo blokus, jame pristatomas kitoks protokolas, kuris gali pasinaudoti skirtingų kūrimo blokų pranašumais ir pasiūlyti patobulintą funkcionalumą.

## Statybiniai blokai

## Statybiniai blokai

Seraphis naudoja kitokį kriptografinių blokų rinkinį savo projektavimo tikslams pasiekti.

  * _Įsipareigojimai_ vis dar slepia sumas
  * _Diapazono patikrinimas_ vis tiek apsaugo nuo perpildymo ir tiekimo padidėjimo
  * _Narystės įrodymai_ suteikia pasirašiusiojo dviprasmiškumo
  * _Įsipareigojimų užskaita_ vis tiek tvirtinamas balansas
  * _Įgaliojimų patvirtinimas_ neleidžia bandyti išleisti dvigubai 

Atkreipkite dėmesį į pakeitimą čia: susieti žiediniai parašai pakeičiami narystės įrodymų ir įgaliotųjų įrodymų deriniu. Grubiai tariant, narystės įrodymai rodo, kad sunaudota produkcija yra didesnės rinkinio dalis, panašiai kaip ir RingCT. Tačiau skirtingai nei „RingCT“, narystės įrodymai visai neapima susiejimo žymos! Įgaliojantys įrodymai rodo, kad susiejimo žyma galioja ir yra naudojama galutinei operacijai pasirašyti.

Kadangi „RingCT“ įtraukia susiejimo žymą į dviprasmišką parašą, pasirašymo (ir kelių parašų) operacijos reikalauja daug daugiau skaičiavimo, todėl tampa sudėtingiau sukurti kitas su žyma susijusias funkcijas. Tačiau Seraphis narystės įrodymų kūrimą galima saugiai perduoti iš labai patikimų įrenginių (kurių skaičiavimo galia gali būti ribota, pvz., aparatinės įrangos piniginės) į mažiau patikimą įrenginį, o pasirašymo (ir kelių parašų) operacijos yra daug paprastesnės naudojant daug paprastesnį įgaliojimo įrodymą. 

Laimei, kai kurie „Seraphis“ reikalingi elementai jau yra kitur ir jų nereikia kurti nuo nulio. Tiek Bulletproofs, tiek Bulletproofs+ konstrukcijos gali būti naudojamos kaip atsparios nuotoliui. „Schnorr“ tipo įrodinėjimo sistemų modifikacijos gali būti naudojamos patvirtinant įrodymus. O efektyvią [ patvirtinimo sistemą](https://eprint.iacr.org/2015/643), kuri jau buvo naudojama kaip Triptych, [Lelantus](https://eprint.iacr.org/2019/373) ir [Spark](https://eprint.iacr.org/2021/1173)* pagrindas, galima modifikuoti. X2127X] 

* Cypher Stack gauna finansavimą Spark kūrimui.

* Cypher Stack gauna finansavimą Spark kūrimui.

## Kreipimasis

## Kreipimasis

Deja, šiuo metu naudojami Monero adresai nesuderinami su Seraphis. Jei Seraphis būtų įdiegtas, vartotojai turės sugeneruoti naujus adresus iš savo piniginės raktų, kad gautų Monero. Tačiau šios ekosistemos išlaidos turi daug privalumų.

Be aukščiau aptartų struktūrinių pranašumų, Seraphis dizainas yra pritaikytas daugeliui skirtingų adresų kūrimo galimybių, kurių kiekviena turi kompromisų. Nors galutinė Seraphis adreso konstrukcija [ vis dar sprendžiama](https://github.com/monero-project/research-lab/issues/92) (viena schema, kuriai skiriama daug dėmesio, vadinama [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), galime apibūdinti kai kurias įprastas ir naudingas funkcijas.

Galbūt žinote, kad Monero adresai siūlo _peržiūros klavišo_ funkciją, kai įrenginiui arba trečiajai šaliai galite pateikti peržiūros raktą ir leisti jai jūsų vardu stebėti gaunamus išėjimus, tačiau neatsisakant išlaidų. institucija. Tai naudinga piniginėms, kurios gali būti nuolat atnaujinamos, o išlaidų raktas yra saugiai užrakintas. Tai taip pat naudinga tais atvejais, kai norite gauti išorinę peržiūrą, pvz., viešajai labdaros organizacijai, siūlančiai skaidrumą, arba įmonei, turinčiai apskaitos skyrių.

Neigiamas Monero peržiūros klavišų trūkumas yra tas, kad jie nesuteikia visos arba smulkios peržiūros prieigos. Neįmanoma patikimai aptikti, kada piniginė išleidžia lėšas, todėl sunku tinkamai apskaičiuoti piniginės likučius, kai nėra išlaidų rakto. Taip pat šiuo metu neįmanoma aptikti gaunamų išėjimų, taip pat neišmokus tuose išvestiuose esančios reikšmės (tai reiškia, kad bet kuri trečioji šalis, atsakinga už gaunamų išėjimų paiešką, tiksliai sužinos, kiek Monero įsigyjate).

Seraphis adresavimo konstrukcijos gali tai išspręsti. Naudojant „Seraphis“, jūsų adresu pateikiami skirtingi klavišai, kuriais galima atlikti įvairius veiksmus: 

  * Stebėkite gaunamus išėjimus, bet slėpkite jų reikšmę
  * Stebėkite gaunamus išėjimus, bet parodykite jų vertę
  * Stebėkite išeinančius išėjimus
  * Padeda generuoti operacijas, bet jų nepasirašyti
  * Generuokite naujus adresus (naudinga mažmenininkams arba mainams su daugeliu klientų)

Kaip adreso savininkas, turite nuspręsti, kiek įgaliojimų perduoti kitiems įrenginiams ar trečiosioms šalims.

## Didelė nuotrauka

## Didelė nuotrauka

Seraphis yra esminis Monero ekosistemos pokytis. Nors tai susiję su adresų ir operacijų kūrimo blokų pakeitimais, jo dizainas siūlo lankstumą ir naudingas funkcijas, kurios neįmanomos naudojant šiandieninį RingCT protokolą. Nors didžioji dalis dizaino yra baigta ir kuriama iki [diegimo](https://github.com/UkoeHB/monero/tree/seraphis_lib), adresų projektavimas ir saugos analizė tebevyksta. Seraphis siūlo puikią galimybę stumti Monero ekosistemą į priekį!

Papildoma literatūra

  * [Kaip Monero unikaliai įgalina žiedinę ekonomiką](/knowledge/monero-circular-economies)/

  * [Monero žiedo parašai prieš CoinJoin kaip Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Kodėl (ir kaip!) turėtumėte turėti savo raktus](/knowledge/hold-your-keys)/

  * [Prisideda prie Monero](/knowledge/contributing-to-monero)/

  * [Kaip nuotoliniai mazgai veikia Monero privatumą](/knowledge/remote-nodes-privacy)/

  * [Kaip „Monero“ naudoja „hard-forks“ tinklui atnaujinti](/knowledge/network-upgrades)/

  * [Peržiūrėkite žymas: kaip vienas baitas sumažins Monero piniginės sinchronizavimo laiką 40%+](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool ir jo vaidmuo decentralizuojant Monero kasybą](/knowledge/p2pool-decentralizing-monero-mining)/

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