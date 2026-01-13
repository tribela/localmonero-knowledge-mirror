---
title: "view tags: कैसे एक byte Monero wallet sync के समय को ४०%+ तक कम कर देगा"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monreo को दिन-प्रतिदिन उपयोग करने के बारे में सबसे आम शिकायतों में से एक यह है कि Monero भेजने में सक्षम होने से पहले बटुए को sync करने में समय लग सकता है। शुक्र है, Monero समुदाय के डेवलपर्स और शोधकर्ताओं ने बिना किसी अतिरिक्त blockchain कचरा(bloat), शुल्क आदि के अपने बटुए को sync करने में लगने वाले समय को ४०%+ तक कम करने का एक शानदार तरीका ढूंढ लिया है। 

"view tags", प्रत्येक लेन-देन के आंकडे में one-byte जोड़ - अगले नेटवर्क अपग्रेड में Monero पर आ रहा है! 

## Bitcoin की तुलना में Monero के बटुए का sync धीमा क्यों है?

View tags जैसे समाधान की आवश्यकता को बेहतर ढंग से समझने के लिए हमें जिन सवालों का जवाब देना है, उनमें से एक यह है कि Monero के बटुए का sync Bitcoin जैसी cryptocurrency की तुलना में धीमा क्यों है। 

Bitcoin में, क्योंकि सभी लेन-देन निजी नहीं हैं और खर्च किए जा रहे सिक्कों, राशियों और चेन पर शामिल पते को प्रकट करते हैं, Bitcoin बटुए बस किसी भी अप्रयुक्त लेनदेन आउटपुट (UTXOs) या किसी दिए गए बटुए के लिए उपयोग किए गए पते की तलाश कर सकते हैं। , केवल उन पतों के स्वामित्व वाले UTXOs के लिए blockchain को scan करके यह पता लगाने के लिए कि कौन से सिक्के आपके बटुए से संबंधित हैं और खर्च किए जा सकते हैं। 

पर Monero में, सभी लेनदेन प्रेषक, प्राप्तकर्ता और प्रत्येक लेनदेन में शामिल राशि को छिपाकर उपयोगकर्ता की गोपनीयता को सुरक्षित रखते हैं। यह गोपनीयता, जबकि नेटवर्क के उपयोगकर्ताओं की सुरक्षा के लिए महत्वपूर्ण है, धीमा बटुआ synchronisation भी पेश करती है। Monero में, आपके बटुए को आपके बटुए की निजी चाबियों के साथ नेटवर्क पर मौजूद प्रत्येक लेनदेन आउटपुट (TXO) की तुलना करनी होगी। 

इस तुलना में बहुत जटिल गणित और cryptography शामिल है, यह सत्यापित करने के लिए कि एक आउटपुट वास्तव में आपका है, क्योंकि सभी राशियाँ, पते और ज्ञात-खर्च(known-spent) किए गए उत्पाद (या सिक्के) Monero में chain पर छिपे हुए हैं। 

## view tags क्या होते हैं?

Monero बटुआ के लिए synchronization समय को कम करने में मदद करने के तरीके के रूप में, [ UkoeHB नाम के एक शोधकर्ता ने एक नया तरीका निकाला ](https://github.com/monero-project/research-lab/issues/73) \- केवल उस लेन-देन के प्रेषक और प्राप्तकर्ता को ज्ञात साझा रहस्य(shared secret) का उपयोग करके प्रत्येक लेनदेन में 1-byte "tag" जोड़ना। 

यह साझा रहस्य प्रेषक द्वारा प्राप्तकर्ता द्वारा प्रदान किए गए पते का उपयोग करके उत्पन्न किया जाता है, और प्रेषक और प्राप्तकर्ता द्वारा किसी भी सक्रिय सहयोग की आवश्यकता नहीं होती है। इस साझा रहस्य का पहला byte (या character) तब लेन-देन की जानकारी में जोड़ा जाता है जब इसे Monero नेटवर्क पर प्रकाशित किया जाता है। 

जब उस लेन-देन में भाग लेने वालों में से कोई अपने बटुए को Monero blockchain के साथ sync करना चाहता है, तो नेटवर्क पर प्रत्येक TXO के लिए सभी जटिल गणित और cryptography करने की आवश्यकता के बजाय, बटुआ अब केवल प्रत्येक लेन-देन में वह 1-byte field जाँच कर सकता है और उसके बाद ही उस tag वाले लेन-देन पर समय लेने वाला सत्यापन कर सकता है - नेटवर्क पर केवल १/२५६ TXO, सटीक होने के लिए! 

यह tag बाहरी दर्शकों के लिए लेन-देन के बारे में कोई जानकारी प्रकट नहीं करता है, लेन-देन के आकार में केवल 1-byte (एक नगण्य राशि) जोड़ता है, और फिर भी हमें आवश्यक जटिल सत्यापनों में कटौती करके sync समय को ४०%+ तक कम करने की अनुमति देता है! 

## View tags: एक सरलीकृत उदाहरण

कल्पना कीजिए कि आपके पास एक कमरे में ४,०९६ बक्से हैं, जिनमें से केवल ५ बक्से आपके हैं। बक्से बाहर से पूरी तरह से अप्रभेद्य हैं, और यह बताने का एकमात्र तरीका है कि कोई बक्सा आपके लिए है या नहीं, इसे खोलना है और यह सुनिश्चित करने के लिए अंदर लिखी गई समय लेने वाली गणित की समस्या को हल करना है। 

अब, कल्पना करें कि आप उन ५ बक्सों को भेजने वाले व्यक्ति को आपके पते का उपयोग करके एक विशेष कोड बनाने का निर्णय लेते हैं, और फिर आपको भेजे जाने वाले प्रत्येक बक्से के बाहर उस उत्पन्न कोड का केवल पहला वर्ण डालते हैं। हर कोई अपने बक्सों के लिए एक ही काम करता है (यह सुनिश्चित करने के लिए कि सभी बक्सों में अभी भी कोई अंतर नहीं है), लेकिन अब आप केवल बक्से के बाहर एक वर्ण कोड को देख सकते हैं, और केवल उन बक्सों को खोल सकते हैं जिन पर वह वर्ण है। 

जबकि अन्य बक्सा आपके कोड से मेल खाएँगे, यहाँ तक कि कुछ ऐसे बॉक्स भी जो आपके स्वामित्व में नहीं हैं, आपको गणित की समस्या को खोलने और हल करने के लिए आवश्यक बक्सों की संख्या सभी ४,०९६ के बजाय केवल १६ (१/२५६ बक्से!) है। 

अब आप उन 16 बक्सों को खोलें, गणित की समस्याओं को हल करें, और उन 5 बक्सों को रखें जो वास्तव में उस समूह के आपके हैं!

## Monero में view tag कब उपलब्ध होंगे?

View tags वर्तमान में [आगामी नेटवर्क अपग्रेड](https://github.com/monero-project/meta/issues/630) में शामिल करने के लिए नियोजित सुविधाओं में से एक है, और इसे इस वसंत में जारी किया जाना चाहिए। समुदाय ने view tags के विकास और कार्यान्वयन को प्रोत्साहित करने के लिए [२३.३XMR (लेखन के समय) उठाया](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) , और इसके परिणामस्वरूप Monero codebase में view tag को शामिल करने के लिए काम का विशाल बहुमत पहले से ही किया जा चुका है। समीक्षकों और शोधकर्ताओं के सहयोग से j-berman द्वारा पूरा किया गया। 

एक बार जब view tag नेटवर्क द्वारा लागू कर दिए जाते हैं, तो नेटवर्क अपग्रेड के बाद भेजे गए सभी लेन-देन बटुए sync समय में काफी सुधार से लाभान्वित होंगे। View tags का उपयोग शुरू करने के लिए आपको कुछ विशेष करने की आवश्यकता नहीं होगी, Monero के लिए आपका पसंदीदा बटुआ स्वचालित रूप से नेटवर्क अपग्रेड के बाद उनका उपयोग करना शुरू कर देगा! 

## मैं और अधिक कैसे सीखूँ?

यदि इसने view tags के बारे में आपकी जिज्ञासा को जगाया है, तो विषय में गहराई तक जाने वाले कुछ अतिरिक्त लिंक के लिए नीचे एक नज़र डालें:

  * [Reduce scan times with 1-byte-per-output ‘view tag'](https://github.com/monero-project/research-lab/issues/73)
  * [ Add view tags to outputs to reduce wallet scanning time ](https://github.com/monero-project/monero/pull/8061)

अग्रिम पठन

  * [कैसे Monero विशिष्ट रूप से परिपत्र अर्थव्यवस्थाओं को सक्षम बनाता है](/knowledge/monero-circular-economies/)

  * [Wasabi की तरह Monero के Ring Signature बनाम CoinJoin](/knowledge/ring-signatures-vs-coinjoin/)

  * [क्यों (और कैसे!) आपको अपनी चाबियां खुद रखनी चाहिए](/knowledge/hold-your-keys/)

  * [Monero में वापस योगदान करना](/knowledge/contributing-to-monero/)

  * [Remote nodes कैसे Monero की गोपनीयता को प्रभावित करते हैं](/knowledge/remote-nodes-privacy/)

  * [नेटवर्क को अपग्रेड करने के लिए Monero hard-forks का उपयोग कैसे करता है](/knowledge/network-upgrades/)

  * [P2Pool और Monero खनन के विकेंद्रीकरण में इसकी भूमिका](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Monero के लिए यह क्या करेगा](/knowledge/seraphis-for-monero/)

  * [क्या Bitcoin को Monero में बदलना उतना ही निजी है जितना कि सीधे मोनेरो को खरीदना?](/knowledge/most-private-way-to-buy-monero/)

  * [Monero ZCash के विपरीत एक भरोसा न लगने वाले(Trustless) प्रणाली का उपयोग क्यों करता है](/knowledge/monero-trustless-setup/)

  * [Bitcoin की तुलना में Monero मूल्य का एक बेहतर भण्डार क्यों है](/knowledge/monero-better-store-of-value/)

  * [Monero Bitcoin के नेटवर्क प्रभाव(network effect) से कैसे जीत सकता है](/knowledge/network-effect/)

  * [Monero के पास सबसे गंभीर सोच वाला समुदाय क्यों है](/knowledge/critical-thinking/)

  * [Monero का उपयोग करते समय इन घोटालों से बचें](/knowledge/monero-scams/)

  * [Monero में Atomic Swap कैसे काम करेगा](/knowledge/monero-atomic-swaps/)

  * [जब networking की बात आती है तो हर Monero उपयोगकर्ता को क्या पता होना चाहिए](/knowledge/monero-networking/)

  * [कैसे RingCT Monero लेनदेन राशि को छुपाता है](/knowledge/monero-ringct/)

  * [Monero Stealth Address आपकी पहचान को कैसे सुरक्षित रखता है](/knowledge/monero-stealth-addresses/)

  * [कैसे Monero Subaddress पहचान संयोजन को रोकते हैं](/knowledge/monero-subaddresses/)

  * [Monero Outputs समझाया गया](/knowledge/monero-outputs/)

  * [प्रारंभी लोगों के लिए Monero सर्वोत्तम प्रणाली](/knowledge/monero-best-practices/)

  * [Ring Signature कैसे Monero के उत्पादन को अस्पष्ट करते हैं](/knowledge/ring-signatures/)

  * [Monero ने Bitcoin को प्रभावित करने वाली block size की समस्या को कैसे हल किया](/knowledge/dynamic-block-size/)

  * [CLSAG कैसे Monero की दक्षता में सुधार करेगा](/knowledge/what-is-clsag/)

  * [Monero में Tail Emission क्यों है](/knowledge/monero-tail-emission/)

  * [Monero का एक संक्षिप्त इतिहास](/knowledge/monero-history/)

  * [Wired पत्रिका Monero के बारे में गलत है, जाने क्यों](/knowledge/wired-article-debunked/)

  * [शीर्ष 15 Monero मिथकों और चिंताओं को खारिज किया गया](/knowledge/monero-myths-debunked/)

  * [Dandelion++ कैसे Monero के लेन-देन की उत्पत्ति को निजी रखता है](/knowledge/monero-dandelion/)

  * [Monero खुला स्रोत(open source) और विकेंद्रीकृत क्यों है](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [मोनेरो खनन: क्या RandomX को इतना खास बनाता है](/knowledge/monero-mining-randomx/)

  * [Monero क्यों Dash, Zcash, Zcoin (यहाँ तक कि Lelantus के साथ भी), Grin and Bitcoin Mixers जैसे Wasabi से बेहतर है (संपादित मई २०२०)](/knowledge/why-monero-is-better/)