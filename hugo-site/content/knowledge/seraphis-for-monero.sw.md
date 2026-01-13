---
title: "Seraphis: Itafanya nini kwa Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: uboreshaji wa muundo wa msimu kwa shughuli za Monero

## Seraphis: uboreshaji wa muundo wa msimu kwa shughuli za Monero

Chapisho hili linafafanua [Seraphis](https://github.com/UkoeHB/Seraphis), seti ya miundo ya itifaki ya miamala na vifupisho vilivyoundwa na mchangiaji wa utafiti asiyejulikana jina bandia [`koe`](https://github.com/UkoeHB) kwa mfumo ikolojia ya Monero, na uchambuzi unaoendelea wa usalama na mchangiaji jina bandia [`coinstudent2048`](https://github.com/coinstudent2048).  
Tunafanya baadhi ya kurahisisha na kuacha maelezo fulani ya kiufundi kwa ajili ya uwazi; kwa sababu hii, na kwa sababu muundo wa Seraphis bado unaendelea, wasomaji wanaopendezwa wanapaswa kurejelea hati za Seraphis kwa habari za kisasa zaidi.

## Shughuli katika Monero

## Shughuli katika Monero

Itifaki kama vile Bitcoin na Monero na nyinginezo zinategemea kinachojulikana kama "muundo wa pato" wa uendeshaji, ambapo _output_ ni kiwakilishi cha thamani ambacho kinaweza kuhamishwa.  
Shughuli za malipo hutumia matokeo mmoja au zaidi zinazodhibitiwa na mtumaji, na kutoa matokeo mapya yanayoelekezwa kwa wapokeaji (au kurudi kwa mtumaji kama mabadiliko); muamala lazima usawazishe kwa kuwa matokeo yanayotumiwa lazima yawe na jumla ya thamani sawa na thamani katika matokeo mapya (pamoja na ada iliyowekwa na mtandao).  
Katika itifaki nyingi kama Bitcoin, thamani iliyo katika pato imeandikwa kwa uwazi, kama ilivyo kwa mpokeaji.  
Zaidi ya hayo, kwa kuangalia blockchain, ni jambo dogo kuona kama wakati pato limetumika (yaani, kama limetumika katika shughuli la baadaye, na ni shughuli gani iliyoitumia).

Kwa kulinganisha, itifaki kama vile Monero inaleta muundo tofauti:

  * Thamani za matokeo zimefichwa na hazionekani kwenye blockchain
  * Anwani za mpokeaji zimefichwa kwa kutumia itifaki ya kushughulikia mara mmoja
  * Iwapo pato limetumika au la limefichwa na utumizi wa sahihi za utata

Matokeo yake ni kwamba, kukosekana kwa taarifa ya nje, ni vigumu kubainisha kama pato fulani limetumika, thamani lake ni nini, na mpokeaji wake ni nani.

Itifaki ya kisasa ya muamala ya Monero inaitwa _RingCT_ , na hutumia vizuizi kadhaa vya ujenzi vya kriptografia kufikia malengo haya ya muundo.

  * _Ahadi_ huficha kiasi kwa njia ya manufaa ya hisabati
  * _Uthibitisho wa masafa_ huzuia mafuriko ambayo yanaweza kuongeza usambazaji
  * _Sahihi za pete zinazoweza kuunganishwa_ hutoa utata wa mtu aliyetia sahihi na kuzuia majaribio ya kutumia mara mbili
  * _Mapunguzo ya ahadi_ yanadai kuwa salio la miamala

Vita vya ujenzi vimeunganishwa kwa uangalifu ili kuunda itifaki ya RingCT.

Sifa muhimu za itifaki ya RingCT ni kwamba baadhi ya vitalu vya ujenzi vinaweza kubadilishwa au kuboreshwa kwa njia ambayo itadumisha muundo na sifa kwa ujumla, lakini hiyo inaweza kutoa ufanisi au uboreshaji wa usalama. Kwa kweli, aina hizi za uboreshaji zimetokea (au zimepangwa kutokea) mara kadhaa katika historia wa Monero. Uthibitisho wa anuwai katika itifaki ya awali ya RingCT ulikuwa mwingi na polepole; baadaye zilisasishwa hadi muundo unaoitwa [Bulletproofs](https://eprint.iacr.org/2017/1066) ambao ulifanya miamala kuwa ndogo na haraka zaidi kwa uchanganuzi bora wa usalama, na zimepangwa kusasishwa hadi muundo mpya unaoitwa [Bulletproofs+](https://eprint.iacr.org/2020/735) kwa manufaa makubwa zaidi za ufanisi. 

Mchakato sawia ulifanywa na kizuizi cha ujenzi cha sahihi ya pete. Katika itifaki asili, ujenzi unaoitwa [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34) ulitumiwa. Hili lilisasishwa baadaye kuwa ujenzi mpya unaoitwa [CLSAG](https://eprint.iacr.org/2019/654) ambao ni wa haraka zaidi, unaosababisha miamala midogo, na una uchanganuzi bora wa usalama. Muundo mpya zaidi wa sahihi wa pete unaoweza kuunganishwa kulingana na [Triptych](https://eprint.iacr.org/2020/018) ulipendekezwa, lakini hii haikuchaguliwa kupelekwa kwa sababu ya athari zake kwenye shughuli za saini nyingi.

## Maserafi

## Maserafi

Seraphis huchukua wazo hili hatua zaidi.  
Badala ya kusasisha miundo mahususi ya itifaki ya muamala iliyopo ya RingCT, inaleta itifaki tofauti inayoweza kuchukua faida ya vizuizi tofauti vya ujenzi na kutoa utendakazi ulioboreshwa.

## Vitalu vya ujenzi

## Vitalu vya ujenzi

Seraphis hutumia seti tofauti za miundo ya kriptografia kufikia malengo yake ya muundo.

  * _Ahadi_ bado huficha kiasi
  * _Uthibitisho wa masafa_ bado huzuia kufurika na ugavi mfumuko wa bei
  * _Uthibitisho wa uanachama_ hutoa utata wa mtu aliyetia sahihi
  * _Mapungufu ya ahadi_ bado yanadai salio
  * _Uthibitisho unaoidhinisha_ huzuia majaribio ya kutumia mara mbili

Angalia mabadiliko hapa: sahihi za pete zinazoweza kuunganishwa hubadilishwa na mchanganyiko wa uthibitisho wa uanachama na uthibitisho wa kuidhinisha. Kwa kusema, uthibitisho wa uanachama unaonyesha kuwa pato linalotumiwa ni sehemu ya seti kubwa, sawa na kile kinachotokea katika RingCT. Lakini tofauti na RingCT, uthibitisho wa uanachama hauhusishi lebo ya kuunganisha hata kidogo! Uthibitisho unaoidhinisha unaonyesha kuwa lebo ya kuunganisha ni halali na inatumiwa kutia sahihi shughuli ya mwisho.

Kwa sababu RingCT huweka lebo ya kuunganisha kwenye sahihi isiyoeleweka, shughuli za kutia saini (na saini nyingi sana) ni za kimahesabu zaidi, na inakuwa vigumu zaidi kuunda utendakazi mwingine unaohusiana na lebo. Lakini katika Seraphis, kuunda uthibitisho wa uanachama kunaweza kukabidhiwa kwa usalama kutoka kwa vifaa vinavyoaminika sana (ambavyo vinaweza kuwa na nguvu ndogo za kompyuta, kama pochi la vifaa) kwa kifaa kisichoaminika sana, na utendakazi wa kusaini (na saini nyingi sana) ni rahisi zaidi kwa kutumia uthibitisho rahisi zaidi wa kuidhinisha. .

Kwa bahati nzuri, baadhi ya vijenzi vinavyohitajika na Seraphis tayari vipo mahali pengine, na havihitaji kutengenezwa kuanzia mwanzo. Miundo wa kuzuia risasi na+ujenzi unaweza kutumika kama uthibitisho wa anuwai. Marekebisho ya mifumo ya uthibitishaji ya aina ya Schnorr unaweza kutumika kuidhinisha uthibitisho. Na [mfumo bora wa kuthibitisha](https://eprint.iacr.org/2015/643) ambao tayari umetumika kama msingi wa Triptych, [Lelantus](https://eprint.iacr.org/2019/373), na [Spark](https://eprint.iacr.org/2021/1173)* unaweza kurekebishwa kwa uthibitisho.

* Cypher Stack unapokea ufadhili wa ukuzaji wa Spark.

## Akihutubia

## Akihutubia

Kwa bahati mbaya, anwani za Monero zinazotumika sasa hazioani na Seraphis. Watumiaji wangehitaji kutoa anwani mpya kutoka kwenye funguo zao za pochi ili kupokea Monero ikiwa Seraphis ingetekelezwa. Hata hivyo, gharama hii ya mfumo ikolojia huja na manufaa mengi.

Kando na manufaa ya kimuundo yaliyojadiliwa hapo juu, muundo wa Seraphis unaweza kufaa kwa uwezekano mwingi wa ujenzi wa anwani, ambapo kila mmoja huja na mabadiliko. Ingawa muundo wa mwisho wa anwani utakaotumiwa katika Seraphis [bado unaamuliwa](https://github.com/monero-project/research-lab/issues/92) (mpango mmoja unaoangaliwa sana unaitwa [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), tunaweza kueleza baadhi vya vipengele vya kawaida na umuhimu.

Unaweza kujua kwamba anwani za Monero hutoa _ufunguo wa kutazama_ , ambapo unaweza kutoa ufunguo wa kutazama kwa kifaa au mtu mwingine na kuiruhusu kutazama matokeo yanayoingia kwa niaba yako, lakini bila kuacha kutumia mamlaka. Hii ni muhimu kwa pochi, ambalo linaweza kusasishwa huku ufunguo wako wa kutumia ukiwa umefungwa kwa usalama. Ni muhimu pia kwa hali ambapo unataka ufikiaji wa mwonekano wa nje, kama vile shirika la kutoa msaada la umma linalotoa uwazi au kampuni iliyo na idara ya uhasibu.

Hali mbaya ya funguo za kutazama za Monero ni kwamba hazitoi ufikiaji kamili au mzuri wa kutazama. Haiwezekani kutambua kwa uhakika wakati pochi inapotumia pesa, jambo ambalo hufanya iwe vigumu kukokotoa salio la pochi vizuri wakati ufunguo wa kutumia haupatikani. Pia haiwezekani kwa sasa kugundua matokeo yanayoingia bila pia kujifunza thamani iliyo katika matokeo hayo (hiyo inamaanisha wahusika wengine wowote wanaohusika na kutafuta matokeo yanayokuja watajifunza ni kiasi gani Monero unapata).

Serafi zinazoshughulikia ujenzi zinaweza kutatua hili. Ukiwa na Seraphis, anwani lako huja ikiwa na vitufe tofauti vinavyoweza kufanya mambo tofauti:

  * Tazama matokeo yanayoingia, lakini ficha thamani lake
  * Tazama matokeo yanayoingia, lakini onyesha thamani lake
  * Tazama matokeo yanayotoka
  * Kukusaidia kutengeneza miamala, lakini usitie saini
  * Tengeneza anwani mpya (zinazofaa kwa wauzaji reja-reja au kubadilishana na wateja wengi)

Kama mwenye anwani, unaweza kuamua ni kiasi gani cha mamlaka utakayokabidhi kwa vifaa vingine au wahusika wengine.

## Picha kubwa

## Picha kubwa

Seraphis ni badiliko kubwa kwa mfumo ikolojia wa Monero. Ingawa inahusisha marekebisho ya anwani na vizuizi vya ujenzi wa miamala, muundo yake hutoa unyumbufu na utendakazi muhimu ambao hauwezekani kwa itifaki ya leo ya RingCT. Ingawa sehemu kubwa ya usanifu inakamilishwa na kuendelezwa kuwa [utekelezaji](https://github.com/UkoeHB/monero/tree/seraphis_lib), muundo wa anwani na uchanganuzi wa usalama unaendelea. Seraphis inatoa fursa nzuri ya kusukuma mfumo ikolojia wa Monero mbele!

Kusoma zaidi

  * [Jinsi Monero huwezesha kwa njia ya kipekee uchumi wa mduara](/knowledge/monero-circular-economies)/

  * [Saini za pete za Monero dhidi ya CoinJoin kama ilivyo kwa Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Kwa nini (na jinsi!) unapaswa kushikilia funguo zako mwenyewe](/knowledge/hold-your-keys)/

  * [Inachangia tena kwa Monero](/knowledge/contributing-to-monero)/

  * [Jinsi nodi za mbali zinavyoathiri faragha ya Monero](/knowledge/remote-nodes-privacy)/

  * [Jinsi Monero hutumia uma-ngumu ili kuboresha mtandao](/knowledge/network-upgrades)/

  * [Tazama lebo: Jinsi baiti moja itapunguza nyakati za usawazishaji wa pochi ya Monero kwa 40%+](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool na Jukumu Lake katika Kugatua Uchimbaji wa Monero](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Je, Kubadilisha Bitcoin kuwa Monero Ni Faragha Kama Kununua Monero Moja kwa Moja?](/knowledge/most-private-way-to-buy-monero)/

  * [Kwa nini Monero Anatumia Usanidi Usioaminika Tofauti na Zcash](/knowledge/monero-trustless-setup)/

  * [Kwa nini Monero Ni Duka Bora la Thamani Kuliko Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Jinsi Monero Inaweza Kushinda Athari za Mtandao za Bitcoin](/knowledge/network-effect)/

  * [Kwa nini Monero Ana Jumuiya Muhimu Zaidi ya Kufikiri](/knowledge/critical-thinking)/

  * [Ulaghai wa Kuangalia Unapotumia Monero](/knowledge/monero-scams)/

  * [Jinsi Ubadilishanaji wa Atomiki Utafanya Kazi huko Monero](/knowledge/monero-atomic-swaps)/

  * [Nini Kila Mtumiaji wa Monero Anahitaji Kujua Linapokuja suala la Mitandao](/knowledge/monero-networking)/

  * [Jinsi RingCT Huficha Kiasi cha Muamala wa Monero](/knowledge/monero-ringct)/

  * [Jinsi Monero Siri Mali HuLinda Utambulisho Wako](/knowledge/monero-stealth-addresses)/

  * [Jinsi Anwani Ndogo za Monero Zinazuia Kuunganisha Utambulisho](/knowledge/monero-subaddresses)/

  * [Matokeo ya Monero Yamefafanuliwa](/knowledge/monero-outputs)/

  * [Mbinu Bora za Monero kwa Wanaoanza](/knowledge/monero-best-practices)/

  * [Jinsi Sahihi za Pete Huficha Mito ya Monero](/knowledge/ring-signatures)/

  * [Jinsi Monero Alivyotatua Tatizo la Ukubwa wa Block Ambayo Inakumba Bitcoin](/knowledge/dynamic-block-size)/

  * [Jinsi CLSAG Itakavyoboresha Ufanisi wa Monero](/knowledge/what-is-clsag)/

  * [Kwa nini Monero Ina Utoaji wa Mkia](/knowledge/monero-tail-emission)/

  * [Historia fupi ya Monero](/knowledge/monero-history)/

  * [Jarida la Wired lina makosa Kuhusu Monero, Hii ndio Sababu](/knowledge/wired-article-debunked)/

  * [Hadithi na Maswala 15 Bora ya Monero Yalipingwa](/knowledge/monero-myths-debunked)/

  * [Jinsi Dandelion++ Huweka Asili ya Muamala wa Monero Faragha](/knowledge/monero-dandelion)/

  * [Kwa nini Monero Ni Chanzo Huria na Imegawanywa](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Uchimbaji wa Monero: Ni Nini Hufanya RandomX Kuwa Maalum](/knowledge/monero-mining-randomx)/

  * [Kwa nini Monero ni Bora kuliko Dash, Zcash, Zcoin (Hata na Lelantus), Grin na Mchanganyiko wa Bitcoin Kama Wasabi (Ilisasishwa Mei 2020)](/knowledge/why-monero-is-better)/

Kusoma zaidi