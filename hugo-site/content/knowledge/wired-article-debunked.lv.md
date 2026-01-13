---
title: "Žurnāls Wired kļūdās par Monero. Lūk, kāpēc"
slug: "wired-article-debunked"
date: "2020-06-24"
image: "/images/wired.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Gan privātuma, gan kriptovalūtas jomā bieži tiek izplatīta dezinformācija. Mums ir [raksts, kurā izklāstīti piecpadsmit plaši izplatīti nepareizi vai novecojuši pieņēmumi par Monero](/knowledge/monero-myths-debunked), taču mēs vēlamies veltīt laiku vienam konkrētam rakstam, ko bieži citē un izplata Monero skeptiķi.

Izdevums Wired 2018. gada 27. martā publicēja [rakstu](https://www.wired.com/story/monero-privacy/), kas pats tika uzrakstīts, reaģējot uz citu nesen publicētu dažādu akadēmisko aprindu rakstu ar nosaukumu “Empīriskā analīze par izsekojamību Monero blokķēdē”.

Lai gan rakstu līdzautorēja personas, kurām ir skaidrs interešu konflikts (viņi ir Zcash padomdevēji un ir līdzdalība tajā), Monero kopiena šo rakstu uztvēra vidēji atzinīgi, jo tas apstiprina lietas, ko kopiena jau ir zinājusi un par ko ir rakstīts viņu pašu Monero Research Lab dokumentos ([MRL-0001](https://web.getmonero.org/resources/research-lab/pubs/MRL-0001.pdf) un [MRL-0004](https://web.getmonero.org/resources/research-lab/pubs/MRL-0004.pdf)), no kuriem pirmais tika publicēts pirms četriem gadiem. Tomēr ar to bija arī vairākas pretrunas, galvenokārt interešu konflikts, fakts, ka jautājumi jau bija zināmi, apspriesti un dažos gadījumos arī novērsti, un Monero privātuma garantiju rupja nepareiza raksturošana tajā laikā. Kopiena komentēja darba priekšdruku, un daudzi no ieteikumiem tika iekļauti galīgajā dokumentā.

Bet kas tieši tika nepareizi raksturots? Fakts, ka Monero vairāk nekā gadu nebija pieļāvuši rakstā apspriestos trūkumus. Pārskaitījumi, kas veikti pirms 2017. gada, patiešām bija neaizsargāti pret privātuma noplūdi, taču publicēšanas laikā Monero bija atrisināta lielākā daļa problēmu. Lai būtu godīgi pret autoriem, viņi nelielā mērā apspriež Monero risinājumus, taču ne pietiekami, lai paskaidrotu to ietekmi uz kriptovalūtu mediju ciklu tajā laikā. Līdz ar to Wired raksts.

Lai gan mēs varam aplūkot attiecīgo Wired rakstu kā attiecīgā laika liecību un to, cik patiess vai nepatiess tas tajā laikā bija, fakts, ka tas joprojām tiek izplatīts šodien, lai pamatotu, kāpēc Monero privātuma garantijas ir vājas, patiesībā liek analizēt, kā raksts noturas tagadnē. Mēs ar prieku pieņemam šo ielūgumu.

Ātri izlasot rakstu, redzamas vairākas sensacionālas rindiņas, piemēram, “[Atklājumiem] nevajadzētu tikai uztraukties ikvienam, kurš šodien mēģina zagšus tērēt Monero”, un viss raksta tonis, kurā pētījums tiek postulēts kā “jauns”, lielā mērā balstās uz publikāciju. Pašā akadēmiskajā darbā ir ieteikumi, piemēram, brīdinājums Monero lietotājiem par iespējamu viņu anonimitātes kompromisu, neskatoties uz to, ka šīs diskusijas ne tikai notika kopš 2014. gada, bet arī kopienas aicinājums bija, lai cilvēki neiegādātos Monero un ka tas bija ļoti eksperimentāls.

Bet kā ar pašu kritiku? Realitāte ir tāda, ka daudzas problēmas ar Monero kā privātuma monētu vai nu vairs neattiecas uz Monero, vai arī ir kopīgas bažas par privātuma monētām kā uz blokķēdes balstītu kriptovalūtu kategoriju. Sāksim risināt šos jautājumus.

Viena no visbiežāk citētajām Monero kritikām ir tāda, ka blokķēdes pastāvības un nemainīguma dēļ, ja nākotnes tehnoloģija varētu uzlauzt privātumu, visi Monero iepriekšējie pārskaitījumi tiktu atklāti. Citiem vārdiem sakot, jūsu privātumam ir tikšķošs pulkstenis.

Mēs nevaram to pietiekami uzsvērt. Burtiski katrai privātuma monētai, kurā tiek izmantotas ķēdes metodes neskaidrības un privātuma nodrošināšanai, ir šis trūkums, un tomēr tā bieži tiek izmantota pret Monero (ironiskā kārtā daudzas reizes no konkurējošām privātuma monētām ar tādu pašu problēmu), un tā tiek darīts arī šajā rakstā. Reakcija uz šo kritiku dažiem varētu būt pārsteidzoša, taču Monero patiesībā var būt mazāk ievainojams nekā citas privātuma monētas, jo tam ir daudzpusīga pieeja privātumam.

Monero slēpj izvades (sūtītājus), summas un saņēmējus, izmantojot attiecīgi trīs dažādas tehnoloģijas - gredzenveida parakstus, RingCT un slepenās adreses. No tiem gredzenveida paraksti ir vājākie un visvairāk pakļauti gan mūsdienu heiristikai, gan teorētiskām nākotnes tehnoloģijām, kas uzlauž privātumu. Monero kopiena to zina jau gadiem ilgi, un tiek veikti aktīvi pētījumi, lai pilnībā uzlabotu vai aizstātu gredzenveida parakstu shēmu.

Tomēr, pat ja gredzenveida paraksts būtu pilnībā bojāts, tiktu atklāta tikai patiesā izvade. NEVIS sūtītājs (kā indivīds), bet izvade. Izvades savienošana ar identitāti nav neiespējama, taču tam būtu nepieciešams vairāk metadatu un resursu. Kopā ar faktu, ka RingCT un slepenā adrese NETIKS atklāta, ietekme vēl vairāk samazinās.

Jāatzīmē, ka Wired raksta daļā, kurā viņi sazinājās ar Rikccrdo 'fluffypony' Spagni, lai saņemtu komentāru, ir viegli apskatīta iepriekš minētā informācija, taču tam atvēlētais laiks ir īss, un šķiet, ka tam pārskriets pāri. Izpratnes trūkums ir īpaši acīmredzams, mēģinot apspriest šīs lietas ar cilvēkiem, kuri mūsdienās dalās ar šo rakstu.

Vēl viena kritika, ko ir daudz grūtāk risināt, ir par to, kā ārpasaule uztver Monero un kā tas ir saistīts ar to, kā Monero apkārtējā sabiedrība uztver monētu. Lai iegūtu piemēru, lasītājiem nav jāmeklē tālāk par paša raksta nosaukumu: “Tumšā tīmekļa iecienītākā valūta ir mazāk neizsekojama, nekā šķiet”.

Ikviena persona, kas pavada ievērojamu laiku Monero kopienā, var apliecināt, ka Monero kopiena dara visu iespējamo, lai parādītu, cik grūti ir panākt īstu privātumu, pat kaitējot mārketinga vai adopcijas centieniem. Ja kopiena nodrošina pietiekami daudz resursu, lai precīzi apspriestu monētu un tās trūkumus, kādā brīdī nezināšana kļūst par lietotāja vainu, kurš uzskata, ka monēta ir viss, kas viņam nepieciešams, lai būtu 100% privāts.

Šobrīd ir skaidrs, ka Monero kopiena nopietni uztver gan savu privātumu, gan godīgumu attiecībā uz tā trūkumiem un turpmākajiem uzlabojumiem. Rakstiem, tāpat kā attiecīgajam rakstam, pilnīgi trūkst šī Monero inovācijas gara. Tas salīdzina Monero ar citu kriptovalūtu bariem, kas izvirza grandiozus solījumus, domājot tikai par peļņu un neizglītotiem investoriem.

Realitāte nevar būt savādāka. Monero ļoti labi apzinās savas vājās puses, tiecas turpināt izstrādi, lai tās uzlabotu, savilktu vājās vietas un sasniegtu ļoti reālo, bet ļoti grūto mērķi – dot pasaulei privātu, aizstājamu kriptovalūtu, ko var izmantot visi, un darīt to visu godīgā, decentralizētā un uz sabiedrību virzītā veidā. Varbūt ir pienācis laiks atmest sensacionalizāciju un rakstu kopīgošanu kā līdzekli, lai promotētu aktīvus un reklamētu konkurentus. Varbūt ir pienācis laiks pastāstīt citu stāstu.

Lasīt tālāk

  * [Kā Monero unikāli nodrošina aprites ekonomiku](/knowledge/monero-circular-economies/)

  * [Monero gredzenveida paraksti salīdzinājumā ar CoinJoin kā Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Kāpēc (un kā!) jums vajadzētu turēt savas atslēgas](/knowledge/hold-your-keys/)

  * [Iesaiste Monero](/knowledge/contributing-to-monero/)

  * [Kā attālie mezgli ietekmē Monero privātumu](/knowledge/remote-nodes-privacy/)

  * [Kā Monero izmanto hard-forks tīkla uzlabošanai](/knowledge/network-upgrades/)

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

  * [15 populārākie Monero mīti un bažas atspēkotas](/knowledge/monero-myths-debunked/)

  * [Kā Dandelion++ saglabā Monero pārskaitījumu izcelsmi privātu](/knowledge/monero-dandelion/)

  * [Kāpēc Monero ir atvērtā pirmkoda un decentralizēts](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero mainošana: ar ko RandomX ir tik īpašs](/knowledge/monero-mining-randomx/)

  * [Kāpēc Monero ir labāks par Dash, Zcash, Zcoin (pat ar Lelantus), Grin un Bitcoin mikseriem, piemēram, Wasabi (atjaunināts 2020. gada maijā)](/knowledge/why-monero-is-better/)