---
title: "Comment les nœuds distants affectent la confidentialité de Monero"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
L'un des plus grands avantages de Monero par rapport aux autres crypto-monnaies est sa confidentialité sur la chaîne en elle-même, mais vous êtes-vous déjà demandé comment la confidentialité de Monero résiste lorsque vous utilisez un nœud distant ? Et si vous utilisez un serveur avec un « portefeuille léger » comme MyMonero ?

Dans cet article, nous allons plonger dans certains des détails sur la façon dont Monero offre une confidentialité exceptionnelle sur la chaîne, même lors de l'utilisation d'un nœud distant, ainsi que ce qu'il faut surveiller lors de l'utilisation de nœuds distants.

## Quelle fonction les nœuds remplissent-ils dans Monero ?

## Quelle fonction les nœuds remplissent-ils dans Monero ?

Pour ceux qui connaissent moins bien le fonctionnement de Monero, les nœuds (ou serveurs) du réseau Monero peuvent être gérés par n'importe qui et permettre au propriétaire du nœud - ou à d'autres avec qui il choisit de le partager ! – de synchroniser une copie de la blockchain et mettre cette copie à disposition des autres sur le réseau. Ces nœuds vérifient également toutes les transactions qui se produisent sur le réseau, ainsi que tous les blocs qui sont publiés et s'assurent qu'ils suivent tous les règles définies par consensus.

L'autre fonction que les nœuds ont dans Monero est de fournir toutes les données dont votre portefeuille Monero préféré a besoin pour vérifier correctement les transactions qui vous appartiennent et effectuer de nouvelles transactions. Ces données sont fournies par les nœuds de deux manières :

  * Les données de chaque bloc de la blockchain sont demandées par le portefeuille, analysées pour les transactions vous appartenant, puis supprimées une fois vérifiées par le portefeuille. 
    * Cette étape sera bientôt considérablement améliorée, grâce aux « [view tags](/knowledge/view-tags-reduce-monero-sync-time) » (un marquage particulier que seul votre portefeuille peut reconnaître).
  * Lors de l'envoi de transactions, le nœud que vous utilisez fournit une liste de leurres possibles (ou fausses entrées) à utiliser lors de la création de la transaction, garantissant que vous avez un bon camouflage chaque fois que vous dépensez du Monero. 
    * Ces leurres font partie des [signatures de cercle](/knowledge/ring-signatures), un élément important de l'approche de Monero en matière de confidentialité sur la chaîne.

  * Cette étape sera bientôt considérablement améliorée, grâce aux « [view tags](/knowledge/view-tags-reduce-monero-sync-time) » (un marquage particulier que seul votre portefeuille peut reconnaître).

  * Ces leurres font partie des [signatures de cercle](/knowledge/ring-signatures), un élément important de l'approche de Monero en matière de confidentialité sur la chaîne.

## Quelle est la manière la plus privée et la plus sécurisée d'utiliser Monero ?

## Quelle est la manière la plus privée et la plus sécurisée d'utiliser Monero ?

La meilleure chose à faire, même avec la forte confidentialité sur la chaîne fournie par Monero lors de l'utilisation de nœuds distants, est d'exécuter votre propre nœud Monero pour vous assurer que vous avez une copie intacte de la blockchain Monero à portée de main et que votre adresse IP soit bien protégée. L'autre avantage lorsque vous exécutez votre propre nœud est que vous pouvez contribuer au réseau, en laissant d'autres nœuds se synchroniser à partir du votre ou même en laissant d'autres utilisateurs s'y connecter avec leurs portefeuilles.

Cela étant dit, Monero offre toujours une excellente confidentialité lors de l'utilisation d'un nœud distant. Si vous êtes intéressé par la gestion de votre propre nœud Monero, voici un guide facile à suivre pour le faire :

  * [Gérer un nœud Monero](https://sethforprivacy.com/guides/run-a-monero-node/)

## Qu'est-ce qu'un nœud distant peut apprendre sur moi ?

## Qu'est-ce qu'un nœud distant peut apprendre sur moi ?

Lorsque vous utilisez un nœud distant, il y a quelques informations clés qui lui sont exposées et quelques principales techniques par lesquelles ce nœud peut vous attaquer, vous empêcher d'effectuer des transactions, et plus encore.

La première chose qu'un nœud distant peut apprendre sur vous est votre adresse IP publique. Bien que cela soit, espérons-le, caché via un VPN ou Tor, le nœud distant pourrait associer votre adresse IP publique à la transaction, les aidant à déterminer d'où vous effectuez la transaction. Le nœud distant peut également apprendre le dernier bloc synchronisé par votre portefeuille et utiliser cette information pour essayer de faire des suppositions éclairées sur vous, par exemple quand vous utilisez normalement Monero et quand vous avez dépensé du Monero pour la dernière fois. Cela est particulièrement vrai si vous venez toujours de la même adresse IP (comme votre domicile). Aussi, un nœud distant peut apprendre sur vous des informations de base sur les transactions que vous lui envoyez. Bien qu'il s'agisse des données les plus évidentes que l'opérateur du nœud distant obtient à votre sujet, il est important de comprendre que cela pourrait être utilisé pour aider à retrouver l'expéditeur de la transaction lors de la combinaison de ces informations avec d'autres données hors chaîne. Cela peut être particulièrement dangereux si le nœud distant est géré par une entité malveillante, une société d'analyse de blockchain ou un État-nation oppressif.

Un nœud distant peut également tenter de vous causer des problèmes en vous cachant des blocs, faisant croire à votre portefeuille qu'il a été synchronisé alors qu'il ne l'était pas. Cela peut vous faire penser que des fonds sont perdus ou vous empêcher de dépenser des fonds jusqu'à ce que vous vous connectiez à un autre nœud. La dernière technique majeure de malveillance qu'un nœud distant pourrait faire est de fournir à votre portefeuille une liste manipulée de leurres. Cela pourrait empêcher votre portefeuille de créer des transactions (vous empêchant ainsi de dépenser des fonds), ou pourrait permettre au nœud distant d'essayer de fournir des leurres dont il sait qu'ils sont dépensés pour réduire l'anonymat sensé vous couvrir pour chaque transaction.

## Quelles garanties de confidentialité existent encore lors de l'utilisation d'un nœud distant ?

## Quelles garanties de confidentialité existent encore lors de l'utilisation d'un nœud distant ?

Bien que cet article vous ait peut-être un peu effrayé, il est important de réaliser que la confidentialité fournie par Monero est excellente même lors de l'utilisation d'un nœud distant, et dépasse de loin toute autre crypto-monnaie lorsqu'elle est utilisée de cette façon. Vous bénéficiez toujours de la forte confidentialité en chaîne fournie par Monero, car le nœud distant ne connaît jamais la véritable entrée (quels jetons vous dépensez), le montant de Monero dépensé dans la transaction ou l'adresse du destinataire de la transaction. Les observateurs extérieurs ne peuvent pas non plus voir la véritable entrée, le montant ou les adresses impliquées (quel que soit le type de nœud que vous choisissez d'utiliser !), garantissant qu'en dehors du nœud distant, même votre adresse IP, les informations de synchronisation du portefeuille et les transactions ont de solides garanties de confidentialité. .

Le nœud distant n'a également jamais accès aux transactions précédentes que vous avez envoyées ou reçues ou au montant de Monero actuellement dans votre portefeuille, et perd toute visibilité sur vos transactions dès que vous commencez à utiliser un autre nœud. Aucune clé privée (qu'il s'agisse de clés de dépense ou de vue) n'est jamais fournie au nœud distant, et votre portefeuille reste donc privé, sécurisé et utilisable. Quel que soit le nœud distant, vous ne risquez jamais non plus de perdre votre solde Monero ou de vous le faire voler, car le nœud ne peut pas modifier l'adresse du destinataire, n'a jamais accès aux clés privées de votre portefeuille et ne peut en aucun cas confisquer votre Monero.

## Que diriez-vous de "portefeuilles légers" comme MyMonero ?

## Que diriez-vous de "portefeuilles légers" comme MyMonero ?

Bien que le sujet sorte un peu du cadre de cet article, nous souhaitons aborder un type unique de portefeuille dans Monero - les portefeuilles légers. Le nom de « portefeuille léger » vient du fait que votre portefeuille (sur votre téléphone ou votre ordinateur) n'a pas à effectuer la synchronisation de la blockchain, ce qui rend l'expérience plus rapide et plus fluide.

Cependant, les portefeuilles comme celui-ci s'accompagnent pour l'instant d'un sérieux compromis en matière de confidentialité - votre portefeuille envoie la clé de vue privée au serveur distant que vous utilisez (comme la valeur par défaut dans MyMonero), donnant au serveur distant une visibilité totale sur tous les fonds reçus depuis la création de votre portefeuille (et jusqu'à ce que vous cessiez d'utiliser ce portefeuille ou ce compte, basé sur votre phrase mnémonique). Cela réduit considérablement la confidentialité que vous obtenez vis-à-vis de l'opérateur de nœud et cela doit être abordé avec prudence.

Heureusement, la communauté Monero travaille à l'amélioration du logiciel que vous pouvez utiliser pour héberger votre propre serveur de portefeuille léger (LWS), ce qui vous permettra d'avoir une synchronisation rapide sans faire confiance à un tiers avec vos clés de vue privées - comme vous exécuterez vous-même le logiciel où votre portefeuille envoie les clés de vue privées ! 

Pour en savoir plus sur le serveur de portefeuille léger personnalisé, consultez le référentiel Github ci-dessous :

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Comment puis-je en savoir plus ?

## Comment puis-je en savoir plus ?

Si vous êtes curieux et que vous aimeriez mieux comprendre ce que sont et font les nœuds dans Monero, et que vous envisagez d'utiliser un nœud distant ou d'exécuter le vôtre, vous pouvez consulter les liens ci-dessous pour découvrir d'excellentes sources pour commencer :

  * [Monero World, une liste de nœuds distants gérés par la communauté qui peuvent être utilisés par tout le monde](https://moneroworld.com/#nodes)
  * [Gérer des nœuds Monero par Seth For Privacy, l'auteur de cet article](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, une liste de nœuds distants avec un statut vérifié fréquemment< /a>](https://monero.fail/)
  * [Comment se connecter à un nœud distant avec le portefeuille GUI](https://www.getmonero.org/fr/resources/user-guides/remote_node_gui.html)
  * [Moneropedia - Nœud distant](https://www.getmonero.org/fr/resources/moneropedia/remote-node.html)

Ressources complémentaires

  * [Comment Monero favorise de manière unique les économies circulaires](/knowledge/monero-circular-economies)/

  * [Les signatures de cercle de Monero face à CoinJoin comme dans Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Pourquoi (et comment !) vous devriez détenir vos propres clés](/knowledge/hold-your-keys)/

  * [Contribuer à Monero](/knowledge/contributing-to-monero)/

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

  * [Le minage de Monero : ce qui rend RandomX si spécial](/knowledge/monero-mining-randomx)/

  * [Pourquoi Monero est meilleur que Dash, Zcash, Zcoin (même avec Lelantus), Grin et les mélangeurs Bitcoin comme Wasabi (mis à jour en mai 2020)](/knowledge/why-monero-is-better)/

Ressources complémentaires