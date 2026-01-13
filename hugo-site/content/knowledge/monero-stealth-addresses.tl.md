---
title: "Paano Pinoprotektahan ng Monero Stealth Address ang Iyong Pagkakakilanlan"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Nagpatupad si Monero ng three-prong approach sa privacy. Ang mga teknolohiyang ito ay [ring signature](/knowledge/ring-signatures), na nagtatago ng tunay na output (nagpadala), RingCT na nagtatago ng mga halaga, at stealth address, na nagtatago sa receiver. Ngayon, tatalakayin natin ang huling mga nabanggit na teknolohiyang ito: mga stealth address.

Maraming dahilan kung bakit maaaring gustong itago ng isang indibidwal kung kanino sila pinadalhan. Hindi natin dapat hayaan ang sinuman na subukang kumbinsihin tayo na ang lahat ng mga halimbawa nito ay hindi magandang pag-uugali. Ang mga bagay tulad ng pagpapadala sa isang hindi sikat na partidong pampulitika, pagbibigay ng donasyon sa mga kawanggawa, o pagsuporta sa mga itinuturing ng kultura na 'kinansela' ay lahat ng mga halimbawa kung saan maaaring naisin ng isang tao na itago ang kanilang mga gawi sa paggastos dahil sa takot na maapektuhan, ngunit ito ay ganap na lehitimo sa kalikasan.[X840X ] 

Sa isang transparent na blockchain, ang mga address kung saan ipinapadala ng isa ang kanilang mga transaksyon ay makikita ng lahat. Mahalagang isaalang-alang na kung ang mga minero mismo ay hindi sumasang-ayon sa kung saan napupunta ang pera, maaari nilang piliing huwag minahan ito sa isang bloke, na epektibong sini-censor ang transaksyong ito sa isang tila platform na lumalaban sa censorship. Ang tanging paraan para gawin ito, tinatanggap na hindi malamang, hindi posible ang censorship ay kung hindi matukoy ng mga minero ang pagkakaiba sa pagitan ng mga transaksyon dahil lahat ng on-chain metadata ay natatakpan ng iba't ibang paraan. Isang bagay na kilala ni Monero.

Niresolba ng Monero ang problemang ito ng mga transparent na address sa pamamagitan ng pagpapatupad ng mga stealth address, isang teknolohiya na aktwal na ginawa para sa Bitcoin noong 2011 ng user ng forum ng Bitcoin Talk na ByteCoin (ang kaugnayan sa Bytecoin, na sa kalaunan ay magsasama ng mga stealth address, ay hindi alam). Gayunpaman, ang kasalukuyang anyo ng mga stealth address ay may ilang mga pagpapabuti kaysa sa paunang ideya. Ngunit una, upang makita kung paano gumagana ang mga ito, pag-usapan natin ang tungkol sa mga susi.

Mahirap na nasa espasyo ng cryptocurrency at hindi makarinig ng tungkol sa mga susi. Ang mga pariralang tulad ng 'i-back up ang iyong pribadong susi' ay karaniwan, ngunit kapag ang isang karaniwang Joe ay nakarinig ng mga salitang "pampublikong susi" at "pribadong susi" sila ay matatakot at iniisip na ito ay masyadong teknikal at nakakalito upang maunawaan. Pero huwag kang mag-alala. Dadalhin natin ito nang dahan-dahan, at gagamit tayo ng maraming halimbawa.

Ang dalawang uri ng key na ginagamit sa mga cryptocurrencies ay, gaya ng nabanggit, pampubliko at pribado. Ang dalawang key na ito ay karaniwang may pares, ibig sabihin, ang isang partikular na pampubliko at pribadong key ay naka-link sa isa't isa. Sa katunayan, kadalasan ang pampublikong susi ay nagmula sa pribado, ibig sabihin, kung alam mo ang pribadong susi, ang iyong wallet ay makakagawa ng ilang mahusay na matematika at makabuo ng tamang pampublikong susi sa bawat pagkakataon.

Ngayon, gaya ng ipinahihiwatig ng mga pangalan, ang pampublikong susi ay maaaring maging pampubliko nang walang kahihinatnan. Kadalasan ito ay bahagi ng address na ibinabahagi mo upang makatanggap ng pera sa iyong cryptocurrency wallet. Kasunod din ng pangalan nito, ang pribadong susi ay isa na hindi dapat ibahagi. Ito ang bagay na nagbibigay-daan sa iyong pumirma at gumastos ng isang transaksyon, kaya kung ito ay ninakaw o ibinahagi, maaaring gastusin ng hamak na third party ang iyong pera, kadalasan sa kanilang sarili.

Ang isang madaling pagkakatulad dito ay isang padlock at ang susi na kailangan para i-unlock ito. Ang bukas na padlock ay malayang maibabahagi, at sa katunayan, anumang bagay ay maaaring mai-lock sa padlock na ito, ngunit ang taong may susi lamang ang makakapagbukas ng anumang bagay na nakasara ang padlock. Ang padlock ay maaaring kopyahin at ibahagi, ang susi ay hindi dapat.

Ang mga key na ito ay kadalasang inaalis mula sa user, kaya hindi mo talaga makikita ang mga ito. Sa Monero, hindi sila lumilitaw bilang isang nakakatakot na alphanumeric string sa lahat. Sa Monero, alam ng karaniwang gumagamit ang pribadong susi bilang kanilang binhi. Ang binhi (na dapat mong isulat kung wala ka pa), ay talagang isang pribadong key na nababasa ng tao. 

Kita mo? Hindi naman kasi nakakatakot. Bumalik sa mga stealth address.

Tulad ng nabanggit dati, ang mga stealth address ay hindi orihinal na ginawa para sa Monero, ngunit Bitcoin. Tulad ng karamihan sa mga bagong ideya, ang unang pag-ulit na ito ay may mga isyu. Ang susunod na pagtatangka ay dumating nang ang CryptoNote ay nilikha ni Nicholas van Saberhagan para sa Bytecoin, ang pasimula ng Monero ([tingnan ang aming kasaysayan ng Monero at Bytecoin dito](/knowledge/monero-history)), at habang ito ay isang tiyak na pagpapabuti sa orihinal, kahit na mayroon itong ilang banayad na mga depekto.

Sa kalaunan, nagkaroon ng isang huling pag-ulit mula sa isang developer para sa isa pang hindi na ngayon, privacy cryptocurrency, na nag-ayos ng mga natitirang isyu sa privacy at seguridad sa ideya. Sa kalaunan ay nakarating ito sa Monero, at ito ang ginagamit ngayon.

Bagama't nalutas ang mga isyung ito sa privacy at seguridad, ang mga stealth address mismo ay nagdagdag ng ibang uri ng quirk sa mga teknolohiyang blockchain, isa na wala pa noon. Ang pangangailangan upang i-scan. Dahil ang pagtanggap ng mga address ay hindi ipinapakita sa publiko sa blockchain, hindi alam ng receiver kung sa kanila ang anumang ibinigay na transaksyon, kaya dapat nilang i-scan ang bawat papasok na transaksyon gamit ang kanilang pribadong key upang makita kung sa kanila ito.

Sa mga transparency coins, ang kailangan lang nilang gawin ay tingnan kung may ipinapadalang transaksyon sa iyong address. Isang madaling tanong na oo o hindi. Ngunit sa mga stealth address, ang bawat transaksyon ay posibleng isa na ipinapadala sa iyo, kaya kailangan mong subukang i-unlock ang bawat isa gamit ang iyong pribadong key upang makita kung ito ay bubukas.

Ito ay isang karagdagang hakbang na wala ang Bitcoin at ang mga derivative nito, at gumagawa ng paunang pag-setup ng wallet, kasama ang pag-sync ng wallet kapag matagal mo itong hindi nabubuksan, mas mahaba kaysa sa Bitcoin. Ang tradeoff ay kinakailangan bagaman, upang i-unlock ang mga garantiya sa privacy na mayroon ito. Dapat tandaan na, hindi tulad ng pinakamahina na punto ng privacy trifecta, ang mga pirma ng singsing, ang mga stealth na address ay hindi madaling kapitan sa heuristics. Ito ay umaasa sa sinubukan at totoong elliptic curve cryptography, kung saan umaasa ang buong internet, kaya ang pagsira nito ay mangangahulugan ng pagwawakas sa seguridad ng computer sa pangkalahatan, hindi lang sa Monero.

Sa isang transparent na blockchain, ang mga address kung saan ipinapadala ng isa ang kanilang mga transaksyon ay makikita ng lahat. Mahalagang isaalang-alang na kung ang mga minero mismo ay hindi sumasang-ayon sa kung saan napupunta ang pera, maaari nilang piliing huwag minahan ito sa isang bloke, na epektibong sini-censor ang transaksyong ito sa isang tila platform na lumalaban sa censorship. Ang tanging paraan para gawin ito, tinatanggap na hindi malamang, hindi posible ang censorship ay kung hindi matukoy ng mga minero ang pagkakaiba sa pagitan ng mga transaksyon dahil lahat ng on-chain metadata ay natatakpan ng iba't ibang paraan. Isang bagay na kilala ni Monero.

Niresolba ng Monero ang problemang ito ng mga transparent na address sa pamamagitan ng pagpapatupad ng mga stealth address, isang teknolohiya na aktwal na ginawa para sa Bitcoin noong 2011 ng user ng forum ng Bitcoin Talk na ByteCoin (ang kaugnayan sa Bytecoin, na sa kalaunan ay magsasama ng mga stealth address, ay hindi alam). Gayunpaman, ang kasalukuyang anyo ng mga stealth address ay may ilang mga pagpapabuti kaysa sa paunang ideya. Ngunit una, upang makita kung paano gumagana ang mga ito, pag-usapan natin ang tungkol sa mga susi.

Mahirap na nasa espasyo ng cryptocurrency at hindi makarinig ng tungkol sa mga susi. Ang mga pariralang tulad ng 'i-back up ang iyong pribadong susi' ay karaniwan, ngunit kapag ang isang karaniwang Joe ay nakarinig ng mga salitang "pampublikong susi" at "pribadong susi" sila ay matatakot at iniisip na ito ay masyadong teknikal at nakakalito upang maunawaan. Pero huwag kang mag-alala. Dadalhin natin ito nang dahan-dahan, at gagamit tayo ng maraming halimbawa.

Ang dalawang uri ng key na ginagamit sa mga cryptocurrencies ay, gaya ng nabanggit, pampubliko at pribado. Ang dalawang key na ito ay karaniwang may pares, ibig sabihin, ang isang partikular na pampubliko at pribadong key ay naka-link sa isa't isa. Sa katunayan, kadalasan ang pampublikong susi ay nagmula sa pribado, ibig sabihin, kung alam mo ang pribadong susi, ang iyong wallet ay makakagawa ng ilang mahusay na matematika at makabuo ng tamang pampublikong susi sa bawat pagkakataon.

Ngayon, gaya ng ipinahihiwatig ng mga pangalan, ang pampublikong susi ay maaaring maging pampubliko nang walang kahihinatnan. Kadalasan ito ay bahagi ng address na ibinabahagi mo upang makatanggap ng pera sa iyong cryptocurrency wallet. Kasunod din ng pangalan nito, ang pribadong susi ay isa na hindi dapat ibahagi. Ito ang bagay na nagbibigay-daan sa iyong pumirma at gumastos ng isang transaksyon, kaya kung ito ay ninakaw o ibinahagi, maaaring gastusin ng hamak na third party ang iyong pera, kadalasan sa kanilang sarili.

Ang isang madaling pagkakatulad dito ay isang padlock at ang susi na kailangan para i-unlock ito. Ang bukas na padlock ay malayang maibabahagi, at sa katunayan, anumang bagay ay maaaring mai-lock sa padlock na ito, ngunit ang taong may susi lamang ang makakapagbukas ng anumang bagay na nakasara ang padlock. Ang padlock ay maaaring kopyahin at ibahagi, ang susi ay hindi dapat.

Ang mga key na ito ay kadalasang inaalis mula sa user, kaya hindi mo talaga makikita ang mga ito. Sa Monero, hindi sila lumilitaw bilang isang nakakatakot na alphanumeric string sa lahat. Sa Monero, alam ng karaniwang gumagamit ang pribadong susi bilang kanilang binhi. Ang binhi (na dapat mong isulat kung wala ka pa), ay talagang isang pribadong key na nababasa ng tao. 

Kita mo? Hindi naman kasi nakakatakot. Bumalik sa mga stealth address.

Tulad ng nabanggit dati, ang mga stealth address ay hindi orihinal na ginawa para sa Monero, ngunit Bitcoin. Tulad ng karamihan sa mga bagong ideya, ang unang pag-ulit na ito ay may mga isyu. Ang susunod na pagtatangka ay dumating nang ang CryptoNote ay nilikha ni Nicholas van Saberhagan para sa Bytecoin, ang pasimula ng Monero ([tingnan ang aming kasaysayan ng Monero at Bytecoin dito](/knowledge/monero-history)), at habang ito ay isang tiyak na pagpapabuti sa orihinal, kahit na mayroon itong ilang banayad na mga depekto.

Sa kalaunan, nagkaroon ng isang huling pag-ulit mula sa isang developer para sa isa pang hindi na ngayon, privacy cryptocurrency, na nag-ayos ng mga natitirang isyu sa privacy at seguridad sa ideya. Sa kalaunan ay nakarating ito sa Monero, at ito ang ginagamit ngayon.

Bagama't nalutas ang mga isyung ito sa privacy at seguridad, ang mga stealth address mismo ay nagdagdag ng ibang uri ng quirk sa mga teknolohiyang blockchain, isa na wala pa noon. Ang pangangailangan upang i-scan. Dahil ang pagtanggap ng mga address ay hindi ipinapakita sa publiko sa blockchain, hindi alam ng receiver kung sa kanila ang anumang ibinigay na transaksyon, kaya dapat nilang i-scan ang bawat papasok na transaksyon gamit ang kanilang pribadong key upang makita kung sa kanila ito.

Sa mga transparency coins, ang kailangan lang nilang gawin ay tingnan kung may ipinapadalang transaksyon sa iyong address. Isang madaling tanong na oo o hindi. Ngunit sa mga stealth address, ang bawat transaksyon ay posibleng isa na ipinapadala sa iyo, kaya kailangan mong subukang i-unlock ang bawat isa gamit ang iyong pribadong key upang makita kung ito ay bubukas.

Ito ay isang karagdagang hakbang na wala ang Bitcoin at ang mga derivative nito, at gumagawa ng paunang pag-setup ng wallet, kasama ang pag-sync ng wallet kapag matagal mo itong hindi nabubuksan, mas mahaba kaysa sa Bitcoin. Ang tradeoff ay kinakailangan bagaman, upang i-unlock ang mga garantiya sa privacy na mayroon ito. Dapat tandaan na, hindi tulad ng pinakamahina na punto ng privacy trifecta, ang mga pirma ng singsing, ang mga stealth na address ay hindi madaling kapitan sa heuristics. Ito ay umaasa sa sinubukan at totoong elliptic curve cryptography, kung saan umaasa ang buong internet, kaya ang pagsira nito ay mangangahulugan ng pagwawakas sa seguridad ng computer sa pangkalahatan, hindi lang sa Monero.

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

  * [Monero Mining: Ano ang Nagiging Espesyal sa RandomX](/knowledge/monero-mining-randomx)/

  * [Bakit Mas Mahusay ang Monero kaysa Dash, Zcash, Zcoin (Kahit na may Lelantus), Grin at Bitcoin Mixers Like Wasabi (Na-update Mayo 2020)](/knowledge/why-monero-is-better)/

Karagdagang pagbabasa