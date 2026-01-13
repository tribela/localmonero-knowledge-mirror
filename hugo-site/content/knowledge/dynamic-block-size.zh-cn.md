---
title: "门罗币是如何解决困扰比特币的区块大小的扩容问题"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**注：** 强烈建议读者阅读我们的文章[“为什么门罗币有尾部发射”](/knowledge/monero-tail-emission)和[“门罗币挖矿：是什么造就了RandomX”太特别了”](/knowledge/monero-mining-randomx)。本文以其中提出的概念为基础。_

每当人们讨论区块链问题时，第一个出现的词就是“扩展”。区块链不能很好地扩展已经不是什么秘密了，但大多数人不知道为什么。

事实是，扩展实际上是一个涵盖两个不同类别的总称：协议支持和给定时间点的技术支持。在本文中，我们将重点关注一个问题，协议支持基本上是衡量协议在给定时间可以处理多少事务的指标。

比特币有区块大小限制，这意味着一旦一个区块中包含足够的交易，任何额外的交易都必须排队等待下一个区块。一个有用的类比是考虑火车。一列火车进站，排队的人鱼贯而入。一旦火车满员，留在外面的人就必须等待下一班车。

比特币使用费用来确定谁进入区块或不进入区块。回到火车的类比，我们可以想象一位即将被抛在后面的潜在乘客向火车工程师提供五美元以给他一个座位。其他乘客也纷纷效仿，最终引发一场竞购战，看看谁能获得哪个座位。由司机决定是否遵守先到先得的政策，但通过接受出价最高的人上车来最大化他的收入符合他的最佳经济利益。

在这个比喻中，矿工就是火车司机。他们可以在区块中包含他们想要的任何交易，但他们通常会选择支付费用最高的交易。

或者，如果区块不是很满，人们就没有动力支付高额费用，因为有大量空闲座位。

在 2017 年加密货币繁荣的鼎盛时期，比特币交易量激增，对于那些想要包含在下一个区块或任何近期区块中的人来说，费用飙升。那些不愿意支付高额费用的人则发现他们的交易被推迟了几个小时、几天，甚至完全退出了队列。

这是对如果经常谈论的“大规模采用”发生的话比特币将会如何发展的一个令人痛心的见解。如果比特币被大众使用，情况会比 2017 年更糟糕，除了富人之外，任何人都无法使用比特币，因为区块大小固定，吞吐量很小，导致费用市场占据主导地位。 .

门罗币预见到了这一点并想做一些不同的事情。因此门罗币开发人员实现了动态区块大小。

基本上，门罗币也有区块大小上限，但它是软上限。当等待交易的队伍太长时，矿工可以增加区块的大小。通过我们的火车类比，您可以想象添加更多的火车车厢来容纳额外的乘客。队列为空后，块会缩小到原始大小。

如果这看起来是一个好主意，那么有理由问为什么门罗币是唯一实现这一点的加密货币。为什么不将其添加到比特币上以解决吞吐量问题？

不幸的是，这是不可能的。原因有很多，我们会尽力解释。

拥有大区块始终符合矿工的最大利益。有了大区块，他们就可以容纳更多交易，并从费用和区块奖励中赚到更多钱。这有可能导致垃圾邮件攻击，即有人发送许多小额交易，收取少量费用，从而使链条膨胀。矿工只会提高区块大小，将它们全部包括在内，因为钱就是钱，无论多小。这将导致区块持续大而经济效益微乎其微。比特币通过人为限制区块大小来解决这个问题，从而产生费用市场。垃圾邮件攻击者必须支付高于其他用户的费用，而且费用不再便宜。但这意味着区块已满，留下一些交易等待，如上所述。

那么门罗币如何拥有动态区块大小同时避免垃圾邮件攻击呢？答案很简单，但很聪明。当区块比正常情况大时，就会对区块奖励进行惩罚。如果矿工想要增加区块大小，他们从找到该区块中获得的奖励将少于他们原本获得的奖励。因此，只有当用户支付的交易费用超过区块奖励损失的部分时，他们才会增加区块大小。例如，如果矿工因增加区块大小而损失 0.5 XMR，而支付的交易费用总和为 0.4 XMR，那么如果他们增加区块大小，将净损失 0.1 XMR，因此他们不会不要这样做。相反，如果总交易费用加起来为 0.7 XMR，那么即使他们因区块奖励惩罚而损失了 0.5 XMR，也会获得 0.2 XMR 的净收益，因此矿工将增加规模。

这些动态区块允许网络有机增长，无需人为限制区块大小以形成强制费用市场，同时仍然避免垃圾邮件攻击。我们可以从更多角度来看待这个想法，以及为什么它不可能添加到比特币的更多原因，但现在，我们希望读者了解门罗币如何回避比特币中的几个问题，以及它的衍生品，以及它计划如何在未来扩展其吞吐量。

进一步阅读

  * [门罗币如何独特地实现循环经济](/knowledge/monero-circular-economies/)

  * [门罗币环形签名与CoinJoin像在Wasabi比较](/knowledge/ring-signatures-vs-coinjoin/)

  * [为什么（以及如何！）你应该持有你自己的钥匙](/knowledge/hold-your-keys/)

  * [贡献为门罗币](/knowledge/contributing-to-monero/)

  * [远程节点如何影响门罗币的隐私](/knowledge/remote-nodes-privacy/)

  * [门罗币是如何使用硬分叉为升级网络](/knowledge/network-upgrades/)

  * [查看标签：一个字节如何将门罗币钱包的同步时间减少40%以上](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool和它在去Monero采矿中心化的作用](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis：它将为门罗币做什么](/knowledge/seraphis-for-monero/)

  * [把比特币兑换成门罗币，就可以高枕无忧了吗?](/knowledge/most-private-way-to-buy-monero/)

  * [为什么门罗币不像大零币那样需要初始信任来实现隐私](/knowledge/monero-trustless-setup/)

  * [为什么门罗币才是电子黄金，相对于比特币更有储存价值的属性](/knowledge/monero-better-store-of-value/)

  * [门罗币是如何蚕食比特币的份额和先发优势](/knowledge/network-effect/)

  * [为什么说门罗币社区最具批判性精神](/knowledge/critical-thinking/)

  * [门罗币防诈骗指南](/knowledge/monero-scams/)

  * [原子互换技术将如何在门罗币上实现](/knowledge/monero-atomic-swaps/)

  * [门罗币与当代互联网，隐私达人的须知](/knowledge/monero-networking/)

  * [ RingCT环形机密技术是如何隐藏门罗币交易的金额](/knowledge/monero-ringct/)

  * [门罗币隐身地址如何保护你的身份](/knowledge/monero-stealth-addresses/)

  * [门罗币子地址是如何防止用户信息被关联](/knowledge/monero-subaddresses/)

  * [加密货币里面的output，中文译作输出，这个概念到底什么意思,又为什么门罗币转账后余额显示错误要等待二十分钟](/knowledge/monero-outputs/)

  * [门罗币最佳入门指南](/knowledge/monero-best-practices/)

  * [环形签名如何保护门罗币发送者的输出](/knowledge/ring-signatures/)

  * [ 新的CLSAG环签名技术将如何提高门罗币的效率](/knowledge/what-is-clsag/)

  * [为什么门罗币拥有尾部增发的特性](/knowledge/monero-tail-emission/)

  * [门罗币的前世今生](/knowledge/monero-history/)

  * [Wired杂志是如何误解了门罗](/knowledge/wired-article-debunked/)

  * [流言终结者：关于门罗币的15大传言和疑虑](/knowledge/monero-myths-debunked/)

  * [Dandelion ++蒲公英改进协议如何使Monero从源头得到更强防护](/knowledge/monero-dandelion/)

  * [为什么门罗币是开源且去中心化的](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [门罗币挖矿: 什么使 RandomX 算法如此特别](/knowledge/monero-mining-randomx/)

  * [为什么门罗币优于达世币, 大零币, 小零币 , 古灵币以及经过Wasabi级别混币器混淆后的比特币 (更新于2020年五月)](/knowledge/why-monero-is-better/)