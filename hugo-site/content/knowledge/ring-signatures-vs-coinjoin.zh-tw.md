---
title: "門羅幣環形簽名與CoinJoin像在Wasabi比較"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
隨著比特幣的隱私工具獲得更多的關注和使用，他們受到了更多的監管審查。這種審查導致比特幣隱私工具Wasabi Wallet [最近宣布](https://twitter.com/wasabiwallet/status/1503091503207432193) ，他們將開始審查和拒絕輸入他們認為非法或違反其服務條款的混合，並將支付區塊鏈分析公司來 "審查"輸入的混合參與者。

使用CoinJoin交易來混淆比特幣的資金來源，多年來一直是比特幣隱私的核心，它的使用所固有的問題和風險是門羅幣的環形簽名所糾正和預防的一些核心問題。

在這篇博文中，我們將簡要介紹CoinJoin和環形簽名的比較，以及為什麼門羅幣採取的方法會導致更大的審查阻力，更大的隱私，以及對用戶更少的麻煩。

## CoinJoin交易是什麼？

## CoinJoin交易是什麼？

由於所有的交易在比特幣中是完全透明的——揭示了發送者、接收者和金額——用戶必須採取額外的措施來保護他們的隱私，不被以前的發送者和未來的接收者發現，或者冒著被審查、監視或通過身體暴力盜竊資金的風險。

目前，比特幣隱私的最佳解決方案是一種叫做 [“CoinJoin”](https://bitcoiner.guide/qna/coinjoin/), 的工具，2個或更多的用戶一起工作（通常通過一個集中的協調人），創建一個特殊的交易，使外部觀察者難以將輸入和輸出聯繫起來。每個參與者在不交出資金保管權的情況下進行溝通，共同建立交易，並在最後收到一個輸出，而這個輸出的歷史對外部觀察者來說現在是不清楚的（或被混淆的）。

這打破了特定的UTXO（未花費的交易輸出）的歷史，允許比特幣用戶在交易時獲得一定程度的前向保密性。然而，CoinJoin（如Wasabi Wallet和Samourai Wallet所實現的，這是兩個最常用的比特幣CoinJoin工具）有幾個主要缺點：

  * 由於CoinJoin交易是完全選擇的，需要積極參與，任何參與者必然表明他們比 "正常"比特幣用戶尋求更大的隱私，有可能將他們挑出來，導致在許多受監管的交易所或實體花費資金的問題。每個用戶都不能否認他們參與了CoinJoin交易。
  * 為了找到其他的CoinJoin用戶，大多數CoinJoin的方法（包括Wasabi Wallet）使用一個集中的協調者，連接參與者，幫助他們溝通並建立一個適當的CoinJoin交易。這個中心化的協調人從來沒有保管用戶的資金，但確實對他們協調的交易有廣泛的了解，可以審查進入的輸入（如Wasabi Wallet的情況），並可以在壓力下收集或分享有關CoinJoin參與者的信息。
  * 擁有大量資金的用戶往往需要等待數小時（甚至數天！）才能找到足夠的參與者進行CoinJoin，導致用戶從收到資金到可以私下消費的時間有很大延遲。
  * CoinJoin交易提供的隱私隨著時間的推移而降低，因為其他參與者花費資金或通過KYC交易所、需要實名認證的商家等將他們的產出與他們的身份聯繫起來。這意味著用戶最好保持他們的資金在CoinJoin交易中不斷流動，以保持他們的匿名集（"隱藏的人群"）盡可能的新鮮。 
  * 在大多數CoinJoin的方法中，參與者必須使用一個固定大小的UTXO（即0.1 BTC），以使CoinJoin交易的輸入和輸出更難連接。這導致更高的費用（每筆大額輸入需要更多的獨立交易），更多的 "有毒零錢"（在不嚴重危害隱私的情況下無法花費的資金），並且如果小型用戶沒有所需的最低餘額，他們可能根本無法進行混合。 

## 環形簽名如何解決這些問題？

## 環形簽名如何解決這些問題？

由於 [我們在過去已經深入研究了什麼是環形簽名](/knowledge/ring-signatures), 我不會在這篇博文中詳細討論它們如何工作的技術問題。相反，我們將看看門羅幣中採取的方法如何解決上面討論的CoinJoin的問題。

> CoinJoin是選擇加入的，需要參與

CoinJoin是選擇加入的，需要參與

門羅幣的環形簽名是隱私協議的一個核心特徵，網絡上的 _每一筆_ 交易都使用它們。這意味著沒有用戶的交易會因為尋求比 “正常” 門羅幣用戶更多的隱私而脫穎而出，而且所有用戶都獲得了他們在任何特定交易中花費資金的合理推諉性。由於花費資金的用戶不會與交易中的誘餌投入相協調或參與，那些擁有碰巧被選為誘餌的投入的用戶可以誠實地說他們沒有參與該交易，加強他們的隱私。

> 使用一個集中的協調器

使用一個集中的協調器

由於門羅幣的環形簽名是完全非協調的，只需要真正的資金花費者來創建交易，所以在門羅幣中不需要一個集中的協調者。這確保了 _沒有人_ 可以拒絕你在門羅幣中獲得隱私，也沒有一個中心化的實體可以施壓，不容易對流動性進行Sybil攻擊，等等。只要你的交易支付適當的費用，你就可以在門羅幣中獲得不可審查的隱私、安全和匿名的機會。

> CoinJoin需要流動性

CoinJoin需要流動性

任何花費門羅幣的人可以用作誘餌的 "流動性"總是鏈上的總輸出，所以永遠不會缺少可以用門羅幣隱藏的誘餌。尋求花費門羅幣的人可以在收到資金後~20分鐘內完成，並且不需要執行任何額外的步驟來獲得門羅幣的強大隱私。

> CoinJoin的隱私會隨著時間的推移而降低

CoinJoin的隱私會隨著時間的推移而降低

由於門羅幣的輸出永遠不會被網絡所知曉，環形簽名所提供的隱私更不容易隨時間退化。一個用戶不需要不斷地在門羅幣中攪動輸出，並且在極其罕見的情況下，隨著時間的推移不會失去隱私。 

然而，如果用戶確實想 "刷新"用於輸出的誘餌，他們只需將資金送回給自己，並能夠像往常一樣在20分鐘後花費它們。 

> CoinJoin通常需要固定規模的輸入

CoinJoin通常需要固定規模的輸入

由於使用 [“機密交易”](/knowledge/monero-ringct) ("RingCT"的一部分), 的每筆交易的金額都是隱藏的，在任何特定交易中使用的誘餌可以是任何大小。在門羅幣中沒有理由需要擔心基於金額的啟發式方法，因此交易的建立要簡單得多，可以利用來自門羅幣區塊鏈上任何時間點和任何金額的誘餌。 

## 我怎樣能了解更多？

## 我怎樣能了解更多？

如果你很好奇，想更好地了解環形簽名或CoinJoin交易，請看下面的鏈接，以了解入門的好地方：

  * [環形簽名如何掩蓋門羅幣的輸出](/knowledge/ring-signatures)
  * [環形簽名 - Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin 問答](https://bitcoiner.guide/qna/coinjoin/)
  * [CoinJoin 概述](https://6102bitcoin.com/coinjoin-overview/)

進一步閱讀

  * [門羅幣如何獨特地實現循環經濟](/knowledge/monero-circular-economies)/

  * [為什麼（以及如何！）你應該持有你自己的鑰匙](/knowledge/hold-your-keys)/

  * [貢獻為門羅幣](/knowledge/contributing-to-monero)/

  * [遠程節點如何影響門羅幣的隱私](/knowledge/remote-nodes-privacy)/

  * [門羅幣是如何使用硬分叉為升級網絡](/knowledge/network-upgrades)/

  * [查看標籤：一個字節如何將門羅幣錢包的同步時間減少40%以上](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool和它在去Monero採礦中心化的作用](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis：它將為門羅幣做什麼](/knowledge/seraphis-for-monero)/

  * [把比特幣兌換成門羅幣，就可以高枕無憂了嗎?](/knowledge/most-private-way-to-buy-monero)/

  * [為什麼門羅幣不像大零幣那樣需要初始信任來實現隱私](/knowledge/monero-trustless-setup)/

  * [為什麼門羅幣才是電子黃金，相對於比特幣更有儲存價值的屬性](/knowledge/monero-better-store-of-value)/

  * [門羅幣是如何蠶食比特幣的份額和先發優勢](/knowledge/network-effect)/

  * [為什麼說門羅幣社區最具批判性精神](/knowledge/critical-thinking)/

  * [門羅幣防詐騙指南](/knowledge/monero-scams)/

  * [原子互換技術將如何在門羅幣上實現](/knowledge/monero-atomic-swaps)/

  * [門羅幣與當代互聯網，隱私達人的須知](/knowledge/monero-networking)/

  * [ RingCT環形機密技術是如何隱藏門羅幣交易的金額](/knowledge/monero-ringct)/

  * [門羅幣隱身地址如何保護你的身份](/knowledge/monero-stealth-addresses)/

  * [門羅幣子位址是如何防止使用者資訊被關聯](/knowledge/monero-subaddresses)/

  * [加密貨幣裡面的output，中文譯作輸出，這個概念到底什麼意思,又為什麼門羅幣轉帳後餘額顯示錯誤要等待二十分鐘](/knowledge/monero-outputs)/

  * [門羅幣最佳入門指南](/knowledge/monero-best-practices)/

  * [環形簽名如何保護門羅幣發送者的輸出](/knowledge/ring-signatures)/

  * [門羅幣是如何解決困擾比特幣的區塊大小的擴容問題](/knowledge/dynamic-block-size)/

  * [ 新的CLSAG環簽名技術將如何提高門羅幣的效率](/knowledge/what-is-clsag)/

  * [為什麼門羅幣擁有尾部增發的特性](/knowledge/monero-tail-emission)/

  * [門羅幣的前世今生](/knowledge/monero-history)/

  * [Wired雜誌是如何誤解了門羅](/knowledge/wired-article-debunked)/

  * [流言終結者：關於門羅幣的15大傳言和疑慮](/knowledge/monero-myths-debunked)/

  * [Dandelion ++蒲公英改進協議如何使Monero從源頭得到更強防護](/knowledge/monero-dandelion)/

  * [為什麼門羅幣是開源且去中心化的](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [門羅幣挖礦: 什麼使 RandomX 算法如此特別](/knowledge/monero-mining-randomx)/

  * [為什麼門羅幣優於達世幣, 大零幣, 小零幣 , 古靈幣以及經過Wasabi級別混幣器混淆後的比特幣 (更新於2020年五月)](/knowledge/why-monero-is-better)/

進一步閱讀