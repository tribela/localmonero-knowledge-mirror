---
title: "為什麼門羅幣優於達世幣, 大零幣, 小零幣 , 古靈幣以及經過Wasabi級別混幣器混淆後的比特幣 (更新於2020年五月)"
slug: "why-monero-is-better"
date: "2024-01-01"
image: "/images/why-monero.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
不是所有的匿名幣都能提供百分之百的隱私保護, 保護隱私需要滿足的條件包括，不可追蹤性, 安全性，可替換性，無需初始信任設置和真正的去中心化. 這些屬性是什麼以及它們為何重要的原因:

## 加密貨幣分析

下面給出的分析比較了那些主流隱私幣/匿名幣他們的區別和不同. 比特幣並不在這個討論的範疇內，而比特幣本身也從未聲稱過它是匿名的.

這個頁面是由門羅幣的用戶創建的. 曾幾何時的我們還不是門羅幣用戶，但我們注重隱私保護. 於是我們研究了那些聲稱能夠保護隱私的加密貨幣，本頁面歸納整理了我們的結論. 這就是為什麼我們選擇門羅幣而不是其他的幣. 也許你覺得我們對其他幣帶有偏見，即便如此，我們的偏見也是基於以下事實，您可以在下面閱讀這些內容並自己來驗證.

### 概述

選擇一個幣的圖片logo跳轉查看該幣的具體分析.

### Monero

門羅幣從一開始就是百分之百的開源項目, 也就是說任何人都可以查看它的 [ 開原始程式碼 ](https://github.com/monero-project/bitmonero) 來確定門羅幣沒有暗箱操作留有後門，也沒有安全性的問題.

還有一篇門羅幣的[ 同行業內的研究報告 ](https://lab.getmonero.org/) 從數學層次上和系統性對上述屬性進行了驗證.

### DASH

達世幣擁有一個 [ 富豪榜](https://bitinfocharts.com/top-100-richest-darkcoin-addresses.html), 所以達世幣稱不上隱私幣. 通過檢索區塊鏈的任何人都可以看到每個帳戶的財務詳細資訊.

> 達世幣根本不算密碼學意義上的隱私加密貨幣. 事實上我演說幻燈片裡有一頁就是這樣的 '達世幣, 呵呵,' 別的無話可說... 達世幣我個人看來就是江湖術士賣的狗皮膏藥，大力丸，本人敬而遠之. 
> 
> **Gregory Maxwell** , 比特幣的核心開發者和密碼學家, 在一篇 [ 給Coinbase交易所的演講裡提到 ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

達世幣根本不算密碼學意義上的隱私加密貨幣. 事實上我演說幻燈片裡有一頁就是這樣的 '達世幣, 呵呵,' 別的無話可說... 達世幣我個人看來就是江湖術士賣的狗皮膏藥，大力丸，本人敬而遠之. 

**Gregory Maxwell** , 比特幣的核心開發者和密碼學家, 在一篇 [ 給Coinbase交易所的演講裡提到 ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

**Peter Todd** , 另一位比特幣核心開發者成員和密碼學家, 發表了一篇 [ 類似的文章](https://twitter.com/petertoddbtc/status/622022840330682368).

### Zcash

大零幣的交易記錄在區塊鏈上是可視的. 雖然他們可以選擇隱藏交易記錄, 但是只有 [ 不到 1% 的交易被隱蔽起來 ](http://stat.bloxy.info/superset/dashboard/zcash/) . 由於隱藏交易並不是系統預設的，而是一個額外的可選選項，並且基本上沒人用這個功能, 因此 [ 當隱藏的交易又出現在區塊鏈上的時候](http://weuse.cash/2016/06/09/btc-xmr-zcash/), 就格外引人注意.

> 順便說一句，對於像WannaCry這樣的犯罪分子，我認為我們可以成功地追蹤他們的大零幣, 可我還是覺得我們是隱私的並且是可替換性. 
> 
> **Zooko Wilcox** , 大零幣的 CEO, 在一個 [ 推文中表示 ](https://twitter.com/zooko/status/863202798883577856)

順便說一句，對於像WannaCry這樣的犯罪分子，我認為我們可以成功地追蹤他們的大零幣, 可我還是覺得我們是隱私的並且是可替換性. 

**Zooko Wilcox** , 大零幣的 CEO, 在一個 [ 推文中表示 ](https://twitter.com/zooko/status/863202798883577856)

如果大零幣可以 "輕易追蹤", 那麼就不能稱作完美的隱私和具備可替換性. 

普通轉帳是透明的. 隱藏交易使用了零知識證明技術的 zk-SNARKS, 在某些情況下有比較可靠的隱私保證. 但問題是這個某些前提條件並不好滿足, 並且使用這個隱私功能的人太少, 這種情況導致了新的問題.

Zcash 大零幣是公司幣，並且該公司還 [ 抽取發行總量的20%的大零幣作為基金會的收入](https://z.cash/blog/funding.html). 

大零幣還要求 **初始信任設置**. 這意味著你必須信任參與初始信任設置的人們是誠實的. 可如果他們不是那麼誠實, [ 那麼無限量的大零幣就會被增發出來，並且不會有人察覺](https://blog.okturtles.com/2016/03/the-zcash-catch/). 這可能導致大零幣價格暴跌，駭客暴富. 沒有任何辦法可以去驗證初始信任設置到底是不是誠實可信. 用戶只能對他們的話照單全收. 這種將人性作為某個潛在的故障點引入了系統，幾乎與其他所有加密貨幣完全相反. 您本應只信任加密貨幣中的數學和可驗證的原始程式碼，而不是人性. 正如我們在幾乎所有大型軟體公司中看到的那樣, 例如 [ 微軟公司](https://www.gnu.org/proprietary/proprietary-back-doors.en.html), [ 蘋果公司](http://www.digitaltrends.com/computing/apple-vs-fbi-backdoor-to-data-already-exists/), 甚至政府, 他們都不應該被信任. 

Peter Todd, 作為比特幣核心的開發者成員 [ 曾參與了 ](https://github.com/zcash/mpc/blob/master/README.md) 大零幣的初始信任設置, 並且稱它為 " [ 後門問題 ](https://twitter.com/petertoddbtc/status/793584540891643906) ". 

> 大零幣的功能實現並不是無條件的, 在目前的技術條件下不能...它要求一個初始信任設置… 隨著時間的推移將需要重做程式才能彌補 [初始信任設置] 這個漏洞. 
> 
> Gregory Maxwell, 比特幣的核心開發成員，密碼學家, 在一個 [ Coinbase交易所的演講裡說到](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

大零幣的功能實現並不是無條件的, 在目前的技術條件下不能...它要求一個初始信任設置… 隨著時間的推移將需要重做程式才能彌補 [初始信任設置] 這個漏洞. 

Gregory Maxwell, 比特幣的核心開發成員，密碼學家, 在一個 [ Coinbase交易所的演講裡說到](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

### Zcoin

**請注意:** Zcoin正在從當前的Sigma協定方案轉變為新協定Lelantus. Lelantus將分階段實施，本文將假設所有階段均已完成並已實施，而不是現在的技術，以便其與其它幣進行適當的比較.

為什麼拿小零幣未來還沒有落地的技術於其它幣做比較，而大零幣按已經落地的技術進行技術評判，這是因為Zcoin小零幣的路線圖包含啟動協議的時間安排，而Zcash大零幣的默認隱私計畫，不論現在還是以後的計畫都是模糊不確定的

Zcoin 小零幣(XZC) 將不再有富豪榜, 所以將會保護隱私. 預設情況下，預計將於2021年強制性隱私生效. 一旦實施，將再也看不到富豪榜(現在仍舊 [可以看到小零幣富豪榜](https://www.coinexplorer.net/XZC/richlist)).

### Grin

### Bitcoin Mixers

所有的比特幣交易都記錄在區塊鏈上，任何人都能隨時隨地查看，並且還有一個比特幣的 [ 富豪榜排名](http://www.bitcoinrichlist.com/top100), 所以比特幣不能保護財產隱私. 比特幣只是 [ 假名系統](https://bitcoin.org/en/you-need-to-know), 並不是匿名系統，"就像微信，你可以給自己起任何昵稱，可是綁定的銀行卡和手機會暴露真實用戶". 

對於 **比特幣混幣器** , 你只能寄希望於他們能保護他們的客戶資訊安全，並且不會被政府法律施壓, 不被駭客組織盜取資料, 或與其它機構達成某種形式上的收購，合作，或者共用資料. 

在2017年7月, 最大的比特幣混幣服務商 BITMIXER.IO, 宣佈他們即刻終止比特幣混幣服務並聲明以下原因: 

> … 現在我們認識到比特幣是透明的而非匿名系統的事實 **這是基於它底層設計決定的**. 區塊鏈就像是一本很棒的公開書… 
> 
> BITMIXER.IO, 在一篇聲明裡宣稱 [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (原文為重點). 

… 現在我們認識到比特幣是透明的而非匿名系統的事實 **這是基於它底層設計決定的**. 區塊鏈就像是一本很棒的公開書… 

BITMIXER.IO, 在一篇聲明裡宣稱 [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (原文為重點). 

在考察了多種保護隱私為主的加密貨幣的幾周後, 他們做了如下聲明: 

> 經過深入調查和研究，我們確定門羅幣才是最好的隱私幣. 所以強烈推薦格外注意隱私的人，直接使用門羅幣. 
> 
> BITMIXER.IO, in a [ 後續跟帖](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

經過深入調查和研究，我們確定門羅幣才是最好的隱私幣. 所以強烈推薦格外注意隱私的人，直接使用門羅幣. 

BITMIXER.IO, in a [ 後續跟帖](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

正是由於比特幣每筆交易都是在區塊鏈上明文記錄的, 所以每筆比特幣交易都可以被追蹤. 比特幣混幣器可以高度混淆一筆比特幣交易, 讓追蹤比特幣變得困難, 但是世事無絕對. 隨著技術的進步和專注於追蹤比特幣交易的公司變得越來越普遍, 高度混幣過的比特幣也將變得容易追蹤: 

  * [ 執法部門持續投入比特幣跟蹤服務 ](https://news.bitcoin.com/law-enforcement-continues-invest-bitcoin-tracking-services/)
  * [ Time.com: 比特幣比你想像的還要好追蹤 ](http://time.com/3689359/bitcoins-track-anonymous/)
  * [ Elliptic: 一家專門追蹤比特幣執法的公司 ](https://www.elliptic.co/)

通過穀歌搜索，您會發現數十篇類似的文章. 請記住, 過去發生在任何時間的比特幣交易記錄都被永久記錄在區塊鏈上，現在和未來都有潛在被追蹤和分析出來的機會, 不論是不是經過混幣器處理過的交易. 事實上, 使用混幣服務的幣才更加惹人注意，正所謂欲蓋彌彰. 

並不是每一枚比特幣的價值都是等值的. 有些比特幣在黑名單列表上並且被多個主體限制交易,這些在黑名單上的幣價值就比沒有在黑名單上的幣價值低. 如果你收到的比特幣曾被用於犯罪, 那麼即便你沒有參與犯罪你的比特幣也會被列入黑名單. 又或者, 在未來不管是某國政府，某個老闆，或者其它主體決定把你的比特幣加進黑名單, 就如同現在他們有權和有能力凍結和沒收另一些人的財產. 普通人對此是無能為力的. 因為混幣器的混幣服務只是讓追蹤你的比特幣稍困難了一些, 比特幣這類問題我們稱作 "not fungible 沒有可替換性." 

  * 前比特幣核心開發組成員，在比特幣和其它社區都深受尊重的Andreas Antonopoulos, 意識到比特幣缺乏可替換性的問題在一個 [ YouTube 視頻採訪裡](https://www.youtube.com/watch?v=ak1iojpiHpM&feature=youtu.be&t=33m9s). 
  * 並且在Bitcointalk上也討論了比特幣沒有可替換性的題 [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=1190707.0)

## 總結

在我們看來如果你在尋找一個能保護隱私, 安全可靠, 不可追蹤, 具備可替代性,不需要初始信任設置的加密貨幣，那麼門羅幣就是最佳的選擇. 任何其他的貨幣都讓您的隱私和安全受到威脅. 當然了不要只聽我們的觀點. 您應該自己去進行調查和深入研究. 可以參考一下門羅已經被哪些需要隱私保護和反追蹤的主體接受和使用, 例如: 

  * [ 暗網匿名郵件服務商SIGAINT ](https://www.reddit.com/r/Monero/comments/4xqrzd/sigaint_launches_tor_monero_node_as_its_operators/)
  * [ Purism純粹主義 ](https://puri.sm/posts/purism-collaborates-with-cryptocurrency-monero-to-enable-mobile-payments/)
  * [ 維琪解密 ](https://shop.wikileaks.org/donate#db9)
  * 2017年七月暗網AlphaBay Market (AB) 被關閉. 披露的檔顯示 [ 聯邦政府 ](https://assets.documentcloud.org/documents/3898109/AlphaBay-Cazes-Forfeiture-Complaint.pdf) 在沒收聲明裡說到: 
    * **門羅幣是唯一的匿名隱私不可追蹤的加密貨幣:**   
"總共，從CAZES的錢包和電腦代理那裡繳獲了大約$8,800,000 美金的比特幣, 乙太坊, 門羅幣, 和大零幣, 具體明細是: 1,605.0503851 美金的比特幣, 8,309.271639 美金的乙太坊, 3,691.98 美金的大零幣, _以及未知數量的門羅幣._ " (p. 20頁底部和p. 21頁頂部, 畫了重點) 
    * **比特幣的交易並不隱私並且可以被追蹤:**   
"聯邦特工在追蹤了許多源自AlphaBay的比特幣和數位貨幣帳戶之間的轉帳確定了其涉案金額, 最終認定了CAZES和他的妻子持有的銀行帳戶和其他有形資產." (17頁, 24-26行) 

  * **門羅幣是唯一的匿名隱私不可追蹤的加密貨幣:**   
"總共，從CAZES的錢包和電腦代理那裡繳獲了大約$8,800,000 美金的比特幣, 乙太坊, 門羅幣, 和大零幣, 具體明細是: 1,605.0503851 美金的比特幣, 8,309.271639 美金的乙太坊, 3,691.98 美金的大零幣, _以及未知數量的門羅幣._ " (p. 20頁底部和p. 21頁頂部, 畫了重點) 
  * **比特幣的交易並不隱私並且可以被追蹤:**   
"聯邦特工在追蹤了許多源自AlphaBay的比特幣和數位貨幣帳戶之間的轉帳確定了其涉案金額, 最終認定了CAZES和他的妻子持有的銀行帳戶和其他有形資產." (17頁, 24-26行) 

LocalMonero 不主張也不鼓勵任何非法活動. 

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

  * [ 新的CLSAG環簽名技術將如何提高門羅幣的效率](/knowledge/what-is-clsag/)

  * [為什麼門羅幣擁有尾部增發的特性](/knowledge/monero-tail-emission/)

  * [門羅幣的前世今生](/knowledge/monero-history/)

  * [Wired雜誌是如何誤解了門羅](/knowledge/wired-article-debunked/)

  * [流言終結者：關於門羅幣的15大傳言和疑慮](/knowledge/monero-myths-debunked/)

  * [Dandelion ++蒲公英改進協議如何使Monero從源頭得到更強防護](/knowledge/monero-dandelion/)

  * [為什麼門羅幣是開源且去中心化的](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [門羅幣挖礦: 什麼使 RandomX 算法如此特別](/knowledge/monero-mining-randomx/)