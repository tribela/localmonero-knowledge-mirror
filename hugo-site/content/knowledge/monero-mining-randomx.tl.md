---
title: "Monero Mining: Ano ang Nagiging Espesyal sa RandomX"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Noong ika-30 ng Nobyembre, 2019, nagkaroon ng kalahating taon na hard fork ang Monero, na ang pinakainaasahang pagbabago ay ang paglipat mula sa lumang PoW algorithm, cryptonight, patungo sa ganap na bago, panloob na binuo, ang RandomX. Naniniwala ang komunidad ng Monero na ang RandomX ay isang malaking hakbang patungo sa egalitarian na pagmimina, ngunit humukay tayo ng mas malalim upang makita kung iyon ang kaso.

## Layunin

Upang hatulan kung ang RandomX ay isang pagpapabuti, kailangan muna nating maunawaan kung ano ang layunin ng pagmimina. Tinitiyak ng pagmimina ang isang blockchain mula sa dobleng paggastos sa pamamagitan ng Nakamoto Consensus. Ang mga eksaktong intricacies ng kung paano ito ginagawa ay lampas sa saklaw ng artikulong ito, ngunit maaari silang matutunan mula sa maraming iba't ibang mga mapagkukunan sa internet. Ang mahalaga ay ang seguridad ay nagmumula sa mga hash na nabuo ng mga computer (mga minero), sa kumpetisyon sa isa't isa upang mahanap ang mathematical na solusyon na kinakailangan upang lumikha ng isa pang block. Habang ginagawa nila ito, nagdaragdag sila ng mga bagong transaksyon sa blockchain. Bilang kapalit ng kanilang trabaho (hashes) sila ay binabayaran ng mga bagong gawang barya.   
  
Mayroong ilang mga isyu na maaaring mangyari sa setup na ito, at nangangailangan ang mga ito ng mga wastong insentibo upang gumana nang tama, ngunit kami ay magtutuon sa isang partikular na problema na maaaring lumitaw. Kung ang pagmimina ay dapat na isang kompetisyon, ano ang mangyayari kapag ang isang minero ay nakakuha ng isang kalamangan?

## Background

Para sa konteksto, pag-usapan natin ang tungkol sa pagmimina ng hardware. Gumagamit ang mga minero ng mga computer para gawin ang trabaho, ngunit alam nating lahat na hindi lahat ng computer ay ginawang pantay. Ang ilang mga computer ay sapat na makapangyarihan upang magpatakbo ng mga network ng AI o matinding laro, habang ang iba ay nahihirapan kahit na sa mga simpleng gawain. Ang mga pagkakaibang ito sa computing power ay nakakaapekto rin sa hash rate, o ang rate kung saan sila naghahanap ng mga block solution.   
  
Ngunit kahit na ang mga pagkakaibang ito sa pagitan ng mga computer ay namumutla kung ihahambing sa mga hash rate ng espesyal na hardware, kung hindi man ay kilala bilang Application Specific Integrated Circuits (ASICs), na mas mataas kaysa sa mga regular na computer sa ilang mga order ng magnitude.  
  
Maglaan tayo ng ilang oras upang tuklasin kung bakit napakalakas ng ASIC. Isipin na ang lahat ng mga computer ay nahuhulog sa isang lugar sa isang spectrum, na mula sa kakayahang gumawa ng maraming bagay, ngunit walang maayos, hanggang sa paggawa lamang ng isang bagay, ngunit ginagawa ito nang napakahusay. Ang mga CPU at ASIC ay nasa magkabilang dulo ng spectrum na ito.  
  
Ang mga CPU na nasa lahat ng karaniwang computer ay nasa unang dulo. Maaari silang gumawa ng maraming bagay, tulad ng pag-browse sa web, paglalaro, o pag-render ng video, ngunit hindi nila magawa ang alinman sa mga ito nang mahusay. Ngunit ang kakayahang umangkop na ito ay dumating sa halaga ng kahusayan.  
  
Ang mga ASIC ay nasa kabilang dulo, kung saan maaari lamang nilang gawin ang isang bagay, ngunit gawin ito sa isang hindi kapani-paniwalang bilis. Maaari lamang silang magsagawa ng isang mathematical function, ngunit dahil maaari nilang balewalain ang lahat ng iba pa, ang mga nadagdag sa pagganap ay astronomical. Gayunpaman, ang kahusayan na ito ay dumating sa halaga ng kakayahang umangkop, kaya kung ang function ay nagbabago kahit na bahagyang - isang halimbawa ay ang x + y = z ay nagbabago sa 2x + y = z - kung gayon ang ASIC ay titigil sa paggana nang buo.   
  
Hindi lahat ay nagmamay-ari ng ASIC, ngunit lahat ay nagmamay-ari ng mga computer. Ito ay maaaring humantong sa isang hindi patas na kalamangan.

## Isang masayang pagkakatulad

Kung ito ay nakalilito pa rin, marahil ang sumusunod na pagkakatulad ay makakatulong. Isipin ang isang lottery kung saan ang isang libong dolyar ay iginawad bawat oras, at ang lottery na ito ay nagpapahintulot sa iyo na mag-print ng iyong sariling mga tiket! Magsisimula kang mag-print ng maraming mga tiket hangga't maaari sa iyong printer sa bahay, na maaaring mag-print ng isang tiket bawat segundo. Pagkatapos ibawas ang mga gastos sa kuryente at tinta, makikita mo na maaari ka pa ring kumita, kahit na isang beses ka lang manalo sa lottery bawat ilang linggo.  
  
Sa paglipas ng panahon, pinalawak mo ang iyong operasyon hanggang sa magkaroon ka ng isang buong silid na nakatuon sa mga printer. 20 lahat. Maayos ang lahat...hanggang sa isang nakamamatay na araw.  
  
May malaking balita. May nag-imbento ng bagong uri ng printer. Maaari lamang itong mag-print ng mga tiket sa lottery. Hindi ito makakapag-print ng mga larawan, o mga dokumento sa opisina, o makakagawa ng double sided printing. Mga lottery ticket lang. Ngunit maaari itong i-print ang mga ito sa rate na 1000 tiket bawat segundo. Tumingin ka sa iyong maliit na silid ng printer. 20 printer. Kailangan mo ng 980 pang printer para lang makasabay sa ISA sa mga halimaw na printer na ito, at kung mayroong dalawa...?  
  
Nakalulungkot kang umalis sa laro ng lottery dahil hindi mo na mabibigyang-katwiran ang mga gastos sa kuryente at tinta.  
  
Ngunit sandali! Makalipas ang ilang linggo, marami pang balita! Ang disenyo ng tiket ay nagbago. Ngayon ang mga numero, na dati ay nasa itaas, ngayon ay nasa ibaba. Ang mga bagong halimaw na printer ay napaka-inflexible na hindi nila ito magagawa. Maaari lamang nilang gawin ang nakaraang disenyo. Hindi nagtagal at muli kang masaya na nagpi-print. Hindi bababa sa hanggang sa may gumawa ng bagong halimaw na printer para sa bagong disenyo.

## RandomX

Saan nababagay ang RandomX sa lahat ng ito? Ito ay naglalayong papantayin ang bentahe ng mga ASIC sa pamamagitan ng paggawa ng mga ASIC na napakahirap gawin. Ginagawa ito sa pamamagitan ng pag-aatas sa mga minero na gumawa at magsagawa ng random na code bilang kapalit ng pag-hash batay sa isang algorithm.  
  
Maaaring nakakalito kung paano ito nakakatulong sa anumang bagay, kaya bumalik tayo sa aming pagkakatulad sa printer. Tandaan kung ano ang nangyari noong nagbago ang disenyo? Ang mga lumang halimaw na printer ay nagiging lipas na gabi-gabi, at ang mga bago ay kailangang gumawa ng bagong disenyo sa isip. Ano ang mangyayari kung ang bawat bagong tiket ng premyong lottery, ay kailangang sumunod sa isang bagong pamantayan ng disenyo para sa bawat bagong jackpot?   
  
Ang paglikha ng bagong halimaw na printer ay magiging napakahirap. Hindi ka na maaaring magplano sa isang disenyo ng tiket. Dahil random ang disenyo, ang mga gumagawa ng halimaw na printer ay kailangang magdagdag ng mga kakayahan sa kulay, mga paraan upang mag-print ng iba't ibang titik at mga hangganan at mga hugis at higit pa. Sa madaling salita, ang makina na kanilang natapos sa pag-imbento ay magiging isang karaniwang, regular na printer. Tulad ng mayroon ang iba.  
  
Sa simpleng pagpapatupad ng randomness na ito sa disenyo ng ticket, nabawasan namin nang husto ang malaking kalamangan na nakuha mula sa espesyal na hardware. Gayon din ang ginagawa ng RandomX, ngunit sa pagmimina.  
  
Sa ganitong paraan, ang mga pakinabang na natamo ng ilang piling mayayamang tao ay nababawasan, na parang namumuhunan sila sa paglikha ng "ASIC" para sa pagmimina ng RandomX, sila ay talagang mag-iimbento lamang ng mas malakas, mas mahuhusay na CPU, na nakikinabang sa buong mundo.  
[ X1455X] Nangangahulugan ito na ang maliit na lalaki kasama ang kanyang 20 printer ng tiket ay bumalik sa laro. Maaaring nahihirapan pa rin siya dahil ang mayayamang indibidwal na ito ay maaari pa ring bumili ng mas maraming printer kaysa sa kanya, ngunit hindi bababa sa ngayon ay hindi siya nahihigitan ng mga order ng magnitude mula lamang sa isang makina. Siya ay mapagkumpitensya sa kanyang maliit na paraan.  
  
Alam na kahit ang maliit na tao ay maaaring maging mapagkumpitensya sa pagmimina ng Monero, hinihikayat namin ang lahat na bigyan ito ng pag-ikot, alinman sa Monero GUI wallet, na may suporta para sa solong pagmimina, o sa pamamagitan ng pag-download ng software na pinapanatili ng komunidad. Ito ay madali, mapagkumpitensya, at bukas sa lahat.

Karagdagang pagbabasa

  * [Paano natatanging pinapagana ng Monero ang mga circular na ekonomiya](/knowledge/monero-circular-economies)/

  * [Ang mga ring signature ni Monero vs CoinJoin tulad ng sa Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Bakit (at paano!) dapat mong hawakan ang sarili mong mga susi](/knowledge/hold-your-keys)/

  * [Nag-aambag pabalik sa Monero](/knowledge/contributing-to-monero)/

  * [Paano nakakaapekto ang malalayong node sa privacy ni Monero](/knowledge/remote-nodes-privacy)/

  * [Paano gumagamit si Monero ng mga hard-forks para i-upgrade ang network](/knowledge/network-upgrades)/

  * [Tingnan ang mga tag: Paano babawasan ng isang byte ang mga oras ng pag-sync ng Monero wallet ng 40%+](/knowledge/view-tags-reduce-monero-sync-time)/

  * [Ang P2Pool at ang Tungkulin Nito sa Desentralisasyon ng Monero Mining](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Ano ang Gagawin Nito para kay Monero](/knowledge/seraphis-for-monero)/

  * [Ang Pag-convert ba ng Bitcoin sa Monero ay Kasing Pribado ng Direktang Pagbili ng Monero?](/knowledge/most-private-way-to-buy-monero)/

  * [Bakit Gumagamit ang Monero ng Walang Tiwala na Setup Hindi Gaya ng Zcash](/knowledge/monero-trustless-setup)/

  * [Bakit Mas Mabuting Tindahan ng Halaga ang Monero kaysa sa Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Paano Malalampasan ng Monero ang Mga Epekto ng Network ng Bitcoin](/knowledge/network-effect)/

  * [Bakit Ang Monero ang May Pinaka Kritikal na Pag-iisip na Komunidad](/knowledge/critical-thinking)/

  * [Mga Scam na Dapat Abangan Kapag Gumagamit ng Monero](/knowledge/monero-scams)/

  * [Paano Gumagana ang Atomic Swaps sa Monero](/knowledge/monero-atomic-swaps)/

  * [Ang Kailangang Malaman ng Bawat Gumagamit ng Monero Pagdating sa Networking](/knowledge/monero-networking)/

  * [Paano Itinatago ng RingCT ang Mga Halaga ng Transaksyon ng Monero](/knowledge/monero-ringct)/

  * [Paano Pinoprotektahan ng Monero Stealth Address ang Iyong Pagkakakilanlan](/knowledge/monero-stealth-addresses)/

  * [Paano Pinipigilan ng Monero Subaddresses ang Pag-uugnay ng Pagkakakilanlan](/knowledge/monero-subaddresses)/

  * [Ipinaliwanag ang Mga Output ng Monero](/knowledge/monero-outputs)/

  * [Pinakamahuhusay na Kasanayan sa Monero para sa Mga Nagsisimula](/knowledge/monero-best-practices)/

  * [Paano Tinatago ng Mga Lagda ng Ring ang Mga Output ni Monero](/knowledge/ring-signatures)/

  * [Paano Nalutas ni Monero ang Problema sa Laki ng Bloke na Sinasalot ang Bitcoin](/knowledge/dynamic-block-size)/

  * [Paano Mapapabuti ng CLSAG ang Efficiency ng Monero](/knowledge/what-is-clsag)/

  * [Bakit May Tail Emission ang Monero](/knowledge/monero-tail-emission)/

  * [Isang Maikling Kasaysayan ng Monero](/knowledge/monero-history)/

  * [Ang Wired Magazine ay Mali Tungkol kay Monero, Narito Kung Bakit](/knowledge/wired-article-debunked)/

  * [Nangungunang 15 Monero Myths and Concerns Debunked](/knowledge/monero-myths-debunked)/

  * [Paano Pinapanatili ng Dandelion++ na Pribado ang Pinagmulan ng Transaksyon ni Monero](/knowledge/monero-dandelion)/

  * [Bakit Open Source At Desentralisado ang Monero](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Bakit Mas Mahusay ang Monero kaysa Dash, Zcash, Zcoin (Kahit na may Lelantus), Grin at Bitcoin Mixers Like Wasabi (Na-update Mayo 2020)](/knowledge/why-monero-is-better)/