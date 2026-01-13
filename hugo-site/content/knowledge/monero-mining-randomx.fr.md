---
title: "Le minage de Monero : ce qui rend RandomX si spécial"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Le 30 novembre 2019, Monero a eu son « hard fork » (ou « embranchement dur », signifiant une nouvelle version non rétro-compatible) semestriel, le changement le plus attendu étant le passage de l'ancien algorithme PoW (Proof of Work, preuve de travail), « cryptonight », au tout nouveau, développé en interne, « RandomX ». La communauté Monero pense que RandomX est un grand pas vers un minage égalitaire, mais creusons plus profondément pour voir si c'est le cas.

## Objectif

Afin de juger si RandomX est une amélioration, nous devons d'abord comprendre quel est le but du minage. Le « minage » sécurise une blockchain contre les doubles dépenses via le consensus de Nakamoto. Les subtilités exactes de la manière dont il procède dépassent le cadre de cet article, mais elles peuvent être trouvées sur de nombreuses sources sur Internet. Ce qui compte, c'est que la sécurité provienne de « hachages » générés par des ordinateurs (appelés ici mineurs), en concurrence les uns avec les autres pour trouver la solution mathématique nécessaire à la création d'un autre bloc. Ce faisant, ils ajoutent de nouvelles transactions à la blockchain. En échange de leur travail (hachages), ils sont récompensés par des jetons nouvellement générés.   
  
Un certain nombre de problèmes peuvent survenir avec cette approche, et ils nécessitent des incitations appropriées pour fonctionner correctement, mais nous allons nous concentrer sur un problème particulier qui pourrait survenir. Si le minage est censé être une compétition, que se passe-t-il lorsqu'un mineur obtient un avantage ?

## Contexte

Pour le contexte, parlons un peu du matériel de minage. Les mineurs utilisent des ordinateurs pour faire le travail, mais nous savons tous que tous les ordinateurs ne sont pas fabriqués de la même manière. Certains ordinateurs sont suffisamment puissants pour exécuter des réseaux d'IA ou des jeux intenses, tandis que d'autres ont du mal avec des tâches même simples. Ces différences de puissance de calcul affectent également le taux de hachage, ou la vitesse à laquelle ils recherchent des solutions de bloc.   
  
Mais même ces différences entre les ordinateurs sont pâles par rapport aux taux de hachage du matériel spécialisé, autrement connu sous le nom de circuits intégrés spécifiques à l'application (ASIC), qui surclassent les ordinateurs ordinaires de plusieurs ordres de grandeur.  
  
Prenons un peu de temps pour explorer ce qui rend les ASIC si puissants. Imaginez que tous les ordinateurs se situent quelque part sur un spectre, qui va de la capacité de faire beaucoup de choses, mais rien de bien, à faire une seule chose, mais de la faire très bien. Les processeurs et les ASIC se situent aux extrémités opposées de ce spectre.  
  
Les processeurs qui se trouvent dans tous les ordinateurs standard sont à la première extrémité. Ils peuvent faire beaucoup de choses, comme naviguer sur le Web, jouer à des jeux ou rendre des vidéos, mais ils ne font rien de très bien. Mais cette flexibilité se fait au détriment de l'efficacité.  
  
Les ASIC sont à l'autre bout, où ils ne peuvent qu'une chose, mais le font à un rythme incroyable. Ils ne peuvent effectuer qu'une seule fonction mathématique, mais comme ils peuvent ignorer tout le reste, les gains de performances sont astronomiques. Cependant, cette efficacité se fait au détriment de la flexibilité, donc si la fonction change même légèrement - un exemple est x + y = z passe à 2x + y = z - alors l'ASIC cessera complètement de fonctionner.   
  
Tout le monde ne possède pas un ASIC, mais tout le monde possède des ordinateurs. Cela peut conduire à un avantage injuste.

## Une analogie amusante

Si cela reste déroutant, peut-être que l'analogie suivante vous aidera. Imaginez une loterie où mille euros sont attribués toutes les heures, et cette loterie vous permet d'imprimer vos propres billets ! Vous commencez à imprimer autant de billets que vous le pouvez sur votre imprimante domestique, qui peut imprimer un billet par seconde. Après avoir soustrait les coûts d'électricité et d'encre, vous voyez que vous pouvez toujours réaliser un profit, même si vous ne gagnez à la loterie qu'une fois toutes les quelques semaines.  
  
Au fil du temps, vous développez votre activité jusqu'à ce que vous disposiez d'une salle entière dédiée aux imprimantes. 20 en tout. Tout va bien ... jusqu'au jour fatidique.  
  
Il y a une grosse nouveauté. Quelqu'un a inventé un nouveau type d'imprimante. Il ne peut imprimer que des billets de loterie. Il ne peut pas imprimer d'images, ni de documents de bureautique, ni effectuer d'impression recto verso. Seulement des billets de loterie. Mais il peut les imprimer à raison de 1000 tickets par seconde. Vous regardez dans votre petite salle d'impression. 20 imprimantes. Vous avez besoin de 980 imprimantes supplémentaires juste pour suivre UNE de ces imprimantes spécialisées, et si quelqu'un en a deux … ?  
  
Vous quittez malheureusement le jeu de loterie car vous ne pouvez plus justifier les coûts d'électricité et d'encre.  
  
Mais attendez ! Quelques semaines plus tard, il y a encore de la nouveauté ! Le modèle du billet a changé. Maintenant, les chiffres, qui étaient en haut, sont maintenant en bas. Les nouvelles imprimantes spécialisées sont si peu flexibles qu'elles ne peuvent pas prendre en compte ce nouveau modèle. Elles ne pouvaient imprimer que selon la version précédente. Il ne vous faudra pas longtemps pour imprimer à nouveau avec plaisir. Au moins jusqu'à ce que quelqu'un fabrique une nouvelle imprimante spécialisée pour le nouveau modèle.

## RandomX

Quelle est la place de RandomX dans tout cela ? Il cherche à égaliser l'avantage qu'ont les ASIC en les rendant très difficiles à fabriquer. Pour ce faire, il oblige les mineurs à créer et à exécuter du code aléatoire à la place du hachage basé sur un algorithme.  
  
Cela peut être déroutant de savoir comment cela aide réellement en quoi que ce soit, alors revenons à notre analogie avec l'imprimante. Vous souvenez-vous de ce qui s'est passé lorsque le modèle du billet a changé ? Les anciennes imprimantes spécialisées devenaient obsolètes, et de nouvelles devaient être développées pour correspondre à ce nouveau modèle. Que se passerait-il si chaque nouveau billet de loterie devait respecter un nouveau m odèle pour chaque nouveau jackpot ?   
  
Créer une nouvelle imprimante spécialisée deviendrait incroyablement difficile. Vous ne pouvez plus vous contenter d'un seul modèle de billet. Étant donné que la conception du modèle est aléatoire, les fabricants d'imprimantes spécialisées devraient ajouter des capacités de couleur, des moyens d'imprimer différents lettrages, bordures et formes, etc. En bref, la machine qu'ils finiraient par inventer serait une imprimante standard et ordinaire. Comme tout le monde.  
  
En introduisant simplement ce caractère aléatoire dans la conception du modèle des tickets, nous avons considérablement réduit l'énorme avantage tiré du matériel spécialisé. RandomX fait la même chose, mais avec le minage.  
  
De cette façon, les avantages obtenus par quelques personnes aisées sont minimisés, car s'ils investissent dans la création d'« ASIC » pour l'exploitation de RandomX, ils vont en fait simplement inventer des processeurs plus puissants et meilleurs, ce qui profite au monde entier.  
  
Cela signifie que le petit gars avec ses 20 imprimantes de tickets est de retour dans le jeu. Il sera peut-être encore en position d'infériorité puisque ces personnes fortunées peuvent toujours acheter plus d'imprimantes que lui, mais au moins maintenant, il n'est pas surclassé par plusieurs ordres de grandeur simplement à partir d'une seule machine. Il est compétitif à sa petite échelle.  
  
Sachant que même le petit gars peut être compétitif dans le minage de Monero, nous encourageons tout le monde à essayer, soit dans le portefeuille officiel Monero (version graphique ou en ligne de commande), qui prend en charge le minage en solo, soit en téléchargeant un logiciel créé et maintenu par la communauté. C'est facile, convivial et ouvert à tous.

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

  * [Pourquoi Monero a une émission résiduelle](/knowledge/monero-tail-emission)/

  * [Une brève histoire de Monero](/knowledge/monero-history)/

  * [Wired Magazine se trompe sur Monero, voici pourquoi](/knowledge/wired-article-debunked)/

  * [Démystification des 15 principaux mythes et inquiétudes au sujet de Monero](/knowledge/monero-myths-debunked)/

  * [Comment Dandelion++ garde les origines des transactions de Monero privées](/knowledge/monero-dandelion)/

  * [Pourquoi Monero est Open Source et décentralisé](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Pourquoi Monero est meilleur que Dash, Zcash, Zcoin (même avec Lelantus), Grin et les mélangeurs Bitcoin comme Wasabi (mis à jour en mai 2020)](/knowledge/why-monero-is-better)/