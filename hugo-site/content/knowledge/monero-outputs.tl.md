---
title: "Ipinaliwanag ang Mga Output ng Monero"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Ang Monero, tulad ng iba pang cryptocurrencies, ay gumagamit ng mga output bilang paraan ng accounting para sa mga pondo. Maraming mga gumagamit ng crypto savvy ang malamang na narinig ang terminong ito dati, ngunit hindi lahat ay nauunawaan kung ano ang ibig nilang sabihin at kung paano sila gumagana. Gaya ng ginalugad sa aming artikulo sa [ring signatures](/knowledge/ring-signatures), ang mga output ay ang aktwal na yunit na ipinagpapalit sa blockchain sa pagitan ng mga nakikipagtransaksyon na partido. Katulad ng isang dollar bill, ngunit ang halaga ay wala sa isang nakapirming denominasyon.

Kung mababayaran ka ng $16 para sa isang trabaho, maaari kang makatanggap ng isang dollar bill, isang limang dollar bill, at isang sampung dollar bill. Mayroon kang $16, ngunit mayroon ka ring tatlong magkakaibang singil sa iyong wallet. Kung gusto mong bayaran ang isang tao ng 6 na dolyar, maaari mong gamitin ang 5 at ang 1 na bayarin, ngunit kung gusto mong magbayad ng $8 sa isang tao maaari mo lamang gamitin ang $10 at makatanggap ng $2 bilang pagbabago. Panghuli, kung gusto mong magbayad ng $14 sa isang tao kailangan mong gamitin ang lahat ng tatlong bill, at makakatanggap ka ng $2 bilang sukli, ngunit sa ilang sandali, kapag ibinigay mo ang lahat ng tatlong bill, wala kang pera sa iyong wallet hanggang sa makuha mo ang bumalik ka.

Gumagana nang katulad ang Monero. Ipagpalagay na nagpapatakbo ka ng isang tindahan at gumawa ng tatlong benta sa tatlong magkakaibang mga item. Maaari kang makatanggap ng 1.5 XMR, 2.25 XMR, at 5.25 XMR para sa kabuuang 9 XMR, ngunit mayroon ka ring tatlong magkakaibang mga output sa iyong wallet ng mga denominasyong nakasaad dati. Katulad ng sa dolyar, baka gusto mong magbayad ng 3 XMR sa isang tao. Maaari mong gamitin lamang ang 5.25 XMR na output, at makatanggap ng 2.25 XMR bilang pagbabago, o maaari mong pagsamahin ang 1.5 at 2.25 XMR na mga output at makakuha ng 0.75 XMR bilang pagbabago.

Ngunit, sa sandaling ipadala mo ang transaksyon, ang mga output na ginagamit mo ay inilalagay sa isang "naka-lock" na estado, ibig sabihin ay hindi naa-access ang mga ito hanggang sa matanggap mo muli ang pagbabago. Ina-unlock ng protocol ang mga pondo (ibig sabihin, ibabalik sa iyo ang pagbabago) pagkatapos ng 10 kumpirmasyon, o humigit-kumulang 20 minuto. Tulad ng sa sandaling ibigay mo ang mga perang papel mula sa iyong wallet, hindi mo magagamit muli ang pera hanggang sa matanggap mo ang sukli pabalik mula sa cashier, hindi maa-access ang iyong Monero hanggang sa matanggap mo muli ang sukli.

Bumalik tayo sa halimbawa ng pagpapadala ng 3 XMR sa isang tao, at ginagamit mo ang 5.25 XMR na output. Ngayon, habang hinihintay mo ang iyong 1.75 XMR pabalik sa pagbabago, hindi mo ito magagamit. Ang 1.75 XMR na ito ay hindi naa-access sa iyo. Ngunit maaari mo pa ring gamitin ang 1.5 XMR at 2.25 XMR na mga output, dahil ang mga ito ay hindi ginastos. Bumalik sa halimbawa ng dolyar, kung binayaran mo ang isang tao ng $8, tulad ng sa halimbawa dati, hindi mo magagamit ang $2 na inaasahan mong babalik sa pagbabago hanggang sa maibigay ito sa iyo, ngunit sa halimbawang ito, mayroon ka pa ring $10 na bill na hindi nagamit sa iyong wallet. Magagamit pa rin ito para bumili ng kahit anong gusto mo habang hinihintay mo ang pagbabago. Ganoon din sa Monero.

Ito ay madalas na isang punto ng pagkalito para sa mga bagong user ng Monero. Kadalasan, ang isang user ay maaaring magkaroon lamang ng isang output sa kanilang wallet, na natanggap mula sa isang exchange o isang kaibigan. Sabihin nating ang output na ito ay 20 XMR. Wala silang ibang output sa wallet nila. Nais na nilang magbigay ng donasyon sa dalawa sa kanilang mga paboritong kawanggawa. Nagpapadala sila ng 5 XMR sa unang charity at pagkatapos ay nalilito dahil, kahit na dapat ay mayroon silang 15 XMR na natitira, hindi nila agad maipadala ang susunod na donasyon sa pangalawang kawanggawa. Gaya ng nahulaan mo, ito ay dahil naka-lock ang 15 XMR. Hindi ito maaaring gastusin hanggang sa maibalik ito bilang pagbabago (10 kumpirmasyon o humigit-kumulang 20 minuto). Pagkatapos ma-unlock ang kanilang mga pondo, maipadala na nila ang kanilang pangalawang donasyon.

Upang ulitin ang punto, hindi sila magkakaroon ng problemang ito kung mayroon na lang silang maraming output, gaya ng dalawang 10 XMR output o katulad. Magagawa nilang magpadala ng parehong mga donasyon nang sunud-sunod, dahil ang unang donasyon ay gagamit ng isa sa 10 XMR output (at maghintay ng 10 kumpirmasyon upang makatanggap ng 5 XMR pabalik bilang pagbabago), at ang pangalawang donasyon ay gagamit ng isa pang 10 XMR output.

Ang ilang mga wallet ng cryptocurrency ay may feature na tinatawag na 'output management', na nagpapakita lamang sa isang user kung aling mga output ang mayroon sila sa kasalukuyan (bilang karagdagan sa kanilang kabuuang kabuuan), at nagbibigay-daan din sa kanila na pumili kung alin ang gusto nilang gamitin kapag gumastos sila. kanilang cryptocurrency.

Sa ngayon, ang Monero GUI ay awtomatikong gumagawa ng pagpili ng output para sa mga user, dahil ang mga user na pumipili ng sarili nilang mga output ay kadalasang humahantong sa pagkalito o, sa ilang mga kaso, nakakapinsala sa privacy. Gayunpaman, may mga wallet na ginagawa, gaya ng bagong proyekto ng Feather wallet, na maglalaman ng mga feature na ito sa pamamahala ng output.

Marami kaming pinag-uusapan tungkol sa bahagi ng pagpapadala, ngunit may isang bagay na kamangha-manghang nangyayari sa receiving end. Kung babalikan ang aming halimbawa ng pagpapadala ng 3 XMR sa isang tao, at paggamit ng iyong 1.5 XMR at 2.25 XMR na mga output sa transaksyon (habang umaasa sa 0.75 XMR sa pagbabago), HINDI tumatanggap ang receiver ng dalawang output na 1.5 XMR at 2.25 XMR. Sa halip ay tumatanggap sila ng ONE 3 XMR output.

Sa background, pinagsasama ng protocol ang lahat ng output na ginagamit para sa paggastos, at binibigyan ang receiver ng isang output ng binabayarang halaga, at nagpapadala ng isang pagbabagong output pabalik sa nagpadala. Kaya't ang nagpadala ay makakatanggap din ng isang output pabalik bilang pagbabago, hindi alintana kung gumamit sila ng dalawa, tatlo, o sampung output upang ipadala ang transaksyon.

Umaasa kaming naalis nito ang ilang kalituhan tungkol sa mga output at kung paano gumagana ang internal accounting ng protocol, pati na rin ang karaniwang user na nahaharap sa problema ng kalituhan kapag nakakaranas ng mga naka-lock na pondo. Sa isa pang artikulo, tutuklasin namin ang pamamahala sa iyong mga output upang mabawasan ang pagkakataong maghintay para sa mga naka-unlock na pondo bago magpadala ng mga transaksyon sa hinaharap.

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