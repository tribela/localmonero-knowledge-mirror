---
title: "How Monero Uses Hard-Forks to Upgrade the Network"
slug: "network-upgrades"
date: "2022-02-10"
image: "/images/upgrades.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
One of the most commonly misunderstood parts of Monero’s approach to building a decentralized, privacy-preserving, and secure cryptocurrency is the role that hard-forks (or network upgrades) play.

In this post we’ll walk through what hard-forks are, why they are important for Monero, and what role you can play in them in the future.

## Why does Monero need to keep upgrading the network?

## Why does Monero need to keep upgrading the network?

The Monero community has committed to iterating and improving the project over time, and it seems that commitment boils down to two key aspects of the community’s ethos:

  1. The Monero project is ultimately software – code – written by humans. This can lead to a need to fix bugs, add in improvements that are discovered or invented over time, implement modernizations to the protocol, or to simply maintain the project. This is similar in many ways to the other pieces of software you use (like the browser you’re reading this in!), which need to constantly be updating in order to add new features and fix bugs.

  2. The Monero project is a privacy tool, and privacy is an ever-advancing arms race. The people and groups who would like nothing more than to strip the world of privacy (both financial and personal) are constantly improving, developing, and inventing new ways to attack modern approaches to preserving privacy, like those used in Monero. As the enemies of privacy find these new approaches, the Monero network needs to be able to adapt and improve to fight back and defend our right to financial privacy.

The Monero project is ultimately software – code – written by humans. This can lead to a need to fix bugs, add in improvements that are discovered or invented over time, implement modernizations to the protocol, or to simply maintain the project. This is similar in many ways to the other pieces of software you use (like the browser you’re reading this in!), which need to constantly be updating in order to add new features and fix bugs.

The Monero project is a privacy tool, and privacy is an ever-advancing arms race. The people and groups who would like nothing more than to strip the world of privacy (both financial and personal) are constantly improving, developing, and inventing new ways to attack modern approaches to preserving privacy, like those used in Monero. As the enemies of privacy find these new approaches, the Monero network needs to be able to adapt and improve to fight back and defend our right to financial privacy.

## What is a hard-fork?

## What is a hard-fork?

The complexity of upgrading Monero comes into effect once you understand how different upgrading a cryptocurrency is versus simply pushing a software update to something like a browser.

In cryptocurrencies, the rules of the network (things like how transactions should look, how mining works, and how to verify each block) must be agreed upon by the network, something that is called “consensus”. When any of these rules need to be changed or upgraded, the network has to agree on the new rules, causing a “hard-fork” – a situation where the network actually splits into two chains of blocks – one on the old rules, and one on the new rules.

When everyone in the community agrees on the rule changes, it’s called a “non-contentious hard-fork”, and the chain that still has the old rules dies off and is not mined on after the hard-fork. This has been the case for almost every Monero hard-fork, and the only continuation of old rules was by projects attempting to profit off of the hard-fork.

While non-contentious hard-forks are the only way to properly upgrade important aspects of the Monero network, they do also have a frustrating side-effect – old software, released before the hard-fork was planned, cannot understand the new rules of the network and so does not function after the hard-fork! This can lead to users thinking funds are lost, thinking the Monero blockchain has stopped, and being unable to move funds until they upgrade their wallet.

## Who decides when the Monero network upgrades and what is included?

## Who decides when the Monero network upgrades and what is included?

As there is no central authority, CEO, or president of Monero, the work around deciding when to upgrade the network, what to include, and how to go about it falls to _us_ , those people in the Monero community who choose to engage and interact! This is both an extremely important part of a decentralized project, as the planning and decision making for the project is ultimately decentralized and crowd-sourced from the community.

The planning of timing and features included in each network upgrade in Monero happens in two main places:

  1. On IRC and Matrix, the most used chat platforms in the Monero community (which are bridged together). These platforms allow for large group chats and are where all scheduled Monero community meetings, dev meetings, and research lab meetings are held. These meetings are the best way for you to listen in (or contribute!) to the planning and discussion around network upgrades in Monero.

  2. On Github, the main communication platform for longer-running Monero discussions, planning, and organization. The Monero community uses Github to organize meetings, discuss new features and ideas, and coordinate the planning of network upgrades in addition to storing the code for the Monero project.

On IRC and Matrix, the most used chat platforms in the Monero community (which are bridged together). These platforms allow for large group chats and are where all scheduled Monero community meetings, dev meetings, and research lab meetings are held. These meetings are the best way for you to listen in (or contribute!) to the planning and discussion around network upgrades in Monero.

On Github, the main communication platform for longer-running Monero discussions, planning, and organization. The Monero community uses Github to organize meetings, discuss new features and ideas, and coordinate the planning of network upgrades in addition to storing the code for the Monero project.

If you have an important idea for a network upgrade, don’t like an approach being taken, or have concerns around the timing of an upgrade, it’s important that you speak up and present your case clearly to the community!

## How can I help with network upgrades?

## How can I help with network upgrades?

As upgrades to the Monero network require community coordination and approval along with software updates, it’s extremely important that as many people as possible get involved in the planning, testing, and communication process of network upgrades.

Here are a few easy ways you can help smooth things out around a network upgrade:

  1. Join the planning meetings [posted on Github](https://github.com/monero-project/meta/issues), listen in, and contribute if you have something relevant to bring up.
  2. Communicate the details around the network upgrade timing (once decided!) to your favorite exchange, wallet, or mining pool. It can be tricky to properly notify all Monero users of an upgrade, so it’s important we all help out where we can to get the word out.
  3. Test the software before the network upgrade. There will be a call put out for testers before the network upgrade, both on testnet and stagenet, to ensure that every aspect of the upgrade has been properly planned for and implemented in the software. The more people get involved and thoroughly test the new versions out, the more likely the network upgrade will go smoothly!
  4. Once releases that are compatible with the network upgrade are published, be sure to upgrade immediately! The more people are upgraded and ready for the network upgrade, the more smoothly the network will handle it and the less headache users will experience.

## What can I expect in the next Monero network upgrade?

## What can I expect in the next Monero network upgrade?

While there is not a date set in stone yet, there will be a network upgrade soon to implement a few key upgrades and features in Monero:

  1. A ring-size increase from 11 to 16, increasing the base anonymity set (read: plausible deniability, or base privacy) of every transaction on the network
  2. [View tags, a brilliant way to reduce wallet sync times by 30-40%](https://localmonero.co/knowledge/view-tags-reduce-monero-sync-time)
  3. Fee changes, improving the security and resilience of the network to rapid changes in the fee market or attacks by malicious entities
  4. [Bulletproofs+, a further improvement in the efficiency of Monero transactions](https://www.getmonero.org/2020/12/24/Bulletproofs+-in-Monero.html)

These changes will go a long way to increasing the privacy, efficiency, and security of the network, all while paving the way for [Seraphis](https://localmonero.co/knowledge/seraphis-for-monero), the next-generation transaction protocol for Monero.

## How can I learn more?

## How can I learn more?

The topic of hard-forks and network upgrades is a vast one and there is a long and storied history of them in Monero, so be sure to dig into some of the following links if you’d like to learn more about the history, process, or planning that is in-progress for the upcoming network upgrade!

  * [Monero v15 hard-fork planning](https://github.com/monero-project/meta/issues/630)
  * [Scheduled software upgrades (in Monero)](https://github.com/monero-project/monero#scheduled-software-upgrades)
  * [A note on scheduled protocol upgrades](https://web.getmonero.org/2020/09/01/note-scheduled-upgrades.html)

Further reading

  * [How Monero Uniquely Enables Circular Economies](/knowledge/monero-circular-economies)/

  * [Monero’s Ring Signatures vs CoinJoin Like in Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Why (And How!) You Should Hold Your Own Keys](/knowledge/hold-your-keys)/

  * [Contributing Back to Monero](/knowledge/contributing-to-monero)/

  * [How Remote Nodes Impact Monero’s Privacy](/knowledge/remote-nodes-privacy)/

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