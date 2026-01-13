---
title: "Kā attālie mezgli ietekmē Monero privātumu"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Viena no lielākajām Monero priekšrocībām salīdzinājumā ar citām kriptovalūtām ir tās privātums ķēdē, taču vai esat kādreiz domājis, kā Monero privātums saglabājas, izmantojot attālo mezglu? Kā būtu, ja izmantotu “vieglā maka” serveri, piemēram, MyMonero?

Šajā rakstā mēs iedziļināsimies dažās detaļās par to, kā Monero nodrošina izcilu ķēdes privātumu pat tad, ja tiek izmantots attālais mezgls, kā arī tam, kam jāpievērš uzmanība, izmantojot attālos mezglus.

## Kādas funkcijas veic mezgli Monero?

Tiem, kas mazāk pārzina Monero darbību, Monero tīkla mezglus (vai serverus) var darbināt ikviens un ļaut mezgla īpašniekam vai citiem, ar kuriem viņi izvēlas, to koplietot! – lai sinhronizētu blokķēdes kopiju un nodrošinātu šo kopiju citiem tīklā. Šie mezgli arī pārbauda visus tīklā notiekošos pārskaitījumus, kā arī visus publicētos blokus un nodrošina, ka tie visi atbilst vienprātīgi noteiktajiem noteikumiem.

Otra funkcija, ko mezgli apkalpo Monero, ir veids, kā nodrošināt visus datus, kas jūsu iecienītākajam Monero makam ir nepieciešami, lai pareizi pārbaudītu jums piederošos pārskaitījumus un veiktu jaunus. Šos datus mezgli nodrošina divos veidos: 

  * Maks pieprasa datus no katra blokķēdes bloka, skenē jums piederošus pārskaitījumus un pēc tam izmet, tiklīdz maks tos ir pārbaudījis. 
    * Šī darbība drīzumā tiks ievērojami uzlabota, pateicoties [skatīšanas tagiem](/knowledge/view-tags-reduce-monero-sync-time).
  * Sūtot pārskaitījumus, jūsu izmantotais mezgls nodrošina iespējamo mānekļu (vai viltus ievades) sarakstu, ko izmantot pārskaitījuma veidošanā, nodrošinot, ka jums ir daudz cilvēku, kuros paslēpties katru reizi, kad tērējat Monero. 
    * Šie mānekļi ir daļa no [gredenveida parakstiem](/knowledge/ring-signatures), kas ir svarīga daļa Monero pieejai privātumam ķēdē.

## Kāds ir privātākais un drošākais Monero lietošanas veids?

Labākais, ko darīt, pat ar spēcīgo ķēdes privātumu, ko nodrošina Monero ar attālajiem mezgliem, ir tomēr palaist savu Monero mezglu, lai nodrošinātu, ka jums ir pieejama neskarta Monero blokķēdes kopija un jūsu IP adrese ir labi aizsargāta. Vēl viens ieguvums, darbinot savu mezglu, ir tas, ka varat pievienoties tīklam, ļaujot citiem mezgliem sinhronizēt no jūsu mezgla vai pat ļaujot citiem lietotājiem izveidot savienojumu ar jūsu mezglu, izmantojot savus makus.

Jāpiemin, ka Monero joprojām nodrošina izcilu privātumu, izmantojot attālo mezglu. Ja vēlaties palaist savu Monero mezglu, šeit ir viegli izpildāms ceļvedis, kā to izdarīt: 

  * [Palaidiet Monero Node](https://sethforprivacy.com/guides/run-a-monero-node/)

## Ko attālais mezgls var uzzināt par mani?

Izmantojot attālo mezglu, ir dažas galvenās informācijas daļas, kas tiek pakļautas attālajam mezglam, un daži galvenie veidi, kā mezgls var jums uzbrukt, neļaut jums veikt pārskaitījumus un ne tikai.

Pirmais, ko attālais mezgls var uzzināt par jums, ir jūsu publiskā IP adrese. Lai gan tas, cerams, tiks slēpts, izmantojot VPN vai Tor, attālais mezgls varētu saistīt jūsu publisko IP adresi ar pārskaitījumu, palīdzot viņiem sašaurināt, no kurienes veicat pārskaitījumus. Attālais mezgls var arī uzzināt pēdējo sinhronizēto maka bloku un izmantot to, lai mēģinātu izdarīt pamatotus minējumus par jums, piemēram, kad parasti lietojat Monero un kad pēdējo reizi iztērējāt Monero. Tas jo īpaši attiecas uz gadījumiem, kad vienmēr nākat no vienas IP adreses (piemēram, no mājām). Pēdējā galvenā lieta, ko attālais mezgls var uzzināt par jums, ir pamatinformācija par pārskaitījumiem, ko sūtāt, izmantojot to. Lai gan šie var būt visredzamākie dati, ko attālā mezgla operators iegūst par jums, ir svarīgi saprast, ka tos var izmantot, lai palīdzētu izsekot pārskaitījuma sūtītājam, apvienojot šo informāciju ar citiem ārpus ķēdes datiem. Tas var būt īpaši bīstami, ja attālo mezglu vada ļaunprātīga struktūra, blokķēdes analīzes uzņēmums vai nomācoša valsts.

Attālais mezgls var arī mēģināt radīt jums problēmas, slēpjot no jums blokus, liekot jūsu makam domāt, ka tas ir sinhronizēts, kad tā patiesībā nav. Tas var likt jums domāt, ka līdzekļi ir pazaudēti vai neļaut jums tērēt līdzekļus, līdz izveidojat savienojumu ar citu mezglu. Pēdējā galvenā lieta, ko attālais mezgls varētu darīt, ir nodrošināt jūsu maku ar manipulētu mānekļu sarakstu. Tas var izraisīt to, ka jūsu maciņam var neizdoties pilnībā izveidot pārskaitījumus (tā rezultātā jūs nevarēsiet tērēt līdzekļus), vai arī attālais mezgls var mēģināt nodrošināt mānekļus, par kuriem tas zina, ka tie ir iztērēti, lai samazinātu jūsu anonimitāti katrā pārskaitījumā.

## Kādas privātuma garantijas joprojām pastāv, izmantojot attālo mezglu?

Lai gan šis raksts jūs, iespējams, ir nedaudz nobiedējis, ir svarīgi saprast, ka Monero nodrošinātā konfidencialitāte ir lieliska pat tad, ja tiek izmantots attālais mezgls, un ievērojami pārspēj jebkuru citu kriptovalūtu, ja to lieto šādā veidā. Jūs joprojām iegūstat Monero nodrošināto spēcīgo privātumu ķēdē, jo attālais mezgls nekad nezina patieso ievadi (kādas monētas jūs tērējat), pārskaitījumā iztērēto Monero summu vai pārskaitījuma saņēmēja adresi. Arī ārējie novērotāji nevar redzēt patieso ievadīto informāciju, summu vai adreses (neatkarīgi no tā, kāda veida mezglu izvēlaties izmantot!), nodrošinot, ka ārpus attālā mezgla pat jūsu IP adresei, maka sinhronizācijas informācijai un pārskaitījumiem ir spēcīgas privātuma garantijas. 

Attālais mezgls arī nekad nevar piekļūt iepriekšējiem pārskaitījumiem, ko esat nosūtījis vai saņēmis, vai Monero summai, kas pašlaik atrodas jūsu makā, un zaudē visu jūsu pārskaitījumu redzamību brīdī, kad sākat izmantot citu mezglu. Attālajam mezglam nekad netiek nodrošinātas privātās atslēgas (ne tērēšanas, ne skatīšanas atslēgas), tāpēc jūsu maks paliek privāts, drošs un lietojams. Neatkarīgi no attālā mezgla jums arī nekad nedraud Monero pazaudēšana vai nozagšana, jo mezgls nevar rediģēt saņēmēja adresi, nekad nevar piekļūt jūsu maka privātajām atslēgām un nekādā veidā nevar konfiscēt jūsu Monero.

## Kā ar "vieglajiem makiem", piemēram, MyMonero?

Lai gan tēma ir nedaudz ārpus šī raksta darbības jomas, es tomēr vēlējos pievērsties unikālam Monero maka veidam — vieglajiem makiem. Nosaukums "vieglais maks" cēlies no tā, ka makam (tālrunī vai datorā) nav jāveic neviena blokķēdes sinhronizācija, padarot pieredzi ātrāku un plūstošāku.

Tomēr šādi maki pašlaik ir saistīti ar nopietnu privātuma kompromisu — jūsu maks nosūta privātā skata atslēgu uz jūsu izmantoto attālo serveri (piemēram, noklusējuma MyMonero), nodrošinot attālajam serverim pilnīgu redzamību par saņemtajiem līdzekļiem kopš maka izveides (un līdz brīdim, kad pārtraucat lietot šo maku vai sēklu). Tas krasi samazina konfidencialitāti, ko saņemat no mezgla operatora, un prasa atbilstošu piesardzību.

Par laimi, Monero kopiena strādā, lai uzlabotu programmatūru, kuru varat izmantot, lai palaistu pats savu vieglā maka serveri (LWS). Tas ļaus jums veikt ātru sinhronizāciju, neuzticoties trešajai pusei ar savām privātajām skata atslēgām, jo programmatūra, kurai jūsu maks nosūta privātā skata atslēgas, būs jūsu!

Plašāku informāciju par pielāgoto vieglā maka serveri skatiet tālāk esošajā Github repozitorijā:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Kā es varu uzzināt vairāk?

Ja jūs interesē un vēlaties labāk izprast Monero mezglus un izpētīt attālā mezgla izmantošanu vai sava palaišanu, skatiet tālāk esošās saites, lai atrastu lieliskas vietas, kur sākt.

  * [Monero World — saraksts ar kopienas pārvaldītiem attāliem mezgliem, ko var izmantot](https://moneroworld.com/#nodes)
  * [Monero mezgli, kurus vada Seth For Privacy, šī raksta autors](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail — attālo mezglu saraksts ar bieži pārbaudītu statusu< /a>](https://monero.fail/)
  * [Kā izveidot savienojumu uz attālo mezglu GUI makā](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia — Attālais Mezgls](https://www.getmonero.org/resources/moneropedia/remote-node.html)

Lasīt tālāk

  * [Kā Monero unikāli nodrošina aprites ekonomiku](/knowledge/monero-circular-economies/)

  * [Monero gredzenveida paraksti salīdzinājumā ar CoinJoin kā Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Kāpēc (un kā!) jums vajadzētu turēt savas atslēgas](/knowledge/hold-your-keys/)

  * [Iesaiste Monero](/knowledge/contributing-to-monero/)

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

  * [Žurnāls Wired kļūdās par Monero. Lūk, kāpēc](/knowledge/wired-article-debunked/)

  * [15 populārākie Monero mīti un bažas atspēkotas](/knowledge/monero-myths-debunked/)

  * [Kā Dandelion++ saglabā Monero pārskaitījumu izcelsmi privātu](/knowledge/monero-dandelion/)

  * [Kāpēc Monero ir atvērtā pirmkoda un decentralizēts](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero mainošana: ar ko RandomX ir tik īpašs](/knowledge/monero-mining-randomx/)

  * [Kāpēc Monero ir labāks par Dash, Zcash, Zcoin (pat ar Lelantus), Grin un Bitcoin mikseriem, piemēram, Wasabi (atjaunināts 2020. gada maijā)](/knowledge/why-monero-is-better/)