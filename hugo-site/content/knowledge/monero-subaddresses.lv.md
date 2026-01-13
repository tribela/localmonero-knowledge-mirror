---
title: "Kā Monero apakšadreses novērš identitātes saistīšanu"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero vienmēr ir atradis novatoriskus veidus, kā atrisināt sarežģītas privātuma problēmas. Bieži vien šīs inovācijas noved pie citiem jauninājumiem, un dažreiz šīs radītās tehnoloģijas var izmantot pat gadījumos, kas iepriekš nav izskatīti. Nekur tas nav vairāk parādīts kā Monero apakšadrešu tehnoloģijas gadījumā.

Apsveriet hipotētisku privātuma problēmu, kurā vienas adreses izmantošana vairākās platformās no šķietami nesaistītiem cilvēkiem var izraisīt minēto cilvēku sasaisti un deanonimizāciju. Vienkārši sakot, ja jūs būtu persona vārdā Billijs Džo Bobs un pārdotu ābolus par Bitcoin, jūs varētu publicēt savu Bitcoin adresi publiskā vietā, lai klienti varētu jums samaksāt. Pieņemsim, ka adrese sākas ar burtu un ciparu virkni 7XybV3... Bet, atmetot malā acīmredzamo privātuma risku, ka ikviens varēs pārbaudīt jūsu Bitcoin bilanci un redzēt, cik daudz esat pārdevis, ir otrs, par kuru netiek bieži runāts. Pieņemsim, ka jūs esat arī pagrīdes hakeris ar vārdu l33tz0r. Jūs veicat trauksmes celšanas darbu, stāstot sabiedrībai par valdības korupciju, un jums ir obligāti jāglabā sava identitāte noslēpumā. Jūs pieņemat Bitcoin ziedojumus par savu darbu un ievietojat adresi publiskā forumā. Tā ir tā pati adrese, kurā jūs pieņemat naudu no saviem Apple klientiem. 7XybV3....

Vienkāršs, bet postošs deanonimizācijas uzbrukums būtu izmantot interneta meklētājprogrammu, lai meklētu savu Bitcoin adresi. Ievietojot meklētājā adresi 7XybV3..., tiek parādīti divi dažādi rezultāti. Ābolu bizness un l33tz0r. Tas ir pietiekami, lai saistītu abas identitātes un deanonimizētu l33tz0r, kas var radīt biedējošas sekas no esošajiem spēkiem.

Ir svarīgi atzīmēt, ka šis uzbrukums ir iespējams ARĪ ar Monero. Lai gan Monero slēpj lielāko daļu ķēdes datu, šis uzbrukums neizmanto neko no tā. Tas izmanto tikai adresi, kas ir jāpublicē, lai saņemtu maksājumu. Publiski anonīmu ziedojumu gadījumā. Šis ir viens no iespējamiem veidiem, kā Monero lietotāji var netīši aizskart savu privātumu, un tas ir arī piemērs tam, ka, lai gan Monero ir visaugstākā līmeņa privātuma saglabāšanas ziņā, tas nav ložu necaurlaidīgs.

Parastais veids, kā apiet šo problēmu, bija vairāki maki. Ja katrai identitātei (vai lietošanas gadījumam) ir publicētas dažādas adreses, tās nevar saistīt. Taču šī konfidencialitāte ir spēkā tikai tad, ja lietotājs tās nekad nesajauc. Nejauši ievietojot nepareizu adresi, būtu tādas pašas sekas. Tāpat arī katras adreses sēkla ir jāglabā drošībā, palielinot drošības darbu, kas nepieciešams, ar katru jaunu maciņu.

Monero risinājums bija apakšadreses. Iespēja zem galvenās adreses izveidot absolūti milzīgu skaitu adrešu, izmantojot to kā sava veida sēklu. Katra ģenerētā apakšadrese var pieņemt Monero, un tā visa nonāk vienā makā. Izmantojot šo metodi, vienā adresē darbināmo identitāšu skaits ir milzīgs, vienlaikus samazinot drošības darbu līdz minimumam. Šīs adreses arī nav matemātiski savienojamas, tāpēc, ja vien lietotājs neizkliedz savu saistību pa pasauli, ārējam novērotājam būs lielas grūtības tās saistīt.

Bet no apakšadresēm parādījās vēl viens interesants lietojums - nīsto maksājumu ID aizstājējs.

Maksājumu ID bija veids, kā tirgotāji varēja noteikt, kurš klients kādu maksājumu nosūtījis. Tā kā Monero informācija ķēdē ir aizklāta, pārskaitījuma saņēmējs nevar redzēt, kura adrese to nosūtīja. Tas nozīmē, ka, ja ir līdzīgas cenas preces un vairāki pasūtījumi, var kļūt neiespējami noteikt, kurš ko nosūtījis. Maksājumu ID ir unikāla, nejauša virkne, ko ģenerē tirgotājs un piešķir klientam. Klients to pievieno kā atsevišķu lauku, nosūtot pārskaitījumu. Šī nejaušā virkne tiek ievietota blokķēdē kā daļa no pārskaitījuma, un šādā veidā tirgotājs var identificēt un kārtot ienākošos pārskaitījumus.

Šī metode bija kļūdaina vairākos veidos. Pirmkārt, tas mazina ķēdē esošo datu vienveidību. Papildu, unikāli metadati var padarīt dažus pārskaitījumus atšķirīgus no pūļa, tādējādi ļaujot veikt heiristisko analīzi. Tas jo īpaši attiecas uz gadījumiem, kad šie metadati nav ieviesti kā obligāti visiem. Tomēr, ja tas būtu obligāti visiem, blokķēdei tiktu pievienota nevajadzīga vieta, un tas netika īstenots. Tāpat, ja maksājuma ID kādreiz tiktu izmantots atkārtoti kāda iemesla dēļ, būtu elementāri saistīt divus pārskaitījumus. Tas parasti tika darīts ar maiņas noguldījumiem, un ikviens varēja viegli saistīt pārskaitījumus gan kā depozītu biržā, gan no vienas konkrētas personas.

Otrkārt, no UX perspektīvas maksājumu ID veido vēl vienu soli, pie kura kriptovalūtas lietotāji, kas nāk no citām monētām, nav pieraduši, un, ja tie tiek aizmirsti, tas rada lielas galvassāpes tirgotājam, kuram šie pārskaitījumi ir jāidentificē ar citiem līdzekļiem. . Parasti tas tika darīts, tieši sarunājoties ar katru klientu, kurš aizmirsa ievadīt maksājuma ID, un apstiprinot citu identificējošu informāciju, ko varēja zināt tikai viņi, piemēram, summas, nosūtīšanas datuma un pārskaitījuma ID kombināciju.

Šo papildu darbību daudzi palaida garām, un tas nonāca tiktāl, ka dažas biržas sāka iekasēt naudu no klientiem, ja viņu nauda bija manuāli jāidentificē, jo tika aizmirsts maksājuma ID. Citi sakoda zobus un pieņēma papildu atbalsta izmaksas, bet neviens par to nebija priecīgs.

Tam bija viens risinājums - integrētas adreses, kas apvienoja adresi un maksājuma ID vienā virknē, tāpēc to nevarēja aizmirst, taču adopcija bija diezgan vāja, neskatoties uz ieguvumiem, ko tirgotāji būtu guvuši no tā iekļaušanas. 

Interesantā notikumu pavērsienā tika izmantotas apakšadreses, lai glābtu situāciju. Iespēja ģenerēt lielu daudzumu apakšadrešu katrai galvenajai adresei un noteikt, kuri pārskaitījumi kādās apakšadresēs tika veikti, ļāva tirgotājiem elegantā veidā atbrīvoties no maksājumu ID, vienlaikus pieņemot nākamās paaudzes Monero tehnoloģiju. Kopš tā laika lielākā daļa biržu un tirgotāju rīku ir pārgājuši uz apakšadresēm kā primāro pārskaitījumu identifikācijas veidu.

Tas, kas sākās kā privātuma problēmas risinājums, kļuva par kaut ko daudz vairāk, kas atrisināja būtisku UX problēmu gan tirgotājiem, gan klientiem. Inovācijas rada vairāk jauninājumu, kas bieži vien var radīt negaidītas uzvaras ikvienam. Monero to ir redzējis atkal un atkal un pieliek lielas pūles, lai ieviestu jauninājumus, kas ir iespējams blokķēdē. Kurš zina, kādas citas lietas mēs varam atklāt kopā?

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