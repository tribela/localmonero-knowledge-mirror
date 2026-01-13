---
title: "Monero gredzenveida paraksti salīdzinājumā ar CoinJoin kā Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Bitcoin privātuma rīkiem gūstot lielāku uzmanību un pielietojumu, tie ir pakļauti stingrākai kontrolei. Šīs kontroles rezultātā Bitcoin privātuma rīks Wasabi Wallet [nesen paziņoja](https://twitter.com/wasabiwallet/status/1503091503207432193), ka viņi sāks cenzēt un noraidīt maisījumos ienākošās ievades, kuras viņi uzskata par nelikumīgām vai pretrunā viņu pakalpojumu sniegšanas noteikumiem, un maksās ķēdes analīzes uzņēmumam, lai tas “izvērtē” ienākošos maisījuma dalībniekus.

CoinJoin darījumu izmantošana, lai apslēptu Bitcoin līdzekļu avotu, jau daudzus gadus ir bijusi Bitcoin privātuma pamatā, un tās izmantošanai raksturīgās problēmas un riski ir dažas no galvenajām problēmām, ko Monero gredzena paraksti izlabo un novērš. 

Šajā blogā mēs īsumā aplūkosim CoinJoin un gredzenveida parakstu salīdzinājumu, kā arī to, kāpēc Monero izmantotā pieeja nodrošina lielāku pretestību cenzūrai, lielāku privātumu un mazāk problēmu lietotājiem.

## Kas ir CoinJoin pārskaitījums?

## Kas ir CoinJoin pārskaitījums?

Tā kā visi darījumi Bitcoin sistēmā ir pilnīgi caurredzami - tiek atklāts sūtītājs, saņēmējs un summas - lietotājiem ir jāveic papildu darbības, lai aizsargātu savu privātumu no iepriekšējiem sūtītājiem un turpmākajiem līdzekļu saņēmējiem vai riskētu ar cenzūru, uzraudzību vai līdzekļu zādzību, izmantojot fizisku vardarbību.

Mūsdienās labākais risinājums Bitcoin privātumam ir rīks ar nosaukumu [“CoinJoin”](https://bitcoiner.guide/qna/coinjoin/), kurā 2 vai vairāk lietotāji strādā kopā (parasti izmantojot centralizētu koordinatoru), lai izveidotu īpašu darījumu, kas apgrūtina ārējam novērotājam savienot ieejas ar izejām. Katrs dalībnieks sazinās, lai kopīgi izveidotu darījumu, nenododot savu līdzekļu glabāšanu, un beigās saņem izvadi, kuras iepriekšējā vēsture tagad ir neskaidra (vai apslēpta) ārējiem novērotājiem.

Tādējādi tiek pārtraukta konkrētu UTXO vēsture, ļaujot Bitcoin lietotājiem, veicot darījumus, iegūt zināmu slepenību. Tomēr CoinJoin (kā ieviests Wasabi Wallet un Samourai Wallet, divos visbiežāk izmantotajos Bitcoin CoinJoin rīkos) ir daži būtiski trūkumi: 

  * Tā kā CoinJoin darījumi ir pilnībā izvēlēti un tiem ir nepieciešama aktīva līdzdalība, jebkurš dalībnieks noteikti parāda, ka vēlas lielāku privātumu nekā “parastie” Bitcoin lietotāji, iespējams, izceļot tos un radot problēmas ar līdzekļu izlietošanu daudzās regulētās biržās vai struktūrās. Lietotājs nevar noliegt, ka ir piedalījies CoinJoin darījumā.
  * Lai atrastu citus CoinJoin, lielākajā daļā CoinJoin pieeju (tostarp Wasabi Wallet) tiek izmantots centralizēts koordinators, kas savieno dalībniekus un palīdz viņiem sazināties un izveidot pareizu CoinJoin darījumu. Šis centralizētais koordinators nekad nepārvalda lietotāju līdzekļus, taču tas gūst plašu ieskatu darījumos, ko koordinē, var cenzēt ienākošos datus (kā Wasabi Wallet gadījumā) un var tikt piespiests vākt vai koplietot informāciju par CoinJoin dalībniekiem.
  * Lietotājiem, kuriem ir lielas līdzekļu summas CoinJoin, bieži vien var būt jāgaida stundas (vai pat dienas!), lai atrastu pietiekami daudz dalībnieku, ar kuriem varētu veikt CoinJoin, tādējādi radot lielu aizturi no brīža, kad lietotājs saņem līdzekļus, līdz brīdim, kad viņš var tos iztērēt privāti. 
  * CoinJoin darījuma nodrošinātā konfidencialitāte laika gaitā pasliktinās, jo citi dalībnieki tērē līdzekļus vai saista savus rezultātus ar savu identitāti, izmantojot KYC apmaiņu, tirgotājus, kuriem nepieciešams ID, u.c. Tas nozīmē, ka lietotāji ideālā gadījumā CoinJoin darījumos saglabā savus līdzekļus nepārtraukti, lai viņu anonimitātes grupa (“pūlis, kurā paslēpties”) būtu pēc iespējas svaigāka.
  * Lielākajā daļā CoinJoin pieeju dalībniekiem ir jāizmanto fiksēta izmēra UTXO (t.i., 0,1 BTC), lai būtu grūtāk savienot CoinJoin darījumu ieejas un izejas. Tas rada augstākas maksas (nepieciešams vairāk atsevišķu pārskaitījumu uz lielu ievadi), vairāk "toksiskas maiņas" (līdzekļi, kurus nevar iztērēt, neradot nopietnus draudus privātumam), un var liegt mazākiem lietotājiem piedalīties vispār, ja viņiem nav minimālais nepieciešamais atlikums.

## Kā gredzenveida paraksti atrisina šīs problēmas?

## Kā gredzenveida paraksti atrisina šīs problēmas?

Tā kā [ jau esam padziļināti izpētījuši, kas ir gredzenveida paraksti](/knowledge/ring-signatures), šajā blogā nerunāsim par to darbības tehniskajiem aspektiem. Tā vietā mēs apskatīsim, kā Monero izmantotās pieejas atrisina problēmas ar CoinJoin, kas apspriestas iepriekš.

> CoinJoin ir jāpiesakās, un ir nepieciešama līdzdalība

CoinJoin ir jāpiesakās, un ir nepieciešama līdzdalība

Monero gredzenveida paraksti ir privātuma protokola galvenā funkcija, un tie tiek izmantoti _katrā_ darījumā tīklā. Tas nozīmē, ka neviena lietotāja pārskaitījumi neizceļas ar lielāka privātuma meklēšanu nekā “parastie” Monero pārskaitījumi, un visi lietotāji var ticami apšaubīt, ka viņi ir iztērējuši līdzekļus kādā konkrētā pārskaitījumā. Tā kā lietotājs, kurš tērē līdzekļus, pārskaitījumu nekoordinē un nepiedalās mānekļu ievadīšanā, tie lietotāji, kuriem pieder ievades dati, kas ir izvēlēti kā mānekļi, var godīgi apgalvot, ka nepiedalījās šajā darījumā, tādējādi stiprinot viņu privātumu.

> Centralizēta koordinatora izmantošana

Centralizēta koordinatora izmantošana

Tā kā Monero gredzenveida paraksti ir pilnībā nesaskaņoti un pārskaitījuma izveidošanai ir nepieciešams tikai patiesais līdzekļu iztērētājs, Monero nav nepieciešams centralizēts koordinators. Tas nodrošina, ka _neviens_ nevar liegt jums piekļuvi Monero privātumam, un nav nevienas centralizētas vienības, uz kuru var izdarīt spiedienu, nav vienkāršu Sybil uzbrukumu likviditātei utt. Kamēr jūsu darījums maksā atbilstošu maksu, jūs iegūstat necenzētu piekļuvi Monero privātumam, drošībai un anonimitātei.

> CoinJoin nepieciešama likviditāte

CoinJoin nepieciešama likviditāte

"Likviditāte", kas pieejama ikvienam, kas tērē Monero, lai to izmantotu kā mānekļus, vienmēr ir kopējais izvadu komplekts ķēdē, lai nekad netrūktu mānekļu, kuros paslēpties ar Monero. Persona, kas vēlas iztērēt Monero, var to izdarīt aptuveni 20 min pēc līdzekļu saņemšanas, un nav jāveic nekādas papildu darbības, lai iegūtu spēcīgu Monero konfidencialitāti.

> CoinJoin konfidencialitāte laika gaitā pasliktinās

CoinJoin konfidencialitāte laika gaitā pasliktinās

Tā kā Monero izvadi nekad netiek iztērēti tīklā, gredzenveida parakstu nodrošinātais privātums laika gaitā ir daudz mazāk pakļauts degradācijai. Lietotājam nav nepārtraukti jāmaina izvades, un ārpus ārkārtīgi retiem apstākļiem laika gaitā tas nezaudē nekādu privātumu.

Ja lietotājs tomēr vēlas “atsvaidzināt” ar izvadi izmantotos mānekļus, viņš var vienkārši nosūtīt līdzekļus sev atpakaļ un var tos iztērēt apmēram 20 min vēlāk kā parasti.

> CoinJoin parasti ir nepieciešamas fiksēta izmēra ievades

CoinJoin parasti ir nepieciešamas fiksēta izmēra ievades

Tā kā summas tiek paslēptas katrā darījumā, izmantojot [“Konfidenciālos pārskaitījumus”](/knowledge/monero-ringct) (daļa no “RingCT”), jebkurā konkrētajā pārskaitījumā izmantotie mānekļi var būt jebkura izmēra. Nav iemesla uztraukties par Monero heiristiku, kas balstīta uz summām, tāpēc darījumus ir daudz vienkāršāk izveidot, un tie var izmantot mānekļus jebkurā laikā un jebkurā daudzumā Monero blokķēdē.

## Kā es varu uzzināt vairāk?

## Kā es varu uzzināt vairāk?

Ja jūs interesē un vēlaties labāk izprast gredzenveida parakstus vai CoinJoin pārskaitījumus, skatiet tālāk esošās saites, lai atrastu lieliskas vietas, kur sākt:

  * [Kā gredzenveida paraksti aizsedz Monero izvadi](/knowledge/ring-signatures)
  * [Gredzenveida paraksts — Moneropēdija](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [CoinJoin pārskats](https://6102bitcoin.com/coinjoin-overview/)

Lasīt tālāk

  * [Kā Monero unikāli nodrošina aprites ekonomiku](/knowledge/monero-circular-economies)/

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