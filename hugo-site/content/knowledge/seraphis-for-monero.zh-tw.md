---
title: "Seraphis：它將為門羅幣做什麼"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis：Monero交易的模塊化設計升級

這篇文章描述 [Seraphis](https://github.com/UkoeHB/Seraphis), 一套交易協議結構和抽象,由化名的研究貢獻者 [`koe`](https://github.com/UkoeHB) 開發的為Monero生態系統, 並由化名開發者 [`coinstudent2048`](https://github.com/coinstudent2048)進行持續的安全分析。  
為了清楚起見，我們做了一些簡化，並省略了某些技術細節；為此，由於Seraphis的設計仍在進行中，感興趣的讀者應該參考Seraphis的文檔，以獲得最新的信息。

## Monero交易

像Bitcoin和Monero以及其他協議都依賴於所謂的"輸出模式" 的運作, 其中 _輸出_ 是可以轉移的價值的代表。  
交易消耗一個或多個由發送者控制的輸出，並產生針對接收者的新輸出（或作為零錢返回給發送者）；交易必須平衡，因為消耗的輸出必須包含與新輸出的價值完全相等的總價值（加上網絡施加的費用）。  
在許多像比特幣的協議中，輸出所包含的價值是寫在明處的，接受者也是如此。  
此外，通過查看區塊鏈，可以很容易地看到一項輸出是否和何時被花費了（也就是說，如果它在後來的交易中被消耗了，以及哪筆交易花費了它）。

相比之下，像Monero這樣的協議引入了一個不同的設計：

  * 輸出值是隱藏的，在區塊鏈上不可見
  * 收款人地址通過使用一次性地址協議而被隱藏起來
  * 使用模棱兩可的簽名掩蓋了一項輸出是否已經支出的問題

其結果是，在沒有外部信息的情況下，很難確定某項輸出是否已經使用，其價值是什麼，以及誰是其接受者。

目前的Monero交易協議被稱為 _RingCT_ , 並使用幾個加密構件來實現這些設計目標。

  * _義務_ 以一種數學上有用的方式隱藏金額
  * _範圍證明_ 防止溢出，可能使供應膨脹
  * _可鏈接的環形簽名_ 提供簽名人的模糊性，防止重複消費的企圖
  * _Commitment offsets_ 主張交易平衡

這些構件被小心地交織在一起，構建RingCT協議。

RingCT協議的一個有用的特性是，一些構件可以在保持整體設計和屬性不變的情況下被改變或升級，但可以提供效率或安全方面的改進。 事實上，這類升級在Monero的歷史上已經發生（或計劃發生）過幾次。 最初的RingCT協議中的範圍證明是笨重和緩慢的；後來被更新為一種構建稱為 [Bulletproofs](https://eprint.iacr.org/2017/1066) 使得交易更小、更快，並有更好的安全分析，併計劃更新為一種新的結構名為 [Bulletproofs+](https://eprint.iacr.org/2020/735) 以獲得更大的效率效益。 

對可鏈接的環形簽名構件也經歷了類似的過程。 在最初的協議中，使用了一種叫做 [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34) 的設計。 這後來被更新為一種較新的結構，稱為 [CLSAG](https://eprint.iacr.org/2019/654) 它的速度更快，交易量更小，並且有更好的安全分析。 一種基於 [Triptych](https://eprint.iacr.org/2020/018) 的更新的可鏈接的環形簽名結構被提出來，但由於它對多簽名操作的影響，沒有被選擇部署。 

## Seraphis

Seraphis 將這一想法向前推進了一步。  
它沒有更新現有RingCT交易協議的各個構件，而是引入了一個不同的協議，為了可以利用不同的構件並提供更好的功能。

## 構建模塊

Seraphis 使用一套不同的加密構件來實現其設計目標。

  * _義務_ 仍然隱藏金額
  * _範圍證明_ 仍然防止溢出和供應膨脹
  * _成員證明_ 提供簽名者的模糊性
  * _承諾抵銷_ 仍然主張平衡
  * _授權證明_ 防止重複消費的企圖

注意這裡的變化：可鏈接的環形簽名被替換成成員證明和授權證明的組合。 粗略地說，成員證明表明，一個被消耗的輸出是一個更大的集合的一部分，類似於RingCT中的情況。 但與RingCT不同的是，成員證明完全不涉及鏈接標籤！ 授權證明表明鏈接標籤是有效的，並用於簽署最終交易。

由於RingCT將鏈接標籤嵌入到模糊的簽名中，簽名（和多簽名）操作在計算上更加密集，而且建立其他與標籤相關的功能也變得更具挑戰性。 但在Seraphis，構建成員證明可以安全地從高度信任的設備（可能有有限的計算能力，如硬件錢包）委託給一個稍微少信任的設備，而且使用更簡單的授權證明，簽名（和多簽名）操作要容易得多。

幸運的是，Seraphis所需的一些構件已經存在於其他地方，不需要從頭設計。 Bulletproofs和Bulletproofs+結構都可以作為範圍證明。 對Schnorr型證明系統的修改可用於授權證明。 還有一個有效的 [證明系統](https://eprint.iacr.org/2015/643) 已經作為Triptych的基礎使用, [Lelantus](https://eprint.iacr.org/2019/373), 和 [Spark](https://eprint.iacr.org/2021/1173)* 可以為成員證明進行修改。 

* Cypher Stack獲得用於Spark開發的資金。 

## 尋址

不幸的是，目前使用的Monero地址與Seraphis不兼容。 如果Seraphis被實施，用戶將需要從他們的錢包密鑰中生成新的地址，以便接收Monero。 然而，這種生態系統的成本伴隨著一系列的好處。

除了上面討論的結構上的好處，Seraphis的設計適用於許多不同的地址建設的可能性，其中每一個都是有取捨的。 雖然在Seraphis中使用的最終地址結構 [仍在決定之中](https://github.com/monero-project/research-lab/issues/92) (有一個方案受到很多人的關注，叫做 [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), 我們可以描述一些常見和有用的功能。

你可能知道，Monero地址提供 _view key_ 功能，你可以向設備或第三方提供view key，並允許它代表你觀察傳入的輸出，但不放棄花費權限。 這對錢包來說很有用，它可以保持更新，同時將你的spend key安全地鎖起來。 它對於你想要外部視圖訪問的情況也很有用，比如提供透明度的公共慈善機構或有會計部門的公司。

Monero視圖鍵的缺點是，它們不提供完整或細粒度的視圖訪問。 不可能可靠地檢測一個錢包何時花費資金，這使得在spend key不可用時很難正確計算錢包餘額。 目前也不可能在不了解這些輸出所包含的價值的情況下檢測到傳入的輸出（這意味著任何負責尋找傳入輸出的第三方都會準確地了解你正在獲取多少Monero）。

Seraphis 的地址建設可以解決這個問題。 有了Seraphis，你的地址就會配備不同的鑰匙，可以做不同的事情：

  * 觀察傳入的輸出，但隱藏其價值
  * 觀察傳入的輸出，但顯示其價值
  * 觀察發出的輸出
  * 幫助你產生交易，但不簽署它們
  * 生成新的地址（對有許多客戶的零售商或交易所很有用）

作為地址持有人，你可以決定將多少權力下放給其他設備或第三方。 

## 大局觀

Seraphis是Monero生態系統的一個重大變化。 雖然它涉及到對地址和交易構件的修改，但它的設計提供了今天的RingCT協議所無法實現的靈活性和有用的功能。 雖然大部分的設計已經定稿，並正在發展成一個 [實施方案](https://github.com/UkoeHB/monero/tree/seraphis_lib), 地址設計和安全分析正在進行。 Seraphis提供了一個極好的機會來推動Monero生態系統的發展!

進一步閱讀

  * [門羅幣如何獨特地實現循環經濟](/knowledge/monero-circular-economies/)

  * [門羅幣環形簽名與CoinJoin像在Wasabi比較](/knowledge/ring-signatures-vs-coinjoin/)

  * [為什麼（以及如何！）你應該持有你自己的鑰匙](/knowledge/hold-your-keys/)

  * [貢獻為門羅幣](/knowledge/contributing-to-monero/)

  * [遠程節點如何影響門羅幣的隱私](/knowledge/remote-nodes-privacy/)

  * [門羅幣是如何使用硬分叉為升級網絡](/knowledge/network-upgrades/)

  * [查看標籤：一個字節如何將門羅幣錢包的同步時間減少40%以上](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool和它在去Monero採礦中心化的作用](/knowledge/p2pool-decentralizing-monero-mining/)

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