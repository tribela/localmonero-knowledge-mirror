---
title: "Sa hannun zoben Monero vs CoinJoin kamar a cikin Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Kamar yadda kayan aikin sirri na Bitcoin suka sami ƙarin kulawa da amfani, sun shiga ƙarƙashin ƙarin bincike na tsari. Wannan binciken ya haifar da sanarwar [ kwanan nan ](https://twitter.com/wasabiwallet/status/1503091503207432193) ta kayan aikin sirri na Bitcoin, Wasabi Wallet, cewa za su fara tantancewa da ƙin abubuwan da ke shigowa don haɗawa waɗanda suke ganin ba daidai ba ne ko kuma a kan ToS ɗin su, kuma za su biya binciken sarkar. kamfani don "vet" mahalarta mahaɗa masu shigowa.

Amfani da ma'amalar CoinJoin don toshe tushen kuɗi a cikin Bitcoin ya kasance tushen sirrin Bitcoin shekaru da yawa yanzu, kuma batutuwa da haɗarin da ke tattare da amfani da shi wasu daga cikin mahimman batutuwan da zoben Monero ya sa hannu daidai da hanawa. 

A cikin wannan shafin yanar gizon za mu ɗan ɗan nutse cikin kwatancen CoinJoin da sa hannun zobe, da kuma dalilin da yasa tsarin da aka ɗauka a Monero yana haifar da juriya mai girma, babban sirri, da ƙarancin wahala ga masu amfani.

## Menene ma'amalar CoinJoin?

Kamar yadda duk ma'amaloli suke gabaɗaya a cikin Bitcoin - suna bayyana mai aikawa, mai karɓa, da adadin kuɗi - masu amfani dole ne su ɗauki ƙarin matakai don kiyaye sirrin su daga masu aikawa da suka gabata da kuma masu karɓar kuɗinsu na gaba ko yin haɗari, sa ido, ko satar kuɗi ta hanyar. tashin hankali na jiki.

Mafi kyawun bayani a yau don sirri akan Bitcoin shine kayan aiki da ake kira ["CoinJoin"](https://bitcoiner.guide/qna/coinjoin/), inda 2 ko fiye masu amfani ke aiki tare (yawanci ta hanyar mai gudanarwa na tsakiya) don ƙirƙirar ma'amala ta musamman wanda ke ba da wahala ga waje. masu sa ido don haɗa abubuwan shigar da abubuwan da aka fitar. Kowane ɗan takara yana sadarwa don haɗin gwiwa don gina ma'amala ba tare da ba da izinin kula da kuɗin su ba, kuma yana karɓar fitarwa a ƙarshen wanda tarihin da ya gabata ba a bayyana shi ba (ko ɓoye) ga masu sa ido na waje.

Wannan ya karya tarihin takamaiman UTXOs, yana bawa masu amfani da Bitcoin damar samun wani tsari na sirrin gaba yayin mu'amala. Koyaya, CoinJoin (kamar yadda aka aiwatar a Wasabi Wallet da Samorai Wallet, kayan aikin CoinJoin guda biyu da aka fi amfani da su don Bitcoin) yana da ƴan manyan matsaloli:

  * Kamar yadda ma'amaloli na CoinJoin ke shiga gabaɗaya kuma suna buƙatar sa hannu mai aiki, kowane ɗan takara dole ya nuna cewa suna neman sirrin sirri fiye da na masu amfani da Bitcoin na “al'ada”, mai yuwuwar ware su da haifar da al'amurran kashe kuɗi a yawancin musanya ko ƙungiyoyi. Kowane mai amfani ba zai iya musun cewa sun shiga cikin ma'amalar CoinJoin ba.
  * Domin nemo wasu zuwa CoinJoin tare da, mafi yawan hanyoyin zuwa CoinJoin (ciki har da Wasabi Wallet) suna amfani da mai gudanarwa na tsakiya wanda ke haɗa mahalarta kuma yana taimaka musu sadarwa da gina ma'amala mai dacewa ta CoinJoin. Wannan mai gudanarwa na tsakiya bai taɓa samun ikon kula da kuɗin mai amfani ba, amma yana samun zurfin fahimta game da ma'amalar da suke daidaitawa, yana iya tantance abubuwan da ke shigowa (kamar yadda yake a cikin Wasabi Wallet), kuma ana iya matsawa cikin tattara ko raba bayanai game da mahalarta CoinJoin.
] 
  * Masu amfani tare da babban adadin kuɗi zuwa CoinJoin sau da yawa suna jira sa'o'i (ko ma kwanaki!) Don samun isassun mahalarta zuwa CoinJoin tare da, haifar da babban jinkiri daga lokacin da mai amfani ya karɓi kuɗi zuwa lokacin da zasu iya kashe su a asirce. 
  * Sirrin da aka bayar ta hanyar ma'amala ta CoinJoin yana raguwa akan lokaci yayin da sauran mahalarta ke kashe kuɗi ko danganta abubuwan da suka samu zuwa ainihin su ta hanyar musayar KYC, ID ɗin da ke buƙatar yan kasuwa, da sauransu. An saita rashin sanin sunan su ("taron don ɓoye a ciki") sabo da zai yiwu.
  * A mafi yawan hanyoyin zuwa CoinJoin, dole ne mahalarta suyi amfani da ƙayyadaddun UTXO (watau 0.1 BTC) don yin wahalar haɗa abubuwan da aka samu da abubuwan da aka samu na ma'amalar CoinJoin. Wannan yana haifar da ƙarin kudade (ƙarin ma'amaloli daban-daban waɗanda ake buƙata kowane babban shigarwar), ƙarin “canjin mai guba” (kuɗin da ba za a iya kashewa ba tare da haɗari mai haɗari ga keɓancewa), kuma yana iya hana ƙananan masu amfani damar haɗawa kwata-kwata idan ba su da. mafi ƙarancin ma'auni da ake buƙata.

## Ta yaya sa hannun zobe ke warware waɗannan batutuwa?

Kamar yadda [ mun yi zurfin bincike kan abin da sa hannun zobe ke da shi a baya](/knowledge/ring-signatures), ba zan yi cikakken bayani game da fasahohin fasaha na yadda suke aiki a cikin wannan gidan yanar gizon ba. Madadin haka, za mu kalli yadda hanyoyin da aka ɗauka a Monero ke warware matsalolin tare da CoinJoin ya tattauna a sama.

> CoinJoin ya shiga kuma yana buƙatar shiga

CoinJoin ya shiga kuma yana buƙatar shiga

Sa hannun zoben Monero shine ainihin fasalin ƙa'idar sirri, kuma _kowane ma'amala_ akan hanyar sadarwa yana amfani da su. Wannan yana nufin cewa babu wani ma'amalar mai amfani da ya fito don neman mafi girman sirri fiye da masu amfani da Monero na yau da kullun, kuma duk masu amfani suna samun ƙin yarda cewa sun kashe kuɗi a kowace ciniki. Kamar yadda mai amfani da kuɗin kashe kuɗi ba ya haɗawa ko shiga tare da bayanan yaudara a cikin ma'amala, masu amfani waɗanda suka mallaki abubuwan da suka faru da za a zaɓa azaman yaudara za su iya cewa ba sa shiga cikin wannan ma'amala, suna ƙarfafa sirrin su.

> Amfani da mai gudanarwa na tsakiya

Amfani da mai gudanarwa na tsakiya

Kamar yadda sa hannun zoben Monero gabaɗaya ba su da haɗin kai kuma suna buƙatar mai kashe kuɗi na gaske kawai don ƙirƙirar ma'amala, babu buƙatar mai gudanarwa na tsakiya a Monero. Wannan yana tabbatar da cewa _babu wanda_ zai iya hana ku samun damar sirri a Monero, kuma babu wani yanki na tsakiya wanda za'a iya matsawa, babu sauki Sybil kai hari kan ruwa, da dai sauransu. Muddin ma'amalarku ta biya kudaden da suka dace, kuna samun damar da ba za a iya tantancewa ba ga keɓantawa, tsaro, da ɓoyewa a Monero.

> CoinJoin yana buƙatar ruwa 

CoinJoin yana buƙatar ruwa 

“ruwa” da ke akwai ga duk wanda ke kashe Monero don amfani da shi azaman kayan kwalliya koyaushe shine jimillar abubuwan da aka fitar akan sarkar don haka ba a taɓa samun ƙarancin yaudara don ɓoyewa tare da Monero. Wani mai neman kashe Monero zai iya yin haka ~ 20minti bayan ya karɓi kuɗi, kuma baya buƙatar yin wasu ƙarin matakai don samun sirri mai ƙarfi a Monero.

CoinJoin sirrin yana raguwa akan lokaci

Kamar yadda ba a taɓa sanin abubuwan da Monero ke bayarwa ta hanyar hanyar sadarwa ba, sirrin da aka bayar ta sa hannun zobe ba shi da saurin lalacewa kan lokaci. Mai amfani baya buƙatar ci gaba da murƙushe abubuwan samarwa a Monero, kuma a waje da yanayin da ba kasafai ba, ba ya rasa sirri yayin da lokaci ke ci gaba.

Idan mai amfani yana son "sakewa" abubuwan da aka yi amfani da su tare da fitarwa, duk da haka, za su iya mayar da kuɗin ga kansu kawai kuma su iya kashe su ~ 20min daga baya kamar yadda suka saba.

> CoinJoin yawanci yana buƙatar ƙayyadaddun bayanai masu girman girman

CoinJoin yawanci yana buƙatar ƙayyadaddun bayanai masu girman girman

Kamar yadda adadin kuɗi ke ɓoye a cikin kowace ma'amala ta amfani da [ "Ma'amaloli na Sirri"](/knowledge/monero-ringct) (wani ɓangare na "RingCT"), yaudarar da aka yi amfani da ita a kowace ciniki na iya zama kowane girman. Babu wani dalili da za a buƙaci damuwa game da ilimin lissafi na tushen kuɗi a Monero, don haka ma'amaloli sun fi sauƙi don ginawa kuma suna iya yin amfani da lalata daga kowane lokaci a lokaci da kowane adadin akan Monero blockchain.

## Ta yaya zan iya ƙarin koyo?

Idan kuna sha'awar kuma kuna son ƙarin fahimtar sa hannun zobe ko ma'amalar CoinJoin, duba hanyoyin haɗin da ke ƙasa don manyan wurare don farawa:

  * [Yadda Sa hannu na Zobe ke ɓoye Fitar Monero](/knowledge/ring-signatures)
  * [ Sa hannu na zobe - Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [ CoinJoin Overview](https://6102bitcoin.com/coinjoin-overview/)

Kara karantawa

  * [Yadda Monero ke ba da damar tattalin arzikin madauwari ta musamman](/knowledge/monero-circular-economies/)

  * [Me yasa (kuma ta yaya!) yakamata ku riƙe maɓallan ku](/knowledge/hold-your-keys/)

  * [Gudunmawar komawa ga Monero](/knowledge/contributing-to-monero/)

  * [Yadda nodes masu nisa ke tasiri sirrin Monero](/knowledge/remote-nodes-privacy/)

  * [Yadda Monero ke amfani da cokali mai yatsa don haɓaka hanyar sadarwa](/knowledge/network-upgrades/)

  * [Duba tags: Yadda byte ɗaya zai rage lokutan daidaitawa na walat ɗin Monero da 40%+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool da Matsayinsa a Rarraba Ma'adinai na Monero](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Abin da Zai Yi wa Monero](/knowledge/seraphis-for-monero/)

  * [Shin Canza Bitcoin zuwa Monero yana da zaman kansa kamar siyan Monero kai tsaye?](/knowledge/most-private-way-to-buy-monero/)

  * [Me yasa Monero ke Amfani da Saitin Amintacce Ba kamar Zcash ba](/knowledge/monero-trustless-setup/)

  * [Me yasa Monero ya fi Bitcoin daraja](/knowledge/monero-better-store-of-value/)

  * [Ta yaya Monero zai iya shawo kan Tasirin hanyar sadarwa na Bitcoin](/knowledge/network-effect/)

  * [Me yasa Monero ke da Mafi Mahimman Tunani Al'umma](/knowledge/critical-thinking/)

  * [Zamba don Kalli Lokacin Amfani da Monero](/knowledge/monero-scams/)

  * [Yadda Atomic Swaps Zai Yi Aiki a Monero](/knowledge/monero-atomic-swaps/)

  * [Abin da Kowane Mai Amfani da Monero Ya Bukatar Sanin Lokacin da Ya zo kan hanyar sadarwa](/knowledge/monero-networking/)

  * [Yadda RingCT ke ɓoye Adadin Kasuwancin Monero](/knowledge/monero-ringct/)

  * [Yadda Monero Stealth Adresoshin Ya Kare Imaninku](/knowledge/monero-stealth-addresses/)

  * [Yadda Monero Subaddresses ke Hana Haɗin Shaida](/knowledge/monero-subaddresses/)

  * [An Bayyana Fitar Monero](/knowledge/monero-outputs/)

  * [Mafi kyawun Ayyuka na Monero don Masu farawa](/knowledge/monero-best-practices/)

  * [Yadda Sa hannu na zobe ke ɓoye abubuwan da Monero ke bayarwa](/knowledge/ring-signatures/)

  * [Yadda Monero Ya Warware Matsalolin Girman Toshe wanda ke addabar Bitcoin](/knowledge/dynamic-block-size/)

  * [Yadda CLSAG Zai Inganta Ingantacciyar Monero](/knowledge/what-is-clsag/)

  * [Me yasa Monero ke fitar da wutsiya](/knowledge/monero-tail-emission/)

  * [Takaitaccen Tarihin Monero](/knowledge/monero-history/)

  * [Mujallar Wired ba daidai ba ce Game da Monero, Ga dalilin da ya sa](/knowledge/wired-article-debunked/)

  * [Manyan Tatsuniyoyi 15 na Monero da Abubuwan da Aka Kashe](/knowledge/monero-myths-debunked/)

  * [Yadda Dandelion++ ke Keɓance Ma'amalar Monero Mai zaman kansa](/knowledge/monero-dandelion/)

  * [Me yasa Monero Buɗaɗɗen Madogara da Rarraba](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Abin da ke Sa RandomX ta Musamman](/knowledge/monero-mining-randomx/)

  * [Me yasa Monero ya fi Dash, Zcash, Zcoin (Ko da Lelantus), Grin da Bitcoin Mixers Kamar Wasabi (An sabunta Mayu 2020)](/knowledge/why-monero-is-better/)