---
title: "Comment les signatures de cercle masquent les sorties de Monero"
slug: "ring-signatures"
date: "2020-09-08"
image: "/images/rings.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero est connu dans tout le paysage des crypto-monnaies comme étant le roi de la confidentialité. Bien que tout le monde sache que Monero offre une bonne confidentialité, peu comprennent comment la confidentialité fonctionne.

De nombreuses autres crypto-monnaies proposant un haut niveau de confidentialité publient des infographies avec des tableaux de comparaison, qui répertorient les noms de la technologie de confidentialité de chaque crypto-monnaie, et dans la plupart, elles qualifient la technologie de Monero avec seulement « RingCT », mais ce n'est que partiellement vrai. Monero a en fait une approche à trois volets de la confidentialité. Une technologie pour masquer le destinataire d'une transaction, une pour masquer le montant envoyé et une pour masquer la sortie utilisée, ce sont respectivement les adresses furtives, RingCT et les signatures de cercle.

Cette approche à trois volets signifie que si l'une des technologies est cassée, les autres ne partagent pas nécessairement le même sort. Les signatures de cercle sont le maillon le plus faible du système de confidentialité ; le mot faible signifiant ici que ce maillon est le plus sensible aux attaques heuristiques. Prenons un peu de temps pour les explorer, d'accord ?

Comme mentionné ci-dessus, le but des signatures de cercle est de masquer une sortie utilisée dans une transaction. Si la terminologie « entrée/sortie » de la crypto-monnaie est confuse pour vous, ne vous inquiétez pas. Ce n'est en fait pas si compliqué. Lorsque vous entendez « sortie », pensez simplement à une vérification. Une de ces choses, qui ne sont plus si courantes, avec lesquelles les gens payent. Comme un chèque, il peut être libellé de n'importe quel montant - 10€, 32,50€, etc. - et est échangé entre les parties lors d'une transaction. Pour les crypto-monnaies, les sorties remplissent ces fonctions.

Lorsque quelqu'un vous paie 10 Monero, vous recevez une sortie de 10 XMR. Cette sortie a une valeur (10) et correspond à ce qui est prélevé sur le portefeuille de l'expéditeur, de la même manière que lorsque vous payez pour un service, un billet quitte votre portefeuille physique et est remis à la personne auprès de laquelle vous achetez.

La façon dont la sortie est masquée consiste à construire un cercle (d'où le nom) de sorties leurres. Mais ces leurres ne sont pas de « fausses sorties ». Ce sont de véritables sorties passées de la blockchain qui n'ont rien à voir avec la transaction actuelle, mais pour un observateur extérieur, chacune de ces sorties peut sembler tout aussi probable que la vraie. La taille de l'ensemble des sorties leurres, plus la vraie, s'appelle la taille du cercle, et actuellement celle de Monero est de onze. Il y a donc dix sorties leurres et une vraie.

Pourquoi ne pas simplement augmenter ce nombre à 100 ou même 1 000 ? Plus il y en a, mieux c'est, n'est-ce pas ? Eh bien, du point de vue de la confidentialité, oui, mais il y a d'autres choses à considérer. Revenons à un exemple physique pour y voir plus clair. Si vous vouliez cacher l'une de vos pièces de un euro parmi dix leurres, vous auriez besoin d'avoir environ onze euros dans votre portefeuille pour chaque euro que vous voudriez dépenser. Une vraie pièce et dix fausses. Cela devient déjà assez lourd si vous voulez dépenser ne serait-ce que quelques euros. Imaginez maintenant que nous augmentions le montant du leurre à 1000. Pour chaque euro que vous souhaitez dépenser, vous auriez besoin de transporter environ 1001 euros. Vous auriez besoin de transporter une mallette juste pour acheter une barre chocolatée ! Il est important de noter que les signatures de cercle ne fonctionnent pas tout à fait de cette façon. Par exemple, les leurres eux-mêmes ne font pas partie de la signature, seulement des références à eux, mais nous espérons que cette analogie pourra être quelque peu utile pour décrire les concepts de base.< /p>

Les leurres sur la blockchain fonctionnent de la même manière. Chaque leurre ajouté augmente le temps et le coût de vérification de la transaction. Chaque nœud doit télécharger la totalité de la signature de cercle pour chaque transaction, et chaque signature de cercle contient la sortie réelle, ainsi que les leurres. Non seulement cela, mais il doit vérifier mathématiquement qu'au moins une de ces sorties est réelle, et le temps de vérification mathématique augmente également avec chaque leurre. Cela signifie que nous devons trouver un juste milieu, où la taille du cercle est suffisamment grande pour masquer de manière adéquate la sortie réelle, même contre de nombreuses attaques heuristiques, mais suffisamment petite pour ne pas provoquer une augmentation massive de la blockchain. Il ne suffit pas de choisir un nombre arbitraire, ou simplement d'augmenter la taille du cercle lorsque nous réduisons la signature (comme avec CLSAG). La communauté Monero veut des preuves mathématiques concrètes sur lesquelles la taille du cercle offre les meilleurs compromis. Un nombre trop petit, et la confidentialité ne sera pas assez forte contre les attaques heuristiques. Trop grand, et nous n'obtenons peut-être qu'un avantage marginal du côté de la confidentialité, et souffrons inutilement en ce qui concerne le passage à l'échelle.

Il reste une dernière chose à mentionner. Certaines publications de Monero simplifient et disent que les signatures de cercle cachent l'expéditeur, mais ce n'est pas tout à fait vrai, et la différence n'est pas minime. La différence entre l'expéditeur (un être humain) et une sortie (un jeton de crypto-monnaie) est importante lorsqu'il s'agit de préserver la confidentialité. Bien qu'une sortie puisse avoir des liens avec un expéditeur, une sortie elle-même n'est pas égale à un expéditeur. Ainsi, même si une signature de cercle devait être brisée, elle n'est pas nécessairement liée à l'identité d'une personne, et le montant et le destinataire sont toujours cachés, ce qui minimise les dommages causés à la confidentialité de toutes les parties.

Cela ne veut pas dire qu'une signature de cercle brisée est insignifiante. Toute métadonnée divulguée est dangereuse et a le potentiel de révéler plus d'informations que nous ne le pensons, en particulier lorsqu'elle est utilisée conjointement avec d'autres métadonnées. Nous faisons donc de notre mieux pour nous assurer que la taille du cercle choisie repose sur une rigueur académique derrière la décision, que d'autres fuites de métadonnées sont minimisées et que l'utilisateur expérimente par défaut les meilleures actions possibles.

Mais si la probabilité d'une signature cassée vous inquiète toujours, eh bien, il y a des nouvelles incroyables à l'horizon. La prochaine génération de protocoles de confidentialité sur lesquels on travaille, tels que Triptych, Arcturus et Lelantus, ont des capacités vraiment intéressantes. Dans ces protocoles, la taille évolue de manière logarithmique, et non linéaire, à mesure que la taille du cercle augmente. Cela signifie que nous pouvons utiliser 100 leurres, mais l'espace utilisé est plus proche de la taille de cercle 10 dans l'ancienne technologie. C'est toute la différence, et cela améliorera considérablement la confidentialité tout autour.

Dans le jeu du chat et de la souris qu'est la confidentialité, Monero innove en permanence pour garder une longueur d'avance et garantir la meilleure confidentialité pratique pour tous.

Les leurres sur la blockchain fonctionnent de la même manière. Chaque leurre ajouté augmente le temps et le coût de vérification de la transaction. Chaque nœud doit télécharger la totalité de la signature de cercle pour chaque transaction, et chaque signature de cercle contient la sortie réelle, ainsi que les leurres. Non seulement cela, mais il doit vérifier mathématiquement qu'au moins une de ces sorties est réelle, et le temps de vérification mathématique augmente également avec chaque leurre. Cela signifie que nous devons trouver un juste milieu, où la taille du cercle est suffisamment grande pour masquer de manière adéquate la sortie réelle, même contre de nombreuses attaques heuristiques, mais suffisamment petite pour ne pas provoquer une augmentation massive de la blockchain. Il ne suffit pas de choisir un nombre arbitraire, ou simplement d'augmenter la taille du cercle lorsque nous réduisons la signature (comme avec CLSAG). La communauté Monero veut des preuves mathématiques concrètes sur lesquelles la taille du cercle offre les meilleurs compromis. Un nombre trop petit, et la confidentialité ne sera pas assez forte contre les attaques heuristiques. Trop grand, et nous n'obtenons peut-être qu'un avantage marginal du côté de la confidentialité, et souffrons inutilement en ce qui concerne le passage à l'échelle.

Il reste une dernière chose à mentionner. Certaines publications de Monero simplifient et disent que les signatures de cercle cachent l'expéditeur, mais ce n'est pas tout à fait vrai, et la différence n'est pas minime. La différence entre l'expéditeur (un être humain) et une sortie (un jeton de crypto-monnaie) est importante lorsqu'il s'agit de préserver la confidentialité. Bien qu'une sortie puisse avoir des liens avec un expéditeur, une sortie elle-même n'est pas égale à un expéditeur. Ainsi, même si une signature de cercle devait être brisée, elle n'est pas nécessairement liée à l'identité d'une personne, et le montant et le destinataire sont toujours cachés, ce qui minimise les dommages causés à la confidentialité de toutes les parties.

Cela ne veut pas dire qu'une signature de cercle brisée est insignifiante. Toute métadonnée divulguée est dangereuse et a le potentiel de révéler plus d'informations que nous ne le pensons, en particulier lorsqu'elle est utilisée conjointement avec d'autres métadonnées. Nous faisons donc de notre mieux pour nous assurer que la taille du cercle choisie repose sur une rigueur académique derrière la décision, que d'autres fuites de métadonnées sont minimisées et que l'utilisateur expérimente par défaut les meilleures actions possibles.

Mais si la probabilité d'une signature cassée vous inquiète toujours, eh bien, il y a des nouvelles incroyables à l'horizon. La prochaine génération de protocoles de confidentialité sur lesquels on travaille, tels que Triptych, Arcturus et Lelantus, ont des capacités vraiment intéressantes. Dans ces protocoles, la taille évolue de manière logarithmique, et non linéaire, à mesure que la taille du cercle augmente. Cela signifie que nous pouvons utiliser 100 leurres, mais l'espace utilisé est plus proche de la taille de cercle 10 dans l'ancienne technologie. C'est toute la différence, et cela améliorera considérablement la confidentialité tout autour.

Dans le jeu du chat et de la souris qu'est la confidentialité, Monero innove en permanence pour garder une longueur d'avance et garantir la meilleure confidentialité pratique pour tous.

Ressources complémentaires

  * [Comment Monero favorise de manière unique les économies circulaires](/knowledge/monero-circular-economies)/

  * [Les signatures de cercle de Monero face à CoinJoin comme dans Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Pourquoi (et comment !) vous devriez détenir vos propres clés](/knowledge/hold-your-keys)/

  * [Contribuer à Monero](/knowledge/contributing-to-monero)/

  * [Comment les nœuds distants affectent la confidentialité de Monero](/knowledge/remote-nodes-privacy)/

  * [Comment Monero utilise les « hard -forks » pour mettre à jour le réseau](/knowledge/network-upgrades)/

  * [Les balises de vue : comment un octet réduira les temps de synchronisation du portefeuille Monero de plus de 40%](/knowledge/view-tags-reduce-monero-sync-time)/

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