---
title: "Kā gredzenveida paraksti apslēpj Monero izvadi"
slug: "ring-signatures"
date: "2020-09-08"
image: "/images/rings.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero ir plaši pazīstams visā kriptovalūtā kā privātuma monētu karalis. Lai gan visi zina, ka Monero piedāvā labu privātumu, ne tik daudzi saprot, kā privātums darbojas.

Daudzās citās privātuma monētās tiek publicētas salīdzināšanas diagrammu infografikas, kurās ir norādīti katras monētas konfidencialitātes tehnoloģijas nosaukumi, un vairumā gadījumu Monero tehnoloģija tiek apzīmēta kā RingCT, taču tā ir tikai daļēji taisnība. Monero faktiski ir trīs veidu pieeja privātumam. Viena tehnoloģija, lai paslēptu pārskaitījuma saņēmēju, viena, lai paslēptu nosūtīto summu, un viena, lai paslēptu izmantoto izvadi. Tās ir attiecīgi slepenās adreses, RingCT un gredzenveida paraksti.

Šī trīsvirzienu pieeja nozīmē, ka, ja viena no tehnoloģijām tiek sabojāta, pārējām ne vienmēr ir tāds pats liktenis. Gredzenveida paraksti ir vājākais posms privātuma shēmā; vārds vājš šeit nozīmē visjutīgāko pret heiristiskiem uzbrukumiem. Atvēlēsim kādu laiku, lai tos izpētītu, vai ne?

Kā minēts iepriekš, gredzenveida parakstu mērķis ir aizēnot pārskaitījumā izmantoto izvadi. Ja kriptovalūtas “ievades/izvades” terminoloģija jūs mulsina, neuztraucieties. Patiesībā tas nav tik sarežģīti. Kad dzirdat vārdu "izvade", vienkārši domājiet - čeks. Viena no tām lietām, kas vairs nav tik izplatīta un ar ko cilvēki mēdz norēķināties. Tāpat kā čeku, to var izrakstīt jebkurā summā — USD 10, USD 32,50 utt., un to var apmainīt starp darījuma pusēm. Kriptovalūtām šīs funkcijas pilda izvades.

Kad kāds jums maksā 10 Monero, jūs saņemat 10 XMR izvadi. Šai izvadei ir vērtība (10), un tā tiek ņemta no sūtītāja maka, tāpat, kad maksājat par pakalpojumu, banknote atstāj jūsu fizisko maku un tiek nodota personai, no kuras iepērkaties.

Izvade tiek paslēpta, izveidojot mānekļu izvadu gredzenu (no turienes arī nosaukums). Taču šie mānekļi nav “viltus” izvades. Tās ir reālas pagātnes blokķēdes izvades, kurām nav nekāda sakara ar pašreizējo pārskaitījumu, taču ārējam novērotājam katra no šīm izvadēm var izskatīties tikpat ticama kā reālā. Mānekļu izvadu komplekta lielums, pieskaitot īsto, tiek saukts par gredzena izmēru, un pašlaik Monero tas ir vienpadsmit. Tātad ir desmit mānekļu izvadi un viens īsts.

Kāpēc mēs vienkārši nepalielinām šo skaitu līdz 100 vai pat 1000? Jo vairāk, jo labāk, vai ne? No privātuma viedokļa jā, taču ir jāņem vērā arī citas lietas. Atgriezīsimies pie fiziska piemēra, lai redzētu, ko es domāju. Ja vēlaties paslēpt vienu no savām dolāra banknotēm starp desmit mānekļiem, jums makā vajadzētu nēsāt apmēram vienpadsmit dolārus par katru dolāru, ko vēlaties tērēt. Viens īsts dolārs un desmit viltoti. Tas jau kļūst diezgan apgrūtinoši, ja vēlaties iztērēt pat dažus dolārus. Tagad iedomājieties, ka mēs palielinām mānekļa summu līdz 1000. Par katru vienu dolāru, kuru vēlaties tērēt, jums līdzi jāņem aptuveni 1001 dolārs. Lai iegādātos vienu šokolādes batoniņu, jums būs jānēsā līdzi portfelis! Ir svarīgi atzīmēt, ka gredzenveida paraksti nedarbojas gluži šādā veidā, piemēram, paši mānekļi nav paraksta sastāvdaļa, bet tikai atsauces uz tiem. Taču mēs ceram, ka šī līdzība var nedaudz noderēt, lai attēlotu pamatjēdzienus.< /p>

Mānekļi blokķēdē darbojas līdzīgi. Katrs pievienotais māneklis palielina pārskaitījuma laiku un apstiprināšanas izmaksas. Katram mezglam ir jālejupielādē viss gredzenveida paraksts katram pārskaitījumam, un katrs paraksts satur reālo izvadi, kā arī mānekļus. Ne tikai tas, bet arī matemātiski jāpārbauda, vai vismaz viens no šiem rezultātiem ir reāls, un arī matemātiskās pārbaudes laiks palielinās ar katru mānekli. Tas nozīmē, ka mums ir jāatrod laimīgs vidusceļš, kur gredzena izmērs ir pietiekami liels, lai pietiekami aizēnotu reālo rezultātu, pat pret daudziem heiristiskiem uzbrukumiem, bet pietiekami mazs, lai neizraisītu masveida blokķēdes palielināšanos. Nepietiek ar patvaļīga skaitļa izvēli vai vienkārši palielināt gredzena izmēru, kad parakstu samazina (piemēram, izmantojot CLSAG). Monero kopiena vēlas konkrētus, matemātiskus pierādījumus par to, kurš gredzena izmērs piedāvā vislabākos kompromisus. Ja skaitlis ir pārāk mazs, privātums nebūs pietiekami spēcīgs pret heiristiskiem uzbrukumiem. Pārāk liels, un mēs, iespējams, gūstam tikai nelielu labumu no privātuma puses un nevajadzīgi ciešam saistībā ar paplašināšanu.

Pēdējais, kas jāpiemin. Dažā Monero literatūrā ir vienkāršots un teikts, ka gredzenveida paraksti slēpj sūtītāju, taču tā nav pilnīgi taisnība, un atšķirība nav tikai pedantiska. Atšķirība starp sūtītāju (cilvēku) un izvadi (čeku) ir liela, ja runa ir par privātuma saglabāšanu. Lai gan izvade var būt saistīta ar sūtītāju, pati izvade nav vienāda ar sūtītāju. Tāpēc pat tad, ja gredzenveida paraksts tiktu salauzts, tas ne vienmēr ir saistīts ar personas identitāti, un gan summa, gan saņēmējs joprojām tiek slēpti, tādējādi samazinot visu pušu privātumam nodarīto kaitējumu.

Tas nenozīmē, ka bojāts gredzenveida paraksts ir nenozīmīgs. Jebkuri nopludinātie metadati ir slikti, un tie var atklāt vairāk informācijas, nekā mēs domājam, it īpaši, ja tos izmanto kopā ar citiem metadatiem. Tāpēc mēs darām visu iespējamo, lai nodrošinātu, ka izvēlētais gredzena lielums ir akadēmiski pamatots, līdz minimumam tiek samazināta citu metadatu noplūde un lietotāja pieredzes noklusējuma darbības tiek veiktas pēc iespējas labāk.

Bet, ja jūs joprojām uztrauc salauzta paraksta iespējamība, tad pie apvāršņa ir dažas neticamas ziņas. Nākamās paaudzes privātuma protokoliem, pie kuriem tiek strādāts, piemēram, Triptych, Arcturus un Lelantus, ir patiešām glītas iespējas. Šajos protokolos, palielinoties gredzena izmēram, izmērs mainās logaritmiski, nevis lineāri. Tas nozīmē, ka mēs varam ievietot 100 mānekļus, bet izmantotā vieta ir tuvāk gredzena izmēram 10 vecajā tehnoloģijā. Tā ir liela atšķirība, un tā ievērojami uzlabos privātumu kopumā.

Kaķa un peles spēlē, kas ir privātums, Monero nepārtraukti ievieš jauninājumus, lai paliktu priekšā un nodrošinātu vislabāko praktisko privātumu visiem.

Mānekļi blokķēdē darbojas līdzīgi. Katrs pievienotais māneklis palielina pārskaitījuma laiku un apstiprināšanas izmaksas. Katram mezglam ir jālejupielādē viss gredzenveida paraksts katram pārskaitījumam, un katrs paraksts satur reālo izvadi, kā arī mānekļus. Ne tikai tas, bet arī matemātiski jāpārbauda, vai vismaz viens no šiem rezultātiem ir reāls, un arī matemātiskās pārbaudes laiks palielinās ar katru mānekli. Tas nozīmē, ka mums ir jāatrod laimīgs vidusceļš, kur gredzena izmērs ir pietiekami liels, lai pietiekami aizēnotu reālo rezultātu, pat pret daudziem heiristiskiem uzbrukumiem, bet pietiekami mazs, lai neizraisītu masveida blokķēdes palielināšanos. Nepietiek ar patvaļīga skaitļa izvēli vai vienkārši palielināt gredzena izmēru, kad parakstu samazina (piemēram, izmantojot CLSAG). Monero kopiena vēlas konkrētus, matemātiskus pierādījumus par to, kurš gredzena izmērs piedāvā vislabākos kompromisus. Ja skaitlis ir pārāk mazs, privātums nebūs pietiekami spēcīgs pret heiristiskiem uzbrukumiem. Pārāk liels, un mēs, iespējams, gūstam tikai nelielu labumu no privātuma puses un nevajadzīgi ciešam saistībā ar paplašināšanu.

Pēdējais, kas jāpiemin. Dažā Monero literatūrā ir vienkāršots un teikts, ka gredzenveida paraksti slēpj sūtītāju, taču tā nav pilnīgi taisnība, un atšķirība nav tikai pedantiska. Atšķirība starp sūtītāju (cilvēku) un izvadi (čeku) ir liela, ja runa ir par privātuma saglabāšanu. Lai gan izvade var būt saistīta ar sūtītāju, pati izvade nav vienāda ar sūtītāju. Tāpēc pat tad, ja gredzenveida paraksts tiktu salauzts, tas ne vienmēr ir saistīts ar personas identitāti, un gan summa, gan saņēmējs joprojām tiek slēpti, tādējādi samazinot visu pušu privātumam nodarīto kaitējumu.

Tas nenozīmē, ka bojāts gredzenveida paraksts ir nenozīmīgs. Jebkuri nopludinātie metadati ir slikti, un tie var atklāt vairāk informācijas, nekā mēs domājam, it īpaši, ja tos izmanto kopā ar citiem metadatiem. Tāpēc mēs darām visu iespējamo, lai nodrošinātu, ka izvēlētais gredzena lielums ir akadēmiski pamatots, līdz minimumam tiek samazināta citu metadatu noplūde un lietotāja pieredzes noklusējuma darbības tiek veiktas pēc iespējas labāk.

Bet, ja jūs joprojām uztrauc salauzta paraksta iespējamība, tad pie apvāršņa ir dažas neticamas ziņas. Nākamās paaudzes privātuma protokoliem, pie kuriem tiek strādāts, piemēram, Triptych, Arcturus un Lelantus, ir patiešām glītas iespējas. Šajos protokolos, palielinoties gredzena izmēram, izmērs mainās logaritmiski, nevis lineāri. Tas nozīmē, ka mēs varam ievietot 100 mānekļus, bet izmantotā vieta ir tuvāk gredzena izmēram 10 vecajā tehnoloģijā. Tā ir liela atšķirība, un tā ievērojami uzlabos privātumu kopumā.

Kaķa un peles spēlē, kas ir privātums, Monero nepārtraukti ievieš jauninājumus, lai paliktu priekšā un nodrošinātu vislabāko praktisko privātumu visiem.

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