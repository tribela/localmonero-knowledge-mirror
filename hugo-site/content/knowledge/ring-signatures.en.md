---
title: "How Ring Signatures Obscure Monero's Outputs"
slug: "ring-signatures"
date: "2020-09-08"
image: "/images/rings.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero is known far and wide across the crypto space as being the king of privacy coins. While everyone knows Monero offers good privacy, not as many understand just how the privacy operates.

Many other privacy coins publish comparison chart infographics, which list off the names of each coin’s privacy technology, and in most they label Monero’s tech as RingCT, but this is only partially true. Monero actually has a three-prong approach to privacy. One technology to hide the receiver of a transaction, one to hide the amount sent, and one to hide the output used, these are stealth addresses, RingCT, and ring signatures respectively.

This three-pronged approach means that if one of the technologies is broken, the others do not necessarily share the same fate. Ring signatures are the weakest link in the privacy scheme; the word weak here meaning the most susceptible to heuristic attacks. Let’s take some time to explore them, shall we?

As mentioned above, the goal of ring signatures is to obscure an output used in a transaction. If the 'input/output' terminology of cryptocurrency is confusing to you, don’t worry. It’s actually not that complicated. When you hear 'output' just think a check. One of those things, not quite so common anymore, that people use to pay with. Like a check, it can be denoted in any amount - $10, $32.50, etc - and is exchanged between transacting parties. For cryptocurrencies, outputs serve these functions.

When someone pays you 10 Monero, you receive a 10 XMR output. This output has a value (10), and is what is taken from the sender’s wallet, in the same way when you pay for a service, a bill leaves your physical wallet and is given to the person you are purchasing from.

The way the output is hidden is by constructing a ring (hence the name) of decoy outputs. But these decoys are not 'fake' outputs’. They are real past outputs from the blockchain that have nothing to do with the present transaction, but to an outside observer, each of these outputs might look equally probable as the real one. The size of the set of decoy outputs, plus the real one is called the ringsize, and currently Monero’s is eleven. So there are ten decoy outputs and one real one.

Why don’t we just increase this number to 100 or even 1000? The more the better, right? Well, from a privacy perspective, yes, but there are other things to consider. Let’s go back to a physical example to see what I mean. If you wanted to hide one of your dollar bills among ten decoys, you would need to carry around eleven dollars in your wallet for each dollar you wanted to spend. One real dollar, and ten fake ones. This already gets pretty cumbersome if you want to spend even a few dollars. Now imagine we increased the decoy amount to 1000. For every one dollar you wanted to spend, you would need to carry around 1001 dollars. You’d need to carry around a briefcase just to buy one candy bar! It's important to note that ring signatures don't work quite this way, for example, the decoys themselves are not a part of the signature, only references to them, but we hope this analogy can be somewhat helpful in picturing the basic concepts.

The decoys on the blockchain work similarly. Each added decoy increases the time and verification cost of the transaction. Every node has to download the entire ring signature for each transaction, and each ring signature contains the real output, as well as the decoys. Not only that, but it has to verify the math that at least one of these outputs is real, and the math verification time also increases with each decoy. This means we have to find a happy middle ground, where the ringsize is large enough to adequately obscure the real output, even against many heuristic attacks, but small enough so as not to cause the blockchain to increase at a massive rate. It’s not enough to pick an arbitrary number, or to just increase the ringsize when we make the signature smaller (such as with CLSAG). The Monero community wants concrete, mathematical evidence on which ringsize offer the best trade offs. A number too small, and the privacy will not be strong enough against heuristic attacks. Too large, and we may be getting only marginal benefit on the privacy side, and needlessly suffering in regards to scaling.

One last thing to mention. Some Monero literature simplifies and says that ring signatures hide the sender, but this is not entirely true, and the difference is not just pedantic. The difference between the sender (a human) and an output (a bill) is a big one when it comes to preserving privacy. While an output may have ties to a sender, an output itself does not equal a sender. So even if a ring signature was to be broken, it does not necessarily link to a person’s identity, and both the amount and the receiver are still hidden, minimizing the damage done to the privacy of all parties.

That’s not to say that a broken ring signature is insignificant. Any leaked metadata is bad, and does have the potential to reveal more information than we think, especially when used in conjunction with other metadata. So we do our best to ensure that the ringsize chosen has academic rigor behind the decision, other metadata leakage is minimized, and the user experiences defaults to the best possible actions.

But if the probability of a broken signature is still worrying to you, well, there is some incredible news on the horizon. The next generation of privacy protocols that are being worked on, such as Triptych, Arcturus, and Lelantus, have really neat capabilities. In these protocols, the size scales logarithmically, not linearly, as ringsize increases. This means that we can fit 100 decoys, but the space used is closer to ringsize 10 in the old tech. That’s quite the difference, and will significantly improve privacy all around.

In the cat and mouse game that is privacy, Monero continuously innovates to stay ahead of the curve and ensure the best practical privacy for all.

Further reading