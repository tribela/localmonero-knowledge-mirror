---
title: "P2Pool and Its Role in Decentralizing Monero Mining"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
One of the core aims in the Monero project is to enable a fair, decentralized, and secure network through new and innovative approaches to proof-of-work (PoW) mining, the main way that cryptocurrency networks are secured today.

While a unique mining algorithm [like RandomX](/knowledge/monero-mining-randomx) is extremely important to this aim as it helps to ensure that anyone with a computer can contribute a fair amount to the security of the network, RandomX does not solve the issues that can occur due to pool mining. Pool mining is by far the most common way to mine cryptocurrencies today, including Monero, but thankfully the emergence of p2pool mining is rapidly changing that.

## What is pool mining?

Pool mining is a way for miners to share the task of attempting to solve a block on the network and then share the rewards evenly for all blocks that the pool finds. While this helps immensely to even out the frequency with which miners are paid versus mining Monero alone, it's not without serious centralization issues.

As each miner contributes work to the pool, they give up control of any work they do and blocks that they find to the pool itself, trusting that the pool will honestly and fairly share the rewards among all miners based on the amount of work each has done. If all goes well, the pool operator collects the work from all miners, submits it to the network, and shares the rewards equally.

## What is the problem with pool mining?

Unfortunately, this relies entirely on trust and allows the pool operator to do nefarious things with the work being done by miners. The pool operator could use the work being done to attack the network, attempt to double-spend funds (if the pool is large enough), or simply use the work being done by the miners to pay themselves and never reward miners properly for their work.

The biggest risk to the network is that of a pool (or multiple pools working together) having greater than 51% of the networks hashrate under their control, as they could use this to cheat and spend funds twice (a double-spend attack) or attempt to change the rules of the network.

## What is p2pool?

p2pool is a concept that was originally created for mining Bitcoin back in 2011, but never saw broad adoption and remains practically unused on Bitcoin. Thankfully, one of the key developers behind RandomX, SChernykh, spent his vacation coming up with solutions to some of the issues with the Bitcoin implementation of p2pool and re-writing all of the software from scratch.

p2pool in Monero allows for a completely trust-less way for miners to work together to solve blocks and secure the Monero network by using special node software for p2pool in order to share the work.

This is done using a new blockchain (a "side-chain") that keeps a record of the work each miner performs, their wallet address, and how much Monero they have earned, and then pays the reward out in a trust-less and decentralized way. As this side-chain has far fewer miners, it's much easier to find and submit blocks on it than on the main Monero network, making it easier for miners to get consistent pay outs versus mining Monero alone.

## How does p2pool solve the problems of pool mining?

In p2pool, there is no centralized pool, centralized pool operator, or single person holding onto funds and distributing payouts. All of the work being collectively done by those mining via p2pool is checked by the p2pool blockchain and other node operators to ensure that it is legitimate, and all miners are paid out according to the work they have done immediately when a block is found directly from the rewards in that found block.

When miners choose to use p2pool instead of a centralized pool, they remove all power and trust from pool operators and ensure that their work contributes to the good of the network and to their own rewards, reduce the risk of network attacks, misuse of their work, or theft of rewards that they are owed.

Not only does this help them protect their own interests, it reduces the risk that centralized pools can pose to the Monero network as a whole. p2pool usage also helps immensely to reduce the risk that nation-states or regulators could pose to the health of the network, as there are no centralized pool operators to pressure, no geographical concentration of pools to lean on, or any other easy point of pressure for them to use against Monero.

## What are the drawbacks?

Thankfully p2pool in Monero has been well-designed and well-built, and functions extremely well! However, the main drawback of p2pool mining is that each miner who wants to use p2pool has to run their own Monero node, causing the process of getting started to be a bit more involved. However, this node is then used to calculate all of the information necessary for building and checking blocks, and ensures that the miner is in complete control of their work being done. The node can also function as a remote node for the miners own wallet, contributes to the network, and much more.

The other key difference from centralized mining is that small miners using p2pool will have a bit more "variance", or time between payouts, than a large centralized pool -- but it's _extremely_ important to note that this will not lead to earning less Monero over time! p2pool will be just as profitable for even small miners over time as centralized pools. Some of this variance is also offset by p2pool natively having 0% fees, as there is no centralized pool operator to pay for their services!

## How can I get started?

Thankfully, due to the excellent design of Monero's p2pool implementation and the many people in the community who have put in time to help simplify the process of mining via p2pool, getting started is getting simpler over time. There are several ways to get started mining with p2pool, but as the technical details are beyond the scope of this article, feel free to jump into a link below depending on your operating system:

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## How can I learn more?

If this has piqued your curiosity around p2pool mining, take a look below for some additional links and explainers on p2pool, how it works, and what it means for Monero:

  * [The official Github for p2pool](https://github.com/SChernykh/p2pool)
  * [The official docs on using p2pool](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool is now live](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, a "block explorer" of sorts for p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh: On his development of P2Pool a Decentralized XMR Mining Pool](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

Further reading

  * [How Monero Uniquely Enables Circular Economies](/knowledge/monero-circular-economies/)

  * [Monero’s Ring Signatures vs CoinJoin Like in Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Why (And How!) You Should Hold Your Own Keys](/knowledge/hold-your-keys/)

  * [Contributing Back to Monero](/knowledge/contributing-to-monero/)

  * [How Remote Nodes Impact Monero’s Privacy](/knowledge/remote-nodes-privacy/)

  * [How Monero Uses Hard-Forks to Upgrade the Network](/knowledge/network-upgrades/)

  * [View Tags: How One Byte Will Reduce Monero Wallet Sync Times by 40%+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [Seraphis: What It Will Do for Monero](/knowledge/seraphis-for-monero/)

  * [Is Converting Bitcoin to Monero Just as Private as Buying Monero Directly?](/knowledge/most-private-way-to-buy-monero/)

  * [Why Monero Uses a Trustless Setup Unlike Zcash](/knowledge/monero-trustless-setup/)

  * [Why Monero Is a Better Store of Value Than Bitcoin](/knowledge/monero-better-store-of-value/)

  * [How Monero Can Overcome Bitcoin's Network Effects](/knowledge/network-effect/)

  * [Why Monero Has the Most Critical Thinking Community](/knowledge/critical-thinking/)

  * [Scams to Look Out for When Using Monero](/knowledge/monero-scams/)

  * [How Atomic Swaps Will Work in Monero](/knowledge/monero-atomic-swaps/)

  * [What Every Monero User Needs to Know When It Comes to Networking](/knowledge/monero-networking/)

  * [How RingCT Hides Monero Transaction Amounts](/knowledge/monero-ringct/)

  * [How Monero Stealth Addresses Protect Your Identity](/knowledge/monero-stealth-addresses/)

  * [How Monero Subaddresses Prevent Identity Linking](/knowledge/monero-subaddresses/)

  * [Monero Outputs Explained](/knowledge/monero-outputs/)

  * [Monero Best Practices for Beginners](/knowledge/monero-best-practices/)

  * [How Ring Signatures Obscure Monero's Outputs](/knowledge/ring-signatures/)

  * [How Monero Solved the Block Size Problem That Plagues Bitcoin](/knowledge/dynamic-block-size/)

  * [How CLSAG Will Improve Monero's Efficiency](/knowledge/what-is-clsag/)

  * [Why Monero Has a Tail Emission](/knowledge/monero-tail-emission/)

  * [A Brief History of Monero](/knowledge/monero-history/)

  * [Wired Magazine Is Wrong About Monero, Here's Why](/knowledge/wired-article-debunked/)

  * [Top 15 Monero Myths and Concerns Debunked](/knowledge/monero-myths-debunked/)

  * [How Dandelion++ Keeps Monero's Transaction Origins Private](/knowledge/monero-dandelion/)

  * [Why Monero Is Open Source and Decentralized](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: What Makes RandomX So Special](/knowledge/monero-mining-randomx/)

  * [Why Monero Is Better Than Dash, Zcash, Zcoin (Even With Lelantus), Grin and Bitcoin Mixers Like Wasabi (Updated May 2020)](/knowledge/why-monero-is-better/)