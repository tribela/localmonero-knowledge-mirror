---
title: "Les signatures de cercle de Monero face à CoinJoin comme dans Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Alors que les outils de augmentant la confidentialité de Bitcoin ont gagné en attention et en utilisation, ils ont fait l'objet d'un examen réglementaire plus approfondi. Cet examen minutieux a conduit à une [annonce récente](https://twitter.com/wasabiwallet/status/1503091503207432193) de la part de l'un de ces outil, Wasabi Wallet, indiquant qu'ils commenceront à censurer et à rejeter les entrées dans des mélanges qu'ils jugent illicites ou contraires à leur conditions d'utilisation, et paieront une entreprise d'analyse de la blockchain pour « vérifier » les participants entrants dans un mélange.

L'utilisation des transactions CoinJoin pour masquer la source des fonds dans Bitcoin est au cœur de la confidentialité de Bitcoin depuis de nombreuses années maintenant, et les problèmes et les risques inhérents à son utilisation sont quelques-uns des principaux problèmes que les signatures de cercle de Monero corrigent et préviennent.

Dans cet article de blog, nous allons brièvement nous plonger dans une comparaison entre CoinJoin et les signatures de cercle, ainsi que pourquoi l'approche adoptée dans Monero conduit à une plus grande résistance à la censure, une plus grande confidentialité et moins de tracas pour les utilisateurs.

## Qu'est-ce qu'une transaction CoinJoin ?

Comme toutes les transactions sont complètement transparentes dans Bitcoin - révélant l'expéditeur, le destinataire et les montants - les utilisateurs doivent prendre des mesures supplémentaires pour préserver la confidentialité des expéditeurs précédents et des futurs destinataires de leurs fonds ou risquer la censure, la surveillance ou le vol de fonds par de la violence physique.

La meilleure solution aujourd'hui pour la confidentialité sur Bitcoin est un outil appelé « [CoinJoin](https://bitcoiner.guide/qna/coinjoin/) », où 2 utilisateurs ou plus travaillent ensemble (généralement via un coordinateur centralisé) pour créer une transaction spéciale qui rend difficile pour les observateurs extérieurs de relier les entrées aux sorties. Chaque participant communique pour construire conjointement la transaction sans céder la garde de ses fonds, et reçoit à la fin une sortie dont l'historique antérieur n'est plus clair (ou obscurci) pour les observateurs extérieurs.

Cela brise l'historique d'UTXO spécifiques, permettant aux utilisateurs de Bitcoin d'obtenir un minimum de confidentialité lors des transactions. Cependant, CoinJoin (tel qu'implémenté dans Wasabi Wallet et Samourai Wallet, les deux outils CoinJoin les plus utilisés pour Bitcoin) présente quelques inconvénients majeurs :

  * Comme les transactions CoinJoin sont entièrement optionelles et nécessitent une participation active, tout participant montre nécessairement qu'il recherche une plus grande confidentialité que celle des utilisateurs « normaux » de Bitcoin, ce qui peut les isoler et causer des problèmes de dépenses dans de nombreux services d'échanges ou entités réglementées. Chaque utilisateur ne peut pas nier avoir participé à une transaction CoinJoin.
  * Afin de trouver d'autres personnes avec lesquelles participer à un CoinJoin, la plupart des approches de CoinJoin (y compris Wasabi Wallet) utilisent un coordinateur centralisé qui connecte les participants et les aide à communiquer et à construire une transaction CoinJoin appropriée. Ce coordinateur centralisé n'a jamais la garde des fonds de l'utilisateur, mais obtient un aperçu approfondi des transactions qu'il coordonne, peut censurer les entrées entrantes (comme dans le cas de Wasabi Wallet) et peut être contraint de collecter ou de partager des informations sur les participants à CoinJoin.
  * Les utilisateurs disposant de fonds importants pour CoinJoin doivent souvent attendre des heures (voire des jours !) pour trouver suffisamment de participants avec lesquels réaliser une opération CoinJoin, ce qui entraîne des retards importants entre le moment où un utilisateur reçoit des fonds et le moment où il peut les dépenser en privé. 
  * La confidentialité fournie par une transaction CoinJoin se dégrade au fil du temps, car les autres participants dépensent des fonds ou lient leurs sorties à leur identité via des échanges KYC, des marchands nécessitant une pièce d'identité, etc. Cela signifie que les utilisateurs conservent idéalement leurs fonds constamment dans les transactions CoinJoin pour garder leur ensemble d'anonymat (« foule dans laquelle se cacher ») aussi frais que possible.
  * Dans la plupart des approches de CoinJoin, les participants doivent utiliser un UTXO de taille fixe (c'est-à-dire 0,1 BTC) afin de rendre plus difficile la connexion des entrées et des sorties des transactions CoinJoin. Cela conduit à des frais plus élevés (plus de transactions séparées nécessaires par grande entrée), plus de « changement toxique » (des fonds qui ne peuvent être dépensés sans risques sérieux pour la vie privée), et peut empêcher les petits utilisateurs de pouvoir mélanger du tout s'ils n'ont pas le solde minimum requis.

## Comment les signatures de cercle résolvent-elles ces problèmes ?

Comme [nous avons examiné en profondeur ce que sont les signatures de cercle dans le passé](/knowledge/ring-signatures), nous n'entrerons pas dans les détails sur les aspects techniques de leur fonctionnement dans cet article de blog. Au lieu de cela, nous verrons comment les approches adoptées dans Monero résolvent les problèmes liés à l'utilisation de CoinJoin discutés ci-dessus.

> CoinJoin est optionnel et nécessite une participation active

CoinJoin est optionnel et nécessite une participation active

Les signatures de cercle de Monero sont une fonctionnalité essentielle du protocole de confidentialité, et _chaque_ transaction sur le réseau les utilise. Cela signifie qu'aucune transaction ne se distingue par la recherche d'une plus grande confidentialité que les utilisateurs "normaux" de Monero, et tous les utilisateurs peuvent nier de manière plausible qu'ils ont dépensé des fonds dans une transaction donnée. Comme un utilisateur dépensant des fonds ne coordonne pas ou ne participe pas aux entrées de leurrage dans une transaction, les utilisateurs qui possèdent des entrées qui se trouvent être sélectionnées comme leurres peuvent honnêtement dire qu'ils ne participaient pas à cette transaction, renforçant ainsi leur confidentialité.

> Utilisation d'un coordinateur centralisé

Utilisation d'un coordinateur centralisé

Étant donné que les signatures de cercle de Monero sont entièrement non coordonnées et ne nécessitent que le véritable dépensier des fonds pour créer la transaction, il n'est pas nécessaire d'avoir un coordinateur centralisé au sein du réseau Monero. Cela garantit que _personne_ ne peut vous refuser l'accès à la confidentialité dans Monero, et il n'y a pas d'entité centralisée sur laquelle on peut faire pression, pas d'attaques Sybil faciles contre la liquidité, etc. Tant que votre transaction paie les frais appropriés, vous obtenez un accès non censuré à la confidentialité, à la sécurité et à l'anonymat dans Monero.

> CoinJoin nécessite des liquidités

CoinJoin nécessite des liquidités

La « liquidité » disponible pour quiconque dépensant du Monero pour l'utiliser comme leurres est toujours la somme totale des sorties sur la chaîne, de sorte qu'il n'y a jamais de pénurie de leurres pour se cacher avec Monero. Une personne cherchant à dépenser du Monero peut le faire environ 20 minutes après avoir reçu les fonds et n'a pas besoin d'effectuer d'étapes supplémentaires pour obtenir une confidentialité renforcée sur le réseau Monero.

> La confidentialité de CoinJoin se dégrade avec le temps

La confidentialité de CoinJoin se dégrade avec le temps

Comme les sorties de Monero ne sont jamais dépensées par le réseau, la confidentialité fournie par les signatures de cercle est beaucoup moins susceptible de se dégrader avec le temps. Un utilisateur n'a pas besoin de générer constamment des sorties dans Monero et, en dehors de circonstances extrêmement rares, ne perd aucune confidentialité au fil du temps.

Si un utilisateur souhaite "rafraîchir" les leurres utilisés avec une sortie, il peut simplement se renvoyer les fonds et pourra les dépenser environ 20 minutes plus tard, comme d'habitude.

> CoinJoin nécessite généralement des entrées de taille fixe

CoinJoin nécessite généralement des entrées de taille fixe

Étant donné que les montants sont cachés dans chaque transaction utilisant le principe des [« Transactions Confidentielles »](/knowledge/monero-ringct) (une partie de « RingCT »), les leurres utilisés dans une transaction donnée peuvent être de n'importe quelle taille. Il n'y a aucune raison de s'inquiéter de l'heuristique basée sur le montant dans Monero, et donc les transactions sont beaucoup plus simples à construire et peuvent exploiter des leurres à tout moment et de n'importe quel montant sur la blockchain Monero.

## Comment puis-je en savoir plus ?

Si vous êtes curieux et que vous souhaitez mieux comprendre les « signatures de cercle » ou les transactions CoinJoin, consultez les liens ci-dessous pour trouver d'excellents points de départ :

  * [Comment les signatures de cercle masquent les sorties de Monero](/knowledge/ring-signatures)
  * [Signature de cercle - Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [Présentation de CoinJoin](https://6102bitcoin.com/coinjoin-overview/)

Ressources complémentaires

  * [Comment Monero favorise de manière unique les économies circulaires](/knowledge/monero-circular-economies/)

  * [Pourquoi (et comment !) vous devriez détenir vos propres clés](/knowledge/hold-your-keys/)

  * [Contribuer à Monero](/knowledge/contributing-to-monero/)

  * [Comment les nœuds distants affectent la confidentialité de Monero](/knowledge/remote-nodes-privacy/)

  * [Comment Monero utilise les « hard -forks » pour mettre à jour le réseau](/knowledge/network-upgrades/)

  * [Les balises de vue : comment un octet réduira les temps de synchronisation du portefeuille Monero de plus de 40%](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool et son rôle dans la décentralisation du minage sur Monero](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis : ce qu'il apportera à Monero](/knowledge/seraphis-for-monero/)

  * [La conversion de Bitcoin en Monero est-elle aussi privée que l'achat direct de Monero ?](/knowledge/most-private-way-to-buy-monero/)

  * [Pourquoi Monero utilise une configuration sans confiance contrairement à Zcash](/knowledge/monero-trustless-setup/)

  * [Pourquoi Monero est une meilleure réserve de valeur que Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Comment Monero peut surmonter les effets de réseau de Bitcoin](/knowledge/network-effect/)

  * [Pourquoi Monero a la communauté qui a la pensée la plus critique](/knowledge/critical-thinking/)

  * [Escroqueries à surveiller lors de l'utilisation de Monero](/knowledge/monero-scams/)

  * [Comment les échanges atomiques fonctionneront avec Monero](/knowledge/monero-atomic-swaps/)

  * [Ce que chaque utilisateur de Monero doit savoir concernant le réseau](/knowledge/monero-networking/)

  * [Comment RingCT masque les montants des transactions Monero](/knowledge/monero-ringct/)

  * [Comment les adresses furtives de Monero protègent votre identité](/knowledge/monero-stealth-addresses/)

  * [Comment les sous-adresses Monero empêchent la mise en correspondance d'identités](/knowledge/monero-subaddresses/)

  * [Explication des sorties Monero](/knowledge/monero-outputs/)

  * [Les meilleures pratiques d'utilisation de Monero pour les débutants](/knowledge/monero-best-practices/)

  * [Comment les signatures de cercle masquent les sorties de Monero](/knowledge/ring-signatures/)

  * [Comment Monero a résolu le problème de taille des blocs dont souffre Bitcoin](/knowledge/dynamic-block-size/)

  * [Comment CLSAG améliorera l'efficacité de Monero](/knowledge/what-is-clsag/)

  * [Pourquoi Monero a une émission résiduelle](/knowledge/monero-tail-emission/)

  * [Une brève histoire de Monero](/knowledge/monero-history/)

  * [Wired Magazine se trompe sur Monero, voici pourquoi](/knowledge/wired-article-debunked/)

  * [Démystification des 15 principaux mythes et inquiétudes au sujet de Monero](/knowledge/monero-myths-debunked/)

  * [Comment Dandelion++ garde les origines des transactions de Monero privées](/knowledge/monero-dandelion/)

  * [Pourquoi Monero est Open Source et décentralisé](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Le minage de Monero : ce qui rend RandomX si spécial](/knowledge/monero-mining-randomx/)

  * [Pourquoi Monero est meilleur que Dash, Zcash, Zcoin (même avec Lelantus), Grin et les mélangeurs Bitcoin comme Wasabi (mis à jour en mai 2020)](/knowledge/why-monero-is-better/)