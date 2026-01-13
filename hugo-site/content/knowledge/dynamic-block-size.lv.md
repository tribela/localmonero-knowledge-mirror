---
title: "Kā Monero atrisināja bloka izmēra problēmu, kas vajā Bitcoin"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Piezīme:** Iepriekš ieteicams izlasīt mūsu rakstus [ "Kāpēc Monero ir astes emisija"](/knowledge/monero-tail-emission) un [ "Monero mainošana: ar ko RanomX ir tik īpašs”](/knowledge/monero-mining-randomx). Šis raksts ir balstīts uz tajos ietvertajiem jēdzieniem._

Kad cilvēki apspriež problēmas ar blokķēdi, viens no pirmajiem uznirstošajiem vārdiem būs “paplašināšana”. Nav noslēpums, ka blokķēdes nav viegli paplašināmas, taču lielākā daļa cilvēku nezina, kāpēc.

Paplašināšana patiesībā ir vispārīgs termins, kas aptver divas dažādas kategorijas: protokola atbalsts un tehnoloģiskais atbalsts noteiktā laika brīdī. Šajā rakstā mēs koncentrēsimies uz vienu — protokola atbalsts būtībā ir mērs, cik pārskaitījumu protokols var apstrādāt noteiktā laikā.

Bitcoin ir bloka lieluma ierobežojums, kas nozīmē, ka, tiklīdz blokā ir iekļauts pietiekami daudz pārskaitījumu, visiem papildu pārskaitījumiem būs jāgaida rindā uz nākamo bloku. Noderīga līdzība būtu domāšana par vilcienu. Vilciens piestāj pie stacijas, un rindā esošie iestājas. Kad vilciens ir pilns, ikvienam, kas paliks ārpusē, būs jāgaida nākamais.

Bitcoin izmanto maksas, lai noteiktu, kurš iekļūst blokā vai nē. Atgriežoties pie vilciena analoģijas, var iedomāties, ka viens potenciālais pasažieris, kurš drīz tiks atstāts, piedāvā vilciena vadītājam piecus dolārus, lai iedotu viņam vietu. Citi pasažieri seko šim piemēram, un galu galā notiek solīšanas karš, lai noskaidrotu, kurš saņems kuras vietas. Vadītāja ziņā ir izlemt, vai viņš vēlas ievērot rindas kārtības politiku, taču viņa finansiālajās interesēs ir maksimāli palielināt savus ienākumus, piesaistot visaugstākās cenas solītājus.

Šajā analoģijā maineri ir vilcienu vadītāji. Viņi blokā var iekļaut jebkurus pārskaitījumus, kurus viņi vēlas, un parasti viņi izvēlas tos, kuriem ir visaugstākās maksas.

Savukārt, ja bloki nav pilni, cilvēkiem nav stimula maksāt lielas maksas, jo ir daudz brīvu sēdvietu.

2017\. gada kriptovalūtas uzplaukuma laikā Bitcoin tika pārpludināts ar pārskaitījumiem, un maksas pieauga tiem, kas vēlējās tikt iekļauti nākamajā blokā vai jebkurā tuvākajā nākotnē. Tie, kuri nevēlējās maksāt augstas maksas, redzēja, ka viņu pārskaitījumi tika atbīdīti pa stundām, dienām vai pat vispār izkrita no rindas.

Šis bija satraucošs ieskats par to, kā Bitcoin veiktos, ja notiktu bieži runātais par “masveida ieviešanu”. Ja Bitcoin izmantotu masveidā, viss būtu vēl sliktāk nekā 2017. gadā, un Bitcoin nebūtu pieejams nevienam, izņemot turīgos, vienkārši tāpēc, ka caurlaides spēja ir maza fiksēta bloka izmēra dēļ, izraisot maksu tirgus pārņemšanu. 

Monero to paredzēja un vēlējās darīt kaut ko citu. Tādēļ Monero izstrādātāji ieviesa dinamisku bloka izmēru.

Būtībā Monero ir arī bloka izmēra ierobežojums, taču tas ir elastīgs. Kad pārskaitījumu gaidīšanas rinda kļūst pārāk gara, maineri var palielināt bloku izmēru. Izmantojot mūsu vilciena analoģiju, varat iedomāties vairāk vilcienu vagonu pievienošanu, lai ietilptu papildu pasažieri. Kad rinda ir iztukšota, bloki samazinās līdz sākotnējam izmēram.

Ja šī ideja šķiet gudra, ir pamatoti jautāt, kāpēc Monero ir vienīgā kriptovalūta, kas to ir ieviesusi. Kāpēc gan to neieviest Bitcoin, lai apturētu caurlaides spējas problēmas?

Diemžēl tas nav iespējams. Tam ir vairāki iemesli un tālāk centīsimies tos izskaidrot.

Maineru interesēs vienmēr ir lieli bloki. Izmantojot lielus blokus, viņi var iekļaut vairāk darījumu un nopelnīt vairāk naudas no maksām, kā arī no bloka atlīdzības. Tas var izraisīt spamošanas uzbrukumus, kad kāds nosūta daudz mazu darījumu par nelielu samaksu, lai uzpūstu ķēdi. Maineri vienkārši palielinātu bloka izmēru, iekļaujot tos visus, jo nauda ir nauda, neatkarīgi no tā, cik maza. Tas radītu nemainīgi lielus blokus ar nelielu ekonomisku labumu. Bitcoin to atrisina, mākslīgi ierobežojot bloka lielumu, tādējādi radot maksas tirgu. Spamošanas uzbrucējiem būtu jāmaksā citiem lietotājiem maksas, un tas vairs nav lēti. Taču tas nozīmē, ka bloki kļūst pilni, atstājot dažus pārskaitījumus gaidīšanas režīmā, kā minēts iepriekš.

Kā Monero var nodrošināt dinamiskus bloku izmērus, bet izvairīties no spamošanas uzbrukumiem? Atbilde ir vienkārša, bet gudra. Ja bloks ir lielāks nekā parasti, tiek samazināta atlīdzība par bloku. Ja maineris vēlas palielināt bloka izmēru, atlīdzība, ko viņš saņem par šī bloka atrašanu, būs mazāka nekā parasti. Tātad maineri palielinās bloka izmēru tikai tad, kad lietotāju samaksātās pārskaitījumu maksas pārsniegs zaudēto bloka atlīdzības daļu. Piemēram, ja maineris zaudētu 0,5 XMR, palielinot bloka izmēru, un saņemto darījumu maksu summa būtu 0,4 XMR, tad, palielinot izmēru, būtu tīrie zaudējumi 0,1 XMR apmērā, un viņš to nedarītu. Un otrādi - ja kopējās darījumu maksas sastādītu 0,7 XMR, tīrā peļņa būtu 0,2 XMR, lai gan viņš zaudēs 0,5 XMR no bloka atlīdzības samazināšanas, tāpēc maineris palielinās izmēru.

Šie dinamiskie bloki ļauj tīklam organiski augt, mākslīgi neierobežojot bloka izmēru, lai izveidotu piespiedu maksas tirgu, vienlaikus izvairoties no spamošanas uzbrukumiem. Ir vēl vairāki aspekti, no kuriem mēs varam aplūkot šo ideju, un vairāki iemesli, kāpēc to nebūtu iespējams pievienot Bitcoin. Taču pagaidām mēs ceram, ka lasītājam ir izpratne par to, kā Monero apiet vairākas no problēmām, kas raksturīgas Bitcoin un tā atvasinājumiem, un to, kā tas plāno palielināt savu caurlaides spēju nākotnē.

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

  * [Kā CLSAG uzlabos Monero efektivitāti](/knowledge/what-is-clsag/)

  * [Kāpēc Monero ir astes emisija](/knowledge/monero-tail-emission/)

  * [Īsa Monero vēsture](/knowledge/monero-history/)

  * [Žurnāls Wired kļūdās par Monero. Lūk, kāpēc](/knowledge/wired-article-debunked/)

  * [15 populārākie Monero mīti un bažas atspēkotas](/knowledge/monero-myths-debunked/)

  * [Kā Dandelion++ saglabā Monero pārskaitījumu izcelsmi privātu](/knowledge/monero-dandelion/)

  * [Kāpēc Monero ir atvērtā pirmkoda un decentralizēts](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero mainošana: ar ko RandomX ir tik īpašs](/knowledge/monero-mining-randomx/)

  * [Kāpēc Monero ir labāks par Dash, Zcash, Zcoin (pat ar Lelantus), Grin un Bitcoin mikseriem, piemēram, Wasabi (atjaunināts 2020. gada maijā)](/knowledge/why-monero-is-better/)