---
title: "Kā CLSAG uzlabos Monero efektivitāti"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Kā protokols, Monero pašlaik ir pastāvīgas inovācijas stāvoklī. Izmantojot pētījumus gan ķēdē, gan ārpus ķēdes risinājumos, Monero kopiena meklē jomas, kuras jāuzlabo, lai padarītu Monero privātāku, vieglāk paplašināmu un pieejamu visiem. Viens no pēdējiem jauninājumiem ir saistāmās gredzenveida parakstu shēmas MLSAG aizstāšana ar ievietošanas nomaiņu CLSAG, kas nozīmē Concise Linkable Spontaneous Anonymous Group.

Virspusējā līmenī CLSAG ieviešana par 25% samazinās izplatītākos 2 ievades, 2 izvades darījumus. Mēs arī redzēsim par 10% mazāku apstiprināšanas laiku.

Bet kas īsti ir CLSAG? Ko tas dara un kā tas atšķiras no vecās versijas MLSAG? Atvēlēsim minūti, lai atgādinātu sev par to, kāpēc un kā tiek izmantoti gredzenveida paraksti, lai mēs varētu labāk izprast šo jēdzienu. Gredzenveida paraksti nodrošina neinteraktīvus, neatšķiramus ievades datus, izmantojot parakstītāja atlasītas iepriekšējo izvadu anonimitātes grupas. Īsāk sakot, tas ļauj lietotājam slēpt savus pārskaitījumā izmantotos rezultātus starp nesaistītiem rezultātiem, un viņi to visu var izdarīt, nevienam citam nepiedaloties. Viss, kas jums nepieciešams, ir blokķēdes kopija. Katra no šīm izvadēm var būt īstā nosūtītā ar vienlīdz lielu varbūtību, tādējādi slēpjot metadatus par sūtītāju.

Tomēr tas rada nelielas problēmas. Kā būtu, ja lietotājs izveidotu gredzena parakstu tikai ar mānekļa izvadiem? Kā lai kāds zinātu, ka nezināmajam sūtītājam nav tiesību nosūtīt kādu no tiem? Vai šis lietotājs varētu tērēt viltotu naudu? Atbilde ir nē. Gredzenveida paraksts ietver metodi, lai pierādītu, ka vismaz viens no izvadiem pieder nezināmam sūtītājam, neatklājot, kurš tas ir. Faktiski gan CLSAG, gan MLSAG (turpmāk SAG) ir daļa no gredzena paraksta, kas to pierāda. Interesanti, ka tajā pašā laikā tas pierāda, ka darījuma summa, kaut arī slēpjas aiz konfidenciāliem pārskaitījumiem (RingCT), ir līdzsvarā. Tas, ka SAG pierāda divas lietas - ka viena izvade pieder kādam gredzena dalībniekam un ka darījums ir līdzsvarots - arī ir izmēra un pārbaudes ietaupījumu pamatā. Ja tas kļūst mulsinoši, neuztraucieties, mēs drīzumā nonāksim pie jautras un viegli saprotamas analoģijas.

Vecā parakstu shēma MLSAG (multilayed Linkable Spontaneous Anonymous Group) pierāda iepriekš minētās divas lietas gredzenveida parakstā, taču tā dara katru atsevišķi. Atsevišķu aprēķinu izmantošana parakstīšanas un saistību atslēgām nozīmē lēnākas darbības. Mūsdienīgs dators var veikt šos aprēķinus dažās milisekundēs, kas nešķiet daudz, un vienam pārskaitījumam tā arī nav. Bet, ja ņemam vērā Monero blokķēdē veikto pārskaitījumu skaitu un to, ka makam, kas sinhronizējas no nulles, būs jālejupielādē un jāpārbauda katrs no tiem, baiti un milisekundes ātri sakrājas.

CLSAG apvieno matemātiku, kas nepieciešama, lai pierādītu abus vienā, kā arī aprēķina abus vienlaikus, turklāt tas tiek darīts drošā veidā. Ko nozīmē drošā veidā? Lai to noskaidrotu un, cerams, padarītu visu saprotamu, aplūkosim šo solīto jautro analoģiju.

Pieņemsim, ka jums ir jāiet gan uz pārtikas preču veikalu, gan datortehnikas veikalu, lai paņemtu divas dažādas lietas: pārtiku un toksiskas tīrīšanas ķimikālijas. Jūs nevēlaties, lai tie sajaucas, jo, ja ķīmiskās vielas izlīs uz pārtikas, tā kļūs neēdama. Jūs nolemjat būt īpaši drošs un braukt no savas mājas uz pārtikas veikalu, nopirkt pārtiku un pēc tam doties atpakaļ uz savu māju. Tikai pēc pārtikas izkraušanas jūs atkal iekāpjat automašīnā, braucat uz datortehnikas veikalu un atpakaļ uz māju ar ķimikālijām. Jūs esat veicis divus atsevišķus braucienus, lai nodrošinātu visu pirkumu drošību. Lai gan tas patiešām ir droši, tas ir neefektīvi. Tas atspoguļo MLSAG, kur tiek glabātas divas dažādas matemātiskas kopas un veikti divi dažādi “izbraucieni”, lai tās aprēķinātu.

Tomēr jūs nolemjat, ka vēlaties to izdarīt ātrāk. Šādi tiek izniekots pārāk daudz laika. Protams, to darot vienu vai divas reizes, jūs nepalaidīsiet garām visu dzīvi, taču, darot to atkal un atkal, stundas sakrājas. Jūs sākat domāt, vai tā vietā varat veikt vienu braucienu. No jūsu mājas uz pārtikas veikalu, tad uz datortehnikas veikalu un atpakaļ uz mājām. Jūs nevarat vienkārši iemest visu savā automašīnā. Tas nav droši. Tā vietā jūs savā automašīnā iezīmējat dažādas vietas dažādām lietām un pārliecināties, ka viss stabili atrodas savās vietās. To darot, jūs varat droši doties vienā braucienā uz abiem veikaliem un turēt lietas tālāk viena no otras. Tas apzīmē CLSAG. Tagad pārskaitījumā ir saglabāta tikai viena matemātikas kopa, lai pierādītu šīs divas lietas, un tas tiek darīts tā, ka tā netraucē viena otrai. Braucieni joprojām ir jāveic, taču jūs esat diezgan krasi samazinājis to skaitu.

Tas viss izklausās diezgan aizraujoši. Vai ir iespējams atrast citus īsceļus vai citus veidus, kā ietaupīt laiku un vietu? Atbilde ir jā un nē. Saskaņā ar pašreizējiem MRL pētniekiem, visticamāk, nav iespējams turpināt modificēt SAG tipa konstrukcijas, lai nodrošinātu labāku izmēru vai ātrumu; tomēr citas konstrukcijas, piemēram, Arcturus, Omniring, RCT3 vai Triptych, rada daudz labākas izmēra paplašināšanas un pārbaudes priekšrocības, izmantojot dažādas matemātiskās metodes. Tomēr katrai no šīm "nākamās paaudzes" pieejām neskaidra parakstītāja protokoliem ir savi kompromisi ieviešanas detaļās, un tiek veikta aktīva izpēte un izmeklēšana.

Galu galā, Monero vienmēr rada jauninājumus.

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

  * [Kāpēc Monero ir astes emisija](/knowledge/monero-tail-emission/)

  * [Īsa Monero vēsture](/knowledge/monero-history/)

  * [Žurnāls Wired kļūdās par Monero. Lūk, kāpēc](/knowledge/wired-article-debunked/)

  * [15 populārākie Monero mīti un bažas atspēkotas](/knowledge/monero-myths-debunked/)

  * [Kā Dandelion++ saglabā Monero pārskaitījumu izcelsmi privātu](/knowledge/monero-dandelion/)

  * [Kāpēc Monero ir atvērtā pirmkoda un decentralizēts](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero mainošana: ar ko RandomX ir tik īpašs](/knowledge/monero-mining-randomx/)

  * [Kāpēc Monero ir labāks par Dash, Zcash, Zcoin (pat ar Lelantus), Grin un Bitcoin mikseriem, piemēram, Wasabi (atjaunināts 2020. gada maijā)](/knowledge/why-monero-is-better/)