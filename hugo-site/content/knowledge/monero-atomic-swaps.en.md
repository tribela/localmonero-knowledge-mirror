---
title: "How Atomic Swaps Will Work in Monero"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
In the pursuit of decentralization and a truly permissionless system, few things are as coveted in the cryptocurrency space as decentralized exchanges and atomic swaps. Since its inception, Monero has struggled to implement atomic swaps, as the privacy features create unique problems when trying to design a protocol.

But first, let's back up. What are atomic swaps? An atomic swap is a protocol by which two different cryptocurrencies, on different blockchains, can be exchanged in a trustless manner with no intermediary. This means if someone wanted to exchange cryptocurrency A for cryptocurrency B, they would be able to do it without an exchange, centralized or decentralized. As one might imagine, this takes considerable research, and the full technical details that make it possible get quite complicated. Once again, LocalMonero is here to help and give a simple explanation for the common person.

To start, let's consider the simplest form of atomic swap, as implemented by Bitcoin. If someone wants to exchange Bitcoin for another coin that uses the same hash time lock contract technology, they can do so in the following way. Alice has Bitcoin (BTC), but wants Litecoin (LTC), and Bob has LTC, but wants BTC. They decide to do an atomic swap so each gets the coin that they want. Alice sends her BTC to a special address, utilizing scripts that lock the funds away so even she can't access it. You can think of it like Alice puts her BTC in a lockbox. When the lockbox is made, she gets a key, and sends a hash of this key to Bob. Now Bob does not have the key itself, only the hash, so he can't yet access the funds.

Bob uses this hash as a seed from which he generates his own lockbox, and sends his LTC there, where it is also locked. Since the hash of Alice's key was used as the seed by which Bob's lockbox was made, she can use her key to claim the LTC in Bob's lockbox. Her key fits! But, using math voodoo magic, when she uses her key to open the LTC lock, she reveals the key to Bob, who can then use it to claim the BTC that she put in her lockbox. In this way, with no intermediary, Alice and Bob have successfully exchanged their assets.

But there's a slight problem. What if Alice sends to her lockbox, and Bob decides he doesn't want to trade anymore. Now, since Alice can't access her BTC that she locked away, and Bob won't complete his part of the transaction, Alice just loses her money forever. Well, luckily, Bitcoin has a little technology called refund transactions, and so after a period of time, if the BTC is not claimed by Bob, the scripts have a fail-safe built in, where the BTC will automatically go back to Alice. This was the primary speedbump for Monero's atomic swaps implementation. Because of Monero's [ring signatures privacy technology](/knowledge/ring-signatures), the sender of a transaction is always uncertain. How can the protocol do a refund transaction if even it doesn't know where the transaction came from?

In 2017, a small group of researchers outlined a different method by which atomic swaps would work in Monero. After several years of refinement, the researchers finalized a process by which Monero would be able to do atomic swaps with Bitcoin, even without refund transactions.

As with many things of this level of technical complexity, our explanation will overly simplify some things in order to convey the idea, but it will still give a solid idea of the mechanisms by which this process would work.

Both Alice (who has XMR and wants BTC) and Bob (who has BTC and wants XMR) must download and run a program that supports the atomic swap. This may be implemented into wallets, decentralized exchanges, or special, specific programs, but the software must be running the atomic swap protocol. In the first step, Alice and Bob's clients connect to each other and make several shared secrets and keys. In this step, a new Monero address is created, with Alice having one half of the key, and Bob having the other. No Monero is in there yet though, so there's nothing to spend. One last thing to note about this address, is that they both have the view key to this wallet, so they can both peek inside to see if or when Monero arrives.

In the second step, Bob sends his BTC to a special address, similar to the Bitcoin atomic swap protocol we've already discussed. After Alice sees the BTC arrive to this address on the blockchain, she sends her Monero to the Monero address that she and Bob both have one half of a key to. Bob can verify that the Monero arrived since he also has the view key, and once he sees the Monero is safely in the wallet, he sends Alice a piece of a key that will allow her to withdraw the Bitcoin. Similar to the other protocol, the process of claiming the Bitcoin reveals her half of the Monero key to Bob. Now Bob has both halves, so he can claim the Monero, while Alice has only her half, so she can't try to take it before he does.

So if you looked at all of this and are still a bit confused about how Monero was able to get around the problem of refund transactions, the answer is quite simple. Since Monero itself does not have refund transactions, the reader should notice that the Bitcoin (which does have refund transactions) is sent first, and only after it is verified as being on the blockchain is the Monero sent. This allows Monero to utilize Bitcoin's ability to script in refund transactions and take advantage of them, without needing to have these capabilities itself.

The atomic swap is now complete, but from here, Bob has a couple of options for his newly claimed XMR. He can use this Monero wallet as is, or move the XMR to another wallet that he already owns. Bob will most likely move the Monero to another wallet, because Alice still has the view key and can see inside.

The beauty of this protocol is that it's still quite new, and there is plenty of room for optimizations. It's also quite flexible in its architecture, so implementation in other wallets or decentralized exchanges should be simple and fit cleanly with their existing architecture.

Further reading