---
title: "Kā Monero izmanto hard-forks tīkla uzlabošanai"
slug: "network-upgrades"
date: "2022-02-10"
image: "/images/upgrades.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Viena no visbiežāk pārprastajām daļām Monero pieejā decentralizētas, privātumu saglabājošas un drošas kriptovalūtas izveidei ir loma, ko spēlē atzarojumi (vai tīkla jauninājumi).

Šajā rakstā mēs apskatīsim, kas ir atzarojumi, kāpēc tie ir svarīgi Monero un kādu lomu jūs tajos varat spēlēt nākotnē.

## Kāpēc Monero ir jāturpina tīkla uzlabošana?

Monero kopiena ir apņēmusies pārskatīt un uzlabot projektu laika gaitā, un šķiet, ka apņemšanās ir saistīta ar diviem galvenajiem kopienas ētikas aspektiem: 

  1. Monero projekts galu galā ir programmatūra — kods, ko rakstījuši cilvēki. Tas var novest pie nepieciešamības labot kļūdas, pievienot laika gaitā atklātus vai izgudrotus uzlabojumus, ieviest protokola modernizāciju vai vienkārši uzturēt projektu. Tas daudzējādā ziņā ir līdzīgs citām jūsu izmantotajām programmatūras daļām (piemēram, pārlūkprogrammai, kurā to lasāt!), kas ir pastāvīgi jāatjaunina, lai pievienotu jaunas funkcijas un labotu kļūdas.

  2. Monero projekts ir privātuma rīks, un privātums ir arvien progresējoša bruņošanās sacensība. Cilvēki un grupas, kas nevēlas neko vairāk kā atņemt privātuma pasauli (gan finansiālu, gan personisku), pastāvīgi uzlabo, attīstās un izgudro jaunus veidus, kā uzbrukt modernām pieejām privātuma saglabāšanai, piemēram, Monero izmantotajām pieejām. Tā kā privātuma ienaidnieki atrod šīs jaunās pieejas, Monero tīklam ir jāspēj pielāgoties un uzlabot, lai cīnītos un aizstāvētu mūsu tiesības uz finansiālo privātumu.

Monero projekts galu galā ir programmatūra — kods, ko rakstījuši cilvēki. Tas var novest pie nepieciešamības labot kļūdas, pievienot laika gaitā atklātus vai izgudrotus uzlabojumus, ieviest protokola modernizāciju vai vienkārši uzturēt projektu. Tas daudzējādā ziņā ir līdzīgs citām jūsu izmantotajām programmatūras daļām (piemēram, pārlūkprogrammai, kurā to lasāt!), kas ir pastāvīgi jāatjaunina, lai pievienotu jaunas funkcijas un labotu kļūdas.

Monero projekts ir privātuma rīks, un privātums ir arvien progresējoša bruņošanās sacensība. Cilvēki un grupas, kas nevēlas neko vairāk kā atņemt privātuma pasauli (gan finansiālu, gan personisku), pastāvīgi uzlabo, attīstās un izgudro jaunus veidus, kā uzbrukt modernām pieejām privātuma saglabāšanai, piemēram, Monero izmantotajām pieejām. Tā kā privātuma ienaidnieki atrod šīs jaunās pieejas, Monero tīklam ir jāspēj pielāgoties un uzlabot, lai cīnītos un aizstāvētu mūsu tiesības uz finansiālo privātumu.

## Kas ir hard-fork?

Monero uzlabošanas sarežģītība stājas spēkā, kad saprotat, cik atšķirīga ir kriptovalūtas uzlabošana salīdzinājumā ar vienkāršu programmatūras atjauninājuma nosūtīšanu, piemēram, pārlūkprogrammai.

Kriptovalūtās par tīkla noteikumiem (piemēram, kā pārskaitījumiem vajadzētu izskatīties, kā notiek mainošana un kā pārbaudīt katru bloku) ir jāvienojas tīklam, un to sauc par “vienprātību”. Ja kāds no šiem noteikumiem ir jāmaina vai jāuzlabo, tīklam ir jāvienojas par jaunajiem noteikumiem, izraisot “hard-fork” jeb atzarojumu – situāciju, kad tīkls faktiski sadalās divās bloku ķēdēs – viena dzīvo pēc vecajiem noteikumiem, un viena pēc jaunajiem.

Kad visi kopienas locekļi piekrīt noteikumu izmaiņām, to sauc par “nestrīdīgu hard-fork”, un ķēde, kurai joprojām ir spēkā vecie noteikumi, nomirst un netiek mainota pēc “hard-fork”. Tas ir noticis gandrīz ar katru Monero atzarojumu, un vienīgais veco noteikumu turpinājums bija projekti, kas mēģināja gūt peļņu no hard-fork.

Lai gan nestrīdīgi hard-forks ir vienīgais veids, kā pareizi uzlabot svarīgus Monero tīkla aspektus, tiem ir arī kaitinoša blakusparādība — vecā programmatūra, kas tika izdota pirms hard-fork plānošanas, nevar saprast jaunos tīkla noteikumus un tāpēc nedarbojas pēc hard-fork! Tas var novest pie tā, ka lietotāji domā, ka līdzekļi ir pazaudēti un Monero blokķēde ir apstājusies, un viņi nevar pārvietot līdzekļus, kamēr nav atjauninājuši savus makus.

## Kurš izlemj, kad Monero tīkls tiks uzlabots un kas tiks iekļauts?

Tā kā Monero nav centrālās iestādes, izpilddirektora vai prezidenta, darbs pie lēmuma pieņemšanas, kad atjaunināt tīklu, ko iekļaut un kā to darīt, ir _mums_ , tiem cilvēkiem Monero kopienā, kas izvēlas iesaistīties un mijiedarboties! Šī ir ārkārtīgi svarīga decentralizēta projekta daļa, jo projekta plānošana un lēmumu pieņemšana galu galā ir decentralizēta, un to nodrošina kopiena.

Katrā Monero tīkla jauninājumā iekļauto laiku un funkciju plānošana notiek divās galvenajās vietās:

  1. IRC un Matrix, Monero kopienas visbiežāk izmantotās tērzēšanas platformas (kas ir savienotas kopā). Šīs platformas nodrošina lielu grupu tērzēšanu, un tajās notiek visas ieplānotās Monero kopienas sanāksmes, izstrādātāju sanāksmes un pētniecības laboratorijas sanāksmes. Šīs sanāksmes ir labākais veids, kā klausīties (vai dot ieguldījumu!) plānošanā un diskusijās par Monero tīkla jauninājumiem.

  2. Github — galvenajā saziņas platformā ilgstošām Monero diskusijām, plānošanai un organizēšanai. Monero kopiena izmanto Github, lai organizētu sanāksmes, apspriestu jaunas funkcijas un idejas un koordinētu tīkla jauninājumu plānošanu papildus Monero projekta koda glabāšanai.

IRC un Matrix, Monero kopienas visbiežāk izmantotās tērzēšanas platformas (kas ir savienotas kopā). Šīs platformas nodrošina lielu grupu tērzēšanu, un tajās notiek visas ieplānotās Monero kopienas sanāksmes, izstrādātāju sanāksmes un pētniecības laboratorijas sanāksmes. Šīs sanāksmes ir labākais veids, kā klausīties (vai dot ieguldījumu!) plānošanā un diskusijās par Monero tīkla jauninājumiem.

Github — galvenajā saziņas platformā ilgstošām Monero diskusijām, plānošanai un organizēšanai. Monero kopiena izmanto Github, lai organizētu sanāksmes, apspriestu jaunas funkcijas un idejas un koordinētu tīkla jauninājumu plānošanu papildus Monero projekta koda glabāšanai.

Ja jums ir svarīga ideja par tīkla jaunināšanu, jums nepatīk kāda pieeja vai ja jums ir bažas par jaunināšanas laiku, ir svarīgi, lai jūs izteiktos un skaidri izklāstītu savu viedokli kopienai!

## Kā es varu palīdzēt ar tīkla uzlabojumiem?

Tā kā Monero tīkla uzlabojumiem ir nepieciešama kopienas koordinācija un apstiprināšana, kā arī programmatūras atjauninājumi, ir ārkārtīgi svarīgi, lai tīkla uzlabojumu plānošanā, testēšanā un saziņas procesā iesaistītos pēc iespējas vairāk cilvēku.

Šeit ir daži vienkārši veidi, kā palīdzēt atrisināt problēmas saistībā ar tīkla uzlabošanu:

  1. Pievienojieties plānošanas sapulcēm [, kas publicētas vietnē Github](https://github.com/monero-project/meta/issues), ieklausieties un sniedziet ieguldījumu, ja jums ir kas aktuāls.
  2. Sazinieties ar informāciju par tīkla atjaunināšanas laiku (kad tas ir izlemts!) ar savu iecienītāko biržu, maku vai mainošanas baseinu. Var būt sarežģīti pareizi informēt visus Monero lietotājus par atjaunināšanu, tāpēc ir svarīgi, lai mēs visi palīdzētu izplatīt šādu informāciju, kur vien varam.
  3. Pārbaudiet programmatūru pirms tīkla uzlabojumiem. Pirms tīkla atjaunināšanas tiks aicināts testēt gan testnet, gan stagenet, lai nodrošinātu, ka visi uzlabojuma aspekti ir pareizi plānoti un ieviesti programmatūrā. Jo vairāk cilvēku iesaistīsies un rūpīgi izmēģinās jaunās versijas, jo lielāka iespēja, ka tīkla atjaunināšana noritēs raiti!
  4. Kad ir publicēti izdevumi, kas ir saderīgi ar tīkla atjauninājumu, noteikti veiciet atjaunināšanu nekavējoties! Jo vairāk cilvēku ir atjauninājuši un gatavi tīkla atjaunināšanai, jo raitāk tīkls ar to tiks galā un lietotājiem būs mazāk galvassāpju.

## Ko varam sagaidīt nākamajā Monero tīkla atjauninājumā?

Lai gan datums vēl nav akmenī kalts, drīzumā tiks veikts tīkla atjauninājums, lai ieviestu dažus svarīgus Monero uzlabojumus un funkcijas:

  1. Gredzena izmēra palielināšana no 11 uz 16, palielinot pamata anonimitātes kopu (lasiet: ticamu noliedzamību vai pamata konfidencialitāti) katram pārskaitījumam tīklā
  2. [Skata atzīmes — lielisks veids, kā samazināt maka sinhronizācijas laiku par 30–40%](/knowledge/view-tags-reduce-monero-sync-time/)
  3. Maksas izmaiņas, uzlabojot tīkla drošību un noturību pret straujām izmaiņām maksas tirgū vai ļaunprātīgu subjektu uzbrukumiem
  4. [Bulletproofs+ — turpmāks Monero pārskaitījumu efektivitātes uzlabojums](https://www.getmonero.org/2020/12/24/Bulletproofs+-in-Monero.html)

Šīs izmaiņas ievērojami uzlabos tīkla privātumu, efektivitāti un drošību, vienlaikus paverot ceļu [Seraphis](/knowledge/seraphis-for-monero/), nākamās paaudzes pārskaitījumu protokolam Monero.

## Kā es varu uzzināt vairāk?

Tēma par atzarojumiem un tīkla uzlabojumiem ir plaša, un Monero tiem ir gara un vēsturiska vēsture. Tāpēc noteikti iedziļinieties dažās no tālāk norādītajām saitēm, ja vēlaties uzzināt vairāk par vēsturi, procesu vai plānošanu, kas notiek gaidāmajai tīkla atjaunināšanai!

  * [Monero v15 hard-fork plānošana](https://github.com/monero-project/meta/issues/630)
  * [Plānotie programmatūras atjauninājumi (Monero)](https://github.com/monero-project/monero#scheduled-software-upgrades)
  * [Piezīme par plānotajiem protokola atjauninājumiem](https://web.getmonero.org/2020/09/01/note-scheduled-upgrades.html)

Lasīt tālāk

  * [Kā Monero unikāli nodrošina aprites ekonomiku](/knowledge/monero-circular-economies/)

  * [Monero gredzenveida paraksti salīdzinājumā ar CoinJoin kā Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Kāpēc (un kā!) jums vajadzētu turēt savas atslēgas](/knowledge/hold-your-keys/)

  * [Iesaiste Monero](/knowledge/contributing-to-monero/)

  * [Kā attālie mezgli ietekmē Monero privātumu](/knowledge/remote-nodes-privacy/)

  * [Skata tagi: kā viens baits samazinās Monero maka sinhronizācijas laiku par 40%+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool un tā loma Monero mainošanas decentralizācijā](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: ko tas darīs Monero](/knowledge/seraphis-for-monero/)

  * [Vai Bitcoin konvertēšana uz Monero ir tikpat privāta kā Monero pirkšana tieši?](/knowledge/most-private-way-to-buy-monero/)

  * [Kāpēc Monero atšķirībā no Zcash izmanto bezuzticības iestatījumu](/knowledge/monero-trustless-setup/)

  * [Kāpēc Monero ir labāks vērtības glabātājs nekā Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Kā Monero var pārvarēt Bitcoin tīkla efektus](/knowledge/network-effect/)

  * [Kāpēc Monero ir viskritiskāk domājošā kopiena](/knowledge/critical-thinking/)

  * [Krāpniecība, kam jāpievērš uzmanība, lietojot Monero](/knowledge/monero-scams/)

  * [Kā Monero darbosies atomiskā apmaiņa](/knowledge/monero-atomic-swaps/)

  * [Kas jāzina ikvienam Monero lietotājam, kad runa ir par tīklu veidošanu](/knowledge/monero-networking/)

  * [Kā RingCT slēpj Monero pārskaitījumu summas](/knowledge/monero-ringct/)

  * [Kā Monero slepenās adreses aizsargā jūsu identitāti](/knowledge/monero-stealth-addresses/)

  * [Kā Monero apakšadreses novērš identitātes saistīšanu](/knowledge/monero-subaddresses/)

  * [Monero izvades tuvplānā](/knowledge/monero-outputs/)

  * [Monero labākā prakse iesācējiem](/knowledge/monero-best-practices/)

  * [Kā gredzenveida paraksti apslēpj Monero izvadi](/knowledge/ring-signatures/)

  * [Kā Monero atrisināja bloka izmēra problēmu, kas vajā Bitcoin](/knowledge/dynamic-block-size/)

  * [Kā CLSAG uzlabos Monero efektivitāti](/knowledge/what-is-clsag/)

  * [Kāpēc Monero ir astes emisija](/knowledge/monero-tail-emission/)

  * [Īsa Monero vēsture](/knowledge/monero-history/)

  * [Žurnāls Wired kļūdās par Monero. Lūk, kāpēc](/knowledge/wired-article-debunked/)

  * [15 populārākie Monero mīti un bažas atspēkotas](/knowledge/monero-myths-debunked/)

  * [Kā Dandelion++ saglabā Monero pārskaitījumu izcelsmi privātu](/knowledge/monero-dandelion/)

  * [Kāpēc Monero ir atvērtā pirmkoda un decentralizēts](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero mainošana: ar ko RandomX ir tik īpašs](/knowledge/monero-mining-randomx/)

  * [Kāpēc Monero ir labāks par Dash, Zcash, Zcoin (pat ar Lelantus), Grin un Bitcoin mikseriem, piemēram, Wasabi (atjaunināts 2020. gada maijā)](/knowledge/why-monero-is-better/)