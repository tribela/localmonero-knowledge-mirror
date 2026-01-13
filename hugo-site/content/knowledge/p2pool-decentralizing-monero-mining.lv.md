---
title: "P2Pool un tā loma Monero mainošanas decentralizācijā"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Viens no Monero projekta galvenajiem mērķiem ir nodrošināt godīgu, decentralizētu un drošu tīklu, izmantojot jaunas un novatoriskas pieejas proof-of-work (PoW) mainošanai, kas ir galvenais veids, kā mūsdienās tiek nodrošināti kriptovalūtu tīkli. 

Lai gan unikāls mainošanas algoritms [, piemēram, RandomX](/knowledge/monero-mining-randomx), ir ārkārtīgi svarīgs šī mērķa sasniegšanai, jo tas palīdz nodrošināt, ka ikviens, kam ir dators, var sniegt pienācīgu ieguldījumu tīkla drošībā, RandomX neatrisina problēmas, kas var rasties baseinu dēļ. Baseinu mainošana mūsdienās ir visizplatītākais kriptovalūtu mainošanas veids, tostarp Monero, taču, par laimi, p2pool mainošanas parādīšanās to strauji maina.

## Kas ir baseinu mainošana?

Baseinu mainošana ir veids, kā maineri var kopīgi mēģināt atrisināt bloku tīklā un pēc tam vienmērīgi sadalīt atlīdzību par visiem blokiem, ko kopums atrod. Lai gan tas ļoti palīdz izlīdzināt maineru darba samaksas biežumu salīdzinājumā ar Monero mainošnu vienatnē, tas nav bez nopietnām centralizācijas problēmām.

Tā kā katrs maineris iegulda darbu baseinā, viņi nodod baseinam kontroli pār jebkuru darbu, ko viņi dara, un blokiem, ko atrod, paļaujoties, ka baseins godīgi sadalīs atlīdzību starp visiem maineriem, pamatojoties uz darba apjomu, ko katrs paveicis. Ja viss norit labi, baseina operators savāc darbu no visiem maineriem, iesniedz to tīklam un vienādi sadala atlīdzību.

## Kāda ir problēma ar baseinu mainošanu?

Diemžēl tas pilnībā balstās uz uzticēšanos un ļauj baseina operatoram veikt nelāgas lietas ar maineru veikto darbu. Baseina operators varētu izmantot paveikto darbu, lai uzbruktu tīklam, mēģinātu divreiz tērēt līdzekļus (ja kopums ir pietiekami liels) vai vienkārši izmantot maineru paveikto darbu, lai samaksātu sev un nekad pienācīgi neatalgotu mainerus par viņu darbu. 

Lielākais risks tīklam ir tas, ka baseins (vai vairāki baseini, kas strādā kopā), kas kontrolē ir vairāk nekā 51% tīkla, to var izmantot, lai krāptos un iztērētu līdzekļus divreiz (dubultā tēriņa uzbrukums) vai mēģināt mainīt tīkla noteikumus.

## Kas ir p2pool?

p2pool ir koncepts, kas sākotnēji tika izveidots Bitcoin mainošanai 2011. gadā, taču tas nekad netika plaši pielietots un paliek praktiski neizmantots Bitcoin. Par laimi, viens no galvenajiem RandomX izstrādātājiem, SCHernykh, pavadīja savu atvaļinājumu, izstrādājot risinājumus dažām problēmām, kas saistītas ar p2pool ieviešanu Bitcoin un pārrakstot visu programmatūru no nulles.

p2pool Monero ļauj maineriem pilnīgi bez uzticības sadarboties, lai atrisinātu blokus un nodrošinātu Monero tīklu, izmantojot īpašu p2pool mezgla programmatūru, lai koplietotu darbu.

Tas tiek darīts, izmantojot jaunu blokķēdi (“sānu ķēdi”), kas reģistrē katra mainera paveikto darbu, savu maka adresi un nopelnīto Monero, un pēc tam izmaksā atlīdzību bezuzticības un decentralizētā veidā. Tā kā šajā sānu ķēdē ir daudz mazāk maineru, tajā ir daudz vieglāk atrast un iesniegt blokus nekā galvenajā Monero tīklā, tādējādi maineriem ir vieglāk iegūt konsekventus maksājumus, salīdzinot ar Monero ieguvi vienatnē.

## Kā p2pool atrisina baseinu mainošanas problēmas?

p2pool nav centralizēta baseina, centralizēta operatora vai vienas personas, kas glabā līdzekļus un sadala izmaksas. Visu darbu, ko kolektīvi veic tie, kas izmanto p2pool, pārbauda p2pool blokķēde un citi mezglu operatori, lai pārliecinātos, ka tas ir likumīgs. Visiem maineriem tiek izmaksāta atlīdzība saskaņā ar paveikto darbu, līdz ko bloks tiek atrasts - tieši no atlīdzības šajā atrastajā blokā.

Kad maineri izvēlas izmantot p2pool, nevis centralizētu baseinu, viņi ņem atpakaļ visas operatoru pilnvaras un uzticību un nodrošina, ka viņu darbs dod tīklam labumu un pelna pašiem atlīdzību. Tas arī samazina riskus kā tīkla uzbrukums, ļaunprātīga izmantošana, atlīdzības zādzība.

Tas ne tikai palīdz viņiem aizsargāt savas intereses, bet arī samazina risku, ko centralizētie baseini var radīt Monero tīklam kopumā. p2pool izmantošana arī palīdz ievērojami samazināt risku, ko valstis vai regulatori var radīt tīkla veselībai, jo nav centralizētu baseinu operatoru, ko pakļaut spiedienam, nav baseinu ģeogrāfiskas koncentrācijas, uz ko balstīties, vai citu vieglu spiediena punktu, ko varētu izmantot pret Monero.

## Kādi ir trūkumi?

Par laimi, p2pool Monero ir rūpīgi izstrādāts un uzbūvēts, un tas darbojas ļoti labi! Tomēr galvenais p2pool ieguves trūkums ir tas, ka katram mainerim, kurš vēlas izmantot p2pool, ir vajadzīgs savs Monero mezgls, tādējādi darba sākšanas process ir nedaudz laikietilpīgāks. Tomēr šis mezgls pēc tam tiek izmantots, lai aprēķinātu visu informāciju, kas nepieciešama bloku veidošanai un pārbaudei, un nodrošina, ka maineris pilnībā kontrolē savu darbu. Mezgls var darboties arī kā attālais mezgls mainera maciņam, dot ieguldījumu tīklā un daudz ko citu.

Otra galvenā atšķirība no centralizētās ieguves ir tā, ka mazajiem maineriem, kas izmanto p2pool, būs nedaudz lielāka "variance" jeb laiks starp izmaksām nekā lielam centralizētam kopumam, taču ' ir _ļoti_ ir svarīgi atzīmēt, ka tas laika gaitā neradīs mazākus Monero ienākumus! p2pool laika gaitā būs tikpat izdevīgs pat maziem maineriem kā centralizētie baseini. Daļu no šīs novirzes kompensē arī tas, ka p2pool sākotnējā maksa ir 0%, jo nav centralizēta operatora, kam būtu jāmaksā par pakalpojumiem!

## Kā es varu sākt?

Par laimi, pateicoties lieliskajam Monero' p2pool izveidojumam un daudzajiem cilvēkiem kopienā, kuri ir veltījuši laiku, lai palīdzētu vienkāršot mainošanas procesu, izmantojot p2pool, laika gaitā darba sākšana kļūst vienkāršāka. Ir vairāki veidi, kā sākt mainošanu, izmantojot p2pool, taču, tā kā tehniskā informācija ir ārpus šī raksta jomas, varat atvērt tālāk norādīto saiti atkarībā no jūsu operētājsistēmas: 

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## Kā es varu uzzināt vairāk?

Ja tas ir izraisījis jūsu interesi par p2pool ieguvi, tālāk skatiet dažas papildu saites un skaidrojumus par p2pool, kā tas darbojas un ko tas nozīmē Monero:

  * [Oficiālā Github vietne p2pool](https://github.com/SChernykh/p2pool)
  * [Oficiālie dokumenti par p2pool izmantošanu](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool tagad ir tiešraidē](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, sava veida "bloku pārlūks" p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [ Sergejs Černihs: par viņa izstrādāto P2Pool - decentralizētu XMR mainošanas baseinu](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

Lasīt tālāk

  * [Kā Monero unikāli nodrošina aprites ekonomiku](/knowledge/monero-circular-economies/)

  * [Monero gredzenveida paraksti salīdzinājumā ar CoinJoin kā Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Kāpēc (un kā!) jums vajadzētu turēt savas atslēgas](/knowledge/hold-your-keys/)

  * [Iesaiste Monero](/knowledge/contributing-to-monero/)

  * [Kā attālie mezgli ietekmē Monero privātumu](/knowledge/remote-nodes-privacy/)

  * [Kā Monero izmanto hard-forks tīkla uzlabošanai](/knowledge/network-upgrades/)

  * [Skata tagi: kā viens baits samazinās Monero maka sinhronizācijas laiku par 40%+](/knowledge/view-tags-reduce-monero-sync-time/)

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