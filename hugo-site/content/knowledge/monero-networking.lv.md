---
title: "Kas jāzina ikvienam Monero lietotājam, kad runa ir par tīklu veidošanu"
slug: "monero-networking"
date: "2020-11-11"
image: "/images/networking.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Nevienam nevajadzētu būt par pārsteigumu, ka Monero un pat visa kriptovalūta darbojas internetā. Un tomēr, lai gan šis apgalvojums šķiet vienkāršs un acīmredzams, daudzi neņem vērā, ko tas nozīmē attiecībā uz viņu privātumu. Citiem vārdiem sakot, ir dažas lietas, no kurām Monero var un nevar aizsargāties, tikai tāpēc, ka darbība notiek internetā. Daži no šiem apsvērumiem ir tikai neērtības, savukārt citi ir daudz nopietnāki situācijā, kad ir nepieciešama absolūta privātuma aizsardzība. Atvēlēsim laiku, lai iepazītos ar to, kā Monero lietotāji mijiedarbojas viens ar otru tīklā un ko tas nozīmē viņu privātumam.

Sākot ar lietu triviālo pusi, ja lietotājam nav piekļuves internetam, viņš nevar lejupielādēt jaunus blokus, izplatīt pārskaitījumus citu vārdā vai nosūtīt savus pārskaitījumus. Interesanti atzīmēt, ka lietotājs ar pilnu mezglu bez piekļuves internetam var izveidot pārskaitījumu bezsaistē, ko var nosūtīt vēlāk. Tas ir tāpēc, ka gredzenveida parakstam ir nepieciešami tikai blokķēdes izvadi, ar kuriem paslēpties. Īss atgādinājums par [, kā darbojas gredzenveida paraksti](/knowledge/ring-signatures), tas slēpj patieso izvadi, ko lietotājs sūta starp nesaistītu izvadu kolekciju, kas izvēlēta no pagātnes. Ja lietotājam ir piekļuve šīm izejām pilnībā lejupielādētas blokķēdes (pilna mezgla) veidā, viņš var izveidot gredzenveida parakstu no iepriekšējiem izvadiem un, tiklīdz interneta savienojums tiek atjaunots, pārskaitījumu izplatīt tīklā.

Lietotājs, kurš izmanto attālo mezglu, to nevar izdarīt, jo, veidojot savu gredzenveida parakstu, viņš sazinās ar attālo pilno mezglu, lai izvadi iekļautu gredzena parakstā. Ja nav interneta, viņš nevar sasniegt šo mezglu, tāpēc arī nav bezsaistes pārskaitījuma izveides iespēju.

Pirms mēs turpinām izskatīt dažus privātuma apsvērumus, īsi apskatīsim, kā internets darbojas kopumā. Viss internets ir nekas cits kā datori, kas savienojas ar citiem datoriem. Tieši tā. Blogs, kuru tev patīk lasīt? Tikai daži faili, kas mitināti kāda cita datorā. Šī vietne, kurā lasāt šo rakstu (LocalMonero)? Faili un kods, kas kaut kur mitināts datorā. Pat lielas trakas vietnes darbojas šādā veidā. Ņemiet, piemēram, YouTube. Vienkārši video faili, kas tiek mitināti Google gigantiskajās datorsistēmās, un jūs izveidojat savienojumu ar tiem, lai lejupielādētu videoklipu savā datorā un varētu to skatīties.

Šie datori var atšķirt viens otru, jo katram datoram, kas ir savienots ar internetu, tiek piešķirts unikāls identifikācijas numurs, ko sauc par IP adresi. Parasti tās ir četras skaitļu kopas, kas atdalītas ar punktiem, piemēram: 172.66.35.7. Ir svarīgi to paturēt prātā, apsverot, kā Monero informācija tiek pārvietota internetā. Monero ir peer-to-peer tīkls (P2P), kas nozīmē, ka datori savienojas tieši viens ar otru, nevis izmanto starpnieku. Tātad, kad lietotāja pilnais mezgls lejupielādē jaunatklāto bloku, viņš to lejupielādē nevis no centrālā servera, bet gan no sev līdzīgiem. Negatīvā puse ir tāda, ka lietotāji savā starpā savienojas tieši, tāpēc viņi zina viens otra IP adreses.

Nu un tad? Tas ir tikai cipars, vai ne? Ne gluži. Pašas IP adreses satur informāciju par lietotāju, piemēram, izcelsmes valsti un tīkla pakalpojumu sniedzēju, bet, vēl ļaunāk, interneta pakalpojumu sniedzēji (ISP) zina katras personas, kas izmanto viņu pakalpojumus, IP adresi. Tas nozīmē, ka šie interneta pakalpojumu sniedzēji un tie, ar kuriem viņi strādā, var vērot lietotāja datu plūsmu un, izmantojot kādu gudru taktiku, atklāt, ka viņi izmanto Monero. Pirms jūs baidāties, ievērojiet tur esošo formulējumu. Viss, ko šie okšķeri var darīt, ir redzēt, ka persona izveido savienojumu ar citiem Monero tīkla mezgliem. Monero privātuma tehnoloģijas dēļ nekas cits par personu netiek nopludināts. Nevis par to, vai viņi palaiž mezglu vai ja/kad viņi nosūta pārskaitījumus, un, ja pārskaitījums tiek nosūtīts, nav zināma nekāda informācija par to. Šie interneta pakalpojumu sniedzēji var redzēt tikai to, ka viens no viņu lietotājiem veido savienojumu ar Monero tīklu.

Tagad dažiem cilvēkiem dažās vietās ar šo informāciju vien var pietikt, lai kaitētu reputācijai vai brīvībai. Vai varbūt doma par to, ka kāds jebkāda iemesla dēļ pārkāpj jūsu privātumu un redz, ko jūs darāt internetā, jums nav pieņemama. Šīs personas tiek mudinātas izveidot savienojumu ar Monero tīklu, tikai izmantojot VPN, Tor vai I2P, kas visi ir pakalpojumi, kas slēpj lietotāja IP adresi no citiem, kā arī slēpj to, ko lietotājs dara no sava ISP. Atšķirības starp šiem pakalpojumiem ir ārpus šī raksta jomas, taču par šo tēmu ir sarakstīts daudz augstas kvalitātes rakstu, tāpēc norūpējušies lietotāji tiek aicināti izpētīt tālāk!

Pārējiem no mums var šķist, ka tas, ka citi zina, ka esam pieslēgti Monero tīklam, nav liela muiža. Galu galā mūsu pārskaitījumu faktiskais saturs vai, ja mēs tos vispār sūtām, ir publiski paslēpts, un kāds ir kaitējums? Lai gan tā var būt taisnība, lietotāji tiek mudināti ņemt vērā faktu, ka galvenā kriptovalūtu ideja ir būt pašam savai bankai. Ja jums ir privātā atslēga un ar to kaut kas notiek, neviens nevar palīdzēt atgūt zaudētos līdzekļus.

Būt paša bankai nozīmē ņemt vērā ne tikai savu digitālo drošību, bet arī fizisko drošību. Ļoti iespējams, ka fakts, kad kāds pieslēdzas Monero tīklam, var piesaistīt nevēlamu uzmanību ne tikai no liela mēroga dalībniekiem kā valstu organizācijām, bet arī no mazākiem, ar savtīgām interesēm, piemēram, hakeriem, kas vēlas viegli nopelnīt. Visā šifrēšanas telpā patiešām ir neskaitāmi stāsti par šādiem scenārijiem, kas faktiski notiek.

Šis raksts nav paredzēts, lai iebiedētu, bet gan mudinātu lietotājus veikt kādu pētījumu par to, kādas tīmekļa sērfošanas aizsardzības metodes viņiem ir piemērotas. Labā ziņa ir tā, ka šīs prasmes ir pielietojamas arī vispārējai interneta lietošanai, ne tikai Monero lietojumam. Tādējādi mūsu pasaulē, kurā arvien vairāk kas tiek pieslēgts internetam, gudrs lietotājs nevar kļūdīties, uzkrājot atbilstošas zināšanas un prasmes, lai saglabātu drošību un patiesi būtu pats sava banka.

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