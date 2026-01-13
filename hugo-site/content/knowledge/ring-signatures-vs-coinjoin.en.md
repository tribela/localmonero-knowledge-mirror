---
title: "Monero’s Ring Signatures vs CoinJoin Like in Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
As Bitcoin’s privacy tools have gained more attention and usage, they have come under more regulatory scrutiny. This scrutiny has led to a [recent announcement](https://twitter.com/wasabiwallet/status/1503091503207432193) by a Bitcoin privacy tool, Wasabi Wallet, that they will start to censor and reject incoming inputs to mixes that they deem illicit or against their ToS, and will pay a chain analysis company to “vet” incoming mix participants.

The use of CoinJoin transactions to obfuscate the source of funds in Bitcoin has been the core of Bitcoin privacy for many years now, and the issues and risks inherent in it’s use are some of the core issues that Monero’s ring signatures correct and prevent.

In this blog post we’ll briefly dive into a comparison of CoinJoin and ring signatures, as well as why the approach taken in Monero leads to greater censorship-resistance, greater privacy, and less hassle for users.

## What is a CoinJoin transaction?

As all transactions are completely transparent in Bitcoin - revealing the sender, receiver, and amounts - users must take extra steps to preserve their privacy from previous senders and future recipients of their funds or risk censorship, surveillance, or theft of funds via physical violence.

The best solution today for privacy on Bitcoin is a tool called [“CoinJoin”](https://bitcoiner.guide/qna/coinjoin/), where 2 or more users work together (usually via a centralized coordinator) to create a special transaction that makes it difficult for outside observers to connect the inputs with the outputs. Each participant communicates to jointly build the transaction without giving over custody of their funds, and receives an output at the end whose previous history is now unclear (or obfuscated) to outside observers.

This breaks the history of specific UTXOs, allowing Bitcoin users to gain some modicum of forward-secrecy when transacting. However, CoinJoin (as implemented in Wasabi Wallet and Samourai Wallet, the two most-used CoinJoin tools for Bitcoin) has a few major drawbacks:

  * As CoinJoin transactions are completely opt-in and requires active participation, any participant necessarily shows that they seek greater privacy than that of “normal” Bitcoin users, potentially singling them out and causing issues spending funds at many regulated exchanges or entities. Each user cannot deny that they participated in a CoinJoin transaction.
  * In order to find other’s to CoinJoin with, most approaches to CoinJoin (including Wasabi Wallet) use a centralized coordinator that connects participants and helps them communicate and build a proper CoinJoin transaction. This centralized coordinator never has custody of user’s funds, but does gain extensive insight into the transactions they coordinate, can censor incoming inputs (as in the case of Wasabi Wallet), and can be pressured into collecting or sharing information about CoinJoin participants.
  * User’s with large amounts of funds to CoinJoin can often have to wait hours (or even days!) to find enough participants to CoinJoin with, leading to large delays from the time a user receives funds to when they can spend them privately.
  * The privacy provided by a CoinJoin transaction degrades over time as other participants spend funds or link their outputs to their identity through KYC exchanges, ID requiring merchants, etc. This means that users ideally keep their funds constantly churning in CoinJoin transactions to keep their anonymity set (“crowd to hide in”) as fresh as possible.
  * In most approaches to CoinJoin, participants must use a fixed-size UTXO (i.e. 0.1 BTC) in order to make it harder to connect inputs and outputs of CoinJoin transactions. This leads to higher fees (more separate transactions necessary per large input), more “toxic change” (funds that are unspendable without serious risks to privacy), and can proclude smaller users from being able to mix at all if they don’t have the minimum balance required.

## How do ring signatures solve these issues?

As [we have looked deeply into what ring signatures are in the past](/knowledge/ring-signatures), I won’t go into great detail on the technical aspects of how they work in this blog post. Instead, we’ll look at how the approaches taken in Monero solve the issues with CoinJoin discusses above.

> CoinJoin is opt-in and requires participation

CoinJoin is opt-in and requires participation

Monero’s ring signatures are a core feature of the privacy protocol, and _every_ transaction on the network uses them. This means that no user’s transactions stand out for seeking greater privacy than “normal” Monero users, and all users gain plausible deniability that they spent funds in any given transaction. As a user spending funds does not coordinate or participate with the decoy inputs in a transaction, those users who own inputs that happen to be selected as decoys can honestly say they were not participating in that transaction, strengthening their privacy.

> Use of a centralized coordinator

Use of a centralized coordinator

As Monero’s ring signatures are entirely non-coordinated and require only the true spender of funds to create the transaction, there is no need for a centralized coordinator in Monero. This ensures that _no one_ can deny you access to privacy in Monero, and there is no centralized entity that can be pressured, no easy Sybil attacks on liquidity, etc. As long as your transaction pays the proper fees, you gain uncensorable access to privacy, security, and anonymity in Monero.

> CoinJoin requires liquidity

CoinJoin requires liquidity

The “liquidity” available to anyone spending Monero to use as decoys is always the total set of outputs on-chain so there is never a shortage of decoys to hide in with Monero. Someone seeking to spend Monero can do so ~20min after receiving funds, and does not need to perform any additional steps to gain strong privacy in Monero.

> CoinJoin privacy degrades over time

CoinJoin privacy degrades over time

As Monero’s outputs are never known-spent by the network, the privacy provided by ring signatures is much less susceptible to degradation over time. A user does not need to constantly churn outputs in Monero, and outside of extremely rare circumstances, loses no privacy as time goes on.

If a user does want to “refresh” the decoys used with an output, however, they can merely send the funds back to themselves and be able to spend them ~20min later as usual.

> CoinJoin usually requires fixed-size inputs

CoinJoin usually requires fixed-size inputs

As amounts are hidden in every transaction using [“Confidential Transactions”](/knowledge/monero-ringct) (a part of “RingCT”), the decoys used in any given transaction can be of any size. There is no reason to need to be worried about amount-based heuristics in Monero, and so transactions are much simpler to build and can leverage decoys from any point in time and of any amount on the Monero blockchain.

## How can I learn more?

If you’re curious and want to better understand ring signatures or CoinJoin transactions, see the links below for great places to get started:

  * [How Ring Signatures Obscure Monero’s Outputs](/knowledge/ring-signatures)
  * [Ring Signature - Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [CoinJoin Overview](https://6102bitcoin.com/coinjoin-overview/)

Further reading

  * [How Monero Uniquely Enables Circular Economies](/knowledge/monero-circular-economies/)

  * [Why (And How!) You Should Hold Your Own Keys](/knowledge/hold-your-keys/)

  * [Contributing Back to Monero](/knowledge/contributing-to-monero/)

  * [How Remote Nodes Impact Monero’s Privacy](/knowledge/remote-nodes-privacy/)

  * [How Monero Uses Hard-Forks to Upgrade the Network](/knowledge/network-upgrades/)

  * [View Tags: How One Byte Will Reduce Monero Wallet Sync Times by 40%+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool and Its Role in Decentralizing Monero Mining](/knowledge/p2pool-decentralizing-monero-mining/)

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