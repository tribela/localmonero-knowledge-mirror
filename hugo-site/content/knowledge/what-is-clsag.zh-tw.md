---
title: "新的CLSAG环签名技术将如何提高门罗币的效率"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
关于门罗币的协议层，目前仍处于持续创新的状态. 门罗币社区通过对链上和链下各种方案的研究，不断探索可改进的领域，从而使门罗币更加保护隐私，更具可扩展性，对普通用户更友好和便于使用，门罗币最新的创新之一是关于用CLSAG技术来替代MLSAG环签名技术，CLSAG全称是Concise Linkable Spontaneous Anonymous Group，它更简洁的实现MLSAG技术方案.

从目前来看，CLSAG的实施将使最常见的门罗交易，也就是通常包含2个输入和2个输出的区块体积减少25％.同时还将减少10％的验证时间.

但是CLSAG到底是什么？ 它有什么作用？与旧版本的MLSAG有何不同？ 那么让我们先花点时间回顾一下，门罗币为什么和如何进行环签名，以便帮助我们更好地理解这一概念. 在一个交易中，发送者需要用自己的私钥进行签名，目前门罗币的一个输出中，包含11个签名，只有一个是发送者本身的，剩余的签名是从整个门罗币历史匿名集中抓取其它人的签名，通过这样可以实现非交互的，包括见证者都无法区分的真实输入. 用外行的话来说，环签名技术，只需要搭配区块链本身，在默认情况下，不需要额外操作和其它任何人参与，自动利用自身输出以及完全不相关的输出，就可以隐藏交易发起人.节点和任何第三方也没有办法分辨. 这些输出中的每一个签名者都有可能是实际发送的输出，从而隐藏了有关发送者的元数据.

但是，这就会让人会产生一系列的疑问. 如果用户要从所有的门罗币历史签名里构造一个假的环形签名怎么办？ 发送者是匿名的，他到底有没有足够的权限和足够的资金？ 该用户可以花假钱吗？ 答案是肯定不可以.环形签名包括一种方法，用于证明签名中至少有一个输出，是由一个真实的发送人拥有，而无需透露它是哪一个. 实际上，CLSAG和MLSAG都是证明这一点的一部分. 以下我们统称它们为SAGs. 与此同时，它也能在匿名的情况下证明，隐藏在机密交易RingCT后面的交易金额仍能平衡，没有人能双花和凭空花费. 总的来说SAGs证明了两件事，一个是输出中11个签名中其中有一个是真实的，归属于某人，同样很重要的是，第二点，交易账户不会被超额花费，转账前后账目平衡. 实际上这部分就是压缩大小和节省验证时间的地方. 如果听到这里，令人困惑，请放心，我们将为你带来一个有趣且易于理解的比喻.

旧的签名方案MLSAG，全称是Multilayered Linkable Spontaneous Anonymous Group，在环签名中证明了上述两件事，但它们是分别进行的.对签名和承诺密钥使用单独的计算意味着速度较慢. 虽然现代计算机可以在几毫秒内完成这些计算，这看起来速度很快，对于一次交易和区块扫描而言，也确实很快. 但是当我们考虑到门罗币Monero区块链上的大量交易，并且从头开始同步的节点必须下载并验证每个交易时，字节大小和毫秒时间的微小差异最后会堆积如山.

CLSAG将证明两者所需的数学结合在一起，并同时计算两者，并且以一种安全的方式进行. 什么是安全的方式计算呢？ 好吧，为澄清这一点，并希望使整个事情变得更好理解，让我们来看一个关于验证承诺的有趣比喻.

假设你需要同时前往杂货店和五金店，购买两种不同的东西，分别为食物和有毒的清洁剂. 你不希望它们混和在一起，如果不小心发生意外，化学物质会溅到食物上，使它们变得不可食用. 你决定安全第一，所以从家中先开车去杂货店购买食物，然后回到家中. 接着卸下食物后，才又回到车里，开车去五金店，然后带着化学品回到家中. 你进行了两次单独的行动，来确保所有购物的安全. 尽管确实安全，但效率低下. 这很像MLSAG环形签名，它其中存储了两组不同的数学运算，并分别进行了两次不同的运算.

但是这种方式实在太慢了,并且太浪费时间了.当然偶尔做一次是没有什么问题，但是如果一遍又一遍的重复往复，时间开始累加起来就会很可怕. 你需要一种更快的方法. 是否可以试着这样改变呢， 先从你的房子到杂货店，再到五金店，再开车回家. 当然这样你不能随便把所有东西扔在车上. 这不安全，不过可以在汽车中设置不同的位置，并确保所有物品都整齐地放置在其位置上. 这样一来，就可以安全地前往两家商店，并且让食物和化学品保持安全远离. 这个新的变化就是CLSAG签名. 现在，在一个交易中仅存储了一组数学运算即可证明这两件事，并且确保它们不会互相干扰.仍然需要运算，但是已经大大减少了运算时间，就像仍然需要开车去不同的商店，可路程大大减少.

所有这些进步听起来很令人兴奋. 那么是否可以找到其它更快捷得方式或更节省时间和空间的方法进一步升级呢？ 答案是肯定的. 目前门罗MRL组研究人员表示，虽然当前可能无法进一步修改SAGs这一型结构以获得更小的尺寸或速度. 但是，其他环签名结构例如Arcturus，Omniring，RCT3或Triptych，它们使用了不同的数学方法，这样会产生更小的数据大小和更快得验证速度. 但是，每种下一代环形签名技术协议的实现细节上都有其自身的取舍，门罗社区正在积极研究和调查各种方案的优缺点.

进一步阅读

  * [门罗币如何独特地实现循环经济](/knowledge/monero-circular-economies)/

  * [门罗币环形签名与CoinJoin像在Wasabi比较](/knowledge/ring-signatures-vs-coinjoin)/

  * [为什么（以及如何！）你应该持有你自己的钥匙](/knowledge/hold-your-keys)/

  * [贡献为门罗币](/knowledge/contributing-to-monero)/

  * [远程节点如何影响门罗币的隐私](/knowledge/remote-nodes-privacy)/

  * [门罗币是如何使用硬分叉为升级网络](/knowledge/network-upgrades)/

  * [查看标签：一个字节如何将门罗币钱包的同步时间减少40%以上](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool和它在去Monero采矿中心化的作用](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis：它将为门罗币做什么](/knowledge/seraphis-for-monero)/

  * [把比特币兑换成门罗币，就可以高枕无忧了吗?](/knowledge/most-private-way-to-buy-monero)/

  * [为什么门罗币不像大零币那样需要初始信任来实现隐私](/knowledge/monero-trustless-setup)/

  * [为什么门罗币才是电子黄金，相对于比特币更有储存价值的属性](/knowledge/monero-better-store-of-value)/

  * [门罗币是如何蚕食比特币的份额和先发优势](/knowledge/network-effect)/

  * [为什么说门罗币社区最具批判性精神](/knowledge/critical-thinking)/

  * [门罗币防诈骗指南](/knowledge/monero-scams)/

  * [原子互换技术将如何在门罗币上实现](/knowledge/monero-atomic-swaps)/

  * [门罗币与当代互联网，隐私达人的须知](/knowledge/monero-networking)/

  * [ RingCT环形机密技术是如何隐藏门罗币交易的金额](/knowledge/monero-ringct)/

  * [门罗币隐身地址如何保护你的身份](/knowledge/monero-stealth-addresses)/

  * [门罗币子地址是如何防止用户信息被关联](/knowledge/monero-subaddresses)/

  * [加密货币里面的output，中文译作输出，这个概念到底什么意思,又为什么门罗币转账后余额显示错误要等待二十分钟](/knowledge/monero-outputs)/

  * [门罗币最佳入门指南](/knowledge/monero-best-practices)/

  * [环形签名如何保护门罗币发送者的输出](/knowledge/ring-signatures)/

  * [门罗币是如何解决困扰比特币的区块大小的扩容问题](/knowledge/dynamic-block-size)/

  * [为什么门罗币拥有尾部增发的特性](/knowledge/monero-tail-emission)/

  * [门罗币的前世今生](/knowledge/monero-history)/

  * [Wired杂志是如何误解了门罗](/knowledge/wired-article-debunked)/

  * [流言终结者：关于门罗币的15大传言和疑虑](/knowledge/monero-myths-debunked)/

  * [Dandelion ++蒲公英改进协议如何使Monero从源头得到更强防护](/knowledge/monero-dandelion)/

  * [为什么门罗币是开源且去中心化的](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [门罗币挖矿: 什么使 RandomX 算法如此特别](/knowledge/monero-mining-randomx)/

  * [为什么门罗币优于达世币, 大零币, 小零币 , 古灵币以及经过Wasabi级别混币器混淆后的比特币 (更新于2020年五月)](/knowledge/why-monero-is-better)/

进一步阅读