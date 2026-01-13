---
title: "Ang Kailangang Malaman ng Bawat Gumagamit ng Monero Pagdating sa Networking"
slug: "monero-networking"
date: "2020-11-11"
image: "/images/networking.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Hindi dapat ipagtaka kaninuman na ang Monero, at talagang lahat ng cryptocurrency, ay tumatakbo sa internet. Gayunpaman, kahit na ang pahayag na ito ay tila simple at halata, marami ang hindi isinasaalang-alang ang mga implikasyon ng kung ano ang ibig sabihin nito tungkol sa kanilang privacy. Sa madaling salita, may ilang bagay na maaari at hindi mapoprotektahan ni Monero, sa likas na katangian ng pagtakbo sa internet. Ang ilan sa mga pagsasaalang-alang na ito ay mga abala lamang, habang ang iba ay mas seryoso sa isang sitwasyon kung saan kinakailangan ang ganap na privacy. Maglaan tayo ng oras upang maging pamilyar sa kung paano nakikipag-ugnayan ang mga user ng Monero sa isa't isa sa network, at kung ano ang ibig sabihin nito para sa kanilang privacy.

Simula sa maliit na bahagi ng mga bagay, kung ang isang user ay walang access sa internet, hindi sila makakapag-download ng mga bagong block, makakapagpalaganap ng mga transaksyon sa ngalan ng iba, o makakapagpadala ng mga sarili nilang transaksyon. Ang isang kawili-wiling bagay na dapat tandaan ay, ang isang user na may buong node, na walang internet access ay maaaring bumuo ng isang transaksyon offline na maaaring ipadala sa ibang pagkakataon. Ito ay dahil ang isang pirma ng singsing ay nangangailangan lamang ng mga output mula sa blockchain upang maitago. Isang maikling paalala sa [kung paano gumagana ang mga ring signature](/knowledge/ring-signatures), itinatago nito ang totoong output na ipinapadala ng isang user sa isang koleksyon ng mga hindi nauugnay na output na pinili mula sa nakaraan. Kung ang user ay may access sa mga output na ito sa anyo ng isang ganap na na-download na blockchain (buong node) pagkatapos ay maaari nilang gawin ang ring signature mula sa mga nakaraang output, at sa sandaling magpatuloy ang koneksyon sa internet, i-propagate ang transaksyon sa network.

Hindi ito magagawa ng isang user na gumagamit ng remote node, dahil kapag ginawa nila ang kanilang ring signature, nakikipag-ugnayan sila sa remote full node para sa mga output na isasama sa ring signature. Nangangahulugan ang walang internet na hindi nila maabot ang node na ito, kaya wala silang mga kakayahan sa pagbuo ng offline na transaksyon.

Bago tayo magpatuloy sa ilan sa mga pagsasaalang-alang sa privacy, magkaroon tayo ng maikling panimulang aklat sa kung paano gumagana ang internet sa kabuuan. Ang buong internet ay walang iba kundi ang mga computer na kumokonekta sa ibang mga computer. Ayan yun. Ang blog na gusto mong basahin? Ilang file lang na naka-host sa computer ng ibang tao. Itong website na binabasa mo ang artikulong ito sa (LocalMonero)? Mga file at code na naka-host sa isang computer sa isang lugar. Kahit na ang malalaking nakatutuwang mga site ay gumagana sa ganitong paraan. Kunin ang YouTube halimbawa. Mga video file lang na naka-host sa napakalaking computer system ng Google, at kumonekta ka sa kanila para i-download ang video sa sarili mong computer para mapanood mo ito.

Maaaring magkahiwalay ang mga computer na ito dahil ang bawat computer na nakakonekta sa internet ay binibigyan ng natatanging identification number na tinatawag na IP address. Ang mga ito ay karaniwang apat na hanay ng mga numero na pinaghihiwalay ng mga tuldok, halimbawa: 172.66.35.7. Mahalagang tandaan ito kapag isinasaalang-alang namin kung paano inililipat ang impormasyon ng Monero sa internet. Ang Monero ay isang peer-to-peer network (P2P), ibig sabihin, ang mga computer ay direktang kumonekta sa isa't isa sa halip na gumamit ng isang tagapamagitan. Kaya kapag ang buong node ng user ay nagda-download ng bagong natuklasang block, hindi nila ito dina-download mula sa isang central server, ngunit mula sa kanilang mga kapantay. Ang downside nito ay, dahil direktang kumokonekta ang mga user sa isa't isa, alam nila ang mga IP address ng isa't isa.

Aba? Ano ang malaking bagay? Number lang naman diba? Hindi eksakto. Ang mga IP address mismo ay naglalaman ng impormasyon tungkol sa user, tulad ng pinagmulang bansa, at network provider, ngunit, mas masahol pa, alam ng mga internet service provider (ISP) ang IP address ng bawat tao na gumagamit ng kanilang mga serbisyo. Nangangahulugan ito na ang mga ISP na ito at ang mga katrabaho nila ay maaaring manood ng trapiko sa internet ng isang user at, gamit ang ilang matalinong taktika, matuklasan na sila ay gumagamit ng Monero. Ngayon bago ka matakot, tandaan ang mga salita doon. Ang magagawa lang ng mga snooper na ito ay makita na ang isang tao ay kumokonekta sa iba pang mga node sa Monero network. Dahil sa teknolohiya ng pagkapribado ng Monero, wala nang ibang nailalabas tungkol sa indibidwal. Hindi kung nagpapatakbo sila ng node o hindi, o kung/kapag nagpadala sila ng mga transaksyon, at kung ipinadala ang isang transaksyon, wala sa impormasyon nito ang nalalaman. Ang nakikita lang ng mga ISP na ito ay ang isa sa kanilang mga user ay kumokonekta sa Monero network.

Ngayon, para sa ilang tao, sa ilang lokasyon, maaaring sapat na ang impormasyong ito upang magdulot ng pinsala sa reputasyon o kalayaan. O marahil ang ideya ng sinumang manghihimasok sa iyong privacy at kung ano ang ginagawa mo sa internet, sa anumang kadahilanan, ay hindi katanggap-tanggap sa iyo. Ang mga indibidwal na ito ay hinihikayat na kumonekta lamang sa Monero network gamit ang mga VPN, Tor, o I2P, na lahat ay mga serbisyong nagtatago ng IP address ng isang user mula sa iba pati na rin nagtatago kung ano ang ginagawa ng isang user mula sa kanilang ISP. Ang mga pagkakaiba sa pagitan ng mga serbisyong ito ay lampas sa saklaw ng artikulong ito, ngunit maraming mga artikulong may mataas na kalidad na nakasulat sa paksa, kaya hinihikayat ang mga nag-aalalang user na mag-aral!

Para sa iba pa sa atin, maaari nating isipin na hindi ganoon kalaki ang pag-alam ng iba na nakakonekta tayo sa Monero network. Pagkatapos ng lahat, ang aktwal na nilalaman ng aming mga transaksyon, o kung nagpapadala kami ng anuman, ay nakatago sa publiko, kaya ano ang masama? Bagama't maaaring totoo ito, hinihikayat ang mga user na isaalang-alang ang katotohanan na ang pangunahing draw ng cryptocurrencies ay ang kanilang sariling bangko. Kapag hawak mo ang iyong pribadong key, at kung may mangyari dito, walang makakatulong sa iyong mabawi ang iyong mga nawawalang pondo.

Ang pagiging sarili mong bangko ay nangangahulugan ng pagsasaalang-alang, hindi lang sa iyong digital na seguridad, kundi sa iyong pisikal na seguridad din. Maaaring ang kaalaman ng isang indibidwal na kumokonekta sa Monero network ay maaaring magdulot ng hindi gustong atensyon, hindi kinakailangan mula sa malalaking aktor tulad ng mga bansang estado, ngunit mas maliliit na may makasariling interes, tulad ng mga hacker na naghahanap ng madaling kumita. Tunay na hindi mabilang ang mga kuwento sa buong crypto space ng mga ganitong sitwasyon na aktwal na nagaganap.

Ang artikulong ito ay hindi nilayon upang takutin o takutin, ngunit hikayatin ang mga user na magsaliksik sa kung anong mga paraan ng proteksyon sa web surfing ang tama para sa kanila. Ang magandang balita ay, na ang mga kasanayang ito ay lilipat din sa pangkalahatang paggamit ng internet, hindi lamang sa paggamit ng Monero, at dahil dito, sa ating lalong nagiging konektadong mundo sa internet, ang isang matalinong user ay hindi maaaring magkamali sa pag-iipon ng tamang kaalaman at kasanayan upang manatiling ligtas. at tunay na maging sarili nilang bangko.

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

  * [Monero Mining: Ano ang Nagiging Espesyal sa RandomX](/knowledge/monero-mining-randomx)/

  * [Bakit Mas Mahusay ang Monero kaysa Dash, Zcash, Zcoin (Kahit na may Lelantus), Grin at Bitcoin Mixers Like Wasabi (Na-update Mayo 2020)](/knowledge/why-monero-is-better)/

Karagdagang pagbabasa