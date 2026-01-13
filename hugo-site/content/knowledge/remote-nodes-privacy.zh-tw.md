---
title: "遠程節點如何影響門羅幣的隱私"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
與其他加密貨幣相比，門羅幣最大的優勢之一是它的鏈上隱私，但你有沒有想過，當你使用遠程節點時，門羅幣的隱私是如何保持的？如果你使用像MyMonero "輕型錢包"服務器呢？

在這篇文章中，我們將深入探討門羅幣在使用遠程節點時如何提供卓越的鏈上隱私的一些細節，以及在使用遠程節點時需要注意的問題。

## 節點在門羅幣中具有什麼功能？

對於那些不太熟悉門羅幣工作方式的人來說，門羅幣網絡中的節點（或服務器）可以由任何人運行，並允許節點的所有者或他們選擇與之共享的其他人來同步區塊鏈的一個副本，並將該副本提供給網絡上的其他人。這些節點還驗證網絡上發生的所有交易，以及所有發布的區塊，並確保它們都遵循共識所設定的規則。

節點在門羅幣中的另一個功能是提供你最喜歡的門羅幣錢包所需的所有數據，以正確檢查屬於你的交易並進行新的交易。這些數據是由節點以兩種方式提供的：

  * 區塊鏈上每個區塊的數據被錢包要求，掃描屬於你的交易，然後在錢包檢查後被丟棄。 
    * 由於 [查看標籤](/knowledge/view-tags-reduce-monero-sync-time)的存在，這一步驟很快就會得到大幅改善。
  * 當發送交易時，你使用的節點提供一個可能的誘餌（或假輸入）的列表，以在建立交易時使用，確保你每次花費門羅幣時都有一個好的人群可以隱藏。 
    * 這些誘餌是 [環形簽名](/knowledge/ring-signatures)的一部分，是門羅幣對鏈上隱私的一個重要部分。

## 使用門羅幣最私密和安全的方式是什麼？

即使在使用遠程節點時，門羅幣提供的強大的鏈上隱私，最好的辦法是運行你自己的門羅幣節點，以確保你有一個原始的門羅幣區塊鏈副本在手，並且你的IP地址得到很好的保護。運行自己的節點的另一個好處是，你可以回饋網絡，讓其他節點從你的節點同步，甚至讓其他用戶用他們的錢包連接到你的節點。

也就是說，在使用遠程節點時，門羅幣確實仍然提供很好的隱私。如果你對運行你自己的門羅幣節點感興趣，這裡有一個易於遵循的指南：

  * [運行門羅幣節點](https://sethforprivacy.com/guides/run-a-monero-node/)

## 遠程節點可以了解什麼情況？

當使用遠程節點時，有幾個關鍵的信息會暴露給遠程節點，以及該節點可以攻擊你、阻止你進行交易等幾個關鍵方式。

遠程節點可以了解到的第一件事是你的公共IP地址。雖然這將有望通過VPN或Tor隱藏起來，但遠程節點可以將你的公共IP地址與交易聯繫起來，幫助他們縮小你的交易地點。遠程節點還可以了解你的錢包最後同步的區塊，並利用這一點試圖對你進行有根據的猜測，比如你通常什麼時候使用門羅幣，以及你最後一次花費門羅幣是什麼時候。如果你總是從同一個IP地址（如你的家）來，這一點尤其正確。遠程節點可以了解到的關於你的最後一件關鍵事情是關於你通過它發送的交易的基本信息。雖然這可能是遠程節點操作員獲得的關於你的最明顯的數據，但重要的是要明白，當把這些信息與其他鏈外數據結合起來時，這可能被用來幫助追踪交易的發件人。如果遠程節點由惡意實體、區塊鏈分析公司或壓迫性國家運行，這可能特別危險。

一個遠程節點也可以試圖通過向你隱藏區塊來給你帶來麻煩，使你的錢包認為它是同步的，但實際上它並不是。這可以使你認為資金丟失或阻止你花費資金，直到你連接到另一個節點。一個遠程節點可能做的最後一件事是給你的錢包提供一個被操縱的誘餌列表。這可能導致你的錢包完全無法建立交易（使你無法花費資金），或者允許遠程節點嘗試提供它知道已經花費的誘餌，以減少你在每筆交易中獲得的匿名性。

## 在使用遠程節點時，仍然存在哪些隱私保障？

雖然這篇文章可能讓你有點害怕，但重要的是要意識到，即使使用遠程節點，門羅幣提供的隱私也是非常好的，以這種方式使用時，遠遠超過任何其他加密貨幣。你仍然獲得了門羅幣提供的強大的鏈上隱私，因為遠程節點永遠不知道真正的輸入（你花了什麼幣），交易中花費的門羅幣數量，或交易接收者的地址。外部觀察者也無法看到真正的輸入、金額或涉及的地址（無論你選擇使用哪種類型的節點！），確保在遠程節點之外，甚至你的IP地址、錢包同步信息和交易都有強大的隱私保證。

遠程節點也永遠無法獲得你之前發送或接收的交易，或者你錢包中當前的門羅幣數量，並且在你開始使用另一個節點的時候，會失去對你交易的所有可見性。沒有任何私人密鑰（無論是花費還是查看密鑰）被提供給遠程節點，因此你的錢包仍然是私人的，安全的，可用的。不管是哪個遠程節點，你也永遠不會有丟失門羅幣或被盜的風險，因為該節點不能編輯收件人地址，永遠無法訪問你的錢包私鑰，也不能以任何方式沒收你的門羅幣。

## 像MyMonero類型 "輕型錢包"如何？

雖然這個話題有點超出本文的範圍，但我確實想談談門羅幣中一種獨特的錢包類型——輕型錢包。輕型錢包的名字來自於這樣一個事實：你的錢包（在你的手機或電腦上）不必執行任何區塊鏈同步，使體驗更快、更流暢。

然而，像這樣的錢包目前有一個嚴重的隱私權衡 —— 你的錢包將私人查看密鑰發送到你使用的遠程服務器（如MyMonero中的默認），讓遠程服務器完全看到自你的錢包創建以來收到的任何資金（以及直到你停止使用該錢包或種子）。這確實大大減少你從節點操作員那裡得到的隱私，應該謹慎對待。

值得慶幸的是，門羅幣社區正在努力改進軟件，你可以用它來託管你自己的輕型錢包服務器（LWS），這將允許你有快速的同步，而無需信任第三方與你的私人查看密鑰 —— 因為你將運行你的錢包發送私人查看密鑰的軟件！

關於定制的輕型錢包服務器的更多信息，請看下面的Github倉庫：

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## 我如何能了解更多？

如果你很好奇，想更好地了解門羅幣的節點，並研究使用遠程節點或運行自己的節點，請看下面的鏈接，以了解開始的好地方：

  * [MoneroWorld，一個可以使用的社區運行的遠程節點列表](https://moneroworld.com/#nodes)
  * [本文作者Seth For Privacy所運行的門羅幣節點](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail，一個經常檢查狀態的遠程節點列表](https://monero.fail/)
  * [如何在GUI錢包內連接到一個遠程節點](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia —— 遠程節點](https://www.getmonero.org/resources/moneropedia/remote-node.html)

進一步閱讀

  * [門羅幣如何獨特地實現循環經濟](/knowledge/monero-circular-economies/)

  * [門羅幣環形簽名與CoinJoin像在Wasabi比較](/knowledge/ring-signatures-vs-coinjoin/)

  * [為什麼（以及如何！）你應該持有你自己的鑰匙](/knowledge/hold-your-keys/)

  * [貢獻為門羅幣](/knowledge/contributing-to-monero/)

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

  * [ 新的CLSAG環簽名技術將如何提高門羅幣的效率](/knowledge/what-is-clsag/)

  * [為什麼門羅幣擁有尾部增發的特性](/knowledge/monero-tail-emission/)

  * [門羅幣的前世今生](/knowledge/monero-history/)

  * [Wired雜誌是如何誤解了門羅](/knowledge/wired-article-debunked/)

  * [流言終結者：關於門羅幣的15大傳言和疑慮](/knowledge/monero-myths-debunked/)

  * [Dandelion ++蒲公英改進協議如何使Monero從源頭得到更強防護](/knowledge/monero-dandelion/)

  * [為什麼門羅幣是開源且去中心化的](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [門羅幣挖礦: 什麼使 RandomX 算法如此特別](/knowledge/monero-mining-randomx/)

  * [為什麼門羅幣優於達世幣, 大零幣, 小零幣 , 古靈幣以及經過Wasabi級別混幣器混淆後的比特幣 (更新於2020年五月)](/knowledge/why-monero-is-better/)