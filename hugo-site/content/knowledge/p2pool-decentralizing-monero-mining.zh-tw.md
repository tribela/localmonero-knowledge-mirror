---
title: "P2Pool和它在去Monero採礦中心化的作用"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero項目的核心目標之一是通過對工作證明的新的和創新的方法來實現一個公平、分散和安全的網絡，這是當今加密貨幣網絡的主要安全方式。

雖然 [像RandomX](/knowledge/monero-mining-randomx) 這樣獨特的挖礦算法對這一目標極為重要，因為它有助於確保任何擁有計算機的人都能為網絡的安全做出合理的貢獻，但RandomX並不能解決由於礦池可能出現的問題。 礦池是目前最常見的加密貨幣挖礦方式，包括Monero，但值得慶幸的是，p2pool挖礦的出現正在迅速改變這種狀況。

## 什麼是礦池採礦？

## 什麼是礦池採礦？

礦池是礦工分擔試圖解決網絡上的區塊的任務，然後平均分享池子裡找到的所有區塊的獎勵的一種方式。 雖然這極大地有助於平衡礦工獲得報酬的頻率與單獨開採Monero的頻率，但也不是沒有嚴重的中心化問題。

當每個礦工向礦池貢獻工作時，他們放棄了對他們所做的任何工作和發現的區塊的控制權，相信礦池會根據每個人所做的工作的數量，在所有礦工之間誠實和公平地分享獎勵。 如果一切順利，礦池運營商會收集所有礦工的工作，提交給網絡，並平均分享獎勵。

## 礦池採礦的問題是什麼？

## 礦池採礦的問題是什麼？

不幸的是，這完全依賴於信任，並允許礦池運營商對礦工所做的工作做一些不正當的事情。礦池運營商可以利用正在進行的工作來攻擊網絡，試圖重複花費資金（如果礦池足夠大的話），或者乾脆利用礦工正在進行的工作來支付自己，而從不適當獎勵礦工的工作。

對網絡來說，最大的風險是一個池（或多個池在一起）在其控制下擁有超過51%的網絡算力，因為他們可以利用這一點作弊並花費兩次資金（雙重消費攻擊）或試圖改變網絡的規則。

## p2pool 是什麼?

## p2pool 是什麼?

p2pool是一個概念，最初是在2011年為開採比特幣而創建的，但從來沒有看到廣泛的採用，在比特幣上幾乎沒有使用。值得慶幸的是，RandomX背後的關鍵開發人員之一，SChernykh，用他的假期想出了解決比特幣實現p2pool的一些問題，並從頭開始重寫了所有的軟件。

Monero中的p2pool允許礦工以完全無信任的方式合作解決區塊，並通過使用p2pool的特殊節點軟件來確保Monero網絡的安全，以便分享工作。

這是通過一個新的區塊鏈 (a "side-chain") 來完成的，它記錄了每個礦工所做的工作，他們的錢包地址，以及他們賺了多少Monero，然後以一種無信任和去中心化的方式支付獎勵。由於這個側鏈的礦工人數少得多，在它上面尋找和提交區塊要比在Monero主網絡上容易得多，這使得礦工比單獨挖Monero更容易獲得穩定的報酬。

## p2pool是如何解決礦池採礦的問題？

## p2pool是如何解決礦池採礦的問題？

在p2pool中，沒有中心化的礦池，沒有中心化的礦池運營商，也沒有一個人掌握著資金和分配報酬。所有通過p2pool挖礦的人集體進行的工作都由p2pool區塊鍊和其他節點運營商檢查，以確保其合法性，當發現一個區塊時，所有礦工都會根據他們所做的工作直接從該發現的區塊中的獎勵中獲得報酬。

當礦工選擇使用p2pool而不是集中式礦池時，他們從礦池運營商那裡移走了所有的權力和信任，並確保他們的工作有助於網絡的利益和他們自己的獎勵，減少網絡攻擊、濫用他們的工作或盜竊他們應得的獎勵的風險。

這不僅有助於他們保護自己的利益，也減少了集中式資金池對整個Monero網絡構成的風險。p2pool的使用也大大有助於減少民族國家或監管機構可能對網絡健康構成的風險，因為沒有集中式資金池運營商可以施壓，沒有資金池的地理集中可以依靠，也沒有任何其他容易讓他們用來對付Monero的壓力點。

## 有什麼弊端？

## 有什麼弊端？

值得慶幸的是，Monero中的p2pool已經被設計得很好，而且功能非常棒! 然而，p2pool挖礦的主要缺點是，每個想使用p2pool的礦工都要運行自己的Monero節點，導致開始的過程比較麻煩。不過，這個節點隨後被用來計算構建和檢查區塊所需的所有信息，並確保礦工完全控制他們正在進行的工作。該節點還可以作為礦工自己錢包的遠程節點，為網絡做出貢獻，以及更多利益。

與集中式挖礦的另一個關鍵區別是，使用p2pool的小礦工將比大型集中式礦池有更多的 "差異", 或兩次支付之間的時間間隔， 但 _極其_ 重要的是，這不會導致長期賺取更少的Monero！p2pool甚至會像集中式礦池一樣長期為小礦工提供利潤。這種差異的一部分也被p2pool本身的0%費用所抵消，因為沒有集中式礦池運營商需要為他們的服務支付費用!

## 我怎樣能開始呢？

## 我怎樣能開始呢？

值得慶幸的是，由於Monero的p2pool實現的出色設計，以及社區中許多人投入時間幫助簡化通過p2pool挖礦的過程，隨著時間的推移，開始變得越來越簡單。有幾種方法可以開始使用p2pool挖礦，但由於技術細節超出本文的範圍，請根據您的操作系統，隨時跳轉到下面的鏈接：

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## 我怎樣能了解更多？

## 我怎樣能了解更多？

如果這已經激起了你對p2pool挖礦的好奇心，請看下面一些關於p2pool的額外鏈接和解釋，它是如何工作的，以及它對Monero意味著什麼：

  * [The official Github for p2pool](https://github.com/SChernykh/p2pool)
  * [The official docs on using p2pool](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool is now live](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, a "block explorer" of sorts for p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh: On his development of P2Pool a Decentralized XMR Mining Pool](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

進一步閱讀

  * [門羅幣如何獨特地實現循環經濟](/knowledge/monero-circular-economies)/

  * [門羅幣環形簽名與CoinJoin像在Wasabi比較](/knowledge/ring-signatures-vs-coinjoin)/

  * [為什麼（以及如何！）你應該持有你自己的鑰匙](/knowledge/hold-your-keys)/

  * [貢獻為門羅幣](/knowledge/contributing-to-monero)/

  * [遠程節點如何影響門羅幣的隱私](/knowledge/remote-nodes-privacy)/

  * [門羅幣是如何使用硬分叉為升級網絡](/knowledge/network-upgrades)/

  * [查看標籤：一個字節如何將門羅幣錢包的同步時間減少40%以上](/knowledge/view-tags-reduce-monero-sync-time)/

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