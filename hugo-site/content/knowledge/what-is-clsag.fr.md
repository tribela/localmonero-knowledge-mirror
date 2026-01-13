---
title: "Comment CLSAG améliorera l'efficacité de Monero"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
En tant que protocole, Monero est dans un état constant d'innovation. En utilisant la recherche sur les solutions en chaîne et hors chaîne, la communauté Monero recherche des domaines à améliorer pour rendre Monero plus privé, plus évolutif et plus accessible à tous. L'une des innovations les plus récentes est le remplacement du schéma de signature de cercle, MLSAG, par un remplacement direct CLSAG, qui signifie « Concise Linkable Spontaneous Anonymous Group ».

En surface, la mise en œuvre de CLSAG réduira de 25% les transactions les plus courantes à 2 entrées et 2 sorties. Nous verrons également une diminution de 10% du temps de vérification.

Mais c'est quoi exactement CLSAG ? Que fait-il et en quoi diffère-t-il de l'ancienne version, MLSAG ? Prenons une minute pour nous rappeler le pourquoi et le comment des signatures de cercle afin de mieux comprendre ce concept. Les signatures de cercle permettent des entrées non interactives et indiscernables par des observateurs extérieurs grâce à l'utilisation d'ensembles d'anonymat sélectionnés par le signataire des sorties précédentes. En termes simples, cela permet à un utilisateur de masquer ses sorties utilisées dans une transaction à côté de sorties non liées, et il peut faire tout cela sans que personne d'autre n'y participe. Tout ce dont vous avez besoin est une copie de la blockchain. Chacune de ces sorties semble généralement être également susceptible d'être celle qui est réellement envoyée, masquant ainsi les métadonnées sur l'expéditeur.

Cela pose un petit problème, cependant. Et si un utilisateur devait construire une signature de cercle avec toutes les sorties leurres ? Comment quelqu'un saurait-il que l'expéditeur inconnu n'a pas le pouvoir d'en envoyer ? Cet utilisateur pourrait-il dépenser de l'argent factice ? La réponse est non. La signature de cercle comprend une méthode pour prouver qu'au moins une des sorties appartient à l'expéditeur inconnu, sans révéler de laquelle il s'agit. En fait, CLSAG et MLSAG (désormais connus sous le nom de SAG) sont la partie de la signature de cercle qui le prouve. Fait intéressant, en même temps, cela prouve que le montant de la transaction, bien que caché derrière des transactions confidentielles (RingCT), s'équilibre. Que les SAG prouvent deux choses, d'abord qu'une sortie appartient à quelqu'un dans le cercle, et ensuite que la transaction s'équilibre, est important, et c'est là où se situent les économies de taille et de vérification. Si cela devient déroutant, ne vous inquiétez pas, nous verrons bientôt une analogie amusante et facile à comprendre.

L'ancien schéma de signature, MLSAG (Multilayered Linkable Spontaneous Anonymous Group) prouve les deux choses susmentionnées dans une signature de cercle, mais il le fait séparément. L'utilisation de calculs séparés pour les clés de signature et d'engagement signifie des opérations plus lentes. Un ordinateur moderne peut effectuer ces calculs en quelques millisecondes, ce qui ne semble pas beaucoup, et en effet, pour une transaction, ce n'est pas le cas. Mais lorsque l'on considère le nombre de transactions sur la blockchain Monero, et qu'un nœud se synchronisant à partir de zéro devra télécharger et vérifier chacune d'elles, les octets et les millisecondes commencent à s'accumuler rapidement.

CLSAG combine les calculs nécessaires pour prouver les deux en un seul, ainsi que d'effectuer le calcul des deux à la fois, et il le fait de manière sûre. Qu'est-ce que cela signifie d'une manière sûre ? Eh bien, pour clarifier cela et, espérons-le, donner plus de sens à tout cela, explorons cette analogie amusante promise.

Supposons que vous deviez vous rendre à la fois à l'épicerie et à la quincaillerie pour acheter deux choses différentes : de la nourriture et des produits de nettoyage toxiques. Vous ne voulez pas qu'ils se mélangent, car s'il y avait un accident, les produits chimiques se répandraient sur les aliments, les rendant non comestibles. Vous décidez d'agir en toute sécurité et conduisez de votre maison à l'épicerie, achetez la nourriture, puis retournez chez vous. Ce n'est qu'après avoir déchargé la nourriture que vous remontez dans la voiture, que vous vous rendez à la quincaillerie et que vous rentrez chez vous avec les produits chimiques. Vous avez effectué deux voyages distincts pour assurer la sécurité de tous les achats. Bien qu'il soit en effet sûr, il est inefficace. Cela représente MLSAG, où deux ensembles différents de calculs sont stockés et deux « voyages » différents sont effectués pour les calculer. 

Vous décidez cependant que vous voulez un moyen plus rapide de le faire. C'est trop de temps perdu. Bien sûr, le faire une ou deux fois ne va pas vous ruiner la vie, mais avoir à le faire encore et encore, les heures commencent à s'accumuler. Vous commencez à vous demander si vous pouvez faire un seul voyage à la place. De votre maison, à l'épicerie, à la quincaillerie et à la maison. Vous ne pouvez pas tout jeter dans votre voiture au hasard. Ce n'est pas prudent. Au lieu de cela, vous désignez différents endroits dans votre voiture pour différentes choses et vous vous assurez que tout rentre parfaitement à sa place. Ce faisant, vous pouvez effectuer un voyage en toute sécurité dans les deux magasins et éloigner les objets les uns des autres. Cela représente le CLSAG. Il n'y a maintenant qu'un seul ensemble de mathématiques stockées dans cette transaction pour prouver ces deux choses, et c'est fait de manière à ce qu'elles n'interfèrent pas l'une avec l'autre. Un voyage doit encore être fait, mais vous en avez réduit considérablement le nombre.

Tout cela semble assez excitant. Est-il possible de trouver d'autres raccourcis, ou d'autres moyens de gagner du temps et de l'espace ? La réponse est oui et non. Selon les chercheurs actuels de MRL, il n'est probablement pas possible de modifier davantage les constructions de type SAG pour une meilleure taille ou vitesse ; cependant, d'autres constructions comme Arcturus, Omniring, RCT3 ou Triptych produisent de bien meilleurs avantages de passage à l'échelle et de vérification de la taille en utilisant différentes méthodes mathématiques. Cependant, chacune de ces approches « nouvelle génération » des protocoles de signature ambigus comporte ses propres compromis dans les détails de mise en œuvre et fait l'objet de recherches et d'investigations actives.

Après tout, Monero innove toujours.

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

  * [Pourquoi Monero a une émission résiduelle](/knowledge/monero-tail-emission)/

  * [Une brève histoire de Monero](/knowledge/monero-history)/

  * [Wired Magazine se trompe sur Monero, voici pourquoi](/knowledge/wired-article-debunked)/

  * [Démystification des 15 principaux mythes et inquiétudes au sujet de Monero](/knowledge/monero-myths-debunked)/

  * [Comment Dandelion++ garde les origines des transactions de Monero privées](/knowledge/monero-dandelion)/

  * [Pourquoi Monero est Open Source et décentralisé](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Le minage de Monero : ce qui rend RandomX si spécial](/knowledge/monero-mining-randomx)/

  * [Pourquoi Monero est meilleur que Dash, Zcash, Zcoin (même avec Lelantus), Grin et les mélangeurs Bitcoin comme Wasabi (mis à jour en mai 2020)](/knowledge/why-monero-is-better)/

Ressources complémentaires