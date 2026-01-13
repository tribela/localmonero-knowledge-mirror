---
title: "Comment les sous-adresses Monero empêchent la mise en correspondance d'identités"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero a toujours trouvé des moyens innovants pour résoudre les problèmes difficiles sur le sujet de la confidentialité. Souvent, ces innovations conduisent à d'autres innovations, et parfois ces technologies résultantes peuvent même être utilisées pour des cas d'utilisation non envisagés auparavant. Cela n'est nulle part mieux illustré que dans le cas de la technologie des sous-adresses de Monero.

Considérez un problème de confidentialité hypothétique, dans lequel l'utilisation d'une adresse sur plusieurs platesformes par des personnes apparemment sans rapport peut entraîner la connaissance de la relation et la désanonymisation de ces personnes. En termes simples, si vous étiez une personne nommée Mme Michu et que vous vendiez des pommes contre du Bitcoin, vous pourriez publier votre adresse Bitcoin dans un lieu public pour que les clients vous paient. Disons que l'adresse commence par la chaîne alphanumérique 7XybV3… . Mais en mettant de côté le risque évident pour la vie privée et la confidentialité que quiconque puisse vérifier votre solde Bitcoin et voir combien vous avez vendu, il y a un second risque, dont on ne parle pas souvent. Disons que vous étiez également un hacker clandestin du nom de l33tz0r. Vous faites un travail de dénonciation, informez une population sans méfiance de la corruption du gouvernement, et il est impératif que vous gardiez votre identité secrète. Vous acceptez les dons en Bitcoin pour votre travail et publiez l'adresse sur un forum public. C'est à la même adresse que vous acceptez l'argent de vos clients pour les pommes. L'adresse qui commence par 7XybV3… .

Une attaque de désanonymisation simple mais dévastatrice consisterait à utiliser un moteur de recherche Internet pour rechercher votre adresse Bitcoin. Mettre l'adresse de 7XybV3… dans le moteur de recherche fait apparaître deux résultats différents. L'entreprise de vente de pommes, et l33tz0r. C'est suffisant pour relier les deux identités et désanonymiser l33tz0r, avec des conséquences potentiellement effrayantes de la part des pouvoirs en place.

Il est important de noter que cette attaque est AUSSI possible avec Monero. Même si Monero cache la plupart des données en chaîne, cette attaque n'en utilise aucune. Elle utilise uniquement l'adresse, qui doit être partagée afin de recevoir le paiement. Publiquement en cas de dons anonymes. C'est un moyen potentiel par lequel les utilisateurs de Monero peuvent involontairement porter atteinte à leur vie privée et leur confidentialité, et c'est aussi un exemple de la façon dont, même si Monero est au premier rang en matière de conservation de la confidentialité, il n'est pas à l'épreuve des balles.

La manière habituelle de contourner ce problème consistait à posséder plusieurs portefeuilles. Avec différentes adresses publiées pour chaque identité (ou cas d'utilisation), elles ne peuvent pas être reliées. Mais cette confidentialité ne tient que si l'utilisateur ne les mélange jamais. L'affichage accidentel d'une mauvaise adresse aurait les mêmes effets mise en relation. De plus, la phrase mnémonique de chaque adresse doit être conservée en toute sécurité, ce qui augmente le travail d'« infosec » (sécurisation des informations) nécessaire à chaque nouveau portefeuille créé.

La solution de Monero consistait en la mise en œuvre des sous-adresses. La possibilité de créer un nombre absolument énorme d'adresses sous l'adresse principale, en l'utilisant comme une sorte de graine. Chaque sous-adresse générée peut accepter Monero, et tout va dans le même portefeuille. En utilisant cette méthode, le nombre d'identités pouvant être exploitées sous une même adresse est énorme tout en minimisant le travail d'infosec. Ces adresses ne sont pas non plus mathématiquement liées, donc à moins que l'utilisateur ne crie la relation entre ses adresses au monde, un observateur extérieur aura beaucoup de difficulté à les relier entre elles.

Mais un autre cas d'utilisation intéressant a émergé des sous-adresses ; comme option de remplacement des identifiants de paiement universellement détestés.

Les identifiants de paiement étaient un moyen pour les marchands d'identifier quel client avait envoyé quel paiement. Étant donné que les informations des transaction avec Monero sont masquées sur la chaîne, le destinataire d'une transaction n'est pas en mesure de voir quelle adresse l'a envoyée. Cela signifie que s'il y a des articles à prix similaire et plusieurs commandes, il peut devenir impossible d'identifier qui a envoyé quoi. Les identifiants de paiement sont une chaîne unique et aléatoire générée par le marchand et donnée au client. Le client l'ajoute dans un champ séparé lors de l'envoi de la transaction. Cette chaîne aléatoire est placée sur la blockchain dans le cadre de la transaction, et de cette façon, le commerçant est en mesure d'identifier et de trier les transactions entrantes.

Cette méthode présentait plusieurs défauts. Premièrement, cela nuit à l'uniformité des données en chaîne. Des métadonnées supplémentaires et uniques peuvent différencier certaines transactions dans la foule, permettant ainsi une analyse heuristique. Cela est particulièrement vrai lorsque ces métadonnées ne sont pas rendues obligatoires pour tous. Rendre cela obligatoire pour tout le monde ajouterait de l'espace inutile à la blockchain, et n'a pas été poursuivi. De plus, si un identifiant de paiement était réutilisé pour une raison quelconque, il serait trivial de déterminer deux transactions comme étant connectées. Cela se produisait généralement avec les dépôts d'échange, et n'importe qui pouvait facilement lier les transactions comme étant à la fois un dépôt sur un échange et d'une personne en particulier.

Deuxièmement, d'un point de vue de l'expérience utilisateur, les identifiants de paiement créent une deuxième étape à laquelle les utilisateurs provenant d'autres crypto-monnaies ne sont pas habitués, et que donc si ceux-ci ne les utilisent pas ou les oublient, cela cause un énorme casse-tête au commerçant qui doit identifier ces transactions par d'autres moyens . Cela se faisait généralement en parlant directement avec chaque client qui avait oublié de mettre l'identifiant de paiement et en confirmant d'autres informations d'identification qu'eux seuls pouvaient connaître, comme une combinaison du montant, de la date d'envoi et de l'identifiant de transaction.

Cette étape supplémentaire a été négligée par beaucoup de personnes, et c'en est arrivé au point où certains échanges ont commencé à facturer des frais aux clients si leur argent devait être récupéré manuellement en raison de l'oubli d'un identifiant de paiement. D'autres serraient les dents et avalaient les frais d'assistance supplémentaires, mais personne n'en était content.

Il y avait une solution à cela, les adresses intégrées, qui fusionnaient l'adresse et l'identifiant de paiement en une seule chaîne de caractères, de sorte qu'il ne pouvait pas être oublié, mais l'adoption était assez faible, malgré les avantages que les commerçants auraient reçus en l'incluant. 

Dans une tournure des événements intéressante, les sous-adresses sont arrivées pour sauver la situation. La possibilité de générer de grandes quantités de sous-adresses par adresse principale et d'identifier quelles transactions sont entrées dans quelles sous-adresses a permis aux commerçants de se débarrasser des identifiants de paiement de manière élégante, tout en adoptant la nouvelle génération de technologie Monero. Depuis lors, la plupart des échanges et des outils marchands sont passés aux sous-adresses comme principal moyen d'identification des transactions.

Ce qui a commencé comme une solution à un problème de confidentialité s'est transformé en quelque chose ayant une portée bien plus grande, qui a résolu un problème majeur d'expérience utilisateur pour les commerçants et les clients. L'innovation engendre plus d'innovation, ce qui peut souvent faire boule de neige et se traduire en bénéfices inattendus pour tout le monde. Monero l'a vu maintes et maintes fois et déploie de grands efforts pour innover dans le domaine de la blockchain. Qui sait quelles autres choses nous pouvons réaliser ensemble ?

Ressources complémentaires

  * [Comment Monero favorise de manière unique les économies circulaires](/knowledge/monero-circular-economies/)

  * [Les signatures de cercle de Monero face à CoinJoin comme dans Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

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