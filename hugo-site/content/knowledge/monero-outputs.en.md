---
title: "Monero Outputs Explained"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero, like other cryptocurrencies, uses outputs as a means of accounting for funds. Many crypto savvy users have probably heard this term before, but not everyone understands what they mean and how they work. As explored in our [ring signatures article](/knowledge/ring-signatures), outputs are the actual unit exchanged on the blockchain between transacting parties. Similar to a dollar bill, but the amount is not in a fixed denomination.

If you get paid $16 for a job, you might receive a one dollar bill, a five dollar bill, and a ten dollar bill. You have $16, but you also have three different bills in your wallet. If you wanted to pay someone 6 dollars, you could use the 5 and the 1 bill, but if you wanted to pay someone $8 you could only use the $10 and receive $2 back in change. Lastly, if you wanted to pay someone $14 you would have to use all three bills, and would receive $2 back in change, but for a moment, when you hand over all three bills, you have no money in your wallet until you get the change back.

Monero works similarly. Suppose you run a store and make three sales on three different items. You might receive 1.5 XMR, 2.25 XMR, and 5.25 XMR for a total of 9 XMR, but you also have three different outputs in your wallet of the denominations stated previously. Just like with the dollars, you might want to pay someone 3 XMR. You could use just the 5.25 XMR output, and receive 2.25 XMR back in change, or you could combine the 1.5 and 2.25 XMR outputs and get 0.75 XMR back in change.

But, as soon as you send the transaction, the outputs that you do use are put in a "locked" state, meaning they are inaccessible until you receive back the change. The protocol unlocks the funds (i.e. gives you back the change) after 10 confirmations, or around 20 minutes. Just like once you hand over the dollar bills out of your wallet, you cannot use the money again until you receive the change back from the cashier, your Monero is inaccessible until you receive back the change.

Let's go back to the example of sending 3 XMR to someone, and you use the 5.25 XMR output. Now, while you wait for you 1.75 XMR back in change, you cannot use it. This 1.75 XMR is inaccessible to you. But you can still use the 1.5 XMR and 2.25 XMR outputs, as these were not spent. Going back to the dollar example, if you paid someone $8, as in the example before, you would not be able to use the $2 that you expect back in change until it is given to you, but in this example, you still have a $10 bill that is unused in your wallet. This can still be used to purchase whatever you want while you wait for the change. The same with Monero.

This is often a point of confusion for new Monero users. Often, a user may just have one output in their wallet, received from an exchange or a friend. Let's say this output is 20 XMR. They have no other outputs in their wallet. They now want to make a donation to two of their favorite charities. They send 5 XMR to the first charity and then are confused because, even though they should have 15 XMR left, they cannot immediately send the next donation to the second charity. As you might have guessed, this is because the 15 XMR is locked. It cannot be spent until it is returned as change (10 confirmations or around 20 minutes). After their funds are unlocked, they would be able to send their second donation.

Just to reiterate the point, they would not have had this problem if they had had multiple outputs instead, such as two 10 XMR outputs or similar. They would be able to send both donations one right after the other, because the first donation would use one of the 10 XMR outputs (and wait 10 confirmations to receive 5 XMR back in change), and the second donation would use the other 10 XMR output.

Some cryptocurrency wallets have a feature called ‘output management’, which simply shows a user which outputs they currently have (in addition to their total sum), as well as allows them to choose which ones they want to use when they spend their cryptocurrency.

As of now, the Monero GUI does output selection for users automatically, as users selecting their own outputs often leads to confusion or, in some cases, harmed privacy. There are wallets under construction however, such as the new Feather wallet project, that will contain these output management features.

We’ve been talking a lot about the sending portion, but something fascinating happens on the receiving end. Going back to our example of sending 3 XMR to someone, and using your 1.5 XMR and 2.25 XMR outputs in the transaction (while expecting 0.75 XMR in change), the receiver does NOT receive two outputs of 1.5 XMR and 2.25 XMR. They instead receive ONE 3 XMR output.

In the background, the protocol combines all outputs used for spending, and gives the receiver one output of the paid amount, and sends one change output back to the sender. So the sender will also receive one output back as change, regardless of whether they used two, three, or ten outputs to send the transaction.

We hope this has cleared up some confusion about outputs and how the internal accounting of the protocol works, as well as the common user facing problem of confusion when encountering locked funds. In another article, we will explore managing your outputs so as to minimize the chance of having to wait for unlocked funds before sending future transactions.

Further reading

  * [How Monero Uniquely Enables Circular Economies](/knowledge/monero-circular-economies/)

  * [Monero’s Ring Signatures vs CoinJoin Like in Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

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