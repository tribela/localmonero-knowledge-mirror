---
title: "新的CLSAG環簽名技術將如何提高門羅幣的效率"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
關於門羅幣的協議層，目前仍處於持續創新的狀態. 門羅幣社區通過對鏈上和鏈下各種方案的研究，不斷探索可改進的領域，從而使門羅幣更加保護隱私，更具可擴展性，對普通用戶更友好和便於使用，門羅幣最新的創新之一是關於用CLSAG技術來替代MLSAG環簽名技術，CLSAG全稱是Concise Linkable Spontaneous Anonymous Group，它更簡潔的實現MLSAG技術方案.

從目前來看，CLSAG的實施將使最常見的門羅交易，也就是通常包含2個輸入和2個輸出的區塊體積減少25％.同時還將減少10％的驗證時間.

但是CLSAG到底是什麼？ 它有什麼作用？與舊版本的MLSAG有何不同？ 那麼讓我們先花點時間回顧一下，門羅幣為什麼和如何進行環簽名，以便幫助我們更好地理解這一概念. 在一個交易中，發送者需要用自己的私密金鑰進行簽名，目前門羅幣的一個輸出中，包含11個簽名，只有一個是發送者本身的，剩餘的簽名是從整個門羅幣歷史匿名集中抓取其它人的簽名，通過這樣可以實現非交互的，包括見證者都無法區分的真實輸入. 用外行的話來說，環簽名技術，只需要搭配區塊鏈本身，在預設情況下，不需要額外操作和其它任何人參與，自動利用自身輸出以及完全不相關的輸出，就可以隱藏交易發起人.節點和任何協力廠商也沒有辦法分辨. 這些輸出中的每一個簽名者都有可能是實際發送的輸出，從而隱藏了有關發送者的中繼資料.

但是，這就會讓人會產生一系列的疑問. 如果用戶要從所有的門羅幣歷史簽名裡構造一個假的環形簽名怎麼辦？ 發送者是匿名的，他到底有沒有足夠的許可權和足夠的資金？ 該用戶可以花假錢嗎？ 答案是肯定不可以.環形簽名包括一種方法，用於證明簽名中至少有一個輸出，是由一個真實的發送人擁有，而無需透露它是哪一個. 實際上，CLSAG和MLSAG都是證明這一點的一部分. 以下我們統稱它們為SAGs. 與此同時，它也能在匿名的情況下證明，隱藏在機密交易RingCT後面的交易金額仍能平衡，沒有人能雙花和憑空花費. 總的來說SAGs證明了兩件事，一個是輸出中11個簽名中其中有一個是真實的，歸屬於某人，同樣很重要的是，第二點，交易帳戶不會被超額花費，轉帳前後帳目平衡. 實際上這部分就是壓縮大小和節省驗證時間的地方. 如果聽到這裡，令人困惑，請放心，我們將為你帶來一個有趣且易於理解的比喻.

舊的簽名方案MLSAG，全稱是Multilayered Linkable Spontaneous Anonymous Group，在環簽名中證明了上述兩件事，但它們是分別進行的.對簽名和承諾金鑰使用單獨的計算意味著速度較慢. 雖然現代電腦可以在幾毫秒內完成這些計算，這看起來速度很快，對於一次交易和區塊掃描而言，也確實很快. 但是當我們考慮到門羅幣Monero區塊鏈上的大量交易，並且從頭開始同步的節點必須下載並驗證每個交易時，位元組大小和毫秒時間的微小差異最後會堆積如山.

CLSAG將證明兩者所需的數學結合在一起，並同時計算兩者，並且以一種安全的方式進行. 什麼是安全的方式計算呢？ 好吧，為澄清這一點，並希望使整個事情變得更好理解，讓我們來看一個關於驗證承諾的有趣比喻.

假設你需要同時前往雜貨店和五金店，購買兩種不同的東西，分別為食物和有毒的清潔劑. 你不希望它們混和在一起，如果不小心發生意外，化學物質會濺到食物上，使它們變得不可食用. 你決定安全第一，所以從家中先開車去雜貨店購買食物，然後回到家中. 接著卸下食物後，才又回到車裡，開車去五金店，然後帶著化學品回到家中. 你進行了兩次單獨的行動，來確保所有購物的安全. 儘管確實安全，但效率低下. 這很像MLSAG環形簽名，它其中存儲了兩組不同的數學運算，並分別進行了兩次不同的運算.

但是這種方式實在太慢了,並且太浪費時間了.當然偶爾做一次是沒有什麼問題，但是如果一遍又一遍的重複往復，時間開始累加起來就會很可怕. 你需要一種更快的方法. 是否可以試著這樣改變呢， 先從你的房子到雜貨店，再到五金店，再開車回家. 當然這樣你不能隨便把所有東西扔在車上. 這不安全，不過可以在汽車中設置不同的位置，並確保所有物品都整齊地放置在其位置上. 這樣一來，就可以安全地前往兩家商店，並且讓食物和化學品保持安全遠離. 這個新的變化就是CLSAG簽名. 現在，在一個交易中僅存儲了一組數學運算即可證明這兩件事，並且確保它們不會互相干擾.仍然需要運算，但是已經大大減少了運算時間，就像仍然需要開車去不同的商店，可路程大大減少.

所有這些進步聽起來很令人興奮. 那麼是否可以找到其它更快捷得方式或更節省時間和空間的方法進一步升級呢？ 答案是肯定的. 目前門羅MRL組研究人員表示，雖然當前可能無法進一步修改SAGs這一型結構以獲得更小的尺寸或速度. 但是，其他環簽名結構例如Arcturus，Omniring，RCT3或Triptych，它們使用了不同的數學方法，這樣會產生更小的資料大小和更快得驗證速度. 但是，每種下一代環形簽名技術協議的實現細節上都有其自身的取捨，門羅社區正在積極研究和調查各種方案的優缺點.

進一步閱讀

  * [門羅幣如何獨特地實現循環經濟](/knowledge/monero-circular-economies/)

  * [門羅幣環形簽名與CoinJoin像在Wasabi比較](/knowledge/ring-signatures-vs-coinjoin/)

  * [為什麼（以及如何！）你應該持有你自己的鑰匙](/knowledge/hold-your-keys/)

  * [貢獻為門羅幣](/knowledge/contributing-to-monero/)

  * [遠程節點如何影響門羅幣的隱私](/knowledge/remote-nodes-privacy/)

  * [門羅幣是如何使用硬分叉為升級網絡](/knowledge/network-upgrades/)

  * [查看標籤：一個字節如何將門羅幣錢包的同步時間減少40%以上](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool和它在去Monero採礦中心化的作用](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis：它將為門羅幣做什麼](/knowledge/seraphis-for-monero/)

  * [把比特幣兌換成門羅幣，就可以高枕無憂了嗎?](/knowledge/most-private-way-to-buy-monero/)

  * [為什麼門羅幣不像大零幣那樣需要初始信任來實現隱私](/knowledge/monero-trustless-setup/)

  * [為什麼門羅幣才是電子黃金，相對於比特幣更有儲存價值的屬性](/knowledge/monero-better-store-of-value/)

  * [門羅幣是如何蠶食比特幣的份額和先發優勢](/knowledge/network-effect/)

  * [為什麼說門羅幣社區最具批判性精神](/knowledge/critical-thinking/)

  * [門羅幣防詐騙指南](/knowledge/monero-scams/)

  * [原子互換技術將如何在門羅幣上實現](/knowledge/monero-atomic-swaps/)

  * [門羅幣與當代互聯網，隱私達人的須知](/knowledge/monero-networking/)

  * [ RingCT環形機密技術是如何隱藏門羅幣交易的金額](/knowledge/monero-ringct/)

  * [門羅幣隱身地址如何保護你的身份](/knowledge/monero-stealth-addresses/)

  * [門羅幣子位址是如何防止使用者資訊被關聯](/knowledge/monero-subaddresses/)

  * [加密貨幣裡面的output，中文譯作輸出，這個概念到底什麼意思,又為什麼門羅幣轉帳後餘額顯示錯誤要等待二十分鐘](/knowledge/monero-outputs/)

  * [門羅幣最佳入門指南](/knowledge/monero-best-practices/)

  * [環形簽名如何保護門羅幣發送者的輸出](/knowledge/ring-signatures/)

  * [門羅幣是如何解決困擾比特幣的區塊大小的擴容問題](/knowledge/dynamic-block-size/)

  * [為什麼門羅幣擁有尾部增發的特性](/knowledge/monero-tail-emission/)

  * [門羅幣的前世今生](/knowledge/monero-history/)

  * [Wired雜誌是如何誤解了門羅](/knowledge/wired-article-debunked/)

  * [流言終結者：關於門羅幣的15大傳言和疑慮](/knowledge/monero-myths-debunked/)

  * [Dandelion ++蒲公英改進協議如何使Monero從源頭得到更強防護](/knowledge/monero-dandelion/)

  * [為什麼門羅幣是開源且去中心化的](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [門羅幣挖礦: 什麼使 RandomX 算法如此特別](/knowledge/monero-mining-randomx/)

  * [為什麼門羅幣優於達世幣, 大零幣, 小零幣 , 古靈幣以及經過Wasabi級別混幣器混淆後的比特幣 (更新於2020年五月)](/knowledge/why-monero-is-better/)