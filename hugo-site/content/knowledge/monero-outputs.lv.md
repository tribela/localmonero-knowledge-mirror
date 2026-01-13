---
title: "Monero izvades tuvplānā"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero, tāpat kā citas kriptovalūtas, izmanto izvades kā uzskaites līdzekli. Iespējams, ka daudzi kriptogrāfijā gudri lietotāji jau ir dzirdējuši šo terminu, taču ne visi saprot, ko tas nozīmē un kā tas darbojas. Kā aprakstīts mūsu [gredzenveida parakstu rakstā](/knowledge/ring-signatures), izvades ir faktiskā vienība, ar kuru blokķēdē apmainās starp pārskaitījuma pusēm. Līdzīgi kā dolāra banknotei, taču summa nav fiksētā nominālvērtībā.

Ja par darbu saņemat 16 dolārus, iespējams, saņemsiet viena dolāra banknoti, piecu dolāru banknoti un desmit dolāru banknoti. Jums ir 16 $, taču makā ir arī trīs dažādas banknotes. Ja vēlaties kādam samaksāt 6 dolārus, varat izmantot 5 un 1 banknotes, bet, ja vēlaties kādam samaksāt 8 ASV dolārus, varat izmantot tikai 10 dolārus un saņemt atpakaļ 2 dolārus. Visbeidzot, ja vēlaties kādam samaksāt 14 dolārus, jums būs jāizmanto visas trīs banknotes un 2 dolārus saņemtu atpakaļ maiņā, taču uz brīdi, kad nododat visas trīš banknotes, jūsu makā nav naudas, līdz nesaņemat maiņu.

Monero darbojas līdzīgi. Pieņemsim, ka jūs vadāt veikalu un trīs reizes pārdodat trīs dažādas preces. Jūs varat saņemt 1,5 XMR, 2,25 XMR un 5,25 XMR kopā par 9 XMR, taču jūsu makā ir arī trīs dažādas iepriekš norādītās nominālvērtības. Tāpat kā ar dolāriem, iespējams, vēlēsieties kādam maksāt 3 XMR. Varat izmantot tikai 5,25 XMR izvadi un saņemt atpakaļ 2,25 XMR izvadi, vai arī varat apvienot 1,5 un 2,25 XMR izvadi un iegūt atpakaļ 0,75 XMR maiņā.

Taču, tiklīdz nosūtāt pārskaitījumu, jūsu izmantotās izvades tiek iestatītas "bloķētā" stāvoklī, kas nozīmē, ka tās nav pieejamas, kamēr nesaņemat atpakaļ maiņu. Protokols atbloķē līdzekļus (t.i., atdod jums maiņu) pēc 10 apstiprinājumiem jeb aptuveni 20 minūtēm. Tāpat kā pēc tam, kad izsniedzat dolāru banknotes no sava maka, jūs nevarat atkārtoti izmantot naudu, kamēr nesaņemat atpakaļ no kases, jūsu Monero nav pieejams, kamēr nesaņemat atpakaļ naudu.

Atgriezīsimies pie 3 XMR nosūtīšanas piemēra, un jūs izmantojat 5,25 XMR izvadi. Tagad, kamēr jūs gaidāt 1,75 XMR maiņu, jūs nevarat to izmantot. Šis 1,75 XMR jums nav pieejams. Bet jūs joprojām varat izmantot 1,5 XMR un 2,25 XMR izejas, jo tās netika iztērētas. Atgriežoties pie dolāra piemēra, ja jūs kādam maksājāt 8 dolārus, kā tas bija piemērā iepriekš, jūs nevarēsiet izmantot 2 dolārus, ko sagaidāt atpakaļ maiņā, līdz tie jums tiks piešķirti, taču šajā piemērā jums joprojām ir 10 $ banknote, kas stāv neizmantota jūsu makā. To joprojām var izmantot, lai iegādātos visu, ko vēlaties, kamēr gaidāt maiņu. Tas pats ar Monero.

Tas bieži rada neskaidrības jauniem Monero lietotājiem. Bieži vien lietotāja makā var būt tikai viena izvade, kas saņemta no biržas vai drauga. Pieņemsim, ka šī izvade ir 20 XMR. Viņiem nav citu izeju savā makā. Tagad viņi vēlas ziedot divām savām iecienītākajām labdarības organizācijām. Viņi nosūta 5 XMR pirmajai labdarības organizācijai un pēc tam ir apmulsuši, jo, lai gan viņiem vajadzēja palikt 15 XMR, viņi nevar uzreiz nosūtīt nākamo ziedojumu otrajai labdarības organizācijai. Kā jūs varētu uzminēt, tas ir tāpēc, ka 15 XMR ir bloķēts. To nevar iztērēt, kamēr tas nav atgriezts kā maiņa (10 apstiprinājumi vai aptuveni 20 minūtes). Kad viņu līdzekļi tiks atbloķēti, viņi varēs nosūtīt savu otro ziedojumu.

Lai vēlreiz atgādinātu, viņiem šīs problēmas nebūtu, ja tās vietā būtu bijušas vairākas izvades, piemēram, divas 10 XMR izejas vai līdzīgas. Viņi varētu nosūtīt abus ziedojumus vienu pēc otra, jo pirmajā ziedojumā tiktu izmantota viena no 10 XMR izvadēm (un gaidītu 10 apstiprinājumus, lai saņemtu atpakaļ 5 XMR), bet otrajā ziedojumā tiktu izmantota otra 10 XMR izvade.

Dažiem kriptovalūtas makiem ir funkcija, ko sauc par “izvadu pārvaldību”, kas vienkārši parāda lietotājam, kuras izvades viņam pašlaik ir (papildus kopējai summai), kā arī ļauj izvēlēties, kuras no tām izmantot, kad tiek tērēta kriptovalūta.

Pašlaik Monero GUI izvades atlasi lietotājiem veic automātiski, jo lietotāji, izvēloties paši savas izvades, bieži rada neskaidrības vai dažos gadījumos tiek apdraudēts privātums. Tomēr tiek izstrādāti maki, piemēram, jaunais Feather maka projekts, kas ietvers šīs izvades pārvaldības funkcijas.

Mēs esam daudz runājuši par nosūtīšanas daļu, taču saņemšanas pusē notiek kaut kas aizraujošs. Atgriežoties pie mūsu piemēra par 3 XMR nosūtīšanu kādam un jūsu 1,5 XMR un 2,25 XMR izvadu izmantošanu pārskaitījumā (gaidot 0,75 XMR maiņu), saņēmējs NESAŅEM divas izvades 1,5 XMR un 2,25 XMR. Tā vietā tie saņem VIENU 3 XMR izvadi.

Fonā protokols apvieno visas izvades, kas tiek izmantotas tēriņiem, un dod saņēmējam vienu izvadi no samaksātās summas un nosūta vienu maiņas izvadi atpakaļ sūtītājam. Tādējādi sūtītājs saņems arī vienu izvadi atpakaļ kā maiņu neatkarīgi no tā, vai darījuma nosūtīšanai izmantoja divas, trīs vai desmit izvades.

Mēs ceram, ka izdevās kliedēt neskaidrības par izvadēm un to, kā darbojas protokola iekšējā uzskaite, kā arī parasto lietotāju apjukuma problēmu, saskaroties ar bloķētiem līdzekļiem. Citā rakstā mēs izpētīsim izvadu pārvaldību, lai samazinātu iespēju, ka pirms turpmāko pārskaitījumu nosūtīšanas būs jāgaida atbloķēti līdzekļi.

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