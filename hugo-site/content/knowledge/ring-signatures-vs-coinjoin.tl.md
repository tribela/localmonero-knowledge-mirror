---
title: "Ang mga ring signature ni Monero vs CoinJoin tulad ng sa Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Dahil ang mga tool sa privacy ng Bitcoin ay nakakuha ng higit na atensyon at paggamit, sila ay sumailalim sa mas maraming regulasyong pagsisiyasat. Ang pagsisiyasat na ito ay humantong sa isang [kamakailang anunsyo](https://twitter.com/wasabiwallet/status/1503091503207432193) ng isang tool sa privacy ng Bitcoin, Wasabi Wallet, na magsisimula silang i-censor at tanggihan ang mga papasok na input sa mga mix na itinuturing nilang bawal o laban sa kanilang ToS, at magbabayad sila ng chain analysis kumpanyang mag-“vet” sa mga papasok na kalahok ng mix.

Ang paggamit ng mga transaksyon sa CoinJoin upang i-obfuscate ang pinagmumulan ng mga pondo sa Bitcoin ay naging ubod ng privacy ng Bitcoin sa loob ng maraming taon na ngayon, at ang mga isyu at panganib na likas sa paggamit nito ay ilan sa mga pangunahing isyu na itinatama at pinipigilan ng mga ring signature ni Monero. .

Sa blog post na ito, sumisid tayo sa isang paghahambing ng CoinJoin at mga ring signature, gayundin kung bakit ang diskarte na ginawa sa Monero ay humahantong sa mas malaking censorship-resistance, mas malaking privacy, at mas kaunting abala para sa mga user.

## Ano ang transaksyon ng CoinJoin?

## Ano ang transaksyon ng CoinJoin?

Dahil ang lahat ng mga transaksyon ay ganap na transparent sa Bitcoin - inilalantad ang nagpadala, tagatanggap, at mga halaga - ang mga user ay dapat gumawa ng mga karagdagang hakbang upang mapanatili ang kanilang privacy mula sa mga nakaraang nagpadala at mga tatanggap sa hinaharap ng kanilang mga pondo o panganib na censorship, pagsubaybay, o pagnanakaw ng mga pondo sa pamamagitan ng pisikal na karahasan.

Ang pinakamahusay na solusyon ngayon para sa privacy sa Bitcoin ay isang tool na tinatawag na [“CoinJoin”](https://bitcoiner.guide/qna/coinjoin/), kung saan 2 o higit pang user ang nagtutulungan (karaniwan ay sa pamamagitan ng isang sentralisadong coordinator) upang lumikha ng isang espesyal na transaksyon na nagpapahirap sa labas mga tagamasid upang ikonekta ang mga input sa mga output. Ang bawat kalahok ay nakikipag-ugnayan upang sama-samang buuin ang transaksyon nang hindi ibinibigay ang pag-iingat ng kanilang mga pondo, at tumatanggap ng isang output sa dulo na ang nakaraang kasaysayan ay hindi malinaw (o malabo) sa mga tagamasid sa labas.

Ito ay sumisira sa kasaysayan ng mga partikular na UTXO, na nagbibigay-daan sa mga user ng Bitcoin na magkaroon ng kaunting pagpapalihim kapag nakikipagtransaksyon. Gayunpaman, ang CoinJoin (tulad ng ipinatupad sa Wasabi Wallet at Samourai Wallet, ang dalawang pinakaginagamit na tool ng CoinJoin para sa Bitcoin) ay may ilang pangunahing disbentaha:

  * Dahil ganap na nag-opt-in ang mga transaksyon sa CoinJoin at nangangailangan ng aktibong pakikilahok, kinakailangang ipakita ng sinumang kalahok na naghahanap sila ng higit na privacy kaysa sa mga "normal" na gumagamit ng Bitcoin, na posibleng ihiwalay ang mga ito at magdulot ng mga isyu sa paggastos ng mga pondo sa maraming kinokontrol na palitan o entity. Hindi maitatanggi ng bawat user na lumahok sila sa isang transaksyon sa CoinJoin.
  * Upang makahanap ng iba pang makakasama sa CoinJoin, karamihan sa mga diskarte sa CoinJoin (kabilang ang Wasabi Wallet) ay gumagamit ng isang sentralisadong coordinator na nag-uugnay sa mga kalahok at tinutulungan silang makipag-usap at bumuo ng isang maayos na transaksyon sa CoinJoin. Ang sentralisadong coordinator na ito ay hindi kailanman may kustodiya ng mga pondo ng user, ngunit nakakakuha ng malawak na insight sa mga transaksyong kanilang ikino-coordinate, maaaring mag-censor ng mga papasok na input (tulad ng sa kaso ng Wasabi Wallet), at maaaring mapilit na mangolekta o magbahagi ng impormasyon tungkol sa mga kalahok sa CoinJoin.[X2068X ] 
  * Ang mga gumagamit na may malaking halaga ng pondo sa CoinJoin ay kadalasang kailangang maghintay ng mga oras (o kahit na araw!) upang makahanap ng sapat na kalahok na makakasama ng CoinJoin, na humahantong sa malalaking pagkaantala mula sa oras na makatanggap ng mga pondo ang isang user hanggang sa kung kailan nila magagamit ang mga ito nang pribado. 
  * Ang privacy na ibinibigay ng isang transaksyon sa CoinJoin ay bumababa sa paglipas ng panahon habang ang ibang mga kalahok ay gumagastos ng mga pondo o ini-link ang kanilang mga output sa kanilang pagkakakilanlan sa pamamagitan ng KYC exchanges, ID na nangangailangan ng mga merchant, atbp. Nangangahulugan ito na ang mga user ay perpektong panatilihin ang kanilang mga pondo na patuloy na umiikot sa mga transaksyon sa CoinJoin upang mapanatili ang kanilang anonymity set ("crowd to hide in") bilang bago hangga't maaari.
  * Sa karamihan ng mga diskarte sa CoinJoin, ang mga kalahok ay dapat gumamit ng fixed-size na UTXO (i.e. 0.1 BTC) para mas mahirap ikonekta ang mga input at output ng mga transaksyon sa CoinJoin. Ito ay humahantong sa mas mataas na mga bayarin (mas hiwalay na mga transaksyon na kinakailangan sa bawat malaking input), mas "nakakalason na pagbabago" (mga pondo na hindi magastos nang walang malubhang panganib sa privacy), at maaaring mag-udyok sa mas maliliit na user na hindi makapaghalo sa lahat kung wala silang kinakailangang minimum na balanse.

## Paano malulutas ng mga ring signature ang mga isyung ito?

## Paano malulutas ng mga ring signature ang mga isyung ito?

Bilang [malalim naming tinitingnan kung ano ang mga pirma ng singsing sa nakaraan](/knowledge/ring-signatures), hindi ko na idedetalye ang mga teknikal na aspeto kung paano gumagana ang mga ito sa post sa blog na ito. Sa halip, titingnan natin kung paano nireresolba ng mga diskarte na ginawa sa Monero ang mga isyu sa CoinJoin na tinatalakay sa itaas.

> Ang CoinJoin ay opt-in at nangangailangan ng pakikilahok

Ang CoinJoin ay opt-in at nangangailangan ng pakikilahok

Ang mga ring signature ng Monero ay isang pangunahing feature ng privacy protocol, at _bawat_ na transaksyon sa network ay gumagamit ng mga ito. Nangangahulugan ito na walang mga transaksyon ng user ang namumukod-tangi para sa paghahanap ng higit na privacy kaysa sa "normal" na mga user ng Monero, at ang lahat ng mga user ay nakakakuha ng kapani-paniwalang pagtatanggi na gumastos sila ng mga pondo sa anumang partikular na transaksyon. Dahil ang mga pondo sa paggastos ng isang user ay hindi nakikipag-ugnayan o nakikilahok sa mga input ng decoy sa isang transaksyon, ang mga user na nagmamay-ari ng mga input na nangyari na napili bilang mga decoy ay maaaring matapat na sabihin na hindi sila nakikilahok sa transaksyon na iyon, na nagpapatibay sa kanilang privacy.

> Paggamit ng isang sentralisadong coordinator

Paggamit ng isang sentralisadong coordinator

Dahil ang mga ring signature ng Monero ay ganap na hindi magkakaugnay at nangangailangan lamang ng tunay na gumagastos ng mga pondo upang gawin ang transaksyon, hindi na kailangan ng isang sentralisadong coordinator sa Monero. Tinitiyak nito na _walang sinuman_ ang maaaring tanggihan ang iyong access sa privacy sa Monero, at walang sentralisadong entity na maaaring mapilit, walang madaling pag-atake ng Sybil sa liquidity, atbp. Hangga't ang iyong transaksyon ay nagbabayad ng wastong mga bayarin, nakakakuha ka ng walang censorable na access sa privacy, seguridad, at anonymity sa Monero.

> Ang CoinJoin ay nangangailangan ng pagkatubig

Ang CoinJoin ay nangangailangan ng pagkatubig

Ang "likido" na magagamit ng sinumang gumagastos ng Monero upang gamitin bilang mga decoy ay palaging ang kabuuang hanay ng mga output na on-chain kaya hindi kailanman magkakaroon ng kakulangan ng mga decoy na itatago sa Monero. Maaaring gawin ito ng isang taong gustong gumastos ng Monero ~20min pagkatapos makatanggap ng mga pondo, at hindi na kailangang magsagawa ng anumang karagdagang hakbang upang magkaroon ng matibay na privacy sa Monero.

> Ang privacy ng CoinJoin ay bumababa sa paglipas ng panahon

Ang privacy ng CoinJoin ay bumababa sa paglipas ng panahon

Dahil ang mga output ni Monero ay hindi kailanman kilala-ginagastos ng network, ang privacy na ibinibigay ng mga ring signature ay hindi gaanong madaling masira sa paglipas ng panahon. Ang isang user ay hindi kailangang patuloy na mag-churn ng mga output sa Monero, at sa labas ng napakabihirang mga pangyayari, hindi mawawalan ng privacy habang tumatagal.

Kung gusto ng isang user na "i-refresh" ang mga decoy na ginamit kasama ng isang output, gayunpaman, maaari lang nilang ipadala ang mga pondo pabalik sa kanilang sarili at magagawang gastusin ang mga ito ~20min mamaya gaya ng dati.

> Ang CoinJoin ay karaniwang nangangailangan ng mga fixed-size na input

Ang CoinJoin ay karaniwang nangangailangan ng mga fixed-size na input

Dahil nakatago ang mga halaga sa bawat transaksyon gamit ang [“Kumpidensyal na Mga Transaksyon”](/knowledge/monero-ringct) (isang bahagi ng “RingCT”), ang mga decoy na ginagamit sa anumang partikular na transaksyon ay maaaring maging anumang laki. Walang dahilan upang kailanganing mag-alala tungkol sa mga heuristic na nakabatay sa halaga sa Monero, at sa gayon ang mga transaksyon ay mas simple na gawin at maaaring magamit ang mga decoy mula sa anumang punto ng oras at ng anumang halaga sa Monero blockchain.

## Paano ako matututo ng higit pa?

## Paano ako matututo ng higit pa?

Kung interesado ka at gusto mong mas maunawaan ang mga ring signature o mga transaksyon sa CoinJoin, tingnan ang mga link sa ibaba para sa magagandang lugar para makapagsimula:

  * [Paano Nalalabo ng Mga Signature ng Ring ang Mga Output ni Monero](/knowledge/ring-signatures)
  * [Ring Signature - Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [Pangkalahatang-ideya ng CoinJoin](https://6102bitcoin.com/coinjoin-overview/)

Karagdagang pagbabasa

  * [Paano natatanging pinapagana ng Monero ang mga circular na ekonomiya](/knowledge/monero-circular-economies)/

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

  * [Monero Mining: Ano ang Nagiging Espesyal sa RandomX](/knowledge/monero-mining-randomx)/

  * [Bakit Mas Mahusay ang Monero kaysa Dash, Zcash, Zcoin (Kahit na may Lelantus), Grin at Bitcoin Mixers Like Wasabi (Na-update Mayo 2020)](/knowledge/why-monero-is-better)/

Karagdagang pagbabasa