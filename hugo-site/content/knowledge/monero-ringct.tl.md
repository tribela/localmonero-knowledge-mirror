---
title: "Paano Itinatago ng RingCT ang Mga Halaga ng Transaksyon ng Monero"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Ang pagkapribado ng Monero ay hindi nakadepende sa isang natatanging mekanismo na, kung masira, ay maghahayag ng kabuuan ng mga transaksyon, ngunit sa halip ay tatlong magkakaibang teknolohiya na gumagana nang magkasabay upang magbigay ng holistic na privacy habang binabayaran ang mga kahinaan ng iba pang bahagi. Ang three-prong approach na ito ay binubuo ng [ring signature](/knowledge/ring-signatures), RingCT, at [stealth address](/knowledge/monero-stealth-addresses). Itinatago ng tatlong teknolohiyang ito ang tunay na output (nagpadala), halaga, at tatanggap ayon sa pagkakabanggit. Ngayon ay pag-uusapan natin ang tungkol sa RingCT.

Maaaring ang RingCT ang pinaka-teknikal sa tatlo, at maaaring mahirap unawain, kaya hindi namin tatalakayin nang eksakto kung paano ito gumagana, ngunit sa halip ay ipakita kung paano posibleng hindi malaman ang isang halaga at kumpirmahin pa rin ang mga bagay tungkol dito . At huwag mag-alala, gagamit kami ng maraming halimbawa gaya ng dati.

Una, tuklasin natin kung bakit mahalagang i-verify ang anuman tungkol sa mga halaga. Bakit hindi na lang natin sila ganap na ilihim? Ang sagot ay, may mga matalinong paraan na ang mga tao ay maaaring lumikha ng pera mula sa manipis na hangin kung bibigyan ng pagkakataon. Paano maaaring gumana ang isang bagay na tulad nito? Tingnan natin ang isang halimbawa.

Kung gusto mong bumili ng item mula sa iyong kaibigan, at gusto niya ng sampung dolyar para dito, magsisimula ka sa sampung dolyar at magsisimula siya sa zero. Pagkatapos mong ibigay sa kanya ang sampung dolyar, mayroon siyang sampung dolyar at zero ka. Nagsimula ka sa sampu, at ngayon ay mayroon na siyang sampu. Walang nalikha o nawasak na pera sa transaksyong ito.

Sa mga cryptocurrencies, ang isang matalinong indibidwal ay maaaring magbigay ng sampung dolyar para sa item at sa halip na makatanggap ng zero dollars bilang pagbabago, maaari silang makatanggap ng dalawang dolyar pabalik. Sa halip na 0 at 10 na humahantong sa 10 at 0 (o 10=10), ito ay 0 at 10 na humahantong sa 10 at 2 (o 10=12). Dalawang Monero ay nilikha lamang mula sa manipis na hangin. Maaari mong isipin na kung gagawin ito ng indibidwal sa kanilang sarili nang ilang beses, makakaipon sila ng napakalaking kayamanan sa maikling panahon.

Sa Bitcoin at iba pa, magiging madali itong makita. Tinitingnan mo ang mga input na pumapasok sa isang transaksyon at ang mga output na lumalabas at siguraduhin na kung ano ang ipinadala ay katumbas ng kung ano ang natanggap. Kung ang mga halagang ito ay naka-encrypt at hindi nakikita, ang isang user ay walang paraan ng pag-verify na kung ano ang ipinadala at kung ano ang natanggap ay pareho.

Sa pagtatangkang pataasin ang privacy ng Bitcoin, nilikha ni Gregory Maxwell ang Confidential Transactions (CT), isang bagong teknolohiya na magbibigay-daan para sa mga naka-encrypt na halaga, habang pinatutunayan na walang nilikha o nawasak sa proseso. Tulad ng karamihan sa teknolohiya ng privacy, hindi ito nakapasok sa Bitcoin, ngunit masigasig si Monero na gamitin ito. May isang problema lang. Ang ipinatupad na teknolohiya ng mga pirma ng singsing ay hindi tugma sa iminungkahing ideya. Kaya, isa sa mga mananaliksik ng MRL noong panahong iyon, si Shen Noether, ay binago ang CT sa RingCT, isang bersyon ng CT na tugma sa mga pirma ng singsing.

Muli, medyo teknikal ang paraan ng paggawa nito, at mahirap ipaliwanag sa isang panimulang artikulo. Para sa mahilig sa cryptography na dapat lang malaman, maraming malalalim na artikulo na nakasulat sa internet tungkol sa mga panloob na gawain ng CT. Para sa iba pa sa atin, ipapakita ng artikulong ito kung paano posibleng itago ang mga halaga, ngunit patunayan pa rin na walang nilikha o nawasak.

Sabihin natin na gustong magpadala ni Alice ng pera kay Bob. Magpapadala si Alice ng 10 XMR kay Bob, na tatanggap ng 10 XMR. 10=10 kaya walang mali dito. Ngunit ayaw ni Alice na malaman ng sinuman kung magkano ang kanyang ipinapadala. Kaya gumawa sila ni Bob ng isang shared secret. Basically number na silang dalawa lang ang nakakaalam. Sabihin nating ang numerong iyon ay 22. Ngayon, pinarami ni Alice ang 10 (kung ano talaga ang ipinapadala niya) sa 22 upang makakuha ng 220. Ito ang numerong ibinabahagi niya sa network.

Ang mga minero mismo ay hindi alam ang sikretong numero. Kung ginawa nila, maaari nilang hatiin ang numerong ipinapakita sa kanila ng sikretong numero at makuha ang tunay na halagang ipinadala. Ngunit dahil wala sila, hindi nila magagawa. Nakikita nila na makakatanggap si Bob ng 220. 220 ang ipinadala. 220 ang natanggap. 220 = 220. Sa ganitong paraan, mabe-verify ng network na walang Monero ang nalikha o nawasak, lahat nang hindi nalalaman ang tunay na halaga na ipinadala ni Alice kay Bob.

Dahil alam ni Bob ang nakabahaging lihim na numero, kapag natanggap niya ang pera, hinahati na lang niya sa 22 para makuha ang tunay na halaga na ipinadala ni Alice, 10. Parehong alam nina Alice at Bob kung magkano ang ipinadala at magkano ang natanggap, habang lahat ng iba ay binibigyan ng maling numero.

Muli, hindi ito ang aktwal na paraan kung saan gumagana ang CT, ngunit nagbibigay ito ng ideya kung paano posible ang isang bagay na tulad nito. Ang totoong paraan ay nagsasangkot ng mga bagay tulad ng mga pangako ng Pedersen, dalawang ipinadalang halaga (isang naka-encrypt na halaga sa tatanggap at isang halaga ng pangako sa network), at...oo, madali nang makita kung paano mawawala ang isang tao sa lahat ng iyon.

Gayunpaman, isang bagay na dapat tandaan, ay habang itinatago ng RingCT ang halagang nakipagtransaksyon sa pagitan ng dalawang partido sa isang transaksyon, hindi nito itinatago ang dalawa pang hanay ng mga numero.

Ang una ay ang mga transaksyon sa coinbase. Kung ang terminong ito ay hindi pamilyar sa iyo, ito ay karaniwang nangangahulugan ng gantimpala na nakukuha ng mga minero para sa paghahanap ng susunod na bloke. Hindi nakatago ang numerong ito. Makikita ng sinuman kung magkano ang iginawad ng protocol sa isang minero para sa kanilang serbisyo. Sa ganitong paraan, ang kasalukuyang halaga ng Monero na umiiral ay maaaring malaman sa pamamagitan ng pagdaragdag ng lahat ng mga transaksyon sa coinbase. Ang kanilang kabuuan ay katumbas ng kasalukuyang Monero sa sirkulasyon.

Ang pangalawang numero na hindi nakatago ay ang bayad na ibinayad sa mga minero kapag nagpadala ng transaksyon ang isang user. Kailangang malinaw ang mga bayarin para malaman ng mga minero kung sino ang uunahin. Ito ay isang paraan na maaaring saktan ng mga user ang kanilang privacy gayunpaman, na parang may gumagamit ng kakaibang bayad sa minero sa tuwing magpapadala sila ng transaksyon (tulad ng 0.12345), kung gayon ang kanilang mga transaksyon ay maaaring i-link.

Bukod sa mga kasong ito, ang RingCT ay nagtatago ng mga halaga ng Monero mula noong 2017, at ang aming kolektibong privacy ay mas malakas para dito.

Karagdagang pagbabasa