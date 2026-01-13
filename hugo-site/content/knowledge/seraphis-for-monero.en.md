---
title: "Seraphis: What It Will Do for Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: a modular design upgrade for Monero transactions

This post describes [Seraphis](https://github.com/UkoeHB/Seraphis), a set of transaction protocol structures and abstractions developed by pseudonymous research contributor [`koe`](https://github.com/UkoeHB) for the Monero ecosystem, and with ongoing security analysis by pseudonymous contributor [`coinstudent2048`](https://github.com/coinstudent2048).  
We make some simplifications and omit certain technical details for the sake of clarity; for this reason, and because the design of Seraphis is still in progress, interested readers should refer to Seraphis documentation for the most up-to-date information.

## Transactions in Monero

Protocols like Bitcoin and Monero and others rely on a so-called "output model" of operation, where an _output_ is a representation of value that can be transferred.  
Transactions consume one or more outputs controlled by a sender, and generate new outputs directed toward recipients (or back to the sender as change); the transaction must balance in that consumed outputs must contain a total value exactly equal to the value in new outputs (plus a network-imposed fee).  
In many protocols like Bitcoin, the value contained in an output is written in the clear, as is the recipient.  
Furthermore, by looking at the blockchain, it is trivial to see if and when an output has been spent (that is, if it has been consumed in a later transaction, and which transaction spent it).

By contrast, protocols like Monero introduce a different design:

  * Output values are hidden and not visible on the blockchain
  * Recipient addresses are hidden by the use of a one-time addressing protocol
  * Whether or not an output has been spent is obscured by the use of ambiguous signatures

The result is that, absent external information, it is difficult to determine whether a given output has been spent, what its value is, and who its recipient is.

The current Monero transaction protocol is called _RingCT_ , and uses several cryptographic building blocks to achieve these design goals.

  * _Commitments_ hide amounts in a mathematically-useful way
  * _Range proofs_ prevent overflow that could inflate supply
  * _Linkable ring signatures_ provide signer ambiguity and prevent double-spend attempts
  * _Commitment offsets_ assert that transactions balance

These building blocks are carefully intertwined to build the RingCT protocol.

A useful property of the RingCT protocol is that some building blocks can be changed or upgraded in a way that keeps the overall design and properties intact, but that can provide efficiency or security improvements. In fact, these kinds of upgrades have occurred (or are planned to occur) several times in Monero's history. Range proofs in the original RingCT protocol were bulky and slow; they were later updated to a construction called [Bulletproofs](https://eprint.iacr.org/2017/1066) that made transactions smaller and faster with better security analysis, and are planned to be updated to a newer construction called [Bulletproofs+](https://eprint.iacr.org/2020/735) for even greater efficiency benefits.

A similar process was undergone with the linkable ring signature building block. In the original protocol, a construction called [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34) was used. This was later updated to a newer construction called [CLSAG](https://eprint.iacr.org/2019/654) that is faster, results in smaller transactions, and has better security analysis. An even newer linkable ring signature construction based on [Triptych](https://eprint.iacr.org/2020/018) was proposed, but this was not selected for deployment because of its impacts on multisignature operations.

## Seraphis

Seraphis takes this idea a step further.  
Rather than update individual building blocks of the existing RingCT transaction protocol, it introduces a different protocol that can take advantage of different building blocks and offer improved functionality.

## Building blocks

Seraphis uses a different set of cryptographic building blocks to achieve its design goals.

  * _Commitments_ still hide amounts
  * _Range proofs_ still prevent overflow and supply inflation
  * _Membership proofs_ provide signer ambiguity
  * _Commitment offsets_ still assert balance
  * _Authorizing proofs_ prevent double-spend attempts

Notice the change here: linkable ring signatures are replaced with a combination of membership proofs and authorizing proofs. Roughly speaking, membership proofs show that a consumed output is part of a larger set, similar to what happens in RingCT. But unlike RingCT, membership proofs don't involve the linking tag at all! Authorizing proofs show that the linking tag is valid and are used to sign the final transaction.

Because RingCT bakes the linking tag into the ambiguous signature, signing (and multisignature) operations are more computationally intensive, and it becomes more challenging to build other tag-related functionality. But in Seraphis, constructing membership proofs can be safely delegated from highly trusted devices (which may have limited computing power, like a hardware wallet) to a less trusted device, and signing (and multisignature) operations are far easier using the much simpler authorizing proof.

Fortunately, some of the building blocks required by Seraphis already exist elsewhere, and don't need to be designed from scratch. Both the Bulletproofs and Bulletproofs+ constructions can be used as range proofs. Modifications to Schnorr-type proving systems can be used for authorizing proofs. And an efficient [proving system](https://eprint.iacr.org/2015/643) used already as the basis for Triptych, [Lelantus](https://eprint.iacr.org/2019/373), and [Spark](https://eprint.iacr.org/2021/1173)* can be modified for membership proofs.

* Cypher Stack receives funding for Spark development.

## Addressing

Unfortunately, Monero addresses currently in use are not compatible with Seraphis. Users would need to generate new addresses from their wallet keys in order to receive Monero if Seraphis were implemented. However, this ecosystem cost comes with a host of benefits.

Aside from the structural benefits discussed above, the Seraphis design is amenable to many different address construction possibilities, each of which comes with tradeoffs. While the final address construction to be used in Seraphis is [still being decided](https://github.com/monero-project/research-lab/issues/92) (one scheme receiving a lot of attention is called [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), we can describe some common and useful features.

You might know that Monero addresses offer _view key_ functionality, where you can provide a view key to a device or third party and allow it to watch for incoming outputs on your behalf, but without giving up spend authority. This is useful for wallets, which can stay updated while keeping your spend key safely locked away. It's also useful for cases where you want external view access, like a public charity offering transparency or a company with an accounting department.

The downside to Monero view keys is that they don't provide complete or fine-grained view access. It's not possible to reliably detect when a wallet spends funds, which makes it difficult to compute wallet balances properly when the spend key isn't available. It's also not currently possible to detect incoming outputs without also learning the value contained in those outputs (which means any third-parties responsible for finding incoming outputs will learn exactly how much Monero you are acquiring).

Seraphis addressing constructions can solve this. With Seraphis, your address comes equipped with different keys that can do different things:

  * Watch for incoming outputs, but hide their value
  * Watch for incoming outputs, but show their value
  * Watch for outgoing outputs
  * Help you to generate transactions, but not sign them
  * Generate new addresses (useful for retailers or exchanges with many customers)

As the address holder, you get to decide how much authority you delegate to other devices or third parties.

## The big picture

Seraphis is a major change to the Monero ecosystem. While it involves modifications to addresses and transaction building blocks, its design offers flexibility and useful functionality that aren't possible with today's RingCT protocol. While much of the design is finalized and being developed into [an implementation](https://github.com/UkoeHB/monero/tree/seraphis_lib), address design and security analysis are ongoing. Seraphis offers an excellent opportunity to push the Monero ecosystem forward!

Further reading

  * [How Monero Uniquely Enables Circular Economies](/knowledge/monero-circular-economies/)

  * [Monero’s Ring Signatures vs CoinJoin Like in Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Why (And How!) You Should Hold Your Own Keys](/knowledge/hold-your-keys/)

  * [Contributing Back to Monero](/knowledge/contributing-to-monero/)

  * [How Remote Nodes Impact Monero’s Privacy](/knowledge/remote-nodes-privacy/)

  * [How Monero Uses Hard-Forks to Upgrade the Network](/knowledge/network-upgrades/)

  * [View Tags: How One Byte Will Reduce Monero Wallet Sync Times by 40%+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool and Its Role in Decentralizing Monero Mining](/knowledge/p2pool-decentralizing-monero-mining/)

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