---
title: "查看标签：一个字节如何将门罗币钱包的同步时间减少40%以上"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
围绕日常使用门罗币最常见的抱怨之一是在能够发送门罗币之前同步钱包的时间。幸运的是，门罗币社区的开发者和研究人员已经找到了一个绝妙的方法，可以将你同步钱包的时间减少40%以上，而且没有任何额外的区块链臃肿、费用等。

“查看标签 （View tags）”，这是每个交易数据中的一个字节的补充--出在下一个门罗币网络升级！

## 为什么门罗币的钱包同步速度比比特币的慢？

## 为什么门罗币的钱包同步速度比比特币的慢？

为了更好地理解查看标签这样的解决方案的需求，我们首先要回答的一个问题是，为什么门罗币的钱包同步速度比比特币等加密货币慢。

在比特币中，由于所有的交易都不是私密的，会在链上显示被花费的硬币、金额和涉及的地址，比特币钱包可以简单地寻找任何未花费的交易输出（UTXO）或特定钱包的使用地址，快速扫描区块链，只寻找这些地址所拥有的UTXO，以找出哪些硬币属于你的钱包并可以被花费。

然而，在门罗币中，所有交易都通过隐藏发送人、收款人和每笔交易涉及的金额来保护用户的隐私。这种隐私，虽然对保护网络用户至关重要，但也带来了较慢的钱包同步。在门罗币中，你的钱包必须将网络上存在的每一笔交易输出（TXO）与你钱包的私钥进行比较。

这种比较涉及到很多复杂的数学和密码学，以验证一个输出是真正属于你的，因为所有的金额、地址和已知花费的输出（或币）都隐藏在门罗币的链上。

## 查看标签是什么？

## 查看标签是什么？

为了帮助减少门罗币钱包的同步时间， [一位名叫UkoeHB的研究人员想出了一个新的方法](https://github.com/monero-project/research-lab/issues/73) – 在每笔交易中添加一个1字节的 “标签”，使用只有该交易的发送方和接收方知道的共享秘密。

这个共享秘密是由发送方使用接收方提供给他的地址生成的，不需要发送方和接收方的任何主动合作。这个共享秘密的第一个字节（或字符）然后在发布到门罗币网络时被添加到交易的数据中。

当该交易的参与者之一想在之后将他们的钱包与门罗币区块链同步时，而不是需要对网络上的每一个交易输出执行所有复杂的数学和密码学，钱包现在可以只检查每笔交易中的那个1字节字段，然后只对有这个标签的交易执行耗时的验证--准确地说，是网络上1/256个交易输出！

这个标签不会向外界透露任何关于交易的信息，只增加1个字节（可以忽略不计）的交易大小，但通过减少必要的复杂验证，我们可以将同步时间减少40%以上！

## 查看标签：一个简化的例子

## 查看标签：一个简化的例子

想象一下，你在一个房间里有4,096个盒子，其中只有5个盒子是属于你的。这些盒子从外面看完全没有区别，要想知道一个盒子是否属于你，唯一的办法就是打开它，解决里面写的一道耗时的数学题，以确保它是你的。

现在，想象一下，你决定让寄给你这5个盒子的人用你的地址生成一个特殊的代码，然后在寄给你的每个盒子的外面只写上该代码的第一个字符。其他人对他们的盒子也做了同样的事情（以确保所有的盒子仍然是不可区分的），但现在你可以简单地看一下盒子外面的一个字符代码，并只打开那些有这个字符的盒子。

虽然其他盒子会与你的代码相匹配，甚至是一些不属于你的盒子，但你需要打开并解决一个数学问题的盒子数量现在只有16个（1/256个盒子！），而不是全部的4096个盒子。

现在你打开这16个盒子，解决数学问题，并保留那组中真正属于你的5个盒子!

## 查看标签何时能在门罗币中使用？

## 查看标签何时能在门罗币中使用？

查看标签是目前计划纳入 [即将到来的网络升级](https://github.com/monero-project/meta/issues/630), 的功能之一，应该在今年春天的某个时候发布。 社区 [筹集了23.3 XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) （在撰写本文时）来激励查看标签的开发和实施，因此，绝大部分将查看标签纳入门罗币代码库的工作已经由j-berman与审核员和研究人员合作完成。

一旦查看标签被网络强制执行，所有在网络升级后发送的交易都将受益于大幅改善的钱包同步时间。你不需要做任何特别的事情来开始使用查看标签，你最喜欢的门罗币钱包将在网络升级后自动开始使用它们!

## 我如何能了解更多？

## 我如何能了解更多？

如果这已经激起了你对查看标签的好奇心，请看下面一些深入研究该主题的外链接：

  * [用每输出一个字节的 ‘查看标签’减少扫描时间](https://github.com/monero-project/research-lab/issues/73)
  * [为输出添加查看标签以减少钱包扫描时间](https://github.com/monero-project/monero/pull/8061)

进一步阅读

  * [门罗币如何独特地实现循环经济](/knowledge/monero-circular-economies)/

  * [门罗币环形签名与CoinJoin像在Wasabi比较](/knowledge/ring-signatures-vs-coinjoin)/

  * [为什么（以及如何！）你应该持有你自己的钥匙](/knowledge/hold-your-keys)/

  * [贡献为门罗币](/knowledge/contributing-to-monero)/

  * [远程节点如何影响门罗币的隐私](/knowledge/remote-nodes-privacy)/

  * [门罗币是如何使用硬分叉为升级网络](/knowledge/network-upgrades)/

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

  * [ 新的CLSAG环签名技术将如何提高门罗币的效率](/knowledge/what-is-clsag)/

  * [为什么门罗币拥有尾部增发的特性](/knowledge/monero-tail-emission)/

  * [门罗币的前世今生](/knowledge/monero-history)/

  * [Wired杂志是如何误解了门罗](/knowledge/wired-article-debunked)/

  * [流言终结者：关于门罗币的15大传言和疑虑](/knowledge/monero-myths-debunked)/

  * [Dandelion ++蒲公英改进协议如何使Monero从源头得到更强防护](/knowledge/monero-dandelion)/

  * [为什么门罗币是开源且去中心化的](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [门罗币挖矿: 什么使 RandomX 算法如此特别](/knowledge/monero-mining-randomx)/

  * [为什么门罗币优于达世币, 大零币, 小零币 , 古灵币以及经过Wasabi级别混币器混淆后的比特币 (更新于2020年五月)](/knowledge/why-monero-is-better)/

进一步阅读