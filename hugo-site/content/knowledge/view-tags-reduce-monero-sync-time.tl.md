---
title: "Tingnan ang mga tag: Paano babawasan ng isang byte ang mga oras ng pag-sync ng Monero wallet ng 40%+"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Isa sa mga pinakakaraniwang reklamo sa paggamit ng Monero araw-araw ay ang oras na maaaring tumagal upang mag-sync ng wallet bago maipadala si Monero. Sa kabutihang palad, ang mga developer at mananaliksik sa komunidad ng Monero ay nakahanap ng napakahusay na paraan upang bawasan ang oras na aabutin mo upang i-sync ang iyong wallet ng 40%+ nang walang anumang idinagdag na blockchain bloat, mga bayarin, atbp.

Ilagay ang “view tags”, isang one-byte na karagdagan sa data ng bawat transaksyon – darating sa Monero sa susunod na pag-upgrade ng network!

## Bakit mas mabagal ang pag-sync ng wallet ni Monero kaysa sa Bitcoin?

Isa sa mga unang tanong na kailangan naming sagutin para mas maunawaan ang pangangailangan para sa solusyon tulad ng mga view tag ay kung bakit mas mabagal ang pag-sync ng wallet ni Monero kaysa sa mga cryptocurrencies tulad ng Bitcoin.

Sa Bitcoin, dahil ang lahat ng mga transaksyon ay hindi pribado at ipinapakita ang mga coin na ginagastos, ang mga halaga, at ang mga address na kasangkot sa kadena, ang mga wallet ng Bitcoin ay maaaring maghanap lamang ng anumang hindi nagastos na mga output ng transaksyon (UTXO) o ginamit na mga address para sa isang partikular na wallet , mabilis na ini-scan ang blockchain para sa mga UTXO lamang na pagmamay-ari ng mga address na iyon upang malaman kung aling mga barya ang nabibilang sa iyong wallet at maaaring gastusin.

Sa Monero, gayunpaman, pinapanatili ng lahat ng transaksyon ang privacy ng user sa pamamagitan ng pagtatago sa nagpadala, tagatanggap, at mga halagang kasama sa bawat transaksyon. Ang privacy na ito, habang mahalaga sa pagprotekta sa mga user ng network, ay nagpapakilala rin ng mas mabagal na pag-synchronize ng wallet. Sa Monero, kailangang ihambing ng iyong wallet ang bawat output ng transaksyon (TXO) na umiiral sa network sa mga pribadong key ng iyong wallet.

Ang paghahambing na ito ay nagsasangkot ng maraming kumplikadong matematika at cryptography upang patunayan na ang isang output ay tunay na sa iyo, dahil ang lahat ng mga halaga, address, at kilalang-ginastos na mga output (o mga barya) ay nakatago on-chain sa Monero.

## Ano ang view tags?

Bilang isang paraan upang makatulong na bawasan ang oras ng pag-synchronize para sa mga wallet ng Monero, [isang researcher na nagngangalang UkoeHB ang nakaisip ng isang bagong diskarte](https://github.com/monero-project/research-lab/issues/73) – magdagdag ng 1-byte na “tag” sa bawat transaksyon gamit ang isang nakabahaging lihim na alam lang sa nagpadala at tumanggap ng transaksyong iyon.

Ang nakabahaging lihim na ito ay nabuo ng nagpadala gamit ang address na ibinigay sa kanila ng tatanggap, at hindi nangangailangan ng anumang aktibong pakikipagtulungan ng nagpadala at tagatanggap. Ang unang byte (o character) ng nakabahaging lihim na ito ay idinaragdag sa data ng transaksyon kapag na-publish ito sa Monero network.

Kapag ang isa sa mga kalahok sa transaksyong iyon ay nais na i-sync ang kanilang wallet sa Monero blockchain pagkatapos, sa halip na kailanganing gawin ang lahat ng kumplikadong matematika at cryptography para sa bawat at bawat TXO sa network, maaari na ngayong suriin ng wallet ang para sa ang 1-byte na field na iyon sa bawat transaksyon at pagkatapos lamang gawin ang matagal na pag-verify sa mga transaksyong may tag na iyon – 1/256 TXO sa network, upang maging tumpak!

Ang tag na ito ay hindi naghahayag ng anumang impormasyon tungkol sa transaksyon sa mga manonood sa labas, nagdaragdag lamang ng 1-byte (isang hindi gaanong halaga) sa mga laki ng transaksyon, at gayon pa man ay nagbibigay-daan sa amin na bawasan ang mga oras ng pag-sync ng 40%+ sa pamamagitan ng pagbabawas sa mga kumplikadong pag-verify kailangan!

## Tingnan ang mga tag: isang pinasimpleng halimbawa

Isipin na mayroon kang 4,096 na kahon sa isang silid, kung saan 5 kahon lang ang pag-aari mo. Ang mga kahon ay ganap na hindi nakikilala mula sa labas, at ang tanging paraan upang malaman kung ang isang kahon ay para sa iyo ay buksan ito at lutasin ang isang matagal na problema sa matematika na nakasulat sa loob upang matiyak na ito ay sa iyo.

Ngayon, isipin na nagpasya kang gagawa ang taong nagpadala sa iyo ng 5 kahon na iyon ng isang espesyal na code gamit ang iyong address, at pagkatapos ay ilagay lamang ang unang character ng nabuong code na iyon sa labas ng bawat kahon na ipapadala sa iyo. Ang iba ay gumagawa ng parehong bagay para sa kanilang mga kahon (upang matiyak na ang lahat ng mga kahon ay hindi pa rin nakikilala), ngunit ngayon ay maaari mo na lamang tingnan ang isang code ng character sa labas ng kahon, at buksan lamang ang mga kahon na may ganoong karakter sa kanila.[ X753X] 

Bagama't tutugma ang ibang mga kahon sa iyong code, kahit na ang ilan ay hindi mo pagmamay-ari, ang bilang ng mga kahon na kailangan mong buksan at lutasin ang isang problema sa matematika ay 16 (1/256 na kahon!) na lang sa halip na lahat ng 4,096. 

Ngayon, buksan mo ang 16 na kahon na iyon, lutasin ang mga problema sa matematika, at panatilihin ang 5 kahon na aktuwal na pag-aari mo mula sa pangkat na iyon!

## Kailan magiging available ang mga view na tag sa Monero?

Ang mga tag ng view ay isa sa mga feature na kasalukuyang pinaplano para sa pagsasama sa [paparating na pag-upgrade ng network](https://github.com/monero-project/meta/issues/630), at dapat na ilabas ilang oras ngayong tagsibol. Ang komunidad [ay nagtaas ng 23.3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (sa oras ng pagsulat) upang bigyang-insentibo ang pagbuo at pagpapatupad ng mga tag ng view, at bilang resulta, ang karamihan sa gawaing magsama ng mga tag ng view sa Monero code base ay naisagawa na. kinumpleto ni j-berman sa pakikipagtulungan ng mga reviewer at researcher.

Kapag ipinatupad na ng network ang mga view tag, lahat ng transaksyong ipinadala pagkatapos ng pag-upgrade sa network ay makikinabang sa napakahusay na oras ng pag-sync ng wallet. Hindi mo na kakailanganing gumawa ng anumang espesyal upang simulan ang paggamit ng mga view tag, ang iyong paboritong wallet para sa Monero ay magsisimulang gamitin ang mga ito pagkatapos ng awtomatikong pag-upgrade ng network!

## Paano ako matututo ng higit pa?

Kung napukaw nito ang iyong pagkamausisa tungkol sa mga tag ng view, tingnan sa ibaba ang ilang karagdagang link na malalim ang papasok sa paksa:

  * [Bawasan ang mga oras ng pag-scan gamit ang 1-byte-per-output na 'view tag'](https://github.com/monero-project/research-lab/issues/73)
  * [Magdagdag ng mga view tag sa mga output para mabawasan ang oras ng pag-scan ng wallet](https://github.com/monero-project/monero/pull/8061)

Karagdagang pagbabasa