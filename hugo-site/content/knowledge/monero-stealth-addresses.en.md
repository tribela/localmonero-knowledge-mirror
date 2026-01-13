---
title: "How Monero Stealth Addresses Protect Your Identity"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero has implemented a three-prong approach to privacy. These technologies are [ring signatures](/knowledge/ring-signatures), which hide the true output (sender), RingCT which hides the amounts, and stealth addresses, which hides the receiver. Today, we will be discussing the last of these mentioned technologies: stealth addresses.

There are many reasons why an individual might want to hide who they are sending to. We must never let anyone try to convince us that all examples of this are unsavory behaviors. Things like sending to a unpopular political party, donating to charities, or supporting those that the culture deems 'cancelled' are all examples of where one might want to hide their spending behaviors for fear of repercussion, but are perfectly legitimate in nature.

On a transparent blockchain, the addresses where one sends their transactions to are visible to all. It's important to consider that if miners themselves disagree with where the money is going, they can choose not to mine it into a block, effectively censoring this transaction on a seemingly censorship resistant platform. The only way to make this, admittedly unlikely, censorship not possible is if miners can't distinguish between transactions because all on-chain metadata is obscured by various means. Something that Monero is known for.

Monero solves this problem of transparent addresses by implementing stealth addresses, a technology that was actually initially made for Bitcoin in 2011 by Bitcoin Talk forum user ByteCoin (the relation to Bytecoin, which would later integrate stealth addresses, is unknown). The current form of stealth addresses has several improvements over the initial idea however. But first, in order to see how they work, let's talk about keys.

It's hard to be in the cryptocurrency space and not hear about keys. Phrases like 'back up your private key' are common, but when an average Joe hears the words "public key" and "private key" they get scared and think it will be too technical and confusing to understand. But don't worry. We'll take it slow, and use plenty of examples.

The two kinds of keys used in cryptocurrencies are, as just mentioned, public and private. These two keys usually come in a pair, meaning that a particular public and private key are linked to one another. In fact, usually the public key is derived from the private one, meaning if you know the private key, your wallet can do some nifty math and come up with the correct public key every time.

Now, as the names imply, the public key can be public without consequence. Usually it's a part of the address that you share to receive money into your cryptocurrency wallet. Also following its namesake, the private key is one that should not be shared. It's the thing that allows you to sign and spend a transaction, so if it is stolen or shared, then the dastardly third party can spend your money, usually to themselves.

An easy analogy to this would be a padlock and the key needed to unlock it. The open padlock can be shared freely, and indeed anything can be locked up with this padlock, but only the person with the key is able to open anything the padlock is closed on. The padlock can be copied and shared, the key should not be.

These keys are usually abstracted away from the user, so you never really see them. In Monero, they don't appear as a scary alphanumeric string at all. In Monero, the common user knows the private key as their seed. The seed (that you should write down if you haven't), is actually just a human readable private key. 

See? Not so scary after all. Back to stealth addresses.

As mentioned before, stealth addresses weren't originally made for Monero, but Bitcoin. As with most fledgling ideas though, this first iteration had issues. The next attempt came when CryptoNote was created by Nicholas van Saberhagan for Bytecoin, the precursor to Monero ([see our history of Monero and Bytecoin here](/knowledge/monero-history)), and while it was a definite improvement over the original, even it had some subtle flaws.

Eventually, one last iteration came into being from a developer for another now-defunct, privacy cryptocurrency, which fixed the outstanding privacy and security issues with the idea. This eventually made its way into Monero, and is what is used today.

Although these privacy and security issues were solved, stealth addresses themselves added a different kind of quirk to blockchain technologies, one that didn’t exist before. The need to scan. Since receiving addresses are not publicly displayed on the blockchain, the receiver never knows if any given transaction is theirs, so they must scan every incoming transactions with their private key to see if it’s theirs.

With transparency coins, all they have to do is check to see if a transaction is sending to your address. An easy yes or no question. But with stealth addresses, every transaction could potentially be one that is being sent to you, so you have to try to unlock each one with your private key to see if it opens.

This is an extra step that Bitcoin and its derivatives do not have, and makes initial wallet setup, along with syncing a wallet when you haven’t opened it for a while, much longer than Bitcoin. The tradeoff is necessary though, to unlock the privacy guarantees it has. It should be noted that, unlike the weakest point of the privacy trifecta, ring signatures, stealth addresses is not susceptible to heuristics. It relies on tried and true elliptic curve cryptography, which the entire internet relies on, so breaking it would mean an end to computer security in general, not just Monero.

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

  * [How RingCT Hides Monero Transaction Amounts](/knowledge/monero-ringct)/

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