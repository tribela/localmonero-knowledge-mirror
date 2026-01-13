---
title: "How RingCT Hides Monero Transaction Amounts"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero’s privacy does not depend on one singular mechanism that, if broken, would reveal the entirety of transactions, but rather three different technologies that work in tandem to provide holistic privacy while compensating for the weaknesses of the other parts. This three-prong approach consists of [ring signatures](/knowledge/ring-signatures), RingCT, and [stealth addresses](/knowledge/monero-stealth-addresses). These three technologies hide the real output (sender), amount, and receiver respectively. Today we’ll be talking about RingCT.

RingCT is arguably the most technical of the three, and can be difficult to understand, so we won’t be covering how it works exactly, but rather showing how it is possible to not know an amount and still confirm things about it. And don’t worry, we’ll use plenty of examples as always.

First, let’s explore why it’s important to verify anything about the amounts. Why can’t we just keep them completely secret? The answer is, there are clever ways that people can create money from thin air if given the opportunity. How might something like this work? Let’s look at an example.

If you want to purchase an item from your friend, and he wants ten dollars for it, then you start with ten dollars and he starts with zero. After you give him the ten dollars, he has ten dollars and you have zero. You started with ten, and now he has ten. No money was created or destroyed in this transaction.

With cryptocurrencies, a clever individual can give ten dollars for the item and instead of receiving zero dollars in change, they can receive two dollars back. Instead of 0 and 10 leading to 10 and 0 (or 10=10), it’s now 0 and 10 leads to 10 and 2 (or 10=12). Two Monero was just created out of thin air. You can imagine that if the individual was to do this to themselves several times, they would be able to amass a gigantic fortune in short order.

With Bitcoin and others, this would be easy to see. You look at the inputs going into a transactions and the outputs coming out and make sure that what is sent equals what is received. If these amounts were encrypted and not visible then a user has no way of verifying that what is sent and what is received is the same.

In an attempt to increase Bitcoin privacy, Gregory Maxwell created Confidential Transactions (CT), a new technology that would allow for encrypted amounts, while proving that nothing was created or destroyed in the process. As with most privacy technology, it did not make it into Bitcoin, but Monero was keen on adopting it. There was just one problem. The already implemented technology of ring signatures was incompatible with the proposed idea. So, one of the MRL researchers at the time, Shen Noether, modified CT into RingCT, a version of CT that was compatible with ring signatures.

Once again, the way this works is quite technical, and would be difficult to explain in an introductory article. For the cryptography enthusiast who simply must know, there are plenty of in-depth articles written on the internet about the inner workings of CT. For the rest of us, this article will show how it might be possible to hide the amounts, but still prove that nothing was created or destroyed.

Let’s say Alice wanted to send Bob money. Alice will send 10 XMR to Bob, who will receive 10 XMR. 10=10 so nothing is wrong here. But Alice doesn’t want anyone to know how much she is sending. So she and Bob create a shared secret. Basically a number that only the two of them know. Let’s say that number is 22. Now, Alice multiplies 10 (what she is really sending) by 22 to get 220. This is the number she shares with the network.

The miners themselves don't know the secret number. If they did, they could divide the number they are shown by the secret number and get the real amount sent. But since they don’t, they can’t. They do see that Bob will receive 220 though. 220 sent. 220 received. 220 = 220. In this way, the network can verify that no Monero was created or destroyed, all without knowing the real amount that Alice sent Bob.

Since Bob knows the shared secret number, when he receives the money, he just divides by 22 to get the real amount that Alice sent, 10. Alice and Bob both know how much was sent and how much was received, all while everyone else is given a false number.

Once again, this is not the actual way in which CT works, but it gives an idea of how something like this might be possible. The real way involves things like Pedersen commitments, two sent amounts (one encrypted amount to the receiver and one commitment amount to the network), and…yeah, it’s already easy to see how one could get lost in all that.

One thing to note however, is that while RingCT does hide the amount transacted between two parties in a transaction, it does not hide two other sets of numbers.

The first is the coinbase transactions. If this term is unfamiliar to you, it basically means the reward that miners get for finding the next block. This number is not hidden. Anyone can see how much the protocol has awarded a miner for their service. In this way, the current amount of Monero in existence can be known by adding up all of the coinbase transactions. Their sum will equal the current Monero in circulation.

The second number not hidden is the fee paid to the miners when a user sends a transaction. The fees have to be in the clear so miners can know who to prioritize. This is a way that users can hurt their privacy however, as if someone uses a unique miner fee each time they send a transaction (like 0.12345), then their transactions can be linked.

Other than these cases, RingCT has been hiding Monero amounts since 2017, and our collective privacy is all the stronger for it.

Further reading

  * [How Monero Uniquely Enables Circular Economies](/knowledge/monero-circular-economies)/

  * [Monero’s Ring Signatures vs CoinJoin Like in Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Why (And How!) You Should Hold Your Own Keys](/knowledge/hold-your-keys)/

  * [Contributing Back to Monero](/knowledge/contributing-to-monero)/

  * [How Remote Nodes Impact Monero’s Privacy](/knowledge/remote-nodes-privacy)/

  * [How Monero Uses Hard-Forks to Upgrade the Network](/knowledge/network-upgrades)/

  * [View Tags: How One Byte Will Reduce Monero Wallet Sync Times by 40%+](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool and Its Role in Decentralizing Monero Mining](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: What It Will Do for Monero](/knowledge/seraphis-for-monero)/

  * [Is Converting Bitcoin to Monero Just as Private as Buying Monero Directly?](/knowledge/most-private-way-to-buy-monero)/

  * [Why Monero Uses a Trustless Setup Unlike Zcash](/knowledge/monero-trustless-setup)/

  * [Why Monero Is a Better Store of Value Than Bitcoin](/knowledge/monero-better-store-of-value)/

  * [How Monero Can Overcome Bitcoin's Network Effects](/knowledge/network-effect)/

  * [Why Monero Has the Most Critical Thinking Community](/knowledge/critical-thinking)/

  * [Scams to Look Out for When Using Monero](/knowledge/monero-scams)/

  * [How Atomic Swaps Will Work in Monero](/knowledge/monero-atomic-swaps)/

  * [What Every Monero User Needs to Know When It Comes to Networking](/knowledge/monero-networking)/

  * [How Monero Stealth Addresses Protect Your Identity](/knowledge/monero-stealth-addresses)/

  * [How Monero Subaddresses Prevent Identity Linking](/knowledge/monero-subaddresses)/

  * [Monero Outputs Explained](/knowledge/monero-outputs)/

  * [Monero Best Practices for Beginners](/knowledge/monero-best-practices)/

  * [How Ring Signatures Obscure Monero's Outputs](/knowledge/ring-signatures)/

  * [How Monero Solved the Block Size Problem That Plagues Bitcoin](/knowledge/dynamic-block-size)/

  * [How CLSAG Will Improve Monero's Efficiency](/knowledge/what-is-clsag)/

  * [Why Monero Has a Tail Emission](/knowledge/monero-tail-emission)/

  * [A Brief History of Monero](/knowledge/monero-history)/

  * [Wired Magazine Is Wrong About Monero, Here's Why](/knowledge/wired-article-debunked)/

  * [Top 15 Monero Myths and Concerns Debunked](/knowledge/monero-myths-debunked)/

  * [How Dandelion++ Keeps Monero's Transaction Origins Private](/knowledge/monero-dandelion)/

  * [Why Monero Is Open Source and Decentralized](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: What Makes RandomX So Special](/knowledge/monero-mining-randomx)/

  * [Why Monero Is Better Than Dash, Zcash, Zcoin (Even With Lelantus), Grin and Bitcoin Mixers Like Wasabi (Updated May 2020)](/knowledge/why-monero-is-better)/

Further reading