---
title: "Saini za pete za Monero dhidi ya CoinJoin kama ilivyo kwa Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Kadiri zana za faragha za Bitcoin zinavyozidi kuzingatiwa na kutumiwa, zimekuwa chini ya uangalizi wa udhibiti zaidi. Uchunguzi huu umesababisha [tangazo la hivi majuzi](https://twitter.com/wasabiwallet/status/1503091503207432193) na zana ya faragha ya Bitcoin, Wasabi Wallet, kwamba wataanza kukagua na kukataa michanganyiko inayoingia kwa michanganyiko ambayo wanaona kuwa haramu au dhidi ya ToS yao, na watalipa uchanganuzi wa msururu. kampuni la "kuchunguza" washiriki mchanganyiko wanaoingia.

Matumizi ya miamala ya CoinJoin ili kuficha chanzo cha fedha katika Bitcoin imekuwa kiini cha faragha ya Bitcoin kwa miaka mingi sasa, na masuala na hatari zilizopo katika matumizi yake ni baadhi ya masuala ya msingi ambazo sahihi za pete za Monero husahihisha na kuzuia. .

Katika chapisho hili la blogu tutazama kwa ufupi katika ulinganisho wa CoinJoin na sahihi za pete, na pia kwa nini mbinu iliyochukuliwa katika Monero inasababisha upinzani mkubwa wa udhibiti, ufaragha mkubwa, na usumbufu mdogo kwa watumiaji.

## Muamala wa CoinJoin ni nini?

Kwa vile miamala yote ni wazi kabisa katika Bitcoin - ikionyesha mtumaji, mpokeaji na kiasi - watumiaji lazima wachukue hatua za ziada ili kuhifadhi faragha yao kutoka kwa watumaji wa awali na wapokeaji wa siku zijazo wa fedha zao au udhibiti wa hatari, ufuatiliaji au wizi wa fedha kupitia ukatili wa kimwili.

Suluhisho bora zaidi leo kwa faragha kwenye Bitcoin ni zana zinazoitwa [“CoinJoin”](https://bitcoiner.guide/qna/coinjoin/), ambapo watumiaji 2 au zaidi hufanya kazi pamoja (kwa kawaida kupitia mratibu mkuu) ili kuunda shughuli maalum ambazo zinafanya iwe vigumu kwa watu wa nje. waangalizi kuunganisha pembejeo na matokeo. Kila mshiriki huwasiliana ili kuunda muamala kwa pamoja bila kuwapa ulezi wa pesa zao, na hupokea pato mwishoni ambalo historia yake ya awali sasa haijulikani (au imefichwa) kwa waangalizi wa nje.

Hii inavunja historia ya UTXO maalum, kuruhusu watumiaji wa Bitcoin kupata kiasi fulani cha usiri wa mbele wakati wa kufanya miamala. Hata hivyo, CoinJoin (kama inavyotekelezwa katika Wasabi Wallet na Samourai Wallet, za aina mbili za CoinJoin zinazotumika zaidi kwa Bitcoin) ina shida chache kuu:

  * Kwa vile miamala ya CoinJoin hujijumuisha kabisa na inahitaji ushiriki amilifu, mshiriki yeyote lazima aonyeshe kuwa anatafuta faragha zaidi ya ile ya watumiaji wa "kawaida" wa Bitcoin, uwezekano wa kuwatenga na kusababisha masuala ya matumizi ya fedha katika kubadilishana au huluki nyingi zinazodhibitiwa. Kila mtumiaji hawezi kukataa kwamba alishiriki katika muamala wa CoinJoin.
  * Ili kupata wengine wa CoinJoin nao, mbinu zingine za CoinJoin (ikiwa ni pamoja na Wasabi Wallet) hutumia mratibu wa kati ambaye huwaunganisha washiriki na kuwasaidia kuwasiliana na kuunda muamala ufaao wa CoinJoin. Mratibu huyu wa serikali kuu kamwe hana uhifadhi wa pesa za mtumiaji, lakini anapata maarifa ya kina kuhusu miamala wanayoratibu, anaweza kukagua pembejeo zinazoingia (kama ilivyo kwa Wasabi Wallet), na anaweza kushinikizwa kukusanya au kushiriki maelezo kuhusu washiriki wa CoinJoin.
  * Watumiaji walio na kiasi kikubwa cha pesa kwa CoinJoin mara nyingi wanaweza kusubiri saa (au hata siku!) ili kupata washiriki wa kutosha wa CoinJoin nao, na kusababisha ucheleweshaji mkubwa kutoka wakati mtumiaji anapokea pesa hadi wakati anaweza kuzitumia kwa faragha. 
  * Faragha inayotolewa na muamala wa CoinJoin huharibika kadiri muda unavyopita washiriki wengine wanapotumia pesa au kuunganisha matokeo yao na utambulisho wao kupitia ubadilishanaji wa KYC, kitambulisho kinachohitaji wauzaji, n.k. Hii ina maana kwamba watumiaji huweka pesa zao kila mara katika miamala la CoinJoin ili kuhifadhi. kutokujulikana kwao kumewekwa (“umati wa kujificha”) safi iwezekanavyo.
  * Katika mbinu zingine za CoinJoin, washiriki lazima watumie UTXO ya ukubwa usiobadilika (yaani 0.1 BTC) ili kuifanya iwe vigumu kuunganisha pembejeo na matokeo la miamala la CoinJoin. Hii husababisha ada ya juu (miamala tofauti zaidi muhimu kwa kila pembejeo kubwa), "mabadiliko yenye sumu" zaidi (fedha ambazo hazitumiki bila hatari kubwa kwa faragha), na linaweza kuwazuia watumiaji wadogo wasichanganye kabisa ikiwa hawana. salio la chini linalohitajika.

## Je, sahihi za pete hutatua vipi masuala haya?

Kama [ tumechunguza kwa kina jinsi sahihi za pete zilivyo hapo awali](/knowledge/ring-signatures), sitaeleza kwa undani vipengele vya kiufundi vya jinsi zinavyofanya kazi katika chapisho hili la blogu. Badala yake, tutaangalia jinsi mbinu zinazochukuliwa katika Monero kutatua masuala na za CoinJoin kujadiliwa hapo juu.

> CoinJoin imejijumuisha na inahitaji ushiriki

Sahihi za pete za Monero ni vipengele vikuu vyaa itifaki vya faragha, na _kila_ muamala kwenye mtandao huzitumia. Hii inamaanisha kuwa hakuna miamala ya mtumiaji inayojitokeza kwa ajili ya kutafuta faragha zaidi kuliko watumiaji wa "kawaida" wa Monero, na watumiaji wote wanapata kukanushwa kuwa walitumia pesa katika shughuli yoyote ile. Kwa vile pesa za matumizi za mtumiaji haziratibu au kushiriki na pembejeo za udanganyifu katika muamala, watumiaji hao ambao wanamiliki pembejeo ambazo hutokea kwa kuchaguliwa kama wadanganyifu wanaweza kusema kwa uaminifu huwa hawakushiriki katika shughuli hizo, wakiimarisha faragha zao.

> Matumizi ya mratibu wa kati

Kwa vile saini za pete za Monero haziratibiwi kabisa na zinahitaji mtumiaji halisi wa pesa kuunda shughuli hizo, hakuna haja ya mratibu mkuu huko Monero. Hii inahakikisha kwamba _hakuna mtu_ anaweza kukunyima ufikiaji wa faragha huko Monero, na hakuna huluki ya serikali kuu inayoweza kushinikizwa, hakuna mashambulio rahisi ya Sybil dhidi ya ukwasi, n.k. Alimradi muamala wako unalipa ada zinazofaa, unapata ufikiaji usiopimika wa faragha, usalama, na kutokujulikana katika Monero.

> CoinJoin inahitaji ukwasi

“Uwezo” unaopatikana kwa mtu yeyote anayetumia Monero kutumia kama ulaghai huwa ni jumla ya matokeo kwenye msururu kwa hivyo kusiwe na upungufu wa madanganyiko ili kujificha ukitumia Monero. Mtu anayetaka kutumia Monero anaweza kufanya hivyo ~dakika 20 baada ya kupokea pesa, na hahitaji kuchukua hatua zozote za ziada ili kupata faragha thabiti huko Monero.

> Faragha za CoinJoin inashusha hadhi baada ya muda

Kwa vile matokeo ya Monero hayatumiwi kamwe na mtandao, faragha inayotolewa na sahihi za pete haiathiriwi sana na wakati. Mtumiaji hahitaji kuchakachua matokeo katika Monero kila mara, na nje ya hali nadra sana, hukosa faragha kadri muda unavyosonga.

Iwapo mtumiaji hatataka "kuonyesha upya" udanganyifu unaotumiwa na pato, hata hivyo, anaweza tu kutuma pesa kwake na kuweza kuzitumia ~dakika 20 baadaye kama kawaida.

> CoinJoin kwa kawaida huhitaji ingizo za ukubwa usiobadilika

Kwa vile kiasi hufichwa katika kila muamala kwa kutumia [ “Miamala ya Siri”](/knowledge/monero-ringct) (sehemu ya “RingCT”), udanganyifu unaotumiwa katika muamala wowote unaweza kuwa wa ukubwa wowote. Hakuna sababu ya kuhitaji kuwa na wasiwasi kuhusu urithi kulingana na kiasi katika Monero, na kwa hivyo miamala ni rahisi zaidi kuunda na inaweza kuongeza udanganyifu kutoka kwa wakati wowote na wa kiwango chochote kwenye msururu wa Monero.

## Ninawezaje kujifunza zaidi?

Ikiwa una hamu ya kujua na ungependa kuelewa vyema saini za pete au miamala ya CoinJoin, angalia viungo vilivyo hapa chini ili upate maeneo mazuri ya kuanza:

  * [Jinsi Sahihi za Mlio Huficha Mito ya Monero](/knowledge/ring-signatures)
  * [Sahihi ya Pete - Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Jiunge na Coin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [Muhtasari waJoinJoin](https://6102bitcoin.com/coinjoin-overview/)

Kusoma zaidi