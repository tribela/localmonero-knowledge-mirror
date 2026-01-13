---
title: "Kā Monero slepenās adreses aizsargā jūsu identitāti"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero ir ieviesis trīs veidu pieeju privātumam. Šīs tehnoloģijas ir [gredzenveida paraksti](/knowledge/ring-signatures), kas slēpj patieso izvadi (sūtītāju), RingCT, kas slēpj summas, un slepenās adreses, kas slēpj saņēmēju. Šodien mēs apspriedīsim pēdējo no minētajām tehnoloģijām: slepenās adreses.

Ir daudz iemeslu, kāpēc persona varētu vēlēties slēpt, kam viņi sūta. Mēs nekad nedrīkstam ļaut nevienam mēģināt mūs pārliecināt, ka visi piemēri ir nepatīkama uzvedība. Tādas lietas kā sūtīšana nepopulārai politiskai partijai, ziedošana labdarības organizācijām vai kādam, ko kultūra uzskata par “atceltu”, ir piemēri, kur var vēlēties slēpt savu tēriņu mērķi, baidoties no sekām, taču tie pēc būtības ir pilnīgi likumīgi.

Caurredzamā blokķēdē adreses, uz kurām tiek nosūtīti pārskaitījumi, ir redzamas visiem. Ir svarīgi ņemt vērā, ka, ja maineri paši nepiekrīt, kur nauda nonāk, viņi var izvēlēties to neiekļaut blokā, efektīvi cenzējot šo pārskaitījumu uz šķietami cenzūras izturīgas platformas. Vienīgais veids, kā šo, protams, maz ticamo cenzūru padarīt neiespējamu, ir tad, ja maineri nevar atšķirt pārskaitījumus, jo visi ķēdes metadati tiek aizēnoti ar dažādiem līdzekļiem. Kaut kas, ar ko Monero ir pazīstams.

Monero atrisina šo caurredzamo adrešu problēmu, ieviešot slepenās adreses — tehnoloģiju, kuru Bitcoin Talk foruma lietotājs ByteCoin 2011. gadā sākotnēji izveidoja Bitcoin (saistība ar Bytecoin, kas vēlāk integrētu slepenās adreses, nav zināma). Tomēr pašreizējai slepeno adrešu formai ir vairāki uzlabojumi salīdzinājumā ar sākotnējo ideju. Bet vispirms, lai redzētu, kā tie darbojas, parunāsim par taustiņiem.

Ir grūti atrasties kriptovalūtas telpā un nedzirdēt par atslēgām. Frāzes, piemēram, “dublēt savu privāto atslēgu”, ir izplatītas, taču, kad vidusmēra Džo dzird vārdus “publiskā atslēga” un “privātā atslēga”, viņš nobīstas un domā, ka tas būs pārāk tehniski un mulsinoši, lai to saprastu. Bet neuztraucieties. Mēs to darīsim lēni un izmantosim daudz piemēru.

Kriptovalūtās izmantotās divu veidu atslēgas, kā tikko minēts, ir publiskās un privātās. Šīs divas atslēgas parasti ir pārī, kas nozīmē, ka noteikta publiskā un privātā atslēga ir savstarpēji saistītas. Faktiski parasti publiskā atslēga tiek atvasināta no privātās atslēgas, kas nozīmē, ka, ja zināt privāto atslēgu, jūsu maciņš var veikt gudrus aprēķinus un katru reizi izdomāt pareizo publisko atslēgu.

Kā norāda nosaukumi, publiskā atslēga var būt publiska bez sekām. Parasti tā ir daļa no adreses, kuru kopīgojat, lai saņemtu naudu savā kriptovalūtas makā. Savukārt privātā atslēga ir tāda, kuru nevajadzētu kopīgot. Tā ir lieta, kas ļauj parakstīt un veikt pārskaitījumu, tādēļ, ja tā tiek nozagta vai tiek koplietota, nelietīga trešā puse var tērēt jūsu naudu.

Vienkārša līdzība tam būtu piekaramā slēdzene un atslēga, kas nepieciešama tās atbloķēšanai. Atvērto piekaramo slēdzeni var brīvi koplietot, un ar šo piekaramo slēdzeni var aizslēgt jebko, taču tikai tas, kuram ir atslēga, var atvērt jebko, kam piekārtā slēdzene ir aizvērta. Piekaramo slēdzeni var kopēt un koplietot, bet ar atslēgu tā nedrīkst notikt.

Šīs atslēgas parasti tiek abstrahētas no lietotāja, tāpēc jūs tās nekad neredzat. Monero tie nemaz neparādās kā biedējoša burtu un ciparu virkne. Monero parastais lietotājs privāto atslēgu zina kā savu sēklu. Sēkla (kas jums vajadzētu pierakstīt, ja neesat to izdarījis) patiesībā ir tikai cilvēkam lasāma privātā atslēga. 

Redzat? Galu galā nav tik biedējoši. Atpakaļ uz slepenajām adresēm.

Kā minēts iepriekš, slepenās adreses sākotnēji netika izveidotas Monero, bet gan Bitcoin. Tomēr, tāpat kā lielākajā daļā jauno ideju, arī te pirmajā mēģinājumā bija problēmas. Nākamais mēģinājums notika, kad Nikolass van Saberhāgans CryptoNote izveidoja Bytecoin, Monero priekštecim ([skatiet mūsu Monero un Bytecoin vēsturi šeit](/knowledge/monero-history)), un, lai gan tas bija nepārprotams uzlabojums salīdzinājumā ar oriģinālu, pat tam bija daži niansēti trūkumi.

Galu galā, izstrādātājs izveidoja vienu pēdējo iterāciju citai, privātuma kriptovalūtai, kura vairs nav pieejama, un ar šo ideju tika novērstas neatrisinātās privātuma un drošības problēmas. Tas galu galā nokļuva Monero, un tas tiek izmantots mūsdienās.

Lai gan šīs privātuma un drošības problēmas tika atrisinātas, pašas slepenās adreses pievienoja blokķēdes tehnoloģijām atšķirīgu dīvainību, kas iepriekš nepastāvēja. Nepieciešamība skenēt. Tā kā saņemšanas adreses blokķēdē netiek publiski parādītas, saņēmējs nekad nezina, vai kāds konkrētais pārskaitījums pieder viņam, tāpēc viņam ir jāskenē visi ienākošie pārskaitījumi ar savu privāto atslēgu, lai noskaidrotu, vai tie ir viņa.

Izmantojot caurredzamas monētas, viņiem atliek tikai pārbaudīt, vai uz jūsu adresi tiek nosūtīts pārskaitījums. Vienkāršs jā vai nē jautājums. Taču, izmantojot slepenas adreses, katrs pārskaitījums var būt tāds, kas jums tiek nosūtīts, tāpēc jums ir jāmēģina katru atbloķēt ar savu privāto atslēgu, lai redzētu, vai tā tiek atvērta.

Šis ir papildu solis, kas nav Bitcoin un tā atvasinājumos, un padara sākotnējo maka iestatīšanu, kā arī sinhronizāciju daudz ilgāku nekā Bitcoin, ja neesat to atvēris kādu laiku. Tomēr kompromiss ir nepieciešams, lai būtu iespējamas šīs privātuma garantijas. Jāatzīmē, ka atšķirībā no privātuma trijzara vājākā punkta, gredzenveida parakstiem, slepenās adreses nav pakļautas heiristikai. Tās balstās uz pārbaudītu un stabilu eliptiskās līknes kriptogrāfiju, uz kuru paļaujas viss internets un kuras salaušana nozīmētu datoru drošības izbeigšanu kopumā, ne tikai Monero.

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