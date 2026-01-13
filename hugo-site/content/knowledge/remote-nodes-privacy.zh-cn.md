---
title: "远程节点如何影响门罗币的隐私"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
与其他加密货币相比，门罗币最大的优势之一是它的链上隐私，但你有没有想过，当你使用远程节点时，门罗币的隐私是如何保持的？如果你使用像MyMonero "轻型钱包"服务器呢？

在这篇文章中，我们将深入探讨门罗币在使用远程节点时如何提供卓越的链上隐私的一些细节，以及在使用远程节点时需要注意的问题。

## 节点在门罗币中具有什么功能？

对于那些不太熟悉门罗币工作方式的人来说，门罗币网络中的节点（或服务器）可以由任何人运行，并允许节点的所有者或他们选择与之共享的其他人来同步区块链的一个副本，并将该副本提供给网络上的其他人。这些节点还验证网络上发生的所有交易，以及所有发布的区块，并确保它们都遵循共识所设定的规则。

节点在门罗币中的另一个功能是提供你最喜欢的门罗币钱包所需的所有数据，以正确检查属于你的交易并进行新的交易。这些数据是由节点以两种方式提供的：

  * 区块链上每个区块的数据被钱包要求，扫描属于你的交易，然后在钱包检查后被丢弃。 
    * 由于 [查看标签](/knowledge/view-tags-reduce-monero-sync-time)的存在，这一步骤很快就会得到大幅改善。
  * 当发送交易时，你使用的节点提供一个可能的诱饵（或假输入）的列表，以在建立交易时使用，确保你每次花费门罗币时都有一个好的人群可以隐藏。 
    * 这些诱饵是 [环形签名](/knowledge/ring-signatures)的一部分，是门罗币对链上隐私的一个重要部分。

## 使用门罗币最私密和安全的方式是什么？

即使在使用远程节点时，门罗币提供的强大的链上隐私，最好的办法是运行你自己的门罗币节点，以确保你有一个原始的门罗币区块链副本在手，并且你的IP地址得到很好的保护。运行自己的节点的另一个好处是，你可以回馈网络，让其他节点从你的节点同步，甚至让其他用户用他们的钱包连接到你的节点。

也就是说，在使用远程节点时，门罗币确实仍然提供很好的隐私。如果你对运行你自己的门罗币节点感兴趣，这里有一个易于遵循的指南：

  * [运行门罗币节点](https://sethforprivacy.com/guides/run-a-monero-node/)

## 远程节点可以了解什么情况？

当使用远程节点时，有几个关键的信息会暴露给远程节点，以及该节点可以攻击你、阻止你进行交易等几个关键方式。

远程节点可以了解到的第一件事是你的公共IP地址。虽然这将有望通过VPN或Tor隐藏起来，但远程节点可以将你的公共IP地址与交易联系起来，帮助他们缩小你的交易地点。远程节点还可以了解你的钱包最后同步的区块，并利用这一点试图对你进行有根据的猜测，比如你通常什么时候使用门罗币，以及你最后一次花费门罗币是什么时候。如果你总是从同一个IP地址（如你的家）来，这一点尤其正确。远程节点可以了解到的关于你的最后一件关键事情是关于你通过它发送的交易的基本信息。虽然这可能是远程节点操作员获得的关于你的最明显的数据，但重要的是要明白，当把这些信息与其他链外数据结合起来时，这可能被用来帮助追踪交易的发件人。如果远程节点由恶意实体、区块链分析公司或压迫性国家运行，这可能特别危险。

一个远程节点也可以试图通过向你隐藏区块来给你带来麻烦，使你的钱包认为它是同步的，但实际上它并不是。这可以使你认为资金丢失或阻止你花费资金，直到你连接到另一个节点。一个远程节点可能做的最后一件事是给你的钱包提供一个被操纵的诱饵列表。这可能导致你的钱包完全无法建立交易（使你无法花费资金），或者允许远程节点尝试提供它知道已经花费的诱饵，以减少你在每笔交易中获得的匿名性。

## 在使用远程节点时，仍然存在哪些隐私保障？

虽然这篇文章可能让你有点害怕，但重要的是要意识到，即使使用远程节点，门罗币提供的隐私也是非常好的，以这种方式使用时，远远超过任何其他加密货币。你仍然获得了门罗币提供的强大的链上隐私，因为远程节点永远不知道真正的输入（你花了什么币），交易中花费的门罗币数量，或交易接收者的地址。外部观察者也无法看到真正的输入、金额或涉及的地址（无论你选择使用哪种类型的节点！），确保在远程节点之外，甚至你的IP地址、钱包同步信息和交易都有强大的隐私保证。

远程节点也永远无法获得你之前发送或接收的交易，或者你钱包中当前的门罗币数量，并且在你开始使用另一个节点的时候，会失去对你交易的所有可见性。没有任何私人密钥（无论是花费还是查看密钥）被提供给远程节点，因此你的钱包仍然是私人的，安全的，可用的。不管是哪个远程节点，你也永远不会有丢失门罗币或被盗的风险，因为该节点不能编辑收件人地址，永远无法访问你的钱包私钥，也不能以任何方式没收你的门罗币。

## 像MyMonero类型 "轻型钱包"如何？

虽然这个话题有点超出本文的范围，但我确实想谈谈门罗币中一种独特的钱包类型——轻型钱包。轻型钱包的名字来自于这样一个事实：你的钱包（在你的手机或电脑上）不必执行任何区块链同步，使体验更快、更流畅。

然而，像这样的钱包目前有一个严重的隐私权衡 —— 你的钱包将私人查看密钥发送到你使用的远程服务器（如MyMonero中的默认），让远程服务器完全看到自你的钱包创建以来收到的任何资金（以及直到你停止使用该钱包或种子）。这确实大大减少你从节点操作员那里得到的隐私，应该谨慎对待。

值得庆幸的是，门罗币社区正在努力改进软件，你可以用它来托管你自己的轻型钱包服务器（LWS），这将允许你有快速的同步，而无需信任第三方与你的私人查看密钥 —— 因为你将运行你的钱包发送私人查看密钥的软件！

关于定制的轻型钱包服务器的更多信息，请看下面的Github仓库：

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## 我如何能了解更多？

如果你很好奇，想更好地了解门罗币的节点，并研究使用远程节点或运行自己的节点，请看下面的链接，以了解开始的好地方：

  * [MoneroWorld，一个可以使用的社区运行的远程节点列表](https://moneroworld.com/#nodes)
  * [本文作者Seth For Privacy所运行的门罗币节点](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail，一个经常检查状态的远程节点列表](https://monero.fail/)
  * [如何在GUI钱包内连接到一个远程节点](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia —— 远程节点](https://www.getmonero.org/resources/moneropedia/remote-node.html)

进一步阅读

  * [门罗币如何独特地实现循环经济](/knowledge/monero-circular-economies/)

  * [门罗币环形签名与CoinJoin像在Wasabi比较](/knowledge/ring-signatures-vs-coinjoin/)

  * [为什么（以及如何！）你应该持有你自己的钥匙](/knowledge/hold-your-keys/)

  * [贡献为门罗币](/knowledge/contributing-to-monero/)

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

  * [门罗币是如何解决困扰比特币的区块大小的扩容问题](/knowledge/dynamic-block-size/)

  * [ 新的CLSAG环签名技术将如何提高门罗币的效率](/knowledge/what-is-clsag/)

  * [为什么门罗币拥有尾部增发的特性](/knowledge/monero-tail-emission/)

  * [门罗币的前世今生](/knowledge/monero-history/)

  * [Wired杂志是如何误解了门罗](/knowledge/wired-article-debunked/)

  * [流言终结者：关于门罗币的15大传言和疑虑](/knowledge/monero-myths-debunked/)

  * [Dandelion ++蒲公英改进协议如何使Monero从源头得到更强防护](/knowledge/monero-dandelion/)

  * [为什么门罗币是开源且去中心化的](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [门罗币挖矿: 什么使 RandomX 算法如此特别](/knowledge/monero-mining-randomx/)

  * [为什么门罗币优于达世币, 大零币, 小零币 , 古灵币以及经过Wasabi级别混币器混淆后的比特币 (更新于2020年五月)](/knowledge/why-monero-is-better/)