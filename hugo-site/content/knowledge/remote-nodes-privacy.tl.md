---
title: "Paano nakakaapekto ang malalayong node sa privacy ni Monero"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Isa sa pinakamalaking bentahe ng Monero kaysa sa iba pang cryptocurrencies ay on-chain privacy ito, ngunit naisip mo na ba kung paano nananatili ang privacy ni Monero kapag gumagamit ka ng remote na node? Paano kung gumamit ka ng "light wallet" server tulad ng MyMonero?

Sa post na ito, susuriin natin ang ilan sa mga detalye kung paano nagbibigay ang Monero ng pambihirang on-chain na privacy kahit na gumagamit ng remote na node, pati na rin kung ano ang dapat bantayan kapag gumagamit ng mga malalayong node.

## Anong function ang nagsisilbing node sa Monero?

Para sa mga hindi gaanong pamilyar sa kung paano gumagana ang Monero, ang mga node (o mga server) sa network ng Monero ay maaaring patakbuhin ng sinuman at payagan ang may-ari ng node – o sa iba pang pipiliin nilang ibahagi ito! – upang i-synchronize ang isang kopya ng blockchain at ibigay ang kopya na iyon sa iba sa network. Bine-verify din ng mga node na ito ang lahat ng transaksyong nangyayari sa network, gayundin ang lahat ng block na na-publish at tinitiyak na sumusunod ang lahat sa mga panuntunan ayon sa itinakda ng consensus.

Ang iba pang function na inihahatid ng mga node sa Monero ay bilang isang paraan upang maibigay ang lahat ng data na kailangan ng iyong paboritong Monero wallet upang maayos na suriin ang mga transaksyong pagmamay-ari mo at gumawa ng mga bagong transaksyon. Ang data na ito ay ibinibigay ng mga node sa dalawang paraan:

  * Ang data mula sa bawat bloke sa blockchain ay hinihiling ng wallet, na-scan para sa mga transaksyong pagmamay-ari mo, at pagkatapos ay itatapon kapag nasuri ng wallet. 
    * Malapit nang mapabuti ang hakbang na ito, salamat sa [view tags](/knowledge/view-tags-reduce-monero-sync-time).
  * Kapag nagpapadala ng mga transaksyon, ang node na ginagamit mo ay nagbibigay ng listahan ng mga posibleng pang-decoy (o mga pekeng input) na gagamitin kapag ginagawa ang transaksyon, na tinitiyak na mayroon kang maraming tao na magtatago sa tuwing gagastusin mo ang Monero. 
    * Ang mga decoy na ito ay bahagi ng [ring signature](/knowledge/ring-signatures), isang mahalagang bahagi ng diskarte ni Monero sa privacy on-chain.

## Ano ang pinakapribado at ligtas na paraan ng paggamit ng Monero?

Ang pinakamagandang gawin, kahit na may malakas na on-chain na privacy na ibinigay ng Monero kapag gumagamit ng mga malalayong node, ay ang magpatakbo ng sarili mong Monero node para matiyak na mayroon kang malinis na kopya ng Monero blockchain na madaling gamitin at ang iyong IP address ay mahusay na protektado. Ang iba pang benepisyo kapag nagpapatakbo ng sarili mong node ay maaari kang mag-ambag pabalik sa network, na nagpapahintulot sa iba pang mga node na mag-synchronize mula sa iyong node o kahit na hinahayaan ang ibang mga user na kumonekta sa iyong node gamit ang kanilang mga wallet.

Iyon ay sinabi, ang Monero ay nagbibigay pa rin ng mahusay na privacy kapag gumagamit ng isang malayuang node. Kung interesado kang magpatakbo ng sarili mong Monero node, narito ang isang madaling sundin na gabay sa paggawa nito:

  * [Magpatakbo ng Monero Node](https://sethforprivacy.com/guides/run-a-monero-node/)

## Ano ang matututuhan ng remote node tungkol sa akin?

Kapag gumagamit ng remote na node, may ilang mahahalagang bahagi ng impormasyon na nalalantad sa isang malayuang node at ilang mahahalagang paraan kung saan maaaring atakehin ka ng node, pigilan kang makipagtransaksyon, at higit pa.

Ang unang bagay na matututunan ng remote node tungkol sa iyo ay ang iyong pampublikong IP address. Bagama't sana ay maitago ito sa pamamagitan ng VPN o Tor, maaaring iugnay ng malayong node ang iyong pampublikong IP address sa transaksyon, na tumutulong sa kanila na paliitin kung saan ka nagmula sa transaksyon. Matututuhan din ng remote na node ang huling block na na-sync ng iyong wallet at gamitin ito upang subukan at gumawa ng mga edukadong hula tungkol sa iyo, gaya ng kung kailan mo karaniwang ginagamit ang Monero at kung kailan mo huling ginugol ang Monero. Ito ay totoo lalo na kung palagi kang nagmumula sa parehong IP address (tulad ng iyong tahanan). Ang huling mahalagang bagay na matututunan ng isang remote na node tungkol sa iyo ay ang pangunahing impormasyon tungkol sa mga transaksyong ipinapadala mo sa pamamagitan nito. Bagama't maaaring ito ang pinaka-halatang data na nakukuha ng remote node operator tungkol sa iyo, mahalagang maunawaan na ito ay magagamit upang makatulong na subaybayan ang nagpadala ng transaksyon kapag pinagsama ang impormasyong iyon sa iba pang data sa labas ng chain. Maaari itong maging partikular na mapanganib kung ang remote node ay pinapatakbo ng isang malisyosong entity, isang blockchain analytics na kumpanya, o isang mapang-aping nation-state.

Maaari ding subukan ng isang malayuang node na magdulot ng problema sa iyo sa pamamagitan ng pagtatago ng mga bloke mula sa iyo, na ginagawang isipin ng iyong wallet na naka-sync ito kapag hindi. Maaari nitong isipin na nawawala ang mga pondo o pigilan ka sa paggastos ng mga pondo hanggang sa kumonekta ka sa isa pang node. Ang huling mahalagang bagay na maaaring gawin ng isang malayuang node ay magpakain sa iyong wallet ng isang manipuladong listahan ng mga pang-aakit. Ito ay maaaring maging sanhi ng iyong wallet na ganap na mabigo sa pagbuo ng mga transaksyon (na nagiging dahilan upang hindi ka makagastos ng mga pondo), o maaaring payagan ang remote na node na subukan at magbigay ng mga decoy na alam nitong ginagastos upang bawasan ang pagka-anonymity na natatanggap mo sa bawat transaksyon.

## Anong mga garantiya sa privacy ang umiiral pa rin kapag gumagamit ng isang malayong node?

Bagaman ang artikulong ito ay maaaring medyo natakot sa iyo, mahalagang malaman na ang privacy na ibinigay ng Monero ay napakahusay kahit na gumagamit ng isang remote na node, at higit na nahihigitan ang anumang iba pang cryptocurrency kapag ginamit sa ganitong paraan. Nakukuha mo pa rin ang malakas na on-chain na privacy na ibinigay ng Monero, dahil hindi alam ng remote node ang totoong input (anong mga barya ang ginagastos mo), ang halaga ng Monero na ginastos sa transaksyon, o ang address ng tatanggap ng transaksyon. Hindi rin makikita ng mga tagamasid sa labas ang totoong input, halaga, o mga address na kasangkot (kahit anong uri ng node ang pipiliin mong gamitin!), na tinitiyak na sa labas ng remote node kahit ang iyong IP address, impormasyon sa pag-sync ng wallet, at mga transaksyon ay may matibay na garantiya sa privacy .

Ang remote na node ay hindi rin magkakaroon ng access sa mga nakaraang transaksyon na iyong ipinadala o natanggap o ang halaga ng Monero na kasalukuyang nasa iyong wallet, at mawawala ang lahat ng visibility sa iyong mga transaksyon sa sandaling magsimula kang gumamit ng isa pang node. Walang mga pribadong key (alinman sa paggastos o view ng mga key) na kailanman ay ibinigay sa remote node, at sa gayon ang iyong wallet ay nananatiling pribado, secure, at magagamit. Anuman ang malayong node, hindi ka rin nanganganib na mawala ang Monero o manakaw nito, dahil hindi ma-edit ng node ang address ng tatanggap, hindi kailanman magkakaroon ng access sa mga pribadong key ng iyong mga wallet, at hindi maaaring kumpiskahin ang iyong Monero sa anumang paraan.

## Kumusta naman ang mga “light wallet” tulad ng MyMonero?

Bagama't ang paksa ay medyo nasa labas ng saklaw ng artikulong ito, gusto kong tugunan ang isang natatanging uri ng wallet sa Monero – mga light wallet. Ang pangalang light wallet ay nagmula sa katotohanan na ang iyong wallet (sa iyong telepono o computer) ay hindi kailangang magsagawa ng alinman sa blockchain synchronization, na ginagawang mas mabilis at mas tuluy-tuloy ang karanasan.

Gayunpaman, ang mga wallet na tulad nito ay may matinding trade-off sa privacy sa ngayon – ipinapadala ng iyong wallet ang pribadong view key sa remote server na ginagamit mo (tulad ng default sa MyMonero), na nagbibigay ng ganap na visibility sa remote server sa anumang natanggap na pondo mula noong likhain ang iyong pitaka (at hanggang sa tumigil ka sa paggamit ng pitaka o binhing iyon). Binabawasan nito nang husto ang privacy na natatanggap mo mula sa node operator, at dapat itong lapitan nang may pag-iingat.

Sa kabutihang palad, ang komunidad ng Monero ay nagsusumikap sa pagpapabuti ng software na magagamit mo upang mag-host ng iyong sariling light wallet server (LWS), na magbibigay-daan sa iyong magkaroon ng mabilis na pag-synchronize nang hindi nagtitiwala sa isang 3rd-party gamit ang iyong mga pribadong view key – habang ikaw tatakbo ang software kung saan ipinapadala ng iyong wallet ang mga pribadong view key!

Para sa higit pa sa custom na light wallet server, tingnan ang ibaba ng Github repository:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Paano ako matututo ng higit pa?

Kung interesado ka at gustong mas maunawaan ang mga node sa Monero at tumingin sa paggamit ng remote na node o pagpapatakbo ng sarili mong node, tingnan ang mga link sa ibaba para sa magagandang lugar para makapagsimula:

  * [Monero World, isang listahan ng mga remote na node na pinapatakbo ng komunidad na maaaring gamitin](https://moneroworld.com/#nodes)
  * [Monero node na pinapatakbo ng Seth For Privacy, ang may-akda ng artikulong ito](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, isang listahan ng mga malalayong node na may madalas na sinusuri na status< /a>](https://monero.fail/)
  * [Paano kumonekta sa isang malayong node sa loob ng GUI wallet](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia - Remote Node](https://www.getmonero.org/resources/moneropedia/remote-node.html)

Karagdagang pagbabasa

  * [Paano natatanging pinapagana ng Monero ang mga circular na ekonomiya](/knowledge/monero-circular-economies/)

  * [Ang mga ring signature ni Monero vs CoinJoin tulad ng sa Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Bakit (at paano!) dapat mong hawakan ang sarili mong mga susi](/knowledge/hold-your-keys/)

  * [Nag-aambag pabalik sa Monero](/knowledge/contributing-to-monero/)

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