---
title: "Les balises de vue : comment un octet réduira les temps de synchronisation du portefeuille Monero de plus de 40%"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
L'une des plaintes les plus courantes concernant l'utilisation quotidienne de Monero est le temps nécessaire pour synchroniser un portefeuille avant de pouvoir envoyer du Monero. Heureusement, les développeurs et les chercheurs de la communauté Monero ont trouvé un moyen brillant de réduire le temps nécessaire pour synchroniser votre portefeuille de plus de 40% sans aucune augmentation de la taille de la blockchain, frais, etc.

Ce sont « les balises de vue », un ajout d'un octet aux données de chaque transaction - à venir sur Monero lors de la prochaine mise à jour du réseau !

## Pourquoi la synchronisation du portefeuille sur Monero est-elle plus lente que celle sur Bitcoin ?

## Pourquoi la synchronisation du portefeuille sur Monero est-elle plus lente que celle sur Bitcoin ?

L'une des premières questions auxquelles nous devons répondre pour mieux comprendre le besoin d'une solution comme les balises de vue est pourquoi la synchronisation du portefeuille de Monero est plus lente que pour les crypto-monnaies comme Bitcoin.

Dans Bitcoin, comme toutes les transactions ne sont pas confidentielles et révèlent les jetons dépensés, les montants et les adresses impliquées sur la chaîne, les portefeuilles Bitcoin peuvent simplement rechercher les sorties de transactions non dépensées (UTXO) ou les adresses utilisées par un portefeuille donné, scannant rapidement la blockchain uniquement pour les UTXO appartenant à ces adresses afin de déterminer quels jetons appartiennent à votre portefeuille et peuvent être dépensés.

Dans Monero, cependant, toutes les transactions préservent la confidentialité de l'utilisateur en masquant l'expéditeur, le destinataire et les montants impliqués dans chaque transaction. Cette confidentialité, bien que vitale pour protéger les utilisateurs du réseau, introduit également une synchronisation plus lente du portefeuille. Dans Monero, votre portefeuille doit comparer chaque sortie de transaction (TXO) qui existe sur le réseau avec les clés privées de votre portefeuille.

Cette comparaison implique beaucoup de calculs et de cryptographie complexes pour valider qu'une sortie est vraiment la vôtre, puisque tous les montants, adresses et sorties (ou jetons) dépensées connues sont cachées sur la blockchain de Monero.

## Que sont les « balises de vue » ?

## Que sont les « balises de vue » ?

Afin d'aider à réduire le temps de synchronisation des portefeuilles Monero, [un chercheur nommé UkoeHB a proposé une nouvelle approche](https://github.com/monero-project/research-lab/issues/73) \- ajouter une « balise » de 1 octet à chaque transaction en utilisant un secret partagé connu uniquement à l'expéditeur et au destinataire de cette transaction.

Ce secret partagé est généré par l'expéditeur à l'aide de l'adresse qui lui est fournie par le destinataire, et ne nécessite aucune collaboration active de l'expéditeur et du destinataire. Le premier octet (ou caractère) de ce secret partagé est ensuite ajouté aux données de la transaction lors de sa publication sur le réseau Monero.

Lorsque l'un des participants à cette transaction souhaite synchroniser son portefeuille avec la blockchain Monero par la suite, au lieu d'avoir à effectuer tous les calculs complexes et la cryptographie pour chaque TXO sur le réseau, le portefeuille peut désormais simplement vérifier ce champ de 1 octet dans chaque transaction et ensuite seulement effectuer la vérification fastidieuse sur les transactions qui ont cette balise - 1/256 TXO sur le réseau, pour être précis !

Cette balise ne révèle aucune information sur la transaction aux examinateurs extérieurs, n'ajoute qu'un octet (une quantité négligeable) à la taille des transactions, et nous permet pourtant de réduire les temps de synchronisation de plus de 40% en réduisant les vérifications complexes au strict nécessaire !

## Les balises de vue : un exemple simplifié

## Les balises de vue : un exemple simplifié

Imaginez que vous avez 4 096 boîtes dans une pièce, dont seulement 5 boîtes vous appartiennent. Les boîtes sont toutes entièrement indiscernables de l'extérieur, et la seule façon de savoir si une boîte est pour vous est de l'ouvrir et de résoudre un problème mathématique chronophage écrit à l'intérieur pour vous assurer qu'elle vous appartient.

Maintenant, imaginez que vous décidiez que la personne qui vous envoie ces 5 boîtes génère un code spécial à l'aide de votre adresse, puis que vous ne mettiez que le premier caractère de ce code généré sur l'extérieur de chaque boîte qui vous est envoyée. Tout le monde fait la même chose pour leurs boîtes (pour s'assurer que toutes les boîtes sont toujours indiscernables), mais maintenant vous pouvez simplement regarder le code à un caractère à l'extérieur de la boîte et n'ouvrir que les boîtes qui ont ce caractère dessus.[

Bien que d'autres boîtes correspondent à votre code, même certaines qui ne vous appartiennent pas, le nombre de boîtes que vous avez besoin d'ouvrir et résoudre un problème mathématique n'est plus que de 16 (1/256 boîtes !) au lieu de 4 096. 

Maintenant, ouvrez ces 16 boîtes, résolvez les problèmes mathématiques et conservez les 5 boîtes qui vous appartiennent réellement dans ce groupe !

## Quand les balises de vue seront-elles disponibles dans Monero ?

## Quand les balises de vue seront-elles disponibles dans Monero ?

Les balises de vue sont l'une des fonctionnalités actuellement prévues pour être incluses dans la [prochaine mise à jour du réseau](https://github.com/monero-project/meta/issues/630), et devraient être publiées au cours du printemps. La communauté [a fait une levée de fonds de 23,3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (au moment de la rédaction) pour encourager le développement et la mise en œuvre des balises de vue, et par conséquent la grande majorité du travail pour inclure les balises de vue dans la base de code Monero a déjà été complété par j-berman en collaboration avec des examinateurs et des chercheurs.

Une fois les balises de vue appliquées par le réseau, toutes les transactions envoyées après la mise à jour du réseau bénéficieront d'un temps de synchronisation du portefeuille considérablement amélioré. Vous n'aurez rien à faire de spécial pour commencer à utiliser les balises de vue, votre portefeuille préféré pour Monero commencera simplement à les utiliser automatiquement après la mise à jour du réseau ! 

## Comment puis-je en savoir plus ?

## Comment puis-je en savoir plus ?

Si cela a piqué votre curiosité à propos des balises de vue, consultez ci-dessous quelques liens supplémentaires qui approfondissent le sujet :

  * [ Réduire les temps de balayage avec une « balise de vue » de 1 octet par sortie ](https://github.com/monero-project/research-lab/issues/73)
  * [Ajouter des balises de vue aux sorties pour réduire le temps d'analyse du portefeuille](https://github.com/monero-project/monero/pull/8061)

Ressources complémentaires

  * [Comment Monero favorise de manière unique les économies circulaires](/knowledge/monero-circular-economies)/

  * [Les signatures de cercle de Monero face à CoinJoin comme dans Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Pourquoi (et comment !) vous devriez détenir vos propres clés](/knowledge/hold-your-keys)/

  * [Contribuer à Monero](/knowledge/contributing-to-monero)/

  * [Comment les nœuds distants affectent la confidentialité de Monero](/knowledge/remote-nodes-privacy)/

  * [Comment Monero utilise les « hard -forks » pour mettre à jour le réseau](/knowledge/network-upgrades)/

  * [P2Pool et son rôle dans la décentralisation du minage sur Monero](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis : ce qu'il apportera à Monero](/knowledge/seraphis-for-monero)/

  * [La conversion de Bitcoin en Monero est-elle aussi privée que l'achat direct de Monero ?](/knowledge/most-private-way-to-buy-monero)/

  * [Pourquoi Monero utilise une configuration sans confiance contrairement à Zcash](/knowledge/monero-trustless-setup)/

  * [Pourquoi Monero est une meilleure réserve de valeur que Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Comment Monero peut surmonter les effets de réseau de Bitcoin](/knowledge/network-effect)/

  * [Pourquoi Monero a la communauté qui a la pensée la plus critique](/knowledge/critical-thinking)/

  * [Escroqueries à surveiller lors de l'utilisation de Monero](/knowledge/monero-scams)/

  * [Comment les échanges atomiques fonctionneront avec Monero](/knowledge/monero-atomic-swaps)/

  * [Ce que chaque utilisateur de Monero doit savoir concernant le réseau](/knowledge/monero-networking)/

  * [Comment RingCT masque les montants des transactions Monero](/knowledge/monero-ringct)/

  * [Comment les adresses furtives de Monero protègent votre identité](/knowledge/monero-stealth-addresses)/

  * [Comment les sous-adresses Monero empêchent la mise en correspondance d'identités](/knowledge/monero-subaddresses)/

  * [Explication des sorties Monero](/knowledge/monero-outputs)/

  * [Les meilleures pratiques d'utilisation de Monero pour les débutants](/knowledge/monero-best-practices)/

  * [Comment les signatures de cercle masquent les sorties de Monero](/knowledge/ring-signatures)/

  * [Comment Monero a résolu le problème de taille des blocs dont souffre Bitcoin](/knowledge/dynamic-block-size)/

  * [Comment CLSAG améliorera l'efficacité de Monero](/knowledge/what-is-clsag)/

  * [Pourquoi Monero a une émission résiduelle](/knowledge/monero-tail-emission)/

  * [Une brève histoire de Monero](/knowledge/monero-history)/

  * [Wired Magazine se trompe sur Monero, voici pourquoi](/knowledge/wired-article-debunked)/

  * [Démystification des 15 principaux mythes et inquiétudes au sujet de Monero](/knowledge/monero-myths-debunked)/

  * [Comment Dandelion++ garde les origines des transactions de Monero privées](/knowledge/monero-dandelion)/

  * [Pourquoi Monero est Open Source et décentralisé](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Le minage de Monero : ce qui rend RandomX si spécial](/knowledge/monero-mining-randomx)/

  * [Pourquoi Monero est meilleur que Dash, Zcash, Zcoin (même avec Lelantus), Grin et les mélangeurs Bitcoin comme Wasabi (mis à jour en mai 2020)](/knowledge/why-monero-is-better)/

Ressources complémentaires