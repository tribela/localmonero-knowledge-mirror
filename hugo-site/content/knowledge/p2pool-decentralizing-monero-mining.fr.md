---
title: "P2Pool et son rôle dans la décentralisation du minage sur Monero"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
L'un des principaux objectifs du projet Monero est de permettre un réseau équitable, décentralisé et sécurisé grâce à de nouvelles approches innovantes de minage reposant sur la preuve de travail (PoW, « Proof of Work » en anglais), ceci étant le principal moyen de sécuriser les réseaux de crypto-monnaie aujourd'hui.

Bien qu'un algorithme de minage spécifique [comme RandomX](/knowledge/monero-mining-randomx) est extrêmement important pour cet objectif, car permettant de garantir que toute personne disposant d'un ordinateur peut contribuer de manière équitable à la sécurité du réseau, il ne résout pas les problèmes pouvant provenir de l'utilisation de « pools de minage » (rassemblement de mineurs). Le minage en pool est de loin le moyen le plus courant pour miner des crypto-monnaies aujourd'hui, y compris Monero, mais heureusement, l'émergence du minage « p2pool » change rapidement la donne.

## Qu'est-ce que le « minage en pool » ?

Le minage en pool est un moyen pour les mineurs de partager la tâche de tenter de résoudre un bloc sur le réseau, puis de se partager les récompenses de manière égale pour tous les blocs trouvés par le pool. Bien que cela aide énormément à égaliser la fréquence à laquelle les mineurs sont payés par rapport au minage de Monero en solitaire, ce n'est pas sans présenter de sérieux problèmes de centralisation.

Au fur et à mesure que chaque mineur contribue au travail du pool, il cède le contrôle de son travail et des blocs qu'il trouve au pool lui-même, en espérant que le pool partagera honnêtement et équitablement les récompenses entre tous les mineurs en fonction de la quantité de travail que chacun a effectué. Si tout se passe bien, l'opérateur du pool collecte le travail de tous les mineurs, le soumet au réseau et partage les récompenses à parts égales.

## Quel est le problème avec le « minage en pool » ?

Malheureusement, cela repose entièrement sur la confiance accordé à l'opérateur du pool et cela pourrait lui permettre d'effectuer des opérations malveillantes avec le travail effectué par les mineurs. L'opérateur du pool pourrait utiliser le travail effectué pour attaquer le réseau, tenter de doubler les fonds (si le pool est assez grand), ou simplement utiliser le travail effectué par les mineurs pour se payer et ne jamais récompenser correctement les mineurs pour leur travail.

Le plus grand risque pour le réseau est celui d'un pool (ou de plusieurs pools travaillant ensemble) ayant plus de 51% du hashrate du réseau sous leur contrôle, car il pourrait l'utiliser pour tricher et dépenser des fonds deux fois (une attaque par double dépense) ou tenter de modifier les règles du réseau.

## Qu'est-ce que P2Pool ?

P2Pool est un concept qui a été créé à l'origine en 2011 pour le minage de Bitcoin, mais il n'a jamais été largement adopté et reste pratiquement inutilisé sur Bitcoin. Heureusement, l'un des principaux développeurs derrière RandomX, SCHernykh, a passé ses vacances à trouver des solutions à certains des problèmes liés à l'implémentation Bitcoin de P2Pool et à réécrire tous les logiciels à partir de zéro.

P2Pool dans Monero permet aux mineurs de travailler ensemble sans besoin de se faire confiance pour trouver des blocs et sécuriser le réseau Monero, en utilisant un logiciel de nœud spécial pour P2Pool afin de partager le travail.

Cela se fait à l'aide d'une nouvelle blockchain (une « chaîne secondaire ») qui conserve un enregistrement du travail effectué par chaque mineur, de son adresse de portefeuille et du montant de Monero qu'il a gagné, puis verse la récompense de manière décentralisée et sans besoin de confiance. Comme cette chaîne secondaire compte beaucoup moins de mineurs, il est beaucoup plus facile de trouver et de soumettre des blocs dessus que sur le réseau principal de Monero, ce qui permet aux mineurs d'obtenir plus facilement des paiements cohérents par rapport au minage de Monero en solitaire.

## Comment P2Pool résout-il les problèmes de minage de pool ?

Dans P2Pool, il n'y a pas de pool centralisé, d'opérateur central ou de personne unique détenant les fonds et distribuant les paiements. Tout le travail effectué collectivement par ceux qui minent via P2Pool est vérifié par la blockchain P2Pool et d'autres opérateurs de nœuds pour s'assurer qu'il est légitime, et tous les mineurs sont payés immédiatement en fonction du travail qu'ils ont effectué lorsqu'un bloc est trouvé, directement à partir de la récompense associée à ce bloc trouvé.

Lorsque les mineurs choisissent d'utiliser P2Pool au lieu d'un pool centralisé, ils retirent tout pouvoir et toute confiance aux opérateurs de pool et s'assurent que leur travail contribue au bien du réseau et à leurs propres récompenses, réduisent le risque d'attaques du réseau, d'abus de leur travail, ou le vol des récompenses qui leur sont dues.

Non seulement cela les aide à protéger leurs propres intérêts, mais cela réduit également le risque que les pools centralisés peuvent représenter pour le réseau Monero dans son ensemble. L'utilisation de P2Pool aide également énormément à réduire le risque que les États-nations ou les régulateurs pourraient poser à la santé du réseau, car il n'y a pas d'opérateurs de pools centralisés sur lesquels faire pression, pas de concentration géographique de pools sur lesquels s'appuyer, ou tout autre point de pression facile qui pourrait être utilisé contre Monero.

## Quels sont les inconvénients ?

Heureusement, P2Pool dans Monero a été bien conçu et bien construit, et fonctionne extrêmement bien ! Cependant, le principal inconvénient du minage avec P2Pool est que chaque mineur qui souhaite l'utiliser doit exécuter son propre nœud Monero, ce qui rend le processus de démarrage un peu plus complexe. Cependant, ce nœud est ensuite utilisé pour calculer toutes les informations nécessaires à la construction et à la vérification des blocs, et garantit que le mineur a le contrôle total de son travail en cours. Le nœud peut également fonctionner comme un nœud distant pour le propre portefeuille des mineurs, contribuer au réseau et bien plus encore.

L'autre principale différence par rapport au minage centralisé est que les petits mineurs utilisant P2Pool auront un peu plus de « variance », ou de temps entre les paiements, qu'un grand pool centralisé -- mais c'est 's _extrêmement_ important de noter que cela ne conduira pas à gagner moins de Monero au fil du temps ! P2Pool sera tout aussi rentable, même pour les petits mineurs, au fil du temps, que les pools centralisés. Une partie de cet écart est également compensée par le fait que P2Pool a nativement 0% de frais, car il n'y a pas d'opérateur de pool centralisé dont on doit payer les services !

## Comment puis-je commencer ?

Heureusement, en raison de l'excellente conception de l'implémentation P2Pool de Monero' et des nombreuses personnes de la communauté qui ont consacré du temps pour aider à simplifier le processus de minage avec P2Pool, le démarrage devient plus simple avec le temps. Il existe plusieurs façons de commencer à miner avec P2Pool, mais comme les détails techniques dépassent le cadre de cet article, n'hésitez pas à sauter dans un lien ci-dessous en fonction de votre système d'exploitation :

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## Comment puis-je en savoir plus ?

Si cela a piqué votre curiosité concernant le minage avec P2Pool, vous pouvez jeter un œil ci-dessous pour quelques liens et explications supplémentaires sur P2Pool, comment cela fonctionne et ce que cela signifie pour Monero :

  * [Le Github officiel pour P2Pool](https://github.com/SChernykh/p2pool)
  * [La documentation officielle sur l'utilisation de P2Pool](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool est maintenant en ligne](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, une sorte d' « explorateur de blocs » pour P2Pool](https://p2pool.observer/)
  * [Monero P2Pool docker-composer](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh : Sur son développement de P2Pool, un pool de minage XMR décentralisé](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

Ressources complémentaires

  * [Comment Monero favorise de manière unique les économies circulaires](/knowledge/monero-circular-economies/)

  * [Les signatures de cercle de Monero face à CoinJoin comme dans Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Pourquoi (et comment !) vous devriez détenir vos propres clés](/knowledge/hold-your-keys/)

  * [Contribuer à Monero](/knowledge/contributing-to-monero/)

  * [Comment les nœuds distants affectent la confidentialité de Monero](/knowledge/remote-nodes-privacy/)

  * [Comment Monero utilise les « hard -forks » pour mettre à jour le réseau](/knowledge/network-upgrades/)

  * [Les balises de vue : comment un octet réduira les temps de synchronisation du portefeuille Monero de plus de 40%](/knowledge/view-tags-reduce-monero-sync-time/)

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