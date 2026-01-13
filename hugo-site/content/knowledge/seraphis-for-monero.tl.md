---
title: "Seraphis: Ano ang Gagawin Nito para kay Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: isang modular na pag-upgrade ng disenyo para sa mga transaksyong Monero

Inilalarawan ng post na ito ang [Seraphis](https://github.com/UkoeHB/Seraphis), isang hanay ng mga istruktura ng protocol ng transaksyon at abstraction na binuo ng pseudonymous research contributor [`koe`](https://github.com/UkoeHB) para sa Monero ecosystem, at may patuloy na pagsusuri sa seguridad ng pseudonymous contributor [`coinstudent2048`](https://github.com/coinstudent2048).  
Gumagawa kami ng ilang pagpapasimple at tinanggal ang ilang teknikal na detalye para sa kalinawan; para sa kadahilanang ito, at dahil ang disenyo ng Seraphis ay isinasagawa pa rin, ang mga interesadong mambabasa ay dapat sumangguni sa dokumentasyon ng Seraphis para sa pinaka-up-to-date na impormasyon.

## Mga transaksyon sa Monero

Ang mga protocol tulad ng Bitcoin at Monero at iba pa ay umaasa sa tinatawag na "output model" ng operasyon, kung saan ang _output_ ay isang representasyon ng halaga na maaaring ilipat.  
Ang mga transaksyon ay gumagamit ng isa o higit pang mga output na kinokontrol ng isang nagpadala, at bumubuo ng mga bagong output na nakadirekta sa mga tatanggap (o pabalik sa nagpadala bilang pagbabago); dapat balanse ang transaksyon sa mga natupok na output ay dapat maglaman ng kabuuang halaga na eksaktong katumbas ng halaga sa mga bagong output (kasama ang bayad na ipinataw ng network).  
Sa maraming mga protocol tulad ng Bitcoin, ang halaga na nilalaman sa isang output ay nakasulat sa malinaw, pati na rin ang tatanggap.  
Higit pa rito, sa pamamagitan ng pagtingin sa blockchain, ito ay walang halaga upang makita kung at kailan ang isang output ay nagastos (iyon ay, kung ito ay natupok sa isang susunod na transaksyon, at kung aling transaksyon ang gumastos nito).

Sa kabilang banda, ang mga protocol tulad ng Monero ay nagpapakilala ng ibang disenyo:

  * Ang mga halaga ng output ay nakatago at hindi nakikita sa blockchain
  * Ang mga address ng tatanggap ay nakatago sa pamamagitan ng paggamit ng isang beses na addressing protocol
  * Natatakpan man o hindi ang isang output dahil sa paggamit ng mga hindi malinaw na lagda

Ang resulta ay, kung wala ang panlabas na impormasyon, mahirap matukoy kung ang isang naibigay na output ay nagastos, kung ano ang halaga nito, at kung sino ang tatanggap nito.

Ang kasalukuyang protocol ng transaksyon ng Monero ay tinatawag na _RingCT_ , at gumagamit ng ilang cryptographic na mga bloke ng gusali upang makamit ang mga layuning ito sa disenyo.

Ang 
  * _Commitments_ ay nagtatago ng mga halaga sa isang mathematically-useful na paraan
Pinipigilan ng 
  * _Mga range proof_ ang pag-apaw na maaaring magpalaki ng supply
  * _Ang mga naka-link na pirma ng singsing_ ay nagbibigay ng kalabuan ng lumagda at pinipigilan ang mga pagtatangka ng dobleng paggastos
Iginiit ng 
  * _Mga pag-offset sa pangako_ na balanse ang mga transaksyon

Ang mga building block na ito ay maingat na magkakaugnay upang bumuo ng RingCT protocol.

Ang isang kapaki-pakinabang na katangian ng RingCT protocol ay ang ilang mga bloke ng gusali ay maaaring baguhin o i-upgrade sa paraang mapanatiling buo ang pangkalahatang disenyo at mga katangian, ngunit maaari itong magbigay ng kahusayan o mga pagpapabuti sa seguridad. Sa katunayan, ang mga ganitong uri ng pag-upgrade ay naganap (o binalak na mangyari) nang ilang beses sa kasaysayan ni Monero. Ang mga patunay ng saklaw sa orihinal na RingCT protocol ay malaki at mabagal; kalaunan ay na-update ang mga ito sa isang construction na tinatawag na [Bulletproofs](https://eprint.iacr.org/2017/1066) na ginawang mas maliit at mas mabilis ang mga transaksyon na may mas mahusay na pagsusuri sa seguridad, at binalak na ma-update sa isang mas bagong construction na tinatawag na [Bulletproofs+](https://eprint.iacr.org/2020/735) para sa mas malaking benepisyo sa kahusayan. 

Isang katulad na proseso ang isinailalim sa linkable ring signature building block. Sa orihinal na protocol, ginamit ang isang construction na tinatawag na [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34). Na-update ito sa ibang pagkakataon sa isang mas bagong construction na tinatawag na [CLSAG](https://eprint.iacr.org/2019/654) na mas mabilis, nagreresulta sa mas maliliit na transaksyon, at may mas mahusay na pagsusuri sa seguridad. Iminungkahi ang isang mas bagong linkable ring signature construction batay sa [Triptych](https://eprint.iacr.org/2020/018), ngunit hindi ito pinili para sa deployment dahil sa mga epekto nito sa mga multisignature na operasyon.

## Seraphis

Isinasagawa ni Seraphis ang ideyang ito nang higit pa.  
Sa halip na i-update ang mga indibidwal na building block ng kasalukuyang RingCT transaction protocol, nagpapakilala ito ng ibang protocol na maaaring samantalahin ang iba't ibang building block at mag-alok ng pinahusay na functionality.

## Mga bloke ng gusali

Gumagamit si Seraphis ng ibang hanay ng mga cryptographic building blocks para makamit ang mga layunin nito sa disenyo.

  * _Ang mga pangako_ ay nagtatago pa rin ng mga halaga
Pinipigilan pa rin ng 
  * _Range proof_ ang pag-apaw at supply ng inflation
  * _Ang mga patunay ng membership_ ay nagbibigay ng kalabuan ng lumagda
  * _Ang mga pag-offset sa pangako_ ay iginigiit pa rin ang balanse
  * _Ang pagpapahintulot sa mga patunay_ ay pumipigil sa mga pagtatangka sa dobleng paggastos

Pansinin ang pagbabago dito: ang mga naka-link na pirma ng singsing ay pinapalitan ng kumbinasyon ng mga patunay ng pagiging miyembro at mga patunay na nagpapahintulot. Sa halos pagsasalita, ang mga patunay ng membership ay nagpapakita na ang isang natupok na output ay bahagi ng isang mas malaking hanay, katulad ng kung ano ang nangyayari sa RingCT. Ngunit hindi tulad ng RingCT, ang mga patunay ng membership ay hindi nagsasangkot ng pag-link na tag sa lahat! Ipinapakita ng mga patunay sa pagpapahintulot na wasto ang tag ng pag-link at ginagamit ito para lagdaan ang huling transaksyon.

Dahil inilalagay ng RingCT ang nagli-link na tag sa hindi malinaw na lagda, ang mga pagpapatakbo ng pag-sign (at multisignature) ay mas masinsinang computation, at nagiging mas mahirap na bumuo ng iba pang functionality na nauugnay sa tag. Ngunit sa Seraphis, ang pagbuo ng mga patunay ng membership ay maaaring ligtas na maitalaga mula sa mga pinagkakatiwalaang device (na maaaring may limitadong kapangyarihan sa pag-compute, tulad ng isang hardware wallet) sa isang hindi gaanong pinagkakatiwalaang device, at ang mga pagpapatakbo ng pag-sign (at multisignature) ay mas madali gamit ang mas simpleng patunay na nagbibigay-daan sa iyo. .

Sa kabutihang palad, ang ilan sa mga bloke ng gusali na kinakailangan ng Seraphis ay umiiral na sa ibang lugar, at hindi na kailangang idisenyo mula sa simula. Parehong ang mga Bulletproof at Bulletproofs+ na mga konstruksyon ay maaaring gamitin bilang mga range proof. Maaaring gamitin ang mga pagbabago sa Schnorr-type proving system para sa pagpapahintulot ng mga patunay. At isang mahusay na [proving system](https://eprint.iacr.org/2015/643) na ginamit na bilang batayan para sa Triptych, [Lelantus](https://eprint.iacr.org/2019/373), at [Spark](https://eprint.iacr.org/2021/1173)* ay maaaring mabago para sa mga patunay ng membership. X2127X] 

* Tumatanggap ang Cypher Stack ng pagpopondo para sa pagpapaunlad ng Spark.

* Tumatanggap ang Cypher Stack ng pagpopondo para sa pagpapaunlad ng Spark.

## Pag-address

Sa kasamaang palad, ang mga Monero address na kasalukuyang ginagamit ay hindi tugma sa Seraphis. Kakailanganin ng mga user na bumuo ng mga bagong address mula sa kanilang mga wallet key upang makatanggap ng Monero kung ipinatupad ang Seraphis. Gayunpaman, ang gastos sa ecosystem na ito ay may kasamang maraming benepisyo.

Bukod sa mga benepisyo sa istruktura na tinalakay sa itaas, ang disenyo ng Seraphis ay pumapayag sa maraming iba't ibang posibilidad sa pagtatayo ng address, na bawat isa ay may mga tradeoff. Habang ang huling pagtatayo ng address na gagamitin sa Seraphis ay [pa rin ang pinagpasyahan](https://github.com/monero-project/research-lab/issues/92) (isang scheme na nakakatanggap ng maraming atensyon ay tinatawag na [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), maaari naming ilarawan ang ilang karaniwan at kapaki-pakinabang na mga tampok.

Maaaring alam mo na ang mga Monero address ay nag-aalok ng _view key_ functionality, kung saan maaari kang magbigay ng view key sa isang device o third party at payagan itong manood ng mga papasok na output sa ngalan mo, ngunit hindi sumusuko sa paggastos awtoridad. Ito ay kapaki-pakinabang para sa mga wallet, na maaaring manatiling updated habang pinapanatiling ligtas na naka-lock ang iyong key ng paggastos. Kapaki-pakinabang din ito para sa mga kaso kung saan gusto mo ng access sa panlabas na view, tulad ng isang pampublikong kawanggawa na nag-aalok ng transparency o isang kumpanyang may departamento ng accounting.

Ang downside sa Monero view key ay hindi sila nagbibigay ng kumpleto o pinong access sa view. Hindi posible na mapagkakatiwalaang matukoy kapag ang isang wallet ay gumastos ng mga pondo, na nagpapahirap sa pagkalkula ng mga balanse ng wallet nang maayos kapag ang key ng paggastos ay hindi magagamit. Kasalukuyang hindi rin posible na matukoy ang mga papasok na output nang hindi rin natututo ang halagang nilalaman ng mga output na iyon (na nangangahulugang anumang mga third-party na responsable sa paghahanap ng mga papasok na output ay eksaktong matututo kung gaano karaming Monero ang iyong nakukuha).

Mareresolba ito ng Seraphis addressing constructions. Sa Seraphis, nilagyan ang iyong address ng iba't ibang mga susi na maaaring gumawa ng iba't ibang bagay:

  * Abangan ang mga papasok na output, ngunit itago ang halaga ng mga ito
  * Abangan ang mga papasok na output, ngunit ipakita ang halaga ng mga ito
  * Abangan ang mga papalabas na output
  * Tulungan kang bumuo ng mga transaksyon, ngunit huwag lagdaan ang mga ito
  * Bumuo ng mga bagong address (kapaki-pakinabang para sa mga retailer o pakikipagpalitan sa maraming customer)

Bilang may hawak ng address, ikaw ang magpapasya kung gaano kalaki ang awtoridad na ibibigay mo sa iba pang device o third party.

## Ang malaking larawan

Ang Seraphis ay isang malaking pagbabago sa Monero ecosystem. Bagama't nagsasangkot ito ng mga pagbabago sa mga address at mga bloke ng pagbuo ng transaksyon, ang disenyo nito ay nag-aalok ng flexibility at kapaki-pakinabang na functionality na hindi posible sa RingCT protocol ngayon. Bagama't ang karamihan sa disenyo ay tinatapos at ginagawang [isang pagpapatupad](https://github.com/UkoeHB/monero/tree/seraphis_lib), ang disenyo ng address at pagsusuri sa seguridad ay nagpapatuloy. Nag-aalok ang Seraphis ng magandang pagkakataon para itulak ang Monero ecosystem pasulong!

Karagdagang pagbabasa

  * [Paano natatanging pinapagana ng Monero ang mga circular na ekonomiya](/knowledge/monero-circular-economies/)

  * [Ang mga ring signature ni Monero vs CoinJoin tulad ng sa Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Bakit (at paano!) dapat mong hawakan ang sarili mong mga susi](/knowledge/hold-your-keys/)

  * [Nag-aambag pabalik sa Monero](/knowledge/contributing-to-monero/)

  * [Paano nakakaapekto ang malalayong node sa privacy ni Monero](/knowledge/remote-nodes-privacy/)

  * [Paano gumagamit si Monero ng mga hard-forks para i-upgrade ang network](/knowledge/network-upgrades/)

  * [Tingnan ang mga tag: Paano babawasan ng isang byte ang mga oras ng pag-sync ng Monero wallet ng 40%+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [Ang P2Pool at ang Tungkulin Nito sa Desentralisasyon ng Monero Mining](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Ang Pag-convert ba ng Bitcoin sa Monero ay Kasing Pribado ng Direktang Pagbili ng Monero?](/knowledge/most-private-way-to-buy-monero/)

  * [Bakit Gumagamit ang Monero ng Walang Tiwala na Setup Hindi Gaya ng Zcash](/knowledge/monero-trustless-setup/)

  * [Bakit Mas Mabuting Tindahan ng Halaga ang Monero kaysa sa Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Paano Malalampasan ng Monero ang Mga Epekto ng Network ng Bitcoin](/knowledge/network-effect/)

  * [Bakit Ang Monero ang May Pinaka Kritikal na Pag-iisip na Komunidad](/knowledge/critical-thinking/)

  * [Mga Scam na Dapat Abangan Kapag Gumagamit ng Monero](/knowledge/monero-scams/)

  * [Paano Gumagana ang Atomic Swaps sa Monero](/knowledge/monero-atomic-swaps/)

  * [Ang Kailangang Malaman ng Bawat Gumagamit ng Monero Pagdating sa Networking](/knowledge/monero-networking/)

  * [Paano Itinatago ng RingCT ang Mga Halaga ng Transaksyon ng Monero](/knowledge/monero-ringct/)

  * [Paano Pinoprotektahan ng Monero Stealth Address ang Iyong Pagkakakilanlan](/knowledge/monero-stealth-addresses/)

  * [Paano Pinipigilan ng Monero Subaddresses ang Pag-uugnay ng Pagkakakilanlan](/knowledge/monero-subaddresses/)

  * [Ipinaliwanag ang Mga Output ng Monero](/knowledge/monero-outputs/)

  * [Pinakamahuhusay na Kasanayan sa Monero para sa Mga Nagsisimula](/knowledge/monero-best-practices/)

  * [Paano Tinatago ng Mga Lagda ng Ring ang Mga Output ni Monero](/knowledge/ring-signatures/)

  * [Paano Nalutas ni Monero ang Problema sa Laki ng Bloke na Sinasalot ang Bitcoin](/knowledge/dynamic-block-size/)

  * [Paano Mapapabuti ng CLSAG ang Efficiency ng Monero](/knowledge/what-is-clsag/)

  * [Bakit May Tail Emission ang Monero](/knowledge/monero-tail-emission/)

  * [Isang Maikling Kasaysayan ng Monero](/knowledge/monero-history/)

  * [Ang Wired Magazine ay Mali Tungkol kay Monero, Narito Kung Bakit](/knowledge/wired-article-debunked/)

  * [Nangungunang 15 Monero Myths and Concerns Debunked](/knowledge/monero-myths-debunked/)

  * [Paano Pinapanatili ng Dandelion++ na Pribado ang Pinagmulan ng Transaksyon ni Monero](/knowledge/monero-dandelion/)

  * [Bakit Open Source At Desentralisado ang Monero](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Ano ang Nagiging Espesyal sa RandomX](/knowledge/monero-mining-randomx/)

  * [Bakit Mas Mahusay ang Monero kaysa Dash, Zcash, Zcoin (Kahit na may Lelantus), Grin at Bitcoin Mixers Like Wasabi (Na-update Mayo 2020)](/knowledge/why-monero-is-better/)