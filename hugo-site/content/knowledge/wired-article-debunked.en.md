---
title: "Wired Magazine Is Wrong About Monero, Here's Why"
slug: "wired-article-debunked"
date: "2020-06-24"
image: "/images/wired.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
In both the privacy and cryptocurrency spheres, misinformation often runs rampant. We have [an article outlining fifteen common incorrect or outdated assumptions about Monero](/knowledge/monero-myths-debunked), but we want to take time to address one particular article that is often cited and circulated by Monero skeptics.

The Wired publication put out [an article](https://www.wired.com/story/monero-privacy/) on the 27th of March, 2018, which itself was written in response to another fresh-off-the-press paper published by various academics titled: “An Empirical Analysis of Traceability in the Monero Blockchain”.

Though the paper was coauthored by individuals with clear conflict of interest (read: they are advisors to, and have a stake in Zcash), the paper was moderately well-received by the Monero community as confirming things the community has already known and written about in their own Monero Research Lab papers ([MRL-0001](https://web.getmonero.org/resources/research-lab/pubs/MRL-0001.pdf) and [MRL-0004](https://web.getmonero.org/resources/research-lab/pubs/MRL-0004.pdf)) the earliest of which was published four years prior. There were also several frustrations with it however, chiefly the conflict of interest, the fact that the issues were already known, discussed and – in some cases – remedied, and the gross mischaracterization of Monero’s privacy guarantees at the time. The community commented on the preprint of the work, and many of their recommendations made it through to the final paper.

But what exactly was mischaracterized? The fact that Monero had not had the flaws discussed in the paper for over a year. Transactions pre-2017 were indeed vulnerable to a form of privacy leakage, but at the time of publishing, Monero had addressed most of the concerns. To be fair to the authors, they discuss Monero’s remedies to a small degree, but not enough to influence the effect it had on the cryptocurrency media cycle at the time. Hence the Wired article.

While we can examine the Wired article in question as a period piece, and how true or untrue it was at the time, the fact that it is still being shared today as reasoning for why Monero’s privacy guarantees are weak actually invite an analysis on how the piece holds up in the present. We gladly take this invitation.

A quick read of the article shows several sensationalized lines, such as “[The findings] shouldn’t just worry anyone trying to stealthily spend Monero today” and the entire tone of the article which postulates the research as ‘new’, based largely off of the publication. The academic paper itself has recommendations such as warning Monero users of the potential compromise of their anonymity, despite the fact that not only had these discussions been happening since 2014, but the rallying cry of the community was for people to not buy Monero and that it was very experimental.

But what of the criticisms themselves? The reality is that many issues with Monero as a privacy coin are either no longer true of Monero, or shared concerns with privacy coins as a category of blockchain-based cryptocurrencies. Let’s begin addressing these.

One of the most often-quoted criticisms of Monero is that, because of the permanence and immutability of the blockchain, if a future technology was to break the privacy, all of Monero’s past transactions would be laid bare. In other words, your privacy has a ticking clock on it.

We cannot stress this enough. Literally every privacy coin that employs on-chain methods for obfuscation and privacy has this flaw, and yet it is often used against Monero (ironically, many times by competing privacy coins with the same problem), and is used in this article as well. The response to this criticism might be surprising to some, but Monero actually may be less vulnerable than other privacy coins to this due to the fact that it has a multi-pronged approach to privacy.

Monero hides outputs (senders), amounts, and receivers through three different technologies, ring signatures, RingCT, and stealth addresses respectively. Of these, ring signatures are the weakest, and most susceptible to both modern day heuristics and theoretical, future, privacy-breaking technologies. This has been known to the Monero community for years, and active research is underway to improve or replace the ring signature scheme entirely.

However, even if the ring signature was broken entirely, only the true output would be revealed. NOT the sender (as in individual), but the output. To couple an output with an identity is not impossible, but it would require more metadata and resources. Coupled with the fact that RingCT and the stealth address would NOT be revealed lessens the impact even further.

It should be noted that the Wired article does lightly discuss the above information in the portion where they reached out to Riccardo ‘fluffypony’ Spagni for comment, but the time given to it is brief, and almost seems to hand-wave away this crucial information. The lack of understanding is especially apparent when trying to discuss these things with people who share the article willy-nilly in the modern day.

Another criticism that’s much harder to address is in how the outside world views Monero, and how that relates with how the community around Monero views the coin. For an example of this, readers need not look farther than the title of the article itself: “The Dark Web’s Favorite Currency Is Less Untraceable Than It Seems”.

Any person who spends any significant amount of time in the Monero community can attest to the fact that the Monero community goes to great lengths to show just how hard real privacy is to achieve, even to the detriment of marketing or adoption efforts. If the community provides ample resources discussing the coin and its shortcomings accurately, at some point, the ignorance becomes the fault of the user who believes that the coin is all they need to be 100% private.

By this point it should be evident that the Monero community takes seriously both its privacy, and its honesty about the weaknesses therein and subsequent improvements. Articles, like the one in question, completely miss this spirit of innovation in Monero. It likens Monero to the droves of other cryptocurrencies that make grandiose claims, with only thought for profit and to prey on uneducated investor-wannabes.

The reality couldn’t be more different. Monero is acutely aware of its weaknesses, seeks to continue building so as to improve them, tighten up loose joints, and achieve the very real, but very hard goal of giving the world a private, fungible cryptocurrency that can be used by all, and do it all in a manner that is fair, decentralized, and community-driven. Perhaps it’s time to put away the sensationalization and article sharing as a means to shill bags and promote competitors. Perhaps it’s time to tell another story.

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

  * [Top 15 Monero Myths and Concerns Debunked](/knowledge/monero-myths-debunked)/

  * [How Dandelion++ Keeps Monero's Transaction Origins Private](/knowledge/monero-dandelion)/

  * [Why Monero Is Open Source and Decentralized](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: What Makes RandomX So Special](/knowledge/monero-mining-randomx)/

  * [Why Monero Is Better Than Dash, Zcash, Zcoin (Even With Lelantus), Grin and Bitcoin Mixers Like Wasabi (Updated May 2020)](/knowledge/why-monero-is-better)/

Further reading