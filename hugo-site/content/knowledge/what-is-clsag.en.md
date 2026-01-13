---
title: "How CLSAG Will Improve Monero's Efficiency"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
As a protocol, Monero is currently in a constant state of innovation. Utilizing research in both on-chain and off-chain solutions, the Monero community looks for areas to improve to make Monero more private, more scaleable, and more accessible to all. One of the more recent innovations is the replacement of the linkable ring signature scheme, MLSAG, with a drop-in replacement CLSAG, which stands for Concise Linkable Spontaneous Anonymous Group.

On the surface level, the implementation of CLSAG will decrease the most common 2 input, 2 output transactions by 25%. We’ll also see a 10% decrease in verification time.

But what exactly is CLSAG? What does it do, and how does it differ from the old version, MLSAG? Let’s take a minute to remind ourselves of the why and how of ring signatures so we can better understand this concept. Ring signatures allow for non-interactive, witness indistinguishable inputs by use of signer-selected anonymity sets of previous outputs. In laymen’s terms, it allows a user to hide their outputs used in a transaction alongside unrelated outputs, and they can do all of this without needing anyone else to take part. All you need is a copy of the blockchain. Each of these outputs mostly appear to be equally probable of being the actual one being sent, thereby hiding metadata about the sender.

This begets a bit of a problem, however. What if a user was to construct a ring signature with all decoy outputs? How would anyone know that the unknown sender doesn't have the authority to send any of them? Would this user be able to spend fake money? The answer is no. The ring signature includes a method for proving that at least one of the outputs is owned by the unknown sender, without revealing which one it is. In fact, both CLSAG and MLSAG (henceforth known as the SAGs) are the part of the ring signature that proves this. Interestingly, at the same time, it proves that the amount of the transaction, though hidden behind confidential transactions (RingCT), balances. That the SAGs prove two things, that one output is owned by someone in the ring, and that the transaction balances, is important, and actually where the size and verification savings lies. If this is getting confusing, don't worry, we'll get to a fun, and easy-to-understand analogy soon.

The old signature scheme, MLSAG (Multilayered Linkable Spontaneous Anonymous Group) proves the aforementioned two things in a ring signature, but it does each separately. The use of separate computations for signing and commitment keys means slower operations. A modern computer can do these computations in a matter of milliseconds, which doesn’t seem like much, and indeed, for one transaction it’s not. But when we consider the sheer number of transactions on the Monero blockchain, and that a node syncing from scratch will have to download and verify each of them, the bytes and milliseconds start to pile up quickly.

CLSAG combines the maths necessary to prove both into one, as well as computes both of them at once, and it does so in a safe manner. What does this mean in a safe manner? Well, to clear this up, as well as hopefully make the whole thing make more sense, let’s explore that promised fun analogy.

Let's say you need to go to both the grocery store and the hardware store, to pick up two different things: food and toxic cleaning chemicals. You don’t want them to intermix, as if there is an accident, the chemicals will spill on the food, making them inedible. You decide to be super safe and drive from your house to the grocery store, buy the food, and then drive back to your house. Only after you have unloaded the food do you get back in the car, drive to the hardware store, and back to your house with the chemicals. You’ve taken two separate trips to ensure the safety of all purchases. Though it is indeed safe, it is inefficient. This represents MLSAG, where two different sets of maths are stored and two different ‘trips’ are made to compute them.

You decide you want a faster way to do this, however. It’s too much wasted time. Sure doing it once or twice isn’t going to steal your life away, but having to do this over and over, the hours begin to add up. You start to wonder if you can make one trip instead. From your house, to the grocery store, to the hardware store, and back home. You can’t just go and throw everything in your car haphazardly. It’s not safe. Instead, you designate different spots in your car for different things, and make sure everything fits neatly in its place. In so doing, you’re able to safely make one trip to both stores, and keep things away from each other. This represents CLSAG. There is now only one set of math stored in this transaction to prove these two things, and it’s done in away that they don’t interfere with each other. A trip has to still be made, but you’ve reduced the number of them quite drastically.

All of this sounds quite exciting. Is it possible we can find other shortcuts, or other ways to save on time and space? The answer is yes and no. According to current MRL researchers, it's likely not possible to further modify the SAG-type constructions for better size or speed; however other constructions like Arcturus, Omniring, RCT3, or Triptych produce much better size scaling and verification benefits using different mathematical methods. However, each of these 'next-gen' approaches to signer-ambiguous protocols comes with its own tradeoffs in implementation details, and are undergoing active research and investigation.

After all, Monero is always innovating.

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

  * [How Monero Stealth Addresses Protect Your Identity](/knowledge/monero-stealth-addresses)/

  * [How Monero Subaddresses Prevent Identity Linking](/knowledge/monero-subaddresses)/

  * [Monero Outputs Explained](/knowledge/monero-outputs)/

  * [Monero Best Practices for Beginners](/knowledge/monero-best-practices)/

  * [How Ring Signatures Obscure Monero's Outputs](/knowledge/ring-signatures)/

  * [How Monero Solved the Block Size Problem That Plagues Bitcoin](/knowledge/dynamic-block-size)/

  * [Why Monero Has a Tail Emission](/knowledge/monero-tail-emission)/

  * [A Brief History of Monero](/knowledge/monero-history)/

  * [Wired Magazine Is Wrong About Monero, Here's Why](/knowledge/wired-article-debunked)/

  * [Top 15 Monero Myths and Concerns Debunked](/knowledge/monero-myths-debunked)/

  * [How Dandelion++ Keeps Monero's Transaction Origins Private](/knowledge/monero-dandelion)/

  * [Why Monero Is Open Source and Decentralized](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: What Makes RandomX So Special](/knowledge/monero-mining-randomx)/

  * [Why Monero Is Better Than Dash, Zcash, Zcoin (Even With Lelantus), Grin and Bitcoin Mixers Like Wasabi (Updated May 2020)](/knowledge/why-monero-is-better)/

Further reading