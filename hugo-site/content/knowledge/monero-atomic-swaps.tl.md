---
title: "Paano Gumagana ang Atomic Swaps sa Monero"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Sa paghahangad ng desentralisasyon at isang tunay na walang pahintulot na sistema, ilang bagay ang hinahangad sa espasyo ng cryptocurrency gaya ng mga desentralisadong palitan at pagpapalit ng atomic. Mula nang magsimula ito, nahirapan si Monero na ipatupad ang mga atomic swap, dahil ang mga feature sa privacy ay lumilikha ng mga natatanging problema kapag sinusubukang magdisenyo ng protocol.

Ngunit una, mag-back up tayo. Ano ang atomic swap? Ang atomic swap ay isang protocol kung saan ang dalawang magkaibang cryptocurrencies, sa magkaibang blockchain, ay maaaring palitan sa paraang walang tiwala na walang tagapamagitan. Nangangahulugan ito kung nais ng isang tao na palitan ang cryptocurrency A para sa cryptocurrency B, magagawa nila ito nang walang palitan, sentralisado o desentralisado. Tulad ng maaaring isipin ng isa, nangangailangan ito ng malaking pananaliksik, at ang buong teknikal na mga detalye na ginagawang posible ay nagiging kumplikado. Muli, narito ang LocalMonero upang tumulong at magbigay ng simpleng paliwanag para sa karaniwang tao.

Upang magsimula, isaalang-alang natin ang pinakasimpleng anyo ng atomic swap, gaya ng ipinatupad ng Bitcoin. Kung nais ng isang tao na palitan ang Bitcoin ng isa pang coin na gumagamit ng parehong teknolohiya ng kontrata ng hash time lock, magagawa nila ito sa sumusunod na paraan. Si Alice ay may Bitcoin (BTC), ngunit gusto ng Litecoin (LTC), at si Bob ay may LTC, ngunit gusto ng BTC. Nagpasya silang gumawa ng atomic swap para makuha ng bawat isa ang coin na gusto nila. Ipinadala ni Alice ang kanyang BTC sa isang espesyal na address, gamit ang mga script na nakakandado sa mga pondo kaya kahit siya ay hindi ma-access ito. Maaari mong isipin na parang inilagay ni Alice ang kanyang BTC sa isang lockbox. Kapag ginawa ang lockbox, makakakuha siya ng susi, at nagpapadala ng hash ng susi na ito kay Bob. Ngayon ay wala na sa sarili ni Bob ang susi, ang hash lang, kaya hindi pa niya ma-access ang mga pondo.

Ginagamit ni Bob ang hash na ito bilang isang binhi kung saan siya bumuo ng sarili niyang lockbox, at ipinadala ang kanyang LTC doon, kung saan ito ay naka-lock din. Dahil ang hash ng susi ni Alice ay ginamit bilang binhi kung saan ginawa ang lockbox ni Bob, magagamit niya ang kanyang susi para i-claim ang LTC sa lockbox ni Bob. Kasya ang susi niya! Ngunit, gamit ang math voodoo magic, kapag ginamit niya ang kanyang susi para buksan ang LTC lock, ibinunyag niya ang susi kay Bob, na maaaring gumamit nito upang kunin ang BTC na inilagay niya sa kanyang lockbox. Sa ganitong paraan, nang walang tagapamagitan, matagumpay na napalitan nina Alice at Bob ang kanilang mga ari-arian.

Ngunit may kaunting problema. Paano kung magpadala si Alice sa kanyang lockbox, at nagpasya si Bob na ayaw na niyang mag-trade. Ngayon, dahil hindi ma-access ni Alice ang kanyang BTC na na-lock niya, at hindi makukumpleto ni Bob ang kanyang bahagi ng transaksyon, mawawala na lang si Alice sa kanyang pera. Well, sa kabutihang-palad, ang Bitcoin ay may kaunting teknolohiyang tinatawag na mga transaksyon sa pag-refund, at kaya pagkatapos ng isang yugto ng panahon, kung ang BTC ay hindi na-claim ni Bob, ang mga script ay may fail-safe na built in, kung saan ang BTC ay awtomatikong babalik kay Alice. Ito ang pangunahing speedbump para sa pagpapatupad ng atomic swaps ng Monero. Dahil sa teknolohiya ng privacy ng [ring signatures ng Monero](/knowledge/ring-signatures), palaging hindi sigurado ang nagpadala ng isang transaksyon. Paano makakagawa ang protocol ng transaksyon sa refund kung kahit na hindi nito alam kung saan nanggaling ang transaksyon?

Noong 2017, isang maliit na grupo ng mga mananaliksik ang nagbalangkas ng ibang paraan kung saan gagana ang mga atomic swap sa Monero. Pagkatapos ng ilang taon ng pagpipino, tinapos ng mga mananaliksik ang isang proseso kung saan makakagawa si Monero ng atomic swaps sa Bitcoin, kahit na walang mga transaksyon sa refund.

Tulad ng maraming bagay sa antas ng teknikal na kumplikadong ito, ang aming paliwanag ay labis na magpapasimple ng ilang bagay upang maihatid ang ideya, ngunit magbibigay pa rin ito ng matibay na ideya ng mga mekanismo kung saan gagana ang prosesong ito.

Parehong sina Alice (na may XMR at gustong BTC) at Bob (na may BTC at gustong XMR) ay dapat mag-download at magpatakbo ng program na sumusuporta sa atomic swap. Ito ay maaaring ipatupad sa mga wallet, desentralisadong palitan, o espesyal, partikular na mga programa, ngunit ang software ay dapat na nagpapatakbo ng atomic swap protocol. Sa unang hakbang, kumonekta ang mga kliyente nina Alice at Bob sa isa't isa at gumawa ng ilang nakabahaging lihim at susi. Sa hakbang na ito, gumawa ng bagong Monero address, kung saan si Alice ang may kalahati ng susi, at si Bob ang may isa pa. Wala pang Monero doon, kaya walang gagastusin. Isang huling bagay na dapat tandaan tungkol sa address na ito, ay pareho silang may view key sa wallet na ito, kaya maaari silang parehong sumilip sa loob upang makita kung o kailan dumating si Monero.

Sa ikalawang hakbang, ipinadala ni Bob ang kanyang BTC sa isang espesyal na address, katulad ng Bitcoin atomic swap protocol na napag-usapan na natin. Pagkatapos makita ni Alice na dumating ang BTC sa address na ito sa blockchain, ipinadala niya ang kanyang Monero sa Monero address kung saan pareho silang may kalahati ng susi. Maaaring i-verify ni Bob na dumating ang Monero dahil mayroon din siyang view key, at kapag nakita niyang ligtas na ang Monero sa wallet, pinadalhan niya si Alice ng isang piraso ng susi na magbibigay-daan sa kanya na bawiin ang Bitcoin. Katulad ng iba pang protocol, ang proseso ng pag-claim ng Bitcoin ay nagpapakita ng kanyang kalahati ng Monero key kay Bob. Ngayon ay mayroon nang dalawang kalahati si Bob, upang maangkin niya ang Monero, habang si Alice ay mayroon lamang ang kanyang kalahati, kaya hindi niya maaaring subukang kunin ito bago niya makuha.

Kaya kung titingnan mo ang lahat ng ito at medyo nalilito pa rin kung paano nalutas ni Monero ang problema ng mga transaksyon sa refund, ang sagot ay medyo simple. Dahil ang Monero mismo ay walang mga transaksyon sa pag-refund, dapat mapansin ng mambabasa na ang Bitcoin (na mayroong mga transaksyon sa pag-refund) ay unang ipinadala, at pagkatapos lamang na ma-verify na nasa blockchain ay ipinadala ang Monero. Nagbibigay-daan ito sa Monero na gamitin ang kakayahan ng Bitcoin na mag-script sa mga transaksyon sa pag-refund at samantalahin ang mga ito, nang hindi kinakailangang magkaroon ng mga kakayahan na ito mismo.

Kumpleto na ang atomic swap, ngunit mula rito, may dalawang opsyon si Bob para sa kanyang bagong na-claim na XMR. Maaari niyang gamitin ang Monero wallet na ito, o ilipat ang XMR sa isa pang wallet na pagmamay-ari na niya. Malamang na ililipat ni Bob ang Monero sa isa pang wallet, dahil hawak pa rin ni Alice ang view key at nakikita niya ang loob.

Ang kagandahan ng protocol na ito ay medyo bago pa rin ito, at maraming puwang para sa mga pag-optimize. Medyo flexible din ito sa arkitektura nito, kaya ang pagpapatupad sa iba pang mga wallet o mga desentralisadong palitan ay dapat na simple at maayos na akma sa kanilang kasalukuyang arkitektura.

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