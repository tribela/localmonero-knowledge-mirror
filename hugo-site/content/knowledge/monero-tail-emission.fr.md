---
title: "Pourquoi Monero a une émission résiduelle"
slug: "monero-tail-emission"
date: "2020-07-30"
image: "/images/emission.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Lorsque la plupart des gens pensent à ce qui distingue Monero des autres, ils pensent à la technologie de confidentialité de Monero. En effet, la plupart considéreraient la confidentialité et la fongibilité qu'elle permet comme le trait déterminant de Monero et l'arme principale qu'elle apporte sur le ring par rapport aux autres crypto-monnaies. Ce que la plupart des gens ne savent peut-être pas, c'est que Monero contient d'autres différences de protocole par rapport à Bitcoin et ses dérivés qui, selon certains, sont tout aussi importantes que les technologies de confidentialité de Monero. Dans cet article, nous allons nous intéresser à l'un d'entre eux : l'émission résiduelle.

Tout d'abord, définissons ce que signifie ce terme. Une émission résiduelle est une subvention incessante de récompenses globales, même après la frappe du « dernier » Monero. En d'autres termes, la récompense de bloc de Monero ne tombera jamais à zéro, mais tombera plutôt jusqu'à ce qu'elle atteigne 0,6 XMR par bloc, puis y restera pour toujours. Les mineurs seront toujours payés pour miner du Monero et n'auront jamais à dépendre uniquement d'un marché payant.

Mais revenons un instant en arrière et examinons le minage à un niveau très élevé. Les mineurs de Monero sont incités à sécuriser un réseau en calculant des hachages. La motivation est l'opportunité de gagner du Monero s'ils trouvent un nouveau bloc. Ce Monero est attribué de deux manières. Premièrement, le mineur reçoit les frais payés par chaque utilisateur qui a payé pour l'inclusion de sa transaction dans le bloc. Ce sont les frais de transaction que vous payez lorsque vous envoyez une transaction. Deuxièmement, le mineur reçoit une quantité prédéterminée de Monero, de la part du protocole lui-même. Dans la plupart des cas, cette « récompense globale » est nettement supérieure aux frais de transaction des utilisateurs et c'est là que les mineurs gagnent le plus d'argent. Cette récompense en bloc sert à maintenir les mineurs financièrement investis dans la sécurisation de la chaîne, mais aussi à faire circuler de nouveaux jetons.

Dans la plupart des protocoles de crypto-monnaie, cette récompense de bloc est définie pour diminuer avec le temps. La plupart des dérivés Bitcoin ont ce qu'on appelle des « halvenings », des moments prédéterminés où la récompense pour trouver un bloc est réduite de moitié (par exemple de 20 BTC à 10 BTC). Ces réductions de moitié se produisent toutes les quelques années, et chaque fois que cela se produit, la sécurité sur le réseau diminue. Pourquoi ? Eh bien, nous encourageons le lecteur à lire notre [article sur le minage et RandomX](/knowledge/monero-mining-randomx), et ce faisant, il apprendra que le minage est une course. Les récompenses de bloc ne sont remises qu'à ceux qui trouvent un bloc, et de nombreuses entités sont en concurrence pour le faire. Lorsque les récompenses sont plus élevées, plus de personnes sont intéressées à jouer à ce jeu, tandis que lorsque les récompenses sont faibles, moins de personnes, même celles qui disposent de l'équipement pour le faire, seront prêtes à utiliser leur temps et leurs ressources pour tenter de gagner un prix misérable.

Nous commençons déjà à gratter la surface de la raison de l'émission résiduelle de Monero. Monero a également une récompense de bloc décroissante, bien que contrairement à Bitcoin, il n'y ait pas de réduction de moitié. Au lieu de cela, chaque récompense de bloc est légèrement inférieure à la précédente, de sorte que la réduction est beaucoup plus fluide. Mais la question pour toutes les crypto-monnaies est : « Que se passe-t-il lorsque la récompense de bloc atteint zéro ? ». C'est une situation étrange dans laquelle, à la fois nous connaissons et ne connaissons pas la réponse. La partie que nous savons est qu'il n'y aura plus de subvention de récompense globale, ce qui signifie que les mineurs devront être motivés uniquement par les frais de transaction des utilisateurs. Ce que nous ne savons pas, c'est si ces montants seront suffisants pour permettre aux mineurs de sécuriser la chaîne.

Comme mentionné précédemment, à l'heure actuelle, la récompense globale dépasse les frais de transaction d'un montant substantiel, donc l'espoir est que, à mesure que de plus en plus d'utilisateurs utilisent la chaîne, les frais augmenteront, et avec des frais accrus, les mineurs jugeront que cela vaut la peine de continuer le minage. Il y a cependant un autre côté à ce scénario, du côté des utilisateurs. Si les frais augmentent, il deviendra alors beaucoup plus coûteux d'effectuer des transactions avec la crypto-monnaie pour tout le monde, ce qui pourrait l'empêcher de disposer de ressources monétaires suffisantes. Mais d'un autre côté, si les frais restent bas et que la récompense globale tombe à zéro, alors très peu de mineurs sécuriseront le réseau, le laissant vulnérable à une attaque des 51% et de transactions inversées.

Personne n'a de bonnes réponses à ce scénario, et aucune crypto-monnaie majeure n'est encore entrée dans cette phase de la vie de leur crypto-monnaie, nous n'avons donc aucune expérience du monde réel avec elle non plus. Tout n'est que spéculation. Un pari. Bitcoin fait le pari que les frais seront suffisants pour faire vivre les mineurs, quitte à exclure les plus démunis. Monero fait un pari différent. Monero parie que les frais à eux seuls ne suffiraient pas pour la sécurisation de la chaîne, il inclut donc une émission résiduelle dans le cadre du protocole.

Nous rappelons au lecteur que la récompense de bloc ne tombera jamais en dessous de 0,6 XMR par bloc. Cela suffira-t-il à motiver les mineurs ? Nous ne savons pas, mais c'est certainement mieux que 0, ce que presque toutes les autres crypto-monnaies ont intégré à leur protocole.

La principale critique formulée à l'encontre de cette approche est que cela signifie que l'offre de Monero est théoriquement infinie, provoquant une inflation au fil du temps, tandis que les crypto-monnaies qui plafonnent la récompense globale ont une offre finie, leur rareté augmentant la valeur au fil du temps. Nous pensons que cet argument est insuffisant pour plusieurs raisons.

Premièrement, à quoi sert une crypto-monnaie rare et de grande valeur qui est facilement attaquée, censurée et détournée en raison d'un manque de sécurité ? Au contraire, la faible sécurité diminuerait la valeur, plus que ce que pourrait apporter l'augmentation de sa rareté. Deuxièmement, bien que l'offre de Monero soit théoriquement infinie, l'inflation est linéaire et tend vers zéro en pourcentage annuel, contrairement à la monnaie fiat qui est exponentielle.

L'inflation de Monero est précisément connue à l'avance et peut être projetée avec précision, contrairement à la monnaie fiat qui peut augmenter plus ou moins sur une année donnée en fonction des caprices des pouvoirs en place. Cela préserve toujours l'esprit « cypherpunk » d'éliminer la possibilité de corruption humaine grâce à une technologie renforcée par un protocole. Avec l'avantage supplémentaire de la tranquillité d'esprit que la sécurisation de la blockchain de Monero grâce au minage sera là aussi longtemps que le monde en aura besoin.

Le dernier point que nous voulons aborder est celui de l'équité. La monnaie est utilisée de plusieurs façons, comme réserve de valeur, comme moyen d'échange et comme unité de compte. Dans un système où l'offre est finie, l'inflation s'arrêtera, ce qui signifie que ceux qui l'utilisent comme réserve de valeur utilisent le système gratuitement. Ils bénéficient de la sécurité continue fournie par les mineurs sans rien payer pour cela, car sans inflation, leur argent ne perd pas lentement de la valeur au fil du temps. À l'inverse, quiconque utilise la monnaie comme moyen d'échange est pénalisé (via des frais de transaction potentiellement élevés). Cela encouragera les gens à détenir mais pas à dépenser, et faussera l'équité du système pour favoriser les détenteurs. En ayant une émission résiduelle, cela égalise l'équation. Désormais, les détenteurs paient également une petite taxe, via l'inflation, pour la sécurité du système. L'émission résiduelle le rend plus juste pour tout le monde.

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

  * [Comment les signatures de cercle masquent les sorties de Monero](/knowledge/ring-signatures)/

  * [Comment Monero a résolu le problème de taille des blocs dont souffre Bitcoin](/knowledge/dynamic-block-size)/

  * [Comment CLSAG améliorera l'efficacité de Monero](/knowledge/what-is-clsag)/

  * [Une brève histoire de Monero](/knowledge/monero-history)/

  * [Wired Magazine se trompe sur Monero, voici pourquoi](/knowledge/wired-article-debunked)/

  * [Démystification des 15 principaux mythes et inquiétudes au sujet de Monero](/knowledge/monero-myths-debunked)/

  * [Comment Dandelion++ garde les origines des transactions de Monero privées](/knowledge/monero-dandelion)/

  * [Pourquoi Monero est Open Source et décentralisé](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Le minage de Monero : ce qui rend RandomX si spécial](/knowledge/monero-mining-randomx)/

  * [Pourquoi Monero est meilleur que Dash, Zcash, Zcoin (même avec Lelantus), Grin et les mélangeurs Bitcoin comme Wasabi (mis à jour en mai 2020)](/knowledge/why-monero-is-better)/

Ressources complémentaires