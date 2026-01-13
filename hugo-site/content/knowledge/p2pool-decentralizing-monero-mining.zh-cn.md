---
title: "P2Pool和它在去Monero采矿中心化的作用"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero项目的核心目标之一是通过对工作证明的新的和创新的方法来实现一个公平、分散和安全的网络，这是当今加密货币网络的主要安全方式。

虽然 [像RandomX](/knowledge/monero-mining-randomx) 这样独特的挖矿算法对这一目标极为重要，因为它有助于确保任何拥有计算机的人都能为网络的安全做出合理的贡献，但RandomX并不能解决由于矿池可能出现的问题。 矿池是目前最常见的加密货币挖矿方式，包括Monero，但值得庆幸的是，p2pool挖矿的出现正在迅速改变这种状况。

## 什么是矿池采矿？

矿池是矿工分担试图解决网络上的区块的任务，然后平均分享池子里找到的所有区块的奖励的一种方式。 虽然这极大地有助于平衡矿工获得报酬的频率与单独开采Monero的频率，但也不是没有严重的中心化问题。

当每个矿工向矿池贡献工作时，他们放弃了对他们所做的任何工作和发现的区块的控制权，相信矿池会根据每个人所做的工作的数量，在所有矿工之间诚实和公平地分享奖励。 如果一切顺利，矿池运营商会收集所有矿工的工作，提交给网络，并平均分享奖励。

## 矿池采矿的问题是什么？

不幸的是，这完全依赖于信任，并允许矿池运营商对矿工所做的工作做一些不正当的事情。矿池运营商可以利用正在进行的工作来攻击网络，试图重复花费资金（如果矿池足够大的话），或者干脆利用矿工正在进行的工作来支付自己，而从不适当奖励矿工的工作。

对网络来说，最大的风险是一个池（或多个池在一起）在其控制下拥有超过51%的网络算力，因为他们可以利用这一点作弊并花费两次资金（双重消费攻击）或试图改变网络的规则。

## p2pool 是什么?

p2pool是一个概念，最初是在2011年为开采比特币而创建的，但从来没有看到广泛的采用，在比特币上几乎没有使用。值得庆幸的是，RandomX背后的关键开发人员之一，SChernykh，用他的假期想出了解决比特币实现p2pool的一些问题，并从头开始重写了所有的软件。

Monero中的p2pool允许矿工以完全无信任的方式合作解决区块，并通过使用p2pool的特殊节点软件来确保Monero网络的安全，以便分享工作。

这是通过一个新的区块链 (a "side-chain") 来完成的，它记录了每个矿工所做的工作，他们的钱包地址，以及他们赚了多少Monero，然后以一种无信任和去中心化的方式支付奖励。由于这个侧链的矿工人数少得多，在它上面寻找和提交区块要比在Monero主网络上容易得多，这使得矿工比单独挖Monero更容易获得稳定的报酬。

## p2pool是如何解决矿池采矿的问题？

在p2pool中，没有中心化的矿池，没有中心化的矿池运营商，也没有一个人掌握着资金和分配报酬。所有通过p2pool挖矿的人集体进行的工作都由p2pool区块链和其他节点运营商检查，以确保其合法性，当发现一个区块时，所有矿工都会根据他们所做的工作直接从该发现的区块中的奖励中获得报酬。

当矿工选择使用p2pool而不是集中式矿池时，他们从矿池运营商那里移走了所有的权力和信任，并确保他们的工作有助于网络的利益和他们自己的奖励，减少网络攻击、滥用他们的工作或盗窃他们应得的奖励的风险。

这不仅有助于他们保护自己的利益，也减少了集中式资金池对整个Monero网络构成的风险。p2pool的使用也大大有助于减少民族国家或监管机构可能对网络健康构成的风险，因为没有集中式资金池运营商可以施压，没有资金池的地理集中可以依靠，也没有任何其他容易让他们用来对付Monero的压力点。

## 有什么弊端？

值得庆幸的是，Monero中的p2pool已经被设计得很好，而且功能非常棒! 然而，p2pool挖矿的主要缺点是，每个想使用p2pool的矿工都要运行自己的Monero节点，导致开始的过程比较麻烦。不过，这个节点随后被用来计算构建和检查区块所需的所有信息，并确保矿工完全控制他们正在进行的工作。该节点还可以作为矿工自己钱包的远程节点，为网络做出贡献，以及更多利益。

与集中式挖矿的另一个关键区别是，使用p2pool的小矿工将比大型集中式矿池有更多的 "差异", 或两次支付之间的时间间隔， 但 _极其_ 重要的是，这不会导致长期赚取更少的Monero！p2pool甚至会像集中式矿池一样长期为小矿工提供利润。这种差异的一部分也被p2pool本身的0%费用所抵消，因为没有集中式矿池运营商需要为他们的服务支付费用!

## 我怎样能开始呢？

值得庆幸的是，由于Monero的p2pool实现的出色设计，以及社区中许多人投入时间帮助简化通过p2pool挖矿的过程，随着时间的推移，开始变得越来越简单。有几种方法可以开始使用p2pool挖矿，但由于技术细节超出本文的范围，请根据您的操作系统，随时跳转到下面的链接：

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## 我怎样能了解更多？

如果这已经激起了你对p2pool挖矿的好奇心，请看下面一些关于p2pool的额外链接和解释，它是如何工作的，以及它对Monero意味着什么：

  * [The official Github for p2pool](https://github.com/SChernykh/p2pool)
  * [The official docs on using p2pool](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool is now live](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, a "block explorer" of sorts for p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh: On his development of P2Pool a Decentralized XMR Mining Pool](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

进一步阅读