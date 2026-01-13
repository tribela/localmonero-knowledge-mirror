---
title: "How Remote Nodes Impact Monero’s Privacy"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
One of the biggest advantages Monero has over other cryptocurrencies is it’s on-chain privacy, but have you ever wondered how Monero’s privacy holds up when you use a remote node? How about if you use a “light wallet” server like MyMonero?

In this post we’ll dive into some of the details behind how Monero provides exceptional on-chain privacy even when using a remote node, as well as what to watch out for when using remote nodes.

## What function do nodes serve in Monero?

## What function do nodes serve in Monero?

For those less familiar with how Monero works, the nodes (or servers) in the Monero network can be run by anyone and allow the owner of the node – or others they choose to share it with! – to synchronize a copy of the blockchain and provide that copy to others on the network. These nodes also verify all the transactions happening on the network, as well as all blocks that are published and ensure that they all follow the rules as set by consensus.

The other function that nodes serve in Monero is as a way to provide all of the data your favorite Monero wallet needs to properly check for transactions that belong to you and make new transactions. This data is provided by nodes in two ways:

  * The data from each block on the blockchain is requested by the wallet, scanned for transactions belonging to you, and then discarded once checked by the wallet. 
    * This step will soon be drastically improved, thanks to [view tags](/knowledge/view-tags-reduce-monero-sync-time).
  * When sending transactions, the node you use provides a list of possible decoys (or fake inputs) to use when building the transaction, ensuring that you have a good crowd to hide in each time you spend Monero. 
    * These decoys are a part of [ring signatures](/knowledge/ring-signatures), an important piece of Monero’s approach to privacy on-chain.

  * This step will soon be drastically improved, thanks to [view tags](/knowledge/view-tags-reduce-monero-sync-time).

  * These decoys are a part of [ring signatures](/knowledge/ring-signatures), an important piece of Monero’s approach to privacy on-chain.

## What is the most private and secure way to use Monero?

## What is the most private and secure way to use Monero?

The best thing to do, even with the strong on-chain privacy provided by Monero when using remote nodes, is to run your own Monero node to ensure that you have a pristine copy of the Monero blockchain handy and that your IP address is well protected. The other benefit when running your own node is that you can contribute back to the network, letting other nodes synchronize from your node or even letting other users connect to your node with their wallets.

That being said, Monero does still provide excellent privacy when using a remote node. If you’re interested in running your own Monero node, here is an easy to follow guide to doing so:

  * [Run a Monero Node](https://sethforprivacy.com/guides/run-a-monero-node/)

## What can a remote node learn about me?

## What can a remote node learn about me?

When using a remote node, there are a few key pieces of information that get exposed to a remote node and a couple of key ways that node can attack you, prevent you from transacting, and more.

The first thing a remote node can learn about you is your public IP address. While this will hopefully be concealed via a VPN or Tor, the remote node could associate your public IP address with the transaction, helping them to narrow down where you are transacting from. The remote node can also learn the last block your wallet synced and use this to try and make educated guesses about you, such as when you normally use Monero and when you last spent Monero. This is especially true if you are always coming from the same IP address (such as your home). The last key thing that a remote node can learn about you is basic information about the transactions you send through it. While this may be the most obvious data that the remote node operator gets about you, it’s important to understand that this could be used to help track down the sender of the transaction when combining that information with other off-chain data. This can be especially dangerous if the remote node is run by a malicious entity, a blockchain analytics company, or an oppressive nation-state.

A remote node can also attempt to cause you trouble by hiding blocks from you, making your wallet think it was synced when it wasn’t. This can make you think funds are lost or prevent you from spending funds until you connect to another node. The last key thing a remote node could do is feed your wallet a manipulated list of decoys. This could cause your wallet to either fail completely to build transactions (making you unable to spend funds), or could allow the remote node to try and provide decoys it knows are spent to reduce the anonymity you receive in each transaction.

## What privacy guarantees still exist when using a remote node?

## What privacy guarantees still exist when using a remote node?

While this article may have scared you a bit, it’s important to realize that the privacy provided by Monero is excellent even when using a remote node, and far surpasses any other cryptocurrency when used this way. You still gain the strong on-chain privacy provided by Monero, as the remote node never knows the true input (what coins you’re spending), the amount of Monero spent in the transaction, or the address of the recipient of the transaction. Outside observers also cannot see the true input, amount, or addresses involved (no matter what type of node you choose to use!), ensuring that outside of the remote node even your IP address, wallet sync information, and transactions have strong privacy guarantees.

The remote node also never has access to the previous transactions you’ve sent or received or the amount of Monero currently in your wallet, and loses all visibility into your transactions the moment you start to use another node. No private keys (either spend or view keys) are ever provided to the remote node, and so your wallet remains private, secure, and usable. No matter the remote node, you also are never at risk of losing Monero or having it stolen, as the node cannot edit the recipient address, never has access to your wallets private keys, and cannot confiscate your Monero in any way.

## How about “light wallets” like MyMonero?

## How about “light wallets” like MyMonero?

While the topic is a bit outside the scope of this article, I did want to address a unique type of wallet in Monero – light wallets. The name light wallet comes from the fact that your wallet (on your phone or computer) does not have to perform any of the blockchain synchronization, making the experience faster and more fluid.

However, wallets like this come with a severe privacy trade-off for now – your wallet sends the private view key to the remote server you use (like the default in MyMonero), giving the remote server full visibility into any received funds since the creation of your wallet (and until you stop using that wallet or seed). This does reduce the privacy you receive from the node operator drastically, and should be approached with caution.

Thankfully, the Monero community is working on improving the software you can use to host your own light wallet server (LWS), which will allow you to have fast synchronization without trusting a 3rd-party with your private view keys – as you will run the software where your wallet sends the private view keys!

For more on the custom light wallet server, see the below Github repository:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## How can I learn more?

## How can I learn more?

If you’re curious and would love to better understand nodes in Monero and look into using a remote node or running your own, see the links below for great places to get started:

  * [Monero World, a list of community-run remote nodes that can be used](https://moneroworld.com/#nodes)
  * [Monero nodes run by Seth For Privacy, the author of this article](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, a list of remote nodes with frequently checked status](https://monero.fail/)
  * [How to connect to a remote node within GUI wallet](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia - Remote Node](https://www.getmonero.org/resources/moneropedia/remote-node.html)

Further reading

  * [How Monero Uniquely Enables Circular Economies](/knowledge/monero-circular-economies)/

  * [Monero’s Ring Signatures vs CoinJoin Like in Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Why (And How!) You Should Hold Your Own Keys](/knowledge/hold-your-keys)/

  * [Contributing Back to Monero](/knowledge/contributing-to-monero)/

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