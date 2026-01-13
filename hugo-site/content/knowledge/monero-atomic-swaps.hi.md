---
title: "Monero में Atomic Swap कैसे काम करेगा"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
विकेन्द्रीकरण और वास्तव में अनुमति रहित प्रणाली की खोज में, कुछ चीजें Cryptocurrency समाज में विकेंद्रीकृत बाज़ारों और Atomic Swap के रूप में प्रतिष्ठित हैं। अपनी स्थापना के बाद से, Monero ने Atomic Swap को लागू करने के लिए संघर्ष किया है, क्योंकि गोपनीयता सुविधाएँ एक protocol को अभिकल्पन करने की कोशिश करते समय अद्वितीय समस्याएँ पैदा करती हैं। 

लेकिन पहले, आइए पीछे जाते हैं। Atomic Swap क्या हैं? Atomic Swap एक ऐसा protocol है जिसके द्वारा दो अलग-अलग cryptocurrency, अलग-अलग blockchain पर, बिना किसी मध्यस्थ के एक भरोसेमंद तरीके से लेनदेन किया जा सकता है। इसका मतलब यह है कि अगर कोई crypocurrnecy B के लिए cryptocurrency A का आदान-प्रदान करना चाहता है, तो वे बिना बाज़ार(exchange), केंद्रीकृत या विकेंद्रीकृत के ऐसा करने में सक्षम होंगे। जैसा कि कोई कल्पना कर सकता है, इसके लिए काफी शोध करना पड़ता है, और इसे संभव बनाने वाले पूर्ण तकनीकी विवरण काफी जटिल हो जाते हैं। एक बार फिर, LocalMonero यहाँ आम लोगों की मदद करने और सरल व्याख्या देने के लिए है। 

शुरू करने के लिए, Atomic Swap के सबसे सरल रूप पर विचार करें, जैसा कि Bitcoin द्वारा लागू किया गया है। यदि कोई Bitcoin को दूसरे सिक्के के लिए बदल करना चाहता है जो उसी hash time lock contract तकनीक का उपयोग करता है, तो वे निम्नलिखित तरीके से ऐसा कर सकते हैं। Alice के पास Bitcoin (BTC) है, लेकिन Litecoin (LTC) चाहता है, और Bob के पास LTC है, लेकिन BTC चाहता है। वे एक Atomic Swap करने का निर्णय लेते हैं ताकि प्रत्येक को वह सिक्का मिले जो वे चाहते हैं। Alice अपने BTC को एक विशेष पते पर भेजती है, script का उपयोग करती है जो पैसों को बन्ध कर देती है ताकि वह इसे ले न सके। आप इसे ऐसे सोच सकते हैं जैसे Alice अपने BTC को एक तिजोरी में रखती है। जब तिजोरी बन जाती है, तो उसे एक चाबी मिलती है, और इस चाबी का एक hash Bob को भेजती है। अब Bob के पास स्वयं कुंजी नहीं है, केवल hash है, इसलिए वह अभी तक निधियों तक नहीं पहुँच सकता है। 

Bob इस hash को एक बीज के रूप में उपयोग करता है जिससे वह अपना खुद की तिजोरी बनाता है, और वहाँ अपना LTC भेजता है, जहाँ यह बंध भी होता है। क्योंकि Alice की कुंजी के हैश का उपयोग बीज के रूप में किया गया था जिसके द्वारा Bob की तिजोरी बनाई गई थी, वह Bob की तिजोरी में LTC का दावा करने के लिए अपनी कुंजी का उपयोग कर सकती है। उसकी चाबी ठीक बैठती है! लेकिन, गणित के जादू का उपयोग करते हुए, जब वह LTC पर का ताला खोलने के लिए अपनी चाबी का उपयोग करती है, तो वह Bob को चाबी बताती है, जो तब BTC का दावा करने के लिए इसका इस्तेमाल कर सकता है जिसे उसने अपनी तिजोरी में रखा था। इस तरह, बिना किसी मध्यस्थ के, Alice और Bob ने सफलतापूर्वक अपनी संपत्ति का आदान-प्रदान किया है। 

लेकिन थोड़ी समस्या है। क्या होगा अगर Alice अपनी तिजोरी में भेजती है, और Bob फैसला करता है कि वह अब और व्यापार नहीं करना चाहता। अब, क्योंकि Alice अपने BTC तक नहीं पहुँच सकती है जिसे उसने बंद कर दिया है, और Bob लेन-देन का अपना हिस्सा पूरा नहीं करेगा, ऐलिस हमेशा के लिए अपना पैसा खो देती है। खैर, सौभाग्य से, Bitcoin में refund transaction नामक एक छोटी सी तकनीक है, और इसलिए समय की अवधि के बाद, यदि Bob द्वारा BTC का दावा नहीं किया जाता है, तो script में एक fail-safe अंतर्निहित है, जहाँ BTC स्वचालित रूप से Alice के पास वापस चली जाएगी। यह Monero के Atomic Swap कार्यान्वयन के लिए प्राथमिक गतिरोध था। Monero की [ Ring Signature गोपनीयता तकनीक ](/knowledge/ring-signatures) के कारण, लेन-देन भेजने वाला हमेशा अनिश्चित रहता है। Protocol धनवापसी लेन-देन कैसे कर सकता है, जब की उसे पता न हो कि लेन-देन कहाँ से आया है? 

२०१७ में, शोधकर्ताओं के एक छोटे समूह ने एक अलग विधि की रूपरेखा तैयार की जिसके द्वारा Monero में Atomic Swap काम करेगा। कई वर्षों के शोधन के बाद, शोधकर्ताओं ने एक प्रक्रिया को अंतिम रूप दिया, जिसके द्वारा Moenro refund transaction के बिना भी Bitcoin के साथ Atomic Swap करने में सक्षम होगा। 

तकनीकी जटिलता के इस स्तर की कई चीज़ों के साथ, हमारी व्याख्या विचार व्यक्त करने के लिए कुछ चीज़ों को अत्यधिक सरल कर देगी, लेकिन यह अभी भी तंत्र का एक ठोस विचार देगी जिसके द्वारा यह प्रक्रिया काम करेगी। 

Alice (जिसके पास XMR है और BTC चाहता है) और Bob (जिसके पास BTC है और XMR चाहता है) दोनों को Atomic Swap का समर्थन करने वाले program को downlaod करना और चलाना चाहिए। यह बटुए, विकेन्द्रीकृत बाज़ारों, या विशेष, विशिष्ट कार्यक्रमों में लागू किया जा सकता है, लेकिन software को Atomic Swap Protocol चलाना चाहिए। पहले चरण में, Alice और Bob के ग्राहक एक-दूसरे से जुड़ते हैं और कई साझा रहस्य और कुंजियाँ (shared secrets, keys) बनाते हैं। इस चरण में, एक नया Monero पता बनाया गया है, जिसमें Alice के पास आधी चाबी है, और Bob के पास दूसरी। हालांकि अभी तक कोई Monero नहीं आया है, इसलिए खर्च करने के लिए कुछ भी नहीं है। इस पते के बारे में ध्यान देने वाली एक आखिरी बात यह है कि उन दोनों के पास इस बटुए की दृश्य कुंजी है, इसलिए वे दोनों यह देखने के लिए अंदर झाँक सकते हैं कि Monero आता है या नहीं। 

दूसरे चरण में, Bob अपने BTC को एक विशेष पते पर भेजता है, Bitcoin Atomic Swap Protocol के समान जिसकी हम पहले ही चर्चा कर चुके हैं। जब Alice देखती है कि BTC blockchain पर इस पते पर पहुँच गया है, तो वह अपने Monero को Monero के पते पर भेजती है जिसकी उसके और Bob दोनों के पास आधी चाबी है। Bob यह सत्यापित कर सकता है कि Monero आ गया है क्योंकि उसके पास दृश्य कुंजी भी है, और एक बार जब वह Monero को बटुए में सुरक्षित रूप से देखता है, तो वह Alice को एक कुंजी का एक टुकड़ा भेजता है जो उसे Bitcoin वापस लेने की अनुमति देगा। अन्य protocol के समान, Bitcoin को लेने की प्रक्रिया से Bob को उसकी आधी Monero कुंजी का पता चलता है। अब Bob के पास दोनों हिस्से हैं, इसलिए वह Monero ले सकता है, जबकि Alice के पास केवल उसका आधा हिस्सा है, इसलिए वह उसे लेने से पहले इसे लेने की कोशिश नहीं कर सकती। 

तो अगर आपने यह सब देखा और अभी भी इस बारे में थोड़ा भ्रमित हैं कि Monero refund transaction की समस्या को कैसे दूर करने में सक्षम था, तो इसका उत्तर काफी सरल है। क्योंकि Monero के पास refund transaction नहीं है, इसलिए पाठक को ध्यान देना चाहिए कि Bitcoin (जिसमें refund transaction होता है) पहले भेजा जाता है, और blockchain पर होने के रूप में सत्यापित होने के बाद ही Monero भेजा जाता है। यह Monero को Bitcoin की refund transaction में script की क्षमता का उपयोग करने और इन क्षमताओं की आवश्यकता के बिना उनका लाभ उठाने की अनुमति देता है। 

Aomic Swap अब पूरा हो गया है, लेकिन यहाँ से, Bob के पास अपने नए लिए गए XMR के लिए कुछ विकल्प हैं। वह इस Monero बटुए का उपयोग कर सकता है, या XMR को दूसरे बटुए में ले जा सकता है जो पहले से ही उसका है। सबसे अधिक संभावना है कि Bob Monero को दूसरे बटुए में ले जाएगा, क्योंकि Alice के पास अभी भी देखने की कुंजी है और अंदर देख सकती है। 

इस protocol की सुंदरता यह है कि यह अभी भी काफी नया है, और अनुकूलन के लिए बहुत जगह है। यह अपने बनावट में भी काफी लचीला है, इसलिए अन्य बटुए या विकेंद्रीकृत बाज़ारों में कार्यान्वयन सरल होना चाहिए और उनके मौजूदा बनावट के साथ आसानी से चलना चाहिए। 

अग्रिम पठन

  * [कैसे Monero विशिष्ट रूप से परिपत्र अर्थव्यवस्थाओं को सक्षम बनाता है](/knowledge/monero-circular-economies/)

  * [Wasabi की तरह Monero के Ring Signature बनाम CoinJoin](/knowledge/ring-signatures-vs-coinjoin/)

  * [क्यों (और कैसे!) आपको अपनी चाबियां खुद रखनी चाहिए](/knowledge/hold-your-keys/)

  * [Monero में वापस योगदान करना](/knowledge/contributing-to-monero/)

  * [Remote nodes कैसे Monero की गोपनीयता को प्रभावित करते हैं](/knowledge/remote-nodes-privacy/)

  * [नेटवर्क को अपग्रेड करने के लिए Monero hard-forks का उपयोग कैसे करता है](/knowledge/network-upgrades/)

  * [view tags: कैसे एक byte Monero wallet sync के समय को ४०%+ तक कम कर देगा](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool और Monero खनन के विकेंद्रीकरण में इसकी भूमिका](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Monero के लिए यह क्या करेगा](/knowledge/seraphis-for-monero/)

  * [क्या Bitcoin को Monero में बदलना उतना ही निजी है जितना कि सीधे मोनेरो को खरीदना?](/knowledge/most-private-way-to-buy-monero/)

  * [Monero ZCash के विपरीत एक भरोसा न लगने वाले(Trustless) प्रणाली का उपयोग क्यों करता है](/knowledge/monero-trustless-setup/)

  * [Bitcoin की तुलना में Monero मूल्य का एक बेहतर भण्डार क्यों है](/knowledge/monero-better-store-of-value/)

  * [Monero Bitcoin के नेटवर्क प्रभाव(network effect) से कैसे जीत सकता है](/knowledge/network-effect/)

  * [Monero के पास सबसे गंभीर सोच वाला समुदाय क्यों है](/knowledge/critical-thinking/)

  * [Monero का उपयोग करते समय इन घोटालों से बचें](/knowledge/monero-scams/)

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