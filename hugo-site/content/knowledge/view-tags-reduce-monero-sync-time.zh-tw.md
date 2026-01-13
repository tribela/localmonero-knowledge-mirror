---
title: "查看標籤：一個字節如何將門羅幣錢包的同步時間減少40%以上"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
圍繞日常使用門羅幣最常見的抱怨之一是在能夠發送門羅幣之前同步錢包的時間。幸運的是，門羅幣社區的開發者和研究人員已經找到了一個絕妙的方法，可以將你同步錢包的時間減少40%以上，而且沒有任何額外的區塊鏈臃腫、費用等。

“查看標籤 （View tags）”，這是每個交易數據中的一個字節的補充--出在下一個門羅幣網絡升級！

## 為什麼門羅幣的錢包同步速度比比特幣的慢？

為了更好地理解查看標籤這樣的解決方案的需求，我們首先要回答的一個問題是，為什麼門羅幣的錢包同步速度比比特幣等加密貨幣慢。

在比特幣中，由於所有的交易都不是私密的，會在鏈上顯示被花費的硬幣、金額和涉及的地址，比特幣錢包可以簡單地尋找任何未花費的交易輸出（UTXO）或特定錢包的使用地址，快速掃描區塊鏈，只尋找這些地址所擁有的UTXO，以找出哪些硬幣屬於你的錢包並可以被花費。

然而，在門羅幣中，所有交易都通過隱藏發送人、收款人和每筆交易涉及的金額來保護用戶的隱私。這種隱私，雖然對保護網絡用戶至關重要，但也帶來了較慢的錢包同步。在門羅幣中，你的錢包必須將網絡上存在的每一筆交易輸出（TXO）與你錢包的私鑰進行比較。

這種比較涉及到很多複雜的數學和密碼學，以驗證一個輸出是真正屬於你的，因為所有的金額、地址和已知花費的輸出（或幣）都隱藏在門羅幣的鏈上。

## 查看標籤是什麼？

為了幫助減少門羅幣錢包的同步時間， [一位名叫UkoeHB的研究人員想出了一個新的方法](https://github.com/monero-project/research-lab/issues/73) – 在每筆交易中添加一個1字節的 “標籤”，使用只有該交易的發送方和接收方知道的共享秘密。

這個共享秘密是由發送方使用接收方提供給他的地址生成的，不需要發送方和接收方的任何主動合作。這個共享秘密的第一個字節（或字符）然後在發佈到門羅幣網絡時被添加到交易的數據中。

當該交易的參與者之一想在之後將他們的錢包與門羅幣區塊鏈同步時，而不是需要對網絡上的每一個交易輸出執行所有復雜的數學和密碼學，錢包現在可以只檢查每筆交易中的那個1字節字段，然後只對有這個標籤的交易執行耗時的驗證--準確地說，是網絡上1/256個交易輸出！

這個標籤不會向外界透露任何關於交易的信息，只增加1個字節（可以忽略不計）的交易大小，但通過減少必要的複雜驗證，我們可以將同步時間減少40%以上！

## 查看標籤：一個簡化的例子

想像一下，你在一個房間裡有4,096個盒子，其中只有5個盒子是屬於你的。這些盒子從外面看完全沒有區別，要想知道一個盒子是否屬於你，唯一的辦法就是打開它，解決裡面寫的一道耗時的數學題，以確保它是你的。

現在，想像一下，你決定讓寄給你這5個盒子的人用你的地址生成一個特殊的代碼，然後在寄給你的每個盒子的外面只寫上該代碼的第一個字符。其他人對他們的盒子也做了同樣的事情（以確保所有的盒子仍然是不可區分的），但現在你可以簡單地看一下盒子外面的一個字符代碼，並只打開那些有這個字符的盒子。

雖然其他盒子會與你的代碼相匹配，甚至是一些不屬於你的盒子，但你需要打開並解決一個數學問題的盒子數量現在只有16個（1/256個盒子！），而不是全部的4096個盒子。

現在你打開這16個盒子，解決數學問題，並保留那組中真正屬於你的5個盒子!

## 查看標籤何時能在門羅幣中使用？

查看標籤是目前計劃納入 [即將到來的網絡升級](https://github.com/monero-project/meta/issues/630), 的功能之一，應該在今年春天的某個時候發布。 社區 [籌集了23.3 XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) （在撰寫本文時）來激勵查看標籤的開發和實施，因此，絕大部分將查看標籤納入門羅幣代碼庫的工作已經由j-berman與審核員和研究人員合作完成。

一旦查看標籤被網絡強制執行，所有在網絡升級後發送的交易都將受益於大幅改善的錢包同步時間。你不需要做任何特別的事情來開始使用查看標籤，你最喜歡的門羅幣錢包將在網絡升級後自動開始使用它們!

## 我如何能了解更多？

如果這已經激起了你對查看標籤的好奇心，請看下面一些深入研究該主題的外鏈接：

  * [用每輸出一個字節的 ‘查看標籤’減少掃描時間](https://github.com/monero-project/research-lab/issues/73)
  * [為輸出添加查看標籤以減少錢包掃描時間](https://github.com/monero-project/monero/pull/8061)

進一步閱讀

  * [門羅幣如何獨特地實現循環經濟](/knowledge/monero-circular-economies/)

  * [門羅幣環形簽名與CoinJoin像在Wasabi比較](/knowledge/ring-signatures-vs-coinjoin/)

  * [為什麼（以及如何！）你應該持有你自己的鑰匙](/knowledge/hold-your-keys/)

  * [貢獻為門羅幣](/knowledge/contributing-to-monero/)

  * [遠程節點如何影響門羅幣的隱私](/knowledge/remote-nodes-privacy/)

  * [門羅幣是如何使用硬分叉為升級網絡](/knowledge/network-upgrades/)

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

  * [ 新的CLSAG環簽名技術將如何提高門羅幣的效率](/knowledge/what-is-clsag/)

  * [為什麼門羅幣擁有尾部增發的特性](/knowledge/monero-tail-emission/)

  * [門羅幣的前世今生](/knowledge/monero-history/)

  * [Wired雜誌是如何誤解了門羅](/knowledge/wired-article-debunked/)

  * [流言終結者：關於門羅幣的15大傳言和疑慮](/knowledge/monero-myths-debunked/)

  * [Dandelion ++蒲公英改進協議如何使Monero從源頭得到更強防護](/knowledge/monero-dandelion/)

  * [為什麼門羅幣是開源且去中心化的](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [門羅幣挖礦: 什麼使 RandomX 算法如此特別](/knowledge/monero-mining-randomx/)

  * [為什麼門羅幣優於達世幣, 大零幣, 小零幣 , 古靈幣以及經過Wasabi級別混幣器混淆後的比特幣 (更新於2020年五月)](/knowledge/why-monero-is-better/)