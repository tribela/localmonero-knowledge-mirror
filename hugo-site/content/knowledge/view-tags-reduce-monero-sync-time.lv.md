---
title: "Skata tagi: kā viens baits samazinās Monero maka sinhronizācijas laiku par 40%+"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Viena no visbiežāk sastopamajām sūdzībām par Monero lietošanu ikdienā ir laiks, kas var būt nepieciešams, lai sinhronizētu maku, pirms var nosūtīt Monero. Par laimi, Monero kopienas izstrādātāji un pētnieki ir atraduši lielisku veidu, kā par 40%+ samazināt laiku, kas nepieciešams, lai sinhronizētu savu maku bez papildu blokķēdes uzpūšanās, maksām utt.

Ievadiet “view tags”, kas ir viena baita papildinājums katra pārskaitījuma datiem — nākamajā tīkla atjauninājumā tas būs pieejams Monero!

## Kāpēc Monero maka sinhronizācija ir lēnāka nekā Bitcoin?

## Kāpēc Monero maka sinhronizācija ir lēnāka nekā Bitcoin?

Viens no pirmajiem jautājumiem, uz kuru mums ir jāatbild, lai labāk izprastu vajadzību pēc tāda risinājuma kā skata tagi, ir iemesls, kāpēc Monero maka sinhronizācija ir lēnāka nekā kriptovalūtām kā Bitcoin.

Tā kā Bitcoin visi pārskaitījumi nav privāti un atklāj iztērētās monētas, summas un ķēdē iesaistītās adreses, Bitcoin maki var vienkārši meklēt visus neiztērēto pārskaitījumu rezultātus (UTXO) vai izmantotās adreses konkrētajam makam, ātri skenējot blokķēdi un meklējot tikai UTXO, kas pieder šīm adresēm, lai noskaidrotu, kuras monētas pieder jūsu makam un kuras var iztērēt.

Tomēr Monero visi pārskaitījumi saglabā lietotāja privātumu, slēpjot sūtītāju, saņēmēju un katrā pārskaitījumā iesaistītās summas. Šis privātums, lai gan ir ļoti svarīgs tīkla lietotāju aizsardzībai, arī rada lēnāku maka sinhronizāciju. Monero jūsu makam ir jāsalīdzina katra tīklā esošā pārskaitījumu izvade (TXO) ar jūsu maka privātajām atslēgām.

Šis salīdzinājums ietver daudzas sarežģītas matemātiskas un kriptogrāfiskas darbības, lai apstiprinātu, ka izvade patiešām ir jūsu, jo visas summas, adreses un zināmās iztērētās izvades (vai monētas) ir paslēptas Monero ķēdē.

## Kas ir skata tagi?

## Kas ir skata tagi?

Lai palīdzētu samazināt Monero maku sinhronizācijas laiku, [pētnieks UkoeHB nāca klajā ar jaunu pieeju](https://github.com/monero-project/research-lab/issues/73) — pievienot 1 baita “birku” katram pārskaitījumam, izmantojot kopīgo noslēpumu, zināmu šī pārskaitījuma sūtītājam un saņēmējam.

Šo kopīgo noslēpumu ģenerē sūtītājs, izmantojot adresi, ko viņam norādījis adresāts, un tai nav nepieciešama aktīva sūtītāja un saņēmēja sadarbība. Pēc tam šī kopīgā noslēpuma pirmais baits (vai rakstzīme) tiek pievienots pārskaitījuma datiem, publicējot to Monero tīklā.

Kad kāds no šī pārskaitījuma dalībniekiem pēc tam vēlas sinhronizēt savu maku ar Monero blokķēdi, tā vietā, lai veiktu visu sarežģīto matemātiku un kriptogrāfiju katram tīkla pārskaitījumam, maks tagad var vienkārši meklēt šo 1 baita lauku katrā pārskaitījumā un tikai pēc tam veikt laikietilpīgo verifikāciju pārskaitījumiem, kuriem ir šis tags — 1/256 no visiem pārskaitījumiem tīklā!

Šis tags ārējiem skatītājiem neatklāj nekādu informāciju par pārskaitījumu, tikai pievieno 1 baitu (niecīgs apjoms) pārskaitījuma izmēram, tomēr ļauj mums samazināt sinhronizācijas laiku par 40%+, samazinot sarežģītās pārbaudes!

## Skata tagi: vienkāršots piemērs

## Skata tagi: vienkāršots piemērs

Iedomājieties, ka jums istabā ir 4096 kastes, no kurām tikai 5 kastes pieder jums. Visas kastes ir pilnīgi neatšķiramas no ārpuses, un vienīgais veids, kā noteikt, vai kaste ir paredzēta jums, ir to atvērt un atrisināt iekšā ierakstītu laikietilpīgu matemātikas uzdevumu, lai pārliecinātos, ka tā pieder jums.

Tagad iedomājieties, ka nolemjat likt personai, kas jums nosūtīja šīs 5 kastes, ģenerēt īpašu kodu, izmantojot jūsu adresi, un pēc tam katras jums nosūtītās kastes ārpusē ievietot tikai šī ģenerētā koda pirmo rakstzīmi. Visi pārējie dara to pašu ar savām kastēm (lai nodrošinātu, ka visas kastes joprojām nav atšķiramas), taču tagad varat vienkārši apskatīt vienas rakstzīmes kodu kastes ārpusē un atvērt tikai tās kastes, uz kurām ir šī rakstzīme.

Lai gan citi lodziņi arī atbildīs jūsu kodam, tai skaitā daži, kas jums nepieder, to lodziņu skaits, kas jums ir jāatver un jāatrisina matemātikas uzdevums, tagad ir tikai 16 (1/256 lodziņi!) visu 4096 vietā. 

Tagad jūs atverat šos 16 lodziņus, atrisināt matemātikas uzdevumus un paturat 5 kastes no šīs grupas, kas patiešām pieder jums!

## Kad skata tagi būs pieejami Monero?

## Kad skata tagi būs pieejami Monero?

Skata tagi ir viena no funkcijām, ko pašlaik plānots iekļaut [gaidāmajā tīkla uzlabojumā](https://github.com/monero-project/meta/issues/630), un tos paredzēts izlaist šajā pavasarī. Kopiena [ savāca 23.3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (rakstīšanas laikā), lai stimulētu skatu tagu izstrādi un ieviešanu, un rezultātā lielākā daļa darba, lai iekļautu skata tagus Monero koda bāzē, jau ir paveikts. To paveica j-berman sadarbībā ar recenzentiem un pētniekiem.

Kad tīkls ir ieviesis skata tagus, visi pārskaitījumi, kas nosūtīti pēc tīkla atjaunināšanas, gūs labumu no krasi uzlabotā maka sinhronizācijas laika. Jums nav jādara nekas īpašs, lai sāktu lietot skata tagus, jūsu iecienītākais Monero maks vienkārši sāks tos lietot pēc tīkla atjaunināšanas!

## Kā es varu uzzināt vairāk?

## Kā es varu uzzināt vairāk?

Ja tas ir izraisījis jūsu interesi par skata tagiem, tālāk ir dažas papildu saites, kas sniedz padziļinātu ieskatu tēmā:

  * [Samaziniet skenēšanas laiku, izmantojot 1 baita uz izvadi “skata tagu”](https://github.com/monero-project/research-lab/issues/73)
  * [Pievienojiet skata tagus izvadēm, lai samazinātu maka skenēšanas laiku](https://github.com/monero-project/monero/pull/8061)

Lasīt tālāk

  * [Kā Monero unikāli nodrošina aprites ekonomiku](/knowledge/monero-circular-economies)/

  * [Monero gredzenveida paraksti salīdzinājumā ar CoinJoin kā Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Kāpēc (un kā!) jums vajadzētu turēt savas atslēgas](/knowledge/hold-your-keys)/

  * [Iesaiste Monero](/knowledge/contributing-to-monero)/

  * [Kā attālie mezgli ietekmē Monero privātumu](/knowledge/remote-nodes-privacy)/

  * [Kā Monero izmanto hard-forks tīkla uzlabošanai](/knowledge/network-upgrades)/

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