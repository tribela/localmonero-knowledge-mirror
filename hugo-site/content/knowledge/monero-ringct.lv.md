---
title: "Kā RingCT slēpj Monero pārskaitījumu summas"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero privātums nav atkarīgs no viena atsevišķa mehānisma, kas kļūdas gadījumā atklātu visu darījumu kopumu, bet gan trīs dažādām tehnoloģijām, kas darbojas kopā, lai nodrošinātu visaptverošu privātumu, vienlaikus kompensējot citu daļu vājās vietas. Šī trīs daļu pieeja sastāv no [gredzenveida parakstiem](/knowledge/ring-signatures), RingCT un [slēptajām adresēm](/knowledge/monero-stealth-addresses). Šīs trīs tehnoloģijas attiecīgi slēpj reālo izvadi (sūtītāju), daudzumu un saņēmēju. Šeit runāsim par RingCT.

RingCT ir neapšaubāmi vistehniskākais no trim, un to var būt grūti saprast. Tāpēc mēs neapspriedīsim, kā tas precīzi darbojas, bet gan parādīsim, kā ir iespējams nezināt summu un tomēr apstiprināt lietas par to. Un neuztraucieties, mēs kā vienmēr izmantosim daudz piemēru.

Vispirms izpētīsim, kāpēc ir svarīgi kaut ko pārbaudīt par summām. Kāpēc mēs nevaram tās turēt pilnībā noslēpumā? Atbilde ir tāda, ka ir gudri veidi, kā cilvēki var radīt naudu no gaisa, ja viņiem tiek dota iespēja. Kā kaut kas līdzīgs varētu darboties? Apskatīsim piemēru.

Ja vēlaties iegādāties preci no sava drauga un viņš par to vēlas desmit dolārus, tad jūs sāksiet ar desmit dolāriem, bet viņš sāks ar nulli. Pēc tam, kad viņam iedosiet desmit dolārus, viņam būs desmit dolāri, bet jums nulle. Jūs sākāt ar desmit, un tagad viņam ir desmit. Šajā darījumā nauda netika izveidota vai iznīcināta.

Izmantojot kriptovalūtas, gudrs indivīds var atdot desmit dolārus par preci, un tā vietā, lai saņemtu nulles dolāru maiņās, viņi var saņemt divus dolārus atpakaļ. 0 un 10 vietā, kas rada 10 un 0 (vai 10=10), tagad 0 un 10 noved pie 10 un 2 (vai 10=12). Divi Monero tikko tika izveidoti no zila gaisa. Varat iedomāties, ka, ja indivīds to darītu ar sevi vairākas reizes, viņš īsā laikā varētu uzkrāt milzīgu bagātību.

Izmantojot Bitcoin un citus, to būtu viegli redzēt. Apskatiet darījumos ievadītos datus un izejošos rezultātus un pārliecinieties, ka nosūtītais ir vienāds ar saņemto. Ja šīs summas ir šifrētas un nav redzamas, lietotājs nevar pārbaudīt, vai nosūtītais un saņemtais ir vienāds.

Mēģinot palielināt Bitcoin privātumu, Gregorijs Maksvels izveidoja Konfidenciālus pārskaitījumus (CT) - jaunu tehnoloģiju, kas ļautu šifrēt summas, vienlaikus pierādot, ka šajā procesā nekas netika izveidots vai iznīcināts. Tāpat kā lielākā daļa privātuma tehnoloģiju, tā neiekļuva Bitcoin, bet Monero priecājās to pieņemt. Bija tikai viena problēma. Jau ieviestā gredzenveida parakstu tehnoloģija nebija savienojama ar piedāvāto ideju. Tad viens no toreizējiem MRL pētniekiem Shen Noether pārveidoja CT par RingCT — CT versiju, kas bija saderīga ar gredzenveida parakstiem.

Vēlreiz jāatzīmē, ka tas ir tehniski niansēti, un to būtu grūti izskaidrot ievadrakstā. Kriptogrāfijas entuziastam, kuram tas vienkārši ir jāzina, internetā ir daudz padziļinātu rakstu par CT iekšējo darbību. Mums pārējiem šis raksts parādīs, kā varētu slēpt summas, bet tomēr pierādīt, ka nekas netika izveidots vai iznīcināts.

Pieņemsim, ka Alise grib nosūtīt Bobam naudu. Alise nosūtīs 10 XMR Bobam, kurš saņems 10 XMR. 10=10, tātad viss ir pareizi. Bet Alise nevēlas, lai kāds zinātu, cik daudz viņa sūta. Tāpēc viņa un Bobs izveido kopīgu noslēpumu. Būtībā tas ir skaitlis, ko zina tikai viņi abi. Pieņemsim, ka šis skaitlis ir 22. Tagad Alise reizina 10 (to, ko viņa patiešām sūta) ar 22, lai iegūtu 220. Šis ir skaitlis, ko viņa kopīgo ar tīklu.

Maineri nezina slepeno skaitli. Ja viņi to zinātu, viņi varētu dalīt parādīto skaitli ar slepeno skaitli un saņemt reālo nosūtīto summu. Bet, tā kā viņi to nezina, viņi nevar. Viņi redz, ka Bobs saņems 220. 220 nosūtīti. 220 saņemti. 220 = 220. Tādā veidā tīkls var pārbaudīt, vai Monero nav izveidots vai iznīcināts, nezinot patieso summu, ko Alise nosūtīja Bobam.

Tā kā Bobs zina koplietoto slepeno skaitli, kad viņš saņem naudu, viņš vienkārši dala ar 22, lai iegūtu patieso summu, ko Alise nosūtīja, — 10. Alise un Bobs zina, cik daudz tika nosūtīts un cik saņemts. visiem pārējiem tiek atklāts nepatiess skaitlis.

Vēlreiz atkārtoju, ka tas nav īstais veids, kā CT darbojas, taču tas sniedz priekšstatu par to, kā kaut kas līdzīgs varētu būt iespējams. Patiesais veids ietver tādas lietas kā Pedersena saistības, divas nosūtītās summas (viena šifrēta summa saņēmējam un viena saistību summa tīklam) un… jā, jau tagad ir viegli saprast, kā tajā visā var pazust.

Tomēr viena lieta, kas jāņem vērā, ir tāda, ka, lai gan RingCT slēpj summu, ko darījumā veic divas puses, tas neslēpj divas citas skaitļu kopas.

Pirmais ir monētu bāzes pārskaitījumi. Ja šis termins jums nav pazīstams, tas būtībā nozīmē atlīdzību, ko maineri saņem par nākamā bloka atrašanu. Šis skaitlis nav slēpts. Ikviens var redzēt, cik daudz protokols ir piešķīris maineriem par viņu pakalpojumu. Tādā veidā pašreizējo Monero daudzumu var uzzināt, saskaitot visus monētu bāzes pārskaitījumus. To summa būs vienāda ar pašreizējo Monero apgrozībā.

Otrais skaitlis, kas nav slēpts, ir maksa, ko maksā maineriem, kad lietotājs nosūta pārskaitījumu. Maksai ir jābūt skaidrai, lai maineri varētu zināt, kam piešķirt prioritāti. Tomēr tas ir veids, kā lietotāji var kaitēt viņu pašu privātumam, jo, ja kāds izmanto unikālu mainera maksu katru reizi, kad nosūta pārskaitījumu (piemēram, 0,12345), viņa pārskaitījumus var saistīt.

Izņemot šos gadījumus, RingCT ir slēpis Monero summas kopš 2017. gada, un mūsu kopīgā privātuma aizsardzība tā dēļ ir vēl spēcīgāka.

Lasīt tālāk

  * [Kā Monero unikāli nodrošina aprites ekonomiku](/knowledge/monero-circular-economies)/

  * [Monero gredzenveida paraksti salīdzinājumā ar CoinJoin kā Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Kāpēc (un kā!) jums vajadzētu turēt savas atslēgas](/knowledge/hold-your-keys)/

  * [Iesaiste Monero](/knowledge/contributing-to-monero)/

  * [Kā attālie mezgli ietekmē Monero privātumu](/knowledge/remote-nodes-privacy)/

  * [Kā Monero izmanto hard-forks tīkla uzlabošanai](/knowledge/network-upgrades)/

  * [Skata tagi: kā viens baits samazinās Monero maka sinhronizācijas laiku par 40%+](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool un tā loma Monero mainošanas decentralizācijā](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: ko tas darīs Monero](/knowledge/seraphis-for-monero)/

  * [Vai Bitcoin konvertēšana uz Monero ir tikpat privāta kā Monero pirkšana tieši?](/knowledge/most-private-way-to-buy-monero)/

  * [Kāpēc Monero atšķirībā no Zcash izmanto bezuzticības iestatījumu](/knowledge/monero-trustless-setup)/

  * [Kāpēc Monero ir labāks vērtības glabātājs nekā Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Kā Monero var pārvarēt Bitcoin tīkla efektus](/knowledge/network-effect)/

  * [Kāpēc Monero ir viskritiskāk domājošā kopiena](/knowledge/critical-thinking)/

  * [Krāpniecība, kam jāpievērš uzmanība, lietojot Monero](/knowledge/monero-scams)/

  * [Kā Monero darbosies atomiskā apmaiņa](/knowledge/monero-atomic-swaps)/

  * [Kas jāzina ikvienam Monero lietotājam, kad runa ir par tīklu veidošanu](/knowledge/monero-networking)/

  * [Kā Monero slepenās adreses aizsargā jūsu identitāti](/knowledge/monero-stealth-addresses)/

  * [Kā Monero apakšadreses novērš identitātes saistīšanu](/knowledge/monero-subaddresses)/

  * [Monero izvades tuvplānā](/knowledge/monero-outputs)/

  * [Monero labākā prakse iesācējiem](/knowledge/monero-best-practices)/

  * [Kā gredzenveida paraksti apslēpj Monero izvadi](/knowledge/ring-signatures)/

  * [Kā Monero atrisināja bloka izmēra problēmu, kas vajā Bitcoin](/knowledge/dynamic-block-size)/

  * [Kā CLSAG uzlabos Monero efektivitāti](/knowledge/what-is-clsag)/

  * [Kāpēc Monero ir astes emisija](/knowledge/monero-tail-emission)/

  * [Īsa Monero vēsture](/knowledge/monero-history)/

  * [Žurnāls Wired kļūdās par Monero. Lūk, kāpēc](/knowledge/wired-article-debunked)/

  * [15 populārākie Monero mīti un bažas atspēkotas](/knowledge/monero-myths-debunked)/

  * [Kā Dandelion++ saglabā Monero pārskaitījumu izcelsmi privātu](/knowledge/monero-dandelion)/

  * [Kāpēc Monero ir atvērtā pirmkoda un decentralizēts](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero mainošana: ar ko RandomX ir tik īpašs](/knowledge/monero-mining-randomx)/

  * [Kāpēc Monero ir labāks par Dash, Zcash, Zcoin (pat ar Lelantus), Grin un Bitcoin mikseriem, piemēram, Wasabi (atjaunināts 2020. gada maijā)](/knowledge/why-monero-is-better)/

Lasīt tālāk