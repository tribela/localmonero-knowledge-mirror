---
title: "Monero mainošana: ar ko RandomX ir tik īpašs"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
2019\. gada 30. novembrī Monero tika veikts pusgada atzarojums (hard fork), un gaidītākās izmaiņas bija pāreja no vecā PoW algoritma Cryptonight uz pilnīgi jauno, iekšēji izstrādāto RandomX. Monero kopiena uzskata, ka RandomX ir liels solis ceļā uz vienlīdzīgāku ieguvi, taču paskatīsimies dziļāk, lai saprastu, vai tas tā ir.

## Mērķis

Lai spriestu, vai RandomX ir uzlabojums, mums vispirms ir jāsaprot, kāds ir mainošanas mērķis. Mainošana nodrošina blokķēdi pret dubultiem tēriņiem, izmantojot Nakamoto Consensus. Šajā rakstā neiedziļināsimies, kā tieši tas darbojas, taču to var uzzināt no daudz un dažādiem avotiem internetā. Svarīgi ir tas, ka drošību nodrošina datoru (maineru) ģenerētie hash, konkurējot savā starpā, lai atrastu matemātisko risinājumu, kas nepieciešams nākamā bloka izveidošanai. To darot, viņi blokķēdē pievieno jaunus pārskaitījumus. Apmaiņā pret darbu (pareizi iegūts hash) viņi saņem no jauna emitētās monētas.   
  
Ar šo iestatījumu var rasties vairākas problēmas. Lai tas pareizi darbotos, ir nepieciešami atbilstoši stimuli, taču mēs pievērsīsimies vienai konkrētai iespējamai problēmai. Ja mainošanai vajadzētu būt sacensībām, kas notiek, ja viens maineris iegūst priekšrocības?

## Atskats

Kontekstam parunāsim mazliet par mainošanas aparatūru. Maineri darba veikšanai izmanto datorus, taču mēs visi zinām, ka ne visi datori ir izgatavoti vienādi. Daži datori ir pietiekami jaudīgi, lai palaistu AI tīklus vai intensīvas spēles, savukārt citi cīnās ar pat vienkāršiem uzdevumiem. Šīs skaitļošanas jaudas atšķirības ietekmē arī hash rate jeb ātrumu, ar kādu tie meklē bloku risinājumus.   
  
Taču pat šīs atšķirības starp datoriem nobāl, salīdzinot ar specializētās aparatūras, ko citādi dēvē par specifiska pielietojuma integrētajām shēmām (ASIC), hash rate, kas vairākkārt pārspēj parastos datorus.  
  
Veltīsim kādu laiku, lai izpētītu, kas padara ASIC tik spēcīgus. Iedomājieties, ka visi datori atrodas kaut kur spektrā, kas svārstās no spējas izdarīt daudzas lietas, bet neko labi, līdz tikai vienas lietas veikšanai, bet ļoti labi. CPU un ASIC atrodas šī spektra pretējos galos.  
  
CPU, kas ir visos standarta datoros, atrodas pirmajā galā. Tie var veikt daudzas darbības, piemēram, pārlūkot tīmekli, spēlēt spēles vai renderēt video, taču nevienu no tām nedara īpaši labi. Šī elastība nāk uz efektivitātes rēķina.  
  
ASIC ir otrā galā, kur tie var darīt tikai vienu lietu, bet ar neticamu ātrumu. Viņi var veikt tikai vienu matemātisko funkciju, bet, tā kā viņi var ignorēt visu pārējo, veiktspējas pieaugums ir astronomisks. Tomēr šī efektivitāte maksā elastību, tāpēc, ja funkcija mainās pat nedaudz (piemēram, x + y = z mainās uz 2x + y = z), ASIC pārstās darboties pavisam.   
  
Ne visiem pieder ASIC, bet katram ir savs dators. Tas var radīt negodīgu priekšrocību.

## Jautra analoģija

Ja tas joprojām mulsina, iespējams, palīdzēs tālāk sniegtā līdzība. Iedomājieties loteriju, kurā katru stundu tiek piešķirts tūkstotis dolāru, un šī loterija ļauj jums izdrukāt biļetes pašam! Jūs sākat drukāt tik daudz biļešu, cik vien iespējams, izmantojot mājas printeri, kas var izdrukāt vienu biļeti sekundē. Atņemot elektrības un tintes izmaksas, jūs redzat, ka joprojām varat gūt peļņu, pat ja laimējat loterijā tikai reizi dažās nedēļās.  
  
Laika gaitā jūs paplašināt savu darbību, līdz jums ir visa telpa, kas veltīta printeriem. 20 kopā. Viss ir kārtībā...līdz vienai liktenīgai dienai.  
  
Ir lielas ziņas. Kāds ir izgudrojis jauna veida printeri. Tas var izdrukāt tikai loterijas biļetes. Tas nevar drukāt attēlus vai biroja dokumentus vai veikt abpusējo drukāšanu. Tikai loterijas biļetes. Bet tas var tās izdrukāt ar ātrumu 1000 biļetes sekundē. Jūs skatāties savā mazajā printeru istabā. 20 printeri. Jums ir nepieciešami vēl 980 printeri, lai neatpaliktu no VIENA no šiem monsterprinteriem, un, ja kādam ir divi…?  
  
Jūs diemžēl izstājaties no loterijas, jo vairs nevarat attaisnot elektrības un tintes izmaksas.  
  
Bet paga! Pēc pāris nedēļām ir jaunas ziņas! Biļetes dizains ir mainījies. Cipari, kas agrāk bija augšā, tagad ir apakšā. Jaunie monstru printeri ir tik neelastīgi, ka to nevar izdarīt. Viņi varēja izgatavot tikai iepriekšējo dizainu. Nepagāja ilgs laiks, kad jūs atkal laimīgi drukājat. Vismaz līdz brīdim, kad kāds uztaisīs jaunu monstru printeri jaunajam dizainam.

## RandomX

Kāda ir RandomX loma tajā visā? Tas cenšas izlīdzināt ASIC priekšrocības, padarot ASIC izveidi ļoti sarežģītu. Tas tiek darīts, pieprasot maineriem izveidot un izpildīt nejaušu kodu hashing vietā, pamatojoties uz algoritmu.  
  
Var būt mulsinoši, kā tas vispār kaut ko palīdz, tāpēc atgriezīsimies pie mūsu printera analoģijas. Atcerieties, kas notika, kad dizains mainījās? Vecie monstru printeri katru nakti novecoja, un bija jāizstrādā jauni, ņemot vērā jauno dizainu. Kas notiktu, ja katrai jaunai loterijas balvas biļetei būtu jāatbilst jaunam dizaina standartam katram jaunam džekpotam?   
  
Izveidot jaunu monstru printeri kļūtu neiedomājami grūti. Jūs vairs nevarat plānot tikai vienu biļetes dizainu. Tā kā dizains ir nejaušs, monstru printeru ražotājiem būtu jāpievieno krāsu iespējas, veidi, kā drukāt dažādus burtus, apmales un formas un daudz ko citu. Īsāk sakot, mašīna, kuru viņi izgudrotu, būtu standarta, parasts printeris. Tāpat kā visiem citiem.  
  
Vienkārši ieviešot šo nejaušību biļešu dizainā, mēs būtiski samazinājām lielo priekšrocību, ko guvām no specializētās aparatūras. RandomX dara to pašu, bet ar mainošanu.  
  
Tādā veidā tiek samazinātas priekšrocības, ko iegūst daži atlasīti turīgi cilvēki, jo, ja viņi iegulda “ASIC” izveidē RandomX ieguvei, viņi faktiski tikai izgudros spēcīgākus, labākus CPU, kas sniedz labumu visai pasaulei.  
  
Tas nozīmē, ka mazais puika ar saviem 20 biļešu printeriem ir atgriezies spēlē. Viņam joprojām var būt grūtāk, jo šīs bagātās personas joprojām var iegādāties vairāk printeru nekā viņš, taču vismaz tagad viņš nav pārspēts vairākkārt tikai no vienas iekārtas. Viņš ir konkurētspējīgs savā mazajā veidā.  
  
Zinot, ka pat mazais puika var būt konkurētspējīgs Monero mainošanā, mēs aicinām ikvienu to izmēģināt vai nu Monero GUI makā, kas atbalsta solo mainošanu, vai arī lejupielādējot kopienas uzturētu programmatūru. Tā ir vienkārša, konkurētspējīga un pieejama visiem.

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

  * [Kāpēc Monero ir labāks par Dash, Zcash, Zcoin (pat ar Lelantus), Grin un Bitcoin mikseriem, piemēram, Wasabi (atjaunināts 2020. gada maijā)](/knowledge/why-monero-is-better)/