---
title: "Paano Pinipigilan ng Monero Subaddresses ang Pag-uugnay ng Pagkakakilanlan"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Ang Monero ay palaging nakakahanap ng mga makabagong paraan upang malutas ang mahihirap na problema sa privacy. Kadalasan ang mga pagbabagong ito ay humahantong sa iba pang mga pagbabago, at kung minsan ang mga nagreresultang teknolohiyang ito ay maaari pang gamitin para sa mga usecase na hindi pa isinasaalang-alang. Wala saanman ito na ipinakita nang higit pa kaysa sa kaso ng teknolohiyang subaddress ng Monero.

Isaalang-alang ang isang hypothetical na problema sa privacy, kung saan ang paggamit ng isang address sa maraming platform mula sa mga mukhang hindi nauugnay na mga tao ay maaaring humantong sa linkage at deanonymization ng nasabing mga tao. Sa madaling salita, kung ikaw ay isang taong nagngangalang Billy Joe Bob at nagbenta ka ng mga mansanas para sa Bitcoin, maaari mong i-post ang iyong Bitcoin address sa isang pampublikong lugar para bayaran ka ng mga customer. Sabihin nating nagsisimula ang address sa alphanumeric string na 7XybV3... Ngunit isinantabi ang halatang panganib sa privacy ng sinuman na masuri ang iyong balanse sa Bitcoin at makita kung magkano ang iyong naibenta, mayroong isang segundo, hindi madalas na pinag-uusapan ang panganib sa privacy. Sabihin nating isa ka ring underground hacker na may pangalang l33tz0r. Gumagawa ka ng whistle blowing work, na nagsasabi sa isang hindi pinaghihinalaang populasyon tungkol sa katiwalian sa gobyerno, at kailangan mong panatilihing lihim ang iyong pagkakakilanlan. Tumatanggap ka ng mga donasyon ng Bitcoin para sa iyong trabaho, at i-post ang address sa isang pampublikong forum. Ito ang parehong address kung saan ka tumatanggap ng pera mula sa iyong mga customer ng apple. Ang 7XybV3... isa.

Ang isang simple, ngunit mapangwasak na pag-atake sa deanonymization ay ang paggamit ng isang search engine sa internet upang hanapin ang iyong Bitcoin address. Ang paglalagay ng address ng 7XybV3... sa makina ay nagdudulot ng dalawang magkaibang resulta. Ang negosyo ng mansanas, at l33tz0r. Ito ay sapat na upang iugnay ang dalawang pagkakakilanlan at i-deanonymize ang l33tz0r, na may potensyal na nakakatakot na mga kahihinatnan mula sa mga kapangyarihan.

Mahalagang tandaan na ang pag-atakeng ito ay posible DIN sa Monero. Kahit na itinago ng Monero ang karamihan sa on-chain na data, ang pag-atakeng ito ay hindi gumagamit ng anuman. Ginagamit lang nito ang address, na dapat ibahagi para makatanggap ng bayad. Pampubliko sa kaso ng anonymous na mga donasyon. Ito ay isang potensyal na paraan kung saan ang mga user ng Monero ay maaaring hindi sinasadyang saktan ang kanilang privacy, at isa rin itong halimbawa ng kung paano, kahit na ang Monero ay nangungunang tier tungkol sa pagpapanatili ng privacy, hindi ito bulletproof.

Ang karaniwang paraan ng paglutas sa problemang ito ay ang pagmamay-ari ng maraming wallet. Sa iba't ibang mga address na naka-post para sa bawat pagkakakilanlan (o usecase), hindi sila mai-link. Ngunit mananatili lamang ang privacy na ito kung hindi kailanman pinaghalo ng user ang mga ito. Ang hindi sinasadyang pag-post ng maling address ay magkakaroon ng parehong mga epekto ng linkage. Gayundin, ang binhi ng bawat address ay dapat na panatilihing secure, na nagdaragdag sa infosec na kailangan sa bawat bagong wallet na ginawa.

Ang solusyon ni Monero ay mga subaddress. Ang kakayahang lumikha ng isang ganap na napakalaking bilang ng mga address sa ilalim ng pangunahing address, gamit ito bilang isang binhi ng mga uri. Ang bawat nabuong subaddress ay maaaring tumanggap ng Monero, at lahat ng ito ay napupunta sa parehong wallet. Gamit ang paraang ito, ang bilang ng mga pagkakakilanlan na maaaring patakbuhin sa ilalim ng isang address ay napakalaki habang pinapanatili ang infosec sa pinakamababa. Ang mga address na ito ay hindi rin mathematically linkable, kaya maliban kung ang user ay sumigaw ng kanilang koneksyon sa mundo, ang isang tagamasid sa labas ay mahihirapang i-link ang mga ito.

Ngunit isa pang kawili-wiling usecase ang lumabas mula sa mga subaddress; bilang kapalit na opsyon ng mga pangkalahatang kinasusuklaman na mga ID sa pagbabayad.

Ang mga Payment ID ay isang paraan para matukoy ng mga merchant kung sinong customer ang nagpadala ng bayad. Dahil ang impormasyon ng Monero ay nakakubli sa chain, hindi makikita ng receiver ng isang transaksyon kung aling address ang nagpadala nito. Nangangahulugan ito na kung mayroong magkatulad na presyo ng mga item at maramihang mga order, maaari itong maging imposible upang matukoy kung sino ang nagpadala ng kung ano. Ang mga Payment ID ay isang natatangi, random na string na nabuo ng merchant at ibinigay sa customer. Idinaragdag ito ng customer bilang isang hiwalay na field kapag ipinapadala ang transaksyon. Ang random na string na ito ay inilalagay sa blockchain bilang bahagi ng transaksyon, at sa paraang ito, nakikilala at nabubukod-bukod ng merchant ang mga papasok na transaksyon.

Ang paraang ito ay may depekto sa maraming paraan. Una, binabawasan nito ang pagkakapareho ng on-chain na data. Ang karagdagang, natatanging metadata ay maaaring gumawa ng ilang mga transaksyon na bukod sa karamihan, sa gayon ay nagbibigay-daan sa heuristic analysis. Ito ay totoo lalo na kapag ang metadata na ito ay hindi ipinapatupad bilang mandatoryo para sa lahat. Ang paggawa ng mandatoryo na ito para sa lahat ay magdaragdag ng hindi kinakailangang espasyo sa blockchain bagaman, at hindi itinuloy. Gayundin, kung ang isang payment ID ay muling ginamit para sa anumang kadahilanan, magiging walang halaga na i-link ang dalawang transaksyon bilang konektado. Karaniwan itong nangyayari sa mga exchange deposit, at sinuman ay madaling mag-link ng mga transaksyon bilang parehong deposito sa isang exchange, at mula sa isang partikular na indibidwal.

Pangalawa, mula sa pananaw ng UX, ang mga payment ID ay gumagawa ng pangalawang hakbang na hindi nakasanayan ng mga gumagamit ng cryptocurrency na nagmumula sa ibang mga coin, at kung nakalimutan sila, nagdudulot ito ng matinding sakit ng ulo sa merchant na dapat tukuyin ang mga transaksyong ito sa pamamagitan ng ibang paraan. . Karaniwang ginagawa ito sa pamamagitan ng direktang pakikipag-usap sa bawat customer na nakalimutang ilagay ang payment ID at pagkumpirma ng iba pang impormasyong nagpapakilala na sila lang ang nakakaalam, tulad ng kumbinasyon ng halaga, petsa ng ipinadala, at transaction ID.

Ang dagdag na hakbang na ito ay napalampas ng marami, at umabot sa punto kung saan nagsimulang maningil ng pera ang ilang palitan sa mga customer kung kailangang manu-manong kunin ang kanilang pera dahil sa pagkalimot ng payment ID. Ang iba ay nagngangalit ang kanilang mga ngipin at kinain ang mga karagdagang gastos sa suporta, ngunit walang natuwa tungkol dito.

May isang solusyon dito, pinagsama-samang mga address, na pinagsama ang address at ang payment ID sa isang string, kaya hindi ito makalimutan, ngunit medyo mahina ang pag-aampon, sa kabila ng mga benepisyong matatanggap ng mga merchant mula sa pagsasama nito. 

Sa isang kawili-wiling pangyayari, dumating ang mga subaddress upang iligtas ang araw. Ang kakayahang bumuo ng malalaking halaga ng mga subaddress sa bawat pangunahing address, at tukuyin kung aling mga transaksyon ang dumating sa kung aling mga subaddress, nagbigay-daan sa mga merchant na alisin sa kanilang sarili ang mga ID ng pagbabayad sa isang eleganteng paraan, habang ginagamit ang susunod na henerasyon ng teknolohiyang Monero. Simula noon, karamihan sa mga palitan at tool ng merchant ay lumipat sa mga subaddress bilang pangunahing paraan ng pagkakakilanlan ng transaksyon.

Ang nagsimula bilang isang solusyon para sa isang problema sa privacy ay naging isang bagay na higit pa, na lumutas sa isang pangunahing isyu sa UX para sa mga merchant at customer. Ang inobasyon ay nagdudulot ng higit pang inobasyon, na kadalasang maaaring maging snowball sa mga hindi inaasahang panalo para sa lahat. Paulit-ulit na nakita ni Monero ang mga ito, at naglalagay ng malaking pagsisikap sa pagbabago kung ano ang posible sa blockchain. Sino ang nakakaalam kung ano ang iba pang mga bagay na maaari nating i-unlock nang magkasama?

Karagdagang pagbabasa

  * [Paano natatanging pinapagana ng Monero ang mga circular na ekonomiya](/knowledge/monero-circular-economies/)

  * [Ang mga ring signature ni Monero vs CoinJoin tulad ng sa Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Bakit (at paano!) dapat mong hawakan ang sarili mong mga susi](/knowledge/hold-your-keys/)

  * [Nag-aambag pabalik sa Monero](/knowledge/contributing-to-monero/)

  * [Paano nakakaapekto ang malalayong node sa privacy ni Monero](/knowledge/remote-nodes-privacy/)

  * [Paano gumagamit si Monero ng mga hard-forks para i-upgrade ang network](/knowledge/network-upgrades/)

  * [Tingnan ang mga tag: Paano babawasan ng isang byte ang mga oras ng pag-sync ng Monero wallet ng 40%+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [Ang P2Pool at ang Tungkulin Nito sa Desentralisasyon ng Monero Mining](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Ano ang Gagawin Nito para kay Monero](/knowledge/seraphis-for-monero/)

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