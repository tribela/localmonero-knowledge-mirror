---
title: "Seraphis: ko tas darīs Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: modulāra dizaina jauninājums Monero pārskaitījumiem

## Seraphis: modulāra dizaina jauninājums Monero pārskaitījumiem

Šajā rakstā ir aprakstīts [Seraphis](https://github.com/UkoeHB/Seraphis) — pārskaitījumu protokolu struktūru un abstrakciju kopums, ko Monero ekosistēmai izstrādājis pseidonīms pētniecības līdzstrādnieks [`koe`](https://github.com/UkoeHB), un ar nepārtrauktu drošības analīzi pseidonīms līdzautors [`coinstudent2048`](https://github.com/coinstudent2048).  
Mēs veicam dažus vienkāršojumus un izlaižam noteiktas tehniskas detaļas skaidrības labad; šī iemesla dēļ un tāpēc, ka Seraphis dizains joprojām tiek izstrādāts, ieinteresētiem lasītājiem ir jāmeklē Seraphis dokumentācija, lai iegūtu jaunāko informāciju.

## Pārskaitījumi Monero

## Pārskaitījumi Monero

Protokoli kā Bitcoin, Monero un citi, balstās uz tā saukto "izvades modeli", kur _izvade_ ir vērtības, ko var pārsūtīt, attēlojums.  
Pārskaitījumos tiek patērēta viena vai vairākas izvades, kuras kontrolē sūtītājs, un tiek ģenerētas jaunas izvades, kas vērstas uz adresātiem (vai atpakaļ sūtītājam kā maiņa); pārskaitījumam ir jābūt līdzsvarotam ar to, ka patērētajām izvadēm ir jāietver kopējā vērtība, kas ir tieši vienāda ar jauno izvadu vērtību (plus tīkla noteiktā maksa).  
Daudzos protokolos, piemēram, Bitcoin, izvadē esošā vērtība ir rakstīta skaidri, tāpat kā adresāts.  
Turklāt, aplūkojot blokķēdi, ir viegli redzēt, vai un kad izvade ir iztērēta (tas ir, vai tā ir iztērēta vēlākā pārskaitījumā un kurā pārskaitījumā to iztērēja).

Turpretim protokoli, piemēram, Monero, ievieš atšķirīgu dizainu:

  * Izvades vērtības ir paslēptas un nav redzamas blokķēdē
  * Adresātu adreses tiek paslēptas, izmantojot vienreizēju adresācijas protokolu
  * Tas, vai izvade ir iztērēta, tiek apslēpts ar neskaidru parakstu izmantošanu

Rezultāts ir tāds, ka, ja nav ārējas informācijas, ir grūti noteikt, vai dotā izvade ir iztērēta, kāda ir tās vērtība un kas ir tās saņēmējs.

Pašreizējais Monero pārskaitījumu protokols tiek saukts par _RingCT_ , un, lai sasniegtu šos mērķus, tiek izmantoti vairāki kriptogrāfiskas uzbūves bloki.

  * _Saistības_ slēpj summas matemātiski saderīgā veidā
  * _Diapazona pierādījumi_ novērš pārplūdi, kas varētu radīt inflāciju
  * _Saistāmie gredzenveida paraksti_ nodrošina parakstītāju neskaidrību un novērš dubultas tērēšanas mēģinājumus
  * _Saistību kompensācijas_ apliecina, ka pārskaitījumi līdzsvarojas

Šie bloki ir rūpīgi savīti, lai izveidotu RingCT protokolu.

Noderīga RingCT protokola īpašība ir tāda, ka dažus blokus var mainīt vai uzlabot tā, lai kopējais dizains un īpašības tiktu saglabātas neskartas, taču tas var nodrošināt efektivitātes vai drošības uzlabojumus. Faktiski šāda veida jauninājumi ir notikuši (vai tiek plānoti) vairākas reizes Monero vēsturē. Diapazona pierādījumi sākotnējā RingCT protokolā bija apjomīgi un lēni; vēlāk tie tika atjaunināti uz konstrukciju ar nosaukumu [Bulletproofs](https://eprint.iacr.org/2017/1066), kas padarīja pārskaitījumus mazākus un ātrākus ar labāku drošības analīzi, un ir plānots tos atjaunināt uz jaunāku konstrukciju ar nosaukumu [Bulletproofs+](https://eprint.iacr.org/2020/735), lai nodrošinātu vēl lielākus efektivitātes ieguvumus. 

Līdzīgs process tika veikts ar saistāmo gredzenveida parakstu daļu. Sākotnējā protokolā tika izmantota konstrukcija ar nosaukumu [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34). Vēlāk tas tika atjaunināts uz jaunāku konstrukciju ar nosaukumu [CLSAG](https://eprint.iacr.org/2019/654), kas ir ātrāka, nodrošina mazākus pārskaitījumus un labāku drošības analīzi. Tika ierosināta vēl jaunāka saistāmo gredzenveida parakstu konstrukcija, kuras pamatā ir [Triptych](https://eprint.iacr.org/2020/018), taču tā netika izvēlēta ieviešanai, jo tā ietekmēja multiparakstu darbības.

## Seraphis

## Seraphis

Seraphis ved šo ideju soli tālāk.  
Tā vietā, lai atjauninātu atsevišķus esošā RingCT protokola blokus, tiek ieviests cits protokols, kas var izmantot dažādu elementu priekšrocības un piedāvāt uzlabotu funkcionalitāti.

## Būvēšanas bloki

## Būvēšanas bloki

Seraphis izmanto citu kriptogrāfijas bloku komplektu, lai sasniegtu savus paredzētos mērķus.

  * _Saistības_ joprojām slēpj summas
  * _Diapazona pierādījumi_ joprojām novērš pārplūdi un inflāciju
  * _Dalības pierādījumi_ nodrošina parakstītāju neskaidrību
  * _Saistību kompensācijas_ joprojām apstiprina līdzsvaru
  * _Pierādījumu autorizācija_ novērš dubultas tērēšanas mēģinājumus

Ņemiet vērā izmaiņas šeit: saistāmie gredzenveida paraksti tiek aizstāti ar dalības apliecinājumu un pilnvarojošo pierādījumu kombināciju. Aptuveni runājot, dalības pierādījumi apliecina, ka iztērētā izvade ir daļa no lielākas kopas, līdzīgi kā tas notiek RingCT. Bet atšķirībā no RingCT dalības pierādījumos vispār nav ietverts saistīšanas tags! Autorizācijas pierādījumi apliecina, ka saistīšanas tags ir derīgs un tiek izmantoti galīgā pārskaitījuma parakstīšanai.

Tā kā RingCT pievieno saistīšanas tagu neskaidrā parakstā, parakstīšanas (un vairāku parakstu) darbības ir daudz skaitļošanas ziņā ietilpīgākas, un kļūst grūtāk izveidot citu ar tagu saistītu funkcionalitāti. Taču Seraphis dalības apliecinājumu izveidi var droši deleģēt no ļoti uzticamām ierīcēm (kurām var būt ierobežota skaitļošanas jauda, piemēram, aparatūras makam) uz mazāk uzticamu ierīci, un parakstīšanas (un vairāku parakstu) darbības ir daudz vienkāršākas, izmantojot daudz vienkāršāku autorizācijas pierādījumu. 

Par laimi, daži Seraphis nepieciešamie elementi jau pastāv citur, un tie nav jāprojektē no nulles. Gan Bulletproofs, gan Bulletproofs+ konstrukcijas var izmantot kā diapazona pierādījumus. Pierādījumu autorizācijai var izmantot modifikācijas Schnorr tipa pierādīšanas sistēmās. Un efektīvu [pierādīšanas sistēmu](https://eprint.iacr.org/2015/643), kas jau tika izmantota kā pamats Triptych, [Lelantus](https://eprint.iacr.org/2019/373) un [Spark](https://eprint.iacr.org/2021/1173)*, var modificēt dalības pierādījumiem. 

* Cypher Stack saņem finansējumu Spark izstrādei.

## Adresēšana

## Adresēšana

Diemžēl pašlaik izmantotās Monero adreses nav saderīgas ar Seraphis. Ja Seraphis tiktu ieviests, lietotājiem būs jāģenerē jaunas adreses no sava maka atslēgām, lai saņemtu Monero. Tomēr šīs ekosistēmas izmaksas ir saistītas ar daudzām priekšrocībām.

Papildus iepriekš apspriestajām strukturālajām priekšrocībām Seraphis dizains ir piemērots daudzām dažādām adreses konstruēšanas iespējām, no kurām katra ir saistīta ar kompromisiem. Lai gan Seraphis izmantojamā galīgā adreses konstrukcija [ vēl tiek izlemta](https://github.com/monero-project/research-lab/issues/92) (vienu shēmu, kurai tiek pievērsta liela uzmanība, sauc par [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), mēs varam aprakstīt dažas kopīgas un noderīgas funkcijas.

Iespējams, jūs zināt, ka Monero adreses piedāvā _skata atslēgas_ funkcionalitāti, kur ierīcei vai trešajai pusei varat nodrošināt skata atslēgu un ļaut tai jūsu vārdā skatīties ienākošos izvadus, nenododot tēriņu atslēgu. Tas ir noderīgi makiem, kas var tikt atjaunināti, vienlaikus saglabājot tēriņu atslēgu droši noglabātu. Tas ir noderīgi arī gadījumos, kad vēlaties saņemt ārēja novērotāja piekļuvi, piemēram, publiskai labdarības organizācijai, kas piedāvā caurspīdīgumu, vai uzņēmumam ar grāmatvedības nodaļu.

Monero skata atslēgu negatīvie aspekti ir tādi, ka tās nenodrošina pilnīgu vai smalku piekļuvi skatam. Nav iespējams droši noteikt, kad maks tērē līdzekļus, tāpēc ir grūti pareizi aprēķināt maka atlikumu, ja nav pieejama tēriņu atslēga. Pašlaik nav arī iespējams noteikt ienākošās izvades, neapgūstot arī šajās izvadēs ietvertās vērtības (tas nozīmē, ka jebkura trešā puse, kas ir atbildīga par ienākošo izvadu atrašanu, uzzinās, cik daudz Monero jūs iegūstat).

Seraphis adresācijas konstrukcijas var to atrisināt. Izmantojot Seraphis, jūsu adrese ir aprīkota ar dažādām atslēgām, kuras var veikt dažādas darbības: 

  * Sekot ienākošajām izvadēm, bet paslēpt to vērtību
  * Skatīties ienākošās izvades, bet parādīt to vērtību
  * Skatīties izejošās izvades
  * Palīdzēt ģenerēt pārskaitījumus, bet neparakstīt tos
  * Ģenerēt jaunas adreses (noder mazumtirgotājiem vai apmaiņai ar daudziem klientiem)

Kā adreses īpašnieks jūs varat izlemt, cik un kādas pilnvaras deleģējat citām ierīcēm vai trešajām pusēm.

## Kopskats

## Kopskats

Seraphis ir būtiskas izmaiņas Monero ekosistēmā. Lai gan tas ietver adrešu un pārskaitījumu veidošanas bloku modifikācijas, tā dizains piedāvā elastību un noderīgu funkcionalitāti, kas nav iespējama ar mūsdienu RingCT protokolu. Lai gan liela daļa dizaina ir pabeigta un tiek izstrādāta [ieviešanā](https://github.com/UkoeHB/monero/tree/seraphis_lib), adresu izveidojums un drošības analīze turpinās. Seraphis piedāvā lielisku iespēju virzīt Monero ekosistēmu uz priekšu!

Lasīt tālāk

  * [Kā Monero unikāli nodrošina aprites ekonomiku](/knowledge/monero-circular-economies)/

  * [Monero gredzenveida paraksti salīdzinājumā ar CoinJoin kā Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Kāpēc (un kā!) jums vajadzētu turēt savas atslēgas](/knowledge/hold-your-keys)/

  * [Iesaiste Monero](/knowledge/contributing-to-monero)/

  * [Kā attālie mezgli ietekmē Monero privātumu](/knowledge/remote-nodes-privacy)/

  * [Kā Monero izmanto hard-forks tīkla uzlabošanai](/knowledge/network-upgrades)/

  * [Skata tagi: kā viens baits samazinās Monero maka sinhronizācijas laiku par 40%+](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool un tā loma Monero mainošanas decentralizācijā](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Vai Bitcoin konvertēšana uz Monero ir tikpat privāta kā Monero pirkšana tieši?](/knowledge/most-private-way-to-buy-monero)/

  * [Kāpēc Monero atšķirībā no Zcash izmanto bezuzticības iestatījumu](/knowledge/monero-trustless-setup)/

  * [Kāpēc Monero ir labāks vērtības glabātājs nekā Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Kā Monero var pārvarēt Bitcoin tīkla efektus](/knowledge/network-effect)/

  * [Kāpēc Monero ir viskritiskāk domājošā kopiena](/knowledge/critical-thinking)/

  * [Krāpniecība, kam jāpievērš uzmanība, lietojot Monero](/knowledge/monero-scams)/

  * [Kā Monero darbosies atomiskā apmaiņa](/knowledge/monero-atomic-swaps)/

  * [Kas jāzina ikvienam Monero lietotājam, kad runa ir par tīklu veidošanu](/knowledge/monero-networking)/

  * [Kā RingCT slēpj Monero pārskaitījumu summas](/knowledge/monero-ringct)/

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