---
title: "Why Monero is Better than Dash, Zcash, Zcoin (Even with Lelantus), Grin and Bitcoin Mixers Like Wasabi (Updated May 2020)"
slug: "why-monero-is-better"
date: "Sat Feb 01"
image: "/images/why-monero.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Not all privacy-centric coins can deliver 100% privacy, untraceability, security and fungibility in a 100% decentralized coin with a trustless setup. Here's what these attributes are and why they're important:

Private
    Your finances are not visible to the public. A person looking at the coin's blockchain won't be able to see how much money you have.
Untraceable
    The coins can't be traced through blockchain analysis or blockchain monitoring.
Secure
    All transactions are encrypted and the wallet which holds your funds is encrypted.
Fungible
    All coins are equal and have the same value.
Decentralized
    All nodes (a node is a running instance of the coin's blockchain) of the network are equal. There is no superclass of nodes which have more influence or control over transactions or the system than other nodes.

## Coin analysis

Here is an analysis of well-known cryptocurrencies which claim anonymity and/or untraceability as their key differentiator. Bitcoin itself is not within the scope of this analysis since it's never claimed to be anonymous.

This site was made by Monero users. There was a time when we weren't Monero users but were concerned about financial privacy. We researched the coins which claimed to be private and this page is the result of our research. It's why we chose Monero over the rest. So, if we appear to be biased, we are, but we believe that bias is based on facts which you can read below and verify for yourself.

### Overview

Select a logo to jump to that coin's analysis.

| Private| Untraceable| Secure| Fungible| Decentralized  
---|---|---|---|---|---  
Monero| Yes| Yes| Yes| Yes| Yes  
DASH| No| No| Yes| No| No  
Zcash| No| Not completely| Yes| No| No  
| Yes| Yes| Yes| Yes| No  
| Sometimes| No| Yes| Unsure| Yes  
Bitcoin mixers| No| No| Yes| No| Sometimes  
  
### Monero

Private
    Monero uses a cryptographically sound system that allows you to send and receive funds without your transactions being publicly visible on the blockchain (the distributed ledger of transactions). This ensures that your purchases, receipts, and other transfers remain **private by default**. The sender, receiver and amount of the transaction are all private. Some coins have a "rich list" which allows anyone to see which account has the most coins. Since Monero is private, a [ Monero rich list ](http://moneroblocks.info/richlist) can't exist.
Untraceable
    By taking advantage of ring signatures (a special property of certain types of cryptography), Monero enables untraceable transactions. This means it's ambiguous which funds have been spent, and thus extremely unlikely that a transaction could be linked to particular user.
Secure
    Using a distributed peer-to-peer consensus network, every transaction is cryptographically secured. Individual accounts have a 25-word mnemonic seed displayed when created, which can be written down to back up the account. A password is mandatory when creating a wallet, and account files are encrypted with a passphrase to ensure they are worthless if stolen.
Fungible
    All coins are equal and have the same value. A user, vendor, or any other entity can't block or blacklist certain Monero coins since the transaction history of Monero coins is ambiguous.
Decentralized
    All Monero nodes are equal. There is no superclass of nodes which have more influence or control over transactions than other nodes. No person or entity can trace transactions by owning multiple nodes. Additionally, there is no trusted setup. This means that the need to trust a person or entity is not a factor. The only things that need to be trusted are the source code (which can be verified by anyone) and math.

Monero has been 100% open source from its inception, meaning anyone can view the software's [ source code ](https://github.com/monero-project/bitmonero) to verify that no backdoors exist and that the software is secure.

Monero also has [ peer-reviewed research papers ](https://lab.getmonero.org/) which mathematically and systematically verify all of its properties listed above.

### DASH

Private
    

DASH has a [ rich list](https://bitinfocharts.com/top-100-richest-darkcoin-addresses.html), so this is not a private coin. The financial details of coin addresses are visible to anyone examining the blockchain.

> DASH isn't cryptographically private at all. Actually I had a slide in the deck that was like 'DASH, LOL,' and like nothing else... it's snakeoil and I'm just sort of beside myself about it, personally. 
> 
> **Gregory Maxwell** , Bitcoin Core developer and cryptographer, in a [ presentation to Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

**Peter Todd** , another Bitcoin Core developer and cryptographer, has made a [ similar statement](https://twitter.com/petertoddbtc/status/622022840330682368).

Untraceable
    Transactions are routed through a series of [ Masternodes ](https://www.dash.org/masternodes/) to make them untraceable. This practice might work if all masternode operators had only pure motives. However, if a government, group of hackers, other entity, or even an individual bought many masternodes (there would be no way to know if this occured) and if the transaction passed through a route where all of the masternodes were owned by that entity, then the transaction could be traced by that entity. Given the relatively low cost of masternodes and the enormous budget of governments and some organizations, the possibility that coins can be traced is real.
Secure
    Transactions are cryptographically secure.
Fungible
    Since transactions are not private, the potential exists for an entity to block or blacklist certain coins, making them less valuable than the others. See the note on the lack of Bitcoin fungibility below since the same principle applies to DASH.
Decentralized
    Not all DASH nodes are equal. There is a superclass of nodes, called _Masternodes_ whose owners have more influence over the system than regular node operators. This makes DASH semi-centralized instead of the ideal 100% decentralized system.

### Zcash

Private
    

Zcash transactions are visible on their blockchain. They do enable hidden transactions, but [ less than 1% of transactions are fully shielded ](http://stat.bloxy.info/superset/dashboard/zcash/) . Since hidden transactions are optional and not the default (not to mention rarely used), the [ hidden transactions stand out on their blockchain](http://weuse.cash/2016/06/09/btc-xmr-zcash/), drawing attention to themselves.

> And by the way, I think we can successfully make Zcash too traceable for criminals like WannaCry, but still completely private & fungible. 
> 
> **Zooko Wilcox** , Zcash CEO, in a [ tweet ](https://twitter.com/zooko/status/863202798883577856)

If Zcash can be "too traceable", then it can't be completely private or fungible. 

Untraceable
    

Regular transactions are transparent. Hidden transactions use zk-SNARKS, which have admittedly robust privacy guarantees under certain conditions. The question is if these conditions are met, and seeing the miniscule amount of people using the shielded capabilities, this remains in question.

Secure
    Transactions are cryptographically secure.
Fungible
    Since all transactions are not private, the potential exists for an entity to block or blacklist certain coins, making them less valuable than the others. See the note on the lack of Bitcoin fungibility below since the same principle applies to Zcash.
Decentralized
    

Zcash is a company and currently it [ takes 20% of all ZEC mined as a founder's reward](https://z.cash/blog/funding.html). 

Zcash required a **Trusted Setup**. This means that you have to trust that the system was set up honestly. If it wasn't set up honestly, [ unlimited amounts of ZEC could be created without anyone knowing](https://blog.okturtles.com/2016/03/the-zcash-catch/). This would make the hacker rich and devalue ZEC. There is no way to know if the Trusted Setup was executed honestly. We have to take them at their word. This introduces a human point of failure into the system which is counter to almost every other cryptocurrency. You should only have to trust math and verifiable source code in cryptocurrecies, not humans. As we've seen with virtually all large software companies, such as [ Microsoft](https://www.gnu.org/proprietary/proprietary-back-doors.en.html), [ Apple](http://www.digitaltrends.com/computing/apple-vs-fbi-backdoor-to-data-already-exists/), and even governments, they shouldn't be trusted. 

Peter Todd, a Bitcoin Core developer who [ participated ](https://github.com/zcash/mpc/blob/master/README.md) in the Zcash Trusted Setup, has called it a " [ backdoor ](https://twitter.com/petertoddbtc/status/793584540891643906) ". 

> Zcash is not unconditionally sound, can't be with current tech...requires a trusted setup… will need to redo the procedure [Trusted Setup] to upgrade the crypto over time so it's a vulnerability. 
> 
> Gregory Maxwell, Bitcoin Core developer and cryptographer, in a [ presentation to Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

**Note:** Zcoin is shifting from its current Sigma scheme to a new protocol that relies on its new work, Lelantus. Lelantus is going to be implemented in stages, and this article is going to assume all stages are complete and implemented for proper comparisons alongside projected implementation times.

The reason Zcoin was given this luxury of being judged on its future protocol, and not Zcash, is because Zcoin has a roadmap with general timings for activation, whereas Zcash's 'privacy by default' plans are and continue to be nebulous.

Private
    

Zcoin (XZC) will not have a rich list, so it will be private. By-default, mandatory privacy is expected to go live in 2021. Once implemented, a rich list will not be possible to create (though currently [they do have one](https://www.coinexplorer.net/XZC/richlist)).

Untraceable
    With the final stage of Lelantus implemented in 2021, Zcoin should not be traceable, although theoretical attacks have not yet been explored since it has not yet been released or had any time out in the wild. At present Zcoin is traceable if one puts a [Zcoin address](https://explorer.zcoin.io/) in a blockchain explorer and you can see its balance and related transactions.
Secure
    Transactions are cryptographically secure.
Fungible
    After the final stage of Lelantus goes live in 2021, it is assumed that Zcoin will be fungible due to the mandatory privacy enforcement. In this regard, it will be a true competitor to Monero. However...
Decentralized
    Zcoin has implemented Znodes, which act simiarly to Dash masternodes, and have greater power than other nodes on the network. Since all nodes are not created equal, and the differenciating factor between them is the amount of money an individual has (Znodes cost 1000 XZC), the network is semi-centralized.

Private
    Grin does not have a rich list, which would indicate some form of privacy. Indeed, passive attackers scanning the chain cannot see which address has how much money in it, partially because amounts are obfuscated via confidential transactions, partially because address data is not stored on chain, and partially because of Mimblewimble's cut-through technology, where intermediate transactions can be removed from the chain, leaving little metadata from past transactions.
Untraceable
    Grin does not defend against an active attacker building a transaction graph. It is possible for both miners and a slightly modified node to watch every transaction, save it before the cut-through technology kicks in, and build a complete transaction graph from here, along with retaining all 'cut-through' data. They would not be able to discern any information prior to when they start, but everything after they begin will be valuable metadata with which they could potentially link transactions.
Secure
    Transactions are cryptographically secure.
Fungible
    Since all transactions are questionably private, and potentially traceable, there exists the possibility of building a transaction graph, from which can be gleaned valuable information that can be used against an individual regarding their spending habits. Outputs can then be linked to identities, and, even though amounts are not seen, the fact that an output can be linked to an identity means the output can be tainted, just off of the basis of who has held it. We think this means that Grin is not fungible, as some outputs may be tainted while others will not be.
Decentralized
    Grin has no premine, founder's reward, masternodes, or treasury. They did not have an ICO, and are run in a manner befitting of a decentralized community. Grin is decentralized.

### Bitcoin Mixers

Private
    

All Bitcoin transactions are visible on the blockchain and there is a [ Bitcoin rich list](http://www.bitcoinrichlist.com/top100), so Bitcoin is not private. Bitcoin is [ pseudononymous](https://bitcoin.org/en/you-need-to-know), not anonymous. 

For **Bitcoin mixers** , you have to trust that they can keep their data safe and are not owned by or cooperating with a government, hackers, or other entities. 

In July of 2017, the founder of the largest Bitcoin mixing service, BITMIXER.IO, announced that they were closing and gave this as their reason: 

> … Now I grasped that Bitcoin is transparent non-anonymous system **by design**. Blockchain is a great open book… 
> 
> BITMIXER.IO, in an announcement of closing on [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (emphasis in the original). 

A few weeks later, after considering the various privacy-centric coins, he said this: 

> After the deep investigation I confirm that MONERO is the best privacy currency. So I strongly recommend MONERO for all people who need extra privacy. 
> 
> BITMIXER.IO, in a [ followup post](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Untraceable
    

Since all Bitcoin transactions are visible on the blockchain, ALL Bitcoin transactions can be traced. A Bitcoin mixer can highly obfuscate transactions, making it much more difficult for someone to trace the Bitcoins, but not impossible. As technology progresses and companies which specialize in tracing Bitcoin transactions become more prevalent, once highly-obfuscated transactions will become relatively easily traceable: 

  * [ Law Enforcement Continues to Invest in Bitcoin Tracking Services ](https://news.bitcoin.com/law-enforcement-continues-invest-bitcoin-tracking-services/)
  * [ Time.com: Bitcoins Are Easier to Track Than You Think ](http://time.com/3689359/bitcoins-track-anonymous/)
  * [ Elliptic: A Company Specializing in Tracing Bitcoin for Law Enforcement ](https://www.elliptic.co/)

A Google search will reveal dozens of articles like the ones above. And remember, any transaction that occurred at any time in the past is on the blockchain and has the potential to be traced, even if a mixing service was used. In fact, the use of a mixing service is likely to draw attention to those transactions. 

Secure
    Transactions are cryptographically secure.
Fungible
    

Not all Bitcoins are equal and have the same value. Some Bitcoins have been blacklisted and blocked by several entities, making those coins less valuable than the rest. If you receive Bitcoins that were used in the past for illegal purposes, then your Bitcoins could be blacklisted even though you had nothing to do with the illegal activity. Or, say a government, employer, or some other entity decides to blacklist your Bitcoins in the future, much like they do with asset freezing or confiscation. There would be nothing you could do. Since a mixer only makes it more difficult to trace your Bitcoins, this category has been marked as "not fungible." 

  * Andreas Antonopoulos, a former Bitcoin Core developer who is well-respected in the Bitcoin and other cryptocurrency communities, acknowledges the Bitcoin fungibility problem in a [ YouTube video](https://www.youtube.com/watch?v=ak1iojpiHpM&feature=youtu.be&t=33m9s). 
  * Discussion of the Bitcoin fungibility problem on [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=1190707.0)

Decentralized
    Bitcoin itself is decentralized, but most mixing services are centralized. This means you need to trust them. Some newer ones, like Wasabi wallet are not, however.

## Summary

In our opinion, Monero is the clear choice if you're looking for a private, secure, untraceable, fungible, decentralized cryptocurrency with no trusted setup required. Anything else puts your privacy and security at risk. But don't just take our opinion. Do your own research and see for yourself. Consider that Monero is endorsed and used by entities which depend on privacy and untraceability, such as: 

  * [ SIGAINT ](https://www.reddit.com/r/Monero/comments/4xqrzd/sigaint_launches_tor_monero_node_as_its_operators/)
  * [ Purism ](https://puri.sm/posts/purism-collaborates-with-cryptocurrency-monero-to-enable-mobile-payments/)
  * [ Wikileaks ](https://shop.wikileaks.org/donate#db9)
  * AlphaBay Market (AB) was shut down in July of 2017. The [ Federal Forfeiture Complaint ](https://assets.documentcloud.org/documents/3898109/AlphaBay-Cazes-Forfeiture-Complaint.pdf) against AB shows that: 
    * **Monero is the only private and untraceable cryptocurrency:**   
"In total, from CAZES' wallets and computer agents took control of approximately $8,800,000 in Bitcoin, Ethereum, Moreno [sic], and Zcash, broken down as follows: 1,605.0503851 Bitcoin, 8,309.271639 Ethereum, 3,691.98 Zcash, _and an unknown amount of Monero._ " (bottom of p. 20 and top of p. 21, emphasis added) 
    * **Bitcoin transactions are not private and can be traced:**   
"Federal agents obtained the warrants after tracing a number of Bitcoin transactions originating with AlphaBay to digital currency accounts, and ultimately bank accounts and other tangible assets, held by CAZES and his wife." (p. 17, lines 24-26) 

LocalMonero does not advocate or encourage any illegal activity. 

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

  * [How CLSAG Will Improve Monero's Efficiency](/knowledge/what-is-clsag)/

  * [Why Monero Has a Tail Emission](/knowledge/monero-tail-emission)/

  * [A Brief History of Monero](/knowledge/monero-history)/

  * [Wired Magazine Is Wrong About Monero, Here's Why](/knowledge/wired-article-debunked)/

  * [Top 15 Monero Myths and Concerns Debunked](/knowledge/monero-myths-debunked)/

  * [How Dandelion++ Keeps Monero's Transaction Origins Private](/knowledge/monero-dandelion)/

  * [Why Monero Is Open Source and Decentralized](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: What Makes RandomX So Special](/knowledge/monero-mining-randomx)/

Not all privacy-centric coins can deliver 100% privacy, untraceability, security and fungibility in a 100% decentralized coin with a trustless setup. Here's what these attributes are and why they're important:

## Coin analysis

Here is an analysis of well-known cryptocurrencies which claim anonymity and/or untraceability as their key differentiator. Bitcoin itself is not within the scope of this analysis since it's never claimed to be anonymous.

This site was made by Monero users. There was a time when we weren't Monero users but were concerned about financial privacy. We researched the coins which claimed to be private and this page is the result of our research. It's why we chose Monero over the rest. So, if we appear to be biased, we are, but we believe that bias is based on facts which you can read below and verify for yourself.

This site was made by Monero users. There was a time when we weren't Monero users but were concerned about financial privacy. We researched the coins which claimed to be private and this page is the result of our research. It's why we chose Monero over the rest. So, if we appear to be biased, we are, but we believe that bias is based on facts which you can read below and verify for yourself.

### Overview

Select a logo to jump to that coin's analysis.

### Monero

Monero has been 100% open source from its inception, meaning anyone can view the software's [ source code ](https://github.com/monero-project/bitmonero) to verify that no backdoors exist and that the software is secure.

Monero also has [ peer-reviewed research papers ](https://lab.getmonero.org/) which mathematically and systematically verify all of its properties listed above.

### DASH

DASH has a [ rich list](https://bitinfocharts.com/top-100-richest-darkcoin-addresses.html), so this is not a private coin. The financial details of coin addresses are visible to anyone examining the blockchain.

> DASH isn't cryptographically private at all. Actually I had a slide in the deck that was like 'DASH, LOL,' and like nothing else... it's snakeoil and I'm just sort of beside myself about it, personally. 
> 
> **Gregory Maxwell** , Bitcoin Core developer and cryptographer, in a [ presentation to Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

DASH isn't cryptographically private at all. Actually I had a slide in the deck that was like 'DASH, LOL,' and like nothing else... it's snakeoil and I'm just sort of beside myself about it, personally. 

DASH isn't cryptographically private at all. Actually I had a slide in the deck that was like 'DASH, LOL,' and like nothing else... it's snakeoil and I'm just sort of beside myself about it, personally. 

**Gregory Maxwell** , Bitcoin Core developer and cryptographer, in a [ presentation to Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

**Peter Todd** , another Bitcoin Core developer and cryptographer, has made a [ similar statement](https://twitter.com/petertoddbtc/status/622022840330682368).

### Zcash

Zcash transactions are visible on their blockchain. They do enable hidden transactions, but [ less than 1% of transactions are fully shielded ](http://stat.bloxy.info/superset/dashboard/zcash/) . Since hidden transactions are optional and not the default (not to mention rarely used), the [ hidden transactions stand out on their blockchain](http://weuse.cash/2016/06/09/btc-xmr-zcash/), drawing attention to themselves.

> And by the way, I think we can successfully make Zcash too traceable for criminals like WannaCry, but still completely private & fungible. 
> 
> **Zooko Wilcox** , Zcash CEO, in a [ tweet ](https://twitter.com/zooko/status/863202798883577856)

And by the way, I think we can successfully make Zcash too traceable for criminals like WannaCry, but still completely private & fungible. 

And by the way, I think we can successfully make Zcash too traceable for criminals like WannaCry, but still completely private & fungible. 

**Zooko Wilcox** , Zcash CEO, in a [ tweet ](https://twitter.com/zooko/status/863202798883577856)

If Zcash can be "too traceable", then it can't be completely private or fungible. 

Regular transactions are transparent. Hidden transactions use zk-SNARKS, which have admittedly robust privacy guarantees under certain conditions. The question is if these conditions are met, and seeing the miniscule amount of people using the shielded capabilities, this remains in question.

Zcash is a company and currently it [ takes 20% of all ZEC mined as a founder's reward](https://z.cash/blog/funding.html). 

Zcash required a **Trusted Setup**. This means that you have to trust that the system was set up honestly. If it wasn't set up honestly, [ unlimited amounts of ZEC could be created without anyone knowing](https://blog.okturtles.com/2016/03/the-zcash-catch/). This would make the hacker rich and devalue ZEC. There is no way to know if the Trusted Setup was executed honestly. We have to take them at their word. This introduces a human point of failure into the system which is counter to almost every other cryptocurrency. You should only have to trust math and verifiable source code in cryptocurrecies, not humans. As we've seen with virtually all large software companies, such as [ Microsoft](https://www.gnu.org/proprietary/proprietary-back-doors.en.html), [ Apple](http://www.digitaltrends.com/computing/apple-vs-fbi-backdoor-to-data-already-exists/), and even governments, they shouldn't be trusted. 

Peter Todd, a Bitcoin Core developer who [ participated ](https://github.com/zcash/mpc/blob/master/README.md) in the Zcash Trusted Setup, has called it a " [ backdoor ](https://twitter.com/petertoddbtc/status/793584540891643906) ". 

> Zcash is not unconditionally sound, can't be with current tech...requires a trusted setup… will need to redo the procedure [Trusted Setup] to upgrade the crypto over time so it's a vulnerability. 
> 
> Gregory Maxwell, Bitcoin Core developer and cryptographer, in a [ presentation to Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

Zcash is not unconditionally sound, can't be with current tech...requires a trusted setup… will need to redo the procedure [Trusted Setup] to upgrade the crypto over time so it's a vulnerability. 

Zcash is not unconditionally sound, can't be with current tech...requires a trusted setup… will need to redo the procedure [Trusted Setup] to upgrade the crypto over time so it's a vulnerability. 

Gregory Maxwell, Bitcoin Core developer and cryptographer, in a [ presentation to Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

**Note:** Zcoin is shifting from its current Sigma scheme to a new protocol that relies on its new work, Lelantus. Lelantus is going to be implemented in stages, and this article is going to assume all stages are complete and implemented for proper comparisons alongside projected implementation times.

The reason Zcoin was given this luxury of being judged on its future protocol, and not Zcash, is because Zcoin has a roadmap with general timings for activation, whereas Zcash's 'privacy by default' plans are and continue to be nebulous.

Zcoin (XZC) will not have a rich list, so it will be private. By-default, mandatory privacy is expected to go live in 2021. Once implemented, a rich list will not be possible to create (though currently [they do have one](https://www.coinexplorer.net/XZC/richlist)).

### Bitcoin Mixers

All Bitcoin transactions are visible on the blockchain and there is a [ Bitcoin rich list](http://www.bitcoinrichlist.com/top100), so Bitcoin is not private. Bitcoin is [ pseudononymous](https://bitcoin.org/en/you-need-to-know), not anonymous. 

For **Bitcoin mixers** , you have to trust that they can keep their data safe and are not owned by or cooperating with a government, hackers, or other entities. 

In July of 2017, the founder of the largest Bitcoin mixing service, BITMIXER.IO, announced that they were closing and gave this as their reason: 

> … Now I grasped that Bitcoin is transparent non-anonymous system **by design**. Blockchain is a great open book… 
> 
> BITMIXER.IO, in an announcement of closing on [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (emphasis in the original). 

… Now I grasped that Bitcoin is transparent non-anonymous system **by design**. Blockchain is a great open book… 

… Now I grasped that Bitcoin is transparent non-anonymous system **by design**. Blockchain is a great open book… 

BITMIXER.IO, in an announcement of closing on [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (emphasis in the original). 

A few weeks later, after considering the various privacy-centric coins, he said this: 

> After the deep investigation I confirm that MONERO is the best privacy currency. So I strongly recommend MONERO for all people who need extra privacy. 
> 
> BITMIXER.IO, in a [ followup post](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

After the deep investigation I confirm that MONERO is the best privacy currency. So I strongly recommend MONERO for all people who need extra privacy. 

After the deep investigation I confirm that MONERO is the best privacy currency. So I strongly recommend MONERO for all people who need extra privacy. 

BITMIXER.IO, in a [ followup post](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Since all Bitcoin transactions are visible on the blockchain, ALL Bitcoin transactions can be traced. A Bitcoin mixer can highly obfuscate transactions, making it much more difficult for someone to trace the Bitcoins, but not impossible. As technology progresses and companies which specialize in tracing Bitcoin transactions become more prevalent, once highly-obfuscated transactions will become relatively easily traceable: 

  * [ Law Enforcement Continues to Invest in Bitcoin Tracking Services ](https://news.bitcoin.com/law-enforcement-continues-invest-bitcoin-tracking-services/)
  * [ Time.com: Bitcoins Are Easier to Track Than You Think ](http://time.com/3689359/bitcoins-track-anonymous/)
  * [ Elliptic: A Company Specializing in Tracing Bitcoin for Law Enforcement ](https://www.elliptic.co/)

A Google search will reveal dozens of articles like the ones above. And remember, any transaction that occurred at any time in the past is on the blockchain and has the potential to be traced, even if a mixing service was used. In fact, the use of a mixing service is likely to draw attention to those transactions. 

Not all Bitcoins are equal and have the same value. Some Bitcoins have been blacklisted and blocked by several entities, making those coins less valuable than the rest. If you receive Bitcoins that were used in the past for illegal purposes, then your Bitcoins could be blacklisted even though you had nothing to do with the illegal activity. Or, say a government, employer, or some other entity decides to blacklist your Bitcoins in the future, much like they do with asset freezing or confiscation. There would be nothing you could do. Since a mixer only makes it more difficult to trace your Bitcoins, this category has been marked as "not fungible." 

  * Andreas Antonopoulos, a former Bitcoin Core developer who is well-respected in the Bitcoin and other cryptocurrency communities, acknowledges the Bitcoin fungibility problem in a [ YouTube video](https://www.youtube.com/watch?v=ak1iojpiHpM&feature=youtu.be&t=33m9s). 
  * Discussion of the Bitcoin fungibility problem on [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=1190707.0)

## Summary

In our opinion, Monero is the clear choice if you're looking for a private, secure, untraceable, fungible, decentralized cryptocurrency with no trusted setup required. Anything else puts your privacy and security at risk. But don't just take our opinion. Do your own research and see for yourself. Consider that Monero is endorsed and used by entities which depend on privacy and untraceability, such as: 

  * [ SIGAINT ](https://www.reddit.com/r/Monero/comments/4xqrzd/sigaint_launches_tor_monero_node_as_its_operators/)
  * [ Purism ](https://puri.sm/posts/purism-collaborates-with-cryptocurrency-monero-to-enable-mobile-payments/)
  * [ Wikileaks ](https://shop.wikileaks.org/donate#db9)
  * AlphaBay Market (AB) was shut down in July of 2017. The [ Federal Forfeiture Complaint ](https://assets.documentcloud.org/documents/3898109/AlphaBay-Cazes-Forfeiture-Complaint.pdf) against AB shows that: 
    * **Monero is the only private and untraceable cryptocurrency:**   
"In total, from CAZES' wallets and computer agents took control of approximately $8,800,000 in Bitcoin, Ethereum, Moreno [sic], and Zcash, broken down as follows: 1,605.0503851 Bitcoin, 8,309.271639 Ethereum, 3,691.98 Zcash, _and an unknown amount of Monero._ " (bottom of p. 20 and top of p. 21, emphasis added) 
    * **Bitcoin transactions are not private and can be traced:**   
"Federal agents obtained the warrants after tracing a number of Bitcoin transactions originating with AlphaBay to digital currency accounts, and ultimately bank accounts and other tangible assets, held by CAZES and his wife." (p. 17, lines 24-26) 

  * **Monero is the only private and untraceable cryptocurrency:**   
"In total, from CAZES' wallets and computer agents took control of approximately $8,800,000 in Bitcoin, Ethereum, Moreno [sic], and Zcash, broken down as follows: 1,605.0503851 Bitcoin, 8,309.271639 Ethereum, 3,691.98 Zcash, _and an unknown amount of Monero._ " (bottom of p. 20 and top of p. 21, emphasis added) 
  * **Bitcoin transactions are not private and can be traced:**   
"Federal agents obtained the warrants after tracing a number of Bitcoin transactions originating with AlphaBay to digital currency accounts, and ultimately bank accounts and other tangible assets, held by CAZES and his wife." (p. 17, lines 24-26) 

LocalMonero does not advocate or encourage any illegal activity. 

LocalMonero does not advocate or encourage any illegal activity. 

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

  * [How CLSAG Will Improve Monero's Efficiency](/knowledge/what-is-clsag)/

  * [Why Monero Has a Tail Emission](/knowledge/monero-tail-emission)/

  * [A Brief History of Monero](/knowledge/monero-history)/

  * [Wired Magazine Is Wrong About Monero, Here's Why](/knowledge/wired-article-debunked)/

  * [Top 15 Monero Myths and Concerns Debunked](/knowledge/monero-myths-debunked)/

  * [How Dandelion++ Keeps Monero's Transaction Origins Private](/knowledge/monero-dandelion)/

  * [Why Monero Is Open Source and Decentralized](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: What Makes RandomX So Special](/knowledge/monero-mining-randomx)/

Further reading