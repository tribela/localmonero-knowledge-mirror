---
title: "How Dandelion++ Keeps Monero's Transaction Origins Private"
slug: "monero-dandelion"
date: "2020-04-28"
image: "/images/dandelion.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Privacy as priority

As a cryptocurrency, Monero might seem very boring to the naked eye. It doesn’t have a big claim to fame such as being a ‘world computer’ or ‘revolutionizing xyz industry’. It’s just trying to be a private, digital, fungible money, and every upgrade and new technology just furthers this end. 

Those that deem this goal as too narrow or uninteresting generally don’t understand how difficult it is to achieve meaningful privacy, especially on a permanent, open ledger like a blockchain. Any avenue for metadata leakage is a potential for privacy erosion.

Monero takes precautions to obfuscate on-chain data, such as the receiver, sender, and amounts, via stealth addresses, ring signatures, and Pedersen commitments respectively. This minimizes the chances of a casual observer from deducing critical info after transactions have already been sent and are now just a part of recorded history. There are, however some attacks that can be done the moment a transaction occurs that cannot be performed any time later.

## Attack to reveal IP address

## The mitigation(s)

Further reading